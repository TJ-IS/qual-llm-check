---
otero_id: 4160
otero_key: "TMJFTJXB"
title: "Engaging Voluntary Contributions in Online Communities: A Hidden Markov Model1"
authors: "Wei Chen; Xiahua Wei; Kevin Xiaoguo Zhu"
year: "2018"
journal: "MIS Quarterly"
doi: "10.25300/misq/2018/14196"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# ENGAGING VOLUNTARY CONTRIBUTIONS IN ONLINECOMMUNITIES: A HIDDEN MARKOV MODEL




---
奥特罗_id：4160
otero_key: "TMJFTJXB"
标题：“在线社区中进行自愿贡献：隐马尔可夫模型1”
作者：“陈伟；魏夏华；朱小国”
年份：“2018”
期刊：《管理信息系统季刊》
doi：“10.25300/misq/2018/14196”
查询：“构造”
来源：“https://ais.kexu.win”
图片下载：假
---
# 在在线社区中进行自愿贡献：隐马尔可夫模型


Wei Chen




陈伟


Eller College of Management, University of Arizona, Tucson, AZ 85721 U.S.A. {weichen@email.arizona.edu}




亚利桑那大学埃勒管理学院，图森，AZ 85721 美国 {weichen@email.arizona.edu}


Xiahua Wei




魏夏华


School of Business, University of Washington, Bothell, WA 98011 U.S.A. {xhwei@uw.edu}




华盛顿大学商学院，Bothell, WA 98011 U.S.A. {xhwei@uw.edu}


Kevin Xiaoguo Zhu




朱小国


Rady School of Management, University of California, San Diego, CA 92093-0553 U.S.A. {kxzhu@ucsd.edu}




加州大学拉迪管理学院，圣地亚哥，CA 92093-0553 U.S.A. {kxzhu@ucsd.edu}


User contribution is critical to online communities but also difficult to sustain given its public goods nature. This paper studies the design of IT artifacts to motivate voluntary contributions in online communities. We propose a dynamic approach, which allows the effect of motivating mechanisms to change across users over time. We characterize the dynamics of user contributions using a hidden Markov model (HMM) with latent motivation states under the public goods framework. We focus on three motivating mechanisms on transi tioning users between the latent states: reciprocity, peer recognition, and self-image. Based on Bayesian estimation of the model with user-level panel data, we identify three motivation states (low, medium, and high), and show that the motivating mechanisms, implemented through various IT artifacts, could work differently across states. Specifically, reciprocity is only effective to transition users from low to medium motivation state, whereas peer recognition can boost all users to higher states. And self-image shows no effect when a user is already in high motivation state, although it helps users in low and medium states move to the high state. Design simulations on our structural model provide additional insights into the consequences of changing specific IT artifacts. These findings offer implications for platform designers on how to motivate user contributions and build sustainable online communities.




用户贡献对于在线社区至关重要，但鉴于其公共产品性质也难以维持。本文研究了激励在线社区自愿贡献的 IT 工件的设计。我们提出了一种动态方法，它允许激励机制的效果随着时间的推移在用户之间发生变化。我们使用公共物品框架下具有潜在动机状态的隐马尔可夫模型（HMM）来描述用户贡献的动态。我们重点关注用户在潜在状态之间转换的三种激励机制：互惠、同伴认可和自我形象。基于使用用户级面板数据对模型进行贝叶斯估计，我们确定了三种动机状态（低、中和高），并表明通过各种 IT 工件实现的激励机制在不同状态下的工作方式可能有所不同。具体来说，互惠仅对用户从低动机状态过渡到中等动机状态有效，而同伴认可可以将所有用户提升到较高状态。当用户已经处于高动机状态时，自我形象没有任何作用，尽管它可以帮助处于低和中等状态的用户转移到高状态。对我们的结构模型的设计模拟提供了对更改特定 IT 工件的后果的额外见解。这些发现为平台设计者如何激励用户贡献和建立可持续的在线社区提供了启示。


Keywords: Online community, IT artifacts, voluntary contribution, dynamics of contribution, motivating mechanisms, structural modeling, public goods, hidden Markov model, Bayesian estimation




关键词：在线社区、IT制品、自愿贡献、贡献动态、激励机制、结构建模、公共物品、隐马尔可夫模型、贝叶斯估计


## Introduction




＃＃ 介绍


In the growing digital economy, online communities have become central in bringing together large numbers of geographically dispersed individuals to spark novel ideas, collaborate on inventions, and share knowledge (Boudreau and Lakhani 2009; Goh et al. 2016; von Hippel 2005). Users in many of these communities (e.g., knowledge sharing platforms such as StackExchange and Quora) usually contribute voluntarily without receiving monetary compensation. To engage user contributions in such a setting, online communities commonly design information technology (IT) artifacts as motivating mechanisms (Ma and Agarwal 2007; Ray et al. 2014). Among these motivating mechanisms, various forms of “gamification,” such as badges, votes, and status systems, have been widely adopted (Zichermann and Cunningham 2011).




在不断发展的数字经济中，在线社区已成为将大量地理分散的个人聚集在一起以激发新颖想法、协作发明和共享知识的核心（Boudreau 和 Lakhani 2009；Goh 等人 2016；von Hippel 2005）。许多此类社区（例如 StackExchange 和 Quora 等知识共享平台）的用户通常自愿贡献，而不会获得金钱补偿。为了在这种环境中吸引用户的贡献，在线社区通常将信息技术 (IT) 工件设计为激励机制（Ma 和 Agarwal 2007；Ray 等人 2014）。在这些激励机制中，徽章、投票和地位系统等各种形式的“游戏化”已被广泛采用（Zichermann and Cunningham 2011）。


Despite their growing popularity, such design efforts do not always achieve positive results. Most of the online communities (even famous ones like Wikipedia) face the challenge of declining user participation over time (Simonite 2013). In particular, inappropriate design could alienate users and drive them away. For instance, Wikipedia’s quality control mechanism was counterproductive in retaining new users (Halfaker et al. 2013). In the case of the social news aggregator Digg.com, the redesign efforts angered users and lost them to competitors (Metz 2012). While social comparison can encourage users below the median to contribute more, users above the median could decrease their contribution to conform to the social norm (Chen et al. 2010). Goal-setting can induce users to exert efforts, but it can also reduce efforts after users reach the goals (Goes et al. 2016).




尽管它们越来越受欢迎，但此类设计努力并不总能取得积极成果。大多数在线社区（甚至像维基百科这样的著名社区）都面临着用户参与度随着时间的推移而下降的挑战（Simonite 2013）。特别是，不恰当的设计可能会疏远用户并将他们赶走。例如，维基百科的质量控制机制在留住新用户方面效果适得其反（Halfaker et al. 2013）。以社交新闻聚合器 Digg.com 为例，重新设计的努力激怒了用户，并将他们输给了竞争对手（Metz 2012）。虽然社会比较可以鼓励低于中位数的用户做出更多贡献，但高于中位数的用户可能会减少贡献以符合社会规范（Chen 等人，2010）。目标设定可以诱导用户付出努力，但也可以在用户达到目标后减少努力（Goes et al. 2016）。


From a theoretical perspective, the design of such mechanisms is related to individual motivations, which are extensively studied in the literature (e.g., Ma and Agarwal 2007; Porter and Donthu 2008). Yet, these motivations are usually theorized as static, even though recent research suggests that users’ contribution patterns exhibit significant dynamics (Sauermann and Franzoni 2015). Fitting a static model to data generated by a dynamic process may result in misleading findings. To the best of our knowledge, no prior work has empirically analyzed the dynamic relationship between motivating mechanisms and voluntary user contribution in online communities. This leaves a gap in our understanding of how a user’s motivation and contribution are dynamically influenced by the design of motivating mechanisms.




从理论角度来看，此类机制的设计与个人动机有关，这在文献中得到了广泛研究（例如，Ma 和 Agarwal 2007；Porter 和 Donthu 2008）。然而，这些动机通常被理论上认为是静态的，尽管最近的研究表明用户的贡献模式表现出显着的动态（Sauermann 和 Franzoni 2015）。将静态模型拟合到动态过程生成的数据可能会导致误导性的结果。据我们所知，之前的工作还没有实证分析在线社区中激励机制与用户自愿贡献之间的动态关系。这使得我们对用户的动机和贡献如何受到激励机制的设计动态影响的理解存在差距。


In this paper, we focus on the design of motivating mechanisms through IT artifacts when user motivations can change, and investigate the following research questions: (1) What kinds of mechanisms and IT artifacts are effective to transfer users among different levels of motivation? (2) How much would users contribute given their levels of motivation? An understanding of the dynamic effect along these two dimensions is essential to better design IT artifacts and effectively motivate user contributions.




在本文中，我们重点关注用户动机发生变化时通过IT工件设计激励机制，并探讨以下研究问题：（1）什么样的机制和IT工件能够有效地在不同动机级别之间转移用户？ (2) 考虑到用户的动机水平，他们会贡献多少？了解这两个维度的动态效应对于更好地设计 IT 工件和有效激励用户贡献至关重要。


In contrast to the literature, we take a dynamic approach. Specifically, we propose a structural econometric model, in which we integrate a hidden Markov model (HMM) into the public goods framework. This structural approach characterizes the dynamics of user contributions with different motivation states, as well as the transition between the states. With a unique panel data set collected from a knowledgesharing community, we use Bayesian estimation to jointly estimate the effect of motivating mechanisms on transition probabilities between the states, and user contributions conditional on their motivation states.




与文献相反，我们采取动态方法。具体来说，我们提出了一种结构计量经济学模型，其中我们将隐马尔可夫模型（HMM）集成到公共物品框架中。这种结构方法描述了具有不同动机状态的用户贡献的动态以及状态之间的转换。通过从知识共享社区收集的独特面板数据集，我们使用贝叶斯估计来共同估计激励机制对状态之间转移概率的影响，以及取决于其动机状态的用户贡献。


We find that the same motivating mechanism could work differently across states. For example, reciprocity is only effective to transition users from low to medium motivation state, whereas peer recognition (such as votes and acceptance from other users) is effective to elevate all users to the high motivation state. Badges are effective to transfer a low- or mediummotivation user to the high motivation state, but surprisingly, they show no effect when a user is already in the high motivation state. We also find that users do respond more to the demand of knowledge (i.e., number of questions that match their expertise) when they are in higher motivation states. These results provide important implications for the design of IT artifacts in online communities, and open up a new area for community managers to explore.




我们发现，相同的激励机制在不同州可能发挥不同的作用。例如，互惠仅能有效地将用户从低动机状态转变为中动机状态，而同伴认可（例如其他用户的投票和接受）能有效地将所有用户提升到高动机状态。徽章可以有效地将低或中等动机的用户转移到高动机状态，但令人惊讶的是，当用户已经处于高动机状态时，它们就没有任何效果。我们还发现，当用户处于较高动机状态时，他们确实会对知识需求（即与他们的专业知识相匹配的问题数量）做出更多反应。这些结果为在线社区中 IT 工件的设计提供了重要的启示，并为社区管理者开辟了一个探索的新领域。


Our research has several features. First, we advance the literature from the conventional static approach to a dynamic perspective on voluntary user contributions, bringing about managerial insights unavailable in prior studies. Second, our structural model helps advance the modeling approach in the online community literature, as it explicitly characterizes the dynamics of user contributions at the individual level. Third, our dynamic approach provides more nuanced insights into an increasingly important mode of open collaboration, and is applicable to a wide range of online communities where user contributions are voluntary and fluctuate over time (Xu et al 2012).




我们的研究有几个特点。首先，我们将文献从传统的静态方法推进到关于自愿用户贡献的动态视角，带来了先前研究中无法获得的管理见解。其次，我们的结构模型有助于推进在线社区文献中的建模方法，因为它明确地表征了个人层面上用户贡献的动态。第三，我们的动态方法为日益重要的开放协作模式提供了更细致的见解，并且适用于用户贡献自愿且随时间波动的广泛在线社区（Xu et al 2012）。


## Literature Review




＃＃ 文献综述


We draw on the literature to build a theory of dynamic motivation and contribution in online communities. We first examine factors that affect user motivation, and illustrate how the design of IT artifacts can influence contribution through various motivations. Then we identify the dynamics of motivation and contribution as a gap in the literature, which motivates our hidden Markov model to characterize such dynamics.




我们借鉴文献建立了在线社区动态动机和贡献的理论。我们首先研究影响用户动机的因素，并说明 IT 工件的设计如何通过各种动机影响贡献。然后，我们将动机和贡献的动态确定为文献中的空白，这促使我们的隐马尔可夫模型来表征这种动态。


## User Motivation and IT Artifacts as Motivating Mechanisms




## 用户动机和 IT 工件作为激励机制


In online communities, motivation is the key driver of user contribution. The literature has distinguished three types of motivations: intrinsic, extrinsic, and internalized extrinsic motivation (for a review, see von Krogh et al. 2012). Intrinsic motivation stems from intrinsic benefits, such as joy, fulfilment, and self-efficacy (Kankanhalli et al. 2005; Ray et al. 2014). In contrast, extrinsic motivation is driven by economic rewards such as career prospects (Huang and Zhang 2016; Roberts et al. 2006).




在在线社区中，动机是用户贡献的关键驱动力。文献区分了三种类型的动机：内在动机、外在动机和内化外在动机（有关综述，请参见 von Krogh 等人，2012 年）。内在动机源于内在利益，例如快乐、成就感和自我效能（Kankanhalli et al. 2005；Ray et al. 2014）。相比之下，外在动机是由职业前景等经济回报驱动的（Huang 和Zhang，2016 年；Roberts 等人，2006 年）。


Internalized extrinsic motivation is unique, in that it arises from external influences at first, but users can assimilate these influences and perceive them as self-regulating behavior rather than external impositions (Deci and Ryan 2002). In online communities, internalized extrinsic motivation includes reciprocity and reputation (von Krogh et al. 2012). Reputation can be further classified as peer recognition and selfimage. We discuss these three factors below.




内化的外在动机是独特的，因为它最初是由外部影响产生的，但用户可以吸收这些影响并将其视为自我调节行为而不是外部强加（Deci and Ryan 2002）。在在线社区中，内在的外在动机包括互惠和声誉（von Krogh et al. 2012）。声誉可以进一步分为同行认可和自我形象。我们下面讨论这三个因素。


First, reciprocity suggests that users who have received others’ help tend to return the favor. It is shown to drive contributions in open source software (Lakhani and von Hippel 2003; Zhu and Zhou 2012) and online communities (Chiu et al. 2006). Second, social interactions, especially peer recognition, validate users that their role in the community is expected (Ray et al. 2014). This identity-verification process enhances the confidence of contributors, and reassures users to contribute with their unique identity (Ma and Agarwal 2007). Third, concerns over self-image can also motivate contribution, as people care about the way others perceive them (Bénabou and Tirole 2006). In online communities, it is common that users contribute in order to earn respect from others and build a better image (Kankanhalli et al. 2005). It is also shown that self-image is important to drive participation in social media (Toubia and Stephen 2013).




首先，互惠意味着接受过他人帮助的用户往往会回报他人的帮助。它被证明可以推动开源软件（Lakhani 和 von Hippel，2003 年；Zhu 和 Zhou，2012 年）和在线社区（Chiu 等人，2006 年）的贡献。其次，社交互动，尤其是同伴认可，可以验证用户在社区中的角色是否符合预期（Ray et al. 2014）。这种身份验证过程增强了贡献者的信心，并让用户放心地使用其独特的身份进行贡献（Ma 和 Agarwal 2007）。第三，对自我形象的关注也可以激发贡献，因为人们关心别人如何看待他们（Bénabou and Tirole 2006）。在在线社区中，用户做出贡献是为了赢得他人的尊重并建立更好的形象（Kankanhalli et al. 2005）。研究还表明，自我形象对于推动社交媒体参与非常重要（Toubia 和 Stephen 2013）。


Through its influence on internalized extrinsic motivation, an online community can affect users’ contribution by employing various IT artifacts as motivating mechanisms (Ma and Agarwal 2007; Peng and Dey 2013). Examples of such IT artifacts include points, badges, status, reputation systems, and other features that facilitate verification of self-identity (e.g., Khansa et al. 2015). Among various IT artifacts, we focus on three types of mechanisms that support reciprocity, peer recognition, and self-image specific to our research context of knowledge-sharing online communities. First, users whose questions have been answered by others may be more likely to answer others’ questions in return. Second, users may care about the evaluation from their peers, through IT artifacts that facilitate user interactions, such as up-votes and acceptance of answers. Third, the community awards badges to users when they contribute, which improves users’ selfimage and serves as a signaling mechanism.




通过对内在外在动机的影响，在线社区可以通过使用各种 IT 工件作为激励机制来影响用户的贡献（Ma 和 Agarwal 2007；Peng 和 Dey 2013）。此类 IT 工件的示例包括积分、徽章、状态、声誉系统以及其他有助于验证自我身份的功能（例如，Khansa 等人，2015 年）。在各种 IT 工件中，我们重点关注三种类型的机制，这些机制支持互惠、同行认可和自我形象，这些机制专门针对我们知识共享在线社区的研究背景。首先，问题已被其他人回答过的用户可能更有可能回答其他人的问题。其次，用户可能会通过促进用户交互的 IT 工件（例如投票和接受答案）来关心同行的评价。第三，社区在用户做出贡献时向其授予徽章，这提高了用户的自我形象并起到了信号机制的作用。


## Dynamics of Motivation and Contribution




## 动机和贡献的动力


Despite the growing literature on user motivations and motivating mechanisms, a majority of these studies build on an implicit static assumption. That is, the relationship between motivating mechanisms and user contributions does not change over time. This is a strong assumption, especially if we examine user contributions over a long time. It is because user motivations often evolve with their changing personal characteristics and their interactions with the community via the channel of various IT artifacts, leading to the fluctuation of contributions (Franzoni and Sauermann 2014).




尽管有关用户动机和激励机制的文献越来越多，但大多数研究都建立在隐含的静态假设之上。也就是说，激励机制和用户贡献之间的关系不会随着时间的推移而改变。这是一个强有力的假设，特别是如果我们长期检查用户贡献的话。这是因为用户的动机往往随着个人特征的变化以及通过各种IT工件与社区的互动而变化，从而导致贡献的波动（Franzoni and Sauermann 2014）。


The internalized extrinsic motivation and the facilitating IT artifacts may have different effects when user motivations are evolving. We expect reciprocity to enhance user motivation. But this effect may be less salient for highly motivated individuals because they contribute disproportionally more than they receive. For peer recognition, users may feel satisfied with their current good reputation and not contribute further. Indeed, research finds that users may decrease their contributions after reaching a certain incentive hierarchy (Goes et al. 2016). With large amount of badges, users may suffer from the “moral licensing” effect, where people may feel justified behaving non-prosocially when they have done something prosocial (Gneezy et al. 2012). Having contributed to the online community and been endorsed by badges, users may sit on their laurels and feel entitled not to contribute subsequently.




当用户动机不断变化时，内在的外在动机和促进 IT 工件可能会产生不同的效果。我们希望互惠能够增强用户的积极性。但对于积极性高的人来说，这种影响可能不太明显，因为他们的贡献远大于他们得到的。对于同行认可，用户可能会对自己当前的良好声誉感到满意，而不会进一步做出贡献。事实上，研究发现，用户在达到一定的激励等级后可能会减少贡献（Goes et al. 2016）。有了大量的徽章，用户可能会受到“道德许可”效应的影响，当人们做了亲社会的事情时，他们可能会觉得自己的非亲社会行为是合理的（Gneezy et al. 2012）。在为在线社区做出贡献并获得徽章认可后，用户可能会坐享其成，并觉得自己有权不再做出贡献。


Modeling the dynamic process in a static way leads to problematic estimation and misleading implications. In this paper, we propose a theoretical framework of dynamics that differs from the literature in two dimensions. First, we propose motivation state as a general construct to characterize the individual’s propensity to contribute, and model it as a mediator between the motivating mechanisms and user contributions. Second, we relax the assumption that an individual’s motivation state is fixed, and allow it to change over time. Our model also allows the impact of motivating mechanisms to be heterogeneous when users are in different motivation states. As such, we introduce a general model to explain the dynamics of user contributions.




以静态方式对动态过程进行建模会导致估计问题和误导性影响。在本文中，我们提出了一个在两个维度上不同于文献的动力学理论框架。首先，我们提出将动机状态作为描述个人贡献倾向的一般结构，并将其建模为激励机制和用户贡献之间的中介。其次，我们放宽了个人动机状态是固定的假设，并允许它随着时间的推移而改变。当用户处于不同的动机状态时，我们的模型还允许激励机制的影响是异质的。因此，我们引入了一个通用模型来解释用户贡献的动态。


Further, our approach has an evident empirical advantage. Prior studies use survey data to measure the psychological state of contributing (e.g., Ray et al. 2014). However, these constructs are hard to quantify with consensus. It is also costly to survey a large number of users over time to reveal the dynamics. Instead, we use observational data to infer motivation states and characterize individual dynamics. This approach enables community managers to estimate the dynamic motivation states of all users.




此外，我们的方法具有明显的经验优势。先前的研究使用调查数据来衡量贡献的心理状态（例如，Ray et al. 2014）。然而，这些结构很难量化并达成共识。随着时间的推移对大量用户进行调查以揭示动态的成本也很高。相反，我们使用观察数据来推断动机状态并表征个人动态。这种方法使社区管理者能够估计所有用户的动态动机状态。


We make a distinction between the dynamics at the community level and at the individual user level. At the community level, the dynamics may come from membership turnover (Butler 2001). Recent studies find that more turnover may be better for the community at the knowledge-retention stage of the life cycle (Ransbotham and Kane 2011). However, it remains unclear how dynamics at the aggregated level may come from individual-level behaviors, and what mechanisms community designers can use to promote the desired outcome. To narrow this gap, we focus on the dynamics of user motivation and contribution at the individual level.




我们区分社区层面和个人用户层面的动态。在社区层面，动态可能来自会员流动（Butler 2001）。最近的研究发现，在生命周期的知识保留阶段，更多的人员流动可能对社区更好（Ransbotham 和 Kane，2011）。然而，目前尚不清楚总体层面的动态如何来自个人层面的行为，以及社区设计者可以使用哪些机制来促进期望的结果。为了缩小这一差距，我们关注个人层面的用户动机和贡献的动态。


## Model the Dynamics of User Contribution




## 对用户贡献的动态进行建模


One challenge of capturing individual-level dynamics is that the structure of such dynamics is usually unobservable. To capture this latent structure, the discrete state space model is a useful approach in the literature (e.g., Heckman 1981). For example, an individual’s present decision depends on his past decision. In most of these models, the states are observable (e.g., brand switching of customers). Still, they tend to ignore other dynamics that could contribute to the change of states. In many other scenarios, however, we cannot observe the underlying states that drive the individual-level dynamics (e.g., motivation states in our research context). In this case, the hidden Markov model (HMM) can be useful.




捕获个体层面动态的一大挑战是这种动态的结构通常是不可观察的。为了捕获这种潜在结构，离散状态空间模型是文献中一种有用的方法（例如，Heckman 1981）。例如，一个人现在的决定取决于他过去的决定。在大多数这些模型中，状态是可观察的（例如，客户的品牌转换）。尽管如此，他们往往忽视了可能导致状态变化的其他动力。然而，在许多其他场景中，我们无法观察驱动个体层面动态的潜在状态（例如，我们研究背景中的动机状态）。在这种情况下，隐马尔可夫模型（HMM）会很有用。


An HMM is a stochastic process that consists of three elements: a finite set of hidden states, observed outcomes conditional on the hidden state, and the probabilities of transitioning from one state to another. It has wide applications in modeling stock market volatility (e.g., Rydén et al. 1998), business cycles (e.g., Hamilton 1989), customer relationship management (Netzer et al. 2008), and the mental states of patients in healthcare communities (Yan and Tan 2014). As far as we are aware, HMM has not yet been applied to modeling user contributions in online communities. Furthermore, we incorporate HMM into the public goods model (Bénabou and Tirole 2006) to formalize the dynamic effect of motivating mechanisms. This structural modeling approach allows us to explicitly characterize the dynamics of user contributions at the individual level.




HMM 是一个随机过程，由三个元素组成：一组有限的隐藏状态、以隐藏状态为条件的观察结果以及从一种状态转换到另一种状态的概率。它在模拟股票市场波动性（例如，Rydén 等人，1998 年）、商业周期（例如，Hamilton，1989 年）、客户关系管理（Netzer 等人，2008 年）以及医疗保健社区患者的心理状态（Yan 和 Tan，2014 年）方面具有广泛的应用。据我们所知，HMM 尚未应用于对在线社区中的用户贡献进行建模。此外，我们将 HMM 纳入公共物品模型（Bénabou 和 Tirole 2006），以形式化激励机制的动态效应。这种结构建模方法使我们能够在个人层面上明确地描述用户贡献的动态。


## Research Design




## 研究设计


To characterize the dynamics of user contributions, we develop an HMM model as shown in Figure 1. It illustrates how a user could switch between motivation states through various motivating schemes, and how his contribution probability depends on the states. Specifically, our HMM model has three elements:




为了表征用户贡献的动态特征，我们开发了一个 HMM 模型，如图 1 所示。它说明了用户如何通过各种激励方案在动机状态之间切换，以及他的贡献概率如何取决于状态。具体来说，我们的 HMM 模型具有三个要素：


(1) We model users with different hidden motivation states, with 1 being the lowest and J the highest. The state captures the strength of motivation to contribute. At any time t, a user is in only one state.




(1) 我们对具有不同隐藏动机状态的用户进行建模，其中 1 最低，J 最高。国家抓住了贡献动力的力量。在任何时间t，用户仅处于一种状态。


(2) From time t-1 to t, the user could switch to any state with certain probability, which is affected by the user’s interaction with the community, such as how his contribution is evaluated by the peers. The community interactions are enabled by various IT artifacts that work through motivating mechanisms (e.g., reciprocity, peer recognition, and self-image).




（2）从时间t-1到t，用户可以以一定的概率切换到任何状态，这受到用户与社区互动的影响，例如他的贡献被同行如何评价。社区互动是通过各种 IT 工件实现的，这些工件通过激励机制（例如互惠、同行认可和自我形象）发挥作用。


(3) Conditional on his state in t, a user may respond differently to community and individual characteristics (e.g., size of the community and the demand for knowledge). We can observe this state-dependent response as his level of contributions in t.




(3) 根据 t 中的状态，用户可能会对社区和个人特征（例如社区的规模和知识需求）做出不同的反应。我们可以将这种依赖于状态的响应观察为他在 t 中的贡献水平。


