---
otero_id: 17647
otero_key: "7QCVNT99"
title: "Designing layered functionality within group decision support systems"
authors: "Brent Vickers"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90068-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing layered functionality within group decision support systems

Brent Vickers

Griffith University, Nathan Campus, Qld, Australia

There appears to be no research available on providing end-users of Group Decision Support Systems (GDSS), with the flexibility to choose from a combination of interface types and levels of functional complexity, that best supports their task requirements, current skill level, and skill acquisition needs. The combination of interface type and level of functional complexity, is defined as “layered functionality”. Prominent researchers in Decision Support Systems (DSS), provide an insightful glimpse at the concept of layered functionality, by briefly examining the concept of a layered command language. This paper builds on this previous research and considers the merits of four potentially useful layers of functionality, using a prototype GDSS named DELAWARE.

Keywords: Layered functionality; Group Decision Support Systems (GDSS); interface; functional complexity; usage sophistication; task requirements; end-users.

![](/api/attachments/7QCVNT99/fulltext/images/8579dc22c11e8e97026b6d2bbc1c1a2a7ba36b9ba62e816f99b3820135f65820.jpg)

Brent Vickers received an Informatics degree in 1987, and a Commerce degree with honours in 1990. Current work includes post graduate studies involving the use of evolutionary prototyping to the continued development of a GDSS named DELAWARE. The development tool is a multiuser version of APL. Currently (1992) there exist only a handful of GDSS available for commercial application (for example, GroupSystems V and SAMM).

Correspondence to: Brent Vickers, Blnf, BCom(Hon), 3 Stapleton Tce., Bethania, Queensland 4111, Australia.

## 1. Introduction

The emergence of computer systems that support groups, arose as a result of increasingly turbulent and complex decision-making tasks that require technologies for increasing the efficiency and effectiveness of decision-orientated meetings (Huber, 1984b; 934–937). For example, experimenting with electronic communications combined with the delphi estimating technique, in many cases have introduced a structured, cost effective, and expedient approach to the decision process (Hiltz and Turoff, 1978; Johansen, Vallee, and Spangler, 1979; cited in Huber, 1984b; 936). Even though examples of GDSS applications conceptually support group decision processes, the reality of the historical success of GDSS as a commercial product, has been meagre.

Few applications experienced commercial viability due to the limited range of services being offered (Gray, 1987; 233–237). Deficiencies with available technology, poor integration of the various components of the computing package, and incomplete understanding of group decision-making, resulted in slower progress with GDSS than originally anticipated (Kraemer and King, 1988; 115). For example, an assessment of the current status of GDSS in 1983, showed that only two organisations had operational systems that were available for purchase (Kraemer and King, 1983). Since that time (1988) there have been no successful business ventures evolving from commercial GDSS applications (Kraemer and King, 1988; 128).

The difficulty with designing suitable GDSS for user organisations, arises from either the extraordinary variability in the patterns of information exchange, or decision paths across groups (Poole et al, 1985; cited in DeSanctis and Dickinson, 1987; 14). This variability is evident in a review (Huber, 1984a; 196) concerning GDSS end-users' overall opinion of a number of GDSS that were implemented in the private sector. The review indicates that individual systems tended to support only a very small set of group tasks, and that emphasis should be placed on a task-driven design strategy (Huber, 1984a; 200). This strategy refers to multiple kinds of functionality (Brown, 1986; 460), which is defined as a set of functions within a system that meet the end-users' task requirements (Bennett, 1978; 460; Goodwin, 1987; 229). An example of multiple functionality is the existence of functional components such as brainstorming, delphi, cross-impact analysis, interpretive structural modelling, ranking and voting mechanisms, message systems, etc. within the same software package. Multiple functionality does not accommodate task requirements, that are best supported by alternative levels of complexity that may exist within a functional component. For example, delphi panellists may need to specify their own judgement making parameters, rather than use the probability and desirability parameters dictated by the system.

Evidence suggests that providing extensive functionality alone does not improve end-users' task performance or acceptance of the system. For example, one study found that the way in which end-users accessed functions affected performance (Meadow, 1983; cited in Goodwin, 1987; 231). Another study indicated that usefulness and ease-of-use strongly correlates with end-user acceptance (Davis, 1989). For end-users to maintain usage of the system, it is important that they perceive that the system is useful, even if it objectively improves performance (Alavi and Henderson, 1981). Conversely, end-users adopt disfunctional systems, because they overrate the performance gains (Davis, 1989; 335). Perceived ease-of-use refers to the effort required to use a particular system (Davis, 1989; 321) and the easier a system is to use then the more useful the system becomes (Davis, 1989; 334). However ease-of-use in no way compensates for the functionality of the system (Davis, 1989; 333). Usefulness and ease-of-use can be influenced by both the functional and interface characteristics of the system (Benbasat and Dexter, 1986; Bewley et al., 1983; Dickson et al., 1986 cited in Davis, 1989; 335).

An obvious problem for designing GDSS that are easy-to-use and useful, is for the GDSS to be able to support end-users with differing abilities to use and learn about a particular layer (Brown, 1986; 461–475). To improve end-users' accepttance of GDSS, they should be provided the flexibility to choose a layer that will best accommodate their usage requirements – including task requirements and usage sophistication requirements. Subsequent sections will demonstrate how a combination of different interfaces and different levels of functional complexity, can be layered according to the level of usage sophistication and task requirements respectively. Layered functionality is therefore described as a set of functions within a system with varying complexity, that are supported by different levels of interface sophistication, that meet the end-users' task requirements, current skill level, and skill acquisition needs.

Layered functionality has been described in various settings, but there appears to be no discussion within the context of GDSS. Examples of layered functionality exist in advanced text editors (such as Emacs and Teco) that use layered functionality to provide end-users with greater scope for undertaking different tasks (Brown, 1986; 460). Possibly the closest example of an examination of layered functionality for GDSS, briefly describes a layered command language for DSS (Sprague and Carlson, 1982; 200; Bennet, 1983; 68). Although an insightful example, the DSS illustration neglects other potential layers of functionality, and provides no evidence in the form of a concrete application to indicate the feasibility of such a concept. There appears to be no evidence of layered functionality designed in any GDSS (or similar group support technologies) that have been designed or implemented to date. For example, there is no mention of a layered functionality concept within any discussions related to the following systems:

\- The PLEXSYS tools for facilitating knowledge acquisition, implemented in the MIS Planning and Decision Laboratory at the University of Arizona (Nunamaker et al., 1986; Dennis et al., 1988; Gallupe, 1988; Liang, 1988; Nunamaker et al., 1988; Jessup, Connolly, and Galegher, 1990; Gallupe et al., undated);

\- Prototype networked workstation technology and electronic blackboard technology (Jarvenpaa, et. al., 1988);

\- An experimental meeting room called "Colab" designed at Xerox's Palo Alto Research Center (PARC) (Stefik et al., 1987; Stefik et al.,

1987; Stefik and Brown, 1989; Phillips, undated);

