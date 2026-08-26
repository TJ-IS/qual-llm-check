---
otero_id: 1562
otero_key: "CA7C7XT9"
title: "Distributed Cognition in Software Design:  An Experimental Investigation of the Role of Design Patterns and Collaboration"
authors: "George Mangalaraj; Sridhar P. Nerur; Radha K. Mahapatra; and Kenneth H. Price"
year: "1999"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.1.12"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DISTRIBUTED COGNITION IN SOFTWARE DESIGN: AN EXPERIMENTAL INVESTIGATION OF THE ROLE OF DESIGN PATTERNS AND COLLABORATION<sup>1</sup>

George Mangalaraj

College of Business and Technology, Western Illinois University, Macomb, IL 61455 U.S.A. {g-mangalaraj@wiu.edu}

Sridhar Nerur, RadhaKanta Mahapatra, and Kenneth H. Price

College of Business Administration, University of Texas at Arlington, Arlington, TX 76019-0437 U.S.A. {snerur@uta.edu} {mahapatra@uta.edu} {price@uta.edu}

Software design is a knowledge intensive task that constitutes a critical part of the software development process. Using a controlled experiment involving software practitioners, this research examines two potentially useful mechanisms for improving the software design process. Specifically, this study examines the impact of structural distribution of cognition through design patterns and social distribution of cognition through collaborating pairs on design outcomes. The results indicate that the use of design patterns as external cognitive artifacts improves design quality, reduces time taken to solve a design problem, and leads to higher participant satisfaction. Collaborating pairs of software designers were compared to participants working alone but whose efforts were conjointly considered as the best and second-best members of nominal pairs. It was found that paired designers produced higher quality designs compared with the second-best members of nominal pairs, did not differ from the best member of a nominal pair, but took more time to complete a design task than either member of a nominal pair. The results also indicate that the availability of design patterns raises the performance level of the second-best member of a nominal pair, in terms of quality, and reduces task completion time when compared with a pair not using design patterns. Finally, paired designers were found to experience higher levels of task satisfaction when compared with individuals. Implications for research and practice are discussed.

Keywords: Software design, agile methodology, paired design, design pattern, nominal group, distributed cognition, codified knowledge

## Introduction

Software design is a cognitively challenging endeavor that has frequently been described as “knowledge intensive” (e.g.,

Robillard 1999) and “complex” (e.g., Agarwal et al. 1996). Among other things, it promotes an understanding and representation of the software problem, both of which are important precursors to programming (Pennington 1987). A good design satisfies the goals of catching errors early (i.e., at the source), eliminating expensive and time-consuming rework, and enhancing the quality of the final software product (Guindon 1990). However, the ambiguity inherent in a design problem presents enormous challenges in terms of enumerating alternatives, evaluating them, and choosing the right solution. Over time, the proponents of software development have evolved myriad “best practices” to ameliorate the design process. Examples include design patterns, pair programming, iterative development, and test-driven development, to name but a few. However, claims about the efficacy of such practices are based largely on anecdotal and experiential accounts, and have scarcely been subjected to rigorous empirical analysis (Zhang and Budgen 2012). There is clearly a need to integrate current software development practices within the body of theoretically grounded empirical research to enhance our understanding of potential advantages and limitations, as well as appropriate applications of these practices.

The unyielding quest for building good software has brought about unprecedented changes to the software development landscape. First, there is a perceptible shift to a collaborative development environment characterized by extensive social interaction among developers and users. A case in point is paired development, which involves two persons working collaboratively on the same problem throughout the development life cycle (Williams et al. 2000). Second, the role of physical artifacts, such as story cards, code fragments, analysis/design diagrams (e.g., class diagrams, sequence diagrams), and software patterns, in fostering feedback and communication is assuming greater significance in software development (Sharp et al. 2009). From a distributed cognition perspective, such an environment presents opportunities for the emergence of cognitive properties that transcend those that are associated with individuals alone (Flor and Hutchins 1991).

Hollan et al. (2000, p. 177) refer to distributed cognition as “a broader conception that includes phenomena that emerge in social interactions as well as interactions between people and structure in their environments.” Broadly speaking, there are two aspects of distributed cognition, social and embodied or structural (Hansen and Lyytinen 2009; Hollan et al. 2000). Socially distributed cognition arises from the dynamic exchange and processing of information between two or more members of a group engaged in a problem-solving task. Structurally distributed cognition, on the other hand, is an outcome of the processing of information interlaced between internal cognitive processes and external artifacts that contain information related to the task at hand. Clearly, this conception goes beyond our customary view of cognition as something that is confined to an individual’s internal processes. It is apparent that contemporary software development involves both social (e.g., pair programming) and structural (e.g., interaction between a developer and an external cognitive resource such as design patterns) distribution of cognition (for example, see Flor and Hutchins 1991; Sharp and Robinson 2008; Sharp et al. 2009). Thus, distributed cognition theory provides an ideal framework to empirically investigate alternative cognitive systems that software development practices engender. To achieve this end, our study evaluates the performance of four cognitive systems resulting from the combination of presence (absence) of social interaction and availability (nonavailability) of a task-related artifact. Specifically, the instantiation of these four cognitive architectures occurs through the use of pair designing to represent the social dimension and design patterns to signify the structural aspect.

The use of pairs is motivated by the increasing popularity and widespread acceptance of pairs and larger teams in the development of software applications (Ambler 2007). However, unlike many studies on pair programming, we focus on software design. Most prior studies on pair programming (Balijepally et al. 2009) have examined how pairs perform vis-à-vis individuals on tasks that were fairly straightforward: code templates were given and the experiment simply involved the creation and/or completion of methods/functions to satisfy the requirements. Subjects engaged in these experiments did not have to search their knowledge structures either to apply sound object-oriented design principles or to evaluate architectural trade-offs, both of which are critical in software development. In contrast, software design is a relatively illstructured activity that is likely to place greater demands on group processes (e.g., communication and coordination).

One of the limitations of the extant empirical research on pair programming (Arisholm et al. 2007; Nosek 1998) is that the performance of collaborating pairs was compared with the same number of individuals working alone (e.g., the mean performance of 20 pairs was compared to the mean performance of 20 individuals working alone). The numerical advantage of collaborating pairs in this approach makes it difficult to determine whether higher performance of the pairs was due to interaction between the two individuals or simply a statistical artifact of having more individuals engaged in the problem solving process. A more rigorous method of comparison advocated in the literature involves randomly assigning subjects who work individually to equal-sized groups, called nominal groups (Balijepally et al. 2009; Laughlin et al. 2006). In our study, designers working individually were randomly paired to create nominal pairs. The members of a nominal pair were rank ordered based on their performance in the design task. The one with superior performance was referred to as the best member and the other was called the second-best member. This approach enabled us to compare the performance of a collaborating pair with that of the best and the second best-member of a nominal pair.

The choice of design patterns as external cognitive artifacts is inspired in part by their potential to facilitate the creation and/or use of knowledge structures (i.e., schemata) (Kohls and Scheiter 2008; Robillard 1999). Robillard (1999, p. 89)

suggests that “some software methodologies explicitly promote the use or creation of schema; an example is software patterns.” Zhang and Budgen (2012, p. 19) note that the findings from the limited body of empirical research on design patterns are equivocal and that “more design-centric evidence is very much needed.” The few empirical studies that have been conducted focused primarily on software maintenance tasks (Prechelt et al. 2001; Prechelt et al. 2002; Vokac et al. 2004) and/or involved coding (Zhang and Budgen 2012). A compelling argument for the use of design patterns in our study stems from the scarcity of research on patterns, the need to empirically affirm their efficacy in design-centric tasks, and the potential of design patterns to influence the dynamics of social interactions and enrich the cognitive properties of the system.

In light of the preceding discussion, our study makes a notable contribution to the literature by addressing the following questions:

1. How would a socially distributed cognitive system comprising a collaborating pair perform vis-à-vis individuals in a software design task?

2. How would a structurally enhanced cognitive system affect the performance of software designers?

3. When comparing the performance of a low performing software designer with that of a collaborating pair, would the availability of an external cognitive artifact to the former compensate for the absence of a social actor?

In summary, our study draws on insights from distributed cognition theory to provide an understanding of two contemporary practices that have received considerable attention in the software development community. In addition to elucidating the ideas of distributed cognition in a software development setting, it sheds light on the efficacy of pairs and design patterns in design tasks. Thus, it has implications for both theory and practice.

The remainder of the paper is organized as follows: The next section presents the research framework followed by a discussion of the research model and specific hypotheses. We then outline the research methodology and present the results. The paper concludes with a discussion of the findings and their implications for research and practice.

## Research Framework

Table 1 presents a summary of conceptual foundations of our study, details of which are outlined in the following sections.

## Overview of Distributed Cognition

Distributed cognition theory calls into question the premise that internal processes alone give rise to cognition, and contends that the social context and the artifacts present in the environment result in a cognitive system that transcends individual cognition (Flor and Hutchins 1991). Cognitive processes may be distributed in three ways (Hollan et al. 2000). First, they may be socially distributed among actors engaged in a collaborative activity. Individuals in a group actively organize themselves and coordinate their efforts to accomplish tasks. Dynamic processing of information resulting from their rich interactions gives rise to a complex system with cognitive processes that are not only singularly different but also cannot be easily anticipated from any constituent member’s internal processes. Second, a cognitive architecture with properties distinct from those of its components may emerge from the interactions between internal cognitive processes (within individuals) and cognitive artifacts or structures (e.g., external media containing taskrelated information) in the work environment. This is referred to as embodied (Hollan et al. 2000) or structural (Hansen and Lyytinen 2009) cognition. Third, there is a temporal aspect of distributed cognition that suggests that experience from past cognitive events can have a bearing on subsequent ones (e.g., Hansen and Lyytinen 2009; Hollan et al. 2000).

Although the usefulness of the theory of distributed cognition for explicating software development phenomena was suggested many years ago (Flor and Hutchins 1991), very few studies have actually employed the theory to study software engineering practices. The few notable exceptions are Sharp and Robinson (2006), Hansen and Lyytinen (2009), and Ramasubbu et al. (2012).

Sharp and Robinson drew on the distributed cognition perspective to elaborate on the difficulties and issues that four mature XP (extreme programming) teams encountered in their collaborative efforts that were mediated by artifacts (e.g., story cards, flipcharts, working code) in the work environment. Hansen and Lyytinen performed a multiple-case study rooted in the tenets of distributed cognition to elucidate the distributed nature of requirements processes that occur during information systems development. Ramasubbu et al. conceptualized their experimental setting as a distributed cognition system to investigate how the interplay between team strategy and structural complexity (extent of cohesion/coupling) affects performance in a software maintenance task. Unlike these studies, our research examines the performance of four cognitive architectures resulting from the interplay between various levels of social distribution (pair versus individual) and structural distribution (with and without design patterns).

<table><tr><td>Conceptual Foundation</td><td>Description</td><td>Relevance to Our Study</td></tr><tr><td>Distributed cognition (Socially versus structurally distributed cognition)</td><td>A cognitive system extends beyond an individual&#x27;s mind. Specifically, cognition may be distributed across individuals, or between individuals and task-related artifacts in the environment. The human cognitive system may be extended by adding a partner (social distribution) or by adding an external artifact (structural distribution).</td><td>Four cognitive arrangements (presence/absence of a partner versus availability/nonavailability of an external artifact) were evaluated. Paired designing provided the socially distributed context while design patterns served as cognitive artifacts with the potential to influence task outcomes.</td></tr><tr><td colspan="3">Distributed Cognition and the Software Design Task</td></tr><tr><td>Structuring the problem space</td><td>The problem space for a design task is typically unstructured because of incomplete information and/or lack of clarity in requirements. Providing access to task-related information can enhance the chances of transforming an ambiguous design problem into a well-structured one, and facilitate its solution.</td><td>Design patterns as external representational media (i.e., structurally distributed cognition) have the potential to facilitate opportunistic designs, evoke cognitive processes relevant to the task at hand, and fill informational gaps to reduce the inherent ambiguity of design problems. Thus, they can affect both the quality of the solution and the time taken to solve the problem by focusing attention on a limited range of feasible alternatives. Likewise, socially distributed cognition in the event of pairing can augment the pool of available knowledge and bridge any gaps that might exist in the problem space.</td></tr><tr><td>Pairing in software design</td><td>Performance of pairs may be enhanced (hindered) by process gains (losses). The comparative performance of pairs and individuals is an enduring stream of research.</td><td>Consistent with prior research in the pair programming domain, our study compares the performance of pairs with that of individuals in the context of software design.</td></tr></table>

## Structurally Distributed Cognition: Software Design and Design Patterns

The goal of design is to develop software that is flexible, extensible, reusable, and easy to maintain (Richter 1999b). Design patterns are a significant development toward this end. Gamma et al. (1995, p. 1) observe that “patterns solve specific design problems and make object-oriented designs more flexible, elegant, and ultimately reusable.” Design patterns rely on abstract cognitive representations as opposed to lower level implementation code to provide design and/or architectural insights (Schmidt et al. 1996). As abstractions, they are domain-independent, but have a descriptive name that is often indicative of what they do, and represent what was once implicitly known only to expert designers (Gamma et al. 1995). In essence, they codify knowledge gleaned from the experiences of good software designers and can be applied to commonly occurring design problems. Therefore, design patterns may be “regarded as a means of codifying expert knowledge schemas derived from software design practice” (Zhang and Budgen 2012).

Figure 1 illustrates a design pattern. It includes the intent of the pattern, the motivation for using the pattern, where it can be applied, how it can be used in a specific context, and the implications of using the pattern (Gamma et al. 1995). The intent and the application context constitute declarative knowledge, whereas the guidelines on how to use a pattern in a given situation determine the procedural knowledge (Kohls and Scheiter 2008). Appendix A describes the application of this design pattern to a specific design problem.

