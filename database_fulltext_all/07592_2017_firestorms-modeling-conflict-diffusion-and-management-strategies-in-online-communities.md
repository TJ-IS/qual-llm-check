---
otero_id: 7592
otero_key: "J59YZTSA"
title: "Firestorms: Modeling conflict diffusion and management strategies in online communities"
authors: "Florian Hauser; Julia Hautz; Katja Hutter; Johann Füller"
year: "2017"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2017.01.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Firestorms: Modeling conflict diffusion and management strategies in online communities

Florian Hauser <sup>a</sup>, Julia Hautz <sup>b,</sup>⇑, Katja Hutter <sup>c</sup>, Johann Füller <sup>d,e</sup>

<sup>a</sup> Innsbruck University School of Management, Department of Banking and Finance, Universitaetsstr. 15, 6020 Innsbruck, Austria <sup>b</sup> Innsbruck University School of Management, Department of Strategic Management, Marketing and Tourism, Universitaetsstr. 15, 6020 Innsbruck, Austria <sup>c</sup> Salzburg University – Department of Marketing and Innovation, Residenzplatz 9, 5020 Salzburg, Austria

<sup>d</sup> Innsbruck University School of Management, Chair of Innovation and Entrepreneurship, Department of Strategic Management, Marketing and Tourism, Universitaetsstr. 15, 6020 Innsbruck, Austria

<sup>e</sup> Hyve Ag, Munich, Schellingstr. 45, 80799 Munich, Germany

## a r t i c l e i n f o

Article history: Received 19 August 2015 Received in revised form 20 December 2016 Accepted 26 January 2017 Available online xxxx

Keywords: Online communities Social conflict Conflict management Agent-based simulation

## a b s t r a c t

This study aims to provide a better understanding of how organizations can manage public conflict and firestorms in social media spheres. We develop an agent-based simulation model of conflicts in firm-hosted online communities and find that a collaborating conflict management style characterized by high levels of cooperativeness and assertiveness helps to successfully handle conflict. However, the effectiveness of this collaborative style is highly dependent on contingency factors related to the participating individuals and the social structure within the community itself, such as the number of moderators and aggressors present in the community, their credibility, as well as the overall opinion of the community. Depending on these factors, collaborating and accommodating conflict management becomes more or less successful. Under some configurations it is even less effective than more competitive and assertive management styles. Therefore, to successfully handle conflict and restrain the escalation of a firestorm, organizations need to optimally adapt their conflict management style to varying conditions by considering individual-level and community-level characteristics.

 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Online communities provide promising new ways of value creation for organizations (Susarla et al., 2012) through leveraging the knowledge and creativity of a crowd of interacting individuals (Berthon et al., 2008; Butler, 2001; Di Gangi and Wasko, 2009; Wellman et al., 1996). In the case of firm-hosted communities organizations set up, host, and manage community platforms and invite community members – often in the form of a contest – to provide specific contributions (Füller et al., 2014; Hutter et al., 2011) such as e.g. product ideas and technical solutions (Boudreau and Lakhani, 2009; Füller, 2010) or insights and content for marketing and customer relationship management (Bernoff and Li, 2008; Hautz et al., 2014; Kozinets, 1999).

But despite new ways of benefiting from online communities, open, direct communication and interactivity also bear the risk of unprecedented levels of negative word-of-mouth (WoM) and the emergence of social conflict (Montoya-Weiss et al.,

2001; Qi et al., 2014; Tybout and Roehm, 2009; Ward and Ostrom, 2006). Social conflict is an interaction relationship that may occur when community participants perceive incompatibilities (Kriesberg, 1973, 2007; Mack and Snyder, 1957; Putman and Poole, 1987; Wall and Callister, 1995). Divergences in goals, resource allocation aspirations, social norms, and values may lead to unmet expectations, perceived dissatisfaction, or violations of fairness. This perceptions of one-sided or even parasitic relationships between firms and communities (Dahlander and Magnusson, 2005) may result in interactive conflict behaviors ranging from adjustment of opinions, polarization of views, negative WoM, antagonism, deviant behavior, public protest, or active resistance of hitherto peaceful community members (Franke et al., 2012; Funke, 2012; Gebauer et al., 2012). Ultimately, this may lead to publically discussed debacles and ‘firestorms’ - rapid discharges of large quantities of negative, often highly emotional posts in the social media environment (Pfeffer et al., 2014; Stich et al., 2014). For example, the notebook brand Moleskine caused a firestorm when asking designers to participate in their online community. The request to submit ‘free’ design work created outrage among freelancers, who felt their basis of existence threatened and subsequently expressed their disagreement with the incentive scheme in more than 500 comments on the Facebook page (Moleskine, 2011).

If not effectively managed such conflict in firm-hosted communities and resulting firestorms can be detrimental to organizations and their brands. While people have always tended to vocalize criticism and complaints about a company, a brand, its products, practices, or actions when they felt affected or unfairly treated, social technologies have exponentiated the speed, range, and scale of diffusion, as well as the detrimental consequences for the firm (Pfeffer et al., 2014; Qi et al., 2014). With this study, we aim to contribute to a better understanding of successfully managing conflict and avoiding potential firestorms in firm-hosted online communities. More specifically, we explore which characteristics influence the diffusion of conflict and how it may be curtailed or even avoided through active conflict management styles.

We apply an agent-based computer simulation (ABS) to analyze information diffusion and opinion adoption triggered by negative conflict messages. So far, research on how organizations can effectively manage negative messages and public conflict in the social media sphere has been mostly limited to qualitative research or analytic modeling (Goh et al., 2013; Qi et al., 2014). However, online communities represent complex social systems (Ren and Kraut, 2014) that require more flexible simulation approaches to better understand the dynamics of conflict diffusion, conflict management, and the avoidance of firestorms. Qualitative case studies can suffer from the overwhelming complexity of social systems, time pressure, and limitations in information and data availability (Lazer and Friedman, 2007). Analytic modeling<sup>1</sup> is constrained in terms of handling combinatorics and dynamics when analyzing complex social systems such as online communities (Lazer and Friedman, 2007). This especially applies to firestorms, where a combination of community members’ behavior results in an emergent dynamic change of opinions over time. Therefore, we follow calls of prior research (Qi et al., 2014) and explore conflict management in online communities via ABS. Although ABS requires simplifying assumptions when specifying the model, it is a powerful tool for studying and understanding complex, non-linear social systems such as an online community by simulating the actions and interactions of autonomous individuals (Ren and Kraut, 2014). It allows us to isolate and study the effectiveness of different conflict management styles while manipulating specific factors identified as relevant by theory on information diffusion and opinion adoption, such as the number of people in the social environment adopting a certain opinion, the strength of one’s opinion, and the credibility of individuals.

In our model, the firm-hosted online community consists of agents with heterogeneous opinions that are subject to change over time due to interaction and may be the source of conflict once they become rather negative. This process depends on agents’ credibility, cooperativeness, and assertiveness. We model and analyze the impact of specific conflict management strategies applied by a moderator on the overall opinion valence in the community. We find that the effectiveness of a collaborative conflict management style characterized by high levels of cooperativeness and assertiveness is highly dependent on contingency factors such as the number of moderators and aggressors, the credibility of aggressors and moderators, and the overall opinion of the community. In some configurations, such as those with low aggressor credibility or a strong positive overall opinion of the community, a competitive, assertive style becomes more effective. Therefore, to successfully handle conflict and restrain the escalation of a firestorm, organizations need to consider the actual state of the community in form of individual-level and community-level characteristics and accordingly adjust their conflict management style.

The first section of this paper provides the theoretical background. Based on multiple presented theories, we develop an agent-based simulation model that simulates conflict diffusion and shows strategies for successful conflict management. We present the illustrative results of our model and discuss their implications. Overall, our study provides insight for researchers and managers on the social dynamics of conflict and escalation in online communities, as well as the prerequisites that have to be met to successfully apply conflict management strategies.

## 2. Theoretical background

In this study we synthesize multiple theoretical streams to develop our agent-based model. We first discuss literature on online communities to get insights into different types of communities, their set-up, and their members. In addition, we draw on social conflict theory to understand why and how individuals engage in interactive conflict behavior such as negative opinion adoption, negative WoM, and active resistance in online communities. We further discuss information diffusion and opinion adoption theory to explore how negative opinions diffuse and are adopted among participants of online communities. Crisis communication and conflict management literature finally provide insights into how companies can try to manage such conflict behavior and avoid diffusion.

Based on the insights from the literature streams summarized in Table 1, we build our model and distil the relevant factors. By integrating insights from these multiple theories, our model depicts a more holistic picture of how moderators in firm-hosted online communities can react to, influence, and avoid the diffusion and adoption of negative, conflict-related opinions within online communities.

## 2.1. Online communities

Social technologies are a multiplier of communication links (Dal Fiore, 2007) leading to an enormous growth of ‘‘cultural aggregations” in the form of online communities (Preece, 2002; Rheingold, 1994; Wasko and Faraj, 2005). Through the facilitation of asynchronous, direct, interactive, low-cost communication, participating individuals are able to share information and content (Berthon et al., 2008) and to form interpersonal relationships that provide knowledge, social interaction, and support, independent of geographical proximity or time (Butler, 2001; Di Gangi and Wasko, 2009). Online communities represent complex socio-technical systems (De Moor and Wagenvoort, 2004; Lazar and Preece, 2002). Usually they consist of a small core of very active members, while the majority of members only rarely participates actively (Nonnecke and Preece, 2000, 2001).<sup>2</sup>

Corporations are increasingly leveraging bidirectional exchange relationships with online communities outside of organizational boundaries. Thereby firms can play various roles depending on the type of online community. Porter (2004) distinguishes between member-initiated and firm-sponsored communities. Member-initiated communities are established and maintained by individuals who share a common interest and come together to discuss and share information and content about self-relevant issues (Porter et al., 2013). In member-initiated communities, firms have no direct control over contributed content related to their products, services, or brand, but can passively observe and collect information or engage in peer-to-peer relationships as ordinary community members. In firm-sponsored communities, in contrast, organizations initiate, sponsor, and/or host communities through creating and managing community platforms (Miller et al., 2009; Porter, 2004) and ask for specific input and content related to their brand, products, or services (e.g. experiences, reviews, technical support, ideas, designs, problem solutions, videos, ads, etc.). While member-initiated communities focus on the relationships among members, firm-sponsored communities encourage relationships between members and the sponsoring organizations as well as their products and brands.

Firm-hosted communities can be leveraged by organizations for value creation for various purposes: knowledge and content sharing (Butler and Wang, 2012; Wasko and Faraj, 2005), strengthening customer loyalty, generating positive WoM and influencing consumer decision-making (Brown et al., 2007: Füller et al., 2010: Ind et al., 2013) or innovation activities such as the generation of technological solutions or ideas for new products and designs (Di Gangi and Wasko, 2009; Füller et al., 2010; Terwiesch and Xu, 2008).

Depending on their purpose, these firm-hosted communities might differ in their range and openness and in the level of member engagement. The New York Police Department and McDonald’s, for example, publicly asked consumers to share positive experiences and stories with their product and services on Twitter (Pfeffer et al., 2014). Both calls backfired nega tively. #myNYPD created more than 70,000 tweets sharing stories and pictures of police brutality and set the NYPD’s rep utation on fire.<sup>3</sup> Also #McDStories was used to express horror stories and past problems. These viral PR campaigns were entirely open to the public. Contribution effort and member involvement were limited by the chosen media platform, short Tweets. In contrast, firms may also ask community members to provide very specific, more elaborate content, requiring deeper, and active engagement, such as the provision of technological solutions or designs. Lego, for example, hosts the LegoIdeas community,<sup>4</sup> where participants can submit and vote for innovative Lego designs from which the best will be commercialized. Also, the Fiat 500 launch was centered on the ‘‘Fiat 500 Wants You” community platform, where Fiat asked members not only for ideas on car designs but also on jingles, ads, celebrity endorsers, and websites (Cucco and Dalli, 2008). These type of firmhosted communities often take the form of contests, which are not completely open to public but require members to register and agree to terms of participation. Companies broadcast invitations to submit contributions to a specific task and offer different types of incentives for participation. While participants compete with their contributions for the offered prizes, they interact and discuss, share experiences, exchange information and knowledge, build relationships and social structures, and establish a sense of community. This phenomenon of coexisting competitive and collaborative behaviors forms hybrid structures, which are referred to as contest communities (Füller et al., 2014; Hutter et al., 2011).

As firm-hosted communities are created, managed, and controlled by organizations, firm-representatives, community moderators, more or less actively engage in moderation activities to ensure community governance and compliance with community norms, guidelines, and a code of conduct (Preece, 2000). The more intensely and actively community members engage, the more they build relationships and expectations with the hosting organization, its brand, or products, and the more they are emotionally attached (Bagozzi and Dholakia, 2002; Fournier, 1998). These close relationships bear the potential of social conflict and resulting conflict interaction behavior (Montova-Weiss et al. 2001: Tybout and Roehm. 2009: Ward and Ostrom, 2006). Therefore, to benefit from firm-hosted communities, firms must carefully engage, manage, protect, and nurture the community member/organization relationship to minimize and manage such problems (Di Gangi et al., 2010).

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

Table 1  
Overview of literature streams

<table><tr><td>Theory</td><td>Insights on</td><td>References</td></tr><tr><td>Online community literature</td><td>Types of online communities and their characteristics</td><td>E.g. Butler, 2001; Di Gangi and Wasko, 2009; Di Gangi et al., 2010; Füller et al., 2014; Lazar and Preece, 2002; Nonnecke and Preece, 2000, 2001; Porter, 2004; Porter et al., 2013; Preece, 2000; Wasko and Faraj, 2005</td></tr><tr><td>Social conflict theory</td><td>Why and how individuals engage in conflict</td><td>E.g. Aubert, 1963; Husemann et al., 2015; Hirschman, 1994; Kriesberg, 2007; Mack and Snyder, 1957</td></tr><tr><td>Information diffusion theory</td><td>How information - i.e. conflict related messages - diffuses within social structures</td><td>E.g. Banerjee, 1992, 1993; Bikhchandani et al., 1998; Chen et al., 2011; Garg et al., 2011; Granovetter, 1978; Goldenberg and Muller, 2001; He et al., 2012; Guille et al., 2013; Moe and Schweidel, 2012; Stich et al., 2014; Yang and Leskovec, 2010</td></tr><tr><td>Opinion adoption theory</td><td>Which factors influence opinion adoption - i.e. conflict related negative opinion - of individuals</td><td>E.g. Ahluwalia, 2000; Iyengar et al., 2011; Kaiser et al., 2011, 2013; Katz and Lazarsfeld, 1955; Lu et al., 2013; Liu et al., 2007; Lyons and Henderson, 2005; Otterbacher, 2009; Stephen et al., 2012; Watts and Dodds, 2007</td></tr><tr><td>Crisis communication and conflict management literature</td><td>How to successfully handle situations which have the potential to hurt organizations and generate negative outcomes</td><td>E.g. Chang et al., 2015; Coombs, 2011, 1998; Ishi, 2010; Jin and Liu, 2010; Jin et al., 2014; Kaiser et al., 2011; Lee et al., 2015; Lee and Song, 2010; Qi et al., 2014; Pruitt, 1983; Rahim, 2002; Thomas, 1976; Thomas et al., 2012; Xia, 2013</td></tr></table>

## 2.2. Social conflict in firm-hosted communities

