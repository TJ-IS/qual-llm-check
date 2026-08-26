---
otero_id: 6828
otero_key: "CAK8YUFX"
title: "Electoral Competition in the Age of Social Media: The Role of Social Media Influencers"
authors: "Chao Ding; Wael Jabr; Hong Guo"
year: "2023"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16422"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ELECTORAL COMPETITION IN THE AGE OF SOCIAL MEDIA: THE ROLE OF SOCIAL MEDIA INFLUENCERS<sup>1</sup>

Chao Ding Innovation and Information Management, Faculty of Business and Economics, The University of Hong Kong, Hong Kong, CHINA, {chao.ding@hku.hk}

Wael Jabr

Supply Chain and Information Systems, Smeal College of Business, Pennsylvania State University, University Park, PA, U.S.A., {wjabr@psu.edu}

Hong Guo Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, AZ, U.S.A., {hguo@asu.edu}

Social media—and, in particular, social media influencers—are playing an increasingly central role in shaping public opinion on a variety of issues. The political sphere is no exception. In response to the impact that social media influencers have on citizens’ political views and voting behaviors, political parties adapt their messages and policies during election campaigns. Media outlets, too, faced with competition for readership from social media, are adjusting their news coverage. To analyze the nature and extent of the impact of social media on parties’ policies, media outlets’ news reports, and citizens’ opinions, we used a game theoretical model of electoral competition involving four key stakeholders— citizens, political parties, media outlets, and social media influencers. Our results show that with social media, parties’ policy positions become more moderate while media outlets’ editorial positions become more extreme. We also show that citizens’ opinions may become more polarized when the influencers true editorial positions are more homogeneous as a result of increased information distortion.

Keywords: Social media, social media influencers, information distortion, electoral competition, editorial position, ideology, polarization

## Introduction

Social media is the most recent addition to an evolving media landscape comprising newspapers, radio, and TV. This addition has undoubtedly transformed the amount of information communicated and its timeliness (Kinder, 2003). It has also contributed to the emergence of influencers who, in a political context, play the key role of independent content contributors and opinion leaders. Acquiring increasingly sizeable audiences, these social media influencers are able to post messages that reach a vast number of users, often shaping their opinion (Flamino et al., 2021; Pei & Mayzlin, 2022). In fact, citizens today have a greater chance of being exposed to political information shared by influencers on social media platforms than by any other media (Bode, 2016; Turcotte et al., 2015). This has become evident in recent U.S. presidential elections, where policy statements and opinion pieces are widely disseminated on social media—see for example the Twitter hashtags #actionclimate and #raisethewage. Consequently, in this age of social media, citizens can potentially learn more about important issues and be better informed about public policies.

Given the influence of social media, one would expect to find a major impact on citizens’ voting behavior in elections (Converse, 1962; Prior, 2007). In turn, this influence may change how parties devise policies during election campaigns. At the same time, citizens’ reliance on social media may reduce their consumption of traditional media outlets (e.g., newspapers), thus posing challenges to the outlets profitability. To make up for financial losses, traditional media outlets may have to adjust their news coverage. With this in mind, we answer four interrelated research questions in this paper: What role does social media play in elections? How does social media impact parties’ policymaking? How does social media impact traditional media outlets’ news reporting? How does social media impact public opinion?

We used an enhanced variation of the spatial model to study the role that social media plays in elections (also referred to as electoral competition) with four key stakeholders—citizens, parties, media outlets, and social media influencers. In line with election modeling in political science, we analyzed the uncertainty of election outcomes so that each stakeholder decides how to maximize their expected utility. Through our modeling, we were able to derive several key findings. First, we show that, in the age of social media, parties’ policy positions become more moderate. We explain this result by examining two key effects of policy positions: an ideology effect, which drives parties to conform to their political ideology, and an election effect, which drives parties towards more moderate policy positions that enable them to attract more votes and thus win an election. Because social media influencers play an important role in informing citizens, they end up strengthening the election effect. Parties’ best response is to moderate their positions such that their policies are more appealing to the general public. Second, we show that media outlets’ editorial positions become more extreme in the age of social media. This is driven by their goal of attracting more readers, given the competition with social media influencers. As such, media outlets are better off choosing radical positions for better differentiation. Third, we find that citizens’ opinions may become more polarized when the true editorial positions of social media influencers are more homogeneous as a result of increased information distortion.

Our paper makes unique contributions to the literature. We incorporate social media, a mainstream IS phenomenon, into the decision-making process of parties, media outlets, social media influencers, and citizens, ahead of elections. We specifically focus on influencers and derive insights about how they may have impacted politics, especially in relation to their level of truth telling. We also contribute to the ongoing academic conversation on the role of social media in politics, especially as it relates to the potential polarization of stakeholders. Our analytical approach derives a number of underlying mechanisms of the election process and of the strategic interactions between stakeholders.

The remainder of this paper is organized as follows. First, we present an overview of relevant literature on the role of social media in politics. Then we describe our modeling framework, followed by two sections with detailed analyses (benchmark model and main model). We provide the managerial implications and concluding remarks in the last section.

## Literature Review

To better position our paper, we first summarize data-driven research that analyzes the political influence of social media. Next, we highlight electoral studies that use the kind of analytical modelling that we apply in our paper.

Similar to other media types, social media plays an important role in informing the public (Graber & Dunaway, 2018; Turcotte et al., 2015). Given their limited time and attention (Stromberg, 2015), the public’s reliance on social media for information is prevalent across a number of fields, including politics (Rathore et al., 2017). For example, Petrova et al. (2021) found that politicians’ use of social media increases their donor base, thus intensifying electoral competition. Mousavi and Gu (2019) showed that, once elected, politicians vote more in line with the political ideology of their voter base. Beyond its informativeness, social media has been playing an influential role as well (Mallipeddi et al., 2022), sometimes resulting in echo chambers (Kitchens et al., 2020) and other times resulting in opinion moderation (Shore et al., 2018). Specifically, social media influencers, who amass sizeable audiences in their millions of followers, play a big role in exposing citizens to political information and in influencing their choices (Bode, 2016; Turcotte et al., 2015). Such influence has also been observed in a number of disciplines, such as marketing (Pei & Mayzlin, 2022). It is noteworthy, however, that no prior work has thus far attempted to provide a theoretical explanation of why the use of social media may exert an influence on parties, media outlets, and citizens. Our modeling approach contributes to this line of research by formalizing the role of social media and its influence on electoral competition.

