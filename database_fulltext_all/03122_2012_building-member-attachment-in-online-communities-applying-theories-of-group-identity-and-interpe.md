---
otero_id: 3122
otero_key: "YJWBKFUH"
title: "Building Member Attachment in Online Communities: Applying Theories of Group Identity and Interpersonal Bonds"
authors: "Yuqing Ren; F. Maxwell Harper; Sara Drenner; Loren Terveen; Sara Kiesler; John Riedl; Robert E. Kraut"
year: "2012"
journal: "MIS Quarterly"
doi: "10.2307/41703483"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Building Member Attachment in Online Communities: Applying Theories of Group Identity and Interpersonal Bonds

Author(s): Yuqing Ren, F. Maxwell Harper, Sara Drenner, Loren Terveen, Sara Kiesler, John Riedl and Robert E. Kraut

Source: MIS Quarterly, September 2012, Vol. 36, No. 3 (September 2012), pp. 841-864

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: https://www.jstor.org/stable/41703483

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at https://about.jstor.org/terms

# BUILDING MEMBER ATTACHMENT IN ONLINE COMMUNITIES: APPLYING THEORIES OF GROUP IDENTITY AND INTERPERSONAL BONDS $^{1}$

Yuqing Ren
Carlson School of Management, University of Minnesota, Minneapolis, MN 55455 U.S.A. {chingren@umn.edu}

F. Maxwell Harper, Sara Drenner, Loren Terveen
Department of Computer Science, University of Minnesota, Minneapolis, MN 55455 U.S.A.
{harper@cs.umn.edu} {mosch@cs.umn.edu} {terveen@cs.umn.edu}

Sara Kiesler

Human-Computer Interaction Institute, Carnegie Mellon University, Pittsburgh, PA 15213 U.S.A. {kiesler@cs.cmu.edu}

John Riedl

Department of Computer Science, University of Minnesota, Minneapolis, MN 55455 U.S.A. {riedl@cs.umn.edu}

Robert E. Kraut

Human-Computer Interaction Institute, Carnegie Mellon University, Pittsburgh, PA 15213 U.S.A. {robert.kraut@cmu.edu}

Online communities are increasingly important to organizations and the general public, but there is little theoretically based research on what makes some online communities more successful than others. In this article, we apply theory from the field of social psychology to understand how online communities develop member attachment, an important dimension of community success. We implemented and empirically tested two sets of community features for building member attachment by strengthening either group identity or interpersonal bonds. To increase identity-based attachment, we gave members information about group activities and intergroup competition, and tools for group-level communication. To increase bond-based attachment, we gave members information about the activities of individual members and interpersonal similarity, and tools for interpersonal communication. Results from a six-month field experiment show that participants' visit frequency and self-reported attachment increased in both conditions. Community features intended to foster identity-based attachment had stronger effects than features intended to foster bond-based attachment. Participants in the identity condition with access to group profiles and repeated exposure to their group's activities visited their community twice as frequently as participants in other conditions. The new features also had stronger effects on newcomers than on old-timers. This research illustrates how theory from the social science literature can be applied to gain a more systematic understanding of online communities and how theory-inspired features can improve their success.

Keywords: Online community, group identity, interpersonal bonds, attachment, participation

## Introduction

Online communities are persistent collections of people with common or complementary interests whose primary method of communication is the Internet (Preece 2000). They offer new channels for organizations to connect with customers, employees, and business partners (Dellarocas 2006; Leidner et al. 2010), are sources of product innovation and customer support (El Sawy and Bowles 1997; Ogawa and Piller 2006), and serve as platforms for new business models (Verona et al. 2006). Online communities also provide the general public with useful information (Gu et al. 2007; Wasko and Faraj 2005), emotional support (Maloney-Krichmar and Preece 2005), venues for political and social discussion (Hill and Hughes 1998), and ways to maintain their social networks and meet new people (Agarwal et al. 2008; Wellman 2001).

Despite the importance and success of some high-profile online communities, many others falter. One Deloitte survey found that most business efforts to build online communities failed to attract a critical mass of members, even when firms spent over \$1 million in the effort (Worthen 2008). Empirical research suggests that a major obstacle to community success is engaging community members; the majority of people who visit online communities contribute little and leave quickly. Simply adding social or group features to a company's website does not guarantee a vibrant community. In one study, more than two-thirds (68 percent) of newcomers to Usenet groups were never seen again after their first post (Arguello et al. 2006). In another, over half of the developers who registered to participate in a Python open source development project did not return after their first contribution (Ducheneaut 2005). In MovieLens.org, the community we studied, the half-life of a new registrant was only 18 days.

The literature on online communities suggests that member participation and retention depends on member attachment, which is cultivated by connecting members with topics of their interest and like-minded others (Preece 2000). $^{2}$ By attachment, we refer to members' affective connection to and caring for an online community in which they become involved. Members who have a strong attachment to their online community are crucial to its success. These are the members most likely to provide the content that others value—answers to others' questions in technical and health support groups (Blanchard and Markus 2004; Rodgers and Chen 2005), code in open source projects (Mockus et al. 2002), and edits in Wikipedia (Kittur et al. 2007). Strongly attached members also help enforce norms of appropriate behavior (Smith et al. 1997), police the community and sanction deviant behaviors (Chua et al. 2007), and perform behind the scenes work to help maintain the community (Butler et al. 2007).

Many books and websites provide advice about how to craft the features and policies of a community to increase members' attachment to it, as evidenced by their likelihood of returning and their willingness to contribute (e.g., Kim 2000; Preece 2000). Although useful, these sources often fail to provide the theoretical rationale for their recommendations or to specify contingencies in applying the principles to communities organized around different purposes. For instance, Kim (2000) recommends that all online communities provide opportunities for participants to exchange personal information so that they can build personal relationships. Contrary to this advice, many communities' policies discourage trading personal information and encourage people to focus on the topic of the community, whether it be real estate investing or movie critiques. The literature contains little theoretical guidance as to which policy is best.

In this paper, we demonstrate how insights from decades of social psychology research help answer such questions. Researchers have made considerable progress in describing the characteristics of different online communities (e.g., Baym 2007; Shklovski et al. 2010) and surveying member reactions to design features (Phang et al. 2009; Shen and Khalifa 2009), but have developed little theoretically based knowledge to predict how or why specific policies and features make online communities successful in engaging and retaining members. We review theories on how group identity and interpersonal bonds (Prentice et al. 1994) increase attachment, and show experimentally that online community features derived from these theories have large influences on members' attachment and participation.

To foreshadow this work, theories of group identity point to community features that build attachment by focusing members' attention on a group, whereas theories of interpersonal bonds point to community features that build attachment by focusing member attention on individual people. To evaluate the effects of these theoretically inspired features on member attachment, we created one set of features to promote attachment to a group within the community (identity-based attachment) and another set to promote attachment to individual members of the community (bond-based attachment). We implemented the features in an existing online community, and evaluated their effects on attachment and subsequent behaviors in a six-month field experiment and a follow-up laboratory experiment. Experimental results show that both identity-based and bond-based features increased member attachment and participation compared to a control condition but identity-based features had substantially stronger effects. Overall, we found support for the theory-based predictions. Our work illustrates the value of theory in understanding successful online communities and improving them, using social psychological theories of group identity and interpersonal bonds as an example.

## Theory and Hypotheses

At the outset, we distinguish between a community as an interacting body and the sense of community experienced by its members (McMillan and Chavis 1986). Communities differ in the extent to which they generate a sense of community among members and members differ in their degree of attachment. Social psychological theory holds that attachment in groups arises in two ways. In the first manner, attachment works through group identity, whereby people feel connected to a group's character or purpose (Hogg and Turner 1985; Tajfel and Turner 1986). For example, members of the Sierra Club may know few other members, but they identify with the cause the group espouses. By contrast, in the second manner, attachment works through interpersonal bonds, whereby people develop relationships with other members (Festinger et al. 1950). Fraternity members feel attached to their fraternities in part because of the friendships they have developed with other members (Prentice et al. 1994).

