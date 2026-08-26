---
otero_id: 17215
otero_key: "455P2B4U"
title: "Integrating databases and preference evaluations in group decision support"
authors: "Rudolf Vetschera"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90078-p"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating databases and preference evaluations in group decision support

A feedback-oriented approach

Rudolf Vetschera

Institut für Betriebswirtschaftslehre der Universität Wien, A-1090 Vienna, Austria

The paper introduces a new concept for group decision support that explicitly incorporates feedbacks from the group level to the individual decision processes. We first show that the representation of such feedback processes requires additional concepts beyond individual database views for group members. We then develop two basic techniques for incorporating group opinions into the individual decision process: explicit and implicit feedback. We show that explicit feedback also solves the database-related problems identified before while implicit feedback more closely corresponds to practical group processes. Therefore, a unified approach combining both techniques is developed. Application of these feedback concepts to a utility-based decision framework leads to a formal model, which is analyzed and illustrated by a numerical example.

Keywords: Group decision support systems, Feedback, Utility.

## 1. Introduction

The increasing complexity of the socio-economic environment makes it less and less possible for single decision makers to consider all relevant aspects of problems. Therefore, many organizations employ groups in decision making. This trend also has important consequences for research on decision support, where Group Decision Support Systems (GDSS) intended to aid multiple cooperating decision makers have become an important topic.

member of TIMS and the Operational Research Society and has published among others in OR Spektrum, Computers and Operations Research and the Journal of Economic Behaviour and Organization.

The overall structure of a GDSS as it is now widely seen in the literature can be described by the hierarchical model shown in fig. 1.

According to this model, a GDSS consists of two distinct levels: an individual level providing support for the group members, and a group level supporting the aggregation of individual opinions. While this overall scheme is widely used in the literature, different branches of research have focused on different parts of the model. One branch sees GDSS as an extension of decision support systems for single users. This branch is strongly focused on databases, data presentation and analyses (Hurrion, 1985; DeSanctis/Gallupe, 1987; Huber, 1984). In a process-oriented view of the hierarchical model of fig. 1, these support functions relate to the bottom layer, in which individuals obtain factual information on available decision alternatives.

![](/api/attachments/455P2B4U/fulltext/images/1c70f1e919426444c8890d7de0029b24ee510798bdd5936c5b70c2e482203f91.jpg)

Rudolf Vetschera is an Assistant Professor at the Department of Management, University of Vienna. He holds a Master's Degree in Economics and Computer Science from the University of Vienna and the Technical University of Vienna and a Ph.d. in Economics and Social Sciences from the University of Vienna. His current research interest is in combining decision theory and information technology in developing advanced approaches to decision support. He is a

![](/api/attachments/455P2B4U/fulltext/images/0865aa30c811dcde26cc812c040a7a10a87a67de5c281c36dad5418cbbf16192.jpg)  
Fig. 1. Structure of GDSS.

The other branch of GDSS research is based on decision theory and tries to develop theoretically founded methods for the evaluation and aggregation of preferences (Jarke et al., 1987; Stohr, 1981; Lewandowski et al., 1986). These functions correspond to the second part of the individual level and the group level in fig. 1.

The model represented in fig. 1 is often also understood to describe the temporal sequence of activities carried out in group decisions: it is assumed that the decision process proceeds in a way that group members first determine their own opinions about decision alternatives and these opinions are then aggregated through the group process.

While it is obvious that group members must first obtain some information about alternatives and start forming their own opinions, this view ignores the importance of feedback effects from the group to individual levels. The opinions of other group members will often cause one member to reconsider and modify his evaluation. For example, finding out that other group members pay considerable attention to one attribute might lead a member to give this attribute also more importance. Such feedbacks from the group to individual opinions are both an empirically observable phenomenon in group decisions (Pruitt, 1971) and important for the ongoing support of a joint decision in its implementation phase (Castore/Murninghan, 1978).

Considering feedback structures in a GDSS increases the complexity of the information structure of the system. In this paper, we first show (in section 2) that this increased complexity cannot be dealt with by existing approaches. In section 3 we introduce an approach for feedback-oriented group decision support. Section four then shows how these general principles can be employed to develop a comprehensive GDSS in a utility-based decision framework. Section 5 provides a numerical example and section 6 concludes the paper and discusses some topics for further research.

## 2. Database Views and Decision Alternatives

Database-oriented approaches to GDSS are often aimed at providing group members with individual views of the problem. These views contain only information relevant to that particular member and thus reduce cognitive strain.

A basic assumption underlying this approach is that group members are interested only in a subset of criteria. This assumption can be justified from an organizational point of view (Laux/Liermann, 1987): Organizations often delegate decisions to a group because individual group members have specialized knowledge of different particular areas that otherwise cannot be brought together in the decision process. However, different individual problem representations lead to difficulties when feedbacks from the group to the individual level take place.

For simplicity, we assume that the group's decision problem can be described by a finite set of alternative characterized by a finite set of attributes. Information about the alternatives is contained in one relation of a relational database. The attributes in the relation are the criteria considered, the records correspond to decision alternatives. We thus ignore a possible intervening step of deriving criteria values from the actual data, which might be of importance in practical group processes (Kull, 1982; Steeb/Johnston, 1981; Hurrion, 1985; Eilon/Cosmetatos, 1980). These aspects can also be incorporated in our framework. Their inclusion, however, would increase the complexity of exposition without offering additional insight into the problems.

