---
otero_id: 1050
otero_key: "CCYKP2RG"
title: "Research Note—Leader Influence on Sustained Participation in Online Collaborative Work Communities: A Simulation-Based Approach"
authors: "Wonseok Oh; Jae Yun Moon; Jungpil Hahn; Taekyung Kim"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0632"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/CCYKP2RG/fulltext/images/3dc74a1e45e4997017847e4146b899203129ad963a5dfe44831183db05a9712b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—Leader Influence on Sustained Participation in Online Collaborative Work Communities: A Simulation-Based Approach

Wonseok Oh, Jae Yun Moon, Jungpil Hahn, Taekyung Kim

To cite this article:

Wonseok Oh, Jae Yun Moon, Jungpil Hahn, Taekyung Kim (2016) Research Note—Leader Influence on Sustained Participation in Online Collaborative Work Communities: A Simulation-Based Approach. Information Systems Research

Published online in Articles in Advance 23 May 2016

http://dx.doi.org/10.1287/isre.2016.0632

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CCYKP2RG/fulltext/images/d2beecd92fb9c9ab09c0aca05d36a68fd0bea91bcce8bae04a0fb512cc6a7720.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Leader Influence on Sustained Participation in Online Collaborative Work Communities: A Simulation-Based Approach

Wonseok Oh

Korea Advanced Institute of Science and Technology, College of Business, Seoul 02455, Korea, wonseok.oh@kaist.ac.kr

Jae Yun Moon

Korea University Business School, Seoul 02841, Korea, jymoon@korea.ac.kr

Jungpil Hahn

School of Computing, National University of Singapore, Singapore 117417, jungpil@nus.edu.sg

Taekyung Kim

Department of Business Administration, University of Suwon, Hwaseong 18323, Korea, kimtk@suwon.ac.kr

rom the perspective of leader-member exchange theory, we investigate how two forms of leadership style (uniform leader-member exchange (ULMX) and differential leader-member exchange (DLMX)) impact member participation in online collaborative work communities (OCWC). Furthermore, based on computer simulations, we also examine the moderating impact of key contextual factors on the relationship between leadership style and member contributions. Efficacy of leadership style in OCWCs is greatly influenced by environmental conditions. DLMX is more effective in sustaining member commitment under high environmental uncertainty, regardless of network size and structure. ULMX is more effective in decentralized structures and during the early stage of community growth. The simulation-based insights suggest that supervisory behavior does matter to member retention and sustained participation in OCWCs, but its impact is significantly moderated by many contextual factors, such as community size, structure, maturity, and environmental uncertainty. In certain situations ULMX prevails, but in others DLMX is more effective. These two forms of governance in fact complement each other, rather than being mutually exclusive forms of leadership style. To attain a maximal outcome, leaders should flexibly adapt their governance styles between DLMX and ULMX over the life cycle of an OCWC to maximize member retention and performance benefits.

Keywords: online collaborative work communities (OCWC); leadership style; uniform LMX; differentiated LMX; sustained participation; network structure; network size; network maturity; computer simulations History: Chris Forman, Senior Editor; Michael Zhang, Associate Editor. This paper was received on April 15, 2013, and was with the authors 17 months for 3 revisions. Published online in Articles in Advance.

## 1. Introduction

The Internet has led to the proliferation of networks of volunteers distributed worldwide engaging in diverse forms of open collaboration to create significant economic value (Forte and Lampe 2013). Such online collaborative work communities (OCWCs) have collectively produced high-quality open source software (OSS) (von Hippel and von Krogh 2003), written a free online encyclopedia (Nov 2007), cocreated remixed music (Jarvenpaa and Lang 2011), and cooperatively produced social news (Goode 2009). OCWCs are now recognized as a viable alternative to the conventional market or firm modes of economic production, with the potential to expand the boundaries of the firm to include discretionary contributions from volunteers (Benkler 2006, Shirky 2008). OCWCs are defined as a “large collectivity of voluntary members whose primary goal is member and collective welfare, whose members share a common interest, experience, or conviction and positive regard for other members, and who interact with one another and contribute to the collectivity primarily over the Net” and whose primary output is “real products, be they software, literary works, or other creations” (Sproull and Arriaga 2007, pp. 898–899, 907). Although there may be many other forms of online communities, our focus is on communities that are primarily engaged in the creation of tangible output. The key defining features of OCWCs are that they consist mainly of volunteers with the goal of collaborative coproduction of information goods.

The voluntary nature of OCWCs poses a challenge for their sustainability because of the many factors (e.g., other online communities, reduced passion, commercial intervention) that may induce members to cease contributing. In fact, membership in many OCWCs is highly volatile with high rates of turnover (Faraj et al. 2011, von Krogh et al. 2003), which can be detrimental (Qin et al. 2014, Ransbotham and Kane 2011). Member retention and sustained participation are crucial for OCWCs’ viability and survival, influencing content volume, quality, interactivity, and responsiveness (Ransbotham and Kane 2011). Sustained online community participation may be driven by diverse intrinsic and extrinsic motivations such as learning, fun, altruism, community identification, member attachment, and need for the collaborative output of the OCWC (e.g., Hertel et al. 2003, Lakhani and Wolf 2005, Ren et al. 2012, von Krogh et al. 2003). Although motivations vary, participants’ behaviors are influenced by peers and prone to herding (Oh and Jeon 2007). Hence, the popular rhetoric regarding OCWCs invokes the image of a leaderless collective, where individuals with varied motivations coordinate and influence one another.

However, leaders play an important role in OCWCs; almost all groups have formal leadership roles that define the initial community-level parameters (e.g., project goal, scope) and attract and retain members on an ongoing basis (Lerner and Tirole 2002, Luther and Bruckman 2011, Weber 2004). Leaders in OCWCs perform an assortment of tasks that are important for group sustainability (Lerner and Tirole 2002). They set the vision and initial blueprint for the final output (Weber 2004). Leaders’ initial choices regarding the OCWCs’ goals and policies (e.g., license choice in OSS development communities) affect the community’s attractiveness for potential participants (Stewart et al. 2006). Leaders’ direct interactions with community members also influence their likelihood of sustained future participation (Johnson 2008, Joyce and Kraut 2006, Huffaker 2010, Xu et al. 2009). A direct response from a prominent core member or leader has a greater impact, because it may be viewed as an indication that one’s contributions are valued (Ducheneaut 2005). The leaders’ role may actually be more critical for member retention in the voluntary setting of OCWCs than in traditional organizations, since participants have no contractual obligations for contributing to the collective (Bock et al. 2008, Koh and Kim 2003). In OCWCs, members can freely join or leave, and participation is in large part influenced by leader behaviors and participation levels of other OCWC members (Oh and Jeon 2007, Weber 2004).

Leaders of OCWCs are faced with challenges that arise from the unique nature of online communities. Member participation is highly peer influenced because reciprocity serves as a driving operational force for OCWCs (Oh and Jeon 2007, Qin et al. 2014). OCWCs often exhibit herding behaviors—members have a strong tendency to match their behaviors to those of other members with whom they interact; and when some members cease contributing or substantially reduce participation levels, those who frequently collaborate with them could become less productive and demotivated and may also lessen their participation (Qin et al. 2014). Such “network influence,” indicating an interpersonal behavioral pattern in which one individual influences the decision of others in socially networked environments (Mason et al. 2007, Watts and Dodds 2007), is most pronounced in knowledge-intensive OCWCs because knowledge is created and accumulated over time mainly through active interaction and dynamic reciprocity among participants. Therefore, when one member discontinues contribution other members may reduce their level of involvement and participation, and subsequently, threaten the stability of the OCWC.

A key question arises: How should leaders behave in these unique environments to best leverage network influence? More specifically, we examine the following research question: What leadership styles are most effective for retaining members and thereby sustaining OCWCs that exhibit network influence dynamics? In spite of the importance of leaders in OCWCs, there has been little work regarding the impact of leader behaviors on retaining member participation, particularly when network influence plays a critical role in shaping the dynamics of member participation and retention. Although recent research (e.g., Johnson et al. 2015) is starting to advance multitheoretical views of what differentiates leaders from followers in online communities, it does not examine what makes leaders effective at inducing highquality contributions from participants. Moreover, the research to date on online leadership has been limited to examining what determines who becomes a leader; so far, there is little research that examines their effectiveness thereafter.

Our agent-based model describes how leadership styles and network influence collectively determine members’ participation in OCWCs. We focus in particular on the impact of different leadership styles on member retention, because ongoing interactions with leaders are important in exerting influence and shaping the collaboration dynamics within the community. This is particularly true of OCWCs that have been initiated by an individual leader. In many OCWCs, the initial founders are likely to take on leadership roles. These formal leaders exert considerable influence over participants in such communities because they define the project goals.

We draw on leader-member exchange (LMX) theory (Graen and Cashman 1975) to elaborate on the quality and strength of leader-member relationships that develop over repeated interactions. Leader-member relationship quality is an important antecedent of turnover and commitment in both formal organizations (Graen et al. 1982a, Harris et al. 2011) and online communities (Yu and Chu 2007). Furthermore, leadership effectiveness is moderated by environmental uncertainty and structural factors, such as organizational size, structure, and maturity (i.e., growth stage in the life cycle of the organization) (e.g., Campion et al. 1993). These factors are thus also likely to have a significant bearing on the extent to which leadership style affects member participation in OCWCs. Therefore, we compare leadership style effects in communities of varying sizes, communication network structures, and maturity states.<sup>1</sup> The impact of leadership styles on sustained member participation in OCWCs may be dynamically emergent and nonlinear as members and leaders constantly influence one another. This creates challenges for isolating, observing, and quantifying the effects empirically. Because of the difficulties of obtaining empirical data regarding the unique environmental conditions that OCWCs face (e.g., diverse forms of network influence and environmental uncertainty), this study adopts a simulation approach, which enables us to rigorously examine different patterns of leader-member communication and their effects on sustaining member participation in OCWCs under varying conditions (Davis et al. 2007).

## 2. Leadership in OCWCs

Leadership has been defined in multiple ways in organizational research over the past several decades (Yukl 2006). Because our interest is in understanding how leadership style affects members’ continued contribution to OCWCs, we define leadership as “the ability of an individual to influence, motivate, and enable others to contribute toward the effectiveness and success of the organizations of which they are members” (House and Javidan 2004, p. 15). Although this definition results from research on leadership in traditional organizations and face-to-face contexts, it applies as well to online leadership (Huffaker 2010). Specifically, our focus is on OCWCs where voluntary members self-organize to collaboratively produce some tangible knowledge product. Leaders in such OCWCs shape the group’s agenda and define the initial task and collective goals.<sup>2</sup> Potential participants judge the attractiveness of the resulting OCWC that has been initiated and structured by the initial founder/leader. Leaders of such OCWCs also possess the most resources related to the collective goal of the OCWC.

