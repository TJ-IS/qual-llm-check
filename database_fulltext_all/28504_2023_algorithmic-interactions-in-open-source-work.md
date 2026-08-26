---
otero_id: 28504
otero_key: "H6WG3WEF"
title: "Algorithmic Interactions in Open Source Work"
authors: "Maha Shaikh; Emmanuelle Vaast"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1153"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Algorithmic Interactions in Open Source Work

Maha Shaikh,<sup>a,</sup>\* Emmanuelle Vaast<sup>b</sup>

<sup>a</sup> King’s College London, London WC2R 2LS, United Kingdom; <sup>b</sup> Desautels Faculty of Management, McGill University, Montreal, Quebec H3A 1G5, Canada

Contact: maha.shaikh@kcl.ac.uk, https://orcid.org/0000-0001-5110-1619 (MS); emmanuelle.vaast@gmail.com, https://orcid.org/0000-0003-2194-883X (EV)

Received: January 11, 2019 Revised: November 22, 2019; July 8, 2020; July 26, 2021; March 23, 2022; May 20, 2022 Accepted: May 27, 2022 Published Online in Articles in Advance: July 20, 2022

https://doi.org/10.1287/isre.2022.1153

Copyright: © 2022 INFORMS

Abstract. This study focuses on algorithmic interactions in open source work. Algorithms are essential in open source because they remedy concerns incompletely addressed by parallel development or modularity. Following algorithmic interactions in open source allows us to map the performance of algorithms to understand the nature of work conducted by multiple algorithms functioning together. We zoom to the level of algorithmic interactions to show how residual interdependencies of modularity are worked around by algorithms. Moreover, the dependence on parallel development does not suf<sup>fi</sup>ce to resolve all concerns related to the distributed work of open source. We examine the Linux Kernel case that reveals how algorithmic interactions facilitate open source work through the three processes of managing, organizing, and supervising development work. Our qualitative study theorizes how algorithmic interactions intensify through these processes that work together to facilitate development. We make a theoretical contribution to open source scholarship by explaining how algorithmic interactions navigate across module rigidity and enhance parallel development. Our work also reveals how, in open source, developers work to auto mate most tasks and augmentation is a bidirectional relationship of algorithms augmenting the work of developers and of developers augmenting the work of algorithms.

History: Hemant Jain, Balaji Padmanabhan, Paul Pavlou, and Raghu Santanam, Senior Editors; Likoebe Maruping, Associate Editor.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1153.

Keywords: algorithmic interactions open source work modularity parallel development augmentation and automation qualitative stud

## Introduction

Open source software work relies on technology to mediate, communicate, and coordinate development (Koike and Chu 1997, Fogel 1999, Atkins et al. 2002). Open source involves developing complex software in online settings with limited face-to-face contact (Fitzgerald and Feller 2002, Lakhani and von Hippel 2003). Working across temporal and spatial boundaries can be challenging. In open source, challenges of managing work in distributed settings have been mitigated through parallel development and modularity (Fitzgerald 2004). Parallel development is the provision to work on the same system or module by multiple developers at the same time (Feller and Fitzgerald 2002). Coupled with modularity— the ability to decompose a large and complex problem, system, or function into smaller manageable components that relate to each other through a common interface (Langlois and Garzarelli 2008)—parallel development can mitigate many problems of open source work.

In practice, however, open source work also necessitates the reliance on numerous algorithms that enable the process of software development and manage residual issues not resolved by parallel development and modularity. Algorithms are sets of instructions that can be computed to achieve a result or goal (Moschovakis 2001). Social scientists adopt a broader perspective that acknowledges relational aspects of algorithms and a degree of uncertainty in how they work in practice (Lynch 2017). A relational understanding of algorithms includes the possibility of unforeseen outcomes arising from any set of algorithmic instructions interacting with other algorithms and humans (Orlikowski and Scott 2015). We adopt this broader relational understanding of algorithms for ou study on open source where algorithms perform a key role in mitigating problems associated with a poor or overmodularized system that suffers from breakdowns in parallel development. Building algorithms to magnify certain procedures or to mitigate problems offers <sup>fl</sup>exibility that rigid design rules would not otherwise afford (Tel 2000). A reliance on algorithms to help manage work breakdowns is typical and essential in open source (Lynch 1996, Nugroho et al. 2020).

The work of algorithms involves interactions not only with users but also with other algorithms (Teodorescu et al. 2021). Signi<sup>fi</sup>cantly, algorithms and their interactions are not entirely predictable (Lazer 2015). Algorithms are lines of instructions that are supposed to follow through as directed when commanded. Yet algorithms do not always operate as expected: some freeze and stall midway through execution; others break down and provide incorrect data (Salovaara et al. 2019). Also, if diverse algorithms instruct one another to initialize and operate, then interactions among algorithms can produce unanticipated consequences (Lazer 2015). Interactions are important because seldom does an algorithm operate in isolation without initialization by a human or another algorithm. It is thus pertinent to focus on interactions among multiple algorithms as well as algorithms and humans—that is, algorithmic interactions. Such a focus will allow us to examine the unanticipated consequences that often emerge through algorithmic use in open source. These issues prompt an important discussion of how algorithms are being employed in open source work settings and the signi<sup>fi</sup>cance of how they unfold.

We need to understand the implications of algorithmic interactions in open source because algorithms rarely operate in isolation. Open source relies heavily on multiple algorithms that work together to complete basic tasks (Atkins et al. 2002, Kornilov and Safonov 2018). Even a simple task such as merging involves more than one algorithm, so the interactions among algorithms, as they work together, become critical. It is often at points of interaction that unpredictability arises. Working with algorithms and interacting with them leads to different results even when the same algorithm is run in the same manner. We need to account for the unpredictability that arises from algorithms interacting with humans and other algorithms in open source. Thus, in this study we ask the following: How do algorithmic interactions shape open source work? Our question prompts the in-depth examination of algorithm to algorithm interactions as well as algorithms and human interactions in a revealing context (Neyland and Mollers¨ 2017). Our context is the Linux Kernel development community and their design and use of three distinct algorithms that worked to mitigate residual concerns of modularity and parallel development.

The main contributions of this work include, <sup>fi</sup>rst, a conceptualization of how algorithmic interactions in open source are sustained and modi<sup>fi</sup>ed to manage across module rigidity issues (Baldwin and Clark 2006). Our process understanding of building and sustaining algorithmic interactions reveals how open source work manages parallel development, organizes residual issues of modularity, and supervises an increased reliance on sophisticated algorithm-to-algorithm interactions. Scholarship has shown technology and developers working together to manage online tasks (Howison and Crowston 2014, Lindberg et al. 2016). We add a theorization of three processes that together deepen the scope and reach of algorithmic interactions to remedy lingering concerns with parallel development and modularity.

Second, our work contributes to an understanding of how algorithmic interactions create the possibility of augmentation and/or automation in open source work. Developers draw on algorithmic interactions to reduce their involvement with hard–to-trace problems in open source development. Greater reliance on algorithms to automate certain tasks while working with them to augment others reinforces and strengthens algorithmic interactions. Contrary to prior studies on augmentation where automation and augmentation are seen as separate (Grønsund and Aanestad 2020) and largely, the domain of humans (Raisch and Krakowski 2021) we show how, in open source, developers are equally likely to augment the work of algorithms as vice versa.

Third, our study furthers scholarship on working with algorithms. Prior work argues that when people are used to maintain algorithms, human effort becomes invisible, menial, and tedious (Ekbia et al. 2015b, Ekbia and Nardi 2017). Our investigation of an open source community instead uncovers the value that designing and maintaining algorithmic interactions holds for developers, which has implications for other contexts such as platform work and crowdsourcing.

In the next section we present our theoretical foundations followed by our research methods. Next, the <sup>fi</sup>ndings highlight different sets of algorithms that the Linux Kernel community relies on to mitigate concerns that arise from parallel development and residual interdependencies of modularity. The <sup>fi</sup>ndings unpack how distinct algorithmic interactions occur in open source work and their signi<sup>fi</sup>cant role in managing tasks. We develop theory based on these <sup>fi</sup>ndings and articulate the implications of this study.

## Theoretical Foundations

Open source developers rely on algorithms to conduct most tasks because their work is online and distributed. Algorithms are the basis of all software programs. When initialized, an algorithm will interact with other algorithms and humans as they operate and complete tasks (Lazer 2015). We de<sup>fi</sup>ne algorithmic interactions a algorithms interfacing with other algorithms and users to produce a result or achieve a goal. The interaction of algorithms requires a user to start a process where one algorithm begins to source another one. Once the correct algorithm is found, there is a handshake between them so that one initializes the action of the other (Beer 2017, Neyland and Mollers¨ 2017). Humans draw on algorithms in different work settings to facilitate and extend their own abilities to complete tasks. Often such an extension is referred to as augmentation (Jussupow et al. 2021, Raisch and Krakowski 2021). Algorithmic augmentation is the harnessing of and increasing reliance on algorithms to extend human capacities through partially autonomous operation.

Algorithmic Interactions in Open Source. Open source developers rely on multiple algorithms to perform minute coordination and decision-making tasks. Algorithms in open source can deal with speci<sup>fi</sup>c problems that arise through branching concerns associated with parallel development (Phillips et al. 2012) and residual interdependencies unresolved by modularity (Narduzzo and Rossi 2008). The long-term sustainability of open source communities depends on being able to attract good code contributions (Maruping et al. 2019), on techniques to manage a higher reliance on interdependent tasks (Howison and Crowston 2014), and on an infrastructure that establishes good governance (Minde et al. 2018). Open source relies on developers working simultaneously on the same or different modules of the codebase without interruption or breakdown. Algorithms are employed by developers to manage problems ignored by parallel development and modularity.

Parallel development makes it possible for multiple developers to write, upload, and change code simultaneously (Fitzgerald 2006, Narduzzo and Rossi 2008). In software development, a technology called version control software is used to manage parallel work, as it offers developers the ability to work on different branches (Phillips et al. 2012). Multiple developers interact with algorithms to work concurrently or sequentially on different branches, thus allowing parallel development to occur. Parallel development allows a project to grow quickly and with minimal interaction among developers. It also offers developers the possibility to select the tasks they want to contribute to. There is thus a good match of developer’s skills and values with the needs of the project. Parallel development involves paralle debugging, where multiple developers use, download, and scrutinize the code of other developers (Fitzgerald 2006). Bugs can usually be found and <sup>fi</sup>xed quickly. However, merging issues between branches can occur as a result of increased complexity or poorly written code (Phillips et al. 2011). Sometimes, as well, merging issues arise when new code patches contradict existing code. These issues only become apparent when algorithmic interactions break down and call on developers to remedy the problem.

Modularity corresponds to a “nearly decomposable system that preserves the possibility of cooperation by adopting a common interface” (Langlois and Garzarell 2008, p. 128). Breaking large complex tasks down into smaller, more manageable ones makes it possible for multiple developers to work on separate issues or the same issues simultaneously (Moon and Sproull 2000). Modularity offers the ability to leverage collective intelligence, supports reusability of ideas and code, minimizes random interactions, and supports the specialization of tasks (Langlois and Garzarelli 2008). However, modular systems can only aspire to complete decomposability because of residual interdependency (Narduzzo and Rossi 2008). Thus, modularity cannot resolve all issues in open source work. Modularity also requires that all elements be speci<sup>fi</sup>ed up front. Yet this is seldom possi ble in open source, given its emergent style of develop ment and parallel work. Also, as the system grows larger and more developers join the project, there is potential for “unorthodox modularity” (Narduzzo and Rossi 2008, p. 97, italics in original), as the core information hiding in modularity gets weakened through constant code tweaks by different developers. We argue that open source developers also rely on a deepening of algorithmic interactions to resolve issues of poor merges in parallel development and concerns with incomplete task decomposition in modular development. Developers introduce new algorithms to rebuild connections among parts of open source code, developers, and other algorithms.

