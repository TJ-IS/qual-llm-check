---
otero_id: 16765
otero_key: "PPQDH5UZ"
title: "Coordination in a Digital Platform Organization"
authors: "Carmen Leong; Silvia Lin; Felix Tan; Jie Yu"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1226"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Coordination in a Digital Platform Organization

## Author:

Leong, Carmen; Lin, Silvia; Tan, Felix; Yu, Jie

## Publication details:

Information Systems Research v. 0: Ahead of Print Chapter No. 1 1047-7047 (ISSN); 1526-5536 (ISSN)

## Publication Date:

2023-08-10

Publisher DOI: https://doi.org/10.1287/isre.2023.1226

## License:

https://creativecommons.org/licenses/by/4.0/ Link to license to see what you are allowed to do with this resource.

Downloaded from http://hdl.handle.net/1959.4/unsworks\_84792 in https:// unsworks.unsw.edu.au on 2026-07-11

This article was downloaded by: [2403:5806:a617:0:d19e:71b3:a7f3:3569] On: 27 October 2023, At: 21:50 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/PPQDH5UZ/fulltext/images/c8d536378a61650cb2fa1512ae70e70fe162d7d17f191c24b624438938ae6f84.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Coordination in a Digital Platform Organization

Carmen Leong, Silvia Lin, Felix Tan, Jie Yu

To cite this article: Carmen Leong, Silvia Lin, Felix Tan, Jie Yu (2023) Coordination in a Digital Platform Organization. Information Systems Research

Published online in Articles in Advance 10 Aug 2023

. https://doi.org/10.1287/isre.2023.1226

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2023 The Author(s)

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individua professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Coordination in a Digital Platform Organization

Carmen Leong,<sup>a</sup> Silvia Lin,<sup>b</sup> Felix Tan,<sup>a</sup> Jie Yu<sup>c,</sup>\*

<sup>a</sup> UNSW Business School, University of New South Wales, UNSW Kensington Sydney, New South Wales 2052, Australia; <sup>b</sup> PwC Australia UNSW Kensington Sydney, New South Wales 2052, Australia; <sup>c</sup> University of Nottingham Ningbo China, Ningbo 315200, China \*Corresponding author

Contact: carmen.leong@unsw.edu.au, https://orcid.org/0000-0002-4201-1512 (CL); silviasylin@gmail.com (SL); f.tan@unsw.edu.au, https://orcid.org/0000-0003-2319-5421 (FT); jie.yu@nottingham.edu.cn, https://orcid.org/0000-0002-4119-2163 (JY)

Received: July 12, 2019 Revised: July 2, 2020; September 29, 2021; September 7, 2022 Accepted: March 1, 2023 Published Online in Articles in Advance: August 10, 2023

https://doi.org/10.1287/isre.2023.1226

Copyright: © 2023 The Author(s)

Abstract. A digital platform (DP) generates value by facilitating direct interactions between two or multiple platform sides. While previous studies have expounded upon how platform sides can be coordinated at a collective level (i.e., by pricing strategy and modular architec ture), digital platform owners must not neglect the dynamics within the platform sides and their interactions. Through an in-depth case study of one of the largest e-commerce platforms worldwide, we develop a process model that explains digital platform coordination in terms of the mechanisms that describe the emergence of coordination issues as a result of the enactment of the platform sides’ agency and how these issues can be circumvented. Thi study makes two contributions. First, this study challenges the existing DP literature concerning the assumption of exogenous platform sides, highlighting the agency of the sides as a source of misalignment that must be managed. Second, the model complements the plat form coordination literature focusing on enabling/constraining the actions of sides by conceptualizing a digital orienting mechanism. By adopting a meta-organizational view of digital platforms, this empirical work is among the few studies that report from the inside of a digital platform organization and adopt a processual account.

![](/api/attachments/PPQDH5UZ/fulltext/images/deb32ff96a28839e333b78e71ba07599365c48dff4b752a359908e44673e90c7.jpg)

History: Ola Henfridsson, Senior Editor; Monideepa Tarafdar, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as “Information Systems Research. Copyright © 2023 The Author(s). https://doi.org/10.1287/ isre.2023.1226, used under a Creative Commons Attribution License: https://creativecommons.org/ licenses/by/4.0/."

Keywords: digital platform • platform coordination • meta-organization • agency • digital orienting • platform dynamic • case stud

## 1. Introduction

Digital platforms (DPs) transform the ways that businesses and industries operate by leveraging technologies to facilitate the direct interactions of two or more economic actors or sides (Gawer 2021). For instance, YouTube connects advertisers with viewers, Apple links developers with users, and Amazon matches sellers and buyers. Because DPs’ very existence is underpinned by value propositions that can only be achieved through the coordinated actions of the participating sides, it is a foremost challenge to understand platform coordination and how platform owners manage the dependencies among the platform sides such that they work together harmoniously (Tiwana 2015, Kretschmer et al. 2022). Platform coordination is critical at the initial stage of DP to ensure participating sides share an overarching goal and know their specific tasks, activities, and interdependencies (Van Alstyne et al. 2016). Platform coordination is equally vital as the platform matures since the coordination costs for platform owners and sides can change over time (resulting in participants deserting a DP for another) (Tiwana 2015), and the configuration of a DP can shift (precipitating changes in the number of sides and/or the interdependencies among sides) (Gawer 2014, Gawer 2021). In their recent moves to expand their scope of services, DPs, such as Instagram and TikTok, have changed their configurations to integrate merchants into their networks of content creators and consumers, and Xbed, an Airbnb-like app, has invited parttime housekeepers to connect with its hosts and customers. Such strategic moves reiterate challenges for platform owners to coordinate platform sides so that they are “brought into an alignment, consid ered and made to act together” (Thompson 2003, p. 13).

In fact, platform coordination is uniquely challenging because it involves the coordination of interdependent but legally autonomous participating sides; in contrast to managing employees in a traditional hierarchical organization, subsidiaries in a business group, or partners in a supply chain of actors bounded to a focal firm by legal employment, ownership structure or contractual relationships, DP owners do not possess any formal authority over the platform sides. The challenge in platform coordination is amplified by the malleability of digital platforms and their highly competitive landscape (Tiwana et al. 2010). DP owners frequently add new products and services and change roles and interactions and/or connect new sides (Li et al. 2022). These competitive moves may change the platform sides interdependencies, causing a shift in the preexisting alignment among the platform sides. For example, when LinkedIn attempted to add corporate users as a new side to grow its platform connecting individual professionals, recruiters and advertisers, it risked causing a conflict of interest as some individual users did not welcome the presence of corporate users who are their employers (Hagiu 2014). Similarly, private drivers on ride-hailing platforms, such as GoJEK Singapore and Uber (New York), raised concerns regarding increased competition when the two platforms decided to partner with local taxi drivers. In Alibaba’s Taobao e-commerce platform, the addition of influencers as a new side further triggered changes in the roles of the existing sides. Because (re)alignment does not occur on its own (Helfat and Raubitschek 2018), DP owners must manage these shifts such that the sides are continuously returned into an alignment (Thompson 2003).

Importantly, these platform coordination challenges underscore the dynamics among the platform sides (Leong et al. 2019b, Tschang 2021). In addition to the changes in the platform configuration, these dynamics arise from the inherent differences among the platform sides in their organizational attributes, including preferences, routines, positions/roles, activity flow, and schemata (Adner 2017, Qiu et al. 2017, Malgonde et al. 2020, Sandberg et al. 2020), which can affect how well they interact and work together. Similarly, insights from ecosystem studies note the heterogeneity in the platform sides and its implications by highlighting the challenges confronting a new side when adapting to the operational requirements and norms dictated by the platform owner and older members (Wareham et al. 2014, Lindgren et al. 2015). Therefore, we argue that when coordinating platform sides, platform owners must not ignore the existence of agency in the sides as the sides exhibit behavioral characteristics, can make independent decisions, and their actions are acknowledged as having an influence over the DP owner and the other sides (de Reuver et al. 2018, Helfat and Raubitschek 2018, Sandberg et al. 2020). As competition between DPs persists, it is expected that agency in the platform sides will only become more relevant; more DPs grow from two-sided to multisided platforms for the purpose of enhancing service offerings and since there are more alternative DPs available in the market, the platform sides will enjoy more freedom to exert their own will and make their own choices.

However, surprisingly, there is a paucity of research seeking to advance our knowledge regarding platform coordination beyond the manipulations of DPs’ overall structural design. The two platform coordination mechanisms widely studied, that is, pricing mechanisms and the provision of a modular architecture, rarely, if at all, contribute to these dynamics among platform sides (Gawer 2014). A prevalent market mechanism, the pricing mechanism focuses on the determination of pricing to sub sidize one side to attract the participation of the other side, thereby triggering the self-reinforcing network effect critical for launching a DP (Rochet and Tirole 2003). The other mechanism—the modular architecture—emphasizes the provision of a technologically enabled modular structure such that the participating sides can contribute according to the embodied division of labor, thus reducing the coordination costs incurred by the DP owner (Baldwin and Woodard 2009). By focusing on the overarching structural arrangement of the interdependencies manifested in the matching links of supply and demand and platform architectural design at an aggregate level, these mechanisms do not consider agency in the platform sides and how agency plays a role in the microlevel of DP coordination actions.

Moreover, the mechanisms are underpinned (respec tively) by two DP conceptualizations—one views platforms as markets, and the other views platforms as technological architectures—that implicitly assumes platform sides being homogenous and exogenous to DPs (Gawer 2014). Because the two conceptualizations treat complementarity among the sides as unchanging and the platform as a structurally stable architecture, we argue that they could inadvertently portray a deterministic view of platform coordination, such that if a structure is in place to enable or constrain certain actions, the platform sides will act accordingly (Cardinale 2018). This view can risk undermining both research and practice. Regarding research, such existent platform coordination knowledge may perpetuate a static view of platforms and platform coordination; prior studies offer powerful explanations of DP design but largely do not address the issues of platform evolution, including changes in platform configurations (Gawer 2014). Regarding practice, focusing only on the overall platform design and structure may result in an arbitrary approach to platform coordination, prompting DP owners to pay attention to only their overarching platform design (pricing and architecture) and lose sight of the reactions of the platform sides, who can choose not to act in accordance with the structures.

Therefore, it is necessary to advance our knowledge of platform coordination by expanding the analysis of platform coordination to include platform sides and consider the influence of the platform sides’ agency while investigating the process of how a DP owner manages the dependencies among the sides. This study asks the question, “How can digital platform sides be coordinated?” Through an in-depth case study of Alibaba’s Taobao, we develop a process model that explains digital platform coordination in terms of the contextual conditions (when platform sides could enact their agency), the mechanisms of the platform sides’ agency enactment and digital orienting, and the resultant outcome. Our findings, building upon the organizational perspective of DPs (Gawer 2014), highlight the agency of sides as a source of misalignment in platform coordination and shed light on the dynamics of the next level constitutive parts of DPs which is poorly understood. Our study is among the first that shows how a DP owner, in addition to putting in place structures to enable or constrain certain actions of platform sides, must also influence their narrowing of possibilities of action toward achieving coordinated actions. We conceptualize this narrowing of possibilities as digital orienting, which comprises of three distinctive mechanisms—habitating, signaling, and anchoring. Our model is expected to assist executives 1) by sensitizing platform owners to the differences in and preferences of the participating members and 2) by providing an expanded repertoire of actions in coordinating platform sides through technology.

Next, we review the coordination of DPs, metaorganization and fundamental elements related to coordination. We then describe the research method and case, followed by our analysis. Finally, we conclude by discussing the contributions and limitations of our study.

## 2. Literature Review

## 2.1. Digital Platform Coordination

This paper refers to a DP as an evolving organization that coordinates constitutive agents to create value by generating economies of scope in supply or demand (Gawer 2014). This organizational perspective of digital platforms treats the economic actors held together by the platform owner via the technological architecture as a part of the organization (Gawer and Cusumano 2001). This perspective is distinct from the two commonly applied perspectives. First, by considering the platform sides as internal agents, the organizational perspective is distinct from the economic perspective that interprets platforms as markets and the platform sides as external agents (Rochet and Tirole 2003, Thomas et al. 2014). Second, by conceptualizing DPs as organizations rather than merely technological architecture from an engineering perspective, the organizational perspective enables us to consider the structural characteristics of the DP architecture with an emphasis on the agency (Ulrich 1995, Baldwin and Woodard 2009). In this paper, a digital platform comprises a DP owner or the firm that owns and manages the technological architecture and constitutive agents connected via the technological architecture. Hence, the DP in our study is similar to a platform-based ecosystem due to its incorporation of “external” entities and their mutual dependencies toward contributing to the focal value proposition (Iansiti and Levien 2004, Jacobides et al. 2018). To maintain the structural characteristics of a DP, we refer to the groups of constitutive economic agents as the sides (e.g., Amazon sellers and buyers).

In contrast to traditional organizations, DP owners do not possess formal authority or hierarchical power over the constitutive members (Gulati et al. 2012, Gawer 2014). The platform sides, individuals or firms, maintain their autonomy in the DP (Gawer 2014, Sandberg et al. 2020). One of the key challenges therefore is for platform owners to coordinate the two or more platform sides, for example, the travelers, hosts and experience providers in Airbnb or the buyers, sellers and video content producers in Amazon (Gawer 2009, Trabucchi and Buganza 2020). According to Malone and Crowston (1990), coordination refers to the act of managing the interdependencies between activities so that actors work together harmoniously to achieve a goal. Based on our review, two coordinating mechanisms are identified.

2.1.1. The Two Prevalent Coordinating Mechanisms. One influential coordinating mechanism in platform studies is pricing. Rooted in the industrial organization economics literature, digital platforms are referred to as two/multisided markets that generate value by facilitat ing the direct interactions between two or more groups of actors who could not otherwise connect with each other (Evans 2003, Rochet and Tirole 2008). Underpinned by the theory of network effects, the platform values for any given side depend on the number of users on the same side (direct network effects) or on the network’s other side (indirect network effects) (Eisenmann 2006). Because network effects can trigger a selfreinforcing virtuous cycle, the question of platform coordination becomes “how to bring multiple sides on board” (Evans 2003, Rochet and Tirole 2006). Rochet and Tirole (2003, 2006) and many others have since focused on pricing strategies to adequately incentivize the participation of sides (Caillaud and Jullien 2003; Rochet and Tirole 2003, 2006; Parker and Van Alstyne 2005; Armstrong 2006; Hagiu 2006, 2009; Cabral 2011; Halaburda and Yehezkel 2013). In line with the economics perspective of DPs, the characterization of platform sides is often confined to that of the “money” or “subsidy” sides (Gawer 2021).

The other prevalent coordinating mechanism is the provision of a modular architecture, primarily to facilitate innovation (Baldwin and Clark 2000). Building on the engineering perspective, a DP embodies a modular technological architecture that can be decomposed into components that can be recombined and structured around a core and a periphery (Baldwin and Woodard 2009) and/or in layers (Yoo et al. 2010) such that the components can be modified or replaced without impacting the overall system work and functionality. By partitioning a system into a stable set of components and a set of loosely coupled components interconnected through standard ized interfaces (Parnas 1972), the modular architecture reduces the interdependencies between the components, therefore allowing the participating actors (mostly referring to innovation complementors or app developers) to innovate on different modules in parallel and unencumbered by dependencies (Tiwana et al. 2010, Gawer 2014). Furthermore, the interfaces, including the platform boundary resources that serve at the boundary between the DP owner and the app developer, provide all information required to build the system and show only the information that actors require for their work (Baldwin and Clark 2000, Ghazawneh and Henfridsson 2013). This further supports the division of labor and specialization among actors (Raghu and Arun 1995). In essence, modular architecture reduces the coordination costs of the DP owner and the complementors (Tiwana 2015).

