---
otero_id: 10082
otero_key: "EHGV6B2H"
title: "Algorithmic Management of Work on Online Labor Platforms: When Matching Meets Control"
authors: "Mareike Möhlmann; Lior Zalmanson; Ola Henfridsson; Robert Wayne Gregory"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15333"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ALGORITHMIC MANAGEMENT OF WORK ON ONLINE LABOR PLATFORMS: WHEN MATCHING MEETS CONTROL<sup>1</sup>

Mareike Möhlmann Bentley University, Waltham, MA, U.S.A {mmoehlmann@bentley.edu}

Lior Zalmanson Coller School of Management, Tel Aviv University, Tel Aviv, ISRAEL {zalmanso@tau.ac.il}

Ola Henfridsson Miami Herbert Business School, University of Miami, Coral Gables, FL, U.S.A. {ohenfridsson@miami.edu}

Robert Wayne Gregory Miami Herbert Business School, University of Miami, Coral Gables, FL, U.S.A. {rwgregory@miami.edu}

Online labor platforms (OLPs) can use algorithms along two dimensions: matching and control. While previous research has paid considerable attention to how OLPs optimize matching and accommodate market needs, OLPs can also employ algorithms to monitor and tightly control platform work. In this paper, we examine the nature of platform work on OLPs, and the role of algorithmic management in organizing how such work is conducted. Using a qualitative study of Uber drivers’ perceptions, supplemented by interviews with Uber executives and engineers, we present a grounded theory that captures the algorithmic management of work on OLPs. In the context of both algorithmic matching and algorithmic control, platform workers experience tensions relating to work execution, compensation, and belonging. We show that these tensions trigger market-like and organization-like response behaviors by platform workers. Our research contributes to the emerging literature on OLPs.

Keywords: Algorithmic management, control, matching, online labor platforms, meta-organizations, Uber

## Introduction

Online labor platforms (OLPs) are transforming how people work. In Europe and the U.S., 163 million independent contractors and freelancers perform temporary, flexible jobs, amounting to 20-30% of the working-age population (Manyika et al. 2018). They are increasingly using OLPs such as Upwork, TaskRabbit, M-Turk, and Uber to secure work assignments. In 2016, 8% of all Americans had worked via an OLP in some capacity (Smith 2016), and in 2018, 10% of adult respondents to a large-sample poll in the EU (European Commission 2018) had offered services through OLPs at least once.

Current IS research interest in OLPs is therefore timely (e.g., Burtch et al. 2018; Chen and Horton 2016; Constantinides et al. 2018; Hong et al. 2016; Huang et al. 2020), with recent studies addressing pricing (Chen and Horton 2016), the new labor market’s effect on entrepreneurial activity (Burtch et al. 2018), and the design of auction processes for labor matching (Hong et al. 2016). To this end, IS research on OLPs tends to adopt an economics perspective, viewing platforms as markets (e.g., Burtch et al. 2018; Chen and Horton 2016; Gawer 2014; Hong et al. 2016; Huang et al. 2020) in which machinelearning algorithms (e.g., Agrawal et al. 2018; Curchod et al. 2020; Faraj et al. 2018) enable efficient matching of demand and supply (De Reuver et al. 2018; Evans 2003; Eisenmann et al. 2006; Parker et al. 2016). Such algorithmic matching is at the heart of most OLPs.

Yet OLPs also offer a model for organizing work. Such organization of work relies on the use of algorithms to monitor and control platform workers (Kuhn and Maleki 2017; Newell and Marabelli 2015; Lee et al. 2015; Rosenblat and Stark 2016), to the extent that some suggest they are “working for an algorithm” (Curchod et al. 2020). Defined as individuals who have registered with an OLP to undertake work assignments within a given area of expertise, platform workers are monitored by the platform. They are subject to performance measurement (Galliers et al. 2017; Newell and Marabelli 2015) as if employed by an organization. This is enabled by algorithmic control.

OLPs can accordingly use algorithms along two dimensions: matching and control. Most OLPs, including Upwork, TaskRabbit, and M-Turk focus on algorithmic matching. Some OLPs, such as Uber, also pay attention to the control of work. We view such OLPs as technology-enabled metaorganizations (Gawer 2014; Gulati et al. 2012), recognizing that they not only create value by matching demand and supply but may also coordinate constitutive agents towards organizational goals. They provide platform workers with a work environment that combines considerable flexibility and autonomy (Deng et al. 2016; Kuhn and Maleki 2017) with surveillance and supervision (Galliers et al. 2017; Newell and Marabelli 2015).

In this paper, we examine the nature of platform work on OLPs, and the role of algorithmic management in organizing how such work is executed, rewarded, and shared. We conducted a qualitative study of Uber drivers in London and New York City, supplemented by interviews with Uber executives and engineers, to address the question: how does algorithmic management as implemented by the Uber app affect platform work? Our choice of Uber as a case for studying algorithmic management of work on online labor platforms exemplifies the extreme-case selection technique (Gerring 2007). Using this technique, a case is selected because of its high values for the variables of interest. Uber scores highly on the dimensions of both algorithmic matching and algorithmic control. This case selection technique is useful for theory development in the area of OLPs and algorithmic management, as “an extreme case corresponds to a case that is considered to be prototypical or paradigmatic of some phenomena of interest” (Gerring 2007, p. 101).

We analyze our data sources using grounded theory techniques (Charmaz 2014; Gioia et al. 2013; Glaser 1978) to allow new insights to emerge from the data. We identify and detail how the

Uber platform’s algorithmic management operates along two dimensions: algorithmic matching, which supports Uber drivers’ use of the app in a marketplace mode, and algorithmic control, through which the Uber app exerts managerial control. Our findings capture three main tensions in the work environment, relating to work execution, work compensation, and work belonging, and we show that drivers’ reactions to these tensions arise from wishing the platform to resemble both a market and an organization. We synthesize our findings into a new grounded theory of the role of algorithmic management of work on OLPs.

Our theory conceptualizes OLPs as a model for organizing work that embodies both market and organizational attributes. It contributes to the literature on OLPs by explaining algorithmic management of platform work in terms of the dynamic interplay of its antecedents (algorithmic management), characteristics (work execution, work compensation, and work belonging tensions), and consequences (platform workers’ responses).

## Conceptual Background

## Online Labor Platforms

IS researchers tend to approach OLPs as markets (e.g., Burtch et al. 2018; Chen and Horton 2016; Gawer 2014; Hong et al. 2016; Huang et al. 2020). Grounded in industrial economics (Armstrong 2006; Evans et al. 2006; Rochet and Tirole 2003), platforms are viewed as “special kinds of markets that play the role of facilitators of exchange between different types of consumers that could not otherwise transact with each other” (Gawer 2014, p. 1240). The platform matches supply and demand, and high-quality matchmaking is essential to the platform’s performance (Parker et al. 2016). In such two-sided markets (Eisenmann et al. 2006), the platform’s value is typically associated with the network effects offered to “two or more distinct user groups platform users who are connected via an indirect network” (Rietveld and Schilling 2021). The platform’s value to a particular user group is influenced by the size of the opposite network. For instance, the benefit to providers (e.g., Uber drivers) depends on the number of consumers (e.g., Uber passengers), while the benefit to consumers depends on the number of providers (Hagiu and Wright 2015). While the literature typically views “network effects as exogenous and fixed” (Gawer 2014, p. 1240), OLPs may make strategic calls in designing their matching algorithms. Such calls may relate to the use of dynamic pricing (Chen 2016), auction-based mechanisms (Hong et al. 2016), or the governance of information asymmetries between the different sides of the market (Parker et al. 2016). All in all, consistent with its underlying assumptions, the economics perspective tends to focus on matching, paying little attention to the fact that OLPs also offer a model for organizing work by implementing mechanisms for monitoring and control.

Early empirical evidence on OLPs relates to how crowdsourcing (e.g., M-Turk) and gig work (e.g., UpWork and TaskRabbit) differ from traditional work environments in how work is structured, communicated, managed, and delivered (Barowy et al. 2016; Irani and Silberman 2013; Deng et al. 2016; Kuhn and Maleki 2017; Petriglieri et al. 2019). One significant difference is the high degree to which platform work is mediated by digital technologies, through websites or smartphone apps on which workers can sign in, bid for work tasks, and be matched with work requesters (Deng et al. 2016; Kuhn and Maleki 2017; Nambisan et al. 2017; Burtch et al. 2018; Liu et al. 2018). As in traditional freelancing, contract work, and self-employment (Barley and Kunda 2006; Cappelli and Keller 2013), this enables platform workers to work remotely and be flexible in their choice of tasks (Deng et al. 2016; Deng and Joshi 2016) and work schedules (Rosenblat and Stark 2016). At the same time, however, platform workers are increasingly controlled (Kuhn and Maleki 2017; Schildt 2017; Zuboff 2019), sometimes to the extent that the relationship between platform and workers may resemble traditional forms of employment (Muhl 2002; Oldham and Hackman 2010).

In sum, as an alternative to the dominant economics view of OLPs, emerging research on the control of work on OLPs is in its infancy. Yet researchers need to recognize that OLPs are not only markets but, increasingly, organizations. This motivates our rigorous analysis of case data and the systematic development of a conceptual model explaining OLPs as work environments. As a basis for this empirical investigation, we use the meta-theoretical lens of platforms as meta-organizations (Gawer 2014; Gulati et al. 2012).

## Meta-Organizations

We view OLPs that exhibit control of work as metaorganizations (Gawer 2014), in that they “solve the problem of organizing without explicitly relying on formal authority as enshrined in an employment contract” (Gulati et al. 2012, p. 580). Such platforms can be “usefully conceptualized as evolving organizations” (Gawer 2014, p. 1239), as they simultaneously “combine organizational and market mechanisms” (Constantiou et al. 2017, p. 232). The core of platform companies is small while the periphery is large (Gulati and Kletter 2005); they are a form of organized activity that allows work to be carried out by multiple actors in a coordinated way. This applies extraordinarily well to Uber, which has a small core, because it neither owns the physical resources (cars) nor officially employs human resources (drivers) yet it employs algorithmic decisionmaking to coordinate resources in order to offer a standardized, high-quality service to customers.

A deeper understanding of OLP work environments also requires examination of the role of technology. We use the notion of algorithmic management (Curchod et al. 2020; Lee et al. 2015; Rosenblat and Stark 2016) to conceptualize OLPs’ technology and information infrastructure. We define algorithmic management as the large-scale collection and use of data on a platform to develop and improve learning algorithms that carry out coordination and control functions traditionally performed by managers. This resonates well with literature on recent advances in digital technology, including big data and machine-learning processing capabilities (Gregory et al. 2020). It also resonates well with recent research on the increasing popularity of practices such as algorithm-mediated surveillance of workers’ behavior and performance (e.g., Kellogg et al. 2020; Newell and Marabelli 2015; Rosenblat and Stark 2016) and automation of management tasks that were previously the responsibility of middle management (Autor 2015; Brynjolfsson and McAfee 2014; Constantiou and Kallinikos 2015; Willcocks and Lacity 2016). However, it is also recognized that OLPs’ managerial agency is essentially performed through digital technology, suggesting that workers may perceive the algorithms employed by the platform company as their “boss” (Curchod et al. 2020). It is therefore relevant to investigate how the algorithmic management implemented in OLPs’ user applications affects platform work.

## Research Design and Methodology

## Design and Case Selection

