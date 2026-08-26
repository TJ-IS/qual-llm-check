---
otero_id: 26040
otero_key: "V9STFG7M"
title: "The capability maturity model and CASE"
authors: "L. Mathiassen; C. Sørensen"
year: "1996"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1996.tb00013.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The capability maturity model and CASE

L. Mathiassen & C. Sørensen

Department of Computer Science, Aalborg University, DK-9220 Aalborg, Denmark, e-mail: larsm@iesd.auc.dk and Systems Analysis Department, Risø National Laboratory, DK-4000 Roskilde, Denmark. e-mail: carsten@risoe.dk

Abstract. Many software organizations face serious problems in their attempts to make expectations and realities meet in introducing CASE technology. One promising approach to understanding CASE introduction better and to managing it more effectively has been developed by relating CASE introduction to the Capability Maturity Model (CMM). This paper reviews software process maturity as a framework for CASE introduction. The relevance of the framework is discussed and three critical questions are explored: 1) What is the role of organizational experiments in CASE introduction? 2) How do the functional characteristics of CASE technology influence CASE introduction? and 3) How does the organizational context influence CASE introduction? The aim of the paper, by way of this discussion, is to explicate the strengths and limits of software process maturity as a framework for CASE introduction, and to identify the most important supplementary issues.

Keywords: Software process maturity, the capability maturity model, CASE diffusion

## 1 INTRODUCTION

The Capability Maturity Model (CMM) (Humphrey, 1989a; Humphrey, 1990a; Paulk et al., 1991; SEI, 1991a; SEI, 1991c; SEI, 1991b; Paulk et al., 1993) is a framework for evaluating and improving software processes. The basic assumption is that enhanced process quality is a prerequisite for improved product quality and increased productivity. The framework contains a five-stage model for improving software processes through organizational learning and intervention based on the systematic collection of experiences and data from software projects. CMM has, since it was presented by Humphrey, rightfully gained much interest both among software engineers and researchers (Bollinger & McGowan, 1991; Huff et al., 1991; Huff, 1992; Sion, 1993; Rugg, 1993; Saiedian & Kuzara, 1995).

Humphrey and Curtis have used CMM as a framework to study important prerequisites for, and key activities in, the successful application of CASE technology in software organizations (Humphrey, 1989b; Curtis, 1992). It is suggested that CASE introduction be deferred until a sufficient level of process maturity has been reached. Still, many organizations choose to introduce CASE, even though they find themselves on the lower levels of maturity. In fact, at Hughes Aircraft, a key example of a process improvement effort (Humphrey et al., 1991; Saiedian & Kuzara, 1995), CASE was used before the recommended level of process maturity was reached (Humphrey et al., 1991).

We will survey and evaluate CMM as a framework for CASE introduction. Our objective is to explicate the strengths and limits of software process maturity in this context, and to identify important supplementary issues related to effective CASE introduction. Section 2 provides a brief presentation of CMM. In section 3, we review the key articles by Humphrey (1989b) and Curtis (1992), discussing CASE introduction within the framework of CMM. The subsequent sections explore the limits of this approach by discussing three critical questions related to CASE introduction: What is the role of organizational experiments in CASE introduction (Section 4)? How do the functional characteristics of CASE technology influence CASE introduction (Section 5)? How does the organizational context influence CASE introduction (Section 6)? Finally, section 7 concludes the article.

## 2 THE CAPABILITY MATURITY MODEL

The key assumption behind CMM is that the ideal software process must be predictable. Cost estimates and schedule commitments should be met with reasonable consistency and the quality of the resulting products should generally meet user needs. Few software organizations operate according to this ideal criteria (see for instance Humphrey (1990b)), but software organizations can use CMM as a point of departure for improvements.

According to Humphrey (1990b), organizations must take five steps to improve their software capabilities: 1) Understand the current status of their development processes; 2) develop a vision of the desired process; 3) establish a list of improvement actions in order of priority; 4) produce a plan to accomplish these actions; and 5) commit the resources to execute the plan. CMM has been developed at the Software Engineering Institute as a practical framework to support managers, practitioners, and consultants addressing these five steps. The model characteristics a software process into one of five maturity levels as illustrated in Figure 1.

The five levels of process maturity are (Humphrey, 1990b):

1 The Initial Level: The first level characterizes the immature software process. The process is performed in an ad hoc manner, and is possibly even chaotic. No formalized procedures for performing and managing the software process are applied. Tools are not integrated with the process.

2 The Repeatable Level: On this level, basic project management functions are applied, and both schedules and cost estimates are generally met. Software projects share a set of behavioural patterns that are repeated from process to process.