Individual views can be generated from the common database by applying relational database operators. The simplest possibility is to apply the projection operator to reduce the relation to those attributes in which a member is interested (Jarke et al, 1987). Other transformations might also be applied, e.g. if a group member explicitly wants to combine records into a single alternative (for an example see Jarke et al., 1987, pp. 332–333). As most problems can be shown for the projection case, we will only consider that case in this paper.

Problems arise because the set of alternatives (database records) resulting from projection might be different for each group member. The differences arise as records differing only in the deleted attributes are combined into a single record.

This effect is shown in fig. 2. Considering only two group members, we can partition the set of attributes into four subsets: $A_{1}$ is the set of attributes in which only member 1 is interested. $A_{2}$ contains attributes considered only by member 2, $A_{b}$ attributes considered by both members and

![](/api/attachments/455P2B4U/fulltext/images/7aecf02cdae5b6fcfc84cfc82196e9fd36ca8d65d3d1e3dfcbf2ff6172850fe6.jpg)  
Fig. 2. Different sets of alternatives generated by database views.

$A_{n}$ those considered by none. The projection on $A_{b}$ then defines a partition of the entire relation into subsets of records. Records in each class of this partition result in one record in the projection. These subsets are further partitioned differently in the individual views. The individual views are projections onto the union of $A_{1}$ with $A_{b}$ and on the union of $A_{2}$ with $A_{b}$ , respectively. Therefore, records of the original relation that are projected onto the same record in one of the views must have identical values in all the attributes in $A_{b}$ and thus will be projected onto the same record in the projection onto $A_{b}$ .

As long as a group decision support system is only concerned with the aggregation of individual opinions, the creation of different “alternatives” for group members need not be a problem. One could imagine an approach in which group members perform individual evaluations over the (sub-)sets of alternatives and criteria contained in their views. They communicate their evaluation to the GDSS in a general format, e.g. as a utility function. The GDSS then internally expands this description to the complete set of all alternatives and criteria. Each alternative in a group member’s view corresponds to an equivalence class of group alternatives. As all alternatives in a class have the same values in the attributes in the member’s view, the group member is indifferent between alternatives in a class. Aggregation is then based on those expanded individual representations.

When feedbacks are considered, a mapping back from the group representation to the individual views is required. In dealing with individual views, database theory has mainly considered updating problems and has shown that considerable problems exist for this case (Furtado/Casanova, 1985). The mapping of orderings of alternatives onto simplified views is a conceptually similar problem. In database updates, one has to describe operations that take place on the full database in terms of restricted views. In our case, information about an ordering defined on the full database would have to be represented within a view. If the view contains fewer records than the group database and the group ranks alternatives in the same equivalence class of a member differently, this is not possible. Individual views that contain only a limited subset of alternatives therefore are not a sufficient basis for providing feedback-oriented group decision support.

This problem could theoretically be solved by including the key attributes of the original relation in the individual views. But this approach would force each group member to deal with attributes in which he/she is not interested and which might not have any meaningful interpretation to him/her.

## 3. A Framework of Feedback-Oriented Group Decision Support

In this section, we develop a general framework for group decision support that combines the reduction in cognitive strain provided by individual views with feedback processes. To develop this concept, we first have to discuss feedback structures in general.

Feedback in our context means that a group member changes his or her preferences so that they more closely reflect the other group members' preferences as perceived by that member. Such a change can be made in two distinct ways: either the group member changes the structure of the existing evaluation system (e.g. by giving some attributes more or less attention) or the group's opinion is explicitly taken into account as an additional attribute.

Changing the importance of attributes seems to be an attractive way of representing feedbacks. It closely corresponds to practical experience in group discussions, where convincing other group members is often attempted by pointing out the importance of certain problem characteristics. On the other hand, it can be shown for a utility-based decision framework that changes in attribute weights do not always provide sufficient changes in preferences (Vetschera, 1988).

The second possibility is to introduce an additional attribute containing information about the other group members' preferences. This attribute will also solve the problem of different sets of alternatives in the individual views. Whenever the other group members evaluate alternatives in one equivalence class of a member differently, these alternatives will also have different values in the group evaluation attribute. Projection on the attributes initially in the member's view plus the group attribute thus will yield a relation containing distinct records for all alternatives.

The group evaluation attribute will also cause less cognitive strain than dealing with all attributes or the key attributes. It can be easily interpreted by each group member as an aggregation of all the other members' special knowledge that warrants a distinction between otherwise identical alternatives.

The main issue in this paper is to support a joint decision making effort of a group of common interests, but different specialized knowledge. This assumption is essential for aggregating all the other members' views into one single criterion, without further questioning the justification of such information. If a group member would not trust the others to provide their information according to their best knowledge and in the best interest of the group, he/she would probably want to disaggregate this evaluation further and find out more precisely why some alternatives are preferred by the other members.

