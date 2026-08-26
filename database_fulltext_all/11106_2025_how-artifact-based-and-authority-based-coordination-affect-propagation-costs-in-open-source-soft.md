---
otero_id: 11106
otero_key: "ZE2QU54P"
title: "How Artifact-Based and Authority-Based Coordination Affect Propagation Costs in Open Source Software Development"
authors: "Michael A. Zaggl"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/18021"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# HOW ARTIFACT-BASED AND AUTHORITY-BASED COORDINATION AFFECT PROPAGATION COSTS IN OPEN SOURCE SOFTWARE DEVELOPMENT<sup>1</sup>

Michael A. Zaggl NEOMA Business School, Reims, FRANCE {michael.zaggl@neoma-bs.fr}

The success of open source software (OSS) projects depends on their ability to produce software architectures with low propagation costs, as such architectures demand little effort from developers. This study focuses on the project’s form of coordination—the way in which interdependent contributions are managed—as a driving force behind propagation costs. It distinguishes between two coordination archetypes. First, artifact-based coordination is found in egalitarian projects, in which developers only use the work artifact (the architecture itself), without direct interaction, to coordinate. Second, authoritybased coordination is used in hierarchical projects (e.g., Linux Kernel) or when companies pay developers for their work. Using a computational model, this study compares these two coordination mechanisms by simulating how they build software architectures (formalized as design structure matrices) from interdependent contributions. As a contextual condition, the model considers the degree of architecture visibility, which is the developers’ (in)ability to see recent additions to the architecture. The model provides two insights. First, artifact-based coordination, as compared to authority-based coordination, generally leads to lower propagation costs. Second, decreasing the degree of architecture visibility reduces propagation costs, an effect that I describe as focal-layered superposition. These insights contribute to the literatures on coordination in OSS development and the mirroring hypothesis. They also have practical implications for the creation of preferable architectures in OSS development.

Keywords: Architectures, artifact-based coordination, design structure matrices (DSM), focal-layered superposition, mirroring hypothesis, open source software, open superposition, propagation costs, simulation model, visibility

## Introduction

Open source software (OSS) development has become a relevant part of our economy and is growing at a double-digit rate annually (Research and Markets, 2020). To ensure the success of OSS, it is essential that OSS projects attract and retain developers (Chengalur-Smith et al., 2010; Daniel et al., 2013; Liu et al., 2021; Sharma et al., 2022). In addition to motivating developers (Daniel et al., 2018; Malgonde et al., 2023; Maruping et al., 2019; Medappa & Srivastava, 2020), this can be achieved by reducing their workload.

The key to reducing OSS developers’ workload is to have software architectures with low propagation costs, which is the extent to which software changes ripple through software architectures. More precisely, propagation costs are defined as the number of functions that are directly or indirectly affected when one function is modified (Baldwin et al., 2014; MacCormack et al., 2006). Low propagation costs enhance adaptability, streamlining the debugging, modification, maintenance, expansion, and updating of software, thereby lightening the work burden for existing developers and simplifying new developers’ familiarization with the software. In contrast, high propagation costs inhibit these activities. For example, when the source code of the

Netscape browser was released to the public in hopes of transforming it into an OSS project, it became evident that “the code was too complicated and crufty and hard to modify, which is why people didn’t contribute” (Zawinski, 1999); the project only became successful when the code was redesigned, reducing the architecture’s propagation costs (MacCormack et al., 2006).

Although it is clear that propagation costs should be kept low, they still creep into OSS architectures. Propagation costs result from individual developers making contributions that build on functions contributed by others. Although developers’ attempts to draw on one another’s functions are desirable, as it helps them focus and specialize (Haefliger et al., 2008; Krueger, 1992; see also Vial, 2023), cumulatively, this practice creates unplanned and unwanted interdependencies in the overall architecture and increases propagation costs (MacCormack et al., 2006, 2012).

However, the way in which OSS projects coordinate the multitude of interdependent contributions may influence propagation costs and thus provide an opportunity to reduce them. Coordination—defined as “managing dependencies between activities” (Malone & Crowston, 1994, p. 90)—has taken different forms across OSS projects, and, primarily, two archetypes can be identified. First, projects deploying what I label artifact-based coordination are organized based on an egalitarian structure (e.g., GNOME and BibDesk; Dahlander & O’Mahony, 2011; Howison & Crowston, 2014), in which developers only coordinate by indirectly interacting through their work on the software code (Becker et al., 2021; Bolici et al., 2016; Howison & Crowston, 2014; Medappa & Srivastava, 2019). Second, other OSS projects rely on authority-based coordination and deploy centralized structures (e.g., Linux) (Kernel and Debian; O’Mahony & Ferraro, 2007; Shaikh & Henfridsson, 2017), in which coordination is facilitated by the project founders, who are “benevolent dictators,” elected leaders, or authorities entering the project because of company involvement in the OSS project (Dahlander & O’Mahony, 2011; Germonprez et al., 2017; O’Mahony & Ferraro, 2007; Shaikh & Henfridsson, 2017).

Although we have a solid understanding of these coordination mechanisms, it is unclear how they affect the propagation costs of OSS architectures. The literature on “mirroring” (Colfer & Baldwin, 2016; MacCormack et al., 2006, 2012) addresses the relationship between organization design and product architectures and advocates for congruence between the type of coordination and the architecture (Cataldo et al., 2008; Cataldo & Herbsleb, 2013). This suggests that a more egalitarian way of organizing, such as artifact-based coordination, leads to lower propagation costs than authoritybased coordination regimes. However, empirical research on the mirroring hypothesis has shown many inconsistencies and exceptions, and it continues to struggle to find consistent support; the main reason for this is a lack of insight into the mechanisms causing mirroring (Cabigiosu & Camuffo, 2012; Colfer & Baldwin, 2016; MacCormack et al., 2012; Mattarelli et al., 2022). Thus, to gain insight into coordination as a factor in the creation of propagation costs, this study asks the following question: How do artifact-based and authoritybased coordination compare in terms of building OSS architectures with low propagation costs?

The answer to this question may be conditional on developers’ ability to read the architecture and see what functions are available (cf. Howison & Crowston, 2014), which I refer to as the visibility of the architecture. The visibility of the architecture is limited (Curto-Millet & Shaikh, 2017), and it can change in different phases of the OSS development process, for example, due to release cycles and the branching of the source code (Shaikh & Vaast, 2016). Reduced visibility disrupts coordination activities because it renders many developers oblivious to recently added functions; therefore, they cannot build on these functions. To account for limitations in visibility, this study also asks the following question: How does reduced visibility moderate artifact-based and authority-based coordination’s effectiveness in building OSS architectures with low propagation costs?

I examine these questions using a computational model (Dong, 2022; Harrison et al., 2007), which simulates the two coordination mechanisms developing an OSS architecture out of interdependent contributions. The architecture is formalized as a design structure matrix (DSM) (Baldwin & Clark, 2000; Eppinger, 1991), which facilitates measuring propagation costs.

This study contributes to two streams of the literature. First, the model extends the literature on coordination in OSS development (Howison & Crowston, 2014; Shaikh & Henfridsson, 2017), which has developed a deep understanding of the various ways to facilitate coordination but has largely remained silent about the impact of these forms, both in absolute terms and relative to each other, on the characteristics of the software or its performance (an exception is Lee et al., 2023). This study shows the impact of coordination on propagation costs as a performance-relevant characteristic of the software. This study also offers a new perspective on coordination, which I call focal-layered superposition. Second, the model sheds new light on the mirroring hypothesis literature (Colfer & Baldwin, 2016; MacCormack et al., 2006, 2012) by proposing an explanation of how coordination relates to software architectures. This explanation is notably simple, as it does not require any deliberate intervention by the organization to maintain mirroring.

![](/api/attachments/ZE2QU54P/fulltext/images/d842c73514e89aff384dab8cfcf653969c2d5cf622840fab8595dfa8d3e0bf50.jpg)

Figure 1. Research Model

## Research Framework and Theoretical Background

The focus of this study is the comparison of artifact-based and authority-based coordination in terms of their effectiveness in building low-propagation-cost OSS architectures out of interdependent contributions, as well as how this effect is moderated by architecture visibility (see Figure 1; see also Appendix A for an overview of the constructs).

