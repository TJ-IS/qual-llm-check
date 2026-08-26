---
otero_id: 24985
otero_key: "EUTNGC6S"
title: "Enhancing User Understanding in a Decision Support System: A Theoretical Basis and Framework"
authors: "David M. Steiger"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518214"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enhancing User Understanding in a Decision Support System: A Theoretical Basis and Framework

David M. Steiger

To cite this article: David M. Steiger (1998) Enhancing User Understanding in a Decision Support System: A Theoretical Basis and Framework, Journal of Management Information Systems, 15:2, 199-220, DOI: 10.1080/07421222.1998.11518214

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518214

![](/api/attachments/EUTNGC6S/fulltext/images/6b1d9297032c776c389524cf14fa18936ff73d8969388420a0d1bde7165ed0ff.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/EUTNGC6S/fulltext/images/9284de9cd2a5029f2bc3b0015bf65efa93998ff111843336fea137cda2fd6471.jpg)

Submit your article to this journal

![](/api/attachments/EUTNGC6S/fulltext/images/96a04df71802948f16aca011a7b0f86f354c50fce7dfcd262eb1f911a4377410.jpg)

Article views: 2

![](/api/attachments/EUTNGC6S/fulltext/images/150fbccc7f5844b8d0859d6aec4738c455b839577d77d9742a052787272b9923.jpg)

View related articles

![](/api/attachments/EUTNGC6S/fulltext/images/20a9c15846d44e8116218d279d6a9b690a085b505f55222f78d7739c66cd810d.jpg)

Citing articles: 1 View citing articles

# Enhancing User Understanding in a Decision Support System: A Theoretical Basis and Framework

DAVID M. STEIGER

DAVID M. STEIGER is an Assistant Professor in the Infonnation Systems and Operations Management Department at the University of North Carolina at Greensboro. He received his B.S. in electrical engineering and M.B.A. from the University of Texas at Austin and a Ph.D. in management science/infonnation systems from Oklahoma State University. Between his M.B.A. and Ph.D. degrees, he spent fifteen years in various analysis and managerial positions in industry, applying the concepts ofinfonnation systems and management science. Dr. Steiger's research interests include decision support systems, model analysis systems, and inductive artificial intelligence technologies. His articles have appeared in Infonnation Systems Research, Management Science, Journal of Management Infonnation Systems, Inteifaces, ORSA Journal On Computing, European Journal of Operational Research, and Annals of Operations Research.

ABSTRACT: The primary purpose of decision support systems (DSS) is to help the decision maker develop an understanding of the ill-structured, complex environment represented by the model. This paper concentrates on understanding the modeled environment through model analysis. Specifically, the purpose of this paper is to propose a framework for model analysis based on Perkins's theory of understanding and its basic premise (knowledge as design) and basic components (purpose, models, and arguments). This framework encourages enhanced user understanding in a DSS via the synergistic combination and integration of: (J) cognitive science (theory of understanding), (2) artificial intelligence (machine learning, knowledge extraction, and expert systems), (3) model analysis (deductive and inductive), and (4) DSS (model management, instance management, and knowledge-base management).

KEY WORDS AND PHRASES: artificial intelligence, decision support systems, design theory, model analysis, model management systems, post-optimality analysis, sensitivity analysis, theory of understanding.

THE PRIMARY PURPOSE OF DECISION SUPPORT SYSTEMS (DSS) is to help the decision maker develop an understanding of the ill-structured, complex environment represented by the model. There are several potential sources of understanding in the modeling process. One such source is in model fonnulation. For example, a decision maker might modify his or her mental model based on (I) the discovery of new relationships between key factors during model development, (2) the development of counterexamples of assumed relationships, and/or (3) the acknowledgment offallacies in deductive logic.

Another potential source of understanding is the deductive analysis of a single model instance in light of the knowledge inherent in the mathematical model and its instantiating data. For example, if the model is formulated and solved in linear programming (LP), the simplex algorithm's sensitivity analysis can help the decision maker understand the relative importance of key parameters and how incremental changes in one parameter can affect the solution [22].

A third potential source of understanding is the inductive analysis of multiple, related solved model instances. For example, if several model instances are specified in which two or more uncertain parameters are varied over appropriate ranges, an analysis of the multiple solved instances may provide new knowledge concerning the relative importance of the individual parameters and how the key parameters interact to affect the model solution [68, 69].

A fourth potential source of understanding is the analysis offeedback after the model has been used to make decisions in real-world situations: for example, differentiating and explaining the forecasted impact of an implemented model decision versus what actually happened.

Not uncommonly, understanding can be gained through a synergistic combination of two or more of the sources of understanding described above: for example, during model formulation and model analysis. For example, an integrated supply, distribution, and marketing model improved profits at a major petroleum refining/marketing company during both its formulation and subsequent implementation. That is, profits improved during model formulation because the modeling effort encouraged decision makers to reexamine their operations and decisions in light ofrational decision making and new key factors that resulted from reorganizing the company as a stand-alone profit center. Specifically, high inventory carrying costs (included explicitly in the formulation of the model) encouraged a more proactive management of product inventories. These initial decisions were verified and further refined via analysis of multiple what-if cases produced by the completed model. The overall results led to reductions in product inventories of \$116 million, resulting in an increase in annual pretax profits of \$14 mi1lion, based on the then-current 12 percent interest rates [37, 38].

This paper concentrates on enhanced understanding of the modeled environment through model analysis. Model analysis is a part of the more general field of model management, the latter including model formulation, model solution, and model analysis (see [44] for an excellent review of model management systems). The purpose of this paper is to propose a framework for model analysis based on Perkins's theory of understanding [58] and its basic premise (knowledge as design) and basic components (purpose, models, and arguments). This framework addresses enhanced user understanding of the modeled environment by integrating the purpose of the modeling effort as specified by the decision maker, the knowledge inherent in the model and its instantiating data, the deductive and inductive analysis of solved model instances, the development and use of computer-generated arguments that relate the results of the analysis to the purpose of the model, and the artificial intelligence/information system technologies that are potentially applicable to understanding.

The evolution of this framework will be evoked by: (1) the needs of the decision maker in his or her search for understanding of ill-structured, complex problems, (2) the innovative advances in inductive data analysis technologies and their application to model analysis, and (3) the synergistic combination of cognitive science (theory of understanding), artificial intelligence (machine learning, knowledge extraction, and expert systems), and DSS (model management, instance management and knowledgebase management).

## Taxonomy and Review of the Current Model Analysis Literature

MODEL ANALYSIS SYSTEMS, AN INTEGRAL COMPONENT of model management systems [12,21,44], are systems that enhance the decision maker's understanding of the business environment represented by the model, by helping him or her interpret and manipulate the output of model solvers and analyze existing knowledge and/or extract new knowledge concerning the complex business environment represented by the model. Existing model analysis systems can be divided into two broad classes, based on the predominant type oflogic employed: that is, deductive model analysis systems CDMAS) and inductive model analysis systems (IMAS). Both of these classes are defined and discussed below, complete with descriptions of existing and prototype analysis systems.

Figure I provides a summary of the taxonomy. The evolutionary third class is labeled as Understanding via Model Analysis Systems (UMAS); it is discussed later.

## Deductive Model Analysis Systems