Newell and Simon’s (1972) theory of human problem solving frames the formulation of a solution to a problem as a search process. According to this theory, the search involved in moving from the problem space to the solution space (i.e., the desired goal state) may be enhanced by applying declarative knowledge, algorithms, and heuristics as well as by following creative problem-solving techniques. Guindon (1990) observes that prior knowledge is useful in solving ill-structured problems such as software design. Patterns provide insight into the problem by acting as a guide in pointing the designer to a solution path. This helps constrain the search space for potential solutions (e.g., Kohls and Scheiter 2008), and hence reduces the time to solve a design problem. Indeed, a design pattern, when used as an external representational medium, is a cognitive artifact that has the potential to (1) serve as an informational scaffold for existing schemas, thereby facilitating

In many scenarios, we may have an object that has different states and each state may have to exhibit different behavior. State pattern utilizes an abstract class to represent the state and it is inherited by all the classes belonging to various operational states.

State pattern is used when the object’s behavior has to change at run-time based on the state. This pattern eliminates the need for conditional statements to check for state and to use appropriate methods.

![](/api/attachments/CA7C7XT9/fulltext/images/f2c3073f2e5c76b0294610bfb1d9b83c49e8608df5b95d0b9c682c7571478130.jpg)

Some of the benefits of the State pattern are (1) it localizes state-specific behavior to separate classes, (2) it makes state transitions explicit, (3) it also share state objects.

Figure 1. Example of a Design Pattern (adapted from Gamma et al. 1995)

their activation and/or (2) reorganize internal knowledge structures in light of new problem-related insights that the pattern provides (e.g., Kohls and Scheiter 2008; Robillard 1999).

Despite the attention received by design patterns in the software engineering literature, empirical research on the topic is sparse (Zhang and Budgen 2012). Prechelt et al. (2001) found that the use of patterns in software maintenance tasks led to improved solution flexibility. However, they also noted that patterns could sometimes result in a more complex solution. In a subsequent study, Prechelt et al. (2002) found that adding comment lines about the pattern used in maintenance programs may result in faster task completion time and fewer errors. Vokac et al. (2004) replicated the first Prechelt et al. study and found the results to be consistent to a great extent. Since design tasks are fundamentally different from maintenance activities, the findings of these studies, albeit insightful, can scarcely be extended to the design domain.

While patterns offer many benefits, there are some caveats to their use. Since patterns offer abstract solutions to problems, designers must carefully adapt the pattern to come up with a specific solution to the problem at hand. Solution adaptation, if not done carefully, can lead to suboptimal results due to anchoring and adjustment biases (Allen and Parsons 2010; Parsons and Saunders 2004). Poor adaptation can also lead to solutions with unwanted features that may make the code error-prone or require more maintenance effort (Prechelt et al. 2001). A lack of knowledge of patterns can lead to inappropriate use and errors (Prechelt et al. 2001). Thus, patterns can help designers. If not used properly, they can also lead to poor designs. It is, therefore, imperative to study the effect of patterns on the outcome of design tasks.

## Socially Distributed Cognition: Pairs in Software Development

Pairing of individuals to work collaboratively on all aspects of software development is claimed to be another strategy for improving design quality (Williams et al. 2000). When individuals engage in collaborative problem solving, they bring unique ideas and competencies to bear on the problem and facilitate the cross-checking of a solution as it unfolds (see Hinsz et al. 1997). Further, distributed cognition theory suggests that the conception of a pair should be expanded to embrace a richer cognitive system that springs forth from the interactions between members of a pair as well as from the interplay between the social actors and the environment in which they are situated (Flor and Hutchins 1991; Hollan et al. 2000; Rosen et al. 2009).

While proponents of XP assert that pairs produce higherquality software with fewer defect densities than traditional programming, researchers have found mixed empirical support for such claims. Early studies by Nosek (1998) and Williams et al. (2000) found that pairs produced higher quality solutions. In contrast, Domino et al. (2007) found that pairs performed worse than individuals, albeit they were more satisfied with their performance. Similarly, Arisholm et al. (2007) found pair programming neither resulted in more correct solutions nor reduced the time required to solve programming problems compared to programmers working alone. A recent and more rigorous study on pair programming, accounting more precisely for the impact of collaboration, reported that collaborating pairs outperform the second-best members of nominal pairs but perform at the same level as the best-members of nominal pairs (Balijepally et al. 2009). Table 2 summarizes recent empirical studies in paired software development.

As Table 2 shows, there is a limited body of empirical research on the issue of design in the context of agile software development. This is also reiterated in a recent review of the literature on empirical studies involving pair programming (Salleh et al. 2011). Neither of the two pair design studies listed in Table 2 addresses the complexities of a software design task. While the study by Lui et al. (2008) was confined to algorithmic design, Canfora et al. (2007) examined the efficacy of pair designing in the context of a software maintenance task. Further, as discussed earlier, these studies share a critical methodological limitation arising out of comparing the performance of collaborating pairs with that of an equal number of individuals, thus giving the pairs a numerical advantage over the individuals.

Our study attempts to satisfy the urgent need to research pair designing using a design-centric task while overcoming the methodological pitfalls of prior research. Of greater importance, the nature of the design task in our study clearly distinguishes it from prior research. As the following section shows, task type can be a major determinant of team processes and outcomes.

## Task Typology and Pair Designing

Scholars in the enduring tradition of small-groups research have long established the critical role that task type plays in influencing team processes (McGrath 1984; Steiner 1972). While it is true that groups tend to do better than average individuals, they seldom do better than the best individuals, particularly on tasks whose solutions are neither easily identifiable nor verifiable (Hill 1982; Laughlin et al. 2002). As Straus (1999, p. 170) affirms, “the nature of the group’s task is a particularly powerful input factor that affects the group interaction process.” Indeed, the systematic classification of tasks (i.e., typologies) by researchers in group behavior and management (Campbell 1988; Hackman 1968; McGrath 1984; Steiner 1972) provided the conceptual foundation for the articulation of a theory of task/technology fit and group support systems (Zigurs and Buckland 1998).

Tasks may be unitary (i.e., cannot be easily divided among team members) or divisible, disjunctive (any member can complete the task) or conjunctive (every member must complete an aspect of the task), maximizing (focus on quantity of output) or optimizing (emphasize quality of solution), and intellective (having verifiable solutions that enable the group to easily reach an agreement) or judgmental (correctness of the solution cannot be indisputably ascertained) (Laughlin et al. 2002; Steiner 1972). McGrath’s (1984) depiction of task types in the form of a “circumplex” clearly illustrates the cognitive and behavioral demands that the nature of the task imposes on problem solvers. It is also apparent from the taxonomy that the extent of communication, coordination, and conflict resolution required varies with the type of task, with judgmental tasks being far more demanding than intellective tasks.

<table><tr><td colspan="4">Table 2. Empirical Studies in Paired Software Development</td></tr><tr><td>Research Study</td><td>Context</td><td>Experimental Task</td><td>Findings/Comments</td></tr><tr><td>Nosek (1998)</td><td>Pair programming</td><td>Implementation of scripts in C.</td><td>Compared with individuals, pairs performed better, relished the problem-solving process to a greater extent, and had higher confidence in their solutions. However, there was no significant difference between pairs and individuals with regard to the time to complete the task.</td></tr><tr><td>Williams et al. (2000)</td><td>Pair programming</td><td>Programming assignments.</td><td>Pairs produced higher quality programs, took less time, and were more satisfied than individuals. However, these differences were not tested for statistical significance.</td></tr><tr><td>Müller (2005)</td><td>Pair programming</td><td>Coding and testing of programs.</td><td>For similar levels of program correctness, there is no difference between the cost of pair programming and the total cost of individual programming followed by a peer review phase.</td></tr><tr><td>Lui and Chan (2006)</td><td>Pair programming</td><td>Same program was written multiple times by the subjects.</td><td>Individuals took more time than pairs to complete the task, but the difference was not tested for statistical significance.</td></tr><tr><td>Arisholm et al.(2007)</td><td>Pair programming</td><td>Maintenance changes to existing programs. Two tasks of varying complexity were used.</td><td>There was no support for the hypotheses that pairs, when compared with individuals, require less time to solve the tasks correctly, or produce a higher proportion of correct solutions.</td></tr><tr><td>Müller (2007)</td><td>Pair programming</td><td>Implementation and testing of Java programs.</td><td>Pairs made as many algorithmic mistakes, but fewer expression mistakes, than programmers working individually.</td></tr><tr><td>Domino et al.(2007)</td><td>Pair programming in both face-to-face and virtual settings</td><td>Writing test cases and pseudocode.</td><td>Pairs who collaborated while writing the test cases and the pseudocode performed poorly when compared with individuals or pairs who collaborated only during the writing of the pseudocode. Pairs who collaborated face-to-face were more satisfied than individuals/pairs in other experimental conditions.</td></tr><tr><td>Balijepally et al.(2009)</td><td>Pair programming</td><td>Modification of existing program snippets.</td><td>Pairs outperformed the second-best members of nominal pairs in terms of solution quality. Further, pairs had greater confidence in their solution, and exhibited higher task satisfaction than individuals.</td></tr><tr><td>Müller (2006)</td><td>Pair designing followed by pair programming</td><td>Design and implementation of a scheduling algorithm for an elevator system.</td><td>Study focused on costs; there was no investigation of the efficacy of pairs vis-à-vis individuals in the context of software design.</td></tr><tr><td>Canfora et al.(2007)</td><td>Pair designing</td><td>Maintenance requests that required changes to existing use cases and class diagrams.</td><td>Pairs outperformed individuals in terms of solution quality but there was no difference in the effort expended.</td></tr><tr><td>Lui et al. (2008)</td><td>Algorithm design in pairs</td><td>Programming aptitude tests as a surrogate for program design.</td><td>Pairs outperformed individuals in terms of time required for task completion. However, the term “design” referred to “algorithmic design” rather than the design of a software system from specifications.</td></tr></table>

Contrary to programming, design tasks are more abstruse, often lack structure, and have myriad alternative solutions that are hard to assess for quality and efficacy (Guindon 1990). Further, the trade-offs between alternative solutions may not be readily apparent, making it very difficult for a designer to convince others of the superiority of one design solution over another. Consider the following questions with which software designers are often confronted: Do we use inheritance or composition? Should we use an abstract class or an interface? Do we sacrifice extensibility for reusability? Should we sacrifice speed for flexibility? It is apparent from this sampling of questions that it is extraordinarily difficult to objectively establish the correctness of a software design solution, thus making it much harder for team members to reach an agreement. Conflicting viewpoints and perspectives have to be reconciled to facilitate a consensus. Therefore, design tasks are more judgmental than programming tasks, and groups engaged in such tasks are likely to experience more process losses than those working on programming problems.

One of the aims of our study is to investigate if the findings of pair programming studies hold up to scrutiny when the task type is significantly different. Such an examination is absolutely necessary for us to establish empirical regularity of our findings with regard to pairs and individuals, which, in turn, is essential for developing a theoretical framework of paired software development.

## Distributed Cognition in Software Design

The following gaps in the literature are apparent from our earlier discussion:

(1) There is little empirical research on the efficacy of pairs versus individuals on design-centric tasks.

(2) Rigorous empirical work on design patterns is not only limited, but also the inconsistent findings in the extant literature offer inadequate guidance to academics and practitioners. In addition, these studies provide no insight into the viability of patterns in a real design context.

(3) To the best of our knowledge, there exists no designcentric study that empirically examines the performance of cognitive systems resulting from the interactions among social actors and external artifacts in a problem solving environment.

In order to fill these gaps, our research relies on the conceptual underpinnings of distributed cognition to study the performance of pairs versus individuals in the presence or absence of an external cognitive artifact. We considered two levels of socially distributed cognition operationalized through subjects working individually or as collaborating pairs, and two levels of structurally distributed cognition instantiated through the presence or absence of design patterns. Their combination resulted in four distinct cognitive architectures, namely, simple-social, simple-individual, complex-social, and complex-individual. Figure 2 illustrates these four cognitive architectures.

The simple-social cognitive system is instantiated through a collaborating pair that does not have access to design patterns. In the simple-individual cognitive system a subject works independently on a design task unaided by an external cognitive artifact (i.e., without patterns). The complex-social cognitive system emerges from the interaction between a collaborating pair and design patterns. Finally, the complexindividual cognitive system is operationalized through an individual working independently with access to design patterns.

From a theoretical perspective, the cognitive processes associated with these four configurations are likely to be different and, therefore, we expect variations in their performance as well. The following section discusses the research model and the hypotheses of interest.

## Research Model

Figure 3 presents the research model used in this study. The dependent variables are solution quality, task completion time, and task satisfaction. The choice of these variables is consistent with Aladwani’s (2002) contention that information systems development performance is multidimensional and must include both task oriented and psychological outcomes. Task oriented outcomes emphasize effectiveness (e.g., quality) and efficiency (e.g., completion time) of completing a task, while psychological outcomes measure the developer’s feelings in performing the task (e.g., task satisfaction).

## Impact of Design Patterns on Software Quality and Completion Time

