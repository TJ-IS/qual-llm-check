---
otero_id: 9578
otero_key: "53KM5VA8"
title: "Coordinating Interdependencies in Online Communities: A Study of an Open Source Software Project"
authors: "Aron Lindberg; Nicholas Berente; James Gaskin; Kalle Lyytinen"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0673"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/53KM5VA8/fulltext/images/7647a61c19ef1d3d960c399f75cda4fb202d96509660f06e2ee9c93be4bbac09.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Coordinating Interdependencies in Online Communities: A Study of an Open Source Software Project

Aron Lindberg, Nicholas Berente, James Gaskin, Kalle Lyytinen

To cite this article:

Aron Lindberg, Nicholas Berente, James Gaskin, Kalle Lyytinen (2016) Coordinating Interdependencies in Online Communities: A Study of an Open Source Software Project. Information Systems Research

Published online in Articles in Advance 02 Dec 2016

http://dx.doi.org/10.1287/isre.2016.0673

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/53KM5VA8/fulltext/images/bb9f65dbbc00f1d554d2ea882ee747da300c767e9470b13df5653d6d37b9a9f7.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Coordinating Interdependencies in Online Communities: A Study of an Open Source Software Project

Aron Lindberg

School of Business, Stevens Institute of Technology, Hoboken, New Jersey 07030, aron.lindberg@stevens.edu

Nicholas Berente

Terry College of Business, University of Georgia, Athens, Georgia 30602, berente@uga.edu

James Gaskin

Marriott School of Management, Brigham Young University, Provo, Utah 84602, james.eric.gaskin@gmail.com

Kalle Lyytinen

Weatherhead School of Management, Case Western Reserve University, Cleveland, Ohio 44106, kalle@case.edu

o manage work interdependencies, online communities draw on a variety of arm’s length coordination mechanisms offered by information technology platforms and associated practices. However, “unresolved interdependencies” remain that cannot be addressed by such arm’s length mechanisms. These interdepend encies reflect, for example, unidentified or emerging knowledge-based dependencies between the community members or unaccounted relationships between ongoing community tasks. At the same time, online communities cannot resort to hierarchical coordination mechanisms such as incentives or command structures to address such interdependencies. So, how do they manage such interdependencies? To address this question, we conduct an exploratory, theory-generating case study involving qualitative and computational analyses of development activities within an open source software community: Rubinius. We analyze the ongoing management of interdependencies within the community and find that unresolved interdependencies are associated with alternatively structured sequences of activities, which we define as routines. In particular, we observe that two distinct classes of interdependencies—development and developer interdependencies—are associated with alternative forms of routine variation. We identify two generalized routine components—direct implementation and knowledge integration, which address these two distinct classes of unresolved interdependencies. In particular, direct imple mentation deals with development interdependencies within the code that are not already coordinated through modular interfaces, while knowledge integration resolves unaccounted interdependencies between developers. We conclude with implications for research into organizing principles for online communities and note the significance of our findings for the study of coordination in organization studies in general.

Keywords: online communities; open source software; routines; interdependencies; coordination; activity variation; order variation; sequence analysis

History: Samer Faraj, Georg von Krogh, Karim Lakhani, Eric Monteiro, Senior Editors; Brian Pentland, Associate Editor. This paper was received on November 15, 2014, and was with the authors 9 months for 3 revisions. Published online in Articles in Advance December 2, 2016.

## Introduction

Coordination addresses interdependencies among tasks and people to accomplish organizational goals (Malone and Crowston 1994, Puranam et al. 2012) and has long been a central concern of organizational science (March and Simon 1958, Thompson 1967). Traditionally, organizational hierarchies have provided the coordination mechanisms that enable the management of complex work, which is characterized by the presence of a large number of different types of interdependencies, such as interactions across components of products and reciprocal relationships across departments (Thompson 1967, Zammuto et al. 2007). Recently, online communities have arisen without traditional organizational hierarchies, yet they can often successfully accomplish coordination of complex, highly interdependent tasks (Winter et al. 2014). In this paper, we investigate how online communities coordinate their work as they accomplish complex tasks in the absence of an organizational hierarchy.

Current explanations of how online communities accomplish coordination of interdependent tasks emphasize the presence of arm’s length mechanisms enabled by supporting information technology (IT)

platforms and associated practices (Ma and Agarwal 2007, Ransbotham and Kane 2011, Zammuto et al. 2007). For open source software (OSS) communities, such practices afforded by IT platforms include modularization of software code and collaboration through incremental layering of contributions (Howison and Crowston 2014, MacCormack et al. 2012, Puranam et al. 2014). These arm’s length coordination mechanisms, however, fail to resolve all interdependencies of development work. In most development settings, several “unresolved interdependencies” inevitably remain in the form of either development or developer interdependencies. Unresolved development interdependencies are unaddressed interactions within the software code. These interdependencies arise because software can never be made perfectly modular, but rather, is in a state of constant flux reflecting the dynamism of its environment (Cataldo and Herbsleb 2013, Lehman 1980). Unresolved developer interdependencies result from the extent and manner in which developers interact with each other to make sense of extant functionalities and envisioned directions of the software across diverse technical environments and user communities (Faraj and Sproull 2000). We therefore ask: How do OSS communities address such unresolved interdependencies?

To address this question, we conducted an exploratory case study of an online community around the OSS project Rubinius. Rubinius is a successful virtual machine and interpreter for the Ruby programming language, which is widely used in developing interactive Web applications (in the context of the Ruby on Rails framework). Rubinius is a typical case of an online community that originated outside the boundaries of any particular organizational hierarchy, but that needs to coordinate an interdependent set of development tasks. This is reflected in the fact that the Rubinius community currently manages an extensive, complex, and rapidly changing codebase. Furthermore, the community consists of a relatively large, sophisticated, and diverse body of developers and users.

We analyzed development practices that take place in conjunction with the use of the IT platform (GitHub) and through which the community coordinates its work. We conceptualize these practices as routines. Routines are stable, yet evolving, patterns of interdependent activities (Feldman and Pentland 2003) that help to coordinate work and accomplish specific development tasks such as fixing a bug or adding a new feature. We analyze variation in the composition and structure of routinized activities associated with various development tasks. We find that Rubinius developers coordinate different classes of interdependencies by engaging in various types of routinized activities. First, they coordinate around “simple” interdependencies through modular structures with straightforward routinized task assignments that follow the principles of superpositioning. Second, unresolved development and developer interdependencies are addressed by generating a greater variety in the structure of routinized activities. Development interdependencies are primarily dealt with by increasing the associated variety of activity types being carried out (i.e., increased activity variation). Furthermore, as development interdependencies increase, more developers tend to become involved, thus increasing the degree of developer interdependencies present in the task. Developer interdependencies, in turn, are addressed by increasing the variation in the ordering of activities associated with a development task (i.e., increased “order variation”). Overall, we find that forms of routine variation associated with successful development tasks emerge as assemblages of varied routine components—stabilized subpatterns within routines—where each component provides a dedicated mechanism for coordinating different types of interdependencies. Activity variation is associated with a routine component we label “direct implementation,” which provides efficient coverage of activities necessary to merge code into the codebase. Order variation is associated with the routine component we label “knowledge integration,” which enables developers to iteratively integrate insights distributed across the community. Through such components within the overall development routine, OSS communities are enabled to address various unresolved interdependencies.

The remainder of this paper is organized as follows. First, we briefly review the relevant literature on coordination—especially in the context of OSS communities. We identify two types of unresolved interdependencies, development and developer interdependencies, and conceptualize the associated practices in terms of routinized patterns of activities. We then present the research design, analysis, and findings of the empirical study. Though the four key constructs of study— development and developer interdependencies, activity, and order variation—emerged inductively during our exploratory data analysis, we introduce the constructs prior to the data analysis as conceptual scaffolding to aid the reader in understanding the logic of our analysis and the findings of the study.

## Coordinating Interdependencies in Online OSS Communities

Organizations provide multiple coordination mechanisms that enable the execution of tasks to minimize hands-on coordination of interdependencies between tasks and organizational units (Mintzberg 1979). These coordination mechanisms include task decomposition, departmentalization, formal rules, standard operating procedures, incentive systems, information systems, values, etc. (March and Simon 1958, Thompson 1967, Galbraith 1974, Wageman 1995, Zammuto et al. 2007). However, these coordination mechanisms can never account for all interdependencies—unresolved interdependencies inevitably exist above and beyond the arm’s length coordination mechanisms (Mintzberg 1979, Perrow 1986). These unresolved interdependencies remain across tasks and across units in the organization (Mintzberg 1979, March and Simon 1958, Puranam et al. 2012). The more complex, uncertain, and innovative the task, the greater the number of unresolved interdependencies and the attendant increase in the need for various integrative mechanisms (Perrow 1986). In organizations, unresolved interdependencies are addressed in the hierarchy— vertically through mechanisms such as hierarchical decision making and laterally by mechanisms such as cross-unit teams (Galbraith 1974, Lawrence and Lorsch 1967, Thompson 1967). The presence of such unresolved interdependencies is a central issue in organizational scholarship and a perennial issue for management as a field (Mintzberg 1979).

Online communities, however, generally do not possess these hierarchies and associated institutionalized coordination mechanisms to allow them to address unresolved interdependencies the way that traditional organizations do, yet they still manage to execute complex tasks successfully (Winter et al. 2014, Puranam et al. 2014). In OSS communities, the structuring of work does not take place through departmentalization, for example, but rather through the online platform, the modular structure of the software, and the processes of open superpositioning (Howison and Crowston 2014). Through modularization of the software, cross-module interdependencies and related coordination are minimized (Baldwin and Clark 2000, Howison and Crowston 2014, Parnas 1972). Such modularization of code on the platform subsequently allows for incremental layering, or superpositioning, of code around existing modules (Howison and Crowston 2014). By largely reducing coordination efforts to arm’s length interface-based coordination, these mechanisms enable OSS communities to successfully develop code by relying on the input of large numbers of independent volunteer developers (Crowston et al. 2012). Just as in traditional forms of organizing, unresolved interdependencies will inevitably remain beyond the work coordinated by the structure of the platform and the software code and the resulting arm’s length practices. Next, we briefly describe two general classes of unresolved interdependencies—those across development tasks (“development interdependencies”) and those across developers (“developer interdependencies”; see Table 1 for definitions of each).

Table 1 Key Constructs

<table><tr><td>Construct</td><td>Definition</td></tr><tr><td>Development interdependencies</td><td>Interdependencies arising from tasks that necessitate unanticipated interactions with other tasks</td></tr><tr><td>Developer interdependencies</td><td>Interdependencies where developers require input from other developers to complete their tasks</td></tr><tr><td>Activity variation</td><td>Diversity of activities comprising an instantiation of a routine</td></tr><tr><td>Order variation</td><td>Diversity of the sequencing of activity types in an instantiation of a routine</td></tr></table>

