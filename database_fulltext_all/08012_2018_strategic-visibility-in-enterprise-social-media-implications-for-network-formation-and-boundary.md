---
otero_id: 8012
otero_key: "N4P6W6C4"
title: "Strategic Visibility in Enterprise Social Media: Implications for Network Formation and Boundary Spanning"
authors: "Wietske Van Osch; Charles W. Steinfield"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1451961"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic Visibility in Enterprise Social Media: Implications for Network Formation and Boundary Spanning

Wietske Van Osch & Charles W. Steinfield

To cite this article: Wietske Van Osch & Charles W. Steinfield (2018) Strategic Visibility in Enterprise Social Media: Implications for Network Formation and Boundary Spanning, Journal of Management Information Systems, 35:2, 647-682, DOI: 10.1080/07421222.2018.1451961

To link to this article: https://doi.org/10.1080/07421222.2018.1451961

![](/api/attachments/N4P6W6C4/fulltext/images/7d65ffbef6db7aaa6479860920e502649111dba5b6384d41ed3fc77cd378dcc5.jpg)

Published online: 15 May 2018.

![](/api/attachments/N4P6W6C4/fulltext/images/58a1842c03d3f9cb76b30025363566a7e5e875c031c14cfa9bfe9d7d2cf4aaa5.jpg)

Submit your article to this journal

![](/api/attachments/N4P6W6C4/fulltext/images/f81f3421d1c9fd1eb659acdd3c8c00f64efa5998217cc68110c1748770f5170b.jpg)

Article views: 13

![](/api/attachments/N4P6W6C4/fulltext/images/118edac14d3bd92d14d411685ca18e001c9e90e45dd749f565222589aae906b7.jpg)

View related articles

![](/api/attachments/N4P6W6C4/fulltext/images/a4035deabff756571b67c37a3c754f8aa5c3a7cb5a9a94d94b6732b748587fbb.jpg)

View Crossmark data

# Strategic Visibility in Enterprise Social Media: Implications for Network Formation and Boundary Spanning

WIETSKE VAN OSCH AND CHARLES W. STEINFIELD

WIETSKE VAN OSCH (vanosch@msu.edu; corresponding author) is an assistant professor in the Department of Media and Information at Michigan State University. She received her Ph.D. in economics (information systems) from the University of Amsterdam’s Business School. Her research work has appeared in the Journal of Management Information Systems, Journal of Information Technology, Information and Management, and leading conferences, including the International Conference on Information Systems. She has received funding from the National Science Foundation and industry for her research on social media. Current research projects involve extensive industry collaborations with several companies, including Steelcase and Leo Burnett.

CHARLES W. STEINFIELD (steinfie@msu.edu) is a professor and former chair of the Department of Media and Information at Michigan State University. He received his Ph.D. in communication theory and research from the Annenberg School for Communication at the University of Southern California. He studies the social and organizational impacts of new information and communication technologies. He is an award-winning author, and editor of 7 books and anthologies and more than 130 articles published in scholarly venues, including Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Organization Science, and others.

ABSTRACT: Effective workgroups engage in team boundary spanning, that is, using communication ties as conduits to critical external resources. The proliferation of enterprise social media (ESM) and the associated increase in visibility of people, content, and interactions, has resulted in a widespread assumption that unlimited visibility improves boundary spanning. Consequently, the ESM literature has generally ignored the sentry functions of teams and failed to examine the possible strategic nature of visibility choices by ESM groups. Using log and content data from 655 ESM-based workgroups at a multinational enterprise, we contribute a deeper understanding of the distinct ways that ESM visibility—bounded or unbounded—is leveraged strategically to evoke diverse network structures, which in turn have implications for distinct boundary-spanning activities. Practically, these findings show that ESM present a unique opportunity for workgroups to simultaneously sustain multiple virtual spaces—with varying levels of visibility—through which they can manage their diverse boundary-spanning goals.

KEY WORDS AND PHRASES: enterprise social media, group-level analysis, knowledge management, network structure, social media, team boundary spanning, teams, visibility, workgroups.

The performance and success of today’s enterprises increasingly depends on the efficiency and quality of their cross-boundary knowledge flows and processes [65, 76]. Cross-boundary knowledge sharing, better known as boundary spanning, has for many decades been a fundamental domain of organizational information management research [6, 87]. It generally refers to the extent to which organizational units and teams are linked to relevant external resources through their communication relationships [87], providing for reputational, informational, and synchronization benefits [6]. Boundary spanning between organizational units, also referred to as team boundary spanning, is considered to be critical to a host of outcomes, including the operational performance of teams [87], the flexibility and innovativeness of goal delivery [6], the transfer of best practices [83], learning [8], new product development [37], and organizational competitiveness, performance, and survival at large [10, 70].

The recent emergence of enterprise social media (ESM) as a new class of organizational information systems has sparked substantial interest among academics and practitioners alike as offering unprecedented opportunities for breaking down knowledge silos in organizations and facilitating more effective and efficient cross-boundary knowledge sharing [28, 45, 57]. By combining a wide range of information sharing and communication functionalities, ESM systems provide many of the capabilities anticipated in earlier work envisioning virtual community knowledge support systems [12]. ESM technologies have proliferated in organizational settings to encourage serendipitous, impromptu, and unstructured knowledge sharing by making it easier to find and engage people with mutual interests and complementary expertise [57] primarily as a function of the communication transparency these tools provide [54]. ESM enables all team members, rather than just gatekeepers, to extend boundary-spanning interactions beyond specific or designated extra-team stakeholders, potentially encompassing the whole of the organization. This has been called the visibility affordance of ESM [85], whereby groups may choose to allow their boundary-spanning attempts and information requests to be visible to anyone in the enterprise and open to any participants to respond. Yet, despite the widespread adoption of ESM, detailed empirical investigations that explore this connection between ESM visibility and the amount and nature of cross-boundary knowledge sharing remain relatively rare [62].

In this study, we seek to advance our understanding of how the strategic use of the visibility affordance of ESM influences the likely connective patterns in ESM groups, with implications for the kinds of boundary-spanning efforts these groups engage in. We therefore pose the following research questions: Do open groups on ESM have different network characteristics than closed ones? Are the types of team boundary-spanning interactions different in open versus closed groups? Is there evidence that group creators choose visibility levels strategically, in order to accomplish particular boundary-spanning objectives?

In addressing these research questions, we investigate whether different levels of visibility are associated with diverse network structures. We further explore whether they also encourage team members to enact distinct kinds of team boundary-spanning interactions. Drawing on the existing literature, we outline three types of boundary-spanning interactions that occur between members of different teams inside an enterprise, including representation, coordination, and general information search [6]. We then develop and test a machine-learning algorithm to facilitate the automatic detection of these activities in ESM posts, all of which have been associated with a range of team and organizational performance benefits [6, 65].

We further provide a novel characterization of the visibility of interactions over ESM that distinguishes between bounded and unbounded visibility rather than considering posts to be visible versus invisible to others. This conceptualization allows us to propose a framework that integrates the disparate views of how the visibility affordance in ESM may be leveraged by groups. This framework considers the impact of the strategic use of visibility on the network characteristics of groups, which are then associated with distinct types of boundary-spanning interactions that occur inside enterprises. We propose that the first type, representation, is more likely to be found in ESM groups that connect to a wider, more diverse range of contacts afforded by unbounded visibility, while the other two types, namely, coordination and information search, are more likely to be found in ESM groups that connect with a narrower, but more specific and densely structured set of contacts afforded by bounded visibility. Although it may initially seem counterintuitive to anticipate greater information search in groups with bounded visibility, as we show later in our review of literature, there are good reasons to expect employees to limit information search requests when viewable by a potentially large and unknown audience.

We test our framework and associated hypotheses on 655 groups registered on the ESM of a large, multinational office solutions manufacturer. We find support for our basic argument that different visibility conditions are associated with different network structures, and network characteristics are, in turn, associated with distinct team boundary-spanning interactions. A preliminary qualitative analysis of the language used by group creators to describe the objectives of the group further suggests that visibility choices may indeed be purposeful and strategic.

Through amalgamating the literature on ESM and boundary spanning, this study contributes to a deeper understanding of how ESMs might transform workplace interactions by demonstrating the influence of the strategic use of group visibility on both the network formation of groups and the types of boundary-spanning interactions they enact. Furthermore, our findings help to move beyond value-laden judgments regarding whether visibility is good or bad and the “ideology of openness” [31] that has characterized much of the ESM literature to date, to a more nuanced approach that suggests that different levels of visibility—bounded versus unbounded —may be leveraged strategically by organizational groups depending on the desired resources a team is intending to obtain. Prior research has failed to examine this possible strategic nature of group-level visibility choices. Therefore, in this study we examine the effect of strategic visibility on boundary spanning as well as the role of network formation as a mediating mechanism.

## Prior Research on Visibility and Enterprise Social Media

The potential advantages of the visibility affordance of ESM have only recently begun receiving attention in the ESM literature, specifically for understanding knowledge sharing inside the enterprise [31, 54, 56, 58, 59]. However, much of this research on the actual ways that organizational participants leverage the visibility affordance for boundary spanning has been sparse and anecdotal. Furthermore, existing research has produced strongly opposing views of the visibility affordance. On the one hand, the majority of ESM studies to date have emphasized the positive effects associated with the enhanced visibility of content and people, including improved meta-knowledge, duplication avoidance, and increased opportunities for recombinant innovation [54, 58]. On the other hand, others challenge this “ideology of openness” [31, 56], emphasizing instead that distinct work objectives of individuals and groups in ESM may require strategic invisibility, such as the creation and sharing of confidential information or knowledge about projects in early stages of development. For example, Kane [45] describes one company where the transparency afforded by the ESM actually hindered collaboration because the prospect of having posts monitored discouraged employees from sharing novel ideas that did not align closely with company norms.

Indeed, much like boundary-spanning interactions before the advent of ESM, groups can elect to constrain the visibility of their boundary-spanning attempts by allowing only designated extra-team stakeholders to interact with members of the team. Early research on team boundary spanning, in fact, identified the need for a “sentry” function in order to filter external inputs and buffer teams from distractions or other problematic information originating in the team’s external environment [4, 6]. More broadly, it has been recognized in the knowledge management literature that effective organizations build an infrastructure that supports not only knowledge acquisition and application processes but also knowledge protection [32]. Finally, research on the dissemination of tacit knowledge has recognized that people may share it openly for fear of giving up their competitive advantage in the organization [80].