The theory of distributed cognition suggests that artifacts, whether they are outcomes of the design process or those that are part of the design environment, are external representational media that can interact with mental processes of designers to confer unique cognitive properties (Flor and Hutchins 1991). In our study, external cognitive artifacts in the form of design patterns containing information relevant to the design problem were made available to some pairs and individuals. Aside from providing the palpable benefit of enabling recall of knowledge pertinent to the problem, such artifacts have the potential to define and lend clarity to an otherwise ill-structured design problem. Further, they can facilitate shared representations, evoke schemas and conceptual operators germane to the design under consideration, and lead to greater team collaboration and reflexivity (Rosen et al. 2009; Shirouzu et al. 2002; Zhang and Norman 1994). Thus, they can benefit both individuals and pairs. In particular, pairs assisted by external artifacts (i.e., design patterns) can more easily resolve design conflicts, integrate diverse viewpoints, and induce a mutually agreeable solution.

![](/api/attachments/CA7C7XT9/fulltext/images/d063616dbd4e646dd6b7018e5087d91f5ba81cf0bdb475fe0000dd3e2a74bb87.jpg)

According to Simon (1973), the crux of problem solving is to find appropriate information to transform an ill-defined problem into a well-structured one to facilitate its easy solution. Design patterns may be viewed as external representations that have the potential to constrain search, to structure the problem, and facilitate a quicker and better solution. As Gamma et al. (1995, p. 2) note, “put simply, design patterns help a designer get a design right, faster.” Further, they extend the cognitive system beyond the internal model of the designer and may trigger schemas that might be useful in developing a high quality solution to a design problem (e.g., Kohls and Scheiter 2008; Robillard 1999). This has also been corroborated by Batra’s (2005) argument that design patterns not only enhance the search for correct operators, but also stimulate existing operators in novel ways.

Based on these arguments, we predict

$\mathbf { H } _ { 1 } \mathbf { \cdot }$ Quality of the design solution will be higher when design patterns are used during software design.

H<sub>2</sub>: Time taken to complete a design task will be shorter when design patterns are used.

## Impact of Pair Designing on Software Quality

In our study, a pair working without the assistance of design patterns constitutes a simple-social system. According to the distributed cognition perspective, a distinctive cognitive system emerges from the informational transactions among members of the pair and any artifacts that they might create while solving a problem. The cognitive performance of such a system is largely an outcome of collective action engendered by patterns of interactions among the internal cognitive processes of the two members and their evolving design solutions. The individuals may not only bring unique knowledge and experience to bear on the problem, but are also likely to benefit from their complementary skills.

While distributed cognition theory argues for the many advantages that accrue from cognition that is socially distributed, the extensive research in the small groups area has demonstrated that group synergies are often hindered by process losses, particularly on tasks that are judgmental. These losses usually stem from social loafing (Karau and Williams 2001) and inadequate communication and coordination (Steiner 1972). As discussed before, design tasks are clearly farther along the intellective–judgmental continuum, exhibiting all of the characteristics (e.g., ambiguity of requirements, large solution space, no verifiable solution, etc.) that have traditionally been believed to hamper group processes. Therefore, pairs performing such a design task are likely to suffer process losses, as a result of which actual solution quality may fall short of expectations.

The aforementioned arguments are consistent with findings in the group literature that groups working on judgmental tasks tend to perform better than second-best individuals but rarely outperform best individuals (Hill 1982; Laughlin et al. 2006). Therefore, we hypothesize

$\mathbf { H } _ { 3 } { \mathrm { : } }$ Solution quality of a collaborating pair will be higher than that of the second-best member of a nominal pair in a software design task.

## Impact of Pair Designing on Task Completion Time

As discussed earlier, a design task is unitary, judgmental, and lacks demonstrability. Small-group research has found that groups take longer than individuals while working on unitary tasks (Hare 1976), that is, tasks that cannot be further subdivided among group members (Steiner 1972). The additional time taken by groups has been attributed to error checking (Hare 1976); time spent in communicating and resolving conflicts among team members (Brodbeck and Greitemeyer 2000); presentation, discussion, rejection, and acceptance of a large number of possible answers (Klugman 1944); and time needed to reach a collective decision (Brodbeck and Greitemeyer 2000). Pairs working on a software design task that is not easily divisible must develop a single solution representing their collective decision. Further, the lack of demonstrability of software design solutions is likely to increase the time required to reconcile design alternatives. In a similar vein, Canfora et al. (2007) found that pairs took more time than individuals to complete a design task in the context of software maintenance.

Consequently, we expect the collaborating pair to take more time to complete a design task vis-à-vis individuals. Hence, we predict

$\mathbf { H } _ { 4 \mathbf { a } } \mathbf { : }$ Time taken by collaborating pairs to complete a software design task will be longer than that of the best member of a nominal pair.

${ \bf { H } } _ { 4 \mathrm { { b } } } { \mathrm { { . } } }$ Time taken by collaborating pairs to complete a software design task will be longer than that of the second-best member of a nominal pair.

## Differential Gains from Structurally Distributed Cognition

The literature on distributed cognition suggests that external representational media, particularly those that have taskrelevant information, can enhance problem solving performance (Flor and Hutchins 1991; Zhang and Norman 1994). The availability of design patterns to pairs can lead to more effective collaboration due to enhanced communication, improved shared understanding, and expedited resolution of design conflicts (Rosen et al. 2009; Shirouzu et al. 2002). Therefore, a complex-social cognitive system comprising pairs and design patterns would have fewer process losses and higher software quality vis-à-vis a simple-social cognitive system. Likewise, the presence of external cognitive artifacts confers certain benefits on a complex-individual cognitive system. Specifically, the availability of design patterns can evoke relevant knowledge structures and schemas that can lend structure to the problem and lead to a better solution visà-vis a simple-individual cognitive system (Kohls and Scheiter 2008). In both cases, the external artifact injects additional knowledge into the cognitive system. Given that both pairs and individuals benefit from the availability of design patterns, the question that arises is: Do individuals and pairs benefit equally from the availability of design patterns? If, however, there is a differential benefit to individuals, would the recipient of this benefit be the individual with the lowest skills (i.e., the second-best member when compared to the best member of a nominal pair)? Examining these questions has theoretical implications centered on the extent that design patterns represent a unique source of “expertise.”

We expect design patterns to provide differential benefits to the best member, the second-best member, and the pair. The best member of a nominal pair has a high level of expertise and competence. A team of paired designers, by virtue of having two persons in the team, has access to additional knowledge, skill, and expertise of the second member of the team. Thus, the expertise encoded in design patterns may be somewhat redundant with that already available to the best individual and the pair, and represents more new information for the second-best member. We, therefore, expect the second-best member to benefit most by this new information and help him/her close the performance gap with the best member and the pair. Hence, we hypothesize

${ \mathbf { H } } _ { 5 { \mathrm { a } } ^ { \cdot } }$ When design patterns are available, the performance gap in solution quality between the secondbest member of a nominal pair and the best member of the nominal pair and the pair will be reduced in contrast to when design patterns are not used.

A related question in this regard is whether the availability of design patterns enables the second-best members of nominal pairs to outperform collaborating pairs that do not have access to patterns. To the best of our knowledge, studies in the distributed cognition area have not compared a socially distributed cognitive system (i.e., pairs) with a structurally distributed cognitive system (i.e., an individual interacting with an external cognitive artifact).

A design pattern provides the second-best member with a compensatory type of expertise when compared with the pair without access to design patterns. Socially distributed cognitive systems allow for emergent group properties that may lead to superior or inferior group performance contingent upon the distribution of information across the group member. In an experiment involving an intellective task, Zhang (1998)

found that an individual with task-related information performed better than a pair that collectively had the necessary information to solve the problem. Apparently, group process losses precluded the pair from effectively sharing all of the information held by its members. Since design tasks are judgmental, we expect pair designers working without design patterns to experience even greater process losses. Therefore, we hypothesize

${ \bf { H } } _ { \mathbf { 5 } \mathbf { b } } { \mathrm { : } }$ Solution quality of the second-best member of a nominal pair with design patterns will be higher than that of the collaborating pair without design patterns in a software design task.

The second index of performance under examination is task completion time. As discussed earlier, the small group literature and research on paired designing suggest that groups/ pairs take more time to arrive at a solution than individuals. Further, Zhang’s study on distributed cognition showed that an individual with access to all task-related information took less time to complete a task than did a pair whose members collectively had all the information to solve the problem. Therefore, we predict that

$\mathbf { H } _ { 5 \mathrm { c } } \mathrm { : }$ Task completion time of the second-best member of a nominal pair with design patterns will be lower than that of the collaborating pairs without design patterns in a software design task.

## Impact of Design Patterns on Software Developers’ Task Satisfaction

Task satisfaction is an important aspect of software development, as has been highlighted in the information systems literature (Aladwani 2002). It has been found to directly influence organizational citizenship behavior and reduce absenteeism (Mason and Griffin 2005). From the perspective of distributed cognition, cognitive artifacts such as design patterns reduce the complexity of design tasks by serving as memory aids and by constraining the search process. Lower task complexity is generally associated with higher confidence in the solution across a variety of tasks (Carey and Kacmar 1997). Design patterns embody design expertise and, therefore, enhance the developer’s confidence in the resulting solution. Small and Venkatesh (2000) argue that higher levels of confidence are associated with increased levels of satisfaction. Therefore, we predict

$\mathbf { H } _ { 6 } \mathbf { \cdot }$ Task satisfaction will be higher when design patterns are used in a software design task.

## Impact of Pair Designing on Task Satisfaction

Small group research has reported that individuals working in groups are typically more satisfied when compared with those working alone. These findings have been documented across different types of tasks (Park and Hinsz 2006). For example, Hinsz and Nickell (2004) found that groups are more satisfied than individuals on goal setting tasks. Similar findings were also reported in the context of brainstorming tasks (Nijstad et al. 2006). Consistent with these findings, pairs working on programming tasks have been found to exhibit higher levels of task satisfaction than individuals working alone (Cockburn and Williams 2001; Nosek 1998).

There are several explanations for higher levels of satisfaction among group members. Paulus et al. (1993) attributes this to a social comparison process in which groups perceive their performance more favorably when compared with individuals working alone. Another line of reasoning is that groups are more satisfied because of the perceived “safety in numbers” during task performance (Park and Hinsz 2006). Shaw et al. (2000) argue that higher task interdependence is associated with higher team member satisfaction. Task interdependence is enhanced when team members work collaboratively to accomplish the group’s objective. Since software design is characterized by a high level of task interdependence, we predict

H : The average level of task satisfaction among collaborating pairs will be higher when compared with the average level of task satisfaction of nominal pairs.

The research method is described in the next section.

## Research Method

## Research Design and Participants

Since our study aims to gain insight into relative performance of four different cognitive systems described earlier, a 2 (design patterns) × 2 (mode of participation) factorial experimental design (see Figure 4) was deemed to be appropriate. In addition to capturing the four systems elegantly, this design provides useful information about the potential interactions that can occur among the four architectures. There were two levels of structural cognition, operationalized through presence or absence of design patterns, and two levels of social cognition, implemented by mode of participation— collaborating pairs versus individuals who worked alone but were randomly combined to form nominal pairs.

A total of 100 participants volunteered for this experiment. Participants were software development professionals recruited from organizations located in a metropolitan area in the United States. Approximately 95 percent of the participants had more than a year of programming experience, but none reported using design patterns at work prior to the experiment. As an incentive to volunteer for this research, all participants were offered a seminar on design patterns sponsored by an academic unit of a large university. Subjects who were aided by design patterns attended the seminar prior to the experiment, whereas others participated in the seminar after completing the experiment. Four data points were excluded from further analysis because of incomplete information. Participants who worked in the individual condition were randomly assigned to nominal pairs. This resulted in 24 participants per cell comprising either 12 collaborating or 12 nominal pairs.

## Procedures

The experiment was conducted in a behavioral research laboratory equipped with rooms that allow subjects to work on their assigned tasks without external interference. Each experimental session was two hours in duration. Upon reporting to the laboratory, all participants were briefed on the study procedures. Following the briefing, subjects were randomly assigned to different experimental conditions. Each pair/individual was assigned to one of the rooms in the behavioral lab for the entire duration of the experiment. After completing the tasks, participants filled out a questionnaire that was designed to gather information related to participant demographics, the dependent variable of satisfaction, and the success of the experimental manipulation check (see Appendix B).

## Pilot Test

A pilot test was conducted prior to the main experiment to verify the experimental protocol. A total of 15 subjects participated in this study. Based on the feedback received from the participants, minor modifications were made to the scripts and materials used in the experiment and to the time allocated for the experimental tasks.

## Manipulation of Independent Variables

## Design Patterns

Prior to the experiment, participants in the pattern condition attended a seminar on design patterns. This three-hour seminar provided the participants an overview of the 23 patterns discussed by Gamma et al. (1995). Care was taken to ensure that the problems and examples discussed in the seminar were unrelated to the software design task used in this study. When the experiment commenced, participants in the pattern condition were provided documentation on four design patterns, namely, Adapter, Memento, Observer, and Strategy (see Gamma et al. for a description of these patterns). Of these, the strategy pattern was relevant to the warm-up task, and the other three were potentially helpful in addressing the design constraints of the main task. The documentation, however, did not offer any clue regarding the usefulness of these patterns in solving the experimental problems.

<table><tr><td rowspan="3" colspan="2"></td><td colspan="2">Level of Structurally Distributed Cognition</td></tr><tr><td>Low</td><td>High</td></tr><tr><td>No Patterns</td><td>Patterns</td></tr><tr><td rowspan="2">Level of Socially Distributed Cognition Absent Present</td><td>Individuals</td><td>Simple-Individualn = 2211 nominal pairs</td><td>Complex-Individualn = 2412 nominal pairs</td></tr><tr><td>Pairs</td><td>Simple-Socialn = 2211 collaborating pairs</td><td>Complex-Socialn = 2412 collaborating pairs</td></tr></table>

Figure 4. Two-by-Two Factorial Research Design

## Collaborating and Nominal Pairs

