---
otero_id: 17084
otero_key: "NGMRVCFW"
title: "SCDAS — Decision support system for group decision making: Decision theoretic framework"
authors: "Andrzej Lewandowski"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90019-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# SCDAS – Decision Support System for Group Decision Making: Decision Theoretic Framework

Andrzej LEWANDOWSKI

International Institute for Applied Systems Analysis, A-2361
Laxenburg, Austria

This paper presents the methodological framework for the Group Decision Support System named SCDAS. The system supports a group of decision makers working together on selecting the best alternative from a given, finite set of alternatives. The framework utilizes aspiration-led and quasisatisficing paradigms for eliciting user's preference, and the achievement function for ranking alternatives. Possible implementation of the system within the framework of a computerized teleconferencing system is discussed. Also, previous experience in applying the SCDAS system is presented.

Keywords: Group Decision Making; Aspirations; Teleconferencing; Alternative Selection; Alternatives Ranking; Achievement Function; Quasisatisficing.

![](/api/attachments/NGMRVCFW/fulltext/images/a21476cd06fedf53befa9f2ad512e83c73e738433ee4f2c0fc02e1e02c329328.jpg)

Andrzej Lewandowski received M.Sc (1970) from Warsaw University of Technology, Poland and Ph.D in control engineering from the same university. Since 1973 Research Assistant and since 1974 Assistant Professor in the Institute of Automatic Control, Warsaw University of Technology. In 1985 joined the System and Decision Sciences Program of the International Institute for Applied Systems Analysis where he is leading the Methodology of Decision Analysis Project. Current

scientific interests include Group Decision Support System, Computer Mediated Collaborative Work and object-oriented programming.

## 1. Introduction

While there is an increasing interest in Group Decision Support Systems (GDSS), there is no consensus regarding the definition of GDSS, the possible decision-making environments, the functions of GDSS or methods of design and implementation etc. Most of publications are devoted to the analysis of basic concepts and principles – for example the recent review by Kraemer and King (1988) and the paper by DeSanctis and Galuppe (1987). Much less discussion is devoted to the practical implementations and applications of GDSS. The most known and well documented implementations are to Co-oP system by Bui (1986, 1988) and the MEDIATOR system by Jarke (Jarke et al., 1987). Gray (1986) presents a brief review of several practical implementations of GDSS. There are several other GDSS described in the literature but there is not much information available regarding their design principles, details of implementation and applications.

Several aspects of the problem must be taken into account when designing the GDSS. The most important is the definition of decision environment. The possible taxonomies of GDSS have been studied extensively by Bui and Jarke (Bui, 1986, Jarke, 1986a) and Jelassi (1987). They proposed four attributes to characterize the decision environment:

Spatial distance. This attribute relates to the organization of the decision making process with respect to the participants physical location. Especially, it tells whether full face-to-face communication between the participants can take place, and whether such a way of communication can be supported by the features offered by the Decision Support System.

Temporal distance. This attribute relates to the time synchronization of the decision process - whether decision makers are submitting their responses at the same time during the meeting, or at different points in time.

Commonalty of goals. This attribute describes the decision making environment – whether the group wants to solve the problem cooperatively, or are there contradictory interests and the whole decision process is more oriented to conflict resolution and bargaining.

Structure of the process. This factor distinguishes the situation where all group members share equal rights and the decision making procedure is supervised by the system, as opposed to one of the committee members having special rights and being considered the Committee President or the Mediator.

Several other taxonomies have been proposed, but most of them coincide with the above. For each possible combination of factors a different methodological approach for GDSS must be developed.

The second important aspect of GDSS methodology is the procedural and decision theoretic framework. Decision making in a group is a complex process requiring analysis of various types of information - both qualitative and quantitative. The quantitative information processing requires formal tools, theories and methodological frameworks. To design this aspect of the process it is necessary to make consistent assumptions regarding the process of decision making and the behavior of individuals participating in the decision group. Several theories exist which can support group decision making (see Arrow and Raynaud, 1986, Schwartz, 1986). Known paradoxes occur in these theories which leave the problem of group decision making far from a complete solution (Campbell and Sowden, 1985). It is necessary to point out that systems presented in the literature are either lacking this decision theoretical framework or this framework is formulated in non-sufficiently consistent and explicit form. Some systems provide a collection of various methodologies and procedures allowing the user to select one which could serve the best to solve a problem (Bui, 1988). This approach assumes a high level of expertise of the user and may lead to difficulties and inconsistencies due to aggregating results obtained by utilizing different theoretical principles and methodological assumptions. The MEDIA-

TOR system uses the utility framework - a theoretical tool which applicability for decision support has been questioned, especially in the context of group decision making (Fisher, 1979). Some other software systems belonging to the category of GDSS, like COLAB (Stefik at all, 1987) have been designed without decision theoretic background and constitute only the environment for the exchange of "soft" information.

The final aspect relates to the organization of information exchange. The idea that the discussion between committee members is one of the most important parts of the decision process. This has been already mentioned in several papers has been pointed out by many researchers. It was stated by DeSanctis and Gallupe (1987):

“...A group decision occurs as the result of interpersonal communication – the exchange of information among members... The communication activities exhibited in a decision-related meeting include proposal exploitation, opinion exploitation, analysis, expression of preference, argumentation, socializing, information seeking, information giving, proposal development and proposal negotiations... In this sense the goal of GDSS (Group Decision Support Systems) is to alter the communication process within groups...”

Huber (1984) also expresses the importance of qualitative support for decision making:

“...Information sharing is the most typical of the activities in which groups engage... general GDSS can also enable groups to elicit, share, modify and use professional judgments and opinions in at least as many ways as they do hard data...”

As it was mentioned previously, most existing GDSS is oriented towards processing numeric information. The user of GDSS can enter numerical information into the system, retrieve this information, share it with other users and perform complicated numerical procedures in order to extract important conclusions from this data. However, other types of information are also important for supporting decision processes. As it has been pointed out by Huber (1984):

“...Today's DSS are largely concerned with the retrieval and use of numeric information.

In contrast, the environment of most meetings in corporation and public agencies is highly verbal. Thoughts are primarily shared and modified, not numbers. To the extent that the thoughts need to be recorded, they are put into text form... Meetings are extremely verbal environments, and the most important thoughts with which they deal are put into text form. A GDSS that does not reflect these facts will serve only a fraction of group tasks. For this reason it is important to consider how GDSS can support decision groups by aiding in the sharing of textual information...”

Designers of many existing GDSS, including Mediator and Co-oP do not pay sufficient attention to this aspect of decision making. They provide mostly tools for number processing, exchanging numerical information between group members, and tools for information exchange based on the unstructured electronic mail concept (Bui, 1988). In most practical situations this type of support can not be sufficient. This relates mostly to situations when decision makers are located in geographically dispersed locations. In this situation GDSS should support not only numerical analysis but also various types of information exchange.

The goal of this paper is to provide a consistent decision theoretic framework for GDSS named Selection Committee Decision Analysis and Support (SCDAS). This system has been designed for supporting decision problems, where the group of experts (the committee) cooperates to select the best alternative (or to reduce the set of alternatives to some reasonable subset which can be considered for further analysis). These alternatives are presented to them by independently acting experts. According to the mentioned above taxonomy the most important attributes of the SCDAS process are commonalty of goals and structure of the process. It is assumed that the decision group has common goals and has to work cooperatively to develop a common solution. The decision process is supervised by the Committee President who specifies and controls all procedural details. Two other attributes are mostly implementation dependent since the SCDAS procedure can be used for a Decision Room environment as well as in a distributed computing environment.

In this paper we will concentrate only on the decision theoretic and procedural aspects of SCDAS framework. The other important issues regarding information processing framework and implementation technology are discussed in separate papers (Lewandowski, 1988a, b).

## 2. The Quasisatisficing Decision Framework

To develop the framework for Decision Support Systems it is necessary to specify the concept of rational decision. This is beyond the scope of this paper to discuss all possible aspects of rationality. Detailed discussion of the problem can be found in the paper by Lewandowski and Wierzbicki (1988a).

There exist several frameworks for analytical rationality. We can represent them best when assuming a certain mathematical structure of the decision situation. Such a structure consists of:

\- a space of decisions (alternatives, options, controls, designs etc.) denoted by $E_x$ ; if this space is a discrete set, we speak about discrete alternatives,

\- a constraint set of admissible decisions $X \subseteq E_x$ ,

\- a space of outcomes (attributes, objective outcomes, objectives, performance indices, etc.) denoted by $E_{v}$ ,

\- an outcome mapping $f: E_x \to E_y$ , which also defines the set of attainable outcomes $Y_0 = f(X_0) \subset E_y$ ; this mapping might be given explicitly by a substantive model of the decision situation or be supplied judgmentally by experts evaluating alternatives along various attributes, in which case we have judgmental model evaluation.

\- a partial preordering in the space of outcomes that is usually implied by the decision problem and usually has some obvious interpretation, such as maximization of profit competing with the maximization of market share, etc. A standard assumption is that this preordering is transitive and can be expressed by a positive cone $D \subset E_y$ .

\- a complete preordering in the space of outcomes or, at least, in the set of attainable outcomes, which is usually not given in any precise mathematical form, but is contained in the mind of the decision maker, such as how actually the preferences between the maximization of profit and the maximization of market share should be distributed in the above example.