Analytically, the economics and political science literatures have examined how various information sources influence citizens’ voting behavior in elections. Earlier work focused on parties’ policies as the sole information source (e.g., Baron (1994). Subsequently, researchers turned their attention to the influence of traditional media outlets on voters, such as newspapers and TV, as additional sources of information. Such media outlets report their viewpoints on parties’ policies (Chan & Suen, 2008) and candidates (Bernhardt et al., 2008;

Piolatto & Schuett, 2015), or may spread fake news about the candidates they oppose (Grossman & Helpman, 2020). After an extensive review of the game theoretical literature, we found little scholarly work that considers the impact of social media in politics. In the management literature, Soberman and Sadoulet (2007) is the only paper that develops an analytical model that is closely related to ours, though their focus is on political campaign spending and the intensity of parties’ communication through traditional media. As more and more people are using social media to spread and receive information, we believe there is a need to investigate social media influence through an analytical lens. Focusing on changes introduced by social media (i.e., social media influencers shaping citizens’ opinions), we are able to better understand the underlying mechanism of the role of social media in elections. We achieve this goal by framing our analysis on a variation of the spatial model to spell out stakeholders’ strategic decision-making processes in an election setting and by accounting for key features of social media in politics.

## Modeling Framework

We consider a unit mass of citizens voting for one of two political parties, denoted by $i \in \{ D , R \}$ , competing in an election.<sup>2</sup> To appeal to citizens, parties choose either a liberal (??) or a conservative (??) policy vis-à-vis important issues of public interest such as taxation or immigration. Parties’ policies are public knowledge. There are two media outlets (e.g., newspapers), denoted by $j \in \{ 1 , 2 \}$ , producing news reports on important issues and showing the outlets’ support for or opposition to a policy. There are two social media influencers, denoted by $k \in \{ 1 , 2 \}$ , posting messages on social media platforms. Following the economics and political science literature (e.g., Mullainathan & Shleifer, 2005 and Schultz, 2008), we capture the actual conditions of the important issues through the state of the economy denoted by ?? , which follows a uniform distribution on [0,1] . <sup>3</sup> Once realized, the state of the economy is known to parties, media outlets, and social media influencers, but not to citizens, due to their limited access to information and lack of expert knowledge. As a result, what citizens learn about the state is crucial for the election outcome. We next describe the strategic decision-making processes of stakeholders in our game theoretical model. All notations are presented in Table 1.

## Parties

The two parties’ political ideologies, denoted by $y _ { i }$ for party ??, are at the two ends of the liberal-conservative line with party ?? being liberal and party ?? conservative, i.e., $y _ { D } = 1 - y _ { R } =$ 0 . A party’s ideology describes a threshold value that determines the party’s preference for policy ?? . Therefore, when evaluating an issue in state ??, party ?? prefers policy ?? if $\theta \geq y _ { i }$ and policy ?? if $\theta < y _ { i } . ^ { 4 }$ In line with prior literature (Besley & Case, 2003; Wittman, 1983), we formulate party ??’s utility function for a given state ?? as follows:

$$
\begin{array}{l l} \mathrm{v} _ {i} [ \theta , I _ {i} ] \\ = \left\{ \begin{array}{l l} I _ {i} \cdot 2 w + (\theta - y _ {i}) & \text {if policy l is the winning policy} \\ I _ {i} \cdot 2 w + (y _ {i} - \theta) & \text {if policy c is the winning policy,} \end{array} \right. \end{array}
$$

where $I _ { i } = 1$ indicates party ?? is elected (or not elected, if $I _ { i } = 0 )$ . The first term captures the party’s utility from holding office when elected. <sup>5</sup> The winning party’s policy is the winning policy which is implemented after the election. The second term captures the utility (disutility) if the winning policy is (is not) the party’s preferred policy. Note that a party preferring one policy does not necessarily lead to that party choosing that policy. This is because the party also wants to win the election by choosing a policy that appeals to citizens. Therefore, we focus on deriving party $i { { \bar { \bf \Delta } } _ { \bf { S } } }$ policymaking strategy characterized by its policy position ??<sub>??</sub> (Chan & Suen, 2008; Glaeser et al., 2005; Grossman & Helpman, 1996), where party ?? chooses policy ?? if $\theta \geq p _ { i }$ and policy ?? if $\theta <$ $p _ { i } . ^ { 6 } \mathrm { I }$ t can be shown that $p _ { D } < p _ { R }$ . When $\theta \in [ p _ { D } , p _ { R } ] ,$ , party ?? chooses policy ??, and party ?? chooses policy ??, resulting in policy pair (??, ??). When ?? takes extreme values $( { \mathrm { i . e . , } } \theta < p _ { D }$ or $\theta > p _ { R } )$ , the resulting policy pair is (??, ??) or (??, ??). Note that policy pair (??, ??) is not feasible.

Since party ?? chooses its policy position $p _ { i }$ before a state $\theta$ is realized, its objective is to maximize expected utilities over all possible states, that is, max $\begin{array} { r } { v _ { i } = \int _ { 0 } ^ { 1 } \bigl ( \sum _ { I _ { i } \in \{ 0 , 1 \} } v _ { i } [ \theta , I _ { i } ] } \end{array}$ ??<sub>??</sub> $\operatorname { P r o b } [ I _ { i } \mid \theta ] ) d \theta$ , where Prob $[ I _ { i } \mid \theta ]$ is party ??’s probability of winning given state ??.

## Citizens

A citizen’s ideology ?? is measured by their preference for policy ??. The ideology is uniformly distributed on $[ 0 , 1 ]$ with $f [ \cdot ]$ and $F [ \cdot ]$ as its respective PDF and CDF. A smaller ?? indicates that the citizen prefers more liberal policies. Given a state $\theta ,$ citizens’ utilities are as follows:

$$
\begin{array}{l l} u [ x, I _ {x} \mid \theta ] \\ = \left\{ \begin{array}{l l} I _ {R} \cdot 2 \delta + (\theta - x) & \text { if   policy   } l \text {   is   the   winning   policy } \\ I _ {R} \cdot 2 \delta + (x - \theta) & \text { if   policy   } c \text {   is   the   winning   policy }. \end{array} \right. \end{array}
$$

The first term captures the citizen’s utility from their preference for the party that is elected to office. We denote citizens’ common preference for party ?? by ?? , which is uniformly distributed on $\left[ - { \frac { 1 } { 2 } } , { \frac { 1 } { 2 } } \right]$ and its corresponding PDF and CDF are denoted by ??[∙] and ??[∙], respectively.<sup>7</sup> Hence, the utility 2?? only applies if party ?? is elected $( \mathrm { i } . \mathrm { e } . , I _ { R } = 1 )$ We note that parties do not know ?? when they make their policy decisions and are thus unable to accurately predict their probability of winning. The second term captures the citizen’s utility from their policy preference according to their ideology ??. After citizens learn about the state of the economy from different information sources (e.g., media outlets’ news report, social media influencers’ messages), they update their beliefs and then cast their votes. We denote citizen $x ^ { \prime } { \mathbf { s } }$ posterior belief about the state of the economy by ${ \widehat { \theta } } _ { x } ;$ hence, citizen ?? chooses a vote that maximizes $\iota [ x , I _ { x } \mid \hat { \theta } _ { x } ]$

## Media Outlets

There are two competing media outlets (e.g., newspapers or TV stations), which have distinct editorial positions, denoted by $m _ { j }$ for outlet ??, that specify the overall polarity of news reports. Specifically, outlet $j ^ { \prime } { \bf s }$ report is in support of policy ?? $\mathrm { i f } \theta \geq m _ { j }$ and in support of policy ?? if $\theta < m _ { j }$ . We consider Outlet 1 (Outlet 2) siding with party $D ' \mathbf { s }$ liberal ideology (party $R ^ { * } s$ conservative ideology), which reflects $m _ { 1 } < m _ { 2 } . ^ { 8 }$ Citizens may read media outlets’ reports on policies, which changes their beliefs about the state of the economy and consequently influences their vote. Media outlets generate revenue from advertisement, which is contingent on the number of readers (Bernhardt et al., 2008; Oliveros & Vardy, 2015; Sobbrio, 2015). Formally, outlet ?? solves the following profit maximization problem $\operatorname* { m a x } _ { m _ { j } } \pi _ { j } = q _ { j }$ , where $q _ { j }$ represents outlet $j ^ { \mathrm { ~ \tiny ~ , ~ } } \mathrm { ~ s ~ }$ expected size of readership. This readership is discounted at a rate of ?? when citizens consume multiple information sources (more details about ?? is provided in the analysis sections).

## Social Media Influencers

There are two social media influencers, with Influencer 1 holding a liberal ideology and Influencer 2 a conservative ideology. Consequently, Influencer 1 (Influencer 2) identifies with party ?? (party ??). We therefore consider that influencer ?? has a true editorial position denoted by $t _ { k }$ , where $t _ { 1 } = 1 -$ $t _ { 2 } = t \in [ 0 , \frac { 1 } { 2 } ]$ . However, influencers may not truthfully reveal their opinions on social media. They might choose a stated editorial position denoted by $s _ { k }$ and post messages that support policy ?? if $\theta \geq s _ { k }$ and support policy ?? if $\theta < s _ { k }$ . As a result, if $s _ { k }$ deviates from $t _ { k } ,$ , influencer $k ' \mathrm { s }$ messages do not disclose their true policy stance when the state is between $s _ { k }$ and $t _ { k }$ . Such untruthful messages lead to information distortion, which worsens as the gap between $s _ { k }$ and $t _ { k }$ widens. Formally, social media influencers solve the following utility maximization problem:

$$
\begin{array}{r} \max _ {s _ {1}} \Pi_ {1} = \mathrm{Prob} [ I _ {D} = 1 ] + Q _ {1} - \beta (s _ {1} - t _ {1}) ^ {2}, \\ \max _ {s _ {2}} \Pi_ {2} = \mathrm{Prob} [ I _ {R} = 1 ] + Q _ {2} - \beta (s _ {2} - t _ {2}) ^ {2}. \end{array}
$$

The first term captures the influencer’s ideology motive so that the influencer benefits from the party with similar ideology identification winning. The second term captures the influencer’s readership motive to attract a larger audience base, which helps to generate more revenue (e.g., from advertising). The third term accounts for the influencer’s truth-telling motive to align the influencer’s stated editorial position with their true editorial position. It is formulated as a disutility resulting from the cost of information distortion, where $\beta \geq 0$ is the cost parameter. Such a cost is generally rooted in a concern for self-reputation, morals, or identity (Abeler et al., 2014; Akerlof & Kranton, 2000; Benabou & Tirole, 2006).

<table><tr><td colspan="2">Table 1. Notations</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td>i</td><td>Party i ∈ {D,R}.</td></tr><tr><td>j</td><td>Media outlet j ∈ {1,2}.</td></tr><tr><td>k</td><td>Social media influencer k ∈ {1,2}.</td></tr><tr><td>l and c</td><td>Two feasible policies.</td></tr><tr><td>θ</td><td>State of the economy which follows a uniform distribution on [0,1].</td></tr><tr><td>x</td><td>A citizen&#x27;s ideology measured by their preference for policy c.It follows a uniform distribution on [0,1] that captures citizen heterogeneity.</td></tr><tr><td>μ</td><td>Median of the uniform distribution for x with μ = 1/2.</td></tr><tr><td>δ</td><td>Citizens&#x27; preference for party R which follows a uniform distribution on [-1/2,1/2].</td></tr><tr><td>α</td><td>Readership discount parameter when citizens consume multiple information sources.</td></tr><tr><td>u[x]</td><td>Citizen x&#x27;s utility.</td></tr><tr><td>yi</td><td>Party i&#x27;s ideology measured by its preference for policy c. yD=1 - yR=0.</td></tr><tr><td>w</td><td>Parties&#x27; preference for winning the election.</td></tr><tr><td>β</td><td>Cost parameter of information distortion.</td></tr><tr><td>tk</td><td>Social media influencer k&#x27;s true editorial position. t1=1-t2=t∈[0,1/2].</td></tr><tr><td>vi</td><td>Party i&#x27;s expected utility.</td></tr><tr><td>qj</td><td>Media outlet j&#x27;s expected size of readership.</td></tr><tr><td>πj</td><td>Media outlet j&#x27;s expected utility.</td></tr><tr><td>Qk</td><td>Social media influencer k&#x27;s expected size of readership.</td></tr><tr><td>Πk</td><td>Social media influencer k&#x27;s expected utility.</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td>pi</td><td>Party i&#x27;s policy position.</td></tr><tr><td>mj</td><td>Media outlet j&#x27;s editorial position.</td></tr><tr><td>sk</td><td>Social media influencer k&#x27;s stated editorial position.</td></tr></table>

## Election

In line with the tradition regarding election analysis in the political economy literature, citizens consider their vote to be decisive in tipping election results. In a majority criterion voting system (i.e., with a single winner who is ranked first by a majority of voters), the election result is determined by the vote of the median citizen whose ideology is at the center of the liberal-conservative line, i.e., $\textstyle \mu = { \frac { 1 } { 2 } }$ . Accordingly, a party’s probability of winning can be derived from the median citizens’ voting probability.<sup>9</sup> We summarize it as follows:

$$
\begin{array}{l} \operatorname{Prob} [ I _ {D} = 1 \mid \theta ] = 1 - \operatorname{Prob} [ I _ {R} = 1 \mid \theta ] \\ = \left\{ \begin{array}{l l} \frac {1}{2} & \text {if policy pair is (l,l) or (c,c)}, \\ G \big [ \hat {\theta} _ {\mu} - \mu \big ] & \text {if policy pair is (l,c)}. \end{array} \right. \end{array}
$$

Next, we analyze parties’ equilibrium decisions under two models. We start with a benchmark model without social media, and then introduce social media influencers in our main model. By comparing these two models, we are able to understand the impact of social media on parties’ policymaking, media outlets’ news reporting, and citizens’ opinions.

probability to win is $G [ \widehat { \theta } _ { \mu } - \mu ]$ , which is the probability of the median citizen voting for party ??.

## Benchmark Model

In the benchmark model, we discuss how citizens choose whether and which report(s) to read, how they are influenced by the reports, and how media outlets and parties maximize their expected utilities. The sequence of events is as follows:

1. Party ?? chooses policy position $p _ { i }$ , and media outlet ?? chooses editorial position ??<sub>??</sub>.

2. The state of the economy ?? is realized. Party ?? chooses policy ?? or ?? depending on whether $\theta \geq p _ { i }$ . Media outlet ?? reports in support of ?? or ?? depending on whether $\theta \geq m _ { j }$

3. Citizens’ party preference ?? is realized. Citizens decide whether to read news reports from media outlets, update their beliefs about ??, then cast their votes. The election result is finalized.

To learn about the state of the economy, a citizen may read reports from one or both media outlets or may not read any news reports. The citizen will only read reports if doing so generates a utility gain. It immediately follows that reading reports leads to a change in the citizen’s vote.<sup>10</sup> As such, it is established that media outlets’ reports exert an influence on citizens and sway their votes if they choose to consume the reports. Therefore, we call a media outlet’s readership its influence territory. Figure 1 summarizes each media outlet’s influence territory.

Accordingly, we derive media outlets’ expected utilities— taking Media Outlet 1 as an example:

$$
\pi_ {1} = \Big (H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right] \Big) + (1 - \alpha) \Big (H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] \Big),
$$

where $H [ \cdot ]$ is the convolution of $F [ \cdot ]$ and ??[∙], i.e., $H [ \cdot ] =$ $( F * G ) [ \cdot ]$ and ?? is the readership discount parameter when citizens read reports from both media outlets. The discount is proportional to the number of information sources consumed. This reflects a reduced profit for the media outlets due to citizens’ split attention. In equilibrium, media outlets and parties maximize their respective expected utility. The results are presented in Proposition 1. The proofs of all propositions are relegated to the Appendix.

Proposition 1 (equilibrium of benchmark model): In equilibrium, parties’ policy positions and media outlets’ editorial positions are as follows:

$$
\begin{array}{r l} & p _ {D} ^ {B M} = 1 - p _ {R} ^ {B M} = \\ & \frac {2 \alpha - 2 w (1 - \alpha) - 1 + \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (1 - \alpha)}, \\ & m _ {1} ^ {B M} = 1 - m _ {2} ^ {B M} = \\ & \frac {6 \alpha^ {2} - 1 1 \alpha - 2 \alpha w (1 - \alpha) + 4 - \alpha \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (2 - \alpha) (1 - \alpha)}. \end{array}
$$

A party’s policy position has two countervailing effects. On the one hand, each party has the incentive to choose a policy position closer to its ideology so that the party’s policy choice is more likely to be aligned with its policy preference. We refer to this effect as policy position’s ideology effect. This effect drives the parties to choose more extreme policy positions. On the other hand, a party’s policy position also plays an information role in the electoral competition. Citizens observe the policies and then update their beliefs about the state of the economy. Without knowing citizens’ exact party preference, the party that chooses an extreme policy position runs the risk of not appealing to the median citizen and losing their vote. As such, each party has an incentive to choose a more moderate policy position. We refer to this effect as policy position’s election effect.

Media outlets compete with each other to expand their influence territory, which we refer to as territory competition. Such competition can significantly shift each outlet’s influence territory, which may subsequently impact their editorial positions as well as parties’ policy positions. As shown in Figure 1, there are five regions of citizens based on whether they read reports and, if so, which outlet’s report they read. The median citizen, being located closer to the center of the line, is likely to read either one or both outlets’ reports, and is hence likely to be more informed and swayed in some states. Therefore, parties have an incentive to make policies that appeal more to the median citizen in order to win the election. In other words, media outlets’ reports strengthen the election effect of policy positions. The equilibrium result of a party’s policy position is achieved by balancing this strengthened election effect and the ideology effect. Next, we discuss electoral competition in the age of social media in the presence of social media influencers.

$\begin{array} { r } { \left( x - \frac { p _ { D } + m _ { j } } { 2 } + 2 \delta \right) } \end{array}$ and they now vote for party ??. Thus, the citizen will read the reports only $\begin{array} { r } { \mathrm { i f } \frac { p _ { D } + m _ { j } } { 2 } \leq x + \delta \leq \frac { p _ { D } + p _ { R } } { 2 } . } \end{array}$ . After reading news reports, the citizen changes their vote. The influence territory is obtained by considering all possible segments of ?? and all citizens.

![](/api/attachments/CAK8YUFX/fulltext/images/0b8a2169e9b054b7f90fc0e7e7dfdb4e57a1199f42e6ec7567d4510704f02046.jpg)  
Figure 1. Media Outlets’ Influence Territories

![](/api/attachments/CAK8YUFX/fulltext/images/5978d093ea8b61e2df3de2b9ba347b00f4c98d8e4ae4cfc45c3f7d68b7dc690f.jpg)  
Figure 2. Influence Territories of Media Outlets and Social Media Influencers Under the TE Strategy

## Main Model: Analysis of Electoral Competition in the Age of Social Media

The sequence of events in the main model is as follows:

1. Party ?? chooses policy position $p _ { i } ,$ media outlet ?? chooses editorial position $m _ { j }$ , and social media influencer ?? chooses stated editorial positions $s _ { k }$

2. State of the economy ?? is realized. Party ?? chooses policy ?? or ?? , depending on whether $\theta \geq p _ { i }$ . Media outlet ?? reports in support of ?? or ??, depending on whether $\theta \geq$ $m _ { j }$ . Social media influencer ?? posts messages that support ?? or ??, depending on whether $\theta \geq s _ { k }$

3. Citizens’ party preference ?? is realized. Citizens decide whether to read influencers’ messages on social media and/or media outlet’s news reports, update their beliefs about ?? , then cast their votes. The election result is finalized.

Social media influencers and media outlets cannot choose more extreme editorial positions than the parties’ policy positions; otherwise, citizens would not consume their news reports or social media messages because such information would not provide additional value. As a result, there are two scenarios corresponding to the two strategic choices of social media influencers’ stated editorial positions. The first is the territory-expanding (TE) strategy under which social media influencers choose editorial positions that are more extreme than the media outlets’ editorial positions $( \mathrm { i . e . , } s _ { 1 } < m _ { 1 } <$ $m _ { 2 } < s _ { 2 } )$ . Alternatively, the second is the territory-sharing (TS) strategy $( \mathrm { i . e . , } m _ { 1 } < s _ { 1 } < s _ { 2 } < m _ { 2 } )$ . As an example, we illustrate the influence territories under the TE strategy in Figure 2.

Accordingly, we derive media outlets and social media influencers’ expected utilities—using Outlet 1 and Influencer 1 as examples:

$$
\begin{array}{r l} & {\pi_ {1} = (1 - \alpha) \left(H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right]\right) + (1 - 2 \alpha) \left(H \left[ \frac {p _ {D} + s _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] + H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {s _ {1} + p _ {R}}{2} \right]\right) + (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right),} \end{array}
$$

$$
\begin{array}{l} \Pi_ {1} = \int_ {0} ^ {1} \mathrm{Prob} [ I _ {D} = 1   |   \theta ]   d \theta + \left(H \left[ \frac {p _ {D} + m _ {1}}{2} \right] - H \left[ \frac {p _ {D} + s _ {1}}{2} \right]\right) + (1 - \alpha) \left(H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right]\right) + (1 - 2 \alpha) \left(H \left[ \frac {p _ {D} + s _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right]\right) + (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right) - \\ H \left[ \frac {p _ {D} + s _ {2}}{2} \right]) - \beta (s _ {1} - t) ^ {2}. \end{array}
$$