We draw on the distinction above to differentiate online communities in which members share a common purpose versus those that foster interpersonal ties. For example, My Starbucks Idea is an online community of Starbucks fans and customers who identify with the brand. Members contribute ideas to help the company improve its products and services, but there are few signs of bonding among its members. By contrast, girlfriendcircles.com is an online community that helps women find local friends. Its members are connected by interpersonal ties. Our conceptual distinction between identity-based and bond-based attachment does not imply that they are mutually exclusive in practice. Individuals may be attached to a particular community through both mechanisms, simultaneously feeling a connection to the community as a whole and to individuals within it. In addition, a particular community may try to foster both types of attachment. For instance, the GNOME open source project highlights both identity-based and bond-based attachment when it describes itself as “a worldwide community of volunteers who hack, translate, design, QA, and generally have fun together” (http://projects.gnome.org/). This description emphasizes the collective purpose of building a user interface to the Linux operating system as well as the fun members have together. Many contributors join its 95 groups and attend in-person events to “meet old friends, discuss new technologies and other GNOME-related stuff (e.g., http://live.gnome.org/Brussels2010).”

In this research, we examine three levels of attachment: identity-based attachment to a group within the community, bond-based attachment to individual members, and attachment to the large community. We experimentally introduce design features either to increase attachment to a group or to individuals. Because, as we discuss in more detail below, affect often spreads from attitude objects to related objects or between a composite object and its components, we expect attachment either to a group or to individuals within the community will lead to attachment to the large community as well (Meyer et al. 2002; Riketta and Dick 2005; Vandenberge et al. 2004). If group identity and interpersonal bonds are mechanisms through which community attachment develops, then to understand how communities succeed or fail, we must first understand the theoretical antecedents of group identity and interpersonal bonds. Following the review by Ren et al. (2007), we summarize these antecedents next and present our hypotheses of how their implementations can increase attachment in online communities, as shown in Figure 1.

## Theoretical Antecedents of Identity-Based Attachment

Group categorization elicits identity-based attachment. Group identity in everyday life emerges when people define a collection of people as members of the same social category (Turner 1985; Turner et al. 1987). In face-to-face groups, gender, location, ethnicity, interests, and political values or choices often define group categories (Karasawa 1991; Postmes and Spears 2000). Tajfel et al. (1971) demonstrated experimentally that merely assigning research participants an arbitrary label (e.g., over-estimators) activated a sense of group identity, even when they did not know others in their group. Researchers have also elicited identity-based attachment experimentally by making group membership explicit using group names and uniforms (Worchel et al. 1998). We expect that if members of an online community are assigned to a group within the community and if this categorization into a group is made explicit, members should feel identified with the group. The categorization might be strengthened with justification and explanation of the membership assignment.

![](/api/attachments/YJWBKFUH/fulltext/images/9d8512c7e9c738b9136af0b0fef7c751dc91e8b2e971af590e58cd9ac6f38d33.jpg)  
Figure 1. Increasing Attachment in Online Communities

Information about the group increases identity-based attachment. Group identity can be enhanced by giving people information about the group, representing individuals as group members, and downplaying their personal attributes, a process called depersonalization. In a study of online depersonalization by Postmes et al. (2002), people interacting in “depersonalized” computer-mediated groups saw group labels that indicated in-group versus out-group categories (e.g., Dutch versus English) but not the names of individual members, whereas in the personalized condition, they saw each others’ first names and personal images. The depersonalization manipulation and information about the attributes or characteristics of one’s group led to stronger attachment to the group.

Group homogeneity increases identity-based attachment. People who identify with a group overemphasize within-group similarity and between-group distinctiveness (e.g., Lee and Ottati 1995; Simon and Pettigrew 1990). This link between homogeneity and identity is bidirectional: homogeneity of membership also increases group identity (Brewer 1991). Pickett and Brewer (2001) argue that a feeling of being connected to an in-group occurs “to the extent that one is similar to the group prototype and all group members are perceived as similar to each other" (p. 342). Therefore, emphasizing in-group homogeneity should increase group identity and attachment to the group.

Intergroup competition increases identity-based attachment. The presence of an out-group and competition with it strongly enhances identity-based attachment (Hogg and Turner 1985; Postmes et al. 2001). Competition with out-groups can be increased by highlighting group boundaries and emphasizing the existence of out-groups. Wikipedia uses this tactic when it pits its success as an encyclopedia against rivals such as the Encyclopedia Britannica (http://en.wikipedia.org/wiki/Reliability\_of\_Wikipedia).

Familiarity with the group increases liking of the group. In early experiments, Zajonc (1968) and Milgram (1977) demonstrated a “mere exposure effect”: the more familiar one is with objects, symbols, or people, the more one likes them. In online communities with a goal of fostering identity-based attachment, making the community and its activities repeatedly visible to members should increase member attachment to the community. Many online communities provide a constant stream of updated information about the community and groups within it. For example, the Community portal on Wikipedia (http://en.wikipedia.org/wiki/Wikipedia:

Community\_portal) is the place for the Wikipedia editing community to come together to share information. It includes “news” articles about Wikipedia written by the community, reports on the status of WikiProjects and task forces, and links to discussions that are seeking wider attention. The updates repeatedly expose members to Wikipedia activities, which should build stronger attachment to Wikipedia.

We expect that these theoretical antecedents, when operationalized and implemented as community features that assign people to a group, that provide information about the group, that highlight group homogeneity and intergroup competition, and that facilitate familiarity with the group through repeated exposure, will increase identity-based attachment. We thus hypothesize:

Hypothesis 1a: Focusing members' attention on a group and group activities will increase their identity-based attachment to the group.

## Theoretical Antecedents of Bond-Based Attachment

Information about individual members increases bond-based attachment. Information about individual members and their unique attributes that personalize members of a group fosters attachment to individual members of the group. Interpersonal bonds arise particularly from exchanges of personal information and self-disclosure (Collins and Miller 1994; Postmes et al. 2001). Opportunities for self-disclosure and self-presentation shift attention from the group as a whole to individual members (Utz 2003), as does displaying individual members' photographs (Postmes et al. 2002; Sassenberg and Postmes 2002).

Interpersonal similarity increases bond-based attachment. Interpersonal comparisons are ubiquitous in social life. These comparisons tell us about others in our social environment, are the grist for conversation, and are the basis of self-evaluation and friendship formation (Suls et al. 2002; Wood 1989). In particular, our similarity to other people is a major determinant of our interpersonal attraction to them. Interpersonal similarity in personal attributes and in preferences has been shown to cause positive evaluation of others and liking of them (Byrne 1997; Newcomb 1961). Researchers frequently manipulate perceived similarities among group members to vary their attachment to each other (Hogg and Turner 1985; Postmes et al. 2001).

Familiarity with members increases liking of the members. The “mere exposure effect” that we mentioned earlier (Zajonc 1968; Milgram 1977) applies to both groups and individuals:

the more familiar one is with a person, the more likely one will like the person. The more individual members encounter one another and are exposed to each other's activities, the more likely they are to communicate with each other and the more they will like and help each other (Festinger et al. 1950). In online communities with a goal of fostering bond-based attachment, making individual members and their activities repeatedly visible to each other should increase the likelihood of friendship and interpersonal attraction. The news feed feature on Facebook, which displays one's friends' recent posts and activities on one's home page, serves this purpose.

Interpersonal communication leads to interpersonal bonds. Interpersonal communication drives the development of interpersonal attraction (Festinger 1950). As people's interactions increase in frequency, their liking for one another also increases (Newcomb 1961). In online communities, frequency of interpersonal communication is a major determinant of the extent to which people can build relationships with one another (McKenna et al. 2002).

We expect that these theoretical antecedents, when operationalized and implemented as community features that provide information about individual members, that highlight interpersonal similarities, that facilitate repeated exposure to individual members, and that enable communication with individual members, will increase bond-based attachment. We thus hypothesize:

Hypothesis 1b: Focusing members' attention on individual members and their activities will increase bond-based attachment to members.

## Attachment to the Large Community as a Whole

Affect generalization is a common phenomenon, in which affect toward one attitude object spreads to related objects. This spread is one source of the halo effect in person perception, in which the affect associated with a component of an attitude object, such as a person's physical attractiveness, spreads to the overall object (i.e., the person), and to other traits, such as his or her intelligence or honesty (Cooper 1981). The spread of affect partially explains the impact of mood on helping behavior (e.g., Isen and Levin 1972) and risk taking (e.g. Forgas 1995). Similar suffusion of affect is likely to occur in organizational settings as well, in which, for example, affective commitment associated with a work group or feelings of liking for a supervisor or coworkers generalize to the organization as a whole and vice versa. The spread of affect may explain the moderate correlations found in recent meta-analyses between affective commitment toward one's workgroup or one's supervisor and affective commitment toward the organization as a whole, and between satisfaction with supervisors and coworkers and affective commitment toward the organization as a whole (Meyer et al. 2002; Riketta and Dick 2005; Vandenberge et al. 2004). Based on this reasoning, we expect identity-based and bond-based attachment to serve as two mechanisms for increasing attachment to the community as a whole. The more a member feels attached to a group or to individuals within the community, the more the member will feel attached to the larger community.

Hypothesis 1c: An increase in either identity-based attachment to a group within an online community or bond-based attachment to an individual member of the community will increase attachment to the large community as a whole.

## Impact of Attachment on Member Behaviors

People who are attached to a group evaluate their group more positively than those who are less attached, stay in the group longer, participate more, and exert more effort on its behalf (Hogg 1992). Likewise, commitment to an organization is associated with lower turnover or intention to leave (Meyer et al. 2002). In one study of volunteer services for AIDS patients, people who reported stronger attachment to the AIDS community participated in a wider range of activities, such as attending AIDS fundraising events, being involved in AIDS activism, and donating to AIDS groups (Omoto and Snyder 2002). We thus posit that increased attachment in an online community, whatever the source of that attachment, will lead to a set of visible behaviors such as longer duration of membership, more frequent visits, and more active participation (Blanchard and Markus 2004, Ren et al. 2007). Figure 1 shows these relationships.

Hypothesis 2a: Increased attachment will increase member participation, mediating the impact of community features that focus attention on a group or individual members.

Hypothesis 2b: Increased attachment will increase member retention, mediating the impact of community features that focus attention on a group or individual members.

In addition to these general effects of attachment, the literature also suggests that identity-based and bond-based attachment may have some different consequences, especially in relation to members' attitudes toward the group or individuals to whom they have become attached (Ren et al. 2007). In particular, identity-based attachment should cause members to attend to and like the group, which in turn will increase their willingness to exert effort to help the group. By contrast, bond-based attachment should cause members to focus on individual relationships with one another, which in turn will increase their willingness to exert effort to help individuals.

Hypothesis 3a: Identity-based attachment to the group will increase members' willingness to exert effort to help the group.

Hypothesis 3b: Bond-based attachment to individual members will increase members' willingness to exert effort to help other members.

## Field Experiment

To test the hypotheses, we conducted a six-month field experiment in a movie-related community called MovieLens.org. The site was launched in the mid-1990s as a place for movie ratings and recommendations as well as a platform for research on social recommender systems. We chose MovieLens as our experimental platform for three reasons. First, it was large and characterized by considerable churn, making it a good site to study the effects of increased attachment on retention and participation. At the beginning of our study, the website had more than 100,000 users and the half-life of a new user was only 18 days. Second, we had adequate control of the site to introduce new features, configure the system into parallel experimental conditions, and randomly assign participants to conditions. Third, it began attracting users with various motives in recent years, which makes it a good setting to test our identity-based and bond-based features. Until 2005, the site was mainly a movie recommendation service. People registered to get movie recommendations and had little awareness of MovieLens as a community or of the presence of other members (Harper et al. 2005). The introduction of discussion forums and movie tagging features (Drenner et al. 2006; Sen et al. 2006) gradually changed the tone of the site for a small set of active members, among whom interpersonal friendships emerged. For these members, MovieLens became, in part, a bond-based community. However, for the large majority of members, even after the introduction of the discussion forums, MovieLens remained a movie recommendation site.

## Method

For the field experiment, we introduced two sets of new website features to MovieLens to create a greater sense of com-

<table><tr><td colspan="3">Table 1. Independent Variables, Theoretical Antecedents, and Community Features</td></tr><tr><td>Type of Attachment:IndependentVariable</td><td>TheoreticalAntecedents ofAttachment</td><td>Community Features: Independent Variables</td></tr><tr><td colspan="3">Community Feature I: Group Versus Individual Profile Page</td></tr><tr><td rowspan="4">Identity-based</td><td>Group categorization</td><td>Group name, icon, and statement on top of member&#x27;s group profile page</td></tr><tr><td>Group information</td><td>Detailed information about the group (e.g., movies the group likes; movies frequently rated by the group)</td></tr><tr><td>Group homogeneity</td><td>Clustering algorithm assigns people with similar movie preferences to the same group; profile shows movies that group members have rated highly</td></tr><tr><td>Intergroupcompetition</td><td>Ranking of one&#x27;s group against other groups according to number of movies rated and percentage of active members; comparison of movies that one&#x27;s group ranked high but other groups ranked low</td></tr><tr><td rowspan="4">Bond-based</td><td>Low group salience*</td><td>Group name and icon in one place on individual profile page</td></tr><tr><td>Personal information</td><td>Detailed information about individual members (e.g., name, city, gender, age, favorite color, history with the community)</td></tr><tr><td>Interpersonalsimilarity</td><td>Clustering algorithm assigns members with similar movie preferences to the same group; profile shows movies that profile viewer and profile owner rated similarly</td></tr><tr><td>Interpersonalcomparisons*</td><td>Profile shows movies that the profile viewer and profile owner rated differently and movies recommended to the profile viewer based on the profile owner&#x27;s ratings</td></tr><tr><td colspan="3">Community Feature II: Group Versus Individual Recent Activity Page</td></tr><tr><td>Identity-based</td><td>Familiarity with the group</td><td>Repeated exposure to group activities by showing movies the group rated and posts from one&#x27;s group on the recent activity page</td></tr><tr><td>Bond-based</td><td>Familiarity with members</td><td>Repeated exposure to individual member activities by showing movies rated and posts by frequently seen others on the recent activity page</td></tr><tr><td colspan="3">Community Feature III: Group and Interpersonal Communication</td></tr><tr><td>Identity-based</td><td>Intragroupcommunication*</td><td>Communication among group members on the group profile page (only accessible to group members, not members of other groups)</td></tr><tr><td>Bond-based</td><td>Interpersonalcommunication</td><td>Communication among individual members on individual profile pages (accessible to all visitors to the page)</td></tr></table>

Note: Constructs with \* are not theoretical antecedents. They are included as counterparts of a theoretical antecedent in the other condition for control purpose. See Figure 1 for detail.

munity. The first set of features—a group profile page, a recent group activity page, and group communication—aimed to increase identity-based attachment. The second set of the features—individual profile pages, a recent individual activity page, and interpersonal communication—aimed to increase bond-based attachment. Table 1 describes each feature and its linkages to the theoretical antecedents, and how the feature creates a focus on the group or a focus on individual members. For experimental comparisons, each implemented feature had a counterpart in the other condition. For instance, a counterpart of intergroup competition (to increase group identity) was interpersonal comparisons (to increase bonds). In the intergroup competition condition, the profile page showed how the participant's group compared with other groups whereas in the interpersonal comparisons condition, the profile page showed how the participant compared with other individuals.

All participants were assigned a user ID and a “movie group.” To assign participants a group, we created 10 movie groups. We chose the number 10 to ensure there would be a sufficient number of groups for intergroup comparison but few enough that members could remember them all. We used wild animal names to label the groups (Tiger, Eagle, Polar Bear, and so forth). Animal names did not have any obvious movie-relevant meaning and were easy to remember.

To ensure that the 10 movie groups comprised users with similar movie tastes and had similar size and levels of activity, we developed a new activity-balanced clustering algorithm (Harper et al. 2007), based on Banerjee and Ghosh's (2002) approach to clustering. Standard clustering algorithms did not meet the requirement of equal-sized groups; for example, the standard k-means clustering algorithm (MacQueen 1967) placed 84 percent of the active MovieLens members into a single group.

The algorithm first uses a (slow) balanced hierarchical clustering algorithm on a subset of the data, and then uses a (fast) stable marriage-inspired algorithm to fully populate the clusters. Because we wanted members with similar tastes to be placed in the same group, we computed similarity scores by measuring the cosine similarity among members' movie ratings vectors, weighted by the number of co-ratings (Sarwar et al. 2001). To generate the final movie groups, we ran the first stage of the algorithm on the MovieLens population that had been recently active, thus distributing recent contributors equally across the 10 movie groups, then ran the second stage of the algorithm to distribute the remaining (recently inactive) members.

## Group Versus Individual Profiles

We created a novel form of group profile to implement the four theoretical antecedents of identity-based attachment listed in Table 1, that is, group categorization, information about the group, group homogeneity, and intergroup competition. The profile page was customized for each member. Figure 2 illustrates a movie group profile page as it appeared to members of the Tiger group. To emphasize group categorization, the top of the page shows the name of the group, the group's icon (in this case, a picture of a tiger), and a group statement describing the types of movies the group prefers. We tried to come up with statements that were both accurate and engaging, for example, "Bears love to watch sci-fi and fantasy blockbusters while not hibernating."

To emphasize group homogeneity, we displayed a list of movies that the group liked. To highlight out-group presence and intergroup competition, we displayed graphs that compared the group's recent movie ratings and login activities to the other nine movie groups. To emphasize group boundaries, group profile pages were shown differently to in-group and out-group members. When an out-group member looked at a profile, the top of the page informed the viewer that he or she was not a member of the currently displayed group. The page also displayed a list of movies the currently displayed group liked and the viewer's group disliked.

We also created a parallel individual profile page, customized for each individual member to implement the theoretical antecedents of bond-based attachment listed in Table 1, that is, information about members, interpersonal similarity, and interpersonal comparisons. Members could update their information and opt-in to a feature that automatically published movie-related information to their profile, based on their movie ratings and forum posts. About 80 percent of MovieLens members agreed to share this type of information. Figure 3 shows an example of an individual profile page. The page contained personal information fields that were editable by the member, such as name, location, gender, an open-ended text field for members to leave personal comments, and a space to upload a personal picture. Each individual profile page also contained several tables that related the owner of the page to the viewer of the page. For instance, one table showed movies that the owner and the viewer both rated highly. This display helped members discover their similarity to others. Underneath the user ID and picture, the page displayed a small name and icon of the movie group to which the page owner was assigned. We included this information only for methodological purposes, so that participants in the bond-based conditions could report their attachment to their movie groups (to compare with those in the identity-based conditions).

## Recent Activity Pages for Groups Versus Members

To increase familiarity with the participant's group in the identity-based condition or with individuals in the bond-based condition, we created a recent activity feature, based on algorithms that increased the probability that participants were exposed to the recent activities of their own group or to selected individual members. To increase identity-based attachment, 80 percent of the content the algorithm showed came from the participant's own movie group and 20 percent from other groups. To increase bond-based attachment, the algorithm first selected move ratings and posts from those members whom a participant had encountered previously. If it did not find enough members from previous sessions, it selected members who had movie tastes similar to the participant. The identity and bond-based versions displayed recent activity information in different formats. As shown in Figure 4, the identity version displayed recent ratings and posts as from a movie group, along with group names and icons. In contrast, as shown in Figure 5, the bond version displayed recent ratings and posts from individual members, along with their names and pictures. A short version of the recent activity page was available on the site's front page, and a longer version was available on a linked page called the Recent Activity Page.

![](/api/attachments/YJWBKFUH/fulltext/images/6f5c97b2b68a6fe057714c58bd77d114d57b729c7f39ceec616885b0e1ecec21.jpg)

## You are a member of the Tiger Group About this group: Tigers have complex relationships with their movies

## The Tiger Group thinks these movies are cool.

Title
Lost in Translation (2003)
Match Point (2005)
Boondock Saints, The (2000)
Breakfast at Tiffany's (1961)
Closer (2004)

These movies have high ratings from the Tiger Group and low ratings from other groups.

<table><tr><td>Title</td><td>Tiger Group</td></tr><tr><td>Boondock Saints, The (2000)</td><td>****</td></tr><tr><td>Closer (2004)</td><td>****</td></tr><tr><td>Match Point (2005)</td><td>****</td></tr><tr><td>Breakfast at Tiffany&#x27;s (1961)</td><td>****</td></tr><tr><td>Lost in Translation (2003)</td><td>****</td></tr></table>

## Group Rankings: Number of Movies Rated in the Last Week

<table><tr><td>Rhino</td><td>828</td></tr><tr><td>Leopard</td><td>633</td></tr><tr><td>Polar Bear</td><td>620</td></tr><tr><td>Alligator</td><td>459</td></tr><tr><td>Lion</td><td>419</td></tr><tr><td>Eagle</td><td>360</td></tr><tr><td>Gorilla</td><td>358</td></tr><tr><td>Tiger</td><td>262</td></tr><tr><td>Snake</td><td>209</td></tr><tr><td>Bear</td><td>157</td></tr></table>

## Frequently Rated Tiger Group Movies: All Time

<table><tr><td>Title</td><td>Average Rating</td><td># of Ratings</td></tr><tr><td>Lord of the Rings: The Two Towers, The (2002)</td><td>★★★</td><td>(457)</td></tr><tr><td>Shrek (2001)</td><td>★★★</td><td>(398)</td></tr><tr><td>Lord of the Rings: The Return of the King, The (2003)</td><td>★★★</td><td>(381)</td></tr><tr><td>Matrix, The (1999)</td><td>★★★</td><td>(367)</td></tr><tr><td>Lord of the Rings: The Fellowship of the Ring, The (2001)</td><td>★★★</td><td>(366)</td></tr></table>

## Comments [prev|next]

## Group Rankings: Active Members

![](/api/attachments/YJWBKFUH/fulltext/images/196a292d877af86a47f5c4baed12cca14b982078a1445d803e41c099acc6442b.jpg)

% of members from each group who logged in during the past week

myname said on September 18, 2006
What's up?

![](/api/attachments/YJWBKFUH/fulltext/images/21c625b5c6f768aa2fa3a185370056e4803e51a4077fc4985e8dba00d7f484a9.jpg)

muck\_stirrer said on September 18, 2006
How many of tigers are in this group?

![](/api/attachments/YJWBKFUH/fulltext/images/50c3b1e3bd673212843c3c1d2dcc3987a0c5fb0916e13ea3089d5498943b049c.jpg)

TNTrucker said on September 18, 2006 Breakfast at Tiffany's is pretty great!

![](/api/attachments/YJWBKFUH/fulltext/images/8d6ee5951a964f3397e00824ee41e1ac58d1582731fa28d0c800782d8dde5b0f.jpg)

snezhinka said on September 18, 2006 The tiger group likes cool movies!

![](/api/attachments/YJWBKFUH/fulltext/images/267a2b2d88e4afc2ac5092c116c8a4fd3e255a5dd6fb5d982b1de787a3c46330.jpg)

mr\_rogers said on September 18, 2006
You talkin' to me? You talkin' to me? You talkin' to me?

Leave a comment for the Tiger Group type your comments here

Add Command

Figure 2. Profile Page of the Tiger Group

## Recent Activity

## Recent Ratings

<table><tr><td>Movie Group</td><td>Movie</td><td>Average Rating in Group</td></tr><tr><td>Tiger Group</td><td>Million Dollar Baby (2004)</td><td>★★★★</td></tr><tr><td>Tiger Group</td><td>Harold and Kumar Go to White Castle (2004)</td><td>★★★★</td></tr><tr><td>Tiger Group</td><td>Invincible (2006)</td><td>★★★</td></tr><tr><td>Tiger Group</td><td>Mystery Science Theater 3000: The Movie (1996)</td><td>★★★★</td></tr><tr><td>Gorilla Group</td><td>Escape from Alcatraz (1979)</td><td>★★★★</td></tr></table>

Recent Posts

## Movie Group Post Preview

Tiger Serenity Prediction : 3.5 stars - Rating : 5 stars I love science-fiction movies, and this is a technically great rip-roaring story, so I may be b...

Tiger Group That's what I thought too. But having just gotten home from seeing it, I'm happy to report it's not bad. To be sure, it's no Citizen Kane, but it d...

Tiger Your comments admittedly made me rethink my initial and not necessarily

Group thought out response to Little Miss Sunshine. The son and uncle's "change...

![](/api/attachments/YJWBKFUH/fulltext/images/9223b3a46e39d62d5f75cbd64d4563f76937bdc7776b9d460e8d92d5fd208328.jpg)

Tiger Group The epic thread, What's the last thing you watched and what did you rate it?, always has the "Thread contains new messages" icon, even when it actually...

Bear Group Raging Bull was kind of slow and boring. Lawrence of Arabia has some interesting scenes and beautiful views but was so long and drawn out. Bleah, C...

Figure 4. An Identity Version of the Recent Activity Page

## Personal Information

Name:  
City:  
State: Southwest  
Country: United States  
Gender:  
Age:  
Favorite color:  
Web Page:

Joined MovieLens: May 2, 2005
Last visit to MovieLens: September 16, 2006

Comments [prev|next]

![](/api/attachments/YJWBKFUH/fulltext/images/7737d7e674dc31e65c7ffb64ac19f23c6cb9600f8994e1c3d06962aceeb08ce6.jpg)

dadsdayoff said on September 13, 2006
I'm supposed to see Spelldown, which you rated 4 stars.
Why was it good?

![](/api/attachments/YJWBKFUH/fulltext/images/07892a16388ec6eb55d3c58c158e8e9793697b458d25af27040fd9d748f7a1c0.jpg)

bife said on September 13, 2006 Our comedies are not to be laughed at.

![](/api/attachments/YJWBKFUH/fulltext/images/3e20881b4fc3d7c9ec28b149488bd4d1b4bdb57a1f0e1c3d56a8cb3496b2290f.jpg)

magsy said on September 13, 2006 where'd you get that picture?

![](/api/attachments/YJWBKFUH/fulltext/images/3a18aa600b409340c6b443d5139aa6d0358a6c55c390c8796fac73771271acc4.jpg)

## This user is in the Tiger Group.

MarcusLarson said on September 13, 2006 I also liked 'a day without a mexican'...nice taste

![](/api/attachments/YJWBKFUH/fulltext/images/fdee4d919c0dd5a11d7449c0f8f32199534ec2ebc87e6bf26021719379e549a0.jpg)

marliez said on September 13, 2006
Thanks for the seabiscuit recommendation in the forums

Leave a comment for galaxy type your comments here

Add Comment

![](/api/attachments/YJWBKFUH/fulltext/images/006cb68ff67ade43380e73b88b1fadff53cdb273f284e226f172a15958dea104.jpg)

Did You Know?
You and galaxy rate these movies high:

<table><tr><td>Title</td><td>galaxy&#x27;s Rating</td><td>Your Rating</td></tr><tr><td>Casablanca (1942)</td><td>★★★★</td><td>★★★★</td></tr><tr><td>Toy Story (1995)</td><td>★★★★</td><td>★★★★★</td></tr><tr><td>Clerks (1994)</td><td>★★★★</td><td>★★★★★</td></tr><tr><td>Smoke Signals (1998)</td><td>★★★★</td><td>★★★★★</td></tr><tr><td>Wallace &amp; Gromt: A Grand Day Out (1989)</td><td>★★★★</td><td>★★★★★</td></tr></table>

## You and galaxy rate these movies low:

<table><tr><td>Title</td><td>galaxy&#x27;s Rating</td><td>Your Rating</td></tr><tr><td>Con Air (1997)</td><td>**</td><td>*</td></tr><tr><td>Addams Family Values (1993)</td><td>*</td><td>**</td></tr><tr><td>Big Momma&#x27;s House (2000)</td><td>*</td><td>*</td></tr><tr><td>Flintstones, The (1994)</td><td>*</td><td>*</td></tr><tr><td>Ace Ventura: When Nature Calls (1995)</td><td>*</td><td>*</td></tr></table>

## You and galaxy disagree on these movies:

<table><tr><td>Title</td><td>galaxy&#x27;s Rating</td><td>Your Rating</td></tr><tr><td>Booge Nights (1997)</td><td>*****</td><td>*j</td></tr><tr><td>Office Space (1999)</td><td>*</td><td>*****</td></tr><tr><td>Aladdin and the King of Theves (1996)</td><td>*</td><td>*****j</td></tr><tr><td>Wizard of Oz, The (1939)</td><td>j</td><td>*****</td></tr><tr><td>Bull Durham (1988)</td><td>j</td><td>*****</td></tr></table>

## MovieLens recommends these movies that galaxy rated high:

<table><tr><td>Title</td><td>galaxy&#x27;s Rating</td><td>Your Prediction</td></tr><tr><td>Moulin Rouge (2001)</td><td>*****</td><td>*****</td></tr><tr><td>Rashomon (Rashomon) (1950)</td><td>*****</td><td>*****</td></tr><tr><td>Out of the Past (1947)</td><td>*****</td><td>*****</td></tr><tr><td>Lower Depths, The (Donzoko) (1957)</td><td>*****</td><td>*****</td></tr><tr><td>Seven Samurai (Shichinin no samurai) (1954)</td><td>*****</td><td>*****</td></tr></table>

## You and galaxy have posted together in these threads:

Thread
If you could only have 10 movies...
New Feature: Movie Linking

Figure 3. Profile Page of a Fictitious Member Named Galaxy

## Recent Ratings

## Recent Activity

<table><tr><td colspan="2">Username</td><td>Movie</td><td>Their Rating</td></tr><tr><td rowspan="2"><img src="/api/attachments/YJWBKFUH/fulltext/images/3326d77175504d18da5e2f7eae5b92f7589f6e71fe468f368ebe048b13916597.jpg"/></td><td>galaxy</td><td>Children of Paradise (Les enfants du paradis) (1945)</td><td>★★★★</td></tr><tr><td>MarcusLarson</td><td>Scanner Darkly, A (2006)</td><td>★★★i</td></tr><tr><td>[3030]</td><td>jenn023</td><td>Graduate, The (1967)</td><td>★★i</td></tr><tr><td rowspan="2"><img src="/api/attachments/YJWBKFUH/fulltext/images/8c181ce076e5563f3272d71ad6c7e27e17e10db2900039bd5eb7137e6b8ac24c.jpg"/></td><td>elfin</td><td>Thomas Crown Affair, The (1999)</td><td>★★</td></tr><tr><td>dispenser</td><td>Brick (2005)</td><td>★★★i</td></tr></table>

## Recent Posts

<table><tr><td colspan="2">Username</td><td>Post Preview</td></tr><tr><td>(vx35)</td><td>galaxy</td><td>Disagree entirely. Best line is when the lights go out and someone in the background yells, &quot;SNAKES!&quot; --DiB...</td></tr><tr><td>(YH80)</td><td>MarcusLarson</td><td>Yeah, but it wouldn&#x27;t have been as funny! Man, I&#x27;d like to see that movie as a musical. That might be the only way I&#x27;d go (and I LIKE Jason Statham....</td></tr><tr><td><img src="/api/attachments/YJWBKFUH/fulltext/images/902855a35c20b2a0d746979d39d997253cfbfd25d2a1126008f02430e1303a00.jpg"/></td><td>dispenser</td><td>Raging Bull was kind of slow and boring. Lawrence of Arabia has some interesting scenes and beautiful views but was so long and drawn out. Bleah. C...</td></tr><tr><td><img src="/api/attachments/YJWBKFUH/fulltext/images/6b6ea30b281789a8e68471799337c6849daca117b1ecf3e31f82fc5e539bfa47.jpg"/></td><td>mod</td><td>Annie Prouk wrote that scene better than it was adapted for the screen. In the short story the sex scene is graphic but you can feel the raw powe...</td></tr><tr><td><img src="/api/attachments/YJWBKFUH/fulltext/images/bca14fe4372969312205f6075d75d02457f4f78f84bb5a8a11381e0abe27c0a8.jpg"/></td><td>PIIR</td><td>Your comments admittedly made me rethink my initial and not necessarily thought out response to Little Miss Sunshine. The son and uncle&#x27;s &quot;change...</td></tr></table>

Figure 5. A Bond Version of the Recent Activity Page

## Group Versus Interpersonal Communication

We created two versions of the communication feature, which allowed public discussion with one's group (in the identity-based condition) or private discussion with other members (in the bond-based condition). Figure 2 shows the group communication feature in the lower right corner of the group profile page. Comments entered in a text-entry box were displayed along with the date of posting, the author's name, and the author's group icon. All messages were displayed in reverse chronological order and were paginated so only five comments appeared at a time. Only members of a movie group could read and write comments on the group's profile page. Figure 3 shows the interpersonal communication feature in the lower left corner of an individual profile page. Any member could leave comments for any other member. When members viewed their own individual profile, they saw the comments others left for them as well as all comments they left for others.

## Participants

We recruited all MovieLens subscribers (except seven extremely active members whose inclusion might bias our results) who visited MovieLens during the experimental period. Of the 4,818 participants, 1,544 were assigned randomly to the control condition, 1,625 to the identity-based condition, and 1,649 to the bond-based condition.

Our design included a control group and two conditions (identity-based and bond-based) subdivided by a full-factorial design with seven conditions as follows: (1) profile only, (2) recent activity only, (3) communication only, (4) profile and recent activity, (5) recent activity and communication, (6) profile and communication, (7) profile, recent activity, and communication. Altogether, there were 15 conditions: seven identity-based conditions, seven bond-based conditions, plus a control condition. This design allowed us to examine the distinct effects of the features used to induce identity and bond-based attachment, as well as their combined effects.

## Procedure

The field experiment took place from January 27, 2007, to July 27, 2007, in the natural environment of MovieLens. The field experiment enabled us to observe member behavior over a substantial period of time. It also enabled us to examine how members with different levels of prior experience with the site responded to the manipulated community features.

We constructed a splash page that described the experiment as a user study to explore new features being considered for MovieLens. Potential participants were informed that they might receive different features during the test, and that afterward we planned to offer the most valuable features to all members. In their first login session (after the launch of the experiment), participants reviewed the splash page with a brief description of the new features they were assigned, and saw the option to share their movie ratings (80 percent did so). The new features defined by a participant's experimental condition were available for the rest of the experimental period. When participants in the control condition returned to MovieLens, they continued seeing the old version of MovieLens without any of the new features.

Those in the identity-based condition first saw recent activities of their own and other movie groups on their front page and then had the option to click to view group profiles, to communicate with their assigned group on its profile page, and to participate in forum discussion as group members (with group name and icon shown next to their posts). Those in the bond-based condition first saw recent activities of a small set of MovieLens users on their front page and had the option to click to view individual user profiles, to communicate with other people on their profile page, and to participate in forum discussion as individual members (with user name and picture shown next to their posts).

## Dependent Variables and Statistical Analyses

Self-reported attachment. At the end of the experiment, we e-mailed a post-test survey to 2,073 members who had given us permission to contact them; 107 of these e-mails bounced. After a single e-mail reminder, 280 people responded, a response rate of 14.2 percent. Of the 280 respondents, 107 had been assigned to the control condition, 82 to the identity-based condition, and 91 to the bond-based condition. Compared to nonrespondents, respondents had visited the site more frequently before and during the experiment (p < .01) and rated more movies (p < .01), but did not read more posts (p = .14).

The questionnaire asked the participants to report their familiarity with the new features, usefulness of the new features, and the reasons they visited MovieLens. We adapted scales from Prentice et al. (1994) and Sassenburg (2002) to measure attachment. Participants reported on five-point Likert scales how strongly they felt attached to MovieLens as a whole, to their movie group (identity-based attachment), and to a frequently seen MovieLens member (bond-based attachment). We selected the frequently seen member based on each participant's actual exposure to three members whom they had seen during the experiment. We asked them to report how familiar they were with each member, and their feelings toward the member with whom they reported being the most familiar.

Responses to the 15 questionnaire items for half the sample were subjected to an exploratory factor analysis. The maximum likelihood method was used to extract the factors, followed by an oblique rotation because attachment at different levels tends to be correlated (Sassenberg 2002). Two items measuring attachment to the participant's movie group (I am interested in learning more about [group name] and I would like to be with [group name] in the future) and two items measuring attachment to a particular person (I felt close to [member name] and [member name] has influenced my thoughts and behaviors) loaded on more than one factor. We dropped these items, resulting in three meaningful factors, with factor loadings displayed in Table 2. Confirmatory factor analysis with the remaining half of the sample showed similar loading patterns. The three-factor model shown in Table 2 is a good fit to the data, with NFI, NNFI, and CFI greater than 0.90 and an insignificant Chi-Square, $\chi^2$ (41, N = 184) = 52.64, $p = 0.11$ .

We averaged the five items with significant loadings ( $\geq .40$ ) on Factor 1 to measure attachment to MovieLens as a whole, the three items with significant loadings on Factor 2 to measure attachment to the participant's movie group, and the three items with significant loadings on Factor 3 to measure attachment to a frequently seen member. We also ran all analyses including all items and the results remained largely unchanged.

Retention. We measured retention as the number of days a participant remained as a member of MovieLens (i.e., days between their first and last visit for participants who left the site and days between their first visit and the end of our experiment for participants who did not leave the site). We classified participants as having left the site if they failed to log in after 50 days, which is three standard deviations longer than the average inter-login duration. We analyzed the data using survival analysis procedure PROC LIFEREG in SAS, with the type of attachment manipulation (control, identity, and bond) as the independent variable, controlling for member history and days in the experiment.

Participation - Visit Frequency. Visit frequency is the average number of sessions participants logged in during the experiment. The data were collected at the member level. Because the number of login sessions is count data, with a distribution truncated at one, we fit the data with a Poisson regression model. We used PROC GENMOD in SAS to perform the analyses, with the type of attachment manipulation (control, identity, and bond) and feature manipulation (profile page, recent activity page, communication channel) and their interactions as the independent variables. To control for the fact that participants who joined the experiment earlier had more days to visit, we included days in the experiment as a control variable.

Participation – Post Views. Post views are the number of posts a participant viewed in the discussion forums per login session. The forums are a venue through which MovieLens members can interact with one another. They were part of the MovieLens site before our experiment, were distinct from the communication features embedded in profile pages, and were available to all participants. We use post views as a proxy to measure participation for three reasons. First, posting behaviors were sparse in our data, as in many other communities; only a small fraction of members have posted. Second, viewing and posting are moderately correlated (r = 0.42). Third, Preece et al. (2004) have shown that “lurkers” (those who view only others’ posts) perceive themselves and are accepted by posters as members of an online community. Further, lurking is a valuable way of learning about an online community. The data were collected at the member-session level. Because views are count data with many members participating in more than one session, we fit the data with a mixed Poisson regression model with sessions nested within members using PROC GLIMMIX in SAS. Again we tested the effects of the attachment manipulations (control, identity, and bond), feature manipulations (the presence of the profile page, the recent activity page, and the communication channel), and their interactions.

Movie Ratings to Help Others. During each login session, we recorded the number of movies that participants rated in a “volunteer center.” The volunteer center included a statement saying, “We’ve put together a list of new movies for you to rate that will help groups of members or other members get better movie recommendations. Click on the link below to start rating.” The participant could click the link to “help a movie group” or to “help a member,” or neither option. More movie ratings signal greater willingness to contribute to help a group or individual members. The data were collected at the member-session level. As with the analyses of forum post views, we fit the data with a mixed Poisson regression model. We used PROC GLIMMIX in SAS to perform the analyses with attachment manipulation (identity versus bond) and the target (groups versus individual members) as the independent variables. Participants in the control condition had no access to the volunteer center. Therefore, they were not included in the analysis of movies rated.

<table><tr><td colspan="4">Table 2. Questionnaire Items to Measure Attachment and Factor Loading</td></tr><tr><td>Attachment to MovieLens</td><td>Attachment to Movie Group</td><td>Attachment to frequently seen other</td><td>Questionnaire Items</td></tr><tr><td>.85</td><td>.03</td><td>-.02</td><td>I like MovieLens as a whole.</td></tr><tr><td>.74</td><td>.04</td><td>.04</td><td>I intend to visit MovieLens in the future.</td></tr><tr><td>.78</td><td>-.06</td><td>-.01</td><td>I would recommend MovieLens to my friends.</td></tr><tr><td>.46</td><td>-.03</td><td>.08</td><td>MovieLens is important to me.</td></tr><tr><td>.78</td><td>.04</td><td>-.03</td><td>MovieLens is very useful to me.</td></tr><tr><td>-.03</td><td>.95</td><td>.04</td><td>I identify with the [group name] group.</td></tr><tr><td>.01</td><td>.99</td><td>.00</td><td>I feel connected to [group name].</td></tr><tr><td>.05</td><td>.79</td><td>.06</td><td>I feel I am a typical member of [group name].</td></tr><tr><td>.03</td><td>.04</td><td>.88</td><td>I would like to be friends with [member name].</td></tr><tr><td>.01</td><td>.04</td><td>.95</td><td>I am interested in learning more about [member name].</td></tr><tr><td>-.01</td><td>.01</td><td>.97</td><td>I would like to interact with [member name] in the future.</td></tr></table>

Newcomer or old-timer. We controlled for member history in all analyses, that is, whether a participant was a newcomer who had used MovieLens fewer than 30 days before the start of the experiment, or an old-timer with more prior experience with MovieLens. Of 4,818 participants, 3,678 or 76.3 percent were newcomers and 1,140 or 23.7 percent were old-timers. Results remained the same when newcomers were defined as those with less than three or six months of experience.

## Results

During the experiment, the average participant visited MovieLens 5.43 times or roughly once per month, viewed 10 messages in the discussion forums, and rated 83 movies including an average of one movie in the volunteer center. In the identity-based conditions, the 1,625 participants were exposed to recent activities of movie groups an average of 36 times (SD = 107.7); 1,135 or 70 percent viewed group profiles one or more times (mean = .79 and SD = 3.12); and 72 left 98 comments. In the bond-based conditions, the 1,649 participants were exposed to recent activities of individual members an average of 32 times (SD = 107.1); 578 or 35 percent viewed individual profiles one or more times (mean = .48, SD = 11.42); 20 left 24 comments.

Participants reported on the questionnaire that they had seen most of the manipulated features, but had not used them regularly. The most popular features were the recent activity page and the individual and group profiles. The part of the profile pages that compared ratings behavior was especially popular. The recent activity, profile page, and movie group features were also reported as being useful, while the communication feature was the least useful. Because only 2 percent of participants ever used the communication features, we excluded this dimension from further analyses.

## Effects of Community Features on Self-Reported Attachment (Hypotheses 1a, 1b, and 1c)

Hypothesis 1a and 1b posit that features that focus members' attention on a group or on individual members, respectively, will increase attachment to those entities. Hypothesis 1c posits that increased attachment to the group or individual members will increase attachment to the community as a whole. The results, summarized in the first three rows of Table 3, provide consistent support for the positive effects of identity-based features but weaker support for the bond-based features. Compared with the control condition, participants in the identity condition increased their attachment to their movie group (76 percent, p < .001), followed by attachment to a frequently seen other (17 percent, p = .05), and attachment to MovieLens as a whole (7 percent, p = .002). Compared with participants in the control condition, those in the bond condition increased their attachment to their movie group (27 percent higher, p = .004) but not to a frequently seen other (9 percent, p = .30) or to MovieLens as a whole (1 percent, p = .64). Thus H1a was fully supported, and H1b and H1c were partially supported.

<table><tr><td rowspan="2">Dependent Variables</td><td rowspan="2"></td><td colspan="3">Attachment Conditions</td><td colspan="4">Differences across Conditions</td></tr><tr><td>Control</td><td>Identity</td><td>Bond</td><td colspan="2">Control vs. Identity</td><td colspan="2">Control vs. Bond</td></tr><tr><td></td><td>N</td><td></td><td></td><td></td><td>F</td><td>p</td><td>F</td><td>P</td></tr><tr><td>Attachment to movie group (H1a)</td><td>200</td><td> $1.69_a$ (0.11)</td><td> $2.97_c$ (0.11)</td><td> $2.15_b$ (0.11)</td><td>56.48</td><td>.001</td><td>7.09</td><td>.004</td></tr><tr><td>Attachment to frequently seen other (H1b)</td><td>202</td><td> $2.08_a$ (0.12)</td><td> $2.43_b$ (0.13)</td><td> $2.26_a$ (0.12)</td><td>4.03</td><td>.05</td><td>1.11</td><td>.3</td></tr><tr><td>Attachment to MovieLens (H1c)</td><td>272</td><td> $3.91_a$ (0.06)</td><td> $4.19_b$ (0.07)</td><td> $3.95_a$ (0.07)</td><td>3.59</td><td>.002</td><td>0.08</td><td>.64</td></tr><tr><td>Visit frequency (H2a)</td><td>4818</td><td> $4.96_a$ (0.90)</td><td> $7.15_c$ (1.08)</td><td> $5.52_b$ (0.90)</td><td>584.6</td><td>.001</td><td>43.52</td><td>.001</td></tr><tr><td>Forum post views (H2a)</td><td>26198</td><td> $.055_a$ (0.005)</td><td> $.075_b$ (0.007)</td><td> $.057_a$ (0.005)</td><td>2.46</td><td>.01</td><td>0.38</td><td>.7</td></tr></table>

Note: Means having the same subscript are not significantly different at p < .05 for attachment and p < .01 for visit frequency and post views. Standard errors are included in parentheses.

## Effects of Community Attachment on Participation and Retention (Hypotheses 2a and 2b)

Hypothesis 2a and 2b posit that feelings of attachment will increase participation and retention and mediate the effects of identity-based and bond-based features on these behaviors. Analysis of visit frequency and forum post views, shown in Table 3, provide strong support for the effectiveness of the identity-based features in increasing participation, and mixed support for the effectiveness of bond-based features. Compared with participants in the control condition, those exposed to identity features visited MovieLens 44 percent more frequently (Table 3, fourth row) and viewed 36 percent more forum posts (Table 3, fifth row). Compared with participants in the control condition, those exposed to bond features visited MovieLens 11 percent more often (Table 3, fourth row) but did not reliably increase their views of forum posts (Table 3, fifth row).

To test the mediating role of attachment between community features and participation, we conducted a mediation analysis following Baron and Kenny (1986). We regressed self-reported attachment on the identity and bond manipulations, regressed visit frequency on identity and bond manipulations, and regressed visit frequency on both identity and bond manipulations and self-reported attachment simultaneously. The analyses show that attachment partially mediated the effects of identity and bond features on visit frequency. After attachment was introduced into the regression predicting visit frequency, the positive effects of the identity-based manipulations decreased from .829 (p < .01) to .632 (p = 0.03), and the positive effects of bond-based manipulations decreased from .778 (p < 0.01) to .632 (p = 0.07). These results suggest that the effects of our identity-based and bond-based features on participation were at least partly mediated by changes in attachment to the movie group or an individual member, as predicted by H2a. We also ran mediation analysis with forum post views as the dependent variable. However, there were no significant results due to the small number of survey respondents who had viewed posts.

We tested the hypothesized effects of identity-based and bond-based features on retention by examining differences across the conditions in the average duration of activity in the community. All independent variables were time-invariant variables—newcomer versus old-timer, days in the experiment, and attachment conditions. The Wald test indicated a significant negative effect on retention of being a newcomer ( $\beta = -1.87, p < .001$ ) and joining the experiment earlier ( $\beta = -0.02, p < .001$ ), and no significant effect of the attachment manipulations (p = .25 for identity versus control and p = .71 for bond versus control). While the identity-based features and bond-based features increased the intensity of use, they did not increase long-term member retention.

## Differential Effects of Attachment to Groups Versus Individuals (Hypothesis 3a and 3b)

Hypothesis 3a posits that identity-based attachment will lead to more movie ratings to help the group, whereas hypothesis 3b posits that bond-based attachment will lead to more movie ratings to help individuals. The analysis testing these hypotheses includes only participants in the identity and bond conditions. Overall, participants rated slightly more movies for groups than for individuals $p < .01$ but contrary to hypotheses 3a and 3b, participants in the identity condition were slightly more likely to rate movies for a frequently seen member than for their movie group, whereas participants in the bond condition were slightly more likely to rate movies for their movie group than for a frequently seen member (interaction p = .05). Because these results are comparatively weak, we hesitate to speculate on their explanation. Perhaps because we presented the volunteer center as part of our new feature offerings, participants' movie ratings might have reflected their curiosity to explore the unavailable features (e.g., participants in the identity condition wanted to learn more about individual members after seeing features about groups), rather than their willingness to help.

<table><tr><td rowspan="2" colspan="2">Dependent Variables</td><td></td><td colspan="2">Attachment Conditions</td><td colspan="2">Interaction between attachment and target</td></tr><tr><td>N</td><td>Identity</td><td>Bond</td><td>F</td><td>P</td></tr><tr><td rowspan="2">Self-Reported Attachment</td><td>Attachment to one&#x27;s movie group</td><td>117</td><td> $2.92_b$ (0.126)</td><td> $2.16_a$ (0.123)</td><td rowspan="2">9.86</td><td rowspan="2">.002</td></tr><tr><td>Attachment to a frequently seen other</td><td>117</td><td> $2.44_a$ (0.14)</td><td> $2.27_a$ (0.14)</td></tr><tr><td rowspan="2">Willingness to Help</td><td>Movies rated to help one&#x27; movie group</td><td>14055</td><td> $.0061_a$ (0.001)</td><td> $.0080_a$ (0.001)</td><td rowspan="2">4.78</td><td rowspan="2">.05</td></tr><tr><td>Movies rated to help a frequently seen other</td><td>14055</td><td> $.0073_a$ (0.001)</td><td> $.0058_a$ (0.001)</td></tr></table>

Note: Means having the same subscript are not significantly different at p < .05 for attachment and p < .01 for contribution. Standard errors are included in parentheses.

We argued that identity-based attachment and bond-based attachment are independent mechanisms that lead to a sense of community. In partial support of this idea, we found that participants in the identity condition reported greater attachment to their movie group than to a frequently seen other (2.92 versus 2.44 in Table 4, rows 1 and 2 in the Identity column). By contrast, participants in the bond condition reported a roughly equal level of attachment to their movie group and to a frequently seen other (2.27 versus 2.16 in Table 4, rows 1 and 2 in the Bond column). The interaction was significant (p = .002).

## Effects of Community Features on Participation Behaviors

We conducted post hoc analyses to learn about the combined effects of the new features. We found a main effect of the profile pages $p < .001$ on login sessions, an interaction between repeated exposure and the attachment manipulation $p < .001$ , and a third-order interaction between profile pages, repeated exposure, and the attachment manipulation $p < .001$ . As shown in Figure 6, participants with access to profile pages, across identify and bond conditions, visited MovieLens more frequently than those without the access. Repeated exposure to group activities increased visit frequency in the identity conditions $p < .001$ but not in the bond conditions $p = .23$ . Participants in the identity condition with access to both group profiles and repeated exposure to their group visited MovieLens almost twice as frequently (11.6 times on average) compared with participants in the other conditions (5.7 times on average; p < .01).

## Differential Effects on Newcomers Versus Old-Timers

Additional analyses suggested that newcomers and old-timers responded differently to the newly introduced community features. Both sets of features increased newcomers' self-reported attachment and level of participation compared with newcomers' behavior in the control condition (p < .001). As shown in Figure 7, compared to newcomers in the control condition (5.0 logins), newcomers in the identity features visited MovieLens 7.8 times (a 56 percent increase, p < .01) and those in the bond condition visited 6.0 times (a 20 percent increase, p < .01). By contrast, compared to old-timers in the control condition (4.8 logins), old-timers in the identity condition visited MovieLens 5.5 times (a 10 percent increase, p < .01) while those in the bond condition actually reduced their number of visits (4.2 logins or a 16 percent decrease, p < .01).

![](/api/attachments/YJWBKFUH/fulltext/images/e3791b3d1a476fbf02fa032954c4d424347ffae9205c5400ec0980c1c1060d92.jpg)

![](/api/attachments/YJWBKFUH/fulltext/images/2a68502494720129dde7a446c9c5a60c7841dbc32dc559bbb026054480011601.jpg)  
Figure 6. Effects of Profile Page and Repeated Exposure on Visit Frequency

![](/api/attachments/YJWBKFUH/fulltext/images/50e3e4c8a0afc436f3a6cc82e92ba8fb6125d79cf66b7bbeb243fbc071983aa0.jpg)

Figure 7. Visit Frequency of Old-Timers Versus Newcomers

We observed a similar pattern in post views in the discussion forums. As shown in Figure 8, on average, newcomers viewed more posts than old-timers across all conditions (p < .01). Also, compared with their counterparts in the control condition (.09 views), newcomers in both the identity and bond conditions viewed more posts (.12 views, a 33 percent increase for identity, p < .05 and .1 views, an 11 percent increase for bond, p = .39). By contrast, compared with their counterparts in the control condition (.043 views per visit), old-timers in the identity condition viewed 53 percent more posts (.066 views, p < .01), but old-timers in the bond condition viewed 12 percent fewer posts (.038 views). This difference, however, is not statistically significant.

## Laboratory Experiment

The field experiment suggested that identity-based features were more powerful in building attachment than bond-based features but this study had an important limitation. Although we randomly assigned identity- and bond-based features to MovieLens users, we could not ensure that participants actually used them or were equally exposed to the features in the different experimental conditions. The behavioral data show there was unequal exposure. Participants in the bond condition used the communication features at about 25 percent of the frequency of those in the identity condition. Participants in the bond condition were also 50 percent less likely to check profiles than those in the identity condition. It is possible that the low impact of bond-based features on attachment occurred because of a lack of sufficient exposure to these features.

We conducted a supplementary, hour-long laboratory experiment that addressed this limitation. A group of 56 participants (half male, half female) were recruited from a mid-Atlantic university. The group consisted of 38 undergraduates and 18 graduate students or staff. All participants were unfamiliar with MovieLens prior to the study. In the first stage of the experiment, participants registered for MovieLens and learned its basic features. As part of this process, participants rated at least 15 movies and checked at least 5 movie detail pages, after which all participants spent 45 minutes exploring MovieLens.

![](/api/attachments/YJWBKFUH/fulltext/images/224c5b29a4419f5bf94ff8f15561ea0bf4091f6a3733affb6a4480de330e4b06.jpg)  
Figure 8. Post Views of Old-Timers Versus Newcomers

The experiment replicated the three between-groups experimental conditions in the field experiment: the control condition, in which participants used the classic MovieLens features; an identity-based condition, in which participants were exposed to all three identity-based features (group profiles, repeated exposure to group activities, and group communication); and a bond-based condition, in which participants were exposed to all three bond-based features (individual profiles, repeated exposure to a small set of users, and individual communication). To enhance experimental control, we constructed a set of approximately equivalent tasks, instructing participants to explore the control, identity-based, and bond-based features, respectively. Participants in the identity condition were asked to look at movie ratings, posts, and profiles associated with groups, and to leave comments on their group's profile page. Participants in the bond condition were asked to look at movie ratings, posts, and profiles from individual users, to update their own profile, and to leave comments for other users.

After they had explored MovieLens, participants completed the attachment questionnaire. They were instructed to imagine being a regular MovieLens member and to report what their reactions would be if they had been using MovieLens for six months. Results from the laboratory experiment supported Hypothesis 1a, 1b, and 1c. As shown in Table 5, participants in both the identity-based and bond-based conditions reported stronger attachment to MovieLens than did participants in the control condition (3.66 and 3.61 versus 2.97, p < .05). They also reported stronger attachment to their movie groups and to the individual members to whom they were exposed.

We did not find support for Hypothesis 3a and 3b; the interaction between experimental manipulation and the target of the attachment was not significant, F (1, 35) = 0.28, p = .6. Participants in both experimental conditions increased their attachment to their movie group and to a frequently seen other member compared with the control condition (p < .02). The increased attachment was stronger toward the group than toward a person in both experimental conditions (p < .05). Due to a lack of behavioral data, we did not test Hypotheses 2a and 2b or the effects on willingness to help in Hypothesis 3a and 3b.

## Discussion

In this article, we show how insights from group identity and interpersonal bonds theories can be leveraged to increase member attachment in online community design. We first reviewed the literature and identified a set of theoretical antecedents to the two types of attachment: identity-based and bond-based. We implemented the two sets of antecedents as two sets of community features in MovieLens, an online movie-recommendation website, and compared their effects with a control condition that had neither set of features. Table 6 summarizes our hypotheses and main findings. A key take-away message from our study is that theory-inspired design can be effective. Despite the limits we imposed on our design to ensure experimental comparisons, our experimental results provide support for the effectiveness of the new features in strengthening member attachment. In the field experiment, both sets of features increased self-reported attachment to movie groups and frequency of visits to MovieLens. The identity features also increased attachment to MovieLens as a whole and increased the number of post views in the forums. In the laboratory experiment, both sets of features increased attachment to MovieLens, to the member's movie group, and to individual members.

Table 5. Effects of Identity- and Bond-Based Features on Self-Reported Attachment in the Laboratory Environment

<table><tr><td rowspan="3">Dependent Variables</td><td rowspan="2"></td><td colspan="3">Attachment Conditions</td><td colspan="4">Differences Among Conditions</td></tr><tr><td>Control</td><td>Identity</td><td>Bond</td><td colspan="2">Control vs. Identity</td><td colspan="2">Control vs. Bond</td></tr><tr><td>N</td><td></td><td></td><td></td><td>F</td><td>P</td><td>F</td><td>P</td></tr><tr><td>Attachment to movie group (H1a)</td><td>56</td><td> $2.42_a$ </td><td> $3.56_b$ </td><td> $3.82_b$ </td><td>5.33</td><td>.02</td><td>5.60</td><td>.02</td></tr><tr><td>Attachment to frequently seen other (H1b)</td><td>56</td><td> $2.36_a$ </td><td> $3.16_b$ </td><td> $3.29_b$ </td><td>7.39</td><td>.009</td><td>10.92</td><td>.002</td></tr><tr><td>Attachment to MovieLens (H1c)</td><td>56</td><td> $2.97_a$ </td><td> $3.66_b$ </td><td> $3.61_b$ </td><td>3.92</td><td>.05</td><td>3.30</td><td>.07</td></tr></table>

Note: Means having the same subscript are not significantly different at p < .05.

<table><tr><td colspan="4">Table 6. Summary of Hypotheses and Main Findings</td></tr><tr><td></td><td>Field Experiment</td><td>Lab Experiment</td><td>Comments</td></tr><tr><td colspan="4">Community features emphasizing identity or bonds increase self-reported attachment to individuals, movie groups, and the large community (H1a, H1b, H1c)</td></tr><tr><td>Greater attachment to one&#x27;s movie group</td><td>Supported</td><td>Supported</td><td></td></tr><tr><td>Greater attachment to frequently seen other</td><td>Not supported</td><td>Supported</td><td></td></tr><tr><td>Greater attachment to MovieLens</td><td>Supported for identity</td><td>Supported</td><td></td></tr><tr><td colspan="4">Community features increase greater retention and participation (H2a, H2b)</td></tr><tr><td>Greater frequency of visiting MovieLens</td><td>Supported</td><td>N/A</td><td>Strongest effect with profiles and repeated exposure in the identity condition</td></tr><tr><td>More post views in the discussion forums</td><td>Supported for identity</td><td>N/A</td><td></td></tr><tr><td>Greater duration of membership</td><td>Not supported</td><td>N/A</td><td></td></tr><tr><td colspan="4">Differential effects of identity and bond on willingness to help group versus member (H3a, H3b)</td></tr><tr><td>Greater attachment to group in identity and to member in bond</td><td>Partially supported</td><td>Not supported</td><td></td></tr><tr><td>More likely to help groups in identity and to help members in bond</td><td>Disconfirmed</td><td>N/A</td><td>Interaction opposite to prediction</td></tr><tr><td colspan="4">Other findings</td></tr><tr><td>Interaction between profile and repeated exposure features</td><td colspan="3">Members in the identity condition with access to group profile and repeated exposure doubled their visit frequency. Members in the bond condition with access to individual profiles increased their visit frequency (no interaction)</td></tr><tr><td>Interaction between features types and members&#x27; prior experience</td><td colspan="3">Identity features increased visit frequency and post views for both old-timers and newcomers. Bond features increased visit frequency and post views for newcomers but reduced both for old-timers</td></tr></table>

Of all the findings, the most surprising is the consistently stronger effects of the identity-based features compared with the bond-based features. We offer two possible explanations for this difference. One possibility is that identity-based attachment is easier to establish than bond-based attachment. In previous research, experimentalists have created group identity easily, by assigning groups a name or giving them a distinctive t-shirt (for a review, see Hogg 2001). By contrast, interpersonal bonds are often slow to develop (Berscheid and Reis 1998). They require opportunities for repeated, one-on-one interactions and self-disclosure with others, and can be particularly difficult to establish in online communities whose members visit infrequently. Although the field experiment lasted six months, many participants never saw or communicated frequently enough with others for these bonds to develop.

The other possibility is that a movie recommendation website may not inspire friendship in the same way that would, say, a social networking site. Most people join MovieLens because they have an interest in finding good movies, and few join to make friends or seek others who share their interest in movies. Therefore, we faced a significant barrier to fostering interpersonal bonds in this community. Established members had little intrinsic interest in the bond-based features. As one member commented, “I do enjoy [movie] ratings, predictions, graphs and classifications....[The] social aspect of it doesn’t mean [anything to] me.” The specific purpose of MovieLens, that is, to give people movie recommendations, may have made the identity-based features a more natural fit. In contrast, features designed to increase bond-based attachment, especially one-on-one communication, were unsuccessful and rarely used. This failure had a stronger effect on the bond manipulation than on the identity manipulation because prior research suggests that one-on-one communication is one of the most powerful techniques for creating bonds but is not needed to create group identity.

Another surprising finding was that the manipulated community features influenced community participation more than they influenced member retention. The features were effective in causing our participants to report a stronger attachment to the site, to visit the site more frequently and to view more posts (in the identity condition), but they failed to increase the duration of active membership. The lack of an effect on retention seems inconsistent with the logic of attachment or commitment that we and others have used, that is, as variables that influence both active participation and retention. However, others studying online communities have found that interventions influenced participation but not retention (Choi et al. 2010). These findings suggest that participation and retention online might be more independent of one another than they are offline. Retention might be strongly affected by the presence of attractive competing sites where participants can pursue the same interests or purpose. Unlike the situation in many offline groups or organizations, online communities compete vigorously for people's time and attention. Someone interested in movies can easily move his active participation from one movie community to another, effectively separating these behaviors.

## Limitations

We conducted this work in a primarily identity-based community. We think the findings could be generalized to many online communities that are organized around a particular topic such as health support, education, a hobby, or a profession (Preece 2000; Ridings and Gefen 2004). Some of our findings, such as the comparative ease of fostering identity-based attachment as opposed to bond-based attachment, might not generalize to socially oriented communities such as friendship groups or social networking sites where members join for intimate relationships or have established relationships. In these communities, fostering bond-based attachment will become easier and creating subgroups may depersonalize or dilute intimacy among members. Similar caution needs to be taken to generalize our findings to online communities hosted by organizations to foster collaboration among their employees. Compared with members of leisure or volunteer communities, organizational employees often have built affective connections with the organization and its employees. Researchers should examine ways to adapt our features to leverage these preexisting connections and both our identity- and bond-based features are likely to significantly affect user behaviors in these communities.

We were constrained by the desire to have parallelism between the identity and bond conditions, so our community features tested only a subset of interesting theoretical ideas. For instance, even though group interdependence, through a joint task, purpose, or reward, strongly induces a common group identity (Sherif et al. 1961), we did not implement a feature based on group interdependence because there was no parallel implementation to introduce in the bond condition. We also separately introduced features to induce either identity-based or bond-based attachment, even though many real communities want to encourage both. In this article, we also limited ourselves to drawing insights from theories of group identity and interpersonal bonds, even though many other social science theories are available as a source of inspiration (e.g., Kollock 1998; Ling et al. 2005). In the future, researchers could and should explore a broader set of theoretical concepts such as group interdependence, goal setting, public goods, and social exchange. Future research should also help us understand how to apply theory to other outcomes such as joining (Krogh et al. 2003), trust (Stewart and Gosain 2006), network evolution (Oh and Jeon 2007), and prevention of deviant behaviors (Friedman and Resnick 2001).

## Theoretical Implications

Our study makes three contributions to the Information Systems literature on online communities. First, our findings showcase two different mechanisms for building member attachment in online communities—by focusing members' attention on a group and its activities or by focusing members' attention on individual members and their activities. Attachment to these entities in an online community leads to attachment to the large community as a whole. Our study adds new insights to the body of knowledge on member attachment and commitment and ways to build successful online communities. Another insight that we contribute is the relative ease of fostering identity-based versus bond-based attachment in online communities, which needs to be further tested in future research. Our second contribution is to show the significant effects of increased attachment on member behaviors that are vital to community success. The new features that provided detailed information about groups and individuals increased member attachment, which in turn led to more frequent visits to the website. Our third contribution is to show the value of mining social science theories to gain new insights into understanding online communities. Our exercise of using insights from the group identity and interpersonal bonds literature to increase member attachment demonstrates the effectiveness of such an approach. It also reveals some challenges in properly implementing theories from the offline context to the online context where, among other things, there are fewer opportunities for repeated interactions, yet there are a multitude of easily available alternatives to connect people.

Our attempt to apply social psychological theory also revealed gaps in the literature where theory can be further refined or extended. Identity and bond theories (Prentice et al. 1994) posit crisp distinctions between group identity and interpersonal bonds as bases of attachment in groups. Identity theories emphasize differences between groups, ignoring heterogeneity among group members, and give little guidance about how interpersonal bonds might arise in such groups. Likewise, bond-based theories do not treat how group identity emerges. Our experimental results suggest that the relationship between attachment to the group and to individual members may be affected by the type of the online community. The correlation between self-reported attachment to participants' movie groups and to their frequently seen individual was significantly lower in the identity condition (r = .42) than in the bond condition (r = .69; for the difference p < .001). While these results support the theoretical distinction between the two types of attachment, they also suggest some interesting patterns between the two. If one imagines a $2 \times 2$ matrix of attachment, identity-based and bond-based attachment may be both high or both low, or identity-based attachment may be high bond-based attachment may be low, but the scenario of low identity-based attachment and high bond-based attachment seems to be less common.

A possible reason is spillover effects between the two types of attachment. Postmes and his colleagues (2006) argue that a convergence of identity-based and bond-based attachment may occur over time as people interact repeatedly. Individuals connected through interpersonal ties may develop attachment to the community. For instance, MySpace members may join to make friends and later become fans of musicians. Shifts from identity-based attachment to bond-based attachment also have been noted. For instance, members of an online chess group reported that by playing chess together they became friends with one other as they talked to each other about common interests (Ginsburg and Weisband 2002).

## Implications for Practice

Our experimental findings have some implications for managers who run online communities and practitioners who design and develop them. In a struggling online community, inducing attachment in a way that doubles the number of visits, as we were able to achieve, could be the difference between success and failure. For a community supported by advertising, doubling the number of visits could double revenue. Considering our finding that identity-based attachment may be comparatively easier to implement, at least in websites with a specific purpose, practitioners may want to launch their community building efforts with features that emphasize groups or community purpose (group categorization, group homogeneity, and detailed information about groups and community). Although participants in the field experiment were randomly assigned to groups with arbitrary wild animal names, they reported significantly greater attachment to their own group than to other groups, and this group assignment increased their visits to the community and the number of posts they read. Studies have shown that group members feel more attached or committed to a self-selected group than an assigned group (Ellemers et al. 1999). In practice, community designers might want to let members self-select into groups rather than to assign them, and use clustering techniques to suggest groups that members could consider joining.

Our results also suggest that implementing algorithms that repeatedly expose members to groups and individuals will be effective but doing so is more challenging at the individual level. Typically, there are orders of magnitude more individuals than groups in an online community. In our field experiment, participants were exposed to 10 movie groups in the identity condition and potentially hundreds of individual members in the bond condition. Even though we developed an algorithm to maximize the chance of a small set of members being repeatedly shown to a target member, repeated exposure to groups turned out to be much more effective than repeated exposure to individuals. One reason may be the frequency at which information was updated on the profile pages. Because information on the group profile page aggregated information from hundreds of group members, it changed whenever any of them rated a movie or posted in the forums. This rate of change was much more frequent than information on an individual profile page, which remained static unless the owner of the profile logged in and used the system or updated his or her profile information. Individual members returning to a profile page may be less likely to visit again if no new information is provided. Thus, featuring individual members on a front page with little information provided and updated on these members' profile pages can result in the failure of the intended repeated exposure.

The results also suggest that when introducing new features, practitioners should attend to the experiences of newcomers and old-timers separately. In the current research, newcomers embraced bond-based features to foster interpersonal relationships while old-timers seemed to resist this strategy. Practitioners need to be sensitive to the reactions of core members when they consider dramatic shifts in the themes or core offerings of a community.

## Concluding Remarks

This research illustrates how social science theories can be applied to develop insights for online community design. Our theory-inspired design approach provides a practical lens through which designers and managers can look at their decisions in a nuanced and systematic manner, rather than using overly general themes of sociality or through trial and error. We believe that theoretical insights supported by empirical evidence are powerful tools that designers and managers could leverage to build vibrant online communities. They will still need to make important choices to customize the design features to fit the technology being used, the class of members, and other particulars that may shape member experience. When it comes to design, there are often no correct answers, only wise tradeoffs among alternatives. However, our theory-inspired approach should help designers and managers constrain and navigate the design space they need to explore. As Greif (1991) stated, “even if the major influence of a theory in artifact design is merely to stimulate creative exploratory activities, we should not undervalue the relevance of theory for the concrete artifact” (p. 214).

## Acknowledgments

This work was supported by National Science Foundation Grant IIS-0325049 (Designing Online Communities to Enhance Participation). The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of NSF. We thank our Community Lab collaborators (listed at http://www.community-lab/), Alok Gupta, Sophie Leroy, Lisa M. Leslie, Carlos Torelli, and the participants of the 2008 Big Ten IS Symposium, Michigan State University Information Technology workshop, and University of Minnesota Information and Decision Sciences Department workshop for their helpful comments. We also thank Sam Hashemi for research assistance and MovieLens users for participating in our study.

## References

Agarwal, R., Gupta, A., and Kraut, R. 2008. “Editorial Overview—The Interplay Between Digital and Social Networks,” Information Systems Research (19:3), pp. 243-252.

Allen, N. J., and Meyer, J. P. 1990. “The Measurement and Antecedents of Affective, Continuance, and Normative Commitment to the Organization,” Journal of Occupational and Organizational Psychology (63), pp. 1-8.

Arguello, J., Butler, B. S., Joyce, L., Kraut, R. E., Ling, K. S., Rosé, C. P., and Wang, X. 2006. “Talk to Me: Foundations for Successful Individual-Group Interactions in Online Communities,” in Proceedings of the 2006 ACM Conference on Human Factors in Computing Systems, New York: ACM Press, pp. 959-968.

Ashforth, B. E., Harrison, S. H., and Corley, K. G. 2008. “Identification in Organizations: An Examination of Four Fundamental Questions,” Journal of Management (34:3), pp. 325-374.

Banerjee, A., and Ghosh, J. 2002. “On Scaling up Balanced Clustering Algorithms,” Paper presented at the Second SIAM International Conference on Data Mining, Arlington, VA.

Baronm R. M., and Kenny, D. A. 1986. "The Moderator–Mediator Variable Distinction in Social Psychological Research: Conceptual, Strategic, and Statistical Considerations," Journal of Personality and Social Psychology (51), pp. 1173-1182.

Baym, N. K. 2007. “The New Shape of Online Community: The Example of Swedish Independent Music Fandom,” First Monday (12:8), August 6 (http://firstmonday.org/issues/issue12\_8/baym/index.html).

Berscheid, E., and Reis, H. T. 1998. “Attraction and Close Relationships,” in The Handbook of Social Psychology, Vol. 2, D. T. Gilbert, S. T. Fiske, and G. Lindzey (eds.), New York: McGraw-Hill, pp. 193-281.

Blanchard, A., and Markus, M. L. 2004. “The Experienced ‘Sense’ of a Virtual Community: Characteristics and Processes,” The Data Base for Advances in Information Systems (35:1), pp. 65-79.

Brewer, M. 1991. “The Social Self: On Being the Same and Different at the Same Time,” Personality and Social Psychology Bulletin (17:5), pp. 475-482.

Butler, B., Sproull, L., Kiesler, S., and Kraut, R. E. 2007. “Community Effort in Online Groups: Who Does the Work and Why?,” in Leadership at a Distance, S. Weisband (ed.), Hillsdale, NJ: Lawrence Erlbaum Associates, pp. 171-194.

Byrne, D. 1997. “An Overview (and Underview) of Research and Theory Within the Attraction Paradigm,” Journal of Social and Personal Relationships (14:3), pp. 417-431.

Choi, B. R., Alexander, K., Kraut, R. E., and Levine, J. M. 2010. "Socialization Tactics in Wikipedia and Their Effects," in Proceedings of the 2010 ACM Conference on Computer-Supported Cooperative Work, New York: ACM Press, pp. 107-116.

Chua, C., Wareham, J., and Robey, D. 2007. “The Role of Online Trading Communities in Managing Internet Auction Fraud,” MIS Quarterly (31:4), pp. 759-781.

Collins, N. L., and Miller, L. C. 1994. “Self-Disclosure and Liking: A Meta-analytic Review,” Psychological Bulletin (116:3), pp. 457-475.

Cooper, W. H. 1981. “Ubiquitous Halo,” Psychological Bulletin (90:2), pp. 218-244.

Dellarocas, C. 2006. “Strategic Manipulation of Internet Opinion Forums: Implications for Consumers and Firms,” Management Science (52:10), pp. 1577-1593.

Drenner, S., Harper, F. M., Frankowski, D., Riedl, J., and Terveen, L. 2006. “Insert Movie Reference Here: A System to Bridge Conversation and Item-Oriented Web Sites,” in Proceedings of the 2006 ACM Conference on Human Factors in Computing Systems, New York: ACM Press, pp. 951-954.

Ducheneaut, N. 2005. “Socialization in an Open Source Software Community: A Socio-Technical Analysis,” Computer Supported Cooperative Work (14:4), pp. 323-368.

Dunham, R. B., Grube, J. A., and Castaneda, M. B. 1994. “Organizational Commitment: The Utility of an Integrative Definition,” Journal of Applied Psychology (79:3), pp. 370-380.

Ellemers, N., Kortekaas, P., Jaap, W., and Ouwerkerk, J. W. 1999. "Self-Categorization, Commitment to the Group and Group

Self-Esteem as Related but Distinct Aspects of Social Identity," European Journal of Social Psychology (29:2-3), pp. 371-389.

Ellemers, N., Spears, R., and Doosje, B. 1997. “Sticking Together or Falling Apart: In-Group Identification as a Psychological Determinant of Group Commitment Versus Individual Mobility,” Journal of Personality and Social Psychology (72:3), pp. 617-626.

El Sawy, O., and Bowles, G. 1997. “Redesigning the Customer Support Process for the Electronic Economy: Insights from Storage Dimensions,” MIS Quarterly (21:4), pp. 457-483

Festinger, L., Schacter, S., and Back, K. 1950. Social Pressures in Informal Groups: A Study of Human Factors in Housing, Palo Alto, CA: Stanford University Press.

Forgas, J. P. 1995. “Mood and Judgment: The Affect Infusion Model (AIM),” Psychological Bulletin (117:1), p 39.

Friedman, F., and Resnick, P. 2001. “The Social Cost of Cheap Pseudonyms,” Journal of Economics and Management Strategy (10:2), pp. 173-199.

Ginsburg, M., and Weisband, S. 2002. “Social Capital and Volunteerism in Virtual Communities: The Case of the Internet Chess Club,” in Proceedings of the 35 $^{th}$ Annual Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press, p. 171b.

Greif, S. 1991. “The Role of German Work Psychology in the Design of Artifacts,” in Designing Interaction: Psychology at the Human–Computer Interface (Vol. 11), J. M. Carroll (ed.), Cambridge, UK: Cambridge University Press, pp. 203-226.

Gu, B., Konana, P., Rajagopalan, B., and Chen, H. W. M. 2007. "Competition Among Virtual Communities and User Valuation: The Case of Investing-Related Communities," Information Systems Research (18:1), pp. 68-85.

Harper, F. M., Li, X., Chen, Y., and Konstan, J. A. 2005. “An Economic Model of User Rating in an Online Recommender System,” in Proceedings of the 10 $^{th}$ International Conference on User Modeling, Edinburgh, UK, July 24-30, pp. 307-316.

Harper, F. M., Sen, S., and Frankowski, D. 2007. “Supporting Social Recommendations with Activity-Balanced Clustering,” in Proceedings of the 2007 ACM Conference on Recommender Systems, New York: ACM Press, pp. 165-168.

Hill, K., and Hughes, J. 1998. Cyberpolitics: Citizen Activism in the Age of the Internet, Lanham, MD: Rowman & Littlefield Publishers, Inc.

Hogg, M. A. 1992. The Social Psychology of Group Cohesiveness: From Attraction to Social Identity, London: Harvester Wheatsheaf.

Hogg, M. A. 2001. “Social Categorization, Depersonalization, and Group Behavior,” in Blackwell Handbook of Social Psychology: Group Processes, M. A. Hogg and S. Tindale (eds.), Oxford, UK: Blackwell, pp. 56-85.

Hogg, M. A., and Turner, J. C. 1985. “Interpersonal Attraction, Social Identification and Psychological Group Formation,” European Journal of Social Psychology (15:1), pp. 51-66.

Isen, A. M., and Levin, P. F. 1972. “Effect of Feeling Good on Helping: Cookies and Kindness,” Journal of Personality and Social Psychology (21:3), pp. 384-388.

Karasawa, M. 1991. “Toward an Assessment of Social Identity: The Structure of Group Identification and Its Effects on In-Group Evaluations,” British Journal of Social Psychology (30:4), pp. 293-307.

Kim, A. J. 2000. Community Building on the Web: Secret Strategies for Successful Online Communities, Berkeley, CA: Peachpit Press.

Kittur, A., Chi, E., Pendleton, B. A., Suh, B., and Mytkowicz, T. 2007. “Power of the Few vs. Wisdom of the Crowd: Wikipedia and the Rise of the Bourgeoisie,” in Proceedings of the 2007 ACM Conference on Human Factors in Computing Systems, New York: ACM Press, pp. 165-168

Kollock, P. 1998. “Design Principles for Online Communities,” PC Update (15:5), pp. 58-60.

Krogh, G. V., Spaeth, S., and Lakhani., K. R. 2003. “Community, Joining, and Specialization in Open Source Software Innovation: A Case Study,” Research Policy (32:7), pp. 1217-1241.

Lee, Y., and Ottati, V. 1995. “Perceived In-Group Homogeneity as a Function of Group Membership Salience and Stereotype Threat,” Personality and Social Psychology Bulletin (21:6), pp. 612-621.

Leidner, D. E., Koch, H., and Gonzalez, E. 2010. “Assimilating Generation Y IT New Hires into USAA’s Workforce: The Role of an Enterprise 2.0 System.” MIS Quarterly Executive (9:4), pp. 229-242.

Ling, K., Beenen, G., Ludford, P. J., Wang, X., Chang, K., Li, X., Cosley, D., Frankowski, D., Terveen, L., Rashid, A. M., Resnick, P., and Kraut, R. 2005. “Using Social Psychology to Motivate Contributions to Online Communities,” Journal of Computer Mediated Communication (10:4), Article 10.

MacQueen, J. B. 1967. “Some Methods for Classification and Analysis of Multivariate Observations,” in Proceedings of the 5 $^{th}$ Berkeley Symposium on Mathematical Statistics and Probability, Berkeley, CA: University of California Press, pp. 281-297.

Maloney-Krichmar, D., and Preece, J. 2005. “A Multilevel Analysis of Sociability, Usability, and Community Dynamics in an Online Health Community,” ACM Transactions on Computer-Human Interaction (12:2), pp. 201-232.

McKenna, K. Y. A., Green, A. S., and Gleason, M. E. J. 2002. "Relationship Formation on the Internet: What's the Big Attraction?" Journal of Social Issues (58:1), pp. 9-31.

McMillan D. W., and Chavis, D. M. 1986. “Sense of Community: A Definition and Theory,” Journal of Community Psychology (14), pp. 6-23.

Meyer, J., Stanley, D., Herscovitch, L., and Topolnytsky, L. 2002. "Affective, Continuance, and Normative Commitment to the Organization: A Meta-Analysis of Antecedents, Correlates, and Consequences," Journal of Vocational Behavior (61:1), pp. 20-52.

Milgram, S. 1977. “The Familiar Stranger: An Aspect of Urban Anonymity,” in The Individual in a Social World: Essays and Experiments, S. Milgram (ed.), Reading, MA: Addison-Wesley, pp. 51-53.

Mockus, A., Fielding, R. T., and Herbsleb, J. D. 2002. "Two Case Studies of Open Source Software Development: Apache and

Mozilla," ACM Transactions on Software Engineering and Methodology (11:3), pp. 309-346.

Newcomb, T. 1961. The Acquaintance Process, New York: Holt, Rinehart, and Winston.

Ogawa, S., and Piller, F. 2006. “Reducing the Risks of New Product Development,” MIT Sloan Management Review (47:2), pp. 65-72.

Oh, W., and Jeon, S. 2007. “Membership Herding and Network Stability in the Open Source Community: The Ising Perspective,” Management Science (53:7), pp. 1086-1101.

Omoto, A. M., and Snyder, M. 2002. “Considerations of Community: The Context and Process of Volunteerism,” American Behavioral Scientist (45:5), pp. 846-867.

Phang, C. W., Kankanhalli, A., and Sabherwal, R. 2009. “Usability and Sociability in Electronic Communities: A Comparative Study of Knowledge Seekers and Contributors,” Journal of the Association for Information Systems (10:10), pp. 721-747.

Pickett, C., and Brewer, M. 2001. “Assimilation and Differentiation Needs as Motivational Determinants of Perceived In-Group and Out-Group Homogeneity,” Journal of Experimental Social Psychology (37:4), pp. 341-348.

Postmes, T., Baray, G., Haslam, S. A., Morton, T. A., and Swaab, R. I. 2006. “The Dynamics of Personal and Social Identity Formation,” in Individuality and the Group: Advances in Social Identity, T. Postmes and J. Jetten. (eds.), Thousand Oaks, CA: Sage Publications, pp. 215-236.

Postmes, T., and Spears, R. 2000. “Refining the Cognitive Redefinition of the Group: De-Individuation Effects in Common Bond vs. Common Identity Groups,” in Side Effects Centre Stage: Recent Developments in Studies of De-Individuation in Groups, T. Postmes, R. Spears, M. Lea, and S. Reicher (eds.), Amsterdam: KNAW, pp. 63-78.

Postmes, T., Spears, R., and Lea, M. 2002. “Intergroup Differentiation in Computer-Mediated Communication: Effects of Depersonalization,” Group Dynamics: Theory Research and Practice (6:1), pp. 3-16.

Postmes, T., Tanis, M., and Boudewijn, D. 2001. “Communication and Commitment in Organizations: A Social Identity Approach,” Group Processes & Intergroup Relations (4:3), pp. 227-246.

Preece, J. 2000. Online Communities: Designing Usability, Supporting Sociability, Chichester, England: Wiley.

Preece, J., Nonnecke, B., and Andrews, D. 2004. “The Top 5 Reasons for Lurking: Improving Community Experiences for Everyone,” Computers in Human Behavior (20:2), pp. 201-223.

Prentice, D. A., Miller, D. T., and Lightdale, J. R. 1994. “Asymmetries in Attachments to Groups and to Their Members: Distinguishing Between Common-Identity and Common-Bond Groups,” Personality and Social Psychology Bulletin (20:5), pp. 484-493.

Ren, Y., Kraut, R. E., and Kiesler, S. 2007. “Applying Common Identity and Bond Theory to Design of Online Communities,” Organization Studies (28:3), pp. 377-408.

Ridings, C. M., and Gefen, D. 2004. "Virtual Community Attraction: Why People Hang Out Online," Journal of Computer Mediated Communication (10:1), Article 4.

Riketta, M., and Dick, R. 2005. “Foci of Attachment in Organizations: A Meta-Analytic Comparison of the Strength and Correlates of Workgroup Versus Organizational Identification and Commitment,” Journal of Vocational Behavior (67:3), pp. 490-510.

Rodgers, S., and Chen, Q. 2005. “Internet Community Group Participation: Psychosocial Benefits for Women with Breast Cancer,” Journal of Computer Mediated Communication (10:4), Article 5.

Sarwar, B., Karypis, G., Konstan, J., and Riedl, J. 2001. “Item-Based Collaborative Filtering Recommendation Algorithms,” in Proceedings of the $10^{th}$ International Conference on the World Wide Web, Hong Kong, May 1-5, pp. 285-295.

Sassenberg, K. 2002. “Common Bond and Common Identity Groups on the Internet: Attachment and Normative Behavior in On-Topic and Off-Topic Chats,” Group Dynamics (6:1), pp. 27-37.

Sassenberg, K., and Postmes, T. 2002. “Cognitive and Strategic Processes in Small Groups: Effects of Anonymity of the Self and Anonymity of the Group on Social Influence,” British Journal of Social Psychology (41:3), pp. 463-480.

Sen, S., Lam, S. K., Rashid, A. M., Cosley, D., Frankowski, D., Osterhouse, J., Harper, F. M., and Riedl, J. 2006. “Tagging, Communities, Vocabulary, Evolution,” in Proceedings of the 20 $^{th}$ ACM Conference on Computer-Supported Cooperative Work, Banff, Alberta, Canada, November 4-8, pp. 181-190.

Shen, K. N., and Khalifa, M. 2009. “Design for Social Presence in Online Communities: A Multidimensional Approach,” AIS Transactions on Human-Computer Interaction (1:2), pp. 33-54.

Sherif, M., Harvey, L. J., White, B. J., Hood, W. R., and Sherif, C. W. 1961. Intergroup Conflict and Cooperation: The Robbers Cave Experiment, Middletown, CT: Wesleyan University Press.

Shklovski, I., Burke, M., Kiesler, S., and Kraut, R. 2010. “Technology Adoption and Use in the Aftermath of Hurricane Katrina in New Orleans,” American Behavioral Science (53:8), pp. 1228-1246.

Simon, B., and Pettigrew, T. 1990. “Social Identity and Perceived Group Homogeneity: Evidence for the In-group Homogeneity Effect,” European Journal of Social Psychology (20:4), pp. 269-286.

Smith, C. B., McLaughlin, M. L., and Osborne, K. K. 1997. "Conduct Control on Usenet," Journal of Computer Mediated Communication (2:4) (http://jcmc.indiana.edu/vol2/issue4/smith.html).

Stewart, K. J., and Gosain, S. 2006. “The Impact of Ideology on Effectiveness in Open Source Software Development Teams,” MIS Quarterly (30:2), pp. 291-314.

Suls, J., Martin, R., and Wheeler, L. 2002. “Social Comparison: Why, With Whom, and With What Effect?,” Current Directions in Psychological Science (11:5), pp. 159-163.

Tajfel, H., Billig, M. G., Bundy, R. P., and Flament, C. 1971. "Social Categorization and Intergroup Behaviour," European Journal of Social Psychology (1:2), pp. 149-178.

Tajfel, H., and Turner, J. C. 1986. “The Social Identity Theory of Inter-group Behavior,” in Psychology of Intergroup Relations,

S. Worchel and L. W. Austin (eds.), Chicago: Nelson-Hall, pp. 7-24.

Turner, J. C. 1985. “Social Categorization and the Self-Concept: A Social Cognitive Theory of Group Behavior,” in Advances in Group Processes: Theory and Research, Vol. 2, E. J. Lawler (ed.), Greenwich, CT: JAI Press, pp. 77-122.

Turner, J. C., Hogg, M. A., Oakes, P. J., Reicher, S. D., and Wetherell, M. S. 1987. Rediscovering the Social Group: A Self-Categorization Theory, Oxford, UK: Blackwell.

Utz, S. 2003. “Social Identification and Interpersonal Attraction in MUDs,” Swiss Journal of Psychology (62:2), pp. 91-101.

Vandenberghe, C., Bentein, K., and Stinglhamber, F. 2004. "Affective Commitment to the Organization, Supervisor, and Work Group: Antecedents and Outcomes," Journal of Vocational Behavior (64:1) pp. 47-71.

Verona, G., Prandelli, E., and Sawhney, M. 2006. “Innovation and Virtual Environments: Towards Virtual Knowledge Brokers,” Organization Studies (27:6), pp. 765-788.

Wasko, M. M., and Faraj, S. 2005. “Why Should I Share? Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice,” MIS Quarterly (29:1), pp. 35-57.

Wellman, B. 2001. “Computer Networks as Social Networks,” Science (293:14), pp. 2031-2034.

Wood, J. 1989. “Theory and Research Concerning Social Comparisons of Personal Attributes,” Psychological bulletin (106:2), pp. 231-248.

Worchel, S., Rothgerber, H., Day, E. A., Hart, D., and Butemeyer, J. 1998. “Social Identity and Individual Productivity Within Groups,” British Journal of Social Psychology (37:4), pp. 389-413.

Worthen, B. 2008. “Why Most Online Communities Fail,” Wall Street Journal, July 16.

Zajonc, R. B. 1968. “Attitudinal Effects of Mere Exposure,” Journal of Personality and Social Psychology (9:1), pp. 1-27.

## About the Authors

Yuqing Ren is an assistant professor of Information and Decision Sciences at the Carlson School of Management at the University of Minnesota. She holds a Ph.D. from Carnegie Mellon University. Her areas of interest include online community design, distributed collaboration, knowledge management, and computational modeling of social and organizational systems. Her work has been published in Academy of Management Annals, Journal of MIS, Management Science, Organization Science, Organization Studies, and the proceedings of conferences including Academy of Management, Computer-Supported Cooperative Work, Hawaii International Conference on System Sciences, International Conference on Information Systems, and SIGCHI. She currently serves on the editorial board of Organization Science.

F. Maxwell Harper is a Ph.D. student in the Department of Computer Science and Engineering at the University of Minnesota, and a software developer at Code 42 Software. He is conducting research to understand the effects of policies, designs, and personalization algorithms on member participation in online communities. He received an M.S. from the University of Minnesota in 2006, and a B.A. from Carleton College in 1998.

Sara Drenner received an M.S. from the Department of Computer Science and Engineering at the University of Minnesota in 2008. While at Minnesota, she conducted research involving the incorporation of newcomers into online communities and recommender systems. She is currently working for BI Worldwide as a technical lead for their Learning and Organizational Effectiveness division, involved in creating learning management systems and e-learning platforms.

Loren Terveen is a professor of Computer Science and Engineering at the University of Minnesota. His research interest spans a variety of topics in human-computer interaction and social computing, including creating more effective online participation and bringing local and online communities together. He helped develop one of the early recommender web sites (PHOAKS), was a coleader of the CommunityLab project, and is a cofounder of the Cyclopath project. Loren received his Ph.D. in 1991 from the University of Texas at Austin. He has served the human-computer interaction community in various leadership roles, including cochair of the Conference on Human Factors in Computing Systems and the Conference on Intelligent User Interfaces and program chair of the Conference on Computer-Supported Cooperative Work.

John Riedl is a professor of Computer Science at the University of Minnesota where he has been a faculty member since 1990. In 1992, John cofounded the GroupLens project on collaborative information filtering, and has been codirecting it since. GroupLens seeks to develop an understanding of the social web by developing principles that guide the development of effective large-scale collaboration tools. Recently, GroupLens Research has been exploring ways in which recommender systems can be used to study and enhance social structures on the Web. John received his Bachelor degree in mathematics from the University of Notre Dame in 1983, his Master's degree in computer science in 1985, and his Ph.D. in computer science in 1990 from Purdue University.

Sara Kiesler is Hillman Professor of Computer Science and Human-Computer Interaction at the Human-Computer Interaction Institute, Carnegie Mellon University. Sara has conducted many studies on the social and organizational aspects of computer-based and new communication technologies reported in a series of books: Connections: New Ways of Working in the Networked Organization (1991, with L. Sproull), Culture of the Internet (1997), and Distributed Work (2002, with P. Hinds). Her recent projects are in the areas of collaboration in hospital work, scientific projects, disasters, human-robot interaction, and online groups.

Robert Kraut is Herbert A. Simon Professor of Human–Computer Interaction at Carnegie Mellon University. He received his Ph.D. in Social Psychology from Yale University in 1973, and has previously taught at the University of Pennsylvania and Cornell University. He was a research scientist at AT&T Bell Laboratories and Bell Communications Research for 12 years. Robert has broad interests in the design and social impact of computing and conducts research on everyday use of the Internet, technology and conversation, collaboration in small work groups, computing in organizations, and contributions to online communities. His most recent work examines factors influencing the success of online communities and ways to apply psychology theory to their design.
