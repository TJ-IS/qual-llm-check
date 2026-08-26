---
otero_id: 16982
otero_key: "PQCEUHCH"
title: "Value-driven expert systems for decision support"
authors: "Ralph L. Keeney"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90003-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Value-Driven Expert Systems for Decision Support \*

Ralph L. KEENEY

Systems Science Department, University of Southern California, Los Angeles, CA 90089, USA

Values are an inherent part of all decision processes. Hence, values are at least implicitly included in all expert systems intended for decision support. This paper outlines the concepts and methodology, which are based on the principles and procedures of decision analysis, to address explicitly the values in an expert system logically and consistently. Implementation of the concepts and methodology involves the elicitation of values using the same general approach as that used by knowledge engineers to explicate expert knowledge.

Keywords: Expert System, Decision Support, Values, Decision Analysis.

![](/api/attachments/PQCEUHCH/fulltext/images/4d9911b5d88e1c84e4a88593166cd74b741ddf04e887a5822e8849c170a82882.jpg)

Ralph L. Keeney is a Professor of Systems Science, University of Southern California, specializing in decision analysis and risk analysis. His experience includes large-scale siting studies (e.g., power plants), energy policy, environmental and risk studies, and corporate management problems. Dr. Keeney received a B.S. in engineering from U.C.L.A. in 1966 and a Ph.D. in operations research from M.I.T. in 1969. During 1969 to 1974, he was Assistant Professor of Civil Engineer ing and then Associate Professor of Operations Research and Management at M.I.T. In 1974–76. he was a Research Scholar at the International Institute for Applied Systems Analysis, Laxenburg, Austria. Dr. Keeney is co-author of Decisions With Multiple Objectives (Wiley, 1976) with Howard Raiffa, the videotape course Decision Analysis (Center for Advanced Engineering Study, M.I.T., 1979) with Alvin W. Drake, and of Acceptable Risk (Cambridge University Press, 1981) with Buruch Fischhoff, Sarah Lichtenstein, Paul Slovic, and Stephen Derby, and the author of Siting Energy Facilities (Academic Press, 1980).

This work was supported in part by the Office of Naval Research under Contract N00014-84-K-0332 titled 'Value-Focused Thinking and the Study of Values'. It is based on a paper originally presented at the International Conference on Multiattribute Decision Making via O.R.-Based Expert Systems at the University of Passau, Germany, April 20–27, 1986.

## 1. Introduction

The intent of both expert systems and decision analysis is to help decisionmakers make better informed decisions. The manners in which these tools provide this help are quite distinct from each other. Indeed, both decision analysis and expert systems have complementary strengths. Consequently, each has significant advantages that could be usefully adapted by the other. This article focuses on how decision analysis could appropriately be used to improve the potential usefulness of expert systems designed for decision support.

This paper is outlined as follows. Section 2 indicates the key elements in analysis to aid decisionmaking and outlines the relative strengths of expert systems and decision analysis for addressing these elements. Section 3 indicates that values are an inherent part of all decision processes and are, at least implicitly, a part of all expert systems. Because it is difficult to address value issues implicitly in a consistent and logical manner, it may be advantageous to use the explicit logic of decision analysis to address these issues in expert systems. The manner in which decision analysis addresses value issues in decision problems is outlined in section 4. Section 5 discusses the integration of decision analysis into expert systems. Section 6 presents conclusions.

2. Decisions, Expert Systems, and Decision Analysis

The orientation of many expert systems and of decision analysis is prescriptive. That is, the intent is to help make better decisions, rather than to describe or predict how decision will be made. To appraise prescriptive help, it is useful to recognize that decisions should depend on three items: the alternatives available, the possible consequences and their relative likelihoods for each of the alternatives, and the relative desirability of those consequences. Items one and two concern factual issues. The third item, the one of interest in this paper, concerns values.

The fundamental premise underlying the comments in this paper is that since values are the driving force for making decisions, values should be prominent in any analysis designed to aid decisionmaking. To understand that this is the case, consider why it is worth the effort to carefully choose an alternative rather than simply let occur what will. The answer is that some concerned party (e.g., a decisionmaker) is interested in the possible consequences that might occur. The desire to avoid unpleasant consequences and to achieve desirable ones, especially when the differences in the relative desirability of the possible consequences are significant, is the motivation for interest in any decision problem. Hence, values should guide the allocation of time and effort spent analyzing decisions and the processes of creating and evaluating alternatives.