The overall design of an integrated GDSS is shown in a dynamic perspective in fig. 3: The process starts with individual evaluations based on individual views of the problem, which contain only part of the attributes and equivalence classes of alternatives. The GDSS constructs a common problem representation for the group containing all alternatives and attributes in full detail. It then maps the individual evaluations onto this representation (A). Using these representations, the GDSS then constructs for each group member an aggregated view of the other members' opinions (B). Agreement is reached when all these views are identical. The aggregated views are then communicated back to the group members (C), who modify their evaluations and provide information about their modified opinions (D).

![](/api/attachments/455P2B4U/fulltext/images/5f29c6f164f2d0af64853f203449f3a506287ea3fda2342f719a4a92c84728eb.jpg)  
Fig. 3. Design of a feedback-oriented GDSS.

## 4. A Utility-Based Approach

We will now develop a specific model to describe the general principles outlined in the preceding section. In this model, we use utility functions (more specifically, riskless value functions as proposed by Keeney/Raiffa, 1976) to represent preferences. This should not indicate that the general framework developed above is applicable only if multiattribute utility theory is used in the individual decision processes. The framework can also be applied to other decision techniques based on different assumptions. Utility theory is used in this example because of its wide theoretical acceptance and because it is a straightforward way to represent preferences.

We will analyze a decision problem in which M group members m are evaluating a set of N decision alternatives n according to K criteria k. The opinion of group member m about these alternatives in iteration i is described by a measurable value function $U_{m}^{(i)}(n)$ :

$$
U _ {m} ^ {(i)} (n) = \sum_ {k} w _ {m, k} ^ {(i)} u _ {m, n, k} ^ {(i)},\tag{1}
$$

where $w_{m,k}$ is the weight of attribute k ( $\Sigma w_{k}=1$ ) and $u_{m,n,k}$ is the partial utility value of alternative n in attribute k for member m. For brevity, we will omit the iteration index (i) and the group member index m unless necessary.

While (1) formally represents a value function as commonly used in multi-attribute utility theory, its interpretation is different. (1) represents the group member's opinion about alternatives at one specific point in time. One main point we are making in this paper is that individual evaluations will undergo changes in the group process and gradually converge to a common opinion. This deviates from the notion about stable preferences commonly found in the utility-oriented literature.

Utility function (1) implies a cardinal evaluation of alternatives by group members. This does not necessarily mean that this information is also fully used in the aggregation and feedback processes of stages (B) and (C) in fig. 3. Cardinal preference information also implies ordinal information. Therefore it is possible for the receiver of such information to use it only as ordinal information, while the contrary (cardinal use of ordinal information) is not possible.

It would therefore be possible to use only ordinal information (i.e. the group member's ranking of alternatives) in the aggregation process of step (B). In this case, only a group ranking could be transmitted back in step (C). If a cardinal aggregation process is used in step (B), cardinal or ordinal information could be transmitted back to the member in step (C).

In this example, we will only consider a system based entirely on cardinal information. Using ordinal information in the feedback process might, however, make the individual adaptation process easier as it can be interpreted more flexibly by the group member. These issues are analyzed in detail in an ongoing research project.

The aggregation of cardinal individual evaluations to a cardinal group evaluation is possible under certain restrictions on individual preferences as well as the group's preferences (Dyer/Sarin, 1979). Using utility functions to describe preferences, this aggregation takes the form of an additive weighting of individual utilities. For group member m, the aggregated ranking of the other members becomes:

$$
U _ {g} (n) = \sum_ {\mu \neq m} \alpha_ {\mu} \sum w _ {\mu , k} u _ {\mu , n, k},\tag{2}
$$

where $\alpha_{\mu}$ are weights for the group members. Consensus is achieved if the ranking of alternatives implied by $U_{g}$ is identical with the ranking implied by $U_{m}$ for all group members m.

As long as differences exist that prevent the group from finding a solution, the aggregated opinions represented by (2) are transmitted back to the group members to induce a revision of individual evaluations. In this feedback structure, group level information is actually used by the member in two ways. The first use is to measure the difference between the group and the individual opinion, the second is the group opinion attribute introduced in section 3 above.

How the difference between individual and group opinions is measured depends on the decision problem the group is facing. In many instances, it will be sufficient if agreement among group members is reached in terms of ordinal preferences, i.e. in terms of a common ranking of alternatives.

Group decisions often involve only the selection of a top ranked alternative. In this paper, we will use a generalization that allows us to consider both the ranking of all alternatives and the selection of a single alternative as special cases. We introduce the concept of a c-agreement between individual and group rankings. A c-agreement between two rankings means that the first c alternatives of the two rankings are identical. The remaining alternatives might be ranked differently, but follow the alternative ranked on position c in both rankings.

For incorporating the other members' opinion in an individual evaluation, however, considering only ordinal rankings might not be sufficient. It might be of interest for the member not only to consider that the others prefer a certain alternative to another, but also how strongly they do so. In this paper, we will therefore present a model in which cardinal group information is used to modify the individual evaluations.

In this case the value function from the group level can directly be used as a partial utility function of an additional attribute. We will label this additional attribute g for “group evaluation”. Incorporating g into (1), we obtain:

$$
U ^ {\prime} (n) = \sum_ {k} w _ {k} u _ {n, k} + w _ {g} u _ {n, g}.\tag{3}
$$

The importance the group member assigns to the other members' opinions in his own evaluation is represented here by a weight $w_{g}$ . The (cardinal) information about the other members' preferences is contained in $u_{n,g} = U_{g}(n)$ . In the process of achieving consensus, the group member will change his/her evaluation so that (3) produces the same ranking as the evaluation of the other members for the first $c$ alternatives. For simplicity, we assume that changes are made only in the weights $w_{k}$ , not in the partial utility evaluations. A model based on changes in the partial utility functions is described in Vetschera (1988).

As we have already discussed, agreement between individual and group rankings can either be brought about by giving the group attribute sufficient weight or by a sufficiently large change in the weights of other attributes. We will first discuss the two possibilities separately before developing an integrated model.

Introducing the group attribute without changing the relative importance of other attributes can be achieved by a proportional reduction in the other weights. When the group attribute is established in the first iteration, the weights of all other attributes are changed to

$$
w _ {k} ^ {\prime} = \left(1 - w _ {g}\right) w _ {k}.\tag{4}
$$

As $\Sigma w_{k}=1$ , the total reduction in the weights $w_{k}$ is equal to $w_{g}$ , so the overall scaling is preserved by this transformation. The same transformation can be applied in subsequent iterations if the group attribute is temporarily discarded and the other weights are rescaled to sum up to 1.

Changes in the structure of the other weights also have to preserve the overall scaling of weights. Denoting the increase in weight $w_{k}$ by $\delta_{k}^{+}$ and its decrease by $\delta_{k}^{-}$ , we obtain:

$$
w _ {k} ^ {\prime} = w _ {k} + \delta_ {k} ^ {+} - \delta_ {k} ^ {-} \quad \text { with }\tag{5}
$$

$$
\sum_ {k} \delta_ {k} ^ {+} - \delta_ {k} ^ {-} = 0.\tag{6}
$$

These two transformations can be combined in two possible ways. Either the changes in other attributes are performed first:

$$
w _ {k} ^ {\prime} = \big (w _ {k} + \delta_ {k} ^ {+} - \delta_ {k} ^ {-} \big) \big (1 - w _ {g} \big),\tag{7}
$$

or the group attribute is introduced first:

$$
w _ {k} ^ {\prime} = w _ {k} \left(1 - w _ {g}\right) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}.\tag{8}
$$

