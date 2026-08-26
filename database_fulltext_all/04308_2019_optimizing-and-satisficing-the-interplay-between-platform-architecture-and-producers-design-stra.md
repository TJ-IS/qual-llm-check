---
otero_id: 4308
otero_key: "YH3Z4EDE"
title: "Optimizing and Satisficing: The Interplay Between Platform Architecture and Producers’ Design Strategies for Platform Performance1"
authors: "Sabine Brunswicker; Esteve Almirall; Ann Majchrzak"
year: "2019"
journal: "MIS Quarterly"
doi: "10.25300/misq/2019/13561"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# OPTIMIZING AND SATISFICING: THE INTERPLAY BETWEEN PLATFORM ARCHITECTURE AND PRODUCERS' DESIGN STRATEGIES FOR PLATFORM PERFORMANCE $^{1}$

Sabine Brunswicker
Research Center for Open Digital Innovation, Purdue University,
West Lafayette, IN 49707 U.S.A. {sbrunswi@purdue.edu}

Esteve Almirall
ESADE Business School, Universitat Ramon Llull, Av. Toree Blanca 59,
SantCugat-Barcelona, SPAIN {esteve.almirall@esade.edu}

Ann Majchrzak
Marshall School of Business, University of Southern California,
Los Angeles, CA 90089 U.S.A. {amajchrzak@usc.edu}

Two-sided platforms are gaining increasing attention in practice and as the subject of IS and management research. We explore an assumption of research and practice: that a platform's architecture needs to be decoupled so that producers can easily mix and match the platform's design elements (APIs, code libraries, process models, etc.) into apps that perform well competitively, and insulate the platform from skewed outcomes and low market performance. However, in practice, complete decoupling is not just difficult but almost impossible. Based on more than two million runs of an exploratory NK model in which producers use a platform's design space for the creation of apps, we generate several surprising insights. First, we show that tighter coupling may not necessarily be harmful depending on the producers' design strategies and the amount of constraints placed on design elements. Second, we observe that if moderate to tightly coupled platforms with optimizing producers focused exclusively on being competitive, platform performance is lower compared to platforms with satisficing producers who put a lower priority of being competitive because of other interests. This is surprising since optimizers are better suited to cope with the inherent uncertainty of coupling. Finally, moderately coupled platforms can outperform platforms with loose coupling when constraints nudge producers into distant design moves while also isolating them from downside uncertainty. These three findings offer implications for multiple streams of literature on platform architectures.

Keywords: Platforms, apps, platform architecture, modular systems, loose coupling, software design, design strategy, NK model, simulation

## Introduction

Google Health. Covisint's B2B Automotive Exchange. Sony's PlayStation Home. Garmin's NuviPhone. Johnson Controls' Panoptix for energy efficiency. These are all application platform failures; that is, consumers of the applications (apps for short) left the platform for lack of value, and producers (e.g., software developers/designers) left because usage such as downloads and active users plummeted. Contrast this list to high performing platforms where apps and consumers are in the millions: Baidu's App Store. Facebook Games. Apple's iOS. Firefox plugins. Salesforce Lightning. RedHat's JBoss EAP. YouTube. The failures remind us that a platform's market performance (measurable in terms of downloads, installs, or active users) is achieved neither simply nor obviously.

What makes it so difficult to predict a platform's performance is its multisided nature of “producers and users in efficient exchanges of value” (Van Alstyne et al. 2016, p. 2), as well as a platform owner's decisions about the platform's architecture, which enable or limit producers in creating apps that users want and value (Tiwana 2015). The architecture of the platform defines how the platform is structured for producers to access, modify, and combine design elements (also referred to as boundary resources) to build software-based apps (Eaton et al. 2015; Ghazawneh and Henfridsson 2012). Examples of design elements include data, code libraries, application components, user interface templates, event models, business processes, and security tokens. As such, the architecture defines a producer's design space from which apps are created in a combinatorial manner (Um et al. 2013; Yoo, Henfridsson, and Lyytinen 2010). The platform owner (Apple, Johnson Controls, Sony, Garmin, Google) makes decisions about the architecture. These decisions are based on which elements of the platform are provided, how the elements are structured, and which producers have access to which elements at what cost (Boudreau 2010; Gawer 2014; Gawer and Cusumano 2002; Ghazawneh and Henfridsson 2010; Parker and Van Alstyne 2018; Parker et al. 2016). Sometimes these decisions can have disastrous outcomes. For example, in a decision about access to the platform architecture in the 1980s,

[Steve Jobs] charged developers for toolkits—inhibiting the very software producers he should have wanted on Apple’s platform. The result was that Apple struggled to create a robust platform connecting Apple customers and software producers (Van Alstyne et al. 2016, p. 2).

In contrast is Marc Benioff's successful decision to create the Force.com platform supplementing Salesforce.com with an architecture consisting of a robust software development kit, an app-exchange website where apps are displayed and purchased, and a sizeable number of components and templates for creating new apps. Benioff's decision contributed to the company's success in moving from a niche CRM player to a global enterprise competitor (Weissman and Broboski 2009, p. 890). Which of these many decisions about platform architecture will increase platform performance? This has been the holy grail of substantial, albeit relatively recent, research on platforms.

Research on platform architecture can be described in terms of two streams. The first stream focuses on the technical/engineering aspects of a platform's architecture. These include the tightness of coupling among the design elements (Baldwin and Clark 2006a; Baldwin and Woodard 2008; Tiwana 2014a; Tiwana et al. 2010; Yoo, Lyytinen et al. 2010) and technical constraints (or architectural control) placed on particular elements (Woodard 2008). Tightness of coupling is the degree to which a change in the functioning of one element may affect the functioning of another element (Baldwin and Clark 2000; Schilling 2000; Tiwana 2015; Tiwana et al. 2010). The Apache Webserver and Salesforce's Lightning are platforms with rather loosely coupled design elements. An Apache server can host a diversity of frameworks and environments such as WordPress or Flask. In contrast, the code structure of the GNU spreadsheet email platform is tightly coupled (Baldwin and Clark 2006a) such that chart displays can only be implemented when macros are turned on. In addition to coupling, a platform owner can also place constraints on how a producer can use or modify a certain design element itself. There is substantial variability in the level of technical constraints exercised by platform owners. For example, Apple's iOS platform has established strict constraints on how design elements should be used. Google's Android platform, in contrast, gives a producer more freedom to modify elements (Eaton et al. 2015; Ghazawneh and Henfridsson 2012). Research in this first stream generally concludes that coupling and constraints affect platform performance: loose coupling and at least moderate constraints are generally considered as having positive implications as they reduce uncertainty in the producers' design process, and insulate the platform from skewed and harmful outcomes.

The second stream focuses on how producers who have access to the design elements in the platform's architecture should be economically incentivized (Boudreau 2010, 2011; Eisenmann et al. 2011; Katz and Shapiro 1994; Parker and Van Alstyne 2018; Rochet and Tirole 2003). This literature generally argues that if platforms foster competition among producers, there are positive implications for the platform's performance. For example, Boudreau (2010) found that if competitive incentives—created through access to the technology—are strong, producers increase their effort and heighten platform performance. As soon as incentives are weaker, efforts and platform performance drop.

We argue that both streams suffer from a fundamental assumption that we question, despite its apparent face validity. They both assume that platforms create, at their foundation, a “competitive” design space in which all producers strive to have a competitive app on the platform (i.e., by having the most downloads, active users, or installs). For example, the first stream argues that decoupling affects producers’ ability to upgrade their apps easily because they all have a competitive drive to improve the market performance of their apps (Tiwana 2015). Similarly, the second stream suggests that every producer would leave a crowded platform because, economically, it is not rational for them to compete as the probability of winning is so small (Boudreau 2011; Boudreau and Jeppesen 2014).

With both streams, then, the assumption is that the strength of competitive aspirations is so high among all producers that it drives their behavior. Yet, Gartner analysts found that “less than 0.01 percent of consumer mobile apps will be considered a financial success by their creators at the end of 2018” (Guglielmo 2014). As Gartner analyst Ken Dulaney reported, “Many mobile apps are not designed to generate revenue but rather are [developed by producers] to build brand recognition and product awareness or are just for fun” (Gartner 2014). If some producers are creating apps for fun, why would they care about how crowded the competitive design space is? While some scholars have mentioned the possibility that there may be variation in the way producers purposively use and combine design elements as they compete (Boudreau and Jeppesen 2014; Qiu et al. 2011; Woodard et al. 2013), research has yet to examine the complex relationship between this variation, platform architecture, and platform performance. Therefore, we ask the research question: What is the relationship between an owner’s decisions about the platform architecture and platform performance when producers’ design strategies are taken into account?

We propose a theoretical model that generatively explores, through agent-based simulations, the sociodynamic process of how platform architecture affects platform performance when producers build apps guided by their design strategies. We conceptualize the creation of apps on a platform as a combinatorial and iterative search process in which producers, in parallel, search the platform's design space, combining accessible design elements into apps. We mathematically represent this conceptualization in an extended version of the NK model (Kauffman 1993), originally developed in evolutionary biology to represent adaptation as a combinatorial optimization process in a fitness landscape. In the NK model, producers are autonomous, computational agents, who do not act in isolation but rather through feedback loops from the market about the performance of their apps. They implement their design strategies through iterative search moves in the NK design landscape. This allows us to account for the complex interrelationships between architectural platform decisions that owners make, producers' design strategies, and platform performance.

Based on over two million simulation runs, we generate several new theoretical insights into the nonlinear interplay between coupling, constraints, and design strategies. First, we show that tighter coupling may not necessarily be harmful depending on the producers' design strategies and the amount of constraints placed on design elements. Second, we observe that if moderate to tightly coupled platforms assemble optimizing producers focused exclusively on being competitive, platform performance is lower compared to platforms with satisficing producers. This is because the latter put a lower priority on being competitive, even though optimizers are better suited to cope with the inherent uncertainty of coupling. Surprisingly, platforms with satisficers are better suited to deal with coupling. Finally, tightly coupled platforms can outperform those with loose coupling when constraints nudge producers into distant design moves while also isolating them from downside uncertainty. These three findings suggest the importance for integrating producers' design strategies in theories, empirical studies, and practice concerned with platform architecture.

## Conceptual Development

To explain the theoretical foundations of our NK model, we first describe how we conceptualize the creation of apps as a search process within an NK landscape. We then introduce our theory in terms of two dimensions of a platform's architecture that affect the design space accessible to producers, as well as two dimensions of producers' design strategies affecting how they search the design space. Finally, we present our focus, which is to explore the sociodynamic process of how these four dimensions unfold when multiple producers are engaged in parallel search across the platform's NK landscape.

## Producers as Searchers in an NK Design Landscape of a Platform

This work is indebted to, and follows, a long strand of research that conceptualizes product development as a process of adaptive search for effective design (and development) decisions in a design space of possible design alternatives (Billinger et al. 2013; Ethiraj and Levinthal 2004; Frenken 2006). Such spaces become complex if decision parameters interact in determining the value of a particular alternative. This complexity is what drives the need for simulation. We use this conceptual logic of search and apply it to producers of a platform who search in parallel as they design the next versions of their apps within the design space made available to them.

We use the NK model (Kauffman 1993) to view the design space of a platform as an NK design landscape of design elements (e.g., technical elements like APIs, code libraries, event and process frameworks such as payment processes) which producers search, evaluate, and combine into apps. Table 1 summarizes the classic NK assumptions as we have applied them to the context of producers iteratively designing apps by searching that design landscape. We elaborate on each below.

## NK Assumption 1: Rugged Landscape

An NK landscape is used to represent combinatorial decision making (Billinger et al. 2013; Kauffman 1993; Levinthal 1997). The space contains all potential combinations of different states of N decision elements in an N-dimensional space (the axis). N defines the size of the landscape. Each combination is mapped onto a fitness value (in N+1 dimensions), where fitness describes the hypothetical performance value of a particular combination. Fitness values are established randomly at the beginning of each simulation. Variability in fitness values create valleys and peaks in the performance surface which define the ruggedness of the landscape's surface or, visually speaking, the number of peaks. K is a hypothetical value of complexity, expressing how changes in the dimensions mutually influence each other in direct and indirect ways; as K increases, the number of peaks increases nonlinearly, creating several valleys and peaks next to each other. This allows exploring nonlinear effects of K.

Applying the assumption of a rugged landscape to a platform, the decision elements are the design elements that the platform owner has made accessible for the producers to be modified and combined when building apps. Design elements include technical design elements (such as APIs, source code libraries, templates), utilities (SDKs), and operational systems such as payments. Salesforce's AppExchange refers to these design elements as components, interface templates or event models in its Lightning library (Choi et al. 2016). The platform Snappii for “no-coding app” producers, refers to them as features, forms and elements (Snappii 2018). We chose N = 16 elements in order to stylistically represent a large design space for producers to search, or using Boudreau's (2011, p. 1411) language, a “virtually infinite one.” There are $2^{16}$ or 65,536 locations represented in the landscape, where each location is a design alternative (i.e., a combination of design elements). Figure $1^{2}$ shows a stylized, simplified three-dimensional version of a six-dimensional landscape with a single peak (K = 0).

## NK Assumption 2: Location in Landscape

In NK, the location in the landscape represents a particular combination of the different states of the N decision elements in the landscape. States are typically modeled as a binary of 0 or 1 for each decision element (Frenken 2006).

Applying this assumption to app design on a platform, a released version of an app is a location on the landscape (Baldwin and Clark 2006b). It is a producer's choice of a particular design alternative, a certain combination of design elements in the design space. In Figure 1, there are three producers, each at a different location in the landscape because they combine design elements (in this case six) in different ways. For example, if they were producers for Salesforce's App Exchange, they could be using predefined Lightning components (self-contained and reusable components of an app) (e.g., Lightning:accordion, a standard app component that allows toggling the display of a section of content), Lightning interface templates (e.g., force:hasRecordID), or Lightning event models (e.g., force:refreshView). In a very stylistic way, the use of such design elements in a particular design alternative can be represented with a set of binary states. For example, producer $\mathrm{P}_1$ 's app release in iteration 1 is presented as a set of [011110], describing how he combines Lightning design elements.

Table 1. Assumptions of NK Model Translated to Search on a Platform's NK Design Landscape

<table><tr><td>NK Search Assumptions</td><td>Theoretical Representation in Model</td><td>Examples</td></tr><tr><td>1. Rugged Landscape: A landscape is a decision space that contains all potential combinations of different states of N decision parameters (Billinger et al. 2013; Kauffman and Levin 1987). K defines the ruggedness in the fitness surface of the landscape.</td><td>a) Decision parameters are represented by design elements, defined as technical component that producers can access, and combine. Elements have a binary state (0 or 1).b) The NK design landscape contains all potential combinations of all N accessible design elements; we choose N = 16 to describe a relatively large design space with  $2^{16}$  design alternatives; N is fixed. K = degree of coupling which varies for different simulations (Levinthal 1997).</td><td>Elements relate to technical, (APIs, templates, etc.) and operational or procedural aspects (e.g., payment) of a potential app (Eaton et al. 2015; Ghazawneh and Henfridsson 2010). Salesforce refers to these elements as components, interface templates, and event models in its Lightning library (Choi et al. 2016); Snappii refers to these elements as features, forms, and elements (Snappii 2018).</td></tr><tr><td>2. Location in the Landscape: A location describes an agent's placement in the landscape based on the combination of the N decision parameters the agent has selected. The distance between one location to the other is one Hamming (Hamming 1950; Kauffman 1993; Wright 1932).</td><td>a) Location is modelled as a design alternative, or an app's release version, with a certain combination of design elements from the design space (Alexander 1964; Frenken 2006).b) A design alternative is abstractly represented as a design set with binary elements, e.g., a set of [111011100011] indicates which elements are used.</td><td>An app is a set of design decisions that combine the different design elements in certain ways: A recruiting app built for Salesforce's AppExchange platform could combine the set of predefined Lightning components (e.g., Lightning:accordion) or Lightning Interface templates (e.g., force: hasRecordID), or Lightning event models (e.g., force: refreshView) (Choi et al. 2016).</td></tr><tr><td>3. Fitness: The fitness is the sum of performance across all N decision parameters for the location chosen by the agent (Frenken 2006; Kauffman 1993; Levinthal 1997).</td><td>a) Fitness is modeled as an objectively achievable market performance (i.e., downloads) at a particular location in the landscape defined prior to simulation.b) The fitness values of each design alternative (i.e., location) are a function of K other locations. They are randomly generated prior to each simulation.</td><td>Market performance for an app is typically measured in downloads, installs, or user ratings (Boudreau and Jeppesen 2014; Tiwana 2015). In spring 2018 a native banking Salesforce app nCino had been installed by more than 150 US banks (nCino 2018). In 2018, the exclusive Google Android app Firstjob was downloaded by ~ 2.3 million users (Firstjob 2018).</td></tr><tr><td>4. Adaptive Agents as Searchers of the landscape: Agents are searchers who make discrete search moves from one to another location (or design alternative) in the landscape, changing states of N parameters. Agents are adaptive by seeking higher fitness. Multiple agents search independently and the starting point is random.</td><td>a) Producers design their apps in iterations. Agents iteratively search the NK design landscape. They move from one location to the other by making discrete design moves in each iteration.b) Producers move in order to improve or sustain their market performance.c) Producers are randomly placed at the start into the landscape to reflect equal conditions.</td><td>During an iterative design process, the producer of iOS game Fruit Ninja updated his app 23 times within 3 years. Such updates included new functionalities and features in order to sustain the market performance of the app.</td></tr><tr><td>5. Bounded Rationality: Agents are rationally bounded, that is, they are locally intelligent such that they are unable to assess all locations in the landscape except for immediate neighboring locations, they do not know where distant locations are, and they do not know the fitness values of the entire landscape (Simon 1955).</td><td>Producers cannot assess all design options (Tiwana et al. 2010); they do not know which combination of design elements are needed to achieve a high market performance; producers cannot reverse engineer all other competitors' apps to know the precise design choices made by all others.</td><td>A producer of an app for IBM PaaS (or Bluemix) does not know the market performance of a particular not-yet-designed app. There are too many combinations of design elements.When working on an app, a producer always assesses opportunities for making a better app with a small design change. If they improve performance, he goes for it because they are easy to implement.</td></tr><tr><td>6. Local versus Distant Search Moves: Local search or hill-climbing and distant search or long-jumps are two distinct search moves. Hill-climbing is when agents move to an immediate neighboring location (by changing one decision parameter) for which they can assess the fitness value (local move). Long-jump is when agents move to a distant location (re-orientation) by changing several decision parameters for which fitness is unknown (Kauffman 1993; Levinthal 1997).</td><td>a) Moves are modelled as discrete actions in which a producer changes the state of one or several design elements Moves vary in terms of distance where local or hill-climbing distance is a single design element change and distant long-jumps change multiple elements (Boudreau and Jeppesen 2014; Woodard et al. 2013).b) Local hill-climbing stylistically represents minor app upgrades. They are predictable because their fitness is known (Billinger et al. 2013; Levinthal and March 1981; March 1991).c) Long-jump moves stylistically represent major app upgrades and require resources. Outcomes are uncertain because producers cannot test major releases sufficiently.</td><td>a) App design typically follows a major versus minor app upgrade logic (also reflected in the versioning number). These two moves (local versus distant) are distinct.b) Local search: The minor release 3.5 of Facebook’s iPhone app (local search) added only the option to share external links from within the app. Facebook was sure about the positive effect on the user before the launch. There was no need to go back.c) Distant search: Instagram’s Version 2.0 of its iPhone app added a range of new features such as live filters, tilt-shift in camera, which require more design element changes (Warren 2011). When Windows launched the Skype Business version, they performed a major upgrade. However, the release was not successful but Windows did not go back to the prior version.</td></tr></table>