Development interdependencies involve the tasks that require other tasks to take place to be completed. They typically result from “hidden” interdependencies and related interactions across software that cannot be managed adequately through modular interfaces (Cataldo and Herbsleb 2013). There are always hidden interdependencies across modules of reasonably complex code for a variety of reasons. First, interfaces need to be occasionally updated to cater to additional functional requirements placed on the module. This situation often arises in fast-evolving situations where the functional interfaces are not fully stabilized (Ernst 2005). Second, software continues to evolve, and future functional needs may not fit well with the current modular structure, necessitating compromises that introduce new interdependencies across modules (Cataldo and Herbsleb 2013). Third, there are often significant unintended and unobserved interactions between modules, which some scholars have labeled “logical dependencies” (Cataldo et al. 2008, Cataldo and Herbsleb 2013). Such interdependencies are not reflected in the structure of function calls across modules or through the use of global variables shared by modules. Many times, such logical interdependencies are created in situ when developers coedit multiple files in unforeseen ways. Logical interdependencies can also arise due to the necessity of making trade-offs between abstraction principles followed during the modularization strategy, due to the developers’ bounded rationality or ignorance of specific technical or performance requirements, or through error (Cataldo et al. 2008).

Developer interdependencies come about when one developer requires input from another community member, often because of the need to integrate the goals and perspectives of the other into the development task (Faraj and Sproull 2000, Puranam et al. 2012). The need for coordinating activities as part of achieving a complex goal stems from the need to draw on diverse expertise available in the community (Faraj and Sproull 2000). Developers possess different experiences, skills, interests, styles, and understanding of the code and its functions. Consequently, they will have different goals and ideas for the further development of the code (Cataldo and Wagstrom 2006, Curtis et al. 1988). The developers also work in separate technical environments with a variety of operating systems, programming languages, or versions of crucial tools such as compilers or software libraries. Essentially, these different sets of developers work within their unique ecologies of knowledge artifacts (Bucciarelli 1994, Hutchins 1995). While executing a complex development task, it is therefore necessary to integrate across, or at least reconcile differences between, these environments and related artifacts or knowledge (Bailey et al. 2010).

Both unresolved development and developer interdependencies require some way to coordinate activities across two or more developers within a development task. The need for such coordination is significant in OSS communities, since development activities involving two or more developers are relatively common (Howison 2009). Next, we introduce the idea of routines within OSS communities to aid in our analysis of how online communities address unresolved interdependencies.

## Routines as Coordination Mechanisms in OSS Development

Online communities (O’Mahony and Lakhani 2011) constitute forms of electronically mediated “communities of practice” or “epistemic communities” (Knorr-Cetina 1991, Lave and Wenger 1991). In such communities, task coordination emerges bottom-up and manifests itself in a family of stable organizational practices and related interactions. Generally, these are embodied in observed activity patterns on the platform, or routines, through which the community members participate in the activities of the community (Cohendet and Llerena 2003). Such routines carry organizational knowledge vital for coordination (Nelson and Winter 1982). Because of the absence of hierarchical coordination mechanisms, routines constitute a principal mechanism for coordinating unresolved interdependencies in online communities.

Routines are defined generally as “repetitive, recognizable patterns of interdependent actions, carried out by multiple actors” (Feldman and Pentland 2003, p. 95). In OSS communities, routines manifest themselves in repeated sequences of activities that multiple developers execute jointly, but often with minimal synchronous interaction. This work takes place primarily by executing activities (such as “comment” or “merge”) afforded by the supporting IT platform. In this sense, the structuring of routines depends somewhat on the design of the OSS platform in that each platform offers a relatively fixed set of primitive activities that may be helpful in coordinating work (such as “reporting a bug” or “submitting a pull request”). These primitives comprise a repertoire of potential activities to be used by developers for their task coordination. Routines are triggered when OSS developers respond to a new demand to develop the code, such as fixing a bug or identifying and/or implementing a new feature. In this regard, each individual activity sequence executing a development task—a contextually emergent instantiation of a routine—constitutes a response to a unique development situation. In consequence, instances of routines are sequenced in ways that exhibit varying approaches and understandings of how to use such mechanisms with varying task content (i.e., different tasks or code elements).

Overall, OSS platforms do not dictate the selection of activities included in a routine, or the order in which the activities are executed. We refer to the diversity of the types of activities included in a routine as “activity variation,” whereas the differential ordering of activities in a routine we label as “order variation” and observe that these emerge from contextual adaptation to coordination demands. These two properties of routine variation have been recognized in a growing body of research on how structures of routines and complex tasks interact (Hærem et al. 2015, Pentland 2003b, Wood 1986). In general, researchers have posited that the increased variety in the composition and sequencing of routine activities is likely to increase the capacity to handle more interdependent tasks (Gaskin et al. 2011, Holten and Rozenkranz 2011, Tushman and Nadler 1978). Several reasons have been put forward for this positive relationship. First, completion of interdependent tasks often requires a larger diversity of activities to match the diversity of the task characteristics. Hence, the more interdependent the task, the greater the expected activity variation (Hærem et al. 2015). Second, variation in the ordering of activities has been connected with increased flexibility in task execution necessary to coordinate interdependencies (Pentland 2003a). Given the tight connection between interdependencies and structuring of routines, the structure of routines is likely to matter for the outcomes of coordinating interdependent tasks (Pentland et al. 2010). Next, we report on an exploratory case study of routine composition and ordering and how they relate to unresolved interdependencies in OSS development.

## An Exploratory Study of Interdependencies and OSS Routine Variation

