---
otero_id: 16915
otero_key: "6VAKQCQR"
title: "Understanding and validating results in model-based decision support systems"
authors: "J.J Brennan; Joyce J Elam"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90120-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding and Validating Results in Model-Based Decision Support Systems

J.J. BRENNAN and Joyce J. ELAM
Electronic Data Systems, Detroit, MI, and College of Business Administration, University of Texas at Austin, Austin, TX 78712, U.S.A.

This paper focuses on the issue of how to construct a software environment for modelling systems that enhances the usefulness of models as problem solving aids. The limitations of currently available modelling systems are explored and current approaches to overcoming these limitations are reviewed. A framework for the user-model interface of a model-based DSS is proposed that incorporates a range of powerful capabilities for aiding a user in interpreting, understanding, and validating model results.

Keywords: Model Management; User Interfaces; DSS Functions

![](/api/attachments/6VAKQCQR/fulltext/images/10a6343da26bf31a98f8e43c454cc6fc9531b7a6a2c53c64ed733885a6ca4ed1.jpg)

J.J. Brennan is Manager of Research and Development for Electronic Data Systems, Detroit, Michigan. He received a Ph.D. in Management from the University of California at Los Angeles and has served on the graduate faculty of the University of Texas at Austin. His research interests span the fields of mathematical programming and computer science, with recent emphasis on machine scheduling.

![](/api/attachments/6VAKQCQR/fulltext/images/7f42c1071fcc813f616418979036b0cf37e18f47495d277d344d32050190e1bb.jpg)

Joyce J. Elam is an Associate Professor of Information Systems in the College of Business, University of Texas at Austin. She holds two degrees from the University of Texas at Austin, a B.A. in mathematics and a Ph.D. in operations research. Prior to joining the faculty at the University of Texas at Austin, she was an Assistant Professor at the Wharton School of Business, University of Pennsylvania. She has consulted with a number of organizations on the design and use of decision support systems. Her current research interests focus on understanding and predicting the behavior of users as they interact with decision support systems and applying this knowledge to the design of the user interface.

## 1. Introduction

Decision Support Systems (DSS) are computer-based systems whose objective is to enable a decision maker to devise high quality solutions to what are often only partially formulated problems. At a minimum, complex decision making involves: searching for information about the current and desired state of affairs, inventing possible courses of action, and exploring the impact of each possible course of action. All decision making involves predicting the likely consequences of decisions, which suggests that the decision maker should have a “model” of the problem situation being faced. The majority of DSS in use today do not attempt to represent this model explicitly, but rather provide access to data that can be utilized by an implicit, internalized model. One way to increase the quality of solutions produced by DSS is by incorporating explicit models of the decision making environment.

Endowing DSS with the capabilities offered by a model-based approach to decision making is an evolutionary process. Unfortunately, this evolution has proceeded at only a modest pace, primarily because of the focus on the solution component of modelling systems to the neglect of the model definition or generation component and the report generator or analysis component.

The DSS movement has highlighted the need for a software environment that includes more than a sophisticated solver. It requires a user interface that allows managers to define models and to view their results in a framework – a conceptual model – that makes sense to them. The widespread acceptance of micro-based spreadsheet packages, e.g., Lotus 1-2-3, is in part due to the fact that these software packages allow the user to work through a conceptual model that is a familiar one. The lack of user interfaces in model-based systems that provide problem specific conceptual models in contrast to the typical decision variables/constraints conceptual model has resulted in the less than enthusiastic response of decision makers who feel, justifiably, that they have no means to control or understand the models being used.

The software environment also requires enhanced capabilities that aid a decision maker in validating the results produced from a modelling effort. Managers are naturally wary of complex models that use sophisticated analytical solution procedures; the failure to provide a direct interpretive aid will most likely result in the disuse of such modelling systems. Disregarding the question of “does the model produce sensible results?” can be a major problem even if only simple modelling tasks are performed. Consider a recent report concerning the use of spreadsheet packages on personal computers by executives [1]. There are examples cited of an overestimation of sales by \$8 million due to a mistake in a simple pricing formula and an error in an order for semiconductor components (30 000 vs 1 500) due to outdated data being used. In both cases, failure to provide interpretive aid, even as simple as “does the result make sense?”, results in significant economic losses to the companies involved.

The focus of this paper is on the next evolution, what we call the evolution of smart modelling systems designed for end users, not technicians. The impetus for this evolution will come from at least two directions: (a) the needs of users, as they themselves express them, which are, in turn, acted upon by DSS specialists, and (b) technical advances in knowledge engineering and data management. In what follows we will examine the report generator/solution analyzer component of model based DSS with an eye toward how these components can, and we believe will, be improved. We narrow the discussion to the “back end” of modelling systems because (a) relatively little attention has been paid to this component, and (b) the subject is sufficiently narrow that specific conclusions can be made. Much of what we say is also applicable to the formulation/generation component.