Social conflict is commonly conceptualized as an interaction relationship between two or more parties that pursue mutually exclusive or incompatible goals concerning the allocation of scarce resources or differ in social norms, values, or attitudes (Husemann et al., 2015; Kriesberg, 2007; Mack and Snyder, 1957). Sociological literature on social conflict theory has identified three factors as essential in determining a relationship as conflictual, including conflict parties, a conflict object, and interactive conflict behavior (Aubert, 1963; Hirschman, 1994; Williams, 1970). Conflict objects, such as incompatible resource allocations, values, and attitudes are usually based on the underlying goals of conflict parties. In firm-hosted communities, advantageous win-win situations for firms and participants are expected, but perceptions of commensalistic relationships where firms generate value but no benefits accrue for communities and their participants, or even parasitic relationships where firms benefit but communities might be harmed, can emerge (Dahlander and Magnusson, 2005). A dissatisfactory participation experience or disappointing experience with the firm, its products or services, disagreement with a firm’s decisions, a general negative attitude towards the company or company representative(s), or perceived injustice concerning the process and outcomes of participation and its rewards may lead to conflictual relationships between a hosting firm and community members. This may result in interactive conflict behavior, ranging from the adjustment of opinions, a polarization of views, tensions, loss of trust, and negative emotions, up to active coercion and persuasion of others, outrage, active resistance attacks, and violence (Franke et al., 2012: Funke. 2012: Gebauer et al., 2012), Research has found that, for example, individuals who feel unfairly treated and are emotionally affected by companies may look for revenge and retaliation (Blodgett et al., 1993; Grégoire and Fisher, 2008). They may engage in negative WoM and also try to encourage others to participate in negative collective actions to insult the blameworthy company (Gamson, 1992; Snow and Benford, 1992).

However, in the social media sphere, negative interactive conflict behavior is very difficult to control and eventually leads to publically discussed disasters that are referred to as ‘firestorms’ (Pfeffer et al., 2014; Stich et al., 2014). Interactive conflict behavior has changed from a previously private to a more public phenomenon. While customers formerly spread their unfa: vorable opinion to five close people on average (Blodgett et al., 1993) nowadays dissatisfaction is easily voiced to the public. Social technologies have thereby exponentiated the speed, range, and scale of opinion diffusion (Pfeffer et al., 2014) which makes the effects of negative opinions and WoM much more severe in online environments (Henning-Thurau et al., 2004) The way consumers organize and express themselves in the social media sphere may also be more powerful (Dalli and Corciolani, 2008; Deighton and Kornfeld, 2010). Disappointed and angry individuals may spread their negative opinions in harmful posts and evaluations, but also in the form of creative drawings, logos, songs, or videos. This was exactly the case when the guitar of the singer-songwriter Dave Carrol was damaged on a United Airlines flight. While nine months of calls and emails to award compensation finally failed, Carroll composed the song ‘‘United Breaks Guitars,” decrying bad customer service and generating a viral buzz: shortly the song received more than 4 million hits on YouTube. The video and its story also spread attention in off-line media and damaged United’s brand severely (The Economist, 2009). Negative WoM thus may result in detrimental effects on brand evaluation and choice, purchase behavior, and brand loyalty, leading to customer losses and ultimately severe financial losses (Pfeffer et al., 2014; van Noort and Willemsen, 2012). There are multiple examples in which a conflict between the hosting firm and community members emerged, resulting in interactive conflict behavior and, in some cases, public firestorms - also due to ineffective and inappropriate conflict management.

The notebook brand Moleskine was not successful in handling a conflict that emerged on its community platform inviting designers, its core customers, to submit a new blog logo. ‘‘Asking their community to submit ‘free’ work – which as any freelancer will tell you is their means of existence – is such an immense faux pas that it has shown more about how little the company understands who their customers are and what they want” (Salt, 2011, p. 1). Hundreds of community members stressed their frustration in negative comments. Some used their design skills and submitted deformed Moleskine logos. The backlash continued on Moleskine’s official site, Facebook fan page, and Twitter, and thousands of customers openly declared their intent to boycott Moleskine (Moleskine, 2011). As seen by this example online firestorms are predominantly opinion-based and not fact-based, thus being highly affective in nature (Pfeffer et al., 2014).

The online community hosted by Pril, a well-known dishwashing detergent owned by Henkel in Germany, provides evidence of community participants who started to protest against the brand, finally resulting in a severe online firestorm (Breithut, 2011). Henkel launched a web platform asking for logo designs for detergent bottles. The design ‘‘Chicken flavored Pril,” which was mostly favored by other participants was not approved by the firm. Henkel finally chose a winning design with low community ratings. Participants felt overruled and engaged in active resistance, voicing and sharing their dissatisfaction on the Pril Facebook Page (Pril, 2011) and across the web. Henkel had to face a long-lasting PR debacle, including reports outside the community in German television and online newspapers like spiegel.de (Breithut, 2011), zeit.de (Sawall, 2011), and focus.de (Frickel, 2011).

An example of conflict management that successfully avoided the escalation of a firestorm is SPAR, one of Austria’s leading retail chains, who set up a community platform and invited participants to submit new shopping-bag designs (Gebauer et al., 2012; Hutter et al., 2014). More than 2000 participants registered and submitted more than 5000 contributions. A jury selected the winning design, which received €2000 and was intended to be produced in a run of one million bags. Conflict, negative interactive behavior, and resistance emerged, as a minority of participants did not agree with the jury’s decision The contest community was promoted as design-focused, but the winning bag relied on wordplay and was without graphical designs. Participants could not understand how the jury decision and felt a lack of respect for the work of other participants: ‘‘Is SPAR serious about choosing those TOP 3 Designs?!?!? This is a joke. I am very disappointed in the jury selection: There were plenty of good designs to choose from and the fact that the jury selection chose THOSE 3 is very disappointing, humiliating, & discouraging to the design profession. I am utterly shocked by SPAR’s decision!” Immediate, transparent and appropriate conflict management – as outlined in detail in the result section – applied by a community moderator finally stopped interactive conflict behavior on the community platform. However, the unexpected reactions prompted SPAR to revise its decision to print and distribute the winning bag. Instead, the second and third-ranked designs, which were accepted in the community, were realized (Gebauer et al., 2012; Hutter et al., 2014).

## 2.3. Information diffusion and opinion adoption

As the previous examples show, negative opinions are rapidly diffused and represent new challenges for corporations to deal with. In the following we discuss how negative opinions diffuse within online communities and what factors influence the adoption of those opinions as these factors might critically influence the effectiveness of different conflict management strategies. Information diffusion and opinion adoption in social media sphere have been identified to depend on: (i) the influence of the social environment in which the information exchange takes place i.e. the number of affected members within a social structure, (ii) the personal characteristics of message-senders i.e. credibility, and (iii) the characteristics of message receivers i.e. strength of established opinions and openness to other’s opinions.

## 2.3.1. Social influence on each other’s opinions

Social influence denotes the phenomenon in which individuals are influenced by the actions taken by others in a social system to behave in a similar way. Members of a group tend to possess an intrinsic desire for consensus and tend to adjust their opinions to those of the majority (Asch. 1955). This has been found to be an important mechanism in the social media sphere as well (Anagnostopoulos et al., 2008; Guille et al., 2013). The probability of adopting a negative opinion therefore depends on the proportion of other community members already expressing this negative opinion. While individuals may be uninfluenced by opinions that are rarely expressed, these opinions might become worthy of consideration and adoption if they are expressed by a large proportion of other community members (Lee et al., 2015: Miller et al., 2009: Moe and Schweidel, 2012). If enough individuals adopt a given opinion, self-sustaining cascades leads to viral and contagious adoption (Gladwell, 2002). These informational cascades lead to herding effects in which individuals converge to a uniform social behavior. Individuals thereby assume an information asymmetry, considering their own information inferior to the opinion of the majority (Banerjee, 1992, 1993; Bikhchandani et al., 1998). This herding is found in numerous online settings including product ratings (Lee et al., 2015; Moe and Schweidel, 2012) or behavior in OSS communities (Oh and Jeon, 2007).

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

Literature has described these online information diffusion processes either through graph-based or non-graph based approaches (Guille et al., 2013). Graph-based models<sup>5</sup> (Chen et al., 2011; He et al., 2012; Stich et al., 2014) are based on directed graphs and assume that the likelihood an individual is influenced by information increases as more of his/her neighbors, connected through direct relationships, are influenced (Kempe et al., 2003). In our study we rely on a non-graph approach which do not assume a specific graph structure (Yang and Leskovec, 2010). Firm-hosted communities are typically closed to unregistered members. However, once registered, information sharing, especially when concerning negative messages, is public to all members and does not take place in private bi-directional relationships between members. Therefore our non-graph based model assumes that a negative message can be read by all community members, independently of direct ties.<sup>6</sup> Further it considers how many community members have already adopted the negative opinion. The more members agree on a specific opinion, the more it influences others’ opinion adoption process.

## 2.3.2. Impact of one’s credibility on others’ opinions

Not all opinions voiced in a community contribute equally toward changing members’ opinions (Miller et al., 2009). Rather some individuals, opinion leaders, have been found to exert a considerable amount of influence over others’ opinions (Kaiser et al., 2011, 2013; Lu et al., 2013; Stephen et al., 2012; Watts and Dodds, 2007). This ability is related to personal and social characteristics (Huffaker, 2010; Sun et al., 2006; Wasko and Faraj, 2005). In our model we summarize these in the concept of perceived credibility due to an individual’s level and type of contributions and activities.

Individuals are more likely to be persuaded by a message and adopt the same opinion if the message sender is perceived as credible. Perceptions of credibility ascribed to individuals are associated with trustworthiness and expertise (Hovland and Weiss, 1951; Hovland et al., 1953). To exert influence, opinion leaders must be trusted, reflecting an audience’s belief that a message sender provides information in an honest, and fair manner. Perceived trustworthiness influences a recipient’s willingness to listen, absorb others’ knowledge, and accept advice in online settings (Ridings and Gefen, 2002; Smith et al., 2005). Further, perceived expertise, the assumption that a message sender is qualified to provide valid and accurate expert information, is affecting one’s ability to influence others (Watts and Dodds, 2007). In addition influence on others’ opinion formation depends on the connectedness of individuals in a social structure (Wasko and Faraj, 2005; Watts and Dodds, 2007). Individuals who are well connected in terms of many relationships (Iyengar et al., 2011; Wasko and Faraj, 2005) and/or with otherwise disconnected sub-groups (Hinz and Spann, 2008) have an advantage in influencing others. Through many social relationships, community members can gradually gain and build trust and demonstrate their expertise within an online community. The social media environment has brought about transparency in the evaluation of expertise and trustworthiness, as it can be based on explicit information from personal profiles, posting histories, or reputation applications (Brown et al., 2007). Individuals’ credibility can be assessed by observing their behavior and level of engagement, including quantity and type of contributed content, and contextualizing it in terms of the community’s purpose and culture (Fayard et al., 2004; Huffaker, 2010). Individuals who show greater levels of knowledge and involvement in their contribu tions and provide high quality content in terms of readability, helpfulness, and comprehensiveness have greater informal influence on the opinion of other users (Liu et al., 2007; Lyons and Henderson, 2005; Otterbacher, 2009). Hence, the credi bility attributed to an individual in our model is based on his/her perceived trustworthiness and expertise and his/her contributions in terms of content quality, quantity, and social relationships. While individuals with high credibility can easily exert influence, individuals are generally unaffected in their opinion formation by negative statements from unimportant, inexperienced, dishonest, or unreliable persons. Therefore activities of firm-agents, such as moderators in firm-hosted communities, may be seen critical (Awad and Etizon, 2007). Consumers have learned that firms communicate and act with the intent to persuade them (Bickart and Schindler, 2001). Messages from actors with an organizational background are perceived as less credible than messages from peers (Berthon et al., 2009; Garg et al., 2011). To influence overall opinion and manage conflict through active intervention moderators must therefore carefully build credibility with a long-term perspective through their prior actions and contributions. Further research suggests that weak negative information causes individuals to act defensively (Pfeffer et al., 2014). Hence if negative messages come from sources of low credibility this can actually strengthen defensive actions of other community members.

## 2.3.3. Individuals’ insistence on own opinion and openness towards others’ opinion

The adoption of someone else’s opinion also depends on the strength of an individual’s pre-existing opinion (Kaiser et al. 2013) which determines both the insistence on his/her own opinion and the openness towards others’ opinions (Ahluwalia, 2000) and finally one’s individual threshold to adopt or withstand others’ opinions (Ahluwalia, 2000). These thresholds convey the tendency of each individual to maintain his/her existing (positive or neutral) opinion in the presence of newly emerging alternative negative messages in the case of conflict (Batra et al., 2012; Stich et al., 2014). Individuals who hold very strong opinions are particularly immune to counter-attitudinal information and are likely to stick with their initially strong positive (negative) opinions when faced with adverse views (Ahluwalia, 2000). Further, they do not only hold their strong opinions, but even start to actively spread WoM expressing the opposite opinion (Batra et al., 2012; Stich et al., 2014). The stronger the individual’s opinion, the higher his/her insistence on the current opinion and the more resistant he/she is to social influences and adoption of alternative opinions; and vice versa, the more open, the more easily the individual may adopt others’ opinions (Ahluwalia, 2000; Stich et al., 2014). The more community members in an online community exhibit a strong positive opinion toward the community itself and the hosting organization, the more likely they are to hold this opinion when faced with conflicting messages within the community. They are also more likely to propagate this positive opinion through their interaction, and in this way increase resilience to negative information (Bhattacharya and Sen, 2004) and avoid the spread of negative opinions resulting in firestorms.

Based on these insights, our model captures the insistence and openness of individuals in their reactions towards others opinions. Assertiveness and cooperativeness allow describing how opposing individuals or groups may deal with others opinions in a conflict situation. The higher an individual’s level of assertiveness, the more he/she will insist on his/her own opinion and point of view and even engage in active communication expressing his/her opposing opinion. The higher an individual’s level of cooperativeness, the more open he/she is to others’ opinion and the more willing to give up his/her own opinion. Therefore, one’s openness towards others’ opinions or insistence on one’s own opinion depends on the assertiveness and cooperativeness of the individuals.

## 2.4. Conflict management

Two literature streams discuss how to effectively manage conflict situations in online communities and minimize the effect of negative interactive conflict behavior: First, recent research on social media crisis communication (Chang et al., 2015; Jin et al., 2014; Lee et al., 2015; Qi et al., 2014; Xia, 2013) builds on situational crisis communication theory (Coombs, 1998, 2011) to investigate the impact of different response strategies to crisis situations in the social media sphere. Second, organizational theory on conflict management and its different conflict management strategies (Pruitt, 1983; Rahim, 2002; Thomas, 1976) investigates how conflicts in online relationships are managed in an effective way (Ishi, 2010).

According to Coombs (1998), response strategies to a crisis – an unpredictable event which can seriously impact organizations performance and generate negative outcomes – might vary from accommodative to defensive strategies. In terms of negative online WoM, these responsive actions have been extended to also include no-action strategies – companies attempts to remain entirely silent or to engage in meaningless communication unrelated to the problem itself (Lee and Cranage, 2014; Lee and Song, 2010). Accommodative strategies refer to corporate acknowledgement and acceptance of existing problems, emphasize image repair, and include ingratiation, corrective and recovery actions, and full apology (Jin and Liu, 2010; Lee and Song, 2010). Finally, defensive strategic responses are based on the insistence that there is no problem by denying responsibility, justifying, scapegoating, or attacking and accusing others (Coombs, 2011; Jin and Liu, 2010; Xia, 2013).