Figure 2 illustrates how both social media influencers are able to expand their respective influence territory to citizens residing in the farther ends, making it is a territory-expanding strategy. By contrast, under the TS strategy, each social media influencer shares their influence territory with media outlets and the other social media influencer. We focus on the market conditions under which both the TE and TS strategies have interior solutions. In other words, we assume that $\underline { { t } } \le t \le \overline { { t } }$ (reflected in the feasible region in Figure 3) in analyzing the equilibrium.<sup>11</sup> We present the results in Proposition 2.

Proposition 2 (Equilibrium of the main model): There are two possible equilibria in the main model:

a. the territory-sharing (TS) equilibrium when $t < \hat { t } _ { 1 }$

$$
\begin{array}{r l} & p _ {D} ^ {T S} = 1 - p _ {R} ^ {T S} = \frac {6 (1 + w) \alpha - 2 w - 1 + \sqrt {(6 (1 + w) \alpha - 2 w - 1) ^ {2} + 8 w (1 - 9 \alpha^ {2})}}{4 (1 - 3 \alpha)}, \\ & s _ {1} ^ {T S} = 1 - s _ {2} ^ {T S} = \\ & \frac {- 6 (3 - w) \alpha - 2 w + 6 4 t \beta + 7 + \sqrt {(6 (1 + w) \alpha - 2 w - 1) ^ {2} + 8 w (1 - 9 \alpha^ {2})}}{8 (2 + 8 \beta - 3 \alpha)}, \\ & m _ {1} ^ {T S} = 1 - m _ {2} ^ {T S} = \frac {- 6 (5 - 3 w) \alpha - 6 w + 5 + 3 \sqrt {(6 (1 + w) \alpha - 2 w - 1) ^ {2} + 8 w (1 - 9 \alpha^ {2})}}{8 (2 - 3 \alpha)}. \end{array}
$$