\- The Shell GDSS developed at the University of Minnesota (DeSanctis and Dickson, 1986);

\- A GDSS called Software Aided Meeting Management (SAMM) developed by Watson, DeSantis, and Poole (Watson, DeSantis, and Poole, 1988);

\- The GDSS named Decision Aids for Groups (DECAID) designed by Gallupe, DeSanctis, and Dickson (Gallupe, DeSanctis, and Dickson, 1988; Gallupe, undated);

\- A GDSS named Local Area Decision Network-LADN-(Hale, Haseman, Munro, 1989);

\- A spreadsheet for cooperative work called the 'Object Lens' (Malone et al., 1987; Lai et al., 1988);

\- The Southern Methodist University (SMU) Decision Room Project (Gray et al., 1983);

\- The Decision Lab located at Queen's University in Canada (Gallupe, 1988; Gallupe, Bell and Yates, undated);

\- An APL Planning Model used by Xerox's Field Financial Operations Group (Palese, undated);

Another study compares the interface design of four experimental GDSS located at the University of Arizona, Claremont Graduate School, University of Minnesota, and XEROX PARC (Gray, 1988). The study discusses cognitive style and the need for end-users to select their own form of presentation. However no mention is made of combining different interfaces with different levels of functional complexity.

From a more general perspective, the concept of layered functionality does not even appear in discussions on Groupware. GDSS is regarded as one of seventeen approaches to team support, all of which fall under the umbrella of Groupware (Johansen, 1988; 12). Groupware is defined as “specialised computer aids geared toward the specific needs of business teams” (Johansen, 1988; vii). A description is made of advanced interface design for Groupware – such as intelligent Artificial Intelligence technologies that put more learning burden on the system (Johansen, 1988; 96–114). Again, no mention is made of combining improvements in interface design with different levels of functional complexity.

![](/api/attachments/7QCVNT99/fulltext/images/d1acfc7a08ca051bdc63475b95a523e1ad4bb87911316733d6d925dc1c92f9e0.jpg)  
Fig. 1. Layered functionality.

A demonstration of how layered functionality (referred to from now on as simply “layer”) can be applied to GDSS, considers four layers defined as closed, closed/open, open/closed and open. The formation of these four layers are based upon a previous evaluation of a prototype GDSS known as DELAWARE. DELAWARE is currently being refined according to the design specifications detailing the four layers. Subsequent evaluation may discover that either alterations to the existing four layers or new layers may be required.

Corresponding with the four layers, end-users' skill levels are categorised as novice, knowledgeable, experienced and expert. It should be noted that the terms end-users, experts, and panellists, all refer to the same type of group of people participating with the GDSS. These terms will be used interchangeably, depending upon the characteristic of the participation.

Figure 1 portrays relationship between the four skill levels and the four layers. This figure indicates that the closed layer provides novice end-users (who are regarded as having no knowledge about how the GDSS works) with a rigid framework that focuses on guiding their use of the GDSS. The closed/open layer facilitates the selection of parameters within a functional component and these end-users need to have an understanding of how the functional components work. The open/closed layer provides experienced end-users with a command language that provides a faster method for using functions (relative to the menu system offered by the first two layers). Experienced end-users require the additional understanding of how the command language works. The open layer enables expert end-users to modify the GDSS in terms of altering the data flow between functional components, altering the structure of the functional components, and to adding new functional components. Expert end-users require an additional conceptual understanding of how the applications programs both work and interrelate. These conceptual understandings will better provide expert end-users with an ability to make conceptual modifications to the GDSS. Applications programmers could then be succeeded to implement the conceptual modifications.

Considered from another dimension, the four layers are able to support various task requirements that enables end-users' to complete some specific work. Progress toward work completion will be affected by task characteristics such as uncertainty, complexity (DeSanctis and Gallupe, 1985), and degree of structure (Lamberti and Wallace, 1990). For a GDSS to effectively support the task requirements, the end-user must choose a layer that best accommodates the task characteristics. It is uncertain at this stage what degree of uncertainty, complexity or structure are best supported by the different layers. It is suggested that unvarying and repetitive tasks within highly structured environments, are best supported by closed systems (Gibson, 1982; 7). The more flexible or unstructured the tasks' environment, the more appropriate an open system (Gibson, 1982; 7). These generalisation do not necessarily hold for the closed and open layers discussed so far. For example, a highly complex task, such as understanding the issues surrounding the future business environment for the European automobile industry toward the year 2000 – described in greater detail later in this paper – would by the above generalizations, be better supported using the more open layers. The task was however, appropriately supported by the closed/open layer. Until future research either proves these generalizations or an alteration of the generalizations, to be true for GDSS, this paper will assume that there is no relationship between any layer and the task characteristics.

It has been indicated so far that end-users need to match both their skill levels and task requirements with a particular layer. A problem that has not yet been addressed, is that task requirements may be more suitably supported by layers for which the end-users aren't sufficiently skilled in using. For example, Figure 2 demonstrates a mismatch between the end-users' skill level and the task requirements, in terms of each being best supported by different layers. The novice end-users are capable of using only the closed layer. The task requirements necessitate the use of the closed/open layer, because for instance, different judgement making dimensions are required for using the delphi component. To eliminate this mismatch, the end-users will have to acquire an understanding of how to use the closed/open layer.

End-users will need to be provided with training programmes that enable them to migrate toward the more sophisticated layers. The training programmes could either be demonstration facilities built into the GDSS software package, training manuals, workshops, or any combination of the three alternatives.

<table><tr><td></td><td></td><td></td><td></td></tr><tr><td>Open</td><td></td><td></td><td></td></tr><tr><td>Open/ closed</td><td></td><td></td><td></td></tr><tr><td>Closed/ open</td><td></td><td>Task requirements</td><td></td></tr><tr><td>Closed</td><td>End users&#x27; current skill level</td><td>Skill acquisition need</td><td></td></tr><tr><td>Novice</td><td>Knowl-edgeable</td><td>Experienced</td><td>Expert</td></tr></table>

Fig. 2. Skill acquisition.

It should be noted that all four layers are considered in a disparate sense, to provide a clearer understanding when examining the merits of each. In practice an application may be suited to adopting a combination of layers. For instance, end-users may decide to use the closed layer for a delphi based sub-task, and the closed/open layer for a cross-impact analysis based sub-task. Choosing a variety of layers in this manner, enables end-users to take advantage of different layers that best suit the task requirements, current skill levels, or skill acquisition needs, within the single application. In addition, future research may find that the four layers should not be so neatly partitioned. For instance, end-users may require either only partial understandings, or an understanding of a combination of the layers. Partitioning functionality into the four layers so far described, at least provides a reference point for future research.

## 2. Research context-the-delaware GDSS

This study on alternative layers is based upon an evaluation of a current prototype GDSS named