3 The Defined Level: The organization has now defined, i.e. explicitly described, key features of the process to ensure consistent implementation and provide a basis for gaining insight into the actual performance within projects.

<table><tr><td>Level</td><td>Characteristics</td><td>Result</td></tr><tr><td>5Optimized</td><td>Improved feed-back into processData gathering is automated and used to identify weakest process elementsNumerical evidence used to justify application of technology to critical tasksRigorous defect-cause analysis and detect prevention</td><td rowspan="4">Productivity &amp; quality</td></tr><tr><td>4Managed</td><td>(Quantitative)Measured processMinimum set of quality and productivity measurements establishedProcess database established with resources to analyze its data and maintain it</td></tr><tr><td>3Defined</td><td>(Qualitative)Process defined and institutionalizedSoftware Engineering Process Group established to lead process improvement</td></tr><tr><td>2Repeatable</td><td>(Intuitive)Process dependent on individualsEstablished basic project controlsStrength in doing similar work, but faces major risk when presented with new challengesLacks orderly framework for improvement</td></tr><tr><td>1Initial</td><td>(Ad hoc/chaotic process)No formal procedures, cost estimates, project plansNo management to ensure procedures are followed, tools are not well integrated and change control is laxSenior management does not understand key issues</td><td>Risk</td></tr></table>

Figure 1. The capability maturity model (CMM) adapted from Curtis (1992).

4 The Managed Level: At this level the organization has initiated comprehensive process measurements based on the established definitions of the process, and beyond those of cost and schedule performance. A central process database, containing data about quality and productivity parameters for each key task in the process, is established and maintained.

5 The Optimized Level: The organisation now has a foundation for continued improvement and optimization of the process.

CMM can be used to analyse and diagnose the present mode of operation in a software organization, and a number of techniques for software process assessment have been developed at SEI (Humphrey, 1990a; Humphrey, 1990b; Humphrey et al., 1991; SEI, 1991a;

SEI, 1991b; SEI, 1991c). Equally important, CMM provides specific guidelines on how to improve the software process on a given level of maturity. For each level, a number of key practices are proposed to formulate a strategy for improvement (Humphrey, 1990a; SEI, 1991a; SEI, 1991b; SEI, 1991c).

## 3 CMM AND CASE

In Humphrey's original work, two fundamental claims are made concerning technology and software process improvements (Humphrey, 1990b): Advanced technology can usefully be introduced at the defined level; the most significant quality improvements begin at the managed level. This basic rationale for managing technology is expressed by Humphrey in the following way:

'Automation of a poorly defined process will produce poorly defined results. This is the normal consequence of picking solution before understanding the problem' (Humphrey, 1989a)

This rationale is further developed by Humphrey and Curtis discussing CASE introduction within the framework of CMM (Humphrey, 1990b; Curtis, 1992). They both reach the conclusion that in order to fully utilize CASE technology and obtain productivity benefits, the software process needs to have reached a managed level of maturity:

'Once the process has come under management control, it is possible to begin defining the tools that will benefit the engineering process.' (Curtis, 1992).

Curtis concludes that using CASE in software processes at the initial level will have little effect. Software processes near, or at, level 2, where the primary goal is to establish management control over the process, can benefit from using project management tools. Towards level 3, CASE might be used in modelling activities, and once level 3 has been reached, some tools will suggest themselves. Curtis notes that the primary benefit of CASE at level 4 and 5, among others, is to provide the necessary quantitative data from projects.

Humphrey discusses how to go about implementing CASE in organizations, and presents the following basic guidelines for CASE introduction (Humphrey, 1989b): 1) If your process is chaotic, get it under control before attempting to install a CASE system; 2) develop your process before or during CASE installation, but not after; 3) system conversion is critical, but converting the people will be the hardest job of all; 4) recognise that a CASE installation is never completed; and 5) don't forget to think! In addition, Humphrey points at the necessity of developers having the benefit of the CASE tools in order for them to accept the technology, the feasibility of having small coherent teams using CASE, and the importance of CASE tools not turning into bureaucratic barriers for rational thought (Humphrey, 1989b).

Despite criticism raised (Bollinger & McGowan, 1991; Saiedian & Kuzara, 1995), CMM is undoubtedly a useful and challenging framework for software process improvements in general and for CASE introduction in particular. The key strengths of CMM as a framework for CASE introduction are:

1 CASE introduction is not seen as an aim in itself. Instead it is rightfully placed as one possible means in the wider context of software process improvements.