![](/api/attachments/YH3Z4EDE/fulltext/images/7ce4a96da10f5f6bee04e58dc16f1f0ef6c2979246738eb7fe1844b9d05d5293.jpg)  
Figure 1. A Representation of an NK Landscape for App Design on a Platform (N = 6, K = 0)

## NK Assumption 3: Fitness in the Landscape

In NK, fitness is the performance mapped into a particular location in the landscape; it is simply the sum of all fitness contributions of each design element for that location (Billinger et al. 2013; Kauffman 1993; Levinthal 1997). The fitness of a location in the landscape can range from 0 to 1, and is randomly generated prior to a simulation (Frenken 2006; Levinthal 1997).

Applying this assumption to app design on a platform, the fitness values of a design alternative (an app) reflects its market performance (Tiwana 2015). Fitness is exogenous and defined prior to a simulation of producers' search across the landscape. An app's market performance is, stylistically, objectively measurable with usage data such as downloads, installations, or average user ratings. In Figure 1, the higher the location on the third dimensional axis, the greater the fitness, or market performance, of that location. Producer $\mathrm{P}_2$ has achieved the highest fitness.

## NK Assumption 4: Adaptive Agents as Searchers Making Iterative Search Moves

In NK, agents are the searchers that traverse the landscape, making a series of discrete search moves from one location to the next in order to improve their fitness (and reach a higher peak) (Frenken 2006; Kauffman 1993). Moves are discrete such that, during any single iteration, the agent only moves to one new location. In NK, multiple agents search independently from each other. Their locations in the landscape are randomly assigned at the beginning of the simulation (Levinthal 1997) to make sure that the initial condition is not affecting the outcome of the simulation.

Applying the notion of iterative search moves to app design on a platform allows the app design process to be iterative, consistent with frequent updates and release cycles typically seen in apps on such platforms as iOS, Android, and Firefox (Tiwana 2015). Each move is a discrete design move (Woodard et al. 2013), in which a producer purposively changes one or several design elements to offer new functionalities to customers and improve the performance of an app. In Figure 1, producer $P_{1}$ (release v 2.0) would move up the hill to position $P_{1}$ (release v 2.1) rather than downward, in order to improve performance.

## NK Assumption 5: Bounded Rationality

In NK, agents are assumed to be boundedly rational (Foss and Weber 2016; Levinthal 1997; Simon 1955); in simple words, this means they do what they think is best having only incomplete information about their potential choices. They then apply simple heuristics (in the sense of rules of thumb) when searching and using the limited information they have available (Gigerenzer and Goldstein 1996). Incomplete information typically assumed in NK is that agents are not aware of all other locations in the landscape, nor do they know fitness levels of each location in the landscape (Kauffman 1993; Levinthal 1997; Simon 1973). As rationally bounded, agents can only evaluate the fitness of locations in the immediate neighborhood at a distance of one Hamming (meaning just one change in a single design element away) (Billinger et al. 2013; Hamming 1950) using prior knowledge. This allows the agent to decide if and where to move to improve his fitness in the immediate neighborhood. Agents use a simple, efficient rule of thumb: they always assess the current (“local”) context—the immediate neighboring solutions—and apply a simple stopping rule that, if a move to a local neighboring solution improves performance, the agent will stop considering other alternatives and move there. Unless there is additional information available indicating that a more distant search is warranted, the agent will not seek out alternatives. Thus, an agent always uses local information first.

Applying this assumption to app design on a platform (Tiwana et al. 2010) implies that producers are neither aware of the exact location of all other producers on the platform, nor are they able to reverse engineer all competitors' apps. They cannot, therefore, know precisely how other apps were built to achieve a high market performance. They can only assess and test (through mental exercise or some trial-and-error software development) design solutions that are very similar to their current design. Colloquially speaking, they are locally intelligent. To be efficient, they always give local information priority and apply a simple rule of thumb: Assess potential simple extensions of your current apps first and if you can gain some benefits then build it.

## NK Assumption 6: Local Versus Distant Search Moves

In NK models, the simplest way to classify search moves is to distinguish two contrasting moves: hill-climbing versus long-jumps (Billinger et al. 2013; Kauffman 1993; Levinthal 1997). When agents hill-climb, they move to an immediate neighboring location at a distance of one Hamming by modifying only a single element. As boundedly rational agents, hill-climbing (or local search) always has priority if such moves are available. Since agents are locally intelligent, they can identify the best local options around them before they decide to move. The performance implications are easy to assess a priori, and there is no need to revisit the choice and go back. In contrast, when agents jump, they move to a distant location by modifying not just one but several elements simultaneously (Kauffman 1993; Levinthal 1997). Long-jumps imply complete reorientation and dismissal of all prior search moves, and thus, in its simplest and extreme form, the selection of design elements to be modified happens randomly. $^{3}$ Long-jumps imply multiple changes such that agents lose the ability to assess the performance of distant locations (Billinger et al. 2013; Cyert and March 1963; Levinthal 1997), making long-jumps highly uncertain. Performance outcomes are uncertain and imply greater variability. Long-jumps use up significant resources which deplete over time (March and Shapira 1992; Rivkin 2000). Further, they are very difficult to reverse. Being boundedly rational makes it very difficult to precisely trace back the changes, and the costs (time, cognitive effort, etc.) are high (Billinger et al. 2013; Rivkin 2000).

![](/api/attachments/YH3Z4EDE/fulltext/images/ff349e4e46f18e4e323ae2c91677adbfc381507b5f28f4cc4b6eac70f1e6541c.jpg)  
Figure 2. Framework Describing How Collective-Level Platform Performance Emerges from Individual-Level Iterative Search Across the NK Design Landscape, Affected by Four Theoretical Factors

Applying these two search moves to app design, in a single iteration, producers may locally hill-climb or long-jump to a distant location as they move through the iterative design process. This is well in line with the classical distinction between major and minor updates in app development (Warren 2011). Hill-climbing would involve modifying only one design element. Figure 1 shows a hill-climbing move. P $_{1}$ 's release v 2.1, which could be Facebook's iPhone app, is a hill-climb (a minor update) from P $_{1}$ 's major release v 2.0. The only prominent new feature that Facebook introduced in this minor update was the option to share external links from within the app (Warren 2011). Facebook could test the new feature before it launched it to the market, and was certain about the positive impact on the user. There was no need to reverse that feature later. For long-jumps, a producer changes more than one design element at a time. Such long-jumps will move the producer to a more distant location in the landscape. Let us assume that Producer P $_{3}$ in Figure 1 would jump and reorient by changing several design elements; such a jump (as figuratively shown) might inadvertently end up with a lower performance. For example, the launch of Skype Business was a long-jump, which was not as successful as Windows had hoped. However, given the resources invested (time, technologies, money, etc.) and the technological debt accrued (Woodard et al. 2013), they did not go back to the prior version.

In sum, we conceptualize producers as searchers traversing an NK design landscape. Each producer searches independently (in the sense of parallel searchers). The producer's search process implies iterative design moves that fall into two categories: local design moves (hill-climbing moves), which lead to incrementally increased performance, and distant design moves (long-jumps), for which performance outcomes are unpredictable.

## Theory: Effects of Architecture and Design Strategy on Individual-Level Design Moves

Having described our NK landscape model for platforms, we now introduce our theoretical development by including four factors that have been suggested as independently affecting producers' iterative design moves at the individual-level: two architectural factors (coupling and constraints) and two factors of producer design strategy (strength of competitive aspiration and market responsiveness). In Figure 2, we provide a simplistic overview of these four factors, which affect each individual-level design move of a particular producer.

As visually articulated, platform performance is a collective-level outcome emerging from individual-level search processes of parallel independent producers across a platform's design space. Varying the four factors conjointly allows exploring how the sociodynamics of this process translates individual-level design moves into certain platform performance levels. The four factors are defined in Table 2 along with brief descriptions of their effects on an individual producer's design move. These effects form the theoretical assumptions in our NK model and justify our specification of how producers as computational agents make iterative design moves across a design landscape using a nondeterministic heuristic to search a combinatorial search space. It is the variation of those four factors jointly that we will explore to understand their implications for the platform's performance as a whole.

## Theory Factor 1: Looseness/Tightness of Coupling Among Design Elements

Looseness/Tightness of Coupling Defined: We build upon Tiwana (2015) and Yoo, Henfridsson, and Lyytinen (2010) to extend the concept of coupling from design theories on modular (Baldwin and Clark 2000; Schilling 2000) and nearly decomposable systems (Simon 1962) to the context of digital platforms, with a focus on the design elements accessible to the producers. $^{4}$ Looseness/tightness of coupling describes the degree to which a change in the functioning of one design element affects the functioning of other design elements used in the app. An extreme and unrealistic case is a completely decoupled design space, in which changes do not ripple (Baldwin and Clark 2006a). In practice, design spaces vary on a continuum from loose to tight coupling.

Effects of Coupling on Producer Design Moves: Literature on platform architecture (Baldwin and Woodard 2009; Tiwana et al. 2010; Ulrich 1995) points us to two effects of coupling on an individual producer's design moves. The first effect is that platforms with loosely coupled design elements allow producers to more easily assess, a priori, the likely performance of the app they create, increasing the potential to make quick predictable wins (Baldwin and Clark 2006b; Fleming 2001; Frenken 2006). A producer using loosely coupled design elements can make these revisions without worrying about other elements (Tiwana 2015). In the long run, such predictable iterative changes—s Tiwana (2015) empirically shows in his study among Firefox plug-in producers—increase the market value of the app (measured in average user rating and installs). In Simon's (1962) language, loose coupling increases the odds of survival since the producer adapts the app in an incremental but predictable way; across iterations this adds up to significant performance improvements. Minimum effort is expended to seize the advantage of a performance improvement. For example, Salesforce App Exchange producers can easily add a dashboard functionality (using code components and interface templates) to any business process without the need to modify the underlying data structure or worrying about data access rights (Choi et al. 2016). A minor upgrade of the app can be implemented easily.

The second effect is that platforms with tightly coupled design elements have (technical) functional interdependencies that are difficult for producers to predict (Baldwin and Clark 2006a; Baldwin and Woodard 2009). Changes in one element alone, as in minor updates and hill-climbing, are rendered ineffective. A single change in one element may make it technically incompatible with another, causing broken links, creating inconsistencies with other elements used (e.g., user interface components), or making data accessed via APIs problematic. To increase the possibility of higher performance with tight coupling, the producer will need to use considerable resources to rule out obvious incompatibilities and, in the end, accept some degree of uncertainty. Because of this uncertainty with tightly coupled design elements, there may be high variation in performance of the app. For example, R has a tightly coupled design space such that the elements in two apps, such as like GoogleVis and Chain Ladder, may have up to 42 hidden connections and dependencies (Gesmann 2014). An R producer attempting to change a single element of his app in order to improve the app's performance will not be able to do so, given the large number of functional dependencies.

To cope with the tight coupling, a producer often needs to completely reorient his app. The R programmer will need to rethink how he uses the 42 connections among the elements in the two apps so that they fit “synergistically” (Fleming and Sorenson 2001; Sanchez and Mahoney 1996; Tiwana 2015; Ulrich 1995). This reorientation requires a major revision of the app in which the producer changes multiple design elements at the same time. Because of the interdependencies, the synergy being attempted is likely to have uncertain outcomes since the precise manner in which the changes ripple through all the design elements cannot be known in advance. However, if the synergy is successfully created, the new app may offer unique qualities that may garner new attention from the marketplace. In essence, coupling increases the performance potential but requires a producer to embrace uncertainty in order to seize this potential. It renders major updates of an app—in the sense of a distant design move—more effective Billinger et al. 2013). However, given the uncertainty associated with major upgrades and the cognitive resources needed to cope with coupling, producers might not even try to engage such efforts and thus stop updating their apps, since minor updates will most likely also fail (e.g., many R packages are never updated).

Representation in the NK Model: In our NK design landscape for app design, the tightness of coupling is represented as K. The larger the K, the more tightly coupled the design space. If K is 0 (completely decoupled), there is only a single peak in the fitness landscape. A change of one element leads to a linear decrease or increase in the performance surface (the third dimension in Figure 1) because the change is only affected by the element itself (and not by other elements). In contrast, when all elements are tightly coupled to each other (e.g., K = 15), a change in every element will change another element, creating a more rugged landscape because of the combinatorial effect on fitness. Therefore, as tightness of coupling increases, the landscape becomes more rugged with

<table><tr><td colspan="3">Table 2. Theoretical Assumptions About Independent Effects of Architecture and Design Strategies on Individual-Level Design Moves</td></tr><tr><td>Factor</td><td>Theoretical Assumptions</td><td>Empirical Examples</td></tr><tr><td colspan="3">Independent Effects of Platform Architecture on Individual-Level Design Moves</td></tr><tr><td>1) Tightness of Coupling among Design Elements</td><td>1a) Looser coupling creates the potential to benefit from local design moves leading to immediate and predictable performance improvements (Baldwin and Clark 2006a; Tiwana 2015; Tiwana et al. 2010).1b) Tighter coupling reduces the potential to benefit from local design moves; while it increases the potentially achievable performance, it also requires producers to embrace uncertainty (Baldwin and Clark 2006b; Tiwana 2015; Tiwana et al. 2010).</td><td>1a) Salesforce AppExchange developers can take advantage of decoupled Lightning elements, and easily add a dashboard component and interface to any business process without the need to consider changes to data or access rights (Choi et al. 2016).1b) When MySpace opened the platform using the .NET technology, the high coupling made it very hard to add features to the platform, leading to low quality apps (Gilette 2011; Woodard et al. 2013). Homejoy created too many dependencies between different service components leading to low quality service offerings (Taeuscher and Kietzmann 2017).</td></tr><tr><td>2) Degree of Constraints placed on Design Elements</td><td>2a) More constraints may reduce the potential to benefit from local design moves (Eaton et al. 2015; Wareham et al. 2014; Woodard 2008).2b) More constraints may (indirectly) induce distant moves (Eaton et al. 2015).</td><td>2a) Apple&#x27;s ban of Flash plug-in for iPhone apps made some app producers discontinue their app on iOS (Eaton et al. 2015).2b) Apple&#x27;s ban of Flash plug-in for iPhone apps led to reorientation of some producers and the creation of apps like Skyfire working around the ban in order to afford online media streaming (Eaton et al. 2015); Twitter&#x27;s 140 word limit per tweet led to new communication forms (Bonchek and Choudary 2013).</td></tr><tr><td colspan="3">Independent Effects of Producer Design Strategy on Individual-Level Design Moves</td></tr><tr><td>3) Producer&#x27;s Competitive Aspirational Strength</td><td>3a) Optimizers (who have high aspiration strengths) are likely to make a distant design move if their app performance fails to be among the top performers (Boudreau and Jeppesen 2014; Boyle and Shapira 2011; Qiu et al. 2011; Schwartz et al. 2002; Shinkle 2012; Shinkle and Kriauciunas 2012).3b) Satisficers (who have moderate aspiration strengths) will make distant moves if their app fails to meet the average performance on the platform (Boudreau and Jeppesen 2014; Simon 1973; Tiwana et al. 2010).</td><td>3a) Some app developers are optimizers who make radical changes to their apps in very frequent way when failing to win in the marketplace (Bushey 2014; Gartner 2014); Developer of the game “Doodle Jump” performed major updates every time his game was facing pressure from competing games like “AngryBirds” (Bushey 2014; Qiu et al. 2011).3b) Indie App Developers are focused on product quality and do not consider the market being important for making decisions on major app releases; indeed, they do not want to be visible in the mass consumer but only try to meet the minimum expected performance (Qiu et al. 2011).</td></tr><tr><td>4) Producer&#x27;s Market Responsiveness</td><td>4) The more responsive, the more likely that a producer will make a distant design move, especially if the producer is an optimizer (Boudreau and Jeppesen 2014; Boyle and Shapira 2011; Greve 2002; Qiu et al. 2011).</td><td>4) The Conga App (for generating reports and documents from Salesforce data) has gone through a major update when recent market data suggested a performance drop (McCarthy 2016); The developer of “Doodle Jump” used the most recent usage data of his game, instead of relying on usage data after his major release months ago, to judge his competitiveness (Bushey 2014; Qiu et al. 2011).</td></tr></table>

more peaks and valleys so that a single change in a design element will not automatically lead to an increase in performance. Coupling affects the agent's search move indirectly: at any point of time in the iterative search process, coupling reduces an agent's potential to move from his current position to a better one nearby using hill-climbing, (visually speaking, K increases the chances that he is stuck on a local peak and there are only valleys around). Thus, the only way to cope with coupling is to embrace uncertainty and jump. Thus, K represents the fact that greater coupling renders a major app upgrade (a long-jump) more effective compared to a landscape with low coupling (Billinger et al. 2013) because there are more peaks compared to a landscape with lower K. Further, these peaks are spread further apart with tight coupling, increasing the odds of landing on them (Rivkin 2000). Thus, embracing uncertainty becomes more valuable if K is higher (compared to lower K).

## Theory Factor 2: Degree of Constraints Placed on Design Elements

