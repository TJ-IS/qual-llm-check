---
otero_id: 4658
otero_key: "MQ8KCSX7"
title: "An Economic Analysis of Peer Disclosure in Online Social Communities"
authors: "Zike Cao; Kai-Lung Hui; Hong Xu"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0744"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/MQ8KCSX7/fulltext/images/5f1a7eabb4a98b296dc049b666a678a340e747eec54ee8313f06ea6632636c24.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# An Economic Analysis of Peer Disclosure in Online Social Communities

Zike Cao, Kai-Lung Hui, Hong Xu

To cite this article: Zike Cao, Kai-Lung Hui, Hong Xu (2018) An Economic Analysis of Peer Disclosure in Online Social Communities. Information Systems Research

Published online in Articles in Advance 20 Jul 2018

https://doi.org/10.1287/isre.2017.0744

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Economic Analysis of Peer Disclosure in Online Social Communities

Zike Cao,<sup>a</sup> Kai-Lung Hui,<sup>b</sup> Hong Xu<sup>b</sup>

<sup>a</sup> Department of Technology and Operations Management, Rotterdam School of Management, Erasmus University, 3062 PA Rotterdam Netherlands; <sup>b</sup> Department of Information Systems, Business Statistics and Operations Management, School of Business and Management, Hong Kong University of Science and Technology, Kowloon, Hong Kong

Contact: cao@rsm.nl, http://orcid.org/0000-0002-5378-4772 (ZC); klhui@ust.hk, http://orcid.org/0000-0002-7074-1176 (K-LH); hxu@ust.hk, http://orcid.org/0000-0001-8561-0163 (HX)

Received: June 19, 2016 Revised: June 6, 2017 Accepted: July 7, 2017 Published Online in Articles in Advance: July 20, 2018

https://doi.org/10.1287/isre.2017.0744

Copyright: © 2018 INFORMS

Abstract. We study a novel privacy concern, i.e., peer disclosure of sensitive personal information in online social communities. We model peer disclosure as the imposition of a negative externality on other people. Our model encompasses the benefits of posting information, positive externalities in the form of recognition and entertainment benefits due to others’ sharing of information, and heterogeneous privacy preferences. We find that regulation of peer disclosure is necessary. We consider two candidate regulations, i.e., nudging and quotas. Nudging reduces user participation and privacy harm and sometimes improves social welfare. By contrast, imposing a quota often improves user participation, privacy protection, and social welfare. Adding a nudge on top of a quota does not bring additional benefits. We show that any regulation that uniformly controls the disclosure of sensitive and nonsensitive information will not serve the triple objectives of reducing privacy harm, increasing social welfare, and increasing information contribution. We derive a necessary condition for solutions that can fulfill these three objectives. We also compare the incentives of the platform owner and social planner and draw related managerial and policy implications.

History: Vĳay Mookerjee, Senior Editor; Subodha Kumar, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0744.

Keywords: peer disclosure • privacy • regulation • online social communities • nudging • quota

## 1. Introduction

User-generated content is ubiquitous on social-networking websites such as Facebook and YouTube. Such content sometimes contains information (i.e., any text, voice recording, image, and video) about other people (peers), which can bring unintended fame or consequences. For example, a high school teacher was fired in 2013 after her student posted a photo to Instagram of her providing alcohol and condoms in a prom after-party (Ortiz 2013). A 15-year-old boy in Québec was abused after a video of him playing a character in Star Wars went viral on the Internet. The boy made the video for a school project, but the video was shared by his friends on the Internet without his consent (Harmon 2003). Many children today are upset because their parents share their personal pictures or videos online (Dell’Antonia 2016). Generally, a person may inflict privacy harm on other people by disclosing their personal information to the public (DiMicco and Millen 2007, Tufekci 2008, Henne and Smith 2013, Choi et al. 2015).

From a social-welfare point of view, the privacy harm from peer disclosure should be balanced against the disclosure benefits. People enjoy social interaction and sharing interesting moments with friends. Friendly disclosure such as birthday greetings or achievement recognitions can bring joy to a social community. Practically, it is dificult for a social community to avoid mentioning related people in its conversations or exchanges. Hence, the pressing issue is to help users interact efectively without excessively infringing other peoples’ privacy in online social communities.

The current privacy practice in online social communities mainly targets users’ voluntary disclosure of their own information. For instance, Facebook ofers users an option to restrict access to their information, including posts, profiles, and photos by other users. Users can also select whose information to view in their own timelines and remove tags about themselves from related posts and photos.<sup>1</sup> However, these controls do not address peer disclosure, where a user’s privacy is infringed by friends’ posts. Therefore, we face a novel challenge: How does the privacy externality arising from peer disclosure of personal information afect the development of online social communities? Should we impose new policies to reduce the harm due to peer disclosure? If so, how should we design the policies? Would community owners prefer such regulation?

To address these questions, we develop a stylized model that captures users’ strategic decisions when they share information in an online social community. In our model, a fraction of users always participate in the community due to psychological commitment, membership, or other altruistic motivations (Hosanagar et al. 2010, Bateman et al. 2011). The other users are not committed and will strategically decide whether to join the community, taking into account the expected benefits from posting information, positive externalities from viewing posts containing others’ personal information, and privacy harm resulting from the disclosure of their personal information by other people. An uncommitted user would join the community if and only if she receives a higher utility from participating than by staying out. The users difer in their privacy sensitivity.

With this model, we characterize the impacts of peer disclosure, i.e., how it afects users’ decisions to join the community and post information about other people. In particular, we seek economic policies that motivate users to internalize the privacy harm caused by their posts. Two broad solutions prevail in the literature of negative externalities, i.e., indirect and direct control. Indirect control, dating back to Pigou (1920), uses an appropriate pricing scheme that charges agents for the externalities that they impose on others. Such externality pricing has been shown to be efective in areas such as environmental protection and trafic control (Cropper and Oates 1992). A common implementation of externality pricing is to impose a tax, where the tax rate is set such that the agents would choose the eficient levels of externalities (Vickrey 1963; Sandholm 2002, 2005). In online social communities, we propose “nudging” as an alternative form of externality pricing. A nudge is a soft paternalistic measure that operates as a cue to remind users of the potential privacy damage that their posts could bring to others, or as an extra time delay in the form of a “cooling-of” period for users to consider withdrawing their posts. The purpose is to “nudge” users to think carefully about the privacy consequences of their posts (Acquisti 2009, Wang et al. 2013, Almuhimedi et al. 2015). A nudge and a Pigouvian tax have essentially similar efects, where the “tax” is nonmonetary but exhibited in the form of additional time or efort in posting each piece of information.<sup>2</sup>

To directly control negative externalities, the classical approach is to use command-and-control regulations that directly restrict agents’ actions (Fullerton and Metcalf 2001). A typical implementation is to impose a quota or provide an allowance to each agent with the objective that the agent will generate the eficient level of externalities (Copes 1986, Calthrop and Proost 1998). Imposing a quota in online social communities is straightforward. We simply need to set a limit on the number or length of posts allowed for each user within a given time period.

The nudging and quota policies, corresponding to externality pricing and command-and-control regulation of negative externalities, are aligned with the practices adopted in many industries, including cigarette and alcohol taxes, pollution permits, and roadspace rationing. Besides externality pricing and command-and-control regulation, the prior literature has advanced other solutions to address negative externalities, including subsidies for abatement, marketable permits, and deposit-refund systems (Stavins 2011). These solutions, however, may not be applicable in online social communities, which mostly feature large numbers of users, making the exchange of user permits practically infeasible. It is also dificult to provide subsidies or request deposits as most online social communities charge no fees to users. Another approach to address the peer disclosure externality is to deploy new technologies. For instance, using text and image processing and advanced data analytics, online social community owners may attempt to distinguish sensitive from nonsensitive personal information and directly regulate a user’s disclosure of sensitive information about other people. We analyze these technical solutions in Section 4.

We find several unique results on nudging and quotas. A nudge decreases user participation and information contributions, but it also reduces the total privacy harm and sometimes increases social welfare by driving some users out of the community. By contrast, a quota preserves users’ incentive to join the community and always increases social welfare, but it cannot encourage information contribution. These findings exemplify the conflicting goals of enhancing social welfare and privacy protection vis-à-vis promoting community development in terms of increasing participation and information contribution. Our model provides a novel theoretical framework for analyzing the optimal policy designs in regulating online information contribution and peer disclosure.

We also find that quotas dominate nudging in increasing user participation and social welfare. Contrary to the prior literature, which suggests that a composite measure is more efective in addressing externalities (Roberts and Spence 1976, Christiansen and Smith 2012), we find that nudging users on top of a quota does not bring additional benefits. Furthermore, although the social planner and community owner may variously benefit from imposing a quota, they mostly prefer different quotas because of misaligned objectives. They may prefer the same quota only when the community owner wants to grow the number of participating users. If it wants to maximize information contribution by participating users, then it will never prefer a nudge or a quota. Following this result, we derive a general necessary condition for any economic policy to reduce privacy harm and increase social welfare while increasing overall information contribution.

Our contributions are threefold. First, we show that regulation is necessary when users can freely post information about other people in an online social community. To our knowledge, this is the first analysis to address the privacy harm caused by peer disclosure on the Internet. Second, we illustrate the nuanced impacts of imposing a nudge and a quota, particularly their implications on user participation, which (to our knowledge) has not been formally analyzed in prior studies (Schulze and d’Arge 1974, Weitzman 1974, Collinge and Oates 1982). Third, we uncover a novel dilemma: Welfare maximization and privacy protection are not aligned with community development. We suggest some directions to resolve this dilemma, such as tailoring the nudge and quota for privacy-infringing posts or enabling users to prune sensitive information related to themselves.

The rest of this paper is organized as follows. Section 2 reviews the related literature. Section 3 presents the model and analyzes the impacts of imposing a nudge and a quota. Section 4 derives a necessary condition for solutions that reduce privacy harm without sacrificing information contribution. Section 5 illustrates the ideas in this paper using a numerical example. Section 6 analyzes three extensions to our main model. Section 7 discusses the implications of this research. Section 8 concludes the paper.

## 2. Related Literature

This study is closely related to the emerging stream of research studying how peer disclosure afects consumers and possible remedial actions. Choi et al. (2015) study how embarrassing posts by friends in online social networks afect individuals’ perceptions of social relationships and their subsequent behavioral responses. Several studies have proposed measures to help consumers remove information shared by others without their consent (Besmer and Lipford 2010, Henne and Smith 2013). In general, the solutions involve identifying the shared information (e.g., by facial recognition technologies) and helping afected users negotiate with the parties posting the information (e.g., by requesting removal of infringing photos). Such solutions apply ex post, after the information has been posted. Hence, they are inadequate because the damage is inflicted once the information is available to the public. An ideal solution should apply ex ante: It should encourage people to not haphazardly post information about others. This is the focus here.

A large body of research has studied voluntary disclosure of personal information (see, e.g., Gross and Acquisti 2005, Dwyer et al. 2007, Acquisti and Gross 2009) and its regulation (Hermalin and Katz 2006, Hui and Png 2006). This literature has variously advocated the use of “privacy nudges” (Acquisti 2009, Wang et al. 2013, Almuhimedi et al. 2015), which can be visual cues about the potential audience of a post, a time delay before the post is published or feedback on the potential sentiment and sensitivity of the post. The essential idea is to nudge users so that they will think twice about the privacy consequences of their posts. The focus of this literature lies in protecting consumer privacy in an online environment and the economic eficiency of information disclosure. To our knowledge, it does not address the externalities due to information disclosure.

Prior research on privacy externalities focus mostly on marketing activities (Anderson and de Palma 2009, Anderson and Gans 2011, Johnson 2013). Seller marketing imposes a direct externality on consumers by congesting consumers’ attention span to process marketing promotions or increasing their costs of reading or processing the marketing. This literature has proposed solutions to help consumers address the externality. For example, Van Zandt (2004) shows that increasing senders’ transmission costs using a tax or technical measures can help increase the welfare of receivers (consumers) and benefit all senders. By considering consumers’ privacy harm due to seller solicitations, Hann et al. (2008) find that it is optimal to impose a charge on seller solicitations. Motivated by these suggestions, we analyze nudging as one candidate economic policy to regulate third-party externalities from peer disclosure (cf. second-party externalities from sellers).

More broadly, the economics literature has extensively analyzed the impacts of imposing a Pigouvian tax and a limit on the externality-generating activities in various contexts featuring production or consumption externalities, such as air and water pollution, smoking, and alcohol consumption (Weitzman 1974, Baumol and Oates 1988, Cropper and Oates 1992, Pizer 2002). An important consideration in this literature is entry and exit. A tax penalizes a firm and hence may force the firm to leave the industry in the long run, which can contract the industry and dampen social welfare (Schulze and d’Arge 1974, Collinge and Oates 1982, Cropper and Oates 1992). In our setting, the privacy nudge resembles a Pigouvian tax. Hence, it is important to endogenize users’ participation decisions in studying the regulation of peer disclosure in online social communities.

By contrast, limiting the externality-generating activities may have a smaller impact on participation. We consider the use of a quota as an alternative economic policy to cap or limit externalities due to peer disclosure. Prior research has also shown that one single policy, such as imposing a tax alone, may not differentiate activities that generate diferent degrees of externalities. Hence, adding a direct control of the externality-generating activities may further enhance social welfare (Roberts and Spence 1976, Bennear and Stavins 2007, Christiansen and Smith 2012). For example, to address the externality due to smoking, we can apply a cigarette tax and concurrently restrict the number of outlets or limit the opening hours of outlets that sell cigarettes. We adopt a similar idea and analyze the merit of combining a nudge and a quota in this paper.

Finally, our work is related to studies of negative network externalities (Liebowitz and Margolis 1994), such as the congestion externality due to free-riding in peer-to-peer (P2P) file-sharing networks (Asvanund et al. 2004). The peer disclosure externality difers from congestion externalities in that it is directly imposed at the individual-user level instead of the community level. Hence, we must account for the size of the user community in analyzing its impact and regulation.

