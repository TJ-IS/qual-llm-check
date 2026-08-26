---
otero_id: 2320
otero_key: "JG3CC9V5"
title: "A simulation-based risk network model for decision support in project risk management"
authors: "Chao Fang; Franck Marle"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.021"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A simulation-based risk network model for decision support in project risk management

Chao Fang ⁎, Franck Marle

Laboratoire Genie Industriel, Ecole Centrale Paris, 92295, Chatenay-Malabry, France

## a r t i c l e i n f o

Article history: Received 20 July 2010 Received in revised form 24 September 2011 Accepted 23 October 2011 Available online 29 October 2011

Keywords: Project risk management Complexity Risk network Simulation Decision support system

## a b s t r a c t

This paper presents a decision support system (DSS) for the modeling and management of project risks and risk interactions. This is a crucial activity in project management, as projects are facing a growing complexity with higher uncertainties and tighter constraints. Existing classical methods have limitations for modeling the complexity of project risks. For example, some phenomena like chain reactions and loops are not properly taken into account. This will in<sup>fl</sup>uence the effectiveness of decisions for risk response planning and will lead to unexpected and undesired behavior in the project. Based on the concepts of DSS and the classical steps of project risk management, we develop an integrated DSS framework including the identi<sup>fi</sup>cation, assessment and analysis of the risk network. In the network, the nodes are the risks and the edges represent the cause and effect potential interactions between risks. The proposed simulation-based model makes it possible to re-evaluate risks and their priorities, to suggest and test mitigation actions, and then to support project manager in making decisions regarding risk response actions. An example of application is provided to illustrate the utility of the model.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Project risk management (PRM) is crucial and indispensable to the success of projects. Indeed, risks in projects have become higher in terms of number and global impact. Projects are more than ever exposed and averse to risks, and stakeholders are asking for more risk management to cover themselves against <sup>fi</sup>nancial or legal consequences. That is why it has become increasingly important to effectively and ef<sup>fi</sup>ciently manage project risks, in order to give a higher guarantee of success and comfort to project stakeholders, or at least to warn them against potential problems or disasters. Several standards have been developed in the <sup>fi</sup>eld of risk management and speci<sup>fi</sup>cally in project risk management [2,9,22–24,35]. Classical PRM process is comprised of four major phases: risk identi<sup>fi</sup>cation, risk analysis, risk response planning, and risk monitoring and control [35]. Risk identi<sup>fi</sup>cation is the process of determining events which, if they occurred, could affect project objectives positively or negatively. Risk analysis is the process of evaluating and prioritizing risks, essentially with respect to their characteristics like probability and impact. The process of risk response planning aims to choose actions which can reduce global risk exposure with least cost. Risk monitoring and control is the ongoing process of “implementing risk response plans, tracking identi<sup>fi</sup>ed risks, monitoring residual risks, identifying new risks, and evaluating risk process effectiveness throughout the project” [35].

Projects are facing a growing complexity, in both their structure and context. In addition to the organizational and technical complexities described by Baccarini [5], project managers have to consider a growing number of parameters (e.g., environmental, social, safety, and security) and a growing number of stakeholders, both inside and outside the project. The existence of numerous and diverse elements which are strongly interrelated is one of the main characteristics of complexity [13,14,25]. The complexity of project leads to the existence of a network of interdependent risks. For instance, there might be propagation from one “upstream” risk to numerous “downstream” risks; on the other side, a “downstream” risk may arise from the occurrence of several “upstream” risks which may belong to different categories. The extreme case of this propagation behavior is the chain reaction phenomenon or the “domino effect”. Another phenomenon is the loop, namely a causal path that leads from the initial occurrence of an event to the triggering of subsequent consequences until the initial event occurs once more. An example of loop is that one initial risk, project schedule delay, may have an impact on a cost overrun risk, which will in<sup>fl</sup>uence a technical risk, and then propagate to and amplify the original risk of schedule delay.

Many risk management methods and associated tools have now been developed. They are usually based on two concepts: probability and impact, assessed by qualitative or quantitative approaches. Criticality is an aggregate characteristic used to prioritize risks. It is generally a combination of probability and impact, or is simply de<sup>fi</sup>ned as the product of them. Many of these methods independently evaluate the characteristics of risks, and focus on the analysis of individual risks. Risks are usually listed and ranked by one or more parameters [5,12]. Generally, these methods do not take into account the subsequent in<sup>fl</sup>uence of risks and cannot represent the interrelation between them. We can also cite the creativity-based or the expertise-based techniques, like expert judgment using Delphi, af<sup>fi</sup>nity diagram, peer interviews or risk diagnosis methodology (RDM) [26–28].

To comprehensively understand a risk, it is helpful to identify its causes as well as its effects. Several methods include this principle, but they still concentrate on a single risk for simplifying the problem [11,21]. For instance, failure modes and effects analysis (FMEA) consists in a qualitative analysis of dysfunction modes followed by a quantitative analysis of their effects, in terms of probability and impact [7,33]; fault tree and cause tree analyses determine the conditions which lead to an event and use logical connector combinations [34]. These methods are unable to model complex interactions among different risks.

Few speci<sup>fi</sup>c methods are able to model risk correlations with a network structure. Several papers on the application of the Bayesian belief network (BBN) have appeared in recent years in the <sup>fi</sup>eld of project risk management [17,29], which could model risk interrelations, from multiple inputs to multiple outputs. Nevertheless, BBN demands oriented links, is inherently acyclic, and hence does not easily model the loop phenomenon; this oversight could potentially lead to a disaster in real projects. These methods are thus not always applicable for practical purpose and fail in some cases to represent the real complexity of the interdependencies among risks.

Therefore, to manage a project with complexly interrelated risks, it is important to <sup>fi</sup>rstly integrate the multiple dimensions of risks, including classical characteristics like probability and impact, and secondly to bring the modeling of risk interactions into the PRM process. Risk interactions should be modeled with a network structure instead of a classical list or tree structure for representing the real complexity of the project. In this paper, we propose an integrated framework for modeling and analyzing the risk network behavior to support decision-making for risk management. We use classical project risk list, which usually only takes into account the negative aspects of risks, as the inputs of the network model. Thus, this paper mainly focuses on the conventional risks with negative effects. Existing methods like the design structure matrix (DSM) for dependency modeling and the analytic hierarchy process (AHP) for pairwise comparison evaluation are employed to identify and evaluate risk interactions. Simulation technique is used to analyze propagation phenomena and to re-evaluate risks. The aim is to support decision-makers in planning risk response actions with a structured and repeatable approach.

The paper is organized as follows. Section 2 presents the framework of decision support system for risk management. Section 3 introduces the process of building the project risk network model. Section 4 describes the potential applications of this model to support managerial decision-making. An example of an application to a real project in the entertainment industry is presented in Section 5 to illustrate the proposed method. We conclude the paper in Section 6 with a discussion of the utility of the model and the perspective on the future work.

## 2. The framework of decision support system for PRM

Our framework is a decision support system (DSS) with <sup>fi</sup>ve phases: (1) risk network identi<sup>fi</sup>cation; (2) risk network assessment; (3) risk network analysis; (4) risk response planning; and (5) risk monitoring and control. Fig. 1 illustrates this framework. The innovative steps based on the classical risk management process and the new generated outcomes are highlighted in the <sup>fi</sup>gure.