DELAWARE – previously known as DELPAC. DELAWARE is a computer-assisted interactive approach to communication and forecasting, and was developed using APL. APL is both a programming language and a system that supports the writing, editing, using, saving and sharing of programs (Gilman and Rose, 1984; foreword). APL was selected as the development tool for DELAWARE, because the rapid prototyping capabilities of APL facilitates prompt responsiveness to changes with end-users' requirements.

DELAWARE combines delphi, Interpretive Structural Modelling (ISM), and Cross-Impact Analysis (CIA) into an integrated software package (Cundiff, 1985; 173);

Delphi is a communication medium for obtaining the subjective evaluations from a group of experts $^{1}$ considering future developments $^{2}$ (Turoff, 1975; 85–87). Delphi allows panellists to revise their initial judgements - as many times as agreed upon by the group - subsequent to viewing the group's aggregated judgements (Turoff, 1975; 85–87). The emphasis behind delphi is its ability to encourage equality of participation - each participant is unaware of the others' responses (Turoff, 1975; 85–87).

ISM is a time saving tool that facilitates the reduction of the complexity surrounding the interactions between specific developments. Emerging evidence suggests that the human brain is severely limited in dealing with complex problems (R. Waller, 1975; 105) and a technological response to this situation, is the supportive role of ISM to the understanding and solution of complex problems. The theory of ISM was founded in the early 1970's by Warfield (Warfield, 1972, 1973, 1974) and is currently recognised because of the inherent simplicity and breadth of application (Cundiff, 1991b; 2). ISM is described as a guideline that provides a measure of understanding on the potential consequences of the relationships between system elements (Linstone, et. al. 1979; 14 cited in Cundiff, 1991b; 2).

CIA is an extension on either delphi or ISM, permitting experts to consider interactions between specific developments (Lonsdale, 1978; 223–226). The purpose of CIA is not to aim at perfection, but to obtain a marginal improvement on one's understanding of the impacts between developments (Helmer, 1977; 19).

The purpose of the delphi, ISM, and CIA functional components offered by DELAWARE, is concerned more with supporting interpersonal communication rather than supporting a fact finding mission. GDSS can be classified according to three levels of information exchange (DeSanctis and Dickson, 1987);

"A Level 1 GDSS seeks to improve the decision path which the group naturally prefers by removing barriers known to inhibit group effectiveness.

A Level 2 GDSS adds structure to the natural process selected by a group and results in smoothing the path used by the group to reach a decision. A Level 3 GDSS imposes new decision structures or paths which fundamentally change the decision process used by the group." (DeSanctis and Dickson, 1987; 4).

DELAWARE falls into the Level 1 category by encouraging anonymity that reduces common barriers to group work and communication such as unequal consideration of ideas, dominance by individuals, peer pressure, and loss of autonomy (Huber, 1982; 92; Kraemer and King, 1988; 128). The three functional components offered by DELAWARE means that it also falls into the

![](/api/attachments/7QCVNT99/fulltext/images/f91116cdb67854e1679de484998c6065892f1fb366cb6c19bda17562edcdc2b5.jpg)

Level 2 category of GDSS. Each of the functional components structure the group's work and decision processes (Kraemer and King, 1988; 128) and also offer mathematical techniques (Gallupe et al., 1988; 278). For example delphi enables a group to collectively quantify their opinions in terms of both probability and desirability and the statistical results – described in Figure 3 – are made available to panellists.

From another perspective, DELAWARE would also be categorized as a single-user GDSS, where one group member is in charge of operating the software (Gallupe et al., undated; 3). DELAWARE can be utilized in either a synchronous or asynchronous environment. In a synchronous environment DELAWARE can be linked to an electronic blackboard that facilitates presentation of analysis results. In an asynchronous environment, questionnaires and analysis output can be facsimilied to panellists.

An alternative arrangement is to organize DELAWARE as a multi-user GDSS, whereby all group members have access to computer terminals to input and view information (Gallupe et al., undated; 3). The multiuser arrangement would be run in synchronous or asynchronous environments similar to single-user GDSS, with the exception that panellists using the multiuser environment would communicate via computer terminals rather than facsimile. DELAWARE is currently being developed to support multiuser capability. The refinement of DELAWARE is proceeding as an evolutionary prototyping process (L. Gibson, 1982; Hekmatpour and Ince, 1987), where an earlier version of DELAWARE is being refined as a result of previous investigations.

Current investigation on the usability of DELAWARE, has emanated from an application involving the future business environment for the

European automotive industry toward the year 2000. In total five panellists from Battelle Geneva and Battelle Frankfurt participated in the DELAWARE application. Battelle is an institute that serves industry and government in the invention, generation, application, and commercialisation of technology (Battelle Europe: guide to available studies). The Battelle DELAWARE application described in the next section below, is used within this paper as a means for examining the closed and closed/open layers. This examination can in turn be related to other GDSS that need to address similar design issues.

## 3. The closed and closed/open layers of functionality

The Battelle DELAWARE application initially used delphi and CIA components under the constraint of a closed layer. It was observed by the Battelle panellists that the existing DELAWARE prototype imposed too much restriction on their decision-making processes and that a closed/open layer was preferable.

Figure 3, presents the round-1 questionnaire sheet that was distributed to the Battelle panellists. The panellists were encouraged to quantify their judgements about the probability and desirability of the future occurrence of thirty four developments – two of which are depicted in figure three. The panellists requested knowledge level as a third dimension, indicating their need for a broader decision-making path.

A closed/open layer would enable panellists to agree on the judgement making dimensions, suited to their particular task requirements. Turoff (1975; 84–92) in his description of a Delphi based system (named Policy Delphi), describes three additional dimensions including: feasibility, importance and confidence. Other judgement making dimensions could exist that are not anticipated by the GDSS designer. Panellists should therefore be provided the flexibility to devise their own judgement making dimension/s.

INTER-ROUND ANALYSIS 1 17/7/1990

<table><tr><td>DEV</td><td>MEAN</td><td>MIN</td><td>MAX</td><td>Q1</td><td>Q2</td><td>Q3</td><td>IQR</td><td>H</td><td>COR</td><td colspan="4">FREQUENCY</td><td colspan="4">VECTOR</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1D</td><td>.75</td><td>.50</td><td>.99</td><td>.72</td><td>.77</td><td>.85</td><td>.13</td><td>1.75</td><td>.37</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>3</td><td>1</td><td>1</td></tr><tr><td>P</td><td>.90</td><td>.75</td><td>.99</td><td>.85</td><td>.93</td><td>.96</td><td>.11</td><td>.81</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>4</td></tr><tr><td>34D</td><td>.41</td><td>.25</td><td>.75</td><td>.28</td><td>.40</td><td>.55</td><td>.28</td><td>2.86</td><td>.41</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>P</td><td>.68</td><td>.40</td><td>.95</td><td>.55</td><td>.75</td><td>.85</td><td>.30</td><td>2.03</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>2</td><td>1</td><td>1</td></tr><tr><td colspan="20">Fig. 4.</td></tr></table>