## Software Architectures and Propagation Costs

The software architecture, specifically its propagation costs, is a critical indicator of OSS developer workload (Baldwin & Clark, 2000; Baldwin et al., 2014; MacCormack et al., 2006, 2012). In addition to its relevance for the developer workload, there are two major reasons to focus on the software architecture as a dependent construct. First, the architecture of a software system represents a very “clean” basis for assessing an OSS project’s outcome. In contrast to indicators such as downloads or ratings (e.g., Setia et al., 2020; Weng & Soh, 2023), which can be influenced by confounding factors external to the OSS project, such as the project’s reputation, the software architecture is a more straightforward and undistorted outcome measure. Second, the concept of software architecture provides a solid basis for formalization, as it can be represented as a DSM, which can be handled with linear algebra operations (Baldwin et al., 2014; Eppinger, 1991).

Propagation costs are an established measure (MacCormack et al., 2006), which is rooted in software engineering (Sharman & Yassine, 2004) and can be directly calculated based on a DSM. Propagation costs are indicative of the effort required to maintain and further develop a software system (Mo et al., 2018). Higher propagation costs correlate with the number of activities required to implement a change (Xiao et al., 2022). As maintenance makes up a large share of the workload in the software lifecycle, reducing maintenance effort is a worthwhile goal in software development. Moreover, it is particularly important in OSS development (Amrit & van Hillegersberg,

2010), as contributions are largely voluntary and developers are often discouraged by any additional and unexpected effort required. Therefore, propagation costs have been used as a measure of modularity (MacCormack et al., 2012) and an indicator of the ability to react to uncertainties and changes in the environment, such as the software ecosystem.

Formally, propagation costs reflect the number of functions in the architecture that are directly and indirectly affected when one function is modified (Baldwin et al., 2014; MacCormack et al., 2012). Propagation costs can be directly calculated based on a DSM. Figure 2 illustrates propagation costs using an architecture consisting of five functions (labeled 1, ..., 5) represented as a graph (left) and a DSM (right). To calculate propagation costs (Sharman & Yassine, 2004), all the shortest dependency paths are counted and divided by the matrix size. The paths of the length of 1 are represented by the arrows in the graph (corresponding to the 1s in the DSM), which are four in number (1 → 2, 2 → 3, 2 → 5, 3 → 4). The paths with a length of 2 are three in number $( 1  2  3 , 1  2  5 , 2  3  4 )$ and there is only one path with a length of 3 (1 → 2 → 3 → 4). Also, each function’s self-reference is considered, and there are five of these $( 1  1 , . . . , 5  5 )$ . Overall, this results in a value of $( 4 + 3 + 1 + 5 ) / 5 ^ { 2 } = 0 . 5 2$

## Contributions and Contribution Interdependence

A contribution is the elementary unit of OSS development. Contributions are similar to what has been referred to as a task or patch (Howison & Crowston, 2014; Puranam et al., 2012), but to emphasize that they represent only a potential and are not necessarily integrated into the OSS, the term contribution is chosen here. Contributions are merely conceived of by the developers as a conceptual solution that enables a specific function, but they are not yet coded or implemented. The developers will only code and submit them if they add value (Howison & Crowston, 2014). To maintain simplicity, it is assumed that each contribution offers exactly one function. However, contributions of the same function can often be designed in different ways; thus, there is the possibility of alternative solutions or workarounds.

![](/api/attachments/ZE2QU54P/fulltext/images/1818593d08bf93136e07056ebef0ea403ce2c52d84c96dd812ce569fcde54e50.jpg)  
Figure 2. Example Describing the Calculation of Propagation Costs

Contributions are often interdependent, which means that one contribution’s function builds on other functions; more precisely, “two tasks [contributions] are interdependent if the value generated from performing each is different when the other task [contribution] is performed versus when it is not. The tasks [contributions] are independent if the value from performing each is the same whether the other task [contribution] is performed or not” (Puranam et al., 2012, p. 421). Accordingly, the degree of contribution interdependence is defined as the number of functions that a contribution’s function (as it is conceived of by a developer before it is coded and committed to the OSS) depends on. The degree of contribution interdependence is a characteristic of the underlying problem that the OSS aims to solve (the aspired-to software system). For example, an operating system manages access to hardware and software resources, un/blocking them dynamically, which is a relatively complex problem, whereas a text processor tackles a simpler underlying problem (MacCormack et al., 2012). Thus, when developing the former relative to the latter, a developer will conceive contributions with more interdependencies.

Overall, differentiating between the degree of contribution interdependence (the underlying problem), the outcome (the architecture and its propagation costs), and how the outcome is achieved (the coordination form) makes it possible to isolate the effect of the form of coordination on the architecture (see again Figure 1). The empirical literature has approximated this differentiation by matching pairs of software programs, with each pair consisting of an OSS and a proprietary software program with the same underlying problem (purpose), for example, MySQL and BerkelyDB as database management systems and Abiword and StarWriter (OpenOffice) as textprocessing software programs (MacCormack et al., 2012).

## Coordination in Open Source Software Development

The presence of interdependencies between contributions creates the need for coordination (Howison & Crowston, 2014; Malone & Crowston, 1994). Empirical research has shown that the ways in which developers’ contributions are coordinated to collectively build software differ fundamentally across OSS projects, with centralized, authority-based organizing as one archetype and flat, decentralized organizing using the artifact as the basis for coordination as the other (Crowston & Howison, 2006; Howison & Crowston, 2014; Lindberg et al., 2016; Medappa & Srivastava, 2019; Shaikh & Henfridsson, 2017).

In the following, it is theorized that a critical difference between the two forms is the absence or presence of predictive knowledge, which is defined as “knowledge that enables one agent to act as though he or she can accurately predict another agent’s actions” (Puranam et al., 2012, p. 420). Only authority-based coordination can make use of predictive knowledge, whereas it is absent from artifact-based coordination, and developers, consequently, cannot make reliable commitments to one another.

## Authority-Based Coordination

Authority-based coordination describes OSS projects that rely on governance structures with a central authority to facilitate coordination (Collier et al., 2010; Dahlander & O’Mahony, 2011; Shah, 2006). Howison and Crowston (2014) call this form of coordination “co-work” or “co-production.” Examples are Apache, Linux Kernel, and Debian (O’Mahony & Ferraro, 2007). The authority can be a senior or founding member (e.g., a “benevolent dictator,” Linus Torvalds in the case of Linux Kernel; see Shaikh & Henfridsson, 2017) or a senior developer who is employed by the company along with multiple others reporting to that senior developer (Agerfalk & Fitzgerald, 2008; Dahlander & Wallin, 2006; Germonprez et al., 2017; Kendall et al., 2019). Situations in which an authority coordinates contributions also occur in the context of inner-organizational OSS development (Buchner & Riehle, 2023; Capraro & Riehle, 2016).

The key characteristic of authority-based coordination is the presence of predictive knowledge. Predictive knowledge resolves the dependence between a contribution and a required but not implemented function as soon as a contribution with the required function is conceived because the authority can solicit a credible commitment from the developer. Consequently, developers’ commitment to providing their contributions is ensured as if these contributions were independent—as if all preconditions were already fulfilled (Puranam et al., 2012)—even though the required function is not yet implemented.

## Artifact-Based Coordination

In contrast to authority-based coordination, more recent organizational theory suggests that online coordination does not necessarily require intervention in developers’ activities. Instead, coordination is artifact based, meaning the common work artifact is used as the only means of coordination. In other words, for OSS developers, the artifact is the sole basis for contributing, and their contributions, in turn, alter the artifact. GNOME and BibDesk are examples of OSS projects with largely autonomous and decentralized acting developers (Dahlander & O’Mahony, 2011; Howison & Crowston, 2014). Despite the simplicity of this form of coordination, remarkably elaborate outcomes can be created (Bolici et al., 2016; Crowston et al., 2005; Howison & Crowston, 2014; Medappa & Srivastava, 2019).

Artifact-based coordination is appealing because it grants the developers the maximum autonomy and self-efficacy, thus boosting their motivation (Kankanhalli et al., 2005; Ke & Zhang, 2010). It is also theoretically intriguing because it can be rooted in environmentally mediated coordination, known as stigmergy (Heylighen, 2016), which has been used as the theoretical foundation of coordination in OSS development (Bolici et al., 2016; Dipple et al., 2014) and, more generally, crowdsourced problem solving (Majchrzak et al., 2021). The notion of open superposition (Howison & Crowston, 2014; Medappa & Srivastava, 2019) is a prominent form of artifactbased coordination and likewise defined as coordination based on the artifact in which developers are not aware of one another’s current activities or plans.

