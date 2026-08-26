---
otero_id: 27514
otero_key: "TTEUYFRE"
title: "A Multiagent Competitive Gaming Platform to Address Societal Challenges1"
authors: "Wolfgang Ketter; Markus Peters; John Collins; Alok Gupta"
year: "2016"
journal: "MIS Quarterly"
doi: "10.25300/misq/2016/40.2.09"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A MULTIAGENT COMPETITIVE GAMING PLATFORM TO ADDRESS SOCIETAL CHALLENGES<sup>1</sup>

Wolfgang Ketter and Markus Peters Rotterdam School of Management, Erasmus University, Rotterdam, NETHERLANDS {wketter@rsm.nl} {peters@rsm.nl}

John Collins Department of Computer Science and Engineering, University of Minnesota, Minneapolis, MN 55455 U.S.A. {jcollins@cs.umn.edu}

Alok Gupta Department of Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, MN 55455 U.S.A. {gupta037@umn.edu}

The shift toward sustainable electricity systems is one of the grand challenges of the 21<sup>st</sup> century. Decentralized production from renewable sources, electric mobility, and related advances are at odds with traditional power systems where central, large-scale generation of electricity follows inelastic consumer demand. Information systems innovations can enable new forms of dynamic electricity trading that leverage real-time consumption information and that use price signals to incentivize sustainable consumption behaviors. However, the best designs for these innovations, and the societal implications of different design choices, are largely unclear. We are addressing these challenges through the Power Trading Agent Competition (Power TAC), a competitive gaming platform on which numerous research groups now jointly devise, benchmark, and improve IS-based solutions to the sustainable electricity challenge. Based on the Power TAC community’s results, we give preliminary empirical evidence for the efficacy of competitive gaming platforms, and for the community’s contributions toward resolving the sustainable electricity challenge.

Keywords: Competitive benchmarking, design science, energy informatics, energy information systems, competitive intelligent agents, research competitions, smart grids, sustainability, virtual worlds

## Introduction

Over the past decades, electricity has revolutionized the way we live. In the United States, more than 40 percent of all energy is supplied through the electric grid (U.S. Energy Information Administration 2013a, 2013b), and digitization has spurred substantial innovation and economic growth (Gartner Group 2013). Most American electricity is generated in large, central power plants from fossil (68%) or nuclear (20%) fuels that have been heavily criticized for their environmental impact (U.S. Energy Information Administration 2013a). These challenges are even greater in the less developed economies. India generates close to 80 percent of its electricity from fossil fuels, more than a fifth of which is lost to its unreliable network infrastructure (Worldbank 2013). These developments make the electric grid and its complex web of interacting public and private institutions an infrastructure of tremendous social importance, in which any intervention must be designed and evaluated with great care (Borenstein 2002).

For example, generation from renewable sources could reduce carbon emission levels, but renewables are difficult to integrate when consumers have little information about their electricity usage and few incentives to invest in smart appliances that adapt to the changing availability of wind and sun (Joskow and Tirole 2006). Technologies for mitigating these issues—real-time metering, bidirectional communication, home automation, etc.—have long been commercially available. But intelligently managing the intricate interplay among the need for sustainability, individual behaviors, and physical constraints remains difficult in complex modern power systems with millions of self-interested participants.<sup>2</sup> Information Systems (IS) innovations can play a decisive role in this situation by influencing participants’ environmental beliefs through information, by coordinating and optimizing electricity networks, and by transforming the current centralized approach to electricity provisioning (Bichler et al. 2010; Melville 2010; Watson et al. 2010).

One such innovation is the introduction of electricity broker agents (EBAs), software agents (Collins, Ketter, and Gini 2009, 2010) that dynamically intermediate between retail customers and large-scale generators of electricity, either autonomously or in support of a human decision-maker.<sup>3</sup> EBAs fulfill many of the same functions as current electricity retailers, but their IS-based nature allows them to provide electricity system participants with much more fine-grained information and economic incentives than what is currently feasible (Ketter et al. 2015; Ramchurn et al. 2012). For example, EBAs are capable of offering electric vehicle owners temporarily reduced charging rates in exchange for the option to use their batteries as local buffers against solar production drops when cloud covers are erratic (Valogianni et al. 2014) or EBAs that turn fleets of electric vehicles into virtual power plants that help balance the grid and overcome inefficiencies (Kahlen et al. 2014). Through such targeted use of information, EBAs encourage more efficient use of existing infrastructures, and they enable behaviorally driven change (Watson et al. 2010).

To realize this idea, we need a principled way of designing and evaluating EBAs and the market mechanisms they operate under in complex power systems. Researchers must provide compelling evidence for the benefits and stability of EBA candidate designs before deploying them into real power systems. However, three characteristics of the sustainable electricity challenge in particular, and of other societal challenges more generally, make it difficult to provide such evidence:

Scope: Understanding, modeling, and validating all pertinent aspects of the challenge before embarking on their actual research exceeds the (intellectual and personnel) capacity of most research groups. Research on EBAs, for example, requires expertise in power systems, customer behavior, information technology, economics, and several other disciplines. Bringing together these experts and coordinating their work is a departure from the hitherto successful “singleinvestigator, social-science-driven model of research” (Nunamaker and Briggs 2011, p. 2). This departure is needed because “a solo researcher, even working with one or two others, could not resolve [these challenges] in a career” (Nunamaker and Briggs 2011, p. 2).

Vastness: Many different candidate designs are needed to obtain confidence that the space of possible solutions has been thoroughly explored. For example, only through benchmarking against a broad range of other designs can the robustness of a particular EBA design in competitive markets be demonstrated.

Complexity: In complex systems like electric grids, the performance effects of interactions often dominate the performance of individual actors studied in isolation (Hanusch and Pyka 2007). To fully understand the consequences of EBA deployments, for example, researchers must evaluate their EBAs at the system level where interaction effects with other market participants can be observed.