2.1.2. Limitations of Prevalent Coordinating Mechanisms. Notwithstanding their significance, the two coordination mechanisms focus on the overall pricing strategy and technological design at the macro level of a DP, treating the platform sides either as peripheral, passive recipients or as a collective entity. We argue that by relying solely on this coordination, DP owners risk neglecting the dynamics in the internal working of DPs. This can be problematic for several reasons.

First, the provision of enabling macrostructures (e.g., subsidy and modular technological architecture) may fall short in considering the competitive interactions between and among the platform sides. Despite the existence of mutual interests, tensions are inevitable among the sides and can discourage continued participation (Van Alstyne et al. 2016). The abovementioned example of LinkedIn, for instance, highlights the possible frictions among the multilateral sides (Hagiu 2014). When some DPs add new sides to their core network, we should be reminded that coordination frictions can emerge even if they were resolved when the participants first joined the DP (Tiwana 2015). While studies investigating platform governance have generated much guidance for managing the tensions of generativity and control (e.g., Ghazawneh and Henfridsson 2013), the locus of their attention is often between the DP owner and participants overall rather than the more complex web of interactions among the sides. Furthermore, the focus of platform governance<sup>1</sup> is inclined to the control, authority and regulation of coordination rather than on actions that bring different actors or things to work together to achieve predetermined goals (Thompson 2003, Tiwana et al. 2010, Li and Kettinger 2021).

Second, despite the wide application of the two coordination mechanisms, the platform sides’ characterization is confined to that of a “money/subsidy” side (in the pricing mechanism) and an innovation complementor (in the architectural coordinating mechanism), which can ignore the individual side’s nature, roles and choice as the cause of coordination issues (Gawer 2021).

The limitation of this stable characterization of sides is further aggravated as recent DP studies highlighted the heterogeneity in their organizational attributes. In work by Malgonde et al. (2020), DPs are treated as complex adaptive business systems, and the authors argued that the platform sides, such as universities and students on internet-based educational platforms, demonstrate different and evolving objectives, preferences, and constraints. Sandberg et al. (2020) similarly noted the organizational attributes in sides by highlighting that they possess schemata to make sense of new information from the environ ment, and the schemata evolve over time. By examining how iOS app developers juggle between the professional expectation of software engineering and the competitive pressure in the platform market, Qiu et al. (2017) also highlight the logics to which the independent side may adhere. These organizational attributes in platform sides further illuminate the intricacies in coordinating sides.

Third, the existing coordinating mechanisms largely position the platform sides as market actors external to the legal boundary of the DP owner firm and its technological platform, downplaying the agency in the sides. The DP’s economics perspective, which is the basis of the pricing mechanism, treats the sides and their interdependencies as exogenous (Gawer 2014), while the technological coordination mechanism continues such positioning with platform boundary resources being purported to preserve the arm’s length relationship between the DP owner and the sides (Ghazawneh and Henfridsson 2013). In contrast, by examining the role of the constitutive sides in shaping the DP, subsequent research has alluded to the discernible role of conscious agency. These studies acknowledge that platform sides do not merely comply with the DP owner’s action (Karanovic et al. 2020) and demonstrate the influence of their action and responses as the DP evolves (Malgonde et al. 2020, Sandberg et al. 2020, Mo¨hlmann et al. 2021), highlighting that the sides “can engage in autonomous decision making and action” (Sandberg et al. 2020, p. 131). Qiu et al. (2017) further enhance our knowledge of the embedded agency of platform sides by showing how app developers can operate in a pluralistic environ ment, which can trigger different logic within the sides and, therefore, lead to idiosyncratic behaviors. In this respect, the current coordinating mechanisms may appear myopic and incomplete, as they make little, if any, space for the sides to exercise their agency (Tiwana 2015).

In summary, our review presents the platform coordination limitations that have accorded insufficient attention to the dynamics within a DP organization. Although the actors and their interactions are integral elements of a DP, few studies have considered these dynamics possibly because of the risk of “drowning in the almost infinite web of interdependences” (Adner 2017, p. 55) or because of pragmatic reasons (rather than conscious neglect), such as data collection costs (Azor´ın and Francisco 2014).

However, the importance of ensuring that actors work harmoniously together is reinforced as more DPs pursue strategic expansion by integrating additional sides (Leong et al. 2019b, Gawer 2021). To better consider platform sides in examining platform coordination, a metaorganizational lens may be useful for two reasons. First, in line with the organizational perspective of DPs, the MO perspective conceptually includes the platform sides as part of a DP organization and reintroduces agency in the concept of a DP (Gawer 2014). It enables not only an empirical observation of entities that were previously treated as exogenous to DPs but also an explicit account of the influence and heterogeneity of the platform sides. With an emphasis on platform sides and their agency, an MO perspective allows us to examine their interactions, where frictions emerge (Tilson et al. 2010). Second, by formalizing the DP as an organization with constitutive parts, the MO concept allows us to shift our focus from the macro factors and collective behaviors of a DP to the microfoundation of a DP. This, in turn, enables us to draw on the basic problem of organizing (Puranam et al. 2014) and Emirbayer and Mische’s (1998) agency to formulate our analysis framework for a deeper examination of platform coordination. Accordingly, this paper aims to address the question, “How can digital platform sides be coordinated?” In the following, we provide the details of the meta-organization.

## 2.2. Meta-Organization: Problem of Coordinating and Agency

A meta-organization, also known as an organization of organizations, is defined as “an organization whose agents are themselves legally autonomous and not linked through employment relationships” (Gulati et al. 2012, p. 573). A meta-organization is a relatively new form of organization that emerged in the mid-2000 s with an increasing number of firms collaborating with external partners, including individuals or firms, due to the unique resources they possessed to achieve an objective that was otherwise not possible (Berkowitz and Dumez 2016). An MO is distinct from a traditional hierarchical organization because the formal authority that characterized the latter is absent in the relationship between the members and the MO architect, that is, the central actor who shapes the design of the MO to provide a regulated and coordinated space for the members (Berkowitz and Bor 2018). Therefore, an MO architect cannot control the other members as a traditional organization controls its employees through contractually specified employment relationships. Similarly, Gulati et al. (2012) argue that neither business groups nor multinational firms are MO because the central actors, that is, headquarters, possess and exercise formal authority over the subsidiaries or units through their controlling ownership stakes. An MO is also distinct from traditional markets with the existence of a central actor who actively shapes the MO design (Gulati et al. 2012) and agents who are more closely coupled (Kretschmer et al. 2022). Notably, in contrast to the theory of interorganizational networks, the notion of an MO treats constitutive agents, that is, the participating sides who are legally external, as an organization (Gawer 2014). To coordinate members who possess their own motivations, incentives, and cognitions (Gulati et al. 2012), the MO architect often promotes a system-level goal that is attainable only by the collective actions of the MO agents (Marciniak 2013).

By incorporating the member sides in the conceptualization of a DP, the notion of a meta-organization allows our analysis of coordination to go beyond the primacy on the macro, collective level of a DP to the next level’s con stitutive parts that make up the DP: the platform sides and their interactions (Gulati et al. 2012, Barney and Felin 2013). To conduct a systematic analysis of coordination in a digital platform, we draw upon the basic problem of organizing for two reasons (Puranam et al. 2014). First, studies have proposed using this work to analyze digital platforms as organizations (Gulati et al. 2012, Staykova 2018), which is consistent with the organizational view of DPs we adopt in this study. Second, the purpose of organizing in Puranam’s work concerns the achievement of coordinated action across diverse organization members, and the two problems proposed (i.e., division of labo and integration of efforts) resonate with the coordinating mechanisms of digital platforms as presented below.

The first problem is the division of labor, which refers to “the breakdown of the organization’s goals into contributory tasks [task division] and the allocation of these tasks to individual members within the organization [task allocation]” (Puranam et al. 2014, p. 165, bracket added). In typical business firms, task division in line with organizational goals, and the common mechanisms of task allocation involve the designation of formal roles and the recruitment of individuals into them (Puranam et al. 2014). Similarly, MO and DP studies argue for the division of tasks in alignment with systemlevel goals that benefit all members and further contend that the tasks can be specific or relatively broad and abstract to accommodate the members’ individual strategies (Gulati et al. 2012). Specific to DPs, task division is arguably embedded in the design of the modular architecture, which allows members to work on a particular task without worrying about other aspects, such as the integration with others’ work later (Baldwin and Woodard 2009, Yoo et al. 2010). In comparison, task allocation in an MO is much more distinct from that in a traditional organization because the members who could move in and out of the permeable boundary of an MO self-select into tasks predefined by the architect (Gulati et al. 2012). Thus, to ensure a meta-alignment given the diverse member contributions, DP researchers have highlighted the control of DP owners to review, filter, and approve the members’ contributions (Eaton et al. 2015). While DP studies take for granted that this coordinating task is assumed by the DP owner, the MO literature suggests that participating members (usually those with better performance) can be assigned to “supervise” lower-tier members (Gulati et al. 2012).

The second problem is the integration of efforts, which represents issues in persuading members to cooperate and coordinate in a way that would “maximize the value of the system as a whole, for a given division of labor” (Puranam and Raveendran 2013, p. 5). This problem is often approached from two aspects: 1) reward provision (from rewards to agents) to motivate members to cooperate by taking costly actions toward executing tasks they are responsible for and 2) information provision (from information to agents) to ensure that agents have enough information to coordinate their actions with others (Puranam et al. 2014). The above-mentioned pricing mechanism in digital platform is a form of reward, albeit one that focuses on the broader level of platform actions (Rochet and Tirole 2003, Parker and Van Alstyne 2005). In addition, the MO literature suggests that tiering can serve as another form of motivation because the benefits associated with higher tiers can create incentives for members to contribute to the collective (Gulati et al. 2012). For example, registered Wikipedia users who are at least 30 days old and have made at least 500 edits can access a content translation tool, in addition to having the ability to create a page. Comparatively, information provision receives less explicit attention in a DP, possibly because it is subsumed in the DP’s modular architecture that fundamentally allows each actor to act independently without having to explicitly coordinate their actions. With technology modularity and the information subsumed notably in boundary resources (such as Apple’s software development kit, the App Approval Process and the rules in the developer license agreement), it is presumed that if each member undertakes their tasks, their actions will in aggregate be coordinated toward the system-level goal (Ghazawneh and Henfridsson 2013, Eaton et al. 2015).

The meta-organizational view of digital platforms further allows us to understand the dynamics of the constitutive agents of an MO (Emirbayer and Mische 1998) by leveraging the organizations-as-institutions perspective (Zucker 1983). MOs reintroduce agency in DPs (Gawer 2014), sensitizing us to the agency in the platform sides as they possess a temporally embedded capacity to act with intent (Emirbayer and Mische 1998). Although most DP studies have given a privileged position to the agency of DP owners, our review identifies the agency of the sides who “draw from the past (habit, prior experiences, interpretive schemes), the present (situation-at-hand, resources and artifacts available), and the future (projections, expectations, norms that inform ongoing practice) to inform their current practice” (Howard-Grenville 2005, p. 267). For example, studies have highlighted that the participation of a firm in a platform ecosystem can be problematic if the firm continues to rely on and refer to past models and its previous identity, routines and procedures (Lindgren et al. 2015). Similarly, platform sides may constantly face situations that require them to evaluate the various alternatives, such as to choose control/standards or generativity/freedom (Ghazawneh and Henfridsson 2013), to supplement or to oppose a new form of organizing (Karanovic et al. 2020), and to sustain participation or to leave a DP (Tiwana 2015). Last, studies also pointed to the future-oriented engagement of platform sides who, aside from a platform member, also act as entrepreneurial venture leaders to ensure the long-term growth and survival of their venture independent of the success of the host platform (Nambisan and Baron 2021). We argue that agency in sides can lead to heterogeneous actions, and some of these actions may deviate from the expectations of the DP owner. Platform coordination must be understood not as a matter of creation by the DP owner and compliance by many independent sides but rather by how it is shaped by the temporally constructed engagement of the platform sides.

In summary, by adopting a meta-organizational lens, we identify the analytical categories of coordinating issues (Puranam et al. 2014) and the disaggregation of agency by temporal dimensions (Emirbayer and Mische 1998), which may allow us to examine the dynamics of DPs without being overwhelmed by their complexities.

## 3. Methodology

This study examines the following important challenge for DP owners: the coordination of platform sides. As DP organization dynamics under the coordination of sides are yet well understood, as previously established, a case study methodology is particularly appropriate (Siggelkow 2007). In particular, we adopt a qualitative approach and predominantly an interpretive stance (Klein and Myers 1999). A case study is a proviso for our capacity to examine different strategies that uncover the DP dynamics under the coordination of sides. To explore how the platform organization unfolds, we examine a change event. A platform firm often adds new sides with distinct organizational attributes such that this changes the organization and the configurations with new interdependencies that require coordination. This study examines Alibaba’s Taobao, which provides privileged inside data as it reports from inside the platform. Taobao presents an exemplary case in which a new side—the influencer—is added to a DP that already connects multiple sides. The integration of a new side has contributed to the performance of the DP firm as a part of the platform expansion strategy. By the end of 2019, there were reportedly more than 1.6 million influencers on Taobao, generating over 6.5 million RMB (USD 918,000) daily. Despite Taobao’s status as a large DP and our inability to rule out the established user base as a contributing factor to its expansion, our initial contact with the gatekeeper (the manager of the Mobile Taobao Team) informed us that this does not preclude the firm from facing challenges in adding a new side.

## 3.1. Data Gathering and Analysis

Our focus on a DP organization requires an appreciation that organizations are socially constructed; thus, we rely on people as informants or knowledgeable agents of organizational realities (Langley 1999, Gioia et al. 2013). Our study involved semistructured interviews with informants from the organization to obtain both retrospective and real-time accounts of their experience with platform coordination. We visited Taobao headquarters in Hangzhou and conducted 21 face-to-face interviews with Taobao executives and representatives from multiple sides in the preexisting network (i.e., merchants, buyers, marketers) and the new side (i.e., influencers). Later, we conducted further interviews with eight influencers and buyers via phone calls, emails, and instant messaging to obtain data that complemented and corroborated our previous interpretation of the events. The interviewees were selected based on a purposeful sampling strategy in consultation with the gatekeeper who led the firm’s initiatives to engage influencers as a new side. Three criteria were applied in evaluating the informants’ suitability: (1) candidates from the DP who were actively involved throughout the addition of the new side and/or were aware of the internal workings of the platform; (2) candidates from the different preexisting sides who had direct engagement with the new side, for example, merchants and buyers who used the services of an influencer; and (3) candidates from the new sides who had different levels of experience and income. Appendix A provides the list of interviewees and their relationships. The interviews generated approximately 30 hours of recordings and over 100 pages of transcripts. We also conducted follow-up interviews when clarification of the transcribed documents was required. According to the designed flexibility of interpretive research, we recognize that the initial interview guide (Appendix B) would be adjusted with the progression of the research (Gioia et al. 2013).