Also organizational research on conflict management has presented a number of different styles for managing conflicts in a structured way. Blake and Mouton (1964) first identified five modes to manage conflict, including problem solving, smoothing, forcing, withdrawal, and sharing. Building on this initial concept, Thomas (1976) and Thomas and Kilmann (1978) argue that these styles are differentiated along two dimensions: the concern for one’s owns self-interest (assertiveness), and the concern for other’s interests (cooperativeness). Based on these two dimensions, various taxonomies of different conflict management styles have been operationalized (see Fig. 1) (Pruitt, 1983; Rahim, 1983, 2002; Thomas, 1976). While avoidant strategies (low cooperativeness and assertiveness) imply neglecting or denying a conflict, accommodating (high cooperativeness, low assertiveness) means making concessions and yielding to others’ wishes. Competitive strategies (high assertiveness, low cooperativeness) are more about gaining and maintaining power and authority and defending own interests, concerns or something that is believed to be right, whereas collaborating (high assertiveness and cooperativeness) is about integration, problem solving, and confirming the concerns of all parties (Thomas and Kilmann, 1978). Finally, compromising (moderate assertiveness and cooperativeness) implies sharing and finding a middle ground (Rahim et al., 2001).

Findings on effective management of crisis or conflict situations in both literature streams support each other. No-action strategies are seen as the least effective among organizational responses (Lee and Cranage, 2014). Generally, both streams favor a more problem-solving and collaborative approach as the most effective approach because it caters to the interests of all parties involved (Pruitt, 1983). In the context of online negative WoM, accommodative strategies have been found to be positively related to a firm’s reputation and sympathy, reducing the perception of a firm’s responsibility and resulting in positive behavioral responses (Chang et al., 2015; Lee and Song, 2010; Xia, 2013). These accommodative, problem-solving, and collaborative approaches are characterized by two integrative concepts. First, they involve the pursuit of rich and positive communication patterns on a consistent level by showing willingness to cooperate with the opposing group. Second, these approaches aim at facilitating an open, transparent exchange of information in order to find a mutually beneficial solution that is acceptable to both parties (Rahim, 2002). Harsh, competitive, and aggressive strategies, in contrast, have been found to be ineffective or to further spur conflict and escalation (Qi et al., 2014). Such defensive strategies negatively impact image and reputation and provoke anger and negative perceptions (Chang et al., 2015; Lee and Song, 2010). Strategies of denying or deleting conflict posts have also been shown to be very ineffective and harmful (Qi et al., 2014). However, recent research has also highlighted the situational dependency of most appropriate strategies. More accommodative response strategies taking collaborative, problem solving approaches are more accepted and effective in the case of an organization-internal crisis origin, such as mismanagement or management failure (Jin and Liu, 2010; Jin et al., 2014). If the crisis origin is external to the organization, such as weather incidents or accidents, defensive responses are more likely to be accepted and successful (Jin et al., 2014). Therefore, in cases of obvious organizational failure, admitting fault might be

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

![](/api/attachments/J59YZTSA/fulltext/images/54bfaf63136df9fea318961cac4d3ba69b49b71daf869e018020760cc7fd1219.jpg)  
Fig. 1. Different conflict management styles based on assertiveness and cooperativeness.

crucial, whereas an apology and a problem solving approach might not necessarily be the most effective strategy in other cases (Coombs and Holladay, 2008)

As companies become aware of the potential risk of social conflict in online communities, they should continuously mon itor the dialogue and actively manage conflict situations once they emerge. The dynamic nature of online communities requires a high degree of promptness in terms of response and reaction (Benthaus et al., 2016; Kaiser et al., 2011; Thomas et al., 2012; Ulmer, 2001). An anticipatory posture with regard to potential consequences is required throughout the conflict management process (Thomas et al., 2012; van Noort and Willemsen, 2012). Sound preparation, sufficient staffing, and honest evaluation of the situation are prerequisites for successfully managing conflicts in the online sphere (Gonzales-Herrero and Smith, 2008).

Considering insights from both literature streams, we specifically follow conflict management theory for specifying our agent-based model. We rely on the specification of two agent characteristics, assertiveness and cooperativeness, to capture how community members deal with others’ conflicting views and opinions. Reliance on the combination of continuous levels of these two dimensions allows us to capture the entire range of conflict management styles suggested by this research stream while also considering the aspects of the two main response strategies suggested by crisis management. The higher the level of assertiveness, the more someone will insist, compete for, and defend his/her own opinion and point of view. The higher an individual’s level of cooperativeness, the more someone is willing to act in the interest of others, give up on his/her opinion, and accommodate.

Fig. 2 synthesizes in detail all insights derived from (1) online communities literature, (2) social conflict theory, (3) information diffusion theory, (4) opinion adoption theory, and (5) literature on conflict management and crisis communication for our model specification. Literature on online communities gives insights on members’ different reading and posting activ ities. The processes of information diffusion and opinion adoption depend on the prevalent opinion within the community, the credibility of the message senders, and an individual’s openness towards others’ opinions or insistence on his/her own opinion captured by his/her assertiveness and cooperativeness. Finally, we specify conflict management styles through combinations of assertiveness and cooperativeness.

## 3. Method

We explore conflict management in online communities via ABS. Agent-based models have been widely utilized to understand various social phenomena such as digital markets, violence, conflict modeling (Jager et al., 2009), trust and cooperation, communication networks (Lazer and Friedman, 2007), innovation diffusion (Delre et al., 2007, 2010), and, most recently, virtual communities (Schweitzer and Garcia, 2010). This method usually follows a bottom-up approach: the behavior of system components (agents: community members) is modeled to understand the emergent behavior of the system (online community) as a whole, A major strength of this method is its capability of studving and understanding complex adaptive systems such as human relationships; thus, this method has been broadly applied in the social sciences (Squazzoni, 2009). In his introduction to ABS, Bonabeau (2002) argues that the application of ABS for modeling human systems is especially useful when

‘‘the interactions between the agents are complex, nonlinear, discontinuous, or discrete (for example, when the behavior of an agent can be altered dramatically, even discontinuously, by other agents)” (Bonabeau, 2002, p. 7287). This matches the case of firestorms, where community members’ opinion changes dramatically due to the actions (messages) of other members.

![](/api/attachments/J59YZTSA/fulltext/images/0d23387f5e3e0e9763cf2d6b62f2efe12fee6a3492f9293d3e4dbe87903bf744.jpg)  
Fig. 2. Overview of theories and implications for model specification.  
the population of a system is heterogeneous, which is the fact for online community members. In this paper, we are especially interested in the influence of the moderation style on the management of a firestorm in an online community, so it is obligatory to model at least one member (the moderator) who is essentially different from the rest of the community members.  
‘‘when the topology of the interactions is heterogeneous and complex” (Bonabeau, 2002, p. 7287), which is the case when a firestorm splits the community into two camps, a situation that is regularly observed in practice as well as in our model.

All of the above-mentioned characteristics impose barriers for analytic modeling, since non-linear emergent behavior of a complex system regularly eludes closed-form solutions of a set of equations that captures these phenomena on a systemlevel. Case studies allow for deep insights into the development of firestorms but lack the necessary reproducibility and suffer from the overwhelming complexity of real-world social systems as well as limitations in data availability (Lazer and Friedman, 2007). In contrast, ABS allows us to study the underlying theoretical mechanisms, micro-mechanisms, and processes of conflict management in a complex system in an analytically focused and tractable way. The agent-based model specified in this study simulates the interaction behavior of individual members of an online community to understand the dynamics of conflict management and avoidance of conflict escalation in that community. Computer simulation enables us to examine inductively the impact of manipulating multiple features and constraints of the system and observe the outcome. Hence, with ABS ‘‘what if” analyses are feasible. This study evaluates a range of conflict management scenarios which would be extremely difficult and costly to test in the real world. Applying ABS, however, provides the opportunity to inves tigate how various specific configurations in the community and characteristics of participating individuals affect the grave ness of an emerging conflict or can avoid its escalation

## 3.1. Model specification

A broadly accepted maxim in ABS in social sciences is the KISS principle, ‘‘keep it simple, stupid!” (Axelrod, 1997). It postulates building a model on simple assumptions so that one can fully understand the influence factors considered in the model and is still able to identify the potential drivers of any result. Therefore, ABS does not claim to represent the accuracy and comprehensiveness of reality in an exhaustive model, but rather focuses on a set of a few relevant factors and the detailed understanding of their influence on the outcome of interest. This requires simplifying assumptions when specifying the model (Ren and Kraut, 2014). In the case of our model, the insights and basic assumption drawn form the multiple theories summarized in Fig. 2 allow us to develop a parsimonious model that covers the following factors identified to be most relevant for social conflict, information diffusion, opinion adoption, and conflict management in the setting of online communities.

First, we consider the individual opinions OP that actors within the community may have concerning the hosting orga-<sup>ð Þ</sup>nization and its brand, product, or service that is the focus of the initial negative conflict message. We characterize this as one single dimension ranging from strongly positive to strongly negative. The opinions of all community members determine the overall opinion of the online community OP calculated as the mean of all opinions expressed within the community, reflecting the opinion and extent of adoption within the social environment. Next, we assume that the level of credibility CR of individual actors in the community determines their ability to influence others’ opinions based on the trust and expertise ascribed to an individual due to his/her contributions in the community. Aside from that, the level of assertiveness AS determines how strongly an individual will insist on his/her initial opinion and actively communicate this <sup>ð Þ</sup>opinion in opposition to a given message. To cover both dimensions of conflict management styles, the level of cooperativeness CO demonstrates to what extent an individual will be willing to give up his/her initial opinion and adopt a view point closer to the initially communicated conflict message. Finally, an individual actor’s reading activity RA determines the probability that an actor becomes aware of the publically available opinion in the community. In the following, we will operationalize these factors on an agent level.

## 3.1.1. Agents

We model an online community with agents $a \in \{ 1 , 2 , \ldots , A \}$ characterized by the following attributes:

Each agent has his/her private opinion ${ \mathsf { O P } } _ { a } \in [ 0 ; 1 ]$ with 0 denoting a strong negative opinion and 1 a strong positive opinion.

To describe an agent’s standing in the community, we associate each agent with a private credibility rating $\mathsf { C R } _ { a } \in [ 0 ; 1 ]$ <sup>2 ½ </sup>where 0 points again to a low value and 1 to a high value. As argued above, there is a strong correlation between the credibility of a community member and the quality of his messages. Therefore, we assume for the sake of a parsimonious model that the quality of a single message depends solely on the credibility of the sender.

Each agent is assigned a private cooperativeness level ${ \mathsf { C O } } _ { a } \in [ 0 ; 1 ]$ that characterizes his/her behavior when interacting <sup>2 ½ </sup>with other agents. 0 refers to a completely uncooperative agent, while 1 denotes a fully cooperative agent.

As a second dimension of interaction, an agent has a private assertiveness level $A S _ { a } \in [ 0 ; 1 ]$ ; with 0 pointing to a very low and 1 to a very high level of assertiveness.

We further apply a certain reading activity level $\mathsf { R A } _ { a } \in [ 0 ; 1 ]$ for each agent.

All of these attributes are modeled using a continuous scale (Ahluwalia, 2000; Stich et al., 2014). This allows a high level of heterogeneity in terms of community member characteristics. Through these continuous parameters, each agent is characterized by a specific behavior when interacting in the community and engaging in a discussion. This enables us to fine-tune each agent when assigning certain roles. All community members are assigned a certain level of opinion, credibility, assertiveness, cooperativeness, and reading activity. Compared to ‘‘ordinary” community members aggressors and moderators differ in their levels on these variables. An ‘aggressor’—a community member starting to seed negative messages because he/she may be dissatisfied, angry, or indignant (Bickart and Schindler, 2001; Johnson and Kaye, 2004)—is typically modeled as an agent with a strong negative (low) opinion level, relatively low cooperativeness, and relatively high assertiveness. ‘Moderators’—actors with an organizational background whose task is to react to negative posts and emerging conflict (van Noort and Willemsen, 2012)—are modeled as agents with a very strong positive (high) opinion. For moderators, combinations of differing levels of cooperativeness and assertiveness provide unique conflict management styles, the impacts of which are analyzed. Further credibility levels of both community member roles are varied to analyze the impact on opinion adoption and conflict management style.

## 3.1.2. Specification of information diffusion and opinion adoption processes

In the following, we model the processes of information diffusion and opinion adoption. In our model, messages are the main information vehicle (Guille et al., 2013). Information diffusion in the community is enabled by public messages $M _ { a , t }$ that are posted by the agents over $t \in \{ 0 , 1 , \ldots , T \}$ rounds. We assume that these messages are published on a publically <sup>2 f g</sup>accessible wall, rather than via private messages between individuals. We suppose that individuals publish messages to share various kinds of information and opinions about hosting organizations and its products and brands with a large number of other actors. Therefore, our model assumes that any message can be read by every agent who is a member of the community, independent of his/her social ties established with other members of the community.

The round structure serves a basic time structure in our model. T 19 provides an upper limit for the number of rounds <sup>¼</sup>we conduct. In some repetitions of the model, information diffusion stops automatically after a few rounds, as no agent posts further messages. However, we also observe repetitions where the posting activity of agents remains high for a long time, meaning that the initial negative conflict message diffuses and raises a firestorm, characterized by high posting volume, which does not settle. In those cases, the variables under consideration (e.g., average opinion of the community) converge and do not change substantially when conducting more than 20 rounds. Fig. 3 provides an overview concerning the programing logic of our model.

The potential firestorm starts by an aggressor posting one message with a negative opinion in round 0. We suppose that the negative content of the message refers to an organization-internal issue such as its products, community participation experience, or relationships with the firm. This rules out messages with origins external to the organization. We further assume that in each of the following rounds t, each agent in the community has the opportunity to read the public messages that other agents posted in round t 1. Whatever messages an agent reads can be used to update his/her opinion, and finally <sup></sup>an agent can optionally post a message that can be read by other agents in the following round $t + 1 ^ { 7 }$ (Ren and Kraut, 2014). The three activities of reading, opinion updating, and posting will be described in detail below.

```txt
Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002
```

![](/api/attachments/J59YZTSA/fulltext/images/9850ac8faae964cdb704085d68b07aa60f55030ef5e80eab90500f033adf2c8c.jpg)  
Fig. 3. Flowchart describing one repetition of the model. Each repetition covers interaction of the community over 20 rounds (orange box). In each round, all agents have the possibility to engage in the discussion (blue box). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

First, an agent a x collects his/her impression of the opinions that other agents expressed in the former round by successively going through all messages $M _ { a \ne x , t - }$ sequentially.<sup>8</sup> For each message, agent a first decides whether to read it based on his/her reading activity. The probability to read a message $M _ { y , t - 1 }$ posted by a sender in the previous round will be $P ( r e a d ) = { \mathrm { R A } } _ { x } . { ^ 9 }$ In the next step, the reader of message $M _ { y , t - 1 }$ decides whether to include the opinion expressed by agent $y \mathrm { ~ -- ~ } 0 \mathrm { P } _ { \mathrm { y , t - 1 } } \mathrm { ~ -- ~ }$ in the process of updating his/her own opinion, $0 \mathsf { P } _ { x , t - 1 }$ . More specifically, $0 \mathsf { P } _ { y , t - 1 }$ will be included in this updating process if and only if the following condition is met:

$$
\left| \mathrm{OP} _ {y, t - 1} - \mathrm{OP} _ {x, t - 1} \right| <   \frac {\mathrm{CO} _ {x} + (1 - \mathrm{AS} _ {y}) + \mathrm{CO} _ {y} + \mathrm{CR} _ {y}}{4}.
$$

1