To build new theory and answer our research question of how a platform’s use of algorithmic management influences platform work, we conducted an intensive study of a single case, with the purpose of generalizing from description to theory (Gerring 2007; Lee and Baskerville 2003). The spatially delimited phenomenon or unit observed here is the Uber platform and its dynamic relationship with Uber drivers. Our case selection was guided by the extreme-case selection technique (Gerring 2007), which is particularly useful for building new theory. The methodological value of this technique derives from the unusually high values for the variables of interest (Gerring 2007, p. 101-102). This facilitates theory development, as a case with such values can be considered as paradigmatic of the phenomenon of interest. The Uber platform scores highly on both algorithmic matching and algorithmic control, making it a particularly interesting case from which to build new theory on algorithmic management of work on OLPs. Rather than relying on statistical generalization, our mode of generalization is therefore analytical (Lee and Baskerville 2003).

## Data Collection

In three waves of data collection, we used multiple sources of qualitative data, including observations, written dialogue, and interviews. The period, amount, focus, and purpose of data collection in each wave are given in Table 1 (all data except those drawn from public dialogue are anonymized to ensure the privacy of our sources).

The starting point for this study was our observation that Uber drivers were switching between different platforms. In December 2015, an Uber driver sent one of us a text message offering a voucher for free Lyft rides. This critical observation aroused our intellectual curiosity and triggered more intense observations and discussions with drivers during Uber rides in our first wave of data collection (see Table 1). Two researchers on the team subsequently took further Uber rides, conducting observations and interviewing drivers. We identified several tensions. For example, UberPOOL rides were a major concern for drivers, as they were less lucrative. In contrast to UberX, where each passenger is picked up and dropped off before taking on the next ride, UberPOOL is a ride-sharing option where riders going in the same direction are matched with each other. Drivers were sanctioned by the platform if they repeatedly declined UberPOOL drive requests. In response, some drivers used systems from competing platforms, including Lyft and Juno, and continuously shared information to optimize their platform switching. In addition to these observations, we also learned that many Uber drivers were angry about their working conditions and low earnings.

In the second wave of data collection, we conducted semistructured interviews with Uber drivers during rides. Appendix A shows the initial version of our interview guide, which we adapted along the way to include more specific follow-up questions. In reflecting on the diversity of questions asked and answers received, we derived a list of topics for data collection (Table 1). Initial themes for our interviews with drivers in New York City and London included switching behaviors and drivers’ identification (with themselves as self-employed freelancers versus the platform company Uber), which had emerged during the first wave of data collection. We also became more interested in the tensions of platform work and how they interrelated with

Uber’s heavy reliance on algorithms to manage drivers. Thus, the themes of controlling drivers through algorithmic management and drivers’ reactions became key topics. We filtered the UberPeople.net website using keywords derived from our emergent observations, extending the dataset by combining data sources.

In the third wave of data collection, we interviewed Uber managers and engineers in different geographical locations in order to capture Uber’s perspective and to understand how and why Uber designed, implemented, and employed algorithmic management in its relationships with Uber drivers and riders around the world. Interviews with Uber managers helped reduce potential bias from incorporating only one side of the Uber platform—driver relationship, in our analysis. We updated our database with recent posts from the UberPeople.net forum in order to extend the period of our dataset and identify any potential changes in platformdriver relationships and day-to-day platform work. We also consulted public dialogues involving Uber employees. We were interested in the design of the platform’s algorithms, tensions experienced by platform workers, and how these were resolved.

## Boundary Conditions of the Theory Development

Our analysis of Uber’s approach to algorithmic management of platform work is based on certain assumptions that set the boundary conditions of our theory development. In what follows, we adopt Bacharach’s (1989) understanding of such boundaries as assumptions about values, time, and space to express how they apply in our case.

Both the members of our research team and the participants in our case study (i.e., Uber drivers, as well as Uber executives and engineers) were located in pluralistic settings characterized by the freedom to express personal viewpoints, possible tensions among multiple perspectives, and dynamic emergent changes (Eisenhardt 2000). These underlying values likely shaped both research team members’ and case study participants’ perceptions of reality and interpretations of events. Thus, applying our emerged concepts and theoretical model to another cultural setting, such as a more unitary, hierarchical, and authoritative setting, might produce slightly different results with, for instance, less pronounced tensions. Our theoretical model is also bounded in time, as the time period of our data collection (2015-2019) was marked by the rapid scaling and popularity of OLPs with considerable gaps in regulations. This research setting is likely to change once platform work has become a more established, perhaps even more regulated, category of work.

<table><tr><td colspan="4">Table 1. Data Collection</td></tr><tr><td></td><td>Method/Sources</td><td>Topics</td><td>Purpose</td></tr><tr><td>Wave 1:December 2015-May 2016</td><td>Observation of Uber drivers in their day-to-day work by taking Uber rides (36 rides, ~15 hours of observation)Informal interviews with Uber drivers during rides (N=15) in New York City (US)Broad reading of entries in the UberPeople.net forum, as well as publicly available accounts of Uber and its drivers</td><td>Drivers&#x27; communication and general behaviorDrivers&#x27; interactions with systems in the carRelationship between drivers and platformDrivers&#x27; switching behaviors</td><td>Verifying Uber as an extreme case: Uber scores highly on both algorithmic matching and algorithmic control, making this case methodologically valuable for building new theory (Gerring 2007, p. 101)Identifying the key theme for the case analysis and story: algorithmic management and its impact on platform work. A related theme is work tensions and workers&#x27; tactics for dealing with platform algorithms</td></tr><tr><td>Wave 2:June 2016-January 2017</td><td>Semistructured interviews with Uber drivers in New York City and London (N=19)Specific posts in the New York City or London UberPeople.net forum relating using specific keywords of interest, e.g., &quot;control,&quot; &quot;switch,&quot; &quot;freelance&quot; (N=1,092 post entries)</td><td>In addition to topics from the first wave:Uber&#x27;s reliance on algorithms to manage drivers and their reactionsNature of the platform worker in the conflicted middle between self-employment and employment-like workDrivers&#x27; feelings, emotions, and responses to control by the platformTensions experienced by platform workers in their everyday work environment</td><td>Understanding algorithmic management; platform work and tensions experienced by drivers; how platform workers are controlled by the platform, and how they respondBuilding grounded analytical categories and understanding their theoretical interrelationships:tentative analytical categories based on the data, including algorithmic management and platform workAnalysis of theoretical associations between dimensions of algorithmic management and specific tensions of platform work</td></tr><tr><td>Wave 3:July 2018-October 2019</td><td>Semistructured interviews with Uber employees and engineers (N=8) across different geographical locationsSpecific posts in the UberPeople.net forum to update our database with recent dataSelected public dialogue involving Uber employees</td><td>In addition to topics from the first and second waves:Uber&#x27;s perspective on algorithmic managementZooming into the design of platform algorithms, including any trade-offs and tensions and how they are resolvedChanges in the Uber platform-driver working relationship over time</td><td>Understanding Uber managers&#x27; goals, motivations, and actions in designing, implementing, and using algorithmic managementReplicating our findings to fill our emergent categories with more empirical content and improve our understanding of theoretical associations between conceptsEnsuring theoretical saturation, where further data collection and analysis would yield no additional insights</td></tr></table>

During the time of our study, we witnessed intense public debates, and Uber was involved in legal disputes in both countries (USA and United Kingdom) where we conducted our field work. The timing of our study may thus have influenced research team members’ perceptions of reality and study participants’ interpretations of events. In the future, judicial decisions and societal changes may shape both OLPs ways of organizing work and platform workers’ perceptions. Lastly, although we believe that algorithmic matching and algorithmic control, as the main elements of algorithmic management, may stand the test of time, the speed of AI and other technical advances are likely to further shape OLPs’ algorithmic management practices.

## Data Analysis

Data analysis and collection activities were intertwined across the three waves. We used a variety of methods and techniques, with varying emphasis depending on the stage in our theory development. Initially, we drew on Siggelkow’s (2007) “talking pig” metaphor to identify an interesting story and construct a tentative case narrative of algorithmic management at Uber. We revised the narrative many times as the contours of our emergent midrange model became clearer. Iterative coding of our evolving dataset over the three data collection waves resulted in the final categories, their interrelationships, and a narrative illustrating our theoretical model.

In our data coding, we adopted an open mindset to analyze data slices in many ways (Glaser 1978), and categorized segments of data with short names that both summarized and accounted for each piece of data (Charmaz 2014). Labels for the initial coding iteration included aspects of algorithmic management such as “tracking behavior,” “performance monitoring,” and “automatic implementation.” We used comparative methods wherever possible to establish analytical distinctions (Charmaz 2014) and to develop the categories of “algorithmic management” and “tensions of platform work,” which eventually became our core focus. Specifically, we made within-source comparisons (e.g., comparing a data slice from one part of a forum thread with another, or from an initial interview with a later one) and cross-source comparisons (e.g., comparing sampled written dialogue from the UberPeople.net forum with interview data). We also compared and contrasted different viewpoints, including the voices we were trying to capture (platform company, drivers and customers) and our own perspectives.

To tackle the well-known problem of wrestling with preconceptions in coding for new theory development (Charmaz 2014), we invited an unbiased additional author to the team at a later stage of our research. This triggered a complete recoding of our dataset, comparison of the results with previous coding, and intensive discussions within the team of coders to develop a shared and internally validated interpretation of the data.

Once our coding had become more focused on the most significant codes from our initial coding phase and the core categories had stabilized across the three waves of data collection, we used Gioia et al.’s (2013) template to create data structures. We developed first-order categories based on the coding described above, while ensuring that the codes remained close to our data and interviewees’ experiences and perspectives. We abstracted from these first-order categories to second-order themes, which foregrounded the interpretations and perspectives of research team members while ensuring connection between the two coding levels. We then aggregated interrelated second-order themes, resulting in the final data structure presented in this paper.

Finally, we synthesized our findings and developed an elaborate model. At this stage, diagramming became important in developing a visual representation of the final categories and their relationships (Charmaz 2014). Viewing our coded data through the lens of our conceptual background helped us to focus our theory development and make important foreground/background decisions, such as placing tensions in the foreground, and switching and other driver tactics in the background of our study, despite our initial focus on the latter.

## Findings

## Case Introduction

Founded in 2009, Uber Technologies Inc.’s ride-hailing platform employs more than 19,000 people, operates in more than 700 cities and 63 countries worldwide, and connects 91 million monthly active platform consumers (i.e., riders) with 3.9 million drivers to complete 14 million trips each day.<sup>2</sup> Former CEO, Travis Kalanick (2016) explained how Uber creates benefits for both riders and drivers simultaneously:

UberX, when we first started, was literally 10 or 15% cheaper than our black car product. It’s now in many cities, half the price of a taxi. And we have all the data to show that the drivers are making more per hour than they would as taxi drivers. What happens is when the price goes down, people are more likely to take Uber at different times of the day than they otherwise would have, and they’re more likely to use it in places they wouldn’t have before. And what that means for a driver is wherever he or she drops somebody off, they’re much more likely to get a pickup and get back in. And so what that means is more trips per hour, more minutes of the hour where they’re productive, and actually, earnings come up.

Viewing himself as an entrepreneur who thinks like a math professor, he described the kind of culture he had created at Uber: “at Uber we like the hard problems and we like getting excited about those and solving them.” Following this mindset, Uber has built a strong platform capability to collect and analyze data on each platform user in real time, feeding a variety of algorithms that “manage” users and create the best possible matches between supply and demand in any location and at any point in time. This use of algorithmic management creates a novel platform work environment that we explain in the following case analysis.

