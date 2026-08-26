---
otero_id: 28406
otero_key: "JWJP7MBA"
title: "Silence Inside Systems: Roots and Generativity Consequences"
authors: "Amrit Tiwana; Hani Safadi"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0586"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Silence Inside Systems: Roots and Generativity Consequences

Amrit Tiwana,<sup>a,</sup>\* Hani Safadi<sup>a</sup>

<sup>a</sup> University of Georgia, Athens, Georgia 30602

\*Corresponding author

Received: October 23, 2022 Revised: July 13, 2023; August 22, 2024; December 10, 2024; March 10, 2025 Accepted: May 5, 2025 Published Online in Articles in Advance: June 27, 2025

https://doi.org/10.1287/isre.2022.0586

Contact: tiwana@uga.edu, https://orcid.org/0000-0003-1750-2528 (AT); hanisaf@uga.edu, https://orcid.org/0000-0003-0609-8005 (HS)

Copyright: © 2025 INFORMS

Abstract. Silence as a system behavior has evaded attention in information systems (IS) discourse, where interaction predominates. It merits examination as systems grow brittle, brute-force countermeasures falter, and autonomous systems risk misbehaving. We conceptualize silence as dynamic system-wide behavior, theorizing how it drives IS generativity by coalescing developers’ attention on temporally shifting slivers of a system’s codebase. Using a supercomputer-scale model, we analyzed nearly 20 million tweaks over a quarter of a century in over a thousand systems, constructing 67,000+ evolving human to-artifact networks to infer such behavioral dynamics. We show that silence breeds generativity by dynamically funneling developers’ attention. We make three contributions. First, we introduce silence as a dynamic system-wide behavior rooted in system architecture. Second, we show silence’s generativity consequences—halving degenerativity, doubling evolution speed, quadrupling releases, and spawning 600 times as many forks. Third, we uncover attention funneling as the mechanism linking silence to generativity.

History: Yulin Fang, Senior Editor; Magnus Ma¨hring, Associate Editor.

Keywords: attention • silence • chattiness • evolutionary dynamics • IS generativity • IT evolution • loose coupling • architecture quietness • supercomputing methods • Miles Davis • Moore’s law • Shikantaza • trace data • system behavior

## 1. Introduction

Small tweaks can fuel giant leaps in systems. A new technology wave such as generative artificial intelligence (AI), a novel design philosophy like containerization, or an infrastructural innovation such as hyperscaling lets us extend systems in powerful new ways, fostering what scholars call information systems (IS) generativity (Fu¨ rstenau et al. 2023, Vial 2023). Although prior research emphasizes its architectural foundations (Yoo et al. 2010, Rolland et al. 2018, Tiwana and Safadi 2024), systems’ behavior—potentially just as crucial—has yet to receive much attention. A growing recognition that as systems evolve, their behavior diverges from their original design puts this in the spotlight (e.g., Lindberg et al. 2016, Fu¨ rstenau et al. 2023).

A key aspect of a system’s behavior is how much its parts interact with each other—what we envision as a system’s “chattiness” or “silence.” Silence, we contend, is an underappreciated trait of systems’ behavior. We retrace silence to an overlooked nuance in the seminal work of Simon (1962, p. 481), where he coveted infrequent interactions among a system’s parts (“silence”). Understanding this theoretically could unlock IS generativity. We initiate the conversation, asking the following question. How and why does silence inside a system shape its generativity?

Brittleness, waning countermeasures, and autonomous systems drive the urgency to understand evolving systems’ understudied behavior. First, systems grow brittle as illustrated by large-scale information technology (IT) meltdowns increasingly precipitated by one tweak.<sup>1</sup> Evolution breeds unpredictable behaviors (Lindberg et al. 2016, Rolland et al. 2018, Fu¨ rstenau et al. 2023, Tiwana and Safadi 2024), often defying architectural expectations (Rahwan et al. 2019). So, we might see chattiness where we expect silence and silence where we expect chattiness. Second, the waning of historic countermeasures—Moore’s law hitting the limits of physics and bandwidth costs soaring (Lundstrom 2003)—aggravates challenges with chatty systems.<sup>2</sup> Netflix’s 900 microservices illustrate this challenge. Brute force can demand deep pockets; Microsoft built a \$400 million, 4,100-mile trans-Atlantic undersea cable for Office-365.<sup>3</sup> Silence inside systems might be an elegant alternative. Third, our nascent understanding of evolving systems’ behavior (Rahwan et al. 2019, p. 478) induces anxiety about AI-fueled autonomous systems as anecdotes of ChatGPT hallucinating, Teslas running over pedestrians, Boeings crashing, smart munitions going haywire, and DaVinci surgeries going awry illustrate.<sup>4</sup> As metallurgist Smith (1981, p. 54) presaged, the essence of complex structures lies in how their parts interact. Understanding behaviors of evolving IT systems requires a uniquely IS mindset where humans and IT artifacts are simultaneously front and center.

Software engineering overlooks this phenomenon for three likely reasons. First, it prioritizes immediate operational performance (latency, congestion, defects, reliability) over long-term generativity (e.g., Jin et al. 2022, Abgaz et al. 2023). Second, it analyzes static code snapshots rather than systems’ evolving behavior (Rahwan et al. 2019)—using a camera where we need a video recorder. Third, causal mechanisms—the “why” (Ashworth et al. 2021, p. 48)—lie outside its foci and repertoire (Rahwan et al. 2019, p. 482).

Figure 1 illustrates our focal gaps: ‹ how silence shapes generativity and › why (the black-box mechanism). Resurrecting March and Simon (1958), we conceptualize silence inside a system as a system-wide behavior of minimal chattiness among its modules. Such silence, we theorize, promotes IS generativity by dynamically funneling teams’ attention on narrow slivers of a system’s codebase. Although rooted in causally upstream studies of IS architecture (the left side of Figure 1), our theory moves nomologically further along the causal chain.

We tested these ideas using a supercomputer to construct novel, computationally intensive data streams. We analyzed 274 million lines of code, 9.7 million dependencies, and 19.8 million code changes across 194,105 modules in 1,356 open-source systems. We examined every human-artifact interaction as these millions of IT artifacts evolved over a quarter of a century, constructing 67,000+ system-wide social-network measures to infer our constructs.

We advance IT evolution research in three ways. First, we introduce silence as a dynamic system-wide behavior, enlarging the architecture-dominated conversation. Second, we show that silence enhances IS generativity— spawning more forks, curbing degenerativity, and speeding evolution—while revealing the consequences of unexpected chattiness and silence. Third, we unblackbox attention funneling as a powerful mechanism that coalesces scarce developer attention into IS generativity. We found that shifting between extremes doubles system quality and evolution pace, quadruples release cadence, and increases generative forking 600 fold. To software engineering, we contribute silence as a theoretical concept rooted in architecture, its long-term effects, novel evolutionary measures, and insights into how system behavior shapes developer-code interactions. Subsequent sections develop these ideas, methods, analyses, and our contributions.

## 2. Theory

The gist of our forthcoming theory is as follows. Silence inside a system—by dynamically funneling team attention—fosters IS generativity. Our unit of analysis is a system. Table 1 defines our key constructs, and Figure 2 summarizes our model. Here, codebase refers to uncompiled source code, whereas architecture— causally upstream to our model’s focus—encompasses the system-wide arrangement of modules, including their coupling, nesting, and scope in prior studies.

## 2.1. Foundation: Simon’s Systems Theory

Our theoretical foundation is Simon’s (1962) general systems theory. His theory applies across all varieties of systems—from biological and mechanical to social and organizational. His central insight is that organizing systems as collections of subsystems (“modules”) that interact minimally with each other but are internally tight-knit makes systems more evolvable. Simon (1962) idolized interactions among modules so weak that they become nearly independent.

Simon’s (1962) ideas profoundly influenced modern IT systems, making modularity a defining trait of modern systems. Lost in the contemporary translation of Simon’s theory is the nuance that Simon emphasized systems’ internal behavior rather than just systems’ architecture. Recent studies in both software engineering (e.g., Aiomar et al. 2024) and IS (e.g., Lindberg et al. 2016, Fu¨ rstenau et al. 2023) have rediscovered that systems behavior often diverges from their architecture as they evolve.

Silence inside a system—which we conceptualize from the ground up from its Simonian roots—is about the dynamic interaction behavior among modules constituting a system; it is distinct and separable from a system’s architecture. To illustrate, consider a building’s architecture. It can influence—but is not deterministic of—how its occupants interact. Similarly, a system’s architecture influences but does not dictate its silence behavior. We, therefore, conceptualize silence as a system-wide behavior that is rooted in but not entirely determined by its architecture. This focuses us on how systems actually behave rather than how their architecture says they should.

Figure 1. (Color online) Our Research Question Encompasses the ‹ Nature (“How”) and the › Black-Boxed Mechanism (“Why”) of the Relationship  
![](/api/attachments/JWJP7MBA/fulltext/images/f326d7205fb38ba742cf8e15c7f254bbdcc09679c6a5058ca689e8c5dc60966e.jpg)

Table 1. Key Constructs and Their Measures