The data collection and data analyses proceeded concurrently such that they were coincidental with preliminary interviews. The voluminous amount of qualitative data were first condensed into a manageable form via narrative and visual mapping strategies (Langley 1999, Gioia et al. 2013). The narrative strategy entailed constructing a “story” that represented an account of what had happened. The visual mapping strategy involved creating chronological event timelines and documenting emergent theoretical ideas in a series of diagrammatic sketches (e.g., Leong et al. 2019a). In Appendix C, we present the timeline of historical events that could provide context to the data and analysis. For instance, by tracing the launch and development of other platforms, the timeline illustrates the intense competition that Taobao faced in acquiring and retaining its influencers (details are provided in Section 4.1), which form the basis for the contextual conditions we identified in the final model. The timeline also depicts the coordination efforts by Taobao related to the integration of efforts, division of labor and emergent value align ment which are further elaborated in Section 4.2.1.

In the first-order analysis, we revealed the codes and categories that emerged early in the research and tended to adhere faithfully to the informants’ terms. We sought to discover patterns and develop further mappings of the coded responses by sifting through the empirical interview data, theoretical perspectives, and relevant literature. As the research progressed, we labelled similarities and differences among the categories, revealing emergent themes that describe and explain our phenomena. During this second-order analysis, we elicited nascent concepts that did not have theoretical referents while relating others to the existing ones. We continued to distill emer gent second-order themes into aggregate dimensions during this theme and concept development process toward theoretical saturation (Glaser and Strauss 1967). From this process, we built a data structure that provided a representation of how we configured our raw data to themes. Throughout the process, we cycled between the emergent data, concepts, themes, dimensions, and relevant literature to reveal new concepts and/or precedents. Therefore, we sought to adhere to the rigor of a qualitative study while still retaining the revelatory potential for an informed theory concerning the platform’s coordination of its sides (Tracy 2010, Gioia et al. 2013).

When confronted with data that challenged or did not fit easily into existing themes or dimensions, the coding scheme would be modified accordingly (i.e., add a new or modify/delete an existing, second-order theme or aggregate dimension; see Strauss and Corbin (1998)), and coding would be restarted. By recursively iterating between and comparing theory and data, the process model was inductively derived and gradually shaped. Among the researchers and key informants, we revisited the data, engaged in mutual discussions, and developed understandings for arriving at consensual interpretations. This process continued until the state of theoretical saturation was reached (Glaser and Strauss 1967), which refers to the state where the inductively derived model can comprehensively account for the case data and incremental learning is minimal, as we are observing phenomena seen before.

## 4. Changes in Taobao’s Digital Platform 4.1. Context

Taobao was founded by the Alibaba Group in 2003 to allow direct interactions and transactions between sellers and buyers on its e-commerce platform. It provides B2C and C2C retailing services for consumers worldwide. Recognizing that there is a limit to how much differentiation can be achieved with strategies that are product-centric (e.g., pricing) and transactionoriented, since 2013, Taobao has prioritized the provision of value-added content that enhances the “interactive community experience” (Alibaba 2015). Within Alibaba’s broader platform strategy described by Group CEO Daniel Zhang as “the leap into the second half of e-commerce,” Taobao encouraged customer-focused content from bloggers and other online personalities through various initiatives, including a social media feed, an embedded live streaming platform, and a marketplace for merchants to transact with content. Most importantly, these initiatives have all propelled the need to grow a new side—the influencer, who is better known as Da Ren (达 人 ) within Taobao, as a driving force of web traffic and sales (Sun et al. 2020). Appendix A describes the roles of the key sides.

These influencers play roles similar to those of socia media influencers; with their opinions and recommendation of products/services, they create content for distribution to a larger crowd to generate consumer trust and to earn a commission or referral fees through affiliate marketing (Duffy 2005). For the calculation of fees earned, a link to the shops or products will usually be provided for the influencers, including those on Amazon Associates or eBay affiliates programs, to share on their social media accounts on Facebook, Instagram, and/or YouTube. Taobao Da Rens adopt a similar method of income generation but differ from influencers on other platforms as their account, contents, followers, and backend features, such as analytic reports, are maintained within Taobao’s platform rather than on other social media platforms. As Taobao evolved to integrate the Da Rens as a new side to the DP, further differentiations were made: Da Rens were able to search for opportunities to work with merchants within the Taobao platform and to develop cooperative relationships with marketers who later helped to manage the influencers’ accounts. Taobao’s heavy investment in Da Rens as an additional side highlights its recognition of their value in providing unique forms of content that allow Taobao to continue its growth as a DP leader. As of 2017, there were over 1.6 million content creators, including Da Rens and the agencies for whom they work, and between them, they shared \$3 billion RMB in commissions in 2017.

However, this platform growth strategy is not without its challenges. The addition of a new side has instigated changes in the interdependencies among the existing sides; for instance, merchants who previously searched for an influencer on a social network platform could build direct interactions with them on Taobao. Marketers who previously provided marketing solutions to Taobao merchants, due to an overlap of roles with the new side, must evolve to redefine their role and, hence, their interactions with merchants and influencers within the platform. In other words, Taobao’s platform side configuration has changed, manifested not only in the number of sides but also in the interactions. This is unlike other cases, such as the Uber situation in which it preserved the interactions of riders and drivers as it added the restaurant (the new side) by establishing an app separated from Uber.

As a result of these configurational changes in Taobao, the platform sides experienced a misalignment and underwent a period during which they must experiment with interactions with new sides and changes in their preexistent roles. As one Da Ren described, mar keters had to adopt a new role that was unfamiliar to most of them (and hence, she did not learn much from working with marketers). As we illustrate later, the mer chants were also unsure of what makes good content. Given that content exchange greatly differs from productcentric e-commerce, Taobao experimented with severa new platform designs and features with the aim of helping the sides adapt. Furthermore, the intense competition among influencers on several large digital platforms, including social e-commerce (e.g., Weibo and Xiaohong shu), video sharing (e.g., TikTok), fashion content sharing (e.g., Mogu), and other e-commerce platforms (e.g., JD. com), presented a challenge (this is presented as the competitive actions in Appendix C). Because it was very common for influencers to have a presence on more than one platform, Taobao must compete with other DPs for these influencers. While competing for these influencers, Taobao also faced a volatile environment due to the rapid upsurge of such user-generated content, which also attracted growing regulatory concerns (refer to Appendix C for some significant regulatory changes). The ease of broadcasting content directly to the masses through med iums, such as livestreaming platforms, has increased the volume of content related to gambling, violence, and pornography, which the Chinese government deems a hazardous influence that may cause social and political instability. DP owners must ensure high compliance with fast-evolving regulatory changes.

## 4.2. Coordinating Platform Sides

Next, we present the issues that emerge when a new side is added and the corresponding actions adopted by Taobao. In the first subsection, we describe three instances of coordination identified as we leverage the two coordination problems by Puranam as the categories of analysis (in Appendix D.1, we provide the data structure for the three coordination instances). In each instance, we explain how the issues emerged (from the agency in sides) and how they were overcome. Therefore, this leads to the structure of the second subsection, where we provide an analysis of the two mechanisms, that is, the enactment of a platform side’s agency and digital orienting.

## 4.2.1. Instances of DP Coordination.

4.2.1.1. Coordinating for the Integration of Efforts. Since 2013, Taobao has been enhancing its DP with features that allow the creation and dissemination of content for product marketing and promotion. Taobao introduced its built-in social commerce platform Weitao in 2013, and in 2015, it launched Taobao Headlines, a fashion and shopping news aggregation. In 2016, the Taobao Live feature was integrated into its e-commerce platform, enabling consumers watching live streaming to add items to their cart and check out in one seamless transaction—without ever leaving the Taobao platform. These initiatives underlined the emergence of the Da Rens. To facilitate the direct connections between merchants and Da Rens, Taobao later launched a content commerce platform, Vtask. The Da Rens could not only engage with buyers on the DP but also seek opportunities to sell their content to merchants with a demand. This in turn introduced influencers formally as a new side who directly interact with a few actors within Taobao.

The Taobao team was confronted with various challenges that prevented the Da Rens and merchants from working jointly. Despite the initial subsidies provided by Taobao, most Da Rens have not behaved in a way that Taobao anticipated. An example was demonstrated by the brevity in the Da Rens’ self-provided information on their profile page, shown to the research team during data collection. Compared with the merchant’s page with a detailed illustration of the seller and products, the Da Rens’ pages were extremely brief, some with only a few lines of text, causing difficulties for merchants in assessing the Da Rens’ quality. At least two reasons related to the Da Rens’ past habits and orientation have contributed to inefficient communication. The first was the lack of a customer service mindset among the Da Rens, and the second reason was the Da Rens unfamiliarity with the DP. The high demand for Da Rens’ services provided limited choices for merchants; more than half of the transactions were communicated offline, and the two parties simply used the platform for the sake of completing the payment. Although the Da Rens’ pages applied an interface similar to that of the merchants (the type of information required and its layout), unlike the merchants who already had years of experience on the DP, most Da Rens failed to provide the information in a way that Taobao or the merchants expected. The Mobile Taobao Team manager explained as follows:

“To be honest, the operating ability of our merchants is so much better than Da Ren on our platform. Because these merchants have been “trained” about how to use our platform for ten, twenty years, they can quickly get used to every new tool and even know how to improve it further.

However, Da Ren is not able to do this for now. At the storefront of merchants, everything in our front-end has a detailed and attractive description. Most Da Rens just put a single sentence to describe themselves, like we just saw. They don’t exactly know what they should write … These Da Rens also do not realize the importance of a customer service mindset … They would think that everything comes to an end once you paid them.”

Simultaneously, the coordination between the Da Rens and merchants was made difficult by the inherent differences in their profession and identity. Although they could find a Da Ren more easily with Vtask, the merchants faced the challenge of assessing the perfor mance and, hence, suitability of a Da Ren. In contrast to the standard goods or services prevalently transacted on Taobao (e.g., apparel and electronic goods), Da Rengenerated content and their performance were novel to the DP and, hence, could not be assessed because of a lack of appropriate measures for individual influences and product creativity. The Vtask Platform Development Team and MCN3 illustrated the struggles facing the merchants and Da Rens, respectively:

“The biggest problem was few merchants engaged at the beginning because they had no idea about the outcome. The Da Ren would quote and charge, while their service may be a black box for merchants, as it’s hard to predict the actual value. The measurement is a problem for both parties.” [Vtask Platform Development Team]

“Taobao is a transaction platform, not a content platform. We [as Da Rens] struggle a lot as we produce contents on this platform. On the one hand, we would like to produce creative content that interests and engage my viewers; on the other hand, my client [the merchants] has an explicit expectation for their investments. They expect the contents to gen erate conversions and sales, and we need to balance that.” [MCN 3]

To alleviate these unexpected behaviors on the new side, Taobao invested much in the development and continuous refinement of its algorithmic rating and ranking. As with most DPs, Taobao served as a middleman that helped merchants by measuring and presenting information on the performance of Da Rens, and one of the most important indicators would be the translation into actual sales. This outcome-based measure ment, although critical, was insufficient to shape the Da Rens’ behaviors on the DP. Therefore, Taobao developed an algorithm to measure different performance aspects of Da Rens, assigning them one of four performance ranks. Subsequently, the algorithm was further refined to rank Da Rens in 7 tiers (L0-L6) based on their “1) commercialization ability, which measures how well thei content can translate into an actual purchase and their servic level, 2) vertical domain attribute, which measures expertis and focus of Da Rens in their domain, and 3) reflective value, which consists of the size of followers, the ability to attract new fans, the ability to keep their fans engaged, these fans activity level,” the Mobile Taobao Team manager explained. Figure 1 depicts the analytical and review tools used by merchants to assess the capabilities of the Da Rens in a transparent way. The control of their behaviors was resonated by the Da Rens as follows:

“If you violate the rules, such as speaking vulgar words, your livestream will be terminated immediately … Each of your livestreaming sessions, including the length, are calculated. You can’t just do whatever you like, or choose to livestream today but not the other, or irregularly … These counts in the algorithm. It is like you are awarded one point if you do well, but otherwise, points will be deducted.”(Da Ren 2)

Da Ren 2 (and the other Da Rens we interviewed) acknowledged that the assessments are not manipulated but generated from an algorithm that no one could clarify. More critically, the algorithmic rating and rank ing that have a direct impact on the reward also serve to shape the desired behaviors of Da Rens in the longer run.

4.2.1.2. Coordinating the Division of Labor Two issues related to the division of labor were also identified when Taobao added the new side of Da Rens. First, when the new side was added, Taobao resumed the role of “supervision.” In addition to filtering inappropriate content at a broad level (content that contains sex, violence, vulgarity) per regulatory requirements, Taobao devised specific guidelines, including the format of the content, type of font in the blog articles, number of pictures, and length of paragraphs. Because content production demanded a different set of knowledge, Taobao chose to implement and refine these guidelines with an iterative process. While being instrumental to the consistency and quality of the content, because of their high frequency of changes, these guidelines imposed an intense feeling of uncertainty and stress on the Da Rens. MCN 4 described the challenges of the Da Rens to stay abreast of frequent changes.

Figure 1. (Color online) Example of Da Ren Analytics Breakdown (Translated)  
![](/api/attachments/PPQDH5UZ/fulltext/images/793ecd14590bc52e84e678f68b17adfb03e89e1d30c9e5f0546f66189a17b52f.jpg)

![](/api/attachments/PPQDH5UZ/fulltext/images/f8bc541bce1205cc325a8da248c1867dccb8dcee493dd021779f6e39fd4553bb.jpg)

“Taobao rules change very frequently … There are minor changes every week and major changes every month … Many Da Rens have no idea or simply no time to keep themselves updated. It can be very messy when they post things up … (MCN 4)

The second issue is related to the evolving task division among the sides. In the context of the DP, this was closely related to the role of the sides and the values that sustain their existence in the DP. In our case, the introduction of Da Rens to Taobao introduced threats to the value proposition and role of another side, that is, the marketers in the DP. The marketers previously provided DP merchants with marketing solutions akin to those of traditional marketing firms for offline businesses. Both the Da Rens and marketers possessed marketing capabilities in general and aimed to maximize the value of their resources, undermining the fact that the Da Rens’ capabilities and roles overlapped with those of marketers. Subsequently, some marketers evolved into agents who offered organizational support to individual Da Rens. Because there was no clear division of tasks among the Da Rens, marketers and agents, several issues emerged, including the risk of agents being “disintermediated” and the problems of static growth in the Da Rens due to the incompetency of the agents. An agent we interviewed, MCN 4, recalled the early stage of its development as follows:

“Due to price transparency and convenience that the platform provides, the merchants could go over us and approach the Da Rens directly. They may not have realized the value-add we provide.”

The unclear role and tasks that should be assumed by an agent were also illustrated by Da Ren 2, who joined the DP in late 2016:

“Because this is a new arena within Taobao, my previous agent seemed to lack operational knowledge … The agent would think that they are leading me in the game, but no training or further information is provided. They won’t share with you how to improve, how to analyze your past data and how to make refinements.”

To address those inefficiencies, Taobao reallocated the resources among the platform sides and shaped work specialization by leveraging technologies. Taobao delegated its coordinator’s task to marketers/agents whose role was formalized as multichannel networks (MCNs). In general, MCNs acted as the managing agents of the Da Rens, providing support for them to grow in the DP. The benefits of this change were multifold. First, by delegating the coordinating task to MCNs, Taobao’s workload was reduced, as they did not have to deal directly with a large number of Da Rens, whom they had little domain knowledge about. Second, Da Rens could focus on their expertise in producing content, with the task of keeping track of the DP updates being “taken over” by the MCNs. Third, the MCNs benefitted from being able to continue with the provision of marketing solutions. By aggregating a number of Da Rens, the bargaining power of MCNs with merchants and service suppliers, such as the logistics and warehousing providers, would be greater than that of an individual Da Ren. The saved costs could also be diverted to explorations and experiments to further develop the Da Rens. MCN 2 called themselves a “bridge” between merchants and Da Rens.

