---
otero_id: 20569
otero_key: "SKREP2Z2"
title: "Jailbreaking in closed two-sided platforms"
authors: "Yunhao Liu; Gengzhong Feng; Yangyang Sun; Xiangyin Kong"
year: "2023"
journal: "Information & Management"
doi: "10.1016/j.im.2023.103859"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Jailbreaking in closed two-sided platforms

Yunhao Liu <sup>a,b</sup>, Gengzhong Feng <sup>a</sup>, Yangyang Sun <sup>c,\*</sup>, Xiangyin Kong d

<sup>a</sup> School of Management, Xi’an Jiaotong University, Xi’an, China

<sup>b</sup> School of Data Science, City University of Hong Kong, Hong Kong, China

<sup>c</sup> School of Economics and Management, Nanjing University of Science and Technology, Nanjing, China

<sup>d</sup> International Institute of Finance, School of Management, University of Science and Technology of China, Hefei, China

## A R T I C L E I N F O

Keywords: Closed two-sided platforms Jailbreaking Indirect network effects Piracy

## A B S T R A C T

Jailbreaking, which refers to security-cracking behavior targeted at systems, threatens closed two-sided plat forms. By allowing customers to access unauthorised content freely, jailbreaking may hurt developers’ enthu siasm and have complicated influences on the platform’s profit. We develop an analytical model to investigate jailbreaking’s influence on closed platforms. The findings reveal that platforms will tolerate jailbreaking only when the customers’ utility suffers a slight decline after jailbreaking. We also prove that jailbreaking hurts the closed platform’s profit. However, when bringing adequate additional benefits for customers beyond free con tent, jailbreaking can raise the platform’s profit. Our results are qualitatively tested in several scenarios.

## 1. Introduction

The two-sided platform, which acts as a medium for connecting consumer groups and content developers, has become a significant mainstay in digital content sales. By creating an integrated environment, such a platform effectively facilitates the provision of products and services for users by developer firms, stimulating consumer demand. However, similar to other information technology (IT) providers, twosided platforms are quite bothered by piracy in routine operations. Currently, piracy brings considerable hurt to the profit-earning of the IT industry, and it has become one of their major concerns. The Global Software Survey Report by the Business Software Alliance [1] pointed out that unlicensed software was used worldwide at alarming rates: 37% in 2018. Besides that, Revenera’s calculations regarding unauthorised software use showed that it caused \$19.8 billion in lost revenue for software suppliers in 2022 [2].

In response to piracy, the platforms usually put much effort into digital rights management (DRM). According to the magnitude of the DRM strictness, platforms can be categorized into different types [3]. Those executing the lowest level of DRM can be called open(-sourced) platforms. In contrast, closed two-sided platforms refer to those adopt ing the highest level of DRM. Only authorized content from providers can sell and run on a closed two-sided platform, effectively preventing the frequent occurrence of piracy. Representative platforms include the operating system IOS, the game console PlayStation, and many others.

However, closed two-sided platforms are not always unbreakable. Customers can bypass the DRM and crack the platform by adopting “jailbreaking” techniques. Executing these, customers can access much content without being charged and enjoy partial platform functions. According to Forbes [4], in 2014, the percentage of iPhone (the cell phone which uses the IOS system) jailbreaking rose from 12.2% in July to 13.6% in September. Moreover, a vulnerability discovered in 2020 made almost every iPhone able to be jailbroken [5].

The impact of jailbreaking on the closed two-sided platform’s reve nue is complicated. On the one hand, the platform can earn profits from customers accessing both genuine and unauthorised content since an initial purchase is still needed. Hence, from the perspective of profit ability, the platform can utilize jailbreaking by focusing on enlarging the whole consumer group. On the other hand, because of the indirect network effects between the two sides, more jailbreaking prevents content providers from deriving profits from customers, thus driving the providers away. This effect hurts the customers’ willingness to purchase and eventually harms the platform’s revenue stream. In such a situation, the optimal pricing decision becomes a critical issue for the closed twosided platform to regulate quantities of consumers and developers and optimize profit.

The diversified influence of jailbreaking poses another significant question: Can jailbreaking benefit the platform’s profit? In practice, most platforms have a very negative attitude toward jailbreaking. For example, game consoles have taken rigorous technical measures to block this kind of behavior. The successful jailbreaking of PlayStation 4 first happened four years after its release, and the bug was fixed very soon [6]. However, several closed platforms, such as mobile phone systems, exhibit a mild attitude towards jailbreaking. Previous academic research provides evidence for the positive effect of piracy on IT providers under certain circumstances [7,8]. Hence, further investigation is warranted about whether the platforms should tolerate jailbreaking behavior.

Reviewing the previous research on platforms, we find that although many works consider piracy behaviors in the platform environment, only limited studies explore the influence of jailbreaking on closed platforms. Thus, this paper is devoted to addressing the following research questions:

1 In the presence of consumer jailbreaking threats, what market situ ations do closed two-sided platforms face, and what are the corre sponding optimal pricing decisions?

2 How does jailbreaking influence the platform’s profit?

3 Should the closed platform tolerate jailbreaking under certain conditions?

To address the questions above, we build an analytical model to describe the utilities and demands of two sides, customers and content developers, and investigate optimal pricing decisions of closed twosided platforms facing jailbreaking threats. Based on the results, we discuss a significant issue by comparing the price and profit with those in our benchmark case (no jailbreaking exists in the market): Can the platform be better off in profitability with no jailbreaking? We also study the platform’s subsidizing decision towards content providers and identify the influencing mechanism of several fundamental factors on the overall profit. With respect to the piracy rate of concern to many parties, we also give definitions and conduct comparative statics anal ysis. Finally, we extend the research such as considering the additional benefits brought by jailbreaking, resulting in several new managerial insights for platforms.

The major conclusions of our study are as follows. According to the magnitude of the consumer-utility discount resulting from jailbreaking, we distinguish two market situations, and the corresponding optimal license and access fees are determined. When the indirect network effect is relatively strong, the platform should subsidize the content providers. A significant finding emphasized by this paper is that an absence of jailbreaking would be better for the platform’s profit, suggesting strict control of consumer jailbreaking behavior. Searching for the reasons, we find that compared with the network effects discussed in previous piracy literature, indirect network effects cannot help two-sided platforms earn extra profits from jailbreaking. These conclusions are proved valid under some other scenarios such as developers deciding the content price independently. However, if jailbreaking can bring considerable addi tional benefits for customers beyond the free content, things change such that tolerating jailbreaking may be the optimal option for closed platforms.

The remainder of this paper is structured as follows. In Section 2, we summarize the relevant literature and clarify the theoretical contribu tions by comparing this work with related publications. Section 3 gives the basic model settings, analyzes the software firm’s optimal pricing in the benchmark case where no jailbreaking exists, and then investigates the market equilibrium in the presence of jailbreaking threats. Section 4 contains an analysis to derive the optimal pricing strategy in the pres ence of jailbreaking. A profit comparison is also conducted to determine the effect of jailbreaking existing. In Section 5, we extend the research by considering several other significant scenarios. Finally, Section 6 summarizes the study and offers future research suggestions.

## 2. Literature review

Three main literature streams are relevant to our research, including two-sided platforms, piracy, and their intersection—piracy in two-sided

platforms.

## 2.1. Two-sided platform

As one of the most significant business innovations in past decades, the platform mode has drawn massive attention from enterprises and researchers since it emerged. Rochet and Tirole [9] were among the first to study this type of platform by generating a theoretical model to describe the participant groups’ decision-making process. They explored how demand elasticity affects the pricing strategy under both monop olistic and competitive situations, and their conclusions unveiled plat form selling’s superiority compared with monopolistic selling. The fundamental features they captured, especially network externality, greatly inspired future research. Based on their work, Armstrong [10] further investigated the platform’s optimal pricing in the competitive environment, mainly considering two cases: agents joining only one platform or joining both. The analytical results further established the significant influence of two-sided network externalities on the plat form’s decisions. Eisenmann et al. [3] directly focused on the indirect (two-sided) network effects, discovering that they might motivate the platform to subsidize one side of the market to attract the other side. In addition to pricing decisions, the conclusions presented by Anderson Jr et al. [11] illustrated the moderating effect of two-sided network ex ternalities on the platform’s quality performance investment in different market scenarios. With the development of platform economics, some other critical issues and technologies in the platform environment were gradually studied, such as the choice between first-party content and third-party content provision [12–14], adoption of one-sided value-add service [15,16], optimal pricing under sharing economies [17,18], and the introduction of the blockchain technology [19].

One problem in particular has drawn longstanding attention from researchers: platform openness. Early works, like Economides and Kat samakas [20], classified platforms into two major types, open-source and proprietary platforms, according to the scale of the platform’s ac cess rights. Through analysis, they found that these two kinds of plat forms exhibit sharp differences in their optimal pricing strategy and profit-earning. Following their work, Kort and Zaccour [21] analyzed the platform’s open-code decisions and found that more motivation exists to open the source code as the quality of complementary products in the market increases. In addition to price decisions, Casadesus-Ma sanell and Llanes [22] studied the optimal quality investment decision for open-source and proprietary platforms, and the results show that open platforms may even need more quality investment than closed platforms.

In summary, this series of studies’ conclusions convey that the platform openness level (mainly controlled by itself) strongly relates to its pricing and quality decision-making. However, most research on closed platforms has ignored the influence of the aforementioned critical factor: indirect network effects. Hence, in this paper, we focus on the closed two-sided platform’s pricing strategy while considering indirect network effects. By investigating whether jailbreaking should be toler ated for closed platforms in the presence of indirect network effects, we aim to enrich the previous literature on two-sided platforms.

## 2.2. Piracy and jailbreaking

As an alternative to legally obtaining genuine digital goods, piracy has drawn massive attention from researchers. Views on it are consis tently enriched, and a consensus has gradually been achieved: piracy can be tolerated under some conditions. even though the unauthorised goods hurt sales through the legal channel. Takeyama [23] first discovered that a firm should allow piracy when the network effects are adequately strong. Shy and Thisse [24] extended their research into the duopoly setting where support and purchase are bundled, achieving similar results that software firms have incentives to tolerate piracy when network effects are strong. Some researchers found that under certain conditions, piracy can play a role in raising both the firm’s profit and social welfare. Jain [25] determined that piracy could help improve firms’ profits and even lift social welfare when copyright protection served as a coordination device in the competitive environment. In the digital supply chain environment, Kim et al. [7] revealed that piracy could alleviate the problem of double marginalization under certain conditions, jointly improving the total profit and maximizing social welfare.

Although piracy can be tolerated under certain conditions, the measures against it still have research significance due to its harm to the consumption habits of genuine products. Versioning could be a solution. Chellappa and Shivendu [26] built a two-stage model to analyze pricing strategy in the presence of piracy and proposed that providing samples could be an effective method of seizing customers from pirated products. Based on that work, Wu and Chen [27] presented the feasible conditions for applying versioning in controlling piracy according to the magnitude of related costs. DRM technology has also been pervasively adopted. Sundararajan [28] first proposed that even though executing DRM may reduce the value of legal products, a proper level of DRM could signif icantly protect sales and profit. Their analytical results uncovered the relationship between the price discrimination mode and the optimal DRM level. Since then, a series of works have continued to explore the optimal DRM level in collaborative structures [29], under government copyright enforcement [30], in the presence of consumer uncertainty for product value [31], and in other scenarios.

When firms execute the highest level of DRM, the piracy behavior to circumvent DRM is named “jailbreaking”. Gopal and Gupta [32] first systematically introduced the motivations and process of jailbreaking behavior on iPhones, and Chao et al. [33] conducted an empirical study to show that jailbreaking’s key motivation was to install pirated content. However, the economic analysis of this kind of piracy behavior has been quite limited. Hence, our paper tries to investigate the influencing mechanism of jailbreaking on closed platforms’ price-setting and then explores the platforms’ attitude towards jailbreaking, aiming to expand this literature stream.

## 2.3. Piracy in the two-sided platforms

With the popularity of platform economics, piracy behavior has become growingly rampant since it can unfreeze users’ access rights to numerous types of content. In response to the need for analysis, Rasch and Wenzel [34] first constructed a model to introduce piracy into platform environment studies. Through analysis, they showed how the optimal prices charged for the two sides change when a conflict regarding protection level arises between software developers and platforms. Rasch and Wenzel [35] continued the study by classifying developers by their prominence. They declared that non-prominent developers might benefit from better protection provided by the plat form. Facing piracy, two-sided platforms may choose different measures to react. Nan et al. [36] suggested that the platform should adjust the protection level against piracy considering the magnitude of content sustainability. Aversa et al. [37] pointed out the feasibility of offering a free sample in a competitive environment. Ishihara and Muller [38] checked the platform’s outsourcing decisions in the presence of piracy, revealing that increasing outsourcing might help deter piracy.

However, concerning the closed two-sided platform’s pricing issue, the jailbreaking behaviors’ influence has yet to be discussed in the literature, generating a significant research gap. Till now, the work by Cavusoglu et al. [39] has been the only economic research to examine the influence of jailbreaking on platform sales, taking mobile systems as an example. By focusing on jailbreaking’s benefit of helping users remove the pre-installed bloatware, they showed that blocking jail breaking is not always preferable for mobile manufacturers. In that work, however, the significant factor of indirect network effects is not mentioned.

Compared with the previous literature, our work exhibits several prominent differences, bringing significant incremental contributions. Concerning the research problem, our work is devoted to exploring the influence of jailbreaking on closed platforms’ pricing decisions, aiming to fill the aforementioned gap in the intersection of platform and piracy literature. Concerning the research model, we integrate the traditional two-sided platform and piracy models in constructing our model framework, considering jailbreaking’s critical characteristics and indi rect network effects. In its conclusions, this paper presents results about jailbreaking’s influence on profit. Surprisingly, we find that no jail breaking is optimal for closed platforms’ profits due to the influence of indirect network effects. As a valuable supplement to prior piracy and two-sided platforms research, we believe that the insights uncovered in this paper can lay a solid theoretical foundation and offer constructive guidance for platforms’ future decision-making.