<table><tr><td>Construct</td><td>Definition and ≈ measure</td><td>Role</td><td>Representative reference</td></tr><tr><td> $\text{Silence}_t$ </td><td>Sparsity of module-to-module interactions within a system≈ (1 - density of codebase-wide module-to-module network) $_t$ </td><td>Predictor</td><td>Simon (2002); Richards and Ford (2020, p. 127)</td></tr><tr><td> $\text{Attention funneling}_t$ </td><td>Concentration of code changes on fewer modules≈ Centralization of codebase-wide developer-to-file linkages $_t$ </td><td>Mediator</td><td>Hansen and Haas (2001)</td></tr><tr><td> $\text{Codebase generativity}^a$ </td><td>Derivative systems spawned from the original codebase≈ Cumulative number of codebase forks</td><td>Criterion</td><td>Fürstenau et al. (2023)</td></tr><tr><td> $\text{Degenerativity}_t$ </td><td>The number of linearly independent paths in codebase≈ Cyclomatic complexity</td><td>Criterion</td><td>Chidamber and Kemerer (1994)</td></tr><tr><td> $\text{Evolution rate}_t$ </td><td>Rate of change in a system&#x27;s codebase≈ Quarterly count of code commits to a  $\text{codebase}_t$ </td><td>Criterion</td><td>Simon (1962, p. 470)</td></tr><tr><td> $\text{Release cadence}^a$ </td><td>Count of upgraded versions of the system released≈ Cumulative lifetime number of releases</td><td>Criterion</td><td>Richards and Ford (2020, p. 116)</td></tr><tr><td> $\text{Loose coupling}_t$ </td><td>Looseness of coupling among system&#x27;s modules≈ 1 - (#module invocations $_t$  ÷ #possible module invocations $_t$ )</td><td>Instrument</td><td>Chidamber and Kemerer (1994)</td></tr><tr><td> $\text{Hierarchical depth}_t$ </td><td>#layers deep module-to-subordinate module relationships run≈ Average shortest-path length in the file-to-module network constructed for the entire system&#x27;s codebase</td><td>Instrument</td><td>Simon (1962, p. 468)</td></tr><tr><td> $\text{Module coarseness}_t$ </td><td>Degree of coarseness of a system&#x27;s modules≈ Centralization of codebase-wide network of file-to-module dependencies $_t$ </td><td>Instrument</td><td>Subramanyam et al. (2012)</td></tr><tr><td> $\text{Code volume}_t$ </td><td>Number of lines of code≈ Count of lines of code in a system&#x27;s  $\text{codebase}_t$ </td><td>Control</td><td>Subramanyam et al. (2012)</td></tr><tr><td> $\text{Module count}_t$ </td><td>Number of modules≈ Number of Java “packages” in a system&#x27;s codebase</td><td>Control</td><td>Simon (1962)</td></tr><tr><td>Age</td><td>Chronological system age≈ Years lapsed since a system&#x27;s initial release</td><td>Control</td><td>—</td></tr><tr><td> $\text{Team size}_t$ </td><td>Number of active developers≈ #Developers who committed  $\text{code}_t$ </td><td>Control</td><td>—</td></tr><tr><td> $\text{Architecture refactoring}_t$ </td><td>Ratio of files that differ from the previous quarter≈ Files changed since last quarter ÷ all files in this and previous quarter</td><td>Control</td><td>(Aiomar et al. 2024)</td></tr></table>

<sup>a</sup>Constructs are cumulative through t + 5 years; all others are panel data measured each quarter .

Figure 2. (Color online) Research Model Illustrating the Central Mechanism of Attention Funneling  
![](/api/attachments/JWJP7MBA/fulltext/images/66149a83acf06132caa07811877067345bb84e84b6dcd5f34e04ebc524ddd6ca.jpg)

## 2.2. Silence Inside Systems

Our conceptualization builds on the notion of weak interaction behavior among a system’s modules in Simon (1962, p. 481)—fundamental to his idea of near independence. His emphasis on near recognized that modules must interact somewhat to constitute a system, advocating for weak interactions among subsystems. In his posthumous work spanning broad classes of systems, Simon (2002) explicitly used the term “silence,” a concept that we adopt. He reiterated minimizing interactions among modules, warning that “talk drowns out silence” (Simon 2002, p. 611).

This idea of limited interaction behavior among a system’s modules is central to organizing systems yet has never explicitly received theoretical attention. However, we must first conceptually differentiate silence from adjacent concepts, demonstrate its unique value, and build it from the ground up in ways cumulative on related work.

2.2.1. Adjacent Concepts. Three architectural concepts— loose coupling, accidental coupling, and architectural drift—are nomologically proximate but conceptually distinct from our conceptualization of silence. They are architectural properties, whereas silence is a system’s behavior. Architecture can influence behavior, but it does not, by itself, constitute behavior. Our model preserves this crucial distinction while assimilating these causally upstream insights. Table 2 summarizes these.

a. Loose coupling. Silence is nomologically proximate yet differs conceptually from loose coupling (e.g., Subramanyam et al. 2012). Although loose coupling describes structural independence among modules, silence characterizes their actual interaction behavior.<sup>5</sup> Loose coupling circumscribes—nondeterministically— interaction behavior among modules. Loosely-coupled modules can be chatty (e.g., in REST (Representational State Transfer) APIs (application programming interfaces) or event-driven systems), while tightly-coupled modules can be silent (e.g., error-handling modules that rarely activate). Consider social platforms like Slack, streaming services like Spotify, and cloud systems like Gmail; all feature loosely-coupled modules that exchange high volumes of data through APIs.

Conversely, automotive systems contain tightlycoupled modules that run briefly at start-up and then, remain silent.<sup>6</sup> As a system evolves, loosely-coupled modules might become chatty, and tightly-coupled modules might go silent. Loose coupling makes silence more likely but does not guarantee it. This positions loose coupling causally upstream to silence in our theory in Figure 1. Only Goren and Moses (2020) previously used the term “silence,” but they used it differently—to formalize a theorem for information transfer through noncommunication.

b. Accidental coupling. Silence differs from “accidental coupling” (Abgaz et al. 2023) or “possible dependencies” (Jin et al. 2022), which emerge from unrecorded structural dependencies from dynamic-typed code and design violations. In dynamic-typed code, the variable type is determined at run time rather than compile time; we eliminate this confound by focusing exclusively on a static-typed language.<sup>8</sup> Design violations occur when implementation actions deviate from design intentions— for example, when expedient shortcuts and patchwork across modules create technical debt (Rolland et al. 2018).<sup>9</sup> Such structural coupling is an architectural attribute that can lead to reducing silence but itself is not silence—a downstream behavior. Refactoring curbs such architectural degradation (Aiomar et al. 2024), which is controlled in our analysis.

c. Architectural drift over time. Recent IS work shows systems’ behavior diverging from architectural expectations, revealing unexpected module interactions (Lindberg et al. 2016) and new or vanishing interactions as they evolve (Fu¨ rstenau et al. 2023, Tiwana and Safadi 2024). As systems drift, silent codebases may grow chatty, and chatty ones may go silent.

Although silence shares conceptual space with these adjacent concepts, as a behavior rather than an architectural property that they represent, it provides a new lens for how systems actually behave.

## 2.3. Conceptualization of Silence

Literally, silence means refraining from talking. Building on Simon, we define silence as the relative absence of observable interaction behavior among a system’s mod ules. In software, silence manifests as reduced traffic (e.g., fewer calls and lesser data flow) among its modules. Practitioners implicitly advocate for silence when advocating that systems minimize data passed between modules (e.g., Richards and Ford 2020, p. 127). The opposite is a chatty system, exhibiting extensive interaction behavior among modules to achieve system functionality (Richards and Ford 2020, p. 110). Silence and chatti ness form a continuum, with silence being a location on it.

Silence is a system-wide property that describes the interaction behavior among its modules. Unlike interaction among human developers, interaction among modules entails one module invoking functionality in other modules or passing data to them. Since one module might invoke another but not the other way around, silence halves when an interaction between two modules goes from unidirectional (� → � call) to bidirectional (� ↔ � call).<sup>10</sup> As silence increases, interactions among modules decrease.

Table 2. Silence vs. Three Adjacent Concepts

<table><tr><td>Concept</td><td>Software Engineering</td><td>Information Systems</td><td>Idea</td></tr><tr><td>Loose coupling</td><td>●</td><td>●</td><td>Modules independent of others&#x27; internal implementation</td></tr><tr><td>Accidental coupling</td><td>●</td><td>○</td><td>Discrepancy between design intentions and implementation actions</td></tr><tr><td>Architectural drift</td><td>○</td><td>●</td><td>Behavior diverges from architectural expectations</td></tr></table>

Note. •, Extensively studied; �, somewhat studied.

Figure 3 contrasts two systems with four modules (�), one more silent (left) and one chattier (right). In realizing the system’s functionality, modules in the silent system invoke each other far less than in the chattier one. A system’s architecture can affect silence—but nondeterministically—as it evolves over time. Consequently, as a system evolves, we can have a chatty system despite loosely-coupled modules or a silent system despite tightly coupled modules.

2.3.1. Java Code Illustration. Figure 4 illustrates this idea using two modules (p1 and p2), containing classes A and B, with their code underneath (files A.java and B.java). Panel (a) of Figure 4 shows two uncoupled modules exhibiting silence as expected. Panel (c) is two tightlycoupled modules that are chatty as expected. Here, A invokes B and module p1 invokes p2 using a Java import statement. Behavior deviates from architecture in panels (b) and (d). Panel (b) shows loosely-coupled modules being unexpectedly chatty because class A uses B without an explicit module-level invocation (import). Panel (d) shows tightly-coupled modules being unexpectedly silent as p1 invokes p2 through an import statement, but this import is unmaterialized in actual class usage. This architecture-behavior divergence is more apparent in systems that have evolved over some time, which is why we subsequently examine such systems.

2.3.2. Silence’s Conceptual Value. Silence’s unique theoretical value added is twofold. First, it directly taps into evolving, observable system behavior, which

Figure 3. (Color online) A Contrast of a Silent (Left Panel) vs. a Chatty (Right Panel) System Composed of Four Modules (�)

![](/api/attachments/JWJP7MBA/fulltext/images/bcd6af9c243d066385d5da0e3117cc20330dcb80790d333f86fb3c7b7edc1b42.jpg)

software engineering scholars describe as understudied and atheoretical (Rahwan et al. 2019, Jin et al. 2022). The urgency to understand the evolving behavior of systems is because they become brittle over time, distributed designs make brute-force countermeasures untenable, and autonomous systems heighten concerns about unpredictable behaviors. Second, it rekindles the underappreciated emphasis on silence as a system behavior in Simon (1962). Like Simon, Smith (1981, p. 54) also emphasized that grasping a complex artifact demands understanding the interaction behaviors within it; these change over time as IT systems evolve. Our conceptualization acknowledges architecture’s essential yet nonde terministic role in shaping system behavior, broadening the theoretical discourse beyond architecture that predominates while cumulatively building on it. This later allows for counterfactually exploring the “what-if” generativity consequences of chattiness where silence is expected and silence where chattiness is anticipated.

## 2.4. Attention Funneling

Attention literally means focusing the mind on something. Simon defines attention as the set of elements that enter into consciousness at any given time, elements to which effort is directed (Van Knippenberg et al. 2015, Tonellato et al. 2024). Funneling literally means to channel to a focal point. Attention funneling then is the channeling of the team’s effort to some subset of the system-wide codebase, such as a module.