Participants working in pairs were instructed to actively collaborate with each other and to arrive at a consensual solution to the software design problem. Further, they were assured that the cubicles were insulated and that they could interact freely without disturbing others. All participants, including those working individually, were told to strive for the best solution. Subjects were provided breaks in a staggered manner, so that there would be no interaction among participants across treatments.

## Experimental Tasks

Appendix C describes the two experimental tasks that all participants completed. The first task, the Duck Simulation

Game, was used as a warm-up task, while the Weather Monitoring problem was used as the main experimental task. The warm-up task required the design of a gaming system that simulated the behaviors of different types of ducks. The main task involved the conceptual design of a weather monitoring station that interfaced with different types of sensors. These two tasks were adapted from sample problems available in systems design books (Freeman et al. 2004; Richter 1999a). The deliverable for each task was a class diagram using the UML (unified modeling language) notation. The warm-up task lasted for 20 minutes and provided an opportunity for the participants in the pattern condition to become familiar with the use of patterns. It also gave participants in the pair condition an opportunity to familiarize themselves with their work partners. All subjects were provided with a glossary of UML class diagramming notations and were also briefed on their use.

## Measurement of Variables

## Solution Quality

Based on the guidelines offered by prior research, a scoring scheme was formulated to assess performance on the experimental task. Rehder et al. (1997) describes an approach to evaluate the quality of a design by decomposing it into a set of atomic design features. Purao et al. (2003) developed a coding scheme that accounts for errors due to omission (Type I error) and commission (Type II error). Following these guidelines, the experimental task was decomposed into elementary classes and their relationships/associations. Solution quality was judged according to how well designs produced by subjects met the expected standards. In addition, bonus points were awarded when the solution included design alternatives and/or features that exceeded the standard solution. On the other hand, outcomes with unwanted classes and/or associations received penalty points. Appendix D presents the grading scheme adopted to evaluate the solutions. Class names shown in the grading scheme are for illustration only. Thus, the evaluation was based on the purpose rather than the specific names of the classes.

Two Ph.D. students with prior experience in object-oriented analysis and design served as judges of the solutions. They were trained to evaluate the solutions using the scoring scheme outlined in Appendix D. They were blind to the experimental conditions of the participants. Each judge independently assessed all solutions. In 19 out of 72 cases, the final scores assigned by the two raters differed by more than 10 points. In these cases, the raters resolved their differences through discussion. The resultant scores were assessed for intra-class correlation (ICC), a measure of inter-rater reliability of quantitative scores. Since two raters were used to assess the quality of solution, we utilized a two-way mixed effects model to check rater consistency (McGraw and Wong 1996). The average measure ICC was 0.97, (F = 36.67, p < 0.001). Consequently, the average of the two scores was used as the score for solution quality in the subsequent analysis.

## Task Completion Time

Subjects were allowed to determine when their tasks had been completed (Dyba et al. 2007) to allow for differences in the time needed to complete the tasks. The average time for task completion was 57.87 minutes with a standard deviation of 16.49 minutes. Consequently, the maximum allotted time of 80 minutes for this part of the experiment appeared adequate for all participants to complete their tasks.

## Task Satisfaction

Task satisfaction assessed the overall affective feelings of the participants toward the software development task. Participants responded to four items asking them how very dissatisfied (1) to very satisfied (7), very displeased (1) to very pleased (7), very frustrated (1) to very contented (7), and very terrible (1) to very delighted (7) they felt about the task they just completed. This scale was based on an existing task satisfaction measure (Balijepally et al. 2009). Estimated reliability of the four item scale of task satisfaction was alpha = 0.89. According to Nunnally (1978), reliabilities exceeding 0.70 are considered to be acceptable.

## Control Variables

A number of individual difference variables such as education level and experience in software development can influence task performance (Darcy et al. 2005). In order to specifically control for these types of extraneous influences, we first individually considered educational level, years of programming experience, years of object-oriented programming experience, and years of object-oriented design experience as potential covariates. Using multivariate analysis of covariance (MANCOVA), only object-oriented programming experience (p = 0.001) and design experience (p = 0.02) were found to significantly influence task performance variables (i.e., solution quality and task completion time). When both of these potential covariates were simultaneously considered, only object-oriented (OO) programming experience (p = 0.034), but not design experience $( \mathtt { p } = 0 . 4 9 )$ , was found to significantly influence task performance. Subsequent correlational analysis revealed that OO programming experience and OO design experience were highly correlated among the study participants (r = 0.56, p < 0.001). Hence, it was decided to include OO programming experience as the covariate for subsequent analysis.

## Manipulation Checks

Use of Design Patterns: During the debriefing session following the experiment, the participants were asked if they had used one or more design patterns in their solutions. Subsequently, their solutions were checked to verify if they had actually used patterns. Of the participants in the pattern condition, 92 percent were found to have used design patterns in their solutions. Consequently, providing participants with patterns had the intended impact of encouraging their use when performing the experimental task. As mentioned earlier, patterns are abstract and difficult to understand and use. The fact that a large percentage of subjects in the pattern condition were able to identify and use the patterns suggests that our manipulation was effective. In the no-pattern condition, one individual and a collaborating pair reported and used design patterns in formulating their solution. Experimental data were analyzed with and without these two observations and no significant difference was found. However, in reporting the results of the data, these two data points were excluded. Hence, the final sample included 12 collaborating and 12 nominal pairs in the pattern condition and 11 collaborating and 11 nominal pairs in the no-pattern condition.

Mode of Participation: Subjects in the pair condition were asked to indicate the extent to which they agreed with the statement that their partners were actively engaged in solving the design problem using a scale from strongly disagree (1) to strongly agree (7). Descriptive statistics indicated a high degree of active participation $( \mathrm { M } = 6 . 2 8 , \mathrm { S D } = 0 . 8 9 )$ . Additionally, none of the paired participants reported a level of participation of 4 (neutral point on the scale) or lower. Therefore, it appears that pairs actively collaborated in solving the design problem.

## Results

## Sample Characteristics

Table 3 describes the demographic characteristics of the participants. Analyses were performed to ensure that there is no systematic variation in the characteristics of subjects across the four treatment conditions. Results of the analysis of variance (ANOVA) tests of self-reported educational level $( \mathrm { F } = 0 . 2 6 ; \mathrm { p } = 0 . 8 9 )$ , programming experience $( \mathrm { F } = 0 . 6 1 ; \mathrm { p } =$ 0.61), object-oriented programming experience (F = 0.41; p = 0.75), and object-oriented design experience (F = 0.36; p = 0.78) did not indicate significant differences across the four experimental conditions. Table 4 presents the descriptive statistics and correlation statistics of the dependent variables.

## Methods of Analysis

Hypotheses 1, 2, 3, 4 , and $4 _ { \mathrm { b } } ,$ describing the expected impact of design patterns and paring on the response measures of solution quality and task completion time were tested using MANCOVA procedures in a 2 (design pattern versus no design pattern) × 3 (collaborating pair versus best member of the nominal pair versus second-best member of the nominal pair) factorial design. Since the MANCOVA test indicated a significant effect, univariate analyses using ANCOVA procedures were followed (Hair et al. 1998, p. 355). Hypotheses $5 _ { \mathrm { a } } ,$ ${ \mathsf { S } } _ { \mathrm { b } } ,$ and $5 _ { \mathrm { c } }$ were tested through planned comparison procedures using one-way ANCOVA analysis (Neter et al. 1996). Hypotheses 6 and 7 describe the expected impact of design patterns and pairing on task satisfaction. These were examined using ANCOVA procedures in a 2 (design pattern versus no design pattern) $\times 2$ (collaborating pair versus nominal pair) factorial design. When appropriate, Bonferroni’s procedures were then used to examine significant differences between pairs of treatment means (Neter et al. 1996).

Statistical tests were conducted to ensure that the underlying assumptions of MANCOVA/ANCOVA were met. For MANCOVA, following assumption checks were performed. Equality of variance–covariance matrices were assessed by

Box’s M (19.2, p = 0.282). Neter et al. (1996) suggest that randomization of subjects in a study is the most important protection against the violation of independence of error terms. This study randomly assigned subjects to various experimental conditions; hence, there may not be a violation of the assumption of independent error terms. Multivariate normality was assessed and found satisfied through Bartlett’s test of sphericity (Chi-squared = 11.93, p = 0.003).

The ANCOVA model’s assumptions were checked next. The assumption regarding constancy of error terms was tested using the modified Levene test and the results indicated that there were no violations of this assumption for any of the dependent variables. Normality of error terms was checked using omnibus normality tests. Results indicated that the task satisfaction variable alone had violations of normality assumptions $( \mathrm { t } = 9 . 2 6 , \mathrm { p } = 0 . 0 1 )$ . According to Neter et al., lack of normality is not a major concern for fixed ANOVA/ ANCOVA models, and Kurtosis of error distribution is more important than skewness in terms of effects on inference. Further analysis revealed that task satisfaction variable did not violate Kurtosis at alpha of 0.05. The test for the assumption of equality of treatment slopes was conducted for the covariate “experience with object-oriented programming.” An F-test was conducted to test the equality of slopes across the treatment conditions as specified by Neter et al. The equality of slopes assumptions could not be rejected at an alpha level of 0.05. As suggested by Neter et al., assumptions regarding linearity of regression relation were checked using the residual plot, which indicated no departure from a linear relationship. Overall, these tests indicated that there was no violation of assumptions, thus allowing us to proceed with hypothesis testing using ANCOVA.

## Hypothesis Testing for Performance Measures

MANCOVA test indicated that the mode of participation had a significant influence on task performance (Wilk’s Lambda $= 0 . 6 8 , \mathrm { F } = 6 . 4 6 , \mathrm { p } < 0 . 0 0 1 )$ . Similarly, the use of design patterns had a significant influence on task performance (Wilk’s Lambda = 0.67, F = 14.94, p < 0.001). There was no significant interaction between mode of participation and design patterns on task performance (Wilk’s Lambda = 0.98, $\mathrm { F } = 0 . 2 9 , \mathrm { p } = 0 . 8 9 )$ . Object-oriented programming experience, which was used as a covariate, also had a significant effect on task performance (Wilk’s Lambda = 0.80, F = 7.63, $\mathsf { p } = 0 . 0 0 1 $ . Due to the significant MANCOVA results, ANCOVA procedures were used to test the individual hypotheses pertaining to solution quality and task completion time. The following sections discuss these findings.

<table><tr><td>Demographic Variables</td><td>Category</td><td>Frequency (Percentage)</td><td>Demographic Variables</td><td>Category</td><td>Frequency (Percentage)</td></tr><tr><td rowspan="5">Gender</td><td>Male</td><td>81 (88%)</td><td rowspan="5">Programming Experience</td><td>0-1 years</td><td>4 (4 %)</td></tr><tr><td>Female</td><td>11 (12%)</td><td>1-2 years</td><td>4 (4 %)</td></tr><tr><td></td><td></td><td>2-4 years</td><td>15 (16 %)</td></tr><tr><td></td><td></td><td>4-6 years</td><td>27 (29 %)</td></tr><tr><td></td><td></td><td>6 &lt; years</td><td>42 (46 %)</td></tr><tr><td rowspan="7">Age</td><td>&lt; 25</td><td>14 (15 %)</td><td>OO</td><td>0-1 years</td><td>11 (12 %)</td></tr><tr><td>26 – 30</td><td>32 (35%)</td><td rowspan="6">Programming Experience</td><td>1-2 years</td><td>17 (18 %)</td></tr><tr><td>31 – 35</td><td>23 (25 %)</td><td>2-4 years</td><td>33 (36 %)</td></tr><tr><td>36 – 40</td><td>8 (9 %)</td><td>4-6 years</td><td>14 (15 %)</td></tr><tr><td>41 – 45</td><td>7 (8 %)</td><td>6 &lt; years</td><td>16 (17 %)</td></tr><tr><td>46 &lt;</td><td>6 (7 %)</td><td>Did not provide</td><td>1 (1 %)</td></tr><tr><td>Did not provide</td><td>2 (2 %)</td><td></td><td></td></tr><tr><td rowspan="6">Education</td><td>High school</td><td>2 (2 %)</td><td rowspan="6">OO Design Experience</td><td>No experience</td><td>2 (2 %)</td></tr><tr><td>Community college</td><td>6 (7 %)</td><td>Novice</td><td>23 (25 %)</td></tr><tr><td>Undergraduate degree</td><td>27 (29 %)</td><td>Intermediate</td><td>60 (65 %)</td></tr><tr><td>Graduate degree</td><td>54 (59 %)</td><td>Expert</td><td>7 (8 %)</td></tr><tr><td>Doctoral degree</td><td>1 (1 %)</td><td></td><td></td></tr><tr><td>Did not provide</td><td>2 (2 %)</td><td></td><td></td></tr></table>

<table><tr><td colspan="7">Table 4. Dependent Variables</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="3">Correlation</td></tr><tr><td>Variable</td><td>Mean</td><td>Standard Deviation</td><td>Reliability</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1. Solution Quality</td><td>38.67</td><td>14.15</td><td> $0.97^a$ </td><td>na</td><td></td><td></td></tr><tr><td>2. Task Completion Time</td><td>57.87</td><td>16.59</td><td></td><td>0.21*</td><td>na</td><td></td></tr><tr><td>3. Task Satisfaction</td><td>5.11</td><td>1.25</td><td> $0.89_b$ </td><td>0.27*</td><td>0.04</td><td>na</td></tr></table>

Notes: <sup>a</sup>Intraclass correlation (ICC)  
<sup>b</sup>Cronbach’s alpha  
\*correlation significant at the 0.05 level

## Solution Quality

Hypothesis $\mathrm { H } _ { \mathrm { l } }$ predicted that solution quality will be higher when design patterns are available, and Hypothesis $\mathrm { H } _ { 3 }$ predicted that solution quality for paired designers will be higher than that of the second-best members of nominal pairs. The results of testing these hypotheses using ANCOVA procedures with experience in object-oriented programming as a covariate are presented in Table 5. The treatment mean plots are shown in Figure 5.

These results demonstrate significant main effects of design patterns $( \mathrm { F } ( 1 , 6 2 ) = 1 8 . 1 4 , \mathrm { p } < 0 . 0 0 1 )$ , and mode of participation (F $( 2 , 6 2 ) = 9 . 6 3 , \mathrm { p } < 0 . 0 0 1 )$ on solution quality. Consistent with H solution quality was higher when design patterns were available (M = 43.72) than when they were not (M = 31.52). Since the main effect for mode of participation was significant and the contrast of interest was specified in advance, Bonferroni’s procedures were used to examine which pair of means differed significantly (Neter et al. 1996). Solution quality of pairs (M = 40.40) was significantly higher (p < 0.001) than that of the second-best individuals in nominal pairs (M = 29.12), thus supporting $\mathrm { H } _ { 3 } .$ Further analysis also revealed that the collaborating pair’s performance did not significantly differ (p = 0.38) from that of the best member of the nominal pair (M = 43.36), and the solution quality of the best member was significantly higher than that of the secondbest member (p < 0.001).

## Task Completion Time

Hypothesis H predicted that time to completion will be shorter when design patterns are used, while Hypothesis $\mathrm { H } _ { 4 \mathrm { a } }$ and $\mathrm { H } _ { 4 \mathrm { b } }$ predicted that time taken by collaborating pairs to complete a design task will be longer than those of the best and second-best members of nominal pairs. ANCOVA procedures were used in a 2 (design patterns versus no design patterns) × 3 (collaborating pair versus best member of nominal pair versus second-best member of nominal pair) design. Again, experience in object-oriented programming was used as a covariate. The results are presented in Table 6. Figure 6 presents the treatment means plot for this analysis.

<table><tr><td colspan="6">Table 5. ANCOVA Model Results for Solution Quality</td></tr><tr><td>Source</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F-ratio</td><td>p-value</td></tr><tr><td>OO Programming Experience</td><td>864.38</td><td>1</td><td>864.38</td><td>6.69</td><td>&lt;0.01</td></tr><tr><td>Mode of Participation</td><td>2488.27</td><td>2</td><td>1244.13</td><td>9.63</td><td>&lt;0.001</td></tr><tr><td>Design Pattern</td><td>2343.56</td><td>1</td><td>2343.56</td><td>18.14</td><td>&lt;0.001</td></tr><tr><td>Mode of Participation × Design Pattern</td><td>122.17</td><td>2</td><td>61.08</td><td>0.47</td><td>0.313</td></tr><tr><td>Error</td><td>8008.17</td><td>62</td><td>129.16</td><td></td><td></td></tr><tr><td>Corrected Total</td><td>14780.57</td><td>68</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/CA7C7XT9/fulltext/images/8e4579722d6c7aeaa6b93561a68e2277f9fa7dc685a62ace979ac06c3ef8f5cc.jpg)  
Figure 5. Means Plot for Solution Quality