2 Assessment techniques are provided to diagnose the present operation within a software organization.

3 Key practices are proposed to improve the software operation on each level of maturity. CASE introduction can, in this way, be understood and evaluated in relation to other complementary forms of intervention.

4 A simple strategy for CASE introduction is implied by the assumption that advanced technologies can only be usefully introduced at the defined level.

The fundamental weakness of CMM as a framework for CASE introduction stems from the assumed one-sided causal relationship between process maturity and tool usage. The complimentary position needs to be considered, as pointed out by Jorgensen (1990), where CASE is seen as an instrument for accelerating process improvements. On a more general level, we must acknowledge the complexity of the issue, as illustrated by Huff et al. (1991). A brainstorm on CASE adoption among software engineers and CASE researchers resulted in 76 attributes about the prerequisites for effective CASE utilization. The suggested attributes reflect a diversity of topics and problems, and among them were, for example: Champion with stature (clout); commitment to training and education; encourage CASE 'skunkworks' (projects experimenting on their own initiative); get the government to stop the 'paper game'; and dispel job loss fears from the adoption of CASE. We need to address CASE introduction from a pragmatic perspective treating it as an art of the possible. In the subsequent sections, we examine the weaker points of CMM as a framework for CASE introduction. We start with a general discussion of the role of organizational experiments in CASE introduction. Then we look more specifically at some of the strategic choices related to the design of CASE interventions. In particular, we look more closely at the functional characteristics and the potential users of CASE technology.

## 4 ACKNOWLEDGING EXPERIMENTS

There is, beyond doubt, a mismatch between the extensive investments made in CASE technology and the benefits achieved so far (Aaen & Sørensen, 1991; Sørensen, 1993a; Vessey & Sravanapudi, 1995). From the point of view of CMM, this is not surprising: only a few organizations have reached the defined level of maturity (Humphrey, 1990b) and, as a consequence, most organizations cannot benefit from advanced technologies like CASE. March proposes, however, a view of organizations and people that challenges the basic assumptions of CMM:

'Interesting people and interesting organizations construct complicated theories of themselves. In order to do this, they need to supplement the technology of reason with a technology of foolishness. Individuals and organizations need ways of doing things for which they have no good reason. Not always. Not usually. But sometimes. They need to act before they think.' (March, 1976)

Our technologies of reason share, according to March, three conspicuous ideas. The first idea is the pre-existence of purpose: there is a strong tendency to believe that objectives are prior attributes of decision making and organizational behaviour in general. The second idea is the necessity of consistency: consistency is widely recognized both as an important property of human behaviour and as a prerequisite for normative models of choice. The third idea is the primacy of rationality: we decide what is correct behaviour by relating consequences systematically to objectives, implicitly rejecting the processes of intuition and the processes of tradition and faith. CMM is based on these fundamental ideas and beliefs. The strengths and weaknesses of the approach is, therefore, strongly related to its emphasis on technologies of reason. It is, of course, important to note that the organizational maturity has to be at a minimum stage before CASE has any meaning at all. As noted by Humphrey (1989b), a total chaotic software process might not benefit much, even from a simple CASE tool, and Sørensen (1994) argues that very immature software organizations do not have the necessary staff for utilizing CASE technology. However, March provides a different framework for interpreting the mismatch between the extensive investments made in CASE technology and the rather minimal benefits achieved so far. Sometimes organizations need to experiment. They need to act before they think. Introducing CASE technology might, in some cases, be a useful approach to formulate operational goals concerning the use of advanced technologies and initiate a fundamental transition process in a software organization.

One alternative framework for analysing CASE introduction from an innovation diffusion perspective is proposed by Wynekoop (1992). Strategies for CASE implementation are characterized as either laissez-faire, cautious, or active, and the relation between current working practice and CASE technology are either seen as compatible, incremental, or radical (see Figure 2). Viewed in this way, CASE introduction processes can be conducted at different paces, from virtually overnight to years. The laissez-faire strategy characterizes the belief that a CASE tool will diffuse in the organization without any organizational intervention. A cautious strategy implies a purposefully careful and slow diffusion approach. An active strategy is applied when a high level of organizational resources and commitment are directed at diffusing CASE (J.L. Wynekoop, pers. comm.). CASE technology is a compatible innovation if it is perceived to be similar to current and past practice. It is an incremental innovation if utilizing the tool demands minor changes in current work practices, and it is a radical innovation if it is perceived to be very different from current practice and past experiences (Wynekoop, 1992).