Task delegation and changes in the interdependencies among the sides were managed delicately, considering the autonomy of these actors in the DP environment. With an official digital certification provided by Taobao, MCNs were openly endorsed and allowed to “recruit” or foster contractual relationships with Da Rens. Through multiple online marketing events and regular updates of MCN rankings (see Figure 2), Taobao indicated the transfer of key resources from the DP to the MCNs, including access to specific channels/pages that allowed Da Rens a higher exposure to visitor traffic. Da Ren 5 described how Da Rens were encouraged to foster a relationship with MCNs,

“Taobao would give some quota to MCNs, which were in turn given to us [the Da Ren]. These “quotas” push us up on the featured page of the platform. When you are being featured, you get more exposure and web traffic.

As of the end of 2018, there were over 600 MCNs, and in 2020, the sales amount of more than 100 MCNs exceeded a hundred million yuan (USD 14 million). In addition to keeping the Da Rens informed of the updates from Taobao, they took up the tasks of filtering good products for the Da Rens, negotiating sales with merchants, analyzing the Da Ren’s followers and providing training and guidance. Almost all the Da Rens interviewed explicitly expressed the advantage of working with MCNs; Da Ren 3 says,

“You cannot do it alone … there are many interrelated tasks and the MCNs are there to support them. I feel that my relationship with my MCNs is one that is mutually enabling … It is a win-win.”

4.2.1.3. Coordinating for Value Alignment. The third aspect of coordination that emerged during our analysis focuses on the possibility of misaligned interests or goals. At the initial stage, Taobao spent most of its attention on providing incentives and support to members of the new side, as the literature suggests. The interests of Taobao and those of the Da Rens are in close alignment;

Figure 2. (Color online) MCN Rankings (Translated)  
![](/api/attachments/PPQDH5UZ/fulltext/images/3ed98c3263df3c7342753d7e1f4780ecd4a339e83fd342e4ba968929c09efc78.jpg)

hence, the significance and size of Da Rens on Taobao grew. Fueled by the technological and infrastructure advancements that made the creation and wide distribution of a variety of content possible (video, live stream), more people realized the monetization value of user-generated content. In 2016, the 12 top-paid You-Tube celebrities earned a combined income of \$70.5 million (Berg 2016). Locally, the success of early influencers, such as Zhang Dayi (followed by more than 4 million followers on Weibo, China’s largest social media platform) and Xueli (followed by 1.4 million Weibo followers), whose Taobao shops recorded monthly sales of millions of yuan (Qian 2016), also attracted a large pool of influencers to Taobao.

However, as the Da Rens operate as free market actors, they soon found themselves facing the issue of misaligned interests with others. One such issue stemmed from the conflict between the long-term interests of the entrepreneurial Da Rens and the short-term priorities of other actors. To increase sales of products, merchants would, in general, expect Da Rens, similarly to a spokesperson or promoter, to speak in favor of their products. However, Da Rens (all of those interviewed in this study) believed that they were accountable to their followers as a trusted source of information and must provide authentic and honest product recommendations to maintain the followers’ loyalty in the long run. Da Ren 1 corroborated their attention to long-term development by describing that careful product selection would go far to maintain a Da Ren’s credibility. Their central and distinctive character shaped by their grassroots origin and the creative logic rooted in their professional norm also compelled them to stay independent despite the principal-agent relationship with the merchants. MCN 3 explained how a Da Ren defended his long-term interest, even at the expense of the merchants,

“Ma [pseudonym of the Da Ren working with MCN 3] only decides to promote a product when he feels okay with it. Otherwise, he would rather go against merchant and refuse to promote. Therefore, his fans are all die-hard fans … . He would try the product first for a few days. In his live streaming, he said he was not afraid of offending the merchants. He would ask the followers to wait for his trial result before buying a 3000-yuan oven because it was quite expensive. If the product is good, he will say it directly. However, if it’s not good, he will also be honest and ask people not to buy it.”

In addition to time orientation, the environment external to the focal DP continued to afford the Da Rens development opportunities beyond the home platform. One of them was cultivating the Da Rens’ personally owned traffic outside Taobao, especially on competing platforms. In addition to their Taobao account, Da Rens could maintain followers on other social media platforms, such as WeChat or Weibo. For instance, on multiple social media and content-sharing platforms, Zhang

Dayi and Li Jiaqi, among the top-performing Da Rens, have presences complementing their Taobao account. At the same time, nearly all major social media platforms that offer personal accounts and groups, including Kuaishou, TikTok, Xiaohongshu and WeChat, have entered Taobao’s e-commerce territory by incorporating e-commerce features within their site. While the Da Rens might find it necessary to maintain their presence on several of these platforms, they could inadvertently drive followers, traffic, and sales away from Taobao’s marketplace. In illustrating the limitations of Taobao on the ability of the Da Rens to connect with their followers, Da Ren 2 shared this feedback from her followers:

“The limitation is evident in the algorithm of Taobao and TikTok. In TikTok or other social media-like platforms, the users will find the influencers whom they followed or subscribed to appearing on the landing page of the app. The bond is naturally stronger. This is, however, different in Taobao. My followers have been telling me that it is not as easy to locate me in the app, and sometimes they gave up buying a product through me. This is likely because Taobao wanted visitors to browse through more shops rather than limiting his or her purchase with one store or via one influ encer. The more the person visits other stores, the more likely he or she will buy something.”

In contrast to the conventional strategy of promoting a user’s single-homing, Taobao not only allowed but also encouraged Da Rens to develop a presence and user base on other DPs and direct traffic from those DPs to Taobao. The core strength of Taobao was in e-commerce, their key to monetizing traffic and followers. Since other platforms, mainly social networking-based platforms, presented additional channels through which content could be distributed and new users reached, they complemented rather than competed head on with Taobao. By allowing

Da Rens to spend time and effort growing their viewership base on other platforms, Taobao hoped that the influence of their personal brand and reputation would spill over and scale. MCN 6 elaborated on how traffic diversion could be accomplished despite the restrictions of other DPs:

“I would ask our Da Rens to film relevant short videos such as how they choose a product for the followers or extract the content of, say, a make-up lesson from their past live stream. We distribute those contents onto other DPs and later bring [the traffic] back to Taobao … We can still leave our WeChat contact details on TikTok, Kuaishou. After they add the Da Rens in WeChat, we can then disseminate the link to the Taobao live stream in the newsfeed. This is how you ‘transfer the followers.

To bolster Da Rens’ dependence on the DP, Taobao implemented several mechanisms to empower Da Rens positions as market actors in the DP. To allow Da Rens to manage their own development and refine their strategies, Taobao continued to improve the dashboard that presented a detailed analysis of a Da Ren’s “business.” In addition to the basic demographic information of its followers, the dashboard also synthesized information related to the products the Da Rens promoted, their past livestreaming sessions, their interactions with followers, and the purchase patterns of their followers (leveraging the integral e-commerce functions of Taobao). Figure 3 depicts an example of Da Ren’s livestreaming dashboard. Another tool provided by Taobao integrated a tiering system that categorized their followers/livestreaming audience. MCN 5 explained the following:

“The tier system is based on the frequency, how long they [viewers] have watched the show, whether they have bought something and whether they have commented. We can see who the die-hard fans are and who are diamond fans. Everyone can see if you are a die-hard fan or diamond fan. The system will notify us by showing that “Your diamond fan has entered the livestream.” We couldn’t remember our fans before, so this is good. The die-hard fans get special rewards and privileges during the live stream, such as being eligible for a lucky draw … This is an efficient and encouraging way to increase the fan’s loyalty to the Da Ren.”

Figure 3. (Color online) Da Ren’s Livestreaming Dashboard by Performance and Time (Translated)  
![](/api/attachments/PPQDH5UZ/fulltext/images/b1fb0b3b420130161d6b3632fde0ec924aaf1e4e197d8f8cfd1e0b21675e4d1e.jpg)

These features, in turn, promoted entrepreneurship among the Da Rens, thus encouraging them to be creative despite operating within a DP. As Da Ren 2 evinced, “This is also a kind of entrepreneurial undertaking.” Similarly, Taobao provided multiple new tools to existing players, such as MCNs to support their “new” roles. For instance, MCNs were provided with a backend tool to manage the Da Rens, such as automating the calculation of the Da Rens’ pay based on a predetermined ratio. MCNs could also explore and select new merchants that they wanted to work with by reviewing their product performance through another feature provided to MCNs.

4.2.2. Analysis Across the Instances. Based on the empirical observations above, we present our analysis. While we focused on identifying how the coordination issues were overcome, we realized that the understanding could not be complete without a comprehension of the agency of the platform sides, which affects how they behave within the platform organization. Therefore, our analysis below focuses on two aspects. First, we delineate how coordination issues arise as the platform sides enact their agency within a digital platform organization. From the three instances of coordination, we identify the platform sides’ agency as a temporally and spatially embedded process of engagement. In the second part of the analysis, we show how Taobao, the DP owner, overcame these coordination issues by employing several moves to influence the sides to align their actions, namely, habitating, signaling, and anchoring.

4.2.2.1. Enactment of the Platform Sides’ Agency. Temporally embedded engagement. Despite operating within a DP, the platform sides possess agency that is enacted when they actively engage with their own temporality (past, present or future orientations) when making a decision or a move. Our analysis, which is summarized in the data structure in Figure 4, shows that the actions and behaviors of the platform sides are not devoid of the influence of their past experience. Due to the Da Rens’ unfamiliarity with the norm of the focal DP as a result of limited prior engagement in the new tasks and the DP environment, they did not act as expected by the DP owner or the preexisting sides. Similarly, the preexisting platform sides (merchants and marketers in our case) were guided by patterns of expectations that arose from their past, cumulative experience of engagement within the DP. These ingrained patterns, which helped the preexisting sides continue to behave in a stable manner and anticipate the behaviors of others, are a “shadow of the past” that can hinder the mutual adaptation and integration between the new side and the others.

Figure 4. Data Structure–Part 1  
![](/api/attachments/PPQDH5UZ/fulltext/images/780757613ba9505578a8439a2c2bd6db13f125e186c8b3ddf0c5bf27b35a2a35.jpg)

Our case analysis also shows how the sides’ actions are informed by the present or immediate constraints and limitations of the DP. In our case, when new sides are added, the task of monitoring the new side is assumed by the DP owner. However, despite the technological lever, DP owners, even those as established as Taobao, have limited capacity and cannot possibly maintain a large and exponentially growing network. The monitoring task can be even more challenging if the addition of a new side involves an emerging area with limited established knowledge or certainty; Taobao has always been a transaction platform rather than a content-sharing platform, such as YouTube or TikTok. This can be problematic for the new side, who must comply with the changes the DP owners adopt as a part of the exploration and learning process of a new domain. In our case, this challenge for the sides was exacerbated when the frequency of change by Taobao was so high that the platform sides could not remain updated with the dynamic changes as they were simultaneously expected to complete the predefined tasks (i.e., content creation).

The last instance of coordination foregrounds another issue, that is, the potential misalignment of interests in a DP originating from the future orientation of actors in formulating goals and objectives. While platform sides (such as Da Rens in our case) surrender a part of their freedom to adapt to the specific rules and norms of a DP, these actors remain independent providers who aim to ensure the growth of their own ventures. As they “wear two hats,” some of their interests may not be in full agreement with those of other actors, and one example of this in our case manifests in the conflict between the long-term interest of the entrepreneurial Da Rens (to build and maintain their credibility and image) and the short-term priorities of merchants (to pursue the conversion to sales). Spatially embedded engagement. In addition to the temporal aspect, our analysis of the coordination issue presents the influence of spatial orientation (see Figure 4). In the first instance of coordination described in the previous section, the Da Rens’ orientation to their individual self was manifested in their identification with the role of a creative content producer. It is evident in our case analysis that the coordination between the new and existing sides can be affected by inherent differences between their logic of profession; compared with the merchants who sold tangible products or conventional services, the Da Rens contributed to the DP by offering creative and artistic content in multiple forms, such as videos and blogs. Due to the unfamiliarity with the product nature and difference in the profession, it is difficult for the existing sides to measure and assess the performance of the new side and their output quality. The coordinating sides’ competing demands further complicate this issue as follows: while merchants expected higher sales and conversion from the creative content, the Da Rens emphasized how creative and engaging their content was. Despite the best efforts and willingness, the costs of measuring the other side and cooperating with them can be too high for platform sides limited by their domain knowledge of the other side.

The second instance of coordination also illustrates the influence of spatial orientation, which relates specifically to the larger interconnected network of platform sides in which the side operates. In our case organization, despite contributing to complementarity at a col lective level, the new resources provided by the new side may overlap with some of those owned by the existing sides; both the Da Rens and marketers survive on their marketing capabilities. This can be problematic as either party, after learning about each other’s competencies, can transform into a credible competitor. Considering such risks, the existing and new sides may engage in renegotiations that change their collaborative relationship by modifying the boundary of the tasks each assumes. In our case, for instance, the marketers evolved into agents that serve, instead of competing with, the Da Rens. However, such fluid, self-organized changes in task division can compromise the quality of coordination, considering the variance in the sides capabilities and the complexities in navigating an uncertain landscape of unclear task boundaries and poten tially unreliable collaborators.

The agency in the sides is also affected by the larger environment in which they are embedded. Our analy sis of value alignment revealed the influence of the envi ronment in which the DP operates. As DPs constantly evolve due to changes in the business environment for their survival, the platform sides, which are legally autonomous, not only adapt to the internal influence of the changes in the DP but also expose themselves to the external influence of the larger environment. The platform sides can respond to market developments independent of the platform evolution, and they may participate in multiple competing platforms, as observed in the Da Rens in our case. From our case analysis, we observe that a rapidly developing environment could afford a range of possible alternatives and opportunities, which actors can leverage for their best interest even if it is at odds with the others.

In summary, the platform sides’ agency can be enacted when their actions are informed by the spatial or temporal contexts within which they act. Evidently, our case demonstrates such enactment of agency within a digital platform environment constituted by heterogenous platform sides, which could lead to coordination issues.

4.2.2.2. Digital Orienting. Habitating: Next, our analysis shows how the platform sides can be aligned despite changes. In our case, the algorithm-based assessment is instrumental in facilitating transactions between the Da Rens and merchants. The hard-to-assess behaviors of the new side are quantified by these algorithms and provided to the others. Hence, the cost of preexisting sides measuring the performance of the new side to make an informed decision is significantly reduced (e.g., when merchants choose a Da Ren to work with). The algorithm represents a codified assessment of the platform sides’ abilities, behaviors and performance, thus imbuing the expectation of DP owners of the sides to cooperate with each other.

Similar to many other DP coordination enhancement measures, Taobao’s algorithm-based assessment incorporates reward provisions by attaching monetary incentives that the sides receive based on the quality of their output. In addition, the algorithm applies an inputbased reward/penalty by tracking the inputs or behaviors of the sides within the DP, such as the regularity of contributions and ability to keep followers engaged. By associating the assessments with consequences, the algorithms encourage the platform sides to learn about the DP owner’s desired behaviors among the participants.

In addition, Taobao establishes a repeated stimulus; thus, the platform sides, such as Da Rens, are constantly reminded of the performance assessment and platform expectations. In addition to the continual performance measurement, the algorithm constantly alerts users of their performance. Their rankings are also frequently shared on the platform. When a rule is violated, the Da Rens receive immediate feedback or a penalty.