## 3. The Model

Consider a unit mass of users who can participate and post information in an online social community. A fraction, $1 - \alpha \ ( 0 < \alpha < 1 )$ , of these users are committed and always participate in the community. The other α users are uncommitted and will participate if and only if they receive a higher utility from participation than from staying out.<sup>3</sup> Among all committed and uncommitted users, $\beta , 0 < \beta < 1$ , have high privacy sensitivity (high types) and $1 - \beta$ have low privacy sensitivity (low types).

Each user is connected to some peers in the social community. A connection can be interpreted as a friendship link. We refer to a user’s connected peers as friends and unconnected peers as nonfriends. As is the case with popular social networking websites such as Facebook or LinkedIn, the connections are undirected, $\mathrm { i . e . , }$ two users accept each other as a friend once a connection is established. Each user, $i ,$ has a probability of $n _ { i } \in [ 0 , 1 ]$ of establishing a connection with any other user. Note that $n _ { i }$ can also be interpreted as the number of friends of user i because we normalize the total mass of users to 1. We use $N _ { i }$ to denote the set of user $i \prime \mathrm { s }$ friends and $\bar { N } _ { i }$ as the set of user $i \prime \mathrm { s }$ nonfriends. For a large population of users, $n _ { i }$ is very small. This is consistent with the case of Facebook, which has more than 700 million users but more than 95% of them have fewer than $1 { , } 0 0 0$ friends (Backstrom 2011). We start with a simple setup where every user has the same number of friends: $n _ { i } = n$ for all i. We relax this assumption in Section 6.

We assume the user types are evenly distributed in each user’s friend and nonfriend networks. Hence, for any user $i , N _ { i }$ and $\bar { N } _ { i }$ contain a proportion α of uncommitted users and a proportion $\beta$ of high-type users. Figure 1 depicts the composition of the population and the connection of user i in a network with 18 users, where $\alpha = 1 / 2 , \beta = 1 / 3 ,$ , and $n _ { i } = 1 / 3$

Each participating user can post sensitive and nonsensitive information about other people. Let $x _ { i t }$ and $y _ { i t }$ be the amount of nonsensitive and sensitive information that user i posts about user $t , \ i \neq t .$ . The posting of sensitive information imposes a negative externality (privacy harm) on user t. Evidently, each piece of sensitive information could cause diferent degrees of privacy harm, which will likely follow some statistical distribution. Without loss of generality, we use $\rho _ { H } \left( \rho _ { L } \right)$ to denote the expected privacy harm that a high- (low-) type user sufers from the release of each piece of sensitive information about her. We assume a participating user can post information about any other users, including nonfriends and nonparticipating users. In practice, Facebook users can share posts or photos about anyone, including celebrities who do not have a Facebook account.

Figure 1. (Color online) An Example of User Population and Connection  
![](/api/attachments/MQ8KCSX7/fulltext/images/2bf53b2dce7c49c35057edd7dcbfcf08a41289f5e802d1438c2efdba6063db15.jpg)  
Note. Total population <sup></sup> 18, α <sup></sup> 1<sup>/</sup>2, β <sup></sup> 1<sup>/</sup>3, and n<sub>i</sub> <sup></sup> 1<sup>/</sup>3.

A user receives a unit benefit, v, from posting each piece of information about other people. The benefit can come from the gratification of being perceived as knowledgeable, or tangible gains from advertising if the information attracts high viewership (e.g., garnering a large number of “likes” on Facebook). The cost for posting a piece of information, including the time and efort to acquire, edit, and upload it, varies by the type of information and connection. We use $C _ { x } ( \overline { { x } } _ { i j } ) =$ $\begin{array} { r } { \dot { \frac { 1 } { 2 } } \dot { c _ { x } } x _ { i j } ^ { 2 } , C _ { y } ( y _ { i j } ) = \frac { 1 } { 2 } c _ { y } y _ { i j } ^ { 2 } , \frac { 1 } { \delta } C _ { x } ( x _ { i k } ) } \end{array}$ , and $\textstyle { \frac { 1 } { \delta } } C _ { y } ( y _ { i k } )$ to denote the cost functions for posting nonsensitive and sensitive information about friends, $j \in N _ { i } ,$ and nonfriends, $k \in { \bar { N } _ { i } } . ^ { 4 }$ We use $j$ to index friends and k to index nonfriends. The convex cost functions capture the increasing dificulty of collecting and posting information as the posting volume increases.

We assume that it is more costly to post sensitive information than nonsensitive information, i.e., $c _ { x } = c$ and $c _ { y } = c / \psi , c > 0$ and $0 < \psi < 1$ . Intuitively, people guard their sensitive information such as medical history or salary more carefully. People may also feel more uncomfortable in divulging embarrassing posts about others when their own identities are observable in the community. We assume that it is more dificult to post information about nonfriends than friends, $\mathrm { i . e . , } 0 < \delta \ll 1$ , because of increased social distance and decreased level of trust toward nonfriends. Realistically, people post more about their online friends who are likely to be friends, relatives, classmates or colleagues in their ofline social circles (DiMicco and Millen 2007).

Besides the direct benefit from posting, a participating user also benefits from information posted by others. We use e to denote the entertainment benefit that a user enjoys from reading a piece of information unrelated to her posted by others $( \mathrm { e . g . } ,$ , many people enjoy gossip about celebrities shared by others on Facebook). Similarly, we use w to denote the recognition benefit that a user enjoys when a piece of her nonsensitive information is posted by others (e.g., a person may experience pride when other people share the news that she has won an award).

Let s be the set of participating users. User i’s expected utility from participation is

$$
\begin{array}{l} u _ {i \mid s} ^ {i n} = \int_ {j \in N _ {i}} \left[ v (x _ {i j} + y _ {i j}) - C _ {x} (x _ {i j}) - C _ {y} (y _ {i j}) \right] d j \\ \quad + \int_ {k \in \bar {N} _ {i}} \left[ v (x _ {i k} + y _ {i k}) - \frac {1}{\delta} C _ {x} (x _ {i k}) - \frac {1}{\delta} C _ {y} (y _ {i k}) \right] d k \\ \quad + e \int_ {m \in s, m \neq i} \left[ \int_ {t \neq i} (x _ {m t} + y _ {m t}) d t \right] d m \\ \quad + w \int_ {m \in s, m \neq i} x _ {m i} d m - \rho_ {i} \int_ {m \in s, m \neq i} y _ {m i} d m. \end{array} \tag {1}\tag{1}
$$

The first two integrals are user $i \prime \mathrm { s }$ expected benefits from posting about her friends and nonfriends. The remaining three terms capture the externalities inflicted by other users. Specifically, the third term is the entertainment benefit, the fourth term is the recognition benefit, and the last term is the privacy harm.

Let $X _ { \cdot i } , Y _ { \cdot i } ,$ and $Q _ { - i }$ be, respectively, the total quantity of nonsensitive information related to user $\bar { i } ,$ the total quantity of sensitive information related to user $i ,$ and the total quantity of information posted by all participating users except user $i , ^ { 5 }$ with

$$
\begin{array}{l} X _ {\cdot i} \equiv \int_ {m \in s, m \neq i} x _ {m i} d m, \\ Y _ {\cdot i} \equiv \int_ {m \in s, m \neq i} y _ {m i} d m, \\ Q _ {- i} \equiv \int_ {m \in s, m \neq i} \left[ \int_ {t} (x _ {m t} + y _ {m t}) d t \right] d m. \end{array}
$$

With these notations, $\begin{array} { r } { \int _ { m \in s , m \neq i } \left[ \int _ { t \neq i } \left( x _ { m t } + y _ { m t } \right) d t \right] d m \equiv } \end{array}$ $Q _ { - i } - X _ { \cdot i } - Y _ { \cdot i } ,$ Equation (1) can be rearranged as

$$
\begin{array}{r l} & u _ {i | s} ^ {i n} = n _ {i} \Bigg [ v x _ {i j} - \frac {c x _ {i j} ^ {2}}{2} + v y _ {i j} - \frac {c y _ {i j} ^ {2}}{2 \psi} \Bigg ] \\ & \qquad + (1 - n _ {i}) \Bigg [ v x _ {i k} - \frac {c x _ {i k} ^ {2}}{2 \delta} + v y _ {i k} - \frac {c y _ {i k} ^ {2}}{2 \delta \psi} \Bigg ] \\ & \qquad + e Q _ {- i} + \omega X _ {\cdot i} - \theta_ {i} Y _ {\cdot i}, \end{array}\tag{2}
$$

where $\omega = w - e$ and $\theta _ { i } = \rho _ { i } + e$ represent the recognition benefit and privacy harm net of the entertainment value for each piece of information. Without loss of generality, we assume $\omega > 0 , \theta _ { H } = 1$ , and $0 < \theta _ { L } < 1$ . We refer to $e Q _ { - i } + \omega X _ { . i }$ as the “positive externalities” that user i receives from all information posted by other users, and $\theta _ { i } Y _ { . i }$ as the privacy harm that user i sufers from information posted about her by other users.

Note that participating users can post information about nonparticipating users. We assume that a nonparticipating user is afected by the externalities caused by the information shared in the community. Realistically, people may get exposed to information that goes viral in other media, and celebrities can be defamed by information posted in an online community even if they are not members of the community. In our model, conditional on $s ,$ user $i \prime \mathrm { s }$ utility from staying out

$$
u _ {i \mid s} ^ {o u t} = \epsilon (e Q _ {- i} + \omega X _ {\cdot i} - \theta_ {i} Y _ {\cdot i}),\tag{3}
$$

where $\epsilon \in ( 0 , 1 )$ captures how easy it is for an outsider to be exposed to (or become aware of) information posted within the community. The larger  is, the easier the information posted in the community spreads outside the community. We can interpret 1 <sup>−</sup>  as the diference between the objective and subjective (perceived) information externalities, including privacy harm, faced by

## Table 1. Notations

$\alpha$ The fraction of uncommitted users $\beta$ The fraction of users with high privacy sensitivity $n _ { i }$ The fraction of population connected with user $i ,$ with $n _ { i } = n$ in the main model $v$ Benefit from posting each unit of information c Cost coeficient of posting nonsensitive information $\psi$ Cost ratio between posting sensitive and nonsensitive information $\delta$ Cost ratio between posting information about friends and nonfriends $\gamma$ Weighted cost ratio between posting about friends and nonfriends, $\mathbf { \nabla } \cdot \boldsymbol { \gamma } = n + ( 1 - n ) \delta$ e Entertainment benefit from each unit of information posted by others w Recognition benefit from each unit of nonsensitive information posted by others ω Net recognition benefit from each unit of nonsensitive information posted by others, $\omega = w - e$ $\rho _ { i }$ User i’s privacy harm from each unit of sensitive information posted by others, $i \in \{ L , H \}$ $\theta _ { i }$ User i’s net privacy harm from each unit of sensitive information posted by others, $i \in \{ L , H \} , \theta _ { i } = \rho _ { i } + e$ $\epsilon$ The degree of information posted within the community being exposed to outsiders $\lambda _ { i }$ User i’s average net privacy harm from each unit of information posted in the community, $i \in \{ L , H \}$ $\tau$ Unit cost due to nudging $\Lambda$ Posting limit or quota

a nonparticipating user i due to the information posted in the community. Hereafter, we refer to measures scaled by  as perceived measures and those unscaled as objective measures. For example, $\theta _ { i } Y _ { \cdot i }$ is objective privacy harm whereas $\epsilon \theta _ { i } Y _ { . i }$ is perceived privacy harm. Table 1 summarizes the key notations.

We study a three-stage game as shown in Figure 2. Stage 1 defines the environment, particularly whether the posting of information is regulated. In Stage 2, uncommitted users decide whether to join the community. In Stage 3, participating users decide how much information to post.

## 3.1. The Status Quo

We first consider a baseline setting where users can freely make participation and posting decisions without accounting for the privacy harm they inflict on others. We use backward induction to derive the subgame perfect equilibrium. Conditional on joining the community, user i’s posting decisions, $x _ { i j } , x _ { i k } , y _ { i j } ,$ and $y _ { i k }$ can be obtained from the first-order conditions of Equation (2)

$$
x _ {i j} ^ {s q} = \frac {v}{c}, y _ {i j} ^ {s q} = \frac {\psi v}{c}, x _ {i k} ^ {s q} = \frac {\delta v}{c}, y _ {i k} ^ {s q} = \frac {\delta \psi v}{c}.\tag{4}
$$

A user would simply post information based on the ratios of posting benefits over posting costs when she omits the privacy harm that she causes. Her own privacy sensitivity will not afect her posting decisions.

However, user i’s participation decision depends not only on her own posting but also on the quantity of information others post about her. We consider a rational-expectations equilibrium in which users can anticipate other users’ posting decisions. Substituting (4) into (2), user i’s conditional utility from participation is

Figure 2. Timing of the Model  
![](/api/attachments/MQ8KCSX7/fulltext/images/7612c58d8d34c10c24e9e0d9460111ae0460299c55b995935f7a72bf3e6ea3fa.jpg)

$$
u _ {i | s} ^ {s q, i n} = \frac {\gamma (1 + \psi) v ^ {2}}{2 c} - \frac {\gamma (1 + \psi) v s \lambda_ {i}}{c}, \quad i \in \{L, H \},\tag{5}
$$

where $s \in [ 1 - \alpha , 1 ]$ because committed users always participate in the community. For brevity, we let $\gamma \equiv$ $n + ( 1 - n ) \delta$ (the weighted cost ratio of posting information about friends and nonfriends) and $\lambda _ { i } \equiv  \dot  ( \psi \theta _ { i } - \lambda \mathrm { ~ }$ $e ( 1 + \psi ) - \omega ) / ( 1 + \psi ) , i \in \{ L , H \}$

