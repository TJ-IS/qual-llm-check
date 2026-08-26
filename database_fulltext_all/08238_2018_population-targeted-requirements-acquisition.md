---
otero_id: 8238
otero_key: "UBMA46TG"
title: "Population targeted requirements acquisition"
authors: "Tuure Tuunanen; Ken Peffers"
year: "2018"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2018.1476015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Population targeted requirements acquisition

Tuure Tuunanen & Ken Peffers

To cite this article: Tuure Tuunanen & Ken Peffers (2018): Population targeted requirements acquisition, European Journal of Information Systems, DOI: 10.1080/0960085X.2018.1476015

To link to this article: https://doi.org/10.1080/0960085X.2018.1476015

![](/api/attachments/UBMA46TG/fulltext/images/e291f696bd707898693bf8cdc782b017631863e477ef0272a454091b8043edb6.jpg)

Published online: 04 Jun 2018.

![](/api/attachments/UBMA46TG/fulltext/images/47aae92691297bc62801487bdc3f40997d85f2957e2d41e14d39c320617c8c07.jpg)

Submit your article to this journal

![](/api/attachments/UBMA46TG/fulltext/images/0ab5341e0bd00b4727ddb094a82a7b5d658c84c38700d0d14a646d287e460332.jpg)

Article views: 10

![](/api/attachments/UBMA46TG/fulltext/images/367ccb7336db1fc86c1b1e9ac93bf44dbab2de012c223c574bde249d2f8c4cd5.jpg)

View related articles

![](/api/attachments/UBMA46TG/fulltext/images/4254d0e06cb775d5912068c1f1910b3c4162c80c6de19d62fc686a7e41a2ae29.jpg)

View Crossmark data

THEORY DEVELOPMENT

Check for updates

# Population targeted requirements acquisition

Tuure Tuunanen <sup>a</sup> and Ken Pe<sup>f</sup>ers <sup>b</sup>

<sup>a</sup>University of Jyväskylä, Faculty of Information Technology, Jyväskylä, Finland; <sup>b</sup>Lee Business School, Department of Management, Entrepreneurship, and Technology, University of Nevada Las Vegas, Las Vegas, NV, US

## ABSTRACT

We use social science theories, design science research methodology, and our experience in <sup>fi</sup>ve development projects to design principles for selecting or adapting requirements acquisition (RA) techniques for use with populations of customers and users. The information systems (IS) literature has not systematically focused on the adaption of RA techniques to particular populations. We developed a nascent design theory for RA to target speci<sup>fi</sup>c populations to de<sup>fi</sup>ne functional requirements for new IS. Five reference theories – personal construct theory, theory of disability, di<sup>f</sup>usion of innovations, social actor theory, and media richness and information synchronicity theory – support the design. The theory was evaluated iteratively with <sup>fi</sup>ve client organisations, involving more than 200 participants.

ARTICLE HISTORY

Received 3 May 2016

Revised 22 April 2018

Accepted 28 April 2018

KEYWORDS

Population; requirement

acquisition; nascent design

theory; design science

research

## 1. Introduction

Understanding and selecting the best features for new information systems (IS) (hereafter “systems”) has long been recognised as an important problem that is di<sup>fi</sup>cult for <sup>fi</sup>rms to solve (Neill & Laplante, 2003). Many important systems have been designed, implemented, and rolled out only to fail because users found that the systems did not meet their functional needs; required time-consuming, frustrating behaviour to make operable, or required awkward workarounds to complete work (Keil, Mann, & Rai, 2000).

Researchers have sought to resolve the problem of poorly understood requirements by advocating requirements acquisition (RA) from users and using elicitation techniques to help users express their needs as well as techniques to present user needs in ways that will help developers understand them (Byrd, Cossick, & Zmud, 1992). These techniques focus on de<sup>fi</sup>ning, understanding, and agreeing on the appropriate set of functionalities, features, and intended bene<sup>fi</sup>ts of new systems. IS research has persuasively shown that engagement with potential system users is important to determine the features and functionality of new systems (Tait & Vessey, 1988).

The most straightforward users with whom to engage during design activities are physically present, already engaged with the <sup>fi</sup>rm, and experienced with and interested in systems based on contemporary technology. Increasingly, however, <sup>fi</sup>rms are developing systems for which conditions for e<sup>f</sup>ective participation cannot be easily assured, even for the systems’ primary intended users. Nonetheless, these users’ satisfaction with the systems’ value, functionality, and usability will determine the ultimate success of the systems and the resulting services. For example, as systems to incorporate social media into sales and marketing activities enlarge the scope of a <sup>fi</sup>rm’s customers, they are likely to engage new, hitherto unknown customer populations. Likewise, fully digital service o<sup>f</sup>erings, such as Internetonly banking, deliver some customers who have had no prior interactions with the <sup>fi</sup>rm. These new customers may only engage with the <sup>fi</sup>rm after new applications, systems, products, and services are developed and implemented.

A useful viewpoint to de<sup>fi</sup>ne “populations” for our purpose and to help understand why populations may require particular attention for systems, applications, and services design may be found in stakeholder theory (Donaldson & Preston, 1995; Freeman, 1984). We use the term “population” here to refer to customers, potential customers, or system users whose preferences we expect to be meaningful and valuable for de<sup>fi</sup>ning systems’ functional requirements. The characteristics of such populations are inherently complex, so engaging them to accurately ascertain their needs and preferences may not be straightforward. Such populations are very diverse (Bergum & Bergum, 1981) and may often be misunderstood or mischaracterised by the observer (Enoch, Shen, Xu, Hodgkinson, & Goldman, 2006). Although systems are intended to provide value to a new population, it is not enough for designers to imagine themselves in the role of the population members and, armed with stereotypes of the population’s preferences, to storyboard themselves through the systems’ use. In doing so, they are likely to err enough to make systems’ value substantially suboptimal (Bergum & Bergum, 1981).

We address this as a design research problem: to design a theory for the e<sup>f</sup>ective use of RA techniques (1) to understand population preferences and reasoning for functionality in new systems and (2) to support the shared understanding of those preferences among downstream development participants. This research should enable e<sup>f</sup>ective population participation in RA activities, where it may not otherwise be assured. Prior literature has not systematically addressed or solved this problem.

To solve this problem, we designed <sup>fi</sup>ve principles for action for using and adapting existing techniques to enable e<sup>f</sup>ective RA activities with populations characterised by “states” that present barriers to RA. We refer to this nascent design theory (Gregor & Hevner, 2013, p. 341) as population-targeted requirements acquisition (PTRA). PTRA resulted from our e<sup>f</sup>orts over several years on projects spanning four countries, three continents, engaging <sup>fi</sup>ve client organisations, and involving more than 200 subjects. Our e<sup>f</sup>orts in these <sup>fi</sup>ve organisational cases provided us the opportunity to iteratively design for our clients, learn, and to improve solutions. An overview of the cases, which we use below in our explication of PTRA’s design, can be found in Appendix 1.

This research has been informed by design science research (DSR) guidelines (Hevner, March, & Park, 2004) and has been carried out using the design science research methodology (DSRM) (Pe<sup>f</sup>ers, Tuunanen, Rothenberger, & Chatterjee, 2007). Next, we recognise <sup>fi</sup>ve population states based on the literature and our own research. Thereafter, we propose a theoretical foundation to resolve the <sup>fi</sup>ve states and provide objectives for such work. We continue by depicting the designed solution to this problem, PTRA, and then showcase its use in <sup>fi</sup>ve studies and evaluate the use of its principles in action. We conclude by discussing the implications of our work, the study’s limitations, and future research.

## 2. RA problems from population states

Populations are often characterised as categorical groups, but this view simpli<sup>fi</sup>es reality; the categories can be disaggregated into smaller useful populations. For example, if one category is “potential customers”, not all potential customers are alike (Freeman, 1984, p. 27). Moreover, the categories consist of aggregations of a number of disparate populations in multiple dimensions, so potential Asian customers, e.g., may be disaggregated by occupation, nationality, disability, income, age, and whether they are in an urban or rural area.

Sociologists have identi<sup>fi</sup>ed states that are known to a<sup>f</sup>ect behaviour (Macionis & Gerber, 2010, pp. 59–65), to include (1) the meaning of symbols within the population); (2) symbols and language facilitating intracultural communication (Petervary, 2016); (3) values and standards leading to action, e.g., for whistleblowing behaviour (Francalanza & Buttigieg, 2016); (4) beliefs about what is true, e.g., about co-existing religious beliefs (Caxton, 2015); and (5) norms, rules, and expectations, e.g., for behaving within social systems (Willette, 2016). Macionis and Gerber (2010, pp. 59–65) found <sup>fi</sup>ve key problems that are important for population states. We adopt and adapt them here to also account for population members’ knowledge and interest in technology:

● Across populations, people <sup>fi</sup>nd it di<sup>fi</sup>cult to understand others’ preferences and reasoning because of di<sup>f</sup>erences in values, assumptions, beliefs, and mental models of how the world works (Kelly, 1955);

● The value that population members place on preferences may be a<sup>f</sup>ected by the environments in which they live and work and the roles they adopt, based on their multiple identities (Lamb & Kling, 2003; Petervary, 2016).

● Population members’ willingness and ability to participate in RA activities are a<sup>f</sup>ected by their highly varied knowledge of and attitudes towards new technologies as well as their tolerance for risk (Rogers, 1995).

● Ability limitations among population members that present barriers to their participation in RA activities may substantially a<sup>f</sup>ect their preferences for system functionality (Michailakis, 2003).

● Divergent understanding among population members and downstream participants about the meaning and value of functional preferences (Rosman, 2014) can create di<sup>fi</sup>culties in achieving a concordant understanding of them.

Next, we review how these state-speci<sup>fi</sup>c problems have been tackled in RA literature.

## 2.1. Mental models and value structures

By understanding peoples’ value structures (Robey & Azevedo, 1994), we can “penetrate the surface of the users’ requirements” and understand the users underlying values or assumptions. Tuunanen, Pe<sup>f</sup>ers, Gengler, Hui, and Virtanen (2006) proposed using values to look at requirements to better understand the mental models and value structures behind preferences and thus to better understand the drivers of system use (Tuunanen, Myers, & Cassab, 2010).

The RA literature recognises the importance of understanding underlying value structures (Chakraborty, Sarker, & Sarker, 2010; Pitts & Browne, 2007; Tuunanen & Kuo, 2015), but most of the literature still takes an instrumental view of the RA process. For example, the use-case technique provides sets of rules and notation instructions for developing design objects and how they link together and form object classes, but this does not necessarily reveal a population’s underlying mental models or value structures. Unless designers understand users’ mental models and values, they may not well incorporate functionality that supports users needs and are likely to include features that a<sup>f</sup>ect e<sup>f</sup>ectiveness negatively (Maedche, Morana, Schacht, Werth, & Krumeich, 2016).

Some RA studies attempt to model users’ value structures. One of these, repertoire grids (Davis, Fuller, Tremblay, & Berndt, 2006), also applies a cognitive mapping technique for requirements analysis (Montazemi & Conrath, 1986). With repertoire grids, cognitive mapping provides a representation of the relationships between di<sup>f</sup>erent requirements (Montazemi & Conrath, 1986). In this way, cognitive mapping models peoples’ value structures and mental models, i.e., personal constructs of the world they live in (Kelly, 1955).

## 2.2. Perception of roles and environmental impact

Contextual RA techniques include the use of ethnographic techniques and conversation analysis (Viller & Sommerville, 1999). Contextual design (Holtzblatt & Beyer, 1993) asserts that the best designs happen when the analyst is involved in collecting and interpreting customer data and can thereby understand what users need (Tuunanen, 2003). This is accomplished by observing participants in situ with the contextual inquiry technique, i.e., where the analyst observes the user as he or she completes routine tasks.

Bergman, King, and Lyytinen (2002) have argued that developers should be concerned with the larger socio-economic context in which the system will be used Similarly, social actor theory (SAT) argues that users should be re-conceptualised as a social actor who is in<sup>fl</sup>uenced by the organisational and community environment and the various roles that people assume while using systems (Lamb & Kling, 2003). Consequently, we should be aware of the situated and institutionally framed actions in which population members participate (Holmström & Sawyer, 2011).

## 2.3. Technological experience and attitude towards innovation

Technology acceptance and adoption is a major theme in the IS literature, e.g., Venkatesh, Thong, and Xu (2012). This research has studied perceived usefulness, perceived ease of use, and attitude as the antecedents of technology acceptance. Other than for testing the perceived usefulness of an RA technique, e.g., De Oliveira, Viana, Conte, Vieira, and Marczak (2013), this literature has not made a substantial contribution to the RA literature

The RA literature does recognise that levels of technological experience vary, which makes technical knowledge a key issue when considering how system functionality may impact the development project (Tiwana & Keil, 2006). However, this has not been studied further to understand how such knowledge might di<sup>f</sup>er among populations. As a result, there is little help in the literature for characterising population di<sup>f</sup>erences in terms of technology experience and attitudes towards technology. Technology experience and attitudes towards technology have been found to be two of the important di<sup>f</sup>erences between information technology (IT) professionals and users, according to Potter (2007); however, she does not provide guidance for resolving these state-related RA problems. Here, we <sup>fi</sup>nd di<sup>f</sup>usion of innovations theory helpful, especially its concepts of categories of technology adopters (Rogers, 1995).

## 2.4. Ability limitations

System design has been greatly in<sup>fl</sup>uenced by concerns for ensuring accessibility by disabled people. The user interface provided by the underlying operating system has been a focal point for these e<sup>f</sup>orts. The literature has been particularly concerned with RA for blind and visually impaired people (Kim, Smith-Jackson, & Nam, 2013). Similarly, there have been calls to study how people with needs for assistive technology should be facilitated in RA (Blackburn & Cudd, 2012) as well as for studies about how do this in practice, e.g., for physically challenged users (Moseley, 2000) or with memory constraints (Appan & Browne, 2010).

The RA literature has also addressed ability limitations, with studies about enabling RA participation for elderly persons (Sustar, Pfeil, & Zaphiris, 2008) and illiterate users (Pitula & Radhakrishnan, 2011), as well as for systems designed for use by children (Molin-Juustila, Kinnula, Iivari, Kuure, & Halkola, 2015). In each of these examples, the ability limitations di<sup>f</sup>er greatly in nature, e.g., physical or cognitive, and severity, e.g., the average limitations of the elderly or the young vs. loss of an essential life functionality. Literature has also observed that, as populations such as the elderly are less able to participate e<sup>f</sup>ectively in RA activities, either as customer participants or developers, this tends to reinforce barriers to participation (Schloegel, Stegmann, Maedche, & Van Dick, 2016).

The systems theory of disability provides a very general view of disabilities (Michailakis, 2003). The concept of a disability is only meaningful within the context of a social system that is a<sup>f</sup>ected by abilities, according to this theory. For this reason, this theory promises to be useful for use in designing RA techniques.

