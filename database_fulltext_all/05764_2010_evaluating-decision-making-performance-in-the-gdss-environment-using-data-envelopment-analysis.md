---
otero_id: 5764
otero_key: "ZY27GJ3Q"
title: "Evaluating decision making performance in the GDSS environment using data envelopment analysis"
authors: "Reza Barkhi; Yi-Ching Kao"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating decision making performance in the GDSS environment using data envelopment analysis

Reza Barkhi <sup>a,</sup>⁎, Yi-Ching Kao 上

<sup>a</sup> Pamplin College of Business, Department of Accounting and Information Systems, Pamplin Hall, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061-0101, United States

<sup>b</sup> Business School, University of Colorado Denver, Campus Box 165, PO Box 173364, Denver, Colorado 80217-3364, United States

## a r t i c l e i n f o

Article history: Received 9 June 2008 Received in revised form 7 December 2009 Accepted 7 February 2010 Available online 12 February 2010

Keywords: Group decision support system Group decisions Incentive Data envelopment analysis Decision ef<sup>fi</sup>ciency

## a b s t r a c t

We provide a framework to evaluate decision making performance with Group Decision Support Systems (GDSSs) using an overall performance indicator. The indicator is constructed using Data Envelopment Analysis (DEA), which measures the economic ef<sup>fi</sup>ciency of a decision-making process, or how ef<sup>fi</sup>ciently a GDSS user converts decision resources into decision outcomes. To illustrate how our framework can be applied, we conduct an experiment that manipulates three contextual factors: communication mode, incentive structure, and group leadership. Within these contexts, we obtain an individual DEA decision ef<sup>fi</sup>ciency score during the GDSS decision process, where participants are engaged in a mixed-motive task. We <sup>fi</sup>nd that the communication mode, incentive structure, and interaction between the two signi<sup>fi</sup>cantly in<sup>fl</sup>uence decision ef<sup>fi</sup>ciency within this GDSS setting. However, the leadership structure does not have a signi<sup>fi</sup>cant impact on decision ef<sup>fi</sup>ciency. The current study presents the <sup>fi</sup>rst application of DEA in the area of GDSS. We illustrate how DEA is useful for evaluating GDSS-supported decision ef<sup>fi</sup>ciency. The results suggest implications that guide the design of the next generation GDSS to support individuals within collaborative work groups involved in mixed-motive tasks.

Published by Elsevier B.V.

## 1. Introduction

Group Decision Support System (GDSS) technology that has received signi<sup>fi</sup>cant attention in the Information Systems literature is now embedded in Web Services to facilitate group interaction, collaboration, and decision making. These Web tools assist group of decision makers to utilize the computing and communication capabilities of computers to improve their decision process, and consequently decision outcomes [26]. The objective of each individual decision maker is to improve his or her own decision-making performance. In a collaborative context, when the individual incentive and the group incentive are compatible, optimal individual choices often manifest into group decisions that are optimal. However, a decision that is favored by one individual and considered to be of high quality may not always be good when viewed by others having different perspectives. Hence, the decision-making performance measure that is often used in many GDSS studies may suffer from the con<sup>fl</sup>icting views on the de<sup>fi</sup>nition of “performance.” We therefore suggest an overall performance measure based on the economics theory which evaluates how ef<sup>fi</sup>ciently the decision outcomes are produced in GDSS facilitated environment.

Previous researchers have deployed different performance measures, such as decision time, decision quality, and decision satisfaction, to measure GDSS impact. However, it is common to see tradeoffs between these measures [15]. Also, the subjective merit and tradeoffs that these measures have in the minds of GDSS users are de<sup>fi</sup>ned by their individual perspectives. For example, while a shorter decision time is usually desired, the longer decision time associated with searching a larger solution space can lead to higher decision quality [10,29]. There may also be a tradeoff between decision satisfaction and decision quality [56]. The literature has stressed the importance of considering both decision outcomes and decision process while evaluating a decision support system [45,51]. Hence, in addition to a set of single-factor measures that demonstrates decision performance in different perspectives and possibly in different directions, we develop and use an overall performance measure. This useful overall decision performance indicator assesses the ultimate impact of GDSS on the decision-making process [30,50]. The generic performance measure can help resolve con<sup>fl</sup>icting <sup>fi</sup>ndings about the use and effectiveness of GDSS based on different single-factor measures. This metric will also compare each decision maker with others to evaluate the decision making performance, subsequently allowing the GDSS to guide users to improve decision outcomes given a certain amount of decision resources.

We propose an overall performance measure, speci<sup>fi</sup>cally, an “economic” ef<sup>fi</sup>ciency measure, for the assessment of the GDSS-facilitated decision-making process using data envelopment analysis (DEA). In economic theories, ef<sup>fi</sup>ciency is de<sup>fi</sup>ned as the ratio of production outputs to inputs. We consider each GDSS user as a decision-making unit (DMU) that utilizes a set of input resources (e.g., time, cognitive effort and GDSS capabilities) to produce a set of outputs (e.g., decision quality, decision satisfaction). We use DEA to measure the decision production ef<sup>fi</sup>ciency during the GDSS-facilitated decision process. Prior studies often measured ef<sup>fi</sup>ciency solely by decision input, such as decision time [10]. However, less decision time indicates a more ef<sup>fi</sup>cient decision process only when the levels of decision outputs and other input factors are controlled. If the decrease in decision time also leads to a change in other decision inputs or decision quality, the overall decision ef<sup>fi</sup>ciency may decrease, increase or remain unchanged. The DEA ef<sup>fi</sup>ciency measure proposed here differentiates from the conventional time ef<sup>fi</sup>ciency measure in GDSS literature by taking both decision inputs and outputs into account at the same time to present an economic ef<sup>fi</sup>ciency indicator. The method evaluates the ef<sup>fi</sup>ciency of each decision maker by comparing it against the most ef<sup>fi</sup>cient decision makers who provide a benchmark.

DEA is a performance evaluation technique [19] that measures the ef<sup>fi</sup>ciency of a DMU by comparing it to other DMUs. DEA differs from conventional productivity approach that utilizes regression analysis. First, DEA is able to handle the production process with multiple inputs and multiple outputs; second, DEA does not have to assume a speci<sup>fi</sup>c production function between inputs and outputs. Using DEA within a GDSS context can reveal how ef<sup>fi</sup>ciently a GDSS user converts his or her multiple input resources into multiple desired decision outputs. Hence, the DEA ef<sup>fi</sup>ciency score considers decision outcomes and decision processes from multiple aspects simultaneously, without the limitation of the single-factor measures often used in GDSS studies. The DEA ef<sup>fi</sup>ciency metric provides a generic benchmark for evaluating GDSS decisions. The method is particularly relevant to GDSS because it establishes the best practice ef<sup>fi</sup>cient DMUs as a benchmark of performance and evaluates the performance of all DMUs based on that benchmark. Hence, as the GDSS is used over time, it can identify the best decision practice and guide future individual decisions within groups to improve their decisions. This way, future generations of GDSS technology can guide users by providing them with feedback about proper use of decision inputs for decision outputs and improve decision ef<sup>fi</sup>ciency within different contexts.

Context can be viewed as shared knowledge about physical, social, historical, or other circumstances within which an action or event occurs [17]. Being aware of the importance of context settings in utilizing GDSS [17], we illustrate how our proposed DEA ef<sup>fi</sup>ciency measure can be useful by evaluating the ef<sup>fi</sup>ciency impacts of three important GDSS contextual factors: communication mode (distant versus face-to-face), incentive structure (group-based versus individual-based), and group leadership (designated leader versus no leader). These contextual variables have practical implications and are of theoretical interest [29]. However, empirical evidence of their impacts on decision making performance was either inconsistent in some aspects or not established. Therefore, it is useful to examine how these contextual factors in<sup>fl</sup>uence DEA ef<sup>fi</sup>ciency to obtain a comprehensive view of their impacts on decision performance and <sup>fi</sup>ll the gap in prior literature.

In summary, we not only propose a new performance metric in GDSS context using DEA but also demonstrate applying DEA in GDSS context is useful. DEA provides a generic performance indicator, measuring how ef<sup>fi</sup>ciently GDSS users convert decision resources into decision outcomes. It allows the individual decision process within a group to be evaluated from many different dimensions simultaneously. DEA decision ef<sup>fi</sup>ciency scores provide an objective measure that can take decision outcome measures along with GDSS utilization process into account. It provides a standardized ef<sup>fi</sup>ciency measure that allows researchers to compare the overall performance of decision makers, as long as they utilize the same kinds of inputs and generate the same types of outputs. In other words, repeated use of GDSS generates a repository of decision cases that provide a benchmark for guiding future decisions. We show how GDSS researchers can study GDSS contexts that in<sup>fl</sup>uence decision-making ef<sup>fi</sup>ciency. The analysis of our experimental results demonstrates the in<sup>fl</sup>uences of meeting context on the DEA decision ef<sup>fi</sup>ciency of GDSS users and provides managerial implications for GDSS adopters. In the future, the technique can be applied to other decisionmaking contexts, in order to understand the impact of different decision aids on decision ef<sup>fi</sup>ciency within various contexts.

This paper is organized as follows. Section 2 discusses decision making performance and process from the economics viewpoint. Section 3 describes the theoretical basis for DEA and how it is applied for evaluating the ef<sup>fi</sup>ciency of decision production process. Section 4 motivates the selection of contextual variables we use in this study to illustrate our generic GDSS evaluation approach. Section 5 describes the GDSS experiment and data collection. Section 6 presents our model and the empirical results of DEA and statistical analysis. Section 7 imparts our conclusion, contribution, limitations, and future research directions.

## 2. GDSS decision-making performance and process

## 2.1. The need for an overall performance measure

Previous GDSS literature (for a comprehensive review see [29]) has evaluated the decision process using various single-factor performance measures (e.g., quality, satisfaction, time, cognitive effort) and explored how various GDSS settings affect these measures. The results of studies based on single-factor performance measures can be dif<sup>fi</sup>cult to interpret and infer conclusions from when the different single-factor measures point toward different directions. For example, [28] found that individuals in groups using an electronic blackboard reached higher decision quality than those using an electronic workstation. However, individuals in groups using an electronic blackboard had lower satisfaction than those using an electronic workstation. Therefore, the overall impact of an electronic blackboard versus an electronic workstation on the decision process remained inconclusive.

Some GDSS contextual factors have been shown to signi<sup>fi</sup>cantly affect decision making performance and processes, but the empirical evidence was mixed. For example, there were con<sup>fl</sup>icting observations regarding the impacts of communication mode. Prior GDSS research indicated signi<sup>fi</sup>cant impacts of communication mode on different single-factor performance measures but in opposing directions. [31] and [49] showed mixed results from different perspectives that decision makers with face-to-face communication had higher satisfaction but generated lower-quality solutions than those without face-to-face communication. [52] and [33] found that decision makers using face-to-face communication were more time ef<sup>fi</sup>cient but reached lower-quality solutions than those without face-to-face communications. Based on the results of these studies, it is dif<sup>fi</sup>cult to determine whether face-to-face communication is bene<sup>fi</sup>cial for the GDSS decision making process as a whole.