## Findings Part 1: Algorithmic Management

Management is generally concerned with coordinating and controlling organizational resources and activities to achieve defined organizational goals and objectives. Uber’s management is qualitatively different, as it must be highly efficient and scalable, and involves resources and activities not wholly controlled by traditional managers. To ensure a consistently high-quality experience for platform consumers and scale its operations to match global supply and demand, Uber employs algorithmic management. This is defined as a platform’s large-scale collection and use of data to develop and improve learning algorithms that carry out coordination and control functions traditionally performed by managers in a highly automated and data-driven fashion.

Uber makes extensive use of algorithmic management to manage a distributed workforce efficiently and accurately, city by city. Based on our interviews with Uber managers, we identified two aggregate dimensions of algorithmic management: algorithmic matching and algorithmic control (see Figure 1). The former involves market-like coordination of human resources, whereas the latter involves a tighter form of control akin to managerial control in hierarchical organizations. In continuously tweaking its approach to algorithmic management, Uber balances these two extremes, creating a work environment in the conflicted middle between market and organization that is full of tensions.

## Algorithmic Matching

Algorithmic matching is the algorithmically mediated coordination of interactions between demand and supply. Three second-order themes in our data structure—algorithm as marketplace, use of input and output data, and dynamic pricing—explain its key facets.

Algorithm as marketplace: One role of algorithms on the Uber platform is to create a better, scalable marketplace. Uber uses algorithms to optimize matching of supply and demand, searching for the most beneficial matches for both sides of the platform. As an Uber executive explained:

When we think about how matches actually happen between riders and drivers, then this happens algorithmically, and what we are solving is for riders and drivers in aggregate to get the best possible matches for the marketplace. We have our definitions of what is the best possible match, and we have accessibility tested that and make sure that it helps both riders and drivers equally.

However, there are limitations to using algorithms to influence platform users and ensure the best possible matching because, according to another executive we interviewed, Uber cannot tell drivers what to do:

We see drivers as our customers as well, and while we do use algorithms to manage drivers, there are many limitations to what we can do—not due to technology, because there is a bunch of things we could do, but because of legal limitations. Because drivers are not normal workers, employees, it means we can’t tell them what to do. We can’t tell them to work x number of hours a day, for example. The only thing we can do is use the algorithms to incentivize drivers.

Thus, riders and drivers make their own decisions on whether and when to enter exchange relationships on the platform. One Uber executive emphasized that “riders and drivers make transactions” and that management under these circumstances means “making sure that information is available for both sides to facilitate decision-making.”

Use of input and output data: To ensure faster and more accurate matching of supply and demand on the platform, the algorithms are fed with input and output data. First, drivers and riders share data on profiles, ride requests, locations, and time availabilities, which are collected and used as preliminary inputs for algorithmic matching. An Uber executive shared an example:

If you have a driver who has, let’s say, that have a vehicle model that is actually eligible to receive requests from several products like Uber Black and Uber X, for example, then the drivers actually themselves can choose which products they want to receive requests from.

Second, effective algorithmic matching also relies on marketlevel performance or outcome data. Riders rate drivers, and the resulting rating scores help Uber to draw inferences about drivers’ performance and feed the matching algorithms to ensure the best possible experiences for riders: “The biggest thing to us is the customer rating. If a driver’s rating falls below a certain level then there would be some sort of like, yeah, there was some sort of action taken.”

Finally, market-level data collected and used by the platform’s matching algorithms include network size to optimize the platform according to network effects. An Uber executive said:

Effectively we operate under principles of economies of scale: the larger the network itself, the more benefits that network brings, and I guess that also helps us make better decisions when matching riders and drivers. So, what I’m saying is, it changes in time, and it’s dependent on the city’s size, the maturity level, if it’s fast growing or not, and so on.

![](/api/attachments/EHGV6B2H/fulltext/images/82a9610d25ce165acaa15de0f4da315d84a58f32aef8d9651bec1e25cf85ebcd.jpg)

Dynamic pricing: One of the key algorithmic matching mechanisms emerging from analysis of the Uber case is dynamic pricing, which focuses on achieving the highest possible levels of economic efficiency and effectiveness in matching supply and demand, depending on current market characteristics. Uber tries to influence the economic system by using clever pricing strategies to ensure that drivers go online when customers need rides. An Uber executive said: “it all just has to do with economics then, and then you try to influence this economic system to balance the supply and demand in a way that the drivers react to it online when the customers need rides.” Setting the right price is difficult, as the price sensitivity of demand and supply must be carefully calibrated. Optimal prices make drivers come online without killing the rider base:

At that point, you can just look at all the data and you can analyze, you can see at what price drivers are happy to drive for, like how much money they have to make today to come online consistently, how much is too much which then kills the rider base, how much is too little which then causes them to quit, when the best times of the day are.

Surge pricing is a key mechanism implemented to ensure that both sides of the platform derive benefits. The platform uses “surge,” meaning a higher fare, to incentivize drivers and reduce temporary driver shortages in specific areas. Individual drivers may benefit from higher earnings, although passengers may be put off, challenging Uber’s interest in maintaining overall demand:

The way the whole thing is set up is really designed to be like an economic system where you can adjust the price to influence the rider behavior, and therefore the driver behavior. If you need more drivers online at a certain time, you can increase the price a lot. If you’re trying to attract more drivers onto the system, you have higher pricing at certain points in the day.

## Algorithmic Control

Uber positions itself in the market as a matchmaker, a platform, or simply an app. Therefore, unsurprisingly, algorithmic matching is the most salient form of algorithmic management focused on coordination. Yet, Uber also employs algorithmic control to offer standardized, high-quality service to customers. Algorithmic control refers to the use of algorithms to monitor platform workers’ behavior and ensure its alignment with the platform organization’s goals. We identified three second-order themes—algorithm as boss, use of process data, and behavioral nudging—to explain algorithmic control.

Algorithm as boss: The role of algorithms in controlling platform workers (i.e., drivers) is to define and enforce common standards and rules to ensure that workers’ activities align with meta-organizational goals and KPIs (e.g., timely acceptance of new ride requests and low frequency of cancelations to avoid pick-up delays). In traditional, hierarchical organizational contexts, managers can directly oversee workers’ behaviors and ensure behavioral compliance and alignment, whereas in Uber, the algorithm is perceived to be “the boss” (many drivers we interviewed used this language). Relying on algorithms rather than human managers to control drivers’ behavior has the obvious advantage of greater scalability, but also creates a perception that “the system runs itself”: “For the business itself, it seems to me that the bigger and bigger and bigger it gets, the more it becomes just economic, like how the whole system runs itself and the less people you need, actually, to run the algorithmic management of the business.” More specifically, some algorithms are perceived as the boss because they have inbuilt technological rules and standardized processes to actively control drivers’ behavior:

Yeah. There was a lot of active control like I said. There were a couple of these rules for logic. There should be rules that we program into the app. For instance, if you don’t accept three trips in a row, the app will just switch off for 15 minutes or whatever. If you switch it off, you have to turn it back on. There was one that was designed to switch the app off for drivers who weren’t actually driving.

These algorithms put in place to control drivers also appear to function like a boss because they automatically enforce sanctions on undesirable driver behavior. This refers mainly to banning drivers from the platform (temporarily) if they do not behave as expected:

There are those issues where we try to address, issues with rider or driver experience, with education and just communication, and I think historically there have been sanctions in place, by sanctions meaning, for example, that we would log off the rider or the driver if they don’t except dispatches or they keep canceling on riders.

Internally, Uber promotes discussion among its engineers and executives to define “fraudulent versus nonfraudulent” driver behavior as a basis for algorithm design:

We do sanction for situations where the driver has attempted to defraud the rider, for example, and you can imagine that we are putting a lot of resources into identifying fraudulent behavior and understanding what is fraudulent versus nonfraudulent. And this is something where we also need to be quite strict. In case there is a fraud, fraud is usually only for the benefit of the driver, and it hurts rider experience and sometimes hurts them financially, so we need to be super strict about that.

Use of process data: Performing algorithmic control and functioning as a “boss” would not work without fine-grained process data to help monitor drivers’ behaviors in great detail. When drivers log into the Uber app, every move is tracked, and detailed information is collected and analyzed in real time using the platform’s learning algorithms. As one Uber executive explained: “We do track it [driver’s behavior]. We track it really closely. But what we do with that information, I think, is the important thing.” Another interviewee explained that nowadays most such algorithms are machine-learning algorithms that continuously improve themselves according to defined goals, shaping drivers’ behaviors. These include, for example, drivers’ acceptance rates, pick-ups, and changing GPS locations. For example, if a driver chooses not to accept a request, this information is immediately captured by the system:

If the driver chooses not to accept the trip, for example, then we redispatch the trip to the next driver, if they want to accept that. So, when the driver does accept the trip, we provide navigational guidelines to help the driver rather than force them to stay on that route, whether it be Uber Pool, whether it be anything else.

Collecting individual data points on platform processes will often not provide a comprehensive picture of drivers behaviors. To gain a better account of each driver’s behavior, several different data points are combined to draw more accurate inferences:

Let me give an example. So, let’s say we have drivers on the platform and they receive requests: they accept a request, but they don’t move for ten minutes and then the trip get canceled for example, and the driver gets the cancelation fee. So, is that fraud, or is that a bad behavior?

Behavioral nudging: Learning from behavioral data on each driver allows the algorithms to iteratively improve their attempts to alter drivers’ behavioral choices on the platform in a subtle and informal way (i.e., without using formal mechanisms such as incentive pay), and without forcing them to do so (i.e., not formally banning them from the platform). An Uber executive explained the basic idea behind this form of nudging:

We have to influence the behavior of drivers but without forcing them, by showing them the best way and showing, or a lot of times explaining, why this is the best way of doing things. This is oftentimes a challenge, because here in the Brazil market alone, we are dealing with over 500,000 drivers. With these numbers, how can you make sure that each individual transaction works really well? So, you have to rely on the algorithms.

Behavioral nudging is based on the predictive capacities of machine-learning algorithms. For example, algorithms are used to optimize tasks such as job allocations to individual drivers through predictive forward dispatch. An Uber executive explained:

There is a feature that we added to the platform years ago which is called “forward dispatch,” which means that when drivers are on the trip currently, then if we know where their trip is going to end, technically make them available for dispatch for the next riders, right?... So, the reason why we did that is we actually have, when rider and driver are currently on the trip, we already know where they are heading, and we might as well make sure that the driver is available to receive the next dispatch faster.

Another example is the provision of information such as upfront pricing (which, unlike incentive pay, is not a formal mechanism), encouraging drivers to take shorter routes:

We have a few technologies built into the app, for example like upfront pricing, where you open up the app and see the price upfront, right? Enter that price, and whatever the route is that the driver takes, it should still be your price, right? And the driver also knows that, so the driver actually has an incentive to complete the shortest route. Like, if we think about all the kinds of exceptions—so whether the driver is on purpose trying to take a longer route to, you know, make more from that trip—this is something we again classify as fraudulent behavior, right?

Indeed, Uber’s tendency to nudge drivers’ behavior has been addressed in public media reporting how Uber uses insights from behavioral economics, for example, to “nudge them into driving longer” (Scheiber 2017) through psychological tricks such as alerts, pop-ups, and text messages.

## Findings Part 2: Tensions of Platform Work

