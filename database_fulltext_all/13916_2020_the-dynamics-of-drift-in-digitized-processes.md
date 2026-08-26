---
otero_id: 13916
otero_key: "EZ6ZBF3S"
title: "The Dynamics of Drift in Digitized Processes"
authors: "Brian T. Pentland; Peng Liu; Waldemar Kremser; Thorvald Hærem"
year: "2020"
journal: "MIS Quarterly"
doi: "10.25300/misq/2020/14458"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE DYNAMICS OF DRIFT IN DIGITIZED PROCESSES<sup>1</sup>

Brian T. Pentland Eli Broad College of Business, Michigan State University, East Lansing, MI 48864 U.S.A. {pentlan2@msu.edu}

Peng Liu Steven G. Mihaylo College of Business and Economics, California State University, Fullerton, Fullerton, CA 92834 U.S.A. {peliu@fullerton.edu}

Waldemar Kremser Institute for Management Research, Radboud University Nijmegen 6500 HK Nijmegen, NETHERLANDS {w.kremser@fm.ru.nl}

Thorvald Hærem BI Norwegian Business School, 0484 Oslo, NORWAY {Thorvald.haerem@bi.no}

This paper uses a simulation to build new theory about complexity and phase change in processes that are supported by digital technologies. We know that digitized processes can drift (change incrementally over time). We simulate this phenomenon by incrementally adding and removing edges from a network that represents the process. The simulation demonstrates that incremental change can lead to a state of self-organized criticality. As the process approaches this state, further incremental change can precipitate nonlinear bursts in process complexity and significant changes in process structure. Digital technology can be designed and used to influ ence the likelihood and severity of these transformative phase changes. For example, the simulation predicts that systems with adaptive programming are prone to phase changes, while systems with deterministic programming are not. We use the simulation to generate a set of theoretical propositions about the effects of digitization that will be testable in empirical research

Keywords: Process complexity, complexity bursts, self-organized criticality, digitized processes

## Introduction

For better or worse, digitized processes tend to drift (Bose et al. 2011; Ciborra et al. 2000; Günther et al. 2006). Processes are digitized to the extent that they are supported by digital technology (Gaskin et al. 2014), so digitized processes are typically enacted by an ensemble of human and material agents (Leonardi 2011; Orlikowski and Scott 2008). By drift, we mean that the way a process is performed tends to change over time. Drift has been documented in a large variety of digitized processes, such as product development and design (Baxter and Berente 2010; D’Adderio 2003; Leonardi 2011), logistics (Ferneley and Sobreprerez 2006), procurement (Berente et al. 2016), clinical routines in healthcare (Goh et al. 2011; Halbesleben et al. 2008; Koppel et al. 2008), insurance underwriting and claims processing (Bose et al. 2011; Lyytinen and Newman 2008), invoice processing (Pentland et al. 2011), and business processes in general (Boudreau and Robey 2005; Ciborra et al. 2000; Lyytinen et al. 2009; Orlikowski 1996, 2000; Petrides et al. 2004; Volkoff et al. 2007). Drift happens, and it can be beneficial or harmful depending on the circumstances. It is a basic mechanism for learning and adaptation (Bickhard and Campbell 2003; Pentland et al. 2012), but it is also possible to drift into disaster, when incremental changes in practices lead to unexpected outcomes (Dekker 2013; Dekker and Pruchnicki 2014).

In this paper, we focus on the dynamics of drift: given a stream of on-going, endogenous change, what happens over time? Our analysis is limited to endogenous change: change that occurs without any external intervention or feedback. Endogenous change enables self-organization: the process changes as a consequence of its own, ongoing operation (Feldman and Pentland 2003; Foster 1997). Put simply, what we did in the past influences but does not determine what we might do in the future. In dynamic systems that have this quality, it is possible to approach a critical state where additional incremental change can precipitate dramatic structural change (Bak 1996; Frigg 2003). This self-organized criticality can produce the “avalanche effects” that tend to happen when complex systems arrive at the edge of chaos (Girod and Whittington 2015). Here, we use the metaphor of phase change (Lewin 1951), where the phases are characterized by different patterns of action, to describe this phenomenon.

Digital technology can have a dramatic effect on the factors that give rise to these dynamics. Digital technology is often intended as a mechanism to improve coordination and control (Berente et al. 2016). By increasing restrictiveness (Markus and Silver 2008), or adding modular interfaces (Simon 1996), digitization can constrain the way a process is performed (Boudreau and Robey 2005). Ironically, while new technology can afford control, it can also provide new occasions for appropriation (DeSanctis and Poole 1994), structuring (Barley 1986), workarounds (Alter 2014), and other forms of ongoing, incremental adjustment (Orlikowski 1996). Even when intended as a mechanism for control, digitization can be a double-edged sword, as new controls inspire new workarounds (Alter 2014; Berente et al. 2016). Furthermore, digital technology includes not only automated technology but also intelligent or AI-based technology. Digital technology may be programmed to create increasingly sophisticated and adaptive software agents that can sense their surroundings, adapt to their environments, and communicate with others (Yoo 2010). When programmed with algorithms for learning and adaptation, intelligent digitized systems can learn from experience and try new courses of action (Littman 2015).

This leads us to ask: What is the role of digitization in the dynamics of drift? In addressing this question, we focus on three kinds of outcomes. First, how does digitization influence process complexity? Second, how does digitization influence the likelihood of transformative phase changes in process structure? And third, how does digitization influence the magnitude of the accumulated change? Together, these questions provide some indication of the theoretical and practical impact of this phenomenon.

## Building Theory Through Simulation

In this paper, we use a simulation to build theory about the dynamics of drift in digitized processes. Simulation is a useful tool for theory generation in this domain because it allows us to visualize the interaction of simple mechanisms over many thousands of process iterations over a wide range of parameter values (Davis et al. 2007; Simon 1996). The effects of digitization will always be contingent on how digital systems are designed and used, so our model includes parameters that can be shaped by digitization, such as modularity (Simon 1996), the number of potential affordances within a process (Anderson and Robey 2017; Leonardi 2011) the probability of workarounds and other variations (Alter 2014; Ciborra et al. 2000), and the span of the process’ memory (Argote 2013; Darr et al. 1995; Holan and Phillips 2004).

Our simulation shows that incremental changes in a process can lead to bursts of complexity that are accompanied by changes in process structure. With no external shocks, the complexity of the simulated process can spike up by several orders of magnitude and then drop back down. These bursts are often accompanied by a transition to a different process configuration, like a phase change from liquid to solid. Complexity theory provides many examples of similar nonlinear phenomena, such as avalanche effects (Frigg 2003; Girod and Whittington 2015). We contribute to this body of theory by demonstrating a mechanism that is unique to the dynamics of repetitive processual phenomena such as business processes, services, and routines.

Our contribution is based on a novel approach to modeling complexity. Rather than networks of interacting actors (e.g., Grimm et al. 2005; Nan 2011; Nan and Tanriverdi 2017), we model networks of sequentially related actions (Pentland et al. 2012). In our model, the network represents ways of getting something done. A phase change represents a transition to a new way of getting things done: a new network of actions with a new dominant path.

We begin by introducing our approach to modeling processes as directed graphs and our graph theoretic framework for measuring the impact of drift on process complexity (Hærem et al. 2015). We describe and then simulate well-established, generic mechanisms that can lead to incremental changes in the graph. We explain how incremental change can lead to bursts of complexity and phase changes and how digital technology can promote or inhibit these phase changes. We construct a set of theoretical propositions by simulating process dynamics over a wide range of conditions. The simulation provides a motivation for further inquiry into how the design and use of digital technology can influence process dynamics.

## Conceptualizing and Measuring Drift

## Processes as Directed Graphs

Digitized processes are often represented as directed graphs (e.g., flow charts or data flow diagrams). Here, we represent processes using a weighted, directed graph with a source and sink (Pentland et al. 2012; Pentland et al. 2015). In this kind of graph, the nodes can be interpreted as actions, events, or actualized affordances (Anderson and Robey 2017; Strong et al. 2014). Edges in the graph represent the sequential relationship between pairs of actions. The weights represent the probability that one action will be followed by the next. The edges in the graph are like ruts in the road: the deeper the rut, the more likely the next action will follow.

To make these concepts more concrete, consider two examples: invoice processing at a business school (Pentland et al. 2011) and medical record-keeping (Goh et al. 2011; Ryan et al. 2016). These are examples of digitized processes carried out by a blend of digital technologies and people. Table 1 shows the basic terminology (with some common synonyms in italics), along with definitions and examples from invoice approval and medical record keeping. We will return to these examples throughout the paper.

## Network Paths as a Measure of Process Complexity

A graph theoretic representation provides a natural way to conceptualize process complexity (Flood 1987; Kauffman 1993; McCabe 1976) which will be a central concept in our theory of dynamics. To measure the complexity of a process, we count the possible paths through the network that represents the process (Hærem et al. 2015). Following Wood’s (1986) concept of coordinative complexity, Hærem et al. (2015) argue that the complexity of a task or process can be estimated by counting the possible paths in the graph that represents the task. Here, we operationalize their definition as follows:

$$
\text { Process   Complexity } = \sum_ {g} \text { simple   paths } _ {h}
$$

A simple path is defined as a path without cycles from source to sink (West 2001), and g is the graph that represents the process. Paths with cycles are excluded because they are innumerable. This measure tends to grow exponentially with the size and density of the graph (Hærem et al. 2015).

This definition has a straightforward interpretation: the complexity of a process is indexed by the number of ways it can be carried out. Intuitively, if there is only one way forward, the process is simple. If there are many ways forward, the process is more complex. This matches the idea that “variety is a measure of the complexity with which management has to deal” (Beer 1995, p. 21). The idea of counting paths in a graph also mirrors McCabe’s (1976) cyclomatic complexity, but it is derived from organizational psychology, rather than software engineering. Given that digitized processes are typically carried out by a combination of people and machines, this conceptual agreement is reassuring. When we say that process complexity is increasing (or decreasing), we are saying that the number of possible ways to do the process is increasing (or decreasing).

## Mechanisms that Influence Complexity

Within our framework, there are two generic mechanisms that can influence complexity: edge formation and edge dissolution. Edge formation can be thought of as path making: it adds new pathways from start to finish. By definition, adding pathways increases process complexity. Conversely, edge dissolution removes pathways from the graph, making it less complex. We discuss these two mechanisms in the context of digitized processes, so that we can incorporate them into our simulation in a realistic way.

## Mechanism 1: Variations Drive Edge Formation

Within a process or routine, the flow from one action to the next is often nearly automatic, as one action triggers the next (Cohen and Bacdayan 1994). Sometimes, however, a problem or an exception occurs that requires some reflection (Dittrich et al. 2016) or recomputation (Ardagna and Pernici 2007). In these cases, the typical next step might seem problematic for the people performing the process, who may perceive the need for a variation or a workaround (Alter 2014). For example, in invoice processing, there might be a need to expedite approval of an invoice (circumventing some intermediate steps), or, if an approver is on vacation, the invoice might need to be routed to an alternate. Similarly, if an algorithm for configuring web services discovers that a preferred service is unavailable, it might need to select an alternative (Ardagna and Pernici 2007).

<table><tr><td colspan="4">Table 1. Terminology and Examples</td></tr><tr><td>Term</td><td>Definition</td><td>Invoice Approval</td><td>Electronic Medical Records</td></tr><tr><td>Graph (network)</td><td>Set of vertices and edges that represent a process</td><td>·The approval process</td><td>·Medical recordkeeping</td></tr><tr><td>Vertex (node)</td><td>Action or event in a process</td><td>·Clerk scans invoice data·System routes data to user·User reviews data</td><td>·Admin enters check-in data·Nurse enters vital signs·Physician enters diagnosis</td></tr><tr><td>Edge (tie or link)</td><td>Sequential relationship between two nodes</td><td>·First, clerk scans invoice, then the System routes invoice</td><td>·First, admin enters check-in data, then Nurse enters vital signs</td></tr><tr><td>Source</td><td>Process start</td><td>·Invoice arrives</td><td>·Patient arrives at clinic</td></tr><tr><td>Sink</td><td>Process end</td><td>·Invoice approved</td><td>·Patient departs from clinic</td></tr><tr><td>Path (performance)</td><td>A list of connected edges; each path represents one way to carry out a process</td><td>·One complete performance of the approval process</td><td>·One complete patient visit to the clinic</td></tr></table>