In phase (1), potential project risks are identi<sup>fi</sup>ed by classical methods and the result is usually a project risk list. Based on this list, risk interactions are identi<sup>fi</sup>ed and represented using a matrixbased method. In phase (2) of the risk network assessment, the probability and impact of identi<sup>fi</sup>ed risks are evaluated by classical methods; then the strength of risk interactions is assessed with an AHP-based method, in terms of the causal probability between risks. One innovation of this framework is that in the <sup>fi</sup>rst two phases, in addition to project risks, risk interactions are also identi<sup>fi</sup>ed and evaluated. This makes it possible to construct the project risk network. In phase (3), the risk network is modeled and run in a discrete-event simulation context. This enables an analysis of the propagation behavior in the network and thus a re-evaluation of risks considering their correlations. Sensitivity analysis is also performed to enhance the reliability of the network analysis phase. The response planning phase (4) consists of three activities: (a) potential mitigation actions are identi<sup>fi</sup>ed according to the analytical results from the previous phase, and they are preliminarily evaluated by experts (some unfeasible actions can be screened out through this activity); (b) candidate actions are tested in the simulation model for estimating their effects on a speci<sup>fi</sup>c target or on the global risk network; and (c) mitigation actions are re-evaluated in terms of their effects, i.e., the level of residual risks that is expected to remain after the implementation of these actions. Then, the project manager makes decisions about the actions suggested by the system. Finally, the evolution of the risk network is monitored and the effectiveness of the actions is evaluated to keep the project under control. The phase of monitoring and control provides feedback for the previous phases, which allows the modi<sup>fi</sup>cation and improvement of their results.

![](/api/attachments/JG3CC9V5/fulltext/images/4d8f63a3edc47662e0c3e34e6030d8f1e20830fc333b885597d26828c509c91a.jpg)  
Fig. 1. Framework of the decision support system for PRM.

This decision support system for project risk management is a cooperative DSS [1,10,19]. Decision-makers (usually the project manager and the team of experts) are allowed to modify, complete, and re<sup>fi</sup>ne the managerial suggestions proposed by the system. It is also necessary for them to participate in each phase of risk management to provide their knowledge, expertise and experience.

## 3. Project risk network model

There are a number of methods for the classical steps of risk identi<sup>fi</sup>cation and risk analysis. These classical methods are used to study individual project risks. Their result, such as the project risk list, serves as the input to study risk interactions for building the risk network model.

## 3.1. Identification of risk network (phase 1)

Identi<sup>fi</sup>cation is the <sup>fi</sup>rst step of determining the cause–effect relationship between risks. The design structure matrix (DSM) method introduced by Steward [40] has proven to be a practical tool for representing and analyzing relations and dependencies among system components [8,15]. For our study, we use the concept of DSM with risks, in the context of project management. The interrelations between project objects such as tasks, actors and product components facilitate identifying the interrelations between the risks related to these objects. For instance, the project schedule gives information about task–task sequence relationships. This helps to identify the correlation between two risks of delay for these tasks. A component– component relationship (functional, structural or physical) means that the risks, which may be related to product functions, quality, delay or cost, can be linked, since one problem on one component may have an in<sup>fl</sup>uence on another (e.g., budget limits). In a similar way, the domain mapping matrix (DMM) introduced by Danilovic and Browning [15] and the multiple-domain matrix (MDM) introduced by Lindemann, Maurer and Braun [30] are helpful in identifying risk interactions across different domains of the project.

According to Thompson's study on relationships in the organizational structure [41], there are three basic types of relationships between each pair of risks:

▪ Dependent: risks are engaged in a potential precedence relationship.

▪ Interdependent: risks are engaged in a mutually dependent relation, directly or within a bigger loop.

▪ Independent: risks are not related.

A fourth type of activity relationship–contingent is introduced by Browning in [8]. The nature of interactions can also be classi<sup>fi</sup>ed into several categories. Multiple links with different natures might exist between two risks. They are expressed as a potential causal relationship between the risks.

Risk interaction is considered as the existence of a possible precedence relationship between two risks. We de<sup>fi</sup>ne the risk structure matrix (RSM), which is a binary and square matrix with $R S M _ { i j } = 1$ when there is a link from $R _ { j }$ to $R _ { i } .$ . It does not address concerns about the probability or impact assessment of this interaction. We put a sanity check between $R _ { i }$ and $R _ { j } .$ Suppose we know that R declared $R _ { j }$ as a cause, if $R _ { j }$ did not declare $R _ { i }$ as a consequence, then there is a mismatch. Each mismatch is studied and solved, like the analogous works by Sosa about the interactions between project actors [39]. Fig. 2 gives an example to show the use of such a RSM to represent the risk network.

![](/api/attachments/JG3CC9V5/fulltext/images/65e3adbe9bccca52880614d6bcb9d5396f49e5bdfaa42ed1de48d2dcab500787.jpg)  
Fig. 2. Illustration of risk structure matrix (RSM).

## 3.2. Assessment of risk network (phase 2)

In the assessment phase, the risk network parameters are evaluated, such as risk impact, spontaneous probability of risks and transition probability between risks.

## 3.2.1. Risk evaluation

As mentioned in the Introduction, risks are classically assessed in terms of probability and impact. Risk impact can be assessed on a qualitative scale (e.g., ordinal or cardinal scale with 5 or 10 levels) or on a quantitative scale (e.g., <sup>fi</sup>nancial loss). In this paper, we use classical methods for the impact assessment, based upon a mix of previous experience and expert judgment.

For the probability assessment, we make a distinction between the probability of a risk to be triggered by another risk inside the network and its probability caused by external events or risks which are outside the system. Spontaneous probability can be interpreted as the evaluated likelihood of a risk, which is not the effect from any other activated risks inside the system. Qualitative scales are often used to express probability with 5 to 10 levels (e.g., very rare, rare, unlikely, etc.) which correspond to non-linear probability measures (e.g., $1 0 ^ { - 4 } , 1 0 ^ { - 3 } , 1 0 ^ { - 2 } , \mathrm { { e t c . } ) }$ . Logarithmic scales have been used by statisticians for many decades [18]. They allow us to distribute probabilities unevenly. In practice, they devote more space to small values, imposing a compressed, logarithmic mapping. Based on this principle, we can use, for example, Eq. (1) for converting qualitative scales into quantitative measures of risk spontaneous probability:

$$
p = \alpha * 1 0 ^ {\left(\frac {- \beta}{s}\right)}\tag{1}
$$

where $p$ indicates the quantitative probability measure, s indicates the qualitative scale value, with parameters α>0, β>0.

## 3.2.2. Risk interactions evaluation

A numerical structure matrix can provide more detailed information than a binary one about the risk network for assisting decision-making. Evaluation is the process of measuring and estimating the strength of the link between risks. Two ways can be used for the estimation: direct assessment and relative assessment. Direct assessment is made for each potential interaction by one or more experts according to their experience and/or expertise. Relative assessment consists in comparing the causes (or the effects) of a single risk which has multiple interactions. This involves using the principle of pairwise comparisons in the analytic hierarchy process (AHP) developed by Saaty [37]. An AHP-based assessment has been developed by Marle to obtain the numerical values of the strength of risk interactions [31]. The main principles are introduced in the next paragraphs and displayed in Fig. 3.

![](/api/attachments/JG3CC9V5/fulltext/images/2a6e299a0f8d5694f7e3384763930cc74dd9797045af1019fa78767190f9b6d3.jpg)  
Fig. 3. Description of the transformation process from RSM to RNM.

• Step 1: Decomposing individual sub-problems For each risk $R _ { i } ,$ we isolate the risks which are related with $R _ { i }$ in column (possible effects) and in row (possible causes). This identi<sup>fi</sup> cation enables one to generate the Binary Cause (or Effect) Vectors, with regard to risk $R _ { i } ,$ respectively called BCV|R and BEV|R .

## • Step 2: Evaluating the relative strength

We build up two matrices (Cause or Effect Comparison Matrices) with regard to one risk $R _ { i }$ (respectively CCM|R and ECM|R ). The AHP is based on the use of pairwise comparisons, which lead to the elaboration of a ratio scale. In our case, we have two parallel pairwise comparison processes to run. The <sup>fi</sup>rst one consists in the ranking in rows for each project risk. The criterion according to which the alternatives are evaluated is the contribution to R in terms of risk input. In other words, for every pair of risks which are compared, $R _ { j }$ and $R _ { k }$ (thus following $\mathsf { R S M } _ { i j } = \mathsf { R S M } _ { i k } = 1 )$ , the user should assess which one is more important to risk $R _ { i }$ in terms of the probability of triggering $R _ { i } .$ These assessments are expressed by numerical values thanks to the use of traditional AHP scales. The second one is the ranking in columns, according to the same principles.