The left-hand side of this less-than-condition denotes the absolute value of the divergence of opinions between agents x and y. The higher this difference, the more the opinions of x and y diverge from each other and take opposing, polarizing viewpoints. The more an agent disagrees with the opinion that another agent expresses in a message, the less likely this opinion will be incorporated into the opinion updating process. The right hand side of the equation shows that the chance that agent x will include y’s opinion:

Increases with higher values for ${ \mathrm { C O } } _ { x } ,$ , meaning cooperative agents will be more open to other agents’ opinions in general.

Decreases with higher values for $\mathsf { A S } _ { y } ,$ , taking into account that an agent might feel offended or annoyed by a highly assertive message sender.

Increases with higher values for ${ \mathsf { C O } } _ { y } .$ , as an agent will be more tolerant of a cooperative agent’s opinion.

<sup></sup> Increases with higher values for ${ \mathrm { C R } } _ { y } ,$ as an agent is more likely to accept the opinion of a credible agent.

As ${ \mathsf { O P } } _ { a } \in [ 0 ; 1 ]$ , the left-hand side of the condition will be limited to values between 0 and 1. The right-hand side of the condition is designed to deliver values between 0 and 1 as well. According to the theory of social influence, which postulates that an individual’s behavior is influenced by the majority of opinions held by others, agent x will then calculate a weighted average opinion of all opinions expressed in the messages he/she has read with the corresponding credibility of the senders serving as weighting factors. The resulting opinion of the online community expressed in t 1, as perceived by agent a in his her updating process in round t, will be denoted as $0 \mathrm { P } _ { c o m / a , t - 1 }$

In the next step of the opinion updating process, we refer again to the agent’s assertiveness. We argue that the more assertive an agent is, the more he/she will stick with his/her own (former) opinion $\mathsf { O P } _ { a , t } .$ , and the less likely he/she will take into account the opinions of other agents. Hence, he/she will calculate his/her updated opinion as

$$
\mathrm{OP} _ {a, t} = \mathrm{AS} _ {a} \cdot \mathrm{OP} _ {a, t - 1} + (1 - \mathrm{AS} _ {a}) \cdot \mathrm{OP} _ {\text { com } / a, t - 1}.\tag{2}
$$

Finally, an agent must decide whether to post a message him/herself in this round. In our model, this posting activity is triggered if an agent reads a message that he/she perceives as controversial.<sup>10</sup> More specifically, when reading a message $M _ { y , t - }$ <sub>1</sub>, agent x will decide to answer if

$$
\left| \mathrm{OP} _ {y, t - 1} - \mathrm{OP} _ {x, t - 1} \right| > \frac {\left(1 - \mathrm{AS} _ {x}\right) + \mathrm{CR} _ {y}}{2}.\tag{3}
$$

The left-hand side of the condition implies that a higher divergence of opinions will increase the chance that agent x answers. The right-hand side takes into account that an assertive agent is considered to be more active in terms of expressing his/her own opinion. A higher assertiveness will thus increase the agent’s chance to post a message. We further argue that an agent will feel the urge to reply to a message given the message sender’s lower credibility, thus lower values of ${ \mathrm { C R } } _ { y }$ also increase the agent’s chance to post a message.

## 3.2. Model implementation

We programmed the model in JAVA. This choice was made due to the advantages that JAVA offers, including high processing speed due to efficient freeware compilers in combination with multithreading, object orientation, and platform independence. All core routines of the model were developed from scratch since existing simulation software packages were not flexible or efficient enough to incorporate all aspects of the developed model.

## 4. Analyses and results

## 4.1. Starting conditions

Our algorithm is applied to all agents (community members, aggressors, and moderators) in all rounds. Depending on the starting conditions of the model, this either results in a lively discussion where aggressor(s), moderator(s), and other community members post several messages over multiple rounds, or it leads to a quick convergence of opinions in the community, in which case the discussion stops after a few rounds. We argue that the starting conditions of our model represent a particular configuration of factors concerning the online community. By economic reasoning, we first develop a base-case scenario reflecting a typical online community situation on the specified factors. In the results section, we will then vary several values of the starting conditions while keeping reference to the theoretically optimal conflict management style of simultaneous assertiveness and cooperativeness in every scenario.

The exact figures for all applied parameters for the starting conditions of the base case are summarized in Table 2. By default, we analyze a rather small online community with 50 active members.<sup>11</sup> We assume their opinions follow a normal distribution with a mean of 0.5 and a standard deviation of 0.15 (we cut values below 0 and above 1 if they occur). This provides us with a scenario where the community members are unsettled in terms of a given annoyance. The values for cooperativeness, assertiveness, and credibility of normal agents are all uniformly distributed in a broad range to guarantee a high heterogeneity among the discussants. All ordinary community members have a rather high reading activity of 0.6

Table 2  
Base case: standard starting conditions in the model.

<table><tr><td></td><td>Normal agents</td><td>Aggressor (s)</td><td>Moderator (s)</td></tr><tr><td>Number of agents</td><td>50</td><td>1</td><td>1</td></tr><tr><td>Opinion of agents</td><td>N(0.5;0.15)</td><td>0.05</td><td>0.95</td></tr><tr><td>Cooperativeness</td><td>U(0.2;0.8)</td><td>0.1</td><td>0.8</td></tr><tr><td>Assertiveness</td><td>U(0.2;0.8)</td><td>0.9</td><td>0.8</td></tr><tr><td>Credibility</td><td>U(0.1;0.7)</td><td>0.8</td><td>0.5</td></tr><tr><td>Reading activity</td><td>0.6</td><td>0.8</td><td>0.8</td></tr></table>

The single aggressor that posts the first negative message, which is the source of conflict and potentially initiates a firestorm, comes with a negative opinion of 0.05. We argue that the default aggressor should be characterized by a rather low cooperativeness of 0.1 and a high assertiveness of 0.9. These two values guarantee that the aggressor’s opinion cannot be changed easily in the discussion with other group members and provides this individual with the insistence to influence others. The aggressor is quite credible and active (each 0.8) to lever his/her influence on the community.

On default the moderator spreads a positive opinion among the community (0.95). This individual is characterized by high levels of cooperativeness and assertiveness (0.8 for each), which is in line with theories about optimal conflict management style (Pruitt, 1983; Tjosvold, 1991). The credibility of the moderator is set at 0.5, representing an above-average credibility level compared to ordinary community members, but still not ranking among the most credible community members. As in the case of the aggressor, the moderator is also characterized by higher reading activity than other agents.

To explore which characteristics of firm-hosted communities influence the management of firestorms, we build on the base case scenario and subsequently vary several starting conditions of our simulation as shown in Table 3.

## 4.2. Results

All results presented in the following are based on 100 repetitions each, which will be referred to as ‘‘one experiment.” In each single repetition, we let agents interact over 20 rounds as shown in Fig. 3. Even with the same starting conditions, each single repetition of our simulation shows different results, since the dynamics of one repetition depend on (a) the exact distribution of attributes for all normal agents; and (b) the random numbers we apply to determine whether agents read messages. However, one major benefit of ABS over a real-world case study is the possibility to repeat a conflict situation and its management as often as necessary to generalize the results. Hence, to even out random effects, all results are based on 100 repetitions (presenting one experiment). For one experiment covering 100 repetitions r, we report the average opinion of the community at the end of each round t as

$$
\overline {{\mathrm{OP} _ {t}}} = \sum_ {r = 1} ^ {1 0 0} \frac {\sum_ {a = 1} ^ {A} \frac {\mathrm{OP} _ {r , a , t}}{A}}{1 0 0}.\tag{4}
$$

We also report the average number of messages per round to analyze the intensity and duration of the firestorm. The study shows that 100 repetitions are sufficient to produce stable results. The figures we present below do not change qualitatively with further repetitions.<sup>12</sup>

## 4.2.1. Base case

First, we analyze the base case with the parameters as described in Table 2. We then vary single parameters and compare the results to the baseline case. Fig. 4 shows the development of the average opinion of our online community over 20 rounds when applying the parameters as shown in Table 2.

Based on the starting conditions, we assume that the community is in a state of unsettledness when the conflict and potential firestorm starts in round 0. Since the base case is well balanced in terms of the influence of the aggressor and the moderator, we observe the average opinion of the community to remain relatively stable over time. The grey boundaries of one standard deviation indicated a moderate convergence of the community’s opinion over time. As the development of the average opinion in Fig. 4 is based on 100 repetitions, and since each repetition is unique, we look at the exact realization of opinions in two representative repetitions in the following.

Fig. 5a shows a particular repetition where conflict is not yet settled at the end of round 19. In the first rounds, a few community members side with the aggressor, while the opinions of the majority converge around 0.65. Due to high cooperativeness, the moderator adjusts his/her own opinion in the first rounds so that he/she can side with the community and properly react to the conflict message to manage conflict. Since we find a bipolar distribution of opinions at the end of round 19, we observe two opposing parties that hold their opinions and engage in endless discussions. Fig. 5b presents a more commonly observed repetition, in which we observe the steady convergence of opinions of all community members, including moderator and aggressor. The discussion stops when no community member feels challenged enough to respond in round

Table 3  
Variation oft starting conditions in all treatments.

<table><tr><td>Treatment</td><td>Number of moderators</td><td>Credibility of moderators</td><td>Number of aggressors</td><td>Credibility of aggressors</td><td>Prior opinion of community</td></tr><tr><td>Base Case</td><td>1</td><td>0.5</td><td>1</td><td>0.8</td><td>N(0.5;0.15)</td></tr><tr><td>Number of moderators</td><td>5</td><td>0.5</td><td>1</td><td>0.8</td><td>N(0.5;0.15)</td></tr><tr><td>Low credibility of the moderator</td><td>1</td><td>0.2</td><td>1</td><td>0.8</td><td>N(0.5;0.15)</td></tr><tr><td>Low credibility of the aggressor</td><td>1</td><td>0.8</td><td>1</td><td>0.2</td><td>N(0.5;0.15)</td></tr><tr><td>Number of aggressors (i)</td><td>1</td><td>0.5</td><td>5</td><td>0.8</td><td>N(0.5;0.15)</td></tr><tr><td>Number of aggressors (ii)</td><td>1</td><td>0.5</td><td>10</td><td> $1 = {0.8},{9} = {0.2}^{\mathrm{a}}$ </td><td>N(0.5;0.15)</td></tr><tr><td>Prior opinion of the community</td><td>1</td><td>0.5</td><td>1</td><td>0.8</td><td>N(0.7;0.15)</td></tr></table>

<sup>a</sup> In the treatment ‘‘Number of aggressors (ii)” there is one aggressor with a high credibility of 0.8 while the other 9 aggressors have a rather low credibility of 0.2.

![](/api/attachments/J59YZTSA/fulltext/images/94397ca9dd0a5a079de9ef0fe94e3825061d308080f87697ffacd06498e3eb3c.jpg)  
Fig. 4. Base case experiment. Average opinion of the community over time. Dashed lines report the range of one standard deviation (based on all opinions we observe in 100 repetitions). The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/57daa3ca32287f71e6a9270b223880a6f391a25ae6f6d2889415a9f846db1490.jpg)  
Fig, 5a. Divergence of opinion. Scatterplot of the opinions of all community members over time, In this repetition we observe no convergence, thus the discussion proceeds beyond round 19

![](/api/attachments/J59YZTSA/fulltext/images/d9311a71b1fe93465728e8612a0370bed6323d78424f00bbda483bb42b60c0bc.jpg)  
Fig. 5b. Convergence of opinion. Scatterplot of the opinions of all community members over time. In this repetition we observe a converging community opinion, so discussion stops in round 12.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

12. As shown by the average number of messages sent in one round (Fig. 4), the diffusion of the negative conflict message is well-managed in the base case and is consequently settled in most of the repetitions after a couple of rounds, avoiding an escalating firestorm.

With the standard parameters of the base case, the moderator is endowed with relatively high levels of assertiveness and cooperativeness (0.8 for each), which represents a collaborative conflict management approach. Fig. 6 shows how the average opinion of the community (0 = entirely negative, 1 = entirely positive) in the last round changes with different conflict management styles represented by combinations of different levels of assertiveness (0 = low, 1 = high) and cooperativeness (0 = low, 1 = high). The distinct peak in the section of the chart where a collaborating conflict management approach is located (high cooperativeness in combination with high assertiveness) shows that, for the base case, our model supports the advantage of collaborating conflict management approaches in an online community. We further observe that a competing approach — characterized by high assertiveness and low cooperativeness — delivers the worst result for the moderator. With high assertiveness in combination with low cooperativeness the moderator will tenaciously insist on his/her positive opinion, and therefore lose contact with the rest of the community. The average opinion of the latter will settle at a much lower value — hence will be more negative —, and, even worse, the steady discussion fed by the assertive moderator will foster negative opinion diffusion: since the moderator cannot convince other community members to side with him/her, the ongoing discussion instead creates opportunities for the aggressor to convince more and more community members of his/her negative opinion.

## 4.2.2. Varying conditions

Following the analysis of the base case, we now adjust the starting conditions by varying individual and community-level factors such as the number of moderators and aggressors, the credibility of aggressors and moderators, and the overall opinion of the community.

a) Number of moderators. We assume that the positive influence of moderators applying the optimal management style on the overall opinion of the community will amplify when we increase the number of moderators in the community. Consequently, Fig. 7 shows that, compared to the base case, the average opinion of the community settles at a much higher level when we change the number of moderators to 5. We also observe the opinion in the community to be more homogeneous in the last round of the firestorm. One reason for that can be found in the high activity of the moderators, who keep the discussion alive for a long time. In this situation, the optimal conflict management style becomes even more important. With a low level of assertiveness, even a group of five moderators will fail to influence the community’s opinion effectively, as shown in Fig. 8.

In contrast, a strong collaborative conflict management style has a much stronger positive influence on the opinion of the community compared to the base case. We observe a very similar pattern with one moderator showing high credibility.

![](/api/attachments/J59YZTSA/fulltext/images/4d5113d5f62ddefd07c430e532fae5824c65b33b2abe4e1adf01d26009f280bc.jpg)  
Fig. 6. Base case. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/a4d810aeb63b64acfbd45ea4721c66e1bec52da9b21f805e8e9c4bed6e728186.jpg)  
Fig. 7. Five Moderators. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/0860ad3a84d9491ad6c9770e35f0a1a4d710f25c00a65d5288278eeefe5b9183.jpg)  
Fig. 8. Five moderators. Influence of the conflict management style on the average opinion of the community in the last round of each repetition

b) Low credibility of the moderator. The chances of the moderator influencing the community will decrease when we weaken his/her position. Assuming that he/she has a low credibility $( \mathbf { C R } _ { M o d } = 0 . 2 )$ , we find the average opinion of the community to settle at a lower level compared to the base case (see Fig. 9). In this case, the theoretically optimal conflict management style no longer works as expected. When the moderator lacks the necessary authority in the community, an assertive conflict management style has no potential to calm down conflict and avoid a negative overall opinion within the system (see Fig. 10). The moderator’s high assertiveness keeps the discussion alive, allowing the aggressor to reiterate his/her point in the discussion. In other words, before fighting a lost battle, the moderator is better off accepting the situation and changing to a compromising or even accommodating strategy