We conducted an exploratory study of a midsized OSS community, Rubinius (https://rubinius.com), to examine the ways in which OSS communities coordinate interdependent tasks. The Rubinius project is concerned with implementing a virtual machine (VM) for an interpreter of the popular Ruby programming language. At the time of the study, a major new feature was being implemented to the VM: runtime support for multiple central processing unit cores allowing for multithreaded processing within the VM. We selected Rubinius as a case study for several reasons: (1) it is a typical example (Yin 2008) of a successful OSS community; (2) it has gained traction within the larger Web development community; (3) the project is technically challenging; (4) it is rapidly changing with multiple official releases; and (5) because of the technical complexity of implementing parallelism in the VM, the project offered a good opportunity to examine the presence of multiple interdependencies and their effects on development work. Overall, the case helps us gain analytical insights (Yin 2008) into emergent coordination mechanisms and their impacts within a relatively complex OSS project. Such projects also lack the more elaborate and explicit governance structures shared by the largest projects in the OSS world, such as Linux, Apache, or Mozilla. In this regard, we can avoid the confounding mechanisms of organizational coordination that are increasingly prevalent in large, heavily institutionalized OSS projects (Fitzgerald 2006).

We followed a mixed-methods research design that consists of both qualitative and computational research methods (Gaskin et al. 2014). We chose this design because it helped us to identify broad, statistically derived patterns in how routine activities are structured and also develop rich accounts of the underlying mechanisms driving such patterns. This allows us to reveal both the general structures of the routinized activities as well as the contextual meaning and purpose attached to those activities as they relate to addressing unresolved interdependencies. The design involved a multistep process through which we sought to triangulate multiple forms of data (mostly digital traces as text and variables) and carry out multiple steps and forms of analysis (qualitative coding, computational operationalization of variables, statistical modeling, and visualizations). We inductively identified constructs and relationships between constructs using iterative interactions with the data corpus and emergent theory informed by relevant literature (Walsh et al. 2015).

## Data Collection

The main portion of the data was available online within the Rubinius repository. We collected this data over a 12-month period (January 6, 2012, to January 6, 2013). This period coincided with the second main release cycle of the software. The data set includes all digital traces of activities recorded on the online development platform GitHub (https://github.com/) along with the public archival data on Rubinius development (public interviews, blog posts, conference talks, etc.).

Table 2 Data Collection

<table><tr><td>Data</td><td>N</td><td>Comment</td></tr><tr><td>Interviews</td><td>17</td><td>All 3 Rubinius core developers, 12 peripheral developers, and 1 senior vice president</td></tr><tr><td>Public audio</td><td>3</td><td>Podcasts and other audio interviews conducted with core developers</td></tr><tr><td>Public video</td><td>3</td><td>Videotaped conference talks conducted by core developers</td></tr><tr><td>Public text</td><td>8</td><td>Blog posts and interviews conducted with core developers</td></tr><tr><td>Public Internet relay chat (IRC)</td><td>1,000+</td><td>Archived IRC conversations between core developers, developers, and users</td></tr><tr><td>Public email</td><td>100+</td><td>Mailing list conversations between core developers, developers, and users</td></tr><tr><td>Pull requests (activities)</td><td>686 (3,704)</td><td>Distinct pull requests on GitHub</td></tr></table>

We also conducted interviews with founders, corporate sponsors, core developers, and peripheral developers. This afforded us rich access to the detailed, inner workings of the community (see Table 2 for a summary of the data collected).

The GitHub platform organizes development work around “pull requests.”<sup>1</sup> A pull request is a distinct unit of work that may contain bug reports, discussions, and code. When a developer wants to initiate some new functionality, she starts by “forking” the codebase. Forking involves creating a separate, personal copy of the codebase. Changes to this fork can only be reunited with the master copy of the codebase through a “merge” activity. This happens when the forking developer requests core developers to “pull” the proposed changes into the baseline copy of the codebase, thus initiating a merge between the fork and the master copy of the codebase. Between the opening of a pull request and a merge (or reject) decision, there are a variety of other activities that may occur. This sequence of activities constitutes the “pull request” and is therefore our unit of analysis. Sets of activities can contain multiple commits (i.e., detailed changes to specific code modules), reports of “issues” (i.e., bugs), assigning issues to specific developers, reviews, discussion, etc. Because of this, pull requests can contain a variable number of activities. See Table 3 for the primitive activities enabled by GitHub and their frequencies in our data set. Accordingly, the GitHub platform enforces a “fork-pull request routine” of OSS development.

Table 3 Activity Frequencies

<table><tr><td>Activity</td><td>Definition</td><td>Freq.</td><td>%</td></tr><tr><td>Assigned</td><td>A problem is assigned to a specific developer</td><td>3</td><td>0.08</td></tr><tr><td>Closed</td><td>A pull request is closed</td><td>857</td><td>23.14</td></tr><tr><td>Commented</td><td>A discussion comment is made</td><td>1,134</td><td>30.62</td></tr><tr><td>Mentioned</td><td>A specific commit is mentioned in a discussion comment</td><td>440</td><td>11.88</td></tr><tr><td>Merged</td><td>A pull request is merged into the baseline copy of the code</td><td>369</td><td>9.96</td></tr><tr><td>Opened</td><td>A pull request is opened/initiated</td><td>268</td><td>7.24</td></tr><tr><td>Referenced</td><td>A pull request is referenced in another pull request</td><td>470</td><td>12.69</td></tr><tr><td>Reopened</td><td>A closed pull request is reopened</td><td>17</td><td>0.46</td></tr><tr><td>Reviewed</td><td>A specific snippet of code is commented on</td><td>146</td><td>3.94</td></tr><tr><td></td><td>Total</td><td>3,704</td><td>100.00</td></tr></table>

To extract the digital traces of activities associated with each pull request (Anjewierden and Efimova 2006), we used scripts based on the data mining toolkit by Gousios and Spinellis (2012). These scripts captured trace data associated with each pull request in the time period under scrutiny. We extracted traces of 686 pull requests containing 3,704 activities. The process followed principles of exploratory data analysis (Tukey 1977), whereby we iterated constantly between visualizations, statistical modeling, and qualitative inquiry.

## Construct Operationalization

We identified and operationalized interdependencies and coordination mechanisms through intensive initial exploration of the data. We enriched our understanding of these constructs through qualitative inquiry into the particular activities associated with each focal construct. Table 4 summarizes the quantitative operationalization of the constructs used in the study, including the measures that capture salient aspects of our focal constructs. We next describe a few that require additional clarification. Descriptive statistics for these measures can be found in Appendix D.

Development interdependencies are logical dependencies between two or more modules in the codebase that often are unaccounted for. To assess the degree of development interdependencies, we draw on Cataldo et al. (2008) by measuring the number of files which are coedited simultaneously in the same pull request. This indicates the degree to which a specific pull request involves work on multiple modular elements of the codebase.

Developer interdependencies are knowledge sharing requirements across developers to leverage diverse expertise and/or reconcile different technical ecosystems (Faraj and Sproull 2000). The degree of developer interdependencies is measured by the number of developers involved in a single pull request. A greater number of developers involved increases the need for coordinating diverse object worlds, mental models, and other distributed cognitions associated with collaborative work.

Table 4 Construct Operationalization

<table><tr><td>Construct</td><td>Operationalization</td></tr><tr><td></td><td>Development interdependencies</td></tr><tr><td>Nonmodular work (presence of development interdependencies)</td><td>A dummy variable indicating which pull requests have two or more files associated with them</td></tr><tr><td>Degree of development interdependencies</td><td>Total number of files being coedited in a pull request</td></tr><tr><td>Average degree of development interdependencies</td><td>The average number of files being coedited in a pull request within a specific subset of pull requests</td></tr><tr><td></td><td>Developer interdependencies</td></tr><tr><td>Nonsuperposition work (presence of developer interdependencies)</td><td>A binary variable indicating which pull requests have two or more developers working on them</td></tr><tr><td>Degree of developer interdependencies</td><td>Number of developers working together on a pull request</td></tr><tr><td>Average degree of developer interdependencies</td><td>The average number of developers working together on a pull request within a specific subset of pull requests</td></tr><tr><td></td><td>Routine variation</td></tr><tr><td>Activity variation</td><td>The Shannon (1948) entropy of activity types in a pull request</td></tr><tr><td>Order variation</td><td>The ratio of transitions between activity types to the total number of activities in a pull request</td></tr><tr><td></td><td>Other variables</td></tr><tr><td>Merging</td><td>Binary measure of whether a pull request has been merged into the baseline copy of the codebase or not</td></tr><tr><td>Activities</td><td>A count of the number of activities executed in relation to a pull request</td></tr><tr><td>Average number of activities</td><td>The average number of activities executed in relation to a pull request in a specific subset of pull requests</td></tr><tr><td>Code-related work</td><td>A binary variable indicating which pull requests have one or more files associated with them</td></tr><tr><td>Proportion of code-related work</td><td>The percentage of pull requests, within a specific subset of pull requests, that have files attached to them</td></tr></table>

Activity variation is the diversity of activity types found in a pull request. Diversity of activity types can be interpreted as a relative measure that depends on both the total number of activity types as well as the total number of activities associated with a pull request. We measure activity variation using Shannon’s (1948) original concept of entropy defined as the “uncertainty” of predicting the distribution of activities across activity types in a given time period (Gabadinho et al. 2011a). This means that activity variation is maximized not by a large range of activity types, but by an even distribution of these activity types across the instances of activity types. For further details, see Appendix A.

Order variation is the variety in the ordering of activity types in a pull request. We measured order variation by counting the number of transitions between activity types within each pull request (Gabadinho et al. 2011b). We then divided the number of transitions between activity types by the number of activities in each pull request. This yields a measure of the variation in the ordering of activities in terms of transitions between activity types, measured at the level of individual pull requests. For further details, see Appendix A.

Merging is adding new code to the codebase. To capture how pull requests containing code were successfully implemented, we measured whether the pull request was merged into the baseline code. Merging means that a core developer with editing rights judged the suggested code contribution to be acceptable and subsequently made a merge decision for that pull request. This is a binary variable—either the code associated with a pull request has been merged or it has not. While regressing the outcome variable “merged” onto predictor variables, the marker “merge” was parsed out from the data before calculating the values of each independent variable.

## Data Analysis

Next we describe specific analyses conducted to elicit the results that are reported in the findings section (see Figure 1 for an overview of the analysis process). First, we need to show that pull requests are indeed different when they involve unresolved development and developer interdependencies compared to pull requests fully addressed by modularization and superpositioning. We demonstrate this difference by showing that nonmodular pull requests (those that coedit two or more files) contain significantly more activities and developers compared to modular pull requests (those that edit a single file). Similarly, we show that such nonsuperpositioning pull requests (those that involve more than one developer) contain significantly more files edited compared to superpositioning pull requests (those that involve a single developer).

Figure 1 Data Analysis Process  
![](/api/attachments/53KM5VA8/fulltext/images/1212592f37fbebe18de1fbd1107a8cedefb3210b943deefd3e1cbbc4f91fbe13.jpg)

We used sequence analysis (Gaskin et al. 2014) to understand how routine variation relates to unresolved interdependencies. Through this analysis, we identified the level of activity variation and order variation in each pull request. Then we explored in greater detail how unresolved development and developer interdependencies are associated with the level of activity and order variation. This was achieved by regressing the two forms of routine variation onto different types of interdependencies as well as through visualizations (Tukey 1977). These analyses show that the relationship between the two constructs have a curious shape—routine variation and unresolved interdependencies manifest wedge-shaped patterns of association well known within studies of ecology and climatology (e.g., Ben-Gai et al. 1993). These can be modeled statistically through testing a scatter plot of the two variables for “sparse zones” or “empty corners.” To observe the presence of the shape, we utilized a “delta test,” which computes the proportion that an empty corner in a scatter plot accounts for (Bardsley et al. 1999, Vetrova and Bardsley 2012) and determines whether this proportion is statistically different from what it would have been given a random distribution.

To reveal the substance of the analyzed activities within identified sets of pull requests, we next conducted two-step qualitative coding that sought to identify the nature of the activities carried out (the technical details of this process are shown in Appendix B). First, we conducted open coding in the spirit of grounded theory (Strauss and Corbin 1990) and elicited a set of codes describing development activities from the interview data as well as the public archival sources. This set of codes was next formalized into a coding scheme that was applied to a smaller theoretically selected sample of the data set to conduct a thematic content analysis (Krippendorff 2013). This approach renders the qualitative coding of the data set rigorous and reliably quantifiable. This coding elicited identifiable routine components in the routine structures. Each of these components was interpreted as a thematically and temporally stable part of the pull request routine being carried out and involved multiple developers (see details in Appendix C). In other words, by analyzing these components, we could validate these routine components as mechanisms that increased activity or order variation to address a specific type of unresolved interdependency. As noted, we identified two meaningful components with distinct characteristics: direct implementation and knowledge integration.

We next integrated thematic coding results with the results of descriptive, statistical modeling. To establish meaningful associations between identified routine components and analyzed routine variation, we next conducted analyses of covariance (ANCOVAs). These analyses show whether the average level of activity and order variation changed, due to the presence or absence of each specific routine component. This was carried out by using dummy variables for each identified routine component.

To understand whether routine variation had an effect on the successful merging of code, we next regressed the binary variable of merging code onto activity and order variation using a logit regression. This regression model used the derived measures of the type of development work and number of developers as controls (whether work is code related, since pull requests can contain zero or more files, and whether work is superposition related, since pull requests can involve one or more developers). We also controlled for the number of activities associated with each pull request. Last, we conceptualized the relationships between unresolved interdependencies, routine variation, routine components, and coordination to fashion a theoretical framework of how to coordinate unresolved dependencies in OSS communities. Hence, our theory is largely grounded in, and emerged from, the data regardless of whether quantitative, qualitative, or visual evidence was used in its formulation (Tukey 1977).

## Findings

We asked the following research question: How do OSS communities address such unresolved interdependencies? To address this question, first we will detail the differences between pull requests with and without unresolved interdependencies, then we will show how the Rubinius community addresses unresolved development and developer interdependencies. After this we will elaborate on the nature of the two routine components, direct implementation and knowledge integration, and show how they drive activity variation and order variation, respectively. Last, we will show the effects of routine variation on the successful merging of code.

Unresolved Interdependencies. First, we show that there is indeed a difference in routine structures associated with different types of pull requests. Therefore, we begin by separating pull requests that potentially involve unresolved interdependencies from those that do not include such interdependencies. In Table 5, we show the differences in means and their statistical significance across salient characteristics of pull requests between modular and nonmodular work and between superpositioning and nonsuperpositioning work.

Table 5 Unresolved Interdependencies

<table><tr><td rowspan="2"></td><td colspan="2">Development interdependencies</td><td colspan="2">Developer interdependencies</td></tr><tr><td>Modular work(1 file, 28%)</td><td>Nonmodular work(2 or more files, 72%)</td><td>Superpositioning work(1 developer, 21%)</td><td>Nonsuperpositioning work(2 or more developers, 79%)</td></tr><tr><td>Average degree of developer interdependencies</td><td>2.71 (1.27)</td><td>2.90 (1.07)***</td><td>—</td><td>—</td></tr><tr><td>Average number of activities</td><td>6.99 (4.24)</td><td>8.55 (5.87)***</td><td>1.71 (0.81)</td><td>7.53 (5.87)***</td></tr><tr><td>Proportion of code-related work</td><td>—</td><td>—</td><td>9%</td><td>49%***</td></tr><tr><td>Average degree of development interdependencies</td><td>—</td><td>—</td><td>0.31 (1.18)</td><td>2.91 (17.44)***</td></tr></table>

Note. Standard deviations are in parentheses.  
<sup>∗∗∗</sup>p < 00001 (Wilcox test of mean differences compared to one file/one developer).

As Table 5 shows, pull requests with unresolved development interdependencies (i.e., nonmodular work that includes coediting two or more files simultaneously) are significantly different from pull requests without such dependencies (i.e., modular work which includes editing one file). The former involves significantly more activities and developers. We also see that pull requests carrying unresolved developer interdependencies (i.e., including nonsuperposition work, where two or more developers collaborate on the same task) contain more activities, include a larger proportion of code-related work, and have more files edited compared to development work that does not involve developer interdependencies (i.e., superposition work including one developer). Thus, the pull requests with unresolved interdependencies clearly differ from those without. Next, we present our findings concerning the structure of the routinized activities that address these differences.

Addressing Unresolved Development Interdependencies. Figure 2(a) and 2(b) shows only the pull requests that have code attached to them (so as not to conflate pull requests with a lack of interdependencies with those that simply do not involve code at all). The relationship between development interdependencies and activity variation (Figure 2(a)) is wedge shaped, as shown by the delta test for empty corners $( \Delta = 0 . 8 8 $ $p { < } 0 . 0 0 1 )$ ). By contrast, the relationship between development interdependencies and order variation (Figure 2(b)) does not show a wedge-shaped pattern based on the delta test $( \Delta = 0 . 6 7 , p = 0 . 3 5 )$ , nor any other discernable relationship. This indicates that developers respond to increasing development interdependencies by increasing their activity variation. At the same time, the increase in the spread of unresolved development interdependencies as activity variation increases indicates that (a) even low degrees of development interdependencies may warrant high degrees of activity variation, while (b) high degrees of development interdependencies rarely are addressed by low degrees of activity variation.

Furthermore, we explored whether there was a relationship between development and developer interdependencies. The results depicted in Figure 3 indicate that as development interdependencies increase, so does the degree of developer interdependencies ( = $1 . 5 9 , p < 0 . \dot { 0 0 } 1 )$ ). This suggests that as developers address development interdependencies, they not only increase activity variation but also increase developer interdependencies. We will next discuss how developer interdependencies are dealt with.