Similarly, results regarding the impact of having a leader in the GDSS environment were mixed. [35] found that designated leadership in a GDSS group improved the level of consensus in the group, and [31] and [40] reported that GDSS groups with designated leaders generated solutions with higher decision quality. On the other hand, [36] and [44] found that having leaders in GDSS groups made no signi<sup>fi</sup>cant difference in the decision processes and performance. Moreover, [12] found that having leaders in GDSS groups even decreased the willingness of group members to disclose information, possibly hindering decision performance. [38] showed that leadership in the GDSS environment indirectly increased the number of proposed solutions but decreased satisfaction with the solution. Results regarding the effects of incentive structure on decision performance were also unclear. [54] documented that compared to those under an individual-based incentive structure, GDSS users operating under a group-based incentive scheme considered more unique solutions but seemed to reach a higher level of consensus.

The aforementioned mixed <sup>fi</sup>ndings regarding the impacts of contextual settings suggest the need for an overall performance measure for the GDSS decision-making process. While it is normal to see that a speci<sup>fi</sup>c GDSS setting improves performance in some aspects but decreases performance in other aspects, an overall performance indicator, if available, can help consolidate the con<sup>fl</sup>icting views and conclusions. The overall performance measure compliments the single-factor performance measure by presenting the big picture. In this study, we construct such an overall performance measure by considering the GDSS decision-making process based on economic theory. We further explain our viewpoint in the following subsection.

## 2.2. GDSS process from an economic viewpoint

Economic theory prescribes the creation of a good or service as a production process which converts a set of production inputs into outputs. Following this line of thought, the decision making process can be modeled as a production process. In line with the prevailing individualistic view [25,32] in the GDSS literature, we consider a decision group as an assembly of its individual group members and the fundamental decision making unit in the GDSS environment as the individual. Each individual member essentially pursues his or her own individual goals, even while working as part of the group. Consequently, we conduct our analysis at the individual level and model the individual decision making process in the GDSS environment. By doing so, we are able to learn more about the factors affecting individual choices which were converged in the group outcome. These <sup>fi</sup>ndings can help us design an individual decision aid to guide the decision process more ef<sup>fi</sup>ciently.

To produce a decision in a GDSS environment, decision makers utilize resources such as time, cognitive effort, and GDSS decision capabilities as production inputs. The outputs of the decision making process can be measured from different dimensions such as decision quality and satisfaction. In economic theory, the performance of a production process can be measured by ef<sup>fi</sup>ciency, that is, how well the production inputs are converted into outputs. As a producer, the decision maker looks for ef<sup>fi</sup>cient production by minimizing costly decision inputs or maximizing decision production performance. In other words, one would aim to utilize the minimum level of decision inputs to reach a solution with a set of predetermined decision outcome measures (e.g., decision quality and satisfaction with the solution). Alternatively, with a given amount of decision inputs, one would aim to obtain a decision outcome whose quality and satisfaction levels are as high as possible.

In this study, we propose using the DEA performance evaluation method to assess the economic ef<sup>fi</sup>ciency of the GDSS decision making process. For illustrative purposes, we evaluate the DEA ef<sup>fi</sup>ciency scores of decision making processes under different contextual settings and statistically test how the different settings impact DEA ef<sup>fi</sup>ciency scores. Fig. 1 illustrates an individual decision-making process from an economic perspective. During the decision process, the decision maker (GDSS user) uses various resources (e.g., time, effort, and GDSS features) as decision inputs and converts them into a solution to the decision problem. The <sup>fi</sup>nal decision is the production output that can be measured in different dimensions. The decision making context, which is characterized by a set of contextual variables (explained in detail in Section 4), can potentially affect the decision process, and thus decision ef<sup>fi</sup>ciency (i.e., how well the decision inputs are converted into decision outputs). Our research applies DEA to estimate the ef<sup>fi</sup>ciency of each individual's decision process, and then illustrates how the contextual variables in<sup>fl</sup>uence decision ef<sup>fi</sup>ciency.

![](/api/attachments/ZY27GJ3Q/fulltext/images/28f5ba6c9d7f11b8fb89e64c04edfe8fc41c9acdd87c380ce347f756cdafe58b.jpg)  
Fig. 1. Decision-making as a production process.

## 2.3. GDSS decision inputs and outputs

A group decision is the collection and convergence of individual decisions. Therefore, the group decision outcome depends on individual decision making, communication, and convergence. We conduct a pioneering study that applies DEA in the GDSS context by developing a generic decision performance measure from the ground up, focusing on the individual decision process. We view each GDSS user as a decision making unit (DMU) that utilizes inputs to produce outputs. The amount of inputs utilized in the decision process to reach the <sup>fi</sup>nal decision is at the discretion of each individual (i.e., each individual has control over the amounts of inputs to be used in the decision process). Other things being equal, the level of an output generally increases as the amount of the utilized input increases.

Two direct inputs to a user's decision process are the time and cognitive effort he or she exerts to reach the <sup>fi</sup>nal solution. When the user spends more time or effort solving the problem and exchanging ideas with other group members, he or she is likely to produce a better solution. Given that we focus on decision making in a GDSS environment, the decision maker's utilization of various GDSS features is also considered. The GDSS we develop for this experiment is a Level 2 GDSS [26], which facilitates group communication and offers decision modeling features (optimization, evaluation, and what-if analysis tools) to reduce uncertainty in the decision process. By using the GDSS features, the user is expected to explore and evaluate a broader set of alternatives and identify a better solution. We designed the GDSS so that it records each user's history of utilizing different features, including proposal making, optimization, evaluation tool, and what-if analysis, during the group decision making process. In this way, we can measure each user's inputs in the GDSS utilization process.

The output of the decision process is a <sup>fi</sup>nal solution to the decision problem. In this study. we look at two important facets of decision output: decision quality and user satisfaction with the decision. Decision quality refers to the objective, measurable bene<sup>fi</sup>t the solution brings to the decision maker. while user satisfaction measures the decision maker's satisfaction with the GDSS solution and, more speci<sup>fi</sup>cally, how close a member believes his or her solution is to the best solution that he or she could achieve. Decision satisfaction is a perceived measure operationalized on a seven-point Likert scale. Both objective decision quality and perceived decision satisfaction are factors that explain the effective, continued use of GDSS. A decision support system can help reach a better solution but does not necessarily increase the decision maker's satisfaction with the decision [43]. DEA provides a way to compare decision performance in cases where the decision outputs in different dimensions favor different parties.

Note that from the economic perspective, each of the single-factor performance measures used in the prior GDSS studies is referred to as either an input or an output factor. For example, time spent is an input factor while satisfaction is an output factor. However, the economic ef<sup>fi</sup>ciency measure we propose here considers all the input and output factors. Speci<sup>fi</sup>cally, the decision ef<sup>fi</sup>ciency evaluated in our model (using DEA) indicates how ef<sup>fi</sup>ciently a decision maker utilizes his or her time, effort, and various GDSS features to generate a decision with certain quality and satisfaction levels. The input and output measures used in this study depict GDSS outcomes and processes, both of which are highly relevant for GDSS evaluation [45,51]. The DEA approach allows us to combine these measures into a uni<sup>fi</sup>ed ef<sup>fi</sup>ciency measure providing a benchmark standard for comparing individual decisions within different GDSS contexts. We consider the decision process at the individual level, so we are able to better understand the factors affecting individual choices within the GDSS context as well as how GDSS can improve individual decision making. This is a pioneer study that models the decision process from an economic viewpoint, using each individual as the decision making unit. However, our approach can easily be applied with input and output measures at the group level to evaluate decision ef<sup>fi</sup>ciency, where each group is considered as a decision making unit. The group level study is a direction for future research. We note that in designing a study focused on group level analysis, one has to design the experimental study and collect data accordingly. We elaborate upon this issue in the discussion on directions for future research.

## 3. Data envelopment analysis

The <sup>fi</sup>rst DEA model was proposed by Charnes, Cooper, and Rhodes (CCR) [18]. The method establishes a best practice production frontier (or envelop) based on the empirical input and output data on DMUs. It determines the level of production inef<sup>fi</sup>ciency of a DMU by projecting the DMU onto the frontier. The original DEA model introduced in 1978 was set up with input orientation and assumes constant returns to scale. In an input-oriented model, the desired output level is achieved by minimizing the production inputs. The constant returns-to-scale assumption suggests that an increase in the amount of inputs utilized would lead to a proportional increase in the amount of outputs generated. The original model has been subsequently extended and numerous variations of DEA have been developed. For example, a DEA model can be set up to be output-oriented [20], which attempts to maximize outputs with a set of available inputs. Another signi<sup>fi</sup>cant development of the DEA model by Banker, Charnes, and Cooper (BCC) [6] allows for variable returns to scale. The variable returns-to-scale assumption suggests that an increase in the amount of inputs utilized can lead to a proportional or unproportional change in the amount of outputs generated.

DEA has been widely used for performance evaluation in different <sup>fi</sup>elds. In the context of information systems, DEA has been applied to evaluate the impact of IT investment on organizational performance in different contexts such as chain restaurants [8], hospitals [41], and public accounting industry [5]. DEA has also been used to examine the performance of software maintenance process [7]. However, to our best knowledge, no GDSS study has ever deployed DEA to assess the performance of a decision making process. Viewing decision making as a production process, we propose the use of DEA for measuring GDSS decision ef<sup>fi</sup>ciency because of its advantages [19]. DEA can handle multiple inputs and multiple outputs simultaneously. Also, DEA is a non-parametric method that does not require a speci<sup>fi</sup>c functional form for the relationship between inputs and outputs. Most importantly, DEA characterizes each individual by a single ef<sup>fi</sup>ciency score. The DEA score provides a comprehensive picture of decision process performance to supplement the single dimensional performance measure that is often used in GDSS studies, which often results in con<sup>fl</sup>icting interpretations of GDSS impact.

Generally speaking, the main objective of a GDSS session is to help the decision makers generate high quality solutions and satisfy the users who would use the GDSS in the future. The GDSS users utilize the available input decision resources to produce the best possible outcomes given the level of resources. Therefore, we deploy the output-oriented DEA model. Rather than assuming certain relationships between decision inputs and decision outputs, the choice between constant returns-to-scale and variable returns-to-scale assumption is based on empirical tests [4] (illustrated in Section 6). To describe the application of DEA model on decision process, assume there are N individual decision makers in the sample data set. Each decision maker produces K decision outputs (e.g., decision quality and satisfaction) using J decision inputs (e.g., time, effort, GDSS utilization). DEA evaluates the ef<sup>fi</sup>ciency of decision maker i by projecting its location onto the production frontier, which is the envelope of all input-output data points in the sample. The following linear program represents a generic output-oriented DEA model that evaluates the DEA score θ of decision maker i under the variable returns-to-scale assumption (i.e. the BCC model):

$$
\underset {\theta , \lambda} {M a x} \theta_ {i}\tag{1.1}
$$

$$
s. t. X \lambda \leq x _ {i}\tag{1.2}
$$

$$
\theta_ {i} y _ {i} \leq Y \lambda\tag{1.3}
$$

$$
e \lambda = 1
$$

$$
\lambda \geq 0.\tag{1.4}
$$

<sub>ð</sub>1:5<sub>Þ</sub>

In the model, X is $\mathsf { a } J { \times } N$ matrix corresponding to the J decision inputs of each of the N decision makers. $x _ { i }$ is a J × 1 matrix corresponding to the J decision inputs used by decision maker i. Y is a K×N matrix representing the K decision outputs of each of the N decision makers. y is a K×1 matrix representing the K decision outputs produced by decision maker i. e is an N×N identity matrix. λ and 0 are N×1 matrices of weights and zeroes, respectively. If the constant returns-to-scale condition is imposed (i.e., the CCR model), then the DEA score $\theta _ { i }$ is obtained by solving the above linear program except that the constraint (1.4) is removed, namely, the objective function (1.1) is maximized subject only to constraints (1.2), (1.3) and (1.5).

