---
otero_id: 11522
otero_key: "6U62ARCK"
title: "Crowdsourcing design decisions for optimal integration into the company innovation system"
authors: "Kristina Risom Jespersen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Crowdsourcing design decisions for optimal integration into the company innovation system

![](/api/attachments/6U62ARCK/fulltext/images/6f7ade0e421259bc45f6464637ce8b5cca1593389ba4d5ab1ffba03b1becd4de.jpg)

Kristina Risom Jespersen

<table><tr><td>PII:</td><td>S0167-9236(18)30156-8</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.09.005</td></tr><tr><td>Reference:</td><td>DECSUP 12991</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>13 April 2018</td></tr><tr><td>Revised date:</td><td>6 September 2018</td></tr><tr><td>Accepted date:</td><td>21 September 2018</td></tr></table>

Please cite this article as: Kristina Risom Jespersen , Crowdsourcing design decisions for optimal integration into the company innovation system. Decsup (2018), doi:10.1016/ j.dss.2018.09.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Crowdsourcing design decisions for optimal integration into the company innovation system

By

Kristina Risom Jespersen\*

Department of Economics and Business Economics,

Aarhus BSS, Aarhus University

Fuglesangs Allé 4

DK-8210 Aarhus V.

Denmark

\*e-mail: kjespersen@econ.au.dk

\*Tel.: 8716 5534

# ACCEPTED MANUSCRIPT

# Crowdsourcing design decisions for optimal integration into the company innovation system

## Abstract

Companies apply crowdsourcing as the digital approach to source external information into their innovation system. Rather than analyzing the crowdsourcing platform facilitating the connection of company and crowd, crowdsourcing into the company innovation system. Proper structural decision support concerns the design of purpose, specificity, and composition of crowdsourcing. The aim of this paper is to explore how these design decisions relates to innovation system outcome. The results are drawn from an agent-based simulation of competing companies to observe the outcome of different designs of crowdsourcing integration into the innovation system. Both local and distant knowledge environments for innovation is simulated. The main finding is that optimal crowdsourcing design into the innovati is contingent on the targeted innovation environment. Secondly, the results also reveals potential conflict between the crowdsourcing platform recommendations in literature and innovation system recommendations made in this paper. Task specificity may generate platform traffic but weakens innovation outcome. In addition, the decided combination of purpose and composition is delicate to ensure highest innovative outcome. Overall, the results provide useful guidelines to companies in their efforts of implementing crowdsourcing into the innovation system.

Keywords: Crowdsourcing design; Specificity; Innovation system; Innovation environment; Agent-based simulation

## Crowdsourcing design decisions for optimal integration into the company innovation system

## 1. Introduction

The crowdsourcing concept describes the act of outsourcing a task or submitting a problem to a vast group of people (a crowd) in form of an open call [1-3]. Empirical studies find that companies using crowdsourcing are growing in numbers [4] and innovativeness [5, 6]. The recent growth in the adoption rate of crowdsourcing as companies’ preferred approach to open innovation is enforced by decreased IT costs in combination with increased outreach and information richness through the Internet [4, 5, 7, 8]. Nonetheless, studies have illustrated that companies deciding on high levels of external sourcing in innovation are not capable of a full value capture [4, 9].

Crowdsourcing literature has focused on platform design and governance [10-12] as well as the crowd traffic, creativity, and submission quality [13-15]. Hence, the social-technical and the organizational–technical design elements of crowdsourcing has been rigorously explored in literature [16, 17]. This technical perspective has discounted that crowdsourcing is also a channel for inflow of external information into company decision systems [2]. Specifically, it is a decision of how to internalize external information into the company innovation system [2, 12, 18]. Therefore, this paper focuses on the integration of crowdsourcing into the innovation system. According to crowdsourcing literature, three task design decisions are important for crowd integration into the innovation system: Why the crowd is needed for assistance (purpose); how the the task broadcasted to the crowd is described (specificity); and how many stages of the innovation process the crowd is integrated into (composition) [16, 17, 19]. Nonetheless, little guidance exists to companies as how to combine purpose, specificity, and composition to benefit innovation system outcome [2]. This paper aims to address this gap in existing literature.

Methodologically, an agent-based simulation model [20-23] of the innovation system with integrated crowdsourcing and its environment is applied for the generation of data to the hypothesis testing. In the simulated world, a cluster of companies synchronously innovates and competes for the intelligence of the crowd [24]. For an innovating company, the competitive environment is focused on the existing trajectory or seeking for a change of trajectory. Hence, a key component of the innovation system environment is ‘where the search is focused in relation to currently available solutions’ [3, 25-27]. Within crowdsourcing and innovation literature in general the distinction is between external search for innovation in local and distant knowledge environments [3, 27]. Consequently, this study explores crowdsourcing design decisions (purpose, specificity, and composition) into innovation systems in these two environments. Hence, this paper is among the first to study how to integrate crowdsourcing into innovation system systematically.

The presented results demonstrate that crowdsourcing should be designed differently for innovation systems in the local versus the distant knowledge environment. Following the given guidelines for crowdsourcing purpose, specificity, and composition, companies can strengthen their innovation effort relative of competitors. Moreover, the results also reveals a potential conflict between the current crowdsourcing platform recommendations and innovation system recommendations made in this paper. It is understandable that success of information systems is measured by platform traffic [3, 19, 29, 57]. However, the lesson learned from the results is that sub-optimizing the crowdsourcing platform design weakens innovation system outcome. Identifying this conflict is an important contribution made to crowdsourcing literature [20].

This paper proceeds as follows. First, the conceptual background is presented, and the theory underpinning the developed hypotheses is discussed. In the next section, a detailed description of the simulation calibration discussed, before implications and limitations are put forward.

## 2. Conceptual background

The system view of the innovation process, applied in this study, focuses on decision-making and innovation environment [28, 29]. The underlying assumption is that information accumulates from the innovation stages to form the process outcome that the company launch on the market. Though internal research and development capabilities are important for innovation outcome [30-32], the importance of a combination of internal and external information resources when generating an innovative output is acknowledged in innovation literature ([33-37] among others). To internalize external information has traditionally concerned the applied heuristics [26]. However, technological development has digitalized these cognitive mechanisms [13]. Crowdsourcing is one of these digital forms of “how to” internalize external sources into the innovation system [2, 12, 18]. Therefore, the integration of the crowdsourcing into the innovation process system, its outcome and its environment are reviewed and conceptualized, before hypotheses development for crowdsourcing design.

## 2.1. Integrating crowdsourcing in the innovation system

The innovation system in figure 1 describes the accumulation and flow of information from the first stage to market launch. Each stage of the innovation system starts internally with information from a company’s research and development (R&D). In addition to this internal knowledge base, the company can decide to source information externally into the innovation system, i.e. to crowdsource [11, 38, 39]. The decision to crowdsource initiates the crowdsourcing loop within the innovation system (indicated by the dotted square in figure 1).

## [insert figure 1 about here]

First, the company finalizes the request set-up based on the decided crowdsourcing design. Second, the request is broadcasted to a crowd inviting crowd members to participate. The execution of step one and two of the crowdsourcing loop builds on careful designed governance mechanisms for the crowdsourcing platform [10]. In the third step of the crowdsourcing loop, the decision initiative shifts to the crowd. The crowd members have to decide whether to accept the request from the focal company or respond to requests made by others in the cluster of companies competing. In the case a crowd member responds positively to the focal company’s request, the company and crowd members are sharing their knowledge resources [40-43]. In step four, the resource sharing between company and crowd consists of information pooling and information integration [40- 43]. First, information pooling is the sharing of information [44]. Each crowd member and company has a unique knowledge profile of application and technical knowledge to share in the information pool [27, 45-50]. As such, the information pool is where company and crowd members make project-related, explicit knowledge and proprietary information readily available for the development project in the designated innovation stage [27, 41]. Second, information integration refers to the sense of the content of the information pooled [51]. The

# ACCEPTED MANUSCRIPT

premise of the crowdsourcing loop is that each member of the crowd self-selects the request to respond to and the company to share resources with [3, 38]. This self-assessed fit by crowd members introduces quality risks on the co-created information pool [39]. Not every member of the crowd that self-selects to respond to a request is in the right position to solve it [3]. The information heterogeneity of the crowd is a major reason of the variability of the information pool content in form of uniqueness and usability [46, 49, 52-54]. In this respect, the company faces an information pool filled with usable and unusable innovation opportunities. In addition, system needed to be bridged for information integration into the innovation system [55]. The company role is to minimize this cognitive distance between the information pool and the company knowledge system [40, 55]. This capability is known as absorptive capacity of companies [31, 36, 56-58]. Therefore, the fifth step of the crowdsourcing loop is a company task. The company has to synthesize the information submissions from the crowd in a meaningful way so as to ensure learning-from-the-crowd [11].

Back in the innovation stage, the innovation system progresses by combining learning-from-the-crowd and internal R&D for the innovation stage closure [33-37]. Thereafter follows the next stages of the innovation process until the innovation process is final. Then, the process outcome is broadcasted to the market. Following launch on the market, the crowd decides whether to select the launched offering and engage in an exchange (buy). This transaction concludes the innovation system.

## 2.2 Innovation system outcome and crowdsourcing