Participation in OCWCs is voluntary and driven by diverse intrinsic and extrinsic motivations, and differences in motivations may lead to different choices of locus of participation within the OCWC. For example, members motivated by career benefits and instrumental goals of solving a problem through the OCWCs’ output may be more likely to engage in contributions that increase the chance of establishing direct relationships with the OCWC’s leader, to gain access to the leader’s resources (e.g., code commit rights in OSS development). Members motivated by fun and learning on the other hand may not need to focus on tasks that require direct access to the OCWC’s leader. Their motivations are likely to be just as well fulfilled through collaborating with other OCWC members. Hence, the diversity of motivations leads to a structure where not necessarily all members develop direct relationships with leaders. In short, in addition to the direct impact that leaders’ behaviors have on those with whom they develop relationships, leaders indirectly influence members with whom they have no direct contact through cascading influence from connected members to those who are distant from the leader (Waldman and Yammarino 1999).

Research to date however fails to address the complex dynamically emergent process of leadership influence in interaction with peer influence within OCWCs. Prior research has focused on the behavioral attributes and determinants of emergent leaders (Burke and Kraut 2008, Fleming and Waguespack 2007, Johnson et al. 2015, O’Mahony and Ferraro 2007), the nature of the work performed by online leaders (Butler et al. 2007), and their impact on member participation (Xu et al. 2009). Results are mixed regarding the impact of leader behaviors on online community outcomes. Whereas some find that direct interaction with leaders negatively affect community participation (Johnson 2008), others find that formal leaders’ feedback has stronger effects on contribution rates than peer feedback (Zhu et al. 2013). We contend that the impact of direct interaction with leaders may vary depending on the nature of leader behaviors toward other members, i.e., leadership styles.

The impact of leadership style on member participation is contingent on a number of factors that define the OCWCs’ internal and external environment. Internally, network influence is one such factor, i.e., other members’ behaviors influence the focal participant (Zhu et al. 2011, 2013). External factors that contribute to perceived uncertainty of the OCWCs’ continued viability may also affect participation and how strongly members are affected by different leadership styles. Finally, impact of leadership styles on member retention and participation may also vary depending on contextual attributes of the OCWCs, such as community size, collaboration network structure, and the life cycle stage of community evolution. We examine this premise further in Sections 2.1–2.3.

## 2.1. Leadership Styles: ULMX vs. DLMX

We draw on LMX theory to derive propositions related to the expected impact of leadership styles in OCWCs. Although LMX theory was developed to explain the impact of leaders’ behaviors within formal organizations, it is still useful for conceptualizing leadership impact in OCWCs, because the two are similar in several aspects. First, leaders of both OCWCs and formal organizations have privileged roles. OCWC leaders have the final decision over the contributions that are formally productized or incorporated into the OCWCs’ final output. Traditional organization leaders control resource allocation. Both make discretionary choices regarding the extent to which they will develop close relationships with members through direct personal interactions. Hence, LMX is an appropriate lens in which to examine the impact of leadership style in OCWCs because it is based on the premise that leaders have limited resources and thus are unable to develop relationships with all members. This basic premise is more keenly observable in fact in OCWCs, because the average team size in traditional organizations is small relative to that of OCWCs. Finally, because LMX is an important antecedent of discretionary extra-role organizational citizenship behaviors (OCB)<sup>3</sup> in traditional organizations (Yu and Chu 2007), and predicts performance of virtual world team members (Goh and

Wasko 2012), it is an appropriate theoretical lens to examine the impact of leadership style on member contributions in OCWCs.

Two different approaches to leadership are recognized as having a profound impact on member turnover and organizational performance. The Average Leadership Style (ALS) approach assumes that “the behavior of the leader is in fact reasonably constant for all staff members” (Seeman 1957, p. 95). Studies building on this framework (e.g., Dansereau et al. 1975) posit that leaders treat all subordinates in a uniform manner, independent of their personality, attitudes, and abilities. For example, an ALS leader provides employees with equal opportunities and resources regardless of performance. In short, all dyadic relationships between leaders and members are presumed to be identical, and any deviation from the “average” leadership style is considered random error (Dienesch and Liden 1986).

By contrast, the Vertical Dyad Linkage (VDL) approach, grounded in role theory, asserts that leader behaviors vary contingent on the relationship with particular members (Graen et al. 1982b). The basic tenet of this approach is that leaders have limited resources and time, and hence are not able to act uniformly toward all followers.<sup>4</sup> Instead, leaders establish close relationships with some followers, distinguishing “in-group” members (e.g., those characterized by high trust, interaction, support, and formal/informal rewards) from “out-group” members. For example, a VDL leader may exhibit “bias” in providing additional opportunities and resources to high performers.

ALS and VDL have otherwise been referred to as uniform leader-member exchange (ULMX) and differential leader-member exchange (DLMX), respectively, (Dienesch and Liden 1986, Graen et al. 1982b). Research to date is mixed on the effectiveness of DLMX relative to ULMX.<sup>5</sup> Leaders’ preferential treatment of a subordinate is perceived as unfair by others, leading them to decrease personal communication with the favored subordinate (Sias and Jablin 1995), resulting in undesirable consequences for group relationships and unity (Tal and Babad 1989). DLMX has a negative impact on members’ team commitment, because their perceptions of leader integrity are adversely influenced by differential treatment of team members (Van Breukelen et al. 2002). Coworkers develop stronger relationships under ULMX leadership (Sherony and Green 2002). The Group Value Model (Tyler 1989) also suggests that leader neutrality engenders members’ perception of procedural justice within teams, resulting in more group-oriented behaviors. Taken together, studies in support of ULMX generally view the principle of equality as an operating norm in collaborative work environments.

However, many other studies find that DLMX leads to superior performance outcomes, because it increases positive work attitude and well-being (Epitropaki and Martin 1999), satisfaction, role clarity, member competence (Gerstner and Day 1997), organizational commitment (Martin et al. 2005), and citizenship behaviors (Townsend et al. 2000). This perspective regards equity, rather than equality, as a more ideal norm in group settings. Building on role theory (Merton 1949) and the principle of equity (Adams 1965), DLMX advocates postulate that under resource constraints, both tangible and intangible, leaders should distribute resources to maximize team output, and reward individuals based on personal contributions to the team.

The debate over equity versus equality in organizations continues, as does that over the effectiveness of DLMX and ULMX. However, the vast majority of studies have examined traditional organizational contexts, with little research comparing these leadership styles in the context of OCWCs, where network influence may be stronger, the network sizes larger, and the collaboration structure more varied than in traditional organizational contexts. The present study aims to fill this void.

## 2.2. Environmental Factors

Environmental factors significantly influence the relationship between leadership style and member performance (Waldman et al. 2001, Agle et al. 2006). It is particularly important to recognize the ramifications of network influence and environmental uncertainty on member participation.

2.2.1. Network Influence in OCWCs. Network influence refers to an interpersonal behavioral pattern in which one individual affects the decision of others in socially connected environments (Mason et al. 2007, Watts and Dodds 2007, Aral 2011). The literature on social conformity (e.g., Cialdini and Trost 1998) indicates that social actors are prone to alter behaviors and decisions to accord with others in their environments (Cialdini and Goldstein 2004, DiMaggio and Powell 1983, Salganik and Watts 2009). Such conformity is driven by the desire for affiliation, selfesteem enhancement, accuracy, or efficiency (Cialdini and Goldstein 2004). Network influence engenders behavioral isomorphism and social conformity among connected members, thereby prompting herding in a variety of decision-making situations. Network influence is particularly important when member-member exchange (MMX) (Sherony and Green 2002) is key to establishing social structure, cultivating cohesiveness, and encouraging member commitment beyond the dyadic leader-member exchange. MMX shapes members’ work attitudes and perceptions of organizational climate, affects performance (Seers et al. 1995), and influences the effectiveness of LMX, or vice versa (Graen and Uhl-Bien 1995). In short, network influence affects the dynamics of leadership exchanges.

OCWC members’ commitment levels and participation decisions are highly interdependent (Chang et al. 2010, Faraj et al. 2011, Qin et al. 2014, Singh et al. 2011). Because OCWC members develop a sense of community through intense, long-term collaboration and collective learning, their decisions and conduct are significantly influenced by their network “neighbors” with whom they frequently interact (Butler 2001, Chang et al. 2010, Zhang et al. 2013, Zhu et al. 2013). In certain situations, horizontal peer interaction may be more critical to performance than vertical interaction through LMX (Chen et al. 2007). The departure and reduced participation of peers may negatively affect community members’ motivation to sustain participation. In particular, in knowledgeintensive OCWCs, where tasks are highly interdependent, the prolonged absence of key members may dampen others’ sense of responsibility toward the OCWCs (Qin et al. 2014) and lead them to reduce effort levels or quit (Oh and Jeon 2007). At their worst, such “snowball effects” driven by network influence can result in the collapse of an entire community, although the impact may vary depending on network size and structure.

2.2.2. Impact of Environmental Uncertainty on OCWCs. In the context of OCWCs, environmental uncertainty represents “unpredictable environmental conditions” that influence the stability of volunteerbased self-organized collaborative networks (Oh and Jeon 2007, p. 1090). The vulnerability of self-organized OCWCs to environmental uncertainty and peer influence is described through “temperature” in Ising theory (Ising 1925). “Social temperature” or “social volatility” (Holyst and Kacperski 2001) indicates “a degree of randomness in the behavior of the members of the community” (Malarz 2003, p. 562). In a stable (low-temperature) environment a member’s decision is based on the collective status of connected neighbors, whereas in unstable (high-temperature) environments, such interdependencies sharply diminish.

Many external factors may contribute to the perceived uncertainty of OCWCs’ sustained viability.

When alternative OCWCs exist that afford participants the opportunity to engage in similar activities and achieve analogous goals, participants may find enlisting in other OCWCs easy to accomplish. For example, many open source projects compete for a limited pool of developers; a large number of such initiatives thus fail (Chengalur-Smith et al. 2010). The availability of alternative OCWCs therefore affects member interdependency and commitment to the focal OCWC. Similarly, commercial intervention from large corporations may induce significant governance changes to an OCWC, raising substantial uncertainty about its continued viability, thereby demotivating members from sustaining community membership (O’Mahony 2003, Vaughan-Nichols 2005). Commercial intervention and monetization efforts are likely to undermine members’ intrinsic motivations, as the community’s future direction and stability become unpredictable (O’Mahony 2003).

2.2.3. Network Influence, Environmental Uncertainty, and Leadership Style. Leaders that demonstrate strong direction and guidance under constraints amplify organizational member commitment and intergroup cohesion, particularly under conditions of high environmental volatility and uncertainty (Finkelstein 1992, Waldman et al. 2001). This is because members are more willing to follow a leader in unstable environments as they become apprehensive and perceive an urgent need for direction and guidance (Shamir and Howell 1999).