The results indicate significant main effects of design patterns (F $( 1 , 6 2 ) = 4 . 0 6 , \mathtt { p } = 0 . 0 2 4 )$ and mode of participation $( \mathrm { ~ F ~ } ~ ( 2 , 6 2 ) ~ = ~ 7 . 2 8 , ~ \mathrm { ~ p ~ } < ~ 0 . 0 0 1 )$ on time to completion. Consistent with $\mathrm { H } _ { 2 } ,$ completion time was shorter when design patterns were available (M = 52.22) compared to when they were not available (M = 60.33). Collaborating pairs took significantly more time (M = 64.12) than the second-best members of nominal pairs $( \mathrm { M } { = } 4 6 . 5 4 , \mathrm { p } { < } 0 . 0 0 1 )$ to complete the task, but their completion time did not significantly differ $( \mathfrak { p } = 0 . 2 0 )$ from that of the best members of nominal pairs (M = 58.14). Thus, Hypothesis $\mathrm { H } _ { 4 \mathrm { b } }$ is supported but not $\mathrm { H } _ { 4 \mathrm { a } } .$

## Impact of Design Patterns and Pairing on Task Performance

Hypothesis $\mathrm { H } _ { \mathrm { 5 a } }$ predicts that the availability of design patterns will benefit the second-best member the most, thereby reducing the gap between the second-best member’s design quality and those of the best-member and the collaborating pair. As shown in Table 5, the results of ANCOVA did not indicate support for a significant interaction effect between design patterns and mode of participation. Separate planned comparisons using contrasts, as outlined by Neter et al., also did not provide support for $\mathrm { H } _ { \mathrm { 5 a } } .$ Overall, the results indicated that the use of design patterns did not provide any additional gain in design quality performance to the second-best member vis-à-vis the best-member and the collaborating pair.

Hypothesis $\mathrm { H } _ { 5 \mathrm { b } }$ predicts that second-best members aided by design patterns will produce design solutions of higher quality compared to those of collaborating pairs working without patterns. To test $\mathrm { H } _ { 5 \mathrm { b } } ,$ we performed planned comparisons of treatment means, as suggested by Neter et al.<sup>2</sup> Solution quality of second-best members of nominal pairs with design patterns $( \mathrm { M } = 3 6 . 8 1 )$ was not significantly $( \mathtt { p } = 0 . 4 2 )$ different from that of collaborating pairs without design patterns $( \mathbf { M } =$ 35.85). Thus, $\mathrm { H } _ { 5 \mathrm { b } }$ was not supported.

Table 6. ANCOVA Model Results for Task Completion Time

<table><tr><td>Source</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F-ratio</td><td>p-value</td></tr><tr><td>OO Programming Experience</td><td>993.47</td><td>1</td><td>993.47</td><td>4.12</td><td>0.023</td></tr><tr><td>Mode of Participation</td><td>3509.21</td><td>2</td><td>1754.61</td><td>7.28</td><td>&lt;0.001</td></tr><tr><td>Design Pattern</td><td>980.08</td><td>1</td><td>980.08</td><td>4.06</td><td>0.024</td></tr><tr><td>Mode of Participation × Design Pattern</td><td>103.34</td><td>2</td><td>51.67</td><td>0.21</td><td>0.404</td></tr><tr><td>Error</td><td>14949.12</td><td>62</td><td>241.11</td><td></td><td></td></tr><tr><td>Corrected Total</td><td>20042.29</td><td>68</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/CA7C7XT9/fulltext/images/97c4318a233ff38d03c532dbc99edcde90e6544e36de178efa3a0d72d5b983e2.jpg)  
Figure 6. Means Plot for Task Completion Time

Hypothesis $\mathrm { H } _ { 5 \mathrm { c } }$ predicts that second-best members with access to design patterns will take less time to complete the design task when compared with collaborating pairs working without patterns. The aforementioned planned comparison of treatment means showed that the task completion time of the second-best member utilizing design patterns (M = 43.83) was significantly lower $( \mathtt { p } < 0 . 0 1 )$ than that of a collaborating pair without design patterns (M=58.62), thus lending support to $\mathrm { H } _ { 5 \mathrm { c } } .$

## Task Satisfaction

Hypothesis $\mathrm { H } _ { 6 }$ proposes that task satisfaction will be higher when patterns are available, while Hypothesis $\mathrm { H } _ { 7 }$ predicts that collaborating pairs will experience higher satisfaction than nominal pairs. To examine these hypotheses, ANCOVA procedures were used in a 2 (design patterns versus no design patterns) $\times 2$ (collaborating pair versus nominal pair) design with experience in object-oriented programming as a covariate. Table 7 presents the results and Figure 7 shows the treatment means plot for this analysis.

The results indicate main effects of design patterns (F(1,41) = 4.68, p = 0.02) and mode of participation (F(1,41) = 1.90, ${ \tt p } = 0 . 0 9 )$ on the self-reported measure of task satisfaction. Consistent with ${ \mathrm { H } } _ { 6 } ,$ overall task satisfaction was higher when design patterns were available (M = 5.39) than when they were not (M = 4.81). Hypothesis H was supported at alpha = 0.1 level, as the overall task satisfaction of collaborating pairs (M = 5.35) was significantly higher than that of the nominal pairs (M = 4.86). Table 8 summarizes the results of this study.

Table 7. ANCOVA Model Results for Task Satisfaction

<table><tr><td>Source</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F-ratio</td><td>p-value</td></tr><tr><td>OO Programming Experience</td><td>2.08</td><td>1</td><td>2.08</td><td>2.35</td><td>0.07</td></tr><tr><td>Mode of Participation</td><td>1.68</td><td>1</td><td>1.68</td><td>1.90</td><td>0.09</td></tr><tr><td>Design Pattern</td><td>4.13</td><td>1</td><td>4.13</td><td>4.68</td><td>0.02</td></tr><tr><td>Mode of Participation × Design Pattern</td><td>0.36</td><td>1</td><td>0.36</td><td>0.41</td><td>0.23</td></tr><tr><td>Error</td><td>36.23</td><td>41</td><td>0.88</td><td></td><td></td></tr><tr><td>Corrected Total</td><td>45.62</td><td>45</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/CA7C7XT9/fulltext/images/b797f110eff9235d9f7dcf633bb91c2fc890e56106d7d5bd32353aa710dafda6.jpg)  
Figure 7. Means Plot for Task Satisfaction

<table><tr><td colspan="2">Table 8. Hypotheses Test Results</td></tr><tr><td>Hypothesis</td><td>Result</td></tr><tr><td> $H_1$ : Quality of the design solution will be higher when design patterns are used during software design.</td><td>Supported***</td></tr><tr><td> $H_2$ : Time taken to complete a design task will be shorter when design patterns are used.</td><td>Supported**</td></tr><tr><td> $H_3$ : Solution quality of collaborating pairs will be higher than that of the second-best member of a nominal pair in a software design task.</td><td>Supported***</td></tr><tr><td> $H_{4a}$ : Time taken by collaborating pairs to complete a software design task will be longer than that of the best member of a nominal pair.</td><td>Not Supported</td></tr><tr><td> $H_{4b}$ : Time taken by collaborating pairs to complete a software design task will be longer than that of the second-best member of a nominal pair.</td><td>Supported***</td></tr><tr><td> $H_{5a}$ : When design patterns are available, the performance gap in solution quality between the second-best member of a nominal pair and the best member of the nominal pair and the pair will be reduced in contrast to when design patterns are not used.</td><td>Not Supported</td></tr><tr><td> $H_{5b}$ : Solution quality of second-best member of a nominal pair with design patterns will be higher than that of the collaborating pair without design patterns in a software design task.</td><td>Not Supported</td></tr><tr><td> $H_{5c}$ : Task completion time of second-best member of a nominal pair with design patterns will be lower than that of the collaborating pairs without design patterns in a software design task.</td><td>Supported**</td></tr><tr><td> $H_6$ : Task satisfaction will be higher when design patterns are used in a software design task.</td><td>Supported**</td></tr><tr><td> $H_7$ : The average level of task satisfaction among collaborating pairs will be higher when compared with the average level of task satisfaction of nominal pairs.</td><td>Supported*</td></tr></table>

Notes: \*\*\*p < 0.001; \*\*p < 0.05; \*p < 0.01

## Discussion and Implications

Our study compared the performance of a socially distributed cognitive system with individual cognitive systems at two levels of performance, namely, best and second-best members of a nominal pair. The results show that, in terms of software quality, a socially distributed cognitive system outperforms a low-performing individual system, but operates at the level of a high-performing individual system. Further, our study demonstrates that a structurally enhanced cognitive system delivers superior performance with regard to both quality and time. In addition, a low-performing individual cognitive system augmented by structural cognition outperforms a socially distributed cognitive system in terms of time, while delivering comparable performance with regard to quality.

The following sections elaborate on our findings and provide a discussion of their implications.

## Impact of Design Patterns on Task Outcomes

Design patterns make software design knowledge available to designers in a codified form. Borrowing from distributed cognition theory, this study argued that design patterns would aid in solving design problems. Specifically, we hypothesized that design patterns would lead to better solution quality and reduced time for task completion, and higher levels of task satisfaction. Our results support the hypothesized relationships. Subjects in the pattern condition performed significantly better than those in the no-pattern condition. Since design patterns are considered to be a source of codified knowledge, this study lends credence to the claim that codification strategies facilitate knowledge reuse.

Participants in the pattern condition also took significantly less time to complete the design task than participants in the no-pattern condition. In a study involving development of sales proposals, Haas and Hansen (2007) found that codified knowledge in the form of electronic documents reduces task performance time resulting in increased efficiency. Consequently, these results demonstrate the positive impact of codified knowledge in a domain that differs from the research of Haas and Hansen. Moreover, the results did not change even when we controlled for object-oriented programming experience of the subjects. This suggests that the use of patterns can potentially enhance software development efficiency, irrespective of the developer’s experience level.

The availability of design patterns was also positively associated with task satisfaction. This is an important consideration since job satisfaction has been associated with critical organizational outcomes, including job performance (Judge and Bono 2001) and organizational commitment (Tett and Meyer 1993). In summary, the use of design patterns results in higher quality designs, shorter time to complete a design task, and improved task satisfaction. To the best of our knowledge, ours is one of the first studies to empirically evaluate the efficacy of design patterns in the context of a software design task.

## Impact of Pair Designing on Task Performance

