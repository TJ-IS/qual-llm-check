---
otero_id: 5792
otero_key: "98GMATKH"
title: "A method for Smart Idea Allocation in crowd-based idea selection"
authors: "Victoria Banken; Quirin Ilmer; Isabella Seeber; Stefan Haeussler"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113072"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A method for Smart Idea Allocation in crowd-based idea selection

Victoria Banken<sup>\*</sup>, Quirin Ilmer, Isabella Seeber, Stefan Haeussler

![](/api/attachments/98GMATKH/fulltext/images/cde116a5c7d63369da2c23465c1ac6c18d10e3c2a721f1418b48ed6344fc767e.jpg)

Department of Information Systems, Production and Logistics Management, University of Innsbruck, Innsbruck 6020, Austria

## A R T I C L E I N F O

Keywords: Crowd evaluation Design science Idea contest Open innovation Set partitioning Bin packing

## A B S T R A C T

When evaluating ideas, raters can quickly experience cognitive overload that might result in poor selection performance, Contest managers have an interest in designing idea evaluation tasks that reduce the expected cognitive load of raters. However, research on how managers can meaningfully allocate ideas to raters to manage cognitive load is limited. Moreover. it is unclear how decision support (systems) should be designed in order to help managers to efectively allocate ideas. This paper addresses this challenge and suggests nine design prin ciples and an approach for Smart Idea Allocation (SIA) as a design artifact, which chunks ideas into small subsets, utilizes cognitive biases, and fairly distributes expected cognitive load among raters. We evaluated the SIA approach on a sample of 525 ideas and compared its performance with a random allocation. Our findings suggest that SIA can utilize potential cognitive biases (salience, herding, and order and anchoring bias) more successfully than a random allocation would, distributes the expected cognitive load more fairly among raters, and requires fewer raters for the evaluation task than a random allocation approach. These findings have implications for research on idea selection and are useful for managers of innovation contests.

## 1. Introduction

In crowdsourced innovation initiatives, the number of submissions can easily reach hundreds or even thousands of ideas [20]. While more generated ideas also increase the probability of having more good ideas [10], filtering the best ideas becomes increasingly time consuming and expensive. At Cisco, for example, six people worked full time for three months to create a shortlist of 40 ideas out of 1200 [37]. For IBM's Innovation Jam, more than 50 senior executives spent one week selecting the top 30 from about 46,000 ideas [5]. Google's Project 10^100 resulted in more than 150,000 ideas, and 3000 employees devoted their time to reviewing the submissions<sup>1</sup>. With a rising number of submitted ideas, contest organizers start to outsource the evaluation of ideas during idea selection from small teams to a large crowd, thereby tapping into the wisdom of the crowd [7, 9, 64]. These crowd workers are usually non-experts, but nonetheless an efective complement to experts' idea selection decisions [68].

Yet, people generally are limited in their ability to discern the best idea, resulting in poor selection performance [26]. In fact, the average quality of selected ideas does not difer much from the average quality of generated ideas [56]. In a related field, raters with domain expertise yielded similar findings [62]. A reason for this inability to discern the best ideas is believed to be the high cognitive demand that the idea selection process entails [26, 50]. Raters engage in complex cognitive processes, such as comparing ideas that are very similar [20] or processing idea attributes, including idea descriptions and crowd feedback [32].

When information is overwhelming, individuals tend to rely on shortcuts in their decision-making, also referred to as heuristic processing [17], which is fast, automatic, efortless [23], and prone to cognitive biases [13] that might lead to poor decisions [1]. They step away from logically sound processing of evidence [31], which is slow and efortful but likely to result in accurate decisions [35]. Yet, recent empirical evidence suggests that systematic as well as heuristic processing can result in selecting high quality ideas [70] as long as the raters do not experience cognitive overload. Hence, raters who experience cognitive overload represent a major challenge for contest managers that organize crowd-based idea evaluation, as those crowd raters will likely choose inaccurately, resulting in diminished selection performance and potentially missing out on the one truly good and innovative idea.

One way to reduce an individual's cognitive load is to improve the presentation of task information so that it is cognitively easier to process. The design of the information presentation could reduce the socalled extraneous cognitive load [65] that raters would experience during idea evaluation. That is why idea allocation plays an important role for designers of idea evaluation tasks, as the idea presentation depends on how ideas are allocated to raters. For example, related research-devised allocation algorithms avoid cognitive overload by lim iting the number of ideas that raters evaluate [14, 40]. Other algorithms make use of previous customer ratings to avoid potential mis classification of top and bottom ideas [66]. In the context of design based research, the limiting of ideas or the use of customer ratings can be understood as design principles (DP) [29] that describe heuristic statements for addressing a problem and fostering certain goals. It remains unclear what design principles idea allocation algorithms should entail. Research on such design principles was mostly a means to an end and not the focus of investigation [e.g., 14, 27, 28, 40]. Yet, design principles implemented in an idea allocation system could provide comprehensive decision support for managers who want to design idea evaluation tasks and minimize extraneous cognitive load.

This paper addresses this gap and suggests an approach that meaningfully allocates ideas into subsets to evenly distribute expected cognitive load and utilize cognitive biases. We derive nine design principles for the Smart Idea Allocation (SIA) approach and instantiate a nascent design theory [29] that performs the prescriptive steps of the approach on a sample of 525 ideas from a real idea contest. Our find ings suggest that SIA outperforms a random idea allocation in terms of more fairly distributing potential cognitive load among raters, better utilizing cognitive biases, and requiring fewer raters, hence fewer fi nancial resources. SIA is an integrative, overarching approach for meaningfully allocating ideas to raters by considering a variety of variables that aim at decreasing the raters' extraneous cognitive load and increasing process eficiency for contest managers.

## 2. Background

## 2.1. Decision-making in idea selection

Research suggests that performance–in this case, the quality of idea evaluation–depends on the task dimension and the individual cognitive capacity itself [65]. The information processing capacity of a human cognitive system is limited, as the human working memory can hold on average only 5 to 7 frames [47]. The size of these frames or chunks is not definite. For example, a frame could be a word or sentence, but also a whole idea. The amount of information included in a chunk depends on what the person knows [47]. The cognitive capacity rises when schemas are constructed by combining and integrating smaller in formation elements [65]. Germane cognitive load reflects the effort required to construct such mental schemas. This kind of load allows the storage of knowledge in the long-term memory [65]. Extraneous cognitive load or unnecessary load is imposed by the task presentation and could be relieved by a more eficient instructional design [53, 65]. Intrinsic cognitive load, however, cannot be altered, as it results from the nature of the task in question [65]. If the cognitive load composed of all three types exceeds the information processing capacity of a human cognitive system, the result is cognitive overload, a central challenge for designers of task instructions [46]. Hence, task designers must know the factors that cause cognitive overload.

Prior research [e.g.. 14] has identified multiple factors leading to choice overload, cognitive overload induced by too many choices–e.g., increases in set size, dificulty of the decision task, or complexity of the choice set. Therefore, the combined efects of the set size and the composition of those sets require consideration [18]. Furthermore, repeated and very diverse information induces information overload, cognitive load induced by too much information, which reduces deci sion quality [34]. When decision makers are cognitively overloaded, they switch to decision-making strategies that require less cognitive efort [35]. Such heuristics make humans prone to cognitive biases, also referred to as systematic errors in decision-making [67], likely to result in reduced decision accuracy [35]. Eickhof [21] analyzes cognitive biases in crowdsourcing settings and emphasizes that they have detrimental efects on decision quality when the task design does not account for them. If heuristics and biases are considered, they can efectively guide an overly complex or uncertain decision-making process [11]. Instead of being cognitively overloaded, individuals might then be in a state of cognitive ease [38] and could approximate the appropriate decision [11]. This research aims at identifying possible sources of cognitive overload and cognitive biases that might inhibit accurate decision-making and suggests design principles that should support the manager in eficiently designing the idea evaluation task for raters.

## 2.2. Design principles for cognitive ease

