---
otero_id: 3818
otero_key: "5QZ4KT7C"
title: "The Design of Social Inclusion Interventions: A Paradox Approach"
authors: "Daniel Curto-Millet; Almudena Cañibano"
year: "2023"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00795"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2023

# The Design of Social Inclusion Inter   ventions: A P   aradox Approach

Daniel Curto-Millet , daniel.curto-millet@ait.gu.se

Almudena Cañibano

, acanibano@escp.eu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# The Design of Social Inclusion Interventions: A Paradox Approach

Daniel Curto-Millet,<sup>1</sup> Almudena Cañibano<sup>2</sup>

<sup>1</sup>University of Gothenburg and Swedish Center for Digital Innovation, Sweden, daniel.curto-millet@ait.gu.se <sup>2</sup>ESCP Business School, Paris, France, acanibano@escp.eu

## Abstract

Are social inclusion and social exclusion opposed? Through a three-year ethnography of an open source civic crowdsourcing platform aiming for generalized social inclusion, we show they are not. We argue that social inclusion and exclusion have a paradoxical relationship: ongoing tensions exist between them, and information systems shape those tensions. We find that design choices have crucial influence over the capacity of information system interventions to include and exclude and propose a framework for designing IS-based social inclusion interventions. The framework encompasses four types of strategies (positive discrimination, integrative oscillation, equitability and iterative inclusivity) for managing the paradoxical link between inclusion and exclusion through IS design. We also present the notion of “collectives” as a new way of thinking about exclusion criteria.

Keywords: Social Inclusion, Social Exclusion, Paradox, Tensions, IS Design, Sociomateriality, Civic Crowdsourcing

Jaime Windeler was the accepting senior editor. This research article was submitted on March 27, 2021 and underwent three revisions. This paper is part of the Special Issue on Technology and Social Inclusion.

## 1 Introduction

Why do so many social inclusion interventions fail? This question, which has troubled researchers, activists, and policy makers alike, created the spark for this paper. Two years after concluding our ethnographic study of Decide Madrid, a highly innovative and ambitious civic crowdsourcing platform, aimed at increasing social inclusion, bitter assessments prevailed. The platform was intended to give executive powers to Madrid’s citizenry: anyone above 16 years old who was a resident of the city could make proposals. If proposals reached 1% of the city’s population in votes, they would become part of the governing party’s agenda. In so doing, Decide Madrid sought to include almost anyone and everyone, both lowering the barriers to effect social change and giving away unprecedented power. When the platform exhibited dwindling participation numbers and only two proposals had passed the threshold, the initial emancipatory technopolitical dreams of inclusion dwindled into a sense of failure.

In this paper, we explore whether the answer to this puzzling situation lies in two interconnected elements: the assumed inverse relation between social inclusion and social exclusion and the underexplored role of IS designs in the social inclusion literature. Social inclusion is defined as the ability of people to fully and meaningfully participate in economic, social, and cultural life (Castells, 2010; Wilson & Secker, 2015), or in society in general (Warschauer, 2002). Conversely, social exclusion is defined by Silver and Miller (2003, p. 3) as a “relational process of declining participation, solidarity, and access.” Latent to these definitions is the idea that by increasing participation one reduces exclusion and vice versa. As such, information systems (IS) interventions are designed to foster social inclusion or reduce social exclusion (Annabi & Lebovitz, 2018; von Hellens et al., 2012; Wilding, 2009) because they are one and the same. However, existing evidence may call this assumption into question (Cornford & Klecun, 2003).

Relying on paradox theory (Lewis, 2000; Putnam et al., 2016; Smith & Lewis, 2011) we question this assumption and propose an alternative paradigm: While seemingly conflicting, social inclusion and social exclusion are interlinked and interreliant. Exclusion is not opposed to inclusion but goes hand in hand with it (Iivari et al., 2018), and ongoing tensions exist between the two. Under this paradigm, it can no longer be assumed that IS interventions both foster inclusion and reduce exclusion in equal measure. We thus ask the question: How do IS influence the tensions between social inclusion and exclusion?

In parallel, how the design of IS contributes to social inclusion has been identified as a key underresearched and critical issue (Olbrich et al., 2015; Trauth, 2013; Trauth et al., 2018). Indeed, social inclusion studies often consider IS as a contextual, generalizable construct, focusing on the outcomes of using or adopting technology. In doing so, they overlook the influence of design choices on social inclusion and how they become entangled with the social (Orlikowski & Scott, 2015; Scott & Orlikowski, 2014), and their societal consequences (Trauth, 2017; Trauth et al., 2018). We follow a sociomaterial approach (Orlikowski & Scott, 2015) to understand IS design choices as encouraging or constraining different relations between the social and the technical. In this sense, IT design choices are not limited to a single material artifact, but can include hardware, software, people, policies, data, and processes as integral components of an information system. (Alter, 2008).

Following Trauth et al.’s (2018) call, we study the practices intimately intertwined with the design of inclusive systems and how design enacts inclusion and exclusion. Elaborating on the assumption that inclusion and exclusion coexist, we specifically ask: What role does an IS design play in managing the tensions between inclusion and exclusion??

We explore these questions through the case of the Madrid city council platform, Decide Madrid. The ambitious project garnered public acclaim, having received the 2018 UN public service award in the category “Making institutions inclusive and ensuring participation in decision-making.”<sup>1</sup> As such, the case can be seen as critical (Goldthorpe, 1968): If exclusions can happen in an IS that has been designed from the ground up to create global inclusion, then it is likely that exclusions will happen in cases that are less careful about social inclusion.

Our analysis offers three key contributions. First, by drawing on the example of Decide Madrid, we bring forth and illustrate the inherent paradoxical tensions between social inclusion and exclusion. Second, we develop a framework to analyze and design IS-based social inclusion interventions considering these paradoxes. The framework, which has important implications for theory and practice, presents four types of strategies for managing the paradoxical link between inclusion and exclusion through IS design (positive discrimination, integrative oscillation, equitability, and iterative inclusivity). Third, we identify the notion of “collectives” (i.e., fleeting groups of people that have shared personal logics in common rather than sociodemographic features such as race, origin, or gender) as a new way of thinking about exclusion criteria, in combination with traditional individual and sociodemographic categorizations.

## 2 Literature Review

This section anchors the study’s research questions in the IS social inclusion literature by raising two interrelated issues: the assumed linear inverse relation between social inclusion and social exclusion and the underdeveloped role of IS design.

Regarding the first, established definitions of social inclusion posit that an increase in participation leads to an increase in inclusion (Warschauer, 2002). Inversely, a decrease in participation leads to an increase in social exclusion (Silver & Miller, 2003). In this sense, the literature makes an implicit assumption of linearity between social inclusion and social exclusion. For example, it has been argued that social exclusion results from a lack of access to technological resources (Díaz Andrade & Techatassanasoontorn, 2020). People cannot participate in society if they cannot connect to the internet. This is a binary perspective that effectively pits the “haves” against the “have nots” and the included against the excluded and creates an implicit value judgment that views technology as a straightforward and uncomplicated solution (Gunkel, 2003; Klecun, 2008). This dichotomous view of social inclusion (Epstein et al., 2011) suggests that increasing social inclusion leads to a decrease in social exclusion and vice-versa. However, existing evidence challenges this assumption.

Deng et al. (2016) found that crowdworkers experienced simultaneous yet contradictory feelings of empowerment and marginalization when interacting with structures that mediated their tasks. Cornford and Klecun (2003, p. 300) proposed that inclusion and exclusion initiatives have an interlinked relation: “while ICTs [information and communication technologies] have the potential to help overcome some forms of exclusion, they may also create new forms or reinforce existing ones” by diminishing opportunities to participate in economic and political life. Social inclusion here cannot transcend social exclusion. Iivari et al. (2018, p. 1043) reported how certain groups became excluded during the implementation of social inclusion initiatives, with exclusion presenting a “dilemma” and “com[ing] hand in hand with inclusion.” As Edwards et al. (2001, p. 425) argued: “traces of exclusion are to be found in the practices of inclusion.” Exclusion, thus, is not the opposite of inclusion (Sorochan, 2016).

These accounts suggest that ongoing tensions exist between inclusion and exclusion: although seemingly opposed, they may actually be complementary, intertwined, and interreliant forces (Lewis, 2000; Putnam et al., 2016; Smith & Lewis, 2011). In this sense, a way forward in exploring the role of IS and social inclusion is to develop a framework that relies on the analysis of paradoxical tensions. Paradoxical tensions are “cognitively or socially constructed polarities that mask the simultaneity of conflicting truths” (Lewis, 2000, p. 761). While, by definition, social inclusion and exclusion would seem to be mutually exclusive, from a paradoxical tension perspective, they would actually be two sides of the same coin. Accordingly, the question is no longer can IS promote social inclusion / reduce social exclusion but rather, how do IS influence the tension between social inclusion and exclusion?