Deductive model analysis systems (DMAS) apply paradigm- or model-specific knowledge to a single instance of the model, addressing such questions as "Why is this the solution?," "Why do the solutions to two model instances differ so much?," or, in the case oflinear programming models, "Why is this instance infeasible?" There are DMAS for each of the three major modeling paradigms: linear programming (LP), simulation, and spreadsheet models.

Two examples of linear programming-based DMAS are ANALYZE [22, 23, 24] and its predecessor, PERUSE [45]. ANALYZE is a computer-assisted analysis system that provides interactive query ofthe LP matrix and the solution values (I) to document and verify the model, (2) to trace causation via network path analysis, (3) to analyze causes of infeasibility, and (4) to simplify the model via substructure elimination or embedded network identification. ANALYZE provides "an artificially intelligent environment, with English translation of results automatically obtained" which is suitable for both expert and nonexpert users oflinear programming [24]. ANALYZE includes a wide variety of commands that allow the analyst, among other things, to find null and singleton rows and columns, to determine implied bounds on primal quantities and dual prices, to report summary statistics, to trace a complete flow path to a designated output, and to report value statistics.

In addition to LP-based DMAS, there is a prototype DMAS that helps analyze simulation models named I-KBS [63]. I-KBS is an intelligent system that helps managers conceive and develop simulation models, as well as learn and verify interactions between model entities. I-KBS provides run-time graphics to aid deCIsion makers in their understanding of causal relations (i.e., events that cause other events) and detect errors in logical relationships.

![](/api/attachments/EUTNGC6S/fulltext/images/1df9180ba7f57d18fa00f7543bf6c2c869f3c5091518af1fdc3891bb3c5343fe.jpg)  
Figure 1. Taxonomy of Model Analysis Systems

There is also a DMAS for spreadsheet-based models named IFPS/Plus [14], a commercially available system based on the ROME/ERGO research system developed at Carnegie-Mellon University [42,43,81]. IFPS/Plus features a set of explanation commands for interpreting and explaining the difference between a specified variable in two model instances (spreadsheets) or in two different periods of the same spreadsheet. These commands allow the user to "trace the path of influences in a model or consolidated structure, so you can see not only which variables are most important from a definition viewpoint, but also which ones had the most influence on the change in values" [14]. For example, the WHY command lets the user ask questions about why a value changes, providing the answer in terms of the smallest subset of variables that accounts for most--say, 80 percent--ofthe change. Variables in this subset are further categorized according to whether they have a positive or negative (counteractive) effect on the variable in question.

In addition, Candle-lighting [34, 31,32] contains a DMAS component that provides an interactive analysis of LP models (and potentially other types of models), based on user-supplied submodels and/or surrogate models. A submodel consists of an equation (i.e., model) that, when executed, determines the value for the parameter of the main model: for example, an objective function cost coefficient may really be a function of labor hours, cost oflabor, and an inflation factor. A surrogate model represents a rule of thumb about some underlying relationship between the main model parameter and other, more elementary, components. Candle-lighting uses these submodels and surrogate models to expand normal sensitivity analysis to answer such questions as: Do any submodels have common variables, and, if so, how much can these common variables change before the basis changes? And what is the cost of changing the results of the model, given that we can act so as to alter assumptions of the model?

## Inductive Model Analysis Systems

Inductive model analysis systems (IMAS) operate on a set of related model instances that represent historical situations familiar to the decision maker and/or what-if cases specified by him or her. The primary goal of IMAS is to help the decision maker develop insight( s) into the business environment represented by the model. Geoffrion [16] states that such insight is seldom evident from the output of a single model run, but is instead generated from the study of many "what-if' cases; in other words, the decision maker must go beyond knowing what the solution is for a given set of input data and discern why the solution is what it is. Developing insight(s) from multiple instance analysis is ultimately a process of finding trends, surprising model behavior(s), and/or comparing the behavior of the model with what is expected or observed in the real world [28].

Inductive model analysis systems are distinguished from deductive analysis systems by both the required input and the type of processing logic employed. That is, IMAS operate on many model instances and apply inductive analysis technologies to extract new knowledge, whereas DMAS operate on one or two model instances and apply deductive analysis based on known, paradigm- or model-specific knowledge. Also, 1M AS are independent of the modeling paradigm, matching the generality and analysis requirements of state-of-the-art modeling languages, such as Structured Modeling [17]

There are several model analysis systems that qualify as IMAS. The first of these [35, 36] applies regression analysis to multiple runs of a (simulation) model, to determine the impact of changes in the model's input parameters on its output; that is, it uses regression to build a metamodel of the simulation model. The authors of this analysis technique rely heavily on statistical experimental design to determine the optimal number of model runs that provide statistically significant results and yet keep model runs to a minimum. For example, they recommend an orthogonal experimental design, specifically a fractional factorial design, when considering main effects only--that is, assuming a first-order polynomial regression model with no interaction between independent variables. They also suggest that it is better to assume significant interactions between pairs of factors, as well as quadratic effects---that is, a secondorder polynomial regression model. However, such designs require many more model runs; to reduce the number of significant dependent variables in such cases, the authors apply the sequential bifurcation screening method [3, 4]. Such regression analysis applied to multiple model instances makes several assumptions, most important, that the analyst knows, a priori, the structure of the resulting metamodel--that is, the order of the approximating polynomial and the statistically significant interaction tenns. It also assumes well-behaved error terms (normally independently distributed). In addition, the sequential bifurcation assumes prior knowledge of the direction of change in the dependent variable caused by changes in each independent variable and the interaction term.

Another IMAS is LISA [65,66]. LISA accepts, as input, a set of many (perhaps one thousand) model instances generated via Monte Carlo simulation and applies standardized rank regression coefficients and partial rank correlation coefficients to determine the key parameters in a probabilistic model-that is, those parameters that are most important in determining variations in the output variable.

A third IMAS is Global Sensitivity Analysis [76], the goal of which is to provide extended sensitivity analyses, based on the analysis of a set of solved model instances. The input to Global Sensitivity Analysis consists of: (I) the marginal distributions of up to ten stochastic model parameters or groups of parameters, where a parameter might be an objective function coefficient, a right-hand side value, or a matrix coefficient, if the model is a linear programming model, (2) a prespecified set of nonlinear, multinomial terms involving the stochastic parameters, with the set of terms based on prior human knowledge or model-specific expertise, and (3) a large set of perhaps two thousand solved model instances obtained by repeatedly varying (via Monte Carlo simulation) one or more of the stochastic parameters and resolving the model. Processing consists of using backward, stepwise, least-squares regression to find the "best $\mathbf { f i t ^ { \prime \prime } }$ between some subset of multinomial terms and the set of instance solutions. The output is the best fit polynomial (consisting of an additive model of twenty to forty or more multinomial terms) and the associated regression coefficients, along with the coefficient of determination, $R ^ { 2 }$ . The output polynomial is then used to determine the sensitivity ofthe original model to changes in a given parameter and to determine which stochastic parameter(s) are most influential in the model solution.

