---
otero_id: 4072
otero_key: "KGUU7NJ7"
title: "Polarization or Bias: Take Your Click on Social Media"
authors: "Debabrata Dey; Atanu Lahiri; Rajiv Mukherjee"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00925"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 26 Issue 3 Special Issue: Health Analytics and IS Theorizing (pp. 575-759)

Article 2

2025

# Polarization or Bias: Take Your Click on Social Media

Debabrata Dey, deb.dey@ku.edu

Atanu Lahiri

, atanu.lahiri@utdallas.edu

Rajiv Mukherjee

, rmukherjee@mays.tamu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Polarization or Bias: Take Your Click on Social Media

Debabrata Dey,<sup>1</sup> Atanu Lahiri,<sup>2</sup> Rajiv Mukherjee<sup>3</sup>

<sup>1</sup>University of Kansas, KU School of Business, USA, deb.dey@ku.edu <sup>2</sup>University of Texas at Dallas, Jindal School of Management, USA, atanu.lahiri@utdallas.edu <sup>3</sup> Texas A&M University, Mays Business School, USA, rmukherjee@mays.tamu.edu

## Abstract

A major policy concern emerging in recent years is whether social media platforms, driven completely by profit motivations, create divisions within society and inject bias into their user base. A related question is: How should a policymaker intervene if these allegations prove to be true? In this study, we set up a microeconomic model to study whether a platform’s profit motivation may indeed compel it to adopt a user-targeting strategy that injects bias and creates polarization. We then examined how a policymaker might intervene and whether there are unintended consequences of such interventions. In doing so, we discovered an interesting duality between polarization and bias—both can add to the platform’s coffers but might act as substitutes in its profit function. If policymakers try to crack down on polarization, it could end up making the platform switch to bias instead. Finally, we examined the role of public awareness in moderating the platform’s desire for profit. Our results provide broad insights into a platform’s incentives and contribute to the public debate on this issue.

Keywords: Social Media, Machine Learning, Ethics of AI, Polarization, Bias, Social Welfare

Giri Kumar Tayi was the accepting senior editor. This research article was submitted on April 27, 2024, and underwent two revisions.

“I am deeply concerned that they have made a product that can lead people away from their real communities and isolate them in these rabbit holes and these filter bubbles. What you find is that when people are sent targeted misinformation to a community it can make it hard to reintegrate into wider society because now you don’t have shared facts.”

– Frances Haugen, Testimony at the UK Parliament<sup>1</sup>

## 1 Introduction

Social media platforms bring together millions of highly diverse users—consumers, content providers, advertisers, buyers, and sellers—to interactively share news, information, entertainment, and opinions with one another. Over the last decade or so, these platforms have become an integral part of our day-to-day lives. Recent estimates indicate that about 4.8 billion people around the world (more than 60% of the current world population) make regular use of social media platforms, spending an average of over two hours per day on social media activities (Chaffey, 2023). For many, social media is their only source of news and entertainment and their primary mode of communication.

The early promises of social media were the many benefits that these platforms bring to individuals and societies by keeping them connected, allowing them to communicate freely, and providing them with an opportunity to learn and share information. However, with the rapid increase in the popularity of social media, concerns have arisen about their adverse effects on individuals and on societal welfare at large (e.g., Allcott et al., 2020; Ichihashi & Kim, 2023; Silva & Kenney, 2019). Such adverse effects include, for example, higher rates of addiction, depression, bullying, suicide, anorexia, insomnia, and sleeping disorders, as well as the broader spread of disinformation and fake news. A recent study by the Pew Research Center found that 64% of Americans feel that “social media negatively affect the way things are going in the country today” (Auxier, 2020).

The purpose of this study is to take a closer look at two of the adverse effects, namely polarization and bias. Given two opposing (polarizing) narratives, polarization occurs when users become split along their proattitudinal narratives and start doubting the legitimacy of counter-attitudinal ones,<sup>2</sup> which can create divisions and distrust that may be difficult to bridge (Barberá, 2020; Druckman et al., 2022). Bias occurs when a platform’s user-targeting strategy starts favoring one narrative over its alternative. Since bias may allow one side to foster misinformation and half-truths—while suppressing the other side’s narrative and bypassing fact-checks—bias is clearly detrimental to an open, fair, and unprejudiced society. Moreover, bias can also lead to societal divisions. When a platform becomes biased towards one of two polarizing narratives, users may either flock to it or switch to a competing platform with a different bias, but few would continue to engage with both. Such segregation of the consumer base is quite commonplace in legacy media where, for example, viewers of CNN or MSNBC are likely to ignore/dislike Fox News or Newsmax and vice versa (Gentzkow & Shapiro, 2017). Such segregation may not be immediately visible in social media activities, but the cross talk (also called cross-cutting in the literature) necessary in a balanced conversation may be lost forever. If such bias is also collective in nature, it might lead a “society to a collective failure, in which overall social welfare is harmed” (Luo, 2017, p.78).

Polarization and bias also play an important role in generating and sustaining social media “firestorms.” An online firestorm occurs when an entity—an individual or a group—faces a sudden flurry of negative attention within a digital environment (Pfeffer et al., 2014). According to Chan et al. (2024), such firestorms are mostly triggered by controversial or divisive events. However, even though the event itself might be the incendiary, at a deeper level, a biased and divided user base of a social media platform serves as the perfect landscape for such firestorms to spread. Firestorms are usually laced with hateful and vulgar comments (Matook et al., 2022), creating acrimony within society and often leading to a culture that “cancels”—boycotts, shames, and ostracizes— individuals or firms for seemingly little fault of their own. Social media firestorms can inflict severe stress and monetary losses on individuals and organizations alike (Chan et al., 2024).

Although the issue of polarization was previously largely confined to academic studies (e.g., Andreottola & Li, 2024; Arora et al., 2022; van Bavel et al., 2021), it has recently started appearing in the popular press as well and has thus entered the arena of active public discourse and policy debate. For example, in October 2021, first in an interview with CBS News,<sup>3</sup> and later in her sworn testimonies before the US Senate and UK Parliament, Frances Haugen, a whistleblower, alleged that Facebook (now Meta) was “creating division” and “promoting hate” and that Facebook was intentionally doing so because it was not willing to sacrifice even a “slither of profit” (Brown & Snider, 2021; Tingle et al., 2021). In other words, Facebook, the leading social media company, was allegedly putting profits before the welfare of its own consumer base. Comparing Facebook’s actions to those of polluting oil companies, Haugen recommended that Facebook should do more to stop and censor hate speech and misinformation, even though doing so might hurt its profits. Of course, Haugen is not alone in her criticism of social media. During Haugen’s testimony before the US Senate, in a somewhat rare moment of bipartisan convergence, senators from both sides of the aisle raised concerns about the numerous ills of social media (Mak, 2021).

What is important about the latest allegations against social media platforms such as Facebook is not just that they create division within society—or that they are biased—but also that such division or bias is a direct outcome of their profit motivation. When a platform is motivated only by its profits and when polarization or bias generates more profit, the platform has no incentive to take steps towards curbing the hazard. <sup>4</sup> Therefore, from the perspective of public policy, it is important that we develop a quantitative understanding of the profit calculus of polarization and bias in order to better understand the extent of the platform’s incentive and to inform the debate on how to bridge the societal division that a platform might end up creating.

The main source of revenue for a social media platform is advertising.<sup>5</sup> If a platform can keep its users engaged for longer periods of time, it will naturally attract more advertisements and earn higher ad revenues. Currently, platforms rely on their predictive analytics abilities— typically based on machine learning and/or artificial intelligence—to nudge users in directions that will keep them engaged or, as some argue, even hooked/addicted (e.g., Alter, 2018). They can do this by simply tracking users’ activities and analyzing that data through sophisticated algorithms to learn what keeps users engaged. They can then employ that knowledge to selectively show/recommend certain personalized content to each user in a manner that is likely to keep them engaged. Critics argue that, in so doing, social media platforms create “echo chambers” where users are nudged towards only one side of the story—the one that they are more likely to engage with—the end result being an unbridgeable division among them (Cinelli et al., 2021; Settle, 2018).

To understand whether such polarization or bias can indeed materialize from a platform’s profit motivation, we develop a parsimonious microeconomic model of a platform, its recommendation engine, and its heterogeneous base of users and content providers. Our objective is to study whether platforms have economic incentives to behave in a biased or polarizing manner. Through this exercise, we expect to understand what type of policy or market mechanism may mitigate such issues. As positivists, it is not our place to take a hard ethical/normative stand, one way or the other. Rather, we seek to study the important components of platforms’ incentives in this regard and verify if there could be unintended consequences of any intervention by a policymaker. Put differently, we do not seek to verify if the allegations of division and bias are true. Rather, we want to understand if social media platforms have any economic reason to behave in a divisive or biased manner; whether or not they act upon those incentives is beyond the scope of this study.

We found that a platform’s profit motivation could indeed lead it to a nudging (or targeting) strategy that materializes in a higher level of polarization. At the same time, however, when left alone to maximize its profit, a social media platform has little incentive to behave in a biased manner, even in a market with inherent asymmetry and bias. In stark contrast, if policymakers compel a social media platform to curb polarization (say, by levying a tax or imposing a penalty), the platform may comply, but doing so could also lead it to become more biased. This duality between polarization and bias as a means to generate profit is at the heart of the issue: Our findings show that left alone or faced with a small penalty, platforms will use polarization, but when facing substantial penalties, platforms will switch to using bias as their profit generator. Seen in this way, from the perspective of social cohesion and harmony, social media may be a double-edged sword, inflicting harm either way, whether policymakers intervene or not.

The story, however, takes a compelling turn when users become aware of the hazards of polarization and bias. When users start internalizing some of the societal costs—and displaying sufficient resistance towards division and bias—a platform may be forced to change its nudging strategy to one that mitigates both these issues. Since direct interventions, in and of themselves, could have the unintended consequence of injecting bias, policymakers should not rush to impose them. Interestingly, the issues could perhaps be more easily resolved if policymakers intervene somewhat indirectly instead, say, by seeking to foster awareness and educate the public. However, if a sufficiently high level of awareness cannot be attained, policymakers may still be able to move platforms toward a socially desirable outcome where both polarization and bias are mitigated. This can be accomplished by combining education (awareness) with a moderate—that is, not too high or too low—level of fiscal intervention.

## 2 Literature Review

The role of social media in abetting polarization and bias within society is a topic of interest for both scholars and policymakers (Allcott et al., 2019; Barberá, 2020; van Bavel et al., 2021). The prevailing notion is that in order to increase user engagement, social media platforms deliver content that is personalized, which then leads to the formation of “filter bubbles,” where content is filtered by algorithms so that recommendations are wellaligned with users’ past interactions and engagements (Pariser, 2012). As a result, users of social media platforms often end up participating in “echo chambers,” engaging mostly with like-minded people who cater to similar belief systems (Settle, 2018; Sunstein, 2018). Arora et al. (2022) found that polarizing content makes users self-select into echo chambers with extreme views and decreases their engagement with opposing views. The issue of these echo chambers is significant because, given a dearth of amphibious views, a “viral” rate of content dissemination and an amplification of responses in the form of “emotional contagion” can induce the residents of such echo chambers to become heavily polarized (Kramer et al., 2014; Sunstein, 2018).

In such a polarized environment, where individuals strongly believe in their pro-attitudinal narratives, the consumption of information is limited to sources that align with their belief systems, exacerbating divisions within society. In fact, when polarizing narratives enjoy unquestioned acceptance from users, social media platforms have the potential to become breeding grounds for misinformation (Brady et al., 2017, 2020). In the absence of sufficient verification of account registrations on social media platforms, computerized virtual agents mimicking human users, often called bots, may be used to disseminate false/biased narratives and deepen polarization even further (Allcott et al., 2019; Azzimonti & Fernandes, 2023).

Two types of polarization have been identified in the literature: (1) ideological, and (2) affective or psychological (Iyengar & Hahn, 2009; Settle, 2018). When polarization is ideological, it is limited to only the divergence of views, but when it becomes affective, people tend to increasingly dislike and distrust one another and perceive that the social distance between them has expanded (Barberá, 2020). Affective polarization creates a level of animus that individuals feel toward those who disagree with them (Overgaard & Wooley, 2022). Both sides become so entrenched in their views that, in essence, they start dismissing the other side as fake, thereby forming a barrier to shared experience and allowing misinformation to metastasize easily and rapidly (Brady et al., 2017, 2020). Although affective polarization is clearly the worst of the two types, we do not differentiate between the two in our study. For, prolonged disagreement on views or frequent exposure to counter-attitudinal information can make people dig in, eventually giving rise to affective polarization (Bail et al., 2018). Similar observations about ideological polarization morphing into affective have also been made by Arora et al. (2022) and Suhay et al. (2018).

Prior literature has also examined how to combat polarization and bias in social media. Diakopoulos (2015), for instance, proposed the notion of algorithmic accountability as a way to reduce polarization: By disclosing their content recommendation algorithms, social media platforms can enable users to understand why they are seeing what they are seeing on the platform. Such algorithmic transparency could help reduce the formation of echo chambers and filter bubbles (Bakshy et al., 2015; Lu, 2021). To combat the rise of misinformation, some social media platforms have also implemented fact-checking mechanisms to curb the dissemination of fake news (Pennycook et al., 2020; Tene & Polonetsky, 2013; Zhou & Zafarani, 2020). Further, many platforms have implemented automated mechanisms to moderate content (Guess et al., 2020). Researchers have also suggested the use of rewards as a mechanism to support positive engagements and discourage toxic behavior on social media platforms (Tukekci, 2017). Finally, there has also been a focus on digital literacy for social media users (Broniatowski et al., 2018). On this front, there could be a collaboration between the government and social media companies to take responsibility for making sure users on the platform are aware of a ground reality. As of now, though, such socially aware platforms are far from being realized.

The literature on the impact of social media—and social networks in a broader sense—on polarization and bias is vast, and it is not possible to provide a complete review here. Interested readers should consult the excellent survey by Barberá (2020) and the literature cited therein. While it builds on prior literature, our study is also quite different. We wish to scrutinize polarization and bias under a microeconomic lens to closely follow the incentives of different parties. In order to do so, we set up a parsimonious model to study how a platform’s nudging strategy influences polarization and bias, whether platforms have incentives to curb these adverse effects on their own, if a policy intervention is at all necessary, and whether such interventions could have unintended consequences. As we discovered, social media platforms, when left to their own devices, have a tendency to exacerbate polarization but not bias. However, when policymakers intervene to curb this polarization, platforms may end up injecting bias, effectively replacing one hazard with another. In this way, our study provides a broader perspective that is missing in the prior literature—a perspective that is evidently necessary to inform the current policy debate.

Our study is also related to the more general topic of the ethics of AI (artificial intelligence). In recent times, there has been a lot of discussion on whether AI leads to outcomes that raise ethical concerns. Social media platforms deploy many of the same algorithmic techniques as AI to classify users and nudge them in different directions. Therefore, the ethics of (AI-driven) recommendation engines are at the heart of the overall debate (Fu et al., 2022; Lambrecht & Tucker, 2019; Yuan et al., 2023). The concept of algorithmic bias— notwithstanding whether or not it is present in social media platforms—has received much attention in the literature (e.g., Etzioni & Etzioni, 2017; Fazelpour & Danks, 2019; Panch et al., 2019); in particular, opaque deep-learning methods that sacrifice interpretability in search for higher accuracy have often been accused of having implicit biases (Barberá, 2020; Lu, 2021). The focus of our study is different, though. We do not study how a platform could make its AI more ethical but examine whether it has any incentive to do so in the first place.