In OCWCs characterized by network influence, environmental uncertainty moderates the relationship between leadership and member commitment. With all other factors equal, DLMX outweighs ULMX in terms of preserving the stability of member commitment levels in OCWCs under increased uncertainty. DLMX fosters a high degree of trust and understanding between a leader and members (Epitropaki and Martin 1999) and positively affects organizational commitment (Martin et al. 2005) and citizenship behaviors (Townsend et al. 2000). Under DLMX leadership, a core group of members develops close relationships with the leader and are unlikely to cease participation even in the face of high environmental uncertainty. These dedicated members are minimally affected by network influence and retain active interaction with the leader even under adverse conditions (Oh and Jeon 2007). By contrast, members of OCWCs under ULMX leadership diminish their participation when environmental uncertainty increases. Their relationship with the leader can be characterized as fragile and temporary with relatively low levels of trust; this fragile confidence may induce members to terminate contribution when other alternatives become available. Absent a core group of members who are nominally susceptible to network influence, ULMX leadership, in which the leader treats all members equally, faces difficulty in sustaining member commitment under conditions of environmental uncertainty.

<sup>Proposition</sup> <sup>1.</sup> In OCWCs characterized by network influence, DLMX is more effective than ULMX when environmental uncertainty increases.

## 2.3. OCWC Attributes Affecting Effectiveness of Leadership Style

2.3.1. Community Size. Leadership effectiveness is contingent on organizational size (Bass and Norton 1951). In large groups, it is difficult for leaders to interact with all members and manage their resources effectively (Campion et al. 1993), and member contributions are less likely to be individually recognized (Mullen et al. 1987). As the collective grows, the leader’s vision may be transmitted less clearly, which may result in dissatisfaction with organizational goals. All of these factors may substantially weaken members’ intrinsic motivation and their sense of responsibility toward the organization’s goals. Therefore, community size is expected to be negatively associated with sustained member participation.

Although we expect a negative main effect of increased community size on leadership effectiveness, the extent of the negative impact may differ by leadership style. With all else constant, as the community expands, the effectiveness of the DLMX leadership style diminishes more rapidly than that of ULMX. The growth of a network has a direct and negative effect on the amount of time the leader can interact with each member, inversely affecting LMX quality (Graen et al. 1982a). Leaders of larger work units spend less time communicating with their close subordinates and rely more extensively on coercive governance mechanisms (Ford 1981). Perceived resource deficiencies may also significantly influence reciprocating behaviors (Pollard and Mitchell 1972). Hence, LMX quality is negatively associated with network size because of leaders’ limited resources and followers’ perceptions of such deficiencies (Green et al. 1983), diminishing DLMX leadership effectiveness.

Although increased network size may also reduce the effectiveness of ULMX, its impact may be less pronounced. Leaders who treat all followers alike have implicit rules, styles, and structures that characterize their interactions with followers (Dansereau et al. 1975). Increases in community size do not affect these supervisory behavioral tendencies of such ULMX leaders. Consequently, members’ perceptions regarding the nature and strength of the relationship between leader and members remain unaffected even when the network grows. In short, members under ULMX leaders realize that the leader’s attention and support will decrease naturally as the network grows, but they also recognize that such changes will influence all of them equally. Because it affects all subordinates in the same fashion, a leader’s reduced attention and resource as a result of increased network size will be perceived as $\operatorname { \mu } _ { \operatorname { \mathrm { f a i r } } ^ { \prime \prime } }$ (Adams 1965, Janssen 2001) and thus be unlikely to lessen members’ commitment levels in OCWCs under ULMX.

<sup>Proposition</sup> <sup>2.</sup> In OCWCs characterized by network influence, ULMX is more effective than DLMX when network size increases.

2.3.2. Community Network Structure. The network structure through which participants exchange knowledge and coordinate their activities also moderates the effectiveness of leadership (Mullen et al. 1991), i.e., the “fit” between network structure and leadership style affects member performance. A centralized, scale-free network structure (Barabási and Albert 1999), in which node connections are preferentially distributed, enables communities to maintain cohesion and foster trust, authority, and enforce group norms (Baldwin and Clark 2006). Moreover, such network structures facilitate smooth vertical coordination and collaboration among members in different layers. Centralized network structures may also facilitate conflict resolution. Many OCWCs exhibit hierarchies of leaders, coordinators, and users who vertically interact and perform differentiated roles and responsibilities (e.g., Burke and Kraut 2008, Lee and Cole 2003, Oh and Jeon 2007, von Krogh et al. 2003). Such differentiated hierarchical network structures may structurally support DLMX because the leader typically has excessive power and authority.

In contrast to centralized networks, a decentralized, random network (Erd˝os and Rényi 1960) in which each participant has a similar number of communication links preserves a more “democratic” operation because connections are evenly distributed. Such networks structurally inhibit the emergence of a powerful leader given that everyone is endowed with equal resources. Recently, some OCWCs have begun to rely on wiki platforms that allow all users to edit the content to enable participation that is “purely open.” This effectively supports collaborative content production in which content ownership is held jointly by all participants—e.g., Wikipedia, the free online encyclopedia (Wagner 2004). The online communication patterns among participants in some wikibased OCWCs resemble a random network in which connections among nodes are approximately equally distributed. Although a central authority governs member interactions in these OCWCs, participation is truly discretionary and not subject to final incorporation decisions and vetoes by leaders. This network structure is considered generally “democratic”

because each participant has a similar number of connections (i.e., resources). As a result, a DLMX style of governance by a leader may demotivate members and eventually drive them to quit.

<sup>Proposition</sup> <sup>3.</sup> In OCWCs characterized by network influence, DLMX is more effective than ULMX as a governance form for eliciting greater member contribution in centralized, scale-free collaboration network structures. However, when OCWCs show decentralized, random collaboration structures, ULMX is more effective than DLMX.

2.3.3. Community Life Cycle and Leadership Effectiveness. OCWCs differ in the extent to which they are able to elicit active member contributions. Whereas some OCWCs have a substantive number of active participants, others rely on contributions from the leader and a small number of active participants (Oh and Jeon 2007). Although this observed variation may partly stem from OCWC popularity, it may also be due to the community life cycle phase (Iriberri and Leroy 2009). Similar to formal organizations, OCWCs go through phases of inception, creation, growth, maturity, and sustained survival (or death) (Iriberri and Leroy 2009). OCWC leaders may need to exercise different leadership styles contingent on the life cycle phase of the OCWC to maximize member participation. The phases are not linear in progression; OCWCs may iterate through these different phases.

At the inception and creation phases, leaders define the OCWCs’ initial blueprint and goals. Potential participants who perceive fit with their individual goals will start to interact with other community members (Butler et al. 2014). At this stage, to elicit member passion and engagement, leaders should utilize ULMX and focus on community building to entice many members with different skills and interests to join the focal OCWC and stoke their passion for its collective goal (Butler et al. 2014, Faraj et al. 2011). The primary goal of the leader is community building and establishing a critical level of impassioned members rather than to selectively retain members by differentiated behaviors that favor some members over others. As the OCWCs become more mature, the community members have established collective norms and collaborative practices, and the OCWCs have successfully produced some tangible output. In such OCWCs, there are more lasting relationships and trust among members and more participants are committed and motivated to actively contribute to the OCWC output. Hence, DLMX becomes a more effective and efficient governance mechanism than ULMX. Because the complexity and frequency of interactions between a leader and members must expand substantially, exercising ULMX leadership is neither feasible nor effective to promote participation. Furthermore, in such mature OCWCs each member’s roles and skill levels are already identified, which makes it easier for leaders to distribute resources economically and utilize the DLMX approach.<sup>6</sup>

<sup>Proposition</sup> <sup>4.</sup> In OCWCs characterized by network influence, ULMX is more effective than DLMX for engaging more members to be committed to participation during the inception phase of the communities. However, DLMX is more effective than ULMX when OCWCs reach the mature stage.

## 3. Simulation Model and Experimental Design

To provide theoretical insights for the four propositions surrounding the impact of leadership styles on members’ contributions in OCWCs, we adopted a complex adaptive systems perspective and developed computer simulation experiments based on Monte Carlo techniques. We do this for several reasons. First, the simulation method is an effective mechanism since it offers the flexibility of predicting outcomes for a variety of scenarios and situations (Davis et al. 2007). Second, simulation experiments allow us to comprehensively design and assess the effectiveness of the leadership styles (ULMX versus DLMX) for sustaining member participation in OCWCs varying in size, network collaboration structure, state of maturity (i.e., community life cycle phase), and environmental uncertainty. Finally, it poses a challenge to obtain empirical data regarding the unique environmental conditions that OCWCs face, i.e., diverse forms of network influence and environmental uncertainty (temperature). The appropriateness of the simulation method has been corroborated by numerous management studies that deal with the investigation of network influence and other network-driven phenomena (e.g., Abrahamson and Rosenkopf 1997, Watts and Dodds 2007).

## 3.1. Research Approach: Agent-Based Modeling and Simulations

Simulation is a research method for using computer programs to model the operation of “real-world” processes, systems, or events (Law and Kelton 1991). Simulation involves creating an abstracted computational representation of the underlying theoretical logic that links constructs together within a simplified representation of the world having some, but not all, of the characteristics of the world (Lave and March 1975). These representations are then instantiated in a software program that is run repeatedly under varying experimental conditions (e.g., alternative assumptions such as the structure or size of the network, varied construct values such as external influence (temperature), or initial activation levels) to obtain theoretical insights. Simulations are appropriate for studying complex systems arising from bottom-up emergent behaviors of a population of interacting and coevolving agents that act on limited and local interactions (Holland 1995). Such emergent behaviors often exhibit nonlinearity and are as a result very difficult to predict and manage (Anderson 1999, Casti 1994). Participation in OCWCs represents one such complex emergent behavior because members’ participation decisions are impacted by network influence and the extent of influence is affected by the structure of the relationships among participants.

Davis et al. (2007) present a step-by-step roadmap for using simulation methods for theory building, which consists of seven steps: (1) begin with an intriguing research question, (2) identify the simple theory, (3) choose a simulation approach, (4) create a computational representation, (5) verify computational representation, (6) experiment to build novel theory, and (7) validate with empirical data. We carefully followed these prescriptions.<sup>7</sup>

## 3.2. Modeling OCWCs’ Environmental Factors

Following Oh and Jeon (2007), we employed the Ising framework (Ising 1925) to model the quantitative patterns of interaction between leaders and members in simulated OCWC environments. Ising theory models an individual’s decision-making behavior as being influenced by (1) the collective status of neighbors in a network environment and (2) the environmental uncertainty that affects his willingness to participate. To explain the framework’s theoretical building blocks, suppose we have N participants in an OCWC, and each member’s level of participation is numerically quantified: +1 (highly active), −1 (highly inactive), and 0 (neutral). The participant is assumed to regularly “poll” his neighbors to understand the extent of their participation in the community and the intensity of interactions among network constituencies. This member may or may not then change the level of his own participation contingent on his neighbors’ levels and external factors. Some environmental factors $( \mathrm { e . g . }$ , external recognition of the community) may positively influence member participation, whereas others (e.g., availability of other opportunities for contributing) may do so negatively.