Given the above premise, it would seem reasonable that expert systems designed to assist decisionmakers should be capable of structuring the values which should and do drive the decisions. Quite simply, many expert systems treat values implicitly and heuristically (see Waterman [1986] for examples). Expert systems often do not develop an explicit objective function to provide the flexibility for decisionmakers to investigate the implications of their own values, as opposed to those built into the system (see Lehner, Probus, and Donnell [1985], White and Sykes [1986], and Farquhar [1986]). Consequently, it is also not possible to investigate the implications of values representing different viewpoints. As strengths, expert systems offer remarkable abilities to process information inexpensively and efficient manners to display this information to decisionmakers.

Decision analysis has complementary strengths. Intuitively, decision analysis is a formalization of common sense for decision problems that are too complex for informal use of common sense. A more technical definition is a philosophy, articulated by a set of logical axioms, and a methodology and collection of systematic procedures, based upon those axioms, for responsibly analyzing the complexities inherent in decision problems. The relative strengths of decision analysis are a logical foundation to structure and analyze decision problems, provided by axioms stated in von Neumann and Morgenstern [1947], Savage [1954], and Pratt, Raiffa, and Schlaifer [1964], and sound, tested procedures to implement this logic. The implication of these procedures is often time consuming and relatively expensive, luxuries that are often appropriate for major, one-of-a-kind decisions such as those summarized in Keeney [1982] and von Winterfeldt and Edwards [1986]. By combining the logic and elicitation techniques of decision analysis and the processing abilities and relatively low expense of using an expert system, expert systems that offer users significantly more insight for better informed decisionmaking are possible.

## 3. Inherent Values in Expert Systems

Values are built into any expert system, since values are necessarily utilized in selecting the problem to be addressed, in selecting the data sources to utilize, in selecting the variables to include in the model, in selecting any rules for evaluation, and in selecting the output indices to communicate with the decisionmakers. The inclusion of values in an expert system is part of the responsibility of the knowledge engineer. Before being more specific, let us briefly summarize what is involved in structuring values explicitly.

The structuring of values involves identifying, organizing, and quantifying them. The process can be characterized in four steps: developing a list of objectives, organizing these objectives into an objectives hierarchy, specifying attributes useful for measuring the degree to which the objectives are met by alternatives, and developing an objective function to integrate the achievement of the various objectives into one overall measure. The first three steps rely on systematic procedures, but they are not mathematical in nature (see Keeney [1985]). The fourth step does rely on a significant amount of mathematical theory, some of which is summarized in section 4. The rest of this section contains suggestions for knowledge engineers to explicitly structure values in expert systems.

Use Objectives, not Goals. Objectives indicate something that should be maximized or minimized, and as such always provide a clear indication of what is better. Goals, on the other hand, have an associated 'standard' or 'aspiration level'. For instance, an objective is to maximize the return on an investment portfolio. Goals might be to obtain a twenty percent return or to maximize the probability of a ten percent return. With the former goal, it is not often clear what one should strive toward, as there are uncertainties in any investment decision and no investment would appear to guarantee a twenty percent return. The shortcoming of a goal such as maximizing the probability of a ten percent return is that it does not differentiate between a twenty percent return and an eleven percent return. Most individuals would prefer a ninety percent chance at a twenty percent return and a ten percent chance at a nine percent return to a guaranteed eleven percent return. However, the latter situation clearly maximizes the probability of a ten percent return. In summary, the use of goals as a basis for decisions is often not logically sound, and hence should not be relied upon in expert systems.

Use Fundamental Objectives Rather Than Means Objectives. If the output of an expert system indicates the degree to which means objectives are met rather than the degree to which fundamental (i.e. ends) objectives are met, the decisionmaker must make an implicit connection between those means and the ends in order to gain insight for the decision being considered. The relationship between means and ends is one concerning facts pertaining to the expertise of a domain expert. Hence, it is often more reasonable and desirable to include the relationships between the means and fundamental objectives as part of the expert system. For instance, consider an expert system designed to guide the construction process to minimize the overall time and cost of the project. An expert system that provided only component completion times of the various tasks necessary to complete the project would not offer as much insight as one that logically integrated those into overall construction time and cost.