The above linear program is solved in $\theta _ { i }$ and λ to maximize the value of $\theta _ { i \cdot }$ The idea is to identify the “best” possible virtual (or composite) decision maker for i. A virtual decision maker is a linear combination of all decision makers in the data set which produces greater outputs than i while using at most the same amount of inputs consumed by i. The <sup>fi</sup>rst constraint (1.2) in the above linear program limits the virtual decision maker to utilize no more than the amount of decision inputs used by i. λ represents a set of weights applied on all decision makers to construct the virtual decision maker that meets the speci<sup>fi</sup>ed constraints. The second constraint (1.3) <sup>fi</sup>nds out that compared to i, how many additional outputs the virtual decision maker can produce, which is indicated by $\theta _ { i } .$ . Speci<sup>fi</sup>cally, the DEA score $\theta _ { i }$ is the ratio of the output level that the virtual decision maker produces to what the decision maker i is currently making. A DEA score of θ =1 for a particular decision maker i indicates that i is ef<sup>fi</sup>cient and located on the production frontier, namely, there is no possible decision maker (real or virtual) that can produce more outputs than i using at most the same amount of input as i. In other cases, θ is greater than 1, indicating i is inef<sup>fi</sup>cient, i.e. the existence of a decision maker (real or virtual) that produces more than i is identi<sup>fi</sup>ed. Therefore, θ is viewed as an inverse indicator of i's decision ef<sup>fi</sup>ciency.

## 4. Contextual factors affecting decision performance

The decision making context is characterized by contextual factors that describe the decision environment. Unlike decision inputs, the contextual factors are not controlled by decision makers, but are often de<sup>fi</sup>ned by management and cannot be altered by individual decision makers. Speci<sup>fi</sup>cally, the contextual factors are exogenously provided during the decision process, whereas the decision inputs can be increased or decreased by individual decision makers. Although uncontrollable, the contextual factors are likely to in<sup>fl</sup>uence the decision maker's attitude and behavior during the decision process. Consequently, they may impact the DEA decision ef<sup>fi</sup>ciency of the decision maker. To illustrate the application of DEA in the GDSS setting, we evaluate the performance impacts of three GDSS contextual variables that were randomly assigned to the subjects of our experiment: communication mode, incentive structure, and leadership. These factors have been identi<sup>fi</sup>ed as important in prior GDSS literature, but their impacts on decision ef<sup>fi</sup>ciency were documented with mixed <sup>fi</sup>ndings (see details in Section 2). We discuss the related theory and develop research hypotheses regarding the impacts of contextual factors on DEA decision ef<sup>fi</sup>ciency in the following subsections. Note that in order to clearly distinguish the “economic ef<sup>fi</sup>ciency” examined in this study from the “time ef<sup>fi</sup>ciency” used in prior GDSS studies, we use the term DEA decision ef<sup>fi</sup>ciency in our discussions.

## 4.1. Communication mode

A GDSS designed for members at different physical locations to communicate at the same time is a Distributed GDSS (DGDSS) [37]. Prior research suggests that DGDSS and Face-To-Face GDSS (FGDSS) groups have substantially different communication styles [34,57]. DGDSS groups cannot engage in face-to-face, verbal, and other forms of non-verbal (i.e., body language) communication. Hence, there is less “social presence” associated with DGDSS than with FGDSS [47]. Social presence is the cognitive synthesis of factors such as the direction one is looking, physical appearance and posture, facial expression, and the feeling of intimacy perceived by the individual. The level of social presence affects how individuals perceive their discussions and relationships with others. A low level of social presence is associated with insensitivity, coldness, and impersonality, and makes it more dif<sup>fi</sup>cult to establish a shared cooperative context within the group [61]. A high level of social presence enables nonverbal compensatory reactions and attraction [22], and reduces the arousal of anxiety and hostility [1]. Consequently, during the group decision making process, a high level of social presence helps resolve con<sup>fl</sup>icts and can facilitate the integration of group solutions.

The impact of communication mode on group decision-making can be explained by media richness theory (MRT) [23,55], social presence, and media synchronicity theory (MST) [24]. MRT classi<sup>fi</sup>es communication media along a continuum of low to high richness using four criteria, including feedback and synchronicity, cue multiplicity, language variety, and personal focus. MRT suggests that rich media are more effective for tasks involving high uncertainty and equivocality, while lean media are more appropriate for tasks involving low uncertainty and equivocality. For group decisions involving complex negotiation tasks, members may <sup>fi</sup>nd it dif<sup>fi</sup>cult to agree to the same solution. This is because each member may have con<sup>fl</sup>icting interpretations of the available information and different objectives. A rich communication mode can facilitate mutual development of common goals and the enactment of a common solution to resolve the equivocality.

Media synchronicity theory (MST) suggests that the richness of the medium is linked to information processing capabilities [24]. MST proposes that <sup>fi</sup>ve media characteristics can affect communication: immediacy of feedback, symbol variety, parallelism, rehearsability, and reprocessability. Face-to-face media rank “high” on feedback and “low” on parallelism. While parallelism is important for idea generation tasks, the immediacy of feedback is important for mixed-motive negotiation tasks. Given that a higher immediacy of feedback in FGDSS facilitates convergence, MST would predict that FGDSS results in higher DEA decision ef<sup>fi</sup>ciency than DGDSS for a mixed-motive task such as the one used in this study.

Both social presence theory and MRT suggest that it is easier for members in FGDSS groups than those in DGDSS groups to develop common goals and reach <sup>fi</sup>nal group solutions. Also, MST indicates that members with FGDSS offering “high” immediacy of feedback can gauge others in a mixed-motive negotiation task. Thus, members in FGDSS groups can more easily converge to better solutions by utilizing less decision resources, and therefore, greater decision ef<sup>fi</sup>ciency than those in DGDSS groups. Speci<sup>fi</sup>cally, we evaluate the following research hypothesis:

H1. The DEA decision ef<sup>fi</sup>ciency of a GDSS user is higher with FGDSS than with DGDSS.

## 4.2. Incentive structure

Incentive structures for members in GDSS groups can affect how members cooperate or compete, exchange information [58], and perform or shirk their responsibility [13]. A group-based incentive structure rewards members equally based on the performance in the group, and may result in free-riding behavior, especially when the cognitive effort of individual members is not observable by others. On the other hand, the individual-based incentive structure rewards each member based on his or her own performance.

The group-based incentive structure encourages members to adopt a cooperative orientation, while the individual-based incentive structure encourages an individualistic orientation [27]. With the cooperative orientation, one has an incentive to do well while also being concerned about the payoff of others. Mutual awareness of a shared cooperative orientation in a group is likely to increase the level of information sharing and promotes a win-win environment. In contrast, with an individualistic orientation, one has an incentive to do as well as he or she can without concern for the payoff of others in con<sup>fl</sup>ict situations. Mutual awareness of a shared individualistic orientation is likely to result in a relationship of mutual suspicion; this development can negatively in<sup>fl</sup>uence the level of information sharing and the collaborative relationships among members.

Under the group-based incentive structure, individuals share the group outcome. Groups with a group-based incentive structure work to maximize the group outcome, and the alignment of goals should help the group members make more ef<sup>fi</sup>cient decisions. On the other hand, under the individual-based incentive structure, each group member has his or her own objective. In order to achieve the maximum reward, they need to convince other members and the leader (if there is a leader in the group) to work toward their objectives. The dif<sup>fi</sup>culty in converging to a consensual decision with individual incentives can waste the GDSS input resources and negatively in<sup>fl</sup>uence the economic ef<sup>fi</sup>ciency of decision making. The GDSS literature investigating the effect of incentive structure on decision performance is relatively lacking with limited <sup>fi</sup>ndings [10,11,54]. To address this gap, we examine the performance impact of incentive structure by evaluating the following hypothesis:

H2. The DEA decision ef<sup>fi</sup>ciency of a GDSS user is higher with a groupbased incentive than with an individual-based incentive.

## 4.3. Leadership structure

Leadership and its in<sup>fl</sup>uence on the performance of small groups in traditional organizations have been studied extensively [2,59]. In general, a leader can help members achieve task-oriented goals, and groups with leaders are less likely to split into subgroups and factions [16]. Previous research on leadership in small groups [16] suggests that the leader not only protects the performance of the organization but also serves as the central force convincing the members to cooperate in order to achieve better solutions for everyone. Leaders in<sup>fl</sup>uence the temporal rhythm of the team by coordinating synchronous communication [60]. Hence, the organization and its members should bene<sup>fi</sup>t from having a group leader. The members in a group with a leader are likely to reach a <sup>fi</sup>nal solution with less decision resources than those in a group without a leader.

Conventional group theory suggests a positive contribution from leaders in terms of decision performance and we aim to con<sup>fi</sup>rm the role of leadership using the DEA ef<sup>fi</sup>ciency measure. To operationalize the role of the leader in traditional organizations, our experiment empowered the designated leader with the authority to override the recommendation of the group or to select among competing member recommendations. The leader could also in<sup>fl</sup>uence the group members using his or her power of personal persuasion by sending coordinating electronic messages. The leader's reward was based on the performance of the organization. We empirically evaluate the following hypothesis regarding leadership impact on overall decision performance:

H3. The DEA decision ef<sup>fi</sup>ciency of a GDSS user is higher in groups with a group leader than in those without a group leader.

## 4.4. Interaction effects

The above discussions suggest that each contextual variable can individually impact DEA decision ef<sup>fi</sup>ciency. In addition, a contextual variable can interact with another variable and generate interaction effects on decision performance. For example, prior research has shown the impact of an interaction between communication mode and incentive structure on decision performance. Speci<sup>fi</sup>cally, FGDSS groups outperformed DGDSS groups when a group-based incentive structure was present [11,12]. Similarly, the interaction between communication mode and leadership, or that between leadership and incentive structure, may in<sup>fl</sup>uence decision performance. We examine the possible interaction effects in our empirical model using the DEA measures discussed previously. Since there is no strong theoretical foundation available in the literature, we focus our exploratory investigation on interaction effects without using formal hypotheses.

## 5. The experiment

We conducted an illustrative experiment to study how various contextual factors in<sup>fl</sup>uence the DEA decision ef<sup>fi</sup>ciency of GDSS users. We implemented a 2 by 2 by 2 factorial design by varying three context variables: communication mode, group leadership mode, and incentive structure. Communication mode has two values: face-to-face (as FGDSS), or distributed (as DGDSS); leadership mode has two values: group with a leader, or group without a leader; incentive structure has two values: individual-based, or group-based incentive structure.

## 5.1. Participants

Participants in this experiment consisted of 156 junior and senior undergraduate business students in business decision making courses who served as subjects for the experiment. The course is required for all undergraduate courses and hence the pool consisted of all undergraduate business majors. About 40% of the participants were female and 60% were male. The average age was 21 years old. The participants were asked to use the GDSS designed for this study to solve a production-planning problem. Groups without a leader consisted of three members, and groups with a leader consisted of three members plus the leader. The groups were randomly assigned to an experimental condition, as shown in Table 1.