Figure 1 (Color online) The Ising Aspect of Network Influence in OCWCs  
![](/api/attachments/CCYKP2RG/fulltext/images/d1314634d457efc872aa3663cb180f4a107d13dff3adc2de61f91eeee8676039.jpg)  
Notes. Each square can be occupied or empty, but only the adjacent neighbors are assumed to interact. The energy of the middle square can be computed as $U = - m _ { 0 } ( m _ { 1 } + m _ { 2 } + m _ { 3 } + m _ { 4 } )$ or $U = - ( \mathsf { f o c a l }$ square5 × 4the sum of its neighbors5, where $m _ { 0 }$ is the status of the focal participant and $m _ { 1 } , m _ { 2 } , m _ { 3 }$ , and $m _ { 4 }$ are the participation status of his four neighbors. Source. Adapted from Oh and Jeon (2007).

Figure 1 illustrates the mechanical aspects of the Ising framework with respect to network influence in the OCWC context. In this spatial network setting, a participant $( m _ { 0 } )$ is assumed to interact frequently with his four neighbors $( m _ { 1 } , m _ { 2 } , m _ { 3 } ,$ and $m _ { 4 } )$ As discussed above, two factors—the collective status of neighbors and environmental uncertainty—are used to define and explain the interaction patterns and network influence among the members. In the original Ising framework, the former is referred to as “energy,” whereas the latter is described as “temperature.” Energy, which is calculated as $U = - m _ { 0 }$ $( m _ { 1 } + \cdots + m _ { 4 } )$ , indicates the collective interaction force between a member and his neighbors. Ising theory suggests that $U > 0$ implies that the majority of members maintain a status (i.e., high participation or low participation) opposite to his $( m _ { 0 } )$ , whereas $U < 0$ indicates that his status $( m _ { 0 } )$ is the same as the majority of his neighbors. Neighbors are evenly split when $U { \bar { = } } 0 . { } ^ { 8 }$

Another important factor that affects a member’s participation decision is environmental uncertainty (or “temperature”), which determines the degree of interdependence and influence among participants. More specifically, in a stable environment (i.e., low temperature) a member’s decision is highly influenced by the collective status of his neighbors, whereas such high interdependencies diminish sharply in unstable environments (i.e., high temperature). The specific Ising formulae are as

follows:

$$
\begin{array}{c} P (\text { change }) = 1 / [ 1 + \exp (\Delta U / T) ], \\ P (\text { stay }) = 1 - P (\text { change }), \end{array}
$$

where P4change5 is the probability that the member will switch his participation status, P 4stay5 is the probability that the member will maintain his participation status, ãU is the difference between current and projected energy after changing participation status, and T is the environmental uncertainty.

The formulae above aptly capture herding propensities due to network influences and the impact of environmental uncertainty. When a member changes participation status (i.e., from −1 to 1 or 1 to −1), the sign of its energy changes (i.e., $U _ { \mathrm { p r o j e c t e d } } = - U _ { \mathrm { c u r r e n t } } ) ,$ and thus the difference in energy is given by $\Delta U =$ $U _ { \mathrm { p r o j e c t e d } } ~ - ~ U _ { \mathrm { c u r r e n t } } ~ = ~ { - U _ { \mathrm { c u r r e n t } } } ~ - ~ U _ { \mathrm { c u r r e n t } } ~ = ~ { - 2 U _ { \mathrm { i n i t i a l } } } .$ Therefore, the more similar a member’s neighbors’ participation status to his own $( \mathrm { i . e . , }$ decreasing U with $\bar { U } < 0 )$ , the energy difference is increased $( \mathrm { i . e . }$ , increasing ãU with $\Delta U > 0 )$ , and the likelihood that he will change participation status is decreased. Conversely, the more different a member’s neighbors are from him (i.e., increasing U with $U > 0 )$ , the more likely he is to switch participation status to match his neighbors’ behaviors. This herding propensity is maximized when environmental uncertainty is low $( \mathrm { i } . \mathbf { e } . , \ T \leq 1 )$ However, as environmental uncertainty increases, network influence is weakened, and herding is less likely to occur as the probability of maintaining one’s participation status and the probability of switching converge (i.e., $P ( \mathrm { c h a n g e } ) \approx \bar { P ( \mathrm { s t a y } ) } \approx \bar { 0 . 5 } )$ . In other words, when environmental uncertainty is high, a member’s participation status no longer depends on his neighbors’ status and becomes less predictable.

In summary, the Ising framework takes into account external factors that affect the level of member participation. In our context, high temperatures indicate high levels of environmental uncertainty such that there are many external factors that induce existing members to leave the community or substantially reduce their amount of contribution. By contrast, low temperatures refer to low levels of uncertainty and limited impact of such destabilizing factors.

## 3.3. Operationalization of OCWC Attributes:

Network Size, Structure, and Maturity Stage OCWCs may vary in terms of size, network structure, and state of maturity. For example, some established OSS communities (e.g., Linux, Apache, etc.) have hundreds of developers and a committee of leaders, whereas other less mature communities are managed by a single leader who interacts with only a small number of members. In addition, although some OCWCs exhibit decentralized, random collaboration structures, many others form highly centralized, scalefree network configurations. Finally, whereas some communities are vibrant with full, active participation from their members, others are managed mostly by a leader with minimal member support.

We operationalized three different levels of OCWC network si $\mathfrak { z e } \_ { N } = \{ 5 0 , 2 5 0 , 5 0 0 \}$ . We operationalized network structures with varying degrees of centrality () following Oh and Jeon (2007). Centralized scale-free networks $( \mathrm { i } . \mathrm { e } . , \ \gamma = 3 )$ were constructed by assigning the number of neighbors to each node randomly drawing from the distribution of the number of neighbors derived from observed OCWC networks (Walsh et al. 2000) and then repeatedly making connections starting from the most highly connected node. To design decentralized, random networks (i.e., $\gamma = 1 . 5 )$ , we chose two random pairs to connect until we exhausted the (chosen) number of connections. Finally, to reflect the diverse maturity stages, i.e., OCWCs at different stages of evolution, we considered three cases in the simulation design—“Highly active communities” (Case 1) where all members actively participate (i.e., all followers are initialized with $^ { \prime \prime } { + } \hat { 1 } ^ { \prime \prime }$ as their activity state), “Medium active communities” (Case 2) where only half of the members participate (i.e., 50% of the followers are initialized with $^ { \bar { \prime \prime } } { + 1 ^ { \prime \prime } }$ and the remaining 50% with $^ { \prime \prime } { - } 1 ^ { \prime \prime }$ as their activity state), and “Highly inactive communities” (Case 3) where no one but a leader actively participates at the initial stage $( \mathrm { i . e . , }$ , all followers are initialized with $^ { \prime \prime } { - } 1 ^ { \prime \prime }$ as their activity state); in all cases, the leader is initialized with and maintains $^ { \prime \prime } { + } 1 ^ { \prime \prime }$ as his state throughout the experiments). We investigated how the two different governance styles (DLMX and ULMX) impact the average participation of members in these cases.

## 3.4. Operationalization of Leadership Styles: ULMX and DLMX

To determine the leader of the networks, we first chose the node with the highest centrality in the network.<sup>9</sup> This is based on examination of the network centrality of the project administrators from our empirical observation of OSS projects, which represent one important type of OCWCs—in 82% of the projects where leadermember interactions were to be found, the project administrator who we defined to be the leader, had the highest centrality. The relational strength between a leader and a member in the ULMX and DLMX cases was operationalized in the simulation as follows. For ULMX, we uniformly assigned a value of 1 to indicate the strength of the relationship between a leader and all developers. In other words, the relational value among all dyadic links between a leader and a member was assumed to be identical, which suggests that a leader treats all members equally. In the case of DLMX it was assumed that the strength of some of these relationships could be greater than or less than 1. To make the comparison more meaningful, no variation in a leader’s resource and capacity exists in both cases. In the case where leaders engaged in DLMX relationships with members, the strength of relationship between a leader and member is calculated as $J _ { L , M } = ( N _ { L } + N _ { M } ) / ( 2 \langle N \rangle )$ 5, where $J _ { L , M }$ is the strength of interaction between a leader (L) and member $( M ) .$ $N _ { L }$ is the number of neighbors that the leader has $N _ { M }$ is the number of neighbors that particular member has, and N  is the average number of neighbors for the whole network. To elucidate numerically, suppose that (1) a DLMX leader (L) has six neighbors $( N _ { L } =$ 6) and a member $( M _ { 1 } )$ has three neighbors $( N _ { M 1 } =$ 3), and that (2) the average number of neighbors N  is four. If they are neighbors themselves, then they can interact. The DLMX strength is then calculated as $( 6 + 3 ) / 8 = 9 / 8 ,$ which is greater than 1. Now consider that another member $( M _ { 2 } )$ has only one neighbor, the DLMX leader. In this case, the interaction strength between L and $M _ { 2 }$ is calculated as $( 6 + 1 ) / 8 = 7 / 8 ,$ which is less than 1. Therefore, even if a leader (L) has more neighbors than the average, the individual interaction strength can be greater or less than 1 depending on the other agent’s number of neighbors. Of course, if $N _ { M 1 }$ (the number of neighbors interacting with $M _ { 1 } )$ is larger than twice the average (in this case 8), then the interaction strength with any of his neighbors will be larger than 1. Consequently, if a node has more neighbors than the average, then on average he will exert a large influence on the network because his neighbors will most likely have an average number of neighbors.

In essence, our theory of OCWC builds on the notion that participation in OCWCs is subject to network influence and external environmental factors. A member’s propensity to participate and contribute is determined by his neighbors’ state of participation (i.e., energy). However this energy can be diminished when external environmental factors compete for the member’s attention and resources. In other words, when external demands are high (i.e., with higher temperature), the strength of the peer influence from the network is weakened.

The extent of network influence is determined by (1) how many connections a member has and (2) the participation state of the members connected to a focal member. At the overall OCWC level, the number of connections the members have is manifested by the network structure and the strength of influence passed on from leader to member is determined by the leadership style. With ULMX, the leader’s attention and influence will be equally distributed among members; whereas with DLMX, the leader’s attention will be unevenly allocated to members where the amount of attention allocated will be proportional to the number of connections the members themselves have. The strength of influence passed on from one member to other members is determined by the level of energy resulting from the participation status of connected members.

## 3.5. Experimental Design and Simulation Procedures