Consider ‘Degrees’ Explicitly. If the intent of an expert system is to assist one in medical decisionmaking, the objective of ‘maximize the probability of survival’ may not be particularly useful if there are significant degrees of survival. To be more explicit, survival after a disease so that one is capable of doing of all that one was able to do prior to the onset of the disease may be much different than survival where one has a significant number of actions or activities that are not possible. Since such degrees are likely important to the decision process, it may enhance an expert system to address them explicitly.

Select Attributes with Reasonable Inherent Values. If one of the attributes (i.e. measure to indicate the degree to which an objective is achieved) is waiting time, there is the implicit assumption that any minute of waiting time is equally desirable as any other minute of waiting time. If the attribute of an investment program is the net present value of investments, there are strong implications about investment opportunities, consistency of interest rates, cost of transactions, and the relative usefulness of funds at different times automatically built in to the attribute. It is often the case that these implicit value judgments are not appropriate for all uses or all users of a particular expert system.

Construct Attributes When Useful. With many of the decisions that are the concern of expert systems, there may be important objectives for which there is no easy-to-measure attribute. In such cases, it may be desirable to construct an attribute that explicitly includes value judgments deemed appropriate for the problem. In a decision system designed to assist in evaluating alternatives for the treatment of cleft lip and pallet for children, Krischer [1976] constructed an attribute for the physical visual impact of such treatment. In a different context, an attribute that may be appropriate for a general purpose expert system to assist in making financial investments is the 'Social desirability' of various investments to a given user.

Separate Elicitation of Factual Expertise and Values. In most complex decision problems, a decisionmaker with certain objectives must rely on factual expertise from one or more experts. For example, a coherent patient with cancer may have a choice of several treatment strategies that will affect his objectives concerning longevity, quality of life, pain and discomfort, and other family members. He would likely wish to rely on the medical expertise of physicians to indicate the possible consequences of each treatment strategy in terms of his four objectives. However, the appropriate value judgments for the decision problem should come from the patient. With many expert systems, both the factual expertise and the values, often only implicitly addressed, are obtained by the knowledge engineer from the domain expert. A major shortcoming of this procedure is that the domain expert may have very different values from those of the patient. Hence, the separation of facts from values can often lead both to a clarified problem structure and to an expert system capable of providing more relevant advice to users.

Complex Objective Functions Often Indicate Poorly-Selected Objectives. When the objective functions are complex, meaning that they involve more than either additive or multiplicative components of single-attribute objective functions, it is sometimes the case that the original objectives were not wisely selected. Specifically, they may involve means objectives, which may be means to several fundamental objectives; they may involve overlapping objectives and hence doublecounting; or they may involve the omission of key objectives (see Keeney, [1981]). A restructuring of the objectives may then be appropriate. If a complex objective function seems reasonable, both value judgments and factual judgments are interrelated, so it is worthwhile to conceptually distinguish their role and relevance.

Address Value Tradeoffs Explicitly. Value tradeoffs are often a key element of a decision problem, as they indicate how much of one objective the decisionmaker is willing to give up in order to achieve a specific amount of another objective. Consequently, it is often useful to explicitly address these value tradeoffs. Oversimplistic value tradeoffs, such as lexicographic orderings, are often too simplistic. One simply does not try to maximize quantity first, and only subject to that consider quality, nor does one try to maximize quality first, and simply subject to that maximize quantity. Common sense requires that both be addressed simultaneously, and value tradeoffs provide a logical basis to do this.

Introduce Values Sequentially. It is usually the case that some of the values in a decision problem are not very controversial, where others may be. An expert system which allows one to introduce the relatively non-controversial values first and see how far one can get with these in terms of evaluating the relative desirability of the alternatives is useful. One can then sequentially introduce more controversial values and repeat the process. This should lead to more insight from an expert system by indicating exactly what values are crucial to a particular decision. Also, in situations where multiple decisionmakers or stakeholders are concerned with the same decision, it may result in agreement on a possible course of action or at least on alternatives that should be discarded.

## 4. Objective Functions Based on Multiattribute Utility

Once an objectives hierarchy has been established and an attribute has been identified for each of the lowest-level objectives in the hierarchy, an appropriate objective function for the problem can be developed.