Observing figure three it is evident that DELAWARE limits the mode of information exchange, by constraining the way panellists can convey their judgements. DELAWARE offers a quantitative percentage format that corresponds to relative descriptive phrases. Several of the Battelle panellists pointed out that their interpretation of the judgement value .70 for instance could vary. The closed/open layer would provide panellists with the opportunity to formulate and describe their own method for conveying judgements.

Figure 4 depicts an inter-round analysis that provides summary statistics on panellists' round 1 judgements. The column headings indicate that the inter-round analysis provides statistics that includes the mean, minimum, maximum, percentiles, inter-quartile range, entropy, correlation coefficient, and frequency vector. Both the fixed type and fixed presentation format of the summary statistics in figure four, could constrain panellists' decision path. For instance, panellists are not given the opportunity to nominate a selection of analysis tools, or choose the presentation format of the analysis output. Most panellists participating in the Battelle application preferred graphical presentations that indicate where individual judgments lie in relation to other panellists. To accommodate this type of request, the closed/open layer would enable panellists to specify the required statistical analysis features and presentation formats.

Subsequent to panellists revising their initial round one judgements, they may undertake a CIA. Figure 5 illustrates part of a CIA questionnaire presented to Battelle panellists. Observing from Figure 5, the constraint placed on panellists' mode of communication, is that they must make a numeric judgement between plus or minus two. The closed/open layer would provide panellists with the opportunity to describe a numeric or descriptive scale of their preference.

![](/api/attachments/7QCVNT99/fulltext/images/84ac99b2b123ae2064a4b10ac1d8864e9803d90a28e208ce07e6c6cec8c10cc4.jpg)

In summary the Battelle DELAWARE application illustrates that the earlier DELAWARE prototype imposed too much closure on the functionality offered by delphi and CIA, relative to the Battelle panellists' knowledgeable skill level and the task requirements. It is intended that novice end-users migrate toward using the closed/open concept after a few hours training and demonstration. It is envisaged (and in this case was evident by the positive responses from the Battelle panellists), that the short term costs in training would be small, relative to improvements with the panellists' performance and acceptance of the system.

## 4. The open / closed layer of functionality

A demonstration of a DELAWARE ISM application presented below – borrowed from Cundiff (1991a) – is used to examine the open/closed layer. To undertake the ISM process the end-user needs to perform the following eight steps within an APL workspace. The commands used in this example are termed direct definitions – command language based – and were programmed by Cundiff (1991b).

Step one - creating the empty matrix: An initial empty matrix of size $N$ by $N$ is generated with the command $\mathbf{B}^{\wedge}\mathbf{N}$ , where the $N$ represents a numeric value chosen by the end-user. For example, matrix one indicates that the end- user requires a six by six matrix.

$$
\begin{array}{c c c c c c} \text {Matrix one} \\ \text {Empty matrix} \\ \hline 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & o & o & o \end{array}
$$

Step two - creating the identity matrix: The identity matrix - described in matrix two - is a necessary component for binary calculations within matrices and is generated with the command I^.

Matrix two
Identity matrix

<table><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

Step three - building the adjacency matrix: Issuing the command RA^C produces the adjacency matrix depicted in matrix three. The adjacency matrix constitutes the intersections of both R (row number) and C (the relative column value) that reflect some pre-determined relationship.

Matrix three
Adjacency matrix

<table><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

Step four - generating the reachability matrix: The command $\mathbf{P}^{\wedge}$ adds the identity matrix to the adjacency matrix and iteratively powers to obtain a reachability matrix - described in matrix four. The reachability matrix identifies transitive dependency, where for instance, element one may indirectly influence element three, only because element one directly influences element two and element two directly influences element three.

Matrix four
Reachability matrix

<table><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

Issuing the command $R \leftarrow RS^{\wedge}$ returns the set reachable from another element and described in matrix five.

## Matrix five

The set reachable from another element

<table><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>6</td></tr><tr><td>0</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>6</td></tr></table>

Step five - create the antecedent set: Given a set of elements $(Si)$ , an antecedent set $A(Si)$ is defined as all those elements on relationship paths that terminate at $Si$ (Cundiff, 1991a; 3). In other words the antecedent matrix below distinguishes between whether there is either a direct or transitive impact relationship, and where no impact relationship of any kind exists (denoted by a zero). The command $R \leftarrow AS^{\wedge}$ returns the antecedent set as described above and the outcome is presented in matrix six.

## Matrix six

Antecedent matrix

<table><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>6</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>5</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>6</td></tr></table>

Step six - creating the intersection matrix: The command $\mathbf{R} \leftarrow \mathbf{IS}^{\wedge}$ returns the intersection of the reachability matrix and the antecedent matrix and the outcome is presented in matrix seven. "The set intersection supplies the data needed to further partition the system into subsystems" (Cundiff, 1991a; 11).

## Matrix seven

Intersection matrix

<table><tr><td>1</td><td>0</td><td>0</td><td>4</td><td>0</td><td>6</td></tr><tr><td>0</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>0</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>0</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr></table>

Step seven - hierarchical restructure into block-triangular form: The command $\mathrm{HR}^{\wedge}$ hierarchically restructures the reachability matrix in block-triangular form. Matrix eight below indicates that elements four and six belong to a separate group by themselves. The remaining elements form a second group, where element one is on the top level hierarchy by itself, while elements two, three, and five are on one level lower.

## Matrix eight

Hierarchically restructured reachability matrix

<table><tr><td></td><td>4</td><td>6</td><td>2</td><td>3</td><td>5</td><td>1</td></tr><tr><td>4</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>6</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Step eight - hierarchical restructure into block-triangular form: The command $\mathrm{HD}^{\wedge}$ hierarchically restructures the development set in block-triangular form as in $\mathrm{HR}^{\wedge}$ and replaces the boolean value one with the appropriate element identification number. The result is presented in matrix nine.

## Matrix nine

Hierarchically restructured element set

<table><tr><td></td><td>4</td><td>6</td><td>2</td><td>3</td><td>5</td><td>1</td></tr><tr><td>4</td><td>4</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>6</td><td>4</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td><td>2</td><td>3</td><td>5</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>2</td><td>3</td><td>5</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>2</td><td>3</td><td>5</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>2</td><td>3</td><td>5</td><td>1</td></tr></table>

In summary the ISM demonstration described above enables the experienced end-user to use a command language that provides direct access to the point of processing, hence saving the end-user time by eliminating their need to wade through a menu system. However, the experienced end-user needs to invest the time to become fully acquainted with the functions offered through the command language.

Similar command language features could be offered for both the delphi and CIA functional components. The interface design could adopt a layered command language structure discussed in previous research (Sprague and Carlson, 1982), to facilitate end-users varying usage sophistication.

## 5. The open layer of functionality

The purpose of the open layer is to provide end-users with the flexibility to customise the