Nonetheless, the existing ESM literature has largely emphasized the more open view of the role of visibility, limiting our ability to understand the diverse ways that ESMs may be leveraged as tools for boundary spanning and organizational knowledge sharing in two ways. First, a number of explorations of the visibility affordance focus mainly on the public nature of posts, without consideration of the interactions occurring in private groups. Visibility is important in these closed groups, however, in that even when groups in ESM opt for invisibility—that is, content is only visible for “invited” members and extra-team stakeholders—this still involves a level of visibility not previously afforded in earlier forms of computer-mediated communication inside the workplace. For example, members of the closed group who may only be reading rather than actively contributing to interactions or threads of other invited members still benefit from increased ambient awareness and opportunities for vicarious learning [54], gaining direct knowledge from others’ discussions and indirect knowledge of who knows about particular topics. Second, it limits our ability to integrate both views; different levels of visibility, for example, may be associated with different social network structures, which in turn have implications for knowledge sharing across boundaries. Visible groups are open to the entire organization, and hence are likely to include a more diverse set of participants from other organizational units than closed groups. The connections between individuals, then, may have the characteristics of weak ties [34], in that participants are less likely to know each other, but may also be conduits through which new information and other resources flow to the group [46, 47]. From a network analysis perspective, this implies that visible groups would afford participants a broader range of contacts. On the other hand, closed groups involve only invited participants, usually including members of their unit, team, or project along with selected external employees, hence, visibility of within-group content and interactions is limited to these select individuals. Participants are thus more likely to be connected with each other given prior interactions, resulting in a more densely connected and cohesive network structure characterized by trust [46] among members, which may elicit sharing of confidential or sensitive information.

These diverse network structures are thus likely to support quite different types of boundary-spanning activities based on the strategic motivations of its users, ultimately resulting in the transfer of distinct types of resources. This is consistent with the expectation that Kane [47] proposes, namely that rational actors would use their knowledge about network structure to form connections over social media strategically. Teams that post on open ESM sites may, for instance, be attempting to build support for their project more broadly across the organization without revealing potentially unflattering details, while those who strategically invite external stakeholders to closed groups may engage in boundary-spanning efforts aimed at facilitating coordination of activities across interdependent functions with a “need to know.” Thus, in the remainder of this article, we seek to advance our understanding of how groups strategically use the visibility affordance of ESM.

## Theoretical Background

In what follows, we present three different types of boundary-spanning interactions that have been theorized in previous knowledge management literature. We then describe distinct characteristics of group interaction processes—that is, their network structures—which can be fostered by the strategic choice for bounded and unbounded visibility, respectively, and show how the interaction of visibility choices and network structures are likely to be associated with distinct types of boundaryspanning goals.

Types of Boundary-Spanning Interactions and the Potential Role of ESM

Team boundary spanning—sometimes also referred to as team boundary work or team boundary management—can be defined as a team’s or group’s effort to establish and manage interactions with parties in the external environment that enhance the team and others linked to the team in meeting performance goals [3, 6, 66]. Although the external environment may refer to other actors and teams residing both within and outside of a team’s host organization [66], in this study we focus on intraorganizational boundary spanning given that ESM usually only supports communication among members of the organization. Throughout this article, we focus on such interactions and refer to them as team boundary spanning. Understanding the role of ESM in supporting team boundary spanning is important as these activities are crucial not only to the performance of a focal team but also to the performance, success, and survival of other organizational parties that are interdependent with the boundary-spanning team and the organization as a whole [66, 76, 94, 95, 96].

Given its focus on the importance of communication links to external sources of information [87], team boundary spanning is closely related to popular concepts from social network theory, including bridging or weak ties [35], and structural holes and information brokerage [21]. All emphasize the importance of establishing and managing external linkages as conduits to critical resources—monetary, informational, or social—as well as coordination and reputation benefits [9, 39]. It is important to recognize, however, that not all boundary spanners are brokers [29]; for instance, a group member simply seeking information is not necessarily attempting to broker relationships between extrateam stakeholders and other members of the group.

Also, team boundary spanning is closely linked to the importance of exploration [63]—creating new knowledge from the acquisition of knowledge across intra- or interorganizational boundaries—as established in the innovation and strategic management literature [15, 77]. Hence, although the concepts of team boundary spanning and knowledge sharing are often used interchangeably, information or knowledge transfer does not constitute the full range of interactions between a team and its environment. Rather boundary work encompasses a broader set of activities that are necessary to build support for new products and projects, shape the demands of other organizational parties, and coordinate product development or innovation efforts with other organizational groups [5]. Hence, beyond the establishment of social capital and the transfer of knowledge, team boundary spanning further involves strategic development, workload and project coordination, and the management of interpersonal conflict [64].

The importance of team boundary spanning does not imply that internal team activities and dynamics are inconsequential. Indeed, with increasing boundary-spanning efforts, an increase in within-team coordination and information sharing is necessary to generate the requisite level of trust that enables successful crossboundary interactions [6]. However, in this study, we limit our focus to the use of ESM for team boundary spanning; thus, internal team processes are beyond the scope of this article.

Within the literature on team boundary spanning, three distinct activities have been proposed and validated empirically: representation, coordination of task performance, and general information search [6, 33].<sup>1</sup> This categorization of team boundary spanning emerged from seminal survey work [6] that focused on behaviors and outcomes of these activities for the team as a whole and its members [65]. The work has since been advanced to also understand team boundary-spanning actions at diverse levels of analysis, including teams and intraorganizational networks of multiple teams or actors [64]. Given this background, we next provide a more detailed overview of the primary types of team boundary-spanning activities identified in the prior literature, and consider them from both internal and extra-team stakeholder perspectives.

Representation, also referred to as the ambassadorial function or impression management [6], involves lobbying for the group up the corporate hierarchy in order to evoke favorable impressions and advocate among (senior) managers. Hence, it is a largely vertical form of team boundary spanning. From an internal perspective, given that the core activity of representation is lobbying, the group member engaging in this team boundary-spanning process tends to be a project manager [6]. Similarly, from an external perspective, although representation can occur at all levels, the target actors typically hold greater power than the boundaryspanning actor [6]. This process is crucial for group performance as the creation of a favorable impression among senior management is a prerequisite for obtaining access to key resources, including reputation, legitimization, higher-level commitment, and the financial support needed to facilitate successful product development [33]. This team boundary-spanning process not only is advantageous to the team but also benefits the target actors—that is, senior managers—as they stay informed of a group’s progress. This further supports higher-level planning and resource allocation decisions, which, in turn, can help the broader organization meet external client expectations [11].

Coordination, also referred to as task coordination [6] or intergroup process [64], involves the facilitation of effective decision making and design implementation through cross-boundary strategizing, planning, and evaluation. It is thus a horizontal form of team boundary spanning that centers on the management and negotiation of intergroup dependencies. From an internal perspective, the group members participating in this team boundary-spanning process tend to be general members of the group [6]. Similarly, from an external perspective, it is general members from the organization—rather than (senior) managers—who are more likely to reciprocate coordination attempts by members of the focal group. Coordination is crucial for group performance as it involves the aligning, negotiating, and monitoring of the efforts of individuals—within and outside the group—in order to accomplish individually and jointly determined project goals, such as delivery deadlines. Hence, coordination is essential for the efficiency, effectiveness, innovativeness, and flexibility of goal delivery [68].

General information search, also referred to as scouting or simply information search [6], involves the general scanning of the external group environment in order to gain access to relevant information, knowledge, and expertise. Information search, similar to coordination, is also a largely horizontal form of team boundary spanning. Again, from an internal perspective, general members of the group are more likely than project managers to engage in scouting [6]. From an external perspective, target actors of information search activities are often loosely coupled with the focal group and are general members from the organization rather than (senior) managers [65]. This team boundary-spanning process is crucial for group performance as it enables members to gain project-specific expertise and an understanding of trends, opportunities, and threats in the external environment [39]. Hence, it is this specific boundary-spanning activity that is most closely linked to concepts of knowledge transfer and knowledge sharing.

The emerging literature on ESM has suggested that these enterprise social media platforms—given their informational and social value—may be particularly useful for boundary work [57, 89]. By enabling the locating and accessing of remote information and individuals, ESM are particularly apt for affording the synchronicity required for effective boundary spanning [51]. Indeed, in a review of the potential influence of ESM on common organizational processes, Leonardi et al. [57] emphasize the need to study the implications for boundary work, describing many ways that ESM could facilitate knowledge sharing across department, spatial, geographic, and other types of boundaries. Furthermore, research has found that the use of ESM fosters increased awareness and possibilities for interaction [25] as a function of the “people sense-making” [24] and easy access to new people and expertise [79] enabled by these tools—all of which may be critical antecedents to effective boundary spanning.

We next turn to how the visibility settings of groups may impact the enactment of boundary spanning, primarily by affecting the kinds of connections that can be reached. This analysis is used to help us better predict how employees may leverage the visibility affordance of ESM in diverse ways in order to achieve boundaryspanning objectives.

## The Visibility of ESM Groups and the Mediating Role of Network Formation in Relation to Boundary Spanning

In the context of ESM, visibility has been proposed as the most foundational affordance of this new class of enterprise technologies [85]. Visibility refers to the relative ease with which an ESM user can locate relevant information and individuals within the organization. ESM make regular exchanges between employees visible to third parties [36], which provides not only visibility of the content of interactions between others but also visibility into the communication partners with whom coworkers interact [49, 55]. This so-called hypervisibility enabled by ESM [54] makes it easy for anyone to see what any other person said and to whom [48].

At the group level, a common feature in most ESM is the ability to select a visibility setting when creating a place to host team posts (e.g., blogs or discussions). This is a critical but largely overlooked feature in the ESM literature, in that the same visibility affordance may encourage both bounded and unbounded visibility. That is, when users establish groups in ESM, they are prompted to select the visibility level of their group, which could be either to open up the group to the entire enterprise or to limit the visibility to a select number of members and extrateam stakeholders (i.e., only to those invited to join the ESM group).

Visibility, in this context, encompasses both dimensions of transparency and permeability. That is, for groups with unbounded visibility, their content is visible to outsiders (i.e., transparency), and these outsiders can usually simultaneously contribute to the group by posting original content or engaging with existing content already generated by the group (i.e., permeability). For groups with bounded visibility, on the other hand, “outsiders”—that is, those not invited to contribute— can neither consume content generated by the group (i.e., lack of transparency) nor contribute content to the group (i.e., impermeability). Nonetheless, ESM still affords increased visibility of content to the invited members and extra-team stakeholders that have been invited to the group space when compared to previous forms of computer-mediated communication in the workplace. All members are able to see the conversations occurring between others, even if they are not part of a conversation. Hence, using the term “invisibility”—as has been proposed by other ESM scholars [31]—may be misleading.

Although most of the ESM literature to date has focused on the positive effects of visibility for social capital formation and knowledge sharing, recent work suggests there are reasons that employees may not be willing to contribute or retrieve information on ESM [56], and even argues that visibility could actually discourage employees’ willingness to post information due to concerns over loss of control, job security, or accidental knowledge spillovers [31]. Hence, although overall visibility appears to have a positive effect on boundary spanning in terms of rendering visible the interests and expertise of potentially unknown others residing elsewhere in the organization, in certain cases restricting visibility to only a select number of extrateam stakeholders may be beneficial.