## • Step 3: Calculating the eigenstructures

Eigenvectors of each matrix ECM|R and CCM|R are now calculated. It enables one to <sup>fi</sup>nd the principal eigenvectors, corresponding to the maximal eigenvalue. They are called Numerical Cause or Effect Vectors and are relative to one risk $R _ { i }$ (NCV and NEV ). The consistency of the results should be tested thanks to the AHP consistency index.

## • Step 4: Aggregating the eigenvectors

For each risk R , Numerical Cause or Effect vectors (NCV and NEV) are respectively aggregated into Numerical Cause or Effect Matrices (NCM and NEM). The i-th row of NEM corresponds to the eigenvector of CCM|R which is associated to its maximum eigenvalue. The j-th column of NCM corresponds to the eigenvector of ECM|R which is associated to its maximum eigenvalue.

## • Step 5: Compiling the results

The two previous matrices are aggregated into a single Risk Numerical Matrix (RNM), the values of which assess the relative strength of local interactions. The RNM is de<sup>fi</sup>ned by a geometrical weighting operation in Eq. (2) (based on the assumption that both estimations in terms of cause and effect can be considered equivalent). We choose the geometrical mean rather than arithmetic mean because it tends to favor balanced values (between the two assessments). ${ \mathrm { R N M } } _ { i j }$ is de<sup>fi</sup>ned as the strength of the cause and effect interaction from R to R .

$$
R N M (i, j) = \sqrt {N C M (i , j) \times N E M (i , j)}, \forall (i, j), 0 \leq R N M (i, j) \leq 1\tag{2}
$$

The RNM thus permits to synthesize the existence and strength of local precedence relationships between risks, as it combines the cause-oriented vision and the consequence-oriented vision of an interaction. This is helpful to avoid any bias or misevaluation which can happen when looking at the problem with single vision. In the risk network model, numerical values of cause–effect interactions in the RNM can also be interpreted as the transition probability between risks. For example, if the element RNM(4,3) is equal to 0.25, then the probability of risk 4 originating from risk 3 is considered to be 25% under the condition that risk 3 is activated.

## 4. Applications to support managerial decision-making

This section presents an analysis of the risk network (Section 4.1) based on the data gathered in Section 3. The results of this analysis help the project manager make decisions about risk mitigation actions (Section 4.2). Finally, the risks and the effects of actions are monitored in order to keep the project under control (Section 4.3).

## 4.1. Risk network analysis (phase 3)

It is dif<sup>fi</sup>cult to calculate the risk propagation in the network, especially with complex phenomena like loops. Furthermore, in the context of project management, it is costly and unfeasible to carry out concrete experimental studies on projects. Simulation is an alternative tool for empirical research in DSS [3]. Nowadays, simulation has become more popular and powerful than ever since computer and software technologies have signi<sup>fi</sup>cantly developed. Simulation techniques are widely used to build model-driven decision support systems [36]. They assist decision-maker in anticipating the effects of events, actions and resource allocations by assessing their potential consequences. Therefore, in this research, we model and analyze the project risk network through simulation using the software ARENA. ARENA is a powerful and widely used simulation tool in industry. It is suitable for modeling complex system and simulating discrete events.

Modeling risk interactions in simulation enables us to analyze the propagation behavior in the risk network. A large number of iterations are conducted for each scenario of simulation. The occurrence of every risk is recorded during the simulation. The simulation results can be analyzed to support decision-making for risk management.

## 4.1.1. Risk re-evaluation

After taking into account the risk propagation behavior, risk probability can be re-evaluated and expressed as statistical risk frequency in the simulation. In practice, a risk could occur more than once during one replicate of the project simulation. This is consistent with the real-life situations. Simulated frequency represents the average occurrence of a risk during the project, which may be greater than 1. The relationship between simulated risk frequency and risk probability is expressed in Eq. (3):

$$
R F [ i ] = P _ {1} (R _ {i}) + 2 \cdot P _ {2} (R _ {i}) + 3 \cdot P _ {3} (R _ {i}) + \dots = \lim _ {m \rightarrow \infty} \sum_ {k = 1} ^ {m} k \cdot P _ {k} (R _ {i})\tag{3}
$$

where RF[i] indicates the simulated risk frequency of $R _ { i } ,$ and $P _ { k } ( R _ { i } )$ indicates the probability of $R _ { i }$ occurring k times during the project.

The simulation model can also be used to anticipate the consequences of one particular risk or a certain scenario. We simulate the scenario by setting the appointed spontaneous probability of certain risks, and then all the potential consequences of this scenario can be observed after simulation. For example, if we assign 100% spontaneous probability to one risk while all the other risks have the value of 0%, then the simulation shows both its direct and indirect impacts on other risks in the network. The consequences of a risk are de<sup>fi</sup>ned in Eq. (4) for re-evaluating its impact in the global scope:

$$
C R [ i ] = \sum_ {j = 1} ^ {n} R F ^ {i} [ j ] \cdot R I [ j ]\tag{4}
$$