The main differences between various frameworks of rationality that lead to diverse approaches to interactive decision support are concerned with the assumptions about this complete preordering and the way of its utilization in the DSS. This issue is also closely related with the way in which the DSS interacts with the decision maker. Some variants of DSS require that the user answers enough questions for an adequate estimation of this complete preordering, some other variants need only general assumptions about the preordering, still other variants admit a broad interpretation of this preordering and diverse frameworks of rationality that might be followed by the user.

The most strongly established rationality framework is based on the assumption of maximization of a value function or an utility function. Under rather general assumptions, the complete preordering that represents the preferences of the decision maker can be represented by an utility function $u: E_{y} \rightarrow R^{1}$ such that by maximizing this function over $x \in X_{0}$ we can select the decision which is most preferable to the decision maker. The publications related to this framework are numerous, for example, the book by Keeney and Raiffa (1976).

There are many fundamental and technical difficulties related to the identification of such utility function. Leaving aside various technical difficulties, we should stress the fundamental ones.

Firstly, a continuous utility function only exists if there is no strict hierarchy of values between decision outcomes, that is if all decision outcomes can be aggregated into one value. This does not mean that hierarchical dependence between outcomes cannot be incorporated in this framework, but such dependencies must be treated as constraints and cannot be evaluated in the decision process. Moreover, the utility maximization framework represents the culture of an entrepreneur facing an infinite market which, although it represents the behavior of many human decision makers, is by no means the universal case of human rationality (Rapoport, 1984). Rapoport states the following:

“...The difficulty is that in many instances a utility function satisfying certain apparently innocuous considering criteria cannot be established to begin with. The investigator who is interested not in actor's utility function per se but rather in his decision behavior is left by no choice but to by-pass the utility problem altogether and work with actual pay-offs used in the experiments, for instance, money...”

Secondly, while the utility maximization framework might be a good predictor of mass economic phenomena, it has many drawbacks as a predictor of individual behavior—see, e.g. Fisher (1979), Erlandson (1981). According to the results of research presented in these papers, the utility function approach can be used in a rather simple, laboratory environment, but can fail in more complex situations.

Thirdly – and most importantly for applications in decision support systems – an experimental identification and estimation of an utility function requires many questions and answers in the interaction with the decision maker (e.g. Keeney and Sicherman, 1975). Users of decision support systems are typically not prepared to answer that many questions, for several reasons. They do not like to waste time and they do not like to disclose their preferences in too much detail. This is because they intuitively perceive that the decision system should support them in learning about the decision situation and thus they should preserve the right to change their minds and preferences. Therefore, if any approximation of an utility function is used in a decision support system, it should be non-stationary in time in order to account for the learning and adaptive nature of a decision making process. Such an approximation cannot be very detailed, it must have a reasonably simple form characterized by some adaptive parameters that can aggregate the effects of learning.

Another rationality framework, called satisficing decision making, was formulated by Simon (1969) and further extended by many researchers (Erlandson, 1981). Originally, this approach assumes that human decision makers do not optimize because of the difficulty of optimization operations, uncertainty of typical decision environment, and complexity of the decision situations in large organizations. Therefore, this approach was sometimes termed bounded rationality. The recent article by March (1986) gives a very detailed analysis of this concept as well as other possible views of rationality.

A very important contribution of the satisficing framework is the observation that decision makers often use aspiration levels for various outcomes of decisions (see Tietz, 1983). In the classical interpretation of the satisficing framework, these aspiration levels indicate when to stop optimizing. While more modern interpretations might prefer other rules for stopping optimization, the concept of aspiration levels is extremely useful for aggregating the results of learning by the decision maker:

aspiration levels represent values of decision outcomes that can be accepted as reasonable or satisfactory by the decision maker and thus are aggregated, adaptable parameters that are sufficient for a simple representation of his accumulated experience.

In order to develop a broader framework that would be useful for decision support for decision makers representing various perspectives of rationality, Wierzbicki (1982, 1984, 1986) proposed the following principles of quasisatisficing decision making.

A quasisatisficing decision situation consists of

\- one or several decision makers or users that might represent any perspective of rationality and have the right of changing their minds due to learning. They have also the right of stopping optimization for any reason,

\- a decision support system that might be either fully computerized or include also human experts, analysts or advisors.

## It is assumed that:

\- The user evaluates possible decisions on the basis of a vector of attributes or objective outcomes. These factors can be expressed in numerical scale (quantitatively) or in verbal scale (qualitatively), like bad, good or excellent. Each factor can be additionally constrained by specifying special requirements on it that must be satisfied. Beside this, objective outcomes can be characterized by their type: maximized, minimized, stabilized – that is, kept close to a given level (which corresponds to foregoing optimization), or floating – that is, included for the purpose of additional information or for specifying constraints. The user has the control over the specification of objective outcomes together with their types and the possible aggregation of such factors.

\- One of the basic means of communication of the user with the decision support system is his specification of aspiration levels for each objective outcome; these aspiration levels are interpreted as reasonable values of objective outcomes. In more complex situations, the user can specify two levels for each objective outcome – an aspiration level interpreted as above and a reservation level interpreted as the lowest acceptable level for the given objective outcome.

\- Given the information specified by the user the decision support system following the quasi-satisficing principle should use this information, together with other information contained in the system, in order to propose to the user one or several alternative decisions that are best attuned to this guiding information. When preparing (generating or selecting) such alternative decisions, the decision support system should not impose on the user the optimizing or the satisficing or any other behavior, but should follow the behavior that is indicated by the types of objective outcomes. This means that the decision support system should optimize when at least one objective outcome is specified as minimized or maximized and should suffice (stop optimizing upon reaching aspiration levels) when all objective outcomes are specified as stabilized.

In order to illustrate possible responses of a quasisatisficing decision support system to the information given by the user, let us assume that all specified objective outcomes are supposed to be maximized and have specified aspiration levels. We can then distinguish the following cases:

Case 1: the user has overestimated the possibilities implied by admissible decisions and there is no admissible decision such that the values of all objective outcomes are exactly equal to their aspiration levels. In this case, however, it is possible to propose a decision for which the values of objective outcomes are as close as possible to their aspiration levels. The decision support system should tentatively propose one decision or several such decisions to the user.

Case 2: the user underestimated the possibilities implied by admissible decisions and there exist a decision which results in the values of objective outcomes exactly equal to the specified aspiration levels. In this case, it is possible to propose a decision which improves all objective outcomes uniformly as much as possible. The decision support system should inform the user about this case and tentatively propose one decision or several such decisions.

Case 3: the user, by chance or as a result of a learning process, has specified aspiration levels that are uniquely attainable by an admissible decision. The decision support system should inform the user about this case and specify the details of the decision that result in the attainment of aspiration levels.

In the process of quasisatisficing decision support, all aspiration levels and the corresponding decisions proposed by the system have tentative character. If a decision proposed by the system is not satisfactory to the user, he can modify the aspiration levels and obtain new proposed decisions, or even modify the specification of objective outcomes or constraints. The process is repeated until the user learns enough to make the actual decision himself or to accept a decision proposed by the system.

The process of quasisatisficing decision making can be formalized mathematically (Wierzbicki, 1986, Lewandowski and Wierzbicki, 1988a) and the mathematical formalization can be interpreted in various ways. Let us consider an interpretation that corresponds to the framework of utility maximization. We assume that the user has a nonstationary utility function that changes in time due to his learning about a given decision situation. At each time instant, however, he can intuitively and tentatively (possibly with errors concerning various aspects of the decision situation) maximize his utility. This tentative maximization determine his aspiration levels, denoted here by $w \in E_{y}$ .

When the decision maker communicates the aspiration levels w to the decision support system, the system should use this information, together with the specification of the decision situation, in order to construct an approximation of his utility function that is relatively simple and easily adaptable to the changes of aspiration levels, treated as parameters of this approximation. By maximizing such an approximate utility function while using more precise information about the attainability of alternative decisions and other aspects of the decision situation – for example, expressed by the substantive model of the decision situation incorporated by expert advice into the decision support system – a tentative decision can be proposed to the user.

Such a tentative approximation of the user's utility function, constructed in the decision support system only in order to propose a tentative decision to the learning decision maker, is called here order-consistent achievement function or simply achievement function and has the form $u(y) = s(y, w)$ . By an order consistent achievement function we understand here either an order representing or an order approximating achievement function, according to the following definitions:

An order representing achievement function is a continuous function $s: Y_{0} \times E_{y} \to R^{1}$ , with arguments $y \in Y_{0}$ and $w \in E_{y}$ interpreted as an attainable objective outcome vector and an aspiration level vector that satisfies the following requirements:

\- It is strictly order preserving (monotone) with respect to $y$ and the positive cone $D$ implied by the partial preordering (according to the types of objective outcomes) specified by the decision maker, that is, for all $w \in E_y$ :

$$
y _ {2} - y _ {1} \in \operatorname{int} D \Rightarrow s (y _ {1}, w) <   s (y _ {2}, w).\tag{1}
$$

\- It is order representing with respect to $y$ and the positive cone $D$ , that is, for all $w \in E_y$ :

$$
\left\{y \in E _ {y}: s (y, w) \geq 0 \right\} = w + D.\tag{2}
$$

If $E_{y}=R^{m}$ and all objective outcomes are maximized, $D=R_{+}^{m}$ , then a simple example of an order representing achievement function is:

$$
s (y, w) = \min _ {1 \leq i \leq m} \frac {y _ {i} - w _ {i}}{a _ {i}},\tag{3}
$$