The first term in (5), $( \gamma ( 1 + \psi ) v ^ { 2 } ) / ( 2 c )$ , is user $i \prime \mathrm { s }$ total benefit from posting. The second term, $( \gamma ( 1 + \psi )$ vs $\lambda _ { i } ) / c _ { . }$ , is the net privacy harm (i.e., privacy harm net of entertainment and recognition benefits) that user i sufers from participating in the community. In the second term, $( \bar { \gamma ( 1 + \psi ) v ) } / c \overset { \smile } { = } n ( x _ { i j } ^ { s q } + y _ { i j } ^ { s q } ) + ( 1 - \bar { n } ) ( x _ { i k } ^ { s q } + y _ { i k } ^ { s q } )$ is the amount of information posted by each participating user; thus $( \gamma ( 1 + \psi ) v s ) / c$ is the total quantity of information posted by the entire community. Therefore, we can interpret $\lambda _ { i }$ as user $i \prime \mathrm { s }$ average net privacy harm caused by each piece of information posted in the community.<sup>6</sup>

User i’s utility from staying out of the community follows Equation (3)

$$
u _ {i | s} ^ {s q, o u t} = - \epsilon \cdot \frac {\gamma (1 + \psi) v s \lambda_ {i}}{c}, i \in \{L, H \}.\tag{6}
$$

We impose the following regularity assumption.

Assumption 1. $\theta _ { L } > e ( 1 + 1 / \psi ) + \omega / \psi$

Note that $\theta _ { L } \leq e ( 1 + 1 / \psi ) + \omega / \psi$ is equivalent to $\lambda _ { L } \leq 0 ,$ which means that all low-type users will participate in the status quo because their net privacy harm is negative (i.e., they benefit from other peoples’ posting). Assumption 1 enables us to focus on a more realistic scenario where the privacy concern is suficiently salient to hinder some users from participating in the community.

Table 2. Equilibrium Participation Rates in the Status Quo

<table><tr><td> $v$ </td><td> $s_{L}^{sq}$ </td><td> $s_{H}^{sq}$ </td><td> $s^{sq}$ </td></tr><tr><td> $(0,2(1-\epsilon)(1-\alpha)\lambda_{L})$ </td><td>0</td><td>0</td><td> $1-\alpha$ </td></tr><tr><td> $[2(1-\epsilon)(1-\alpha)\lambda_{L},2(1-\epsilon)(1-\alpha\beta)\lambda_{L}]$ </td><td> $\frac{v/(2(1-\epsilon)\lambda_{L})-(1-\alpha)}{\alpha(1-\beta)}$ </td><td>0</td><td> $\frac{v}{2(1-\epsilon)\lambda_{L}}$ </td></tr><tr><td> $(2(1-\epsilon)(1-\alpha\beta)\lambda_{L},2(1-\epsilon)(1-\alpha\beta)\lambda_{H})$ </td><td>1</td><td>0</td><td> $1-\alpha\beta$ </td></tr><tr><td> $[2(1-\epsilon)(1-\alpha\beta)\lambda_{H},2(1-\epsilon)\lambda_{H}]$ </td><td>1</td><td> $\frac{v/(2(1-\epsilon)\lambda_{H})-(1-\alpha\beta)}{\alpha\beta}$ </td><td> $\frac{v}{2(1-\epsilon)\lambda_{H}}$ </td></tr><tr><td> $(2(1-\epsilon)\lambda_{H},+\infty)$ </td><td>1</td><td>1</td><td>1</td></tr></table>

Given s, user i will participate if and only if $u _ { i | s } ^ { s q , i n } \geq u _ { i | s } ^ { s q , o u t }$ . Let $s _ { L } \ ( s _ { H } )$ be the participation rate for uncommitted low- (high-) type users, and $\scriptstyle s ^ { s q } = ( 1 - \alpha ) \cdot$ + $\alpha ( 1 - \beta ) s _ { L } ^ { s q } + \alpha \beta s _ { H } ^ { s q } ,$ i.e., the sum of all committed and uncommitted low- and high-type participating users. The following results characterize users’ equilibrium participation as the posting benefit, v, varies.

Lemma 1. In the status quo equilibrium, uncommitted users will participate according to Table 2.

In the status quo, participating users ignore the privacy harm inflicted on others. When the posting benefit $v < 2 ( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } ,$ , low- and high-type uncommitted users prefer to stay out because the privacy harm outweighs the benefit from posting information.

Figure 3. Equilibrium Outcomes in the Status Quo  
![](/api/attachments/MQ8KCSX7/fulltext/images/440720a3527b47367923eb8f8129511240efa1bc5c2c4f5f3e2e2dcc952f40c0.jpg)

![](/api/attachments/MQ8KCSX7/fulltext/images/1ebdad9568248b599ee4be7dc97dccadf9deb304a95cdd32254d2fcfc2a0ce9a.jpg)

As v increases, the users will gradually participate by order of privacy sensitivity, and the participation rate increases with v. When v is suficiently large, all users participate in the community.

Let Π be the social welfare, defined as the aggregate surplus of all users including the perceived privacy harm sufered by all nonparticipating users, let Q be the total quantity of information posted in the community, and let ξ be the total objective privacy harm including the harms inflicted on non-participating users.<sup>7</sup> The next lemma characterizes the outcomes in the status quo. Figure 3 illustrates how the outcomes in Lemmas 1 and 2 vary with v.

Lemma 2. In the status quo, the total quantity of information posted, Q, and total privacy harm, ξ, increase with v.

![](/api/attachments/MQ8KCSX7/fulltext/images/07cfcf991d8b765a2f1eb3b4acc9a36923605b1a65281d17e14ba7fef046b17d.jpg)

![](/api/attachments/MQ8KCSX7/fulltext/images/8e2e253ab83189b716e6aa5a7fc953caaf6f056d936fd22fb2a49caebfb5a6c1.jpg)

Social welfare is negative if and only if (i) $0 < v < 2 [ \bar { \lambda } -$ $( 1 - \epsilon ) \alpha \dot { \beta } \lambda _ { H } ] ,$ , or (ii) $2 [ \bar { \lambda } ^ { " } - ( 1 - \epsilon ) \dot { \alpha } \dot { \beta } \lambda _ { H } ] < v < 2 \bar { \lambda }$ and $\beta > ( ( 1 - \epsilon ) \lambda _ { H } - \lambda _ { L } ) / ( \lambda _ { H } - \lambda _ { L } ) .$ , where $\begin{array} { r } { \bar { \lambda } = \beta \lambda _ { H } + ( 1 - \beta ) \lambda _ { L } . } \end{array}$

Social welfare can be negative for two reasons. Nonparticipating users carry negative utility since they are also (partially) afected by the privacy harm generated in the community. When the proportion of nonparticipating users increases as the posting benefit v decreases, the overall negative utility outweighs the positive utility from some of the participating users, therefore leading to negative social welfare. As posting benefit v increases, high-type users could still have a large negative utility even after they participate because the positive utility from posting is lower than the privacy harm imposed on them. This could also lead to negative social welfare when there are many such highly privacy-sensitive users, i.e., β is suficiently high.

One interesting observation in the status quo, as depicted in Figure 3, is that, when the social welfare is negative, a slight increase in v may further decrease social welfare. An increase in posting benefit v induces users to post more information and more uncommitted users to join the community and post information. Such additional information brings negative marginal benefit due to its privacy harm. The implication is that in some online social communities, having more users or encouraging users to post more information involving peers can be bad. Indeed, many people post unverified gossip on the Internet. Recent research has shown that online social communities or, more broadly, the Internet can help propagate materials that support racial hatred, political flaming, and cyberbullying (see, e.g., Davis 1999, Keith and Martin 2005, Kowalski and Limber 2007, Bhuller et al. 2013, Chan et al. 2016).

As a benchmark, we next derive the first-best posting decisions, in which we assume the users account for the externalities from their posting behavior. Without loss of generality, we let $\epsilon = 1$ and derive the first-best posting strategies as

$$
\begin{array}{l} x _ {i j} ^ {f b} = \frac {v + e + \omega}{c}, \qquad y _ {i j} ^ {f b} = \max \bigg \{0, \frac {\psi (v - \theta_ {j})}{c} \bigg \}, \\ x _ {i k} ^ {f b} = \frac {\delta (v + e + \omega)}{c}, \qquad y _ {i k} ^ {f b} = \max \bigg \{0, \frac {\delta \psi (v - \theta_ {k})}{c} \bigg \}. \end{array}\tag{7}
$$

A simple comparison of the above posting amount with those in the status quo, as shown in Equations (4), shows that users in the first-best case post more nonsensitive information and less sensitive information than in the status quo, and that the amount of sensitive information is contingent on the privacy sensitivity of the subjects being posted.

In the following subsections, we analyze a few policies and compare their impacts on users’ decisions.

We focus on two policies, nudge and quota, that are highly feasible because they uniformly apply to sensitive and nonsensitive information. We then extend the analysis to other policies, including targeted nudge (TN), targeted quota (TQ), and information pruning (IP), that diferentiate between the two types of information. These policies may become feasible with future advancements in technology. We also provide implications for each policy from the perspectives of the social planner and the community owner.

## 3.2. Nudge

We first study the use of a privacy nudge as a regulation policy (Acquisti 2009, Wang et al. 2013, Almuhimedi et al. 2015). The online social community can remind users of the potential privacy harm that their posts may cause for other people through, e.g., visual cues or warning messages. The community can also introduce an extra time delay before a post is really publicized to allow users a “cooling-of” period during which they can revoke the post. Such privacy nudges increase users’ mental eforts needed to post information and ofer a chance for them to reconsider their decisions. We model the privacy nudge as imposing an additional linear posting cost on users, $\tau \in \dot { [ 0 , v ] } . ^ { \vee }$ Intuitively, if the nudge exceeds users’ posting benefit, v, then users would obtain negative benefit from posting and hence no user would post any information.

Because the nudge applies to all users and information, it increases the overall cost of posting information in the online social community. As highly drastic as it may seem, mechanisms similar to a nondiscriminatory nudge are commonly proposed. For example, one renowned solution to combat music or movie piracy is to impose a tax on all blank storage media such as CD or DVD even though they are often used for legitimate purposes such as data storage. Bill Gates has famously suggested an email tax to curb spam, which inevitably afects all legitimate uses of email. We add the superscript n to all variables in the setting with a nudging policy.

With nudging, user i’s utility from participation becomes

$$
\begin{array}{l} u _ {i | s} ^ {n, i n} = n _ {i} \left[ v x _ {i j} - \frac {c x _ {i j} ^ {2}}{2} + v y _ {i j} - \frac {c y _ {i j} ^ {2}}{2 \psi} - \tau (x _ {i j} + y _ {i j}) \right] \\ \quad + (1 - n _ {i}) \left[ v x _ {i k} - \frac {c x _ {i k} ^ {2}}{2 \delta} + v y _ {i k} - \frac {c y _ {i k} ^ {2}}{2 \delta \psi} - \tau (x _ {i k} + y _ {i k}) \right] \\ \quad + e Q _ {- i} + \omega X _ {\cdot i} - \theta_ {i} Y _ {\cdot i}. \end{array} \tag {8}
$$

The first-order conditions of (8) give the following posting decisions:

$$
\begin{array}{l} {x _ {i j} ^ {n} = \frac {v - \tau}{c}, y _ {i j} ^ {n} = \frac {\psi (v - \tau)}{c},} \\ {x _ {i k} ^ {n} = \frac {\delta (v - \tau)}{c}, y _ {i k} ^ {n} = \frac {\psi \delta (v - \tau)}{c}.} \end{array}\tag{9}
$$

Table 3. Equilibrium Participation Rates with Nudge

<table><tr><td>v</td><td> $s_L^n$ </td><td> $s_H^n$ </td><td> $s^n$ </td></tr><tr><td>(0,2(1-ε)(1-α)λL+τ)</td><td>0</td><td>0</td><td>1-α</td></tr><tr><td>[2(1-ε)(1-α)λL+τ,2(1-ε)(1-αβ)λL+τ]</td><td>(v-τ)/(2(1-ε)λL)-(1-α)/α(1-β)</td><td>0</td><td>v-τ/2(1-ε)λL</td></tr><tr><td>(2(1-ε)(1-αβ)λL+τ,2(1-ε)(1-αβ)λH+τ)</td><td>1</td><td>0</td><td>1-αβ</td></tr><tr><td>[2(1-ε)(1-αβ)λH+τ,2(1-ε)λH+τ]</td><td>1</td><td>(v-τ)/(2(1-ε)λH)-(1-αβ)/αβ</td><td>v-τ/2(1-ε)λH</td></tr><tr><td>(2(1-ε)λH+τ,+∞)</td><td>1</td><td>1</td><td>1</td></tr></table>

Note. $s ^ { n } = ( 1 - \alpha ) + \alpha ( 1 - \beta ) s _ { L } ^ { n } + \alpha \beta s _ { H } ^ { n }$

Clearly, the nudge decreases the amount of information posted by participating users. However, it does not afect nonparticipating users. Hence, user i’s utility from staying out, $u _ { i \mid s } ^ { \star , o u t } .$ , takes the same form as Equation (3). Her participation decision then depends on the comparison between $u _ { i \mid s } ^ { n , i n }$ and $u _ { i \mid s } ^ { n , o u t }$ . The following lemma summarizes the equilibrium participation rates.

Lemma 3. When a nudge, $\tau \in ( 0 , v ] ,$ , is imposed, uncommitted users will participate according to Table 3.

By comparing Lemma 3 with Lemma 1, with nudging, a higher v is needed to encourage both types of users to participate and post information. Not surprisingly, the nudge also leads to less information posting. Hence, it efectively reduces the total privacy harm created by the community. The following proposition states these results formally.

Proposition 1. Compared to the status quo, a nudge reduces user participation, total quantity of information posted, and total privacy harm. Furthermore, the participation rates, total quantity of information posted, and total privacy harm decrease in the level of nudge, τ.

Intuitively, users may be annoyed by the privacy nudge (e.g., warning messages, time delay) and hence may post less information or even drop out from the community. Our result is consistent with previous research showing that many consumers are impatient and may drop out of online communities due to inconvenience (Galletta et al. 2006, Rajamma et al. 2009, Ding et al. 2015). Note that, although a nudge can efectively reduce the total privacy harm as it discourages peer disclosure, it also leads to less activity in the community and lower posting, entertainment, and recognition benefits. Its overall impact on the community is determined by the trade-ofs between these benefits and costs. The following result characterizes the case in which a nudge is socially preferred.

Proposition 2. (i) A nudge can improve social welfare when social welfare is negative in the status quo. In this case, the socially optimal nudge is $\tau ^ { * } = v ,$ which gives social welfare of 0.

(ii) A nudge always decreases social welfare when social welfare is positive in the status quo. In this case, the socially optimal nudge is $\tau ^ { * } = 0$

As discussed in Lemma 2, allowing users to post information is socially undesirable when the social welfare is negative. Imposing a nudge can dissuade people from posting and hence improve social welfare. The optimal outcome is to nudge all users extensively so that they do not post any information. Social welfare will then increase from being negative to 0. A harsher nudge could be viewed as a less userfriendly interface. The results here show that when privacy externalities dominate, an easier-to-use interface may actually hurt social welfare. By contrast, when social welfare is positive, allowing users to post information brings more benefits than harm. Imposing a nudge will only increase the cost to the community. Hence, the optimal nudge is $\tau ^ { * } = 0 .$

The implication of the nudging analysis is that, if a person is concerned about privacy, perhaps she should simply not join the community. Incidentally, this implication is consistent with the Chicago School’s view of how privacy should be treated, although here the privacy harm arising from peer disclosure is a form of negative externality that calls for regulation (Posner 1978, 1979, 1981; Stigler 1980).

Because a nudge always decreases user participation and posting of information, it is clearly not in the interest of the community owner to impose a nudge. However, a social planner such as the government cares more about social welfare and privacy. ${ \mathrm { S o } } ,$ the social planner prefers nudging for all v specified in Condition (i) of Proposition 2 because it helps achieve higher social welfare and lower total privacy harm. Such discrepancy in objectives helps explain why most online social communities today do not alert users about the potential adverse consequences of peer disclosure.

## 3.3. Quota

We next consider the merit of a quota, Λ, which is a limit on the total quantity of information that a user can post in the community. We assume $\Lambda \in ( 0 , ( \gamma \cdot$ $( 1 + \psi ) v ) / c ]$ . Recall from Equation (4) that a user would post $( \gamma ( 1 + \psi ) v ) / c$ units of information in the status quo. Hence, when $\Lambda { > } ( \gamma ( 1 + \psi ) v ) / c .$ , the quota is not binding. We refer to any $\Lambda { \in } ( 0 , ( \gamma ( 1 + \psi ) v ) / c ]$ as an efective quota as it will afect the user’s equilibrium behavior. We say that the quota is inefective otherwise.

We add the superscript q to all variables in the setting with a quota. Conditional on participation, the user’s posting decisions are now subject to an additional constraint

$$
n (x _ {i j} ^ {q} + y _ {i j} ^ {q}) + (1 - n) (x _ {i k} ^ {q} + y _ {i k} ^ {q}) \leq \Lambda .\tag{10}
$$

We compute $x _ { i j } ^ { q } , \ y _ { i j } ^ { q } , \ x _ { i k } ^ { q } ,$ and $y _ { i k } ^ { q }$ by solving Equation (2) with constraint (10). Because the utility function in (2) is concave and Λ cannot be greater than its unique interior solution, $\gamma ( 1 + \psi ) v / c ,$ , a participating user will always use up the quota, meaning constraint (10) is binding, or $n ( x _ { i j } ^ { q } + y _ { i j } ^ { q } ) + ( 1 - n ) ( x _ { i k } ^ { q ^ { \smile } } + y _ { i k } ^ { q } ) = \Lambda$ Similar to the status quo, with an efective quota, the equilibrium quantities of information are determined by the corresponding posting costs

$$
\begin{array}{l l} x _ {i j} ^ {q} = \frac {\Lambda}{\gamma (1 + \psi)}, & y _ {i j} ^ {q} = \frac {\psi \Lambda}{\gamma (1 + \psi)}, \\ x _ {i k} ^ {q} = \frac {\delta \Lambda}{\gamma (1 + \psi)}, & y _ {i k} ^ {q} = \frac {\delta \psi \Lambda}{\gamma (1 + \psi)}. \end{array}\tag{11}
$$

By sharp contrast to nudging which afects community development in obvious ways (refer to Proposition 2, the platform owner prefers not to nudge any participating users), a quota does not impose any additional cost on users. Hence, it is not obvious whether the community owner’s and social planner’s interests are aligned. We next examine the optimal quota in terms of user participation, total quantity of information posted, and social welfare.

3.3.1. Participation-Maximizing Quota. We first consider user participation. For online communities, particularly those at an early stage of development, having a large user base is critical to triggering network efects among users and seeking financial support from venture capitals. We use the superscript ? to denote the optimal outcomes when the objective is to maximize the number of participating users. Let ι be an infinitesimally small positive number. The following proposition characterizes the optimal quota.

Proposition 3. Imposing a quota on the status quo will weakly increase the number of participating users. The participation-optimal schedule of quota is

(i) When $( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } < v \leq ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } ,$ the optimal quota is $\Lambda ^ { \star } = \iota ,$ which gives participation rates $s _ { L } ^ { \star } =$ $( \stackrel { . } { ( } v - \iota ) / \stackrel { . } { ( } ( 1 - \epsilon ) \lambda _ { L } ) - ( 1 - \alpha ) ) \stackrel { \sim } / ( \alpha ( \stackrel { . } { 1 } - \beta ) ) , \stackrel { . } { s } _ { H } ^ { \star } = 0 ,$ and $s ^ { \star } =$ $( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { L } )$

(ii) When $( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } < v \leq \operatorname* { m i n } \{ ( 1 - \epsilon ) ( 1 -$ $\alpha \beta ) \lambda _ { H } , 2 ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } \}$ , the optimal quota is $\Lambda ^ { \star } \in$ $( \dot { 0 } , [ 2 \gamma ( 1 + \psi ) [ v - ( 1 - \dot { \epsilon } ) ( 1 - \alpha \beta ) \lambda _ { L } ] ] / c )$ , which gives participation rates $s _ { { t } . } ^ { \star } = 1 , s _ { { t } } ^ { \star } = 0 , a n d s ^ { \star } = 1 - \alpha \beta$