We define attention funneling as the degree to which a project team temporarily concentrates its code changes on fewer modules of a system. Although modularity enables individual developers to focus on a specific segment of a system’s codebase, attention funneling dynamically coalesces team-wide effort on a narrow sliver, such as a module or a file. This transient concentration shifts over time to different slivers of the codebase. Although silence characterizes how code artifacts behave, attention funneling characterizes how team members collectively behave.

Our conceptualization differs from attention concepts in management and software engineering by being both dynamic—as attention shifts between modules from one period to the next—and inward focused within teams.<sup>11</sup> Like the emphasis in Harvey (2014, p. 332) on dynamic team processes, attention funneling evolves over time to create what she describes as deep collective engagement, reflecting different knowledge types’ distinct attention needs (Zhang et al. 2024). It is a team-level analog to the idea of March and Simon (1958, p. 154) of narrowing individuals’ attention spans, recognizing that attention operates simultaneously at individual and team levels (Zhang et al. 2024). Unlike outward-focused narrowing of attention of organizations in management, inward narrowing of attention of teams is akin to switching from a wide lens to a macro lens.

Figure 4. (Color online) Loosely-Coupled Modules Can Be Chatty (Panel (b)), and Tightly-Coupled Ones Can Be Silent (Panel (d)), Although We Would Expect Loosely-Coupled Modules to Be Silent (Panel (a)) and Tightly-Coupled Ones to Be Chatt (Panel (c))  
![](/api/attachments/JWJP7MBA/fulltext/images/0cdfa22f46d086af2b2624f2797d9f81e7bdf07fefbff0f06ceab646c839e5cc.jpg)

Funneling attention translates into developers collectively concentrating effort on fewer modules, whereas its opposite—attention scattering—splinters effort across the codebase. Figure 5 contrasts this using two threeperson (�) teams working on three modules (�) in a codebase. The team in the left panel shows funneled attention with all members focused on one module, whereas the one in the right panel has scattered attention. Attention funneling mirrors the individual-level Zen practice of Shikantaza (只 管 打 坐 ) at the team level: a heightened state of concentrated awareness. It characterizes human developers’—not a system’s modules— collective behavior.

## 2.5. Hypotheses

2.5.1. How Attention Funneling Shapes IS Generativity. IS generativity broadly refers to a system’s capacity for doing new things (Vial 2023). Recent IS studies conceptualize generativity as emerging both from and within a system, although they diverge on whether agency resides with external third parties or the original develo pers. From-system generativity refers to a system spawning innovations via the uncoordinated third-party actors independent of its originators (Yoo et al. 2010, Fu¨ rstenau et al. 2023), such as when forking creates derivative sys tems. Systems can also experience degenerative change that degrades quality (Fu¨ rstenau et al. 2019). Within system generativity encompasses internal changes, measured through its rate of change and new version releases (Tiwana 2015, Vial 2023). We will, therefore, cast a wide empirical net spanning all four conceptualizations of generativity from (forking and degenerativity) and within (evolution rate and releases) systems.<sup>12</sup>

Figure 5. (Color online) A Team with Attention Funneled (Left Panel) vs. Attention Scattered (Right Panel)  
![](/api/attachments/JWJP7MBA/fulltext/images/e854f6889f6890795a23f775f8da8baf0b14728ce52c1747676a8cbcaeb00111.jpg)  
Note. � indicates modules, and � indicates developers.

Recent IS generativity studies suspect that misallocating attention has repercussions, emphasizing cues for developers to focus future effort (Fu¨ rstenau et al. 2019, p. 1322). Our focus on the attention-funneling mechanism stems from the cognitive load of tracking module interactions on individual developers’ finite attention as they coalesce development effort. Realizing IS generativity thus depends heavily on how teams allocate their attention across the system. When individual developers attention is scattered across multiple modules, consensus building on future development priorities becomes difficult (Fu¨ rstenau et al. 2019, Tonellato et al. 2024). This dispersion of effort impedes the team’s ability to realize focused, high-quality code changes within discrete modules during each development period. Consequently, the team struggles to produce sufficiently valuable code for generative extension by other developers (Vial 2023) while simultaneously risking codebase degradation.

Conversely, when all developers in a team temporarily concentrate their effort on fewer modules, they make more tangible progress. Allocating attention drives groups’ productivity (Van Knippenberg et al. 2015). Team fixation on specific codebase slivers indicates consensus on development priorities, increasing the likelihood of realizing envisioned code changes (Tonellato et al. 2024). This focused development effort leads to higher-quality, release-worthy code that other developers can build on while also curbing codebase degradation—both key aspects of from-system generativity. Coalesced team-wide effort enables expedient implementation of code changes and fulfillment of future development commitments, improving both the evolution rate and release frequency aspects of withinsystem IS generativity (Tiwana 2015; Richards and Ford 2020, p. 116). Overall, funneling of team-wide attention helps extend systems’ functionality beyond their original design. We, therefore, expect it to enhance overall IS generativity.

Hypothesis 1. Attention funneling enhances IS generativity.

2.5.2. How Silence Shapes Team-Wide Attention. With greater silence among a system’s modules, changing one module requires fewer simultaneous adjustments elsewhere (Simon 1962). It frees up team members’ scarce attention that would otherwise be allocated to tracking modules’ interactions (Harvey 2014; Fu¨ rstenau et al. 2019, p. 1322). Zhang et al. (2024) showed that different types of knowledge require different attention patterns, and silence enables teams to match their cognitive focus to development priorities, which is difficult in chatty systems where multiple module interactions compete for attention.

With higher silence, a team can focus collectively on one salient module at a time in relative isolation, achieving the deep collective engagement in Harvey (2014, p. 332), without needing time-consuming iteration to preserve interoperability with other modules. This allows the whole project team to temporarily focus its development effort on a sliver of the codebase (Van Knippenberg et al. 2015, Tonellato et al. 2024). Individual developers in the project team can thus pay more attention to fewer modules on average, consistent with the attention allocation ideas developed in Section 2.4.

In contrast, a chattier system requires tracking how even a single change in one module affects other mod ules in the system’s codebase. Multiple modules then simultaneously compete for team members’ scarce attention (Simon 2002), scattering team attention. We, therefore, expect greater silence among the system’s modules to enhance the funneling of its project team’s attention.

Hypothesis 2. Silence inside a system enhances funneling of its project team’s attention.

2.5.3. Mechanism. Silence breeds IS generativity by shaping how teams collectively engage with the system’s codebase. It creates conditions to coalesce team-wide attention (Van Knippenberg et al. 2015, Fu¨ rstenau et al. 2019), which in turn, improves generative outcomes. Because attention operates simultaneously at individual and team levels (Zhang et al. 2024), attention funneling serves as the connective mechanism to coalesce individual developers attention into team-level effort concentrated on one sliver of the codebase at a time. Rather than directly causing generativity, silence influences team attention allocation patterns (Section 2.5.1), which subsequently foster generative outcomes (Section 2.5.2). Thus, attention funneling mediates the effect of silence on IS generativity.

Hypothesis 3. Attention funneling mediates the influence of silence on IS generativity.

## 3. Methods

We used bleeding-edge trace analysis with data streams collected as part of the Open Knowledge Relics Archaeology (OKRA) initiative. OKRA is a larger, decade-long research program studying IT evolution using opensource digital relics and using supercomputing-driven induction as a form of digital archeology (Tiwana and Safadi 2024). Trace data are longitudinal field data collected in source-code management systems over the course of development activities. We assembled time-series records spanning each system’s lifespan (Salganik 2017, p. 26). Like frames in a video, these quarterly snapshots captured both module-to-module and developer-to-module interaction behaviors. This approach enabled the type of causal inference (Rahwan et al. 2019, p. 478) advocated to understand interaction behavior inside systems. Figure 6 shows ou timeline.

To mitigate confounding because of programming languages, dynamic typing, and heterogeneity in how systems’ modules interface, we focused exclusively on

Figure 6. Correspondence of Our Data Timeline with Theoretical Causal Ordering  
![](/api/attachments/JWJP7MBA/fulltext/images/623d86418ff8a8ac6547b8ea8845214bcd3f2f35bd61c82fdeb8e13585c22689.jpg)

Java-language systems. Such narrowing of context permits more precisely disentangling the mechanism at work (Ashworth et al. 2021, p. 6). Modules (called packages) in a Java system interact in highly standardized ways.<sup>13</sup> Java uses static typing, thus mitigating confounding by dynamic typing (wherein the type of a variable is determined at run time rather than at compile time, such as in Ruby and Python) that impedes maintainability (Aiomar et al. 2024).

From GitHub’s 46.7 million projects database, we randomly sampled 1,356 Java projects that met four winnowing criteria: (a) coded in Java; (b) actively developed (defined as at least a monthly code commit over the preceding five-year window); (c) original (nonforked) systems; and (d) nonprivate, open-source repositories. Using GitHub standardized the development environment, whereas open source permitted constructing quarter-century data streams implausible with proprietary systems. We analyzed in each system’s source code every line of code that ever existed, every change, the location of every file, and every module in each system that it affected over a quarter of a century (1996–2016 plus another five years for our generativity outcomes).<sup>14</sup>

Using a supercomputing cluster, we analyzed 274 million lines of source code and comments spanning 1.4 million files in 194,105 modules, with 9.7 million dependencies, 19.8 million commit records, and 7,200 developers—approximating 163,000 issues (40,000 years) of Information Systems Research. We assembled quarterly snapshots into 1,356 time-series trace data streams. This balances observing silence with preempting confounds while remaining computationally feasible as a quarterly window consumed several weeks of supercomputer processing time. We wrote a custom source-code analyzer to extract different networks from each project and used the NetworkX Python package (networkx.org) to construct a triad of 22,534 networks—system-wide module-to-module for silence, developer-to-module linkages for attention, and file-to-module for instruments— for every system spanning 83 quarters. Following Cunningham (2021, p. 94), this aggregates granular microdata to the higher system level as trace data streams composed of a long time series of short observation intervals.

## 3.1. Measures

We measured all constructs using data accreted from reconstructing for every observation interval the digital fingerprints that developers left behind in their code changes over each system’s lifetime. We leveraged Java systems’ organization as modules, each with a unique folder containing .java source-code files. Dependencies among two files in different folders are module-tomodule dependencies. We focused only on systemnative modules, excluding imports from the Java library and external modules. We analyzed every line of this source code for each system in every quarter, which was the input for our novel social-network measures unlike any used in software engineering. Table 1 summarizes the measures for our theoretical constructs, instruments, and controls.