where $a_{i}$ represent some scaling units for subsequent objectives. Because of these scaling units, this function has a cardinal form i.e. does not depend on positive affine transformations of the space of outcomes together with scaling units.

An order-approximating achievement function is a continuous function $s: Y_{0} \times E_{y} \to R^{1}$ , with arguments $y \in Y_{0}$ and $w \in E_{y}$ interpreted as an attainable objective outcome vector and an aspiration level vector that satisfies the following requirements:

\- It is strongly order preserving (monotone) with respect to $y$ and the positive cone $D$ , that is, for all $w \in E_y$ :

$$
\begin{array}{r l} y _ {2} - y _ {1} & \in D \setminus (D \cap - D) \\ & \Rightarrow s (y _ {1}, w) <   s (y _ {2}, w). \end{array}\tag{4}
$$

\- It is order approximating with respect to $y$ and the positive cone $D$ , that is, for all $w \in E_y$ and for some small $\epsilon > 0$ :

$$
w + D \subset \left\{y \in E _ {y}: s (y, w) \geq 0 \right\} \subseteq w + D _ {\epsilon},\tag{5}
$$

where

$$
D _ {\epsilon} = \left\{y \in E _ {y}: \operatorname{dist} (y, D) <   \epsilon \| y \| \right\}.\tag{6}
$$

If $E_{y}=R^{m}$ and $D=R_{+}^{m}$ , then a simple example of an order approximating achievement function is:

$$
s (y, w) = \max _ {1 \leq i \leq m} \frac {y _ {i} - w _ {i}}{a _ {i}} + \frac {\epsilon}{m} \sum_ {i = 1} ^ {m} \frac {y _ {i} - w _ {i}}{a _ {i}}.\tag{7}
$$

Intuitively speaking, we might say that if $w \in Y_{0} - D$ , then the maximization of $s(y, w)$ over $y \in Y_{0}$ represents a uniform maximization of all components of the surplus $y - w \in D$ ; if $w \notin E_{y} - D$ , then the same maximization represents distance minimization between the sets $w + D$ and

$$
\left\{y \in Y _ {0}: Y _ {0} \cap (y + D \setminus (D \cap - D)) = \emptyset \right\}\tag{8}
$$

which is the set of generalized Pareto optimal objective outcomes in the sense implied by the positive cone D.

Important properties of order consistent achievement functions are summarized by the following theorems (Wierzbicki, 1986):

Theorem 1. If $s(y, w)$ is strongly order preserving then its maximal points in $y \in Y_0$ are generalized Pareto optimal, that is, satisfy the following condition:

$$
\tilde {y} = \underset {y \in Y _ {0}} {\arg \max} s (y, w) \Rightarrow Y _ {0} \cap (\tilde {y} + \tilde {D}) = \emptyset ,\tag{9}
$$

where

$$
\tilde {D} = D \backslash (D \cap - D).\tag{10}
$$

If $s(y, w)$ is strictly order preserving then its maximal points in $y \in Y_0$ are generalized weakly Pareto optimal, that is, satisfy the following condition:

$$
y = \underset {y \in Y _ {0}} {\arg \max} s (y, w) \Rightarrow Y _ {0} \cap (\tilde {y} - \operatorname{int} D) = \emptyset .\tag{11}
$$

Theorem 2. If $s(y, w)$ is order approximating and $w \in Y_0$ is generalized properly Pareto optimal (with trade off coefficients bounded by $\epsilon$ and $1/\epsilon$ ), then the maximum of $s(y, w)$ in $y \in Y_0$ , equal zero, is attained at $y = w$ . If $s(y, w)$ is order representing and $w \in Y_0$ is generalized weakly Pareto optimal, then the maximum of $s(y, w)$ in $y \in Y_0$ , equal zero, is attained at $y = w$ .

Thus, the usefulness of achievement functions in building interactive decision support systems follows from the following properties:

\- maximization of an order approximating achievement function results in Pareto optimality, no matter whether the aspiration level is attainable or not. Order representing functions are less useful, because their maxima are only weakly Pareto optimal,

\- if a decision $\hat{x} \in X_0$ and the corresponding objective outcome $\hat{y} \in Y_0$ maximize an order approximating achievement function and $\hat{s} = s(\hat{y}, w) = 0$ then the aspiration levels $w$ are attainable and Pareto optimal,

\- if, in the above situation, $\hat{s} < 0$ , then the aspiration levels $w$ are not attainable,

\- if, in the above situation, $\hat{s} > 0$ , then the aspiration levels $w$ are attainable, but not Pareto optimal.

Therefore, an order approximating achievement function can be used for computing Pareto optimal decisions as well as for checking for Pareto optimality and attainability of an arbitrarily given $w \in E_{y}$ . Moreover, the value of such achievement function can be meaningfully interpreted – it can be treated as a qualitative distance between a given decision $\hat{x}$ or its objective outcome $\hat{y}$ and the aspiration level w.

Beside the achievement functions specified by equations (3) and (7), there are many other forms of this function (Wierzbicki, 1986). Another example of an order representing achievement function might be

$$
s (y, w) = \max \left\{\rho \max _ {i \leq i \leq m} \frac {y _ {i} - w _ {i}}{a _ {i}}, \frac {1}{m} \sum_ {i = 1} ^ {m} \frac {y _ {i} - w _ {i}}{a _ {i}} \right\}.\tag{12}
$$

The above function is especially useful when applied to decision support systems with substantive models of linear multiobjective optimization type, when its maximization can be reduced by suitable transformation of variables to a single objective linear programming problem with additional constraints (Lewandowski et al., 1985, 1987, Lewandowski and Wierzbicki, 1988c).

Practical experiments with this approach (Lewandowski et al., 1985, Dobrowolski and Zebrowski, 1987) have shown that the language of aspiration levels coincides very well with the style of thinking of practical decision makers. The information which is required from the user is easy to express, as opposed to other approaches based on pairwise comparisons, explicit weighting factors, estimation of other forms of utility functions, etc.

Theoretically, the learning process of interaction with a quasisatisficing decision support system via changing aspiration levels might not be sufficient for all decision makers: some of them might learn sufficiently to selects their preferred decision, some others might still be puzzled and require some help in the convergence to their best preferred decision. There are several ways of organizing such support for the user in changing his aspiration levels that the corresponding maxima of achievement functions converge to the maximum of his utility function. One way consists in the visual interactive approach of Korhonen (1988) and Korhonen and Laakso (1986), or directional scanning of aspirations and the corresponding maxima of achievement functions.

## 3. Alternative Based and Aspiration Led Group Decision Support System

The problem of selecting one alternative from a finite set of alternatives presented to a committee is one of the most basic and classical decision problems and has received much attention in the decision-theoretical literature (e.g. Mirkin, 1979, Schwartz, 1986). There are many variants of this kind of problems. We will consider the following formulation:

A committee consists of several members. Each member can have either equal or different voting power (denoted here by a voting power coefficient $v_{k}$ ), specified a priori by the committee charter. In addition to the committee structure, the committee charter might specify the purpose of the committee's work, procedural details, etc.

The problem faced by the committee is to jointly rank or select one or a few from a set of available decision alternatives. The list of alternatives need not be complete at the beginning of the committee's work. During the decision-making process, new alternatives may be generated and subsequently evaluated.

Evaluation of alternatives is performed by the committee by specifying decision attributes and then assessing each alternative with respect to each of these attributes. The list of decision attributes might be specified in the committee's charter or decided upon by the committee. In any case, decision attributes must be specified before alternatives can be evaluated and compared.

Each alternative must be evaluated by the committee or its individual members. The problem consists of proposing a decision process which together with an assessment of various attributes of alternatives and an aggregation of evaluations across both attributes and committee members, leads to a final ranking or selection of one or several alternatives in a way that is rational, understandable and acceptable to the committee members.

Beside an aspiration level which expresses a reasonable (or satisfactory) value for each attribute, members of the committee can specify a reservation level, which represents a minimum acceptable level for each attribute. If an alternative is evaluated below the reservation level on even one attribute, it is considered unacceptable; if it is evaluated at least equal to aspiration levels for all attributes, it is considered highly desirable. Details of the procedure, theoretical background and principles of implementation were presented by Lewandowski and Wierzbicki (1986, 1987).

## 3.1. Procedural Framework

One of the basic features of the presented method is a structuring of the decision process: it is assumed that the process consists of several well defined stages. According to this procedure, it is possible to advance the decision process forward only if all committee members successfully completed all previous stages. Details of the procedure must be defined during the initial stage of the decision process. Let us consider in detail all stages of this decision making process.

The first stage or point on the agenda is to define the procedures by which the committee will operate. The questions addressed here should include the following:

\- What is the expected product of the committee work and how does it influence the selection of the details of the procedure? The answer to this question depends on the committee's charter and its perceived role.

\- What rules for aggregating opinions across the committee should be adopted, in particular, should outlying opinions be included in or excluded from aggregation?

\- Should the committee be allowed to divide and form coalitions that might present separate assessments of aspirations, attribute scores and thus final rankings of alternatives?

The second objective of the first stage is problem specification. Neither the list of alternatives, nor their descriptions need be complete at this stage; moreover, this information might not be known to the committee members at this stage, if they wish to avoid the bias in specifying attributes and their aspiration levels. The important issue at this stage that requires discussion and specification by the entire committee is the definition of the attributes of the decision and their scales of assessment.