(iii) When $( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { { \scriptscriptstyle H } } < v \leq ( 1 - \epsilon ) \lambda _ { { \scriptscriptstyle H } } ,$ the optimal quota is $\Lambda ^ { \star } = \iota ,$ , which gives participation rates $s _ { L } ^ { \star } = 1 , s _ { H } ^ { \star } =$ $( ( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { H } ) - ( 1 - \alpha \beta ) ) / ( \alpha \beta )$ , and $s ^ { \star } = \left( v - \iota \right) /$ $( ( 1 - \epsilon ) \lambda _ { H } )$

(iv) When $( 1 - \epsilon ) \lambda _ { \scriptscriptstyle H } < v < 2 ( 1 - \epsilon ) \lambda _ { \scriptscriptstyle H } ,$ the optimal quota is $\Lambda ^ { \star } \in ( 0 , [ 2 \gamma ( 1 + \psi ) [ v - ( 1 - \epsilon ) \lambda _ { H } ] ] / c )$ , which gives participation rates $s _ { I . } ^ { \star } = 1$ , and $s _ { H } ^ { \star } = 1 , s ^ { \star } = 1$

(v) For all other v, imposing a quota will not improve the participation rate relative to the status quo.

We illustrate Proposition 3 in Figure 4(A). Uncommitted users will participate only when they obtain higher utility from participation than from staying out, which requires the positive posting benefits and externalities to outweigh the (objective) privacy harm. An efective quota limits the amount of information that each user can post. This decrease in information causes the privacy harm to decrease faster than the positive benefits decrease, which tends to encourage users to participate in the community. As shown in Figure $4 ( \mathrm { A } )$ both types of users are now willing to participate with a lower posting benefit, v, compared with the status quo.

3.3.2. Information-Maximizing Quota. We next consider the total quantity of information. Some online communities rely on user activities to generate revenue. For example, Facebook places contextual advertisements related to user feeds. Some specialized communities such as cyberlockers obtain advertising revenues by capitalizing on users’ sharing of digital materials of broad interest. The following proposition characterizes the impact of the quota when the objective is to maximize total information contribution.

Proposition 4. Imposing any efective quota, $\Lambda < ( \gamma$ $( 1 + \psi ) v ) / c$ , will decrease the total quantity of information posted in the community.

A quota does not increase information contribution because it limits the amount of information that a participating user can post. Although it helps attract more users to participate, the incremental gain in information due to these marginal users does not outweigh the loss resulted from the reduction of contribution from every user. Overall, Proposition 4 suggests that imposing a quota will not help an online social community in terms of increasing information contribution.

3.3.3. Welfare-Maximizing Quota. We now consider social welfare. For brevity, we present the optimal quota in the appendix. The following proposition summarizes its impact.

Figure 4. (Color online) Participation and Welfare Comparison  
(A)  
![](/api/attachments/MQ8KCSX7/fulltext/images/c26a2151b65a34f05955e65c6908fe6a6b02149911719bff8e21d2194a1003bb.jpg)

Proposition 5. Imposing a quota to the status quo will increase social welfare. The socially optimal quota presented in the appendix weakly reduces the aggregate privacy harm and increases the number of participating users.

Recall from Proposition 2 that a nudge can improve social welfare only by nudging users out of the community. Here, a quota encourages user participation but reduces the quantity of information posted by each user. More users will join the community and contribute information but, by Proposition 4, the total quantity of information will always decrease. This implies that the net benefit from posting information and privacy harm will decrease for each user. Nevertheless, by the utility specification in (2), the net benefit of positing information will decrease at a slower rate than the privacy harm, leading to an overall improvement in social welfare.<sup>9</sup>

Furthermore, Lemma 2 shows that social welfare is negative when the posting benefit, v, is not high enough because of excessive posting from all participating users. Imposing a quota will also help because, by choosing a suficiently small quota, the social planner can efectively contain the privacy harm generated. As shown in Figure 4(B), the social planner can always achieve a positive social welfare by choosing an appropriate quota.

3.3.4. Quota vs. Nudge. By the above analysis, it is straightforward to see that the quota is better than the nudge in terms of enhancing social welfare.

Proposition 6. The socially optimal quota weakly dominates the socially optimal nudge in improving user participation and social welfare.

By Propositions 1 and 3, a quota increases user participation, but a nudge decreases user participation. More important, the quota preserves users’ incentives to post information. Figure 4(B) shows that the socially optimal quota achieves higher social welfare than the socially optimal nudge when v is suficiently high. When v is small, allowing users to post information is not socially beneficial. Hence, the quota and nudge apply restrictively to discourage user posting. Note that, as shown in Propositions 1 and 4, neither a nudge nor a quota can increase the total quantity of information posted in the community.

(B)  
![](/api/attachments/MQ8KCSX7/fulltext/images/164239e8bab11af69e63659bf757e69f95e68d321edd7878ca9a57a83c7b1b06.jpg)

3.3.5. Quota Choice Between the Community Owner and Social Planner. Interestingly, Propositions 3–5 suggest that the community owner will never prefer a quota when it wants to maximize information contribution, but it may prefer a quota when it wants to grow the number of participating users. Will the community owner and social planner ever prefer the same quota? The answer is yes: A community owner who wants to maximize user participation may prefer the socially optimal quota. Figure 5 plots the optimal quotas that maximize the participation rate and social welfare. The optimal quotas overlap in some ranges of v, meaning they can serve both purposes. See the online appendix for a discussion of the formal conditions where the community owner and social planner prefer the same quota.

## 3.4. Combining Nudge and Quota

We next examine if combining a nudge and a quota gives any complementary benefit. By Proposition 2, the optimal nudge can improve social welfare only by discouraging all users from posting information. Adding a quota is not meaningful and will not make any diference in such a scenario. Therefore, we only consider the efect of adding a nudge on top of a quota.

Let $\tilde { \Lambda } \in ( 0 , \bar { \gamma ( 1 + \psi ) v } / c ]$ be the free quota given to each user, beyond which a nudge τ >˜ 0 will be applied to each additional piece of information posted by the user. Although the option of posting beyond the quota gives users more flexibility in posting information, the following results show that it does not bring any benefit to the community.

Figure 5. (Color online) Participation-Optimal vs. Welfare-Optimal Quotas  
![](/api/attachments/MQ8KCSX7/fulltext/images/e1804f1cebd4888999fd745e18cbf030b9e555656a9560dfaf7e67335b142d5e.jpg)

Proposition 7. The optimal quota weakly dominates the composite policy of adding a nudge to the quota in terms of increasing user participation and social welfare.

With an appropriate composite policy, $\tilde { \Lambda } < ( \gamma ( 1 + \psi )$ $( v - \tilde { \tau } ) ) / c ,$ , the users can post beyond the quota if they are willing to be nudged. Such marginal posts generate more privacy harm on other people, which dissuades sensitive users from joining the community. With fewer participating users, the community as a whole would generate less information. Hence, social welfare will decrease because of lower user participation and less surplus received by each participating user. Intuitively, the composite policy neutralizes the benefit of the quota. The purpose of having a quota is to reduce privacy harm so that the privacy-sensitive users will find joining the community attractive. Allowing users to post beyond the quota, however, induces more privacy harm. This tends to drive the sensitive users out and hence counteracts the quota.

Note that such a composite policy will not increase the total quantity of information posted in the community compared with the status quo. This is because, by Propositions 1 and 4, quota and nudge always decrease information contribution. Hence, any combination of them will lead to a further reduction of information. Together with Proposition 7, we conclude that a composite policy cannot serve the interests of the social planner or the community owner.

## 4. Solving Discord Between the Community Owner and the Social Planner

Many online social communities generate revenues by “dollarizing” their user bases. A common business model is to serve context-based advertisements. For example, Facebook feeds advertisements to users based on their activities such as likes, shares, and comments. The success of such context-based advertising greatly depends on whether the users are active, meaning the community owner may prefer to maximize information contribution by its users. However, our results so far show that a nudge or a quota, or their combinations, will never serve this preference of the community owner despite the fact that the social planner may prefer a nudge or a quota.

In general, consider the user’s utility from joining vis-à-vis staying out of the community. Subtracting Equation (6) from (5)

$$
\begin{array}{r l} & u _ {i | s} ^ {s q, i n - o u t} = \frac {\gamma (1 + \psi) v ^ {2}}{2 c} - (1 - \epsilon) \frac {\gamma (1 + \psi) v s \lambda_ {i}}{c} \\ & \quad = \frac {\gamma (1 + \psi) v ^ {2}}{2 c} - (1 - \epsilon) \cdot \lambda_ {i} \cdot Q ^ {s q} (s), \quad i \in \{L, H \}, \end{array}\tag{12}
$$

where $Q ^ { s q } ( s )$ is the total quantity of information posted in the community given the size of participation, s. User i will join the community if and only if $u _ { i \mid s } ^ { i n - }$ out is nonnegative. To address the privacy harm due to peer disclosure, we must curb user posting of information about other people. This reduces the first term in Equation (12). Because each user would post less, to serve the community owner’s interest in increasing the total quantity of information, we must increase the number of users participating in the community. However, given fixed $( 1 - \epsilon ) \lambda _ { i } ,$ such a requirement necessarily causes $Q ^ { s q } ( s )$ in the second term of Equation (12) to increase. Hence, taken together, $u _ { i \mid s } ^ { s q , i n - o u t }$ will decrease, meaning fewer users will want to participate in the community. This contradicts the requirement of increasing user participation.

Accordingly, any feasible welfare-maximizing solutions that also serve the community owner’s interest in increasing the total quantity of information must decrease $( 1 - \epsilon ) \lambda _ { i }$ in the second term of Equation (12). The next result formalizes the necessary conditions for such solutions.

Proposition 8. To reduce the privacy harm due to peer disclosure without decreasing the total quantity of information posted in the community, we must reduce the average net privacy harm from posting each piece of information, $\lambda _ { L }$ or $\lambda _ { H } ,$ or increase outsiders’ exposure to the information posted within the community, .

Equation (12) and Proposition 8 are important because they highlight the intricate dilemma in the peer disclosure problem, i.e., the contradictory objectives of decreasing privacy harm and maintaining information contribution. They crystallize the necessary characteristics of solutions that can address the peer disclosure problem. How can a community owner simultaneously curb peer disclosure, increase total posts, and improve social welfare? Increasing the community’s visibility, $\epsilon ,$ so that nonparticipating users are more aware of the information posted in the community is one way to entice users to join the community. However, increasing  means that all nonparticipating users would sufer more (perceived) privacy harm, which is not desirable to the social planner. Arguably, making more nonparticipating people sufer is not a good way to boost participation and information contribution. Therefore, in the following discussion, we focus on policies that decrease the average net privacy harm from each piece of information, $\lambda _ { L }$ and $\lambda _ { H }$

The nudge and quota analyzed in Sections 3.2 and 3.3 do not change $\lambda _ { i }$ because they uniformly penalize sensitive and nonsensitive information, causing them to decrease by the same proportion. The community owner may be able to improve the distinction of sensitive from nonsensitive information with, for example, the latest photo-recognition technologies or text mining and natural-language processing techniques. Taking this possibility as given (i.e., we do not consider the community owner’s cost of investing in technologies to detect sensitive information), we discuss some suggestive solutions to address the dilemma highlighted in Proposition 8.

## 4.1. Targeted Nudge and Quota

If distinguishing sensitive from nonsensitive information is possible, then the community owner can impose a nudge or a quota to target sensitive information. As a result, participating users will post less sensitive information relative to nonsensitive information, reducing the overall privacy harm generated by the community. Formally, we add the superscripts tn and tq to all variables when a TN and a TQ are used. When sensitive information can be perfectly separated from nonsensitive information, Equation (12) becomes

$$
\begin{array}{l} u _ {i | s} ^ {t n, i n - o u t} = \underbrace {\frac {\gamma v ^ {2}}{2 c} + \frac {\gamma \psi (v - \tau) ^ {2}}{2 c}} _ {*} \\ \quad - \underbrace {(1 - \epsilon) \cdot Q ^ {t n} (s) \cdot (\lambda_ {i} - \zeta^ {t n})} _ {* *}, \quad i \in \{L, H \}, \\ \text { where } \zeta^ {t n} = \frac {\psi \tau (\theta_ {i} + \omega)}{(1 + \psi) [ v + \psi (v - \tau) ]}, \end{array}\tag{13}
$$

and

$$
\begin{array}{l} u _ {i \mid s} ^ {t q, i n - o u t} = \underbrace {\frac {\gamma v ^ {2}}{2 c} + v \Lambda - \frac {c \Lambda^ {2}}{2 \gamma \psi}} _ {\#} - \underbrace {(1 - \epsilon) \cdot Q ^ {t q} (s) \cdot (\lambda_ {i} - \zeta^ {t q})} _ {\# \#}, \\ \text { where } \quad \zeta^ {t q} = \frac {(\theta_ {i} + \omega) (\gamma \psi v / c - \Lambda)}{(1 + \psi) (\gamma v / c + \Lambda)}. \end{array} \tag {14}\tag{14}
$$

Note that $0 < \tau \leq v$ and $0 < \Lambda < \gamma \psi v / c$ because a user would post only $\gamma \psi v / c$ pieces of sensitive information in the status quo.

Recall that $Q ^ { t n } ( s )$ and $Q ^ { t q } ( s )$ are the total quantities of information posted in the community given participation size, s. Comparing Equations (13) and (12), <sup>(∗)</sup> is smaller than $\gamma ( 1 \bar { + } \psi ) \bar { v ^ { 2 } } / ( \bar { 2 c } )$ because the nudge makes posting information more costly. However, if the targeting is suficiently accurate $( \mathrm { i } . \mathrm { e } . , \bar { \zeta } ^ { t n }$ is suficiently large), then even if user participation increases leading to $Q ^ { t n } ( s ) > Q ^ { s q } ( s )$ , the second term in Equation (13), <sup>(∗∗)</sup>, can still be smaller than the second term in Equation (12), $( 1 - \epsilon ) Q ^ { s q } ( s ) \lambda _ { i }$ . Hence, the TN reduces the average net privacy harm due to peer disclosure, meaning the contradiction highlighted by Equation (12) need not exist. A similar analysis applies to a TQ. When $\zeta ^ { t q }$ is suficiently large, a TQ may increase overall information contribution but suppress privacy harm and increase social welfare.

A real-life implementation of TN is the smartphone app ReThink (ABC News 2015). It alerts users when they try to post ofensive words or phrases in social media. The core component of the app is a database of ofensive trigger words and phrases. In practice, such targeted information controls or nudges cannot completely distinguish sensitive from nonsensitive information. They may generate false positives, i.e., nonsensitive or inofensive information could be wrongly detected as sensitive or ofensive information, or false negatives, passing sensitive or ofensive information that causes harm to others. However, as long as the targeting is suficiently accurate, such approaches to regulating information contribution could help curb privacy harm and increase social welfare. Their deployment is also aligned with the interest of community owners because, by reducing privacy harm, more people may be willing to join online social communities, which can lead to an overall increase in information contribution.

## 4.2. Information Perturbation and Pruning

In the same spirit as the series of data perturbation techniques developed to protect privacy (e.g., Li and Sarkar 2006, Menon and Sarkar 2007), another possible solution to addressing the peer disclosure problem is to help users identify and prune sensitive information $( \mathrm { e . g . }$ , automatically blurring faces or replacing faces with emojis in photos or videos). This can directly reduce the privacy harm caused by each piece of sensitive information and thus decrease $\lambda _ { i }$ . Such IP may cause users to obtain less pleasure in posting information, decreasing v. Referring to Equation (12), this will decrease the user’s posting benefit and the net privacy harm sufered from others’ posting. However, as long as the pruning of sensitive information is suficiently accurate to the extent that it reduces the privacy harm (by reducing λ ) more than the posting benefit (due to a decrease in v), then it can be an efective solution. Arguably, blurring or substituting the faces in a picture by unobtrusive measures could eliminate most privacy harms inflicted on the people involved without significantly hurting the poster’s pleasure.

## 5. Numerical Example

We use a numerical example to demonstrate two results from the above discussion. First, we show that a uniform quota (UQ) and uniform nudge (UN) can increase social welfare and reduce privacy harm under diferent levels of v as shown in Lemma 1 and Propositions 1–5. Second, we show that properly constructed TN, TQ, and IP can resolve the conflict between social planner and community owner as characterized in Section 4, by efectively regulating privacy harm while increasing the number of participating users and social welfare.

Let $\alpha = 0 . 7 , \beta = 0 . 5 , n = 0 . 1 , \psi = 0 . 5 , \delta = 0 . 5 , \epsilon = 0 . 1 ,$ $e = 0 . 1 , \omega = 0 . 0 1 , c = 1 , \theta _ { L } = 0 . 5 ,$ and $\theta _ { H } = 1$ . These values describe an online social community with many strategic users facing high costs of posting sensitive information and posting about strangers in a small friendship network. Users in the community enjoy some recognition benefits. Users not in the community face a small chance of being afected by the privacy externality. As specified in Lemma 1, the equilibrium outcomes in the status quo difer in five ranges of v. We choose the average v in each of these five ranges and construct five sets of outcomes in Table 4.<sup>10</sup> For each value of v in Table 4, we compare the outcomes in the status quo with the outcomes under diferent regulations, including UN, UQ, TN, TQ, and IP. For illustrative purposes, we set the UN at 30% of the posting benefit, v, and the UQ at 70% of the posting volume in the status quo. We set the TN at 60% of v and TQ at 50% of the posting volume of sensitive information in the status quo.<sup>11</sup> Figure 6 plots the results under the diferent levels of v as shown in Table 4.

Table 4. Numerical Example

<table><tr><td></td><td>s</td><td>Q</td><td> $\Pi(\times 10^{-2})$ </td><td> $\xi(\times 10^{-2})$ </td></tr><tr><td colspan="5">v=0.016</td></tr><tr><td>Status quo</td><td>0.300</td><td>0.004</td><td>-0.018</td><td>0.100</td></tr><tr><td>Uniform nudge</td><td>0.300</td><td>0.003</td><td>-0.013</td><td>0.070</td></tr><tr><td>Uniform quota</td><td>0.300</td><td>0.003</td><td>-0.012</td><td>0.070</td></tr><tr><td>Targeted nudge</td><td>0.650</td><td>0.007</td><td>-0.003</td><td>0.100</td></tr><tr><td>Targeted quota</td><td>0.650</td><td>0.007</td><td>0.004</td><td>0.088</td></tr><tr><td>Information pruning</td><td>0.300</td><td>0.004</td><td>-0.007</td><td>0.064</td></tr><tr><td colspan="5">v=0.051</td></tr><tr><td>Status quo</td><td>0.475</td><td>0.020</td><td>-0.074</td><td>0.503</td></tr><tr><td>Uniform nudge</td><td>0.333</td><td>0.010</td><td>-0.036</td><td>0.246</td></tr><tr><td>Uniform quota</td><td>0.618</td><td>0.018</td><td>-0.067</td><td>0.457</td></tr><tr><td>Targeted nudge</td><td>0.650</td><td>0.021</td><td>0.022</td><td>0.316</td></tr><tr><td>Targeted quota</td><td>0.650</td><td>0.021</td><td>0.055</td><td>0.278</td></tr><tr><td>Information pruning</td><td>0.650</td><td>0.025</td><td>-0.032</td><td>0.442</td></tr><tr><td colspan="5">v=0.168</td></tr><tr><td>Status quo</td><td>0.650</td><td>0.090</td><td>0.107</td><td>2.248</td></tr><tr><td>Uniform nudge</td><td>0.650</td><td>0.063</td><td>-0.083</td><td>1.574</td></tr><tr><td>Uniform quota</td><td>0.650</td><td>0.063</td><td>0.233</td><td>1.574</td></tr><tr><td>Targeted nudge</td><td>0.890</td><td>0.096</td><td>0.387</td><td>1.416</td></tr><tr><td>Targeted quota</td><td>1</td><td>0.105</td><td>0.757</td><td>1.396</td></tr><tr><td>Information pruning</td><td>0.740</td><td>0.092</td><td>0.279</td><td>1.643</td></tr><tr><td colspan="5">v=0.337</td></tr><tr><td>Status quo</td><td>0.825</td><td>0.229</td><td>1.390</td><td>5.727</td></tr><tr><td>Uniform nudge</td><td>0.650</td><td>0.126</td><td>0.580</td><td>3.159</td></tr><tr><td>Uniform quota</td><td>1</td><td>0.194</td><td>1.467</td><td>4.860</td></tr><tr><td>Targeted nudge</td><td>1</td><td>0.217</td><td>2.229</td><td>3.193</td></tr><tr><td>Targeted quota</td><td>1</td><td>0.210</td><td>3.579</td><td>2.802</td></tr><tr><td>Information pruning</td><td>1</td><td>0.250</td><td>1.994</td><td>4.457</td></tr><tr><td colspan="5">v=0.458</td></tr><tr><td>Status quo</td><td>1</td><td>0.378</td><td>3.237</td><td>9.446</td></tr><tr><td>Uniform nudge</td><td>0.786</td><td>0.208</td><td>1.261</td><td>5.196</td></tr><tr><td>Uniform quota</td><td>1</td><td>0.264</td><td>4.083</td><td>6.612</td></tr><tr><td>Targeted nudge</td><td>1</td><td>0.295</td><td>4.546</td><td>4.345</td></tr><tr><td>Targeted quota</td><td>1</td><td>0.286</td><td>6.885</td><td>3.813</td></tr><tr><td>Information pruning</td><td>1</td><td>0.340</td><td>4.572</td><td>6.064</td></tr></table>

Note. s, participation size; Q, total posts; Π, social welfare; ξ, total privacy harm.

Consistent with Proposition 1, a UN reduces user participation because it makes information contribution less beneficial. The total quantity of information in the community declines, leading to less privacy harm. It may increase social welfare by driving some marginal users out as Proposition 2 suggests. However, such welfare improvement is possible only when social welfare is negative in the status quo, i.e., when $v = 0 . 0 1 6 \mathrm { o r } 0 . 0 5 1$ . When social welfare is positive in the status quo, i.e., when $v = 0 . 1 6 8 , 0 . 3 3 7 .$ , or 0.458, nudging decreases social welfare.

By Proposition 3, a UQ helps some users obtain a higher surplus and encourages them to join the community. In our example, when $v = 0 . 0 5 1$ or 0.337, imposing a quota can increase user participation. It also enhances social welfare in all of the scenarios as suggested in Proposition 5. However, consistent with Proposition 4, it always decreases the total quantity of information posted in the community.

One dilemma highlighted in Section 4, particularly Equation (12), is that a nondiscriminatory nudge or quota cannot simultaneously increase social welfare, decrease privacy harm, and increase information contribution. We simulate the impacts of imposing a TN and a TQ as analyzed in Section 4.1. We allow the targeting technologies to be imperfect: Nonsensitive information can be misclassified as sensitive (“false positive”) and wrongly suppressed, and sensitive information can be misclassified as nonsensitive (“false negative”). We set the probability of such mistargeting at 10%. See the online appendix for how we derive numerical results for TN and TQ. Furthermore, to illustrate the efect of IP as analyzed in Section 4.2, we multiply v and $\lambda _ { i }$ by discount factors of 90% and 50%, respectively.

As shown in Table 4 and Figure $6 ,$ all three targeting and pruning measures (TN, TQ, and IP) can improve social welfare and reduce the privacy harm. They also increase total information contribution in many scenarios. Specifically, TN and TQ increase total posts when $v = 0 . { \dot { 0 } } 1 6 , 0 . 0 5 { \dot { 1 } }$ , and 0.168, and IP increases total posts when v <sup></sup> 0.051, 0.168, and 0.337. This is achieved by attracting more users to join the community. These numerical results are consistent with our analysis in Section 4, that targeted information control (TN or TQ) and IP can help align the interests of the social planner and the community owner. They can lead to a win–win situation, i.e., increase social welfare, decrease privacy harm, and increase total information contribution.

## 6. Extensions

We assess the robustness of the above analysis by relaxing several key assumptions.

(i) Heterogeneity in friendship. In this extension, we relax the assumption that all users must have the same more friends. The justification is that users who are more privacy sensitive tend to minimize exposure of their personal information, and restricting their friendship network is one efective means to reduce such exposure. Previous research has shown that reciprocity is salient in social networking websites (e.g., Cha et al. 2009, Kumar et al. 2010, Weng et al. 2010), suggesting that people who share more information with others tend to have more friends, which is consistent with our assumption. To simplify the analysis and focus on the impact of heterogeneity in friendship, we assume that all users are uncommitted strategic users in this extension, $\mathrm { i } . \mathrm { e } . , \alpha = 1$ . All other set-ups remain the same as in the main model. The objective function for any user i with $n _ { i }$ friends is specified in Equation (2). We characterize the equilibrium in the status quo in Lemma 4.

Figure 6. (Color online) Graphic Illustration of the Numerical Example  
![](/api/attachments/MQ8KCSX7/fulltext/images/3ab8ca2bf553092c9282b34694c2c46750e53d966b20e4f8ae33092a5c7ffbda.jpg)

![](/api/attachments/MQ8KCSX7/fulltext/images/c14c77e537ba1164b235a9afb51cdf4141647f234b8c214eb79e63331a85c811.jpg)

![](/api/attachments/MQ8KCSX7/fulltext/images/d88bf9dae4b9e5cc7e394a89b022d391fc4fd018ed34b347c94989a4d426e07e.jpg)

![](/api/attachments/MQ8KCSX7/fulltext/images/9c46de60fd83ba5a210c4aa9b6e165067dd272ff8098ba9e8f850dba1c920eab.jpg)  
expected number of friends. We allow for heterogeneity in users’ number of friends and assume that $n _ { i }$ is uniformly distributed between 0 and 1, $\mathbf { i . e . , } n _ { i } \in U [ 0 , 1 ]$ To ensure tractability, we let $\theta _ { i } = 1 - n _ { i } \in [ 0 , 1 ]$ , meaning that users who are less sensitive about privacy have

Lemma 4. In the status quo, (1) when $0 < v < ( 1 - \epsilon )$ $( 1 + 1 / \delta ) ( \psi - e ( 1 + \psi ) - \omega ) / ( 1 + \psi )$ , users with $\theta < \theta ^ { o }$ participate in the community and users with $\theta > \theta ^ { o }$ stay out of the community, where $\theta ^ { \overset { \cdot } { \rho } }$ is the solution to $v = [ ( 1 - \epsilon )$ $\dot { \theta } ^ { o } ( \psi \theta ^ { o } - e ( 1 \bar { + } \psi ) - \omega ) ( 2 - ( 1 - \delta ) \theta ^ { o } ) ] / [ ( 1 + \psi ) ( 1 - |$ $( 1 - \delta ) \theta ^ { o } ) ] ;$ ; (2) when $v \geq ( 1 - \epsilon ) ( 1 + 1 / \delta ) ( \psi - e ( 1 + \psi )$ $- \omega ) / ( 1 + \psi )$ , all users participate in the community.

It is easy to verify that $\theta ^ { o }$ increases in v, meaning that the participation rate is increasing in the posting benefit. This is consistent with our findings from the main model.

We next consider the impact of a nudge. Imposing a nudge reduces a user’s benefit from posting each piece of information. Hence, the impact of a nudge is similar to that of reducing the posting benefit, v. As the participation rate is increasing in v, we expect that a nudge would decrease the participation rate. Furthermore, using a numerical example (see the online appendix), we show that a nudge has a similar impact on the community’s participation rate, total information contribution, total privacy harm, and aggregate user surplus as in the main model.

The analysis of a quota is less straightforward because a UQ is no longer appropriate when users adopt diferent posting strategies based on their numbers of friends. We consider a quota of the following form: $\Lambda _ { i } =$ $f \cdot \gamma _ { i } ( 1 + \psi ) v / c$ , where $\bar { \boldsymbol { f } } \in [ 0 , 1 ]$ and $\gamma _ { i } ( 1 + \psi ) v / c$ is the total amount of information that user i would post in the status quo. In other words, users face diferent quotas contingent on their numbers of friends. We show (see the online appendix) that there exists a quota that (weakly) increases the participation rate and decreases total information contribution and total privacy harm caused by the community, and hence exhibits similar efects as the quota in the main model. We further use numerical analysis (see the online appendix) to show that a properly designed quota improves the social welfare under diferent parameters.

(ii) Nonlinear externality. We consider a scenario when the externalities, $e , \omega ,$ and θ increase with the number of participating users. Realistically, the impact of disclosing sensitive information may increase with audience size. A larger audience increases the chances that the information resonates with interested friends or acquaintances. Let $e ( s ) = e s , \omega ( s ) = \omega s , \theta _ { L } ( s ) \equiv \theta _ { L } s ,$ and $\theta _ { H } ( s ) \equiv \theta _ { H } s = s ,$ , where $s \in ( 0 , 1 )$ is the fraction of participating users. With these changes, the total privacy harm that a user sufers becomes a convex function.

See the online appendix for detailed equilibrium outcomes. Lemma 5 characterizes users’ participation incentives.

Lemma 5. When the externalities increase with the number of participating users, the uncommitted users are more likely to participate in the status quo.

Recall that uncommitted low-type users join the community at a lower v than uncommitted high-type users. When low-type users deliberate their participation decisions, they enjoy less externality because the size of participating users is small, $s < 1$ . Hence, lowtype users will sufer less privacy harm because the community is still small and so will join when v is lower. When v increases, some uncommitted high-type users will gradually join. These early high-type users also sufer less privacy harm and thus have more incentive to join. All of our earlier results on the merits of the regulations continue to apply.

(iii) Unintended Disclosure. In our model, users make posting decisions about sensitive and nonsensitive information, meaning they intentionally divulge others’ sensitive information. See the online appendix for our analysis of a variant in which users make posting decisions about one entire set of information containing sensitive and nonsensitive information. In other words, they unintentionally disclose others’ sensitive information. We assume that an exogenous fraction (unknown to the user) of the posted information causes privacy harm to others. All results in the main model continue to apply in this new setting.

## 7. Discussion and Implications

Using a stylized model, we show that regulation is necessary to control peer disclosure in an online social community. Depending on the benefit from posting information, the community may have too many participants and the participants may post too much information about other people. Although many countries legislate explicit privacy laws to protect consumer privacy, most of these regulations focus on the merchant–consumer relationship involving direct privacy infringement, not third-party privacy harm such as peer disclosure.<sup>12</sup> In privacy disputes resulting from peer disclosure, individuals may pursue a defamation or libel lawsuit against the insulting party. However, such cases are rare because not every sensitive statement on social media can be considered as the basis for a defamation or libel lawsuit. For example, the mere disclosure of the whereabouts of a person may cause the person to lose her job because of dereliction of duties, but such disclosure does not constitute any defamation or libel. Furthermore, suing people for ofensive or disturbing messages may have a negative impact on free speech (Swinford 2012). Practically, it is not feasible to stipulate what a person can say about her friends and peers. Defining and sanctioning peer disclosure could be immensely dificult or costly. Hence, explicit legislation is not likely to be a practicable solution.

We propose two implementable policies, i.e., nudge and quota. A carefully selected nudge or quota can help enhance user welfare, but they work diferently. A nudge helps by driving users who are concerned about privacy out of the community and suppressing those who participate from posting information. A quota helps by reducing the amount of information posted by each user and hence reducing the privacy harm and preserving participation incentives. We show that the community owner will never prefer nudging and mostly does not prefer a quota either except to grow its user base. We present an important necessary condition, Proposition 8, for any regulation to achieve the triple objectives of enhancing social welfare, reducing privacy harm, and increasing information contribution. Based on this condition, we propose three solutions that selectively target diferent kinds of information.

One immediate insight from our analysis in Sections 3.1 and 3.2 is that, lacking any regulation, some users should simply not join online social communities with mediocre benefits from information sharing (cf. the magnitude of privacy harm from peer disclosure). These users should be excluded not because they are “harmful” to other people, but because they are more vulnerable to privacy harm from peer disclosure. The practical implication is that if a person is sensitive about privacy, she should not join online social communities with particularly intimate themes, such as those promoting extramarital afairs or socially improper behaviors such as drug consumption. Similarly, users who are not ready for politically charged discussion or abusive comments with real personal identities should stay out from communities predominated by users who like to post information about, confront or abuse others.

Notwithstanding this insight, regulation is necessary to enhance the collective welfare of users in online social communities. Our nuanced consideration of user participation and information contribution helps explain why almost no online social community is eager to nudge users despite the fact that nudging has been repeatedly advocated (Acquisti 2009, Acquisti et al. 2013, Wang et al. 2013). It also highlights the disadvantage of imposing a quota, that it preserves users’ incentives to join the community but decreases overall information contribution.

Ideally, we want to limit the privacy harm due to peer disclosure but encourage users to participate in the community and contribute more information. Section 4 discusses three solutions that impose a nudge or a quota selectively on sensitive information, or perturb or prune the sensitive information while retaining its informational benefits. Section 5 shows that these solutions can increase social welfare and are aligned with the community owner’s interest. However, they require sophisticated technologies that can identify and target sensitive personal information with reasonable accuracy. Such technologies may be impracticable or too expensive; hence, not all owners of online social communities are willing to develop and deploy them.

Lacking an extrinsic motivation to address privacy harm, how can the community owner be motivated to adopt these regulatory policies (impose a uniform nudge or quota at the cost of less information contribution, or invest in relevant technologies to target sensitive information)? A promising direction is to attribute part of the damage from the privacy harm to the community owner so that it has an incentive to address the harm sufered by privacy-sensitive users. For example, the regulator can help victims take legal actions and seek compensation from the owner of an online social community when the privacy damage from peer disclosure is excessive. Such legal sanctions against platform owners who do not directly impose the damage is not without precedent. For example, the U.S. government shut down MegaUpload.com, a cyberlocker helping users download movies or music shared by other users because it “contributed” to the infringement of the copyright of afected intellectual property owners. It is also common for plaintifs in defamation cases to sue the media for contributing to the damage caused by other people (a situation highly similar to “peer disclosure” in our setting). If the platform owner can be held liable for the information disclosed by its users about their peers, then it should have a stronger, vested incentive to regulate user behaviors.<sup>13</sup>

Although our analysis is framed on peer disclosure, our insights extend to other settings where users impose negative externalities on peers. One example is game invitations on online social communities. Increasingly, games designed for mobile devices encourage players to send invitations to friends before granting additional game credits to the players. This promotional tactic has caused many players to invite friends to try the games, which arguably creates annoyance and inconvenience to peers. Although this practice does not involve disclosure, it intrudes on the peers’ private space and so threatens the seclusion aspect of privacy (Stigler 1980). As such, our analysis directly applies. Nudging or imposing a limit on such “invitations” would help enhance the aggregate user welfare. In fact, we contend that platform owners may have a higher incentive to nudge or cap such game invitations because they are less vested in these promotions.

Numerous instances of externality-curbing policies exist in other P2P applications. For example, BitTorrent, a popular P2P file sharing protocol, reduces network trafic congestion by reducing the download speed for free riders (Hosanagar et al. 2010). Online music streaming services such as Spotify and Pandora have been pressed by music labels to limit free streaming access to alleviate the negative externalities imposed on paying users and musicians (Tofel 2013, O’Connor 2015). Facebook has experimented with charging fees to users who bombard celebrities with unwanted messages to limit the negative externalities generated from such harassment (Legge 2013). Our framework provides a basis for analyzing the optimal choices of policy instruments in these applications.

## 7.1. Implementation

Given our conclusion that regulation is necessary and the identification of the properties of a good regulatory policy, this paper has made an important first step towards improving the privacy and welfare for users participating in online social communities. The next step is to determine how to implement the right nudges or quotas. Lacking an accurate account of privacy externality, we ofer the following guidance.

The first step is to measure the size and privacy sensitivity of users. It may not be feasible to directly poll users about their privacy preferences. Users may not respond to such polls and, even if they do, their responses are likely biased because people tend to exaggerate their privacy needs (Harper and Singleton 2001, Hui et al. 2007, Vasalou et al. 2011). An alternative is to infer users’ preferences from their activities. For example, Facebook can track the frequency of users untagging their names from photos shared by their friends. Google can track delisting requests related to identity removal. Such data can help construct users’ privacy profiles. A potential challenge with this approach is accounting for selection bias as we can only observe the behavior of participating users. This selection bias poses a smaller threat when the participating group is large relative to the nonparticipating group, which is likely the case for prominent communities such as Facebook or Google. Nonetheless, measuring the privacy preferences of people not taking part in online social communities is a good topic for future research.

To set the nudge or quota levels, the community owner can gauge users’ posting benefit, v, using standard marketing techniques such as conjoint analysis (e.g., Hann et al. 2007, Krasnova et al. 2009) or field experiments (e.g., Hui et al. 2007, Beresford et al. 2012). Users’ posting cost, c, consisting of the cost to collect and post peers’ information, can be calibrated based on the nature of the community and the technological sophistication of the users. For example, users in a community of indecent afairs or paparazzi are likely to incur a higher posting cost as the underlying content is more privacy sensitive and dificult to obtain. By contrast, for a community targeting the mass market such as Facebook, users tend to bear much lower information collection and posting costs.

The implementation of a nudge or a quota also requires quantification of personal information because diferent types of personal information vary in privacy sensitivity. Previous research has attempted to quantify the value and sensitivity of personal data (e.g., Hui et al. 2007, Hann et al. 2007). Similar methodologies can be extended to other personal data such as photos or videos. A nudge or a quota can then be applied directly to each piece of “unitized” information.

Nudging can take diferent forms in practice, such as warning messages or visual cues. As a user gains experience, they may become unresponsive to privacy nudges. To ensure the salience of the privacy nudges, the community owner can include a time delay whenever a nudge is applied, for example, by forcing users to read the warning messages. It can also regularly change how and when the warning messages or cues are displayed, or the content of the messages or cues itself. By doing so, users will be less likely to skip the privacy cues.

## 7.2. Limitations and Future Research

Our analysis has several limitations. First, for ease of tractability, we assume two types of users, which allows us to show the responses of users with differing privacy sensitivity to the regulations. Future research should extend the analysis to more heterogeneous users. It may also model homophily which could afect how users form friendships and engage in peer disclosure.

Second, we consider the community owner’s interest in maximizing user participation or posting of information, but we have not developed its objective function. Constructing such a function may help us gain a holistic view of social welfare and the equilibrium behaviors. The challenge lies in how to reasonably capture the difering objectives of online social communities.

Third, this analysis is confined to one online social community and does not consider “multi-homing” (Koh and Fichman 2014). An interesting extension is to allow users to choose between communities and study how their privacy preferences and peer disclosure interact.

Finally, because of complexity with interplays of many factors such as user commitment, privacy concerns, information sensitivity, costs, and the modeling of friendship-network structure, we cannot derive an unambiguous comparative static analysis. Hence, we cannot conclude ${ \mathrm { i f } } ,$ for example, having more committed or privacy-sensitive users will favor a nudge or a quota, or whether regulation is more or less important when the user demographic changes in a particular direction. Developing a more parsimonious model may help overcome this dificulty. However, balancing parsimony and richness of insights is an obvious challenge.

## 8. Concluding Remarks

In 2017, the number of active users on Facebook, WeChat, Instagram, Twitter, and Pinterest was 1.97 billion, 889 million, 600 million, 319 million, and 150 million, respectively (Statistica 2017). There are around 3.2 billion Internet users. This means that Facebook alone has more than 60% penetration. Evidently, these online platforms present people with novel avenues for social interaction. New research is necessary to uncover the implications of such interaction with unprecedented reach and scale.

This paper analyzes one novel behavior in online social communities, peer disclosure of personal information. The sharing of information among friends is mostly unregulated, but its consequence is starting to surface. For example, there have been cases when people were sacked from work because of friends’ posting of their improper behavior in online social communities, and crime syndicates have used data harvested from online social networks to track targeted victims. Studying the implications of peer disclosure and its regulation is an important first step towards shaping a healthy online environment for social interaction. This study serves that purpose.

We find that regulation is necessary. The choice of regulation depends on how privacy is treated in the jurisdiction. A nudge is helpful if privacy is absolutely preferred, whereas a quota is better if we focus on economic utility and are willing to trade privacy for the pleasure of sharing information. Most important, having more users need not be good for the society. Any thoughtful analysis of the benefits of online social communities should consider the pros and cons of user participation and exit and the related benefits and damages in a holistic framework.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their helpful comments. The authors also thank the participants at the 2013 Workshop on Information Systems and Economics and the seminar at the University of Texas at Dallas, and Lizhen Xu, Andrew Whinston, and Jason Chan for their helpful suggestions.

## Appendix

This appendix presents the optimal quota that maximizes the aggregate user surplus. We use the superscript <sup>∗</sup> to denote the associated outcome. Note that ι is an infinitesimally small positive number.

$$
\mathrm{(i)} \text {   When   } \epsilon \leq (1 - \beta) (1 - \lambda_ {L} / \lambda_ {H}) \text {:}
$$

(i.1) $\begin{array} { r } { \mathrm { I f } \ 0 < v \leq ( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } , \Lambda ^ { * } = \iota , } \end{array}$ leading to $s _ { L } ^ { q * } = 0 ,$ $s _ { H } ^ { q * } = \dot { 0 } ,$ , and $s ^ { q * } = 1 - \alpha .$ (i.2) If $( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } < v \leq ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } , \Lambda ^ { * } = \iota ,$ leading $\mathrm { t o } s _ { L } ^ { q * } = ( ( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { L } ) - ( 1 - \alpha ) ) / ( \alpha ( \dot { 1 } - \beta ) ) , s _ { H } ^ { q * } = 0 ,$ and $s ^ { q \bar { * } } = ( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { I } ) .$

(i.3) I $\mathrm { ~ f ~ } ( 1 - \epsilon ) ( 1 - \alpha \bar { \beta } ) \lambda _ { L } < v \leq \bar { \lambda } - ( 1 - \epsilon ) \alpha \beta \lambda _ { H } , \Lambda ^ { * } = \iota ,$ leading t $) s _ { L } ^ { q * } = 1 , s _ { H } ^ { q * } = 0 , \mathrm { a n d } s ^ { q * } = 1 - \alpha \beta .$