The SIA approach builds on cognitive load theory and cognitive biases. These theories supported the development of the following de sign principles (DP) that contribute to an integrated, overarching idea allocation algorithm. The design principles aim to support the evaluation process for the raters directly (i.e., chunking, grouping of similar ideas, separation of ideas with visual attachments from those without, utilization of feedback information, and fair distribution of text length and text complexity) and support the manager in more eficiently organizing the allocation and evaluation (i.e., randomizing presentation order, equal number of ratings, and reducing the number of raters). Their order follows a logical flow relating to the process of preparing and distributing subsets to raters.

An increasing number of alternatives (ideas) has been linked to higher cognitive load [58]. In a study by Kornish and Ulrich [40], subjects had to identify the most novel ideas by relating similar ideas to each other. The study suggests that people cannot keep more than 75 ideas in mind. To deal with the high quantity of generated ideas, the number of ideas each rater must evaluate is reduced [e.g., 40]. Previous studies from related domains show that the number of ideas should be limited to 5 to 10 options for improved decision-making [e.g., 30, 45]. This has also been referred to as chunking and describes the combi nation of multiple ideas by similarity [30]. In order to fully utilize the concept of chunking, ideas should be allocated first to subsets and then one or more subsets should be allocated to raters for evaluation.

## DP 1. Allocate ideas to subsets.

## DP 2. Assign one or more subsets to raters for evaluation.

Ideas submitted to a contest typically vary in their degree of elaboration; while some are described precisely, others lack specificity and require imagination to identify the gems hidden within rough stones [37]. When potentially relevant information is missing from the idea description, and therefore the decision becomes riskier and more dificult, the ambiguity efect occurs [22]. Most individuals then select one alternative over another because of more available information, making the estimation of a favorable outcome easier. In the case of shortlisting, an ambiguity efect may occur when raters assess an idea in a set of similar ideas. Categorizing ideas according to similarity provides an overview of which ideas are unique and which are generated frequently [40]. Kornish and Ulrich [40] allocate ideas to raters to identify similarity among ideas. At IBM's Innovation Jam, humans and machines clustered similar ideas to highlight the ideas of special interest [5]. Banken et al. [2] found that presenting raters with sets of similar ideas leads to higher decision accuracy than presenting raters with sets of random ideas. This suggests that the visualization of similar ideas allows raters to compare features between ideas more eficiently and to better identify those ideas that are less elaborated. The less elaborated an idea is, the more ambiguous it is and the higher the chance of reducing risk by eliminating the idea from further consideration. Hence, subsets should contain similar ideas so that the ambiguity bias can be utilized and more information related to the same topic is available in each subset.

## DP 3. Cluster ideas by content similarity in each subset.

People contributing ideas to an idea contest, also called ideators, may make use of sketches, images or videos to depict complex ideas. Accompanied by visuals, these ideas are more likely to be memorized than through verbal or textual stimuli alone [16]. An attribute of an idea is salient when it exceeds that attribute's average level in the choice set [8]. For example, if only one idea in a subset has a picture, raters are more likely to give it disproportionately greater weight [8]. This might result in noticeable positive efects of ideas with visual at tachments, compared to those that have only textual descriptions. However, choosing one alternative over another just because an attached picture or video made it more prominent or memorable does not necessarily reflect a choice based on higher quality of the contribution. Similarly, ideators might also incorporate humorous pictures to draw attention to their submission, unrelated to its quality [25]. Mitchell and Olson [48] find that visual stimuli are efective in forming or changing the attitude toward a product, even if the visual stimuli is irrelevant to the product. Hence, subsets should contain only ideas with visual attachments or only ideas without visual attachments, to reduce salience bias.

## DP 4. Separate ideas with visual attachments from those without visual attachments.

Sourcing feedback from the contest community plays an important role in improving ideas by conveying quality signals about aspects such as an idea's market potential [19], feasibility [3] or popularity [52, 59]. In fact, ideas with feedback in the form of likes and comments are more likely to get selected [61] and implemented [32]. Toubia and Florès [66] devise and compare algorithms that classify ideas as top or bottom, based on sequenced consumer evaluations. Also, Görzen and Kundisch [28] allocate ideas to subsets in which all ideas or none have previous star ratings. They found that raters deviated less from the expert-based or crowd-based rating when they assessed high-quality ideas and deviated more from those ratings when they assessed lowquality ideas [28]. Raters rely more on ratings when evaluating good ideas as a way to reduce the complexity of the task [28]. They weigh the information from the aggregated crowd ratings more heavily than their own interpretation [33] of the idea description. This behavior of following the crowd has been referred to as herd behavior [4] and allows people to move away from systematic decision-making [49] to a more efortless decision-making [23]. Therefore, the visualization of community feedback should be considered for idea allocation, as it is an indicator of idea quality and can induce cognitive ease. By allocating one idea with a very high level of feedback into a subset of ideas with low feedback, raters can more easily make a decision, as the quick-toprocess feedback scores provide quality signals.

## DP 5. Balance subsets considering high and low feedback.

Ideas submitted to a contest difer in their length and, hence, afect readability and comprehension diferently [44, 50]–some are long, others are rather short. In online communities, people tend to respond to shorter rather than to longer messages, perceiving a longer text as more complex and less precise [36]. Longer ideas also include more information elements that a rater might not be able to process [43]. Conversely, Nagar et al. [50] find that longer submissions have a better chance of being selected as semi-finalists.

Another important factor that might inhibit decision-making and trigger cognitive overload is the complexity of an idea [14], some easier to understand than others. Comprehension and readability are relevant in idea selection for diferent reasons. Readability is positively related to idea quality [54], and it moderates the efect of diferent selection mechanisms on decision quality [6]. Yet, no study considers text length and text complexity for idea allocation, even though a fair distribution of text length and text complexity is likely to increase decision quality. Hence, combining ideas with very long descriptions and very short descriptions to harmonize the text length that each rater must read for evaluation could be relevant. Highly complex ideas might also induce higher cognitive load and thus should be combined with ideas that are easy to comprehend.

## DP 6. Balance allocated ideas considering text length and text com plexity.

Order biases, namely the primacy efect [69] and the recency effect [12] can negatively afect decision quality [1], as more attention is paid to the first or the last piece of information presented. To avoid this artificially created increased attention to one idea, ideas are rather randomly partitioned into smaller sets where they are randomly positioned and then also randomly allocated to raters [e.g., 2, 39, 41, 55]. In addition, the first presented idea might foster an anchoring efect, which occurs when people make estimations based on a starting point and then adjust their estimate to come to a final answer [67]. The problem is that this adjustment, independent of the starting point, is often insuficient [63], and that anchors can sometimes be irrelevant to the content itself [21]. To attenuate order or anchoring efects, ideas should be presented in a random order so that each idea is presented in diferent positions within and across subsets.

## DP 7. Randomize order of ideas and subsets.

To deal with the high number of ideas generated in the Dell IdeaStorm innovation contest, the managers included additional raters to evaluate ideas and to catch up with the backlog of work [20]. This is in line with the findings that companies are increasingly turning from small teams to a large crowd for idea evaluation [7, 9, 64]. In his work on the wisdom of the crowd, Surowiecki [64] points out that the errors each individual makes in arriving at an answer will cancel themselves out. Hence, averaging the ratings of a diverse set of raters will reduce individual systematic errors in decision-making. Therefore, ideas are allocated to multiple raters for evaluation [e.g., 2, 27, 55]. Riedl et al. [55] further find that stable ranking results can be achieved with an average of 20 ratings per idea. To ensure that the positive efects of the wisdom of the crowd set in, the number of ratings should be equally distributed among ideas in order to create comparable ratings.

## DP 8. Ensure an equal number of ratings for each idea.