This model can be applicable to various online communities, as long as user motivation is unobservable, user contributions fluctuate, and the goal of the community managers is to motivate user contributions by designing appropriate IT artifacts.




该模型可以适用于各种在线社区，只要用户动机不可观察，用户贡献波动，并且社区管理者的目标是通过设计适当的IT工件来激励用户贡献。


## Research Context




## 研究背景


We study our research questions in an online community called StackExchange (stackexchange.com), which is a representative, large knowledge-sharing platform based on Wikipedia-style voluntary contributions. It started in 2008 with StackOverflow, a knowledge sharing website on programming. Now it has expanded to more than 100 subsites covering widespread technical (e.g., math, Tex) and nontechnical (e.g., cooking, bicycle) topics. On each subsite, users ask topic-related questions and provide answers. Users can also vote, comment, and revise other users’ questions and answers as they do in Wikipedia, which allows the community to improve the content collectively.




我们在一个名为 StackExchange (stackexchange.com) 的在线社区中研究我们的研究问题，这是一个基于维基百科式自愿贡献的代表性大型知识共享平台。它始于 2008 年 StackOverflow，一个编程知识共享网站。现在它已扩展到 100 多个子站点，涵盖广泛的技术（例如数学、德克萨斯）和非技术（例如烹饪、自行车）主题。在每个子网站上，用户提出与主题相关的问题并提供答案。用户还可以像在维基百科中一样投票、评论和修改其他用户的问题和答案，这使得社区能够集体改进内容。


Like many other online communities, StackExchange faces the challenge to maintain user participation. To cope with this, StackExchange employs various mechanisms to encourage user contribution and to sustain the high quality of questions and answers. For example, when a user receives 10 upvotes on one of his answers, he earns a “Nice Answer” badge. If the answer receives more than 40 up-votes and is accepted by the question poster, he is rewarded a “Guru” badge. Our sample includes 158 types of badges and they have been awarded for 414,761 times. A user can also earn reputation points, which are displayed together with the badges right below the user name on the profile page. These mechanisms serve as important channels for the users’ identity verification.




与许多其他在线社区一样，StackExchange 面临着维持用户参与的挑战。为了应对这一问题，StackExchange 采用各种机制来鼓励用户贡献并维持高质量的问题和答案。例如，当用户对其某个答案获得 10 票赞成时，他将获得“好答案”徽章。如果答案获得超过 40 票赞成并被问题发布者接受，他将获得“大师”徽章。我们的样本包括 158 种徽章，获奖次数为 414,761 次。用户还可以获得声誉积分，这些积分与徽章一起显示在个人资料页面上用户名的正下方。这些机制是用户身份验证的重要渠道。


These features help us understand user behaviors when knowledge collaboration is organized in such a voluntary community. First, it provides detailed data about user interactions. For example, we can observe when a user receives an up-vote on his answer, and whether his answer has been accepted. Such fine-grained user-level data help us identify the effect of different interactions on users’ transition probabilities. Second, as many other online communities are using similar motivating mechanisms, our analysis could be generalized in a broader sense. For example, peer voting is used in crowdsourcing ideation initiatives (Huang et al. 2014), and the badge system is one important device in many online communities (Piskorski et al. 2010).




当在这样一个自愿社区中组织知识协作时，这些功能有助于我们理解用户行为。首先，它提供有关用户交互的详细数据。例如，我们可以观察用户何时收到对其答案的赞成票，以及他的答案是否已被接受。这种细粒度的用户级数据有助于我们识别不同交互对用户转换概率的影响。其次，由于许多其他在线社区正在使用类似的激励机制，因此我们的分析可以在更广泛的意义上进行推广。例如，众包创意活动中使用了同行投票（Huang et al. 2014），徽章系统是许多在线社区的重要设备之一（Piskorski et al. 2010）。


![](/api/attachments/TMJFTJXB/fulltext/images/13e350dad6526012909c1785b3d316ca6a0373f2c8db1436ac7cd96b811132bc.jpg)  
Figure 1. Hidden Markov Model of User Contributions




![](/api/attachments/TMJFTJXB/fulltext/images/13e350dad6526012909c1785b3d316ca6a0373f2c8db1436ac7cd96b811132bc.jpg)  
图 1. 用户贡献的隐马尔可夫模型


## Data




＃＃ 数据


Our data comes from SuperUser.com, a subsite of StackExchange, for computer enthusiasts and power users. We employ SuperUser because of its data quality, as it is one of the largest subsites on StackExchange by the number of contributions. It employs various mechanisms to engage users, such as voting and badge systems. Hence, the site has rich information on user interactions that are appropriate to study our research questions.




我们的数据来自 SuperUser.com，这是 StackExchange 的子网站，面向计算机爱好者和高级用户。我们使用 SuperUser 是因为它的数据质量，因为它是 StackExchange 上贡献数量最大的子网站之一。它采用各种机制来吸引用户，例如投票和徽章系统。因此，该网站拥有丰富的用户交互信息，适合研究我们的研究问题。


SuperUser was launched in July 2009, and has accumulated about 214,000 questions and over 351,000 answers by April 2014. We collected detailed data on daily activities of each user from July 12, 2009, to March 1, 2012 (964 days). We only include users who contributed at least 10 answers during the sample period.<sup>2</sup> Our full sample contains 2,147 users who have contributed 127,360 out of the 157,375 answers, equivalent to 26,200 hours of work.<sup>3</sup> Because these users make over 80% of the contributions, it is critical to understand their behaviors.




SuperUser于2009年7月推出，截至2014年4月已积累约214,000个问题和超过351,000个答案。我们收集了2009年7月12日至2012年3月1日（964天）每个用户日常活动的详细数据。我们仅包含在样本期间贡献了至少 10 个答案的用户。<sup>2</sup>我们的完整样本包含 2,147 个用户，他们贡献了 157,375 个答案中的 127,360 个答案，相当于 26,200 个小时的工作时间。<sup>3</sup>由于这些用户贡献了超过 80% 的贡献，因此了解他们的行为至关重要。


## Community and User Level Trends




## 社区和用户级别趋势


We first demonstrate the general trends of the data in Figure 2. With the exception of the surge around the launch of the community, the numbers of new questions (graph a) and answers (graph b) are relatively stable over time. Similarly, the trends are stable for the numbers of badges and up-votes, as shown in graphs (d) and (e), respectively. Graph (c) plots the number of accepted answers each day. The stable trend suggests that question posters deem the quality of answers being consistent over time. We also plot in graph (f) the average up-votes per answer, which indicates the overall quality of the answers in the community. The trend is stable except for a decline at the initial stage. Overall, SuperUser is a relatively healthy community with steady contributions in our sample.




我们首先展示图 2 中数据的总体趋势。除了社区启动前后的激增之外，新问题（图 a）和答案（图 b）的数量随着时间的推移相对稳定。同样，徽章和赞成票数量的趋势也很稳定，分别如图 (d) 和 (e) 所示。图 (c) 绘制了每天接受的答案数量。稳定的趋势表明问题发布者认为答案的质量随着时间的推移是一致的。我们还在图 (f) 中绘制了每个答案的平均赞成票，这表明了社区中答案的整体质量。除初期有所下降外，走势平稳。总体而言，SuperUser 是一个相对健康的社区，在我们的样本中贡献稳定。


The contributions at the individual level, however, show a different pattern. Figure 3(a) presents the average number of answers contributed by each user over time. The contribution shows a declining trend. However, some users stay for a long time in the community. Figure 3(b) shows a histogram of contribution tenure, which is defined as the days between the first and last answers of each user. We can see significant heterogeneity in the time span during which users contribute. For those users contributing for a long time, understanding their behaviors and motivations can help develop sustainable online communities.




然而，个人层面的贡献却呈现出不同的模式。图 3(a) 显示了一段时间内每个用户贡献的平均答案数。贡献率呈现下降趋势。然而，有些用户在社区中停留的时间较长。图 3(b) 显示了贡献期限的直方图，其定义为每个用户的第一个答案和最后一个答案之间的天数。我们可以看到用户贡献的时间跨度存在显着的异质性。对于那些长期贡献的用户，了解他们的行为和动机有助于发展可持续的在线社区。


![](/api/attachments/TMJFTJXB/fulltext/images/fd43b4e8219f533cf02eec506451580790dd66d30d513fc490e9be2c2b6d01a8.jpg)




![](/api/attachments/TMJFTJXB/fulltext/images/fd43b4e8219f533cf02eec506451580790dd66d30d513fc490e9be2c2b6d01a8.jpg)


![](/api/attachments/TMJFTJXB/fulltext/images/187e0fd5413d3a1d3597c81ebebe3b61ed0388873da196925d129f54e46446d3.jpg)




![](/api/attachments/TMJFTJXB/fulltext/images/187e0fd5413d3a1d3597c81ebebe3b61ed0388873da196925d129f54e46446d3.jpg)


![](/api/attachments/TMJFTJXB/fulltext/images/7bc72645b43ef8eb14231373af778ffca6ab4b6ef06bccafa0e6ab8e6256d6e5.jpg)




![](/api/attachments/TMJFTJXB/fulltext/images/7bc72645b43ef8eb14231373af778ffca6ab4b6ef06bccafa0e6ab8e6256d6e5.jpg)


(d) Total Number of Badges  
![](/api/attachments/TMJFTJXB/fulltext/images/ca1fd5ddb8cae036a2c39726493e74a3a51a007ea8f6d2d6beef48db02bf35c2.jpg)  
Figure 2. Trends of Key Variables




(d) 徽章总数  
![](/api/attachments/TMJFTJXB/fulltext/images/ca1fd5ddb8cae036a2c39726493e74a3a51a007ea8f6d2d6beef48db02bf35c2.jpg)  
图 2. 关键变量的趋势


(e) Total Number of Up-votes  
![](/api/attachments/TMJFTJXB/fulltext/images/0e09bc1fe6074d8dbd9a1c0b8697d16084a64aa7e39cc5a3479774fd8a1fb222.jpg)




(e) 赞成票总数  
![](/api/attachments/TMJFTJXB/fulltext/images/0e09bc1fe6074d8dbd9a1c0b8697d16084a64aa7e39cc5a3479774fd8a1fb222.jpg)


(f) Average Final Upvotes on Answers  
![](/api/attachments/TMJFTJXB/fulltext/images/5e9f62be1a04356573b9c5b1c860c39fce37a3640ade6ac0b96fa0efbe10c9e9.jpg)




(f) 答案的平均最终赞成票  
![](/api/attachments/TMJFTJXB/fulltext/images/5e9f62be1a04356573b9c5b1c860c39fce37a3640ade6ac0b96fa0efbe10c9e9.jpg)


![](/api/attachments/TMJFTJXB/fulltext/images/81dfaa4833af349b8b9316e6fc276e2c91c2e780fb77d911b689a7a0c9b468a5.jpg)




![](/api/attachments/TMJFTJXB/fulltext/images/81dfaa4833af349b8b9316e6fc276e2c91c2e780fb77d911b689a7a0c9b468a5.jpg)


(b) Tenure Length Distribution of Users  
![](/api/attachments/TMJFTJXB/fulltext/images/44fcd42c58284c5b18464af105b4c7130420c2e65c3f9271f68b0c79070ce089.jpg)  
Figure 3. Average Answers over Time and Tenure Distribution




(b) 用户使用期限分布  
![](/api/attachments/TMJFTJXB/fulltext/images/44fcd42c58284c5b18464af105b4c7130420c2e65c3f9271f68b0c79070ce089.jpg)  
图 3. 随时间变化的平均答案和任期分布


We further drill down to the individual level and plot the contributions of five representative users from our sample in Figure 4 (user IDs anonymized). Each row shows the answers of a user over the sample period. Each point represents the number of answers contributed by that user. A point is missing if the user does not contribute at a particular time. We observe that even relatively active users exhibit substantial fluctuation of contributions during their tenure. They actively contribute for some time periods, while idling for other periods. Our goal is to model the fluctuation of user contributions (dynamics), and study the influence of different motivating mechanisms that drive such dynamics of active (or lack of) contributions.




我们进一步深入到个人级别，并绘制了图 4 中样本中五个代表性用户的贡献（用户 ID 已匿名）。每行显示用户在样本期间的答案。每个点代表该用户贡献的答案数。如果用户在特定时间没有做出贡献，则缺少一分。我们观察到，即使是相对活跃的用户在其任期内的贡献也表现出巨大的波动。他们在某些时间段积极贡献，而在其他时间段闲置。我们的目标是对用户贡献（动态）的波动进行建模，并研究驱动主动（或缺乏）贡献动态的不同激励机制的影响。


## Model Development: Structural Modeling of User Behavior




## 模型开发：用户行为的结构建模


In this section, we describe the details of our structural model with HMM, where a user interacts with the community and decides his level of contribution.




在本节中，我们将描述使用 HMM 的结构模型的细节，其中用户与社区交互并决定他的贡献级别。


![](/api/attachments/TMJFTJXB/fulltext/images/ea123199fc78ff98b2e5822b13362bff1b54f5f2bce7f3a5cc3bfcd78fa70e8c.jpg)  
Figure 4. Fluctuation of User Contribution over Time




![](/api/attachments/TMJFTJXB/fulltext/images/ea123199fc78ff98b2e5822b13362bff1b54f5f2bce7f3a5cc3bfcd78fa70e8c.jpg)  
图 4. 用户贡献随时间的波动


## Modeling User Contribution as Public Goods




## 将用户贡献建模为公共物品


In online communities, user contributions are public goods in nature, because they are voluntary, free, and open. The key issue about public goods is free-riding, which means that everyone can share the benefits, but only the contributors incur the cost. Under-provision is a common equilibrium in many pure altruism models (e.g., Andreoni 1988). It follows that online communities may eventually be depleted, suffered from the “tragedy of the commons.” But these models are not adequate to explain why large groups, such as the Wikipedia community, are able to attract substantial user contributions. Such discrepancy between theoretical models and empirical phenomena may be reconciled by impure altruism models (e.g., Andreoni 1990; Bénebou and Tirole 2006), where individuals contribute because they obtain utilities not only from pure altruism, but also from their own private benefits, such as signalling personal skills or the fulfilment of helping others.




在网络社区中，用户的贡献本质上是公共产品，因为它们是自愿的、免费的、开放的。公共产品的关键问题是搭便车，即每个人都可以分享利益，但只有贡献者承担成本。在许多纯粹利他主义模型中，供给不足是一种常见的平衡（例如，Andreoni 1988）。由此可见，在线社区最终可能会耗尽，遭受“公地悲剧”。但这些模型不足以解释为什么维基百科社区等大型团体能够吸引大量用户贡献。理论模型和经验现象之间的这种差异可以通过不纯粹的利他主义模型来调和（例如，Andreoni 1990；Bénebou 和 Tirole 2006），其中个人做出贡献是因为他们不仅从纯粹的利他主义中获得效用，而且还从自己的私人利益中获得效用，例如表明个人技能或帮助他人的成就感。


We use the public goods framework, particularly the impure altruism models, to model user contributions in an online community. Each self-interested user chooses how much to contribute. A user’s net utility consists of three parts: (1) his valuation of the accumulated contribution (e.g., knowledge) in the community, (2) his valuation of his own contribution, and (3) his cost of contribution. The first part captures the benefit the user could obtain from the community, as suggested by the pure altruism literature. The second part captures the impure altruism, corresponding to internalized extrinsic motivations that we have reviewed in the “Literature Review” section. The third part suggests that making contributions is costly in terms of time and effort.




我们使用公共物品框架，特别是不纯粹的利他主义模型，来模拟在线社区中的用户贡献。每个自利的用户都会选择贡献多少。用户的净效用由三部分组成：（1）他对社区中累积贡献（例如知识）的评估，（2）他对自己贡献的评估，以及（3）他的贡献成本。第一部分描述了用户可以从社区获得的好处，正如纯粹利他主义文献所建议的那样。第二部分抓住了不纯粹的利他主义，对应于我们在“文献评论”部分中评论过的内在的外在动机。第三部分表明，做出贡献需要付出时间和精力的代价。


Assuming additive separability of the above three parts, we specify the utility function of user i at time t as




假设上述三部分可加分离，我们将用户 i 在时间 t 的效用函数指定为


$$
\begin{array}{l} {U _ {i t} \big (Y _ {i t}, X _ {i t}, W _ {i, t - 1}, Y _ {j \tau} \big) =} \\ {\gamma_ {i} \sum_ {\tau = 1} ^ {t} \sum_ {j = 1} ^ {N _ {\tau}} \delta^ {t - \tau} Y _ {j \tau} + f \big (X _ {i t}, W _ {i, t - 1} \big) \cdot Y _ {i t} - \frac {1}{2} c _ {i} Y _ {i t} ^ {2}} \end{array}\tag{1}
$$




$$
\begin{array}{l} {U _ {i t} \big (Y _ {i t}, X _ {i t}, W _ {i, t - 1}, Y _ {j \tau} \big) =} \\ {\gamma_ {i} \sum_ {\tau = 1} ^ {t} \sum_ {j = 1} ^ {N _ {\tau}} \delta^ {t - \tau} Y _ {j \tau} + f \big (X _ {i t}, W _ {i, t - 1} \big) \cdot Y _ {i t} - \frac {1}{2} c _ {i} Y _ {i t} ^ {2}} \end{array}\tag{1}
$$


where $Y _ { i t }$ is the contribution of user i at time t. Intuitively, a user gains utility from the accumulative knowledge in the community, and his own incremental contribution at present, net of his cost.




其中 $Y _ { i t }$ 是用户 i 在时间 t 的贡献。直观上，用户从社区中积累的知识以及他自己目前的增量贡献（扣除成本）中获得效用。


We choose such a functional form following Chen et al. (2010). The first term on the right hand side captures user i’s valuation of the accumulated contribution of the community, in which $\gamma _ { i }$ is user i’s marginal benefit from the accumulated contribution, $N _ { \tau }$ is the number of users in the community at time $\tau ,$ and δ is a discount factor of the contribution stock. In the second term, $f ( X _ { i t } , W _ { i , t - 1 } )$ captures user i’s valuation of his own contribution at time t. This could be viewed as a parsimonious version of the “image rewards” as in the prosocial behavior model (Bénabou and Tirole 2006), which will “depend on the informational and economic context, including what others are doing” (p. 1658). Therefore, this valuation could change over time with $X _ { i t } ,$ which is a vector of individual and community characteristics, and $W _ { i , t - 1 } ,$ which captures the community interactions in a vector. Essentially, in our model, a user’s valuation of his own contribution could fluctuate because of his changing interactions with peers in the community. The third term is the cost function. We use a quadratic cost function to capture the convex cost of contributions (Gu et al. 2007).




我们遵循 Chen 等人的观点选择了这样的函数形式。 （2010）。右侧第一项表示用户 i 对社区累计贡献的估值，其中 $\gamma _ { i }$ 是用户 i 从累计贡献中获得的边际收益，$N _ { \tau }$ 是 $\tau 时刻社区中的用户数量，$ 是贡献存量的折扣因子。在第二项中，$f ( X _ { i t } , W _ { i , t - 1 } )$ 捕获用户 i 在时间 t 时对其自身贡献的估值。这可以被视为亲社会行为模型中“形象奖励”的简约版本（Bénabou 和 Tirole 2006），它将“取决于信息和经济背景，包括其他人在做什么”（第 1658 页）。因此，这种估值可能会随着时间的推移而变化，其中 $X _ { i t } ,$ 是个人和社区特征的向量，$W _ { i , t - 1 } ,$ 捕获向量中的社区互动。本质上，在我们的模型中，用户对自己贡献的评价可能会因为他与社区中同伴的互动的变化而波动。第三项是成本函数。我们使用二次成本函数来捕获贡献的凸成本（Gu et al. 2007）。


Using the first order condition of Equation (1) with respect to $Y _ { i t } ,$ we obtain the equilibrium contribution of user i at time t as




使用方程（1）关于 $Y _ { i t } 的一阶条件，$ 我们得到用户 i 在时间 t 的均衡贡献为


$$
Y _ {i t} ^ {*} = \frac {\gamma_ {i} + f (X _ {i t} , W _ {i , t - 1})}{c _ {i}}\tag{2}
$$




$$
Y _ {i t} ^ {*} = \frac {\gamma_ {i} + f (X _ {i t} , W _ {i , t - 1})}{c _ {i}}\tag{2}
$$


For analytical tractability, we assume that $f ( X _ { i t } , W _ { i , t - 1 } )$ is linear in $X _ { i t }$ conditional on motivation state $s _ { i t } .$ And $s _ { i t }$ is further determined by a latent transition propensity $L ( W _ { i , t - 1 } )$ (details in the “Transition Probabilities of Motivation States” section, below). We then obtain




对于分析易处理性，我们假设 $f ( X _ { i t } , W _ { i , t - 1 } )$ 在 $X _ { i t }$ 中是线性的，条件是动机状态 $s _ { i t } .$ 并且 $s _ { i t }$ 进一步由潜在转换倾向 $L ( W _ { i , t - 1 } )$ 确定（详细信息见下文“动机状态的转变概率”部分）。然后我们得到


$$
Y _ {i t} ^ {*} = X _ {i t} ^ {\prime} \beta_ {s _ {i t}} + \varepsilon_ {i t}, \quad \left(\varepsilon_ {i t} | X _ {i t}, s _ {i t}\right) \sim N \left(0, \sigma^ {2}\right)\tag{3}
$$




$$
Y _ {i t} ^ {*} = X _ {i t} ^ {\prime} \beta_ {s _ {i t}} + \varepsilon_ {i t}, \quad \left(\varepsilon_ {i t} | X _ {i t}, s _ {i t}\right) \sim N \left(0, \sigma^ {2}\右)\标签{3}
$$


where $X _ { i t }$ is a vector of community and individual characteristics, the error term $\varepsilon _ { i t }$ follows a normal distribution with mean zero and variance $\sigma ^ { 2 } ,$ , and the individual marginal benefit parameter $\gamma _ { i }$ and cost coefficient $c _ { i }$ are represented by a constant term and time-varying individual characteristics in $X _ { i t } ,$ and the error term $\varepsilon _ { i t } .$




其中$X _ { i t }$是社区和个体特征的向量，误差项$\varepsilon _ { i t }$服从均值为零和方差$\sigma ^ { 2 } ,$的正态分布，个体边际收益参数$\gamma _ { i }$和成本系数$c _ { i }$由常数项和$X _ { i t 中随时间变化的个体特征表示} ,$ 和误差项 $\varepsilon _ { i t } .$


Our goal is to estimate the coefficient vector $\beta _ { s _ { i t } }$ , which captures the influence of vector $X _ { i t }$ on the user’s contribution $Y _ { i t } .$ Note that vector $\beta _ { s _ { i t } }$ depends on user i’s motivation state $s _ { i t } ,$ which is associated with user i’s previous interactions with the community $W _ { i , t - 1 }$ . We detail the motivation states and their transitions in our model below.




我们的目标是估计系数向量 $\beta _ { s _ { i t } }$ ，它捕获向量 $X _ { i t }$ 对用户贡献 $Y _ { i t } 的影响。$ 请注意，向量 $\beta _ { s _ { i t } }$ 取决于用户 i 的动机状态 $s _ { i t } ,$ 与用户 i 的动机状态相关联之前与社区的互动 $W _ { i , t - 1 }$ 。我们在下面的模型中详细介绍了动机状态及其转变。


## Motivation States in HMM




## HMM 中的动机状态


Our proposed HMM characterizes the dynamics of a user’s contribution as two stochastic processes: a process of observed contributions, and an underlying unobserved process of the user’s motivation states. We denote $s _ { i t }$ the state of user i at time t. A user can have J hidden motivation states: $s _ { i t } \in$ $S = \{ 1 , 2 , . . . , J \}$




我们提出的 HMM 将用户贡献的动态特征描述为两个随机过程：观察到的贡献过程和用户​​动机状态的潜在未观察过程。我们将 $s _ { i t }$ 表示用户 i 在时间 t 的状态。用户可以有 J 个隐藏动机状态： $s _ { i t } \in$ $S = \{ 1 , 2 , . 。 。 , J\}$


The hidden state captures the time-dependent feature of a user’s valuation of his own contribution (i.e., the strength of his motivation to contribute). If a user has high valuation of the contributions he provided to the community at time t-1 (i.e., in a high motivation state), he may also highly value his contributions at time t. Based on his state, a user responds differently to the community and individual characteristics (i.e., vector $X _ { i t } )$ . For example, if a user is in a high motivation state, he may be more likely to respond to new questions posted in the community. The observed contributions could be regarded as a noisy signal of the hidden state process. The hidden state and observed contributions together form a hidden Markov chain (Rabiner 1989).




隐藏状态捕获了用户对其自身贡献的评估的时间相关特征（即，他贡献的动机的强度）。如果用户对他在时间 t-1 为社区提供的贡献评价很高（即处于高动机状态），那么他也可能高度评价他在时间 t 的贡献。根据用户的状态，他对社区和个人特征（即向量 $X _ { i t } ）$ 做出不同的反应。例如，如果用户处于高积极性状态，他可能更有可能回答社区中发布的新问题。观察到的贡献可以被视为隐藏状态过程的噪声信号。隐藏状态和观察到的贡献一起形成隐藏马尔可夫链（Rabiner 1989）。


From time t-1 to $t ,$ a user may stay in one state, or switch to another. In our HMM, the state process $\left\{ S _ { i t } \right\} _ { t \geq 0 }$ is characterized as a first-order Markov chain with state space $S = \{ 1$ ， $2 , . . . , J \}$ . Together with $Y _ { i t } ,$ the observed contribution of user i at time t, we can model the vector-valued stochastic process $( Y _ { i t } , s _ { i t } )$ as a hidden Markov chain. Its probability of transition from one period to the next can be factorized as




从时间 t-1 到 $t ，$ 用户可能停留在一种状态，或者切换到另一种状态。在我们的 HMM 中，状态过程 $\left\{ S _ { i t } \right\} _ { t \geq 0 }$ 被表征为具有状态空间 $S = \{ 1$ ， $2 , 的一阶马尔可夫链。 。 。 , J \}$ 。结合 $Y _ { i t } ,$ 在时间 t 观察到的用户 i 的贡献，我们可以将向量值随机过程 $( Y _ { i t } , s _ { i t } )$ 建模为隐马尔可夫链。它从一个时期过渡到下一个时期的概率可以分解为