The key characteristic distinguishing artifact-based coordination from authority-based coordination is the absence of predictive knowledge. Interdependence is managed through deferral instead; that is, if the artifact does not provide the required functions, the developer will wait with her contribution until the required functionality is implemented; as Howison and Crowston (2014, p. 34) put it, from the developer’s perspective: “[Others’] commitment was unpredictable [and] I did not want to rely on their portion of shared work being completed.”

## Illustration Distinguishing Authority-Based and Artifact-Based Coordination

The following illustration juxtaposes the two coordination forms and the role of predictive knowledge. In an authoritybased coordination regime, Linus works on an OSS project, which develops a reference management program. Tove is employed by a company to work on the reference management program. Linus has the idea for a contribution that extends the program with a function allowing users to upload references to a social media website. Linus’s contribution requires a data transmission protocol (another function), which Linus cannot develop. Linus submits his need for the data transmission protocol to a community board, and a manager in the company finds the function to be valuable; thus, the manager instructs Tove to implement the transmission protocol and adds a note to the board indicating that it has been taken care of and when it will be available. Linus can immediately begin to develop his upload function because he can rely on the commitment that Tove’s contribution will be available. Put simply, he has predictive knowledge.

In contrast, in the artifact-based coordination regime, Emmanuele and Marta face the same situation. Emmanuele also wants to add the same upload feature to a reference management program, but he, like Linus, cannot develop the required transmission protocol. Marta, like Tove, has expertise in transmission protocols, but there is no authority to make her build the required protocol. The ability to communicate using a community board does not change this circumstance, as she cannot make a credible commitment to finish the protocol by a certain time (cf. Howison & Crowston, 2014, p. 34). Thus, Emmanuele will wait until Marta or someone else has implemented the transmission protocol. He defers his contribution.

## The Degree of Visibility of the Artifact’s Architecture as a Moderating Condition

The visibility of the architecture is a potential condition moderating how the coordination mechanisms transform interdependent contributions into a software architecture. The degree of visibility defines the parts of the architecture that can be seen and, therefore, built on by the developers. In OSS development, as well as in any kind of collective development, it is critical for developers to know which functions are present (Dabbish et al., 2012; Howison & Crowston, 2014), or as Majchrzak and Malhotra (2013) put it, “an architecture affording knowledge evolution allows anyone to see what knowledge has been collectively generated thus far” (p. 265). Thus, imperfect visibility can be seen as an obstacle, especially when coordination is based on the artifact.

In development practice, visibility is often limited. This leads to delays, which occur because contributions are typically not immediately integrated. Rather, they must be run through assessments or other kinds of approval procedures, which take time. If they pass, they become part of the artifact, but until then, they cannot be seen by other developers; thus, visibility is temporarily reduced. Shaikh and Vaast (2016) refer to such a delay in visibility as the process of “folding” and “unfolding” in OSS development.

Two fundamental mechanics delay visibility in OSS projects. First, when code is branched off from the main repository by a developer to work on it, that developer is cut off from the changes in the main branch until she has finished her coding work and a core developer (one with commit rights) has accepted the changes and, thus, integrated—pulled—them into the software system. In the same way, others are oblivious to her changes during that period. Thus, functions added after branching are not visible until merging occurs (e.g., Pastore et al., 2017). Second, releases, specifically the time between releases, can reduce visibility temporarily. A release is the distribution of a stable and tested version of the OSS to its users (Fogel, 2022; Michlmayr et al., 2015). Releases can be scheduled in regular time intervals (time-based) or after a certain set of features is developed (feature-based). Especially when the developers are also users of the software, they are typically only aware of the functions in the current system, and functions that have been developed since the latest software release will be less considered in terms of building on. In sum, collaborative OSS development is typically subject to temporal, cyclical changes in the visibility of the software artifact’s architecture (Shaikh & Vaast, 2016).

## Model

To formalize how the two coordination mechanisms build a software architecture out of interdependent contributions, given different degrees of visibility, and measure the architecture’s propagation costs, I developed a computational model. Computational models make it possible to investigate processes and identify mechanisms that cannot be empirically observed (Harrison et al., 2007). This is essential in examining coordination isolated from confounding effects. Computational models can also establish causality and overcome endogeneity, which helps to set focus on the effect of the coordination regimes while blending out other effects, such as potential reciprocal effects between the architecture and the selection of coordination mechanisms. The model does not require representations by agents, as in the agentbased paradigm; instead, it represents the two coordination mechanisms as procedures that try to integrate interdependent contributions into a software architecture.

## Model Components

The model consists of two components: (1) the software architecture and (2) contributions.

The Software Architecture Formalized as a Design Structure Matrix (DSM)

The artifact architecture represents a software system and is formalized as a DSM (Baldwin & Clark, 2000; Eppinger, 1991). A DSM is a squared matrix in which each row (mirrored in the columns) contains or is reserved for a specific function. The matrix defines the dependencies of that function; 1 (0) indicates the row function’s (in)dependence on the respective column function. Figure 3 shows an example of a DSM with 10 possible functions. Functions 3, 6, and 7 are implemented. Function 3 requires Function 7. Function 6 has no requirements, and Function 7 requires Function 6.

## Contributions

A contribution is a solution proposed to provide a specific, valuable function (MacCormack et al., 2006); consider, for example, a file providing a specific feature (see also Appendix A). A contribution’s function can require other functions. Technically, each contribution is formalized as (1) a function and (2) a dependency structure (see Figure 4).

(1) The contribution’s function is represented as an integer. It is assumed that there are 100 different potential functions labeled by the identifiers 1, ..., 100 (note for illustration purposes that Figure 3 has only 10 potential functions). The label determines the row in the DSM into which the contribution fits. This set of possible functions represents the imperfectly anticipated overall functionality that the software is intended to provide (i.e., the aspiration for the software system). Put simply, all functions that have the potential to add value to the software system.

(2) The contribution’s dependency structure is a vector indicating the required functions. For each possible function, the vector contains one element (0 or 1), which indicates whether the focal contribution’s function depends on the respective function (the self-reference is included, so the dependency structure of a contribution with function x has a 1 in the x<sup>th</sup> position). The expected number of 1s is determined by the parameter degree of contribution interdependence (see below). If implemented, the contribution’s dependency structure is written in the corresponding row of the DSM (see again Figure 3).

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>2</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>3</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>5</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>8</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>9</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>10</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr></table>

Figure 3. Illustration of the Software Architecture as a DSM

Formalization:

Example:

Empirical equivalence of the example:

<table><tr><td colspan="2">Contribution</td></tr><tr><td>Function{1,...,100}7</td><td>Dependency structure{0|1}1000 1 0 0 1 0 1 0 0 0 0 1 0 1 0 0 0 ...</td></tr><tr><td>File “7”sqr(val):return val^2</td><td>Import “2”Import “5”Import “12”Import “14” ...</td></tr></table>

Figure 4. A Contribution Contains a Function and a Dependency Structure; a File is the Empirical Equivalent

## Model Process

Each simulation run begins with an empty architecture (i.e., the DSM contains no functions). In each time step, a set of contributions is randomly generated, and the coordination mechanisms attempt to integrate these contributions into the DSM.

## Model Parameters

The model considers three parameters (see also Appendix A): (1) the degree of contribution interdependence, (2) the coordination mechanism (artifact-based or authority-based), and (3) the degree of visibility of the architecture. All remain constant throughout a simulation run.

## Degree of Contribution Interdependence

The degree of contribution interdependence is formalized as the probability for each element in a contribution’s dependency structure to be 1 (instead of 0), which means that the contribution’s function depends (or does not depend) on the function represented by this vector element. The higher the degree of contribution interdependence, the more requirements the contribution’s functions have. For example, a value of 0.1 means that the contribution’s dependency structure consists of approximately 10% 1s and 90% 0s (robustness checks that constrain how the 1s are distributed over the dependency structure vector indicate the insensitivity of the model results).