Our study also compared the performance of collaborating pairs with those of individuals in nominal pairs. Our results indicated that the solution quality of collaborating pairs exceeded that of the second-best member of a nominal pair but was not different from that of the performance of the best member of a nominal pair. This finding is a departure from the assertion that collaborating pairs outperform individuals in terms of software quality when working on design tasks (Canfora et al. 2007). It is, however, consistent with Balijepally et al.’s (2009) findings that paired programmers outperform the second-best members of nominal pairs, but not the best members.

It is interesting to note that consistency in results between this and the study by Balijepally et al. was obtained across different samples and tasks. This study used experienced software developers, whereas the research by Balijepally et al. employed novice programmers as subjects. Further, we studied a software design task, while the Balijepally et al. research examined a programming task. Again, while these findings may seem counter to the claims in the software engineering literature (Canfora et al. 2007; Lui et al. 2008), they are consistent with results published in the small group research stream (Laughlin et al. 2006). The extant research on the effect of pairing on task completion time is inconsistent, which has been highlighted by a recent meta-analysis study (Hannay et al. 2009). Our study found collaborating pairs to take significantly more time to complete a design task than the second-best individual in the nominal pair. However, the hypothesis that collaborating pairs would take more time to complete the design task when compared with the best individual of a nominal pair was not supported. In terms of solution quality, the mean performance of best members was comparable to that of collaborating pairs, and was significantly higher than that of second-best members. This suggests that best members have expertise that more than compensates for the absence of a collaborating partner. Such expertise, however, relies on sifting through various abstractions to formulate an understanding of the problem and its attendant solution, particularly when confronted with cognitively demanding tasks. This plausible explanation is consistent with the observation that experts tend to take more time to understand a problem than do novices (Villeneuve and Fedorowicz 1997).

Task satisfaction is an important consideration in work situations due to its impact on employee absenteeism and turnover (Hackman and Oldham 1976). Our study found that when working on a design task, collaborating pairs experience higher levels of satisfaction compared with the average task satisfaction levels of individuals in nominal pairs. This is consistent with prior empirical research in pair programming (Domino et al. 2007; Nosek 1998). It also resonates with the general findings in group research that group work is more satisfying (Hinsz and Nickell 2004).

## Impact of Design Patterns and Pairing on Task Performance

This study also examined the question of relative benefits when patterns were made available to individuals and pairs. The results indicated that design patterns elevated the performance of both individuals and pairs. Notably, second-best members with access to patterns completed the design task significantly faster than collaborating pairs working without patterns. However, there was no evidence of differential benefit to individuals versus pairs when patterns were available. In other words, the second-best member, the bestmember, and the collaborating pair benefitted equally from the availability of design patterns. This suggests that the patterns used in our study were a source of additional knowledge to all participants in the pattern condition. This is consistent with the claim in the distributed cognition literature that the presence of external representational media can enhance the performance of the problem solver (Zhang 1998). This appears to be a plausible explanation for why design patterns did not provide a differential benefit to second-best members vis-à-vis best-members and collaborating pairs.

Our hypothesis that enhanced structural cognition would help second-best members produce higher quality design solutions than those delivered by collaborating pairs unassisted by design patterns was not supported. The results suggest that a complex-individual system characterized by augmented structural cognition performs—in terms of quality—at a level that is comparable to that of a simple-social system (i.e., pairs without access to patterns). From a distributed cognition standpoint, it is conceivable that increased structural cognition compensates for the absence of a social actor. While secondbest members benefitted to a degree from the use of patterns, their inability to fully exploit the knowledge embodied in the patterns might have stemmed from the difficulty of using abstract patterns (Cline 1996) as well as from the purported biases associated with their use (Prechelt et al. 2001).

## Contribution to Research

Our study contributes to theory and scholarship in the areas of IS development, collaborative problem solving, and distributed cognition.

First, it makes a valuable contribution to the corpus of existing literature on software development, an important area of IS research. In recent times, paired development has gained considerable traction among software developers. The findings of our study run counter to the general claims of pair superiority over the individual developer. This study also found design patterns to be useful in enhancing task performance in software design. This supports the use of codified knowledge in the domain of software development. Despite the importance accorded to software development in organizations, theoretically anchored empirical research on this topic is, at best, sparse, especially in premier IS journals. In particular, our research adds to a small but growing body of empirical IS research that addresses issues related to software development practices and processes; examples include Allen and Parsons (2010), Balijepally et al. (2009), Nelson et al. (2009), Shaft and Vessey (2006), and Vidgen and Wang (2009). Theories are seldom developed from scratch, but are often engendered by the gradual accumulation of insights from research (Whetten 1989). From this perspective, our study furthers the cumulative tradition that we hope will one day result in a stronger theoretical framework of IS development.

Second, this study contributes to research in the small group area that explores collaborative problem solving. The sensitivity of group performance to task type and group characteristics makes it important to continue research on group performance (Davis and Harless 1996). Our results suggest that the performance of the second-best individual augmented with design patterns, a form of codified knowledge, is comparable to that of a collaborating pair not using design patterns. This finding, that design patterns can provide compensatory expertise in the absence of a partner, adds to the research stream that has explored alternatives that might allow an individual to perform at the level of a pair (Müller 2005, 2006).

Finally, drawing on research in distributed cognition (Hansen and Lyytinen 2009; Hollan et al. 2000), our study clarifies the impact that an extended cognitive system, broadened either socially or structurally, has on a software design task. While the theory of distributed cognition has been used in previous studies, none of the prior works has compared a socially distributed cognitive system with one in which an individual developer interacted with a material cognitive artifact. This is an important first step in benchmarking the efficacies of these two cognitive systems.

## Contribution to Practice

The findings of this study also have important implications for practitioners. It has been reported that patterns are not widely used in practice (Manolescu et al. 2007). This could be due to a lack of awareness of the benefits of using patterns and/or a lack of knowledge of how to use patterns. In light of our findings, organizations should explore the use of patterns to improve their software development practices. Since software design is a critical upstream activity in the software development life cycle, any quality enhancement in this phase will result in significant savings (Beck 1999). Our results strongly suggest that the use of patterns in software design should be encouraged. Both individuals of different expertise and pairs benefitted from the use of patterns. There did not seem to be any downside, as quality improvements due to the use of patterns were not accompanied by increased “costs” associated with longer completion time. Practitioners constantly strive to deliver high quality solutions in an efficient manner (i.e., in less time). In this context, our finding that lowperforming individuals aided by design patterns produce designs of comparable quality in less time vis-à-vis collaborating pairs unassisted by patterns is particularly insightful.

Additionally, these results can provide guidance to practitioners in deciding when to resort to paired development. Pairs experience higher task satisfaction and deliver designs of superior quality but take more time to complete the design task than the second-best individual. Thus, paired development may be used to improve job satisfaction of developers and/or to compensate for the lower skill level of the less competent member of a pair. IT managers, however, must consider the higher development cost, in terms of personhours, associated with paired development while making such assignments.

The best practices in the field of software development are mostly driven by practitioners and are frequently embraced based on anecdotal evidence or an unquestioning faith in the claims made by leading consultants. Systems thinkers like Jackson (1991) maintain that a good grasp of the theoretical presuppositions and assumptions underlying a methodology is necessary to ensure its proper and efficacious use. In line with this reasoning, it is imperative for IS researchers to theoretically examine contemporary software development practices to validate the assumptions on which they rest. Our study is a small step in this direction.

## Limitations and Future Research

As with any research, there are some potential limitations of this study, and the conclusions should be viewed in light of them. Participants in this study were volunteers, who were recruited from among industry practitioners. The reward for participation was a free seminar on design patterns. The incentive was designed to attract software developers who lacked a knowledge of patterns, while excluding practitioner groups, such as database administrators and network administrators, that didn’t routinely perform software design tasks. The incentive, however, has the potential for self-selection bias as the sample would exclude those developers who didn’t have an interest in learning about design patterns. Subjects in the pattern condition participated in a seminar on design patterns prior to the experiment whereas the no-pattern group was briefed on UML notations used in design. The potential for bias introduced by the seminar, however small, should be noted while interpreting our results.

This study utilized software development professionals as participants but did so within the environment of a laboratory experiment. Consequently, some important situational variables (e.g., commitment, incentive for performance) that may be present in an actual workplace could be absent in the laboratory environment. However, a laboratory experiment provides the necessary control to make causal inferences about the phenomenon under study. Further, it has been argued that laboratory findings may be generalized to the field (Locke 1986). Moreover, the utilization of practitioners rather than students as subjects gives our study a real-world flavor.

Pattern use in a design task is a three-step process: selection, adaptation, and use. The designer selects one or more patterns appropriate for the design task at hand, adapts them suitably, and uses them in the design. In our experiment, we restricted the search process in the selection step by providing the subjects a limited number of patterns. This was done keeping in mind that our subjects were experienced designers with no prior exposure to patterns. To this extent, our study did not simulate some real world scenarios that may involve an exhaustive search through a large array of patterns. Our research design, however, was appropriate to address a more fundamental question with regard to the usefulness of design patterns on task performance.

This study randomly paired individuals without considering factors that might facilitate/hinder collaborative performance. The question of what enables pairs to derive the synergies required to outperform best individuals remains unanswered. To this end, future studies may investigate the effects of factors such as team size, team diversity, difference in the levels of expertise between team members, and personality types of collaborators on software development group outcomes. The moderating effects of these variables may very well provide keen insights into the cognitive performance of groups vis-à-vis individuals.

Future studies could also focus more on the structural distribution of cognition. For example, they could use a large selection of patterns to explore the impact of the search and selection process on design task performance. Further, since patterns vary in the degree of difficulty, it would be interesting to study how patterns of different complexity impact task performance. Our study focused on the outcomes of using patterns without regard to cognitive variables that influence the process of reuse (Allen and Parsons 2010). Future studies could investigate process-related variables that may facilitate or hamper the use of design patterns.

## Conclusions

In a recent article devoted to unraveling “enduring questions in cognitive IS research,” Davern et al. (2012, p. 276) observe that, “social context and the manner in which cognition is distributed across a group of users and IT artifacts is an area that should be of increasing focus for cognitive research in IS.” In addition to addressing this imperative to an extent, our study responds to the clarion call for design-centric research that empirically investigates the efficacy of contemporary software practices such as design patterns (Zhang and Budgen 2012) and pair designing (Salleh et al. 2011).

Our articulation of a two-by-two framework based on the social and structural dimensions of distributed cognition opens up new vistas of research on distributed cognition. Further, the instantiation of the theoretical framework using individual and paired designers along the social dimension and the availability/nonavailability of design patterns along the structural dimension provides a robust conceptual scaffold for investigating the cognitive performance of four distinct systems.

Our study is not only an affirmation of the claim that design patterns can facilitate a correct solution faster, but is also a clarification of the role that external representational media play in cognitively challenging tasks. Consistent with the theorization of distributed cognition, this research demonstrates that the insertion of task-related external artifacts can alter the cognitive performance of a system. Further, the results suggest that increased structural distribution (i.e., second-best individual with design patterns) can adequately compensate for the absence of a collaborating partner. Future studies on software development may seek to affirm these findings while elucidating the nature of the distribution of cognition across social actors and external representational media.

## Acknowledgments

We thank Suprateek Sarker, our senior editor, the associate editor, and the reviewers for their insightful comments and thoughtful suggestions that helped us significantly improve the quality of the manuscript.

## References

Agarwal, R., Sinha, A. P., and Tanniru, M. 1996. “The Role of Prior Experience and Task Characteristics in Object-Oriented Modeling: An Empirical Study,” International Journal of Human–Computer Studies (45:6), pp. 639-667.

Aladwani, A.M. 2002. “An Integrated Performance Model of Information Systems Projects,” Journal of Management Information Systems (19:1), Summer, pp. 185-210.

Allen, G., and Parsons, J. 2010. “Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries,” Information Systems Research (21:1), pp. 56-77.