Table 1  
Summary of key notation.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $v$ </td><td>Customers&#x27; valuation of the closed two-sided platform</td></tr><tr><td> $k$ </td><td>Fee customers must pay for a unit of content ( $0 < k \leq 1$ )</td></tr><tr><td> $a$ </td><td>Total intensity of indirect network effects ( $0 \leq a \leq 1$ )</td></tr><tr><td> $b$ </td><td>Discount of customer utility stemming from jailbreaking ( $0 \leq b < 1$ )</td></tr><tr><td> $n_{c}, n_{d}$ </td><td>Active customers, content developers for the platform</td></tr><tr><td> $N_{D}$ </td><td>Total number of content developers( $0 < N_{D} \leq 1$ )</td></tr><tr><td> $n_{cr}, n_{cp}$ </td><td>Customers using the authorized, unauthorised content</td></tr><tr><td> $p_{c}, p_{d}$ </td><td>Access fee for customers, license fee for developers</td></tr><tr><td> $f$ </td><td>Developer&#x27;s cost to produce content ( $0 \leq f \leq 1$ )</td></tr><tr><td> $U_{c}, U_{uc}$ </td><td>Utilities of genuine, unauthorised customers</td></tr><tr><td> $r$ </td><td>Additional benefits stemming from jailbreaking ( $r \geq 0$ )</td></tr></table>

## 3. Model setup

In this section, we consider a monopolistic two-sided platform in the market facing the jailbreaking threats. The closed platform serves two sides: the content developers and customers. It acts as an intermediate and charges both groups: a license fee $p _ { d }$ to developers selling content on the platform and an access fee $p _ { c }$ to customers purchasing the platform. Here, negative prices indicate that the platform will subsidize the content developer. For simplicity, we consider neither the marginal costs of running the platform nor development costs. The platform also charges no marginal fees during the interaction between developers and cus tomers $[ 1 1 , 1 2 , 4 0 , 4 1 ]$ . According to Armstrong [10], there is no differ ence in platform profit if tariffs are levied based on a lump-sum or revenue-sharing marginal fees.<sup>1</sup>

Table 1 lists the main notation in the whole framework.<sup>2</sup>

## 3.1. Basic model settings

For simplicity in the following analysis, we normalize the population of customers willing to purchase the platform to 1. Each consumer has an intrinsic valuation of v for the closed platform, which is heteroge neous and uniformly distributed on [0, 1] (v ∈ U[0, 1]) [12,15]. Following Rochet and Tirole [9], we assume that the consumers can enjoy an average value $K ,$ , and the average price is k when purchasing a unit of content from the content provider. Thus, the net surplus they can obtain is $a = K$ − k, which can be defined as the indirect network effect. We assume both k and a are homogeneous and lie in [0, 1] [15]. For simplicity, we assume that consumers purchase just one unit of content from one provider in the platform [10,11]. Since there exist $n _ { d }$ active developers providing content, the net benefit customers can obtain is $a n _ { d } .$ The utility of customers accessing the platform is shown in Eq. (1).

$$
U _ {c} = v + a n _ {d} - p _ {c}\tag{1}
$$

Jailbreaking is another option for accessing content, an alternative to purchasing the content. When implementing this behavior, customers hope to bypass the DRM to link to the platform’s content without authorization. Chao et al. [33] empirically proved that the core purpose of jailbreaking was installing apps and services freely. In our model, we assume that customers jailbreaking the system aim to enjoy the unau thorised content without paying the fee k and do not obtain any other benefits.

However, when customers choose to jailbreak, their utilities suffer from this behavior. Unlike open platforms, closed two-sided platforms adopt quite strict DRM and can detect jailbreaking in most cases. Thus, jailbroken platforms usually will not be supported by manufacturers. For example, Apple refuses to provide warranty service to jailbroken devices even within the usual warranty period [42]. Besides this, jailbroken platforms often fail to provide certain functionalities available when using the original platform. Games on the jailbroken Nintendo Switches cannot connect to the Internet, or the machines will be banned instantly [43]. Similarly, when experiencing the content provided on jailbroken platforms, customers may have to bear harmful effects such as these. Therefore, it can be assumed that the overall utility of customers de grades due to their jailbreaking [7,34]. We use b $( 0 < b < 1 )$ to denote the consumer-utility discount. The values of the platform and the con tent face the same level of consumer-utility discount when jailbreaking exists [23,44,45]. Hence, the consumer’s valuation of the platform itself becomes bv, and the unauthorised content’s value is $b ( a + k ) n _ { d } .$ . In summary, the utility function of these unauthorised customers, repre sented by the subscript uc, can be expressed as Eq. (2). Here, following Ishihara and Muller [38], we choose to omit the jailbreaking cost.

$$
U _ {u c} = b (v + (a + k) n _ {d}) - p _ {c}\tag{2}
$$

On the opposite side of the platform, a total number of $N _ { D }$ developers are ready to provide content. We assume $0 < N _ { D } < 1$ , which means the developer group size that is smaller than the platform’s user size, which agrees with reality. Content developers’ profits only stream from the sales of authorized content, so we assume that developers can earn an average income of $k$ from a customer accessing genuine content. Through calculation, we can discover an intuitive result that when customers jailbreak the platform, they always choose not to pay for the content. The reason lies in that the utility of paying after jailbreaking $( b \nu + a n _ { d } - p _ { c } )$ ) is always inferior to accessing the authorized content (v + $a n _ { d } - p _ { c } )$ ). Hence, the developers’ total income is $k n _ { c r } ,$ depending on the number of authorized users, $n _ { c r } .$ The content developer bears two kinds of costs. The first is the license fee $p _ { d }$ mentioned above. The other, called the development cost $f ,$ captures the developer’s technical level and engineering efficiency in producing content. We assume that it is uni formly distributed on [0, 1]. Then, the overall profit of the content developer is formulated in Eq. (3).

$$
U _ {d} = n _ {c r} k - p _ {d} - f\tag{3}
$$

The closed two-sided platform sets prices, $p _ { c }$ and $p _ { d } ,$ for customers and developers, respectively, sides to maximize its profit. Thus, the profit optimization problem can be defined as:

$$
\max _ {p _ {c}, p _ {d}} \Pi (p _ {c}, p _ {d}) = n _ {c} p _ {c} + n _ {d} p _ {d}\tag{4}
$$

In the whole process, the game sequence among different parties can be illustrated as follows:

Step 1. The two-sided platform decides the access fee for customers and the license fee for content developers.

Step 2. The content developers decide whether to join the platform. Simultaneously, customers choose between buying and then jailbreaking, buying but not jailbreaking, and not doing anything.

Step 3. The purchasing is finished, and the platform starts earning profit.

## 3.2. The benchmark: no jailbreaking exists

Currently, a noteworthy business situation is that the severity of jailbreaking varies among different platforms. Some platforms put much effort into controlling customers’ piracy behavior by executing technical measures or cultivating a consumer culture. The results can be surpris ingly effective; jailbreaking on the game consoles PS4 and XBOX One was not widespread during the product life cycle. In comparison, other products encounter difficulties in eliminating piracy, such as Apple’s IOS system, and jailbreaking can often be observed. The benchmark scenario in our study is that the closed platform encounters no jail breaking threats.

When refusing to jailbreak after accessing the platform, the utility consumers can obtain is shown in Eq. (1). Letting $U _ { c } = 0 ,$ , we derive the marginal consumer type indifferent between purchasing the platform or not as $\nu ^ { * } = p _ { c } - a n _ { d }$ . Thus, the number of active customers in the market is $n _ { c } = 1 - \nu ^ { * } = 1 - p _ { c } + a n _ { d } .$ . Since no jailbreaking exists in the market, $n _ { c r } = n _ { c }$ . Similarly, the marginal cost below which the content developer is willing to join can be derived as $f ^ { * } = n _ { c } k - p _ { d }$ by letting $U _ { d } = 0 .$ Hence, the number of active developers is $n _ { d } = f ^ { * } N _ { D } = ( n _ { c } k - p _ { d } ) N _ { D } .$ Substituting $n _ { c }$ and $n _ { d }$ with each other and then solving, we derive the size of customer and developer groups, dependent on prices, in the following equations.

$$
n _ {c} = \frac {1 - a p _ {d} N _ {D} - p _ {c}}{1 - a k N _ {D}}, n _ {d} = \frac {N _ {D} (k - p _ {c} k - p _ {d})}{1 - a k N _ {D}}\tag{5}
$$

The closed two-sided platform sets prices to maximize its overall profit, and the optimization problem can be defined as:

$$
\max _ {p _ {c}, p _ {d}} \Pi (p _ {c}, p _ {d}) = n _ {c} p _ {c} + n _ {d} p _ {d}\tag{6}
$$

The solutions lead to Lemma 1, which presents the platform’s optimal pricing decisions in the absence of jailbreaking. Here the subscript nj denotes the no jailbreaking case.

Lemma 1. When the platform runs without the jailbreaking threats, the optimal license fee is $\begin{array} { r } { p _ { d n j } ^ { * } = \frac { k - a } { 4 - ( k + a ) ^ { 2 } N _ { D } } } \end{array}$ and the optimal access fee is $\begin{array} { r } { p _ { c n j } ^ { * } = \frac { 2 - k ( a + k ) N _ { D } } { 4 - ( k + a ) ^ { 2 } N _ { D } } . } \end{array}$ . The corresponding profit of the platform is $\begin{array} { r } { \pi _ { n j } ^ { * } = \frac { 1 } { 4 - ( k + a ) ^ { 2 } N _ { D } } . } \end{array}$

Lemma 1 uncovers an interesting feature of pricing: the platform will subsidize the developers when the indirect network effect is strong enough $( a > k )$ . In this case, the content is adequately attractive to customers, so subsidizing can help maintain the participation of de velopers when customers move to unauthorised content on a large scale, which further encourages customer purchasing. Eventually, the plat form can find that the income from consumer purchasing compensates for and even exceeds the loss on the developer side.

## 3.3. Market equilibrium analysis in the presence of jailbreaking

In this section, we investigate customers’ choices among accessing authorized content, jailbreaking after purchasing, and doing nothing. Specifically, the market segmentation of customer and developer sides depends on the conditions of Individual Rationality (IR) and Incentive Compatibility (IC). The utility functions of consumers accessing genuine content and unauthorised content are $U _ { c } = \pmb { \nu } + \pmb { a n _ { d } } - p _ { c }$ and $U _ { u c } = b ( \nu +$ $( a + k ) n _ { d } ) - p _ { c }$ , respectively, and we clarify the consumer choices by applying these to solve the IR and IC conditions.

If customers choose not to jailbreak the platform after purchasing, their types satisfy the following inequalities. Here $\nu _ { 1 }$ indicates the marginal consumer indifferent between purchasing the platform or not, and $\nu _ { 3 }$ is the marginal consumer indifferent between jailbreaking or not after buying the platform.

$$
I R _ {L}: U _ {c} > 0 \Leftrightarrow v > v _ {1} = p _ {c} - a n _ {d}
$$

$$
I C _ {L}: U _ {c} > U _ {u c} \Leftrightarrow v > v _ {3} = \frac {(b (a + k) - a) n _ {d}}{1 - b}
$$

Similarly, if a customer decides to jailbreak, their type meets the following conditions. Here $\nu _ { 2 }$ represents the marginal consumer indif ferent between jailbreaking or not.

$$
I R _ {J}: U _ {u c} > 0 \Leftrightarrow v > v _ {2} = \frac {p _ {c} - b (a + k) n _ {d}}{b}
$$

$$
I C _ {J}: U _ {u c} > U _ {c} \Leftrightarrow v <   v _ {3} = \frac {(b (a + k) - a) n _ {d}}{1 - b}
$$

By comparing these indifference points, we discover that when $\nu _ { 2 }$ $> \nu _ { 1 : }$ , no customer chooses to jailbreak after purchasing the platform. Fig. 1 illustrates the only possible market segmentation, and we call this the “no jailbreaking region.” When $\nu _ { 2 } \leq \nu _ { 1 }$ , there exist two situations based on the relative magnitude between v and 1. $\mathrm { I f } \ \nu _ { 3 } < 1 $ , the con sumer distributed in $[ \nu _ { 3 } ,$ , 1] is motivated to jailbreak the platform, and the consumer distributed in $[ \nu _ { 2 } , \nu _ { 3 } ]$ will buy the platform, but they may not jailbreak the platform based on $I C _ { J }$ condition. Hence, customers accessing genuine and unauthorised content coexist in the market. We define this case as the “partial jailbreaking region,” shown in Fig. 2. When $\nu _ { 3 } \geq 1$ , an extreme case emerges that customers who purchase the platform all jailbreak. This “full jailbreaking region” is shown in Fig. 3.

In our work, the “full jailbreaking region,” which exists when $\nu _ { 3 } \geq { } .$ 1, is regarded as not feasible for further consideration. That is because, in this case, all consumers accessing the platform choose to jailbreak to obtain unauthorised content, meaning that the DRM maintained by the platform is no longer valid. In other words, the platform cannot operate as a closed platform. Moreover, it has been extremely hard to find business cases in recent years that meet the requirements of this “full jailbreaking region.” Thus to focus on our research issues and address them precisely, we propose the following Assumption 1, which means that there always exist partial customers who choose genuine content after purchasing the platform.

Assumption 1. The full jailbreaking case is not feasible, so we do not consider $\nu _ { 3 } < 1$

Based on the solutions of the IR and IC conditions, we derive the exact numbers of customers purchasing the genuine content $( n _ { c r } ) ,$ , jail breaking for unauthorised content $( n _ { c p } )$ , and accessing the platform $( n _ { c } )$ under the two cases, respectively, which are shown in the following Eqs. (7) and 8.