(i.4) $\mathrm { I f } \stackrel {  } { \lambda } - ( 1 - \stackrel {  } { \epsilon } ) \alpha \beta \lambda _ { H } < v \leq ( 1 - \epsilon ) ( 2 - \alpha \beta ) \lambda _ { H } - \bar { \lambda } , \Lambda ^ { * } =$ $\gamma ( 1 + \psi ) [ v - \bar { \lambda } + ( 1 - \epsilon ) \dot { \alpha \beta } \lambda _ { H } ] / c ,$ , leading to $s _ { L } ^ { q * } { \overset { . } { = } } 1 , s _ { H } ^ { q * } { = } 0 ,$ , and $s ^ { q * } = 1 - \alpha \beta .$

$$
\text {   If   } (1 - \epsilon) (2 - \alpha \beta) \lambda_ {H} - \bar {\lambda} <   v \leq 2 (1 - \epsilon) (1 - \alpha \beta) \lambda_ {H}, \tag {i.5}
$$

$$
\Lambda^ {*} = 2 \gamma (1 + \psi) [ v - (1 - \epsilon) (1 - \alpha \beta) \lambda_ {H} ] / c,
$$

$$
s _ {H} ^ {q *} = 0, \text {   and   } s ^ {q *} = 1 - \alpha \beta .
$$

