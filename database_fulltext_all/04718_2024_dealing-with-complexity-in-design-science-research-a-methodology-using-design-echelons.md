---
otero_id: 4718
otero_key: "M9TMFDUY"
title: "Dealing with Complexity in Design Science Research: A Methodology Using Design Echelons"
authors: "Tuure Tuunanen; Robert Winter; Jan vom Brocke"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/16700"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DEALING WITH COMPLEXITY IN DESIGN SCIENCE RESEARCH: A METHODOLOGY USING DESIGN ECHELONS<sup>1</sup>

Tuure Tuunanen Faculty of Information Technology, University of Jyväskylä, Jyväskylä, FINLAND {tuure@tuunanen.fi}

Robert Winter Institute of Information Management, University of St. Gallen, St. Gallen, SWITZERLAND {robert.winter@unisg.ch}

Jan vom Brocke European Research Center for Information Systems, University of Münster, Münster, GERMANY {jan.vom.brocke@uni-muenster.de)

Design science research (DSR) aims to generate knowledge about innovative solutions to real-world problems. Consequently, DSR needs to deal with the complexity related to problem and solution spaces involving sociotechnical phenomena that people perceive differently and are subject to constant change. This complexity poses challenges to sequential, process-based approaches—specifically, the existing DSR methodology. We designed a DSR methodology that extends existing approaches by adding a complementary organizing logic to address complexity. Based on the theory of hierarchical, multilevel systems, we suggest organizing DSR based on the concept of “echelons”—meaning decomposing DSR projects into smaller logically coherent self-contained parts—and suggest a set of five design echelons that imply a hierarchical organizing logic for DSR projects. The echeloned DSR (<sup>e</sup>DSR) methodology was developed in five iterations, involving seven design and evaluation episodes.

Keywords: Design science research, methodology, research project complexity, design knowledge development, organizing logic, design echelon, echelon-specific validation

## Introduction

Design science research (DSR) generates knowledge by designing and evaluating innovative and purposeful artifacts<sup>2</sup> to real-world problems (Hevner et al., 2004; Peffers et al., 2007). Such design knowledge can take diverse forms, including generic problem solutions (Winter, 2008), design principles (Chandra et al., 2015), and design theories (Gregor & Jones, 2007). It may also provide a foundation for behavioral science, which develops and tests theories about how people engage with artifacts (Baskerville et al., 2018; Hevner et al., 2004). Design knowledge generally makes statements about means-end relationships between problem and solution spaces (Venable, 2006; vom Brocke et al., 2020). With its focus on innovative solutions to real-world problems, DSR is a research paradigm that can increase the practical relevance of research, and information systems (IS) research in particular (Lee, 2015; vom Brocke et al., 2013) and, as such, may contribute to solving greater societal and economic challenges (Becker et al., 2015).

Peffers et al. (2007) conceptualized the DSR process as consisting of six phases, namely problem identification, definition of objectives, design and development, demonstration, evaluation, and communication of results. While the DSR process builds on extant knowledge often referred to as kernel theories, its strategy of inquiry particularly builds on creative thinking and innovative problem-solving, evidenced by evaluating potential solutions in context (vom Brocke et al., 2020).

With the focus on the generation of innovative solutions to real-world problems, DSR projects<sup>3</sup> need to deal with complexity on a variety of fronts: (1) DSR projects involve close interaction with stakeholders from the real world, specifically representatives from industry or society, (2) they are broad and open-ended in scope as both the problem and solution space needs to be understood and defined in the course of the project, and (3) they are subject to the possible change in all elements over the course of the project. Rai et al. (2017) refer to DSR projects as projects that deal with complex sociotechnical systems. In the same editorial, Alan Hevner reflects on the challenges of intellectual control of such DSR projects (Rai et al., 2017, p. 5) and highlights two complexity-related challenges: (1) understanding the problem and formulating the research objectives, which often requires several nonlinear DSR iterations, and (2) organizing the research process to generate and validate solutions, as the process can at best be planned in essential stages of development but must be adapted in detail to the situational conditions, which evolve as a project progresses. We discuss both challenges further in the following:

1. Problem and objectives challenge: DSR can be subject to complexity in problem understanding, as different people have different perceptions of (and perspectives on) real-world problems; most problems are abstract and subject to change. To deal with this complexity, DSR adopts an iterative approach to problem understanding and objective formulation (vom Brocke et al., 2020). This is a particularly demanding challenge, as noted by Strong et al. (2020): “We started to use existing DSR methodologies to guide our DSR project, we encountered challenges in applying them. Our problem was not well defined and feasible solutions were unknown, and as a result, our research problem and its feasible solutions evolved as we conducted a series of DSR projects ... Thus, a methodology based on defining the problem and building an artifact that would solve the problem did not fit well.” (p. 1).

2. Process and validation challenge: DSR projects often develop multiple instantiations of the artifact used in different situations. For example, Tuunanen and Peffers (2018) used the developed artifacts in five organizations in multiple countries, and more than 200 people participated in the DSR program. Thus, we also need to ensure that the use of multiple instantiations in different situations receives appropriate methodological support. Lukyanenko et al. (2014) introduced the concept of instantiation validity (analogous to construct validity in survey research or design validity in experimental research), referring to the validity of IT artifacts as instantiations of theoretical constructs. The existing DSR methodology does not provide support in ensuring instantiation validity.

Considering the complexity of DSR projects, we propose rethinking DSR based on the theory of hierarchical, multilevel systems (Mesarovic et al., 1970). This entails decomposing a complex DSR project into specifically defined intermediate self-contained units—which, drawing on hierarchical systems theory, we refer to as “echelons” (Mesarovic et al., 1970). With an echelon-oriented approach, we decompose a (larger) problem into a hierarchy of several logical subproblems. We create solutions for such subproblems, which serve as intermediate results that can be developed, validated, and communicated independently. In combination, such intermediate results contribute to the overall solution.

Echelons are essentially organizing units that the DSR researcher can choose freely according to their understanding and choice to decompose a problem. To further conceptualize the echeloned DSR (<sup>e</sup>DSR) methodology, we distinguish five types of design echelons. One form of type formation is to differentiate design echelons as they combine specific analysis/design and validation activities related to a specific intermediate state of the artifact:

1. Problem analysis: contributing the problem statement

2. Objectives and requirements definition: contributing design requirements

3. Design and development: contributing a projectable solution design

4. Demonstration: contributing an illustrative instance of the artifact (in an artificial or natural context)

5. Evaluation: contributing the contextualized artifact in use

For the design echelon types, which we built by combining specific analysis/design and validation activities related to a specific intermediate state of the artifact, we intentionally chose names that represent certain activities and a certain type of (intermediate) artifact. While these names typify design echelons as they accomplish intermediate contributions to specific analysis/design and validation activities, they conceptually differ from activities:

1. Each design echelon makes a distinct contribution to design knowledge. Thus, in this paper, we discuss criteria for rigorously crafting and validating each echelon so that it can be communicated. This way, iteration is supported in DSR projects (problem and objectives challenge), as design knowledge is represented in smaller self-contained and validated units. Iteration can be organized to focus more closely on the contributions of the parts to the entire solution and to follow a more concurrent sequence.

2. Design echelons also relate to one another in one-tomany relations in such a way that (for example), for one set of objectives and requirements, multiple echelons may suggest alternative designs to meet these requirements. Every solution design may have multiple illustrative instances, e.g., in a different context to demonstrate mutability (process and validation challenge). For every design instance, there may (and should) be multiple uses that provide evidence for its utility.

Thus, it is important to note that the design echelons conceptually differ from process phases (e.g., DSRM process phases), not only because they combine specific activities with specific stages of intermediate design knowledge but also because they form a hierarchical network of self-contained DSR components and their conceptualization can be directly justified by hierarchical systems theory.

However, our intention is not to replace the existing DSR methodology. We intend to offer a new but complementary way of structuring and organizing DSR projects to advance our capabilities as a community to better deal with the complexity of DSR projects, especially those that involve sociotechnical systems and involve close interaction with stakeholders from industry and/or society (Tuunanen & Peffers, 2018). Our contribution especially applies in complex DSR projects, where the logic of sequential, process-based activities does not address the earlier defined (1) problem and objective challenge and/or (2) process and validation challenge. Our objective is to help researchers deal with complexity in DSR projects. Thus, we seek to answer the following research question: How can we use design echelons to support planning, conducting, and communicating knowledge creation in complex projects? Our paper reports a five-year DSR study, including five major iterations that developed and evaluated a novel DSR methodology to address this gap in the existing DSR literature.

This paper is structured as follows: First, we give an account of related work and argue for a need to advance the extant sequential, process-based view of DSR toward a new echelon-oriented view of DSR to organize complex DSR projects. Next, the study’s research design is described, and the proposed DSR methodology is introduced. The methodology is then demonstrated using several published DSR cases, and evaluative evidence of the methodology’s utility is presented. Finally, the findings are discussed, and conclusions are then drawn.

## Echelons as a Foundation for Planning, Conducting, and Communicating DSR Projects

DSR has been practiced in many research communities for several decades (Winter, 2008). However, it only became more visible in the international IS literature with the publication of seminal papers in the 1990s by Nunamaker et al. (1991) and Walls et al. (1992). These two articles introduced DSR to the IS literature but proposed different research process models. The systems development approach of Nunamaker et al. (1991) promoted interactions between systems development, experimentation, observation, and theory building. Walls et al. (1992) looked at theory development more closely, using kernel theories and requirements related to problem generalizations (i.e., metarequirements). Later, Hevner et al. (2004) proposed a cyclical model of specific DSR iterations comprising development, building, and evaluation activities. Kuechler and Vaishnavi (2008) then proposed a linear process model with the following stages: awareness of a problem, suggestion of a design, development, evaluation, and conclusion.

The DSR methodology (DSRM) proposed by Peffers et al. (2007) built on these methodological proposals and suggested a way to conduct DSR in IS. DSRM consists of six phases: (1) identifying the problem and motivation, (2) defining the objectives, (3) designing, (4) demonstrating, (5) evaluating, and (6) communicating (Peffers et al., 2007). The process thus begins with identifying the research problem(s) and the motivation for the research. Based on the evidence, reasoning, and inference, the process continues to define the objectives of a solution to solve the research problem. This process should be based on prior knowledge in the given field and then used to design and develop an artifact and create “how-to” knowledge. The artifact may then be used to solve the described problem. This process demonstrates the artifact in a suitable context before evaluating its effectiveness and/or efficiency. The DSRM approach produces disciplinary knowledge communicated to academia and practitioners. This process can and should be iterative. DSRM also proposes four possible entry points to the research process. The first is the traditional problem-centered initiation, which can also be found in qualitative and quantitative research methodologies. The second is the objective-centered solution approach, which enables researchers to approach the research project by first setting (quantitative or qualitative) objectives to establish how the new artifact is expected to support solutions to achieve the stated objectives. The third entry point is design-centered, in which initiation can result from an interesting design or development problem. The fourth entry point is where the design starts with a research client.

However, with DSRM, evaluation can only occur after design and development (Sonnenberg & vom Brocke, 2012); all discussed DSR guidance positions, and evaluation activities occur after the design and development activities. Even if evaluation is understood as a multi-episode validation journey rather than a monolithic phase (e.g., Venable et al., 2016; Strong et al., 2020), it is still not fundamentally interlaced with the design process creating multiple intermediate artifacts. However, it may be much better for complex problems or solutions to “fail early, fail often” (Abraham et al., 2014). This principle is also a cornerstone of the agile methods increasingly replacing traditional phase-based approaches in software development (Conboy, 2009). Validation should not be an afterthought but rather an integral part of problem analysis, objective definition, and design or development. These activities should focus on different intermediate artifacts relevant to the nascent design knowledge (Sonnenberg & vom Brocke, 2012). This holds not only for routine design but also for theorizing design (Gregory & Muntermann, 2014, p. 646). Such integration of design and validation activities offers a clearer understanding of how different intermediate artifacts should be designed in such complex DSR projects.

Sonnenberg and vom Brocke (2012) built on prior work describing DSR activities within the overall DSR process, arguing that these activities progress toward the intended artifacts differently and thus offer the potential for understanding multi-episode design process that can include multiple intermediate artifacts. Such a design process can mitigate risk, as early feedback on the incremental steps leading to the eventual artifact can be incorporated into the design process. The obtained information can also be directed better if the validation focuses on the different aspects of design, i.e., intermediate artifacts when relevant decisions are being made during the design process. For this purpose, Sonnenberg and vom Brocke (2012) identified four validation activities (which they designated as evaluation types): evaluation of the problem understanding, evaluation of the design, evaluation of the instantiation, and evaluation of the artifact in use. Following this approach, design knowledge is built in four stages, and specific analysis/design activities are directly related to the respective stage of design knowledge.

While the Sonnenberg/vom Brocke model makes important progress toward a more differentiated process to deal with the (particularly evaluation-related) challenges of complexity in DSR, its sequentialization of knowledge development phases is not informed by complexity science, and its process phases are, as in other DSR process models, conceptually detached from iterations. A suitable organizing logic for complex DSR projects should aim at integrating process phases and build/evaluate iterations into a model that guides researchers even in the face of multiple abstraction levels, complex artifacts, changing contexts, and evolving problem understanding. It should also account for the incremental knowledge accumulation character of complex DSR projects that start with fewer abstract conceptualizations of the problem, solution, and utility before later developing multiple branches of more complete, contextualized conceptualizations. Experience from complex DSR projects shows a mismatch between this hierarchical problem-solving structure and the iterative yet linear process models available for methodological guidance.

## Theory of Hierarchical, Multilevel Systems