Ambler, S. 2007. “Survey Says...Agile Has Crossed the Chasm,” Dr. Dobb’s Journal, July 2 (http://www.drdobbs.com/ architecture-and-design/survey-saysagile-has-crossed-thechasm/200001986; accessed July 11, 2013).

Arisholm, E., Gallis, H., Dybå, T., and Sjøberg, D. I. K. 2007. “Evaluating Pair Programming with Respect to System Complexity and Programmer Expertise,” IEEE Transactions on Software Engineering (33:2), pp. 65-86.

Balijepally, V., Mahapatra, R., Nerur, S. P., and Price, K. H. 2009. “Are Two Heads Better Than One for Software Development? The Productivity Paradox of Pair Programming,” MIS Quarterly (32:4), pp. 91-118.

Batra, D. 2005. “Conceptual Data Modeling Patterns: Representation and Validation,” Journal of Database Management (16:2), pp. 84-106.

Beck, K. 1999. Extreme Programming Explained: Embrace Change, Reading, MA: Addison-Wesley.

Brodbeck, F., and Greitemeyer, T. 2000. “A Dynamic Model of Group Performance: Considering the Group Members’ Capacity to Learn,” Group Processes & Intergroup Relations (3:2), pp. 159-182.

Campbell, D. J. 1988. “Task Complexity: A Review and Analysis,” Academy of Management Review (13:1), pp. 40-52.

Canfora, G., Cimitile, A., Garcia, F., Piattini, M., and Visaggio, C. A. 2007. “Evaluating Performances of Pair Designing in Industry,” Journal of Systems and Software (80:8), pp. 1317-1327.

Carey, J. M., and Kacmar, C. J. 1997. “The Impact of Communication Mode and Task Complexity on Small Group Performance and Member Satisfaction,” Computers in Human Behavior (13:1), pp. 23-49.

Cline, M. P. 1996. “The Pros and Cons of Adopting and Applying Design Patterns in the Real World,” Communications of the ACM (39:10), pp. 47-49.

Cockburn, A., and Williams, L. 2001. “The Costs and Benefits of Pair Programming,” in Extreme Programming Examined, G. Succi and M. Marchesi (eds.), Upper Saddle River, NJ: Pearson Education, pp. 223-243.

Darcy, D. P., Kemerer, C. F., Slaughter, S. A., and Tomayko, J. E. 2005. “The Structural Complexity of Software: An Experimental Test,” IEEE Transactions on Software Engineering (31:11), pp. 982-995.

Davern, M., Shaft, T., and Te’eni, D. 2012. “Cognition Matters: Enduring Questions in Cognitive IS Research,” Journal of the Association for Information Systems (13:4), pp. 273-314.

Davis, D. D., and Harless, D. W. 1996. “Group Vs. Individual Performance in a Price-Searching Experiment,” Organizational Behavior and Human Decision Processes (66:2), pp. 215-227.

Domino, M. A., Collins, R. W., and Hevner, A. R. 2007. “Controlled Experimentation on Adaptations of Pair Programming,” Information Technology and Management (8:4), pp. 297-312.

Dyba, T., Arisholm, E., Sjøberg, D. I. K., Hannay, J. E., and Shull, F. 2007. “Are Two Heads Better Than One? On the Effectiveness of Pair Programming,” IEEE Software (24:6), pp. 12-15.

Flor, N. V., and Hutchins, E. L. 1991. “Analyzing Distributed Cognition in Software Teams: A Case Study of Team Programming During Perfective Software Maintenance,” in Empirical Studies of Programmers: Fourth Workshop, J. Koenemann-Belliveau, T. Moher, and S. Robertson (eds.), Norwood, NJ: Ablex, pp. 36-64.

Freeman, E., Freeman, E., Sierra, K., and Bates, B. 2004. Head First Design Patterns, Sebastopol, CA: O’Reilly Media.

Gamma, E., Helm, R., Johnson, R. E., and Vlissides, J. 1995. Design Patterns: Elements of Reusable Object-Oriented Software, Reading, MA: Addison-Wesley.

Guindon, R. 1990. “Knowledge Exploited by Experts During Software System-Design,” International Journal of Man-Machine Studies (33:3), pp. 279-304.

Haas, M. R., and Hansen, M. T. 2007. “Different Knowledge, Different Benefits: Toward a Productivity Perspective on Knowledge Sharing in Organizations,” Strategic Management Journal (28:11), pp. 1133-1153.

Hackman, J. R. 1968. “Effects of Task Characteristics on Group Products,” Journal of Experimental Social Psychology (4:2), pp. 162-187.

Hackman, J. R., and Oldham, G. R. 1976. “Motivation through the Design of Work: Test of a Theory,” Organizational Behavior and Human Performance (16:2), pp. 250-279.

Hair, J. F., Tatham, R. L., Anderson, R. E., and Black, W. 1998. Multivariate Data Analysis (5<sup>th</sup> ed.), Upper Saddle River, NJ: Prentice Hall.

Hannay, J. E., Dyba, T., Arisholm, E., and Sjøberg, D. I. K. 2009. “The Effectiveness of Pair Programming: A Meta-Analysis,” Information and Software Technology (51:7), pp. 1110-1122.

Hansen, S., and Lyytinen, K. 2009. “Distributed Cognition in the Management of Design Requirements,” in Proceedings of the 15<sup>th</sup> Americas Conference on Information Systems, San Francisco, CA, August 6-9.

Hare, A. P. 1976. Handbook of Small Group Research (2<sup>nd</sup> ed.), New York: Free Press.

Hill, G. W. 1982. “Group Versus Individual-Performance: Are N + 1 Heads Better Than One,” Psychological Bulletin (91:3), pp. 517-539.

Hinsz, V. B., and Nickell, G. S. 2004. “Positive Reactions to Working in Groups in a Study of Group and Individual Goal Decision Making,” Group Dynamics-Theory Research and Practice (8:4), pp. 253-264.

Hinsz, V. B., Tindale, R. S., and Vollrath, D. A. 1997. “The Emerging Conceptualization of Groups as Information Processors,” Psychological Bulletin (121:1), pp. 43-64.

Hollan, J., Hutchins, E., and Kirsh, D. 2000. “Distributed Cognition: Toward a New Foundation for Human–Computer Interaction Research,” ACM Transactions on Computer–Human Interaction (7:2), pp. 174-196.

Jackson, M. C. 1991. Systems Methodology for the Management Sciences, New York: Plenum Press.

Judge, T. A., and Bono, J. E. 2001. “Relationship of Core Self-Evaluations Traits—Self-Esteem, Generalized Self-Efficacy, Locus of Control, and Emotional Stability—with Job Satisfaction and Job Performance: A Meta-Analysis,” Journal of Applied Psychology (86:1), pp. 80-92.

Karau, S. J., and Williams, K. D. 2001. “Understanding Individual Motivation in Groups: The Collective Effort Model,” in Applied Social Research, M. E. Turner (ed.), Mahwah, NJ: Lawrence Erlbaum Associates, pp. 113-141.

Klugman, S. F. 1944. “Cooperative Versus Individual Efficiency in Problem Solving,” Journal of Educational Psychology (35:2), pp. 91-100.

Kohls, C., and Scheiter, K. 2008. “The Relation Between Design Patterns and Schema Theory,” in Proceedings of the 15<sup>th</sup> Conference on Pattern Languages of Programs (PLoP’08), Nashville, TN, October 19, Article 15.

Laughlin, P. R., Bonner, B. L., and Miner, A. G. 2002. “Groups Perform Better Than the Best Individuals on Letters-to-Numbers Problems,” Organizational Behavior & Human Decision Processes (88:2), pp. 605-620.

Laughlin, P. R., Hatch, E. C., Silver, J. S., and Boh, L. 2006. “Groups Perform Better Than the Best Individuals on Lettersto-Numbers Problems: Effects of Group Size,” Journal of Personality and Social Psychology (90:4), pp. 644-651.

Locke, E. A. 1986. Generalizing from Laboratory to Field Settings: Research Findings from Industrial-Organizational Psychology, Organizational Behavior and Human Resource Management, Lexington, MA: Lexington Books.

Lui, K. M., and Chan, K. C. C. 2006. “Pair Programming Productivity: Novice–Novice Vs. Expert–Expert,” International Journal of Human-Computer Studies (64:9), pp. 915-925.

Lui, K. M., Chan, K. M., and Nosek, J. 2008. “The Effect of Pairs in Program Design Tasks,” IEEE Transactions on Software Engineering (34:2), pp. 197-211.

Manolescu, D., Kozaczynski, W., Miller, A., and Hogg, J. 2007. “The Growing Divide in the Patterns World,” IEEE Software (24:4), pp. 61-67.

Mason, C. M., and Griffin, M. A. 2005. “Group Task Satisfaction,” Group & Organization Management (30:6), pp. 625-652.

McGrath, J. E. 1984. Groups: Interaction and Performance, Englewood Cliffs, NJ: Prentice-Hall.

McGraw, K. O., and Wong, S. P. 1996. “Forming Inferences About Some Intraclass Correlation Coefficients,” Psychological Methods (1:1), pp. 30-46.

Müller, M. M. 2005. “Two Controlled Experiments Concerning the Comparison of Pair Programming to Peer Review,” Journal of Systems and Software (78:2), pp. 166-179.

Müller, M. M. 2006. “A Preliminary Study on the Impact of a Pair Design Phase on Pair Programming and Solo Programming,” Information and Software Technology (48:5), pp. 335-344.

Müller, M. M. 2007. “Do Programmer Pairs Make Different Mistakes Than Solo Programmers?,” Journal of Systems and Software (80:9), pp. 1460-1471.

Nelson, H. J., Armstrong, D. J., and Nelson, K. M. 2009. “Patterns of Transition: The Shift from Traditional to Object-Oriented Development,” Journal of Management Information Systems (25:4), pp. 271-297.

Neter, J., Kutner, M. H., Wasserman, W., and Nachtsheim, C. J. 1996. Applied Linear Statistical Models (4<sup>th</sup> ed.), New York: McGraw-Hill/Irwin.

Newell, A., and Simon, H. A. 1972. Human Problem Solving, Englewood Cliffs, NJ: Prentice-Hall.

Nijstad, B. A., Stroebe, W., and Lodewijkx, H. F. M. 2006. “The Illusion of Group Productivity: A Reduction of Failures Explanation,” European Journal of Social Psychology (36:1), pp. 31-48.

Nosek, J. T. 1998. “The Case for Collaborative Programming,” Communications of the ACM (41:3), pp. 105-108.

Nunnally, J. C. 1978. Psychometric Theory, New York: McGraw-Hill.

Park, E. S., and Hinsz, V. B. 2006. “‘Strength and Safety in Numbers’: A Theoretical Perspective on Group Influences on Approach and Avoidance Motivation,” Motivation and Emotion (30:2), pp. 135-142.

Parsons, J., and Saunders, C. 2004. “Cognitive Heuristics in Software Engineering: Applying and Extending Anchoring and Adjustment to Artifact Reuse,” IEEE Transactions on Software Engineering (30:12), pp. 873-888.

Paulus, P. B., Dzindolet, M. T., Poletes, G., and Camacho, L. M. 1993. “Social Influence Processes in Group Brainstorming,” Perception of Performance in Group Brainstorming: The Illusion of Group Productivity (19:1), pp. 78-89.

Pennington, N. 1987. “Stimulus Structures and Mental Representations in Expert Comprehension of Computer Programs,” Cognitive Psychology (19:3), pp. 295-341.

Prechelt, L., Unger, B., Tichy, W. F., Brossler, P., and Votta, L. G. 2001. “A Controlled Experiment in Maintenance Comparing Design Patterns to Simpler Solutions,” IEEE Transactions on Software Engineering (27:12), pp. 1134-1144.

Prechelt, L., Unger-Lamprecht, B., Philippsen, M., and Tichy, W. F. 2002. “Two Controlled Experiments Assessing the Usefulness of Design Pattern Documentation in Program Maintenance,” IEEE Transactions on Software Engineering (28:6), pp. 595-606.

Purao, S., Storey, V. C., and Han, T. D. 2003. “Improving Analysis Pattern Reuse in Conceptual Design: Augmenting Automated Processes with Supervised Learning,” Information Systems Research (14:3), pp. 269-290.

Ramasubbu, N., Kemerer, C., and Hong, J. 2012. “Structural Complexity and Programmer Team Task Strategy: An Experimental Test,” IEEE Transactions on Software Engineering (38:5), pp. 1054-1068.

Rehder, B., Pennington, N., and Lee, A. Y. 1997. “Scoring the Completeness of Software Designs,” Journal of Systems and Software (36:1), pp. 33-68.

Richter, C. 1999a. “Design Problems and Object-Oriented Solutions” (http://www.oeng.com/problemsandsolutions.htm; accessed Feburary 10, 2013).

Richter, C. 1999b. Designing Flexible Object-Oriented Systems with UML, Indianapolis, IN: Macmillan Technical Publishing.

Robillard, P. N. 1999. “The Role of Knowledge in Software Development,” Communications of the ACM (42:1), pp. 87-92.

Rosen, M. A., Salas, E., Fiore, S. M., Pavlas, D., and Lum, H. C. 2009. “Team Cognition and External Representations: A Framework and Propositions for Supporting Collaborative Problem Solving,” in Proceedings of the Human Factors and Ergonomics Society Annual Meeting, Santa Monica, CA: Human Factors and Ergonomics Society, pp. 1295-1299.

Salleh, N., Mendes, E., and Grundy, J. 2011. “Empirical Studies of Pair Programming for CS/SE Teaching in Higher Education: A Systematic Literature Review,” IEEE Transactions on Software Engineering (37:4), pp. 509 - 525.

Schmidt, D. C., Fayad, M., and Johnson, R. E. 1996. “Software Patterns,” Communications of the ACM (39:10), pp. 36-39.

Shaft, T. M., and Vessey, I. 2006. “The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification,” MIS Quarterly (30:1), pp. 29-55.

Sharp, H., and Robinson, H. 2006. “A Distributed Cognition Account of Mature XP Teams,” in Proceedings of the 7<sup>th</sup> International Conference on eXtreme Programming and Agile Processes in Software Engineering, P. Abrahamsson, M. Marchesi, and G. Succi (eds.), Berlin: Springer-Verlag, pp. 1-10.

Sharp, H., and Robinson, H. 2008. “Collaboration and Coordination in Mature Extreme Programming Teams,” International Journal of Human-Computer Studies (66:7), pp. 506-518.

Sharp, H., Robinson, H., and Petre, M. 2009. “The Role of Physical Artefacts in Agile Software Development: Two Complementary Perspectives,” Interacting with Computers (21:1-2), pp. 108-116.

Shaw, J. D., Duffy, M. K., and Stark, E. M. 2000. “Interdependence and Preference for Group Work: Main and Congruence

Effects on the Satisfaction and Performance of Group Members,” Journal of Management (26:2), pp. 259-279.

Shirouzu, H., Miyake, N., and Masukawa, H. 2002. “Cognitively Active Externalization for Situated Reflection,” Cognitive Science (26:4), pp. 469-501.

Simon, H. A. 1973. “The Structure of Ill Structured Problems,” Artificial Intelligence (4:3-4), pp. 181-201.

Small, R. V., and Venkatesh, M. 2000. “A Cognitive-Motivational Model of Decision Satisfaction,” Instructional Science (28:1), pp. 1-22.

Steiner, I. D. 1972. Group Process and Productivity, New York: Academic Press.

Straus, S. G. 1999. “Testing a Typology of Tasks: An Empirical Validation of McGrath’s (1984) Group Task Circumplex,” Small Group Research (30:2), pp. 166-187.

Tett, R. P., and Meyer, J. P. 1993. “Job Satisfaction, Organizational Commitment, Turnover Intention, and Turnover: Path Analyses Based on Meta-Analytic Findings,” Personnel Psychology (46:2), pp. 259-203.

Vidgen, R., and Wang, X. 2009. “Coevolving Systems and the Organization of Agile Software Development,” Information Systems Research (20:3), pp. 355-376.

Villeneuve, A. O., and Fedorowicz, J. 1997. “Understanding Expertise in Information Systems Design, or, What’s All the Fuss About Objects?,” Decision Support Systems (21:2), pp. 111-131.

Vokac, M., Tichy, W., Sjøberg, D. I. K., Arisholm, E., and Aldrin, M. 2004. “A Controlled Experiment Comparing the Maintainability of Programs Designed with and without Design Patterns: A Replication in a Real Programming Environment,” Empirical Software Engineering (9:3), pp. 149-195.

Whetten, A. D. 1989. “What Constitutes a Theoretical Contribution?,” Academy of Management Review (14:4), pp. 490-495.

Williams, L., Kessler, R. R., Cunningham, W., and Jeffries, R. 2000. “Strengthening the Case for Pair Programming,” IEEE Software (17:4), pp. 19-25.

Zhang, C., and Budgen, D. 2012. “What Do We Know About the Effectiveness of Software Design Patterns,” IEEE Transactions on Software Engineering (38:5), pp. 1213-1231.

Zhang, J. 1998. “A Distributed Representation Approach to Group Problem Solving,” Journal of American Society of Information Science (49:9), pp. 801-809.

Zhang, J., and Norman, D. A. 1994. “Representations in Distributed Cognitive Tasks,” Cognitive Science (18:1), pp. 87-122.

Zigurs, I., and Buckland, B. K. 1998. “A Theory of Task/ Technology Fit and Group Support Systems Effectiveness,” MIS Quarterly (22:3), pp. 313-334.

## About the Authors

George Mangalaraj is an associate professor of Information Systems at Western Illinois University, Macomb. He received his M.S. and Ph.D. degrees in Information Systems from the University of Texas at Arlington. His research interests are in the areas of systems development, diffusion of innovations, and issues in online

environment. His publications appear in Communications of the ACM, IEEE Transactions of Professional Communication, European Journal of Information Systems, Journal of the Association for Information Systems, Journal of Information Privacy and Security, Journal of Information Systems Education, Journal of Accounting Education ,and various conference proceedings.

Sridhar Nerur is an associate professor of Information Systems at the University of Texas at Arlington. He holds an engineering degree in electronics from Bangalore University, a PGDM (MBA) from the Indian Institute of Management, Bangalore, India, and a Ph.D. in business administration from the University of Texas at Arlington. His research appears in MIS Quarterly, Strategic Management Journal, Communications of the ACM, Communications of the AIS, The DATA BASE for Advances in Information Systems, European Journal of Information Systems, Information Systems Management, and Journal of International Business Studies. He has served as an associate editor for the European Journal of Information Systems. His research and teaching interests consider social networks, software design, adoption of software development methodologies, cognitive aspects of programming, dynamic IT capabilities, and agile software development.

RadhaKanta Mahapatra is a professor of Information Systems at the University of Texas at Arlington. He holds a bachelor’s degree in Electrical Engineering from the National Institute of Technology, Rourkela, India, a PGDM (MBA) from the Indian Institute of Management, Ahmedabad, India, and a Ph.D. in Information Systems from Texas A&M University. His research interests include agile software development and project management, data warehousing and business intelligence, data quality, and healthcare information systems. His research publications have appeared in MIS Quarterly, Communications of the ACM, Decision Support Systems, Information & Management, European Journal of Information Systems, and other journals. He received the Distinguished Research Publication Award and the Distinguished Professional Publication Award from the College of Business Administration of the University of Texas at Arlington.

Kenneth H. Price is a professor emeritus of Management and Organizational Behavior at the University of Texas at Arlington. He received his Ph.D. from Michigan State University in Industrial-Organizational Psychology. His research publications appear in Management Science, Academy of Management Journal, Journal of Management, Organizational Behavior and Human Decision Processes, Journal of Applied Psychology, MIS Quarterly, Journal of Information Systems, Personality and Social Psychology Bulletin, Group and Organizational Studies, Basic and Applied Social Psychology, Human Resource Management Review, Behavioral Research in Accounting, The Accounting Review, and Theory and Decision. He is a past associate editor of the International Journal of Conflict Management and was a guest editor and is currently a member of the Editorial Board of Organizational Behavior and Human Decision Processes.

# DISTRIBUTED COGNITION IN SOFTWARE DESIGN: AN EXPERIMENTAL INVESTIGATION OF THE ROLE OF DESIGN PATTERNS AND COLLABORATION

George Mangalaraj

College of Business and Technology, Western Illinois University, Macomb, IL 61455 U.S.A. {g-mangalaraj@wiu.edu}

Sridhar Nerur, RadhaKanta Mahapatra, and Kenneth H. Price College of Business Administration, University of Texas at Arlington, Arlington, TX 76019-0437 U.S.A. {snerur@uta.edu} {mahapatra@uta.edu} {price@uta.edu}

## Appendix A

## An Illustrative Example of the Application of a Design Pattern

The state pattern allows an object to exhibit a different behavior (i.e., alter its response to one or more messages) when its internal state changes (Gamma et al. 1995). Consider an Account class that keeps track of a customer’s credit payments. At any time during its life cycle, such an Account object can be in one of many possible states: Current, Canceled, and PastDue, to name but a few. The state of the Account object would determine its response to requests/messages that it receives from other objects. For example, a request to handle payment (i.e., invocation of the handlePayment() method) would result in different behaviors depending on whether it is in the Current, Canceled, or PastDue state. When the state pattern is not used, a variable (e.g., a String) would typically be used to maintain the state of the object. As shown below, the use of such a String variable (let us call it status) would result in conditional statements in the handle payment operation.

public void handlePayment() {

if ( status.equals(“Current”))

// statements to handle payment when the Account object is current

else if ( status.equals(“Canceled”))

//statements to handle payment when the Account object is in the canceled state

//statements to handle payment when the Account object is past due

Clearly, the method would have to be changed every time a new state is introduced. For example, if we decide to introduce a state called Hold, the condition for hold would have to be included in the if…then statements.

The state pattern advocates maintaining a state object rather than a variable such as status, so that the Account object’s behavior can be changed easily at run-time while giving us the flexibility to add states in the future without modifications to the state-dependent methods themselves. Therefore, in our example, we would introduce an abstract class called AccountState that presents an interface common to its subclasses, Current, Canceled, and PastDue (see Figure A1). Note that there are as many subclasses as there are conditional branches shown in the code above. The Account object now maintains a reference to a state object (i.e., an object of type AccountState), indicating its present state. All requests (such as handlePayment()) that are dependent on the state would be delegated to this state object. Therefore, when the state pattern is applied, the snippet of code would be as follows:

public void handlePayment() { state.handlePayment(); //where state is an AccountState object }

![](/api/attachments/CA7C7XT9/fulltext/images/0170b1e6e9733ad7c5371b26f8c511eb47818e57b29f5443c5a731195c06d3b7.jpg)  
Figure A1. Current, Cancelled, and Past Due Subclasses

## Reference

Gamma, E., Helm, R., Johnson, R. E., and Vlissides, J. 1995. Design Patterns: Elements of Reusable Object-Oriented Software, Reading, MA: Addison-Wesley.

## Appendix B

## Questionnaire

1. Please circle your gender: Male Female

2. Please indicate your age on your last birthday

3. Highest educational level: a) High school b) Technical school or community college c) Undergraduate degree d) Graduate degree d) Doctoral degree e) Other