Parallel development and modularity are crucial for open source work performed collectively across distributed settings because they make complex work manageable and uncertainty tolerant (Baldwin and Clark 2006). However, too much modularity can lead to common coupling, whereby “modules unnecessarily refer to variables and structures in other modules” (Fitzgerald 2004, p. 93), and design rules of any software product can become in<sup>fl</sup>exible and too entrenched to change (Baldwin and Clark 2006). Also, although modularity allows for a system to be tolerant to uncertainty and change within modules, it does not extend this <sup>fl</sup>exibility to the rules that guide across module behavior (Baldwin and Clark 2006, Gavras and Kostakis 2021). Interactions between modules require sustained work and effort. In open source, interactions between modules are worked on through custom-made algorithms.

Algorithmic Interactions Augmenting and Automating Open Source. Algorithms interacting with other algorithms extend the reach of other algorithms and of humans within the system (MacKenzie 2018, Miklos-´ Thal and Tucker 2019). The way algorithms operate often necessitates that one algorithm transfer the same or a related task to another algorithm in a handoff. Algorithms rely on each other to perform tasks. Algorithms also facilitate open source work as they manage interdependencies between tasks (Howison and Crowston 2014). Most open source development work is carried out online. The coordination of tasks relies on developers who, in turn, delegate to algorithms. For instance, most tasks related to merging of code changes are carried out by different algorithms working together. Tasks such as initializing a merge, <sup>fl</sup>agging a duplicate code change for the same bug, and offering a developer choice between code change options provide examples of work carried out by algorithms in open source. Yet algorithms, in turn, can also give rise to unpredictable results. Most scholarship on algorithms has focused on how they augment the work of humans (Jussupow et al. 2021). Augmentation refers to the idea that algorithms extend and amplify the capacity of the user (Engelbart 1962, Skagestad 1993). In open source, developers and users interact with algorithms (Kallinikos and Tempini 2014) so that algorithms can enhance their ability to work. Yet algorithms do not necessarily augment work (Burton et al. 2020). Likewise, algorithms may not always automate work (Hui 2015). Algorithms work with other algorithms autonomously (Lenglet and Mol 2016, Raj and Seamans 2019) and create a more resilient mesh of algorithms invoking one another simultaneously (Schildt 2017), yet there is nearly always a need for human involvement (Bainbridge 1983, Ekbia and Nardi 2017). The autonomous operation of multiple algorithms in open source enables us to interrogate algorithmic interactions while noting the nature of human involvement that arises.

We can understand that “automation implies that machines take over a human task, [while] augmentation means that humans collaborate closely with machines to perform a task” (Raisch and Krakowski 2021, p. 193). However, such a perspective and others like it deepen the divide and reestablish the human-versus-technology problem (Brynjolfsson and McAfee 2011). The implicit claim in management scholarship is that automation, although useful, will reduce interactions that involve humans. There is thus a need to bring the human back in the workplace and augment human work with technology by keeping the “human in the loop” (Grønsund and Aanestad 2020). When the - human does not understand the algorithm, then the algorithm is changed to make it more effective and transparent. At the same time, the human adapts to the algorithm and learns new skills (or is forced to reskill). However, the inclusion of algorithms can increase short-term ef<sup>fi</sup>ciency through both automation and augmentation, yet in the long term, there is less diversity in organizational routines because of the greater standardization of work (Balasubramanian et al. 2022) and a reliance on formal authority embedded into algorithmic design (Lindebaum et al. 2020). This decreases the capacity of organizational learning in the long term (Balasubramanian et al. 2022). Our study points toward how, in open source development, humans as well as algorithms play a mutually crucial role. We <sup>fi</sup>nd that the perspective on augmentation in open source needs to be broadened to include not only how developers are augmented by algorithms but also how algorithms are augmented by developers. Such ideas have been hinted at in prior scholarship (Purao et al. 2003, Ebben 2020), but few if any studies have offered empirical evidence of how this unfolds.

Technologies, and algorithms more speci<sup>fi</sup>cally, are employed to enhance human work (Ekbia and Nardi 2018). It is the developers’ efforts that are augmented, and algorithms are a tool toward that goal. Some schol ars argue that the “system is not ever actually autonomous, but always requires human mediation” (Ekbia et al. 2015a, p. 6). However, such work focuses largely on the invisibility of human effort in the process of automation (Ekbia et al. 2015b) and on how value is being extracted from humans without acknowledgement or recognition of human effort and interaction (DeCanio 2016). Seminal work on automation makes a similar observation about the role of the human operators of technology where the technology is considered largely autonomous (Bainbridge 1983). This is an irony of automation where the operators of technology must interact closely with autonomous technology to understand any failure. Only close and continued interactions between both make the job of maintenance straightforward (Bainbridge 1983, Hancke 2020). Although this scholarship acknowledges and appreciates the continued need for humans to work with autonomous technology, it also echoes how such human involvement is menial work.

Raisch and Krakowski (2021) explain how automation and augmentation exist in an interdependent relationship. If human creative work is augmented with algorithms, then they argue that, over time, parts of the job, as both humans and algorithms interact and learn to work together, will become easier to automate. Such a managerial perspective, although important, does not explain developers and algorithms working together in open community forms of work. Open source develop ers, unlike managers, are both the designers and users of algorithms. In open source, developers and algorithms interact with each other, and through interactions, developers gain a more meaningful understanding of the limits and strengths of algorithms interacting. Increasing automation for one task, such as merge decisions in open source, also affects other tasks. This raises the skill level needed to perform the same task. We argue that, in open source, the interactions among algorithms and with developers reveal how concerns are improved in practice and enable us to understand the relationship between augmentation and automation.

## Research Methods

We draw on the Linux Kernel development community. We focus our attention on speci<sup>fi</sup>c algorithms of version control systems. Version control helps developers track and record changes to source code over time and ensures that code is not overwritten arbitrarily. Our case examines algorithms in use by two version control software, BitKeeper (BK) and Git. Linux developers discussed the adoption of BK for a period of at least six years (1999–2005). Git has been adopted since 2005 and is still currently used. The 1999–2005 period was relevant in Linux history because of the questioning and controversy of BK adoption and what it revealed about the reliance on algorithmic functionality. Our analysis of Git adoption since 2005 enriches our data beyond one version control software and develops our theoretical understanding of algorithmic interactions. Open source developers are known for their eagerness to learn and understand the algorithms that they build and work with (Ghosh 1998, Roberts et al. 2006). Their discussions of algorithms thus differ from the typical user perspective that is often considered when algorithms in work settings are studied (Mohler et al. 2015).

## Data Collection

We drew on the Linux Kernel Mailing List (LKML), which is a publicly accessible archive of developer messages. We chose the LKML because it provides direct access to communications among community members. Prior studies have established the use of email archives for their data (see O’Mahony and Ferraro (2007) and Shaikh and Vaast (2016)). Taking all the threads and messages discussing BitKeeper and Git from June 1995 to early 2018, we engaged in theoretical sampling (Glaser and Strauss 1967) (see Table 1). The process of email collection involved taking each email, reading it, drawing initial analytical interpretations, and then using the emergent ideas to collect more data in a focused manner. We manually copied and pasted all messages into a text document for analysis and worked with the content analysis software ATLAS.ti. The discussion of BitKeeper was both long and detailed. It lasted between 1995 and 2005. Git (2005 onward), by comparison, saw fewer email threads dedicated to it. This was partly because BK was a proprietary tool and thus forced the Linux community to consider the rami<sup>fi</sup>cations of adopt ing a closed source tool for a high-pro<sup>fi</sup>le open source project such as the Linux Kernel, but also because Git was an open source software initiated by the leader of Linux, Linus Torvalds. To better grasp issues associated with Git, we turned to the discussion forum on GitHub, LKML, and other sources.<sup>1</sup> We selected forums where the developers of Git or core Linux users of Git were participants to understand algorithmic interactions as seen through the discussions of the experts who built the algorithms.

We repeatedly adapted the search keywords we relied on as the story unfolded. The fact that the Linux community questioned the use of BK was helpful to this study because different BK algorithms and their respective merits were discussed. We followed developers’ discussions and focused on two algorithms in BK: TimeSync and auto-merge. The reactions to both algorithms in the Linux community have been extreme. Whereas TimeSync was hailed as a step forward in open source development work, auto-merge was seen as an aggression on developers’ decision-making authority. In 2005, the Linux community moved away from BK use. BK was no longer available to the Linux community. Instead, the Linux community focused on building its own version control software, Git. To deepen our theoretical development and understanding of algorithmic interactions, we studied algorithms at work in Git. This was primarily because the experts building Linux were also the same developers using and developing Git. Their insight into Git offered us an opportunity to follow algorithmic interactions and use. Tracing conversations through the LKML as well as related Github forums, we focused on discussions of Git hooks. After we had collected and analyzed most messages related to these three algorithms (TimeSync, auto-merge, and Git hooks), we found that certain questions were left unanswered and required a more direct approach of investigation. The <sup>fi</sup>eld researcher then carried out seven in-depth interviews with key developers, designers, and users of BK and Git. The questions dealt with how and why certain algorithms had been designed, what purpose they served, and how effectively each algorithm automated work. When an algorithm broke down, we also examined whether this was due to a poor interaction and how developers resolved the issue(s).

Table 1. Data Collection