These tools not only establish an awareness of the DP’s expectations and dispositions but also grow familiarity within the sides. Over time, the sensitivity and responsiveness to the platform algorithm becomes ingrained in the sides’ patterns of behavior, leading to a reflexivity in the platform sides, who constantly monitor themselves, scrutinize themselves and use the resulting feedback to organize themselves. We refer to this process as habitating, which refers to the process by which the digital platform owner orients the platform sides toward acting in alignment with the platform’s dispositions rather than toward acting in accordance with their habits or practices by exposing them to repeated stimulus through consequences or reminders determined by a codified assessment of the platform sides’ abilities, behaviors and performance. This analysis is represented in the data structure in Figure 5.

Signaling: Our analysis pertinent to the coordination of the division of labor highlights the imperative to consider the agency embedded in the immediate temporal condition and the complex and fluid interdependencies among the sides. Our findings reveal the challenges that prevent the successful participation and adaptation of the (new) side, that is, the frequent governance changes imposed by the DP owner and the unclear task division with the existing sides. To address this problem, DP owners could refine the task design and allocation. As evident in our case, the DP owners delegated their supervisory role to MCNs (formerly marketers/agents) by giving them key resources previously owned by the DP owners (i.e., exclusive access to channels through which Da Rens can promote their content). There are at least two advantages to this approach as follows: 1) a reduction in the coordinative complexity of DP owners and 2) the redefinition of the interdependencies among the existing and new sides to change the overlapping resources or conflicting activities into synergistic ones. Regarding the new side composed of individual Da Rens, the new task structure that allows them to work with another side (i.e., MCNs) who acts as their agents buffers them from the frequency of changes, thus enabling them to focus on their own task (creating new contents).

How the DP owner encourages the members to forge desirable relations while allowing the individuals’ free will is highly crucial for this abdication of control to another. To achieve this goal, DP owners generate and share multiple signals, such as a digital certification or badge bestowed to MCNs who legitimize their new role. This process declares the DP owner’s approval and support of the new role. By endorsing MCNs, Taobao not only legitimizes their position as surrogate supervisors of the Da Rens but also acknowledges the prominent positions they occupy such that others will be enticed to replicate their success.

Furthermore, the DP owner could highlight the resources possessed by MCNs to encourage relevant sides, such as merchants and Da Rens, to forge new relationships with the MCNs. Through high-profile events that recognize the performance of MCNs and the regular and ongoing release of MCN rankings, Taobao sends clear indications to the participants that the resources previously owned by the DP owners (such as the traffic pool) currently belong to the MCNs.

We refer to this process as signaling, which refers to the process by which the digital platform owner orients the platform sides toward acting in alignment with the platform’s preferred value propositions and interactions by making its strategic decisions explicit and known to the platform sides through digital symbols and highlights. Signaling is critical when two (or more) parties have different information. The digital symbols and prominent prompts could signal some unobservable changes planned by the platform owners, such as the preference for MCN-Da Rens relationships. Because DP owners have no hierarchical power over the members, it is critical for DP owners to communicate their strategic plan such that the participants can make their own assessment and plan, which are hopefully aligned with those of the owners.

Figure 5. Data Structure–Part 2  
![](/api/attachments/PPQDH5UZ/fulltext/images/baf3cfb41b5908a6f06704b0314cb65b50722bd66e61662449bac20aa448ed8e.jpg)

Anchoring: The last digital orienting mechanism we identified is anchoring<sup>2</sup>, a process by which digital platform owners orient the platform sides toward acting in alignment with the platform’s long-term development by deepening the platform sides’ dependencies on the digital infrastructure such that they can use the platform as a primary base for their entrepreneurial undertaking outside the platform.

Anchoring can be achieved by building, enhancing and defending the core and unique strength of the DP while growing the dependency of the sides. In the example in our case, the DP owner owns a strong foothold in the e-commerce space. While defending their core strength, the DP owner empowers the platform sides by providing digital tools and capabilities that promote their level of cospecialization with the DP. Examples include the analytic dashboard, fine-grained functionality to help Da Rens manage their followers, and a backend functionality that supports the new role of MCNs in managing Da Rens. With these tools, the platform sides are better supported to operate as a business entity on the platform; the increased insight into their operations helps the sides improve their business over time, contributing to the overall growth of the DP and the collective good.

Notably, the DP owner in our case indirectly encourages the platform sides to further explore opportunities on other DPs. The DP owner realizes that it is difficult and unrealistic to forbid or even discourage the sides from having a presence on other DPs. Additionally, despite the rules regarding engagement, for example, users cannot mention the name of other DPs in Taobao livestream, users could use another code or phrase to refer to other DPs. Recognizing the need of Da Rens to build their follower base on multiple platforms, MCNs consciously plan for them to grow their presence on other platforms and, more importantly, to channel the resources (in our case, the followers and traffic) back to Taobao.

Taken together, although the sides are allowed to have a presence on other DPs, they leverage the focal platform as the dominant, default home base for it provide not only sufficient space to explore outside the DP but also the technological support and functions needed to operate as an entrepreneur on the platform. As the sides are “anchored” in a particular DP, they are encouraged to innovate while developing their ventures. This inclusivity is realized when the sides, despite multihoming, channel the resources back to the focal DP (e.g., by sharing the link to visit the focal DP on other DPs).

## 4.3. Outcome

As briefly presented in the concluding paragraph of each DP coordination instance in Section 4.2.1, the outcomes of Taobao’s interventions manifested in harmonious interactions among the platform sides. For example, in the first instance of DP’s coordination (Section 4.2.1), we illustrate how the Da Rens were able to grasp the “expectations” of their counterparts as a result of Taobao formalizing the performance metrics. Through the measures of their commercialization ability, the Da Rens further refined the design of their content to better address the merchants’ needs.

As previously mentioned in the second instance (Coordinating the division of labor), all Da Rens interviewed agreed that the new MCN role was beneficial. “I leave the communications with merchants to my MCN … I do my best to promote products. But, there could be other reasons as to why the product sales were not satisfactory … maybe it’s the quality or others … I would rather my MCNs handle these conversations” (Da Ren 2). Instead of viewing each other as competitors or treating one as having more advantage or power over them, Da Rens and MCNs worked with and complemented each other.

In saying that, these harmonious interactions can be temporary, leading to subsequent changes in platform sides’ interdependencies and power dynamics. MCN 6 suggested that the relationships between the Da Rens and MCNs can change: “We think that whoever possesses the control over the traffic calls the shots - followers are linked to the Da Rens’ accounts. You may feel that a Da Ren listens to you when he/she has a hundred or a thousand followers; they tend to agree more with you and think you could help them. But when they hit fifty, or sixty thousand followers, their mentality changes. We may push them further, but some Da Rens would be contented with their performance … They would have their own thoughts.” In fact, one of his Da Rens did so well and decided to start her own MCN, while several others commanded the buying power of millions of followers (Yang 2022). In Appendix D.2, we summarize the data structure of the outcomes.

## 5. Discussion

Our research aims to address the question, “How can digital platform sides be coordinated?” We propose a process model that focuses on 1) the contextual conditions foregrounding the influence of the platform sides agency, 2) the mechanisms activated for platform coordination, and 3) its outcome. In Figure 6, we summarize the model, which is discussed in the following sections.

## 5.1. Contextual Conditions

Our research at Taobao shows that platform coordination is triggered by the instability in a DP organization as a result of dissatisfaction among the platform sides, whose interdependencies are changed, and the limited control of the DP owner over the platform sides. The critical role of a DP owner lies in the ability to create a stable value network in which all sides are satisfied with their positions and interactions (Cennamo et al. 2018). As shown in our case, the stability of this network can be disturbed by the strategic addition of a new side. More importantly, this shift in platform configuration necessitates changes in the existing interactions; the merchants are currently encouraged to engage the Da Rens, and marketers need to foster a new principalagent relationship with the Da Rens. Despite the structure implemented, such as a new feature that allows merchants to transact directly with Da Rens, the plat form sides can still experience dissatisfaction while interacting with their new counterparts, who do not behave how the DP owner expected (e.g., merchants find it difficult to evaluate the past performance of a Da Rens from the brief information they provide regarding themselves).

Furthermore, it is becoming more difficult for DP owners to exercise their “power” over the sides. Fundamentally, because the sides are legally autonomous, DP owners have no hierarchical power in dictating the platform sides’ actions (Gawer 2014). In saying that, scholars have asserted that some large and dominant DP owners exert power over the participating sides and

Figure 6. The Process Model of Digital Platform Coordination

<table><tr><td></td><td>Enactment of the platform sides&#x27; agencyTemporally embedded engagementSpatially embedded engagementDigital orienting by platform ownerIntegration of effortsHabitatingDivision of labor SignalingValue alignment Anchoring</td><td>Temporary) Harmony within digital platform organization</td></tr><tr><td>Concept</td><td colspan="2">Definition</td></tr><tr><td>Contextual conditions</td><td colspan="2">The starting point for the enactment of the platform sides&#x27; agency and digital orienting is when the sides are not satisfied with the new configuration and the power asymmetry between the DP owner and sides is low.</td></tr><tr><td>Enactment of platform sides&#x27; agency</td><td colspan="2">A process by which coordination issues emerge when a platform side engages with patterns from their temporality and/spatiality while interacting with other sides or the DP owner.Temporally embedded engagement: A process of engaging with one&#x27;s past, present, and future orientation when making a decision or action.Spatially embedded engagement: A process of engaging with oneself, interrelations with other sides, and relationships with other DPs when making a decision or action.</td></tr><tr><td>Digital orienting</td><td colspan="2">A process by which the DP owner induces the platform sides to pursue certain actions within the space of enabled possibilities.Habitating: a process by which the digital platform owner orients platform sides toward acting in alignment with the platform&#x27;s dispositions rather than toward acting in accordance with their habits or practices by exposing them to a repeated stimulus through consequences or reminders determined by a codified assessment of the platform sides&#x27; abilities, behaviors and performance.Signaling: a process by which the digital platform owner orients platform sides toward acting in alignment with the platform&#x27;s preferred value propositions and interactions by making its strategic decisions explicit and known to the platform sides through digital symbols and highlights.Archoring: a process by which the digital platform owner orients platform sides toward acting in alignment with the platform&#x27;s long-term development by deepening the platform sides&#x27; dependencies on the digital infrastructure such that they can use the platform as a primary base for their entrepreneurial undertaking outside the platform.</td></tr><tr><td>Harmony within digital platform organizations</td><td colspan="2">Coordinated actions within a digital platform organization in terms of divisions of tasks, integration of efforts and value alignment among the DP owner and platform sides.</td></tr></table>

that their informal, bargaining power stems from the possession of unique resources, such as access to a large customer base or technological architecture (Gulati et al. 2012, Cutolo and Kenney 2021); Amazon, for instance, has entered the market of its seller (Zhu and Liu 2018). This is, however, not evident in Taobao’s case. First, by adding Da Rens as a new side, Taobao is venturing into a new business area of content creation and, thus, competes with other existing content, livestreaming, and social networking platforms, representing the origins of most influencers. Similar to Taobao, many other e-commerce platforms compete for these influencers. The availability of alternative platforms that afford a similar market access lowers the power asymmetry between Taobao and the Da Rens as a new side. In fact, the informal power of some large platforms may have been overestimated. For instance, Facebook’s prevailing position as an influential and dominating social networking platform has been circumvented by the rise of TikTok, which is only five years old (The Economist 2022).

## 5.2. Mechanisms

The contextual conditions set the scene for the activation of the action formation mechanism, which comprises the following two main mechanisms: the enactment of agency by the platform sides and digital orienting by the DP owner.

5.2.1. Enactment of the Platform Sides’ Agency. The enactment of a platform side’s agency refers to the process by which coordination issues emerge when a platform side engages with patterns from their temporality and spatiality while interacting with other sides or the DP owner.

We conceptualize the enactment of agency as a temporally embedded process of engaging with one’s past, present, and future orientations. In line with Emirbayer and Mische’s (1998) notion of temporally constructed agency, the platform sides’ actions can be informed by their past (e.g., routines) and the present (e.g., current challenges) and directed by the future orientation (e.g., future goal). Furthermore, despite being a relatively new form of organization with permeable organizational boundaries (Gulati et al. 2012), a DP is nonetheless an organization and, therefore, has its culture and norm; we cannot assume that any participants who join can immediately “work” seamlessly with others. In helping the participants to accommodate the DP, we cannot disregard the temporality of their empirical existence, which may not be aligned with the DP owners and other sides. For instance, when platform sides exercise agency, they construct future expectations regarding their development on the DP. As they generate actions in relation to their hopes, concerns, and desires for the future, those actions may form a contradictory force with the DP owners and other sides who similarly have their own future expectations. To ensure an alignment of actions, the platform sides must negotiate their paths toward the future with other entities. While DP studies have underlined the self-interested motives of platform participants and, hence, the conflict of interest or collective-individual tension between the DP owner and a particular side (Wareham et al. 2014), our study further explicates the source of misalignment by featuring the temporality aspect of agency.

We also identify the enactment of agency as a spatially embedded process of engaging with oneself, interrelation with other sides, and relationships with other DPs. Consis tent with a few prior studies (Ghazawneh and Henfridsson 2011, Tiwana 2015, Staykova 2018), our study acknowledges that platform sides exercise their agency while operating within an organization with fluid boundaries. In line with the previous argument that the platform sides operate in a pluralistic environment (Qiu et al. 2017), our analysis further reveals that actors are simultaneously embedded in multiple local and global landscapes that shape their interactions (Malgonde et al. 2020). When interacting with others in a DP, the platform sides are predisposed to account for their positioning in different spaces, including their individual self (e.g., professional practices), their interrelations with other sides (e.g., competitive relationships with other sides), and their relationships with other DPs (e.g., the need to maintain a presence on other DPs). In fact, previous studies concerning platform ecosystems have revealed the influence of the individual entity, such as that manifests in the inherent expectations and guiding norms emanating from one’s organizational identity (Lindgren et al. 2015). Our study further explicates how the actions of platform sides are affected by the web of interdependencies that connects them with other sides and the larger landscape comprising multiple competing DPs. In contrast to coordination in a traditional organization or interfirm networks in which the entities actions are primed by either an internal hierarchical environment or market relations, the emergent findings in this study reveal the existence of multiple environments in which the DP sides are embedded, highlight ing the tendency and challenges the sides face in asserting their individuality while operating as an integrated part of a larger whole (Wang 2021).

Understanding the temporally and spatially embedded engagement when the sides enact their agency enables us to account for the unique positions of the participating sides and sensitizes us to a broader range of issues that may arise while coordinating multiple sides.