We close this section by recognizing a curious similarity between our context (awareness vs. intervention) and the debate about education vs. enforcement. The notion of employing education and/or enforcement measures to counter the noncompliance of a law or policy is not new, and both approaches have been employed in the past— sometimes together and sometimes one at a time—to curb many types of illegal behavior, such as tobacco sales to minors, alcoholism, drunk driving, and drug abuse (e.g., Feighery et al., 1991). In our context, fostering awareness among users is akin to providing education, and intervention is akin to enforcement. Like prior literature that has found that education and enforcement complement each other in curbing noncompliant behavior, we also found that awareness and intervention can work hand in hand to curb polarization and bias generated by social media platforms. There is a difference, though. In our context, education is the primary driver rather than enforcement as in prior literature. For example, when the noncompliance of organizational security policies is rampant, organizations should invest in enforcement before education (Dey et al., 2021). However, in our setting, if polarization is excessive and awareness among users low, policymakers should first foster awareness. Only if that does not adequately mitigate the issue should policymakers add moderate levels of fiscal intervention.

## 3 Model and Analyses

We consider a social media platform with a large number of subscribers and many content providers. Naturally, such a platform would deal with a wide variety of topics, of which we focus on a subset—the set of topics that have two starkly contrasting narratives, A and B, and, therefore, have the potential of creating division.<sup>6</sup> We can think of these narratives as situated at two different extremes of a continuum, denoted by a horizontal [0,1] line, as shown in Figure 1. The point to note here is that this [0,1] interval, although somewhat similar to a traditional Hotelling line, is also different from it. Analogous to the Hotelling setup, our users are also uniformly distributed over [0,1], but their locations now represent their proclivities towards a narrative. We will discuss this point in the next subsection, but let us first consider the timeline of events.

The game starts when a user initiates a session with a social media platform. At that point, the platform makes a recommendation to the user to nudge him in one of the two directions. The user now has two choices: He can either accept the nudge and engage, or he can ignore it altogether. If he ignores it, he can quit without engaging or look on his own for content to engage with.

## 3.1 User Behavior

In our setting, users are distributed over two orthogonal dimensions, ?? and ?? ; please see Figure 1. A user situated at ?? has a proclivity of ?? towards B; that is, he prefers to engage with Narrative B an ?? fraction of the time and with A, an 1 − ?? fraction. Naturally, all users with $x < \%$ lean more towards Narrative A, and those with ?? > ½ , towards B. We label the first group as Atype and the second as B-type; the zero mass at ?? = ½ can be added to either group or ignored altogether.

Our users are also heterogeneous in the “pleasure” (benefit) they derive when engaging, denoted as ?? ∈ [0, 1] in Figure 1. When nudged by the platform, user ⟨??, ??⟩ may accept the nudge to enjoy a benefit of ??. Whether or not user ⟨??, ??⟩ accepts a nudge depends only on his proclivity index, ?? , as follows: when nudged towards Narrative A, he accepts it with probability 1 − ?? , and when nudged towards B, he accepts with probability ??. If the user does not accept the nudge, he may still engage by searching or scrolling to look for content. When looking for content himself, whether he engages with A or B is again determined by his proclivity index, ??; he engages with Narrative A (Narrative B) with probability 1 − ?? (probability ??).

We also assume that the user incurs a search cost of ?? when he does not accept the platform’s nudge and looks for content himself, so he would now get to enjoy a net benefit of only ?? − ??. Users with ?? > ?? would be willing to incur ?? and are denoted as active users in Figure 1; clearly, a 1 − ?? fraction of users would belong to this category (see Figure 1). The remaining ?? fraction—comprising users with ?? ≤ ??—would find it excessively taxing to look for content and would refrain from doing so; hence, they would engage only when they accept the platform’s nudge and not otherwise. The users belonging to this ??-fraction are labeled passive in Figure 1. In summary, if a user accepts the recommendation, he engages with the narrative the platform nudges him to, but if he does not, he may engage with either narrative (depending on his proclivity) or not engage at all. Formally:

Assumption 1: Social media users are indexed by ⟨??, ??⟩, the first index indicating a user’s proclivity towards Narrative B and the second, the user’s benefit from engaging. Users are uniformly distributed over the unit square spanned by ?? and ??. All users incur a search cost of ?? ∈ (0, 1) when looking for appropriate content to engage with.

![](/api/attachments/KGUU7NJ7/fulltext/images/6e896be60bb96cfdb38703bf961115d811840541b8e9d27f9d8b87b88c040b3d.jpg)  
Figure 1. Users are Distributed over a Unit Square

![](/api/attachments/KGUU7NJ7/fulltext/images/436a1683c34ba15af333f138f2f5a9e7c18dd8c5800ca137e1b108feba205a77.jpg)  
Figure 2. Recommendation Engine and Nudging Strategy

## 3.2 Recommendation Engine

We now model the recommendation engine that the platform deploys to nudge its users in directions that would likely keep them engaged. For example, the platform may nudge a user towards a certain narrative by pushing selective information to the user—such as news feeds, recommended articles, highlighted posts, and fact checks—that supports the narrative. Even though the actual location (proclivity) of a user may not be known, it does not really matter to the platform. This is because, as far as the platform is concerned, it is a case of binary classification. Based on the user’s past activities (and recorded behavior), the platform’s algorithm can simply classify each user as either A- or B-type. In Figure 2, these predictions by the classifier are represented in lower case, as ?? and ??, respectively.

Now, even though the classifier can predict a user’s type (?? or ??) fairly accurately, this accuracy, denoted $\sigma = { \mathrm { P r } } [ a | { \mathrm { A } } ] { \mathrm { - o r } } \sigma = { \mathrm { P r } } [ b | { \mathrm { B } } ]$ ] as the case may be— would likely not be 100%, especially for users who are near the middle and show comparable proclivities towards both narratives. In fact, at $\begin{array} { r } { x = \frac { 1 } { 2 } , } \end{array}$ the user has exactly the same proclivity towards either narrative, so the classifier can do no better than a random coin toss when $\textstyle x = { \frac { 1 } { 2 } }$ . At the same time, it should be easier for the classifier to make correct predictions near the two extremes, $x = 0$ and $x = 1$ . In other words, $\sigma ( x )$ should be an increasing function of $\left| { \frac { 1 } { 2 } } - x \right|$ . We use the quadratic form:

Assumption 2: The classifier’s accuracy about user $x ' s$ type is $\begin{array} { r } { \sigma ( x ) = \frac { 1 } { 2 } + 2 \rho \left( \frac { 1 } { 2 } - x \right) ^ { 2 } } \end{array}$ , where $\rho \in [ 0 , 1 ]$ is a parameter representing the discriminating power of the classifier.

According to Assumption 2, the classifier’s accuracy is the highest at the two extremes and lowest at the middle: $\ \sigma ( 0 ) = \sigma ( 1 ) = { \frac { 1 + \rho } { \ 2 \ } }$ and $\begin{array} { r } { \sigma ( \frac { 1 } { 2 } ) = \frac { 1 } { 2 } . } \end{array}$

## 3.3 Nudging Strategy

If the platform were to rely fully on its recommender system, it should nudge all users classified as ?? towards Narrative A and all classified as ?? towards B. However, such a strategy could reduce users’ exposure to diverse content, especially if the recommendation engine is any good, that is, $\mathrm { i f } \rho$ is sufficiently high. For social media platforms, this could be an issue; so, to achieve some diversity, the platform might mix things up a little. As shown in the tree in Figure 2, the platform can do so by nudging an ?? fraction of cases classified as ?? towards Narrative B and a $\beta$ fraction of cases classified as ?? towards A. This way, the platform adheres to the recommender system only an $1 - \alpha - \beta \ge 0$ fraction of the time. <sup>7</sup> Viewed differently, the platform has two independent diversity levers in ?? and ?? by which it can discourage the formation of echo chambers and maintain a public image of fostering diversity.

If the platform chooses some $\alpha \neq \beta$ , the difference would manifest itself as the platform’s bias towards one narrative or the other. For example, if $\beta > \alpha$ platform’s nudges towards Narrative $\mathbf { A }$ outnumbers those towards B by $\frac { \beta - \alpha } { 2 }$ . Likewise, if $\alpha > \beta$ , nudges towards B would be higher by a factor of $\frac { \alpha - \beta } { 2 }$ Therefore, a platform’s bias towards one or the other narrative can be quantified as $\vert \alpha - \beta \vert$ , and if fully unbiased, a platform ought to set $\alpha = \beta$

Definition 1 (bias): When a platform adopts a strategy of $( \alpha , \beta )$ , it injects a bias of $w = | \alpha - \beta |$ into its nudges.

A platform’s nudging strategy for a given ?? can also be represented in the transformed space of $( z , w )$ , where $z =$ $\rho ( 1 - \alpha - \beta )$ and ?? is as in Definition 1. In this transformed space, the original constraints $\alpha , \beta \ge 0$ and $\alpha + \beta \leq 1$ translate to $\begin{array} { r } { \frac { z } { \rho } + w \leq 1 } \end{array}$ and $z , w \ge 0$ , respectively. Either way—that ${ \mathrm { i } } \mathbf { s } ,$ irrespective of whether a platform’s nudging strategy is represented as $( \alpha , \beta )$ or as (??, ??) —these quantities are the platform’s private choices, hidden carefully behind algorithmic opacity and business secrecy.

## 3.4 Platform’s Profit

Consider the case of user $\langle x , y \rangle$ . Let $p _ { a } ( x )$ and $p _ { b } ( x ) =$ $1 - p _ { a } ( x )$ be the probabilities of him getting nudged towards narratives A and B, respectively. $\begin{array} { r } { \operatorname { I f } x \leq \frac { 1 } { 2 } , } \end{array}$ that is, if he is truly an A-type user, he would be classified as ?? with an accuracy of $\mathrm { P r } [ a | \mathrm { A } ] = \sigma ( x )$ . Thus, an A-type would be classified as ?? and ?? with probabilities of $\sigma ( x )$ and $1 - \sigma ( x )$ , respectively. Accordingly, he will be nudged towards A with a total probability of $\sigma ( x ) ( 1 -$ $\alpha ) + { \bigl ( } 1 - \sigma ( x ) { \bigr ) } \beta$ . Using analogous arguments, when $\begin{array} { r } { x > \frac { 1 } { 2 } . } \end{array}$ —that is, if the user is B-type—the probabilities of being classified as ?? and ?? should become: $\mathrm { P r } [ b | \mathrm { B } ] =$ $\sigma ( x )$ and $\mathrm { P r } [ a | \mathrm { B } ] = 1 - \sigma ( x )$ , so he will be nudged towards A with probability $\big ( 1 - \sigma ( x ) \big ) ( 1 - \alpha ) + \sigma ( x ) \beta$ Taken together, for user $\langle x , y \rangle$ , the probabilities of getting nudged towards narratives A and B would be given by:

$$
p _ {a} (x) = \left\{ \begin{array}{l l} \sigma (x) (1 - \alpha) + \big (1 - \sigma (x) \big) \beta , & \text {if} x \leq \frac {1}{2}, \\ \big (1 - \sigma (x) \big) (1 - \alpha) + \sigma (x) \beta , & \text {otherwise}; \end{array} \right.
$$

$$
p _ {b} (x) = \left\{ \begin{array}{l l} \sigma (x) \alpha + \big (1 - \sigma (x) \big) (1 - \beta), & \text { if } x \leq \frac {1}{2}, \\ \big (1 - \sigma (x) \big) \alpha + \sigma (x) (1 - \beta), & \text { otherwise }. \end{array} \right.
$$

For user $\langle x , y \rangle$ , the platform’s nudge towards A becomes successful with probability $1 - x$ and that towards B, with ??. Naturally, the total probability that the platform’s nudge is successful—that is, accepted by the user being nudged—is simply $p ( x ) = ( 1 - x ) p _ { a } ( x ) + x p _ { b } ( x )$ When user $\langle x , y \rangle$ accepts the nudge, he does not incur the search cost and enjoys a full benefit of $y > 0 ; { \mathrm { s o } }$ , his probability of engaging is 1. In contrast, if he does not accept the nudge, which occurs with a probability of $1 -$ $p ( x )$ , he can still engage if his $y$ is greater than ?? , implying that he would do so only with a probability of $1 - s$ . Taken together, the probability that he engages would simply be: $e ( x ) = p ( x ) ( 1 ) + ( 1 - p ( x ) ) ( 1 - s )$ integrating which over ??, we can get the total engagement with the platform: $\begin{array} { r } { E = \int _ { 0 } ^ { 1 } e ( x ) d x } \end{array}$

Lemma 1: For a social media platform, its users’ total engagement, ?? , increases linearly with $z : E =$ $\frac { 2 - 5 } { 2 } + \frac { s z } { 8 }$ , where $z \triangleq \rho ( 1 - \alpha - \beta )$ represents the platform’s nudging strategy.

The platform’s profit, ??, should also be its revenue since its marginal cost is negligible. Furthermore, since a higher level of engagement brings in more ad revenue, ?? should be proportional to ??, that is, $\pi = g E$ where $g > 0$ is the constant of proportionality. Since maximizing ?? is equivalent to maximizing $E ,$ , we can, without any loss of generality, set ?? to 1 and treat ?? as the platform’s profit. <sup>8</sup> Therefore, if the platform is motivated only by profit, it ought to maximize ?? , making the following result obvious:

Proposition 1: A profit-maximizing platform would set $\left( z ^ { \ast } , w ^ { \ast } \right) = \left( \rho , 0 \right)$ , that is, set $\alpha ^ { * } = \beta ^ { * } = 0$

Proposition 1 tells us that a profit-maximizing platform has no incentives to curb polarization in its user base and would set both its levers, ?? and ??, to their minimum. The result in Proposition 1 is consistent with our original understanding of the context. Nudging users towards their dominant proclivities results in them engaging more with the platform.

We next examine whether, as alleged in the press, the platform’s strategy to maximize engagement could actually be detrimental from a societal perspective and, if so, how such societal costs can be accounted for in the social welfare calculus (Allcott et al., 2020). If the extant literature is any indication, nudging users towards their proclivities might result in the formation of echo chambers and a polarization within the user base (Barberá, 2020). If indeed so, this would be a case of negative externality—in order to keep on generating profits, the social media platform may impose a cost that falls solely on society, a cost not borne by the platform nor perceived by its users. To formally understand this externality, we consider whether, and how, the platform’s actions could actually create division within its user base.

## 3.5 Polarization

Polarization increases when people flock to their proattitudinal narratives—thereby creating echo chambers— and ignore counter-attitudinal ones. In contrast, as users get exposed to opposing narratives, a diversification of perspectives ensues, which may mitigate polarization to an extent (Allcott et al., 2020). In our context, when an Atype visits A, or a B-type visits B, they add to intragroup engagement and echo chambers are likely to be created, but when an A-type visits B or a B-type visits A, crosstalk results from inter-group engagement. To the extent that such cross-talk counters the formation of echo chambers (e.g., Barberá, 2020), the overall polarization can be defined as:

Definition 2 (polarization): Polarization, ??, is the total engagement with the pro-attitudinal narrative minus that with the counter-attitudinal one.

To understand how ?? depends on the platform’s nudging strategy, (??, ??), we note that there are just two ways user $\langle x , y \rangle$ can visit or engage with Narrative A: (1) the user is successfully nudged by the platform towards A, which happens with probability $p _ { a } ( x ) ( 1 -$ ??), or (2) the nudge is rejected (with probability 1 − $p ( x ) )$ , the user looks for his own content (with probability $1 - s )$ , and then finds something suitable from Narrative A to engage (with probability $1 - x )$ making the probability of such an engagement equal to $( 1 - p ( x ) ) ( 1 - s ) ( 1 - x )$ . Therefore, the total probability of engaging with Narrative A is the total of the two probabilities from (1) and (2), which becomes $( 1 -$ $x ) \left( p _ { a } ( x ) + { \bigl ( } 1 - p ( x ) { \bigr ) } ( 1 - s ) \right)$ . Analogously, the total probability of engaging with Narrative B is $x \left( p _ { b } ( x ) + \right.$ $\bigl ( 1 - p ( x ) \bigr ) ( 1 - s ) \bigr )$ . According to Definition 2, the overall polarization can then be expressed as:

$$
\begin{array}{l} D \\ = \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} (1 - x) \left(p _ {a} (x) + (1 - p (x)) (1 - s)\right) d x} _ {\text {A - type visits A}} \right. \\ \left. + \underbrace {\int_ {\frac {1}{2}} ^ {1} x \left(p _ {b} (x) + (1 - p (x)) (1 - s)\right) d x} _ {\text {B - type visits B}}\right) \\ - \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} x \left(p _ {b} (x) + (1 - p (x)) (1 - s)\right) d x} _ {\text {A - type visits B}} \right. \\ \left. + \underbrace {\int_ {\frac {1}{2}} ^ {1} (1 - x) \left(p _ {a} (x) + (1 - p (x)) (1 - s)\right) d x} _ {\text {B - type visits A}}\right). \end{array}\tag{1}
$$