Prior to this, let us introduce notation to concisely describe the generic problem structure. We have generated a number of alternatives $A_j$ , $j = 1, \ldots, J$ , and an objectives hierarchy with $n$ lowest-level objectives $O_i$ , $i = 1, \ldots, n$ , where $n$ may equal one. Associated with each lowest-level objective is an attribute $X_i$ , $i = 1, \ldots, n$ . Furthermore, define $x_i$ to be a specific level of $X_i$ , so the possible impact of selecting an alternative can be characterized by the consequence $x = (x_1, x_2, \ldots, x_n)$ . An example of an objective $O_i$ is 'maximize the local economic benefit' and an associated attribute $X_i$ may be 'annual local tax paid'. A level $x_i$ could then be \$29 million.

It is probably impossible to achieve the best level with respect to each objective in a decision problem. The question is, 'How much should be given up with regard to one objective to achieve a specified improvement in another?' The issue is one of value tradeoffs. For decision problems with either single or multiple objectives, it is rarely the case (except in simple problems) that one alternative is guaranteed to yield the best available consequence. There are usually circumstances that could lead to relatively undesirable consequences with any given alternative. The question is, 'Are the potential benefits of having things go right worth the risks of things going wrong?' This issue is about risk attitudes. Both value tradeoffs and risk attitudes are particularly complicated because there are no right or wrong values. Basically, what is needed is an objective function which aggregates all the individual objectives and an attitude toward risk. In decision analysis, such an objective function is referred to as a utility function, symbolically written u. Then $u(x)$ , the utility of the consequence x, indicates the desirability of x relative to all other consequences. Following directly from the axioms of decision analysis, alternatives with higher expected (i.e., average) utilities should be preferred to those with lower expected utilities.

This step, unique to decision analysis, involves the creation of a model of values to evaluate the alternatives. This is done in a structured discussion between a decision analyst and the decision makers to quantify value judgments about possible consequences in the problem. As illustrated in Keeney [1980], the procedure systematically elicits relevant information about value tradeoffs and risk attitudes with provision for consistency checks. In addition to the obvious advantage of providing a theoretically sound manner to evaluate alternatives, the explicit development of a value model offers several other advantages, including indicating which information is of interest in the problem, suggesting alternatives that may have been overlooked, providing a means to calculate the value of obtaining additional information, and facilitating concise communication about objectives among interest parties. In addition, a sensitivity analysis of the value judgments can be conducted to appraise their importance for the overall decision.

The process of determining the utility function can be broken into five steps: (1) introducing terminology and ideas, (2) determining the general value structure, (3) assessing single-attribute utility functions, (4) evaluating scaling constants, and (5) checking for consistency and reiterating. For decision problems with a single objective, only Steps 1, 3, and 5 are relevant. In practice there is considerable interaction between the steps although each will be separately discussed.

Introducing Terminology and Ideas. The basic purpose of this step is to develop a rapport and an ability to communicate between the decision analyst and the decisionmaker or decisionmakers. It should be stated that the goal of the assessment process is to end up with a consistent representation of values for evaluating alternatives. The analysis should make sure that the decisionmakers are comfortable with the assessment procedure and understand the meaning of each attribute and the objective it is meant to measure. If the decisionmakers have not been closely involved in defining the attributes or describing the impact of alternatives, this phase of communication is particularly important. The decisionmakers should understand that there are no correct or incorrect values and that expressed values can be altered at any time.

Determining the General Value Structure. Here, one structures value with a model indicating the general functional form of the utility function $u(x_{1},\ldots,x_{n})$ . To obtain the structure for multiple objectives, one uses value independence concepts in the same way that probabilistic independence is utilized in structuring models of impacts. Most of the independence concepts concern relative values for consequences with levels of a subset of the attributes fixed. The independence concepts are used to derive a simple function f such as

$$
\begin{array}{r l} u (x _ {1}, \dots , x _ {n}) & = f [ u _ {1} (x _ {1}), \dots , u _ {n} (x _ {n}), \\ & k _ {1}, \dots , k _ {m}, \dots , k _ {r} ], \end{array}\tag{1}
$$

where the $u_{i}$ are single-attribute utility functions and the $k_{m}$ are scaling constants. Specific functional forms following from various assumptions are found in Fishburn [1964, 1965, 1970], Meyer [1970], Keeney and Raiffa [1976], Bell [1977], and Farquhar and Fishburn [1981]. Using (1), the overall utility function is determined by assessing the single-attribute utility functions and the scaling constants which weight various combinations of single-attribute functions.