The second stage of the decision process is devoted to specification and discussion of aspirations. Aspiration and/or reservation levels for all attributes are determined separately by each committee member. After these values are entered into the decision support system, all necessary indicators (disagreement indicators, dominant weighting factors) can be computed.

The third stage has again two objectives. One is the analysis and discussion of aspirations by the entire committee. These discussions are supported by the computed indicators and their graphic interpretations. In these discussions, the committee might address the following questions:

\- Do the computed indicators accurately reflect the perceptions of individual committee members about the relative importance of various attributes?

\- What are the relevant differences of opinions between committee members and do they represent an essential disagreement about decision principles?

\- Does the entire committee agree to use joint, aggregated aspirations (reservations), or will there be several separate sub-group aggregations?

The second objective of the third stage is a survey of alternatives. Discussions might center on the following issues:

\- Are the available descriptions of alternatives adequate for judging them according to the accepted list of attributes? If the answer is negative, additional information should be gathered by sending out questionnaires, consulting experts etc.

\- Which of the available alternatives are irrelevant and should be deleted from the list? Such preliminary screening can be done in various ways. The committee might define some screening attributes and reservation levels for them: for example, we do not accept investments which are more expensive than a given limit.

The fourth stage of the decision process is the individual assessment of alternatives. The evaluation of each attribute for each alternative is the main input of committee members into the system. Each member specifies evaluation scores; the decision support system helps him by displaying the evaluations already made and those still to be entered.

When all evaluations are entered, a committee member should proceed to the individual analysis of alternatives, based on calculations of an achievement function that leads to a ranking of all alternatives for the given committee member. This ranking is the main source of learning about the distribution of alternatives relative to aspirations.

The questions addressed by each member at this point might be as follows:

\- Do the rankings along each attribute correctly represent the individual's evaluations of alternatives; does the achievement ranking, based on individual aspirations, correctly represent the aggregate evaluation (if not, should the scores be modified)?

\- If the committee member agrees with the individual achievement ranking proposed by the system, what are the differences between this ranking and that based on individual scores but related to committee aggregated aspirations? Are these differences significant, or can he accept them as the result of agreement on joint decision principles?

The fifth stage of the decision process relates to an aggregation of evaluations and rankings across the committee and consists of a discussion of essential differences in evaluations, followed by a discussion of disagreements about a preliminary ranking of alternatives aggregated across the committee. These discussions are supported by the system; the system computes indicators of differences of opinion and prepares a preliminary aggregated ranking.

The questions addressed by the committee at this point might be following:

\- Which attributes and alternatives show the largest differences in evaluations between committee members? Do these disagreements represent essential differences in information about the same alternative?

\- What is the essential information (or uncertainty about such information) that causes such disagreements? Should additional information be gathered, or can certain committee members supply this information?

\- Would the results of these discussions and possible changes of evaluations influence the preliminary aggregated ranking list proposed by the system? This can be tested by applying simple sensitivity analysis tools.

\- Does the preliminary ranking proposed by the system correctly represent prevalent committee preferences?

After these discussions, a return to any previous stage of the process is possible. If the committee decides that the decision problem has been sufficiently clarified, it can conclude the fifth stage by the final agreement on the aggregated ranking or selection of one or more alternatives. It is important to stress again that the committee need not stick to the ranking proposed by the system, since the purpose of this ranking – as well as of all information presented by the decision support system – is to clarify the decision situation rather than to prescribe the action that should be taken by the committee.

## 3.2. Formalization of the Procedural Framework

In the previous section we presented the general structure of the decision process. The decision support system supervises the progress of discussion within the committee – its role is to process all the information necessary to perform the discussion, compute all necessary informative indicators, display graphic information and ensure proper structuralization of the process. In the sequel, we will consider in more detail the functions of the decision support system during each stage of the decision process.

## 3.2.1. Setting and Discussing Aspirations

Most judgmental decision processes require a choice of scales of evaluation for each decision attribute. The scales are often qualitative but can be transformed into quantitative scales for computational purposes. When asked to specify aspiration and reservation levels on these scales at an early stage of the decision process, the decision maker is better prepared to make consistent evaluations across alternatives. However, we cannot expect and we should not require full consistency in any judgmental decision process, since not all relevant attributes might be evaluated and the relevant information about alternatives is never completely shared by all committee members. If each committee member is asked independently to specify his aspiration and (or) reservation levels for each attribute, a comparison of such results across the committee and across attributes serves several purposes:

\- the relative importance of each attribute for each committee member and across the committee, as implied by the more or less attainable levels of aspirations, becomes more apparent, as discussion below.

\- the division of opinions among the committee members can be discussed. If a significant subset of the committee has high aspirations (reservations) for an attribute and another subset has low aspirations (reservations), it is a case of a clear disagreement on decision principles. The committee might then discuss this disagreement and come to a consensus; or agree to disagree by allowing the formation of coalitions that rally for the importance of various attributes (for example, when deciding on siting an industrial facility, a part of the committee might be more concerned with environmental impacts, another more concerned with economic impacts).

\- if the discussion shows that the reason for disagreement stems from different perceptions by various committee members about the exact meaning of a particular attribute and its scale of evaluation, the result might be a better specification of the list of attributes.

\- if the committee (or a coalition inside the committee) agrees to use averaged aspiration and (or) reservation levels, each committee member has a better perception of the anchor points to be used when evaluating alternatives.

In order to support these discussions, a number of indicators can be computed. Denote the individually specified aspiration levels for attribute j by the committee member k by $p_{jk}$ and the corresponding reservation levels by $r_{jk}$ . Then the committee “voting” procedure might specify an averaging of individual inputs, weighted by the voting power coefficients $v_{k}$ as follows:

$$
p _ {j} = \frac {\sum_ {k = 1} ^ {K} v _ {k} p _ {j k}}{\sum_ {k = 1} ^ {K} v _ {k}},\tag{13}
$$

$$
r _ {j} = \frac {\sum_ {k = 1} ^ {K} v _ {k} r _ {j k}}{\sum_ {k = 1} ^ {K} v _ {k}}.\tag{14}
$$

Such an average is subject to manipulations by committee members who have an incentive to distort their true aspirations in order to influence the entire committee. A classical remedy, successfully used in subjective evaluations is to exclude outlying opinions, in this case deleting the highest and the lowest $p_{jk}$ or $r_{jk}$ across all k before aggregating. This procedural option motivates committee members to state their preferences carefully since they will have no impact if they voice the outlying opinions. If the committee adopts this option (or if it is imposed by the committee charter), then an aggregation of opinions can be characterized by

$$
p _ {j} = \frac {\sum_ {k \neq \overline {{k}} _ {p j} , \underline {{k}} _ {p j}} v _ {k} p _ {j k}}{\sum_ {k \neq \overline {{k}} _ {p j} , \underline {{k}} _ {p j}} v _ {k}}, \quad \text { where }\tag{15}
$$

$$
\bar {k} _ {p j} = \arg \min _ {1 \leq k \leq K} p _ {j k}; \quad \underline {{k}} _ {p j} = \arg \max _ {1 \leq k \leq K} p _ {j k}\tag{16}
$$

denote the committee members with outlying aspiration levels who are therefore excluded from the averaging. The calculations are similar for aggregation of reservation levels $r_{j}$ with corresponding $\overline{k}_{r_{j}}$ and $\underline{k}_{r_{j}}$ . Evidently, computing the average is not the only one possible approach to aggregating individual aspirations. Another approach was suggested by Mirkin (1979) who proposed computing the median as a good aggregation principle. The basic advantage of median is its robustness – the median is naturally insensitive on data outliers.

## 3.2.2. Assessing Disagreement

The disagreement about aspiration (reservation) levels for an attribute among the committee can be measured in various ways. Clustering algorithms can be used in the case of very large numbers of committee members to identify the positional structure of the committee. Or, one could evaluate various statistical moments of the distributions of $p_{jk}$ and $r_{jk}$ across k, although moments of a distribution do not typically indicate the configuration of dissent or shape of the distribution of opinions within a group. A good indicator of disagreement should distinguish between the case when there are two or more sizeable dissenting groups of committee members, each representing a uniform opinion, and the case when the differences of opinion are distributed uniformly or attributed mainly to outlying opinions. To identify these differences, a disagreement indicator can be heuristically defined in the following way.

First let us consider the absolute change of aspirations

$$
\Delta P _ {j K} = p _ {j 1} - p _ {j K},\tag{17}
$$

where committee members are renumbered such that

$$
p _ {j 1} \geq p _ {j 2} \geq \dots p _ {j (K - 1)} \geq p _ {j K}.\tag{18}
$$

Now $\Delta P_{jk}$ can be split into the distribution of individual changes of opinion:

$$
\Delta p _ {j k} = p _ {j k} - p _ {j (k - 1)}, \quad k = 2, \dots , K - 1.\tag{19}
$$

In these equations, k can be interpreted as the index of the pairwise comparison between two ranked committee members. If large differences occur only at the ends of the range of k, corresponding to outlying opinions or small minority groups, they are not as significant as when they occur in the middle of the range. To correct for this, we introduce a coefficient $c_{k}$ – for example, in the form

$$
c _ {k} = \frac {1 6 (k - 1) ^ {2} (K - 1 - k) ^ {2}}{(K - 2) ^ {4}}.\tag{20}
$$