## 2.5. Divergent views about preferences

Populations include di<sup>f</sup>erent groups of people, and their viewpoints about the meaning and value of system preferences vary. Groups have their own view preferences (Darke & Shanks, 1996); sharing them creates RA problems (Charaf, Rosenkranz, & Holten, 2013; Rosenkranz, Vranesic, & Holten, 2014). This is seen in the literature as a gap between users and other actors in the system development process, e.g., managers and designers (Grudin, 1991).

To Mathiassen, Saarinen, Tuunanen, and Rossi (2007), this is a requirements speci<sup>fi</sup>cation problem. They suggested several techniques to resolve it, such as data <sup>fl</sup>ow diagramming. They argued that highly complex requirements are di<sup>fi</sup>cult to understand, specify, and communicate; therefore, groups of people have di<sup>f</sup>erent understandings of the meaning and value of preferences. Consequently, achieving concordant understanding among the parties to system development about what people want, why they want it, and how much value they place on preferences may not straightforward (Rosenkranz, Charaf, & Holten, 2013).

Researchers have proposed di<sup>f</sup>erent ways to resolve this problem. Pe<sup>f</sup>ers and Tuunanen (2005) recommend addressing this problem by applying information theory (Dennis, Fuller, & Valacich, 2008) to determine when to use speci<sup>fi</sup>c communication techniques to achieve conveyance or convergence needs. Other researchers have suggested similar solutions. Calefato, Damian, and Lanubile (2007) applied information theory to enable synchronous text-based communication for distributed RA workshops. Wing, Andrew, and Petkov (2015) combined several techniques to achieve rich participation and improve requirements understanding among clients. We observed this discussion and used media richness and information synchronicity in our programme to choose communication techniques for our projects.

## 3. Associating population states with theories and objectives

Five theories helped shape our understanding of di<sup>f</sup>erences across populations states that may a<sup>f</sup>ect members’ system preferences, perceptions about value, and interest and ability to participate in RA: (1) personal construct theory (PCT), (2) SAT, (3) di<sup>f</sup>usion of innovations theory, (4) systems theory of disability, and (5) media richness and information synchronicity. Our identi<sup>fi</sup>cation of these theories was purposeful. While working with population samples in each study, we reached out to identify theories that we could associate with understanding the population state and that could potentially contribute design theory for resolving the speci<sup>fi</sup>c RA problems.

Our selection of applicable theory might best be described in reference to Gregory and Muntermann’s (2014) heuristic theorising framework, which suggests that e<sup>f</sup>ective problem-solving involves repeatedly iterating between heuristics for structuring problems and heuristics for designing solutions. We iterated between problem structuring and solution design in each case and sometimes between cases. To structure the problem in each study, we used decomposition heuristics, class-identi<sup>fi</sup>cation heuristics, or both to understand the problem (or part of it) as an instance of a problem class. To design a solution, we employed analogical design to locate a theory that <sup>fi</sup>t the identi<sup>fi</sup>ed problem or sub-problem and sought to apply techniques associated with that theory to a problem solution (Gregory & Muntermann, 2014).

In what follows, we review each of the theories and argue for their applicability and we de<sup>fi</sup>ne an objective as the focus of RA performance e<sup>f</sup>orts with each state. We argue that the two concepts are similar, with objective implying an ex ante desired performance and proposition implying an ex post claim. The review is summarised in Table 1.

Associating population states with theories and objectives.

<table><tr><td>State</td><td>Applicable theory</td><td>Objective</td></tr><tr><td>Beliefs and mental models affect functional preferences and value (BMM)</td><td>Personal construct theory (Kelly, 1955)</td><td>For managers, designers, and others to understand user preferences and reasoning</td></tr><tr><td>Identities, environments, and affiliations affect preferences (IE&amp;A)</td><td>Social actor theory (Lamb, 2006; Lamb &amp; Kling, 2003)</td><td>For managers, designers, and others to understand discrete preferences, values, and reasoning for functionality across populations</td></tr><tr><td>Motivation and experience affect ability to imagine new technology benefits (IMAGINE)</td><td>Diffusion of innovations theory (Rogers, 1976, Rogers, 1995; Von Hippel, 1986)</td><td>For a population to participate effectively to enable the collection of preferences for functionality based on new technology</td></tr><tr><td>Abilities affect functional preferences and participation costs (ABIL)</td><td>Systems theory of disability (Michailakis, 2003; Murugami, 2009)</td><td>For managers and designers to accommodate barriers and costs for effective participation by populations with disabilities</td></tr><tr><td>Variance in understanding of the value of functionality across populations (CONC)</td><td>Media richness and information synchronicity (Daft &amp; Lengel, 1986; Dennis et al., 2008)</td><td>For managers, designers, and others to achieve concordance on the meaning and value of functionality from hitherto unexperienced technology</td></tr></table>

## 3.1. Beliefs and mental models a<sup>f</sup>ect functional preferences and value

PCT was developed by practising school psychologist George Kelly (1955), as he modelled how patients saw relationships among states of the universe, the consequences of those states, and the impact of those consequences on individual values, to better understand how they and their teachers understood the world di<sup>f</sup>erently. These relationships, or personal constructs (Pervin, 1993, p. 228), result from our individual observations and interpretations of events (Kelly, 1955). Each of us has individual multidimensional models (constructs) that describe the features and behaviour of objects and events, their resulting consequences, and their e<sup>f</sup>ects on our values. According to PCT, individual observers note that a system has certain features; they use their own constructs to conclude that these features have expected consequences, which, in turn, pertain to values.

PCT-based data-gathering techniques are used to acquire information about people’s knowledge structures. One pertinent technique, “laddering” (Reynolds & Gutman, 1988), models consumer value structures related to product and feature preferences. An analyst uses structured interviewing to collect chains of features, reasons, and values from a number of participants. The chains are aggregated across participants to produce network models for how participants interrelate the constructs (Gengler & Reynolds, 1995).

It may be critically important for managers, designers, and developers to understand user preferences and the reasons for them, particularly when targeted users view the world di<sup>f</sup>erently. A population is a cluster of individuals who may be similar along one or more dimensions of beliefs and mental models (BMM), i.e., personal constructs. PCT supports techniques for understanding population’s constructs.

## 3.1.1. Objective for the BMM state

When a population holds beliefs, mental models, or values that materially di<sup>f</sup>er from those of managers, designers, and other project participants, understanding requires that the developers be provided with representations that incorporate preferences, reasoning, and values to enable consistent understanding among development participants.

## 3.2. Identities, environments, and a<sup>fi</sup>liations a<sup>f</sup>ect preferences

SAT views the system user’s characteristics and behaviour in the context of roles de<sup>fi</sup>ned by social systems (Lamb & Kling, 2003). Three dimensions of these roles – identities, a<sup>fi</sup>liations, and environments (IE&A) – are elaborated by the characteristics or behaviours of contextually involved individuals (Lamb & Kling, 2003).

Identities are the acknowledged presentations of the “self” and the recognised pro<sup>fi</sup>les of organisation members as individuals and collective entities. Social actors use systems to construct these identities and control perceptions of them. The a<sup>fi</sup>liations dimension depicts the networked nature of current work habits; we are connected to di<sup>f</sup>erent individuals and organisations in our daily life in di<sup>f</sup>erent layers of involvement (e.g., organisational, national, and international) with the surrounding society. Organisational networks shape social actor networks that are dynamic in nature, a<sup>f</sup>ect the way information is communicated, and in turn have an impact on the needed resources, such as capital and labour (Lamb, 2006; Lamb & Kling, 2003). Finally, environments portray the surrounding world of the community and the organisation, where social actors in<sup>fl</sup>uence each other in terms of regulations, practices, associations, and locations, thereby a<sup>f</sup>ecting the environmental reality. Organisational environments exercise technical and institutional pressure on other organisations and individuals, the dynamics of which vary by business domain.

Individuals acting within what they see as their roles within the scope of one or more of their IE&A may be expected to adopt appropriate beliefs and values. SAT may suggest useful population disaggregations to better understand preferences and reasoning stemming from the subtleties of world views based on di<sup>f</sup>ering IE&A and how they a<sup>f</sup>ect user preferences.

## 3.2.1. Objective for the IE&A state

When beliefs, values, and preferences seem to di<sup>f</sup>er materially within a population by IE&A, RA e<sup>f</sup>orts should attend to understanding how the preferences of a subpopulation’s members are related to their various roles.

## 3.3. Motivation and experience a<sup>f</sup>ect ability to imagine a new technology’s bene<sup>fi</sup>ts

Di<sup>f</sup>usion of innovations theory represents and predicts patterns of innovation adoption by populations of potential users (Rogers, 1976, 1995). A key element of this theory is the consensus around a basic idea of an S-shaped cumulative adoption curve that is a<sup>f</sup>ected by in<sup>fl</sup>uence from both within and external to the population. Among adoption researchers, interest has focused on the small group of people who tend to adopt innovations very early in the curve (Von Hippel, 1986), compared with the remainder of the population. At any time, current innovation adoptions by these “lead users” and the robustness thereof tend to predict adoptions by a larger mass market in future periods, particularly the level of eventual adoption and the pace of adoption (Pe<sup>f</sup>ers & Dos Santos, 1996).

These lead users tend to be more familiar with innovations that lie in the future for most population members; their experience with leading-edge technologies positively a<sup>f</sup>ects their attitudes towards previously unexperienced technologies; and they tend to be more able to think creatively about the potential of new technologies. They can be used as a need- or preference-forecasting laboratory (Von Hippel, 1986). The lead user concept has found appeal among academic and business researchers because using lead users has been shown to lead to higher performance in product development and marketing (Lilien, Morrison, Searls, Sonnack, & Von Hippel, 2002).

When population members are ill-equipped or unmotivated to participate because they lack experience with the product type, the technology, the organisation, or its products (IMAGINE), the lead user concept suggests a route towards e<sup>f</sup>ective RA e<sup>f</sup>orts.

## 3.3.1. Objective for the IMAGINE state

When population members have insu<sup>fi</sup>cient motivation or competence to participate e<sup>f</sup>ectively or when they have low-risk tolerance and negative attitudes towards new technologies, managers and designers should ensure e<sup>f</sup>ective population participation by engaging members from population segments that are most able to participate e<sup>f</sup>ectively.

## 3.4. Abilities a<sup>f</sup>ect functional preferences and participation costs

Disability theory opens the door to viewing participation abilities broadly, so that ability or disability is no longer a rare malady that a<sup>f</sup>ects just a small niche population. Most of us are or will someday face barriers to participation at some dimension and in some social systems. For example, a professor develops cataracts, which a<sup>f</sup>ects his ability to drive to teach night classes, or a student copes with a learning disability by adopting behaviours that enable her to succeed, albeit at substantial costs in time and e<sup>f</sup>ort. Social systems create the need for de<sup>fi</sup>nitions that serve to discriminate among people as being well or ill, allowed or not allowed to drive, and able or unable to work. Each social system only needs to be concerned with dimensions of performance that a<sup>f</sup>ect participation within that system. Outside of social systems with system-relevant abilities, the concept of ability or lack thereof has relatively little meaning. A disability is therefore de<sup>fi</sup>ned by the social system in which the de<sup>fi</sup>nition is required (Michailakis, 2003).

It is also important that people who participate or might participate in social systems, but with constrained abilities, adopt their own values. Because abilities, by de<sup>fi</sup>nition, a<sup>f</sup>ect economic and practical aspects of life, e.g., the time required to travel to a new place (Murugami, 2009), they necessarily a<sup>f</sup>ect the values attached to the consequences of system functionality. Population members with limited abilities have substantially di<sup>f</sup>erent values with respect to time and attention constraints as well as to the relative importance of system-related outcomes than do others: it is axiomatic that, when time and attention are dear, one must minimise participation in activities that are less critical to one’s happiness and well-being. Finally, many, if not most, people have or will experience some limitations in their ability (ABIL).

## 3.4.1. Objective for the ABIL state

When the ability of population members to participate in RA activities is limited, managers and designers should accommodate technical and social barriers as well as barriers that result from di<sup>f</sup>ering participation costs to e<sup>f</sup>ectively include these population members in RA activities and thereby understand their preferences and values.

## 3.5. Variance in understanding of the value of functionality across populations

Researchers seeking to facilitate communication developed information theory, in which media is characterised by its richness and information synchronicity (Daft & Lengel, 1986; Dennis et al., 2008). Media richness refers to the media’s capability to carry complex, multidimensional information and cues that help message recipients to better understand the intended message (Daft & Lengel, 1986). Information richness helps managers and designers to manage uncertainty and equivocality in the decision environment.

“Media synchronicity” is an extension of media richness theory based on the need for conveyance of data and convergence of shared understanding to accomplish meaningful action as well as the requirement for communication that supports both (Dennis et al., 2008; Dennis & Valacich, 1999). The conveyance of su<sup>fi</sup>cient information is essential for individuals to reach correct conclusions, while convergence is necessary for the group to be able to act together with synchronicity and with a common understanding (Dennis et al., 2008; Dennis, Fuller, & Valacich, 2008).

Media synchronicity theory portrays media in terms of <sup>fi</sup>ve characteristics: immediacy of feedback, symbo variety, parallelism, rehearsability, and reprocessability. Immediacy of feedback a<sup>f</sup>ects the level of interaction among the participants in communication. Symbol variety refers to the number of ways in which a message may be understood. Parallelism refers to the media’s ability to carry multiple conversations simultaneously. Rehearsability refers to the extent to which an author can take time to prepare and edit a communication, while reprocessability refers to the extent to which a communication can be observed multiple times and be stored for future reference (Dennis et al., 2008; Pe<sup>f</sup>ers & Tuunanen, 2005).

Media richness and media synchronicity theory provide guidance for designing RA communication activities with the necessary su<sup>fi</sup>ciency and richness to optimise RA and understanding. They also provide guidance to convey this understood data to decisionmaking and execution activities with reprocessability and rehearsability, which supports concordance among population members (CONC).

## 3.5.1. Objective for CONC

Communication for RA should be designed so that the communication elements provide the su<sup>fi</sup>ciency and richness in RA to communicate preferences as well as rehearsability and reprocessability to achieve concordance of understanding within a population.

## 4. Nascent design theory: PTRA

PTRA is a nascent design theory for acquiring newsystem functional requirements through e<sup>f</sup>ective population participation in RA activities, where it may otherwise be limited by lack of motivation, impaired ability, or beliefs and values that make it di<sup>fi</sup>cult for managers and designers to understand the population members’ preferences and reasoning. It is intended to a<sup>f</sup>ect RA e<sup>fi</sup>cacy by designing or selecting and adapting techniques to e<sup>f</sup>ectively acquire preferences and reasoning for system functionality from population members. In practice, a PTRA instantiation is a context-situated RA method. An RA method is a collection of RA techniques. An applied RA technique is an instantiation of a given principle for action.