A related approach to model values for multiple objectives involves building a value function $v(x_{1},\ldots,x_{n})$ which assigns higher numbers (i.e., values) to preferred consequences. This is done in a spirit akin to (1) using either single-attribute value functions or indifference curves together with scaling constants. A utility function is assessed over value providing $u[v(x)]$ which incorporates value tradeoffs in v and an attitude toward risk in u. Models of value functions addressing multiple objectives are found in Debreu [1960], Koopmans [1960], Luce and Tukey [1964], Krantz et al. [1971] and Dyer and Sarin [1979].

Assessing Single-Attribute Utility Functions. Procedures for assessing single-attribute utility functions are well developed. In summary, one wishes to first determine the appropriate risk attitude. For instance, one is said to be risk-averse if consequence $(x_{1} + x_{2})/2$ is always preferred to a lottery yielding either $x_{1}$ or $x_{2}$ each with a probability of 0.5. In this case, the average of $x_{1}$ and $x_{2}$ is preferable to risking a half chance of the higher and a half chance of the lower consequence. When one is risk-averse, the corresponding single-attribute utility function is concave. As discussed in Pratt [1964], special risk attitudes restrict the functional form of single-attribute utility functions. A common utility function is the exponential utility function

$$
u (x) = d + b ^ {- c x},\tag{2}
$$

where d, b > 0, c > 0 are scaling constants. This utility function is referred to as constantly risk-averse since it is the only one consistent with the following property. If $x_{3}$ is indifferent to a 0.5 chance at either $x_{1}$ or $x_{2}$ , then $x_{3} + E$ must be indifferent to 0.5 chance at either $x_{1} + E$ or $x_{2} + E$ for all possible E.

To specify the scaling constants d and b in (2), one arbitrarily sets the utility corresponding to two consequences. This is similar to defining a temperature scale by selecting a boiling and a freezing point. The utilities of all other consequences are relative to the two chosen for the scale. To specify the appropriate numerical value for the constant c in (2), one can identify both a lottery and a consequence which are equally preferred by the decisionmaker. For instance, suppose the decisionmaker is indifferent regarding the certain consequence $x_{3}$ and a lottery yielding either $x_{1}$ or $x_{2}$ with equal chances of 0.5. Then, to be consistent with the axioms of decision analysis, the utility of $x_{3}$ must be set equal to the expected utility of the lottery. Hence,

$$
u \left(x _ {3}\right) = 0. 5 u \left(x _ {1}\right) + 0. 5 u \left(x _ {2}\right).\tag{3}
$$

Substituting (2) into (3) and solving yields parameter c.

Evaluating Scaling Constants. With multiple objectives, the same concept is utilized to determine scaling constants, which relate to the relative desirability of specified changes of different attribute levels. To illustrate this in a simple case, consider the additive utility function

$$
u (x _ {1}, \dots , x _ {n}) = \sum_ {i = 1} ^ {n} k _ {i} u _ {i} (x _ {i}),\tag{4}
$$

where $k_{i}, i=1,\ldots,n$ are scaling constants. For this additive utility function, the values of the $k_{i}$ indicate the relative importance of changing each attribute from its least desirable to its most desirable level. To assess these scaling constants, one generates data representing stated value judgments of the decisionmaker. For instance, if the decisionmaker is found to be indifferent between $(x_{1},\ldots,x_{n})$ and $(y_{1},\ldots,y_{n})$ , the utility of these two consequences must be equal. They are set equal using (4) which yields an equation with the scaling factors as unknowns. Using such indifferences, one generates a set of n independent equations which is solved to determine numerical values for the n unknown scaling constants. The equations can be generated by sequentially considering consequences which differ in terms of the levels of only two attributes. This significantly simplifies the comparison task required of the decisionmakers. More details about the assessment of utility functions can be found in Fishburn [1967], Keeney and Raiffa [1976], Farquhar [1984], and von Winterfeldt and Edwards [1986].

Checking Consistency. It has been my experience that there are invariably inconsistencies in the initial assessments. In fact, this is one of the main reasons for the procedure, because once inconsistencies are identified, decisionmakers alter their responses to reach consistency and better reflect their basic values. Furthermore, decision-makers usually feel better after having straightened out their value structure in their own mind. Thus, it is essential to ask questions in different ways and to carefully reiterate through aspects of the assessment procedure until a consistent representation of the decisionmaker's values is achieved.