3.1.1. Silence. For silence, we constructed 22,534 codebase silence networks of every module-to-module invocation across a system’s codebase, one for each system for every quarter. We focused on the two primary object-oriented module-to-module dependencies: class composition and class inheritance. A file in a Java codebase represents at least one class. If one class invokes or inherits from another class, an interaction dependency exists between the two files of the two classes. We tallied dependencies between files in different modules to compute module-to-module chattiness. We also robustly replicated all models at a more granular file level using method calls between files rather than modules.<sup>15</sup>

Following Figure 3, silence equals one minus the density of the module-to-module interaction network for an entire system’s codebase. This converts density to spar sity, transforming chattiness to silence. In Java, one directed link from module A → B exists when module A invokes (in Java lingo, “imports”) module B. If it also invokes in reverse (A ← B), it adds another link. We aggregated this count of module-to-module interactions for each system’s native modules in every quarter to estimate density. The lower this density, the higher the silence among a system’s modules. It ranges from zero (where every possible module-to-module interaction exists) to 100% (where no modules talk). Aggregating this creates a system-wide measure for the intensity of module-to-module interaction behavior. Unlike software engineering’s static, granular file/module measures, our novel social-network analyses of code artifacts capture dynamic system-wide behavior of evolving modules’ interactions, complementing recent OKRAbased IS work on architectural changes over time (e.g.,

Tiwana and Safadi 2024):