The participants were randomly assigned to groups and were given multiple group assignments during the term before they were given the case for this experiment. Thus, the groups had developed some group history prior to solving this case. To acquaint the participants with the GDSS, a training session was held and a sample problem was solved. The formal experiment began after it was determined that the participants fully understood the problem and the features of the GDSS. The GDSS supports real-time communication between the group members. Members of FGDSS groups were seated in a meeting room and could communicate both verbally and via a computer during the problem solving session. Members of DGDSS groups were physically separated, did not have face-to-face contact and communicated via the communication subcomponent of the GDSS.

Table 1 Between-subjects factors.

<table><tr><td></td><td>Treatment</td><td>Number of students</td></tr><tr><td rowspan="2">Leadership</td><td>NO LEADER</td><td>72</td></tr><tr><td>LEADER</td><td>84</td></tr><tr><td rowspan="2">Communication Mode</td><td>DGDSS</td><td>84</td></tr><tr><td>FGDSS</td><td>72</td></tr><tr><td rowspan="2">Incentive</td><td>GROUP</td><td>82</td></tr><tr><td>INDIVIDUAL</td><td>74</td></tr></table>

To make the participants take this experiment seriously, they were informed in advance that 15% of their course grade was to be allocated for this experiment according to the following scheme. Each student's grade for the experiment is directly proportional to the reward points he or she receives on the exercise. Each subject can use the optimization capability of the GDSS to <sup>fi</sup>nd the optimal solution from his or her perspective. This value is an estimate of the reward points that one can receive on the exercise and it is used as a measure of performance. Each member had to agree on a compromise solution that would indicate what production plan to select. In addition to agreeing on a production plan, each member had to select how much effort to expend to maximize his/her performance as de<sup>fi</sup>ned by his or her incentive function. We compared the performance for each member with those achieved by others in the same treatment condition. The highest performance received the full 15% grade and the others received a percentage of 15% that is proportional to the percentage of the value of the highest. In doing so, we operationalized an incentive system that encouraged the participants to maximize their points so that they get to 15% or very close to it. Hence, the student participants linked the points in the experiment to 15% of their grade.

All groups had access to the same GDSS. There was no explicit time limit imposed. On average, it took a group about two hours to complete the experiment. The task is adopted from previous research [9] and is described in Appendix A.

## 5.2. Incentive and leadership structures

The individual-based incentive structure gives rewards based on individual (i.e., departmental) outcome; the group-based incentive structure gives rewards based on group (i.e., organizational/company) outcome. The operationalization of these two incentive structures are explained in the <sup>fi</sup>rst two sections of Appendix A. We also present a numerical example to illustrate the decision-making problems faced by the group members in Appendix B. In groups with leaders, the leader tried to maximize the organizational pro<sup>fi</sup>t as his or her reward was directly tied to organizational pro<sup>fi</sup>t. The leader's problem is illustrated in Appendix A.3. The leader has the authority to impose his or her solution on the department managers. Initially the leader only has an estimate of the departmental costs, and the members may send the leader updated information using the GDSS tool. The reward for each member is computed by calculating the corresponding objective function value resulting from the solution adopted.

## 5.3. GDSS features

We designed a GDSS to support the problem solving and communication needs of groups in a client-server environment. Both face-to-face and distributed groups used this GDSS. The GDSS provides modeling and optimization capabilities, information exchange facilities, a “what-if” capability, and the capability to capture group memory. We classify the GDSS as a Level Two GDSS [26] because of its modeling capability. The GDSS provides process support (i.e., information exchange via prede<sup>fi</sup>ned templates), task structure (i.e., modeling and “what-if” capability), and task support (i.e., optimization capability based on the model formulated for each decision maker presented earlier) as described in the framework by [48]. The GDSS also provides communication support (real-time chat and pre-de<sup>fi</sup>ned templates), some process structuring (complete record of group interaction), and capabilities for information processing (information evaluation, cross impact analysis) as de<sup>fi</sup>ned in the literature [62]. Information processing and process structuring capabilities are the focus of a GDSS designed to aid group decision makers faced with complex tasks. The GDSS consists of three main screens: GDSS Menu, Outgoing Messages, and Public Message Board. The information exchange facility allows the user to send text messages as well as task-speci<sup>fi</sup>c templates of information. The screen for textual message exchange has two major windows. In one window, the user types messages for others. In a second window, the user observes all messages that have been sent to him/her.

![](/api/attachments/ZY27GJ3Q/fulltext/images/e3ae396864f1baa7cb0f2a9182142007fffdd9ef0107b231b6e0d25ae265d64a.jpg)  
Fig. 2. The GDSS and the optimization module

The task-speci<sup>fi</sup>c templates provide the means to exchange information by using pre-de<sup>fi</sup>ned templates. These templates facilitate the exchange of structured and numeric information. Examples of such templates include those that allow members to transmit their departmental cost information to others, and to propose solutions to other members of the group. When a task-speci<sup>fi</sup>c template is transmitted, the local database of each recipient is automatically updated. The modeling capability of the GDSS selects the appropriate model for the problem from the model-base component of the GDSS. It uses the information in a group member's database to formulate speci<sup>fi</sup>c problem instances and to solve each one optimally. The GDSS uses the costs associated with the effort levels that users expend to formulate the model of the problem that is presented in Appendix A.1. The GDSS would then use an optimization module to compute the optimal solution to the problem along with the corresponding reward to the user (see Fig. 2).

A participant evaluates another participant's proposed solution by using the system's “what-if” capability. The what-if capability allows each person to examine the incremental effect of changes to a solution (see Fig. 3).

The “group memory” capability keeps a history of all proposed solutions. Group members have information available about the solutions that have been proposed to date by the various group members. This feature aids in the negotiation process by providing a participant with information about the preferences of other individuals and how these preferences are changing over time.

![](/api/attachments/ZY27GJ3Q/fulltext/images/4e22db851f5723066d33542232f0a7e04c3bde654853dc0f3ec27b37d7cc0ebf.jpg)  
Fig. 3. Solution evaluation module.

## 5.4. Data collection

To understand how the participants in each group deployed the GDSS, the system logged each participant's use of different features. To reveal other unobservable factors during the decision process, each member also completed a short survey after completing the experiment. Based on our research model shown in Fig. 1, we collected the following variables for each group member based on the computer logs and survey.

(1) For the decision process outputs, we identi<sup>fi</sup>ed two measures for the quality and satisfaction of the <sup>fi</sup>nal decision.

REWARD the number of reward points the member received in the experiment. This parameter is an objective measure of decision quality.

SATISFAC the member's level of satisfaction with the <sup>fi</sup>nal group solution, or more speci<sup>fi</sup>cally, how close one believed that the solution came to the best he or she could achieve. The item was measured on a seven-point Likert scale.

(2) For the inputs into the decision process, we collected the following variables:

EFFORT the level of effort the member exerted on the group task, measured on a seven-point Likert scale.

TIME the number of minutes the member spent on the GDSS decision process as recorded by the computer clock for the session start and end.

OPT the number of times the member employed the GDSS optimization tool.

EVAL the number of times the member used the GDSS solution evaluation tool.

W\_IF the number of times the member conducted the GDSS what-if analysis.

PROP the number of unique solutions the member proposed to the group using the GDSS.

Note that EFFORT captures the individual's consumption of physical and mental energy to make the decision, while TIME measures the time spent on the decision process. The two concepts are different. The correlation between EFFORT and TIME is as low as 0.14 in our sample.

(3) For the contextual variables, we recorded the following information that describes the experimental settings of each group:

PROX (Proximity) the communication mode; a dummy variable of 1 assigned for FGDSS, and 0 for DGDSS.

G\_INC the incentive structure; a dummy variable of 1 assigned for group-based incentive, and 0 for individual-based incentive. LEADER the leadership structure; a dummy variable of 1 assigned for a group with a leader, and 0 for a group with no leader.

Note that we collected data only on the 135 group members. We exclude the group leaders from our analysis as their task objectives are different from those of the group members. Table 2 presents the descriptive statistics of the collected variables.

## 6. Data analysis

Our data analysis included two stages of operations. First, we implemented DEA to derive an ef<sup>fi</sup>ciency score for each group member. Second, we applied regression analysis to examine the impacts of contextual factors on user ef<sup>fi</sup>ciency and other measures and to test our three research hypotheses.

Table 2 Descriptive statistics.

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>EFFICIENCY</td><td>0.8258</td><td>0.5606</td></tr><tr><td>REWARD</td><td>94.8796</td><td>22.3302</td></tr><tr><td>SATISFAC</td><td>4.9482</td><td>1.6586</td></tr><tr><td>EFFORT</td><td>5.4296</td><td>1.3075</td></tr><tr><td>TIME</td><td>115.2444</td><td>24.8814</td></tr><tr><td>OPT</td><td>8.4148</td><td>8.1115</td></tr><tr><td>EVAL</td><td>19.1259</td><td>15.6135</td></tr><tr><td>W_IF</td><td>20.7333</td><td>24.1263</td></tr><tr><td>PROP</td><td>2.8815</td><td>1.8490</td></tr><tr><td>PROX</td><td>0.4444</td><td>0.4987</td></tr><tr><td>LEADER</td><td>0.4667</td><td>0.5008</td></tr><tr><td>G_INC</td><td>0.5333</td><td>0.5008</td></tr></table>

## 6.1. Data envelopment analysis

In our experiment, each group member utilized six kinds of input resources (EFFORT, TIME, OPT, EVAL, W\_IF, PROP) to solve the problem. The decision output is a solution that can be measured from two important perspectives, the objective measure of decision quality (REWARD) and the user's satisfaction level with the solution (SATISFAC). Although EFFORT and SATISFAC are ordinal, we considered the data we collected for the inputs and outputs as numerically reliable and used them directly in the DEA analysis [21]. Based on the generic BCC model (which allows for variable returns to scale) presented in Section 3, we constructed the following linear program model with six inputs and two outputs for each group member i in our data set:

$$
\underset {\lambda_ {n}, \theta_ {i}} {\text { Max }} \theta_ {i}\tag{2.1}
$$

$$
\text { s.t. } \quad \sum_ {n = 1} ^ {1 3 5} \lambda_ {n} X _ {n j} \leq X _ {i j} \quad \text { for   } j = 1, 2, 3, 4, 5, 6\tag{2.2}
$$

$$
\theta_ {i} Y _ {i k} \leq \sum_ {n = 1} ^ {1 3 5} \lambda_ {n} Y _ {n k} \quad \text { for } k = 1, 2\tag{2.3}
$$

$$
\sum_ {n = 1} ^ {1 3 5} \lambda_ {n} = 1\tag{2.4}
$$

$$
\lambda_ {\mathrm{n}} \geq 0, n = 1, 2, 3, \dots , 1 3 5\tag{2.5}
$$

where $Y _ { i l } \ = R E W A R D , Y _ { i 2 } \ = S A T I S F A C , X _ { i l } \ = E F F O R T , X _ { i 2 } \ = T I M E , X _ { i 3 } =$ $O P T , X _ { i 4 } = E V A L , X _ { i 5 } = W \_ I F , X _ { i 6 } = P R O P .$

The linear program compares the production performance of group member i against other individuals in the sample. The output-oriented setting implies that each decision maker seeks to maximize his or her outputs given the available set of inputs<sup>1</sup>. As we explained in Section 3, θ is considered an inverse indicator of decision ef<sup>fi</sup>ciency. Since there are 135 members in our sample, we ran 135 linear programs to obtain the BCC estimator of DEA score, referred to as θ<sup>B</sup>, for each group member. To derive the CCR estimator (assumed with constant returns to scale) of DEA score, referred to as θ<sup>C</sup>, we removed Eq. (2.4) and solved the linear program with Eqs. (2.1), (2.2), (2.3) and (2.5).