The goal of an innovation contest is to source new ideas that migh result in promising business outcomes $[ \mathbf { e . g . } ,$ , 15]. However, if there are too many ideas that require thousands of employees to review them, the process of reviewing and selecting ideas might already consume the resources that those innovations might potentially generate. In a Fortune 100 company, the evaluation of one idea takes about 500 USD and 4 h of staf and management time [57]. Whereas crowd raters evaluated 10 ideas (business models) for about 0.50 EUR (0.56 USD), taking on average 4:32 min [27]. Considering the design principles described above, outsourcing the evaluation to the crowd should result in economic benefits by freeing up internal resources and lowering costs; hence, the number of raters should be reduced.

## DP 9. Minimize the number of raters needed for evaluation in light of design principles one through nine.

Table 1 summarizes which works on idea evaluation considered which design principles of idea allocation. Clearly, none of the existing approaches covers the complete set of design principles for allocating ideas to raters. Thus, constructing an integrated idea allocation algorithm aimed at equally distributing cognitive load among raters and utilizing cognitive biases to facilitate cognitive ease (see DP 1–6) addresses an important research gap. SIA represents decision support for contest managers to eficiently design the evaluation process, reduces allocation time, and enables estimation of financial and human resources required for evaluation (see DP 7–9).

Overview of design principles covered in literature.

<table><tr><td rowspan="2">Design principle</td><td colspan="13">Sources</td></tr><tr><td>[40]</td><td>[37]</td><td>[5]</td><td>[2]</td><td>[3]</td><td>[59]</td><td>[61]</td><td>[66]</td><td>[27]</td><td>[28]</td><td>[41]</td><td>[39]</td><td>[55]</td></tr><tr><td>1 - Allocation of ideas to subsets</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>2 - Allocation of subsets to rater</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>3 - Group similar ideas</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 - Separate ideas with visual attachments from those without</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 - Utilize feedback information</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>6 - Distribute text length and text complexity equally</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7 - Present ideas in random order</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>8 - Collect equal number of ratings per idea</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>9 - Reduce number of required raters</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 3. Method

The proposed design artifact [29] is a method that prescribes up to four tasks for allocating ideas to raters by incorporating the previously introduced design principles:

Task 1: Preprocessing

Task 2: Allocation of ideas to subsets (AIS)

Task 3: Allocation of subsets to raters (ASR)

Task 4: Harmonize the allocated subsets (HAS)

Task 1, preprocessing, aims at splitting the dataset according to one or more grouping variable(s). The manager can either divide the data set based on its content to utilize the ambiguity bias (DP3) and/or based on whether the ideas contain visual attachments or not to mitigate the salience bias (DP4). This optional decision largely depends on the available data and the manager's preferences. The result of this preprocessing step is several idea lists, or one unstructured list of all ideas in the absence of preprocessing.

Task $^ { 2 , }$ allocation of ideas to subsets (AIS), reduces cognitive load by allocating ideas to subsets (DP1). The manager can choose between diferent idea attributes, i.e., feedback, text length, text complexity, as an allocation objective. For example, the manager can utilize the herding bias (DP5) by allocating an idea with a high level of feedback to a subset of ideas with low feedback. Next, the manager can choose either text length or text complexity to fairly balance the expected cognitive load among raters (DP6) when creating subsets.

Task 3, allocation of subsets to raters (ASR), allocates the subsets generated in Task 2 to raters (DP2) in a random order (DP7). In this task, SIA also determines the minimal number of raters (DP9), which requires the manager to input (i) the number of reviews (DP8) for each idea and (ii) the assumed reading speed of the raters. The reading speed serves as a control parameter and is the basis for calculating the time required for idea evaluation by each rater.

Finally. Task $^ { 4 , }$ harmonize the allocated subsets (HAS). allows the manager to re-allocate the given subsets (from Task 2) to the obtained number of raters (from Task 3). The allocation objective can be the idea attribute of either text length or text complexity. The purpose is to minimize the deviation of number words or level of complexity between raters and thereby distribute cognitive load equally among them (DP6). This task also randomizes the order of ideas and subsets presented to the raters to mitigate order and anchoring efects (DP7).

## 4. Artifact description

This section describes the mathematical models for Tasks 2, 3 and 4 (“Allocation of ideas to subsets”, “Allocation of subsets to raters” and “Harmonize the allocated subsets”).

## 4.1. Task 2: allocation of ideas to subsets (AIS)