b. the territory-expanding (TE) equilibrium when $t \geq \hat { t } _ { 1 }$

$$
\begin{array}{r l} & p _ {D} ^ {T E} = 1 - p _ {R} ^ {T E} = \\ & \frac {6 \alpha - 8 \beta t - 1 + \sqrt {(2 w (1 + 4 \beta - 3 \alpha) - 1 - 8 \beta t + 6 \alpha) ^ {2} + 8 w (1 + 4 \beta - 3 \alpha) (2 + 8 \beta - 3 \alpha)}}{4 (1 + 4 \beta - 3 \alpha)} - \frac {w}{2}, \\ & s _ {1} ^ {T E} = 1 - s _ {2} ^ {T E} = \\ & \frac {1 8 (3 - w) \alpha^ {2} + (2 4 (w - 4) \beta + 6 w - 7 2 t \beta - 3 3) \alpha + 4 (1 + 4 \beta) (1 + 8 t \beta)}{4 (1 + 4 \beta - 3 \alpha) (2 + 8 \beta - 3 \alpha)} - \\ & \frac {3 \alpha \sqrt {(1 + 8 t \beta - 6 \alpha) ^ {2} + 4 w (3 + 8 (2 - t) \beta) (1 + 4 \beta - 3 \alpha) + 4 w ^ {2} (1 + 4 \beta - 3 \alpha) ^ {2}}}{4 (1 + 4 \beta - 3 \alpha) (2 + 8 \beta - 3 \alpha)}, \\ & m _ {1} ^ {T E} = 1 - m _ {2} ^ {T E} = \frac {6 (5 - w) \alpha^ {2} + (8 (t + w - 6) \beta + 2 w - 2 3) \alpha + 4 (1 + 4 \beta)}{4 (1 + 4 \beta - 3 \alpha) (2 - 3 \alpha)} - \\ & \frac {\alpha \sqrt {(1 + 8 t \beta - 6 \alpha) ^ {2} + 4 w (3 + 8 (2 - t) \beta) (1 + 4 \beta - 3 \alpha) + 4 w ^ {2} (1 + 4 \beta - 3 \alpha) ^ {2}}}{4 (1 + 4 \beta - 3 \alpha) (2 - 3 \alpha)}. \end{array}
$$

The messages posted on social media by the influencers function similarly to media outlets’ reports by influencing citizens’ beliefs and swaying their votes. In other words, social media influencers join the territory competition with media outlets. However, media outlets and social media influencers have different objectives. As profit maximizers, media outlets shape their editorial positions through news reports to compete for readership. In comparison, social media influencers choose a stated editorial position in order to achieve the maximization of not only the readership motive but also their ideology motive and truth-telling motive. Although the latter two play the same role under both the TS and TE strategies, the readership motive differs between the two strategies. Specifically, territory competition among media outlets and social media influencers exhibits different characteristics. Territory competition is more intense for social media influencers under the TS strategy than under the TE strategy. The equilibrium is illustrated in Figure 3.

When ?? is relatively small, social media influencers are more differentiated in terms of their true editorial positions. More differentiation helps relax the competitive tension between the two social media influencers. In this case, they can afford to endure the TS strategy for the benefit of inducing a larger readership base. In contrast, when ?? is relatively large, social media influencers are more homogeneous. This creates more competitive tension between the two social media influencers. In this case, they have to resort to the TE strategy to counterbalance the territory competition and maintain their readership.

In the next two propositions, we establish the impact of social media on parties’ policy positions and media outlets’ editorial positions.

Proposition 3 (impact of social media on parties’ policy positions): In the age of social media, parties’ policy positions are more moderate in comparison with the age prior to social media $( i . e . , p _ { D } ^ { T S } , p _ { D } ^ { T E } > p _ { D } ^ { B \hat { M } }$ and $p _ { R } ^ { T S } , p _ { R } ^ { T E } < \bar { p _ { R } ^ { B M } } )$

The presence of social media influencers has two opposing impacts on parties’ policy positions. On the one hand, social media influencers serve as an additional channel for citizens to learn about the state of the economy. As a result, citizens become more informed, leading to a strengthened election effect. On the other hand, social media influencers sometimes choose stated editorial positions that deviate from their true editorial positions in order to better serve their ideology motive and readership motive. This leads to information distortion that has an adverse impact on citizens’ knowledge of the state of the economy, thus leading to a weakened election effect. Note that information distortion only occurs under certain states of economy. Therefore, the overall election effect is strengthened. Also note that social media does not influence the ideology effect of the policy position. As such, this strengthened election effect drives the parties to moderate their policy positions. Doing so increases the likelihood that their policies are preferred by the median citizen, thus improving the parties’ probabilities of winning.

![](/api/attachments/CAK8YUFX/fulltext/images/aae3448a32a8889d604bf7745c4c577381dc1ced976b51b8eda3e18b42c4263b.jpg)  
Note: Feasible region is indicated by the bold boundary lines, i.e., $\begin{array} { r } { \underline { { t } } \leq t \leq \overline { { t } } \ , 0 \leq t \leq \frac { 1 } { 2 } , } \end{array}$ and $\beta \geq 0$  
Figure 3. Equilibrium of Main Model

We note that the phenomenon of parties moderating their positions has been documented in a number of recent polls and case studies. In their analysis of parliamentarians’ communications in a number of countries, a notable example is Esteve Del Valle et al. (2022), who showed that “online social platforms open up spaces for conversation between political parties.” Using a polarization index of parliamentarians in the Netherlands, they provide evidence to refute the rise of party polarization. In another work that uses survey data from 174 election studies, Moral and Best (2023) showed a moderating trend for political parties in a number of Western democracies (such as Denmark and Sweden) over the last few years, as social media became a ubiquitous phenomenon there. Our result in Proposition 3 is consistent with such anecdotal evidence.

Proposition 4 (impact of social media on media outlets’ editorial positions): In comparison with the age prior to social media, media outlets’ editorial positions are more extreme in the age of social media ( $i . e . , m _ { 1 } ^ { T S } , m _ { 1 } ^ { T E } < m _ { 1 } ^ { B M }$ and $m _ { 2 } ^ { T S } , m _ { 2 } ^ { E S } > \overline { { { m } } } _ { 2 } ^ { B \bar { M } } )$ .

In the age of social media, social media influencers join media outlets in the territory competition for readers. The intensified competition provides media outlets with the incentive to moderate their editorial positions in order to maintain readership. However, as we know from Proposition 3, the parties moderate their policy positions in the age of social media, and the media outlets respond by differentiating from one another and choosing more extreme editorial positions. This potentially improves the media outlets’ readership, which in turn enhances their profit. Overall, media outlets choose more radical editorial positions in the age of social media. As anecdotal evidence, it is clear that some mainstream media outlets tend to take a more extreme stance on political issues. This also shows in the influence on citizens. When polled during the 2020 U.S. presidential election year, 65% of Republicans stated they trusted Fox News, while 67% of Democrats trusted CNN, and 48% trusted MSNBC (Jurkowitz et al., 2020).

To further establish social media’s impact on citizens, we borrowed the concept of dispersion of public opinion first introduced by DiMaggio et al. (1996). In the political context, the dispersion of public opinion is a variance measure commonly used to evaluate citizens’ polarization (Santos et al., 2021). We applied the same variance measure to assess the changes in citizens’ opinions about a party under the influence of social media. This is in direct connection with the dispersion of their votes, i.e., whether citizens tend to vote alike or not. Note that, in equilibrium, all stakeholders’ decisions are symmetric (see Propositions 1 and 2). Therefore, we represent citizens’ dispersion of public opinion as $\begin{array} { r } { D P O = \int ( \mathrm { P r o b } [ I _ { D } = 1 ~ | \theta ] - \mathrm { P r o b } [ I _ { D } = } \end{array}$ $\begin{array} { r } { \mathrm { 1 } ] ) ^ { 2 } d \theta = \int ( { \mathrm { P r o b } } [ I _ { R } = 1 \ | \ \theta ] - { \mathrm { P r o b } } [ I _ { R } = 1 ] ) ^ { 2 } d \theta \quad . \quad \mathrm { A } } \end{array}$ larger (smaller) dispersion indicates that public opinion is more (less) polarized. By comparing the dispersion of the benchmark model with the main model, we obtain the following proposition.