## Coordination Mechanisms: Authority-Based and Artifact-Based Coordination

In authority-based coordination, one contribution is selected from the set of available contributions created in each time step. This contribution is assumed to be the first to come to the authority’s awareness, and an attempt is made to integrate it. If the contribution requires a function that is not in the DSM, the required function is searched for among the other available contributions. If a contribution with the required function can be found, the required functions of that contribution are searched for in the DSM and, if not found there, in the available contributions via a recursive process. The contributions are only implemented (all at the same time) if all required functions are found in the DSM or the set of available contributions. If not all required functions can be found, the implementation of another contribution within the set of available contributions is tried. If multiple contributions with the same function are available, a temporal order within the current time step is assumed, which determines the order in which they are tried. (Robustness checks with alternative operationalizations, e.g., maximizing or minimizing the number of contributions to be integrated, show the insensitivity of the model results.)

This process is repeated until a contribution and its required contributions can be implemented or all available contributions have been unsuccessfully tried. In the latter case, no implementation takes place. The intuition behind authority-based coordination is that the mechanism can make use of predictive knowledge (Puranam et al., 2012) if the solutions for the required functions are available in the form of contributions, as in the example of Linus and Tove.

Artifact-based coordination can capture all available contributions for which all requirements are implemented in the DSM. If multiple contributions with the same function are available, a temporal order within the time step is assumed and the first contribution in this order whose all requirements are fulfilled will be implemented in the same way as under authority-based coordination. In contrast to authority-based coordination, however, the other contributions in the available set of contributions cannot be used to satisfy functional requirements that are not provided by the DSM. However, artifact-based coordination allows all available contributions to be implemented in parallel if their functional requirements are fulfilled by the DSM. This represents fully autonomous contributors working independently and in parallel.

The intuition behind artifact-based coordination is the absence of predictive knowledge (Puranam et al., 2012), as in the example of Emmanuele and Marta. Available contributions cannot be coordinated with one another, and only the artifact (DSM) can serve as the basis for coordination (Bolici et al., 2016; Howison & Crowston, 2014; Medappa & Srivastava, 2019).

## Degree of Visibility

The degree of visibility is modeled by delaying when parts of the DSM can be built onto it. The standard setting is the immediate visibility of new functions (i.e., full visibility), which means that a function can be built onto it beginning with the next time step after its implementation. Delayed visibility means that the DSM is updated only at certain intervals, which are measured in time steps. For example, if the degree of visibility is 1/50, the update occurs each 50th time step. In time steps 1 to 49, the attempted implementations of contributions can only build on the functions in the DSM as of time step 1. In time steps 50 to 99, they can only build on the functions as of time step 50. (Robustness checks with feature-based instead of this time-based modeling of these delays show the insensitivity of the model results.)

## Findings

The simulations were run until the DSM was completed. All combinations of the coordination mechanisms {artifact-based, authority-based} with the settings for the degree of contribution interdependence [0.005, …, 0.080] and the degree of visibility {full, 1/50} were simulated. The chosen spectrum for the degree of contribution interdependence ensures that complete DSMs are produced within 1,000 time steps. The results are averages of 100 repeated simulation runs for each combination of settings. The number of contributions available in each time step was set to 100. (Robustness tests show the insensitivity of the model results to a wide range in terms of the number of contributions [5, …, 150] and delay frequencies [1/25, …, 1/100].)

The model yields two major findings. (1) Under artifactbased coordination, as compared to authority-based coordination, architectures have notably lower propagation costs. More precisely, artifact-based coordination produces a linear relationship with the degree of contribution interdependency, while authority-based coordination creates an over-linear increase in propagation costs. (2) Delayed visibility reduces propagation costs, an effect I refer to as focal-layered superposition.

![](/api/attachments/ZE2QU54P/fulltext/images/75116e2c13de81a431b973e7e5e927085226b77d51615ccbc7450364ca8379fe.jpg)  
Figure 5. Relationship between Contribution Interdependence and Propagation Costs Under the Two Coordination Mechanisms

## Artifact-Based vs. Authority-Based Coordination

The effects of the two coordination mechanisms on the relationship between the degree of contribution interdependence and the architecture’s propagation costs differ strongly (Figure 5). Under artifact-based coordination (circles), there is a small, linear increase in propagation costs with increasing contribution interdependence. In contrast, authority-based coordination (triangles) leads to a much steeper curve. Throughout the entire spectrum of contribution interdependence, artifact-based coordination produces lower propagation costs than authority-based coordination. More precisely, the former is more effective in transforming contributions with a given degree of interdependence into a sparse software architecture with low propagation costs.

The difference in propagation costs is driven by authoritybased coordination’s ability to implement interdependent contributions. These interdependent functions create more and, especially, longer propagation paths in the DSM when implemented. Thus, with each integration, the architecture grows a new layer of relatively interdependent functions. Building on the metaphor of superposition (Howison & Crowston, 2014), this layer can be characterized as relatively tight. In contrast, artifact-based coordination adds loose layers, which are only coupled to the deeper functions from previous implementations, not within the layer.

Proposition 1a: When coordinating interdependent contributions into a software architecture, artifact-based coordination creates lower propagation costs than authority-based coordination throughout the spectrum of contribution interdependence.

By adding relatively loose layers on top of each other, artifact-based coordination creates a linear overall relationship between the degree of contribution interdependence and propagation costs. In contrast, authority-based coordination leads to an over-proportional relationship, with a rapid incline that levels off before reaching its maximum. The reason for this over-proportional relationship is that long propagation paths are integrated into the DSM even at medium degrees of contribution interdependence. These long paths over-proportionally boost propagation costs. With further increases in the degree of contribution interdependence, the propagation paths become more numerous but not longer.

Proposition 1b: When coordinating interdependent contributions into a software architecture, artifact-based coordination creates a linear relationship between the degree of contribution interdependence and the software architecture’s propagation costs.

Proposition 1c: When coordinating interdependent contributions into a software architecture, authority-based coordination creates an over-proportional relationship between the degree of contribution interdependence and the software architecture’s propagation costs.

## Delayed Visibility of the Architecture and Focal-Layered Superposition

Next, I turn to the visibility of the architecture by setting the degree of visibility to 1/50; thus, the DSM is updated only every 50th time step instead of the immediate updating that has been assumed until this point.

Figure 6, surprisingly, shows that delaying visibility decreases propagation costs. Delayed visibility, as compared to full visibility, shows lower overall propagation costs under authority-based coordination (empty triangles vs. solid triangles in Figure 6a). Under artifact-based coordination, the already small extent of propagation costs is further reduced (empty circles vs. solid circles).

The relative reduction is, in general, stronger under artifactbased coordination than under authority-based coordination (57.6% vs. 39.7% throughout the spectrum of contribution interdependence).<sup>2</sup> Only at very low degrees of contribution interdependence is the relative reduction stronger under authority-based coordination because there is a certain level of propagation costs that cannot be undercut by artifact-based coordination (see Figure 6b).

Proposition 2a: Delayed visibility decreases the software architecture’s propagation costs under both coordination mechanisms.

Proposition 2b: The reduction of propagation costs through delayed visibility is stronger under artifact-based coordination than under authority-based coordination except when there is a low degree of contribution interdependence.

The reason for the decline in propagation costs with delayed visibility is an effect that I refer to as focal-layered superposition. While regular open superposition describes the adding of functions as layers in which current and deeper layers enable the functionality on which future layers build (Howison & Crowston, 2014), focal-layered superposition is the process of adding layers that connect only to layers beyond a certain minimum depth, not the most recently added layers. On top of the recent layers of the architecture, which are inaccessible to build on because of a lack of visibility, functions become loosely stacked, and couplings exist only with the visible (deeper) parts. Thus, under focallayered superposition, dependencies are unequally distributed, in contrast to regular open superposition, in which the entire architecture is assumed to be open and dependencies are thus more uniformly distributed. Put simply, delayed visibility causes focal-layered superposition because it renders the deeper layers the only basis to build on.