Degree of Constraints Defined: Constraints refer to a platform owner's decision to limit the producer's choices in modifying a single element; modifications are restricted or not allowed at all (Woodard 2008). Constraints are distinct from coupling as they relate to a unique element and not the functional relationship between two technical design elements. An element can be coupled with others regardless of whether it is constrained.

Effects of Constraints on Producer Design Moves: Platform literature suggests that the extent of design constraints may affect design moves (Eaton et al. 2015; Tiwana et al. 2010; Woodard 2008). Since constraints limit producers' options for searching the design space, constraints that keep an element from being used require producers to consider alternative design elements to modify; in some cases, this triggers the producer to take a less certain rework for a design update (Eaton et al. 2015; Wareham et al. 2014). For example, innovative apps like Skyfire, surfaced from the constraint of Apple iPhone banning Adobe Flash (Eaton et al. 2015; Lee 2010). If constraints prevent a producer from using a key design element that would have led to greater acceptance in downloads, then constraints may nudge the producer away from creating a high-performing app (Eaton et al. 2015). However, in the case of Apple and Adobe Flash, many producers stopped working on their apps because they were not willing to make a distant move. Thus, the effect of constraints on producers' design moves may not be linear or direct.

Representation in the NK Model: Constraints are represented through fixed states of design elements (since our elements are binary, their state is fixed to 1 or 0). Constraints do not change the size and surface of the fitness landscape (unlike looseness/tightness of element coupling). They only reduce the actual number of design alternatives available to the producers, since some elements cannot be changed (e.g., from 0 to 1 or from 1 to 0). In Figure 1, we illustratively highlighted two constraints in grey: among six elements, elements four and five are fixed. Because of that, all three producers in Figure 1 only have four elements to manipulate, essentially reducing their available design space. We represent the degree of constraints available to producers during a particular simulation with four levels (low to high) by varying the number of randomly selected design elements constrained to zero. If there is a constraint, the producer will not be able to move to that location but will be forced to assess alternative locations around him. Since there will be less options (most likely in the immediate neighborhood of an agent), hill-climbing moves cannot be executed since constraints are placed on design elements nearby making local peaks inaccessible.

## Theory Factor 3: Competitive Aspirational Strength

Competitive Aspirational Strength Defined: Aspirations describe the desired performance level of a producer's goal (Shinkle 2012). In a platform context, it can be assumed that platform producers have a general desire to outperform others and achieve a highly competitive performance. However, the strength of this competitive aspiration may vary by producers. Some producers may have a high competitive aspirational strength, being focused exclusively on their apps becoming unicorns (or stars), that is, those that become mainstream and extremely popular such as Zynga or Pandora. For example, the developer of the “Black Panther” game is quoted as stating: “It’s all about visitor counts, download count, server count, people playing” (Boudreau and Jeppesen 2014, p. 1773). In contrast, other producers have interests in addition to achieving financial rewards, including reputation, signaling, learning, joy, and collective action (Baldwin and von Hippel 2011; Boudreau and Jeppesen 2014; Parker and Van Alstyne 2018). Such producers are described here as having only a moderate strength of competitive aspiration because competing for market visibility is only one of many reasons for them to contribute. A producer’s competitive aspiration strength may be affected by such factors as identity, individual differences, and institutional logic nurtured on the platform (Qiu et al. 2011; Schwartz et al. 2002; Shinkle and Kriauciunas 2012). For the purposes of our NK model, we are focused on one distinguishing characteristic of aspiration strength, that is, the desired market performance for the producer’s app relative to other producers on the platform (e.g., the most downloaded app etc.), in the sense of a relative performance target (Baucells et al. 2011; Billinger et al. 2013; Shinkle 2012). Producers pay attention to this relative target; it guides their design moves.

To classify two archetypes of producers with distinguishable competitive aspiration strengths and relative performance targets, we build on the established distinction between optimizing (or maximizing) and satisficing in the literature on search. Recent platform literature has also pointed to the importance of this distinction between two strengths of competitive aspiration for theorizing about producers' design moves (Simon 1973; Simon et al. 1987; Tiwana et al. 2010). Optimizers think they need to optimize and so their performance target is exclusively defined by market performance: they want to have the most competitive app (e.g., most downloaded, installed, or liked app). In contrast, producers with moderate strength of competitive aspirations will satisfy with a moderately competitive app since learning or reputation or joy are equally important reasons to build apps: their relative performance target is lower.

While any platform is likely to have both optimizing and satisficing producers, some platforms may be dominated by one type of producer. For example, a study by Vision Mobile (2015) of more than 10,000 mobile app developers in 130 countries found that Apple's iPhone platform is dominated by full-time professionals, with a large proportion of “hunters” who are highly competitive, and thus classify as optimizers. In contrast, the Window’s Phone platform is dominated by satisficers since, as hobbyists and explorers working part-time, they appear to be less concerned about their competitive standing.

Effects of Competitive Aspirational Strength on Producer Design Moves: Studies on platforms suggest that a central idea of theories of search and aspirations, of how competitive aspiration strength affects the choice of a distant search move, applies also to producers (Ansoff 1987; Billinger et al. 2013; March 1981; Shinkle 2012; Shinkle and Kriauciunas 2012). They encode their performance relative to their performance target in simple ways (either as success or failure) and adjust their next design move accordingly. Failure triggers a distant design move, while success implies that they won’t move at all. Thus, optimizers (producers with strong competitive aspirations) will strive for the higher target since they want to be the best. An optimizer then differs from a satisficer in two ways. First, the optimizers’ performance target is higher than a satisficer’s. Second, because an optimizer’s performance target is higher, small incremental changes to their apps at each iteration is unlikely to be sufficient to make their apps the best. Consequently, optimizers are more likely to engage in long-jumps compared to satisficers. For example, the developer of the game “Doodle Jump” (an optimizer) undertook major upgrades of his game every time his game had less users than the best game “AngryBirds” (Bushey 2014).

Satisficing producers, on the contrary, have a more moderate performance target and, thus, will not reorient and move away from their current approach every time their apps fail to be the best app in terms of market performance. They will only engage in a distant design move (a major upgrade of their apps) if they are not meeting a moderate performance level to avoid being removed from the platform (Baldwin and von Hippel 2011; Qiu et al. 2011; von Hippel 2005). “Indy app developers,” such as Sam Soffes the maker of Cheddar app, are examples of satisficers. As a professionally trained independent software developer, Sam has a craftsman mentality, and seeks high engineering and design standards, declaring a new version “ready to ship [only] when it is complete, well tested, and has good documentation,” not simply to respond to a drop in downloads (Qiu et al. 2011, p. 7). He is more concerned about peer recognition, learning new technologies, and serving particular niche users where quality and experience matter rather than appealing to the mass market (downloads, ratings, etc.). Indeed, people like Sam Soffes even “rage against the app store and the popping of apps that are not well crafted like the Indy apps” (Richie 2016). He would not consider a major upgrade only because his app is not among the most competitive ones.

Representation in the NK model: Since all agents are rationally bounded, they will always first try to make quick wins: predictable hill-climbing moves. If such hill-climbing moves do not increase their performance (perhaps because they are in a location where coupling creates only valleys around them), they will attend to their performance target (the best if an optimizer, and the average performance of all apps if a satisficer). Only if the current achieved performance of their app falls below their target will they make a long-jump, provided they have the resources. Thus, generally speaking, optimizers have a higher probability than satisficers in taking a long-jump. However, it is important to note that each agent has a different probability at a particular point of time of engaging in a long-jump, since his choice of a long-jump is affected by his position in the landscape (and thus the hill-climbing moves available) as well as the performance distribution of all agents at a particular point of time.

## Theory Factor 4: Producers' Market Responsiveness

Market Responsiveness Defined: Responsiveness refers to the speed with which a producer responds to changes in his market performance (Ansoff 1987; Greve 2002; Labianca et al. 2009; Shinkle 2012). Empirical studies on app developers suggests that not all producers on a platform are equally responsive to market changes (Greve 2002; Qiu et al. 2011; Tiwana 2014a; Van Alstyne et al. 2016; Woodard et al. 2013; Yin et al. 2014). Highly responsive producers respond quickly in order to remain competitive (Billinger et al. 2013; Boyle and Shapira 2011; Greve 2002; Shinkle and Kriauciunas 2012).

Market responsiveness is distinct from the producer's competitive aspirational strength. While the latter defines the relative performance target that a producer strives for, the former describes how recent the market insight is that he uses to assess his market performance. An optimizer focused on being “the best” may delay responding to the market to see if the market continues to trend a certain way, and thus trusts past market data to judge his performance. A satisficer may respond quickly to ongoing market changes because he is curious as to how a new design element he uses, like augmented reality or face recognition, affects his app’s users. Thus, instead of relying on past market data, such as usage data after the last major release, he uses the most recent market information to judge whether his app is good enough (around average).

Effects of Producers' Market Responsiveness on Producer Design Moves: If producers are not responsive to the market, they tend to believe that their app is sufficiently competitive (Boudreau and Jeppesen 2014; Qiu et al. 2011), simply because they use past market insights to judge their performance without recognizing that other producers have moved on and improved. Thus, most likely, they will not see the need to move and upgrade their app, in particular if they are satisficers. Studies on search in high competitive environments suggest that the opposite is true if a producer is responsive to the market and is also an optimizer (Boyle and Shapira 2011): Optimizers (or leaders) who are highly responsive to the market, tend to engage in uncertain distant moves (long-jumps) every time their apps score lower than the current top apps without considering how well their app has done in the past. For example, the producer of the game “Doodle Jump” paid close attention to the current market leaders like “Angry Birds” (Bushey 2014, Qiu et al. 2011) on a daily basis, and considered a major design change every time his app had a few less users. If he was less responsive to the market, he would have trusted the market insights gained from several iterations earlier when he launched a major revision and was clearly outperforming other apps because of the new features he had integrated in his app. The “Doodle Jump” developer has a so-called “liability” of highly responsive optimizers who want to remain at the top, and thus engage in excessive distant search efforts irrespective of the uncertainty associated with doing so (Boyle and Shapira 2011).

Representation in the NK Model: We model four levels of responsiveness by capturing the speed at which a producer responds to the market. The producer attends to the app's performance from the last iteration, or with a delay of 5, 10, or 25 iterations, taking an action at one of these junctures. His responsiveness defines which market information agents use to assess his performance relative to his performance targets. For any single simulation run, all agents will have the same market responsiveness. Thus, the lower the market responsiveness, the lower the probability that an agent will take a long-jump, simply because the platform as a whole has moved on and improved, at least to some extent. However, it is important to note that not all agents act the same way, simply because they are in different locations and because they have a different relative standing compared to others.

## Sociodynamic Exploration of All Four Theory Factors Conjointly

Our model explores the conjoint effects of a manipulation of each of the four factors on platform performance and captures the sociodynamic process in which changes in these parameters unfold. All four factors first and foremost affect the individual-level design move. However, when hundreds or thousands of producers move through an iterative design process in parallel, they are not isolated but mutually influence each other through feedback loops from the market about the competitive standing of a single producer's app relative to others. The feedback loop adds an entirely new characteristic to the exploration and connects the individual-level with the platform-level. Feedback on app performance is based on the aggregate performance of all producers on the platform and as, such, whether a producer is triggered to move based on less than expected performance cannot be known in advance. The nature of the effects of each of the four factors and the nonlinearity of the NK space is such that a particular producer's choice of a certain design move (as well as the performance implications) is nondeterministic and conditionally probabilistic. Each agent creates his unique path through the landscape, and at every step there are multiple ways as to how he may move on because of his unique context. For example, whether an agent makes a jump at a certain time depends on the particular condition: the agent's current performance, the performance of the best (or the median), and the location in the landscape (and the valleys and peaks around an agent). In other words, platform performance emerges “bottom-up” through a complex, nonlinear, sociodynamic process across a “rugged” design space.

We chose an agent-based model to discern the sociodynamics of how a parallel search of multiple producers unfolds (Bruch and Atwell 2015; Epstein 2006; Epstein and Axtell 1996; Nan and Tanriverdi 2017). In essence, our goal is to develop a generative model that offers new insights that existing empirical research cannot afford since it is almost impossible to jointly vary all four theoretical factors across a large parameter space. We then explore how the sociodynamics affect collective outcomes after a long period of time (e.g., months and years).

## Model Implementation

In this section, we summarize how we implemented our theoretical model computationally. We present the model parameters, the specification of simulation experiments, and our actions for model validation.

## Model Specification and Simulation Parameters

Table 3 summarizes the basic elements and parameters that we use to translate our NK assumptions and our theoretical assumptions about how the four manipulated parameters affect individual-level search in executable code.

At the beginning of each simulation, each design alternative is associated with a certain fitness value. To assign the fitness values prior to the simulation, we follow Kauffman (1993) and Levinthal (1997) and randomly draw these values from a normal distribution between 0 and 1 to allocate the individual fitness contribution $w_{n}$ for each design element $d_{n}$ . The performance value $w_{p}(d)$ of a certain design alternative is the mean of the fitness contribution $w_{n}$ of each design element $d_{n}$ of a particular design alternative (Frenken 2006). Thus, there are N performance values $w_{p}(d)$ of N design alternatives that represent all objectively achievable fitness values for an agent searching the landscape. However, as described in the “Conceptual Development” section, our boundedly rational agents cannot see all locations and their fitness values.

When searching the NK landscape, each agent is given a certain instantiation of a 16-dimensional vector $\mathrm{d} = <\mathrm{d}_1,\dots ,\mathrm{d}_{16}>$ with binary design elements (a design set) representing an agent's position in the landscape. The fitness value associated with that location represents the realized performance $w_{r}(d)$ of the agent at a certain point of time. During each iteration of our simulation, all agents make a single move on this landscape from one location to another (although in some iterations some agents may not move). They move by changing one or several design elements in the decision vector. One iteration represents a single move of all the agents on the landscape, in which they choose a new design alternative. However, some agents might not move because they do not have any hill-climbing options available, and they are not below their performance target. An agent's goal is to increase the $w_{r}(d)$ of his design alternative. To do so, within any single iteration, an agent can take only one choice: (1) a hill-climbing move or (2) a long-jump or (3) not move at all. In a hill-climbing move, an agent moves a Hamming distance of one by changing only one design element. Since he can assess the fitness of all design alternatives of all neighboring solutions, he moves to the neighboring design alternative with the highest fitness value based on the assessment of the performance potential of neighboring solutions $w_{pn}(d)$ . If none of those alternatives leads to an improvement in fitness, he does not move, unless his design strategy makes him attend to his relative performance target. In a long-jump, the agent randomly changes N design elements in his 16-dimensional design vector, with N being randomly drawn from $<2,\dots,6>$ because he cannot assess the fitness of this new design alternative up front. Thus, the new realized performance $w_{r}(d)$ in a certain iteration may be much higher or lower than the one in the previous iteration. The decision to take a long-jump is guided by the producer's search heuristic h as a probabilistic function (see Table 3).

At the start of each new iteration within the simulation, an agent will first examine opportunities for hill-climbing by assessing the $w_{pn}(d)$ of neighboring design alternatives only a hill-climbing move away—compared to the realized performance of his current location on the landscape $w_{r}(d)$ . The performance potential $w_{pn}(d)$ of neighboring design alternatives is affected by the coupling (K) and constraints (C) of the fitness landscape. If all neighboring performance potentials are lower than the agent's current realized performance $w_{r}(d)$ , the agent is in a local maximum. Whether he jumps or not depends on his design strategy (market responsiveness measured as speed of adjustment (S) and the strength of competitive aspiration (A)).

Long-jumps take a lot of effort (resources). We equip each agent with resources (R) (a certain number of long-jumps). If these resources are exhausted, the developer is unable to make a long-jump. Following prior work (e.g., Rivkin 2000), we choose 100 as a maximum for R to establish a population with significant (but not extremely large) resources for long-jumps. This number does not exactly represent reality, but given the binary nature of our decision vector, 100 long-jumps are comparable to a significant number of major app design releases (e.g., 100 long-jumps implying binary design changes in the design elements may represent 10 major app releases using a more complex decision vector with nonbinary decisions).

We used 1,000 agents to represent a sufficiently large number of competing developers. We derive platform performance $W_{r}(d)$ as the aggregate (or the same as the average expressed in thousandths) of the realized performance of all 1,000 agents $w_{r}(d)$ at the end of the simulation. During all the iterations for any single simulation, the landscape and agents' search strategy remain constant. Since our agents are not communicating with each other, results can be compared across different simulation runs.

The simulation starts with the creation of the landscape based on tightness of coupling (K) and constraints (C), and the random position of the 1,000 agents on that landscape. All agents are equipped with the same single competitive aspiration strength and the same market responsiveness for any particular simulation, with different simulations differentially varying the strength and responsiveness. Each individual agent then starts his autonomous iterative design process (a series of search moves across the landscape), which is affected by both the landscape and the design strategy with which he is equipped. The simulation will include multiple iterative search moves (iterations). The simulation ends when all agents either (1) find a peak in the NK landscape that meets their performance target; (2) exhaust their resources R; or (3) reach a total limit of 500 iterations (see Appendix B. $^{5}$ )