The second aspect of the literature we build on is the underresearched role of IS design in technological interventions and social inclusion. IS and technologies in social inclusion research are often considered to be contextual constructs. They are part of a structure in which various kinds of inequalities are reproduced (Amis et al., 2020). For example, IT-related professions are spaces in which gender diversity could be promoted (Hardey, 2020; Joshi et al., 2017; Windeler et al., 2020). When technologies are considered, these are often backgrounded as technologies “enabling” (Heath & Babu, 2017), “promoting” (Díaz Andrade & Doolin, 2016), or acting as “barriers” (Mervyn et al., 2014) to social inclusion. Interventions are thus also general, involving, for example, upskilling initiatives to develop digital literacy skills (Klecun, 2008). Viewing technology in these general terms has advanced our understanding of the consequences of our growing reliance on digital systems and how these can (re)produce inequalities and relations of dependency (Coleman, 2018).

However, generalizing technology and IS artifacts has major shortcomings. First, it effectively freezes the IS artifact in time and decontextualizes it from grounded social practices, rendering how actors respond to the inclusion/exclusion tensions they encounter invisible. This is problematic because social inclusion and exclusion are processes (Silver & Miller, 2003) that can take place as interventions develop (Iivari et al., 2018). A structural view of the implication of technologies in these processes cannot precisely account for how actors come to understand them nor does it allow for the exploration of the social practices put in place to circumvent or attenuate exclusion.

Second, relying on generalizations can render the myriad choices made when designing IS invisible, obscuring systems’ capacity to include and exclude (Trauth et al., 2018) because policies are ingrained within the technological artifact during the design process (Goldkuhl, 2016). A focus on IS design processes can thus help us understand more precisely how they interact with social practices and how they enact inclusion and exclusion. Relying on the assumption that inclusion and exclusion are not opposed but paradoxical tensions, we ask: What role does IS design play in managing the tension between inclusion and exclusion?

Paradox theory scholars have suggested that tensions are managed through different types of responses (Jarzabkowski & Lê, 2017; Lewis, 2000). Putnam et al. (2016) organized them into three categories: either-or, both-and, and more-than. Either-or responses treat opposing poles as separate, independent phenomena. For instance, selection denies the existence of one of the poles. Both-and responses treat opposing poles as interdependent (Smith & Lewis, 2011). This category includes strategies such as vacillation (alternatively privileging one pole over the other over time) and integration and balance (compromising on a middle ground). More-than responses connect oppositional poles, creating a new relationship between them. This category is exemplified by strategies like connection and dialogue, which involve engaging opposites dynamically, keeping the paradox open. We draw on this categorization to analyze how different IS designs can respond to and manage the tensions between inclusion and exclusion in different ways.

## 3 Case Study and Methodology

This paper is the result of a longitudinal study of Decide Madrid conducted from 2017-2019. Decide Madrid (“You Decide Madrid” in English, Decide for short), is an open source civic crowdsourcing platform created in 2015 by the Madrid city council under the auspices of a newly elected government with roots in the Spanish Occupy movement.<sup>2</sup> Decide is an example of a civic tech platform for organizing participation and collective action (Cardoso et al., 2019) and finding innovative solutions to social issues (Saldivar et al., 2018) (see Appendix A and B for screenshots of the platform and details on its interface).

We analyze the design choices proposed for the platform, how it embedded itself into society, what principles it followed, the expectations it embodied, and the results it achieved. This case is interesting not only because of the unintended consequences of its implementation, but because of its unrealized intentions. Although the former has captured much of our scholarly attention, the latter arguably matters at least as much if there is an important departure between the espoused results and designed intentions (Sen, 2013). While Decide initially attracted massive participation (more than 700,000 votes on proposals), involvement slowly dwindled. Indeed, only two citizen proposals managed to be turned into legislation. More importantly, the tool was not adopted by the people who had participated in the Spanish Occupy movement, even though the designers of the platform were part of the movement. At the center of this challenging adoption was the contested notion of inclusion that the information system constituted, which resulted in a number of initiatives to adapt the technological and the social to better fit each other.

The study followed an inductive approach. Although we believed that Decide would be an interesting platform to study, given its lofty ambitions and the purposeful openness of the platform (both in terms of its development as an open source project as well as an attempt to “open source” the city), there was no set agenda. In addition, we thought it would be important to go into the field with an ethnographic mindset of respecting participants’ agency and study this reflection where it happened. Social inclusion was not one of the expected research outputs. However, its recurrent, frequent, and fraught presence throughout the study called for its analysis. Through the ethnographic approach, this research was situated close to people’s real lives (Trauth, 2017) in that its designers reflected on the platform and its intended objectives.

## 3.1 Data Collection

The data was collected primarily through recurrent participant observation spanning three years (2017- 2019). This longitudinal approach permitted us to capture design intentions and the effects of those designs, as well as the moments of reflection when participants evaluated what happened (Yin, 2003).

These key moments coalesced around reflective events organized by the Madrid innovation lab that directly discussed Decide. The lab is a public organization belonging to the city council. It is a space for political, civic, and cultural experimentation and collaboration that gathers citizens, hackers, social activists, and artists (see Corsín Jiménez and Estalella, 2023, for a detailed history). In total, the first author observed 48 events including hackathons, focus groups, workshops, conferences, and meetings (267 hours).

Many different types of people took part in these events: e.g., city administrators, citizens, activists, hackers, academics, and consultants. These events were interspersed in time and often attended by people who already knew each other. These recurrent meetings to explore Decide were helpful to follow the changing understandings of participation in-situ, and led to informal ethnographic interviews—for example, during the coffee break of a hackathon or in the hallway during the break between two conference presentations. Specifically, we conducted 129 such ethnographic interviews, including all types of people attending the events.

Two more data collection sources were important: archival data and semi-structured interviews. Archival data comprised 189 reflective documents—for example, consultancy reports commissioned by the city council and outputs from hackathons or focus groups. In keeping with the spirit of openness of the city council, these documents are usually made available publicly. Other primary sources included social media use from key actors in the project, sound bites from political leaders, related YouTube videos, official press releases and press interviews with Decide leaders, and mailing lists from the movement protests that led to Decide and the platform’s own GitHub accounts.

We also conducted 11 semi-structured interviews in order to understand and contrast information from primary and secondary sources and to confirm factual data and timelines. The list of interviewees included Decide leaders and decision makers, project leaders that were given supervisory charge over projects on Decide, project managers, project participants, coders, hackers, and platform users. These interviews lasted 90 minutes on average.

Finally, we had access to the participation data from the platform itself, spanning the four years it was active. This included all the proposals, the votes, the comments they received, and the debates that emerged from them.

The entire process of developing the dataset was driven by a wish to triangulate data both in time (e.g., participants evaluating the platform’s inclusion outcomes) and materially (e.g., the same participants reflecting on the same issue in different material formats). This triangulation effort helped reveal both subtle and large changes regarding Decide and the contested notion of inclusivity. The inductive and longitudinal approach contributed to understanding the creative role that social inclusion had in the platform’s design and reflective activities, as well as the realization that the expectations could not be met. This allowed us to zoom in to see the dominant tensions and zoom out to see the overall picture and the role of tensions within a longer time frame (Fairhurst et al., 2016; Schad & Bansal, 2018).

## 3.2 Analytical Process

Given the many events that took place and the prominent discourse involving Decide in the media, it rapidly became imperative to view this project as the construction of an archive tracing design decisions and their multiple ramifications. Memoing thus became a central practice in making sense of the evolution of the platform and our own understanding of Decide, allowing us to repeatedly compare and contrast current events with past events. Through constructing this archive, we observed that actors were producing different narratives concerning the role of Decide and how it should meet the expectations of inclusion.

We followed Gioia et al. (2012) and the interpretivist IS tradition (Bartis & Mitev, 2008) to study how members construct meaning and organize themselves accordingly. In keeping with the inductive aims of the research, we were interested in how people working with Decide made sense of the platform and how it could foster social inclusion in Madrid.

We used open coding to help maintain coherence with the concepts used by informants and to guide the development of rich theoretical insights (Gioia et al., 2012; Urquhart, 2012), and used established theories to make sense of what was happening—in particular, the tension between the design of the system and its simultaneous creation of inclusion and exclusion.

The open coding step was rife with moments of constant comparisons between what looked like different and isolated initiatives in the past trajectory of Decide’s design and its intended objectives. Constant comparison helped us make better sense of the complexity behind the deployment of the system and the various nuances of inclusion that emerged over the lifetime of Decide (see Figure 1).