$$
P \big (Y _ {i t}, s _ {i t} | Y _ {i, t - 1}, s _ {i, t - 1} \big) = P \big (Y _ {i t} | s _ {i t} \big) \cdot p \big (s _ {i, t - 1}, s _ {i t} \big)
$$




$$
P \big (Y _ {i t}, s _ {i t} | Y _ {i, t - 1}, s _ {i, t - 1} \big) = P \big (Y _ {i t} | s _ {i t} \big) \cdot p \big (s _ {i, t - 1}, s _ {i t} \big)
$$


where $p ( s _ { i , t - 1 } , s _ { i t } )$ is the transition probability from state $s _ { i , t - 1 }$ to state $s _ { i t } ,$ and $P ( Y _ { i t } | S _ { i t } )$ is the conditional probability describing the state-dependent contributions. We elaborate these two probabilities in the next two sub-sections, respectively.




其中 $p ( s _ { i , t - 1 } , s _ { i t } )$ 是从状态 $s _ { i , t - 1 }$ 到状态 $s _ { i t } ,$ 的转移概率，$P ( Y _ { i t } | S _ { i t } )$ 是描述状态相关贡献的条件概率。我们分别在接下来的两个小节中详细阐述这两个概率。


## Transition Probabilities of Motivation States




## 动机状态的转移概率


A user can switch among all the possible states in S. The transition matrix $P ( s _ { i , t - 1 } , s _ { i t } )$ below characterizes the probability of such transitions.




用户可以在 S 中的所有可能状态之间进行切换。下面的转移矩阵 $P ( s _ { i , t - 1 } , s _ { i t } )$ 描述了这种转移的概率。


$$
P \big (s _ {i, t - 1}, s _ {i t} \big) = \left[ \begin{array}{c c c c} p (1, 1) & p (1, 2) & \dots & p (1, J) \\ p (2, 1) & p (2, 2) & \dots & p (2, J) \\ \vdots & \vdots & \ddots & \vdots \\ p (J, 1) & p (J, 2) & \dots & p (J, J) \end{array} \right]
$$




$$
P \big (s _ {i, t - 1}, s _ {i t} \big) = \left[ \begin{array}{c c c c} p (1, 1) & p (1, 2) & \dots & p (1, J) \\ p (2, 1) & p (2, 2) & \dots & p (2, J) \\ \vdots & \vdots & \ddots & \vdots \\ p (J, 1) & p (J, 2) & \dots & p (J, J) \end{array} \right]
$$


where p(j, k) is the transition probability from state j to state $k ,$ and $\sum _ { k } p ( j , k ) = 1$ for all $j , k \in S$ . We assume that p(j, k)




其中 p(j, k) 是对于所有 $j , k \in S$ 从状态 j 到状态 $k ,$ 和 $\sum _ { k } p ( j , k ) = 1$ 的转移概率。我们假设 p(j, k)


is influenced by a user’s interactions with the community, which may create certain social or personal norms for the user (Bénabou and Tirole 2006). The user then evaluates his own contributions differently based on the norms. For instance, if all of his past contributions were voted up and appreciated, the user would be more likely to value his own contribution and remain highly motivated. Otherwise, he may switch to a lower motivation state.




受到用户与社区互动的影响，这可能会为用户创建某些社会或个人规范（Bénabou 和 Tirole 2006）。然后，用户根据规范对自己的贡献进行不同的评估。例如，如果他过去的所有贡献都被投票并受到赞赏，那么用户将更有可能重视自己的贡献并保持高度积极性。否则，他可能会转向较低的积极性状态。


We model the transition probabilities with a probit model (Wooldridge 2010). We assume that the states are determined by a latent propensity of transition $L _ { i t } \dot { . }$




我们使用概率模型对转移概率进行建模（Wooldridge 2010）。我们假设状态是由潜在的转移倾向 $L _ { i t } \dot { 决定的。 }$


$$
\begin{array}{l} L _ {i t} = W _ {i, t - 1} ^ {\prime} \xi_ {s _ {i, t - 1}} + u _ {i t}, \\ \left(u _ {i t} | W _ {i, t - 1}, s _ {i, t - 1}\right) \sim N \Big (0, \sigma_ {u} ^ {2} \Big) \end{array}\tag{4}
$$




$$
\begin{array}{l} L _ {i t} = W _ {i, t - 1} ^ {\prime} \xi_ {s _ {i, t - 1}} + u _ {i t}, \\ \left(u _ {i t} | W _ {i, t - 1}, s _ {i, t - 1}\right) \sim N \Big (0, \sigma_ {u} ^ {2} \Big) \end{array}\tag{4}
$$


such that $s _ { i t } = j$ if $L _ { i t } \in \left[ \mu _ { j - 1 } , \mu _ { j } \right)$ , where $W _ { i , t - 1 }$ is a vector of lagged variables related to the user’s previous interactions with the community, $\xi _ { s _ { i , t - 1 } }$ is a vector of the corresponding coefficients, and $u _ { i t }$ is a normal error term from the probit model. In this model, the $\{ \mu _ { i } \} , j = 1 , . . . , J ,$ are threshold values with $\mu _ { 0 }$ normalized to negative infinity, $, \mu _ { 1 }$ to zero, and $\mu _ { J }$ to infinity. The remaining cut-off points are assumed to satisfy $\mu _ { 2 } \le \ldots \le \mu _ { J - 1 }$ so that the cumulative probabilities are nondecreasing (Chib 2001). Note that $\xi _ { s _ { i , t - 1 } }$ is state-specific, capturing different effects of $W _ { i , t - 1 }$ under different states. Then we obtain the transition probability as follows:




使得 $s _ { i t } = j$ if $L _ { i t } \in \left[ \mu _ { j - 1 } , \mu _ { j } \right)$ ，其中 $W _ { i , t - 1 }$ 是与用户之前与社区互动相关的滞后变量向量， $\xi _ { s _ { i , t - 1 } }$ 是相应系数的向量，$u _ { i t }$ 是概率模型中的正态误差项。在此模型中， $\{ \mu _ { i } \} , j = 1 , . 。 。 , J ,$ 是阈值，$\mu _ { 0 }$ 标准化为负无穷大，$, \mu _ { 1 }$ 标准化为零，$\mu _ { J }$ 标准化为无穷大。假设剩余的分界点满足 $\mu _ { 2 } \le \ldots \le \mu _ { J - 1 }$ ，因此累积概率是非递减的（Chib 2001）。请注意， $\xi _ { s _ { i , t - 1 } }$ 是特定于状态的，捕获 $W _ { i , t - 1 }$ 在不同状态下的不同效果。然后我们得到转移概率如下：