<table><tr><td colspan="2">Table 3. Overview of Simulation Parameters</td></tr><tr><td colspan="2">Basic Parameter of NK Design Landscape</td></tr><tr><td>Number of design elements</td><td>N = 16.</td></tr><tr><td>Design vector d</td><td>d =, d binary (0,1); describing all potential design alternatives as combinations of 16 design elements.</td></tr><tr><td>Size of landscape</td><td> $2^{16}$ , 65,536 combinations of 16 design elements.</td></tr><tr><td>Type of NK landscape</td><td>Random, normalized between [0,...,1] after its construction (Kauffman 1993); fixed throughout the simulation experiment; all agents search the same landscape; this allows comparing results across different simulation runs.</td></tr><tr><td>Individual performance opportunity space (performance potentials)</td><td> $w_p(d)$  N fitness values on a scale from [0,...,1] associated with all points in the landscape.</td></tr><tr><td colspan="2">Individual-Level Search Across Landscape and Agent&#x27;s Search Heuristic</td></tr><tr><td>Individual realized performance (fitness)</td><td> $w_r(d) = w_p(d)$  on value from [0,...,1] that agents have realized when choosing a certain design alternative.</td></tr><tr><td>Hill-climbing</td><td>Move by only a Hamming distance of one with total visibility of the fitness  $w_{pn}(d)$ ) of all neighboring design alternatives; agents choose the maximum position if there are multiple alternatives that fulfill ( $wr(d) < wp(d)$ ); if there is no better alternative, they keep their current design alternative (they do not move).</td></tr><tr><td>Long-jump</td><td>Random change of n parameters in the decision vector d; n = &lt;2,...,6&gt;; the number of elements changed is drawn randomly; agents can neither assess the performance of the new design alternative up-front, nor can they return to their original location after a long-jump. Long-jumps are highly uncertain because the outcome of a long-jump is not predictable.</td></tr><tr><td>Search heuristic h (non-deterministic)</td><td>h = f (A,  $w_r(d)$ ,  $w_{pn}(d)$ , R, A, S) with  $w_{pn} = f(K,C)$ . Agents always try to improve their performance through hill-climbing. If no improvement in their fitness can be found through hill-climbing ( $w_{pn}(d) < w_r(d)$ ), then they compare their current fitness,  $w_r(d)$ , with the performance target associated with their aspiration strength (A) (the best or the median). We use a discrete function to model their response to A: if their own performance  $w_r(d)$ , is lower than their target associated with A, they engage in a long-jump, assuming they have sufficient resources R left to perform a long-jump. If their own performance  $w_r(d)$  is higher or equal to the target, they do not move. However, if in the next iteration their performance  $w_r(d)$  is below the target, they start moving again.</td></tr><tr><td>Resources for long-jumps R</td><td>Each agent has R resources for long-jumps available with a mean of 100. R represents a number of long-jumps. We normally distribute R across our agents.</td></tr><tr><td colspan="2">Manipulated Parameters (Two for Architecture and Two for Design Strategies)</td></tr><tr><td colspan="2">Platform Architecture: Coupling and Constraints in the Design Space</td></tr><tr><td>1. Tightness of coupling (K) (16 levels)</td><td>K with values from 0,1..15; interactions are randomly assigned.</td></tr><tr><td>2. Degree of constraints (C) (4 levels)</td><td>C = 0 no constraintsC = 2, some constraints, 2 elements, randomly chosen out of 16C = 4, moderate constraints, 4 elements, randomly chosen out of 16C = 6, many constraints, 6 elements, randomly chosen out of 16</td></tr><tr><td colspan="2">Producer Design Strategy</td></tr><tr><td>3. Strength of competitive aspiration (A) (2 levels)</td><td>Optimizing: A = max( $w_r(d)$ ) of all agentsSatisficing: A = median( $w_r(d)$ ) of all agents</td></tr><tr><td>4. Market responsiveness measured as speed of adjustment to market (S) (4 levels)</td><td>S = 1, high, all agents assess performance of their apps after each (1) iterationS = 5, moderate, all agents assess performance of their apps after 5 iterationsS = 10, low, all agents assess performance of their apps after 10 iterationsS = 25, very low, all agents assess performance of their apps after 25 iterations</td></tr><tr><td colspan="2">Platform Performance</td></tr><tr><td>Number of agents</td><td>D = 1000</td></tr><tr><td>Platform performance (fitness)</td><td> $W_r(d) = \text{mean}(w_r(d))$  across A agents at end of simulation</td></tr><tr><td>End of simulation</td><td>Simulated experiments end when (1) all the agents exhaust their resources R, (2) when all agents achieve their aspirations, or (3) when the total number of 500 iterations is reached. On average, the number of iterations was 311 per simulation experiment.</td></tr></table>

## Simulation Experiments

We ran more than two million exploratory simulation experiments (352,000 for our main experiments and more than 1.6 million runs for robustness checks) in which, at the start of each simulation experiment, we specified a certain combination of our manipulated parameters for platform architecture (K, C) and producer design strategy (A and S). As discussed earlier, A and S are the same for all 1,000 agents during a simulation, and K and C remain fixed throughout the iterations. This gives us an opportunity to precisely explore the role of individual and collective variability while excluding effects from variability caused by different design strategies within a platform population, as well as to explore variability caused by interim changes made to the platform architecture by the platform owner. The individual variability results from the fact that each agent has a unique condition: he is positioned in a particular location on the landscape and has a certain standing relative to the rest. As he moves through the landscape, his particular context (ruggedness) and his relative performance at a particular time affect the probability of whether he takes a long-jump or a hill-climbing move or settles. At the end of one simulation (with multiple iterative search moves), we calculate total platform performance $(\mathrm{W_r(d)})$ , and store the realized performance of all 1,000 agents to calculate performance distributions. Each experimental condition was repeated 500 times and the final results are averaged.

We performed our simulation in three stages. Table 4 summarizes the order in which our simulation experiments were run. Stage 1 focused on the conjoint effect on platform performance of (1) tightness of coupling K, and the producers' design strategy while holding (2) constraints C constant. In Stage 2, we explore both coupling K and constraints C to account for their mutual interaction when studying the joint effect with producer design strategy on platform performance. In both stages, we ran two base case experiments in which we did not equip our agents with a design strategy. Rather, we use hill-climbing agents, which only take hill-climbing moves in order to represent a situation where producers do not have design strategies to compete (Woodard et al. 2013). They lack competitive aspirations. After the base cases, in both of these stages, we gradually increased the number of manipulated parameters from two (coupling and aspiration strengths) to four (all four factors) (remember that we repeat each experiment 500 times) to explore the patterns emerging from individual and joint manipulation of the parameters. In Stage 3, we ran three groups of robustness checks to examine the sensitivity of our results for alternative assumptions of how agents adjust their design moves throughout the iterative design process (see Appendix A for more details).

Our computational simulation model was written in Julia (version v 0.4), a fast language particularly suited to agent-based simulation and originally developed at the Massachusetts Institute of Technology (Bezanson et al. 2012). Plots were made in Julia and R. We used a single-instance EC2 machine (m4 and c4 instances) available through Amazon Web Services to perform the computation. It typically took a few days for each experiment to complete. The code is publicly accessible (see details in Appendix C).

## Model Validation

In accordance with the established practice of using simulation studies to stimulate a new theoretical view, we took four actions (Anderson 1999; Davis et al. 2007; Law 1991; Nan and Tanriverdi 2017). First, as demonstrated in Tables 1 and 2, in translating the NK model to the context of platform architecture, we made sure that our abstract NK assumptions were consistent with prior NK usage and an appropriate abstraction of a real-world platform, and we ensured that our causal theoretical assumptions about the four factors were consistent with empirical observations. Second, before submitting our model for simulation, we chose simulation parameters that have been validated in prior NK simulations as being appropriate. Third, we ensured consistency between base case findings and empirical work on platforms (see Table 5 in “Results”) and discuss our findings using practical implications to ground our findings empirically (see Table 6 in “Results”). Finally, we performed a series of sensitivity analyses in order to ensure that our results were robust. These sensitivity analyses are reported in Appendix A.

## Results

We present our exploratory results in accordance with our two-stage experimental analysis process. Table 5 describes our base case results for stage 1 and stage 2. Following previous work (Almirall and Casadesus-Masanell 2010), our base cases consist of agents using local search only (hill-climbing). They have neither competitive aspirations nor variations in market responsiveness. In stage 1, the base case only varies the fitness landscape in terms of coupling (K). In stage 2, the base case varies the landscape in terms of coupling (K) and constraints (C).

Table 6 summarizes results of the simulation experiments for stages 1 and 2, that build upon the base cases.

<table><tr><td colspan="3">Table 4. Summary of Two-Stageed Exploratory Simulation Experiments</td></tr><tr><td>Experiments</td><td>Parameter Space of Two Factors of Design Strategy (Applied to all 1000 Agents)</td><td>Parameter Space of Two Factors of Design Space Searched by Producers</td></tr><tr><td colspan="3">Stage 1: Tightness Coupling K, Constraints C, Competitive Aspirational Strength A, and Market Responsiveness (measured as Speed of Adjustment to Market S)</td></tr><tr><td>1. Experiment 1: Base case1: Coupling</td><td>No competitive aspirations (agents are hill-climbing only)</td><td>16 levels of coupling (K from 0,...,15)No constraints (C = 0)</td></tr><tr><td>2. Experiment 2: Coupling &amp; Competitive Aspiration Strength</td><td>Two distinct strengths of competitive aspirations (optimizing vs. satisficing)One level of speed of adjustment modeled (S = 1)</td><td>16 levels of coupling (K from 0,...,15)No constraints (C = 0)</td></tr><tr><td>3. Experiment 3: Coupling &amp; Competitive Aspiration Strength &amp; Speed of Adjustment</td><td>Two distinct strengths of competitive aspirations (optimizing vs. satisficing)Four levels of speed of adjustment modeled (S = [1,5,10,25])</td><td>16 levels of coupling (K from 0,...,15)No constraints (C = 0)</td></tr><tr><td colspan="3">Stage 2: Tightness of Coupling K, Constraints C, Competitive Aspirational Strength A, and Market Responsiveness (measured as Speed of Adjustment to Market S)</td></tr><tr><td>4. Experiment 4: Base case2: Constraints &amp; Coupling</td><td>No competitive aspirations (agents are hill-climbing only)</td><td>16 levels of coupling (K from 0,...,15)4 levels of constraints C = [0, 2, 4, 6]</td></tr><tr><td>5. Experiment 5: Constraints &amp; Coupling &amp; Competitive Aspiration Strength</td><td>Two distinct strengths of competitive aspirations (optimizing vs. satisficing)One level of speed of adjustment modeled (S = 1)</td><td>16 levels of coupling (K from 0,...,15)4 levels of constraints C = [0, 2, 4, 6]</td></tr><tr><td>6. Experiment 6: Constraints &amp; Coupling &amp; Competitive Aspiration Strength &amp; Speed of Adjustment</td><td>Two distinct strengths of competitive aspirations (optimizing vs. satisficing)Four levels of speed of adjustment modeled (S = [1,5,10,25])</td><td>16 levels of coupling (K from 0,...,15)4 levels of constraints C = [0, 2, 4, 6]</td></tr><tr><td colspan="3">Stage 3: Robustness Checks (Discussed in More Detail in the Online Supplement)</td></tr><tr><td>7. Experiments focused on Robustness Checks: Three types of robustness checks focused on search moves and design strategies</td><td colspan="2">Robustness Check 1: Alternative modeling of long-jump (continuous instead of binary search moves in accordance with Billinger et al. (2013))Robustness Check 2: 4 levels of resources for long-jumps R: R = [10, 25, 100 and 500] representing the mean number of long-jumps available for all agentsRobustness Check 3: Probabilistic modeling of failure-induced long-jump rather than dichotomous</td></tr></table>

## Results Stage 1

In the first stage of simulations, we vary degree of tight coupling (K), competitive aspirational strength (A), and speed of market responsiveness (S) while holding constraints (C) constant at zero (i.e., no constraints). We use our base case 1 shown in Figure 3(a) as the “hill-climbing only” slope as a comparison for simulations in which producers are either satisficers (slope of \*) or optimizers (slope of diamonds). Apparent from Figure 3(a) is that, when a platform consists of agents who are either optimizers or satisficers, such a platform will perform collectively better than the base case with hill-climbing only. Moreover, comparing the inflection points on the slopes indicate that, when producers’ design strategies are considered, some tight coupling does not harm platform performance. Finally, after only a moderate tightness of coupling (K > 7) is considered, satisficers collectively outperform optimizers, despite literature suggesting that the long-jumps more likely taken by optimizers are more effective if there is coupling (Billinger et al. 2013; Fleming and Sorenson 2001; Tiwana et al. 2010). Apparent from these results is that optimizing agents are not collectively rewarded and satisficing agents collectively perform equally or better than optimizing agents on tighter coupled design spaces.

To further explore these results of lower performance of optimizers in more tightly coupled design spaces, we examined the distribution of the individual performance of all agents at different tightness of coupling, as shown in Figure 3(b). Apparent from Plot B, where coupling tightness is high (K = 11), only a few optimizers achieve very high performance levels, while a sizeable number get stuck in lower positions resulting in lower aggregate performance. In comparison, satisficers in Plot B had a smoother distribution through the top range, with a handful achieving very high positions and only a few ending up in lower performance positions. A look at the maximum tightness of coupling (K = 15) (Plot C) provides a clearer picture of the same phenomenon. In the case of satisficers, few achieved very high positions, while many were close to the top and some occupy lower positions. This suggests that platforms with tighter coupling, using exclusively satisficing producers, perform better than platforms with exclusively optimizing ones.

<table><tr><td colspan="3">Table 5. Empirical Consistency of Base Case Findings</td></tr><tr><td>Stage</td><td>Base Case Finding</td><td>Empirical Consistency Check</td></tr><tr><td>Stage I Base case: 16 levels of coupling; no constraints, hill-climbing only</td><td> $B_{1}$ : If producers lack competitive aspirations, an increase in coupling leads to significant performance drops</td><td>When semiconductor platforms become increasingly coupled, this led to significant challenges in building valuable products, leading to performance drops (Baldwin and Clark 2000)Before MySpace opened the platform, high coupling led to significant performance drops (Woodard et al. 2013)</td></tr><tr><td>Stage 2 Base Case: 16 levels of coupling; 4 levels of constraints, hill-climbing</td><td> $B_{2}$ : Constraints and coupling jointly lower platform performance (when producers lack competitive aspirations)</td><td>When OpenStack, an OSS platform, introduced constraints on its APIs to make them less compatible with AWS, this led to significant performance drops in the new components created by the developers (Tee and Woodard 2013)</td></tr></table>

<table><tr><td>Finding</td><td>Practical Interpretation</td><td>Empirical Examples</td></tr><tr><td colspan="3">Simulation Stage 1: Joint Effects of Coupling, Competitive Aspirational Strength, and Market Responsiveness on Platform Performance Holding Constraints Constant at C = 0</td></tr><tr><td> $F_1$ :When producers' design strategies are considered, some tight coupling does not harm platform performance(in contrast to the assumption that coupling significantly drops performance).</td><td>Platforms can perform well even with some tight coupling, as long as producers have some degree of competitive spirit; complete decoupling is not needed.</td><td>Mobile app platforms like iOS or software enterprise platforms like IBM PaaS can perform well even with some moderate coupling across the different layers of the platform architecture (e.g., data access (API) and real-time analytics). They can perform well If they make sure that their producers have at least some aspirations to build apps that meet platform's user needs by using app metrics and other governance practices to increase attention to the market.</td></tr><tr><td> $F_2$ :Platforms with tighter coupling, using exclusively satisficing producers, perform better than platforms with exclusively optimizing ones(in contrast to the expectation that optimizers cope better with coupling).This finding occurs because optimizers create unequal performance, separating a few "stars" from the rest, dragging down aggregate performance.</td><td>Platform owners should NOT assume that it is better to have optimizing producers when their platform is tightly coupled since they can harm the platform's market performance; there is significant value to incentivizing satisficing strategies and encouraging other interests.</td><td>The various policies used by platform owners to create fierce market-oriented competition (e.g., leaderboards, and competitions offered by Apple) may backfire when coupling is tighter; they induce too much change: optimizers will make major updates too often, and will eventually fail and accrue too much technological debt. It might be better to subdivide leaderboards by categories of apps, effectively reducing competition (and unnecessary long-jumps resulting from that), and encouraging more than just market performance and downloads (e.g., app with best tech feature, producer's community spirit, etc.).</td></tr><tr><td> $F_3$ :Platforms with tighter coupling, using exclusively satisficing producers will no longer perform better than optimizers if satisficers are slow market responders.</td><td>Platform owners with tighter coupling should encourage fast response to changing conditions from platform producers, especially if producers are satisficers.</td><td>New technologies, particularly in their early stages, result in tightly coupled design elements, such as with virtual reality and augmented reality now appearing in the iOS and Android platforms for user authentication, creating new functional interdependencies across different layers and elements of the platforms. Platform owners should foster their adoption, paying special attention to satisficer producers.Satisficer producers should have clear incentives to further develop and update their apps. The use of recommender systems could help.</td></tr><tr><td colspan="3">Simulation Stage 2: Joint Effect of Coupling, Constraints, Competitive Aspirational Strength, and Market Responsiveness on Platform Performance</td></tr><tr><td> $F_4$ :With moderate or more constraints, loose coupling performs worse than moderately tight coupling if producers have competitive aspirations(in contrast to the expectation that tighter coupling will harm performance).</td><td>Even if loose coupling could be achieved, it might harm rather than benefit the platform if producers are constrained in modifying certain design elements (API etc.).</td><td>·If Apple decides to decouple design elements, this may lower performance because of the constraints placed on certain design elements (e.g., API or code library can be implemented only in very restricted ways); then, producers would not need to make major design changes to combine them with other design elements (simple plug-and-play is possible).·If constraints are in place, tighter coupling between design elements can encourage producers to explore new ways to translate constraints into better performing apps and they will not have to worry so much about performance drops because of the constraints put in place by the platform owner.</td></tr><tr><td> $F_5$ :Platforms with constraints are not negatively affected by optimizing strategies if they are tightly coupled.</td><td>Owners offering tightly coupled platforms with many constraints may ignore the producers' design strategies and focus on balancing constraints and coupling.</td><td>·If platform owners constrain how new (more tightly coupled) technologies are used, they do not have to worry as much about the competitive aspirations of their producers but only have to ensure sufficient responsiveness to the market and user needs.</td></tr></table>

![](/api/attachments/YH3Z4EDE/fulltext/images/7321d1394efe733f2ed92d5f25a9c54c7ac57f634ca5b632ba08cd8fbed5bf29.jpg)  
(a) Platform Performance (Aggregate)

![](/api/attachments/YH3Z4EDE/fulltext/images/c7fd9e658fabef7f4f019266c1c32e404af27c797da124c517dfffc0bf8183dc.jpg)

![](/api/attachments/YH3Z4EDE/fulltext/images/45f8e9f569b1cce5a7e849f9971d5476d41a2909cf0fb9e74318de77b776b340.jpg)

![](/api/attachments/YH3Z4EDE/fulltext/images/6d022526d9406e6fd1eac2e181e0dd0d94350b501eb68ab13f08820badfe81d7.jpg)  
(b) Distribution Plots A, B, and C for Platforms with Different Levels of Coupling
(Plot A: K = 3; Plot B: K = 11; Plot C: K = 15)

Figure 3. Platform Performance for Platforms with Different Levels of Coupling (K) and Producers with Different Aspiration Strengths (Optimizers Versus Satisficers)