We find the general systems theory (von Bertalanffy, 1968; Miller, 1978) an applicable framework for understanding complex sociotechnical systems (e.g., Emery, 2016; Trist & Bamforth, 1951). Researchers, such as Katz and Katz (1966), have considered how to import the metaphor of the living biological organism to describe and explain how sociotechnical systems work, specifically accounting for multiple ways to accomplish various goals. Systems theory laid the foundation for what was later framed as systems thinking, a holistic approach that focuses on how a system's components or subsystems relate to each other and how systems develop over time (Checkland, 1981). The general systems theory literature has emphasized that systems should be viewed as a whole and that the parts are interdependent and interact through mutual feedback processes (von Bertalanffy, 1968). Changes to one subsystem directly or indirectly influence the other subsystems. Furthermore, the extant literature assumes that there is not one best way to organize but that not all ways are equally effective (equifinality).

However, complexity becomes an issue if—as is often the case—systems consist of many subsystems whose dependencies are nontrivial (e.g., they form feedback loops). von Bertalanffy defined a system as a set of elements standing in interrelations, which means that the behavior of an element is different depending on the relation to another element (von Bertalanffy, 1968, p. 55). Thus, the more subsystems we have, the more the entire system will have emergent properties increasing the system’s complexity level, see, e.g., Searle (2008, p. 69) for further details. Bunge (1979, p. 249) further argued that the more complex a system, the more difficult its assembly. Consequently, specific approaches should be applied to such complex, adaptive systems to support their analysis, planning, and steering (Holland, 2006). Furthermore, Ackoff and Emery (1972) argued that understanding the aims of systems should be done holistically by accounting for the different sociotechnical aspects of the system. This way, we can better understand the sociotechnical system’s purpose and the factors driving demand for it.

We aim to improve the organizing logic for complex DSR projects. From the general systems theory perspective, these projects are sociotechnical systems consisting of many subsystems (iterations, phases) with interdependencies being based, e.g., on path dependencies and/or feedback loops. It is thus fair to assume that these complex DSR projects have emergent properties that create challenges for their effective analysis, planning, and steering. To address these challenges, we cannot simply decompose them into local units or assume that they can be understood and/or managed in a linear way. Instead, we should apply findings from systems theory to analyze, plan, and steer them.

Aiming to understand the diversity of interdependencies within organizational systems and to provide a foundation for understanding and designing those systems, Mesarovic et al. (1970) developed the theory of hierarchical, multilevel systems. They defined hierarchy not as a simple structuring concept for complex systems but as a combination of three abstraction dimensions with different characteristics:

Layers decompose a system (or subsystem) into sub(sub)systems of different decision stages. Decomposing a system in layers can be achieved by aggregating elements that share similar effects on other subsystems. For example, in production planning, a start layer would be a plan that only comprises direct customer demands. Subsequent layers would also include indirect demands (derived according to a bill of materials); finally, the planning would proceed to plans comprised of production orders instead of customer orders (derived based on lot sizing, technical dependencies, etc.) (Winter, 1996). In the extant DSR methodology, the concept of layering has been implemented in the form of phases. Applied to complex DSR projects, a starting layer would be to understand the design problem. Subsequent layers would proceed, through requirements specification and solution design, until the final layers would deal with demonstration instantiations and applications. Hierarchical problem-solving usually starts with foundational layers (a few preconditions) and proceeds to consecutive layers, according to logical dependencies.

Strata decompose a system (or subsystem) into sub(sub)systems. This decomposition can be achieved by aggregating structural elements (and thus simplifying structure) or by aggregating dynamic elements (and thus simplifying dynamics). For example, in production planning, the top stratum would represent an enterprise-wide plan, with supply and demand aggregated to product types. Lower strata would represent plant-specific plans, with supply and demand on the product family level. The lowest strata would deal with workshop-specific plans, with supply and demand on the level of product items or even product variants (Winter, 1996). Hierarchical problem-solving normally starts with abstract strata and proceeds to more detailed strata. In the extant DSR methods, the concept of stratification has typically been implemented in the form of iterations in the DSR process. Consequently, applied to complex DSR projects, a start stratum would be the initial problem understanding and the initial solution idea, while later strata would provide more detail for both the problem understanding and solution design.

Echelons decompose a system (or subsystem) into sub(sub)systems of self-contained units. Such units are independent of layers and strata as they aggregate activities in an object-oriented way, whereas layers and strata focus solely on decision dependencies and object abstraction, respectively. For example, in production planning, organizations would first identify product types, product families, and product items based on their similarities with respect to their demand patterns and/or technical characteristics (“product program management”). Then, appropriate planning horizons for products and derived material demands would need to be identified (“production planning design”). Finally, a function for “long-range, enterprise-wide planning” would be defined on the corporate level, functions for “medium-range plant planning” would be defined for every plant, and a decentral function for “short-term production control” would be defined on the workshop level (Winter, 1996). All these echelon types combine certain decision sequence characteristics with certain object abstraction characteristics. When such a system design is implemented, the management/design echelons and the actual planning/control echelons would be executed concurrently, and their interdependencies would need to be managed by an overarching coordination function.

The extant DSR methods, such as the DSRM, organize DSR work according to layers—that is, structuring work based on activities building up toward a finite solution. Strata, in turn, are considered as iterations in the DSR process. Such organizing logic limits the ability to deal with complexity in DSR, since design knowledge can only be communicated once all DSR phases are completed after identifying the problem and motivation, defining the objectives, designing and developing, demonstrating, and evaluating.

The concept of design echelons offers the opportunity to decompose DSR work into smaller self-contained units that deliver design knowledge on the contributions of specific parts to a finite solution. Echelons can be, therefore, interpreted as self-contained “decision units” whose structure can deviate considerably from strata and layers (Abraham et al., 2014). Consequently, several design echelons can exist on a certain stratum or a certain layer representing an organizing logic of problem-solving, i.e., combining activities that should be combined to allow for efficient problem-solving for complex DSR projects.

To the best of our knowledge, the concept of design echelons has not been implemented in extant DSR methods. For complex DSR projects, it is surprising that the existing methodology only considers two distinct hierarchy dimensions but overlooks the third, integrative one. The general findings of complex systems theory should be usefully applicable to DSR as well. In this study we therefore set out to investigate how the concept of echelons should be implemented to support planning, conducting, and communicating complex DSR projects, propose complements to existing methods, demonstrate our proposal, and evaluate its utility.

## Research Design

The study was conducted over a period of eight years (2016- 2023). First, based on our problem understanding outlined in the Organizing DSR Projects section, we defined specific requirements and identified the Sonnenberg/vom Brocke model as a suitable solution candidate. It differentiates four types of intermediate design knowledge—an understood problem, a proposed design, an instantiated solution, and a solution in use—with two activities each to analyze/design and validate the result of the stage. We, therefore, refer to the Sonnenberg/vom Brocke model as the <sup>e</sup>DSR V1 model. To evaluate the model’s potential to address the two complexity challenges in DSR, we analyzed four studies applying the Sonnenberg/vom Brocke model (see the Demonstrating <sup>e</sup>DSR section). In addition, we conducted interviews with the lead authors of those studies (see the Evaluating <sup>e</sup>DSR section).

Second, based on the evaluation results of <sup>e</sup>DSR V1, we created an improved model, <sup>e</sup>DSR V2, comprised of five loosely coupled activity clusters that focus on a type of intermediate design knowledge: (1) problem analysis, (2) objectives and requirements definition, (3) design and development, (4) demonstration, and (5) evaluation. We tested the utility of this model in a field experiment with two cohorts of Ph.D. students (n = 30) in two different countries (see the Evaluating <sup>e</sup>DSR section).

Third, based on the <sup>e</sup>DSR V2 evaluation results, we further developed the conceptualization of the five activity clusters based on the echelon concept, resulting in <sup>e</sup>DSR V3. We evaluated and further refined <sup>e</sup>DSR V3 in two rounds with two senior DSR expert panels (n = 19), extending, in particular, the definition and role of the respective intermediate artifacts (see the Evaluating <sup>e</sup>DSR section), resulting in <sup>e</sup>DSR V4 and finally <sup>e</sup>DSR V5.

Fourth, we used a complex DSR project as an expository instantiation of the proposed <sup>e</sup>DSR methodology (see the Demonstrating <sup>e</sup>DSR section). Next, we present the resulting Version 5 of <sup>e</sup>DSR. We then provide further details on our activities in designing and evaluating <sup>e</sup>DSR in the various stages of our research process.

## The <sup>e</sup>DSR Model

The <sup>e</sup>DSR model was inspired by the idea that the problem understanding and formulation of research objectives require several nonlinear DSR iterations involving multiple stakeholders and research sites during the project. The model resembles the hierarchical nature of conducting a complex DSR project and thus provides complementary structuring support (in addition to DSR iterations and phases) to facilitate planning, conducting, and communicating design knowledge creation in complex DSR projects. Moreover, DSR can be understood as design knowledge accumulation processes with many iterations and backtracking and as chains of building blocks that combine phase-specific analysis/design and validation activities (see Table 1 for details).

As argued above, DSR strata are associated with iterations: During the process, the designer learns more about the problem, while the solution becomes more elaborate and useful (Winter & Albani, 2013). Layers, in turn, are associated with process phases: Starting with comparably few inputs (problem analysis), subsequent process phases become increasingly dependent on the results from preceding phases so that the overall process constitutes a meaningful chain of analytic, construction, and validation activities.

However, in addition to iterations and process phases that instantiate existing DSR guidance, we argue that there is a need for a complementary, echelon-based way of representing how a complex DSR project can be broken down into a system of selfcontained decision units. In DSR, a design echelon corresponds to self-contained analysis/design, and validation activities are integrated to create a meaningful intermediate artifact. The system theoretic concept of echelons justifies introducing this perspective into DSR methodology. Complementing the guidance provided by different DSR iterations (“strata”) and phases (“layers”), echelons are instrumental to understanding the logic of DSR decision-making and thus support planning, conducting, and communicating design knowledge contributions in complex DSR.

Furthermore, according to extant research on design knowledge accumulation and evolution (vom Brocke et al., 2020), design knowledge comprises both a solution specification and a problem specification. Most importantly, it includes goodness criteria regarding the extent to which the respective solution solves the respective problem. Considering this conceptualization of design knowledge, every echelon provides a partial contribution to such design knowledge in the form of an intermediate artifact: Problem analysis echelons provide the problem statement, thereby guiding the overall DSR project; objectives and requirements definition echelons provide the set of design objective(s) and requirement(s); design and development echelons provide projectable solution design; demonstration echelons provide solution characteristics, and evaluation echelons provide goodness criteria. These types of echelons are described below. In a focused DSR project, there is usually only one problem analysis echelon instance. At the same time, there may be a small number of objectives and requirements definition echelon instances, many design and development echelon instances, and even more demonstration and evaluation echelon instances. Altogether, the design echelons form a hierarchy of decision units, the organization logic of a complex DSR project.

## Problem Analysis Echelon

Regarding the problem analysis echelon, the intermediate artifact is a problem statement (Mullarkey & Hevner, 2019), which needs to be validated according to the degree to which the problem was solved previously as well as the solvability of the problem expressed in terms of a continuum and the degree to which it can be solved. The following techniques are recommended for accomplishing this: reviewing practitioner initiatives from the available industry and/or academic literature and conducting expert interviews, focus groups, and survey studies. These activities should yield a validated problem statement as a design knowledge output.

## Objectives and Requirements Definition Echelon

Regarding the objectives and requirements definition echelon, the intermediate artifact is the set of design objective(s) and requirement(s), as discussed in more detail, for example, by Maedche et al. (2019). These should be validated against the following criteria: applicability (to the research problem), coherence to avoid contradictions, completeness in stakeholder requirements, feasibility (including economic), and design operationality. Researchers should also evaluate how the design fits the validated problem statement to meet coherency criteria. This can be done using the following recommended techniques: logical reasoning of the design’s value, benchmarking the design against industry leaders or state-of-the-art examples, and conducting expert interviews and focus groups. The design knowledge output will be validated design objectives.

## Design and Development Echelon

Regarding the design and development echelon, the intermediate artifact is a projectable solution design in the form (for example) of a functional design and its architecture. These should be evaluated for their (1) applicability to instantiate the artifact, (2) internal consistency, (3) elegance and/or design feasibility, and (4) justification of the choice of design in terms of the level of detail, parsimony, soundness, and transparency. For coherency, the fit of the design to the validated design objectives should be considered. Assertion, benchmarking, conformity with proven pattern identification, design mockups, expert interviews, focus groups, logical reasoning, mathematical proofs, and simulations are recommended as techniques. The design knowledge output should be the validated artifact design.

## Demonstration Echelon

Regarding the demonstration echelon, the intermediate artifact is the instance of an artifact in an artificial or natural context. This should be assessed regarding the artifact’s ease of use, effectiveness, and robustness. How the instantiated artifact fits its validated design should be assessed for the proof of concept (PoC) (Nunamaker et al., 2015). The PoC demonstrates the functional feasibility of a potential solution and is defined as the degree to which a potential solution is technically possible and the extent to which its use is within the mental and physical abilities of its intended users or participants (Nunamaker et al., 2015). The following techniques can be used for this evaluation: demonstrations with prototypes; experiments with prototypes or systems; benchmarking; and surveys, expert interviews, or focus groups. The design knowledge output should be a validated instance of the artifact.

## Evaluation Echelon