As already indicated, Uber’s use of algorithmic management impacts and shapes platform workers’ behaviors and everyday work practices. Our analysis reveals tensions in terms of work execution, work compensation, and the sense of belonging experienced by Uber drivers as platform workers who find themselves in the conflicted middle between self-employment and employee-like work (see Figure 2).

## Work Execution Tension

While executing platform work, drivers reported experiencing tensions between the autonomy of a flexible job on a matchmaking platform and the lack of flexibility to diverge from instructions programmed by algorithms.

Autonomy: On the one hand, drivers seem to enjoy considerable autonomy. For instance, they reported flexibility to create and adapt their own work schedules. A new driver seeking feedback from the online community posted:

I just passed the exam to get my license. I’m thinking of making this my schedule: tues, wed, thurs 7am-1:30pm. Fri and sat 11pm-2am. Sunday off. Monday 6am-5pm. What do you think I can expect to make?

While drivers of black cabs (in London) and yellow cabs (in New York City) are allocated to set work shifts, Uber drivers choose when and for how long they wish to work on any given day and which area they prefer to serve. A New York City driver expressed her feeling of being in control of her own work: “You are your own boss. If you want, you work; if you don’t want, you stay home. It depends on you.” Drivers seem to enjoy the freedom of logging on and off whenever they liked: “I work five hours in the morning, take a break, then five hours at night. Or if I got a job to do, or another gig, I just sign off the app and go get that money. I jump in and out of the app as I please.” In enjoying the selfemployed-like characteristics of platform work, drivers also reported feeling like it was easier for them to keep up with family commitments during the day:

You know, it’s not difficult to start a job. You can rent a car and you can, um, you can work any time. If you have an important appointment, you can stop the job, you can do a different appointment, you can look after your kids. That’s why I prefer this job, it’s good.

Being able to pursue education was highlighted as another benefit of flexible platform work:

I want to get out of the office life, jump-start my freelance career and pursue another bachelor’s. Uber/base work will just be the bridge. I will go hard full-time and also work on building my freelance work. I plan on it for one to two years. Maybe longer, who knows?

![](/api/attachments/EHGV6B2H/fulltext/images/69aaadf561ef0a130e9695f83c6d799b280e593d4f43cf55de9b72b2ad5f7d78.jpg)

In our interviews, autonomy seemed to be an overarching theme of having a flexible platform job. Drivers stressed that they enjoyed not having a supervisor looking over their shoulder, and expressed their satisfaction about working in a non-hierarchical environment: “I see those guys, they are having bosses telling them off—‘don’t use your cell phone’ or something like that, you know? ‘You can’t go in the restroom right now,’ or you know…”

Supervision: On the other hand, despite drivers’ claims that they “answered to no one,” they clearly also experience close supervision by the platform, as they reported having minimal flexibility to diverge from instructions given by platform algorithms. They expressed a sense of being controlled, having to comply with policies, rules, and terms of service enforced through the app. When “on the clock,” they reported that their actions were supervised and constantly controlled by algorithmic instructions. According to one driver: “Everything is controlled by Uber. And when a customer gets into your car, your responsibility is to drop him to his or her destination and that’s it.”

Our analysis of how work was being executed shows limited freedom and room for maneuvering among drivers, with virtually no wiggle room to diverge from algorithmic instructions, particularly with UberPOOL. Although drivers generally consider UberPOOL rides to be less lucrative than UberX rides, some drivers reported being banned from the platform if they repeatedly declined UberPOOL requests. One driver commented: “Let’s say we took a shortcut, like trying to stop taking Uber rides—UberPOOL rides—and once we do that they will shut you off.”

Drivers were particularly concerned about the risk of “getting canceled” through account deactivation if they did not comply with the platform rules and algorithmic instructions. They also expressed discomfort about not always being able to fully satisfy passengers’ demands. This can occur, for example, when a passenger orders a shared UberPOOL ride, only to realize that this meant complying with the system’s routing app and driving instructions, with little flexibility for the driver to adapt to special client requests. In an interview, a driver explained:

On POOL, they use their own system. And once you press the navigation, it comes directly as their own system, you cannot use any other… I have no choice; you’re following it even if you get stuck in the traffic, and it may take you to [the] wrong places.

Drivers experienced tensions between algorithmic supervision and a sense of autonomy in determining the timing and location of their work. Many said they felt “controlled” by the algorithm. One London driver said: “It seems to me that Uber is behaving like an employer by dictating which jobs drivers should take.” Tension between the drivers’ autonomy and algorithmic supervision can manifest in conflicts between drivers and passengers. A driver recalled an experience:

She [the passenger] starts fighting with me: “why are you not dropping me first?” I said, “Miss, if you have a problem, just order UberX. It’s UberPOOL; it’s all about the Uber system, so I am just driving how they’re telling me to drive.”

Drivers blamed the algorithm for its lack of flexibility to accommodate special demands, and sometimes felt frustrated about having to follow the system’s instructions.

## Work Compensation Tension

Another tension experienced daily by Uber platform workers relates to work compensation: uncertainty about exact earnings due to possible cancelations, sanctions, and so forth, combined with trust in the algorithm to provide repeated and profitable jobs.

Uncertainty: Drivers also reported experiencing uncertainty about how much income could be achieved, manifesting in various ways before, during, and after conducting platform work. Before starting a work day, drivers stated that they were typically uncertain how many rides they would be allocated by the algorithm. From short to long rides, and less to more profitable work, drivers emphasized that they needed luck when starting a work shift. During platform work, drivers also expressed uncertainty about whether an allocated job (i.e., ride) would be canceled, increasing their idle time and reducing their income. They reported sometimes being sent to a specific location by the system, only to have their ride canceled along the way. A driver in New York City complained:

We’re going to Chelsea Bridge now, right? And if it was UberPOOL, somebody could send me a job from Fifth Avenue and let’s say 45th Street, or even 9th Avenue and 50th Street, and they may cancel it, but by the time they cancel, you’ve already made this left. So, you know, it’s a lot of headaches in the city … it doesn’t make any sense.

Added to the uncertainty about earnings, other sources of negative experiences include traffic and rush hours. Drivers who get stuck in traffic on their way to a passenger risk getting canceled. Drivers also expressed that it was very difficult to calculate the exact earnings for each ride, particularly with the ride-sharing system. When working for UberPOOL, drivers stated that they had no idea how much each passenger would end up paying. A driver explained:

They don’t pay the base fee, the minimum. Like for instance, you’re hiring this cab right now, you pay what we call the base fee and plus mileage and time. But if then in the UberPOOL the second customer comes in, he doesn’t pay the base fee, and automatically once I accept the second in, my meter will be frozen. Until I pick up that customer, the first customer is not paying me anything, and once I pick up the second customer, if the second customer gets off earlier, you find out the way the portion of his payment, he can go for almost a mile and pay \$2.50 and get off the cab. That’s wrong. Yeah, that’s wrong.

Drivers generally expressed feeling a lack of transparency about how the algorithm worked, not least in terms of allocating rides and calculating their earnings. The drivers stated that their earnings statements were not updated until several hours after a ride had been completed, giving them little opportunity to know in the moment how much money they were making. A driver said: “I don’t know what they do, you know … It should be like a meter you know? When I finish the ride, I have to see how much I make, right?”

Another source of uncertainty stems from passengers evaluations of drivers. At the end of each ride, passengers typically rate drivers on a five-star scale. Drivers reported that their evaluations varied greatly, sometimes due to circumstances beyond their control (e.g., weather conditions, traffic, surge pricing). Unfavorable driver evaluations negatively impact future job opportunities on the platform, further increasing uncertainty. A driver explained: “If you have a good rating, they always give you the good customers. And good customers means the long rides. Yeah. If you don’t have that, you have the bad rating, then they’re not going to give you the good customers.”

Repeatability: Despite uncertainty about their exact earnings, drivers generally reported trusting the algorithm to provide repeated and profitable job opportunities. Unlike traditional taxi drivers, Uber drivers do not need to look out for passengers hailing taxis on the streets. A driver explained:

You don’t have to go out there and source your own passengers, to go and look for the passengers. In [the] case of Uber and Lyft, they have the passenger database already; all you need to do is jump into the cab and they will send you the passengers.

In addition, unlike self-employed workers, Uber platform workers do not need to advertise and market themselves. When logged into the Uber system, a more or less steady stream of ride requests from passengers is almost guaranteed by the algorithm, which efficiently matches supply and demand. Thus, drivers trust the platform’s ability to supply work and earning opportunities on an ongoing basis. One manifestation of the perceived earning opportunities from working on the Uber platform is the high geographical density of aggregate demand, ideally allowing the platform to offer drivers repeat jobs on their preferred routes. For example, drivers can communicate their home address as the final destination of the day. The platform will then create a route that ensures multiple jobs on the way home, maximizing the driver’s available time and earning opportunities on that route:

From Uptown they are going to give you the customer which is going towards the Downtown, OK? And you enter the Downtown, they are going to send you another customer which is going to Brooklyn from the Downtown, so that’s how they can keep giving you the rides, and you will finally, you will go near to home.

Since the platform can only provide repeated jobs on desirable routes in very busy areas such as central London or central New York City, many drivers expressed tension between trusting in the platform’s supply of repeat jobs and uncertainty about their overall earnings. Drivers stated that this tension often causes anxiety and affects their willingness to work long hours. One driver said:

If you are putting in maximum hours, like 72 hours, 80 hours per week, you are making enough money. You are making good money, instead of any other job … If you work 60 hours or 50 hours, you are going to make like \$1,500 easy … and \$1,500 is going to be some gas money. You can say \$150 and then \$50 other expenses, \$200 for the car, and after that I think \$1,000, \$1,200 left. If you put in 60 hours, it’s like 10 hours per day and six days per week.

To increase their earning opportunities, some drivers reported actively looking out for so-called surge areas. A driver commented on the UberPeople.net forum: “I have no shame in switching off for 20 mins and driving into a surge area that I want to be at, get one job an hour instead of carrying people cheap all night long, wasting fuel and wearing my car seats out.” In summary, drivers expressed considerable uncertainty about earnings, yet, also generally trusted that the algorithm would provide repeated and profitable jobs.

## Worker Belonging Tensions

The third tension of platform work characterizing the new work environment of algorithmically managed platforms relates to platform workers’ sense of belonging. Such tensions manifested in drivers’ self-identity as independent workers versus being part of a larger community working for algorithms that everyone is seeking to understand.

Self-identity: Many drivers identified themselves as independent workers and their own bosses, rather than as members of the Uber company. In this respect, their selfidentity was often expressed through their self-employment status:

For me, the identity, that’s how we identify ourselves, as Uber drivers … I see myself as being self-employed. I don’t have to answer to anybody. It works for me. I don’t work well for a boss, and I haven’t done that in 20 years. I’ve been independent.

In public communications, Uber avoids labeling drivers as “employees,” instead referring to them as “partners.” However, many drivers mocked this term, stressing their independence:

Now we are partners? You take 40% of the fare, we give our sweat, blood, and expenses, and you call us partners? What kinda partnership is that? You get to wear the pants while I do everything and I’m still stuck with the bills? Partnership? Partners? Employer? Master?

When asked whether they would “brand” themselves as members of Uber by wearing t-shirts displaying the Uber brand, one driver stressed that he would rather not do so: “Well, it wouldn’t be a good thing to do because it’s not, it’s not an employed work, it’s an independent operator thing.”

Our findings reveal that many drivers did not wish to be affiliated with Uber. One driver self-confidently emphasized how drivers “should not take the side of Uber,” as they have their own identity, and even if Uber “would go bust,” drivers would still find new job opportunities:

Use Uber, don’t get used by them! Don’t take the side of Uber. Uber is not a human who will understand your pain. Uber never listens to drivers or pax and never will in future! … Company comes, company goes. Who cares? Something else will come if Uber goes bust. What makes someone loyal to Uber? It’s an app.!!!!!! There is nothing to be loyal!!!!!!!! Use it or delete it!

Perceptions of their self-identity as independent workers were further amplified by the fact that platform work typically does not involve working in groups or teams. Drivers spend most of their time either by themselves or with passengers with whom they have brief human interactions. Unlike traditional taxi drivers, who seem to have more opportunities to socialize at designated taxi stations and talk directly to employees at their taxi dispatch firm, the Uber drivers we interviewed typically did not know any other Uber employees. Socialization with colleagues and direct communication with superiors typical of traditional work environments were very limited in the platform work we observed. When drivers need support, they usually have to communicate with Uber via the app, or by email with automated responses. The drivers we interviewed found this form of communication with Uber employees and interaction with the platform to be frustrating. One driver complained: “You email everything ... If something goes wrong with your app, you just have to wing it.”

Community: Although drivers stated that they cherish their self-identity as independent workers, they also consider it important to be part of a broader community of drivers. Many reported trying to compensate for the lack of membership of the Uber company through engagement in informal communities of Uber drivers in online forums such as UberPeople.net, in social media groups, on WhatsApp, and through informal offline conversations with other Uber drivers (e.g., when waiting to be matched to a ride at the airport or with friends also driving for Uber). When asked whether Uber plays an active role in building and nurturing the community of drivers, a driver from London responded: “Uber does not do that.”

In the absence of Uber-sponsored membership, UberPeople.net is one of the largest online communities used frequently by drivers. In this forum, drivers connect with each other, creating a group identity and allowing workers to feel part of a community of drivers:

Just want to take the time to thank you all. I know that I hit heads with many. I know that some have completely opposite opinions that the ones I share and promote. But still, being part of this community of drivers, help me immensely go thru very dark times.

In this forum, drivers can share personal stories and provide mutual support. A driver from New York City shared quite detailed forum tips with others, seeking to help drivers to navigate through the difficulties they might be facing as Uber drivers:

Respect yourself and remember that these companies are worth jack without you. Don’t allow yourself to be abused by pax, and don’t worry about receiving a few bad ratings here and there. Everybody drops in the beginning, but good drivers bounce back up in the long run. But you must remember to always keep polite and professional. Be nice, even when you are kicking someone out of your vehicle. And don’t forget to get a dash cam that records inside. NY is a one-party wiretape state, but even if it wasn’t it is a lot easier to answer the accusation of illegal recording than one of physical abuse, sexual misconduct and/or rape. Remember that you never know who is getting into your vehicle and there have been numerous stories of drivers being falsely accused by passengers. A dash cam is your friend.

The algorithmic “black box” seems to motivate drivers to join global online communities like UberPeople.net or social media groups to exchange thoughts and insights into how algorithms work and how to optimize behavior to get the most out of them. An Uber executive explained:

A lot of people get together in the same WhatsApp group and they try to understand better how to make money on the platform … Trying to understand and trying to improve upon the work … just look at something comparable, like Craigslist: there is not the same tendency for people to get together as we see it on the Uber platform. I would compare it to Youtube, where you also see content creators flocking together to understand the algorithms better.

Our findings for all three tensions suggest that platform work in the conflicted middle between self-employment and employee-like work, shaped by algorithmic management, is characterized by tensions in work execution, work compensation, and workers’ sense of belonging.

## Part 3: Platform Workers’ Responses

A recurrent pattern in our data was drivers searching for coping strategies to deal with the tensions of platform work (see Figure 3). Response behaviors took two forms: mainly during platform work, drivers assumed free-market agency (i.e., market-like behavior), whereas before and after platform work in the public space, some drivers assumed an employeetype status (i.e., organization-like behavior).

## Market-Like Behavior

We identified a variety of responses to algorithmic management by platform workers participating in the Uber network. We distinguish between the market-like responses of bypassing and switching, and the organization-like responses of striking and embracing.

![](/api/attachments/EHGV6B2H/fulltext/images/d4536f541bf735c85c1982e21b8ed645abf449487b6d50988a085bfaffaae8bc.jpg)

Bypassing: In some cases, platform workers reported rejecting platform instructions and refusing to carry out requested jobs, either completely or exactly as prescribed by the algorithm. They also admitted to canceling passenger ride requests and temporarily deactivating the GPS or Uber app on their mobile devices. They shared experiences of actively blocking the Uber system, making comments such as: “If possible refuse all pool trips. Great for Uber, bad for us,” and “Turn on all apps and ignore pool and Lyft line jobs. Trust me, you will be happier.” One Uber driver stated:

If you do not want to take uberpoop rides then just ignore them. After about 2-3 days of ignoring them you will not receive any more. I have not received an uberpoop request in months. I guess uber thinks they are punishing me by not sending me any more...poor me. LOL.

Motivations for such responses to algorithmic management varied, but generally related to the idea of not wanting to blindly follow an algorithm while executing the work or to simply maximizing individual utility as a free agent. Besides simply ignoring notifications and incoming requests, we also encountered cases where drivers used online communities as a vehicle to form coalitions and “game” the system by strategically logging on and off the platform:

Driver A: Guys, stay logged off until surge. Driver B: Why? Driver A: Less supply high demand = surge. Driver B: Uber will find out if people are manipulating the system. Driver A: They already know cos it happens every week. Deactivation en masse coming soon. Watch this space.

Uber generally instructs its algorithms to prevent bypassing behaviors as much as possible and to enforce sanctions where necessary. Bypassing algorithmic instructions is treated as “fraudulent” behavior when it surpassed a certain threshold. Interestingly, drivers reported that, over time, Uber was able to identify some of the loopholes and constantly updated the system in order to make it more difficult for drivers to game the system to their advantage.

Switching: Another market-like behavior we observed that is (now) generally tolerated by Uber is switching between alternative ride-hailing platforms and marketplaces during the same work shift. Drivers in New York City typically have multiple platforms from which to choose, including Uber, Lyft, and Juno. They often work for more than one platform simultaneously, allowing them to compare the attractiveness of jobs (i.e., rides) across platforms, and to switch back and forth between different systems as they saw fit, to take advantage of the best earning opportunities. A key motivation for switching behavior is to minimize idle time and maximize earnings. To do so, drivers use multiple smartphones simultaneously, each connected to a different ride-hailing platform. When they become idle or are getting close to finishing a ride, they accept new ride requests on a “first come, first served” basis. We retrieved the following conversation between drivers in the forum:

Make the switch to Lyft and save our jobs while we have a chance. Uber just wants to give our jobs to machines and keep lowering rates.

We all know that these companies like to offer better incentives to drivers that miss some time. So, drive Uber for one week, Juno next, Lyft third, etc. I switch between Uber/Juno weekly.

When asked about responses to switching behaviors, an Uber executive explained that the preferred approach is not sanctioning but incentivizing (e.g., premium earning opportunities) so that drivers would choose Uber from among the competing platforms. Switching behavior was a less dominant issue in London when we gathered our data, because no major competing ride-hailing platforms had entered the local market. While some London drivers reported working for other mini-cab companies, these did not allow “ride-to-ride” switching because they used advance bookings rather than ad hoc rides.

## Organization-Like Behavior

Striking: There have been instances of Uber drivers organizing and openly participating in strikes, behaviors typically associated with employees working for an organization. Some of these attempts happened in local markets, while others sought to globalize and attract Uber drivers from other cities or countries. Other strikes were joined by drivers from other ridehailing platforms, such as Lyft drivers, as observed in New York City in May 2019. Similar to strikes against other OLPs such as Deliveroo and Instacart, the focus of these strikes is generally to attract public attention and raise awareness of the challenges posed by working conditions. As one driver stated: “The purpose of the strike is to call media attention—calling attention to the suffering of the drivers. With a fragmented work force, we are never going to get a full strike.” In the online forums, many drivers appealed to individual freedom and workers’ right to strike, claiming that Uber could not prevent it: “You are within your rights to strike or not strike. It is a personal decision after all. I chose to strike and that is my decision.”

As a foundation for organizing more powerful strikes, we also found evidence of Uber drivers in some geographical regions where Uber operates attempting to form unions. To do so, they leveraged the massive participation in online forums to form coalitions, but these attempts have been unsuccessful. One driver complained: “We are not supposed to make a union. We are struggling, we are trying to go to different forums where they just give us permission to make a union. But we don’t have any union yet and we can’t form a union yet.” Uber drivers have justified their attempts to unionize by appealing to the ongoing political and public discourse on Uber’s responsibilities. One Uber driver stated very directly: “Uber was in court last week, in case you forgot. They are breaking the law. Why stand for this?”

Embracing: Despite this evidence of “negative” or “neutral” responses to Uber’s algorithmic management, many drivers said they were happy and showed signs of embracing the Uber platform and its opportunities. One way in which embracing the Uber platform has become salient is through drivers repeatedly expressing their gratitude for a new earning opportunity and easy market entry. Many drivers truly enjoy their jobs on the platform. A driver interviewed in London explained:

Um, I think it’s a good thing because if … You know, it’s not difficult to start a job. You can rent a car and you can, um, you can work any time … So I would say, yeah, I would see what will happen; but as I told you, I’ve been here six weeks, so if I am happy then I will continue.

Some drivers we interviewed had already participated for longer on the Uber platform, showing signs of loyalty. Another London driver said: “I have been working for Uber for 1.5 years. If I don’t like it I stop doing it. I am happy with Uber now. They say minimum wage, but you never know. I hope the best thing comes to us, the drivers.” Loyalty to the platform went as far as wanting to contribute to further developing it and becoming part of it:

Sometimes they call us for a meeting. And they do research: “everything going alright?” I mean, what kind of ideas we come up with to make it better, do you know what I mean? Sometimes they will phone us and ask us … Well, they phone me anyway, ask us for my opinion. Because in two months’ time I’ll be here. I’m three years.

Finally, in another instance of embracing the platform, we encountered Uber drivers actively recommending Uber to others to encourage them to join the platform as well. Because entry barriers to becoming an Uber driver are comparatively low, drivers’ private networks have turned out to be a valuable source of new recruits. One explained why he joined the platform:

Yeah, a friend. I didn’t see that in the news or magazine or newspaper but friend, yeah. That’s why I start for this job. Then I am using someone’s car. This car belongs, I lent, because I want to see how it’s going; or if I’m happy I’m going to buy a car, I am going to stay, continue with it.

In summary, platform workers’ responses to the platform and algorithmic management varied from market-like to organization-like and were perceived by Uber to be either positive (embracing), neutral (switching), or negative (bypassing).

## Model and Theoretical Integration

The model depicted in Figure 4 synthesizes the findings of our Uber case study. It incorporates the view of OLPs as metaorganizations and highlights that platform workers experience platform work as both a market and a controlling organization (compare the left-hand and right-hand sides of the model).

![](/api/attachments/EHGV6B2H/fulltext/images/60c92a02544d1c76a5578b2f5915609c196949276ba74518681f564616283ccb.jpg)  
Figure 4. Algorithmic Management of Platform Work on Online Labor Platforms