Figure 7 illustrates the layering dynamics of focal-layered superposition as a result of delayed visibility. Full visibility, in which all functions of the architecture are accessible, leads to regular open superposition (Figure 7a). The functions of Contributions 6, 2, and 3 can be implemented because their requirements (Functions 1, 5, and 8) are visible. In contrast, under delayed visibility (Figure 7b), only the functions in the visible layer (at the bottom, i.e., Functions 1, 9, and 8) can serve as a basis to build on, not the functions in the invisible layer (Functions 5 and 4). The function of Contribution 6 cannot be implemented because Function 5, which is required, is hidden; instead, Contribution 6’, which is a workaround of Contribution 6 with the same function but requiring Function 1 instead of Function 5, is implemented. Contribution 6’ is not implemented under full visibility, as shown in Figure 7a, because Contribution 6 was conceived of first. Thus, delayed visibility leads to the funneling of new dependencies to the visible layer and away from the invisible layer. This reduces propagation costs significantly.<sup>3</sup>

Focal-layered superposition applies to any coordination form that uses the artifact, not only artifact-based coordination but also authority-based coordination. However, the exclusive reliance on the architecture as the basis for coordination under artifact-based coordination makes the effect of focal-layered superposition stronger and explains the larger relative impact on propagation costs (see Proposition 2b).

![](/api/attachments/ZE2QU54P/fulltext/images/6df8ac815a7dac4152fbc5962b96386aa28df9178a9b684c14e4664aa6d4bc0e.jpg)

(b) Percentage differences in propagation costs  
![](/api/attachments/ZE2QU54P/fulltext/images/0ad3c2a9a31ec7bc707aae4b63d73fb48801fc2074193bcbeae5a7dcc5f482ca.jpg)

authority, full

authority, delayed

artifact, full

--artifact, delayed

\- artifact-based, relative difference

authority-based, relative difference

![](/api/attachments/ZE2QU54P/fulltext/images/8eedc38945fa967a4c9de30a75e42a6571cb97f984df3efc977722fccd610f1a.jpg)

![](/api/attachments/ZE2QU54P/fulltext/images/4c3eace15fe7b3d961e575b5c1197b97eddd53c8b2ef71c869974e226b3ed5ad.jpg)  
Figure 7. (a) Full Visibility and Regular Open Superposition and (b) Delayed Visibility and Focal-Layered Superposition

## Discussion

This study examined how artifact-based and authority-based coordination compare in building OSS architectures with low propagation costs from interdependent contributions and how visibility influences this effect. The model showed that—and how—artifact-based coordination produces architectures with lower propagation costs (Propositions 1a-c). Delayed visibility reduces propagation costs (Propositions 2a-b) through focal-layered superposition.

## Implications for Theory

Most fundamentally, this study is intended to provide insights regarding lightening OSS developers’ workload by reducing the propagation costs of the software architecture, providing a complementary view and adding to the literature on OSS developers’ motivations (Daniel et al., 2018; Malgonde et al., 2023; Maruping et al., 2019; Medappa & Srivastava, 2020). Specifically, this study contributes to two literature streams: that on coordination in OSS development and that on the mirroring hypothesis.

## Contribution to the Literature on Coordination in Open Source Software Development

The literature on coordination in OSS development is extended in multiple ways. First, although this literature has uncovered a large variety of coordination and governance forms across OSS projects (Maruping & Matook, 2020; Medappa & Srivastava, 2018; O’Mahony & Ferraro, 2007) and investigated their power and limitations in terms of meeting the need to manage interdependencies (Howison & Crowston, 2014; Lindberg et al., 2016; Shaikh & Henfridsson, 2017), there is not a sufficient understanding of how the different coordination forms relate to performance-relevant OSS project outcomes. This study focuses on propagation costs as a performance-relevant factor resulting from coordination activities and demonstrates that the different coordination forms have strong impacts.

Second, the coordination literature has identified software architectures as a relevant basis for coordination (Bolici et al., 2016; Howison & Crowston, 2014; Medappa & Srivastava, 2019, 2020) but much less so as an outcome of coordination activities. This study emphasizes the architecture as a dependent construct subject to coordination activities.

Third, this study sheds new light on the workings of the coordination mechanisms and their dynamics by integrating temporal changes in visibility and openness (Shaikh & Vaast, 2016). Specifically, this study draws a more complete picture of coordination by proposing the notion of focal-layered superposition and its effects on the software architecture, implying that the process of open superposition changes with imperfect visibility. Focal-layered superposition also demonstrates that strong macrolevel effects (different software architectures) can emerge as a result of microlevel mechanisms and interactions.

Finally, it is worth mentioning that the model demonstrates the effectiveness of coordinating exclusively through an artifact. This demonstration informs our understanding of minimal coordination and self-organization in OSS development and other forms of open collaboration and crowdsourcing, which have been described and widely discussed (Crowston et al., 2007; Howison & Crowston, 2014; Kudaravalli & Faraj, 2008; Majchrzak et al., 2021; Medappa & Srivastava, 2019).

## Contribution to the Literature on the Mirroring Hypothesis

The insights derived from this study also contribute to the literature on software architectures (Baldwin et al., 2014; MacCormack et al., 2006, 2012), specifically the mirroring hypothesis, which suggests that there is coherence between organizational structures and software (and product) architectures (Colfer & Baldwin, 2016; Conway, 1968). Accordingly, flat organizational structures correspond to sparse system architectures, while hierarchical and authority-based structures correspond to more intertwined architectures. However, research on the mirroring hypothesis has struggled to find consistent empirical support, and a lack of understanding regarding its underlying mechanisms has been frequently mentioned as the reason for this shortcoming (Cabigiosu & Camuffo, 2012; Colfer & Baldwin, 2016; Mattarelli et al., 2022).

Contributing to this research, this study provides detailed insights into the mechanisms involved, including their causality. The model supports the claim that there is a correspondence by demonstrating that artifact-based coordination, as compared to authority-based coordination, is related to lower propagation costs, thus upholding the known correlational evidence for the mirroring hypothesis (Baldwin et al., 2014; MacCormack et al., 2006, 2012). Beyond that, this study proposes an explanation for correspondence in the form of an underlying causal mechanism. It sheds light on how the implementation of interdependent “chunks” of contributions creates tight layers in the architecture, as driven by authority-based coordination with predictive knowledge, versus the implementation of contributions independent of one another, which creates loose layers in the architecture, as driven by artifact-based coordination without predictive knowledge. Overall, these mechanisms provide a simple explanation for the correspondence between organizational conditions and outcomes.

Furthermore, this mechanism provides an interesting perspective on the literature that has, explicitly and implicitly, suggested that mirroring results from deliberate design efforts to align organizations and product architectures (Cabigiosu & Camuffo, 2012; Colfer & Baldwin, 2016; Sanchez & Mahoney, 1996). In contrast, this study demonstrates that design efforts and other deliberate interventions on the part of the organization, other than choosing the coordination regime, are not necessarily required to achieve and maintain mirroring. Thus, this study provides a naturalistic explanation for the mirroring hypothesis.

## Implications for Practice

Practitioners who organize based on authority to produce OSS should be aware that their coordination activities can increase propagation costs. This can have a negative effect in that it might become more difficult to attract new voluntary contributors from outside the company. Therefore, they are encouraged to use artifact-based coordination to reduce propagation costs. Practitioners can also use release strategies deliberately, as delayed visibility is helpful in reducing propagation costs.

## Limitations and Future Research

Although this study has overcome challenges posed by the empirical literature, follow-up research on real-world OSS projects is needed to gain a more complete understanding of evolving software architectures. In particular, the results of this study suggest the need for empirical investigations into the process of focal-layered superposition and the influence of visibility and openness policies.

As with any model, this model represents a specific, simplified view of reality, thereby ignoring other aspects. Reducing the underlying problem to the degree of contribution interdependence is a simplification worth pointing out. Future research could theorize about and empirically investigate other factors that characterize the underlying problem and influence the effect of coordination on the software architecture. More specifically, the notion of an aspired-to software system could stimulate follow-up research. My model does not account for (partly) prespecified architectures, as this assumption is more appropriate for proprietary software projects. Instead, the model describes a typical setting for OSS projects, which have often been seen as deliberately “incomplete by design” in order to facilitate “the capacity to incorporate functionality relatively easily … and maintaining abstractness in goal definition” (Garud et al., 2008, p. 360). Thus, my model is less suitable for proprietary software development, and generalization to such a context is not intended.