Our main research question is: How can competitive simulation games be used to design and evaluate interventions in societal challenges such as making our electric power systems more sustainable? We aim to answer this question through a novel competitive research approach called competitive benchmarking (CB), consisting of four elements: A community-developed competitive simulation (CDCS) platform that accurately models selected facets of the challenge including one or more market mechanisms in which a set of competitive intelligent agents (CIAs) can interact with each other; a series of tournaments through which researchers jointly design, benchmark, and improve their CIAs and the market mechanisms within which they operate; an open repository of research artifacts and data, including the CDCS platform, executable copies of CIAs contributed by various research groups, and complete data sets from prior tournaments.

We describe in some detail a particular instance of our approach called the Power Trading Agent Competition (Power TAC) (Collins and Ketter 2014; Ketter et al. 2015) to address the sustainable electricity challenge through innovative IS designs. Power TAC is an instance of a smart market (Bichler et al. 2010) for the sustainable electricity sector and includes a CDCS platform, a set of CIAs (called EBAs in the Power TAC context), a data repository, and a growing shared set of analysis tools. Based on the data generated by the Power TAC community, we provide preliminary empirical evidence of Power TAC’s efficacy as a research platform, and of the benefits of competitively designed EBAs toward providing affordable, reliable, and sustainable energy for the 21<sup>st</sup> century (Amin and Wollenberg 2005).

## The Power Trading Agent Competition

The Power Trading Agent Competition (Ketter, Collins and Reddy 2013; Ketter et al. 2015; Ketter, Peters, and Collins 2013; see also www.powertac.org) was first initiated in 2009, when a global community of researchers realized that the three principal challenges outlined in the introduction (scope, vastness, and complexity) require new forms of research and coordination.

Scope and complexity, on the one hand, speak in favor of one community-built problem definition that is created, peerreviewed, and maintained by a multitude of experts in a scalable, distributed fashion. Such a peer-reviewed problem definition facilitates early coordination, promotes research results that are comparable after the fact, and leads to a greater confidence that the community’s efforts flow into the highest-value research questions. Vastness, on the other hand, speaks in favor of intense, competitive innovation that incentivizes individual researchers and practitioners to bring their diverse skills to bear and to continually outperform each other. For such competitive innovation to be effective, researchers must start from compatible assumptions and use their limited resources to the greatest effect in their respective areas of expertise.

Power TAC distills these insights into a CDCS on which an iterative, competitive research process executes. The community contributes to Power TAC in three ways: by building and validating the Power TAC platform itself, by contributing novel EBA designs to the Power TAC process, and by conducting independent analyses of the resulting datasets. In this section, we describe the four principles underlying the Power TAC platform and process (see also Table 1), and in the following section we provide empirical evidence of their efficacy.

## Shared Problem Definition

Power TAC models the economic operation of a competitive electric distribution system in a medium- sized city, in which consumers and small-scale producers may choose from among a set of alternative electricity providers, represented by EBAs. EBAs are autonomous, profit-maximizing software agents built by individual research groups. The rest of the scenario is modeled by Power TAC (Figure 1). In order to evaluate the adaptability of EBA designs to varying competitive environments, the Power TAC scenario allows the number of competitors to be varied over a wide range, from pure monopoly, through oligopoly, to a strongly competitive market with many players.

Note that profit maximization does not preclude other social goals such as fairness, utilization of renewables, or certain levels of electric vehicle market penetration. By properly setting the market’s economic mechanisms (Dash et al. 2003), market designers can create incentive structures that lead selfinterested, profit-maximizing EBAs to socially desirable outcomes. Power TAC can be extended with user-designed market mechanisms that can then be subjected to EBA competition, but we limit our discussion here to its main use case of EBA design for brevity.

EBAs offer electricity tariffs (also known as plans or rates) to household and business customers through a retail market. Tariffs may include usage-based and per-day charges, fixed and varying prices for both consumption and production of electricity, rates that apply only above a specified usage threshold, etc. Some customers are equipped with solar panels and wind turbines, and many own demand-side management capabilities such as remotely controllable heat pumps or water heaters. All customers are equipped with smart meters from which consumption and production is reported every hour. Customers are sensitive to price changes and weather conditions, and they have a range of preferences over tariff terms. For example, some are willing to subscribe to variable-rate tariffs if they have the opportunity to save by adjusting their power usage, while others are willing to pay higher prices for the simplicity of fixed-rate or time-of-use tariffs. Many of these models are contributions from the community (e.g., Gottwalt et al. 2011; Reddy and Veloso 2012). EBAs buy and sell energy either from retail customers, or in the dayahead wholesale market, where utility-scale generators sell their output.

<table><tr><td colspan="4">Table 1. Core Principles Underlying the Power TAC CDCS Platform and Process</td></tr><tr><td>Principle</td><td>Explanation</td><td>Platform</td><td>Process</td></tr><tr><td>Joint work on shared problem definition</td><td>Replaces the single-investigator model and resulting smaller, incompatible problem definitions with a social learning process. The problem definition is continuously updated and validated in the CDCS, which is the central workpiece in CB.</td><td>√</td><td></td></tr><tr><td>Independent design</td><td>Independent research groups develop alternative solutions based on the CDCS, which yields a broader range of designs than conventional research approaches.</td><td></td><td>√</td></tr><tr><td>Competitive evaluation</td><td>Competitive evaluation yields higher confidence in the external validity of designs than single-investigator approaches. Importantly, and in contrast to conventional research competitions, evaluations against a fully dynamic problem definition (CDCS) enable evaluation at the system level where interactions between candidate designs can be observed.</td><td>√</td><td>√</td></tr><tr><td>Rich results and open analysis</td><td>Detailed trace data of CB competitions, together with executable designs, and analyses are made publicly available for third parties to validate and improve.</td><td></td><td>√</td></tr></table>

![](/api/attachments/TTEUYFRE/fulltext/images/9c1ad241bb4441d359b3033dc56c3beaf9206fa7be521ee68afb2527dbe990d6.jpg)

Figure 1. Main Elements of the Power TAC Scenario (EBAs are autonomous software agents built by individual research groups. The remainder of the scenario is modeled by the Power TAC platform.)