These findings are reflected in and supported by the Moleskine case. The company had asked their community members for contributions in a way, which made them believe they were being exploited. This set-up had already reduced trustworthiness and credibility attributed to Moleskine within the community. After the first negative posts on the community site, Moleskine failed to react for one week, and then began aggressively defending their position and choice of format by arguing that other brands were following similar concepts with great participation and results. They insisted on their approach and highlighted that submission was free and voluntary, and that everyone could decide whether to participate or not (Moleskine, 2011). This very competitive and assertive style backfired, resulting in an even more negative community opinion, as also shown in Fig. 10. This style did not calm but rather heated the discussion on the community site. Five hundred forty-two conflict-related comments followed, displaying the angry reactions that became even further outraged when allegations were raised that Moleskine was beginning to delete negative Facebook comments. Four days later, Moleskine responded again. This time, they adopted a more accommodating approach characterized by high levels of cooperativeness. They apologized for their late response, stated the purpose of the contest had never been to exploit people, and admitted their mistake. They announced that only the copyright of the winner’s design would be retained by Moleskine, while the copyright of all other designs would be left with the designers. This approach was more successful; however, as with our

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

![](/api/attachments/J59YZTSA/fulltext/images/4f69525893239c1dc8ca79da6660afc550e4c4d22135cf130a210113ddbdb018.jpg)  
Fig. 9. Low credibility of the moderator. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/57de813ea27b94a743aee4fa9e31933483f0f2dcf766f8ea20d6e40674cb98bc.jpg)  
Fig. 10. Moderator with low credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

simulation, the overall opinion in the Moleskine case was quite negative, with many unsatisfied and disappointed community members (Moleskine, 2011).

The same is true of the case of Pril. Despite announcements to accept community voting, Henkel changed the terms and conditions of community participation twice without any further announcement and selected another winner. Through this action, moderators lost all credibility and trustworthiness, and any further defense of the decision resulted in fierce discus: sion across community borders.

c) Low credibility of the aggressor. The strength of the relative positions of the aggressor and moderator is found to be one key factor for successfully moderating a firestorm. While the previous result showed that an assertive moderation style might be problematic if the moderator is in a weak position (i.e. moderator’s credibility is low and aggressor’s credibility is high), we now consider the opposite case: we assume that the moderator already established substantial credibility $( \mathsf { C R } _ { M o d } = 0 . 8 )$ before the conflict, and that the conflict is raised by a non-credible aggressor $( \mathbf { C R } _ { A g g } = \mathbf { 0 . 2 } )$ <sup>¼</sup>. As shown in Fig. 11, the estab <sup>¼</sup>lishment of the moderator’s pre-conflict communication and credibility is a valuable factor to properly manage a firestorm. In the case of a low credibility aggressor, a moderator with a good standing in the community should adopt an assertive moderation style. In this case cooperation is less important, and instead a more competitive, ‘‘aggressive” moderation style should be used without conceding to the aggressor, resulting in a positive opinion within the community.

This has been the case when negative conflict-related messages were posted on the community site of the SPAR just after the jury decision was published. Some participants kept following a very aggressive and offensive protesting strategy. One community member switched from raising their voice to actively calling for collective mobilization and protest actions: ‘‘Send complaints to SPAR: presse@SPAR.at or office@SPAR.at.” To diffuse this call for protest, this user very obviously set up four fake accounts that he/she registered within a short time span using similar usernames and e-mail addresses. However, this community member was not very active within the community and had not submitted any designs in the contest with his/her primary ID. Other community members openly questioned his/her intentions, identity, and trustworthiness. ‘‘Don’t hyde your identity, for what? You obiously have submitted some desings, otherwise you wouldnt be that committed. Just take the desicion as it is and come down again. By the way I see on your Acitivity Counter that you supported 300 designs - 446 maybe???????? [sic].” This reduced the credibility of this particular aggressor. The moderator reacted more assertively to this aggressor and used participants’ agreement to the terms and conditions and a code of conduct in the course of registration as justification for deleting all offending posts. The moderator, an active member of the community, acted very timely, transparently, and openly, and relied on a genial yet firm language in his/her statements. Conflict-related actions halted after this intervention.

![](/api/attachments/J59YZTSA/fulltext/images/dbf1517c537316bc247fa3f600605472a470248979bbf1789363af13ed8a3266.jpg)  
Fig. 11. Aggressor with low credibility facing a moderator with high credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

d) Number of aggressors. When we allow not a single aggressor, but multiple aggressors to engage in sending negative messages we find one moderator in a difficult position. In the case of five aggressors the posting activity of the community remains on a higher level (Fig. 12), and the average community opinion in the community declines substantially. In this case, both competing and collaborating management styles fail (Fig. 13).

If the moderator assertively insists on his/her opinion even though a substantial number of credible individuals commu: nicate an opposite, negative opinion, his/her insistence will antagonize the diffusion of the negative opinion and the likelihood of a firestorm to grow. In such a severe case accommodating might be the only appropriate strategy.

However, it might be more likely that one credible aggressor is followed by a host of multiple, less credible aggressors. We model this scenario and allow ten aggressors — a very large proportion compared to community size — of which only one is of high credibility and the others are perceived as less credible. In this case the average opinion in the community is hardly affected (Fig. 14). Although many individuals communicating the negative opinion are of considerably low credibility, again a competing management style is not successful. In contrast, like in the base case, the collaborating conflict management style is the most effective one (Fig. 15).

e) Prior opinion of the community. As shown in Fig. 16. the stronger the individuals' current opinion, the less malleable the community will be in terms of negative social influence. When we begin the simulation with $\overline { { \mathrm { O P } _ { a } } } = 0 . 7 ,$ , we observe that the <sup>¼</sup>final opinion of the community settles at that level as well, meaning that the aggressor hardly gains any influence. In that situation, the moderator's high assertiveness can easily convince the community to side with him/her. Here, it is not even necessary for the moderator to be cooperative, so a competing conflict management strategy is optimal as well.

## 4.3. Robustness checks

To test the robustness of our results, we extend our model in two ways suggested by community literature.¹³ First, we introduced directed ties (i.e. links) between agents, in which a tie from agent x to agent y indicates that agent y is a follower of agent x. The existence of a tie between agents increases the credibility agent y ascribes to agent x and increases the probability that y reads the posts of x. In our simulation, we approximate a scale-free network, which follows a power-law distribution (Barabasi and Albert, 1999). Second, we ran an additional simulation in which we increased the size of the active core of the community to 250 agents, thereby assuming a larger size of the overall community (Nonnecke and Preece, 2000, 2001). We did not adjust the number of aggressors or moderators compared to the base case. The results from both simulations support our findings of our initially specified model. Hence, our findings seem to be rather robust and valid for larger communities and when controlling for direct links.

![](/api/attachments/J59YZTSA/fulltext/images/54b3d51518c57b5f8654f9f092b8164468562dd6c133c6b6db07a7b2cfa0e857.jpg)  
Fig. 12. Five aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/2f8267d6b3966a3d70f07eb2a248029b4db31395b6d6bb6805850e49b79d9498.jpg)  
Assertiveness  
Fig. 13. Five Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition

![](/api/attachments/J59YZTSA/fulltext/images/6b04a677a8f6a435e740f31ee110ad74591daf2e435ec2d4c456e291b23a1d92.jpg)  
Fig. 14. Ten aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

```txt
Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002
```

![](/api/attachments/J59YZTSA/fulltext/images/116adbddccc620ed404f95c4c6f44c625df82b0ea54110ff9a747c082648d8b8.jpg)  
Fig. 15. Ten Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

![](/api/attachments/J59YZTSA/fulltext/images/bc9cc24f704aa3bf48153ad1341a20e6158f1dd8d00b3c1e20898fe0972261f6.jpg)  
Fig. 16. High prior opinion of the community. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

## 5. Discussion and conclusion

## 5.1. Theoretical and managerial implications

The contributions of our research are manifold: we provide insights into the conflict situations of online communities and analyze the diffusion of negative information and opinion adoption triggered by a negative conflict message, which may result in firestorms. We synthesized multiple theories in an ABM to understand the effectiveness and appropriateness of various conflict management styles. In the model, we allow heterogeneity of community members’ characteristics, including their credibility, openness towards others’ opinions, cooperativeness, and assertiveness. This variability enables analysis of how factors such as the number of aggressors and moderators, their credibility, and the overall opinion in the community affect the severity of conflict situations and the appropriateness of different conflict management styles.

With our study, we contribute to a contingency view of conflict and crisis management in the social media environment. We show that there is no universally optimal approach to handle conflict arising in an online community. While prior literature has already considered situational dependency (Jin and Liu, 2010; Jin et al., 2014), our findings highlight that conflict management is not only dependent on the origin of conflict but is also influenced by additional factors. These factors include characteristics of individual participants, such as credibility and openness to others’ opinions, as well as community factors, such as overall sentiment and opinion within the community toward the organization. Based on these factors, different conflict management styles can be either a good choice or lead to further intensified discussions, amplifying the potential for a resulting firestorm.

Our model further shows that, in a typical setting, a collaborating conflict management strategy can indeed be the key to avoiding escalation and minimizing harmful outcomes of conflict in online social environments. We show the advantages of combining high assertiveness with high levels of cooperativeness in a collaborating style, which requires the difficult balance of showing consideration and openness for opposing opinions while still not giving up one’s own point of view and continuing to actively communicate this opinion. This delicate combination is challenging in practice. However, the effectiveness of this collaborative management style is contingent on several factors. It might be appropriate in situations with one aggressor perceived as credible by the community followed by a large proportion of less credible individuals communicating the negative opinion. Here, the combination of being cooperative with the credible aggressor, while showing assertiveness for the host of low credibility actors allow successfully managing the conflict. The positive impact of a collaborating management style can further be enhanced by an increase in the number of moderators. However, when adopting a very accommodating conflict style characterized only by high cooperativeness or with low credibility, even an increased number of moderators will fail to influence the community’s opinion, and the optimal conflict management style becomes even more important. This has important implications for the set up of successful community management and moderation. Without having insights into the conflict management style appropriate to a certain situation, organizations do not create value through investing more financial and personal resources and engaging multiple individuals in the moderation and active management of conflicts.

Our results further indicate that the perceived credibility of individuals is an essential influential factor in either initiating the diffusion of negative messages that might ultimately result in a firestorm or in effective conflict management to avoid the spread of negative conflict messages and increase resilience within the community. These findings are supported by pervious empirical evidence. By employing analytical modeling Stich et al. (2014) have shown that when initiators of negative eWoM have an important social status then the threat becomes substantial and may potentially lead to a firestorm. Based on first empirical observation in case studies Pfeffer et al. (2014) have further suggested that trusted information sources are essential in managing negative messages. We provide further evidence and show that adopting a collaborative conflict management style might fail when the moderator lacks a certain level of credibility or if multiple aggressors are of high credibility. Here our study shows that a more compromising or even accommodating management style might be more efficient. Our findings especially highlight that adopting an assertive, competitive approach in such situations, where a community moderator defends and justifies organizational actions and decisions taken and insists on a specific point of view, can even spark steady heated discussion and foster negative opinion diffusion and adoption to an extent where a firestorm cannot be avoided. This has been the case in the examples of Henkel and Moleskine. In both situations, community participants questioned the trustworthiness of organizational actors. In the case of Moleskine, the entire set up and incentive scheme of the online community resulted in a loss of trustworthiness and credibility amongst community participants. In the case of Henkel, the actions taken by organizational actors – changing terms and conditions to influence community outcomes in favor of the organization’s opinion – had the same detrimental effects. In both cases, the organizational actors focused on aggressively justifying and defending the standpoint of the organization. This high assertiveness had detrimental effects, resulting in fierce discussions, online firestorms, and PR debacles far beyond the community’s borders

To assess the impact and consequences of their actions, community moderators should be able to assess their level of credibility within the community at any point in time. Due to their visible organizational background and their associated commercial intent to persuade and influence others in favor of their company, moderators might not be perceived as trustworthy per se and may initially lack the necessary levels of credibility needed to influence others. First empirical case studies have also found that especially in the emergence of a firestorm, it is very difficult for organizational members to be perceived as credible and trusted sources of information and effectively diffuse positive information (Pfeffer et al., 2014). On one hand, the moderator’s establishment of pre-conflict credibility is valuable for proper conflict management and avoidance of a firestorm, but on the other hand, also the consistent awareness and assessment of what perceptions are prescribed to the community moderator are critical. Both can be achieved by organizational actors within communities through open, transparent, and proactive communication, including fair and clearly communicated objectives, purpose, and terms and conditions. Proactive and frequent interactions between community members and moderators from the hosting organization should result in a positive and trustful atmosphere, which is important for building credibility. Especially in large communities with a high communication volume, also text-mining software can provide helpful tools to capture the current sentiment within the community.

Besides the credibility of moderators, our study has shown that the credibility of the individuals who engage in spreading negative opinions and messages importantly influences the choice of appropriate conflict management. As has been shown in the case of SPAR, because the credibility and trustworthiness of the main aggressor was questioned by other community members, community moderators could successfully apply a more assertive conflict management approach, defending the organization’s position and transparently and openly deleting the conflict messages of this particular individual. As shown by our study, this competing management style characterized by assertiveness would not have been very successful in the case of a highly accepted community member even if multiple less credible members would have further spread the conflict message. In such a case, assertiveness would have been detrimental even spurring further negative communication. Therefore, it is important for community moderators to diagnose and assess the identities of the individual(s) spreading the negative conflict message. This information includes insights on their acceptance and standing in the community, if they are very active and well accepted contributors, and if they seem to be experienced and therefore also respected based on the quality and elaboration of their contributions. Again, this can be achieved through actively engaging in communication and skimming contributions. Specific community design features can help here, as well. Activity counters, or statistics that show the most valuable community members in terms of contributions, helpful comments, and suggestions to others, may help moderators to quickly assess the reputation and standing of an individual within a community. Such community features can be based on contribution quantity or voting and assessment mechanisms through which all community participants rate the helpfulness or informational value, etc. of others’ contributions.

Thirdly, our results reveal that the stronger individuals’ current opinion and the more positive the atmosphere and opinion within the entire community, the less susceptible the community as a whole will be in terms of negative social influence. This supports first empirical studies investigating conflict management in terms of firestorms through case studies and analytic modeling (Pfeffer et al.. 2014: Stich et al., 2014). The findings of both studies suggest that in the case of firestorms counter-campaigns can become effective when employing a large ‘‘fan” base, which possibly involves members with important social status, and communicates positive message. Our finding provide additional evidence and also suggest that a way for organizations to avoid the spread of negative opinions resulting in firestorms might be to put emphasis on the long-term management of loyal participants who exhibit a strong positive attitude and those who are highly active and enthusiastic members of the community before conflict emerges. The more community members exhibit a strong positive attitude toward the purpose of the community itself and the hosting organization, the more likely they are to hold this opinion when faced with conflicting messages within the community and to propagate this positive opinion through their interactions, thereby increasing resilience to negative information. In this situation, it is possible to be assertive and adopt a competing conflict management strategy to actively defend the hosting organization and its actions. However, if participants are already dissatisfied and negative-minded, such as in the case of Moleskine, an assertive approach is very dangerous. Again, computer-aided text mining and textual analysis of communication can help the organization to obtain a better understand ing, but pre-conflict management of the community through frequent interactions and communication can signal interest in the community members’ concerns. The active consideration and integration of community members allows the building of mutual respect and an eye-level discussion, resulting in positive attitudes and opinions towards the organization and the initiated community. In such a situation, a moderator has a better chance to convince and influence the community to side with him/her when negative opinions are voiced.

Finally, we believe that our agent-based model has the potential to evolve into a multicontingency tool for diagnosis and choice of conflict management style for online communities (Burton and Obel, 2004; Ren and Kraut, 2014). Expanded with a user-friendly interface, our agent-based simulation could support community management and moderators and serve as a decision-making tool in emerging conflict situations. By changing individual parameters in the model, community moderators could run multiple ‘‘what-if” experiments to explore different conflict scenarios and match their conflict management approach to the specific context of their community such as for example in terms of aggressor credibility. Ren and Kraut (2014) have already pointed out that the potential use of simulation models as tools to support real-life decision-making is still severely under-recognized. Therefore, an effort to customize them for practical use and increase awareness about their potential is needed to raise acceptance and increase the use of agent-based simulations as decision-making tools for community management.