The fourth IMAS is called INSIGHT [68, 69]. INSIGHT is a prototype analysis environment whose goal is to generate, using artificial intelligence, a simplified auxiliary model or metamodel that helps the decision maker develop insight(s) into the business environment being modeled. The input to INSIGHT consists of a small set of perhaps ten to fifty solved model instances generated either by the decision maker through a series of what-if instances or by Monte Carlo simulation If the marginal distributions ofthe uncertain parameters are known or estimated. Processing consists of two sequential steps: first, the Group Method of Data Handling (GMDH) algorithm, an inductive self-organizing cross between statistics and neural networks that employs a multilayered cascading network of interconnected nodes to model nonlinear relationships [15,27,60], is utilized to generate an additive model oflinear and/or nonlinear multinomial terms that explain variations in the solutions to the model instances, based on variations in the input parameters, and, second, stepwise regression is used to form a "best $\mathbf { f } _ { 1 } \mathbf { t } ^ { \dag \prime }$ simplified metamodel from a subset of the multinomial terms produced by GMDH. This simplified auxiliary model helps the decision maker develop insight(s) into the interactions and tradeoffs between key model parameters, as well as the sensitivity of model solutions to changes in parameter values. INSIGHT has been used to duplicate the insight-generating simplified auxiliary model for a classical facility location model [16] without requiring the human expertise or mathematical manipulation used in Geoffrion's analysis.

In addition to the above systems, there is an inductive component in the Candlelighting approach [8, 33]. That is, Candle-lighting uses genetic algorithms and associated analysis technologies to address two goals: (1) to search for effective combinations of parameters, within given constraints, associated with possible actions by the decision maker, and (2) to generate and analyze key tradeoffs and relationships between key parameter values and the associated model results. In both of these situations, Candle-lighting performs an automated, heuristically driven what-ifsearch, instead of requiring analysts to manipulate parameter values directly.

## Limitations of Current Model Analysis Systems

There are four primary shortcomings of current deductive/inductive model analysis systems. First, there is no mechanism that promotes, or even allows, the integration of existing knowledge inherent in a DMAS (or the model itself) with new knowledge extracted via an IMAS. It seems reasonable that such integrated knowledge can provide a significant enhancement to the decision maker's understanding of the business environment.

Second, there is no motivation to generate multiple simplified auxiliary models, or metamodels, from IMAS; however, multiple metamodels can be an effective aid to understanding the model and can clarify interrelationships between input parameters and the model solution. Multiple metamodels can be generated by using different technologies (e.g., INSIGHT, Global Sensitivity Analysis, regression), by modifying the set of instances that are input to a specific technology, by modifying the order of those instances (which may lead to different models in certain inductive technologies), or by modifying appropriate technology parameters (e.g., the step size in neural network-based techniques, the complexity parameter in GMDH-based techniques, or the threshold criteria for the removal/addition of terms in stepwise regression).

Third, there is no provision or theoretical basis for evaluating multiple metamodels, either by comparing one model against another or by validating the accuracy, necessity, sufficiency, and consistency of an individual metamodel and its components.

And fourth, there is no way to link analysis results to the basic principles of the environment being modeled, a link that could reasonably enhance the understanding of results by the decision maker.

In fact, what is needed is a design theory for model analysis systems that enhances understanding by the decision maker of the modeled environment through model analysis. Such a design theory should include metarequirements (a class of goals to which the theory applies), a metadesign (a class of systems and components suggested to meet the metarequirements), one or more kernel theories that govern design requirements and design process, a design methodology, and a set of testable design process hypotheses (to verify consistency between design method results and the metadesign) [6, 29, 77]. A design theory for model analysis systems, based on Perkins's theory of understanding, is proposed in the following sections.

## Theory of Understanding

To "UNDERSTAND" IS TO COMPREHEND FULLY, OR GAIN A FULL MENTAL GRASP, of the nature, significance, or explanation of a situation [78]. Several psychologists have proposed theories of understanding. One such early theory was by Wertheimer, a Gestalt psychologist who suggested that understanding was the perception of "rho relations" which represent the "inner structure" of the problem or situation. Such rho relations, once perceived, could be used to transfer understanding to other situations (i.e., were at least somewhat generalizable) and excluded, or made unlikely, the understanding offalsehoods [79]. Dunker [13] suggested that understanding required a knowledge of the functional value (i.e., the purpose) of the solution. More recently Newton [54], in her theory of understanding, proposed that one understands a situation (i.e., a problem and its solution) if one is able to develop a mental model of the situation, a model sufficiently rich and valid to serve as a performance guide in that situation.

Perkins [58] provides perhaps the most insightful description of understanding and its prerequisite components in his theory of understanding, a theory that adapts the concepts of Wertheimer and Dunker and is consistent with Newton's theory. Perkins states that understanding involves the knowledge of three things: (1) the purpose of the analysis or what the decision maker wants to understand, (2) a design (or model) of the process/system to be understood, and (3) arguments about why the design serves the purpose.

The purpose of the analysis is simply a statement of what the decision maker wants to understand-for example, to find the area of a parallelogram, a simple example used throughout the following discussion. In a DSS, the specific purpose should be stated by the decision maker as part of model analysis, and should include key words or phrases, as well as references to key underlying concepts, such as inventory control, working capital, capital budgeting, the time value of money, and so on, that might be appropriate in many business-related problems. Alternatively, the purpose might be implied or hypothesized by the system from the problem or through the analysis of a set of related what-if model instances.

The design is a general description of the material to be understood, its structure, components, properties, relations, and so on [58, pp. 2-6]. In a DSS, the design takes the form of one or more hypothesized models or metamodels. These models typically refer to concepts already understood by the decision maker. For example, in understanding how to calculate the area of a parallelogram, the design or hypothesized model might be the (previously learned) formula for calculating the area, A, of a rectangle, $A = b \times h$ , where b is the length of the base (in inches) and h is the height (also in inches). Concepts already understood in this model include mathematical equality, base, and height. The design may also include one or more illustrative examples, or instances, of the model: for example, a drawing of a parallelogram with the length of its base, height, and area noted on the figure.

The unique addition made by Perkins's theory is his emphasis on arguments. Arguments can be thought of as evidence showing that the hypothesized model does, or does not, support the purpose. There are three general types of arguments: evaluative arguments, simple explanatory arguments, and deep explanatory arguments.

## Evaluative Arguments

Evaluative arguments are arguments that focus on assessment, addressing whether the model does a good job in faithfully representing the knowledge [58, pp. 33,45]. Such arguments may take the form of comparing the advantages and disadvantages of two competing models, to determine which model better serves the purpose of understanding the knowledge-that is, which is the better model with respect to accuracy, simplicity, conceptual validity, and so on. For example, the formula (model) $A = b ^ { 2 }$ may prove accurate for calculating the area of some, but not all, parallelograms, whereas the formula $A = b \times l _ { 1 }$ sin x (where $l _ { 1 }$ is the length of one side and x is the acute angle between the base and the side of the parallelogram) is accurate for all parallelograms; thus, the second formula is preferable to the first based on accuracy. However, a third formula, $A = b \times h$ , would match the accuracy of the second formula and have the additional advantage of simplicity (no trigonometric functions), making it the best of the three models. Evaluative arguments may be based on multiple evaluation criteria and a relative weighting scheme as specified by the decision maker or inferred from the purpose.

Evaluative arguments also address the sufficiency, necessity, and consistency requirements of a single model and its components. Model sufficiency addresses whether the model is sufficient to depict the knowledge and/or to provide sufficient understanding of the knowledge. For example, Darwin's theory of natural selection, including its three primary conditions (generation-to-generation similarities or inheritance, individual variation, and natural selection), has been used to explain the evolution of both plant and animal species. That is, it sufficiently explains long-term changes of a species in response to the similarities and adaptations of the species to its environment.