$$
\text { Partial   jailbreaking } \left\{ \begin{array}{l} n _ {c r} = a n _ {d} + \frac {1 - b - b k n _ {d}}{1 - b} \\ n _ {c p} = \frac {b (k n _ {d} + p _ {c}) - p _ {c}}{b (1 - b)} v _ {2} <   v _ {1} \text { and } v _ {3} <   1 \\ n _ {c} = 1 + \frac {(a + k) b n _ {d} - p _ {c}}{b} \end{array} \right.\tag{7}
$$

$$
\text { No   jailbreaking } \left\{ \begin{array}{l l} n _ {c r} = 1 + a n _ {d} - p _ {c} \\ n _ {c p} = 0 \\ n _ {c} = 1 + a n _ {d} - p _ {c} \end{array} \quad v _ {2} \geq v _ {1} \right.\tag{8}
$$

Next. we discuss the decisions of content developers. The number of developers participating in the platform can be derived as $n _ { d } = ( k n _ { c r } -$ $p _ { d } ) N _ { D }$ . We substitute this equation into the above Eqs. (7) and (8), and

![](/api/attachments/SKREP2Z2/fulltext/images/6d889d1b54926306d389a2c5b2594af1cf415f2873f0d17417efd9f75cd617b2.jpg)  
Fig. 1. Market segmentation of the “no jailbreaking” region.

![](/api/attachments/SKREP2Z2/fulltext/images/5c1ef8b761e7a3ffde8c1aff57b149e64418e36a390477aa6aa8a5ca1247929c.jpg)  
Fig. 2. Market segmentation of the “partial jailbreaking” region

![](/api/attachments/SKREP2Z2/fulltext/images/89c3de676e4f08b348a7944218178941d00f811a63627687680fa49e822c3dee.jpg)

Fig. 3. Market segmentation of the “full jailbreaking” region (not feasible in reality).

solve simultaneously for $n _ { c } , n _ { c r } ,$ , and $n _ { d } .$ . The results are displayed in Lemma 2.

Lemma 2. In the presence of jailbreaking, the numbers of authorized customers, content developers, and total active customers under two market situations are as follows:

$$
\text {Partial jailbreaking} \left\{ \begin{array}{c} n _ {c r} = \frac {1 - b + (\mathrm{bk} - \mathrm{a} (1 - \mathrm{b})) N _ {D} p _ {d}}{1 - b + k (b k - a (1 - b)) N _ {D}} \\ n _ {c p} = \frac {(1 - b) N _ {D} (k - p _ {d})}{1 - b + k (b k - a (1 - b)) N _ {D}} v _ {2 t} \langle 1 \text {and} v _ {1 t} \rangle 0 \\ n _ {c} = 1 - \frac {p _ {c}}{b} + \frac {(1 - b) (a + k) N _ {D} (k - p _ {d})}{1 - b + k (b k - a (1 - b)) N _ {D}} \end{array} \right.
$$

$$
\text { No   jailbreaking } \left\{ \begin{array}{c} n _ {c r} = \frac {1 - a p _ {d} N _ {D} - p _ {c}}{1 - a k N _ {D}} \\ n _ {c p} = \frac {N _ {D} (k (p _ {c} - 1) - p _ {d})}{1 - a k N _ {D}} \quad v _ {1 t} \leq 0 \\ n _ {c} = \frac {1 - a p _ {d} N _ {D} - p _ {c}}{1 - a k N _ {D}} \end{array} \right.
$$

$$
\text { Here, } \nu_ {1 t} = p _ {c} - \frac {b k N _ {D} (k - p _ {d})}{1 - b + k (b k - a (1 - b)) N _ {D}} \text { and } \nu_ {2 t} = \frac {N _ {D} (b k - a (1 - b)) (k - p _ {d})}{1 - b + k (b k - a (1 - b)) N _ {D}}
$$

## 4. Platform’s optimal pricing in the presence of jailbreaking

Based on the number of active customers and developers displayed in Lemma 2, we solve the platform’s profit maximization problem in this section. Through analysis, the optimal pricing decisions of the closed two-sided platform in the presence of jailbreaking are obtained and expressed as Proposition 1. According to the relative magnitude of the consumer-utility discount b caused by jailbreaking, two potential market situations exist, and the platform charges optimal fees correspondingly. Here we set $\begin{array} { r } { L _ { 1 } = 1 - \frac { 1 } { 2 } k ( a + k ) N _ { D } } \end{array}$ and $\begin{array} { r } { L _ { 2 } \ = \frac { 4 - 2 a k N _ { D } } { 4 - k ( a + k ) N _ { D } } } \end{array}$

Proposition 1. There exist two possible market situations that the closed two-sided platforms may encounter.

No Jailbreaking region: When the degradation of consumer utility led by jailbreaking is large $( 0 < b \leq L _ { 1 } ) _ { : }$ , all customers accessing the platform will pay for the content they experience, and the jailbreaking threats disappear. The platform sets the prices as

$$
\begin{array}{l} p _ {d} ^ {*} = \frac {k - a}{4 - (a + k) ^ {2} N _ {D}} \\ p _ {c} ^ {*} = \frac {2 - k (a + k) N _ {D}}{4 - (a + k) ^ {2} N _ {D}} \end{array}
$$

Partial jailbreaking region: When the consumer utility degradation caused by jailbreaking is moderate $( L _ { 1 } < b < m i n \{ L _ { 2 } , 1 \} )$ , some of the cus tomers accessing the platform will jailbreak $i t ,$ and this behavior will be tolerated. The optimal prices are:

$$
p _ {d} ^ {*} = \frac {(1 - b) ((2 - b) k - a b) - k ^ {2} (a (2 - b) - b k) N _ {D}}{4 (1 - b) - (4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)) N _ {D}}
$$

$$
p _ {c} ^ {*} = \frac {2 b (1 - b) + b k (k (1 + b) - a (1 - b)) N _ {D}}{4 (1 - b) - \left(4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)\right) N _ {D}}
$$

When b is small, the consumer utility faces a sharp decline, so jail breaking behavior becomes uneconomical. Hence, customers get no incentives to jailbreak, and the platform can set the fees without considering jailbreaking threats. We note from Proposition 1 that, in this case, the price-setting has no relationship with b. When b grows larger, some low-valuation customers may find it better to jailbreak and enjoy unauthorised content. When this happens, the platform finds it uneco nomical to prohibit jailbreaking by price-setting and prefers to tolerate it. Then the partial jailbreaking region emerges.

Next, we investigate the influence of jailbreaking on the platform’s pricing decisions by comparing the optimal prices in the partial jail breaking region and those in the benchmark, where no jailbreaking exists. The results are stated in Corollary 1.

Corollary 1. When the consumer-utility discount b satisfies the condition b $\scriptstyle < m i n \left( 1 , { \frac { 2 - 2 a k N _ { D } } { 2 - k ( a + k ) N _ { D } } } \right)$ , the optimal access fee p<sup>∗</sup> in the presence of jailbreaking is higher than that in the benchmark, while the optimal license $f e e p _ { d } ^ { * }$ is lower than in the benchmark. Otherwise, when $\begin{array} { r } { b > m i n \Big ( 1 , \frac { 2 - 2 a k N _ { D } } { 2 - k ( a + k ) N _ { D } } \Big ) , p _ { c } ^ { * } } \end{array}$ becomes lower than that in the benchmark, and $p _ { d } ^ { * }$ is higher than that in the benchmark.

When $\begin{array} { r } { b < m i n \Big ( 1 , \frac { 2 - 2 a k N _ { D } } { 2 - k ( a + k ) N _ { D } } \Big ) } \end{array}$ , to maintain a stable operation, the platform should charge a relatively low license fee or even subsidize to keep content developers from leaving. On the consumer side, since the platforms realize that many customers may purchase and then access unauthorised content, they prefer to charge a higher access fee than in the benchmark case to take advantage of the increasing customer group. Fig. 4 shows the price differences, where the parameter values are set as $a = 0 . 8 , b = 0 . 6 ,$ , and $N _ { D } = 0 . 8 .$ . It can be observed that when b is smaller than the threshold, the access fee $p _ { c n j }$ (license fee $p _ { d n j } )$ in the benchmark is lower (larger) than $p _ { c } \ ( p _ { d } )$ in the partial jailbreaking region.

To further explore the influence of jailbreaking on optimal prices, we turn our attention to the subsidization decision of platforms. Proposi tion 2 presents the results.

Proposition 2. In the partial jailbreaking region, the platform subsidizes the content developers when the indirect network effect intensity gets rela tively large $\begin{array} { r } { \left( \frac { k ( 2 + b ( b k ^ { 2 } N _ { D } - 3 ) ) } { b ( 1 - b ) + ( 2 - b ) k ^ { 2 } N _ { D } } < a < 1 \right) } \end{array}$

A larger intensity of indirect network effect a sharply strengthens the content’s attractiveness. In this case, if the platform insists on the high license fee, content developers’ revenue suffers from being charged by the platform and from the reduction of customers accessing genuine content. Then a large-scale retreat of developers further hurts cus tomers’ willingness to purchase, which poses a massive challenge for the platform. Hence, it is wise for the platform to provide a subsidy to maintain market viability. To illustrate this, we conduct the numerical experiment by setting parameter values as $k = 0 . 7 , b = 0 . 7 ,$ and $N _ { D } =$ 0.8. Fig. 5 demonstrates the results. We can find that when a exceeds the threshold, the platform subsidizes the developer group.

Next, we discuss the influence of jailbreaking on the platform’s profit. The optimal profit the platform can earn in the partial jail breaking region is:

$$
\Pi^ {*} = \frac {b (1 - b) + k ^ {2} N _ {D}}{4 (1 - b) - \left(4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)\right) N _ {D}}\tag{9}
$$

Abundant literature has shown that, under some circumstances, tolerating piracy can be economically optimal. For example, Conner and Rumelt [8] proved that positive network effects can make allowing pi racy more profitable than prohibiting it. Kim et al. [7] proposed that in the supply chain environment, there exists a particular scenario where both manufacturers and retailers can be better off in the presence of piracy than without it. However, by comparing the platform’s profit in the presence of jailbreaking with that in our benchmark, we obtain Proposition 3:

Proposition 3. Jailbreaking will hurt the closed two-sided platform’s profit.

The main reason for the above finding is that the indirect network effects do not act as simply as the positive network effects commonly discussed in the previous literature. Obviously, the platform’s attrac tiveness among customers increases as indirect network effects get stronger, and the sales are thus promoted. However, the decline of consumers using genuine content also discourages the developers participation. Thus, the revenue increase from the consumer side is counteracted by the loss caused by the developers leaving, hurting the whole profit. Eventually, the platform finds its profit is always highe with no jailbreaking than when jailbreaking exists.

In contrast with the previous studies proving that direct network effects can make the company benefit from piracy [8,23], we prove the following Corollary 2.

Corollary 2. The indirect network effects cannot make closed two-sided platforms benefit from jailbreaking in terms of profitability.

Corollary 2 offers significant managerial insights into platform op erations. If the purpose of customer jailbreaking is only to access unauthorised content, the platform should treat jailbreaking strictly to encourage only authorized access to content. For example, when cus tomers jailbreak the game consoles to enjoy pirated games, the company can take various measures to reduce their user experience, such as blocking the internet connection of detected jailbroken machines and refusing to honor a warranty. Put simply, eliminating jailbreaking threats is a wise option economically.<sup>3</sup>

We now turn to investigate the influencing mechanism of those exogenous factors on the platform profit. Conducting a comparative statics analysis, we obtain Proposition 4.

Proposition 4. In the partial jailbreaking region, the optimal profit of the platform satisfies the following:

(1) The profit increases as the total number of content developers $N _ { D }$ grows.

(2) The profit increases as the intensity of indirect network effects a grows.

(3) The profit decreases as the consumer-utility discount caused by jailbreaking b grows.

(4) When k is large $\left( \frac { 2 - b - b ^ { 2 } } { a N _ { D } } < k < 1 \right)$ , the profit decreases as the content fee k grows. Otherwise, the profit increases as k grows.

The influence of the number of developers, $N _ { D } ,$ on the platform profit is easy to understand. The expansion of the developer community brings more available content and can help attract more customers, including those willing to access authorized content. Thus, the developers find their income increases correspondingly and become more motivated to provide content, and the platform earns more from both sides. Con cerning the indirect network effect a, any increase in its intensity makes the content more valued and improves customers’ utilities irrespective of whether they jailbreak. Since the platform can stabilize the developer group through subsidizing, its overall profit can benefit from an increasing consumer group.

![](/api/attachments/SKREP2Z2/fulltext/images/1f54b3d2d47f8d0fcd56211c06c0300daf27172c6d472c080e38d456cb018069.jpg)  
Fig. 4. Differences of the access fees $p _ { c }$ (solid line) and license fees $p _ { d }$ (dashed line) with and without the presence of jailbreaking

![](/api/attachments/SKREP2Z2/fulltext/images/87b357ec33cc72e53fc0d19feb0483ff2aa4323735ee0fb73c768e6f93cbdd42.jpg)  
Fig. 5. Optimal prices in the partial jailbreaking region.

An increase in the consumer-utility discount b delivers two aspects of the effect. On the one hand, as the decline in utility becomes less apparent, the option of “purchasing and then jailbreaking” is perceived as more valuable. Thus, the platform can earn more due to the customer group’s enlargement, even though the proportion of customers access ing authorized content declines. On the other hand, more customers switching to unauthorised content magnifies the content developer’s potential loss and drives them away, cutting down the platform’s profit from this side and hurting the customers’ enthusiasm for purchasing. We discover that eventually, the latter effect dominates the former, resulting in a negative effect on profit, as part (3) of Proposition 4 states.

Part (4) of Proposition 4 includes relatively complicated results. As the customer’s unit content cost k increases, more developers are motivated to generate and provide content, which improves the plat form’s profit from the developer side. However, the effect of k on con sumer decisions deserves further discussion. Intuitively, the heavier cost pressure in obtaining the authorized content drives customers to jail break or even quit the platform. In contrast, the indirect effect is that increasing content provided by more developers brings additional ben efits, which alleviates the effect of customers leaving. Thus, when k is small $\begin{array} { r } { ( k < \frac { 2 - b - b ^ { 2 } } { a N _ { D } } ) } \end{array}$ , as it grows, the increase in the platform’s income from the developer side overweighs the loss stemming from the customer side. However, when k goes beyond the threshold, the loss due to jailbreaking becomes severe enough that a further increase of k dis courages consumer purchasing, profoundly hurting the developer’s profit realization and reducing revenue.

Fig. 6 illustrates how the platform’s profits from both sides and its total profit vary with the increase of $k ,$ where $a = 0 . 8 , b = 0 . 8$ , and $N _ { D } =$ 0.8. Here $\pi _ { c }$ and $\pi _ { d }$ refer to the platform’s revenue earned from the customer side and the developer side, respectively. The black line, π, represents how the whole revenue changes with k. It can be found that when k exceeds the threshold, the platform’s profit decreases as k rises.

Finally, we focus on how the “jailbreaking rate,” endogenously determined in our model, varies with those parameters. The jailbreaking rate indicates the fraction of customers accessing the content without authorization, raising the concerns from the platform itself and content developers. In the partial jailbreaking region, the jailbreaking rate $R =$

$\frac { k ( a + k ) N _ { D } - 2 ( 1 - b ) } { 2 ( 1 - b ) + k ( k ( 1 + b ) - a ( 1 - b ) ) N _ { D } } .$ . We state the influencing mechanism in Corollary 3.

Corollary 3. In the partial jailbreaking region, the jailbreaking rate R satisfies:

(1) R is monotonically increasing as the indirect network effect a grows.

(2) R is monotonically increasing as the consumer-utility discount b grows.

(3) R is monotonically increasing as the number of content de velopers N grows.

![](/api/attachments/SKREP2Z2/fulltext/images/6a37d5d763175cdd038c4ce0b112f1183969d512578ee42fd9c7d8e610b96266.jpg)  
Fig. 6. How the optimal profit changes with an increasing content price k.

(4) When $\begin{array} { r } { \frac { 1 } { 2 } \bigg [ 1 - \frac { 4 k } { a + 2 k } + \frac { \big ( a + 6 k \big ) ^ { 2 } - 4 a k ^ { 2 } ( a + 2 k ) N _ { D } } { ( a + 2 k ) ^ { 2 } } \bigg ] < b , } \end{array}$ R decreases as k grows. Otherwise, when $\begin{array} { r } { b \le \frac { 1 } { 2 } \left[ 1 - \frac { 4 k } { a + 2 k } + \sqrt { \frac { \left( a + 6 k \right) ^ { 2 } - 4 a k ^ { 2 } \left( a + 2 k \right) N _ { D } } { \left( a + 2 k \right) ^ { 2 } } } \right] } \end{array}$ R increases as k grows.

As the indirect network effect a become stronger, the increasing content value will eventually persuade customers to jailbreak and obtain the cracked content. Similarly, a larger developer community scale en ables customers to derive higher utilities when accessing the increas ingly enriched content, which encourages jailbreaking behavior. Also, the increase of b alleviates the degradation in consumer utility caused by jailbreaking, so more customers are motivated to enjoy unauthorised content.

Generally, as a larger content fee k motivates developers to provide content, customers will become more inclined to jailbreak and then access it freely. However, when b enters the high-value region $( { \scriptstyle { \frac { 1 } { 2 } } } \left\lceil 1 \right. -$ $\begin{array} { r } { \frac { 4 k } { a + 2 k } + \ \sqrt { \frac { \left( a + 6 k \right) ^ { 2 } - 4 a k ^ { 2 } \left( a + 2 k \right) N _ { D } } { \left( a + 2 k \right) ^ { 2 } } } \bigg ] < b ) } \end{array}$ , the jailbreaking option cannot be neglected from the perspective of consumer utility. In this case, increasing k leads to a large-scale shift of customers towards unau thorised content, bringing a loss to the developers that cannot be compensated for by charging a higher content fee. Hence, the shrinking of the developer community narrows the jailbreaking rate in turn.