<table><tr><td></td><td>Compatible</td><td>Incremental</td><td>Radical</td></tr><tr><td>Active</td><td></td><td></td><td></td></tr><tr><td>Cautious</td><td></td><td></td><td></td></tr><tr><td>Laissez-faire</td><td></td><td></td><td></td></tr></table>

Figure 2. Case implementation strategy and perceived radicality of the innovation (Wynekoop, pers.comm.).

Wynekoop's model describes the intrinsic relationship between the perceived radicality of CASE, and the diffusion strategy applied. Other related frameworks are proposed in the CASE literature. Fischer et al. (1993) characterize CASE implementation strategies as either fast or slow (seducing the fox or boiling the frog) and Orlikowski distinguishes between incremental and radical change (Orlikowski, 1993). Gallivan et al. (1994) argues for the analytical distinction between, on the one hand, the nature of the innovation which can be either radical or incremental, and on the other hand, the pace of change, i.e., either rapid or gradual change. They further argue that segmenting radical innovations into discrete chunks, allowing for gradual change, may be a viable strategy — a position consonant with the notion of managing CASE implementation as a sequence of planned initiatives (Mathiassen & Sørensen, 1995), and with Aaen's (1992) suggestion to bootstrap the CASE process.

In summary, CMM, with its bias for technologies of reason, needs to be supplemented in its approach to experimentation and organizational learning. March explores five general ideas on how to develop and utilize what he calls sensible foolishness as a supplement to the well-known technologies of reason (March, 1976). The first idea is to treat goals as hypotheses: we should experiment with the goals of CASE introduction, and we should include alternative goals to discover options related to the use of CASE that were not previously imagined in the organization. The second idea is to treat intuition as real: to permit ways of working with CASE tools that are outside the present scheme for justifying behaviour. The third idea is to treat hypocrisy as a transition: hypocrisy is an inconsistency between expressed values on the application of CASE and de facto behaviour that might represent an experiment or a learning process eventually leading to a better situation. The forth idea is to treat memory as an enemy: in most cases good memories support good choices, but the ability to forget, or overlook, established traditions and standards is also useful, and is sometimes even necessary, in making organizations successfully become expert CASE technology users. Fifth, we can treat experience as a theory: learning from personal history by encouraging interpretations and reinterpretations of concepts, beliefs and experiences related to the use of CASE tools.

## 5 FUNCTIONAL VARIATIONS

A closer look at the functional variations of CASE technology can lead to a more nuanced understanding of the possibilities and limitations of applying this technology at different software process maturity levels. CASE technology is, in general, providing computer support for the use of development methodologies, however, the term is interpreted in a variety of ways, as, for example, CASE tool, CASE workbench, or CASE toolkit (McClure, 1988; McClure, 1989). The technology provides a broad range of tool-functionalities (Fournier, 1991) and concepts such as Upper-CASE, Lower-CASE, and Integrated CASE (ICASE) (McClure, 1989; Gane, 1990; Lyytinen et al., 1991) reflect attempts to classify tools according to the part of the development process they support. The two major distinctive features of CASE technology are the central encyclopaedia (or repository) containing elements at a higher level than code statements or physical data element definitions, together with a set of tools providing support for one or more software development methodologies (Gane, 1990; Fournier, 1991; Lyytinen et al., 1991). This definition excludes programming environments and 3GL code generators as CASE tools and it complies well with Humphrey's definition:

'Such an environment should include a set of compatible tools, a common database, task management facilities, and provision for configuration control' (Humphrey, 1989b)

Both Henderson & Cooprider (1990) and Lyytinen et al. (1991) have developed functional models of CASE technology. Of these two quite comparable CASE technology models, we have chosen to base the following on the FCTM (Functional CASE Technology Model) developed by Henderson & Cooprider (1990). The FCTM (see Figure 3) classifies the functionalities of CASE technology into three main components: production technology, co-ordination technology, and organizational technology. Table 1 presents the definitions for each of the functional components in FCTM by selected quotes from Henderson & Cooprider (1990).

Humphrey and Curtis both stress that organizations should be at level 2 at least, and preferably at level 3 before it makes any sense to invest in CASE. This conclusion only makes sense because Humphrey and Curtis consider the full utilization of an ICASE environment (Humphrey, 1989b; Curtis, 1992). Opening the black box of CASE technology makes us appreciate which aspects and facilities of the technology can be utilized for specific purposes in particular organizational settings. If we look at the three functional CASE components presented above, we can identify the following archetypes of activities that CASE can support:

1 Analysis and design activities utilizing the production technology functionality. This is the predominant way of utilizing CASE technology (Aaen et al., 1992).