Table 2 outlines a set of <sup>fi</sup>ve principles for action, each of which associates a population state with an applicable social science theory, a principle indicating how the theory can be used to a<sup>f</sup>ect a solution, and the intended performance impact. The principles are intended to form the bases for analysts to adopt, adapt, or design methodological solutions to particular RA problems. The context of an RA task with speci<sup>fi</sup>c populations presents a multidimensional state portfolio, one or more of which may be hitherto unexperienced, others of which may be straightforwardly addressed, and others for which accommodation may be unnecessary.

Nascent design theory for population targeted requirements acquisition.

<table><tr><td>Principle</td><td>State</td><td>Actions</td><td>Contextual factors</td><td>Intended outcome</td></tr><tr><td>Knowledge capture</td><td>Beliefs and mental models affect functional preferences and value (BMM)</td><td>DISCOVER the implicit architecture of the population knowledge; AGGREGATE knowledge with architecture that preserves the population&#x27;s knowledge structure; RETAIN individual requirements data with the resulting aggregated preference and reasoning information</td><td>Preferences; reasoning; values</td><td>OPTIMISE decision makers&#x27; and designers&#x27; understanding of a selected population</td></tr><tr><td>Subpopulation knowledge capture</td><td>Identities, environments, and affiliations affect preferences (IE&amp;A)</td><td>IDENTIFY meaningful subpopulations; ANALYSE requirements data for each to capture preferences and reasoning</td><td>Identities; environments; affiliations</td><td>UNDERSTAND preferences and reasoning for selected subpopulation(s)</td></tr><tr><td>Ability to imagine beneficial functionality</td><td>Motivation and experience affect ability to imagine new technology benefits (IMAGINE)</td><td>CONSTRUCT non-representative samples of motivated participants whose ideas will be predictive of the population; SUPPORT effective participation for the targeted sample of experts</td><td>Risk aversion; inexperience with new technology; lack of motivation</td><td>ELICIT requirements from selected participants of a population</td></tr><tr><td>Participation ability</td><td>Abilities affect functional preferences and participation costs (ABIL)</td><td>ENABLE participation by accommodating technical limitations in ability to participate; CHANGE the economics of participation through technical and procedural accommodation; RECOGNISE preferences and values that differ because of population members&#x27; abilities or limitations</td><td>Ability to participate; non-participation; Ineffective participation</td><td>CAPTURE preferences and values that differ because of population members&#x27; ability to participate or due to limitations in abilities</td></tr><tr><td>Convergent understanding</td><td>Variance in understanding of the value of functionality across populations (CONC)</td><td>TAILOR communication media to effectively acquire preferences, reasoning, and values; GAIN concordant understanding of preferences and their value for decision-making and design</td><td>Shared understanding; convergence.</td><td>DEVELOP system requirements that reflect well-understood preferences for functionality, value, and priority among population members</td></tr></table>

## 4.1. The principles for action

We present the principles as we addressed them earlier in the paper: ordered by the population states that motivated them. Clearly, however, the reader should not understand from this order of presentation that there is a sequential process that should be observed or that all of the principles should be applied to a particular RA e<sup>f</sup>ort. Instead, where the analyst observes a population state that may impair RA e<sup>f</sup>ectiveness, he or she can consider applying the appropriate principle, using a technique that we have used, adapting a di<sup>f</sup>erent one from the literature, or designing a new one for the speci<sup>fi</sup>c task, depending on the contextual factors related to a speci<sup>fi</sup>c population. In following, we present rules for the application of the PTRA as principles for action, as outlined in Table 2.

For BMM, use techniques that (1) discover the implicit architecture of the population knowledge, (2) aggregate knowledge with architecture that preserves the population’s knowledge structure, and (3) retain individual requirements data with the resulting aggregated preference and reasoning information. This principle addresses the objective to capture knowledge and beliefs, values, and mental models that di<sup>f</sup>er for population members, so as to optimise decision makers’ and designers’ understanding of the population’s preferences, reasoning, and values,

For IE&A, use techniques to identify meaningful subpopulations, based on members’ roles speci<sup>fi</sup>c to their identities, environments, and a<sup>fi</sup>liations and capture and analyse requirements data for each in order to understand each subpopulation’s preferences and reasoning.

For IMAGINE, use techniques to construct non-representative samples of lead users or experts who will be motivated and well able to participate e<sup>f</sup>ectively and whose ideas will be predictive of those of the population, to elicit preferences for functionality that is enabled by hitherto unexperienced technology. The objective is to overcome risk aversion, inexperience with new technology, or lack of motivation among population members to participate in order to e<sup>f</sup>ectively capture their ideas and preferences.

For ABIL, enable participation by accommodating technical limitations in ability to participate in RA tasks and change the economics of participation through technical and procedural accommodation. Also, use techniques to recognise preferences and values that di<sup>f</sup>er because of population members abilities or limitations. The objective is to overcome limitations in population members’ ability to participate, which limitations can result in higher costs for the participant and potentially non-participation or ine<sup>f</sup>ective participation.

For CONC, attend to media synchronicity characteristics to tailor communication media to e<sup>f</sup>ectively acquire preferences, reasoning, and values at early stages and to achieve concordant understanding of preferences and their value for decision-making and design at the later stages. The objective is to develop shared understanding and convergence on functionality and feature preferences across the population.

## 5. PTRA in use

Here, we present how we have applied the <sup>fi</sup>ve principles for action to address speci<sup>fi</sup>c problems related to the BMM, IE&A, ABIL, IMAGINE, and CONC states. In each section we also describe how we have evaluated the use of the principles and how this helped us to further develop the PTRA together with <sup>fi</sup>ve client organisations. For Rutgers University we worked with our client to develop a portfolio of systems that would create high value across the campus. For Helsingin Sanomat (HS) (Sanoma Plc.) we helped the newspaper develop a three-year development plan for their self-service ad tra<sup>fi</sup>cking system catering all their advertising clients from consumers to corporate clients, a mission critical system for the newspaper. Digia (Plc.) tasked us with <sup>fi</sup>nding out how consumers would like to use the <sup>fi</sup>rst generation of smartphones for conducting their personal <sup>fi</sup>nancial services – already several years before these devices came to markets. Nokia (Plc.), in turn, asked us to ascertain the features consumers would prefer to use from an innovative and heretofore unseen technology, called “presence,” that conveyed the user’s availability and status. Finally, RNZFB asked us to develop mobile service concepts for blind and visually impaired smartphone users that would go beyond existing technological solutions. This work is summarised in Table 3 and elaborated in the sections that follow. Appendix 1 also provides an overview of all <sup>fi</sup>ve studies and individual project details.

In DSRM (Pe<sup>f</sup>ers et al., 2007), evaluation is divided into two sub-activities: demonstration and evaluation. Demonstration is like a proof-of-concept evaluation to “demonstrate that the artefact feasibly works to solve one or more instances of the problem, i.e. to achieve its purpose in at least one context” (Venable, Pries-Heje, & Baskerville, 2012). The latter evaluation is considered to be formal and it should evaluate how well the artefact supports a solution to the problem (Pe<sup>f</sup>ers et al., 2007). Sonnenberg and Vom Brocke (2012) later expanded on the DSRM demonstration–evaluation pattern to a more re<sup>fi</sup>ned principle-based continuous build–evaluate pattern in which e<sup>f</sup>orts move among identifying a problem, designing, constructing, and using the theory.

We recognise that our e<sup>f</sup>orts in this study have been consistent with this more re<sup>fi</sup>ned, iterative, build–evaluate pattern. Following this approach, we evaluate the <sup>fi</sup>ve principles through their instantiations in the studies, i.e., the individual techniques that have been used to resolve states in each of the <sup>fi</sup>ve studies. Qualitative assessments of instantiated performance by participants, i.e., through observation, participant feedback, and interpretation, is appropriate (Tremblay, Hevner, & Berndt, 2010), because the organisational e<sup>f</sup>ects of DSR artefacts cannot always be observed as rigorously as can, e.g., behavioural e<sup>f</sup>ects observed with quantitative data sets (Winter, 2008).

Application of principles in cases.

<table><tr><td>Case-specific context for application</td><td>Principle applied to resolve state</td><td>Technique(s) applied to the case(s)</td><td>Evaluation of the applied technique(s)</td></tr><tr><td>Rutgers University: New systems applications with high value across the campusHS: Requirements for a system that allows customers to design and purchase display advertising for the newspaper</td><td>Knowledge capture to resolve BMM state</td><td>Laddering interviews with purposive goalsPersonal construct-based network modellingRich presentation tool to aid in communication</td><td>Proof-of-concept validation for laddering interviewing with 1000+ and 2500+ requirements collected and analysed. In addition, the technique has been applied successfully in the other three cases.</td></tr><tr><td>Nokia: Consumers in Finland, Hong Kong, and the USA might want to use their availability or activity, i.e., “presence”, status information in new mobile applications</td><td>Subpopulation knowledge capture to resolve IE&amp;A state</td><td>Qualitative thematic analysisAnalysis of subpopulation requirements data</td><td>Significant differences observed among the three locations with respect to the importance of the system features.</td></tr><tr><td>Digia: Financial mobile service customers for yet-to-be-launched innovative next-generation smartphones</td><td>Ability to imagine beneficial functionality to resolve IMAGINE state</td><td>Lead users, expertsSnowball sample</td><td>Proof-of-concept validation for lead user both with traditional snowballing and the use of virtual communities.</td></tr><tr><td>RNZFB: Blind and visually impaired people&#x27;s participation in RA activities</td><td>Participation ability to resolve ABIL state</td><td>Recruitment by referralRemote interviews</td><td>Preferences most highly rated by the RA participants were also the most highly rated by all study participants.</td></tr><tr><td>Digia: Business and engineering executives and other business and engineering managersRutgers University: System professionals and managersHS: Senior business, marketing, and development managers and executives</td><td>Convergent understanding to resolve CONC state</td><td>Ideation workshops Decision support toolWorkshopEvaluation surveyUpgrade road map</td><td>Proof-of-concept validation by Digia&#x27;s top management and the development of three-year road map of system development for HS.</td></tr></table>

For this purpose, we apply the evaluation criteria suggested by Venable et al. (2012):

● Evaluate each designed principle for action to establish its utility and e<sup>fi</sup>cacy (or lack thereof) for achieving its stated purpose;

● Evaluate formalised knowledge of each principle for action for utility for achieving its purpose;

● Evaluate each principle for action, or formalised knowledge of it, for side e<sup>f</sup>ects or undesirable consequences of its use and identify weaknesses and areas of improvement.

## 5.1. Application of knowledge capture principle

At Rutgers University, we faced a situation where we anticipated and observed that IT professionals and managers saw the university, its environment, and how it worked quite di<sup>f</sup>erently than did faculty members and administrators in the organisation. Our study participants included faculty members from the business, law, and liberal arts schools, so we tried to ensure that expressed functionality would re<sup>fl</sup>ect high-level, strategic purposes, rather than functionality with narrow operational intent. Hoping to encourage participants to think beyond their own needs, we began by asking each to tell us about an idea for a new system that would bene<sup>fi</sup>t Rutgers Camden. We began each interview by asking a participant to rank-order four randomly selected ideas suggested by others. We used the two highest ranked ideas in the interview.

The laddering technique uses stimuli to collect data that includes speci<sup>fi</sup>c preferences for features or functionality, expected consequences, and reasoning for how the respondent relates the outcomes to his/ her value system (Pe<sup>f</sup>ers, Gengler, & Tuunanen, 2003). The data is collected as multiple chains of associations from each participant. Its simplicity is well-suited to handle varied knowledge, values, and belief structures. In this case, the laddering produced data with 149 chains, including more than 1000 individual requirement statements (see Appendix 2 for an example of a ladder chain).

To render this verbose and low-structured requirements data understandable to downstream users, we employed a two-stage hierarchical clustering procedure. First, in an interpretive, agglomerative clustering process, we clustered the 1000+ participant requirement statements into 81 constructs, including descriptive system features, performance outcomes, and goals. This resulted in similar statements being assigned a common construct label. Next, we used a minimum variance quantitative clustering procedure to aggregate the constructs into clusters. We mapped the clusters into graphical PCT-based network maps, a separate map for each cluster (see Appendix 3 for an example of a network map). Each of the <sup>fi</sup>ve network maps represented a system of features, potential consequences, and values that could be interpreted as a new system and reasons therefor, so downstream system designers could understand why speci<sup>fi</sup>c functionality was desired.

At Helsingin Sanomat (HS), we sought to improve upon the clustering techniques that we used at Rutgers University so that chains of reasoning collected from interview participants stayed intact in the analysis. Minimum variance clustering split some of the chains of individual statements into di<sup>f</sup>erent clusters, see details of data clustering methods, e.g., from Aldenderfer and Blash<sup>fi</sup>eld (1984). Keeping the chains intact would facilitate downstream users’ ability to drill down from network maps to individual statements in case they wanted to better understand reasoning nuances. To accomplish keeping the chains intact, we adopted thematic analysis to cluster whole participant chains consisting of 2500+ requirements statements into themes (Braun & Clarke, 2006). Analysts worked independently to cluster the 244 chains of requirements data into <sup>fi</sup>ve themes, in a kind of pile-sorting e<sup>f</sup>ort. After resolving di<sup>f</sup>erences, we created a graphical network value map to represent each theme. The resulting maps contained 60 features, 40 reasons why users wanted the features, and 16 values related to the reasoning. Next, we reexamined the themes to cluster determine by consensus subthemes that could be found in them. Finally, we developed graphical network models that incorporated themes, subthemes, features, reasons, and values, through rounds of sketches.

## 5.1.1. Utility and e<sup>fi</sup>cacy of the knowledge capture principle

The use of laddering interviews resulted in 1000+ requirements statements in the Rutgers case, providing proof-of-concept validation for the utility of the technique. The same technique was used with HS with 2500+ requirements statements, which provided further validation for the utility of the technique for RA.

In the Rutgers case, we used a data-clustering technique to aggregate the 149 laddering chains to constructs and later to graphical network maps. Later, in the HS case, we used an improved clustering technique to aggregate 244 laddering chains into constructs and themes. The result was graphical network maps that describe the population’s needs for features, their reasoning behind these, and goals and values that drive their perceived use intentions. The ability to handle a more complex requirements data set provides further validation for the utility and e<sup>fi</sup>cacy of the technique.

We used the thematic clustering technique later in the three other cases without any signi<sup>fi</sup>cant changes and in several studies that have followed the PTRA development project, see, e.g., Tuunanen and Govindji (2016). The technique has also been used by 15+ graduate students for their thesis studies in Finland and New Zealand. Thesis students need a two 1-h workshops to learn how to use the laddering and thematic clustering techniques; thereafter they require only supervisorial guidance. We also use PTRA as part of master’s level courses with 40–50 students.