Proposition 5 (impact of social media on the dispersion of public opinion): In the age of social media, public opinion becomes less polarized (i.e., $D P O ^ { T S } , D P O ^ { \hat { T } E } < D \bar { P ( } O ^ { B M } \ )$ 0 when $t < \hat { t } _ { 2 }$ and more polarized $( i . e . , \ D P O ^ { T E } \ge D P O ^ { B M } ,$ ) when $t \geq \hat { t } _ { 2 }$ in comparison with the age prior to social media.

Figure 4 illustrates the threshold that characterizes the impact of social media on public opinion, more specifically, the dispersion of citizens’ voting behavior.

Interestingly, we found that when social media influencers are more homogeneous in terms of their true editorial positions, public opinion becomes more polarized. This is reflected by a higher variability in citizens’ voting behavior. Such a polarization result occurs only when social media influencers choose the TE strategy. That is, relative to media outlets’ editorial positions, social media influencers choose more radical stated editorial positions to avoid intense territorial competition. However, these more radical positions also result in a higher degree of information distortion that could impact citizens’ beliefs. Therefore, citizens’ voting behavior and opinions tend to become highly polarized. Following the same logic, public opinion becomes less polarized in the presence of social media influencers who are more differentiated.

Our result in Proposition 5 offers a potential explanation for the divergent findings in the literature regarding the polarization of citizens’ opinions in the age of social media. In the U.S., studies have found evidence both for and against the rise of citizens’ opinion polarization. While Bail et al. (2018) and Jurkowitz et al. (2020), among others, found increased polarization. The findings are inconclusive in this large body of work. Some attribute the mixed evidence to the fact that polarization may be misperceived (Levendusky & Malhotra, 2016) or overestimated (Fernbach & Van Boven, 2022). Others have gone further, arguing against the “conception of a polarized America” (Bianco & Canon, 2021). This divergence regarding the polarization of citizens’ opinion is also observed across world regions. Tyagi et al. (2020), for example, provided evidence of increased citizens’ opinion polarization in both India and Pakistan based on analysis of parliamentary elections in 2019, while Boxell et al. (2020) showed that out of 12 countries studied around local election times, citizens’ opinion polarization increased in six countries and decreased in the other six.

## Discussion and Conclusion

Social media is undoubtedly becoming a central force in informing the public about a variety of issues. Furthermore, social media influencers have been playing an increasingly important role in shaping public opinion through their social media posts (e.g., tweets). In the political arena, this influence exerts an impact on citizens’ views and, consequently, on their voting behavior. Anticipating such an impact during election campaigns, parties may change how they devise policies. With citizens’ extensive use of social media and reduced reliance on media outlets, the profitability of media outlets may be jeopardized, potentially prompting them to adjust their news coverage. In this paper, we therefore study the impact of social media on parties’ policymaking, media outlets’ news reporting, and the dispersion of public opinion. Our work builds on wellestablished spatial models in economics and political science and contributes to a burgeoning stream of research in IS that investigates the impact of IS artifacts on politics.

We used a game theoretical model to analyze the strategic decisions of citizens, parties, media outlets, and social media influencers in an election with highly uncertain outcomes. For citizens, we characterized their voting behavior based on the state of the economy, which they learned about from different sources. For parties, we identified two important effects from their policy positions: an ideology effect resulting from parties conforming to their ideology, and an election effect resulting from parties’ desire to win the election. For media outlets, we studied their editorial positions that shape their news reports in the territory competition for readership. For social media influencers, we studied the potential for information distortion whenever their stated editorial positions deviate from their true editorial positions. We found that in the age of social media, parties’ policy positions become more moderate and media outlets’ editorial positions become more extreme. We also showed that citizens’ opinions may become more polarized when the influencers’ true editorial positions are more homogeneous as a result of increased information distortion.

With social media platforms constituting an increasingly essential information source in everyday life, citizens opinions may tend to be further shaped by the messages of social media influencers. In elections, the impact of social media is understandably tied to the level of citizens’ social media usage. As usage varies from region to region, depending, among other things, on how extensive the IT infrastructure is (e.g., how widespread the 5G network is), it is expected that the impact of social media will vary accordingly. Regions in East Asia, for example, have on average higher social media penetration and growth than regions in South Asia, partly because of their robust communication infrastructure. Our results suggest that in regions with more robust IT infrastructure, and thus higher social media penetration, political parties are more likely to be in agreement about policymaking during election campaigns. Under these conditions, news reporting on policies is also likely to become more extreme, as compared to regions with less robust IT or lower social media penetration.

![](/api/attachments/CAK8YUFX/fulltext/images/11ac79540c2f2ecdb065f3250dace1b64ea5b54204e92d016bfb8c8ec76f49df.jpg)  
Note: Feasible region is indicated by the bold boundary lines, i.e., ?? ≤ ?? ≤ ?? , 0 ≤ ?? ≤ <sup>1</sup>, and $\beta \geq 0 .$  
Figure 4. Dispersion of Public Opinion

Our results also provide theoretical guidance for parties and media outlets on how to adjust their positions when a new communication technology becomes available. By reading media outlets’ reports or social media influencers’ messages, citizens become better informed about public policies; parties should thus consider making their policies more appealing to the median citizen. Our findings suggest that, as innovative technologies that efficiently disseminate information are further developed, parties should further moderate their policy positions in future election cycles. In addition, technological innovations result in competitive pressures on media outlets for readership. Accordingly, we suggest that media outlets may have to polarize their editorial positions in order to maintain profitability. However, we note that enhanced communication technologies also make information distortion less costly for influencers. Citizens who consume influencers social media messages are more likely to espouse extreme views, leading to opinion polarization.

Considering the complex nature of elections and the intricate interplay between all the stakeholders, our game theoretical model inevitably has limitations, due to the possibility that we did not capture all elements that play a role in the election process. One interesting direction for future research would be to explore the role of social media platforms per se, not just the influencers on those platforms. This becomes more pressing, given the increasing indications that such platforms may have a preset political standpoint, promoting certain governance policies, advocating certain positions, or manipulating information (Aral & Eckles, 2019). Analyzing the role that social media platforms play through, for example, filtering their algorithms would generate insights regarding the consequences on elections or on the promotion or censorship of social media content and thereby entail regulatory implications. Additionally, modeling the finegrained process of information dissemination among social media users would produce additional insights regarding the reinforcement of opinions and the empowerment of individuals. Such insights would be helpful for the effective design of political campaigns on social media.

## References

Abeler, J., Becker, A., & Falk, A. (2014). Representative evidence on lying costs. Journal of Public Economics, 113, 96-104. https://doi.org/10.1016/j.jpubeco.2014.01.005

Akerlof, G. A., & Kranton, R. E. (2000). Economics and Identity. The Quarterly Journal of Economics, 115(3), 715-753. https://doi.org/10.1162/003355300554881

Aral, S., & Eckles, D. (2019). Protecting elections from social media manipulation. Science, 365(6456), 858-861. https://doi.org/ 10.1126/science.aaw8243

Bail, C. A., Argyle, L. P., Brown, T. W., Bumpus, J. P., Chen, H., Hunzaker, M. F., ..., & Volfovsky, A. (2018). Exposure to opposing views on social media can increase political polarization. Proceedings of the National Academy of Sciences, 115(37), 9216- 9221. https://doi.org/10.1073/pnas.1804840115

Baron, D. P. (1994). Electoral competition with informed and uninformed voters. American Political Science Review, 88(1), 33- 47. https://doi.org/10.2307/2944880

Benabou, R., & Tirole, J. (2006). Incentives and Prosocial Behavior. American Economic Review, 96(5), 1652-1678. https://doi.org/ 10.1257/aer.96.5.1652

Bernhardt, D., Krasa, S., & Polborn, M. (2008). Political polarization and the electoral effects of media bias. Journal of Public Economics, 92(5/6), 1092-1104. https://doi.org/10.1016/j.jpubeco. 2008.01.006

Besley, T., & Case, A. (2003). Political Institutions and Policy Choices: Evidence from the United States. Journal of Economic Literature, 41(1), 7-73. https://doi.org/10.1257/jel.41.1.7

Bianco, W. T., & Canon, D. T. (2021). American Politics Today (7th ed.). Norton.

Bode, L. (2016). Pruning the news feed: Unfriending and unfollowing political content on social media. Research & Politics, 3(3). https://doi.org/10.1177/2053168016661873

Boxell, L., Gentzkow, M., & Shapiro, J. M. (2020). Cross-country trends in affective polarization (NBER Working paper 26669). National Bureau of Economic Research. https://doi.org/10.3386/ w26669

Chan, J., & Suen, W. (2008). A spatial theory of news consumption and electoral competition. The Review of Economic Studies, 75(3), 699-728. https://doi.org/10.1111/j.1467-937x.2008.00495.x

Converse, P. E. (1962). Information flow and the stability of partisan attitudes. Public Opinion Quarterly, 26(4), 578-599. https://doi.org/10.1086/267129

DiMaggio, P., Evans, J., & Bryson, B. (1996). Have American’s social attitudes become more polarized? American Journal of Sociology, 102(3), 690-755. https://doi.org/10.1086/230995

Esteve Del Valle, M., Broersma, M., & Ponsioen, A. (2022). Political interaction beyond party lines: Communication ties and party polarization in parliamentary twitter networks. Social Science Computer Review, 40(3), 736-755. https://doi.org/10.1177/ 0894439320987569

Fernbach, P. M., & Van Boven, L. (2022). False polarization: Cognitive mechanisms and potential solutions. Current Opinion in Psychology, 43, 1-6. https://doi.org/10.1016/j.copsyc.2021.06.005

Flamino, J., Galezzi, A., Feldman, S., Macy, M. W., Cross, B., Zhou, Z., Serafino, M., Bovet, A., Makse, H. A., & Szymanski, B. K. (2021). Shifting polarization and Twitter news influencers between two U.S. presidential elections. Available at https://ui.adsabs. harvard.edu/abs/2021arXiv211102505F

Glaeser, E. L., Ponzetto, G. A. M., & Shapiro, J. (2005). Strategic extremism: Why Republicans and Democrats divide on religious values. Quarterly Journal of Economics, 120(4), 1283-1330. https://doi.org/10.1162/003355305775097533

Graber, D. A., & Dunaway, J. (2018). Mass media and American politics (10th ed.). SAGE

Grossman, G. M., & Helpman, E. (1996). Electoral Competition and Special Interest Politics. Review of Economic Studies, 63(2), 265- 286. https://doi.org/10.2307/2297852

Grossman, G. M., & Helpman, E. (2020). Electoral competition with fake news (NBER Working paper 26409). National Bureau of Economic Research. https://doi.org/10.3386/w26409

Haelle, T. (2014). Democrats have a problem with science, too. Politico. https://www.politico.com/magazine/story/2014/06/ democrats-have-a-problem-with-science-too-107270

Jurkowitz, M., Mitchell, A., Shearer, E., & Walker, M. (2020). U.S. Media polarization and the 2020 election: A nation divided. Pew Research Center. https://www.journalism.org/2020/01/24/u-smedia-polarization-and-the-2020-election-a-nation-divided/

Kinder, D. R. (2003). Communication and politics in the age of information. In Oxford handbook of political psychology (pp. 357- 393). Oxford University Press.

Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS

Quarterly, 44(4), 1619-1649. https://doi.org/10.25300/misq/2020 16371

Levendusky, M. S., & Malhotra, N. (2016). (Mis)perceptions of partisan polarization in the American public. Public Opinion Quarterly, 80, 378-391. https://doi.org/10.1093/poq/nfv045

Mallipeddi, R. R., Kumar, S., Sriskandarajah, C., & Zhu, Y. (2022). A framework for analyzing influencer marketing in social networks: selection and scheduling of influencers. Management Science, 68(1), 75-104. https://doi.org/10.1287/mnsc.2020.3899

Moral, M., & Best, R. E. (2023). On the relationship between party polarization and citizen polarization. Party Politics, 29(2), 229- 247. https://doi.org/10.1177/13540688211069544

Mousavi, R., & Gu, B. (2019). The impact of Twitter adoption on lawmakers’ voting orientations. Information Systems Research, 30(1), 133-153. https://doi.org/10.1287/isre.2018.0791

Mullainathan, S., & Shleifer, A. (2005). The market for news. American Economic Review, 95(4), 1031-1053. https://doi.org/ 10.1257/0002828054825619

Oliveros, S., & Vardy, F. (2015). Demand for slant: How abstention shapes voters’ choice of news media. Economic Journal, 125(587), 1327-1368. https://doi.org/10.1111/ecoj.12169

Pei, A., & Mayzlin, D. (2022). Influencing social media influencers through affiliation. Marketing Science, 41(3), 593-615. https://doi. org/10.1287/mksc.2021.1322

Petrova, M., Sen, A., & Yildirim, P. (2021). Social media and political contributions: The impact of new technology on political competition. Management Science, 67(5), 2997-3021. https://doi. org/10.1287/mnsc.2020.3740

Piolatto, A., & Schuett, F. (2015). Media competition and electoral politics. Journal of Public Economics, 130, 80-93. https://doi.org/ 10.1016/j.jpubeco.2015.04.003

Prior, M. (2007). Post-broadcast democracy: how media choice increases inequality in political involvement and polarizes elections. Cambridge University Press.

Rathore, A. K., Kar, A. K., & Ilavarasan, P. V. (2017). Social media analytics: Literature review and directions for future research. Decision Analysis, 14(4), 229-249. https://doi.org/10.1287/deca. 2017.0355

Santos, F. P., Lelkes, Y., & Levin, S. A. (2021). Link recommendation algorithms and dynamics of polarization in online social networks. PNAS, 118(50), 1-9. https://doi.org/10.1073/pnas.2102141118

Schultz, C. (2008). Information, polarization and term length in democracy. Journal of Public Economics, 92(5-6), 1078-1091. https://doi.org/10.1016/j.jpubeco.2007.12.008

Shore, J., Baek, J., & Dellarocas, C. (2018). Network structure and patterns of information diversity on Twitter. MIS Quarterly, 42(3), 849-872. https://doi.org/10.25300/misq/2018/14558

Sobbrio, F. (2015). Citizen-editors’ endogenous information acquisition and news accuracy. Journal of Public Economics, 113, 43-53. https://doi.org/10.1016/j.jpubeco.2014.03.007

Soberman, D., & Sadoulet, L. (2007). Campaign spending limits and political advertising. Management Science, 53(10), 1521-1532. https://doi.org/10.1287/mnsc.1070.0717

Stromberg, D. (2015). Media and politics. Annual Review of Economics, 7(1), 173-205. https://doi.org/10.1146/annureveconomics-080213-041101

Turcotte, J., York, C., Irving, J., Scholl, R. M., & Pingree, R. J. (2015). News recommendations from social media opinion leaders: Effects on media trust and information seeking. Journal of Computer-

Mediated Communication, 20(5), 520-535. https://doi.org/ 10.1111/jcc4.12127

Tyagi, A., Field, A., Lathwal, P., Tsvetkov, Y., & Carley, K. M. (2020). A computational analysis of polarization on Indian and Pakistani social media. In Proceedings of the International Conference on Social Informatics. https://doi.org/10.1007/978-3-030-60975- 7\_27

Wittman, D. (1983). Candidate motivation: A synthesis of alternative theories. The American Political Science Review, 77, 142-157. https://doi.org/10.2307/1956016

## About the Authors

Chao Ding is principal lecturer in the Faculty of Business and Economics at The University of Hong Kong. His research concentrates on social media, information goods, e-commerce, and platform economy. His works have appeared in Production and Operations Management, Manufacturing & Service Operations Management, Journal of the Association for Information Systems, Decision Support Systems, and other outlets. ORCID 0000-0001- 7101-140X.

Wael Jabr is an assistant professor of supply chain and information systems at the Smeal College of Business, Pennsylvania State University. His research has been awarded multiple national grants and received several Best Paper awards. He frequently serves as associate editor at the International Conference on Information Systems and is currently an associate editor at the Journal of Business & Information Systems Engineering. ORCID 0000-0001- 5850-5077.

Hong Guo is a professor of information systems at Arizona State University. Hong studies emerging IS phenomena (such as digital platforms, digital games, algorithmic interpretability, net neutrality, and business data visualization) and firms’ corresponding strategies. Hong’s research has been published in top business journals such as MIS Quarterly, Information Systems Research, Manufacturing & Service Operations Management, and Production and Operations Management. Her work was recognized with the INFORMS ISS Sandy Slaughter Early Career Award in 2018. She currently serves as an associate editor for Information Systems Research and as a senior editor for Production and Operations Management. She also served as an associate editor for MIS Quarterly in 2017-2020.ORCID 0000-0001-6028-8155.

## Appendix

## Proof of Proposition 1

Citizens’ information consumption is as follows:

Do not consume information $\begin{array} { r } { x + \delta < \frac { p _ { D } + m _ { 1 } } { 2 } } \end{array}$

Read news reports by $m _ { 1 }$

$$
\frac {p _ {D} + m _ {1}}{2} \leq x + \delta <   \frac {m _ {1} + p _ {R}}{2},
$$

Read news reports by $m _ { 2 }$

$$
\frac {p _ {D} + m _ {2}}{2} \leq x + \delta <   \frac {m _ {2} + p _ {R}}{2},
$$

Do not consume information $\begin{array} { r } { x + \delta \ge \frac { m _ { 2 } + p _ { R } } { 2 } . } \end{array}$

Then, parties’ winning probabilities can be derived as follows:

$$
\operatorname{Prob} [ I _ {D} = 1 \mid \theta ] = 1 - \operatorname{Prob} [ I _ {R} = 1 \mid \theta ] = \left\{ \begin{array}{l l} 1 / 2 & \theta <   p _ {D}, \\ G \left[ \frac {p _ {D} + m _ {1}}{2} - \mu \right] & p _ {D} \leq \theta <   m _ {1}, \\ G \left[ \frac {m _ {1} + m _ {2}}{2} - \mu \right] & m _ {1} \leq \theta <   m _ {2}, \\ G \left[ \frac {m _ {2} + p _ {R}}{2} - \mu \right] & m _ {2} \leq \theta <   p _ {R}, \\ 1 / 2 & \theta \geq p _ {R}. \end{array} \right.
$$

Media outlet ?? chooses editorial position ??<sub>??</sub> to maximize its expected utility:

$$
\max _ {m _ {1}} \pi_ {1} = \Big (H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right] \Big) + (1 - \alpha) \Big (H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] \Big),
$$