Taken together, these findings indicate that platforms can perform well even with some tight coupling, as long as the producers have some competitive aspirations. Moreover, platform owners should not assume that it is better to have optimizing producers since such producers can drag down the platform's performance with any degree of tight coupling. Finally, given that satisficing producers can foster higher platform performance, we encourage platform owners to revise their leaderboards and metrics so that they encourage not only optimizers but also satisficers, who are motivated not by a mission to win but for other reasons as well. In the next experiment, we included the second parameter describing design strategy, market responsiveness, measured in terms of speed of adjustment. Each simulation takes on one of four values: from high (after each iteration, S = 1) to low (after every $25^{th}$ iteration, S = 25). Figure 4 summarizes the results in four plots varying in different tightness of coupling for our base case, then for all optimizers, and then for all satisficers.

Apparent from Figure 4 is that, for platforms with optimizing agents, speed of adjustment appears to have no effect on the negative relationship between coupling and aggregate performance. In contrast, for satisficers, slowing their market responsiveness (Plots F and G) harms performance dramatically such that the increased value they provide over optimizers in Figure 3(a) vanishes.

Visually speaking, the curves flip. This effect is especially strong at moderate to moderately tight coupling (3<=K>=9). This is because, as coupling increases, agents take long-jumps less frequently, eventually leading to lower platform performance. Moreover, with slow market responsiveness (Plot G), satisficers' performance becomes strongly hampered by any degree of coupling, even relatively loose coupling, unlike the inflection point found in Figure 3(a).

Practically, this finding suggests that satisficing producers should only be recruited if they tend to respond quickly to market conditions. Similarly, platform owners should encourage faster responses to changing conditions from platform producers. For example, fostering the adoption of new design elements such as artificial intelligence or machine learning libraries, paying special attention to satisficer producers, or providing incentives to further develop and update apps are ways to increase attention to the market, and thus also to a faster response to changing market conditions.

## Results Stage 2

Stage 2 explored the effect of platform design constraints. Results are shown in Figure 5 compared to the base case of hill-climbing for each plot, in which constraints lower the platform performance irrespective of the degree of coupling. Compared to the base case, we find that if design strategies are considered, coupling reverses the negative effect of constraints. For example, in Plot J depicting a platform with moderate constraints (e.g., C = 4), platform performance increases as coupling increases but only to a point. In practice, this suggests that even if loose coupling could be achieved, some coupling might even be wanted if platform owners place (or are mandated to place) constraints, since it triggers producers to respond to constraints with more distant moves (long-jumps). To conclude, with moderate or more constraints, loose coupled platforms perform worse than moderately tight coupling as long as producers have competitive aspirations.

Clearly, the presence of constraints only benefits apps in environments with moderate coupling tightness. The constraints that Apple imposes on its developers, for example, with respect to how they implement security and privacy through predefined components (e.g., because of policy regulations), may have a significant negative effect if Apple decides to decouple its design elements further or, in the other extreme, if they couple such design elements very tightly with other elements. This suggests that platform owners should consider both coupling and constraints when changing the architecture of the platform. When placing constraints, going for extreme conditions of coupling—very loose or very tight—might be harmful.

Examining the plots in Figure 5 further, we find that constraints also remove the performance differences as coupling becomes tighter. For moderate constraints (C=4), and tighter coupling (K>9), the gap between optimizing and satisficing is smaller. If constraints are further increased (C=6), the gap completely disappears. To conclude, platforms with constraints are not negatively affected by optimizing strategies if they are tightly coupled.

To uncover why performance differences disappear we took a closer look at the performance distributions of all 1,000 agents. In Figure 6, we plot the aggregated platform performance and the underlying distributions for moderate constraints (C = 4). For the distributions we chose three different tightness levels of coupling. As design spaces become more tightly coupled (Plot M), we see that competitive aspirations unfold in a positive way, no matter whether producers are optimizing or satisficing: both curves move to the right in Plot M compared to Plot L and there is no bimodal distribution that leads to inequalities. Only under extreme conditions, meaning extremely high coupling (Plot N: K = 15), do we observe the emergence of a lower peak for optimizing agents.

Plot D: High Market Responsiveness  
![](/api/attachments/YH3Z4EDE/fulltext/images/722da3726052a3465d0b5e2d7e08e5e19fe2494418b215fb78a0d6a3c3bde832.jpg)

Plot E: Somewhat Slower Market Responsiveness  
![](/api/attachments/YH3Z4EDE/fulltext/images/f4aadae0233ef4c96dd69b09c18d12e67dbd687acb4cb5612c37b23f9168fccd.jpg)

Plot F: Slow Market Responsiveness  
![](/api/attachments/YH3Z4EDE/fulltext/images/58881e5b1488a19d06297d9152afce03bf5758f4b91ff83137dc4a55c73f0990.jpg)

Plot G: Very Slow Market Responsiveness  
![](/api/attachments/YH3Z4EDE/fulltext/images/533ddc31687054e69afb0c801ff14f5ec9fb59add61e5794a9f171866f280f19.jpg)  
Figure 4. Platform Performance for Platforms with Different Levels if Coupling (K = 0,...,15) and Producers with Different Design Strategies—Two Aspirational Strengths (Optimizers Versus Satisficers) and Four Levels of Market Responsiveness (S = 1; S = 5; S = 10; S = 25)

Plot H: No Constraints  
![](/api/attachments/YH3Z4EDE/fulltext/images/5e1e0f3ecbaed77259bf7214cba2dda783bf4861c3f64450a4b540707a6bb11a.jpg)

Plot I: Some Constraints  
![](/api/attachments/YH3Z4EDE/fulltext/images/5b2a69b0388683a7476f7934e57f2229db8834fb894a47b88a50641977dbd14d.jpg)  
Plot J: Moderate Constraints

![](/api/attachments/YH3Z4EDE/fulltext/images/11eb16d47da130619ac98dcd23761e085b586cc08e7d612b09ff570019a8f21f.jpg)

Plot K: Many Constraints  
![](/api/attachments/YH3Z4EDE/fulltext/images/5f11a82087124cdd1a0c6bbb5e4c4d15c878b957c513957fbff751fb1e150c9a.jpg)  
Figure 5. Platform Performance for Platforms with Different Levels of Constraints (C = 0; C = 2; C = 4; C = 6), Different Levels of Coupling (K = 0,...,15), and Producers with Different Aspirational Strengths (Optimizers Versus Satisficers)

Practically, this suggests that platform owners that use (or have to use) many constraints and also offer tightly coupled design elements (e.g., because they just introduced a range of new design elements like virtual or augmented reality for which standards have not yet been defined) may not have to worry about whether their producers are too competitive: as long as the producers are paying attention to the market and respond quickly to user needs, chances of skewed outcomes and inequalities are low.

## Discussion

Our NK simulations make several theoretical contributions. We will discuss those next, before pointing to limitations, highlighting implications for practice, and making some concluding remarks.

## Theoretical Contribution

Our primary contribution relates to the research stream on loose coupling and modularity in platform architecture (Alexander 1964; Baldwin and Clark 2000; Simon 1962; Tiwana 2014a; Tiwana et al. 2010). This stream generally asserts that platform architectures should be decoupled in order to prevent harmful performance drops and too much variance when producers make changes to parts of the platform. However, like others (Tiwana et al. 2010; Yoo, Henfridsson, and Lyytinen 2010), we questioned the assumption that platform owners can (or should) completely decouple the platform architecture. The technical elements that producers can use to build apps—ranging from data, software libraries, user interface templates, business processes—relate to different layers in the platform (Eaton et al. 2015; Ghazawneh and Henfridsson 2012; Yoo et al. 2012; Yoo, Lyytinen

![](/api/attachments/YH3Z4EDE/fulltext/images/a578a207df20ae794b30aea352ac3e06a70c14e81f7865a508df3c9821b975a7.jpg)

(a) Platform Performance for Moderate Constraints (C = 4)  
![](/api/attachments/YH3Z4EDE/fulltext/images/7c59d56b71f6fa21300d120a181e2e8a3a10f426d3f3c6f9eaa75a4b6dc23a3a.jpg)

![](/api/attachments/YH3Z4EDE/fulltext/images/440ea79e89d6fe2861c32d7f584637a79422b44fbbd460885b8961054d3afec2.jpg)

![](/api/attachments/YH3Z4EDE/fulltext/images/07a11bb8c7bad0ece9a92117004852ada64cc698bf1dffc136c30c5ea02ec1a2.jpg)  
(b) Distribution Plots L, M, and K for Platforms with Moderate Constraints (C = 4) and with Different Levels of Coupling (Plot L: K = 3; Plot M: K = 11; Plot N: K = 15)

Figure 6. Platform Performance and Distributions Plots for Moderate Constraints (C = 4); Distributions for Different Levels of Coupling (K = 3; K = 11; K = 15)

et al. 200b), and thus complete decoupling is simply not possible. Thus, advancing our understanding of different degrees of coupling, from moderately loose to tighter coupling, critical.

Here, our model generates important new insights into nonlinear effects of different degrees of coupling. Our results make three concrete suggestions to the literature on loose coupling in platform architecture.

First, we suggest that recent advances in modular systems theory for platform architectures (Tiwana 2015; Tiwana et al. 2010; Um et al. 2013; Yoo, Henfridsson, and Lyytinen 2010), deeply rooted in Simon's (1962) work on nearly decomposable systems, should incorporate our granular conceptualization of coupling and constraints among the various design elements in digital platforms, since these two factors of the platform architecture have significant performance implications. Such middle-range theorizing, as Tiwana (2015) calls it, is essential to advance literature on platform architecture. Further, modular system theory specifically developed for digital platforms (e.g., Tiwana 2015) should incorporate our insights on the sociodynamic search processes that explain how design strategies affect individual search, collectively aggregating to various levels of platform performance. Producers do not act in isolation from each other when designing their apps; feedback-loops from the competitive platform market and information about their competitive positions affect how they implement their strategies. Considering these feedback loops and their effect on search is essential as they trigger emerging behavior that moderates the effect of the platform's architecture in unexpected ways. For example, we find that optimizing and high sensitivity to changes in the competitive performance can trigger too many distant moves if architectures are tightly coupled. Thus, while a simple theoretical causal assumption from prior literature can be effective at the individual level—take long-jump moves with coupled design elements (Billinger et al. 2013)—the sociodynamics on a platform reverse this assumption.

Second, within this literature we specifically question the rationale that decoupling is needed to make the platform “tolerant of uncertainty,” so that producers can iterate their apps quickly without fear of major performance drops or even failure. Literature grounded in theories of modular systems (Pil and Cohen 2006; Schilling 2000) and real options (Baldwin and Clark 2006b; Gamba and Fusari 2009; Tiwana 2014) suggests that tight coupling of design elements may have significant negative implications for platform performance because of the way it affects a single producer’s iterative design process. If design elements are coupled, a small change in one element in an app may ripple through and affect many other design elements in unpredictable ways. Essentially, variance in outcome is very high and complete failure is not unlikely. Collectively, when many producers work in parallel on a platform, this can drive down the platform performance as a whole. However, the normative conclusion drawn, that decoupling is needed to make design tasks like an app design tolerant to uncertainty, is a conclusion we suggest may be too simplistic. When the strength of competitive aspirations of the producers are taken into account, the effects of uncertainty from more tightly coupled design elements may not have such a negative effect. For example, platforms with satisficing producers will be less skewed (than those with optimizers) even with more tightly coupled design elements.

We learn that collectively satisficing design strategies triggers a sufficient, but not too much, amount of distant design moves (long-jumps) that allow all producers to cope with variances in outcomes. Thus, instead of requiring platforms to have loosely coupled design elements to insulate the platform from uncertainty, we suggest that platforms simply encourage the participation of satisficing producers as insulators that make the platform tolerant to uncertainty. Since differences in design strategies may be rooted in producers' motivations, identities, and institutional logics (Berente and Yoo 2011; Qiu et al. 2011; Tilson et al. 2010; Wareham et al. 2014), our theoretical insights invite other scholars to explore how such design strategies can be nurtured so that they create insulating mechanisms.

Third, our model provides a more generalized explanation of the conjoint complex effect of coupling under conditions of technical constraints and provides more nuances to arguments of a potential dualistic logic between constraints and coupling raised in the literature (Eaton et al. 2015; Tiwana 2008, 2015; Wareham et al. 2014). While some argue that tighter coupling may potentially undermine producers' design efforts if there are constraints (Tiwana 2015), we find that, at least up to a certain degree of coupling, constraints and tighter coupling act in concert. With constraints, as coupling increases, producers engage in broader exploration and distant design moves (more long-jumps) because local design moves (hill-climbing) may not be an option from which producers can choose, simply because several design elements are coupled and moves to familiar designs are blocked. Distant moves and broader exploration become more likely. At the same time, constraints seem to make such exploration more certain—at least up to a certain degree of coupling, since platform performance increases. In sum, we contribute to the literature in describing the mechanisms when coupling and constraints act in concert rather than against each other.

We also contribute to a second stream of literature concerned with economic incentives associated with producers' access to the platform architecture. This literature is primarily focused on the competitive incentives that platform owners create when they invite external producers to build apps for their platform (Boudreau 2011; Boudreau and Lakhani 2015; Parker and Van Alstyne 2018), for example, through simple contracts, licensing, or IP rights. The primary assumption in this literature is that strong competitive aspirations and responsiveness to changes in the market are needed, whether producers are paid or unpaid, in order to improve platform performance. Lowering incentives to compete (e.g., through too little or too many intellectual property rights) is considered as being harmful for the platform. However, we question these results as our theory draws different conclusions. Our model suggests that the effect of design strategies interacts with coupling and constraints in conjoint and complex ways. Thus, the effect of design strategies, and lower or higher competitive aspirations, are not as unequivocal as suggested by scholars (e.g., Boudreau 2010, 2011). Indeed, we find that there are conditions where the moderate competitive aspirations of satisficers can actually lead to greater platform performance, compared to a platform that brings together producers with very strong competitive aspirations. The same applies to market responsiveness. This suggests, then, that the economic literature that assumes producers need to be highly competitive and responsive to the market needs to be reconsidered. In addition, while most economic theories of platform recognize the important role of access to the platform architecture on platform performance (e.g., Parker and Van Alstyne 2018), our findings strongly suggest that this literature should incorporate the fact that coupling and constraints not only create competitive incentives but also moderate the process and the outcome of the producer's design process.