<table><tr><td>Data source</td><td>Use in analysis</td></tr><tr><td colspan="2">Publicly accessible email archives</td></tr><tr><td>Emails sent to the LKML (http://lkml.iu.edu/hypermail/linux/kernel/) from 1995 to 2005 for BitKeeper. Approximately 410 email messages related to BK&#x27;s algorithms were collected, read, and analysed.</td><td rowspan="2">Provided details of specific algorithms, how they work in practice, and the problems they raisedMade visible different algorithms offered by BK and GitProvided compelling examples of direct developer interactions with different algorithms, as well as algorithm to algorithm</td></tr><tr><td>Emails discussing Git on the LKML (https://git-scm.com/community) from 2005 to early 2018. Seventy-six messages on Git hooks were collected, read, and analysed.</td></tr><tr><td colspan="2">Interviews with key informants</td></tr><tr><td>Specific interviews via Skype and email of key informants who designed BK and used it. Seven in-depth interviews were conducted.</td><td>Provided answers to questions about specific algorithms of BK used over the yearsProvided details on how and why the algorithms were constructedGave opportunity to triangulate and confirm (or otherwise) our theoretical constructs</td></tr></table>

## Data Analysis

Table 2 summarizes our data analysis process. In the <sup>fi</sup>rst stage, we approached our data about particular algorithms with open codes (Krippendorff 1980, Neuendorf 2002, Wiesche et al. 2017). These codes were drawn from our theoretical foundation but also from our initial reading of emails (Orton 1997, Walker and

Myrick 2006), as is consistent with Strauss and Corbin’s (1998) guidelines for qualitative analysis. Our open codes such as algorithmic interaction, modularity, parallel development, branching, breakdowns, and automation led us to choose speci<sup>fi</sup>c algorithms. Linux Kernel discussions on the LKML devoted a large part of community time to discourse about various algorithms. We followed some of these discussions in greater detail. The <sup>fi</sup>rst author built a small list of potential algorithms that could be integrated in the study and discussed the value of each with the coauthor. We then returned to the data to seek more insights.

The aim of the second stage was to narrow down our analyses on a smaller set of algorithms by examining the relationships among codes. The chosen algorithms included BitKeeper’s TimeSync and auto-merge. We also chose Git hooks used by integration software. This theoretical sampling (Charmaz 2006) came about because these algorithms were relevant not only for thei technical strength but also for how they affected open source work. These algorithms that developers used frequently performed crucial tasks. We collected all email messages regarding these three algorithms and the associated interview transcripts and began to look for interactions among algorithms.

Table 2. Data Analysis

<table><tr><td>Stage</td><td>Tasks</td><td>Outputs</td></tr><tr><td>1. Open coding</td><td>Developed early open codes for the theoretical scaffold, drawing on theoretical foundationsRevealed examples of codes from literature, but we also found data-driven codes.Searched for distinct algorithms used by Linux developers to work in distributed settings</td><td>An iterative grounded understanding of three key constructsEarly code book size of open codes: 57List of different, interesting algorithms used by Linux</td></tr><tr><td>2. Focus on three algorithms</td><td>Used code book to analyze the entire data setReduced the code book by eliminating duplicates and similar codesNarrowed down analysis on three algorithms where the choice of algorithms was based on interest in LKML discussion and their functionality in distributed work</td><td>Code book reduced to 36 open codesInitial theoretical memos emerged related to different types of interactionObservations of TimeSync, auto-merge, and Git hook algorithms</td></tr><tr><td>3. Identify distinct interaction types</td><td>Searched for distinct interaction types between algorithmsSearched for when algorithms interacted only with other algorithmsBuilt relationships between distinct interaction types through grouping codes, writing memos, and refining theoretical ideasWrote yet more detailed memos to explain the relationships between interaction typesDocumented three different processes across the algorithms used by version control software</td><td>Eleven theoretical memos related to different interactions builtInteraction types coalesced into three processes: managing parallel development, organizing modularity challenges, and supervising of open source work by algorithmsGrouping of interactional activity to document key dimensions of task, design of algorithm, and interactional context</td></tr><tr><td>4. Key dimensions of three processes focused on modularity and parallel development</td><td>Refined key dimensions that led to automationElaborated and defined theoretical construct of the three processes and their relationship</td><td>Identification of breaks in automation and shift to processesCreation of Figures 1 and 2Theoretical constructs established and theoretical development built</td></tr></table>

The <sup>fi</sup>rst author developed notes that mapped out the journey of these algorithms, which other algorithms interacted with them, as well as whether developers commented on them and made changes to them. These notes, <sup>fl</sup>eshed out over time in detail and depth, became theoretical memos. As we delved deeper into our data set, our code book became more nuanced. We added different categories and characteristics. We also noticed that the code book had duplicate codes, which we then tidied and reduced. We also began to make sense of relationships among codes. This was a natural progression in the analyses, because questioning the need for a speci<sup>fi</sup>c code entailed defending it through relational signi<sup>fi</sup>cance with other codes or memos. This brought insight into distinct interactions among algorithms.

In the third stage, we focused exclusively on interactions among algorithms. Different interaction types became apparent in our data (see Figure 1). We made notes of them in theoretical memos. These memos deepened our understanding of algorithmic interactions as a core category for theoretical development. We wrote new theoretical memos along with explanatory notes for segments of data that revealed different interactions. We noted that certain interactions worked together. We grouped interactions as they occurred in the data and wrote detailed memos for these groupings. Each grouping of interactions gave rise to a different process (Cloutier and Langley 2020). The memos distinguished three processes with different interactions working together.

Figure 1. Data Analysis  
![](/api/attachments/H6WG3WEF/fulltext/images/1302a301d5a6f3f8f842b3875d56d06e9c7be3229d0d391e3a829b10af5718b2.jpg)

In the fourth, and last, stage, we looked across the data to ensure that the processes of managing parallel development, organizing modularity challenges, and supervising open source work could be observed in distinct occasions and under different conditions. We also looked for situations where the processes did not occur together. Doing this allowed us to understand the boundary conditions of our theorizing and to strengthen our understanding of how the three processes were related. We found three key dimensions—task, design of algorithm, and interactional context—that helped us to understand the relationship between algorithmic interactions and issues created by poor modularity or inadequate conditions of parallel development and to develop further our theorizing.

## Findings: Algorithmic Interactions in Linux

In open source, algorithms removed unnecessary interruptions and expedited work. We examined three in<sup>fl</sup>uential algorithms (see the online appendix for details on how each algorithm operates) of version control software used by Linux Kernel developers. These algorithms included BitKeeper’s TimeSync algorithm, Bit-Keeper’s auto-merge, and Git’s integration hooks. Open source work tackled continuing problems with parallel development and the modularity of tasks and code. Linux developers built algorithms to address these two problems.

The <sup>fi</sup>rst of our three algorithms, the TimeSync algorithm of BK, “ensures that all <sup>fi</sup>les in a repository (or a collection of repositories) always obey the same timeline” (BitKeeper Documentation).<sup>2</sup> BK developers created the time-stamping algorithm (the term developers used for TimeSync) to enable parallel work in distributed settings, where time zones and multiple developers working together made it imperative to give each code contribution a unique stamp or identi<sup>fi</sup>er.

The second algorithm was BitKeeper’s auto-merge algorithm, which facilitates code merging to manage parallel tasks in open source:

Our auto-merge virtually eliminates false positives and the wasted time associated with unwinding a bad merge … . BK auto-merged 89% of the time with zero mistakes. (BitKeeper Documentation)

The need to merge code arose from multiple developers who submitted their work at the same time. This functionality ensured that codes from different developers were not overwritten accidentally.

The third algorithm was Git’s continuous integration hooks algorithm(s) (Git hooks).<sup>3</sup> Developers rely on Git hooks to make code integration ef<sup>fi</sup>cient. Git hooks manage parallel distributed work at the developer end (client side), locally, or at the server end, where Linux code is held for all developers. Hooks are algorithmic scripts programmed to act when a developer makes a patch commit (client side). These algorithms automate real-time testing of new code, which can then be integrated ef<sup>fi</sup>ciently:

“git send-email” learned to run sendemail-validate hook to inspect and reject a message before sending it out … . [T]he default die() routine had a code to prevent it from getting called multiple times, which interacted badly when a threaded program used it (one downside is that the real error may be hidden and instead the only error message given to the user may end up being “die recursion detected”, which is not very useful).<sup>4</sup>

Our <sup>fi</sup>ndings follow these three algorithms as they interacted with other algorithms and developers. Interactions were often between two or more algorithms. The <sup>fi</sup>ndings reveal algorithmic interactions that facilitated or resolved problems related to work in open source (see Table 3 for illustrative data).

## Managing Parallel Development with Algorithmic Interactions

Developers needed to automate the coordination of their work. Working in parallel with multiple developers required a combination of algorithmic interactions that included automated categorizing, calibrating, and invoking interactions. We also found that a distinct type of interaction, which we named a “defective” interaction, triggered a push toward developer-toalgorithm interactions.

Developers created code locally and then uploaded it to the main build via version control software that was held on a server that the community had access to. Such work was performed by initiating a merge algorithm. For a patch to be merged, it <sup>fi</sup>rst had to be categorized and given a unique time stamp so that all incoming patches could be distinguished from one another. This was core to parallel development. However, interactions among different actors were not predictable, and unexpected behavior arose that needed algorithmic and/or developer support.

Categorizing Interactions. Developers used the Time-Sync algorithm to reorganize and line up different bits of code into an order that worked across time and space. Developers depended on automating this part of their work because, in software development that spanned different time zones, time was not singular. BK’s TimeSync algorithm had been designed to automate this part of development work. Much open source work relied on automating different tasks. Developers needed to rely on algorithms to interact with other algorithms and accomplish tasks with little to no human involvement because there was less likelihood of mistakes being made, and work could be carried out at all hours:

Table 3. Illustrative Data with Analysis

<table><tr><td>Type of interaction(s)</td><td>Data</td><td>Analysis</td></tr><tr><td>Defective interactions; extending interactions</td><td>&quot;Run the test case under the debugger *while* reading the source code (best if I can use a remote debugger that interacts with my source code browser) and use the debugger to validate my assumptions by answering those questions* the loop is repeated until I have an &quot;aha&quot; moment, which is the point at which I *think* I see what the code is doing that it shouldn&#x27;t have done.&quot; (Source: http://lkml.iu.edu/hypermail/ linux/kernel/0009.2/0308.html)</td><td>The focus is on the process of debugging code. The developer to debugger algorithm interaction needs to be replaced by an algorithm-to-algorithm one—where a remote debugger is automatically triggered to interact with the source code. Such debugging needs to continue in a &quot;loop&quot; until the problem is surfaced and resolved.</td></tr><tr><td>Invoking interactions; defective interactions; forceful interactions</td><td>&quot;[A]uto&#x27; forces the use of kerneld at boot time. Without it, it seems that when the initlevel changes to 2, 3, 4 or 5, the kerneld is invoked.&quot; (Source: http://lkml.iu.edu/hypermail/ linux/kernel/0103.0/0356.html)</td><td>Kerneld is the user space daemon that the kernel invokes so that automatic loading of different drivers can occur. This developer is suggesting that automating the initialization of kerneld is not happening unless certain conditions are met so the algorithm-to-algorithm interaction is not rendering the correct response.</td></tr><tr><td>Extending interactions</td><td>&quot;CXL devices contain an array of capabilities that describe the interactions software can interact with the device, or firmware running on the device.... A CXL compliant memory device must implement the memory device capability. Each of the capabilities can [will] provide an offset within the MMIO region for interacting with the CXL device.&quot; (Source: http://lkml.iu.edu/hypermail/ linux/kernel/2011.1/04207.html; brackets in original)</td><td>Compute express link (CXL) is an open standard that allows interactions between the CPU and other algorithms/software. In this thread the focus is on how CXL has numerous capabilities that can be operationalized when other algorithms interact with the memory mapping input/output (MMIO) region.</td></tr><tr><td>Defective interactions</td><td>&quot;I&#x27;m playing with CONFIG_NO_HZ_FULL. I&#x27;m getting a strange result where some CPUs are able to turn off local timer interrupts and others aren&#x27;t. Is there a known interaction between kvm-based VMs and CONFIG_NO_HZ_FULL?... Is kvm doing something &#x27;odd&#x27; to mess it up?&quot; (Source: http://lkml.iu.edu/hypermail/ linux/kernel/1503.2/04673.html)</td><td>The focus is on ensuring that high-speed real-time operations continue to operate without stalling any CPU. If one CPU is stalled, it can create a ripple effect to stall all others in operation. The defective interaction between kvm based VMs and CONFIG_NO_HZ_FULL has created an unpredictable result where some CPUs can turn off local timer interrupts.</td></tr><tr><td>Defective interactions; simulating interactions</td><td>&quot;[W]hen an IOMMU is set, the /dev/vfio/ vfio container becomes a conduit for file ops from the container to be forwarded to the IOMMU.... [T]he user doesn&#x27;t have another object to interact with the IOMMU. It&#x27;s entirely possible that with an ioasid shim, the user would continue to interact directly with the /dev/ioasid fd for IOMMU manipulation.&quot; (Source: http://lkml.iu.edu/hypermail/ linux/kernel/2104.2/06917.html)</td><td>The /dev/vfio/vfio container is initialized when the input/output memory management unit (IOMMU) interacts with it. The interaction converts the /dev/vfio/vfio into a pathway. There is unpredictability introduced because with ioasid, it is not sure if users can continue to interact directly and employ IOMMU effectively.</td></tr></table>

The pull command is used to update your repository as painlessly as possible. The default behavior is to pull changes from your parent repository and apply them with the minimal amount of human interaction.

If there are no over lapping changes (on a per line basis, not a per file basis), then the changes are applied automatically. This may not always produce the semantically correct result.<sup>5</sup>

Developers worked locally on their own computers, so there was always a local time stamp for each code push/pull. However, when a local change was pushed into the main Linux Kernel build, it was given an “atemporal” time stamp. TimeSync stamped the changed patch with a universal stamp. This universality was created by BK and its algorithms and not a Linux developer using BK. Time-stamping was consequential for all code that was created afterward and for developers desirous to see their code contributions become accepted patches. However, as McVoy points out above, the result was not always correct. Interactions between algorithms were supposed to operate as designed, yet in practice, these developers found that the context affected results. The interactional context was important because it led the same algorithm to interact with others with different results. The difference in interactions arose from the purpose and function of an algorithm along with the interactional context (e.g., operating system, number of software programs running, type of programs running, as well as the purpose and function of the second algorithm). Each algorithm interacted differently with other algorithms and humans. Linux developers automated their work, yet as an interaction unfolded, the result could—and often did—necessitate a developer coming to the rescue of the algorithm that had stalled, as Torvalds himself noted:

[M]y suggestion to have a “bk backmerge” does not remove the temporal relationships. All changesets already have a timestamp (they clearly have to have it, just so that you can see when they happened and say “what did this tree look like one month ago?”). So we already \_have\_ the temporal information, and encod ing that temporal information into the “relationship” information actually ends up costing you quite dearly. I’d say that most (maybe all) of the complaints about not being able to apply changesets in any random order comes exactly from the fact that developers \_know\_ that temporal relationships are often not relevant.<sup>6</sup>

Developers demanded reliability with time stamps for patches because any mistake in this step involved algorithms freezing midway through an operation, leading to more than one patch having the same time stamp. Torvalds explained that developers were sometimes keen to reorder changesets (batches of code <sup>fi</sup>xes and additions) manually. Algorithms automated work, but on occasion, developers preferred to carry out themselves part of what was otherwise usually an algorithmic task. In the previous quote, Torvalds giving recognition to developer engagement with tasks that could be automated demonstrates the importance of human involvement in open source work.

BK allowed a developer to scale backward or forward in time with builds. In Linux, an algorithm that provided accurate and unique time stamps for each patch was crucial to the development process. This ensured the reordering of patches so that each patch could be merged into the main build in a precise order. We call such reordering of patches in parallel development calibrating interactions, because it involved the TimeSync algorithm to <sup>fi</sup>rst categorize and then calibrate each patch of code. Calibrating interactions, such as categorizing interactions, must be automated because the risk of a nonunique time stamp on any patch makes tracing any problem in millions of lines of software impossible:

One important thing to consider is that time can go forward or backward. … Time semantics. A distributed system cannot depend on reported time being correct. It can go forward or backward at any rate.

There is no universal “before” and “after”, even within one repository; there might be changes that can't be ordered … and might have happened in any order for the same result.<sup>8</sup>

Calibrating Interactions. TimeSync recalibrated and reorganized submitted patches. No matter which chronological order they were submitted in, TimeSync bound them into a new universal order. This was necessary to organize open source work:

Our TimeSync<sup>TM</sup> feature ensures that all files in a repo sitory (or a collection of repositories) always obey the same timeline. This guarantees total reproducibility and prevents broken builds or indeterminate states. …

All the <sup>fi</sup>les and components are always consistent. If one is rolled back to how it looked 3 weeks ago, all the others are rolled back as well. This eliminates broken builds due to out-of-sync libraries and con<sup>fi</sup>gurations. (BitKeeper Documentation)

TimeSync calibrated different patches into a new order. This enabled multiple developers to work in parallel and not worry about the order of patches. Stamping patches with TimeSync’s own interpretation of time and recalibrating the work created a new merging arrangement:

With TimeSync … we started updating system time continuously through the whole lifetime of Hyper-V guests. Every 5 seconds there is a time sample from the host which triggers do\_settimeofday. While the time from the host is very accurate such adjustments may cause issues:

Time is jumping forward and backward, some applications may misbehave.<sup>9</sup>

At the same time, the auto-merge algorithm in BK sought out any changes made in any branch by different developers and then automatically merged them into a clean build. Syncing code from other sources forced the auto-merge algorithm to interact with multiple algorithms. Auto-merge was designed to automate merging and eliminate the human developer from decision making. McVoy had designed auto-merge to reduce human errors and subjectivity in decisions about patch preference:

Syncing from the main kernel, synching from someone else, syncing with a coworker, whatever. It doesn’t really matter. With the limitation that BK wants you to eat everything that the other guy has that you don’t, it all just works. And you can sync from N different places all of which happened to have the same patch in the same changeset, and it gets applied once, BK knows it has it already. … [W]ith BK, it’s a lot nicer, most stuff just automerges, and the stuff that doesn’t only needs to be merged once.<sup>10</sup>

As the number of contributors grew, the auto-merge algorithm took longer to perform its work, as there were more changes hidden in different branches. Linux developers looked to alternative areas that could be automated to improve ef<sup>fi</sup>ciency. Integration hook algorithms constituted one way of precipitating testing. The auto-merge algorithm interacted with the integration hook algorithm and invoked it to action once a merge was successful.

Invoking Interactions. Integration hooks, once set in motion, worked with little developer interaction. Continuous work by algorithms initialized the testing of patches while they were being merged. This reduced the need for large-scale testing and localized any issue caused by a new patch. Linux development relied on multiple algorithms invoking and interacting with other algorithms for ef<sup>fi</sup>ciency, speed, and accuracy to manage parallel development. Hooks also had prehooks (i.e., another set of algorithms) that were automatically initialized by other algorithms. When integration and prehooks ran smoothly, they became invaluable tools for open source work. Prehooks were invoked by other algorithms but could at times lead to a defective interaction. This happened as some “loops” could be created where an “invalid nested call” set in motion more algorithm to algorithm interactions that had no end condition. Such automation defects stalled development and forced developers to remain involved and vigilant during the process. Developers could not automate all tasks. However, even certain simple tasks that lent themselves to automation were usually carried out with at least some developer intervention. Complete automation was not feasible. Often a developer returned to a faulty interaction to <sup>fi</sup>x the problem. This was evident from email conversations on the LKML about such issues:

[B]ridge netfilter code registers operations that are invoked any time nh\_hook is called … .

Packet wise, the bridge net<sup>fi</sup>lter hook runs <sup>fi</sup>rst … . Its <sup>fi</sup>nish function, br\_nf\_pre\_routing\_<sup>fi</sup>nish, then resets in\_prerouting <sup>fl</sup>ag to 0 and the packet continues up the stack. The packet eventually makes it to the VRF [virtual routing and forwarding] driver and it invokes nf\_hook .in case any rules have been added against the vrf device.

Because of the registered operations the call to nf\_hook causes ip\_sabotage\_in to be invoked. That function sees the nf\_bridge on the skb and that in\_prerouting is not set. Thinking it is an invalid nested call it steals (drops) the packet.

Update ip\_sabotage\_in to recognize that the bridge … can be enslaved to a VRF (L3 master device) and allow the packet to go through the nf\_hook a second time.<sup>11</sup>

Defective Interactions. Developers that made patch commits were freed from carrying out initial tests on their code and could instead simply invoke a commit command and let the commit algorithm call upon a precommit hook to test their code:

“git p4” didn’t interact with the internal of .git directory correctly … .

“git rebase” … was manually aborted without using “git rebase –abort”.<sup>12</sup>

However, hooks often malfunctioned. Defective automation interactions pushed the developer to reengage with the system and resolve the defective functioning of a prehook. Such moments were revealing of how developers were seldom detached from the work of algorithms. Automation with the help of algorithms was effective because developers were constantly present, vigilant, and working with algorithms:

Completion for “git checkout ” that auto-creates the branch out of a remote tracking branch can now be disabled, as this completion often gets in the way when completing to checkout an existing local branch that happens to share the same prefix with bunch of remote tracking branches.<sup>13</sup>

Developers attempted workarounds such as creating another hook to simulate the correct interaction and return algorithms to interface with one another again with little developer interaction. Automation breakdowns in open source increased the need for developer intervention in the short term. Developers sourced the problem and in doing so learned more about the interactional context that caused the defect. Often developers converted such learning, in the medium to long term, into better algorithms, which led to improved automation. Automation breakdowns played a crucial role in open source by pushing developers to reengage with algorithms and, in the long term, by improving automation.

Effective interactions between algorithms made the algorithms in operation invisible. This was important because numerous algorithms interacted with other algorithms to automate open source work. Automerging was a controversial algorithm because it obliged automation in an area where developers felt that their own intervention would be better suited. According to developers, merging tasks required human decision making rather than algorithms taking over because algorithms working to predesigned instructions were less likely to recognize out of the ordinary creative code:

There is a point to be made though that if \*Linus\* has to do a complicated merge, the “patch” that caused the merge should probably be suspect in the first place … . I've had some strange things happen on a BK automerge in the past, and I don’t trust any automated system that doesn’t understand the code to not make some subtle semantic mistake. (Mind you, when strange things happened, the code usually worked, and I didn’t notice until I tried to \*manually\* prepare a “patch” to send upstream).<sup>14</sup>

Defective algorithmic interactions played an important role. At a basic level they were an annoyance for developers. Yet our study revealed that when algorithms operated as planned, they were not questioned, and importantly, they were not improved upon. When a defective interaction occurred, developers were forced to step in, and developer-to-algorithm interactions increased, at least temporarily. Developers then created new and different algorithms either as workarounds or as more straightforward ways to resolve the problem. Maintaining smooth operations for parallel development required developers to step in continually to diagnose concerns with algorithmic interactions. However, parallel development breakdowns were not the only concern; modularity was also not perfectly achieved. This leads us to the process of organizing modularity challenges with algorithmic interactions.

## Organizing Modularity Challenges with Algorithmic Interactions

This process was triggered by deactivating, seeking, simulating, and reversing interactions. A combination of these interactions created situations where developers maneuvered workarounds to bypass possible breakdowns. Developers wanted to strengthen algorithm-to-algorithm interactions. However, when such interactions went awry, developers noticed problems with aspects of modularity of both task and system. Modularity and task decomposition ensured that objects could hide their implementation information and only the interface between objects needed to be manipulated. Yet when an interaction did not occur, developers were compelled to resolve the problem.

There was a pattern emerging: developers wanted to automate numerous and often cumbersome tasks associated with working in a distributed environment, but algorithms often behaved unpredictably and could not resolve complex problems. Full automation of any task seemed unlikely. Modularity problems were often more complex than parallel development ones. This obliged developers to consider how much they needed to be involved and for which tasks.

Deactivating Interactions. When an interaction between algorithms failed and did so repeatedly, it had to be deactivated. Developers did so by introducing a break and forcing a redirect of one or more algorithm(s). If the interfaces between objects had behaved as designed, then such interaction breakdowns would not have occurred. Modularity was something that developers had to work on continually to achieve and correct. An example of this is the Git send-email algo rithm that was created to interact directly with sendmail-validate hook algorithm. Sendmail-validate hook was tasked with inspecting messages so that it could decide whether to reject or send them out to their destination. If the sendmail-validate hook did not operate as designed, it caused a bad interaction between algorithms. This was an automation failure. Developers stepped in and interacted with the algorithm to redirect or disable it:

A test allowed both “git push” and “git receive-pack” on the other end write their traces into the same file. This is OK on platforms that allows atomically appending to a file opened with O\_APPEND, but on other platforms led to a mangled output, causing intermittent test failures. This has been fixed by disabling traces from “receive-pack” in the test.<sup>15</sup>

In certain cases, developers also built a new algorithmic hook to “disable traces” of bad algorithmic interactions. Developers remedied poor interfacing between objects so that the new hook could invoke fresh, correct interactions. This was one way to regain modularity.

Seeking Interactions. When a merge was invoked, Git sought every possible pathway of the branch of code so that the merge could capture all changes. This process also involved seeking out renamed branches and code because Git retained a complete history of the main build. Often Git attempted to locate lost code because the pathway to the code had been renamed. This meant that Git needed to recreate history and reconnect path ways. Task decomposition was embedded into each object so that any object only performed a small but complete action. The usual approach would be that an algorithm would seek out a pathway by name. Yet if the name of the pathway had been relabeled and modi<sup>fi</sup>ed, the seeking algorithm could not make a match and complete its task. Task decomposition was rendered ineffective. This provided another example of lingering modularity problems:

When “git merge” detects a path that is renamed in one history while the other history deleted (or modified) it, it now reports both paths to help the user understand what is going on in the two histories being merged.<sup>16</sup>

The git merge algorithm invoked multiple algorithms to seek different branches and merge their histories. Certain branches got deleted, but some traces were left of them—residual interdependencies. A developer then examined histories and pathways to decide whether they needed to be merged. The developer’s decision set conditions and built a precedent that the git merge algorithm learned. The next time it faced the same issue, the algorithm invoked its own decision and interaction possibilities. Automation through learned algorithmic behavior was visible.

Automerging, Git hooks, and time-stamping were related algorithms that frequently interacted with one another. The merge had to be correct so that histories of each branch could be rolled forward or backward in time accurately. Achieving system modularity was not straightforward. Being able to foresee all future possibilities in code changes, versions, and branches was impossible. Algorithmic interactions were more complex than a simple matching of names or labels listed by the developers’ command. When developers used different command options, the algorithms learned to conduct more sophisticated tasks. Sometimes, this involved creating or even redressing simulated algorithmic interactions.

Simulating Interactions. Algorithms faked interactions when needed. These simulated interactions were useful, but they, in turn, could create problems when triggered accidentally:

regmap API [application programming interface] … used readl() and writel() to interact with the hardware, meaning that all writes are converted to little endian when writing to the hardware. This caused a bad interaction with the regmap core in big endian mode since it was not aware of the byte swapping and so ended up performing little endian writes.

In this discussion about the sequence of computer memory storage (“little endian” and “big endian”), a developer described how when the default in a program was set to little endian, it created a problem because the algorithm simulated interaction with the opposite sequence (big endian). The algorithm was working to its default setting. However, as the default was the opposite of what was needed, it created a bad interaction among algorithms. A developer had to remedy this problem manually. This, again, broke the <sup>fl</sup>ow of automated interactions between algorithms.

Another reason for simulated interactions was when a precommit hook was pulled along accidentally with the code that a developer wanted to change. The developer was unaware that other developers had embedded their precommit hooks into the code they had written:

This would provide a reliable way to force pre-commit to use an internal registry to install a given hook … .

The main issue is that people will often do a git pull (pulling in a hook bump somebody else did), make some changes of their own locally, then run git commit which invokes pre-commit to install the updated hooks.

There’s no easy way to make sure this git commit command runs...like it needs to in order to succeed, leading to some confusing behavior.<sup>18</sup>

Problems arose when numerous prehooks began to build up in a branch while developers, unaware of this, continued to make changes to the branch. One of the problems was opposing prehooks written by different developers. The consequences of prehooks often only became apparent after the merge was completed, but by then it was too late. If a developer attempted to push his or her changes back into the build, the precommit hook(s) reacted badly with server-side hooks. The interfaces, clearly, did not work well, so modularity issues arose. Developers needed to <sup>fi</sup>x this problem at an earlier stage or reverse the issues caused by mul tiple precommit hooks working against one another.

Reversing Interactions. Developers, as a last resort, either used workarounds or employed more drastic purging of their precommit caches. This was necessary when traces left in memory erroneously drew interfaces between two objects toward each other. Another algorithm was then invoked to create a solution:

Unfortunately when this issue was noticed it was addressed by updating the DT [device tree] for the affected devices to specify them as little endian. This happened to work since it resulted in two endianness swaps which cancelled each other out and gave little endian behaviour but meant that the DT was clearly not accurately describing the hardware.<sup>19</sup>

The correction did not overwrite the last command but instead created a counter-command that reversed the strength of multiple precommit hooks, thus nullifying their effect. A new trace was built so that interfacing continued ef<sup>fi</sup>ciently and algorithm-to-algorithm interactions could return to an automated process. Developers worked at automating algorithms and spent time maintaining the system to keep algorithmic interactions running. This was necessary because in large systems built over a long period of time by multiple developers, modularity through algorithmic interactions alone was not enough to facilitate open source work.

## Supervising of Open Source Work by Algorithmic Interactions

The third process revealed a deepening of algorithm–toalgorithm interactions where increased automation was established. Certain algorithmic interactions became stable and autonomous enough to supervise open source work. Algorithms assembled multiple interactions with other algorithms: forceful interactions that found new ways to resolve the issue at hand with limited developer intervention, extending interactions that broadened as well as deepened the network of algorithmic interactions, and reconnecting interactions that offered the ability to mobilize multiple algorithms simultaneously.

Forcing Interactions. Developers considered algorithmic in<sup>fl</sup>uence to be productive in open source work. However, at times, developers viewed increased algorithm-to-algorithm interactions as a personal loss of control. The auto-merge algorithm, for instance, gave a degree of control to version control software by removing developers from important decision making. This frustrated some developers enough for them to demand that their tools and algorithms do what they wanted them to do rather than the other way around:

But it can’t cope with the drop-in style, and at this point I can’t be coerced into a new mode of development. If BK could sanely handle drop-in trees (the right way), trust me, I'd already be using it. But I'm still forced to do the merging work by hand, if I insist on maintaining the drop-in tree (without CVS), even if using a BK clone as my source base.

My tool needs to do what I tell it to, not the other way around.<sup>20</sup>

Developers objected to the idea that important decisions such as merging could be delegated to an algorithm. BK algorithms had the capacity to enhance open source development work. However, BK algorithms compelled developers to adapt their work practices to BK. BK had been designed and built to improve the ability of Linux to work in parallel as well as improve the interfacing of objects and task decomposition (modularity). However, the approach taken was to rely further on algorithm–to-algorithm interactions. Relying on algorithms to augment a developer’s job was acceptable and even encouraged. Yet developers were concerned by the full automation of merging. To them, only humans could recognize innovative patches of code because algorithmic design was limited. Certain tasks could be programmed into useful algorithms, but creative tasks were too ambiguous to be encoded.

Developers argued for algorithms to behave and execute when a developer initiated them rather than work autonomously. The developer community wanted algorithms to augment their work for particular tasks:

The person sending the patch should be the one responsible for resolving a complicated merge. If BK makes that easier, great. HOWEVER, I don’t really want Linus to be using some tool that does automerging. No SCM system and automerge tool is going to understand what the code \*means\*, unless it’s got a compiler integrated into it.<sup>21</sup>

Those in favor of algorithmic interactions enhancing their work argued that if a certain patch of code broke the execution of a merge, then rather than blame the algorithm, perhaps the problematic patch should be unpacked. These developers believed in forceful interactions of algorithms to deepen augmentation by extending algorithmic interactions working with and for developers:

I’ve had some strange things happen on a BK automerge in the past, and I don’t trust any automated system that doesn’t understand the code to not make some subtle semantic mistake. (Mind you, when strange things happened, the code usually worked, and I didn’t notice until I tried to \*manually\* prepare a “patch” to send upstream).<sup>22</sup>

Extending Interactions. Algorithmic interactions were extended in three ways: by creating intermediaries, by building multiplicity of syncing into algorithms, and by increasing autonomous execution decision by algorithms. Interactions among drivers, hardware, and other software modules needed to be intermediated by algorithmic Git hooks that interfaced with different parts:

Proper charging on n900 needs [to] interact with isp1704 driver. But this is specified for n900, not for all boards. bq2415x module should be general for all boards—so it should cover \*only\* bq2415x chip … and that [can] be done with hooks … No need for yet another driver. (Contreras 2011)<sup>23</sup>

Building an algorithmic intermediary ensured the automation of tasks and freed developers of the need to initialize each task separately, as illustrated in the creation of the .cvsignore algorithm for CVS:

Out of sheer frustration about kernel source interaction with CVS I have written a .cvsignore file so we can all use the kernel source with CVS again. Please put it in the next kernel tarball, it'll save a lot of people a lot of frustration.<sup>24</sup>

Another way to improve interfacing between objects through extending algorithmic reach was with the use of algorithms that synced work from different branches of a build simultaneously. The auto-merge algorithm of BK performed multiple syncs by seeking changes across the build, including all possible branches in one merge:

BitKeeper saves tremendous amounts of manual work by significantly increasing the reliability of auto-merge. BitKeeper is able to automatically handle the vast majority of even very hard merges. Even more importantly, our auto-merge virtually eliminates false positives and the wasted time associated with unwinding a bad merge … . Like all BitKeeper features, our automerge has as its’ imperative “First, do no harm.” This essentially eliminates bad merges and means that you can trust the auto-merges to be accurate … . BK automerged 89% of the time with zero mistakes. (BitKeeper Documentation)

Drawing on the basic laws of robotics (Asimov 1942), here the creator of BK’s auto-merge algorithm explained how the primary directive of auto-merge was to “do no harm.” Auto-merge interacted directly with other algorithms. This eliminated the need for developers to execute merges and extended their ability to work in parallel.

Another form of extending algorithmic reach was with the use of Git hooks. Algorithms’ autonomous decision making initialized the testing of patches as they were merged in real time. In some situations, a deepening of algorithm-to-algorithm interactions made it dif<sup>fi</sup>- cult for developers to understand the root cause of a problem. The reliance on algorithms that automated work was the reason for this lack of understanding because developers no longer needed to step in as often to resolve interactional breakdowns. They were thus less experienced about possible problems that could arise. Developers’ stunted learning paradoxically led to an increased dependence on developer intervention in the future. When an algorithm did not function as designed, it became harder for developers to make sense of the problem. The time needed to resolve the problem increased and thus reduced the ability to automate.

Reconnecting Interactions. Developers depended on algorithms to facilitate their work by designing algorithms to invoke previously lost algorithms. Finding lost algorithms allowed different segments of code to reconnect and interact with algorithms that had not been called upon by any code. Reconnecting interactions consolidated the position of algorithms in open source by working alongside interactions that were forceful and extended algorithmic reach. In a 2016 interview with the <sup>fi</sup>rst author, Torvalds discussed such reconnecting interactions:

We already automate as much of it as possible and all the maintainers I know use tools of various kinds of not just to maintain their trees, but to pick up the patches in the first place and prioritize them. For example, many maintainers use “patchwork” that automatically picks up patches from the various development mailing lists and gathers together comments about them.

Situations arose when code written by other devel opers, or even the same developer over time, became forgotten and ignored. Algorithms were well suited to pursue one another in a reconnecting exercise, irrespective of where the hidden algorithm existed:

“Generic” (module sg) does appear automagically. This confused me a bit. Doug Gilbert was kind enough to explain to me that the module loading needed be done explicitly for sr\_mod … . Then I came to wonder why “generic” registered by the module sg showed up. I thought that I was not calling for automatic loading of “sg” myself … .

It took me a while to <sup>fi</sup>gure out why “sg” was inserted automatically.<sup>25</sup>

In this example, a module sg (support generation module that provided access to SCSI devices) appeared without being invoked as though “automagically” (i.e., to developers’ surprise). An experienced developer explained that module sg was probably orphaned and embedded in code that was multitude of lines of code distant from the command the <sup>fi</sup>rst developer was attempting to invoke. Module sg had been found by a developer invoking a command algorithm and driven into implementation by an algorithm. Algorithms could connect and interact with one another through commands that developers initiated. Yet, clearly, not all algo rithmic behavior was expected or explicable.

Modularity through better task decomposition and effective interfacing was evident in BK. Together with Git, BK made it possible for developers to rely increasingly on algorithmic interactions. Forcing, extending, and reconnecting interactions worked together to strengthen and deepen algorithmic interactions. Developers became further removed from some of the daily tasks of their work through increased reliance on algorithms, yet over time, they realized such automation was not always effective without developer supervision. Developers work thus at times augmented the work of algorithms. Developers also understood that resilience of work required stability. They established stability through working closely with algorithms so that more tasks could be further automated in the future.

## Discussion and Implications

We explored algorithmic interactions to understand their signi<sup>fi</sup>cance in open source. Algorithms operating autonomously are key to solving problems in open source development when principles of modularity and parallel development cannot resolve all the issues that developers face. However, developers are seldom absent from these interactions. We thus establish a dynamic interactional approach of algorithms in open source working with and for developers to perform work.

## Processes of Algorithmic Interactions in Open Source

Developers in open source make an effort to deepen algorithm to algorithm interactions to automate work. Algorithmic interactions are not static moments. They are <sup>fl</sup>uid and fast-moving. They involve a set of processes that work together to increase and extend the capacity of humans and algorithms. Algorithms mediate interactions with developers. Importantly, algorithms also interact with one another, which occasionally makes developer intervention less necessary. Open source work has a deep reliance on algorithms. Open source work is accomplished by multiple algorithms at play simultaneously, which, in turn, creates multiple interactions among algorithms. This can generate complexity that increases concerns with modularity breakdowns and drives developers to create yet more algorithms to simplify tasks and reduce problems arising from residual interdependencies. Therefore, algorithmic interactions of open source work harness and increase developer reliance on algorithms in ways that enhance human capacities through semiautonomous operation.

Our <sup>fi</sup>ndings reveal three processes that, together, facilitate open source work (see Figure 2). The <sup>fi</sup>rst of these three processes, managing parallel development, entails creating associations and constructing a network of interactions to establish engagement rules. Interactions that occur as needed establish stability in open source work. However, algorithmic interactions do not always occur as designed. Defective interactions require the attention of developers to rebuild interactional pathways. If the defect is signi<sup>fi</sup>cant, it can stall work and break the rhythm of algorithmic interactions. Defective interactions nudge developers to reestablish themselves as intermediary actors. However, developer interventions enhance algorithms not only when problems arise but also through simple acts of initialization and constant vigilance of algorithms at work. Importantly, then, the work of developers is augmented by algorithms, but equally, the work of algorithms is augmented by developer intervention.

The second process—that of organizing modularity— reveals how developers build and amend algorithms to establish reliability across modules. An important issue with too much or too little modularity is establishing reliable relations between modules. Developers design algorithms to maintain and reestablish interactions between modules where needed. Certain tasks of open source become algorithmically self-sustained. These are often routine and well-structured tasks that are straightforward to automate. Equally, automation is evident with established algorithmic interactions repeating similar routines ef<sup>fi</sup>ciently. Interactions such as deactivating and simulating involve developer intervention to create the possibility of more substantial algorithmic interactions. They require a developer to stop the execution of a problematic algorithmic interaction or to build a workaround with yet another algorithm to simulate the effect of the problematic one. Developers are aware that as the codebase of their work grows, they need to rely more on algorithms to <sup>fi</sup>nd and resolve residual interdependencies. Algorithms do not only complete a task but also reverse problems, thus removing modularity problems unprompted by a developer.

Figure 2. Algorithmic Interactions Managing, Organizing, and Supervising Open Source  
![](/api/attachments/H6WG3WEF/fulltext/images/86604e1f2e93d034077415c8e850d5c959eabc64b7eda125ed61d87f9216d0a6.jpg)

The processes of managing parallel development and organizing modularity require momentum to establish and complete tasks that facilitate open source work. If interactions among algorithms are productive, these two processes feed into a third one, the process of algorithmic interactions supervising open source work. Interactions in this process become increasingly and purposefully designed to be algorithmic-centric: multiple interactions emerge among algorithms. This deepens the ability of algorithms to facilitate open source work through autonomous interactions. In open source work, developers remain the caretakers of algorithmic interactions and important intermediaries. Algorithms require care and oversight because interactions do break down; require maintenance, change, and updates; and redirection. This refutes the idea of complete automation.

In open source work, if an algorithmic interaction does not complete as tasked, then developers create another algorithm to <sup>fi</sup>x or nullify incorrect effects. Such breaks in automation are key moments in the process. When automation fails, a developer must reengage with the system to complete the task and <sup>fi</sup>x the problem. However, developers can only remedy the problem if they understand the problem and its interactional context. The interactional context makes the difference between a developer understanding the problem and resolving it or, instead, working through a repeat of trial and error steps. Once the problem is remedied, algorithmic interactions can continue as designed. Through experience and learning, developers can build better algorithms, create workarounds if the problem is not immediately <sup>fi</sup>xable, and learn which tasks to modularize and automate further.

Our study reveals that some algorithmic interactions create the possibility for more or less automation. Three dimensions are in<sup>fl</sup>uential in this process: the type of task, design and purpose of the algorithm, and interactional context. The task that is being performed by a developer and/or algorithm is relevant because its complexity, the frequency with which it is needed, and its type all contribute to the ability of a developer to design an algorithm to perform it. Certain tasks, because of their nature, can be readily converted into lines of instructions. With more experience of both the task at hand and developing algorithms, developers can deepen task conversion into algorithmic design. Related to the task is the algorithmic design and purpose. There are different types of algorithms (e.g., recursive, sequential), and their design affects how they run, interact, and even break down. Finally, the interactional context, which refers to the speci<sup>fi</sup>c con<sup>fi</sup>guration of programs running at the same time, the expertise of the developer, the operating system in use, and the number of programs running, also affects how algorithmic interactions unfold.

Depending on these three dimensions, the algorithm performs as designed or breaks down. If the algorithm performs as designed, developers continue to deepen their reliance on the autonomous performance of many algorithms while still being engaged with mediation such as initialization, vigilance, and minor adjust ments. Our <sup>fi</sup>ndings reveal that developers turn to algorithms to augment human effort. At the same time, however, algorithms also rely on developers to keep running smoothly. If an algorithm’s performance breaks down, then a developer must become more deeply engaged beyond simple vigilance. The problem needs to be <sup>fi</sup>xed for a return to <sup>fl</sup>uid algorithmic interactions to occur. Such an accomplishment deepens developers’ learning and understanding of various problems and their solutions.

## Implications for Open Source Work

Through a focus on algorithmic interactions, we explain how algorithms maneuver around problems of poor branching practices, merging issues, and increased complexity that arise as the distributed project’s codebase grows along with the number of contributing developers. It is through distinct types of algorithmic interactions that such problems are eliminated. Our study adds to prior scholarship on the speci<sup>fi</sup>c practices of sustaining and deepening parallel development and modularity (Narduzzo and Rossi 2008; Phillips et al. 2011; 2012). Our three processes illuminate how algorithmic interactions work to resolve issues with parallel development and modularity and supervise open source work. Our grounded theorization adds to open source scholarship an explanation of how algorithmic interactions remedy concerns with residual interdependencies through autonomously seeking, working around, or removing unwanted interactions.

Prior scholarship on open source has emphasized that modularity in excess can generate unnecessary interdependencies (Fitzgerald 2004) as well as create an in<sup>fl</sup>exible system of rules that guide across module behavior (Baldwin and Clark 2006). Few if any studies show us how open source accomplishes work despite such issues. Thus, our research offers a theorization of how algorithmic interactions accomplish open source work and ameliorate the problems that accompany modularity and parallel development (Feller and Fitzgerald 2002). Open source developers maintain algorithms so that algorithmic interactions continue to perform, thus ensuring that branching problems do not develop. The process of managing parallel development reveals how precise measures are taken to distinguish patches, patch history, and version branches. The numerous algorithms in operation together through interactions need to work through or around any emergent breakdown. Moreover, our study demonstrates instances of excessive modularity (Fitzgerald 2004) where algorithms are interacting with other unnecessary algorithms and slowing down open source work. Developers need to deactivate or reverse such interactions. A rigid system of rules across modules (Baldwin and Clark 2006) is resolved through simulating, forcing, or extending interactions. Our work adds to scholarship by offering a detailed mapping of algorithmic interactions as they resolve problems of modularity and parallel development in open source.

Research has focused on how work routines reveal new interdependencies of knowledge work and on where the integration of open source becomes the realm of a combination of developers and algorithms (Lindberg et al. 2016). There are studies on interdependencies between different types of technology (Bailey et al. 2010) as well as between technology and humans (Lindberg et al. 2016). A focus on Linux development allows us to show interactions that are involved in creating technological interdependencies (Bailey et al. 2010). This study offers a conceptualization of how multiple interactions and new interdependencies are built and operate between algorithms that together ensure that open source work continues without breakdowns. The algorithms in our study are multiple and so are the networks of their interactions. This is relevant because open source is complex, with numerous human actors and algorithms in operation. We add to scholarship on technological interdependencies by revealing how multiple algorithms build interdependencies that work simultaneously rather than sequentially.

Development interdependencies where code growth relies on other code are managed by version control. However, developer interdependencies relate to multiple developers all working together on the same problem through parallel development. For multiple developers to work together effectively, there is a need for collective understanding (Lindberg et al. 2016). Development and developer interdependencies need to be managed together. We add to this and other related work in open source a more focused examination of development interdependencies. Our study reveals that developer interdependencies are purposefully reduced over time when algorithms complete tasks on their own. This is not to suggest that develop ers are not needed by algorithms. Developers in open source want to automate tasks wherever possible. This could be due to automation breakdowns. Yet develop ers need to remain involved and vigilant to ensure that processes run smoothly (Bainbridge 1983). During breakdowns, as developers learn to <sup>fi</sup>x problems, they deepen their own knowledge and understanding of problem scenarios. Over time, this knowledge is converted into unambiguous algorithmic instructions, thus leading to the automation of more tasks.

Open source developers are both the users and developers of the algorithms upon which they rely. This positions them uniquely to gauge the strength of the algorithms in use in open source. They are experts. Past studies have focused on algorithms where changes in code, reviews, and ratings are taken as a proxy for algorithms in work settings (Orlikowski and Scott 2014; 2015). We move away from proxy manifestations of algorithms to the actual behavior of algorithms in practice as explained by their designers. Past work has also often, because of the chosen context, been forced to rely on access to users of algorithms rather than their designers and to traces of algorithmic interactions rather than interactions themselves. Our study offers examples where both a behavioral manifestation of changes and a deep discussion of algorithmic interactions that caused the change are made visible simultaneously. Moreover, algorithmic interactions also occur beyond open source settings: most platform-based work needs to consider the rami<sup>fi</sup>cations of increased reliance on algorithms interacting increasingly with other algorithms and humans.

## Implications for Augmentation and Automation of Open Source Work

Scholarship to date has converged in proposing that augmentation is the better approach, as it gives a voice to humans working with algorithms (Purao et al. 2003, Davenport and Ronanki 2018). We see a contrasting perspective in open source. The developers preferred approach is that of automation, because tasks are conducted online with many contributors working in parallel. If tasks are automated, then developers no longer need to micromanage all work. This frees up time for them to engage in development work that builds reputation (Stewart 2005, Gallus 2017). At the same time, there is a need for developers to remain vigilant and involved in many algorithmic interactions. When and how developers are needed to participate in the accomplishment of a task is not obvious. This is telling of the relationship between augmentation and automation (Wilson and Daugh erty 2018, Raisch and Krakowski 2021) in open source.

The relationship between automation and augmentation changes as does the question of what is being augmented: the work of developers or of algorithms. In open source, developers and algorithms build on each other’s work.

Some research has argued for the need of a more human-centric understanding of algorithmic use (Wilson and Daugherty 2018). This is often driven by a managerial perspective rather than a developer one. A related concern raised by similar studies is that human involvement and effort is usually rendered invisible, thus making it appear that augmented work is instead automated (Ekbia et al. 2015b, DeCanio 2016). However, our study of open source work illuminates not only the deep involvement of developers but also that their involvement is openly acknowledged and discussed in the community. Developers strive to make their work as automated as possible, so it is noteworthy to see that they complain about their own involvement in tasks that algorithms should have accomplished autonomously. Creating remedies for automation failures in open source also helps to establish the reputation of developers (Anthony et al. 2009). This contradicts the idea that all work to maintain algorithms is invisible and menial. In open source, this is not the case.

Regarding the nature of open source tasks that are a better <sup>fi</sup>t for automation, our study reveals that in work settings where users and designers of algorithms are the same, there will be a push for greater automation rather than augmentation of tasks. Yet our research also reveals that those tasks where human decision making is understood to improve the quality of work are protected to remain humancentric. We show that the judgement and evaluation of the most important part of an open source project, the code, must remain the domain of humans and not algorithms because algorithms are less able to discern innovative solutions.<sup>26</sup>

## Implications for Working with Algorithms

Beyond open source, algorithms and their interactions also have in<sup>fl</sup>uence on the future of work more generally. Our study highlights that the future workplace will need to consider the nature of the tasks being changed and the type of algorithms performing work. Studies that offer accounts of the future of work changing with algorithms often describe the tendency toward human deskilling and an increase in unemployment because arti<sup>fi</sup>cial intelligence (AI) may outpace and outperform humans in many jobs (Spencer 2018, Kellogg et al. 2020). Our study reveals that, for the time being and for some highly skilled and complex types of work at least, this fear may be misplaced. Algorithms are harnessed in open source work to carry out the kind of tasks that humans are not keen on doing and are less adept at completing ef<sup>fi</sup>ciently.

In turn, people can then focus on other, more creative, tasks. Algorithms may thus not always take jobs away from people: they also create the need for new and different jobs.

Our research also reveals that the experts who build and create algorithms in open source respect the work carried out by algorithms. Open source developers have the expertise to change algorithms. They appreciate algorithms that work to lessen their load. Develop ers are thus less likely to feel threatened by algorithms because they can change and understand them. This <sup>fi</sup>nding has implications for emerging scholarship on algorithms and work. Whereas much existing scholarship (Orlikowski and Scott 2015, Curchod et al. 2020) has focused on the link between algorithms working in the background and their relationship with users in the visible foreground, we develop a theorizing of how algorithmic interactions can shift from working quietly in the background to becoming the relevant foreground in some work settings.

## Limitations and Future Research

Like all research, our study has limitations that offer opportunities for future scholarship. For one, it would be useful to develop our ideas of algorithmic interactions in settings other than open source to understand how they play out in different settings such as in platform work where the algorithmic management of employees is common. Moreover, our study relies on a single in-depth case. It would be worthwhile to stretch the observations and analyses beyond this context. Access to minute algorithmic data as well as the code structure of algorithms may also prove interesting to understand how different types of code, in interaction with one another, operate under different settings.

It would also be relevant to see how AI settings would differ and how far our model would be applicable. AI may be associated with different or additional dimensions that in<sup>fl</sup>uence algorithmic interactions and their outcome. A possible lens to understand algorithmic interactions further would be that of multiagent systems (Ferber and Weiss 1999). Such a lens would be appropriate when the algorithms in question are part of an intelligent system (Rudowsky 2004) and the algorithms are capable of learning with minimal human supervision. Moreover, although our work took a human perspective to understand algorithmic interactions, it could be useful to follow algorithms solely. Finally, a longitudinal analysis of an algorithm and its interactions could be telling of its changes, its impact, and the pathways it takes in real-world settings.

## Conclusion

This study offers a theorization of how algorithmic interactions are spurred on by developers in open source and how these interactions eventually intensify. The intensi<sup>fi</sup>cation of algorithmic interactions automates and augments open source work because algorithms, though designed to work autonomously, often necessitate the presence and engagement of developers. In open source, the impetus for increased algorithmic interactions is rooted in developers’ motivation to make open source work more ef<sup>fi</sup>cient. The main contribution of this work includes a conceptualization of how algorithmic interactions are designed, fostered, and maintained in open source to overcome issues of too much or not enough modularity as well as the challenges not dealt with by parallel development.

## Acknowledgments

The authors thank senior editors Hemant Jain, Balaji Padmanabhan, Paul Pavlou, and Raghu Santanam. They are very grateful to the associate editor, Likoebe Maruping, for his constructive support of their work, and they thank their reviewers.

## Endnotes

<sup>1</sup> See https://git-scm.com/.

<sup>2</sup> BitKeeper Documentation is an online resource, see https://www. bitkeeper.org/documentation.html.

<sup>3</sup> For the sake of simplicity, we will, for the rest of the paper, refer to Git’s continuous integration hooks as “Git hooks.”

<sup>4</sup> Junio C Hamano, “[ANNOUNCE] Git v.2.14.0,” Linux-Kernel Archive, August 4, 2017, http://lkml.iu.edu/hypermail/linux/kernel/1708. 0/03653.html.

<sup>5</sup> Larry McVoy, “Re: The Linux Kernel Project Management System (INITIAL PROPOSAL),” Linux-Kernel Archive, September 27, 1999, http://lkml.iu.edu/hypermail/linux/kernel/9909.3/0518.html.

<sup>6</sup> Linus Torvalds, “Re: A modest proposal—We need a patch penguin,” Linux-Kernel Archive, January 30, 2002, http://lkml.iu.edu/ hypermail/linux/kernel/0201.3/1834.html.

<sup>7</sup> Zack Brown, “Re: BitBucket: GPL-ed KitBeeper clone,” Linux-Kernel Archive, March 8, 2003, http://lkml.iu.edu/hypermail/linux kernel/0303.1/0155.html.

<sup>8</sup> Horst von Brand, “Re: BitBucket: GPL-ed KitBeeper clone,” Linux-Kernel Archive, March 12, 2003, http://lkml.iu.edu/hypermail/linux kernel/0303.1/0911.html.

<sup>9</sup> Vitaly Kuznetsov, “[PATCH v3 0/2] hv\_util: adjust system time smoothly,” Linux-Kernel Archive, January 17, 2017, http://lkml.iu. edu/hypermail/linux/kernel/1701.2/01329.html.

<sup>10</sup> Larry McVoy, “Re: [Linux-fbdev-devel] Fbdev Bitkeeper repository,” Linux-Kernel Archive, April 17, 2002, http://lkml.iu.edu/hypermail linux/kernel/0204.2/0288 html

<sup>11</sup> Greg Kroah-Hartman<sup>,</sup> “[PATCH 4.18 016/150] netfilter: bridge: Dont sabotage nf\_hook calls from an l3mdev,” Linux-Kernel Archive, November 2, 2018, http://lkml.iu.edu/hypermail/linux/ kernel/1811.0/01305.html.

<sup>12</sup> Junio C Hamano, “[ANNOUNCE] Git v2.12.0-rc0,” Linux-Kernel Archive, February 3, 2017, http://lkml.iu.edu/hypermail/linux kernel/1702.0/02306.html.

<sup>13</sup> Junio C Hamano, “[ANNOUNCE] Git v2.13.0,” Linux-Kernel Archive, May 9, 2017, http://lkml.iu.edu/hypermail/linux/kernel 1705.1/01336 btml

<sup>14</sup> Troy Benjegerdes, “Re: The direction linux is taking,” Linux-Kernel Archive, December 27, 2001, https://lkml.iu.edu/hypermail/ linux/kernel/0112.3/0545.html.

<sup>15</sup> Hamano, “[ANNOUNCE] Git v.2.14.0.”

<sup>16</sup> Hamano, “[ANNOUNCE] Git v2.13.0.”

<sup>17</sup> Mark Brown, “[PATCH RFC 2/2] MIPS: dt: Explicitly specify native endian behaviour for syscon,” Linux-Kernel Archive, January 26, 2016, http://lkml.iu.edu/hypermail/linux/kernel/1601.3/ 02711.html.

<sup>18</sup> Chris Kuehl, “Allow specifying environment variables for hook installation? #758,” GitHub, June 1, 2018, https://github.com/precommit/pre-commit/issues/758

<sup>19</sup> Brown, “[PATCH RFC 2/2].”

<sup>20</sup> M. R. Brown, “Re: [Linux-fbdev-devel] Fbdev Bitkeeper repository,” Linux-Kernel Archive, April 17, 2002, http://lkml.iu.edu/hypermail linux/kernel/0204.2/0371.html

<sup>21</sup> Benjegerdes, “Re: The direction linux is taking.”

<sup>22</sup> Benjegerdes, “Re: The direction linux is taking.”

<sup>23</sup> Contreras 2011, see https://lkml.iu.edu/hypermail/linux/kernel/ 1112.0/02330 btml

<sup>24</sup> Rik van Riel, “a proper .cvsignore for the kernel,” Linux-Kernel Archive, January 2, 1999, http://lkml.iu.edu/hypermail/linux/ kernel/9901.0/0334.html.

<sup>25</sup> Ishikawa, “Found out why "sg" was loaded automagically. Re: devfs: "cd" device not showing up initially,” Linux-Kernel Archive, March 2, 2001, http://lkml.iu.edu/hypermail/linux/kernel/0103. 0/0356.html.

<sup>26</sup> This may well change if machine learning algorithms are employed to accomplish this task in the future.

## References

Anthony D, Smith SW, Williamson T (2009) Reputation and reliability in collective goods: The case of the online encyclopedia Wikipedia. Rationality Soc. 21(3):283–306.

Asimov I (1942) Runaround. Astounding Sci. Fiction (March), 94–103.

Atkins DL, Ball T, Graves TL, Mockus A (2002) Using version control data to evaluate the impact of software tools: A case study of the version editor. IEEE Trans. Software Engrg. 28(7):625–637.

Bailey DE, Leonardi PM, Chong J (2010) Minding the gaps: Understanding technology interdependence and coordination in knowl edge work. Organ. Sci. 21(3):713–730.

Bainbridge L (1983) Ironies of automation. Johannsen G, Rijnsdorp JE, eds. Analysis, Design and Evaluation of Man–Machine Systems (Elsevier, Oxford, UK), 129–135.

Balasubramanian N, Ye Y, Xu M (2022) Substituting human decisionmaking with machine learning: Implications for organizational learning. Acad. Management Rev. Forthcoming.

Baldwin CY, Clark KB (2006) Modularity in the design of complex engineering systems. Braha D, Minai A, Bar-Yam Y, eds. Com plex Engineered Systems (Springer, Berlin), 175–205.

Beer D (2017) The social power of algorithms. Inform. Comm. Soc. 20(1):1–13.

Brynjolfsson E, McAfee A (2011) Race Against the Machine: How the Digital Revolution Is Accelerating Innovation, Driving Productivity, and Irreversibly Transforming Employment and the Economy (Digital Frontier Press, Lexington, MA).

Burton JW, Stein M-K, Jensen TB (2020) A systematic review of algo rithm aversion in augmented decision making. J. Behav. Decision Making 33(2):220–239.

Charmaz K (2006) Constructing Grounded Theory: A Practical Guide Through Qualitative Analysis (Sage Publications, London).

Cloutier C, Langley A (2020) What makes a process theoretical contribution? Organ. Theory 1(1):1–32.

Curchod C, Patriotta G, Cohen L, Neysen N (2020) Working for an algorithm: Power asymmetries and agency in online work settings. Admin. Sci. Quart. 65(3):644–676.

Davenport TH, Ronanki R (2018) Arti<sup>fi</sup>cial intelligence for the real world. Harvard Bus. Rev. 96(1):108–116.

DeCanio SJ (2016) Robots and humans—Complements or substi tutes? J. Macroeconom. 49(September):280–291.

Ebben M (2020) Automation and augmentation: Human labor as essential complement to machines. Hai-Jew S, ed. Maintaining Social Well-Being and Meaningful Work in a Highly Automated Job Market (IGI Global, Hershey, PA), 1–24.

Ekbia HR, Nardi BA (2017) Heteromation, and Other Stories of Comput ing and Capitalism (MIT Press, Cambridge, MA).

Ekbia HR, Nardi BA (2018) From form to content. Cultural Anthro pol. 33(3):360–367.

Ekbia HR, Nardi B, <sup>ˇ</sup>Sabanovic S (2015a) On the margins of the machine:´ Heteromation and robotics. iConference 2015 Proc. (iSchools, Grandville, MI), http://hdl.handle.net/2142/73678.

Ekbia H, Mattioli M, Kouper I, Arave G, Ghazinejad A, Bowman T, Suri VR, Tsou A, Weingart S, Sugimoto CR (2015b) Big data, bigger dilemmas: A critical review. J. Assoc. Inform. Sci. Tech. 66(8):1523–1545.

Engelbart DC (1962) Augmenting human intellect: A conceptual framework. Summary Report AFOSR-3223, Stanford Research Insti tute, Menlo Park, CA.

Feller J, Fitzgerald B (2002) Understanding Open Source Software Development (Addison-Wesley, London).

Ferber J, Weiss G (1999) Multi-Agent Systems: An Introduction to Distributed Artificial Intelligence (Addison-Wesley, Reading, MA).

Fitzgerald B (2004) A critical look at open source. Computer 37(7): 92–94.

Fitzgerald B (2006) The transformation of open source software. MIS Quart. 30(3):587–598.

Fitzgerald B, Feller J (2002) A further investigation of open source software: Community, co-ordination, code quality and security issues. Inform. Systems J. 12(1):3–6.

Fogel K (1999) Open Source Development with CVS (Coriolis Open Press, Scottsdale, AZ).

Gallus J (2017) Fostering public good contributions with symbolic awards: A large-scale natural <sup>fi</sup>eld experiment at Wikipedia. Management Sci. 63(12):3999–4015.

Gavras K, Kostakis V (2021) Mapping the types of modularity in open-source hardware. Design Sci. 7, https://doi.org/10.1017/ dsj.2021.11.

Ghosh RA (1998) Interviews with Linus Torvalds: What motivates free software developers? First Monday 3(3), https://doi.org/10. 5210/fm.v3i2.583.

Glaser BG, Strauss A (1967) The Discovery of Grounded Theory: Strat egies for Qualitative Research (Aldine, Chicago).

Grønsund T, Aanestad M (2020) Augmenting the algorithm: Emerging human-in-the-loop work con<sup>fi</sup>gurations. J. Strategic Inform. Systems 29(2):101614.

Hancke T (2020) Ironies of automation 4.0. IFAC-PapersOnLine 53(2): 17463–17468.

Howison J, Crowston K (2014) Collaboration through open superposi tion: A theory of the open source way. MIS Quart. 38(1):29–50.

Hui Y (2015) Algorithmic catastrophe—The revenge of contingency. Parrhesia 34:122–143.

Jussupow E, Spohrer K, Heinzl A, Gawlitza J (2021) Augmenting medical diagnosis decisions? An investigation into physicians decision-making process with arti<sup>fi</sup>cial intelligence. Inform. Systems Res, 32(3):713–735

Kallinikos J, Tempini N (2014) Patient data as medical facts: Social media practices as a foundation for medical knowledge creation. Inform. Systems Res. 25(4):817–833.

Kellogg K, Valentine M, Christin A (2020) Algorithms at work: The new contested terrain of control. Acad. Management Ann. 14(1): 366–410.

Koike H, Chu HC (1997) VRCS: Integrating version control and module management using interactive three-dimensional graphics. Proc. IEEE Sympos. Visual Languages (IEEE, Piscataway, NJ), 168–173.

Kornilov AS, Safonov IV (2018) An overview of watershed algorithm implementations in open source libraries. J. Imaging 4(10):123

Krippendorff K (1980) Content Analysis: An Introduction to Its Methodology (Sage Publications, Beverly Hills, CA).

Lakhani K, von Hippel E (2003) How open source software works: “Free” user-to-user assistance. Res. Policy 32(6):923–943.

Langlois RN, Garzarelli G (2008) Of hackers and hairdressers: Modularity and the organizational economics of open-source collab oration. Indust. Innov. 15(2):125–143.

Lazer D (2015) The rise of the social algorithm. Science 348(6239): 1090–1091.

Lenglet M, Mol J (2016) Squaring the speed of light? Regulating market access in algorithmic <sup>fi</sup>nance. Econom. Soc. 45(2):201– 229.

Lindberg A, Berente N, Gaskin J, Lyytinen K (2016) Coordinating interdependencies in online communities: A study of an open source software project. Inform. Systems Res. 27(4):751–772.

Lindebaum D, Vesa M, den Hond F (2020) Insights from “the machine stops” to better understand rational assumptions in algorithmic decision making and its implications for organizations. Acad. Management Rev. 45(1):247–263.

Lynch NA (1996) Distributed Algorithms (Morgan Kaufmann, San Francisco).

Lynch C (2017) Stewardship in the “Age of Algorithms.” First Mon day 22(12), http://dx.doi.org/10.5210/fm.v22i112.8097.

MacKenzie D (2018) ‘Making’, ‘taking’ and the material political economy of algorithmic trading. Econom. Soc. 47(4):501–523.

Maruping LM, Daniel SL, Cataldo M (2019) Developer centrality and the impact of value congruence and incongruence on commitment and code contribution activity in open source software communities. MIS Quart. 43(3):951–976.

Miklos-Thal J, Tucker C (2019) Collusion by algorithm: Does better´ demand prediction facilitate coordination between sellers? Management Sci. 65(4):1552–1561.

Mindel V, Mathiassen L, Rai A (2018) The sustainability of polycen tric information commons. MIS Quart. 42(2):607–632.

Mohler GO, Short MB, Malinowski S, Johnson M, Tita GE, Bertozzi AL, Brantingham PJ (2015) Randomized controlled <sup>fi</sup>eld trials of predictive policing. J. Amer. Statist. Assoc. 110(512): 1399–1411.

Moon JY, Sproull L (2000) Essence of distributed work: The case of the Linux Kernel. First Monday 5(11), https://doi.org/10.5210/ fm v5i11.801

Moschovakis YN (2001) What is an algorithm? Engquist B, Schmid W, eds. Mathematics Unlimited—2001 and Beyond (Springer, Berlin) 919–936.

Narduzzo A, Rossi A (2008) The role of modularity in free/open source software development. Tan FB, ed. Global Information Technologies: Concepts, Methodologies, Tools, and Applications, vol. 1 (IGI Global, Hershey, PA), 449–464.

Neuendorf KA (2002) The Content Analysis Guidebook (Sage Publications, Thousand Oaks, CA).

Neyland D, Mollers N (2017) Algorithmic if¨ … then rules and the conditions and consequences of power. Inform. Comm. Soc. 20(1):45–62.

Nugroho YS, Hata H, Matsumoto K (2020) How different are different diff algorithms in Git? Empir. Software Engrg. 25(1): 790–823.

O’Mahony S, Ferraro F (2007) The emergence of governance in an open source community. Acad. Management J. 50(5):1079–1106.

Orlikowski WJ, Scott SV (2014) What happens when evaluation goes online? Exploring apparatuses of valuation in the travel sector. Organ. Sci. 25(3):868–891.

Orlikowski WJ, Scott SV (2015) The algorithm and the crowd: Considering the materiality of service innovation. MIS Quart. 39(1): 201–216.

Orton JD (1997) From inductive to iterative grounded theory: Zip ping the gap between process theory and process data. Scand. J. Management 13(4):419–438.

Phillips S, Ruhe G, Sillito J (2012) Information needs for integration decisions in the release process of large-scale parallel development. Proc. ACM 2012 Conf. Comput. Supported Cooperative Work (ACM, New York), 1371–1380.

Phillips S, Sillito J, Walker R (2011) Branching and merging: An investigation into current version control practices. Proc. 4th Internat. Workshop Cooperative Human Aspects Software Engrg. (ACM, New York), 9–15.

Purao S, Storey VC, Han T (2003) Improving analysis pattern reuse in conceptual design: Augmenting automated processes with supervised learning. Inform. Systems Res. 14(3):269–290.

Raisch S, Krakowski S (2021) Arti<sup>fi</sup>cial intelligence and management: The automation–augmentation paradox. Acad. Management Rev. 46(1):192–210.

Raj M, Seamans R (2019) Primer on arti<sup>fi</sup>cial intelligence and robotics. J. Organ. Design 8(1):Article 11.

Roberts J, Hann I-H, Slaughter S (2006) Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7):984–999.