Model necessity addresses whether all components of the model are required to depict or understand the knowledge. In Darwin's theory of natural selection, it is easy to show that each component in the model is necessary-4hat is, without generationto-generation similarities or inheritance, two generations would be alike only in a random sense; without "variation," two generations would have exactly the same characteristics and would therefore never evolve; and without "selection," all members of the species would be equally likely to survive and reproduce, providing no evolutionary direction.

Model consistency addresses whether all components of the model are consistent with other components. In mathematical models, consistency is defined in terms of units of measurements across all model terms. For example, in an additive model, all model terms must reduce to the same units of measure----such as square feet, foot pounds, and so on.

## Simple Explanatory Arguments

Simple explanatory arguments are arguments that explain or define the elements of the model and/or state what each element contributes. For example, simple explanatory arguments for our parallelogram model might include the following: (I) b is the base length, in inches, of the parallelogram, (2) h is the height, also in inches, from the base to the top of the parallelogram, (3) the area is directly proportional to both the base length and height, (4) the base and height measurements contribute equally to the area (i.e., both have the same coefficient and are raised to the same power), and (5) the area is independent of the length of the sides and the angle between the base and side individually, but is directly proportional to a combination of these parameters.

Alternatively, for the Darwin example, simple explanatory arguments might include the following: (I) "species similarity" suggests that the generations of a species have almost, but not exactly, the same survival characteristics as parent generations, (2) "variation" suggests that a small percentage of each generation differs in some significant respect and that some of these variations make their bearers better able to adapt to particular ecological conditions than their parents, and (3) "selection" suggests that there are external forces (e.g., predators, ecological conditions) that affect the reproductive ability of individual members of the species.

## Deep Explanatory Arguments

Deep explanatory arguments seek to explain a design or model in terms of basic underlying principles. For example, deep explanatory arguments for our parallelogram model might include the following: (1) by cutting offthe (right) triangular end of the parallelogram and moving it to the other end, the parallelogram can be made into a rectangle, (2) the area of the transformed parallelogram has not been changed by step 1, and (3) the area of the resulting rectangle is known to be

$$
\text { Area } = \text { base } \times \text { height }.
$$

Alternatively, for the Darwin example, deep explanatory arguments might include the following: (1) geologically and ecologically, the earth changes over time (due to earthquakes, volcanoes, etc.), (2) variations in a species might make some individuals of that species better able to survive and produce more offspring like themselves in the "new" environment, (3) over the passage oftime, the less-well-adapted are slowly weeded out as they die before producing any (or as many) offspring, and (4) as ecological/geological conditions change slowly over time, the species would change and adapt slowly in concert, owing to an accumulation of adaptations through multiple generations.

The advantages of deep explanatory arguments include their power of abstraction, generalization, and insight generation, resulting from the application of basic principles and relations to current analyses. Whereas simple explanatory arguments may possibly lead to insight and understanding on the part of the decision maker, valid deep explanatory arguments may have a much higher probability of success. The basic disadvantage of deep explanatory arguments is the difficulty of defining, storing and retrieving relevant basic principles, relating these basic principles to the model, and successfully communicating the relationships to the decision maker/user.

## A Framework for Enhancing Understanding via Model Analysis

THE IMPLICATIONS OF PERKINS'S THEORY, WHICH EMPHASIZES PURPOSE, design, and arguments, provide a framework for a new evolution of model analysis systems, termed Understanding via Model Analysis Systems (or UMAS) in the taxonomy of figure I.

The primary purpose of the UMAS class of analysis systems is to enhance the decision maker's insightful understanding of the complex business environment, represented in a DSS. Insightful understanding is defined in the cognitive science literature as the holistic perception of the essential relationships of the problem, frequently involving the combination and restructuring of previously learned facts or responses into new and novel patterns or combinations of patterns [26, 39, 40, 46, 47). Insight is usually contrasted with trial-and-error learning [75] and means-end analysis [53] as a cognitive process used in complex problem solving and learning. Experimentation has provided evidence that insightful understanding is a distinct, empirically measurable psychological phenomenon applicable to complex problem solving (see the appendix for a brief summary of Metcalf s research in this area and for several insightful and not-insightful problems used in her research [48,49,50».

We assume in the following discussion that the decision maker uses the analysis of mUltiple what-if cases in a DSS environment to explore the thing he or she is trying to understand: for example, to determine the key factors of a model and explore potential relationships between those key factors and the business decisions under consideration.

Matching the purpose, design, and arguments of Perkins's theory, the five components of the UMAS framework include purpose administration, design generation, evaluative argument generation, simple explanatory argument generation, and deep explanatory argument generation. Each component of the framework is discussed individually below, along with the artificial intelligence/information system technologies that are potentially applicable to each.

## Purpose Administration

Purpose administration consists of soliciting a purpose from the decision maker, interpreting the response, and storing it for future use. Such future use may include using the purpose to recall arguments and solutions when trying to solve similar problems. A problem's purpose evokes the memory of the associated design and arguments; in this way, understanding improves recall, and vice versa.

Purpose administration also includes soliciting, from the decision maker, appropriate key words and phrases, basic principles, and underlying concepts that may be relevant to the purpose. The purpose administration component then links this information to the analysis, making key words available for use in simple explanatory arguments, and flagging the appropriate principles and concepts for potential use in deep explanatory arguments.

Artificial intelligence/information system (AllIS) technologies applicable to purpose administration include a knowledge base for accessing and storing basic concepts and principles, a natural language interpreter and parser for interpreting the purpose, search algorithms for finding specified concepts and prinCIples already stored, links with the MMS model definition language, and case-based reasoning [25,41,67] and/or analogical reasoning [10, 11] for storing and retrieving concepts and principles.

## Design Generation

Perkins's theory requires one or more designs (i.e., models) of the thing to be understood. Such models might include the original model, alternative initial models, the simplified metamodels generated as outputs of the inductive model analysis systems discussed above, relations specified by the decision maker, based on human expertise, and/or new models generated from UMAS-applied technologies. Multiple metamodels and relations can be generated from inductive model analysis systems in several ways: (1) by using multiple technologies (e.g., neural networks [80], GMDH [15,60,68,69], statistics [20, 35, 36], genetic algorithms [19, 33], to analyze the same set of model instances), (2) by varying the sequence or contents of the set of model instances used as input to these inductive technologies, (3) by modifying technologyspecific parameters, and/or (4) by changing search criteria and varying the modIfications in analogical reasoning analyses [25,41]. Note that Perkins's theory, through the use of evaluative arguments (see below), provides for the elimination of inapplicable and relatively inferior models, resulting from inappropriate technologies, insufficient data, unrelated model instances used as input, and/or designs that are not generalizable (due perhaps to overlearning). That is, some inferior models may be eliminated via evaluative arguments that compare the strengths and weaknesses of multiple models, other inferior models may be eliminated due to lack of internal consistency, necessity, and sufficiency requirements. Still other inferior models may be eliminated due to lack of support of the purpose or by generating obviously false generalizations and/or explanatory arguments. And finally, inferior models may be eliminated due to links with irrelevant underlying principles during the generation of deep explanatory arguments. Further, since evaluative/simple/deep arguments are applied in every analysis process, there is little penalty for initially generating too many metamodels or executing multiple technologies to produce different metamodels.