$$
\begin{array}{r l} & p (j, k) = P \big (s _ {i t} = k | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = P \big (\mu_ {k - 1} \leq L _ {i t} <   \mu_ {k} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = P \big (L _ {i t} <   \mu_ {k} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) - \\ & \qquad P \big (L _ {i t} <   \mu_ {k - 1} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = \Phi \bigg (\frac {\mu_ {k} - W _ {i , t - 1} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg) - \Phi \bigg (\frac {\mu_ {k - 1} - W _ {i , t - 1} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg) \end{array}\tag{5}
$$




$$
\begin{array}{r l} & p (j, k) = P \big (s _ {i t} = k | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = P \big (\mu_ {k - 1} \leq L _ {i t} < \mu_ {k} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = P \big (L _ {i t} < \mu_ {k} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) - \\ & \qquad P \big (L _ {i t} < \mu_ {k - 1} | s _ {i, t - 1} = j, W _ {i, t - 1} \big) \\ & \quad = \Phi \bigg (\frac {\mu_ {k} - W _ {i , t - 1} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg) - \Phi \bigg (\frac {\mu_ {k - 1} - W _ {i , t - ) 1} ^ {\prime} \xi_ {j}}{\sigma_ {u}} \bigg) \end{array}\tag{5}
$$


where Φ is the standard normal distribution function. When a user first joins the community, we assume that he has an initial probability $p _ { j }$ to be in motivation state j and $\sum _ { j = 1 } ^ { J } p _ { j } = 1 .$




其中 Φ 是标准正态分布函数。当用户第一次加入社区时，我们假设他有一个初始概率 $p _ { j }$ 处于动机状态 j 且 $\sum _ { j = 1 } ^ { J } p _ { j } = 1 。$


## State-Dependent Contributions




## 国家相关贡献


Given the states above, we now derive the conditional probability $( Y _ { i t } | s _ { i t } )$ to describe the state-dependent contributions. Since the observed user contributions are nonnegative, we adopt the standard Tobit model (Wooldridge 2010) following the Bayesian literature (Rossi and Allenby 2003):




考虑到上述状态，我们现在推导条件概率 $( Y _ { i t } | s _ { i t } )$ 来描述与状态相关的贡献。由于观察到的用户贡献是非负的，我们遵循贝叶斯文献（Rossi 和 Allenby 2003）采用标准 Tobit 模型（Wooldridge 2010）：


$$
\begin{array}{c} Y _ {i t} ^ {*} = X _ {i t} ^ {\prime} \beta_ {s _ {i t}} + \varepsilon_ {i t}, \qquad \big (\varepsilon_ {i t} | X _ {i t}, s _ {i t} \big) \sim N \Big (0, \sigma^ {2} \Big) \\ a n d Y _ {i t} = \max \Big (0, Y _ {i t} ^ {*} \Big) \end{array}
$$




$$
\begin{array}{c} Y _ {i t} ^ {*} = X _ {i t} ^ {\prime} \beta_ {s _ {i t}} + \varepsilon_ {i t}, \qquad \big (\varepsilon_ {i t} | X _ {i t}, s _ {i t} \big) \sim N \Big (0, \sigma^ {2} \Big) \\ a n d Y _ {i t} = \max \Big (0, Y _ {i t} ^ {*} \Big) \end{array}
$$


where $Y _ { i t }$ stands for the observed contributions. Then the state-dependent contributions would follow the distribution below. The probability of making no contribution is




其中 $Y _ { i t }$ 代表观察到的贡献。那么依赖于国家的贡献将遵循以下分布。不做出贡献的概率是


$$
\begin{array}{l} P \big (Y _ {i t} = 0 | X _ {i t}, s _ {i t} \big) = \\ P \Big (Y _ {i t} ^ {*} \leq 0 | X _ {i t}, s _ {i t} \Big) = 1 - \Phi \left(\frac {X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right) \end{array}
$$




$$
\begin{array}{l} P \big (Y _ {i t} = 0 | X _ {i t}, s _ {i t} \big) = \\ P \Big (Y _ {i t} ^ {*} \leq 0 | X _ {i t}, s _ {i t} \Big) = 1 - \Phi \left(\frac {X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right) \end{array}
$$


For $Y _ { i t } > 0$ , the probability density function is




对于 $Y _ { i t } > 0$ ，概率密度函数为


$$
f \left(Y _ {i t} \mid X _ {i t}, s _ {i t}\right) = \frac {1}{\sigma} \phi \left(\frac {Y _ {i t} - X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right)
$$




$$
f \left(Y _ {i t} \mid X _ {i t}, s _ {i t}\right) = \frac {1}{\sigma} \phi \left(\frac {Y _ {i t} - X _ {i t} ^ {\prime} \beta_ {s _ {i t}}}{\sigma}\right)
$$


where $\phi$ is the standard normal density function. With the transition probabilities and the state-dependent contributions specified, we now proceed to estimation and identification.




其中 $\phi$ 是标准正态密度函数。指定了转移概率和状态相关贡献后，我们现在进行估计和识别。


## Analysis




＃＃ 分析


## Estimation and Identification




## 估计和识别


We estimate the state-dependent contribution parameters $\beta _ { s _ { i t } }$ in equation (3), and the transition matrix coefficients $\xi _ { s _ { i , t - 1 } }$ in equation (4). Since $s _ { i t } \in S ,$ we essentially estimate the parameter vectors $\beta = ( \beta _ { 2 } , . . . , \beta _ { J } )$ and $\pmb { \xi } = ( \xi _ { 1 } , . . . , \xi _ { J } )$ where β captures the effect of community and individual characteristics on the contributions, and $\xi$ captures the influence of community interactions on the user’s state transition probability. To estimate these key parameters, we also estimate the standard deviations σ and $\sigma _ { u } ,$ as well as the state process $\widetilde { \pmb { S } } = \big \{ s _ { i t } \big \} , t = 1 , . . . , T ; i = 1 , . . . , N _ { t }$ . For ease of reference, we write the parameter space as $\pmb { \theta } = \{ \pmb { \beta } , \pmb { \xi } , \sigma , \sigma _ { u } \}$ and $\widetilde { s }$ Note that β and $\xi$ are state-dependent, while σ and $\sigma _ { u }$ are not.




我们估计方程（3）中的状态相关贡献参数$\beta _ { s _ { i t } }$，以及方程（4）中的转移矩阵系数$\xi _ { s _ { i , t - 1 } }$。由于 $s _ { i t } \in S ，$ 我们实质上估计了参数向量 $\beta = ( \beta _ { 2 } , . . . , \beta _ { J } )$ 和 $\pmb { \xi } = ( \xi _ { 1 } , ... , \xi _ { J } )$，其中 β 捕获了社区和个人特征对贡献的影响，并且$\xi$ 捕捉社区互动对用户状态转换概率的影响。为了估计这些关键参数，我们还估计标准差 σ 和 $\sigma _ { u } ,$ 以及状态过程 $\widetilde { \pmb { S } } = \big \{ s _ { i t } \big \} , t = 1 , 。 。 。 , T ;我 = 1 , . 。 。 ，N_{t}$。为了便于参考，我们将参数空间写为 $\pmb { \theta } = \{ \pmb { \beta } 、 \pmb { \xi } 、 \sigma 、 \sigma _ { u } \}$ 和 $\widetilde { s }$ 请注意，β 和 $\xi$ 是状态相关的，而 σ 和 $\sigma _ { u }$ 则不是。


We estimate our HMM using a Bayesian procedure developed by Kim and Nelson (1999). The Bayesian estimation algorithm treats θ and $\widetilde { s }$ as random variables with prior distributions. The algorithm then updates their joint distributions $\pi \big ( \theta , \widetilde { \boldsymbol { S } } | \boldsymbol { Y } , \boldsymbol { X } , \boldsymbol { W } \big )$ using Gibbs sampling (Albert and Chib 1993). This updates the posterior distribution by incorporating the observed information from data.




我们使用 Kim 和 Nelson (1999) 开发的贝叶斯程序来估计 HMM。贝叶斯估计算法将 θ 和 $\widetilde { s }$ 视为具有先验分布的随机变量。然后，该算法使用吉布斯采样更新它们的联合分布 $\pi \big ( \theta , \widetilde { \boldsymbol { S } } | \boldsymbol { Y } , \boldsymbol { X } , \boldsymbol { W } \big )$ (Albert and Chib 1993)。这通过合并从数据中观察到的信息来更新后验分布。


Bayesian estimations of HMM models may encounter the “label switching” problem (Jasra et al. 2005), which means our posterior distribution of θ and $\widetilde { s }$ may be invariant if we switch the labels. Since the motivation states in our context have self-evident economic interpretation, we adopt a normalization requirement that the constant terms in $\beta _ { j } \in \pmb { \beta }$ are ordered. Denote the constant term in $\beta _ { j }$ as $c _ { j } ^ { x } .$ We permutate $\beta$ according to $c _ { j } ^ { x }$ such that $c _ { 1 } ^ { x } \leq \ldots \leq c _ { J } ^ { x }$ in each draw of our Gibbs samplers. This requirement means that without any stimulus, a user in a high motivation state on average contributes more than if he were in a lower motivation state. This technique helps us identify the states in our model.




HMM 模型的贝叶斯估计可能会遇到“标签切换”问题（Jasra et al. 2005），这意味着如果我们切换标签，我们的 θ 和 $\widetilde { s }$ 的后验分布可能是不变的。由于我们上下文中的动机状态具有不言而喻的经济解释，因此我们采用标准化要求，即 $\beta _ { j } \in \pmb { \beta }$ 中的常数项是有序的。将 $\beta _ { j }$ 中的常数项表示为 $c _ { j } ^ { x } .$ 我们根据 $c _ { j } ^ { x }$ 排列 $\beta$，使得在吉布斯采样器的每次抽取中 $c _ { 1 } ^ { x } \leq \ldots \leq c _ { J } ^ { x }$ 。这一要求意味着，在没有任何刺激的情况下，处于高动机状态的用户平均比处于较低动机状态时贡献更多。这项技术可以帮助我们识别模型中的状态。


## Samples and Variables




## 样本和变量


To test our structural model, we construct a user-date panel of the 2,147 users in 964 days from SuperUser. We exclude the first 100 days (with substantial fluctuation), and analyze the steady-state periods afterwards.<sup>5</sup> Because of the computational burden (over 2 million data points), we divide the sample into subsamples that each contains 200 days. Our estimation focuses on the subsample in 101–300 days with 1,215 unique users, and 210,890 user-date observations. Table 1 presents the definitions of our variables and summary statistics. We use other subsamples for robustness checks.




为了测试我们的结构模型，我们构建了 SuperUser 964 天内 2,147 个用户的用户日期面板。我们排除前 100 天（波动较大），然后分析之后的稳态期。<sup>5</sup>由于计算负担（超过 200 万个数据点），我们将样本分为子样本，每个子样本包含 200 天。我们的估计重点是 101-300 天内的子样本，其中包含 1,215 个唯一用户和 210,890 个用户日期观察值。表 1 列出了变量的定义和汇总统计数据。我们使用其他子样本进行稳健性检查。


Our dependent variable is $A n s w e r s _ { i t } ,$ which is the number of answers provided by user i at time t. We choose this dependent variable because among various ways to participate in the community, providing answers may be the most crucial because of the knowledge-sharing nature of the site. It is also the most challenging activity as it takes time and effort and requires certain domain expertise.




我们的因变量是 $A n s w e r s _ { i t } ，$ 是用户 i 在时间 t 提供的答案数量。我们选择这个因变量是因为在参与社区的各种方式中，由于网站的知识共享性质，提供答案可能是最重要的。这也是最具挑战性的活动，因为它需要时间和精力，并且需要一定的领域专业知识。


We categorize two sets of explanatory variables that may affect users’ transition probabilities (W) and conditional contributions (X), respectively. The variables in vector W contain individual and community characteristics enabled by ITartifacts that could have an enduring effect on a user’s motivation state. First, if a user’s questions are answered by others, he may be more likely to return to the site and may have higher chance to contribute. Moreover, he may be more likely to answer others’ questions out of reciprocity. We use the number of answers a user receives on his past questions $( A n s w e r s \_ r e c e i \nu e d _ { i , t - l } )$ to capture such reciprocity. Second, peer recognition can play a role in state transitions. When more answers provided by a user are voted up or accepted as the best answer, one may value his contribution higher because the contribution is appreciated by the community. This may transfer the user to a high motivation state so that he contributes even more. We measure these effects by the number of up-votes that a user receives on his previous answers (Upvotes $\underline { { a n s w e r } } _ { i , t - l } )$ as well as the number of accepted answers of a user (Accepted $\underline { { a n s w e r s } } _ { i , t - l } )$ . Third, self-image related motivation may also influence a user. To award users for their contributions, SuperUser grants users various badges, which serve as a signalling mechanism for a user’s selfimage. To examine the effect of the badge system, we include $B a d g e s _ { i , t - l }$ as another explanatory variable, which represents the incremental number of badges earned by user i for his answers at time $t \mathrm { - } I .$




我们对两组可能影响用户转移概率（W）和条件贡献（X）的解释变量进行分类。向量 W 中的变量包含 ITartifacts 启用的个人和社区特征，这些特征可能对用户的动机状态产生持久影响。首先，如果用户的问题得到其他人的回答，他可能更有可能返回该网站，并且可能有更高的机会做出贡献。此外，他可能更有可能出于互惠而回答别人的问题。我们使用用户在过去的问题上收到的答案数量 $( An s w e r s \_ r e c e i \nu e d _ { i , t - l } )$ 来捕获这种互惠性。其次，同行认可可以在状态转变中发挥作用。当用户提供的更多答案被投票或接受为最佳答案时，人们可能会更高地评价他的贡献，因为该贡献受到社区的赞赏。这可能会将用户转移到高度积极的状态，以便他做出更多贡献。我们通过用户对其之前的答案收到的赞成票数 (Upvotes $\underline { { an s w e r } } _ { i , t - l } )$ 以及用户接受的答案数 (Accepted $\underline { { an s w e r s } } _ { i , t - l } )$ 来衡量这些影响。第三，自我形象相关的动机也可能影响用户。为了奖励用户的贡献，超级用户授予用户各种徽章，作为用户自我形象的信号机制。为了检查徽章系统的效果，我们将 $B a d g e s _ { i , t - l }$ 作为另一个解释变量，它表示用户 i 在 $t \mathrm { - } I .$ 时刻的回答所获得的徽章增量数量。


The variables in vector X contain individual and community characteristics that may have a direct effect on a user’s valuation of his contribution. First, the types of questions are diverse in the community and user expertise is different; whether a user can contribute his knowledge depends on whether a question is within his domain.<sup>6</sup> StackExchange uses tags (i.e., certain words or phrases) to identify the topics of each question and the expertise of each user. By sorting questions and users into specific, well-defined categories, tags are a means of matching experts with questions that they are able to answer. We calculate Matched $t a g s _ { i t }$ as the number of identical tags matched between the questions and the user i at time t. Matched $\_ t a g s _ { i t }$ captures not only the demand for knowledge on the site, but also the feasible supply of knowledge specific to the user’s expertise.




向量 X 中的变量包含个人和社区特征，可能会直接影响用户对其贡献的评估。首先，社区的问题类型多样，用户专业知识不同；用户能否贡献自己的知识取决于问题是否属于其领域。<sup>6</sup>StackExchange 使用标签（即某些单词或短语）来识别每个问题的主题以及每个用户的专业知识。通过将问题和用户分类为特定的、定义明确的类别，标签是一种将专家与他们能够回答的问题进行匹配的方法。我们计算 Matched $t a g s _ { i t }$ 作为在时间 t 时问题和用户 i 之间匹配的相同标签的数量。匹配的$\_ t a g s _ { i t }$不仅捕获了站点上对知识的需求，还捕获了针对用户专业知识的可行知识供应。


Second, the tenure of membership can affect a user’s contribution. As Figure 3(a) shows, users contribute less when they stay longer on the site. We use the days since user i registered $( T e n u r e _ { i t } )$ to account for this declining tendency of contributions over time. Third, we also include the total number of answers that have been provided by the user $( T o t a l \_ a n s w e r s _ { i , t - l } )$ The rationale is that if a user has provided more answers in the past, he may also be more inclined to provide new answers in the current period. Fourth, we proxy the community size by Group\_size<sub>t</sub>, the number of users who participate in any activities at time t. Classic public goods models show that the average level of contribution decreases with group size, while in impure altruism models, the private benefits can increase with group size, as the enjoyment of contributing is enhanced by the number of recipients. We call this the social effect. As a group becomes larger, the motivation of pure altruism can decrease, while the social effect can increase. Given the importance of group size, we include it as a contextual factor in our analysis.




其次，会员的任期会影响用户的贡献。如图 3(a) 所示，用户在网站上停留时间越长，贡献就越少。我们使用自用户注册 $(Tenure_{it})$ 以来的天数来解释贡献随时间的下降趋势。第三，我们还包括用户提供的答案总数$(Total\_answers_{i,t-l})$，理由是如果用户过去提供了更多答案，那么他也可能更倾向于在当前时期提供新答案。第四，我们用 Group\_size<sub>t</sub> 来代理社区规模，即在时间 t 参与任何活动的用户数量。经典的公共物品模型表明，平均贡献水平随着群体规模的扩大而降低，而在不纯粹利他主义模型中，私人收益会随着群体规模的扩大而增加，因为接受者数量增加了贡献的乐趣。我们称之为社会效应。随着群体规模的扩大，纯粹利他主义的动机会减少，而社会效应会增加。鉴于群体规模的重要性，我们将其作为背景因素纳入我们的分析中。


## Model Selection




## 型号选择


In our model specification, the number of states was not defined a priori. It instead needs to be estimated with the data.




在我们的模型规范中，状态的数量没有预先定义。相反，需要用数据来估计。


<table><tr><td colspan="6">Table 1. Variables and Descriptive Statistics</td></tr><tr><td>Variable</td><td>Description</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Dependent Variable (Yit)</td></tr><tr><td>Answersit</td><td>Number of answers</td><td>0.118</td><td>0.657</td><td>0</td><td>23</td></tr><tr><td colspan="6">Community and Individual Characteristics (Xit)</td></tr><tr><td>Matched_tags</td><td>Number of tags matched between questions and the user&#x27;s profile</td><td>27.061</td><td>23.894</td><td>0</td><td>225</td></tr><tr><td>Tenureit</td><td>Number of days since the user registered</td><td>153.537</td><td>73.142</td><td>0</td><td>299</td></tr><tr><td>Total_answersi,t-1</td><td>Total number of past answers by the user</td><td>31.405</td><td>88.596</td><td>0</td><td>2018</td></tr><tr><td>Group_sizet</td><td>Number of participating users</td><td>112.400</td><td>21.659</td><td>54</td><td>158</td></tr><tr><td colspan="6">Community Interactions (Wi,t-1)</td></tr><tr><td>Answers_receivedi,t-1</td><td>Number of answers to past questions received by the user</td><td>0.039</td><td>0.318</td><td>0</td><td>19</td></tr><tr><td>Upvotes_answeri,t-1</td><td>Number of up-votes to past answers of the user</td><td>0.177</td><td>1.006</td><td>0</td><td>37</td></tr><tr><td>Accepted_answersi,t-1</td><td>Number of accepted answers of the user</td><td>0.032</td><td>0.29</td><td>0</td><td>10</td></tr><tr><td>Badgesi,t-1</td><td>Number of badges earned by the user</td><td>0.022</td><td>0.177</td><td>0</td><td>10</td></tr></table>




<table><tr><td colspan="6">表 1. 变量和描述性统计</td></tr><tr><td>变量</td><td>描述</td><td>平均值</td><td>S.D.</td><td>最小值</td><td>最大值</td></tr><tr><td colspan="6">因变量（Yit）</td></tr><tr><td>回答</td><td>回答数</td><td>0.118</td><td>0.657</td><td>0</td><td>23</td></tr><tr><td colspan="6">社区和个人特征(Xit)</td></tr><tr><td>Matched_tags</td><td>问题与用户之间匹配的标签数量个人资料</td><td>27.061</td><td>23.894</td><td>0</td><td>225</td></tr><tr><td>Tenureit</td><td>自用户以来的天数已注册</td><td>153.537</td><td>73.142</td><td>0</td><td>299</td></tr><tr><td>Total_answersi,t-1</td><td>过去回答的总数用户</td><td>31.405</td><td>88.596</td><td>0</td><td>2018</td></tr><tr><td>Group_sizet</td><td>参与人数用户</td><td>112.400</td><td>21.659</td><td>54</td><td>158</td></tr><tr><td colspan="6">社区互动（Wi,t-1）</td></tr><tr><td>Answers_receivedi,t-1</td><td>数量用户过去收到的问题的回答</td><td>0.039</td><td>0.318</td><td>0</td><td>19</td></tr><tr><td>Upvotes_answeri,t-1</td><td>对过去的答案的赞成票数user</td><td>0.177</td><td>1.006</td><td>0</td><td>37</td></tr><tr><td>Accepted_answersi,t-1</td><td>接受的答案数用户</td><td>0.032</td><td>0.29</td><td>0</td><td>10</td></tr><tr><td>Badgesi,t-1</td><td>获得的徽章数量用户</td><td>0.022</td><td>0.177</td><td>0</td><td>10</td></tr></table>


<table><tr><td>Number of States</td><td>- 2*Log-likelihood</td><td>AIC</td><td>BIC</td><td>MSC</td><td>Number of Variables</td></tr><tr><td>1</td><td>135,246.5</td><td>135,270.5</td><td>135,331.7</td><td>—</td><td>12</td></tr><tr><td>2</td><td>134,065.9</td><td>134,111.9</td><td>134,229.3</td><td>345,144.4</td><td>23</td></tr><tr><td>3</td><td>119,391.6</td><td>119,461.6</td><td>119,640.1</td><td>330,957.1</td><td>35</td></tr><tr><td>4</td><td>120,577.6</td><td>120,671.6</td><td>120,911.4</td><td>333,159.2</td><td>47</td></tr></table>




<table><tr><td>状态数量</td><td>- 2*对数似然</td><td>AIC</td><td>BIC</td><td>MSC</td><td>数量变量</td></tr><tr><td>1</td><td>135,246.5</td><td>135,270.5</td><td>135,331.7</td><td>—</td><td>12</t d></tr><tr><td>2</td><td>134,065.9</td><td>134,111.9</td><td>134,229.3</td><td>345,144.4</td><td>23</td></t r><tr><td>3</td><td>119,391.6</td><td>119,461.6</td><td>119,640.1</td><td>330,957.1</td><td>35</td></tr><tr ><td>4</td><td>120,577.6</td><td>120,671.6</td><td>120,911.4</td><td>333,159.2</td><td>47</td></tr></table>


To estimate the number of states, we adopt several model selection criteria from the literature. Our selection criteria include the log-likelihood, the commonly used Akaike information criterion (AIC) and Bayesian information criterion (BIC) (Singh et al. 2011; Yan and Tan 2014), and the Markov switching criterion (MSC) which is specially designed for Markov switching models (Netzer et al. 2008).<sup>7</sup> Given a set of candidate models for the data, the preferred model is the one with the minimum value of the selection criteria.




为了估计状态的数量，我们采用了文献中的几个模型选择标准。我们的选择标准包括对数似然、常用的 Akaike 信息准则 (AIC) 和贝叶斯信息准则 (BIC)（Singh et al. 2011；Yan and Tan 2014），以及专为马尔可夫切换模型设计的马尔可夫切换准则 (MSC)（Netzer et al. 2008）。<sup>7</sup>给定一组数据候选模型，首选模型是具有最小值的模型选择标准。


We estimate models of different states, and report the results in Table 2. Our benchmark is the one-state static model, which assumes that a user stays in the same motivation state throughout, and thus his contribution behavior does not change over time.<sup>8</sup> As Columns 2–5 show, whereas the static model has the largest value, the three-state HMM has the smallest value in each selection criterion. Hence, all selection criteria suggest that HMM models with more than one state are superior to the static model, and particularly the threestate HMM is the best-fitting model that outperforms other models. Therefore, we report estimation results of the threestate HMM hereafter.




我们估计不同状态的模型，并在表 2 中报告结果。我们的基准是单状态静态模型，它假设用户始终处于相同的动机状态，因此他的贡献行为不会随时间变化。<sup>8</sup>如第 2-5 列所示，静态模型具有最大值，而三态 HMM 在每个选择标准中具有最小值。因此，所有选择标准都表明具有不止一种状态的 HMM 模型优于静态模型，特别是三态 HMM 是优于其他模型的最佳拟合模型。因此，我们在下文中报告三态 HMM 的估计结果。


## Estimation Results




## 估算结果


Table 3 reports the estimated parameters of the three-state HMM based on Bayesian estimation. For ease of discussion, we refer the three motivation states as low, medium, and high, denoted as L, M, and H, respectively. The coefficients in vectors β and ξ vary across states (the three columns), indicating that a change in states would lead to a change in contribution. The initial probabilities of being in L, M, and H states are 0.755, 0.216 and 0.029, respectively (bottom row). Hence, a new user tends to be in L state much more likely than in higher states. This confirms the importance of studying how to energize and motivate community members.




表 3 报告了基于贝叶斯估计的三态 HMM 的估计参数。为了便于讨论，我们将三种动机状态称为低、中、高，分别表示为L、M和H。向量 β 和 xi 中的系数因状态（三列）而异，表明状态的变化将导致贡献的变化。处于 L、M 和 H 状态的初始概率分别为 0.755、0.216 和 0.029（底行）。因此，新用户处于 L 状态的可能性比处于更高状态的可能性要大得多。这证实了研究如何激励和激励社区成员的重要性。


<table><tr><td colspan="4">Table 3. Results of HMM Bayesian Estimation</td></tr><tr><td>Variable Name</td><td>State L(Low Motivation)</td><td>State M(Medium Motivation)</td><td>State H(High Motivation)</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^x$ </td><td>-3.053*** (0.064)</td><td>0.316*** (0.086)</td><td>7.072*** (0.312)</td></tr><tr><td>Matched_tags $_{it}$ </td><td>0.015*** (0.000)</td><td>0.022*** (0.001)</td><td>0.029*** (0.001)</td></tr><tr><td>Tenure $_{it}$ </td><td>-0.0004 (0.0003)</td><td>-0.006*** (0.003)</td><td>-0.016*** (0.001)</td></tr><tr><td>Total_answers $_{i,t-1}$ </td><td>0.001*** (0.000)</td><td>0.002*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td>Group_size $_t$ </td><td>0.003*** (0.000)</td><td>0.002*** (0.000)</td><td>-0.010*** (0.002)</td></tr><tr><td></td><td colspan="3">1.011*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ξ - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^w$ </td><td>-1.651*** (0.024)</td><td>-0.578*** (0.029)</td><td>1.118*** (0.135)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.217*** (0.019)</td><td>0.021 (0.023)</td><td>0.013 (0.051)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.231*** (0.016)</td><td>0.109*** (0.013)</td><td>0.031 (0.028)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.594*** (0.036)</td><td>0.235*** (0.023)</td><td>0.081*** (0.030)</td></tr><tr><td>Badges $_{i,t-1}$ </td><td>0.400*** (0.037)</td><td>0.201*** (0.036)</td><td>-0.030 (0.058)</td></tr><tr><td>Initial Probability</td><td>0.755*** (0.015)</td><td>0.216*** (0.014)</td><td>0.029*** (0.005)</td></tr></table>




<table><tr><td colspan="4">表3. HMM贝叶斯估计结果</td></tr><tr><td>变量名称</td><td>状态L（低动机）</td><td>状态M（中动机）</td><td>状态H（高动机）</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - 后验平均值（标准差）</td></tr><tr><td> $c^x$ </td><td>-3.053*** (0.064)</td><td>0.316*** (0.086)</td><td>7.072*** (0.312)</td></tr><tr><td>匹配_标签 $_{it}$ </td><td>0.015*** (0.000)</td><td>0.022*** (0.001)</td><td>0.029*** (0.001)</td></tr><tr><td>任期$_{it}$ </td><td>-0.0004 (0.0003)</td><td>-0.006*** (0.003)</td><td>-0.016*** (0.001)</td></tr><tr><td>总答案数 $_{i,t-1}$ </td><td>0.001*** (0.000)</td><td>0.002*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td>Group_size $_t$ </td><td>0.003*** (0.000)</td><td>0.002*** (0.000)</td><td>-0.010*** (0.002)</td></tr><tr><td></td><td colspan="3">1.011*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ψ - 后验均值（标准）偏差）</td></tr><tr><td> $c^w$ </td><td>-1.651*** (0.024)</td><td>-0.578*** (0.029)</td><td>1.118*** (0.135)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.217*** (0.019)</td><td>0.021 (0.023)</td><td>0.013 (0.051)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.231*** (0.016)</td><td>0.109*** (0.013)</td><td>0.031 (0.028)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.594*** (0.036)</td><td>0.235*** (0.023)</td><td>0.081*** (0.030)</td></tr><tr><td>徽章 $_{i,t-1}$ </td><td>0.400*** (0.037)</td><td>0.201*** (0.036)</td><td>-0.030 (0.058)</td></tr><tr><td>初始概率</td><td>0.755*** (0.015)</td><td>0.216*** (0.014)</td><td>0.029*** (0.005)</td></tr></table>


\* p < 0.1, \*\* p < 0.05; \*\*\* p < 0.01. For brevity, we use “significant” and “insignificant” in the results discussion.




\* p < 0.1，\*\* p < 0.05； \*\*\* p < 0.01。为简洁起见，我们在结果讨论中使用“显着”和“不显着”。


## State-Dependent Contributions (β)




## 国家相关贡献 (β)


We first examine the state-dependent contributions (top panel in Table 3). The interpretation of the three states is determined by the state-specific intrinsic propensity to contribute (the constant vector c<sup>x</sup>), as discussed in the “Estimation and Identification” section. The estimates are -3.053, 0.316, and 7.072 for states L, M, and H, respectively (all significant at 1% level). The relative large distances between states indicate that the states are well identified.




我们首先检查依赖于国家的贡献（表 3 中的顶部面板）。三种状态的解释由特定于状态的内在贡献倾向（常数向量 c<sup>x</sup>）决定，如“估计和识别”部分中所述。 L、M 和 H 州的估计值分别为 -3.053、0.316 和 7.072（均在 1% 水平上显着）。状态之间相对较大的距离表明状态被很好地识别。


The coefficients of Matched\_tags are 0.015, 0.022, and 0.029 for states L, M, and H, respectively (all significant at 1% level). The positive coefficients suggest that all users tend to supply more knowledge when the need arises and matches their expertise. Also, the increasing magnitude of the coefficients shows that as users move from L to M to H, they become more responsive to the demand for knowledge.




对于状态 L、M 和 H，Matched\_tags 的系数分别为 0.015、0.022 和 0.029（均在 1% 水平上显着）。正系数表明所有用户都倾向于在需要时提供更多与他们的专业知识相匹配的知识。此外，系数的增加表明，随着用户从 L 移动到 M 再到 H，他们对知识的需求变得更加敏感。


For other individual characteristics, we find a negative relationship between Tenure length and user contributions. The negative coefficients in state M (-0.006, significant at 1% level) and state H (-0.016, significant at 1% level) suggest that users involved for a longer time tend to contribute less. It is possible that, all else being equal, the longer a user has been associated with the community, the more inertia (or lower incentives) he has in terms of contribution. Such a stalling effect poses another challenge to online communities.




对于其他个人特征，我们发现任期长度和用户贡献之间存在负相关关系。状态 M（-0.006，在 1% 水平上显着）和状态 H（-0.016，在 1% 水平上显着）的负系数表明，参与时间较长的用户往往贡献较少。在其他条件相同的情况下，用户与社区关联的时间越长，他在贡献方面的惯性就越大（或激励越低）。这种停滞效应给在线社区带来了另一个挑战。


We also confirm that the answers a user contributed in the past have a positive relationship with how much he would contribute in the future. The highly significant coefficients of Total\_answers for state L (0.001), M (0.002), and H (0.003) show that the effect of this variable increases as users moves from state L up to state H.




我们还确认，用户过去贡献的答案与他未来贡献的数量呈正相关。状态 L (0.001)、M (0.002) 和 H (0.003) 的 Total\_answers 的高度显着系数表明，随着用户从状态 L 移动到状态 H，该变量的影响会增加。


Regarding Group\_size, the coefficients are positive and significant in L (0.003) and M states (0.002). A user may contribute more when the community is larger, which confirms the “social effect” discussed before. Yet, this effect decreases as a user transitions from state L to M. As the user moves further up to state $H ,$ the community size is no longer a positive factor (-0.01, significant at 1%). This suggests that users in states L and M may put higher valuation on a larger community, while users in state H may be more susceptible to the free-riding problem.




关于组大小，L (0.003) 和 M 状态 (0.002) 中的系数为正且显着。当社区越大时，用户可能会贡献更多，这证实了之前讨论的“社交效应”。然而，随着用户从状态 L 转换到 M，这种影响会减弱。随着用户进一步移动到状态 $H ，$ 社区规模不再是一个积极因素（-0.01，在 1% 时显着）。这表明L和M状态的用户可能会对更大的社区给予更高的评价，而H状态的用户可能更容易受到搭便车问题的影响。


## State Transition Probabilities (ξ)




## 状态转移概率 (xi)


We now turn to the effects of different motivating mechanisms on state transition probabilities (bottom panel in Table 3). The constant term $c ^ { w }$ is negative: -1.651 and -0.578 for states L and M, respectively (both significant at 1% level). This indicates that in the absence of motivating mechanisms, users in states L and M are likely to stay or transition to lower states. This once again reinforces the importance to have motivating mechanisms in place, or else the community will decline.




我们现在转向不同激励机制对状态转换概率的影响（表 3 中的底部面板）。常数项 $c ^ { w }$ 为负：状态 L 和 M 分别为 -1.651 和 -0.578（均在 1% 水平上显着）。这表明在缺乏激励机制的情况下，处于L和M状态的用户很可能会停留或过渡到较低的状态。这再次强调了建立激励机制的重要性，否则社区将会衰落。


Also, the more negative coefficient for users in state L suggests that they are more likely to be in L compared with users in M. In contrast, the constant term c<sup>w</sup> becomes positive in state H (1.118, significant at 1% level). Users in H state tend to remain highly motivated.




此外，处于 L 状态的用户的负系数表明，与处于 M 状态的用户相比，他们更有可能处于 L 状态。相反，常数项 c<sup>w</sup> 在状态 H 中变为正值（1.118，在 1% 水平下显着）。处于 H 状态的用户往往保持高度积极性。


Overall, users in all three states seem to benefit from the motivating mechanisms through their interaction with the community. However, different mechanisms have different impacts on the motivation conditional on a user’s current state. When comparing the coefficients corresponding to each motivating mechanism across the three states, we can see that the mechanisms are the most effective among the low-state users. This is also precisely the user state that needs to be activated by the online community. Such finer-grained results were not revealed in the prior literature.




总体而言，这三个州的用户似乎都通过与社区的互动从激励机制中受益。然而，不同的机制对用户当前状态的动机有不同的影响。当比较三种状态下每种激励机制对应的系数时，我们可以看到这些机制在低状态用户中是最有效的。这也正是网络社区需要激活的用户状态。先前的文献中并未揭示这种更细粒度的结果。


Specifically, reciprocity seems to be effective only for the least motived users. For users in state L, receiving more answers on their previous questions tends to help transfer them into higher states (0.217, significant at 1% level). The coefficient becomes insignificant in states M and H. Users in M and H state tend to contribute anyway, less because they want to return the favor of their peers. Hence, reciprocity can be more useful to stimulate low-state users.




具体来说，互惠似乎只对最不积极的用户有效。对于处于 L 状态的用户，收到更多关于之前问题的答案往往有助于将他们转移到更高的状态（0.217，在 1% 水平上显着）。该系数在状态 M 和 H 中变得微不足道。处于 M 和 H 状态的用户无论如何都倾向于做出贡献，但贡献较少，因为他们想回报同伴的青睐。因此，互惠对于刺激低状态用户可能更有用。


For peer-recognition, the coefficients on Upvotes\_answerand Accepted\_answers are all positive and mostly significant (rows 3–4 in the bottom panel). We interpret this result as the verification of one’s identity. When a user receives more upvotes or has more answers accepted, he may feel the value of his contribution being recognized and thus his identity in the community validated. Further, this identity-verification effect is more prominent in lower states, and declines as a user moves to H. For instance, Accepted\_answers motivates users in state L (0.594, significant at 1%) the most, followed by state M (0.235, significant at 1%), and then state H (0.081, significant at 1%). This indicates that the marginal effect of accepted answer diminishes as a user moves to higher motivation states. The pattern is similar for Upvotes\_answer. Together, these results highlight the effectiveness of peer recognition as a motivating scheme to enhance self-identity, especially for users in low state.




对于同行认可，Upvotes\_answer 和 Accepted\_answers 的系数均为正值且大多显着（底部面板中的第 3-4 行）。我们将此结果解释为身份验证。当用户收到更多的点赞或接受更多的答案时，他可能会觉得他的贡献的价值得到认可，从而验证了他在社区中的身份。此外，这种身份验证效应在较低的州中更为突出，并且随着用户转向 H 而下降。例如，Accepted\_answers 对处于 L 状态的用户的激励最大（0.594，显着性为 1%），其次是状态 M（0.235，显着性为 1%），然后是状态 H（0.081，显着性为 1%）。这表明，随着用户转向更高的动机状态，接受的答案的边际效应会减弱。 Upvotes\_answer 的模式类似。总之，这些结果凸显了同伴认可作为增强自我认同的激励方案的有效性，特别是对于处于低状态的用户。


Likewise, we find the effectiveness of badges to strengthen self-image motivation. Earning more badges seems to lift a user from states L and M to state H (coefficients are 0.400 and 0.201, significant at 1% level). The effect of badges becomes insignificant for users in H. This seems to suggest that highly motivated users are insensitive to badges; earning badges may not help them verify their self-identity. This may be due to the “moral licensing” effect of prosocial behavior. If so, using badge system to motivate user contributions should be gauged carefully, despite the fact that badges are widely used in many online communities. To retain users in H state, community managers need to design more effective mechanisms. This could be an interesting area for future research.




同样，我们发现徽章可以有效增强自我形象动机。获得更多徽章似乎可以将用户从状态 L 和 M 提升到状态 H（系数为 0.400 和 0.201，在 1% 的水平上显着）。徽章的影响对于 H 中的用户来说变得微不足道。这似乎表明积极性高的用户对徽章不敏感；获得徽章可能无法帮助他们验证自己的身份。这可能是由于亲社会行为的“道德许可”效应。如果是这样，则应仔细衡量使用徽章系统来激励用户贡献，尽管徽章在许多在线社区中得到了广泛使用。为了留住H状态的用户，社区管理者需要设计更有效的机制。这可能是未来研究的一个有趣领域。


## Transition Matrices and Marginal Effects




## 转移矩阵和边际效应


We substitute the estimates from Table 3 into equation (5) to calculate the transition probabilities among states. Transition matrix (a) in Table 4 presents the transition probabilities evaluated at the mean level of community interactions (from column “Mean” in Table 1). The transition probabilities are substantially different when a user is in L, M, or H states. This confirms that modeling the stochastic process with the three hidden states is reasonable. Further, the matrix indicates the stickiness of state L. Once a user is in this state, he is most likely to be trapped, and even if a user starts off in state H, he also tends to slip down to M and then to L. This implies the challenge of inherent deteriorating participation as we posed earlier, and the importance of stimulating users to become more motivated.




我们将表 3 中的估计值代入方程（5）来计算状态之间的转移概率。表 4 中的转移矩阵 (a) 呈现了在社区互动的平均水平上评估的转移概率（来自表 1 中的“平均值”列）。当用户处于 L、M 或 H 状态时，转移概率有很大不同。这证实了用三个隐藏状态对随机过程进行建模是合理的。此外，该矩阵表示状态L的粘性。用户一旦处于该状态，他最有可能被困住，即使用户从状态H开始，他也倾向于滑落到M，然后滑落到L。这意味着我们之前提出的固有参与度恶化的挑战，以及刺激用户变得更有动力的重要性。


To quantify the marginal effect of each motivating mechanism on transition probability, we calculate the transition probabilities when the mean value of a variable increases by one unit, while holding other variables constant. The matrices (b)–(d) in Table 4 show the transition probabilities caused by such a change in up-votes, accepts and badges, respectively. We focus on up-votes, accepts and badges, because they are the mechanisms that platform designers could manage. For example, if the community decreases the cost of up-votes or even enhances the incentives of up-votes, the number of upvotes is likely to increase. If the platform designer changes the setup such that each question could accept multiple answers, then the mean of accepted answers is likely to increase. Further, because online communities provide various kinds of badges to users, a more careful design of the badge system may help elevate the user contributions.




为了量化每种激励机制对转移概率的边际效应，我们计算变量平均值增加一个单位时的转移概率，同时保持其他变量不变。表 4 中的矩阵 (b)-(d) 分别显示了由赞成票、接受票和徽章的这种变化引起的转移概率。我们专注于投票、接受和徽章，因为它们是平台设计者可以管理的机制。例如，如果社区降低点赞成本，甚至增强点赞激励，点赞数量就有可能增加。如果平台设计者更改设置，使每个问题可以接受多个答案，那么接受答案的平均值可能会增加。此外，由于在线社区为用户提供各种徽章，因此更仔细地设计徽章系统可能有助于提高用户贡献。


We can then take the difference between respective cells of (a) and (b)–(d) to calculate the marginal effect on transition probability. For example, in matrix (b), receiving one additional up-vote on average hypothetically increases the probability of transitioning from state L to state M by 3.1% (from 5.8% to 8.9%), while a user in state M would increase his likelihood of staying in the state from 28.8% to 32.5%, and that of switching to state H from 0.4% to 0.6%. Similarly, in matrix (c), one additional accepted answer could increase the transition probability from state L to state M by 10.5% (from 5.8% to 16.3%), and increase the probability of staying in state M by 8.1% (from 28.8% to 36.9%). It also increases the transition probability to state H by 0.1%, 0.4% and 2.1% for users in state L, M, and H, respectively. Such changes are nontrivial because the low motivation state tends to be sticky.




然后，我们可以利用 (a) 和 (b)–(d) 各自单元格之间的差异来计算转移概率的边际效应。例如，在矩阵 (b) 中，假设平均获得 1 个额外的赞成票，从状态 L 转换到状态 M 的概率会增加 3.1%（从 5.8% 到 8.9%），而处于状态 M 的用户会将其留在该状态的可能性从 28.8% 增加到 32.5%，切换到状态 H 的可能性从 0.4% 增加到 0.6%。类似地，在矩阵（c）中，一个额外的可接受的答案可以将从状态 L 到状态 M 的转移概率增加 10.5%（从 5.8% 到 16.3%），并将停留在状态 M 的概率增加 8.1%（从 28.8% 到 36.9%）。对于处于状态 L、M 和 H 的用户，它还分别将状态 H 的转换概率增加了 0.1%、0.4% 和 2.1%。这种变化是不平凡的，因为低动机状态往往是粘性的。


<table><tr><td colspan="7">Table 4. Mean Posterior Transition Matrices</td></tr><tr><td></td><td colspan="3">(a) Mean Interactions</td><td colspan="3">(b) Up-votes</td></tr><tr><td>t-1 to t</td><td>L</td><td>M</td><td>H</td><td>L</td><td>M</td><td>H</td></tr><tr><td>L</td><td>94.2</td><td>5.8</td><td>0.0</td><td>91.0</td><td>8.9</td><td>0.0</td></tr><tr><td>M</td><td>70.8</td><td>28.8</td><td>0.4</td><td>66.9</td><td>32.5</td><td>0.6</td></tr><tr><td>H</td><td>13.1</td><td>69.7</td><td>17.2</td><td>13.1</td><td>69.7</td><td>17.2</td></tr><tr><td></td><td colspan="3">(c) Accepts</td><td colspan="3">(d) Badges</td></tr><tr><td>t-1 to t</td><td>L</td><td>M</td><td>H</td><td>L</td><td>M</td><td>H</td></tr><tr><td>L</td><td>83.6</td><td>16.3</td><td>0.1</td><td>88.0</td><td>12.0</td><td>0.0</td></tr><tr><td>M</td><td>62.2</td><td>36.9</td><td>0.8</td><td>63.5</td><td>35.7</td><td>0.8</td></tr><tr><td>H</td><td>11.5</td><td>69.2</td><td>19.3</td><td>13.1</td><td>69.7</td><td>17.2</td></tr></table>




<table><tr><td colspan="7">表 4. 平均后向转移矩阵</td></tr><tr><td></td><td colspan="3">(a) 平均交互作用</td><td colspan="3">(b) 赞成票</td></tr><tr><td>t-1 至t</td><td>L</td><td>M</td><td>H</td><td>L</td><td>M</td><td>H</td></tr><tr><td>L</td><td>94.2 </td><td>5.8</td><td>0.0</td><td>91.0</td><td>8.9</td><td>0.0</td></tr><tr><td>中号</td><td>70.8 </td><td>28.8</td><td>0.4</td><td>66.9</td><td>32.5</td><td>0.6</td></tr><tr><td>H</td><td>13 .1</td><td>69.7</td><td>17.2</td><td>13.1</td><td>69.7</td><td>17.2</td></tr><tr><td></td><td colspan="3">(c) 接受</td><td colspan="3">(d) 徽章</td></tr><tr><td>t-1 至t</td><td>L</td><td>M</td><td>H</td><td>L</td><td>M</td><td>H</td></tr><tr><td>L</td><td>83 .6</td><td>16.3</td><td>0.1</td><td>88.0</td><td>12.0</td><td>0.0</td></tr><tr><td>M</td><td >62.2</td><td>36.9</td><td>0.8</td><td>63.5</td><td>35.7</td><td>0.8</td></tr><tr><td>H</td ><td>11.5</td><td>69.2</td><td>19.3</td><td>13.1</td><td>69.7</td><td>17.2</td></tr></table>


Note: All numbers are probabilities (%).




注：所有数字均为概率 (%)。


With more than 200 up-votes and 30 accepted answers each day on SuperUser, the effects of these mechanisms significantly enhance the contributions at the community level.




SuperUser 每天有超过 200 个赞成票和 30 个接受答案，这些机制的效果显着增强了社区层面的贡献。


## Design Simulations




## 设计模拟


We now turn to the normative perspective on motivating mechanisms using design simulations.<sup>9</sup> We do three simulation experiments to see if platform designers can encourage more contributions by strengthening users’ internalized extrinsic motivations through calibrating specific IT-artifacts: up-votes received for answers, accepted answers, and badges. If it becomes easier to enhance peer recognition and selfimage through each of these channels, are users going to provide more answers? We hypothetically double the value of the variables Upvotes\_answer, Accepted\_answers, and Badges, making it twice as easy to earn each reward. We then simulate, under each scenario, the evolution of the total number of answers and users in state M and state H over time.




现在，我们转向使用设计模拟的激励机制的规范视角。<sup>9</sup>我们进行了三个模拟实验，看看平台设计者是否可以通过校准特定的 IT 工件（对答案收到的赞成票、接受的答案和徽章）来加强用户的内在外在动机，从而鼓励更多贡献。如果通过这些渠道更容易增强同伴认可和自我形象，用户是否会提供更多答案？假设我们将变量 Upvotes\_answer、Accepted\_answers 和 Badges 的值加倍，从而使获得每个奖励的难度加倍。然后，我们在每种情况下模拟状态 M 和状态 H 下答案和用户总数随时间的演变。


Figure 5 presents the results, which are the average of 100 simulation iterations for each user on each date. The first column (graphs 1, 4, and 7) shows the simulated total number of answers (grey dots) versus the actual total number of answers (black dots) for the doubled Upvotes\_answer, Accepted\_answers, and Badges, respectively. To better illustrate the effects and trends, we fit the simulated answers with a dash curve and the actual answers with a solid curve. Both curves are smoothed. In the second column (graphs 2, 5, and 8), we plot the number of users who are in state M. Similarly, the solid line shows users in state M under the current design, and the dashed lines show simulated users in state M if we were to change the corresponding motivation mechanism. In the third column, we plot the number of users who are in state H in a similar way.




图 5 显示了结果，这是每个用户在每个日期进行 100 次模拟迭代的平均值。第一列（图 1、图 4 和图 7）分别显示了加倍的赞成\_答案、接受\_答案和徽章的模拟答案总数（灰点）与实际答案总数（黑点）。为了更好地说明效果和趋势，我们用虚曲线拟合模拟答案，用实曲线拟合实际答案。两条曲线均经过平滑处理。在第二列（图2、图5和图8）中，我们绘制了处于状态M的用户数量。同样，实线表示当前设计下处于状态M的用户，虚线表示如果我们改变相应的激励机制则模拟处于状态M的用户。在第三列中，我们以类似的方式绘制处于状态 H 的用户数量。


We discover three patterns here. First, the simulated number of answers is greater than the actual data in all three cases. This means that when it becomes easier to receive rewards to enhance one’s internalized extrinsic motivation (through upvotes, accepted answers or badges), users will contribute more. Second, up-votes and accepted answers seem to be more effective than badges, which may be due to the moral licensing effect of badges in high motivation state. However, as a design mechanism, badges are much easier to change than up-votes and accepted answers. To test the effectiveness of different badges, a platform designer could potentially examine the simulated experiment on many specific badges. Third, highly motivated users are critical to the knowledge contribution and accumulation in the online community. The actual number of users in state H is relatively small, and it also declines slightly. The stimulation of more up-votes, accepted answers, and badges not only boost the number of these users in state H, but also smooth the declining trend.




我们在这里发现了三种模式。首先，在这三种情况下，模拟的答案数量都大于实际数据。这意味着，当更容易获得奖励以增强一个人的内在外在动机（通过投票、接受的答案或徽章）时，用户将做出更多贡献。其次，赞成票和接受的答案似乎比徽章更有效，这可能是由于徽章在高动机状态下的道德许可效应。然而，作为一种设计机制，徽章比赞成票和接受的答案更容易改变。为了测试不同徽章的有效性，平台设计者可以检查许多特定徽章的模拟实验。第三，积极性高的用户对于网络社区的知识贡献和积累至关重要。 H状态的实际用户数量相对较少，并且也略有下降。更多点赞、接受答案和徽章的刺激不仅可以增加处于 H 状态的用户数量，还可以平滑下降的趋势。


Together, our experiments suggest that it is important for platform designers to manage internalized extrinsic motivation, so as to encourage users to contribute more. Note that we are not suggesting a constant effect of these mechanisms; as we change the design of the community, the perception of the users may change accordingly. Rather, our design simulation opens up a direction for further exploration.




总之，我们的实验表明，平台设计者管理内在的外在动机非常重要，以鼓励用户做出更多贡献。请注意，我们并不是暗示这些机制会产生持续的影响；当我们改变社区的设计时，用户的看法可能会相应改变。相反，我们的设计模拟为进一步探索开辟了方向。


![](/api/attachments/TMJFTJXB/fulltext/images/5b0a8c286ad8556b028c3b3ec70f3b3b9889162c264000c032ad09756d7f05f8.jpg)  
Figure 5. Design Simulation: What If Rewards Are Easier to Earn?




![](/api/attachments/TMJFTJXB/fulltext/images/5b0a8c286ad8556b028c3b3ec70f3b3b9889162c264000c032ad09756d7f05f8.jpg)  
图 5. 设计模拟：如果奖励更容易获得怎么办？


## Robustness Checks




## 稳健性检查


We conduct several robustness checks and provide the detailed results in Appendix D. First, to ensure that our results are not biased by the sample period, we estimate the model on several alternative steady-state sample periods (e.g., 301–500 days). The results from those estimations are consistent to the results reported above. We also examine the first 100 days, where there is substantial fluctuation of user activities. Compared with the steady periods, the magnitude of coefficients across states do not have an evidently different pattern.




我们进行了几次稳健性检查，并在附录 D 中提供了详细结果。首先，为了确保我们的结果不会因样本期而产生偏差，我们在几个替代稳态样本期（例如 301-500 天）上估计模型。这些估计的结果与上面报告的结果一致。我们还检查了前 100 天，其中用户活动存在大幅波动。与稳定期相比，各州系数的大小没有明显不同的模式。


Second, to probe deeper into the possible heterogeneity of users and questions, we test the following variables in our model:




其次，为了更深入地探讨用户和问题可能存在的异质性，我们在模型中测试了以下变量：


(1) Special roles of users. Some users are elected as moderators, which may explain their higher contribution. We include a binary indicator of whether a user is a moderator, and find its coefficient is only significant in states M and H. Hence, on average a moderator is more likely to be in higher motivation states.




(1)用户的特殊角色。一些用户被选为版主，这也许可以解释他们的贡献较高。我们包含一个用户是否是主持人的二元指标，并发现其系数仅在状态 M 和 H 中显着。因此，平均而言，主持人更有可能处于较高的动机状态。


(2) Questions from influential users. Questions from influence users, such as moderators, can motivate users to contribute. We construct a variable to measure how many questions are asked by moderators. The coefficient on this variable is insignificant across all states, suggesting that the overall contribution of users is insensitive to whether or not the question comes from influential individuals. These analyses provide additional insights, while our main results remain consistent as before.




(2)有影响力的用户提出的问题。来自有影响力的用户（例如版主）的问题可以激励用户做出贡献。我们构造一个变量来衡量主持人提出了多少问题。该变量的系数在所有州中都不显着，这表明用户的总体贡献对问题是否来自有影响力的个人不敏感。这些分析提供了额外的见解，而我们的主要结果与以前保持一致。


Third, we conduct robustness checks on different time aggregations and user samples. We aggregate daily data into weekly to smooth any possible fluctuation during a week (e.g., weekday versus weekend effect). Results on weekly data are consistent with the daily analysis. To alleviate computational burden, results presented so far are based on a sample with users that have contributed more than 10 answers during the sample period. We also estimate the model separately on all users on the site, users who have contributed at least one answer, and those with more than 50 answers, respectively. The results are consistent.




第三，我们对不同时间聚合和用户样本进行稳健性检查。我们将每日数据汇总为每周数据，以平滑一周内任何可能的波动（例如，工作日与周末的影响）。每周数据的结果与每日分析一致。为了减轻计算负担，迄今为止给出的结果基于样本，其中用户在样本期间贡献了超过 10 个答案。我们还分别对网站上的所有用户、至少提供了一个答案的用户以及提供超过 50 个答案的用户分别估计模型。结果是一致的。


## Conclusions




## 结论


User contributions are voluntary but vital in many online communities. This paper studies the effects of motivating mechanisms on voluntary contributions through IT-artifacts design from a dynamic perspective. Using a hidden Markov model under the public goods framework, we identify three motivation states that increase in the propensity of contribution, and investigate the effect of several types of mechanisms (reciprocity, peer recognition, and self-image) on transitioning users between the states.




用户贡献是自愿的，但在许多在线社区中至关重要。本文从动态角度研究了信息技术制品设计激励机制对自愿捐款的影响。使用公共物品框架下的隐马尔可夫模型，我们确定了贡献倾向增加的三种动机状态，并研究了几种类型的机制（互惠、同伴认可和自我形象）对用户在状态之间转换的影响。


This dynamic perspective is a unique feature of our work. The existing literature relies on a conventional static approach, which implicitly assumes that the relationship between motivating mechanisms and user contributions is static. In contrast, our dynamic approach allows the effect of motivating mechanisms to change across users and over time. As such, our approach advances the literature on voluntary user contributions in online communities. It also enriches the literature on public goods that features in impure altruism and internalized extrinsic motivations.




这种动态的视角是我们工作的独特之处。现有文献依赖于传统的静态方法，该方法隐含地假设激励机制和用户贡献之间的关系是静态的。相比之下，我们的动态方法允许激励机制的效果随着用户和时间的推移而变化。因此，我们的方法推进了在线社区中自愿用户贡献的文献。它还丰富了有关公共物品的文献，这些文献以不纯粹的利他主义和内在的外在动机为特征。


Our results from the dynamic model shed light on a key question in the research on online communities: how to design effective IT artifacts that can engage users to contribute. We find that IT artifacts (e.g., up-votes, accepted answers, and badges) as motivational devices are useful to elevate contributions, but their influence varies significantly with motivation states. Although badges are widely used in practice, they can be ineffective for users in high motivation state. Hence, the design of a badge system (or gamification in a broader sense) deserves careful consideration. In contrast, up-votes and accepted answers are shown to be much more effective across motivation states. These results highlight the effectiveness of peer recognition as a motivating scheme, especially in switching users to and retaining them in higher motivation states.




我们的动态模型结果揭示了在线社区研究中的一个关键问题：如何设计可以吸引用户做出贡献的有效 IT 工件。我们发现 IT 工件（例如，赞成票、接受的答案和徽章）作为激励手段对于提升贡献很有用，但它们的影响因激励状态而异。尽管徽章在实践中被广泛使用，但对于处于高动机状态的用户来说，它们可能无效。因此，徽章系统（或更广泛意义上的游戏化）的设计值得仔细考虑。相比之下，在不同的动机状态下，赞成票和接受的答案被证明更加有效。这些结果凸显了同伴认可作为激励方案的有效性，特别是在将用户切换到并保持更高动机状态方面。


Our results provide important managerial implications for devising various mechanisms, and evaluating their effectiveness on encouraging user contribution. First, managers need to be mindful that users have a different propensity to contribute, and it is crucial to design proper instruments to motivate contributions. The changing influence of peerrecognition in different states suggests that community managers can gear their intervention toward users in specific motivation states. For example, if the goal is to induce more users to be in high motivation state, then encouraging users to accept high quality answers may be a more effective intervention than adding more badges. Second, our structural model allows community managers to perform interesting design simulations and evaluate the consequence of changing certain mechanisms. As our design simulations suggest, if the design of the community makes it easier for users to gain up-votes or accepted answers, for example by allowing users to accept more than one answer of high quality, then users are more likely to become highly motivated. A platform designer can also experiment with a specific badge and decide how to adjust it. Third, managers should also consider how to foster the community. It would be helpful to attract new users to make the social effect more prominent, and encourage users to ask questions to raise the demand of knowledge. The estimated hidden states from our model allow community managers to classify users in real time and help them target the right kinds of users.




我们的结果为设计各种机制并评估其鼓励用户贡献的有效性提供了重要的管理意义。首先，管理者需要注意用户有不同的贡献倾向，设计适当的工具来激励贡献至关重要。不同状态下同伴认可的影响不断变化表明社区管理者可以针对特定动机状态的用户进行干预。例如，如果目标是诱导更多用户处于高动机状态，那么鼓励用户接受高质量答案可能是比添加更多徽章更有效的干预措施。其次，我们的结构模型允许社区管理者进行有趣的设计模拟并评估改变某些机制的后果。正如我们的设计模拟所表明的那样，如果社区的设计使用户更容易获得赞成票或被接受的答案，例如允许用户接受多个高质量的答案，那么用户更有可能变得高度积极。平台设计者还可以尝试特定的徽章并决定如何调整它。第三，管理者还应该考虑如何培育社区。有利于吸引新用户，使社交效果更加凸显，并鼓励用户提出问题，提高知识需求。我们的模型估计的隐藏状态允许社区管理者实时对用户进行分类，并帮助他们定位正确的用户类型。


Our dynamic framework would help motivate future work on the design of IT artifacts in online communities. First, while we use a knowledge sharing community as a testing field, our framework is applicable to many other online communities relying on voluntary user contributions. One may caution that there are other design features unavailable in our contexts. However, our dynamic framework, with appropriate modifications under specific research context (especially the utility function), can be extended to other settings. Second, our findings point to several interesting avenues of future research. For instance, the insignificant effect of badges in high motivation state implies that there may be too many trivial badges in the system. It would be interesting to identify the types of badges that are truly effective. Another example is that from our analysis, we cannot conclude the changing effectiveness of motivating mechanisms across the lifecycle of the community. A more in-depth study along this line may generate interesting implications in the future.




我们的动态框架将有助于推动在线社区中 IT 工件设计的未来工作。首先，虽然我们使用知识共享社区作为测试领域，但我们的框架适用于许多其他依赖用户自愿贡献的在线社区。人们可能会注意到，在我们的环境中还有其他设计功能不可用。然而，我们的动态框架，在特定的研究背景下（特别是效用函数）进行适当的修改，可以扩展到其他设置。其次，我们的研究结果指出了未来研究的几个有趣的途径。例如，徽章在高动机状态下的作用不显着意味着系统中可能存在太多琐碎的徽章。确定真正有效的徽章类型会很有趣。另一个例子是，从我们的分析中，我们无法得出激励机制在整个社区生命周期中的有效性变化的结论。沿着这条线进行更深入的研究可能会在未来产生有趣的影响。


More broadly, this research is related to open models of coproduction in user communities over time. Our study informs the design of internalized extrinsic mechanisms in contexts such as crowdsourcing, user generated contents, open innovation, and even crowdfunding. As data become available, future research may expand into these broader areas. In such environments, production moves beyond the boundary of traditional, formal organizational structure, and voluntary contributions facilitated by IT artifacts become crucial. New challenges such as the design of motivating mechanisms in a dynamic environment need to be managed, so that the coproduction of open communities can be sustainable (Zhu and Zhou 2012). Our paper, although currently examined in a knowledge sharing community, may generate new insights into designing IT artifacts to engage voluntary contributions in online communities without formal governance or compensation structures in the traditional sense. While many open questions remain, we hope our analysis framework and initial findings will help stimulate more research in this growing area.




更广泛地说，这项研究与用户社区随着时间的推移共同生产的开放模型有关。我们的研究为众包、用户生成内容、开放创新甚至众筹等背景下的内在外在机制的设计提供了信息。随着数据的出现，未来的研究可能会扩展到这些更广泛的领域。在这样的环境中，生产超越了传统、正式的组织结构的边界，IT 工件促进的自愿贡献变得至关重要。需要管理新的挑战，例如动态环境中激励机制的设计，以便开放社区的共同生产能够可持续（Zhu and Zhou 2012）。我们的论文虽然目前正在知识共享社区中进行审查，但可能会产生新的见解，设计 IT 工件以在没有传统意义上的正式治理或补偿结构的情况下在在线社区中进行自愿贡献。尽管仍然存在许多悬而未决的问题，但我们希望我们的分析框架和初步发现将有助于刺激这一不断发展的领域进行更多研究。


## Acknowledgments




## 致谢


The authors are grateful for the comments and suggestions made by three anonymous reviewers, the associate editor, and the senior editor. Part of the work is supported by the National Natural Science Foundation of China (#71620107005) and the QD Innovation Leadership Project (#13-CY-4).




作者感谢三位匿名审稿人、副主编和高级编辑提出的意见和建议。部分工作得到国家自然科学基金（#71620107005）和QD创新领导力项目（#13-CY-4）的支持。


## References




＃＃ 参考


Albert, J. H., and Chib, S. 1993. “Bayesian Analysis of Binary and Polychotomous Response Data,” Journal of the American Statistical Association (88:422), pp. 669-679.




Albert, J. H. 和 Chib, S. 1993 年。“二元和多分类响应数据的贝叶斯分析”，《美国统计协会杂志》(88:422)，第 669-679 页。


Andreoni, J. 1988. “Privately Provided Public Goods in A Large Economy: The Limits of Altruism,” Journal of Public Economics (35:1), pp. 57-73.




Andreoni, J. 1988。“大型经济体中私人提供的公共物品：利他主义的局限性”，《公共经济学杂志》(35:1)，第 57-73 页。


Andreoni, J. 1990. “Impure Altruism and Donations to Public Goods: A Theory of Warm-Glow Giving,” The Economic Journal (100:401), pp. 464-477.




Andreoni, J. 1990。“不纯利他主义和公共物品捐赠：温暖奉献理论”，《经济杂志》(100:401)，第 464-477 页。


Bénabou, R., and Tirole, J. 2006. “Incentives and Prosocial Behavior,” American Economic Review (96:5), pp. 1652-1678.




Bénabou, R. 和 Tirole, J. 2006 年。“激励和亲社会行为”，美国经济评论 (96:5)，第 1652-1678 页。


Boudreau, K. J., and Lakhani, K. R. 2009. “How to Manage Outside Innovation,” MIT Sloan Management Review (50:4), pp. 69-73.




Boudreau, K. J. 和 Lakhani, K. R. 2009 年。“如何管理外部创新”，《麻省理工学院斯隆管理评论》(50:4)，第 69-73 页。


Butler, B. S. 2001. “Membership Size, Communication Activity, and Sustainability: A Resource-Based Model of Online Social Structures,” Information Systems Research (12:4), pp. 346-362.




Butler, B. S. 2001。“会员规模、沟通活动和可持续性：基于资源的在线社会结构模型”，信息系统研究 (12:4)，第 346-362 页。


Chen, Y., Harper, F. M., Konstan, J., and Xin Li, S. 2010. “Social Comparisons and Contributions to Online Communities: A Field Experiment on MovieLens,” The American Economic Review (100:4), pp. 1358-1398.




Chen, Y.、Harper, F. M.、Konstan, J. 和 Xin Li, S. 2010。“社会比较和对在线社区的贡献：MovieLens 的现场实验”，《美国经济评论》(100:4)，第 1358-1398 页。


Chib, S. 2001. “Markov Chain Monte Carlo Methods: Computation and Inference,” in Handbook of Econometrics (Volume 5), J. J. Heckman and E. Leamer (eds.), Amsterdam: North-Holland, pp. 3569-3649.




Chib, S. 2001。“马尔可夫链蒙特卡罗方法：计算和推理”，《计量经济学手册》（第 5 卷），J. J. Heckman 和 E. Leamer（编辑），阿姆斯特丹：北荷兰，第 3569-3649 页。


Chiu, C.-M., Hsu, M.-H., and Wang, E. T. G. 2006. “Understanding Knowledge Sharing in Virtual Communities: An Integration of Social Capital and Social Cognitive Theories,” Decision Support Systems (42:3), pp. 1872-1888.




Chiu, C.-M.、Hsu, M.-H. 和 Wang, E. T. G. 2006 年。“理解虚拟社区中的知识共享：社会资本和社会认知理论的整合”，决策支持系统 (42:3)，第 1872-1888 页。


Deci, E. L., and Ryan, R. M. 2002. Handbook of Self-Determination Research, Rochester, NY: University Rochester Press.




Deci, E. L. 和 Ryan, R. M. 2002 年。《自我决定研究手册》，罗彻斯特，纽约：罗彻斯特大学出版社。


Franzoni, C., and Sauermann, H. 2014. “Crowd Science: The Organization of Scientific Research in Open Collaborative Projects,” Research Policy (43:1), pp. 1-20.




Franzoni, C. 和 Sauermann, H. 2014 年。“群体科学：开放合作项目中的科学研究组织”，研究政策 (43:1)，第 1-20 页。


Gneezy, A., Imas, A., Brown, A., Nelson, L. D., and Norton, M. I. 2011. “Paying to Be Nice: Consistency and Costly Prosocial Behavior,” Management Science (58:1), pp. 179-187.




Gneezy, A.、Imas, A.、Brown, A.、Nelson, L. D. 和 Norton, M. I. 2011。“为友善付费：一致性和昂贵的亲社会行为”，管理科学 (58:1)，第 179-187 页。


Goes, P. B., Guo, C., and Lin, M. 2016. “Do Incentive Hierarchies Induce User Effort? Evidence from an Online Knowledge Exchange,” Information Systems Research (27:3), pp. 497-516.




Goes, P. B.、Guo, C. 和 Lin, M. 2016。“激励层次结构会导致用户努力吗？来自在线知识交换的证据”，信息系统研究 (27:3)，第 497-516 页。


Goh, J. M., Gao, G., and Agarwal, R. 2016. “The Creation of Social Value: Can an Online Health Community Reduce Rural– Urban Health Disparities?” MIS Quarterly (40:1), pp. 247-263.




Goh, J. M.、Gao, G. 和 Agarwal, R. 2016。“社会价值的创造：在线健康社区能否减少城乡健康差距？” MIS 季刊 (40:1)，第 247-263 页。


Gu, B., Konana, P., Rajagopalan, B., and Chen, H.-W. M. 2007. “Competition Among Virtual Communities and User Valuation: The Case of Investing-Related Communities,” Information Systems Research (18:1), pp. 68-85.




Gu, B.、Konana, P.、Rajagopalan, B. 和 Chen, H.-W. M. 2007。“虚拟社区和用户估值之间的竞争：投资相关社区的案例”，信息系统研究 (18:1)，第 68-85 页。


Halfaker, A., Geiger, R. S., Morgan, J. T., and Riedl, J. 2013. “The Rise and Decline of an Open Collaboration System How




Halfaker, A.、Geiger, R. S.、Morgan, J. T. 和 Riedl, J. 2013 年。“开放式协作系统的兴衰如何


Wikipedia’s Reaction to Popularity Is Causing Its Decline,” American Behavioral Scientist (57:5), pp. 664-688.




维基百科对受欢迎程度的反应正在导致其衰落”，《美国行为科学家》(57:5)，第 664-688 页。


Hamilton, J. D. 1989. “A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle,” Econometrica (57:2), pp. 357-384.




Hamilton, J. D. 1989。“非平稳时间序列和经济周期经济分析的新方法”，Econometrica (57:2)，第 357-384 页。


Heckman, J. J. 1981. “Heterogeneity and State Dependence,” in Studies in Labor Markets, S. Rosen (ed.), Chicago: University of Chicago Press, pp. 91-139.




Heckman, J. J. 1981。《劳动力市场研究》中的“异质性和国家依赖性”，S. Rosen（主编），芝加哥：芝加哥大学出版社，第 91-139 页。


Huang, P., and Zhang, Z. 2016. “Participation in Open Knowledge Communities and Job-Hopping: Evidence from Enterprise Software,” MIS Quarterly (40:3), pp. 785-806.




Huang, P. 和Zhang, Z. 2016 年。“参与开放知识社区和跳槽：来自企业软件的证据”，MIS 季刊 (40:3)，第 785-806 页。


Huang, Y., Vir Singh, P., and Srinivasan, K. 2014. “Crowdsourcing New Product Ideas Under Consumer Learning,” Management Science (60:9), pp. 2138-2159.




Huang, Y.、Vir Singh, P. 和 Srinivasan, K. 2014 年。“消费者学习下的众包新产品创意”，管理科学 (60:9)，第 2138-2159 页。


Jasra, A., Holmes, C. C., and Stephens, D. A. 2005. “Markov Chain Monte Carlo Methods and the Label Switching Problem in Bayesian Mixture Modeling,” Statistical Science (20:1), pp. 50-67.




Jasra, A.、Holmes, C. C. 和 Stephens, D. A. 2005 年。“马尔可夫链蒙特卡罗方法和贝叶斯混合建模中的标签切换问题”，统计科学 (20:1)，第 50-67 页。


Kankanhalli, A., Tan, B. C. Y., and Wei, K.-K. 2005. “Contributing Knowledge to Electronic Knowledge Repositories: An Empirical Investigation,” MIS Quarterly (29:1), pp. 113-143.




Kankanhalli, A.、Tan, B. C. Y. 和 Wei, K.-K. 2005 年。“向电子知识库贡献知识：实证研究”，MIS 季刊 (29:1)，第 113-143 页。


Khansa, L., Ma, X., Liginlal, D., and Kim, S. S. 2015. “Understanding Members’ Active Participation in Online Question-and-Answer Communities: A Theory and Empirical Analysis,” Journal of Management Information Systems (32:2), pp. 162-203.




Khansa, L.、Ma, X.、Liginlal, D. 和 Kim, S. S. 2015 年。“了解会员在在线问答社区中的积极参与：理论和实证分析”，《管理信息系统杂志》(32:2)，第 162-203 页。


Kim, C.-J., and Nelson, C. R. 1999. State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications, Cambridge, MA: The MIT Press.




Kim, C.-J. 和 Nelson, C. R. 1999 年。具有机制切换的状态空间模型：经典和吉布斯采样方法及其应用，马萨诸塞州剑桥：麻省理工学院出版社。


Lakhani, K. R., and von Hippel, E. 2003. “How Open Source Software Works: ‘Free’ User-to-User Assistance,” Research Policy (32:6), pp. 923-943.




Lakhani, K. R. 和 von Hippel, E. 2003 年。“开源软件如何工作：‘免费’用户对用户协助”，研究政策 (32:6)，第 923-943 页。


Ma, M., and Agarwal, R. 2007. “Through a Glass Darkly: Information Technology Design, Identity Verification, and Knowledge Contribution in Online Communities,” Information Systems Research (18:1), pp. 42-67.




Ma, M. 和 Agarwal, R. 2007 年。“透过黑暗的玻璃：在线社区中的信息技术设计、身份验证和知识贡献”，信息系统研究 (18:1)，第 42-67 页。


MacDonald, I. L., and Zucchini, W. 1997. Hidden Markov and Other Models for Discrete- Valued Time Series, Boca Raton, FL: CRC Press.




MacDonald, I. L. 和 Zucchini, W. 1997。隐马尔可夫和其他离散值时间序列模型，博卡拉顿，佛罗里达州：CRC Press。


Metz, R. 2012. “Why Did Reddit Succeed Where Digg Failed?,” MIT Technology Review, July 18.




Metz, R. 2012。“为什么 Reddit 在 Digg 失败的地方成功了？”，《麻省理工科技评论》，7 月 18 日。


Netzer, O., Lattin, J. M., and Srinivasan, V. 2008. “A Hidden Markov Model of Customer Relationship Dynamics,” Marketing Science (27:2), pp. 185-204.




Netzer, O.、Lattin, J. M. 和 Srinivasan, V. 2008 年。“客户关系动态的隐马尔可夫模型”，《营销科学》(27:2)，第 185-204 页。


Peng, G., and Dey, D. 2013. “A Dynamic View of the Impact of Network Structure on Technology Adoption: The Case of OSS Development,” Information Systems Research (24:4), pp. 1087-1099.




Peng, G. 和 Dey, D. 2013 年。“网络结构对技术采用影响的动态观点：OSS 开发案例”，信息系统研究 (24:4)，第 1087-1099 页。


Piskorski, M. J., Eisenmann, T. R., Bussgang, J. J., and Chen, D. 2010. “Foursquare,” Harvard Business School Case 711-418.




Piskorski, M. J.、Eisenmann, T. R.、Bussgang, J. J. 和 Chen, D. 2010。“Foursquare”，哈佛商学院案例 711-418。


Porter, C. E., and Donthu, N. 2008. “Cultivating Trust and Harvesting Value in Virtual Communities,” Management Science (54:1), pp. 113-128.




Porter, C. E. 和 Donthu, N. 2008 年。“在虚拟社区中培养信任并收获价值”，管理科学 (54:1)，第 113-128 页。


Rabiner, L. 1989. “A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition,” Proceedings of the IEEE (77:2), pp. 257-286.




Rabiner, L. 1989。“语音识别中隐马尔可夫模型和选定应用的教程”，IEEE 会议录 (77:2)，第 257-286 页。


Ransbotham, S., and Kane, G. C. 2011. “Membership Turnover and Collaboration Success in Online Communities: Explaining Rises,” MIS Quarterly (35:3), pp. 613-627.




Ransbotham, S. 和 Kane, G. C. 2011 年。“在线社区中的会员流动和协作成功：解释崛起”，MIS 季刊 (35:3)，第 613-627 页。


Ray, S., Kim, S. S., and Morris, J. G. 2014. “The Central Role of Engagement in Online Communities,” Information Systems Research (25:3), pp. 528-546.




Ray, S.、Kim, S. S. 和 Morris, J. G. 2014 年。“在线社区参与的核心作用”，信息系统研究 (25:3)，第 528-546 页。


Reiss, P. C., and Wolak, F. A. 2007. “Structural Econometric Modeling: Rationales and Examples from Industrial Organization,” Chapter 64 in Handbook of Econometrics (Volume 6), J. J. Heckman and E. E. Leamer (eds.), Amsterdam: North-Holland, pp. 4277-4415.




Reiss, P. C. 和 Wolak, F. A. 2007 年。“结构计量经济学模型：工业组织的原理和示例”，《计量经济学手册》第 64 章（第 6 卷），J. J. Heckman 和 E. E. Leamer（编辑），阿姆斯特丹：北荷兰，第 4277-4415 页。


Roberts, J. A., Hann, I. H., and Slaughter, S. A. 2006. “Understanding the Motivations, Participation, and Performance of Open Source Software Developers: A Longitudinal Study of the Apache Projects,” Management Science (52:7), pp. 984-999.




Roberts, J. A.、Hann, I. H. 和 Slaughter, S. A. 2006 年。“了解开源软件开发人员的动机、参与和绩效：Apache 项目的纵向研究”，管理科学 (52:7)，第 984-999 页。


Rossi, P. E., and Allenby, G. M. 2003. “Bayesian Statistics and Marketing,” Marketing Science (22:3), pp. 304-328.




Rossi, P. E. 和 Allenby, G. M. 2003 年。“贝叶斯统计与营销”，《营销科学》(22:3)，第 304-328 页。


Rydén, T., Teräsvirta, T., and Åsbrink, S. 1998. “Stylized Facts of Daily Return Series and the Hidden Markov Model,” Journal of Applied Econometrics (13:3), pp. 217-244.




Rydén, T.、Teräsvirta, T. 和 Åsbrink, S. 1998。“日收益系列的程式化事实和隐马尔可夫模型”，《应用计量经济学杂志》(13:3)，第 217-244 页。


Sauermann, H., and Franzoni, C. 2015. “Crowd Science User Contribution Patterns and Their Implications,” Proceedings of the National Academy of Sciences (112:3), pp. 679-684.




Sauermann, H. 和 Franzoni, C. 2015 年。“群体科学用户贡献模式及其影响”，《美国国家科学院院刊》(112:3)，第 679-684 页。


Simonite, T. 2013. “The Decline of Wikipedia: Even As More People Than Ever Rely on It, Fewer People Create It,” MIT Technology Review, October 22.




Simonite, T. 2013。“维基百科的衰落：尽管依赖它的人比以往任何时候都多，但创建它的人却越来越少”，《麻省理工学院技术评论》，10 月 22 日。


Singh, P. V., Tan, Y., and Youn, N. 2011. “A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects,” Information Systems Research (22:4), pp. 790-807.




Singh, P. V.、Tan, Y. 和 Youn, N. 2011。“开源软件项目中开发人员学习动态的隐马尔可夫模型”，信息系统研究 (22:4)，第 790-807 页。


Toubia, O., and Stephen, A. T. 2013. “Intrinsic vs. Image-Related Utility in Social Media: Why Do People Contribute Content to Twitter?,” Marketing Science (32:3), pp. 368-392.




Toubia, O. 和 Stephen, A. T. 2013 年。“社交媒体中的内在效用与图像相关效用：人们为什么向 Twitter 贡献内容？”，《营销科学》(32:3)，第 368-392 页。


von Hippel, E. 2005. Democratizing Innovation, Cambridge, MA: The MIT Press.




von Hippel, E. 2005。民主化创新，剑桥，马萨诸塞州：麻省理工学院出版社。


von Krogh, G., Haefliger, S., Spaeth, S., and Wallin, M. 2012. “Carrots and Rainbows: Motivation and Social Practice in Open Source Software Development,” MIS Quarterly (36:2), pp. 649-676.




von Krogh, G.、Haefliger, S.、Spaeth, S. 和 Wallin, M. 2012 年。“胡萝卜和彩虹：开源软件开发中的动机和社会实践”，MIS 季刊 (36:2)，第 649-676 页。


Wooldridge, J. M. 2010. Econometric Analysis of Cross Section and Panel Data (2<sup>nd</sup> ed.), Cambridge, MA: The MIT Press.




Wooldridge, J. M. 2010。横截面和面板数据的计量经济学分析（第二版），马萨诸塞州剑桥：麻省理工学院出版社。


Xu, S. X., Zhu, C., and Zhu, K. X. 2012. “Why Do Firms Adopt Innovations in Bandwagons? Herding under Competition in Open Standards Adoption.” International Journal of Technology Management (59:1/2), pp. 63-91.




Xu, S. X.、Zhu, C. 和 Zhu, K. X. 2012。“为什么企业会跟风创新？开放标准采用竞争中的羊群效应”。国际技术管理杂志 (59:1/2)，第 63-91 页。


Yan, L., and Tan, Y. 2014. “Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients,” Information Systems Research (25:4), pp. 690-709.




Yan, L. 和 Tan, Y. 2014 年。“感觉忧郁？上网：患者社会支持的实证研究”，信息系统研究 (25:4)，第 690-709 页。


Zhu, K. X., and Zhou, Z. Z. 2012. “Lock-In Strategy in Software Competition: Open-Source Software vs. Proprietary Software,” Information Systems Research (23:2), pp. 536-545.




Zhu, K. X. 和 Zhou, Z. Z. 2012 年。“软件竞争中的锁定策略：开源软件与专有软件”，信息系统研究 (23:2)，第 536-545 页。


Zichermann, G., and Cunningham, C. 2011. Gamification by Design: Implementing Game Mechanics in Web and Mobile Apps (1<sup>st</sup> ed.), Sebastopol, CA: O’Reilly Media.




Zichermann, G. 和 Cunningham, C. 2011 年。设计游戏化：在 Web 和移动应用程序中实现游戏机制（第一版），加利福尼亚州塞巴斯托波尔：O’Reilly Media。


## About the Authors




## 关于作者


Wei Chen is an assistant professor of Management Information Systems at the Eller College of Management, University of Arizona. He received his Ph.D. in Business Administration from the Rady School of Management, University of California, San Diego. His research focuses on how technology transforms innovation. Currently, he is investigating how organizations manage IT-enabled external resources to produce knowledge and products in areas such as crowdsourcing, crowdfunding, and digital marketing.




陈伟是亚利桑那大学埃勒管理学院管理信息系统助理教授。他获得了博士学位。毕业于加州大学圣地亚哥分校拉迪管理学院工商管理专业。他的研究重点是技术如何转变创新。目前，他正在研究组织如何管理 IT 支持的外部资源，以在众包、众筹和数字营销等领域生产知识和产品。


Xiahua Wei is an assistant professor of Economics at the University of Washington, Bothell School of Business. She received her Ph.D. in Economics from the University of California, San Diego. Her research interest is the economics of information technology, with a focus on innovation strategy, marketing strategy, and mechanism design in technology-enabled markets.




魏夏华是华盛顿大学博塞尔商学院经济学助理教授。她获得了博士学位。加州大学圣地亚哥分校经济学博士。她的研究兴趣是信息技术经济学，重点是技术驱动市场的创新策略、营销策略和机制设计。


Kevin Xiaoguo Zhu received his Ph.D. from Stanford and is currently a professor of innovation and technology at the Rady School of Management, University of California, San Diego. His research focuses on technology-enabled innovations in a global environment, economic impacts of IT on firms/industries, data analytics, IT-enabled supply chains, and competition in software, media and telecomm industries. His research has been published in top academic journals such as Management Science, Information Systems Research, MIS Quarterly, and Marketing Science. His work has received more than 7300 citations in Google Scholar, and has been recognized by several Best Paper Awards in the field, and the prestigious CAREER Award from the U.S. National Science Foundation. He has served as a principal investigator on several large research projects, as well as serving as an editor for top academic journals in the field.




朱小果获得博士学位。来自斯坦福大学，目前是加州大学圣地亚哥分校拉迪管理学院创新与技术教授。他的研究重点是全球环境中技术驱动的创新、IT 对公司/行业的经济影响、数据分析、IT 驱动的供应链以及软件、媒体和电信行业的竞争。他的研究成果发表在《管理科学》、《信息系统研究》、《MIS Quarterly》、《营销科学》等顶级学术期刊上。他的工作在 Google Scholar 中被引用超过 7300 次，并获得了该领域的多项最佳论文奖以及美国国家科学基金会颁发的著名的职业奖。他曾担任多个大型研究项目的首席研究员，并担任该领域顶级学术期刊的编辑。


# ENGAGING VOLUNTARY CONTRIBUTIONS IN ONLINECOMMUNITIES: A HIDDEN MARKOV MODEL




# 在在线社区中进行自愿贡献：隐马尔可夫模型


Wei Chen




陈伟


Eller College of Management, University of Arizona, Tucson, AZ 85721 U.S.A. {weichen@email.arizona.edu}




亚利桑那大学埃勒管理学院，图森，AZ 85721 美国 {weichen@email.arizona.edu}


Xiahua Wei




魏夏华


School of Business, University of Washington, Bothell, WA 98011 U.S.A. {xhwei@uw.edu}




华盛顿大学商学院，Bothell, WA 98011 U.S.A. {xhwei@uw.edu}


Kevin Xiaoguo Zhu




朱小国


Rady School of Management, University of California, San Diego, CA 92093-0553 U.S.A. {kxzhu@ucsd.edu}




加州大学拉迪管理学院，圣地亚哥，CA 92093-0553 U.S.A. {kxzhu@ucsd.edu}


## Appendix A




## 附录 A


## The MCMC Estimation of the HMM




## HMM 的 MCMC 估计


We estimate the parameters vector $\big \{ \theta , \widetilde { S } \big \}$ with Gibbs sampling (Albert and Chib 1993). Suppose we have motivation state $s _ { i t } \in \{ 1 , 2 , . . . ,$ $J _ { \it { \Psi } }$ in our model. We generate the joint posterior distribution by sampling from each conditional distribution of the following parameter blocks:




我们用吉布斯采样估计参数向量 $\big \{ \theta , \widetilde { S } \big \}$ (Albert and Chib 1993)。假设我们有动机状态 $s _ { i t } \in \{ 1 , 2 , . 。 。 ,$ $J _ { \it { \Psi } }$ 在我们的模型中。我们通过从以下参数块的每个条件分布中采样来生成联合后验分布：


$$
\begin{array}{l} \boldsymbol {\theta} = (\theta_ {1}, \theta_ {2} ^ {\prime}, \theta_ {3} ^ {\prime}, \theta_ {4} ^ {\prime}, \theta_ {5} ^ {\prime}) ^ {\prime} \\ \theta_ {1} = \sigma^ {2} \\ \theta_ {2} = (\beta_ {1}, \beta_ {2} ^ {\prime}, \dots , \beta_ {J} ^ {\prime}) ^ {\prime} \\ \theta_ {3} = (\xi_ {1}, \xi_ {2} ^ {\prime}, \dots , \xi_ {J} ^ {\prime}) ^ {\prime} \\ \theta_ {4} = (\mu_ {2}, \mu_ {3}, \dots , \mu_ {J - 1}) ^ {\prime} \\ \theta_ {5} = (L _ {i 1}, L _ {i 2}, \dots , L _ {i T}) ^ {\prime}, i = 1, \dots , n \\ \theta_ {6} = (s _ {i 1}, s _ {i 2}, \dots , s _ {i T}) ^ {\prime}, i = 1, \dots , n \end{array}
$$




$$
\begin{array}{l} \boldsymbol {\theta} = (\theta_ {1}, \theta_ {2} ^ {\prime}, \theta_ {3} ^ {\prime}, \theta_ {4} ^ {\prime}, \theta_ {5} ^ {\prime}) ^ {\prime} \\ \theta_ {1} = \sigma^ {2} \\ \theta_ {2} = (\beta_ {1}, \beta_ {2} ^ {\prime}, \dots , \beta_ {J} ^ {\prime}) ^ {\prime} \\ \theta_ {3} = (\xi_ {1}, \xi_ {2} ^ {\prime}, \dots , \xi_ {J} ^ {\prime}) \\ ^ {\prime} \theta_ {4} = (\mu_ {2}, \mu_ {3}, \dots , \mu_ {J - 1}) ^ {\prime} \\ \theta_ {5} = (L _ {i 1}, L _ {i 2}, \dots , L _ {i T}) ^ {\prime}, i = 1, \dots , n \\ \theta_ {6} = (s _ {i 1}, s _ {i 2}, \dots , s _ {i T}) ^ {\prime}, i = 1, \dots , n \end{array}
$$


For the simplicity of presentation, we denote $\theta _ { - i } = ( \theta _ { \mathrm { i } } ^ { \prime } ) ^ { \prime } , \forall j \neq i$ below.




为了简单起见，我们在下面表示 $\theta _ { - i } = ( \theta _ { \mathrm { i } } ^ { \prime } ) ^ { \prime } , \forall j \neq i$ 。


(1) Sample $\theta _ { 1 } = \sigma ^ { - 2 }$ from $\mathrm { P } ( \theta _ { 1 } | \theta _ { - 1 } , Y , X , W )$




(1) 样本 $\theta _ { 1 } = \sigma ^ { - 2 }$ 来自 $\mathrm { P } ( \theta _ { 1 } | \theta _ { - 1 } , Y , X , W )$


Prior: $\sigma ^ { - 2 } \sim \Gamma ( \alpha , \delta )$ . Conditional on $\theta _ { - 1 } , Y , X ,$ and $W ,$ it is equivalent to observing $\left\{ \varepsilon _ { i t } \right\}$ where $\varepsilon _ { i t } = Y _ { i t } - X _ { i t } \beta _ { s _ { i t } }$




先验： $\sigma ^ { - 2 } \sim \Gamma ( \alpha , \delta )$ 。以 $\theta _ { - 1 } 、 Y 、 X 、$ 和 $W ,$ 为条件，相当于观察 $\left\{ \varepsilon _ { i t } \right\}$ where $\varepsilon _ { i t } = Y _ { i t } - X _ { i t } \beta _ { s _ { i t } }$


Posterior: $( \sigma ^ { - 2 } | \theta _ { - 1 } , Y , X , W ) \sim \Gamma ( \alpha + { \mathrm { \small { ~ \frac { 1 } { 2 } ~ } } } n T , \delta + { \mathrm { \small { ~ \frac { 1 } { 2 } ~ } } } S S R )$ , where $S S R = { \sum } ^ { n } { \sum } ^ { T } { \varepsilon } _ { i t } ^ { 2 }$




后验： $( \sigma ^ { - 2 } | \theta _ { - 1 } , Y , X , W ) \sim \Gamma ( \alpha + { \mathrm { \small { ~ \frac { 1 } { 2 } ~ } } } n T , \delta + { \mathrm { \small { ~ \frac { 1 } { 2 } ~ } } } S S R )$ ，其中 $S S R = { \sum } ^ { n } { \sum } ^ { T } { \varepsilon } _ { i t } ^ { 2 }$


(2) Sample $\theta _ { 2 } = ( \beta _ { 1 } , \beta _ { 2 } ^ { \prime } , . . . , \beta _ { \mathrm { i } } ^ { \prime } ) ^ { \prime }$ from $P ( \theta _ { 2 } | \theta _ { - 2 } , Y , X , W )$




(2) 样本 $\theta _ { 2 } = ( \beta _ { 1 } , \beta _ { 2 } ^ { \prime } , ..., \beta _ { \mathrm { i } } ^ { \prime } ) ^ { \prime }$ from $P ( \theta _ { 2 } | \theta _ { - 2 } , Y、X、W)$


Prior: $( \beta _ { 1 } | \sigma ^ { - 2 } ) \sim N ( m _ { j } , M _ { j } ) , j = 1 , . . . , J$ (independent of each other)




先验： $( \beta _ { 1 } | \sigma ^ { - 2 } ) \sim N ( m _ { j } , M _ { j } ) , j = 1 , . 。 。 , J$ (彼此独立)


Posterior: Conditional on $\left\{ s _ { i t } \right\}$ , only those observations for which $s _ { i t } = j$ are relevant to posterior distribution of $\dot { \cdot } \beta _ { j } \colon ( \beta _ { j } | \theta _ { - 2 } , Y , X , W ) \sim N ( m _ { j } ^ { * }$ $\boldsymbol { M } _ { j } ^ { * } )$ , where




后验：以 $\left\{ s _ { i t } \right\}$ 为条件，仅那些 $s _ { i t } = j$ 的观测值与 $\dot { \cdot } \beta _ { j } \colon ( \beta _ { j } | \theta _ { - 2 } , Y , X , W ) \sim N ( m _ { j } ) 的后验分布相关^ { * }$ $\boldsymbol { M } _ { j } ^ { * } )$ ，其中


$$
* M _ {j} ^ {*} = \left(M _ {j} ^ {- 1} + \sigma^ {- 2} \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} X _ {i t} X _ {i t} ^ {\prime} 1 _ {\{s _ {i t} = j \}}\right) ^ {- 1}
$$




$$
* M _ {j} ^ {*} = \left(M _ {j} ^ {- 1} + \sigma^ {- 2} \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} X _ {i t} X _ {i t} ^ {\prime} 1 _ {\{s _ {i t} = j \}}\right) ^ {- 1}
$$


and




和


$$
m _ {j} ^ {*} = M _ {j} ^ {*} \left(M _ {j} ^ {- 1} m _ {j} + \sigma^ {- 2} \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} X _ {i t} Y _ {i t} 1 _ {\{s _ {i t} = j \}}\right)
$$




$$
m _ {j} ^ {*} = M _ {j} ^ {*} \left(M _ {j} ^ {- 1} m _ {j} + \sigma^ {- 2} \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} X _ {i t} Y _ {i t} 1 _ {\{s _ {i t} = j \}}\右）
$$


(3) Sample $\theta _ { 3 } = \left( \xi _ { 1 } ^ { \prime } , \xi _ { 2 } ^ { \prime } , \dots , \xi _ { I } ^ { \prime } \right) ^ { \prime }$ from $P ( \theta _ { 3 } | \theta _ { - 3 } , Y , X , W )$




(3) 样本 $\theta _ { 3 } = \left( \xi _ { 1 } ^ { \prime } , \xi _ { 2 } ^ { \prime } , \dots , \xi _ { I } ^ { \prime } \right) ^ { \prime }$ from $P ( \theta _ { 3 } | \theta _ { - 3 } , Y , X , W )$


:Prior $\xi _ { j } \sim N ( m w _ { j } , M w _ { j } ) , j = 1 , \ldots , J .$




:先验 $\xi _ { j } \sim N ( m w _ { j } , M w _ { j } ) , j = 1 , \ldots , J .$


Posterior: $\left( \beta _ { \mathrm { j } } \big | \theta _ { - 3 } , Y , X , W \right) { \sim } N ( m w _ { j } ^ { \ast } , M w _ { j } ^ { \ast } )$ , where




后验： $\left( \beta _ { \mathrm { j } } \big | \theta _ { - 3 } , Y , X , W \right) { \sim } N ( m w _ { j } ^ { \ast } , M w _ { j } ^ { \ast } )$ ，其中


$$
M w _ {j} ^ {*} = \left(M w _ {j} ^ {- 1} + \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} W _ {i, t - 1} W _ {i, t - 1} ^ {\prime} 1 _ {\{s _ {i, t - 1} = j \}}\right) ^ {- 1}
$$




$$
M w _ {j} ^ {*} = \left(M w _ {j} ^ {- 1} + \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} W _ {i, t - 1} W _ {i, t - 1} ^ {\prime} 1 _ {\{s _ {i, t - 1} = j \}}\right) ^ {- 1}
$$


and




和


$$
m w _ {j} ^ {*} = M w _ {j} ^ {*} \left(M w _ {j} ^ {- 1} m w _ {j} + \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} W _ {i, t - 1} L _ {i t} 1 _ {\{s _ {i, t - 1} = j \}}\right)
$$




$$
m w _ {j} ^ {*} = M w _ {j} ^ {*} \left(M w _ {j} ^ {- 1} m w _ {j} + \sum_ {i = 1} ^ {n} \sum_ {t = 1} ^ {T} W _ {i, t - 1} L _ {i t} 1 _ {\{s _ {i, t - 1} = j \}}\右）
$$


Note that since $\sigma _ { u } ^ { 2 }$ is not identifiable, we normalize it to 1 in the estimation.




请注意，由于 $\sigma _ { u } ^ { 2 }$ 不可识别，因此我们在估计中将其标准化为 1。


(4) Sample $\theta _ { 4 } = \left( \mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { J - 1 } \right) ^ { \prime }$ from $P ( \theta _ { 4 } | \theta _ { - 4 } , Y , X , W )$ Albert and Chib provide the posterior for $\mu _ { j }$ given the other threshold parameters $\mu _ { k } , k \neq j$ . For each $\mu _ { j } ,$ let $L o w e r =$ $\operatorname* { m a x } \Bigl \{ \operatorname* { m a x } \{ L _ { i t } \colon s _ { i t } = j \} , \mu _ { j - 1 } \Bigr \}$ and $U p p e r = \operatorname* { m i n } \{ \operatorname* { m i n } \{ L _ { i t } \colon s _ { i t } = j + 1 \} , \mu _ { j + 1 } \}$ . Then we can sample $\mu _ { j }$ from the uniform distribution .[ݎ݁݌݌ܷ ,ݎ݁ݓ݋ܮ]ܷ




(4) 样本 $\theta _ { 4 } = \left( \mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { J - 1 } \right) ^ { \prime }$ from $P ( \theta _ { 4 } | \theta _ { - 4 } , Y , X , W )$ Albert 和 Chib 提供后验$\mu _ { j }$ 给定其他阈值参数 $\mu _ { k } , k \neq j$ 。对于每个 $\mu _ { j } ，$ 让 $L o w e r =$ $\operatorname* { m a x } \Bigl \{ \operatorname* { m a x } \{ L _ { i t } \colon s _ { i t } = j \} 、 \mu _ { j - 1 } \Bigr \}$ 和 $U p p e r = \operatorname* { m i n } \{ \operatorname* { m i n } \{ L _ { i t } \colon s _ { i t } = j + 1 \} , \mu _ { j + 1 } \}$ 。然后我们可以从均匀分布 中采样 $\mu _ { j }$ 。


(5) Sample $\theta _ { 5 } = ( L _ { i 1 } , L _ { i 2 } , \dots , L _ { i T } ) ^ { \prime } , i = 1 , \dots , n$ from $P ( \theta _ { 5 } | \theta _ { - 5 } , Y , X , W )$ $L _ { i t }$ determines $s _ { i t }$ according to the following formula: $s _ { i t } = j i f \mu _ { j - 1 } < L _ { i t } < \mu _ { j } ,$ where $\mu _ { 0 } = - \infty , \mu _ { 1 } = 0 , \mu _ { J } = \infty$ , and $\mu _ { 2 } , \ldots , \mu _ { J - 1 }$ are given in step (4). Conditional on $\theta _ { - 5 }$ , we can generate $L _ { i t }$ from a truncated normal distribution $T N _ { ( \mu _ { j - 1 } , \mu _ { j } ) } ( W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } } , 1 )$ ,	which is a normal distribution with mean $W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } }$ and variance 1, and truncated left at $\mu _ { j - 1 }$ and right at $\mu _ { j }$ . Repeating this for $t = 1 , \dots , T$ and $i = 1 , \dots , n$ gives a draw from $P ( \theta _ { 5 } | \theta _ { - 5 } , Y , X , W )$ .




(5) 样本 $\theta _ { 5 } = ( L _ { i 1 } , L _ { i 2 } , \dots , L _ { i T } ) ^ { \prime } , i = 1 , \dots , n$ from $P ( \theta _ { 5 } | \theta _ { - 5 } , Y , X , W )$ $L _ { i t }$ 根据以下公式确定 $s _ { i t }$： $s _ { i t } = j i f \mu _ { j - 1 } < L _ { i t } < \mu _ { j } ,$ 其中 $\mu _ { 0 } = - \infty , \mu _ { 1 } = 0 , \mu _ { J } = \infty$ 和 $\mu _ { 2 } 、 \ldots 、 \mu _ { J - 1 }$ 在步骤（4）中给出。以 $\theta _ { - 5 }$ 为条件，我们可以从截断正态分布 $T N _ { ( \mu _ { j - 1 } , \mu _ { j } ) } ( W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } } , 1 )$ 生成 $L _ { i t }$ ，这是均值 $W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } }$ 和方差为 1 的正态分布，并在 $\mu _ { j - 1 }$ 处向左截断，在 $\mu _ { j }$ 处截断右侧。对 $t = 1 、 \dots 、 T$ 和 $i = 1 、 \dots 、 n$ 重复此操作，得到 $P ( \theta _ { 5 } | \theta _ { - 5 } , Y , X , W )$ 的平局。