Both θ<sup>B</sup> and θ<sup>C</sup> are consistent estimators of θ [3]. If the null hypothesis of constant returns to scale is true, the asymptotic empirical distributions of $\theta _ { i } ^ { B }$ and $\theta _ { i } ^ { C }$ would be identical. To test for constant returns to scale, we conducted two semiparametric statistical tests of returns to scale proposed by Banker and Chang [4]. Assuming that the DEA scores are distributed exponentially, the following sum ratio test statistic is evaluated against the Fdistribution with (2 N, 2 N) degrees of freedom:

$$
T _ {E X P} = \sum_ {i = 1} ^ {1 3 5} \left(\theta_ {i} ^ {C} - 1\right) / \sum_ {i = 1} ^ {1 3 5} \left(\theta_ {i} ^ {B} - 1\right) = 2. 1 5 8 1.
$$

Assuming that the DEA scores follow a half-normal distribution, the following sum of square ratio test statistic is evaluated against the F-distribution with (N, N) degree of freedom:

$$
T _ {H N} = \sum_ {i = 1} ^ {1 3 5} \left(\theta_ {i} ^ {C} - 1\right) ^ {2} / \sum_ {i = 1} ^ {1 3 5} \left(\theta_ {i} ^ {B} - 1\right) ^ {2} = 3. 1 5 2 8
$$

Both $\mathrm { T } _ { \mathrm { E X P } }$ and ${ \mathrm { T } } _ { \mathrm { H N } }$ are signi<sup>fi</sup>cant at 5% level. Therefore, we rejected the null hypothesis of constant returns to scale and use θ<sup>B</sup> in our second stage analysis to evaluate whether the contextual factors can signi<sup>fi</sup>cantly affect DEA decision ef<sup>fi</sup>ciency. To enable easier interpretation of our result, we calculated the reciprocal of $\theta _ { i } ^ { B }$ to obtain a positive indicator of decision ef<sup>fi</sup>ciency. We have labeled this ef<sup>fi</sup>ciency score as EFFICIENCY to be used in the second-stage regression analysis. The most ef<sup>fi</sup>cient individuals earned the EFFICIENCY score of 1 and others make a score less than 1. The mean of the EFFICIENCY scores in our sample is 0.83.

## 6.2. Second-stage parametric analysis

In order to evaluate how the contextual factors in<sup>fl</sup>uence DEA decision ef<sup>fi</sup>ciency, we conducted a second stage parametric analysis. Following Banker and Natarajan [9], we regress the DEA ef<sup>fi</sup>ciency scores on the three contextual variables to obtain consistent estimators of the impact of contextual variables. To capture the possible interaction effects between the three contextual variables [11,12], we also include three interaction terms in our estimation model formulated as follows (the common subscript i of all variables have been removed for easier reading):

$$
E F F I C I E N C Y = \alpha_ {0} + \alpha_ {1} P R O X + \alpha_ {2} G _ {-} I N C + \alpha_ {3} L E A D E R + \alpha_ {4} P R O X \times G _ {-} I N C
$$

$$
+ \alpha_ {5} P R O X \times L E A D E A R + \alpha_ {6} G \_ I N C \times L E A D E R + \varepsilon\tag{3}
$$

We estimated the equation using the ordinary least squares method (OLS). We conducted several tests to ensure that our analysis did not violate basic econometric assumptions. We then checked the value of studentized residuals to see if there were any in<sup>fl</sup>uential outliers [14]. We <sup>fi</sup>nd that all observations are in the acceptable range with the absolute value of studentized residuals smaller than three. The Belsley-Kuh-Welsch [14] condition indices indicate that multicollinearity is not a problem. The Shapiro-Wilk [53] test reveals that the residuals from the model do not violate the normality assumption. We also tried including the social background factors, such as gender, major (information systems versus non-information systems) and age of each decision maker, as independent variables in our model but we did not <sup>fi</sup>nd any signi<sup>fi</sup>cant impacts from them. Therefore, no individual background factor needs to be added to our <sup>fi</sup>nal model.

For the purpose of comparison, we also evaluated how the three contextual factors and their interactions affect the decision outputs and inputs using another eight equations by replacing the dependent variable of Eq. (3) with REWARD, SATISFAC, TIME, EFFORT, OPT, EVAL, W\_IF and PROP. The decision output and input variables are also outcome measures commonly used in Group Support System literature. They cover most of the outcome measure categories listed in [29]: REWARD is an effectiveness measure; SATISFC is a satisfaction measure;

Table 4  
Table 3  
Impacts of contextual factors on decision inputs, outputs and DEA ef<sup>fi</sup>ciency.

<table><tr><td rowspan="2">Dependent variable</td><td colspan="6">Coefficient of independent variable (t-Value)</td></tr><tr><td>PROX</td><td>G_INC</td><td>LEADER</td><td>PROX×G_INC</td><td>PROX×LEADER</td><td>G_INC×LEADER</td></tr><tr><td>Decision Efficiency: EFFICIENCY ( $R^2=0.15$ , F-Value = 3.86 $^{++}$ )</td><td>0.1434 (2.26) $^{**}$ </td><td>0.1766 (3.78) $^{***}$ </td><td>-0.0002 (-0.32)</td><td>0.1510 (2.30) $^{**}$ </td><td>0.0163 (0.25)</td><td>-0.0476 (0.73)</td></tr><tr><td>Decision Outputs: REWARD ( $R^2=0.32$ , F-Value = 10.10 $^{++}$ )</td><td>18.7693 (2.75) $^{***}$ </td><td>21.6661 (4.32) $^{***}$ </td><td>-5.2466 (-0.94)</td><td>9.6505 (1.37)</td><td>-3.0295 (-0.43)</td><td>5.9976 (0.86)</td></tr><tr><td>SATISFAC ( $R^2=0.09$ , F-Value = 2.23 $^{++}$ )</td><td>0.6889 (1.18)</td><td>1.3672 (3.18) $^{***}$ </td><td>0.0982 (0.21)</td><td>1.6243 (2.68) $^{***}$ </td><td>0.3669 (0.61)</td><td>-0.4199 (-0.70)</td></tr><tr><td>Decision Input: TIME ( $R^2=0.14$ , F-Value = 3.59 $^{++}$ )</td><td>-16.3308 (-1.91) $^{**}$ </td><td>-18.6323 (-2.97) $^{***}$ </td><td>2.7279 (0.39)</td><td>-16.9853 (-1.92) $^{**}$ </td><td>15.2917 (1.75) $^{**}$ </td><td>-4.5294 (-0.52)</td></tr><tr><td>EFFORT ( $R^2=0.04$ , F-Value = 0.99)</td><td>0.1109 (0.23)</td><td>-0.5306 (-1.52)</td><td>0.2310 (0.60)</td><td>-0.1679 (-0.34)</td><td>-0.1493 (-0.31)</td><td>-0.1225 (-0.25)</td></tr><tr><td>OPT ( $R^2=0.31$ , F-Value = 9.78 $^{++}$ )</td><td>1.6056 (0.64)</td><td>9.3672 (5.11) $^{***}$ </td><td>0.3482 (0.17)</td><td>-0.4312 (-0.17)</td><td>-1.5498 (-0.61)</td><td>-2.4199 (-0.95)</td></tr><tr><td>EVAL ( $R^2=0.20$ , F-Value = 5.31 $^{++}$ )</td><td>-3.6858 (-0.71)</td><td>-19.8243 (-5.20) $^{***}$ </td><td>-6.3966 (-1.51)</td><td>-8.3560 (-1.56)</td><td>-7.2939 (-1.37)</td><td>17.2582 (3.26) $^{***}$ </td></tr><tr><td>W_IF ( $R^2=0.24$ , F-Value = 6.63 $^{++}$ )</td><td>40.0029 (5.11) $^{***}$ </td><td>-13.2655 (-2.31) $^{**}$ </td><td>-16.6785 (-2.61) $^{**}$ </td><td>31.4153 (3.88) $^{***}$ </td><td>-19.5023 (-2.44) $^{***}$ </td><td>31.1601 (3.90) $^{***}$ </td></tr><tr><td>PROP ( $R^2=0.14$ , F-Value = 3.61 $^{++}$ )</td><td>-2.7296 (-4.30) $^{***}$ </td><td>-0.8252 (-1.77)</td><td>-0.5727 (-1.11)</td><td>-2.0256 (-3.09) $^{***}$ </td><td>1.6065 (2.47) $^{***}$ </td><td>-0.3562 (-0.55)</td></tr></table>

<sup>++</sup>Signi<sup>fi</sup>cant at the 5% level.  
<sup>+++</sup>Signi<sup>fi</sup>cant at the 1% level.  
<sup>⁎⁎</sup>Signi<sup>fi</sup>cant at the 5% level (one-sided test).  
<sup>⁎⁎⁎</sup>Signi<sup>fi</sup>cant at the 1% level (one-sided test).

TIME is a process measure; and OPT, EVAL, W\_IF and PROP are usability measures. In Table 3, we summarize our OLS estimation results of the coef<sup>fi</sup>cients of the independent variables in the nine equations discussed above.

To further demonstrate the effects of different GDSS environmental setting, we obtained the least square means of the estimated dependent variables for groups under different contextual settings using LSMeans analyses in SAS. The results are shown in Table 4.

## 6.3. Empirical results

Table 3 shows that communication mode (PROX) has a signi<sup>fi</sup>cant and positive impact on DEA decision ef<sup>fi</sup>ciency, supporting our research hypothesis H1. Users with FGDSS have a signi<sup>fi</sup>cantly higher level of DEA decision ef<sup>fi</sup>ciency than those using DGDSS, indicating that FGDSS users faced with a mixed-motive task bene<sup>fi</sup>t from the richer communication mode. This <sup>fi</sup>nding helps us resolve the con<sup>fl</sup>icting observations on the individual impact of PROX on each of the decision output and input variables. In terms of decision outputs, we found that FGDSS users earn a signi<sup>fi</sup>cantly higher REWARD than DGDSS users. However, the communication mode does not affect the user's satisfaction level with the <sup>fi</sup>nal solution. In terms of decision inputs, the communication mode signi<sup>fi</sup>cantly affects the user's inputs in time (TIME), what-if analysis (W\_IF), and unique solutions proposed (PROP), although in different directions. FGDSS users spend signi<sup>fi</sup>cantly less time and make signi<sup>fi</sup>cantly fewer proposals than DGDSS users when reaching a problem solution. Nonetheless, FGDSS users utilize the what-if analysis tool signi<sup>fi</sup>cantly more frequently than DGDSS users. This implies that the rich media available in the FGDSS environment induce the user to evaluate potential solutions more carefully before making a formal electronic proposal. On the other hand, the lean communication channel in DGDSS hampers the members' ability to gauge others in a mixedmotive task. Hence, they seem to compensate by proposing more solutions to gauge others based on their reactions to the proposed solutions. By examining the DEA score, we are able to show the bigger picture and draw conclusions. Although the communication mode has opposing impacts on the utilization of various inputs, decision makers with FGDSS demonstrate higher overall decision ef<sup>fi</sup>ciency than those with DGDSS. In other words, if decision makers using the two different communication modes consume the same amount of decision inputs for all input factors, decision makers with FGDSS will be able to generate a higher level of decision outputs than those with DGDSS.