The integration of crowdsourcing into the innovation process stages influences the information accumulation within the innovation system and subsequently system performance [3, 38]. The innovation system holds three outcome levels: in-stage, process, and market [28, 29]. First, the in-stage outcome is the result of the operational decisions taken within each stage [29]. Specifically for crowdsourcing integration, the result of crowdsourcing in an innovation stage is the amount of learning-from-the-crowd that the company combines with its internal R&D. Second, the process outcome is the result of combining learning-from-crowd and internal R&D throughout the stages in the innovation process [58, 59]. This sum of knowledge represents the extracted innovation by the company pre-launch on the market, i.e. the process outcome [47]. Third, within

# ACCEPTED MANUSCRIPT

a cluster of companies synchronously innovating, the process outcome from each company form the portfolio of innovation offerings to the crowd. The selection of offerings by the crowd defines the market outcome of the innovation system in form of the obtained sales by each company offering (the process outcome)[24]. Hence, crowdsourcing creates an inflow of information to the innovation system at in-stage level and becomes part of the produced innovation at process level. An innovation system outcome rated by the crowd (marke level). Therefore, to examine how the integration of crowdsourcing influence the innovation system outcome, this study uses the process outcome as level of analysis.

## 2.3 The innovation system environment and crowdsourcing

The innovation system assumes a fit between the process and its environment. The information inflow in the innovation process should match the demanded changes imposed by the environment. Specifically, a company that crowdsources in the innovation process competes with other companies for the intelligence of a crowd [24]. For an innovating company, the competitive environment may be focusing on the existing trajectory or seeking a change of trajectory. Hence, a key component of the innovation system environment is ‘where the search is focused in relation to currently available solutions’ [3, 25-27]. Within crowdsourcing and innovation literature in general the distinction is between external search for innovation in local and distant knowledge environments [3, 27]. Consequently, this study applies these two environment conceptualizations examining the optimal design of crowdsourcing into the innovation system.

In the local knowledge environment, the innovation output in the local search environment has an evolutionary nature [60]. The innovation outcome ranges from incrementally adapting to radically improving existing solutions in the market [26, 61]. In other words, the needed problem solving is framed in a known environment positioned on an existing trajectory. This means that the search for innovation is conducted within the neighborhood of the company’s current position [3, 31]. Specifically for crowdsourcing, the crowd is invited to engage in problem solving of narrow and precisely defined problems with clear criteria [17, 24]. Within this environment, uncertainty is controlled by a predefined innovation space.

In the distant knowledge environment, the innovation agenda is broader and more complex reflecting a desire to rethink the current state of affairs by seeking and evaluating new technological or new market

# ACCEPTED MANUSCRIPT

trajectories [3, 62, 63]. The innovation output in the distant knowledge environment has a revolutionary nature [60] as the innovation outcome ranges from incrementally reframing to radically disrupting existing solutions in the market [26, 61]. The innovation search focuses outside the current position of the incumbent firms. Within this environment, the company needs the crowd to extend its own knowledge base. The competitive race in the environment is to change the trajectory. The change of trajectory sought by companies leave uncertainty among competitors as to which solution becomes market dominant [17, 24].

As such, the crowd represents a valuable resource of information for innovation systems in both environments [3, 17, 44]. However, the innovation agenda is different for the two knowledge environments, which affects the information inflow to the innovation system and makes the crowdsourcing design a set of delicate decisions.

## 3. Crowdsourcing design decisions and innovation system outcome

Taking crowdsourcing forward into the innovation system requires a set of structural decisions that refers to the innovation system elements. Crowdsourcing literature holds three design elements significant for crowdsourcing integration into the innovation system that companies modify to suit innovation milieu and agendas: Purpose, specificity, and composition [16, 17, 19, 64]. As the innovation system cannot be separated from its environment, this study applies the characteristics of the innovation system environment (§2.3) for the examination of crowdsourcing design correlations with innovation system outcome. Each crowdsourcing design element is defined below followed by their hypotheses development.

## 3.1 Crowdsourcing design purpose

Crowdsourcing purpose is the decided focus of the task outsourced to a crowd. The question needed answering by the company is “why the crowd is needed for assistance in the innovation process?” Consequently, crowdsourcing purpose is tightly linked to the innovation stage in question. The innovation process contains stages customized to each company, but it may in general be regarded as a decision-making process of the three phases: intelligence, design, and choice [16, 18]. In the intelligence phase, the purpose of the crowd is to accelerate the richness of information held by the company. Examples of task purposes are ideation, designs, trendspotting, and information providers [12, 16]. In the design phase, the purpose of the crowd is to produce physical designs or prototypes. The crowd becomes research assistants and part of the team co-creating the actual offering [47]. Digitally the crowd contributes with user-generated content as either author or reviewer [12]. In the choice stage, the request broadcasted to the crowd is to vote, select, review, or give feedback [2, 19]. Crowd testing is an innovation activity with a long tradition in the innovation process [37].

## 3.1.1 Purpose and innovation system outcome

Purpose is the decision as to when in the innovation process external information is sourced into the innovation system. According to open innovation literature, all purposes for collaboration with external users are equally important for the innovation system outcome [34, 65]. However, research on information processing and innovation finds that innovation search are enhanced by changes in environment conditions [66].

The local knowledge environment is characterized by a bounded innovation search in a pool of existing knowledge. Innovation management literature finds that the innovation process along established trajectories is standardized in form of stages activities and gate criteria [37]. In this innovation system, creativity occurs in the front end and is then managed efficiently through the other stages [14, 60, 67]. Optimizing the front end is found empirically to be a key success factor of new products [37]. Furthermore, the anticipated movement of competitors resolve the experienced uncertainty. Innovating in a predefined innovation space along existing trajectories become reassurance of own innovative effort [68]. It is therefore reasonable to expect a larger effect of crowdsourcing in the intelligence stage relative of design and choice stages in the local knowledge environment.

For radical or revolutionary innovation, the innovation process is iterative with uncertainty about stage activities and decision criteria as the process progresses [60]. Therefore, unbounded search for innovation characterizes the distant knowledge environment. Crowdsourcing is integrated in all stages to stay flexible and alert to changing demands in the environment [69, 70]. The key lies in the experience uncertainty [71]. As the environment requires high levels of innovation from the competing companies, the innovation process should facilitate exploratory behavior throughout its stages [28]. This means that the focal company cannot predict the development direction taken in either innovation stage. Consequently, attention to all task purposes is important because of the unexplored territory threaded [3, 26, 27]. Based on the above relation of crowdsourcing purpose and innovation system environment, it is hypothesized that:

H1. The positive correlation of crowdsourcing purpose and innovation system outcome is highest for the intelligence purpose relative of design and choice in the local knowledge environment.

H2. The positive correlation of crowdsourcing purpose and innovation system outcome is equal throughout the innovation process in the distant knowledge environment.

## 3.2. Crowdsourcing design specificity

Specificity in crowdsourcing design concerns the task description that may range from well-structured to open-ended (unstructured) [3, 5, 38]. A well-structured task has a clear delineation and thoroughly defined initial states [3]. In other words, task specificity is high. For unstructured tasks, the problem solving space is indefinite as a predefined solution or approach is not specified [3, 24]. In this regard, task specificity is low because of the open-ended task structure. Consequently, the specificity of the broadcasted request to the crowd is central for the information inflow to the innovation system, because it determines whether the company seeks information close to or distant to their knowledge system. Consequently, the designed task specificity determines how known the information shared by a crowd is to the company [11] [38].

## 3.2.1 Specificity and innovation outcome.

The key is to understand the knowledge gap of the crowd and the company knowledge system due to the combination of task specificity and system environment. The Schumpeterian argument is that knowledge base diversity increases the possibility of recombination of partners’ knowledge into innovations, while knowledge similarity is found to maintain the status quo [72, 73]. This trade-off between distance and similarity highlights the cognitive proximity paradox. Corporate coherence [74] and proximity paradox [55, 75] theories show that being cognitively too close or too distant inhibits learning and innovation.

# ACCEPTED MANUSCRIPT

Search in the local knowledge environment travels from adaption to improvement of existing solutions (§2.3). Here, the creativity level of the innovation system output is bounded by the existing innovation trajectory of the environment [3, 61]. Consequently, the designed task specificity determines whether information shared by members in a crowd is new to the seeking firm. High task specificity becomes search close to the company’s current knowledge position. Differently low task specificity could lead to the discovery of new knowledge important for the further evolvement of the existing trajectory [3, 11, 16]. Literature agrees that the highest evolved output on a known trajectory leads in the market [62, 63]. This translates into low task specificity benefitting the innovation system outcome in the local knowledge environment. The distance of crowd input to the company knowledge system has a distance but remains in a predefined innovation space.

The distant knowledge environment begins where the local knowledge environment ends. It is an innovation search in a space of new and unknown information [3]. Hence, irrespective of task specificity the knowledge from the crowd is at a distance to the company knowledge system (§2.3). High task specificity would frame new information in a known setting whereas low task specificity increase the risk of receiving knowledge too distant from the company’s knowledge system [55]. Thus, differently from the local knowledge environment, high task specificity is expected to benefit innovation system outcome in the distant knowledge environment.