5.2.2. Digital Orienting. In response to the coordination issues arising from the enactment of the platform sides agency, DP owners activate what we call the digital orienting mechanism, which is a process by which the DP owner induces the platform sides to pursue certain actions within the space of enabled possibilities. This conceptualization contrasts the often-discussed enabling and constraining effect of technology in DP. To illustrate, enabling or constraining technology means the creation of possibilities or impossibilities of action. In the context of a DP, studies have described how the platform architecture and governance can enable and constrain the interactions among the sides (Cennamo and Santalo´ 2019, Sandberg et al. 2020) and how boundary resources can impose what is allowed and what is not when the DP owner attempts to establish the boundaries of a platform (Eaton et al. 2015). For instance, platform governance, which is defined as who makes what decisions regarding a platform (Tiwana et al. 2010, p. 679), dictates what a platform side can and cannot make a decision about. By suggesting that actors will narrow down the possibilities to one course of action desired by DP owners, they risk neglecting the autonomy of the sides within the spaces of enabled possibilities (Cardinale 2018). Therefore, while these studies focus on whether a platform side will or will not participate, they may have overlooked the fact that platform sides can determine “how to participate”; a recent study by Malgonde et al. (2020) highlights that a DP owner must nudge their decisions. As our study foregrounds the agency of the sides, the analysis opened space for us to observe the unexpectedly deviating actions of the sides that do not follow either enabled actions or constrained actions. These deviating actions can lead to misalignments among the platform sides and DP owner, preventing the value proposition from being realized. Importantly, the analysis allows us to focus on how DP owners orient actors toward some possibilities rather than toward others, leveraging digital means including algorithm, digital certification and announcements, and digital infrastructure. We argue that the conceptualization of digital orienting is significant because it theorizes the nature of the DP owners’ action in coordinating sides that are not subjected to its formal authority. Our analysis shows three digital orienting mechanisms.

5.2.2.1. Habitating. The first mechanism is habitating, a process by which DP owners expose the platform sides to a repeated stimulus through consequences or reminders determined by a codified assessment of the platform sides’ abilities, behaviors, and performance. Recognizing the agency of the platform sides in making its decision regarding how to participate in a specific DP and, hence, the limitation of a DP owner’s directive command in influencing the sides’ behavior, the DP owner must explore other ways to orient the platform sides toward acting in alignment with the platform’s new expectations. A fundamental step (demonstrated in our case) is to measure and track the platform sides’ performance, abilities and behaviors (Mo¨hlmann et al. 2021). In the context of a digital platform, these measurements can be codified in algorithms, reflecting the dispositions of DP owners. Drawing on Bourdieu’s (1989)’s concept of habitus, we argue that these codified measurements shape the habitus of DP organization by refining the worldview and way of thinking that the DP owners would like to impose on the platform sides (Shimoni 2017). Once habitus is learned by social agents (individual, groups or organizations), it “‘naturally affects the way they think and behave” (Shimoni 2017, p. 264). Hence, to encourage platform sides to learn about the habitus, DP owners can associate a reward or penalty and measured performance, abilities or behaviors in order to strengthen or weaken the voluntary behaviors of the platform sides in relation to the DP owner’s expectations. In addition to rewards and punishments, the platform sides learn to operate in a DP through nonassociative learning, such as repeated stimulus, a learning that is not associated with a direct reward or penalty. A repeated stimulus can manifest in continual performance assessments and provision of the assessment outcomes to the sides, frequent and regular sharing of performance rankings, and instant feedback regarding behaviors, such as a warning (with no penalty). These repeated and significant stimuli sensitize the platform sides as they are perceived as having strong positive or negative values. Over time, these sensitizations will be internalized into platform sides’ awareness, directing their behavior and habitual reactions (Joyce and Edinboro 2022). For instance, a Da Ren is more likely to work on his/her interactions with viewers if this issue is consistently flagged as an area for improvement in the person’s performance dashboard or to work toward developing a consistent theme in their content, which is one of the measured dimensions of ability. Over time, the platform sides who remain with the DP will be oriented toward certain actions, particularly those measured and tracked per the DP owner’s strategic intention. While some of our findings correspond to the literature concerning platform control, we focus on the learning process of platform sides rather than the control a DP owner possesses (Tiwana et al. 2010).

5.2.2.2. Signaling. The second mechanism is signaling, a process by which a DP owner makes its strategic decisions explicit and known to the platform sides through digital symbols and highlights. Compared with habitating, which is related to influencing specific behaviors and practices, signaling is related to shifts in the platform sides’ value network, roles, and tasks, which are largely unexplored since the previous DP literature has imposed fixed roles on platform sides, restricting them to either being consumers or innovators (Gawer 2014). When a change in a DP’s configuration warrants changes in the value network, roles, and tasks of the platform sides, the DP owner must employ measures to orient the actions of the platform sides, who make independent decisions with regard to its strategy and development as legally independent entities (Gulati et al. 2012). To reduce the information asymmetry between DP owners and sides (Connelly et al. 2011), a key step is for the DP owner to send signals or “informational cues sent out by one party to another in order to influence desired outcomes” (Taj 2016, p. 339). These signals could contain information regarding the DP owner’s strategic directions and design choice, which are shared through a high-profile declaration of changes (such as the introduction of a new side or changes in existing sides through a site-wide or in-app announcements) intended to garner the attention of receivers (i.e., sides) who can then make an informed choice of action (Connelly et al. 2011). A signal like the digital certification attached to a user account could also serve as an endorsement of new roles or changes required for not only the directly impacted side (e.g., marketers in our case) but also other players due to their interdependencies such that the affected sides can be assured that their adaptation is worthwhile in the long run and a mutual agreement among the sides in regard to their positions and activity flow can be achieved (Adner 2017). Because a DP owner may allow multiple possible ways of interactions (for example, merchants can choose to transact with Da Rens directly or via MCNs) and platform sides cannot know for certain which interactions are desired, signaling in the form of frequent highlights of MCN success and mentions by the DP owner is also critical for explicitly indicating which interactions are prioritized over others (Hukal et al. 2020). Over time, the relevant sides are influenced to adapt, leading to the realization of a new set of coordinated actions that the DP owner intended.

5.2.2.3. Anchoring. The last mechanism of digital orienting is anchoring, a process by which DP owners deepen the platform sides’ dependencies on the digital infrastructure such that they can use the platform as a primary base in their entrepreneurial undertaking outside the platform. While the platform sides surrender a part of their freedom to adapt to the specific rules and norms of a DP, these actors remain independent providers who aim to ensure the growth of their own ventures (Nambisan and Baron 2021). In fact, platform sides demonstrate a “tendency to preserve and assert its individuality as a quasi-autonomous whole; and to function as an integrated part of an (existing or evolving) larger whole” (Koestler 1967, p. 343); they can function as a constituent part of a DP and an independent entity functioning in several complementary or competing DPs. Acknowledging this individual-collective tension and the need to embrace the entrepreneurial, selfinterested motivations of sides (Wareham et al. 2014), DP owners could strengthen the dependency on the DP by enhancing their competencies on the DP (Iansiti and Levien 2004, Van Alstyne and Schrage 2016, Jacobides et al. 2018) while allowing them to explore further opportunities on other DPs. It is critical to develop ways and incentive for the sides to channel the resources gathered on other DPs back to the focal DP. These actions could collectively establish the DP as a home base enhancing the values the DP owner can afford to the sides (Huber et al. 2017); despite operating on multiple platforms, platform sides likely use one platform as their primary operating base. Instead of adopting a competitive position, DP owners can establish themselves as supporters of sides who are likely to have a presence in multiple platforms. Our conceptualization of anchoring resonates with the infrastructural anchor, proposed by Ingram Bogusz and Morisse (2018) to represent the digital infrastructure that links diverse groups of entrepreneurs and that limit their options in responding to environmental change. While we acknowledge that platform governance studies may provide further insight into the rules and control strategies for aligning the participants’ interests, we also argue that our findings regarding promoting the mutual interests of the platform sides and owners could extend the governance mechanisms that “would not provide incentives for higher user satisfaction beyond the minimum threshold” (Cennamo and Santalo ´ 2019, p. 637).

5.2.3. Outcome of Digital Platform Coordination. The outcome of successful digital platform coordination is a (temporary) harmony within the digital platform organization, that is, a set of coordinated actions within the digital platform organization in terms of the division of the task, integration of efforts and value alignment among the DP owner and platform sides. Such an outcome can be appreciated by a close examination of the interactions within the next-level entities of a digital platform. As depicted in Figure 6, the coordination of a digital platform organization is triggered by instability in the DP organization as a result of dissatisfaction among the platform sides whose interdependencies are changed (e.g., as a result of the introduction of a new side) and the reduced power asymmetry between the DP owner and sides considering the alternative DPs to which the platform sides can switch. These contextual conditions precipitate the enactment of the agency of the platform sides, who seek a more settled disposition to guide their actions during periods of upheaval and uncertainty (Emirbayer and Mische 1998). This enactment of the platform sides’ agency, in turn, limits the effectiveness of the DP owner’s coordinating actions, which revolve around the provision of an enabling or constraining structure. Hence, DP owners activate the digital orienting mechanism with the hope of influencing the decisions and actions of the platform sides. To influence the practices and routines of platform sides, DP owners codify their expectations in algorithm-based measurements and expose the sides to repeated stimuli (habitating). When changes in the value network affect the sides’ positions, roles, and tasks within the DP, the DP owner can send informational cues regarding the strategic changes and preferred arrangements, which could be otherwise difficult to observe, such that the sides can make an informed choice of action (signaling). Simultaneously, the DP owner can also orient the actions of the platform sides by building the focal DP as a home base as the sides inevitably activate their entrepreneurial undertaking on other DPs (anchoring). The platform sides could continually activate their agency while the DP owner engages in these digital orienting mechanisms. When a set of coordinated actions are achieved, as evident by harmonious interactions among the sides and between the sides and DP owner for achieving a goal, a harmony is attained within the DP organization. Because of the fluidity of the DP organizational boundaries and the interdependencies among the sides, this harmony can be temporary. As described earlier, the successful Da Rens can choose to become or double as a MCN, further complicating the platform sides interdependencies and power within the platform sides. This can trigger the further change in the power asymmetry between DP owner and sides; to illustrate, several Da Rens on Taobao had amassed a significant number of followers (some with over 60 million followers) which gave them immense power over the merchants and DP owner (Yang 2022). This competitive landscape, accompanied closely by a change in power asymmetry and interdependencies, requires DPs therefore to invest concerted effort for coordination and cultivation of platform sides. Platform coordination is an ongoing effort expanded to ensure continuous alignment among the platform sides (Gulati et al. 2012, Tiwana 2015).

## 6. Theoretical and Practical Contributions

Our study contributes to the digital platform literature. By adopting a meta-organizational view of digital platforms, we generate a process model that explains digital platform coordination in terms of the contextual conditions (when the platform sides enact their agency), the mechanisms of the platform sides’ agency enactment and digital orienting, and the resultant outcome. The articulation of the digital platform coordination process as an interaction between the enactment of the platform sides’ agency (by the platform sides) and digital orienting (by the DP owner) not only challenges the assumption that platform sides are exogenous to a DP (Gawer 2014) but also advances the DP literature by exhibiting the bidirectional influence between a DP owner and platform sides toward the attainment of alignment (Tiwana et al. 2010). To the best of our knowledge, this study is the first to offer a process model of digital platform coordination.

The process model offers at least two contributions to the DP literature. First, this model challenges the existing DP literature regarding the assumption of exogenous platform sides, highlighting the agency of the sides as a source of misalignment that must be managed. Previous studies largely assumed that digital platforms are stable entities; once a DP is successfully launched, platform sides are brought into coordination, which does not shift much, especially with the informal power that the DP owner possesses over the sides (Gulati et al. 2012, Gawer 2014). However, the platform configuration can change after its initial launch; when sides are added, removed, or shifted in terms of their roles or interdependencies with others, dissatisfaction can emerge. Therefore, it is problematic to continue treating the DP sides as exogenous and fixed, given that DP owners are actively and continually pursuing strategic changes. By regarding platform sides as a part of the DP organization, we not only show that the DP is “not an agent-less structure” (Gawer 2014) but also present how the agency of the sides can be a source of misalignment. Our findings validate the presence of a temporal orientation in the sides as they react to the coordination by DP owners and allude to the presence of a spatial orientation. As platform sides coordinate, they are oriented to the logic, opportunities, and constraints dominant in the different spaces that they simultaneously occupy. This situation is unique to DPs as platform sides are not subject to the dominant predisposition of a singular organizational environment in contrast to traditional employees. More importantly, the idea that (re)alignment within a DP organization will not occur on its own (Helfat and Raubitschek 2018) could benefit from our process model, which specifies the circumstances conducive to the enactment of the platform sides’ agency and how the platform sides can enact their agency while engaging with a diverse range of temporal or spatial orientations that derail them from the DP owner’s expected behaviors. Therefore, our analysis sheds light on the dynamics of the next-level constitutive parts, which remain poorly understood (Leong et al. 2019b).

Second, the proposed model complements the platform coordination literature that focus on enabling/ constraining the actions of sides by conceptualizing the digital orienting mechanism. By explicitly acknowledging the presence and influence of the platform sides agency, our investigation of platform coordination sensitizes us to the limitations of the existing coordination mechanisms in which DP owners implement a structure in the forms of incentive or technological architecture and then allow the market to influence all other actions (Qiu et al. 2017). Our study is a significant departure from past research. In addition to the structures that DP owners implement to enable or constrain certain actions of platform sides, our findings show that DP owners must also influence the members’ narrowing of possibil ities of action to orient the decision making and actions of the platform sides toward the DP’s preconceived design of interactions to achieve coordinated action. This can be achieved through digital orienting, which comprises habitating, signaling, and anchoring. Our mechanisms demonstrate how technology can be leveraged in a DP to influence platform sides and build voluntary cooperation within a digital platform organization, extending the primary focus of scholarly work concerning the effect of technological architecture. While resonating with the promotion of norms that similarly influence the sides’ behaviors (Huber et al. 2017, Qiu et al. 2017), the digital orienting mechanisms provide a more nuanced understanding of how influence can occur at an individual level rather than at the collective level. Considering that platform sides currently have more options of alternative DPs and are usually involved in multiple rather than merely one platform ecosystem (Wang 2021), it is prudent for DP owners to learn how they can influence the choice of the independent sides rather than imposing rules, codes of conduct or policies in building the norm of coordination.

Our study also offers managerial implications for DP owners. First, the DP coordination model offers an account that depicts the context in which the coordination mechanism will work, the sources of coordination issues, and the outcome. The insights of our process model benefit platform owners of new DPs because they prevent them from assuming that alignment among members can be created once structures, such as pricing and modular architecture, are implemented. The findings also benefit mature DPs whose configurations can change when sides are added (or dropped), as in our case. In particular, the model could shift the focus of executives or entrepreneurs to issues arising from the differences in and preferences of the participating members. The narrative accounts of how Taobao successfully coordinated multiple sides can be considered a contribution in general (Walsham 1995).

The second implication is the expanded repertoire of actions in coordinating a DP’s sides. DPs comprise members who are not legally bound to the organization via employment contracts (Gulati et al. 2012). Acknowledging the limitation of the formal authority and informa power of DP owners, previous studies proposed the need for hybrid organizing to draw upon both the hierarchical mode of control and the market-based mechanism in managing a DP. Our work builds upon and extends the previous literature as follows: we shift the primary focus to the agency, and we acknowledge that hybrid organizing is appropriate and offer further guidance for DP owners regarding how they can better coordinate members with technology. By contrasting with the previous application of technology for enabling and constraining actions among members, we conceptualize three mechanisms by which DP owners can influence the choice and decisions of platform sides, namely, through the design of algorithms (habitating), messages (signaling), and technological infrastructure (anchoring).

## 7. Limitations and Conclusion

This study has several limitations that can constitute a basis for future research. The first lies in this research’s singular context. Our study examines a digital exchange platform; its strategic focus rests on facilitating the matchmaking of core sides (e.g., buyers and sellers) and having more sides that reduce the costs that core sides incur to find each other and interact can potentially lead to a larger network effect and diversified sources of revenues (Evans and Schmalensee 2008, Hagiu 2014). Hence, we must be cautious in generalizing the results to other DPs with different foci, including often-studied software platforms that require the DP firm to retain a high degree of control over the development process of innovative products (Evans and Schmalensee 2008) and, hence, prefer fewer sides.