The distribution utility (DU) models a regulated monopoly that owns and operates the physical facilities (feeder lines, transformers, etc.) and is responsible for real-time balancing of supply and demand within the distribution network. It does this primarily by operating a balancing market that interacts with the real-time facet of the wholesale market, and by exercising demand and supply controls provided by EBAs. EBAs that have not properly balanced their demand-side and supply-side commitments ahead of time incur penalties through which the DU’s last-minute balancing services are financed.

Given a portfolio of customers, EBAs compete in the wholesale market to minimize the cost of power they deliver to their consuming customers, and to maximize the value of power delivered to them by their producing customers. A typical Power TAC simulation lasts approximately 60 days of simulated time (two hours of real time), although much longer simulations are possible. Together with its main scenario, the platform provides a scientific toolset that allows researchers to influence environmental conditions (e.g., the degree of renewable deployment) and to analyze and visualize the resulting individual and system behaviors.

The shared problem definition encoded in the Power TAC platform is continuously extended by the community to reflect real-world developments, which gradually raises the bar for EBA designers. These extensions are prioritized by an open community, and by an industry advisory board to ensure that the highest-value research questions are addressed (Rosemann and Vessey 2008). Jointly developing the platform spreads the effort of understanding and modeling the challenge across many researchers to increase scientific cycle speed. The initial investment amortizes as researchers gain the ability to rapidly test EBA designs without the frictions of first finding compatible benchmarks. The platform’s source code is licensed under a research and business-friendly Apache license and can be downloaded for free from https://github.com/powertac together with information on how to become engaged in the Power TAC community.

## Independent Design and Competitive Evaluation

Any effective design method is a structured approach to exploring and learning about solution spaces. Researchers create new designs, evaluate their realism and usefulness, learn from experience, and iterate to improve their work. This structured form of learning and improvement is related to benchmarking in that it requires skills in

systematic problem solving, experimentation with new approaches, learning from...own experience and past history, learning from the experiences and best practices of others, and transferring knowledge quickly and efficiently. [Its best practitioners rely] on the scientific method, rather than guesswork, for diagnosing problems [and insist] on data, rather than assumptions, as background for decision making (Garvin 1993, p. 81).

The upper part of Figure 1 illustrates how Power TAC embodies this competitive benchmarking notion in its iterative research process.

Participating researchers design EBAs based on the Power TAC CDCS platform. The platform is a comprehensive and thoroughly validated model of the underlying challenge. EBAs can also involve human traders, which opens interesting avenues for work on behavioral theories. Participants repeatedly evaluate their designs against the platform, and potentially other EBAs, to detect and remove weak- nesses. EBAs are then pitted against each other in a formal tournament where strategic interactions and system-level dynamics can be observed.

Unlike in conventional research methods, EBAs have to compete against a field of highly competitive benchmarking partners instead of a few benchmarks compiled by the research team itself. Moreover, an independent party determines the tournament schedule, including the pairing of EBAs and environmental conditions (e.g., weather conditions and electric vehicle deployment). This increases external validity and researchers’ confidence in the absence of unanticipated social negatives.

Finally, independent design and competitive evaluation add naturalistic dynamics to EBA evaluations. Researchers cannot hope to deploy preliminary designs into actual power systems and must therefore resort to working against a model of the challenge. However, one particularly important facet of real-world evaluation can be brought into the laboratory: the competitive coevolution of EBAs. Like firms and individuals in the real world, Power TAC participants constantly seek to improve their designs by adapting to the behavior of the environment and of others. The ensuing dynamics provide a unique tradeoff between artificial and naturalistic evaluation elements.

## Open Analysis and Rich Publication

The tournament outcome is a ranking of strategies, together with fine-grained data on individual EBA behaviors and system-level behavior. Unlike in conventional research processes, this data is made publicly available to participants and to third-party analysts who promote credible analyses that can be produced quickly and distributed along with the underlying data. Researchers can replay all tournament games to study courses of events in greater detail. The insights gleaned from these analyses are disseminated to participants and other stakeholders in order to pinpoint drivers of EBA performance that research groups can use to direct their future efforts (Ketter, Peters, and Collins al. 2013). Participants make executable versions of their tournament EBAs available for study, which is an attractive additional channel for distributing tangible research results that is not commonly found in conventional research methods. The comprehensive data generated in the Power TAC process also provides clear visibility of the progress that designers make in improving their artifacts. When progress tapers off, the community may decide to call the advisory board for new challenges.

We have focused our description here on the design and evaluation of EBAs, but Power TAC’s process equally supports other types of design tasks, and several non-design types of scientific inquiry. In particular, the platform together with a fixed set of high-performing EBAs can be used as a conventional agent-based virtual world (ABVW; Chaturvedi et al. 2011) to perform controlled experiments in pursuit of explanatory theories.

## Outcomes of the Power TAC Process

The Power TAC process encompasses official annual championships, and pilots that provide additional informal benchmarking opportunities. To date, pilots have been held at IJCAI 2011 in Barcelona, at AAMAS 2012 in Valencia, at IEEE SG-TEP 2012 in Nuremberg, and at the 2014 Erasmus Energy Forum in Rotterdam. The first two official championships were held at the AAAI 2013 conference in Bellevue, WA, and at AAMAS 2014 in Paris.<sup>4</sup>

All tournaments consisted of qualifying rounds in which EBAs were screened for technical flaws, followed by final rounds in which varying combinations of three, five, and eight EBAs competed. The finalists of the 2012, 2013, and 2014 tournaments were designed by groups with expertise in Artificial Intelligence, Electrical Engineering, Information Systems, Machine Learning, and other areas. Their heterogeneous approaches have contributed to a rich repository of design ideas, executable EBAs, and EBA performance data that we analyzed. Figure 2 gives a high-level view of the performances of EBAs at different levels of competition in the tournaments.<sup>5</sup> The figure supports several preliminary conclusions.

Heterogeneity Matters: Heterogeneity in designs led to large performance differences. The best EBAs outperformed competitors by more than an order of magnitude. Attracting heterogeneous designs, benchmarking them against each other, and understanding the theoretical basis of their functioning is, therefore, critically important.

Breakthrough Innovation: The two best EBAs in 2013 had only submitted an early-stage prototype in 2012 (TacTex) or no entry at all (cwiBroker). Nevertheless, they surpassed more established designs in the following year, which illustrates the powerful effect of competitive innovation.