The difference of expected outcome of the innovation system due to task specificity to the crowd is interesting because of the recommendations made in crowdsourcing literature. Crowdsourcing research states high task specificity as a necessary condition for solver contribution [38]. The benefit of high task specificity is that simplification of tasks through modularization makes it easier for solvers to contribute. This increases the number of submissions received by the company from the crowd [64]. Yet, higher task specificity also increase the incremental nature of submission from a crowd [11].

H4. Crowdsourcing designed with high task specificity correlates positively with the innovation system outcome in the distant knowledge environment.

## 3.3. Crowdsourcing composition design

The crowdsourcing design composition refers to the sequence of crowdsourcing integration into the stages of the innovation system [7, 45]. The distinction in literature is between simple and complex compositions [17]. Simple designs have one innovation stage with integration of crowdsourcing, whereas complex designs integrate crowdsourcing into multiple innovation stages of the innovation process [64]. In other words, the design decisions for crowdsourcing composition is focused on the timing of internalizing external information into the innovation system.

## 3.3.1 Composition and innovation system outcome

The open innovation paradigm praises the inflow of information from external sources throughout the innovation process (complex compositions). A more-is-better assumption exists because of the ability of users’ innovativeness to outperform companies on creativity, cost, and speed [34, 76]. However, the increasing number of idea tournaments and innovation competitions demonstrate that the practical application of open innovation is through simple compositions (one stage) [17]. One explanation is the technological ease of setting up innovation platforms. Despite the technological ease, empirical findings are mixed regarding innovation system outcome [5]. This study argues that the knowledge environment of the innovation system interacts with the performance of crowdsourcing composition design decisions.

In the local knowledge environment, the innovation system is operationalized in detail with all activities defined including those eligible for the crowd to contribute on [37]. The innovation process view follows project management methods with focus on efficiency and timeliness of the process [77]. To uphold this, external input is timed purposefully into the process to aid process efficiency and not to delay the planned process. For radical innovation, the focus of the distant knowledge environment, the innovation process is recursive and more chaotic of nature [28]. The uncertainty about process outcome enforces iterations and nonlinearity of the innovation effort. As such, the path travelled in the innovation process is unknown at the front end. Literature agrees that high novelty comes at the risk of misunderstanding in the market [55]. This risk can be controlled by continuous crowdsourcing in the innovation process. This would ensure that nonalignment with the market is expected [63, 78]. As advocated in extant literature, knowledge co-creation is the competitive capability of industry leaders [8, 34].

In summary, the crowdsourcing composition is found to be contingent upon the innovation system environment. Simple compositions are benefiting innovation outcome in the local environment due to the project management perspective. In the distant environment, complex compositions are supporting the innovation outcome due to the faced uncertainty. Thus, for crowdsourcing design composition, it is hypothesized that:

H5. A simple crowdsourcing composition is positive for innovation system outcome in a local knowledge environment.

H6. A complex crowdsourcing composition is positive for innovation system outcome in a distant knowledge environment.

## 4. Methodology

Methodologically the exploration of the crowdsourcing design integrated into the innovation system is approached with an agent-based modeled simulation (ABMS). ABMS is a computational technique that models systems and system outcomes based on agent calibrations. The agent-based modeled simulation tool ‘Repast’ is used because of its proven ability to simulate interaction between agents [79, 80]. Crowd members and companies are represented by a set of basic characteristics and rules that determine uniquely for each agent how they will act in a given system [20-23]. Our simulation is a configuration of the crowdsourcing system in figure 1(§2.1). In the simulation, the local knowledge environment is defined from [0, 0.5] and the distant knowledge environment from ]0.5; 1] (§2.3). Further, companies were simulated to compete in the same knowledge space [3, 24]. This means that the simulated world contained four time steps (j); a step for each of the three innovation stages, and one-step for the process outcome launch on the market. In the simulated world,

# ACCEPTED MANUSCRIPT

seven company agents<sup>1</sup> innovate and launch simultaneously, thereby indirectly competing to attract crowd members in each time step. The number of crowd members in the simulated world was set to 1000 [53, 54, 81]. According to the innovation system in figure 1, the company and crowd agents hold application knowledge (AK), technical knowledge (TK), an information integration ability (λ), and an internal innovation engagement ability (η). Appendix A describes in detail the calibration of company and crowd member agents in the simulation.

## 4.1. Operationalizing the crowdsourcing system

The requisites for simulating the integration of crowdsourcing into the innovation process are the crowdsourcing design elements, the request response rule for crowd members, and the learning-from-thecrowd. The operationalization and measurement of these are accounted for in the following.

## 4.1.1. The design elements.

First, the composition design of crowdsourcing determines the number of times in the innovation process a request is broadcasted to a crowd. With the innovation system in figure 1 holding three innovation process steps, the frequency range for composition design is [1;3]<sup>2</sup>. Second, the simulated innovation process for all companies (c) is defined as a three step process of idea, design, and choice, followed by a fourth time step where all companies launch their developed products on the market to a crowd. This means that the designed crowdsourcing purpose has three forms: idea, design, and choice. These variables are measured binary for each company agent $( 1 = \mathrm { y e s ~ a n d } ~ 0 = \mathrm { n o } )$ . Third, task specificity $( \delta _ { \mathrm { c j } } )$ is set randomly for the companies within the defined interval (§4) of the simulated knowledge environment. In each environment, task specificity is low at the upper bound of the given intervals and high at the lower bound. This means that higher values of task specificity measure more open-ended designed requests being broadcasted to a crowd.

## 4.1.2. Response rule.

The response rule to a broadcasted request is modeled on the Euclidian one dimension distance measurement. A crowd member would respond positively (yes) to a company’s request to collaborate on innovation if the distance between a user’s (i) innovation engagement $( \delta _ { \mathrm { i j } } )$ and the company’s (c) broadcast specificity $( \delta _ { \mathrm { c j } } )$ is the smallest possible in the set of broadcasts at a given time step (j). Equation (1) states the applied Euclidian collaboration rule.

$$
(1) \Delta_ {\mathrm{icj}} = \operatorname{Min} _ {\mathrm{icj}} | \delta_ {\mathrm{ij}} - \delta_ {\mathrm{cj}} |
$$

## 4.1.3. Learning-from-the-crowd.

Learning-from-the-crowd (LfC) in an innovation stage (j) is the product of information pooling and information integration of company (c) and crowd members (i). The shared knowledge entered into the information pool is the interaction of applied knowledge (AK) and technical knowledge (TK) of crowd member (i) and company (c) measured as $[ ( \mathrm { A K _ { c j } ^ { * } A K _ { i j } } ) + ( \mathrm { T K _ { c j } ^ { * } T K _ { i j } } ) ]$ . The influence of information integration of a crowd memeber $( \lambda _ { \mathrm { i j } } )$ and a company $( \lambda _ { \mathrm { c j } } )$ on the information pool is measured by multiplying the information pool with λ. Equation (2) expresses the applied operationalization of LfC for a company (c).

$$
\mathrm{LfC} _ {\mathrm{c}} = \Sigma_ {\mathrm{j}} ([ (\mathrm{AK} _ {\mathrm{cj}} * \mathrm{AK} _ {\mathrm{ij}}) + (\mathrm{TK} _ {\mathrm{cj}} * \mathrm{TK} _ {\mathrm{ij}}) ] * \lambda_ {\mathrm{ij}} * \lambda_ {\mathrm{cj}})
$$

Data was generated through consecutive executions of the simulation for each of the two search environments.

## 4.2 Output measurement

## 4.2.1. Innovation system outcome

Following existing literature ([33-37] among others), the innovation system outcome (<sub>c</sub>) is defined as the sum of knowledge learned from the crowd $\mathrm { ( L f C _ { c } ) }$ and knowledge from internal R&D (η<sub>c</sub>) (see appendix A1). For the simulated innovation system, a logarithmic transformation of the absolute amount of $\mathrm { L f C _ { c } }$ is performed to ensure linearity with $\mathfrak { n } _ { \mathrm { c } } . \ \mathfrak { n } _ { \mathrm { c } }$ is multiplied three times to signify the three innovation stages of the innovation system in figure 1. The constant (k) is applied to normalize <sub>c</sub>. Equation (3) shows the calculation of innovation system outcome.

(3) $\Pi _ { \mathrm { c } } = ( \mathrm { L o g } ( \Sigma \mathrm { L f C _ { \mathrm { c } } } ) + 3 \eta _ { \mathrm { c } } ) / \mathrm { k }$

## 4.2.2. Market outcome

Market outcome is measured as the number of crowd members responding positively to the company’s innovative outcome relative of competitors in the market. Equation (1) is applied to simulate the market exchange situation. At the end of the innovation process (world step four), the broadcasted request to the crowd is the obtained innovation system outcome (<sub>c</sub>). Hence, a member of the crowd would buy from a company rather than a competitor, if the distance between a crowd member’s (i) innovation engagement (<sub>i</sub>) and a company’s (c) innovation system outcome (<sub>c</sub>) is the smallest possible in the set of offerings. Sales are measured as the number of crowd members (n<sub>i</sub>) in the simulation buying from the focal company.

## [insert table 1a and 1b about here]

Table 1a and 1b show how crowdsourcing design elements and innovation system outcome correlate within and across constructs for each of the knowledge environments. The diagonal in table 1a and 1b holds the discriminant validity coefficients. These are below the threshold 0.85, demonstrating construct validity of the analyzed variables. The model used for analysis of the proposed hypotheses is provided in Equation 4:

Innovation system outcome

(4)

$\mathbf { \beta } = \mathbf { \alpha } \alpha + \beta _ { 1 , 2 , 3 }$ Task Purpose dummies

$+ \beta _ { 5 }$ Task Composition

$+ \beta _ { 4 }$ Task Specificity

# ACCEPTED MANUSCRIPT

## 5. Results and discussion

## 5.1. Descriptive results

The descriptive results provide a general overview of the innovation system outcome at stage, system, and market levels for the two knowledge environments. The main figures describing average innovation system outcome and average number of crowd members across the crowdsourcing design elements are shown in table 2.

Table 2 illustrates that a high number of crowd members does not raise the learning-from-the-crowd (LfC). Indeed, input from a large share of the crowd can contribute to lower learning. This is especially pronounced for the composition design element of crowdsourcing. In the local knowledge environment, average LfC in a two-stage composition is 61.632 with an average of 478.56 crowd members submitting information. This learning level is only marginally higher than for a one-stage composition where LfC equals 53.999 with an average of 148.56 crowd members. Hence, the input from additional 330 crowd members only marginally increase learning due to the integration of crowd members company. Table 2 shows a similar picture for the distant search environment. This is interesting because crowdsourcing literature holds the number of submissions from a crowd as a platform success indicator [17, 64, 82]. Here, high task specificity is one design mechanism argued to ensure a high number of submission on crowdsourcing platforms [58]. Yet, table 2 shows that low task specificity attracts a higher average number of crowd members (611.74 > 156.68) in the local knowledge environment. Though high task specificity in the distant knowledge environment leads to more submissions (543.38 > 199.71), the innovation system outcome does not benefit from this (.498 < .594). As such, the descriptive findings indicate that platform governance and design recommendations may be restricting the innovation system outcome.

[insert table 2 about here]

## 5.2. Regression results

With regard to the simulation design, regression analysis is applied to test the hypotheses. The regressions were estimated in SPSS 24.0 applying OLS-estimation. The coefficients state the importance of crowdsourcing design decisions for the focal firms’ innovation system outcome when integrating crowdsourcing. The estimation of Equation 4 is performed for local (table 3) and distant (table 4) knowledge environments separately to capture combinatory differences and similarities with crowdsourcing design decisions. Table 3 and 4 show the five models estimated in our analysis. Model 1 to 3 test the importance of each crowdsourcing design element for innovation system outcome, and model 4 and 5 present the full model. Collinearity between task purpose and task composition necessitated two full models (model 4 and 5).

[insert table 3 about here]

5.2.1 Crowdsourcing design for innovation in local environments

Table 3 shows how the crowdsourcing design decisions relate to innovation system outcome in the local knowledge environment. For crowdsourcing purpose, hypothesis 1 stated that an intelligence purpose would be more important than design and choice purposes. Model 1 shows that intelligence (β = .443) and choice (β = .359) purposes of crowdsourcing design are positive for innovation system outcome whereas inviting the crowd to join in the design stage is insignificant. Model 4 reinforces this result though the importance of crowd testing (choice purpose) is reduced. Hence, hypothesis 1 is supported. However, it is noted that crowdsourcing can serve the choice purpose also and still benefit innovation system outcome in the local knowledge environment.

For crowdsourcing specificity, the concern was whether low task specificity benefitted innovation system outcome (hypothesis 3). The results in table 3 show positive effects of low task specificity on innovation system outcome, both individually $( \beta _ { \mathrm { m o d e l } 2 } = . 6 1 2 )$ and in the full models $( \beta _ { \mathrm { m o d e l } 4 } = . 5 2 1 ; \beta _ { \mathrm { m o d e l } 5 } =$ .539). Therefore, hypothesis 3 is supported. This is interesting because literature on crowdsourcing platform design and governance recommends high task specificity for optimal performance [3, 17, 38]. It is understandable that success of information systems is measured by traffic on a designed platform. But based on the presented results, the recommendation of high task specificity because of increased decomposability in crowdsourcing literature [38] would potentially trap company integration of crowdsourcing into their innovation systems. Especially the relative low innovation system outcome in table 2 $( \mu = . 2 6 6 )$ for companies

# ACCEPTED MANUSCRIPT

broadcasting well-structured tasks in the local search environment supports the existence of a trap. This is in congruence with coherence [74] and proximity paradox [55, 75] theories arguing that a minuscule cognitive distance inhibits learning and innovation. Thus, the acceptance of hypothesis 3 stresses the potential conflict of crowdsourcing architecture and crowdsourcing governance design decisions within innovation systems in the local knowledge environments. A conflict not previously addressed in crowdsourcing literature.

Crowdsourcing composition is the decision about the number stages in the innovation process that crowdsourcing is integrated into. Hypothesis 5 advocated for the benefit of a simple composition in the local knowledge environment. Model 3 depicts a positive correlation of multiple stages of crowdsourcing in the innovation system. An effect reduced in model 5. However, table 2 illustrated that innovation system outcome on average is similar for one-stage (idea and choice) as multiple stages of the innovation system. These findings indicate that crowdsourcing is either in a single stage (simple composition) or throughout the entire innovation process (complex composition) in the local knowledge environment. As such, hypothesis 5 is partially supported. With a simple composition, crowd inputs in form of ideas upfront or testing at backend benefit the standardized innovation system in the local knowledge environment. Also benefitting innovation system outcome is the integration of crowdsourcing in all stages. It becomes the knowledge co-creation ability of companies that generates rent in form of unique solutions and difficult-to-imitate resources relative of competitors rather than traditional cost advantages from monopoly and Ricardian rents such as scale economies, capital requirement, and employee know how [8, 83].

Based on the results for the local knowledge environment, crowdsourcing is to be designed with low task specificity of the broadcasted request and timed for the intelligence stage or incorporate into all stages in order for companies to gain optimal innovation system outcome.

[insert table 4 about here]

## 5.2.2 Crowdsourcing design for innovation in distant environments

Table 4 shows how the crowdsourcing design decisions relate to innovation system outcome in a distant knowledge environment. For task purpose decisions, the expectation was equal importance across intelligence, design and choice. Model 1 shows that intelligence (β = .380) and choice (β = .359) purposes of crowdsourcing design are positive at similar levels for innovation system outcome. The results are reinforced in model 4. Differently design is negative but insignificant. Hence, hypothesis 2 is partially supported. One explanation is what can be described as a “solver-ability” reflection. The key point is that the ability to co-create is a privilege of expert users in a crowd (lead users and hobby experts)[46]. In other words, crowdsourcing targets a crowd too broadly to fulfill the design purpose thereby generating noise in the external sourced information for the innovation system. As such, the results are not reflecting that crowdsourcing is ineffective for design and development in the innovation system. Rather, crowdsourcing design decisions for innovation system integration should be reflected in the governance design of the applied platform. Literature on crowdsourcing platform design has not previously distinguished between innovation task purposes in the platform governance recommendations [10].

For crowdsourcing specificity, hypothesis 4 stated that high task specificity would be important for innovation system outcome. However, the results in table 4 demonstrates that task specificity is mainly insignificant for innovation outcome in the distant environment, leading to a rejection of hypothesis 4. Differently from the local knowledge environment, innovation system outcome is not benefitting from task specificity. Although surprising, because high task specificity is a central success measure of crowdsourcing platform performance [3, 17, 38], an explanation can be given in the characteristics of the distant knowledge environment. In the distant knowledge environment, even a well-structured specification of a task is openended relative of the local search environment because of the cognitive distance to the company knowledge system [3]. The high system outcome averages for low and high task specificity in table 2 support this.

In congruence with the more-is-better assumption underlying open innovation [65, 84, 85], hypothesis 3 forwarded that increasing complexity of the crowdsourcing composition would benefit innovation system outcome positively. The results in table 3 and table 4 confirm this relationship leading to acceptance of hypothesis 6. However, simple compositions of crowdsourcing render high average innovation system outcomes to companies according to table 2 $( \beta _ { \mathrm { i n t e l l i g e n c e } } = . 5 0 1 ; \beta _ { \mathrm { c h o i c e } } = . 5 3 9 )$ that are similar to complex crowdsourcing compositions $( \beta _ { \mathrm { t w o - s t a g e s } } = . 4 5 5 ; \beta _ { \mathrm { t h r e e - s t a g e s } } = . 6 3 7 )$ . These findings indicate that several composition design option may exist.

Overall, the findings are for the distant knowledge environment that crowdsourcing integration into the innovation system pertains to delicate purpose and composition decisions. In particular, research find that purpose and composition are systematically the most closely associated design elements of crowdsourcing as

## 5.2.3 Further analysis

The combination of task purpose and task composition conceptualizes the timing decision of crowdsourcing integration into a company innovation system. The results in table 3 and table 4 demonstrate that purpose and composition are positive for both environments. To illustrate the knowledge environment differences outlined above, the innovation system outcome gained from each combination of purpose and composition is depicted in figure 2. The graph for the local knowledge environment shows peak performance for innovation system outcome of companies integrating crowdsourcing in the idea stage or throughout the entire innovation process. For the distant knowledge environment, the graph illustrates several performance peaks from complex timing decisions: a one-stage composition with choice purpose, a two-stage composition with idea and choice purposes, and a three-stage composition with all purposes.