In general, when some situational contingency leads to a perceived need for a workaround (Alter 2014), there are at least three possible cases: (1) the process might still proceed along the most frequent path (e.g., by retrying or resending); (2) the process might take an alternative but previously followed path; or (3) the process might branch into an entirely new path. It is important to note that these basic behaviors (retrying and exploring alternatives) are not limited to humans. They are a basic part of digitized processes such as communication protocols, network routing algorithms (Loo et al. 2016), and web service configuration (Ardagna and Pernici 2007).

Research has shown that workarounds can have positive as well as negative effects on organizational outcomes (Halbesleben et al. 2008; Kossek et al. 1994; Petrides et al. 2004; Rerup and Feldman 2011). Even in cases when a “quick fix” is overall inefficient and slow, it might become a persistent part of the process as enacted (Desanctis and Poole 1994; Koopman and Hoffman 2003). Tyre and Orlikowski (1994, p. 108) report one example where “users clung to the system they had become accustomed to, and prevented engineers from dismantling the ‘temporary’ workaround.” In other words, variations can become standard practice regardless of their impact on process outcomes (Rice and Cooper 2010).

The difficulty in selecting “good” variations results from the “credit assignment” problem in reinforcement learning (Fu and Anderson 2008, p. 321):

Some of the most difficult situations in skill learning occur when the learner has to perform a sequence of actions but only receives feedback on their success at the end of the sequence. … The credit-assignment problem is even more difficult when the actions are interdependent, and the environment may change both autonomously and as a result of the actions.

On top of this, Rice and Cooper (2010) point out that in real organizational settings feedback (1) is often distorted or not available at all; (2) may not be given to the individuals involved in actually carrying out the work; and (3) provides little guidance about how their particular actions helped (or hindered) the overall result. Therefore, we do not include costs, outcomes, or incentives in our model.

## Mechanism 2: Selective Reinforcement Drives Edge Dissolution

The repetitive enactment of a process tends to create the “ruts in the road” that characterize organizational routines (Cohen and Bacdayan 1994, Pentland et al. 2012). Routines are often considered as a form of organizational memory (Argote 2013; Walsh and Ungson 1991). In line with this metaphor, behavioral theories of organizations generally claim that “organizations remember by doing” (Nelson and Winter 1982, p. 99). The inversion of this argument, that organizations will forget what they don’t do, has not received the same attention in organization research (Holan and Phillips 2004). Forgetting is essential to change (Kluge and Gronau 2018; Ram and Santamaría 1997) and it is essential to our understanding of enacted processes.

Remembering and forgetting are two sides of the same coin, as explained by Casey and Olivera (2011, p. 306):

Rather than viewing memory as knowledge stored in a collection of retention bins, the emphasis is on memory as continually constructed and reconstructed …. From this perspective, memory and forgetting are inextricably linked: The processes through which organizational knowledge is enacted are also processes of … retention and decay.

Research on organizational memory has identified a number of factors that can influence the balance between remembering and forgetting in the enactment of organizational processes. In this respect, the most general insight is that recent events are more likely to be recalled than distant ones (Casey 1997). In line with this, a number of studies have shown that knowledge in organizations will depreciate at varying rates (for an extensive review, see Argote 2013). The highest rate of knowledge depreciation was found in a study of pizza stores (Darr et al. 1995). In these stores, only about half of the knowledge available at the beginning of the month would remain at the end of the month. Similar but different to this is the insight that cyclical events will in general be remembered better, even if the cycle times are quite long (Campbell-Kelly 1996). Paths that are taken more frequently will be reinforced and remembered. Paths taken less frequently will fade over time and, at some point, may even be forgotten (Feldman and Feldman 2006; Kluge and Gronau 2018). Simply put: use it or lose it.

## Phase Transitions in the Network of Actions

Because we model networks of actions, rather than actors, it is important to clarify what we mean by a phase transition. As we demonstrate below, incrementally adding or removing edges from the network can lead to bursts of complexity, after which the network can settle into a new state with a new dominant path. This burst of complexity, accompanied by a transition from one set of dominant paths to another, signifies the phase change.

## The Challenge of Modeling Ensembles of Human and Material Agency

Theorizing about the effects of digitization on processual dynamics is difficult because of the inherent gap between the properties of digital artifacts, as designed, and the emergent properties of digitized processes, as enacted. Yoo (2010, p. 231) offers a list of seven properties of “digitalized artifacts”: programmability, addressability, sensibility, communicability, memorizability, traceability, and associability. As Yoo points out, these properties can be embodied into an endless variety of designs at the level of particular artifacts (e.g., a cell phone) or large ensembles (e.g., a cellular network). However, decades of research on information systems demonstrates that system properties “as used” do not necessarily reflect system properties “as designed” (Desanctis and Poole 1994). Without question, system design can enable and constrain process enactment, but the influence on processual dynamics may be indirect and emergent.

In order to create a generalizable model, we note that edge formation and edge dissolution in digitized processes can be enacted by any combination of human and material agents. Current organizational systems typically involve a mix of more-or-less deterministic technology and more-or-less adaptive humans, but this is just one possibility in a much larger design space. Over time, adaptive, autonomous digital agents (Maes 1993) are expected to gain prominence in applications such as industrial operations (Zhang et al. 2017), supply chain ordering (Mortazavi et al. 2015), and healthcare (Isern and Moreno 2016). Adaptive algorithms have been a foundational technology in network protocols and routing algorithms for decades (Loo et al. 2016), and they are already prevalent in securities trading (Treleaven et al. 2013) and many other domains (Schultze et al. 2018). Deterministic systems operated by adaptive humans represents an important special case that we discuss below, but our model is intended to reflect the dynamics of drift in any digitized process where it is possible to form and dissolve edges as a result of performing the process.

## The Dynamics of Drift in the Digitized World

## Model Overview

The mechanisms for edge formation and dissolution were implemented within the simulation framework used in Pentland et al. (2012). In this framework, a process is modeled as a progression of steps that repeats over time. Process execution is not constrained or influenced by organizational structures or external feedback. We model actions, not actors, so the framework makes no assumptions or distinctions about human or material agency.

We simulate the trajectory of the process as it changes over time. The process starts as a series of sequential steps with no branches or loops: a simple, happy path. As the process is performed, edges are formed and dissolved according to mechanisms described above. Over time, the process drifts. In this paper, a trajectory consists of five thousand iterations of a process. Each iteration is one performance of the process, from source to sink (e.g., one invoice approval, or one patient visit to the clinic). Each iteration consists of many steps. Each step can be interpreted as an action or an actualized affordance (Strong et al. 2014).

![](/api/attachments/EZ6ZBF3S/fulltext/images/8d8f0dae24d332d308f36b62f93418b95211069398cee61e2413fbdd753d53c8.jpg)  
Figure 1. Variation and Reinforcement of Actions Results in Process Change

Figure 1 shows the dynamic relationship between the network that represents the process (on the left) and the specific iterations of the process (on the right). The network summarizes the current state of the process; it describes the edges between each of the possible actions. Darker squares represent more frequent edges (deeper ruts in the road). The network is used to generate iterations of the process, which may include variations. Those variations get folded back into the network after each iteration to form new edges. Figure 1(a) shows a process without modules, while Figure 1(b) shows the same process with three modules that add sequential constraints on the way the process can be performed.

The model has four parameters: the size of the lexicon of actions afforded (L), the modularity of the process (M), the probability of variations (V) and the number of prior iterations that reinforce the current process (R). As we introduce each parameter, we give examples of how it may be influenced by the properties of digital technology. Later, in the discussion, we provide a more holistic summary of how the design and use of digital systems may influence the dynamics of drift and process complexity.

## Lexicon of Actions (L)

The simulation uses a lexicon of L actions that might be observed as the process is carried out. L is the maximum number of actions, and it is fixed for the duration of the simulation. Pentland et al. (2012) referred to this parameter as the “choice set” and simulated only one value (L=10).