After the initial open-coding step, the selective coding step revealed controversies about the design of the platform and how it did not meet expectations in terms of inclusion. Taking a step back from open coding revealed that the same design resulted in both inclusions and exclusions, which did not match the platform’s goal of creating social inclusion in general and for everyone. Questions about who was being included, why, and at the expense of whom were key in the further study of arising tensions. In this light, the different initiatives that were designed to resolve enduring tensions—for example, promoting offline deliberation of citizen juries as a complement to Decide’s online proposals, favored certain collectives over others and constituted alternative forms of inclusion. All designs shared the same purpose of social and political inclusion but they were enacted in different ways constituting a particular understanding of inclusion and exclusion. Key events in this process and the evolving understanding of inclusion they brought are reflected in Figure 1. This realization incentivized going back to the codes to look for overlapping contradictions between design intentions for including people, consequences, and proposed alternatives.

## 4 Data and Analysis

Decide Madrid is the emblematic tool put in place by Madrid’s government to create “everyone’s government” through direct participation. This strategic objective is embedded in its design and is thus very much intentional. Figure 1 presents a timeline of the project’s key moments up to 2019, the year in which Decide lost its political importance after new elections led to a change in government. It also shows how the underlying assumptions about inclusion evolved and how such changing assumptions influenced IS design choices. These elements are described in detail in the following sections.

## 4.1 Social Inclusion through Participation

Decide was a tool designed from the outset with social inclusion in mind. The new government that designed it, led by a civic platform called Ahora Madrid (“Now Madrid” in English), had its roots in the 2011 Spanish Occupy movement, in which issues of social inclusion were key (Kavada & Treré, 2020). The protests were seen as the result of a political system that had rejected many of its citizens, leading to the disenfranchisement of Spanish youth, the social and political exclusion of many citizens, and the reinforcement of power around dominant political players such as political parties and the market. The disenfranchisement of the population and the need for social inclusion was clearly identified in the political program of the new government, and participation was seen as the way to resolve these issues:

![](/api/attachments/5QZ4KT7C/fulltext/images/9cbf60a72681d4511a8a596aa376087fd3c248b99969122106bee4980f7670d8.jpg)  
Figure 1. Key Moments, Inclusion Assumptions and IS Design Choices in Decide (2011-2019)

Citizens have been excluded from political participation … (p. 4) A city where citizens can directly influence any municipal area that affects them and can develop their decision-making capacity regardless of their age, gender, sexual orientation, origin or functional diversity. We want to guarantee full and equitable participation in democratic processes … (p. 19) (Ahora Madrid’s political program, 2015)

“Full and equitable participation in democratic processes” was key in reaching the new government’s political ambition to make citizens co-producers of the city. The intention was thus to increase social inclusion through participation. The most emblematic expression of that sentiment manifested in the civic policy crowdsourcing platform Decide Madrid, which embodied this intention in its design. Decide was an attempt to provide executive access to policy making for any citizen 16 years of age or older living in Madrid (the only two required conditions). But the ultimate goal was greater than that: Decide wanted to “open source” the city (Gutiérrez, 2016). The idea was that the platform would change social relations between the city and the citizens, and usher in a new politics that would cater to all. As the then-mayor of Madrid said:

What we see rather clearly is that the city has changed. We see that participation is leaving a mark. But we cannot be auto complacent and we have to reflect on what participation is. What do we mean when we say “everybody’s government?” (From notes, conference on “collective intelligence for democracy” and Decide)

## 4.2 Design Choices: What Kind of Inclusion Did Decide Foster?

To allow as inclusive and direct a participation as possible, the tool was extremely simple. As reports ordered by the city council show, there was a widespread belief by the proponents that participating would not be complicated. A previous prototype, implemented during the Occupy protests was deemed to be “too complex” by a Decide leader (interview) and linked to low uptake. Proposals for Decide merely comprised a title and a short description. For example, one of the most straightforward proposals called “Massively Cover Madrid with Trees” included only a short paragraph and received 20,606 votes. In addition, the interface conformed to inclusive internet standards for design and was certified as an accessible website by one of Spain’s largest standardization bodies. “For us, the philosophy of Consul [Decide Madrid’s upstream fork] is that it would be a super easy app to use” (Interview, a principal programmer for Decide).

Participation in Decide was principally organized around the individual. Individual participation could be anonymized and there were few conditions to participate, with no obvious way to associate class or social status to participants. Anyone could make proposals once registered but only Madrid citizens could vote for proposals. Individual participation was key to the design of Decide, as reported by a number of informants and multiple documents commissioned by the city council:

The largest part of proposals is made by individuals, with only 5% proposed by a collective. (Report by Saulière et al., 2017, on behalf of Madrid’s city council)

Participation in Decide Madrid is individual, because the creation of communities or the involvement of users is not encouraged. (Report by Padilla and Malo de Molina, 2018, on behalf of Madrid’s city council)

The design intention was for the platform to be a direct vehicle between citizens’ affects and the city council without any meddling.

We do not want a recipe [on how to participate], we can participate directly because technology allows us to. Democracy is one thing in a town of 30 and another in a city of 3 million like Madrid. Technology scales it. (Designer, from notes, focus group on radical democracy and Decide)

This scaling ability provided by technology represent one way of enabling direct democracy and bypassing representative powers. The technology behind Decide permitted it to focus on individuals’ voices to promote “full and equitable participation” to all citizens without anyone speaking for them. As one of the early web interfaces stated: “Here any voice has its space and it is the citizens’, and no one on their behalf, who decide by voting in the debates, which are the most important issues of each moment” (Decide’s original welcoming page, 2015).

The social inclusion program behind Decide and the development of the tool itself thus built on the individual as the sovereign political body of choice. The emphasis on the individual may be striking for a democratic tool, yet the design intention was for the platform to be a direct vehicle between citizens’ affects and the city council. It was “participation ‘without filters,’” as one report said (Padilla & Malo de Molina, 2018, p. 41). Project leaders wanted to avoid mimicking traditional politics within the platform and “replicating dysfunctionalities from traditional bodies composed of [political] parties” (Decide leader, from notes on a conference).

## 4.3 What Kind of Exclusion Did Decide Generate?

The deliberate design of Decide and its focus on individuals excluded collectives and their organizational capacity. For example, associations and collectives could have accounts to make proposals and create comments but such accounts were principally there to inform citizens that they were interacting with a collective. They had no special organizational functions to channel participation or organize on the platform (e.g., they could not send group emails, collectively draft proposals on the platform or vote to support a proposal). This issue of excluded collectives appeared frequently in the sources studied. A commissioned report studied the lack of uptake of Decide by local fora, deliberative citizen bodies that had privileged channels to the government and represented districts in Madrid (Co-incidimos, report commissioned by the city council). Another specifically suggested that one of the reasons for the lack of uptake was Decide’s own exclusion of collectives, particularly and paradoxically by those who had originally been involved in the protest movements from which Decide was born (Padilla & Malo de Molina, 2018). We therefore questioned why certain groups did not use Decide and what kind of participation was excluded by designing inclusion around the individual.

Because the functionality was focused on individual users, the kind of collectives that could participate with Decide were temporary political bodies that organized themselves around proposals and dismantled themselves once the proposal was no longer active. The system was conducive to individually writing proposals but left little room to work collectively. At most, the platform allowed individuals to comment on a proposal and post polls, but once a proposal was written, it could not be amended. Otherwise, it would have been possible for a proposal to be changed after being voted on by others, which would have distorted voters’ voices.

In other words, the focus on individual participation preemptively excluded participation from collectives. Since Decide was built around a simple, traditional web forum design metaphor, it did not have the functionalities needed for people to be proactive on the platform, requiring participation to necessarily overspill into other social networks. Decide did not have a process to create stable groups that could coordinate and organize, leaving that to other social networks and online collaboration tools.

The difficulties behind collective participation ended up affecting the quality of participation that took place on the platform. Participation was based more around affinity with certain kinds of topics than around the creation of political bodies for the long haul. Another exclusion was, paradoxically, that of individual participants themselves. The low barrier to entry created a massive influx of proposals that sabotaged the platform in the end. A person we talked to during one of the events noted that there were so many proposals that participating actually took a lot of effort:

I have participated in Decide and I find it very interesting, but then I enter there and there are thousands of proposals. There is no job more difficult than being a responsible citizen. To really participate in budgets, I should read 20 proposals, studying architecture as well! (From notes from a hackathon on the future of Decide)