In the next section, we discuss the types of problems that arise in using models to support decision making. In Section 3, we review the current approaches that have been employed to meet the needs of users to overcome these problems. In Section 4, we present a framework for viewing “smarter” modelling systems and detail the basic set of functions required by such systems.

## 2. Limitations of Current Modelling Systems

Management scientists have focused on developing more powerful algorithms and then implementing these algorithms in what we call solvers. In their efforts they have been undeniably successful. These scientists continue to produce entirely new and more efficient algorithms for some problems, and refine their implementations of others. Add to this the dramatic advances in computer architecture over the past decade, and what often results are solvers that are an order of magnitude, or more, faster to run.

How do users respond? Quite often they respond by creating and solving models that are an order of magnitude larger or more complex than previously. Larger and more complex models demand a similar increase in the volume of data churned out by report generators piggybacked onto the solvers.

Not only is the sheer physical volume of these reports growing as solvers are improved, but more important, the task of interpreting and analyzing the output of solvers is becoming increasingly complex. The stated aim of modelling systems is to gain insight and knowledge about the real world system being modelled. As is commonly agreed, models should not be used to produce a solution that is blindly and automatically put to practice. Yet at some point, and perhaps we have already reached it, the size of a model and the attendant output generated by a solver makes the job of interpreting and assimilating the solution ponderous.

Most report generators are designed to present the model's solution with a high level of detail. Unfortunately, detail itself makes the decision maker's task of pinpointing important model relationships difficult. Even with the best report generators available, it often takes considerable effort on the part of both technical and non-technical personnel to divine anything at all of consequences from a stack of model reports, save the solution itself and, perhaps, some marginal cost information.

Related to the question of what is the appropriate level of detail in model output, is the question of what is the appropriate structure of the output. Most modelling systems report their results to the user with a data orientation. Even the usual report formats suggest the flat file arrangement of relational data base systems. We have already mentioned the fact that users respond to modelling systems more favorably when a clearly-specified conceptual model emerges. It seems to us that a major flaw of current modelling systems is their inability to communicate model results in a way most likely to be understood by the user.

Then there is the trouble caused by discontinuities in the information base fed by a modelling system's output. We will illustrate two types of discontinuities that can arise when analyzing the output of a model.

First, there are mathematical discontinuities. For models with integer variables it is well known that the optimal value of the objective function is not, in general, a continuous function of model parameters, e.g., the value of the right-hand-side of a constraint. Under these conditions, a small change in a parameter may cause an unexpected and disproportionate change in the optimal value of the solution. Discovering such effects is not an easy task, although methods of dealing with these discontinuities have been proposed by Nauss [8], among others.

A more pervasive and general type of discontinuity can appear in any question asking/question answering system. It could be termed the natural discontinuity of information sources, and was first studied in conjunction with data base management systems. An example will illustrate it.

Suppose we are querying a data base and ask "what is the cheapest flight from Dallas to Los Angeles on the morning of July 31?" The data base systems responds "XYZ Air - \$299."

The trouble with the answer is that the likely intent of the question is to find a low cost flight from Dallas to Los Angeles. Perhaps an afternoon or evening flight offers a better fare. Or perhaps rates change on August 1, lowering the fare. The questioner would probably like to know this information, but due to discontinuities in the source, does not receive it.

It is not at all difficult to imagine how this type of discontinuity arises in modelling systems, which can be viewed as narrowly focused and highly technical question answerers. On the input side, model parameters can be affected by the type of discontinuity just discussed, rendering the entirety of the model's output a discontinuous source of information. Models are commonly subjected to a sequence of sensitivity runs. Determining which model assumptions or parameters to change and by how much, requires some assessment of the possible presence of discontinuities, and not just mathematical discontinuities. Unfortunately, a complete assessment does not seem possible with only mathematical tools – considerable knowledge of the system being modelled and the fidelity of the model itself must be considered.

Then there is the problem of fidelity itself. No model reflects reality perfectly and modelling bias is probably only controllable in degree; no amount of effort or resourcefulness can purge it completely. A decision maker's knowledge that models can, and often will, be unfaithful to the system being modelled hardly promotes confidence in their use. This psychological barrier to building and using models will not be overcome easily.

One necessary way to overcome this resistance is to understand the process of modelling. Emerging results in the study of model aggregation (see, e.g., Zipkin [10]) fit into this category. The goal of aggregation is measuring, in a formal way, the effectiveness of a model as it moves from coarse to fine on a scale of fidelity. Aggregation, then, is concerned with formalizing the process of modelling.

We argue that efforts to understand the process of modelling are necessary, but not sufficient, to overcome the lack of confidence in models. Our experience suggests that, in order to gain the acceptance modelling systems deserve, they must possess:

(a) The capability of validating the model against all of the information sources available to the decision maker, and

(b) a method and means of delivery to use the information available to the decision maker so as to suggest both model improvements and directions in which sensitivity tests should be made, and

(c) the capability of providing answers to “why did it happen?” and not just “what happens if?”

In summary, most modelling systems would have to receive low marks on:

(a) Their ability to deal with voluminous model output, in particular, their ability to sift model output data so that consequential output features remain;

(b) Their ability to structure output conceptually in a way that facilitates the user's ability to understand, interpret, and validate it;

(c) Their ability to deal with discontinuities, particularly in model input sources;

(d) Their ability to assess both the validity and fidelity of the model based on its output;

(e) Their ability to guide the user to uncover the possibility of interesting future analyses; and

(f) Their ability to explain why the model acted the way it did.

## 3. Approaches for Building Software Environments for Model Analysis and Reporting

A model-based decision support system requires development of three interfaces: the user-model interface, the model-data interface, and the user-data interface [2]. Of the three, the user-model interface is the most critical, least studied, and least understood [3]. The ability of a decision maker to use a model-based DSS in an effective manner without the assistance of a management scientist is largely dependent on the design of this interface. In this section, we review two major approaches, data-oriented and process-oriented, that have been used in the design of the user-model interface.

A data-oriented approach supports the user-model interface by treating the representation of a model and its solution as part of a database. The major objective of this approach is to support the manipulation of large amounts of information within the modelling system. This is clearly an important requirement for any modelling system. This approach, however, simply provides a mechanism for extracting subsets of data. The user is responsible for imposing some structure on the vast amount of data available, i.e., the user must retrieve appropriate data as well as transform the requested data into information.

This approach has been used for locating errors in large, complex models, where the data needed to correct an error exist as a small fraction of the total model output. Several commercially available modelling systems support the data-oriented approach through sophisticated report writers $[4,9]$ . Other systems $[5]$ facilitate the interactive debugging and analysis of model solutions through a query facility. The characteristics common to currently implemented data-oriented modelling systems are (1) they are designed to be used by analysts trained in mathematical programming, and (2) they require considerable effort on the part of the analyst to develop procedures for examining data in order to answer any question related to model validity. These characteristics limit the capabilities of the data-oriented approach to address the limitations outlined in Section 2.

Helping users to understand the process of modelling was discussed in Section 2 as one approach for overcoming the problems associated with using models for decision support systems. Operationally, this process-oriented approach supports the evaluation and interpretation of model results through the use of auxiliary models that provide intuitively reasonable explanations as to why the results of the full model were obtained [6]. The general approach is as follows:

(1) Develop highly simplified analytic models that can be solved by simple arithmetic or in closed form.

(2) Derive from these models hypotheses concerning how the full model solution should behave.

(3) Test these hypotheses using solutions from the full model.

(4) Use the results from (3) to aid in understanding and interpreting the numerical results provided by the full model.

This approach holds considerable promise for helping an end-user understand whether a particular model is a valid representation of a problem situation. The approach has two major limitations, however. First, it has not, as yet, been formally incorporated into a system that would allow an end-user, rather than a management scientist, to perform the steps outlined above. Second, there is no guarantee, indeed only a dim hope, that a simple explanatory model even exists for a particular modelling situation.

The design of the user-model interface for a smart modelling system should incorporate aspects of both of these approaches but must add a new dimension - a knowledge-oriented approach - in order to overcome the limitations of current modelling systems detailed in Section 2. This dimension is described in the next section.

## 4. Enhancing the Analysis Component

Our goal in this section is to distill, from our analysis of the limitations of current modelling systems in Section 2, those key capabilities that a “smart” modelling system would possess. Below we describe six of these key capabilities. Our description is not in terms of any particular representation scheme and we impose no a priori restrictions on the method of implementing each capability. Our approach is simply this: given the current limitations of most model-based DSS, what fundamental capabilities must be available to overcome these limitations? The reader is forewarned that the boundaries between the six key capabilities we list are not always clear cut.

## 1. Detection

Detection is the ability to decide, in specific cases, what is important. Part of the detection task is also summarizing pieces of information deemed important to create key facts. Of all the capabilities we list, detection is the most fundamental in tackling the limitations of model based DSS. If the analogy of a computerized Sherlock Holmes comes to mind, then the analogy is a good one, for Holmesian capabilities are exactly what we mean here. The detection capability is not guided by expectations; rather it is the ability to assess and analyze openly.

The salient difference between detection and report generation is this. The latter makes the assumption that the modelling situation encountered can always be characterized by the same set of important facts and summary measures. A system possessing detection capabilities does not rely on this assumption.

## 2. Verification / Validation