To conclude, facing the threats from customer jailbreaking, the closed two-sided platform should consider price-setting comprehen sively to optimize the overall profit. Through analysis, we distinguish the market situations into two cases based on the relative magnitude of consumer-utility discount, including the no jailbreaking and partial jailbreaking regions. The analytical results provide the optimal license and access fees and clarify the conditions when the platform should subsidize content developers. The comparative statics analysis of profit and jailbreaking rate also provides several interesting results. Most significantly, the results we obtained uncover that no jailbreaking can benefit the platform’s profit. The conclusions we obtain provide prac tical implications for the platform’s pricing decisions.

## 5. Extension

## 5.1. Additional benefits from jailbreaking

The closed two-sided platform integrates the content provision and creates a relatively stable environment resistant to external threats. However, strict DRM also poses obstacles for customers to improve user experiences via adjusting settings individually. Overriding the DRM via jailbreaking, customers can enjoy additional benefits beyond freely accessing content. This kind of platform can be defined as a “jail breaking-beyond-piracy” platform. For example, customers can remove the bloatware pre-installed on the platform [39], or they can enjoy music or books in a format not normally supported. Certain questions

$$
\text { Partial   jailbreaking } \left\{ \begin{array}{l l} n _ {c r} = \frac {p _ {d} N _ {D} (a - b a - b k) - b + r + 1}{k N _ {D} (a (b - 1) + b k) - b + 1} \\ n _ {d} = \frac {N _ {D} ((b - 1) p _ {d} - k (b - r - 1))}{k N _ {D} (a (b - 1) + b k) - b + 1} & r \geq v _ {1 t} ^ {*} \text {   and   } r \leq v _ {2 t} ^ {*} \\ n _ {c} = 1 - \frac {p _ {c} - r}{b} - \frac {(a - k) N _ {D} (k (b - r - 1) - (b - 1) p _ {d})}{k N _ {D} (a (b - 1) + b k) - b + 1} \end{array} \right.
$$

emerge: Considering these benefits, how should the platform adjust the optimal prices to react? Can tolerating jailbreaking generate more profit?

To address these problems, we denote the additional benefi $( \mathrm { i . e . , }$ beyond accessing content) brought by jailbreaking as r. For simplicity, we assume r is homogeneous among customers. Then the utility function of customers accessing unauthorised content becomes:

$$
U _ {u c} = b (v + (a + k) n _ {d}) - p _ {c} + r\tag{10}
$$

According to the IR and IC conditions, the consumer type choosing to access the genuine content can be described as:

$$
\begin{array}{l} v - p _ {c} + a n _ {d} > 0 \Leftrightarrow v > v _ {1} ^ {\prime} = p _ {c} - a n _ {d} \\ v - p _ {c} + a n _ {d} \geq b (v + (a + k) n _ {d}) - p _ {c} + r \Leftrightarrow v \geq v _ {3} ^ {\prime} = \frac {(a b + b k - a) n _ {d} + r}{1 - b} \end{array}
$$

Similarly, if a customer chooses to jailbreak after accessing the platform, their type satisfies the following conditions:

$$
\begin{array}{l} b (v + (a + k) n _ {d}) - p _ {c} + r > 0 \Leftrightarrow v > v _ {2} ^ {\prime} = \frac {p - r - b (a + k) n _ {d}}{b} \\ b (v + (a + k) n _ {d}) - p _ {c} + r > v - p _ {c} + a n _ {d} \Leftrightarrow v <   v _ {3} ^ {\prime} = \frac {(a b + b k - a) n _ {d} + r}{1 - b} \end{array}
$$

Similar to the analysis in Section 3.3, we omit the situation of full jailbreaking, which means that $\nu _ { 3 } < 1$ . Then we obtain the quantity of customers accessing authorized content $\left( n _ { c r } \right)$ , conducting jailbreaking $\left( n _ { c p } \right)$ , and purchasing the platform (n ) under the two market situations as follows.

$$
\text { Partial   jailbreaking } \left\{ \begin{array}{l l} n _ {c r} = a n _ {d} + \frac {1 - b - b k n _ {d} - r}{1 - b} \\ n _ {c p} = \frac {b (k n _ {d} + p _ {c}) - p _ {c} + r}{b (1 - b)} & v _ {2} ^ {\prime} <   v _ {1} ^ {\prime} \text { and } v _ {3} ^ {\prime} <   1 \\ n _ {c} = 1 + \frac {(a + k) b n _ {d} - p _ {c}}{b} \end{array} \right.\tag{11}
$$

$$
\text { No   jailbreaking } \left\{ \begin{array}{l l} n _ {c r} = 1 + a n _ {d} - p _ {c} & \\ n _ {c p} = 0 & v _ {2} ^ {\prime} \geq v _ {1} ^ {\prime} \\ n _ {c} = 1 + a n _ {d} - p _ {c} & \end{array} \right.\tag{12}
$$

In contrast, the content developers’ profit function will not be affected by $r ,$ so the total number of active developers remains $n _ { d } =$ $( n _ { c } k - p _ { d } ) N _ { D }$ . Substituting this into the above equations and solving them simultaneously, we obtain the numbers of customers and de velopers, dependent on prices, in Lemma 3.

Lemma 3. When jailbreaking brings additional benefits, the numbers of customers accessing genuine content, content developers, and total active customers under two market situations are:

$$
\text { No   jailbreaking } \left\{ \begin{array}{l} n _ {c} = n _ {\mathrm{cr}} = \frac {1 - a p _ {d} N _ {D} + p _ {c}}{1 - a k N _ {D}} \\ n _ {d} = \frac {(k (p _ {c} - 1) - p _ {d}) N _ {D}}{1 - a k} \quad r \leq v _ {1 t} ^ {*} \end{array} \right.
$$

Here, $\nu _ { 1 t } ^ { * } = ( 1 - b ) p _ { c } + b k p _ { d } N _ { D } ,$ , and $\nu _ { 2 t } ^ { * } = 1 - b + p _ { d } N _ { D } ( a ( b - 1 ) +$ $b k ) .$

Based on the above analysis, we can investigate the platform’s profit optimization problem. The solutions are shown in Proposition 5. Here the threshold values of r are defined as follows:

$$
\begin{array}{l} r _ {1} = \frac {(1 - b) (4 (1 - b) + (a b + b k - 2 a) k N _ {D})}{4 - a (a + 3 k) N _ {D} - b (4 - (a + k) (a + 2 k) N _ {D})} \\ r _ {2} = \frac {b (1 - b) (k (a + k) N _ {D} - 2 (1 - b))}{2 - 2 a k N _ {D} + b \left(k ^ {2} - a ^ {2}\right) N _ {D} + b ^ {2} \left((a + k) ^ {2} N _ {D} - 2\right)} \\ r _ {3} = \frac {2 (1 - b) - k (a + k) N _ {D}}{(a + k) ^ {2} N _ {D} - 4} \end{array}
$$

Proposition 5. Partial jailbreaking region: When max $\left. r _ { 2 } , \ 0 \right.$ $< r \leq r _ { 1 }$ , the platform tolerates customer jailbreaking and charges the following prices:

$$
p _ {c} ^ {*} = \frac {r (b (k (a + k) N _ {D} - 2) - 2 a k N _ {D} + 2) + b k N _ {D} (a (b - 1) + b k + k) - 2 (b - 1) b}{b ^ {2} (a + k) ^ {2} N _ {D} - b ((a - 3 k) (a + k) N _ {D} + 4) - 4 a k N _ {D} + 4}
$$

$$
p _ {d} ^ {*} = \frac {2 k N _ {D} (b + r - 1) + b (1 - b) (a + k) N _ {D} \left(1 - \frac {k (a + k) (b + r - 1) N _ {D}}{t} + \frac {r}{b}\right)}{4 (1 - b) N _ {D} - \frac {(1 - b) ^ {2} (a + k) ^ {2} N _ {D} ^ {2}}{t}}
$$

No jailbreaking region with threats: When max $\{ r _ { 3 } , 0 \} < r \le r _ { 2 } ,$ no jailbreaking behavior occurs, but the platform still needs to consider the jailbreaking threats in price-setting:

$$
\begin{array}{l} p _ {c} ^ {*} = \frac {b k ^ {2} N _ {D} + (2 (1 - b) + (a b + b k - 2 a) k N _ {D}) r}{2 ((1 - b) ^ {2} + (a b + b k - a) k N _ {D})} \\ p _ {d} ^ {*} = \frac {k - k N _ {D} (a (b - 1) + b k) (a r + k (r - 1)) + a (b - 1) r + b k (2 b + 3 r - 3) - k r}{2 (k N _ {D} (a (b - 1) + b k) + (b - 1) ^ {2})} \end{array}
$$

No jailbreaking region without threats: When $0 < r \le r _ { 3 } ,$ , no jail breaking behavior occurs, and the threats also disappear. The platform optimally sets the prices:

$$
p _ {c} ^ {*} = \frac {2 - k (a + k) N _ {D}}{4 - (a + k) ^ {2} N _ {D}} p _ {d} ^ {*} = \frac {k - a}{4 - (a + k) ^ {2} N _ {D}}
$$

Here, $t = 1 - b + ( b k - a ( 1 - b ) ) k N _ { D } .$

The critical difference between Proposition 5 and Proposition 1 lies in that a new market scenario emerges, where jailbreaking behavior no longer exists but still affects the platform’s pricing decisions. Facing the potential threats, the platform must adjust the prices to make jail breaking uneconomical and retain the developer group.

Eventually, to check whether the platforms will tolerate jailbreaking when this behavior brings additional customer benefits, we compare the optimal profit with that in Section 3.2′s benchmark. The comparison brings new insights for this issue, as shown in Proposition 6. The threshold value of $r _ { 0 }$ is given in the Appendix.

Proposition 6. Jailbreaking can benefit the closed two-sided platform’s profit only when additional benefits from jailbreaking become sufficiently large for customers $( r > r _ { 0 } )$

Adequately large additional benefits enhance the attractiveness of jailbreaking enormously, so much so that purchasing and then jail breaking becomes an appealing option for almost all customers. Thus, from the perspective of interests, even though the platform has to sub sidize substantially to retain developers, indicating the sacrifice of this profit stream, the large number of customers crowding in positively impacts its total revenue. In the end, the platform wins by tolerating jailbreaking. This finding partially explains the difference in attitudes towards jailbreaking between different platforms. On game platforms (such as PlayStation), the primary purpose of customer jailbreaking is to install pirated games, and thus these platforms usually tend to prohibit jailbreaking, with mobile platforms (such as IOS) may tolerate the jail breaking’s existence.

## 5.2. In the presence of direct network effects

In the main model, we focus on the indirect network effects’ influ ence on the closed platform’s attitude towards jailbreaking. Now, we extend the work by considering the direct network effects on the con sumer side. Since customers accessing the content can share their ex periences with each other whenever they do or do not jailbreak, we denote the direct network effects active customers can enjoy as a<sub>d</sub>n<sub>c</sub>. Hence, in this case, the utility function of customers accessing genuine content is as follows.

$$
u _ {c} ^ {d} = a _ {d} n _ {c} + a n _ {d} - p _ {c} + \nu\tag{13}
$$

Similarly, the utility function of those customers jailbreaking the platform is:

$$
u _ {u c} ^ {d} = b (a + k) n _ {d} + a _ {d} b n _ {c} + b v - p _ {c}\tag{14}
$$

The content developers’ utility is still:

$$
U _ {d} = n _ {c r} k - p _ {d} - f\tag{15}
$$

and the platform can earn revenue:

$$
\max _ {p _ {c}, p _ {d}} \Pi (p _ {c}, p _ {d}) = n _ {c} p _ {c} + n _ {d} p _ {d}
$$

In the presence of both direct and indirect network effects, we find that the calculation process turns too complicated to derive clear managerial insights. Thus, to better deliver implications, we conduct numerical experiments. Fixing other parameter values as $N _ { D } = 0 . 8 , k =$ $0 . 8 , b = 0 . 5 ,$ , and $a = 0 . 4$ , we draw the profit function to show its relationship with $^ { a _ { d } , }$ as shown in Fig. 7.

We define the threshold of the no jailbreaking region and the partial jailbreaking region as $a _ { d } ^ { * } .$ When $a _ { d } < a _ { d } ^ { * } .$ , no jailbreaking behavior exists. Otherwise, when $a _ { d } \geq a _ { d } ^ { * } .$ , the market situation enters the partial jail breaking region. The observation of this figure can lead to the following observations.

Observation 1. . As the direct network effect intensity grows, the plat form’s optimal profit increases.

This observation is intuitive. As the direct network effect grows stronger, customers can obtain more utility, and their willingness to pay is enhanced, which also encourages content developers’ participation. Hence, the platform’s profit improves.

Observation 2. . As the direct network effect intensity grows, customers are more likely to jailbreak the platform.

As the direct network effect grows stronger, more customers will be motivated to join the platform, further persuading content developers to join. In this case, jailbreaking can bring a larger utility than accessing authorized content, and the platform will also find that it is better to tolerate this behavior since it can benefit more from the increasing numbers of both customers and developers.

Combining these two observations, we find that strong direct network effects simultaneously encourage customer jailbreaking and improve the platform’s profit. Hence, compared with situations having low direct network effects, jailbreaking will be more pervasive, but the platform can also earn more when direct network effects are high. In this case, tolerating the existence of jailbreaking will be better for closed platforms than prohibiting it, exhibiting a sharp difference from the case with indirect network effects. In other words, the influencing mecha nism of these two kinds of network effects on closed platforms’ opera tions is differentiated.

![](/api/attachments/SKREP2Z2/fulltext/images/e593fff32796c52e9b4f7f19711049120e6c7fbe9082074a286cbb974c960bd0.jpg)  
Fig. 7. How the optimal profit changes with an increasing direct network effect intensity $a _ { d } .$

## 5.3. Content developers can benefit from unauthorised customers

Our basic model assumes that content developers cannot earn any thing from unauthorised access, an assumption widely adopted in abundant literature. However, in business reality, content developers can sometimes benefit from pirating users, although the users paid nothing. For instance, these customers accessing unauthorised content can share their experiences with other users, thus enhancing the word of-mouth effect [46]. Besides this, in the presence of the high switch ing cost for customers, these customers’ existence can empower the content developer with a competitive advantage over other competitors on the platform. Hence, we assume that content developers can earn two streams of benefits now. In addition to the income from content pur chasing, they also enjoy the extra benefits originating from all active customers, denoted by k n . Here $k _ { 2 }$ captures the unit benefit. Hence, the utility function of the content developer when no jailbreaking exists turns into:

$$
U _ {d} = n _ {c} k + n _ {c} k _ {2} - p _ {d} - f
$$

The utility function of content developers when jailbreaking exists is:

$$
U _ {d} = n _ {c r} k + n _ {c} k _ {2} - p _ {d} - f
$$

The customers’ utility function and the platform’s profit function remain unchanged. Following the steps in Section 4, we derive the optimal prices and profits. However, the equilibrium results are complicated to analyze in this case, so we use numerical experimenta tion to illustrate them. Setting the parameter values as $N _ { D } = 0 . 8 , k =$ $0 . 8 , a = 0 . 4 ,$ , and $b = 0 . 5 ,$ , we obtain the results shown in Fig. 8.

Observing this figure, we can find that as $k _ { 2 }$ grows, the platform’s optimal profit always increases. The reason is that as k rises, content developers become more motivated to join the platform, further encouraging customer purchases and improving the platform’s profit. Here it is noteworthy that the platform may even subsidize the de velopers in some cases, but their joining can still boost the sales among users, leading to an increase in the platform’s income.

Also, when $k _ { 2 }$ increases, the platform becomes more motivated to tolerate jailbreaking behavior. Searching for the reasons, we find that a larger $k _ { 2 }$ motivates content developers to remain on the platform. Although the fraction of customers choosing to jailbreak may increase, the total user population grows. Hence, the platform tends to tolerate this phenomenon since it can earn from both developer and customer groups.

## 5.4. When the content price is decided by the developers

In this section, we relax the main model’s content price assumption and assume that content developers can decide that price. This setting is more realistic because, in reality, the prices of most platform content are determined by the developers themselves. However, it is noteworthy that this price-setting process is not completely free; it is partially restricted. For example, in the App Store on IOS, the product pricing of some low-price content can only be selected from a few categorical prices, such as \$0.99 or \$1.99, instead of being directly priced by con tent developers.

Based on the above observations, we assume that the platform charges prices for consumers and developers, but the price of content is decided by content developers. In the face of the content valuations, the consumers are divided into two groups. The first group is the high-value group H, for whom the average valuation of the content is $K _ { H } .$ For the other group of consumers, $L ,$ their valuation of the content is $K _ { L } .$ . The proportion of consumers of type H to the total number of consumers is m, and type L customers take the remaining $1 - m$ . We assume that the consumer type and the consumer’s valuation of the platform are inde pendent; that is, v is not related to $K _ { H }$ and $K _ { L }$

![](/api/attachments/SKREP2Z2/fulltext/images/f8ae9c639c4625828cfbb371e5f66a2de59624d4bc9c104ebd70ab288c78ce31.jpg)  
Fig. 8. How the optimal profits change with an increasing content price $k _ { 2 } .$

The content developers can set prices independently. We assume the content developers set the content price as k to meet different types of consumer demand.

When consumers enter the market and decide to consume products, their utility function is:

$$
u _ {c t} = v + \operatorname{Max} [ (K _ {T} - k) n _ {d}, 0 ] - p _ {c} (T \in [ H, L ])
$$

It is worth noting that since the content developer determines the price of k, the case $K _ { T } < k$ is likely to occur. In this case, consumers will only purchase the platform and not purchase any content. Additionally, k may be negative, in which case the content developer pays the con sumer, and the platform provides a subsidy to the content developer. To reflect reality, we assume that $k \leq K _ { H }$

Similarly, when consumers purchase the platform and jailbreak, their utility function is:

$$
u _ {c j} = b v + b \operatorname{Max} [ K _ {T} n _ {d}, 0 ] - p _ {c} \qquad (T \in [ H, L ])
$$

Content developers can only earn revenue from consumers who refuse to jailbreak the platform and purchase the content. Therefore, the content developer’s utility function is

$$
u _ {d t} = \left(\sum \operatorname{Max} [ n _ {\mathrm{Tr}}, 0 ] k\right) - p _ {d} - f \quad (T \in [ H, L ])
$$

where $n _ { \mathrm { T r } }$ refers to the total number of consumers who have purchased both the platform and the content of type T. The developer’s cost f is still uniformly distributed in $[ 0 , 1 ]$

For the platform, its profits still come from two sources, content developers and consumers. The platform's profit function is

$$
\pi = n _ {d} p _ {d} + \sum (\operatorname{Max} [ n _ {\mathrm{Tr}}, 0 ] p _ {c})
$$

As this model is complex, we cannot obtain intuitive analytical and numerical solutions. In this section, we use Reinforcement Learning to obtain corresponding numerical analysis results. Fixing $K _ { H } = 0 . 7 , K _ { L } =$ $0 . 5 ,$ , and $N _ { D } = 0 . 8$ , we set m as $0 . 1 , 0 . 3 , 0 . 5 , 0 . 7 ;$ , and 0.9, respectively. In Fig. 9, we illustrate how the optimal profit and corresponding region change with the variation of the customer utility discount from jailbreaking, denoted b. The solid line represents the no jailbreaking region, and the dashed line shows the partial jailbreaking region.

![](/api/attachments/SKREP2Z2/fulltext/images/9b9bda930d4c05cd73d61b1cc1a1874ac1e5f9218291cdf75513a6eb0f224ef2.jpg)  
Fig. 9. How the optimal profits change with an increasing customer utility discount b caused by jailbreaking.

From $\mathrm { F i g . ~ } 9 ,$ it can be clearly seen that as b increases, the market situation platforms face will change from the no jailbreaking region into the partial jailbreaking region. The reason is that as b increases, the attraction of jailbroken content increases, making it harder for the platform to manage jailbreaking behavior. Hence, the market turns into a partial jailbreaking region.

Observing the profit change, we can also find that when the market situation changes into the partial jailbreaking region as b grows, the closed platform’s optimal profit decreases, proving that the presence of jailbreak hurts the platform’s profitability.

Additionally, when the proportion of high-type consumers increases, the optimal profit increases, and the market is more likely to enter the partial jailbreaking region. This is because as m increases, the platform can attract more high-value consumers, thereby increasing its profits. However, at the same time, due to the increased attractiveness of plat form content, the benefits obtained by jailbroken consumers are also greater, making it easier for the market to enter the partial jailbreaking region.

Next, we examine the optimal content price’s variation in different scenarios. In the above numerical analysis we finished, we find that in all scenarios, the content developers would set the content price as $K _ { L }$ to obtain all consumers. We change the parameters, where $K _ { H } = 0 . 9 , b =$ 0.92, $N _ { D } = 0 . 8 ,$ , to observe the price-setting. We find that the content developer set the price $k = K _ { H }$ only when the difference between $K _ { H }$ and $K _ { L }$ is large enough and m is large enough (see Fig. 10). At this time, the content developer only serves high-type consumers. The low-type con sumers only buy the platform; they do not purchase the content, or they use the content by jailbreaking the platform.

## 6. Conclusion

Jailbreaking has been a critical issue for closed two-sided platforms for a long time, but previous literature rarely focuses on it. Although jailbreaking may help enlarge the user population, it harms developers enthusiasm for providing content and thus brings a complicated effect on the platform's overall profit. In this work, we investigate the influ: ence of jailbreaking on closed two-sided platforms’ pricing. Considering several significant factors, such as the customer-utility discount caused by jailbreaking and the indirect network effects, we build a model framework to explore the platform’s optimal pricing in the presence of jailbreaking. The influencing mechanism of these factors on profit realization is also identified. Moreover, using the case where no jail breaking exists as the benchmark, we discuss whether platforms should tolerate this kind of behavior. Finally, we extend the model by relaxing several major assumptions, aiming to deepen the comprehension of this problem.

Our research results distinguish realistic market situations into two regions depending on the relative magnitude of the consumer-utility discount. If customers suffer a sharp decline in utility when experi encing unauthorised content, jailbreaking will not occur. If the consumer-utility degradation caused by jailbreaking is not so apparent, the platform tends to tolerate jailbreaking and earns mainly from charging access fees, which compensates for the developer side’s reve nue loss. In this case, to retain developers and maintain a stable oper ation, the platforms should subsidize the developer group when the indirect network effect gets sufficiently large. Furthermore, we find that with our basic model, the platform always has higher profit when there is no jailbreaking, indicating that the indirect network effect cannot make the platform earn more from jailbreaking than it loses. These conclusions are also proved valid under some other scenarios, such as developers deciding the content price independently. Finally, when we consider that jailbreaking the platform brings additional benefits, a new market region emerges where jailbreaking acts as an “invisible hand” influencing the platform’s pricing decisions.

![](/api/attachments/SKREP2Z2/fulltext/images/0bb4a2904dd3c451b84100fa09901f373b3454717e43b91aa5492a6f7f9dccf4.jpg)  
Fig. 10. How the content price changes with an increasing m.

A significant finding of our work is that jailbreaking behavior harms the platform’s profit even when indirect network effects exist, if the jailbreaking behavior is conducted to access unauthorised content. This conclusion suggests an uncompromising attitude towards piracy. On the one hand, jailbreaking’s attractiveness can help promote customer purchasing and enrich the income platforms can earn from customers. However, the decrease in the proportion of customers accessing genuine content discourages developers’ participation, which hurts the customer utility of accessing the platform. Eventually, the platform’s profit in the presence of jailbreaking will not exceed that in the benchmark. How ever, when in some extreme scenarios, such as jailbreaking brings considerable benefits for consumers beyond just accessing unauthorised content, tolerating jailbreaking can become a feasible option to maxi mize the overall profit. As a significant supplement to the piracy and platform literature, our work provides practical guidelines for closed platforms in making pricing and DRM decisions.

There are several limitations of this work awaiting subsequent research. Firstly, further research could consider the research, devel opment, and implementation costs of DRM against the cost of jail breaking in search of the optimal pricing strategy. Next, jailbreaking’s influence could be examined in a competitive environment, which may deliver differentiated insights. Finally, the study considered only closed two-sided platforms, meaning that the platforms execute the highest DRM level. Future research could also consider open platforms anti piracy issues.

## CRediT authorship contribution statement

Yunhao Liu: Conceptualization, Methodology, Formal analysis, Writing – review & editing. Gengzhong Feng: Funding acquisition, Supervision, Writing – review & editing. Yangyang Sun: Validation, Writing – original draft, Writing – review & editing. Xiangyin Kong: Methodology, Writing – review & editing.

interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

## Declaration of Competing Interest

This work was supported by the National Social Science Foundation of China under Grant No. [20&ZD053]

The authors declare that they have no known competing financial

## Appendix

## A. Proofs of Lemmas, Propositions, and Corollaries

Proof of Lemma 1

In the absence of jailbreaking, we only consider authorized consumers who appear in the market. Hence, the optimal prices $p _ { d }$ and $p _ { c }$ satisfy the following first-order conditions:

$$
\frac {\partial \pi}{\partial p _ {c}} \left(p _ {c} ^ {*}, p _ {d} ^ {*}\right) = \frac {\partial \pi}{\partial p _ {d}} \left(p _ {c} ^ {*}, p _ {d} ^ {*}\right) = 0\tag{16}
$$

Solving Eq. (16), we derive the optimal price $p _ { c n j } ^ { * }$ and $p _ { d n j } ^ { * }$ given in Lemma 1, where we also summarize the maximal profit the platform can earn Proof of Lemma 2

In the no jailbreaking region, all customers will access authorized content, which means that $n _ { c r } = n _ { c }$ . Through analysis, we obtain that:

$$
n _ {c} = n _ {\mathrm{cr}} = \frac {1 - a p _ {d} N _ {D} + p _ {c}}{1 - a k N _ {D}}\tag{17a}
$$

$$
n _ {d} = \frac {(k (p _ {c} - 1) - p _ {d}) N _ {D}}{1 - a k}\tag{17b}
$$

The inequation $\nu _ { 1 } \leq \nu _ { 2 }$ leads to

$$
\frac {N _ {D} (b k - a + a b) (k - p _ {d})}{1 - b + k (b k - a + a b) N _ {D}} \leq 0
$$

The partial jailbreaking region indicates tha ${ \bf \cdot n } _ { c r } \neq { \bf n } _ { c }$ . Substituting $n _ { d } = ( k n _ { c r } - p _ { d } ) N _ { D }$ into the expression $\begin{array} { r } { n _ { c r } = a n _ { d } + \frac { 1 - b - b k n _ { d } } { 1 - b } , n _ { c } = 1 + \frac { ( a + k ) b n _ { d } - p _ { c } } { b } , n _ { d } } \end{array}$ $= N _ { D } ( k n _ { c r } - p _ { d } )$ , and solving these simultaneously, we derive the specific numbers of customers and developers:

$$
n _ {c r} = \frac {p _ {d} N _ {D} (- b a + a - b k) - b + 1}{k N _ {D} (a b - a + b k) - b + 1}\tag{18a}
$$

$$
n _ {d} = \frac {N _ {D} ((b - 1) p _ {d} - k (b - 1))}{k N _ {D} (a b - a + b k) - b + 1}\tag{18b}
$$

$$
n _ {c} = \frac {b - p _ {c} + r}{b} - \frac {(a - k) N _ {D} (k (b - 1) - (b - 1) p _ {d})}{k N _ {D} (a b - a + b k) - b + 1}\tag{18c}
$$

Because $\nu _ { 1 } \geq \nu _ { 2 }$ and $\nu _ { 3 } < 1$ , we obtain

$$
(1 - b) p _ {c} - \frac {(1 - b) b k N _ {D} (k - p _ {d})}{1 - b + k (b k - a + a b) N _ {D}} <   1\tag{19a}
$$

$$
\frac {N _ {D} (b k - a + a b) (k - p _ {d})}{1 - b + k (b k - a + a b) N _ {D}} \geq 0\tag{19b}
$$

## Proof of Proposition 1

We derive the optimal prices under two regions respectively.

No Jailbreaking Region:

The fact $\nu _ { 1 t } < 0$ brings the direct effect that jailbreaking behavior disappears in the market. Hence, similar to Lemma 1, we solve the following equation.

$$
\frac {\partial \pi}{\partial p _ {c}} \left(p _ {c} ^ {*}, p _ {d} ^ {*}\right) = \frac {\partial \pi}{\partial p _ {d}} \left(p _ {c} ^ {*}, p _ {d} ^ {*}\right) = 0\tag{20}
$$

The obtained results are as follows. To fulfill the equation $\nu _ { 1 t } < 0 ,$ we derive the feasible range of consumer-utility discount b.

$$
p _ {d} ^ {*} = \frac {k - a}{4 - (a + k) ^ {2} N _ {D}}
$$

$$
p _ {c} ^ {*} = \frac {2 - k (a + k) N _ {D}}{4 - (a + k) ^ {2} N _ {D}}
$$

Partial jailbreaking Region:

Solving Eqs. (20), 18b, and 18c simultaneously, we derive the optimal prices:

$$
p _ {d} ^ {*} = \frac {(1 - b) ((2 - b) k - a b) - k ^ {2} (a (2 - b) - b k) N _ {D}}{4 (1 - b) - (4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)) N _ {D}}
$$

$$
p _ {c} ^ {*} = \frac {2 b (1 - b) + b k (k (1 + b) - a (1 - b)) N _ {D}}{4 (1 - b) - \left(4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)\right) N _ {D}}
$$

The restrictions $\nu _ { 1 t } \geq 0$ and $\nu _ { 2 t } < 1$ lead to the feasible range of b being $L _ { 1 } \leq b \leq L _ { 2 }$ . Here $\begin{array} { r } { L _ { 2 } \ = \frac { 4 - 2 a k N _ { D } } { 4 - k ( a + k ) N _ { D } } } \end{array}$

To show the solution’s optimality, we check the second-order conditions and prove the following:

$$
\frac {\partial^ {2} \pi}{\partial p _ {d} ^ {2}} = - \frac {2}{b} <   0\tag{21a}
$$

$$
\frac {\partial^ {2} \pi}{\partial p _ {d} ^ {2}} = - \frac {2 (1 - b) N _ {D}}{- b (k (a + k) N _ {D} + 1) - a k N \neg_ {D} + 1} \leq 0\tag{21b}
$$

$$
\det (\text { Hessian }) = \frac {(1 - b) N _ {D} (4 - N _ {D} (a ^ {2} (1 - b) b + 2 a (- b ^ {2} - b + 2) k - b (b + 3) k ^ {2}) - 4 b)}{b (k N _ {D} (a b - a + b k) - b + 1) ^ {2}} \geq 0\tag{21c}
$$

Proof of Corollary 1

We compare the license and access fees between the partial jailbreaking region and the benchmark. The differences can be expressed as:

$$
d p _ {c} ^ {*} = \frac {2 (2 - k (a + k) N _ {D} - 2 b) (2 - b (2 - k (a + k) N _ {D}) - 2 a k N _ {D})}{(4 - (a + k) ^ {2} N _ {D}) (b ^ {2} (a + k) ^ {2} N _ {D} - b ((a + k) (a - 3 k) N _ {D} + 4) - 4 a k N _ {D} + 4)}\tag{22}
$$

$$
d p _ {d} ^ {*} = \frac {(a + k) (k (a + k) N _ {D} + 2 (b - 1)) (k N _ {D} (a b - 2 a + b k) - 2 b + 2)}{(4 - (a + k) ^ {2} N _ {D}) (- N _ {D} (a ^ {2} (1 - b) b + 2 a (- b ^ {2} - b + 2) k - b (b + 3) k ^ {2}) - 4 b + 4)}\tag{23}
$$

We first check Eq. (22) and find that its sign (positive and negative) can be judged by comparing $- ( 2 + k N _ { D } ( a b - 2 a + b k ) - 2 b )$ and 0. Equation 23's sign depends on the relative magnitude of $2 + k N _ { D } ( a b - 2 a + b k ) - 2 b ,$ , which indicates that $d p _ { c } ^ { * } > 0$ and $d p _ { d } ^ { * } < 0$ share the same threshold. Thus, we conclude that when $\begin{array} { r } { b < \operatorname* { m i n } \Bigl ( 1 , \frac { 2 - 2 a k N _ { D } } { 2 - k ( a + k ) N _ { D } } \Bigr ) } \end{array}$ , both $d p _ { c } ^ { * } < 0$ and $d p _ { d } ^ { * } > 0$ hold. Otherwise, when $\begin{array} { r } { b > \operatorname* { m i n } \Bigl ( 1 , \frac { 2 - 2 a k N _ { D } } { 2 - k ( a + k ) N _ { D } } \Bigr ) , d p _ { c } ^ { * } > 0 \mathrm { a n d } d p _ { d } ^ { * } < 0 . } \end{array}$

Proof of Proposition 2

In the partial jailbreaking region, the optimal license fee is:

$$
p _ {d} ^ {*} = \frac {(1 - b) ((2 - b) k - a b) - k ^ {2} (a (2 - b) - b k) N _ {D}}{4 (1 - b) - (4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)) N _ {D}}
$$

This equation implies that

$$
4 - N _ {D} \left(a ^ {2} (1 - b) b + 2 a (- b ^ {2} - b + 2) k - b (b + 3) k ^ {2}\right) - 4 b > 0\tag{24}
$$

Thus, it is easy to prove that the denominator of $\dot { p _ { d } }$ is positive. Then in order to solve ${ p } _ { d } ^ { * } < 0 ,$ , we let the numerator be smaller than 0 and obtain the range of a as $\begin{array} { r } { \frac { k ( 2 + b ( b k ^ { 2 } N _ { D } - 3 ) ) } { b ( 1 - b ) + ( 2 - b ) k ^ { 2 } N _ { D } } \leq a \leq 1 } \end{array}$ , where the platform subsidizes the content developers.

Proof of Proposition 3

The profit when no jailbreaking occurs on the market is:

$$
\pi_ {n j} ^ {*} = \frac {1}{4 - (a + k) ^ {2} N _ {D}}\tag{25}
$$

The platform’s profit in the partial jailbreaking region is:

$$
\pi_ {p j} ^ {*} = \frac {b (1 - b) + k ^ {2} N _ {D}}{4 (1 - b) - \left(4 a k - b ^ {2} (a + k) ^ {2} + b (a - 3 k) (a + k)\right) N _ {D}}\tag{26}
$$

We compare the profits and obtain that:

$$
\pi_ {n j} ^ {*} - \pi_ {p j} ^ {*} = \frac {(k (a + k) N _ {D} + 2 (b - 1)) ^ {2}}{(4 - (a + k) ^ {2} N _ {D}) (4 - 4 b - N _ {D} (a ^ {2} (1 - b) b + 2 a (- b ^ {2} - b + 2) k - b (b + 3) k ^ {2}))}\tag{27}
$$

Both the denominator and the numerator can be proven positive, which means that $\pi _ { n j } ^ { * } - \pi _ { p j } ^ { * } > 0 .$ . The result indicates that it is better to drive the jailbreaking threats out of the market than to retain them from the perspective of profitability. In other words, even in the presence of the indirect network effects $^ { a , }$ the closed platform still cannot benefit from jailbreaking.

Proof of Proposition 4

Proof of (1): It suffices to check the sign of the following derivative:

$$
\frac {\partial \pi^ {*}}{\partial N _ {D}} = \frac {(1 - b) ^ {2} (a b + b k + 2 k) ^ {2}}{\left(N _ {D} \left(a ^ {2} (b - 1) b - 2 a (- b ^ {2} - b + 2) k + b (b + 3) k ^ {2}\right) - 4 b + 4\right) ^ {2}}\tag{28}
$$

Since both the numerator and denominator can be proven positive, $\frac { \partial \pi ^ { * } } { \partial N _ { D } } > 0$ can be proved, which indicates (1) in this Proposition. Proof of (2): It suffices to check the sign of the following derivative:

$$
\frac {\partial \pi^ {*}}{\partial a} = \frac {2 (1 - b) N _ {D} (a b + b k + 2 k) ((1 - b) b + k ^ {2} N _ {D})}{(N _ {D} (a ^ {2} (b - 1) b - 2 a (- b ^ {2} - b + 2) k + b (b + 3) k ^ {2}) - 4 b + 4) ^ {2}}\tag{29}
$$

We can prove that the numerator and denominator are both positive, which leads to $\textstyle { \frac { \partial \pi ^ { * } } { \partial a } } > 0$

Proof of (3): It suffices to check the sign of the following derivative:

$$
\frac {\partial \pi^ {*}}{\partial b} = \frac {(2 (1 - b) - k (a + k) N _ {D}) (k N _ {D} (a (2 b - 1) + (2 b + 3) k) - 2 b + 2)}{(N _ {D} (a ^ {2} (b - 1) b - 2 a (- b ^ {2} - b + 2) k + b (b + 3) k ^ {2}) - 4 b + 4) ^ {2}}\tag{30}
$$

The denominator can be proven to always be positive. Considering $\begin{array} { r } { \frac 1 2 \big ( 2 - a k N _ { D } - k ^ { 2 } N _ { D } \big ) < b , } \end{array}$ , we can derive that $2 ( 1 - b ) - k ( a + k ) N _ { D }$ is negative. Also, we can prove $k N _ { D } ( a ( 2 b - 1 ) + ( 2 b + 3 ) k ) - 2 b + 2 = ( 2 - 2 b ) ( 1 - a k N _ { D } ) + a k N _ { D } + 2 b k ^ { 2 } N _ { D } + 3 k ^ { 2 } N _ { D } > 0 ,$ Thus the numerator is negative, which means that $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial b } < 0 } \end{array}$