Sample) 6( (6) Sample $\theta _ { 6 } = ( s _ { i 1 } , s _ { i 2 } , \ldots , s _ { i T } ) ^ { \prime } , i = 1 , \ldots , n$ from from $P ( \theta _ { 6 } | \theta _ { - 6 } , Y , X , W )$




样本) 6( (6) 样本 $\theta _ { 6 } = ( s _ { i 1 } , s _ { i 2 } , \ldots , s _ { i T } ) ^ { \prime } , i = 1 , \ldots , n$ 来自 $P ( \theta _ { 6 } | \theta _ { - 6 } , Y , X , W )$


We generate the states using the single-move Gibbs-sampling algorithm in Kim and Nelson (1999), which is also the well-known Forward-Backward algorithm. Denoting $\psi _ { i t }$ as information for user ݅ up to time ݐ, and $\psi _ { i T }$ as information from the whole sample, we follow the forward-backward algorithm as below to obtain $P ( s _ { i t } | S _ { i , - t } , \bar { \psi } _ { i T } )$




我们使用 Kim 和 Nelson (1999) 中的单步吉布斯采样算法生成状态，这也是著名的前向-后向算法。将 $\psi _ { i t }$ 表示为用户 x 截至时间 m 的信息，将 $\psi _ { i T }$ 表示为整个样本的信息，我们按照如下的前向-后向算法得到 $P ( s _ { i t } | S _ { i , - t } , \bar { \psi } _ { i T } )$


(a) Forward: Calculate $P ( s _ { i t } | \psi _ { i t } )$




(a) 正向：计算$P ( s _ { i t } | \psi _ { i t } )$


Step 1: Given $P ( s _ { i , t - 1 } = k | \psi _ { i , t - 1 } ) , k = 1 , \ldots , J$ at the beginning of period t, calculate $P \left( s _ { i t } = j , s _ { i , t - 1 } = k \middle | \psi _ { i , t - 1 } \right) =$ $P \big ( s _ { i t } = j \big | s _ { i , t - 1 } = k , \psi _ { i , t - 1 } \big ) P \big ( s _ { i , t - 1 } = j \big | \psi _ { i , t - 1 } \big )$ , where




步骤 1：给定 $P ( s _ { i , t - 1 } = k | \psi _ { i , t - 1 } ) , k = 1 , \ldots , J$ 在周期 t 开始时，计算 $P \left( s _ { i t } = j , s _ { i , t - 1 } = k \middle | \psi _ { i , t - 1 } \right) =$ $P \big ( s _ { i t } = j \big | s _ { i , t - 1 } = k , \psi _ { i , t - 1 } \big ) P \big ( s _ { i , t - 1 } = j \big | \psi _ { i , t - 1 } \big )$ ，其中


$$
P \big (s _ {i t} = j \big | s _ {i, t - 1} = k, \Psi_ {i, t - 1} \big) = \left\{ \begin{array}{c c} \Phi \big (\mu_ {1} - W _ {i, t - 1} \xi_ {k} \big), & i f j = 1 \\ \Phi \big (\mu_ {j} - W _ {i, t - 1} \xi_ {k} \big) - \Phi \big (\mu_ {j - 1} - W _ {i, t - 1} \xi_ {k} \big), & i f j = 2, \ldots , J - 1 \\ 1 - \Phi \big (\mu_ {j - 1} - W _ {i, t - 1} \xi_ {j} \big), & i f j = J \end{array} \right.
$$




$$
P \big (s _ {i t} = j \big | s _ {i, t - 1} = k, \Psi_ {i, t - 1} \big) = \left\{ \begin{array}{c c} \Phi \big (\mu_ {1} - W _ {i, t - 1} \xi_ {k} \big), & i f j = 1 \\ \Phi \big (\mu_ {j} - W _ {i, t - 1} \xi_ {k} \big) - \Phi \big (\mu_ {j - 1} - W _ {i, t - 1} \xi_ {k} \big), & if j = 2, \ldots , J - 1 \\ 1 - \Phi \big (\mu_ {j - 1} - W _ {i, t - 1} \xi_ {j} \big), & i f j = J \end{array} \right。
$$


For the first period, we use the initial probability $P ( s _ { i 1 } = j ) = p _ { j } { \mathrm { ~ f o r ~ } } j = 1 , \ldots , J { \mathrm { ~ } }$ which are sampled from a Dirichlet distribution.




对于第一个周期，我们使用从狄利克雷分布中采样的初始概率 $P ( s _ { i 1 } = j ) = p _ { j } { \mathrm { ~ for or ~ } } j = 1 , \ldots , J { \mathrm { ~ } }$ 。


Step 2: Once $X _ { i t }$ and $Y _ { i t }$ are observed in period ݐ, we update the probability term by calculating $\begin{array} { r } { P ( s _ { i t } = j | \psi _ { i t } ) = } \end{array}$ $\begin{array} { r } { \sum _ { k = 1 } ^ { J } P ( s _ { i t } = j , s _ { i , t - 1 } = k | \psi _ { i t } ) } \end{array}$ , where




步骤 2：一旦在周期 p 内观察到 $X _ { i t }$ 和 $Y _ { i t }$，我们通过计算 $\begin{array} { r } { P ( s _ { i t } = j | \psi _ { i t } ) = } \end{array}$ $\begin{array} { r } { \sum _ { k = 1 } ^ { 来更新概率项J } P ( s _ { i t } = j , s _ { i , t - 1 } = k | \psi _ { i t } ) } \end{array}$ ，其中


$$
\begin{array}{r l} & P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i t} \big) \\ & \quad = P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i, t - 1}, X _ {i t}, Y _ {i t} \big) \\ & \quad = \frac {f \big (Y _ {i t} | s _ {i t} = j , s _ {i , t - 1} = k , \Psi_ {i , t - 1} , X _ {i t} \big) P \big (s _ {i t} = j , s _ {i , t - 1} = k \mid \Psi_ {i , t - 1} \big)}{f \big (Y _ {i t} | \Psi_ {i , t - 1} , X _ {i t} \big)} \\ & \quad \propto f (Y _ {i t} | s _ {i t} = j, X _ {i t}) P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i, t - 1} \big) \end{array}
$$