To be featured on the front page (i.e., to remain visible, given the massive numbers of proposals), a proposal had to remain actively voted on. This specific IS design feature rewarded attention-grabbing proposals rather than nuanced, high-quality, well-written proposals. Although voting enabled participation, it also shaped how and where proposals appeared on the platform. Thus, only those who were able to campaign for their proposal to attract sufficient attention have a chance of being included. As one report stated:

This means that there is a bigger incentive for marketing and campaigning for a proposal than there is for developing an informed and nuanced proposal. (Report commissioned by the city council on participation and citizen juries)

## 4.4 Rethinking Social Inclusion and IS Design

It may seem surprising that participation on this platform—with its power, effectively handed to the citizenry, to shape policies—began to slump after only two years. In the end, only two proposals passed the required thresholds of votes to be sent for discussion in the local parliament. The last time the platform registered more than 200,000 votes was in February 2017. After that, votes on proposals stagnated, remaining below 80,000 votes. This slump in participation, especially from the activist circles, encouraged the government to commission Madrid’s innovation lab to reflect on ways to improve Decide’s design.

The assumption that social inclusion would be inherent to the platform began to fade, and new assumptions about inclusion emerged. Over time, this led to the development of four different but compatible design choices (see Figure 1): proponent communities, territorialization, the City Observatory, and data mining. Proponents of Decide questioned how different designs created opportunities for different kinds of inclusion. Often, this did not entail changing the original interface but complementing it and mitigating its deficiencies in the social context.

Proponent communities: The impermanence of temporary collectives and their inability to become communities became a main driver of this design initiative. One leader of Decide asked the following question:

Sometimes a community does not get woven and we do not know how to find the ingredients to make that work. Do you have ideas of some ingredients that we can use? (A leader of Decide questioning data analysts, from conference notes,)

The assumption behind proponent communities was that the platform could be complemented through a process of creating sustainable strategic citizen communities based on topics of interest. A group of consultants analyzed participation patterns in Decide through social network analysis as a prerequisite to identify ways to establish lasting communities:

This document is based on a mapping of Decide Madrid users and their interests in order to define strategies to strengthen existing and potential communities; and launch campaigns that allow some of the selected proposals to be widely voted on. (Report by Saulière et al., 2017, on behalf of Madrid’s city council)

This analysis sought first to understand why people participate in Decide (e.g., to improve the city, to censure behavior, to have ideological debates, etc.) and what types of proposals were appealing (e.g., highly concrete demands, public service improvements, specific collective’s needs, etc.). It then sought to identify the themes with the biggest potential to garner support and create sustainable communities around them. Two themes were chosen (environmental protection andchildhood) based on criteria such as the capacity to elicit passion, the avoidance of polarization, creating real options for change, creating general interest, and the capacity to combine efforts. This approach to inclusion, however, was far removed from the original global inclusive aspirations: only consensual issues could be resolved through this process, leaving more thorny, less widely appealing issues on the sidelines.

Territorialization: Another design initiative, implemented at the same time, experimented with a design to ground Decide within localities and to “territorialize” the platform to include neighborhoods, particularly disadvantaged ones. The idea of physical territories was adapted to work with the platform through a team of activists who tried to imbricate Decide within the local social fabric to get closer to neighbours' real needs. Local artists and long-time activists were recruited to facilitate offline, neighborly participation in a disenfranchised district of Madrid. A video from the project states: “Step into the territory and make participation a daily act.” (Facebook post), and to find out “what proposals appeal to the territory, in what specific spaces ... generate a story, meet people” (From notes from a focus group on the future of Decide). Here again, the platform itself did not change. It became incorporated into the specific local contexts (e.g., neighborhoods rather than interest groups) by enabling offline, in-situ deliberation through the use of artistic prompts (e.g., drawing, posters, videos). These collectively developed proposals were then to be uploaded to the platform. The IT artifact, on its own, did not reach the neighborhood and needed to be accompanied by a deployment of tailored social processes.

Data mining: This design initiative regrouped multiple efforts to use data mining techniques to explore the common preoccupations of the city. This initiative intended to mitigate the fragmentation of proposals by developing a new way of accessing and visualizing the information on the platform. For example, some suggested using natural language processing to semantically regroup proposals, “making it easier to navigate the constellation of proposals” (De Dios Llorens & Pérez, 2019). Here, listening to people’s voices became a technological problem of organization. In this sense, Decide’s usefulness emerged not directly, by giving citizens a direct voice, but indirectly through the capable manipulation of big data that could sift through proposals and find what truly worried most citizens. The technology thus favored a bird’s-eye view of proposals, transformed into meta-areas of concern. A conference to discuss this type of initiative was held at the end of 2018 and, although a number of prototypes were developed, they were never integrated into Decide’s platform.

The City Observatory: The last key design initiative (launched in May 2019) sought to solve Decide’s difficulty of attracting enough votes for proposals to be turned into legislation. A new political body of representative citizen juries was institutionalized to evaluate the quality of the Decide proposals with the most votes. To work, the platform thus had to create new alliances with this body, which included voices that were different from the ones originally planned. This citizen jury was composed of a random sample of citizens based on specific criteria (age, district they lived in, and gender). The overall IS design thus moved from seeking individual participation to seeking demographic representativity. The people and processes involved in creating and evaluating the proposals changed, leading to the emergence of new policies. Although not a statistical representation of Madrid’s society (though sometimes promoted as such), proponents argued that it created a “descriptive representation” of citizens that would give legitimacy to Decide’s proposals and its lack of numbers:

Basically, what you want is to replace the system of legitimation of proposals to reach 28,000 supports by a representative system chosen by lottery that evaluates the proposals and decides if they are relevant, okay? So that’s the fundamental idea. (Interview, one of the leaders of Madrid’s innovation lab and designer of the City Observatory)

Effectively, inclusion was no longer an outcome of the platform but happened externally when the platform was coupled with citizen juries. It was the statistical qualities of the juries that provided inclusion in global form to descriptively represent Madrid’s citizens. This resulting inclusion contrasted with the inclusion in the previous redesign initiatives, which sought to embed Decide into the realities and social complexities of Madrid’s neighborhoods and valued the voice of any individual citizen above all else, whether they fit a statistical description of the city or not. Indeed, the statistical representation itself was debated: variables such as political tendencies were played with and abandoned along the way.

Overall, all these initiatives underline how the connection between participation, social inclusion and IS design became problematized in Decide. Nevertheless, they all encountered drawbacks, underlining the existence of ongoing, unavoidable tensions between inclusion and exclusion. For example, the first proposal that the City Observatory had to evaluate stemmed from the work done by one of the proponent communities. The proposal named “Right to Play” was drafted by parents and children in their spare time, after work and after school. It successfully obtained a large number of votes but had not yet passed the threshold when it was discussed by the citizen jury. To the surprise of the organizers and the support staff, the proposal was struck down. Whether this was the right decision or not is not important here. What is important is how a Decide design choice (proponent communities) creating a specific kind of inclusion (that of children and parents) stumbled against another design choice (the City Observatory) and its alternative, statistical understanding of inclusion.

## 5 A Framework for Designing IS-Based Social Inclusion Interventions

This case study offers a window into a critical case of social and political inclusion through IS. Its analysis shows that design choices have crucial influence over IS interventions’ capacity to include or exclude because design enacts different understandings of inclusion and exclusion. Although, in Decide, the IS was designed with the intent to include everyone and anyone, it ultimately could not because there was a paradoxical tension between inclusion and exclusion. While the literature tends to see inclusion and exclusion as opposites, assuming that a decrease in one leads to an increase in the other (Epstein et al., 2011; Warschauer, 2002), the findings of this paper are aligned with work suggesting that inclusion and exclusion are interdependent experiences and two sides of the same coin (Deng et al., 2016; Iivari et al., 2018; Sorochan, 2016).

In light of these findings, adopting a paradox lens opens up our capacity to theorize the influence of IS designs on inclusion. Drawing on the literature’s categorization of responses to paradox (i.e., either-or, both-and, morethan) (Putnam et al., 2016) and the analysis of Decide, Table 1 proposes a framework for designing IS-based social inclusion interventions that underlines the role that IS design can play in managing the tension between inclusion and exclusion. The framework encompasses four types of IS design strategies, which rely on different assumptions regarding the tension between inclusion and exclusion and entail different responses to paradox.

The first three strategies emerge from the Decide case: positive discrimination, integrative oscillation, and equitability. The first strategy, positive discrimination, can be categorized as an either-or approach (Putnam et al., 2016). It is a selection strategy that assumes that when observing exclusion, specific actors and groups may be given preferential attention in the design to develop meaning that favors them. This can be used, for example, to favor those that have been historically underrepresented. For example, Decide made a conscious design choice to favor individual citizens’ participation at the expense of representative bodies, under the assumption that the latter had been given more opportunities to participate in the past through other means. In other contexts, marginalized actors may be given preference over others deemed to be already more included. For instance, designing an IS that focuses on including the elderly may assume that it cannot simultaneously engage younger people, who may then be excluded. While this strategy may help circumvent and redress power imbalances, it chooses who the vulnerable and underrepresented groups are and prioritizes them, running the risk of stereotyping and placing individuals into strict categories.