We propose that the strategic use of the visibility of a group in ESM influences the types of boundary-spanning activities that are enacted by the group through its impact on structural aspects of the network that it supports. Social media researchers have explored network features that shape information diffusion [81]. A wellestablished body of research provides insights into the network characteristics and structures that facilitate knowledge sharing and transfer in the organization [20]. This research suggests that various network characteristics and structures can affect the transfer of resources across organizational boundaries and help us explain the mechanisms by which teams are able to benefit from resources residing elsewhere in the organization [37, 76]. System features can shape the kinds of information flows that occur over an ESM; a public post has a chance to be seen by anyone in the organization regardless of their location, functional area, or organizational unit, while posts on private groups can only be seen by its members.

Visible groups are open to the entire organization, and hence are likely to include a more diverse set of participants from organizational units other than closed groups. Thus, from a network perspective, visible groups would afford participants a broader range of contacts, which may be less likely to know each other—that is, display characteristics of weak ties [34] and thus may act as conduits through which novel information and other resources flow to the group [37, 76]. On the other hand, closed groups involve only invited participants, usually including members of their unit, team, or project along with selected external employees, hence, visibility of within-group content and interactions is bounded to these select individuals. Thus, from a network perspective, groups characterized by bounded visibility afford more cohesive network structures encompassing individuals who know each other from previous interactions— that is, display characteristics of strong ties—and thus may create ideal opportunities for coordination, negotiation, or the sharing of sensitive information as a result of the trust, shared identity, shared understanding, and reciprocity norms that exist in these cohesive networks [1, 9, 14, 26, 27, 40, 69, 86, 88].

Hence, understanding the various network characteristics that stem from the selected level of visibility of groups in ESM is crucial for explaining the types of boundary-spanning activities that are likely to occur in ESM. Thus, we turn now to discussing the distinction between bounded and unbounded visibility in ESM and subsequently address the issue of how visibility may trigger distinct network characteristics, which in turn will differentially affect the types of boundary-spanning activities enacted by groups in ESM.

Unbounded Visibility, Network Range and Representation Activities: Unbounded visibility describes a group in which conversations between and posts by the members can be seen by any user of the ESM. Because of the group’s unbounded visibility, nonmembers of the group are not only aware of the group’s existence, purpose, and members but also can engage with the content of the group as well as become a member without the need for an invitation or request to join the group. By opening up the content of the group to anyone else in the organization, it becomes easier and more likely for employees elsewhere in the organization to interact with members of the group, fostering more external ties that span structural holes. That is, the communication links afforded by unbounded visibility are likely to result in the establishment of novel social connections with previously unknown others inside the organization [18] and thus a general broadening of the network range of a group. Furthermore, from a network perspective, because visible groups are open to the entire organization, the connections between individuals are likely to display characteristics of weak ties [34], in that participants are less likely to know each other. As each participant in the group brings in his or her own unique set of connections, groups will include a more diverse set of participants from other organizational units than closed groups. Thus, beyond the subsequent benefits that weak ties may have for providing groups with distinct and unique resources, a more direct benefit of weak ties that characterize the relations between participants in open groups is the greater network range that emerges. Therefore, we propose:

Hypothesis 1a: Groups with unbounded visibility will display greater network range than groups with bounded visibility.

Furthermore, given the organization-wide transparency of groups characterized by unbounded visibility, these groups are the ideal stage for the types of selective selfpresentational and lobbying activities that constitute representation [6]. Studies of individual social media behavior abound with examples of selective self-presentation [85, 92] through the manipulation of information for creating more favorable impressions. Furthermore, the online community, open source software, and usergenerated content literatures have also offered substantial evidence of attention currency and reputational benefits acting as key drivers of individuals’ public contributions and displays of expertise [19, 60].

Researchers of e-mail and other text-based modes of computer-mediated communication have found that impression management motivations often drive technology use and result in individual strategic choices to reveal or conceal information [13]. Similarly, within the enterprise setting, groups that aim to engage in impression management activities regarding team performance, seek to obtain maximum attention [38], therefore, showcasing successes in bounded space would limit the audience, whereas in groups with unbounded visibility, the entire organization becomes the audience.

As representation involves keeping others informed and persuading them that the group’s activities are valuable and should be supported, these activities usually “include opening up communication channels” [4, p.10]. This increased transparency is aimed at molding the beliefs of others about the group and thus at changing the external world. Moreover, as representation is a primarily vertical activity, unbounded groups are associated with a greater possibility of senior managers discovering such group achievements, thereby increasing the likelihood of obtaining monetary or legitimization support. Indeed, inviting senior managers to be part of a relatively bounded group space would be inappropriate, so the broad reach of groups characterized by unbounded visibility increases the serendipity of information discovery including by higher-ranked target audiences. An exploratory study of ESM-based boundary spanning shows that organization-wide visibility may be useful for enacting representation given the broad and diverse awareness it generates for team accomplishments [89, 90]. Therefore, we propose:

Hypothesis 1b: Groups with unbounded visibility will display more representation activities than groups with bounded visibility.

While the unbounded visibility of a group may affect the amount of representation activities directly, the broader network range that evolves in unbounded groups may further mediate the relationship between visibility and boundary-spanning activities of a representational kind. This mediating role of network range and hence its direct effect on representation is the focus in what follows.

Network range—relationships that span diverse networks and knowledge pools [37,76]—gives teams access to diverse audiences that may be the source of important resources. Although the unbounded visibility makes it easier and more likely for nonmembers to interact with members of the group, thereby resulting in greater network range, the unbounded nature of a group does not automatically imply greater network range. For instance, not all topics will go viral and attract organization-wide attention. Nonetheless, members will choose visibility with the goal of maximizing network range.

When unbounded groups develop a broad network of external ties, group members are more likely to frame their initial request in such a way that a diverse audience of recipients can understand the request [16, 76]. The primary benefit of network range will be most evident in the context of representation activities. For representation activities to be enacted successfully—that is, yield monetary or legitimizing resources—these vertical requests need to reach higher-level managers. If an open group does attract many external members, the resulting network range should display a greater diversity of audiences, including greater hierarchical diversity. Thus, network range allows for greater opportunities for ambassadorial and impression management activities (i.e., representation) to reach the higher-level audiences these are intended to reach [6]. Therefore, we propose:

Hypothesis 1c: The network range of a group will positively mediate the relationship between the unbounded visibility of the group and the amount of representation activities enacted by the group.

Bounded Visibility, Network Cohesion, and Coordination and Information Search Activities: Contrary to groups with unbounded visibility, groups that limit their visibility to a select set of extra-team stakeholders—that is, groups with bounded visibility—are those whose members and content are only visible to those who have been invited to the group. The unbounded visibility therefore has two direct implications for network formation. First, when groups are based on invited membership, participants are more likely to be connected with each other from prior interactions. That is, the ties between members of the group are likely to be strong [34] and dense [45].

Second, because of the group’s bounded visibility, the evolving relationship building that is ongoing within the group is unlikely to be disrupted from outside the group. The lack of interruptions fosters a shared memory system, strong coordination norms, shared identity and understandings, psychological safety, as well as trust and mutual respect among members of the closed group [9, 26, 27, 40, 69]. Furthermore, because the group content is invisible to nonmembers, the privacy of conversations in the group may lead to greater sharing of personal information and the development of strong interpersonal relationships [57, 90], which will further reinforce the cohesiveness of the group. The context of bounded visibility is thus more likely to lead to network cohesion among the members of the group. Therefore, we propose:

Hypothesis 2a: Groups with bounded visibility will display greater network cohesion than groups with unbounded visibility.

Beyond the effect of bounded visibility on network cohesion, groups that provide a strong demarcation through restricting visibility to select others have their own benefits for boundary spanning, in particular in the context of coordination and information search activities for two reasons.

First, by carefully selecting the extra-team stakeholders that are most critical to the team’s coordination, not only do groups increase the willingness to share sensitive information and coordinate, but transaction costs of coordination are also likely reduced. Research has shown that when people cannot see what others do, or when, with whom, and how they do it, coordination suffers [23] and work duplication occurs [53]. Therefore, controlling the audience and strategically inviting extra-team stakeholders is required for effective coordination, but further ensures that coordination costs are minimized by keeping everybody informed and involved.

Second, in their original work explaining the various boundary-spanning functions of teams, Ancona and Caldwell [5] highlight the importance of sentry functions— that is, controlling from whom groups will accept input and how much or in what form. Sentry activities help to protect the group from external interruptions and minimize distraction [4], which can support coordination. Indeed, extant research finds that in the context of interpersonal relationships, individuals leverage technology strategically to control the flow of social information in face-threatening situations [71]. Similar strategic choices would underpin concerns for coordination that will often involve the revealing of potential embarrassing information such as falling behind on project schedules or budgets. Thus, we propose:

Hypothesis 2b: Groups with bounded visibility will display more coordination activities than groups with unbounded visibility.

Considering the classic way of viewing weak ties as conduits to novel information [34, 46], information search may be expected to be greater in open groups. However, unrestricted or public attempts for information search could be revealing and are generally associated with lower expectations of relevant information provision [50]. Therefore, restricting information search attempts to a limited audience of individuals who are more likely to possess the requisite expertise not only increases the expectations of yielding the desired knowledge but also avoids accidental knowledge leaks or spillovers and avoids vulnerability

The greater occurrence of information search activities in groups characterized by bounded visibility does not imply that no such attempts will occur in groups characterized by unbounded visibility. In fact, for crowdsourcing-type information search requests—where the person asking the question does not know who might hold the answer or relevant information—posting a question in a group with unbounded visibility may be more useful [2]. However, similar to coordination, the willingness of groups to share sensitive information—such as early stage ideas— or ask sensitive questions—for instance, questions that may reveal lack of knowledge in a particular domain—is likely to increase when their audience is restricted through the careful selection of extra-team stakeholders [74]. Thus, we propose:

Hypothesis 2c: Groups with bounded visibility will display more information search activities than groups with unbounded visibility.

While the bounded visibility of a group may affect the amount of coordination and information search activities and network cohesion of the group directly, the stronger network cohesion that evolves in bounded groups may mediate the relationship between visibility and boundary-spanning activities of a coordination and information search nature. This mediating role of network cohesion and hence its direct effect on coordination and information search is the focus in what follows.

Network cohesion—the extent to which the group attains full connectedness or maximum network density [1, 75]—provides groups with strong relational benefits. Although the bounded visibility helps to shield groups from external interruptions and thus makes it more likely for team members to develop strong cohesive relationships, the bounded nature of a group does not automatically imply greater network cohesion. For instance, there may be tensions in the group that undermine the repeated interactions that are required to form dense networks. Nonetheless, members will strategically choose bounded visibility with the goal of minimizing interruptions and maximizing the likelihood for network cohesion to emerge.