Figure 2 (Color online) Routine Variation and Development Interdependencies  
![](/api/attachments/53KM5VA8/fulltext/images/2e0641c20094c46e3d18aeb4fac5b7a40b6fc7e80ca1f9478796d8686ab82fd8.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/7fb47ad68c421d0532235fa1bccaafdc5ccaa0398f3309b1d48258b2aa206190.jpg)  
Note. A single pull request was deleted for being an outlier. It had over 2,000 files attached and essentially consisted of changing the name of a variable across the whole codebase.

Figure 3 (Color online) Relationship Between Development and Developer Interdependencies  
![](/api/attachments/53KM5VA8/fulltext/images/466d2a3a0e38b0c0d33b046d36f6099c89aa4c93a1a2a8e63d7cada2257ef561.jpg)

Addressing Unresolved Developer Interdependencies. We observed above that unresolved developer interdependencies are connected with both activity variation and order variation (Figure 4(a) and 4(b)). This relationship with order variation can be modeled both linearly and through fitting a wedge-shaped relationship.

As Figure 4(a) illustrates, when more developers become involved with a particular pull request, we can see a linear increase in the activity variation when code is attached to the pull request $( \beta = 2 . 0 8 , p < 0 . 0 0 1 , N =$ 198); this is also true for pull requests without code attached $( \beta = 3 . 7 0 , p < 0 . 0 \dot { 0 } 1 , N = \dot { 4 } 8 8 )$ . The difference between these two conditions is that when existing code gets involved in the work, the average degree of activity variation will be higher (0.55 compared to 0.31, $p < 0 . 0 0 1 )$ . Additionally, there is no evidence for a wedge-shaped relationship between activity variation and developer interdependencies per the delta test for empty corners $( \Delta = 0 . \dot { 2 } 7 , p = 0 . 9 4 )$

Figure 4 Routine Variation and Developer Interdependencies  
![](/api/attachments/53KM5VA8/fulltext/images/6fdb235bbc430c2dc7cce41305c93bb1e48f281106363418d9c9ccdb4620a692.jpg)

Furthermore, as Figure 4(b) shows, a greater number of unresolved developer interdependencies is also associated with greater order variation $( \beta = 1 . 1 6 , p <$ 00001). This effect is particularly pronounced for pull requests, which have no code attached to them $( \beta =$ 1048, $p < 0 . 0 0 1 , N = 1 9 8 )$ , but is also present for pull requests that contain code $( \beta = 1 . 2 0 , p < 0 . 0 0 1 $ , N = 488). Furthermore, a wedge-shaped pattern is evident between the developer interdependencies and order variation, as confirmed by the delta test $( \Delta = 0 . 4 9 ,$ $p < 0 . 0 5 )$ . This suggests that the degree of order variation can be high even with low degrees of unresolved developer interdependencies, whereas as unresolved developer interdependencies increase, order variation is rarely, if ever, low.

Since there is a direct relationship between unresolved development interdependencies and developer interdependencies, we can also detect an indirect effect between development interdependencies, developer interdependencies, and order variation (Sobel, Aroian, and Goodman tests are all significant at $p < 0 . 0 1 )$ . This suggests that as development tasks become more interdependent, not only is more activity variation generated, but the number of developers involved also increases, and therefore also the degree of order variation generated.

Thus far we have established that (1) pull requests with unresolved interdependencies differ from those without unresolved interdependencies, (2) unresolved development interdependencies have a wedge-shaped relationship with activity variation and are also associated with developer interdependencies, and (3) unresolved developer interdependencies have a wedge-shaped relationship with order variation and are also associated with activity variation. Next we unpack the nature of these patterns by investigating the content of related routine components.

(b) Order variation  
![](/api/attachments/53KM5VA8/fulltext/images/230e3a6628d72e84d98c30e8f6c1c1b3953938358c1c7387ccb81fb47431d1b7.jpg)

Table 6 ANCOVA

<table><tr><td rowspan="2">Component</td><td rowspan="2">N</td><td>df</td><td>F</td><td>P</td><td>Effect size</td><td>df</td><td>F</td><td>p</td><td>Effect size</td></tr><tr><td colspan="4">Activity variation</td><td colspan="4">Order variation</td></tr><tr><td>Direct implementation</td><td>172</td><td>1</td><td>56.46</td><td>&lt;0.001</td><td>1.01</td><td>1</td><td>0.00</td><td>0.98</td><td>0.02</td></tr><tr><td>Knowledge integration</td><td>172</td><td>1</td><td>2.29</td><td>0.13</td><td>0.21</td><td>1</td><td>37.01</td><td>&lt;0.001</td><td>0.87</td></tr></table>

Routine Components. What do increases in routine variation mean in terms of the content of activities performed? Through qualitative analysis, we identified two separate routine components: direct implementation and knowledge integration.

In Table 6 we show, based on ANCOVA, that increases in activity variation are associated with the direct implementation component $( \beta = 1 . 0 1 , p \ <$ 00001)—a set of activities aimed toward writing code that is distributed across multiple files. This component can be found in 42% of all pull requests. Simultaneously, this routine component has a nonsignificant association with order variation $( \beta = 0 . 0 2 , p = 0 . 9 8 )$ To illustrate the direct implementation component, we show a typical pull request exhibiting this routine component in Table 7. Quantitatively, this component exhibits a high degree of activity variation (0.85) when compared to other pull requests involving multiple files.

The scenario associated with this component is as follows. A developer (skogstroll) wants to fix a particular feature. Several changes are made to the code to add some new features and additional tests are requested and implemented, after which the code is merged. Note that carl\_c reacts in this sequence to an “invalid pointer”—meaning that a variable in the code has been related to an object in an incorrect way. The tests make sure that the new code does not “break the build” by inserting unwanted interactions with other parts of the code.

Direct implementation activities often start with code proposals (“This fix moves the inclusion of the paths after all libs are processed so that these included paths are first.”), which are then elaborated on by a duo or triad of developers, often involving an iterative process of asking for clarification (“Your specs need a proper version guard for 200 so they don’t fail on 108 and 1090”), and providing clarification about the code as well as communication around tests of various kinds (“Sorry 0 0 0 should not send 6pull request7 at Friday25 Should be fixed now”). These activities all seek to make sure that no unwanted interactions occur across the codebase.

Furthermore, increases in order variation are associated with the knowledge integration component $( \beta =$ 0087, p < 00001). This set of activities is oriented toward identifying, collating, and integrating knowledge distributed across multiple developers. This component is present in 60% of all pull requests, and although clearly related to order variation, it is not related to activity variation. The association between knowledge integration and activity variation is nonsignificant ( = 0002, p = 0098). To illustrate the knowledge integration component we provide an example of a typical pull request involving this component in Table 8. This pull request exhibits a high degree of order variation (0.96) when compared to other pull requests involving multiple developers.

This example shows how a developer (koneal) proposes a change but is not sure about the best way to implement the change. A rich discussion ensues with regard to the best way to rewrite the piece of code that caused the original problem. Developers often engage in such discussions to identify and integrate knowledge distributed across multiple developers. The varied sequential ordering structure of such pull requests and related discussions manifests itself in increased order variation. Overall, a higher degree of order variation indicates more frequent switching between activity types, therefore enabling different kinds of knowledge to surface. Developers jointly iterate across such activity types to integrate knowledge and thereby resolve developer interdependencies.

A number of activities carry out the work of identifying and resolving developer interdependencies. For example, we identified diagnosing and causal theorizing as two ways that developers attempt to identify and gauge knowledge to understand what is going on in the codebase (“As near as I can tell without looking at your system is that you have both MRI 108 and 109 installed and when you installed rake, you did so with 1091 so the rake gem binary wrapper is invoking 109”), thus paving a way for outlining a tangible solution.

Diagnosing and causal theorizing involve trying to understand the issues faced by other developers (“If you can provide us a repro, that would be great! Otherwise I suspect it’s going to be almost impossible for us to investigate what is going on”) as well as attempting to figure out the causes of faced issues. These activities indicate that developers are not on the same page and that they need to inquire into each other’s mental models to identify and integrate knowledge that will help resolve partially understood interdependencies. This,

Table 7 Example of a Direct Implementation Routine Component

<table><tr><td>Code</td><td>Data</td></tr><tr><td>—</td><td>skogstroll $^{a}$  opened this pull request: “Array rotate fixes”</td></tr><tr><td>Adding features</td><td>skogstroll commented: “Fixes for Array#rotate failing specs”</td></tr><tr><td>Adding features</td><td>carl_c reviewed: “For this guard we usually use Rubinius:: Type.coerce_to(ndigits, Integer, :to_int) but I guess this is ok too.”</td></tr><tr><td>Asking for clarification</td><td>skogstroll reviewed: “Changed in skogstroll@e6c0d8f, is this the way? Also fixed unnecessary #dup”</td></tr><tr><td>Asking for tests</td><td>carl_c commented: “I’d love to test and merge this but I just got an invalid pointer when trying to run the tests, so maybe someone else can take a look.”</td></tr><tr><td>Providing tests</td><td>tristan commented: “@carl_c—I’ve tested it and all tests are passing.”</td></tr><tr><td>Providing tests</td><td>carl_c commented: “Still seeing issues but I was able to test this too. Thanks all!”</td></tr><tr><td>—</td><td>carl_c merged 1 commit carl_c closed the pull request</td></tr></table>

<sup>a</sup>All developer nicknames are fictitious to preserve the anonymity of the individuals being portrayed. We have attempted to choose nicknames similar in character to what are commonly used on GitHub.

Table 8 Example of a Knowledge Integration Routine Component