Other formulae can also be used for this coefficient; the above has been selected after empirical tests. The maximum value of $c_{k}$ for any $(K, k)$ is one. Also, for all K, $c_{k}=0$ for both k=1 and k=K-1 since outlying opinions are not counted in the aggregation. It is useful to define the disagreement indicator as

$$
D I (p, j) = \sum_ {k = 2} ^ {K - 2} c _ {k} \Delta p _ {j k}.\tag{21}
$$

This disagreement indicator is bounded by the absolute difference of aspirations, $\Delta P_{jK}$ ; but $DI(p, j) = \Delta P_{jK}$ only if the committee is split into two equal fractions of equal aspirations in each fraction. Note that the disagreement indicator (21) has a peculiar property: it is always equal to zero if $K \leq 3$ . Clearly this is because a committee of three always has two outlying opinions and only one will therefore be counted in the aggregation.

Similarly, disagreement indicators $DI(r, j)$ for the distribution of reservation levels $\Delta r_{jk}$ can be computed. If both aspiration and reservation levels are used, the committee might be interested in disagreement indicators for averages, $DI(pr, j)$ , computed for the distribution of $pr_{jk}$ , defined as

$$
\Delta p r _ {j k} = \frac {\Delta p _ {j k} + \Delta r _ {j k}}{2}.\tag{22}
$$

It should be stressed that the above indicators serve only to draw the attention of the committee to the attributes and aspirations that cause dissent, for which a discussion of differences of opinion might be useful. Similar disagreement indicators can be used when comparing the differences between individual assessments of specific alternatives.

Another type of indicator relates to the relative importance of various attributes as implied by specified aspirations (reservations). Various types of indicators can also be used here. We choose dominant weighting factors implied by aspirations as relevant indicators because they are consistent with the function used later for the evaluation of alternatives.

To be consistent with our theoretical decision model, the weighting factors for attributes are constructed as follows: If a committee member specifies aspirations for one attribute that are “closer” to the upper end of its evaluation scale than for another attribute, then this implies that the former attribute is more important to him than the latter one. More specifically, an indicator should be inversely proportional to such a distance and, if the indicators are interpreted as weighting coefficients, they should be normalized so that they sum up to one across all attributes. To avoid computational errors, the indicators should be calculable even in such an unreasonable case that a committee member specifies aspirations equal to the upper end of the scale. Hence, we extend the upper bound slightly, denoting it by $ub_{j}$ , and for simplicity normalize all scales so that the lower bounds of the scales of all attributes are zero. Then the dominant weighting factors implied by aspiration levels p of attributes j for committee member k are computed as follows:

$$
w _ {p j k} = \left\{\frac {u b _ {\bar {j}}}{u b _ {\bar {j}} - p _ {j k}} \right\} / \left\{\sum_ {j = 1} ^ {J} \frac {u b _ {\bar {j}}}{u b _ {\bar {j}} - p _ {j k}} \right\}.\tag{23}
$$

Weighting factors implied by stated reservation levels $w_{rjk}$ are calculated similarly.

These weighting factors can also be calculated for the preferences aggregated across the committee. In all cases, the indicators serve only as feedback signals to individuals or to the committee to check whether their aspirations correctly reflect their perception of the relative importance of various attributes. Any observed inconsistencies can be easily corrected.

## 3.2.3. Evaluating Alternatives by Individual Committee Members

An essential part of the decision process is an individual assessment and analysis of all alternatives by each committee member. In the approach followed in this paper, it is assumed that the assessment is performed not by rankings or pairwise comparisons but simply by assigning evaluation scores for each attribute to each alternative. Uncertainty in each assessment could be expressed by supplying a range of scores or a probability distribution for the scores; however, we consider here only the simpler case without individual uncertainty of evaluations. The scores of the kth committee member for the jth attribute of the ith alternative are denoted here by $q_{ijk}$ .

In order for each committee member to see what the scores imply and check for any scoring errors, rankings of alternatives by various attributes can be produced in the system by listing the alternatives, starting with the best score on a given attribute and ending with the worst score. However, the committee member is also interested in an aggregate ranking which takes into account scores on all attributes to test whether his intuitive opinion about which alternatives are best is consistent with the results of the scoring procedure.

A special approximation of a utility function implied by aspiration levels is applied in order to produce such an aggregate ranking; this approximation is called an order-consistent achievement function.

Suppose the user knows the upper and lower bounds of an assessment scale and has specified a reservation and an aspiration level for each decision attribute. These four points we denote respectively by $lb_{j}$ , $ub_{j}$ , $r_{j}$ and $p_{j}$ , where

$$
l b _ {j} <   r _ {j} <   p _ {j} <   u b _ {j}.\tag{24}
$$

Let us assume, that a satisfaction value of zero is assigned to an alternative whose attribute assignments are all equal to reservation levels, and a satisfaction value of one to an alternative whose attributes are all equal to aspiration levels. We assume further that alternatives which have scores satisfying all their reservation levels are preferred to any alternative which has at least one score not satisfying the corresponding reservation level. And similarly, alternatives which have scores satisfying all their aspiration levels are preferred to any alternative which has at least one score not satisfying the corresponding aspiration level. Finally, let an alternative with scores all equal to the lower bounds of the scales have the value of -b (a negative number) and an alternative with scores all equal to the upper bounds have the value of $1 + a$ (a number greater than one).

The simplest function that meets the listed above requirements can be constructed by using linear approximations between the points for which its values are known $(-b, 0, 1 \text{ and } 1 + a)$ . Such a function, called also an order-representing achievement function, has the following form (Wierzbicki, 1986):

$$
s \left(q _ {i k}, p, r\right) = \min _ {1 \leq j \leq J} u _ {j} \left(u _ {i j k}, p _ {j}, r _ {j}\right). \text { where }\tag{25}
$$