Context Matters: Performance depended on the level of competitiveness and other environmental con- ditions. AstonTAC’s design, for example, lost ground to several competitors in three-EBA games in 2013, but continued to perform well in highly competitive eight-EBA games. Repeatable games under different environmental conditions, therefore, play an important role in fully understanding system dynamics and reducing the risk of incurring social negatives.

Note that it is only through Power TAC’s shared problem definition, the CDCS, and the public nature of its research process that we can freely access, understand, and compare such a broad variety of creative designs.

## Social Impact of Competitively Designed EBAs

Toward understanding the benefits of EBAs for addressing the sustainable electricity challenge, we now contrast the performance of retail electricity markets with and without EBAs.

![](/api/attachments/TTEUYFRE/fulltext/images/977ef5e27b3a25f0bfd1b2357ec4c0dc497b27a77be3834d5be99a60f4a42b7d.jpg)  
Larger circles indicate higher profits on average. Darker circles indicate a higher certainty, that is, a lower standard deviation of average profits.  
Figure 2. Average Profits of EBAs in the 2012 (top panel), 2013 (middle panel), and 2014 (bottom panel) Tournaments

To this end, we repeated the 59 games of the 2013 finals under identical environmental conditions but with only the incumbent monopoly, that is, without competitive EBAs. This procedure yielded 59 pairs of games, or close to 20 years of simulated system behavior at hourly resolution, for which we analyzed several important societal indicators.<sup>6</sup> Table 2 shows the quality indicators that we used in our comparison, and for which we calculated the mean differences between the monopolistic and the competitive setting. In all cases, the null hypothesis is no change. These quality indicators can be categorized as follows (see Appendix A for further details):

Retail Market Behavior: Overall system performance critically depends on the interactions of the EBAs with retail customers. We tracked realized prices, price variability, overall energy traded, and retail market competitiveness as indicated by the Herfindahl-Hirschman concentration index (HHI).

Balancing Behavior: In the case of imbalances between supply and demand, the balancing market acts as the energy source and sink of last resort. Such interventions by the distribution utility are an indication of instability if they occur frequently. We therefore tracked the development of balancing energy required by EBAs as a percentage of their overall energy trading business.

Load Factor: A steadier, more efficient use of the power infrastructure leads to lower environmental impact (e.g., fewer power line corridors) and reduced consumer prices. We tracked the load factor, the ratio between average and maximum load on the distribution infrastructure, as a measure of this efficiency.

The targeted change in these key performance indicators depends on perspective, and the directions given in Table 2 reflect Power TAC’s objective of contributing to the resolution of the sustainable energy challenge. The introduction of EBAs should lead to highly competitive retail markets with low and stable consumption prices ì – î, and attractive rewards for producing locally from renewable sources ñ. Because the incumbent monopoly already offers stable (albeit high) prices, retail price variability can at best be expected not to increase by much. Balancing ratios should decline as EBAs improve their forecasting abilities ï, and load factors should increase as EBAs learn to better incentivize favorable customer behavior ð. Meeting as many of these goals as possible is the Power TAC community’s long-term goal, as it would provide evidence that the decentralized, economic coordination provided by EBAs indeed contributes to the efficient operation of sustainable power systems.

Table 2. Quality Indicators for Power TAC’s Competitive Retail Electricity Market<sup>†</sup>

<table><tr><td colspan="2">Metric</td><td>3 Brokers</td><td>5 Brokers</td><td>8 Brokers</td><td>All Games</td><td colspan="3">Target</td></tr><tr><td rowspan="2">Retail Price Change</td><td>Sale</td><td>-0.42*</td><td>-0.44*</td><td>-0.45*</td><td>-0.43*</td><td>↘</td><td>✓</td><td>2</td></tr><tr><td>Purchase</td><td>-0.01*</td><td>-0.02*</td><td>-0.04*</td><td>-0.02*</td><td>↗</td><td>✘</td><td>6</td></tr><tr><td rowspan="2">Retail Price Variability</td><td>Sale</td><td>0.02*</td><td>0.017*</td><td>0.018*</td><td>0.018*</td><td>→</td><td>✘</td><td>3</td></tr><tr><td>Purchase</td><td>0.002*</td><td>0.005*</td><td>0.002*</td><td>0.004*</td><td>→</td><td>✓</td><td></td></tr><tr><td rowspan="2">Retail Volume Change</td><td>Sale</td><td>1.4*</td><td>1.41*</td><td>1.4*</td><td>1.4*</td><td>↘</td><td>✘</td><td>7</td></tr><tr><td>Purchase</td><td>1.02*</td><td>1.02*</td><td>1.02*</td><td>1.02*</td><td>↗</td><td>✓</td><td>8</td></tr><tr><td rowspan="2">HHI Change</td><td>Sale</td><td>-3050*</td><td>-4953*</td><td>-6802*</td><td>-4433*</td><td>↘</td><td>✓</td><td>1</td></tr><tr><td>Purchase</td><td>-216</td><td>-1132*</td><td>-27*</td><td>-746*</td><td>↘</td><td>✓</td><td></td></tr><tr><td rowspan="2">Balancing Ratio</td><td>Sale</td><td>0.02*</td><td>0.07*</td><td>-0.01</td><td>0.05*</td><td>↘</td><td>✘</td><td>4</td></tr><tr><td>Purchase</td><td>0.02*</td><td>0.07*</td><td>-0.01</td><td>0.05*</td><td>↘</td><td>✘</td><td>4</td></tr><tr><td colspan="2">Load Factor</td><td>0</td><td>-0.01</td><td>-0.01</td><td>-0.01</td><td>↗</td><td>✘</td><td>5</td></tr></table>

<sup>†</sup>As mean difference between competitive 2013 tournament games and corresponding monopolistic games, interpreted from the broker’s perspective. Stars indicate significance at the 5% level, circled numbers are referenced from the main text, checkmarks indicate targets that have been met.