The second strategy, integrative oscillation, can be categorized as a both-and approach, focusing on vacillation between opposite poles (Putnam et al., 2016). In line with Cornford and Klecun (2003), it assumes that it is impossible to avoid exclusion from the implementation of any participatory IS. Inclusion and exclusion are inseparable and interdependent (Smith & Lewis, 2011). However, different kinds of exclusions can be managed by combining complementary systems that focus on different poles. The exclusionary potential towards other groups is limited by providing multiple participation channels that are appropriate for different collectives. Díaz Andrade and Techatassanasoontorn (2020) suggest this type of strategy by proposing offline alternatives to those who feel uncomfortable with online governmental services. Exclusions would be thus counteracted through these different participatory channels. In this way, systems recurringly oscillate between inclusion and exclusion for each of the actors involved.

This was the espoused option for Decide when creating the proponent communities, the territorialization initiatives, or the City Observatory. The individuality of the proposals and the unmediated voice of citizens was coupled with either engaging collectives in developing proposals (gathered around a common interest or in their local context) or with the legitimacy of an institutionalized group of citizens that provided some concrete representation of Madrid and could evaluate the proposal’s value to the city before it was forwarded to parliament. The inclusionary/ exclusionary consequences of each of these initiatives was balanced by the other initiatives.

In segmenting participatory actors, this strategy seeks to connect opposing poles of inclusion and exclusion in different times and contexts (Poole & Van de Ven, 1989), and to sequentially vacillate between them. In this sense, it can be reactive to emerging needs. However, this strategy is potentially very expensive because it implies accommodating multiple, simultaneous designs.

The third strategy, equitability, attempts to balance tradeoffs and can also be considered a both-and approach (Putnam et al., 2016). Instead of favoring any collective and moving back and forth between them, this strategy seeks a design that may treat all participants equally. Such designs look for the lowest common denominator in order to equally cater to all actors. One example from Decide was the attempt to data mine the main areas of concern on the platform. The quantity of proposals provided an attractive source of big data that enabled themes of interest to emerge across all actors who participated, regardless of who they were or the strength of their proposal. The algorithmic approach arguably created a meaning with similar value for all actors involved. Although it admits that both inclusion and exclusion will result from an IS design, this strategy focuses on meeting competing demands and assumes that the degree of harm from resulting exclusions can be limited.

Table 1. Framework for Designing IS-Based Social Inclusion Interventions

<table><tr><td>Design strategy</td><td>Positive discrimination</td><td>Integrative oscillation</td><td>Equitability</td><td>Iterative inclusivity</td></tr><tr><td>Response to paradox management</td><td>Either-or (selection)</td><td>Both-and (vacillation between poles)</td><td>Both-and (balancing poles)</td><td>More-than (third spaces and reflective practices)</td></tr><tr><td>Key assumptions</td><td>Through intervention a level playing field is possibleNeed to provide preferential treatment to a specifically vulnerable group to raise inclusion</td><td>A level playing field is impossible but exclusion is manageableCompeting demands can be met through vacillation, focusing on one exclusion at a time</td><td>Harm of exclusion can be minimized if actors are treated equallyIt is important to find a compromise or a middle-ground approach</td><td>Tensions are used to open inclusion meanings and enact systemsIS and their enactments are in perpetual beta</td></tr><tr><td>Key actions and design choices</td><td>Identify the vulnerable collective to includeFavor them with tailored designs at the expense of others</td><td>Identify excluded collectivesProvide multiple inclusion channels that cater to different collectives.</td><td>Create designs that treat all collectives equallyFocus on minimum denominator of inclusion</td><td>Rapidly deploy and modify ISContinuously evaluate inclusions and exclusions by actorsProvide extensive resources to lower design costs</td></tr><tr><td>Decide illustration</td><td>Targeting individual participants at the expense of representative bodies</td><td>Individuality of voice to include all citizens complemented by proponent communities, territorialization or citizen juries</td><td>Big data techniques to condense the multitude of individual voices</td><td>N.A.</td></tr><tr><td>Literature examples</td><td>Women quotas in boards (Terjesen &amp; Sealy, 2016)</td><td>Employee voice exercised through complementary means (e.g. direct voice, trade union representation)(Wilkinson &amp; Mowbray, 2019)</td><td>Text-based and machine-readable websites(Youngblood, 2014)</td><td>Self-care technology design for and by disabled people(Sánchez et al., 2016)</td></tr><tr><td>Critical evaluation</td><td>Visibility and prioritization issues: how to choose vulnerable groups?Risk of stereotypingMay circumvent power imbalances</td><td>Potentially expensive solution since multiple designs must be accommodatedMay be reactive to emerging needs</td><td>The degree of inclusion is constrained by the threshold of exclusionEquitability depends on all potential actors participating equallyPotential algorithmic biasLimited social exclusion</td><td>Never-ending processCan the costs of engaging be lowered enough to include the most vulnerable?Collectives included as co-creatorsNotions of exclusion empiricalFine-tuning of inclusion needs</td></tr></table>

There are several problems that emerge when following this approach to the letter. First, the direct voices of individual citizens might become sidelined by a technology that summarizes, abstracts, and catalogs the nuance and experiential complexity of their concerns in unknown ways. In addition, this strategy can only really be equitable if all potential actors participate equally (in the case of Decide, all the citizens of Madrid would need to participate to the same degree). In this sense, in complex systems involving numerous actors, it may be difficult for this strategy to be effective (Putnam et al., 2016). Another problem may be that systems designed for larger groups may be less effective than those designed for smaller groups (Abascal & Nicolle, 2005). Furthermore, algorithms may introduce biases and overlook important semantic ambiguities (Ferguson, 2020).

The positive discrimination strategy offers a mechanism to cope with the inclusion/exclusion paradox without actively engaging with it. The other two strategies develop an awareness of the paradox and provide alternatives to meet the opposing needs in the short term. All three tend to bury the paradoxical tension between inclusion and exclusion because they treat the paradox as solved or managed. This becomes captured in the IS design: once a design choice has been made it becomes almost immutable. As a result, the paradoxical tensions risk becoming “dormant, unperceived, or ignored” (Smith & Lewis, 2011, p. 390). The danger is that IS design may become a structural force that serves to define the “terms of participation” (Shestakofsky & Kelkar, 2020, p. 867), which creates excluding effects that become invisible over time (Polat, 2012) or prioritizes voices that become relatively more expensive to hear (Díaz Andrade & Techatassanasoontorn, 2020).

Indeed, either-or and both-and approaches to paradox have been deemed unsustainable in the long run (Jarzabkowski & Lê, 2017; Putnam et al., 2016; Seo, Putnam, & Bartunek, 2004). Instead, the literature suggests that more-than approaches may be a better long-term avenue to engage with tensions because of their ability to “preserve the dynamic interplay between opposites … cultivate a variety of responses, and situate contradictions at both individual and collective levels” (Putnam et al., 2016, p. 130). One such approach might be to consider the IS to be perpetually in “beta,” with prototyping becoming a continuous state.

This points to a fourth strategy, iterative inclusivity. The findings suggest the difficulty that Decide was confronted with in connecting itself effectively with different forms of participation and different participating collectives. Being able to reach a satisfactory degree of effectiveness may require repeated tinkering on both local processes (e.g., local community creation) and technical features (e.g., the ability to connect to technical staff). For IS designs to be able to effectively create meaning for certain participatory actors, there needs to be what Corsín Jiménez (2014) calls the “right to infrastructure” as one of the conditions to Lefebvre’s (1967) “right to the city.” This right to infrastructure “is incarnated in and deployed through very specific (open source) sociotechnical designs, interventions, and affordances” to shape epistemic regimes and create new political and social alternatives. The ultimate objective of social inclusion is to allow people to participate meaningfully and create symbolic, political, and material resources “where the means and ends of political action converge in very concrete and material objects of infrastructure” (Corsín Jiménez, 2014, p. 358). This implies that IS designs should cater to epistemologies that are, first and foremost, meaningful to those that are or should be socially and politically included rather than to states and administrations (Scott, 2020).