$$
\begin{array}{l} {u _ {j} (q _ {i j k}, p _ {j}, r _ {j})} \\ {= \left\{ \begin{array}{l l} {b \left(\frac {q _ {i j k} - l b _ {j}}{r _ {j} - l b _ {j}} - 1\right)} & {\mathrm{if} \quad l b _ {j} \leq q _ {i j k} <   r _ {j}} \\ {\frac {q _ {i j k} - r _ {j}}{p _ {j} - r _ {j}}} & {\mathrm{if} \quad r _ {j} \leq q _ {i j k} \leq p _ {j}} \\ {a \frac {q _ {i j k} - p _ {j}}{u b _ {j} - p _ {j}} + 1} & {\mathrm{if} \quad p _ {j} <   q _ {i j k} \leq u b _ {j}} \end{array} \right.} \end{array}\tag{26}
$$

and $q_{ik}=(q_{i1k},\ldots,q_{ijk},\ldots,q_{iJk})$ is the vector of scores given by the kth committee member to the ith alternative. Thus the achievement functions maps a vector of attributes into a scalar value for each alternative. Additionally, $p=(p_{1},\ldots,p_{j},\ldots,p_{J})$ and $r=(r_{1},\ldots,r_{j},\ldots,r_{J})$ are vectors of aspiration and reservation levels aggregated across the committee in a way that is acceptable to all members. In its middle range, the function (25) can also be interpreted as a distance from reservation level scaled by the difference between aspiration and reservation levels for each attribute.

However, the above achievement function has some disadvantages. Suppose the scales of assessments for all attributes are from 0 to 10, and the reservation levels are all 3 while the aspiration levels are all 7. Compare two alternatives: one with all scores equal to 5 so that the value of the achievement function (25) equals 0.5, while the second alternative has scores of 7 for all attributes but one, which has the score 4 so that $s(q, p, r) = 0.25$ . But the second alternative might be considered better: the better achievements on many attributes could compensate for a worse achievement on one attribute. In order to correct for this consideration, a modified form of the function (25), that is an order-approximating achievement function can be proposed:

$$
\begin{array}{l} s (q _ {i k}, p, r) \\ = \min _ {1 \leq j \leq J} \left\{u _ {j} (q _ {i j k}, p _ {j}, r _ {j}) + \frac {\epsilon}{J} \sum_ {j = 1} ^ {J} u _ {j} (q _ {i j k}, p _ {j}, r _ {j}) \right\} \\ / (1 + \epsilon), \end{array}\tag{27}
$$

where $u_{j}(q_{ijk}, p_{j}, r_{j})$ are defined as in equation (25). The parameter $\epsilon$ in this function represents the intensity of correction of the worst (under-) achievement by the average (over-) achievement. In the example considered above, if $\epsilon = 1$ and there are 5 attributes, then the first alternative has a value of the achievement function (25) equal to 0.5 (due to the subdivision by $1 + \epsilon$ in equation (25), this does not depend on $\epsilon$ if all $u_{j}$ are equal) but the second alternative has the corresponding value of 0.55. Hence the second alternative is preferred. If, however, $\epsilon = 0.5$ , then the first alternative has an achievement value equal to 0.5 but the second alternative has an achievement value of 0.45, hence the first alternative is now preferred.

The choice of the parameter $\epsilon$ is left to the committee: if its members feel that the worst achievement matters most, they should choose slight correction ( $\epsilon = 0.1$ ); if they feel that the average achievement matters most, they should choose very strong correction ( $\epsilon = 2$ ), indicating that average achievement is twice as important as worst achievement.

The achievement function (25) is used to aggregate scores given by a committee member of various attributes of an alternative and then to rank various alternatives according to their achievement values. This can be done when using either individual aspirations (reservations) of a committee member or aggregated aspirations (reservations). In the former case, the ranking proposed by the system serves as a feedback to the committee member: he should compare it with his intuitive perception of ranking of alternatives. If the ranking does not match his intuitive perception, he should check whether he did not make any errors in scoring; another reason for such mismatch might be his disagreement with the correction coefficient $\epsilon$ adopted by the committee. If the ranking does match his intuitive perception, he should be prepared to accept the fact that the ranking based on aggregated aspirations (reservations) might be different; but the committee member cannot protest if he accepts the right of the committee to impose aggregated decision principles on the collective group.

## 3.2.4. Aggregating Individual Assessments Across the Committee

There are various interpretations of the process of aggregating preferences across a group of decision makers. Typically, the interpretation is related to the concept of fairness (Sen, 1970). However, various paradoxes in decision theory (Saari, 1982) show that there is no absolute meaning in this concept. In this paper, we simply require that the committee specify a set of procedures that is accepted as fair by the group. For example, if the charter of the committee specifies the voting power of each member, the procedurally fair aggregation is to take the weighted average of evaluations. The members with greater voting power are supposedly either more responsible (consider, say, the role of the chairman of the committee), more concerned with the outcome of the decision process, or more knowledgeable in a certain substantive area.

Hence, a final ranking of alternatives for the entire committee can be proposed by the decision support system by computing the (weighted) average achievement values for each alternative:

$$
S _ {i} = \frac {\sum_ {k = 1} ^ {K} v _ {k} s (q _ {i k} , p , r)}{\sum_ {k = 1} ^ {K} v _ {k}}\tag{28}
$$

with $s(q_{ik}, p, r)$ defined as in (25) or (27).

This aggregation procedure gives reliable results under assumptions that committee members do not bias their opinions in order to manipulate the outcome of the decision process. In order to discourage such manipulations, it is advisable to exclude outlying opinions from the averaging process, as was done in (7) for the aggregation of aspiration levels:

$$
S _ {i} = \frac {\sum_ {k \neq \underline {{k}} _ {i} , \overline {{k}} _ {i}} v _ {k} s (q _ {i k} , p , r)}{\sum_ {k \neq \underline {{k}} _ {i} , \overline {{k}} _ {i}} v _ {k}}, \quad \text { where }\tag{29}
$$

$$
\underline {{k}} _ {i} = \arg \min _ {1 \leq k \leq K} s (q _ {i k}, p, r),\tag{30}
$$

$$
\overline {{k}} _ {i} = \arg \max _ {1 \leq k \leq K} s (q _ {i k}, p, r).\tag{31}
$$

The alternative procedure for aggregating individual scores can be based on the interpretation of achievement function. As it has been mentioned is Section 3.2.2, values of achievement function can be meaningfully interpreted as a qualitative distance between alternatives and aspiration level.

On the current stage of decision process all committee members have specified already the values of achievement function

$$
s _ {i k} = s \left(q _ {i k}, p, r\right),\tag{32}
$$

where p and r denote vectors of aspiration and reservation levels aggregated across the committee. Therefore, the ith alternative can be characterized by a vector

$$
s _ {i} = \big (s _ {i 1}, s _ {i 2}, \dots , s _ {i k}, \dots , s _ {i K} \big).\tag{33}
$$

These vectors can be considered as elements of space $R = R^{K}$ with natural ordering introduced by the cone $R_{+}^{K}$ . This ordering is motivated by the fact that the value of the function $s_{i}$ characterizes the overachievement of a given alternative over the committee aspirations, according to the opinion of the kth committee member, which should be maximized. Moreover, knowing the properties of achievement function (25) we can specify the aspiration and reservation levels for the decision problem in the space $R -$ the aspiration level is equal to 1, and reservation level is equal to 0. Therefore, we can apply the achievement function of the same form as defined by equation (27):

$$
w \left(s _ {i}\right) = \min _ {1 \leq k \leq K} \left\{u _ {k} \left(s _ {i k}\right) + \frac {\epsilon}{K} \sum_ {k = 1} ^ {K} u _ {k} \left(s _ {i k}\right) \right\}
$$

$$
/ (1 + \epsilon), \quad \text { where }\tag{34}
$$

$$
u _ {k} \left(s _ {i k}\right) = \left\{ \begin{array}{l l} b \left(\frac {l b _ {k} - s _ {i k}}{l b _ {k}} - 1\right) & \text { if } \quad l b _ {k} \leq s _ {i k} <   0 \\ s _ {i k} & \text { if } \quad 0 \leq s _ {i k} \leq 1 \\ a \frac {s _ {i k} - 1}{u b _ {k} - 1} + 1 & \text { if } \quad 1 <   s _ {i k} \leq u b _ {k}. \end{array} \right.\tag{35}
$$

The same reasoning can be used to interpret the values of function (34): the biggest is the value of this function for a given alternative, the better is this alternative in the sense of overachievement specified by all committee member according to the committee aspiration. The parameter $\epsilon$ has the same interpretation as previously – as the instrument allowing to choose between the importance of overachievement and the compensation.

Values of achievement functions can be used for measuring the final disagreement between rankings computed by the committee an the committee members.

Let i denotes the index of the best alternative according to the committee

$$
\bar {i} = \arg \max _ {1 \leq i \leq I} w (s _ {i})\tag{36}
$$

and $\hat{s}$ denote the corresponding value of achievement function computed for this alternative

$$
\hat {s} = s \left(q _ {i k}, p, r\right).\tag{37}
$$

Let, correspondingly, $\hat{s}_{k}$ denotes the value of achievement function computed for the best alternative according to the kth committee member

$$
\hat {s} _ {k} = \max _ {1 \leq i \leq 1} s (s _ {i k}, p, r).\tag{38}
$$

The value

$$
D _ {k} = \frac {| \hat {s} - \hat {s} _ {k} |}{1 + a + b}\tag{39}
$$

can be interpreted as the disagreement indicator between the individual and committee rankings for the committee member k. Several other disagreement indicators can be introduced utilizing the achievement function values; we will not discuss this problem in detail. Especially interesting is the application of interactive graphic systems which could allow the user to analyse values of achievement function using various views suitable for exploratory analysis of the decision problem.

Discussing the procedural framework, we assumed that committee members possess the same information about alternatives. This very demanding assumption is never fully satisfied in practice. The decision process encourages discussion and exchange of information about alternatives between committee members in part by including concise descriptions of alternatives and requiring agreement at certain stages. When disagreement is indicated by major differences in individual rankings of alternatives or by large values of the disagreement indicators, this should tell the committee to stop and search for sources of disagreement. If the disagreement is due to a difference in the information base between individuals, then the problem can be resolved by sharing and exchanging information. A graphic representation of the diverging scores for an attribute of an alternative helps greatly in such discussions. A committee member with a dissenting opinion can either convince the committee that he has specific valuable information to share, or be convinced that his opinion cannot be substantiated. This serves as an additional disincentive for attempting to manipulate the outcome of the decision process by biasing assessments.

After such discussion, the committee can either decide to return to some earlier stage of the decision process (for example, to correct the evaluation scores) or conclude the process. When adopting the final decision (a ranking or a selection of alternatives) the committee is by no means constrained by the aggregate ranking proposed by the decision support system, but merely guided by the results.

## 4. Implementation Framework

We have experimented with several ways of implementing the framework presented in previous sections. The first implementation, designed mostly for testing the aspiration-led paradigm, ergonomic aspects of user interface, methods of information presentation etc., was based on the data base-centered approach, similar to the concept of the MEDIATOR system (Lewandowski, 1987). This implementation has been used for experimental application in chemical engineering (Dobrowolski and Zebrowski, 1987).

The second implementation of SCDAS is based on the principle of the workstation which implements the SCDAS framework and can cooperate with a standard computer teleconferencing system. Such a concept allows smooth transition from the existing practice of office and telecommunication systems utilization to new forms. Moreover such an environment requires only small modifications or extensions to the existing software to support new functions.

The basic idea of implementing the SCDAS in a teleconferencing framework is the extension of the concept of document. In the standard office automation and teleconferencing systems the text-letters, memoranda etc. - constitute the basic information carrier. In the extended or decision teleconferencing system the concept of document has been generalized - besides of textual data, numbers are transmitted between the members of a group. Moreover, the formalized knowledge necessary to interpret the data and to structure properly the decision process must be implemented within the system and made available in a sufficiently simple form to the users of the system. Therefore, several types of documents can exist simultaneously in the extended teleconference system - documents which can be of different origins and type but strongly interdependent. These dependencies can reflect logical relationships between numeric and textual data, or can reflect the users' opinion and knowledge related to the information being processed.

Standard teleconferencing systems introduce a certain level of information structuring. In the simplest case the conference has a tree-like structure: the conference is split into discussions, discussions are split into topics. Conference participants add their comments into the common pool of documents organized as linked lists. Other types of conferences can exist with different structuring principles.

With information structuring offered by standard teleconferencing systems, the conference participant can have certain difficulties with the analysis of information generated and distributed within the computerized mail or teleconferencing system. Frequently it can be difficult for him to find important notes in the information flooding his computer every day. The issue of informational overload has been studied in detail by Hiltz and Turoff (1985). They state that:

“...The volume and pace of information can become overwhelming, especially since messages are not necessarily sequential and multiple topics threads are common, resulting in information overload... Unless computer-mediated communication systems are structured, users will be overloaded with information. But structure should be imposed by individuals and user groups according to their needs and abilities, rather than through general software features...”

To overcome this problem, several attempts to introduce some level of organization and structuring in the computerized message system have been made. To investigate the problem of applicability of structuring of messages in SCDAS, it is necessary to analyse the possible types of information which can be processed within the system. This information can be categorized according to two attributes: information access and ownership and structural properties of information.

The access to the information generated during the SCDAS session depends on two factors:

\- the privileges of the individuals participating in the SCDAS conference. The conference owner (or committee president) is the only person authorized to change the definition of the problem - like adding new committee members or removing them, changing the list of attributes or list of alternatives etc. He also can generate the textual information relating to the problem definition or to the progress of the conference, which have the read-only status for other committee members. Moreover, he can decide whether at a given stage of the process this information can be visible or hidden to other conference participants.

\- the stage of the process. Since the SCDAS conference has temporal dimension - the decision process advances from the given stage to the next one if all committee members specified all information necessary on the given stage, the access rules can change in time.

With respect to structural properties, the information generated during the SCDAS conference can belong to two classes:

\- the highly structured numerical and qualitative data. This category contains all information constituting the problem definition, related information generated by conference participants (aspirations, scores) as well as information generated by computer (values of achievement function, rankings, graph plots, etc.). There exist strong and well defined relationships between this data – we will call these relationships structured links in the sense that it is well defined what data is required from the conference participants at a given stage, what properties this data should possess, what actions (and calculations) are necessary to perform when data is entered into the system or changed by the user and what data must be used to calculate other numerical information.

\- the unstructured textual information - notes, memoranda, mail notes send to other conference participants. This information is similar to those generated and distributed during the standard conference. The only difference is in the structuring principle – usually, some part of this st of information can strongly relate to the numerical data. Therefore, the numerical data can be treated as the equivalent of a topic in a standard conference – for every numerical item there can exist the linear list of comments generated by conference participants. Therefore the hard links between textual documents can exist – two linear links of comments will be interrelated if there exist links between numerical data which this textual information is associated. We will call these links hard since they are a priori determined by the organization of SCDAS procedure.

Summarizing, the information generated during the SCDAS conference can be structured by the structure of the decision process itself. It is possible, however, that a second layer of links between numerical data and textual information can exist – namely links introduced by the user in order to reflect his particular, personal view on various aspects of the problem being solved. This kind of relation between documents we will call soft links.

The soft links can be arranged in a similar way as in the hypertext system. In this way we have two, parallel layers of links – the soft layer and the hard layer. Therefore, contrary to the standard hypertext we will have the primary relevant documents and the secondary relevant documents – depending on the fact whether relevant documents are belonging to the same layer where the root of the search tree is located.

It is necessary to mention, that the soft layer can be further split into sublayers - the public sublayer and the private sublayer. The public links can be generated either by the committee president or by authorized conference participants. The private links are known only to the user who is creating them and constitute the part of his local information base (the notebook).

The soft links play the role of the remainder – the user can link and browse documents which he, or other participants consider as important on a given stage of the process. Evidently, these documents can contain both the numeric and textual data.

It is necessary to point out the similarity between the document structuring concept in SCDAS system and hypertext systems (Conklin, 1987). However, the concept of the node in the information structure of SCDAS system is much more complicated than in a standard hypertext. On the top level of hierarchy we have data nodes – the information structures responsible for storage and manipulation of a certain class of data. From the user point of view these nodes represent the active electronic forms to be filled by the user. Similar concept of semistructured nodes has been explored by Conklin and applied in ISAAC hyper-text-like the system for supporting the software design process (Conklin, 1987).

Summarizing, we can view the SCDAS decision conference as the document exchange problem with documents being procedurally structured and contextually structured. The documents created during the SCDAS conference are linked. As it was mentioned in the previous sections, some links have organizational character – i.e. they are predefined by the SCDAS procedure. Documents can be also linked by referential links pointing to the information which not necessary belongs to a given category, but can be interesting or relevant from a given point of view. Usually, these links do not reflect the logical relationships between data, but rather the contextual relationships. All conference participants have full freedom to create referential links – both between structured and unstructured documents.

The above mentioned concept of workstation and principles of information structuring are being implemented for IBM-AT in Smalltalk/V. The workstation cooperates with the Telecenter teleconferencing software (Pearson and Kulp, 1981, Fuhrmann, 1987) running on the VAX/780 computer under the UNIX operating system (see Lewandowski, 1988 for more details).

## 5. Applications and Experience

Until now, little practical experience has been gained with the application of the SCDAS procedure. This is mostly due the fact that difficulties in implementing real-life applications in the field of group decisions making are at least a magnitude bigger than in the case of a single decision maker. Usually, such exercises require large resources and a long time to perform, as well as high motivation of individuals participating in the exercise (for more detailed comments regarding the validation of GDSS procedures, see the paper by Iz and Jelassi, 1988). The laboratory experiments which involves students or other randomly chosen participants cannot be considered as a real source of information regarding the applicability of the GDSS procedure.

At the moment, except for some artificial and academic testing examples, two serious applications have been made (other applications are in progress). The first one (done in cooperation with the Academy of Mining and Metallurgy, Cracow, Poland) relates to the problem of selection of technology for methanol production form coal.

According to the result of the analysis of the general structure of energy demand and supply (using the MIDA decision support systems, see Kopytowski and Zebrowski, 1988) it has been decided that the facility for production of methanol with specified production capacity should be located in a particular industrial region. The region in consideration is rich in low grade coal which is not suitable for power generation but can be used for the production of liquid synthetic fuels. Since mining cost in this region is low due to convenient geological conditions, this coal should be considered as a main feedstock for chemical processing. One of the possible locations for this methanol production device is a large chemical plant which, among many other products, produces carbide. Another potential location under consideration is a site next to the open lignite pit. The lignite is cheaper than coal and therefore, can be considered as another possible domestic feedstock. Other feedstocks, like natural gas, must be imported.

Methanol is usually produced on the industrial scale from syngas, a mixture of carbon monoxide and hydrogen, in the presence of a catalyst and under specific temperature and pressure conditions. Syngas may be obtained from any raw material containing carbon, and therefore all fossil resources are potential starting materials. Alternative raw materials are heavy fraction of crude oil distillation, and natural gas. Nine technologies of methanol production based on the above mentioned raw materials constitute the set of alternatives presented to the group of experts. Detailed description of these technologies, including numerical data can be found in the paper by Dobrowolski and Zebrowski (1987).

There are two categories of attributes characterizing a particular methane production technology. The first one is represented by quantitative, easily measurable parameters, such as rate of return, productivity of the capital, thermal efficiency, investment cost, production cost. These attributes are easy to compare since they are usually backed by engineering and economic data. In terms of industrial experts these attributes describe the scale (volume) or the intensity of industrial operation.

The second category of attributes have more qualitative character and can be difficult to measure or their values can be obtained only approximately with relatively high level of uncertainty. These attributes are: investment to increase the manpower availability, impact of terms of trade, predicted net profit, predicted availability of raw materials, availability of technology, environmental impacts. These attributes are much less reliable, more difficult for quantification and therefore the role of the expert's experience and judgment is decisive at the stage of evaluation of alternatives.

The SCDAS procedure has been applied successfully to provide the ranking of technologies and to generate information necessary for further steps of analysis. For a detailed description of the experiment see the mentioned above paper by Dobrowolski and Zebrowski (1987).

The second application relates to the evaluation of performance of control equipment for large electric power generation plants (see Vlacic et al., 1986). During the decision process several alternative microcomputer-based control systems are evaluated. Alternatives, together with corresponding values of attributes obtained on the basis of analysis of simulation models are presented to a group of experts. The problem is more complicated than the standard decision problem analysed in the paper, since attributes possess the hierarchical structure. For example, the attribute dynamic properties depends on the low-level attributes such as system utilization factor, system response time and extent of system centralization. Other high-level attributes include completeness of system functions, flexibility and uniformity of control algorithms, reliability, safety and redundancy, design and functional configuration, documentation, standardization of equipment. Detailed discussion of attributes, presentation of alternatives as well as sample sessions with SCDAS procedure can be found in the mentioned above paper by Vlacic et al. (1986).

Generally, experiments shows the applicability of the SCDAS procedure, however several extensions and modifications have been suggested by individuals participating in these experiments. These comments relate mostly to providing tools for sensitivity analysis as well as better tools for the graphic presentation of results.

## References

Arrow, K.J. and H. Raynaud (1986). Social Choice and Multicriterion Decision-Making. The MIT Press, 1986.

Bui, T.X. and M. Jarke (1986). Communications Design for Co-oP: A Group Decision Support System. ACM Transactions on Office Information Systems, Vol. 4, No. 2. April 1986.

Bui, T.X. (1988). Co-oP: A Group Decision Support System for Cooperative Multiple Criteria Group Decision Making. Lecture Notes in Computer Science. Vol. 290, Springer-Verlag.

Campbell, R. and L. Sowden (1985). Paradoxes of Rationality and Cooperation: Prisoner's Dilemma and Newcomb's Problem. The University of British Columbia Press, Vancouver 1985.

Conklin, J. (1987). Hypertext: An Introduction and Survey. IEEE Computer, September 1987, pp. 17–41.

DeSanctis, G. and R.B. Gallupe (1987). A Foundation for the Study of Group Decision Support Systems. Management Science, Vol. 33, No. 5, May 1987.

Dobrowolski, G. and M. Zebrowski (1987). Ranking and Selection of Chemical Technologies: Application of SCDAS Concept. In: A. Lewandowski and A. Wierzbicki, Eds., Theory, Software and Testing Examples for Decision Support Systems, WP-87-26, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Erlandson, F.E. (1981). The Satisficing Process: A New Look. IEEE Trans. on Systems, Man and Cybernetics, Vol. SMC-11, No. 11, November 1981.

Fisher, W.F. (1979). Utility Models for Multiple Objective Decisions: Do They Accurately Represent Human Preferences? Decision Sciences, Vol. 10, pp. 451–477.

Fuhrmann, C. (1987). Telectr User's Manual. IIASA Software Library Series, LS-16, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Gray, P. (1986). Group Decision Support Systems. In: E. McLean and H.G. Sol. Eds: Decision Support Systems: A Decade in Perspective, Proceedings of the IFIP WG 8.3 Working Conference on Decision Support Systems, Noordwijkerhout, The Netherlands.

Hiltz, S.R. and M. Turoff (1985). Structuring Computer-Mediated Communication Systems to Avoid Information Overload. Communications of the ACM, Vol. 28, No. 7, July 1985.

Huber, G.P. (1984). Issues in the Design of Group Decision Support Systems. MIS Quarterly, September 1984, pp. 195–205.

Iz, P. and T. Jelassi (1988). An Empirical Investigation of Multiobjective Techniques for Group Decision Making. Invited paper to the EURO IX/TIMS XXVIII Joint International Conference, Paris, France, July 6–8, 1988.

Jarke, M. (1986a). Group Decision Support Through Office Systems: Developments in Distributed DSS Technology. In: E. McLean and H.G. Sol, Eds: Decision Support Systems: A Decade in Perspective, Proceedings of the IFIP WG 8.3 Working Conference on Decision Support Systems, Noordwijkerhout, The Netherlands.

Jarke, M., X.T. Bui and M.T. Jelassi (1986b). Micro-Mainframe DSS for Remote Multi-Person Decisions. In: Managers, Micros and Mainframes: Integrating Systems for End-Users. Edited by M. Jarke. John Wiley Information Systems Series. John Wiley & Sons.

Jarke, M., M.T. Jelassi and M.F. Shakun (1987). Mediator: Toward a Negotiation Support System. European Journal of Operational Research, No. 3, September 1987.

Jelassi, M.T. and R.A. Bauclair (1987). An Integrated Framework for Group Decision Support System Design. IRMIS Working Paper W703, Institute for Research on the Management of Information Systems, School of Business, Indiana University.

Johnson, S. (1984). Decision Support for Committee Selection. International Institute for Applied Systems Analysis, Laxenburg, Austria (manuscript).

Keeney, R.L. and A. Sicherman (1975). An Interactive Computer Program for Assessing and Analysing Preferences Concerning Multiple Objectives. Research Memorandum RM-75-12, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Keeney, R.L. and H. Raiffa (1976). Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

Kopytowski, J. and M. Zebrowski (1988). MIDA – Experience in Theory, Software and Application of DSS in Chemical Industry. In: A. Lewandowski and A. Wierzbicki, Eds., Theory, Software and Testing Examples for Decision Support Systems, WP-88-71, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Korhonen, P. and J. Laakso (1986). A Visual Interactive Method for Solving the Multiple Criteria Problem. European Journal of Operational Research, Vol. 24, pp. 277–287.

Korhonen, P. (1988). A Visual Reference Direction Approach to Solving Discrete Multiple Criteria Problems. European Journal of Operational Research, Vol. 34, pp. 152–159.

Kraemer, K.L. and J.L. King (1988). Computer-Based Systems for Cooperative Work and Group Decision Making. ACM Computing Surveys, Vol. 20, No. 2, June 1988.

Lewandowski, A., M. Grauer, and A.P. Wierzbicki (1984). DIDAS – Theory, Implementation and Experiences. In: M. Grauer and A.P. Wierzbicki, Eds: Interactive Decision Analysis, Proceedings, Laxenburg, Austria, 1983. Lecture Notes in Economics and Mathematical Systems, Vol. 229. Springer Verlag, Berlin.

Lewandowski, A., T. Rogowski, and T. Kreglewski (1985). A Trajectory-oriented Extension of DIDAS and its Applica-

tion. In: M. Grauer, M. Thompson, A.P. Wierzbicki, Eds: Plural Rationality and Interactive Decision Processes. Proceedings, Sopron, Hungary, 1984. Lecture Notes in Economics and Mathematical Systems, Vol. 248. Springer-Verlag, Berlin.

Lewandowski, A., S. Johnson and A.P. Wierzbicki (1986). A Selection Committee Decision Support System: Implementation, Tutorial Example and Users Manual. In: Towards Interactive and Intelligent Decision Support Systems. Proceedings of the Seventh International Conference on Multiple Criteria Decision Making Kyoto, Japan, August 1986. Lecture Notes in Economics and Mathematical Systems, Vol. 286, Springer-Verlag.

Lewandowski, A. (1987). Selection Committee Decision Analysis and Support Systems (SCDAS) – Users Manual V. 2.0. International Institute for Applied Systems Analysis, Laxenburg, Austria, manuscript.

Lewandowski, A., T. Kreglewski, T. Rogowski and A.P. Wierzbicki (1987). Decision support systems of DIDAS family. In A. Lewandowski, A.P. Wierzbicki, Eds: Theory, Software and Testing Examples for Decision Support Systems. Working Paper WP-87-26, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Lewandowski, A. and A.P. Wierzbicki (1987). Interactive Decision Support Systems – The Case of Discrete Alternatives for Committee Decision Making. WP-887-38, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Lewandowski, A. (1988a). SCDAS – Decision Support System for Group Decision Making: Short User's Manual. International Institute for Applied Systems Analysis, Laxenburg, Austria, manuscript.

Lewandowski, A. (1988b). Distributed SCDAS - Decision Support System for Group Decision Making: Functional Specification. International Institute for Applied Systems Analysis, Laxenburg, Austria, manuscript.

Lewandowski, A. and A.P. Wierzbicki (1988a). Aspiration Based Decision Analysis and Support. Part I: Theoretical and Methodological Backgrounds. WP-88-03, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Lewandowski, A. (1988b). SCDAS – Decision Support System for Group Decision Making: Information Processing Issues. WP-88-48, International Institute for Applied Systems Analysis, Laxenburg, Austria.

Lewandowski, A. and A.P. Wierzbicki (1988c). Theory, Software and Testing Examples in Decision Support Systems. WP-88-71, International Institute for Applied Systems Analysis, Laxenburg, Austria.

March, J.G. (1986). Bounded rationality, Ambiguity and the Engineering of Choice. In: Rational Choice, Ed. J. Elster, New York University Press.

Mirkin, B.G. (1979). Group Choice. John Wiley & Sons, New York.

Pearson, M.L. and J.E. Kulp (1981). Creating an Adaptive Computerized Conferencing System on UNIX. In: R.P. Uhlig, Ed., Computer Message Systems, North-Holland, 1981.

Rapoport, A. (1984). The Uses of Experimental Games. In: M. Grauer, M. Thompson, A. Wierzbicki, Eds: Plural Rationality and Interactive Decision Processes. Proceedings, Sopron, Hungary, 1984. Lecture Notes in Economics and Mathematical System, Vol. 248. Springer-Verlag, Berlin.

Saari, D. (1982). Inconsistencies of Weighted Voting Systems. Mathematics of Operations Research, Vol. 7.

Schwartz, T. (1986). The Logic of Collective Choice. Columbia University Press, New York, 1986.

Sen, A.K. (1970). Collective Choice and Social Welfare. Holden-Day, Inc., Oliver & Boyd.

Simon, H. (1969). Administrative Behavior, McMillan, New York.

Stefik, M., D.G. Bobrow, G. Foster, S. Lanning and D. Tatar (1987). WYSIWIS Revised: Early Experiences with Multi-user Interfaces. ACM Transactions on Office Information Systems, Vol. 5, No. 2, pp. 147–167.

Tietz, R. (1983). Aspiration-Oriented Decision Making. In: Aspiration Levels in Bargaining and Economic Decision Making, R. Tietz, Ed. Proceedings of the Third Conference on Experimental Economics, Winzenhohl, Germany, August 1982. Lecture Notes in Economics and Mathematical Systems, Vol. 213, Springer-Verlag.

Vlacic, L., B. Matic and A.P. Wierzbicki (1986). Aggregation Procedures for Hierarchically Grouped Decision Attributes with Application to Control System Performance Evaluation. International Conference on Vector Optimization, Darmstadt, 1986.

Wierzbicki, A.P. (1982). A Mathematical Basis for Satisfying Decision Making, Mathematical Modelling, Vol. 3, pp. 391–405.

Wierzbicki, A.P. (1984). Interactive Decision Analysis and Interpretative Computer Intelligence. In: M. Grauer and A.P. Wierzbicki, Eds: Interactive Decision Analysis, Proceedings, Laxenburg, Austria, 1983. Lecture Notes in Economics and Mathematical Systems, Vol. 229. Springer Verlag, Berlin.

Wierzbicki, A.P. (1986). On the Completeness and Constructiveness of Parametric Characterizations of Vector Optimization Problems. OR-Spektrum, Vol. 8, pp. 73–87.