Regarding the evaluation echelon, the intermediate artifact here is the contextualized artifact in use. Its value<sup>4</sup> should be evaluated against the following criteria: completeness of the design, external consistency, the efficacy of the artifact, and the generalization/projectability and utility of the results. How the use of the artifact fits its validated instance should be assessed for coherence. Case studies, field experiments, simulations, surveys, expert interviews, and focus groups are useful for conducting such evaluations. This should yield the artifact’s validated proof of value (PoV) as the design knowledge output, which can create value across various contexts, conditions, and generalizable solutions (Nunamaker et al., 2015).

Depending on the intent of the evaluation, both formative and summative valuation can be applied (Hamilton & Chervany, 2008; William & Black, 1996). While the formative evaluation aims to generate information to further develop an evaluand, the summative evaluation seeks to assess the qualities of an evaluand in context. In DSR, Sonnenberg & vom Brocke (2012) and Venable et al. (2016) have offered guidance on evaluation strategies that can be used to achieve valid PoV. Venable et al. (2016) defined formative and summative evaluation approaches as follows:

The formative approach is used “to produce empirically based interpretations that provide a basis for successful action in improving the characteristics or performance of the evaluand.”

The summative approach, in turn, is used “to produce empirically based interpretations that provide a basis for creating shared meanings about the evaluand in the face of different contexts.”

Table 1 above outlines specific validation criteria for each of the design/analysis and validation activities (i.e., the five design echelon types) and possible techniques that can be used to validate design knowledge outputs. The intermediate artifacts are also recognized alongside the design knowledge outputs.

## The <sup>e</sup>DSR Metamodel

The metamodel of the proposed <sup>e</sup>DSR methodology is summarized in Figure 1. Every echelon type is associated with a specific type of intermediate design artifact. Centered around that phase of design knowledge creation is a cluster of phase-specific analysis/design and related validation activities. We differentiate between intra-echelon and interechelon validation criteria. By iterating the design and validation of an echelon until all validation criteria are met, only valid analysis/design knowledge is created, and potential issues are detected and corrected as early as possible (Abraham et al., 2014).

## Demonstrating <sup>e</sup>DSR

The following section demonstrates the <sup>e</sup>DSR methodology by first describing recent DSR studies that apply an early version of the echelonized model (the Sonnenberg/vom Brocke model) to structure a DSR project and then depicting a case that purposefully applies the final <sup>e</sup>DSR methodology. This approach showcases the emergent properties of a DSR project and how multiple echelons emerge, and how they interact.

The DSR studies selected for the first part applied the Sonnenberg/vom Brocke model outlined in their 2012 publication, which already depicted a nascent form of our echelon concept. Interestingly, Stöckli et al. (2017) reported 69 citations of the original Sonnenberg/vom Brocke model in the five years after it was first published. However, of these 69 referencing studies, only 26 (see Appendix A) applied the model; the others only mentioned it or compared it with other proposals (Stöckli et al., 2017). Of these 26 applications, only six used all the evaluative activities in a formative manner; the others presented their evaluation results according to the model but did not intertwine design and validation. For demonstration purposes, four cases that applied theoretical sampling have been selected for this study to ensure diversity, one of which<sup>5</sup> is presented in more detail in the following.

## Demonstrating the Use of Intermediate Artifact Validations

The authors of several studies addressed the problem of data integration between process management and accounting IS (Sonnenberg & vom Brocke, 2012; vom Brocke et al., 2009; vom Brocke et al., 2010; vom Brocke et al., 2011; vom Brocke et al., 2014) to account for the economic implications of state changes in process design time and run time. In these studies, design science was applied to develop a “process accounting model” (PAM), linking the essential concepts of accounting and process management.

<table><tr><td>Design echelon type</td><td>Intermediate artifact</td><td>Validation criteria</td><td>Validation techniques</td><td>Design knowledge</td></tr><tr><td>Problem analysis</td><td>Problem statement</td><td>Degree to which the problem has been solvedSolvability (continuum, degree)</td><td>Literature reviewReview practitioner initiativesExpert interviewFocus groupSurveys</td><td>Validated problem statement</td></tr><tr><td>Objectives and requirements definition</td><td>Design requirements</td><td>Fit to the validated problem statement (coherency)Applicability (to the problem)Coherence (no contradictions)Completeness (per stakeholder requirements)Feasibility (economic)Operationality</td><td>Logical reasoningBenchmarkingExpert interviewFocus group</td><td>Validated design objectives</td></tr><tr><td>Design and development</td><td>Projectable design for functionality and its architecture</td><td>Fit to the validated design objectives (coherency)Applicability (to instantiate the artifact)Consistency (internal)Elegance (of design)Feasibility (of design)Justification of design choice rationale (level of detail, parsimony, soundness, transparency)</td><td>AssertionBenchmarkingConformity with proven identification of patternsDesign mock-upExpert interviewFocus groupLogical reasoningMathematical proofSimulation</td><td>Validated design of the artifact</td></tr><tr><td>Demonstration</td><td>Instance of artifact (in artificial or natural context)</td><td>Fit to the validated design of the artifact (coherency)Ease of use (of the artifact)Effectiveness (of the artifact)Efficiency (of the artifact)Robustness (of the artifact)</td><td>Demonstration with prototypeExperiment with prototypeExperiment with systemBenchmarkingSurveysExpert interviewFocus group</td><td>Validated PoC of the instantiated artifact</td></tr><tr><td>Evaluation</td><td>Contextualized artifact in use</td><td>Fit to the validated instance of the artifact (coherency)Completeness (of design)Consistency (external)Efficacy (of the artifact)Generalization (of results)Projectability (of results)Utility (of the artifact)</td><td>Case studyField experimentSimulationSurveyExpert interviewFocus group</td><td>Validated PoV of the artifact</td></tr></table>

![](/api/attachments/M9TMFDUY/fulltext/images/ad3ef18d3ee13855b409b62b9e1c78843abf186bd402f456a8f25b4f8d459acf.jpg)

The authors observed the problem’s industry interactions, in which partners reported struggling from a lack of integration in both accounting and process management because (1) decisions in process management could not be evaluated according to economic consequences, and (2) information produced by accounting did not refer to process-related concepts subject to management. Consequently, information quality was reportedly poor, and costs to overcome the gap were high. The literature review for this study aimed to validate the problem and evaluate its novelty and solvability (Sonnenberg et al., 2012; vom Brocke et al., 2011). Consequently, the lack of data integration between accounting and process management IS was formulated as the validated problem statement.

When addressing the problem statement, a specific objective was to determine a design for a data model to integrate and structure accounting and process data that supported the design, execution, and control of business processes. The objective’s economic feasibility and contribution to solving the identified problem had to be assessed. As a validation technique, the researchers used expert interviews (n = 4) to investigate how such data models should be developed. This was supported by logical reasoning and drew from existing integration examples using process management and accounting methods (e.g., Thomas & vom Brocke, 2010; vom Brocke et al., 2010). The output was the specification of validated design objectives using technical specifications (Sonnenberg & vom Brocke, 2011), which were still specific to the selected example methods.

In the design phase, the researchers generalized their findings through logical reasoning toward a data model, independent of specific methods both in process management and accounting, which served as a design mock-up. Multiple versions of the model were developed and discussed with experts (n = 22) from both industry and academia regarding the applicability, feasibility, and internal consistency. During the design process, design principles were identified and incorporated into the PAM— specifically, the principles of event-data disaggregation, event classification, process relatedness, and economic reciprocity. The PAM was specified through a set of metamodels, which served as validated design specifications.

The PAM was used to develop several prototypes, such as double-entry bookkeeping (including account postings in a purchasing transaction), to demonstrate that accounting operations based on the model work effectively. The prototypes also used sensing of economic reciprocity in business process structures to demonstrate the effectiveness of process evaluations based on the model (Sonnenberg & vom Brocke, 2014).

The subsequent evaluation was carried out using demonstrations with the prototypes regarding specific aspects of the PAM design. For instance, the researchers developed an ontology for aligning IT infrastructure capacity with business needs, applying PAM’s event data disaggregation and event classification principle (vom Brocke et al., 2014). The application took place at the Hilti Corporation, an international manufacturing company, and interviews with users demonstrated the perceived usefulness of the artifact in assessing the economic consequences of IT infrastructure and process decisions (n = 6). Expert interviews were carried out to evaluate the perceived utility of the ontology. To date, a full evaluation of PAM’s principles and design aspects has yet to be reported.

## Demonstrating the Emergent Properties of Multiple Design Echelons

Based on hierarchical systems theory, we have argued that organizing DSR projects according to phases (“layers”) and iterations (“strata”) brings limitations when dealing with emergent properties of DSR projects. To substantiate this argumentation further, in this section, we present a complex, multi-year, and multi-publication DSR project (Weiss et al., 2013; Winter, 2016; Schilling et al., 2019). During the project, 16 echelons emerged that instantiate the five proposed design echelon types (see Figure 2):

One overarching “analyzing overall research problem” echelon of the problem analysis type:

• A sequence of two “deriving design objectives” echelons of the objectives and requirements definition type

• A journey of four design and re-design echelons of the design and development type

• Four demonstration echelons of the demonstration type

• Five evaluation echelons (including one sequence of two echelons) of the evaluation type

In Figure 2, the broken green arrows denote the logical flow of echelons, while yellow dotted arrows denote learning journeys within an echelon type.

## Problem Analysis Echelon

The overarching problem addressed by the research used as an example in Figure 2 is the limited ability of large, decentrally organized companies to achieve company-wide, long-term “global” benefits (e.g., leverage synergies by sharing software solutions, limit the complexity of IT application landscape) because local decision makers focus instead on project-, unit-, or function-specific short-term “local” benefits (Brosius et al., 2019). One symptom of this overarching problem is that enterprise-wide coordination approaches, such as enterprise architecture management, appear to have reached impact limitations due to the lack of institutionalization by most local decision makers (Ross & Quaadgras, 2012). The limited impact of coordination interventions can be explained by local decision makers’ perceived social legitimacy, efficiency, organizational grounding, and trust in the interventions (Weiss et al., 2013). Thus, an effective design solution would include design principles for coordination interventions that effectively improve local decision makers’ perception of the legitimacy, efficiency, organizational grounding, and/or perceived trustworthiness of the interventions (Winter, 2022).

## Objectives and Requirements Definition Echelon

As the empirically grounded design objectives are quite distinct, the research we use as an example found that solution design should first focus on a certain objective, such as better demonstrating the intervention efficiency or improving the social legitimacy of enterprise-wide coordination. By testing the effectiveness of different novel interventions, it should be possible to generalize effective intervention design to design principles (that link generalized design requirements to generalized design features).

## Design and Development Echelon

For every proposed set of design requirements, the analysis of extant research as well as the state of practice would result in distinct sets of solution components that would then be integrated and tailored to the problem at hand. For example, to demonstrate coordination efficiency (“What’s in it for me?”), either the cost-calculation and charging of technical debt to noncompliant change projects or the provision of cost-reduction project support (e.g., by supporting architects or reduced costs of shared software solutions) could be used as foundations (Aier et al., 2015). A possible foundation for improving the social legitimacy of enterprise-wide coordination (“Why should I comply?”) could be communication measures (e.g., showcasing successful solution sharing, see Schilling et al., 2018) or engineered social pressure (e.g., by making noncompliant projects transparent across the organization—see Winter, 2016). At a later stage, the generalization of effective design features and design requirements makes it possible to formulate design principles (Winter, 2022).

![](/api/attachments/M9TMFDUY/fulltext/images/a70cb1f0b399a035c14da34dab6a54dca2d293ccb3c6581f6cefb4cc421270a7.jpg)  
Figure 2. Depiction of Echelon Instances of Five Design Echelon Types Emerging During a Project

## Demonstration Echelon (PoC)

All the above-mentioned solution strategies must be contextualized to demonstrate their potential to solve the design problem. For example, to demonstrate the ability of social interventions to increase the compliance of decentralized decisions in change projects effectively, labels need to be developed together with the case organization to guarantee understanding and acceptance. Such labels make transparent which projects (or business units) are more or less compliant and thus create or decrease technical debt for the entire organization (Schilling et al., 2019). An alternative PoC for this projectable design is to create “relation manager guilds,” where know-yourcustomer data quality issues can be discussed, and a common sense of regulatory compliance can be institutionalized.

## Evaluation Echelon (PoV)

Finally, promising concepts need to be applied with real people who have real stakes in the outcomes (Nunamaker et al., 2015). In the project used as an example, two companies were involved in field tests (in different business units) (Schilling et al., 2019) as well as in a pilot study (Cahenzli, 2020), respectively.

## Demonstrating the Organizing Logic of <sup>e</sup>DSR

Does the proposed echelon model support planning, organizing, conducting, and communicating complex DSR projects—or is it a complication? After demonstrating the “informal coordination interventions” project using the <sup>e</sup>DSR model, Figures 3 and 4 illustrate how the project would have looked if it had been structured using the DSR process model or the DSR iteration model.

If we collapse the (horizontal) DSR iteration dimension (Figure 3), we are left with the DSRM process structure model, which corresponds with the “strata” concept of hierarchical, multilevel systems theory. If we collapse the (vertical) DSR process phase model dimension (Figure 4), we yield an instantiation of the iterative structure model of the DSRM, which, in turn, corresponds with the layer concept of hierarchical, multilevel systems theory. This demonstration makes it clear how the echelon concept advances traditional process- or iteration-oriented structuring approaches—combining them and adding additional “learning journey” semantics.

![](/api/attachments/M9TMFDUY/fulltext/images/ee38bb18115217745efdd0050ad33ea5462fd112fde577489105eb26f54e5f41.jpg)

Figure 3. DSR Project Depicted by “Strata” of Hierarchical, Multilevel Systems Theory with Collapsed Microlevel Iterations