Second, because our research design focused on coordination within a DP organization and business envi ronment, limited attention was given to the regulatory and ethical contexts. Although these arguably fall beyond the scope of our study, they limit a complete and in-depth understanding of DP owners’ moves, which can have a downstream effect on coordination among sides. For example, the DP’s fast development pace, which instigated work specialization among the Da Rens and agents, was driven in part by the thenmaturing Chinese regulatory oversights over content generated by grassroots influencers who connect to a large audience (Tech Wire Asia 2019). We posit that future scholarly attention should be given to these external contexts, given the awakening market power of large DPs, such as Google, Apple, and Alibaba. In our case, the misalignment of the platform sides stemmed from the addition of a new side, a strategy that the DP owner adopted to integrate a variety of services in its platform. This, however, may be undesirable or even prohibited in other economic environments, such as those with competition laws and monopolistic concerns (Alt and Zimmermann 2019). Future researchers could further examine the agency of platform actors who are embedded in those larger contexts.

Despite these limitations, this study extends the scholarly and practitioner knowledge on how a DP firm can coordinate platform sides so that they are “brought into an alignment, considered and made to act together” (Thompson 2003, p. 13). Because DPs continue to evolve, platform coordination is not only a central but also an ongoing problem for maintaining alignment among the dynamic interactions of the platform sides. By adopting a meta-organizational view of digital platforms, our study reveals agency in the platform sides, coordination issues at the constitutive level of a DP, and the corresponding act of digital orienting. This study is arguably the first to offer an explicit account of DP coordination through research from within a digital platform and adopting a processual account (de Reuver et al. 2018). We hope that our model, by presenting a richer and more realistic portrayal of platform side coordination, advances our knowledge of the dynamics of digital platforms that are playing a growingly central role in the digital economy (Adner 2017, de Reuver et al. 2018).

Appendices  
Appendix A. List of Interviewees and Their Relationships

<table><tr><td>Company/Association</td><td>Position/Role</td><td>No. of Subjects</td><td>Description</td></tr><tr><td>Mobile Taobao Team</td><td>Team manager, product manager and one staff member</td><td>3</td><td>They lead the development and daily operations of the Taobao Vtask Platform that matches the merchants and Da Rens. This is the team that led the initiative to engage the Da Rens as a new side to the Taobao platform. The manager has ten years of experience working at Alibaba and has spent her last five years with the content strategy team.</td></tr><tr><td>Taobao Vtask Platform Development Team</td><td>Manager, Employee</td><td>2</td><td>They develop the Vtask platform. Both individuals have a combination of 15 years of experience with Alibaba.</td></tr><tr><td>Taobao Algorithm Team</td><td>Head of Commercialization Team and Project Manager</td><td>2</td><td>They focus on algorithm development to enhance the effectiveness of the matching between the merchants and the Da Rens, to quantify the performance of the Da Rens and to integrate the calculation of the Da Rens&#x27; earned incentives and income with other divisions within Alibaba.</td></tr><tr><td>Taobao Live streaming Team</td><td>Manager</td><td>1</td><td>The team leads the development of the livestreaming feature</td></tr><tr><td>Merchant 1</td><td>Employee</td><td>2</td><td>Merchant 1 represented a company with a 17-year history of producing face masks. He was in charge of liaising with the Taobao Da Rens.</td></tr><tr><td>Merchant 2</td><td>Employee</td><td>1</td><td>Merchant 2 represented a company with a 10-year history of selling children&#x27;s apparel.</td></tr><tr><td>Da Ren 1</td><td>—</td><td>1</td><td>Da Ren 1 was among the top 150 Da Rens at Taobao and was associated with MCN 4. She has over 230,000 followers and earned an annual income of approximately 5 million RMB (USD 1 million).</td></tr><tr><td>Da Ren 2</td><td>—</td><td>1</td><td>Da Ren 2 was a professional make-up artist who started a live stream that has been operating since the end of 2016. She moved to another MCN (MCN 4) for six months (as of the time of the interview). She had more than 5,000 followers, of whom the majority have stayed for at least two years.</td></tr><tr><td>Da Ren 3</td><td>—</td><td>1</td><td>Da Ren 3 joined the profession in 2017, producing content related to female apparel.</td></tr><tr><td>Da Ren 4</td><td>—</td><td>1</td><td>Da Ren 4, focused on skin care products, has a follower base of 320,000 and owns her online stores.</td></tr><tr><td>Da Ren 5</td><td>—</td><td>1</td><td>Da Ren 5 was a policewoman before working as a Da Ren promoting skin care products since 2018.</td></tr><tr><td>Marketer-turned MCN 1</td><td>Employee, Director of Digital Group, Director of SN system and COO</td><td>4</td><td>MCN 1 was a traditional marketing firm that joined the Taobao platform to serve merchants in 2015. In 2017, it transformed into an MCN that aided Da Rens in creating content for merchants. The number of staff increased from 70 in 2018 to over 100 in 2020.</td></tr><tr><td>Marketer-turned MCN 2</td><td>Employee</td><td>1</td><td>MCN 2 was founded in 2013 with strong marketing capabilities in producing short videos and graphics. It has a staff of over 30 as of 2018.</td></tr><tr><td>Marketer-turned MCN 3</td><td>Employee</td><td>1</td><td>MCN 3 was founded in 2015. It has a staff of approximately 160 and was one of the three winners of the three 3-star Short Video Maker prize awarded by Taobao in 2017.</td></tr><tr><td>MCN 4</td><td>Employee</td><td>1</td><td>Established in 2016, MCN 4 began by producing livestreaming content and manages over 180 Da Rens focusing on livestreaming beauty and fashion products.</td></tr><tr><td>MCN 5</td><td>Employee</td><td>2</td><td>Established in 2016, MCN 5 manages over 72 Da Rens with a staff of 15. It focuses on producing content in video and livestreaming formats mainly related to beauty products. On average, six Da Rens have made over 1 million.</td></tr><tr><td>MCN 6</td><td>Director</td><td>1</td><td>The interviewee was a director associated with MCN 4.</td></tr><tr><td>MCN 7</td><td>Manager of Da Rens</td><td>1</td><td>The interviewee was an agent working directly with a Da Ren in an MCN.</td></tr><tr><td>MCN 8</td><td>Trainer of Da Rens</td><td>1</td><td>The interviewee was a trainer associated with MCN 4.</td></tr><tr><td>Buyer 1</td><td>—</td><td>1</td><td>Buyer 1 has used the platform for at least 11 years and has followed at least five influencers on Taobao and WeChat.</td></tr><tr><td>Buyer 2</td><td>—</td><td>1</td><td>Buyer 2 has used the platform for at least ten years, has followed more than 10 influencers, and has bought products recommended by these influencers.</td></tr><tr><td>Total number of subjects</td><td></td><td>30</td><td></td></tr></table>

## Appendix A. (Continued)

![](/api/attachments/PPQDH5UZ/fulltext/images/aec9cdcd544ee443fc03b25fdb11fc3d41616c441cde2fbb75fd95c463dc0844.jpg)

## Roles and relationships of key sides on digital platform

Digital Platform: connects and enable the direct interactions of the multiple sides of economic actors and earn a transaction fees from the sides

Merchants: platform users (individuals or firms) who provide and sell a range of products/services

Buyers: platform users (mostly individuals) who consume and buy the products/services from the merchants

Da Rens: platform users who generate content containing their opinions and recommendation of products/services for distribution to a larger crowd (buyers) to generate consumer trust and to earn commissio or referral fee. Da Rens facilitate the transactions between merchants and buyers

Marketers: platform users (firms) who provide marketing solutions for merchants to promote their products/services within the digital platform

MCNs: platform users (firms) that played the role of the agents of these Da Rens in offering an integrated marketing solution. MCNs often evolved from marketers

## Appendix B. Initial Interview Guide

Digital Platform — Taobao’s Management

1. Can you describe your role, job scope, years of experience (in the company and others), expertise?

2. Can you describe the background of the company/unit—when was it established, purpose, KPIs, size, vision, relationship with other units?

3. Can you explain why the DP engages the influencers?

4. What are some of the key metrics used by the merchants and Da Rens?

5. How many influencers and merchants are there on the DP? How do you recruit them?

6. What are the services that you provide to them?

7. What are the challenges in managing the influencers and merchants on the platform? What strategies do you use to help the merchants and Da Rens establish themselves?

8. How does the DP address conflicts and issues that arise (a) between merchants and Da Rens, (b) among the Da Rens and (c) with the Da Ren Merchants

1. Can you describe how your company works with the Da Rens to promote your products?

2. Can you compare and describe the differences between product endorsement by traditional celebrities and by Da Ren?

3. How do you assess the performance of a Da Ren?

4. What are some conflicts and issues that arise (a) from using the DP to connect with marketers and Da Rens, (b) with Da Rens’, (c) and other DP actors?

5. How do you resolve those conflicts and issues that arise?

6. How effective are the DP’s advertising services? Do they differ for live streaming vs. blogs?

## Da Rens

1. Can you describe your work as an influencer? How do you generate income from the content that you create?

2. How did you start using the DP and other channels to promote your content?

3. How did you establish yourself as an influencer on the DP? How does the DP support your growth as an influencer? How do you grow your following on and beyond the DP?

4. How do you use the DP to track the success of your promotions?

5. What are some conflicts and issues that arise (a) from using the DP to connect with marketers and buyers, (b) with merchants on the DP, (c) with other Da Rens, and (d) with other DP actors?

6. How do you resolve these conflicts and issues that arise?

Marketers/Multichannel Networks (MCNs)

1. Can you describe your work as a marketer/MCN? Can you describe your work with Da Rens?

2. What are the changes to your work/company with the entry of Da Rens to the DP?

3. What are some conflicts and issues that arise a) from using the DP to connect with other actors b) with merchants and c) with Da Rens?

4. How do you resolve these conflicts and issues that arise?

5. How do you grow your business and operations?

6. How many Da Rens do you work with?

7. What are their average demographics?

1. How long have you been using the Taobao platform?

2. What do you usually buy on the platform and how frequent are your purchases?

3. Do you use other platforms? What are they? Why do you use different platforms?

4. How has an influencer affected your purchase and use habit?

5. What determines whether you “follow” an influencer?

6. What is important to you when deciding whether to purchase a product recommended by an influencer?

Appendix C. Chronology of Events  
![](/api/attachments/PPQDH5UZ/fulltext/images/218adcf16595279a63c6467061e9ae1c4f80ed41f3387d7d8bb4547a00864e77.jpg)

<sup>1</sup>Cyberspace Administration of China (CAC) issued the “Provisions on the Administration of Internet Livestreaming Services” to regulate livestreaming, for example, all platforms need to provide real-time monitoring on livestreaming, and all recordings must be stored for at leas 60 days.

<sup>2</sup>Regulations were imposed on digital platforms to ensure the livestreaming content has no violent or sensitive content.

<sup>3</sup>E-Commerce Law of the People’s Republic of China regulated that e-commerce participants should have formal registration and the obligation of tax payment.

<sup>4</sup>Several regulations were issued to regulate online sales behaviors, to prevent false promotion and counterfeit goods. They also provided formal definitions and regulations on different sides of the livestreaming e-commerce platform, including sellers, livestreamers, platforms and MCNs.

<sup>5</sup>National Radio and Television Administration issued that “Livestreaming shows and hosts should be clearly classified, based on their content, as music, dance, singing, fitness or games, among other categories, according to the circular; livestreaming platforms should implement real name management for users, as well as several specific rules on tipping behaviors.'

<sup>6</sup>Taobao upgraded Daren measurement Index Algorithm; “Da Ren Index” is an overall measurement of Da Ren capability or potential. The index includes five aspects, each with specific measurement items/features. These details are available on their personal pages. Also, the upgraded version includes more specific features such as return rates of fans, interaction qualities etc.

<sup>7</sup>Taobao initiated an incentive tool for Da Ren to grow their fan base. Da Ren could attract new fans by giving them “red packets,” or monetary gifts.

## Appendix D. Data Structures Appendix D.1. Data Structure of Coordination Aspects

1<sup>st</sup> Order Indicators

• Taobao provides rewards, in the form of monetary award and ranking, to Da Rens to motivate them to join and cooperate by executing tasks they are responsible fo

• Taobao provides additional resources such as exposure on official tasks to MCNs to motivate them to cooperate by executing tasks they are responsible fo

• Taobao provides information to platform sides to ensure that they have enough information to coordinate their actions with other

• Taobao develops the performance measurement of Da Rens fo merchants to assess their capabilities

2<sup>nd</sup> Order Themes

• Taobao develops a modular architecture that predefined the roles o each platform sides and their particular tasks (e.g., as merchants)

Core category

• Participants self-select into the roles, e.g., individuals can join the platform as merchant or Da Ren

• Taobao refines the architecture to add the new role of Da Ren and redefine the roles of others (e.g., marketers turned into MCNs)

• Taobao assumes the role of supervising Da Rens at the beginning and later delegated this role to MCNs

• Participants are free to move in and out of Taobao platform

• Taobao establishes the connections between merchants, buyers and marketers, creating a platform for their cocreation of product/service

• Marketers find their role being overlap that of Da Rens and thus evolve into MCNs

Aggregate Dimensions

• Taobao adds Da Rens to the platform to further enhance the economic gains for all platform sides

• Conflict between the long-term interest of the Da Rens who want t maintain their credibility and the short-term interest of merchant who prioritized profits (over honesty in product review)

• Da Rens prefer to maintain their independence despite the principalagent relationship with merchants

• Taobao supports the development of Da Rens beyond its platform • Taobao encourages MCNs to identify new Da Rens from other DPs • Da Rens diverts the traffic and followers from external platforms to Taobao

Provide reward provision

Integration of efforts

Provide information

Divide task

Division of labor

Allocate task

Coordination aspects in digital platform

![](/api/attachments/PPQDH5UZ/fulltext/images/60402cb9c9e1ea39ec2cab600a8dca61747cc0439884592ff4b164a0347b210b.jpg)

Maintain economic dependency

Resolve conflict of preference

Value alignment

Develop the future

Note. We would like to highlight that those highlighted in grey boxes are existing constructs adopted from Puranam (2014)’s basic problem of organizing.

## Appendix D.2. Data Structure of Outcome

## 1<sup>st</sup> Order Indicators

• Merchants are able to understand the performance of Da Rens with the algorithmic rating and ranking

• Merchants are able to appreciate the quality of Da Rens’ service (in the form of content)

• Da Rens develop familiarity with the rules of engagement in the platform

• Marketers turn into MCNs working as the agent of Da Rens rathe than their competitors

•MCNs position themselves as one that assists Da Rens with backend operations so to allow them to focus on content production

• (Most) Da Rens are happy with not having to deal directly with the constant rule changes by Taobao, and are contented with being able to focus on content production

• Da Rens use Taobao as the base, despite having presence in multiple platforms

• Da Rens and MCNs position themselves as an entrepreneu • Da Rens prefers Taobao over other livestreaming platforms for it provides a healthy ecosystem that focus on long term growth

• MCNs work with Da Rens to maintain their fans and growth over time

## 2<sup>nd</sup> Order Themes

Aggregate Dimensions

Coordinated actions in terms of integration o efforts:

Platform sides overcome costly actions to work together

Coordinated actions in terms of division of labor Platform sides act in accordance with the defined task breakdown that contribute to the shared goa