<table><tr><td>Code</td><td>Data</td></tr><tr><td>Asking for clarification</td><td>koneal commented: “I based the change broadly on the changes in this commit from MRI. However, I wasn’t sure if changes similar to these (which extend the ‘update max fd’ calls to pretty much everywhere open (2) or pipe (2) are called) where necessary (e.g., here)? I attempted to do something similar to closefrom... but the process locked up, and I didn’t investigate further.”</td></tr><tr><td>Causal theorizing</td><td>koneal commented: “This breaks the signal handler as it closes the file descriptors created here (and written to here and here) and the threads just hang waiting for eternity :disappointed.”</td></tr><tr><td>—</td><td>...3 comments and 3 reviews</td></tr><tr><td>Asking for tests</td><td>drax commented: “@koneal thanks for working on this. I think it’s a reasonable solution. I wish we had some real world benchmarks we could check, but I suppose we will see if anyone reports slowness that shows a bottleneck here.”</td></tr><tr><td>Diagnosing</td><td>drax commented: “Just to reiterate, I think this is a superior solution to blacklisting special fds that we may use internally, primarily because the total number of fds can be set with ulimit, we’d need to check that value and iterate a possibly very big number. I don’t see how doing that is a better solution. @att care to weigh in on this?”</td></tr><tr><td>—</td><td>...3 comments</td></tr><tr><td>Diagnosing</td><td>drax commented: “...After this discussion, I’m persuaded that tracking max_fd is probably the cleaner approach.”</td></tr><tr><td>—</td><td>...1 comment and 2 reviews</td></tr><tr><td>Teaching</td><td>drax commented: “I manually merged this and moved the code for tracking the fd’s to the VM. It needs to track it atomically and this way we make sure it’s always tracked properly. drax closed this pull request”</td></tr><tr><td>—</td><td>koneal commented: “Great, thanks”</td></tr></table>

for example, involves asking for clarification or providing clarification with regard to what flags, arguments, or versions another developer is running. Integrating such knowledge is often crucial for understanding why one developer may see an artifact behave in a particular way, while others may not have the same experience. Furthermore, teaching others reflects the intention to impart knowledge to others, albeit in a unilateral way (“The fact that config.rb is part if the signature is precisely because the signature prevents loading an invalid runtime that may be in path when rbx is invoked with a relative path”). Essentially, as developers work in concert, they realize that they each possess disparate forms of knowledge that must be identified and integrated to either work in concert or in parallel on a shared set of design artifacts. As they confront such interdependencies in relation to those artifacts, they take action to resolve them.

Merging Code. As we can see in Table 9, activity variation is clearly associated with merging of code

Table 9 Logit Regression

<table><tr><td>Dependent variable</td><td>Merged (Y/N)</td></tr><tr><td> $R^{2}$ </td><td>0.75</td></tr><tr><td>N</td><td>686</td></tr><tr><td>Intercept</td><td>-4.80***</td></tr><tr><td>Activity variation</td><td>1.51***</td></tr><tr><td>Order variation</td><td>-0.62*</td></tr><tr><td>Nonsuperposition work</td><td>-0.22 (0.75)</td></tr><tr><td>Code-related work</td><td>5.32***</td></tr><tr><td>Activities</td><td>-0.59**</td></tr></table>

Notes. All variables except dichotomous variables are standardized.Tests for homoscedasticity showed no significant deviations from this assumption. To test for multicollinearity, variance inflation factors were estimated. These were all below 2 for the logit regression and below 3.5 for the ANCOVA models, well below the accepted threshold of 10 (O’Brien 2007). Furthermore, the variables’ activity variation and order variation were transformed by the natural logarithm to ensure normality before being used in the logit regression. The computation of the various measures for the logit regression did not include the “merged” activity, to not include the dependent variable in the computation of the predictors. Furthermore, the logit regression also does not include the dummy variables for routine components (direct implementation and knowledge integration), because routine variation is a manifestation of the components, and this would confound the coefficients (essentially measuring the same thing twice). We used Nagelkerke’s (1991) pseudo-R<sup>2</sup> for the logit regression.

$$
^ {*} p <   0. 0 5; ^ {* *} p <   0. 0 1; ^ {* * *} p <   0. 0 0 1.
$$

$( \beta = 1 . 5 1 , p < 0 . 0 0 1 )$ : an increase of one standard deviation in activity variation increases the chance of merging the code by 82%.<sup>2</sup> Hence, diversity in activity types (i.e., activity variation) forms an important characteristic of pull requests that leads to merged code. This implies that activity variation needs to provide just the right amount of activities, or a range of activities that can provide efficient coverage of necessary activity types. This set identifies a necessary set of activities to write and merge working code (see Appendix A for an extensive example).

Furthermore, order variation is negatively related to the likelihood of merging code $( \beta = - 0 . 6 \dot { 2 } , p < 0 . 1 0 )$ Hence, an increase of one standard deviation in order variation will decrease the chance of merging the code by 65%. In other words, the more varied the order of activities within a pull request, the less likely it is that code will be successfully merged.

## Discussion

Online platforms, modularization, and superpositioning have been identified as important coordination mechanisms that enable OSS communities to construct complex software artifacts. OSS developers layer incremental changes on top of existing modules in a piecemeal fashion. They postpone tasks associated with more complex module interactions until such work becomes feasible to deal with in this way (Howison and Crowston 2014). Code evolves through continuous sedimentation, which enables further layering. Hence, the superpositioning approach to task assignment complements modularization (Yoo et al. 2010) as a way of understanding not only how code is partitioned into manageable pieces but also how the development process itself gets divided into manageable chunks that are then executed as self-contained tasks. Creation of such self-contained tasks is a fundamental way of reducing interdependencies (Galbraith 1974, Simon 1996). Yet, as noted, unresolved interdependencies remain after code has been modularized and layered (Cataldo et al. 2008). Accordingly, a host of OSS development tasks require knowledgebased coordination (Howison 2009, Faraj and Sproull 2000) of interdependencies related to both development work and the developers themselves. In this study, we extend our understanding of this next level of coordination by exploring how an OSS community overcomes a set of unresolved interdependencies that remain beyond those addressed by modularization and superpositioning.

We asked the following research question: How do OSS communities address such unresolved interdependencies? To answer this question, we elicited insights through an exploratory case study using large quantities of qualitative and structured data, drawing on a variety of analysis techniques. The analyses sought to elicit novel theoretical insights in the same way that qualitative researchers have done for decades by using inductive methods such as grounded theory to generate novel theoretical insight from a rich data corpus (Strauss and Corbin 2008, Walsh et al. 2015). New questions, constructs, and relationships emerged in conjunction with the iterative, stepwise, and exploratory analysis process we followed (Tukey 1977). We were also able to triangulate and extend evolving insights by mixing qualitative and computational analyses of digital trace data.

We identified two distinct components within the fork-pull request routine: direct implementation and knowledge integration that deal with development and developer interdependencies, respectively. Direct implementation was shown to be associated with greater activity variation, whereas knowledge integration was shown to be associated with greater order variation. This distinction essentially unpacks a difference between the two forms of routine variation. Direct implementation involves a more diverse mix of activities in the routine (i.e., activity variation), indicating that in these cases developers deal with development interdependencies and the attendant work of writing code to efficiently cover necessary activities. Knowledge integration, by contrast, is associated with a different form of routine variation (i.e., order variation)

Figure 5 Addressing Unresolved Interdependencies  
![](/api/attachments/53KM5VA8/fulltext/images/dfb7218eb615f831daa5e423d8fba6260f03547c6f1e1a56a233555f3706ef19.jpg)

which highlights how developers iteratively and collaboratively work to identify and integrate distributed knowledge reflecting present developer interdependencies, resulting in more varied sequencing of the various activities. Last, we showed that the effects of engaging in these forms of routine variation are different: increased activity variation is positively associated with merged code, whereas increased order variation is negatively associated with merged code.

## Toward a Theory of Coordinating Unresolved Interdependencies

Overall, each distinct routine component provides a set of coherent activities that is focused on resolving either of the two unresolved interdependencies (see Figure 5 and a summary in Table 10). To wit, different routine components reflect separate capacities endowed by the participants to achieve specific goals associated with development tasks. This is somewhat similar to how dynamic capabilities (Teece et al. 1997) are viewed as “the organizational and strategic routines by which firms achieve new resource configurations” (Eisenhardt and Martin 2000, p. 1107).

Table 10 Routinized Responses to Unresolved Interdependencies

<table><tr><td>Component</td><td>Direct implementation</td><td>Knowledge integration</td></tr><tr><td>Interdependencies addressed</td><td>Development interdependencies</td><td>Developer interdependencies</td></tr><tr><td>Activity variation</td><td>Increased</td><td>—</td></tr><tr><td>Order variation</td><td>—</td><td>Increased</td></tr><tr><td>Coordination mechanism</td><td>Resolve development interdependencies through an efficient coverage of activities which is necessary to implement the code changes</td><td>Resolve developer interdependencies through identifying, making sense of, and integrating diverse knowledge distributed among developers</td></tr></table>

Through direct implementation, developers engage collaboratively with the task of writing code that interacts with multiple modules of the codebase. Developers address such pull requests by engaging in diverse activity types such as commenting, mentioning specific commits, reviewing code, and referencing other pull requests (these activity types represent 59% of all performed activities). Overall, activities within this routine component focus on dealing with identified development interdependencies and seek the most efficient means for completing such tasks—what we refer to as the “efficient coverage” of necessary activities. Efficient coverage captures how a diverse set of necessary activities are brought to bear upon a problem. Diversity, as it is understood through the lens of Shannon’s (1948) entropy, means that it is not only a wide range of activities but a diverse distribution of activities across possible activity types that is necessary to complete the task. Efficient coverage is the routine-level analog to a set of cognitive strategies that economize cognitive effort, such as in Fiske and Taylor’s (1984) “cognitive miser.” Direct implementation usually consists of a proposal by a peripheral developer, upon which a decision is later made by a core developer. This is the ideal for how the fork-pull request routine is supposed to work in addressing relatively complex but well-identified design tasks.

By contrast, when multiple developers start to work together, they encounter interdependencies that arise from the need to align their different perspectives (Boland and Tenkasi 1995) and object worlds (Bucciarelli 1994), which precipitates a need to engage in knowledge integration. This manifests itself in increased order variation in pull requests. Increased order variation addresses developer interdependencies by varying participants’ relationships with external software packages, introducing idiosyncratic use cases, generating variations in local software and hardware configurations, or articulating different understandings of the codebase itself, while iterating among all of these activities as required. Overall, pull requests that include this routine component invite multiple developers to participate in a collaborative inquiry to “get on the same page” (Crowston and Kammerer 1998). This is similar to accounts of distributed cognition (Hutchins 1995) in that it generates extensive flows of knowledge across mental models and external artifacts, thus resulting in sharing and integration of knowledge. During such a process, developers identify and resolve interdependencies, which manifests as increased order variation (Cramton 2001).