<table><tr><td colspan="17">Matrix tenImpact matrix from Battelle CIA application</td><td></td><td></td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td></tr><tr><td>1</td><td>0</td><td>-0.8</td><td>0</td><td>1</td><td>1</td><td>1.3</td><td>1</td><td>1.3</td><td>0</td><td>0.3</td><td>-1</td><td>0</td><td>0.3</td><td>1.3</td><td>0</td><td>1.5</td><td>1</td><td>0.8</td></tr><tr><td>2</td><td>0.5</td><td>0</td><td>0.3</td><td>-1</td><td>-0.8</td><td>-0.3</td><td>0</td><td>0</td><td>1.3</td><td>0.8</td><td>1</td><td>0</td><td>-0.3</td><td>0</td><td>-0.5</td><td>0.3</td><td>-1</td><td>0.5</td></tr><tr><td>3</td><td>0</td><td>-0.3</td><td>0</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>1</td><td>0.8</td><td>-0.3</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0.8</td><td>1.5</td><td>1</td><td></td></tr><tr><td>4</td><td>0</td><td>0.5</td><td>1</td><td>0</td><td>1.5</td><td>1.5</td><td>1</td><td>1.3</td><td>-0.5</td><td>0</td><td>0</td><td>0</td><td>1.5</td><td>1</td><td>1.5</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>-0.3</td><td>0.3</td><td>0.5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1.5</td><td>0</td><td>0.3</td><td>0</td><td>0</td></tr><tr><td>6</td><td>0</td><td>0.1</td><td>0.6</td><td>0.3</td><td>0.8</td><td>0</td><td>0.8</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.8</td><td>1</td><td>1.5</td><td>0</td><td>0</td></tr><tr><td>7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.3</td><td>1.5</td><td>0</td><td>0.3</td></tr><tr><td>8</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0.8</td><td>0</td><td>0</td><td>0</td><td>-0.8</td><td>0.3</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.8</td><td>1</td><td>0</td><td>0.8</td></tr><tr><td>9</td><td>0.3</td><td>0</td><td>0.7</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>1.5</td><td>0</td><td>1.2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1.5</td><td>1</td><td>0.9</td></tr><tr><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.8</td><td>-0.8</td><td>0</td><td>0</td><td>0</td><td>-0.3</td><td>0</td><td>0</td><td>1.5</td><td>1</td><td>0.5</td></tr><tr><td>11</td><td>0.5</td><td>1.5</td><td>0.5</td><td>0</td><td>-0.8</td><td>0.8</td><td>0.8</td><td>-0.5</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>-0.5</td><td>0</td><td>-1</td><td>-0.3</td><td>0.5</td><td>0</td></tr><tr><td>12</td><td>0</td><td>1.4</td><td>0.3</td><td>0.3</td><td>-1</td><td>0</td><td>0</td><td>1</td><td>0.8</td><td>0.8</td><td>1</td><td>0</td><td>0.3</td><td>0.5</td><td>1</td><td>1</td><td>-0.3</td><td>0.3</td></tr><tr><td>13</td><td>0</td><td>0.4</td><td>0.3</td><td>0.5</td><td>0.3</td><td>0.5</td><td>0.5</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.8</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>14</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.8</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td></tr><tr><td>15</td><td>0</td><td>0</td><td>0.3</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td></tr><tr><td>16</td><td>0</td><td>-0.3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1.3</td><td>-0.5</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td></tr><tr><td>17</td><td>0</td><td>-0.3</td><td>0.3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.8</td><td>-1</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td></tr><tr><td>18</td><td>0.3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1.5</td><td>1</td><td>1.3</td><td>0.3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr></table>

GDSS to suit task requirements that the designer either did not anticipate, or thought not worthwhile. Often new technology is utilized to do other things that the designer had not intended or predicted (Rubin 1989; 28). The open layer enables end-users to modify the GDSS in terms of altering the data flows between the functional components, altering the structure of the existing functional components, and adding new functional components.

Two examples below demonstrate how end-users are able to make use of the flexibility provided by the open layer.

The first example is a data transfer process, and is considered by the designer as an uncommon task requirement that would not be included within the design of the package. The example illustrates automating the transfer of data between CIA and ISM, to determine if the grouping relationships between developments from an initial ISM application, were altered as a consequence of a subsequent CIA application. A second ISM application (subsequent to the CIA application) would determine any change in the grouping relationships between developments.

The data transfer involves taking the aggregated impact values such as those created within the Battelle CIA application (shown in matrix ten below), and substituting impact values zero with binary values 0 and non-zero impact values with binary values 1. The APL program named CONVERT, presented in Appendix 1, was developed by the researcher to automatically convert the impact values to their equivalent binary form and to place them in the adjacency matrix previously described in matrix three above. Typing the word CONVERT replaces step three of the ISM application described above and eliminates tedious data entry.

The second example illustrates an alteration of the physical structure of ISM rather than the conceptual structure. For instance, from the initial ISM demonstration above, it is evident that some ISM features can be made transparent to the end-user. For example, subsequent to the end-user describing the empty matrix with the command B^N (where N represents the size of the matrix), the identity matrix could be generated automatically. In addition, after entering the contextual relations in the adjacency matrix, the reachability matrix – obtained by issuing the command P^ - could also be generated automatically. Introducing transparency of this nature, in a sense, imposes a degree of closure on the ISM. However in another sense, the decision path that ISM supports, is not being affected in any way, because the two steps being automated are bounded by the natural progression of any ISM application.

In summary, to make any changes to DELAWARE (such as the changes made with both example 1 and example 2 above), end-users need to commit time and effort to learning, development, and training. Time and effort will only be saved relative to the number of applications that use the changes, compared with the time and effort required to make the changes. In the case of both examples one and two above, time and effort are saved by eliminating data entry, but only after a number of applications have accrued time savings relative to the time taken to either develop or alter the programmes respectively.

It is expected that any modifications to the GDSS, would be undertaken in a two stage process. The first stage would require the end-users to conceptualise any required modifications. The second stage would involve applications programmers, to undertake the technical development.

It is important to note that if programming standards aren't maintained, then any changes made to the GDSS may make it difficult for other end-users to make future changes. In addition, any syntactic or semantic errors created by any changes, may have deleterious consequences for the integrity of other interdependent functions within the GDSS. It is therefore necessary that time is allocated to ensure that the revised the GDSS package is completely tested. To assist with the testing process, the designer should provide an automated tracking facility that monitors both what and how functions are affected by any saved changes made to any other functions (either new or altered).

## 6. Discussion

If GDSS is to emerge as a successful commercial product, then its design needs to be based upon a concept of functionalism. Functionalism is described as “... the theory of design that the form of a thing should be determined by its use”

(Collins English Dictionary, 1983; 588). In other words the manner in which the functionality of GDSS support end-users task requirements, current skill level, and skill acquisition needs, should be determined by the end-users themselves. It is argued that design evaluations are end-user centred, as information is provided about potential end-users and ensures that the design minimizes the intrusion of the system upon the task (Rubin 1989; 167).