After some algebra, we get:

Lemma 2: When the platform adopts a nudging strategy, $z \triangleq \rho ( 1 - \alpha - \beta )$ , it creates a level of polarization that is linearly increasing in $z \colon D =$ $\begin{array} { r } { \frac { \dot { 2 } - s } { 4 } + \frac { z ( 2 + 3 s ) } { 3 0 } . } \end{array}$

The next result is immediate from Proposition 1 and Lemma 2:

Theorem 1: The nudging strategy of a profitmaximizing platform would show no bias towards either narrative but would end up creating the maximum polarization in its user base.

Theorem 1 lends credence to the allegations against social media platforms and shows that such a platform could earn a significant part of its profit at the expense of serious polarization within society. This societal cost, not accounted for in the platform’s profit, creates an externality that is not internalized by the individual users. It should therefore be an important consideration for any debate on related public policy.

## 4 Intervention by Policymaker

## 4.1 Policy Objective and the First Best

In economic analyses, the usual objective is to maximize the total social welfare, which is the sum of individual gains of all economic agents. Further, in a free-market setting, every transaction between economic agents is considered Pareto optimal—were it not, transacting agents would not have voluntarily participated in it anyway. So, in many practical contexts, establishing a free market is sufficient for maximizing collective welfare. There are exceptions, however, where such welfare calculus and free-market mechanisms do not work, and it becomes necessary to choose a policy objective independently. Our setting happens to fall in this category of exceptions.<sup>9</sup>

In our setting, the cost of polarization and bias created by a social media platform is unlikely to show up in a user’s individual utility for two reasons: (1) users may be unaware of the societal cost (information asymmetry), or (2) even if they are aware, they may not count the societal cost as their own (free riding). As a result, a traditional consumer surplus (CS) calculation would not account for the societal cost of polarization ( ?? ). Still, it would continue to count the users’ consumption benefit—the pleasure ( ?? ) from users’ voluntary engagement (with or without nudges) aggregated over all users—making CS an increasing function of ??. In our setup, much like profit, CS too turns out to be linear in ??:

$$
\mathrm{CS} = \frac {1 + (1 - s) ^ {2}}{4} + \frac {s z (2 - s)}{1 6}.
$$

Therefore, if we were to simply maximize the collective welfare of the platform and users, our task would be the same as maximizing the total engagement, and we would end up with the boundary outcome of $( z , w ) = ( \rho , 0 )$ inadvertently and incorrectly inferring that unabated polarization of society should indeed be the ultimate objective. If that were to be true—that is, if (??, ??) = (??, 0) were indeed the desirable social outcome— much of the current debate on this issue along with a large volume of extant literature would become pointless, as would become of the fate of this exercise. In other words, before intervening, a policymaker must overlook the myopic welfare calculus and independently define what it aims to achieve through an intervention. Given that excessive polarization and bias are both undesirable for society, it becomes imperative that a benevolent policymaker aims to mitigate both. From a policy standpoint, therefore, the first best should be $( z , w ) =$ (0,0) . In subsequent sections, we will examine under what conditions such an objective can be met through appropriate policy interventions.

## 4.2 Fiscal Intervention

How should a benevolent policymaker intervene to mitigate the externality of polarization? The most common, and perhaps also the most acceptable, intervention would be a fiscal one: a tax or subsidy depending on whether the externality is negative or positive (Laffont, 1989). In this way, similar to the case of pollution, policymakers could levy a tax or penalty on the platform. However, one could ask: Can policymakers not completely ban algorithmic nudges on polarizing topics? The optics of a ban coming across as draconian notwithstanding, the putative answer is in the affirmative—policymakers could indeed impose such a ban. Still, we need not consider this possibility separately because, after all, a ban is similar to a formidably large tax or penalty levied on the platform.

A fiscal intervention can be either on the demand side or the supply side. Since a demand-side intervention—that is, a tax on consumption—could be difficult to operationalize, we consider a supply-side intervention only. More specifically, we consider what would happen if a policymaker were to intervene in this market by imposing on the platform a tax of ?? > 0 per unit of polarization. This would then compel the platform to maximize ?? − ???? where, as before, ?? represents the polarization created by the platform. In essence, ?? can also be viewed as the strength of the policymaker’s intervention.

A point to note here is that the supply-side fiscal intervention penalizes the platform only for the polarization it creates but does not levy a tax on the bias it exhibits. There are practical reasons for this exclusion. First, an attribution of bias is subjective, leading to asymmetric perceptions among users. What is perceived as “bias” by one group of users could well be hailed as “fair” by another because of a divergence of their “naive realism” (Pronin et al., 2004). Put differently, a proattitudinal bias may be discounted or ignored, but users are likely to register a counter-attitudinal bias. Therefore, from the perspective of experiment design, bias is a nebulous concept that is difficult to measure using survey instruments. In contrast, as amply demonstrated in prior research (e.g., Allcott et al., 2020; Bakshy et al., 2015; Settle, 2018), the overall polarization of society is measurable through carefully crafted field experiments. Second, policymakers cannot see or estimate either ?? or $\beta$ because social media platforms can and do hide behind the opacity of their algorithms (Lu, 2021). Even if the platform’s activity logs are audited, all that policymakers can see from these logs are the recorded nudges, for real or simulated users; the actual reason behind a nudge is opaque, as the platform’s algorithms are its business secrets (Cowgill & Tucker, 2020). Seen this way, it becomes clear that levying a penalty on the actual bias present in the platform’s nudging strategy becomes impractical for policymakers.

## 4.3 Impact of Intervention

If policymakers were to intervene with a tax-rate of $\kappa ,$ the platform would pick ?? to maximize:

$$
E - \kappa D = \frac {(2 - s) (2 - \kappa)}{4} + \frac {z}{2} \left(\frac {s}{4} - \frac {\kappa (2 + 3 s)}{1 5}\right).
$$

Lemma 3: Let $\begin{array} { r } { \chi \triangleq \frac { 1 5 s } { 4 ( 2 + 3 s ) } } \end{array}$ . If ?? , the strength of intervention, is larger than $\chi ,$ the platform sets $z ^ { * } =$ 0; otherwise, it sets $z ^ { * } = \rho$

According to Lemma 3, if the intervention is weak— specifically, if $\kappa \leq \chi$ —it would have little impact in curbing polarization, as the platform would continue to set ?? at its maximum possible value of $\rho$ . In contrast, when $\kappa > \chi$ , the platform would set $z ^ { * } = 0 -$ —that is, $\alpha ^ { * } +$ $\beta ^ { * } = 1 -$ thereby minimizing polarization created by its nudging strategy.

Evidently, despite having two independent levers in ?? and ?? —or equivalently in ?? and ?? —the platform combines them into a single one, $\alpha + \beta$ . In fact, hidden therein are the seeds of bias. To understand this, note that when $\kappa \leq \chi ,$ , the intervention is too weak, and the platform goes about its profit maximization as usual; to do so, it must set $\alpha ^ { * } =$ $\beta ^ { * } = 0$ . In other words, profit provides the platform with an economic incentive to remain unbiased. As the intervention gathers in strength and ?? goes beyond $\chi , z ^ { * }$ becomes zero and $\alpha ^ { * } + \beta ^ { * } = 1$ . To remain completely unbiased now, the platform ought to set $\begin{array} { r } { \alpha ^ { * } = \beta ^ { * } = \frac { 1 } { 2 } , } \end{array}$ but there is no inherent incentive for the platform to do so.

Theoretically, the platform could get exactly the same effect by setting $\alpha ^ { * } = 0$ and $\beta ^ { * } = 1$ , or $\alpha ^ { * } = 1$ and $\beta ^ { * } =$ 0, or any other combination such as $\begin{array} { r } { \alpha ^ { * } = \frac { 1 } { 4 } } \end{array}$ and $\begin{array} { r } { \beta ^ { * } = \frac { 3 } { 4 } , } \end{array}$ possibly injecting a net bias of $w ^ { \ast } = | \alpha ^ { \ast } - \beta ^ { \ast } | > 0$ . In practice, too, we expect to see $\alpha \neq \beta$ . The platform is, after all, run by a set of individuals who are likely to have their own biases. These individual biases, when collective, could manifest themselves in the platform’s overall nudging strategy. Besides, as we will soon see in Section 5, advertisers could be disproportionately inclined towards one narrative, implying that there is more ad revenue to be earned when users are nudged to one side over the other. In short, unless $\kappa \leq \chi$ and $\alpha ^ { * }$ + $\beta ^ { * } = 0$ , we would expect the platform to be biased, that is, ?? $w ^ { * }$ to be strictly positive.

Theorem 2: If the intervention is weak $( \kappa \leq \chi )$ , it has no impact on the platform’s nudging strategy. If the intervention is sufficiently strong $( \kappa > \chi )$ , the platform would adopt a nudging strategy that curbs polarization but possibly so at the expense of becoming biased.

Theorem 2 is illustrated in Figure 3, where the entire $( s , \kappa )$ -space can be partitioned into two regions. In the bottom region where ?? $\leq \chi ,$ the intervention is too weak to have any impact, and the platform’s decision remains the same as the case where there is no intervention at all. As ?? gains in strength and crosses $\chi$ , the intervention takes complete hold—the platform drives ?? to zero, curbing polarization but possibly introducing bias in the process. Theorem 2 thus highlights the quandary of policymakers who are placed between the rock of bias and the hard place of polarization. Of course, policymakers cannot allow the platform to create divisions within society and are thus compelled to intervene in some way. When they do, though, it may make the platform less polarizing but more biased. In this way, Theorem 2 points to the inability of a fiscal intervention to achieve the first best of $( z , w ) = ( 0 , 0 )$

![](/api/attachments/KGUU7NJ7/fulltext/images/446900c558852bbed037f6965699725c44744306875746acce04832ae841f1f3.jpg)  
Figure 3. Impact of Policymaker’s Intervention, ??

## 5 Revisiting Bias

Before moving on to other possibilities, we would like to revisit the issue of bias and explore it further. Strictly speaking, the way the platform’s profit function is modeled so far, it is invariant of the level of bias. Consequently, we cannot claim with certainty that the platform will always be biased. There is a good possibility that it would be in practice, but we cannot be certain. This is why we tiptoe around this issue by referring to it only as a possibility in Theorem 2.

To formally understand where this incentive for bias could stem from, we now consider the presence of inherent, structural bias in the overall ecosystem. Consider, for example, the situation where the ad pool itself has an asymmetry, with more advertisers concentrated at one of the two ends, say end A, so more ad revenues are to be earned from A than from B. That such asymmetry exists in the ad pool for legacy media has already been recognized in the literature (e.g., Beattie et al., 2021).

Assumption 3: For every dollar it earns from an engagement with B, the platform earns $1 + m$ dollars from an engagement with A, where $m \geq 0$ is the extra margin.

Our entire analysis so far remains intact, except that the platform’s profit, ??, is no longer the same as the total engagement, ?? . To calculate ?? , we have to separate the engagement with A from that with B. Recall from Section 3.5 that the probability of engaging with Narrative A is $P _ { a } ( x ) = ( 1 - x ) \left( p _ { a } ( x ) + \right.$

$\bigl ( 1 - p ( x ) \bigr ) ( 1 - s ) \bigr )$ , and that for B is $P _ { b } ( x ) = x \Big ( p _ { b } ( x ) +$ $\bigl ( 1 - p ( x ) \bigr ) ( 1 - s ) \bigr )$ . Integrating them over all ??, we can find the engagements with A and B separately. Therefore, we can write:

$$
\begin{array}{c} \pi = (1 + m) \Bigg (\underbrace {\int_ {0} ^ {1} P _ {a} (x) d x} _ {\text {Visits to A}} \Bigg) + (1) \Bigg (\underbrace {\int_ {0} ^ {1} P _ {b} (x) d x} _ {\text {Visits to B}} \Bigg) \\ = \Big (1 + \frac {m}{2} \Big) \Big (\frac {2 - s}{2} + \frac {s z}{8} \Big) + \frac {m w (2 + s)}{1 2}. \end{array}\tag{2}
$$

The platform now has two levers in ?? and ??, turning which it can change its profit. Of course, it would like to maximize ?? subject to the constraint $\begin{array} { r } { \frac { z } { \rho } + w \leq 1 } \end{array}$ The following result is immediate:

Proposition 2: Let ${ \overline { { \rho } } } \triangleq { \frac { 4 m ( 2 + s ) } { 3 s ( 2 + m ) } }$ . In equilibrium, the platform would set $( z ^ { * } , w ^ { * } )$ to $( \rho , 0 )$ if $\rho \geq { \bar { \rho } } ,$ and to (0,1) otherwise.

In other words, when the classifier has ample discriminating power, that is, when $\rho \geq { \bar { \rho } } ,$ , the platform sets $w ^ { * } = 0$ , and Theorem 1 continues to hold as stated. If $\rho < \bar { \rho } ,$ , however, the platform sets $w ^ { * } = 1$ and becomes fully biased itself. Proposition 2 is illustrated in Figure 4, which clearly shows the trade-off a platform faces between $\rho ,$ its classifier’s discriminating power, and $m ,$ the pull from a biased ad pool. When the classifier’s discriminating power is sufficiently high, the platform mostly ignores the bias in the ad pool and sticks to its strategy of maximizing engagement in an unbiased manner. That a platform can remain unbiased despite the presence of structural bias in the ecosystem is noteworthy.