$$
\begin{array}{l} \text {Silence} _ {\mathrm{t}} = \{1 - \{(\# \text {module-to-moduleinvocations} _ {\mathrm{t}}) \\ \div ((\# \text {modules} _ {\mathrm{t}}) \times (\# \text {modules} _ {\mathrm{t}} - 1)) \} \}. \end{array}
$$

Figure 7(a) visualizes silence inside one sampled system—autopsy (github.com/sleuthkit/autopsy)—in one quarter (the last quarter of 2011); the hollow circles (�) are modules, and the arrows (→) are calls among modules (�). It had high silence (0.7) in this observation window.

The appendix illustrates our strategy for inferring silence from the Java source code of an enterprise application with three modules. It also shows how silence and loose coupling can vary independently. The code snippets and Figure 7 highlight the relationship between method invocation and import statements. To compose the functionality of the application, some modules need to invoke code from other modules using the “import” statements that we used to measure the intensity of module-to-module interactions.

3.1.2. Attention Funneling. We measured attention funneling as developers’ focus on fewer modules in each quarter assessed using system-wide developer-to-file networks whose links represent code commits. The fewer the modules on which their commits are concentrated in an interval, the more funneled is the team’s attention.<sup>16</sup> We then estimated this network’s Freeman centralization, which is the difference between the most central node and other nodes in this network of commits each quarter, measuring team-wide attention. These developer-to-module interactions evolve across observation windows, tapping into evolving human developerwith-code artifact interactions:

$$
\begin{array}{l} \text {Attention funneling} \\ = \left\{\sum_ {d \in \text {developers}} (\max _ {\nu \in \text {developers}} (c e n t r a l i t y (\nu)) - c e n t r a l i t y (d)) \right\} \div \# \text {developers.} \end{array}
$$

Higher centralization indicates that developers collectively focus commits to fewer modules, reflecting teamwide attention funneled to fewer modules in a system’s codebase. Like our silence networks for module-tomodule interaction behaviors, we constructed 22,534 such attention-funneling networks, each capturing every human developer-to-file relationship from each system’s codebase commit history list for every quarter.

Figure 7(b) visualizes attention funneling in the same sample project as in Figure 7(a). It had low attention funneling (0.2) as indicated by the arrows (→) representing code commits by different developers (�) to files in different modules (�) (Figure 7(b)). Thus, developers code changes were concentrated on fewer files (which are nested in fewer modules in a Java codebase). To recap, silence means less aggressive invocation behavior across modules in a codebase; attention funneling means that commits went to fewer modules.

3.1.3. Generativity. The narrowest conception of generativity is a system changing through unfiltered contri butions from broad, varied audiences, whereas the broadest conception encompasses external, third-party modifications, technical improvements, and resistance to degenerative forces. The literature is also theoretically ambiguous about whether generativity stems from third-party modifications or from original developers actions. Reflecting this ambiguity, we used four different measures to cover the entirety of plausible generativity manifestations. The first most direct one was the lifetime-cumulative count of codebase forks measured five years beyond $\mathbf { t } _ { 3 }$ (the end of the first quarter of 2021; codebase generativity) (Fu¨ rstenau et al. 2023, Vial 2023). Developers who fork a codebase as a foundation for derivative systems are the users of the codebase itself, analogous to end users of a compiled system. Following the logic of Fu¨ rstenau et al. (2023) for growth in a sys tem’s users as generativity, we counted lifetime forks to measure codebase generativity. Of our four metrics, our stance is that the true hallmark of IS generativity is such developer-independent extension by external third parties, which cleanly separates it from other evolutionary outcomes. We complemented this with a lagged mea sure of codebase quality degradation to measure degener ativity (Fu¨ rstenau et al. 2019) using a lagged count variable of the number of cyclomatically complex lines of code at $\mathrm { t } _ { 3 } .$ These covered from-system generativity. We complemented these with within-system generativity quantified as change internal to a system’s codebase as evolution rate measured at $\mathrm { t } _ { 3 }$ as the count of quarterly code commits. This follows the emphasis on system adaptation in Vial (2023). Because more code changes alone might not suffice to produce release-quality outcomes, we complemented it with release cadence, measured five years after $\mathrm { t } _ { 3 }$ as the cumulative lifetime count of new releases of the whole system (Richards and Ford 2020, p. 116). Generativity and release cadence were lifetime-cumulative measures lagged for an additional five years beyond $\mathrm { t } _ { 3 } ;$ evolution rate and cyclomatic com plexity were measured quarterly $\left( \mathrm { { t } } _ { 3 } \right)$

3.1.4. Instruments. We constructed our three instruments—loose coupling, hierarchical depth (Chidamber and Kemerer 1994), and module coarseness (Subramanyam et al. 2012)—by also analyzing each system’s codebase every quarter. These are each system’s architectural properties—its modules’ coupling, nesting, and scope—discussed later in Section 4.1, which Figure 10 visually illustrates.<sup>17</sup> They are time-variant, systemwide properties recomputed for every quarter, creating 22,534 networks similar to the silence and attention ones but using file-to-module linkages. This mitigated

Figure 7. (Color online) Examples of One of 22,534 Supercomputational Silence (Above) and Attention Funneling Networks (Below) Constructed  
![](/api/attachments/JWJP7MBA/fulltext/images/abdc3609247d194bc0997d8aefef4093e663ba5d576b08dd0720706c7e2108b9.jpg)

(b)  
![](/api/attachments/JWJP7MBA/fulltext/images/2daf7fa3f54f775192ecf165631b527e008d44f19173ab48a4d8eb7fe262e383.jpg)  
Notes. (a) An illustration of 1 of 22,534 measurement networks constructed for each quarter for each system to estimate silence among modules ( ) in a system. (b) An illustration of 2 of 22,534 measurement networks constructed for each quarter for each system to estimate attention funneling of developers (�) in a project team. This is for the same system as in panel (a) but is a developer-to-module (� → �) network.

bleeding into our silence measure. We measured loose coupling as the sparsity of the file-to-module network reflecting the boxes-within-boxes metaphor with near independence between the boxes. In Java, files representing classes and interfaces are organized within packages representing modules. The sparsity of this containment network indicates that a system is composed of relatively independent modules (range from zero to one). Hierarchical depth was the average shortest-path length in the file-to-module network in each system’s entire codebase in every quarter; larger values indicate a deeper codebase hierarchy. Module coarseness was the centralization <sup>a</sup>Cumulative through t + 5 years; all other variables are panel data on a system-quarter basis. <sup>b</sup>Million lines of code. \*p < 0.01.

of the file-to-module network. High centralization implies that few modules implement most functions on which various classes depend; it ranged from 0.5 to 12.15 in our nonnormalized data.

## 3.2. Descriptive Statistics and Patterns of Attention and Silence over Time

Table 3 shows low correlations among loose coupling, silence, and attention funneling in our panel data, confirming their distinctiveness (instruments are shaded). Systems in the fourth quarter of 2016 averaged 4.75 (σ � 2.96) years in age, with 6 (σ � 8.9) developers making 537 $( \sigma = \dot { 1 } , 1 0 6 )$ quarterly changes to 241 (σ � 465) files. Systems had 1,181 (σ � 1,611) files organized into 143 (σ � 193) native modules with 7.44 (σ � 13.2) million lines of code and documentation; their modules invoked each other 7,190 (σ � 10,377) times. As of 2021, lifetime fork counts averaged 323 (σ � 1,456), with 7.9 (σ � 11.8) major releases. Stationarity tests using the xtunitroot procedure in Stata confirmed that at least one panel is stationary. Codebase files to which attention was funneled changed 90.7% (σ � 11.6%) from one quarter to the next, confirming highly dynamic attention funneling. The shifts over time in median silence and attention funneling in Figure 8 show that they go hand in hand.<sup>18</sup> Silence degraded as a system crossed the 15-year mark (60 quarters), scattering attention along with it. We speculate that many systems reached their end of life in about 15 years.

The crosscorrelogram in Figure 9 further shows that silence precedes attention funneling by one to three quarters, with no reverse relationship. This underscores our causality argument that prior silence affects the current attention funneling, and attention today is not associated with future silence. Granger-causality tests confirm that silence causes attention funneling $( \chi ^ { 2 } =$ 5.21, $p < 0 . 0 0 1 )$ , but attention funneling does not cause silence $( \chi ^ { 2 } = 0 . 0 6 3 , \mathrm { n } . s . )$ . Further, silence consistently and robustly precedes attention changes. Silence and atten tion funneling are, therefore, causally related.

3.2.1. Rival Explanations. Our fixed effects model holds constant time-invariant system and team properties, which are the bulk of rival explanations in prior studies. We controlled for time-variant (a) code volume (Subramanyam et al. 2012), (b) module count, (c) system age (Fu¨ rstenau et al. 2019), and (d) team size from prior studies. We reestimated them for every quarter. Module count is Simon’s (1962) span of a system, which is the number of subsystems that a system’s codebase is parti tioned into. Greater code volume (measured as the logged codebase line count measured in millions (Subramanyam et al. 2012)) has more plausible instances for code change and thus, higher generativity. With increasing system age, accumulation of technical debt and changes in its surrounding infrastructure impede changes (Rol land et al. 2018), lowering generativity. More developers actively changing the codebase (team size) provides more manpower to refine code, for which we counted the number of unique developers committing code in each quarter. Finally, rationalizing the codebase through architecture refactoring (Aiomar et al. 2024) (proxied as the ratio of files that differ from the preceding quarter<sup>19</sup>) can reduce its complexity to bolster generativity. This accounts for recent software engineering advances in accidental coupling and possible dependencies (e.g., Jin et al. 2022, Abgaz et al. 2023). Stage 3 in Table 4 shows that four of the five controls were significant.

## 4. Analysis

Our unit of analysis is a system. Our trace data are longitudinal, criterion variables are count based, and our predictor is likely endogenous. To isolate the effect of silence on attention funneling, we accounted for the endogeneity of silence and for time-variant rival explanations of generativity. Our model’s focus on the effects of withinsystem silence on generativity makes within-system analysis appropriate.

Table 3. Construct Correlations and Psychometric Properties

<table><tr><td>Construct</td><td> $\overline{x}$ </td><td> $\sigma$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>1. Silence</td><td>0.93</td><td>0.10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Attention funneling</td><td>0.42</td><td>0.15</td><td>0.09*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Degenerativity</td><td>27,140.4</td><td>50,400</td><td>0.23*</td><td>0.14*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Evolution rate</td><td>784.9</td><td>2,208</td><td>0.11*</td><td>0.03*</td><td>0.2*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Release cadencea</td><td>7.60</td><td>11.7</td><td>-0.12*</td><td>0.00</td><td>-0.07*</td><td>-0.02*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Codebase generativitya</td><td>365.20</td><td>1,376.3</td><td>0.01</td><td>0.06*</td><td>0.01</td><td>0.03*</td><td>0.21*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. Loose coupling</td><td>0.98</td><td>0.05</td><td>0.38*</td><td>0.15*</td><td>0.16*</td><td>0.08*</td><td>-0.044*</td><td>0.02*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. Hierarchical depth</td><td>3.61</td><td>0.91</td><td>0.54*</td><td>0.13*</td><td>0.23*</td><td>0.09*</td><td>-0.14*</td><td>-0.02*</td><td>0.43*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. Module coarseness</td><td>0.57</td><td>0.23</td><td>0.48*</td><td>0.08*</td><td>0.24*</td><td>0.08*</td><td>-0.13*</td><td>0.01</td><td>0.31*</td><td>0.51*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. Code volumeb</td><td>6.49</td><td>11.14</td><td>0.26*</td><td>0.17*</td><td>0.93*</td><td>0.21*</td><td>-0.09*</td><td>0.01</td><td>0.18*</td><td>0.28*</td><td>0.28*</td><td></td><td></td><td></td><td></td></tr><tr><td>11. Module count</td><td>118.7</td><td>172.9</td><td>0.34*</td><td>0.2*</td><td>0.57*</td><td>0.21*</td><td>-0.13*</td><td>0.01*</td><td>0.2*</td><td>0.47*</td><td>0.36*</td><td>0.7*</td><td></td><td></td><td></td></tr><tr><td>12. System age (years)</td><td>3.26</td><td>2.89</td><td>0.21*</td><td>0.12*</td><td>0.26*</td><td>-0.01*</td><td>-0.02*</td><td>0.04*</td><td>0.17*</td><td>0.16*</td><td>0.20*</td><td>0.27*</td><td>0.27*</td><td></td><td></td></tr><tr><td>13. Team size</td><td>5.56</td><td>6.54</td><td>0.21*</td><td>0.21*</td><td>0.32*</td><td>0.28*</td><td>-0.00</td><td>0.22*</td><td>0.15*</td><td>0.22*</td><td>0.20*</td><td>0.37*</td><td>0.43*</td><td>0.11*</td><td></td></tr><tr><td>14. Architecture refactoring</td><td>0.36</td><td>0.32</td><td>-0.15*</td><td>-0.02*</td><td>-0.18*</td><td>0.18*</td><td>0.07*</td><td>0.03*</td><td>-0.15*</td><td>-0.12*</td><td>-0.16*</td><td>-0.2*</td><td>-0.19*</td><td>-0.33*</td><td>0.02*</td></tr></table>

Note. Shaded rows are instruments (Lines of Code).

Figure 8. Shifts over Time in Silence and Attention Funneling  
![](/api/attachments/JWJP7MBA/fulltext/images/6199fa733ea9ae672b19fd2d0baa749da2d77f0cc790ffd3c811f52cf2f32a13.jpg)

Three tests led us to fixed effects using heteroskedasticity-mitigating robust standard errors (Cunningham 2021, p. 77). A significant Hausman test $\dot { ( \chi } ^ { 2 } =$ $2 . 7 \bar { 7 } , p < 0 . 0 0 1 )$ led us to fixed effects over random effects, simultaneously eliminating time-invariant rival explanations. Our data were heteroscedastic $( \chi ^ { 2 } = 1 . 5 \mathrm { e } + \dot { 0 6 } , p <$ 0.001; rejected the null of homoskedasticity) and autocorrelated $( F _ { \mathrm { W o o l d r i d g e } } = 1 9 . 7 6 , p < 0 . 0 0 1 _ { \mathrm { \Omega } }$ ; rejected the null of zero autocorrelation).

We used a three-stage model using xtivreg2 in Stata 16: (1) the two-stage least squares (2SLS) silence model with instruments predicting silence, (2) the 2SLS attention model using silence from stage 1 predicting attention funneling, and (3) the negative binomial generativity model using predicted attention from stage 2 plus controls. Table 4 shows the results.

## 4.1. Stage 1 (Silence Model): Endogeneity of Silence Inside a System

Silence is likely endogenously shaped by a system’s architecture, reflecting its architectural roots. Rahwan et al. (2019, p. 480) singled out systems’ architecture—the internal arrangement of its modules by its designers— affecting its behavior. Lacking empirical precedent, we used three architectural system attributes in Figure 10 as theoretically guided instruments: ‹ loose coupling, hierarchical depth, and fi module coarseness. They address omitted variables bias crucial for causal infer ence (Cunningham 2021, p. 11) while recognizing the causally upstream roots of silence in systems’ heteromorphic architectures. This approach assimilates prior architectural studies (e.g., coupling, nesting (Chidamber and Kemerer 1994), and granularity (Subramanyam et al. 2012)) into our downstream systems behavior. Loose coupling among a system’s modules increases silence by lowering modules’ need to interact. Hierarchical depth— how many layers deep the module-to-subordinate module relationships run—ranges from flat to deep

Figure 9. Crosscorrelogram of the Association of Attention Funneling and Lagged Silence over Time  
![](/api/attachments/JWJP7MBA/fulltext/images/bd3b16b21932ef0ea15fc7f83c32df995e181ca9d37726a74bc4d92c26b90157.jpg)

Table 4. Results

<table><tr><td rowspan="4">Model →StageInstruments</td><td rowspan="3">SilenceStage 1</td><td rowspan="3">AttentionStage 2</td><td colspan="4">Generativity (incidence response ratios)</td></tr><tr><td colspan="4">Stage 3</td></tr><tr><td rowspan="2">Codebase generativitya</td><td rowspan="2">Degenerativityt3</td><td rowspan="2">Evolution rate t3</td><td rowspan="2">Release cadencea</td></tr><tr><td>Silencet1</td><td>Attention funnelingt2</td></tr><tr><td>Loose couplingt0</td><td>0.13** (3.19)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hierarchical deptht0</td><td>0.02*** (15.71)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Module coarsenesst0</td><td>0.05*** (16.46)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Endogenous predictor</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Silence $_{ij-t1}$ </td><td></td><td>0.48*** (8.00)</td><td>0.06 (-1.85)</td><td>9.21*** (22.67)</td><td>1.22* (2.10)</td><td>0.20 (-1.93)</td></tr><tr><td>Mediator</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Attention funneling $_{ij-t2}$ </td><td></td><td></td><td>616.87*** (6.36)</td><td>0.50*** (-4.85)</td><td>1.98*** (5.08)</td><td>3.68* (2.08)</td></tr><tr><td>Controls</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Code volumet2</td><td></td><td></td><td>1.00 (0.22)</td><td>1.00*** (24.16)</td><td>1.00 (-0.94)</td><td>1.00 (-0.80)</td></tr><tr><td>Module countt2</td><td></td><td></td><td>1.00** (-3.15)</td><td>1.00*** (12.50)</td><td>1.00 (-0.01)</td><td>1.00** (-2.78)</td></tr><tr><td>System aget2</td><td></td><td></td><td>1.10** (3.26)</td><td>1.08*** (66.48)</td><td>0.97*** (-12.26)</td><td>1.01 (0.43)</td></tr><tr><td>Team sizet2</td><td></td><td></td><td>1.11*** (7.56)</td><td>1.01*** (24.28)</td><td>1.03*** (28.41)</td><td>1.02** (2.82)</td></tr><tr><td>Architecture refactoringt2</td><td></td><td></td><td>0.69 (-1.26)</td><td>0.79*** (-22.51)</td><td>1.65*** (26.21)</td><td>1.18 (0.84)</td></tr><tr><td>N</td><td>22,534</td><td>22,534</td><td>1,180</td><td>21,299</td><td>20,805</td><td>1,180</td></tr><tr><td> $\chi^2$ </td><td></td><td></td><td>150.39</td><td>24,348.02</td><td>2,255.89</td><td>37.94</td></tr><tr><td>Model F (log likelihood)</td><td>286.45***</td><td>63.96***</td><td>(-6,668.61)</td><td>(-198,555.86)</td><td>(-137,909.21)</td><td>(-3,002.08)</td></tr></table>

Notes. Stages 1 and 2 are two-stage least squares linear regression coefficients; stage 3 is incidence response ratios for the negative binomial regression model. The t statistics are in parentheses. Shaded cells are hypothesis tests.  
<sup>a</sup>Cumulative through $\mathrm { t } _ { 3 } + 5$ years.  
\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

hierarchies (Simon 1962, p. 468; depth of trees in code hierarchy in Chidamber and Kemerer 1994). Flatter hierarchies make most modules peers in a system’s hierarchy, requiring greater interaction (Simon 1962, p. 469), and deeper hierarchies thus increase silence. Finally, as Figure 10 illustrates, a system can have a mix of smaller, fine-grained modules and larger, coarse-grained modules. Module coarseness—how large the average module in a system is (Subramanyam et al. 2012)—mirrors Simon’s (2002) notion of a system being composed of larger subsystems. Larger modules contain more functionality internally, reducing crossmodule traffic compared with smaller modules that must interact more with other modules to accomplish system functions (Richards and Ford 2020, p. 110). Therefore, silence increases with coarser modules. Instruments should influence silence but not directly affect attention funneling. Our instruments satisfy this conceptual requirement because they affect how modules with a system interact but are unlikely to directly affect how members within the project team direct their attention. Equation (1) shows the stage 1 model. Stage 1 in Table 4 shows that all three instruments were significant:

Figure 10. (Color online) Three Attributes of System Architecture from Prior Research—‹ Loose Coupling, › Hierarchical Depth, and fi Module Coarseness—Can Endogenously Shape Silence Inside a System  
![](/api/attachments/JWJP7MBA/fulltext/images/23229882e10e896ec1fe5fcb6c429833f55601c29f98b94d493ad8652c1d4d90.jpg)  
Note. � indicates modules.

$$
\begin{array}{c} \text {Silence} _ {\mathrm{t1}} = \alpha_ {0} + \alpha_ {1} \text {loose - coupling} _ {\mathrm{t0}} \\ \qquad + \alpha_ {2} \text {hierarchical depth} _ {\mathrm{t0}} \\ \qquad + \alpha_ {3} \text {module coarseness} _ {\mathrm{t0}} + \varepsilon . \end{array}\tag{1}
$$

4.1.1. Model Identification. Our instruments satisfied the relevance criterion of high correlations with silence $( r _ { \mathrm { l o o s e - c o u p l i n g } } = 0 . 3 6 ,$ r<sub>hierarchical</sub> $\mathrm { d e p t h } = 0 . 5 1$ , and $r _ { \mathrm { m o d u l e } }$ � 0.45, all $p < 0 . 0 0 1 )$ ) and the exclusion restriction of low correlations with attention $( r _ { \mathrm { l o o s e - c o u p l i n g } } = 0 . 0 8 ,$ $r _ { \mathrm { h i e r a r c h i c a l ~ d e p t h } } = 0 . 1 2 ,$ , and r<sub>module</sub> <sub>coarsen</sub> $\mathsf { \Pi } _ { \mathsf { s s } } = \mathsf { \bar { 0 } } . 0 \mathsf { \bar { 7 } } , \mathsf { a l l } p <$ 0.001). The large F statistic $( 2 8 6 > 1 0 , p < 0 . 0 0 1$ , stage 1) showed no instrument weakness, whereas Kleibergen–Paap $( \chi ^ { 2 } = 6 9 7 . 7 1 , p < 0 . 0 0 1 )$ , Cragg–Donald $( F _ { \mathrm { W a l d } } = 8 5 0 . 1 6 ,$ $p < 0 . 0 0 1 )$ , and Sargan–Hansen $( \chi ^ { 2 } = 0 . 2 7 , \mathrm { n . s . } )$ tests confirmed proper identification, strong instruments, and valid overidentification

## 4.2. Stage 2: Attention-Funneling Model

Stage 2 (Equation (2)) used predicted silence from stage 1 to estimate attention funneling, thus accounting for systems’ heteromorphic structures known from prior studies:

$$
\mathrm{Attentionfunneling} _ {\mathrm{t2}} = \beta_ {0} + \beta_ {1} \mathrm{silence} \hat {y} _ {\mathrm{t1}} + \varepsilon .\tag{2}
$$

The significant, positive effect of silence on attention funneling $( \beta = 0 . \dot { 4 } 8 , T \mathrm { v a l u e } = 8 . 0 0 , p < 0 . 0 0 1 )$ highlighted in stage 2 in Table 4 supports Hypothesis 2. Effect sizes are also crucial in drawing causal inferences in such voluminous data (Cunningham 2021, p. 51). In our stage 2 linear regression model where silence and attention have a zero to one range, the effect size of 0.48–0.5 indicates that each unit increase in silence increases attention funneling by 1/2 unit.

## 4.3. Stage 3: Generativity Model

Our criterion variables are count variables, for which both negative binomial regression (NBR) models and simpler Poisson models are plausible. Codebase generativity and release cadence are nonpanel, lifetimecumulative count variables, and degenerativity and evolution rate are panel and count variables. Their dispersion parameter $\alpha > 0$ indicates overdispersion, for which an NBR model is more appropriate. It was $3 . 3 7 \ : ( T = 2 9 . 3 )$ $p < 0 . 0 0 1 )$ for codebase generativity, $0 . 5 \ : ( T = - 4 . 8 5 , p <$ 0.001) for degenerativity, 1.31 $( T = \dot { 1 } 7 0 , p < 0 . 0 0 1 )$ for evolution, and 5.6 $( T = 3 2 . 5 , p < 0 . 0 0 1 )$ for release cadence, leading us to NBR models.

Stage 3 (Equation (3); used for all four criterion variables) estimated generativity using NBR fixed effects models, also including the controls discussed in Section 3.2.1. Stage 3 of Table 4 shows incidence rate ratios (IRRs) appropriate for NBR models in lieu of conventional regression coefficients. IRRs are exponentiated coefficients; so, negative coefficients become $\mathrm { I R R s } \le 1$ , and positive ones become $\mathrm { I R R s } > 1 $

$$
\begin{array}{l} \text {Generativity} _ {\mathrm{t3}} = \gamma_ {0} + \gamma_ {1} \text {attention funneling} \hat {y} _ {\mathrm{t2}} \\ \qquad + \{\gamma_ {2} \text {code volume} _ {\mathrm{t2}} \\ \qquad + \gamma_ {3} \text {module count} _ {\mathrm{t2}} + \gamma_ {4} \text {system ag} _ {\mathrm{t2}} \\ \qquad + \gamma_ {5} \text {team size} _ {\mathrm{t2}} \} + \gamma_ {6} \text {silence} \hat {y} _ {\mathrm{t1}} + \varepsilon . \end{array}\tag{3}
$$

Attention funneling significantly increased codebase generativity in stage 3 in Table 4 $( \mathrm { I R R } = 6 1 6 . 8 7 , T = 6 . 3 6 ,$ $p < 0 . 0 0 1 )$ , reduced degenerativity $( \mathrm { I R R } = 0 . 5 0 , T = - 4 . 8 5 ,$ $p < 0 . 0 0 1 )$ , enhanced the system’s evolution rate $( { \mathrm { I R R } } =$ $1 . 9 8 , T = 5 . 0 8 , p < 0 . 0 0 1 )$ ), and increased release cadence $( \mathrm { I R R } = 3 . 6 8 , T = 2 . 0 8 , p < 0 . 0 5 )$ . This strongly supported Hypothesis 1 across all four metrics of IS generativity. Significant mediation tests using the results from stages 2 and 3 showed that attention funneling completely mediated the effect of silence on codebase generativity $( T _ { \mathrm { S o b e l } } = 4 . 9 8 , \ : T _ { \mathrm { A r o i a n } } = 4 . 9 4 , \ : T _ { \mathrm { G o o d m a n } } = 5 . 0 2 , \ : \mathrm { a l l } \ : p \ : <$ 0.001). Similarly, mediation tests were significant across degenerativity $( T _ { \mathrm { S o b e l } } = 4 . 1 5 , p < 0 . 0 0 1 )$ , evolution rate $( T _ { \mathrm { S o b e l } } = 4 . 2 9 , p < 0 . 0 0 1 )$ ), and release cadence $( T _ { \mathrm { S o b e l } } =$ $2 . 0 1 , p < 0 . 0 5 )$ . Hypothesis 3 was, therefore, supported across all four generativity metrics.