## [insert figure 2 about here]

Within crowdsourcing literature, this study aids in explaining two empirical findings. First, empirical studies demonstrate that hosting an idea generation site does not guarantee innovativeness [10]. Figure 2 shows that crowdsourcing at the front end is important for innovation system outcome in the local knowledge environment, but far less effective in the distant knowledge environment. Secondly, empirical evidence has concluded that companies are struggling with full value capture from crowdsourcing integration throughout the innovation system [4, 9]. Figure 2 supports the more-is-better assumption underlying open innovation as

# ACCEPTED MANUSCRIPT

integration of crowdsourcing throughout the innovation system yields highest outcome in both environments. However, figure 2 nuances this conclusion by also demonstrating that there are equal performance efficient design alternatives for companies to select and that the importance of these for innovation system outcome is contingent on the knowledge environment in which the company operates. As such, this study contributes to existing knowledge of crowdsourcing system design through the distinction between local and distant knowledge environments that provides explanation for the mixed results in the literature [4].

## 6. Conclusion

The aim of this paper was to explore the integration of crowdsourcing into the company innovation system in local and distant knowledge environments. The presented results demonstrate that the knowledge environment chosen for innovation search is an important factor for the design decisions of crowdsourcing. In the local knowledge environment, low tasks specificity drives innovation system outcome. This approach to task design is well-documented in external sourcing theory [58], but the approach is new within crowdsourcing design literature. Crowdsourcing design literature states task modularity (high task specificity) as a necessary condition for solver contribution [3, 17, 38] and for the number of submissions received from a crowd [64]. specificity weakens overall innovation system outcome as well as market competitiveness. This result is an important contribution to crowdsourcing literature and highlights the difference between information system design and information management.

Another difference of the two knowledge environments pertains to the timing of crowdsourcing integration. Timing decisions are delicate for innovation system outcome in the distant knowledge environment. Here alternative design options can be chosen, but a simple design in the intelligence stage, i.e. an idea tournament or contest is not among those. Overall, the investigation leads to the conclusion that crowdsourcing design elements have different values for innovation outcome in local and distant knowledge environments, which extends the existing view of crowdsourcing design into the innovation process. Thereby, this investigation of crowdsourcing design decisions contributes to a growing line of research on innovative performance of external sources [18, 59, 86, 87].

# ACCEPTED MANUSCRIPT

## 6.1. Implications

For managers and business owners, the presented findings suggest that competitiveness in the market results from different crowdsourcing design guidelines in the local and distant knowledge environment. This is significant knowledge as it has been stressed that companies are struggling with negative results from opening of their innovation process [9, 84]). The patterns observed in data suggest that the task specification is imperative for innovativeness in a local knowledge environment. Composition and purpose elements of crowdsourcing design are substituted by task openness. Yet, a simple crowdsourcing design like an idea tournament result in positive innovation performance in a local knowledge environment; assuming that task specificity in the tournament is designed as open-ended. In the distant knowledge environment, the recommendations for crowdsourcing design are different. Here, task openness to the crowd is not an option but a requirement of crowdsourcing design. However, in the search of the next market-leading trajectory it is advised to design the integration of crowdsourcing with a complex structure as to ensure the involvement of the crowd in more than one innovation stage. Optimally, ideas from the crowd should be combined with crowd selection to ensure market alignment of the process output thereby lowering the risk of low market performance.

## 6.2. Limitations

While providing interesting insights, it is recognized that this study provides a partial perspective on crowdsourcing integration into an innovation process. With agents-based modelling as the chosen data collection method, the premises of the model founded also limit the outcome and keeps the findings at a purely explorative level. The assumptions underlying the behavioral rules are a simplification of company and crowd interaction through crowdsourcing, but these are designed to ensure the flow of interactions of an innovation system with integrated crowdsourcing. Intentional simplification is a long-time tradition among modelers [33, 88]. The insights provided into gained competitiveness as companies operating in the same market adopt open innovation are a contribution to an understanding of the potential challenges of using crowdsourcing in the innovation process. Still, it is acknowledged that the outcome may be different for other approaches to open innovation, and the presented findings should therefore not be applied to open innovation in general. Our focus,

# ACCEPTED MANUSCRIPT

in fact, is limited to the investigation of the crowdsourcing design elements for innovation process integration. Addressing how governance systems and managerial systems are implemented goes beyond our scope. Case studies of crowdsourcing decisions and performance at portfolio level would provide deeper insights. Furthermore, we disregarded the measurement of satisfaction by company and crowd members from crowdsourcing participation [47]. If that were the interest, longitudinal studies addressing the influence of company and crowd (dis)satisfaction of the crowdsourcing experience and the influence of participation and r follow-up research. Having contributed with knowledge about crowdsourcing design decision for optimal innovation system performance, more research on design decision for the integration of external sources into the innovation system is called for.

## Acknowledgments

The Aarhus University Research Foundation [Grant AUFF AU IDEAS 904324] supported this work.

## Appendix A. Agent calibration

## Appendix A1. Company agents

## Table A1a

Company agents in the local innovation environment (means)

<table><tr><td>Label</td><td>Variable</td><td>Interval</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>References</td></tr><tr><td>Applied knowledge</td><td>AK</td><td>[0;1]</td><td>.485</td><td>.613</td><td>.685</td><td>.276</td><td>.563</td><td>.578</td><td>.468</td><td>[27, 48, 49]</td></tr><tr><td>Technical knowledge</td><td>TK</td><td>[0;1]</td><td>.653</td><td>.630</td><td>.355</td><td>.488</td><td>.544</td><td>.611</td><td>.1824</td><td>[27, 48, 49]</td></tr><tr><td>Integration</td><td> $\lambda$ </td><td>[0;1]</td><td>.630</td><td>.587</td><td>.482</td><td>.473</td><td>.598</td><td>.513</td><td>.592</td><td>[36, 51, 56, 57]</td></tr><tr><td>Internal R&amp;D</td><td> $\eta$ </td><td>[0;1]</td><td>.392</td><td>.407</td><td>.370</td><td>.284</td><td>.264</td><td>.317</td><td>.298</td><td>[35, 36, 56, 57].</td></tr><tr><td rowspan="3">Crowdsourcing combination</td><td>Stage 1</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Stage 2</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Stage 3</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr></table>

## Table A1b

Company agents in the distant innovation environment (means)

<table><tr><td>Label</td><td>Variable</td><td>Interval</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>References</td></tr><tr><td>Applied knowledge</td><td>AK</td><td>[0;1]</td><td>.495</td><td>.509</td><td>.619</td><td>.421</td><td>.387</td><td>.498</td><td>.517</td><td>[27, 48, 49]</td></tr><tr><td>Technical knowledge</td><td>TK</td><td>[0;1]</td><td>.771</td><td>.414</td><td>.387</td><td>.513</td><td>.543</td><td>.411</td><td>.362</td><td>[27, 48, 49]</td></tr><tr><td>Integration</td><td> $\lambda$ </td><td>[0;1]</td><td>.648</td><td>.540</td><td>.383</td><td>.282</td><td>.393</td><td>.685</td><td>.697</td><td>[36, 51, 56, 57]</td></tr><tr><td>Internal R&amp;D</td><td> $\eta$ </td><td>[0;1]</td><td>.200</td><td>.250</td><td>.160</td><td>.391</td><td>.492</td><td>.312</td><td>.414</td><td>[35, 36, 56, 57].</td></tr><tr><td rowspan="3">Crowdsourcing combination</td><td>Stage 1</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Stage 2</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Stage 3</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr></table>

## Appendix A2. Crowd member agents

## Tabel A2

Crowd member descriptives (means)

<table><tr><td>Name</td><td></td><td>Lead users</td><td>Hobby experts</td><td>Pioneers</td><td>Requesting users</td><td>First-buyers</td><td>References</td></tr><tr><td rowspan="2">Applied knowledge</td><td rowspan="2">AK1</td><td>[0.8; 1]</td><td>[0; 0.5]</td><td>[0.5; 1]</td><td>[0; 1]</td><td>[0;0.2]</td><td rowspan="2">[45, 46, 50, 53, 54]</td></tr><tr><td>.902</td><td>.257</td><td>.735</td><td>.519</td><td>.109</td></tr><tr><td rowspan="2">Technical knowledge</td><td rowspan="2">TK1</td><td>[0.8; 1]</td><td>[0.5; 1]</td><td>[0.2; 0.5]</td><td>[0; 0.2]</td><td>[0;0.2]</td><td rowspan="2">[45, 46, 50, 53, 54]</td></tr><tr><td>.905</td><td>.740</td><td>.350</td><td>.097</td><td>.093</td></tr><tr><td rowspan="3">Integration</td><td rowspan="3"> $\lambda^2$ </td><td>+10</td><td>-5</td><td>+10</td><td>+1</td><td>-10</td><td rowspan="3">[46, 53, 54, 81]</td></tr><tr><td>+10</td><td>+5</td><td>+5</td><td>-10</td><td>-10</td></tr><tr><td>+10</td><td>+5</td><td>+10</td><td>+1</td><td>-10</td></tr><tr><td>Innovation engagement</td><td>δ</td><td>.516</td><td>.553</td><td>.508</td><td>.514</td><td>.525</td><td>[89-91]</td></tr><tr><td># in crowd</td><td>n</td><td>50</td><td>150</td><td>200</td><td>500</td><td>100</td><td>[53, 54, 81]</td></tr><tr><td>References</td><td></td><td>[92-94]</td><td>[46]</td><td>[45, 95-97]</td><td>[46, 53]</td><td>[95]</td><td></td></tr></table>