In addition to the technologies mentioned above, other (AllIS) technologies applicable to design generation include 103 [61,62] for inductively generating discrimination networks (structures related to decision trees), AQl5 [51] for generating a set of production rules, INLEN's TreeCon [30] for generating decision trees, and computerintensive statistical methodologies to assess the comparative quality of multidimensional recommendations provided by the different designs or models using small sample sizes [56]. Intelligent databases (perhaps object-oriented database management systems) can also be employed in the storage, retrieval, and management of the instances, analysis technologies, metamodels, knowledge bases, and approved arguments [72].

## Evaluative Argument Generation

Evaluative arguments compare different models or metamodels to determine the strengths and weaknesses of each, and evaluate the necessity, sufficiency, and consistency requirements of a single model and its components. In comparing different models, the UMAS can rely on internal evaluation measures, such as the accuracy of a model over some set of instances, model complexity (with respect to the number of terms, degrees of polynomial terms, etc.), or some combination of both [2]. The UMAS can also include the capability to query the decision maker for other measures of comparison, along with their definitions and relative evaluation weights. Efficiency frontiers can be incorporated to evaluate different models based on multiple criteria [82]. In addition, the UMAS can utilize various technologies to help the decision maker rank order the models with respect to multiple criteria.

The UMAS also includes a hypothesis-testing capability for all potential models. This provides the ability to evaluate potential models based on (a) rules presented to, and validated by, the decision maker, (b) internally generated validity checks based on the substitution of extreme parameter values into the model to see if reasonable/feasible results occur, and (c) substitution of multiple values of nonkey parameters into the original model to verifY that the solution does not change significantly [55].

In evaluating the sufficiency and necessity ofa specific model and its components, the UMAS can use any of a variety of specific measures that capture the explanatory power of the model. For example, the coefficient of determination, $R ^ { 2 } { \mathrm { ~ } }$ , provides a measure of sufficiency for an inductive model that supposedly explains the variations in output due to changes in input parameters. Likewise, the necessity requirement of model components can be measured by Wagner's all-save-one $R ^ { 2 } .$ -based measure [76, p. 952], which employs conditional expectations and classic probability theory to determine whether one specific model term has a large influence on the variation in the model as a whole, relative to the other model terms.

In evaluating the consistency of a metamodel and its component terms, dimensional analysis should be included for all mathematical expressions in a model, as suggested by several researchers [59, 73, 74]. Bhargava reduces the dimensional consistency problem to numeric arithmetic by a "suitable encoding of fundamental units as primes," deriving units as products of these primes [5].

In general, AI/IS technologies that are potentially applicable to evaluative argument generation include inductive expert systems, the analytic hierarchy process [64], and statistics, in addition to the technologies mentioned above.

## Simple Explanatory Argument Generation

Perkins's theory also requires the generation of simple explanatory arguments that support or refute the ability ofthe design (model) to support the purpose. This implies that the UMAS must generate such arguments, based on its interpretation of the model, and present such arguments to the decision maker for verification.

Explanatory arguments can be in the form of multiple, natural-language production rules as recommended by Parsaye et al. [57]. They can also include key words and key phrases, such as "directly proportional," "inversely proportional," and the like. Alternatively, they can take the form of a base case and examples generated to demonstrate the response of the model to changes (both large and small) in input parameter values.

In general, the AllIS technologies that are applicable to generating simple explanatory arguments include expert systems, explanation-based learning [52], access to and use ofthe model management system's model definition language, multiple links with the IMAS and DMAS, and the ability within the UMAS to intelligently select a base case and generate appropriate model instances. Note that the MMS model definition language is similar in function to a database management system's data definition language and contains, for each variable and parameter, a natural-language definition, statement of units, and range of legitimate values [12].

## Deep Explanatory Argument Generation

Deep explanatory arguments seek to explain a design or model in terms of basic underlying principles. These arguments require links between the UMAS and those underlying principles relevant to the modeled environment: for example, the formulas behind balance sheets, income statements and funds flows statement for financial models or the principles of queues, self-service versus full service, and the use of money to facilitate trade for certain operational models. The principles can contain natural-language explanations in terms of the parameters defined and understood by the UMAS. They can also contain key terms, key relationships, and common synonyms so that they can be used to form links with other models.

AllIS technologies applicable to deep explanatory argument generation include expert systems for forming natural-language arguments, a knowledge base for storing fundamental principles, case-based reasoning [25,41,67] and/or analogical reasoning [10, II] for retrieving appropriate fundamental principles, and links with the MMS model definition language.

## Sample Application ofUMAS

As an example of an application of Perkins's theory to a business problem, assume a decision maker is working on a warehouse location problem consisting of a new market area that includes thirteen cities, all located in central Texas, with a source of supply in Los Angeles. Also, assume that she wants to determine the impacts on the optimal number of required warehouses caused by changes in four uncertain factors: (I) the fixed building cost $, f ,$ of each warehouse (assumed to be equal at all potential warehouse locations), (2) the forecasted demand, d, at each city within the market area (assumed to be the same at each city), (3) the transportation costs, I, from the warehouse to each demand city (assumed to be a function of both the transportation mode and distance), and (4) the factory-to-warehouse transportation costs, T.

To address this problem, our decision maker constructs a warehouse location model in the form of a mixed integerllinear programming model [16]. After validating the model, she runs several (perhaps twenty) what-if cases, varying one or more of the four parameters $( f , d , t ,$ and 1) over ranges of reasonable values. She then analyzes the results of these cases with the aid of the inductive model analysis system, INSIGHT [68,69], which generates a relationship between changes in the four parameters and their effects on the optimal number of warehouses. Such an analysis reveals that only three of the four possible parameters affect the solution, and that the appropriate relation is

$$
n = k ^ {*} (d ^ {*} t / f).\tag{1}
$$

where n is the optimal number of warehouses and k is a constant. A second model, proposed by a consultant and generated by mathematical manipulation and simplification of the integer/linear programming model is given by [16]

$$
n = k ^ {*} (d ^ {*} t / f) ^ {2 / 3}.\tag{2}
$$

A third model, generated by the GMDH-based algorithm of AIM [I, 27] using the same set of twenty solved model instances as above, is given by:

$$
\begin{array}{l} n = 6. 1 2 + 3. 3 7 \left\{5. 1 8 + 5. 7 1 (- 1. 1 4 + 0. 3 5 6 d) \right. \\ + 5. 1 4 (- 1. 1 3 + 0. 2 7 4 t) + 8. 6 8 (- 0. 7 8 1 + 0. 2 6 7 f ^ {- 1}) \\ - 0. 7 1 9 (- 1. 1 3 + 0. 2 7 4 t) ^ {2} \\ + 4. 8 7 (- 1. 1 4 + 0. 3 5 6 d) * (- 1. 1 3 + 0. 2 7 4 t) \\ + 7. 6 1 (- 1. 1 4 + 0. 3 5 6 d) * (- 0. 7 8 1 + 0. 2 6 7 f ^ {- 1}) \\ + 0. 6 9 9 (- 1. 1 3 + 0. 2 7 4 t) * (- 0. 7 8 1 + 0. 2 6 7 f ^ {- 1}) \\ + 5. 2 5 (- 1. 1 4 + 0. 3 5 6 d) * (- 1. 1 3 + 0. 2 7 4 t) * (- 0. 7 8 1 + 0. 2 6 7 f ^ {- 1}) \\ + 0. 3 4 1 (- 1. 1 3 + 0. 2 7 4 t) ^ {2} + 0. 0 7 8 7 (- 0. 7 8 1 + 0. 2 6 7 f ^ {- 1}) ^ {3} \}. \end{array}\tag{3}
$$