![](/api/attachments/KGUU7NJ7/fulltext/images/6221f28161b448803562ac07fdd6782152ce2d37918baff297187f1939616dc8.jpg)  
Figure 4. Impact of Ad-Pool Bias, ??

![](/api/attachments/KGUU7NJ7/fulltext/images/e18795e50beb8b1b8637234f86dac4b6aad12175b891d8e008d33bec192b0eed.jpg)  
Figure 5. Impact of Policymaker’s Intervention with Biased Ad-Pool; $\pmb { m } = \mathbf { 0 . 1 }$

When the classifier is not amply discriminating, however, the platform succumbs to the inherent bias in the ad pool and starts nudging its users in a biased manner. In fact, when the ad-pool bias is large— specifically, when $\begin{array} { r } { m > \frac { 6 s } { 8 + s } } \end{array}$ —the platform can no longer remain unbiased, irrespective of the discriminating power of its classifier. Thus, Proposition 2 tells us that, when the bias in the ad pool is large, the platform’s strategy also becomes fully biased, even in the absence of any intervention from the policymaker.

It can be easily verified that $\begin{array} { r } { \frac { \partial \overline { { \rho } } } { \partial m } = \frac { 8 ( 2 + s ) } { 3 s ( 2 + m ) ^ { 2 } } } \end{array}$ is positive. When ?? increases, the higher level of structural bias pulls $\bar { \rho }$ upwards, thereby expanding the blue region and shrinking the red. The same behavior is also observed when ?? decreases because $\begin{array} { r } { \frac { \partial \overline { { \rho } } } { \partial s } = - \frac { 8 m } { 3 s ^ { 2 } ( 2 + m ) } < 0 } \end{array}$ . When ?? increases, the platform’s nudge becomes more valuable to the user relative to engaging otherwise; this gives the platform more control over its users. The resulting market power strengthens the platform’s hand and allows it to show more resistance towards succumbing to the structural bias—the red region expands and the blue shrinks.

Let us now see what happens when the policymaker intervenes with ??, making the platform maximize:

$$
\begin{array}{r} \pi - \kappa D = \frac {(2 - s) (2 + m - \kappa)}{4} + \frac {m w (2 + s)}{1 2} \\ + \frac {z}{2} \bigg (\frac {s (2 + m)}{8} - \frac {\kappa (2 + 3 s)}{1 5} \bigg), \end{array}
$$

subject to the constraint that $\frac { z } { \rho } + w \leq 1$

Lemma 3′: Let $\begin{array} { r } { \chi \triangleq \frac { 1 5 s \left( 2 + m \right) } { 8 \left( 2 + 3 s \right) } - \frac { 5 m \left( 2 + s \right) } { 2 \rho \left( 2 + 3 s \right) } . } \end{array}$ . When the policy maker intervenes with ?? , the platform’s optimal nudging strategy becomes: $\left( z ^ { * } , w ^ { * } \right) = \left( \rho , 0 \right) { \mathrm { i f ~ } } \kappa \leq$ $\chi ,$ and $( z ^ { * } , w ^ { * } ) = ( 0 , 1 )$ ) otherwise.

It is easy to verify that this ?? reduces to the one in Lemma 3 when $m = 0$ , and our analysis reduces to the original setting.

Theorem 2′: Let $\chi$ be as defined in Lemma $3 ^ { \prime } .$ If less than $\chi ,$ ?? has no impact on the platform’s nudging strategy. Otherwise, the platform adopts a strategy that curbs polarization but injects bias.

Therefore, Theorem 2 continues to hold with the redefinition of $\gamma .$ The result in Theorem $2 ^ { \prime }$ is illustrated in Figure 5 for $m = 0 . 1$ . Since $\begin{array} { r } { \frac { \partial { \boldsymbol \chi } } { \partial m } < 0 } \end{array}$ for all $m > 0$ , the bias within the ad pool only expands the region where the platform’s nudging strategy exhibits bias. Viewed differently, a biased ad pool tends to pull the platform towards being more biased. As ?? increases, the structural bias takes a stronger hold of the platform’s nudging strategy, and beyond $\begin{array} { r } { m = \frac { 6 s } { 8 + s } , \lambda } \end{array}$ ?? ceases to be positive for any $\rho \in [ 0 , 1 ]$ , so the platform becomes fully biased even when there is no policy intervention; this echoes our earlier finding in Proposition 2, where there was no intervention, so ?? was zero.

Theorems 2 and 2′ point to an interesting duality between polarization and bias. As far as the platform is concerned, when it tries to maximize its overall profit, it treats polarization and bias as strategic substitutes.<sup>10</sup> As such, it prefers to use only polarization to keep users engaged so that its ad revenue is maximized. When compelled to show restraint in terms of polarization, though, fiscally or otherwise, it may look towards using bias as a part of its nudging strategy. In essence, the platform can earn profit from either polarization or bias, although, when left to its own device in a market with little structural bias (small ??), it earns more from polarization and prefers to use it over bias. As either ?? or ?? increases, polarization starts losing its appeal relative to bias. Finally, when ?? crosses ??, this loss is complete, and bias becomes the platform’s first choice as its profit-earner. It is this duality between the two—polarization and bias—that blunts the effectiveness of any direct policy intervention in this market.

## 6 Public Awareness

Our analyses so far have revolved around a setting where users of social media platforms are either not aware of the issues related to polarization and bias, or if they are, they do not care, so they keep those costs out of their individual decisions to engage. Now, a setting where users are fully unaware would perhaps be a more accurate description of the initial years of social media. At present, however, users are becoming more and more aware of the adverse effects. To understand how our results would change in such an extended setting, we now investigate what happens when users, at least some of them, become aware of the detrimental effects of the platform and start taking that into consideration. More specifically, we assume that a ?? fraction of users is aware and incurs a per-use cost of $\mu D + \nu w$ when engaging, where $\mu , \nu > 0$ are constants and ?? and ?? are the expected levels of polarization and bias.<sup>11</sup> The remaining $1 - \lambda$ fraction is assumed to be unaware of these detriments and goes about its old ways of engaging with the platform; these users do not perceive these costs, let alone bear them.

Consider user ⟨??, ??⟩ . With probability ?? , the user is aware and, with $1 - \lambda$ , the user is not aware. Therefore, the probability that the user engages would now change to:

$$
\begin{array}{l} e (x) = \\ \left\{ \begin{array}{l} (1 - \lambda) e _ {U} (x), \text {if} \mu D + v w \geq 1, \\ (1 - \lambda) e _ {U} (x) + \lambda p (x) (1 - \mu D - v w), \text {if} 1 > \mu D + v w \geq 1 - s, \\ (1 - \lambda) e _ {U} (x) + \lambda p (x) (1 - \mu D - v w) + (1 - p (x)) (1 - s - \mu D - v w) \\ \text {otherwise}, \end{array} \right. \end{array}\tag{\(\nu w)\}
$$

(3)

where $e _ { U } ( x ) = p ( x ) + { \bigl ( } 1 - p ( x ) { \bigr ) } ( 1 - s )$ is the probability of engagement for unaware users. Of the three possible cases, the first one is infeasible as it eliminates all aware users from engaging—it can be mathematically verified that, in equilibrium, the platform would never make such choices of ?? and ?? that end up completely shutting the aware users out. The second case, $1 > \mu D + \nu w \geq 1 - s$ , where all aware users become passive users, albeit possible, is also somewhat extreme and can occur only when ??, ??, and ?? take on large values simultaneously. For ease of exposition, going forward, we will stay away from the extreme cases and assume that only the third case is relevant, that is, $\mu D + \nu w < 1 - s$ . We have verified that including the second case into our analysis makes no qualitative difference to our insights; please see Appendix B.

Now, although $e ( x )$ can be used to determine the total engagement, ??, it is of little use when $m > 0$ , since we must then consider engagements with A and B separately to calculate ??. If user $\langle x , y \rangle$ is not aware, the user’s probability of engaging with Narratives A and B are still $( 1 - x ) \left( p _ { a } ( x ) + { \big ( } 1 - p ( x ) { \big ) } ( 1 - s ) \right)$ and $x \left( p _ { b } ( x ) + { \bigl ( } 1 - p ( x ) { \bigr ) } ( 1 - s ) \right)$ , respectively. However, if the user is now aware, the user’s probabilities would become $( 1 - x ) ( p _ { a } ( x ) ( 1 - \mu D - \nu w ) + ( 1 - p ( x ) ) ( 1 -$ ?? − ???? − ????)) and $x \left( p _ { b } ( x ) ( 1 - \mu D - \nu w ) + \left( 1 - \mu D \right) ^ { 2 } \right)$ $p ( x ) \big ) ( 1 - s - \mu D - \nu w ) \big )$ , respectively. Therefore, for a random user ⟨??, ??⟩, the user’s total probability of engaging with Narratives A and B would respectively be:

$$
\begin{array}{c} P _ {a} (x) = \lambda (1 - x) \Big (p _ {a} (x) (1 - \mu D - \nu w) + \big (1 - p (x) \big) (1 - s - \mu D - \nu w) \Big) \\ + (1 - \lambda) (1 - x) \Big (p _ {a} (x) + \big (1 - p (x) \big) (1 - s) \Big), \text { and } \end{array}
$$

$$
\begin{array}{c} P _ {b} (x) = \lambda x \left(p _ {b} (x) (1 - \mu D - v w) + (1 - p (x)) (1 - s - \mu D - v w)\right) \\ + (1 - \lambda) x \left(p _ {b} (x) + (1 - p (x)) (1 - s)\right). \end{array}
$$

Integrating them over ??, and applying the extra margin of ?? to A, we get:

$$
\begin{array}{l} \pi = (1 + m) \Bigg (\underbrace {\int_ {0} ^ {1} P _ {a} (x) d x} _ {\text {Visits to A}} \Bigg) + \Bigg (\underbrace {\int_ {0} ^ {1} P _ {b} (x) d x} _ {\text {Visits to B}} \Bigg) \\ = \Big (1 + \frac {m}{2} \Big) \Bigg (\frac {2 - s}{2} + \frac {s z}{8} - \lambda (\mu D + \nu w) \Bigg) \\ + \frac {m w \big (2 + s - 2 \lambda (\mu D + \nu w) \big)}{1 2}. \end{array}\tag{4}
$$

Also, the overall polarization can be estimated as:

$$
\begin{array}{l} D = \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} P _ {a} (x) d x} _ {\text {A - type visits A}} + \underbrace {\int_ {\frac {1}{2}} ^ {1} P _ {b} (x) d x} _ {\text {B - type visits B}}\right) - \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} P _ {b} (x) d x} _ {\text {A - type visits B}} + \underbrace {\int_ {\frac {1}{2}} ^ {1} P _ {a} (x) d x} _ {\text {B - type visits A}}\right) \\ = \frac {2 - s}{4} + \frac {z (2 + 3 s)}{3 0} - \frac {\lambda (2 z + 1 5) (\mu D + \nu w)}{3 0}. \end{array}\tag{5}
$$

simplicity, though, we use D and w in this analysis with the tacit understanding that they represent the expected values till we solve the fixed-point equations that fulfill the expectations. After that, they represent their realized values.

When expectations are fulfilled, the realized value echoes the expected one. We solve the fixed point equation in (5) to obtain:

$$
D = \frac {2 (1 - \lambda \nu w) (1 5 + 2 z) - 3 s (5 - 2 z)}{6 0 + 2 \lambda \mu (1 5 + 2 z)}.\tag{6}
$$

It is easy to see in (4), (5), and (6) that ?? is essentially a scale parameter and can be absorbed into $\mu$ and $\nu .$ Therefore, we normalize ?? to one without any loss of generality. We now substitute ?? from (6) into (4) to get:

$$
\begin{array}{r} \pi = \frac {\left(1 + \frac {m}{2}\right) \left(3 0 \left(1 - \nu w - \frac {s}{2} \left(1 - \frac {z}{4}\right)\right) + \frac {s z ^ {2} \mu}{4} - \frac {1 7 s z \mu}{8}\right)}{3 0 + \mu (1 5 + 2 z)} \\ + \frac {5 m w \left(1 - \nu w + \frac {s}{2} + \frac {\mu s}{2} - \frac {s z \mu}{1 5}\right)}{3 0 + \mu (1 5 + 2 z)}. \end{array}
$$

Facing a tax rate of ??, the platform would then want to maximize $\pi - \kappa D$ , where ?? is as given in (6). Depending on the parameter values, the platform may adopt one of four different nudging strategies: $( z ^ { * } , w ^ { * } )$ could be $( \rho , 0 ) , ( 0 , 1 ) , ( 0 , 0 ) , \mathrm { o r } ( 0 , w ^ { * } )$ , where $0 <$ $w ^ { * } < 1$

Lemma 4: In equilibrium, $z ^ { * }$ can be either zero or $\rho .$ When $z ^ { * } = \rho , \ w ^ { * }$ must be zero. However, when $z ^ { * } = 0 ,$ , an interior solution of ?? is possible: $w ^ { * } =$ $\frac { 2 + s ( 1 + \mu ) } { 4 \nu } - \frac { 3 ( 2 + m - \kappa ) } { 2 m }$ . This solution is valid only if $\xi _ { L } \le \kappa \le \xi _ { U }$ , where $\begin{array} { r } { \xi _ { L } \triangleq 2 + m - { \frac { m \left( 2 + s \left( 1 + \mu \right) \right) } { 6 \nu } } } \end{array}$ and $\begin{array} { r } { \xi _ { U } \triangleq 2 + \frac { 5 m } { 3 } - \frac { m \left( 2 + s \left( 1 + \mu \right) \right) } { 6 \nu } . \operatorname { I f } \kappa > \xi _ { U } , w ^ { \ast } \mathrm { i s } 1 } \end{array}$ , and if $\kappa < \xi _ { L } ,$ , it is 0.

The interval $[ \xi _ { L } , \xi _ { U } ]$ , where an interior ?? is possible, has a width of ${ \frac { 2 m } { 3 } } ,$ , implying an interior solution does not exist for $m = 0$ . In order to find out which nudging strategy is optimal for the platform, we need to compare the values of the objective function, $\pi - \kappa D$ , for different nudging strategies and pick the one that yields the maximum. This comparison can be done in a pairwise fashion to find the threshold that separates a pair of strategies. For example, comparing the profit from $\left( z ^ { * } , w ^ { * } \right) = \left( \rho , 0 \right)$ with $( z ^ { * } , w ^ { * } ) = ( 0 , 1 )$ , we get:

$$
\begin{array}{r l} & {\chi \triangleq \frac {\frac {2 \nu (3 + 2 m) (3 0 + 1 7 \mu)}{3} + \frac {5 (2 s (9 + m \mu) - 3 m (8 + s))}{1 2}}{4 + s (6 + 4 \mu) + \nu (3 0 + 1 7 \mu)}} \\ & {- \frac {2 \mu (2 - s) + \frac {1 5 s \mu^ {2} (1 + 2 m)}{8} + \frac {2 3 m \mu (1 + s)}{3} + \frac {m s \mu^ {2}}{4 8}}{4 + s (6 + 4 \mu) + \nu (3 0 + 1 7 \mu)},} \end{array}
$$

$( \rho , 0 )$ dominating (0,1) if and only if $\kappa < \chi .$ . It is easy to verify that this $\chi$ approaches the ?? in Lemma $3 ^ { \prime }$ when both ?? and ?? approach zero. All the other boundaries can be found in a similar manner. We are now ready to characterize the complete equilibrium solution.