Another simplification is that the model portrays predictive knowledge as either fully present or fully absent. This simplification is helpful for shedding light on the mechanisms (Puranam et al., 2012), but it ignores the possibility that some degree of predictive knowledge can form over time without the presence of an authority. When developers begin to learn about one another’s work habits, trust can emerge, and reliable commitments can be made to some extent. At the same time, authorities in the real world are limited in terms of identifying interdependencies and coordinating between developers; thus, the assumed perfect rationality of authority-based coordination is also a simplification worth pointing out.

The model ignores some conditions that may influence the effectiveness of coordination mechanisms, such as the development environment, including the programming language(s) used. Future research on how the development environment shapes perceptions of the problem that the software is intended to solve and its interdependencies would be highly promising. Programming languages vary in terms of their features, paradigms, and libraries, which impact how contributions are implemented. Programming languages have different levels of support for encapsulation. Some languages provide extensive built-in libraries and packages, which shape developers’ perception of the problem and their ability to reuse code. These factors influence the notion of the degree of contribution interdependence.

Future research should also investigate changes in the coordination form over time. It is likely to be useful to involve authority-based coordination to a larger extent at the beginning of the development of a technical system, and when the technology has reached a certain level of growth, authorities may be needed to a lesser extent. Empirical research documents similar patterns (Shaikh & Henfridsson, 2017). Linking such changes to propagation costs or other aspects of the architecture could help to manage software architectures better.

Future modeling research can challenge theoretically established conditions for artifact-based coordination other than visibility—for example, irrevocable openness (Howison & Crowston, 2014). Revoking parts of the software code because of legal disputes, for instance, would not only affect the software architecture directly but would also require certain qualities on the part of the coordination regime to be able to fix such issues. Perhaps the top-down approach of authority-based coordination is preferable under such conditions; alternatively, artifact-based coordination may handle such challenges better.

Finally, the sole focus on propagation costs as the dependent construct in this study ignores other important outcomes of coordination. For example, as unreported simulations have shown, artifact-based coordination limits the range of possible systems that can be developed, while authority-based coordination can handle higher degrees of contribution interdependence and is thus useful for a broader range of systems. When managing coordination, multiple outcomes— not only propagation costs—must be considered, some of which may conflict with each other.

## Conclusion

Software architectures with low propagation costs are deemed critical for the viability of OSS development, as they reduce OSS developers’ workload. In a computational model, I compare artifact-based and authority-based coordination as two archetypes of OSS coordination in building a DSM, which represents a software architecture, out of interdependent contributions. The model shows that artifact-based coordination, relative to authority-based coordination, is a powerful mechanism for reducing the propagation costs of the software architecture. The model also reveals the process of focal-layered superposition, which extends the notion of open superposition (Howison & Crowston, 2014) and sheds new light on dynamics and conditions in terms of how software architectures emerge.

## Acknowledgments

I thank senior editor Likoebe Maruping, the anonymous associate editor, and the three anonymous reviewers for their constructive feedback, which has tremendously enhanced the quality of this work. My gratitude for feedback and discussions also goes out to Oliver Alexy, Carliss Baldwin, Joachim Henkel, Ann Majchrzak, David Reetz, and Manuel Trenz. I also thank the participants in the BEWIP Seminar at the Technical University of Munich, the SOD Seminar at the University of Southern Denmark, and ICIS 2018 in San Francisco, where earlier versions of this work were presented.

## References

Agerfalk, P. J., & Fitzgerald, B. (2008). Outsourcing to an unknown workforce: Exploring opensourcing as a global sourcing strategy. MIS Quarterly, 32(2), 385-409. https://doi.org/10.2307/25148845

Amrit, C., & van Hillegersberg, J. (2010). Coordination implications of software coupling in open source projects. In Proceedings of the 6th International IFIP WG 2.13 Conference on Open Source Systems (pp. 314-321). https://doi.org/10.1007/978-3-642-13244- 5\_25

Baldwin, C. Y., & Clark, K. B. (2000). Design rules: The power of modularity. The MIT Press.

Baldwin, C. Y., MacCormack, A., & Rusnak, J. (2014). Hidden structure: Using network methods to map system architecture. Research Policy, 43(8), 1381-1397. https://doi.org/10.1016/ j.respol.2014.05.004

Becker, M. C., Rullani, F., & Zirpoli, F. (2021). The role of digital artefacts in early stages of distributed innovation processes. Research Policy, 50(10), 104349. https://doi.org/10.1016/j.respol. 2021.104349

Bolici, F., Howison, J., & Crowston, K. (2016). Stigmergic coordination in FLOSS development teams: Integrating explicit and implicit mechanisms. Cognitive Systems Research, 38, 14-22. https://doi.org/10.1016/j.cogsys.2015.12.003

Buchner, S., & Riehle, D. (2023). The business impact of inner source and how to quantify it. ACM Computing Surveys, 56(2), 1-27. https://doi.org/10.1145/3611648

Cabigiosu, A., & Camuffo, A. (2012). Beyond the “mirroring” hypothesis: Product modularity and interorganizational relations in the air conditioning industry. Organization Science, 23(3), 686- 703. https://doi.org/10.1287/orsc.1110.0655

Capraro, M., & Riehle, D. (2016). Inner source definition, benefits, and challenges. ACM Computing Surveys, 49(4), 1-36. https://doi.org/ 10.1145/2856821

Cataldo, M., & Herbsleb, J. D. (2013). Coordination breakdowns and their impact on development productivity and software failures. IEEE Transactions on Software Engineering, 39(3), 343-360. https://doi.org/10.1109/TSE.2012.32

Cataldo, M., Herbsleb, J. D., & Carley, K. M. (2008). Socio-technical congruence: A framework for assessing the impact of technical and work dependencies on software development productivity. In Proceedings of the 2nd ACM-IEEE International Symposium on Empirical Software Engineering and Measurement. https://doi.org/10.1145/1414004.1414008

Chengalur-Smith, I., Sidorova, A., & Daniel, S. L. (2010). Sustainability of free/libre open source projects: A longitudinal

study. Journal of the Association for Information Systems, 11(11), 657-683. https://doi.org/10.17705/1jais.00244

Clements, P., Kazman, R., & Klein, M. (2001). Evaluating software architectures: Methods and case studies. Addison-Wesley.

Colfer, L. J., & Baldwin, C. Y. (2016). The mirroring hypothesis: Theory, evidence, and exceptions. Industrial and Corporate Change, 25(5), 709-738. https://doi.org/10.1093/icc/dtw027

Collier, B., Burke, M., Kittur, N., & Kraut, R. (2010). Promoting good management: Governance, promotion, and leadership in open collaboration communities. In Proceedings of the International Conference on Information Systems.

Conway, M. (1968). How Do Committees Invent? Datamation, 14(5), 28-31.

Crowston, K., & Howison, J. (2006). Hierarchy and centralization in free and open source software team communications. Knowledge, Technology & Policy, 18(4), 65-85. https://doi.org/10.1007/ s12130-006-1004-8

Crowston, K., Wei, K., Li, Q., Eseryel, U., & Howison, J. (2005). Coordination of free/libre open source software development. In Proceedings of the International Conference on Information Systems.

Crowston, K., Li, Q., Wei, K., Eseryel, U. Y., & Howison, J. (2007). Self-organization of teams for free/libre open source software development. Information and Software Technology, 49(6), 564- 575. https://doi.org/10.1016/j.infsof.2007.02.004

Curto-Millet, D., & Shaikh, M. (2017). The Emergence of openness in open-source projects: The case of openEHR. Journal of Information Technology, 32(4), 361-379. https://doi.org/10.1057/ s41265-017-0042-x

Dabbish, L., Stuart, C., Tsay, J., & Herbsleb, J. (2012). Social coding in GitHub: Transparency and collaboration in an open software repository. In Proceedings of the ACM Conference on Computer Supported Cooperative Work. https://doi.org/10.1145/2145204. 2145396

Dahlander, L., & O’Mahony, S. (2011). Progressing to the center: Coordinating project work. Organization Science, 22(4), 961-979. https://doi.org/10.1287/orsc.1100.0571

Dahlander, L., & Wallin, M. W. (2006). A man on the inside: Unlocking communities as complementary assets. Research Policy, 35(8), 1243-1259. https://doi.org/10.1016/j.respol.2006. 09.011