Rudowsky I (2004) Intelligent agents. Comm. Assoc. Inform. Systems 14(1):275–290.

Salovaara A, Lyytinen K, Penttinen E (2019) High reliability in digi tal organizing: Mindlessness, the frame problem, and digita operations. MIS Quart. 43(2):555–578.

Schildt H (2017) Big data and organizational design—The brave new world of algorithmic management and computer augmented transparency. Innovation 19(1):23–30.

Shaikh M, Vaast E (2016) Folding and unfolding: Balancing openness and transparency in open source communities. Inform. Systems Res. 27(4):813–833.

Skagestad P (1993) Thinking with machines: Intelligence augmentation, evolutionary epistemology, and semiotic. J. Soc. Evolutionary Systems 16(2):157–180.

Spencer DA (2018) Fear and hope in an age of mass automation: Debating the future of work. New Tech. Work Employment 33(1):1–12.

Stewart D (2005) Social status in an open-source community. Amer Sociol. Rev. 70(5):823–842

Strauss A, Corbin J (1998) Basics of Qualitative Research: Technique and Procedures for Developing Grounded Theory (Sage Publications, Thousand Oaks, CA).

Tel G (2000) Introduction to Distributed Algorithms (Cambridge Uni versity Press, Cambridge, UK).

Teodorescu MHM, Morse L, Awwad Y, Kane GC (2021) Failures of fairness in automation require a deeper understanding in human Ml augmentation. MIS Quart. 45(3):1483–1500.

Walker D, Myrick F (2006) Grounded theory: An exploration of process and procedure. Qualitative Health Res. 16(4):547–559.

Wiesche M, Jurisch MC, Yetton PW, Krcmar H (2017) Grounded theory methodology in information systems research. MIS Quart. 41(3):685–701.

Wilson HJ, Daugherty PR (2018) Collaborative intelligence: Humans and AI are joining forces. Harvard Bus. Rev. 96(4):114–123.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