Overall, these activities can be viewed as a form of collective sense making, where a diverse set of developers jointly seek to achieve common ground on problem diagnoses and solutions. Collective sense making requires reciprocal interaction—what Weick (1979) refers to as a “double interact.” Such collective sense making leads developers to adopt both “make” and “take” perspectives (Boland and Tenkasi 1995) because developers have different understandings, visions, and goals for the software, as well as varying levels of expertise. Also, this knowledge integration may involve communicating with each other regarding the contents of multiple object worlds and related artifacts that each developer interacts with (Bucciarelli 1994). Developers work in unique environments— with their particular computers, operating systems, browsers, software programs—and this material environment is implicated in their perspectives and also in the tangible workings of their development work (e.g., a developer may experience a bug with a particular version of a browser). Such intense communicative practices are foundational to any system development effort (Hansen and Rennecker 2010) and are manifest in OSS development through increased variation in the iterative sequences of development activities. Indeed, extant literature in software design recognizes the importance of building a common understanding among software developers (e.g., Curtis et al. 1988) and also holds for OSS communities (Scozzi et al. 2008). Our observations of knowledge integration affirm the challenge that unresolved developer interdependencies constitute as well as the importance of developers working collectively to identify and integrate distributed knowledge.

## Coordination in Online Communities

Online communities are increasingly the site of creativity, innovation, and design activities, especially in terms of the “coproduction” (Kane et al. 2014) of various artifacts. Since online communities eschew formal coordination mechanisms, understanding the emergent dynamics of how such communities are coordinated is an important focus of research (Malone and Crowston 1994). Our research adds to this conversation by explicating the role of routines and their associated forms of variation in providing mechanisms for coordination.

Technical platforms such as GitHub support coordination by providing a suite of communication and collaboration features, including tools for forum conversations and version control (Scacchi 2004). In our case study, such tools were essential because they allowed for dividing tasks into manageable units and then managing these units. The platform also facilitated community-wide communication and memory (Michlmayr and Hill 2003). However, the features supporting coordination provided by the GitHub platform are not in themselves sufficient to explain how complex development activities are coordinated. Rather, the platform simply makes available a suite of affordances that developers can utilize to accomplish coordination (Faraj et al. 2011). In activating such affordances, developers are encouraged to write code in a modular, superpositioning fashion to minimize unnecessary interactions across tasks and developers.

Organization theory has long noted that interdependencies tend to exist across both tasks and actors (March and Simon 1958, Mintzberg 1979, Puranam et al. 2012). In the context of OSS, pull requests may be independent from each other, but the agents performing the development work contained in each pull request may still be interdependent, and the development work itself may also manifest new interdependencies across the codebase. We show that unresolved interdependencies can be addressed through routine variation and related activities. This identifies elements of online community coordination that are not visible through theoretical lenses focusing on arm’s length explanations. This view highlights the background conversations among community members that help them collaborate jointly on complex tasks (see Howison 2009, Faraj and Sproull 2000).

Earlier research on challenges associated with coordinating interdependencies in OSS has mainly focused on existing structural relationships among developers—not ongoing activity relationships and their variety. Cataldo et al. (2008), for example, argue that relational coordination is enabled by belonging to the same organizational team or by being colocated. They acknowledge, however, the presence of what they call “actual coordination”—the relationships that form as developers collaborate on joint tasks—regardless of whether the developers belong to the same team or are colocated. We extend this finding by showing what structural features of routinized activities manifest such coordination.

The success of GitHub is a good example of an innovation that promoted better coordination, since it provided the first fork-pull request-based version control platform that integrated hypertext functionality and discussion forums organically with the platform’s version control functions. Insights from this study can be helpful for platform designers in creating new features that can support coordination of complex and distributed communities. For example, one might draw on our notion of efficient coverage to identify minimal sets of activities necessary to achieve expected positive outcomes under specific conditions and then build platform features that can support (possibly through cues and nudges) the completion of those activities. We showed how, in OSS communities, developers string together activities on the platform that generate efficient coverage for coordinating specific complex tasks. Similarly, one might expect that activity sequences that more efficiently cover activities necessary to the crowdsourcing of ideas in open innovation contests (Malhotra and Majchrzak 2014), for example, would be more likely to generate desired outcomes.

## Coordination in Organization Studies

Ashby’s (1956) law of requisite variety posits that to control any system, the state space of a controller must be equal to or greater than the state space of the system under control. The notion of requisite variety has been consequently applied in multiple ways in the organizational literature (Boisot and McKelvey 2011). For example, Beer (1984) reformulated the law in his statement that the variety of an organization’s management absorbs the variety or uncertainty associated with interdependencies in that organization’s activities. Beer (1984) identified two tactics for managing requisite variety—managers can either attenuate the variety that their organization must deal with or they can amplify the ability of their organization to deal with more and varying tasks. Attenuation involves tactics such as modular decomposition, which minimizes the number of interdependencies that organizations have to deal with at any point of time (Baldwin and Clark 2000, Simon 1962). Amplifying strategies would involve creating new cross-organizational or crosssystem connections such as the use of lateral or vertical information systems that enable the organization to approach uncertain situations in more varied ways (Galbraith 1974, Lee and Berente 2012). To amplify and attenuate variety, traditional organizations mostly use formal mechanisms to structure themselves in specific ways so as to manage interdependencies (Thompson 1967).

In self-organizing contexts such as online communities, however, community members typically utilize loosely structured platforms to perform the work and amplify the variety of the community through emergent interaction. Routinized activity structures emerge, which enable the necessary coordination on the fly. The idea of emergent routines within online communities thus forms a fundamental departure from the ways scholars have typically thought about routines and the ways to coordinate complex tasks. In traditional organizations, actors follow well-specified ostensive routines, or programs (March and Simon 1958), that take care of coordination effort, and thereby attenuate the variety that individuals address. In online communities, on the other hand, actors are involved in continuous and dynamic configuration of routines manifesting significant contextual variation as the developers seek to make the routinized activities fit with the set of interdependencies they face. This variation cannot be construed as a deviation from a prespecified pattern, but rather as a contextual emergence of routinized action that is sensitive to varying contingencies (Faraj et al. 2011), including the possibility of new interdependencies and related actors and tasks.

The routine components that we identified in this case study can be seen mainly as emergent, amplifying coordination mechanisms that complement attenuating mechanisms such as modularization and superpositioning. This view leads us to look beyond strategies in coordinating online work such as modularization and superposition that attenuate the variety carried by interdependencies, and directs attention toward ways in which emergent coordination mechanisms can amplify variety generation within development tasks. This helps us to understand how organizing in increasingly distributed and dynamic contexts relies not only on attempts to attenuate possible interdependencies but also how actors in such contexts can be supported to generate a greater variety by offering ways to increase different forms of routine variation.

By showing that routinized behaviors can emerge in a self-organizing manner and by explicating the role of specific routine components in this process, our analysis also sheds light on the significant role that routinized activities have in coordinating complex work. Most accounts of coordination rest upon grand models of hierarchies or markets (Benkler 2006), or related ideas of modularization and superpositioning (Baldwin and Clark 2000, Howison and Crowston 2014). As an important source of coordination, routines have been expected to be a resilient feature of highly structured contexts, such as formal organizations. We showed that routinized behavior also plays a specific role in coordinating self-organizing contexts. Such routines differ from those found in hierarchies in that they are never explicitly and fully structured, but enable the structure to emerge as actors at the micro level seek to address specific interdependencies. They are also distinct from modularization and superpositioning in that they generate variety to complete complex tasks, rather than seeking to minimize interdependencies.

Our contributions are naturally limited by the scope of our inquiry and data. First, though we sampled a relatively typical OSS project, it is not clear that similar routine structures will emerge in all OSS projects with similar tasks, or in other online communities. Even though the case provides novel theoretical insights, we urge scholars to conduct inquiries that can extend our insights across other contexts. Second, there are many aspects of software development that we could not observe, but that still could influence coordination, since they were never shared in digital traces or noted in the interviews. Further inquiry using ethnographic methods could help us to analyze routines and activities that have remained hidden to us. Third, the correlations between some of the variables in the study were fairly high (<0.70), indicating a potential threat of multicollinearity, although no variance inflation factors (VIFs) exceeded the generally accepted threshold of 10 (the VIFs were all below 3.5), according to O’Brien (2007). Fourth, our measures are derived from pull requests as they appear after a merge or reject decision has been made. Another approach might consider how interdependencies or variation at the beginning of a pull request leads to differences in interdependencies or variation in the latter part of the pull request. We leave this, however, to future research.

## Conclusion

Much of the existing research on coordination is premised on the idea that explicitly specified mechanisms provide the necessary means to coordinate interdependent organizational activities (Galbraith 1974, March and Simon 1958, Thompson 1967). This assumption has been questioned in recent decades as online communities have flourished and succeeded in carrying out complex tasks without the benefit of preexisting organizational hierarchies (O’Mahony and Lakhani 2011, Winter et al. 2014). OSS communities form a particularly successful example of such communities—one that has similarities to other types of online communities, but with unique characteristics such as the coproduction of complex artifacts (Stewart et al. 2006). OSS communities coordinate the design and development of complex artifacts despite the presence of a number of conditions traditionally seen as antithetical to successful coordination: geographical and temporal distribution, volunteerism, and virtual communication. Therefore, a variety of researchers view OSS communities as harbingers of next-generation organizational forms that can provide viable alternatives to traditional organizational coordination (von Hippel and von Krogh 2003, von Krogh and von Hippel 2006). In this paper we have used a novel, exploratory approach to elicit a theory for how routines and their attendant forms of variation serve as emergent coordination mechanisms in such online communities, thereby potentially leading the way to a better understanding of future forms of organizing.

## Acknowledgments

This research was supported by a grant from the CISE division of the U.S. National Science Foundation [1217345]. The authors thank the senior editors, associate editor, and reviewers for their guidance and valuable feedback throughout the review process. The authors also acknowledge the insightful comments provided by participants at Stevens Institute of Technology, Temple University, and the Academy of Management meeting, where earlier versions of the manuscript was presented.

## Appendix A. Routine Variation Measures

## Activity Variation

We measure activity variation in a manner consistent with Shannon’s (1948) original concept of entropy, defined as the “uncertainty” of predicting the event distribution in a given time period (Gabadinho et al. 2011a). Entropy is calculated in our case by summing the proportions of occurrences of each event type multiplied by the natural logarithm of each proportion. We utilized the “TraMineR” R package to measure the entropy (Gabadinho et al. 2011b). The highest activity variation is achieved when a sequence contains an equal proportion of every activity type. Any “bias” toward a specific activity type in the given sequence decreases entropy.

Figure A.1 Activity Variation  
![](/api/attachments/53KM5VA8/fulltext/images/91b183ff2e29715fe39825d4641482d24046508bb031fbe4a141339142771ef6.jpg)

To illustrate the measure, consider this (see Figure A.1): assuming the same number of actual activities being performed, a pull request with three different types of activities (one instantiation of each of the three different activity types, e.g., open–comment–merge) will exhibit more activity variation than a pull request with only two different types of activities (e.g., one instantiation of the first activity type and two instantiations of the second activity type, open– comment–comment).

To counter the claim that the difference between activity variation and order variation boils down to differences in the number of activities within a pull request, each of these measures was correlated with this measure. This revealed relatively minor correlations: order variation correlated with the number of activities at 0.29, while activity variation and order variation correlated with each other at 0.30; by contrast, activity variation correlated with the number of activities at 0.43. This is a substantive correlation, but still too small to argue that activity variation is just a linear function of the number of activities within a pull request.