5.1.2. Formalised knowledge about the knowledge capture principle’s utility for achieving its purpose At Rutgers University, the clients saw barriers – different mental models of the systems’ purposes – among IT and academic professionals and managers. This limited the ability of the IT group to understand the academics’ functional preferences. Intensive requirements collection and network modelling allowed us to provide the IT group members with very rich information that helped them understand user preferences and reasoning much better than previously (Pe<sup>f</sup>ers et al., 2003).

Thematic clustering, with its much improved retention of participant reasoning, enabled us use the requirements data to create subthemes. With this complex knowledge structure in hand, we were able to create a multidimensional, multimedia representation in a tool that could present preferences, reasoning, and values at various levels of granularity to several potential audiences of development participants (e.g., executives, designers, and programmers). The information was rich enough and the presentation robust enough that it was used for several years during the development and system upgrade e<sup>f</sup>ort (Tuunanen, 2005).

## 5.1.3. Side e<sup>f</sup>ects or undesirable consequences of the knowledge capture principal use or weaknesses and areas of improvement

For Rutgers, we applied a made-for-purpose software application (not updated to run on any contemporary computer) to collect and code the data, to cluster the data according to Ward’s technique (Ward, 1963), and to produce a draft network map. Although the results were good and the analysis provided meaningful results in terms of graphical network maps (Pe<sup>f</sup>ers et al., 2003), we were concerned about the analysis technique. Requirements preference statements had to be coded so that the software could cluster the data. We were concerned that the coding resulted in the loss of some individual requirement details. We wanted to retain individual requirement preferences, with detailed feature descriptions, reasons for wanting these features, and goals and values that drove desires for the features. Thus, losing this detail in analysis would constitute a fault.

To solve this problem, we developed a thematic clustering technique (Tuunanen, Pe<sup>f</sup>ers, & Gengler,

2004). Thematic analysis allowed us to cluster whole statements into themes and subthemes, from which we could develop network models of preferences, reasoning, and values, while retaining all of the individual data. This resulted in more detailed network maps and allowed us to use the individual data to develop the earlier described multidimensional, multimedia presentation tool to present <sup>fi</sup>ndings to downstream users. Thematic analysis was applied for the <sup>fi</sup>rst time at HS, which also allowed us to deploy the presentation tool for development of the system (Tuunanen, 2005).

## 5.2. Application of subpopulation knowledge capture principle

At Nokia, we sought to extend our e<sup>f</sup>orts to understand user preferences and reasoning by considering the di<sup>f</sup>erent preferences connected with social identities and environments. The Nokia study was global in nature, and within that study it was considered very important to avoid errors that can result when managers assume an application that is successful in one culture will work in another one. We expected the requirements data that we collected from Hong Kong, Helsinki, and Las Vegas to di<sup>f</sup>er, in part because of the di<sup>f</sup>erent cultural environments and the resulting social identities. Our operating premise was that we would notice substantial di<sup>f</sup>erentiation in preferences for mobile application functionality and features among these locations.

Using thematic analysis, as we had done at HS, we classi<sup>fi</sup>ed all 663 chains into themes. The mobile application ideas were clustered into six themes, including “Special Interest Groups”, “Presence Messaging”, “City Reporter”, and “Shopping Assistant”. Each of these themes became the basis of a graphical network model to describe a set of functionality and feature preferences, expected consequences, and personal values a<sup>f</sup>ected.

## 5.2.1. Utility and e<sup>fi</sup>cacy of the subpopulation knowledge capture principle

We observed statistically signi<sup>fi</sup>cant di<sup>f</sup>erences among the three locations with respect to the importance of the themes (Tuunanen et al., 2006), such that applications built on a global view of preferences would likely have failed in one or more of the locations.

● “Special Interest Groups” was most important in Helsinki (preferred by 33% of participants; e.g., to facilitate pick-up hockey games);

● “City Reporter” predominated preferences in Hong Kong (preferred by 36%; e.g., for entertainment activities); and

● “Presence Messaging” with location was most important in Las Vegas (preferred by 26%; e.g., to enhance hunting party coordination for safety with availability/activity information).

However, one theme, “Shopping Assistant”, showed a uniform preference level in each of the three cities, at about 18%. The results provide strong evidence for the utility and e<sup>fi</sup>cacy of the principle’s instantiation to capture subpopulation preferences.

## 5.2.2. Formalised knowledge about the

## subpopulation knowledge capture principle’s utility for achieving its purpose

In the Nokia case, we sought ideas for global applications using technical capabilities that had never been used before in consumer products. It was critical that we not make the dangerous assumption that applications attractive to one population would be similarly attractive elsewhere. To di<sup>f</sup>erentiate preferences among the cities, we did a full study in each. The results revealed very di<sup>f</sup>erent preferences among our sample participants in each of the cities, strongly supporting the need to develop application portfolios separately for each population (Tuunanen et al., 2006).

## 5.2.3. Side e<sup>f</sup>ects or undesirable consequences of the subpopulation knowledge capture principle use or weaknesses and areas of improvement

The end result of the study surprised us. We did not anticipate that cultural di<sup>f</sup>erences would be so evident in the data. The results thus justify further research to better acquire culturally distinct requirements. Such a technique would focus on developing feature themes based more on region-speci<sup>fi</sup>c preference reasoning than on speci<sup>fi</sup>c feature preferences (Tuunanen et al., 2006), and some researchers have already proposed ways to accomplish this. For example, Tuunanen and Kuo (2015) have proposed that a value-based view of culture be assessed and consequently requirements be prioritised as one solution to this, and provide results that di<sup>f</sup>erentiate the subpopulations, but also provide insights of the di<sup>f</sup>erences between population members within a subpopulation.

## 5.3. Application of ability to imagine bene<sup>fi</sup>cial functionality principle

At Digia, we addressed the problem of how to motivate population members to participate and how to improve participants’ ability to imagine functionality for technologies that had not hitherto been made available to end-user customers. The potential customers would be well-to-do, business-savvy, and active professionals, managers, and investors. Few, if any, of the potential customers had experience with or any other reason to care about Digia.

To address this, we needed a sample of the very small number of potential customers who would also qualify as lead users, who, as the di<sup>f</sup>usion of innovations theory describes them, are the small number of people, within any population, who tend to adopt new technology <sup>fi</sup>rst and would be able and motivated to imagine the functionality and value of applications they had not previously encountered (Olson & Bakke, 2001). In this case, the lead users would be a hidden population, distributed among the general population. To locate them, we adopted the snowball selection technique (Salganik & Heckathorn, 2004), which assumes that if we can <sup>fi</sup>nd one or more members of an otherwise hidden subpopulation they will be acquainted with and can refer us to others in the subpopulation and the subject pool for the study will “snowball” to a su<sup>fi</sup>- cient size. Knowledge-based screen is used to validate the membership of each new potential participant in the study.

## 5.3.1. Utility and e<sup>fi</sup>cacy of the ability to imagine bene<sup>fi</sup>cial functionality principle

To elicit participation for the Digia study, we developed two lists of potential participants: experts and lead users. For potential expert participants, we worked with Digia’s CEO Mr Sivonen and his executive assistant to develop a list that included a cross section of Finland’s most relevantly knowledgeable scientists, professionals, and managers. For lead users, we elicited participation from sophisticated communications technology users, starting with nominations by faculty members at the Helsinki School of Economics. After referrals from the nominees, a combined list of nominated participants contained 40 names. We were able to contact 32 of them, all of whom participated.

## 5.3.2. Formalised knowledge about the ability to imagine bene<sup>fi</sup>cial functionality principle’s utility for achieving its purpose

At Digia, we addressed the problem of studying preferences for applications about which almost none of the potential customers would have given prior thought, in order to discover the potential mobile “killer application” for <sup>fi</sup>nancial services. We combined the lead user concept with the snowball sample selection to seek out RA participants among the three-dozen people in the country most likely to be able to imagine potential valuable application functionality. Among those contacted, everyone participated with very substantial e<sup>f</sup>orts and the resulting application ideas became the basis for several early mobile <sup>fi</sup>nancial applications.

## 5.3.3. Side e<sup>f</sup>ects or undesirable consequences of the ability to imagine bene<sup>fi</sup>cial functionality principle use or weaknesses and areas of improvement

The lead user and snowballing technique combination was later used in the Nokia study with an adaptation. For two of the research sites, Hong Kong and Las Vegas, we followed the original technique reported here, but also developed a set of screening questions to select the participants. These screening questions were based on the di<sup>f</sup>usion of innovations theory with the purpose of recognising potential lead users for their general innovation adoption behaviour and were also speci<sup>fi</sup>c to the mobile service at hand (Tuunanen, Bragge, Häivälä, Hui, & Virtanen, 2011).

In the third location, Helsinki, we decided to try to attract participants from a selected set of virtual communities. Our goal for this was to attempt to provide a solution to previously encountered problems related to the repeated use of snowball sampling of lead users (Olson & Bakke, 2001). The results were promising. The perceived quality of the participants, based on their data input, was statistically equally good in the study that used the virtual community approach versus the other that used the traditional snowballing technique to recruit the lead users (Tuunanen et al., 2011).

However, we did experience unexpected hardships in recruiting blind and visually impaired participants for the RNZFB study. This led to further development of the PTRA theory and the inclusion of the participation ability principle reported next.

## 5.4. Application of participation ability principle

At the RNZFB, we addressed the problem of e<sup>f</sup>ective target population participation in design of innovative mobile services through a technical accommodation to conserve participant working memory resources and an economic and social accommodation for higher participation costs and participant concerns for safety. Our preliminary study led us to expect to be prepared to accommodate three barriers to blind RA participation. First, blind persons may feel vulnerable when meeting unfamiliar people, so a mechanism to establish preliminary trust is necessary. Second, travel for the blind is generally far more time consuming than for the sighted and often more hazardous, particularly when travelling to a new place for the <sup>fi</sup>rst time, so avoiding unnecessary travel is important. Third, blind persons have the same limitations in terms of their working memory capabilities as do sighted people, so some RA activities may require redesign when oral presentation is substituted for visual, since visual presentation material tends to be persistent and can extend short-term memory.

Participant recruitment was challenging because of the need to establish trust among this population, because the target participants were scarce among the general population, and because we had no reason to think that they would be particularly interested in participating. We used participant recruitment by referral to help accommodate the trust issue. Speci<sup>fi</sup>cally, we used a trusted intermediary, the communication channels of the RNZFB, to refer prospective participants for the study. Referral by this trusted organisation was expected to allow us to borrow credentials from this well-respected organisation, thereby mitigating risks attached to meeting with strangers. We emailed several hundred invitations to RNZFB lists, inviting list members to take a short screening survey. An announcement was also posted on the RNZFB telephone oral newspaper service. In addition, the researchers asked willing participants to nominate other likely participants and contacted them either by email or through the referring participant. These e<sup>f</sup>orts yielded <sup>fi</sup>ve participants after 4 weeks.

Recruitment continued with a presentation about the study by a researcher at the RNZFB training centre, yielding <sup>fi</sup>ve participants. RNZFB sta<sup>f</sup> contacted people directly, yielding three more participants. In addition, one of the sta<sup>f</sup> members agreed to participate. In all, this resulted in 14 potential participants in New Zealand. We then turned our attention to Germany and to an online newspaper for the blind, Trierische Tonpost. This medium yielded 9 participants, for a total of 23. To screen for quali<sup>fi</sup>ed users, we used a two-part screening survey that included use and knowledge questions about technology. One participant was screened out of the study, leaving 22 participants.

To accommodate the potential cost, convenience, and safety concerns of the participants regarding travelling to a place that is new to them, we arranged to conduct the laddering interviews by telephone. By telephone, we invited each of the 22 participants to an individual interview and asked each of them to give us one idea for a potential mobile service that would be of interest to them. Some participants contributed three or more ideas. After the <sup>fi</sup>rst seven invitations, we developed a preliminary list of stimuli for use with the <sup>fi</sup>rst interviews. This was gradually extended and re<sup>fi</sup>ned with new ideas for the remainder of the interviews. This allowed us to start the interviews before all participants had committed to taking part. The interviews lasted an average of 35 min each, with no noticeable di<sup>f</sup>erence when the interview was conducted in person or by telephone. Telephone interviews served to minimise potential resistance to unnecessary travel among the participants.

Later, we telephoned each participant to conduct a short feedback interview. We wanted to understand which themes were the most important, so the problem was to represent each theme and its associated features without overwhelming participants’ short-term memory with verbose descriptions. To limit complexity, each theme was given a brief description that included a re<sup>fi</sup>ned name of the theme, followed by a summarised enumeration of the related features. The theme summaries were read to the participants. After each summary, the participant was asked to indicate, on a scale between 1 and 10, the value of the theme to him/her.

Theme-level preferences comparison before/after <sup>Table 4.</sup>data analysis.

<table><tr><td colspan="2">Pre-analysis sum of  $ratings^a$ </td><td colspan="2">Post-analysis sum of  $ratings^b$ </td></tr><tr><td>Navigation and routing</td><td>173</td><td>Navigation and routing</td><td>161</td></tr><tr><td>Traffic and public transport assistant</td><td>153</td><td>Shopping assistant</td><td>155</td></tr><tr><td>Shopping Assistant</td><td>147</td><td>Traffic and public transport assistant</td><td>154</td></tr></table>

<sup>a</sup>Sums of inverted ranking scores, normalised by multiplying the inverted ranking by the number of items ranked by the participant.  
<sup>b</sup>Sum of Likert-type scale ratings (1–6).

## 5.4.1. Utility and e<sup>fi</sup>cacy of the ability to participate principle

We evaluated the utility and e<sup>fi</sup>cacy of the instantiation as follows. Firstly, we aimed to clarify which of the ideas proposed by individual participants were most valued by others. Secondly, we sought to verify whether the interpretive analyses, which were carried out by the researchers, accurately represented users’ needs. After the laddering interviews were conducted, we asked the participants to rank order their top three ideas. This provided us with the <sup>fi</sup>rst round of data. Thereafter, data was collected in follow-up telephone interviews. Table 4 presents a tally of Likert-type rating scales for the ideas that lie within the top three themes, which accounted for 70% of the rating scores. The results show that the preferences most highly rated by the participants in the laddering interview collection were also the most highly rated by all participants during the post-interview feedback collection. The fact that the same themes where highly rated suggests some support for the aggregation and modelling of the analysts, i.e., that the preferences and reasoning were well captured and interpreted. The rest of the themes followed this trend within the data.

## 5.4.2. Formalised knowledge about the ability to participate principle’s utility for achieving its purpose

We recognise that based on the <sup>fi</sup>ndings populations with RA ability limitations hold di<sup>f</sup>erent functional preferences and that understanding their economic, social, and technical requirements for participation is key to successful RA e<sup>f</sup>orts. We addressed the problem of participant trust by obtaining referrals to potential participants from trusted organisations. We addressed logistical and economic costs by conducting requirements collection remotely. We addressed participant working memory load through a scenario-based, two-step rank-ordering technique. This provided trust, motivation, convenience, safety, and vision for the participants and resulted in an adequate sample and good requirements data. In the study, we were able to identify application functionality that we would have been very unlikely to discover in RA e<sup>f</sup>orts with a general population sample.