Proof of (4): It suffices to check the sign of the following derivative:

$$
\frac {\partial \pi^ {*}}{\partial k} = \frac {2 (1 - b) N _ {D} (a b + b k + 2 k) (- a k N _ {D} - b ^ {2} - b + 2)}{\left(N _ {D} \left(a ^ {2} (b - 1) b - 2 a (- b ^ {2} - b + 2) k + b (b + 3) k ^ {2}\right) - 4 b + 4\right) ^ {2}}\tag{31}
$$

Through calculation, we discover that the sign of the above expression depends on the relative magnitude of ${ \bf 2 } - \mathrm { \Delta } a k N _ { D } - \mathrm { \Delta } b ^ { 2 } - \mathrm { \Delta } b$ . When $\begin{array} { r } { \frac { 2 - b ^ { 2 } - b } { a N _ { n } } \leq k \leq 1 , \frac { \partial \pi ^ { * } } { \partial k } > 0 } \end{array}$ holds in the partial jailbreaking region. When $\begin{array} { r } { 0 < k < \frac { 2 - b ^ { 2 } - b } { a N _ { D } } , \frac { \partial \pi ^ { * } } { \partial k } < 0 . } \end{array}$ . Vice versa.

Proof of Corollary 3

Proof of (1): Similar to the proof of Proposition 4, we check the relative magnitude between the following derivative and 0, and we can easily discover that it is always positive.