4.3.1. Effect Sizes. The exponentiated-form IRRs in our stage 3 NBR models are the number of events associated with a unit of increase in the response variable. They show the effect of moving from completely scattered attention (zero) to perfectly funneled attention (one). (Attention-funneling IRR is the rate ratio for a one-unit increase in attention funneling at t<sub>2</sub> as predicted by silence in $\mathrm { t } _ { 1 } . )$ Codebase generativity’s IRR of 616.8 indicates that a one-unit increase in attention (i.e., moving from completely scattered to perfectly funneled attention) leads to 617 times more forks. Degenerativity’s 0.5 IRR indicates that a one-unit increase in attention funneling halves the number of cyclomatically complex lines of code (i.e., doubles the system’s code quality). Evolution rate’s 1.98 IRR implies that perfectly funneling scattered team attention roughly doubles quarterly commits. Release cadence’s 3.6 IRR indicates that this nearly quad ruples future releases of the system. In summary, fully focusing a scattered attention team doubles system qual ity and evolution rate, quadruples release cadence, and generatively propagates its codebase for derivative systems by over 600 times more.

4.3.2. File-Level Reanalysis for Silence and Attention Funneling. We replicated all models using file-to-file interactions focused on method calls instead of module to-module interactions. High correlations of file to file with module-to-module measures $( \rho = 0 . 8 1 , p < 0 . 0 0 1 )$ signaled what our reanalysis subsequently confirmed— that they are tapping into the same underlying construct. The silence → attention effect was robust across all models using the instruments from Table 4 as well as different ones subjected to more stringent tests appropriate for the different measurements. We replicated the stage 3 NBR same-instruments and different-instruments models, respectively, with three and two of the four criterion variables in Table 4 given the nature of the data. Their relationships were robust across all analyses, with only release cadence showing weaker significance (one tailed) in the same-instruments model. This assures robustness, irrespective of computing silence and attention across a system’s modules or files.

The effect of silence on attention funneling held up (β $= 0 . 2 8 , T = 2 . 8 9 , p < 0 . 0 1 )$ ) when we instead control for the three architectural attributes using a two-step model. Thus, silence impacts attention funneling above and beyond architecture. Attention-funneling effects on the generativity variables also held up (one-tailed $p \ <$ $\bar { 0 } . 0 5 \substack { - 0 . 0 0 1 } )$ ), except for the evolution rate being untestable because of model nonconvergence.