Iterative inclusivity would thus see localized IS designs rapidly deployed and modified to adapt to the continuous evaluations of inclusions and exclusions. While Decide experimented with several design initiatives over time, its proponents’ belief that exclusion could be resolved prevented them from engaging in iterative inclusivity. As a more-than response to paradox, rather than resolving contradictions or satisfying competing needs, iterative inclusivity strategies consciously engage with the tension between inclusion and exclusion. It is a neverending process that “develops collaborative dialogue among stakeholders” (Putnam et al., 2016; p. 127). In this sense, in contrast with the other strategies, iterative inclusivity can be considered a bottom-up approach: To a certain degree, the process is owned by those who are being excluded, who can empirically define the terms of exclusion and the ways in which IS can help foster inclusion, transforming them into co-creators. Inclusion needs are not preestablished and can be finetuned by the localized ongoing process.

Remaining questions about this strategy include whether the most vulnerable are in a position to engage in this process (e.g., single parents having multiple low-income jobs) and how to minimize their cost of engagement. Further, this strategy relies on populations willing to engage with digital technologies, which is a challenge in itself (see Díaz & Techatassanasoontorn, 2020).

## 6 Discussion

This paper started with an empirical observation which posed a theoretical conundrum: Decide Madrid, one of the most innovative and ambitious IS social inclusion interventions in the world, disappointed many of its proponents and created exclusion.

Analyzing this puzzling case enables us to make three key contributions to the literature. First, we articulate the inherent paradoxical tensions that exist between social inclusion and exclusion. While the literature has predominantly assumed an inverse relation between social inclusion and social exclusion (e.g., Warschauer, 2002; Silver and Miller, 2003), the case of Decide shows that exclusion is not the opposite of inclusion (e.g., (Edwards et al., 2001; Iivari et al., 2018). Relying on paradox theory, we thus propose that, while apparently opposed, inclusion and exclusion are “socially constructed polarities that mask the simultaneity of conflicting truths” (Lewis, 2000, p. 761).

Through taking a sociomaterial view of IS, we also illustrate how such tensions are woven within IT and other material artifacts. Indeed, the surprise that social activists shunned Decide shows how IS design can influence who becomes included and that exclusion is not just a social matter. It is entangled with technology’s materiality. In trying to include, IS cannot help but exclude as well. To make matters even more complicated, who will be excluded is unclear at the outset because inclusion is constituted by continuous sociomaterial practices (Scott & Orlikowski, 2014). Future research should consider longitudinal studies of technologies to understand how inclusivity is constituted in time and to examine artifacts in detail.

Our second contribution offers a framework to analyze and design social inclusion interventions dealing with these inherent paradoxical tensions. First, the framework offers novel evaluative guidelines for information systems that promote social inclusion, which is a key element of interventions (von Hellens et al., 2012). Accurate evaluation may enable actors to develop “paradoxical cognition” (i.e., the cognitive ability to accept paradox and face seemingly impossible choices) (Lewis, 2000). It can thus feed into the design of new systems that acknowledge the tensions between inclusion and exclusion, enabling proactive responses (Jarzabkowski, Lê, & Van de Ven, 2013). Such proactive responses are needed to take account of the performativity of IS—or, in other words, to view IS as intrinsically entangled with relational and sociomaterial features that play a role in its making and remaking rather than viewing IS as independent entities (Glaser et al., 2021). The constitution of inclusion is continuous, requiring the design of interventions that do not look at static outcomes but at how inclusion is apprehended by actors.

The framework also has implications for large-scale social-inclusion IS and projects such as those related to sustainable development goals (SDG) and social justice and activism (Aanestad et al., 2021; Selander & Jarvenpaa, 2016). Social inclusion is a key SDG and may have a paradoxical nature that is similar to other SDGs. Indeed, the literature has suggested that SDGs are full of trade-offs and incompatibilities (Biggeri et al., 2019; Savaget et al., 2019). Our framework can help researchers and policy makers understand how different IS designs might help them manage the tensions within and across SDGs. Other types of large-scale social inclusion programs (e.g., “one laptop per child”) also experience inherent tensions (Kelty, 2016) and may benefit from a paradox lens to make sense of and respond to such tensions.

Finally, social inclusion interventions have often been seen from a top-down perspective, excluding or tokenizing those to be included (Arnstein, 1969; Young, 2002). Our framework indicates that there are indeed topdown strategies to manage the paradoxical tensions between inclusion and exclusion (positive discrimination, integrative oscillation, and equitability) but there is also a principally bottom-up option (iterative inclusivity). Being a “more-than” response to paradox, iterative inclusivity can “employ performative practices to engage tensions and avoid premature closure of options” and “sustain the ongoing interplay between opposites” (Putnam et al., 2016, pp. 128-130). Given the performativity of IS in constituting inclusivity, involving actors in designing solutions (e.g., disabled ramp access—Sánchez Criado et al., 2016) can help to locally transcend the paradox between inclusion and exclusion. From a policy perspective, the role of public services is no longer providing solutions but providing the means for local actors to take action. This is a challenge for bureaucracy, given its ingrained suspicion of the crowd (Kornberger et al., 2017).

Indeed, treating citizens as partners in developing those epistemic regimes of the city will require a major shift in the way administrations and states see their traditional role of preserving bureaucratic efficiency (Kornberger et al., 2017). If participation technologies are indeed to include citizens socially and politically, then they will potentially transform city officials into mediators between citizens as stakeholders and potential product owners, on the one hand, and an executive branch, on the other. This evolution of roles could be reflected in IS through applying an iterative inclusivity strategy, making such technologies constantly in the process of becoming (Curto-Millet & Shaikh, 2017).

Our third contribution offers a new way of thinking about exclusion criteria: considering collectives vs. individuals. In delimiting inclusion and exclusion, prior research has mainly considered groups based on individual demographic, social, and identity characteristics (Baker & Sibona, 2022; Heath & Babu, 2017) such as gender (Naidoo et al., 2019), race (Joshi et al., 2017), status (Wilding, 2009), disability (Kim et al., 2018), and age (Fox and Connolly, 2018). In contrast, in this case, the evaluation of who was included and excluded did not center so much on such traditional characteristics but on how the characteristics of the design attracted or dissuaded participatory “collectives.”

Collectives are an abstract grouping of people that do not have preassumed underlying connections such as demographics and have become a key unit of organization (Baudry et al., 2021). They emerge based on often fleeting shared personal logics (Bennett & Segerberg, 2012)—for instance, revulsion about an ecological disaster (Barberá-Tomás et al., 2019)—rather than inherent individual features. While relying on sociodemographic attributes runs the risk of treating these attributes as monolithic and immutable elements, thinking in terms of collectives expands potential theorizing, because, like collectives, exclusion not only works along preestablished social or demographic lines, it can also be performative.

Moreover, a sociodemographic approach assumes that exclusion is the result of bias or prejudices against certain types of individuals. It may, however, be the case that certain groups are excluded not solely through biases coded into the technology’s design, but through the performative role of technology in constituting collectives. That is, the way technology entangles itself with the social could organize inclusion and exclusion within, beyond, but also across, demographic, social, and political lines (Amrute, 2016; Haraway, 1991).

Considering collectives to study and promote social inclusion opens the door to questions regarding their impermanence. Whether they have the capacity to become communities and sustain themselves (Gerbaudo, 2012) despite their diffuse identity and fluid collective action and what they may need to do so become important questions. A future avenue of research would also be to study how established concepts in social inclusion, which have often been framed in terms of demographics such as the digital divide (Warschauer, 2002), intersect with more fluid notions of collectives (Yuval‐Davis, 2007).

## 7 Conclusion

The analysis presented in this paper suggests that efforts to foster inclusion among those most vulnerable to exclusion must promote new and perhaps radical ways of thinking about inclusion through the continuous design of IS. Building on the idea that paradoxical tensions are inherent to social inclusion, we show that different IS designs enact different responses to paradox. We thereby provide a framework for designing and evaluating information systems based on social inclusion interventions and a critical analysis of different strategies. Future research could empirically analyze the effectiveness of these strategies in different contexts, and the extent to which they may be complementary or conflicting.

Overall, we conclude that obviating the exclusionary potential of social inclusion interventions amounts to “wishing away” the ontological characteristics of their underlying tension (Schad & Bansal, 2018). This provides a reasoned explanation of why so many social inclusions are considered to be failures. Inclusion and exclusion are intimately linked; thus, any search for social inclusion will at least exhibit traces of exclusion. This should not be cause for despair but should rather be heralded as a first step in acknowledging the ambivalent and paradoxical realities of social inclusion and exclusion.

## Acknowledgments

This project has received funding from the European Union’s Horizon 2020 research and innovation program under the Marie Skłodowska-Curie grant agreement No. 744957.

## References

Aanestad, M., Kankanhalli, A., Maruping, L. M., Pang, M.-S., & Ram, S. (2021). Call for papers MISQ special issue on Digital Technologies and Social Justice. MIS Quarterly. https://misq. umn.edu/skin/frontend/default/misq/pdf/Curre ntCalls/SI\_DigitalTechnologies.pdf

Abascal, J., & Nicolle, C. (2005). Moving towards inclusive design guidelines for socially and ethically aware HCI. Interacting with Computers, 17(5), 484-505.

Alter, S. (2008). Defining information systems as work systems: implications for the IS field. European Journal of Information Systems, 17(5), 448- 469.

Amis, J. M., Mair, J., & Munir, K. A. (2020). The Organizational Reproduction of Inequality. Academy of Management Annals, 14(1), 195- 230.

Amrute, S. B. (2016). Encoding race, encoding class Indian IT workers in Berlin. Duke University Press.

Annabi, H., & Lebovitz, S. (2018). Improving the retention of women in the IT workforce: An investigation of gender diversity interventions in the USA. Information Systems Journal, 28(6), 1049-1081.

Arnstein, S. R. (1969). A Ladder Of Citizen Participation. Journal of the American Institute of Planners, 35(4), 216-224.

Baker, E. W., & Sibona, C. J. (2022). Digital OER Impact on learning outcomes for social inclusion. Journal of Computer Information Systems, 62(2), 278-289.

Barberá-Tomás, D., Castelló, I., de Bakker, F. G. A., & Zietsma, C. (2019). Energizing through visuals: How social entrepreneurs use emotionsymbolic work for social change. Academy of Management Journal, 62(6), 1789-1817.

Bartis, E., & Mitev, N. (2008). A multiple narrative approach to information systems failure: a successful system that failed. European Journal of Information Systems, 17(2), 112- 124.

Baudry, J., Tancoigne, É., & Strasser, B. J. (2021). Turning crowds into communities: The collectives of online citizen science. Social Studies of Science, 52(3), 399-424.

Bennett, W. L., & Segerberg, A. (2012). The logic of connective action. Information, Communication and Society, 15(5), 739-768.

Biggeri, M., Clark, D. A., Ferrannini, A., & Mauro, V. (2019). Tracking the SDGs in an “integrated” manner: A proposal for a new index to capture synergies and trade-offs between and within goals. World Development, 122, 628-647.

Cardoso, A., Boudreau, M.-C., & Carvalho, J. Á. (2019). Organizing collective action: Does information and communication technology matter? Information and Organization, 29(3), Article 100256.

Castells, M. (2010). End of millennium. Wiley.

Coleman, D. (2018). Digital Colonialism: The 21st Century Scramble for Africa through the Extraction and Control of User Data and the Limitations of Data Protection Laws Note. Michigan Journal of Race & Law, 24(2), 417- 440.

Cornford, T., & Klecun, E. (2003). Social exclusion and information systems in community healthcare. In M. Korpela, R. Montealegre, & A. Poulymenakou (Eds.), Organizational Information Systems in the Context of Globalization: IFIP TC8 & TC9 / WG8.2 & WG9.4 Working Conference on Information Systems Perspectives and Challenges in the Context of Globalization June 15-17, 2003, Athens, Greece (pp. 291-305). Boston, MA: Springer.

Corsín Jiménez, A. (2014). The right to infrastructure: Prototype for open source urbanism. Environment and Planning D: Society and Space, 32(2), 342-362.

Corsín Jiménez, A., & Estalella, A. (2017). Political exhaustion and the experiment of street: Boyle meets Hobbes in Occupy Madrid. Journal of the Royal Anthropological Institute, 23(S1), 110- 123.

Corsín Jiménez, A., & Estalella, A. (2023). Free Culture and the city: Hackers, commoners, and neighbors in Madrid, 1997-2017. Cornell University Press.

Curto-Millet, D., & Shaikh, M. (2017). The emergence of openness in open-source projects: the case of openEHR. Journal of Information Technology, 32(4), 361-379.

Deng, X., Joshi, K. D., & Galliers, R. D. (2016). The duality of empowerment and marginalization in microtask crowdsourcing: Giving voice to the less powerful through value sensitive design. MIS Quarterly, 40(2), 279-A19.

Díaz Andrade, A., & Doolin, B. (2016). Information and communication technology and the social

inclusion of refugees. MIS Quarterly, 40(2), 405-416.

Díaz Andrade, A., & Techatassanasoontorn, A. A. (2020). Digital enforcement: Rethinking the pursuit of a digitally-enabled society. Information Systems Journal, 31(1), 184-197.

Edwards, R., Armstrong, P., & Miller, N. (2001). Include me out: critical readings of social exclusion, social inclusion and lifelong learning. International Journal of Lifelong Education, 20(5), 417-428.

Epstein, D., Nisbet, E. C., & Gillespie, T. (2011). Who’s responsible for the digital divide? Public perceptions and policy implications. The Information Society, 27(2), 92-104.

Fairhurst, G. T., Smith, W. K., Banghart, S. G., Lewis, M. W., Putnam, L. L., Raisch, S., & Schad, J. (2016). Diverging and converging: Integrative insights on a paradox meta-perspective. Academy of Management Annals, 10(1), 173- 182.

Ferguson, A. G. (2020). Rise of big data policing: surveillance, race, and the future of law enforcement. NYU Press.

Gerbaudo, P. (2012). Tweets and the streets: Social media and contemporary activism. Pluto Press.

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2012). Seeking qualitative rigor in inductive research. Organizational Research Methods, 16(1), 15- 31.