Using (8), it is possible to formulate a linear model for the total modification process, while (7) would lead to a nonlinear model. For our further analysis, we will therefore use (8).

The feedback problem now consists in finding a transformation according to (8) that will lead to a c-agreement between individual and group rankings and is acceptable to the group member. We suppose that the member will more likely accept a transformation the smaller the total change is. In order to formulate an optimization model to determine such a transformation, we have to operationalize the amount of change in the utility function.

The total change consists of two parts: modification of the original attribute weights and the weight given to the group attribute. The modification in original attribute weights can be measured by $\delta_{k}^{+}$ and $\delta_{k}^{-}$ . As any weight taken away from one attribute must be assigned to some other attributes, it is sufficient to use one of the two groups of variables in the objective function. The first component can thus be defined as $\Sigma\delta_{k}^{+}$ .

The change required by introducing the group attribute can conveniently be measured through the value of $w_{g}$ . As the weight given to the group opinion always indicates a deviation from the individual opinion, $w_{g}$ (rather than its increase above the previous iteration) can be used in all iterations of the process.

These two actually are different objectives measuring different types of change. It is, however, reasonable to assume that the two different types can be linearly substituted, so the two components can be additively aggregated into one objective. The rate of substitution need not be determined a priori. We can thus define an overall objective describing the total change required to reach c-agreement as:

$$
\sum \delta_ {k} ^ {+} + G w _ {g},\tag{9}
$$

where G is a weight used to represent different rates of substitution between the two kinds of change. G can be varied parametrically to study different possibilities for adaptation.

To simplify the exposition, we assume that the alternatives are numbered according to the group ranking, i.e. the other members prefer alternative 1 to alternative 2 etc. In order to reach a c-agreement with this ranking, the modified weights must fulfill the conditions

$$
\begin{array}{l} \sum w _ {k} ^ {\prime} u _ {1, k} + w _ {g} u _ {1, g} > \sum w _ {k} ^ {\prime} u _ {2, k} + w _ {g} u _ {2, g}, \\ \sum w _ {k} ^ {\prime} u _ {2, k} + w _ {g} u _ {2, g} > \sum w _ {k} ^ {\prime} u _ {3, k} + w _ {g} u _ {3, g}, \\ \dots \\ \sum w _ {k} ^ {\prime} u _ {c - 1, k} + w _ {g} u _ {c - 1, g} > \sum w _ {k} ^ {\prime} u _ {c, k} + w _ {g} u _ {c, g}, \end{array}\tag{10}
$$

for the first $c$ alternatives and