A fourth model, proposed, say, by an analyst, is given by

$$
n = t / f.\tag{4}
$$

In this example, Perkins would state that the purpose of the model is to help understand how changes in building cost, transportation costs (both factory-to-warehouse and warehouse-to-city), and demand affect the optimal number of warehouses. The design of the knowledge is given by any of the above models.

Evaluative arguments, testing the accuracy, consistency, simplicity, necessity, sufficiency, and consistency of the four models (equations 1-4), might include the following: (I) the fourth model is inferior due to (a) inaccuracy (as measured by its limited explanatory power, R2, over the set of twenty solved model instances), and $R ^ { 2 }$ (b) dimensional inconsistency (i.e., the left and right sides of the equation do not reduce to the same units); (2) the third model is inferior since (a) it contains terms that fail the necessity test (i.e., that do not significantly increase the explanatory power of the model) and (b) it is more complex than the first two models (with respect to the number and degree of its terms) without significant increases in explanatory power; (3) the second model is inferior to the first model, since it has approximately the same explanatory power but is more complex (due to the basic term being raised to the 2/3 power); and (4) the first model is accurate (explaining 92 percent of the variations from the average of the twenty solved instances), consistent (the right-hand side reduces to a unitless quantity to match the left-hand side), and includes only terms that are necessary (omitting one or more variables significantly reduces the accuracy of the model). Thus, the first model is superior to the other three.

Simple and deep explanatory arguments about why the first model serves the purpose (based primarily on the model's knowledge base, the MMS' s model definition language and relationships inherent in balance sheets, income statements, and funds flow statements) include first, that significant increases in transportation costs and/or demand tend to cause an increase in the best number of warehouses since extremely high transportation costs or huge demands in every city would justify building a warehouse in each and every city, thereby reducing variable costs--that is, the higher fixed costs of investment expense, interest, and depreciation associated with buIlding thirteen warehouses would be more than offset by the lower variable costs associated with transportation, leading to greater overall profitability. Second, significant increases in the warehouse building costs tend to decrease the desired number of warehouses, since extremely high warehouse construction costs would dictate building a single, centrally located warehouse to conserve capital budgets and limit interest and depreciation expenses. Third, changes in transportation costs or demand tend to offset similar changes in building costs--that is, there is a tradeoff between building costs and the other factors in their effect on the number of warehouses. Fourth, the constant, k, provides an overall indication of the amount of change in $d , t ,$ andfrequired to cause a change in the integer number of warehouses--that is, k provides an indication of the sensitivity, or robustness, of the best number of warehouses, $^ { n , }$ automatically taking into consideration the units in which $d ,$ t, and $f$ are measured. Fifth, and last, other factors, such as factory-to-warehouse transportation costs, either have an insignificant impact on the number of warehouses or are basically constant in the real-world environment.

## Conclusions and Research Directions

IT HAS BEEN STATED THAT THE PURPOSE OF MODELING is insight, not numbers [16]. Given that modeling is the central component of every DSS [71], and that insight is a special type of (holistic) understanding [46,47], it follows that the purpose of DSS is understanding: specifically, understanding by the decision maker of the business environment depicted in the DSS. We have suggested that one source of such understanding is the analysis of one or more model instances using deductive or inductive logic, or both. But the theory of understanding [58] states that models and logic alone are insufficient to promote understanding. Also required are various types of arguments (evaluative, simple explanatory, and deep explanatory arguments) that show how the model and model instances support the purpose----that is, how they enhance the decision maker's understanding. This paper has applied Perkins's theory of understanding to DSS analysis to develop a framework for the next evolution of model analysis systems.

In the DSS literature, especially the management science aspects of it, the focus of research has historically been on model specification and model solution. It is time now to give the analysis of solutions the importance it deserves. An early effort in this regard has been to articulate the tasks of model analysis. Several DSS researchers [9] have developed some theory in this vein, but the area still needs further refinement. Specifically, we need to identify a "minimal spanning set" of tasks that leads to successful model analysis, and to validate these through experimentation.

Another research area could explore and evaluate technologies that are potentially applicable to analysis and understanding. Initial evaluation could match the input, processing, output, and feedback characteristics of these technologies against the corresponding requirements of the prime analysis tasks mentioned above. The results would provide a research agenda for the application of the technologies to the analysis tasks, along with empirical testing of their effectiveness.

A third research area would develop an intelligent database environment to enhance the analysis of solved model instances and provide the management of technology in model analysis. That is, this research thrust could develop, as an extension of the model management system of a DSS, a model instance management system that provides the user with an easy-to-use, computer-based platform that enhances the decision maker's ability to apply artificial intelligence and information technologies to the analysis of multiple solved model instances [72].

A final research area would include applying and testing the concepts proposed in this paper on a set of actual test cases, such as those discussed in [18, 34, 33].

Acknowledgment: The author would like to thank two anonymous referees for their excellent comments, all of which significantly improved the paper.

## REFERENCES

I. Abductory Inductive Models-User 's Manual. Charlottesville, VA: Ab-Tech, 1990.

2. Barron, R.L. Predicted square error: a criterion for automatic model selection. In 1. Farlow (ed.), Self-Organizing Methods in Modeling: GMDH Type Algorithms. New York: Marcel Dekker, 1984, pp. 25--66.

3. Bettonvil, B. Detection of Important Factors by Sequential Bifurcation. Tilburg, Neth-

erlands: Tilburg University Press, 1990.

4. Bettonvil, B., and Kleijnen, J.P.c. Identifying the important factors in simulation models with many factors. Working paper, Department ofiS and Center, Tilburg University, Tilburg, Netherlands, 1994.

5. Bhargava, H.K. Dimensional analysis in mathematical modeling systems: a simple numerical method. ORSA Journal on Computing, 5, I (Winter 1993), 33-39.

6. Boland, R.J., Jr., and Day, W. The process of system design: a phenomenological approach. Proceedings of the Third International Conference on Information Systems, Ann Arbor, MI, December 1982, pp. 31-45.

7. Bonczek, R.H.; Holsapple, C.W.; and Whinston, A.B. Future directions for developing decision support systems. Decision Sciences, 11,4 (October 1980), 61 /Hi31.

8. Branley, B.; Fradin, R.; Kimbrough, S.O.; and Shafer, T. On heuristic mapping of decision surfaces for post-evaluation analysis. Proceedings of the Twenty-Ninth Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1977,416-425.

9. Brennan, 1.1., and Elam, 1. 1. Understanding and validating results in model-based decision support systems. Decision Support Systems, 2 (February 1986),49-54.

10. Burstein, M.H. Concept formation by incremental analogical reasoning and debugging. In R.S. Michalski, J. Carbonell, and T.M. Mitchell (eds.), Machine Learning: An <sub>Art\~ficial</sub> IntelligenceApproach, vol. 2. Los Altos, CA: Morgan Kaufmann, 1986, pp. 351-370.