<sup>1</sup> [..] is the applied interval for the specific agents in the simulation and the number below is the mean.  
<sup>2</sup> The impact on each of the stages of the simulation is presented.

## References

[1] J. Howells, Intermediation and the role of intermediaries in innovation, Research policy, 35 (2006) 715- 728.

[2] D. Stieger, K. Matzler, S. Chatterjee, F. Ladstaetter-Fussnegger, Democratizing strategy, California Management Review, 54 (2012) 44-68.

[3] A. Afuah, C.L. Tucci, Crowdsourcing as a solution to distant search, Academy of Management Review, 37 (2012) 355–375.

[4] M. Ma, R. Agarwal, Through a Glass Darkly: Information Technology Design, Identity Verification, and Knowledge Contribution in Online Communities, Information Systems Research, 18 (2007) 42-67.

[5] J. Füller, H. Mühlbacher, K. Matzler, G. Jawecki, Consumer empowerment through Internet-based cocreation, Journal of Management Information Systems, 26 (2009-2010) 71-102.

[6] L.B. Jeppesen, K. Laursen, The role of lead users in knowledge sharing, Research Policy, 38 (2009) 1582- 1589.

[7] C. Fuchs, M. Schreier, Customer empowerment in new product development, Journal of Product Innovation Management, 28 (2011) 17-32.

[8] R. Reed, S. Storrud-Barnes, L. Jessup, How open innovation affects the drivers of competitive advantage, Management Decision, 50 (2012) 58-73.

[9] M.P. Knudsen, T.B. Mortensen, Some immediate - but negative - effects of openness on product development efforts, Technovation, 31 (2011) 54-64.

[10] I. Blohm, S. Zogaj, U. Bretschneider, J.M. Leimeister, How to manage crowdsourcing platforms effectively?, California Management Review, 60 (2018) 122-149.

[11] R.T. Nakatsu, E.B. Grossman, C.L. Iacovou, A taxonomy of crowdsourcing based on task complexity, Journal of Information Science, 40 (2014) 823–834.

[12] G. Saxton, O. Oh, R. Kishore, Rules of Crowdsourcing: Models, issues, and system controls, Information Systems Management, 30 (2013) 2-20.

[13] D. Geiger, M. Schader, Personalized task recommendation in crowdsourcing information systems - Current state of the art, Decision Support Systems, 65 (2014) 3-16.

[14] D. O'Leary, On the relationship between number of votes and sentiment in crowdsourcing ideas and comments for innovation: A case study of Canada's digital compass, Decision Support Systems, 88 (2016) 28-37.

[15] J. Ren, J.V. Nickerson, W. Mason, Y. Sakamoto, B. Graber, Increasing the crowd's capacity to create: how alternative generation affects the diversity, relevance and effectivieness of generated ads, Decision Support Systems, 65 (2014) 28-39.

[16] C.-M. Chiu, T.-P. Liang, E. Turban, What can crowdsourcing do for decision support?, Decision Support Systems, 65 (2014) 40-49.

[17] J. Lampel, P.P. Jha, A. Bhalla, Test-Driving the Future: How Design Competitions Are Changing Innovation, Academy of Management Perspectives, 26 (2012) 71-85.

[18] J. West, M. Bogers, Leveraging external sources of innovation: A review of research on open innovation, Journal of Product Innovation Management, 31 (2014) 814-831.

[19] S. Liu, F. Xia, j. Zhang, W. Pan, Y. Zhang, Exploring the trends, chracteristic antecedents, and performance consequences of crowdsourcing project risks, International Journal of Project Management, 34 (2016) 1625-1637.

[20] R. Garcia, Uses of agent-based modeling in innovation/new product development research, Journal of Product Innovation Management, 22 (2005) 380-398.

[21] H. Rahmandad, J. Sterman, Heterogeneity and network structure in the dynamics of diffusion:

comparing agent-based and differential equation models, Management Science, 54 (2008) 998-1014.

[22] C. Terwiesch, Y. Xu, Innovation contest, open innovation, and multiagent problem solving, Management Science, 54 (2008) 1529-1543.

[23] G. Ziervogel, M. Bithell, R. Washington, T. Downing, Agent-based social simulation: A method for assessing the impact of seasonal climate forecast applications among smallholder farmers, Agricultura systems 83 (2005) 1-26.

[24] R. Katila, E.L. Chen, Effects of Search Timing on Innovation: The Value of Not Being in Sync with Rivals, Administrative Science Quarterly, 53 (2008) 593-625.

[25] D.A. Levinthal, J.G. March, The myopia of learning, Strategic Management Level, 14 (1993) 95-112.

[26] H. Lopez-Vega, F. Tell, W. Vanhaverbeke, Where and how to search? Search paths in open innovation, Research Policy, 45 (2016) 125-136.

[27] L. Rosenkopf, A. Nerkar, Beyond local search: Boundary spanning, exploration, and impact in the optical disk industry, Strategic Management Journal, 22 (2001) 287-306.

[28] I.P. McCarthy, C. Tsinopoulos, P. Allen, C. Rose-Anderssen, New product development as a complex adaptive system of decisions, Journal of Product Innovation Management, 23 (2006) 437-456.

[29] V. Krishnan, K.T. Ulrich, Product development: A review of the literature, Management Science, 47 (2001) 1-21.

[31] R. Katila, G. Ahuja, Something old, Something new: A longitudinal study of search behavior and new product introduction, Academy of Management Journal, 45 (2002) 1183-1194.

[33] J.G. March, Exploration and exploitation in organizational learning, Organization Science, 2 (1991) 71- 87.

[34] H.W. Chesbrough, M.M. Appelyard, Open innovation and strategy, California Management Review, 50 (2007) 57-76.

[35] A.K. Gupta, K.G. Smith, C.E. Shalley, The interplay between exploration and exploitation, Academy of Management Journal, 49 (2006) 693-706.

[36] W. Cohen, D.A. Levinthal, Absorptive capacity: A new perspective on learning and innovation, Administrative Science Quarterly, 35 (1990) 128-152.

[37] J. Grönlund, D.R. Sjödin, J. Frishammar, Open innovation and the stage-gate process, California Management Review, 52 (2010) 106-131.

[38] L.B. Jeppesen, K.R. Lakhani, Marginality and problem-solving effektiveness in broadcast search, Organization Science, 21 (2010) 1016-1033.

[39] C.S. Stockstrom, R.C. Goduscheit, C. Lüthje, J.H. Jørgensen, Identifying valuable users as informants for innovation processes:Comparing the search efficiency of pyramiding and screening, Research Policy, 45 (2016) 507-516.

[40] I. Nonaka, G. von Krogh, Tacit Knowledge and Knowledge Conversion: Controversy and Advancement in Organizational Knowledge Creation Theory, Organization Science, 20 (2009) 635-652.

[41] N. Berente, R. Baxter, K. Lyytinen, Dynamics of inter-organizational knowledge creation and information technology use across object worlds: the case of an innovative construction project, Construction Management and Economics, 28 (2010) 569-588.

[42] S. Helper, MacDuffie, J.P. and Sabel, C. , Pragmatic collaborations: advancing knowledge while controlling opportunism., Industrial and Corporate Change, 9 (2000) 443–488.

[43] H.K. Gardner, F. Gino, B.R. Staats, Dynamically integrating knowledge in teams: Transforming resources into performance, Academy of Management Journal, 55 (2012) 998-1022.

[44] S. Nambisan, Information systems as a reference discipline for new product development, MIS Quaterly, 27 (2003) 1-18.

[45] K.R. Jespersen, Online Channels and Innovation: Are users being empowered and involved?. International Journal of Innovation Management, 15 (2011) 1141-1159.

[46] P.R. Magnusson, Exploring the contributions of involving ordinary users in ideation to technologybased services, Journal of Product Innovation Management, 26 (2009) 578-593.

[47] C.K. Prahalad, V. Ramaswamy, The new frontier of experience innovation, Sloan Management Review, DOI (2003) 12-18.

[48] A.B. Hargadon, Brokering Knowledge: Linking learning and innovation, Organizational Behavior 24 (2002) 41-85.

[49] S. Nambisan, Designing virtual customer environments for new product development: Toward a theory, Academy of Management Review, 28 (2002) 392-413.

[50] C. Lüthje, Characteristics of innovating users in a consumer goods field: An empirical study of sportsrelated product consumers, Technovation, 24 (2004) 683-695.

## ACCEPTED MANUSCRIPT

[51] T.B. Kasdan, P. Rose, F.D. Fincham, Curiosity and exploration: Facilitating positive subjective experiences and personal growth opportunities., Journal of Personality Assessement, 82 (2004) 291-305.

[52] J.M. Bonner, O.C. Walker, Selecting influential business-to-business customers in new product

development: relational embeddedness and knowledge heterogenity considerations, Journal of Product Innovation Management, 21 (2004) 155-169.

[53] E. Enkel, J. Perez-Freije, O. Gassmann, Minimizing Market Risks Through Customer Integration in New Product Development: Learning from practice, Creativity and Innovation Management, 14 (2005) 425-437.