Glaser, B. G., & Strauss, A. L. (1967). Discovery of grounded theory: strategies for qualitative research. AldineTransaction.

Glaser, V. L., Pollock, N., & D’Adderio, L. (2021). The biography of an algorithm: Performing algorithmic technologies in organizations. Organization Theory, 2(2), 1-27.

Goldkuhl, G. (2016). E-government design research: Towards the policy-ingrained IT artifact. Government Information Quarterly, 33(3), 444-452.

Goldthorpe, J. H. (1968). The Affluent worker: political attitudes and behaviour. Cambridge University Press.

Gunkel, D. J. (2003). Second thoughts: Toward a critique of the digital divide. New Media & Society, 5(4), 499-522.

Gutiérrez, B. (2016). The open source city as the transnational democratic future. Transnational Institute.

Haraway, D. (1991). Simians, cyborgs and women: The reinvention of nature. Free Association Books.

Hardey, M. (2020). The culture of women in tech: An unsuitable job for a woman. Emerald Points.

Heath, D., & Babu, R. (2017). Theorizing managerial perceptions, enabling IT, and the social inclusion of workers with disabilities. Information and Organization, 27(4), 211-225.

Iivari, N., Kinnula, M., Molin‐Juustila, T., & Kuure, L. (2018). Exclusions in social inclusion projects: Struggles in involving children in digital technology development. Information Systems Journal, 28(6), 1020-1048.

Jarzabkowski, P. A., & Lê, J. K. (2017). We have to do this and that? You must be joking: Constructing and responding to paradox through humor. Organization Studies, 38(3-4), 433-462.

Jarzabkowski, P. A., Lê, J. K., & Van de Ven, A. H. (2013). Responding to competing strategic demands: How organizing, belonging, and performing paradoxes coevolve. Strategic Organization, 11(3), 245-280.

Joshi, K. D., Trauth, E. M., Kvasny, L., Morgan, A. J., & Payton, F. C. (2017). Making Black lives matter in the information technology profession: Issues, perspectives, and a call for action. The Data Base for Advances in Information Systems, 48(2), 21-34.

Kavada, A., & Treré, E. (2020). Live democracy and its tensions: making sense of livestreaming in the 15M and Occupy. Information, Communication & Society, 23(12), 1787-1804.

Kelty, C. M. (2016). Too Much Democracy in All the Wrong Places: Toward a Grammar of Participation. Current Anthropology, 58(S15), S77-S90.

Klecun, E. (2008). Bringing lost sheep into the fold: Questioning the discourse of the digital divide. Information Technology and People, 21(3), 267-282.

Kornberger, M., Meyer, R. E., Brandtner, C., & Höllerer, M. A. (2017). When Bureaucracy meets the crowd: Studying “open government” in the Vienna city administration. Organization Studies, 38(2), 179-200.

Lefebvre, H. (1967). Le droit à la ville. L’Homme et la société, 6(1), 29-35.

Lewis, M. W. (2000). Exploring paradox: Toward a more comprehensive guide. Academy of Management Review, 25(4), 760-776.

Mervyn, K., Simon, A., & Allen, D. K. (2014). Digital inclusion and social inclusion: A tale of two cities. Information, Communication & Society, 17(9), 1086-1104.

Naidoo, R., Coleman, K., & Guyo, C. (2019). Exploring gender discursive struggles about social inclusion in an online gaming community. Information Technology & People, 33(2), 576-601.