$$
\frac {\partial R}{\partial a} = \frac {2 k N _ {D} \left(k ^ {2} N _ {D} - b ^ {2} + b\right)}{\left(k N _ {D} (a b - a + b k + k) - 2 b + 2\right) ^ {2}}\tag{32}
$$

Proof of (2): Here we just need to check the sign of the following derivative:

$$
\frac {\partial R}{\partial b} = \frac {k N _ {D} (2 (a + 3 k) - k (a + k) ^ {2} N _ {D})}{(k N _ {D} (a b - a + b k + k) - 2 b + 2) ^ {2}}\tag{33}
$$

We can find that it depends on the relative magnitude between $6 k - a ^ { 2 } k N _ { D } - 2 a k ^ { 2 } N _ { D } + 2 a - k ^ { 3 } N _ { D }$ and 0. Considering the feasible range of these parameters, we conduct the following deduction, through which we prove that $\begin{array} { r } { \frac { \partial R } { \partial b } > 0 } \end{array}$ always holds.

$$
6 k - a ^ {2} k N _ {D} - 2 a k ^ {2} N _ {D} + 2 a - k ^ {3} N _ {D} > 2 a + 2 k + a ^ {2} k N _ {D} - a ^ {2} k N _ {D} + 2 a k ^ {2} N _ {D} - 2 a k ^ {2} N _ {D} + k ^ {3} N _ {D} - k ^ {3} N _ {D} = 2 a + 2 k > 0
$$