$$
\max _ {m _ {2}} \pi_ {2} = \Big (H \left[ \frac {m _ {2} + p _ {R}}{2} \right] - H \left[ \frac {m _ {1} + p _ {R}}{2} \right] \Big) + (1 - \alpha) \Big (H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] \Big).
$$

Party ?? chooses policy position $p _ { i }$ to maximize its expected utility:

$$
\max _ {p _ {i}} v _ {i} = \int_ {0} ^ {1} \left(\sum_ {I _ {i} \in \{0, 1 \}} v _ {i} [ \theta , I _ {i} ] \cdot \operatorname{Prob} [ I _ {i} \mid \theta ]\right) d \theta ,
$$

s.t. $\textstyle \sum _ { I _ { i } \in \{ 0 , 1 \} } v _ { i } [ \theta , I _ { i } ] \cdot \operatorname { P r o b } [ I _ { i } \mid \theta ]$ is the same for choosing ?? and ?? at $\theta = p _ { i }$

The constraint represents that party ?? is indifferent between choosing policy ?? and ?? when the state is $p _ { i } .$ . Parties and outlets solve their own optimization problems, which yields Proposition 1.

## Proof of Proposition 2

Under the territory-sharing (TS) strategy, citizens’ information consumption is as follows:

Do not consume information $\begin{array} { r } { x + \delta < \frac { p _ { D } + m _ { 1 } } { 2 } } \end{array}$