Daniel, S. L., Agarwal, R., & Stewart, K. J. (2013). The effects of diversity in global, distributed collectives: A study of open source project success. Information Systems Research, 24(2), 312-333. https://doi.org/10.1287/isre.1120.0435

Daniel, S. L., Maruping, L. M., Cataldo, M., & Herbsleb, J. (2018). The impact of ideology misfit on open source software communities and companies. MIS Quarterly, 42(4), 1069-1096. https://doi.org/ 10.25300/MISQ/2018/14242

Dipple, A., Raymond, K., & Docherty, M. (2014). General theory of stigmergy: Modelling stigma semantics. Cognitive Systems Research, 31-32, 61-92. https://doi.org/10.1016/j.cogsys.2014.02.002

Dong, J. Q. (2022). Using Simulation in information systems research. Journal of the Association for Information Systems, 23(2), 408- 417. https://doi.org/10.17705/1jais.00743

Eppinger, S. D. (1991). Model-based approaches to managing concurrent engineering. Journal of Engineering Design, 2(4), 283- 290. https://doi.org/10.1080/09544829108901686

Fogel, K. (2022). Producing open source software: How to run a successful free software project (CreativeCommons Attribution-ShareAlike (3.0) license). http://producingoss.com/en/producingoss. html

Garud, R., Jain, S., & Tuertscher, P. (2008). Incomplete by design and designing for incompleteness. Organization Studies, 29(3), 351- 371. https://doi.org/10.1177/0170840607088018

Germonprez, M., Kendall, J. E., Kendall, K. E., Mathiassen, L., Young, B., & Warner, B. (2017). A theory of responsive design: A field study of corporate engagement with open source communities. Information Systems Research, 28(1), 64-83. https://doi.org/10.1287/isre.2016.0662

Haefliger, S., von Krogh, G., & Spaeth, S. (2008). Code reuse in open source software. Management Science, 54(1), 180-193. https://doi.org/10.1287/mnsc.1070.0748

Harrison, J. R., Lin, Z., Carroll, G. R., & Carley, K. M. (2007). Simulation modeling in organizational and management research. Academy of Management Review, 32(4), 1229-1245. https://doi.org/10.5465/AMR.2007.26586485

Heylighen, F. (2016). Stigmergy as a universal coordination mechanism I: Definition and components. Cognitive Systems Research, 38, 4-13. https://doi.org/10.1016/j.cogsys.2015.12.002

Howison, J., & Crowston, K. (2014). Collaboration through open superposition: a theory of the open source way. MIS Quarterly, 38(1), 29-50. https://doi.org/10.25300/MISQ/2014/38.1.02

Kankanhalli, A., Tan, B. C. Y., & Wei, K.-K. (2005). Contributing knowledge to electronic knowledge repositories: An empirical investigation. MIS Quarterly, 29(1), 113-143. https://doi.org/ 10.2307/25148670

Ke, W., & Zhang, P. (2010). The effects of extrinsic motivations and satisfaction in open source software development. Journal of the Association for Information Systems, 11(12), 784-808. https://doi.org/10.17705/1jais.00251

Kendall, K. E., Kendall, J. E., Germonprez, M., & Mathiassen, L. (2019). The third design space: A postcolonial perspective on corporate engagement with open source software communities. Information Systems Journal, 30(2), 369-402. https://doi.org/ 10.1111/isj.12270

Krueger, C. W. (1992). Software reuse. ACM Computing Surveys, 24(2), 131-183. https://doi.org/10.1145/130844.130856

Kudaravalli, S., & Faraj, S. (2008). The structure of collaboration in electronic networks. Journal of the Association for Information Systems, 9(10), 706-726. https://doi.org/10.17705/1jais.00172

Lee, J., Park, S., & Lee, H. (2023). Polyarchy and project performance in open, distributed forms of innovation. Strategic Organization. https://doi.org/10.1177/14761270221145567

Lindberg, A., Berente, N., Gaskin, J., & Lyytinen, K. (2016). Coordinating interdependencies in online communities: a study of an open source software project. Information Systems Research, 27(4), 751-772. https://doi.org/10.1287/isre.2016.0673

Liu, M., Hansen, S., & Tu, Q. (2021). Sustaining collaborative software development through strategic consortium. Journal of Strategic Information Systems, 30(3), Article 101671. https://doi.org/ 10.1016/j.jsis.2021.101671

MacCormack, A., Baldwin, C., & Rusnak, J. (2012). Exploring the duality between product and organizational architectures: A test of the “mirroring” hypothesis. Research Policy, 41(8), 1309-1324. https://doi.org/10.1016/j.respol.2012.04.011

MacCormack, A., Rusnak, J., & Baldwin, C. Y. (2006). Exploring the structure of complex software designs: An empirical study of open source and proprietary code. Management Science, 52(7), 1015- 1030. https://doi.org/10.1287/mnsc.1060.0552

Majchrzak, A., & Malhotra, A. (2013). Towards an information systems perspective and research agenda on crowdsourcing for innovation. Journal of Strategic Information Systems, 22(4), 257- 268. https://doi.org/10.1016/j.jsis.2013.07.004

Majchrzak, A., Malhotra, A., & Zaggl, M. A. (2021). How Open crowds self-organize. Academy of Management Discoveries, 7(1), 104-129. https://doi.org/10.5465/amd.2018.0087

Malgonde, O., Saldanha, T., & Mithas, S. (2023). Resilience in the open source software community: How pandemic and unemployment shocks influence contributions to others’ and one’s own projects. MIS Quarterly, 47(1), 361-390. https://doi.org/ 10.25300/misq/2022/17256

Malone, T. W., & Crowston, K. (1994). The interdisciplinary study of coordination. ACM Computing Surveys, 26(1), 87-119. https://doi.org/10.1145/174666.174668

Maruping, L. M., Daniel, S. L., & Cataldo, M. (2019). Developer centrality and the impact of value congruence and incongruence on commitment and code contribution activity in open source software communities. MIS Quarterly, 43(3), 951-976. https://doi.org/10.25300/misq/2019/13928

Maruping, L. M., & Matook, S. (2020). The evolution of software development orchestration: Current state and an agenda for future research. European Journal of Information Systems, 29(5), 443- 457. https://doi.org/10.1080/0960085x.2020.1831834

Mattarelli, E., Bertolotti, F., Prencipe, A., & Gupta, A. (2022). The Effect of role-based product representations on individual and team coordination practices: A field study of a globally distributed new product development team. Organization Science, 33(4), 1423- 1451. https://doi.org/10.1287/orsc.2021.1487

Medappa, P. K., & Srivastava, S. C. (2018). Restrictions in open source: A study of team composition and ownership in open source software development projects. In Proceedings of the International Conference on Information Systems.

Medappa, P. K., & Srivastava, S. C. (2019). Does superposition influence the success of FLOSS projects? An examination of opensource software development by organizations and individuals. Information Systems Research, 30(3), 764-786. https://doi.org/ 10.1287/isre.2018.0829

Medappa, P. K., & Srivastava, S. C. (2020). Ideological shifts in open source orchestration: Examining the influence of licence choice and organisational participation on open source project outcomes. European Journal of Information Systems, 29(5), 500-520. https://doi.org/10.1080/0960085X.2020.1756003

Michlmayr, M., Fitzgerald, B., & Stol, K.-J. (2015). Why and how should open source projects adopt time-based releases? IEEE Software, 32(2), 55-63. https://doi.org/10.1109/ms.2015.55

Mo, R., Snipes, W., Cai, Y., Ramaswamy, S., Kazman, R., & Naedele, M. (2018). Experiences applying automated architecture analysis tool suites. In Proceedings of the 33rd ACM/IEEE International Conference on Automated Software Engineering. https://doi.org/ 10.1145/3238147.3240467

O’Mahony, S., & Ferraro, F. (2007). The emergence of governance in an open source community. Academy of Management Journal, 50(5), 1079-1106. https://doi.org/10.5465/AMJ.2007.27169153

Pastore, F., Mariani, L., & Micucci, D. (2017). BDCI: Behavioral driven conflict identification. In Proceedings of the 11th Joint Meeting on Foundations of Software Engineering. https://doi.org/ 10.1145/3106237.3106296