With multiple decisionmakers, as discussed in Harsanyi [1955], Fishburn [1973], or Keeney and Raiffa [1976], additional value judgments are required to address the relative importance of the different decisionmakers and the relative intensity of the potential impact to each in order to determine an overall utility function. In addition, the decision problem can be analyzed from the viewpoints of the different decisionmakers by using their own utility functions. It may be that the same alternative is preferred by each decision-maker, possibly for different reasons. In any case, it might be helpful to eliminate dominated alternatives, identify the basis for conflicts, and suggest mechanisms for resolution.

The value judgments made explicit in assessing u for any decision maker is an essential part of building a model of values. This process of building a model of values corresponds precisely with that used for any model. We gather some data (the decisionmaker's judgments), and use the data in a generic model (the utility function u) to calculate its parameters (e.g., the $k_{m}$ 's in (1) and c in (2)). Additional value judgments are necessary to structure values of multiple decisionmakers into one coherent utility function.

## 5. Integrating Decision Analysis into Expert Systems

The inclusion of a value model as part of an expert system can be done in different ways. For a given expert system, one may be better than another. At one level, in the development of an expert system, it may be useful to carefully obtain a 'good' objective function to use in the expert system. Such a good objective function would have carefully thought out value judgments built implicitly into the expert system, but it would not allow the user to vary these value judgments easily.

At a second level, the expert system would include a value model that offered the user partial choice of the objective function used in his or her applications of the expert system. For instance, a value model connected to an expert system designed to aid personal financial investment may allow the user to provide value judgments about an appropriate risk attitude and appropriate value tradeoffs for income in different time periods. Other value judgments about the overall form (e.g., an additive or multiplicative utility function) would be chosen by the developers (i.e. knowledge engineers and domain experts) of the expert system and not easily changed by the user for a specific application.

The third level of a value model for an expert system would offer users a menu to select their form for the objective function and dialog to provide the value judgments necessary to imply the specific objective function with that form. It may also provide for easy sensitivity analysis with different objective functions.

The most involved and most flexible value model associated with an expert system would allow the potential user to completely assess his or her own objective function as part of the expert system. Such a flexible system would, however, have to be based on a given set of objectives and attributes, as the output information on those attributes would necessarily need to be available from the expert system. Indeed, different users may focus on a different set of fundamental objectives for their specific purposes. This option is not a great deal different from having a separate expert system to assess an individual's utility function. Along this line, Wellman [1985, 1986] has developed an expert system to identify the appropriate form of a multiattribute utility function consistent with any set of value independence assumptions. Given the form, one would likely rely on many of the ideas in the multiattribute utility assessment programs developed by Humphreys and Wishuda [1980] and Sicherman [1982] to identify the specific utility function.

## 6. Conclusions

The main conclusion of this paper is simple and straightforward. Namely, the use of decision analysis and multiattribute utility theory in developing some expert systems can make a significant contribution to the quality of those systems. This conclusion is based on the following:

(1) Values are the basis for interest in a given decision problem.

(2) The values in the given decision problem are often not explicitly or consistently addressed in expert systems.

(3) Multiattribute utility provides a logically sound and operationally tested method to include values in expert systems.

A very small portion of the total effort in developing an expert system is spent explicitly addressing the value judgments inherent in the problem. The shift of a small amount (e.g. 5 percent) of the total effort to focus explicitly on the values relevant to the decision problem addressed by an expert system can make substantial contributions. We would expect these contributions to enhance both the amount of usage and the usefulness of such expert systems.

Acknowledgment. The comments of Professors Peter H. Farquhar of Carnegie-Mellon University and Richard S. John of the University of Southern California on an early draft were very helpful in revising this manuscript.

## References

Bell, D.E., 1977. A Utility Function for Time Streams Having Interperiod Dependencies, Operations Research 25, 448–458.

Debreu, G., 1960. Topological Methods in Cardinal Utility Theory, in: Mathematical Methods in the Social Sciences, 1959, K.J. Arrow, S. Karlin and P. Suppes (eds.). Stanford University Press, Stanford, CA.

Dyer, J.S., and R.K. Sarin, 1979. Measurable Multiattribute Value Functions, Operations Research 27, 810–822.

Farquhar, P.H., 1984. Utility Assessment Methods, Management Science 300, 1283–1300.

Farquhar, P.H., 1986. Applications of Utility Theory in Artificial Intelligence Research, Technical Report 86-2, Decision Research Program, Graduate School of Industrial Administration, Carnegie-Mellon University, Pittsburgh, PA.