2 Co-operative and co-ordination activities using the co-ordination technology functionality in order to articulate the development process and negotiate mutual agreements and commitments. State-of-the-art CASE technology does not sufficiently provide this type of functionality

![](/api/attachments/V9STFG7M/fulltext/images/492f803ceec92e84fa5e1b6acee4b01ae65388ef181bb810099eb1d0531d6b7c.jpg)  
Figure 3. Henderson & Cooprider's (1990) Functional CASE technology model (FCTM).  
© 1996 Blackwell Science Ltd, Information Systems Journal 6, 195–208

Table 1. Definitions of the functional CASE technology model (FCTM) components from (Henderson & Cooprider, 1990)

<table><tr><td>Production technology</td><td>‘... functionality that directly impacts the capacity of an individual(s) to generate planning or design decisions and subsequent artifacts or products.’ (p.232)</td></tr><tr><td>Representation</td><td>‘... functionality to enable the user to define, describe or change a definition or description of an object, relationship or process.’ (p.233)</td></tr><tr><td>Analysis</td><td>‘... functionality that enables the user to explore, simulate, or evaluate alternate representations or models of objects, relationships or processes.’ (p.234)</td></tr><tr><td>Transformation</td><td>‘... functionality that executes a significant planning or design task, thereby replacing or substituting for a human designer/planner.’ (p.234)</td></tr><tr><td>Co-ordination technology</td><td>‘... functionality that enables or supports the interactions of multiple agents in the execution of a planning or design task.’ (p.233)</td></tr><tr><td>Control</td><td>‘... functionality that enables the user to plan for and enforce rules, policies or priorities that will govern or restrict the activities of team members during the planning or design process.’ (p.236)</td></tr><tr><td>Cooperative functionality</td><td>‘... functionality that enables the user to exchange information with another individual(s) for the purpose of influencing (affecting) the concept, process or product of the planning/design team.’ (p.236)</td></tr><tr><td>Organisational technology</td><td>‘... functionality and associated policy or procedures that determine the environment in which production and coordination technology will be applied to the planning and design process.’ (p.238)</td></tr><tr><td>Support</td><td>‘... functionality to help an individual user understand and use a planning ad design aid effectively.’ (p.239)</td></tr><tr><td>Infrastructure</td><td>‘... functionality standards that enables portability of skills, knowledge, procedures, or methods across planning or design processes.’ (p.240)</td></tr></table>

(Malmborg, 1992; Mathiassen & Sørensen, 1995; Sørensen, 1995; Vessey & Sravanapudi, 1995).

3 Project management oriented activities where CASE repository information is used in project planning and monitoring. Here, parts from all three components of the FCTM can be utilized.

From a practical management point of view it is necessary to analyse which aspects of a CASE tool are feasible and desirable for a software organisation to utilize. Strategic considerations should address the utilization of different aspects of CASE tools for various purposes at various stages of process maturity instead of merely considering the 'big-bang' approach (Parkinson, 1990). To illustrate this point, several sources point t the importance of software developers perceiving benefits from using CASE in order to lay a foundation for diffusing CASE in the organization (Humphrey, 1989b; Aaen, 1992; Wynekoop et al., 1992; Orlikowski, 1993; Gallivan et al., 1994; Sørensen, 1994). The CASE implementation process can be focused in this direction by carefully selecting which work procedures to support with which CASE tool functionality, that is, according to the archetypes presented above.

## 6 CONTEXTUAL VARIATIONS

One of the main strengths of Humphrey's and Curtis' approaches is that they offer a specific framework and a clear focus to discuss the implementation of CASE. Their narrow focus on software process maturity has, however, a built-in blindness for the organizational setting into which CASE is introduced. State-of-the-art CASE tools primarily support software professionals in doing their job properly, but developing computer-based systems is a process involving a variety of other stakeholders. When only the software process is in focus, a whole set of important questions cannot be asked: how does the organizational and cultural environment influence CASE introduction? Who are affected by the introduction of CASE tools? Under which circumstances can other actors benefit from utilizing CASE?

CASE tools are never introduced into an organizational vacuum. CASE introduction is a particular instance of innovation diffusion and we must focus on how organisational characteristics influence this process (Tornatzky & Klein, 1982; Wynekoop et al., 1992; Sørensen, 1993b). Including the organizational context in an analysis of CASE introduction implies an investigation of the match between technological and organizational characteristics. Fischer et al. conclude that:

'... implementation of CASE technology was only successful when it was regarded as a process of changing the culture of the IT department, i.e., when it was regarded as a process of organization development.' (Fischer et al., 1993)