We use a small lexicon of actions (L = 10) to explain the basic model operation, and a more realistic lexicon (100 # L # 400) to develop theory. Augusto et al. (2018) found that the number of distinct action types ranged from 7 to 310 in their review of 24 databases for process mining benchmarks. In invoice processing, Pentland et al. (2011) observed 28 distinct action types. In medical record keeping, Ryan et al. (2016) observed 102 distinct action types. In any process consisting of many modules (e.g., the ERP system described by Berente et al. 2016), a series of “small” process modules would add up to a larger value of L.

## Influence of Digital Technology on L

Programmability can have a dramatic effect on the lexicon of actions in a digitized process by either increasing or decreasing the set of actions available. Yoo (2010, p. 231) defines programmability as “the ability of a digitalized artifact to accept new sets of logic to modify its behaviors and functions.” The set of available behaviors can also be conceptualized in terms of the restrictiveness of the technology (Markus and Silver 2008; Silver 1990). By design, information systems vary widely in terms of the sheer number of potential actions they afford, but the size of the lexicon is not a purely technical issue. It will also be influenced by policies concerning authorization (who is allowed to access certain features?), training (who has the capability to use those features?), or whether people remember them and perceive them as useful (Anderson and Robey 2017; Strong et al. 2014).

## Modularity (M)

Modularity is a fundamental idea in the architecture of complexity (Simon 1996), information systems (Nunamaker et al. 1990), processes (Basu and Blanning 2003; Reijers and Mendling 2008,) and routines (Kremser and Schreyögg 2016). Modularity imposes sequential constraints on the order of steps within the overall process. We model modularity by subdividing the process into a set of M modular subunits (M = 1, 5, 10, 20). Figure 1b shows an example where M = 3.

## Influence of Digital Technology on M

Modularity is generally created and enforced by interfaces between systems (Kremser and Schreyögg 2016; Simon 1996). In other words, it is an architectural feature of the technical environment and the work process that limits the range of actions available to perform the process (Yoo et al. 2010). Modularity is clearly shaped by the addressability (or lack of addressability) of artifacts in a system (Yoo 2010).

For example, IP addresses and sub-net masks are used to create separate, modular sections within a larger network. In the absence of sub-networks, there would be no modularity in the network: every host would be directly addressable by every other host.

Modularity can also be influenced by the design of business rules and interfaces that govern a work process (Kremser and Schreyögg, 2016). For example, in invoice processing, the interface between the approval system and the payment system creates a firm, one-way boundary. After approval, invoice data is exported to a completely separate accounts payable system. In medical record keeping, there is no such boundary in the technology itself, but there are physical boundaries in the clinic (front desk versus examination rooms) where different kinds of work take place. In the dermatology clinic, patient visits are divided into stages that including patient check-in, the medical work, and patient check-out. These examples demonstrate an important fact about modularity in digitized processes: it can be enforced by technical design (as in the invoice process) or it can emerge from human practice (as in the medical record keeping process). In our simulation, we model the situation in invoice approval, where there is a strict, one-way interface between modules.

## Variations (V)

The parameter V governs the probability that the process will encounter an issue that may require sequential variation. If V = 0, no issues arise and the process stays on track without variation. When V = 0.001, there is a one-in-a-thousand chance that an issue will arise at each step. Note that encountering an issue does not necessarily lead to the formation of a new edge. When an issue arises, the simulation chooses the next step randomly, but it draws from a set of choices that includes the existing edges. Therefore, a randomly chosen action could reinforce an existing edge. This corresponds to the common sense strategy of retrying or resending, which is typical in communication and network protocols (Loo et al. 2016). We simulate three levels of variations (V = 0.001, 0.005, 0.01).

## Influence of Digital Technology on V

The potential for sequential variability in a process is directly affected by the programming and memory of the digital artifacts used in the process. In principle, programmability (Yoo 2010) could remove all variation from a process, but in practice, the outcome is less certain. For example, Pentland et al. (2011) noted that new and infrequent users tended to introduce variations in the invoice approval routine. Users devised ways to use new workflow technology to implement their old, paper-based process (they printed hard copy of the documents, walked them around for approval, and then scanned them back in). Time and again, research shows how humans adapt to what they perceive as inflexible technology (Alter 2014). As adaptive agents become more prevalent, they may accelerate the tendency to look for workarounds, loopholes, and exceptions. Depending on how these agents are programmed, they would be capable of identifying and reacting to many more issues than their human counterparts, effectively increasing V.

## Reinforcement (R)

The parameter R refers to how many past process iterations are remembered by the existing process. In a sense, it sets a limit on the effect of history; it determines how quickly the ruts in the road are filled in and forgotten. R is implemented as a “moving window” of previous sequences. When the most recent action sequence is added to the history matrix, H, the oldest action sequence in the window is dropped. When R = 0, there is no effect of history and no way to retain variations. In our simulation, we vary R from 0 to 200.

## Influence of Digital Technology on R

We caution readers against jumping to the conclusion that in the digital world, memory of all kinds is effectively infinite. Yoo (2010) notes that, in principle, digital artifacts have material properties such as memorizability (to store and record information) and traceability (to relate events over time). While digital systems can store large numbers of past transactions, they may or may not be programmed to use any of that information to help users decide where to click when there is a problem processing the next transaction. Even if systems are designed to provide guidance based on experience, users may choose to do something else.

Also, Zuboff’s (1988) classic distinction between systems that automate and systems that informate provides a useful way to theorize about the role of alternative system designs. Consider the ideal type of complete automation, where a deterministic program fully controls the sequence of actions. In this special case, there is no effect of past iterations on future iterations. If there is an exception or variation in one iteration of the process, it does not influence subsequent iterations. In a deterministic system, R = 0. It can change instantly (when the system administrator changes the program), but the program itself is not affected by prior iterations. History is irrelevant.

Now consider the more common case where there is some mix of human and material agency (Leonardi 2011). Larger values of R can be conceptualized as providing users with more information (and choice) about what to do based on past experience. It is important to realize that we are talking about remembering what to do next on a very fine grained level (“Where to click? Who to call? Are they on vacation this week? Maybe we can text them if it’s really important or maybe we should just wait and try again later.”).

In current practice (e.g., invoice approval or medical record keeping), where a human agent is interacting with a deterministic program, the choice of what to do next may be shaped by system design (Anderson and Robey 2017) but not necessarily controlled by it (Desanctis and Poole 1994; Pentland and Feldman 2008). Think of the search function of your email program. If well programmed, the search algorithm gives you better access to your own history, but it does not tell you what search term to use or in what sequence you should read and reply to the messages.

As adaptive, intelligent agents become more prevalent, guidance about specific actions based on past experience may become more prevalent, as well. To the extent that happens, it would indicate increased R. However, more memory is not necessarily better. Low values of R are associated with lower inertia and greater flexibility (Pentland et al. 2012). Adaptive systems or intelligent agents need to have both learning and forgetting mechanisms. When a new situation arises, they create new paths by adapting stored solutions to the new situation (Nuxoll and Laird 2012), but old paths need to be forgotten at some point. The mechanism we use here— removing the oldest memories—is a common approach to implementing this essential function (Ram and Santamaría 1997).

To help ground our model parameter, we compared the effective rate of “forgetting” in our simulation to empirical research on knowledge depreciation (Argote 2013; Darr et al. 1995). When we compute the influence of R on the rate of edge dissolution (number of edges dissolved/current number of edges) in a given iteration, we find that the rate varies from 0.8% (when R = 10) to 0.1% (when R = 200). In a typical run of our simulation, with R = 50, the average rate of edge dissolution is 0.3%. It is difficult to compare directly, because the learning curve literature refers to the rate of depreciation of the value of accumulated knowledge, which is not explicitly represented in our model. Still, a rate of less than 1% appears to be conservative rate compared to empirical research (Argote 2013; Darr et al. 1995). In the real world, we expect that R is typically rather low.

<table><tr><td colspan="3">Table 2. Model Parameters</td></tr><tr><td>Model Parameter</td><td>Simulated Values</td><td>Explanation</td></tr><tr><td>Initial process model</td><td>1, 2, 3, 4, 5, ...</td><td>Each trajectory starts with the happy path</td></tr><tr><td>T</td><td>5000</td><td>Number of iterations of the process in the trajectory</td></tr><tr><td>L</td><td>100 – 400</td><td>Number of possible actions to accomplish the process</td></tr><tr><td>M</td><td>1, 5, 10, 20</td><td>Number of modules within the process</td></tr><tr><td>V</td><td>0.001, 0.005, 0.01</td><td>Probability that an issue will arise in selecting the next action.</td></tr><tr><td>R</td><td>0 – 200</td><td>Number of past performances included in the moving window that is used to compute the history matrix.</td></tr></table>

## Iterations of the Process (T)

This parameter refers to the number of iterations of the process within the trajectory. In this paper, all trajectories include 5,000 iterations. The time scale of the model is arbitrary, so the number of iterations does not correspond to any particular length of time. Depending on the frequency with which a routine is performed, 5,000 iterations could be completed in hours or in years. For example, the dermatology clinics at the University of Rochester handle 40,000 patient visits per year, so 5,000 iterations would take about six weeks. The invoice approval process at the BI Norwegian Business School handles over 20,000 invoices per year, so 5,000 iterations would take about 3 months.

## History Matrix (L × L)

At each iteration, the current state of the process is described by a weighted, directed graph. The graph is recomputed after every process iteration. Pentland et al. (2012) refer to this as the “history” matrix (H). Each cell (i, j) in the matrix represents the probability $\mathfrak { p } _ { \mathrm { i j } }$ that action i will be followed by action j. In Figure 1, the shading of each cell in the history matrix reflects ${ \mathfrak { p } } _ { \mathrm { i j } }$ for one pair (i, j) of actions. If one row in the matrix contains a nonzero probability, the sum of the probabilities in the row is 1. This matrix can be interpreted as a first order Markov transition matrix (Anderson and Goodman 1957; Poole et al. 2016). The history matrix describes the potential action sequences that are likely to emerge, and it is used to generate sequences according to these probabilities. The history matrix is updated after every iteration because variations form precedents that can be followed immediately subsequent iterations of the process.

Table 2 summarizes the range of parameters used in our simulation. In the following sections, we run the simulation in two ways. First, to help the reader build intuition for how it works, we simulate a few example trajectories with L = 10. Then, to theorize about the effects of digitization, we simulate millions of trajectories over the full range of parameters shown in Table 2.

## The Nonlinear Dynamics of Drift

To demonstrate the effects of edge formation and dissolution over time, we simulated a small process model (L = 10, M = 1, V = 0.01, and R = 50) on trajectories of T = 5,000 process iterations. Figure 2 shows three examples of trajectories with sudden bursts of complexity followed by periods of much lower complexity. In each of these trajectories, the effect is completely endogenous.

To help visualize what is happening within these trajectories, Figure 3 shows a set of process graphs at three distinct periods in the trajectory. These are snapshots of the trajectory shown in Figure 2, far right. The nodes in these graphs represents actions in a task, process or routine. The initial condition is one way of doing that task, process or routine. Starting from the initial condition, process complexity develops as one might expect. The introduction of new edges leads to incremental increases in process complexity. The deletion of existing edges leads to incremental decreases in process complexity. If new edges are formed just a little bit faster than established ones can dissolve, drift will increase the complexity of the process, at first only incrementally. The first row of Figure 3 shows exactly that. At t = 5, the first new edge is formed. By t = 15, there are a couple of new edges, but at t = 60, one of those edges has dissolved due to lack of reinforcement. By t =100, there are several new edges. During this phase, the average density of the graph is quite low (density # 0.13). Depending on the specific settings of V and R, and random chance, this phase can continue for many thousands of iterations, or it can enter a different phase almost immediately.

![](/api/attachments/EZ6ZBF3S/fulltext/images/b67c8bc632b3c50a9784cc9abcdf96599a4ad52b1730ee315db6f2d8920c1229.jpg)  
Figure 2. Process Complexity Can Change Suddenly

![](/api/attachments/EZ6ZBF3S/fulltext/images/5a8a27ec27a1ae9ff961aa8cf7d399aa04b16f9c869fbdbb69642df99e3a35be.jpg)

![](/api/attachments/EZ6ZBF3S/fulltext/images/7becd44afe7d4888999c96bfa101e7b000473b107ae0c4d01a2eed420196addd.jpg)  
Figure 3. Phase Change in One Trajectory

In the trajectory shown in Figure 3, the process undergoes a dramatic burst in complexity centered around t = 2,500. Remember that we operationalize complexity as the number of paths in the network (Hærem et al. 2015). In this phase, the complexity of the process increases and decreases substantially from one performance to the next. It is important to point out that during this phase the average density of the process network is much higher than the initial phase or the subsequent phase (mean density = 0.386), and, on average, the sequences are longer.

After a complexity burst, the process can settle into a new dominant path that is characterized by much lower com plexity. The original path has been replaced by a new dominant path. The process continues to drift, but does not go through any new bursts of complexity. In this new phase, process complexity is generally low, also the density of the process is low. The ten-step “happy path” has been replaced by a process that allows sequences as short as three steps. In many trajectories, the third phase is so stable that the process does not transition to another phase.

## The Role of Graph Density in the Mechanics of Phase Change

The density of the process graph is not an input parameter, but it has a crucial role in this phenomenon. This is because the density of the graph influences both the formation and dissolution of edges. Density influences the dynamics in at least five distinct says.

(1) By definition, new edge formation increases the density of the graph.

(2) When graph density is high, variations will be more likely to reinforce an existing edge. Put differently, the more variations you have already tried out, the less likely it is that you will have to develop a new variation to resolve an issue.

(3) Density tends to increase the rate of edge dissolution because within any given number of sequences, R, a limited number of edges can be reinforced. Hence, as density goes up, more edges will dissolve. The intuition here is straightforward: the more there is to forget, the more will be forgotten.

(4) The forgetting of edges in a dense graph will not happen randomly since high density also systematically weakens the longest paths. This is true since, in a dense graph, the chance that the process “finds” the sink earlier is higher than for a less dense graph. While the algorithm is not explicitly selecting shorter paths over longer paths, it tends to find shorter paths in a denser graph.

(5) Density affects the magnitude of changes in process complexity when a new edge is formed or dissolved. As density increases, adding or removing an edge from a graph is likely to have a greater impact on the number of paths in the graph. We can think of these as heavy edges: edges with high betweenness (Freeman 1977) that sit on more network paths. Thus, density influences both the rate of edge formation/dissolution, as well as its impact.

While many trajectories exhibit the characteristic phase changes shown in Figure 2, it is worth noting that each specific trajectory is different. Every process drifts in its own direction, as different edges form and dissolve. Phase transitions and inertia are commonplace, but not inevitable, because the trajectories are stochastic.

## Effects of Digitization on the Dynamics of Drift

Digitization can influence each of the model parameters, directly or indirectly. As explained above, the effects of digitization will depend on the design and use of particular systems and combinations of systems. To theorize about how digitization might influence these phenomena, we simulate the dynamics of drift over a wide range of realistic process parameters. We interpret the simulation results to generate propositions about the effect of digitization on three distinct kinds of outcomes: (1) average process complexity; (2) the probability of phase change; and (3) the magnitude of change, that is, how far the process drifts away from where it originally started. Each of these outcomes underscores a different way that digitization can influence processes and their dynamics.

The combination of three dependent variables and four independent variables results in a set of 12 propositions as summarized in Table 3 and discussed below. We summarize the results in qualitative terms because the magnitude is an artifact of simulation parameters. Each of these simulated effects can be tested in empirical research, if so desired.

Figures 4, 5, and 6 show an array of simulation results. Each figure has the same general layout to show multiple levels of each simulation parameter. Each row shows one level of the lexicon, L (100, 200, 300, 400). Each column shows one level of modularity, M (1, 5, 10, 20). Within each subplot, the x-axis is R (0, 50, 100, 150, 200) and the y-axis is the dependent variable (e.g., Figure 4 shows average process complexity on the y-axis). Within each subplot, each line represents a distinct level of variation, V (0.001, 0.005, 0.01). Thus, each figure summarizes the results of a full factorial design (4 × 4 × 5 × 3). Each point in each subplot represents the average result of 500 simulated trajectories.

## Average Process Complexity

In Figure 4, we see that complexity increases with increasing V and with increasing R, as expected.<sup>2</sup> The subplots in Figure 4 are arrayed to show the effect of L and M, as well. Looking down the columns of subplots, the size of the lexicon in creases from 100 to 400. Holding other parameters equal, increasing the number of possible actions for a process increases its complexity. If we regard the size of the lexicon

<table><tr><td colspan="4">Table 3. Predicted Effects of Digitization</td></tr><tr><td></td><td>Average Process Complexity(See Figure 4)</td><td>Probability of Endogenous Phase Change(See Figure 5)</td><td>Magnitude of Change(See Figure 6)</td></tr><tr><td>Size of Lexicon</td><td>Increase</td><td>Minimal effect</td><td>Minimal effect</td></tr><tr><td>Modularity</td><td>Decrease</td><td>Suppresses phase change</td><td>Preserves original process</td></tr><tr><td>Variation</td><td>Increase</td><td>Minimal effect</td><td>Large effect</td></tr><tr><td>Reinforcement</td><td>Increase</td><td>Large effect</td><td>Small effect</td></tr></table>

![](/api/attachments/EZ6ZBF3S/fulltext/images/0ad328ca8455ca5b6d1a4fcd8386973eeac024cdd87ea8f7516e73fe84a7f1b7.jpg)  
Figure 3. Average Process Complexity

as an indicator of component complexity (Wood 1986), we could say that component complexity correlates with process complexity. Across the rows in Figure 4, the number of modular divisions increases from 1 to 20. If we look across the rows, we can see that modularity tends to decrease process complexity (holding other process parameters equal). This result coincides with Simon’s (1996) explanation of modularity in the fable of Hora and Tempus. To the extent that digitization increases the modularity of a process, it tends to decrease the overall complexity of that process.

In sum, Figure 4 aligns with our intuition that on average, lexicon size, variability and memory increase complexity, while modularity decreases it. These results lend face validity to the model, but they do not speak to the question of dynamics: how does digitization influence the tendency of processes to undergo phase transitions?

## Probability of a Phase Change

In Figure 5, we show the same basic dimensions of digitalization (L, M, V and R), but the y-axis is the probability that the process trajectory will include a phase change. We use two key features to distinguish trajectories with a phase change: (1) at least one large burst of complexity; and (2) lower complexity after the phase change.<sup>3</sup> Thus, we are only counting the counterintuitive case where incremental change leads to lower complexity and fewer possible paths. The probability is simply the fraction of simulated trajectories that meet these criteria.

Unlike Figure 4, which generally conforms to our intuition, Figure 5 contains some surprises. The main message is that phase change is not only possible, it is likely over a wide range of circumstances. To see how digitization may influence this phenomenon, look down the columns of this figure. As you read down the figure, the simulation includes larger lexicon of actions (L). Notice that the top row is quite similar to the bottom row. So, while the size of the lexicon influences the average level of complexity of a process, it does not seem to influence the probability of a phase change.

Now look across the rows of this figure. In each row, the curves drop off more quickly at higher levels of modularity. Unlike the size of the process, modularity does seem to suppress the possibility of phase changes. This leads us to suggest that increased modularity tends to reduce the probability of a phase change.

Further, while phase change is impossible in a mechanistically automated process (R = 0), the effect is limited to that special case. In general, phase changes are most likely in processes with lower values of R. As soon as past performances begin to influence future performances, phase changes become likely (p > 0.5). As R increases, the probability of phase change is reduced. This is because edges are retained for more iterations. For processes with high modularity, phase changes can be minimized, but overall, our simulation leads us to expect that endogenous phase changes may be found in all corners of the digital world.

The most telling and interesting effect concerns the role of the parameters, V and R. Notice that in every subplot of Figure 4, there is a region where the chance of a phase change is quite high (approaching 100% in some cases). The effect is determined almost entirely by the parameter R. Contrary to our expectations, the level of variation, V, is largely irrelevant. A factor of 10 makes no visible difference throughout most of Figure 5.

While variation drives edge formation, “forgetting” (or lack of reinforcement) drives edge dissolution. Edge dissolution was the essential mechanism that ends the complexity peak, so it makes sense that it would appear in Figure 5 as a strong influence. When R is relatively low (\~R = 50), edges can dissolve fast. The process can freeze quickly into a new phase. When R is higher (\~R = 200), it freezes more slowly and tends to preserve a more complex structure, regardless of the level of variation. There is at least one spike in nearly every trajectory, but as R increases, these do not necessarily result in lower complexity.

## Magnitude of Process Change

In Figure 6, we show the same basic dimensions of digitali zation (L, M, V and R), but the dependent variable on the yaxis is the magnitude of process change over the course of the trajectory. This is measured by the percentage of edges from the original happy path that are retained after 5,000 process iterations.

As expected, complete automation eliminates process change. Modularity can help suppress change, as well, but the variability, V, has the largest effect. This makes sense, because this is the parameter that directly drives edge formation. As more edges form, the process will move away from the original happy path. In contrast, with the exception of full automation, R has relatively little effect. Low values of R are somewhat worse, but the main practical concern would be stopping variations in the first place (e.g, through programs like Six Sigma).

![](/api/attachments/EZ6ZBF3S/fulltext/images/a809f8359d0e633f6a1ada59e611c72d657d10e6aee72c3bfe7cb8724fb41608.jpg)  
Figure 5. Probability of a Phase Change

We have also examined the dispersion of the end states: How far are the trajectories from each other after 5000 iterations? The results are qualitatively similar. The main driver is variability. If an organization was operating multiple instances of the same process, they would not stay the same very long unless they are fully automated or managed by a process control regime of some sort.

## Discussion: Processual Dynamics in the Digitized World

Our simulation is theoretically interesting because we treat processes as generative, dynamic systems, rather than static objects. The process generates the performances, but at the same time, the performances generate the process (Feldman et al. 2016). This reciprocal relationship echoes a core principle in social theory (e.g., Giddens 1984), and in the theory of organizational routines (Feldman and Pentland 2003). The relationship between performances and processes also forms the basis for business process mining and discovery (Dumas et al. 2018; van der Aalst 2011), but in that line of research processes are generally conceptualized as stationary objects to be discovered.

Our simulation helps us theorize about how the reciprocal relationship between process and performance plays out in the digitized world, where processes are enacted by a mix of human and material agency (Leonardi 2011). Those were summarized in Table 3, and in Figures 4, 5 and 6. In addition to theorizing about the effects of digitization per se, we offer a number of insights about drift and digitization, contributions to complexity theory and practical significance, as described in the following sections.

![](/api/attachments/EZ6ZBF3S/fulltext/images/ce2274931cada77d29c9fa8df28ca500b19c8b35add991a3e57e737141f8419a.jpg)  
Figure 6. Magnitude of Process Change

## Drift in the Age of Intelligent Machines

Thirty years ago, when Zuboff (1988) framed our current understanding of what it meant to “automate” work, her analysis was based on the special case where adaptive humans deal with deterministic systems. In that corner of the digital world, the deterministic machines operate with V = 0 and

R = 0, but the people certainly do not. As a result, even when the technology was deterministic, the overall sociomaterial ensemble was not (Barley 1986; Desanctis and Poole 1994; Markus and Silver 2008; Orlikowski 1996). That is one of the main lessons from the last 30 years of research on technology in organizations

Looking forward, we confront a new and more difficult question: What will happen when adaptive systems work side by side with adaptive humans? These systems will take many different forms and we cannot know in advance the details of how they will function. We cannot collect data from event logs of processes that have yet to be designed, implemented and performed. We can, however, simulate what could happen and that is what we have done here.

Unlike their deterministic predecessors, adaptive systems will try new courses of action. They will take into account past experience. They will learn. In terms of our model, these systems will operate with R > 0 and V > 0. The specific level of these parameters will be different for different systems, and it is reasonable to ask whether our digitized assistants will be any better than humans at choosing what to do next. Certainly, one of the most promising aspects of digitization in general is the availability of better data for adaptation and learning (George et al. 2014).

In a recent review of reinforcement learning in the journal Nature, Littman (2015) explicitly discusses the potential for future practical applications of machine learning to problems that involve selecting a course of action (e.g., medical treatment plans). He articulates a number of concerns. First, he notes that in real situations, the computational burden can become “astronomically high,” so simplifying assumptions are required. For example, the algorithms that show the most promise make the critical simplifying assumptions that (1) the environment is stationary and (2) there are “no dependencies from one round of decision-making to the next” (p. 450). Unfortunately, in a wide variety of situations, these assumptions are incorrect. Furthermore, machine learning algorithms perform better with high quality feedback. As we discussed above, real processes performed by multiple actors in a constantly changing environment often provide poor feedback or no feedback at all (Rice and Cooper 2010).

While we have limited our formal model to endogenous systems with no feedback, the digital world is filled with opportunities for feedback, which is essential to learning (Huber 1991) and agility (Sambamurthy et al. 2003). At the same time, learning can lead to “competency traps” (Levitt and March 1988), where an organization becomes locked in to once efficient but now potentially ineffective patterns of action. Our simulation demonstrates how easily this can occur, even in the absence of external feedback.

Going forward, there is no doubt that digitized processes will be enacted in new and different ways. Automation is just one possibility among many. As we muddle through our daily lives with the help of our adaptive assistants, new edges will form and old edges will dissolve. Inevitably, processes will drift. When they do, we predict that they will be prone to unanticipated bursts of complexity followed by relative inertia.

## Self-Organizing Criticality in Processual Phenomena

The phase changes we describe here can be interpreted in terms of self-organizing criticality, an established concept in complexity theory which has been applied to explain the behavior of physical, biological and social systems (Bak et al. 1988; Frigg 2003; Levin 2005). Phase changes are often associated with dramatic metaphors, such as “tipping points” and “avalanches” (Frigg 2003). For example, Griod and Whittington (2015, p. 1522) describe “a process of progressive accumulation, by which the buildup of small changes finally creates insupportable pressures that explode into a greater event. The initial pattern of change may be incremental and slow, but, when positive feedback finally overwhelms restraining forces, the outcome is large and sudden.” When the system reaches the tipping point, behavior becomes chaotic or an avalanche occurs (Bak and Paczuski 1995). Miller and Page (2007) describe a similar phenomenon.

The specific, novel contribution of this research is the introduction of the notion of self-organized criticality into the world of process. It is based on a set of three closely related ideas that form the heart of this simulation model:

(1) the state of the process is modeled by a graph, not a vector of random variables;

(2) adding or removing specific edges can change the structure of the process; and

(3) the dynamics of this system are governed by the enacted pathways, not just by the average number of edges or nodes as assumed in much research on complexity in organizations (e.g., Wood 1986).

## Paths Define the Process and Enable the Dynamics

In a real business process, paths describe how products and services are created and delivered. The paths from start to finish (e.g., order to cash, purchase to pay) define how the process works, what it costs, how long it takes, and so on. Paths are central to the dynamics described here.

For a spike in complexity to occur, the network needs to gain paths, not just edges. As we explained above, the density of the network plays a major role in the dynamics. The network gains paths primarily by adding heavy edges: edges that have a disproportionately large influence on the number of paths because of their position in the network. Heavy edges generate more paths, and heavy edges are more likely to be reinforced because they sit on multiple paths. And since the network is becoming denser, the newly formed edges are more likely to be heavy. When the spike is building, the growth in process complexity is self-reinforcing.

Paths are the central mechanism in ending the complexity bursts, as well. The simulation traces a new path in each iteration, but it only retains the edges from the last R paths. At the height of process complexity, there are many possible paths, and therefore not every path can be followed. Some paths in the resulting network will be shorter than the original path. When the process follows shorter paths, it will tend to accelerate the tendency of the process to drop edges. Thus, the decline in complexity is self-reinforcing, as well.

Once the complexity bursts have subsided and the process has settled into a new regime, it will continue to drift by forming and dissolving edges. However, once the process enters a regime that reinforces shorter paths, it is unlikely to return to the original regime. Shorter paths allow fewer opportunities for variation, and they are more likely to be reinforced from start to finish, as whole paths. This self-reinforcement manifests itself as inertia, a common property of routines.

## Relationship to Classical Dynamic Systems Theory

Classical dynamic systems theory (and the idea of critical points, phase changes and attractors) originated in the mathematics of ordinary differential equations, where the state of the system was modeled by a vector of continuous variables (Forrester 1997). This class of models is consistent with orthodox variance-based thinking about organizations, where everything is treated as variable. As a result, the classical dynamic system framework is more parsimonious than the graph theoretic model we use here. In classical dynamic systems, phase changes are marked by “critical values” of model parameters and they can be precisely calculated. Here, phase changes are marked by changes to the structure of the system and their boundaries are less distinct. Empirically, this makes them harder to observe, but no less important.

## Relationship to nK Models

In some respects, random boolean networks (Kauffman 1993; Levinthal and Warglien 1999) offer a dramatic improvement over classical dynamic systems because they incorporate the network representation. However, these models assume a random pattern of connections in the graph, as defined by the parameter k. nK models are concerned with the average number of connections, not the specific connections, so they provide no insight into the question of how the specific configuration of edges might influence outcomes. In real processes, adding or removing a single edge can make the difference between a functioning process and a completely broken one. For example, if the connection between approval and payment was removed, no invoices would ever be paid.

## Relationship to Tipping Point Models

A system is said to exhibit self-organized criticality if it can reach its critical state, “where a single local event … can lead to effects that affect the system in its entirety” (Frigg 2003, p. 616), in a self-organized fashion, that is, without significant exogenous shocks. In our simulation, the process endogenously becomes incrementally more complex until it reaches its critical state. While a single grain of sand can precipitate an avalanche on a sandpile (Griod and Whittington 2015), the transformative effects we observe in our simulation require ongoing performance of the process. This is one reason why self-organizing criticality takes a distinctive quality in processual phenomena.

As they approach a critical state, systems may be operating on the boundary of a chaotic regime (Brown and Eisenhardt 1998; Carroll and Burton 2000), a regime that may provide opportunities for adaptation. In the domain of business processes, these models and metaphors are generally consistent with the results of our simulation. Like other examples of self-organizing criticality, our model shows that incremental changes can have disproportionate effects. Our simulation results allow us to formulate propositions on how to influence the likelihood and magnitude of these phase changes.

## Interpreting the Bursts of Complexity

The bursts of complexity in our model could be interpreted in very different ways: negatively, as a “complexity catastrophe” (Kauffman 1993; McKelvey 1999), or, more positively, as a “window of opportunity” (Tyre and Orlikowski 1994) with increased potential for agility (Sambamurthy et al. 2003).

It seems appropriate to characterize these bursts as a complexity catastrophe (Kauffman 1993; McKelvey 1999). During this phase, there would be so many ways to “get things done” that it would be difficult to say which is best, and difficult to judge the effects of particular improvements (where improvements are understood as adding/removing edges). As a manager or designer, it would be difficult to deliberately adapt the process to changing circumstances when it is in such a chaotic state.

At the same time, however, a period of high process com plexity could also be interpreted as a period of high adaptive potential. At the first sight, this interpretation of high process complexity values seems counterintuitive, but it fits the typical pattern of process adaptation that Tyre and Orlikowski (1994, p. 99) called the “window of opportunity”:

Our research finds that adaptation drops off dramatically after an initial burst of intensive activity.... We also find that this decline of adaptation is not irreversible, in that later, unexpected events can trigger new spurts of adaptive activity. These later episodes, however, are also of limited duration.

Tyre and Orlikowski explain these episodes in terms of factors that are mostly exogenous to the observed process, like the introduction of new technology or other exogenous pressures to change. Our simulation results provide a different, more endogenous explanation. Since the adaptiveness of an enacted process will depend on the number of paths remembered by the people enacting the process, high process complexity could make the process more adaptive. For example, when a variation leads to a new heavy edge, the many new paths that suddenly become possible could inspire a more effective way of enacting the process.

The subsequent process phase of reduced complexity and shorter sequences is also subject to competing interpretations. One interpretation would be that a shorter sequence is more efficient: through random variation, the system has eliminated unnecessary steps. In this view, the path got shorter, simpler and happier. Another interpretation would be that shorter sequences are incomplete, and therefore dysfunctional, because essential steps have been omitted. In this view, the path isn’t happy at all. Either way, the process has transformed and it has become more resistant to change.

## Beyond Drift: Designing for Processual Dynamics

A key theoretical move in this paper has been to focus on actions, rather than actors (Feldman et al. 2016; Pentland et al. 2017). Because of this focus, our framework offers a simple, general way to describe processual dynamics in terms of changes in a directed graph. Our simulation is limited to purely endogenous, emergent dynamics, but it raises an interesting possibility: Can we design processes with desirable dynamic properties?

Herbert Simon (1996, p. xii) argued that the sciences of the artificial are concerned “not with how things are but with how they might be—in short, with design.” By putting actions in the foreground, we are concerned not with how things might be, but with how actions might be. Of course, the emphasis on action is not entirely new. Business process management is concerned with patterns of action, but it generally emphasizes conformance and control (Dumas et al, 2018): ensuring that processes are enacted as designed, thereby eliminating drift and dynamics. Interaction design (Preece et al. 2015) is less focused on conformance, but is also oriented toward supporting particular goals and outcomes.

As agents operate in increasingly information-rich environments, the theoretical and practical challenge is whether we can help those agents make effective use of feedback to guide processual dynamics. Processes are enacted one action at a time, so actors are always faced with the problem of how their next action affects the overall process. As outlined above, there are good reasons to expect that this problem has no simple solution. However, our framework points to at least two design dimensions that might otherwise be overlooked. First, even with a modest lexicon, the space of possible process paths can be enormous. To search that space and gain feedback on which paths are better, process enactment needs to include variation. Variation implies nonconformity with the process-as-designed (i.e., workarounds), which is often viewed as undesirable (Alter 2014). From our perspective, variation provides an essential opportunity for feedback and learning (Bickhard and Campbell 2003).

Second, our model demonstrates that forgetting is just as important as learning. For a process to undergo a phase change to a new dominant path, edges and paths in the graph need to be removed. Without forgetting, variations will lead to continually increasing levels of complexity that diminish the adaptive capacity of the process (McKelvey 1999). If designers want to capitalize on feedback for process improvement, they need to consider that the beneficial effects of process complexity for adaptivity critically rely on forgetting. Without forgetting, there can be no phase change and no adaptation.

## Theoretical and Practical Significance

The possibility of phase change in digitized processes has a variety of theoretical and practical implications. Until these phenomena are documented in empirical research, these implications should be treated as propositions, not findings.

## Novel Explanation for Inertia and Change in Routines

The phase change that results from the complexity bursts can explain the “inertia” that is often seen as a characteristic of organizational routines (Cohen et al. 1996; Nelson and Winter 1984; Rice and Cooper 2010). After the phase change the processes have been more resistant to change. Even with the same level of variation, V, they do not continue to change outside of a very narrow range. Issues arise, but the routine does not change. This is a very common phenomenon in real world routines (Cohen et al. 1996), and it happens under a wide range of conditions in our simulation. Digitization can suppress drift and endogenous phase change (e.g., with very high modularity or deterministic automation), but such a process would have high inertia due to the digitization itself.

Paradoxically, the same mechanism that can cause inertia also leads us to a novel possibility for change. Where most change theories require a precipitating event or managerial intervention (Hayes 2014; Keen 1981; Lewin 1951; Pugh 2016; Schein 1994; Weick and Quinn 1999), our model suggests that the “precipitating event” can be the result of incremental change. As we mentioned above, we know that processes drift, but endogenous unfreezing is a novel possibility that could be exacerbated by digitization (e.g., by adding “flexibility” that reduces the effect of past actions on present choices).

## Practical Implications of Phase Change

These phase transitions are practically significant, as well. For example, in organizations that are trying to maintain consistent processes across multiple locations, minor drift is troublesome and potentially costly (Rozinat and van der Aalst 2005). Process consistency and control are major reasons that organizations introduce digital technology, like ERP systems (Berente et al. 2016). If minor drift is bad, then phase changes are potentially worse, especially when they are followed by inertia. Our theory offers some predictions about how design and use of digital technology can influence the probability and severity of these deviations.

If consistent processes are not an issue, neither is drift. But consider the case of so-called high reliability organizations (HROs) (Weick and Roberts 1993). When operations are tightly coupled, complex interactions are a known cause of “normal accidents” (Perrow 2011), such as reactors malfunctioning, aircraft falling down, or breakdown of money transfer systems. The actions and particularly the interactions of digitized processes are often both non-linear and dynamic (Perrow 2011). In settings where consistency matters, drift and subsequent phase change can have unexpected consequences for the efficiency and reliability of digitalized processes, and the phase changes themselves will increase the risk for new dysfunctional patterns.

Our model also aligns with the widely observed “worsebefore-better” dynamic in systems implementation (Sambamurthy and Zmud 2015; Valerdi and Fernandes 2011). When a business process is digitized (e.g., during ERP implementation), stakeholders often expect an immediate positive effect on organizational performance. Unfortunately, in some cases, work processes drift into dysfunctional patterns (Rice and Cooper 2010), become frozen into those patterns, and the expected benefits never emerge (Sambamurthy and Zmud 2015). The logic of our model applies: after a process enters a chaotic phase (e.g., systems implementation) it can quickly refreeze into a state that may or may not be desirable.

Awareness of phase change as a consequence of drift—even without exogenous shocks—should be useful for monitoring and managing risks in digitized processes. Phase changes are likely to occur relatively early in the trajectory of process, as it begins to accumulate alternative paths. Identifying and understanding these changes as they occur will be of practical significance to those managing digitized processes (Weick and Sutcliffe 2007).

Phase changes can also be triggered by external interventions, such as systems implementation. We do not explicitly model this kind of triggering, but the potentially problematic consequences arise during the refreezing. The more elements the respective business process has, and the more interdependent these elements are, the higher the costs of IS implementation (Sharma et al. 2008) and the more prolonged the phase of declining performance after implementation (Repenning and Sterman 2002). Regardless of how a phase change is triggered, the practical insight is that digitized processes have ongoing, internal dynamics that can result in unexpected outcomes. Our results show that these dynamics cannot be brought under control by simply shielding the process or system from exogenous shocks.

## Limitations and Future Work

The most important limitation of this work is the most obvious: it is a simulation. Simulations like this produce propositions, not findings. Our goal is not to devise a more expressive or accurate way to model any particular process. Rather, our goal is to theorize about the effects of digitization on process dynamics in general (Feldman et al. 2016). As Miller (2015) points out, every simulation involves a trade-off between veridicality and abstraction. Weick (1969) notes a similar trade-off between simplicity, accuracy and generality in theorizing. Our simulation is simple and general. It has only four parameters, so it cannot provide a realistic description of any particular process. As a result, there are a number of issues and opportunities the reader should consider in interpreting and extending this work, if so desired.

## Performance-Based Feedback and Learning

In our model, we do not include performance based feedback, costs, or other external factors. There are no incentives or feedback loops to influence changes in the process. There is no hierarchy or formal organization. The process parameters are fixed at the beginning of each trajectory, so any changes during the trajectory are strictly endogenous. In a sense, we have created a model for trial and error learning with a very simple objective function (to complete the path from source to sink). By changing the objective function (as in Pentland et al. 2012), it is possible to steer the trajectory of the process in different directions (Fu and Anderson 2008; Littman 2015). Future work could explore alternative kinds of performancebased feedback and algorithms to guide process enactment and process dynamics.

## Coevolution

We do not model coevolution of process and technology, as in Goh et al.’s (2011) study of evolving healthcare routines. Within this framework, coevolution could be modeled by changing the lexicon of possible actions. In some cases, technical evolution would increase restrictiveness (resulting in a smaller lexicon). In other cases, technical evolution would add new possible affordances. The same logic could be applied to coevolution of one process with other processes. For example, the clinical routines at the University of Rochester Medical Center may evolve in response to changes in related functions, such as billing or insurance. Coevolution would provide a theoretical basis for extending our model.

## Heterogeneous Agents

Our simulation does not explicitly identify particular agents or their properties. Technically, it is not an “agent based” simulation. Processes in the digitized world are carried out by ensembles of heterogeneous agents, but our model represents the tendencies of the sociomaterial ensemble as a whole. If some agents are fully automated, they would have R = 0, while other agents would have different values for R. In our model, we treat R as a property of the whole system, but it could also be conceptualized as a property of each agent that carries out the process. For example, the invoice processing system at the Norwegian Business School is programmed to take certain actions without human intervention (Pentland et al. 2011).

## Social Learning

The model we implement here is a classic example of trial and error learning (or learning by doing), but it does not include any element of social learning (Bandura and Walters 1977). Social learning has been identified as a key mechanism for propagation of beliefs and behavior in the digital world (Pentland 2015). Scholars who are interested in how the performance of one process might influence the performance of other processes could add a social learning component to the simulation.

## Empirical Validation

Empirical research on this phenomenon will require careful attention to research design. While the effects modeled here occur over a wide range of conditions, they are not universal and they may be difficult to observe. In our simulation, phase changes appear to happen within the first few thousand iterations of a process. Phase changes appear to be less likely in long-running processes that have already undergone many thousands of iterations and years of adaptation. The ruts in the road are there, but the process through which they were formed is long gone. If we follow a new process from inception, we have a much better opportunity to see these dynamics occur. The field study by Goh et al. (2011) provides a good example because they studied the introduction of new clinical routines and traced their evolution over time.

The most observable processes are supported by a single platform, such as invoice processing or medical record keeping. We can download the event log and look. But the digitized world contains an enormous array of processual phenomena, criss-crossing the boundaries of the organizational container (van der Aalst 2000; Winter et al. 2014). These processes may be more difficult to study.

Research on process mining provides a range of sophisticated tools for discovering processes from event logs (Dumas et al. 2018). Unfortunately, contemporary process mining approaches generally assume the process to be discovered is in steady state (Bose et al. 2011). In effect, endogenous change is treated as noise, rather than signal. Empirical research on this topic needs to use tools that are sensitive to the phenomena we are trying to understand.

## Conclusion

The simulation model we present here demonstrates that incremental change can create unexpected bursts of complexity, after which the process can enter a phase that is characterized by lower complexity, shorter paths and greater inertia. Our simulation predicts that these phase transitions are likely to occur over a wide range of digitized processes, with the exception of fully automated processes. The key theoretical idea is that incremental drift can lead to dramatic changes in process structure. This possibility has implications for process design, management and control. We hypothesize that digitization can be used to suppress, steer or accelerate these dynamics, but these ideas remain to be tested in empirical research.

## References

Alter, S. 2014. “Theory of Workarounds,” Communications of the Association for Information Systems (34), pp. 1041-1066.

Anderson, T. W., and Goodman, L. A. 1957. “Statistical Inference about Markov Chains,” The Annals of Mathematical Statistics (28:1), pp. 89-110.

Anderson, C., and Robey, D. 2017. “Affordance Potency: Explaining the Actualization of Technology Affordances,” Information and Organization (27:2), pp. 100-115.

Ardagna, D., and Pernici, B. 2007. “Adaptive Service Composition in Flexible Processes,” IEEE Transactions on Software Engineering (33:6), pp. 369-384.

Argote, L. 2013. Organizational Learning, Boston: Springer.

Augusto, A., Conforti, R., Dumas, M, La Rosa, M., and Bruno, G. 2018. “Automated Discovery of Structured Process Models from Event Logs: The Discover-and-Structure Approach,” Data & Knowledge Engineering (117), pp. 373-392.

Bak, P. 1996. “How Nature Works: The Science of Self-Organized Criticality,” Nature (383:6603), pp. 772-773.

Bak, P., Tang, C., and Wiesenfeld, K. 1988. “Self-Organized Criticality,” Physical Review A (38:1), pp. 364-374.

Bak, P., and Paczuski, M. 1995. “Complexity, Contingency, and Criticality,” Proceedings of the National Academy of Sciences of the United States of America (92:15), pp. 6689-6696

Barley, S. R. 1986. “Technology as an Occasion for Structuring: Evidence from Observations of CT Scanners and the Social Order of Radiology Departments,” Administrative Science Quarterly (31:1), pp. 78-108.

Bandura, A., and Walters, R. H. 1977. Social Learning Theory (Vol. 1), Englewood Cliffs, NJ: Prentice-Hall.

Basu, A., and Blanning, R. W. 2003. “Synthesis and Decomposition of Processes in Organizations,” Information Systems Research (14:4), pp. 337-355.

Bax, E. T. 1994. “Algorithms to Count Paths and Cycles,” Information Processing Letters (52:5), pp. 249-252.

Baxter, R. J., and Berente, N. 2010. “The Process of Embedding New Information Technology Artifacts into Innovative Design Practices,” Information and Organization (20:3-4), pp. 133-155.

Beer, R. D. 1995. “A Dynamical Systems Perspective on Agent– Environment Interaction,” Artificial Intelligence (72:1-2), pp. 173-215.

Berente, N., Lyytinen, K., Yoo, Y., and King, J. L. 2016. “Routines as Shock Absorbers During Organizational Transfor-

mation. Integration, Control, and NASA’s Enterprise Information System,” Organization Science (27:3), pp. 551-572.

Bickhard, M. H., and Campbell, D. T. 2003. “Variations in Variation and Selection: the Ubiquity of the Variation-and-Selective-Retention Ratchet in Emergent Organizational Complexity,” Foundations of Science (8:3), pp. 215-82.

Bose, R. P. J. C., van der Aalst, W. M. P., Žliobaitë, I., and Pechenizkiy, M. 2011. “Handling Concept Drift in Process Mining,” in Advanced Information Systems Engineering. CAiSE 2011. Lecture Notes in Computer Science (Vol. 6741), H. Mouratidis and C. Rolland (eds.), Berlin: Springer, pp. 391-405

Boudreau, M. C., and Robey, D. 2005. “Enacting Integrated Information Technology: A Human Agency Perspective,” Organization Science (16:1), pp. 3-18.

Brown, S. L., and Eisenhardt, K. M. 1998. Competing on the Edge: Strategy as Structured Chaos, Boston: Harvard Business Press.

Campbell-Kelly, M. 1996. “Information Technology and Organizational Change in the British Census, 1801–1911,” Information Systems Research (7:1), pp. 22-36.

Carroll, T., and Burton, R. M. 2000. “Organizations and Complexity: Searching for the Edge of Chaos,” Computational & Mathematical Organization Theory (6:4), pp. 319-337.

Casey, A. J. 1997. “Collective Memory in Organizations,” in Organizational Learning and Strategic Management, J. P. Walsh and A. S. Huff (eds.), Greenwich, CT: JAI Press, pp. 111-151.

Casey, A. J., and Olivera, F. 2011. “Reflections on Organizational Memory and Forgetting,” Journal of Management Inquiry (20:3), pp. 305-310.

Ciborra, C. U., Braa, K., Cordella, A., Dahlbom, B., Failla, A., Hanseth, O., Hepsø, V., Ljungberg, J., Monteiro, E., and Simon, K. A. 2000. From Control to Drift: The Dynamics of Corporate Information Infrastructures, Oxford, UK: Oxford University Press.

Cohen, M. D., and Bacdayan, P. 1994. “Organizational Routines Are Stored as Procedural Memory: Evidence from A Laboratory Study,” Organization Science (5:4), pp. 554-568.

Cohen, M. D., Burkhart, R., Dosi, G., Egidi, M., Marengo, L., Warglien, M., and Winter, S. 1996. “Routines and Other Recurring Action Patterns of Organizations: Contemporary Research Issues,” Industrial and Corporate Change (5:3), pp. 653-698.

D’Adderio, L. 2003. “Configuring Software, Reconfiguring Memories: the Influence of Integrated Systems on the Reproduction of Knowledge and Routines,” Industrial and Corporate Change (12:2), pp. 321-350.

Darr, E. D., Argote, L., and Epple, D. 1995. “The Acquisition, Transfer, and Depreciation of Knowledge in Service Organizations: Productivity in Franchises,” Management Science (41:11), pp. 1750-1762.

Davis, J. P., Eisenhardt, K. M., and Bingham, C. B. 2007. “Developing Theory through Simulation Methods,” Academy of Management Review (32:2), pp. 480-499.

DeSanctis, G., and Poole, M. S. 1994. “Capturing the Complexity in Advanced Technology Use: Adaptive Structuration Theory,” Organization Science (5:2), pp. 121-147.

Dekker, S. W. A. 2013. “Drifting into Failure: Complexity Theory and the Management of Risk,” Chaos and Complexity Theory for

Management: Nonlinear Dynamics, in S. Banerjee (ed.), Hershey, PA: IGI Global Business Science Reference, pp. 241-253.

Dekker, S., and Pruchnicki, S. 2014. “Drifting into Failure: Theorising the Dynamics of Disaster Incubation,” Theoretical Issues in Ergonomics Science (15:6), pp. 534-544.

Dittrich, K., Guérard, S., and Seidl, D. 2016. “Talking About Routines: The Role of Reflective Talk in Routine Change,” Organization Science (27:3), pp. 678-697.

Dumas, M., La Rosa, M., Mendling, J., and Reijers, H. A. 2018. Fundamentals of Business Process Management, Heidelberg: Springer.

Feldman, M. S., and Pentland, B. T. 2003. “Reconceptualizing Organizational Routines as a Source of Flexibility and Change,” Administrative Science Quarterly (48:1), pp. 94-118.

Feldman, M.S., Pentland, B. T., D’Adderio, L., and Lazaric, N. 2016. “Beyond Routines as Things: Introduction to the Special Issue on Routine Dynamics,” Organization Science (27:3), pp. 505-513.

Feldman, R. M., and Feldman, S. P. 2006. “What Links the Chain: An Essay on Organizational Remembering as Practice,” Organization (13:6), pp. 861-887.

Ferneley, E. H., and Sobreperez, P. 2006. “Resist, Comply or Workaround? An Examination of Different Facets of User Engagement with Information Systems,” European Journal of Information Systems (15:4), pp. 345-356.

Flood, R. L. 1987. “Complexity: A Definition by Construction of A Conceptual Framework,” Systems Research (4:3), pp. 177-185.

Forrester, J. W. 1997. “Industrial Dynamics,” Journal of the Operational Research Society (48:10), pp. 1037-1041.

Foster, J. 1997. “The Analytical Foundations of Evolutionary Economics: From Biological Analogy to Economic Self-Organization,” Structural Change and Economic Dynamics (8:4), pp. 427-451.

Freeman, L. 1977. “A Set of Measures of Centrality Based on Betweenness,” Sociometry (40:1), pp. 35-41.

Frigg, R. 2003. “Self-Organised Criticality—What it Is and What it Isn’t,” Studies in History and Philosophy of Science Part A (34:3), pp. 613-632.

Fu, W. T., and Anderson, J. R. 2008. “Solving the Credit Assignment Problem: Explicit and Implicit Learning of Action Sequences with Probabilistic Outcomes,” Psychological Research (72:3), pp. 321-330.

Gaskin, J., Berente, N., Lyytinen, K., and Yoo, Y. 2014. “Toward Generalizable Sociomaterial Inquiry: A Computational Approach for Zooming In and Out of Sociomaterial Routines,” MIS Quarterly (38:3), pp. 849-871.

George, G., Haas, M. R., and Pentland, A. 2014. “Big Data and Management,” Academy of Management Journal (57:2), pp. 321-326.

Giddens, A. 1984. The Constitution of Society: Outline of the Theory of Structuration, Berkeley, CA: University of California Press.

Girod, S. J., and Whittington, R. 2015. “Change Escalation Processes and Complex Adaptive Systems: From Incremental Reconfigurations to Discontinuous Restructuring,” Organization Science (26:5), pp. 1520-1535.

Goh, J. M., Gao, G., and Agarwal, R. 2011. “Evolving Work Routines: The Adaptive Routinization of Technology in Healthcare,” Information Systems Research (22:3), pp. 565-585.

Günther, C. W., Rinderle, S., Reichert, M., and van Der Aalst, W. 2006. “Change Mining in Adaptive Process Management Systems,” in On the Move to Meaningful Internet Systems 2006: CoopIS, DOA, GADA, and ODBASE, R. Meersman and Z. Tari (eds.), Berlin: Springer, pp. 309-326.

Grimm, V., Revilla, E., Berger, U., Jeltsch, F., Mooij, W. M., Railsback, S. F., Thulke, H. H., Weiner, J., Wiegand, T., and DeAngelis, D. L. 2005. “Pattern-Oriented Modeling of Agent-Based Complex Systems: Lessons from Ecology,” Science (310:5750), pp. 987-991.

Hærem, T., Pentland, B. T., and Miller, K. D. 2015. “Task Complexity: Extending a Core Concept,” Academy of Management Review (40:3), pp. 446-460.

Halbesleben, J. R. B., Wakefield, D. S., and Wakefield, B. J. 2008. “Work-Arounds in Health Care Settings: Literature Review and Research Agenda,” Health Care Management Review (33:1), pp. 2-12.

Hayes, J. 2014. The Theory and Practice of Change Management, London: Palgrave Macmillan.

Holan, P. M. D., and Phillips, N. 2004. “Remembrance of Things Past? The Dynamics of Organizational Forgetting,” Management Science (50:11), pp. 1603-1613.

Huber, G. P. 1991. “Organizational Learning: The Contributing Processes and the Literatures,” Organization Science (2:1), pp. 88-115.

Isern, D., and Moreno, A. 2016. “A Systematic Literature Review of Agents Applied in Healthcare,” Journal of Medical Systems (40:2), Article 43.

Kauffman, S. A. 1993. The Origins of Order: Self-Organization and Selection in Evolution, New York: Oxford University Press.

Keen, P. G. 1981. “Information Systems and Organizational Change,” Communications of the ACM (24:1), pp. 24-33.

Kluge, A., and Gronau, N. 2018. “Intentional Forgetting in Organizations: The Importance of Eliminating Retrieval Cues for Implementing New Routines,” Frontiers in Psychology (9:51), pp. 1-17.

Koppel, R., Wetterneck, T., Telles, J. L., and Karsh, B. T. 2008. “Workarounds to Barcode Medication Administration Systems: Their Occurrences, Causes, and Threats to Patient Safety,” Journal of the American Medical Informatics Association (15:4), pp. 408-423.

Koopman, P., and Hoffman, R. R. 2003. “Work-Arounds, Make-Work, and Kludges,” IEEE Intelligent Systems (18:6), pp. 70-75.

Kossek, E. E., Young, W., Gash, D. C., and Nichol, V. 1994. “Waiting for Innovation in the Human Resources Department: Godot Implements A Human Resource Information System,” Human Resource Management (33:1), pp. 135-159.

Kremser, W., and Schreyögg, G. 2016. “The Dynamics of Interrelated Routines: Introducing the Cluster Level,” Organization Science (27:3), pp. 698-721.

Leonardi, P. M. 2011. “When Flexible Routines Meet Flexible Technologies: Affordance, Constraint, and the Imbrication of Human and Material Agencies,” MIS Quarterly (35:1), pp. 147-167.

Levin, S. A. 2005. “Self-Organization and the Emergence of Complexity in Ecological Systems,” Bioscience (55:12), pp. 1075-1079.

Levinthal, D. A., and Warglien, M. 1999. “Landscape Design: Designing for Local Action in Complex Worlds,” Organization Science (10:3), pp. 342-357.

Levitt, B., and March, J. G. 1988. “Organizational Learning,” Annual Review of Sociology, 14(1), 319-338.

Lewin, K. 1951. Field Theory in Social Science, New York: Harper & Brothers.

Littman, M. L. 2015. “Reinforcement Learning Improves Behaviour from Evaluative Feedback,” Nature (521:7553), pp. 445-451.

Loo, J., Mauri, J. L., and Ortiz, J. H. 2016. Mobile Ad Hoc Networks: Current Status and Future Trends, Boca Raton, FL: CRC Press.

Lyytinen, K., and Newman, M. 2008. “Explaining Information Systems Change: A Punctuated Socio-Technical Change Model,” European Journal of Information Systems (17:6), pp. 589-613.

Lyytinen, K., Newman, M., and Al-Muharfi, A. R. A. 2009. “Institutionalizing Enterprise Resource Planning in the Saudi Steel Industry: A Punctuated Socio-Technical Analysis,” Journal of Information Technology (24:4), pp. 286-304.

Maes, P. 1993. “Modeling Adaptive Autonomous Agents,” Artificial Life (1:1-2), pp. 135-162.

Markus, M. L., and Silver, M. S. 2008. “A Foundation for the Study of IT Effects: A New Look at DeSanctis and Poole’s Concepts of Structural Features and Spirit,” Journal of the Association for Information systems (9:10), Article 5.

McCabe, T. J. 1976. “A Complexity Measure,” IEEE Transactions on Software Engineering (4), pp. 308-320.

McKelvey, B. 1999. “Avoiding Complexity Catastrophe in Coevolutionary Pockets: Strategies for Rugged Landscapes,” Organization Science (10:3), pp. 294-321.

Miller, K. D. 2015. “Agent-Based Modeling and Organization Studies: A Critical Realist Perspective,” Organization Studies (36), pp. 175-196.

Miller, J. H., and Page, S. E. 2007. Complex Adaptive Systems: An Introduction to Computational Models of Social Life, Princeton, NJ: Princeton University Press.

Mortazavi, A., Khamseh, A. A., and Azimi, P. 2015. “Designing of an Intelligent Self-Adaptive Model for Supply Chain Ordering Management System,” Engineering Applications of Artificial Intelligence (37), pp. 207-220.

Nan, N. 2011. “Capturing Bottom-Up Information Technology Use Processes: A Complex Adaptive Systems Model,” MIS Quarterly (35:2), pp. 505-532.

Nan, N., and Tanriverdi, H. 2017. “Unifying the Role of IT in Hyperturbulence and Competitive Advantage Via a Multilevel Perspective of IS Strategy,” MIS Quarterly, (41:3), pp. 937-958.

Nelson, R. R., and Winter, S. G. 1982. An Evolutionary Theory of Economic Change, Cambridge, MA: Belknap Press.

Nunamaker Jr., J. F., Chen, M., and Purdin, T. D. 1990. “Systems Development in Information Systems Research,” Journal of Management Information Systems (7:3), pp. 89-106.

Nuxoll, A. M., and Laird, J. E. 2012. “Enhancing Intelligent

Agents with Episodic Memory,” Cognitive Systems Research (17), pp. 34-48.

Orlikowski, W. J. 1996. “Improvising Organizational Transformation Over Time: A Situated Change Perspective,” Information Systems Research (7:1), pp. 63-92.

Orlikowski, W. J. 2000. “Using Technology and Constituting Structures: A Practice Lens for Studying Technology in Organizations,” Organization Science (11:4), pp. 404-428.

Orlikowski, W. J., and Scott, S. V. 2008. “Sociomateriality: Challenging the Separation of Technology, Work and Organization,” Academy of Management Annals (2:1), pp. 433-474.

Pentland, A. 2015. Social Physics: How Social Networks Can Make Us Smarter, New York: Penguin Books.

Pentland, B. T., and Feldman, M. S. 2008. “Designing Routines: On the Folly of Designing Artifacts, While Hoping for Patterns of Action,” Information and Organization (18:4), pp. 235-250.

Pentland, B. T., Feldman, M. S., Becker, M. C., and Liu, P. 2012. “Dynamics of Organizational Routines: A Generative Model,” Journal of Management Studies (49:8), pp. 1484-1508.

Pentland, B. T., Hærem, T., and Hillison, D. 2011. “The (N)Ever-Changing World: Stability and Change in Organizational Routines,” Organization Science (22:6), pp. 1369-1383.

Pentland, B., Recker, J., and Wyner, G. 2015. “A Thermometer for Interdependence: Exploring Patterns of Interdependence Using Networks of Affordances,” in Proceedings of the 36<sup>th</sup> International Conference on Information Systems, Fort Worth, TX.

Pentland, B. T., Pentland, A. P., and Calantone, R. J. 2017. “Bracketing Off the Actors: Towards an Action-Centric Research Agenda,” Information and Organization (27:3), pp. 137-143.

Perrow, C. 2011. Normal Accidents: Living with High Risk Technologies, Princeton, NJ: Princeton University Press.

Petrides, L. A., McClelland, S. I., and Nodine, T. R. 2004. “Costs and Benefits of the Workaround: Inventive Solution or Costly Alternative,” International Journal of Educational Management (18:2), pp. 100-108.

Poole, M. S., Lambert, N., Murase, T., Asencio, R., and McDonald, J. 2016. “Sequential Analysis of Processes,” Chapter 16 in The SAGE Handbook of Process Organization Studies, A. Langley and H. Tsoukas (eds), Washington, DC: SAGE Publishing.

Pugh, L. 2016. Change Management in Information Services, Abingdon, England: Routledge.

Preece, J., Rogers, Y., and Sharp, H. 2015. Interaction Design: Beyond Human–Computer Interaction, Hoboken, NJ: John Wiley & Sons.

Ram, A., and Santamaría, J. C. 1997. “Continuous Case-Based Reasoning,” Artificial Intelligence (90:1-2), pp. 25-77.

Reijers, H., and Mendling, J. 2008. “Modularity in Process Models: Review and Effects,” in Proceedings of the 6<sup>th</sup> International Conference on Business Process Management, Milan, Italy, pp. 20-35.

Repenning, N. P., and Sterman, J. D. 2002. “Capability Traps and Self-Confirming Attribution Errors in the Dynamics of Process Improvement,” Administrative Science Quarterly (47:2), pp. 265-295.

Rerup, C., and Feldman, M. S. 2011. “Routines as a Source of Change in Organizational Schemata: The Role of Trial-and-Error Learning,” Academy of Management Journal (54:3), pp. 577-610.

Rice, R. E., and Cooper, S. D. 2010. Organizations and Unusual Routines: A Systems Analysis of Dysfunctional Feedback Processes, Cambridge, UK: Cambridge University Press.

Rozinat, A., and van der Aalst, W. M. 2005. “Conformance Testing: Measuring the Fit and Appropriateness of Event Logs and Process Models,” in Business Process Management Workshops, BPM 2005. Lecture Notes in Computer Science (Vol. 3812), C. J. Bussler and A. Haller (eds.), Berlin: Springer, pp. 163-176.

Ryan, J. L., Pinto, D., Pentland, A. P., and Pentland, B. T. 2016. “Complexity Thermometer: Unraveling Complexity of Clinic Process,” Journal of Investigative Dermatology (136:5), p. S26.

Sambamurthy, V., Bharadwaj, A., and Grover, V. 2003. “Shaping Agility through Digital Options: Reconceptualizing the Role of Information Technology in Contemporary Firms,” MIS Quarterly (27: 2), pp. 237-263.

Sambamurthy, V., and Zmud, R. 2015. Business Platforms, Digital Platforms and Digital Innovation: An Executive Agenda, Tallahassee, FL: Legerity Digital Press.

Schein, E. H. 1994. “Management of Change: The Case of Information Technology,” in Information Technology and the Corporation of the 1990s: Research Studies, T. J. Allen and M. S. Scott Morton (eds.), New York: Oxford University Press, pp. 325-341.

Schultze, U., Aanestad, M., Mähring, M., Østerlund, C., and Riemer, K. (eds.). 2018. Living with Monsters? Social Implications of Algorithmic Phenomena, Hybrid Agency and the Performativity of Technology, Basel: Springer Nature Switzerland AG.

Silver, M. S. 1990. “Decision Support Systems: Directed and Nondirected Change,” Information Systems Research (1:1), pp. 47-70.

Simon, H. A. 1996. The Sciences of the Artificial (3<sup>rd</sup> ed.), Cambridge, MA: MIT Press.

Sharma, R., Yetton, P. W., and Zmud, R. W. 2008. “Implementation Costs of IS-Enabled Organizational Change,” Information and Organization (18:2), pp. 73-100.

Strong, D. M., Volkoff, O., Johnson, S. A., Pelletier, L., R., Tulu, B., Isa, B.-O., Trudel, J., and Garber, L. 2014. “A Theory of Organization–EHR Affordance Actualization,” Journal of the Association for Information System (15:2), pp. 53-85.

Treleaven, P., Galas, M., and Lalchand, V. 2013. “Algorithmic Trading Review,” Communications of the ACM (56:11), pp. 76-85.

Tyre, M. J., and Orlikowski, W. J. 1994. “Windows of Opportunity: Temporal Patterns of Technological Adaptation in Organizations,” Organization Science (5:1), pp. 98-118.

Valerdi, R., and Fernandes, B. 2011. “Underestimation in the ‘When it Gets Worse Before it Gets Better’ Phenomenon in Process Improvement,” in Improving Complex Systems Today: Proceedings of the 18<sup>th</sup> ISPE International Conference on Concurrent Engineering, D. D. Frey, S. Fukuda, and G. Rock (eds.), London: Springer, pp. 3-10.

van der Aalst, W. M. P. 2000. “Loosely Coupled Interorganizational Workflows: Modeling and Analyzing Workflows Crossing Organizational Boundaries,” Information & Management (37:2), pp. 67-75.

van der Aalst, W. M. P. 2011. Process Mining: Discovery, Conformance and Enhancement of Business Processes, Heidelberg: Springer.

Volkoff, O., Strong, D. M., and Elmes, M. B. 2007. “Technological Embeddedness and Organizational Change,” Organization Science (18:5), pp. 832-848.

Walsh, J. P., and Ungson, G. R. 1991. “Organizational Memory,” Academy of Management Review (16:1), pp. 57-91.

Weick, K. E. 1969. The Social Psychology of Organizing, New York: McGraw-Hill.

Weick, K. E., and Quinn, R. E. 1999. “Organizational Change and Development,” Annual Review of Psychology (50:1), pp. 361-386.

Weick, K. E., and Roberts, K. H. 1993. “Collective Mind in Organizations: Heedful Interrelating on Flight Decks,” Administrative Science Quarterly (38:3), pp. 357-381.

Weick, K. E., and Sutcliffe, K. M. 2007. Managing the Unexpected: Resilient Performance in an Age of Uncertainty, San Francisco: Jossey-Bass.

West, D. B. 2001. Introduction to Graph Theory, Upper Saddle River, NJ: Prentice Hall.

Winter, S., Berente, N., Howison, J., and Butler, B. 2014. “Beyond the Organizational ‘Container’: Conceptualizing 21<sup>st</sup> Century Sociotechnical Work, “Information and Organization (24:4), pp. 250-269.

Wood, R. E. 1986. “Task Complexity: Definition of the Construct,” Organizational Behavior and Human Decision Processes (37:1), pp. 60-82.

Yoo, Y. 2010. “Computing in Everyday Life: A Call for Research on Experiential Computing,” MIS Quarterly (34:2), pp. 213-231.

Yoo, Y., Henfridsson, O., and Lyytinen, K. 2010. “Research Commentary—The New Organizing Logic of Digital Innovation: An Agenda for Information Systems Research,” Information Systems Research (21:4), pp. 724-735.

Zhang, Y., Qian, C., Lv, J., and Liu, Y. 2017. “Agent and Cyber-Physical System Based Self-Organizing and Self-Adaptive Intelligent Shopfloor,” IEEE Transactions on Industrial Informatics (13:2), pp. 737-747.

Zuboff, S. 1988. In the Age of the Smart Machine: The Future of Work and Power, New York: Basic Books.

## About the Authors

Brian T. Pentland is the Main Street Capital Partners Endowed Professor in the Broad College of Business at Michigan State University. His creative work has appeared in Academy of Management Review, Administrative Science Quarterly, Journal of Management Studies, Management Science, MIS Quarterly, Organization Science, and Organization Studies, on YouTube, and elsewhere.

Peng Liu is an assistant professor in the Information Systems and Decision Sciences Department, at the Mihaylo College of Business and Economics, California State University, Fullerton. His research interests include organizational routines and capabilities, the impact of IT on routines and organizations, and IT governance. Peng has published in journals such as Information Systems Management and IT Professional.

Waldemar Kremser is an assistant professor at Radboud University. In his research, combines a practice perspective on roles and routines with insights from complexity theory and organization design to better understand phenomena such as new forms of organizing, self-reinforcing dynamics, and radical innovations. In exploring these phenomena empirically, he often combines ethnographic research with the analysis of various forms of digital trace data. His research has been published in outlets such as Organization Science and Research in the Sociology of Organizations.

Thorvald Hærem is an associate professor at BI Norwegian Business School. His research interests include organizational and individual routines, behavioral decision making, and information processing in organizations. He has published research in journals such as Journal of Applied Psychology, Journal of Behavioral Decision Making, Organization Studies, Organization Science, Leadership Quarterly, and Academy of Management Review.

## Appendix A

## Simulation Model

This function will generate one simulation trajectory. It will plot the initial and final history matrix, and the estimated complexity of the process after each iteration.

function Make\_One\_Complexity\_Trajectory() %% This is the code used to simulate complexity trajectories

% initialize the main parameters % N = number of time steps N =1000;

% V = variation (probability of random variation in sequences) V= 0.1;

% L = size of lexicon, maximum size of the LxL history matrix L = 30;

% U = Number of sub-Units to divide the lexicon into. L/U should be % integer. U = 1;

% R = size of window for new history matrix (R = “retained”) R =50;

% H = History matrix H = zeros(L,L);

% S = sequences -- this is also a key working structure % Each cell in the array contains a sequence, one sequence per time step. % you need an extra “R” for the initial set. S = cell(1,N+R);

% cut off paths that are longer than 5x the size of the lexicon. % this prevents infinite loops Max\_Seq\_Length = 5\*L;

```matlab
% History of history matrices - keep for computing distances
% H_History = zeros(L,L,N);

% load data from prior runs? if file does not already exist, set this to zero.
% load_existing=1;

% initialize or load data from prior runs?
data = struct;

% Output array...
C = zeros(1,N); % Complexity

%% Initialize the Happy Path, history matrix and initial sequences
for i=1:L-1
    H(i,i+1) = 1;
end

for i=1:R
    S{i} = [1:L];
end

figure
H=H*300;
    image(H,'CDataMapping','scaled')
    image(H)

colormap(flipud(hot))
colorbar

%% Now loop through N time steps
for t=1:N

    % Get the next sequence, based on the history matrix and
    % probability of variation, V

    [S{t+R}] = generate_new_S(H, V, Max_Seq_Length, L, U)

    % Now recompute the history matrix based on previous R sequences
    if R>0
    H = get_new_H(S(1,t:t+R), L);
    end

    % Compute metrics for analysis
    C(t) = get_complexity(H);

end

%% %% feature extraction from the complexity trace
% smooth with moving average
Cmean = movmean(C,10);

%% display results
plot_results(Cmean, 'Process Complexity');
```

```matlab
figure
H=H*300;
    image(H,'CDataMapping','scaled')
    image(H)

colormap(flipud(hot))
colorbar

%% Generate a new sequence
function [ns] = generate_new_S(h, v, max_length, L, U)

% assign the global source and sink
global_source=1;
global_sink=size(h,1);

% get the local source/sink for each sub-unit U
[source, sink] = get_source_and_sink(L, U);

% Get a viable sequence that starts at the global_source and ends at
% the global_sink. Limit to max_length
ns=[global_source];
next_step=global_source;

while next_step < global_sink

    % get the range of values for this unit
    r=[(source(next_step)+1):sink(next_step)];

    % First check for r=1 (units have only source/sink
    if length(r)==1

    next_step=next_step+1;

    else

    % This is path following...
    if rand()>v

    % All zero row means you are at global_sink
    if sum(h(next_step,:))==0
    next_step = global_sink;

    % when you hit a unit sink, go to the next unit
    elseif next_step == sink(next_step)
    next_step = next_step+1;

    else
    % guard against case where we jump to zero place...
    if sum(h(next_step,r))>0
    next_step = randsample(r,1,true,h(next_step,r));
    else
    next_step = randsample(r,1);
    end

end
```

else % workaround is needed

```matlab
% but not in the case where you are a unit sink
    if next_step == sink(next_step)
    next_step = next_step + 1;

    else

    next_step = randsample(r,1);

    end

    end

    % Prevent infinite loop
    if length(ns) >= max_length
    break;
    % next_step = global_sink;
    end

    % concatenate the next step onto the sequence
    ns = [ns next_step];

    end % r == 1 if -else
    end % while loop

    end
    %% Fill in source and sink for multiple units
    function [source, sink] = get_source_and_sink(L, U)

    Source = zeros(L, 1);
    sink = zeros(L, 1);

    % r is the range of each sub-unit
    r = L / U;

    loop through the lexicon and assign source / sink for each
    for i = 1 : L

    unitNum = 1 + floor((i - 1) / r);

    source(i) = 1 + (unitNum - 1) * r;

    sink(i) = unitNum * r;

    end
end

%% Generate a new history matrix
function new_H = get_new_H(s, l)

    new_H = zeros(l, l);

    % get the number of sequences
    r = size(s, 2);

    % loop for each sequence
    for i = 1 : r
```

```matlab
seq = s{i};
for e=1:length(seq)-1
    new_H(seq(e), seq(e+1)) = new_H(seq(e), seq(e+1)) + 1;
end

end

% normalize the values within each row
for row=1:l
    if sum(new_H(row,:)) == 0
    new_H(row,:)=new_H(row,:);
    elseif sum(new_H(row,:)) > 0
    new_H(row,:)= new_H(row,:)/sum(new_H(row,:));
    end
end

end

%% compute the drift using hamming distance between the two arrays.
function d = drift(h1, h2)

%    d = sum(sum((h1-h2).^2))^0.5;
    h1 = double(h1>0);
    h2 = double(h2>0);
    d = pdist([h1(:)'; h2(:)'], 'hamming');

end

%% compute complexity index
function c = get_complexity(h )

    % Vertices
    v = size(h,1);

    % Edges
    e = sum(sum(h>0));

    % compute complexity index
    cidx = 0.08 + 0.08*e - 0.08*v;

    % exponentiate to get the estimated number of paths
    c=10^cidx;

end

%% plot the results
function plot_results(Y_var, Y_label)
figure
xRun = [1:size(Y_var,2)];
hComp = plot(xRun, Y_var);
set(hComp, 'LineStyle', '-', 'LineWidth', 1.0, 'Color', 'Black');
set(hComp, 'Marker', 'o', 'MarkerFaceColor', [0.1 0.1 0.1], 'MarkerEdgeColor', [0 0 0], 'MarkerSize', 2.0);
xlabel('Process Iterations', 'FontSize', 16);
ylabel(Y_label, 'FontSize', 16, 'Rotation', 90);

end

end
```