Farquhar, P.H., and P.C. Fishburn, 1981. Equivalence and Continuity in Multivalent Preference Structures, Operations Research 29, 282–293.

Fishburn, P.C., 1964. Decision and Value Theory, Wiley, New York.

Fishburn, P.C., 1965. Independence in Utility Theory with Whole Product Sets, Operations Research 13, 28–45.

Fishburn, P.C., 1967. Methods of Estimating Additive Utilities, Management Science 13, 435–453.

Fishburn, P.C., 1970. Utility Theory for Decision Making, Wiley, New York.

Fishburn, P.C., 1973. The Theory of Social Choice, Princeton University Press, Princeton, NJ.

Harsanyi, J.C., 1955. Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility, Journal of Political Economy 63, 309–321.

Humphreys, P.C. and A. Wishuda, 1980. Multiattribute Utility Decomposition, Technical Report 72-2/2, Decision Analysis Unit, Brunel University, Uxbridge, Middlesex, England.

Keeney, R.L., 1980. Siting Energy Facilities, Academic Press, New York.

Keeney, R.L., 1981. Analysis of Preference Dependencies among Objectives, Operations Research 29, 1105–1120.

Keeney, R.L., 1982. Decision Analysis: An Overview, Operations Research 30, 803–838.

Keeney, R.L., 1985. Hierarchies of Objectives, Report 8515, Faculty of Mathematics and Computer Science, University of Passau, Germany.

Keeney, R.L., and H. Raiffa, 1976. Decisions with Multiple Objectives, Wiley, New York.

Koopmans, T.C., 1960. Stationary Ordinal Utility and Impatience, Econometrica 28, 287–309.

Krantz, D.H., R.D. Luce, P. Suppes and A. Tversky, 1971. Foundations of Measurement 1. Academic Press, New York.

Krischer, J.P., 1976. Utility Structure of a Medical Decision-Making Problem, Operations Research 24, 951–972.

Lehner, P.E., M.A. Probus, and M.L. Donnell, 1985. Building Decision Aids: Exploiting the Synergy between Decision Analysis and Artificial Intelligence, IEEE Transactions on Systems, Man, and Cybernetics SMC-15, 469–74.

Luce, R.D., and J.W. Tukey, 1964. Simultaneous Conjoint Measurement: A New Type of Fundamental Measurement, Journal of Mathematical Psychology 1, 1–27.

Meyer, R.F., 1970. On the Relationship among the Utility of Assets, the Utility of Consumption, and Investment Strategy in an Uncertain, but Time Invariant World, in OR 69: Proceedings of the Fifth International Conference on a Operational Research, J. Lawrence (ed.). Tavistock Publishing. London.

Pratt, J.W., 1964. Risk Aversion in the Small and in the Large, Econometrica 32, 353–375.

Pratt, J.W., H. Raiffa and R.O. Schlaifer, 1964. The Foundations of Decision under Uncertainty: An Elementary Exposition, Journal of the American Statistical Association 69, 353–375.

Savage, L.J., 1954. The Foundations of Statistics, Wiley, New York.

Sicherman, A., 1982. Decision Framework for Technology Choice, Volume 2: Decision Analysis User's Manual, EPRI Report EA-2153, Electric Power Research Institute, Palo Alto, CA.

von Neumann, J., and O. Morgenstern, 1947. Theory of Games and Economic Behavior, Ed. 2., Princeton University Press, Princeton, NJ.

von Winterfeldt, D., and W. Edwards, 1986. Decision Analysis and Behavioral Research, Cambridge University Press, New York.

Waterman, D.A., 1986. A Guide to Expert Systems, Addison-Wesley, Reading, MA.

Wellman, M.P., 1985. Reasoning about Preference Models, Technical Report 340, Laboratory for Computer Science, Massachusetts Institute of Technology, Cambridge, MA.

Wellman, M.P., 1986. Automated Multiattribute Utility Decomposition: Examples, Preprint, Laboratory for Computer Science, Massachusetts Institute of Technology, Cambridge, MA.

White, C.C. III, and E.A. Sykes, 1986. A User Preference Guided Approach to Conflict Resolution in Rule-Based Expert Systems, IEEE Transactions on Systems, Man, and Cybernetics SMC-16, 276–278.