[54] K.R. Jespersen, User-involvement and open innovation: The case of decision-maker openess,

International Journal of Innovation Management, 14 (2010) 471-489.

[55] B. Nooteboom, W.V. Haverbeke, G. Duyesters, V. Gilsing, A.v.d. Oord, Optimal cognitive distance and absorptive capacity, Research Policy, 36 (2007) 1016-1034.

[56] G. Todorava, B. Durisin, Absorptive capacity: Valuing a reconceptualization, Academy of Management Review, 32 (2007) 774-786.

[57] S.A. Zahra, G. George, Absorptive capacity: A review, reconceptualization, and extension, Academy of Management Review, 27 (2002) 185-203.

[58] K. Laursen, A. Salter, Open for innvoation: The role of openness in explaning innovation performance among U.K. manufacturing firms, Strategic Management Journal, 27 (2006) 131-150.

[59] K. Laursen, A.J. Salter, The paradox of openness: Appropriability, external search and collaboration, Research Policy, 43 (2014) 867-878.

[60] J. Morgan, R. Wang, Tournaments for ideas, California Management Review, 52 (2010) 77-97.

[61] J. Nicholas, A. Ledwith, J. Bessant, Reframing the search space for radical innovation, Reseach-Technology Management, 56 (2013) 27-35.

[62] E. Danneels, Disruptive technology reconsidered: A critique and research agenda, Journal of Product Innovation Management, 21 (2004) 246-258.

[63] G.M. Schmidt, C.T. Druel, When is a disruptive innovation disruptive?, Journal of Product Innovation Management, 25 (2008) 347-369.

[64] H.J. Khasraghi, A. Aghaie, Crowdsourcing contests: understanding the effect of competitors

participation history on their performance, Behaviour & Information Technology, 33 (2014) 1383–1395.

[65] C. Baldwin, E.v. Hippel, Modeling a Paradigm Shift: From Producer Innovation to User and Open Collaborative Innovation, Organziational Science, 22 (2011) 1399–1417.

[66] C. Dröge, R. Calantone, N. Harmancioglu, New product success: Is it really controllable by managers in highly turbulent environments?, Journal of Product Innovation Management, 25 (2008) 272-286.

[67] I. Alam, Removing the fuzziness from the fuzzy front-end of service innovations thorugh customer interactions, Industrial Marketing Management, 35 (2006) 468-480.

[68] D.G. Sirmon, M.A. Hitt, Contingencies within dynamic managerial capabilities: Interdependent effects of ressource investment and deployment on firm performance., Strategic Management Journal, 30 (2009) 1375-1394.

[69] X. Koufteros, M. Vonderembse, W. Doll, Integrated product development practices and competitive capabilities: the effect of uncertainty, equivocality, and platform strategy, Journal of Operations Management, 20 (2002) 331-355.

[70] U. Lichtenthaler, Outbound open innovation and its effect on firm performance: examing environmental influences, R&D management, 39 (2009) 317-330

[71] J.A. Siguaw, P.M. Simpson, C.A. Enz, Conceptualizing Innovation Orientation: A framework for study and integration of innovation research, Journal of Product Innovation Management, 23 (2006) 556-574.

[72] N.J. Foss, J.F.l. Christensen, A Market-Process Approach to Corporate Coherence, Managerial & Decision Economics, 22 (2001) 213-226.

[73] V.v.d. Vrande, Research notes and commentaries. Balancing your technology-sourcing portfolio: How sourcing mode diversity enhances innovative performance, Strategic Management Journal, 34 (2013) 610– 621.

[74] D.J. Teece, R. Rumelt, G. Dosi, S. Winter, Understanding corporate coherence, Journal of Economic Behavior & Organization, 23 (1994) 1-30.

[75] B. Nooteboom, Learning by Interaction: Absorptive Capacity, Cognitive Distance and Governance. , Journal of Management and Governance, 4 (2000) 69-92.

[76] C. Hienerth, E.v. Hippel, M.B. Jensen, User community vs. producer innovation development efficiency: A first empirical study, Research Policy, 43 (2014) 190-201.

[77] R.G. Cooper, Perspective: The Stage-Gate Idea-to-launch process - Update, what's new, and NexGen Systems., Journal of Product Innovation Management, 25 (2008) 213-232.

[78] H. Wang, J. Li, Untangling the effect of overexploitation and overexploration on organizational

performance: the moderating role of environmental dynamism, Journal of Management, 34 (2008) 925- 951.

[79] C.A. Coen, C.A. Maritan, Investing in capabilities: The dynamics of resource allocation, Organization Science, 22 (2011) 99-117.

[80] M.J. North, C.M. Macal, Managing business complexity: Discovering strategic solutions with agent based modeling and simulation, Oxford University Press, New York, 2007.

[81] D. Tapscott, A.D. Williams, Wikinomics: How Mass Collaboration Changes Everything, 2006.

[82] S. Adamczyk, A.C. Bullinger, K.M. Möslein, Innovation contests: A review, classification and outlook, Creativity and Innovation, 21 (2012) 335-360.

[83] J.T. Marcher, C.S. Boerner, Expertience and scale and scope economier: Trade-offs and performance in development, Strategic Management Journal, 27 (2006) 845-865.

[84] E. Enkel, O. Gassmann, H.W. Chesbrough, Open R&D and open innovation: Exploring the phenomenon, R&D management, 39 (2009) 311-316.

[85] E.K.R.E. Huizingh, Open innovation: state of the art and future perspectives, Technovation, 31 (2011) 2- 9.

[86] B. Cassiman, R. Veugelers, In search of complementarity in innovation strategy: Internal R&D and external knowledge acquisition, Management Science, 52 (2006) 68-82.

[87] M. Segarra-Ciprés, J.C. Bou-Llusar, V. Roca-Puig, Exploring and exploiting external knowledge: The effect of sector and firm technological intensity, Innovation: Management, Policy & Practice, 14 (2012) 203- 217.

[88] N. Siggelkow, J.W. Rivkin, When exploration backfires: Unintended consequences of multilevel organizational search, Academy of Management Journal, 49 (2006) 779-795.

[89] C. Schulz, S. Wagner, Outlaw community innovations, International Journal of Innovation Management, 12 (2008) 399-418.

[90] L. Chen, J.R. Marsden, Z. Zhang, Theory and analysis of company-sponsered value co-creation, Journal of Management Information Systems, 29 (2012) 141-172.

[91] V. Mahajan, E. Muller, R.K. Srivastava, Determination of adopter categories by using innovation diffusion models, Journal of Marketing Research, 27 (1990) 37-50.

[92] M. Bogers, A. Afuah, B. Bastian, Users as innovators: A review, critique, and future research directions, Journal of Management, 36 (2010) 857-875.

[93] M. Schreier, R. Prügl, Extending lead-user theory:Antecendents and consequences of consumers' lead userness, Journal of Product Innovation Management, 25 (2008) 331-346.

[94] E. von Hippel, Economics of product development by users: The impact of 'sticky' local information, Management Science, 44 (1998) 629-644.

[95] K.L. Janssen, B. Dankbaar, Proactive involvement of consumers in innovation: Selecting appropriate techniques, International Journal of Innovation Management, 12 (2008) 511-541.

[96] J.H. Kim, Z.-T. Bae, The role of online brand community in new product development: Case studies on digital product manufacturers in Korea, International Journal of Innovation Management, 12 (2008) 357- 376.

[97] C. Li, J. Bernoff, Groundswell: winning in a world transformed by social technologies, Harvard Business Press, Boston, MA, 2008.

![](/api/attachments/6U62ARCK/fulltext/images/4a2a9ccec54196714c6003b5d541b23d9aae77f81dbfa796e0b14e8914f17506.jpg)  
Fig. 1. The integration of crowdsourcing in the innovation system.

## ACCEPTED MANUSCRIPT

Correlations and means of constructs in the local knowledge environment.

<table><tr><td>Local search</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>Mean</td></tr><tr><td>1. Composition</td><td>.1964</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.50</td></tr><tr><td>2. Specificity</td><td>.208</td><td>.5498</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>.2342</td></tr><tr><td>3. LfC stage 1</td><td>.178</td><td>.489***</td><td>.5497</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>32.565</td></tr><tr><td>4. LfC stage 2</td><td>-0,063</td><td>-.179</td><td>-.229</td><td>.5443</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-74.112</td></tr><tr><td>5. LfC stage 3</td><td>.302*</td><td>.482***</td><td>.223</td><td>.042</td><td>.6346</td><td></td><td></td><td></td><td></td><td></td><td>49.044</td></tr><tr><td>6. Intelligence Purpose</td><td>.471***</td><td>.149</td><td>.376**</td><td>-.034</td><td>-.008</td><td>-</td><td></td><td></td><td></td><td></td><td>.50</td></tr><tr><td>7. Design purpose</td><td>.471***</td><td>.046</td><td>.028</td><td>-.189</td><td>.06</td><td>-.167</td><td>-</td><td></td><td></td><td></td><td>.50</td></tr><tr><td>8. Choice purpose</td><td>.471***</td><td>.1</td><td>-.152</td><td>.134</td><td>.375**</td><td>-.167</td><td>-.167</td><td>-</td><td></td><td></td><td>.50</td></tr><tr><td>9. Inno. Sys. outcome</td><td>.406***</td><td>.664***</td><td>.500***</td><td>-.059</td><td>.609</td><td>.373**</td><td>-.074</td><td>.275*</td><td>.1627</td><td></td><td>.3536</td></tr><tr><td>10. Market outcome</td><td>.221</td><td>.325***</td><td>.298*</td><td>-.048</td><td>.271*</td><td>.282*</td><td>-.118</td><td>.149</td><td>.626***</td><td>.1389</td><td>142.85</td></tr></table>