4. Indicate number of years of your programming experience in any programming language? a) 0 – 1 b) 1 – 2 c) 2 – 4 d) 4 – 6 e) > 6

5. Indicate number of years of your programming experience in object-oriented languages? a) 0 – 1 b) 1 – 2 c) 2 – 4 d) 4 – 6 e) > 6

6. What would you consider to be your level of experience in object-oriented design? a) No experience b) Novice c) Intermediate d) Expert

7. What would you consider to be your level of experience in design patterns? a) No experience b) Novice c) Intermediate d) Expert

8. What object-oriented programming languages are you familiar with? a) C++ b) C# c) Java d) Small Talk e) Objective-C f) Eiffel g) Python h) VB.NET i) Others

9. Before today’s task performance, have you ever worked with your partner?\* a) Yes b) No

10. How do you feel about your overall experience of working on the task today?

<table><tr><td>Very Dissatisfied</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>Very Satisfied</td></tr><tr><td>Very Displeased</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>Very Pleased</td></tr><tr><td>Very Frustrated</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>Very Contented</td></tr><tr><td>Absolutely Terrible</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>Absolutely Delighted</td></tr></table>

11. My partner actively participated in solving the design problem\* Strongly Disagree 1 2 3 4 5 6 Strongly Agree

12. What patterns did you use to arrive at the solution?

Note: \*These questions were asked only in the collaborating pair condition.

## Appendix C

## The Two Experimental Tasks

## Warm-Up Task: Duck Pond Simulation Game<sup>1</sup>

XYZ Corporation is in the process of designing a duck pond simulation game. The game can display a large variety of duck species swimming and making quacking sounds. Some of the duck types that are planned to be used in the simulation game include: Mallard Duck, Redhead Duck, Bufflehead Duck, and Pintail Duck. They are also planning to add Rubber Duck to the game. Real ducks are capable of quacking and flying whereas the rubber ducks can only squeak and cannot fly. All the ducks have a behavior to display themselves on the screen. You are required to draw a class diagram that can be used to implement the system described above.

## Main Task: Weather Monitor<sup>2</sup>

You must develop software that allows clients to periodically check for changes in the status of sensors in a weather monitoring station Examples of various sensors could be temperature gauge, pressure gauge, humidity sensor, etc. A client must be able to create a monitor that will periodically check a particular sensor in the network. If the state of that sensor has changed since the monitor last checked the sensor, the monitor should write an event to a global event log.

A sensor is uniquely designated by its sensor ID. When making its initial monitoring request, the client specifies the ID of the sensor to be monitored and the monitoring period. At that point, the monitor is initialized but has not yet been started. The client makes a subsequent request to start the monitor. The client should be able to start and stop the monitor at any time.

Each sensor has an interface to check its current state, although the precise interface differs from sensor to sensor. As an example, to check a temperature sensor, you invoke its getTemparature method, whereas to check a relative humidity sensor, you call its getRh method. The various sensor classes are provided by different vendors, so you are not permitted to change the interfaces of those classes.

The components that make up the states of different sensors may also differ. For example, the state of a temperature sensor is defined by a floating point value. A relative humidity sensor state, on the other hand, is represented by a string.

Assume the existence of an Event Log and an Event class. The Event Log classes define a method, logEvent that takes an Event as an argument and places that Event in the Log. You should write a specific type of Event, a Sensor Change Event that includes the ID of the sensor.

You are required to draw a class diagram that can be used to implement the system described above.

## Appendix D

## Grading Sheet for Weather Monitoring Station Problem

Subject ID:

<table><tr><td>No.</td><td>Description</td><td>Purpose</td><td>Points</td><td>Points Scored</td><td>Remarks</td></tr><tr><td colspan="6">A. Classes</td></tr><tr><td>1</td><td>Monitor</td><td>Sensors are monitored by this class</td><td>5</td><td></td><td></td></tr><tr><td>2</td><td>Sensor</td><td>Can be abstract or an interface</td><td>5</td><td></td><td></td></tr><tr><td>3</td><td>Specific Sensor</td><td>Temperature, Pressure sensors etc.</td><td>5</td><td></td><td></td></tr><tr><td>4</td><td>Event log</td><td>Log of various events</td><td>5</td><td></td><td></td></tr><tr><td>5</td><td>Event</td><td>Generic class</td><td>5</td><td></td><td></td></tr><tr><td>6</td><td>Change Event</td><td>This is the sensor change event</td><td>5</td><td></td><td></td></tr><tr><td>7</td><td>Adapter class</td><td>Adapter for the sensors to handle different states</td><td>10</td><td></td><td></td></tr><tr><td>8</td><td>PollToken</td><td>To store state and compare</td><td>10</td><td></td><td></td></tr><tr><td colspan="6">B. Associations</td></tr><tr><td>1</td><td>Monitor/Sensors Interface</td><td>Polltoken object is returned to monitor</td><td>5</td><td></td><td></td></tr><tr><td>2</td><td>Event logging</td><td>Monitor detects changes when they occur, creates change event</td><td>10</td><td></td><td></td></tr><tr><td>3</td><td>Specific sensor/ Poll token</td><td>Specific sensors creating poll token</td><td>5</td><td></td><td></td></tr><tr><td>4</td><td>Comparing states</td><td>Monitor should be able to compare poll tokens (previous state poll token is the current state poll token)</td><td>10</td><td></td><td></td></tr><tr><td>6</td><td>Sensor Adapter/ Sensor</td><td>Sensor Adapters forward poll to specific sensors</td><td>10</td><td></td><td></td></tr><tr><td colspan="6">C. Optional Classes</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6">D. Unnecessary/Wrong Classes</td></tr><tr><td>1</td><td></td><td></td><td>-</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td>-</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td>-</td><td></td><td></td></tr><tr><td></td><td>Total</td><td></td><td></td><td></td><td></td></tr></table>

## Patterns Used:

Note: Class names are given for illustration only and the evaluated solution can have different names for them.