$$
s _ {L} ^ {q *} = 1,
$$

$( \mathrm { i } . 6 ) \mathrm { I f } 2 ( 1 - \epsilon ) ( \dot { 1 } - \alpha \beta ) \lambda _ { H } < v \leq 2 ( 1 - \epsilon ) \lambda _ { H } - \bar { \lambda } , \Lambda ^ { * } =$ $( \gamma ( 1 + \psi ) v ) / c ,$ , leading to $s _ { L } ^ { q * } = 1 , ~ s _ { H } ^ { q * } = ( v / ( 2 ( 1 - \epsilon ) \lambda _ { H } ) -$ <sup>(</sup>1 <sup>−</sup> αβ<sup>))/</sup>αβ, and $s ^ { q * } = v / ( 2 ( 1 - \epsilon ) \lambda _ { H } )$

$( \mathrm { i } . 7 ) \mathrm { I f } v > \operatorname * { m a x } \{ 2 ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { H } , 2 ( 1 - \epsilon ) \lambda _ { H } - \bar { \lambda } \} , \Lambda ^ { * } =$ $( \gamma ( 1 + \psi ) ( v - \bar { \lambda } ) ) / c , { \mathrm { l e a d i n g ~ t o ~ } } s _ { L } ^ { q * } = 1 , s _ { H } ^ { q * } = 1$ , and $s ^ { q * } = 1$