The results of the 2013 tournament already meet several of these goals. Most importantly, we observe large and significant increases in competitiveness ì and decreases in retail prices í. We also note a significant but small price decrease for energy sourced from small-scale renewables ñ, contrary to the prediction of a price increase, and a slight increase in volume ó. These findings are further confirmed by Figure 3, which illustrates EBAs’ retail market strategies for the sale (left) and purchase (right) of energy. The left panel shows a remarkable reduction in overall price levels for consumers relative to the incumbent monopoly, as well as narrow price differences between EBAs in their competitive environment. The right panel additionally shows that many EBAs make use of small-scale production in their sourcing strategies, even if their control of this option is presently less evolved than that of retail sales (lighter font in the figure), and the increase in decentralized sourcing is consequently small ó.

These positives currently come with several social negatives that require careful consideration. First, lower retail consumption prices have naturally led to higher electricity consumption ò. While some of this additional consumption comes from renewable sources, we see the need for incentives that encourage consumer energy efficient behavior even when prices decline. EBAs could, for example, be rewarded for selling smarter through distribution charges coupled to a steadier, more efficient utilization of the distribution infrastructure. Second, through competition, retail markets have become significantly more turbulent as reflected in higher retail price variability î, the need for additional balancing power ï, and slightly lower load factors ð. Parts of the favorable competitive retail prices are, in other words, socialized by EBAs that put higher stress on consumers and the physical infrastructure in an effort to offer the lowest possible prices while remaining competitive.

## Discussion

The preliminary results above are ambivalent, but expected and desirable from a CB perspective. They are expected in that EBA designers have made meaningful, high-return design choices to obtain control over their complex environment in the first iterations of Power TAC’s process. Present generation EBAs autonomously set competitive prices, forecast demand with acceptable accuracy, and make explicit use of many strategic options such as sourcing from small-scale production. As the field of competitors grows more sophisticated, designers will also need to consider more subtle effects arising from complex interactions like those in the balancing market. In the future, we expect that designers incorporate ideas with successively lower return on design investment.

The results are desirable in that they raise the right questions. The analyses we presented above are objective in the sense that we provide no value judgment on the relative importance

![](/api/attachments/TTEUYFRE/fulltext/images/f74839a06d45c18efe78105b7e0b0761020490f0f054ed41eff0dde9aca4a4e7.jpg)  
Each panel shows the relationship between volume captured and average price paid. Left: Market for energy consumption (EBAs sales). Right: Market for small-scale production (EBAs purchases). Lighter labels indicate higher variations in market shares between games. The Incumbent (left panel), as well as AstonTAC and TacTex (right panel) deal at price levels outside the visible area of the figure.

## Figure 3. Strategic Retail Market Positioning of EBAs

of individual goals. It is unclear whether all goals can be achieved simultaneously, and it is the subject of politics to prioritize among them. Should society care about higher stress on distribution infrastructures? Should the bulk of the welfare effects from price reductions go to consumers, or should parts of these benefits be used to incentivize more efficient energy use and investments in renewables? Power TAC invites these questions, and provides the means to study the effect of alternate answers on businesses and consumers.

## Research Context

Our work on Power TAC is rooted in the competitive research approach pioneered by the Trading Agents community (Ketter and Symeonidis 2012; Wellman 2011), which aims to deploy computation techniques to trading applications. Trading Agent Competitions (TAC) challenge researchers to devise software agents for complex, uncertain environments like supply chains, and to benchmark and improve them iteratively (Collins, Ketter, and Sadeh 2010b). A key difference of our work is its emphasis on real-world alignment. Theories developed through Power TAC must be representative of realworld dynamics to the degree that they can be used for policy guidance, and designs developed through Power TAC must meet the usefulness criterion of IS design science. That is, they must address an important business problem, and their utility, quality, and efficacy must be clearly demonstrated (Hevner et al. 2004). While previous TACs, such as TAC SCM, the competition for Supply Chain Management (Ketter et al. 2012), have been inspired by current business settings, their focus has been on stylized decision problems, and system-level consequences of interventions played no significant role in them.