The incentive structure variable signi<sup>fi</sup>cantly affects DEA decision ef<sup>fi</sup>ciency, showing that GDSS users under the group-based incentive scheme perform signi<sup>fi</sup>cantly more ef<sup>fi</sup>ciently than those under the individual-based incentive structure. Our research hypothesis H2 is thus supported, suggesting that the proper design of incentives for individuals in a group is critical for ef<sup>fi</sup>cient utilization of GDSS resources. The incentive structure also signi<sup>fi</sup>cantly impacts most decision outputs and inputs, with the exception of the number of proposals made. The users under the group-based incentive scheme earn a higher REWARD (i.e., generate higher quality solutions) and feel more satis<sup>fi</sup>ed with the generated solutions than those under an individual-based scheme. The users under the group-based incentive scheme generally utilize less input resources than those under the individual-based scheme – they spend less time and effort, and deploy the evaluation tool and what-if analysis fewer times. However, it is important to note that the users under the group-based incentive scheme deploy the optimization tool signi<sup>fi</sup>cantly more frequently. Therefore, the incentive structure impacts the decision maker's utilization of various inputs in different directions. Our analysis deploying the DEA ef<sup>fi</sup>ciency measure allows us to resolve the con<sup>fl</sup>icting observations and conclude that, in total, the users under the group-based incentive scheme are more ef<sup>fi</sup>cient decision makers than those under the individual-based incentive scheme. Namely, if decision makers under the two incentive structures consume the same amount of decision inputs for all input factors, then decision makers under the group incentive structure will produce more decision outputs than those under an individual-based incentive structure.

Least square means of groups under different GDSS settings.

<table><tr><td rowspan="3">Performance/output/input measures</td><td colspan="6">Least square means under different GDSS settings</td></tr><tr><td colspan="2">Proximity</td><td colspan="2">Incentive structure</td><td colspan="2">Leadership</td></tr><tr><td>FGDSS</td><td>DGDSS</td><td>Group incentive</td><td>Individual incentive</td><td>With leader</td><td>No leader</td></tr><tr><td>Decision Efficiency: EFFICIENCY</td><td>0.8550*</td><td>0.7116*</td><td>0.8716*</td><td>0.6950*</td><td>0.7833</td><td>0.7832</td></tr><tr><td>Decision Outputs: REWARD</td><td>103.1172*</td><td>84.3479*</td><td>104.5656*</td><td>82.8996*</td><td>91.1093</td><td>96.3559</td></tr><tr><td>SATISFAC</td><td>4.87885</td><td>4.1896</td><td>5.2177*</td><td>3.8505*</td><td>4.4850</td><td>4.5832</td></tr><tr><td>Decision Input: TIME</td><td>113.1569*</td><td>129.4877*</td><td>112.0061*</td><td>130.6385*</td><td>122.6862</td><td>119.9583</td></tr><tr><td>EFFORT</td><td>5.3760</td><td>5.4869</td><td>5.1662</td><td>5.6968</td><td>5.5470</td><td>5.3160</td></tr><tr><td>OPT</td><td>8.0729</td><td>6.4674</td><td>11.9538*</td><td>2.5866*</td><td>7.4443</td><td>7.0906</td></tr><tr><td>EVAL</td><td>22.5675</td><td>26.6088</td><td>14.4983*</td><td>34.3226*</td><td>21.2121</td><td>27.6088</td></tr><tr><td>W_IF</td><td>39.6182*</td><td>0.1847*</td><td>12.9840*</td><td>26.2495*</td><td>11.2775*</td><td>27.9560*</td></tr><tr><td>PROP</td><td>2.1220*</td><td>4.8516*</td><td>3.0741</td><td>3.8994</td><td>3.2004</td><td>3.7731</td></tr></table>

\* Signi<sup>fi</sup>cantly different from the other treatment at the 5% level.

The interaction of PROX and G\_INC (Group Incentive) has a signi<sup>fi</sup>cant and positive impact on DEA decision ef<sup>fi</sup>ciency, though it affects the utilization of different decision input factors in different directions. Speci<sup>fi</sup>cally, the use of FGDSS within a group-based incentive scheme can further increase DEA decision ef<sup>fi</sup>ciency, compared to the ef<sup>fi</sup>ciency level associated with using FGDSS or the group-based incentive alone. We explain this result by observing that a group-based incentive structure requires the group members to exchange information, develop a common goal, build a productive working climate, and engage in other positive actions to manage their con<sup>fl</sup>ict. Hence, members under a group-based incentive structure should bene<sup>fi</sup>t from a FGDSS that facilitates the building of a shared cooperative context [61].

The leadership structure variable does not have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on DEA decision ef<sup>fi</sup>ciency. Therefore, hypothesis H3 regarding the leadership structure cannot be con<sup>fi</sup>rmed. The leadership structure also has no signi<sup>fi</sup>cant impact on any of the decision input and output variables with the exception of the use of what-if analysis. With the presence of a leader in the group, the group members tend to conduct fewer what-if analyses. There are several possible reasons for the insigni<sup>fi</sup>cant impact of leadership. First, it is possible that a GDSS mitigates the in<sup>fl</sup>uence of a leader and that democratic groups can operate as well as those with leaders in a GDSS environment. It is also possible that the assigned leaders cannot exercise power in coordinating the group due to their lack of leadership experience or because of the limited de<sup>fi</sup>nition of leadership in this experiment. Another likely explanation is that the leaders in the experiment were externally assigned instead of internally elected by the group members. Externally assigned leaders may be less capable of coordinating and achieving relational goals than internally elected leaders [42]. Given that we did not test for these conjectures explicitly, we are limited to reporting only the results obtained from our experimental setting. The impact of a leader as operationalized in this study and in this speci<sup>fi</sup>c GDSS environment is not signi<sup>fi</sup>cantly related to DEA decision ef<sup>fi</sup>ciency. Additionally, the interactions between LEADER and PROX, and LEADER and G\_INC do not have a signi<sup>fi</sup>cant impact on DEA decision ef<sup>fi</sup>ciency.

## 7. Conclusion and implications

The key contributions of this study are to view the decision making process from an economic perspective and suggest a generic method ology for the performance evaluation of GDSS usage. We view each individual's decision making process within a GDSS context as a production process and propose a decision ef<sup>fi</sup>ciency measure based on DEA, which is an optimization-based technique that measures the relative ef<sup>fi</sup>ciency of DMUs that convert multiple inputs into multiple outputs. The technique offers an economic ef<sup>fi</sup>ciency measure showing how ef<sup>fi</sup>ciently a decision maker converts his or her decision resources into decision outputs. The methodology simultaneously takes into account the input and output factors to present an overall performance measure. This overall performance measure supplements the singlefactor performance measures often used in prior GDSS studies.

We demonstrate how DEA can be applied in the context of GDSS to measure the performance of each GDSS user and then examine how different contextual variables impact DEA decision ef<sup>fi</sup>ciency. Since GDSS users operate in socio-technical contexts, contextual variables outside the scope of the GDSS itself can in<sup>fl</sup>uence decision-making, as shown in our illustrative analysis. The results of the nonparametric DEA and parametric regression analysis suggest that the communication mode and incentive structure signi<sup>fi</sup>cantly in<sup>fl</sup>uence DEA decision ef<sup>fi</sup>ciency in a GDSS environment. GDSS adopters should properly design these factors in the GDSS context to bene<sup>fi</sup>t from GDSS decision guidance. The results of our study on the in<sup>fl</sup>uence of context on GDSS performance can be useful to the design science creating GDSS features and contexts facilitating human decision-making processes [46].

Our study shows that members in FGDSS groups make decisions more ef<sup>fi</sup>ciently than those in DGDSS groups as measured by DEA. It is interesting to <sup>fi</sup>nd that, although the GDSS tool provides task-speci<sup>fi</sup>c facilities to communicate problem-speci<sup>fi</sup>c information, the ability to communicate face-to-face still results in better decision ef<sup>fi</sup>ciency, possibly through resolving equivocality and uncertainty for the groups involved. We also found that members under a group-based incentive have higher DEA decision ef<sup>fi</sup>ciency than those under an individual-based incentive, as the group-based incentive structure provides members in the same group a congruent objective to work on. This observation highlights the importance of designing an incentive-aligned information system for GDSS group meetings.

Taking the individualistic view, we consider each individual as the unit of analysis and focus on the DEA decision ef<sup>fi</sup>ciency of individuals within the GDSS context. A direct extension of this study is to analyze decision performance at the group level with rede<sup>fi</sup>ned group inputs and outputs. Note that when we designed the study, we operationalized our data collection instruments for decision input and output metrics at the individual level. These variables describing individual choices should not be directly aggregated into those at the collective group level due to possible information loss that may introduce bias and complexities to the analysis. To consider the group as the unit of analysis and explore how ef<sup>fi</sup>ciently a group uses “group input resources” to produce “group outcomes”, the data collection instruments should be redesigned to re<sup>fl</sup>ect the group focus. For example, instead of using individual satisfaction as a construct, group level construct should be operationalized to measure satisfaction with group decision process and group outcome.

Another extension of this research is to incorporate DEA methodology into the design of next-generation GDSS so that the decision maker is guided to make decisions that fall on the ef<sup>fi</sup>ciency frontier. This feature should improve the next generation GDSS, leading each individual in GDSS groups to produce better decisions from a DEA decision ef<sup>fi</sup>ciency perspective. In other words, to waste less input resources in the decision production process. The DEA can also inform the usefulness of various GDSS features for decision ef<sup>fi</sup>ciency and enable incremental improvement in GDSS features, which will subsequently increase the value of the next generation GDSS in supporting collaborative groups. Implementing the DEA ef<sup>fi</sup>ciency measures in web-based GDSS systems like salesforce.com and other customer relationship management systems will allow for the evaluation of decisions using the benchmark formed by decisions made by all decision makers. Another area to apply the concept of decision ef<sup>fi</sup>ciency is Critical Incident Management Systems (CIMS), where decision inef<sup>fi</sup>ciency can have tremendous consequences. Developing DEA decision ef<sup>fi</sup>ciency enables evaluating each decision with respect to all decisions recorded in the decision repository for critical systems (e.g., emergency services), and from there speci<sup>fi</sup>c suggestions could be conjectured to help improve decision ef<sup>fi</sup>ciency for these critical decision systems [39].

This study, like other experimental studies, has its limitations. First, the reader should be cautious about extending the results of this study beyond the experimental conditions that de<sup>fi</sup>ne this study. For example, how we operationalized leadership in this study may be more in tune with tactical leadership than transformational leadership [2]. Also, there may be many different ways that leadership can be operationalized in a GDSS context. Future researchers could investigate the impact of other aspects of leadership on how input resources are converted into decision outputs using the DEA ef<sup>fi</sup>ciency measure in a GDSS context. The approach we illustrated in this study can easily be extended to other GDSS contexts to generate useful results for the design of next generation GDSS and their effective utilization. The next generation GDSS can, therefore, guide individuals in different group decision-making contexts to make optimal use of decision resources in order to convert them to high quality decision outputs.

## Appendix A. The task

The production planning problem is about a company that manufactures four products. A customer order consists of some combination of all four products. Associated with each order is a total revenue value that depends on the number of products and the complexity of modifying the products to satisfy the speci<sup>fi</sup>c requirements. For example, an order might consist of 200 units of product 1450 units of product 2200 units of product 3, and 400 units of product 4. The three members in a group represented the managers of three departments. They met to decide which orders to <sup>fi</sup>ll for the company. A decision to <sup>fi</sup>ll an order means that the order is satis<sup>fi</sup>ed completely; no partial orders are shipped. The information available to the subject includes the details of the order and the total revenue the order generates.