$( \mathrm { i i . 1 } ) \mathrm { I f } \ 0 < v \leq ( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } , \Lambda ^ { * } = \iota ,$ leading to $s _ { L } ^ { q * } = 0 ,$ <sup></sup> 0, and s<sup>q∗</sup> <sup></sup> 1 <sup>−</sup> α.

(ii.2) If $( 1 - \epsilon ) ( 1 - \alpha ) \lambda _ { L } < v \leq ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } , \Lambda ^ { * } = \iota ,$ leading t $\textbf { o } s _ { L } ^ { q * } = ( ( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { L } ) - ( 1 - \alpha ) ) / ( \alpha ( \dot { 1 } - \beta ) ) , s _ { H } ^ { q * } = 0 ,$ and $s ^ { q * } = \bar { ( v - \iota ) } / ( ( 1 - \epsilon ) \lambda _ { L } ) .$

(ii.3) $\mathrm { I f } ~ ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { L } < v \leq ( 1 - \epsilon ) ( 1 - \alpha \beta ) \lambda _ { H } , \Lambda ^ { * } = \iota ,$ leading to $s _ { { \scriptscriptstyle I } . } ^ { q * } = 1 , s _ { { \scriptscriptstyle H } } ^ { q * } = 0 , \mathrm { a n d } s ^ { q * } = 1 - \alpha \beta .$

$\mathrm { ( i i . 4 ) ~ \ I \bar { f } { \ ( 1 - \epsilon ) } ( \bar { 1 } - \alpha \beta ) } \lambda _ { H } < v \leq ( 1 - \epsilon ) \lambda _ { H } , \Lambda ^ { * } = \iota ,$ leading to $s _ { L } ^ { q * } = 1 , s _ { H } ^ { q * } = ( ( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { H } ) - ( 1 - \alpha \beta ) ) / ( \alpha \beta ) ,$ , and $s ^ { q * } =$ $( v - \iota ) / ( ( 1 - \epsilon ) \lambda _ { H } ) .$

$( \mathrm { i i } . 5 ) \mathrm { I f } ( 1 - \epsilon ) \lambda _ { H } < v \leq \bar { \lambda } , \Lambda ^ { \ast } = \iota ,$ leading to $s _ { L } ^ { q * } = 1 , s _ { H } ^ { q * } = 1 .$ and s<sup>q</sup> <sup></sup> 1.

(ii.6) If $v > \bar { \lambda } , \Lambda ^ { * } = ( \gamma ( 1 + \psi ) ( v - \bar { \lambda } ) ) / c ,$ , leading to $s _ { L } ^ { q * } = 1 .$ $s _ { H } ^ { q * } = \dot { 1 }$ , and $s ^ { q * } = 1$

## Endnotes

<sup>1</sup> For a comprehensive review of Facebook’s privacy options, see https://www.facebook.com/help/325807937506242/ (accessed May 2017).

<sup>2</sup> Unlike a monetary tax, the cost due to a nonmonetary tax, such as a nudge, cannot be recovered and hence becomes a deadweight loss to the society.

<sup>3</sup> Individuals may participate in online social communities because of undisclosed self-interests, psychological commitments or other altruistic motivations (Bateman et al. 2011). The way we model heterogeneity in user participation resembles the distinction between “altruistic” and “strategic” nodes in P2P media-distribution networks in Hosanagar et al. (2010).

<sup>4</sup> The linear benefit and quadratic cost functions give rise to diminishing marginal utility, which is a common feature in the literature because it is mathematically tractable and often guarantees an interior solution. It also fits real online social networks well. For example, no Facebook user would post all information about every other user, perhaps because doing so is prohibitively costly.

<sup>5</sup> Because the size of the user population is a continuous measure, including user i’s contribution (which is just a point in the integral) does not afect the aggregate sum, Q− . Continuous measures of user population are quite common in the literature (see, e.g., Daughety and Reinganum 2010, Conitzer et al. 2012). This reflects the realistic assumption that one single agent’s decision will not afect the collective outcome for the population.

<sup>6</sup> A random piece of information may or may not be privacy infringing to user i. Therefore, λ<sub>i</sub> is the expected privacy harm if a random piece of information is sensitive and related to user i minus the expected entertainment and recognition benefits otherwise.

<sup>7</sup> See the online appendix for the total perceived privacy harm. The analysis of objective and perceived privacy harms gives similar qualitative insights.

<sup>8</sup> The findings are qualitatively similar if we use a quadratic nudging cost.