Read news reports by $m _ { 1 }$

$$
\frac {p _ {D} + m _ {1}}{2} \leq x + \delta <   \frac {m _ {1} + p _ {R}}{2},
$$

Read news reports by $s _ { 1 }$

$$
\frac {p _ {D} + s _ {1}}{2} \leq x + \delta <   \frac {s _ {1} + p _ {R}}{2},
$$

Read news reports by $s _ { 2 }$

$$
\frac {p _ {D} + s _ {2}}{2} \leq x + \delta <   \frac {s _ {2} + p _ {R}}{2},
$$

Read news reports by $m _ { 2 }$

$$
\frac {p _ {D} + m _ {2}}{2} \leq x + \delta <   \frac {m _ {2} + p _ {R}}{2},
$$

<sub>{</sub>Do not consume information $\begin{array} { r } { x + \delta \ge \frac { m _ { 2 } + p _ { R } } { 2 } . } \end{array}$

Then, parties’ winning probabilities can be derived as follows:

$$
\operatorname{Prob} [ I _ {D} = 1 \mid \theta ] = 1 - \operatorname{Prob} [ I _ {R} = 1 \mid \theta ] = \left\{ \begin{array}{l l} 1 / 2 & \theta <   p _ {D}, \\ G \left[ \frac {p _ {D} + s _ {1}}{2} - \mu \right] & p _ {D} \leq \theta <   s _ {1}, \\ G \left[ \frac {s _ {1} + m _ {1}}{2} - \mu \right] & s _ {1} \leq \theta <   m _ {1}, \\ G \left[ \frac {m _ {1} + m _ {2}}{2} - \mu \right] & m _ {1} \leq \theta <   m _ {2}, \\ G \left[ \frac {m _ {2} + s _ {2}}{2} - \mu \right] & m _ {2} \leq \theta <   s _ {2}, \\ G \left[ \frac {s _ {2} + p _ {R}}{2} - \mu \right] & s _ {2} \leq \theta <   p _ {R}, \\ 1 / 2 & \theta \geq p _ {R}. \end{array} \right.
$$

Media outlet ?? chooses editorial position $m _ { j }$ to maximize its expected utility:

$$
\begin{array}{r l} & {\underset {m _ {1}} {\max} \pi_ {1} = (1 - \alpha) \left(H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right]\right) + (1 - 2 \alpha) \left(H \left[ \frac {p _ {D} + s _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] + H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {s _ {1} + p _ {R}}{2} \right]\right) + (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right),} \\ & {H \left[ \frac {p _ {D} + s _ {2}}{2} \right]),} \end{array}
$$

$$
\begin{array}{l} \max _ {m _ {2}} \pi_ {2} = (1 - 2 \alpha) \left(H \left[ \frac {p _ {D} + s _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {2}}{2} \right] + H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {s _ {1} + p _ {R}}{2} \right]\right) + (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right) + (1 - \alpha) \left(H \left[ \frac {m _ {2} + p _ {R}}{2} \right] - H \left[ \frac {s _ {2} + p _ {R}}{2} \right]\right). \\ H \left[ \frac {m _ {1} + p _ {R}}{2} \right]). \end{array}
$$

Social media influencer ?? chooses stated editorial position $s _ { k }$ to maximize their expected utility:

$$
\begin{array}{r l} & {\underset {s _ {1}} {\max} \Pi_ {1} = \int_ {0} ^ {1} \mathrm{Prob} [ I _ {D} = 1 | \theta ] d \theta + \left(H \left[ \frac {p _ {D} + m _ {1}}{2} \right] - H \left[ \frac {p _ {D} + s _ {1}}{2} \right]\right) + (1 - \alpha) \left(H \left[ \frac {p _ {D} + m _ {2}}{2} \right] - H \left[ \frac {p _ {D} + m _ {1}}{2} \right]\right) + (1 - 2 \alpha) \left(H \left[ \frac {p _ {D} + s _ {2}}{2} \right] - H \left[ \frac {p _ {D} + s _ {1}}{2} \right]\right)} \\ & {H \left[ \frac {p _ {D} + m _ {2}}{2} \right]) + (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right) - \beta (s _ {1} - t) ^ {2},} \end{array}
$$

$$
\begin{array}{l} \max _ {s _ {2}} \Pi_ {2} = \int_ {0} ^ {1} \mathrm{Prob} [ I _ {R} = 1 | \theta ] d \theta + \left(H \left[ \frac {s _ {2} + p _ {R}}{2} \right] - H \left[ \frac {m _ {2} + p _ {R}}{2} \right]\right) + (1 - \alpha) \left(H \left[ \frac {m _ {2} + p _ {R}}{2} \right] - H \left[ \frac {m _ {1} + p _ {R}}{2} \right]\right) + (1 - 2 \alpha) \left(H \left[ \frac {m _ {1} + p _ {R}}{2} \right] - H \left[ \frac {s _ {1} + p _ {R}}{2} \right]\right) + \\ (1 - 3 \alpha) \left(H \left[ \frac {s _ {1} + p _ {R}}{2} \right] - H \left[ \frac {p _ {D} + s _ {2}}{2} \right]\right) - \beta (s _ {2} - 1 + t) ^ {2}. \end{array}
$$

Party ?? chooses policy position $p _ { i }$ to maximize its expected utility:

max $\begin{array} { r } { v _ { i } = \int _ { 0 } ^ { 1 } \left( \sum _ { I _ { i } \in \{ 0 , 1 \} } v _ { i } [ \theta , I _ { i } ] \cdot \mathrm { P r o b } [ I _ { i } \mid \theta ] \right) d \theta , } \end{array}$ ??<sub>??</sub>

s.t. $\textstyle \sum _ { I _ { i } \in \{ 0 , 1 \} } v _ { i } [ \theta , I _ { i } ] \cdot \operatorname { P r o b } [ I _ { i } \mid \theta ]$ is the same for choosing ?? and ?? at $\theta = p _ { i }$

Parties, media outlets, and social media influencers solve their own optimization problems, which yields the solution for the TS strategy. Similarly, we can solve for each stakeholder’s decision under the territory-expanding (TE) strategy.