Associated with each order is a departmental Projected Cost (PC) that is the best estimate the company expects each department to incur for <sup>fi</sup>lling the particular order. This information is available to all departments (all group members). Each department, however, has information about its internal costs, the Actual Departmental Cost (ADC), which is not available to the other departments unless the department wishes to reveal these numbers. ADC is not necessarily equal to the departmental PC. Furthermore, each department has information about Uncompensated Departmental Effort Cost (UDEC), which represents the costs the department incurs for <sup>fi</sup>lling an order but is invisible to the company and, hence, the department is not directly compensated for them. In general, the harder the departments work, the lower the ADCs will become. However, the harder the department works, the more departmental resources will be used. The UDEC captures the extra cost of departmental resources that the department has to absorb internally without compensation from the company. In essence, the ADC is a decreasing function of effort while the UDEC is an increasing function of effort in the department. Each department makes its effort level decision based on the incentive structure and the tradeoffs between ADC and UDEC.

Each group member should select a set of orders and come to a consensus set of orders with other members. Once they all agree on a common set of orders, each member decides how much effort to exert on each of the orders. We provide a numerical example in Appendix B.

## A.1. Individual-based incentive

Typical of many organizational incentive structures, member (department manager) bonus is based on how well each department controls its Actual Departmental Costs (ADC) compared to Projected Costs (PC). A department receives a bonus equal to a percentage, without loss of generality, of the difference between the ADC and PC. To lower the ADC's in an attempt to maximize bonus, each department incurs some Uncompensated Departmental Effort Costs (UDEC). The UDEC is borne by the department and is not directly compensated by the organization, hence the term “uncompensated”.

As a member increases his effort level, the ADC decreases and, hence, the deviation of ADC and PC widens, resulting in a higher bonus. However, because an increased bonus is associated with an increased UDEC, the reward that is the bonus minus the UDEC is not necessarily an increasing function of effort level.

For ease of exposition and to avoid overly complicating the experiment, we select four discrete levels of effort (including the optimal) and the corresponding values of ADC and UDEC and presented them to the subjects. The reward due to selecting a subset of orders (among 20 orders) and expending an effort level (choices were 1, 2, 3, or 4) at department d (three departments of marketing, production, and purchasing) is the objective that along with the product capacity constraints leads to the model of the problem, PROB-INDIVIDUAL, given below:

## PROB-INDIVIDUAL:

$$
\begin{array}{l} \text {Max} \sum_ {i \in S} \sum_ {j \in E} \left[ (P C _ {i d} - A D C _ {i j d}) 60 \% - U D E C _ {i j d} \right] X i j \\ \text {S.t.} \\ \sum_ {i \in S} Q _ {i k} Y _ {i} <   C a p a c i t y _ {k} \quad \forall k \in K \\ \sum_ {j \in E} X _ {i j} = Y _ {i} \quad \forall i \in S \end{array}
$$

where;