<sup>9</sup> Proposition 5 also holds if the net benefit from posting information increases linearly but the privacy harm increases exponentially with the amount of information posted by each user on another user. Realistically, the marginal privacy harm may increase when a user posts more information about her friends, $\mathrm { e . g . } ,$ , the accumulated information may allow others to track a person with a higher precision, which poses a bigger privacy threat.

<sup>10</sup> For the last equilibrium in Lemma 1 where both types of users participate in the community, the range of v can extend to infinity. We choose the last v in Table 4 as $2 ( 1 - \epsilon ) \lambda _ { { \scriptscriptstyle H } } + 0 . 5$

<sup>11</sup> Note that these are not optimal nudges and quotas. The optimal nudges and quotas difer in settings with diferent vs. We choose these values just to illustrate that the uniform and targeted nudges and quotas indeed carry the properties and functions as analyzed in our model.

<sup>12</sup> For example, the European Parliament and Council Directive 95/46/EC states that it “shall not apply to the processing of personal data...by a natural person in the course of a purely personal or household activity.”

<sup>13</sup> Because we have not developed a utility function for the platform owner, we cannot explicitly analyze how this allocation of damage would afect the extent of regulation and the equilibrium outcomes. We do not model the platform owner’s utility because its decision may not be driven purely by economic considerations. We defer the study of the platform owner’s decisions and utility to future research.

## References

ABC News (2015) 15-year-old’s “rethink” app aims to prevent cyberbullying. (August 26), http://abcnews.go.com/Lifestyle/ 15-year-olds-rethink-app-aims-prevent-cyberbullying/story?id <sup></sup>33329748.

Acquisti A (2009) Nudging privacy: The behavioral economics of personal information. IEEE Security Privacy 7(6):82–85.

Acquisti A, Gross R (2009) Predicting social security numbers from public data. Proc. Natl. Acad. Sci. 106(27):10975–10980.

Acquisti A, Brandimarte L, Adjerid I (2013) Gone in 15 seconds: The limit of privacy transparency and control. IEEE Security Privacy 11(4):72–74.

Almuhimedi H, Schaub F, Sadeh N, Adjerid I, Acquisti A, Gluck J, Cranor LF, Agarwal Y (2015) Your location has been shared 5,398 times!: A field study on mobile app privacy nudging. Proc. 33rd Annual ACM Conf. Human Factors Comput. Systems (ACM, New York), 787–796.

Anderson SP, de Palma A (2009) Information congestion. RAND J. Econom. 40(4):688–709.

Anderson SP, Gans J (2011) Platform siphoning: Ad-avoidance and media content. Amer. Econom. J.: Microeconomics 3(4):1–34.

Asvanund A, Clay K, Krishnan R, Smith MD (2004) An empirical analysis of network externalities in peer-to-peer music-sharing networks. Inform. Systems Res. 15(2):155–174.

Backstrom L (2011) Anatomy of Facebook. Facebook Data Team (November 21), https://www.facebook.com/notes/facebook -data-team/anatomy-of-facebook/10150388519243859.

Bateman PJ, Gray PH, Butler BS (2011) Research note—The impact of community commitment on participation in online communities. Inform. Systems Res. 22(4):841–854.

Baumol WJ, Oates WE (1988) The Theory of Environmental Policy, 2nd ed. (Cambridge University Press, New York).

Bennear LS, Stavins RN (2007) Second-best theory and the use of multiple policy instruments. Environ. Resource Econom. 37(1): 111–129.

Beresford AR, Kubler D, Preibusch S (2012) Unwillingness to pay for privacy: A field experiment. Econom. Lett. 117(1):25–27.

Besmer A, Lipford HR (2010) Moving beyond untagging: Photo privacy in a tagged world. Proc. SIGCHI Conf. Human Factors Computing Systems (ACM, New York), 1563–1572.

Bhuller M, Havnes T, Leuven E, Mogstad M (2013) Broadband Internet: An information superhighway to sex crime? Rev. Econom. Stud. 80(4):1237–1266.

Calthrop E, Proost S (1998) Road transport externalities. Environ. Res. Econom. 11(3):335–348.

Cha M, Mislove A, Gummadi KP (2009) A measurement-driven analysis of information propagation in the Flickr social network. Proc. 18th Internat. Conf. World Wide Web (ACM, New York), 721–730.

Chan J, Ghose A, Seamans R (2016) The Internet and racial hate crime: Ofline spillovers from online access. MIS Quart. 40(2): 381–403.

Choi BCF, Jiang Z(J), Xiao B, Kim SS (2015) Embarrassing exposures in online social networks: An integrated perspective of privacy invasion and relationship bonding. Inform. Systems Res. 26(4): 675–694.

Christiansen V, Smith S (2012) Externality-correcting taxes and regulation. Scandinavian J. Econom. 114(2):358–383.

Collinge RA, Oates WE (1982) Eficiency in pollution control in the short and long runs: A system of rental emission permits. Canadian J. Econom. 15(2):346–354.

Conitzer V, Taylor CR, Wagman L (2012) Hide and seek: Costly consumer privacy in a market with repeat purchases. Marketing Sci. 31(2):277–292.

Copes P (1986) A critical review of the individual quota as a device in fisheries management. Land Econom. 62(3):278–291.

Cropper ML, Oates WE (1992) Environmental economics: A survey. J. Econom. Literature 30(2):675–740.

Daughety AF, Reinganum JF (2010) Public goods, social pressure, and the choice between privacy and publicity. Amer. Econom. J.: Microeconomics 2(2):191–221.

Davis R (1999) The Web of Politics: The Internet’s Impact on the American Political System (Oxford University Press, New York).

Dell’Antonia KJ (2016) Don’t post about me on social media, children say. New York Times (March 8), http://well.blogs.nytimes .com/2016/03/08/dont-post-about-me-on-social-media-children -say.

DiMicco JM, Millen DR (2007) Identity management: Multiple presentations of self in Facebook. Proc. Internat. ACM Conf. Supporting Group Work (ACM, New York), 383–386.

Ding AW, Li S, Chatterjee P (2015) Learning user real-time intent for optimal dynamic web page transformation. Inform. Systems Res. 26(2):339–359.

Dwyer C, Hiltz SR, Passerini K (2007) Trust and privacy concern within social networking sites: A comparison of Facebook and MySpace. Proc. Thirteenth Amer. Conf. Inform. Systems, Keystone, CO, 339.

Fullerton D, Metcalf GE (2001) Environmental controls, scarcity rents, and pre-existing distortions. J. Public Econom. 80(2): 249–267.

Galletta DF, Henry RM, McCoy S, Polak P (2006) When the wait isn’t so bad: The interacting efects of website delay, familiarity, and breadth. Inform. Systems Res. 17(1):20–37.

Gross R, Acquisti A (2005) Information revelation and privacy in online social networks: The Facebook case. Proc. 2005 ACM Workshop Privacy Electronic Soc. (ACM, New York), 71–80.

Hann I-H, Hui K-L, Lee S-YT, Png IPL (2007) Overcoming online information privacy concerns: An information-processing theory approach. J. Management Inform. Systems 24(2):13–42.

Hann I-H, Hui K-L, Lee S-YT, Png IPL (2008) Consumer privacy and marketing avoidance: A static model. Management Sci. 54(6):1094–1103.

Harmon A (2003) Fame is no laughing matter for the “star wars kid.” New York Times (May 19), http://www.nytimes.com/2003/05/ 19/business/ compressed-data-fame-is-no-laughing-matter-for -the-star-wars-kid.html.

Harper J, Singleton S (2001) With a grain of salt: What consumer privacy surveys don’t tell us. Competitive Enterprise Inst. 1–18.

Henne B, Smith M (2013) Awareness about photos on the web and how privacy-privacy-tradeofs could help. Adams AA, Brenner M, Smith M, eds. Financial Cryptography and Data Security, Lecture Notes Comput. Sci., Vol. 7862 (Springer, Berlin Heidelberg), 131–148.

Hermalin BE, Katz ML (2006) Privacy, property rights and eficiency: The economics of privacy as secrecy. Quant. Marketing Econom. 4(2):209–239.

Hosanagar K, Han P, Tan Y (2010) Difusion models for peer-to-peer (P2P) media distribution: On the impact of decentralized, constrained supply. Inform. Systems Res. 21(2):271–287.

Hui K-L, Png IPL (2006) The economics of privacy. Hendershott T, ed. Economics and Information Systems, Vol. 1 (Emerald Group Publishing, Bingley, UK), 471–497.

Hui K-L, Teo HH, Lee S-YT (2007) The value of privacy assurance: An exploratory field experiment. MIS Quart. 31(1):19–33.

Johnson JP (2013) Targeted advertising and advertising avoidance. RAND J. Econom. 44(1):128–144.

Keith S, Martin ME (2005) Cyber-bullying: Creating a culture of respect in a cyber world. Reclaiming Children Youth 13(4):224–228.

Koh T-K, Fichman M (2014) Multi-homing users’ preferences for twosided exchange networks. MIS Quart. 38(4):977–996.

Kowalski RM, Limber SP (2007) Electronic bullying among middle school students. J. Adolescent Health 41(6):S22–S30.

Krasnova H, Hildebrand T, Guenther O (2009) Investigating the value of privacy in online social networks: Conjoint analysis. Internat. Conf. Inform. Systems, Phoenix, 173–191.

Kumar R, Novak J, Tomkins A (2010) Structure and evolution of online social networks. Yu PS, Han J, Faloutsos C, eds. Link Mining: Models, Algorithms, and Applications (Springer, New York), 337–357.

Legge J (2013) Facebook now charges you for messages sent to celebrities and people you aren’t friends with. The Independent (April 7), http://www.independent.co.uk/news/uk/home -news/facebook-now-charges-you-for-messages-sent-to-celebrities -and-people-you-arent-friends-with-8563299.html.

Li X-B, Sarkar S (2006) Privacy protection in data mining: A perturbation approach for categorical data. Inform. Systems Res. 17(3): 254–270.

Liebowitz SJ, Margolis SE (1994) Network externality: An uncommon tragedy. J. Econom. Perspect. 8(2):133–150.

Menon S, Sarkar S (2007) Minimizing information loss and preserving privacy. Management Sci. 53(1):101–116.

O’Connor R (2015) Spotify reportedly under pressure from music labels to limit free streaming. The Independent (March 22), http://www.independent.co.uk/arts-entertainment/music/news/ spotify-reportedly-under-pressure-from-music-labels-to-limit -free-streaming-10126106.html.

Ortiz E (2013) Florida teacher fired after she rented party penthouse for students that included alcohol, condoms. New York Daily

News (October 17), http://www.nydailynews.com/news/ national/fla-teacher-fired-allegedly-giving-students-alcohol -condoms-article-1.1488471.

Pigou AC (1920) The Economics of Welfare (Palgrave Macmillan, London).

Pizer WA (2002) Combining price and quantity controls to mitigate global climate change. J. Public Econom. 85(3):409–434.

Posner RA (1978) An economic theory of privacy. Regulation 9(3): 19–26.

Posner RA (1979) Privacy, secrecy, and reputation. Bufalo Law Rev. 28:1–55.

Posner RA (1981) The economics of privacy. Amer. Econom. Rev. 71(2):405–409.

Rajamma RK, Paswan AK, Hossain MM (2009) Why do shoppers abandon shopping cart? Perceived waiting time, risk, and transaction inconvenience. J. Product Brand Management 18(3): 188–197.

Roberts MJ, Spence M (1976) Efluent charges and licenses under uncertainty. J. Public Econom. 5(3-4):193–208.

Sandholm WH (2002) Evolutionary implementation and congestion pricing. Rev. Econom. Stud. 69:667–689.

Sandholm WH (2005) Negative externalities and evolutionary implementation. Rev. Econom. Stud. 72(3):885–915.

Schulze W, d’Arge RC (1974) The Coase proposition, information constraints, and long-run equilibrium. Amer. Econom. Rev. 64(4):763–772.

Statistica (2017) Most famous social network sites worldwide as of April 2017, ranked by number of active users (in millions). https://www.statista.com/statistics/272014/global-social-networks -ranked-by-number-of-users/.

Stavins RN (2011) The problem of the commons: Still unsettled after 100 years. Amer. Econom. Rev. 101(1):81–108.

Stigler GJ (1980) An introduction to privacy in economics and politics. J. Legal Stud. 9(4):623–644.

Swinford S (2012) Drunk Twitter users unlikely to face criminal prosecution. The Telegraph (December 19), http://www .telegraph.co.uk/technology/twitter/9754007/Drunk-Twitter -users-unlikely-to-face-criminal-prosecution.html.

Tofel KC (2013) Pandora caps monthly free tunes on mobiles to 40 hours. Gigaom.com (February 28), https://gigaom.com/2013/ 02/28/pandora-caps-monthly-free-tunes-on-mobiles-to-40-hours/.

Tufekci Z (2008) Can you see me now? Audience and disclosure regulation in online social network sites. Bull. Sci. Tech. Soc. 28(1): 20–36.

Van Zandt T (2004) Information overload in a network of targeted communication. RAND J. Econom. 35(3):542–560.

Vasalou A, Gill AJ, Mazanderani F, Papoutsi C, Joinson A (2011) Privacy dictionary: A new resource for the automated content analysis of privacy. J. Amer. Soc. Inform. Sci. Tech. 62(11): 2095–2105.

Vickrey WS (1963) Pricing in urban and suburban transport. Amer. Econom. Rev. 53(2):452–465.

Wang Y, Leon PG, Scott K, Chen X, Acquisti A, Cranor LF (2013) Privacy nudges for social media: An exploratory Facebook study. Proc. 22nd Internat. Conf. World Wide Web (ACM, New York), 763–770.

Weitzman ML (1974) Prices vs. quantities. Rev. Econom. Stud. 41(4): 477–491.

Weng J, Lim E-P, Jiang J, He Q (2010) Twitterrank: Finding topicsensitive influential twitterers. Proc. Third ACM Internat. Conf. Web Search Data (ACM, New York), 261–270.