## 4.4. Five Limitations

First, although attention funneling provides one explanation, alternative mechanisms merit consideration. For example, simpler systems might naturally exhibit both silence and generativity, and team expertise could shape developer-code interactions independently of silence. Second, our findings from open-source systems may not generalize to closed-source systems. Third, trace data, lags matching our model’s causal order, and Granger causality do not establish true causality. Fourth, our instruments reflect temporal snapshots of actual architecture but have no baseline for what the intended architecture might have been at each system’s inception. Fifth, using a single language mitigates crosslanguage confounds but bounds generalizability.

## 5. Discussion

IS theory—rapt with communication—has been dead silent about silence, which is a central pillar of Simon’s theory. This behavior merits attention as systems grow brittle, brute force plateaus, and autonomous systems misbehave. Although software engineering prioritizes operational performance and static code properties, IS must examine long-term dynamics and causal mechanisms. This initial foray examined how and why silence in a system shapes IS generativity.

We theorized that silent systems achieve higher generativity because they coalesce IS teams’ attention on smaller parts of a system. Our novel insights are into how evolving codebase behavior drives IS generativity by shaping the behavior of humans maintaining it. Our theory’s novel attention-funneling mechanism focuses on human-with-artifact dynamics, simultaneously bringing human developers and IT artifacts to the forefront.

To test these ideas, we constructed novel socialnetwork-theoretic measures from our data streams. We analyzed using supercomputing methods 274 million lines of source code in \~190,000 modules in 1,356 systems as they underwent nearly 20 million changes over a quarter of a century. From this, we constructed over 67,000 human-to-artifact and artifact-to-artifact social networks to uncover dynamics of behavior as these systems evolved over time. Our empirical findings support our theory, with the temporal sequence matching our causal chain, effect sizes suggesting practical significance, and robust patterns across diverse projects over time.

We introduced silence as a system behavior distinct from architecture, showed its IS generativity consequences, and unmasked the underlying mechanism of attention funneling. Silence reflects the dynamic interaction behaviors among modules, complementing the predominant architectural lens for understanding systems evolution. Our attention-centric explanation of how silence inside systems shapes IS generativity makes three novel theoretical contributions.

5.1. Theoretical Notion of Silence Inside Systems Our novel theoretical notion of silence inside systems enlarges the IT evolution conversation from architecture to behavior. We conceptualized it as an evolving systemwide behavior of its modules constraining their mutual interactions, building on Simon’s (1962) early, underap preciated emphasis on the interaction behavior among a system’s modules. Smith (1981, p. 54) once emphasized that the meaning of everything in a complex structure is in interactions. Interactions inside a system change as it evolves, leading to behaviors that its original architec ture cannot account for (Lindberg et al. 2016, Rolland et al. 2018, Fu¨ rstenau et al. 2023). This can cause the system’s behavior to deviate over time from what is expected, a phenomenon recognized in both IS and software engineering.

Although in IT project teams, communication is key, within the IT artifact itself, silence is golden. Silence, rather than being merely auxiliary, is causally downstream from a system’s architecture. Our theory of silence thus enlarges the IS generativity discourse beyond architecture and governance to encompass systems’ behaviors (e.g., Rolland et al. 2018, Fu¨ rstenau et al. 2019, Tiwana and Safadi 2024). Our concept of silence also bridges the artifact focus of software engineering with the human developer focus of IS, helping explain why similar systems’ generative outcomes vary.

Although our theory’s basic concern is interaction behaviors among a system’s modules, it theoretically assimilates their causally upstream architectural arrangement—the left side of Figure 1—that has dominated prior studies. Although not part of our theory of silence, using them as a theoretical scaffold enabled cumulative theory building in ways that empirical controls cannot. This theoretically, causally, and empirically assimilates a priori-known heteromorphism (differences in the structure) of systems in explaining our focal silence → generativity relationship. This expands a historical emphasis in IS on dialog among human developers with dialog among a system’s IT artifacts and between artifacts and humans. More broadly, silence theoretically expands IS scholars’ historical focus on interaction and communication to also encompass isolation and quietness.

## 5.2. Generativity Consequences of Silence

Our second novel contribution is causally linking silence in systems to IS generativity. Although prior research examines management (e.g., Rolland et al. 2018) and architecture influences (e.g., Yoo et al. 2010, Fu¨ rstenau et al. 2019), how internal system behaviors shape longterm generativity is unbroached. Our results confirm that silence breeds generativity, manifested as greater improvements in forking, degenerativity, evolution, and releases in silent systems relative to chattier ones. Silence fostered the most recognized form of generativity— forked derivatives (e.g., Fu¨ rstenau et al. 2023, p. 1700)— that grew by a dramatic 600 times while also halving degenerativity (e.g., Fu¨ rstenau et al. 2019). Further, it doubled system evolution speed and quadrupled lifetime releases of new versions.

These findings extend insights about how changing system interactions can either be generative or be “dialog halting” among developers (Fu¨ rstenau et al. 2023, p. 1700). Our focus on interactions among IT artifacts constituting a system rather than among developers themselves revealed generativity benefits from minimizing internal system dialog. This introduces a novel mechanism into the IS generativity conversation for understanding the coevolution of human and systems’ behaviors.

5.2.1. Counterfactual Generativity Consequences of Unexpected Silence. What happens when we see chattiness in systems where we expect silence and silence where we expect chattiness? Our theory underscores that architectural choices alone do not determine silence. Both modular and monolithic architectures can exhibit varying degrees of silence; thus, architecturally similar systems can display divergent silence behavior as they evolve. Our model allows for nuanced, counterfactual “what-if” analyses, juxtaposing silence anticipated from a system’s architecture with its evolving, observed behavior. This back-and-forth retroduction between empirics and theory leads to novel insights (Ashworth et al. 2021, p. 4), helping us dissect how plausible mismatches affect generativity.