Puranam, P., Raveendran, M., & Knudsen, T. (2012). Organization design: The epistemic interdependence perspective. Academy of Management Review, 37(3), 419-440. https://doi.org/10.5465/amr. 2010.0535

Research and Markets. (2020). Open source services market by industry, service type, and geography—Global forecast to 2026. https://www.researchandmarkets.com/reports/5185453/opensource-services-market-by-industry-service

Sanchez, R., & Mahoney, J. T. (1996). Modularity, flexibility, and knowledge management in product and organization design. Strategic Management Journal, 17(S2), 63-76. https://doi.org/ 10.1002/smj.4250171107

Setia, P., Bayus, B. L., & Rajagopalan, B. (2020). The takeoff of open source software: A signaling perspective based on community activities. MIS Quarterly, 44(3), 1439-1458. https://doi.org/ 10.25300/misq/2020/12576

Shah, S. K. (2006). Motivation, governance, and the viability of hybrid forms in open source software development. Management Science, 52(7), 1000-1014. https://doi.org/10.1287/mnsc.1060.0553

Shaikh, M., & Henfridsson, O. (2017). Governing open source software through coordination processes. Information and Organization, 27(2), 116-135. https://doi.org/10.1016/j.infoandorg.2017.04.001

Shaikh, M., & Vaast, E. (2016). Folding and unfolding: Balancing openness and transparency in open source communities. Information Systems Research, 27(4), 813-833. https://doi.org/ 10.1287/isre.2016.0646

Sharma, P. N., Daniel, S. L., Chung, T. (Rachel), & Grover, V. (2022). A motivation-hygiene model of open source software code contribution and growth. Journal of the Association for Information Systems, 23(1), 165-195. https://doi.org/10.17705/ 1jais.00712

Sharman, D. M., & Yassine, A. A. (2004). Characterizing Complex product architectures. Systems Engineering, 7(1), 35-60. https://doi.org/10.1002/sys.10056

Vial, G. (2023). A complex adaptive systems perspective of software reuse in the digital age: An agenda for IS research. Information Systems Research, 34(4), 1728-1743. https://doi.org/10.1287/isre. 2023.1200

Weng, Q., & Soh, F. (2023). The influence of project initiators’ personto-person followership on project popularity in open source communities: The role of reach and importance. Journal of Strategic Information Systems, 32(2), Article 101771. https://doi.org/10.1016/j.jsis.2023.101771

Xiao, L., Cai, Y., Kazman, R., Mo, R., & Feng, Q. (2022). Detecting the locations and predicting the maintenance costs of compound architectural debts. IEEE Transactions on Software Engineering, 48(9), 3686-3715. https://doi.org/10.1109/tse.2021.3102221

Zawinski, J. (1999). Resignation and postmortem. https://www.jwz. org/gruntle/nomo.html

## About the Author

Michael Zaggl’s research is on distributed and digital innovation. He is a full professor at NEOMA Business School in France. Before joining NEOMA Business School, he was an associate professor at Aarhus University and led a research group at the Technical University of Munich, TUM School of Management, where he also received a Habilitation degree. He received a Ph.D. from the Technical University of Hamburg and an M.Sc. and B.Sc. in Information Systems and Management from the University of Koblenz. He has won numerous awards, including the Academy of Management Best Conference Paper Award (CTO division) and the Jürgen Hauschildt Preis. His research has been published in leading innovation and information systems journals, e.g., Academy of Management Discoveries, Journal of the Association for Information Systems, Research Policy, and Strategic Management Journal. ORCID: https://orcid.org/0000-0002-7119-7061

## Appendix A

## Model and Construct Validity

<table><tr><td colspan="3">Table A1. Model Constructs</td></tr><tr><td>Concept and definition:</td><td>Empirical equivalent/relevance:</td><td>Operationalization in model</td></tr><tr><td>Software architecture: The software artifact is represented by an architecture, which is defined as “the way the software is constructed from separately developed components [functions] and the way in which those components [functions] interact” (Clements et al., 2001, p. xvii).</td><td>The architecture of a software system (e.g., Ubuntu or Mozilla Firefox) reflects the interactions in this software system (e.g., functions [files] and calls [require, imports] operations between them).</td><td>The architecture is formalized as a design structure matrix (DSM). Each row (mirrored by the corresponding column) represents a function. The DSM grows over time by adding functions.</td></tr><tr><td>Propagation costs: Indicator of architecture quality. A measure of costs (effort or workload) that is required when a function is changed (Baldwin et al., 2014; MacCormack et al., 2006). Higher propagation costs mean that a single change in one function triggers a larger number of other functions. Higher propagation costs reduce maintainability and adaptability.</td><td>Costs (effort or workload) occur as changes in the software trigger other changes because of dependencies. Each triggered change, in turn, can trigger further changes. For example, if a function that returns information about an event is changed to a different format (the purchase time in an online shop is changed to POSIX format), all the other functions using that function must potentially also be changed (changing also to POSIX format). In turn, functions that use the changed functions might require changes as well. All these changes require developer time and effort (mostly testing and debugging).</td><td>Dependent construct: Defined as the sum of all the shortest paths in the architecture divided by the architecture size (i.e., the number of functions squared; see MacCormack et al., 2006).</td></tr><tr><td>Contributions and degree of contribution interdependence: Contributions offer a specific function. The degree of contribution interdependence reflects the extent of dependencies in the underlying problem that is solved by the artifact.</td><td>A contribution represents activities producing software code that provides a certain function (e.g., a mathematical operation, an input interface, an export feature, or a graphical output representation). A contribution can represent a new file containing a new function. It also can be a change to an existing file that adds a new function.The degree of contribution interdependence is the average extent of the dependencies in the underlying problem. The potential functions intended to solve the problem are, by their nature, more or less interdependent. For example, a word processor faces a lower degree of contribution interdependence than an operating system (MacCormack et al., 2012).</td><td>Model parameter: A contribution contains a function identifier {1, ..,100} and a dependency structure vector (determines the required functions).The degree of contribution interdependence is a model parameter determining the number of 1s in the dependency structure.</td></tr><tr><td>Artifact-based coordination: Mechanism describing coordination exclusively based on the common work artifact, without any authority (see Howison &amp; Crowston, 2014), which means the absence of predictive knowledge (Puranam et al., 2012). Counterpart/counterfactual to authority-based coordination.</td><td>As described by Howison and Crowston (2014), “I did not want to rely on the free time and commitment of others to finish something I would need for my work ... since their commitment was also unpredictable, I did not want to rely on their portion of shared work being completed. I feared being left ‘high and dry’” (p. 34). For example, consider the situation of Emmanuele and Marta in the illustration, which is managed by “productive referral” (i.e., waiting with a contribution until its requirements are implemented; see also Howison &amp; Crowston, 2014, p. 40.) Artifact-based coordination represents coordination in decentralized, leaderless OSS projects (e.g., GNOME and BibDesk).</td><td>Model parameter (alternative to authority-based coordination): Contributions are only implemented (i.e., added to the DSM) if all required functions are provided by the DSM.</td></tr><tr><td>Authority-based coordination: Counterpart/counterfactual to artifact-based coordination. Under authority-based coordination, predictive knowledge (Puranam et al., 2012) is present and assumed to be enabled by a central authority.</td><td>Developers can be sure regarding whether or not other developers implement the required contributions because an authority can ensure their implementation. This corresponds to “co-work” or “co-production” in Howison and Crowston (2014) and the situation of Linus and Tove in the illustration. Authority-based coordination represents more centralized OSS projects, with an authority or company involvement (e.g., Apache or Linux Kernel).</td><td>Model parameter (alternative to artifact-based coordination): Adds the possibility of implementing contributions when the required functions are in the set of available contributions.</td></tr><tr><td>(Degree of) visibility: The visibility of the artifact is essential for coordination, but it is often imperfect. The most recently added functionalities are typically not visible to the developers (Shaikh &amp; Vaast, 2016).</td><td>The degree of visibility represents the circumstance that recent functions are often not immediately visible to developers (Shaikh &amp; Vaast, 2016), for example, because of branching (Pastore et al., 2017) and the packaging of functions for various releases. In this timespan, current additions are not visible.</td><td>Model parameter: Delay (in time steps) in which the DSM is updated as perceived by the developers. For example, 1/50 means that every 50 time steps, the DSM’s visibility is updated.</td></tr></table>