Notes: The table presents the correlations of crowdsourcing design elements and the innovation system outcome. The diagonal holds the estimated discriminant validity coefficients. \*Significant at the 10% level; \*\*significant at the 5% level; \*\*\*significant at the 1% level.

Correlations and means of constructs in the distant knowledge environment.

<table><tr><td>Distant search</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>Mean</td></tr><tr><td>1. Composition</td><td>.1964</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.50</td></tr><tr><td>2. Specificity</td><td>-.078</td><td>.5498</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>.7563</td></tr><tr><td>3. LfC stage 1</td><td>.283*</td><td>-.340**</td><td>.5497</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>37.950</td></tr><tr><td>4. LfC stage 2</td><td>-.08</td><td>.059</td><td>-.027</td><td>.5443</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-14.641</td></tr><tr><td>5. LfC stage 3</td><td>.398***</td><td>-.014</td><td>.117</td><td>-.077</td><td>.6346</td><td></td><td></td><td></td><td></td><td></td><td>92.656</td></tr><tr><td>6. Intelligence Purpose</td><td>.471***</td><td>-.397***</td><td>.527***</td><td>.226</td><td>.065</td><td>-</td><td></td><td></td><td></td><td></td><td>.50</td></tr><tr><td>7. Design purpose</td><td>.471***</td><td>.288*</td><td>.001</td><td>-.236</td><td>.000</td><td>-.167</td><td>-</td><td></td><td></td><td></td><td>.50</td></tr><tr><td>8. Choice purpose</td><td>.471***</td><td>.071</td><td>-.125</td><td>-.115</td><td>.522***</td><td>-.207</td><td>-.110</td><td>-</td><td></td><td></td><td>.50</td></tr><tr><td>9. Inno. Sys. outcome</td><td>.359**</td><td>-.078</td><td>.398***</td><td>.436***</td><td>.395***</td><td>.299*</td><td>-.241</td><td>.427***</td><td>.1627</td><td></td><td>.4257</td></tr><tr><td>10. Market output</td><td>.128</td><td>-.198</td><td>.159</td><td>.344**</td><td>.219</td><td>.248</td><td>-.155</td><td>.130</td><td>.533***</td><td>.1389</td><td>142.85</td></tr></table>

Notes: The table presents the correlations of crowdsourcing design elements and the innovation system outcome. The diagonal holds the estimated discriminant validity coefficients. \*Significant at the 10% level; \*\*significant at the 5% level; \*\*\*significant at the 1% level

Table 2  
Output across the crowdsourcing design elements

<table><tr><td rowspan="2"></td><td colspan="4">Local knowledge environment</td><td colspan="4">Distant knowledge environment</td></tr><tr><td>Crowd members</td><td>LfC level</td><td>Inno. Sys. outcome</td><td>Market outcome</td><td>Crowd members</td><td>LfC level</td><td>Inno. Sys. outcome</td><td>Market outcome</td></tr><tr><td colspan="9">Purpose:</td></tr><tr><td>Intelligence</td><td>578.00</td><td>110.706</td><td>.435</td><td>124.38</td><td>511.00</td><td>187.501</td><td>.501</td><td>150.67</td></tr><tr><td>Design</td><td>538.00</td><td>87.238</td><td>-.074</td><td>103.00</td><td>478.67</td><td>120.057</td><td>.365</td><td>131.50</td></tr><tr><td>Choice</td><td>550.63</td><td>120.024</td><td>.376</td><td>127.71</td><td>506.65</td><td>205.512</td><td>.539</td><td>153.83</td></tr><tr><td colspan="9">Specificitya:</td></tr><tr><td>High</td><td>156.68</td><td>102.414</td><td>.266</td><td>89.56</td><td>543.38</td><td>139.801</td><td>.498</td><td>138.71</td></tr><tr><td>Low</td><td>611.74</td><td>175.050</td><td>.493</td><td>163.52</td><td>199.71</td><td>124.534</td><td>.594</td><td>111.29</td></tr><tr><td colspan="9">Composition:</td></tr><tr><td>one-stage</td><td>148.56</td><td>53.999</td><td>.255</td><td>119.56</td><td>231.72</td><td>73.912</td><td>.325</td><td>138.61</td></tr><tr><td>two-stages</td><td>478.56</td><td>61.632</td><td>.383</td><td>114.94</td><td>506.56</td><td>105.037</td><td>.455</td><td>127.44</td></tr><tr><td>three-stages</td><td>1116.50</td><td>246.692</td><td>.559</td><td>124.00</td><td>757.50</td><td>390.849</td><td>.637</td><td>180.33</td></tr><tr><td>Overall</td><td>374.73</td><td>84.798</td><td>.3536</td><td>118.214</td><td>371.54</td><td>132.531</td><td>.4257</td><td>139.788</td></tr></table>

<sup>a</sup> High task specificity is measured as below average equaling a well-structured task; Low task specificity is measured as above average equaling an open-ended task.  
Note: The table presents the estimated means of the innovation system outcomes for the crowdsourcing design decision together with the mean number of crowd members responding to the crowdsourcing request.

Table 3  
Estimates for innovation system outcome in the local search environment

<table><tr><td rowspan="2"></td><td colspan="5">Innovation system outcome</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td colspan="6">Purpose:</td></tr><tr><td>Intelligence</td><td>0.443***(3.064)</td><td></td><td></td><td>0.346***(2.808)</td><td></td></tr><tr><td>Design</td><td>0.060(0.414)</td><td></td><td></td><td>0.006(0.048)</td><td></td></tr><tr><td>Choice</td><td>0.359***(2.484)</td><td></td><td></td><td>0.176*(1.365)</td><td></td></tr><tr><td>Low Specificity</td><td></td><td>0.612***(4.897)</td><td></td><td>0.521***(4.160)</td><td>0.539***(4.240)</td></tr><tr><td>Composition</td><td></td><td></td><td>0.406***(2.810)</td><td></td><td>0.243**(1.913)</td></tr><tr><td> $R^2$ </td><td>0.259</td><td>0.375</td><td>0.165</td><td>0.495</td><td>0.428</td></tr><tr><td>F</td><td>4.438</td><td>23.976</td><td>7.898</td><td>9.084</td><td>14.616</td></tr></table>

Notes: The table presents the estimation results of the OLS regression models. The dependent variable is the innovation system outcome of the simulation in Equation 3. T-statistics are in parentheses  
\*Significant at the 10% level; \*\*significant at the 5% level; \*\*\*significant at the 1% level

## Table 4

Estimates for innovation system outcome in the distant search environment

<table><tr><td rowspan="2"></td><td colspan="5">Innovation system outcome</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td colspan="6">Purpose:</td></tr><tr><td>Intelligence</td><td>0.380***(2.798)</td><td></td><td></td><td>0.441***(3.107)</td><td></td></tr><tr><td>Design</td><td>-0.123(-0.918)</td><td></td><td></td><td>-0.140(-1.051)</td><td></td></tr><tr><td>Choice</td><td>0.492***(3.647)</td><td></td><td></td><td>0.502***(3.753)</td><td></td></tr><tr><td>Low Specificity</td><td></td><td>0.021(0.131)</td><td></td><td>0.185*(1.345)</td><td>0.079(0.521)</td></tr><tr><td>Composition</td><td></td><td></td><td>0.359***(2.435)</td><td></td><td>0.372***(2.465)</td></tr><tr><td> $R^2$ </td><td>0.353</td><td>0.000</td><td>0.129</td><td>0.383</td><td>0.135</td></tr><tr><td>F</td><td>6.917</td><td>0.017</td><td>5.931</td><td>5.931</td><td>3.047</td></tr></table>

Notes: The table presents the estimation results of the OLS regression models. The dependent variable is the innovation system outcome of the simulation in Equation 3. T-statistics are in parentheses  
\*Significant at the 10% level; \*\*significant at the 5% level; \*\*\*significant at the 1% level

![](/api/attachments/6U62ARCK/fulltext/images/6e09d73960f04b5ebc004654aa56b52c2fa893dfe2da83352f6db700416dc487.jpg)  
Fig. 2. Crowdsourcing timing and innovation system outcome

## Biographical note

Kristina Risom Jespersen is Associate Professor in Innovation Economics at The Department of Economics and Business Economics, Aarhus BSS, Aarhus University, Denmark. Her research fields are within open innovation, human capital and innovative work behavior, and the integration of information technology into the innovation system.

Highlights

Crowdsourcing design decisions are pivotal for innovation system integration.

There is a conflict between crowdsourcing platform recommendations and innovation system outcome.

High specification of crowdsourcing task weakens innovation system outcome.

Optimal crowdsourcing design into the innovation system is contingent on targeted innovation environment.

The decided combination of crowdsourcing purpose and composition is delicate for the innovation system outcome.