$$
\begin{array}{l} \sum w _ {k} ^ {\prime} u _ {c, k} + w _ {g} U _ {c, g} > \sum w _ {k} ^ {\prime} u _ {c + 1, k} + w _ {g} u _ {c + 1, g}, \\ \sum w _ {k} ^ {\prime} u _ {c, k} + w _ {g} U _ {c, g} > \sum w _ {k} ^ {\prime} u _ {c + 2, k} + w _ {g} u _ {c + 2, g}, \\ \dots \\ \sum w _ {k} ^ {\prime} u _ {c, k} + w _ {g} U _ {c, g} > \sum w _ {k} ^ {\prime} u _ {N, k} + w _ {g} u _ {N, g}, \end{array}\tag{11}
$$

to generate the ranking of the next alternatives. Taking also into account the balancing conditions on $\delta_{k}^{+}$ and $\delta_{k}^{-}$ and the fact that weights must not become negative, we obtain the following linear programming model:

$$
\begin{array}{l} \text { minimize } \sum \delta_ {k} ^ {+} + G w _ {g} \quad \text { s.t. } \\ \sum_ {k} (u _ {n, k} - u _ {n + 1, k}) (- w _ {k} w _ {g} + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}) \\ \quad + (u _ {n, g} - u _ {n + 1, g}) w _ {g} > - \sum_ {k} (u _ {n, k} - u _ {n = 1, k}) w _ {k}, \\ n = 1 \dots c - 1 \\ \sum_ {k} (u _ {c, k} - u _ {n + 1, k}) (- w _ {k} w _ {g} + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}) \\ \quad + (u _ {c, g} - u _ {n + 1, g}) w _ {g} > - \sum_ {k} (u _ {c, k} - u _ {n + 1, k}) w _ {k}, \\ n = c \dots N - 1 \\ \sum_ {k} \delta_ {k} ^ {+} - \sum_ {k} \delta_ {k} ^ {-} = 0, \\ w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-} \geq 0, \quad k = 1 \dots K \end{array}\tag{12}
$$

Optimization models similar to the model above have been used to determine criteria weights in several assessment techniques for multi-attribute decision problems (Klein et al., 1985; Huber, 1974; Schoemaker/Waid, 1982; Weber, 1987). Our model differs from these techniques in several aspects. In estimation problems, the ranking implied by the utility function to be estimated should correspond as closely as possible to the user's responses. However, if responses are not consistent, it cannot be guaranteed that all preference statements can be represented. Therefore, some distance between the implied ranking and the responses is minimized. In our problem, the group ordering is consistent. It can therefore be formulated as a set of constraints. On the other hand, the problem is one of changing a utility function, not of estimating an entirely new function. There fore, the amount of change required becomes important and is used in the objective function. In estimation problems, no similar concept exists.

Parametric variation of coefficient G in (12) will lead to trade-off curves between the two objectives $\Sigma\delta_{k}^{+}$ and $w_{g}$ . These curves will always be convex (i.e. exhibit decreasing rates of substitution) as they are the projection of the convex feasible set of (12) onto the two-dimensional objective space. Furthermore, it can be shown that trade-off curves for higher values of c will always lie to the right of and above curves for lower values of c, i.e. the objective value of (12) will not decrease for increasing values of c.

For any given value of $c$ , as

$$
\begin{array}{l} \sum_ {k} \left(w _ {k} \left(1 - w _ {g}\right) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c - 1, k} + w _ {g} u _ {c - 1, g} \\ > \sum_ {k} \left(w _ {k} \left(1 - w _ {g}\right) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c, k} + w _ {g} u _ {c, g}, \end{array}\tag{13}
$$

and

$$
\begin{array}{l} \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c, k} + w _ {g} u _ {c, g} \\ \quad > \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c + 1, k} \\ \quad + w _ {g} u _ {c + 1, g}, \\ \quad \dots \\ \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c, k} + w _ {g} u _ {c, g} \\ \quad > \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+ -} - \delta_ {k} ^ {-}\right) u _ {N, k} + w _ {g} u _ {N, g}, \end{array}\tag{14}
$$

we can add redundant constraints

$$
\begin{array}{l}\sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c - 1, k} + w _ {g} u _ {c - 1, g}\\\quad > \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c + 1, k}\\\quad + w _ {g} u _ {c + 1, g},\\\quad \dots\\\sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c - 1, k} + w _ {g} u _ {c - 1, g}\\\quad > \sum_ {k} \left( \right.w _ {k} (1 - w _ {g}) + \delta_ \textit \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf (\textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf \textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\textbf {\x}}}}}}}}}}}}}}}}}}\\\quad + w _ {g} u _ {c + 1, g},\\\quad \dots\\\end{array}\tag{15}
$$

Table 3

without changing the optimal solution. Thus the model for a given value of c is identical with the model for c-1 plus an additional set of constraints

$$
\begin{array}{l} \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c, k} + w _ {g} u _ {c, g} \\ \quad > \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c + 1, k} \\ \quad + w _ {g} u _ {c + 1, g}, \\ \quad \dots \\ \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {k} ^ {+} - \delta_ {k} ^ {-}\right) u _ {c, k} + w _ {g} u _ {c, g} \\ \quad > \sum_ {k} \left(w _ {k} (1 - w _ {g}) + \delta_ {g} ^ {+} - \delta_ {k} ^ {-}\right) u _ {N, k} + w _ {g} u _ {N, g}. \end{array}\tag{16}
$$

As in a minimization model the optimal objective value never decreases when additional constraints are introduced, the optimal objective value for model (12) will not decrease as c is increased.