II. Carbonell, 1. Deviational analogy: Ii theory of reconstructive problem solving and expertise acquisition. In R.S. Michalski, J. Carbonell, and T.M. Mitchell (eds.), Machine Learning: An ArtijiciallntelligenceApproach, vol. 2. Los Altos, CA: Morgan Kaufmann, 1986, pp. 351-370.

12. Dolk, D.R. A generalized model management system for mathematical programming. ACM Transactions on Mathematical Software, 12, 2 (June 1986),92-126.

13. Dunker, K. On problem solving. Psychological Monographs, 58,270 (1945).

14. EXECUCOM. Interactive Financial Planning System: User's Manual. Austin, TX: EXECUCOM, 1992.

15. Farlow, S.J. Se/fOrganizing Methods in Modeling: GMDH Type Algorithms. New York: Marcel Dekker, 1984.

16. Geoffrion, A.M. The purpose of mathematical programming is insight, not numbers. Interfaces, 7, 1 (January-February 1976),81-92.

17. Geoffrion, A.M. An introduction to structured modeling. Management Science, 33, 5 (May 1987),547-588.

18. Geoffrion, A.M., and Nauss, R. Parametric and postoptimality analysis in integer linear programming. Management Science, 23, 5 (May 1977),453-466.

19. Golberg, D.E. Genetic Algorithms in Search Optimization and Machine Learning. Reading, MA: Addison-Wesley, 1991.

20. Green, G.H. Quantitative Discovery: Using dependencies to discover nonlinear terms. Master's thesis, University of Illinois at Urbana, Champaign, 1988.

21. Greenberg, H.J. A tutorial on computer-assisted analysis. In H.J. Greenberg, F.H. Murphy, and S.H. Shaw (eds.), Advanced Techniques in the Practice of Operations Research. New York: Elsevier Science Publishing, 1982, pp. 212-249.

22. Greenberg, H.J. A Computer-Assisted Analysis System for Mathematical Programming Models and Solutions: A User's Guide for ANALYZE. Boston: Kluwer, 1993a.

23. Greenberg, H.J. Enhancements of ANALYZE: a computer-assisted analysis system for linear programming. ACM Transactions on Mathematical Software, 19, 2 (June I 993b), 223-256.

24. Greenberg, H.J. Syntax-directed report writing in linear programming using ANAL YZE. European Journal of Operational Research, 72,2 (January 27, 1994),300-311.

25. Hammond, K.F. Case-based planning. Proceedings of a Workshop on Case-based Reasoning, May 10-13, 1988, pp. 17-20.

26. Hilgard, E.R. Theories of Learning, 2d ed. New York: Appleton-Century-Crofts, 1956.

27. Ivakhnenko, G.G. Polynomial theory of complex systems. IEEE Transactions on Systems, Man and Cybernetics, 4, 3 (March 1971),364-384.

28. Jones, C.V. User interfaces. In E.G. Coffman, J.K. Lenstra, and A.Y. Kan (eds.),

Handbooks of Operations Research and Management Science, vol. 3. Amsterdam: North Holland/Elsevier, 1992, pp. 603--668.

29. Kasper, G. M. A theory of decision support system design for user calibration. Information Systems Research, 7,2 (June 1996),215-232.

30. Kaufman, K.A.; Michalski, R.S.; and Kershberg, L. Mining for knowledge in databases; goals and general description of the INLEN system. In G. Piatetsky-Shapiro and W. Frawley (eds.), Knowledge Discovery in Databases. Menlo Park, CA: AAAI Press/MIT Press, 1991, pp. 449-462.

31. Kimbrough, S.O.; Moore, S.A.; Pritchett, e.W.; and Sherman, C.A. On DSS support for candle-lighting analysis. Transactions of DS\~92 (1992), 118-135.

32. Kimbrough, S.O.; Oliver, 1.R.; and Pritchett, e.W. On post-evaluation analysis: candlelighting and surrogate models. Interfaces, 23, 3 (May-June 1993), 17-28.

33. Kimbrough, S.O., and Oliver, J.R. On automating candle-lighting analysis: insight from search with genetic algorithms and approximate models. Proceedings of the Twenty-seventh Annual Hawaii International Conference on System Sciences, 1994, pp. 536-544.

34. Kimbrough, S.O.; Pritchett, C.W.; Bieber, M.P.; and Bhargava, H.K. The Coast Guard's KSS project. Interfaces. 20,6 (November-December 1990),5--16.

35. Kleijnen, J.P.e. Sensitivity analysis and optimization of simulation models. Working paper, Center and Department of I.S., Tilburg University, Tilburg, Netherlands, 1994.

36. Kleijnen, 1.P.e. Statistical Toolsfor Simulation Practitioners. New York: Marcel Dekker, 1987.

37. Klingman, D.; Phillips, N.; Steiger, D.; Wirth, R.; Padman, R.; and Krishnan, R. An optimization based integrated short-term refined petroleum product planning system. Management Science, 33, 7 (July 1987), 81 \~30.

38. Klingman, D.; Phillips, N.; Steiger, D.; and Young, R. The successful deployment of management science throughout Citgo Petroleum Corporation. Interfaces. 17, I (January-February 1987), \~25.

39. Kohler, W. The Mentality of Apes, trans. by E. Winter. New York: Harcourt, Brace, 1925.

40. Kohler, W. The Task of Gestalt Psychology. Princeton, NJ: Princeton University Press, 1969.

4 \. Kolodner, J.L. Extended problem solver capabilities through case-based inference. Proceedings of a Workshop on Case-Based Reasoning. May 10-13, 1988, pp. 21-30.

42. Kosy, D.W., and Wise, B.P. Self-explanatory financial planning models. Proceedings of the National Conference of Artificial Intelligence, August 1984, pp. 176-181.

43. Kosy, D.W., and Wise, B.P. Overview of Rome: a reason-oriented modeling environment. In L.F. Psu (ed.), ArtifiCial Intelligence in Economics and Management. Amsterdam: North-Holland, Elsevier Science Publishers, 1986, pp. 21-30.

44. Krishnan, R. Model management: survey, future research directions and a bibliography. ORSA CSTS Newsletter. 14, I (Spring 1993), 1-22.

46. Lee, D.L. Perception, intuition and insight. In W.R. Niblett (ed.), How and Why Do We Learn. London: Faber and Faber, 1965.

47. Logan, F.A., and Ferraro, D.P. Systematic Analyses of Learning and Motivation. New York: John Wiley and Sons, 1978.

48. Metcalf, 1. Premonitions of insight predict impending error. Journal of Experimental Psychology: Learning. Memory and Cognition, 12,4 (October 1986),623--634.

49. Metcalf, J. Feeling of knowing in memory and problem solving. Journal of Experimental Psychology: Learning. Memory and Cognition, J 2,2 (April 1986),288-294.

50. Metcalf, 1., and Wiebe, D. Intuition in insight and non insight problem solving. Memory and Cognition, 15, 3 (May 1987), 238-246.

51. Michalski, R.S., and Stepp, R. Revealing conceptual structure in data by inductive learning. Machine Intelligence, 10 (1982), 173-196.

52. Mitchell, T.M.; Keller, R.M.; and Kedar-Cabelli, S.T. Explanation-based generalization: a unifying view. Machine Learning, I, 1 (January 1986),47-80.