Following the strategy in Cunningham (2021, p. 10) of counterfactual thinking using yˆs, we contrast architecturally expected silence vis-a\`-vis observed silence. Expected silence is the level that our theory predicts based on a system’s architecture (stage 1 of our model) counterfactually contrasted with observed silence following Cunningham (2021, p. 42). This approach creates a productive dialog between theory and empirics as advocated by Ashworth et al. (2021, p. 3). The 2 × 2 in Figure 11 shows generativity for matched (cells ¶ and ) and mismatched (cells • and ) expected versus observed silence. (The high-low halves in Figure 11 is mean splits; the italicized number in each cell in Figure 11 is generativity measured as fork counts.)

A silent system (cell ¶ in Figure 11)—that is architecturally expected to be silent and also, behaves silently— exhibits the most generativity, mirroring our core thesis. A chatty system (cell )—that is chatty and also, is architecturally expected to be chatty—exhibits the secondlowest level of generativity. The other two hatched cells are systems whose observed behavior mismatches architectural expectations. A garrulous system (cell )—that behaves less silently than expected—has generativity poorer than the matched cell . A mute system (cell

Figure 11. (Color online) Generativity in Systems Whose Actually Observed Behavior Matches (¶ ) and Mismatche (• ) Architecturally Driven Expectations of Silence  
![](/api/attachments/JWJP7MBA/fulltext/images/f2f0e7742bd62b185fa23749052326473c879527e146e0d0932418c9c93c8fb7.jpg)

)—that is unexpectedly silent—has the poorest generativity. The most generative systems have higher-thanexpected silence (the upper half of Figure 11), favoring overly silent architectures. Designers should, therefore, pare interactions among modules to the bare minimum required to realize system functionality.

## 5.3. Attention Funneling Mechanism

Our third contribution is our mechanism—attention funneling—linking silence to IS generativity. Mechanisms answer “why” questions (Ashworth et al. 2021, p. 48), addressing the black box in Figure 1’s causal chain. Silence in a system enhances IS generativity because it dynamically coalesces teams’ attention on a small codebase sliver—such as a module or a file—at one time.

This mechanism bridges two historically separate research streams: IS studies of human developer interactions and software engineering studies of code artifacts, underscoring their interplay. It connects silence with attention—fundamental yet overlooked notions in Simon (1962, p. 470)—to show how previously unobserved behaviors inside IT artifacts causally shape teamwide attention dynamics.

Although prior work emphasized divergent thinking (Harvey 2014) and knowledge sharing (Zhang et al. 2024), our mechanism shows how system properties shape teams’ collective cognition. It also enlarges the conversation on the dynamics of IT evolution, complementing Fu¨ rstenau et al.’s (2019, p. 132) insights on misallocated attention. This mechanism for generatively harnessing developers’ attention integrates individual and collective attention in the recent footsteps of Zhang et al. (2024). More broadly, it echoes Simon’s thinking that attention scarcity requires concentrating on select activities while deliberately ignoring others.

## 5.4. Contributions to Software Engineering

First, our conceptualization of silence as a system-wide behavior links design to behavior, a connection sought after by software engineering scholars (Aiomar et al. 2024). This insight is particularly timely given the growing trend toward refactoring monolithic systems into distributed microservices (Abgaz et al. 2023). Second, our focus on long-term consequences—such as forks, complexity creep, codebase evolution, and release tempo— complements their short-term concerns, like congestion, latency, performance, and reliability (e.g., Jin et al. 2022, Abgaz et al. 2023). Third, our novel social-network measures of system-wide dynamics expand their repertoire beyond file- or module-level static analysis. Fourth, our mechanism—which operates outside the typical radar of software engineering scholarship—reveals how system behaviors shape human-code interactions in ways that can spawn derivatives and curb degradation.

## 6. Conclusion

For IS practice, cultivating silence inside systems catalyzes IS generativity, and this silence can be seeded through thoughtful architecture and disciplined evolution. Such an approach coalesces scarce developer attention and circumvents the unsustainable Band-Aid fix of compensating for chattiness by increasing processing power and bandwidth. A silent revolution?

Five questions merit future work. First, how does silence across—rather than within—systems influence IS generativity? Second, when does chattiness inside modules foster silence inside systems? Third, how can silence be regained when technical debt breaks it? Fourth, what are the evolutionary consequences of intertemporal increase or decrease of silence in a system? Finally, beyond silence in this initial foray, what other system behaviors merit consideration as funnels for developers attention?

In conclusion, silence—rooted in thoughtful architecture—breeds generativity by focusing teams on one codebase sliver at a time. Jazz legend Miles Davis said that, in music, silence is more important than sound. In systems, silence is as crucial as interaction.

## Appendix. An Illustration of Inference of System-Wide Silence by Examining Java Code

In Figure A.1, an archetypical enterprise resource planning application is structured with three Java packages (modules): accounting, human resources (HR), and marketing, with corresponding code shown in the lower half of the figure. The HR module contains the class Employee, which encapsulates employee data. Within the marketing module, two classes exist: Customer (representing company customers) and Offer (representing offers to customers). Because an offer requires both a customer and a supervising employee, the Offer class has a composition relationship with classes. In Unified Modeling Language (UML) lingo, Offer has a Customer, and Offer has an Employee. Because Employee resides in a different module, the Offer class must import it via an import statement—creating a silencereducing coupling between the two modules (marketing import-HR).

The accounting module contains two classes, Payroll and Payee. A payroll comprises multiple payees. In UML lingo, Payroll has a Payee. No import statements are required fo this relationship because both classes reside within the same module. Although Payroll imports the java.util module to access the class ArrayList, this import is excluded from our silence measurements as it is an external, nonnative module. Finally, the class Payee is a subclass of Employee. A Payee is an employee with extra information, like the bank account and tax withholdings. In UML lingo, Payee is an Employee represented with the Java extends keyword. Because the two classes Payee and Employee are in dif ferent modules, an import statement is needed (thus, accounting-import-HR). This example illustrates how two fundamental object-oriented coupling relationships— inheritance and composition—create import relationships between modules, affecting system silence.

Figure A.1. (Color online) Inference of Module-Module Interaction Behaviors Using Class Composition and Inheritance  
![](/api/attachments/JWJP7MBA/fulltext/images/1be3a6f16b7f13f0bf455ea1b5457b97985ac348880a479fbdea89e5187aebea.jpg)

## Endnotes

<sup>1</sup> See wsj.com/business/airlines/flight-cancellations-delays-microsoftoutage-998f1c60.

<sup>2</sup> Distributedness creates latency across the network, penalizing system responsiveness when the system’s modules interact. Module interactions risk slowdowns, prompting admonishing of “chatty” APIs (e.g., Abgaz et al. 2023, Aiomar et al. 2024).

<sup>3</sup> See www.wsj.com/articles/google-amazon-meta-and-microsoftweave-a-fiber-optic-web-of-power-11642222824.

<sup>4</sup> See https://www.wsj.com/opinion/boeing-not-pilot-error-737-maxplane-crash-f0ce9172.

<sup>5</sup> The modularity literature has no concept capturing system silence behavior, often assuming that behavior mirrors architecture. Modu larity in use describes end users reconfiguring components, distinct from our focus on internal system behavior.

<sup>6</sup> Loosely-coupled modules exhibit strong interaction behavior through frequent communication or extensive data exchange. Systems using shared services, concurrent processes (like REST APIs), or event-driven architectures exemplify frequent interactions among loose-coupled modules. Here, modules often interact to synchronize states in response to events generated by other modules but often through well-defined interfaces or APIs that preserve loose coupling among modules. Conversely, tightly-coupled modules exhibiting silence include batch-processing systems that interact only during batch jobs; monolithic apps, like Word, contain tightly-coupled error-handling and reporting modules that activate only when errors occur, exchanging minimal data.

<sup>7</sup> Their idea focused on reducing communication costs in faultprone distributed systems through a message-optimal “stealth protocol” to improve fault tolerance (Goren and Moses 2020).

<sup>8</sup> Dynamic typing (in Python but not static-typed Java) creates dependencies invisible in source code (Jin et al. 2022). Our Javaonly approach eliminated this confound.

<sup>9</sup> Modules’ code becomes significantly coupled rather than exhibiting the interaction behavior that we study.

<sup>10</sup> Software engineering calls incoming and outgoing dependencies afferent and efferent dependencies, respectively (Abgaz et al. 2023).

<sup>11</sup> It is unlike software engineering’s logical dependencies that track comodified source-code files; this captures human developers’ collective dynamics. For example, when files A and B are frequently modified together, they have a logical dependency based on their change history rather than code structure.

<sup>12</sup> Evolution rate captures team productivity, and release cadence captures its tempo.

<sup>13</sup> Java’s strict application programming interface (API), libraries, and predefined class interaction standards (formats and conventions)

eliminate interface variance, reducing modularity to its loose-coupling dimension.

<sup>14</sup> GitHub hosts 200 million code repositories (172 million private) with 83 million developers. (Gousios–Spinellis’ repository is at http://ghtorrent-downloads.ewi.tudelft.nl/mysql/mysql-2017-01-19. tar.gz.) We used 2016 as a cutoff as (1) Java language changes in 2017 made earlier code comparisons infeasible and (2) it allowed five-year lagging of generativity. Of 1,679 qualifying projects, our final sample was 1,356 after excluding those deleted or missing main branches or source-code files. This includes pre-GitHub projects migrated to it after 2008.

<sup>15</sup> We created file and module dictionaries that tracked nested classes and crossreferenced class references against imports, enabling construction of 22,500+ networks incorporating inheritance and composition relationships. The file-to-file dependencies used to construct these networks parallel our module-level analyses.

<sup>16</sup> One developer-to-file linkage is created when a developer changes a file by committing code to it. Our approach is conceptually analogous to the Hansen and Haas (2001) attention measure counting document retrievals in intranets.

<sup>17</sup> Unlike software engineering snapshot studies of a single system, like Linux, with an explicitly documented initial conceptual architecture, we examine concrete architecture across thousands of evolving systems inferred from their code. A system’s architecture progresses in stages (conceptual (purpose/scope/constraints) → logical (entities to translate into artifacts) → structural (data/protocols) → concrete (implementation language/technologies/services)); our study centers on the final con crete stage as manifested in evolving codebases.

<sup>18</sup> We applied a three-quarter moving average to both time series and excluded systems older than 75 quarters (<1% of data) for xaxis clarity. The crosscorrelogram (Figure 9) is a correlation of two time series. It shows that attention funneling correlates most strongly with silence from one to three quarters prior.

<sup>19</sup> We tracked both content changes (adding/removing lines in existing files) and structural changes (adding/removing files). High change ratios often indicate active refactoring.

## References

Abgaz Y, McCarren A, Elger P, Solan D (2023) Decomposition of monolith applications into microservices architectures. IEEE Trans. Software Engrg. 49(8):4213–4242.

Aiomar E, Mkaouer M, Ouni A (2024) Behind the intent of extract method refactoring. IEEE Trans. Software Engrg. 50(4):668–694.

Ashworth S, Berry C, de Mesquita E (2021) Theory and Credibility: Integrating Theoretical and Empirical Social Science (Princeton Uni versity Press, Princeton, NJ).

Chidamber S, Kemerer C (1994) A metrics suite for object-oriented design. IEEE Trans. Software Engrg. 20(6):476–493.

Cunningham S (2021) Causal Inference (Yale University Press, New Haven, CT).

Fu¨ rstenau D, Baiyere A, Kliewer N (2019) A dynamic model of embeddedness in digital infrastructures. Inform. Systems Res. 30(4):1319–1342.

Fu¨ rstenau D, Baiyere A, Schewina K, Schulte-Althoff M, Rothe H (2023) Extended generativity theory on digital platforms. Inform. Systems Res. 34(4):1686–1710.

Goren G, Moses Y (2020) Silence. J. ACM 67(1):1–26.

Hansen M, Haas M (2001) Competing for attention in knowledge markets. Admin. Sci. Quart. 46(1):1–28.

Harvey S (2014) Creative synthesis: Exploring the process of extraordinary group creativity. Acad. Management Rev. 39(3):324–343.

Jin W, Zhong D, Cai Y, Kazman R, Liu T (2022) Evaluating impact of possible dependencies on architecture-level maintainability IEEE Trans. Software Engrg. 49(3):1064–1085.

Lindberg A, Berente N, Gaskin J, Lyytinen K (2016) Coordinating interdependencies in online communities. Inform. Systems Res. 27(4):751–772.

Lundstrom M (2003) Moore’s law forever? Science 299(5604):210–211.

March J, Simon H (1958) Organizations, 2nd ed. (Wiley, New York).

Rahwan I, Cebrian M, Obradovich N, Bongard J, Bonnefon JF, Breazeal C, Crandall JW, et al. (2019) Machine behavior. Nature 568(7753):477–486.

Richards M, Ford N (2020) Fundamentals of Software Architecture (O’Reilly, Sebatapol, CA).

Rolland K, Mathiassen L, Rai A (2018) Managing digital platforms in user organizations. Inform. Systems Res. 29(2):419–443.

Salganik M (2017) Bit by Bit: Social Research in the Digital Age (Prince ton University Press, Princeton, NJ).

Simon H (1962) The architecture of complexity. Proc. Amer. Philos. Soc. 106(6):467–482.

Simon H (2002) Organizing talk and silence in organizations. Indust. Corporate Change 11(3):611–618.

Subramanyam R, Ramasubbu N, Krishnan M (2012) In search of efficient flexibility. Inform. Systems Res. 23(3):787–803.

Smith C (1981) A Search for Structure (MIT Press, Cambridge, MA).

Tiwana A (2015) Evolutionary competition in platform ecosystems. Inform. Systems Res. 26(2):266–281.

Tiwana A, Safadi H (2024) Atrophy in aging systems: Evidence dynamics, and antidote. Inform. Systems Res. 35(1):66–86.

Tonellato M, Tasselli S, Conaldi G, Lerner J (2024) A microstructural approach to self-organizing: The emergence of attention networks. Organ. Sci. 35(2):496–524.

Van Knippenberg D, Dahlander L, Haas M, George G (2015) Information, attention, and decision making. Acad. Management J. 58(3):649–657.

Vial G (2023) A complex adaptive systems perspective of software reuse in the digital age: An agenda for IS research. Inform. Sys tems Res, 34(4):1728–1743.

Yoo Y, Henfridsson O, Lyytinen K (2010) The new organizing logic of digital innovation. Inform. Systems Res. 21(4):724–735.

Zhang X, Fang Y, Zhou J, Lim K (2024) How collaboration technology use affects IT project team creativity: Integrating team knowledge and creative synthesis perspectives. MIS Quart., ePub ahead of print October 8, https://doi.org/10.25300 MISQ/2024/16651.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