Proof of (3): We check the following derivative and can easily prove that it is positive.

$$
\frac {\partial R}{\partial N _ {D}} = \frac {2 (1 - b) k (a b + b k + 2 k)}{\left(k N _ {D} (a b - a + b k + k) - 2 b + 2\right) ^ {2}}\tag{34}
$$

Proof of (4): It suffices to check the sign of the following derivative:

$$
\frac {\partial R}{\partial k} = \frac {2 N _ {D} ((1 - b) (a b + 2 (b + 2) k) + a k ^ {2} N _ {D})}{(k N _ {D} (a b - a + b k + k) - 2 b + 2) ^ {2}}\tag{35}
$$

Through calculation, we find that the sign of Eq. (35) depends on the magnitude of $2 N _ { D } ( ( 1 - b ) ( a b + 2 ( b + 2 ) k ) + a k ^ { 2 } N _ { D } )$ , which can be found to not be monotonic. Thus, considering the region of the parameters’ value, we obtain the condition:

In the partial jailbreaking region, when $\begin{array} { r } { \frac { 1 } { 2 } \left( 1 - \frac { 4 k } { a + 2 k } + \sqrt { \frac { \left( a + 6 k \right) ^ { 2 } - 4 a k ^ { 2 } \left( a + 2 k \right) N _ { D } } { \left( a + 2 k \right) ^ { 2 } } } \right) < b \ , \frac { \partial R } { \partial k } > 0 . } \end{array}$ . Otherwise, $\begin{array} { r } { \frac { \partial R } { \partial k } \leq 0 } \end{array}$

Proof of Lemma 3

In the no jailbreaking region, all users purchasing the platform will access the authorized content, which means that $n _ { c r } = n _ { c }$ . Thus, we obtain:

$$
n _ {c} = n _ {\mathrm{cr}} = \frac {1 - a p _ {d} N _ {D} + p _ {c}}{1 - a k N _ {D}}\tag{36a}
$$

$$
n _ {d} = \frac {(k (p _ {c} - 1) - p _ {d}) N _ {D}}{1 - a k}\tag{36b}
$$

The condition $\nu _ { 1 } < 0$ leads to the feasible range of r being:

$$
r \leq (1 - b) p _ {c} + b k p _ {d} N _ {D}\tag{37}
$$

In the partial jailbreaking region, $n _ { c r } \neq n _ { c }$ . Considering the following conditions simultaneously, we obtain the numbers of customers and de velopers in Eqs. (38a), 38b, and 38c.

$$
n _ {c r} = a n _ {d} + \frac {1 - b - b k n _ {d} + r}{1 - b}
$$

$$
n _ {c} = 1 + \frac {(a + k) b n _ {d} - p _ {c}}{b}
$$

$$
n _ {d} = N _ {D} (k n _ {c r} - p _ {d})
$$

$$
n _ {c r} = \frac {p _ {d} N _ {D} (a - b a - b k) - b + r + 1}{k N _ {D} (a b - a + b k) - b + 1}\tag{38a}
$$

$$
n _ {d} = \frac {N _ {D} ((b - 1) p _ {d} - k (b - r - 1))}{k N _ {D} (a b - a + b k) - b + 1}\tag{38b}
$$

$$
n _ {c} = \frac {b - p _ {c} + r}{b} - \frac {(a - k) N _ {D} (k (b - r - 1) - (b - 1) p _ {d})}{k N _ {D} (a b - a + b k) - b + 1}\tag{38c}
$$

Knowing $\nu _ { 1 } \geq \nu _ { 2 }$ and $\nu _ { 3 } < 1$ hold, we obtain that

$$
r \geq (1 - b) p _ {c} + b k p _ {d} N _ {D}\tag{39a}
$$

$$
r \leq 1 - b + p _ {d} N _ {D} (a b - a + b k)\tag{39b}
$$

Proof of Proposition 5

In the presence of the additional benefits brought by jailbreaking, the optimal access fee $p _ { c }$ and license fee $p _ { d }$ in the no jailbreaking region is the same as for the benchmark. Since Lemma 2 indicates that $\nu _ { 1 t } \geq \nu _ { 3 t }$ , the feasible section of the no jailbreaking region can be derived as $0 \leq r \leq r _ { 3 }$ . Here, $\begin{array} { r } { r _ { 3 } = \frac { 2 \left( 1 - b \right) - k \left( a + k \right) N _ { D } } { \left( a + k \right) ^ { 2 } N _ { D } - 4 } . } \end{array}$

The condition $\nu _ { 1 t } < \nu _ { 3 t } \leq 1$ leads to the range of r being $r > r 3$ and $\begin{array} { r } { r \leq r _ { 2 } = \frac { b ( 1 - b ) ( k ( a + k ) N _ { D } - 2 ( 1 - b ) ) } { 2 - 2 a k N _ { D } + b ( k ^ { 2 } - a ^ { 2 } ) N _ { D } + b ^ { 2 } ( ( a + k ) ^ { 2 } N _ { D } - 2 ) } . } \end{array}$ . Since $r \geq 0$ must be satisfied, we then focus on the section max $\left\{ 0 , r _ { 3 } \right\} \le r \le r _ { 2 }$ . In this case, no jailbreaking occurs in the market. Letting $\nu _ { 1 } = \nu _ { 3 }$ , the optimal access fee can be derived as: r − kNp(ar − b(k − pj))

$$
p _ {c} = \frac {r - k N _ {D} (a r - b (k - p _ {d}))}{1 - b + k (a (- 1 + b) + b k) N _ {D}}
$$

Thus, we formulate the profit as:

$$
\pi (p _ {c} ^ {\prime}, p _ {d}) = \frac {\frac {(a p _ {d} N _ {D} + p - 1) (k N _ {D} (b k - a r - b p _ {d}) + r)}{k N _ {D} (a b - a + b k) - b + 1} + p _ {d} N _ {D} (p _ {d} + k p - k)}{a k N _ {D} - 1}
$$