When unbound groups develop a strong, cohesive network of relationships, these groups provide the ideal setting for engaging in coordination and information search activities [1, 86, 88] for two reasons. First, network cohesion results in strong cognitive and expressive benefits. From a cognitive perspective, groups with strong network cohesion display greater solidarity, trust, and reciprocity norms, and therefore are ideally positioned to pursue collective goals [1, 86, 88]. Additionally, the informal socializing interactions that take place in groups characterized by strong network cohesion also result in expressive benefits [72, 82, 86], which help to evolve single-resource into multiple-resource ties [74], thereby supporting the informational and coordination needs simultaneously.

Second, as both coordination and information search activities have high levels of vulnerability and uncertainty associated with them, visibility alone—without dense interaction patterns between the members of the group—may not provide the requisite levels of trust [40]. Indeed, it is only when strong social cohesion emerges as a result of the group being shielded off from the rest of the organization, that cooperative norms and a greater willingness to share sensitive knowledge and information emerges [76]. Cooperative norms are critical because they help to avoid a potentially destructive side effect of boundary spanning, namely, competition between members of different teams and units that would restrict the transfer of resources between them [7, 76, 83]. Therefore, we propose:

Hypothesis 2d: The network cohesion of a group will positively mediate the relationship between the bounded visibility of the group and the amount of coordination activities enacted by the group.

Hypothesis 2e: The network cohesion of a group will positively mediate the relationship between the bounded visibility of the group and the amount of information search activities enacted by the group.

## Theoretical Model

Our theoretical framework (Figure 1) summarizes our arguments about the relationship between the strategic visibility of ESM groups and their network characteristics as well as the direct and mediated effect of this visibility choice on the types of boundary-spanning activities—representation, coordination, and information search —enacted by ESM groups.

![](/api/attachments/N4P6W6C4/fulltext/images/2abbbe1c94626789b01886d2d3a194e0b093cfa53e9423d9c1ed4a5863ca87dd.jpg)  
Figure 1. Proposed Research Model

## Research Setting and Methodology

To test our hypotheses, we captured the content and interactions formed by 655 groups by using the system log data of the identified ESM. A total of approximately 6,500 discussion threads were collected from across 300 groups with unbounded visibility and 355 groups with bounded visibility.

The measurements for the constructs are derived from the organizational records embedded in the ESM. For the operationalization of the dependent variables, that is, representation, coordination, and information search, we developed a machinelearning algorithm to automatically delineate the types of boundary-spanning requests that are made by groups as will be further discussed below. For the independent variables we calculated basic network measures (i.e., network range and cohesion) by using the log data from the ESM as follows.

## The Case Organization

Our case organization (hereafter referred to as Global Deskcorp, a pseudonym, as are all names in this article) is a worldwide provider of workplace furnishings, products, and services. Global Deskcorp has approximately 10,000 employees around the world and is headquartered in the United States with offices and divisions in nearly 40 countries in North and South America, Europe, Africa, Asia, Oceania, and the Middle East.

Global Deskcorp’s international growth and expansion in the past decades has been realized through a number of acquisitions of existing furnishing companies around the world, thereby further highlighting the potential disconnect and the heightened need for effective interteam boundary spanning between the organization’s many dispersed teams.

In March 2012, Global Deskcorp launched an ESM tool based on the Jive Platform.<sup>2</sup> Jive is a provider of corporate social technologies that assist business connections, communications, and collaborations among employees by providing a platform offering built-in support for group chat, group blogging, social networking, social bookmarking, telephony integration, and strong security. Jive’s customer base includes many multinational corporations and global institutions, including Nike, Hewlett-Packard, T-Mobile, and the World Bank.

Product development and client consulting at the case organization is provided through global teams that rely on a multiplicity of information and communications technologies (ICTs) for collaboration, including e-mail, GoogleDocs, MSN, Sharepoint, and Skype. With the introduction of the ESM—which offers a large number of communication functionalities—the technology providers within Global Deskcorp hope to offer an umbrella tool that can better support intraorganizational communication and collaboration and potentially replace the plethora of tools currently available to teams, thereby serving as a single intrateam and interteam knowledge repository. Following the ESM global launch in March 2012, adoption and use has grown substantially, with a total user base of approximately 10,000 users as of this writing. From the 10,000 unique users in Inspire, a pseudonym for the ESM system, 91 percent (i.e., over 9,000 unique users) are members of groups and thus participate in group discussions and activities via the ESM.

## Data Collection and Sample

To test our hypotheses, we collected data from 655 groups over a period of two years, resulting in a total data set of 2,029 discussions and 6,500 discussion threads. We conducted the analysis on 655 groups, including 300 groups with unbounded visibility and 355 groups with bounded visibility.

We first looked for differences between the groups in base characteristics and found that groups with unbounded visibility, on average, were statistically larger (average of 27 versus 12 group members) and created more content overall (average of 61.3 versus 37.9 pieces of unique content created).<sup>3</sup>

For the purpose of this study, we focused on the content within discussion forums only as these were the most externally oriented spaces of groups, and thus most likely to be used for purposes of team boundary spanning. Data collection was completed in two phases. First, we collected all content data available in the system to detect the types of boundary-spanning activities enacted by the two group types. Second, all social network and log data were collected to compute the independent variables.

## Operationalization of Variables

Dependent Variables: Boundary-Spanning Activities: We examined three types of boundary-spanning interactions—representation, coordination, and information search—as the main dependent variables, all three of which are operationalized as count variables at the group level. Representation refers to the number of instances in which boundary-spanning attempts from the group involve ambassadorial or impression management activities. The variable thus measures the total count of instances of representational attempts across all content from the group. Coordination refers to the number of instances of boundary-spanning requests from the group that focus on managing and negotiating project schedules and deadlines. The variable thus measures the total count of instances of coordination attempts across all content from the group. Information search refers to the number of boundary-spanning requests from the group focus on obtaining relevant knowledge and expertise. The variable thus measures the total count of instances of scouting attempts across all discussion forums associated with the group.

The variables were computed through a machine-learning algorithm, which involved various stages of development. In the first stage of algorithm development, three graduate students were trained to perform manual coding of a subset of all content data from the 655 groups to ensure the reliable development of the machinelearning algorithm. The students were asked to assign the various posts to categories reflecting the type of boundary-spanning activity each contained (or lack thereof). Coding was preceded by an elaborate training session to familiarize the coders with the coding manual and the coding scheme.

The coding manual included five coding categories: three categories for each of the three boundary-spanning activities—representation, information search, and coordination. Furthermore, posts that did not fall into any of these three categories were characterized as two other types of activities: either work-related other or nonwork related other (see also Table 1 below).

Following the training, the coders were supervised in the independent coding of 14 percent of the content to compute interrater agreement. An initial interrater agreement of 89.6 percent with a corresponding .71 Cohen’s kappa (i.e., substantial agreement; cf. [52]) provided confirmation of coding scheme validity and coding process reliability.

Following the reconciliation of differences, in the next stage, the manually coded data were used to create an algorithm for automated text classification. The problem of text data classification belongs to the area of natural language processing, which is one of the most popular applications of machine learning. Compared to machinelearning problems that deal with numerical data, text data mining and classification is more tedious.

In this study, we used a support vector machine (SVM) learning algorithm to develop the prediction model. A support vector machine is a supervised learning algorithm. The idea of this algorithm is to construct a (set of) hyperplane(s) in a high dimensional space, which can be used to separate data samples belonging to different classes. The hyperplane chosen should have the largest distance to the nearest training data points from different classes as a larger margin will lead to lower generalization error.

SVM is particularly well-suited for text categorization for a number of reasons [44]. For example, text data have many features with each unique word as a feature, and SVM deals well with high-dimensional data since SVM offers overfitting protection. Text data, after being processed, will also generate a sparse matrix, and SVM is well-suited for sparsity.

Although the original SVM algorithm was invented in 1963 as a linear model, a kernel trick was later introduced to be applied to nonlinear classifiers [17]. In this project, we applied a sigmoid kernel function in the nonlinear classification model, which was determined using cross validation by comparing the performance to other kernel functions including linear and radial basis functions (RBFs).

In the process of training the nonlinear classifiers, the two best-performing ones were maintained for the categorization of the entire data set. As a result, each post in the data was classified by both of the classifiers. In 93.6 percent of cases, the two classifiers agreed in terms of labeling, thus enhancing our confidence in the accuracy of predictions. However, in the few cases where classifiers disagreed, both labels were assigned. It is for this reason that the distribution row in Table 1 adds up to 106.8 percent. That is, 6.8 percent of all posts received two labels—for example, both representation and information search. The overall accuracy of tenfold cross validation of training samples for the boundary-spanning algorithm is 86.2 percent.

For each type of boundary-spanning interaction, a group score was created by taking the sum of all occurrences across all the discussion forums associated with a single group. Table 1 presents the keywords and example sentences for each type of boundary-spanning interaction. The boundary-spanning scores at the group level were further normalized according to the two control variables, group size and content creation, listed in Table 2.<sup>4</sup>

Independent Variables: Group Visibility: Visibility is operationalized as a dichotomous variable reflecting the existing visibility settings of the group afforded to users by the system. The ESM has inherent mechanisms for controlling group visibility. Groups with unbounded visibility allow anyone to read and write, regardless of membership of the group. For groups with bounded visibility, not only is reading or writing the sole prerogative of members and invited extra-team stakeholders, but also these groups are unsearchable in the system, meaning their existence in the ESM is unknown to anyone who has not been invited to the group.

Given our focus on the role of visibility on boundary-spanning interactions, we focus on a comparison of these interactions in groups with bounded versus unbounded visibility. We validated that group visibility settings are determined upon the creation of the group space and are not altered afterward, confirming that group visibility is likely a strategic choice that precedes both the network characteristics and the nature of the boundary-spanning interactions that unfold subsequently.

Network Range: Our indicator of network range is betweenness centrality, which we computed using R-statistical package and network data from the ESM. Betweenness centrality refers to the number of shortest paths connecting other nodes in the entire network that pass through a particular individual [46]. A path (or link) was operationalized using the system feature allowing a user to “follow” another user. We considered user A following user B (and/or vice versa) as the existence of a link between the two, and had this data from system logs for the entire user base of the ESM. Betweenness centrality is thus a function of the path distance—that is, geodesic—between actors in the network. In computing individual betweenness centrality scores, we further limited our calculation to those network paths that originate from group members and connect them to individuals from outside the group only. By doing so, individuals who are high in betweenness centrality provide rapid access to nonequivalent contacts and nonredundant knowledge and information [20, 30, 84]. To calculate a single betweenness centrality score for each group in our data set, we averaged the betweenness centrality scores of all individual members of the group in order to control for differences in group size, in particular since open groups tend to be larger than closed groups. Higher betweenness scores at the group level thus indicate groups where members have greater bridging connections to organizational members residing outside the group.

Table 1. List of Discriminatory Keywords Used to Code Types of Boundary-Spanning Interaction and Examples