## 5. Numerical Example

In this section, we will illustrate the approach developed above by a numerical example. To allow for comparison to other approaches to group decision support, we will use an example already presented in the literature (Jarke et al., 1987). We consider a group of two persons, who has to decide about the purchase of a car. The group has already identified 10 possible options, which are listed in table 1.

For simplicity, we assume that both members have identical, linear partial utility functions. The partial utility values resulting from this assumption are given in table 2.

Group member A uses weights (0.15, 0.20, 0.50, 0.15), member B (0.05, 0.75, 0.20, 0). Although member B does not use attribute “Speed” in his evaluation, he can distinguish between all alternatives by regarding the other attributes.

Table 2 Partial utility values.  
Table 1
Data on decision alternatives.  
Utility values and ranks of alternatives for both members.

<table><tr><td>Car</td><td>Fuel</td><td>Space</td><td>Price</td><td>Speed</td></tr><tr><td>Opel Record</td><td>0.3984</td><td>0.8482</td><td>0.5679</td><td>0.9077</td></tr><tr><td>Peugeot 505</td><td>0.4742</td><td>0.8244</td><td>0.5147</td><td>0.8615</td></tr><tr><td>Peugeot 104</td><td>0.7307</td><td>0.0000</td><td>0.7957</td><td>0.6769</td></tr><tr><td>Citroen Diane</td><td>1.0000</td><td>0.2083</td><td>1.0000</td><td>0.0000</td></tr><tr><td>VW Golf</td><td>0.5387</td><td>0.3095</td><td>0.7181</td><td>0.4769</td></tr><tr><td>Mercedes 230</td><td>0.4113</td><td>1.0000</td><td>0.0000</td><td>0.9692</td></tr><tr><td>Citroen CX</td><td>0.3065</td><td>0.8780</td><td>0.2161</td><td>0.9385</td></tr><tr><td>Volvo 244</td><td>0.0000</td><td>0.9732</td><td>0.4067</td><td>0.4308</td></tr><tr><td>BMW 520</td><td>0.1113</td><td>0.8036</td><td>0.1396</td><td>1.0000</td></tr></table>

Possible modifications, c = 6, Member A.

<table><tr><td>Car</td><td>Fuel</td><td>Space</td><td>Price</td><td>Speed</td></tr><tr><td>Opel Record</td><td>10.48</td><td>7.96</td><td>46700</td><td>176</td></tr><tr><td>Peugeot 505</td><td>10.01</td><td>7.88</td><td>49500</td><td>173</td></tr><tr><td>Peugeot 104</td><td>8.42</td><td>5.11</td><td>35200</td><td>161</td></tr><tr><td>Citroen Diane</td><td>6.75</td><td>5.81</td><td>24800</td><td>117</td></tr><tr><td>Citroen Visa</td><td>7.30</td><td>5.65</td><td>32100</td><td>142</td></tr><tr><td>VW Golf</td><td>9.61</td><td>6.15</td><td>39150</td><td>148</td></tr><tr><td>Mercedes 230</td><td>10.40</td><td>8.47</td><td>75700</td><td>180</td></tr><tr><td>Citroen CX</td><td>11.05</td><td>8.06</td><td>64700</td><td>178</td></tr><tr><td>BMW 520</td><td>12.26</td><td>7.81</td><td>68593</td><td>182</td></tr></table>

<table><tr><td rowspan="2">Car</td><td colspan="2">Member A</td><td colspan="2">Member B</td></tr><tr><td>Utility</td><td>Rank</td><td>Utility</td><td>Rank</td></tr><tr><td>Opel Record</td><td>0.6504</td><td>3</td><td>0.7700</td><td>3</td></tr><tr><td>Peugeot 505</td><td>0.6226</td><td>4</td><td>0.7450</td><td>4</td></tr><tr><td>Peugeot 104</td><td>0.6090</td><td>5</td><td>0.1957</td><td>10</td></tr><tr><td>Citroen Diane</td><td>0.6917</td><td>1</td><td>0.4063</td><td>7</td></tr><tr><td>Citroen Visa</td><td>0.6548</td><td>2</td><td>0.3374</td><td>9</td></tr><tr><td>VW Golf</td><td>0.5733</td><td>6</td><td>0.4027</td><td>8</td></tr><tr><td>Mercedes 230</td><td>0.4071</td><td>9</td><td>0.7706</td><td>2</td></tr><tr><td>Citroen CX</td><td>0.4704</td><td>7</td><td>0.7170</td><td>5</td></tr><tr><td>Volvo 244</td><td>0.4626</td><td>8</td><td>0.8112</td><td>1</td></tr><tr><td>BMW 520</td><td>0.3972</td><td>10</td><td>0.6362</td><td>6</td></tr></table>

<table><tr><td>G</td><td> $w_g$ </td><td> $δ_1$ </td><td> $δ_2$ </td><td> $δ_3$ </td><td> $δ_4$ </td><td> $Σδ_k^+$ </td></tr><tr><td>≤ 0.3380</td><td>0.998</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>-0.5416</td><td>0.690</td><td>0.000</td><td>0.104</td><td>-0.104</td><td>0.000</td><td>0.104</td></tr><tr><td>-0.5500</td><td>0.127</td><td>0.000</td><td>0.409</td><td>-0.278</td><td>-0.131</td><td>0.409</td></tr><tr><td>&gt;0.5500</td><td>0.000</td><td>0.013</td><td>0.479</td><td>-0.316</td><td>-0.150</td><td>0.479</td></tr></table>