## 5.2. Limitations and future research

While this study provides the first insights into the characteristics that influence the diffusion of conflict messages, adoption of negative opinions, and successful conflict management within online communities, the current research has limitations that raise the need for more academic work on the topic.

First, in our study, we focus on firm-hosted communities, more specifically on online communities, in which organizations ask community participants for specific and elaborate contributions. This type of community, often set up as a contest community, require more time, effort, and intensive levels of engagement than participation in social media PR campaigns, where firms only ask for brief experiences with a certain brand, as in the cases of #myNYPD or #McDStories. The more participants engage, the more they build expectations with the hosting organization and its brand, products, or services, and the more they are emotionally attached. In such a setting, the potential of social conflict evolving into an emotionally driven fire storm is given, which makes effective conflict management strategies by organizational actors even more important. However, in other types of firm-hosted communities, such as more PR oriented campaigns, participants might show lower levels of engagement and emotional attachment, and therefore differ in their reactions to negative messages. Compared to contest communities also the positive attitude and opinion towards the community, its purpose and the hosting organization might

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

be lower in pure PR oriented platforms, which again has implications for the appropriate conflict management strategy. Different effects can also be expected in member-initiated communities without hosting organizations. For firms, it might be much more difficult to actively ‘‘manage” negative information related to their products or brands in such communities. Their legitimacy to become active, their credibility, and their trustworthiness may even be lower than in firm-hosted communities, which might significantly reduce the spectrum of conflict management strategies available. Therefore, our results have to be interpreted with caution beyond firm-hosted contest communities, and future research should focus on examining the relationships in different types of online communities.

Further, our specified model is a compromise between simplicity and accuracy. As with any ABS, we made simplifying assumptions to create our model clearly and interpretably and to capture the essence of different conflict management strategies on community opinion under different conditions. We intentionally kept the model to the minimum complexity necessary to capture some essential factors of conflict management within firm-hosted online communities. However, it would be insightful to add further dimensions that might influence the processes of the diffusion and adaption of negative opinions and conflict management within such a community. We acknowledge these limitations and discuss ways in which future research could extend and empirically test our model.

Although our specified model is based on multiple theories relevant to conflict management in online communities, this selection is not exhaustive. The chosen theories provide relevant insights for our research question; however, we acknowledge that they do not encompass all factors relevant for social conflict and conflict management in online communities. For example, information overload theory (Jones et al., 2004) proposes that people’s information-processing capacity is limited, and too much information or noise is aversive, In a large community this would reduce the chance of a conflict-related message to diffuse rapidly, Although previous research has found that, due to a negativity effect, negative messages gain much more rapid attention (Benthaus et al., 2016; Sen and Lerman, 2007), future research could explicitly consider this information overload effect in an extension of our model. Second, we do not explicitly consider quality of messages. As explained in the theory and model specification section, we define individuals’ credibility in online communities to depend on the quality of their contributed content and the trustworthiness and expertise demonstrated through this content, which is supported by literature. However, future research could still explicitly add a factor for message quality to our model. We expect message quality to function similarly to credibility in our model. Further, we model a closed world and thus ignore external communication over channels aside from public messages on the community’s forum. These other channels can have a substantial influence, but can hardly be implemented directly into our model. Therefore, our intention was to provide strategies that avoid a firestorm to develop in the first place. Hence, through appropriate management strategies conflict should be settled before the opinion in the community tilts and community opinion gets entirely negative and most importantly before the viral buzz develops and other alternate channels get involved. However, future research could indirectly analyze such external communication effects on the model, by introducing shocks to the opinion of the community. In addition, we consider a stable community size without considering joining and leaving of community members. In reality, new members can come in and others can exit the community, especially in the case of conflict, without voicing their disagreement with the situation or the conflict itself. Furthermore, the simplifying assumption that agents are able to access the complete set of messages posted in the former round but none of the messages from the recent round allows us to ignore the updating order of agents. This updating order of agents might affect their influence on the discussion. Future research could also cover the variation of parameters already included in the model, such as the distribution of individual agents’ parameters. In addition, we include only active agents in our model. Even though passive members (so-called ‘‘lurkers”) can constitute a substantial part of an online community (Nonnecke and Preece, 2000, 2001), we argue that they would not have any influence on the information diffusion due to lacking posting activity. However, since we are interested in shedding light on the development of the whole community’s opinion during a firestorm, the exclusion of passive members must be considered as a limitation that can be overcome in future research.

Finally, future research should focus on empirical testing of the present findings. Our results support previous empirical studies, which have studied parts of our model. But the calibration of the simulation based on real-world data would be of great value. This would require data on multiple online communities in which conflict emerged and was more or less successfully managed through different strategies. Although the log-files of online communities would allow researchers to access and analyze the behavioral data of community members, such as the direction and frequency of interactions between individuals and the focus of conflict formation and management, this method would also requires contextual analysis and interpretation of the content of relationships. Only content analysis allows for determining negative or positive communication behavior either intended to spur or to calm conflict. Therefore, testing our model in the field is a challenge concerning data availability and information processing limitations. However, parts of our findings could be tested in a controlled setting, such as by providing members of the community with the same negative conflict message but with different moderating styles or the same reaction of moderators with different credibility levels.

## Acknowledgement

We would like to thank editor Robert Galliers and three anonymous reviewers for their valuable comments and guidance in further developing this paper.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

## Appendix A. Robustness checks

In order to test the robustness of our results we extended our model in two ways: (i) we introduce directed ties between agents (ii) and we increase community size. The reasons for conducting these two particular robustness checks and the details of our model specification in the robustness checks are given below.

## A.1. Robustness check 1: Consideration of ties between agents

As highlighted in our theory section literature has described the processes of information diffusion and opinion adoption within an online environment either based on graph-based or non-graph based approaches (Guille et al., 2013). Graph-based models are based on directed graphs and assume that the likelihood that individuals (nodes) are influenced (activated) by information increases as more of its direct neighbors, connected through paths, are activated (Kempe et al., 2003). These approaches have been extended to also consider the diffusion of negative messages (Chen et al., 2011; He et al., 2012; Stich et al., 2014). Non-graph based approaches, in contrast, do not assume a specific graph structure (Yang and Leskovec, 2010). In our agent-based model we assume that communication and information sharing – especially when concerning negative messages - is mostly public to all members on public walls or blogs and does not take place in private bidirectional relationship between members. Therefore, we initially do not specify a graph-based model relying on specific bi-directional relationships between direct neighbors, but rather a non-graph based model assuming that a negative post or message can be read by all members in the community, independent of direct ties. To check the robustness of our findings against the inclusion of network effects, we first specify a graph-based model and introduce directed ties (i.e. links) between agents. A tie from agent x to agent y thereby indicates that agent y is a follower of agent x. This will have two effects for agent y: (1), due to this connection he/she will perceive agent x as more credible than other agents do and (2), his/her chance to read a message from agent x will increase. We will only allow followers for ordinary agents and aggressors but not for moderators, as our research question concerns the effect of moderation style on the management of a firestorm. With allowing the moderator to have followers, the position of the moderator in the graph would become relevant, and potentially interfere with the moderation style. Disentangling the two factors would clearly go beyond the scope of the robustness checks.

To increase the perceived credibility of one agent to his/her followers, we assume that each tie has strength of 0.3, implying that a follower perceives the agent he/she is following as additional 0.3 more credible than non-followers do, which can be interpreted as a substantial increase. To counterbalance the increasing overall credibility resulting from the introduction of ties, we lower the distribution for ordinary agents’ credibility to U(0.05;0.6). This way, the agent with the highest possible credibility of 0.6 will be perceived with a credibility of 0.9 by his/her followers. For the aggressor, we lower the credibility to 0.7, hence he/she will be with a credibility of 1 by his/her followers.

As outlined above, a follower of any given agent will also be more likely to read his/her messages than non-followers. More precisely, since normal agents’ reading activity is defined as 0.6 in our model, ties will again introduce an increase of 0.3, hence a 0:6 0:3 90% chance to read the message of an agent they follow. We aim at approximating a scale-free network where the distribution of ties roughly follows a power-law distribution (Barabasi and Albert, 1999), while at the same time the credibility of one agent determines the number of followers he/she has. To do so, we assume that the number of followers of an ordinary agent x is $\| 5 0 ^ { \mathrm { C R } _ { x } } \|$ . We chose this function as it respects the limits of credibility and community size:

A credibility of CR 0 will result in $\| 5 0 ^ { 0 } = 1 \|$ follower.

A credibility of CR 1 will give $\lVert 5 0 ^ { 1 } = 5 0 \rVert$ followers.

In the base-case, the aggressor with a credibility of 0.7 has $\lVert 5 0 ^ { 0 . 7 } = 1 5 \rVert$ followers.

The normal agent with the highest possible credibility $\mathrm { C R } = 0 . 6$ <sup>¼</sup>has $\lVert 5 0 ^ { 0 . 6 } = 1 0 \rVert$ followers.

The normal agent with the lowest possible credibility CR 0:05 has $\lVert 5 0 ^ { 0 . 0 5 } = 1 \rVert$ follower.

Fig. A1 shows one example of a resulting network graph based on the graph-based models specified above. One can see that the aggressor (agent 50, red) has a central position in the graph with 15 followers. He/she is linked to other central agents like agent 5, 7, and 40 who also have a central position in the graph. Other agents have a peripheral position, e.g. agent 2, 41 and 46 each have only one follower. The moderator agent 51 does not have any followers.

## A.2. Analyses and results

## A.2.1. Base case

Fig. A2 shows the development of the average opinion of our online community over 20 conducted rounds. Compared to the results in our non-graph based model without ties, it can be seen that the average opinion of the community shows a marginal decrease over the 20 rounds. Further tests show that this is indeed due to the ties (followers) of the aggressor. These directional relationships give him/her and his/her messages a slightly more sustainable impact on the opinion of his/her followers. However, the differences to the non-graph based model are very small in scale.

```txt
Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002
```

![](/api/attachments/J59YZTSA/fulltext/images/82c79d0ee0e3ce5caa12692031f3a3aaaab11d4272ed83711702d61d47e01b2d.jpg)  
Fig. A1. Example of a generated graph with ties between agents.

![](/api/attachments/J59YZTSA/fulltext/images/364df5991c8763ea1460b960fc5c98374951adf621db58e6edc87a3a6da94ee6.jpg)  
Fig, A2. Base case, Average opinion of the community over time. Dashed lines report the range of one standard deviation, The grey area refers to the number of messages per round (rescaled by the right axis).

Fig. A3 further shows how the average opinion of the community in the last round changes with different conflict management styles. Here we might again note that results qualitatively do not change after the introduction of ties. A minor difference is again that the overall opinion (for all moderation styles) is marginally lower due to the more sustainable influence of the aggressor.

## A.2.2. Number of moderators

Also when increasing the number of moderators, the adjusted model with ties almost perfectly replicates our results from the model without ties, as shown in Figs. A4 and A5.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

![](/api/attachments/J59YZTSA/fulltext/images/d2863300373d45c5d3e6784db29cfba1d754d812211fd5a3b00621eb8db816c3.jpg)  
Fig. A3. Base case. Influence of the conflict management style on the average opinion of the community in the last round of each repetition

![](/api/attachments/J59YZTSA/fulltext/images/30bbf5b53096950363b46fe27b7203a0bbe3fa786b475af7b8cb87ac4b4bbe6f.jpg)  
Fig. A4. Five moderators. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/25a7c53bde0d9d060b86a7b0f5dc8da45ed5f963a989024a7282a91a0b205347.jpg)

Fig. A5. Five moderators. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

## A.2.3. Credibility of the moderator

Assuming the moderator has a low credibility $( \mathbf { C R } _ { M o d } = \mathbf { 0 . 2 } ) ,$ , we find the average opinion of the community to develop <sup>¼</sup>very similar as in the original model (see Fig. A6). Also the former results concerning the optimal conflict management style turn out to be robust against ties as depicted by Fig. A7.

## A.2.4. Low credibility of the aggressor

Also concerning the case where a moderator with a high credibility faces an aggressor with a low credibility, the initial results concerning the appropriateness of specific conflict management styles can again be confirmed for a network with ties, as shown in Fig. A8.

## A.2.5. Number of aggressors

Robustness is given as well for the treatment with five aggressors. As shown in Figs. A9 and A10 the results for the treatment with five aggressors hardly change compared to the standard model.

For the treatment with ten aggressors, but only one of them being credible, the results of the standard model can also be replicated when including ties, as shown in Figs. A11 and A12.

## A.2.6. Prior opinion of the community

As shown in Fig. A13, results concerning the impact of conflict management styles for a community with a high initial opinion qualitatively do not change when introducing ties.

![](/api/attachments/J59YZTSA/fulltext/images/91d93664e7c4fc2bf0f124cd9c411f41a8d8a943fdbeb2fddc7dabc3b190cfe4.jpg)  
Fig. A6. Low credibility of the moderator. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/e4d136cd342bb68440ac837e3f1efa443f067eb7b9fec03d87ad76677eedd719.jpg)  
Fig. A7. Moderator with a low credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/ace82c807e570ffaf5877d5e33e65f182abac87004720b36cfd1b9acdd87c1d2.jpg)

Fig. A8. Aggressor with low credibility facing a moderator with high credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.  
![](/api/attachments/J59YZTSA/fulltext/images/09e2ad2faf2446e67508ed9eb0bd64668d7dd8e77f6ebec5351df92eb49fec5e.jpg)

Fig. A9. Five aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).  
![](/api/attachments/J59YZTSA/fulltext/images/96cb5cc6aa74cc4f566949626290fc48d59dac971df875b678448050c2b8933f.jpg)

Fig. A10. Five Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/4ee210d6c362a1a443947c4736b65d5494d88d9a95fc797e0b2823d1faca8619.jpg)  
Fig. A11. Ten aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/66f71cf5579957cbadf2a0f104fc877cc4c68660dc91a94034f3730eb74b106d.jpg)  
Fig. A12. Ten Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition

![](/api/attachments/J59YZTSA/fulltext/images/2281e1dc5648f08117300b3a9f3865b66dffe02c6c8e6d64cbc507e15490223f.jpg)  
Fig. A13. High prior opinion of the community. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online commu nities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

## A.3. Robustness check 2: Increase of community size

Online communities are virtual destinations for interacting around narrow shared interests at low efforts and costs with ease of joining (Miller et al., 2009; Preece, 2002; Wasko and Faraj, 2005). Usually these online communities are therefore large in size but they consist of a smaller core of very active members, while the majority of members only rarely participate actively (Nonnecke and Preece, 2000, 2001). As we intend to model only active agents — as stated in our model specification — our initial community size was limited to 50 members. Lurkers, as defined with Nonnecke and Preece, do not actively participate in the communication and do not post any message. Hence, we assume that these passive agents do not play an active role in information diffusion in the online community. The agents in our model therefore only represent active agents, which are willing to contribute at least once in the communication and information diffusion process. To make sure that this community size is not influencing our results we conduct a second robustness check. We start again with our base-case treatment based on a non-graph model as described in our paper, but now we change the number of ordinary agents in our community to 250. As the agents in our model only represent the active proportion of all community members, often representing only 1–10% of the entire community (Nonnecke and Preece, 2000, 2001) one can consider that this robustness check analyzes a very large community. Note that we do not adjust the number of aggressors or moderators according to community size in this robustness check but use the same numbers as in our initial analysis