## Order Variation

To measure order variation, we counted the transitions between activity types within each pull request. We then normalized this measure by the number of activities within the pull request. This yields a measure of the order variation, measured at the level of individual pull requests, independent of other pull requests.

All else equal, a pull request with more activity type transitions (from one type to another) will exhibit more order variation than one with fewer activity type transitions. For example (see Figure A.2), ordering comment– review–comment (two transitions) will equate to more order variation than ordering comment–comment–review (one transition), despite having the same number of unique activity types, as well as the distribution of activities across types, thus indicating the same degree of activity variation.

Figure A.2 Order Variation  
![](/api/attachments/53KM5VA8/fulltext/images/0c678fd9a93e1536b7d9c2331e66f58c181066279f225efbbaf9fccb05e49ae2.jpg)

## Appendix B. Qualitative Coding

To understand not only the structure of pull requests but also their substantive contents, we analyzed the interviews as well as sources of publicly available archival data using an open and axial coding approach informed by grounded theory (Strauss and Corbin 2008). This helped us elicit descriptive codes with regard to various substantive activities associated with development work, such as analyzing issues, writing code, or collating distinct pieces of knowledge required to solve a specific problem. Overall, the process yielded 432 text excerpts along with 13 analytical memos and 87 distinct low-level codes. Then, through axial grouping, we organized these low-level codes into a smaller set of medium-level categories constituting a general coding scheme that could be used to code sequencelevel archival data (i.e., digital traces of pull requests as text). Last, we synthesized these medium-level categories into high-level themes that describe types of activities, i.e., routine components.

Next we applied this coding scheme to the digital traces of pull requests performed during our study period. We systematically analyzed the content of activities with attached text (i.e., the activity types opened, commented, and reviewed, collectively representing 41.8% of all activities). To ensure the reliability of our coding, we calibrated the coding scheme with two coders (the first and second author), who, in multiple rounds, coded 10 pull requests at a time, compared their results, and iteratively made changes to the coding scheme and how it was applied. Eventually the coders achieved an acceptable interrater reliability with a kappa of 0.87 (Cohen 1977). At this point, we considered the coding scheme to be sufficiently stable, and the remaining pull requests were divided evenly between the two coders.

The validated coding scheme was used to code a random sample of 25% (172 out of 686 sequences) of the pull requests, thereby characterizing their “routine components.” In Table B.1, we show the qualitative coding scheme. The relative frequency denotes the percentage of the coded pull requests that contain a particular component. Note that a single pull request can contain both components, which is why the relative frequencies do not add up to 100%.

## Appendix C. Validating the Routine Nature of Activities

We argue that the activities we are observing actually are routinized for a number of reasons. First, the pull requests show thematic structure—we were able to code a persistent set of thematically organized activities (per the content analysis). Second, these activities repeat and are distributed evenly across time. To validate this notion, we plotted the distribution of pull requests within each component over time to ensure a uniform distribution.

In Figure C.1, we can see that for both of our focal components, the pull requests are evenly distributed across the entire year. The date of each pull request is calculated as the midpoint between the opening and closing of the pull request. Note that some midpoints therefore fall outside of the studied period, since those pull requests were initiated or closed before or after the focal period. All in all, we can conclude that the components are stable across time, because the distribution of observations of each component is evenly distributed across time.

Table B.1 Coding Scheme

<table><tr><td>Component</td><td>Relative frequency (%)</td><td>Description</td><td>Activity</td><td>Description</td></tr><tr><td rowspan="8">Knowledge integration</td><td rowspan="8">60.47</td><td rowspan="8">Collating and integrating knowledge distributed across multiple developers</td><td>Diagnosing</td><td>Discussing alternative diagnoses of the problem or solutions</td></tr><tr><td>Causal theorizing</td><td>Providing ideas of what is causing specific behaviors to occur in the code</td></tr><tr><td>Asking for clarification</td><td>If a developer does not understand what the issue is, he asks for clarification</td></tr><tr><td>Clarification</td><td>Providing a clarification with regard to what the issue is</td></tr><tr><td>Teaching</td><td>Providing knowledge with regard to good coding practices or how the code works</td></tr><tr><td>Adding features</td><td>Request and execution of adding features to the code patch</td></tr><tr><td>Increasing code clarity</td><td>Rewriting the code to increase its clarity</td></tr><tr><td>Increasing code functionality</td><td>Rewriting the code to increase its performance (speed)</td></tr><tr><td rowspan="4">Direct implementation</td><td rowspan="4">42.11</td><td rowspan="4">Writing code distributed across multiple files</td><td>Asking for tests</td><td>Asking the patch submitter to provide specifications (specs) or tests of the code</td></tr><tr><td>Providing tests</td><td>Providing specifications (specs) or tests of the code</td></tr><tr><td>Asking for documentation</td><td>Asking the patch submitter to provide documentation for the code patch</td></tr><tr><td>Providing documentation</td><td>Providing documentation for the code patch</td></tr></table>

<table><tr><td></td><td>N</td><td>Mean</td><td>S.D.</td><td>Range</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1. Activity variation</td><td>686</td><td>0.42</td><td>0.22</td><td>0.86</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Order variation</td><td>686</td><td>0.73</td><td>0.33</td><td>1.33</td><td>0.30</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Activities</td><td>686</td><td>6.90</td><td>5.90</td><td>72</td><td>0.43</td><td>0.29</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Developer interdependencies</td><td>686</td><td>2.50</td><td>1.40</td><td>12</td><td>0.36</td><td>0.37</td><td>0.72</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>5. Development interdependencies</td><td>686</td><td>2.40</td><td>16.0</td><td>87</td><td>0.26</td><td>-0.02 (NS)</td><td>0.20</td><td>0.12</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>6. Merge (Y/N)</td><td>686</td><td>0.29</td><td>0.45</td><td>1</td><td>0.78</td><td>-0.14</td><td>0.47</td><td>0.16</td><td>0.64</td><td>1.00</td><td></td><td></td></tr><tr><td>7. Direct implementation</td><td>172</td><td>0.42</td><td>0.50</td><td>1</td><td>0.63</td><td>0.00 (NS)</td><td>0.41</td><td>0.21</td><td>0.75</td><td>0.77</td><td>1.00</td><td></td></tr><tr><td>8. Knowledge integration</td><td>172</td><td>0.85</td><td>0.36</td><td>1</td><td>0.12 (NS)</td><td>0.54</td><td>0.51</td><td>0.48</td><td>0.10 (NS)</td><td>-0.22</td><td>-0.03 (NS)</td><td>1.00</td></tr></table>

Figure C.1 Temporal Distribution of Components  
![](/api/attachments/53KM5VA8/fulltext/images/5e0d310e7b51eec1989ecc2ae2ffcc960aaf041d11f1ac82b1c5299e4a3d7cb1.jpg)