The model explains the antecedents, characteristics, and consequences of OLPs as work environments. First, we find that the design, implementation, and use of algorithmic management is an antecedent to platform work on OLPs, providing a new scalable form of management that can deal with a rapidly scaling user base (Huang et al. 2017) but is not bound by the number of employees who can perform managerial functions at the operational level. Compared with previous literature (e.g., Curchod et al. 2020; Kellogg et al. 2020; Rosenblat and Stark 2016; Schildt 2017), our grounded conceptualization of algorithmic management exhibits two dimensions—algorithmic matching and algorithmic control— as two counterparts for organizing distributed platform work carried out by numerous actors in a coordinated way (see Gawer 2014; Gulati et al. 2012). These two manifestations of algorithmic management reflect different perspectives: algorithmic matching reflects a view of platforms as markets (Eisenmann et al. 2006; Evans et al. 2006; Gawer 2014; Rochet and Tirole 2003), while algorithmic control reflects a view of platforms as organizations (Kellogg et al. 2020; Zuboff 2019).

Our findings suggest that OLPs like Uber must balance algorithmic matching and control in order to engage free agents while simultaneously ensuring that the platform work is aligned with organizational goals. The model also shows that this balancing act results in tensions across three dimensions, each reflecting opposing poles of platform work. First, the dimension of work execution highlights tensions between the autonomy of a flexible platform job offered through algorithmic matching, and supervision over when and where jobs are accepted or declined, driven by algorithmic control. This echoes previous findings on the autonomy paradox (Mazmanian et al. 2013), the key difference being that the use of algorithmic control is enabled by the collection and use of vast amounts of microlevel process data on platform workers’ behaviors, giving these workers a perception of real-time surveillance by an algorithm viewed as their “boss” (see Curchod et al. 2020; Kellogg et al. 2020; Zuboff 2019).

Second, the dimension of work compensation captures the observation that although platform workers experience uncertainty about how much money they can expect to make, they also trust the platform’s algorithmic matching capabilities to offer them repeated job opportunities. Ultimately, the algorithm controls to whom jobs are offered and when. Although the allocation of jobs severely affects revenue, the algorithmic decision-making is a “black box” to platform workers (see Burrell 2016; Dourish 2016; Faraj et al. 2018). Indeed, Uber drivers claim that the underlying logic of the algorithm is not transparent, making some Uber app instructions incomprehensible and unpredictable. This finding mirrors the new reality of complex machine-learning algorithms. These may be multicomponent systems comprising tens of thousands of data features trained on billions of examples (Burrell 2016; Dourish 2016); platform workers may find them difficult to decode and understanding their logic may thus be challenging (Burrell 2016; Newell and Marabelli 2015).

Finally, the third dimension of worker belonging in our model highlights that platform workers matched with clients by the platform algorithms value their self-identity as independent workers yet simultaneously feel a desire to engage in informal communities such as UberPeople.net, social media networks, or WhatsApp in order to exchange information and experiences with other platform workers about how to optimize their algorithm-controlled behavior. In the absence of algorithmic management and when platforms are viewed only as markets, perceptions of independence, i.e., of being one’s own boss as a self-employed worker, are likely to dominate. For example, users of craigslist.com do not form communities to exchange best practices on how to sell and buy their products and services on the platform. Uber differs, one reason being that drivers are working for a complex, nontransparent algorithm (Burrell 2016; Dourish 2016; Faraj et al. 2018) that creates a need for platform workers to exchange information and experiences to learn about and improve their own interactions with this algorithm. These informal communities may emerge as a substitute for the faceto-face relationships more common in traditional work contexts, where workers can often easily mingle with colleagues and supervisors. Interestingly, these communities are not facilitated by Uber, but are created and maintained by the drivers themselves, beyond Uber’s control.

The third overarching finding depicted in the model relates to the consequences of tensions created by algorithmic management of platform work. The model highlights two types of platform workers’ responses to algorithmic management, which dynamically feed back into the balancing act between algorithmic matching and algorithmic control. As the model shows, market-like behavior generally triggers algorithmic control, as Uber either sanctions or gently nudges drivers to ensure behaviors congruent with the platform’s meta-organizational goals and objectives. On the other hand, Uber deals with organization-like behavior by fostering public communication of the platform as a marketplace to avoid responsibilities associated with traditional organizations (e.g., employment status and benefits).

In summary, the left-hand side of our model mirrors characteristics previously associated with markets (e.g., Burtch et al. 2018; Chen and Horton 2016; Deng and Joshi 2016), while the right-hand side reflects characteristics typically associated with hierarchical organizations (e.g., Cappelli and Keller 2013; Gawer 2014; Kuhn and Maleki 2017). This dual perspective is relevant to all three core constructs: algorithmic management, platform work environment tensions, and platform workers’ responses. Yet, as joint constructs, the novel work category of OLPs integrates these perspectives.

## Theoretical Implications

## Online Labor Platforms

The IS literature on OLPs (see e.g., Burtch et al. 2018; Chen and Horton 2016; Deng et al. 2016; Hong et al. 2016; Huang et al. 2020) largely adopts an economics perspective, viewing platforms as markets and emphasizing the use of algorithms to enable efficient matching of supply and demand. It tends to overlook the fact that platforms also offer a model for organizing platform work without employment contracts (see Gulati et al. 2012; Gawer 2014), relying largely on the use of algorithms to control work (Kuhn and Maleki 2017; Bucher et al. 2019; Wood et al. 2019). Our model goes beyond previous work by offering a conceptual basis for understanding both sides of OLPs, with a focus on algorithmic management and platform work. It explains the algorithmic management of platform work by specifying its antecedents (algorithmic management), characteristics (work execution, work compensation, and work belonging tensions), and consequences (platform workers’ responses), and how they all relate to each other.

In particular, we conceptualize two dimensions of algorithmic management—algorithmic matching and algorithmic control— that serve as a starting point for using our model to analyze platform work. With this distinction, it is possible to place the implementation of OLPs on a two-dimensional plane reflecting varying levels of matching and control. Some OLPs, such as Amazon Mechanical Turk and TaskRabbit, score relatively high on algorithmic matching but low on algorithmic control because they do not closely monitor the work conducted on the platform. Other OLPs, such as Fiverr, which focuses on creative work, score lower on algorithmic matching (work requesters are encouraged to find the most suited creative worker from a range of options themselves rather than being automatically matched) but high on algorithmic control because the platform implements multiple control mechanisms, including punishing workers, to ensure that work is conducted on time and is high quality (Bucher et al. 2019).

As our model is used as a tool for analyzing OLPs, it is important to determine how the OLPs under investigation score on the two dimensions of algorithmic management, and how their approach shapes platform work environments and platform workers’ responses. High scores on both dimensions will invite fully fledged use of the model. Even cases where OLPs primarily encapsulate aspects of one side of the model offer a basis for detailed analysis. For instance, previous studies of crowdsourcing and the gig economy assume that platforms fade into the background by simply facilitating a marketplace in which workers are not actively managed by the platform but by other market participants (i.e., job requesters) on the basis of work outcomes (Barowy et al. 2016; Curchod et al. 2020; Deng et al. 2016, Kuhn and Maleki 2017; Petriglieri et al. 2019). Such market-like platform work tends to be characterized by high levels of worker autonomy, uncertainty about work compensation, and a self-identity exhibiting a strong feeling of independence (as illustrated on the left-hand side of our model). Yet, with increasing sophistication of machine-learning algorithms and availability of data (e.g., Agrawal et al. 2018; Gregory et al. 2020), OLPs are becoming increasingly interested in process control and real-time behavioral nudging. The implementation of such practices is likely to shift workers’ experience of platform work, eventually exhibiting features typically associated with work in organizations, like those illustrated on the right-hand side of our model. This resonates with Kuhn and Maleki’s (2017, p. 189) observation that: “The Upwork platform is more similar to a market-place than many other labor platforms, but it now enables electronic monitoring of workers, which is likely to reduce their perceived autonomy.”

By conceptualizing subdimensions that cut across algorithmic matching and algorithmic control, the model also offers a vocabulary that speaks to previous research on the use of algorithms in OLPs and in work environments more generally (e.g., Curchod et al. 2020; Faraj et al. 2018; Galliers et al. 2017; Kellogg et al. 2020; Newell and Marabelli 2015; Rosenblat and Stark 2016; Schildt 2017). To this end, we distinguish between the role of the algorithm (either facilitating a marketplace or taking the role of a dictating “boss”), the type of data used (either input and output data, or process data), and the coordination and control mechanism (either dynamic pricing or behavioral nudging) in algorithmic management. This facilitates analysis of a phenomenon that varies with different implementations of algorithmic matching and algorithmic control manifested on different OLPs.

Furthermore, the model theorizes how platform workers experience tensions relating to execution, compensation, and belonging. For example, it captures workers’ simultaneous experience of autonomy alongside tight supervision in their work execution. In doing so, our model paves the way for characterizing a new category of work—platform work that synthesizes attributes previously associated with either markets or organizations. This analysis transcends previous categorizations of freelancing, contract work, or selfemployment, as typically associated with the context of market-like platforms, as well as employment, as typically associated with the context of organizations (see Barley and Kunda 2006; Deng and Joshi 2016; Muhl 2002; Kalleberg 2009; Oldham and Hackman 2010; Petriglieri et al. 2019; Shalley et al. 2000). We propose a need to establish the nature of this synthesis and how it diverges from traditional work categories documented over recent decades (see Barley and Kunda 2006; Cappelli and Keller 2013; Kuhn and Maleki 2017). Establishing that OLPs exhibit the distinct work category of platform work, which sits at the cross-sections of traditional work categories, begins this endeavor.

## Meta-Organizations

In addition to our contribution to the substantive area of OLPs, some insights from this study relate to the use of our metatheoretical lens. As Kelle (2007) outlines, the objective of using meta-theories in grounded theory is to increase the theoretical sensitivity (Glaser 1978) of the research. In this regard, meta-organizations (Gawer 2014; Gulati et al. 2012) offered a useful lens to sensitize us to what data were important in developing the model. In particular, it supported us in thinking of OLPs as a model for organizing work, where “agents are themselves legally autonomous and not linked through employment relationships” (Gulati et al. 2012, p. 573). This steered our attention to the control aspects of our empirical domain, and why the Uber drivers we interviewed sometimes acted as if they were employed by the OLP. In turn, this helped us discover the phenomenon of algorithmic control and also articulate its unique character as a property of platform work and a key component of algorithmic management.

Following the direction of the meta-theory in its emphasis on control without formal authority, our model explains how platform work is organized through the collection and use of process data. This allows the OLP to predict individual workers’ future performance, meaning that it can shape platform workers’ behavior in real time rather than penalizing low work performance in retrospect, as is common on OLPs characterized by output control (see Kuhn and Maleki 2017). Thus, based on extensive access to data, algorithmic control involves ongoing data-based optimization (Schildt 2017), providing even more opportunities to individualize management decisions. Workers’ behavior can be modified by behavioral nudging with subtle cues and rewards (Zuboff 2019).