Aaen & Sørensen (1991) analyse, in a review of state-of-the-art CASE literature, technological and organizational factors affecting CASE diffusion, using an innovation diffusion framework consisting of the following six groups of factors: 1) profitability, 2) scale of investment, 3) technical characteristics, 4) acceptability, 5) change agents, and 6) tool-user qualifications. The analysis concludes that no single factor, but rather, a complex mix of factors, explains successful CASE adoption. Orlikowski (1993) applies grounded theory in order to identify and analyse organizational factors explaining the CASE implementation process in two organizations. Gallivan et al. (1994) conclude that both the structural and cultural characteristics of the organization studied contributed to the success of the CASE implementation process, and they promote the characteristics of the organizational context and the characteristics of the technological innovation as the two key promoting or demoting factors for an effective CASE diffusion process in the organization investigated.

Several possible frameworks can be developed, each yielding different results. In this context we will focus on two critical dimensions of matching CASE technology and organizational context: potential stakeholders and scope of effect (see Figure 4). We describe the groups of potential stakeholders in the CASE implementation process simply as software experts, managers and domain experts. All three groups are ultimately going to be affected by the introduction of CASE. Gallivan et al. (1994) report a similar distinction: IS managers, IS staff and customers. They found that CASE implementation led to changes in the roles of both developers and users. The change in the users' role in the development process was mainly due to the CASE tool leading to an increased level of user involvement.

<table><tr><td></td><td>Few individuals</td><td>Selected projects</td><td>Entire organisation</td></tr><tr><td>Software experts</td><td></td><td></td><td></td></tr><tr><td>Managers</td><td></td><td></td><td></td></tr><tr><td>Domain experts</td><td></td><td></td><td></td></tr></table>

Figure 4. Type of stakeholders and scope of CASE effects.

Focusing on scope of effect, a CASE tool will not necessarily affect the whole organization. It may only affect the work practice of individuals, or of selected project groups. This implies a distinction between the following scope of effect of CASE usage: few individuals, selected projects, or the entire organization. Gallivan et al. (1994) documents a gradual CASE implementation process which evolves from a few software experts to involving developers, domain experts and managers in several divisions.

The application of CMM as reference framework for analysing CASE introduction provides a valuable perspective on the issues involved in matching the software process with CASE technology. In order to address questions regarding the broader organizational effect of diffusing CASE in organizations we need to apply complementary frameworks characterizing issues such as organizational maturity, organizational diversity, potential stakeholders, and scope of effects.

## 7 CONCLUSION

We have reviewed Humphrey's and Curtis' efforts to support the management of CASE introduction and have found their approach interesting and relevant, but limited in perspective. We have discussed three essential questions regarding CASE introduction, which the use of CMM does not provide means to answer properly: 1) What is the role of organizational experiments in CASE introduction? 2) How do the functional characteristics of CASE technology influence CASE introduction? and 3) How does the organizational context influence CASE introduction? As a complement to CMM, each of these questions point to important strategic options related to CASE introduction.

## 7.1 Organizational experiments

Most CASE adopting organizations do not have a sufficiently mature software process (in terms of CMM) to obtain large productivity effects from using CASE. One possible conclusion is that these organizations have introduced CASE technology at an inappropriate stage of development. We argue, based on March (1976), that organizations sometimes need to experiment, and act before they think. Wynekoop's characterization of different CASE implementation strategies — laissez-faire, cautious, or active — and of the perceived distance between current work practice, on the one hand, and the CASE technology, on the other hand, are forwarded as means of broadening management considerations related to CASE introduction (Wynekoop, 1992).

## 7.2 Functional variances

Not all aspects of a CASE tool need to be utilized by the software organizations in the first phases of CASE introduction. Different outcomes of CASE introduction can be discussed according to the three functional components of CASE technologies promoted by (Henderson & Cooprider, 1990): production technology, co-ordination technology and organizational technology. We suggest that each of these aspects can lead to the identification of different activities in which to start utilizing CASE: analysis and design, co-operation and co-ordination between participants, and project management.

## 7.3 Contextual variances

CASE tools are not introduced into an organizational vacuum, and CASE may affect and be affected by more than the software process. We discuss various models focusing on the organizational environment. We propose that managers should focus on strategic choices as to what stakeholders to affect including managers, software experts as well as domain experts, and also on the scope of effects of introducing CASE ranging from a few individuals over selected projects to the entire organization.

## ACKNOWLEDGEMENTS