The simulation was conducted as follows. First, we construct an OCWC network according to the various parameters of size $( N = \{ 5 0 , 2 5 0 , 5 0 0 \} )$ , structure $( \gamma =$ 81051 2051 3009), and stage of initial maturity (maturity = {highly active, medium active, highly inactive}). We then operationalize the leadership style governing the OCWC networks by either uniformly assigning initial states of 1 to all edges for ULMX or by assigning differential weights to the edges based on the strengths of the relationships $\left( J _ { L , M } \right)$ for DLMX. Second, we start evolving the network according to the Ising Monte Carlo scheme.<sup>10</sup> Specifically, at each simulated time step, a member is randomly chosen and his participation status is probabilistically determined by network influence for a predetermined level of environmental uncertainty. The overall intensity of member participation for the network m is recorded.<sup>11</sup> The simulation ends once each node has been visited 100 times or more. This procedure was repeated according to a full factorial experimental design with three network sizes $( N = \{ 5 0 , \bar { 2 } 5 0 , 5 0 0 \} ) \times 3$ network structures $( \gamma =$ $\{ 1 . 5 , 2 . 5 , 3 . 0 \} ) \times 3$ initial maturity stages (maturity = {highly active, medium active, highly inactive}), at varying degrees of environmental uncertainty $( T =$ $0 , \ldots , 6 0 )$ . For each leadership style, the simulation generates N data points representing community member participation, which are then averaged. In Section 4, for the sake of brevity, rather than presenting all results in a sequential manner, we selectively report the highly salient and noteworthy results.

## 4. Results

## 4.1. The Effectiveness of Leadership Style Under Environmental Uncertainty

Proposition 1 denotes that in OCWCs characterized by network influence, DLMX is more effective than ULMX as environmental uncertainty increases. The findings derived from the simulation experiment support this argument, showing that DLMX outperforms ULMX in terms of eliciting member contribution as uncertainty becomes greater, regardless of network size and structure (see Figure 2).

## 4.2. Impacts of Network Size and Network Structure

As shown in Figure 3(a), for a given network structure (i.e., highly centralized $\gamma = 3 )$ the effectiveness of DLMX diminishes gradually as environmental uncertainty increases. At low uncertainty, DLMX is highly successful for small communities. However, as uncertainty increases, DLMX becomes a less effective governance mechanism in communities of all sizes, whereas the largest reduction in DLMX effectiveness is observed in small communities. In contrast to DLMX, ULMX leadership style experiences a “sudden collapse” that results from a small increase in uncertainty and becomes nearly insensitive to size variation. Figure 3(b) shows that under ULMX, regardless of network size, member participation sharply increases at low environmental uncertainty, but abruptly declines as the uncertainty increases beyond a critical point. This result lends support for Proposition 2, which states that the negative effect of increased network size is more pronounced for DLMX-style leadership than ULMX-style leadership.

Figure 4 shows how environmental uncertainty moderates the relationship between the effectiveness of leadership and member commitment. The results exhibited in Figure 4 were based on a large community $( N = 5 0 0 )$ , but communities of smaller sizes showed similar patterns. The y-axis represents the difference between the two leadership styles (i.e., DLMX–ULMX) in their ability to elicit member contribution, and the x-axis indicates the degree of network centralization (i.e., from decentralized $( \gamma = 1 . 5 )$ to centralized $( \gamma = 3 . 0 ) )$ . The results indicate that ULMX is better than DLMX in engaging member participation in decentralized networks, regardless of the level of environmental uncertainty. However, as network centralization and environmental uncertainty increase

Figure 2 Effectiveness of DLMX and ULMX with Respect to Size and Structure  
![](/api/attachments/CCYKP2RG/fulltext/images/9e5851a3291bf81d8cfbba72cb91af5f4136262daf0c693511ece7dd82548564.jpg)  
Leadership style ULMX DLMX

Note. N = 8501 2501 5009 represent {small size, medium size, large size} networks, and Gamma = 81051 2051 3009 represent {decentralized, medium, centralized} network structures.

(T > 5), DLMX is more effective in eliciting member contributions. This provides support for Proposition 3, which states that DLMX is more effective for sustaining member participation under more centralized networks.

## 4.3. Community Life Cycle and Leadership Effectiveness

Case 1—Highly Active Communities. For highly active communities, all members of communities were initialized to be fully committed in the project at the

Figure 3 Impact of Network Size (Network Structure Fixed at  = 300)  
![](/api/attachments/CCYKP2RG/fulltext/images/915051ed5a2699e017565ccc06ce53759d1fbd890ab5229037af9585593fb8bd.jpg)

![](/api/attachments/CCYKP2RG/fulltext/images/50502d8918a935d36aa5732db21661099d27350df22973831002f806246458f7.jpg)

![](/api/attachments/CCYKP2RG/fulltext/images/8cea3469253adaef5ede29f016dbb9518bf078c46f75e7df0794905193146430.jpg)

onset.<sup>12</sup> Figure 5 reports the results for large communities (N = 500), but similar patterns are observed in smaller communities. We investigated how the two leadership styles differ in terms of maintaining member commitment in response to the changes in level of environmental uncertainty. Figure 5(a) shows that all of the members in this community are fully committed to participate initially, but as the environment becomes increasingly unstable, their commitment decreases radically. Reduced commitment as a result of environmental uncertainty was found for both leadership styles. However, a more dramatic reduction in average member commitment and participation was observed in communities managed by a ULMX leader compared to the communities managed by a DLMX leader. For example, when environmental uncertainty increases from 0 to 10, member commitment under the DLMX leadership style diminishes moderately by approximately 50% (from 1 to 0.5). However, with the same change in environmental uncertainty, member commitment under ULMX decreases substantially by almost 90% (from 1 to 0.1). In short, in the event of such an environmental shift, only 50 out of 500 members remain actively committed to the OCWC in the case of ULMX. Furthermore, when environmental uncertainty reaches a moderate level (e.g., T = 10), collective member participation under ULMX becomes almost zero, whereas DLMX still sustains member participation at a moderate level (i.e., 0.5).

Figure 4 Environmental Uncertainty and Member Contribution (Network Size Fixed at N = 500)  
![](/api/attachments/CCYKP2RG/fulltext/images/a25094f47380e422230541f8adb7494f0747823740d460b2358b8623870e9b99.jpg)

Case 2—Medium Active Communities. For medium active communities, 50% of the members were initialized as fully committed to participate and contribute to the collective, whereas the remaining 50% were initialized as noncommitted. The results show that as environmental uncertainty increases, collective member participation in this community under ULMX increases initially, but decreases as environmental uncertainty exceeds a certain threshold (T ≈ 4). DLMX exhibits similar patterns as does ULMX, but as in Case 1, DLMX outperforms ULMX in terms of eliciting aggregate member participation in this community (see Figure 5(b)).

<sup>12</sup> Full commitment does not mean that participants are making actual contributions simultaneously. Committed participants have finished their exploration of the OCWCs and have become attached to the focal OCWC, and hence can be relied on to make contributions when needed. In short, they are “active” and tuned in to the work ongoing in the OCWC, and hence participating.

(c) Highly Inactive Communities

(b) Medium Active Communities

(a) Highly Active Communities

Figure 5 Community Maturity and Member Commitment (ULMX vs. DLMX)

![](/api/attachments/CCYKP2RG/fulltext/images/bcb4c24ddfd6e857fbbeaadbb8697475d73b561d992ed1d5b1287b6942f65a3b.jpg)

![](/api/attachments/CCYKP2RG/fulltext/images/e72d68a5ad0a5799e439c84b97a7195774c756410ad45102e739f40cb5cdf593.jpg)

![](/api/attachments/CCYKP2RG/fulltext/images/71bf9a0601fc919177f10798f7198cee5201a90d465460e4184bef1cb13645ea.jpg)  
Environmental uncertainty (T )  
commitment. However, once a community becomes mature and maintains stable member commitment, then DLMX outperforms ULMX in preserving member participation in response to increased environmental uncertainty.

Case 3—Highly Inactive Communities. We also analyzed the case in which no one except the leader is participating initially while all of the members are initially inactive (i.e., in many communities, members exist only in name and are not committed to actively participate). We assigned $^ { \prime \prime } { - } 1 ^ { \prime \prime }$ to indicate a member’s state of inactivity, i.e., members have not developed a level of commitment to the OCWC so as to induce any active contributions. In very stable environments, a community at this stage under DLMX performs marginally better than a community under ULMX. As uncertainty increases, however, people tend to look around for opportunities for participation (note that initially no one was interested in this project) and hence the participation rate goes up as uncertainty increases. Interestingly, ULMX was found to be more efficient in building up network participation, outperforming DLMX, even at very high levels of environmental uncertainty (T ≈ 30). By contrast, the network with DLMX leadership is slower to build up member commitment and ensuing participation, becoming more effective than ULMX only when environmental uncertainty is extremely high (T ≈ 45). In addition, the superiority of DLMX over ULMX at high temperatures (i.e., uncertainty) appears to be only marginal (see Figure 5(c)).

In summary, the findings for the three cases support Proposition 4, which states that ULMX is more effective than DLMX during the initial growth stage of communities, but DLMX outperforms ULMX when OCWCs reach maturity. One consistent finding was obtained across the varying OCWC network sizes and network structures. In contrast to our prediction, ULMX is more effective at sustaining member participation than DLMX under certain conditions, particularly when a leader was primarily responsible for most contributions to the OCWC, with minimal member participation. In other words, when members are not committed and hence not actively participating at the initial stage of the OCWC, ULMX is a more effective leadership style than DLMX in inducing member

## 5. Discussion and Implications

Table 1 summarizes the key findings of the simulation and their important managerial implications for OCWCs. Consistent with our conceptual discussion, the effectiveness of both types of leadership style decreases sharply as environmental uncertainty or network size increases. When network structure, maturity state, and environmental uncertainty are all held constant, the average member participation rate for the small community with only 50 members was, at its peak, three times higher than the rates for the medium and large communities with 250 and 500 members, respectively. The results also suggest that for a small community, DLMX generally outperforms ULMX in terms of enticing member contributions. Furthermore, both types of leadership were ineffective in preventing small communities from experiencing a “sudden collapse” (i.e., an abrupt decrease in member commitment), which often arises from increased environmental uncertainty. Finally, for small communities the effectiveness of the two leadership styles did not change substantially across different network structures, indicating that leadership effectiveness in small communities was almost insensitive to network structure.

For both medium and large communities, however, leadership styles play a more important role. When environmental uncertainty was low, ULMX was superior to DLMX in terms of increasing member commitment, but the reverse was observed at higher levels of environmental uncertainty. This finding suggests that the efficacy of leadership style in OCWCs is greatly influenced by environmental conditions. When the environment is relatively stable, ULMX appears to be

Table 1 Summary of Key Findings and Implications