<table><tr><td>Categories</td><td>Representation</td><td>Coordination</td><td>Information search</td><td>Work-related other activity</td><td>Nonwork- related other activity</td></tr><tr><td>Distribution (%)</td><td>19.05</td><td>19.88</td><td>35.05</td><td>11.95</td><td>21.05</td></tr><tr><td>Example</td><td>Here is a great video showing the work of our team in Vodafone&#x27;s new workplace.</td><td>OK, CDC folks, the cancellation of the innovation center meeting threw us a little curve ball, but here&#x27;s the revised planning.</td><td>Has anyone worked on an innovation center that they could share?</td><td>The Global Deskcorp interns had the opportunity to participate in Chicago yesterday. It was great to see the Global Deskcorp show so full and have such an exciting buzz around it.</td><td>Have you hopped on a bike lately??? If so how long and where did you ride?</td></tr><tr><td>Most indicative words</td><td>Show, success, embrace, support.</td><td>Calendar, meeting, schedule, poll.</td><td>Help, solve, question, suggestion.</td><td>Excluded from further analysis.</td><td>Excluded from further analysis.</td></tr></table>

Table 2. Summary of Dependent and Independent Variables

<table><tr><td>Variable</td><td>Type</td><td>Definition</td><td>Descriptive measures</td></tr><tr><td>Visibility</td><td>IV</td><td>The extent to which a group opens itself up to all external members or a limited set of external members inside the organization</td><td>Unbounded Visibility Groups (0) Count: 300 Bounded Visibility Groups (1) Count: 355</td></tr><tr><td>Network Range</td><td>IV; Continuous</td><td>Network range was computed from the betweenness centrality scores of individual group members. To calculate a single betweenness centrality score for each group in our data set, we averaged the betweenness centrality scores of all individual members of the group.</td><td>Ave: 0.477 Std. dev.: 0.421 Min: 0 Max: 2.058</td></tr><tr><td>Network Cohesion</td><td>IV; Continuous</td><td>Network cohesion was measured by the extent to which each group member is directly connected to each other group member outside of group membership. This individual score was then averaged to obtain a cohesion score at the group level.</td><td>Ave: 0.340 Std. dev.: 0.293 Min: 0 Max: 1</td></tr><tr><td>Representation</td><td>DV, Count</td><td>The lobbying for the team up the hierarchy to create favorable impressions among senior managers.</td><td>Ave: 3.905 Std. dev.: 6.931 Min: 0 Max:22</td></tr><tr><td>Coordination</td><td>DV, Count</td><td>The facilitation of effective decision making and design implementation through cross-boundary strategizing, planning, and evaluation.</td><td>Ave: 4.110 Std. dev.: 5.772 Min: 0 Max: 39</td></tr></table>

<table><tr><td>Information Search</td><td>DV, Count</td><td>The general scanning of the external team environment to gain access to relevant information, knowledge, and expertise.</td><td>Ave: 7.193Std. dev.: 27.11Min: 0Max: 129</td></tr><tr><td>Group Size*</td><td>Control, Continuous</td><td>The total number of members in the group.</td><td>Ave: 18.98Std. dev.: 32.98Min: 2Max: 448</td></tr><tr><td>Group Content Creation*</td><td>Control, Continuous</td><td>The total number of unique pieces of content (including discussion boards, blogs, documents, and ideas) created by the group.</td><td>Ave: 48.65Std. dev.: 117.81Min: 0Max: 1,619</td></tr></table>