## 5.4.3. Side e<sup>f</sup>ects or undesirable consequences of the ability to participate principal use or weaknesses and areas of improvement

The extension of this work is ongoing, and we see that, e.g., further work needs to be done in order to reduce the cognitive load of participation for populations with limitations in ability to participate, such as being blind or visually impaired. For these participants, this is a major problem as most of the RA techniques heavily rely on visual cues for interaction between the analyst and the population members.

During this study, we also recognised that these limitations are not necessarily only limited to disabilities, but instead, our abilities to participate can be in<sup>fl</sup>uenced by di<sup>f</sup>erent physical and/or cognitive abilities.

## 5.5. Application of convergent understanding principle

At Rutgers University, we sought to demonstrate that our requirements collection and analysis techniques would lead to managers and designers having a very good understanding of what users wanted and why. The requirements collection and analysis e<sup>f</sup>orts resulted in <sup>fi</sup>ve network maps, each representing an idea for a new system that employees thought would be important to the Rutgers Camden Campus, such as “Excellence through Research” and “Student Recruitment and Quality”. Each described speci<sup>fi</sup>c system features, critical success factors a<sup>f</sup>ected, and university goals.

Using these outcomes, we organised two half-day ideation workshops with Rutgers system professionals and managers in two locations. We charged them with the objective to use their expertise, without resorting to outside information, to produce “backof-the-envelope” level proposals that brie<sup>fl</sup>y described feasible system projects that addressed performance in terms of the models described by the maps. The projects were to be speci<sup>fi</sup>ed brie<sup>fl</sup>y in terms of a project name, description, the likely project architecture, resources required, cost, risk, and expected impact on the organisation.

Workshop participants transformed the network models into four feasible system ideas. They found that the richness of the models helped them understand what the participants intended, although they wished that they could have much more richness, e.g., by asking clarifying questions.

At Digia, we extended our e<sup>f</sup>orts to provide managers and designers with rich, actionable information from which they could develop ideas for applications that would support new, smartphone-based <sup>fi</sup>nancial businesses. Requirements collection and analysis at Digia produced <sup>fi</sup>ve network models for customerfacing mobile applications.

To provide the managers and professionals with the capability of creating feasible and worthwhile application ideas, we raised the level of participation in the workshop above what it had been at Rutgers. A 5-h ideation workshop was held in isolation, which was attended by Digia’s highest level business and engineering executives. For each of the <sup>fi</sup>ve models, the objective was to come up with a project idea that would address the consequences and values expressed in the models and, importantly, that would be feasible. The ideas were to be expressed at a “back-of-theenvelope” level of detail, including a name, short description, IT architecture, list of supply chain players, user segment(s), bene<sup>fi</sup>ts for value chain participants and users, pro<sup>fi</sup>t model, and risks involved (Pe<sup>f</sup>ers & Tuunanen, 2005).

We extended the presentation design further at HS to create a tool that might be used as a communication artefact among parties to decision-making, design, and implementation. We wanted to implement a high level of reproducibility in a tool that could be used over and over in the decision and design processes and one that would present di<sup>f</sup>erent views of the preferences and reasoning on demand. The <sup>fi</sup>ve network value models, similar to those created for our earlier clients, became Level 1 in the three-dimensional decision support tool. Level 1 could be used by anyone to understand the big picture of a new system. The Level 1 representation included two innovations. First, subthemes in this layer facilitated presentation of <sup>fi</sup>ner grained feature preferences than we had presented to prior clients. Secondly, hyperlinks in Level 1 allowed the user to drill down to Level 2 to see individual participant statement chains. Links led the viewer further down to Level 3, where the viewer could listen to recorded segments of any of the original statements.

We used this decision support tool to facilitate negotiation activities, including a manager/developer workshop, validation and evaluation of the requirements, the development of a business report recommending speci<sup>fi</sup>c actions, and an application road map to plan a speci<sup>fi</sup>c, sequenced, and timed set of future service updates. We held a full-day workshop that featured participation by senior business, marketing, and development managers and executives. There, we demonstrated use of the tool to managers and developers so that they understood it as an expression of user preferences and learned how to use it to obtain rich information.

To complete the decision-making process, we sought to develop a 3-year road map for HS’ system upgrades. First, we employed a feedback e<sup>f</sup>ort to validate and evaluate the themes and features. To measure the value of the requirements items, we conducted a survey with an independent sample of 33 people. The results were used to develop a business report that described the most valuable subthemes or “system features”, in rank order (Tuunanen, 2005; Tuunanen et al., 2004).

## 5.5.1. Utility and e<sup>fi</sup>cacy of the convergent understanding principle

At Rutgers, ideation workshop participants saw opportunities to use the network maps to propose system solutions that did not always need the development of major new applications, and the ideation workshops enabled them to consider relatively inexpensive solutions to their important system needs (Pe<sup>f</sup>ers et al., 2003). At Digia, Mr Markus Ahonen, a product analyst, regarded our study and its results favourably for the following reasons: (1) the technique seems to work well, and it is easy to see why it works; (2) the interviewer collecting data for the technique needs no special abilities or skills; and (3) the resulting network maps are very helpful in understanding how people think about an issue and Digia’s chairman, Mr Pekka Sivonen, remarked that the workshop “positively exceeded [his] expectations [about] the results” needs (Pe<sup>f</sup>ers & Tuunanen, 2005).

In the HS study, the report that summarised the 3-year road map for their system upgrades recommended that the <sup>fi</sup>rm focus resources to develop the top 10 features list and the top 3 themes: those that the survey participants valued the most. Using the decision support tool and the business report, the HS project team developed a 3-year upgrade road map for the system that described features, priorities, and development schedules. The road map called for the release of four major system upgrades in 2004 and 2005. Almost all of the features included in the road map can be traced back to the study data, including 42 of the 59 (71%) functional features that were speci<sup>fi</sup>cally recommended in the business report (Tuunanen, 2005; Tuunanen et al., 2004).

## 5.5.2. Formalised knowledge about the convergent understanding principle’s utility for achieving its purpose

At Rutgers University, we were able, according to feedback from our clients, through two-half-day workshops, to help technical professionals and managers understand the preferences and reasoning of managers, as they had not been able to understand it in the past. They saw the potential, however, to be provided with much more rich requirements data. At Digia, we extended these e<sup>f</sup>orts dramatically by engaging top executives in the workshop and by extending the workshop outcomes to include, e.g., supply chain participants, user segment(s), and pro<sup>fi</sup>t-model descriptions. We extended the potential e<sup>fi</sup>cacy of the outcomes to facilitate convergent understanding further at HS with the development of a multilevel, multimedia decision support tool to support communication among managers and development professionals. We also conducted follow-up requirements collection and analysis to prioritise the functional features. We used this to help the client produce a 3-year upgrade road map for the system, nearly all of which was subsequently implemented.

## 5.5.3. Side e<sup>f</sup>ects or undesirable consequences of the convergent understanding principal use or weaknesses and areas of improvement

The reported instantiation of the principle relies on the use of o<sup>fi</sup>ce application packages and thus does not provide ways to link the requirements data to design. This was studied in several follow-up studies, and meta-modelling was considered an interesting approach to resolve this. For this work, we used a well-known package software, MetaCase+, to provide proof-of-concept-level validation (Rossi & Tuunanen, 2010; Tuunanen & Rossi, 2004).

Later, we developed an open-source application based on the Eclipse framework for using the PCTbased requirements data structures to develop metamodels of system requirements (Przybilski & Tuunanen, 2007). These meta-models were linked with Java code to enable drag-and-drop-style generation of code and rapid prototyping of the application (Tuunanen & Przybilski, 2014). This way, the population members, in addition to the managers and designers, could be easily included in creating convergent understanding of the important features for a given application.

## 6. Discussion

PTRA applies techniques to problems through theoretically justi<sup>fi</sup>ed principles. The nascent design theory has been used in projects for more than 10 years, and the techniques depicted here have undergone several iterations for those projects. Consequently, our studies have demonstrated principles for implementation, including step-by-step instructions and case-speci<sup>fi</sup>c process models of applying PTRA in di<sup>f</sup>erent settings to develop context-situated RA methods for clients. An exemplar of a context-situated RA method is discussed in Section 7 and further elaborated in Appendix 4. The <sup>fi</sup>eld case studies have also shown practical success with the PTRA theory.

In addition, PTRA has been used in other projects, e.g., Hänninen, Tuunanen, and Vartiainen (2015) and Tuunanen and Govindji (2016), which have been similarly successful. Finally, we evaluate the theory by assessing the utility and e<sup>fi</sup>cacy of the principles; present formalised knowledge of the principle’s utility for achieving its given purpose; and present possible side e<sup>f</sup>ects, undesirable consequences, weaknesses, or areas of improvement for the principles.

The study additionally contributes to the literature in terms of the <sup>fi</sup>ve theories we applied while developing PTRA as a nascent design theory. Over the years, we have worked with the PCT (Kelly, 1955) and especially looked at how we can enhance the presentation of requirements, but also at the analysis of laddering interview-based requirements data sets. This work contributes to the earlier work done with repertoire grids (Davis et al., 2006) and cognitive mapping in general (Montazemi & Conrath, 1986). Furthermore, our studies provide examples of how to apply PCT and laddering interviewing to RA. This work extends and continues the work by Browne and Ramesh (2002) and Browne and Rogich (2001), who introduced these ideas to the IS literature.

The study also contributes to the SAT literature (Lamb & Kling, 2003). We apply the concept of a social actor as an IS user to further understand how context a<sup>f</sup>ects RA. Our work therefore extends the literature on recognising how perception of roles and the environment a<sup>f</sup>ects population needs for system (s). This work also links Holmström and Sawyer’s (2011) argument of the need for developers, as well as managers, to understand the wider context of system use. Furthermore, our study contributes to the literature that looks at culture’s impact on RA, see, e.g., Tuunanen and Kuo (2015).

Although the impact of varying levels of technological experience on RA has been recognised in the literature (Tiwana & Keil, 2006), little use of this literature has been made to guide RA. We highlight here how technological experience and attitudes towards new technologies can be accommodated for in RA by applying the lead user concept (Von Hippel, 1986). Our work also illustrates that the use of nonrepresentative population sampling can be helpful to make use of lead users for RA. Consequently, our study also extends the literature on product development, see, e.g., Olson and Bakke (2001) and the use of lead users in development.

Our study introduces the systems theory of disability (Michailakis, 2003) to the RA literature. This theory impresses us as potentially extremely useful for IS research. A person is not either able or disabled; he or she is disabled with respect to particular social systems in which his or her physical or mental limitations a<sup>f</sup>ect participation. Thus, we are all now, or were, or are likely to be disabled with respect to one system or another. In this view, disability is a problem for most, not for a small minority. What is more, we extend the current view of how to deal with di<sup>f</sup>erent kinds of population members’ ability limitations. PTRA can be applied to resolve some of the obvious problems facing RA with, e.g., blind participants; however, we need not be limited to this perspective. We can think in terms of accommodating varying sets of limitations that occur among population members. For example, these can be related to problems with RA and the elderly (Sustar et al., 2008) or children (Molin-Juustila et al., 2015).

Finally, our study contributes to the information theory literature (Daft & Lengel, 1986; Dennis et al., 2008) and how it can be applied in RA. The speci<sup>fi</sup>cation of requirements is a widely recognised problem in the literature (Mathiassen et al., 2007). Our study extends the previous literature by demonstrating how information theory can be applied in di<sup>f</sup>erent RA settings in order to gain convergent views of requirements.

## 7. Implications for practice

The PTRA theory o<sup>f</sup>ers a set of principles for action that are ready for use in practice. It has been extensively <sup>fi</sup>eld tested through use in 20+ research projects. The cost to train analysts to adopt the PTRA in practice has not been excessive. While the cases presented here bene<sup>fi</sup>ted from participation by authors, others have successfully applied the theory in subsequent projects with modest levels of training, e.g., two 1-h sessions, along with some supervised practice. The subsequent projects were conducted in development contexts such as an intelligent mining industry equipment system (Hänninen et al., 2015) and an Internet television service for tertiary education (Tuunanen & Govindji, 2016).

PTRA’s applicability to practice is independent of what systems analysts think of as “requirements speci<sup>fi</sup>cations”, but it could be the front-end requirements collection and analysis that set up the requirements speci<sup>fi</sup>cation e<sup>f</sup>orts and subsequent system to be very successful. PTRA is also independent of IT portfolio planning but understanding the potential functionality of systems in the IT project portfolio can go a long way towards understanding their value and strategic contribution. In addition, PTRA is independent of the IS development methodology and project stage. It should work equally well with methodologies from waterfall to agile. Furthermore, the design of the principles for action and the study descriptions, summarised in Table 3, provides examples for how to think about the instantiation of PTRA. The reader who is interested in additional, very operational, detail can further pursue our narrative of the HS study that is summarised in

Appendix 4 where we explicate an instantiation of a context-situated RA method.

## 8. Conclusions

We have identi<sup>fi</sup>ed a research problem and justi<sup>fi</sup>ed its solution in developing new systems: understanding the needs and preferences of various system users, for whom such understanding is not straightforwardly accomplished. We used several theories to frame our investigation and the development of PTRA, a nascent design theory to acquire requirements, and we associated each of the theories with the solution to a speci<sup>fi</sup>c RA problem. In <sup>fi</sup>ve RA case studies with real external clients, we designed, demonstrated, evaluated, and, where applicable, iteratively redesigned or extended a RA technique. The result of the work here is a nascent design theory for RA. PTRA can be used by actors in the development process, where the actors choose to apply speci<sup>fi</sup>c elements of the principles to suit their population RA needs.

The paper makes the following contributions to the literature. First, it presents PTRA, a nascent design theory, which is shown to be useful for deeply understanding population preferences and reasoning for new system or application functionality. The paper also argues for a need for population targeted RA and presents <sup>fi</sup>ve states related to resolving population speci<sup>fi</sup>c RA problems. Finally, it demonstrates the use of the DSRM (Pe<sup>f</sup>ers et al., 2007) to develop and evaluate a nascent design theory.

The limitation of what is accomplished here is inherent in the larger purpose of the artefact, the exhaustiveness of which is limited on several dimensions. First, identifying states that could interfere with successful RA is an unbounded problem. The number of such states is not <sup>fi</sup>nite, and many of them might bene<sup>fi</sup>t from PTRA. Secondly, identifying theories that could contribute to RA methodological design is also unbounded. We purposefully selected <sup>fi</sup>ve known theories that we expected to make such contributions. From a number of theories that, from our perspective, is not <sup>fi</sup>nite, we know of no practical, objective technique to determine the best ones for this purpose. Better theory remains to be identi<sup>fi</sup>ed and deployed to extend or complement PTRA. Thirdly, readers might infer that there is an unspoken premise to this work that managers and developers know which stakeholders’ preferences are important to accommodate in a system. The question of stakeholder identi<sup>fi</sup>cation and salience (Mitchell, Agle, & Wood, 1997) is in itself a broad, multidimensional <sup>fi</sup>eld of study. We could not begin to address it in this paper.