Coordinated actions in terms of value alignment: Platform sides make decisions and plan their development with the intention to stay and grow with the digital platform

(Temporary) Harmony within digital platform organization

## Endnotes

<sup>1</sup> While platform governance and platform coordination are closely related, their foci are distinct. Thompson (2003) has distinguished them by denoting “coordination as the ‘bringing together’ to governance as a ‘securing’ or regulation of that coordination.” (Thompson 2003, p. 14). Furthermore, Li and Kettinger (2021) differentiate plat form coordination by uncoupling it from authority and control, which are inherent in platform governance, to which Tiwana et al. (2010) refer as “who makes what decisions about a platform” (p. 679).

<sup>2</sup> The concept of anchoring in our paper is distinct from the anchoring effect/anchoring bias often studied in the context of individual decision making and algorithm-supported decision making. We focus on the use of anchoring as a strategic organizational level (rather than the downstream effect of the aforementioned studies) (e.g., Ingram Bogusz and Morisse 2018), and thus treating it as a concept at organizational level that can affect individuals, groups and firms (Ballinger and Rockmann 2010).

## References

Adner R (2017) Ecosystem as structure: An actionable construct for strategy. J. Management 43(1):39–58.

Alibaba (2015) Taobao turns shoppers into sales force for 12.12 event. Alizila News. Alibaba Group, Hangzhou, China.

Alt R, Zimmermann HD (2019) Electronic markets on platform com petition. Electron. Marketing 29(2):143–149.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Azor´ın M, Francisco J (2014) Microfoundations of strategic management: Toward micro–macro research in the resource-based theory. BRQ Bus. Res. Quart. 17(2):102–114.

Baldwin C, Clark K (2000) Design Rules: The Power of Modularity (MIT Press, Cambridge, MA).

Baldwin CY, Woodard JJ (2009) The architecture of platforms: A unified view. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar, Cheltenham, UK and Northampton), 19–44.

Ballinger GA, Rockmann KW (2010) Chutes vs. ladders: Anchoring events and a punctuated-equilibrium perspective on social exchange relationships. Acad. Management Rev. 35(3):373–391.

Barney JAY, Felin T (2013) What are microfoundations? Acad. Man agement Perspect. 27(2):138–155.

Berg M (2016) The highest-paid YouTube stars 2016: Pewdiepie remains no. 1 with \$15 million. Forbes.

Berkowitz H, Bor S (2018) Why meta-organizations matter: A response to Lawton et al. and Spillman. J. Management Inquiry 27(2):204–211.

Berkowitz H, Dumez H (2016) The concept of meta-organization: Issues for management studies. Eur. Management Rev. 13(2):149–156.

Bourdieu P (1989) Social space and symbolic power. Sociol. Theory 7(1):14–25.

Cabral L (2011) Dynamic price competition with network effects. Rev. Econom. Stud. 78(1):83–111.

Caillaud B, Jullien B (2003) Chicken and egg: Competition among intermediation service providers. RAND J. Econom. 34(2):309–328

Cardinale I (2018) Beyond constraining and enabling: Toward new microfoundations for institutional theory. Acad. Management Rev. 43(1):132–155.

Cennamo C, Santalo ´ J (2019) Generativity tension and value creation in platform ecosystems. Organ. Sci. 30(3):617–641.

Cennamo C, Ozalp H, Kretschmer T (2018) Platform architecture and quality trade-offs of multihoming complements. Inform. Systems Res. 29(2):461–478.

Connelly BL, Certo ST, Ireland RD, Reutzel CR (2011) Signaling the ory: A review and assessment. J. Management 37(1):39–67.

Cutolo D, Kenney M (2021) Platform-dependent entrepreneurs: Power asymmetries, risks, and strategies in the platform econ omy. Acad. Management Perspect. 35(4):584–605.

de Reuver M, Sørensen C, Basole RC (2018) The digital platform: A research agenda. J. Inform. Tech. 33(1):124–135.

Duffy DL (2005) Affiliate marketing and its impact on e-commerce. J. Consumer Marketing 22(3):161–163.

Eaton B, Elaluf-Calderwood S, Sørensen C, Yoo Y (2015) Distributed tuning of boundary resources: The case of Apple’s iOS service system. MIS Quart. 39(1):217–A212.

Eisenmann TR (2006) Platform-mediated networks: Definitions and core concepts. Harvard Business School Module Note 807-049. https://www.hbs.edu/faculty/Pages/item.aspx?num=33529& source=post\_page.

Emirbayer M, Mische A (1998) What is agency? Amer. J. Sociol. 103(4):962

Evans DS (2003) Some empirical aspects of multi-sided platform industries. Rev. Netw. Econom. 2(3):191–209.

Evans DS, Schmalensee R (2008) Markets with two-sided platforms Issues Competition Law Policy 1(28):667–693.

Gawer A (2009) Platforms, markets and innovation: An introduction. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar, Cheltenham, UK and Northampton), 1–16.

Gawer A (2014) Bridging differing perspectives on technological plat forms: Toward an integrative framework. Res. Policy 43(7):1239–1249.

Gawer A (2021) Digital platforms’ boundaries: The interplay of firm scope, platform sides, and digital interfaces. Long Range Plann. 54(5):102045.

Gawer A, Cusumano MA (2001) Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation (Harvard Business School Press, Boston).

Ghazawneh A, Henfridsson O (2011) Micro-strategizing in platform ecosystems: A multiple case study Proc. Internat. Conf. Inform. Systems 2011, vol. 3. https://aisel.aisnet.org/icis2011/proceedings/ generaltopics/3.

Ghazawneh A, Henfridsson O (2013) Balancing platform control and external contribution in third-party development: The boundary resources model. Inform. Systems J. 23(2):173–192.

Gioia DA, Corley KG, Hamilton AL (2013) Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. Organ. Res. Methods 16(1):15–31.

Glaser BG, Strauss AL (1967) The Discovery of Grounded Theory: Strat egies for Qualitative Research (Aldine de Gruyter, New York).

Gulati R, Puranam P, Tushman M (2012) Meta-organization design: Rethinking design in interorganizational and community contexts. Strategic Management J. 33(6):571–586.

Hagiu A (2006) Pricing and commitment by two-sided platforms RAND J. Econom. 37(3):720–737.

Hagiu A (2009) Two-sided platforms: Product variety and pricing structures. J. Econom. Management Strategy 18(4):1011–1043.

Hagiu A (2014) Strategic decisions for multisided platforms. MIT Sloan Management Rev. 55(2):71–80.

Halaburda H, Yehezkel Y (2013) Platform competition under asym metric information. Amer. Econom. J. Microecon. 5(3):22–68.

Helfat CE, Raubitschek RS (2018) Dynamic and integrative capabili ties for profiting from innovation in digital platform-based eco systems. Res. Policy 47(8):1391–1399.

Howard-Grenville JA (2005) The persistence of flexible organizational routines: The role of agency and organizational context. Organ. Sci. 16(6):618–636.

Huber TL, Kude T, Dibbern J (2017) Governance practices in platform ecosystems: Navigating tensions between cocreated value and governance costs. Inform. Systems Res. 28(3):563–584.

Hukal P, Henfridsson O, Shaikh M, Parker G (2020) Platform signaling for generating platform content. MIS Quart. 44(3): 1177-1205

Iansiti M, Levien R (2004) Strategy as ecology. Harvard Bus. Rev 82(3):68–126.

Ingram Bogusz C, Morisse M (2018) How infrastructures anchor open entrepreneurship: The case of Bitcoin and stigma. Inform. Systems J. 28(6):1176–1212.

Jacobides MG, Cennamo C, Gawer A (2018) Toward a theory of eco systems. Strategic Management J. 39(8):2255–2276.

Joyce E, Edinboro U (2022) Bourdieu’s practice theory as framework for grasping organizational change: A case study in China. AOM Annual Meeting Proc. 2022. https://journals.aom.org/doi/ abs/10.5465/AMBPP.2022.13683abstract.

Karanovic J, Berends H, Engel Y (2020) Regulated dependence: Platform workers’ responses to new forms of organizing. J. Management Stud. 58(4):1070–1106.

Klein HK, Myers MD (1999) A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quart. 23(1):67–94.

Koestler A (1967) The Ghost in the Machine (MacMillan, New York).

Kretschmer T, Leiponen A, Schilling M, Vasudeva G (2022) Platform ecosystems as meta-organizations: Implications for platform strategies. Strategic Management J. 43(3):405–424.

Langley A (1999) Strategies for theorizing from process data. Acad. Management Rev. 24(4):691–710.

Leong C, Pan SL, Bahri S, Fauzi A (2019a) Social media empowerment in social movements: Power activation and power accrual in digital activism. Eur. J. Inform. Systems 28(2):173–204.

Leong C, Pan SL, Leidner DE, Huang JS (2019b) Platform leadership: Managing boundaries for the network growth of digital platform. J. Assoc. Inform. Systems 20(10):1531–1565.

Li H, Kettinger WBJ (2021) The building blocks of software plat forms: Understanding the past to forge the future. J. Assoc. Inform. Systems 22(6):1524–1555.

Li H, Zhang C, Kettinger WJ (2022) Digital platform ecosystem dynamics: The roles of product scope, innovation, and collabo rative network centrality. MIS Quart. 46(2):739–770.

Lindgren R, Eriksson O, Lyytinen K (2015) Managing identity tensions during mobile ecosystem evolution. J. Inform. Tech. 30(3):229–244.

Malgonde O, Zhang H, Padmanabhan B, Limayem M (2020) Taming complexity in search matching: Two-sided recommender systems on digital platforms. MIS Quart. 44(1):49–84.

Malone TW, Crowston K (1990) What is coordination theory and how can it help design cooperative work systems? Proc. 1990 ACM Conf. Comput. Cooperative work (ACM, New York), 357–370.

Marciniak R (2013) From organization design to meta organization design. Benghozi PJ, Krob D, Rowe F, eds. Digital Enterprise Design and Management 2013. Advances in Intelligent Systems and Computing, vol. 205 (Springer, Berlin, Heidelberg).

Mo¨hlmann M, Zalmanson L, Henfridsson O, Gregory RW (2021) Algorithmic management of work on online labor platforms: When matching meets control. MIS Quart. 45(4):1999–2022.

Nambisan S, Baron RA (2021) On the costs of digital entrepreneurship: Role conflict, stress, and venture performance in digita platform-based ecosystems. J. Bus. Res. 125:520–532.

Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parnas DL (1972) On the criteria to be used in decomposing systems into modules. Commun. ACM. 15(12):1053–1058.

Puranam P, Raveendran M (2013) Interdependence and organization design. Grandori A, ed. Handbook of Economic Organization (Edward Elgar Publishing, London).

Puranam P, Alexy O, Reitzig M (2014) What’s “new” about new forms of organizing? Acad. Management Rev. 39(2):162–180.

Qian R (2016) Celebrity economy set for explosive growth in China. China Daily, http://www.ecns.cn/business/2016/03-16/203077. shtml.

Qiu Y, Gopal A, Hann I-H (2017) Logic pluralism in mobile plat form ecosystems: A study of indie app developers on the iOS app store. Inform. Systems Res. 28(2):225–249.

Raghu G, Arun K (1995) Technological and organizational designs for realizing economies of substitution. Strategic Management J. 16(S1):93–109.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Rochet JC, Tirole J (2008) Competition policy in two-sided markets, with a special emphasis on payment cards. Buccirossi P, ed. Hand book of Antitrust Economics (MIT Press, Cambridge, MA), 543–582.

Sandberg J, Holmstro¨m J, Lyytinen K (2020) Digitization and phase transitions in platform organizing logics: Evidence from the process automation industry. MIS Quart. 44(1):129–153.

Shimoni B (2017) What is resistance to change? A habitus-oriented approach. Acad. Management Perspect. 31(4):257–270

Siggelkow N (2007) Persuasion with case studies. Acad. Management J. 50(1):20–24.

Staykova KS (2018) Managing platform ecosystem evolution through the emergence of micro-strategies and microstructures. Proc. Internat. Conf. Inform. Systems 2018. https://aisel.aisnet.org/icis2018/ innovation/Presentations/22.

Strauss A, Corbin J (1998) Basics of Qualitative Research: Procedures and Tech niques for Developing Grounded Theory (Sage, Thousand Oaks, CA)

Sun H, Fan M, Tan Y (2020) An empirical analysis of seller advertising strategies in an online marketplace. Inform. Systems Res. 31(1):37–56

Taj SA (2016) Application of signaling theory in management research: Addressing major gaps in theory. Eur. Management J. 34(4):338–348.

Tech Wire Asia (2019) China’s social media censorship is effective but disrupts advertisers. Tech Wire Asia, https://techwireasia.com/ 2019/04/is-chinas-social-media-censorship-actually-a-good-thing/.

The Economist (2022) The all-conquering quave. https://www.economist. com/leaders/2022/07/07/whos-afraid-of-tiktok

Thomas LDW, Autio E, Gann DM (2014) Architectural leverage: Putting platforms in context. Acad. Management Perspect. 28(2):198–219.

Thompson G (2003) Hierarchies, Markets, and Networks: A Preliminary Comparison Between Hierarchies and Markets: The Logic and Limits of Network Forms of Organization (Oxford University Press, New York).

Tilson D, Lyytinen K, Sørensen C (2010) Digital infrastructures: The missing IS research agenda. Inform. Systems Res. 21(4):748–759.

Tiwana A (2015) Platform desertion by app developers. J. Management Inform. Systems 32(4):40–77.

Tiwana A, Konsynski B, Bush AA (2010) Research commentary-Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Trabucchi D, Buganza T (2020) Fostering digital platform innovation: From two to multi-sided platforms. Creat. Innov. Management 29(2):345–358.

Tracy SJ (2010) Qualitative quality: Eight “big-tent” criteria for excellent qualitative research. Qual. Inq. 16(10):837–851.

Tschang FT (2021) Platform-dependent entrepreneurs: Participants in an expanding universe of platforms? Acad. Management Perspect. 35(4):696–701.

Ulrich K (1995) The role of product architecture in the manufacturing firm. Res. Policy 24(3):419–440.

Van Alstyne MW, Schrage M (2016) The best platforms are more than matchmakers. Harvard Bus. Rev. https://hbr.org/2016/08/ the-best-platforms-are-more-than-matchmakers.

Van Alstyne MW, Parker GG, Paul Choudary S (2016) Pipelines, platforms, and the new rules of strategy. Harvard Bus. Rev. 2016(April):54–60, 62.

Walsham G (1995) Interpretive case studies in IS research: Nature and method. Eur. J. Inform. Systems 4(2):74–81.

Wang P (2021) Connecting the parts with the whole: Toward an information ecology theory of digital innovation ecosystems. MIS Quart. 45(1):397–422.

Wareham J, Fox PB, Cano Giner JL (2014) Technology ecosystem governance. Organ. Sci. 25(4):1195–1215.

Yang Z (2022) How China’s Biggest Online Influencers Fell from Their Thrones (MIT Technology Review). https://www.technologyreview.com/

2022/06/10/1053598/austin-li-jiaqi-china-biggest-onlineinfluencers-fell/.

Yoo Y, Henfridsson O, Lyytinen K (2010) The new organizing logic of digital innovation: An agenda for information systems research. Inform. Systems Res. 21(4):724–735.

Zhu F, Liu Q (2018) Competing with complementors: An empirical look at Amazon.com. Strategic Management J. 39(10) 2618–2642.

Zucker LG (1983) Organizations as institutions. Res. Sociol. Organ 2(1):1–47.