This capability is that of answering the question, “do the model results make sense?” This capability would make automatic inquiries into how the results obtained compare to actual situations, experience or expectations. The user would be informed of substantive variances. This function would also allow the user to determine whether important relationships that exist in the situation being modelled exist in the model itself and also discover those relationships that are missing.

## 3. Natural Language

Although this capability is included for the sake of completeness, it is not at all clear that DSS with natural language capabilities accomplishes much in the way of model analysis directly. Granted, natural language capabilities might greatly enhance the ease of use of DSS, model-based or otherwise, but our concern is mainly on the power of the analytical component of DSS. In that regard, natural language capabilities do not seem crucial.

In fact, it is possible natural language will delay the development of more powerful model based DSS. A likely scenario is that the development of usable language capabilities will proceed the development of other capabilities mentioned here. In that event, natural language and existing DSS (primarily nonmodel-based) will be paired. This pairing could provide inertia to the adoption of model-based DSS as tools, as well as draw resources away from efforts to enhance model based systems. Nevertheless, from the user's standpoint, natural language capabilities might be the vehicle with which to deliver other enhancements.

## 4. Guidance

Guidance addresses the question of “what to do next.” This capability is a generalized version of sensitivity analysis, which is often available as a byproduct of solutions to mathematical programming problems. It is the ability of the DSS to provide the user with clues as to interesting or important changes to the model structure or parameters. The guidance capability would also help the user recognize opportunities or avoid pitfalls (e.g., the effects of discontinuities).

## 5. Explanation

Explanation is the power to provide answers to inquiries of why the model acted the way it did. To automate the explanation process beyond what is currently available (i.e. the ability to query a data base) requires that some subset of the DSS understand the model and its relationship to the situation modelled. The ability of the DSS to explain some or all of the model's behaviors seems to us to be a critical factor in comforting users who would otherwise be skeptical of model results. At the same time, building explanatory powers into a DSS is a formidable task, since the underlying rationale to model solutions (if any) is often not easily seen, even by expert technicians.

## 6. Exploration

Exploration is the ability to use the model as a predictor of the behavior of the system being modelled and to perform other inferential tasks of a general nature. Examples of exploratory tasks are: (a) generating hypotheses concerning system (or model) behavior, (b) generating simple explanatory models based on the pattern of model results, and (c) anticipating or guessing model solutions for scenarios substantially different from the norm.

Our description of major system capabilities provides some direction in future development. We have not tried to force the tools on the problems; rather we have attempted, ir. a general way, to consider what tools are needed to cope with them.

The pace of development of these capabilities will undoubtedly be slow. Creating a system with only modest capabilities along the lines we envision is years off. Yet it is worthwhile to carefully examine what we want model-based DSS to do and equally to carefully assess the possibility of accomplishing an effective implementation.

## 5. Conclusion

In this paper we have outlined a framework for the user-model interface of a decision support system that overcomes many of the limitations of current modelling systems. Through this interface, a user is provided with a range of powerful capabilities – detection, validation, communication, guidance, explanation, and exploration – that allows models to be used as problem solving aids. To provide these capabilities, the modelling system must have powerful data management capabilities, incorporate an understanding of the modelling process in general, and an understanding of the problem situation being addressed in particular. Our hypothesis is that knowledge engineering promises to be important technology underlying the development of such systems. We readily admit that developing even elementary versions of the capabilities we have discussed is a formidable task – no loss formidable than development of model solvers. Nonetheless, it will be an important undertaking.

## References

[1] Business Week, How Personal Computers Can Trip Up Executives, (Sept 1984).

[2] R. Bonczek, C. Holsapple and A. Whinston, The Evolving Roles of Models in Decision Support Systems, Decision Sciences (1980).

[3] J. Elam and R. Schneider, Optimization-Based Decision Support Systems, Working Paper, College of Business Administration, University of Texas (1984).

[4] E.F.D. Ellison and G. Mitra, UIMP: User Interface for Mathematical Programming, ACM Transactions on Mathematical Software, Vol. 8, No. 3 (Sept 1982).

[5] W. Kurator and R. O'Neill, Peruse: An Interactive Query System for Mathematical Programs, Technical Report TR/OA/79, United States Department of Energy.

[6] A. Geoffrion, The Purpose of Mathematical Programming is Insight, Not Numbers, Interfaces, Vol. 7, No. 1 (Nov 1976).

[7] N. Greenfeld and M. Yonke, AIPS: An Information Presentation System for Decision Makers, Report No. 4228, Bolt Beranek and Newman, Inc. (Dec 1979).

[8] R.M. Nauss, Parametric Integer Programming, University of Missouri Press (1979).

[9] UNICOM Consultants Ltd.. A Brief Survey of the Currently Available Matrix Generator Report Writer Systems (1974).

[10] P. Zipkin, Bounds on the Effect of Aggregating Variables in Linear Programs, Operations Research, Vol. 28, No. 2 (March–April 1980).