Theorem 3: Let $\xi _ { L } , \xi _ { U } ,$ and $\chi$ be as defined above, and let $\begin{array} { r } { \psi _ { 1 } \triangleq \frac { 2 + m } { 2 + s ( 3 + 2 \mu ) } \Big ( \frac { 1 5 s ( 4 - \mu ^ { 2 } ) } { 3 2 } - \frac { \mu ( 2 - s ) } { 2 } \Big ) } \end{array}$ and $\psi _ { 2 } \triangleq 2 +$ $\begin{array} { r } { m + m \left( \frac { \Delta \left( 2 + \mu \right) } { 6 \nu } - \frac { 7 6 + 3 4 \mu + s \left( 5 4 + 6 3 \mu + 1 7 \mu ^ { 2 } \right) } { 6 \nu \left( 3 0 + 1 7 \mu \right) } \right) , } \end{array}$ , where $\Delta =$

$$
\sqrt {1 6 \left(2 s + \frac {2 - s}{2 + \mu}\right) \left(\frac {3 4 + s (2 1 + 1 7 \mu)}{(3 0 + 1 7 \mu) ^ {2}}\right) - 3 \nu \left(1 + \frac {2}{m}\right) \left(1 5 + \frac {2 \mu}{2 + \mu}\right) \left(\frac {3 2 + 3 s (6 + 5 \mu)}{(3 0 + 1 7 \mu) ^ {2}}\right)}.
$$

Further, let $s _ { 1 }$ and $s _ { 2 }$ be the solutions of $\psi _ { 1 } = \xi _ { L }$ and $\psi _ { 2 } = \chi ,$ respectively, and let:

$$
\phi \triangleq \left\{ \begin{array}{l l} \psi_ {1}, & \text {if s <   s_{1}}, \\ \psi_ {2}, & \text {if s_{1} \leq s <   s_{2}}, \\ \chi , & \text {otherwise.} \end{array} \right.
$$

Then, the platform’s nudging strategy in equilibrium is as follows:

$$
\begin{array}{l l} (z ^ {*}, w ^ {*}) \\ = \left\{ \begin{array}{l l} (\rho , 0), & \text { if   } \kappa \leq \phi \text {(low bias, high polarization)}, \\ (0, 0), & \text { if   } \phi <   \kappa <   \xi_ {L} \text {(low bias, low polarization)}, \\ (0, w ^ {*}), & \text { if   } \xi_ {L} \leq \kappa <   \xi_ {U} \text { and   } \kappa > \phi \text {(some bias, low polarization)}, \\ (0, 1), & \text { otherwise   (high bias, low polarization)}. \end{array} \right. \end{array}
$$

Theorem 3 is illustrated in Figure 6, where the entire $( s , \kappa )$ space is partitioned into four distinct regions. In the bottom-most region (shaded in red), the intervention is too weak and has little impact on the platform’s nudging strategy. In the topmost region (shaded in blue), the intervention is too strong, and the platform becomes heavily biased. However, in the region shaded in green, where the intervention is moderate, we obtain the socially desirable outcome of low bias and low polarization. Nestled between the blue and green regions is the cyan, where an interior $w ^ { * }$ is optimal, so there may be some bias in this region, but polarization is still low there.

Interestingly, the green region is present in all the panels in Figure 6, but Panels (a) and (b), both drawn up for $m = 1$ , are perhaps the more remarkable ones. Recall from Proposition 2 and Figure 4 that $m = 1 >$ $\frac { 6 s } { 8 + s }$ is an extreme value that makes the platform fully biased even if it has a perfect $\rho = 1$ . What is remarkable is that, even in such an extreme case, there is now a significant green region where the policymaker could intervene fiscally and not make the platform biased. It is only at a large ?? and small ?? that this region significantly shrinks or even disappears.

To understand the relative impact of users’ awareness, compare Figure 6 with Figure 5. As can be clearly seen, the socially desirable outcome of low bias and low polarization, distinctly present in all four panels of Figure 6 as the green region, is conspicuous in its absence in Figure 5. Not just the green region, but the cyan region is also missing in Figure 5. The implications are clear. When they become sufficiently aware—that is, when ?? and ?? are significant—the users themselves start modifying their engagement with the platform in such a manner that their collective awareness mitigates both polarization and bias, obviating any need for policy intervention. This is certainly true for smaller values of ??. At a larger ??, a moderate level of intervention could actually be useful.

![](/api/attachments/KGUU7NJ7/fulltext/images/14aa01761e2b81c14774f02f3c5659e5e5ce90a8430810a59bd452f025040541.jpg)  
(a) m = 1, µ = 0.5, ν = 0.2

![](/api/attachments/KGUU7NJ7/fulltext/images/e3cc751c5317b9a9a45d442d8f387f707882e9b6c89643e94fd7697c75f86e48.jpg)  
(b) m = 1, µ = 0.5, ν = 0.3

![](/api/attachments/KGUU7NJ7/fulltext/images/9ea304c0ab0c5d271e07b6df88a9be2219cbcbc3faa7f36c6392ae4fb086710c.jpg)  
(c) m = 0.5, µ = 0.2, ν = 0.2

![](/api/attachments/KGUU7NJ7/fulltext/images/902795f45ac6ebbf83bd33a7646da6a70a03b32e1b5b5f69bdd226f435fb23f6.jpg)  
(d) m = 0.25, µ = 0.75, ν = 0.3  
Figure 6. Impact of Policymaker’s Intervention with Aware Users

Surprisingly, a fiscal intervention—which without users’ awareness was only a blunt double-edged sword—could now become an effective mitigation tool. For this to happen, though, the intervention level, ??, cannot be too high or too low; it must be moderate. Specifically, a desirable intervention should satisfy $\psi _ { 1 } \leq \kappa \leq \xi _ { L }$ . Any lower than $\psi _ { 1 } ,$ , the intervention is inadequate in curbing polarization; any higher than $\xi _ { L } ,$ , it is too strong and forces the platform to switch to bias as its source of profit. In other words, the green region in Figure 6 can be thought of as the window of effective intervention, denoted $W =$ $( \psi _ { 1 } , \xi _ { L } )$ . Evidently, ?? is large for small values of ??, but it shrinks as ?? increases. In fact, for a small enough ?? or a large enough ?? or both, ?? could completely disappear at a large ??; consider the case in Panel (a) of Figure 6 for example.

## 7 Direct vs. Indirect Intervention

The previous section clearly illustrates the fundamental role public awareness could end up playing in the mitigation of both polarization and bias in social media platforms. This, along with the observation that direct intervention alone is ineffective, makes us wonder whether policymakers could look at other approaches in their battle against polarization and bias. Our results in the previous section indicate that one possible approach would be to raise awareness about these adverse effects of social media and let users themselves moderate their activity after becoming aware. Providing education to raise awareness could allow the market to internalize the externality recognized earlier.

What means do policymakers have to educate the public, raise their levels of awareness, and change their ?? and ??? There are several ways in which policymakers can reach the public in an effort to influence their behavior. In fact, any old-fashioned, targeted advertisement campaign should do the trick. Billboards, road signs, and TV ads are all possible ways to mildly and repeatedly remind users of the adverse effects of polarization and bias. Targeted advertisement on social media itself is also a possibility. In more extreme cases, policymakers could force social media platforms to have a welcome screen that highlights the dangers of division and bias. Finally, policymakers could make the public aware by holding public hearings on these issues and broadcasting them on social and legacy media.

The notion of education as a way to influence the public towards making socially acceptable choices is certainly not new; in fact, education has long been successfully used alongside direct intervention, such as enforcement, to curb many types of noncompliant behavior, including illegal tobacco sales, alcoholism, drunk driving, and drug abuse (e.g., Dey et al. 21, Feighery et al., 1991). Strictly speaking, education (or fostering awareness) is also a form of intervention, albeit an indirect one. Such indirect interventions are common in practice. For instance, every time we are reminded through billboards or road signs that “seat belts save lives” or “drunk driving kills,” authorities are making an indirect intervention to educate the public about possible hazards. In addition, there may also be some type of direct intervention in the form of a penalty (traffic ticket) when caught violating the law (driving drunk or without a seat belt).

Although the insights from Section 6 are useful for public policy, the analysis there was done for an arbitrarily fixed level of awareness, represented by the exogenous parameters ?? and ??, over which the policymaker had little control. However, as discussed earlier in this section, in reality, policymakers may be able to influence the level of public awareness. The objective of this section is to see what happens when a policymaker has some influence over ${ } ^ { , \mu }$ and ??. Before embarking on this journey, let us first discuss what a benevolent policymaker could do in this context. Of course, the policymaker would want to be in the green region in Figure 6 and would want ?? to be as large as possible, which can be achieved by lowering $\psi _ { 1 }$ and raising $\xi _ { L } .$ To understand how this can be affected, we perform comparative statics with respect to ?? and ??:

Proposition 3: Let $\begin{array} { r } { \bar { \mu } \triangleq \sqrt { 4 + \left( \frac { 8 ( 2 - s ) } { 1 5 s } \right) ^ { 2 } } - \frac { 8 ( 2 - s ) } { 1 5 s } } \end{array}$ and $\begin{array} { r } { \bar { \nu } \triangleq \frac { 8 m s \left( 2 + s \left( 3 + 2 \mu \right) \right) ^ { 2 } } { 3 \left( 2 + m \right) \left( 3 2 + s \left( 3 2 + 3 0 \mu + 3 s \left( 1 2 + 5 \mu \left( 3 + \mu \right) \right) \right) \right) } } \end{array}$ . Then, in equilibrium, the following trends are observed:

$$
\frac {\partial \psi_ {1}}{\partial \mu} <   0, \frac {\partial \xi_ {L}}{\partial \mu} <   0, \left. \psi_ {1} \right| _ {\mu = \overline {{\mu}}} = 0, \left. \xi_ {L} \right| _ {m = 0} = 2,
$$

(ii) $\begin{array} { r } { \frac { \partial \psi _ { 1 } } { \partial \nu } = 0 , \frac { \partial \xi _ { L } } { \partial \nu } > 0 , } \end{array}$

(iii) $\frac { \partial | W | } { \partial \mu } > 0$ if and only if $\nu > \bar { \nu }$ , but $\frac { \partial | W | } { \partial \nu }$ is always positive, and

$$
\mathrm{(iv)} \frac {\partial^ {2} | W |}{\partial \mu \partial \nu} > 0.
$$

Proposition 3 gives us a more complete understanding of what a policymaker may want with respect to ?? and ?? . First, we find in Part (i) that an increase in $\mu$ is desirable for bringing $\psi _ { 1 }$ down but, at the same time, it also brings $\xi _ { L }$ down (not desirable). Part (ii) tells us that, when ?? increases, $\xi _ { L }$ goes up while there is no impact on $\psi _ { 1 }$ , implying that ?? , the window of intervention, expands as ?? goes up. However, as stated in Part (iii), the net impact of a higher $\mu$ on |??| could be negative unless ?? is sufficiently strong (that $\mathrm { i s } , \nu >$ ??̅). Finally, in Part (iv), we see that the two levers of public awareness, ?? and $\nu ,$ complement each other, that is, they work in a synergistic way towards widening ??.

How can the policymaker make use of these facts to curb polarization and bias? The first thing one can do is to raise $\mu$ beyond $\bar { \mu }$ such that $\psi _ { 1 }$ becomes negative. If this can be accomplished, then an indirect intervention through education itself would be sufficient, and no fiscal intervention would actually be needed. Of course, such an increase in $\mu$ could also bring $\xi _ { L }$ down. As long as $\xi _ { L }$ remains above zero, however, the market fully internalizes the externalities of bias and polarization, and nothing more is required. $\mathrm { I f } \ \xi _ { L }$ goes below zero, the policymaker can induce ?? to go up so that $\xi _ { L }$ is pushed up beyond zero.

In certain cases—for example, when ?? is large— $- \bar { \mu }$ could be too high and it may not possible to move ?? beyond it. The policymaker can still intervene, supplementing the awareness drive with a direct intervention of $\kappa \in W ;$ ; see Figure 6. In this regard, the policymaker would want to drive $\xi _ { L }$ as high as possible so that ?? remains well below $\xi _ { L }$ , thereby creating some wiggle room for implementing its policy. The larger the $W ,$ the bigger would be this wiggle room. To achieve a larger ??, policymakers could try to increase $\nu ;$ in fact, if they can drive ?? to a value larger than ??̅, the green region would start expanding as $\mu$ is increased.

In summary, our results seem to indicate the primacy of education (awareness) over enforcement (intervention). One key aspect of awareness is that it can solve the issue of bias quite comprehensively. As long as the policymaker does not intervene strongly, that is, as long as ?? is no larger than $\xi _ { L }$ , the platform would have little incentive to inject any bias. With one of the hazards out of the way, the policymaker can concentrate on polarization alone and, if needed, mitigate it with a moderate level of intervention, $\psi _ { 1 } < \kappa \leq \xi _ { L }$

## 8 An Analysis of Trolling

A study of polarization in social media is perhaps not complete unless it addresses the issue of what is colloquially referred to as trolling. According to the Merriam Webster Online Dictionary, trolling involves activities specifically meant to: (1) “antagonize (others) online by deliberately posting inflammatory, irrelevant, or offensive comments or other disruptive content,” or (2) “harass, criticize, or antagonize (someone) especially by provocatively disparaging or mocking public statements, postings, or acts.” By its very nature, trolling requires trolls to engage with a narrative that is counter-attitudinal to their own. Trolling is often followed by acrimonious arguments, half-truths, and misinformation, leading to distrust, bitterness, and even threats of violence. Thus, trolling may actually exacerbate polarization, well beyond the echo chambers induced by algorithmic nudges. Interestingly, trolling not only increases the engagement level of the focal user but its effect also spills over to other users who get stuck in the firestorm of arguments and counterarguments.

In our original setup, both profit and polarization were increasing functions of ?? ; as long as these trends persist, our results should hold qualitatively. However, now in the face of trolling behavior and the resulting additional engagement with the platform, it is not clear whether these monotonicities would be preserved. In particular, the fact that a platform could profit by nudging users towards their counter-attitudinal narrative—thereby encouraging them to troll—is new and must be accounted for in the calculus of its nudging strategy.

To incorporate this aspect into our analysis and check for robustness, we now consider a setup in which each user has a trolling tendency, denoted ?? ; it represents the probability that a user will start behaving like a troll at any instant. While trolling, users exhibit a higher proclivity towards the counter-attitudinal narrative; thus, user ?? is now assumed to behave like user $1 - x$ . Users are heterogeneous in their trolling tendencies, and we assume that ?? is uniformly distributed over [0, ??]. Even though ?? can have any value between 0 and 1, users’ trolling behavior should not overshadow their normal engagement, so we expect ?? to be no more than ${ \frac { 1 } { 2 } } .$

Assumption 4: Users are indexed by the tuple $\langle x , y , \zeta \rangle ,$ where ?? and ?? are as in Assumption 1, and ?? is the trolling tendency. When trolling, users at ?? behave like a user at $1 - x .$ . Users are distributed in accordance with the following probability density function:

$$
f (x, y, \zeta) = \left\{ \begin{array}{l l} \frac {1}{\tau}, & \quad \text {if} \langle x, y, \zeta \rangle \in [ 0, 1 ] \times [ 0, 1 ] \times [ 0, \tau ], \\ 0, & \quad \text {otherwise.} \end{array} \right.
$$

Therefore, users can engage with the platform in two ways: (1) with probability $1 - \zeta$ , users behave normally, preferring to engage with their proattitudinal narrative, or (2) with probability ?? , users troll, seeking to engage more with the counterattitudinal one. When users engage normally, there is little spillover effect, so every engagement counts as 1. When they troll, however, their actions generate additional engagement by inducing others to engage, so each engagement counts as $1 + \eta \colon$

Assumption 5: Every trolling engagement generates activities that are 1 + ?? times the activities generated by a normal engagement, where $\eta \in$ [0,1] is the engagement boost from trolling.

We are now ready to quantify the platform’s profit and polarization for this extended setup. As derived in Section 5, for a user $\langle x , y , \zeta \rangle$ behaving normally, the probabilities of engaging with narratives A and B would respectively $P _ { a N } ( x ) = ( 1 - x ) \left( p _ { a } ( x ) + \bigl ( 1 - p _ { N } ( x ) \bigr ) ( 1 - s ) \right)$ and $P _ { b N } ( x ) = x \left( p _ { b } ( x ) + { \left( 1 - p _ { N } ( x ) \right) } ( 1 - s ) \right)$ where $p _ { N } ( x ) = ( 1 - x ) p _ { a } ( x ) + x p _ { b } ( x )$ is the probability of a successful nudge when a user behaves normally. When trolling, the probabilities of engaging with narratives A and B would change to $P _ { a T } ( x ) = x ( p _ { a } ( x ) + ( 1 - \frac { } { }$ $p _ { T } ( x ) { \big ) } ( 1 - s ) { \bigg ) }$ and $P _ { b T } ( x ) = ( 1 - x ) ( p _ { b } ( x ) + ( 1 - )$ $p _ { T } ( x ) { \big ) } ( 1 - s ) { \bigg ) }$ , respectively, where ${ p } _ { T } ( x ) = x p _ { a } ( x )$ + $( 1 - x ) p _ { b } ( x )$ is the probability of a successful nudge when a user trolls. The profit from users’ normal behavior can then be calculated as before:

$$
\begin{array}{c} \pi_ {N} = \underbrace {(1 + m) \int_ {0} ^ {1} P _ {a N} (x) d x} _ {\text {Normal visits to A}} + \underbrace {(1) \int_ {0} ^ {1} P _ {b N} (x) d x} _ {\text {Normal visits to B}} \\ = \left(1 + \frac {m}{2}\right) \left(\frac {2 - s}{2} + \frac {s z}{8}\right) + \frac {m w (2 + s)}{1 2}. \end{array}
$$

Now, the profit from users’ trolling behavior should be given by:

$$
\begin{array}{l} \pi_ {T} = \underbrace {(1 + \eta) (1 + m) \int_ {0} ^ {1} P _ {a T} (x) d x} _ {\text { Trolling   visits   to   A }} + \underbrace {(1 + \eta) (1) \int_ {0} ^ {1} P _ {b T} (x) d x} _ {\text { Trolling   visits   to   B }} \\ = (1 + \eta) \left(\left(1 + \frac {m}{2}\right) \left(\frac {2 - s}{2} - \frac {s z}{8}\right) + \frac {m w (2 + s)}{1 2}\right). \end{array}
$$

Interestingly, while $\pi _ { N }$ increases with $z \ , \ \pi _ { T }$ is a decreasing function of ??. By aggregating over all ??, the total profit can then be calculated as:

$$
\begin{array}{l} \pi = \frac {1}{\tau} \int_ {0} ^ {\tau} \big ((1 - \zeta) \pi_ {N} + \zeta \pi_ {T} \big) d \zeta \\ = \Big (1 + \frac {\eta \tau}{2} \Big) \Bigg (\Big (1 + \frac {m}{2} \Big) \Big (\frac {2 - s}{2} \Big) + \frac {m w (2 + s)}{1 2} \Bigg) \\ \qquad + \frac {s z}{8} \Big (1 + \frac {m}{2} \Big) \Bigg (1 - \tau \Big (1 + \frac {\eta}{2} \Big) \Bigg). \end{array}
$$

It is clear that ?? is increasing in ?? only if $\begin{array} { r } { \tau < \gamma _ { 1 } \triangleq \frac { 2 } { 2 + \eta } . } \end{array}$ However, if $\tau > \gamma _ { 1 }$ —that is, if the trolling effect is sufficiently large—the profit could become decreasing and the platform may intentionally reduce ?? to drive its profit up; our original results might not hold in that case.

![](/api/attachments/KGUU7NJ7/fulltext/images/65fef50f6bac78dcf8d48c73eab2634e15564c577498707a3f7cfd1c6bf2470e.jpg)  
Figure 7. Impact of Trolling on Polarization; ?? = ??. ????

We now turn our attention to polarization, which also has two components: (1) the original component, $D _ { N } .$ arising out of normal behavior, and (2) a new part, $D _ { T } ,$ for trolling. $D _ { N }$ must exactly be the same as ?? in Lemma $^ { 2 , }$ so $\begin{array} { r } { D _ { N } = \frac { 2 - s } { 4 } + \frac { z ( 2 + 3 s ) } { 3 0 } } \end{array}$ . Since both pro- and counterattitudinal engagements associated with trolling generate acrimony and division, we count them both as contributing to polarization:<sup>12</sup>

$$
\begin{array}{c} D _ {T} = \underbrace {(1 + \eta) \int_ {0} ^ {1} P _ {a T} (x) d x} _ {\text {Trolling visits to A}} + \underbrace {(1 + \eta) \int_ {0} ^ {1} P _ {b T} (x) d x} _ {\text {Trolling visits to B}} \\ = (1 + \eta) \left(\frac {2 - s}{2} - \frac {s z}{8}\right). \end{array}
$$

Aggregating over all ??, we get:

$$
\begin{array}{l} D = \frac {1}{\tau} \int_ {0} ^ {\tau} \big ((1 - \zeta) D _ {N} + \zeta D _ {T} \big) d \zeta \\ = \Big (1 + \frac {\tau}{2} + \eta \tau \Big) \Big (\frac {2 - s}{4} \Big) + \frac {z \Big (8 (2 - \tau) + 3 s \big (8 - \tau (9 + 5 \eta) \big) \Big)}{2 4 0}. \end{array}
$$

Therefore, polarization is increasing in ?? as long as $8 ( 2 - \tau ) + 3 s \bigl ( 8 - \tau ( 9 + 5 \eta ) \bigr ) > 0$ , that is, as long as $\tau <$ $\begin{array} { r } { \gamma _ { 2 } \triangleq \frac { 8 \left( 2 + 3 s \right) } { 8 + 3 s ( 5 \eta + 9 ) } } \end{array}$ . We summarize this analysis in the following proposition:

Proposition 4: Let $\begin{array} { r } { \gamma _ { 1 } = \frac { 2 } { 2 + \eta } } \end{array}$ and $\begin{array} { r } { \gamma _ { 2 } = \frac { 8 \left( 2 + 3 s \right) } { 8 + 3 s \left( 5 \eta + 9 \right) } . } \end{array}$ . When users’ trolling behavior is accounted for, both profit and polarization are increasing in ?? if $\tau < \gamma _ { 1 } ,$ , and both are decreasing $\mathrm { i f } \ \tau > \gamma _ { 2 } . \ \mathrm { I f } \ \gamma _ { 1 } \leq \tau \leq \gamma _ { 2 }$ , however, profit is decreasing in ?? but polarization is increasing. Irrespective of ?? , profit is always increasing in ?? , whereas polarization is independent of ??.

Proposition 4 is illustrated in Figure 7, where the entire $( \eta , \tau )$ space gets partitioned into three distinct regions. In the green region where $\tau < \gamma _ { 1 }$ , profit and polarization are both increasing in ??, just as they were in our original setup. In the blue region where $\gamma _ { 1 } \leq \tau \leq \gamma _ { 2 }$ , profit is decreasing in ?? but polarization is increasing. Finally, in the red region where $\tau > \gamma _ { 2 }$ , both profit and polarization are decreasing in ??.

What do Proposition 4 and Figure 7 tell us about the robustness of our original analysis? We contend that the green region—where profit and polarization are both increasing in ??—best represents reality. First, in the blue region, there is no misalignment of incentives. Since polarization is increasing in ?? there, a policymaker would want as low a ?? as possible and, at the same time, the platform would also want a low ?? because its profit is decreasing in ??. Naturally, were the blue region the true reflection of reality, there would be no externality and no need for a policy intervention to achieve the first best. In fact, if the outcome were in the blue region, much of the policy debate would be rendered pointless. Second, the red region is also not practical. In this extreme case, where ?? and ?? are both large, the platform sets $z = 0 ,$ but now, doing so increases the level of polarization. There is thus a reverse misalignment of incentives in this case—the platform wants to reduce the formation of echo chambers, but the policymaker would prefer just the opposite.

users dig their heels in even more; if that occurs, trolling could lead to more polarization (Bail et al. 2018). The net effect is not necessarily clear. In this study, we only consider the second effect.

Evidently, neither the blue region nor the red is consistent with practical observations; the green region appears to be the only one that is indicative of the contextual reality. Since the platform’s profit and polarization are increasing in ?? in this region, the game becomes similar to the original setup, and all our results hold qualitatively. Furthermore, as mentioned earlier, we expect ?? to be less than ${ \frac { 1 } { 2 } } ,$ , and since $\gamma _ { 1 }$ is always greater than $\frac { 1 } { 2 }$ , our analysis appears robust to the extension that accounts for users’ trolling behavior.

## 9 Discussion

Our analysis provides several broad implications for public policy. First, from Theorem 1, we conclude that a platform’s profit motivation may indeed lead it to adopt a nudging strategy that materializes in a higher level of polarization. Therefore, our results lend support to common allegations that social media platforms may be responsible for creating more division within society. We also found that, notwithstanding their role in polarizing the user base, such platforms have no incentive to behave in a biased manner, especially when there is little structural bias in the market and the platforms are left alone by policymakers to maximize their own profits. In other words, we did not find any evidence in support of the allegations of bias against social media platforms.

Next, recognizing the fact that policymakers can hardly afford to allow polarization to run amok within society, we consider what would happen if policymakers were to intervene directly, with a tax or penalty. From Theorem 2, we determined that a fiscal intervention could indeed curb the extent of polarization but would do so only at the expense of injecting bias, possibly even when there is no structural bias within the system. In fact, Theorem 2′ shows that the presence of structural bias makes the situation even worse. Taken together, these results point to the difficulty policymakers face in this context. On the one hand, they cannot allow societal division to run rampant; on the other hand, interventions to curb polarization may manifest as bias in the platform’s nudging strategy.

We also consider the case where users—at least some of them—become aware of the societal costs brought on by the platform so that they can start internalizing some of these costs. Interestingly, the story changes when users become aware. When users start internalizing societal costs and displaying sufficient resistance towards division and bias, a platform may be forced to change its nudging strategy to one that mitigates these issues. In Theorem 3, we observe that when education to foster awareness among users is used in conjunction with some fiscal intervention, a large region appears in the parameter space where the socially desirable outcome emerges. In fact, Proposition 3 tells us that, as long as the resistance towards polarization is significant, that is, as long as $\mu >$ ??̅ , the platform would curb polarization even without direct fiscal intervention and it would do so without injecting further bias into its nudging strategy. Viewed differently, Theorem 3 and Proposition 3 provide a clear action path for policymakers—instead of directly intervening with a tax, policymakers can do significantly better by educating users about these issues so that they can resist the detrimental effects of social media.

Now, education also has its limitations. In particular, when $\mu < \bar { \mu }$ and there is no intervention, the platform goes about adopting a nudging strategy that completely ignores users’ resistance, so a high level of polarization ensues. In such a situation, policymakers could use a judicious mix of education and intervention. From Theorem 3, we found that, when users internalize some of the societal costs, policymakers can indeed curb both polarization and bias by setting a tax rate that is moderate, i.e., neither too low nor too high. More specifically, if policymakers were to impose a ?? such that $\psi _ { 1 } \leq \kappa \leq \xi _ { L } ,$ the nudging strategy adopted by the platform in equilibrium could lead to low polarization as well as low bias. However, if policymakers were to become overzealous and impose a $\kappa > \xi _ { L }$ , the platform would become biased. At the other extreme, if ?? is too small, that is, if it is less than $\psi _ { 1 }$ , the intervention has little impact on polarization.

## 10 Conclusion

Polarization and bias—two of the most important adverse effects of social media—have long been a public policy concern. In this paper, we set up a positive modeling experiment to study a platform’s incentives and policymakers’ choices. Our setup considers a heterogeneous user base with different benefits from engaging with the platform and different proclivities towards opposing narratives, a recommendation engine to implement the platform’s nudging strategy, and a pool of advertisers that may or may not be biased.

We find that, consistent with common allegations, a platform does have incentives to increase engagement even though it may create more polarization within society. However, the platform has little incentive to be biased, unless there is a large structural bias in the ad pool. What is particularly interesting is that, if policymakers try to fiscally intervene with a tax or penalty on the social media platform, they could indeed succeed in forcing the platform to reduce polarization, but this intervention would also inject bias. This duality between polarization and bias, which allows policymakers to curb one or the other but not both at the same time, can only be broken when users become aware about these issues. This implies that policymakers would be better off intervening indirectly, through public education and fostering awareness, rather than cracking down on polarization using the fiscal whip. Only when an adequate level of public awareness cannot be attained should policymakers supplement it with a moderate level of fiscal intervention.

Our work is not without limitations. Intentionally, we developed a parsimonious model that makes several simplifying assumptions. For example, we assume that users are uniformly distributed over a unit square. In reality, though, the distribution need not be uniform; similar to the case of a normal distribution, we are likely to see more probability mass towards the middle of the square. We also assume that policymakers use a simple linear tax rate, whereas, in practice, they could deploy a nonlinear tax structure. Further, even though there is some anecdotal evidence that supports our insights, a rigorous field experiment would be required to validate our findings. Despite these limitations, we consider this exercise worthwhile to the extent that it highlights the duality between polarization and bias in social media and provides guidelines in terms of how policymakers should approach these issues.

## Acknowledgments

The authors are grateful for the valuable comments and guidance received from the referees and editors of this journal.

## References

Allcott, H., Braghieri, L., Eichmeyer, S., & Gentzkow, M. (2020). The welfare effects of social media. American Economic Review, 110(3), 629-676.

Allcott, H., Gentzkow, M., & Yu, C. (2019). Trends in the diffusion of misinformation on social media. Research & Politics, 6(2), 1-8.

Alter, A. (2018). Irresistible: The rise of addictive technology and the business of keeping us hooked. Penguin Press.

Andreottola, G., & Li, C. (2024). Polarization and policy design. Journal of Political Economy Microeconomics, 2(1). https://www.journals. uchicago.edu/doi/10.1086/726844

Arora, S., Singh, G., Chakraborty, A., & Maity, M. (2022). Polarization and social media: A systematic review and research agenda. Technological Forecasting & Social Change, 183, 1-17.

Auxier, B. (2020). 64% of Americans say social media have a mostly negative effect on the way things are going in the U.S. today. Pew Research Center. https://www.pewresearch.org/shortreads/2020/10/15/64-of-americans-say-socialmedia-have-a-mostly-negative-effect-on-theway-things-are-going-in-the-u-s-today/

Azzimonti, M., & Fernandes, M. (2023). Social media networks, fake news, and polarization. European Journal of Political Economy, 76, 1- 25.

Bail, C., Argyle, L., & Brown, T. (2018). Exposure to opposing views on social media can increase political polarization. PNAS, 115(37), 9216- 9221.

Bakshy, E., Messing, S., & Adamic, L. (2015). Exposure to ideologically diverse news and opinion on Facebook. Science, 348(6239), 1130- 1132.

Barberá P. (2020). Social media, echo chambers, and political polarization. In N. Persily & J. Tucker (Eds.), Social media and democracy: The state of the field, prospects for reform (pp. 34-55). Cambridge University Press.

Beattie, G., Durante, R., Knight, B., & Sen, A. (2021). Advertising spending and media bias: Evidence from news coverage of car safety recalls. Management Science, 67(2), 698-719.

Brady, W., Crockett, M., & van Bavel, J. (2020). The MAD model of moral contagion: The role of motivation, attention, and design in the spread of moralized content online. Perspectives on Psychological Science, 15(4), 978-1010.

Brady, W., Wills, J., Jost, J., Tucker, J., & van Bavel, J. V. (2017). Emotion shapes the diffusion of moralized content in social networks. Proceedings of the National Academy of Sciences, 114(28), 7313-7318.

Broniatowski, D., Jamison, A., Qi, S., AlKulaib, L., Chen, T., Benton, A., Quinn, S., & Dredze, M. (2018). Weaponized health communication: Twitter bots and Russian trolls amplify the vaccine debate. American Journal of Public Health, 108(10), 1378-1384.

Brown, M., & Snider, M. (2021). Facebook whistleblower’s explosive testimony: Company makes “disastrous” choices, prioritizes profit. USA Today. https://www.usatoday.com/story/ tech/2021/10/05/facebook-whistleblower-liveupdates-frances-haugen-speakscongress/6001909001/

Bulow, J., Geanakoplos, J., & Klemperer, P. (1985). Multimarket oligopoly: Strategic substitutes and complements. Journal of Political Economy, 93(3), 488-511.

Chaffey, D. (2023). Global social media statistics research summary 2023. Smart Insights. Retrieved June 17, 2023 from https://www. smartinsights.com/social-media-marketing/ social-media-strategy/new-global-social-mediaresearch/

Chan, T., Lee, Z., Skoumpopoulou, D., & Situmeang, F. (2024). Judging the wrongness of firms in social media firestorms: The heuristic and systematic information processing perspective. Journal of the Association for Information Systems, 25(2), 463-500.

Cinelli, M., De Francisci Morales, G., Galeazzi, A., Quattrociocchi, W., & Starnini, M. (2021). The echo chamber effect on social media. PNAS, 118(9), 1-8.

Cowgill, B., & Tucker, C. (2020). Algorithmic fairness and economics. Social Science Research Network.

Dey, D., Ghoshal, A., & Lahiri, A. (2021). Circumventing circumvention: An economic analysis of the role of education and enforcement. Management Science, 68(4), 2914- 2931.

Diakopoulos, N. (2015). Algorithmic accountability: Journalistic investigation of computational power structures. Digital Journalism, 3(3), 398- 415.

Druckman, J., Klar, S., Krupnikov, Y., Levendusky, M., & Ryan, J. (2022). (Mis)estimating affective

polarization. The Journal of Politics, 84(2), 1106-1117.

Etzioni, A., & Etzioni, O. (2017). Incorporating ethics into artificial intelligence. Journal of Ethics, 21(4), 403-41.

Fazelpour, S., & Danks, D. (2019). Algorithmic bias: Senses, sources, solutions. Philosophy Compass, 16(8), 1-16.

Feighery, E., Altman, D., & Shaffer, G. (1991). The effects of combining education and enforcement to reduce tobacco sales to minors. Journal of the American Medical Association, 266(22), 3168- 3171.

Feldman, A., & Serrano, R. (2006). Welfare Economics and Social Choice Theory. Springer.

Fu, R., Aseri, M., Singh, P., & Srinivasan, K. (2022). “Un”fair machine learning algorithms. Management Science, 68(6), 4173-4195.

Gentzkow, M., & Shapiro, J. (2017). Media bias and reputation. Journal of Political Economy, 114(2), 280- 316.

Guess, A., Nyhan, B., & Reifler, J. (2020). Exposure to untrustworthy websites in the 2016 US election. Nature Human Behavior, 4(5), 472-480.

Heatherly, K., Lu, Y., & Lee, J. (2017). Filtering out the other side? cross-cutting and like-minded discussions on social networking sites. New Media and Society, 19(8), 1271-1289.

Ichihashi, S., & Kim, B.-C. (2023). Addictive platforms. Management Science, 69(2), 1127-1145.

Iyengar, S., & Hahn, K. (2009). Red media, blue media: Evidence of ideological selectivity in media use. Journal of Communication, 59(1), 19-39.

Kramer, A., Guillory, J., & Hancock, J. (2014). Experimental evidence of massive-scale emotional contagion through social networks. PNAS, 111(24), 8788-8790.

Laffont, J.-J. (1989). Externalities. In J. Eatwell, M. Millgate, & P. Newman (Eds.), Allocation, information and markets (pp. 112-116). Palgrave Macmillan.

Lambrecht, A., & Tucker, C. (2019). Algorithmic bias? An empirical study of apparent gender-based discrimination in the display of STEM career ads. Management Science, 65(7), 2966-2981.

Lu, S. (2021). Algorithmic opacity, private accountability, and corporate social disclosure in the age of artificial intelligence. Vanderbilt Journal of Entertainment and Technology Law, 23(1), 99-159.

Luo, X. (2017). Collective mass media bias, social media, and non-partisans. Economics Letters, 156, 78-81.

Mak, A. (2021). The Facebook whistleblower finally got republicans to stop yapping about anticonservative bias. Slate. https://slate.com/ technology/2021/10/facebook-whistleblowerfrances-haugen-hearing-republicansdemocrats.html

Matook, S., Dennis, A., & Wang, Y. (2022). User comments in social media firestorms: A mixedmethod study of purpose, tone, and motivation. Journal of Management Information Systems, 39(3), 673-705.

Overgaard, C., & Wooley, S. (2022). How social media platforms can reduce polarization. Brookings Institute Report.

Panch, T., Mattie, H., & Atun, R. (2019). Artificial intelligence and algorithmic bias: Implications for health systems. Journal of Global Health, 9(2), 1-5.

Pariser, E. (2012). The filter bubble: How the new personalized web is changing what we read and how we think. Penguin.

Pennycook, G., Bear, A., Collins, E., & Rand, D. (2020). The implied truth effect: Attaching warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings. Management Science, 66(11), 4944- 4957.

Pfeffer, J., Zorbach, T., & Carley, K. (2014). Understanding online firestorms: Negative word-of-mouth dynamics in social media networks. Journal of Marketing Communications, 20(1-2), 117-128.

Pronin, E., Gilovich, T., & Ross, L. (2004). Objectivity in the eye of the beholder: Divergent perceptions of bias in self versus others. Psychological Review, 111(3), 781-799.

Settle, J. (2018). Frenemies: How social media polarizes America. Cambridge University Press.

Silva, S., & Kenney, M. (2019). Algorithms, platforms, and ethnic bias. Communications of the ACM, 62(11), 37-39.

Suhay, E., Bello-Pardo, E., & Maurer, B. (2018). The polarizing effects of online partisan criticism: Evidence from two experiments. The International Journal of Press/Politics, 23(1), 95-115.

Sunstein, C. (2018). #Republic: Divided democracy in the age of social media. Princeton University Press.

Tene, O., & Polonetsky, J. (2013). Big data for all: Privacy and user control in the age of analytics. Northwestern Journal of Technology and Intellectual Property, 11(5). https://scholarlycommons.law.northwestern.ed u/njtip/vol11/iss5/1

Tingle, R., Newman, J., & Howard, H. (2021). “Instagram may NEVER be safe for 14-yearolds.” Dailymail. https://www.dailymail.co.uk/ news/article-10128197/Facebook-whistle blower-Frances-Haugen-gives-evidence-MPsscrutinising-online-safety-bill.html

Tirole, J. (1994). The theory of industrial organization. MIT Press.

Tukekci, Z. (2017). Twitter and tear gas: The power and fragility of networked protest. Yale University Press.

van Bavel, J., Rathje, S., Harris, E., Robertson, C., & Sternisko, A. (2021). How social media shapes polarization. Trends in Cognitive Sciences, 25(11), 913-916.

Yuan, D., Aseri, M., & Mukhopadhyay, T. (2023). Is fair advertising good for platforms? SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstrac t\_id=4444865

Zhou, X., & Zafarani, R. (2020). A survey of fake news: Fundamental theories, detection methods, and opportunities. ACM Computing Surveys, 53(5), 1-40.

## Appendix A: Proofs

Proof of Lemma 1 and Proposition 1: Integrating $e ( x ) = p ( x ) + ( 1 - p ( x ) ) ( 1 - s )$ and substituting $z = \rho ( 1 - \alpha - \beta )$ we get Lemma 2. Since $\begin{array} { r } { E = \frac { 2 - s } { 2 } + \frac { s z } { 8 } } \end{array}$ is a linearly increasing function of ??, maximizing ?? will result in the boundary solution of $z ^ { * } = \rho$ as stated in Proposition 1.

Proof of Lemma 2 and Theorem 1: To prove Lemma 2, simply integrate (1) and substitute $z = \rho ( 1 - \alpha - \beta )$ . Since $\begin{array} { r } { D = \frac { 2 - s } { 4 } + \frac { z ( 2 + 3 s ) } { 3 0 } } \end{array}$ is a linearly increasing function of ?? , ?? would reach its maximum when $z = \rho$ . According to Proposition 1, therefore, the platform’s nudging strategy in equilibrium would create maximum polarization. Further, $z = \rho ( 1 - \alpha - \beta ) = \rho$ implies that $\alpha = \beta = 0$ resulting in $w = 0$ , so no bias would be shown by the platform.

Proof of Lemma 3 and Theorem 2: Since $\frac { \partial ( E - \kappa D ) } { \partial z }$ is positive when $\kappa \leq \chi$ and negative otherwise, the platform’s nudging strategy in equilibrium is given by:

$$
z ^ {*} = \left\{ \begin{array}{l l} \rho , & \quad \text { if   } \kappa \leq \chi \triangleq \frac {1 5 s}{4 (2 + 3 s)}, \\ 0, & \quad \text { otherwise }. \end{array} \right.
$$

Therefore, when $\kappa \leq \chi , \alpha = \beta = 0$ , and we should expect maximum polarization but no bias. On the other hand, when $\kappa > \chi , \alpha + \beta = 1$ , so polarization is minimum. Further, since the platform is free to choose any ?? and $\beta$ satisfying $\alpha +$ $\beta = 1$ , if it has any inherent bias, that bias would show up as $\alpha \neq \beta { \mathrm { ~ o r ~ } } w > 0$

Proof of Proposition 2: Since $\frac { \partial \pi } { \partial z }$ and $\frac { \partial \pi } { \partial w }$ are both positive, it is in the platform’s interest to increase both ?? and ??. In optimality, therefore, the constraint $\frac { z } { \rho } + w \leq 1$ should be binding; so, $\begin{array} { r } { w = 1 - \frac { z } { \rho } , } \end{array}$ substituting which we get:

$$
\pi = \frac {(3 + m) (4 - s) - 6}{6} + \frac {z}{4} \left(\frac {s (2 + m)}{4} - \frac {m (2 + s)}{3 \rho}\right).
$$

It is clear that ?? is increasing in ?? if and only $\begin{array} { r } { \frac { s ( 2 + m ) } { 4 } - \frac { m ( 2 + s ) } { 3 \rho } } \end{array}$ is positive, that is, iff $\begin{array} { r } { \rho > \frac { 4 m ( 2 + s ) } { 3 s ( 2 + m ) } . } \end{array}$ . Since $\begin{array} { r } { w ^ { \ast } = 1 - \frac { z ^ { \ast } } { \rho } , } \end{array}$ the equilibrium is now given by:

$$
(z ^ {*}, w ^ {*}) = \left\{ \begin{array}{l l} (\rho , 0), & \quad \text {if} \rho \geq \bar {\rho}, \\ (0, 1), & \quad \text {otherwise}. \end{array} \right.
$$

Naturally, if $\rho \geq { \bar { \rho } } ,$ , we should expect maximum polarization but no bias. On the other hand, if $\rho < \bar { \rho } ,$ , we would get minimum polarization but maximum bias.

Proof of Lemma ${ \mathbf { } } ^ { \prime }$ and Theorem $\pmb { 2 ^ { \prime } } \pmb { \mathrm { : } }$ Note that $\pi - \kappa D$ is increasing in ??; it is also increasing in ?? as long as $\frac { s ( 2 + m ) } { 8 } -$ $\frac { \kappa ( 2 + 3 s ) } { 1 5 } > 0$ , which is equivalent to $\begin{array} { r } { \kappa < \frac { 1 5 s ( 2 + m ) } { 8 ( 2 + 3 s ) } } \end{array}$ . Therefore, if $\begin{array} { r } { \kappa > \frac { 1 5 s ( 2 + m ) } { 8 ( 2 + 3 s ) } . } \end{array}$ , the optimal solution would be $( z ^ { * } , w ^ { * } ) =$ (0,1). On the other hand, if $\begin{array} { r } { \kappa \leq \frac { 1 5 s ( 2 + m ) } { 8 ( 2 + 3 s ) } , \pi - \kappa D } \end{array}$ is increasing in both ?? and ??, and the constraint $\frac { z } { \rho } + w \leq 1$ would become binding. Substituting $\begin{array} { r } { w = 1 - \frac { z } { \rho } , } \end{array}$ we get:

$$
\pi - \kappa D = \frac {(2 - s) (2 + m - \kappa)}{4} + \frac {m (2 + s)}{1 2} + \frac {z}{2} \bigg (\frac {s (2 + m)}{8} - \frac {\kappa (2 + 3 s)}{1 5} - \frac {m (2 + s)}{6 \rho} \bigg),
$$

which is decreasing in ?? if and only if $\begin{array} { r } { \kappa > \frac { 1 5 s ( 2 + m ) } { 8 ( 2 + 3 s ) } - \frac { 5 m ( 2 + s ) } { 2 \rho ( 2 + 3 s ) } . } \end{array}$

Since $\frac { \partial ( E - \kappa D ) } { \partial z }$ is positive when $\begin{array} { r } { \kappa \leq \chi \triangleq \frac { 1 5 s ( 2 + m ) } { 8 ( 2 + 3 s ) } - \frac { 5 m ( 2 + s ) } { 2 \rho ( 2 + 3 s ) } } \end{array}$ and negative otherwise, the platform’s nudging strategy in equilibrium is given by:

$$
(z ^ {*}, w ^ {*}) = \left\{ \begin{array}{l l} (\rho , 0), & \quad \text {if} \kappa \leq \chi , \\ (0, 1), & \quad \text {otherwise}. \end{array} \right.
$$

Therefore, if $\kappa \leq \chi$ , we should expect maximum polarization but no bias. In contrast, if $\kappa > \chi ,$ , we would get minimum polarization but maximum bias.

Proof of Lemma 4 and Theorem 3: The platform’s objective function in this case is given by:

$$
\pi - \kappa D = \frac {s \left(\frac {\kappa (1 5 - 6 Z)}{2} - \frac {(2 + m) (\mu z (1 7 - 2 Z) + 1 5 (8 - 2 Z))}{1 6} + \frac {m w (1 5 (1 + \mu) - 2 \mu Z)}{6}\right) + (1 - w \nu) (3 0 + 5 m (3 + w) - \kappa (1 5 + 2 Z))}{3 0 + \mu (1 5 + 2 Z)},
$$

where $Z = { \frac { z } { \rho } } .$ This objective function is convex in ?? because:

$$
\frac {\partial^ {2} (\pi - \kappa D)}{\partial Z ^ {2}} = \frac {2 0 \mu (6 \kappa + \mu (6 + m (3 + w))) (s (3 + 2 \mu) + 2 (1 - \nu w))}{(3 0 + \mu (1 5 + 2 Z)) ^ {3}} > 0,
$$

unless $\begin{array} { r } { \nu w > 1 + \frac { s ( 3 + 2 \mu ) } { 2 } } \end{array}$ , a situation that can be shown as impossible in equilibrium—when ?? is high, the platform chooses a small $w ,$ and when the platform chooses a large ??, ?? must have been small. In other words, we should expect a boundary solution for ??, that is, either $z ^ { * } = 0 \mathrm { o r } z ^ { * } = \rho . \mathrm { I f } z ^ { * } = \rho , w ^ { * }$ must be zero. If, on the other hand, $z ^ { * } = 0$ , we can substitute that into the objective function to get:

$$
\pi - \kappa D = \frac {m (2 (3 + w) (1 - w \nu) - s (3 - w (1 + \mu))) + 3 (2 - \kappa) (2 - s - 2 w \nu)}{6 (2 + \mu)}.
$$

This objective function is concave with respect to ?? because:

$$
\frac {\partial^ {2} (\pi - \kappa D)}{\partial w ^ {2}} = - \frac {2 m \nu}{3 (2 + \mu)} <   0,
$$

Therefore, solving $\begin{array} { r } { \frac { \partial ( \pi - \kappa D ) } { \partial w } = 0 } \end{array}$ , we can get:

$$
w ^ {*} = \frac {2 + s (1 + \mu)}{4 \nu} - \frac {3 (2 + m - \kappa)}{2 m}.
$$

Since $0 \leq w ^ { * } \leq 1$ , this solution is valid only if $\xi _ { L } \le \kappa \le \xi _ { U }$

The theorem follows from comparing the objective function values for these different solutions in a pairwise fashion. More specifically, $\left( z ^ { \ast } , w ^ { \ast } \right) = \left( \rho , 0 \right)$ dominates $( z ^ { * } , w ^ { * } ) = ( 0 , 0 ) { \mathrm { ~ i f ~ } } \kappa < \psi _ { 1 } ; ( \rho , 0 )$ dominates $( 0 , w ^ { * } )$ for all $w ^ { * } \in ( 0 , 1 )$ if $\kappa < \psi _ { 2 } ;$ and $( \rho , 0 )$ dominates (0,1) if and only if $\kappa < \chi ,$ , where $\psi _ { 1 } , \psi _ { 2 }$ , and $\chi$ are as stated in the theorem.

## Proof of Proposition 3:

(i) Note that $\begin{array} { r } { \frac { \partial \psi _ { 1 } } { \partial \mu } = - \frac { \left( 2 + m \right) \left( 3 2 + s \left( 3 2 + 3 0 \mu + 3 s \left( 1 2 + 5 \mu \left( 3 + \mu \right) \right) \right) \right) } { 1 6 \left( 2 + s \left( 3 + 2 \mu \right) \right) ^ { 2 } } } \end{array}$ , which is clearly negative. Similarly, $\frac { \partial \xi _ { L } } { \partial \mu } = - \frac { m s } { 6 \nu }$ , which is also negative. Solving $\psi _ { 1 } = 0$ for ??, we get $\begin{array} { r } { \overline { { \mu } } = \sqrt { 4 + \left( \frac { 8 ( 2 - s ) } { 1 5 s } \right) ^ { 2 } } - \frac { 8 ( 2 - s ) } { 1 5 s } } \end{array}$ ; therefore, $\psi _ { 1 } | _ { \mu = \overline { { \mu } } } = 0$ . Finally, setting $m = 0 .$ , we get $\xi _ { L } | _ { m = 0 } = 2$

(ii) Since $\psi _ { 1 }$ does not depend on $\nu , \frac { \partial \psi _ { 1 } } { \partial \nu }$ must be zero. On the other hand, $\begin{array} { r } { \frac { \partial \xi _ { L } } { \partial \nu } = \frac { m \left( 2 + s \left( 1 + \mu \right) \right) } { 6 \nu ^ { 2 } } } \end{array}$ , which is clearly positive.

(iii) It is easy to see that $\begin{array} { r } { \frac { \partial | W | } { \partial \nu } = \frac { \partial \xi _ { L } } { \partial \nu } = \frac { m s ( 2 + \mu ) } { 8 \nu ^ { 2 } } > 0 } \end{array}$ . In contrast, $\begin{array} { r } { \frac { \partial | W | } { \partial \mu } = \frac { \left( 2 + m \right) \left( 3 2 + s \left( 3 2 + 3 0 \mu + 3 s \left( 1 2 + 5 \mu \left( 3 + \mu \right) \right) \right) \right) } { 1 6 \left( 2 + s \left( 3 + 2 \mu \right) \right) ^ { 2 } } - \frac { m s } { 6 \nu } , } \end{array}$ which is positive for large ?? but negative otherwise. Solving $\frac { \partial | W | } { \partial \mu }$ for ??, we get $\begin{array} { r } { \bar { \nu } = \frac { 8 m s \left( 2 + s \left( 3 + 2 \mu \right) \right) ^ { 2 } } { 3 \left( 2 + m \right) \left( 3 2 + s \left( 3 2 + 3 0 \mu + 3 s \left( 1 2 + 5 \mu \left( 3 + \mu \right) \right) \right) \right) } , } \end{array}$ Therefore, if and only if $\nu > \bar { \nu } ,$ we will $\mathrm { g e t } { \frac { \partial | W | } { \partial \mu } } > 0$

(iv) To check for complementarity between $\mu$ and ??, we find that $\frac { \partial ^ { 2 } | W | } { \partial \mu \partial \nu } = \frac { \partial ^ { 2 } \xi _ { L } } { \partial \mu \partial \nu } = \frac { m s } { 6 \nu ^ { 2 } } > 0$

Proof of Proposition 4: It is clear that $\begin{array} { c c c } { \frac { \partial \pi } { \partial z } = \frac { s } { 8 } \Big ( 1 + \frac { m } { 2 } \Big ) \left( 1 - \tau \left( 1 + \frac { \eta } { 2 } \right) \right) } \end{array}$ is positive if and only if $\begin{array} { r } { \tau < \gamma _ { 1 } \triangleq \frac { 2 } { 2 + \eta } . } \end{array}$ Similarly, $\begin{array} { r } { \frac { \partial D } { \partial z } = \frac { 8 \left( 2 - \tau \right) + 3 s \left( 8 - \tau \left( 9 + 5 \eta \right) \right) } { 2 4 0 } } \end{array}$ is positive as long as $8 ( 2 - \tau ) + 3 s \bigl ( 8 - \tau ( 9 + 5 \eta ) \bigr ) > 0$ , that is, as long as $\begin{array} { r } { \tau < \gamma _ { 2 } \triangleq \frac { 8 \left( 2 + 3 s \right) } { 8 + 3 s \left( 5 \eta + 9 \right) } . } \end{array}$ This completes the proof.

## Appendix B: A More Detailed Analysis of Public Awareness

Recall that the analysis in Section 6 assumes that $s , \mu ,$ and ?? are all not large simultaneously. This assumption allowed us to focus only on the third case of Equation (3) and ignore the other two. The first case in which no aware user engages with the platform can never be an equilibrium outcome, but the second case where $1 > \mu D + \nu w \geq 1$ is certainly possible. How would our analysis change if we do not ignore this case? The purpose of this appendix is to examine that situation carefully.

First, we consider the validity of the original analysis done with the assumption that $\mu D + \nu w < 1 - s$ . Substituting ?? from (6) and simplifying, we get the validity condition as $\begin{array} { r } { s < \frac { 1 2 \left( 1 - w \nu \right) } { 1 2 + \mu \left( 3 + 2 z \right) } } \end{array}$ . Based the optimal values of ?? and ?? for the four different outcomes, we find the following:

• The outcome $( z , w ) = ( \rho , 0 )$ is valid if $\begin{array} { r } { s < \frac { 1 2 } { 1 2 + \mu ( 3 + 2 \rho ) } . } \end{array}$

The outcome $( z , w ) = ( 0 , 1 )$ is valid if $\begin{array} { r } { s < \frac { 4 ( 1 - \nu ) } { 4 + \mu } . } \end{array}$

• The outcome $( z , w ) = ( 0 , 0 )$ is valid if $\begin{array} { r } { s < \frac { 4 } { 4 + \mu } . } \end{array}$

• The outcome $( z , w ) = ( 0 , w ^ { * } )$ is valid if $\begin{array} { r } { \kappa < 2 + m + \frac { m \left( 2 - s \left( 5 + 2 \mu \right) \right) } { 6 \nu } . } \end{array}$

Let us next consider the second case where $1 > \mu D + \nu w \geq 1 - s$ . According to Equation (3), for a random user $\langle x , y \rangle$ , the total probability of engaging with narratives A and B would now become:

$$
P _ {a} (x) = \lambda (1 - x) p _ {a} (x) (1 - \mu D - \nu w) + (1 - \lambda) (1 - x) \left(p _ {a} (x) + (1 - p (x)) (1 - s)\right), \mathrm{and}
$$

$$
P _ {b} (x) = \lambda x p _ {b} (x) (1 - \mu D - \nu w) + (1 - \lambda) x \Big (p _ {b} (x) + \big (1 - p (x) \big) (1 - s) \Big).
$$

As before, we normalize ?? to 1. Now, integrating the above probabilities (of engaging) over ?? and applying the extra margin of ?? to A, we get:

$$
\begin{array}{l} \pi = (1 + m) \left(\underbrace {\int_ {0} ^ {1} P _ {a} (x) d x} _ {\text {Visits to A}}\right) + \left(\underbrace {\int_ {0} ^ {1} P _ {b} (x) d x} _ {\text {Visits to B}}\right) \\ \qquad = \left(1 + \frac {m}{2}\right) \left(\frac {2 - s}{2} + \frac {s z}{8} - \mu D - \nu w\right) + \left(\frac {m w (1 - \mu D - \nu w)}{4}\right) - \frac {(4 - z) (2 + m) (1 - s - \mu D - \nu w)}{1 6}. \end{array}
$$

Also, the overall polarization can be represented as:

$$
\begin{array}{c} D = \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} P _ {a} (x)   d x} _ {\text {A - type visits A}} + \underbrace {\int_ {\frac {1}{2}} ^ {1} P _ {b} (x)   d x} _ {\text {B - type visits B}}\right) - \left(\underbrace {\int_ {0} ^ {\frac {1}{2}} P _ {b} (x) d x} _ {\text {A - type visits B}} + \underbrace {\int_ {\frac {1}{2}} ^ {1} P _ {a} (x)   d x} _ {\text {B - type visits A}}\right) \\ = \frac {2 - s}{4} + \frac {z (2 + 3 s)}{3 0} - \frac {(1 5 + 2 z) (\mu D + \nu w)}{3 0} - \frac {(5 - 2 z) (1 - s - \mu D - \nu w)}{2 0}. \end{array}
$$

When expectations are fulfilled, we get: $\begin{array} { r } { D = \frac { ( 2 z + 3 ) ( 1 - \nu w ) } { 1 2 + \mu ( 2 z + 3 ) } } \end{array}$ . Facing a tax rate of ??, the platform now chooses $( z , w )$ to maximize $\pi - \kappa D$ . The analysis remains similar to the original one in the paper. Similar to that case, here as well, four outcomes are possible: $( \rho , 0 )$ , (0,1), (0,0), and $( 0 , w ^ { * } )$ , although the expression for $w ^ { * }$ now changes to $\begin{array} { r } { w ^ { \ast } = \frac { 1 } { 2 \nu } - \frac { 2 + m - \kappa } { 2 m } . } \end{array}$ This $w ^ { * }$ is valid if it is between 0 and 1, implying that $\begin{array} { r } { 2 + m - \frac { m } { \nu } < \kappa < 2 + 3 m - \frac { m } { \nu } } \end{array}$ must hold for the interior solution to occur.

We superimpose this new analysis on top of the original one in Figure 6 to obtain a more comprehensive picture in Figure B1. Comparing the two figures, we see that our results continue to hold qualitatively, even for large ??. The only notable change for large ?? is that the red and cyan regions expand a bit and the blue one shrinks. The green region may shrink, expand, or not change at all.

![](/api/attachments/KGUU7NJ7/fulltext/images/d4f36dfd253cc0883704895630d2369ae6a5a87029a6ac7c87ea0b81b0e837ca.jpg)  
(a) m = 1, µ = 0.5, ν = 0.2

![](/api/attachments/KGUU7NJ7/fulltext/images/3f1f53d77127c2e05fbe693b052dc9fb57f0bafda511c177202f62e5b90e22f5.jpg)  
(b) m = 1, µ = 0.5, ν = 0.3

![](/api/attachments/KGUU7NJ7/fulltext/images/24f3cb84010ac902e390e559747e4a840b48c15b258a5ea709178bf5797ba548.jpg)  
(c) m = 0.5, µ = 0.2, ν = 0.2

![](/api/attachments/KGUU7NJ7/fulltext/images/0ca388f9ef3899e7f89531e143473d41aecfc0e09df57946f8606860dac01edd.jpg)  
(d) m = 0.25, µ = 0.75, ν = 0.3  
Figure B1. Extended Analysis of Policymaker’s Intervention with Aware Users

## About the Authors

Debabrata Dey is the Ronald G. Harper Professor artificial intelligence and information systems at the KU School of Business, University of Kansas. He received his PhD from the Simon School of Business, University of Rochester. His research has appeared in Management Science, Operations Research, Information Systems Research, MIS Quarterly, Journal of Management Information Systems, and INFORMS Journal on Computing, among several other journals. Currently, he serves as an associate editor for Information Systems Research. In the past, he has served as a senior editor for Information Systems Research and as an associate editor for Management Science. He is a distinguished fellow of the INFORMS Information Systems Society and a senior member of INFORMS.

Atanu Lahiri is an associate professor at the Jindal School of Management, University of Texas at Dallas. He received his PhD from the Simon Business School, University of Rochester. His research interests are at the intersection of information systems and economics. His work has appeared in journals such as Information Systems Research, Journal of Management Information Systems, Management Science, MIS Quarterly, and INFORMS Journal on Computing. Currently, he serves as an associate editor for Information Systems Research and the Journal of the Association for Information Systems.

Rajiv Mukherjee is an assistant professor at the Mays Business School, Texas A&M University. He received his PhD from the McCombs School of Business, University of Texas, Austin. His research interests are at the intersection of information systems and economics. His work has appeared in journals such as Management Science and MIS Quarterly.

Copyright © 2025 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