In addition, there is an important learning aspect of the OLP as a meta-organization (see Gregory et al. 2020). With a dramatic improvement in the price-performance ratio of information processing, storage, and networking technologies, OLPs deploy machine-learning algorithms that adapt dynamically to changing environments (Burrell 2016; Constantiou and Kallinikos 2015; Faraj et al. 2018; Gregory et al. 2020). The self-learning element is a source of so-called algorithmic agency in managing platform workers. While the OLP certainly maintains control points reminiscent of the leadership of traditional organizations, algorithms mediate managerial agency as they act on process data and materialize behavioral nudging. Yet the agency of sophisticated algorithms (see e.g., Burrell 2016; Dourish 2016; Faraj et al. 2018) can only be leveraged if fed with real-time data on workers’ behavior. We theorize how algorithmic management shapes platform work, and eventually induces different responses by platform workers, which then, in an endless loop, feed back into algorithmic management. In this regard, our model captures the interplay of algorithmic agency and human agency (i.e., workers). Although beyond the scope of this paper, the idea of algorithmic agency (e.g., Andersen et al. 2016; Faraj et al. 2018) revives classic debates on the role of human agency and performativity in information systems (e.g., Orlikowski 1992; Orlikowski and Scott 2008).

All in all, a meta-theoretical lens should provide direction in terms of theoretical sensitivity while at the same time scoring low on empirical content in order to avoid enforcing the lens on the data (Kelle 2007). The meta-organizational lens (Gawer 2014; Gulati et al. 2012) provided imperative direction to our theory development. In return, our use of this lens in the context of platform work offers some insights into the idea of metaorganizations. For instance, Gulati et al. (2012) propose a taxonomy of meta-organizations, including models of extended enterprises, closed communities, open communities, and managed ecosystems. OLPs can be added to this taxonomy; but, more importantly, our research epitomizes how control can be exercised without formal authority and shows that algorithmic management is an essential element for doing so.

## Practical Implications and Limitations

Our research has significant practical implications. First, several jurisdictions around the world are addressing the tricky question of how Uber workers should be classified. For instance, in 2017, Uber drivers in the U.K. were labeled as workers rather than contractors, whereas in 2018, a district judge in Philadelphia ruled that Uber drivers are contractors rather than employees under federal U.S. law. Our conceptualization of platform work as a distinct work category situated between the market and the organization may provide direction to policy makers’ ongoing discussion of whether entrenched structures are infeasible for dealing with the new ways of working on OLPs.

Second, managers of OLPs can learn from our conceptualization of algorithmic management and its influence on platform work. Given that OLPs are increasingly required to ensure certain service quality and reliability standards, the next few years will involve an increasing need to carefully balance algorithmic matching and algorithmic control. The three tensions relating to execution, compensation, and belonging offer valuable clarity in managing this balance. It is in OLPs’ best interests to attempt to dissolve some of these tensions in their relationships with workers. Our study of Uber drivers hints at possible directions, including improving transparency in data collection practices, explaining algorithmic calculation of wages and fees, and mitigating drivers’ feelings of isolation by providing a humanbased worker support line.

Our paper has some limitations. First, the data sources used may be prone to the biases typical of self-reported data. For instance, the interview data may suffer from social desirability bias. Both interviews and driver testimonials may suffer from drivers’ selective memory, incorrect attribution of events to Uber or to the algorithmic management, and exaggeration or embellishment of events. To address these concerns, we compared multiple data sources, verifying that data from one source were congruent with other sources. We also interpreted the drivers’ testimonials in view of their sociocultural context.

Furthermore, the community of Uber drivers is heterogeneous. Some drivers perceived the identified tensions to be very significant, others less so, resulting in a variety of response behaviors. For example, given the anonymity on UberPeople.net, we have no data on the number of drivers currently active in online discussions nor on the prevalence of given response behaviors in the general driver population. Our research focused on qualitative assessment of the effects of Uber’s algorithmic management on the work environment, but future research might focus on quantifying these effects.

Lastly, we collected data on Uber drivers from two cities, New York City and London, known as metropolitan hubs. While this allowed us to confirm that our results were not specific to a single market, ride-hailing regulations and policies and the prevalence of competitors in local markets vary. Thus, we encourage future research to focus on other websites, industries, and geographies.

## Conclusion and Future Research

Our research highlights salient features of algorithmic management of platform work on OLPs. It adds to a growing body of work in the form of a new model that captures two key dimensions of managing platform work: algorithmic matching and algorithmic control. This study represents an emerging area of inquiry that offers several directions for future research. For instance, future research might unveil the interplay and balancing act of algorithmic matching and algorithmic control to understand how OLPs might design their platforms along those two dimensions in order to create effective meta-organizations. In addition, research might address unresolved tensions of platform work. As work redesign has been “prominent as a strategy for attempting to improve simultaneously the productivity and the quality of the work experience of employees in contemporary organizations” (Hackman and Oldham 1976, p. 250), we call for more research on platform work design, focusing on how to better balance the interests of platforms and their workers. Another interesting area for future research might be ethical leadership (Ananny 2016; Irani and Silberman 2016) and its potential in the area of platform work. For example, such research could focus on the mitigation of negative feelings triggered by the algorithm’s lack of transparency or the relatively low level of social and face-to-face interactions with platform representatives experienced by platform workers. Future research might also investigate individual perspectives on supervision and how these relate to concerns about security and privacy, repeatability and workers’ motivation, and behavioral nudging and workers’ conscious decision-making.

Research on platform work on OLPs is clearly in its infancy. This research takes a small step in advancing the understanding of this important area. We humbly encourage researchers to take its message on board, broaden its scope, and push its boundary conditions.

## Acknowledgments

Many thanks are due to three anonymous reviewers and the associate editor. The senior editor Brian Butler offered really valuable and thoughtful guidance. We are also grateful for the constructive feedback received when presenting the paper at workshops and conferences, including the 2017 ICIS conference and 2019 Academy of Management conference. Furthermore, the research has benefitted from feedback offered by the participants at research seminars at HEC Montreal, Ivey Business School, London School of Economics, UIC Barcelona, University of Galway, University of Georgia, University of Miami, University of Tilburg, and Warwick Business School. Finally, we would like to thank the German-Israeli Foundation for Scientific Research and Development for their financial support, and Verizon for funding the McIntire Emerging Scholars professorship at the McIntire School of Commerce.

## References

Agrawal, A., Gans, J., and Goldfarb, A. 2018. Prediction Machines: The Simple Economics of Artificial Intelligence, Harvard Business Review Press.

Ananny, M. 2016. “Toward an Ethics of Algorithms: Convening, Observation, Probability, and Timeliness,” Science, Technology & Human Values (41:1), pp. 93-117

Andersen, J. V., Lindberg, A., Lindgren, R., and Selander, L. 2016. “Algorithmic Agency in Information Systems: Research Opportunities for Data Analytics of Digital Traces,” in Proceedings of the 49th Annual Hawaii International Conference on System Sciences, pp. 4597-4605.

Armstrong, M. 2006. “Competition in Two‐Sided Markets,” The RAND Journal of Economics (37:3), pp. 668-691.

Autor, D. H. 2015. “Why Are There Still So Many Jobs? The History and Future of Workplace Automation,” Journal of Economic Perspectives (29:3), pp. 3-30.

Bacharach, S. B. 1989. “Organizational Theories: Some Criteria for Evaluation,” The Academy of Management Review (14:4), pp. 496- 515.

Barley, S. R., and Kunda, G. 2006. Gurus, Hired Guns, and Warm Bodies: Itinerant Experts in a Knowledge Economy, Princeton University Press.

Barowy, D. W., Curtsinger, C., and McGregor, A. 2016. “Automan: A Platform for Integrating Human-Based and Digital Computation,” in OOPSLA ’12: Proceedings of the ACM International Conference on Object Oriented Programming Systems Languages and Applications, pp. 639-654.

Brynjolfsson, E., and McAfee, A. 2014. The Second Machine Age: Work, Progress, and Prosperity in a Time of Brilliant Technologies, Norton.

Bucher, E., Schou, P. K., and Frischherz, F. 2019. “The Emergence of Self-Disciplinary Practices in the Face of Algorithmic Governance,” Academy of Management Proceedings (2019:1), Article 13825.

Burrell, J. 2016. “How the Machine ‘Thinks’: Understanding Opacity in Machine Learning Algorithms,” Big Data & Society (3:1), pp. 1-12.

Burtch, G., Carnahan, S., and Greenwood, B. N. 2018. “Can You Gig It? An Empirical Examination of the Gig Economy and Entrepreneurial Activity,” Management Science (64:12), pp. 5497- 5520.

Cappelli, P., and Keller, J. R. 2013. “Classifying Work in the New Economy,” Academy of Management Review (38:4), pp. 575-596.

Charmaz, K. 2014. Constructing Grounded Theory, 2nd ed., SAGE.

Chen, D. L., and Horton, J. 2016. “Research Note: Are Online Labor Markets Spot Markets for Tasks? A Field Experiment on the Behavioral Response to Wage Cuts,” Information Systems Research (27:2), pp. 403-423

Chen, M. K. 2016. “Dynamic Pricing in a Labor Market: Surge Pricing and Flexible Work on the Uber Platform,” in Proceedings of the 2016 ACM Conference on Economics and Computation, p. 455.

Constantinides, P., Henfridsson, O., and Parker, G. G. 2018. “Introduction: Platforms and Infrastructures in the Digital Age,” Information Systems Research (29:2), pp. 381-400

Constantiou, I., and Kallinikos, J. 2015. “New Games, New Rules: Big Data and the Changing Context of Strategy,” Journal of Information Technology (30:1), pp. 44-57

Constantiou, I., Marton, A., and Tuunainen, V. K. 2017. “Four Models of Sharing Economy Platforms,” MIS Quarterly Executive (16:4), pp. 231-251.

Curchod, C., Patriotta, G., Cohen, L., and Neysen, N. 2020. “Working for an Algorithm: Power Asymmetries and Agency in Online Work Settings,” Administrative Science Quarterly (65: 3), pp. 644- 676 .

De Reuver, M., Sørensen, C., and Basole, R. C. 2018. “The Digital Platform: A Research Agenda,” Journal of Information Technology (33:2), pp. 124-135

Deng, X., and Joshi, K. D. 2016. “Why Individuals Participate in Micro-Task Crowdsourcing Environment: Revealing Crowdworkers’ Perceptions,” Journal of the Association for Information Systems (17:10), pp. 648-673

Deng, X., Joshi, K. D., and Galliers, R. D. 2016. “The Duality of Empowerment and Marginalization in Microtask Crowdsourcing: Giving Voice to the Less Powerful Through Value Sensitive Design,” MIS Quarterly (40:2), pp. 279-302.