End-user centred design evaluations will help ensure that GDSS appear natural to end-users. This state of perceived naturalness was evident in previous studies on DSS, where several authors (Jungermann, 1980; Pitz, 1983; Stabell, 1983; cited in Kottemann and Remus, 1989; 171) argued that DSS design must be congruent with the cognitive and behavioural strategies used by decision makers. They suggest that such naturalness makes DSS easier to learn and use, and lessens the chance that DSS imposes inappropriate normative decision-making processes (Kottemann and Remus, 1989; 171). Other authors add that

"Research on skill acquisition shows that humans usually develop qualitatively different perceptions of a task and/or mode of decision making as their skill improves (Dreyfus and Dreyfus, 1986). In an organisational setting a system must be robust enough to support users with varying levels of expertise. It is crucial to understand differences between high- and low-skill employees' approaches to problem-solving in order to design a system that adequately supports their strategies." (Lamberti and Wallace, 1990; 281).

Future research will have to examine the possibilities concerning GDSS support of a mixture of end-users with different skill levels undertaking the same application. Emphasis would be placed on encouraging the more skilful end-users to guide the less skilful end-users in acquiring new skills, so that all of the end-users are able to use the higher layer.

In addition, if the GDSS is to appear natural to the end-users, they must be given complete control over usage, through choosing an appropriate layer (in terms of usage sophistication and task requirements). The key to optimizing the performance of a range of end-users with varying skills is the flexibility to choose options (Walther and O'Neil 1974). Research on decisional control demonstrates that when end-users have the power to choose, they perceive control over their environments (Baronas and Louis, 1988; 114). Designing closed, closed/open, open/closed, and open layers, provides end-users with a choice – and greater control – over how they wish to match both their usage sophistication and task requirements, with the desired layer.

It is likely that expert end-users will effect greater decision performance relative to the less skilful end-users for the more difficult tasks, because the expert end-users have greater flexibility to match a layer with the task requirements. In contrast, flexibility of choice may impair ease-of-use for either the novice, knowledgeable, or experienced end-users (Goodwin, 1987; Davis, 1989), because these end-users may not understand when or why to use the more sophisticated options. The less sophisticated end-users may also perceive the relatively higher layers as being complicated and not at all easy to use. It is therefore essential that during skill acquisition processes, end-users be provided guidance – either through training, manuals or help screens – on the what, when, why and how they should use the various options.

Researchers have found that even with prior training, end-users undertake considerable learning during the use of a software package (Bergeron, et. al., 1990; 248). Other studies have found that in order to support this learning, ongoing support must be provided to end-users, either through documentation or human advisers (Eason et al., 1975; Martin et al., 1973; cited in Bergeron et al., 1990; 248). The processes involved with skill acquisition presents difficulties for the designer, the end-users' organisation, and the end-users themselves.

The challenge for the designer, is to accommodate end-users with skill levels that are progressing from the novice through to the expert levels. For instance, the designer will have to provide end-users with facilities to learn more about the functional components of DELAWARE, the command language and possibly APL. Any expenditure in time or effort needed to facilitate skill acquisition, should be considered by the organisation employing the end-users, as a long-term investment. Especially since economies of scales could be achieved – in terms of the end-users passing on acquired skill to other applications and other end-users – and the accrument of better performance in using the GDSS, could result in both quantitative savings and qualitative benefits – such as improved decision-making. Organisations must initially be prepared to invest in end-users' time and effort, encouraging end-users to become completely familiar with using the technology from an open layer. In congruence with this encouragement, end-users' themselves need to have the motivation to migrate from the closed layer through to the open layer.

## 7. Conclusion

This paper has considered an alternative perspective concerning GDSS design issues. Central to the adopted perspective, is the ability of GDSS to provide end-users with the flexibility to choose a layer of functionality that suits their task requirements, current skill level, and skill acquisition needs.

For the purposes of this study end-users are categorized as either novice, knowledgeable, experienced and expert For each of the four skill levels there exist an appropriate layer that include closed, closed/open, open/closed, and open layers. The closed layer offers a rigid approach toward using the GDSS, with the aim of encouraging novice end-users to become knowledgeable end-users after a few hours use. The closed/open layer facilitates the selection of parameters within the functional components. The open/closed layer provides experienced end-users with a command language that enables them to use functions faster compared with a menu system. The open layer enables expert end-users to modify the GDSS.

End-users vary in their task requirements, skill levels, and skill acquisition needs, that in turn present a variety of contentions. For the less sophisticated end-users, the closed layers are relatively easier to learn and use. However, these end-users are more constrained in being able to apply their creative abilities and assume less control over structure of the decision making process. Ultimately it is preferable that end-users acquire expert status so that optimal use can be made of the GDSS. Skill acquisition necessitates investment in human resources such as time and effort, and such resources may be extremely scarce, or information overload may reduce the overall performance of this resource. Such costs have to be weighed against improvements in the end-users' performance – including decision quality and decision speed. In addition the end-users themselves will need to have the motivation to step out of their comfort zones and acquire the necessary skills.

## Acknowledgements

I would like to thank Bill Cundiff for both his initial and continued development of DELAWARE and for his noteworthy efforts in providing valuable feedback. My appreciation is also extended to the distinguished panel at both Battelle Genva and Battelle Frankfurt, for their valuable contributions toward evaluating the software package.

## References

[1] Alavi, M. and Henderson, J.C. "An Evolutionary Strategy for Implementing a Decision Support System," Management Science (27:6), November 1981, pp. 1309-1323.

[2] Baronas, A-M.K. and Louis, M.R. "Restoring a Sense of Control During Implementation: How User Involvement Leads to System Acceptance," MIS Quarterly, March 1988, pp. 110–124.

[3] Battelle Europe: A Guide to the Available Studies, undated.

[4] Benbasat, I. and Dexter, A.S. "An Investigation of the Effectiveness of Color and Graphical Presentation Under Varying Time Constraints, MIS Quarterly (10:1), March 1986, pp. 59–84.

[5] Bennett, J.L. “Incorporating Usability into System Design: The Opportunity for Interactive Computer Graphics,” in: Proceedings of the International Conference on Cybernetics and Society (Tokyo-Kyoto, Japan, Nov. 3–7). Institute of Electrical and Electronics Engineers, New York, 1978, pp. 1119–1124.

[6] Bennett, J.L., Building Decision Support Systems, Addison-Wesley, 1983.

[7] Bergeron, F., Rivard, S., and De Serre, L. "Investigating the Support Role of the Information Centre," MIS Quarterly, September 1990, pp. 246–260.

[8] Bewley, W.L., Roberts, T.L., Schoit, D. and Verplank, W.L., "Human Factors Testing in the Design of Xerox's 8010 'Star' Office Workstation," CHI '83 Human Factors in Computing Systems, Boston, December 12–15, 1983, ACM, New York, NY, pp. 72–77.

[9] Brown, S.T., “From Cognitive to Social Ergonomics and Beyond,” in User Centered Systems Design: New Perspectives on Human-Computer Interaction, Norman, D.A., and Draper, S.W., eds., Lawrence Erlbaum Associates, Hillsdale New Jersey, 1986, pp. 457–486.

[10] Cawelti, S. "Interpretive Structural Modeling," Iowa English Bulletin, vol. 33, nos. 1 & 2, 1989, pp. 24–25.

[11] Cundiff, W.E. "Technical Note: Interactive Software for the Capture, Management, and Analysis of Data in DELPHI Inquiries," Technological Forecasting and Social Change (28:2), 1985, pp. 173–185.

[12] Cundiff, W.E. “Interactive Software for the Capture, Management, and Analysis of Data in DELPHI Inquiries: Defined Functions in APL,” Technological Forecasting and Social Change (34:2), 1988, pp. 185–195.

[13] Cundiff, W.E. "DSS Structure and Algorithmic Transparency in APL," to be published in APL QUOTE QUAD, 1991a.

[14] Cundiff, W.E., Model Structure, Complexity, and Algorithmic Transparency in APL, to be published in Applied Mathematical Modelling, 1991b.

[15] Davis, F.D. Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology, MIS Quarterly, September 1989, pp. 318–340.

[16] Davis, F.D., Bagozzi, R.P. and Warshaw, P.R., User Acceptance of Computer Technology: A Comparison of Two Theoretical Models, Management Science (35:8), August 1989, pp. 982–1003.

[17] Dennis, A.R., George, J.F., Jessup, L.M., Nunamaker, J.F., and Vogel, D.R., Information Technology to Support Electronic Meetings, MIS Quarterly, December 1988, pp. 591–624.

[18] DeSanctis, G. and Dickson, G.W., GDSS: A Shell System in Support of a Program of Research, Proceeding of the 20th Annual Hawaii International Conference on System Sciences, Kona, HI, 1987, pp. 1–22.

[19] DeSanctis, G. and Gallupe, B., Group Decision Support Systems: A New Frontier, Data Base, (16:2), Winter 1985, pp. 3–10.

[20] Dickson, G.W., DeSanctis, G. and McBride, D.J., Understanding the Effectiveness of Computer Graphics for Decision Support: A Cumulative Experimental Approach, Communications of the ACM (29:1), January 1986, pp. 40–47.

[21] Dreyfus, H.L. and Dreyfus, S.E., Mind Over Machine - The Power of Human Intuition and Expertise in the Era of the Computer, The Free Press, New York, NY, 1986.

[22] Eason, K.D., Domodovan, L. and Stewart, T.F.M., Interface Problems in Man-Computer Interactions, in Human Choice and Computers, E. Mumford and H. Sackman (eds.), North-Holland, Amsterdam, 1975, pp. 91–105.

[23] Gallupe, B.R., Decision Lab: Current Status - Future Projects, Unpublished working paper, April 1988.

[24] Gallupe, B.R., Suppressing the Contribution of the Group's Most Proficient Member: Is GDSS Use Appropriate For All Group Tasks?, unpublished, undated.

[25] Gallupe, B.R., Bell, B.T. and Yates, B.R. Enhancing the Productivity of Managerial Meetings: Can Real-Time Computer Support Help?, Unpublished, undated, p. 3.

[26] Gallupe, B.R., DeSanctis, G. and Dickson, G.W., Computer-Based Support for Group Problem-Finding: An Experimental Investigation, MIS Quarterly, June 1988, p. 278.

[27] Gibson, L., Designing User-Friendly APL systems; in 1982 APL Users Meeting: Proceedings, Special Technical Topics, Designing APL Systems, vol II, I.P. Sharp Associates Ltd., Toronto, Ontario, 1982, p. 7.

[28] Gilman, L. and Rose, A.J. APL: An Interactive Approach, Johnson Wiley & Sons Inc., 1984.

[29] Gray, P., Group Decision Support Systems, Elsevier Science Publishers B.V., North-Holland, 1987, pp. 233–237.

[30] Gray, P., Using Group Decision Support for Crisis Management, Claremont Graduate School, Information Science Applications Centre, 1988, p. 4.

[31] Gray, P., Aronofsky, J.S., Kane, G., and Perkins, T.E., The SMU Decision Room Project, Proceedings of the Chinese-U.S. Symposium on Systems Analysis, John Wiley and Sons, Inc., 1983, pp. 309–322.

[32] Goodwin, N.C., Functionality and Usability, Communications of the ACM (30:3), March 1987, pp. 229–233.

[33] Hale, D.P., Haseman, W.D., and Munro, D.L., Architectural Requirements for Integrating Group Decision Support Systems Into the Daily Managerial Experience, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, vol. Ill, 1989, pp. 321–325.

[34] Hekmatpour, S. and Ince, D.C. (1987). Evolutionary prototyping and the human-computer interface. In: H.J. Bullinger and B. Shackel (Eds). Proceedings of the Second IFIP Conference on Human-Computer Interaction-INTER-ACT '87. Stuttgart, Federal Republic of Germany, 1–4 September. London: North-Holland.

[35] Helmer, O., Problems in Futures Research: Delphi and Causal Cross-Impact Analysis, Futures, IPC Business Press Ltd., (9), February 1977, p. 19.

[36] Hiltz, S. and Turoff, M. The Network Nation: Human Communication Via Computer, Addison-Wesley, Reading, Mass., 1978.

[37] Hiltz, S. and Turoff, M. Top Decisions: Strategic Decision-Making in Organisations, Jossey-Bass Inc. Publishers, 1986.

[38] Huber, G.P., Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques,?, 1982, pp. 96–108.

[39] Huber, G.P., Issues in the Design of Group Decision Support Systems, MIS Quarterly (8:3), September 1984a, pp. 195–204.

[40] Huber, G.P., The Nature and Design of Post-Industrial Organisations, The Institute of Management Sciences (30:8), August 1984b, pp. 934–937.

[41] Jarvenpaa, S.L., Rao, V.S., and Huber, G.P., Computer Support for Meetings of Groups Working on Unstructured Problems: A Field Experiment, MIS Quarterly, December 1988, (12), pp. 645–666.

[42] Jessup, L.M., Connolly, T., and Galegher, J., The Effects of Anonymity on GDSS Group Process With an Idea-Generating Task, MIS Quarterly, September 1990, 313–321.

[43] Johansen, R., Groupware: Computer Support for Business Teams, Collier Macmillan Pub., 1988.

[44] Johansen, R., Vallee, J. and Spangler, K. Electronic Meetings, Addison-Wesley, Reading, Mass., 1979.

[45] Jungermann, H. Speculations about Decision-Theoretic Aids for Personal Decision Making, Acta Psychologica (45:1–3), August 1980, pp. 7–34.

[46] Kraemer, K.L. and King, J.L. Computer-Supported Conference Rooms: A State of the Art Assessment. Public Policy Research Organisation, Univ. of California, Irvine, Calif., 1983.

[47] Kraemer, K.L. and King, J.L., Computer-Based Systems for Cooperative Work and Group Decision Making, ACM Computing Surveys (20:2), June 1988, pp. 115, 128.

[48] Kottemann, J.E. and Remus, W.E., A Study of the Relationship Between Decision Model Naturalness and Performance, MIS Quarterly (?), June 1989, pp. 170–181.

[49] Lai, K.Y., Malone, T.W., and Yu, K.C., Object Lens: A Spreadsheet for Cooperative Work, ACM Transactions on Office Information Systems, 1988.

[50] Lamberti, D.M. and Wallace, W.A., Intelligent Interface Design: An Empirical Assessment of Knowledge Presentation in Expert Systems, MIS Quarterly, September 1990, pp. 278–311.

[51] Liang, T.P., Model Management for Group Decision Support, MIS Quarterly, December 1988, pp. 667–680.

[52] Linstone. H.A., Lendaris, G.G., Rogers, S.D., Wakeland, W. and Williams, W., The Use of Structural Modelling for Technological Assessment, Technological Forecasting and Social Change (14), pp. 291–327.

[53] Lonsdale, A., Judgemental Research in Policy Analysis, Futures, IPC Business Press Ltd., (10), June 1978, pp. 223–226.

[54] Malone, T.W., Grant, K.R., Turbak, F.A., Brobst, S.A., and Cohen, M.D., Intelligent Information-Sharing Systems, Communications of the ACM, (30:5), May 1987, pp. 390–402.

[55] Martin, J.H., Carlisle, J.H. and Tren, S., The User Interface for Interactive Bibliographic Searching: An Analysis of the Attitudes of Nineteen Information Scientists, Journal of the American Society for Information Sciences (24:2), March-April 1973, pp. 47–66.

[56] Meadow, C.T., User Adaptation in Interactive Information Retrieval, J. Am. Soc. Inf. Sci. (34:4), July 1983, pp. 289–291.

[57] Nunamaker, J.F., Applegate, L.M., and Konsynski, B.R., Facilitating Group Creativity: Experiencing with a Group Decision Support System, in Journal of Management Information Systems (3:4), Spring 1987, pp. 5–19.

[58] Nunamaker, J.F., Konsynski, B.R., Chen, M., Vinze, A.S., Chen, I.L., and Heltne, M.M., Knowledge-based Systems Support for Information Centers, IEEE, (4), 1988, pp. 96–105.

[59] Palese, V.J., Top Down Budgeting: A Fair-Share Approach, Xerox Corporation, Rochester, New York, undated.

[60] Phillips, L.D., People-Centred Group Decision Support, Knowledge Based Management Support Systems, Doukidis, G., Land, F., and Miller, G., (eds), Ellis Horwood, October 1988.

[61] Phillips, L.D., Decision Analysis for Group Decision Support, Decision Analysis Unit, unpublished, undated.

[62] Pitz, G.F., Human Engineering of Decision Aids, in Analyzing and Aiding Decision Processes, P. Humphreys, O. Svenson, and A. Vari (eds.), North-Holland, Amsterdam, Holland, 1983, pp. 205–221.

[63] Poole, M.S., Seibold, D.R. and McPahee, R.D., Group Decision- Making as a Structurational Process, Quarterly Journal of Speech, 1985, pp. 71–102.

[64] Rubin, T., User Interface Design For Computer Systems, E. Horwood Publication, NY, 1988, p. 167.

[65] Sprague, R.H. and Carlson, E., Building Effective Decision Support Systems, Prentice-Hall, INC., 1982.

[66] Sprague, R.H. and Watson, H.J., Decision Support Systems: Putting Theory into Practice, R. Sprague and H. Watson (eds.), Prentice-Hall, 1986, pp. 1–3.

[67] Stabell, C., A Decision-Oriented Approach to Building DSS, in Building Decision Support Systems, J. Bennett (ed.), Addison-Wesley, Reading, MA, 1983.

[68] Stefik, M., Bobrow, D.G., Foster, G., Lanning, S., and Tatar, D., WYSIWIS Revised: Early Experiences with Multiuser Interfaces, ACM Transactions on Office Information Systems, (5:2), April 1987, pp. 147–167.

[69] Stefik, M., Foster, G., Bobrow, D.G., Kahn, K., Lanning, S., and Suchman, L., Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings, Communications of the ACM, (30:1), January 1987, pp. 32–47.

[70] Stefik, M., and Brown, J.S., Toward Portable Ideas, Technical Support for Work Group Collaboration, Olsen, M.H. (ed), Lawrence Erlbaum Pub., 1989, pp. 147–165.

[71] Turoff, M., The Policy Delphi, Technological Forecasting and Social Change, Addison-Wesley Pub. Co. Inc., 1975, pp. 84–92.

[72] Waller, R.J. Portraits of Complexity: Applications of Systems Methodologies to Societal Problems, Battelle Monograph, (Battelle, Columbus, Ohio) no. 9, June 1975, p. 105.

[73] Walther, G.H., and O'Neil, H.F., Jr. On-Line User-Computer Interface-The Effects of Interface Flexibility, Terminal Type, and Experience on Performance. In AFIPS Conference Proceedings (43), (Chicago, Ill., May 6–10), AFIPS Press, Reston, Va., 1974, pp. 379–384.

[74] Warfield, J.N., A Unified Systems Engineering Concept, Battelle Monograph (Battelle, Columbus, Ohio) no. 1, 1972.

[75] Warfield, J.N., An Assault on Complexity, Battelle Monograph (Battelle, Columbus, Ohio) no. 3, 1973.

[76] Warfield, J.N., Structuring Complex Systems, Battelle Monograph (Battelle, Columbus, Ohio) no. 4, 1974.

[77] Watson, R.T., DeSanctis, G., and Poole, M.S., Using GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences, MIS Quarterly, September, 1988, 463–478.

## Appendix one

APL program named convert

∇CONVERT[□]
[0] CONVERT;ROW;NUMROW;COL;
NUMCOL;AMCOL;VALS

[1] $\mathbf{ROW}\gets 1$

[2] NUMROW $\leftarrow \rho$ NUM

[3] INITIAL: COL ← 12345

[4] AMCOL $\leftarrow 1$

[5] NUMCOL $\leftarrow \rho$ NUM

[6] TEST: $\rightarrow (0 = 1 \times \mathrm{VALS} \leftarrow$

± ISMVAL[ROW;COL])/ROWTEST

[11] AMCOL $\leftarrow$ AMCOL $+1$

$$
[ 7 ] \quad \mathrm{A} \Delta \mathrm{M} [ \text {ROW}; \mathrm{AMCOL} ] \leftarrow 1
$$

[8] ROWTEST: $\rightarrow (1 =$ NUMCOL)/INCROW [12] $\rightarrow$ TEST

[13] INCROW: $\rightarrow (1 = \text{NUMROW}) / \text{FINISH}$

[9] NUMCOL $\leftarrow$ NUMCOL-1

[14] $\mathrm{ROW}\gets \mathrm{ROW} + 1$

[10] $\mathrm{COL}\gets \mathrm{COL} + 55555$

[15] NUMROW $\leftarrow$ NUMROW-1

[16] $\rightarrow$ INITIAL

[17] FINISH: A $\Delta M$