<sub>reation</sub> <sub>by</sub> <sub>the</sub> g<sup>roup</sup>. <sup>\*control</sup> <sup>v</sup> 6.510;
p = 0.011) than invisible groups. Therefore, the dependent variables were normalized to control for preexisting differences in group size and the amount of Notes: Mean comparisons showed that visible groups displayed significantly larger group sizes (F = 38.330;
p = 0.000) and significantly greater content creation (F =

Network Cohesion: Our indicator of cohesion is constructed from interaction data extracted from the system log data. Previous measures of network cohesion have relied on similar quantitative, interaction-based approaches to measuring cohesion [76, 84]. In line with previous studies, our measure of network cohesion is network density [76, 84]. We measure network density following the approach of Wasserman and Faust [93], where density is the proportion of possible ties that are present between members of a group, that is, it measures the extent to which each member of a group maintains active direct connections to all other members of the group via the ESM. However, because active connections (as a result of group membership) inside the group are to be expected, we restricted our calculation of density to those ESM connections between group members that occurred outside of the group space, for example by following them and their content. To calculate a single network density score for each group in our data set, we averaged the scores of all individual members of the group. Network cohesion at the group level can take any value between 0 and 1, where 0 indicates a group with no density (i.e., none of the group members are directly connected as friends/followers within the ESM and are only connected through membership in the group) and 1 indicates maximum density (i.e., each member of the group is directly connected with each other member in the group). Table 2 summarizes the operationalization of dependent and independent variables.

## Model Specification and Data Analysis

We conducted our analyses by using R-statistical package. All three dependent variables are count variables that are heteroskedastic (i.e., the variance is not constant but depends on the value of the estimate itself) and bounded by zero.<sup>5</sup> To remedy this situation, we used zero-inflated Poisson regression and modeled the dependent variable as a Poisson-distributed variable. To conduct data analysis, we entered the data into Excel and then imported it into the LME4 statistical package in R, which is mainly preferred for its ability to support zero-inflated Poisson regression analysis [42, 61]. Per our hypotheses, all independent and dependent variables in our Poisson regression model are at the group level.

## Results

## Preliminary Qualitative Exploration of the Strategic Nature of Visibility Choices

Our theoretical model is based on the assumption that the choice for bounded or unbounded visibility is a strategic one that is motivated by a group’s desired outcomes in terms of group goals. Although the theory section of this study provided support for this assumption, our first step in the analysis encompassed a preliminary qualitative exploration of the explicit goals of groups as communicated through their group descriptions on ESM. Thus, in order to provide some initial insights into whether the choice for a visibility level is strategic, we crawled all the one-sentence group descriptions from the 655 groups in our data set. Specifically, when the creator of a group sets up the group space, in addition to selecting a visibility level, he or she is also required to create a one-sentence description of the purpose of the group. Using these purpose descriptions, we then extracted the keywords most commonly used and retained only those keywords that were unique to each type of group (i.e., bounded versus unbounded). These keywords are provided in Table 3.

As shown by the bolded words in each list, the choice of bounded versus unbounded visibility does appear to be associated at the outset with strategic motivations for the kinds of interactions that the group’s initiator plans to encourage. The description of bounded groups often contained words that are suggestive of coordination and information search boundary-spanning purposes, including words like collaboration, communication, sharing, knowledge, documents, private, secret, repository, and strategy. On the other hand, several common words used on the unbounded group descriptions are more suggestive of representation purposes, including news, updates, experience, company, management, and post. This lends credence to the notion that groups understand what ESM visibility can potentially afford—namely, representation—and direct boundary spanning posts on the ESM with this in mind.

The Relation Between Unbounded Visibility, Network Range, and Representation Activities

To test for H1a, we ran an independent sample t-test for examining the effect of unbounded visibility on network range. The results show that groups with unbounded visibility display significantly broader network range $( t = 7 . 9 8 ; p =$ .000) than groups with bounded visibility. The results support H1a, implying that groups with unbounded visibility have greater network range than groups with bounded visibility.

To test for H1b, we ran a zero-inflated Poisson regression for the direct effect of unbounded visibility on representation, in what we call the direct model (see

Table 3. Results from a Preliminary Qualitative Analysis of Group Goals and Strategic Visibility

<table><tr><td colspan="2">Group Purpose Keywords—Groups with Bounded Visibility</td><td colspan="2">Group Purpose Keywords—Groups with Unbounded Visibility</td></tr><tr><td>coe</td><td>myhr</td><td>account</td><td>practices</td></tr><tr><td>collaboration</td><td>page</td><td>based</td><td>product</td></tr><tr><td>communication</td><td>private</td><td>committee</td><td>products</td></tr><tr><td>content</td><td>repository</td><td>company</td><td>provide</td></tr><tr><td>dealer</td><td>secret</td><td>customer</td><td>quality</td></tr><tr><td>development</td><td>services</td><td>customers</td><td>related</td></tr><tr><td>documents</td><td>set</td><td>discuss</td><td>software</td></tr><tr><td>emea</td><td>sharing</td><td>employees</td><td>things</td></tr><tr><td>finance</td><td>space</td><td>experience</td><td>topics</td></tr><tr><td>focus</td><td>spark</td><td>lean</td><td>und</td></tr><tr><td>knowledge</td><td>strategy</td><td>management</td><td>updates</td></tr><tr><td>leadership</td><td>test</td><td>new</td><td>welcome</td></tr><tr><td>ll</td><td>tools</td><td>news</td><td>worklife</td></tr><tr><td>make</td><td>use</td><td>people</td><td>world</td></tr><tr><td>marketing</td><td></td><td>post</td><td></td></tr></table>

Note: Words in bold are reflective of boundary-spanning intentions.

Table 4). The results show that groups with unbounded visibility display significantly higher rates of representation activities than groups with bounded visibility (B $= . 2 7 5 ; p = . 0 0 0 )$ . Furthermore, to test the mediating relationships hypothesized in H1c, we ran a Poisson regression for the effect of network range to representation in the presence of visibility, which shows that network range is strongly significant (B $= . 3 3 9 ; p = . 0 0 0 )$ . However, visibility loses its significance in the presence of network range $( B = . 0 1 2 ; p = . 8 7 0 )$ , thus showing that the relationship between visibility and representation is fully mediated by the role of network range as shown in Table 4 and Figure 2.

Table 4. Results of t-test and Zero-Inflated Poisson Regressions for H1

<table><tr><td></td><td>Mean (Visible/Invisible)</td><td>Std. dev.</td><td>t</td><td>Sig.</td></tr><tr><td rowspan="2">Unbounded Visibility &gt; Network Range</td><td>.637/.379</td><td>.413/.412</td><td>7.98</td><td>.000</td></tr><tr><td>Median</td><td>Std. error</td><td>B</td><td>Sig.</td></tr><tr><td>Direct Model: Unbounded Visibility &gt; Representation</td><td>.328</td><td>.043</td><td>.275</td><td>.000</td></tr><tr><td>Mediated Model: Unbounded Visibility &gt; Representation</td><td>.328</td><td>.077</td><td>.012</td><td>.870</td></tr><tr><td>Mediated Model: Range &gt; Representation</td><td>.361</td><td>.082</td><td>.339</td><td>.000</td></tr></table>

![](/api/attachments/N4P6W6C4/fulltext/images/d0af731b78cf56cc5d2d37909bb6f52a37a1c8582b452dbac9955a0612da34ff.jpg)  
Figure 2. A Mediated Model of Representation Activities  
Note: Visibility has been reverse-scored in this figure (and analysis) so that 1.00 is a group with unbounded visibility and 0.00 a group with bounded visibility.

## The Relation Between Bounded Visibility, Network Cohesion, and Coordination and Information Search Activities

To test for H2a, we ran an independent sample t-test to examine the effect of bounded visibility on network cohesion. Groups with bounded visibility display significantly higher levels of network cohesion $( t = 6 . 8 7 ; p = . 0 0 )$ than groups with unbounded visibility. The results support H3, implying that groups with bounded visibility have greater network cohesion than groups with unbounded visibility.

To test for H2b and H2c, we ran zero-inflated Poisson regressions for the direct effects of bounded visibility on coordination and information search. The results show that—in isolation—groups with bounded visibility display significantly higher rates of coordination activities $( B = . 2 3 2 ; p = . 0 0 0 )$ and information search activities $( B = . 2 1 8 , p = . 0 0 0 )$ than groups with unbounded visibility (see Table 5).

Furthermore, to test for H2d and H2e, we ran zero-inflated Poisson regressions for the effects of network cohesion on coordination and information search in the presence of visibility to test for mediation. The results show that groups with strong network cohesion, enact higher numbers of coordination activities $( B = 2 . 2 3 2 , p = . 0 0 0 )$ and information search activities $( B = 4 . 1 2 7 , p = . 0 0 0 )$ . In both instances, bounded visibility continues to be a significant predictor of coordination $( B = . 6 2 9 ; p = . 0 0 0 )$ and information search $( B =$ $. 4 7 0 ; p = . 0 0 0 )$ , thus showing that the relationship between visibility and representation is partially mediated by the role of network range as shown in Table 5 and Figure 3.

Table 5. Results of t-test and Zero-Inflated Poisson Regressions for H2

<table><tr><td></td><td>Mean(Visible/Invisible)</td><td>Std. dev.</td><td>t</td><td>Sig.</td></tr><tr><td rowspan="2">Bounded Visibility &gt; Network Cohesion</td><td>.236/.387</td><td>.201/.334</td><td>6.87</td><td>.000</td></tr><tr><td>Median</td><td>Std. error</td><td>B</td><td>Sig.</td></tr><tr><td>Direct Model: Bounded Visibility &gt; Coordination</td><td>.499</td><td>.023</td><td>.232</td><td>.000</td></tr><tr><td>Direct Model: Bounded Visibility &gt; Information Search</td><td>.605</td><td>.014</td><td>.218</td><td>.000</td></tr><tr><td>Mediated Model: Bounded Visibility &gt; Coordination</td><td>.499</td><td>.037</td><td>.629</td><td>.000</td></tr><tr><td>Mediated Model: Bounded Visibility &gt; Information Search</td><td>.605</td><td>.022</td><td>.470</td><td>.000</td></tr><tr><td>Mediated Model: Cohesion &gt; Coordination</td><td>.543</td><td>.132</td><td>2.323</td><td>.000</td></tr><tr><td>Mediated Model: Cohesion &gt; Information Search</td><td>.737</td><td>.092</td><td>4.127</td><td>.000</td></tr></table>

![](/api/attachments/N4P6W6C4/fulltext/images/280e33306088d735c751a75d892e9264e6db7f17a35244168f99aa2d5abde6c8.jpg)  
Figure 3. A Mediated Model of Coordination and Information Search Activities Note: Visibility has been scored in this figure (and analysis) so that 1.00 is a group with bounded visibility and 0.00 a group with unbounded visibility.

## Summary of Results

In order to assess the effect of bounded versus unbounded visibility and network characteristics on boundary-spanning activities, we studied 6,500 discussion threads from across 655 groups, including 300 groups with unbounded visibility and 355 groups with bounded visibility. Our investigation yielded three sets of results (see overview in Figure 4).

First, our preliminary qualitative analysis of the group purposes of all groups in our data set provides an initial validation of our theoretical assumption that a group’s choice for bounded or unbounded visibility is associated at the outset with strategic motivations for the kinds of interactions that the group’s initiator plans to encourage.

![](/api/attachments/N4P6W6C4/fulltext/images/f9de1c91dbe9553b6b229808fb47fb9e44c89a902f11b9f53b7f6b669aee7bfb.jpg)  
Figure 4. Validated Research Model  
Note: In the upper half of the model, the visibility variable is scored as 1 for unbounded and 0 for bounded, while the lower half uses 1 for bounded and 0 for unbounded.

Second, our quantitative assessment of hypotheses reveal that the strategic choice for unbounded or bounded visibility influences the kinds of network characteristics the group develops, so that unbounded visibility results in significantly higher levels of network range and bounded visibility leads to significantly higher levels of network cohesion.

Third, our hypotheses testing further confirmed that the direct relationship from strategic visibility to boundary-spanning activities is significant so that groups with unbounded visibility display significantly higher rates of representation activities compared to groups characterized by bounded visibility, which instead display significantly higher rates of coordination and information search activities.

Finally, we validated our mediated model by analyzing the intermediate role of a group’s network characteristics on the relationship between strategic visibility and boundary-spanning activities. The findings showed that network range fully mediates the relationship between unbounded visibility and representational activities, whereas network cohesion partially mediates the relationship between bounded visibility and coordination and information search activities.

## Discussion

The proliferation of ESM technologies and their anticipated benefits for knowledge management and boundary spanning as a function of the increased visibility of content and interactions provided the impetus for this empirical investigation. The following discusses a set of theoretical and managerial implications associated with our findings that distinct boundary-spanning activities—that is, representation, coordination, and information search—stem from the strategic choice for distinct group visibility levels and subsequent emergent network characteristics.

## Theoretical Implications and Future Research Directions

Theoretically, this study contributes to a deeper and more nuanced understanding of how ESMs might transform workplace interactions by measuring the impact of bounded versus unbounded visibility on boundary-spanning exchanges in organizations. Specifically, our findings help to move beyond the myopic focus on whether visibility is good or bad, to a nuanced model that shows that both bounded and unbounded visibility can have positive outcomes by encouraging the enactment of different types of boundary-spanning activities.

Beyond this more nuanced understanding of ESM visibility, our findings also help to contribute the notion that visibility choices may be strategic to the ESM literature. Indeed, our findings show that the same affordance—visibility—can be used strategically to create either open or closed groups depending on the desired resources a team is intending to obtain. Thus our findings help to reveal not only how strategic visibility choices impact the nature of organizational activities groups engage in but also the mediating mechanism accounting for this effect—namely the diverse network structures that develop in groups as a result of revealing or restricting group access.

Furthermore, our findings may appear to suggest that there is a trade-off for teams between selecting bounded or unbounded visibility, hence, that groups can either do representation or coordination and information search. However, the unique opportunity provided by ESM is that organizational teams can sustain multiple virtual spaces simultaneously. This allows groups to avoid context-collapse [57] by strategically segregating their audiences, so that representation activities can be directed at the broadest audience possible—the entire organization—and coordination and information search activities can involve close interactions with carefully selected extra-team stakeholders.

Our theoretical implications also point to promising avenues for future research. First, although the general focus in the boundary-spanning literature is on measuring the occurrence of each of the boundary-spanning activities rather than measuring their success, whether or not a group enacts many representational activities does not tell us much about how successful each of these activities are. Hence, future research should (1) find algorithmic and behavioral methods for assessing the success of these three team boundary-spanning activities and (2) explore the effects of group visibility on the effectiveness rather than mere frequency of boundary-spanning attempts.

Furthermore, our machine-learning algorithm reveals that beyond the three boundary-spanning activities, interteam interactions also encompass activities (about 12 percent) that do not fall into the categories of representation, coordination, and/or information search, but are still work-related. Hence, future research should explore whether additional boundary-spanning activities exist in ESM that have not been previously identified in the knowledge management literature. For instance, in their early work, Ancona and Caldwell [4] separated boundary-spanning activities from the production (or task) and maintenance functions of groups [67]. Yet, a close examination of the task functions—those that enable the group to achieve its goals or solve the problem it is supposed to address—shows that coordination and information search are critical aspects of task functions. Hence, other task functions—such as elaborating, evaluating, or recording [78]—may account for the 12 percent of work-related activities not classified as representation, coordination, or information search. Similarly, around 20 percent of activities were nonwork-related. Therefore, future research could aim to further classify these activities using the lens of maintenance functions, such as harmonizing, encouraging, compromising, and setting standards.

Future research should attempt to further investigate why coordination and information search are more likely to occur in groups with bounded visibility; a finding that may have implications both for boundary-spanning theory and ESM system design. Our focus on the greater network cohesion, the likely greater trust, and the more secure environment that ensues in bounded groups certainly creates avenues for further exploration. Moreover, future research could try to develop ways to detect associated concepts like trust, psychological safety, shared identity, mutual respect, and reciprocity norms in the discussion threads of groups in order to elucidate other theoretical mechanisms that could explain the link between visibility and various intended or unintended ESM outcomes/activities.

In addition, prior work on virtual group collaboration has emphasized the challenges in providing team members with appropriate levels of awareness of remote team members’ activities in order to ensure adequate common ground for successful task completion [22, 41, 43, 73]. It may be that by inviting appropriate external stakeholders who already understand critical foundational aspects of a team’s work further paves the way for more common ground, thereby creating better opportunities for information sharing and effective coordination. The specific visibility features afforded by ESM may help address some of the prior awareness challenges noted by earlier researchers studying virtual team collaboration tools, leading to the stronger incidence of coordination and information search efforts among groups with bounded visibility.

Additionally, the finding that information search occurs more in groups characterized by bounded visibility may seem to contradict anecdotal evidence and theorizing in the ESM literature that focuses on the benefits of serendipitous encounters enabled by “hypervisibility” [54]. Our study attributes this finding to the greater expectation of information provision from a more restricted audience. These findings appear to be in line with literature on online crowdsourcing that has also shown that crowdsourcing tends to be more successful when the audience is carefully selected by so-called open innovation intermediaries [50].

The initial evidence that visibility choices are strategically motivated opens up several avenues in need of further exploration. In this context, specifically the use of mixed-method approaches that combine qualitative and quantitative data not only show the role of the strategic use of visibility in affecting network structures and boundary-spanning activities, but also help to elucidate the underlying intricacies of the kinds of groups or projects for which creators choose bounded or unbounded spaces. These are interesting topics that may result in novel theorizing about strategic visibility for the workplace [31, 91].

Finally, although this study confirms that strategic use of group visibility and its influence on the network characteristics of a group are important group-level antecedents to boundary-spanning frequency, additional antecedents may exist that reside either at the work group, individual, or even organizational level. For instance, individual job satisfaction and organizational culture may all impact the extent to which groups engage in boundary spanning. However, the challenge with these variables is that they are not readily operationalized and assessed through log data, and would thus require a mix of behavioral and self-reported approaches, which could be explored in future ESM research.

## Management Implications

Furthermore, not only do these findings help to advance theories of boundary spanning by providing behavioral insights into group-level antecedents of boundary-spanning activities, they further offer several practical contributions. First, the machine-learning algorithm can be used or modified by knowledge managers interested in assessing the extent to which boundary spanning occurs through ESM or other content-based and interaction-oriented platforms.

Second, our findings can inform managers of two important group-level antecedents that may or may not be conducive to the occurrence of each of the boundaryspanning activities. The recognition that different groups—as distinguished by their visibility and network characteristics—enact distinct boundary-spanning activities discourages a “one size fits all” approach to boundary spanning, resource sharing, and knowledge management in organizations. Understanding and testing these boundary-spanning antecedents helps to improve the creation and organization of work groups with the aim of enhancing the effectiveness of intraorganizational representation, information search, and coordination.

Third, our findings partially challenge organizational efforts to enhance contributions to ESM with the assumption that greater visibility will benefit the organization. That is, managers should not one-sidedly promote unbounded visibility, but take into consideration the organizational and team benefits stemming from bounded visibility. These findings further imply that designers should not merely focus on designing information flows that are visible organization-wide, but rather carefully consider various mechanisms—such as the ability to separately control reading, writing, and membership—that help (groups of) users enact their diverse strategic goals.

## Limitations

Although this study is the first to validate that the visibility affordance of ESM affects network characteristics of ESM groups as well as the amount and types of boundary-spanning activities enacted by these groups, there are several important limitations associated with this study. We did not differentiate ESM groups based on task type to explore whether task type (e.g., new product development versus internal audit) influences the types of boundary-spanning activities most likely to be enacted. We also do not know with certainty why groups selected the visibility setting for their groups; it could have been done strategically, by default, or without obvious thought. Although our preliminary qualitative content analysis suggests that the choice for visibility is a strategic one, future research should employ qualitative methods to unveil group creators’ choices for creating open or closed groups. Our network analyses are based exclusively on ESM interactions rather than all the interactions individuals may have during the course of their work; therefore, only a partial view of (boundary-spanning) interactions is obtained. Although existing research has shown that boundary-spanning activities are a critical antecedent to team (operational) performance, innovativeness, new product development, and organizational performance at large [6, 10, 37, 83, 87], our study does not measure the extent to which the boundary-spanning activities enacted in ESM contribute to these performance-oriented group and organizational outcomes. Finally, our study focused on exploring the relationship between strategic visibility and boundary spanning in the context of ESM; however, for real-world teams, ESM represents a single technology in a portfolio of communication tools available to workplace teams and therefore this study offers only a partial perspective of the complete set of boundary-spanning activities a team conducts.

## Conclusion

Despite these limitations, this study makes significant contributions. In particular, it provides a deeper and more nuanced understanding of how teams leverage ESM visibility in the context of boundary-spanning exchanges in organizations. Furthermore, our findings help to contribute the notion that visibility choices may be strategic and thereby impact not only the nature of organizational activities groups engage in but also the mediating mechanisms accounting for the effects of these impacts. In conclusion, future research should explore whether ESM thus present real-world teams with the opportunity to simultaneously sustain multiple virtual spaces—characterized by varying levels of visibility—through which they can manage their diverse team boundary-spanning goals and other objectives.

## Funding

This material is based in part upon work supported by the National Science Foundation under Grant Number IIS-1422316. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## NOTES

1. Please note that the actual terms used to describe these three team boundary-spanning activities by various authors differ.

2. http://www.jivesoftware.com.

3. Mean comparisons showed that visible groups displayed significantly larger group sizes $( F = 3 8 . 3 3 0 ; p = 0 . 0 0 0 )$ and significantly greater content creation $( F = 6 . 5 1 0 ; p = 0 . 0 1 \bar { 1 } )$ than invisible groups.

4. To normalize our dependent variable by two variables, we first created an “engagement” variable (by dividing the # of total content creation activities in a group by the size of the group) and then divided the number of boundary-spanning activities—representation, coordination, or information search—by the newly created engagement variable. We then rounded up the normalized variable to the nearest integer to retain a count variable.

5. The analysis results indicate that our main variables of interest are significantly zeroinflated, thereby offering further statistical support that the zero-inflated Poisson regression is the appropriate method of analysis.

## REFERENCES

1. Adler, P., and Kwon, S. Social capital: Prospects for a new concept. Academy of Management Review, 27, 1 (2002), 17–40.

2. Afuah, A., and Tucci, C.L. Crowdsourcing as a solution to distance search. Academy of Management Review, 37, 3 (2012), 355–375.

3. Ancona, D.G. Outward bound: Strategies for team survival in an organization. Academy of Management Journal, 33, 2 (1990), 334–365.

4. Ancona, D.G., and Caldwell, D.F. Beyond task and maintenance: Defining external functions in groups. Organization Studies, 13, 4 (1988), 468–494.

5. Ancona, D.G., and Caldwell, D.F. Beyond boundary spanning: Managing external dependence in product development teams. Journal of High Technology Management Research, 1, 2 (1990), 119–135.

6. Ancona, D.G., and Caldwell, D.F. Bridging the boundary: External activity and performance in organizational teams. Administrative Science Quarterly, 37, 4 (1992), 634–665.

7. Argote, L. Organizational Learning: Creating, Retaining and Transferring Knowledge. Boston: Kluwer Academic, 1999.

8. Argote, L.; Beckman, S.L.; and Epple, D. The persistence and transfer of learning in industrial settings. Management Science, 36, 2 (1990), 140–154.

9. Argote, L.; McEvily, B.; and Reagans, R. Managing knowledge in organizations: An integrative framework and review of emerging themes. Management Science, 49, 4 (2003), 571–582.

10. Baum, J.A.C., and Ingram, P. Survival-enhancing learning in the Manhattan hotel industry, 1898–1980. Management Science, 44, 7 (1998), 996–1016.

11. Bettencourt, L.A.; Brown, S.W.; and MacKenzie, S.B. Customer-oriented boundaryspanning behaviors: Test of a social exchange model of antecedents. Journal of Retailing, 81 (2005), 141–157.

12. Bieber, M.; Engelbart, D.; Furuta, R.; et al. Toward virtual community knowledge evolution. Journal of Management Information Systems, 18, 4 (2002), 11–35.

13. Birnholtz, J.; Dixon, G.; and Hancock, J. Distance, ambiguity and appropriation: Structures affording impression management in a collocated organization. Computers in Human Behavior, 28, 3 (2012), 1028–1035.

14. Bittner, E.A.C., and Leimeister, J.M. Creating shared understanding in heterogeneous work groups: Why it matters and how to achieve it. Journal of Management Information Systems, 31, 1 (2014), 111–144.

15. Boland, R.J., and Tenkasi, R.V. Perspective making and perspective-taking in communities of knowing. Organization Science, 6, 4 (1995), 350–372.

16. Borgatti, S.P., and Cross, R. A relational view of information seeking and learning in social networks. Management Science, 49, 4 (2003), 432–445.

17. Boser, B.E.; Guyon, I.M.; and Vapnik, V.N. A training algorithm for optimal margin classifiers. In Haussler, D. (ed.), Proceedings of the 5th Annual ACM Workshop on Computational Learning Theory, New York, NY, ACM Press; 1992, pp. 144–152.

18. Brzozowski, M.J. WaterCooler: Exploring an organization through enterprise social media. In Teasley, S., Havn, E., Prinz, W, and Lutters, W. (eds.), Proceedings of the ACM 2009 International Conference on Supporting Group Work. Group ’09. Sanibel Island, FL: ACM, 2009, pp. 219–228.

19. Bulgurcu, B.; Van Osch, W.; and Kane, G.C. The rise of the promoters: user classes and contribution patterns in enterprise social media. Journal of Management Information Systems, 35, 2 (Forthcoming).

20. Burt, R.S. The Network structure of social capital. Research in Organizational Behavior, 22, (2000), 345–423.

21. Burt, R.S. Structural holes and good ideas. American Journal of Sociology, 110, 2 (2004), 349–399.

22. Cramton, C.D. The mutual knowledge problem and its consequences for dispersed collaboration. Organization Science, 12, 3 (2001), 346–371.

23. Dey, A.K., and De Guzman, E.S. From awareness to connectedness: The design and deployment of presence displays. In Grinter, R., Rodden, T., Aoki, P., Cutrell, E., Jeffries, R., Olson, G. (eds.), Proceedings of CHI 2006. New York, NY: ACM, 2006, pp. 899–908.

24. DiMicco, J.; Geyer, W.; Millen, D.; Dugan, C.; and Brownholtz, B. People sensemaking and relationship building on an enterprise social network site. In Sprague, R. (ed.), 42nd

Hawaii International Conference on Systems Sciences. Washington DC: IEEE, 2009, pp. 1– 10.

25. DiMicco, J., and Millen, D. Identity management: multiple presentations of self in facebook. In Gross, T. and Inkpen, K. (eds.), Proceedings of the ACM 2007 International Conference on Supporting Group Work, Group ’07. Sanibel Island, FL: ACM, 2007, pp. 0–3.

26. Edmondson, A.C. Psychological safety and learning behavior in work teams. Administrative Science Quarterly, 44, 2 (1999), 350–383.

27. Edmondson, A.C. Managing the risk of learning: Psychological safety in work teams. In M.A. West, D. Tjosvold, and K.G. Smith (eds.), International Handbook of Organizational Teamwork and Cooperative Working. Chichester: Wiley, 2003, pp. 255–275.

28. Ellison, N.B.; Gibbs, J.L.; and Weber, M.S. The use of enterprise social network sites for knowledge sharing in distributed organizations: The role of organizational affordances. American Behavioral Scientist, 59, 1 (2015), 103–123.

29. Fleming, L., and Waguespack, D.M. Brokerage, boundary spanning, and leadership in open innovation communities. Organization Science, 18, 2 (2007), 165–180.

30. Freeman, L.C. Centrality in social networks conceptual clarification. Social Networks, 1, 3 (1978), 215–239.

31. Gibbs, J.L.; Rozaidi, N.A.; and Eisenberg, J. Overcoming the “ideology of openness”: Probing the affordances of social media for organizational knowledge sharing. Journal of Computer-Mediated Communication, 19, 1 (2013), 102–120.

32. Gold, A.H.; Malhotra, A.; and Segars, A.H. Knowledge management: An organizational capabilities perspective. Journal of Management Information Systems, 18, 1 (2001), 185–214.

33. Grabher, G. Temporary architectures of learning: Knowledge governance in project ecologies. Organization Studies, 25, 9 (2004), 1491–1514.

34. Granovetter, M.S. The strength of weak ties. American Journal of Sociology, 78, 6 (1973), 1360–1380.

35. Granovetter, M.S. Economic action and social structure: The problem of embeddedness. American Journal of Sociology, 91, 3 (1985), 481–510.

36. Hampton, K.N.; Lee, C.-J.; and Her, E.J. How new media affords network diversity: Direct and mediated access to social capital through participation in local social settings. New Media and Society, 13, 7 (2011), 1031–1049.

37. Hansen, M.T. The search-transfer problem: The role of weak ties in sharing knowledge across organization subunits. Administrative Science Quarterly, 44, 1 (1999), 82–111.

38. Hansen, M.T., and Haas, M.R. Competing for attention in knowledge markets: Electronic document dissemination in a management consulting company. Administrative Science Quarterly, 46, 1 (2001), 1–28.

39. Hargadon, A.B. Firms as knowledge brokers: Lessons in pursuing continuous innovation. California Management Review, 40, 3 (1998), 209–227.

40. Harvey, S. Creative synthesis: Exploring the process of extraordinary group creativity. Academy of Management Review, 39, 3 (2014), 324–343.

41. Hinds, P.J., and Bailey, D.E. Out of sight, out of sync: Understanding conflict in distributed teams. Organization Science, 14, 6 (2003), 615–632.

42. IDRE/UCLA. Zero-inflated Poisson regression; STATA data analysis examples. Statistical Consulting Group. http://stats.idre.ucla.edu/stata/dae/zero-inflated-poisson-regression/.

43. Jang, C.-Y.; Steinfield, C.; and Pfaff, B. Virtual team awareness and groupware support: An evaluation of the TeamSCOPE system. International Journal of Human-Computer Studies, 56, 1 (2002), 109–126.

44. Joachims T. (1998). Text categorization with Support Vector Machines: Learning with many relevant features. In: Nédellec C., Rouveirol C. (eds), Machine Learning: ECML-98.

ECML 1998. Lecture Notes in Computer Science (Lecture Notes in Artificial Intelligence), vol. 1398. Springer, Berlin, Heidelberg, pp.137–142.

45. Kane, G.C. The evolutionary implications of social media for organizational knowledge management. Information and Organization, 27, 1 (2017), 37–46.

46. Kane, G.C.; Alavi, M.; Labianca, G.; and Borgatti, S.P. What’s different about social media networks? A framework and research agenda. MIS Quarterly, 38, 1 (2014), 274–304.

47. Kane, G.C., and Borgatti, S.P. Centrality-IS proficiency alignment and workgroup performance. MIS Quarterly, 35, 4 (2011), 1063–1078.

48. Keen, A. Digital Vertigo: How Today’s Online Social Revolution Is Dividing, Diminishing, and Disorienting Us. New York: St. Martin’s Press, 2012.

49. Kietzmann, J.H.; Hermkens, K.; McCarthy, I.P.; and Silvestre, B.S. Social media? Get serious! Understanding the functional building blocks of social media. Business Horizons, 54, 3 (2011), 241–251.

50. King, A., and Lakhani, K. Using open innovation to identify the best ideas. MIT Sloan Management Review, 55, 1 (2013), 41–48.

51. Kirkman, B.L., and Mathieu, J.E. The dimensions and antecedents of team virtuality. Journal of Management, 31, 5 (2005), 700–718.

52. Landis, J.R., and Koch, G.G. The measurement of observer agreement for categorical data. Biometrics, 33, 1 (1977), 159–174.

53. Lapré, M.A., and Van Wassenhove, L.N. Creating and transferring knowledge for productivity improvement in factories. Management Science, 47, 10 (2001), 1311–1325.

54. Leonardi, P.M. Social media, knowledge sharing, and innovation: Toward a theory of communication visibility. Information Systems Research, 25, 4 (2014), 796–816.

55. Leonardi, P.M. Ambient awareness and knowledge acquisition: Using social media to learn “who knows what” and “who knows whom.” MIS Quarterly, 39, 4 (2015), 747–762.

56. Leonardi, P.M. The social media revolution: Sharing and learning in the age of leaky knowledge. Information and Organization, 27, 1 (2017), 47–59.

57. Leonardi, P.M.; Huysman, M.; and Steinfield, C. Enterprise social media: Definition, history, and prospects for the study of social technologies in organizations. Journal of Computer-Mediated Communication, 19, 1 (2013), 1–19.

58. Leonardi, P.M.; Vaast, E. Social Media and Their Affordances for Organizing: A Review and Agenda for Research. Academy of Management Annals, 11, 1 (2017), 150–188.

59. Leonardi, P.M., and Meyer, S.R. Social media as social lubricant: How ambient awareness eases knowledge transfer. American Behavioral Scientist, 59, 1 (2014), 10–34.

60. Levina, N., and Arriaga, M. Distinction and status production on user-generated content platforms: Using Bourdieu’s theory of cultural production to understand social dynamics in online fields. Information Systems Research, 25, 3 (2014), 468–488.

61. Long, J.S. Regression Models for Categorical and Limited Dependent Variables, Advanced Quantitative Methods in the Social Sciences. Thousand Oaks, CA: Sage, 1997.

62. Lu, B.; Guo, X.; Luo, N.; and Chen, G. Corporate blogging and job performance: Effects of work-related and nonwork-related participation. Journal of Management Information Systems, 32, 4 (2015), 285–314.

63. March, J.G. Exploration and exploitation in organizational learning. Organization Science, 2, 1 (1991), 71–87.

64. Marks, M.A.; Mathieu, J.E.; and Zaccaro, S.J. A temporally based framework and taxonomy of team processes. Academy of Management Review, 26, 3 (2001), 356–376.

65. Marrone, J.A. Team boundary spanning: A multilevel review of past research and proposals for the future. Journal of Management, 36, 4 (2010), 911–940.

66. Marrone, J.A.; Tesluk, P.E.; and Carson, J.B. A multilevel investigation of antecedents and consequences of team member boundary-spanning behavior. Academy of Management Journal, 50, 6 (2007), 1423–1439.

67. McGrath, J.E. Groups: Interaction and Performance. Englewood Cliffs, NJ: Prentice Hall, 1984.

68. Mohrman, S.A.; Cohen, S.G.; and Mohrman, A.M. Designing Team-Based Organizations: New Forms for Knowledge Work. San Francisco: Jossey-Bass, 1995.

69. Nahapiet, J., and Ghoshal, S. Social capital, intellectual capital, and the organizational advantage. Academy of Management Review, 23, 2 (1998), 242–266.

70. Nidumolu, S.R.; Subramani, M.; and Aldrich, A. Situated learning and the situated knowledge web: Exploring the ground beneath knowledge management. Journal of Management Information Systems, 18, 1 (2001), 115–150.

71. O’Sullivan, P.B. What you don’t know won’t hurt me: Impression management functions of communication channels in relationships. Human Communication Research, 26, 3 (2000), 403–431.

72. Oh, H.; Chung, M.H.O.; and Labianca, G. Group social capital and group effectiveness: The role of informal socializing ties. Academy of Management Journal, 47, 6 (2004), 860–875.

73. Olson, G.M., and Olson, J.S. Distance matters. Human-Computer Interaction, 15, 2 (2000), 139–178.

74. Podolny, J.M., and Baron, J.N. Relationships and resources: Social networks and mobility in the workplace. American Sociological Review, 62, 5 (1997), 673–693.

75. Putnam, R.D. Bowling Alone. New York: Simon and Schuster, 2000.

76. Reagans, R., and McEvily, B. Network structure and knowledge transfer: The effects of cohesion and range. Administrative Science Quarterly, 48, 2 (2003), 240–267.

77. Rosenkopf, L., and Nerkar, A. Beyond local search: Boundary-spanning, exploration, and impact in the optical disk industry. Strategic Management Journal, 22, 4 (2001), 287– 306.

78. Schein, E.H. Process Consultation: Its Role in Organizational Development. Reading, MA: Addison-Wesley, 1969.

79. Steinfield, C.; DiMicco, J.; Ellison, N.B.; and Lampe, C. Bowling online: Social networking and social capital within the organization. In C&T ’09 Proceedings of the fourth international conference on Communities and technologies. New York, ACM, 2009, pp. 245–254.

80. Stenmark, D. Leveraging tacit organization knowledge. Journal of Management Information Systems, 17, 3 (2000), 9–24.

81. Stieglitz, S., and Dang-Xuan, L. Emotions and information diffusion in social media: sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29, 4 (2013), 217–248.

82. Swap, W.; Leonard, D.; Shields, M.; and Abrams, L. Using mentoring and storytelling to transfer knowledge in the workplace. Journal of Management Information Systems, 18, 1 (2001), 95–114.

83. Szulanski, G. Exploring internal stickiness: Impediments to the transfer of best practice within the firm. Strategic Management Journal, 17, 1 (1996), 27–43.

84. Tortoriello, M.; Reagans, R.; and McEvily, B. Bridging the knowledge gap: The influence of strong ties, network cohesion, and network range on the transfer of knowledge between organizational units. Organization Science, 23, 4 (2012), 1024–1039.

85. Treem, J.W., and Leonardi, P.M. Social media use in organizations: Exploring the affordances of visibility, editability, persistence, and association. Annals of the International Communication Association, 36 (2012), 143–189.

86. Tsai, W., and Goshal, S. Social capital and value creation: The role of intrafirm networks. Academy of Management Journal, 41, 4 (1998), 464–476.

87. Tushman, M.L., and Scanlan, T.J. Boundary spanning individuals: Their role in information transfer and their antecedents. Academy of Management Journal, 24, 2 (1981), 289– 305.

88. Uzzi, B. Social structure and competition in interfirm networks: The paradox of embeddedness. Administrative Science Quarterly, 42 (March 1997), 35–67.

89. VanOsch, W., and Steinfield, C. Team boundary spanning: Strategic implications for the implementation and use of enterprise social media. Journal of Information Technology, 31, 2 (2016), 207–225.

90. VanOsch, W.; Steinfield, C.; and Balogh, B.A. Enterprise social media: Challenges and opportunities for organizational communication and collaboration. In Proceedings of the 48th Hawaii International Conference on System Sciences. IEEE Computer Society Press, 2015, pp. 763–772.

91. VanOsch, W.; Steinfield, C.; and Zhao, Y. Team boundary spanning through enterprise social media: Exploring the effects of group-level diversity using a data science approach. In Proceedings of the 49th Hawaii International Conference on System Sciences (HICSS). IEEE, 2016, pp. 2176–2185.

92. Walther, J.B. Selective self-presentation in computer-mediated communication: Hyperpersonal dimensions of technology, language, and cognition. Computers in Human Behavior, 23, 5 (2007), 2538–2557.

93. Wasserman, S., and Faust, K. Social network analysis: Methods and applications. Methods and Applications, (1994), 825.

94. Whelan, E.; Golden, W.; and Donnellan, B. Digitising the R&D social network: Revisiting the technological gatekeeper. Information Systems Journal, 23, 3 (2013), 197–218.

95. Whelan, E., and Teigland, R. Transactive memory systems as a collective filter for mitigating information overload in digitally enabled organizational groups. Information and Organization, 23, 3 (2013), 177–197.

96. Whelan, E.; Teigland, R.; Donnellan, B.; and Golden, W. How Internet technologies impact information flows in R&D: Reconsidering the technological gatekeeper. R&D Management, 40, 4 (2010), 400–413.