$$
\begin{array}{r l} & P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i t} \big) \\ & \quad = P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i, t - 1}, X _ {i t}, Y _ {i t} \big) \\ & \quad = \frac {f \big (Y _ {i t} | s _ {i t} = j , s _ {i , t - 1} = k , \Psi_ {i , t - 1} , X _ {i t} \big) P \big (s _ {i t} = j , s _ {i , t - 1} = k \mid \Psi_ {i , t - 1} \big)}{f \big (Y _ {i t} | \Psi_ {i , t - 1} , X _ {i t} \big)} \\ & \quad \propto f (Y _ {i t} | s _ {i t} = j, X _ {i t}) P \big (s _ {i t} = j, s _ {i, t - 1} = k \mid \Psi_ {i, t - 1} \big) \end{array}
$$


(b) Backward: In the backward process, we generate $s _ { i t }$ conditioning on $\psi _ { i t }$ and $s _ { i , t + 1 } \left( t = T - 1 , T - 2 , \dots , 1 \right)$ ( using $g ( s _ { i t } | \psi _ { i t } , s _ { i , t + 1 } ) \propto$ $g \big ( s _ { i , t + 1 } \big | s _ { i t } , \psi _ { i t } \big ) g ( s _ { i t } | \psi _ { i t } )$ . We then can calculate




(b) 向后：在向后过程中，我们在 $\psi _ { i t }$ 和 $s _ { i , t + 1 } \left( t = T - 1 , T - 2 , \dots , 1 \right)$ 上生成 $s _ { i t }$ 条件（使用 $g ( s _ { i t } | \psi _ { i t } , s _ { i ） , t + 1 } ) \propto$ $g \big ( s _ { i , t + 1 } \big | s _ { i t } , \psi _ { i t } \big ) g ( s _ { i t } | \psi _ { i t } )$ 然后我们可以计算。


$$
P \big (s _ {i t} = j \big | s _ {i, t + 1}, \Psi_ {i t} \big) = \frac {g \big (s _ {i , t + 1} \big | s _ {i t} = j , \Psi_ {i t} \big) g (s _ {i t} = j | \Psi_ {i t})}{\sum_ {k = 1} ^ {J} g \big (s _ {i , t + 1} \big | s _ {i t} = k , \Psi_ {i t} \big) g (s _ {i t} = k | \Psi_ {i t})}
$$




$$
P \big (s _ {i t} = j \big | s _ {i, t + 1}, \Psi_ {i t} \big) = \frac {g \big (s _ {i , t + 1} \big | s _ {i t} = j , \Psi_ {i t} \big) g (s _ {i t} = j | \Psi_ {i t})}{\sum_ {k = 1} ^ {J} g \big (s _ {i , t + 1} \big | s _ {i t} = k , \Psi_ {i t} \big) g (s _ {i t} = k | \Psi_ {i t})}
$$


Then we can use a random number drawn from a uniform distribution to generate $s _ { i t }$ according to $P ( s _ { i t } | S _ { i , - t } , \varPsi _ { i T } )$




然后我们可以使用从均匀分布中抽取的随机数根据 $P ( s _ { i t } | S _ { i , - t } , \varPsi _ { i T } )$ 生成 $s _ { i t }$


## Appendix B




## 附录 B


## Log-Likelihood and Model Selection Criteria




## 对数似然和模型选择标准


As detailed in Appendix A, we estimate the parameters in our HMM with Bayesian estimation, which does not require us to calculate the likelihood. However, to select the number of states, the selection criteria would rely on the likelihood. Therefore, we describe the calculation of the likelihood of an observed sequence of contributions and the selection criteria below.




如附录 A 中详述，我们使用贝叶斯估计来估计 HMM 中的参数，这不需要我们计算可能性。然而，为了选择状态的数量，选择标准将依赖于可能性。因此，我们在下面描述了观察到的贡献序列的可能性的计算和选择标准。


## Log-Likelihood Calculation




## 对数似然计算


Because we adopt a hidden Markov model, the contribution probabilities for each individual over time are correlated through the hidden states. The joint likelihood of each individual’s contribution sequence has to consider the possible paths of the underlying states (Netzer et al. 2008). Suppose that there are ܬ possible states. Then according to MacDonald and Zucchini (1997), we can write the joint probability using a matrix product as




因为我们采用隐马尔可夫模型，所以每个个体随时间的贡献概率通过隐藏状态相关。每个个体贡献序列的联合似然必须考虑潜在状态的可能路径（Netzer et al. 2008）。假设有 可能的状态。然后根据 MacDonald 和 Zucchini (1997)，我们可以使用矩阵乘积将联合概率写为


$$
P _ {i} (Y _ {i 1} = y _ {i 1}, \dots , Y _ {i T} = y _ {i T}) = P _ {0} \Omega_ {i} (1) Q _ {i} (1, 2) \Omega_ {i} (2) \dots Q _ {i} (T - 1, T) \Omega_ {i} (T) \mathbf {1} ^ {\prime}
$$




$$
P _ {i} (Y _ {i 1} = y _ {i 1}, \dots , Y _ {i T} = y _ {i T}) = P _ {0} \Omega_ {i} (1) Q _ {i} (1, 2) \Omega_ {i} (2) \dots Q _ {i} (T - 1, T) \Omega_ {i} (T) \mathbf {1} ^ {\prime}
$$


where $P _ { 0 }$ is the initial probability, $\varOmega _ { i } ( t )$ ( is ${ \mathrm { a } } J \times J$ diagonal matrix with the elements of emission probability $\omega _ { i t | j } = f ( Y _ { i t } | X _ { i t } , s _ { i t } = j ; \pmb { \beta } , \sigma ^ { 2 } )$ on the diagonal, $Q _ { i } ( t - 1 , t )$ is the $J \times J$ transition matrix for individual ݅ at time ݐ with the elements of $q _ { i } ( k , j ) =$ $f \big ( s _ { i t } = j \big | W _ { i , t - 1 } , s _ { i , t - 1 } = k ; \xi \big )$ on the $k ^ { t h }$ row and $j ^ { t h }$ column, and $\mathbf { 1 ^ { \prime } }$ is ${ \mathrm { ~ a ~ } } J \times 1$ vector of ones. The element probabilities are obtained according to our model setup:




其中 $P _ { 0 }$ 是初始概率， $\varOmega _ { i } ( t )$ ( 是 ${ \mathrm { a } } J \times J$ 对角矩阵，其元素为发射概率 $\omega _ { i t | j } = f ( Y _ { i t } | X _ { i t } , s _ { i t } = j ; \pmb { \beta } , \sigma ^ { 2 } )$ 在对角线上，$Q _ { i } ( t - 1 , t )$ 是个体 x 在时刻 g 的 $J \times J$ 转移矩阵，其元素为 $q _ { i } ( k , j ) =$ $f \big ( s _ { i t } = j \big | W _ { i , t - 1 } , s _ { i , t - 1 } = k ; \xi \big )$ 在 $k ^ { t h }$ 行和 $j ^ { t h }$ 列上，而 $\mathbf { 1 ^ { \prime } }$ 是 ${ \mathrm { ~ a ~ } } J \times 1$ 向量。设置：


$$
\omega_ {i t | j} = f (Y _ {i t} | X _ {i t}, s _ {i t} = j; \pmb {\beta}, \sigma^ {2}) = \left\{1 - \Phi \left(\frac {X _ {i t} ^ {\prime} \beta_ {j}}{\sigma}\right) \right\} ^ {1 \{Y _ {i t} = 0 \}} \left\{\frac {1}{\sigma} \phi \left(\frac {Y _ {i t} - X _ {i t} ^ {\prime} \beta_ {j}}{\sigma}\right) \right\} ^ {1 \{Y _ {i t} > 0 \}}
$$




$$
\omega_ {i t | j} = f (Y _ {i t} | X _ {i t}, s _ {i t} = j; \pmb {\beta}, \sigma^ {2}) = \left\{1 - \Phi \left(\frac {X _ {i t} ^ {\prime} \beta_ {j}}{\sigma}\right) \right\} ^ {1 \{Y _ {i t} = 0 \}} \left\{\frac {1}{\sigma} \phi \left(\frac {Y _ {i t} - X _ {i t} ^ {\prime} \beta_ {j}}{\sigma}\right) \right\} ^ {1 \{Y _ {i t} > 0 \}}
$$


and




和


$$
q _ {i} (k, j) = f \big (s _ {i t} = j \big | W _ {i, t - 1}, s _ {i, t - 1} = k; \xi \big) = \Phi \big (\mu_ {j + 1} - W _ {i, t - 1} \xi_ {k} \big) - \Phi \big (\mu_ {j} - W _ {i, t - 1} \xi_ {k} \big)
$$




$$
q _ {i} (k, j) = f \big (s _ {i t} = j \big | W _ {i, t - 1}, s _ {i, t - 1} = k; \xi \big) = \Phi \big (\mu_ {j + 1} - W _ {i, t - 1} \xi_ {k} \big) - \Phi \big (\mu_ {j} - W _ {i, t - 1} \xi_ {k} \big)
$$


Then we can write the log-likelihood as ln $\begin{array} { r } { L = \sum _ { i } \log ( P _ { i } ) } \end{array}$




然后我们可以将对数似然写为 ln $\begin{array} { r } { L = \sum _ { i } \log ( P _ { i } ) } \end{array}$


## Selection Criteria




## 选择标准


We adopt three model selection criteria to determine the number of states in our HMM. First, we use the commonly used Akaike information criterion (AIC) and Bayesian information criterion (BIC) (Singh et al. 2011; Yan and Tan 2014):




我们采用三个模型选择标准来确定 HMM 中的状态数量。首先，我们使用常用的赤池信息准则（AIC）和贝叶斯信息准则（BIC）（Singh et al. 2011；Yan and Tan 2014）：


$$
A I C = - 2 * \ln L + 2 * s i z e
$$




$$
A I C = - 2 * \ln L + 2 * 尺寸
$$


and




和


$$
B I C = - 2 * \ln L + s i z e * \ln N
$$




$$
B I C = - 2 * \ln L + 大小 * \ln N
$$


where size is the number of parameters in the model, and N is the number of users in the sample. Second, realizing that we are using a Bayesian estimation for our HMM, we also adopt Markov switching criterion (MSC), which was developed for HMM’s state and variable selection (Smith et al. 2006). We follow the adaptation in the literature for its formulation (Netzer et al. 2008):




其中 size 是模型中参数的数量，N 是样本中用户的数量。其次，意识到我们对 HMM 使用贝叶斯估计，我们还采用了马尔可夫切换准则 (MSC)，它是为 HMM 的状态和变量选择而开发的 (Smith et al. 2006)。我们遵循文献中的改编来制定其公式（Netzer et al. 2008）：


$$
M S C = - 2 * \ln L + \sum_ {s = 1} ^ {J} \frac {\hat {T} _ {s} (\hat {T} _ {s} + J * K)}{\hat {T} _ {s} - J * K + 2}
$$




$$
M S C = - 2 * \ln L + \sum_ {s = 1} ^ {J} \frac {\hat {T} _ {s} (\hat {T} _ {s} + J * K)}{\hat {T} _ {s} - J * K + 2}
$$


where $\begin{array} { r } { \hat { T } _ { s } = \sum _ { t = 1 } ^ { T } \sum _ { i = 1 } ^ { N _ { t } } P ( s _ { i t } = s ) , J } \end{array}$ is the number of states in the model, and ܭ is the number of covariates in both the transition matrix and the state-dependent vector.




其中 $\begin{array} { r } { \hat { T } _ { s } = \sum _ { t = 1 } ^ { T } \sum _ { i = 1 } ^ { N _ { t } } P ( s _ { i t } = s ) , J } \end{array}$ 是模型中的状态数，而 是模型中的状态数转换矩阵和状态相关向量中的协变量。


## Appendix C




## 附录 C


## Testing the Estimation on Simulated Data




## 测试模拟数据的估计


Because our model has a nonlinear feature by incorporating the Tobit and probit models, we could not use standard statistical software to estimate it. We have to write our own estimation algorithm instead. Hence we did, but we need to ensure that it is correct before applying the algorithm to the actual data. We run the algorithm on simulated data based on known parameters, and test whether it could recover the true parameters. Because there is some model uncertainty on the number of states in our HMM, we also simulate data with $2 , 3$ , and 4 true states, and then estimate the model with 2, 3, and 4 states in HMM. Then we use the model selection criteria to determine whether our algorithm points out the true number of states. Here we use three true states as an example.




由于我们的模型通过结合 Tobit 和 Probit 模型而具有非线性特征，因此我们无法使用标准统计软件来估计它。我们必须编写自己的估计算法。因此我们这样做了，但在将算法应用于实际数据之前，我们需要确保它是正确的。我们在基于已知参数的模拟数据上运行该算法，并测试它是否可以恢复真实参数。因为我们的 HMM 中的状态数量存在一些模型不确定性，所以我们还模拟具有 $2 、 3$ 和 4 个真实状态的数据，然后在 HMM 中估计具有 2、3 和 4 个状态的模型。然后我们使用模型选择标准来确定我们的算法是否指出了真实的状态数。这里我们以三种真实状态为例。


We first generate the true parameters ࣂ, the community and individual characteristics variables $X = \{ X _ { i t } \} _ { t = 1 , \ldots , T ; i = 1 , \ldots , N _ { t } } ,$ , and the community interaction variables $W = \{ W _ { i t } \} _ { t = 1 , \dots , T ; i = 1 , \dots , N _ { t } }$ with three motivation states (ܬ = 3(. Since we assume that a user has an initial probability $P _ { 0 } = \{ p _ { 1 } , p _ { 2 } , p _ { 3 } \}$ , at ݐ = 1 we draw the initial state $s _ { i 1 }$ of user ݅	from a Dirichlet distribution using the initial probability $P _ { 0 }$ for each user ݅ that enters the community. Conditional on $s _ { i 1 }$ , we then draw the contribution $Y _ { i 1 } = \operatorname* { m a x } ( 0 , Y _ { i 1 } ^ { * } )$ , where $\bar { Y _ { i 1 } ^ { * } } = X _ { i t } \beta _ { s _ { i 1 } } \bar { + } ~ \varepsilon _ { i 1 }$ and $\varepsilon _ { i 1 }$ is generated from a normal distribution with mean 0 and variance $\sigma ^ { 2 } .$ For any $t > I _ { ; }$ , we first draw $L _ { i t } = W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } } + u _ { i t } ,$ where $u _ { i t }$ is drawn from $N ( 0 , 1 )$ . Then we generate the new state $s _ { i t }$ according to $L _ { i t }$ . Repeating the same process, we generate $Y = \{ Y _ { i t } \} _ { t = 2 , \dots , T ; i = 1 , \dots , N _ { t } }$ for all .ݐ




我们首先生成真实参数ࣂ，社区和个体特征变量$X = \{ X _ { i t } \} _ { t = 1 , \dots , T ; i = 1 , \ldots , N _ { t } } ,$ ，以及社区互动变量 $W = \{ W _ { i t } \} _ { t = 1 , \dots , T ; i = 1 , \dots , N _ { t } }$ 具有三种动机状态 ( ^ = 3( 。由于我们假设用户有一个初始概率 $P _ { 0 } = \{ p _ { 1 } , p _ { 2 } , p _ { 3 } \}$ ，在 p = 1 时，我们绘制用户 p 的初始状态 $s _ { i 1 }$根据进入社区的每个用户 p 的初始概率 $P _ { 0 }$ 的狄利克雷分布，以 $s _ { i 1 }$ 为条件，然后得出贡献 $Y _ { i 1 } = \operatorname* { m a x } ( 0 , Y _ { i 1 } ^ { * } )$ ，其中 $\bar { Y _ { i 1 } ^ { * } } = X _ { i t } \beta _ { s _ { i 1 } } \bar { + } ~ \varepsilon _ { i 1 }$ 和 $\varepsilon _ { i 1 }$ 是根据均值为 0 和方差 $\sigma ^ { 2 } .$ 的正态分布生成的，对于任何 $t > I _ { ; }$ ，我们首先绘制 $L _ { i t } = W _ { i , t - 1 } \xi _ { s _ { i , t - 1 } } + u _ { i t } ,$ 其中 $u _ { i t }$ 是从 $N ( 0 , 1 )$ 中得出的，然后我们根据 $L _ { i t }$ 生成新状态 $s _ { i t }$ 。重复相同的过程，我们为所有 .p 生成 $Y = \{ Y _ { i t } \} _ { t = 2 , \dots , T ; i = 1 , \dots , N _ { t } }$


With the simulation data {X, W, Y}, we estimate the model with our procedure and present the results in Table C1. Our simulation data contains 322 individuals and 20 periods of time. The true number of states is ܬ = 3. The community and individual characteristics vector X contains four variables, and the community interaction vector W contains four variables. In Table C1, the “True Parameters” panel on the left displays the original parameters $\theta = \{ \beta , \xi , \sigma ^ { 2 } \}$ that we employ to generate the simulation data. The “Estimation” column on the right displays the estimated parameters. Our estimation recovers the true parameters accurately.




利用模拟数据 {X, W, Y}，我们用我们的程序估计模型并将结果显示在表 C1 中。我们的模拟数据包含 322 个人和 20 个时间段。真实的状态数为 ≤ 3。社区和个体特征向量 X 包含四个变量，社区交互向量 W 包含四个变量。在表 C1 中，左侧的“真实参数”面板显示了我们用来生成模拟数据的原始参数 $\theta = \{ \beta , \xi , \sigma ^ { 2 } \}$ 。右侧的“估计”栏显示估计的参数。我们的估计准确地恢复了真实参数。


We also present the model selection criteria in Table C2. Given the true state number is three, all our model selection criteria indicate that our HMM model with three states fit the data the best. This confirms the reliability of the estimation algorithm, and gives us confidence in its empirical application to the actual data.




我们还在表 C2 中列出了模型选择标准。鉴于真实状态数为 3，我们所有的模型选择标准都表明我们的具有三种状态的 HMM 模型最适合数据。这证实了估计算法的可靠性，并让我们对其在实际数据中的经验应用充满信心。


<table><tr><td colspan="7">Table C1. Estimation Results from Simulation Data (Number of States = 3)</td></tr><tr><td></td><td colspan="3">True Parameters</td><td colspan="3">Estimation</td></tr><tr><td>Variables</td><td>State 1</td><td>State 2</td><td>State 3</td><td>State 1</td><td>State 2</td><td>State 3</td></tr><tr><td> $\beta$ </td><td></td><td></td><td></td><td colspan="3">Mean (Standard Deviation)</td></tr><tr><td> $x_1$ </td><td>3</td><td>5</td><td>7</td><td>2.98 (0.07)</td><td>4.99 (0.07)</td><td>6.99 (0.03)</td></tr><tr><td> $x_2$ </td><td>4</td><td>6</td><td>8</td><td>4.00 (0.02)</td><td>6.02 (0.01)</td><td>8.01 (0.01)</td></tr><tr><td> $x_3$ </td><td>5</td><td>7</td><td>9</td><td>4.99 (0.02)</td><td>7.00 (0.02)</td><td>8.98 (0.01)</td></tr><tr><td> $x_4$ </td><td>6</td><td>8</td><td>10</td><td>6.00 (0.02)</td><td>8.00 (0.01)</td><td>10.01 (0.01)</td></tr><tr><td> $\sigma^2$ </td><td colspan="3">1.5</td><td colspan="3">1.53 (0.03)</td></tr><tr><td> $\xi$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $w_1$ </td><td>-1.5</td><td>-0.5</td><td>0.5</td><td>-1.63 (0.13)</td><td>-0.48 (0.08)</td><td>0.42 (0.06)</td></tr><tr><td> $w_2$ </td><td>1.15</td><td>0.37</td><td>2.53</td><td>1.18 (0.11)</td><td>0.27 (0.08)</td><td>2.57 (0.14)</td></tr><tr><td> $w_3$ </td><td>6.32</td><td>4.48</td><td>7.35</td><td>6.53 (0.29)</td><td>4.41 (0.22)</td><td>7.67 (0.44)</td></tr><tr><td> $w_4$ </td><td>2.65</td><td>3.05</td><td>6.96</td><td>2.73 (0.15)</td><td>3.10 (0.12)</td><td>7.04 (0.17)</td></tr><tr><td> $μ_j$ </td><td></td><td>2</td><td></td><td></td><td>1.95 (0.04)</td><td></td></tr><tr><td> $σ_u^2$ </td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td> $P_0=\{p_j\}$ </td><td>0.45</td><td>0.40</td><td>0.15</td><td>0.44 (0.02)</td><td>0.41 (0.03)</td><td>0.15 (0.020)</td></tr><tr><td>T=20</td><td>N=322</td><td>Draws=2,000</td><td></td><td></td><td></td><td></td></tr></table>




<table><tr><td colspan="7">表 C1。仿真数据的估计结果（状态数 = 3）</td></tr><tr><td></td><td colspan="3">真实参数</td><td colspan="3">估计</td></tr><tr><td>变量</td><td>状态 1</td><td>状态 2</td><td>状态3</td><td>状态 1</td><td>状态 2</td><td>状态 3</td></tr><tr><td> $\beta$ </td><td></td><td></td><td></td><td colspan="3">平均值（标准偏差）</td></tr><tr><td> $x_1$ </td><td>3</td><td>5</td><td>7</td><td>2.98 (0.07)</td><td>4.99 (0.07)</td><td>6.99 (0.03)</td></tr><tr><td> $x_2$ </td><td>4</td><td>6</td><td>8</td><td>4.00 (0.02)</td><td>6.02 (0.01)</td><td>8.01 (0.01)</td></tr><tr><td> $x_3$ </td><td>5</td><td>7</td><td>9</td><td>4.99 (0.02)</td><td>7.00 (0.02)</td><td>8.98 (0.01)</td></tr><tr><td> $x_4$ </td><td>6</td><td>8</td><td>10</td><td>6.00 (0.02)</td><td>8.00 (0.01)</td><td>10.01 (0.01)</td></tr><tr><td> $\sigma^2$ </td><td colspan="3">1.5</td><td colspan="3">1.53 (0.03)</td></tr><tr><td> $\xi$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $w_1$ </td><td>-1.5</td><td>-0.5</td><td>0.5</td><td>-1.63 (0.13)</td><td>-0.48 (0.08)</td><td>0.42 (0.06)</td></tr><tr><td> $w_2$ </td><td>1.15</td><td>0.37</td><td>2.53</td><td>1.18 (0.11)</td><td>0.27 (0.08)</td><td>2.57 (0.14)</td></tr><tr><td> $w_3$ </td><td>6.32</td><td>4.48</td><td>7.35</td><td>6.53 (0.29)</td><td>4.41 (0.22)</td><td>7.67 (0.44)</td></tr><tr><td> $w_4$ </td><td>2.65</td><td>3.05</td><td>6.96</td><td>2.73 (0.15)</td><td>3.10 (0.12)</td><td>7.04 (0.17)</td></tr><tr><td> $μ_j$ </td><td></td><td>2</td><td></td><td></td><td>1.95 (0.04)</td><td></td></tr><tr><td> $σ_u^2$ </td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td> $P_0=\{p_j\}$ </td><td>0.45</td><td>0.40</td><td>0.15</td><td>0.44 (0.02)</td><td>0.41 (0.03)</td><td>0.15 (0.020)</td></tr><tr><td>T=20</td><td>N=322</td><td>抽奖=2,000</td><td></td><td></td><td></td><td></td></tr></table>


<table><tr><td colspan="6">Table C2. Selection of Number of States from Simulation Data (Number of States = 3)</td></tr><tr><td>Number of States</td><td>- 2*Log-likelihood</td><td>AIC</td><td>BIC</td><td>MSC</td><td>Number of Variables</td></tr><tr><td>2</td><td>35404.87</td><td>35442.87</td><td>35514.59</td><td>41380.24</td><td>19</td></tr><tr><td>3</td><td>22700.68</td><td>22758.68</td><td>22868.14</td><td>22700.68</td><td>29</td></tr><tr><td>4</td><td>22734.37</td><td>22812.37</td><td>22959.57</td><td>30211.52</td><td>39</td></tr></table>




<table><tr><td colspan="6">表 C2。从仿真数据中选择状态数（状态数 = 3）</td></tr><tr><td>状态数</td><td>- 2*对数似然</td><td>AIC</td><td>BIC</td><td>MSC</td><td>状态数变量</td></tr><tr><td>2</td><td>35404.87</td><td>35442.87</td><td>35514.59< /td><td>41380.24</td><td>19</td></tr><tr><td>3</td><td>22700.68</td><td>22758.68 </td><td>22868.14</td><td>22700.68</td><td>29</td></tr><tr><td>4</td><td>22734.3 7</td><td>22812.37</td><td>22959.57</td><td>30211.52</td><td>39</td></tr></table>


## Appendix D




## 附录 D


## Robustness Checks




## 稳健性检查


We conduct several sets of robustness checks. First, we estimate the model on another sample period (301-500 days). The results are in Table D1. Second, we examine whether the moderator role of a user or new questions by the moderators in the community would affect the transition probability of a user. We control for these two factors separately in $W _ { i t } ,$ , and present the results in Table D2 and Table D3, respectively. Finally, we estimate the model on weekly data and include the results in Table D4.




我们进行了几组稳健性检查。首先，我们在另一个样本周期（301-500 天）上估计模型。结果见表D1。其次，我们检查用户的版主角色或社区中版主的新问题是否会影响用户的转换概率。我们在 $W _ { i t } ,$ 中分别控制这两个因素，并将结果分别呈现在表 D2 和表 D3 中。最后，我们根据每周数据估计模型并将结果包含在表 D4 中。


Table D1. Results of HMM on Daily Data for Day 301-500 Subsample




表 D1。第 301-500 天子样本每日数据的 HMM 结果


<table><tr><td>Variable Name</td><td>State 1(Low Motivation)</td><td>State 2(Medium Motivation)</td><td>State 3(High Motivation)</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^x$ </td><td>-2.791*** (0.071)</td><td>-0.103 (0.091)</td><td>4.735*** (0.330)</td></tr><tr><td>Matched_tags $_{it}$ </td><td>0.015*** (0.001)</td><td>0.029*** (0.001)</td><td>0.046*** (0.002)</td></tr><tr><td>Group_size $_t$ </td><td>0.001*** (0.000)</td><td>0.006*** (0.000)</td><td>0.013*** (0.002)</td></tr><tr><td>Tenure $_{it}$ </td><td>-0.001*** (0.000)</td><td>-0.004*** (0.000)</td><td>-0.01*** (0.001)</td></tr><tr><td>Total_answers $_{i,t-1}$ </td><td>0.0002*** (0.000)</td><td>-0.0003*** (0.000)</td><td>-0.001*** (0.000)</td></tr><tr><td> $σ^2$ </td><td colspan="3">1.009*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ξ - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^w$ </td><td>-1.752*** (0.035)</td><td>-0.644*** (0.043)</td><td>0.941*** (0.114)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.268*** (0.019)</td><td>0.049* (0.026)</td><td>-0.117 (0.077)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.262*** (0.020)</td><td>0.117*** (0.014)</td><td>0.021 (0.028)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.562*** (0.037)</td><td>0.300*** (0.024)</td><td>0.084** (0.035)</td></tr><tr><td>Badges $_{i,t-1}$ </td><td>0.250*** (0.053)</td><td>0.275*** (0.040)</td><td>-0.095* (0.058)</td></tr><tr><td>Initial Probability</td><td>0.797*** (0.017)</td><td>0.186*** (0.016)</td><td>0.017*** (0.004)</td></tr><tr><td colspan="4">*p&lt;0.1, **p&lt;0.05; ***p&lt;0.01.</td></tr></table>




<table><tr><td>变量名称</td><td>状态 1（低动机）</td><td>状态 2（中动机）</td><td>状态 3（高动机）</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - 后验均值（标准）偏差）</td></tr><tr><td> $c^x$ </td><td>-2.791*** (0.071)</td><td>-0.103 (0.091)</td><td>4.735*** (0.330)</td></tr><tr><td>匹配标签 $_{it}$ </td><td>0.015*** (0.001)</td><td>0.029*** (0.001)</td><td>0.046*** (0.002)</td></tr><tr><td>Group_size $_t$ </td><td>0.001*** (0.000)</td><td>0.006*** (0.000)</td><td>0.013*** (0.002)</td></tr><tr><td>任期 $_{it}$ </td><td>-0.001*** (0.000)</td><td>-0.004*** (0.000)</td><td>-0.01*** (0.001)</td></tr><tr><td>总计答案 $_{i,t-1}$ </td><td>0.0002*** (0.000)</td><td>-0.0003*** (0.000)</td><td>-0.001*** (0.000)</td></tr><tr><td> $σ^2$ </td><td colspan="3">1.009*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">Σ - 后验均值（标准偏差）</td></tr><tr><td> $c^w$ </td><td>-1.752*** (0.035)</td><td>-0.644*** (0.043)</td><td>0.941*** (0.114)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.268*** (0.019)</td><td>0.049* (0.026)</td><td>-0.117 (0.077)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.262*** (0.020)</td><td>0.117*** (0.014)</td><td>0.021 (0.028)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.562*** (0.037)</td><td>0.300*** (0.024)</td><td>0.084** (0.035)</td></tr><tr><td>徽章 $_{i,t-1}$ </td><td>0.250*** (0.053)</td><td>0.275*** (0.040)</td><td>-0.095* (0.058)</td></tr><tr><td>初始概率</td><td>0.797*** (0.017)</td><td>0.186*** (0.016)</td><td>0.017*** (0.004)</td></tr><tr><td colspan="4">*p<0.1, **p＜0.05； ***p<0.01。</td></tr></table>


<table><tr><td colspan="4">Table D2. Results of HMM after Controlling Moderator in W</td></tr><tr><td>Variable Name</td><td>State 1(Low Motivation)</td><td>State 2(Medium Motivation)</td><td>State 3(High Motivation)</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^x$ </td><td>-3.075*** (0.069)</td><td>0.325*** (0.087)</td><td>7.054*** (0.330)</td></tr><tr><td>Matched_tags $_{it}$ </td><td>0.015*** (0.001)</td><td>0.023*** (0.001)</td><td>0.030*** (0.001)</td></tr><tr><td>Group_size $_t$ </td><td>0.003*** (0.000)</td><td>0.002*** (0.000)</td><td>-0.010*** (0.002)</td></tr><tr><td>Tenure $_{it}$ </td><td>-0.0004* (0.000)</td><td>-0.006*** (0.000)</td><td>-0.016*** (0.001)</td></tr><tr><td>Total_answers $_{i,t-1}$ </td><td>0.0005*** (0.000)</td><td>0.001*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td> $σ^2$ </td><td colspan="3">1.010*** (0.006)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ξ - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^w$ </td><td>-1.655*** (0.018)</td><td>-0.581*** (0.026)</td><td>1.069*** (0.127)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.214*** (0.017)</td><td>0.021 (0.023)</td><td>0.013 (0.054)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.238*** (0.023)</td><td>0.101*** (0.022)</td><td>0.015 (0.059)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.588*** (0.038)</td><td>0.221*** (0.036)</td><td>0.060 (0.096)</td></tr><tr><td>Badges $_{i,t-1}$ </td><td>0.400*** (0.033)</td><td>0.198*** (0.033)</td><td>0.026 (0.063)</td></tr><tr><td>Moderator $_{i,t-1}$ </td><td>-0.115 (0.086)</td><td>0.284*** (0.089)</td><td>0.803*** (0.145)</td></tr><tr><td>Initial Probability</td><td>0.758*** (0.014)</td><td>0.213*** (0.014)</td><td>0.029*** (0.005)</td></tr><tr><td colspan="4">*p&lt;0.1, **p&lt;0.05; ***p&lt;0.01.</td></tr></table>




<table><tr><td colspan="4">表 D2。 W控制调节器后的HMM结果</td></tr><tr><td>变量名称</td><td>状态1（低动机）</td><td>状态2（中动机）</td><td>状态3（高动机）</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - 后验平均值（标准差）</td></tr><tr><td> $c^x$ </td><td>-3.075*** (0.069)</td><td>0.325*** (0.087)</td><td>7.054*** (0.330)</td></tr><tr><td>匹配_标签 $_{it}$ </td><td>0.015*** (0.001)</td><td>0.023*** (0.001)</td><td>0.030*** (0.001)</td></tr><tr><td>Group_size $_t$ </td><td>0.003*** (0.000)</td><td>0.002*** (0.000)</td><td>-0.010*** (0.002)</td></tr><tr><td>任期 $_{it}$ </td><td>-0.0004* (0.000)</td><td>-0.006*** (0.000)</td><td>-0.016*** (0.001)</td></tr><tr><td>Total_answers $_{i,t-1}$ </td><td>0.0005*** (0.000)</td><td>0.001*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td> $σ^2$ </td><td colspan="3">1.010*** (0.006)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ψ - 后验平均值（标准差）</td></tr><tr><td> $c^w$ </td><td>-1.655*** (0.018)</td><td>-0.581*** (0.026)</td><td>1.069*** (0.127)</td></tr><tr><td>Answers_received $_{i,t-1}$ </td><td>0.214*** (0.017)</td><td>0.021 (0.023)</td><td>0.013 (0.054)</td></tr><tr><td>Upvotes_answer $_{i,t-1}$ </td><td>0.238*** (0.023)</td><td>0.101*** (0.022)</td><td>0.015 (0.059)</td></tr><tr><td>Accepted_answers $_{i,t-1}$ </td><td>0.588*** (0.038)</td><td>0.221*** (0.036)</td><td>0.060 (0.096)</td></tr><tr><td>徽章 $_{i,t-1}$ </td><td>0.400*** (0.033)</td><td>0.198*** (0.033)</td><td>0.026 (0.063)</td></tr><tr><td>主持人 $_{i,t-1}$ </td><td>-0.115 (0.086)</td><td>0.284*** (0.089)</td><td>0.803*** (0.145)</td></tr><tr><td>初始概率</td><td>0.758*** (0.014)</td><td>0.213*** (0.014)</td><td>0.029*** (0.005)</td></tr><tr><td colspan="4">*p<0.1，**p<0.05； ***p<0.01。</td></tr></table>


Table D3. Results of HMM after Controlling New Questions by Moderator in W




表 D3。 W 中主持人控制新问题后的 HMM 结果


<table><tr><td>Variable Name</td><td>State 1 (Low Motivation)</td><td>State 2 (Medium Motivation)</td><td>State 3 (High Motivation)</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^x$ </td><td>-2.990*** (0.080)</td><td>0.364*** (0.079)</td><td>7.368*** (0.365)</td></tr><tr><td>Matched_tagsit</td><td>0.015*** (0.000)</td><td>0.023*** (0.001)</td><td>0.029*** (0.001)</td></tr><tr><td>Group_sizet</td><td>0.002*** (0.001)</td><td>0.002*** (0.000)</td><td>-0.011*** (0.002)</td></tr><tr><td>Tenureit</td><td>-0.0005** (0.000)</td><td>-0.006*** (0.000)</td><td>-0.015*** (0.001)</td></tr><tr><td>Total_answersi,t-1</td><td>0.0005*** (0.000)</td><td>0.001*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td> $\sigma^2$ </td><td colspan="3">1.012*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ξ - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^w$ </td><td>-1.666*** (0.020)</td><td>-0.567*** (0.027)</td><td>1.442*** (0.246)</td></tr><tr><td>Answers_receivedi,t-1</td><td>0.220*** (0.016)</td><td>0.014 (0.023)</td><td>0.003 (0.059)</td></tr><tr><td>Upvotes_answeri,t-1</td><td>0.234*** (0.015)</td><td>0.115*** (0.014)</td><td>0.028 (0.027)</td></tr><tr><td>Accepted_answersi,t-1</td><td>0.592*** (0.035)</td><td>0.253*** (0.026)</td><td>0.075** (0.036)</td></tr><tr><td>Badgesi,t-1</td><td>0.408*** (0.034)</td><td>0.221*** (0.038)</td><td>-0.049 (0.064)</td></tr><tr><td>New_q_moderatorsi,t-1</td><td>-0.002 (0.005)</td><td>-0.003 (0.009)</td><td>0.001 (0.038)</td></tr><tr><td>Initial Probability</td><td>0.758*** (0.016)</td><td>0.214*** (0.015)</td><td>0.028*** (0.005)</td></tr><tr><td colspan="4">*p&lt;0.1, **p&lt;0.05; ***p&lt;0.01.</td></tr></table>




<table><tr><td>变量名称</td><td>状态 1（低动机）</td><td>状态 2（中动机）</td><td>状态 3（高动机）</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - 后验均值（标准）偏差）</td></tr><tr><td> $c^x$ </td><td>-2.990*** (0.080)</td><td>0.364*** (0.079)</td><td>7.368*** (0.365)</td></tr><tr><td>Matched_tagsit</td><td>0.015*** (0.000)</td><td>0.023*** (0.001)</td><td>0.029*** (0.001)</td></tr><tr><td>Group_size</td><td>0.002*** (0.001)</td><td>0.002*** (0.000)</td><td>-0.011*** (0.002)</td></tr><tr><td>终身教职</td><td>-0.0005** (0.000)</td><td>-0.006*** (0.000)</td><td>-0.015*** (0.001)</td></tr><tr><td>Total_answersi,t-1</td><td>0.0005*** (0.000)</td><td>0.001*** (0.000)</td><td>0.003*** (0.000)</td></tr><tr><td> $\sigma^2$ </td><td colspan="3">1.012*** (0.005)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ψ - 后验均值（标准差）</td></tr><tr><td> $c^w$ </td><td>-1.666*** (0.020)</td><td>-0.567*** (0.027)</td><td>1.442*** (0.246)</td></tr><tr><td>Answers_receivedi,t-1</td><td>0.220*** (0.016)</td><td>0.014 (0.023)</td><td>0.003 (0.059)</td></tr><tr><td>Upvotes_answeri,t-1</td><td>0.234*** (0.015)</td><td>0.115*** (0.014)</td><td>0.028 (0.027)</td></tr><tr><td>Accepted_answersi,t-1</td><td>0.592*** (0.035)</td><td>0.253*** (0.026)</td><td>0.075** (0.036)</td></tr><tr><td>巴吉西，t-1</td><td>0.408*** (0.034)</td><td>0.221*** (0.038)</td><td>-0.049 (0.064)</td></tr><tr><td>New_q_moderatorsi,t-1</td><td>-0.002 (0.005)</td><td>-0.003 (0.009)</td><td>0.001 (0.038)</td></tr><tr><td>初始概率</td><td>0.758*** (0.016)</td><td>0.214*** (0.015)</td><td>0.028*** (0.005)</td></tr><tr><td colspan="4">*p<0.1，**p<0.05； ***p<0.01。</td></tr></table>


Table D4. Results of HMM on Weekly Data for Day 101-300 Subsample




表 D4。第 101-300 天子样本每周数据的 HMM 结果


<table><tr><td>Variable Name</td><td>State 1(Low Motivation)</td><td>State 2(Medium Motivation)</td><td>State 3(High Motivation)</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^x$ </td><td>-0.986*** (0.116)</td><td>10.566*** (0.772)</td><td>37.557*** (2.661)</td></tr><tr><td>Matched_tagsit</td><td>0.003*** (0.000)</td><td>0.014*** (0.001)</td><td>0.031*** (0.001)</td></tr><tr><td>Group_sizet</td><td>0.002*** (0.001)</td><td>-0.062*** (0.005)</td><td>-0.213*** (0.016)</td></tr><tr><td>Tenureit</td><td>-0.002*** (0.000)</td><td>-0.029*** (0.001)</td><td>-0.070*** (0.003)</td></tr><tr><td>Total_answersi,t-1</td><td>0.002*** (0.000)</td><td>0.013*** (0.000)</td><td>0.024*** (0.001)</td></tr><tr><td> $σ^2$ </td><td colspan="3">2.028*** (0.030)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ξ - Posterior Mean (Standard Deviation)</td></tr><tr><td> $c^w$ </td><td>-1.835*** (0.043)</td><td>-0.793*** (0.066)</td><td>-0.124*** (0.303)</td></tr><tr><td>Answers_receivedi,t-1</td><td>0.072*** (0.012)</td><td>0.023 (0.015)</td><td>0.021 (0.035)</td></tr><tr><td>Upvotes_answeri,t-1</td><td>0.069*** (0.017)</td><td>0.018 (0.017)</td><td>0.013 (0.027)</td></tr><tr><td>Accepted_answersi,t-1</td><td>0.110*** (0.038)</td><td>0.056*** (0.018)</td><td>0.128 (0.083)</td></tr><tr><td>Badgesi,t-1</td><td>0.183*** (0.033)</td><td>0.144*** (0.036)</td><td>-0.054 (0.044)</td></tr><tr><td>Initial Probability</td><td>0.769*** (0.045)</td><td>0.192*** (0.041)</td><td>0.039*** (0.011)</td></tr><tr><td colspan="4">*p&lt;0.1, **p&lt;0.05; ***p&lt;0.01.</td></tr></table>




<table><tr><td>变量名称</td><td>状态 1（低动机）</td><td>状态 2（中动机）</td><td>状态 3（高动机）</td></tr><tr><td> $X_{it}$ </td><td colspan="3">β - 后验均值（标准）偏差）</td></tr><tr><td> $c^x$ </td><td>-0.986*** (0.116)</td><td>10.566*** (0.772)</td><td>37.557*** (2.661)</td></tr><tr><td>Matched_tagsit</td><td>0.003*** (0.000)</td><td>0.014*** (0.001)</td><td>0.031*** (0.001)</td></tr><tr><td>Group_size</td><td>0.002*** (0.001)</td><td>-0.062*** (0.005)</td><td>-0.213*** (0.016)</td></tr><tr><td>终身教职</td><td>-0.002*** (0.000)</td><td>-0.029*** (0.001)</td><td>-0.070*** (0.003)</td></tr><tr><td>Total_answersi,t-1</td><td>0.002*** (0.000)</td><td>0.013*** (0.000)</td><td>0.024*** (0.001)</td></tr><tr><td> $σ^2$ </td><td colspan="3">2.028*** (0.030)</td></tr><tr><td> $W_{i,t-1}$ </td><td colspan="3">ψ - 后验均值（标准差）</td></tr><tr><td> $c^w$ </td><td>-1.835*** (0.043)</td><td>-0.793*** (0.066)</td><td>-0.124*** (0.303)</td></tr><tr><td>Answers_receivedi,t-1</td><td>0.072*** (0.012)</td><td>0.023 (0.015)</td><td>0.021 (0.035)</td></tr><tr><td>Upvotes_answeri,t-1</td><td>0.069*** (0.017)</td><td>0.018 (0.017)</td><td>0.013 (0.027)</td></tr><tr><td>已接受_answersi,t-1</td><td>0.110*** (0.038)</td><td>0.056*** (0.018)</td><td>0.128 (0.083)</td></tr><tr><td>Badgesi,t-1</td><td>0.183*** (0.033)</td><td>0.144*** (0.036)</td><td>-0.054 (0.044)</td></tr><tr><td>初始概率</td><td>0.769*** (0.045)</td><td>0.192*** (0.041)</td><td>0.039*** (0.011)</td></tr><tr><td colspan="4">*p<0.1，**p<0.05； ***p<0.01。</td></tr></table>


Netzer, O., Lattin, J. M., and Srinivasan, V. 2008. “A Hidden Markov Model of Customer Relationship Dynamics,” Marketing Science (27:2), pp. 185-204.




Netzer, O.、Lattin, J. M. 和 Srinivasan, V. 2008 年。“客户关系动态的隐马尔可夫模型”，《营销科学》(27:2)，第 185-204 页。


## References




＃＃ 参考


Albert, J. H., and Chib, S. 1993. “Bayesian Analysis of Binary and Polychotomous Response Data,” Journal of the American Statistical Association (88:422), pp. 669-679.




Albert, J. H. 和 Chib, S. 1993 年。“二元和多分类响应数据的贝叶斯分析”，《美国统计协会杂志》(88:422)，第 669-679 页。


Kim, C.-J., and Nelson, C. R. 1999. State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications, Cambridge, MA: The MIT Press.




Kim, C.-J. 和 Nelson, C. R. 1999 年。具有机制切换的状态空间模型：经典和吉布斯采样方法及其应用，马萨诸塞州剑桥：麻省理工学院出版社。


MacDonald, I. L., and Zucchini, W. 1997. Hidden Markov and Other Models for Discrete-Valued Time Series, Boca Raton, FL: CRC Press.




MacDonald, I. L. 和 Zucchini, W. 1997。隐马尔可夫和其他离散值时间序列模型，博卡拉顿，佛罗里达州：CRC Press。


Singh, P. V., Tan, Y., and Youn, N. 2011. “A Hidden Markov Model of Developer Learning Dynamics in Open Source Software Projects,” Information Systems Research (22:4), pp. 790-807.




Singh, P. V.、Tan, Y. 和 Youn, N. 2011。“开源软件项目中开发人员学习动态的隐马尔可夫模型”，信息系统研究 (22:4)，第 790-807 页。


Smith, A., Naik, P. A., and Tsai, C.-L. 2006. “Markov-Switching Model Selection Using Kullback-Leibler Divergence,” Journal of Econometrics (134:2), pp. 553-577.




Smith, A.、Naik, P. A. 和 Tsai, C.-L. 2006 年。“使用 Kullback-Leibler 散度进行马尔可夫切换模型选择”，《计量经济学杂志》(134:2)，第 553-577 页。


Yan, L., and Tan, Y. 2014. “Feeling Blue? Go Online: An Empirical Study of Social Support Among Patients,” Information Systems Research (25:4), pp. 690-709.




Yan, L. 和 Tan, Y. 2014 年。“感觉忧郁？上网：患者社会支持的实证研究”，信息系统研究 (25:4)，第 690-709 页。