## A.3.1. Base case

For the base-case, we observe a development of the average opinion in the community that is again quite similar to the original model. The main differences are that (1) the absolute number of messages is much higher due to the larger number of agents actively engaging in communication (see the scaling of the right axis in Fig. A14) and (2) that the relative share of messages becomes much smaller in later rounds, compared to the small community with 50 agents. In fact, we observe that the increased exchange of opinions in the large community tends to prevent situations where two groups of agents with diverging opinions emerge.

As shown in Fig. A15, the influence of the single moderator on the development of the average opinion is still present, and we confirm that for a large community, a collaborating conflict management approach is again the most promising option in the base-case treatment.

## A.3.2. Number of moderators

As shown in Fig. A16, the presence of five moderators still levers their influence on the community. However, we note that the increase of the average opinion that stems from the four additional moderators is somewhat smaller than in the community with 50 agents. This is due to the smaller share of moderators relative to the total number of agents. In terms of the conflict management style, we can confirm the robustness of the results as shown in Fig. A17.

## A.3.3. Credibility of the moderator

Assuming that the moderator has a low credibility (CR 0:2), we find the average opinion of the community to <sup>¼</sup>develop again very similar to the original model (see Fig. A18). In addition, the former results concerning the optimal conflict management style turn out to be robust against increasing community size as depicted by Fig. A19.

## A.3.4. Credibility vs. moderator’s credibility

As shown in Fig. A20, the influence of the moderation style is marginally dampened by the large community size when compared to the original results, but conceptually the former results can be confirmed to be robust again.

![](/api/attachments/J59YZTSA/fulltext/images/d44de4ce09a9b38114150cb4938925dcbb840d96902cc98ad2dc664430ad4256.jpg)  
Fig. A14. Base case. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/8986605d05eedc09b9da5848774e2f7bc182d5ee73a1e2aa6db0de77d143546c.jpg)  
Fig. A15. Base case. Influence of the conflict management style on the average opinion of the community.

![](/api/attachments/J59YZTSA/fulltext/images/db666706a1ccf5c92626fe3a7690d64f617c8894cb3ef0b2c7bce9b1050eebe8.jpg)  
Fig. A16. Five moderators. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/27a4982945eb530c3716da6d574201bbf477b53f481270f1d598063112d0db23.jpg)  
Fig. A17. Five moderators. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/ebd59d81928b9570e8ebe6828b53a70fa90617ca3ef28b5ddab1a6b46daf6b4a.jpg)  
Fig. A18. Low credibility of the moderator. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

![](/api/attachments/J59YZTSA/fulltext/images/8ff42ee5220c3c0a47a700e9993df4104c35b1a92dfdfc863248e89d9feb0f51.jpg)  
Fig. A19. Moderator with a low credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

![](/api/attachments/J59YZTSA/fulltext/images/df0cc40c4de31c9bff8120bfa41500c4525664124e67003d7b33396ca7973517.jpg)  
Fig. A20. Aggressor with low credibility facing a moderator with high credibility. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

<table><tr><td>Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002</td></tr></table>

![](/api/attachments/J59YZTSA/fulltext/images/24b77be7d06eea0e020994d864dbcd32e1d79b7fc1cc803f70e06c516e32f48a.jpg)  
Fig. A21. Five aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

## A.3.5. Number of aggressors

In case of a large community size the dynamics during firestorms are very similar to the standard model, as shown in Fig. A21. Concerning the moderation style, we find the effect of a highly assertiveness moderation style to be slightly more pronounced than in the smaller community, as depicted by Fig. A22

For the treatment with ten aggressors, but only one of them being credible, the results of the standard model can be con firmed for a larger community, as shown in Figs. A23 and A24.

![](/api/attachments/J59YZTSA/fulltext/images/f4f9edecdc8aaab973114acfa4fd9e2981d75ac13802b569547f3a7220d25eb9.jpg)  
Fig. A22. Five Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

![](/api/attachments/J59YZTSA/fulltext/images/15d13e840b14444c760fcf5c5df00f8f69356ea13e52e038aaf80c34f12824d0.jpg)  
Fig. A23. Ten aggressors. Average opinion of the community over time. Dashed lines report the range of one standard deviation. The grey area refers to the number of messages per round (rescaled by the right axis).

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online commu nities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

![](/api/attachments/J59YZTSA/fulltext/images/7623effd8378aa3d165fa1b17216026a824d837ccbfe7d1e96635d4d8e60a44b.jpg)  
Fig. A24. Ten Aggressors. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

![](/api/attachments/J59YZTSA/fulltext/images/b78cb8e9e10ce53b63d60329896784c33e76efa7230ab2cc49a9f72f336a408d.jpg)  
Fig. A25. High prior opinion of the community. Influence of the conflict management style on the average opinion of the community in the last round of each repetition.

## A.3.6. Prior opinion of the community

Finally as shown in Fig. A25, the effect of the moderator’s conflict management style becomes very small when the prior opinion of a large community is very high. Therefore, we can again confirm our original results that a high assertiveness maximizes the influence of the moderator in this situation.

## References

Ahluwalia, R., 2000. Examination of psychological processes underlying resistance to persuasion. J. Consum. Res. 27, 217–232

Anagnostopoulos, A., Kumar, R., Mahdian, M., 2008. Influence and Correlation in Social Networks, in: KDD’08. Las Vegas.

Asch, S.E., 1955. Opinions and Social Pressure. Sci. Am. 193, 31–35

Aubert, V., 1963. Competition and dissensus: two types of conflict and of conflict resolution. J. Conflict Resolut. 1, 26–42.

Awad, N., Etizon, H., 2007. Stay out of my forum! evaluating firm involvement in online ratings communities, in: Proceedings of the Annual Hawaii International Conference on System Sciences, Waikoloa, HI. pp. 153c–153c.

Axelrod, R., 1997. The Complexity of Cooperation: Agent-Based Models of Competitition and Collaboration. Princeton Univesity Press, Princeton, NI

Bagozzi, R.P., Dholakia, U.M., 2002. Intentional social action in virtual communities. J. Interact. Mark. 16, 2–21.

Banerjee, A.V., 1992. A simple model of herd behavior. Q. J. Econ. 107, 797–817.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

Banerjee, A.V., 1993. The economics of rumours. Econ. Stud. 60, 309–327.

Barabasi, A., Albert, R., 1999. Emergence of scaling in random networks. Science 286, 509–512.

Batra, R., Ahuvia, A., Bagozzi, R.P., 2012. Brand love. J. Mark. 76, 1–16.

Benthaus, J., Risius, M., Beck, R., 2016. Social media management strategies for organizational impression management and their effect on public perception. J. Strateg. Inf. Syst. 25, 127–139.

Bernoff, J., Li, C., 2008. Harnessing the power of the oh so social web. MIT Sloan Manag. Rev. 49, 35–42.

Berthon, P., Pitt, L.F., Campbell, C., 2009. Does brand meaning exist in similarity or singularity? J. Bus. Res. 62, 356–361.

Berthon, P., Pitt, L.F., Campell, C., 2008. When customers create the ad. Calif. Manage. Rev. 50, 6–30.

Bhattacharya, C.B., Sen, S., 2004. Doing better at doing good: when, why, and how consumers respond to corporate social initiatives. Calif. Manage. Rev. 47, 9–24.

Bickart, B., Schindler, R.M., 2001. Internet forums as influential sources of consumer information. J. Interact. Mark. 15, 31–40.

Bikhchandani, S., Hirshleifer, D., Welch, W., 1998. Learning from the behavior of others: conformity, fads, and informational cascades. Econ. Perspect. 12, 151–170.

Blake, R.R., Mouton, J.S., 1964. The Managerial Grid. Gulf, Houston, TX.

Blodgett, J., Granbois, D., Walters, R., 1993. The effects of perceived justice on complainants’ negative word-of-mouth behavior and repatronage intentions. J. Retail. 69, 399–428.

Bonabeau, E., 2002. Agent-based modeling: methods and techniques for simulating human systems. Proc. Natl. Acad. Sci. 99, 7280–7287.

Boudreau, K.J., Lakhani, K.R., 2009. How to manage outside innovation. MIT Sloan Manag. Rev. 50, 69–76.

Breithut, J., 2011. Pril-Wettbewerb Endet Im PR-Debakel [WWW Document]. Spiegel Online <http://www.spiegel.de/netzwelt/web/virale-werbefallen-prilschmeckt-nach-haehnchen-a-756532.html> (accessed 4.12.11).

Brown, J., Broderick Amanda, J., Lee, N., 2007. Word of mouth communication within online communities: conceptualizing the online social network. J. Interact. Mark. 21, 2–20.

Burton, R.M., Obel, B., 2004. Strategic Organizational Diagnosis and Design – The Dynamics of Fit With OrgCon Software. Kluwer Academics, Boston, MA.

Butler, B., 2001. Membership size, communication activity and sustainability: the internal dynamics of networked social structures. Inf. Syst. Res. 12, 346– 362.

Butler, B.S., Wang, X., 2012. The cross-purposes of cross-posting: boundary reshaping behavior in online discussion communities. Inf. Syst. Res. 23, 993– 1010.

Chang, H.H., Tsai, Y.C., Wong, K.H., Wang, J.W., Cho, F.J., 2015. The effects of response strategies and severity of failure on consumer attribution with regard to negative word-of-mouth. Decis. Support Syst. 71, 48–61.

Chen, Y., Wang, Q., Xie, J., 2011. Online social interactions: a natural experiment on word of mouth versus observational learning. J. Mark. Res. 48, 238–254.

Coombs, W.T., 1998. An analytic framework for crisis situations: better responses from a better understanding of the situation. J. Public Res. 10, 177–191

Coombs, W.T., 2011. Ongoing Crisis Communication: Planning, Managing, and Responding. Sage, Thousand Oaks, CA

Coombs, W.T., Holladay, S.J., 2008, Comparing apology to equivalent crisis response strategies: clarifying apology's role and value in crisis communication. Public Relat. Rev. 34, 252–257.

Cucco, R., Dalli, D., 2008. 500 Wants You. Un caso di convergenza tra retro-marketing, cooperative innovation e community management. Econ. e Manag. 2, 53–72.

Dahlander, L., Magnusson, M.G., 2005. Relationships between open source software companies and communities: observations from Nordic firms. Res. Policy 34, 481–493.

Dal Fiore, F., 2007. Communities versus networks: the implications on innovation and social change. Am. Behav. Sci. 50, 857–866

Dalli, D., Corciolani, M., 2008. Collective forms of resistance: the transformative power of moderate communities. Int. J. Mark. Res. 50, 757–775.

De Moor, A., Wagenvoort, J., 2004. Conflict management in an online gaming community. In: Proc. of the Community Informatics Research Network Conference. Prato, Italy, pp. 1–21.

Deighton, J., Kornfeld, L., 2010. United Breaks Guitars. Harvard Business School Case 510-057, January 2010. (Revised August 2011.).

Delre, S.A., Jager, W., Bijmolt, T.H.A., Janssen, M.A., 2007. Targeting and timing promotional activities: an agent-based model for the take-off of new products 60, 826–835.

Delre, S.A., Jager, W., Bijmolt, T.H.A., Janssen, M.A., 2010. The effects of social influences and network topology on innovation diffusion. J. Prod. Innov. Manage. 27, 267–282.

Di Gangi, P.M., Wasko, M., 2009. Steal my idea! Organizational adoption of user innovations from a user innovation community: a case study of Del IdeaStorm. Decis. Support Syst. 48, 303–312.

Di Gangi, P.M., Wasko, M.M., Hooker, R.E., 2010. Getting customers’ ideas to work for you: learning from dell how to succeed with onlineine user innovation communities. MIS Q. 9, 213–228.

Fayard, A., DeSanctis, G., Roach, M., 2004. Language games in online forums. In: Weaver, K.M. (Ed.), 64th Annual Meeting of the Academy of Management. Academy of Management, Biracliff Manor, NY.

Fournier, S., 1998. Consumers and their brands: developing relationship theory in consumer research. J. Consum. Res. 24, 343–373.

Franke, N., Keinz, P., Klausberger, K., 2012. ‘‘Does This Sound Like a Fair Deal?”: Antecedents and consequences of fairness expectations in the individual’s decision to participate in firm innovation. Organ. Sci. 25, 1495–1516.

Frickel, C., 2011. Facebook: Aufstand gegen Pril-Wettbewerb [WWW Document] URL <http://www.focus.de/digital/internet/facebook/facebook-aufstandgegen-pril-wettbewerb\_aid\_628554.html> (accessed 5.19.11).

Füller, J., 2010. Refining virtual co-creation from a consumer perspective. Calif. Manage. Rev. 52, 98–122.

Füller, I.. Hutter. K., Hautz, I.. Matzler, K., 2014. User roles and contributions in innovation-contest communities, I. Manag, Inf. Syst, 31, 273–307.

Füller. I. Mühlbacher, H., Matzler. K., Jawecki. G., 2010. Consumer empowerment through internet-based co-creation, I. Manag, Inf. Syst, 26. 71–102

Funke. T., 2012. Konflikte Zwischen Herstellern Und User-Communities: Ein Agentenbasiertes Modell, Disseration, Vienna University of Economic and Business.

Gamson, W.A., 1992. Talking Politics. Cambridge University Press, Cambridge.

Garg, R., Smith, M., Telang, R., 2011. Measuring information diffusion in an online community. J. Manag. Inf. Syst. 28, 11–38.

Gebauer, I., Füller, I., Pezzei, R., 2012, The dark and the bright side of co-creation: triggers of member behavior in online innovation communities. I. Bus. Res. 66, 1516–1527.

Gladwell, M., 2002. The Tipping Point: How Little Things Can Make a Big Difference. Little Brown and Company, London, UK.

Goh, K.-Y., Heng, C.-S., Lin, Z., 2013. Social media brand community and consumer behavior: quantifying the relative impact of user- and marketergenerated content. Inf. Syst. Res. 24, 88–107.

Goldenberg, B.L., Muller, E., 2001. Talk of the network: a complex systems look at the underlying process of word-of-mouth. Mark. Lett. 12, 211–223.

Gonzales-Herrero, A., Smith, S., 2008. Crisis communications management on the web: How Internet-based technologies are changing the way public relations professionals handlebusiness crises. J. Contingencies Cris. Manag. 16, 143–163.

Granovetter, M., 1978. Threshold models of collective behavior. Am. J. Sociol. 83, 1420–1443.

Grégoire, Y., Fisher, R.J., 2008. Customer betrayal and retaliation: when your best customers become your worst enemies. J. Acad. Mark. Sci. 36, 247–261.

Guille, A., Hacid, H., Favre, C., Zighed, D.A., 2013. Information diffusion in online social networks: a survey. SIGMOD Rec. 42, 17–28.

Hautz, J., Füller, J., Hutter, K., Thürridl, C., 2014. Let users generated your video ads? The impact of video source and quality on consumers’ perceptions and intended behaviors. L Interact, Mark 28, 1-15

He, X., Song, G., Chen, W., Jiang, Q., 2012. Influence blocking maximization in social networks under the competitive linear threshold model. In: Ghosh, J., Liu, H., Davidson, I., Domeniconi, C., Kamath, C. (Eds.), 12th SIAM International Conference on Data Mining. Society for Industrial and Applied Mathematics, Anaheim, CA, pp. 463–474.

Henning-Thurau, T., Gwinner, K.P., Walsh, G., Gremler, D.D., 2004. Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate themselves on the Internet? J. Interact. Mark. 18, 38–52.