53. Newell, A., and Simon, H.A. Human Problem Solving. Englewood Cliffs, NJ: Prentice-Hall, 1972.

54. Newton, N. Foundations of Understanding. Amsterdam: John Benjamin Publishing, 1996.

55. Nickerson, R.S.; Perkins, D.N.; and Smith, E.E. The Teaching of Thinking. Hillsdale, NJ: Lawrence Er1baum Associates, 1985.

56. O'Leary, D.E. Measuring the quality of computer model performance. European Journal of Operational Research, 56, 3 (February 10, 1992), 319-331.

57. Pars aye, K.; Chignell, M.; Khoshafian, S.; and Wong, H. Intelligent databases. AI Expert (March 1990),3&--47.

58. Perkins, D.B. Knowledge As Design. Hillsdale, NJ: Lawrence Er1baum Associates, 1986 59. Piela, P.C.; Epperly, T.; Westerberg, K.; and Westerberg, A. An object-oriented computer environment for modeling and analysis, part 1--the modeling language. Computers and Chemical Engineering, 15, 1 (January 1991),53-72.

60. Prager, M.H. Group method of data handling: a new method for stock identification. Transactions of the American Fishery Society, 117 (1988), 290-296.

61. Quinlan, J.R. Discovering rules from large collections of examples: a case study. In D. Michie (ed.), Expert Systems in the Micro Electronic Age. Edinburgh: Edinburgh University Press, 1979, pp. 168-201.

62. Quinlan, J.R. Learning efficient classification procedures and their application to chess end-games. In M.S. Michalski, J. Carbonell, and T.M. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach. Los Altos, CA: Morgan Kaufmann, 1983, pp. 463-482.

63. Reddy, Y.Y. The role ofintrospective simulation in managerial decision making. DSS-85 Transactions, IADSS. Austin, TX: University of Texas, 1985, pp. 18-32.

64. Saaty, T.S. Decision Making: The Analytical Hierarchical Process. Pittsburgh, PA: University of Pittsburgh Press, 1988.

65. Salte IIi , A., and Homma, T. Sensitivity analysis for model output. Computational Statistics and Data Analysis, 13, 1 (January 1992),73-94.

66. Saltelli, A., and Marivoet, J. Non-parametric statistics in sensitivity analysis for model output: a comparison of selected techniques. Reliability Engineering and Systems Safety, 28, 4 (April 1990),229-253.

67. Schank, R., and Reisbeck, C. Inside Case-Based Reasoning. Hillsdale, NJ: Lawrence Erlbaum Associates, 1989.

68. Sharda, R., and Steiger, D.M. Using artificial intelligence to enhance model analysis. In S.G. Nash and A. Sofer (eds.), The Impact of Emerging Technologies on Computer Science and Operations Research. Boston: Kluwer, 1995, pp. 263-280.

69. Sharda, R., and Steiger, D.M. Inductive model analysis systems: enhancing model analysis in decision support systems. Information Systems Research, 7, 3 (September 1996), 328-341.

70. Simon, H.A., and Newell, A. Human problem solving: the state of the theory in 1970. American Psychologist, 26, 2 (February 1971), 145-159.

71. Sprague, R.H., Jr., and Carlson, E.D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall, 1982.

72. Steiger, D.M. Model instance management systems: an extension of MMS/DSS for the intelligent management and analysis of mUltiple model instances. Working paper no. ISOM960502, University of North Carolina, Greensboro, 1996.

73. Stephanopoulos, G.; Henning, G.; and Leone, H. MODEL.LA. a modeling language for process engineering-I: the formal framework. Computers and Chemical Engineering, 14,8 (August 1990), 813-846.

74. Stephanopoulos, G.; Henning, G.; and Leone, H. MODEL.LA. a modeling language for process engineering-II: multifaceted modeling of processing systems. Computers and Chemical Engineering, 14, 8 (August 1990), 847\~69.

75. Thorndike, E.L. Animal Intelligence: An Experimental Study of the Associative Processes in Animals. New York: Macmillan, 1898.

76. Wagner, H.M. Global sensitivity analysis. Operations Research, 43, 6 (November-December 1995), 948-969.

77. Walls, J.G.; Widmeyer, G.R.; and El Sawy, O.A. Building an information system design theory for vigilant EIS. Information Systems Research, 3, 1 (March 1992),36-59.

78. Webster's New Collegiate Dictionary. Springfield, MA: Merriam, 1961.

79. Wertheimer, M. Productive Thinking, rev. ed. New York: Harper and Row, 1959.

80. Weiss, S.M., and Kulikowski, C.A. Computer Systems That Learn. San Mateo, CA: Morgan Kaufman Publishers, 1991.

81. Wise, B.P., and Kosy, D.W. Model-based evaluation oflong-range resource allocation plans. In L.F. Pau (ed.), Artijiciallntelligence in Economics and Management. Amsterdam: North-Holland, Elsevier Science Publishers, 1986, pp. 9\~102.

82. Zeleny, M. Multiple Criteria Decision Making. New York: McGraw-Hill, 1982.

## ApPENDIX: Experimentation in Insightful Understanding

EXPERIMENTATION HAS PROVIDED EVIDENCE THAT INSIGHTFUL UNDERSTANDING is a distinct, empirically measurable psychological phenomenon applicable to complex problem solving. Specifically, Simon and Newell [53, 70] proposed that people are able to solve complex, analytical problems by using means-end analysis; i.e., they compare the current state to a specified goal state and, if a move makes the current state more like that goal state, that move is taken. This suggests that the problem solver gets progressively and incrementally closer to the solution until slhe finally solves the problem. Further, the problem solver can provide estimates of goal proximity, estimates that are measurable in terms ofa "feeling of warmth." However, Metcalfe [48, 49, 50] hypothesized that some problems (specifically, those requiring insightful analysis) are solved by nonanalytical, nonsequential processes.

Metcalfe hypothesized that the "warmth" pattern expressed by the problem solver would be significantly different for insightful understanding; i.e., that the subjects would rate themselves as "cold" up until they suddenly solved the problem, at which time their warmth rating would jump from very cold to maximal warmth.

In her experiments, Metcalfe used algebraic word problems similar to the following as examples of problems that produced incrementally increasing (i.e., noninsightful) "feelings of warmth" over time:

1. Given containers of 163, 14, 25 and II ounces, and a source of unlimited water, show how you could obtain exactly 77 ounces of water.

2. Three people playa game in which one person loses and two people win each round. The one who loses must double the amount of money that each of the other two players has at that time. The three players agree to play three games. At the end of the three games, each player has lost one game and each person has \$8. What was the original stake of each player?

Examples of insight problems that required insightful understanding and produced sudden jumps (i.e., step functions) of "warmth" included the following:

3. A landscape gardener is given instructions to plant 4 special trees so that each one is exactly the same distance from each of the others. How is he able to do it?

4. Show how you can arrange I 0 pennies so that you have 5 rows (lines) of 4 pennies in each row.

Metcalfe used think aloud protocol experiments to verify that in some problems (i .e., problems 3 and 4 above), insightful understanding is a distinct and measurable phenomenon. She concluded that the empirical findings "indicate in a straight -forward manner that insight problems are, at least subjectively, solved by a sudden flash of illumination; [whereas] non-insight problems are solved more incrementally" [50, p. 243].