Dourish, P. 2016. “Algorithms and their Others: Algorithmic Culture in Context,” Big Data & Society (3:2), (https://doi.org/10.1177/2053951716665128).

Eisenhardt, K. M. 2000. “Paradox, Spirals, Ambivalence: The New Language of Change and Pluralism,” The Academy of Management Review (25:4), pp. 703-705.

Eisenmann, T. R., Parker, G., and Van Alstyne, M. W. 2006. “Strategies for Two Sided Markets,” Harvard Business Review (84:10), pp. 92-101.

European Commission. 2018. “New Report Shows that Digital Employment Platforms Are Gaining a Foothold in Europe’s Labour Markets,” European Commission ( https://ec.europa. eu/social/main.jsp?langId=en&catId=89&newsId=9146).

Evans, D. S. 2003. “Some Empirical Aspects of Multi-Sided Platform Industries,” Review of Network Economics (2:3), pp. 191-209.

Evans, D. S., Hagiu, A., and Schmalensee, R. 2006. “Software Platforms,” in Industrial Organization and the Digital Economy, G. Illing and M. Peitz (eds.), MIT Press, pp. 31-71.

Faraj, S., Pachidi, S., and Sayegh, K. 2018. “Working and Organizing in the Age of the Learning Algorithm,” Information and Organization (28:1), pp. 62-70.

Galliers, R. D., Newell, S., Shanks, G., and Topi, H. 2017. “Datification and its Human, Organizational and Societal Effects: The Strategic Opportunities and Challenges of Algorithmic Decision-Making,” Journal of Strategic Information Systems (26:3), pp. 185-190.

Gawer, A. 2014. “Bridging Differing Perspectives on Technological Platforms: Toward an Integrative Framework,” Research Policy (43:7), pp. 1239-1249.

Gerring, J. 2007. Case Study Research Principles and Practices, Cambridge, UK: Cambridge University Press.

Gioia, D. A., Corley, K. G., and Hamilton, A. L. 2013. “Seeking Qualitative Rigor in Inductive Research: Notes on the Gioia Methodology,” Organizational Research Methods (16:1), pp. 15- 31.

Glaser, B. 1978. Theoretical Sensitivity, Sociology Press.

Gregory, R. W., Henfridsson, O., Kaganer, E., and Kyriakou, H. 2020. “The Role of Artificial Intelligence and Data Network Effect for Creating User Value,” Academy of Management Review.

Gulati, R., and Kletter, D. 2005. “Shrinking Core, Expanding Periphery: The Relational Architecture of High-Performing Organizations,” California Management Review (47:3), pp. 77- 104.

Gulati, R., Puranam, P., and Tushman, M. 2012. “Meta‐Organization Design: Rethinking Design in Interorganizational and Community Contexts,” Strategic Management Journal (33:6), pp. 571-586.

Hackman, J. R., and Oldham, G. R. 1976. “Motivation through the Design of Work: Test of a Theory,” Organizational Behavior and Human Performance (16:2), pp. 250-279.

Hagiu, A., and Wright, J. 2015. “Multi-Sided Platforms,” International Journal of Industrial Organization (43:C), pp. 162-174.

Hong, Y., Wang, C., and Pavlou, P. A. 2016. “Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets,” Information Systems Research (27:1), pp. 49-69.

Huang, N., Burtch, G., Hong, Y., and Pavlou, P.A. 2020. “Unemployment and Worker Participation in the Gig Economy: Evidence from an Online Labor Market,” Information Systems Research (31:2), pp. 431-448.

Huang, J. C., Henfridsson, O., Liu, M. J., and Newell, S. 2017. “Growing on Steroids: Rapidly Scaling the User Base of Digital Ventures through Digital Innovation,” MIS Quarterly (41:1), pp. 301-314.

Irani, L. C., and Silberman, M. 2013. “Turkopticon: Interrupting Worker Invisibility in Amazon Mechanical Turk,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pp. 611-620.

Irani, L., and Silberman, S. 2016. “Stories We Tell About Labor: Turkopticon and the Trouble with ‘Design’,” in CHI ’16: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, pp. 4573-4586.

Kalanick, T. 2016. “Uber’s Plan to Get More People into Fewer Cars,” TED (https://www.ted.com/talks/travis\_kalanick\_uber\_s\_plan\_ to\_get\_more\_people\_into\_fewer\_cars?language=en).

Kalleberg, A. L. 2009. “Precarious Work, Insecure Workers: Employment Relations in Transition,” American Sociological Review (74:1), pp. 1-22.

Kelle, U. 2007. “The Development of Categories: Different Approaches in Grounded Theory,” in The Sage Handbook of Grounded Theory, A. Bryant and K. Charmaz (eds.), SAGE, pp. 191-213.

Kellogg, K., Valentine, M., and Christin, A. 2020. “Algorithms at Work: The New Contested Terrain of Control,” Academy of Management Annals (14:1), pp. 366-410.

Kuhn, K. M., and Maleki, A. 2017. “Micro-Entrepreneurs, Dependent Contractors, and Instaserfs: Understanding Online Labor Platform Workforces,” The Academy of Management Perspectives (31:3), pp. 183-200.

Lee, A. S., and Baskerville, R. L. 2003. “Generalizing Generalizability in Information Systems Research,” Information Systems Research (14:3), pp. 221-316.

Lee, M. K., Kusbit, D., Metsky, E., and Dabbish, L. 2015. “Working with Machines: The Impact of Algorithmic, Data-Driven Management on Human Workers,” in Proceedings of the 33rd Annual ACM SIGCHI Conference, pp. 1603-1612.

Liu, M., Brynjolfsson, E., and Dowlatabadi, J. 2018. “Do Digital Platforms Reduce Moral Hazard? The Case of Uber and Taxis,” NBER Working Paper No. 25015, National Bureau of Economic Research (https://www.nber.org/system/files/ working\_papers/w25015/w25015.pdf).

Manyika, J., Lund, S., Bughin, J., Robinson, K., Mischke, J., and Mahajan, D. 2018. “Independent Work: Choice, Necessity, and the Gig Economy,” McKinsey Global Institute (https://www.mckinsey.com/featured-insights/employment-andgrowth/independent-work-choice-necessity-and-the-gigeconomy).

Mazmanian, M., Yates, J., and Orlikowski, W. J. 2013. “The Autonomy Paradox: The Implications of Mobile Email Devices for Knowledge Professionals,” Organization Science (24:5), 1337- 1357.

Muhl, C. 2002. “What is an Employee? The Answer Depends on Federal Law,” Monthly Labour Review (125:1), pp. 3-11.

Nambisan, S., Lyytinen, K., Majchrzak, A., and Song, M. 2017. “Digital Innovation Management: Reinventing Innovation Management Research in a Digital World,” MIS Quarterly (41:1), pp. 223-238.

Newell, S., and Marabelli, M. 2015. “Strategic Opportunities (and Challenges) of Algorithmic Decision-Making: A Call for Action on the Long-Term Societal Effects of ‘Datification,’” Journal of Strategic Information Systems (24:1), pp. 3-14.

Oldham, G. R., and Hackman, J. R. 2010. “Not What It Was and Not What It Will Be: The Future of Job Design Research,” Journal of Organizational Behavior (31:2-3), pp. 463-479.

Orlikowski, W. J. 1992. “The Duality of Technology: Rethinking the Concept of Technology in Organizations,” Organization Science (3:3), pp. 301-441.

Orlikowski, W. J., and Scott, S. 2008. “Sociomateriality: Challenging the Separation of Technology, Work and Organization,” The Academy of Management Annals (2:1), pp. 433-474.

Parker, J., Van Alystyne, M. W., and Choudary, S. P. 2016. Platform Revolution: How Networked Markets are Transforming the Economy and How to Make them Work for You, Norton.

Petriglieri, G., Ashford, S. J., and Wrzesniewski, A. 2019. “Agony and Ecstasy in the Gig Economy: Cultivating Holding Environments for Precarious and Personalized Work Identities,” Administrative Science Quarterly (64:1), pp. 124-170.

Rochet, J. C., and Tirole, J. 2003. “Platform Competition in Two-Sided Markets,” Journal of the European Economic Association (1:4), pp. 990-1029.

Rosenblat, A., and Stark, L. 2016. “Algorithmic Labor and Information Asymmetries: A Case Study of Uber’s Drivers,” International Journal of Communication (10), pp. 3758-3784.

Rietveld, J., and Schilling, M. A. 2021. “Platform Competition: A Systematic and Interdisciplinary Review of the Literature,” Journal of Management (47:6), pp. 1528-1563.

Scheiber, N. 2017. “How Uber Uses Psychological Tricks to Push Its Drivers’ Buttons,” The New York Times (https://www.

nytimes.com/interactive/2017/04/02/technology/uber-driverspsychological-tricks.html

Schildt, H. 2017. “Big Data and Organizational Design: The Brave New World of Algorithmic Management and Computer Augmented Transparency,” Innovation (19:1), pp. 23-30.

Shalley, C. E., Gilson, L. L., and Blum, T. C. 2000. “Matching Creativity Requirements and the Work Environment: Effects on Satisfaction and Intentions to Leave,” The Academy of Management Journal (43:2), pp. 215-223.

Siggelkow, N. 2007. “Persuasion with Case Studies,” The Academy of Management Journal (50:1), pp. 20-24.

Smith, A. 2016. “Labor Platforms: Technology-Enabled ‘Gig Work,’” Pew Research Center (https://www.pewresearch.org/ internet/2016/11/17/labor-platforms-technology-enabled-gigwork/).

Willcocks, L. P., and Lacity, M. 2016. Service Automation: Robots and the Future of Work, Steve Brookes Publishing.

Wood, A. J., Graham, M., Lehdonvirta, V., and Hjorth, I. 2019. “Good Gig, Bad Gig: Autonomy and Algorithmic Control in the Global Gig Economy,” Work, Employment and Society (33:1), pp. 56-75.

Zuboff, S. 2019. The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power, Profile Books.

## About the Authors

Mareike Möhlmann is an assistant professor at Bentley University. Previously, she worked as an assistant professor at Warwick Business School, a teaching fellow/visiting assistant professor at the London School of Economics, and a postdoc at New York University. Her research focuses on AI and management, digital platforms, trust/reputation, the sharing economy, and the future of work.

Lior Zalmanson is an assistant professor (senior lecturer) at Coller School of Management, Tel Aviv University. Formerly, he was a Fulbright visiting scholar at Stern School of Business, New York University. Lior’s research has been published in leading journals, including the Academy of Management Journal and MIS Quarterly. His current research interests include engagement, trust, and commitment in online environments, community-based business models, AI-human collaboration, and the future of work.

Ola Henfridsson is a Schein Family Endowed Chair and Professor of Business Technology at Miami Herbert Business School, University of Miami. Ola is also a WBS Distinguished Research Environment Professor at Warwick Business School in the UK and a KIN Fellow at VU Amsterdam. His research interests relate to digital innovation, platforms, and technology management. Ola’s research has been published in world-elite journals such as Academy of Management Review, Information Systems Research, MIS Quarterly, and Organization Science.

Robert Wayne Gregory is an associate professor at Miami Herbert Business School, University of Miami. He received his Ph.D. in management information systems from Goethe University Frankfurt. His research interests include digital innovation and strategy, platforms, and technology-driven change.

## Appendix

## Initial Version of the Questionnaire for Semistructured Interviews

The following questionnaire was originally developed to conduct semistructured interviews with drivers in New York City in 2016. It was later adapted and modified on the fly for further interviews in London in 2016 and 2017.

I am a researcher working at [name of university]. I would like to ask you a couple of questions. Please be aware that this conversation will be recorded. Everything you tell me will be anonymized and your identity will never be revealed.

Currently, several ride-hailing apps/companies compete on the market in New York City. Drivers have several choices: they might drive for Uber, for Lyft, for Juno, or for a similar app/company.

1. For which company do you currently drive? Do you drive for one, or for several companies at the same time and switch between companies? Was it always like this? Did you drive for fewer or more companies in the past? Why do you think you changed your behavior?

2. If you drive for several companies, could you describe the process of “switching” in more detail? How has this changed over time? For instance, how frequently do you switch, what does it look like in practice, do you open several apps at the same time, how do you avoid getting several requests at the same time?

3. Why did you decide to drive for the company/companies for which you drive, for instance because they pay better (including special promotions), they have better customer service, or because they listen to the drivers? How has this changed over time? Is it only costbenefit (more revenue), or are there also other factors that are important, such as how well they communicate with you?

4. Do you identify with, feel loyal to, or part of the company/companies you drive for? Or do you identify as being a self-employed worker? Why? For instance, you may feel supported by them, or you may not. Are you happy to be your own boss, as an independent contractor? Do you sometimes try to “play” the system?