Third, once the pull requests have been closed, they serve as guidance to other developers. In the data, we observe how developers use the “reference” activity type (12.69% of all activities) to connect a pull request being worked on to other, older pull requests. This is a way to transfer knowledge from past work so that it can inform current work, as described in the GitHub documentation (https://guides.github.com/ features/issues/).

## Appendix D. Descriptive Statistics

In Table D.1 we show the correlation matrix for the variables used in the linear models. We also note the N , mean, standard deviation, and range for each variable. Correlations that are nonsignificant at the 0.05 level have been marked with “(NS).”

Often times [pull requests] are dependent on other [pull requests], or at least relate to them and you’d like to connect the two 0 0 0 0 References make it possible to deeply connect the work being done with the bug being tracked, and are a great way to add visibility into the history of your project.

Note that the activity type merge is not part of the calculations of the variables activities, activity variation, and order variation, as they relate to the merge variable, to not include the dependent variable in the computation of the independent variables.

The correlations between the dichotomous variable merge (variable 6), the dummy-coded components (variables 7 and 8), and other variables are biserial correlations, while the correlations among variables 6–8 themselves are tetrachoric correlations.

In Figure D.1, the frequency histogram for each variable is displayed, in its untransformed state.

Table D.1 Descriptive Statistics

8. Knowledge integration

3. Activities

Figure D.1 Histograms  
![](/api/attachments/53KM5VA8/fulltext/images/6ccca6e7458eae83f995a5a494614097e65db0394dc73de64d892de00da0f5e5.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/4807844ce94b0e90b9e97e626244ba51fb44a346249b6415cc3d9138b3b4ab11.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/58cb1541e99774c760e3a4b349f8b4d98e44b7acaf70ce59f34d194a0355040b.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/4c5e110b9e7a8b44930749cb33af8a58b411e57cf3f1fb814fc36af804393d07.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/75b902525afab4113d683af30c52cf6e46c55c1395ea5404a3d4772cc573d05e.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/de209f71d26a9f31eaba335bb25924f5bf37b8ff973c9dd9fb9f001083747a71.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/a7157ad8cafd84902b455327588a21746a697d9756a21a149560939007644bb9.jpg)

![](/api/attachments/53KM5VA8/fulltext/images/6bed3f273b1ac99dc9abfc7730c5fc45d73a7cab455e3822cb09bf54fe935298.jpg)

## References

Anjewierden A, Efimova L (2006) Understanding weblog communities through digital traces: A framework, a tool and an example. Meersman R, Tari Z, Herrero P, et al. eds. On the Move to Meaningful Internet Systems 20062 OTM 2006 Workshops, Lecture Notes Comput. Sci. Vol. 4277 (Springer-Verlag, Berlin Heidelberg), 279–289.

Ashby WR (1956) An Introduction to Cybernetics (Chapman & Hall, London).

Bailey DE, Leonardi PM, Chong J (2010) Minding the gaps: Understanding technology interdependence and coordination in knowledge work. Organ. Sci. 21(3):713–730.

Baldwin CY, Clark KB (2000) Design Rules: The Power of Modularity (MIT Press, Boston).

Bardsley WE, Jorgensen MA, Alpert P, Ben-Gai T (1999) A significance test for empty corners in scatter diagrams. J. Hydrology 219(1–2):1–6.

Beer S (1984) The viable system model: Its provenance, development, methodology and pathology. J. Oper. Res. Soc. 35(1):7–25.

Ben-Gai T, Bitan A, Manes A, Alpert P (1993) Long-term change in October rainfall patterns in Southern Israel. Theoretical Appl. Climatology 46:209–217.

Benkler Y (2006) The Wealth of Networks: How Social Production Transforms Markets and Freedom (Yale University Press, New Haven, CT).

Boisot M, McKelvey B (2011) Complexity and organizationenvironment relations: Revisiting Ashby’s law of requisite variety. Allen P, Maguire S, McKelvey B, eds. The SAGE Handbook of Complexity and Management (Sage, London), 279–298.

Boland RJ Jr, Tenkasi RV (1995) Perspective making and perspective taking in communities of knowing. Organ. Sci. 6(4):350–372.

Bucciarelli L (1994) Designing Engineers (MIT Press, Boston).

Cataldo M, Herbsleb JD (2013) Coordination breakdowns and their impact on development productivity and software failures coordination. IEEE Trans. Software Engrg. 39(3):343–360.

Cataldo M, Wagstrom P (2006) Identification of coordination requirements: Implications for the design of collaboration and awareness tools. CSCW ’06 Proc. 2006 20th Anniversary Conf. Comput. Supported Cooperative Work (ACM, New York), 353–362.

Cataldo M, Herbsleb JD, Carley KM (2008) Socio-technical congruence: A framework for assessing the impact of technical and work dependencies on software development productivity. Proc. Second ACM-IEEE Internat. Sympos. Empirical Software Engrg. Measurement (ACM, New York), 2–11.

Cohen J (1977) Statistical Power Analysis for the Behavioral Sciences (Lawrence Erlbaum Associates, Hillsdale, NJ).

Cohendet P, Llerena P (2003) Routines and incentives: The role of communities in the firm. Indust. Corporate Change 12(2):271–297.

Cramton CD (2001) The mutual knowledge problem and its consequences for dispersed collaboration. Organ. Sci. 12(3):346–371.

Crowston K, Kammerer E (1998) Coordination and collective mind in software requirements development. IBM Systems J. 37(2): 227–245.

Crowston K, Wei K, Howison J, Wiggins A (2012) Free/libre opensource software development: What we know and what we do not know. ACM Comput. Surveys 44(2):1–35.

Curtis B, Herb K, Neil I (1988) A field study of the software design process for large systems. Comm. ACM 31(11):1268–1287.

Eisenhardt KM, Martin J (2000) Dynamic capabilities: What are they? Strategic Management J. 21(10–11):1105–1121.

Ernst D (2005) Limits to modularity: Reflections on recent developments in chip design. Indust. Innovation 12(3):303–335.

Faraj S, Sproull L (2000) Coordinating expertise in software development teams. Management Sci. 46(12):1554–1568.

Faraj S, Jarvenpaa SL, Majchrzak A (2011) Knowledge collaboration in online communities. Organ. Sci. 22(5):1224–1239.

Feldman MS, Pentland BT (2003) Reconceptualizing organizational routines as a source of flexibility and change. Admin. Sci. Quart. 48(1):94–121.

Fiske S, Taylor S (1984) Social Cognition, 2nd ed. (Longman Higher Education, Boston).

Fitzgerald B (2006) The transformation of open source software. MIS Quart. 30(3):587–598.

Gabadinho A, Ritschard G, Studer M (2011a) Analyzing and visualizing state sequences in R with TraMineR. J. Statist. Software 40(4):1–37.

Gabadinho A, Ritschard G, Studer M, Nicolas SM (2011b) Mining sequence data in R with the TraMineR package: A user’s guide. http://mephisto.unige.ch/pub/TraMineR/doc/ 1.2/TraMineR-1.2-Users-Guide\_.pdf.

Galbraith JR (1974) Organization design: An information processing view. Interfaces 4(3):28–36.

Gaskin J, Thummadi V, Lyytinen K, Yoo T (2011) Digital technology and the variation in design routines: A sequence analysis of four design processes. Thirty Second Internat. Conf. Inform. Systems, Shanghai, China, 1–16.

Gaskin J, Berente N, Lyytinen K, Yoo Y (2014) Toward generalizable sociomaterial inquiry: A computational approach for zooming in and out of sociomaterial routines. MIS Quart. 38(3):849–871.

Gousios G, Spinellis D (2012) GHTorrent: GitHub’s data from a firehose. 9th IEEE Working Conf. Mining Software Repositories, 12–21.

Hærem T, Pentland B, Miller K (2015) Task complexity: Extending a core concept. Acad. Management Rev. 40(3):446–460.

Hansen S, Rennecker J (2010) Getting on the same page: Collective hermeneutics in a systems development team. Inform. Organ. 20(1):44–63.

Holten R, Rozenkranz C (2011) Designing viable social systems: The role of linguistic communication for self-organization. Kybernetes 40(3–4):559–580.

Howison J (2009) Alone together2 A socio-technical theory of motivation, coordination and collaboration technologies in organizing for free and open source software development. Carnegie Mellon University, Pittsburgh.

Howison J, Crowston K (2014) Collaboration through open superposition: A theory of the open source way. MIS Quart. 38(1): 29–50.

Hutchins E (1995) Cognition in the Wild (MIT Press, Cambridge, MA).

Kane GC, Johnson J, Majchrzak A (2014) Emergent life cycle: The tension between knowledge change and knowledge retention in open online coproduction communities. Management Sci. 60(12):3026–3048.

Knorr-Cetina K (1991) Epistemic Cultures: Forms of Reason in Science (Harvard University Press, Cambridge, MA).

Krippendorff K (2013) Content Analysis: An Introduction to Its Methodology (Sage, Thousand Oaks, CA).

Lave J, Wenger E (1991) Situated Learning: Legitimate Peripheral Participation (Cambridge University Press, Cambridge, UK).

Lawrence PR, Lorsch JW (1967) Differentiation and integration in complex organizations. Admin. Sci. Quart. 12(1):1–47.

Lee J, Berente N (2011) Digital innovation and the division of innovative labor: Digital controls in the automotive industry. Organ. Sci. 23(5):1428–1447.

Lehman M (1980) Programs, life cycles, and laws of software evolution. Proc. IEEE 68(9):1060–1076.

Ma M, Agarwal R (2007) Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Inform. Systems Res. 18(1): 42–67.

MacCormack A, Baldwin C, Rusnak J (2012) Exploring the duality between product and organizational architectures: A test of the “mirroring” hypothesis. Res. Policy 41(8):1309–1324.

Malhotra A, Majchrzak A (2014) Managing crowds in innovation challenges. California Management Rev. 56(4):103–123.

Malone TW, Crowston K (1994) The interdisciplinary study of coordination. ACM Comput. Surveys 26(1):87–119.

March JG, Simon HA (1958) Organizations (John Wiley & Sons, New York).

Michlmayr M, Hill BM (2003) Quality and the reliance on individuals in free software projects. Feller J, Fitzgerald B, Hissam S, Lakhani K, eds. Taking Stock of the Bazaar: Proc. 3rd Workshop Open Source Software Engrg., 105–109.

Mintzberg H (1979) The Structuring of Organizations: A Synthesis of the Research (Prentice-Hall, Upper Saddle River, NJ).

Nagelkerke NJD (1991) A note on a general definition of the coefficient of determination. Biometrika 78(3):691–692.

Nelson RR, Winter SG (1982) An Evolutionary Theory of Economic Change (Harvard University Press, Cambridge, MA).

O’Brien RM (2007) A caution regarding rules of thumb for variance inflation factors. Quality Quant. 41(5):673–690.

O’Mahony S, Lakhani KR (2011) Organizations in the shadow of communities. Working paper, Harvard Business School, Research in the Sociology of Organizations: Communities and Organizations, Vol. 11–131.

Parnas D (1972) On the criteria to be used in decomposing systems into modules. Comm. ACM 15(12):1053–1058.

Pentland B (2003a) Conceptualizing and measuring variety in the execution of organizational work processes. Management Sci. 49(7):857–870.

Pentland BT (2003b) Sequential variety in work processes. Organ. Sci. 14(5):528–540.

Pentland BT, Haerem T, Hillison D (2010) Comparing organizational routines as recurrent patterns of action. Organ. Stud. 31(7): 917–940.

Perrow C (1986) Complex Organizations: A Critical Essay (Random House, New York).

Puranam P, Alexy O, Reitzig M (2014) What’s “new” about new forms of organizing? Acad. Management Rev. 39(2):162–180.

Puranam P, Raveendran M, Knudsen T (2012) Organization design: The epistemic interdependence perspective. Acad. Management Rev. 37(3):419–440.

Ransbotham S, Kane G (2011) Membership turnover and collaboration success in online communities: Explaining rises and falls from grace in Wikipedia. MIS Quart. 35(3):613–627.

Scacchi W (2004) Free and open source development practices in the game community. IEEE Software 21(1):59–66.

Scozzi B, Crowston K, Eseryel UY, Li Q (2008) Shared mental models among open source software developers. 41st Annual Hawaii Internat. Conf. System Sci., 306–316.

Shannon C (1948) A mathematical theory of communication. Bell System Technical J. 27(3):379–423.

Simon HA (1962) The architecture of complexity. Proc. Amer. Philos. Soc. 106(6):467–482.

Simon HA (1996) The Sciences of the Artificial (MIT Press, Boston).

Stewart KJ, Ammeter AP, Maruping LM (2006) Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Inform. Systems Res. 17(2):126–144.

Strauss A, Corbin J (1990) Basics of Qualitative Research: Grounded Theory Procedures and Techniques (Sage, Thousand Oaks, CA).

Strauss A, Corbin J (2008) Basics of Qualitative Research: Techniques and Procedures for Developing Grounded Theory, 3rd ed. (Sage, Thousand Oaks, CA).

Teece DJ, Pisano G, Shuen A (1997) Dynamic capabilities and strategic management. Strategic Management J. 18(7):509–533.

Thompson JD (1967) Organizations in Action: Social Science Bases of Administrative Theory (Transaction Publishers, New Brunswick, NJ).

Tukey JW (1977) Exploratory Data Analysis (Addison-Wesley, Reading, MA).

Tushman M, Nadler D (1978) Information processing as an integrating concept in organizational design. Acad. Management Rev. 3(3):613–624.

Vetrova VV, Bardsley WE (2012) Technical note: A significance test for data-sparse zones in scatter plots. Hydrology Earth System Sci. 16(4):1255–1257.

von Hippel E, von Krogh G (2003) Open source software and the “private-collective” innovation model: Issues for organization science. Organ. Sci. 14(2):209–223.

von Krogh G, von Hippel E (2006) The promise of research on open source software. Management Sci. 52(7):975–983.

Wageman R (1995) Interdependence and group effectiveness. Admin. Sci. Quart. 40(1):145–180.

Walsh I, Holton JA, Bailyn L, Fernandez W, Levina N, Glaser, B (2015) What grounded theory is… : A critically reflective conversation among scholars. Organ. Res. Methods 18(4):581–599.

Weick KE (1979) The Social Psychology of Organizing, 2nd ed., Topics Soc. Psych., Vol. 2 (Addison-Wesley, New York).

Winter S, Berente N, Howison J, Butler B (2014) Beyond the organizational “container”: Conceptualizing 21st century sociotechnical work. Inform. Organ. 24(4):250–269.

Wood R (1986) Task complexity: Definition of the construct. Organ. Behav. Human Decision Processes 37(1):60–82.

Yin RK (2008) Case Study Research: Design and Methods (Sage, Thousand Oaks, CA).

Yoo Y, Henfridsson O, Lyytinen K (2010) Research commentary– The new organizing logic of digital innovation: An agenda for information systems research. Inform. Systems Res. 21(4): 724–735.

Zammuto RF, Griffith TL, Majchrzak A, Dougherty DJ, Faraj S (2007) Information technology and the changing fabric of organization. Organ. Sci. 18(5):749–762.