$$
\begin{array}{l} X _ {i j} = \left\{ \begin{array}{c c} 1 & \text { if   order   i   taken   at   effort   level   j } \\ & 0 \qquad \text { otherwise } \end{array} \right. \\ Y _ {i} = \left\{ \begin{array}{c c} 1 & \text { if   order   i   taken } \\ & 0 \qquad \text { otherwise } \end{array} \right. \\ Q _ {i k} = \text { Quantity   of   product   k\inK   required   in   order   i\inS} \end{array}
$$

and,

PC =Projected Cost of <sup>fi</sup>lling order i, at department d. This term is the best estimate the organization has regarding how much it should cost the department to <sup>fi</sup>ll an order.

$\mathsf { A D C } _ { \mathrm { i j d } } = \mathsf { A c t u a l }$ Departmental Cost of <sup>fi</sup>lling order i, expending effort level j, at department d. For varied levels of effort, the ADC differs and this information is internal to each department.

UDEC =Uncompensated Departmental Effort Cost is the cost that department d incurs, but is not compensated by the organization directly, for <sup>fi</sup>lling order i, for effort level j. This information is internal to each department.

With individual-based incentive structure, utility theory predicts that each member will select an effort at a level where the marginal increase in reward (i.e., bonus minus UDEC) is equal to the marginal cost of extra effort (i.e., ADC). Note that with this incentive structure, the effort level of one department manager has no impact on another department manager's reward.

The problem faced by the members to select effort levels and orders can be divided into two separate sub-problems. The <sup>fi</sup>rst subproblem is to select effort levels for each order. This sub-problem is easily solved by employing marginal analysis as a decision rule. Once optimal effort levels are selected, the best ADC and UDEC, $( \mathsf { A D C } ^ { * } )$ and $( \mathrm { \bar { U } D E C } ^ { * } )$ respectively, will be used to solve the second sub-problem of selecting a subset of the orders. The second sub-problem, SPROB-INDIVIDUAL, is modeled as follows:

$$
\begin{array}{l} \underline {{\text { SPROB - INDIVIDUAL:}}} \\ \text { Max } \sum_ {i \in S} [ (P C _ {i d} - A D C _ {i d} ^ {*}) . 6 0 - U D E C _ {i d} ^ {*} ] Y _ {i} \\ \text { S.t. } \\ \sum_ {i \in S} Q _ {i k} Y _ {i} <   C a p a c i t y _ {k} \quad \forall k \in K \\ \text { where, } \\ U D E C _ {i d} ^ {*} = \text { Uncompensated   Dept.Effort   Cost   for   optimal   effort } \\ A D C _ {i d} ^ {*} = \text { Actual   Departmental   Cost   for   optimal   effort   level } \end{array}
$$

## A.2. Group-based incentive

A percentage of the organizational pro<sup>fi</sup>t, without loss of generality, is assigned as a bonus, and each member receives an equal percentage of this group outcome. Organizational pro<sup>fi</sup>t is calculated by subtracting the sum of ADCs incurred at the three departments from the revenues generated by the selected orders. Hence, the bonus each member receives depends on the Actual Departmental Costs (ADC) of other members as well as his own. If costs of other members are assumed constant, then each member may <sup>fi</sup>nd the optimal effort level for each order, and this information is available locally at the department. However, due to the interaction between a member's bonus and other members' costs, isolated local effort decisions do not result in the best reward for all members.

As a member increases his effort level, the ADC decreases and, hence, the deviation between revenue and sum of the ADCs at the three departments widens, resulting in a higher bonus for each member. However, because an increased bonus is associated with increased UDEC, the reward that is bonus minus the UDEC is not necessarily an increasing function of the effort level. Although the increased bonus is shared by others, the increased UDEC is borne by the department alone. As with individual-based incentive structure, we provide the subjects with the values of ADC and UDEC corresponding to four effort level choices. Each department's problem, with group-based incentive structure, PROB-GROUP, can be modeled as follows:

$$
\begin{array}{l} \underline {{\text {PROB - GROUP:}}} \\ \text {Max} \sum_ {i \in S} \sum_ {j \in E} 1 5 \% [ (R e v _ {i} - \sum_ {t \neq d, t \in D} A D C _ {i t} - A D C _ {i j d}) - U D E C _ {i j d} ] X _ {i j} \\ \text {S.t.} \\ \sum_ {i \in S} Q _ {i k} Y _ {i} <   C a p a c i t y _ {k} \quad \forall k \in K \\ \sum_ {j \in E} X _ {i j} = Y _ {i} \quad \forall i \in S \\ \text {where,} \end{array}
$$

The leader's incentive is the same in all groups. It is a direct percentage of the organizational pro<sup>fi</sup>t. Next, we explain how the organizational pro<sup>fi</sup>t may be calculated.

## A.3. Organizational profit

A group leader tries to maximize the organizational pro<sup>fi</sup>t since his reward is directly tied to organizational pro<sup>fi</sup>t. The organizational pro<sup>fi</sup>t generated by each order selected is the revenue it generates minus the sum of the ADCs incurred at the three departments. The leader gets a percentage of the organizational pro<sup>fi</sup>t as reward. The leader's problem, PROB-LEADER, is modeled as follows:

$$
\begin{array}{l} \underline {{\text {PROB - LEADER:}}} \\ \text {Max} \sum_ {i \in S} [ 9 \% (R e v _ {i} - \sum_ {d \in D} A D C _ {i d}) ] Y _ {i} \\ \text {S.t.} \\ \sum_ {i \in S} Q _ {i k} Y _ {i} <   C a p a c i t y _ {k} \quad \forall k \in K \end{array}
$$

The leader has to select a subset of the incoming customer orders and has the authority to impose his solution on the managers. The leader may also let the members negotiate a commonly acceptable set of orders. The leader's reward depends on the ADC incurred at each department. The ADC is private information at the departmental level and the leader originally has only information about the Projected Costs (PC), which are the best estimates of how much it should cost each department to <sup>fi</sup>ll an order. The department managers may electronically update their ADC by transmitting task-speci<sup>fi</sup>c templates of the GDSS.

## Appendix B

We provide a simple example to illustrate the problem faced by the group members and the interplay of the key variables. We also show what are the decision alternatives faced by each group member. Table A1 below shows the sample information available to the three group members for a speci<sup>fi</sup>c order (e.g., order 1). There are twenty such orders in the experimental task.

Table A1 Public information about an order.  
```haskell
Order 1
Revenue = $865.00
Projected Costs (Marketing) = 200
Costs (Production) = 400
Costs (Purchasing) = 250
```

Table A2 shows the ADC's and UDEC's for each department (group member) associated with order 1 shown in Table A1. This information is provided to the department only and is not available to other departments (other group members).

Table A2 Local information available in each department for each order.

<table><tr><td colspan="3">Marketing</td><td colspan="3">Production</td><td colspan="3">Purchasing</td></tr><tr><td>Effort</td><td>ADC</td><td>UDEC</td><td>Effort</td><td>ADC</td><td>UDEC</td><td>Effort</td><td>ADC</td><td>UDEC</td></tr><tr><td>1</td><td>190</td><td>0</td><td>1</td><td>360</td><td>0</td><td>1</td><td>250</td><td>0</td></tr><tr><td>2</td><td>150</td><td>10</td><td>2</td><td>330</td><td>20</td><td>2</td><td>240</td><td>10</td></tr><tr><td>3</td><td>140</td><td>20</td><td>3</td><td>300</td><td>40</td><td>3</td><td>200</td><td>20</td></tr><tr><td>4</td><td>120</td><td>30</td><td>4</td><td>300</td><td>50</td><td>4</td><td>190</td><td>30</td></tr></table>

The member have to select a subset of the twenty orders and select an effort level for each order they select. Each order generates a revenue and has costs associated with the chosen effort level. For example, order 1 has a revenue of \$865. Assuming that the managers of the marketing, production, and purchasing departments take effort levels 2, 2, and 3, respectively. This results in an organizational pro<sup>fi</sup>t of \$185 (i.e., 865− 150−330−200=185). The bonus for each of the department managers is 15% of this value, namely \$27.75. The reward is found by subtracting UDEC from the bonus resulting in \$17.5, \$7.5 and \$7.5 for each of the three managers. If, instead, they all selected effort level one, then the reward would have been \$9.75 for each. It is trivial to calculate the impact of one member expending effort level 1 while others expend higher effort levels to see whether there is motivation for members to select low effort levels, to take free rides off others, or to prevent others from taking free rides from them. This is a numerical example for groupbased incentive shown in Appendix A (A2).

## References

[1] A.R. Allegeier, D. Byrne, Attraction toward the opposite sex as a determinant of physical proximity, Journal of Social Psychology 90 (1973) 213–219.

[2] B.J. Avolio, F.O. Walumbwa, T.J. Weber, Leadership: current theories, research, and future directions, Annual Review of Psychology 60 (2009) 421–449.

[3] R.D. Banker, Maximum likelihood, consistency and data envelopment analysis: a statistical foundation, Management Science 39 (10) (1993) 1265–1273.

[4] R.D. Banker, H. Chang, A simulation study of hypotheses tests for differences in ef<sup>fi</sup>ciencies, International Journal of Production Economics 39 (1) (1995) 37–54

[5] R.D. Banker, H. Chang, Y. Kao, Impact of information technology on public accounting <sup>fi</sup>rm productivity, Journal of Information Systems 16 (2) (2002) 209–222.

[6] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale inef<sup>fi</sup>ciencies in data envelopment analysis, Management Science 30 (1984) 91–107.

[7] R.D. Banker, D. Dater, M. Srikant, C.F. Kemerer, A model to evaluate variables impacting the productivity of software maintenance projects, Management Science 37 (1) (1991) 1–18.

[8] R.D. Banker, R.J. Kauffman, R.C. Morey, Measuring gains in operational ef<sup>fi</sup>ciency from information technology: a study of the Positran deployment at Hardee's Inc, Journal of Management Information Systems 7 (2) (1990) 29–54.

[9] R.D. Banker, R. Natarajan, Evaluating contextual variables affecting productivity using data envelopment analysis, Operations Research 56 (1) (2009) 48–58.

[10] R. Barkhi, The effects of decision guidance and problem modeling on group decisionmaking, Journal of Management Information Systems 18 (3) (2001) 259–282.

[11] R. Barkhi, V.S. Jacob, H. Pirkul, The in<sup>fl</sup>uence of communication mode and incentive structure on GDSS process and outcomes, Decision Support Systems 37 (2) (2004) 287–305.

[12] R. Barkhi, V.S. Jacob, L. Pipino, H. Pirkul, A study of the effect of communication channel and authority on group decision process and outcomes, Decision Support Systems 22 (1998) 205–226.

[13] A. Barua, C.-H.S. Lee, A.B. Whinston, Incentives and computing systems for teambased organizations, Organization Science 4 (2) (1995) 487–504.

[14] D. Belsley, E. Kuh, R. Welsch, Regression diagnostics: identifying in<sup>fl</sup>uential data and sources of Collinearity, John Wiley and Sons, New York, 1980.

[15] I. Benbasat, L.H. Lim, The effects of group, task, context, and methodology variables on the usefulness of group support systems — a meta-analysis of experimental studies, Small Group Research 24 (4) (1993) 430–462.

[16] E.F. Borgatta, R.F. Bales, Some <sup>fi</sup>ndings relevant to the great man theory of leadership, American Sociological Review 19 (1954) 755–759.

[17] M.R.S. Borges, P. Brezillon, J.A. Pino, J.C. Pormerol, Groupware system design and the context concept, Lecture Notes in Computer Science 3168 (2005) 45–54.

[18] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making unit, European Journal of Operational Research 2 (1978) 429–444.

[19] A. Charnes, W.W. Cooper, A.Y. Lewin, L.M. Seiford, Data envelopment analysis: theory, methodology, and application, Kluwer Academic Publishers, Boston, 1994.

[20] A. Charnes, W.W. Cooper, E. Rhodes, Evaluating program and managerial ef<sup>fi</sup>ciency: an application of data envelopment analysis to program follow through, Management Science 27 (6) (1981) 668–697.

[21] W.D. Cook, D.A. Johnston, D. McCutcheon, Implementations of robotics: identifying ef<sup>fi</sup>cient implementers, Omega 20 (2) (1992) 227–239.

[22] L.M. Coutts, M. Ledden, Nonverbal compensatory reactions to changes in interpersonal proximity, Journal of Social Psychology 102 (1977) 283–290.

[24] A.R. Dennis, R.M. Fuller, J.S. Valacich, Media, tasks, and communication processes: a theory of media synchronicity, MIS Quarterly 32 (3) (2008) 575–600.

[25] G. DeSanctis, Shifting foundations in group support system research, in: L.M. Jessup, J.S. Valacich (Eds.), Group Support Systems: New Perspectives, Macmillan Publishing Co., New York, NY, 1993.

[26] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987) 589–609.

[27] M. Deutsch, The Resolution of Con<sup>fl</sup>ict, Yale University Press, 1973.

[28] C.A. Ellis, G.L. Rein, S.L. Jarvenpaa, Nick experimentation: selected results concerning effectiveness of meeting support technology, Journal of Management Information System 6 (3) (1990) 7–24.

[29] J. Fjermestad, S.R. Hiltz, An assessment of group support systems experimental research: methodology and results, Journal of Management Information Systems 15 (3) (1999) 7–150.

[30] G. Forgionne, An AHP model of DSS effectiveness, European Journal of Information Systems 8 (1999) 95–106.

[31] R.B. Gallupe, G. DeSanctis, G.W. Dickson, Computer-based support for group problem-finding: an experimental investigation MIS Ouarterly 12 (2) (1998) 277-296

[32] J.F. George, K. Marett, G. Giordano, Deception: toward an individualistic view of group support systems, Journal of the Association for Information Systems 9 (10) (2008) 653–676.

[33] D.E. Gundersen, D.L. Davis, D.F. Davis, Can DSS technology improve group decision performance for end users? An experimental study, Journal of End User Computing 7 (2) (1995) 3–10.

[34] R.T. Hightower, L. Sayeed, Effects of communication mode and prediscussion information distribution characteristics on information exchange in groups, Information Systems Research 7 (4) (1996) 451–465.

[35] S.R. Hiltz, K. Johnson, M. Turoff, Group decision support: the effects of designated human leaders and statistical feedback in computerized conferences, Journal of Management Information Systems 8 (2) (1991) 81–108.

[36] T.H. Ho, K.S. Raman, The effect of GDSS and elected leadership on small group meetings,, Journal of Management Information Systems 8 (2) (1991) 109–133.

[37] R. Johansen, A. Martin, R. Mittman, P.I. Saffo, D. Gibbet, S. Benson, Leading Business Teams, Addison-Wesley, Reading, MA, 1991.

[38] S.S. Kahai, J.J. Sosik, B.J. Avolio, Effects of participative and directive leadership in electronic groups, Group & Organization Management 29 (1) (2004) 67–105.

[39] J.K. Kim, R. Sharman, H.R. Rao, S. Upadhyaya, Ef<sup>fi</sup>ciency of critical incident management systems: Instrument development and validation, Decision Support Systems 44 (2007).235–250

[40] Y. Kim, S.R. Hiltz, M. Turoff, Coordination structures and system restrictiveness in distributed group support systems, Decision Support Systems 11 (5) (2002) 379–404.

[41] B. Lee, N.M. Menon, Information technology value through different normative lenses, Journal of Management Information Systems 16 (4) (2000) 99–119.

[42] J.E. Lee-Partridge, An empirical investigation of task and interactional facilitator intervention in the use of group decision support systems, Unpublished Ph.D. Dissertation, University of Minnesota, Minneapolis, MN, 1992.

[43] G.L. Lilien, G.H. Van Bruggen, K. Starke, DSS effectiveness in marketing resource allocation decisions: reality vs. perception, Information Systems Research 15 (3) (2004) 216–235.

[44] L.H. Lim, K.S. Raman, K.K. Wei, Interacting effects of GDSS and leadership, Decision Support Systems 12 (3) (1994) 199–211.

[45] M. Limayem, P. Banerjee, L. Ma, Impact of GDSS: opening the black box, Decision Support Systems 42 (2) (2006) 945–965.

[46] S. March, G.F. Smith, Design & natural science research on information technology, Decision Support Systems 15 (1995) 251–266.

[47] P.R. Monge, L.W. Rothman, E.M. Eisenberg, K.I. Miller, K.K. Kirste, The dynamics of organizational proximity, Management Science 31 (9) (1985) 1129–1141.

[48] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, J.F. George, Electronic meeting systems to support group work, Communications of The ACM 34 (7) (1991) 41–61.

[49] J.S. Olson, G.M. Olson, M. Storrosten, M. Carter, How a group-editor changes the character of a design meeting as well as its outcome, Proceedings of the Conference on Computer-Supported Cooperative Work (1992) 91–98.

[50] K.N. Papamichail, S. French, Design and evaluation of an intelligent decision support system for nuclear emergencies,, Decision Support Systems 41 (2005) 84–111.

[52] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectivemess: a review and an empirical test, Management Science 34 (2) (1988) 139–157.

[53] S.S. Shapiro, M.B. Wilk, An analysis of variance test for normality (complete samples), Biometrika 52 (1965) 591–611.

[54] A. Shirani, M. Aiken, J.G. Paolillo, Group decision support systems and incentive structures, Information & Management 33 (5) (1998) 231–240.

[55] L. Trevino, R. Lengel, R. Daft, Media symbolism, media richness and media choice in organizations: a symbolic interactionist perspective, Communications Research 14 (5) (1987) 553-575.

[56] M. Turoff, S.R. Hiltz, Computer support for group versus individual decisions, IEEF Transactions on Communications 30 (1) (1982) 82–90

[57] M. Turoff, S.R. Hiltz, A.N. Bahgat, A.R. Rana, Distributed group support systems, MIS Quarterly 17 (4) (1993) 399–417.

[58] S. Whang, Analysis of interorganizational information sharing, Journal of Organizational Computing 3 (3) (1993) 257–277.

[59] G. Yukl, Leadership in Organizations, 3rdPrentice-Hall, Englewood Cliffs, NJ, 1994.

[60] Y. Yoo, M. Alavi, Emergent leadership in virtual teams: what do emergent leaders do? Information and Management 14 (2004) 27–58.

[61] M.H. Zack, Interactivity and communication mode choice in ongoing management groups, Information Systems Research 4 (3) (1993) 207–239.

[62] I. Zigurs, B.K. Buckland, A theory of Task/technology <sup>fi</sup>t and group support systems effectiveness, MIS Quarterly 22 (3) (1998) 313–334.

Reza Barkhi is an Associate Professor and Faculty Research Fellow of Information Systems in the Department of Accounting and Information Systems, Pamplin College of Business, at Virginia Polytechnic Institute & State University. He is on leave from Virginia Tech during 2007–2008 and is the department Head of MIS department at American University of Sharjah. His current research interests are in the areas of collaborative technologies and problem solving, and topological design of telecommunication networks. Reza has published in journals such as Location Science, European Journal of Operational Research, Computers & OR, Group Decision and Negotiation, and Decision Support Systems, Communication Research, Communications of AIS, Information Technology and Management, Information & Management, and Journal of Management Information Systems He received a BS in Computer Information Systems MBA, MA, and Ph.D. in Business focusing on Information Systems, Operations Management, and Decision Sciences all from The Ohio State University.

Yi-Ching Kao is visiting assistant professor in the Business School at University of Colorado Denver. She received her Ph.D. from the University of Texas at Dallas. Her research interests include IT business value and performance evaluation of IT projects.