![](/api/attachments/455P2B4U/fulltext/images/083b393bce3f17eca16cf43eb4380a5ede023c666bbec708959587aa3a7a688b.jpg)  
Fig. 4. Trade-off curves for member A.

The partial utility values and weights indicated above lead to the individual evaluations listed in table 3.

Since the group consists of only two members, no aggregation is necessary. One member's evaluation directly corresponds to the group evaluation for the other member.

For brevity, we will only present the modification process for one member, member A, in detail. Setting, for example, parameter c to a value of 6 leads to the solutions of model (12) listed in table 4.

Similar calculations can be performed for all possible values of c, leading to the trade-off curves shown in fig. 4. For member A, only three different curves exist: the outermost curve holds for c = 1, the next for c = 2 to c = 6 and the last curve for c = 7 to c = 10. This figure also shows that the trade-off curves are convex and that curves for higher values of c are dominated by or equal to curves for lower values.

![](/api/attachments/455P2B4U/fulltext/images/912a8c900fb6cda6bad3e75d89420fe1e1ace24d3ef6971dac63ac1154a9ee82.jpg)  
Fig. 5. Trade-off curves for member B.

Modified utility values and ranks of alternatives for both members.

<table><tr><td rowspan="2">Car</td><td colspan="2">Member A</td><td colspan="2">Member B</td></tr><tr><td>Utility</td><td>Rank</td><td>Utility</td><td>Rank</td></tr><tr><td>Opel Record</td><td>0.7624</td><td>1</td><td>0.7285</td><td>1</td></tr><tr><td>Peugeot 505</td><td>0.7318</td><td>2</td><td>0.7050</td><td>2</td></tr><tr><td>Peugeot 104</td><td>0.3575</td><td>10</td><td>0.3717</td><td>10</td></tr><tr><td>Citroen Diane</td><td>0.5298</td><td>7</td><td>0.5923</td><td>4</td></tr><tr><td>Citroen Visa</td><td>0.4721</td><td>8</td><td>0.5138</td><td>7</td></tr><tr><td>VW Golf</td><td>0.4703</td><td>9</td><td>0.4622</td><td>8</td></tr><tr><td>Mercedes 230</td><td>0.6409</td><td>4</td><td>0.5858</td><td>5</td></tr><tr><td>Citroen CX</td><td>0.6348</td><td>5</td><td>0.5759</td><td>6</td></tr><tr><td>Volvo 244</td><td>0.6775</td><td>3</td><td>0.5965</td><td>3</td></tr><tr><td>BMW 520</td><td>0.5416</td><td>6</td><td>0.4559</td><td>9</td></tr></table>

For member B, the trade-off curves shown in fig. 5 can be obtained.

Let us assume that member A is willing to change his evaluation system according to the proposal listed in the second line of table 4, but will only make half of this change. This leads to a value of $w_{g}=0.345$ and a change vector of weights of (0.0, 0.052, -0.052, 0.0). The new vector of weights for member A then becomes (0.098, 0.183, 0.275, 0.098). If B similarly performs half the change obtained for c=6, which leads to $w_{g}=0.151$ and weights (0.166, 0.503, 0.170, 0.009), the modified evaluations listed in table 5 are obtained.

These modifications have therefore led to consensus on the first three alternatives (Opel Record, Peugeot 505 and Volvo 244) as well as to a considerable agreement on the ranking of the other alternatives.

## 6. Conclusions and Topics for Further Research

In this paper, we introduced a comprehensive framework for group decision support that combines data and preference-oriented approaches in a dynamic, feedback-oriented context. We discussed the various problem representations and flows of information in a group decision support system, both from the individual to the group level and vice versa. It turned out that it is possible to construct individual problem views that are based on only a subset of attributes and thus provide cognitive simplification to the group members, but these views must allow each group member to distinguish between all alternatives open to the group. This distinction can be achieved by introducing an additional attribute in each view representing the aggregated opinion of all other group members.

We have developed this general framework into a utility-based feedback model describing the changes in individual opinions required to achieve consensus. While we demonstrated only the cardinal use of group information, such models can also be constructed for the case of communicating ordinal preference information. Our formal model exhibits highly plausible behavior with regard to several aspects of group decision making: more comprehensive consensus is much harder to achieve. In our framework, more comprehensive consensus means that more alternatives have to be ranked unanimously by the group. The model also exhibits “decreasing returns” when weight to the explicit group attribute is substituted for changes in the other attribute weights.