RA techniques have made enormous strides since the era in which engineers and managers were sure that they knew best about what a system should do and how it should interact with “users”. Now, we move beyond that into an era in which organisations seek to market customised services to segments as small as one customer (Bailey, Baines, Wilson, & Clark, 2009; Kara & Kaynak, 1997) and to co-produce services with customers (Lusch & Nambisan, 2015; Peters et al., 2016). This means that the ability to capture and understand the preferences and reasoning for all customers, not just the majority of them, will carry very high value. It is not hard to imagine that system requirements might bene<sup>fi</sup>t from a similar logic.

The enumeration of the limitations described above clearly segues to opportunities for productive research e<sup>f</sup>orts. Designing new applications, systems, and ITbased products or services is at the very centre of the raison d’être for IS research. This paper provides a conceptual basis for research on RA techniques for speci<sup>fi</sup>c populations and context-situated RA methods (cf. Appendix 4), but we think that it has hardly scratched the surface. We believe it best to think of this paper as a modular core, which researchers can improve through extension and redesign. We anticipate a need for additional theory and methodology development for RA; the recognition of population states that require di<sup>f</sup>erent theories and techniques; the identi<sup>fi</sup>cation of populations and their salience; the development of a more mature general DSR theory for population-targeted RA; and research about how to blend deep, qualitative RA with big data analytics. All are required and will provide opportunities for productive DSR research. Fortunately, the architecture of the design theory described here lends itself, with its modularity, to extension and revision. We hope to see subsequent research that explicates extension of the design theory with additional states, theories, and principles, as well as redesign of principles that we have explicated here.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## ORCID

Tuure Tuunanen http://orcid.org/0000-0001-7119-1412 Ken Pe<sup>f</sup>ers http://orcid.org/0000-0001-7511-3702

## References

Aldenderfer, M. S., & Blash<sup>fi</sup>eld, R. K. (1984). Cluster Analysis. Beverly Hills and London: Sage.

Appan, R., & Browne, G. J. (2010). Investigating retrievalinduced forgetting during information requirements determination. Journal of the Association for Information Systems, 11(5), 250–275. Retrieved from <Go to ISI>://WOS:000280539800001

Bailey, C., Baines, P. R., Wilson, H., & Clark, M. (2009). Segmentation and customer insight in contemporary services marketing practice: Why grouping customers is no longer enough. Journal of Marketing Management, 25(3–4), 227–252.

Bergman, M., King, J. L., & Lyytinen, K. (2002). Large scale requirements analysis revisited: The need for understanding the political ecology of requirements engineering. Requirements Engineering, 7(3), 152–171.

Bergum, B. O., & Bergum, J. E. (1981). Population stereotypes: An attempt to measure and de<sup>fi</sup>ne. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. Thousand Oaks, CA: Sage.

Blackburn, S., & Cudd, P. (2012). A discussion of systematic user requirements gathering from a population who require assistive technology. Technology and Disability, 24(3), 193–204.

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 32, 77– 101. Retrieved from: http://www.tandfonline.com/doi abs/10.1191/1478088706qp063oa.

Browne, G. J., & Ramesh, V. (2002). Improving information requirements determination: A cognitive perspective. Information & Management, 39(8), 625–645. Retrieved from <Go to ISI>://000176750500001

Browne, G. J., & Rogich, M. B. (2001). An empirical investigation of user requirements elicitation: Comparing the e<sup>f</sup>ectiveness of prompting techniques. Journal of Management Information Systems, 17(4), 223–249. Retrieved from <Go to ISI>://000167939400010

Byrd, T. A., Cossick, K. L., & Zmud, R. W. (1992). A synthesis of research on requirements analysis and knowledge acquisition techniques. MIS Quarterly, 16(1), 117–138. Retrieved from <Go to ISI>://A1992HM97300009

Calefato, F., Damian, D., & Lanubile, F. (2007). An empirical investigation on text-based communication in distributed requirements workshops. International conference on global software engineering (ICGSE 2007), IEEE, Munich, Germany. doi:10.1109/ICGSE.2007.9

Caxton, N. (2015). The Influence of Luyia Traditional Religious Rituals on Christianity: a Case Study of African Israel Church Nineveh in Vihiga County, Kenya (PhD Dissertation Dissertation). University of Nairobi.

Chakraborty, S., Sarker, S., & Sarker, S. (2010). An exploration into the process of requirements elicitation: A grounded approach. Journal of the Association for Information Systems, 11(4), 212–249. Retrieved from <Go to ISI>://WOS:000280539300002

Charaf, M. C., Rosenkranz, C., & Holten, R. (2013). The emergence of shared understanding: Applying functional pragmatics to study the requirements development process. Information Systems Journal, 23(2), Retrieved from <Go to ISI>://WOS:000314068200002, 115–135.

Daft, R., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 33(5), 554–569.

Darke, P., & Shanks, G. (1996). Stakeholder viewpoints in requirements de<sup>fi</sup>nition: A framework for understanding viewpoint development approaches. Requirements Engineering, 1(2), 88–105.

Davis, C. J., Fuller, R. M., Tremblay, M. C., & Berndt, D. J. (2006). Communication challenges in requirements elicitation and the use of the repertory grid technique. Journal of Computer Information Systems, 46(5), 78–86.

De Oliveira, M., Viana, D., Conte, T., Vieira, S., & Marczak, S. (2013). Evaluating the REMO-EKD technique: A technique for the elicitation of software

requirements based on EKD organizational models. 2013 3rd International Workshop on Empirical Requirements Engineering (EmpiRE), Rio de Janeiro, Brazil. doi: 10.1109/EmpiRE.2013.6615210

Dennis, A. R., Fuller, R. M., & Valacich, J. S. (2008). Media, tasks, and communication processes: A theory of media synchronicity. MIS Quarterly, 32(3), 575–600.

Dennis, A. R., & Valacich, J. S. (1999). Rethinking media richness: Towards a theory of media synchronicity. Proceedings of the 32nd Hawaii International Conference on System Sciences - 1999, p 10 p. Retrieved from: www.computer.org/proceedings/hicss/0001/ 00011/00011017.PDF

Donaldson, T., & Preston, L. E. (1995). The stakeholder theory of the corporation: Concepts, evidence, and implications. The Academy of Management Review, 201, 65–91. Retrieved from:http://www.jstor.org/stable/ 258887.

Enoch, M.-A., Shen, P.-H., Xu, K., Hodgkinson, C., & Goldman, D. (2006). Using ancestry-informative markers to de<sup>fi</sup>ne populations and detect population strati<sup>fi</sup>cation. Journal of Psychopharmacology, 20(4), 19–26.

Francalanza, C., & Buttigieg, E. (2016). Maltese certi<sup>fi</sup>ed public accountants and whistle-blowing: Traits, in<sup>fl</sup>uences and propensity. Journal of Applied Accounting Research, 173, 262–284. Retrieved from: http://www. emeraldinsight.com/doi/abs/10.1108/JAAR-09-2013- 0062.

Freeman, R. E. (1984). Strategic management: A stakeholder approach. Boston: Pitman.

Gengler, C., & Reynolds, T. J. (1995). Consumer understanding and advertising strategy: Analysis and translation of laddering data. Journal of Advertising Research, 35(4), 19–33.

Gregor, S., & Hevner, A. (2013). Positioning and presenting design science reseach for maximum impact. MIS Quarterly, 37(2), 337–355.

Gregory, R. W., & Muntermann, J. (2014). Research note —heuristic theorizing: proactively generating design theories. Information Systems Research, 25(3), 639– 653.

Grudin, J. (1991). Interactive systems - bridging the gaps between developers and users. Computer, 24(4), 59–69. Retrieved from <Go to ISI>://A1991FE92800005

Hänninen, J., Tuunanen, T., & Vartiainen, T. (2015, August 13th-15th).Value co-creation for cyber-physical systems in mining and construction industry. American Conference on Information Systems (AMCIS), Puerto Rico. Atlanta, USA: Association for Information Systems.

Hevner, A., March, S. T., & Park, J. (2004). Design research in information systems research. MIS Quarterly, 28(1), 75–105.

Holmström, J., & Sawyer, S. (2011). Requirements engineering blinders: Exploring information systems developers’ black-boxing of the emergent character of requirements. European Journal of Information Systems, 20(1), 34–47.

Holtzblatt, K., & Beyer, H. (1993). Making customer-centered design work for teams. Communications of the ACM, 36(10), 93-103. Retrieved from <Go to ISI>:/ A1993LZ71500016

Kara, A., & Kaynak, E. (1997). Markets of a single customer: Exploiting conceptual developments in market segmentation. European Journal of Marketing, 3111/12, 873–895. Retrieved from: http://www.emeraldinsight. com/doi/abs/10.1108/03090569710190587.

Keil, M., Mann, J., & Rai, A. (2000). Why software projects escalate: An empirical analysis and test of four theoretical models. MIS Quarterly, 24(4), 631–664.

Kelly, G. (1955). The psychology of personal constructs. New York: Norton.

Kim, H. N., Smith-Jackson, T. L., & Nam, C. S. (2013). Elicitation of haptic user interface needs of people with low vision. International Journal of Human-Computer Interaction, 29(7), 488–500.

Lamb, R. (2006, August 4-6). Alternative paths toward a social actor concept. the Twelfth Americas Conference on Information Systems, Acapulco. Atlanta, USA: Association for Information Systems.

Lamb, R., & Kling, R. (2003). Reconceptualizing users as social actors in information systems research. MIS Quarterly, 27(2), 197–235.

Lilien, G. L., Morrison, P. D., Searls, K., Sonnack, M., & Von Hippel, E. (2002). Performance assessment of the lead user idea-generation process for new product development. Management Science, 48(8), 1042–1059. Retrieved from <Go to ISI>://000177887400006

Lusch, R. F., & Nambisan, S. (2015). Service innovation: A service-dominant logic perspective. MIS Quarterly, 39 (1), 155–175.

Macionis, J. J., & Gerber, L. M. (2010). Sociology (seventh canadian ed.) upper saddle river. Canada, NJ: Pearson Education Canada.

Maedche, A., Morana, S., Schacht, S., Werth, D., & Krumeich, J. (2016). Advanced user assistance systems. [Journal Article]. Business & Information Systems Engineering, 58(5), Retrieved from, 367–370.

Mathiassen, L., Saarinen, T., Tuunanen, T., & Rossi, M. (2007). A contingency model for requirements development. Journal of Association of Information Systems, 8 (11), 569–597.

Michailakis, D. (2003). The systems theory concept of disability: One is not born a disabled person, one is observed to be one. Disability & Society, 18(2), Retrieved from, 209–229.

Mitchell, R. K., Agle, B. R., & Wood, D. J. (1997). Toward a theory of stakeholder identi<sup>fi</sup>cation and salience: De<sup>fi</sup>ning the principle of who and what really counts. The Academy of Management Review, 224, 853–886. Retrieved from: http://www.jstor.org.ezproxy.library. unlv.edu/stable/259247.

Molin-Juustila, T., Kinnula, M., Iivari, N., Kuure, L., & Halkola, E. (2015). Multiple voices in ICT design with children–A nexus analytical enquiry. Behaviour & Information Technology, 34(11), 1079–1091.

Montazemi, A. R., & Conrath, D. W. (1986). The use of cognitive mapping for information requirements analy sis. MIS Quarterly, 10(1), 45–56.

Moseley, W. (2000). Requirements elicitation for an intelligent software test environment for the physically challenged. Proceedings of the 5th international conference on Intelligent user interfaces. New York, NY: ACM.

Murugami, M. W. (2009). Disability and identity. Disability Studies Quarterly, 29(4). Retrieved from: http://dsq-sds. org/article/view/979/1173

Neill, C. J., & Laplante, P. A. (2003). Requirements engineering: The state of the practice. IEEE Software, 20(6), 40–45.

Olson, E. L., & Bakke, G. (2001). Implementing the lead user method in a high technology <sup>fi</sup>rm: A longitudinal study of intentions versus actions. Journal of Product Innovation Management, 18(6), 388–395. Retrieved from <Go to ISI>://000172750100005

Pe<sup>f</sup>ers, K., & Dos Santos, B. (1996). Performance e<sup>f</sup>ects of innovative it applications over time. IEEE Transactions on Engineering Management, 43(4), 381–392.

Pe<sup>f</sup>ers, K., Gengler, C., & Tuunanen, T. (2003). Extending critical success factors methodology to facilitate broadly participative information systems planning. Journal of Management Information Systems, 20(1), 51–85.

Pe<sup>f</sup>ers, K., & Tuunanen, T. (2005). Planning for IS applications: A practical, information theoretical method and case study in mobile <sup>fi</sup>nancial services. Information & Management, 42(3), 483–501.

Pe<sup>f</sup>ers, K., Tuunanen, T., Rothenberger, M., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45–78.

Pervin, L. A. (1993). Personality theory and research (6th ed.). New York, NY: John Wiley & Son, Inc.

Peters, C., Maglio, P., Badinelli, R., Harmon, R. R., Maull, R., Spohrer, J. C., . . . Demirkan, H. (2016). Emerging digital frontiers for service innovation. Communications of the Association for Information Systems, 39(1), 136–149.