Hinz, O., Spann, M., 2008. The impact of information diffusion on bidding behavior in secret reserve price auctions. Inf. Syst. Res. 19, 351–368

Hirschman, A.O., 1994. Social conflicts as pillars of democratic market society. Polit. Theory 22, 203–218.

Hovland, C.I., Irving, J.L., Kelley, H.H., 1953. Communication and Persuasion: Psychological Studies of Opinion Change. Yale University Press, Haven, CT.

Hovland, C.I., Weiss, W., 1951. The influence of source credibility on communication effectness. Public Opin. Q. 15, 635–650

Huffaker, D., 2010. Dimensions of leadership and social influence in online communities. Hum. Commun. Res. 36, 593–617.

Husemann, K.C., Ladstetter, F., Luedicke, M.K., 2015. Conflict culture and conflict management in consumption communities. Psychol. Mark. 32, 265–284.

Hutter, K., Füller, J., Hautz, J., Thürridl, C., 2014. Don’t mess with the crowd! The emergence and management of crowdsourcing disasters. in: Proceedings of the Academy of Management Meeting 2014, Orlando, FL, 15432.

Hutter, K., Hautz, J., Füller, J., Mueller, J., Matzler, K., 2011. Communitition: the tension between competition and collaboration in community-based design contests. Creat. Innov. Manag. 20, 3–21.

Ind, N., Iglesias, O., Schultz, M., 2013. Building Brands Together: Emergence and Outcomes of Co-Creation. Calif. Manage. Rev. 55, 5–26.

Ishi, K., 2010. Conflict management in online relationships. Cyberpsychology Behav. Soc. Netw. 13, 365–370.

Iyengar, R., Van den Bulte, C., Valente, T.W., 2011. Opinion leadership and social contagion in new product diffusion. Mark. Sci. 30, 195–212.

Jager, W., Popping, H., van de Sande, H., 2009. Clustering and fighting in two-party crowds: aimulating the approach – avoidance conflict. J. Artif. Socities Soc. Simul. 4.

Jin, Y., Liu, B.F., 2010. The blog-mediated crisis communication model: recommendations for responding to influential external blogs. J. Public Relations Res. 22, 429–455

Jin, Y., Liu, B.F., Austin, L.L., 2014. Examining the role of social media in effective crisis management: the effects of crisis origin, information form, and source on publics’ crisis responses. Communic. Res. 41, 74–94.

Johnson, T.I., Kave. B.K., 2004. Wag the blog: how reliance on traditional media and the internet influence credibility perceptions of weblogs among blog users. I. Mass Commun, 0. 81, 622–642.

Jones, Q., Ravid, G., Rafaeli, S., 2004. Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration. Inf. Syst. Res. 15, 194–210.

Kaiser, C., Kröckel, J., Bodendorf, F., 2013. Simulating the spread of opinions in online social networks when targeting opinion leaders. Inf. Syst. E-bus. Manag. 11, 597–621.

Kaiser, C.. Schlick, S., Bodendorf, F.. 2011, Warning system for online market research - identifving critical situations in online opinion formation Knowledge-Based Syst. 24, 824–836.

Katz, E., Lazarsfeld, P., 1955. Personal Influence: The Part Played by People in the Flow of Mass Communications. Free Press, Glencoe, IL.

Kempe, D., Kleinberg, J., Tardos, É., 2003. Maximizing the spread of influence through a social network. In: Getoor, L., Senator, T.E., Domingos, P., Faloutsos, C. (Eds.), Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York, NY, pp. 137–146.

Kozinets, R.V., 1999. E-Tribalized Marketing?: The strategic implications of virtual communities of consumption. Eur. Manag. J. 17, 252–264

Kriesberg, L., 1973. The Sociology of Social Conflicts. Prentice Hall, Englewood Cliffs, New Jersey.

Kriesberg, L., 2007. Constructive Conflicts: From Escalation to Resolution. Lanham, Rowman & Littlefield, Lanham, MD

Lazar, J., Preece, J., 2002. Online Communities: Usability, Sociability and Users’ Requirements. Cogn. Digit. World. Mahwah, NJ Lawrence Erlbaum Assoc., pp. 127–151.

Lazer, D., Friedman, A., 2007. The network structure of exploration and exploitation. Adm. Sci. Q. 52, 667–694

Lee, C.H., Cranage, D.A., 2014. Toward understanding consumer processing of negative online word-of-mouth communication: the roles of opinion consensus and organizational response strategies. J. Hosp. Tour. Res. 38, 330–360.

Lee, Y.-J., Hosanagar, K., Tan, Y., 2015. Do I follow my friends or the crowd? Information cascades in online movie ratings do. Manage. Sci. 61, 2241–2258

Lee, Y.-L., Song, S., 2010. An empirical investigation of electronic word-of-mouth: informational motive and corporate response strategy. Comput. Hum. Behav. 26 1073-1080

Liu, J., Cao, Y., Lin, C.-Y., Huang, Y., Zhou, M., 2007. Low-quality product review detection in opinion summarization. In: Joint Conf. Empirical Methods in NLP and Comput. NLP (Association for Computational Linguistics), pp. 334–342.

Lu, Y., Jerath, K., Singh, P.V., 2013. The emergence of opinion leaders in a networked online community: a dyadic model with time dynamics and a heuristic for fast estimation. Manage, Sci, 59 1783–1799

Lyons, B., Henderson, K., 2005. Opinion leadership in a computer-mediated environment. J. Consum. Behav. 4, 319–329.

Mack, R.W., Snyder, R.C., 1957. The analysis of social conflict— toward an overview and synthesis. Confl. Resolut. 1, 212–248.

Miller, K.D., Fabian, F., Lin, S.-J., 2009. Strategies for online communities. Strateg. Manag. J. 30, 305–322.

Moe, W.W., Schweidel, D.A., 2012. Online product opinions: incidence, evaluation, and evolution. Mark. Sci. 31, 372–386

Moleskine, 2011. Facebook Entry by Moleskine on October 21, 2011 [WWW Document] URL <http://www.facebook.com/moleskine> (accessed 11.5.11).

Montoya-Weiss, M.M., Massey, A.P., Song, M., 2001. Getting it together: temporal coordination and conflict management in virtual communities. Acad. Manag. J. 44, 1251–1262.

Nonnecke, B., Preece, J., 2000. Lurker demographics: counting the silent, in: Machinery, A. of C. (Ed.), SIGCHI Conf Human Factors Comput. Systems. ACM Press, New York, pp. 73–80.

Nonnecke, B., Preece, J., 2001. Why lurkers lurk. In: AMCIS 2001 Proceedings. Boston, MA, pp. 294.

Oh. W., Jeon. S., 2007, Membership herding and network stability in the open source community: the Ising perspective, Manage, Sci. 53. 1086–1101.

Otterbacher, J., 2009. Helpfulness” in online communities: a measure of message quality. In: SIGCHI Conf. Human Factor Comput. Systems. ACM, New York, pp. 955–964.

Pfeffer, J., Zorbach, T., Carley, K.M., 2014. Understanding online firestorms: negative word-of-mouth dynamics in social media networks. J. Mark. Commun. 20, 117–128.

Porter, C.E., 2004. A typology of virtual communities: a multi-disciplinary foundation for future research. J. Comput. Commun. 10

Porter, C.E., Devaraj, S., Sun, D., 2013. A test of two models of value creation in virtual communities. J. Manag. Inf. Syst. 30, 261–292

Preece, J., 2000. Online Communities - Designing Usability, Supporting Sociability. John Wiley & Sons, Chichester.

Preece, J., 2002. Supporting community and building social capital. Commun. ACM 45, 36–40.

Preece, J., Nonnecke, B., Andrews, D., 2004. The top 5 reasons for lurking: improving community experiences for everyone. Comput. Human Behav. 20, 201– 223.

Pril, 2011. Facebook Entry by Pril [WWW Document] URL <https://www.facebook.com/pril/posts/208826712490762> (accessed 5.17.11).

Pruitt, D.G., 1983. Strategic choice in negotiation. Am. Behav. Sci. 27, 167–194.

Putman, L.L., Poole, M.S., 1987. Conflict and Negotiation. Sage, Beverly Hills, CA.

Qi, J., Qu, Q., Tan, Y., Mu, J., 2014. Modeling MGC strategies under extreme negative UGC. J. Electron. Commer. Res. 15, 150–161.

Rahim, M.A., 1983. A measure of styles of handling interpersonal conflict. Acad. Manag. J. 26, 368–376.

Rahim, M.A., 2002. Toward a theory of managing organizational conflict. Int. J. Confl. Manag. 13, 206–235

Rabim. M A. Antonioni, D. Psenicka C. 2001. A structural equations model of leader power subordinates' styles of handling conflict, and job performance Int. J. Confl. Mange. 12, 191–211.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online communities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002

Ren, Y., Kraut, R.E., 2014. Agent-based modeling to inform online community design: impact of topical breadth, message volume, and discussion moderation on member commitment and contribution. Human-Comput. Interact. 29, 351–389.

Rheingold, H., 1994. A slice of life in my virtual community. In: Harasim, L.M. (Ed.), Global Networks. Computers and International Communication. MIT Press, Cambridge, MA, pp. 57–80.

Ridings, C.M., Gefen, D., 2002. Bay Arinze Some antecedents and effects of trust in virtual communities. J. Strateg. Inf. Syst. 11, 271–295.

Salt, S., 2011. How to Lose Fans & Annoy Advocates: The Moleskine Story [WWW Document]. Inc Slingers <http://www.theincslingers.com/2011/10/howto-lose-fans-annoy-advocates-the-moleskine-story/> (accessed 11.15.11).

Sawall, A., 2011. Henkel vergrault seine Facebook-Freunde. Zeit-Online. http://www.zeit.de/digital/internet/2011-05/pril-facebook-pr.

Schweitzer, F., Garcia, D., 2010. An agent-based model of collectivr emotions in online communities. Eur. Phys. J. B - Condens. Matter Complex Syst. 77. 553– 545.

Sen, S., Lerman, D., 2007. Why are you telling me this? An examination into negative consumer reviews on the web. J. Interact. Mark. 21, 76–94.

Smith, D.S., Menon, S., Sivakumar, K., 2005. Online, peer and editorial recommendations, trust and choice in virtual markets. J. Interact. Mark. 19, 15–37.

Snow, D.A., Benford, R.D., 1992. Master frames and cycles of protest. In: Morris, A.D., Mc Clurg Mueller, C. (Eds.), In Frontiers of Social Movement. Yale Univeristy Press, New Haven, CT, pp. 133–155.

Squazzoni, F., 2009. The impact of agent-based models in the social sciences after 15 years of incursions. Sociol. Methodol. 2, 1–23.

Stephen, A., Dover, Y., Muchnik, L., Goldenberg, J., 2012. The Effects of Transmitter Activity and Connectivity on Information Dissemination Over Online Social Networks. Pittsburgh.

Stich, L., Golla, G., Nanopoulos, A., 2014. Modelling the spread of negative word-of-mouth in online social networks. J. Decis. Syst. 23, 203–221.

Sun, T., Youn, S., Wu, G., Kuntaraporn, M., 2006. Online word-of-mouth (or mouse): an exploration of its antecedents and consequences. J. Comput. Mediat. Commun. 11, 1104–1127.

Susarla, A., Oh, J.-H., Tan, Y., 2012. Social networks and the diffusion of user-generated content: evidence from youtube. Inf. Syst. Res. 23, 23–41.

Terwiesch, C., Xu, Y., 2008. Innovation contests, open innovation, and multiagent problem solving. Manage. Sci. 49, 1529–1543

The Economist, 2009. Did Dave Carroll lose United Airlines \$180m? Econ. http://www.economist.com/blogs/gulliver/2009/07/did\_dave\_carroll\_cost\_ united1.

Thomas, J.B., Peters, C.O., Howell, E.G., Robbins, K., 2012. Social media and negative word of mouth: strategies for handing unexpecting comments. Atl. Mark. J.1.87-108.

Thomas, K.W., 1976. Conflict and conflict management. In: Dunnette, M.D. (Ed.), Handbook in Industrial and Organizational Psychology. Rand McNally, Chicago, pp. 889–935

Thomas, K.W., Kilmann, R., 1978. Comparison of four instruments measuring conflict behavior. Psychol. Rep. 42, 1139–1145.

Tjosvold, D., 1991. The Conflict-Positive Organization: Stimulate Diversity and Create Unity. Addison-Wesley Pub Reading, MA

Tybout, A.M., Roehm, M., 2009. Let the response fit the scandal. Harv. Bus. Rev. 86, 82–89.

Ulmer. R.R., 2001, Effective crisis management through established stakeholder relationships: Malden mills as a case study, Manag, Commun, O. 14. 590– 615.

van Noort, G., Willemsen, L.M., 2012. Online damage control: the effects of proactive versus reactive webcare interventions in consumer-generated and brand-generated platforms. J. Interact. Mark. 26, 131–140.

Wall, J.A., Callister, R.R., 1995. Conflict and its management. J. Manage. 21, 515–558.

Ward, J.C., Ostrom, A.L., 2006. Complaining to the masses: the role of protest framing in customer-created complaint web sites. J. Consum. Res. 33, 220–230.

Wasko, M M. Farai S. 2005, Why should i share?: Examining social capital and knowledge contribution in electronic networks of practice, MIS O. 29. 35- 57.

Watts, D.J., Dodds, P.S., 2007. Influentials, networks, and public opinion formation. J. Consum. Res. 34, 441–458

Wellman, B., Salaff, J., Dimitrova, D., Garton, L., Gulia, M., Haythornthwaire, C., 1996. Computer networks a social networks: collaborative work, telework, and virtual community. Annu. Rev. Sociol. 22, 213–238.

Williams, R.M., 1970. Social order and social conflict. Proceedings of the American Philosophical Society 114, 217–225.

Xia, L., 2013. Effects of companies’ responses to consumer criticism in social media. Int. J. Electron. Commer. 17, 73–100

Yang, J., Leskovec, J., 2010. Modeling information diffusion in implicit networks, in: ICDM ’10 Proceedings of the 2010 IEEE International Conference on Data Mining, Sydney, Australia. pp. 599–608.

Florian Hauser is a Senior Lecturer at the Innsbruck University School of Management. Florian holds as doctoral degree in Social and Economic Sciences from the University of Innsbruck. His research interest is focused on information aggregation and diffusion, market efficiency, as well as agent-based simulations in finance, economics and management

Julia Hautz is an Assistant Professor at the Innsbruck University School of Management. Julia holds as doctoral degree in Social and Economic Sciences from the University of Innsbruck. In her research, Julia focuses on strategy and innovation. In particular, she explores corporate diversification strategies and openness of innovation and strategy processes from a social network perspective.

Katja Hutter is Professor for Marketing and Innovation at the University of Salzburg and an associate of the Crowd Innovation Lab/NASA Tournament Lab at the Harvard University. Her research topics are anchored in the fields of marketing and innovation. She is interested in incentive schemes and consumer interaction behavior in online communities to generate insights for innovation activities that resolves around customers and their needs.

Johann Füller is Professor for Innovation and Entrepreneurship at the Innsbruck University School of Management. He is Fellow at the at the Crowd Innovation Lab/NASA Tournament Lab at Harvard University and CEO of Hyve AG, an innovation and community company. In line with his research focus, he regularly gives guest lectures about co-creation, online branding, creative consumer behavior, online marketing, open innovation, and the utilization of online communities.

Please cite this article in press as: Hauser, F., et al. Firestorms: Modeling conflict diffusion and management strategies in online commu nities. J. Strateg. Inform. Syst. (2017), http://dx.doi.org/10.1016/j.jsis.2017.01.002