We formulate a Mixed Integer Linear Problem (MILP) optimization model (set partitioning model), which is defined as follows: Given a list of N ideas $I = \{ i _ { 1 } , . . . , i _ { N } \}$ that should be assigned to M subsets $S = \{ s _ { 1 : }$ $\ldots , s _ { M } \rangle$ such that (i) all ideas i are part of exactly one subset m and (ii) a given allocation objective is minimized. Depending on the chosen allocation objective the values for the ideas $i _ { n }$ are either the feedback (e.g., number of likes), the text length (e.g., number of words) or the text complexity (e.g., text complexity index) of each idea. The aim of Eq. (1) is to minimize the absolute deviation of all subset divided by M.

minimize $\frac { 1 } { M } \Re \sum _ { m = 1 } ^ { M } d _ { m }$

(1)

where $d _ { m }$ represents the absolute deviation of each subset m and is defined as:

$$
d _ {m} = \sum_ {n = 1} ^ {N} \left| \frac {i _ {n}}{M} - i _ {n} ^ {*} x _ {n, m} \right|\tag{2}
$$

For a given number of subsets M, the first part of the right hand side of Eq. (2) is a parameter, i.e., the sum of feedback from all ideas divided by the number of subsets M. The second part comprises a binary allocation variable $x _ { n , m }$ which means that it $\ : i _ { n } ^ { * } x _ { n , m } = 1 \ :$ idea n is allocated to subset m and 0 otherwise. A solution with $d _ { m } = 0$ is therefore a perfect allocation. This means, that each subset comprises the same text length, text complexity or feedback. With regard to the latter, a perfect allocation means that high feedback ideas are allocated to subsets with low feedback ideas which could ease decision-making. As absolute deviation functions are known to be non-linear, we linearized the mathematical model to reduce computation time<sup>2</sup>. In order to ensure that each idea $i _ { n }$ is allocated to exactly one subset m we add constraint (3). To promote a certain level of arousal and to limit the cognitive load we include constraints (4) and (5), which define a lower $( L B _ { A I S } )$ and an upper bound $( U B _ { A I S } )$ for the number of ideas within a subset.

$$
\sum_ {m = 1} ^ {M} i _ {n} ^ {*} x _ {n, m} = 1.\tag{3}
$$

$$
\sum_ {n = 1} ^ {N} i _ {n} ^ {*} x _ {n, m} \geq L B _ {A I S}\tag{4}
$$

![](/api/attachments/98GMATKH/fulltext/images/25847f97adc5ac740825375401be094fdfb69cea4884c12be0dd1b7ca9ad70a3.jpg)  
Fig. 1. Example for allocation of ideas to subsets.

$$
\sum_ {n = 1} ^ {N} i _ {n} ^ {*} x _ {n, m} \leq U B _ {A I S}
$$

$$
x _ {n, m} \in \{0, 1 \}\tag{5}
$$

(6)

Fig. 1 exemplifies the understanding of the procedure. A set of six ideas should be allocated to two subsets based on their feedback. There exists an idea with high feedback (11 likes) and two ideas with low feedback (1 like each). A perfect allocation by SIA considering the feedback is depicted on the left side, whereas one possible random allocation is depicted on the right side. With SIA, the sum of feedback would be equal to the average feedback of all ideas for both subsets. Hence, the average feedback deviation is zero. In the random condition, the average feedback deviation might be higher (e.g., 7.5 in the example) when ideas with high and medium feedback get mixed.

## 4.1.1. Parameters for AIS

Setting the lower $( L B _ { A I S } )$ and the upper bound $( U B _ { A I S } )$ of ideas per subsets also defines the number of subsets (m). We define m as the number of ideas n divided by all integer values between the $L B _ { A I S }$ and $U B _ { A I S }$ and round the result to the next integer. Depending on the number of ideas in a subset, the resulting objective value will vary. In order to identify the optimal subset size, SIA runs the AIS multiple times and selects the subset size m that results in the lowest objective value.

## 4.2. Task 3: allocation of subsets to rater (ASR)

We formulate an optimization model (similar to a bin packing problem), which assigns the list of M subsets $\boldsymbol { S } = \{ s _ { 1 } , . . . , s _ { M } \}$ , given from AIS, to K raters $R = \{ r _ { 1 } , . . . , r _ { K } \}$ such that the number of raters k is minimized (Eq. (7)).

$$
\min \sum_ {k = 1} ^ {K} r _ {k}\tag{7}
$$

subject to

$$
\sum_ {m = 1} ^ {M} s _ {m} ^ {*} x _ {m, k} \geq L B _ {A S R} ^ {*} r _ {k}\tag{8}
$$

$$
\sum_ {m = 1} ^ {M} s _ {m} ^ {*} x _ {m, k} \leq U B _ {A S R} ^ {*} r _ {k}\tag{9}
$$

$$
\sum_ {k = 1} ^ {K} x _ {m, k} \geq N O R
$$

$$
r _ {k} \in \{0, 1 \}\tag{10}
$$

(11)

$$
x _ {m, k} \in \{0, 1 \}\tag{12}
$$

Constraints (8) and (9) guarantee that each rater does not read less than a minimum and a maximum text length or receives a minimum and maximum text complexity $( L B _ { A S R }$ and $U B _ { A S R } ,$ , respectively). Constraint (10) ensures that each subset m receives a minimum number of reviews (NOR) and that no idea is shown more than once to the same rater.

## 4.2.1. Parameters for ASR

Within the ASR model, we need to set three parameters: (i) the minimum $( L B _ { A S R } )$ and (ii) the maximum text length or text complexity $( U B _ { A S R } )$ provided to each rater and (iii) the number of reviews (NOR) for each subset. In general, the first parameter $( L B _ { A S R } )$ can be omitted because the goal is to minimize the number of raters and hence, the model allocates as many e.g., words to each rater as possible. However, in some cases it might be useful to set a minimum $\mathbf { e . g . , }$ text length so that no rater is underutilized. The second parameter $( U B _ { A S R } )$ largely depends on the planned maximum duration of the idea selection process and the assumed reading speed. The third parameter (NOR) is probably the most cost and quality driven parameter. If it is set too low, the idea ranking might not be robust enough, setting it higher will increase stability of the results, but at the same time it will also increase the costs due to higher amount of raters.

## 4.3. Task 4: harmonize the allocated subsets (HAS)

The task of HAS is, given a list of M subsets $\boldsymbol { S } = \{ s _ { 1 } , . . . , s _ { M } \}$ , to find an allocation of subsets to raters $R = \{ r _ { 1 } , . . . , r _ { K } \}$ such that the deviation of a certain allocation objective (text length or text complexity) is minimized (Eq. (13)). Note that the number of subsets M and raters K is given from Task 2 and Task 3, respectively.

$$
\min \sum_ {k = 1} ^ {K} d _ {k}\tag{13}
$$

$$
d _ {k} = \sum_ {m = 1} ^ {M} \left| \frac {s _ {m}}{K} - s _ {m} ^ {*} x _ {m, k} \right|\tag{14}
$$

The objective function (13) is similar to the one presented in Section 4.1, with the diference that we divide $s _ { m }$ by the number of raters K in Eq. (14) because we now allocate subsets to raters instead of ideas to subsets. Hence, this tasks allows to re-allocate subsets among raters so that each rater has a similar amount of text to read or text complexity to process. Furthermore, we include constraint (15) to ensure that each subset $s _ { m }$ is allocated to exactly one rater k. Additionally, constraint (16) guarantees that each rater receives subsets that when combined comply with the defined boundaries of text length or text complexity (see Section 4.2):

$$
\sum_ {k = 1} ^ {K} s _ {m} ^ {*} x _ {m, k} = 1.\tag{15}
$$

$$
\sum_ {m = 1} ^ {M} s _ {m} ^ {*} x _ {m, k} \leq U B _ {A S R}\tag{16}
$$

For the HAS, all parameters are predefined by the previous Tasks of SIA.

## 4.4. Solution techniques

The three optimization models presented above belong to the wellknown categories of “set partitioning” (AIS and HAS) and “bin packing” (ASR) problems known to be NP-hard [24]. We solved the models using the commercial solver CPLEX with a time limit of 2 h. This means that if the solver could not find the global optimum within this time frame, the algorithm stopped, and the integrality gap was reported. The computation was done on a regular computer with 3.6 GHz CPU and 16 GB memory. Additionally, we used a simple greedy heuristic that might not find the optimal solution, but the computation times are negligible, a factor that would be especially important for large idea contests such as

IBM's Innovation Jam with over 46,000 submissions [5]. The greedy heuristic was coded using Perl<sup>3</sup>. We compared the performance of the optimization solver and the greedy heuristic, which both constitute the SIA approach, to a random allocation approach, possibly a common practice for idea allocation [27, 41]. The result for the random ap proach was an average of 10,000 random allocations of ideas to subsets and subsets to raters.

## 5. Artifact evaluation

## 5.1. Case description

For a proof of concept, we tested the proposed Smart Idea Allocation with 525 ideas from the ZEISS VR ONE App Contest<sup>4</sup>. The goal of the contest was to source ideas for apps or completed apps for virtual reality (VR) and augmented reality (AR) headsets. For each idea, we received information on the idea description, including pictures and the community feedback. Feedback was operationalized with the number of likes, which were highly skewed (see Fig. 2). Text length was measured by counting the number of words accompanying an idea. About 50% of the ideas were rather short (up to 100 words), whereas only about 3% were identified as long (more than 399 words) (see Fig. 3a). Text complexity was a combined measure that considered an idea's noun phrase complexity and unit length using the tool for the automatic analysis of syntactic sophistication and complexity (TAASSC), where higher values indicate a higher level of complexity [42]<sup>5</sup>. The minimum complexity was 0 and the maximum was 63.8. The distribution was slightly right skewed (see Fig. 3b).

## 5.2. Results

As formally introduced in Section 4, SIA provides choices for the definition of allocation objectives and parameters for each task. The column Choices of Idea Attributes in Table 2 summarizes which idea attributes could be used as grouping variables (for Task 1) or allocation objectives (for Tasks 2, 3, and 4). The column Design Principles high lights which design principle would be considered when choosing the corresponding idea attribute. Moreover, the table outlines performance criteria with which each design principle was evaluated to assess the allocation (see column SIA Performance Criteria). The purpose of the design principles is to lower expected cognitive load, utilize cognitive biases, and increase eficiency of idea allocation. Hence, the tested performance criteria allow comparing the allocation quality between SIA and a random allocation. Finally, the column Design Principles in Case Example shows that all developed design principles, except design principle 3 (group similar ideas), were considered as part of this artifact evaluation.

## 5.2.1. Task 1: preprocessing

To showcase SIA, the idea attribute visual attachment, or specifically picture, was used as a grouping variable to utilize the salience bias (DP4). About 11% of the ideas had images attached. Assuming that a random allocation took place, this would mean that 50–90% of the subsets (depending on the average number of ideas per subset) would be mixed and thus contain ideas with and without pictures. Assuming that an allocation with SIA took place, two separate idea lists were created: one list including ideas with pictures (N = 59) and one list including ideas without pictures (N = 466 ideas). The allocation of idea subsets proceeded for each list resulting in no (0%) mixed idea lists.

![](/api/attachments/98GMATKH/fulltext/images/0685a97915a56728fb981affcf579bce74bf95aa7e27c670ce85f35772864ef3.jpg)

Fig. 2. Distribution of feedback.  
![](/api/attachments/98GMATKH/fulltext/images/f6f6e1bc96e7b69ab8737c822ca949f05cc8f8b09863bf7a0312c50fcb9e81a0.jpg)  
(a) Distribution of text length

![](/api/attachments/98GMATKH/fulltext/images/887861ffd62cef5873c9e061a364138ccda223a0e77207576addc29f8c91ad7e.jpg)  
(b) Distribution of text complexity  
Fig. 3. Information on idea description.

## 5.2.2. Task 2: allocation of ideas to subsets (AIS)

We used the idea attribute feedback as the allocation objective, to utilize the herding bias (DP5) and allocate ideas into subsets (DP1). The AIS was carried out for the two created idea lists from the previous Preprocessing Task. Tables 3 and 4 show the results for the picture and no-picture lists, respectively. The upper part of each table depicts the number of subsets (m) and the average feedback per subset (denoted as Avg. feedback/subset). Each column depicts the results for a diferent number of ideas per subset, ranging from four ideas per subset in the second column to eight ideas per subset in the fourth. Given the three diferent subset sizes, this resulted in a diference in the total number of subsets m, i.e., 14, 10, and 8 for the picture list and 116, 78, and 59 for the no-picture list.

The lower parts show the results for the AIS for the random allocation, greedy heuristic, and optimization denoted as Random, Greedy heuristic and Optimization-CPLEX, respectively. The performance was measured by the feedback deviation, which should be minimized according to our objective function (see Section 4.1). Finally, we calculated the relative diference between the random allocation and the optimization and the greedy heuristic, respectively, displayed in brackets. Negative values indicate that the SIA approach (greedy heuristic or optimization) was better than the random approach.

Table 4  
Table 2  
Overview of covered design principles with SIA in the case example.

<table><tr><td></td><td>Choices of idea attributes</td><td>Design principles</td><td>SIA performance criteria</td><td>Design principles in case example</td></tr><tr><td rowspan="4">Task 1: Preprocessing</td><td>Content</td><td>3</td><td>Percentage of mixed idea listsa</td><td></td></tr><tr><td>Visual attachments</td><td>4</td><td>Percentage of mixed idea listsb</td><td>4</td></tr><tr><td>Content and visual attachments</td><td>3, 4</td><td>Percentage of mixed idea listsc</td><td></td></tr><tr><td>No preprocessing</td><td>-</td><td>Percentage of mixed idea listsc</td><td></td></tr><tr><td rowspan="3">Task 2: AIS</td><td>Feedback</td><td>1, 5</td><td>Feedback deviation</td><td>1, 5</td></tr><tr><td>Text complexity</td><td>1, 6</td><td>Text complexity deviation</td><td></td></tr><tr><td>Text length</td><td>1, 6</td><td>Text length deviation</td><td></td></tr><tr><td rowspan="2">Task 3: ASR</td><td>Text complexity</td><td>2, 6, 7, 8, 9</td><td>Number of raters</td><td></td></tr><tr><td>Text length</td><td>2, 6, 7, 8, 9</td><td>Number of raters</td><td>2, 6, 7, 8, 9</td></tr><tr><td rowspan="2">Task 4: HAS</td><td>Text complexity</td><td>2, 6, 7, 8</td><td>Text complexity deviation</td><td></td></tr><tr><td>Text length</td><td>2, 6, 7, 8</td><td>Text length deviation</td><td>2, 6, 7, 8</td></tr></table>

<sup>a</sup> A mixed idea list contains ideas from diferent categories.  
<sup>b</sup> A mixed idea list contains either ideas with pictures and ideas without pictures.  
<sup>c</sup> A mixed idea list contains ideas with and without pictures and/or ideas from diferent categories.

Table 3  
Results of Task 2: Allocation of ideas to subsets picture.

<table><tr><td>Picture: 59 ideas</td><td>4 ideas/subset</td><td>6 ideas/subset</td><td>8 ideas/subset</td></tr><tr><td>Number of subsets m</td><td>14</td><td>10</td><td>8</td></tr><tr><td>Avg. feedback/subset</td><td>15.28</td><td>21.42</td><td>26.78</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">Feedback deviation (objective value)</td></tr><tr><td>Random</td><td>3.45</td><td>3.91</td><td>4.50</td></tr><tr><td>Greedy heuristic</td><td>1.69 (-51.0%)</td><td>0.60 (-84.7%)</td><td>1.00 (-77.9%)</td></tr><tr><td>Optimization-CPLEX</td><td> $0.27 (-92.2\%)^a$ </td><td> $0.50 (-87.2\%)^b$ </td><td> $0.47 (-89.6\%)^c$ </td></tr></table>

<sup>a</sup> Optimum found in 5 s.  
b Optimum found in less than 1 s.  
<sup>c</sup> Optimum found in 2 s.

Results of Task 2: Allocation of ideas to subsets no-picture.

<table><tr><td>No-picture: 466 ideas</td><td>4 ideas/subset</td><td>6 ideas/subset</td><td>8 ideas/subset</td></tr><tr><td>Number of subsets m</td><td>116</td><td>78</td><td>59</td></tr><tr><td>Avg. feedback/subset</td><td>8.73</td><td>12.98</td><td>17.17</td></tr><tr><td colspan="4">Feedback deviation (objective value)</td></tr><tr><td>Random</td><td>2.45</td><td>3.04</td><td>3.57</td></tr><tr><td>Greedy heuristic</td><td>0.91 (-62.9%)</td><td>0.23 (-92.4%)</td><td>0.29 (-91.9%)</td></tr><tr><td>Optimization-CPLEX</td><td> $0.84 (-65.7\%)^a$ </td><td> $0.22 (-92.8\%)^b$ </td><td> $0.28 (-92.2\%)^c$ </td></tr></table>

<sup>a</sup> No optimum found in 2 h, gap: 7.0%.  
<sup>b</sup> Optimum found in 98.04 s.  
<sup>c</sup> Optimum found in 51.51 s.

The evaluation shows that the greedy heuristic clearly outperformed the random allocation, as the objective value feedback deviation is smaller for each subset size. For the random allocation, the higher feedback deviation suggests the existence of subsets that include mul. tiple ideas with high feedback scores, which might prevent cognitive ease (see Fig. 1 for an example). The optimization model found the optimal solution to all but one case (see Table 4), thus outperforming even the greedy heuristic for all given subset sizes. The diference between the optimal solution and the greedy heuristic was largest for ideas that included a picture. Especially in the case of four ideas per subset, the heuristic reached an objective value of 1.69, compared to the optimum of 0.27 (see Table 3). Both SIA models (greedy heuristic and optimization) outperformed the random allocation by about

51–93%. This suggests that SIA successfully allocated ideas with very high levels of feedback to subsets of ideas having very low feedback values, hence, more likely utilizing a herding bias to make idea evaluation easier as raters experience cognitive ease.

We choose to proceed with six ideas per subset, since, overall, thi subset size yielded the lowest feedback deviation and, in order to run Task 3, we merged the two idea lists (picture and no-picture) again.

## 5.2.3. Task 3: allocation of subsets to rater (ASR)

For allocating subsets to raters (DP2), we considered the idea attribute text length for minimizing the number of raters (DP9) needed for evaluation, because it represents the demand on a rater's cognitive capacity. We assumed an average rater's reading speed of 501 words per minute and a task duration of 15 min<sup>6</sup>, which led to an upper bound of 7515 words per rater. The number of reviews (NOR) (DP8) was based on related literature [55] that suggests an idea should be rated 20 times to represent a stable idea rating. Furthermore, the order of ideas within each subset and the order of subsets presented to raters was randomized (DP7) to mitigate the order and anchoring effects.

The results of the ASR for the random, greeedy heuristic and optimization approach are depicted in the second through the fourth columns of Table 5. The rows in Table 5 indicate the number of raters, the maximum, minimum, and average text length (measured in words) that a rater must read. Additionally, the text length and the text complexity deviation values indicate the range of words and complexity among all raters, where a lower deviation indicates a more equal distribution.

The results show that the random approach allocated ideas to 259.89 raters, the heuristic to 200 and the optimization to 189. Hence, the SIA optimization model and greedy heuristic outperformed the random approach by 27.3% and 23%, respectively (DP8), implying high potential for cost reduction. With respect to the fair distribution of text length (DP6), the random allocation would require raters to read ideas between 416 and 7498 words. In contrast, the SIA allocation would require raters to read between 3876 and 7482 words (heuristic) or between 4800 and 7500 words (optimization). This suggests that SIA outperforms a random allocation allowing for a more balanced workload with fewer required raters.

## 5.2.4. Task 4: harmonize allocated subsets (HAS)

In the last step of the Smart Idea Allocation approach, we aimed at harmonizing the workload among raters. After all, a lower number of raters means that each rater must read more on average and therefore deal with a higher cognitive load on average, during the evaluation (see Table 5). Given the results of Task 3 (see Table 5), we attempted to minimize the text length deviation among the raters (DP6). Since this step can only be carried out by the greedy heuristic and the optimization, the results for the random allocation in Task 3 remain unchanged. Recall that the random allocation resulted in an average text length deviation of 2100 words/rater.

Table 5  
Results of Task 3: Allocation of subsets to rater.

<table><tr><td></td><td>Random</td><td>Greedy heuristic</td><td>Optimization CPLEXa</td></tr><tr><td>Number of raters (objective value)</td><td>259.89</td><td>200 (-23.0%)</td><td>189 (-27.3%)</td></tr><tr><td>Max. text length</td><td>7498.23</td><td>7482.00 (-0.2%)</td><td>7500.00 (±0%)</td></tr><tr><td>Min. text length</td><td>416.02</td><td>3876.00 (+89.3%)</td><td>4800.00 (+91.3%)</td></tr><tr><td>Avg. text length/rater</td><td>5350.70</td><td>6950.30 (+29.7%)</td><td>7354.81 (+37.5%)</td></tr><tr><td>Avg. text length deviation/ rater</td><td>2100.32</td><td>616.96 (-70.6%)</td><td>111.28 (-94.7%)</td></tr><tr><td>Avg. complexity/rater</td><td>499.48</td><td>648.80 (+29.9%)</td><td>915.59 (+83.3%)</td></tr><tr><td>Avg. complexity deviation/ rater</td><td>200.86</td><td>150.42 (-25.1%)</td><td>139.67 (-30.5%)</td></tr></table>

<sup>a</sup> No optimal solution found in 2 h, gap: 1.4%.

The results for the greedy heuristics and the optimization model are shown in Table 6, where the ASR columns report the results from the previous Task 3, and the HAS columns report the final results after Task 4. The difference between the ASR and HAS values is shown in brackets The heuristic and the optimization vastly reduced the text length deviation, by − 69.0% and − 99.7%, respectively. The deviation was below 200 words for the greedy heuristic and below 1 word for the optimization. This suggests that SIA can significantly increase the equal distribution of expected cognitive load induced by text length.

## 6. Discussion, limitations and future work

This paper reports on an idea allocation approach that aims at decreasing extraneous cognitive load for raters and increasing process eficiency for contest managers. In the context of Design Science Research, this approach could be classified as exaptation research [29], where known solutions, i.e., common allocation methods from Operations Research, are extended to new problems, i.e., idea allocation. Our four-step idea allocation approach provides flexible decision support to contest managers who must eficiently allocate many ideas to many raters, and who want to reduce raters' expected cognitive load by also utilizing potential cognitive biases and fairly distribute the workload among raters. A basic principle of this approach is to intelligently chunk ideas into subsets to ease information processing and reduce the probability of raters' cognitive overload [30]. Past research on

## Table 6

Results of Task 4: Harmonize the allocated subsets.

<table><tr><td rowspan="2"></td><td colspan="2">Greedy heuristic</td><td colspan="2">Optimization CPLEXa</td></tr><tr><td>ASR</td><td>HAS</td><td>ASR</td><td>HAS</td></tr><tr><td>Avg. text length deviation (objective value)</td><td>616.96</td><td>191.24 (-69.0%)</td><td>111.28</td><td>0.30 (-99.7%)</td></tr><tr><td>Max. text length</td><td>7482.00</td><td>7269.00 (-2.1%)</td><td>7500.00</td><td>7355.00 (-2.2%)</td></tr><tr><td>Min. text length</td><td>3876.00</td><td>6487.00 (+67.4%)</td><td>4800.00</td><td>7354.00 (+53.2%)</td></tr><tr><td>Avg. complexity deviation</td><td>150.42</td><td>127.43 (-15.3%)</td><td>139.67</td><td>112.59 (-24.1%)</td></tr><tr><td>Number of raters</td><td></td><td>200</td><td></td><td>189</td></tr><tr><td>Avg. text length/rater</td><td></td><td>6950.30</td><td></td><td>7354.81</td></tr><tr><td>Avg. complexity/rater</td><td></td><td>648.80</td><td></td><td>915.59</td></tr></table>

<sup>a</sup> No global optimum found in 2 h, gap: 97.8%.

allocation recognizes that the number of options or ideas presented to raters influences performance [18, 41] and that idea attributes, such as feedback, also could be utilized [66]. But none have so far approached the allocation of ideas from such a holistic cognitive perspective as the approach presented here. The proposed SIA approach makes three major contributions. First, this paper conceptually derives nine design principles for idea allocation systems that aim at decreasing and fairly distributing the expected cognitive load for raters (DP 1–6) as well as increasing process eficiency (DP 7–9).

Second, the paper contributes the SIA approach, an idea allocation system implementing all design principles. The evaluation demonstrated that SIA can utilize e.g., a potential herding bias more successfully than a random allocation when grouping ideas with low and high levels of feedback. SIA also distributes the expected cognitive load more fairly among raters. We demonstrate this by showing for instance, that deviations of average text length per rater are considerably lower for SIA, compared to those in the random allocation approach.

Finally, the SIA approach is also more economical than a random allocation, as SIA requires fewer raters for evaluation. Furthermore, using a simple greedy heuristic is suficient, since it largely out performed a naive random allocation approach and yielded a solution close to optimum with less computation time required than an optimization solver.

## 6.1. Implications for research

The findings of this study have several implications for research on (crowdsourced) idea allocation and evaluation. This study ofers nine design principles and the implemented SIA approach that allow in vestigating the efects on cognitive biases and cognitive load in idea evaluation. Essentially, SIA aims at influencing the decision-making process of raters in a predictable way. The implemented design principles can be understood as digital nudges, referring to user interface elements that “guide people's behavior in digital choice environments” [60]. In that sense, SIA creates choice environments for each prospective rater, as the approach outputs subsets of ideas. Once these subsets are presented online, one can study the degree to which the digital nudges can utilize cognitive biases and reduce cognitive load. Moreover, the implemented design principles grouping of content (DP3) or visual attachments (DP4) and randomization of ideas (DP7) can also be understood as debiasing strategies [17] to minimize the ambiguity, salience, and order or anchoring biases. Hence, the findings of this study may be important for design-oriented research to investigate digital nudges and debiasing strategies in idea evaluation.

Second, the findings of this study are not bound to idea allocation alone but may also be generalized to other domains. For example, in consumer research, the allocation of ideas could be replaced by the allocation of products on websites. Also in the domain of human resource management, ideas could be replaced by talent information when shortlisting candidates for an open position. Hence, any researcher whose research links to the selection among various options could benefit from SIA by adopting it into their own selection domains.

## 6.2. Implications for practice

We found that the SIA approach outperforms a random allocation in terms of eficient resource planning, where SIA required 189 (optimization model) or 200 (greedy heuristic), compared to 260 raters for the random allocation, which represents a reduction of up to 27.3%. This has implications for practice, as we expect the increase in eficiency to be even larger, since, in practice, the whole idea allocation process is often very unstructured [27, 41]. This means that besides saving costs for fewer raters we also expect a higher decision quality by the raters since SIA fairly distributes the cognitive load among the raters.

Moreover, SIA enables automatic grouping and chunking of ideas into idea subsets. While a manager of an innovation contest can easily perform a grouping and chunking of ideas for 20 to 30 ideas, the task is likely to get demanding as soon as the number of ideas rises. Hence, practitioners can benefit from the automated allocation, because SIA can perform this task more quickly, more efortlessly, and largely errorfree. Furthermore, we show that a simple greedy heuristic yields results that are close to the optimal solution. Thus, we suggest practitioners to use this heuristic, especially for large idea contests, due to its negligible computation time.

Lastly, SIA provides decision support to the manager by ofering several choices in designing the idea evaluation task. For example, the manager who wants to refrain from utilizing feedback information (DP5) to create subsets in Task 2 can alternatively rely on text length or text complexity (DP6). The result would be equally long or complex subsets. that do not difer much with respect to text length or text complexity.

## 6.3. Limitations and future research

This study also has some limitations that must be taken into account. First, other idea attributes might exist that could afect cognitive overload and should therefore be considered as design principles. Consider, for example, a rater who has domain knowledge of artificial intelligence was assigned ideas on electric cars. The rater might be better utilized by considering a match between the rater's domain knowledge and the idea's domain. Yet, often the crowd rater's expertise is not known at the time of idea allocation. Should this information exist, an additional design principle could be conceptualized that matches raters expertise with idea subsets in the respective idea categories (DP3). Furthermore, there might be variables that influence the value of ex isting design principles, i.e., the timing of submission that afects the number of likes. Future research could extend the approach to also address additional design principles for idea allocation.

Second, the evaluation of SIA was done according to objective performance criteria that enabled testing for successful implementation of the design principles. They cannot confirm that raters' cognitive load and cognitive biases were altered. Hence, the evaluation should be understood as a proof of concept but not yet as a proof of value [51]. In order to establish a proof of value, future research should apply the SIA approach in the laboratory or the field with human raters. Data on raters' decision-making behavior and their perceptions would then provide the necessary insights, if SIA can in fact utilize cognitive biases and reduce cognitive load during idea evaluation.

## Acknowledgments

The research leading to the presented results was partially funded by the Austrian Science Fund (FWF): P 29765.

## References

[1] D. Arnott, Cognitive biases and decision support systems development: a design science approach. Information Systems Journal 16 (2006) 55–78

[2] V. Banken, I. Seeber, R. Maier, Comparing pineapples with lilikois: an experimental Analysis of the effects of idea similarity on evaluation performance in innovation contests, Proceedings of the 52nd Hawaii International Conference on System Sciences Maui Wailea 2019

[3] M. Beretta, Idea selection in web-enabled ideation systems, Journal of Product Innovation Management 36 (1) (2019) 5–23

[4] S. Bikhchandani, D. Hirshleifer, I. Welch, A theory of fads, fashion, custom, and cultural change as informational cascades, Journal of Political Economy 100 (5) (1992) 992–1025

[5] O.M. Bjelland, R.C. Wood, An inside view of IBM's ‘innovation jam’, MIT Sloan Management Review 50 (1) (2008) 32–40.

[6] I. Blohm, C. Riedl, J. Füller, J.M. Leimeister, Rate or trade? Identifying winning ideas in open idea sourcing, Information Systems Research 27 (1) (2016) 27–48

[7] E. Bonabeau, Decisions 2.0: the power of collective intelligence, MIT Sloan Management Review 50 (2) (2009) 45–52.

[8] P. Bordalo, N. Gennaioli, A. Shleifer, Salience and consumer choice, Journal of

Political Economy 121 (5) (2013) 803–843.

[9] K.J. Boudreau, K.R. Lakhani, Using the crowd as an innovation partner, Harvard Business Review 91 (4) (2013) 60–69

[10] R.O. Briggs, B.A. Reinig, Bounded ideation theory, Journal of Management Information Systems 27 (1) (2010) 123–144.

[11] L.W. Busenitz, J.B. Barney, Diferences between entrepreneurs and managers in large organizations: biases and heuristics in strategic decision-making, Journal of Business Venturing 12 (1) (1997) 9–30.

[12] G.B. Chapman, G.R. Bergus, A.S. Elstein, Order of information afects clinical judgment, Journal of Behavioral Decision Making 9 (3) (1996) 201–211.

[13] S. Chen, S. Chaiken, The heuristic-systematic model in its broader context, in: S. Chaiken, Y. Trope (Eds.), Dual-process Theories in Social Psychology, Guilford Press, New York, 1999, pp. 73–96.

[14] A. Chernev, U. Böckenholt, J. Goodman, Choice overload: a conceptual review and meta-analysis. Journal of Consumer Psychology 25 (2) (2012) 333–358

[15] H.W. Chesbrough, The era of open innovation, MIT Sloan Management Review 127 (3) (2003) 35–42.

[16] T.L. Childers, M.J. Houston, Conditions for a picture-superiority efect on consume memory, Journal of Consumer Research 11 (2) (1984) 643.

[17] P. Croskerry, G. Singhal, S. Mamede, Cognitive debiasing 1: origins of bias and theory of debiasing, BMJ Quality and Safety 22 (2013) ii58–ii65.

[18] B.G.C. Dellaert, T. Baker, E.J. Johnson, Partitioning sorted sets: overcoming choice overload while maintaining decision quality, Columbia Business School Research Paper, 2017.

[19] P.M. Di Gangi, M. Wasko, Steal my idea! Organizational adoption of user innova tions from a user innovation community: a case study of Dell IdeaStorm, Decision Support Systems 48 (1) (2009) 303–312.

[20] P.M. Di Gangi, M.M. Wasko, R.E. Hooker, Getting customers' ideas to work for you: learning from Dell how to succeed with online user innovation communities, MIS Quarterly Executive 9 (4) (2010) 213–228.

[21] C. Eickhof, Cognitive biases in crowdsourcing, Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining, ACM. New York, 2018

[22] D. Ellsberg, Risk, ambiguity, and the savage axioms, The Quarterly Journal of Economics 75 (4) (1961) 643–669.

[23] J.S.B.T. Evans, Dual-processing accounts of reasoning, judgment, and social cog nition, Annual Review of Psychology 59 (1) (2008) 255–278.

[24] E. Falkenauer, A. Delchambre, A genetic algorithm for bin packing and line bal ancing, Proceedings of International Conference on Robotics and Automation, vol. 2, IEEE, 1992, pp. 1186–1192

[25] A. Gatzweiler. V. Blazevic. E.T. Piller. Dark side or bright light: destructive and constructive deviant content in consumer ideation contests, Journal of Produc Innovation Management 34 (6) (2017) 772–789.

[26] K. Girotra, C. Terwiesch, K.T. Ulrich, Idea generation and the quality of the best idea, Management Science 56 (4) (2010) 591–605.

[27] T. Görzen, D. Kundisch, Can the crowd substitute experts in evaluating creative jobs? An experimental study using business models, Proceedings of the 24th European Conference on Information Systems. 2016.

[28] T. Görzen, D. Kundisch, When in doubt follow the crowd: how idea quality moderates the efect of an anchor on idea evaluation, Thirty Eighth International Conference on Information Systems, 2017.

[29] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Ouarterly 37 (2) (2013) 337–355.

[30] M.-L. Grisé, R.B. Gallupe, Information overload: addressing the productivity paradox in face-to-face electronic meetings. Journal of Management Information Systems 16 (3) (1999) 157–185.

[31] M.G. Haselton, D. Nettle, P.W. Andrews, The evolution of cognitive bias, The Handbook of Evolutionary Psychology, John Wiley & Sons Inc., 2005, pp. 724–746

[32] S. Hoornaert, M. Ballings, E.C. Malthouse, D. Van den Poel, Identifying new product ideas: waiting for the wisdom of the crowd or screening ideas in real time. Journa of Product Innovation Management 34 (5) (2017) 580–597.

[33] J.-H. Huang, Y.-F. Chen, Herding in online product choice, Psychology & Marketing 23 (5) (2006) 413–428.

[34] M.I. Hwang, J.W. Lin. Information dimension, information overload and decision quality, Journal of Information Science 25 (3) (1999) 213–218.

[35] E.J. Johnson, J.W. Payne, Efort and accuracy in choice, Management Science 31 (4) (1985) 395–414.

[36] Q. Jones, G. Ravid, S. Rafaeli, Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration, Information Systems Research 15 (2) (2004) 194–211.

[37] G. Jouret, Inside Cisco’ s search for the next big idea, Harvard Business Review 87 (9) (2009) 43–45.

[38] D. Kahneman, Thinking, Fast and Slow, Macmillan, New York, 2011, p. 499.

[39] M. Klein, A.C.B. Garcia, High-speed idea filtering with the bag of lemons, Decision Support Systems 78 (2015) 1–25.

[40] L.J. Kornish, K.T. Ulrich, Opportunity spaces in innovation: empirical analysis of large samples of ideas, Management Science 57 (1) (2011) 107–128

[41] L.J. Kornish. K.T. Ulrich. The importance of the raw idea in innovation: testing the sow's ear hypothesis, Journal of Marketing Research 51 (1) (2014) 14–26.

[42] K. Kyle, Measuring Syntactic Development in L2 Writing: Fine Grained Indices of Syntactic Complexity and Usage-based Indices of Syntactic Sophistication, Ph.D. thesis Georgia State University, 2016.

[43] G. Lauto, F. Valentin, How preference markets assist new product idea screening, Industrial Management and Data Systems 116 (3) (2016) 603–619

[44] M. Li, A. Kankanhalli, S.H. Kim, Which ideas are more likely to be implemented in online user innovation communities? An empirical analysis, Decision Support Systems 84 (2016) 28–40.

[45] N.K. Malhotra, Information load and consumer decision making, Journal of Consumer Research 8 (4) (1982) 419.

[46] R.E. Mayer, R. Moreno, Nine ways to reduce cognitive load in multimedia learning, Educational Psychologist 38 (1) (2003) 43–52

[47] G.A. Miller, The magical number seven, plus or minus two: some limits on out capacity for processing information, Psychological Review 65 (2) (1956) 81–97.

[48] A.A. Mitchell, J.C. Olson, Are product attribute beliefs the only mediator of advertising efects on brand attitude? Journal of Marketing Research 18 (3) (1981) 318.

[49] E.R. Mollick, R. Nanda, Wisdom or madness? Comparing crowds with expert eva luation in funding the arts, Management Science 62 (6) (2016) 1533–1553.

[50] Y. Nagar, P. de Boer, A.C.B. Garcia, Accelerating the review of complex intellectual artifacts in crowdsourced innovation challenges, Thirty Seventh International Conference on Information Systems, Dublin, 2016, pp. 1–17.

[51] J.F. Nunamaker Jr, R.O. Briggs, Toward a broader vision for information systems, ACM Transactions on Management Information Systems 2 (4) (2011) 1–12.

[52] D.E. O’Leary, On the relationship between number of votes and sentiment in crowdsourcing ideas and comments for innovation: a case study of Canada's digita compass, Decision Support Systems 88 (2016) 28–37.

[53] F. Paas, A. Renkl, J. Sweller, Cognitive load theory and instructional design: recent developments, Educational Psychologist 38 (1) (2003) 1–4.

[54] M. Rhyn, I. Blohm, A machine learning approach for classifying textual data in crowdsourcing, Proceedings of 13th International Conference on Wirtschaftsinformatik. St. Gallen. 2017. pp. 1171–1185.

[55] C. Riedl, I. Blohm, J.M. Leimeister, H. Krcmar, The effect of rating scales on decisior quality and user attitudes in online innovation communities, International Journa of Electronic Commerce 17 (3) (2013) 7–36.

[56] E.F. Rietzschel, B.A. Nijstad, W. Stroebe, Productivity is not enough: a comparison of interactive and nominal brainstorming groups on idea generation and selection, Journal of Experimental Social Psychology 42 (2) (2006) 244–251.

[57] A.G. Robinson, D.M. Schroeder, Ideas are Free: How the Idea Revolution is Liberating People and Transforming Organizations, Berrett-Koehler Publishers, 2004.

[58] B. Scheibehenne, R. Greifeneder, P.M. Todd, Can there ever be too many options? A meta-analytic review of choice overload, Journal of Consumer Research 37 (3) (2010) 409–425.

[59] B. Schemmann, A.M. Herrmann, M.M. Chappin, G.J. Heimeriks, Crowdsourcing ideas: involving ordinary users in the ideation phase of new product development, Research Policy 45 (6) (2016) 1145–1154.

[60] C. Schneider, M. Weinmann, J. vom Brocke, Digital nudging: guiding online user choices through interface design. Communications of the ACM 61 (7) (2018) 67–73.

[61] I. Seeber, D. Zantedeschi, A. Bhattacherjee, J. Füller, The more the merrier? The efects of community feedback on idea quality in innovation contests, Proceedings of the 50th Hawaii International Conference on System Sciences, 2017, pp. 4334–4343.

[62] D.K. Simonton, Scientific creativity as constrained stochastic behavior: the integration of product, person, and process perspectives, Psychological Bulletin 129

(4) (2003) 475–494.

[63] P. Slovic, S. Lichtenstein, Comparison of Bayesian and regression approaches to the study of information processing in judgment, Organizational Behavior and Human Performance 6 (1971).649–744

[64] J. Surowiecki, The Wisdom of the Crowds, Anchor Books, New York, 2005.

[65] J. Sweller, J.J.G. Van Merrienboer, F.G.W.C. Paas, Cognitive architecture and in structional design, Educational Psychology Review 10 (3) (1998) 251–296.

[66] O. Toubia, L. Florès, Adaptive idea screening using consumers, Marketing Science 26 (3) (2007) 342–360.

[67] A. Tversky, D. Kahneman, Judgement under uncertainty: heuristics and biases Science 185 (4157) (1974) 1124–1131.

[68] V.K. Velamuri, D. Schneckenberg, J.B.A. Haller, K.M. Moeslein, Open evaluation of new product concepts at the front end of innovation: objectives and contingency factors, R&D Management 47 (4) (2015) 501–521

[69] J.F. Yates, S.P. Curley, Contingency judgment: primacy efects and attention decrement. Acta Psychologica 62 (3) (1986) 293–302.

[70] Y. Zhu, S.M. Ritter, B.C.N. Müller, A. Dijksterhuis, Creativity: intuitive processing outperforms deliberative processing in creative idea selection, Journal of Experimental Social Psychology 73 (2017) 180–188

Victoria Banken is PhD candidate at the Department of Information Systems, Production and Logistics Management, University of Innsbruck, Austria, where she also earned her master's degree in Information Systems. Her research focuses on open innovation and crowdsourcing, in particular on idea selection by large groups of raters. She conceptualizes and develops decision support systems that deal with cognitive load and cognitive biases during idea evaluation.

Quirin Ilmer is PhD candidate at the Department of Information Systems, Production and Logistics Management, University of Innsbruck, Austria, where he also earned his master's degree in Information Systems. His research focuses on operations management, in particular the optimal allocation of resources in diferent environmental settings which aris e.g., in the steel industry, dual resource constrained job shops or crowdsourcing. He develops decision support systems based on optimization techniques.

Isabella Seeber is Assistant Professor at the Department of Information Systems, Production and Logistics Management, University of Innsbruck, Austria. Her research focuses on team- and crowd-based innovation, Collaboration Engineering, digital nud ging, and conversational agents in team collaboration. Her research has appeared in journals such as Journal of Management Information Systems, Computers in Human Behavior, Information & Management, and Group Decision and Negotiation.

Stefan Haeussler received his PhD at the Department of Information Systems, Production and Logistics Management, University of Innsbruck, Austria. His areas of interest include manufacturing planning and control, simulation modeling, workload control, optimiza tion models. forecasting, regression and behavioral operations management.