<table><tr><td>Key findings</td><td>Managerial implications</td></tr><tr><td>In general, leadership effectiveness begins to decline, regardless of governance style (e.g., DLMX and ULMX), as environmental uncertainty increases.</td><td>Environmental uncertaintyRegardless of leadership styles, leaders should routinely scan the environment and promptly react to environmental changes. When the environment becomes more uncertain, leaders should make additional efforts to interact with their members.</td></tr><tr><td>DLMX is more effective than ULMX when environmental uncertainty increases.</td><td>When the environment becomes more volatile, DLMX leaders should collaborate more intensely with their in-group members because these followers play buffer roles that can minimize the damage caused by such variations.</td></tr><tr><td>In general, the effectiveness of both types of leadership styles (e.g., DLMX and ULMX) diminishes as the network expands.</td><td>Network sizeAs communities increase in size, leaders, regardless of what governance mechanism they employ, should interact with more community members and ensure that all members maintain a sense of community and attachment.</td></tr><tr><td>The negative effect of increased network size is more pronounced for DLMX-style leadership than for ULMX-style leadership.</td><td>Leaders who treat their subordinates differently should attempt to maintain LMX quality as high as possible when their communities are expanding. Quantity (i.e., community size) can affect quality (i.e., relationship) under DLMX-style governance.</td></tr><tr><td>Small networks are susceptible to “sudden collapse” even in response to small increases in environmental uncertainty, whereas medium and large networks are relatively less vulnerable to such radical erosions.</td><td>Leaders who manage small OCWCs should be mindful about the vulnerability of their communities in the face of environmental changes. They should frequently scan the environment and exert considerable effort to maintain member participation, particularly when environmental uncertainty looms.</td></tr><tr><td>For both medium and large networks, ULMX outrivals DLMX in stable environments. However, as uncertainty increases, DLMX becomes more effective than ULMX as a governance mechanism.</td><td>Leaders of medium and large OCWCs should utilize a “contingency” approach by which they flexibly employ, depending on the degree of environmental stability, various leadership styles to maximize member participation.</td></tr><tr><td>In general, centralized structures promote a higher level of member participation than random structures, regardless of network size and leadership style. However, a moderately centralized network outperforms a highly centralized one, particularly when the environment is stable.</td><td>Network structureLeaders should establish and promote centralized structures for their OCWCs by actively initiating relationships and communications with OCWC participants to facilitate higher levels of member participation and commitment. However, too much centralization might adversely affect member participation, particularly when a minimal environmental threat exists. Leaders should determine the “right” level of centralization that facilitates the optimal level of member participation.</td></tr><tr><td>In decentralized networks, ULMX outperforms DLMX in stable environments. However, in large communities with more centralized structures, DLMX is not only as effective as ULMX at attracting member participation and increasing commitment but also more enduring than ULMX in response to increases in environmental uncertainty.</td><td>OCWCs that have decentralized structures may not welcome “undemocratic” operations facilitated by DLMX. A “cultural mismatch” might exist between decentralized OCWCs and DLMX, which may adversely affect member participation. However, the importance of such cultural alignment diminishes as environmental threats grow. Consequently, leaders should adopt DLMX to preserve high levels of member participation under high environmental uncertainty.</td></tr><tr><td colspan="2">Maturity state (stage of community evolution)</td></tr><tr><td>In inactive networks, ULMX outperforms DLMX at both low and medium levels of environmental uncertainty. Furthermore, DLMX does not effectively increase member commitment and promote member participation, except at very high levels of uncertainty.</td><td>When OCWCs are in their infancy, the majority of members are just “observing” and not committed to actively participating in community development. In such situations, leaders must adopt more “democratic” leadership styles (e.g., ULMX) to substantially increase member participation. In such “quiet” OCWCs, interacting intensively with only a select few members through DLMX appears to demotivate other members from active participation and dampen their commitment. Leaders of such OCWCs should be more open-minded and responsive to members’ diverse ideas and suggestions.</td></tr><tr><td>In moderately active networks, DLMX performs slightly better than ULMX in terms of attracting member participation. However, compared to highly active networks, the difference is negligible. Interestingly, compared to other maturity states, member participation in these networks is less sensitive to changes in environmental uncertainty.</td><td>When the members of OCWCs start to evolve and exhibit a moderate level of participation (e.g., approximately half of their “existing” members are committed and actively participate), leaders may utilize DLMX to maximize member participation. DLMX is particularly useful when a high degree of environmental uncertainty exists. However, when the environment is stable, ULMX and DLMX can be equally effective. Therefore, leaders in these OCWCs should choose the style that best “fits” their community norms and values.</td></tr><tr><td>In highly active networks that are characteristic of mature communities, DLMX outrivals ULMX regardless of environmental uncertainty. The difference between the two mechanisms becomes wider as the level of uncertainty increases.</td><td>When all OCWC members are fully committed to participating, the leader’s main concern is preserving the current state in response to environmental uncertainties. DLMX is more resilient to environmental changes than ULMX and can structurally preserve a higher level of member commitment and hence participation. Consequently, such a leader should leverage DLMX to its full capacity to ensure the OCWC’s survival.</td></tr></table>

highly effective in stimulating inactive members who are exploring the OCWC to “awaken” and become committed so as to begin contributing, particularly in a decentralized, random structure. By contrast, when environmental uncertainty is low, DLMX tends to exhibit a limited impact on member contributions in a decentralized, large network. However, when environmental uncertainty increases, DLMX outperforms ULMX, irrespective of network structures. Whereas member commitment and contributions under ULMX exhibit a sudden collapse even at low uncertainty, DLMX is more resilient against such abrupt cessations of member contributions. Although variations exist across different network structures, member commitment cultivated by DLMX declined slowly and smoothly even in response to excessive increases in uncertainty. One reason for this stability is that those “in-group” core members who form close relationships with the DLMX leader are unlikely to leave the community because of their high levels of commitment and continue to contribute even in the event of high environmental uncertainty. High levels of mutual trust, dependence, and respect fostered through high-quality DLMX may enforce in-group member resilience in the face of increased environmental uncertainty. Conversely, ULMX may have a structural disadvantage in obtaining and preserving such loyal and passionate members whose contributions are critical to the sustainability of OCWCs, particularly when environmental uncertainty is high.

The findings pertaining to OCWC network size provide several important implications for leaders of OCWCs. First, the larger the community becomes, the weaker the impact of leadership on retaining members and motivating them to contribute. Therefore, leaders of OCWCs should appoint additional leaders to maintain the leader-member ratio at a reasonable level, thereby adopting a “shared-leadership” approach to governance in which multiple leaders collaborate and jointly make key decisions (Carson et al. 2007). This leadership form also embraces a division of labor principle in which each leader, on a day-to-day basis, focuses on his own expertise and interest, and strategic decisions critical to the OCWC are made by a committee of leaders (Fielding 1999). Alternatively, when shared leadership is not a feasible option, leaders of OCWCs must significantly enhance their interactions with members as the community expands. This means that leaders must increase their time commitments and resource commitments proportional to community expansion.

Another important insight is that leaders should wisely and flexibly adjust their leadership style depending on many factors, including community size, maturity state, network structure, and environmental uncertainty. The results derived from the simulation suggest that leadership effectiveness is contingent, to a great extent, on such attributes of OCWCs, refuting the idea of “one leadership style fits all.” To attain a maximal outcome, leaders should flexibly adapt their governance styles between DLMX and ULMX over the life cycle of an OCWC. Apart from network size, network structure was also found to significantly moderate the impact of OCWC leadership style on member participation. When other factors are held constant, centralized networks generally exhibit outcomes that are superior to their decentralized counterparts. This finding indirectly supports the assertion that leaders’ direct interaction with members has a positive performance implication for the member’s level of contribution. A cohesive network structure is useful for quality control, an issue that is faced by many OCWCs. When the project is centrally managed and monitored, consistency is preserved, while conflict among members is resolved amicably through a leader’s intermediation. However, such benefits are difficult to realize in decentralized structures, although the autonomy and diversity available in decentralized formations facilitate the preservation of a creative work environment in an OCWC (Burt 1982).

Although ULMX is generally more effective than DLMX in stimulating member contributions at the low end of environmental uncertainty, the dominance of DLMX over ULMX was consistently observed under high environmental uncertainty across diverse network structures. Furthermore, when all else is equal, DLMX becomes more effective than ULMX as the degree of network centralization increases. DLMX has a “cultural match” with centralized networks, and the same can be said of ULMX and decentralized networks (Sparrowe and Liden 2005). Decentralized networks in which everyone is expected to possess a similar level of authority and responsibility may not welcome a leader’s undemocratic style of operation wherein he interacts and makes decisions in conference with only in-group members. Moreover, in centralized networks where a leader has many followers, he is simply unable to interact intensively with everyone in his circle because of limited time and resources. Consequently, for networks with high degrees of centralization, DLMX is culturally and practically a more successful supervisory form than ULMX. If member retention and sustained participation are of utmost importance, OCWC leaders may consider enhancing the centrality of their community structures by initiating new ties with members who are not currently under their sphere of direct supervision. As the network grows increasingly centralized, leaders need to invest additional time and effort. The spirit of equality manifested in ULMX supervision is often beneficial to OCWCs, particularly under low environmental uncertainty. However, when uncertainty looms large and a significant portion of members are lured to leave a particular community or substantially reduce their commitment, leaders must turn to their “loyal” and passionate members to sustain their communities.

A community’s state of maturity, or stage of evolution in the OCWC life cycle, may also moderate the effectiveness of leadership in OCWCs. For example, when OCWCs are in their infancy and the majority of members are just “observing” and not committed to making frequent contributions, leaders should treat everyone more or less uniformly. For OCWCs in a nascent stage of development, leaders interacting intensely with only a select few members through DLMX could severely demotivate other members and hinder their participation. Therefore, leaders should be more open-minded and responsive to the diverse ideas and suggestions of their members, particularly during the early stage of the community’s development. However, when OCWCs have reached a certain critical mass in terms of members who are committed to participate, preserving a few passionate followers through DLMX is necessary for community sustainability in the event of increased environmental uncertainty.

It should also be noted that all of these findings and implications are relevant and useful when the community’s main objective is to retain its existing members and increase their level of commitment toward active contribution. However, sometimes a certain degree of member turnover is desired and even required to sustain the dynamic inflow and outflow of members to ensure community knowledge expansion (Faraj et al. 2011). Faraj et al. (2011) argue that high member retention may, in fact, have a negative impact on an OCWC’s collective levels of creativity and ingenuity, elements that are often thought to be imperative for the survival of knowledge-intensive online communities (Ransbotham and Kane 2011). If innovation and knowledge novelty are deemed more vital than member retention, leaders may behave differently and counter the suggestions provided to dampen member retention. For example, leaders should promote, rather than inhibit, decentralized structures such that members themselves may collaborate intensively with one another with limited leader supervision and entice new members to join. Similarly, if the community’s primary goal is not to retain members, but to create and share new knowledge, ULMX, instead of DLMX, may be more effective for a community that has reached maturity with full member commitment and participation. This is particularly important for company-hosted user innovation communities for new product development wherein the objective is not to sustain a stable membership base, but to ensure continued collaborative production of new products (Di Gangi et al. 2010, Di Gangi and Wasko 2009, Gallaugher and Ransbotham 2010, Jeppesen and Frederiksen 2006).