Olbrich, S., Trauth, E. M., Niedermann, F., & Gregor, S. (2015). Inclusive design in IS: Why diversity matters. Communications of the Association for Information Systems, 37(1), 767-782.

Orlikowski, W. J., & Scott, S. V. (2015). The algorithm and the crowd: Considering the materiality of service innovation. MIS Quarterly, 39(1), 201-216.

Padilla, M., & Malo de Molina, M. (2018). Formación e investigación sobre las relaciones ciudadanas con Decide Madrid. Medialab Prado.

Polat, R. K. (2012). Digital exclusion in Turkey: A policy perspective. Government Information Quarterly, 29(4), 589-596.

Poole, M. S., & Van de Ven, A. H. (1989). Using paradox to build management and organization theories. Academy of Management Review, 14(4), 562-578.

Putnam, L., Fairhurst, G. T., & Banghart, S. (2016). Contradictions, dialectics, and paradoxes in organizations: A constitutive approach. Academy of Management Annals, 10(1), 65-171

Saldivar, J., Parra, C., Alcaraz, M., Arteta, R., & Cernuzzi, L. (2018). Civic technology for social innovation. Computer Supported Cooperative Work (CSCW), 27(3), 1215-1253.

Sánchez Criado, T., Rodríguez Giralt, I., & Mencaroni, A. (2016). Care in the (critical) making. Open prototyping, or the radicalisation of independent-living politics. European Journal of Disability Research, 10(1), 24-39.

Saulière, S., Diez Escudero, R., & Abellán, A. (2017). Análisis digital de Decide Madrid— Comunidades colaborativas. Medialab Prado.

Savaget, P., Geissdoerfer, M., Kharrazi, A., & Evans, S. (2019). The theoretical foundations of sociotechnical systems change for sustainability: A systematic literature review. Journal of Cleaner Production, 206, 878-892.

Schad, J., & Bansal, P. (2018). Seeing the forest and the trees: How a systems perspective informs paradox research. Journal of Management Studies, 55(8), 1490-1506.

Scott, J. C. (2020). Seeing like a state: how certain schemes to improve the human condition have failed. Yale University Press

Scott, S. V., & Orlikowski, W. J. (2014). Entanglements in Practice: Performing anonymity through social media. MIS Quarterly, 38(3), 873-894.

Selander, L., & Jarvenpaa, S. L. (2016). Digital action repertoires and transforming a social movement organization. MIS Quarterly, 40(2), 331-352.

Sen, A. (2013). Foreword. In The passions and the interests: political arguments for capitalism before its triumph (Revised ed.). Princeton University Press.

Seo, M.-G., Putnam, L., & Bartunek, Jean M. (2004). Dualities and tensions of planned organizational change. In A. H. Van de Ven & M. S. Poole (Eds.) Handbook of organizational change and innovation (pp. 73-107). Oxford University Press.

Shestakofsky, B., & Kelkar, S. (2020). Making platforms work: Relationship labor and the management of publics. Theory and Society, 49(5), 863-896.

Silver, H., & Miller, S. M. (2003). Social exclusion: The European approach to social disadvantage. Indicators, 2(2), 5-21.

Smith, W. K., & Lewis, M. W. (2011). Toward a theory of paradox: A dynamic equilibrium model of organizing. Academy of Management Review, 36(2), 381-403.

Sorochan, C. (2016). Participation as ideology in Occupy Wall Street. In D. Barney, G. Coleman, C. Ross, J. Sterne & T. Tembeck (Eds.) The participatory condition in the digital age (pp. 22-43). University of Minnesota Press.

Terjesen, S., & Sealy, R. (2016). Board gender quotas: Exploring Ethical tensions from a multitheoretical perspective. Business Ethics Quarterly, 26(1), 23-65.

Trauth, E. M. (2013). The role of theory in gender and information systems research. Information and Organization, 23(4), 277-293.

Trauth, E. M. (2017). A research agenda for social inclusion in information systems. The Data Base for Advances in Information Systems, 48(2), 9-20.

Trauth, E. M., Joshi, K. D., & Yarger, L. K. (2018). ISJ Editorial. Information Systems Journal, 28(6), 989-994.

Urquhart, C. (2012). Grounded theory for qualitative research: A practical guide. SAGE.

van Stekelenburg, J. (2012). The Occupy movement: Product of this time. Development, 55(2), 224- 231.

von Hellens, L., Trauth, E. M., & Fisher, J. (2012). Editorial. Information Systems Journal, 22(5), 343-353.

Warschauer, M. (2002). Reconceptualizing the digital divide. First Monday. https://doi.org/10.5210/ fm.v7i7.967

Wilding, R. (2009). Refugee youth, social inclusion, and ICTs: can good intentions go bad? Journal of Information, Communication and Ethics in Society, 7(2/3), 159-174.

Wilkinson, A., & Mowbray, P. (2019). Creating and Sustaining Involvement and Participation in the Workplace. In A. Wilkinson, N. Bacon, S. Snell, & D. Lepak (Eds.), The SAGE Handbook of Human Resource Management (pp. 253- 270). SAGE.

Wilson, C., & Secker, J. (2015). Validation of the Social Inclusion Scale with Students. Social Inclusion, 3(4), 52-62.

Windeler, J., Petter, S., Chudoba, K., Coleman, E., Fox, G., & Chapman, T. (2020). In or out? Perceptions of inclusion and exclusion among AIS members. Communications of the Association for Information Systems, 46(5), 92- 116.

Yin, R. (2003). Case study research—Design and methods. Sage.

Young, I. M. (2002). Inclusion and democracy. Oxford University Press.

Youngblood, N. E. (2014). Revisiting Alabama state website accessibility. Government Information Quarterly, 31(3), 476-487.

Yuval‐Davis, N. (2007). Intersectionality, citizenship and contemporary politics of belonging. Critical Review of International Social and Political Philosophy, 10(4), 561-574.

Appendix A: Navigating Proposals on Decide Madrid in 2017  
![](/api/attachments/5QZ4KT7C/fulltext/images/fb2d0fa93b1830b718334a3abea9005c790d9136e2f1f147d9af12a0d1940ad5.jpg)  
Appendix A is a screenshot of the proposal menu, showing two proposals alongside different navigation options and actions. The user can look at the day’s most active proposals (Más activas hoy), those that have received the most support (Más apoyadas), new proposals (Nuevas), and archived proposals (Archivadas). Proposal tags (the grey tags under the text of proposals), categories (Categorias) such as equality and social rights, and tendencies (Tendencias), are other ways to navigate proposals. The user can cast their vote (Apoyar) or create a new proposal (Crea una propuesta).

Appendix B: Example of a Citizen Proposal from User “Koala” to Enlarge a Metro Line to an Underserved Madrid neighbourhood.  
![](/api/attachments/5QZ4KT7C/fulltext/images/c637319576bee52e9bd93b21ea246a1602adfabe03882f07125bd6b83d072257.jpg)  
Appendix B shows a screenshot of one of the proposals. It has 14 comments and received 1,410 votes of the 27,662 necessary to become part of the governing party’s political agenda. The yellow button “Apoyar” registers individual citizens’ votes. Unbeknownst to the author, the request is not under the control of the city but of the region, which makes the proposal invalid. The interface shows a menu where people can debate (debates, not limited to registered citizens), make proposals (propuestas), be involved in voting processes and participatory budgeting (votaciones, where citizens can vote on specific government-led proposals and presupuestos participativos), and get help (ayuda, where a FAQ and various resources indicate how the system should be used and suggest ways to gain votes). Throughout the research, “proposals” were identified as the most important aspect of the system since it allowed citizens and activists to directly influence the city’s governance. This function held the innovative potential of the system since, in the words of the lead designer, it “allowed [citizens] to hack the city.” Proposals were drafted by an individual using a simple form and had to include a title and a text explaining the proposal.

## About the Authors

Daniel Curto-Millet is an assistant professor in the Department of Applied IT at the University of Gothenburg. He received his PhD from the London School of Economics and Political Science and is a Marie Skłodowska Curie scholarship alumnus. His research interests include open source and online communities, digital organizing, and social movements. His work has been published in journals such as Journal of Information Technology and European Journal of Information Systems.

Almudena Cañibano is an associate professor of management and the scientific director of the Happiness and Well-Being in Management Research Centre at ESCP Business School. She holds a PhD from the London School of Economics in political science. Her research focuses on the changing nature of work and its connection to lived experiences. She studies innovative work organization systems, such as flexible or virtual working, freelancing, and crowdwork and their effect on well-being and inclusion. Her work has been published in Human Relations, Human Resource Management Journal, and Industrial Relations: A Journal of Economy and Society.