![](/api/attachments/M9TMFDUY/fulltext/images/da1ad8809cb98c08e38145da271a7d3eb788558de0bb975b067e1161e8af0d3e.jpg)

Figure 4. DSR Project Depicted by “Layers” of Hierarchical, Multilevel Systems Theory with Collapsed Processes

The effort required to deal with a third structuring dimension is outweighed by improved clarity and expressiveness, particularly for complex, multi-publication, and multi-artifact projects. Beyond the organizing logic that helped to coordinate research collaborators and “keep track” in this complex project, the echelon-specific focus on certain intermediate artifacts served as effective communication guidance.

## Evaluating <sup>e</sup>DSR

Based on the argument and summary presented in Table 1, the primary criteria for evaluating <sup>e</sup>DSR’s value can be described as follows:

1. Coherency: the fit between <sup>e</sup>DSR and how the evaluation is performed in the studies

2. Completeness: the extent to which <sup>e</sup>DSR components are instantiated in the studies

3. External consistency: the extent to which research follows the <sup>e</sup>DSR research process

4. Efficacy: the extent to which <sup>e</sup>DSR facilitates better results

5. Generalization/projectability: the extent to which the studies provide insights about the general value of the <sup>e</sup>DSR proposal

6. Utility: the extent to which <sup>e</sup>DSR is instrumental to the studies in an efficient, effective, and/or innovative way

Suppose the presented criteria are consolidated and related to researcher-driven DSR projects (e.g., where motivation and ownership can be assumed). In that case, the application of <sup>e</sup>DSR should improve the following process-, outcome-, and progress-related performance indicators of DSR projects:

• Process-related efficacy:

o Improved ability to plan, structure, control, and adapt the project

o Improved ability to deliver on time, on budget, and within the project scope

• Outcome-related efficacy:

o Improved support for answering the research question(s)

o Faster and more detailed feedback and increased ability to manage mistakes

• Contribution-related efficacy:

o External consistency of the research process

o Improved projectability of results

o Improved utility for practice and/or for the research community

We conducted a three-phased validation of the PoV using 1) formative and 2) summative evaluation approaches (Venable et al., 2016). First, using a formative approach, we interviewed the authors of the selected DSR studies, after which we conducted a field experiment with doctoral students in two European countries. Second, we held four expert panels with renowned design science researchers from the Americas, Europe, Asia, and the Pacific region using a summative approach. In the following section, we report the results of these activities.

## Author Interviews

For each of the four DSR studies<sup>6</sup> included in the first part of the demonstration section, an author was interviewed for 30 to 45 minutes over the phone. Prior to the interviews, the authors were provided with the list of DSR project performance indicators mentioned above. These interviews allowed for observing the utility claims of evaluations (regarding the above performance indicators) and obtaining insights to refine the proposed extended DSR organizing logic (described previously). Table 2 summarizes the learning, perceived utility, and overall efficiency of the evaluations. The structure of the interviews can be found in Appendix B.

One author of the Niemöller et al. (2014) article saw the most significant gains from closing the conceptual gap between the DSR project’s diverse stakeholders (industry clients and researchers). This was even more important in other DSR projects (e.g., in healthcare with nurses as artifact users), forcing the authors to specify use cases early, which improved consistency. Using simple techniques like mock-ups proved instrumental for keeping the outcomes applicable and straightforward. This was beneficial in terms of the evaluation approach. The developed techniques could be applied to other DSR projects (e.g., healthcare or supply chain management, even with five or six iterations). Overall, the author concluded that the extra effort for multiple validations was outweighed by the improved communication among stakeholders.