This research has been partially sponsored by the Danish Natural Science Research Council, Programme No. 11-8394, and by the Danish Technical Research Council. We would like to thank Gro Bjerknes, Michael Vitale, Pål Sørgaard, Ivan Aaen and the anonymous reviewers for constructive comments and suggestions. All errors in this paper naturally remain the responsibility of the authors.

## REFERENCES

Aaen, I. (1992) CASE Tool Bootstrapping — how little strokes fell great oaks. In: Next Generation CASE Tools. Lyytinen, K. and Tahvanainen, V.-P. (eds), pp.8–17. IOS Press, Amsterdam.

Aaen, I., Siltanen, A., Sørensen, C. & Tahvanainen, V.-P. (1992) A Tale of Two Countries — CASE Experience and Expectations. In: Proceedings from IFIP WG 8.2. Work-

ing Conference: The Impact of Computer Technologies on Information Systems Development, Minneapolis, Kendall, K.E., Lyytinen, K. & DeGross, J., pp.61–94. North-Holland, Amsterdam.

Aaen, I. & Sørensen, C. (1991) A CASE of great expectations. Scandinavian Journal of Information Systems, 3, 3–23.

Bollinger, T.B. & McGowan, C. (1991) A critical look at software capability evaluations. IEEE Software, 8, 25–41.

Curtis, B. (1992) The CASE for Process. In: The Impact of Computer Technologies on Information Systems Development, Proceedings from IFIP WG 8.2. Working Conference, Minneapolis, Kendall, K.E., Lyytinen, K. & DeGross, J., pp.333–344. North-Holland, Amsterdam.

Dion, R. (1993) Process Improvement and the Corporate Balance Sheet. IEEE Software, 10, 28–35.

Fischer, S., Doodeman, M., Vinig, T. & Achterberg, J. (1993) Boiling the Frog or Seducing the Fox: Organizational Aspects of Implementing CASE Technology. In: Human Organizational, and Social Dimensions of Information Systems Development, Avison, D., Kendall, J.E. & DeGross, J.I., pp.419–437. Elsevier Science Publishers, Amsterdam.

Fournier, R. (1991) Practical Guide to Structured System Development and Maintenance. Yourdon Press, New Jersey.

Gallivan, M.J., Hofman, J.D. & Orlikowski, W.J. (1994) Implementing radical change: gradual versus rapid pace. In: Proceedings of the 15th International Conference on Information Systems, Vancouver, Canada, DeGross, J.I., Huff, S.L. and Munro, M.C., pp. 325–339, ACM Press, New York.

Gane, C. (1990) Computer-Aided Software Engineering — The Methodologies, the Products, and the Future. Prentice-Hall, UK.

Henderson, J.C. & Cooprider, J.G. (1990) Dimensions of I/S Planning and design aids: a functional model of CASE technology. Information Systems Research, 3, 227–254.

Huff, C.C. (1992) Elements of a realistic CASE tool adoption budget. Communications of the ACM, 35, 45–54.

Huff, C.C., Smith, D., Stephien-Oakes, K., Morris, E. & Zarella, P. (1991) CASE Adoption Workshop. Carnegie Mellon University, Pittsburg.

Humphrey, W.S. (1989a): Improving the software development process. Datamation, 35, 28–30.

Humphrey, W.S. (1989b): CASE Planning and Software Process. Technical Report CMU/SEI-89-TR026. Software Engineering Institute, New York.

Humphrey, W.S. (1990a) Managing the Software Process. SEI Series in Software Engineering. Software Engineering Institute, University.

Humphrey, W.S. (1990b): Characterizing the Software Process: A Maturity Framework. In: Software State-Of-The-Art: Selected Papers, DeMarco, T. and Lister, T. (eds), pp.62–75. Dorset House Publishing.

Humphrey, W.S., Snyder, T.R. & Willis, R.R. (1991) Software process improvement at Hughes Aircraft. IEEE Software, 8, 11–23.

Jørgensen, P.C. (1990): Accelerating processing maturity with CASE. American Programmer, 3(9), 10–15.

Lyytinen, K., Smolander, K. & Tahvanainen, V.-P. (1991) Modelling CASE Environments in Systems Development. In: Metamodels in CASE Environments, Smolander, K. (ed), pp. 26–44. University of Jyväskylä, Jyväskyä.

Malmborg, L. (1992) Diffusion of CASE — an obstacle race? Scandinavian Journal of Information Systems, 4, 105–118.

March, J.G. (1976) The Technology of Foolishness. In: Ambiguity and Choice in Organizations, March, J.G. and Olson, J.P. (eds). Universitetsforlaget, Norway.