Then, by solving $\begin{array} { r } { \frac { \partial \pi ( \boldsymbol { p ^ { \prime } } _ { c 2 } . \boldsymbol { p } _ { d 2 } ) } { \partial \boldsymbol { p } _ { d 2 } } = 0 } \end{array}$ and substituting $p _ { d 2 } ^ { * }$ into $p _ { c 2 } ^ { ' } ,$ we obtain the two prices as follows:

$$
p _ {d} ^ {*} = \frac {- k N _ {D} (a (b - 1) + b k) (a r + k (r - 1)) + a (b - 1) r + b k (2 b + 3 r - 3) - k r + k}{2 \left(k N _ {D} (a (b - 1) + b k) + (b - 1) ^ {2}\right)}
$$

$$
p _ {c} ^ {*} = \frac {b k ^ {2} N _ {D} + (2 (1 - b) + (a b + b k - 2 a) k N _ {D}) r}{2 ((1 - b) ^ {2} + (a b + b k - a) k N _ {D})}
$$

We define this new emerging region as “No jailbreaking region with threats”, where the jailbreaking acts as an invisible hand affecting pricesetting. The corresponding feasible interval of r is $\operatorname* { m a x } \{ 0 , r _ { 3 } \} < r \leq r _ { 2 } .$

The numbers of consumers and content developers in the partial jailbreaking region are also given in Lemma 3. Thus solving the condition $\frac { \partial \pi } { \partial p _ { c } } ( ( p _ { c } ^ { * } )$ $\begin{array} { r } { , ( p _ { d } ^ { * } ) ) = \frac { \partial \pi } { \partial p _ { d } } ( ( p _ { c } ^ { * } ) , ( p _ { d } ^ { * } ) ) = 0 } \end{array}$ simultaneously by substituting the values of $n _ { c }$ (given by Eq. (38b)) and $n _ { d } ( { \mathrm { g i v e n } }$ by Eq. (38c)). we obtain the optimal fees as follows. Here $t = 1 - b + ( b k - a ( 1 - b ) ) k N _ { D }$ . The corresponding range of r can be derived as max $\begin{array} { r } { \{ 0 , r _ { 2 } \} \le r \le r _ { 1 } = \frac { ( 1 - b ) ( 4 ( 1 - b ) + ( a b + b k - 2 a ) k N _ { D } ) } { 4 - a ( a + 3 k ) N _ { D } - b ( 4 - ( a + k ) ( a + 2 k ) N _ { D } ) } . } \end{array}$ p<sup>∗</sup><sub>c</sub> = <sup>r(b(k(a+k)ND−</sup> <sup>2)−</sup> <sup>2akND+2)+bkND(a(b−</sup> <sup>1)+bk+k)−</sup> <sup>2(b−</sup> <sup>1)b</sup><sub>2 2</sub>

$$
p _ {d} ^ {*} = \frac {2 k N _ {D} (b - r - 1) + b (1 - b) (a + k) N _ {D} \left(1 - \frac {k (a + k) (b - r - 1) N _ {D}}{t} - \frac {r}{b}\right)}{4 (1 - b) N _ {D} - \frac {(1 - b) ^ {2} (a + k) ^ {2} N _ {D} ^ {2}}{t}}
$$

Proof of Proposition 6

In the presence of additional benefits $r ,$ we determine the differences in the platform’s profit between the benchmark and the partial jailbreaking region as:

$$
d \pi_ {2} ^ {*} = \frac {- \frac {L _ {1} ^ {2}}{4 - (a + k) ^ {2} N _ {D}} + r ^ {2} \left(\frac {t}{b - b ^ {2}} - 1\right) - L _ {1} r}{b ^ {2} (a + k) ^ {2} N _ {D} - b ((a - 3 k) (a + k) N _ {D} + 4) - 4 a k N _ {D} + 4}
$$

Letting $d \pi _ { 2 } ^ { * } < 0 ;$ , we obtain that:

$$
r > r _ {0} = \frac {L _ {1} \left(\frac {\sqrt {(1 - b) b} \sqrt {(b - 1) b (a + k) ^ {2} N _ {D} + 4 t}}{\sqrt {4 - (a + k) ^ {2} N _ {D}}} + (1 - b) b\right)}{2 (t - b (1 - b))}
$$

## B. In the Presence of a Revenue-sharing Mechanism

In business practice, in addition to the fees charged for both content developers and the price for customers, many platforms adopt a revenue sharing mechanism. In this case, whenever the content developer sells one unit of content to one consumer, some of the resulting income will be transferred to the platform according to a negotiated fixed revenue-sharing rate. For instance, the Apple Store usually charges a commission rate of

30% to developers, although Apple has introduced the Small Business Program, which cuts fees to 15% for developers who make under 1 million U.S. dollars annually. Setting the revenue-sharing rate as $r s _ { d } ,$ we find that in the partial-jailbreaking region, the consumers’ utility functions do not change, but the content developer’s profit function $U _ { d } ^ { r s }$ now turns into:

$$
U _ {d} ^ {r s} = n _ {c r} k (1 - r s _ {d}) - f\tag{40}
$$

Letting $U _ { c } = 0$ and $U _ { d } ^ { r s } = 0 .$ , we can obtain the number of active customers, active content developers, and customers accessing unauthorised content, respectively:

$$
n _ {c} = \frac {k (1 - r s _ {d}) N _ {D} (b k - p _ {c} (a (1 - b) - b k)) + (1 - b) (b - p _ {c})}{b (k (1 - r s _ {d}) N _ {D} (a (1 - b) - b k) - b + 1)}\tag{41}
$$

$$
n _ {d} = \frac {(1 - b) k (1 - r s _ {d}) N _ {D}}{1 - b + k (1 - \mathrm{rs}) N _ {D} (b k - a (1 - b))}\tag{42}
$$

$$
n _ {c r} = \frac {1 - b}{1 - b + k (1 - \mathrm{rs}) N _ {D} (b k - a (1 - b))}\tag{43}
$$

Similarly, the closed two-sided platform sets prices and the revenue-sharing rate to maximize the profit, and the optimization problem can be defined as:

$$
\max _ {r s _ {d}, p _ {c}} \Pi (r s _ {d}, p _ {c}) = n _ {c} p _ {c} + n _ {d} n _ {c r} r s _ {d} k\tag{44}
$$

Through analysis, we derive the equilibrium results as follows:

$$
r s _ {d} ^ {*} = \frac {(b - 1) (a b + (b + 2) k)}{k (k N _ {D} (a (b - 2) + b k) - 4 b + 4)} + 1
$$

$$
p _ {c} ^ {*} = \frac {b (k N _ {D} (a (b - 1) + b k + k) - 2 b + 2)}{N _ {D} (a ^ {2} (b - 1) b + 2 a (b ^ {2} + b - 2) k + b (b + 3) k ^ {2}) - 4 b + 4}
$$

which can be used to show that the optimal profit is:

$$
\Pi^ {*} = \frac {b (1 - b) + k ^ {2} N _ {D}}{N _ {D} \left(a ^ {2} (b - 1) b + 2 a (b ^ {2} + b - 2) k + b (b + 3) k ^ {2}\right) - 4 b + 4}
$$

It is easy to show that the above optimal profit equals that presented in $\operatorname { E q . } \left( 9 \right)$ . Furthermore, the boundary between the partial jailbreaking region and no jailbreaking region is $b = L _ { 1 } ,$ which also remains unchanged. Hence, the existence of the revenue-sharing mechanism cannot affect the platform's profit-earning, proving the robustness of our modeling framework

C. Discussion of the “No Jailbreaking with Threats” Region

Assuming that a “no jailbreaking with threats" region exists, where $\nu _ { 1 } = \nu _ { 2 } = \nu _ { 3 } $ , we can derive that $\begin{array} { r } { n _ { d } = \frac { ( 1 - b ) p _ { c } } { b k } } \end{array}$ . We know $n _ { c } = 1 + a n _ { d } - p _ { c }$ , and substituting n into this, we obtain that $\begin{array} { r } { n _ { c } \ = \frac { p _ { c } ( a ( - b ) + a - b k ) } { b k } + 1 } \end{array}$ . Then we compare $n _ { d }$ and $n _ { c }$ with the results in no jailbreaking region, where

$$
n _ {c} = n _ {\mathrm{cr}} = \frac {1 - a p _ {d} N _ {D} + p _ {c}}{1 - a k N _ {D}}
$$

$$
n _ {d} = \frac {(k (p _ {c} - 1) - p _ {d}) N _ {D}}{1 - a k}
$$

When $\nu _ { 1 } = \nu _ { 2 } ,$ we find that

$$
p _ {c} = \frac {b k N _ {D} (k - p _ {d})}{1 - b + k (b k - a (1 - b)) N _ {D}}
$$

Substituting the price into $n _ { c }$ and $n _ { d } ,$ we obtain $\begin{array} { r } { n _ { d } = \frac { ( 1 - b ) p _ { c } } { b k } } \end{array}$ and $\begin{array} { r } { n _ { c } = \frac { p _ { c } ( a ( - b ) + a - b k ) } { b k } + 1 } \end{array}$ , which equals the result of the no jailbreak with threat region. This means that we can combine these two regions. In other words, the results exhibit no difference from those in Lemma 3.2. Similarly, when va = va. the optimal pricing decision is

$$
\nu_ {2} = \nu_ {3}
$$

$$
p _ {d} = \frac {k \left(k N _ {D} (a (b - 1) + b k) + 2 b ^ {2} - 3 b + 1\right)}{2 \left(k N _ {D} (a (b - 1) + b k) + (b - 1) ^ {2}\right)}.
$$

As $\begin{array} { r } { p _ { c } = \frac { b k N _ { D } ( k - p _ { d } ) } { a b k N _ { D } - a k N _ { D } + b k ^ { 2 } N _ { D } - b + 1 } , } \end{array}$ we substitute $p _ { d }$ into it and derive

$$
p _ {c} = \frac {b k ^ {2} N _ {D}}{2 \left(k N _ {D} (a (b - 1) + b k) + (b - 1) ^ {2}\right)}.
$$

Letting $b = L _ { 1 } .$ , we obtain $\begin{array} { r } { p _ { c } = \frac { k ( a + k ) N _ { D } - 2 } { ( a + k ) ^ { 2 } N _ { D } - 4 } , p _ { d } = \frac { a - k } { ( a + k ) ^ { 2 } N _ { D } - 4 } , } \end{array}$ which equals the results in no jailbreaking region when $b = L _ { 1 }$

To summarize. the optimal pricing decision when $\nu _ { 1 } = \nu _ { 2 } = \nu _ { 3 }$ is the same as in the no jailbreaking region. Hence, according to the boundary of the no jailbreaking region, we do not need to consider the “no jailbreaking with threats” region in our main model.

## References

[1] BSA, Software management: security imperative, Bus. Opportunity. Retrieved from (2018). https://gss.bsa.org/wp-content/uploads/2018/05/2018\_BSA\_GSS\_Repo rt\_en.pdf.

[2] Goff, M. (2022). Software piracy statistics 2022 – stat watch. Retrieved from htt ps://www.revenera.com/blog/software-monetization/software-piracy-stat-watch/

[3] T. Eisenmann, G. Parker, M.W. Van Alstyne, Strategies for two-sided markets, Harv. Bus. Rev. 84 (10) (2006) 92.

[4] Brewster, T. (2020). Of Ma and malware: inside China’s iPhone jailbreaking industrial complex. Retrieved from https://www.forbes.com/sites/thomasbrewst er/2015/06/26/china-iphone-jailbreak-industry/?sh=19a03e677538

[5] Kelly, G. (2020). New iPhone, iPad jailbreak exposes massive zero-day flaw impacting 900 million devices. Retrieved from https://www.forbes.com/sites/g ordonkelly/2020/05/24/apple-iphone-ios-135-warning-security-jailbreak-iph one-11-pro-max-upgrade/?sh=4a405ee778d2.

[6] Fisher, T. (2019). PlayStation demanding \$20,000 From PS4 hacker and pirated games seller. Retrieved from https://comicbook.com/gaming/news/ps4-pl aystation-sony-hacker-pirate/.

[7] A. Kim, A. Lahiri, D. Dey, The" invisible hand" of piracy: an economic analysis of the information-goods supply chain, MIS Q. 42 (4) (2018) 1117–1142.

[8] K. Conner, R.P. Rumelt, Software piracy: an analysis of protection strategies, Manag. Sci. 37 (2) (1991) 125–139.

[9] J.C. Rochet, J. Tirole, Platform competition in two-sided markets, J. Eur. Econ. Assoc, 1 (4) (2003) 990–1029.

[10] M. Armstrong, Competition in two-sided markets, Rand. J. Econ. 37 (3) (2006) 668–691.

[11] E.G. Anderson Jr, G.G. Parker, B Tan, Platform performance investment in the presence of network externalities, Inf. Syst. Res. 25 (1) (2014) 152–172.

[12] A. Hagiu, D. Spulber, First-party content and coordination in two-sided markets, Manag, Sci. 59 (4) (2013) 933–949.

[13] P. Huang, G. Lvu, Y. Xu, Ouality regulation on two-sided platforms: exclusion, subsidization, and first-party applications, Manag. Sci. 68 (6) (2022) 4415–4434.

[14] B. Tan, E.G. Anderson Jr, G.G Parker, Platform pricing and investment to drive third-party value creation in two-sided networks, Inf. Syst.Res. 31 (1) (2020) 217–239.

[15] G. Dou, P. He, X. Xu, One-side value-added service investment and pricing strategies for a two-sided platform, Int. J. Prod. Res. 54 (13) (2016) 3808–3821.

[16] R. Sui, X. Zhang, B. Dan, H. Zhang, Y. Liu, Bilateral value-added service investment in platform competition with cross-side network effects under multihoming, Eur. J. Oper. Res. 304 (3) (2023) 952–963.

[17] L.C. Kung, G.Y. Zhong, The optimal pricing strategy for two-sided platform delivery in the sharing economy, Transp. Res. Part E: Logistics Transp. Revie 101 (2017) 1–12.

[18] C. Zhang, J. Chen, S. Raghunathan, Two-sided platform competition in a sharing economy, Manage Sci 68 (12) (2022) 8909–8932.

[19] Y.Y. Wang, F. Tao, J. Wang, Information disclosure and blockchain technology adoption strategy for competing platforms, Inf. Manag. 59 (7) (2022), 103506.

[20] N. Economides, E. Katsamakas, Two-sided competition of proprietary vs. opensource technology platforms and the implications for the software industry, Manag. Sci, 52 (7) (2006) 1057–1071.

[21] P.M. Kort, G. Zaccour, When should a firm open its source code: a strategic analysis, Prod. Operations Manag. 20 (6) (2011) 877–888.

[22] R. Casadesus-Masanell, G. Llanes, Investment incentives in open-source and proprietary two-sided platforms. J. Econ, Manag. Strategy 24 (2) (2015) 306–324.

[23] L.N. Takeyama, The welfare implications of unauthorized reproduction of intellectual property in the presence of demand network externalities, J. Ind. Econ. 42 (2) (1994) 155–166.

[24] O. Shy, J.F. Thisse, A strategic approach to software protection, J. Econ. Manag. Strategy 8 (2) (1999) 163–190.

[25] S. Jain, Digital piracy: a competitive analysis, Mark, Sci, 27 (4) (2008) 610–626.

[26] R.K. Chellappa, S. Shivendu, Managing piracy: pricing and sampling strategies for digital experience goods in vertically segmented markets, Inf. Syst. Res. 16 (4) (2005) 400–417.

[27] S.Y. Wu, P.Y. Chen, Versioning and piracy control for digital information goods, Oper, Res. 56 (1) (2008) 157–172.

[28] A. Sundararajan, Managing digital piracy: pricing and protection, Inf. Syst. Res. 15 (3) (2004) 287–308

[29] Y.M. Li. C.H. Lin. Pricing schemes for digital content with DRM mechanisms. Decis Support Syst, 47 (4) (2009) 528–539.

[30] L. Zhang, L. Fan, H. Peng, Y. Zhang, Optimal piracy control and pricing strategies considering quality degradation: the effects of policy instruments, Electron. Commer. Res. Appl. 48 (2021), 101072.

[31] Z. Yi, Z. Cao, K.L. Cheung, Managing digital piracy under consumer valuation uncertainty: the roles of product demonstrations and antipiracy measures, Inf. Manag. 59 (2) (2022), 103601.

[32] R.D. Gopal, A. Gupta, Trading higher software piracy for higher profits: the case of phantom piracy, Manag. Sci. 56 (11) (2010) 1946–1962.

[33] H. Chao, C.Y. Ho. T.C. Leung, T. Ng, To root or not to root? The economics ot jailbreak, J. Comp. Econ. 45 (3) (2017) 481–497.

[34] A. Rasch, T. Wenzel, Piracy in a two-sided software market, J. Econ. Behav. Organ. 88 (2013) 78–89.

[35] A. Rasch, T. Wenzel, The impact of piracy on prominent and non-prominen software developers, Telecomm. Policy 39 (8) (2015) 735–744.

[36] G. Nan, L. Yao, Y.C. Ho, Z. Li, M. Li, An economic analysis of platform protection in the presence of content substitutability, J. Manag. Inf. Syst. 36 (3) (2019) 1002-1036.

[37] P. Aversa, A. Hervas-Drane, M. Evenou, Business model responses to digital piracy, Calif. Manag. Rev. 61 (2) (2019) 30–58.

[38] M. Ishihara, E. Muller, Software piracy and outsourcing in two-sided markets, Ouantitative Mark. Econ. 18 (1) (2020) 61–124.

[39] H. Cavusoglu, H. Cavusoglu, X. Geng, Bloatware and jailbreaking: strategic impacts of consumer-initiated modification of technology products, Inf. Syst. Res. 31 (1) (2020) 240–257.

[40] H.K. Bhargava, B.C. Kim, D. Sun, Commercialization of platform technologies: launch timing and versioning strategy, Prod. Operations Manag. 22 (6) (2013) 1374–1388.

[41] Z. He, T. Cheng, J. Dong, S. Wang, Evolutionary location and pricing strategies for service merchants in competitive O2O markets, Eur. J. Oper. Res. 254 (2) (2016) 595–609.

[42] O’Flaherty, K. (2020). This Is How You Can Hack An Apple iPhone Using An Android Device. Retrieved from https://www.forbes.com/sites/kateoflahertyuk 2020/03/04/this-is-how-you-can-jailbreak-an-apple-iphone-using-an-android -device/?sh=2c07ad032271

[43] Hernandez, P. (2020). The nintendo switch hacking scene is chaos right now. Retrieved from https://www.theverge.com/2018/6/28/17501530/nintendo-swi tch-hacking-piracy-porn-bans.

[44] D.S. Banerjee, Software piracy: a strategic analysis and policy instruments, Int. J. Ind. Organ. 21 (1) (2003) 97–127.

[45] M. Peitz, P. Waelbroeck, Piracy of digital products: a critical review of the theoretical literature, Inf. Econ. Policy 18 (4) (2006) 449–476.

[46] H.K. Cheng, Y. Liu, Optimal software free trial strategy: the impact of network externalities and consumer uncertainty. Inf. Syst. Res. 23 (2) (2012) 488–504.

Yunhao Liu is currently a Ph.D. Candidate at the School of Management, Xi’an Jiaotong University and School of Data Science, City University of Hong Kong. His-research in terests include platform protection strategy and tourism forecasting. His-papers once appeared on Expert Systems with Applications and Current Issues in Tourism

Gengzhong Feng received his Ph.D. degree in Management Science and Engineering at the School of Management, Xi’an Jiaotong University. He is currently a professor at the School of Management, Xi’an Jiaotong University. He is the Director of Key Laboratory of Process Control & Efficiency Engineering of Ministry of Education, Vice President of Systems Engineering Society of China, and Vice Chairman of China Society of Logistics. His-research interests include information management and E-commerce, logistics and supply chain management, big data and data quality management. His-papers have been published on JAIS, DSS and other IS related journals.

Yangyang Sun is currently an assistant professor at the School of Economics & Manage ment. Nanjing University of Science and Technology. He received his Ph.D. from Xi’ar Jiaotong University and City University of Hong Kong, His-research interests include en terprise software pricing and information system management. His-work has been pub lished on IJPR, IMDS and other journals

Xiangyin Kong is currently an associate professor at the School of Management, Uni versity of Science and Technology of China. He received his Ph.D. degree from both the School of Management, Xi’an Jiaotong University, and the Department of Management Science, City University of Hong Kong. His-research interests include robust optimization, contract theory, and incentives mechanism design. His-papers have been published in top journals such as Operations Research and Marketing Science