This study has several limitations. First, the simulation experiment was employed as a primary analytical instrument because of the difficulties associated with obtaining empirical data for many of the parameters investigated in our study. These include degree of environmental uncertainty, extent of network influence, and amount of member commitment and contributions, as well as identifying OCWCs at different stages of evolution in the OCWC life cycle. Personal interviews and survey methods may be used to operationalize these constructs, but they themselves may be incomplete and inaccurate because of respondents’ potential subjective biases. The simulation experiment was the most appropriate given our research objective because it allowed us to observe the phenomenon in diverse situations and contexts that differ in terms of community size, structure, and maturity states. However, although the simulation model was calibrated on the basis of empirical data, the findings from the experiments provide only initial insights regarding the relationships between leadership style and member contributions, which are moderated by many contextual factors. Therefore, our findings require further research based on empirical data that represent the properties of real-world OCWCs as closely as possible. Moreover, our simulation model was simplified to represent a minimal OCWC and may be further refined. For example, degrees of DLMX variability can be divided into finer levels of granularity to provide more in-depth and comprehensive insights regarding the role of LMX variations on member behaviors. However, although technically feasible, more specific categorizations of these contextual variables require a much greater number of parameter combinations, rendering the results too complex to interpret. Therefore, in this study we opted for model parsimony at the expense of complexity and completeness.

We also note that any results derived from simulation research are firmly based on the construction of the simulation model. For example, our model assumes that network structure and leadership styles are independent. However, the real world is dynamic rather than static. As a result, it is conceivable that leadership style may have an impact on the resulting network structure, which may in turn further influence the leadership style adopted. Our current model does not allow for this kind of dynamic, complex evolution of network structure. We also note that changes in network structure are long-term consequences of agents’ behaviors. In the short term, network structures can be conceptualized as somewhat static and our focal research question relates to uncovering the impacts of leadership styles on OCWC success given a particular network structure. Therefore, our analyses and results do provide at least some important initial insights relating to the efficacy of different leadership approaches in OCWCs. Further research is needed to explore these possibilities. Future research can focus on extending our model by adding network structure dynamics.

Finally, recent research cautions the direct application of theories and models from the physical sciences to explain collective emergent behaviors in online communities because of the difficulty in mapping directly the regular laws of physical entities to the dynamics of human-motivated behaviors (Johnson et al. 2014). Our adoption of the Ising perspective is also subject to these limitations. The Ising perspective employed in this study is just one way that can be used to quantify the patterns of network influence. In this type of conceptualization, a member’s level of contribution is significantly influenced by the collective status of his peers who interact frequently with him. Although members of OCWCs may indeed observe others’ activities in OCWCs, we contend that direct connections will nonetheless exert the greatest influence. Future research should relax our simplifying assumptions that participation levels are mostly influenced through such direct connections. In short, we do not capture the full complexities of network influence in online collaborative work communities. Johnson et al. (2014) found that communication network formation can be explained through a combination of mechanisms drawn from models in physical science (e.g., preferential attachment) and from social psychological motivational theories. Future studies that operationalize network influence differently are also warranted. For example, a member could simply be influenced by one particularly influential member instead of all individuals with whom he interacts.

## 6. Conclusion

From an LMX perspective, this study aimed to provide some initial stylized insights regarding the factors that influence OCWC sustainability. Although some OCWCs successfully preserve membership fluidity through the continuous influx of new members, many others suffer from member turnover and reduced commitment and participation. The simulation-based insights suggest that supervisory behavior does matter to member retention and sustained participation in OCWCs, but its impact is significantly moderated by many contextual factors, such as community size, structure, maturity, and environmental uncertainty. In certain situations ULMX prevails, but in others DLMX is more effective. These two forms of governance in fact complement each other, rather than being mutually exclusive forms of leadership style. Therefore, the traditional debate over which form of leadership is universally superior does not provide much fruitful guidance for understanding leadership dynamics in OCWCs. Savvy leaders who understand the complex nature of OCWCs may successfully adjust their supervisory behaviors and complementarily use both DLMX and ULMX leadership styles to maximize benefits to their OCWCs.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0632.

## Acknowledgments

The authors thank the senior editor, associate editor, and the anonymous reviewers for their constructive comments and valuable suggestions on the paper. This study was supported by the National University of Singapore Academic Research Fund (AcRF) Tier 1 Start Up Research Grant. The research is partially supported by the research fund at Korea University Business School. The second author is the corresponding author of this paper.

## References

Abrahamson E, Rosenkopf L (1997) Social network effects on the extent of innovation diffusion: A computer simulation. Organ. Sci. 8(3):289–309.

Adams JS (1965) Inequity in social exchange. Berkowitz L, ed. Advances in Experimental Social Psychology, Vol. 2 (Academic Press, New York), 267–299.

Agle BR, Nagarajan NJ, Sonnenfeld JA, Srinivasan D (2006) Does CEO charisma matter? An empirical analysis of the relationships among organizational performance, environmental uncertainty, and top management team perceptions of CEO charisma. Acad. Management J. 49(1):161–174.

Anderson P (1999) Complexity theory and organization science. Organ. Sci. 10(3):216–232.

Aral S (2011) Identifying social influence: A comment on opinion leadership and social contagion in new product diffusion. Marketing Sci. 30(2):217–223.

Baldwin CY, Clark KB (2006) The architecture of participation: Does code architecture mitigate free riding in the open source development model? Management Sci. 52(7):1116–1127.

Barabási A-L, Albert R (1999) Emergence of scaling in random networks. Science 286(5439):509–512.

Bass BM, Norton FT (1951) Group size and leaderless discussions. J. Appl. Psych. 35(6):397–400.

Bateman PJ, Gray PH, Butler B (2011) The impact of community commitment on participation in online communities. Inform. Systems Res. 22(4):841–854.

Benkler Y (2006) The Wealth of Networks: How Social Production Transforms Markets and Freedom (Yale University Press, New Haven, CT).

Bock GW, Ng WL, Shin YY (2008) The effect of a perceived leader’s influence on the motivation of the members of nonworkrelated virtual communities. IEEE Trans. Engrg. Management 55(2):292–303.

Burke M, Kraut RE (2008) Mopping up: Modeling Wikipedia promotion decisions. ACM Conf. Comput. Supported Cooperative Work (ACM, New York), 27–36.

Burt RS (1982) Toward a Structural Theory of Action: Network Models of Social Structure, Perception, and Action (Academic Press, New York).

Butler BS (2001) Membership size, communication activity, and sustainability: A resource-based model of online social structures. Inform. Systems Res. 12(4):346–362.

Butler BS, Bateman PJ, Gray PH, Diamant EI (2014) An attractionselection-attrition theory of online community size and resilience. MIS Quart. 38(3):699–728.

Butler BS, Sproull LS, Kiesler S, Kraut RE (2007) Community effort in online groups: Who does the work and why? Weisband SP, ed. Leadership at a Distance: Research in Technologically Supported Work (Lawrence Erlbaum, Mahwah, NJ), 171–194.

Campion MA, Medsker GJ, Higgs AC (1993) Relations between work group characteristics and effectiveness: Implications for designing effective work groups. Personnel Psych. 46(4): 823–850.

Carson JB, Tesluk PE, Marrone JA (2007) Shared leadership in teams: An investigation of antecedent conditions and performance. Acad. Management J. 50(5):1217–1234.

Casti J (1994) Complexification: Explaining a Paradoxical World Through the Science of Surprise (HarperCollins, New York).

Chang RM, Oh W, Pinsonneault A, Kwon D (2010) A network perspective of digital competition in online advertising industries: A simulation-based approach. Inform. Systems Res. 21(3): 571–593.

Chen Z, Lam W, Zhong JA (2007) Leader–member exchange and member performance: A new look at individual-level negative feedback-seeking behavior and team-level empowerment climate. J. Appl. Psych. 92(1):202–212.

Chengalur-Smith I, Sidorova A, Daniel S (2010) Sustainability of free/libre open source projects: A longitudinal study. J. Assoc. Inform. Systems 11(Special Issue):657–683.

Cialdini RB, Goldstein NJ (2004) Social influence: Compliance and conformity. Annual Rev. Psych. 55:591–621.

Cialdini RB, Trost MR (1998) Social influence: Social norms, conformity and compliance. Gilbert DT, Fiske ST, Lindzey G, eds. The Handbook of Social Psychology, 4th ed., Vol. 2 (McGraw-Hill, New York), 151–192.

Dansereau F, Graen G, Haga WJ (1975) A vertical dyad approach to leadership within formal organizations. Organ. Behav. Human Performance 13(1):46–78.

Davis JP, Bingham CB, Eisenhardt KM (2007) Developing theory through simulation methods. Acad. Management Rev. 32(2): 480–499.

Di Gangi PM, Wasko MM (2009) Steal my idea! Organizational adoption of user innovations from a user innovation community: A case study of Dell IdeaStorm. Decision Support Systems 48(1):303–312.

Di Gangi PM, Wasko MM, Hooker RE (2010) Getting customers’ ideas to work for you: Learning from Dell how to succeed with online user innovation communities. MIS Quart. Executive 9(4):163–178.

Dienesch RM, Liden RC (1986) Leader-member exchange model of leadership: A critique and further development. Acad. Management Rev. 11(3):618–634

DiMaggio P, Powell W (1983) The iron cage revisited: Institutional isomorphism and collectivity rationality in organizational fields. Amer. Sociol. Rev. 48(2):147–160.

Ducheneaut N (2005) Socialization in an open source software community: A socio-technical analysis. Comput. Supported Cooperative Work 14(4):323–368.

Epitropaki O, Martin R (1999) The impact of relational demography on the quality of leader-member exchanges and employees’ work attitude and well-being. J. Occupational Organ. Psych. 72(2):237–240.

Erd˝os P, Rényi A (1960) On the evolution of random graphs. Publications Math. Inst. Hungarian Acad. Sci. 5:17–61.

Faraj S, Jarvenpaa SL, Majchrzak A (2011) Knowledge collaboration in online communities. Organ. Sci. 22(5):1224–1239.

Fielding RT (1999) Shared leadership in the Apache project. Comm. ACM 42(4):42–43.

Finkelstein S (1992) Power in top management teams: Dimensions, measurement, and validation. Acad. Management J. 35(3): 505–538.

Fleming L, Waguespack DM (2007) Brokerage, boundary spanning, and leadership in open innovation communities. Organ. Sci. 18(2):165–180.

Ford J (1981) Departmental context and formal structure as constraints on leader behavior. Acad. Management J. 24(2):274–288.

Forte A, Lampe C (2013) Defining, understanding, and supporting open collaboration: Lessons from the literature. Amer. Behavioral Scientist 57(5):535–547.

Gallaugher J, Ransbotham S (2010) Social media and customer dialog management at Starbucks. MIS Quart. Executive 9(4): 197–212.

Gerstner CR, Day DV (1997) Meta-analytic review of leadermember exchange theory: Correlates and construct issues. J. Appl. Psych. 82(6):827–844.

Goh S, Wasko M (2012) The effects of leader-member exchange on member performance in virtual world teams. J. Assoc. Inform. Systems 13(10):861–885.

Goode L (2009) Social news, citizen journalism and democracy. New Media Soc. 11(8):1287–1305.

Graen G, Cashman JF (1975) A role-making model of leadership in formal organizations: A developmental approach. Hunt JG, Larson LL, eds. Leadership Frontiers (Kent State University Press, Kent, OH), 143–165.