Mathiassen, L. & Sørensen, C. (1995) The Why, What, Who, Where and How of CASE Management. In: Proceedings of the 18th Information Systems Research seminar in Scandinavia, Gjern, Denmark, August 11–13, Dahlbom, B., Kämerer, F., Ljungberg, F., Stage, J. and Sørensen, C. (eds), pp. 479–492. Gothenburg University, Gothenburg.

McClure, C. (1988) The CASE for structured development. PC Tech Journal, 6(8), 51–67.

McClure, C. (1989) CASE is Software Automation. Prentice Hall, New Jersey.

Orlikowski, W. (1993) CASE Tools as organizational change: investigating incremental and radical changes in systems development. MIS Quarterly, 17, 309–340.

Parkinson, J. (1990) Making CASE work. In: CASE on Trial, Spurr, K. and Layzell, P. (eds), pp.213–242. Wiley, Chichester.

Paulk, M.C., Curtis, B., Chrissis, M.B. & others (1991): Capability Maturity Model for Software. Carnegie Mellon University, Pittsburgh.

Paulk, M.C., Curtis, B., Chrissis, M.B. & Weber, C.V. (1993) Capability maturity model — version 1.1. IEEE Software, 10, 18–27.

Rugg, D. (1993) Using a capability evaluation to select a contractor. IEEE Software, 10, 36–45.

Saiedian, H. & Kuzara, R. (1995) SEI capability maturity model's impact on contractors. IEEE Computer, 12, 16–26.

SEI (1991a) Capability Maturity Model for Software. Software Engineering Institute, Carnegie Mellon University, SESI-91-TR-24.

SEI (1991b) Key Practices of the Capability Maturity Model. Software Engineering Institute, Carnegie Mellon University, SEI-91-TR-25.

SEI (1991c) Software Process Maturity Questionnaire. Software Engineering Institute, Carnegie Mellon University, SEI-91-TR-25.

Sørensen, C. (1993a): What influences regular CASE use in organizations? — man empirically based model. Scandinavian Journal of Information Systems, 5(1), 25–50.

Sørensen, C. (1993b) Introducing CASE Tools into Software Organizations. Ph.D. Dissertation, Aalborg University.

Sørensen, C. (1994): CASE Introduction — Matching Technological and Organizational Characteristics. In: Quality Software — Concepts and Tools.

Stage, J., Nørmark, K. and Larsen, K.G., pp. 91–118.
Aalborg University, Aalborg.

Sørensen, C. (1995) Why CASE Tools do not Support Coordination. In: CASCW (Computer Supported Co-operative Working) and the Software Process, Savoy Place, London, M. Barret (ed.), pp.4/1–4/3. IEE, London.

Tornatzky, L.G. & Klein, K.J. (1982) Innovation characteristics and innovation adoption-implementation: a meta-analysis of findings. IEEE Transactions on Engineering Management, 29(1), 28–45.

Vessey, I. & Sravanapudi, A.P. (1995) CASE Tools as Collaboration Support Technologies. Communications of the ACM., 38(2), 83–95.

Wynekoop, J.L., Senn, J.A. & Conger, S.A. (1992) The Implementation of CASE Tools: An Innovation Diffusion Approach. In: The Impact of Computer Technologies on Information Systems Development, Proceedings from IFIP WG 8.2. Working Conference Minneapolis. Kendall, K.E., Lyytinen, K. and De Gross, J., pp.25–42. North-Holland, Amsterdam.

## Biographies

Lars Mathiassen is a professor of computing at Aalborg University in Denmark. He holds a MSc in computer science from Aarhus University, Denmark, and a PhD in computer science from Oslo University, Norway. Dr. Mathiassen's research interest is in the intersection between information systems and software engineering with particular emphasis on systems development and IT management. He has published quite a number of papers and books related to information systems including 'Professional Systems Development', Prentice-Hall, 1990 (together with N.E. Andersen et al.) and 'Computers in Context', Blackwell, 1993 (together with Bo Dahlbom).

Carsten Sørensen is senior scientist at the Systems Analysis Department, Risø National Laboratory in Denmark. He holds a BSc in mathematics, a MSc in computer science and a PhD in computer science from Aalborg University, Denmark. Dr Sørensen's area of research is information technology supporting complex work in technical domains. The work can be divided into the two strands of: Organizational implementation of CASE (Computer Aided Software Engineering) technology supporting the systems development process; and coordination mechanisms as a CSCW (Computer Supported Cooperative Work) technology supporting the coordination of complex work in manufacturing and software engineering.