Here $C R [ i ]$ is the consequences of $R _ { i } ,$ and $R F ^ { i } [ j ]$ indicates the simulated risk frequency of $R _ { j }$ originating from $R _ { i } , R [ [ j ]$ is the evaluated risk impact of $R _ { j } ,$ which may be expressed on qualitative or quantitative scales, as mentioned in Section 3.2.1.

The local criticality of a risk can be re-evaluated by multiplying its simulated frequency and its local evaluated impact, as in the following equation:

$$
L C [ i ] = R F [ i ] \cdot R I [ i ]\tag{5}
$$

In a similar way, we can re<sup>fi</sup>ne the estimation of risk criticality by incorporating all the consequences of the risk in the network. The simulated global criticality of R is de<sup>fi</sup>ned by Eq. (6):

$$
G C [ i ] = R F [ i ] \cdot C R [ i ]\tag{6}
$$

## 4.1.2. Risk prioritization

In the process of PRM, risk prioritization is relied on to plan response actions. We simulate the risk propagation in the network to obtain different indicators for risk prioritization, such as the re<sup>fi</sup>ned risk frequency and criticality. The prioritization results based on the re-evaluated indicators provide the project manager with a new understanding of risks and their relative severity in the project. The shift of risk prioritization also in<sup>fl</sup>uences the planning of mitigation actions.

## 4.1.3. Sensitivity analysis

Uncertainties exist in the assessment phase of evaluating risks and risk interactions. The reliability of analysis results therefore needs to be considered. Sensitivity analysis regards the study of the behavior of a model to ascertain how much its outputs depend on the input parameters [38]. In this respect, sensitivity analysis is performed to examine the effects of input uncertainties on the outputs. For example, we evaluate risks with three-level spontaneous probabilities (optimistic, most likely, and pessimistic value). Depending on the varying input values, the corresponding criticality of each risk is obtained. Sensitivity analysis is a useful tool of DSS to verify the <sup>fi</sup>nal ranking of the alternatives [32]. It helps to enhance the robustness of the system and the reliability of its managerial suggestions.

## 4.2. Mitigation action planning and test (phase 4)

In project risk management, mitigation is an important and common treatment strategy to reduce local or global risk exposure. Taking early action to reduce the probability and/or impact of a risk occurring on the project is often more effective than trying to repair the damage after the risk has occurred [35]. In classical methods, courses of action are carried out on risks having the highest ranking or priority, in other words, on risks with the highest criticality. These actions are in practice, for instance, internal or external communication actions, training of members, buying additional or superior material resources, choosing a cheaper, more stable or closer supplier, or increasing the number of tests. Mitigation actions always consume time, money and resources. It requires a leader, or at least one project member accountable for them. They should be included in the project plan like every action contributing to the delivery of the project result.

Based on the simulation analysis of the risk network, we get the risk re-evaluation and new prioritization results. Hence, a new risk response plan can be developed. The new actions include: (1) classical mitigation actions, but applied to risks with re-evaluated values and rankings (simulated values may be different from initial estimated values); (2) non-classical mitigation actions, which mitigate risk propagation instead of risk occurrence. Strategies for mitigating risks in different categories are likely to be different. For example, risks without any input while leading to many outputs are likely to be source risks; risks with many inputs as well as many outputs can be considered as transition risks in a project; risks without output are accumulation risks, often related to project performance like schedule, cost or quality. In addition to the scope of local target on one or several speci<sup>fi</sup>c risks, mitigation actions could also be proposed to achieve global effects on the risk network.

In the simulation model, different kinds of mitigation actions can be tested by changing the values of the parameters, so that the effects on a part of or on the global risk network can be observed. For a particular risk, classical mitigation action is conducted by giving the risk a lower spontaneous probability without considering its interactions with other risks. A complementary preventive action is cutting off the input links or reducing their transition probability. This strategy is compatible with the accumulation or transition risks. Instead of acting on a risk, the action focuses on the sources of this risk. For instance, the choice of suppliers and the communication plan are potential sources of many risks in the project, so that paying enough attention to these points at the beginning of the project may help to avoid many subsequent risks. Blocking the output links of a risk can be regarded as the action for con<sup>fi</sup>ning its further propagation in the network. This is suitable for the source and transition risks. Instead of acting on the risk, the action focuses on its consequences. For instance, even if it is not possible (or would involve huge overcosts) to avoid a small delay in the delivery of a part in a civil engineering project, it is possible to negotiate a contract in which the penalties will begin at a higher threshold. We do not avoid this risk, since uncertainty is inherent in this work, but we implement an action to avoid its propagation and ampli<sup>fi</sup>cation to the rest of the project.

## 4.3. Risk network monitoring and control (phase 5)

Planned risk response actions are executed during the project, but their performance needs to be measured, in order to make sure that they have the desired effects on risks, while not inducing secondary effects. Moreover, the project, its environment and therefore the risks in the network, are continuously evolving. The status of the risk network should thus be continuously monitored throughout the project. Risk network monitoring and control could result in periodic risk reviews, identi<sup>fi</sup>cation of new risks, and reporting on response action performance and any unanticipated effects. This phase provides feedback for the previous phases of the DSS. The project manager can use this information to modify the risk network structure and its parameters in phases 1 and 2, to update the risk analysis reporting in phase 3, and to amend the response plan in phase 4.

## 5. An illustrative example

In this section, we illustrate the application of our method to a project of staging a musical show in Paris, France. The project is the production of a family musical show, including costumes, lightning and sound design, casting management, rehearsal management, fund raising and overall project management. The duration of the project is 15 months and the team is composed of 18 people, plus the actors and actresses. The following analysis shows the implementation and the results of the DSS in each phase of project risk management.

## 5.1. Phases 1 and 2: risk network modeling

The <sup>fi</sup>rst action consisted in interviewing the persons directly involved in the project risk management process, namely the risk owners and the project manager. These participants were given a short background questionnaire on their experience in the organization and in this kind of project. They were also given a presentation of the method, including the analysis that will be made using the input data they were going to provide. To avoid potential differences among interviewers and their interviewing techniques, only one interviewer was used for all the interviews. Through the interviews and meetings we were able to perform the identi<sup>fi</sup>cation and assessment of risks and risk interactions. During the <sup>fi</sup>nal meeting, the evaluations were exposed and discussed by all the participants. Some changes were made during the discussion and a consensus was reached at the meeting, which lasted about three hours. As a whole, three weeks were needed to build up the RNM.

In every identi<sup>fi</sup>cation process, there is a limit to the scope when considering risks inside or outside the project risk list. Downstream limits are generally the <sup>fi</sup>nal expected project results, which may include immediate results like pro<sup>fi</sup>t, delivery time or post-project results related to operation, maintenance or recycling phase. Upstream limits are generally decided depending on the in<sup>fl</sup>uence or capacity of actions that the decision-makers have on these causes. The identi<sup>fi</sup>cation of risk interactions has been done on direct cause or effect relationship. In the end, the aggregation of local cause–effect relationships made it possible to display the global project risk network. This permitted us to organize a meeting where the interviewees had the possibility to add or remove nodes and edges in the risk network.

The assessment of risks was then performed using the 10-level qualitative scale; and the strength of risk interactions was assessed using a developed AHP-based method, as described in Section 3.2.2. Due to the high level of expertise of interviewees, this step was done quite quickly (for several hours, including the interviews and two meetings). In order to get the spontaneous probability, they supposed that none of the identi<sup>fi</sup>ed cause would occur and then they were asked: “what is the remaining probability of this event to occur?” Qualitative probability is converted into numerical probability through Eq. (1), where the parameters are set as $\alpha = 5 , \beta = 8$ by experience. The only dif<sup>fi</sup>culty was that it appeared easier for the risk owners to consider the interactions with causes that could affect them, than to consider the interactions with effects of their own actions and decisions. But this potential bias was <sup>fi</sup>xed by the meetings and the simultaneous presence of the different correlated owners. This approach enabled us to get the consistency on both the existence and the assessment of each interaction, because the two involved owners (respectively for the cause and effect risks) were present.

The left part of Table 1 shows the risk names and their initial evaluated characteristics. Fig. 4 displays the risk numerical matrix with evaluated transition probability of the risk interactions. For instance, in the (7,11)-th item of the matrix, the value 0.327 denotes that the transition probability from risk 11 (Bad scenic, lightning and sound design) to risk 7 (Cancellation or delay of the <sup>fi</sup>rst performance) is 32.7%.

Even with a mix of individual and collective work, misjudgments are possible and the estimations remain uncertain or unreliable. This is all the more true that we are not in a context with lots of experience, where estimations could be considered as quite reliable. This is why we decided to run the sensitivity analysis, in order to consider the uncertainties on the inputs and their in<sup>fl</sup>uence on the outputs. This work is detailed at the end of Section 5.2.

## 5.2. Phase 3: risk network analysis

In the simulation, one important question is: “how many iterations are needed to reach a chosen level of precision of the results?” Ref. [6] gives some formulas that can be used to estimate a minimal number of iterations. While for our study, it is dif<sup>fi</sup>cult to estimate a satisfactory number of iterations because it depends on the size and the complexity of the risk network (particularly the in<sup>fl</sup>uence of loops). However, we can still accomplish suf<sup>fi</sup>cient runs by increasing the number of iterations until the output, namely the simulated risk frequency, become stable enough.

In the case study, we increase the number of simulation iterations gradually from 1000, 2000, … , to 10 000. The criterion for evaluating the stability of the output is de<sup>fi</sup>ned as the following equation:

$$
\sum_ {i = 1} ^ {n} \Delta R F [ i ] ^ {2} <   T h r e s h o l d\tag{7}
$$

where ΔRF[i] indicates the deviation of the simulated frequency of Risk i with the previous simulation. The threshold is set to be $1 0 ^ { - 6 }$ in the test, which ensures that the output deviation with regard to each risk does not exceed $1 0 ^ { - 3 }$ . The criterion is always achieved after 6000 iterations. For statistical and computational convenience, 10 000 iterations are conducted in each scenario of the risk network model. The simulation time is not a limiting factor, since it costs less than 5 min for 10 000 iterations using the software ARENA on a normal PC.

The propagation behavior in the risk network is analyzed as discussed in Sections 4.1.1 and 4.1.2. In Table 1, we consolidate the re-evaluation results of risks, and compare them with the results of classical method.

Based on the results in Table 1, risks are prioritized by different indicators, shown in Table 2. It gives a different insight on risk priorities due to the changes in risk evaluations and risk rankings.

Eckert and co-authors de<sup>fi</sup>ned (in the context of change propagation in design projects) the four following categories of risks: constants, absorbers, carriers and multipliers [16]. Some risks appear to be high accumulation risks, or “absorbers”, notably the risks R10

Project risk list and the comparison of re-evaluated simulation results with those of classical method.

<table><tr><td rowspan="2">Risk ID</td><td rowspan="2">Risk name</td><td rowspan="2">Nature</td><td colspan="5">Evaluation results by classical method</td><td colspan="4">Re-Evaluation Results by Simulation</td></tr><tr><td>Qualitative probability (evaluated)</td><td>Spontaneous probability (Eq. (1))</td><td>Qualitative impact (evaluated)</td><td>Qualitative criticality (QP*QI)</td><td>Evaluated criticality (SP*QI)</td><td>Simulated frequency (Statistic)</td><td>Consequences of risk (Eq. (4))</td><td>Simulated local criticality (Eq. (5))</td><td>Simulated global criticality (Eq. (6))</td></tr><tr><td>R01</td><td>Low budget</td><td>Cost and time</td><td>8</td><td>0.500</td><td>7</td><td>56</td><td>3.50</td><td>0.807</td><td>32.07</td><td>5.65</td><td>25.88</td></tr><tr><td>R02</td><td>Infractions against law</td><td>Contract</td><td>7</td><td>0.360</td><td>5</td><td>35</td><td>1.80</td><td>0.696</td><td>17.46</td><td>3.48</td><td>12.15</td></tr><tr><td>R03</td><td>Low communication and advertising for the show</td><td>User/ customer</td><td>8</td><td>0.500</td><td>9</td><td>72</td><td>4.50</td><td>0.771</td><td>12.36</td><td>6.94</td><td>9.53</td></tr><tr><td>R04</td><td>Unsuitable cast</td><td>Organization</td><td>5</td><td>0.126</td><td>9</td><td>45</td><td>1.13</td><td>0.495</td><td>15.53</td><td>4.45</td><td>7.69</td></tr><tr><td>R05</td><td>Unsuitable ticket price-setting</td><td>Strategy</td><td>7</td><td>0.360</td><td>6</td><td>42</td><td>2.16</td><td>0.364</td><td>31.19</td><td>2.18</td><td>11.36</td></tr><tr><td>R06</td><td>Unsuitable rehearsal management</td><td>Controlling</td><td>3</td><td>0.011</td><td>8</td><td>24</td><td>0.09</td><td>0.266</td><td>13.89</td><td>2.13</td><td>3.69</td></tr><tr><td>R07</td><td>Cancellation or delay of the first performance</td><td>Cost and time</td><td>5</td><td>0.126</td><td>8</td><td>40</td><td>1.01</td><td>0.425</td><td>15.40</td><td>3.40</td><td>6.55</td></tr><tr><td>R08</td><td>Poor reputation</td><td>User/ customer</td><td>3</td><td>0.011</td><td>7</td><td>21</td><td>0.08</td><td>0.388</td><td>8.73</td><td>2.72</td><td>3.39</td></tr><tr><td>R09</td><td>Lack of production teams organization</td><td>Organization</td><td>4</td><td>0.050</td><td>6</td><td>24</td><td>0.30</td><td>0.049</td><td>17.62</td><td>0.29</td><td>0.85</td></tr><tr><td>R10</td><td>Low team communication</td><td>Organization</td><td>3</td><td>0.011</td><td>6</td><td>18</td><td>0.07</td><td>0.529</td><td>19.11</td><td>3.18</td><td>10.11</td></tr><tr><td>R11</td><td>Bad scenic, lightning and sound design</td><td>Technical performance</td><td>2</td><td>0.001</td><td>7</td><td>14</td><td>0.01</td><td>0.393</td><td>12.07</td><td>2.75</td><td>4.75</td></tr><tr><td>R12</td><td>Bad costume design</td><td>Technical performance</td><td>3</td><td>0.011</td><td>8</td><td>24</td><td>0.09</td><td>0.400</td><td>13.50</td><td>3.20</td><td>5.40</td></tr><tr><td>R13</td><td>Low complicity between cast members</td><td>Technical performance</td><td>3</td><td>0.011</td><td>7</td><td>21</td><td>0.08</td><td>0.383</td><td>13.94</td><td>2.68</td><td>5.34</td></tr><tr><td>R14</td><td>Too ambitious artistic demands compared to project means</td><td>Requirements</td><td>7</td><td>0.360</td><td>2</td><td>14</td><td>0.72</td><td>0.445</td><td>7.88</td><td>0.89</td><td>3.51</td></tr><tr><td>R15</td><td>Few spectators/lukewarm reception of the show</td><td>User/ customer</td><td>2</td><td>0.001</td><td>9</td><td>18</td><td>0.01</td><td>0.196</td><td>15.88</td><td>1.76</td><td>3.11</td></tr><tr><td>R16</td><td>Technical problems during a performance</td><td>Technical performance</td><td>4</td><td>0.050</td><td>5</td><td>20</td><td>0.25</td><td>0.191</td><td>7.07</td><td>0.96</td><td>1.35</td></tr><tr><td>R17</td><td>Low cast motivation</td><td>Organization</td><td>2</td><td>0.001</td><td>4</td><td>8</td><td>0.00</td><td>0.469</td><td>8.63</td><td>1.88</td><td>4.05</td></tr><tr><td>R18</td><td>Unsuitable for family audiences</td><td>Strategy</td><td>2</td><td>0.001</td><td>5</td><td>10</td><td>0.01</td><td>0.002</td><td>7.84</td><td>0.01</td><td>0.01</td></tr><tr><td>R19</td><td>Low creative team leadership</td><td>Controlling</td><td>3</td><td>0.011</td><td>10</td><td>30</td><td>0.11</td><td>0.014</td><td>17.43</td><td>0.14</td><td>0.24</td></tr><tr><td>R20</td><td>Low creative team reactivity</td><td>Controlling</td><td>2</td><td>0.001</td><td>2</td><td>4</td><td>0.00</td><td>0.001</td><td>7.91</td><td>0.00</td><td>0.01</td></tr></table>

(Low team communication) and R17 (Low cast motivation). This can be seen in Fig. 4 with an important number of inputs (in rows) for these risks. The changes on the risk occurrence assessment are visible in Tables 1 and 2, both in the absolute value and in terms of ranking. The risks of this kind are unlikely to occur spontaneously, but some other identi<sup>fi</sup>ed risks may lead to them. Some risks have been moderately anticipated by the classical method, but they are still to some extent underestimated, such as R4 (Unsuitable cast) and R7 (Cancellation or delay of the <sup>fi</sup>rst performance). Overall, a number of risks have increased occurrence frequency in varying degrees, which re<sup>fl</sup>ect their intensity of interactions in the network.

On the contrary, some risks engender many paths in the risk network. For example, R01 (Low budget), R02 (Infractions against law) and R10 (Low team communication) are called “multipliers” and they may be the original cause of numerous undesired effects. Their direct consequences (in columns) can be seen in Fig. 4, but their global consequences in the network are only visible in Tables 1 and 2, with the gap between classically evaluated impacts and simulated consequences of the risks. Among these risks, R02 and R10 are some of the “leverage points” which are initially underestimated with low impact, nevertheless they should be mitigated because they have a large potential to trigger other risks. R05 (Unsuitable ticket price-setting) is another example of the “leverage points”, which does not have numerous direct outputs but has a high impact on some important risks like R01 (Low budget), with RNM(1,5)=0.770.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td>0.770</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.159</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>0.410</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>0.243</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.137</td><td>0.391</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>0.164</td><td>0.337</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.471</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.372</td><td>0.115</td></tr><tr><td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.197</td><td></td><td>0.327</td><td>0.346</td><td></td><td></td><td></td><td>0.139</td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td></td><td>0.311</td><td></td><td></td><td></td><td></td><td>0.287</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.193</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td></td><td>0.153</td><td>0.118</td><td>0.217</td><td></td><td>0.301</td><td>0.183</td><td></td><td>0.129</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.108</td><td></td><td></td><td></td></tr><tr><td>11</td><td>0.415</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.129</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>0.415</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.129</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td></td><td></td><td></td><td>0.173</td><td></td><td></td><td></td><td></td><td></td><td>0.394</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.175</td><td></td><td>0.154</td><td></td></tr><tr><td>14</td><td>0.106</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.203</td></tr><tr><td>15</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.311</td><td>0.157</td><td></td><td></td><td></td><td>0.184</td><td></td><td></td></tr><tr><td>16</td><td>0.164</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17</td><td></td><td>0.186</td><td>0.116</td><td></td><td></td><td></td><td>0.159</td><td></td><td>0.170</td><td>0.146</td><td></td><td></td><td>0.252</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.352</td></tr><tr><td>19</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. Risk numerical matrix of the project.

Table 2  
Risk prioritization results by different indicators.

<table><tr><td rowspan="2">Ranking</td><td colspan="2">By spontaneous probability</td><td colspan="2">By simulated frequency</td><td colspan="2">By evaluated criticality</td><td colspan="2">By simulated global criticality</td></tr><tr><td>Risk ID</td><td>Value</td><td>Risk ID</td><td>Value</td><td>Risk ID</td><td>Value</td><td>Risk ID</td><td>Value</td></tr><tr><td>1</td><td>R01</td><td>0.500</td><td>R01</td><td>0.807</td><td>R03</td><td>4.50</td><td>R01</td><td>25.88</td></tr><tr><td>2</td><td>R03</td><td>0.500</td><td>R03</td><td>0.771</td><td>R01</td><td>3.50</td><td>R02</td><td>12.15</td></tr><tr><td>3</td><td>R02</td><td>0.360</td><td>R02</td><td>0.696</td><td>R05</td><td>2.16</td><td>R05</td><td>11.36</td></tr><tr><td>4</td><td>R05</td><td>0.360</td><td>R10</td><td>0.529</td><td>R02</td><td>1.80</td><td>R10</td><td>10.11</td></tr><tr><td>5</td><td>R14</td><td>0.360</td><td>R04</td><td>0.495</td><td>R04</td><td>1.13</td><td>R03</td><td>9.53</td></tr><tr><td>6</td><td>R04</td><td>0.126</td><td>R17</td><td>0.469</td><td>R07</td><td>1.01</td><td>R04</td><td>7.69</td></tr><tr><td>7</td><td>R07</td><td>0.126</td><td>R14</td><td>0.445</td><td>R14</td><td>0.72</td><td>R07</td><td>6.55</td></tr><tr><td>8</td><td>R09</td><td>0.050</td><td>R07</td><td>0.425</td><td>R09</td><td>0.30</td><td>R12</td><td>5.40</td></tr><tr><td>9</td><td>R16</td><td>0.050</td><td>R12</td><td>0.400</td><td>R16</td><td>0.25</td><td>R13</td><td>5.34</td></tr><tr><td>10</td><td>R06</td><td>0.011</td><td>R11</td><td>0.393</td><td>R19</td><td>0.11</td><td>R11</td><td>4.75</td></tr><tr><td>11</td><td>R08</td><td>0.011</td><td>R08</td><td>0.388</td><td>R06</td><td>0.09</td><td>R17</td><td>4.05</td></tr><tr><td>12</td><td>R10</td><td>0.011</td><td>R13</td><td>0.383</td><td>R12</td><td>0.09</td><td>R06</td><td>3.69</td></tr><tr><td>13</td><td>R12</td><td>0.011</td><td>R05</td><td>0.364</td><td>R08</td><td>0.08</td><td>R14</td><td>3.51</td></tr><tr><td>14</td><td>R13</td><td>0.011</td><td>R06</td><td>0.266</td><td>R13</td><td>0.08</td><td>R08</td><td>3.39</td></tr><tr><td>15</td><td>R19</td><td>0.011</td><td>R15</td><td>0.196</td><td>R10</td><td>0.07</td><td>R15</td><td>3.11</td></tr><tr><td>16</td><td>R11</td><td>0.001</td><td>R16</td><td>0.191</td><td>R15</td><td>0.01</td><td>R16</td><td>1.35</td></tr><tr><td>17</td><td>R15</td><td>0.001</td><td>R09</td><td>0.049</td><td>R11</td><td>0.01</td><td>R09</td><td>0.85</td></tr><tr><td>18</td><td>R17</td><td>0.001</td><td>R19</td><td>0.014</td><td>R18</td><td>0.01</td><td>R19</td><td>0.24</td></tr><tr><td>19</td><td>R18</td><td>0.001</td><td>R18</td><td>0.002</td><td>R17</td><td>0.00</td><td>R18</td><td>0.01</td></tr><tr><td>20</td><td>R20</td><td>0.001</td><td>R20</td><td>0.001</td><td>R20</td><td>0.00</td><td>R20</td><td>0.01</td></tr></table>

The risk prioritization results have changed after the simulation. Several risks have increased in the ranking in terms of frequency or criticality, while several other risks have decreased. For example, in the classical method, R03 (Low communication and advertising for the show) was considered to be the most critical risk, but the one with the highest simulated global criticality is R01 (Low budget). The value gap between risks has also changed. For example, R02 (Infractions against law) and R04 (Unsuitable cast) are evaluated with similar criticality. After re-evaluated by the simulation, R02 is still ranked above R04, and the relative gap between them has widened. This is the opposite situation for R05 (Unsuitable ticket price-setting) and R10 (Low team communication): R10 is still behind R05, but closer.

Our focus is then what Eckert and co-workers de<sup>fi</sup>ned as the “avalanches”, i.e., the unpredictable propagation of initial events [16]. They and other co-authors also discussed some patterns de<sup>fi</sup>ning local propagation motifs and de<sup>fi</sup>ning relationships between two or three elements [20]. We are focusing on more global patterns, which are potentially the combinations of the local ones, like long propagation chains, heterogeneous propagation chains and loops. In these three cases, the anticipation and then the decision-making are very hard, because of the dif<sup>fi</sup>culty to connect elements with different natures of risks, different actors, and different occurrence times.

Regarding the uncertainties of the estimated input values for the simulation, the spontaneous probability of each risk is assessed by the experts with three-level values: optimistic, most likely, and pessimistic, shown in Table 3.

Sensitivity analysis is performed on the three-level values of spontaneous probability. Each risk has a dissimilar range of simulated global criticality, as shown in Fig. 5. For example, R02 (Infractions against law) and R05 (Unsuitable ticket price-setting) have similar most likely values of criticality, but R05 has a larger potential range and thus it could be more unstable in the project. With respect to the risk prioritization, in all situations, R01 (Low budget) has higher simulated criticality than R02. Prioritized by the most likely value,

Table 3  
Evaluated three-level values of risk spontaneous probability.

<table><tr><td rowspan="2">Risk ID</td><td colspan="3">Spontaneous probability</td></tr><tr><td>Optimistic</td><td>Most likely</td><td>Pessimistic</td></tr><tr><td>R01</td><td>0.450</td><td>0.500</td><td>0.950</td></tr><tr><td>R02</td><td>0.100</td><td>0.360</td><td>0.600</td></tr><tr><td>R03</td><td>0.350</td><td>0.500</td><td>0.650</td></tr><tr><td>R04</td><td>0.010</td><td>0.126</td><td>0.200</td></tr><tr><td>R05</td><td>0.250</td><td>0.360</td><td>0.700</td></tr><tr><td>R06</td><td>0.005</td><td>0.011</td><td>0.200</td></tr><tr><td>R07</td><td>0.010</td><td>0.126</td><td>0.150</td></tr><tr><td>R08</td><td>0.010</td><td>0.011</td><td>0.100</td></tr><tr><td>R09</td><td>0.010</td><td>0.050</td><td>0.200</td></tr><tr><td>R10</td><td>0.010</td><td>0.011</td><td>0.050</td></tr><tr><td>R11</td><td>0.001</td><td>0.001</td><td>0.020</td></tr><tr><td>R12</td><td>0.005</td><td>0.011</td><td>0.020</td></tr><tr><td>R13</td><td>0.005</td><td>0.011</td><td>0.100</td></tr><tr><td>R14</td><td>0.100</td><td>0.360</td><td>0.900</td></tr><tr><td>R15</td><td>0.000</td><td>0.001</td><td>0.100</td></tr><tr><td>R16</td><td>0.045</td><td>0.050</td><td>0.070</td></tr><tr><td>R17</td><td>0.000</td><td>0.001</td><td>0.050</td></tr><tr><td>R18</td><td>0.000</td><td>0.001</td><td>0.002</td></tr><tr><td>R19</td><td>0.005</td><td>0.011</td><td>0.012</td></tr><tr><td>R20</td><td>0.000</td><td>0.001</td><td>0.002</td></tr></table>

R02 is superior to R03 (Low communication and advertising for the show); nevertheless, under certain circumstances, R03 will lead to higher impact and be more critical than R02.

## 5.3. Phase 4: mitigation actions planning and test

The simulation-based model allows the project manager to test the proposed actions before the implementation in order to get the anticipation of their impacts on the network. The presented examples of actions are to achieve two different goals: the local mitigation of particular risks, and the global risk exposure mitigation of the risk network. This is a prototype which does not take into account all the desired information about the action, including its cost and its dif-<sup>fi</sup>culty or feasibility of implementation.

## 5.3.1. Local mitigation

In the simulation results of the case study (Table 2), we <sup>fi</sup>nd that some risks had a signi<sup>fi</sup>cant increase in terms of frequency and ranking, such as R10 (Low team communication) and R17 (Low cast motivation). For mitigating their occurrence, there are different possible strategies, which are displayed in Table 4. In the <sup>fi</sup>rst place, if we only apply classical actions by reducing their spontaneous probability to 0% (we suppose that the spontaneous probability can be reduced to 0% for the test in the prototype simulation model), R10 and R17 still have high simulated frequencies at the value of 0.516 and 0.468 respectively. In fact, the increase of simulated frequency is due to their input links from other risks. This explains why we design and test the non-classical actions on the risk interactions. By cutting several of their input links (links from R03, R04 and R07 to R10, and links from R03, R10 and R13 to R17), the frequency of these “absorber” risks has decreased a lot, shown in Table 4. For instance, acting on the transition between R13 (Low complicity between cast members) and R17 (Low cast motivation) may involve <sup>fi</sup>nding other motivation drivers which make the cast less sensitive to team complicity. This new action on the link is different from reducing the occurrence of R13, for example, by proposing team-building activities.

![](/api/attachments/JG3CC9V5/fulltext/images/4db31421fe138ae4e5c1d7782e07080f2ac3c19b093135dffd873ac0a447dab2.jpg)  
Fig. 5. Sensitivity analysis results of project risks.

Table 4  
Effects of different mitigation actions on particular risks.

<table><tr><td rowspan="2">Risk ID</td><td rowspan="2">Simulated risk frequency</td><td colspan="2">Simulated frequency after taking action</td></tr><tr><td>Classical mitigation actions on risks</td><td>New mitigation actions on risk interactions</td></tr><tr><td>R10</td><td>0.529</td><td>0.516</td><td>0.194</td></tr><tr><td>R17</td><td>0.469</td><td>0.468</td><td>0.205</td></tr></table>

## 5.3.2. Global mitigation

With regard to the global risk network, R03 (Low communication and advertising for the show) has the highest evaluated criticality using the classical method. In the simulation analysis, R01 (Low budget) becomes the top risk in terms of global criticality. Some mitigation actions are devised and tested in the risk network model. Fig. 6 compares their effects on the global risk network, i.e., the residual simulated frequency of all the risks after the action is conducted. Action 1 mitigates R03 according to the classical analysis; action 2 mitigates R01 based on the new prioritization by the simulation model; in the third action, a new action is executed by cutting the link from R05 (Unsuitable ticket price-setting) to R01 (Low budget), together with the classical action 2 on R01. Concretely, this could be done by increasing the part of the budget which comes from sponsorship and external investors, independently of the sales income. The <sup>fi</sup>nancial risk is then shared with different stakeholders. Even if the incomes from ticket presales are lower, this approach still ensures the normal operation of the project, while not to get the project stalled or to induce other risks for lack of funds. In this prototype model for mitigation actions test, we make the assumption that the risk interaction can be completely cut off, i.e., the transition probability can be reduced to 0%.

The results in Fig. 6 demonstrate the effectiveness of applying the risk network model to support mitigation actions planning.

![](/api/attachments/JG3CC9V5/fulltext/images/0149fc9448fefed53020f6871060cc25b9d5eff2b8c6b0a22b35d6e6fed2c829.jpg)  
Fig. 6. Comparison of effects on the global risk network by applying different mitigation actions.

## 5.4. Phase 5: monitoring and contro

The sensitivity analysis results demonstrate the impact of uncertainties in the assessment phase on the subsequent analysis phase. In addition, there exist potential changes in the project and uncertainties in the external environment as the project advances. Therefore, considering the reliability of the analysis results and the uncertainties in the later phases of the project, the risk network should be monitored after the implementation of actions, and the response plans will be modi<sup>fi</sup>ed and improved. With regard to the current example, this study took place at the end of the project in order to verify the usefulness of the developed prototype of DSS. The application of the monitoring phase will be included in future real-time case studies.

## 6. Conclusions and perspective

This paper has presented an interactions-based risk network model using advanced simulation. The model addresses the limitations of current methods regarding modeling complexity in project risk management. The performance of the model and the satisfaction of the users are validated by the project manager and the associated experts with whom we cooperated for the application to a real musical show project. The DSS enables the project manager to save time for designing risk response plan, and to reduce the cost of dealing with contingencies. Proactive risk management can be achieved by monitoring the status of the risk network and adjusting the risk mitigation plan as the project progresses.

The integrated DSS framework provides the project manager with a structured procedure and a series of methods to model, analyze and control the risk network. The project manager and the team of experts are involved throughout the whole process of the DSS to construct the risk network model and decide the risk response plans. Through modeling the propagation behavior in the project risk network, the model enables the project manager to gain innovative insights into the risks, into the relationships between them, and into the global risk network behavior. The re<sup>fi</sup>ned risk analysis and prioritization results support the project manager in making decisions, for instance, reassigning the risk ownership and planning more effective mitigation actions. The model is also useful for testing and evaluating the proposed action plans. In addition to the examples of actions tested in Section 5.3, a complete list of mitigation actions is proposed to the project manager based on the DSS. The project manager is able to choose a portfolio of actions to manage the project risks.

The selected case study analyzes a number of typical risks in a project of staging a musical show. Moreover, the approach manipulates values of risks and risk interactions, independently of their nature, their number and the type of project. In the risk management of any kind of project, generally risks are all assessed in terms of probability and impact, which are here included in the simulation model. This is why the approach can be generalized and applied to a much wider set of projects. Since the model uses matrix-based and simulation-based methods, the approach is possible to be applied in some very complex situations.

There are some limitations and potential extensions of the model. Although the identi<sup>fi</sup>ed risk interactions are assumed to be independent in this study, sometimes the effect of an interaction is in<sup>fl</sup>uenced by other related interactions. To address this limitation, more identi-<sup>fi</sup>cation work about cross-impact between risk interactions by experts and decision-makers is required. In the future work, more parameters like cost of actions will be included so that the mitigation plan can be optimized under resource constraints. Risks with positive effects in the network will be considered, such as risks with positive impact or so-called opportunities like surplus budget and some conditions like good team communication which may mitigate some other negative risks. In addition, risk lifecycles should be registered, so that outdated risks will be deleted in the network structure during the monitoring and control phase. The effectiveness of the model also depends on the validity of the input estimations. At the end of Section 5.2, we performed a preliminary sensitivity analysis on the three-level estimations of risk spontaneous probability, demonstrating the in<sup>fl</sup>uence of input uncertainties on the risk analysis results. Ref. [4] discusses the challenges involved in the representation and treatment of uncertainties in risk assessment, with regard to decision support. This provides some guidance for our future work on the modeling of input assessment uncertainties and their propagation in the risk network for project risk management. The DSS will be applied to projects in different industries and with different levels of complexity.

## Acknowledgements

The authors acknowledge Dr. Ludovic-Alexandre Vidal for his help on the case study. We are also grateful to the anonymous referees for their valuable comments and suggestions.

## References

[1] A. Adla, J.L. Soubie, P. Zarate, A cooperative intelligent decision support system for boilers combustion management based on a distributed architecture, Journal of Decision Systems (JDS) 16 (2) (2007) 241–263.

[2] APM, Project Risk Analysis & Management (PRAM) Guide, ASSOCIATION FOR PROJECT MANAGEMENT, High Wycombe, 2nd edition, 1996.

[3] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (3) (2008) 657–672.

[4] T. Aven, E. Zio, Some considerations on the treatment of uncertainties in risk assessment for practical decision making, Reliability Engineering and System Safety 96 (1) (2011) 64–74.

[5] D. Baccarini, R. Archer, The risk ranking of projects: a methodology, International Journal of Project Management 19 (3) (2001) 139–145.

[6] J. Banks, J.S. Carson, B. Nelson, D. Nicol, Discrete-Event System Simulation, 5th Edition Prentice Hall, 2009.

[7] J. Bowles, The New SAE FMECA Standard, in: IEEE (Ed.), PROCEEDINGS Annual RELIABILITY and MAlNTAINABlLITY Symposium, 1998.

[8] T. Browning, Applying the design structure matrix to system decomposition and integration problems: a review and new directions, IEEE Transactions on Engineering Management 48 (3) (2001) 292–306.

[9] BSI, ISO/IEC Guide 73:2002, Risk Management — Vocabulary — Guidelines for Use in Standards, BRITISH STANDARD INSTITUTE, London, 2002.

[10] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (3) (1999) 225–237.

[11] V. Carr, J.H.M. Tah, A fuzzy approach to construction project risk assessment and analysis: construction project risk management system, Advances in Engineering Software 32 (10–11) (2001) 847–857.

[12] C.B. Chapman, S.C.C. Ward, Project Risk Management — Processes, Techniques and Insights, John Wiley & Sons, Chichester, 2003.

[13] D. Chu, R. Strand, R. Fjelland, Theories of complexity — common denominators of complex systems, Complexity 8 (3) (2003).

[14] L.M. Corbett, J. Brockelsby, C. Campbell-Hunt, Tackling Industrial Complexity Institute for Manufacturing, Cambridge, Cambridge, 2002.

[15] M. Danilovic, T. Browning, Managing complex product development projects with design structure matrices and domain mapping matrices, International Journal of Project Management 25 (2007) 300–314.

[16] C. Eckert, P.J. Clarkson, W. Zanker, Change and customisation in complex engineering domains, Research in Engineering Design 15 (1) (2004) 1–21.

[17] C. Fan, Y. Yu, BBN-based software project risk management, Journal of Systems and Software 73 (2) (2004) 193–203.

[18] J.L. Fleiss, Statistical Methods for Rates and Proportions, John Wiley&Sons, New York, 1981.

[19] A. Gachet, P. Haettenschwiler, A Jini based software framework for developing distributed cooperative decision support systems, Software: Practice and Experience 33 (3) (2003) 221–258.

[20] M. Gif<sup>fi</sup>n, O. De Weck, G. Bounova, R. Keller, C. Eckert, P.J. Clarkson, Change propagation analysis in complex technical systems, Journal of Mechanical Design 131 (2009) 081001.

[21] G. Heal, H. Kunreuther, Modeling interdependent risks, Risk Analysis 27 (3) (2007) 621–634

[22] IEC, CEI/IEC 300-3-9:1995 Risk Management: Part 3 — Guide to Risk Analysis of Technological Systems, INTERNATIONAL ELECTROTECHNICAL COMMISSION, Geneva, 1995.

[23] IEEE, IEEE Standard 1540–2001: Standard for Software Life Cycle Processes — Risk Management, INSTITUTE OF ELECTRICAL AND ELECTRONIC ENGINEERS, New York, 2001.

[24] ISO, ISO 10006 — Quality Management Systems — Guidelines for Quality Management in Projects, 2nd edition International Organization for Standardization, Switzerland, 2003.

[25] B.S. Jones, P. Anderson, Diversity as a determinant of system complexity, GIST technical report G 2005–1, 2005.

[26] J. Kawakita, The Original KJ Method, Kawakita Research Intitute, Tokyo, 1991.

[27] J. Keizer, J. Halman, M. Song, From experience: applying the risk diagnosing methodology, The Journal of Product Innovation Management 19 (3) (2002) 213–232.

[28] H. Kerzner, Project Management: a Systems Approach to Planning, Scheduling and Controlling, John Wiley & Sons, New York, 1998.

[29] E. Lee, Y. Park, J. Shin, Large engineering project risk management using a Bayesian Belief Network, Expert Systems with Applications 36 (3) (2008) 5880–5887.

[30] U. Lindemann, M. Maurer, T. Braun, Structural Complexity Management: An Approach for the Field of Product Design, Springer Verlag, 2008.

[31] F. Marle, L.-A. Vidal, J.-C. Bocquet, Interactions-based risk clustering methodologies and algorithms for complex project management, International Journal of Production Economics (in press), doi:10.1016/j.ijpe.2010.11.022.

[32] C. Mészáros, T. Rapcsák, On sensitivity analysis for a class of decision systems, Decision Support Systems 16 (3) (1996) 231–240.

[33] MIL-STD-1629, Procedures for Performing FMECA (Revision A [1998]), 1998.

[34] G. Pahl, W. Beitz, J. Feldhusen, K. Grote, Engineering Design — a Systematic Approach, Third Edition Springer, 2007.

[35] S.C. PMI, A Guide to the Project Management Body of Knowledge (PMBOK) (2008 ed.), Project Management Institute, Newton Square, PA, USA, 2008.

[36] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (3) (2007) 1044–1061.

[37] T. Saaty, Decision-making with the AHP: why is the principal eigenvector necessary, European Journal of Operational Research 145 (1) (2003) 85–91.

[38] A. Saltelli, K. Chan, E.M. Scott, Sensitivity Analysis, John Wiley & Sons, New York, 2000.

[39] M. Sosa, S. Eppinger, C. Rowles, The misalignment of product architecture and organizational structure in complex product development, Management Science 50 (12) (2004) 1674–1689.

[40] D. Steward, The Design Structure Matrix: a method for managing the design of complex systems, IEEE Transactions on Engineering Management 28 (3) (1981) 71–74.

[41] J. Thompson, Organizations in Action, McGraw-Hill, New York, 1967.

Chao Fang is pursuing his PhD degree in Industrial Engineering at Ecole Centrale Paris, France. He is a research assistant in the Project Management Research Group at ECP Industrial Engineering Laboratory, France. His current research interests include project management, risk management, complex system modeling and simulation. Mr. Fang holds a BS degree in Information Engineering and a MS degree in System Engineering from Xi'an Jiaotong University, People's Republic of China.

Franck Marle is assistant professor in project management at Ecole Centrale Paris for eleven years. He is founder and head of the Project Management Research Group in the Industrial Engineering Laboratory. He made his PhD at Ecole Centrale Paris in 2002 about interactions modeling in PSA Peugeot-Citroën internal projects. He is now conducting research works about risk modeling in projects, interactions modeling and assessment, and decision-making in project and multi-projects context. He has a MSc of Ecole Centrale Lyon (1997).