Graen G, Uhl-Bien M (1995) Relationship-based approach to leadership: Development of leader-member exchange (LMX) theory of leadership over 25 years: Applying a multi-level multidomain perspective. Leadership Quart. 6(2):219–247.

Graen G, Novak M, Sommerkamp P (1982a) The effects of leadermember exchange and job design on productivity and satisfaction: Testing a dual attachment model. Organ. Behav. Human Performance 30(1):109–131.

Graen GB, Liden RC, Hoel W (1982b) Role of leadership in the employee withdrawal process. J. Appl. Psych. 67(6):868–872.

Green SG, Blank W, Liden RC (1983) Market and organizational influences on bank employees’ work attitudes and behaviors. J. Appl. Psych. 68(2):298–306.

Harris KJ, Wheeler AR, Kacmar KM (2011) The mediating role of organizational job embeddedness in the LMX-outcomes relationships. Leadership Quart. 22(2):271–281.

Hertel G, Niedner S, Herrmann S (2003) Motivation of software developers in open source projects: An Internet-based survey of contributors to the Linux kernel. Res. Policy 32(7):1159–1177.

Holland JH (1995) Hidden Order: How Adaptation Builds Complexity (Perseus Books, Reading, MA).

Holyst JA, Kacperski K (2001) Social impact models of opinion dynamics. Annual Rev. Comput. Phys. 9:253–273.

House RJ, Javidan M (2004) Overview of GLOBE. House RJ, Hanges PJ, Javidan M, Dorfman PW, Gupta V, eds. Culture, Leadership, and Organizations: The GLOBE Study of 62 Societies (Sage, Thousand Oaks, CA), 9–28.

Huffaker D (2010) Dimensions of leadership and social influence in online communities. Human Comm. Res. 36(4):593–617.

Iriberri A, Leroy G (2009) A life-cycle perspective on online community success. ACM Comput. Surv. 41(2):1–29.

Ising E (1925) Beitrag zur Theorie des Ferromagnetismus. Zeitschrift für Physik 31(1):253–258.

Janssen P (2001) Fairness perceptions as a moderator in the curvilinear relationships between job demands, and job performance and job satisfaction. Acad. Management J. 44(5): 1039–1050.

Jarvenpaa SL, Lang KR (2011) Boundary management in online communities: Case studies of the Nine Inch Nails and ccMixter music remix sites. Long Range Planning 44(5–6):440–457.

Jeppesen LB, Frederiksen L (2006) Why do users contribute to firmhosted communities? The case of computer-controlled music instruments. Organ. Sci. 17(1):45–63.

Johnson SL (2008) Impact of Leadership on Continued Participation in Online Groups (University of Maryland, College Park, MD).

Johnson SL, Faraj S, Kudaravalli S (2014) Emergence of power laws in online communities: The role of social mechanisms and preferential attachment. MIS Quart. 38(3):795–808.

Johnson SL, Safadi H, Faraj S (2015) The emergence of online community leadership. Inform. Systems Res. 26(1):165–187.

Joyce E, Kraut RE (2006) Predicting continued participation in newsgroups. J. Comput.-Mediated Comm. 11(3):723–747.

Koh J, Kim YG (2003) Sense of virtual community: A conceptual framework and empirical validation. Internat. J. Electronic Comm. 8(2):75–93.

Lakhani KR, Wolf R (2005) Why hackers do what they do: Understanding motivation and effort in free/open source projects. Feller J, Fitzgerald B, Hissam S, Lakhani KR, eds. Perspectives on Free and Open Source Software (MIT Press, Cambridge, MA), 3–21.

Lave C, March JG (1975) An Introduction to Models in the Social Sciences (Harper & Row, New York).

Law AM, Kelton DW (1991) Simulation Modeling and Analysis, 2nd ed. (McGraw-Hill, New York).

Lee GK, Cole RE (2003) From a firm-based to a community-based model of knowledge creation: The case of the Linux kernel development. Organ. Sci. 14(6):633–649.

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Luther K, Bruckman A (2011) Leadership and success factors in online creative collaboration. IEEE Potentials 30(5):27–32.

Malarz K (2003) Social phase transition in Solomon network. Internat. J. Modern Phys. C 14(5):561–565.

Martin R, Thomas G, Charles K, Epitropaki O, McNamara R (2005) The role of leader-member exchanges in mediating the relationship between locus of control and work reactions. J. Occupational Organ. Psych. 78(1):141–147.

Mason WA, Conrey FR, Smith ER (2007) Situating social influence processes: Dynamic, multidirectional flows of influence within social networks. Personality Soc. Psych. Rev. 11(3):279–300.

Merton RK (1949) Social Theory and Social Structure (Free Press, New York).

Mullen B, Johnson C, Salas E (1991) Effects of communication network structure: Components of positional centrality. Soc. Networks 13(2):169–185.

Mullen B, Johnson DA, Drake SD (1987) Organizational productivity as a function of group composition: A self-attention perspective. J. Soc. Psych. 127(2):143–150.

Nov O (2007) What motivates Wikipedians? Comm. ACM 50(11): 60–64.

Oh W, Jeon S (2007) Membership herding and network stability in the open-source community: The Ising perspective. Management Sci. 53(7):1086–1101.

O’Mahony S (2003) Guarding the commons: How community managed software projects protect their work. Res. Policy 32(7):1179–1198.

O’Mahony S, Ferraro F (2007) The emergence of governance in an open source community. Acad. Management J. 50(5):1079–1106.

Organ DW, Konovsky M (1989) Cognitive versus affective determinants of organizational citizenship behavior. J. Appl. Psych. 74(1):157–164.

Pollard WE, Mitchell TR (1972) Decision theory analysis of social power. Psych. Bull. 78(6):433–446.

Qin X, Salter-Townshend M, Cunningham P (2014) Exploring the relationship between membership turnover and productivity in online communities. Proc. 8th Internat. AAAI Conf. Weblogs Soc. Media 4ICWSM 20145 (AAAI Press, Menlo Park, CA).

Ransbotham S, Kane GC (2011) Membership turnover and collaboration success in online communities: Explaining rises. MIS Quart. 35(3):613–627.

Ren Y, Harper FM, Drenner S, Terveen L, Kiesler S, Riedl J, Kraut RE (2012) Building member attachment in online communities: Applying theories of group identity and interpersonal bonds. MIS Quart. 36(3):841–864.

Salganik MJ, Watts DJ (2009) Web-based experiments for the study of collective social dynamics in cultural markets. Topics Cognitive Sci. 1(3):439–468.

Seeman MA (1957) A comparison of general and specific leader behavior descriptions. Stogdill RM, Coons AE, eds. Leader Behavior: Its Description and Measurement (Ohio State University, Columbus, OH), 86–102.

Seers A, Petty MM, Cashman JF (1995) Team-member exchange under team and traditional management. Group Organ. Management 20(1):18–38.

Shamir B, Howell JM (1999) Organizational and contextual influences on the emergence and effectiveness of charismatic leadership. Leadership Quart. 10(2):257–284.

Sherony KM, Green SG (2002) Coworker exchange: Relationships between coworkers, leader-member exchange, and work attitudes. J. Appl. Psych. 87(3):542–548.

Shirky C (2008) Here Comes Everybody: The Power of Organizing Without Organizations (Penguin Press, New York).

Sias PM, Jablin FM (1995) Differential superior-subordinate relations, perceptions of fairness, and coworker communication. Human Comm. Res. 22(1):5–38.

Singh PV, Tan Y, Youn N (2011) A hidden Markov model of developer learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Sparrowe RT, Liden RC (2005) Two routes to influence: Integrating leader-member exchange and social network perspectives. Admin. Sci. Quart. 50(4):505–535.

Sproull L, Arriaga M (2007) Online communities. Bidgoli H, ed. Handbook of Computer Networks: Distributed Networks, Network Planning, Control, Management, and New Trends and Applications, Vol. 3 (John Wiley & Sons, Hoboken, NJ), 898–914.

Stewart KJ, Ammeter AP, Maruping LM (2006) Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Inform. Systems Res. 17(2):126–144.

Tal Z, Babad E (1989) The “teacher’s pet” phenomenon as viewed by Israeli teachers and students. Elementary School J. 90(1): 97–108.

Townsend J, Phillips JS, Elkins TJ (2000) Employee retaliation: The neglected consequence of poor leader-member exchange relations. J. Occupational Health Psych. 5(4):457–463.

Tyler TR (1989) The psychology of procedural justice: A test of the group-value model. J. Personality Soc. Psych. 57(5):830–838.

van Breukelen W, Konst D, van der Vlist R (2002) Effects of LMX and differential treatment on work unit commitment. Psych. Reports 91(1):220–230.

Vaughan-Nichols SJ (2005) Commercializing open-source stirs debate. eWeek (August 4), http://www.eweek.com/c/a/Linux -and-Open-Source/Commercializing-OpenSource-Stirs-Debate.

von Hippel E, von Krogh G (2003) Open source software and the “private-collective” innovation model: Issues for organization science. Organ. Sci. 14(2):209–223.

von Krogh G, Spaeth S, Lakhani KR (2003) Community, joining, and specialization in open source software innovation: A case study. Res. Policy 32(7):1217–1241.

Wagner C (2004) Wiki: A technology for conversational knowledge management and group collaboration. Comm. Assoc. Inform. Systems 13(1):265–289.

Waldman DA, Yammarino FJ (1999) CEO charismatic leadership: Levels-of-management and levels-of-analysis effects. Acad. Management Rev. 24(2):266–285.

Waldman DA, Ramirez G, House R, Puranam P (2001) Does leadership matter? CEO leadership attributes and profitability under conditions of perceived environmental uncertainty. Acad. Management J. 44(1):134–143.

Walsh JP, Kucker S, Maloney NG, Gabbay S (2000) Connecting minds: Computer-mediated communication and scientific work. J. Amer. Soc. Inform. Sci. 51(14):1295–1305.

Watts D, Dodds P (2007) Influentials, networks, and public opinion formation. J. Consumer Res. 34(4):441–458.

Weber S (2004) The Success of Open Source (Harvard University Press, Cambridge, MA).

Xu B, Jones D, Shao B (2009) Volunteers’ involvement in online community based software development. Inform. Management 46(3):151–158.

Yu CP, Chu TH (2007) Exploring knowledge contribution from an OCB perspective. Inform. Management 44(3):321–331.

Yukl GA (2006) Leadership in Organizations (Pearson/Prentice Hall, Upper Saddle River, NJ).

Zhang C, Hahn J, De P (2013) Continued participation in online innovation communities: Does community response matter equally for everyone? Inform. Systems Res. 24(4):1112–1130.

Zhu H, Kraut RE, Kittur A (2013) Effectiveness of shared leadership in Wikipedia. Human Factors: J. Human Factors Ergonomics Soc. 55(6):1021–1043.

Zhu H, Kraut RE, Wang Y-C, Kittur A (2011) Identifying shared leadership in Wikipedia. Proc. ACM Conf. Human Factors Comput. Systems (ACM, New York), 3431–3434.