Petervary, T. (2016). Language, ideology and power in contemporary Ireland (NUI Galway PHD Thesis.

Pitts, M. G., & Browne, G. J. (2007). Improving requirements elicitation: An empirical investigation of procedural prompts. Information Systems Journal, 17(1), Retrieved from <Go to ISI>://WOS:000244063700005, 89–110.

Pitula, K., & Radhakrishnan, T. (2011). On eliciting requirements from end-users in the ICT4D domain. Requirements Engineering, 16(4), 323–351.

Potter, L. E. 2007. The Information Technology Gap: Exploring the Factors That Potentially Separate and Di<sup>f</sup>erentiate It Professionals and Users. In School of Information & Communication Technology Grifith (pp. 287). Australia: Gri<sup>fi</sup>th University.

Przybilski, M., & Tuunanen, T. (2007). From rich user requirements to system requirements. PACIS 2007 Proceedings, p 34. Atlanta, USA: Association for Information Systems.

Reynolds, T. J., & Gutman, J. (1988). Laddering theory, method, analysis, and interpretation. Journal of Advertising Research, 28(1), 11–31.

Robey, D., & Azevedo, A. (1994). Cultural analysis of the organizational consequences of information technology. Accounting, Management and Information Technologies, 4(1), 23–37.

Rogers, E. M. (1976). New product adoption and di<sup>f</sup>usion. Journal of Consumer Research, 2, 290–301.

Rogers, E. M. (1995). Difusion of innovations (4th ed.). New York: The Free Press.

Rosenkranz, C., Charaf, M. C., & Holten, R. (2013). Language quality in requirements development: Tracing communication in the process of information systems development. Journal of Information Technology, 28(3), Retrieved from <Go to ISI>:// WOS:000322925900003, 198–223.

Rosenkranz, C., Vranesic, H., & Holten, R. (2014). Boundary interactions and motors of change in requirements elicitation: A dynamic perspective on knowledge sharing. Journal of the Association for Information Systems, 15(6), 306–345. Retrieved from <Go to ISI>:// WOS:000339385900001

Rosman, K. (2014). When the female customer perplexes techie male CEOs. The Wall Street Journal, B1–B7. New York, NY: Dow Jones & Company, Inc., Retrieved from:

https://www.wsj.com/articles/when-the-female-custo mer-perplexes-techie-male-ceos-1406071549

Rossi, M., & Tuunanen, T. (2010). A method and tool for rapid consumer application development. International Journal of Organisational Design and Engineering, 1(1–2), 109–125.

Salganik, M. J., & Heckathorn, D. D. (2004). Sampling and estimation in hidden populations using respondent-driven sampling. Sociological Methodology, 34(1), 193–240.

Schloegel, U., Stegmann, S., Maedche, A., & Van Dick, R. (2016). Reducing age stereotypes in software development: The e<sup>f</sup>ects of awareness- and cooperation-based diversity interventions. Journal of Systems and Software, 121, 1–15. Retrieved from: http://www.sciencedirect. com/science/article/pii/S0164121216301352.

Sonnenberg, C., & Vom Brocke, J. (2012). Evaluations in the Science of the Arti<sup>fi</sup>cial – Reconsidering the Build-Evaluate Pattern in Design Science Research. In Pe<sup>f</sup>ers K., Rothenberger M., Kuechler B. (Eds.), Design Science Research in Information Systems. Advances in Theory and Practice. DESRIST 2012. Lecture Notes in Computer Science (Vol. 7286, pp. 381–397). Berlin, Heidelberg: Springer. doi:10.1007/978-3-642-29863-9\_28

Sustar, H., Pfeil, U., & Zaphiris, P. (2008). Requirements elici tation with and for older adults. IEEE Software, 25(3), 16–17.

Tait, P., & Vessey, I. (1988). The e<sup>f</sup>ect of user involvement on system success: A contingency approach. MIS Quarterly, 12(1), 91–108.

Tiwana, A., & Keil, M. (2006). Functionality risk in information systems development: An empirical investigation. IEEE Transactions on Engineering Management, 53(3), 412–425.

Tremblay, M. C., Hevner, A., & Berndt, D. J. (2010). Focus groups for artifact re<sup>fi</sup>nement and evaluation in design research. Cais, 26, 27.

Tuunanen, T. (2003). A new perspective on requirements elicitation methods. JITTA: Journal of Information Technology Theory & Application, 5(3), 45–62.

Tuunanen, T. (2005). Requirements Eliciation for Wide Audience End-Users (PhD.). Helsinki School of Economics, Helsinki.

Tuunanen, T., Bragge, J., Häivälä, J., Hui, W., & Virtanen, V. H. (2011). A method for recruitment of lead users from virtual communities to innovate it enabled services for consumers in global markets. Pacific Asia Journal of the Association for Information Systems, 3(2), 3.

Tuunanen, T., & Govindji, H. (2016). Understanding <sup>fl</sup>ow experience from users’ requirements. Behaviour & Information Technology, 35(2), 134–150.

Tuunanen, T., & Kuo, I.-T. (2015). The e<sup>f</sup>ect of culture on requirements: A value-based view of prioritization. European Journal of Information Systems, 24(3), 295– 313.

Tuunanen, T., Myers, M., & Cassab, H. (2010). A conceptual framework for consumer information systems development. Pacific Asia Journal of the Association for Information Systems, 2(1), 5.

Tuunanen, T., Pe<sup>f</sup>ers, K., & Gengler, C. (2004). Wide Audience Requirements Engineering (WARE): A practical method and case study. Helsinki: Helsinki School of Economics.

Tuunanen, T., Pe<sup>f</sup>ers, K., Gengler, C., Hui, W., & Virtanen, V. (2006). Developing feature sets for geographically diverse external end users: A call for value-based preference modeling. JITTA: Journal of Information Technology Theory & Application, 8(2), 41–55.

Tuunanen, T., & Przybilski, M. (2014). Domain speci<sup>fi</sup>c case tool for ict-enabled service design. System sciences (HICSS), 2014 47th Hawaii International Conference on.

Tuunanen, T., & Rossi, M. (2004). Engineering a method for wide audience requirements elicitation and integrating it to software development. System sciences, 2004. Proceedings of the 37th Hawaii International Conference on System Sciences, Big Island, HI, USA. doi:10.1109/HICSS.2004.1265420

Venable, J., Pries-Heje, J., & Baskerville, R. (2012). A comprehensive framework for evaluation in design science research. In K. Pe<sup>f</sup>ers, M. Rothenberger, & B. Kuechler, (Eds.), 7th International Conference on Design Science Research in Information Systems (DESRIST 2012) (pp. 423-438). Las Vegas, USA: Springer-Verlag.

Venkatesh, V., Thong, J. Y., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the uni<sup>fi</sup>ed theory of acceptance and use of technology. MIS Quarterly, 36(1), 157–178.

Viller, S., & Sommerville, I. (1999, 7-11 June). Social analysis in the requirements engineering process: From ethnography to method. 4th IEEE International Symposium on Requirements Engineering, Limerick, Ireland.

Von Hippel, E. (1986). Lead users: A source of novel product concepts. Management Science, 32(7), 791–805.

Ward, J. H., Jr... (1963). Hierarchical grouping to optimize an objective function. Journal of the American Statistical Association, 58, 236–244.

Willette, J. M. (2016). A phenomenological study of gay male undergraduate college students’ experiences at a Jesuit Catholic university. PhD Dissertation. Colorado State University.

Wing, J. W., Andrew, T. N., & Petkov, D. (2015). a systemic framework for improving clients’ understanding of software requirements. Twenty-Third European Conference on Information Systems, Münster. Atlanta, USA: Association for Information Systems.

Winter, R. (2008). Design science research in Europe. European Journal of Information Systems, 17(5), 470– 475.

## Appendix 1 Overview of the DSR programme

Our study represents a form of DSR in which, over the course of several years, we designed or adapted and implemented RA techniques for client organisations in Europe, North America, and the Asia Paci<sup>fi</sup>c. The e<sup>f</sup>orts described here involved engaging <sup>fi</sup>ve client organisations and more than 200 subjects in four di<sup>f</sup>erent countries to solve client RA problems during the years 1999–2007. We evaluated the results, and then, as opportunities arose, we applied lessons learned in one client case to design a better solution for another. Consequently, this paper presents a programme of DSR that encompasses several individual projects that cumulatively led to the development of a nascent design theory. In below, we <sup>fi</sup>rst present the descriptions of each <sup>fi</sup>ve studies in linear order and then provide the overview of the whole DSR programme.

The research programme began when the Rutgers University, Camden Provost engaged us in 1999 to conduct a planning study to discover a set of new systems applications with high value across the campus. Rutgers Camden is a small (16 ha) urban campus of the state university. We used this project as an opportunity to show that we could engage in a RA process in which participants across administrative and professional occupations were able to think strategically, instead of proposing new services that narrowly bene<sup>fi</sup>ted themselves. We invited participation from 18 employees, the provost, an associate provost, 2 deans, 11 other administrators, and 3 faculty members.

The next step was when Digia (Plc., NASDAQ OMX HELSINKI) Chairman and CEO Pekka Sivonen approached us in 2001 with a request to identify a set of “killer cocktails” for mobile <sup>fi</sup>nancial services – services that would be so well embraced by customers that they would ensure the accep tance of yet-to-be-launched next generation smartphones, just as VisiCalc had ensured the acceptance of the personal computer for business in the early 1980s. Digia had conducted strategic analyses of the potential market and decided that it would be lucrative for the <sup>fi</sup>rm to develop applications for use with the new mobile devices. Researchers worked with prototypes and sketches of the new devices, as well as ideas for what the technology might enable consumers to do. Our task was to determine if we could elicit ideas from potential customers for feasible applications using these devices, even though they had never used the devices or any artefacts with equivalent functionality.

In 2003, we were engaged by the business development team at HS (Sanoma Plc., NASDAQ OMX HELSINKI), Helsinki’s major newspaper and Finland’s leading advertising media, to develop the functional requirements for version 2.0 of Medianetti, a Web-based system that allows customers to design and purchase display advertising for the newspaper, its Nyt Weekly Supplement, and its classi-<sup>fi</sup>ed online service. Medianetti targets six customer segments: regular and infrequent small-scale advertisers, medium-scale and large-scale advertisers, ad agencies, and internal users. Version 1.0 of the service was ready for release, but no customers had seen it.

Nokia (Plc., NASDAQ OMX HELSINKI) was the key participant of a 2004–2007 consortium study that included more than 20 Finnish organisations that were interested in digital marketing. Our part was to ascertain how consumers might want to use availability or activity status information, which Nokia de<sup>fi</sup>ned as “presence”, in new mobile applications. Customers would be able to include presence status in their mobile phone contact list, enabling subscribers to the list to know their availability for a voice call or other interaction. Presence information was a technology that was not available to the public at that time, which required both a special smartphone that Nokia manufactured at the time and a server-side technology to support the mobile services. Consequently, the <sup>fi</sup>rms had only a limited understanding of which potential application features would be worthwhile or how that might di<sup>f</sup>er in various cultures or locations around the world.

Finally, at the RNZFB, we focused on the special needs that people who are blind have to enable participation in RA activities, as well as the importance of their participation, i.e., whether blind customers require di<sup>f</sup>erent system functionality for mobile services than sighted people do. What’s more RNZFB tasked us to think outside of the current technological “box” in developing innovative service concepts for blind and visually impaired smartphone users. This study was carried out in New Zealand and Germany in 2006 with the help of the RNZFB and Trierische Tonpost, a monthly spoken magazine for vision-impaired German subscribers. To recruit participants, we employed communications channels of the RNZFB in New Zealand and Trierische Tonpost in Germany.

As a result of working in di<sup>f</sup>erent contexts, with di<sup>f</sup>erent problems, in <sup>fi</sup>ve organisations, the overall DSR programme is complex. To provide the reader with a mental model of this work, we mapped it to the DSRM in Figure 1. The <sup>fi</sup>gure shows how we worked through identifying the problem, de<sup>fi</sup>ning a design objective, identifying the appropriate theory to apply, designing a solution, demonstrating it through our work with the client, and evaluating the e<sup>fi</sup>cacy of the design. It identi<sup>fi</sup>es logical connections among activities and projects with the clients, as well as iteration across projects that resulted when evaluation steps identi<sup>fi</sup>ed limitations in design activities or outcomes.

The <sup>fi</sup>gure maps elements of each project, beginning with the one at Rutgers University, against key elements of the DSRM, including problem identi<sup>fi</sup>cation, objectives, design, demonstration, and evaluation. It also identi<sup>fi</sup>es a key actualising element, theory, to connect a solution objective to design in each project.

For four of the projects, dashed arrows indicate e<sup>f</sup>ective feedback between evaluation in one project and initiation of or techniques employed in the next project. At Rutgers University, we realised that clustering concepts with Ward’s technique resulted in lost information, as chains of data from individual participants were separated in di<sup>f</sup>erent clusters. We, therefore, implemented a thematic clustering technique for our work at HS. Feedback from managers and developers at Rutgers also told us that we needed to provide much richer information in the results, so at HS we provided our clients with an interactive tool with several levels of aggregation, from top-level models down to individual interview audio recordings.

As we transitioned from Rutgers to the Digia project, we realised that we needed to attend to the ability of participants to e<sup>f</sup>ectively engage in RA activities involving not yet available technology. Our task at Digia was to develop innovative digital services for devices that would leapfrog the technological possibilities of its time, so we needed participants’ who would be motivated and able to meaningfully imagine preferences for products and services that would use technologies about which they had no prior experience. We incorporated non-representative samples of experts and lead users to resolve this problem.

Client feedback at HS informed us of the need to di<sup>f</sup>erentiate among di<sup>f</sup>erent subpopulations, so we worked to identify and separately analyse subpopulations in our study at Nokia. Our experience at Nokia led us to consider how to accommodate di<sup>f</sup>erent kinds of participation barriers with RNZFB. At Digia, Rutgers, and HS, we were motivated to seek consensus about the meaning and value of features and concepts and so employed media richness and information synchronicity theory to achieve e<sup>f</sup>ective preference communication in data collection steps and concordant understanding in analytic steps.

![](/api/attachments/UBMA46TG/fulltext/images/4dfa2a29c35bad2d90a3d154066537d70a36ecf490e4e26060a0bffa3ed8cff9.jpg)  
PTRA research programme mapped to the DSRM (Pe<sup>f</sup>ers et al., 2007).

## Appendix 2 Exemplar ladder chain from the HS case

<table><tr><td></td><td>Interview 12, chain 6</td></tr><tr><td>Participant segment</td><td>Infrequent, small-scale user</td></tr><tr><td>Stimulus</td><td>Customer portfolio</td></tr><tr><td>Attributes</td><td>I could check out own reservationsYou would get a notification of your own reservations → Branch to Chain 7It would remind me to confirm advance reservations</td></tr><tr><td>Consequences</td><td>I could get a notificationI could conform or cancel through itWithin limits of working time</td></tr><tr><td>Values/goals</td><td>It would free my assistants&#x27; memory capacity to something elseUse of time</td></tr></table>

## Appendix 3 Exemplar network map from the HS case

The network map of the “agility of real time” theme from the HS case, showing <sup>fi</sup>rst- and second-level subthemes and links among <sup>fi</sup>rst-level subthemes, is shown in Figure 2 in Appendix 3. Unshaded boxes on the left refer to attributes and features, and shaded boxes refer to consequences.

## Appendix 4 Context-situated RA method for HS

The case of our RA e<sup>f</sup>orts at HS newspaper (cf. Appendix 1 for details) included a variety of states, contextual factors, and their association with the application of speci<sup>fi</sup>c technical solutions. This is summarised in Table 5. We <sup>fi</sup>rst identi<sup>fi</sup>ed the IMAGINE state at HS because our client wanted to target clients that had never previously placed or designed a piece of display advertisement with the system. Consequently, we expected them to have di<sup>fi</sup>culty imagining the potential bene<sup>fi</sup>ts to them of an application intended to solve display advertising design problems. This motivated us to seek out potential lead users among this population (see step 1 in below).

Among the large and small customers, advertising agencies, and many di<sup>f</sup>erent roles inside the <sup>fi</sup>rm, we could see that potential participants in the use of a new system had very di<sup>f</sup>erent mental models of its purposes and use (the BMM state). To reconcile these di<sup>f</sup>erent mental models, we required data and analysis that would enable downstream participants in the process to acquire detailed understanding of the preferences and reasoning. This led us to employ laddering interviews (see step 2.1 and Appendix 2) with participants to collect preference and reasoning data and thematic clustering with network modelling (see step 2.2 and Appendix 3) to present the preferences and reasoning.

To achieve concordance among participants (CONC), i.e., everyone understanding the meaning of participant preferences and reasoning, as well as their implications for system design, we employed several techniques intended to facilitate deep understanding of the information among managers and system designers. We developed a presentation tool to portray the preference and reasoning information at several levels of aggregation, so that managers and engineers could view the preference data at di<sup>f</sup>erent levels. We conducted a workshop (see step 3.1) among high-level managers and system designers to help them understand how to use the data and analysis.

Next, we developed a business report (see steps 3.2–3) to present and communicate the prioritised system features to middle and top management. Finally, a 3-year release road map (step 3.4) was developed to present the functionality to be released in scheduled updates and its expected bene<sup>fi</sup>ts for the <sup>fi</sup>rm and its customers. In this particular case, the ABIL and IE&A states were not identi<sup>fi</sup>ed and related techniques were not needed or applied. In below, we provide a detailed step-by-step description of the PTRA application process.

![](/api/attachments/UBMA46TG/fulltext/images/bafcf345dbe99a2bb931fa38d157cb8ee0ef9808857cf9c05240dd6430ac1635.jpg)  
Exemplar network map from the HS case.

## Step 1: IMAGINE activities – participant selection

We began the data gathering process by identifying project participants. We interviewed 30 people for this project. We wanted our sample to include the <sup>fi</sup>ve customer segments for the system that were identi<sup>fi</sup>ed by the <sup>fi</sup>rm, as well as to include potential “lead users”, i.e., users who are likely to be willing to quickly embrace new features and systems.

## Step 2.1: BMM activities – data collection

The project steering committee for Medianetti version 2.0 had done some preliminary analysis as part of the project feasibility study. They were able to provide us with a list of seven key areas in which they anticipated focusing revisions for version 2.0. The list is shown below. We used this list to provide stimuli in our interviews with participants.

● Customer portfolio

● Request for free space

● Campaign planning

● Solution con<sup>fi</sup>guration

● Filing ads

● Preparing picture ads

● Advertising archive

We interviewed each of the participants individually and in person. Participants were presented with a list of the stimuli and asked to rank order them in terms of their importance to them. Then, one at a time, for the two highest ranked stimuli, the interviewer asked the participant to describe a feature that would be important to him/her. He then asked, “Why would that be important to you?” to elicit consequences that the participant expected from the feature. He continued with a series of “why would that be important?” questions to elicit a chain of consequences the participant expected to result from the feature and values or objectives that were furthered by the feature. To elicit more concrete system attributes, he asked the participant a series of questions, such as, “What would there be about the system that would make you think that it would do that?” This data was recorded in the notes as a series of chains. An example chain is shown in Appendix 1.

The 30 interviews resulted in the collection of 244 individual chains of data, an average of 8.13 per participant, containing 2566 individual statements.

## Step 2.2: BMM activities – model aggregation

In total, 244 chains containing 2566 distinct statements would be di<sup>fi</sup>cult, if not impossible, for decision makers and designers to interpret directly. It was important to aggregate this data to produce a meaningful, but smaller, set of rich, uni<sup>fi</sup>ed aggregated models that managers and designers could grasp. To accomplish this, we devised a technique to cluster the chains qualitatively into themes.

The objective was to create the top layer aggregated representation of participant models: network maps. In an all-day session, two analysts discussed the 244 chains and agreed that <sup>fi</sup>ve conceptual themes could capture all of the chains. The found themes represent di<sup>f</sup>erent kinds of user needs. The two analysts worked independently to sort the 244 chains into the themes and then went through the chains together to resolve di<sup>f</sup>erences by consensus. Later, a third analyst independently created themes and sorted the chains.

Next, we created the network maps by transforming the chains clustered into each theme into a network map. These maps contained features (attributes), reasons customers saw them as necessary or interesting (consequences), and <sup>fi</sup>nally, goals or values driving the customers. Next, the analysts examined the chains in each of the themes to determine, interpretively, what subthemes could be found in them.

Context-situated RA method for HS.

<table><tr><td>Principle</td><td>State</td><td>Action</td><td>Contextual factors</td><td>Outcome</td></tr><tr><td>Ability to imagine beneficial functionality</td><td>Motivation and experience affect ability to imagine new technology benefits (IMAGINE)</td><td>Snowball lead user recruitment from different customer segments.</td><td>Different customer segments of HS advertisers. The biggest newspaper in the Nordic countries at the time.</td><td>Non-representative sample of key customer segments.</td></tr><tr><td>Knowledge capture</td><td>Beliefs and mental models affect functional preferences and value (BMM)</td><td>Data collection with laddering interviews with selected potential customers. Model aggregation with thematic clustering of the data set.</td><td>Potential users of a new system had very different mental models of its purposes and use as customers varied from media offices to small businesses and corporate clients.</td><td>High-level network models, individual chains, and audio recordings were implemented together in a spreadsheet and packaged on a DVD disc for use by decision makers and designers.</td></tr><tr><td>Convergent understanding</td><td>Variance in understanding of the value of functionality across populations (CONC)</td><td>Workshop to communicate the requirements, and the reasoning and values behind them. Survey feedback from potential customers to prioritise the system features.</td><td>Developers, managers, and top-level management at the corporate level in a leading media group in the Nordic countries.</td><td>Business Report to present and communicate the prioritised system features. Three-year release road map for the system.</td></tr><tr><td>Participation ability</td><td>Abilities affect functional preferences and participation costs (ABIL)</td><td>Not applied.</td><td>Not applied.</td><td>Not applied.</td></tr><tr><td>Subpopulation knowledge capture</td><td>Identities, environments, and affiliations affect preferences (IE&amp;A)</td><td>Not applied.</td><td>Not applied.</td><td>Not applied.</td></tr></table>

These were recognised by consensus. Finally, they developed graphical network models through rounds of sketches.

These graphical network models were implemented as the top level in a three-dimensional electronic spreadsheet-based presentation tool that included links to allow the user to drill down from each model to the chains from which it was constructed, and further down to listen to the original data collection, i.e., recorded segments of the original participant statements. One such model is shown in Appendix 2. It describes the Agility of Real Time theme. On the left, the drawing refers to system attributes suggested by participants. Attribute consequences are shown in the centre. Linked participant goals and values are shown on the right. The themes are subdivided into two levels of subthemes. For example, in the “Agility of Real Time” theme, “Immediate Feedback” is a higher-level subtheme, and “Order Con<sup>fi</sup>rmation” is a second-level subtheme or “feature.” The <sup>fi</sup>rst-level subthemes are connected by lines to indicate links among attributes, consequences, and values that were found in the original chains collected from participants.

Each subtheme is annotated with links, e.g., “R52”, to selected key statements shown in the context of their original chains. This is the second level in the presentation tool. Figure 2 shows an example of one chain from the Agility of Real Time theme. From this chain, a user can click on selected key statements to hear digital audio recordings of original participant statements from the data collection interview, the tool’s third level.

The high-level network models, individual chains, and audio recordings were implemented together in an electronic spreadsheet and packaged on a DVD for use by decision makers and designers. The <sup>fi</sup>nished presentation tool contained 824 MB of data.

## Step 3.1: CONC activities – workshop

We used the presentation tool to facilitate consensusreaching activities that included a manager/developer workshop and a post-elicitation user survey. Our objectives included presenting the tool to managers and developers so that they understood that it was an expression of customer preferences and reasoning, training them in its use so that they understood how to use it to obtain rich information, and measuring the importance or value of the requirements that we had elicited from the user participants.

The workshop was held on a single day in March 2003. Workshop participants included both managers and developers, including the project manager for project development, a marketing director, a developer, a system manager, a business development manager, and the Medianetti project manager. To help workshop participants understand the tool and become familiar with it, we presented the tool and gave them tasks to complete. Starting slowly initially, the participants soon grasped the idea of the tool and could work quickly.

At the end of the workshop, we surveyed the participants about their views of the workshop’s usefulness and the features presented in the tool. The results suggest that the workshop participants were well satis<sup>fi</sup>ed that they now understood the goals of the customers as presented in the presentation tool. One participant wrote, “The workshop showed us that we are going in the right direction and it helped us to formulate the features better.” Another expressed her happiness at being able to do something and said that the tool provided an easy and expressive way to describe and analyse the requirements. In general, the participants seemed very happy with the richness and interactive design of the presentation tool.

## Step 3.2: CONC activities – survey

The next task was to conduct a post-elicitation survey of potential customers to determine the relative value of the requirements items that we had acquired and, secondarily, to validate the collected data. We conducted the post-elicitation survey using an independent sample of

Survey results.

<table><tr><td>Rank</td><td>Feature</td><td>Description reasoning</td><td>Value score</td><td>Subtheme</td><td>Theme map</td></tr><tr><td>1.</td><td>Order confirmation</td><td>It makes it easier to make and modify plans, to react to events. This leaves me better in control of the process, and that helps me get a better return on my advertising investments.</td><td>120</td><td>Immediate feedback</td><td>Agility of Real Time</td></tr><tr><td>2.</td><td>Ability to make changes in real time/flexible in time and place</td><td>I can fix mistakes or modify plans easier. I can react to events easier. I can save time by working anywhere. This helps me to get a better return on my advertising investment, and it improves my own personal productivity.</td><td>80</td><td>Ability to make changes in real time</td><td>Agility of Real Time</td></tr><tr><td>3.</td><td>Receipt for submitted material</td><td>I can fix mistakes or modify plans easier. I can react to events easier. I can save time by working anywhere. This helps me to get a better return on my advertising investment, and it improves my own personal productivity.</td><td>77</td><td>Immediate feedback</td><td>Agility of Real Time</td></tr><tr><td>4.</td><td>Ability to remove ads</td><td>I can fix mistakes easier and I would be able to accurately fix specific ads and campaigns. This would save time for me and would enable me to react to events. This helps me to get a better return on my advertising investment and it improves my own personal productivity.</td><td>67</td><td>Ability to make changes in real time</td><td>Agility of Real Time</td></tr><tr><td>5.</td><td>Reusing material and making repetitions</td><td>I would be able to reuse material stored in the personal archive, and this would empower me to create ads easier but at the same time keep the consistency of style and content. This would mean better, faster, and cheaper ad creation that would save money and at the same time enable me to do better creative campaigns.</td><td>47</td><td>Personal archive</td><td>Ad Creative Work</td></tr><tr><td>6.</td><td>Circulation, readership information, etc.</td><td>I would like to know more about reach information in order to get more effective placement for my ads or for finding the best value for my ads purchases. This would enable me to more easily evaluate campaign performance and would make it possible for me to be more flexible and create better campaigns. These would all save me time and money.</td><td>44</td><td>Reach information</td><td>Research-Campaign Planning</td></tr><tr><td>7.</td><td>Competitors&#x27; ads</td><td>I would like to see what my competitors are doing in advertising to have more knowledge of effective campaigns and get creative ideas. This would enable me to more easily evaluate campaign performance and would make it possible for me to be more flexible and create better campaigns. These would all save me time and money.</td><td>43</td><td>Ad library</td><td>Research-Campaign Planning</td></tr><tr><td>8.</td><td>Ability to make reservations</td><td>I would like to reserve advertising space online and in real time. This would enable me to do things on my own time. This would also enable me to plan more easily, be more in control of the process, and increase my personal productivity. This would, in the end, result in higher income or more personal free time.</td><td>41</td><td>Ability to make changes in real time</td><td>Agility of Real Time</td></tr><tr><td>9.</td><td>Helpdesk chat</td><td>I would not need to wait hours to receive an answer for a specific question, and I could continue working. This would mean better personal productivity and customer satisfaction.</td><td>39</td><td>Immediate feedback</td><td>Agility of Real Time</td></tr><tr><td>10.</td><td>Who reads sections of newspaper</td><td>I would like to know who is reading specific sections of the newspaper in order to get more effective placement for my ads or for find the best value for my ads purchases. This would enable me to more easily evaluate campaign performance and would make it possible for me to be more flexible and create better campaigns. These would all save me time and money.</td><td>36</td><td>Reach information</td><td>Research-Campaign Planning</td></tr></table>

33 people from the same end-user segments as previously. We contacted each survey participant by telephone and then three times by email. This resulted in 24 survey answers with one partially completed answer (73% response rate). We paid each of the participants an incentive of 50€ in the form of either a gift certi<sup>fi</sup>cate or a charity donation in their name.

The results of the survey are summarised in Table 1, which was intended as part of a report to the managers and developers. The survey value score represents a weighted value, aggregated across the participants. It is a sum of weighted participant rankings, where a participant’s highest ranked feature was awarded 10 points, the next highest 9 points, and so on. On the right, the (<sup>fi</sup>rstlevel) subtheme, e.g., “Immediate Feedback” in the <sup>fi</sup>rst item, is indicated. In addition, for each feature, the table also reports a summary of participants’ reasons for wanting the feature and the <sup>fi</sup>rst-level theme, or network map, to which it belongs. Survey respondents also rated the <sup>fi</sup>ve top-level themes. The results are shown in Table 2. The most important theme, or map, was clearly the Agility of Real Time, followed by Budget

Management and Research-Campaign Planning in a near tie with each other.

## Step 3.3: CONC activities – business report

Based on the results of our study, we made the following recommendations in a business report to the <sup>fi</sup>rm: focus resources to develop features mentioned in the top 10 features list (Table 6) and in the top three themes (Table 7). These are the (Pe<sup>f</sup>ers et al., 2007) features and themes most valued by the customers.

Weighted total ratings, based on ratings by 33 <sup>Table 7.</sup>participants, where themes were awarded 5 points when ranked <sup>fi</sup>rst, 4 points when rated second, etc.

<table><tr><td>Theme</td><td>Mean of inverted ranks</td></tr><tr><td>Agility of Real Time</td><td>40.6</td></tr><tr><td>Budget Management</td><td>21.4</td></tr><tr><td>Research-Campaign Planning</td><td>20.4</td></tr><tr><td>Ad Creative Work</td><td>15.3</td></tr><tr><td>Communication</td><td>8.6</td></tr></table>

## Step 3.4: CONC activities – release road map

Using the presentation tool, the Medianetti project team developed a feature release road map for Medianetti that described features, priorities, and development schedules for the next three years. It called for the release of version 2.0 by February 2004, version 2.1 in fall 2004, version 2.2 in winter 2004–2005, and version 3.0 in late 2005. Almost all of the features included in the road map can be traced back to the study data; 42 of the 59 functional features were speci<sup>fi</sup>cally recommended in the business report, along with seven that came from other sources.