<table><tr><td colspan="4">Table 2. Author Interview Results</td></tr><tr><td>Case/criteria</td><td>Process-related efficacy</td><td>Outcome-related efficacy</td><td>Contributions to external consistency, projectability, and utility</td></tr><tr><td>Niemöller et al.(2014)</td><td>Collaboration supported by always having a process-wide framework for positioning current activities and outcomes</td><td>Enforcing a discourse about deciding on a specific artifact type in an early phase of the DSR process</td><td>Overall quality is much higher than the required additional effort</td></tr><tr><td>Sonnenberg &amp; vom Brocke(2014)</td><td>Effective support for guiding a multi-year DSR study “journey”</td><td>Improved ability to formulate fine-granular research questions, leading to specific DSR subprojects that contributed to the overall studyAllowing incremental improvements to the superordinate research question and research design (e.g., focusing on the interface model instead of the overarching model</td><td>Avoiding overengineering (getting “lost in design”) in the early stages of the DSR projectCreating intermediate results in subprojects early to better facilitate generalizationAdditional effort outweighed by steering and result improvements</td></tr><tr><td>Blaschke et al.(2017)</td><td>Closing the conceptual gap between diverse stakeholders</td><td>Mock-up was instrumental in keeping outcomes simple and applicable</td><td>Forced to specify use cases early, thereby improving consistencyApproaches and techniques can be applied in other DSR projectsExtra effort for multiple validations outweighed by improved communication with stakeholders</td></tr><tr><td>Lück &amp; Leyh(2017)</td><td>Significant DSR guidance, especially for inexperienced researchersHelpful for project planning and stakeholder integration</td><td>Obtain feedback early and avoid research pitfallsMultiple validations forced the structure of the project, connections to experts, and creation of intermediate results</td><td>Systematic creation of intermediate resultsMultiple validations helped prioritize alternative use cases and focus the evaluation efforts</td></tr></table>

An author of the paper on the data integration between process management and accounting (Sonnenberg & vom Brocke, 2012) reported that the study was the result of a long effort (eight years) that started with a broad vision, branched into a sequence of detailed substudies with specific artifact designs, and concluded with a projectable artifact. During the process, the authors mitigated the typical danger of being “carried away by design” and losing focus by applying a multiple validations concept. This strategy also facilitated discussion and created opportunities for the intermediate results to be published, thereby increasing the success of what would be a long-term effort (known as a “design sprint”). This also meant that the created design knowledge contributed to a better understanding of the general problem and directed the project overall—not only by improving the design but also by informing more appropriate objectives and specific research questions.

Similarly, an author from the Blaschke et al. (2017) article indicated that the biggest benefit from multiple validations is collaboration support through a process-wide framework for positioning current activities and outcomes used as a boundary object (1) within a diverse team of co-authors and (2) between the author team and focus groups or experts. In addition to helping the authors structure the discussion, this information also proved useful in presenting and discussing the results and tasks with other researchers. Another significant benefit was that the approach facilitated discourse with regard to deciding how to decide on a specific artifact type (design principle vs. method vs. tool) during an early process phase. This was very beneficial in early discussions with stakeholders representing diverse topics of interest. Overall, the gains in process, outcome, and contribution quality were higher than the additional effort required. This may have been due to the heterogeneity of the research team and the researcher-practitioner gap observed in this project and its context.

Finally, an author of the Lück and Leyh (2017) article reported that one of the most significant benefits was avoiding unpromising research paths by obtaining feedback at an early stage. Specifically, the author singled out the validation of the research problem as having been particularly helpful. Multiple validations also helped to prioritize alternatives (use cases) and focus evaluation efforts, which forced the authors to structure the project’s research process, connect with experts, and create intermediate artifacts and results. The author reported that this provided significant DSR guidance, especially for inexperienced researchers on the DSR team. The author also observed that the systematic creation of intermediate artifacts and results aided project planning and stakeholder integration and created publication opportunities.

## Doctoral Student Experiment

In 2019, we conducted a field experiment in two European countries to further validate the efficacy of the initial version of <sup>e</sup>DSR (see Table 1 for the description of the <sup>e</sup>DSR versions). The experiment was undertaken with doctoral students from several European countries who were taking a post-graduate course on how to plan a DSR project. Our objective was to apply <sup>e</sup>DSR to treatment groups of students at both locations and then take a more hands-off approach with the control groups, enabling the students to choose their way of planning a DSR project. The experiment was designed to explore the extent to which applying <sup>e</sup>DSR impacts the efficacy of DSR. For process-related efficacy, we assessed students’ ability (1) to plan and structure a DSR project and (2) to deliver it on time and within the project scope. For the outcome-related efficacy, we assessed (3) students’ ability to find support in answering the research question(s) and (4) whether faster and more detailed feedback provided to the treatment group increased their ability to manage mistakes.

Regarding contribution-related efficacy, we assessed (5) the consistency between problem understanding and solution design and (6) whether the treatment group was able to propose more projectable designs. We controlled the experiment by giving all the students the same teaching case to develop their research plan, understand the design problem, and propose a design solution. The selected case depicted the problem of designing crowdsourcing systems to increase information quality and user participation (Lukyanenko & Parsons, 2020). The students (n = 30) at both locations were randomly assigned to either treatment or control groups, with the target of even distribution. At Location 1, there were eight students in the control group and seven in the treatment group. At Location 2, there were nine students in the treatment group and six in the control group.

We assigned several independent assessors (who were not involved in the project) at both locations to assess the presentations, which were each evaluated by two or three assessors. All the assessors had very good knowledge of conducting DSR, and all had at least a doctoral degree in IS. The assessors did not know which group the students were assigned to. They were given a scripted evaluation form (see Appendix C) to help with the assessments. The assessors’ specific tasks were to appraise how the students were able to (1) analyze the design problem (Task 1), (2) sketch a problem solution (Task 2), and (3) plan how to demonstrate and/or evaluate their design (Task 3). Finally, the assessors were asked to grade the overall performance of the students addressing the previously mentioned tasks (Overall).

Table 3 presents the average student evaluation for each task per location. We also provide t-test results for the given tasks between locations. We chose to perform one-sided t-tests with the assumption of homoscedastic variances. This decision was based on the assumption that there were no differences between the abilities of the students to perform the tasks and reflected our interest in investigating the direction of student performance (we queried whether the students in one group performed better than those in the other). The results clearly show that the treatment group performed better on the assigned tasks at both locations. Both treatment groups outperformed the control groups on each of the tasks. Most importantly, the overall performances between the treatment and control groups were significantly different. For Location 1, the overall averages were 72.96 for the treatment group and 56.05 for the control group (t-test result: 0.003), while the corresponding numbers for Location 2 were 65.83 and 50.00, respectively (t-test result: 0.028).

<table><tr><td colspan="11">Table 3. Experiment Results</td></tr><tr><td rowspan="2">Average result/location</td><td colspan="4">Treatment group</td><td colspan="4">Control group</td><td colspan="2"></td></tr><tr><td>Task 1</td><td>Task 2</td><td>Task 3</td><td>Overall</td><td>Task 1</td><td>Task 2</td><td>Task 3</td><td>Overall</td><td>T-test overall</td><td>T-test Task 3</td></tr><tr><td>1</td><td>78.53</td><td>68.53</td><td>70.29</td><td>72.96</td><td>67.25</td><td>49.75</td><td>52.50</td><td>56.05</td><td>0.003**</td><td>0.012*</td></tr><tr><td>2</td><td>74.17</td><td>64.72</td><td>56.11</td><td>65.83</td><td>62.50</td><td>49.58</td><td>35.42</td><td>50.00</td><td>0.028*</td><td>0.030*</td></tr><tr><td>T-test between locations</td><td>0.207</td><td>0.298</td><td>0.064</td><td>0.120</td><td>0.277</td><td>0.471</td><td>0.028*</td><td>0.207</td><td></td><td></td></tr></table>

Note: \* 0.05 significance level (one-sided t-test, assuming homoscedastic variances); \*\* 0.001 significance level (one-sided t-test)

With Task 3 (plan how to demonstrate and/or evaluate your design), we can see a notable difference between student results for both the treatment and control groups. Looking at the average results for Task 3, there is a clear difference between the locations for the control groups (average of 52.50 vs. 35.42). The t-test result is also statistically significant $( p = 0 . 0 2 8 )$ . After inspecting the results more carefully and going through the teaching notes for the course at Location 2, we noticed that one student received no marks from either of the assessors. This student presented his doctoral research proposal, resulting in no marks. In the treatment group, we saw a similar result for Task 3 (the average scores were 72.96 and 65.83), although the t-test result was below statistical significance (p = 0.064).

In conclusion, the performance of the treatment groups provides evidence that the application of <sup>e</sup>DSR improved students’ ability to plan and structure a DSR project. Similarly, the overall performance of the treatment groups versus control groups indicates that the application of <sup>e</sup>DSR contributes to the ability to deliver a DSR project plan on time and within the project scope. Regarding outcome-related efficacy, we argue that using <sup>e</sup>DSR can provide improved support for answering the research question(s) (Tasks 1 and 2 specifically). It allows for quick and detailed feedback, which increased students’ ability to manage mistakes. Regarding contribution-related efficacy, the students performance (especially with Tasks 1 and 2) indicates that those in the treatment groups obtained better consistency between problem understanding and solution design than those in the control groups. Finally, the overall performance of the treatment groups shows they were better able to propose more projectable designs than the other students.

However, the results for planning how to demonstrate and/or evaluate a design (Task 3) were more mixed. At Location 1, the application of <sup>e</sup>DSR led to better results in the treatment group: the average results were 70.3 and 52.2 (p = 0.012). At Location 2, the results were nearly as good considering the smaller sample: the average results were 56.1 versus 35.4 (p = 0.030). However, the students at Location 2 did not perform as well on Task 3 as those at Location 1. While the results are not directly comparable due to having a different set of assessors at each location, they indicate that the students at Location 1 experienced some challenges in fully meeting the course expectations about providing plans for demonstrating and/or evaluating their designs.

## Expert Panels

We organized four online expert panels to further validate the PoV for the <sup>e</sup>DSR approach. The panel design included a sample<sup>7</sup> of experienced design science researchers that was diverse in terms of age, region, and gender. The approximate run time for the panels was 1.5 hours, with four or five participants each and three moderators. The sessions were held on the Zoom video communications platform (zoom.us) and recorded (with participants’ permission). The two rounds of panels (n = 11 and n = 8) were first provided with a short presentation of a version of the <sup>e</sup>DSR concept (see Tables 1 and 4 for details) and then some guiding questions to elicit feedback, which are listed below.

Recognizing differences between <sup>e</sup>DSR and the legacy DSR methodologies:

• How is this any different?

• How do you like this (general thinking)?

• Would you feel comfortable applying this?

## Recognizing the impact on planning and running a DSR project:

• How would this impact your ability to plan and/or structure a DSR project?

• How would this impact your ability to control and/or adapt a DSR project?

How would this impact your ability to deliver a DSR project on time and/or on budget and/or within the project scope?

• How would this impact your ability to find support in answering the research question(s)?

• How would this impact your ability to gain feedback and manage mistakes?

## How would this impact the outcomes of a DSR project?

• How would this impact the external consistency of the research process?

• How would this impact the projectability of results?

• How would this impact the utility of the results for practice and/or the research community?

## Future research:

What is still needed to make this fly? How could this be improved?

• What would be interesting to investigate further?

The feedback on the iterative nature of <sup>e</sup>DSR resulted in a new cyclic presentation of the approach. The cyclic representation also led us to discuss how <sup>e</sup>DSR can be used in multiple instances of the DSR cycle and how these multiple cycles impact the overall design process. This motivated us to consider echelons as pathways, as described in Figure 2. Finally, both pieces of feedback detailed above enabled us to reflect on the design knowledge accumulation and theory development, which was later depicted in the <sup>e</sup>DSR metamodel (Figure 1).

Table 4 summarizes the key findings from the panels. With each panel session, the presentation of <sup>e</sup>DSR was adopted incrementally. Due to space limitations, we do not include all four resulting iterations of <sup>e</sup>DSR but instead summarize the key feedback in Table 4. The main themes that emerged were the iterative nature of <sup>e</sup>DSR, echelons as pathways, and how design knowledge accumulates and supports theory development.

![](/api/attachments/M9TMFDUY/fulltext/images/e6ecdadb5cf9b95378a315906e5bbce3fc204855e69222d17846072793092c41.jpg)

<table><tr><td>Echelons as pathways</td><td>Is the problem statement still valid after a cycle? What would be a good research question for an echelon (or two), especially for a novice researcher?You set the criteria first, then do it. Did I have the right criteria?Are there patterns here?I would encourage framing this so that it has different pathways to apply it. Can the echelons be less strictly tied to the steps? You could move from having a demonstration echelon to design and then see how to think of problems, etc.</td><td>The panelists provided numerous comments and questions regarding how eDSR can be used in multiple instances of the DSR cycle and how these multiple cycles impact the overall design process.<img src="/api/attachments/M9TMFDUY/fulltext/images/0553fb7c545b2de5da214762a1fbc71b5a926e1eac3df15780f9bbf18a5c07a0.jpg"/>We attempt to summarize this in the figure above. This example represents how a DSR project moves through different echelons in several cycles. It also depicts how it sometimes makes sense not to follow the nominal DSRM process but to skip certain phases. Consequently, this research process also impacts, for example, the validation criteria or research problem statement as the project goes forward.</td></tr><tr><td>Design knowledge accumulation and theory development</td><td>Make the contribution to knowledge clear (what is the DSR bit?).Design knowledge cumulation is not explicit in the model now.Every step of DSR projects contributes to knowledge.Echelons are building blocks of a research paper. Having standardized outcomes of DSR could make it closer to design practice, like design thinking.</td><td>In our initial eDSR presentation (cf. this table&#x27;s section &quot;Iterative nature of the eDSR process&quot;), we did not explicitly address how design knowledge accumulates and how this impacts theory development.This led us to consider the matter and development of Figure 2 more carefully. This characterizes how we see that echelons are accumulating design knowledge, which consequently supports design theory development, e.g., movement from problem diagnosis via solution ideas toward complete design knowledge that combines problem analysis, solution design, and evaluative evidence (vom Brocke et al., 2020).<img src="/api/attachments/M9TMFDUY/fulltext/images/62c83dfadad3e8a56b0a3eb67753ae886b4bd5db7bc87a8482723cbd87f610b1.jpg"/></td></tr></table>

## Implications and Limitations

This paper proposes a new organizing logic for complex DSR projects. Instead of following the sequential thinking— structuring work according to a series of activities building up to a finite solution—we propose decomposing the design process into a hierarchy of decision units (“design echelons”), units that are loosely coupled yet related and self-contained. In so doing, we hope each such unit makes a distinct contribution to design knowledge—each in a different way. Our approach is grounded in hierarchical systems theory (Mesarovic et al., 1970), based on which we define design echelons. Thus, we refer to the approach as <sup>e</sup>DSR.

Our evaluative evidence supports the claim that the <sup>e</sup>DSR methodology advances the planning, conducting, and communicating of DSR more efficiently when dealing with complexity. Additionally, it demonstrates that intermediate artifacts can also be developed collectively, allowing for a division of labor approach and fostering the accumulation and evolution of design knowledge within a team of researchers and the entire DSR community. Specifically, the echelonoriented organizing logic in DSR provides a new way to deal with complexity in DSR, especially regarding challenges related to understanding the problem and formulating research objectives for iterative and nonlinear DSR projects that involve multiple stakeholders and research sites. Against this backdrop, the paper makes several important contributions, which we discuss in the following. We then outline the limitations that we have identified in the study.

First, the focus on the development and evaluation of echelons allows for early feedback on specific aspects of design. Compared to widely adapted process models in DSR (Peffers et al., 2007), echelons form smaller yet self-contained, meaningful units of work that focus on specific aspects of design, such as understanding the problem, analyzing objectives, specifying requirements, designing a candidate solution, demonstrating the design, and ultimately applying the designed solution to prove its utility. Hence, <sup>e</sup>DSR supports the idea of the design and evaluation of intermediate artifacts (Sonnenberg & vom Brocke, 2012). Using <sup>e</sup>DSR, the design and validation results (i.e., the intermediate artifacts, see Table 2) would be available comparably earlier in the process of crafting complex artifacts and would also be more specific in terms of the contribution an echelon makes, such as understanding a problem or drafting a solution. This could later result in the development of theories for problems or solutions (see Majchrzak et al., 2016). Therefore, validation results could inform the design (and further design) of solutions, which could be reported separately (e.g., in conference proceedings or journals). Thus, the echelon-based communication of intermediate results could enable more efficient reporting of DSR outputs and support an increased level of rigor for complete DSR projects, analogous to the way in which article/essay-based dissertations are composed and reported.

Second, from the perspective of an individual researcher or a team of researchers, the opportunity to focus on echelons (instead of entire end-to-end DSR processes) lowers the burden of making contributions to design knowledge. In a recent editorial, Peffers et al. (2018) observed (critically) that many DSR papers have been rejected for not correctly going through all the DSRM phases or not evaluating the artifact in the ways reviewers expect. With the echelon-oriented approach, single articles would not expected to cover all phases mentioned in the DSRM for a complex DSR project. Instead, papers could focus on selected design aspects, making it possible to elaborate on learnings made during iterations and interactions. Each researcher would be able to make contributions more quickly, and more individuals could be encouraged to contribute, which would arguably have a positive effect on the productivity of the field. Thus, the approach enables researchers to specialize in the aspects of design they find most interesting or those they feel most capable of contributing to. Some may focus on identifying, analyzing, and describing problems, while others may choose problems and propose alternative solution designs. Hence, the loose coupling of the echelons in <sup>e</sup>DSR supports the division of labor and may thus foster specialization in DSR. Research has shown that specialization positively impacts the economics of processes, specifically regarding time and quality (Dumas et al., 2018).

Third, by organizing work in DSR around echelons, it would also be possible to foster communication and knowledge exchange in DSR, thereby contributing positively to the accumulation and evolution of design knowledge. In the DSRM model (Peffers et al., 2007), communication takes place only at the end of the entire design process, that is, after all phases (the identification of the problem, the specification of the objective, the design of a solution, and its demonstration and evaluation) have been completed. Many design projects do not even get to the end of this process (Peffers et al., 2018), which often takes multiple years to complete (Venable et al., 2019). <sup>e</sup>DSR makes it possible to communicate the intermediate results of a DSR project, i.e., the respective results of DSR iterations consisting of the problem analysis, objectives and requirements definitions, design and development, the results of a demonstration, and the results of an evaluation. <sup>e</sup>DSR also makes it possible to compare the results of different strata during a DSR project. This would be interesting, for example, for a project applying the same artifact in different research contexts. A practical example of this would be using a requirements acquisition method (see Tuunanen & Peffers, 2018) in various industry settings and organizations. This, in turn, should result in a better understanding of the research problem and enhance design knowledge accumulation and the development of more mature design theories (see Gregor & Hevner, 2013).

Fourth, the <sup>e</sup>DSR approach provides early and concurrent feedback on design decisions, enabling the DSR process to be more responsive to change. Research on the role of evaluation in DSR has argued for making greater provisions for more fine-grained and concurrent assessment (Sonnenberg & vom Brocke, 2012), and the FEDS model, for instance, considers multiple formative episodes of design and evaluation both in artificial and naturalistic settings (Venable et al., 2016). Decomposing the overall DSR project into smaller logical parts, which could be developed and evaluated independently, would allow evaluation results to be obtained earlier. They could also be achieved more specifically in relation to the precise intermediate contributions of the respective echelon. Both the temporal and factual aspects of <sup>e</sup>DSR would enable DSR processes to be more responsive to change. Apart from dealing with changes in the environment of a DSR project, <sup>e</sup>DSR also accounts for the inherent change of DSR within DSR processes. Such change is important, given the novelty of the design knowledge created and the limited possibilities of planning design processes in advance.

While we consider <sup>e</sup>DSR to be applicable to various DSR projects, we also recognize that it may not be ideal for all DSR projects. Strong et al. (2020) highlighted the emergent nature of DSR processes. Furthermore, the DSR process can hardly be planned. Rather, it evolves during design, recognizing constraints and opportunities (Hevner et al., 2021; vom Brocke et al., 2021). How then should one decide when it would be appropriate to consider using <sup>e</sup>DSR? We suggest using the two following heuristics:

The problem understanding and respective design are likely to be emergent due to stakeholder diversity, evolving situational conditions, a multitude of aspects in analysis and design, and/or sparse descriptive knowledge usable for design.

The intended projectability of the artifact is high; thus, diverse use situations are needed for demonstration/evaluation activities, and/or the artifact requires several nonlinear DSR iterations.

Tuunanen and Peffers (2018) offer a good example of a project that would have benefitted from the application of <sup>e</sup>DSR. The project developed artifacts in five organizations in multiple countries on three different continents, and more than 200 people from different stakeholder groups participated in the

DSR demonstration and evaluation activities. The article also offers a graphical illustration of the overall study, which depicts the nonlinear DSR iterations and how these link to each other. The project thus offers a good match of both heuristics. However, there are also examples of DSR studies that might not have benefitted from the <sup>e</sup>DSR approach. For example, vom Brocke et al. (2021) presented a DSR study that developed a framework to classify business processes for their research client, Hilti.<sup>8</sup> First, given the focus on the case company Hilti, this DSR study aimed for low projectability of the artifact. The framework was expected to apply to Hilti globally but was limited to Hilti’s organizational context. Second, the problem understanding was comparably clear from the outset of the project. Online survey data were collected from 50+ Hilti global process owners. The researchers and the global process owners agreed on two primarily relevant factors based on the data analysis. They created a framework consisting of a 2×2 matrix differentiating four process clusters (performance, creativity, reliability, and agility). Specific management requirements were identified for each cluster, and process management practices were defined. Thus, since this DSR project was not characterized by a high level of complexity, <sup>e</sup>DSR may not have been of benefit. That said, it would be interesting to see the spectrum of solutions the <sup>e</sup>DSR approach might have been capable of producing.

Fifth, we expect <sup>e</sup>DSR to positively impact the education and engagement of young talent in DSR. <sup>e</sup>DSR provides a conceptualization of what constitutes a design, and it defines clear design subunits, enabling better planning and scoping of complex DSR projects. Further, specific intermediate artifacts, validation criteria, validation techniques, and the output of design knowledge are defined, supporting the rigorous crafting of each echelon. The field experiment we conducted with Ph.D. students provides evidence of the positive effect of advising students to conceptualize a design process according to echelons and to structure their work accordingly. Further, the identification of echelons would also allow for the development of further guidelines on how to rigorously craft specific echelons for multi-year Ph.D. projects. This, in turn, would further advance the rigor and quality of contributions a single researcher could make to design knowledge.

Sixth, the <sup>e</sup>DSR approach also provides a means to involve practice more continuously and systematically in the creation of design knowledge. For instance, practitioners could formulate problems, which researchers could pick up to further conceptualize and specify definitions of objectives and requirements. In contrast, others might work on potential design and development evaluated and co-created by practitioners. Specifically, as DSR is positioned to conduct research in the intersection of—as Hevner et al. (2004) put it—the “business environment” and the “knowledge base,” such academia-practice engagement is instrumental to DSR. It has an immediate effect on the quality of design knowledge and the impact of DSR. <sup>e</sup>DSR would allow practitioners to engage in the formulation of problems and their validation while at the same time participating in the development and validation of intermediate artifacts and complex design projects. Moreover, beyond DSR, many calls have been made in IS research to intensify dialogue between academia and practice (Baskerville et al., 2020; Te’eni et al., 2017), and <sup>e</sup>DSR certainly offers a means to demonstrate and leverage such dialogue. In this regard, <sup>e</sup>DSR also provides new opportunities for clinical research based on IS practice to generate knowledge from practitioner-researcher interventions to achieve desired outcomes in IS development, use, and management practice contexts (Baskerville et al., 2023). This, in turn, could facilitate proof-of-use (Nunamaker et al., 2015) contributions to design knowledge, both in terms of practice and by further theorizing the findings. This could lead to breakthroughs in DSR in terms of its impact on society and business.

Finally, no study is without limitations, and ours is no exception. The artifact design was mainly influenced by two DSR methodologies: the DSRM by Peffers et al. (2007) and the Sonnenberg/vom Brocke model (2012). Other prominent DSR methodologies are available, such as the systems development approach of Nunamaker et al. (1991), the DSR cycle model of Hevner et al. (2004, 2007), the action design research of Sein et al. (2011), and the design research cycle presented by Kuechler and Vaishnavi (2008). Action design research may come closest to what was attempted in the present study, with concurrent feedback on design decisions. The other DSR methodologies focus more on different aspects of the concept, such as the iterative approach to DSR (Hevner, 2007; Hevner et al., 2004).

This study does not give normative advice on validation criteria or techniques but rather consolidates suggestions from extant discourses to illustrate the character of the proposed DSR echelons. For a structured literature review on developing a comprehensive set of validation criteria or techniques, see Peffers et al. (2012) or Prat et al. (2015). Instead, this study offers heuristics based on the selected literature, observations drawn from the investigated demonstration studies, and the authors’ own experience of conducting DSR over the past 20 years. It seeks to meet completeness criteria by offering different options for specific DSR stages. Researchers should choose suitable subsets of the described criteria and techniques that fit their research contexts and might also engage in developing further criteria and techniques.

## Conclusion

We sought to answer how to align the DSR process with research environments, which are often very complex when working toward innovative solutions to real-world problems. Rapid changes in a research environment can be problematic if DSR outputs are evaluated as a final phase of the DSR process, as DSRM suggests (Peffers et al., 2007). The <sup>e</sup>DSR methodology in this study develops an echelon-oriented organizing logic for DSR projects that supports a nonlinear DSR process and is, of course, compatible with the iterative nature of DSR. The <sup>e</sup>DSR methodology was developed through a deductive and inductive research process. An artifact was developed based on findings from the literature, expository instantiations, qualitative research with authors and experts, and field experiments. Process-, outcome-, and contribution-related criteria were used to evaluate the DSR methodology. Our study presents a robust and ready-to-use methodology that can be applied in dynamic research environments featuring DSR complexity (of a problem and/or solution) as well as multiple research clients and/or contexts. The <sup>e</sup>DSR methodology can also be applied in more stable research environments. It offers a highly agile approach to DSR with clear and well-defined evaluation criteria for each study phase. This study also includes suggested sets of validation techniques for researchers to apply.

## Acknowledgments

The authors want to thank Professor Emeritus Jyrki Wallenius for his support in developing the general systems theory section of the article. We also thank the anonymous reviewers and the editors for their feedback and supportive comments to develop the article. Finally, we want to thank all those who participated in the demonstration and evaluation of the <sup>e</sup>DSR methodology during the past eight years.

## References

Ackoff, R. L. (1973). Science in the systems age: Beyond IE, OR, and MS. Operations Research, 21(3), 661-671. https://doi.org/10.1287/opre.21.3.661

Ackoff, R. L., & Emery, F. E. (1972). On purposeful systems. Tavistock.

Abraham, R., Aier, S., & Winter, R. (2014). Fail early, fail often: Towards coherent feedback loops in design science research evaluation. In Proceedings of the International Conference on Information Systems.

Aier, S., Labusch, N., & Pähler, P. (2015). Implementing architectural thinking: A case study at Commerzbank AG. In A. Persson & J. Stirna (Eds.), Advanced Information Systems Engineering Workshops (CAiSE 2015) (pp. 389-400). Springer. https://doi.org/10.1007/978-3-319-19243-7\_36

Baskerville, R., vom Brocke, J., Mathiassen, L., & Scheepers, H. (2023). Clinical research from information systems practice. European Journal of Information Systems, 32(1), 1-9. https://doi.org/10.1080/0960085X.2022.2126030

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: Finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358-376. https://doi.org/10.17705/ 1jais.00495

Becker, J., vom Brocke, J., Heddier, M., & Seidel, S. (2015). In search of information systems (grand) challenges. Business & Information Systems Engineering, 57(6), 377-390. https://doi.org/10.1007/s12599-015-0394-0

Blaschke, M., Haki, K., Riss, U., & Aier, S. (2017). Design principles for business model-based management methods—A servicedominant logic perspective. In A. Maedche, J. vom Brocke, & A. Hevner (Eds.), Designing the digital transformation (DESRIST 2017) (pp. 179-198). Springer. https://doi.org/10.1007/978-3- 319-59144-5\_11

Brosius, M., Aier, S., Haki, K., & Winter, R. (2019). The institutional logic of harmonization: Local versus global perspectives. In D. Aveiro, G. Guizzardi, S. Guerreiro, & W. Guédria (Eds.), Advances in Enterprise Engineering XII (EEWC 2018) (pp. 3- 17). Springer. https://doi.org/10.1007/978-3-030-06097-8\_1

Bunge, M. A. (1979). Treatise on basic philosophy: Ontology II: A world of systems. Reidel. https://doi.org/10.1007/978-94-009- 9392-1

Cahenzli, M. (2020). Guiding the institutionalization of behavior: designing a nudging-inspired solution (Working paper). Institute of Information Management (IWI-HSG), University of St. Gallen. https://www.alexandria.unisg.ch/handle/20.500.14171/ 112614

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions. In Proceedings of the Hawaii International Conference on System Sciences. https://doi.org/10.1109/HICSS.2015.485

Checkland, P. (1981). Systems thinking, systems practice. Wiley.

Conboy, K. (2009). Agility from first principles: Reconstructing the concept of agility in information systems development. Information Systems Research, 20(3), 329-354. https://doi.org/ 10.1287/isre.1090.0236

Conboy, K., Gleasure, R., & Cullina, E. (2015). Agile design science research. In B. Donnellan, M. Helfert, J. Kenneally, D. VanderMeer, M. Rothenberger, & R. Winter (Eds.), New horizons in design science: Broadening the research agenda (DESRIST 2015) (pp. 168-180). Springer. https://doi.org/10.1007/978-3-319-18714-3\_11

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. (2018). Fundamentals of business process management. Springer. https://doi.org/10.1007/978-3-662-56509-4

Emery, F. (2016). Characteristics of socio-technical systems. In E. Trist, H. Murray, & B. Trist (Eds.), The social engagement of social science, a Tavistock anthology (Vol. 2) (pp. 157-186). University of Pennsylvania Press. https://doi.org/10.9783 9781512819052-009

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-355. http://www.jstor.org/stable/43825912

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312- 335. http://aisel.aisnet.org/jais/vol8/iss5/1

Gregory, R. W., & Muntermann, J. (2014). Research note—Heuristic theorizing: Proactively generating design theories. Information Systems Research, 25(3), 639-653. https://doi.org/10.1287/ isre.2014.0533

Gross, S., Stelzl, K., Grisold, T., Mendling, J., Röglinger, M., & vom Brocke, J. (2021). The business process design space for exploring process redesign alternatives. Business Process Management Journal, 27(8), 25-56. https://doi.org/10.1108/ BPMJ-03-2020-0116

Hamilton, S., & Chervany, N. L. (1981). Evaluating information system effectiveness-Part I: Comparing evaluation approaches. MIS Quarterly, 5(3), 55-69. https://doi.org/10.2307/249291

Hevner, A. R. (2007). A three cycle view of design science research. Scandinavian Journal of Information Systems, 19(2), 87-92. http://aisel.aisnet.org/sjis/vol19/iss2/4

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105. https://doi.org/10.2307/25148625

Hevner, A., Parsons, J., Brendel, A., Lukyanenko, R., Tiefenbeck, V., Trembley, M., & vom Brocke, J. (2021). Research transparency in design science research. Presented at the International Conference on Design Science Research in Information Systems.

Holland, J. H. (2006). Studying complex adaptive systems. Journal of Systems Science and Complexity, 19(1), 1-8. https://doi.org/10.1007/s11424-006-0001-z

Katz, D., & Kahn, R. L. (1966). The social psychology of organizations. Wiley.

Kuechler, B., & Vaishnavi, V. (2008). On theory development in design science research: Anatomy of a research project. European Journal of Information Systems, 17(5), 489-504. https://doi.org/10.1057/ejis.2008.40

Lee, J. K. (2015). Guest editorial: Research framework for AIS grand vision of the bright ICT initiative. MIS Quarterly, 39(2), ii-xii. https://www.jstor.org/stable/26628353

Lück, D., & Leyh, C. (2017). Enabling business domain-specific ecollaboration: Developing artifacts to integrate e-collaboration into product costing. In A. Maedche, J. vom Brocke, & A. Hevner (Eds.), Designing the digital transformation (DESRIST 2017) (pp. 296-312). https://doi.org/10.1007/978-3-319-59144- 5\_18

Lukyanenko, R., Evermann, J., & Parsons, J. (2014). Instantiation validity in IS design research. In M. C. Tremblay, D. VanderMeer, M. Rothenberger, A. Gupta, & V. Yoon (Eds.), Advancing the impact of design science: Moving from theory to practice (DESRIST 2014) (pp. 321-328). Springer. https://doi.org/10.1007/978-3-319-06701-8\_22

Lukyanenko, R., & Parsons, J. (2020). Easier crowdsourcing is better: Designing crowdsourcing systems to increase information quality and user participation. In J. vom Brocke, A. Maedche, & A. Hevner (Eds.), Design Science Research. Cases. Springer. https://doi.org/10.1007/978-3-030-46781-4\_3

Maedche, A., Gregor, S., Morana, S., & Feine, J. (2019). Conceptualization of the problem space in design science research. In B. Tulu, S. Djamasbi, & G. Leroy (Eds.), Extending the boundaries of design science theory and practice (DESRIST 2019) (pp. 18-31). Springer. https://doi.org/10.1007/978-3-030- 19504-5\_2

March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. Decision Support Systems, 15(4), 251-266. https://doi.org/10.1016/0167-9236(94)00041-2

Majchrzak, M., Markus, M., & Wareham, J. (2016). Designing for digital transformation: Lessons for information systems research from the study of ICT and societal challenges. MIS Quarterly, 40(2), 267-277. https://www.jstor.org/stable/26628906

Mesarovic, M. D., Macko, D., & Takahara, Y. (1970). Theory of hierarchical, multilevel systems. Academic Press.

Mesarovic, M. D. & Takahara, Y. (1972). General systems theory: Mathematical foundations. Academic Press.

Miller, J. G. (1978). Living systems. McGraw-Hill.

Mullarkey, M. T., & Hevner, A. R. (2019). An elaborated action design research process model. European Journal of Information Systems, 28(1), 6-20. https://doi.org/10.1080/0960085X.2018. 1451811

Newell, A., & Simon, H. A. (1972). Human problem solving. Prentice Hall.

Niemöller, C., Özcan, D., Metzger, D., & Thomas, O. (2014). Towards a design science-driven product-service system engineering methodology. In M. C. Tremblay, D. VanderMeer, M. Rothenberger, A. Gupta, & V. Yoon (Eds.), Advancing the impact of design science: Moving from theory to practice (DESRIST 2014) (pp. 180-193). Springer. https://doi.org/10.1007/978-3-319-06701-8\_12

Nunamaker Jr., J. F., Briggs, R. O., Derrick, D. C., & Schwabe, G. (2015). The last research mile: Achieving both rigor and relevance in information systems research. Journal of Management Information Systems, 32(3), 10-47. https://doi.org/ 10.1080/07421222.2015.1094961

Nunamaker, J. F., Chen, M., & Purdin, T. D. (1991). Systems development in information systems research. Journal of Management Information Systems, 7(3), 89-106. https://doi.org/10.1080/07421222.1990.11517898

Peffers, K., Rothenberger, M., Tuunanen, T., & Vaezi, R. (2012). Design science research evaluation. In K. Peffers, M. Rothenberger, & B. Kuechler (Eds.), Design science research in information systems. Advances in theory and practice (DESRIST 2012) (pp. 398-410). Springer. https://doi.org/10.1007/978-3- 642-29863-9\_29

Peffers, K., Tuunanen, T., & Niehaves, B. (2018). Design science research genres: Introduction to the special issue on exemplars and criteria for applicable design science research. European Journal of Information Systems, 27(2), 129-139. https://doi.org/10.1080/0960085X.2018.1458066

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77. https://doi.org/10.2753/MIS0742-1222240302

Prat, N., Comyn-Wattiau, I., & Akoka, J. (2015). A taxonomy of evaluation methods for information systems artifacts. Journal of Management Information Systems, 32(3), 229-267. https://doi.org/10.1080/07421222.2015.1099390

Rai, A. (2017). Editor's comments: Diversity of design science research. MIS Quarterly, 41(1), iii-xviii. https://www. jstor.org/stable/26629633

Searle, J. (2008). Reductionism and the irreducibility of consciousness. In M. A. Bedau & P. Humphreys (Eds.), Emergence: Contemporary readings in philosophy and science

(pp. 69-80). MIT Press. https://doi.org/10.7551/mitpress/ 9780262026215.003.0005

Schilling, R., Aier, S., & Winter, R. (2019). Extending the portfolio of control mechanisms for managing IS complexity: Designing an enterprise architecture label. In Proceedings of the International Conference on Information Systems. https://aisel.aisnet.org/icis2019/design\_science/design\_science/3

Schilling, R., Haki, K., & Aier, S. (2018). Dynamics of control mechanisms in enterprise architecture management: A sensemaking perspective. In Proceedings of the International Conference on Information Systems. https://aisel.aisnet.org/ icis2018/governance/Presentations/1

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37-56. https://doi.org/10.2307/23043488

Sonnenberg, C., Huemer, C., Hofreiter, B., Mayrhofer, C., & Braccini, A. M. (2012). The REA-DSL: A domain-specific modeling language for business models. In H. Mouratidis & C. Rolland (Eds.), Advanced Information Systems Engineering (CAiSE 2012) (pp. 252-266). Springer. https://doi.org 10.1007/978-3-642-21640-4\_20

Sonnenberg, C., & vom Brocke, J. (2011). Evaluation patterns for design science research artifacts. In M. Helfert & B. Donnellan (Eds.), Practical Aspects of Design Science (EDSS 2011) (pp.71- 83). Springer. https://doi.org/10.1007/978-3-642-33681-2\_7

Sonnenberg, C., & vom Brocke, J. (2012). Evaluations in the science of the artificial: Reconsidering the build-evaluate pattern in design science research. In K. Peffers, M. Rothenberger, & B. Kuechler (Eds.), Design science research in information systems. Advances in theory and practice (DESRIST 2012) (pp. 381-397). Springer. https://doi.org/10.1007/978-3-642-29863-9\_28

Sonnenberg, C., & vom Brocke, J. (2014). The missing link between BPM and accounting: Using event data for accounting in process-oriented organizations. Business Process Management Journal, 20(2), 213-246. https://doi.org/10.1108/BPMJ-12- 2012-0136

Stöckli, E., Neiditsch, G., Uebernickel, F., & Brenner, W. (2017). Towards an understanding of how and why design science research scholars evaluate. In Proceedings of the Australasian Conference on Information Systems. https://aisel.aisnet.org/ acis2017/16

Strong, D. M., Tulu, B., Agu, E., & Pedersen, P. C. (2020). Search and evaluation of coevolving problem and solution spaces in a complex healthcare design science research project. IEEE Transactions on Engineering Management, 70(3), 912-926. https://doi.org/10.1109/TEM.2020.3014811

Thomas, O., & vom Brocke, J. (2010). A value-driven approach to the design of service-oriented information systems: Making use of conceptual models. Information Systems and e-Business Management, 8(1), 67-97. https://doi.org/10.1007/s10257-009- 0110-z

Trist, E. L., & Bamforth, K. W. (1951). Some social and psychological consequences of the longwall method of coalgetting: An examination of the psychological situation and defences of a work group in relation to the social structure and technological content of the work system. Human relations, 4(1), 3-38. https://doi.org/10.1177/001872675100400101

Tuunanen, T., & Peffers, K. (2018). Population targeted requirements acquisition. European Journal of Information Systems, 27(6), 686-711. https://doi.org/10.1080/0960085X.2018.1476015

Venable, J. (2006). The role of theory and theorising in design science research. In Proceedings of the International Conference on Design Science Research in Information Systems and Technology.

Venable, J. R., vom Brocke, J., & Winter, R. (2019). Designing TRiDS: Treatments for risks in design science. Australasian Journal of Information Systems, 23. http://doi.org/10.3127/ajis.v23i0.1847

Venable, J., Pries-Heje, J., & Baskerville, R. (2012). A comprehensive framework for evaluation in design science research. In K. Peffers, M. Rothenberger, & B. Kuechler (Eds.), Design science research in information systems. Advances in theory and practice (DESRIST 2012) (pp. 423-438). Springer. https://doi.org/10.1007/978-3-642- 29863-9\_31

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. European Journal of Information Systems, 25(1), 77-89. https://doi.org/10.1057/ejis.2014.36

von Bertalanffy, L. (1968). General systems theory: Foundations, development, applications. George Braziller.

vom Brocke, J., Braccini, A. M., Sonnenberg, C., & Spagnoletti, P. (2014). Living IT infrastructures—An ontology-based approach to aligning IT infrastructure capacity and business needs. International Journal of Accounting Information Systems, 15(3), 246-274. https://doi.org/10.1016/j.accinf.2013.10.004

vom Brocke, J., Gau, M., & Maedche, A. (2021). Journaling the design science research process. Transparency about the making of design knowledge. In L. Chandra Kruse, S. Seidel, & G. I. Hausvik (Eds.), The next wave of sociotechnical design (DESRIST 2021) (pp. 131- 136). Springer. https://doi.org/10.1007/978-3-030-82405-1\_15

vom Brocke, J., Recker, J., & Mendling, J. (2010). Value-oriented process modeling: Integrating financial perspectives into business process re-design. Business Process Management Journal, 16(2), 333-356. https://doi.org/10.1108/14637151011035633

vom Brocke, J., Sonnenberg, C., & Baumoel, U. (2011). Linking accounting and process-aware information systems: Towards a generalized information model for process-oriented accounting. In Proceedings of the European Conference on Information Systems. https://aisel.aisnet.org/ecis2011/23

vom Brocke, J., Sonnenberg, C., & Simons, A. (2009). Valueoriented information systems design: The concept of potentials modeling and its application to service-oriented architectures. Business & Information Systems Engineering, 1(3), 223-233. https://doi.org/10.1007/s12599-009-0046-3

vom Brocke, J., Watson, R., Dwyer, C., Elliot, S., & Melville, N. (2013). Green information systems: Directives for the IS discipline. Communications of the Association for Information Systems, 33, 509-520. https://doi.org/10.17705/1CAIS.03330

vom Brocke, J., Weber, M., & Grisold, T. (2021). A matrix for context-aware business process management: Empirical evidence from Hilti. In Proceedings of the International Conference on Business Process Management. https://ceurws.org/Vol-3112/paper5.pdf

vom Brocke, J., Winter, R., Hevner, A., & Maedche, A. (2020). Accumulation and evolution of design knowledge in design science research: A journey through time and space. Journal of the Association for Information Systems, 21(3), 520-544. https://doi.org/10.17705/1jais.00611

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59. https://doi.org/10.1287/isre. 3.1.36

Weiss, S., Aier, S., & Winter, R. (2013). Institutionalization and the effectiveness of enterprise architecture management. In Proceedings of the International Conference on Information Systems. https://aisel.aisnet.org/icis2013/proceedings/Governance Management/9

William, D., & Black, P. (1996). Meanings and consequences: a basis for distinguishing formative and summative functions of assessment? British Educational Research Journal, 22(5), 537- 548. https://doi.org/10.1080/0141192960220502

Winter, R. (1996). Continuous abstraction hierarchies in hierarchical production planning. Journal of Decision Systems, 5(1-2), 11-34. https://doi.org/10.1080/12460125.1996.10511672

Winter, R. (2008). Design science research in Europe. European Journal of Information Systems, 17(5), 470-475. https://doi.org/10.1057/ejis.2008.44

Winter, R. (2016). Establishing “architectural thinking” in organizations. In J. Horkoff, M. A. Jeusfeld, & A. Persson (Eds.), The practice of enterprise modeling (PoEM 2016) (pp. 3-8). Springer. https://doi.org/10.1007/978-3-319-48393-1\_1

Winter, R. (2022). Designing informal EAM interventions: A complementary approach for managing enterprise architecture complexity. In Proceedings of the 55th Hawaii International Conference on System Sciences (pp. 7244-7253). http://hdl.handle.net/10125/80212

Winter, R., & Albani, A. (2013). Restructuring the design science research knowledge base: A one-cycle view of design science research and its consequences for understanding organizational design problems. In R. Baskerville, M. de Marco, & P. Spagnoletti (Eds.), Designing organizational systems: An interdisciplinary discourse (pp. 63-81). Springer. https://doi.org/10.1007/978-3-642-33371-2\_4

## About the Authors

Tuure Tuunanen is a professor of information systems in the Faculty of Information Technology at the University of Jyväskylä. He leads the Value Creation for Cyber-Physical Systems and Services Research Group and the Finnish Hub for Digitalization. He is also a global faculty fellow of the Center for Service Leadership at Arizona State University. He holds M.Sc. and D.Sc. (Econ.) degrees from the Aalto University School of Business. His research is at the cross-sections of information systems, software engineering, and marketing and service research, and he is keenly interested in multidisciplinary research in service innovation, design, and development. His current research interests lie in digital and cyber-physical services. He is an associate editor for Communication of the Association for Information Systems (Department of Digital Design) and Journal of Service Research and a senior editor for European Journal of Information Systems and Journal of the Association for Information Systems He is also a member of the editorial board for Information Systems Research. He has published in Journal of Management Information Systems, Journal of the Association for Information Systems, European Journal of Information Systems, and Journal of Service Research, among other journals. https://orcid.org/0000-0001-7119-1412

Robert Winter is a full professor at the Institute of Information Management, University of St. Gallen (HSG) in Switzerland. He is also the founding director of HSG’s Executive MBA program in Business Engineering. Having been vice editor-in-chief of Business & Information Systems Engineering journal and senior editor of the European Journal of Information Systems, he currently serves on the editorial board of MIS Quarterly Executive. His research interests include design science research methodology, and all aspects of enterprise-level IS research, such as enterprise architecture management, the design and governance of digital platforms, corporate data management, and the design and governance of enterprise transformation. He has published in Management Information Systems Quarterly, Journal of the Association for Information Systems, Journal of Information Technology, and European Journal of Information Systems, among other journals. https://orcid.org/0000-0001-9383-2276

Jan vom Brocke is the chair of Information Systems & Business Process Management at the University of Münster in Germany and is the director of ERCIS—The European Research Center for Information Systems. He is a visiting professor at the University of Liechtenstein, and he has been named a Fellow of the Association for Information Systems (AIS), a Fellow of the ESCP Center for Design Science in Entrepreneurship, a Schoeller Senior Fellow at Friedrich Alexander University (FAU) in Germany, and a Distinguished Professor at the National University of Ireland, Maynooth University (MU). He has published in Management Information Systems Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Information Technology, European Journal of Information System, Information Systems Journal, Journal of Strategic Information Systems, Communications of the ACM, MIT Sloan Management Review, and Management Science, among others journals. https://orcid.org/0000-0002-0071-3719

## Appendix A

## Papers Applying the Sonnenberg/vom Brocke Model

Abraham, R. (2015). Development of design principles for boundary objects in enterprise transformation [Unpublished doctoral dissertation]. University of St. Gallen.

Afflerbach, P., Bolsinger, M., & Röglinger, M. (2016). An economic decision model for determining the appropriate level of business process standardization. Business Research, 9(2), 335-375. https://doi.org/10.1007/s40685-016-0035-6

Bärenfänger, R., & Otto, B. (2015). Proposing a capability perspective on digital business models. In Proceedings of the Institute of Electrical and Electronics Engineers Conference on Business Informatics. https://doi.org/10.1109/CBI.2015.18

Blaschke, M., Haki, K., Riss, U., & Aier, S. (2017). Design principles for business model-based management methods—A service-dominant logic perspective. In A. Maedche, J. vom Brocke, & A. Hevner (Eds.), Designing the digital transformation (DESRIST 2017) (pp. 179- 198). Springer. https://doi.org/10.1007/978-3-319-59144-5\_11

Bolsinger, M. (2014). Bringing value-based business process management to the operational process level. Information Systems and e-Business Management, 13(2), 355-398. https://doi.org/10.1007/s10257-014-0248-1

Braunnagel, D., & Leist, S. (2016). Applying evaluations while building the artifact: Experiences from the development of process model complexity metrics. In Proceedings of the Hawaii International Conference on System Sciences. https://doi.org/10.1109/HICSS.2016.551

Engelmann, A., Heinrich, P., & Schwabe, G. (2017). Mobiles Lernen für Industrie 4.0: Probleme, Ziele, Lernarrangement [Mobile learning for industry 4.0: Problems, goals, learning arrangement]. In Proceedings of the International Conference on Wirtschaftsinformatik. https://doi.org/10.5281/zenodo.830284

Häckel, B., Miehle, D., Pfosser, S., & Übelhör, J. (2017). Development of dynamic key figures for the identification of critical components in smart factory information networks. In Proceedings of the European Conference on Information Systems. http://aisel.aisnet.org/ ecis2017\_rip/27

Herterich, M. M., Buehnen, T., Uebernickel, F., & Brenner, W. (2016). A taxonomy of industrial service systems enabled by digital product innovation. In Proceedings of the Hawaii International Conference on System Sciences. https://doi.org/10.1109/HICSS.2016.157

Hewing, M. (2013). Business process blueprinting: A method for customer-oriented business process modeling. Springer. https://doi.org/10.1007/978-3-658-03729-1

Holler, M., Neiditsch, G., Uebernickel, F., & Brenner, W. (2017). Digital product innovation in manufacturing industries: Towards a taxonomy for feedback-driven product development scenarios. In Proceedings of the Hawaii International Conference on System Sciences. https://doi.org/10.24251/HICSS.2017.576

Jannaber, S., Riehle, D. M., Delfmann, P., Thomas, O., & Becker, J. (2017). Designing a framework for the development of domain-specific process modelling languages. In A. Maedche, J. vom Brocke, & A. Hevner (Eds.), Designing the digital transformation (DESRIST 2017) (pp. 39-54). Springer. https://doi.org/10.1007/978-3-319-59144-5\_3

Lehnert, M., Röglinger, M., & Seyfried, J. (2018). Prioritization of interconnected processes. Business & Information Systems Engineering, 60(2), 95-114. https://doi.org/10.1007/s12599-017-0490-4

Lück, D., & Leyh, C. (2017). Enabling business domain-specific e-collaboration: Developing artifacts to integrate e-collaboration into product costing. In A. Maedche, J. vom Brocke, & A. Hevner (Eds.), Designing the digital transformation (DESRIST 2017) (pp. 296- 312). Springer. https://doi.org/10.1007/978-3-319-59144-5\_18

Marjanovic, O. (2016). Designing innovative education through action design research: Method and application for teaching design activities in large lecture environments. Journal of Information Technology Theory and Application. 17(2), 22-50. https://aisel.aisnet.org/jitta/vol17/iss2/1

Niemöller, C., Metzger, D., Berkemeier, L., Zobel, B., Thomas, O., & Thomas, V. (2016). Designing health applications for developing countries. In Proceeding of the European Conference on Information Systems. https://aisel.aisnet.org/ecis2016\_rp/149

Niemöller, C., Metzger, D., Fellmann, M., Özcan, D., & Thomas, O. (2016). Shaping the future of mobile service support systems: Ex-ante evaluation of smart glasses in technical customer service processes. In H. C. Mayr & M. Pinzger (Eds.), Informatik 2016 (pp. 53-767). Gesellschaft für Informatik. https://cs.emis.de/LNI/Proceedings/Proceedings259/753.pdf

Niemöller, C., Zobel, B., Berkemeier, L., Metzger, D., Werning, S., Adelmeyer, T., …, & Thomas, O. (2017). Sind Smart Glasses die Zukunft der Digitalisierung von Arbeitsprozessen? Explorative Fallstudien zukünftiger Einsatzszenarien in der Logistik [Are smart glasses the future of digitalization of work processes? Explorative case studies of future use scenarios in logistics]. In Proceedings of the International Conference on Wirtschaftsinformatik. https://www.wi2017.ch/images/wi2017-0348.pdf

Nunamaker Jr, J. F., Briggs, R. O., Derrick, D. C., & Schwabe, G. (2015). The last research mile: Achieving both rigor and relevance in information systems research. Journal of Management Information Systems, 32(3), 10-47. https://doi.org/10.1080/07421222. 2015.1094961

Raber, D. 2013. Reifegradmodellbasierte Weiterentwicklung von Business Intelligence im Unternehmen [Maturity model-based evolution of business intelligence in organizations] [Unpublished doctoral dissertation]. University of St. Gallen.

Rosenberger, M., Lehrer, C., & Jung, R. (2016). Ein Datenmodell zur Unterstützung der Datenintegration von Nutzeraktivitäten aus verschiedenen sozialen Netzwerken [A data model to support data integration of user activities from different social networks]. In Proceedings of the Multikonferenz Wirtschaftsinformatik. https://www.alexandria.unisg.ch/handle/20.500.14171/104621

Sonnenberg, C. (2013). Bridging the gap between business process management and accounting: Design and evaluation of a process accounting model [Unpublished doctoral dissertation]. University of Liechtenstein.

Sonnenberg, C., & vom Brocke, J. (2014). The missing link between BPM and accounting: Using event data for accounting in processoriented organizations. Business Process Management Journal, 20(2), 213-246. https://doi.org/10.1108/BPMJ-12-2012-0136

Tuunanen, T., Vartiainen, T., Ebrahim, M., & Liang, M. (2015). Continuous requirements risk profiling in information systems development. In Proceedings of the Hawaii International Conference on System Sciences. https://doi.org/10.1109/HICSS.2015.483

van Staden, C. J., van Biljon, J. A., & Kroeze, J. H. (2017). Using a user experience evaluation framework for eModeration. In Proceedings of the Conference on Information Communication Technology and Society. https://doi.org/10.1109/ICTAS.2017.7920523

Vanhoof, E. (2016). Evolvable accounting information systems: Applying design science methodology and normalized systems theory to tackle combinatorial effects of multiple GAAP [Unpublished doctoral dissertation]. University of Antwerpen.

vom Brocke, J., Braccini, A. M., Sonnenberg, C., & Spagnoletti, P. (2014). Living IT infrastructures—An ontology-based approach to aligning IT infrastructure capacity and business needs. International Journal of Accounting Information Systems, 15(3), 246-274. https://doi.org/10.1016/j.accinf.2013.10.004

## Appendix B

## Author Interviews

<table><tr><td colspan="5">Table B1. Windmill Management Information System Development (Niemöller et al., 2014)</td></tr><tr><td>Design echelon</td><td>Intermediate artifact</td><td>Validation criteria</td><td>Validation techniques</td><td>Design knowledge</td></tr><tr><td>Problem analysis</td><td>Product-service engineering methods must be adapted to include IT artifact development</td><td>PSS engineering methodologies in the context of DSR have yet to be analyzed (degree to which the problem has been solved)</td><td>Literature review (nonstructured)</td><td>Validated research gap: adjusted design science-oriented PSS engineering methodology</td></tr><tr><td>Objectives and requirements definition</td><td>99% availability requirement</td><td>Completeness per stakeholder requirements, economic feasibility, operationality</td><td>Expert interviews, plant-level simulation, logical reasoning of technical customer service process</td><td>Online plant component added: technicians must be connected via a mobile service support system</td></tr><tr><td>Design and development</td><td>Customer requirements specification</td><td>Internal consistency of the method</td><td>Design mock-up (without integration)</td><td>Use case descriptions for a fictional case</td></tr><tr><td>Demonstration</td><td>Instance of an artifact</td><td>Efficiency (of the artifact)</td><td>Experiment with prototype: customer demonstration with concept prototype</td><td>Improperly designed data flows detected in experiment; validated artifact instance in an artificial setting</td></tr><tr><td>Evaluation</td><td>Instance of an artifact plus knowledge database (to facilitate transfer/use)</td><td>Completeness (of design): product roll-out and signing service contracts, external consistency</td><td>Focus group, international trade fair</td><td>Proof of intended value (not realized)</td></tr></table>

<table><tr><td colspan="5">Table B2. Data Structures for Process-Oriented Accounting (Sonnenberg &amp; vom Brocke, 2014)</td></tr><tr><td>Design echelon</td><td>Intermediate artifact</td><td>Validation criteria</td><td>Validation techniques</td><td>Design knowledge</td></tr><tr><td>Problem analysis</td><td>Observation of a problem: lack of info-logical or data-logical structures necessary to establish dedicated process-oriented accounting</td><td>Degree to which the problem has been solvedSolvability (continuum, degree)</td><td>Literature review (nonstructured)</td><td>Validated problem statement: lack of data integration between accounting and process management IS</td></tr><tr><td>Objectives and requirements definition</td><td>Design objective: data model capable of integrating and structuring accounting and process data in support of the design, execution, and control of business processes</td><td>Fit to validated problem statement (coherency)Applicability (to the problem)Feasibility (economic)</td><td>Expert interview (n = 4)Logical reasoning</td><td>Validated design objectives: semi-automatic parameterization and provision of data needed for financial assessment</td></tr><tr><td>Design and development</td><td>Design specification</td><td>· Fit to validated design objectives (coherency) · Applicability to instantiate the artifact · Consistency (internal) · Feasibility</td><td>· Logical reasoning · Design mock-up · Expert interview (n = 22)</td><td>Validated artifact design: metamodel for data integration between accounting and process management IS and design principles</td></tr><tr><td>Demonstration</td><td>Instance of an artifact (examples)</td><td>· Fit to validated artifact design (coherency)</td><td>Demonstration with prototype</td><td>Validated instance of the artifact: data structures for process-oriented accounting, tool implementation</td></tr><tr><td>Evaluation</td><td>Evaluation of the artifact in parts (principles of event data disaggregation and event classification)</td><td>· Fit to validated instance of the artifact (coherency) · Utility (of the artifact)</td><td>· Case study · Expert interviews (n = 6)</td><td>Validated PoV of the artifact (in parts)</td></tr></table>

<table><tr><td>Design echelon</td><td>Intermediate artifact</td><td>Validation criteria</td><td>Validation techniques</td><td>Design knowledge</td></tr><tr><td>Problem analysis</td><td>What design principles guide the design of business model-based management (BMBM) methods to eventually account for and realize an S-D logic?</td><td>Degree to which the problem has been solved: extant research has already started incorporating network- and customer-oriented views in business model research</td><td>• Literature review (nonstructured)• Focus groups (n = 20)</td><td>Validated research gap: lack of guidance on designing BMBM methods in the literature</td></tr><tr><td>Objectives and requirements definition</td><td>Guidance for business model-based management (based on S-D logic)</td><td>Completeness per customer requirements</td><td>• Literature review (nonstructured)• Focus groups (n = 20)</td><td>Problem statement</td></tr><tr><td>Design and development</td><td>Decision for design principles (not method, not tool)</td><td>• Completeness (of design)• Fit (to objectives)</td><td>• Logical reasoning• Design mock-ups</td><td>Validated design specification based on S-D logic</td></tr><tr><td>Demonstration</td><td>Instance of an artifact: design principles</td><td>Proof of concept</td><td>Expert interviews (n = 4)</td><td>Proof of applicability, improved design principles</td></tr><tr><td>Evaluation</td><td>Instance of an artifact: design principles</td><td>• Completeness (of design)• Consistency (external)• Projectability (of results)• Effectiveness</td><td>Focus group (n = 6)</td><td>Validated artifact instance in a partially naturalistic setting</td></tr></table>

<table><tr><td colspan="5">Table B4. Business Domain-Specific E-Collaboration (Lück &amp; Leyh, 2017)</td></tr><tr><td>Design echelon</td><td>Intermediate artifact</td><td>Validation criteria</td><td>Validation techniques</td><td>Design knowledge</td></tr><tr><td>Problem analysis</td><td>A recognized need to overcome the challenges in product costing by supporting actors involved in the costing process when and where they need help</td><td>Solvability: As generic e-collaboration tools are not appropriate, a domain-specific tool should (and can) be developed</td><td>Qualitative survey (online, n = 28) complemented by interviewsReview (nonstructured) of scientific literature and practice solutions</td><td>Validated research gap: need for business domain-specific e-collaboration tool</td></tr><tr><td>Objectives and requirements definition</td><td>Identify requirements for e-collaboration in product costing</td><td>·Applicability (to the problem) ·Completeness per customer requirements</td><td>·Structured expert interviews (n = 14), coded afterward ·Validation of requirements by different experts (n = 11)</td><td>Requirements specifications (18 requirements and six constraints)</td></tr><tr><td>Design and development</td><td>Design specification</td><td>·Design fit ·Justification of design choice rationale (level of detail, transparency)</td><td>Testing mock-up (five user interface screens) with the designer team</td><td>Validated collaboration mock-up</td></tr><tr><td>Demonstration</td><td>Five use cases that instantiate the artifact (requirements specification)</td><td>Design fit</td><td>Focus group (n = 7)</td><td>·Proof of applicability (use cases, proof of concept) ·Selection and prioritization of promising use cases</td></tr><tr><td>Evaluation</td><td>Instance of an artifact (prototype) for the most promising use case</td><td>·Completeness (of design) ·Consistency (external)</td><td>·Survey (n = 8) ·Focus group (usability test for a selected use case, n = 8)</td><td>PoV (validated prototype)</td></tr></table>

## Interview Protocol

Can you describe (in specific detail) your learning and feedback regarding the product/process in these five steps? This will complement our tables.

How did the process benefit from the early-phase availability of intermediate artifacts (look at agile/concurrent justifications)?

o Efficiency of Design/Design Process Quality

▪ Reducing risk

• Intermediate results/adjustments

▪ Meeting time, cost, scope requirements

• Intermediate results/adjustments

▪ Enhancing collaboration/communication effectiveness

• Within team (additional reflection)

• With client

o Effectiveness of Design/Design Product (Artifact) Quality

▪ Features

▪ Usability, acceptance

How do these benefits relate to the additional efforts for multiple validations?

\- Describe the research journey with the paper.

\- Motivation: Why did you choose to evaluate intermediate artifacts?

Effects: What have you experienced (critical incident technique)?

▪ Positive

▪ Negative

## Appendix C

## Student Evaluation Form

## DSR Case Exercise Evaluation Form

Group number: ……. Participant name: …………………… .

All tasks relate to the case «Designing Crowdsourcing Systems to Increase Information

Quality and User Participation». Presentation time is 10 minutes.

Task 1: Analyze the design problem

Recommendations:

Formulate the problem in one statement.

\- Characterize the context the problem

o What is the domain/application where the problem occurs?

o Who are the stakeholders having the problem and what are their concerns?

When would you consider the problem to be solved?

o Specifically, what would an envisioned solution (regardless how it would look like in detail) enable the stakeholders to do?

Comments ………… …. Percentage (0-100):

Task 2: Sketch a problem solution

Recommendations:

What type of artifact serves as a solution?

How does the solution work (which mechanism, effect)?

What are the solution’s components?

Why is this solution design (most) promising?

\- What are the requirements for constructing the solution?

Comments ……………………… ……………………. Percentage (0-100):

Task 3: Plan how to demonstrate and/or evaluate your design

Recommendations:

When is the solution design «good enough» to stop iterating?

\- Where are the data for building and evaluating the artifact coming from?

How is the solution design to be demonstrated (proof of concept)?

How can the use value of the solution design be assessed (proof of use)?

Comments ……………… ………………. Percentage (0-100):

How do you evaluate the overall performance addressing the tasks?

Comments ……………………… ……………………. Percentage (0-100):