These plausible results indicate that our approach is a viable instrument for providing formalized support for such important aspects of group decisions as feedbacks and changes in individual opinions that up to now have received little attention in the group decision support literature. While it can be shown directly that those results hold in general, further work is required to analyze how various factors like problem dimension or the degree of overlap between attribute sets considered by individual group members affect those results quantitatively. Ongoing work is also dealing with the problem of cardinal vs. ordinal consideration of group opinions. While it is obvious that cardinal evaluations require more changes than ordinal evaluations, the amount of difference and its determining factors remain to be studied in detail. For practical application, these results also have to be generalized beyond the decision framework provided by utility theory. Alternative techniques based e.g. on outranking relations (Roy/Vincke, 1981) or reference points (Wierzbicki, 1980) would allow the individual group members more flexibility in their decision process, but can still be used as a basis for group aggregation (Bui/Jarke, 1984; Lewandowski et al, 1986). The general feedback-oriented framework is clearly applicable to those techniques, too, but specific models for its implementation remain to be developed. These issues will be at the focus of an ongoing research project aimed at developing a practical feedback-oriented group decision support system.

## References

Adelman, Leonard: Real-Time Computer Support for Decision Analysis is a Group Setting: Another Class of Decision Support Systems. Interfaces 14 (1984) 75–83.

Bui, Tung; Jarke, Matthias: A DSS For Cooperative Multiple Criteria Group Decision Making. Proceedings, Fifth International Conference on Information Systems, Tucson, Arizona, 1984.

Bui, Tung X.; Jarke, Matthias: Communications Design for Co-oP: A Group Decision Support System. ACM Transactions on Office Information Systems 4 (1986) 81–103.

Castore, Carl H.; Murnighan, J. Keith: Determinants of Support for Group Decisions. Organizational Behavior and Human Performance 22 (1978) 75–92.

DeSanctis, Gerardine; Gallupe, R. Brent: A Foundation for the Study of Group Decision Support Systems. Management Science 33 (1987) 589–609.

Dyer, James S.; Sarin, Rakesh K.: Group Preference Aggregation Rules Based on Strength of Preference. Management Science 25 (1979) 822–832.

Eilon, Samuel; Cosmetatos, G.P.: Models for collective decision making in industry. EJOR 4 (1980) 374–379.

Furtado, Anthony L.; Casanova, Marco A.: Updating Relational Views. In: Won Kim; David S. Reiner; Don S. Batory (Eds.): Query Processing in Database Systems. (Springer, Berlin 1985) 127–142.

Huber, George P.: Methods for Quantifying Subjective Probabilities and Multi-Attribute Utilities. Decision Sciences 5 (1974) 430–458.

Huber, George P.: Issues in the Design of Group Decision Support Systems. MIS Quarterly, Sept. (1984) 195–204.

Hurrion, Robert D.: Implementation of a visual interactive consensus decision support system. EJOR 20 (1985) 138–144.

Jarke, Matthias: Knowledge Sharing and Negotiation Support in Multiperson Decision Support Systems. Decision Support Systems 2 (1986) 93–102.

Jarke, Matthias; Jelassi, M. Tawfik; Shakun, Melvin F.: MEDIATOR: Towards a Negotiation Support System. EJOR 31 (1987) 314–334.

Keeney, Ralph L.; Raiffa, Howard: Decisions with Multiple Objectives: Preferences and Value Tradeoffs. (J. Wiley & Sons, New York et al. 1976).

Klein, Gary W.; Moskowitz, H.; Mahesh, S.; Ravindran A.: Assessment of Multiattribute Measurable Value and Utility Functions via Mathematical Programming. Decision Sciences 16 (1985) 309–324.

Kull, D.: Group Decisions: Can a Computer help? Computer Decisions 14 (1982) 64–70.

Laux, Helmut; Liermann, Felix: Grundlagen der Organisation. Springer, Berlin 1987.

Lewandowski, Andrzej; Johnson, Sarah; Wierzbicki, Andrzej: A Prototype Selection Committee Decision Analysis and Support System. SCIDAS: Theoretical Background and Computer Implementation. IIASA Working Paper WP-86-27.

Nunamaker, J.F.; Vogel, Douglas R.: Negotiations Support Systems Software and Facilities for Public Sector Issues. Paper presented at the 31st Annual meeting of the Society for General Systems Research, Budapest, 1987.

Pruitt, Dean G.: Choice Shifts in Group Discussions: An Introductory Review. Journal of Personality and Social Psychology 30 (1971) 339–360.

Roy, Bernard; Vincke, Philippe: Multicriteria analysis: survey and promising directions. EJOR 8 (1981) 207–218.

Schoemaker, Paul J.H.; Waid, Carter C.: An Experimental Comparison of Different Approaches to Determining Weights in Additive Utility Models. Management Science 28 (1982) 182–196.

Steeb, R.; Johnston, S.C.: A Computer Based Interactive System for Group Decision Making. IEEE Transactions Systems, Man Cybernetics 11 (1981) 544–552.

Stohr, Edward A.: DSS for Cooperative Decision Making. Working Paper CRIS 19, Center for Research on Information Systems, New York University 1981.

Vetschera, Rudolf: Unterstützung von Gruppenentscheidungen durch minimale Präferenzmodifikationen. In: Schellhaas, H. et al. (Eds.): Operations Research Proceedings 1987, (Springer, Berlin 1988) 217–224.

Weber, Martin: Decision making with incomplete information. EJOR 28 (1987) 44–57.

Wierzbicki, A.P.: A mathematical basis for satisficing decision making. IIASA Working Paper WP-80-90.