Finally, we offer a contribution of the model embodied as a novel implementation of an NK algorithm. The computational NK model and the use of NK simulations to theorize about platforms is a contribution of its own. Our model, and its algorithm, can be used and extended by scholars concerned with platform architectures that vary in terms of loose or tight coupling and their producers' design strategies. The NK landscape translated to the platform context is particularly suited for that. It gives scholars a new way to reason about empirically observed performance differences of platforms widely discussed in everyday life, such as Google's Android, Apple's iOS, Facebook, or Twitter. Furthermore, it allows scholars to anticipate collective-level implications of a change in a platform's architecture (e.g., Apple's iOS with fewer constraints) or a platform owner's efforts to purposively nurture satisficing design strategies among its producers (e.g., Sony's PlayStation console platform encouraging its developers to experiment with creative virtual reality game ideas that might not necessarily sell well right away; see Muncy, 2018). A range of additional parameters can be built into the baseline specification as well as the different experimental conditions described, in order to use this new way of making sense of platforms and their performance in the world around us.

We suggest, in particular, several directions for future research on platform architecture in which our model could be extended to generate new insights. First, to simplify our analysis, in any particular simulation run, we fixed the tightness of coupling and the number of constraints in our landscape. However, as pointed out by platform scholars (Eaton et al. 2015; Ghazawneh and Henfridsson 2012), platform owners change the design elements available for the producers, typically not very often but through “boundary-tuning” efforts. As such, future research should extend the model by allowing for changes in the coupling tightness and constraints over time. Second, interdependencies between the producers were ignored (e.g., in the sense of profit dependencies and conditional returns). Also, interdependencies among platform users, in the sense of attachments among multiple platform users to the same app (“the richer apps become richer”), could be included in future modeling efforts. Adding these parameters may allow for a closer integration of the platform architecture results with producers’ design moves, conceptualized as search, and economic incentives.

Third, while we have focused exclusively on producers within a single platform at a time, the model could be extended to consider both platform architectures and producer design strategies as elements of the platform's competitive business strategy and their effect on inter-platform wars. For example, extensions of our model allow scholars to reason about battles between two competing platforms, such as the battle between the gaming consoles Microsoft Xbox versus Sony PlayStation (Groen 2013; Muncy 2018), with a focus on the supply side. Such a focus may account for differences and changes in the platform's architecture as well as the producer design strategies that contribute to either or both platforms. For example, scholars may model changes in such interdependencies between competing platforms, such as exploring the effect of situations when satisficing producers leave one platform (e.g., Microsoft's Xbox One) and join the competing one (e.g., Playstation's Console PS4). They switch because the latter is less constrained and encourages experimentation with new technologies (e.g., virtual reality) rather than just being focused on market performance (e.g., number of downloads). $^{6}$ Depending on the differences in the architecture of the competing platforms, such a model may predict how to prevent mass exodus from one platform to another as well as reveal impending transition points.

Our paper may also encourage the use of NK simulations in information systems research beyond the literature on platform architecture. For example, scholars studying information privacy (e.g., Bélanger and Crossler 2011) may use our NK algorithm, and its extensions, to advance an understanding of information privacy at the collective level in order to explain such phenomena as a collective spread of misinformation or privacy fatigue. Such simulations could represent the complex interplay within more or less coupled and controlled information search spaces (e.g., in social media or e-commerce), and the privacy practices used by a heterogeneous group of online users when searching, sharing, and transacting data. Unlike other methods used in privacy research (qualitative and quantitative empirical studies), an NK model would allow scholars to capture the sociodynamic process that unfolds when many heterogeneous individuals search and share information guided by their socially moderated information sharing strategies. In sum, we hope that our paper encourages other IS research fields to use NK-based simulation studies to explore implications of unique combinations of information systems' architectural landscapes and individuals' search strategies with those configurations.

Finally, we hope that our theoretical insights also inspire research designs for collecting empirical data on platform architecture, producer design strategies, and platform performance. For example, controlled experiments in virtual environments could provide richer insights into the antecedent conditions behind individual producers' design strategies and may further advance our understanding of search strategies and design moves taking place on real and ecologically more valid empirical landscapes. Future researchers might design a contest (e.g., a web application design contest) with a specific set of more or less coupled design elements (e.g., elements of the JavaScript visualization library D3.js). By purposively considering individual differences and human tendencies in terms of competitiveness and need for private gains when sampling developers (Levine and Prietula 2013), or by varying incentives and platform rules intended to nurture the strengths of competitive aspirations (e.g., more high-powered incentives fostering optimizing and competitive racing for more performance points), such studies could then empirically observe iterative design moves on empirical landscapes. Such experiments will further refine the individual-level theoretical assumptions about whether and how antecedent factors for optimizing (e.g., high-powered incentives or platform rules) affect design moves across empirical landscapes. Visually speaking, such experiments focusing on empirical landscapes can potentially turn the conceptualization of design moves as “leaps from peak to peak into, instead, a walk across a bridge.” $^{7}$

## Limitations

Our NK modeling and simulation is not without limitations. In the prior section we highlighted several ways in which our model could be advanced by future work. In addition to those limitations that translate easily into future work, it is important to point out that our NK simulation is a stylistic representation of reality. It reveals new, unexplored insights into how platform architectures affect performance via a sociodynamic process that other methods cannot achieve. Our abstraction and our exploratory approach come at the cost of translating our findings into empirical parameters and effect sizes. For example, design elements do not just have two states but typically have several. Furthermore, in our study we argued that satisficing behavior results from lower competitive aspiration strengths, and a lower priority of market performance (measured in terms of number of downloads) compared to other producer goals (e.g., quality of certain features, or use of certain programming styles). However, we did not detail further the trade-off between multiple goals and implications of satisficing on market performance for the strength of other aspirations and goals. Our findings are also at a more abstract level, and we hope that future work will focus on specific aspects of our findings in a more granular way using other, more suitable techniques.

## Practical Implications

Our simulations are abstract but our findings have broader practical implications. As summarized in our findings (Table 6), each finding of our simulation gives platform owners some guidance on how to architect their platforms so that they thrive sustainably. In addition, we offer two additional suggestions for transforming platform owners into platform architects.

First, platform owners should revisit the general assumption that decoupling is needed to make their platforms successful. Decoupling is costly, and our simulation suggests that this investment is not always justified. Indeed, we recommend that platform owners pay more attention to the design strategies of their producers. The use of platform metrics (e.g., observing frequency of updates, responding to performance drops, etc.) can be easily implemented and should help platform owners learn about the competitive aspirations and market responsiveness of their producers.

Second, our findings suggest that platform owners should consider actively shaping the design strategies of their producers using suggestions we presented in Table 6. They may also revisit whether or not they really want to create fierce competition on their platform since there is a trade-off: if they foster competition, they may have to invest in decoupling the design elements they are offering to their producers. Instead of decoupling, they might be better off creating less competitive environments and at the same time use information technology to make their producers aware of changes in the market. Second, our simulations indicate that platform owners should architect platform constraints in conjunction with coupling. They are not substitutes. It might be useful to increase coupling if there are constraints as it offers a means to get the best of both worlds: broad exploration and robustness (insensitivity to failure).

## Conclusion

Our work shows that the task of architecting platforms is an exciting but also a challenging one since the effect of architecture unfolds through a sociodynamic process that is nonlinear and cannot be engineered. This research is intended to inspire others to begin to address the interplay between platform architectures and platform performance in a way that captures human agency and the complexity of the social processes of how producers contribute to platforms. App design is often not about creating the most widely used app. Producers have different preferences and different strategies; our results suggest that nurturing this diversity can improve the overall performance and sustainability of a platform. Computational models like ours allow exploring the large design space related to the design of platforms: such exploration may be increasingly important as new technologies, such as artificial intelligence, are incorporated into platforms. Platform designers will want to be anticipating rather than reacting, and simulating can be an important form of anticipating.

## Acknowledgments

First, we thank our reviewers and editors for their constructive feedback and guidance throughout this research process. We also acknowledge those scholars that have provided valuable feedback when we presented earlier versions of the paper at conferences and invited talks: For example, we thank attendees of our presentations at the speaker series of the Northwestern Institute of Complexity, Northwestern University (November 2016), the Third Annual Research Symposium (2015) on Complexity & IT at the Montpellier Business School, France, or the research symposium organized by the Management of Technology Group at EPFL, Switzerland (September 2014). We also thank our own personal network of app developers who frequently contribute to digital platforms (e.g., iOS, Google Android, R, etc.) and helped us to make sense of our simulation results through discussions and observations. Finally, we would like to acknowledge the National Science Foundation in the United States: This work was financially supported by the Science of Science and Innovation Policy (SciSIP) program (grant number #1462044).

## References

Alexander, C. 1964. Notes on the Synthesis of Form, Boston: Harvard University Press.

Almirall, E., and Casadesus-Masanell, R. 2010. “Open Versus Closed Innovation: A Model of Discovery and Divergence,” Academy of Management Review (35), pp. 27-47.

Anderson, P. 1999. “Perspective: Complexity Theory and Organization Science,” Organization Science (10), pp. 216-232.

Ansoff, H. I. 1987. “The Emerging Paradigm of Strategic Behavior,” Strategic Management Journal (8:6), pp. 501-515.

Baldwin, C., and Clark, K. B. 2000. The Power of Modularity, Cambridge, MA: MIT Press.

Baldwin, C., and Clark, K. B. 2006a. “The Architecture of Participation: Does Code Architecture Mitigate Free Riding in the Open Source Development Model?,” Management Science (52:7), pp. 1116-1127.

Baldwin, C., and Clark, K. B. 2006b. “Modularity in the Design of Complex Engineering Systems,” in Complex Engineered Systems: Understanding Complex Systems, Berlin: Springer, pp. 175-205.

Baldwin, C., and von Hippel, E. 2011. “Modeling a Paradigm Shift: From Producer Innovation to User and Open Collaborative Innovation,” Organization Science (22), pp. 1399-1417.

Baldwin, C., and Woodard, C. J. 2009. “The Architecture of Platforms: A Unified View,” in Platforms, Markets, and Innovation, A. Gawer (ed.) Cheltenham, UK: Edward Elgar Publishing, pp. 19-44.

Baucells, M., Weber, M., and Welfens, F. 2011. “Reference-Point Formation and Updating,” Management Science (57), pp. 506-519.

Berente, N., and Yoo, Y. 2011. “Institutional Contradictions and Loose Coupling: Postimplementation of NASA’s Enterprise Information System,” Information Systems Research (23:2), pp. 376-396.

Bélanger, F., and Crossler, R. E. 2011. “Privacy in the Digital Age: A Review of Information Privacy Research in Information Systems,” MIS Quarterly (35:4), pp. 1017-1041.

Bezanson, J., Karpinski, S., Shah, V. B. and Edelman, A. 2012. "Julia: A Fast Dynamic Language for Technical Computing," Cornell University (https://arxiv.org/abs/1209.5145).

Billinger, S., Stieglitz, N., and Schumacher, T. R. 2013. “Search on Rugged Landscapes: An Experimental Study,” Organization Science (25:1), pp. 93-108.

Bonchek, M., and Choudary, S. P. 2013. “Three Elements of a Successful Platform Strategy,” Harvard Business Review (https://hbr.org/2013/01/three-elements-of-a-successful-platform).

Boudreau, K. J. 2010. “Open Platform Strategies and Innovation: Granting Access vs. Devolving Control,” Management Science (56:10), pp. 1849-1872.

Boudreau, K. J. 2011. “Let a Thousand Flowers Bloom? An Early Look at Large Numbers of Software App Developers and Patterns of Innovation,” Organization Science (23:5), pp. 1409-1427.

Boudreau, K. J., and Jeppesen, L. B. 2014. “Unpaid Crowd Complementors: The Platform Network Effect Mirage,” Strategic Management Journal (36:12), pp. 1761-1777.

Boudreau, K. J., and Lakhani, K. R. 2015. “Open’ Disclosure of Innovations, Incentives and Follow-on Reuse: Theory on Processes of Cumulative Innovation and a Field Experiment in Computational Biology,” Research Policy (44:1), pp. 4-19.

Boyle, E., and Shapira, Z. 2011. “The Liability of Leading: Battling Aspiration and Survival Goals in the Jeopardy! Tournament of Champions,” Organization Science (23:4), pp. 1100-1113.

Bruch, E., and Atwell, J. 2015. “Agent-Based Models in Empirical Social Research,” Sociological Methods & Research (44:2), pp. 186-221.

Bushey, R. 2014. “How to Make Millions in the App Store, According to the Guy Who Made the Original Viral Iphone Game Doodle Jump,” Business Insider (http://www.businessinsider.com/doodle-jump-anniversary-2014-3, accessed June 5, 2018).

Choi, P., McGuire, C., and Roth, C. 2016. “Lightning Platform Fundamentals: An Introduction to Custom Application Development in the Cloud,” Salesforce.com, August 1 (https://resources.docs.salesforce.com/214/latest/en-us/sfdc/pdf/salesforce\_creating\_on\_demand\_apps.pdf).

Cyert, R. M., and March, J. G. 1963. A Behavioral Theory of the Firm, Englewood Cliffs, NJ: Prentice Hall, Inc.

Davis, J. P., Eisenhardt, K. M., and Bingham, C. B. 2007. “Developing Theory Through Simulation Methods,” Academy of Management Review (32), pp. 480-499.

Eaton, B., Elaluf-Calderwood, S., Sorensen, C., and Yoo, Y. 2015. "Distributed Tuning of Boundary Resources: The Case of Apple's iOS Service System," MIS Quarterly (39), pp. 217-243.

Eisenmann, T., Parker, G., and Van Alstyne, M. 2011. “Platform Envelopment,” Strategic Management Journal (32), pp. 1270-1285.

Epstein, J. M. 2006. Generative Social Science: Studies in Agent-Based Computational Modeling, Princeton, NJ: Princeton University Press.

Epstein, J. M., and Axtell, R. 1996. Growing Artificial Societies: Social Science from the Bottom Up, Cambridge, MA: MIT Press.

Ethiraj, S. K., and Levinthal, D. 2004. “Modularity and Innovation in Complex Systems,” Management Science (50), pp. 159-173.

Firstjob. 2018. “Firstjob App” (https://www.appsterhq.com/ourwork/firstjob/).

Fleming, L. 2001. “Recombinant Uncertainty in Technological Search,” Management Science (47), pp. 117-132.

Fleming, L., and Sorenson, O. 2001. “Technology as a Complex Adaptive System: Evidence from Patent Data,” Research Policy (30:7), pp. 1019-1039.

Foss, N. J., and Weber, L. 2016. “Moving Opportunism to the Back Seat: Bounded Rationality, Costly Conflict, and Hierarchical Forms,” Academy of Management Review (41), pp. 61-79.

Frenken, K. 2006. “A Fitness Landscape Approach to Technological Complexity, Modularity, and Vertical Disintegration,” Structural Change and Economic Dynamics (17:3), pp. 288-305.

Gamba, A., and Fusari, N. 2009. “Valuing Modularity as a Real Option,” Management Science (55), pp. 1877-1896.

Ganco, M., and Hoetker, G. 2009. “NK Modeling Methodology in Strategy Literature: Bounded Search on Rugged Landscapes,” in Research Methodology in Strategy and Management, D. D. Bergh and J. K. Ketchen (eds.), Bingley, UK: Emerald Group Publishing Limited, pp. 237-268.

Gartner. 2014. “Gartner Says Less Than 0.01 Percent of Consumer Mobile Apps Will Be Considered a Financial Success by Their Developers Through 2018,” Gartner Group, Stamford, CT (https://www.gartner.com/newsroom/id/2648515, accessed May 25, 2018).

Gawer, A. 2014. “Bridging Differing Perspectives on Technological Platforms: Toward an Integrative Framework,” Research Policy (43:7), pp. 1239-1249.

Gawer, A., and Cusumano, M. A. 2002. Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation, Boston: Harvard Business School Press.

Gesmann, M. 2014. “Managing R Package Dependencies,” R-Bloggers, September 23 (https://www.r-bloggers.com/managing-r-package-dependencies/, accessed June 4, 2018).

Ghazawneh, A., and Henfridsson, O. 2010. “Governing Third-Party Development through Platform Boundary Resources,” in Proceedings of the 31 $^{st}$ International Conference on Information Systems, St. Louis, MO.

Ghazawneh, A., and Henfridsson, O. 2012. “Balancing Platform Control and External Contribution in Third-Party Development: The Boundary Resources Model,” Information Systems Journal (23:2), pp. 173-192.

Gigerenzer, G., and Goldstein, D. G. 1996. “Reasoning the Fast and Frugal Way: Models of Bounded Rationality,” Psychological Review (103:4), pp. 650-669.

Gilette, F. 2011. “The Rise and Inglorious Fall of Myspace,” Bloomberg.Com (https://www.bloomberg.com/news/articles/2011-06-22/the-rise-and-inglorious-fall-of-myspace).

Greve, H. R. 2002. “Sticky Aspirations: Organization Time Perspective and Competitiveness,” Organization Science (13:1), pp. 1-17.

Groen, A. 2013. “Why Game Developers Are Flocking to Sony and Fleeing From Microsoft,” Wired (https://www.wired.com/2013/04/sony-indies/).

Guglielmo, C. 2014. “Mobile Apps Won’t Lead to Riches For Most Developers,” Forbes (https://www.forbes.com/sites/connieguglielmo/2014/01/13/mobile-apps-may-not-pave-the-way-to-developer-riches-sales-average-less-than-1250-a-day/, accessed May 25, 2018).

Hamming, R. W. 1950. “Error Detecting and Error Correcting Codes,” Bell System Technical Journal (26), pp. 147-160.

Katz, M. L., and Shapiro, C. 1994. “Systems Competition and Network Effects,” Journal of Economic Perspectives (8:2), pp. 93-115.

Kauffman, S. A. 1993. The Origins of Order: Self-Organization and Selection in Evolution, Oxford, UK: Oxford University Press.

Kauffman, S. A., and Levin, S. 1987. “Towards a General Theory of Adaptive Walks on Rugged Landscapes,” Journal of Theoretical Biology (128:1), pp. 11-45.

Kauffman, S. A., and Weinberger, E. D. 1989. “The NK Model of Rugged Fitness Landscapes and its Application to Maturation of the Immune Response,” Journal of Theoretical Biology (141:2), pp. 211-245.

Labianca, G., Fairbank, J. F., Andrevski, G., and Parzen, M. 2009. "Striving toward the Future: Aspiration—Performance Discrepancies and Planned Organizational Change," Strategic Organization (7:4), pp. 433-466.

Law, A. M. 1991. Simulation Modeling and Analysis, New York: McGraw-Hill.

Lee, D. 2010. “Apple Boss Explains Ban on Flash,” BBC News, Technology Section (https://www.bbc.com/news/10092298).

Levine, S. S., and Prietula, M. J. 2013. “Open Collaboration for Innovation: Principles and Performance,” Organization Science (25:5), pp. 1414-1433.

Levinthal, D. 1997. “Adaptation on Rugged Landscapes,” Management Science (43:7), pp. 934-950.

Levinthal, D., and March, J. G. 1981. “A Model of Adaptive Organizational Search,” Journal of Economic Behavior & Organization (2:4), pp. 307-333.

March, J. G. 1981. “Variable Risk Preferences and Adaptive Aspirations,” Journal of Economic Behavior and Organization (9:1), pp. 5-24.

March, J. G. 1991. “Exploration and Exploitation in Organizational Learning,” Organization Science (2:1), pp. 71-87.

March, J. G., and Shapira, Z. 1992. “Variable Risk Preferences and the Focus of Attention,” Psychological Review (99:1), pp. 172-183.

McCarthy, B. 2016. “Top 10 Most Popular AppExchange Apps,” Salesforce Ben, August 15. (http://www.salesforceben.com/top-10-popular-appexchange-apps/, accessed June 6, 2018).

Muncy, J. 2018. “Xbox Is Losing the Console War—but That’s a Good Thing,” Wired (https://www.wired.com/story/xbox-console-wars/).

Nan, N., and Tanriverdi, H. 2017. “Unifying the Role of IT in Hyperturbulence and Competitive Advantage via a Multilevel Perspective of IS Strategy,” MIS Quarterly (41:3), pp. 937-958. nCino. 2018. “nCino About” (https://www.ncino.com/about).

nCino. 2018. “nCino About” (https://www.ncino.com/about).

Parker, G., and Van Alstyne, M. 2018. “Innovation, Openness, and Platform Control,” Management Science (64:7), pp. 3015-3032.

Parker, G. G., Van Alstyne, M., and Choudary, S. P. 2016. Platform Revolution, New York: W. W. Norton & Company.

Pil, F. K., and Cohen, S. K. 2006. “Modularity: Implications for Imitation, Innovation, and Sustained Advantage,” The Academy of Management Review (31:4), pp. 995-1011.

Qiu, Y., Gopal, A., and Hann, I-H. 2011. “Synthesizing Professional and Market Logics: A Study of Independent iOS App Entrepreneurs,” in Proceedings of the 32 $^{nd}$ International Conference on Information Systems, Shanghai, China.

Richie, R. 2016. “What No Indie Developer Wants to Hear about the App Store,” IMore, March 11 (https://www.imore.com/appstore-disconnect, accessed June 6, 2018).

Rivkin, J. W. 2000. “Imitation of Complex Strategies,” Management Science (46:6), pp. 824-844.

Rivkin, J. W., and Siggelkow, N. 2007. “Patterned Interactions in Complex Systems: Implications for Exploration,” Management Science (53:7), pp. 1068-1085.

Rochet, J. C., and Tirole, J. 2003. “Platform Competition in Two-Sided Markets,” Journal of the European Economic Association (1:4), pp. 990-1029.

Sanchez, R., and Mahoney, J. T. 1996. “Modularity, Flexibility, and Knowledge Management in Product and Organization Design,” Strategic Management Journal (17: Winter Special Issue), pp. 63-76.

Schilling, M. A. 2000. “Toward a General Modular Systems Theory and Its Application to Interfirm Product Modularity,” The Academy of Management Review (25:2), pp. 312-334.

Schwartz, B., Ward, A., Monterosso, J., Lyubomirsky, S., White, K., and Lehman, D. R. 2002. “Maximizing Versus Satisficing: Happiness Is a Matter of Choice,” Journal of Personality and Social Psychology (83:5), pp. 1178-1197.

Shinkle, G. A. 2012. “Organizational Aspirations, Reference Points, and Goals: Building on the Past and Aiming for the Future,” Journal of Management (38:1), pp. 415-455.

Shinkle, G. A., and Kriauciunas, A. P. 2012. “The Impact of Current and Founding Institutions on Strength of Competitive Aspirations in Transition Economies,” Strategic Management Journal (33:4), pp. 448-458.

Simon, H. A. 1955. “A Behavioral Model of Rational Choice,” The Quarterly Journal of Economics (69:1), pp. 99-118.

Simon, H. A. 1962. “The Architecture of Complexity,” Proceedings of the American Philosophical Society (106), pp. 467-482.

Simon, H. A. 1973. “Organizational Man: Rational or Self-Actualizing?,” Public Administration Review (33), pp. 346-353.

Simon, H. A., Dantzig, G. B., Hogarth, R., Plott, C. R., Raiffa, H., Schelling, T. C., Shepsle, K. A., Thaler, R., Tversky, A., and Winter, S. 1987. “Decision Making and Problem Solving,” Interfaces (17:5), pp. 11-31.

Snappii. 2018. “Start Making Your Mobile Business App Today” (https://www.snappii.com/create-mobile-apps-without-coding-with-snappii).

Taeuscher, K., and Kietzmann, J. H. 2017. “Learning from Failures in the Sharing Economy,” MIS Quarterly Executive (16:4), pp. 253-263.

Tee, R., and Woodard, C. J. 2013. “Architectural Control and Value Migration in Layered Ecosystems: The Case of Open-Source Cloud Management Platforms,” paper presented at the 35 $^{th}$ DRUID Celebration Conference 2013, Barcelona, June 17-19.

Tilson, D., Lyytinen, K., and Sørensen, C. 2010. “Research Commentary—Digital Infrastructures: The Missing IS Research Agenda,” Information Systems Research (21:4), pp. 748-759.

Tiwana, A. 2008. “Does Technological Modularity Substitute for Control? A Study of Alliance Performance in Software Outsourcing,” Strategic Management Journal (29), pp. 769-780.

Tiwana, A. 2014a. “Evolving an App,” Chapter 11 in Platform Ecosystems: Aligning Architecture, Governance, and Strategy, Boston: Morgan Kaufmann, pp. 247-268.

Tiwana, A. 2014b. “Real Options Thinking in Ecosystem Evolution,” Chapter 8 in Platform Ecosystems: Aligning Architecture, Governance, and Strategy, Boston: Morgan Kaufmann, pp. 179-190.

Tiwana, A. 2015. “Evolutionary Competition in Platform Ecosystems,” Information Systems Research (26:2), pp. 266-281.

Tiwana, A., Konsynski, B., and Bush, A. 2010. “Platform Evolution: Coevolution of Platform Architecture, Governance, and Environmental Dynamics,” Information Systems Research (21:4), pp. 675-687.

Ulrich, K. 1995. “The Role of Product Architecture in the Manufacturing Firm,” Research Policy (24:3), pp. 419-440.

Um, S., Yoo, Y., Wattal, S., Kulathinal, R., and Zhang, B. 2013. "The Architecture of Generativity in a Digital Ecosystem: A Network Biology Perspective," in Proceedings of the $34^{th}$ International Conference in Information Systems, Orlando, FL.

van Alstyne, M. W., Parker, G. G., and Choudary, S. P. 2016. “6 Reasons Platforms Fail,” Harvard Business Review (https://hbr.org/2016/03/6-reasons-platforms-fail, accessed May 25, 2018).

von Hippel, E. 2005. Democratizing Innovation, Cambridge, MA: MIT Press.

Vision Mobile. 2015. “Developer Economics: The State of the Developer Nation Q1 2015,” London: Vision Mobile Ltd. (https://www.developereconomics.com/reports/developer-economics-q1-2015-state-developer-nation).

Wareham, J., Fox, P. B., and Cano Giner, J. L. 2014. “Technology Ecosystem Governance,” Organization Science (25:4), pp. 1195-1215.

Warren, C. 2011. “When & How You Should Update Your Mobile App,” September 11 (https://mashable.com/2011/09/22/mobile-app-update/#fHJvf11HTuqZ).

Weissman, C.D., and Broboski, S. 2009. “The Design of the Force.Com Multitenant Internet Application Development Platform,” in Proceedings of the 2009 ACM SIGMOD International Conference on Management of Data, New York: ACM, pp. 889-896.

Woodard, C. J. 2008. “Architectural Control Points,” in Proceedings of the 3 $^{rd}$ International Conference on Design Science Research in Information Systems and Technology, Atlanta.

Woodard, C. J., Ramasubbu, N., Tschang, F. T., and Samba-murthy, V. 2013. “Design Capital and Design Moves: The Logic of Digital Business Strategy,” MIS Quarterly (37:2), pp. 537-564.

Wright, S. 1932. “The Roles of Mutation, Inbreeding, Cross-breeding and Selection in Evolution,” in Proceedings of the VI International Congress on Genetics (1), pp. 356-366. (http://www.blackwellpublishing.com/ridley/classictexts/wright.pdf).

Yin, P.-L., Davis, J. P., and Muzyrya, Y. 2014. “Entrepreneurial Innovation: Killer Apps in the iPhone Ecosystem,” American Economic Review (104:5), pp. 255-259.

Yoo, Y., Boland, R. J., Lyytinen, K., and Majchrzak, A. 2012. "Organizing for Innovation in the Digitized World," Organization Science (23), pp. 1398-1408.

Yoo, Y., Henfridsson, O., and Lyytinen, K. 2010. “Research Commentary—The New Organizing Logic of Digital Innovation: An Agenda for Information Systems Research,” Information Systems Research (21:4), pp. 724-735.

Yoo, Y., Lyytinen, K. J., Boland, R. J., and Berente, N. 2010. “The Next Wave of Digital Innovation: Opportunities and Challenges: A Report on the Research Workshop ‘Digital Challenges in Innovation Research’” (http://dx.doi.org/10.2139/ssrn.1622170).

## About the Authors

Sabine Brunswicker is a professor of Digital Innovation and director of the Research Center for Open Digital Innovation at Purdue University. Her interdisciplinary research work has been funded by NSF, NIH, the European Commission, and various industry donors (e.g., Red Hat, Accenture). She has published in top academic journals and conferences bridging social sciences and information technology and sciences, including Scientometrics, Journal of the Association for Information Science and Technology, Journal of Small Business Management, and MIS Quarterly. Sabine serves on the editorial board of PLoS ONE. A user-inspired researcher, she frequently engages with industry partners, and acts as advisor and keynote speaker for policy makers and thought leaders.

Esteve Almirall is an associate professor of Operations, Innovation and Data Science at ESADE Business School, Ramon Llull University, Barcelona. He holds a Ph.D. in Management Science, a M.Res. in Artificial Intelligence, an MBA, and a degree in Computer Engineering. His research appeared in leading journals such as Academy of Management Review, MIS Quarterly, Communications of the ACM, and Harvard Business Review. He has directed numerous European projects and serves as a reviewer, expert, and evaluator for the European Commission. Before joining academia, he worked in the industry for over 20 years as a CIO-CTO of a Spanish bank, in the IT industry, and as a with several startups. Esteve is a well-known keynote speaker and does advisory work for private and public organizations on innovation, smart cities and artificial intelligence.

Ann Majchrzak is the Associates of USC Chair of Business Administration and Digital Innovation for the Marshall School of Business at the University of Southern California. She is a Senior Scholar and Fellow of the Association for Information Systems. Ann has been a member of three National Research Council committees. She is the longest running senior editor for Organization Science. She has published in top academic (Management Science, Organization Science, Information Systems Research, MIS Quarterly) as well as top practitioner (Harvard Business Review, Sloan Management Review, California Management Review) journals.

# OPTIMIZING AND SATISFICING: THE INTERPLAY BETWEEN PLATFORM ARCHITECTURE AND PRODUCERS' DESIGN STRATEGIES FOR PLATFORM PERFORMANCE

Sabine Brunswicker

Research Center for Open Digital Innovation, Purdue University, 516 Northwestern Avenue, West Lafayette, IN 49706 U.S.A. {sbrunswi@purdue.edu}

Esteve Almirall

ESADE Business School, Universitat Ramon Llull, Av. Toree Blanca 59,

SantCugat-Barcelona, SPAIN {esteve.almirall@esade.edu}

Ann Majchrzak
Marshall School of Business, University of Southern California,
Los Angeles, CA 90089 U.S.A. {amajchrzak@usc.edu}

## Appendix A

## Summary of Robustness Checks

We performed a series of simulations that were examining the robustness of our model specification (Davis et al. 2007). In particular, we explored whether the results would change if we modified the search heuristic h (see Table 3 in the main document) and the design moves (hill-climbing and long-jump) that define how agents search the design space when combining design elements into apps. We implemented three major robustness analyses: First, we examined the robustness of our binary representation of long-jump and hill-climbing as two dichotomous search moves, modeled in accordance with Levinthal (1997). To do so, we explored the effects of an alternative continuous representation following Billinger et al. (2013). Second, we examined the robustness of our assumption about the average amount of resources for long-jumps (R) that each agent has available when moving through the iterative search process (Billinger et al. 2013; March 1981; Rivkin 2000). Third, we also explored whether a simple categorical function to model failure-induced jumps is appropriate given alternative probabilistic models suggested in the literature on search and decision making (Greve 1998, 2002; Hu et al. 2011; Lant 1992). We will briefly report the results of these three robustness checks.

## Robustness Check 1: Alternative Modeling of Local Versus Distant Search

In our simulations reported in the main document, we modeled hill-climbing and long-jumps as dichotomous facets of local versus distant search, following the line of research of Levinthal (1997). Our agents randomly change a design element in their design vector $d = <d1, \ldots, d16>$ . The type of search move (hill-climbing or long-jump) defines how many decision variables they change. If they are hill-climbing, they change only one element, but if they engage in a long-jump, they randomly change several (up to six) design elements in their vector. We labeled this as a “greedy” model in our simulation model, and also in the code itself. As an alternative approach, we implemented and tested Billinger et al.’s (2013) approach to modeling different facets of search. In this alternative approach, the agents gradually adjust their search distance starting with an initial search distance of three that is then adjusted according to their success. We labeled this modeling as adaptive” (and the code respectively). In essence, this implies that if agents could find a higher position, they became more conservative and gradually reduced the search distance over time. On the contrary, if agents are unsuccessful, they became more risk-taking by increasing their search distance gradually. Thus, our agents rapidly take many long-jumps at high levels of coupling. The use of what we call adaptive in our code resulted in a higher number of iterations, and slightly less pronounced results. However, the general insights gained from our simulations remain the same. Only minor differences could be detected. We judged our results as robust after completing these robustness checks.

## Robustness Check 2: Varying the Level of Resources for Long-Jumps

The second aspect that we explored was resources for long-jumps available to our agents (March and Shapira 1992). Indeed, prior studies extending Levinthal's the NK model highlight that bold long-jumps are limited by the resources available to the agent (Billinger et al. 2013; Rivkin 2000). Further, this theoretical assumption is also consistent with empirical insights. Major design moves are resource intensive, and accrue technological debt (Gilette 2011; Woodard et al. 2013). Developing a radically new app takes time, money, and energy, and such resources deplete. Thus, we explored different scenarios by limiting the number of long-jumps available to each agent from 25, 50, 100, to 250. Obviously more resources for long-jumps altered the results significantly, particularly at the lower end of the spectrum: If resources were really low (10 or 25 jumps as average), agents quickly suffered from too little resources to engage in long-jumps even if they aspired to jump because they were below their competitive aspiration. We learned that a minimum of 50 long-jumps is necessary to allow developers to cope with higher levels of coupling. If the amount of resources available is really high (e.g., 500 long-jumps as average), the differences in the effect of producers' design strategies (optimizing versus satisficing) unfold in an even more pronounced way. The downside of optimizing is even more obvious: platforms with optimizing producers perform significantly lower, and the outcome is even more skewed such that only a few stars are clearly separated from the rest of the population. However, general trends and transition points were similar, and we learned that, on platforms where “extra” effort and major design moves are needed (tight coupling), very high levels of resources for risk-taking long-jumps can be very detrimental.

## Robustness Check 3: Probabilistic Function for Failure-Induced Long-Jumps

Finally, we also explored the impact of a probabilistic model for failure-induced long-jumps as a function of one agent's distance from the performance target associated with his competitive aspiration. Prior research on adaptive aspirations has concluded that both individuals and organizations often follow a simple heuristic when judging their performance as failure, and taking distant moves depending on their relative standing. They encode any value above their aspiration as a success and thus hill-climb (and the opposite for any value below as failure, triggering long-jumps). However, following prior work by Greve (2002) and other recent studies on adaptive aspirations (Hu et al. 2011; Lant 1992), we also pursued a probabilistic representation of the rule. We provided a higher probability for an agent making long-jumps if the agent is farther away from the agent's competitive aspiration (which can be either an optimizing or a satisficing one). In our probabilistic modeling, the ones that are separated from their aspiration by the greatest distance had a probability of 0.9 to engage in a long-jump; the ones that were closer to their aspiration had only 0.1 probability of taking a long-jump. The probability was linearly distributed between 0.1 and 0.9, in accordance with the constant-slope response model proposed by Greve (1998). The results obtained in the experiments with a probabilistic modeling approach were completely consistent with the ones obtained when agents follow a categorical decision rule.

## Appendix B

## Note on Simulation Length

Our simulation ends when all the agents exhausted their resources available for long-jumps (the maximum number of long-jumps available to them) or when no agent changes the position after a full iteration. The length of the simulations varies depending on K, the tightness of coupling of the elements in the platform, and other treatment conditions. For the reported number of simulations (based on an average maximum number of long-jumps of 100), the number of design iterations ranged from 6 to 500.

In Figure B1, we provide an overview of the length of the simulations for different levels of coupling (K), no constraint (C = 0), and speed of adjustment of S = 1 and S = 10. The length of the simulation increases as K increases. Further, with a higher S, we see that the number of iterations decreases as K increases. If we increase C, the simulations also become shorter. The average number of iterations was 311 across all simulation experiments. Thus, on average the simulations ended before the maximum length of 500 iterations because agents had exploited their resources for long-jumps or had settled on the design with the highest fitness.

Coupling K 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15  
![](/api/attachments/YH3Z4EDE/fulltext/images/7dfc190c995cffd24c9edae318c9b1faf82cee182b4f3e8d0ecce6b56d332140.jpg)

Figure B1. Overview of Length of Simulations

## Appendix C

Simulation Code

## Summary Information

Our computational model extends the traditional NK Model used by Levinthal (1997). In this pseudocode, we present the main loop of the simulations with variations.

The code is optimized for speed. Therefore, the code is as simple as possible using extremely simple logical structures. NK landscapes are mapped into a vector with a single index. Agents are depicted as a structure and also arranged as a vector of this structure. The program is written in Julia, a very fast dynamic programming language for high-performance numerical analysis.

The resulting algorithm is simple. For each simulation a landscape is created. Then 1,000 agents are randomly placed on it. For each iteration and each agent, a movement is executed. Hill-climbing is first attempted. If hill-climbing is not possible because the agent has reached a local maximum, a long-jump is executed in accordance with the behavioral rules specified for the agents. These movements are continued until the end of the simulation (when no movements are left).

```julia
Table C1. Summary of Code Structure (Pseudo-Code)

type agent
    position    # position in the NK landscape
    searchdistance  # (initially 3, only in case of adaptive jumps with changing radius
    #in accordance with Billinger et al. 2013, not used for greedy)
    maxJumps    #each agent has a max number of jumps
    numJumps    #the number of long-jumps that has done the agent so far
end

for constraints = none, 2 bits, 4 bits, 6 bits
    for aspiration point = none, medianAgent, topAgent
    for K = 0..15
    for experiments = 1..500
    landscape = create a landscape(N = 16, K, constraints)
    Deploy 1000 agents in random locations in the landscape
    while there are still changes AND there are iterations left
    find aspiration point # either top, median or none if hill-climbing
    for each agent
    # hill-climbing
    Search at distance 1 for the best design with platform constraints
    If none better found AND fitness(agent) < aspiration point
    jump by randomly changing between 2..6 bits
    agent.numJumps++
    there are changes = TRUE
    end
    end
    end
    end
    end
end
```

## The Implementation in Julia (version v 0.4)

```julia
BestStrategy.jl
include("ListStrategies.jl")
include("Fitness.jl")

function BestStrategy(strategy,ag,iN)
# BestStrategy - Looks for the best possible strategy of the agents
#Return
#    newStg -> New Strategy to implement
#Inputs
#    strategy-> 1)Incremental + greedy (max fitness)
#    2)Incremental + fitter (better fitness with fitness' prob.)
#    3)Pattern selection
#    ag -> Agent to be considered
#    iN -> Range of bits to consider e.g., beginning: end (depends if some components are fixed ...)
maxFit=Fitness(ag.stg)
newStg=ag.stg
```

```julia
#if (strategy == 1 || strategy == 2 || strategy == 3 || strategy == 4 || strategy == 5)
    # Incremental + greedy
    IStg = ListStrategies(ag.stg, iN, 1)

    for IS = 1: size(IStg)[1]
    if (Fitness(IStg[IS]) > maxFit)
    newStg = IStg[IS]
    maxFit = Fitness(IStg[IS])
    end
    end
#end
return newStg
end
```

## BitGet.jl

```txt
function BitGet(i,nbit)
# BitGet Returns the value of a certain bit
# Returns:
# 0,1 -> value of the bit
# Inputs:
# i -> integer to consider
# nbit -> number of bit to consider
```

i=int32(i)

```lua
if (i & int32(2^(nbit-1))) >0
    return 1
else
    return 0
end
```

## end

## BitSet.jl

```julia
function BitSet(i,nbit,val)
# BitSet    Returns i with nbit set to val
# Returns:
# i    ->    i with nbit set to val
# Inputs:
# i    -> integer to consider
#    nbit    -> number of bit to consider
#    val    -> value to set (0,1)

i=int32(i)

if val==1
    i=i|2^(nbit-1)
else
    i=i&~(2^(nbit-1))
end

return i

end
```

## ListStrategies.jl

```julia
function ListStrategies(stgO,iN,M)
# ListStrategies From a given strategy, lists all strategies that differ in M or less components
# Returns:
#    IStg -> vector with all possible strategies
# Inputs:
#    stgO -> original strategy
#    iN -> elements (bits) to be considered in the set
#    M -> maximum number of components in which strategies can differ=1;
xM=M

IStg=zeros(Int,1)

if (xM>size(iN,1))
    xM=size(iN,1)
end

for i=1:xM
    combi=collect(combinations(iN,i))
    n_combi=size(combi,1)
    s_combi=size(combi[1],2)

    for j=1:n_combi
    n_stg=stgO
    for t=1:s_combi

    if (n_stg & 2^(combi[j,t][1]-1)) == 0
    # if (bitget(n_stg,combi[j,t])==0)
    n_stg=(n_stg | 2^(combi[j,t][1]-1))
    # n_stg=bitset(n_stg,combi[j,t]);
    else
    n_stg=(n_stg $ 2^(combi[j,t][1]-1))
    # n_stg=bitset(n_stg,combi[j,t],0);
    end
    end

    if i==1 && j==1    # first time
    IStg[1]=n_stg
    else
    push!(IStg,n_stg)
    end
    end
end

return IStg
end
```

## CreaLandscape.jl

```julia
function CreaLandscape(N,K)
# CreaLandscape Creates a landscape N-K (see Kauffman)
# Returns:
# m_cs->max interactions
# CS -> global variable that contains vector dependencies
# CV -> global variable that contains random number used to build the
# landscape
# Inputs:
# N -> number of different components of the Strategy
# K -> number of components of which every single component depends on

#global landscape
#global cs
#global maxLand

dosaN=2^N
dosaK1=2^(K+1)

landscape=zeros(dosaN,1)

cs=zeros(Int,N,K+1)
cvx=rand(dosaK1,N)

#Random with repetition
for i=[1:N]
    tmp=[1:i-1,i+1:N]
    tmp1=randperm(N-1)
    cs[i,:]=[i tmp[tmp1[1:K]]']
## cs(i,:)=sort(cs(i,:))
end

maxval=0
minval=9

for i=[0:(dosaN-1)]
    valor=0;
    for j=[1:N]
    ind=0;
    for p=[1:(K+1)]
#
    pm=int32(2^cs[j,p])
#
    println(i," ",pm," ",i&pm," ",ind|pm)
    if (i & int32(2^(cs[j,p]-1))) >0
    ind=(ind | 2^(p-1))
    end
#
    if (bitget(i,cs(j,p))==1)
#
    ind=bitset(ind,p,1);
#
    end
    end
    valor=valor+cvx[ind+1,j]
    end

landscape[i+1]=valor/N
if (landscape[i+1]>maxval)
    maxval=landscape[i+1]
```

```julia
maxLand=i+1
end
if (landscape[i+1]<minval)
    minval=landscape[i+1]
end
end

dif=maxval-minval
landscape=(landscape.-minval)/dif

return landscape
end

Fitness.jl

function Fitness(stg)
# Fitness Returns the fitness of an strategy
# Returns:
# fit -> fitness corresponding to the strategy of the agent
# corresponds to the strategy of the agent + 1 into the landscape
# Inputs:
# stg -> strategy of the agent

global landscape

fit=landscape[stg+1]

return fit

end
```

```julia
Simula.jl
include("BestStrategy.jl")
include("Fitness.jl")
include("BitGet.jl")
include("BitSet.jl")

#----
function Simula(strategy,ag,aex...)
# Simula    Performs a simulation depending on the Strategy
#    -> strategy=1 - Hill-climbing
#    -> strategy=2 - Hill-climbing with info about avg Fitness of the Landscape
# Returns:
#    ag    -> structure of agents
#    bestCases   -> final benchmark
# Inputs:
#    strategy -> 0= Hill-climbing - used as a baseline
#    1= Hill-climbing with restricted bits
#    2= Hill-climbing with explorers using max fitness found w restricted bits
#    3= Hill-climbing with explorers using avg fitness found w restricted bits
#    4= Hill-climbing using Best Cases from explorers
#    5= Hill-climbing from Best Cases extracted from the agents themselves
#    ag    -> structure of agents
#    aex    -> structure of the explorers or number of array of agents to consider for Best Case

#    required global variables
#    landscape   -> the vector representing the landscape
#    N    -> number of different components of the Strategy
#    K    -> number of components of which every single component depends on

global landscape
global N, K

global nBestCases

global _fixbits, _freebits,_fixval
global _dpivot

dosaN=2^N
dosaK1=2^(K+1)

nagents=size(ag,1)

#counting iterations
_niter=0

if strategy==1 || strategy==0
    # Do Hill-climbing
    canvi=true

    while canvi
    canvi=false
    for i=1:nagents
    if strategy==0
    newStg=BestStrategy(strategy, ag[i],[1:N])
    else
    newStg=BestStrategy(strategy, ag[i], _freebits)
```

```julia
end
    if newStg != ag[i].stg
    ag[i].stg = newStg
    canvi = true
    end
    end
    _niter = _niter + 1
    end
    return (ag, _niter)
end

if (strategy == 2 || strategy == 3 || strategy == 4)
    # Do Hill-climbing with Explorers with the max fitness found by the explorers
    ex = aex[1]
    e = size(ex, 1)
    if (strategy == 2 || strategy == 3)
    avgEx = 0
    for i = 1: e
    if strategy == 2
    if Fitness(ex[i].stg) > avgEx
    avgEx = Fitness(ex[i].stg)
    end
    else
    avgEx = avgEx + Fitness(ex[i].stg)
    end
    end
    if strategy == 3
    avgEx = avgEx / e
    end
    # @printf("avgEx %4f\n", avgEx)
    else
    # Select the best cases found by explorers
    bestCases = zeros(e)
    for i = 1: e
    bestCases[i] = Fitness(ex[i].stg)
    end
    bestCases = sort(bestCases, rev=true)
    end

canvi = true

while canvi
    canvi = false
    if _dpivot > 0
    # find minimum fitness
    _minfit = 9.0
    for i = 1:nagents
    if Fitness(ag[i].stg) < _minfit
    _minfit = Fitness(ag[i].stg)
    end
    end
    end
    for i = 1:nagents
    if ag[i].nPivot < ag[i].mPivot
    newStg = BestStrategy(strategy, ag[i], _freebits)
    if newStg != ag[i].stg
    ag[i].stg = newStg
    canvi = true
```

```julia
else
# @printf("agent %2d tBCase %2d nPivot %2d mPivot %2d \n",i,ag[i].tBCase,ag[i].nPivot,ag[i].mPivot)
if ((strategy== 2 || strategy==3) && Fitness(newStg)<avgEx) ||
( strategy==4 && Fitness(newStg)<bestCases[ag[i].tBCase] )
#
#@printf("Old strategy %7f New strategy %7f",ag[i].stg,newStg)
#
#@printf("Aixo no hauria de passar Fitness(newStg) %7f avgEx %7f dif %7f
\n",Fitness(newStg),avgEx,avgEx-Fitness(newStg))
# Jump
_jump=false
if _dpivot==0
    #greedy
    _jump=true
else
    #only 1 proportional negative is considered
    if (strategy==2 || strategy ==3)
    _p=(Fitness(ag[i].stg)-_minfit)/(avgEx-_minfit)
    else
    _p=(Fitness(ag[i].stg)-_minfit)/(bestCases[ag[i].tBCase]-_minfit)
    end
    _p=1-_p
    if rand()<=_p
    _jump=true
    end
end
if _jump==true
    btC=int(rand()*4)+2  #bt 2..6 bits
    for j=1:btC
    bC=int(rand()*length(_freebits)-1))+1
    if BitGet(ag[i].stg,_freebits[bC])==0  # Flip
    ag[i].stg=BitSet(ag[i].stg,_freebits[bC],1)
    else
    ag[i].stg=BitSet(ag[i].stg,_freebits[bC],0)
    end
    end
    canvi=true
    ag[i].nPivot=ag[i].nPivot+1
end
end
end
end
end
End
if (strategy==5)
    # Do Hill-climbing using Best Cases crowdsourced from the agents themselves
    ex=aex[1]
    e=size(ex,1)
    bestCases=zeros(e)
    for i=1:e
    bestCases[i]=Fitness(ag[ex[i]].stg)
    end
    bestCases=sort(bestCases,rev=true)
```

for i=1:length(bestCases)

```julia
# @printf("Best Case %2d %2.5f \n",i,bestCases[i])
# end
avgF=0
for i=1:nagents
    avgF=avgF+Fitness(ag[i].stg)
end
avgF=avgF/nagents
# @printf("Init %3d Average fitness of Best Cases %2.5f Agents %2.5f\n",e,mean(bestCases[1:5]),avgF)
canvi=true
njump=0
while canvi
    canvi=false
    if _dpivot>0
    #find minimum fitness
    _minfit=9.0
    for i=1:nagents
    if Fitness(ag[i].stg)<_minfit
    _minfit=Fitness(ag[i].stg)
    end
    end
    end
# @printf("We have _minfit \n")
for i=1:nagents
    if ag[i].nPivot<ag[i].mPivot
    newStg=BestStrategy(strategy, ag[i], _freebits)
    if newStg != ag[i].stg
    ag[i].stg=newStg
    canvi=true
    else
# @printf("Are we going to jump? Fitness(newStg) %5f bestCases[ag[i].tBCase] %5f \n",Fitness(newStg),bestCases[ag[i].tBCase])
if Fitness(newStg)<bestCases[ag[i].tBCase]
# @printf("Are we going to jump 2?\n")
# @printf("agent %2d tBCase %2d nPivot %2d mPivot %2d \n",i,ag[i].tBCase,ag[i].nPivot,ag[i].mPivot)
# @printf("Fitness(newStg) %4f bestCases[ag[i].tBCase] %4f \n",Fitness(newStg),bestCases[ag[i].tBCase])
# Jump
    _jump=false
    if _dpivot==0
    #greedy
    _jump=true
    else
    #only 1 proportional negative is considered
    _p=(Fitness(ag[i].stg)-_minfit)/(bestCases[ag[i].tBCase]-_minfit)
end
    _p=1-_p
    if rand()<=_p
    _jump=true
    end
    if _jump==true
    btC=int(rand()*4)+2 #bt 2..6 bits
    for j=1:btC
    bC=int(rand()*length(_freebits)-1))+1
    if BitGet(ag[i].stg,_freebits[bC])==0 # Flip
    ag[i].stg=BitSet(ag[i].stg,_freebits[bC],1)
```

```julia
else
    ag[i].stg=BitSet(ag[i].stg,_freebits[bC],0)
end
end
canvi=true
ag[i].nPivot=ag[i].nPivot+1
njump=njump+1
end
end
end
end
end
bestCases=zeros(e)
for i=1:e
    bestCases[i]=Fitness(ag[ex[i]].stg)
end
bestCases=sort(bestCases,rev=true)
    _niter=_niter+1
end
# avgF=0
# for i=1:nagents
#    avgF=avgF+Fitness(ag[i].stg)
# end
# avgF=avgF/nagents
# @printf(" ...    Average fitness of Best Cases %2.5f Agents %2.5f jumps %4d\n",mean(bestCases[1:5]),avgF,njump)
# for i=1:nagents
#    if Fitness(ag[i].stg)<bestCases[ag[i].tBCase]
    #tobat
#    @printf(">>> agent %3d fitness %2.4f tBCase %2d fitness Best Case %2.4f nPivots %3d maxPivots %3d \n",
#    i,Fitness(ag[i].stg),ag[i].tBCase,bestCases[ag[i].tBCase],ag[i].nPivot,ag[i].mPivot)
#    end
# end

# return ag, bestCases[1:nBestCases]
return (ag, _niter)
```

end

```julia
NKtransp.jl
# NKtransp ----
# command line inputs
# NKtransp.jl <nagents> <nexperiments> <maxTrials> <agentsRisk> <platformBits> <meanPivots> <forceAdopt>
# nagents Number of agents to be deployed in the landscape - typically 1000
# nexperiments Number of experiments to perform - bt 100..1000
# maxSearchTrials Max number of Search Trials - bt 100..1000
# agentsRisk 0-> conservative. First they exhaust all incremental opportunities then engage in long-jumps
# 1-> adaptive. They engage in adaptive behavior all the time and change their search radius.
# platformBits Number of bits fixed devoted to the platform.
# meanPivots Mean number of Pivots that agents will do. Normally distributed around meanPivots, std=1
# speed Speed of the update of the social benchmark 0-> static -1 ->every iteration n-> every n iterations
#
include("../CreaLandscape.jl")
include("../BestStrategy.jl")
include("../Fitness.jl")
include("../Simul.jl")

global landscape, N, K

global _fixbits, _freebits, _fixval

N=16
K=0

#get parameters from command line args
if size(ARGS,1)!=7
    @printf("Incorrect args in command line\n")
    @printf("NKtransp.jl <nagents> <nexperiments> <maxSearchTrials> <agentsRisk> <platformBits> <meanPivots> <speed>\n")
    exit()
end

_nag=parse(Int,ARGS[1])
_nexp=parse(Int,ARGS[2])
_mST=parse(Int,ARGS[3]) #normally 5* _nexp
_agR=parse(Int,ARGS[4])
_nfixbits=parse(Int,ARGS[5])
_mPivots=parse(Int,ARGS[6])
_speed=parse(Int,ARGS[7])

#Fix bits and assign them a value
_fixbits=randperm(N)
_freebits=_fixbits[1:end-_nfixbits]
_fixbits=_fixbits[end-_nfixbits-1):end]

_fixval=zeros(_nfixbits)
for i in 1:_nfixbits
    _fixval[i]=round(Int,rand())
end

#File name
fname="NK-" "B"string(_agR)"PI"string(_nfixbits)"Pv"string(_mPivots)"S"string(_speed)Libc.strftime("%Y-%m-%d %H:%M", time())
fOut=open(string(fname,".dat"), "w+")
```

```julia
fOutCsv=open(string(fname,".csv","w+")  
fOutCsvD=open(string(fname,"D",".csv","w+")  
write(fOutCsv,"N.Iter, #Bench, K, #Simu, Mean Fitness, Std Fitness, Search Distance\n")  
write(fOutCsvD,"N.Iter, #Bench, K, #Simu, #Agent, Fitness, Search Distance\n")  
if _nfixbits!=0  
    nB=6  
    B=[-1 0 1 2 3 4]  
else  
    nB=5  
    B=[0 1 2 3 4]  
end  
avgFit=zeros(nB,N,_nexp)  
miterF=zeros(nB,N,_mST)  
niterF=zeros(nB,N,_mST)  
type agent  
    stg::Int64  
    last::Int64  
    sD::Int32  
    mPivot::Int32  
    nPivot::Int32  
end  
ag=Array(agent,_nag)  
aFitness=zeros(_nag)  
cB=1  
for b in B  
    for K=0:N-1  
    @printf("Benchmark %2d NKtransp K=%2d \n",b,K)  
    flush(STDOUT)  
    siter=0  
    for t=1:_nexp  

    #Create a landscape  
    landscape=CreaLandscape(N,K)  

    # Put the agents on the floor  
    for i=1:_nag  
    init=round(Int,rand()*(2^N-1))  
    if b<0  

    #Baseline without restricted bits  
    ag[i]=agent(init,init,0,0,0) # 0..2^N -1  
    else  
    _ag=agent(init,init,0,0,0) # 0..2^N -1  
    for j=1:length(_fixbits)  
    _ag.stg=BitSet(_ag.stg,_fixbits[j],_fixval[j])  
    end  
    ag[i]=_ag  
    end  
    ag[i].sD=3 #initially we set the Search Distance to 3  
    ag[i].mPivot=round(Int,randn()+_mPivots)  
    ag[i].nPivot=Int(0)  
end
```

```julia
ag, _niter, iterF=Simul(ag,b,_agR,_mST,_speed)

for i=1:_mST
    miterF[cB,K+1,i] += iterF[i]
    if iterF[i] !=0
    niterF[cB,K+1,i] +=1
    end
end

for i=1:_nag
    # println(Fitness(ag[i].stg))
    aFit=Fitness(ag[i].stg)
    avgFit[cB,K+1,t]=avgFit[cB,K+1,t]+aFit
    aFitness[i]=aFit
    writecsv(fOutCsvD,[_niter b K t i aFit ag[i].sD])
end
avgFit[cB,K+1,t]=avgFit[cB,K+1,t]/_nag
siter=siter+_niter

writecsv(fOutCsv,[_niter b K t mean(aFitness) std(aFitness) mean(ag[].sD)])
# println(avgFit[K+1,t])
end
@printf("N. of iterations %3d, Fitness %4f, Search Distance %2d \n",siter/_nexp,mean(avgFit[cB,K+1,:]),mean(ag[].sD))
flush(STDOUT)
end
cB=cB+1

end

for i=1:nB
    for j=1:N
    for k=1:_mST
    if niterF[i,j,k] !=0
    miterF[i,j,k]=miterF[i,j,k]/niterF[i,j,k]
    else
    miterF[i,j,k]=0
    end
    end
    end
end

serialize(fOut,avgFit)
serialize(fOut,miterF)
close(fOut)
close(fOutCsv)
close(fOutCsvD)

#for i=1:2^16
# @printf("Landscape %5d %7.3f \n ",i,landscape[i])
#end

#@printf("Max landscape min landscape %7.3f %7.3f %7.3f\n",maximum(landscape),minimum(landscape),mean(landscape))
```

## References

Billinger, S., Stieglitz, N., and Schumacher, T. R. 2013. “Search on Rugged Landscapes: An Experimental Study,” Organization Science (25:1), pp. 93-108.

Gilette, F. 2011. “The Rise and Inglorious Fall of Myspace,” Bloomberg.Com (https://www.bloomberg.com/news/articles/2011-06-22/the-rise-and-inglorious-fall-of-myspace).

Greve, H. R. 1998. “Performance Aspirations and Risky Organizational Change,” Administrative Science Quarterly (43:1), pp. 58-86.

Greve, H. R. 2002. “Sticky Aspirations: Organization Time Perspective and Competitiveness,” Organization Science (13:1), pp. 1-17.

Hu, S., Blettner, D., and Bettis, R. A. 2011. “Adaptive Aspirations: Performance Consequences of Risk Preferences at Extremes and Alternative Reference Groups,” Strategic Management Journal (32:13), pp. 1426-1436.

Lant, T. K. 1992. “Aspiration Level Adaptation: An Empirical Exploration,” Management Science (38:5), pp. 623-644.

Levinthal, D. A. 1997. “Adaptation on Rugged Landscapes,” Management Science (43:7), pp. 934-950.

March, J. G. 1981. “Variable Risk Preferences and Adaptive Aspirations,” Journal of Economic Behavior and Organization (9:1), pp. 5-24.

Rivkin, J. W. 2000. “Imitation of Complex Strategies,” Management Science (46:4), pp. 824-844.

Woodard, C. J., Ramasubbu, N., Tschang, F. T., and Sambamurthy, V. 2013. “Design Capital and Design Moves: The Logic of Digital Business Strategy,” MIS Quarterly (37:2), pp. 537-564.