Because we focus on the interesting market conditions under which both the TE and TS strategies have interior solutions, we obtain the boundary conditions when media outlets’ editorial positions are the same as social media influencers’ stated editorial positions. By taking the partial derivative of $( s _ { 1 } ^ { T S } - m _ { 1 } ^ { T S } )$ with respect to parameter ??, we obtain $\frac { \partial \big ( s _ { 1 } ^ { T S } - m _ { 1 } ^ { T S } \big ) } { \partial t } > 0$ . Therefore, $s _ { 1 } ^ { T S } - m _ { 1 } ^ { T S } \geq 0$ when $t \geq \underline { { t } } .$ . This lower bound for ?? is obtained by equating $m _ { 1 } ^ { T S }$ and $\begin{array} { r } { s _ { 1 } ^ { T S } , \mathrm { i . e . , } \underline { { t } } = \frac { 1 6 \beta - ( 1 0 - 4 w + 1 3 2 \beta - 2 4 w \beta ) \alpha + ( 3 9 - 1 8 w + 2 1 6 \beta - 7 2 w \beta ) \alpha ^ { 2 } - ( 3 6 - 1 8 w ) \alpha ^ { 3 } } { 1 6 \beta ( 2 - 9 \alpha + 9 \alpha ^ { 2 } ) } + } \end{array}$ $\frac { ( 3 \alpha ^ { 2 } - 2 \alpha - 1 2 \beta \alpha ) \sqrt { ( 6 ( 1 + w ) \alpha - 2 w - 1 ) ^ { 2 } + 8 w ( 1 - 9 \alpha ^ { 2 } ) } } { 1 6 \beta ( 2 - 9 \alpha + 9 \alpha ^ { 2 } ) }$ . By taking the partial derivative of $( m _ { 1 } ^ { T E } - s _ { 1 } ^ { T E } )$ with respect to parameter ?? , we obtain $\begin{array} { r } { \frac { \partial \left( m _ { 1 } ^ { T E } - s _ { 1 } ^ { T E } \right) } { \partial t } < 0 } \end{array}$ . Therefore, $m _ { 1 } ^ { T E } - s _ { 1 } ^ { T E } \geq 0$ when $t \leq \overline { { t } }$ . This upper bound for ?? is obtained by equating $m _ { 1 } ^ { T E }$ and $s _ { 1 } ^ { T E }$ , i.e., $\overline { { t } } =$ $\frac { 1 6 \beta + ( 1 0 - 4 w - ( 7 6 - 8 w ) \beta ) \alpha - ( 3 3 - 1 4 w - ( 8 4 - 1 6 w ) \beta ) \alpha ^ { 2 } + ( 2 7 - 1 2 w ) \alpha ^ { 3 } } { \texttt { + - 6 0 r - 7 - 5 - 4 . 5 2 5 } } - \frac { \alpha \sqrt { ( 2 - 4 \beta - 3 \alpha ) ^ { 2 } ( ( 1 - 3 \alpha ) ^ { 2 } + 4 w ^ { 2 } ( 1 - 2 \alpha ) ^ { 2 } + 1 2 w ( 1 - 3 \alpha + 2 \alpha ^ { 2 } ) ) } } { \texttt { + - 6 0 r - 7 - 5 - 5 - 2 5 } }$ . Furthermore, we compare 16??(2−7??+6??<sup>2</sup>) 16??(2−7??+6??<sup>2</sup>) social media influencers’ utilities under the two equilibria. By taking the partial derivative of $( \boldsymbol { { \Pi } } _ { 1 } ^ { T E } - \boldsymbol { { \Pi } } _ { 1 } ^ { T S } )$ with respect to parameter ??, we obtain $\begin{array} { r } { \frac { \partial \left( \varPi _ { 1 } ^ { T E } - \varPi _ { 1 } ^ { T S } \right) } { \partial t } > 0 } \end{array}$ . Therefore, $\Pi _ { 1 } ^ { T E } - \Pi _ { 1 } ^ { T S } \geq 0$ when $t \geq \hat { t } _ { 1 }$ . The threshold $\hat { t } _ { 1 }$ is obtained by equating $\Pi _ { 1 } ^ { T S }$ and $\Pi _ { 1 } ^ { T E }$

## Proof of Proposition 3

$$
\begin{array}{l} \text {Case} \quad 1, \quad \text {when} \quad t <   \hat {t} _ {1}, \quad \text {we} \quad \text {have} \quad p _ {D} ^ {B M} = \frac {2 \alpha - 2 w (1 - \alpha) - 1 + \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (1 - \alpha)} \quad \text {and} \quad p _ {D} ^ {T S} = \\ \frac {6 (1 + w) \alpha - 2 w - 1 + \sqrt {(6 (1 + w) \alpha - 2 w - 1) ^ {2} + 8 w (1 - 9 \alpha^ {2})}}{4 (1 - 3 \alpha)}. \text {It follows that} p _ {D} ^ {T S} - p _ {D} ^ {B M} > 0. \\ \text {Case} \quad 2, \quad \text {when} \quad t \geq \hat {t} _ {1}, \quad \text {we} \quad \text {have} \quad p _ {D} ^ {B M} = \frac {2 \alpha - 2 w (1 - \alpha) - 1 + \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (1 - \alpha)} \quad \text {and} \quad p _ {D} ^ {T E} = \\ \frac {6 \alpha - 8 \beta t - 1 + \sqrt {(2 w (1 + 4 \beta - 3 \alpha) - 1 - 8 \beta t + 6 \alpha) ^ {2} + 8 w (1 + 4 \beta - 3 \alpha) (2 + 8 \beta - 3 \alpha)}}{4 (1 + 4 \beta - 3 \alpha)} - \frac {w}{2}. \text {It follows that} p _ {D} ^ {T E} - p _ {D} ^ {B M} > 0. \text {Since} p _ {R} ^ {T S} = 1 - p _ {D} ^ {T S}, p _ {R} ^ {T E} = 1 - p _ {D} ^ {T E}, \text {and} \\ p _ {R} ^ {B M} = 1 - p _ {D} ^ {B M}, \text {we know that} p _ {R} ^ {T S} - p _ {R} ^ {B M} <   0 \text {and} p _ {R} ^ {T E} - p _ {R} ^ {B M} <   0. \end{array}
$$

## Proof of Proposition 4

$$
\begin{array}{l} \text {Case} \quad 1, \quad \text {when} \quad t <   \hat {t} _ {1}, \quad \text {we} \quad \text {have} \quad m _ {1} ^ {B M} = \frac {6 \alpha^ {2} - 1 1 \alpha - 2 \alpha w (1 - \alpha) + 4 - \alpha \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (2 - \alpha) (1 - \alpha)} \qquad \text {and} \qquad m _ {1} ^ {T S} = \\ \frac {- 6 (5 - 3 w) \alpha - 6 w + 5 + 3 \sqrt {(6 (1 + w) \alpha - 2 w - 1) ^ {2} + 8 w (1 - 9 \alpha^ {2})}}{8 (2 - 3 \alpha)}. \text {It follows that} m _ {1} ^ {B M} - m _ {1} ^ {T S} > 0. \end{array}
$$

$$
\text {Case} \quad 2, \quad \text {when} \quad t \geq \hat {t} _ {1}, \quad \text {we} \quad \text {have} \quad m _ {1} ^ {B M} = \frac {6 \alpha^ {2} - 1 1 \alpha - 2 \alpha w (1 - \alpha) + 4 - \alpha \sqrt {\left((2 \alpha - 1) - 2 w (1 - \alpha)\right) ^ {2} + 8 w (1 - \alpha) (1 + \alpha)}}{4 (2 - \alpha) (1 - \alpha)} \quad \text {and} \quad m _ {1} ^ {T E} =
$$

$\frac { 6 ( 5 - w ) \alpha ^ { 2 } + ( 8 ( t + w - 6 ) \beta + 2 w - 2 3 ) \alpha + 4 ( 1 + 4 \beta ) - } { 4 ( 1 + 4 \beta - 2 \alpha ) ( 7 - 2 \alpha ) } - \frac { \alpha \sqrt { ( 1 + 8 t \beta - 6 \alpha ) ^ { 2 } + 4 w ( 3 + 8 ( 2 - t ) \beta ) ( 1 + 4 \beta - 3 \alpha ) + 4 w ^ { 2 } ( 1 + 4 \beta - 3 \alpha ) ^ { 2 } } } { A ^ { \prime } + 4 A ^ { \prime } \beta - 2 \alpha \Upsilon / 2 - 2 \alpha ) }$ . It follows that $m _ { 1 } ^ { B M } - m _ { 1 } ^ { T E } > 0$ . Since 4(1+4??−3??)(2−3??) 4(1+4??−3??)(2−3??) $m _ { 2 } ^ { T S } = 1 - m _ { 1 } ^ { T S } , m _ { 2 } ^ { T E } = 1 - m _ { 1 } ^ { T E }$ , and $m _ { 2 } ^ { B M } = 1 - m _ { 1 } ^ { B M }$ , we know that $n _ { 2 } ^ { B \dot { M } } - m _ { 2 } ^ { T S } < 0 \mathrm { a n d } m _ { 2 } ^ { B M } - m _ { 2 } ^ { T E } < 0$

## Proof of Proposition 5

$$
\begin{array}{l} \text {Case 1, when t <   \hat {t} _{1} , we have DPO^{BM} = \frac {(m_{1} ^{BM} - p_{D} ^{BM})(1- m_{1} ^{BM} - p_{D} ^{BM})^{2}}{2} and DPO^{TS} = \frac {(s_{1}^{TS} - p_{D}^{TS})((p_{D}^{TS})^{2} - p_{D}^{TS}(2- s_{1}^{TS}) + 2(1- s_{1}^{TS})^{2} - m_{1}^{TS}(2- p_{D}^{TS} - 3s_{1}^{TS}))}{4} . It}\\ \text {follows that DPO^{TS} -DPO^{BM} <  0.} \end{array}
$$

Case 2, when $t \geq \hat { t } _ { 1 }$ , we have $\begin{array} { r } { D P O ^ { B M } = \frac { ( m _ { 1 } ^ { B M } - p _ { D } ^ { B H } ) ( 1 - m _ { 1 } ^ { B M } - p _ { D } ^ { B M } ) ^ { 2 } } { 2 } \operatorname { a n d } D P O ^ { T E } = \frac { ( m _ { 1 } ^ { T E } - p _ { D } ^ { T E } ) \left( ( m _ { 1 } ^ { T E } ) ^ { 2 } + ( 1 - p _ { D } ^ { T E } ) ^ { 2 } + p _ { D } ^ { T E } s _ { 1 } ^ { T E } - \left( s _ { 1 } ^ { T E } \right) ^ { 2 } - m _ { 1 } ^ { T E } ( 2 - p _ { D } ^ { T E } - s _ { 1 } ^ { T E } ) \right) } { 2 } } \end{array}$ By taking the partial derivative of $D P O ^ { T E }$ with respect to parameter ??, we obtain $\begin{array} { r } { \frac { \partial D P O ^ { T E } } { \partial t } > 0 } \end{array}$ . Additionally, $D P O ^ { B M }$ is independent of ??. Therefore, $D P O ^ { T E } - D P O ^ { B M } \geq 0$ when $t \geq \hat { t } _ { 2 } .$ . The threshold $\hat { t } _ { 2 }$ is obtained by equating $D P O ^ { B M }$ and $D P O ^ { T E }$