A competitive element is also present in research competitions, like those organized by Netflix (Bell and Koren 2007) and Kaggle (http://www.kaggle.com), which encourage participants to develop solutions for data mining, forecasting, and optimization problems. Like Power TAC, they attract diverse communities of experts from various technical backgrounds, and the rich repositories of resulting designs explore many corners of the vast space of possible solutions. But while research competitions leverage iteration and benchmarking, they forgo the benefits of collaborative analysis, learning, and improvement that are central to Power TAC. Moreover, they are based on static datasets, not on CDCS platforms, and interactions between candidate designs play no role in them, because they aim to address complicated, not complex problems.

Work on agent-based computational economics (ACE; Tesfatsion 2006) and agent-based virtual worlds (ABVW; Chaturvedi et al. 2011) foregrounds complexity issues in an effort to derive possible futures of sociotechnical systems, and the paths to these futures, based on realistic assumptions. Creating agent-based models that faithfully capture interesting aspects of real-world phenomena is difficult, because the represented phenomena are often vague, unstructured, and perennially changing. ABVW research, therefore, promotes the use of simulation platforms on which user-contributed content can be executed, so that users become citizen developers who contribute to the richness and validation of the models. The Power TAC platform is a virtual world by definition, and design guidelines like the involvement of citizen developers were important in its construction. However, in CB, the platform remains one aspect of a larger idea, and competitive innovation, independent evaluation, and other aspects play an equally important role.

## Impact

Counteracting the rapid deterioration of our natural environment requires research that goes “beyond conceptualizing, analyzing, and even designing, to...demonstrable impact” (Malhotra et al. 2013, p. 1266). Within four years from the original idea, Power TAC has evolved into the most comprehensive economic simulation for electric distribution networks worldwide, and we now describe the impact this idea is generating on research, teaching, and practice.

The initial development of Power TAC was supported by a core community of researchers who conducted stakeholder interviews, surveyed the power systems and smart grids literatures, and implemented early versions of the platform. These efforts gradually attracted researchers interested in leveraging the publicly available platform for their own work. Several groups contributed specialized knowledge that improved its realism in areas where no other community member possessed the requisite expertise or resources, for example, customer modeling (Reddy and Veloso 2012) and balancing (de Weerdt et al. 2011). In exchange, the contributors could study their models in a rich environment that they could not have created otherwise, including a dedicated community that validated and critiqued their models. Other groups created experimental tools for and third-party analyses of Power TAC, compared the platform against real-world behaviors, and published early EBA designs (e.g., Kuate et al. 2013; Nanoha 2013; Peters et al. 2013; Reddy and Veloso 2011). By now, these early efforts have sparked a lively research dialog on design ideas and improvements, which shows that the Power TAC process is unfolding its effect (Babic and Podobnik 2014; Liefers et al. 2014; Urieli and Stone 2014; Valogianni et al. 2013).

It is worth emphasizing that many of these researchers had technical expertise but no prior domain knowledge or interest in contributing to the sustainable electricity challenge. It was the availability of a CDCS that triggered them to apply their diverse technical skills to sustainable energy. Conversely, researchers and external stakeholders with energy domain knowledge benefited from the innovative contributions of these technical experts.

We observe a similar impact on our teaching, where we are using Power TAC to raise awareness of sustainable energy issues in students at the undergraduate, graduate, and executive levels. For example, we are currently supervising master’s theses and dissertations on sustainable business models for electric vehicle fleets, influencing environmental beliefs through IS, using social networks to foster sustainable electricity communities, economic analyses of IS deployments, and numerous other topics that would exceed the scope of this article. In each of these cases, the tangible nature of the Power TAC platform played a decisive role in exciting students about the possibility of making a meaningful contribution to a seemingly gargantuan challenge. Many of our graduates have chosen to continue their energy-related work at universities, in the energy industry, or as sustainable energy entrepreneurs.

Finally, our focus on continuously aligning Power TAC with real-world developments has spawned a series of collaborations with stakeholders in the energy industry and in energy policy. We already mentioned the Power TAC advisory board, which comprises representatives from utility companies, network infrastructure providers, communication electronics manufacturers, electricity cooperatives, and electricity customer lobby groups. The board meets twice yearly to provide researchers with industry insights, to ensure that important challenges are being tackled, and to disseminate research results based on the Power TAC platform. The strong interest in these results has prompted the first author to found the Erasmus Energy Forum (www.rsm.nl/ energyforum), now in its fourth year, bringing together practitioners, policy makers, and researchers to debate the future of electricity.

An important input to these debates are the insights gleaned from practical Power TAC implementations. For example, Power TAC is now being used as part of the Cassandra platform (www.cassandra-fp7.eu) for strategic decisionmaking in power systems. First versions of this platform have been deployed in pilot projects in Coventry (UK), Milan (Italy), and Luleå (Sweden). Customers in participating pilot buildings receive real-time feedback on their electricity consumption, see the impact of their own decisions on the overall power system, and coordinate through social networks to reduce their impact as a community. In another project, we are evaluating the potential of Power TAC as a testbed for innovative interventions in smart energy neighborhoods. In this project, a major Dutch utility is operating a smart energy pilot neighborhood, and is seeking ways of evaluating candidate interventions before deploying them into the actual system.

## Conclusions

Power TAC is an example of a competitive benchmarking approach, through which a global community of researchers aims to address the sustainable electricity challenge. To date, this community has created a diverse set of candidate designs for a novel class of IS artifacts that we call EBAs, and that contribute to sustainability objectives like better integration of renewable energy sources. By turning worthy causes into viable business models, EBAs provide “an opportunity to create shared value—that is, a meaningful benefit for society that is also valuable to the business” (Porter and Kramer 2006, p. 84).

Our focus in this research note has been on portraying the community-built Power TAC platform, and the novel type of competitive research process that builds on it. Platform and process together facilitate scalable, self-organizing research communities, shift peer-review and applicability checks to the earliest possible time, bring competitive elements to designers’ laboratories, and lead to a swift dissemination of independently evaluated results. Within four years, a strong research community has crystallized around Power TAC, including many technical experts with no prior interest in sustainability issues, who are contributing to the resolution of the sustainable electricity challenge. The fruits of this work are tangible artifacts and analyses that are interesting to practitioners and policy makers alike, and several of these designs are now being deployed on smart grid pilot sites.

If competitive benchmarking proves an effective method for design in fast-paced, high-complexity environments like power systems, it stands to reason that it is generally useful as a method for research on rapidly evolving societal challenges with similar characteristics.

For example, research on financial market stability could benefit from a competitive research approach where researchers design and improve new trading strategies and the rules under which these strategies operate. A competitive strategy design process could be more effective in uncovering potential loopholes in the market rules, and the designers of new market rules could validate their work against a broader set of trading strategies. Importantly, the results of these evaluations would be metrics of interest at the societal level (see Table 2) instead of narrow technical indicators, which can be used to guide policy decisions. We therefore speculate that the potential benefits of the community’s effort go beyond the design of electricity EBAs alone.

## References

Amin, M. S., and Wollenberg, B. F. 2005. “Toward a Smart Grid: Power Delivery for the 21<sup>st</sup> Century,” IEEE Power and Energy Magazine (3:5), pp. 34-41.

Babic, J., and Podobnik, V. 2014. “Adaptive Bidding for Electricity Wholesale Markets in a Smart Grid,” in Proceedings of the 13<sup>th</sup> International Conference on Autonomous Agents and Multi-Agent Systems, Paris, France.

Bell, R., and Koren, Y. 2007. “Lessons from the Netflix Prize Challenge,” ACM SIGKDD Explorations Newsletter (9:2), pp. 75-79.

Bichler, M., Gupta, A., and Ketter, W. 2010. “Designing Smart Markets,” Information Systems Research (21:4), pp. 688-699.

Borenstein, S. 2002. “The Trouble with Electricity Markets: Understanding California’s Restructuring Disaster,” Journal of Economic Perspectives (16:1), pp. 191-211.

Chaturvedi, A. R., Dolk, D. R., and Drnevich, P. L. 2011. “Design Principles for Virtual Worlds,” MIS Quarterly (35:3), pp. 673-684.

Collins, J., and Ketter, W. 2014. “Smart Grid Challenges for Electricity Retailers,” KI—Künstliche Intelligenz (28:3), pp. 191-198.

Collins, J., Ketter, W., and Gini, M. 2009. “Flexible Decision Control in an Autonomous Trading Agent,” Electronic Commerce Research Applications (8:2), pp. 91-105.

Collins, J., Ketter, W., and Gini, M. 2010. “Flexible Decision Support in Dynamic Interorganizational Networks,” European Journal of Information Systems (19:3), pp. 436-448.

Collins, J., Ketter, W., and Sadeh, N. 2010. “Pushing the Limits of Rational Agents: The Trading Agent Competition for Supply Chain Management,” AI Magazine (31:2), pp. 63-80.

Dash, R. K., Jennings, N. R., and Parkes, D. C. 2003. “Computational-Mechanism Design: A Call to Arms,” IEEE Intelligent Systems (18:6), pp. 40-47.

de Weerdt, M., Ketter, W., and Collins, J. 2011. “A Theoretical Analysis of Pricing Mechanisms and Broker’s Decisions for Real-Time Balancing in Sustainable Regional Electricity Markets,” in Proceedings of the Conference on Information Systems and Technology, Charlotte, pp. 1-17.

Gartner Group. 2013. “IT Spending Report, Q4 Update,”Stamford, CT.

Garvin, D. A. 1993. “Building a Learning Organization,” Harvard Business Review (71:4), pp. 78-91.

Gottwalt, S., Ketter, W., Block, C., Collins, J., and Weinhardt, C. 2011. “Demand Side Management—A Simulation of Household Behavior Under Variable Prices,” Energy Policy (39), pp. 8163-8174.

Hanusch, H., and Pyka, A. 2007. “Principles of Neo-Schumpeterian Economics,” Cambridge Journal of Economics (31:2), pp. 275-289.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Joskow, P., and Tirole, J. 2006. “Retail Electricity Competition,” The Rand Journal of Economics (37:4), pp. 799-815.

Kahlen, M., Ketter, W., and van Dalen, J. 2014. “Balancing with Electric Vehicles: A Profitable Business Model,” in Proceedings of the 22<sup>nd</sup> European Conference on Information Systems, Tel Aviv, Israel.

Ketter, W., Collins, J., Gini, M., Gupta, A., and Schrater, P. 2012. “Real-Time Tactical and Strategic Sales Management for Intelligent Agents Guided by Economic regimes,” Information Systems Research (23:4), pp. 1263-1283.

Ketter, W., Collins, J., and Reddy, P. 2013. “Power TAC: A Competitive Economic Simulation of the Smart Grid,” Energy Economics (39), pp. 262-270.

Ketter, W., Collins, J., Reddy, P., and de Weerdt, M. 2015. “The 2015 Power Trading Agent Competition,” Technical Report ERS-2015-001-LIS, RSM Erasmus University, The Netherlands.

Ketter, W., Peters, M., and Collins, J. 2013. “Autonomous Agents in Future Energy Markets: The 2012 Power Trading Agent Competition,” in Association for the Advancement of Artificial Intelligence Conference Proceedings, Bellevue, WA, pp. 1298-1304.

Ketter, W., and Symeonidis, A. 2012. “Competitive Benchmarking: Lessons Learned from the Trading Agent Competition,” AI Magazine (33:1), pp. 103-107.

Kuate, R. T., He, M., Chli, M., and Wang, H. H. 2013. “An Intelligent Broker Agent for Energy Trading: An MDP Approach,” in Proceedings of the 23<sup>rd</sup> International Joint Conference on Artificial Intelligence, pp. 234-240.

Liefers, B., Hoogland, J., and La Poutre, H. 2014. “A Successful Broker Agent for Power TAC,” in Proceedings of the 13<sup>th</sup> International Conference on Autonomous Agents and Multi-Agent Systems, Paris, France.

Malhotra, A., Melville, N. P., and Watson, R. T. 2013. “Spurring Impactful Research on Information Systems for Environmental Sustainability,” MIS Quarterly (37:4), pp. 1265-1274.

Melville, N. P. 2010. “Information Systems Innovation for Environmental Sustainability,” MIS Quarterly (34:1), pp. 1-21.

Nanoha, R. 2013. “Confidence Assessment of an Agent-Based Simulation—Operational Validation of the Power TAC Simulation Platform,” Master’s Thesis, Rotterdam School of Management.

Nunamaker, Jr., J. F., and Briggs, R. O. 2011. “Toward a Broader Vision for Information Systems,” ACM Transactions on Management Information Systems (2:4, Article 20).

Peters, M., Ketter, W., Saar-Tsechansky, M., and Collins, J. E. 2013. “A Reinforcement Learning Approach to Autonomous

Decision-Making in Smart Electricity Markets,” Machine Learning (92), pp. 5-39.

Porter, M. E., and Kramer, M. R. 2006. “The Link Between Competitive Advantage and Corporate Social Responsibility,” Harvard Business Review (84:12), pp. 78-92.

Ramchurn, S., Vytelingum, P., Rogers, A., and Jennings, N. 2012. “Putting the ‘Smarts’ into the Smart Grid: A Grand Challenge for Artificial Intelligence,” Communications of the ACM (55:4), pp. 86-07.

Reddy, P., and Veloso, M. 2011. “Strategy Learning for Autonomous Agents in Smart Grid Markets,” in Proceedings of the 22<sup>nd</sup> International Joint Conference on Artificial Intelligence, Barcelona, pp. 1446-1451.

Reddy, P., and Veloso, M. 2012. “Factored Models for Multiscale Decision Making in Smart Grid Customers,” in Proceedings of the 26<sup>th</sup> AAAI Conference on Artificial Intelligence, Toronto, pp. 363-369.

Rosemann, M., and Vessey, I. 2008. “Toward Improving the Relevance of Information Systems Research to Practice: The Role of Applicability Checks,” MIS Quarterly (32:1), pp. 1-22.

Tesfatsion, L. 2006. “Agent-Based Computational Economics: A Constructive Approach to Economic Theory,” in Handbook of Computational Economics (Volume 2), L. Tesfatsion and K. L. Judd (eds.), Amsterdam: North Holland, pp. 831-880.

Urieli, D., and Stone, P. 2014. “TacTex13: A Champion Adaptive Power Trading Agent,” in Proceedings of the 28<sup>th</sup> Conference on Artificial Intelligence, Quebec, Canada.

U.S. Energy Information Administration. 2013a. “Electric Power Annual 2011” (http://www.eia.gov/electricity/annual/).

U.S. Energy Information Administration. 2013b. “Monthly Energy Review February 2013” (http://www.eia.gov/mer).

Valogianni, K., Ketter, W., and Collins, J. 2013. “Smart Charging of Electric Vehicles Using Reinforcement Learning,” in Workshops at the 27<sup>th</sup> AAAI Conference on Artificial Intelligence, pp. 41-48.

Valogianni, K., Ketter, W., Collins, J., and Zhdanov, D. 2014. “Enabling Sustainable Smart Homes: An Intelligent Agent Approach,” in Proceedings of the 35<sup>th</sup> International Conference on Information Systems, Auckland, New Zealand.

Watson, R. T., Boudreau, M.-C., and Chen, A. J. 2010. “Information Systems and Environmentally Sustainable Development: Energy Informatics and New Directions for the IS Community,” MIS Quarterly (34:1), pp. 23-38.

Wellman, M. P. 2011. Trading Agents, San Rafael, CA: Morgan & Claypool Publishers.

Worldbank. 2013. “CO2 Emissions (kt) Catalog Sources World Development Indicators” (http://data.worldbank.org/indicator/ EN.ATM.CO2E.KT/countries).

## About the Authors

Wolf Ketter is Professor of Next Generation Information Systems and chair of the Information Systems section at the Department of Technology and Operations Management at the Rotterdam School of Management of Erasmus University. In addition, he is director of the Learning Agents Research Group at Erasmus (LARGE) and the Erasmus Center for Future Energy Business. Wolf is also the founder and chair of the Erasmus Forum for Future Energy Business. In 2010, he became president of the Association for Trading Agent Research (ATAR). ATAR organizes the annual Trading Agent Competition (TAC). Wolf is leading Power TAC, a new TAC challenge on energy retail markets. He has served as general chair or program chair of more than 20 international conferences and workshops. His research has been published in various op energy, information systems, and computer science journals such as Decision Sciences, Energy Economics, Information Systems Research, and Machine Learning. He serves on the editorial boards of Information Systems Research and MIS Quarterly. In December 2012, he received the prestigious INFORMS Design Science Award, and in June 2013, he received the runner-up award for the best European Information Systems research paper of the year.

Markus Peters’s research focuses on machine learning algorithms for future retail electricity markets. His work on the topic has appeared in Data and Knowledge Engineering and Machine Learning Journal, and has been presented at various information systems and computer science conferences. Markus obtained his Ph.D. in Information Systems from Erasmus University in 2015. He is now the Director of Development & Operations at Peters Software.

John Collins spent 30 years in industry doing research and product development before returning to the University of Minnesota, where he completed his Ph.D. in 2002. There, he taught in the areas of software engineering and artificial intelligence until his retirement in 2013. His research focuses on economic decision processes in autonomous software agents. For the past 12 years, he has been involved in the Association for Trading Agent Research, where he led a major redesign of the supply-chain scenario, served on the board of directors for several years, and is currently managing the continuing development and maintenance of the game scenario and software infrastructure for the Power TAC competition.

Alok Gupta is the Associate Dean for Faculty and Research at the Carlson School of Management, University of Minnesota. He is Curtis L. Carlson Schoolwide Chair in Information Management, and the former chair of the Information and Decision Sciences Department. His research has appeared in several information systems, economics, and computer science journals including Management Science, Information Systems Research, and MIS Quarterly. Alok was awarded the prestigious NSF CAREER Award for his research on dynamic pricing mechanisms on the Internet in 2001, and named an INFORMS Information Systems Society Distinguished Fellow in 2014. He served as a senior editor for Information Systems Research from 2007–2013 and has been serving as an associate editor of Management Science since 2007.

## Appendix A

## Definition of Quality Indicators

<table><tr><td colspan="3">Table A1. Definition of Quality Indicators for Power TAC&#x27;s Competitive Retail Electricity Market</td></tr><tr><td colspan="2">Metric</td><td>Definition</td></tr><tr><td rowspan="2">Retail Price</td><td>Sale</td><td>Price of one kWh sold by EBAs to retail customers, averaged over all transactions by all EBAs.</td></tr><tr><td>Purchase</td><td>Price of one kWh purchased by EBAs from retail customers (small-scale producers), averaged over all transactions by all EBAs.</td></tr><tr><td rowspan="2">Retail Price Variability</td><td>Sale</td><td>Standard deviation of average retail sale prices per kWh per time interval (one hour of simulated time).</td></tr><tr><td>Purchase</td><td>Standard deviation of average retail purchase prices per kWh per time interval (one hour of simulated time).</td></tr><tr><td rowspan="2">Retail Volume Change</td><td>Sale</td><td>Relative change in overall retail electricity sales between monopolistic and competitive setting (1.0 = unchanged).</td></tr><tr><td>Purchase</td><td>Relative change in overall retail electricity purchase between monopolistic and competitive setting (1.0 = unchanged).</td></tr><tr><td colspan="2">HHI</td><td> $\sum_{n=1}^{N} s_n^2$  where N denotes the total number of firms in a market and  $s_n$  the market share of firm n in percent. Possible index values range from 0 (perfect competition) to 10,000 (monopoly).</td></tr><tr><td rowspan="2">Balancing Ratio</td><td>Sale</td><td>Amount of excess energy sold to the balancing market (i.e., spot sales) relative to overall wholesale market sales.</td></tr><tr><td>Purchase</td><td>Amount of excess energy purchased from the balancing market (i.e., spot purchases) relative to overall wholesale market purchases.</td></tr><tr><td colspan="2">Loading Factor</td><td>Ratio between the average and the maximum utilization (in kWh) of the distribution infrastructure. Higher load factors indicate better utilization of the fixed-capacity infrastructure.</td></tr></table>
