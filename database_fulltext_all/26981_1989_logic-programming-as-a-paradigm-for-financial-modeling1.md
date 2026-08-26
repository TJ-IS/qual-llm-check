---
otero_id: 26981
otero_key: "9H5GSZ23"
title: "Logic Programming as a Paradigm for Financial Modeling1"
authors: "Robert P. Minch"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248702"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Logic Programming as a Paradigm for Financial Modeling
Author(s): Robert P. Minch
Source: MIS Quarterly, Vol. 13, No. 1 (Mar., 1989), pp. 65-84
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248702

Accessed: 24/06/2014 19:37

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Logic Programming as a Paradigm for Financial Modeling $^{1}$

By: Robert P. Minch
Department of Computer Systems and Decision Sciences
College of Business
Boise State University
Boise, ID 83725

## Abstract

Logic programming is investigated as a vehicle for structuring and implementing decision support systems, with particular attention paid to those dealing with financial modeling. This approach to model building, analyzing, and interfacing is compared to currently popular paradigms such as spreadsheet systems and financial modeling languages. The logic programming approach is shown to subsume these in expressive power and permit the incorporation of important capabilities not currently available. Examples operationalizing some of the concepts using the logic programming language Prolog are given.

Keywords: Decision support systems, financial modeling, financial planning systems, logic programming, Prolog

ACM Categories: F.4.1, H.4.2, I.2.4, J.1

## Introduction

The computer is becoming essential as a tool that facilitates the development and use of financial planning models for many organizations. From relatively humble beginnings, software systems supporting financial modeling have grown to support corporate-wide budgeting, planning, and analysis in the role of decision support systems (DSS) (Bonczek, et al., 1981). Approximately 85 percent of surveyed firms use some type of financial model (Wilkinson, 1984). The first section of this article considers the current state of financial modeling systems, their limitations, and the desirable goals of such systems.

## Overview of Computer-Assisted Financial Modeling

paradigms

Software supporting financial modeling has typically fallen into two main classes: (1) spreadsheet systems, often implemented on microcomputers and used for smaller applications; and (2) modeling languages, usually offering features tailored for specific kinds of problems and often used to represent very large models on mainframe computers. An example of the first type of software is the popular Lotus 1-2-3 spreadsheet system (Lotus, 1984); an example of the second is the Interactive Financial Planning System (IFPS) (Execucom, 1984). Both spreadsheet and modeling language systems are commonly implemented using third-generation programming languages; however, other approaches to financial modeling use less traditional vehicles such as APL (Appleyard and Hui, 1985) and microProlog (Kerschberg and Dickinson, 1985).

## Spreadsheet Systems

Spreadsheet systems may be described as restricted cases from a larger class of cellular automata having the following general features: (1) the spreadsheet consists of cells arranged in a two-dimensional, $^{2}$ rectangular configuration; (2) the “neighborhood” of each cell (the list of other cells that may affect the given cell) consists of the entire spreadsheet; (3) the number of states each cell can assume is infinite, usually consisting of "labels" (character strings), integer and floating point numbers within the range of the host computer, and perhaps logical (0-1) values; and (4) the system state is determined by sequentially evaluating each cell in the spreadsheet according to a specified order (usually based on cell dependencies). Because users of spreadsheet systems enter cell formulae in a definitional manner, spreadsheets are often perceived as being non-procedural even though the underlying system evaluates the spreadsheet in a procedural manner. The popularity of spreadsheet systems is due to their natural metaphor with paper worksheets and their ease of use when creating, evaluating, and modifying spreadsheets. Unfortunately, enhancements to commercially available spreadsheet modeling software have not addressed fundamental issues concerned with assisting model building and interpretation. Instead, they have focused on incremental enhancements related to model size, formatting, statistical analysis routines, etc. (Fordyce, 1987). Figure 1 shows a model specification and resultant model evaluation for a very simple spreadsheet. From this model it is easy to note that a critical method of knowledge representation is in terms of the absolute and relative positions of cells in the spreadsheet.

## Modeling Languages

Modeling languages differ from spreadsheet systems primarily because they employ a statement-based “modeling language” to specify how spreadsheet cell values are to be computed — however, their underlying structure usually remains constrained to the same two-dimensional arrangement of cells. Data are often aggregated either explicitly or implicitly by row or column, again representing knowledge by position in the spreadsheet. Commands are used to evaluate the modeling language statements and create a spreadsheet solution. A model specification and evaluation in a modeling language are shown in Figure 2.

The advantages of the modeling language approach include a natural language-like interface, convenient model documentation, and ease of use by non-programming managers. In addition to the basic spreadsheet capabilities, they may provide for model editing, storage, and retrieval, solution formatting and report writing, graphical display, model consolidation, separate data and command files, and a variety of financial and other special-purpose functions. For model analysis, modeling languages provide a number of additional features. The “what-if” capability allows the user to temporarily modify assumptions (independent variables) and examine the effect on other (dependent) model variables. A “goal-seeking” capability attempts to find values of independent variables that result in user-specified values of dependent variables. Sensitivity analysis provides a convenient mechanism for examining a number of systematic changes in model assumptions. Finally, Monte Carlo simulation may be used to compute summary statistics for output variables from a model with random inputs.

## Limitations of existing paradigms

While expedient and useful, current financial planning software suffers from several significant limitations, including the following:

One-to-one relationships of formulae-to-values. Compared to the most general alternative of many-to-many formulae-to-values, one-toone relationships impose two significant limitations. First, each formula must be evaluable to a single value, thus eliminating mathematical relations (e.g., square root) as well as many other multi-valued relationships such as fuzzy sets. Second, only one formula may be used to specify each resultant value. This restriction is arbitrarily imposed in many current systems because of unsophisticated procedural evaluation strategies that may be avoided when using logic programming. Multiple formulae for a particular result are desirable because each may vary in terms of inputs required, efficiency of operation, and confidence level for the codified relationships. Maintaining several alternative methods allows intelligent, run-time selection of the most feasible or appropriate formula.

<table><tr><td colspan="5">Specification</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>1 'SALES</td><td>+1000</td><td>+B1*1.1</td><td>+C1*1.1</td><td>+D1*1.1</td></tr><tr><td>2 'COST OF GOODS SOLD</td><td>+B1*.6</td><td>+C1*.6</td><td>+D1*.6</td><td>+E1*.6</td></tr><tr><td>3 'GROSS MARGIN</td><td>+B1-B2</td><td>+C1-C2</td><td>+D1-D2</td><td>+E1-E2</td></tr><tr><td colspan="5">Evaluation</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>1 SALES</td><td>1000</td><td>1100</td><td>1210</td><td>1331</td></tr><tr><td>2 COST OF GOODS SOLD</td><td>600</td><td>660</td><td>726</td><td>789.6</td></tr><tr><td>3 GROSS MARGIN</td><td>400</td><td>440</td><td>484</td><td>532.4</td></tr><tr><td colspan="5">10 COLUMNS 1-420 SALES = 1000, PREVIOUS SALES * 1.130 COST OF GOODS SOLD = 60% * SALES40 GROSS MARGIN = SALES - COST OF GOODS SOLD</td></tr><tr><td colspan="5">Evaluation</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>SALES</td><td>1000</td><td>1100</td><td>1210</td><td>1331</td></tr><tr><td>COST OF GOODS SOLD</td><td>600</td><td>660</td><td>726</td><td>798.6</td></tr><tr><td>GROSS MARGIN</td><td>400</td><td>440</td><td>484</td><td>532.4</td></tr></table>

Figure 1. Example Spreadsheet Model

Figure 2. Example Modeling Language Model

Tight coupling of data and knowledge to particular geometrical configurations. One problem related to this limitation is that the unwitting modification of a spreadsheet cell's contents may have numerous ramifications that are not easily traceable, due to other cells referencing its contents explicitly or implicitly by position. Correctness and auditability of models become difficult to ensure, and higher level data structures (such as hierarchical and network data models) cannot be supported in the two-dimensional spreadsheet. In addition, many systems require large amounts of computer memory because all calculated results are stored in memory.

Restriction to non-symbolic, arithmetic operations. Except for limited text processing, current financial planning systems deal exclusively with the manipulation of numerical quantities. This precludes the incorporation of large classes of valuable symbolic, semantic, and other qualitative relationships. Many such relationships (e.g., “X is owned by Y” and “A is less risky than B") are integral to the robust description of realistic financial situations.

Object-level model manipulation only. While some might argue that the use of macros (stored, recallable keystroke sequences), multiple-model consolidation, and other financial modeling software tools provide meta-level manipulation of models, they are essentially object-level utilities provided for user convenience. True meta-level model manipulation (e.g., where a meta-model manipulates the object-model to achieve higher objectives) would allow queries about the model itself (not related to a particular solution) such as: Is the model internally consistent? What variables depend on both X and Y? What is the longest chain of relationships between input and output variables? These meta-level queries are useful in verifying, validating, and auditing models during construction and use.

Restricted model query capabilities. In the spreadsheet approach, model querying consists of modifying cells that serve as inputs while observing the resultant changes in output cells. Modeling languages only provide slightly more flexibility by allowing user-defined reports and similar predefined outputs. Neither of the traditional approaches provides anything remotely as powerful as a generalized, ad hoc query capability for all model variables (such as would be expected of a database management system query language).

Little explanation of reasoning. A few spreadsheet systems provide the ability to investigate which cells affect or are affected by another cell. Similar capabilities are more common with modeling languages, but both methods provide only an indication of the static relationships present in the models. They do not explain in detail the process by which conclusions are reached, allowing the user to follow the reasoning step by step. The purposes of an explanation facility are to (Turban, 1988):

— make the system more intelligible to the user

— uncover shortcomings in the knowledge base and rules

— explain situations that were unanticipated by the user

— satisfy psychological and/or social needs

— clarify assumptions underlying the system's operations

— conduct sensitivity analyses that test the effects of change on the system

Mere exhaustive tracing of the procedural steps may be inadequate (Kidd and Cooper, 1985); ideally, explanations should be justified by basic principles and tailored to the user's abilities and needs (Hayes-Roth, et al., 1983). More detailed accounts of the general issues involved may be found in Goguen, et al. (1983) and Hassling, et al. (1984). Discussions of explanation facilities in the specific context of financial modeling systems are contained in King (undated) and Kosy and Wise (1984).

## Goals of financial modeling systems

A brief review of the financial modeling software's basic goals and functions might prove useful. These functions, as shown in Table 1, can be classified into three main areas: model building, model analysis, and model interfacing. A correspondence between these functions and the ways in which such software is used by managers has been established previously (Higgins and Opdebeeck, 1984; Naylor and Schuland, 1976). The financial modeling functions listed in Table 1 are consistent with component-oriented design recommendations for decision support systems such as the ROMC (representations, operations, memory aids, and control mechanisms) approach (Sprague and Carlson, 1982); the latter approach emphasizes technological components necessary to support the modeling functions. The following section describes how the logic programming paradigm for financial modeling (a combined function and component-oriented approach) addresses model building, analysis, and interfacing.

Table 1. Financial Modeling Software Functions

<table><tr><td>Function</td><td>Includes</td></tr><tr><td>Model building</td><td>StructuringEditingStoringRetrievingVerification</td></tr><tr><td>Model analysis</td><td>What-ifGoal seekingVariance analysisScenario generationRisk analysis</td></tr><tr><td>Model interfacing</td><td>Model-to-data interfaces:importing, maintaining,exporting, sorting,organizing, etc.Model-to-model interfaces:linkage, consolidation, etc.Model-to-user interfaces:report generation, graphics,user-defined commands,command files, scripts, etc.Domain-specific interfaces to special purpose functions, external software, etc.</td></tr></table>

## The Logic Programming Paradigm

In this section a logic programming paradigm for financial modeling is introduced. Each of the three main areas of financial modeling software functions (model building, analyzing, and interfacing) is addressed, and the potential contributions of the approach are shown to include mitigating the limitations associated with conventional systems and providing additional new capabilities. Comparisons are drawn between the existing systems and the proposed conceptual logic programming paradigm, eventually addressing each of the six previously identified limitations of the traditional approaches. Readers not familiar with logic programming and the Prolog language may wish to refer to the appendix for a brief overview.

## Model building

For completeness, this section begins the discussion of logic programming as a model building tool by reconsidering the simple spreadsheet and modeling language models presented in Figures 1 and 2. A logic program modeling the same basic relationships is shown in Figure 3. For this and subsequent examples, logic programming model examples will be shown in the Edinburgh dialect of the Prolog language (Clocksin and Mellish, 1981). In this model, sales for period one are given as a fact, while a recursive relationship defines sales for any future period based on the initial sales and the growth factor of 1.1. The cost of goods sold and gross margin rules relate their respective predicates to sales for any period, thus completing the specification of the simple model. While this article later discusses what can be done to insulate the user from the arcane Prolog grammar shown here, the example illustrates how a spreadsheet or modeling language model can also easily be represented using logic programming techniques. More importantly, there are many areas where the logic programming approach goes significantly beyond these basic capabilities. These areas are discussed in the next sections in three main categories: (1) syntactical features, (2) semantic features, and (3) meta-level features.

## Syntactical Features

The first limitation of traditional financial modeling software (one-to-one relationships of formulae-to-values) is eliminated in the logic programming approach because of its ability to capture many-to-many relationships of definitions to results. For instance, to incorporate many-to-one formulae-to-values in the example of Figure 3, gross margin might also be defined a second way — perhaps as follows:

```prolog
gross margin(Period,Amount) :-
    sales(Period,Sales__amount),
    Amount is Sales__amount * 0.4.
```

(a period's gross margin amount is computed by finding the period's sales and multiplying by .4)

Although this example of two gross margin definitions is trivial, it demonstrates a capability that is valuable in practice and in principle — the ability to include several methods in the same model defining how a desired result may be obtained. A practical advantage is seen even in this simple example, where the original defini-

<table><tr><td>sales(1,1000).</td><td>(sales in period 1 are 1000)</td></tr><tr><td>sales(Period,Amount) :-Previous__period is Period - 1,Previous__period &gt; 0,sales(Previous__period,Previous__ amount),Amount is Previous__amount * 1.1.</td><td>(sales in other periods are computed from previous periods greater than zero by finding the previous sales and multiplying by 1.1)</td></tr><tr><td>cost of goods sold(Period,Amount) :-sales(Period,Sales__amount),Amount is Sales__amount * 0.6.</td><td>(a period&#x27;s cost of goods sold is computed from sales by multiplying by 0.6)</td></tr><tr><td>gross margin(Period,Amount) :-sales(Period,Sales__amount),cost of goods sold(Period,COGS),Amount is Sales__amount - COGS.</td><td>(a period&#x27;s gross margin is computed by finding sales and cost of goods sold, then computing their difference)</td></tr><tr><td colspan="2">Using a default or user-defined output format, the display generated from this model could be shown like the output from either Figure 1 or Figure 2.</td></tr></table>

Notes: The is infix operator used above evaluates its second argument (an arithmetic expression) and instantiates its first argument to the result. It is used here for clarity and correspondence to the other example models. A much more powerful technique involves the use of “reversible” predicates such as $sum(X,Y,Z)$ where, in this case, if any two variables are instantiated, the third may be computed. The latter method is essential for maximum flexibility in both generating and testing model solutions, and for explaining the reasoning behind solutions.

The example program contains several constants imbedded in rules, whereas good programming practice would suggest storing at least some of these constants in separate facts such as growth factor(1.1).

Figure 3. Example Logic Programming Model in Prolog tion of gross margin requires cost of goods sold as an input, while the second definition above does not; thus the definition used may be chosen automatically based on the availability of input variables. More general interpretations of the principle imply that models may maintain multiple hypotheses about the world they represent, one or more of which may be applicable at a given time or under particular circumstances. The more unstructured the problem domain, the more likely multiple hypotheses would be necessary and useful.

In some cases where multiple methods apply, the system itself may determine which method is appropriate (e.g., if only one method succeeds given the current database or if all methods lead to the same result). If multiple solutions as well as multiple methods are available, this situation may often be regarded as positive, meaning there are several alternatives available to the decision maker. In other cases it may be desirable to ask the user via a simple menu, which method is most appropriate. Regardless, the overall model robustness is increased by having several available means for finding solutions. Note that in spreadsheet models it is impossible to have multiple definitions for any cell, and in modeling language systems an arbitrary conflict resolution scheme (such as accepting only the last definition for any cell) is normally employed.

In addition to the many-to-one example described previously, instances of one-to-many relationships between definitions and values can be modeled, such as mathematical equations with multiple roots. Full many-to-many relationships may be envisioned in models involving several alternative methods of accounting or financial analysis and complex mathematical relationships.

The second limitation of traditional systems (tight coupling of data and knowledge to particular geometrical configurations) is alleviated by another syntactic advantage of the logic programming approach. This advantage relates to the simple and robust way in which a logic programming model generates output values necessary to prove queries proposed by the user. There is no need for the user to be concerned with allocating space in a model for all possible ad hoc query results because it is not necessary to store the results in the model itself — only the facts and rules necessary to reconstruct the results. Thus, information may be represented implicitly by means of logical relationships as well as explicitly in the form of assertions (facts). For example, consider the following predicate, which can be used to generate a list of all variables affecting a given variable in a financial model:

$affects(V1,V2) :-$ used to compute(V1,V2).

(variable V1 affects variable V2 if V1 is used to compute V2)

affects(V1,V2) :-
used to compute(V1,V3),
affects(V3,V2).

(variable V1 affects variable V2 if V1 is used to compute a variable V3 and V3 affects V2)

Relationships of this form, often specified recursively, make it unnecessary to state explicitly (and hence store) a large number of elementary assertions. Logic programming facilitates the expression of virtual knowledge.

The computational completeness of logic programming (discussed in the appendix) ensures that all of the application-specific features of spreadsheet systems and modeling languages are possible using logic programming. For instance, formatted printing in spreadsheet form, special-purpose functions, user-defined macros and command files, etc. may be implemented in straightforward fashion. As one example, the positional knowledge imbedded in a familiar spreadsheet row and column display can be represented explicitly with predicates of the form:

spreadsheet(Row,Column,Value) : <conditions>.

for instance,

$$
\begin{array}{l} \text {spreadsheet(1,3,X): - } \\ \text {spreadsheet(1,1,Y),} \\ \text {spreadsheet(1,2,Z),} \\ \text {X is Y + Z.} \end{array}
$$

(the cell at row 1, column 3 is computed by finding the value of the cell at 1,1 and the cell at 1,2 and adding them together)

Of course, spreadsheets of higher dimensionality could also be simulated by merely increasing the number of terms in the spreadsheet predicate. This particular technique for emulating traditional spreadsheets is not proposed as desirable, however, because this would reintroduce an undesirable coupling of the modeled relationships with an arbitrary geometrical configuration. For example, the use of constant rather than variable terms in rules would jeopardize consistency under naive model editing. This would also imbed knowledge in the orderings of predicate terms, rather than in the predicates themselves and the values of their terms. Wherever possible, it is preferable to represent predication (meaning) in the form of predicates rather than predicate term orderings and values (Lee, 1984). It is then possible to separate the conceptual and semantic model properties from more temporal terms the predicates relate.

## Semantic Features

More important than the syntactic advantages of logic programming in planning situations is its ability to manipulate objects in terms that have semantic meaning to the user. Prolog interpreters, and logic programming languages generally, are symbol manipulation programs. There are other symbol manipulation languages (e.g., Lisp), but Prolog is designed in such a way that the manipulations performed on the symbols rigorously mirror the underlying semantics (intended interpretation) of the symbols. Meaning is conveyed through the user's interpretation of predicate names and terms, which forms the basis for natural, named relationships among terms. In the case of one-place predicates, the predicate name is usually associated with some property ascribed to its term, e.g., blue(sky). Predicates with arity (number of terms) two or greater are normally used to describe some relationship between the terms, e.g., larger(alaska,hawaii). $^{3}$ This lends itself to considerable flexibility in representing modeling knowledge and eliminates the third limitation associated with traditional systems (restriction to non-symbolic, arithmetic operations). For example, there may be occasion to define and use predicates such as the following:

turnover ratio(Company,high) :-
    business type(Company,manufacturing),
    net revenue(Company,Revenue\_amount),
    total assets(Company,Assets\_amount),
    Ratio is Revenue\_amount / Assets\_amount,
    Ration > 2.

acceptable for capital budgeting (payback\_method) :-
precision required(low),
decision objective(preliminary\_screening),
project risk(high),
planning horizon(short).

The semantic interpretation of logic programs allows qualitative knowledge as well as quantitative relationships to be captured. A common use of this facility is to classify objects into named categories that have meaning in a decision-making context such as "high" or "good." There is considerable support for the use of qualitative relationships in financial models. Linguistic variables and fuzzy production rules similar to those mentioned above have been previously incorporated in a knowledge-based DSS for financial ratio analysis (Ganoe, 1984) and several other systems (Whalen, et al., 1987). There is strong empirical evidence that financial diagnosticians translate quantitative inputs into qualitative variables (Bouwman, 1983). Additionally, enhancing existing systems such as IFPS with symbolic reasoning, rule-based knowledge, and logic has been advocated by research and development departments of major financial planning software vendors (King, undated).

## Meta-Level Features

Perhaps the most powerful but least often used feature of logic programming is the ability to construct meta-level models using the same built-in facilities available for object-level programs. The fourth limitation of traditional financial modeling software (object-level model manipulation only) may be removed through these powerful meta-level capabilities of logic programming, which relate primarily to manipulating the database of facts and rules to achieve higher-level goals. The essential advantage of meta-level financial model manipulation is the ability to query the model regarding its internal characteristics without invoking an object-level solution procedure. For instance, rather than changing the value of an input variable and re-solving the model to observe whether a particular output variable is related (an inadequate but often used technique), the model itself can be examined with a query to determine the exact relationship between the variables in question.

Other examples of meta-level modeling include the division of facts and rules into several classes according to their origin or purpose. For instance, object-level facts and rules could be classified by meta-level facts and rules according to how they apply to a specific corporate division, plant, or other level in a knowledge hierarchy. This is consistent with the view that the solution to many problems involves the application of generic, global, or reusable knowledge (e.g., public knowledge) coupled with domain-specific knowledge (e.g., private knowledge) (Hayes-Roth, et al., 1983). Meta-level rules can also classify object-level rules according to the seriousness of the issues they address, their past record of success, their execution speed, and their subjective confidence of rule correctness (Rowe, 1988). Separation of logical problem-solving levels into a planning level, a methods level, and a domain knowledge level has also been suggested (Sterling, 1984).

Another meta-logical technique used to augment logic programming models has been referred to as lemma generation (Clark and McCabe, 1982). In this process, certain critical facts are dynamically added to and deleted from the database during processing of queries. For instance, if many rules in a model were to require a calculation of net income, the first such rule invoked may simply “assert” the result as a new fact. The asserted facts can then be used in future queries to enhance the efficiency of problem processing. It is also possible to add, delete, and change (through deletion followed by adding a replacement) rules in a similar manner. For instance, if a set of rules is applicable only when net income is negative, a model that deduces a positive net income may (perhaps temporarily) eliminate the unnecessary rules from the model. Automatically adding or changing rules is, as intuitively suggested, a much more complex task than deleting them; but the task is sometimes appropriate when attempts are made to design adaptable heuristics. The capability of adding, changing, or deleting rules during model execution corresponds to run-time modification of program code — typically impossible with conventional programming languages.

Many enhancements and extensions to Prolog, at both object and meta level, have been suggested. For example, a simple extension of Prolog for generalized model management is discussed in Blanning (1984). Blanning shows that this extension provides relationally complete model management as measured by the operations of execution, optimization, and sensitivity analysis. This result is important because it demonstrates the generality of applications possible with a logic programming approach. Other suggested enhancements include augmenting Prolog's default backward-chaining control mechanism through the implementation (still within Prolog) of forward-chaining or hybrid control structures (Rowe, 1988). Meta-level analysis (as opposed to representation) of models is discussed at the end of the next section.

## Model analysis

The fifth limitation of traditional financial planning software (restricted query capability) is essentially eliminated through the logic programming approach. The query facilities of logic programming-based models fall into two main areas of capability: the ability to confirm a conjectured fact and the ability to generate facts (i.e., retrieve data that satisfies conditions). Answers to the first type of query are either “yes” or “no,” while answers to the second type of query may result in zero, one, or more instances of data retrieval. For example, to retrieve and verify the value of period 3 sales, the following queries might be issued (user input is underlined):

sales(3,Amount).

(what is the sales amount for period 3?)
Amount = 1210;

(after the first answer, the user types ;) no

(no more answers can be found)

sales(3,1210).

(verify that the period 3 sales amount is 1210)

yes

(the assertion is provable)

To retrieve gross margin for a range of years, these queries might be used:

member(Period,[1,2,3]), gross margin(Period, Amount).

Period = 1

Amount = 400;

Period = 2

Amount = 440;

Period = 3

Amount = 484;

no

As the last example shows, many solutions to a single query are possible (and may be desirable in many decision-making contexts).

The powerful nature of Prolog query processing is apparent in the way that what-if and goal-seeking model analyses are accomplished. By properly ordering the goals and choosing the appropriate constants and variables, the desired solutions can be found. For example, consider the following queries:

## sales(1,1250), gross margin(1,Amount). gross margin(1,500), sales(1,Amount).

These two queries are identical except for the ordering of goals and the choice of constant or variable terms. Given the example model's relationships, the first query is an example of what-if because it deduces conclusions from asserted conditions, while the second query is goalseeking because it attempts to prove asserted conclusions by locating the required conditions. This is an example where each individual predicate term can be used for either input or output, depending on whether the predicate is called with a constant or a variable in that term's position. Variously known as invertibility (Hogger, 1984), multiway reasoning (Rowe, 1988), relational programming (Clocksin and Mellish, 1981), and reversibility (Fordyce, 1987), this capability is considered a particularly powerful feature of Prolog. Since a relation, e.g., sales(a,b) can be interpreted as a function (fsales(a) = b), then the query sales(a,X) means find X in fsales(a)=X while the query sales(X,b) means find X in X=fsales $^{-1}$ (b).

Use of Prolog as a query language and database management system is discussed (along with several example systems) in Futo, et al. (1978). In this article, efficiency considerations (such as improving the default linear search of facts in a Prolog database) are addressed and several Prolog enhancements for database applications are noted. Refer to Lee (1985) for treatment of relationships between logic programming and relational data models, including entity-relationship interpretations. Other related work includes Jarke and Vassiliou (1984), Lee (1984), and Walker (1984).

The sixth limitation of traditional systems (little explanation of reasoning) can be eliminated by enhancing the basic inference engine capabilities with facilities for explaining the deductive reasoning performed. Techniques for implementing stepwise retrospective tracing of rules (considering successive ancestors of rules fired) in Prolog are discussed in Sterling and Shapiro (1986) and Walker (1984). A simple example dialog of this technique using the APES — Augmented Prolog for Expert Systems — (LPA, 1984b) system is shown in Figure 4.

```txt
gross margin(3,Amount).
    Amount=484 why
To deduce
    gross margin(3,484)
I used the rule
gross margin(Period,Amount) :-
    sales(Period,Sales_amount),
    cost of goods sold(Period,COGS),
    Amount is Sales_amount - COGS.
I can show
    1 sales(3,1210)
    2 cost of goods sold(3,726)
    3 1210 is 484 + 726
    Type a number
    2
To deduce
    cost of goods sold(3,726)
I used the rule
cost of goods sold(Period,Amount) :-
    sales(Period,Sales_amount),
    Amount is Sales_amount * .6.
I can show
    1 sales(3,1210)
    2 726 is 1210 * 0.6
    Type a number stop
```

Note: Augmented Prolog for Expert Systems (APES) was originally designed to work with the micro-Prolog (Clark and McCabe, 1984; LPA, 1984a) syntax. An actual dialog in that syntax has been modified to resemble the Edinburgh syntax in this example to improve readability. User input is underlined; predicate names are italicized.

## Figure 4. Example of Logic Programming Explanation Facilities

In addition to retrospective explanations that are essentially traces, users may benefit from facilities such as hypothetical and counterfactual reasoning (Waterman, 1986), suggested from expert systems research. Under hypothetical reasoning the system explains what would have happened under different facts or rules, and under counterfactual reasoning it explains why an expected conclusion was not reached. Furthermore, the system may be expected to respond not only to these “how” questions but also to “why ask” and “why better” queries (that tell the user why a particular input is required or why one alternative solution is judged better than another, respectively) (Rowe, 1988). As models increase in size, filtering and selecting appropriate explanation components become significant objectives in the construction of an appropriate meta-interpreter with Prolog.

Research in the financial planning domain suggests that users of financial models may benefit from at least two kinds of explanations (Kosy and Wise, 1984): those that help to validate the model by showing how it corresponds with reality and those that help to verify the model's correctness by showing the steps involved in deriving the results. In an empirical study of a spreadsheet-like equation-manipulating expert system (Fordyce, 1987), users judged the explanation of reasoning as a valuable feature.

A final and very powerful method of model analysis, which again addresses the fourth limitation associated with conventional software, is called meta-analysis. By using meta-analysis, it is possible to analyze the model without performing any analysis at the object level (e.g., object variable instantiation); rather the predicates themselves can be examined. For example, the (meta) predicate dependent on may be defined with two (object) predicate name arguments such that dependent on succeeds if the first object predicate's truth value is affected by the truth value of the second object predicate. Since predicate names appearing on the left side of the ':-' in Prolog rules are dependent on predicate names appearing on the right, it is a relatively simple matter to define the desired meta-predicate. This makes it possible to answer queries such as the following:

dependent on(gross\_margin,X)
dependent on(X,sales)

Meta-analysis facilities such as these are particularly valuable aids for examining, verifying, and validating models.

## Model interfacing

Separation of data, models, and the user interface as previously proposed by some authors (e.g., Sprague and Carlson, 1982), is not customarily maintained in logic programs. Furthermore, such separation is probably counterproductive because of the nature of logic programming. For example, consider the relationship between data and models. At a cursory level one may view facts as data and rules as models. This division is not a clean factoring of functionality, however, since logic programming implicitly generates data (facts) when evaluating rules. It can even generate and delete rules themselves, operating on them essentially as data. Perhaps a more useful portrayal of logic programming shows it manipulating an extremely large implicit database while physically storing only a small number of facts and rules for retrieving this data.

Model-model interfacing is accomplished with special predicates such as the “consult” command in Prolog. This facility allows both facts and rules to be moved from model to model, either on an ad hoc basis or when the need is determined by an executing program. A typical use of this facility is to modularize knowledge by type, source, etc., and subsequently use this knowledge as required. This also provides a means for separating generic knowledge from domain-specific knowledge.

A basic model-user interface is an integral part of logic programming interpreters such as Prolog. This interface consists primarily of two functions — one that allows facts and rules to be added to the knowledge base and another that facilitates querying of that knowledge base. In addition to this interface, a customized user interface can be easily built for whatever particular needs arise. Extensions to Prolog for a financial planning system's user interface are discussed in a later section of this article. An example of a general-purpose extension that is currently available is the APES (LPA, 1984b) interface, which explains the path of Prolog reasoning to the user as well as provides customizable input-output facilities.

For certain domain-specific functions and facilitation of interfaces to external software, it is expedient to rely on procedural attachments to logic programming engines. By using procedural attachments, subroutines of procedural code written in traditional programming languages can be invoked as required and relevant results can be returned to calling predicates. This allows all necessary special-purpose or pre-written routines to be accessible. In cases where logic programming-based financial modeling functions are desired within a larger system, it is also possible to call the Prolog inferencing mechanism as a sub-task and return results to the calling program.

## Implementation Considerations

This section addresses implementation considerations for logic programming-based financial modeling software. First, limitations of the Prolog vehicle for logic programming are discussed. Second, desirable extensions to basic logic programming and Prolog capabilities in support of useful financial planning systems are addressed. Finally, a simple example of how the proposed system might look to the user is shown.

## Limitations of Prolog

Coelho (1983) has compiled an extensive list of existing Prolog-based logic programming systems for applications including database management, natural language understanding, robotics, and production control systems. Despite the large number of operational Prolog applications, this particular language is sometimes criticized for its inefficiency, extra-logical characteristics, and failure to implement the full first order logic. Because Prolog is the most popular implementation language of logic programming, these criticisms will be briefly discussed.

The combinatorial nature of Prolog's resolution-based theorem-proving mechanism (Robinson, 1965) (discussed in the appendix) presents the potential for grossly inefficient programs. To help alleviate this problem, most Prolog dialects include a special "cut" predicate used to prune the search tree and prevent unnecessary backtracking. This is especially useful where only one solution to some intermediary goal is required for a higher level goal to succeed, preventing the wasteful location of all possible intermediary solutions. Many times a cut is not strictly necessary and may actually interfere with the implementation of multiway reasoning, but is included for the sake of execution efficiency. For a direct user of Prolog, the cut predicate represents an extrapolical procedural element that may require some knowledge of the problem domain to be properly used. The user of a logic programmingbased financial modeling system would not interact directly with Prolog, however, but rather would use a meta-interpreter "shell" (discussed in the final section). This shell can insulate the user from dealing with cuts directly.

Additional methods for enhancing Prolog efficiency include the use of Prolog compilers (Van Roy, 1984), the exploitation of parallelism (Clark and Gregory, 1983), specialized hardware (Dorby, 1984), and enhancements to the language such as goal caching (Fagin, 1984). Using one or more of these techniques, Prolog programs can be executed with approximately the same speed as comparable programs written in procedural languages. When using standard dialects of Prolog, it is currently more practical to implement many existing well-structured algorithms such as linear programming with the use of procedural attachments written in programming languages such as C or FORTRAN. This may not always be the case, however, considering recent enhancements of the Prolog language such as Prolog III (Colmerauer, 1987), which uses constraint-based methods to strengthen the numerical analysis capabilities of Prolog.

Of primary importance among Prolog's extralogical features is its so-called “negation by failure” feature. Based on a closed world database view, Prolog will judge not P true if P cannot be proved true from the existing base of facts and rules. This scenario can result in unanticipated results if it is used without due care, but can be avoided through proper program construction. Similar caution is necessary in circumstances (such as those involving mathematical computations) where extra-logical procedure calls are involved and where the order of terms and clauses may become significant.

Most current Prolog implementations do not incorporate the full first order logic, although there is research aimed at eliminating this shortcoming (e.g., Bowen, et al., 1982). In particular, explicit quantification of variables is not allowed, often requiring the Prolog programmer to simulate these features with suitably defined predicates. On the positive side, however, many Prologs currently support certain second-order logic facilities, including the use of variable predicates (predicate names treated as “first class” objects), which can result in extremely compact programs of extraordinary power and generality.

## Extensions of logic programming for financial modeling

It would be unreasonable to ask (and is not in this article) that managers and other users of financial planning software become familiar with a logic programming language such as Prolog in its “raw” form. The key to a successful logic programming-based financial modeling system for end users lies in the notion of a meta-interpreter (cf. Sterling and Shapiro, 1986). A meta-interpreter is essentially a “shell” or environment through which the underlying object language is controlled. Because of the extensible nature of Prolog, meta-interpreters are easily written in the Prolog language itself, and may range in complexity from a trivial form that merely calls the object language to elaborate systems controlling virtually every aspect of object language operation. Previously developed Prolog meta-interpreters have been used to provide traces of reasoning, for interactive expert system shells, and to incorporate reasoning with uncertainty (Sterling and Shapiro, 1986). For a financial modeling system, the following nine meta-interpreter components are desirable (the first five are particularly related to the user interface):

1. A user input parser and mapper accepts user input in a format convenient for the user, decomposes the input into its salient elements, and restructures it into a clausal form amenable for logic programming. For instance, an input format similar to existing modeling languages could be used where the user-supplied statement

$$
\begin{array}{c} \text {VARIABLE COST =} \\ \text {UNIT COST * SALES VOLUME} \end{array}
$$

is translated to the Prolog clause

variable cost(Vc) :-
unit cost(Uc),
sales volume(Sv),
multiply(Uc,Sv,Vc).

If emulation of current spreadsheet system interfaces is desired by users (as suggested in Kerschberg and Dickinson (1985)), another form of user interface would allow the user to move about the screen while automatically noting the locations where entries are made. When a definition is entered at a particular spreadsheet location, that location can be recorded with a predicate of the form

display location(predicate\_name,row,column).

Unlike traditional spreadsheets, however, the entry itself does not need to be inseparably coupled with the spreadsheet location where it was entered (the display location predicate is actually a meta-relation because it stores information about other relations). The independence between stored formulae or relationships and their location avoids constraining the logic program itself and still permits the answering of ad hoc queries not dependent on display location.

2. A model lister performs the inverse mapping of the first component, making a model stored internally in logic programming format readable to the user for inspection and modification. Users interacting with either a modeling language-like or spreadsheet-like interface would see entries displayed in essentially the same form as they were originally made.

3. A solution formatter formats output from the model as requested through the users' queries. Users desiring a spreadsheet display would be able to define the necessary display locations and formats. Other users might prefer to design an output report form more in the style of modeling language report generators. Even the choice of providing input in spreadsheet mode but displaying output in a modeling-language-like report (or vice versa) is possible. Again, independence between stored clauses and input/output details provides considerable flexibility.

4. A generalized explanation facility traces the reasoning process by which the inference engine reaches conclusions, and it explains this process to the user upon demand. As discussed earlier, this feature helps the user to validate and verify the model and understand its operation better. While a retrospective approach such as APES (LPA, 1984b) may suffice in some cases, a sophisticated explanation facility should be user-tailored and user-controlled and should rely on basic and meta-level principles to explain strategic reasoning (Hasling, et al., 1984). It should answer “how,” “how not,” and “why” questions.

5. A user-friendly query language allows the user to retrieve specific data (facts) and relationships (rules) as desired. This component essentially performs the same functions at the object level as components' one through three, but on an ad hoc basis that usually involves only a subset of the entire model. At the meta level, this facility provides a means for investigating specific model relationships and performing model meta-analysis, as discussed earlier.

6. A simple knowledge acquisition and maintenance facility manages dynamically changing facts and rules contained in the database. For instance, it will query the user for information necessary to proceed with reasoning when that information is not contained in the current database. Integrity and accuracy of the database may be maintained by detecting and correcting situations where the database contains recognizable redundancies or inconsistencies.

7. A loop detector recognizes model relationships that may be erroneous or may represent the presence of simultaneous equations. Loops can be detected by implicitly constructing a directed graph of consequent relationships and examining the resultant graph. Loops that are the result of user errors would be brought to the user's attention for correction, while others that represent simultaneous equations might be passed to a special equation-solving routine.

8. Internal utility routines allow the incorporation of such facilities as model consolidation and auditing features, which are appropriately implemented in Prolog.

9. An external software interface allows existing modules of code written in other languages to be available to the system. These external routines might include time value of money calculations, optimization procedures, graphical display routines, and other efficient segments of code that are better implemented outside Prolog.

With the recent interest in expert systems, it is interesting to note the relationship of the proposed extended logic programming paradigm to a recently developed expert system approach to worksheet modeling (Fordyce, 1987). This work implemented five enhancements to the basic spreadsheet approach: equation ordering, reversibility, calculation explanation, variable breakdown (dependency analysis), and English-like query capabilities. The first two of these func tions are integral to Prolog, while the remaining three are straightforward meta-level extensions very similar to a subset of the logic programming extensions addressed previously.

## A simple example

While the author believes the underlying expressiveness of the logic programming approach is the fundamental contribution of its application to financial modeling, the practical importance of a user interface must be recognized. In this section the discussion is brought to a very concrete and tangible level by illustrating a few features of one possible user interface that could be constructed through the use of a meta-interpreter shell. We must recognize that it is hardly possible to demonstrate more than a small fraction of the features or potential applications of a fully implemented system.

The example concerns a hypothetical loan evaluation model to be used by bank loan officers in evaluating loan applications. Consider the spreadsheet-oriented user interface as shown in Figure 5. A windowing system is used to manage the display of information to the user, with the main window containing an overall outline of the model but omitting detailed aspects. As in a conventional spreadsheet, the user may move from cell to cell and define (or display the definition of) the current cell by resting on that cell. Predicate names (or more English-like equivalents) will typically be shown as labels for other cells displaying the values of the predicate's terms. For example, the top line in the example might correspond to the internally maintained fact applicant name('Smith, John'). The meta-interpreter allows relationships to be extended using a pre-defined syntax that is translated into Prolog clauses for internal storage. Locations of relationships are noted for display purposes, and the usual labeling, formatting, and other appearance-related features are supported. A command window can be displayed at any time for necessary functions such as saving or printing the model.

The example shows that some sections of the spreadsheet (in this case, the top five lines of the main window) could be primarily used for user input. In addition to numbers and text, the user can enter (1) yes (true) or no (false), (2) qualitative values, and (3) "unknown" where appropriate. In this example, when the input cell for type of loan is given a value, a dialog window for that loan type appears to gather specific information on that type of loan (see the dialog window for automobile loans in Figure 5). The user does not need to define each dialog window when establishing the model — the meta-interpreter uses meta-rules that know that a dialog window is a “method of last resort” for instantiating any predicate containing unknown terms.

![](/api/attachments/9H5GSZ23/fulltext/images/f416c5eb59f66bb03e2c02b7319b9c1f8721aff8d57df929e1b250b100c08e71.jpg)  
Figure 5. A Spreadsheet-Oriented User Interface

Other sections of the spreadsheet (the next two lines of the main window in this example) could primarily be used to display output from the model. In this model, there are both numerical and qualitative outputs. Some cells can have multiple values or solutions — these cells could be highlighted on a display screen. By selecting a cell (through cursor keys or a mouse) and choosing a function (through function keys or a pulldown menu) the user can see both explanations of the reasoning and multiple solutions, if any. The “Explanation window for CREDIT RISK” in Figure 5 shows a possible explanation received after the user selected the “Credit risk” cell for investigation. The “INTEREST RATE solutions” window is shown when the user selects the “Interest rate” cell (which is highlighted, indicating multiple solutions) to seek additional solutions. The meta-interpreter has the ability to list not only multiple instantiations of terms for the term requested (interest rate), but also can automatically list the associated values of other terms in the same predicate or closely related predicates that directly affect interest rate (in this case, loan amount and term in months).

Since multiway reasoning allows some terms to function as either input or output, the user can fix the value of cells currently serving as output by merely entering one of those values as a constant input. For instance, in this example the user could rest the cell pointer on a cell with multiple solutions and cycle through several alternate solutions using a function key. When a preferred alternative is identified, another function key could be used to fix the term at that value. This would change the cell to an input term rather than an output term. The user would be able to release that term in the future, in which case it could revert to an output term again. A useful strategy for dealing with several related uninstantiated cells would be to successively supply input values for the known items and observe how the system automatically recognizes when enough information is present to compute remaining cells. Meta-rules can also be used to control the order of display where multiple values are present, e.g., in order of decreasing magnitude.

## Summary

Use of logic programming for financial modeling decision support systems can accomplish the same basic complement of functions associated with present day state-of-the-art systems. Much more importantly, it offers many advantages over more conventional spreadsheet or modeling language approaches, including the following:

1. a syntactical form that frees the user from spreadsheet-like constraints such as one-to-one definition to value relationships and two-dimensional rectangular geometrical configurations.

2. incorporation of semantic information into models, including the use of natural, named relationships given interpretation by the user and qualitative as well as quantitative knowledge.

3. flexibility derived from the properties of logic programming, e.g., multiway reasoning, self-adapting models, meta-level reasoning and explanation of reasoning, and the manipulation of knowledge (whether data or models) with the same basic mechanisms.

Future logic programming-based systems for financial planning will undoubtedly incorporate extensions for model building and analysis, increase the sophistication of inference mechanisms to more efficiently locate problem solutions, and provide better English-like explanatory facilities for justifying results to users. Combined with powerful semantic and knowledge-based capabilities, these systems will significantly extend the usefulness and scope of financial modeling software.

## References

Appleyard, F. and Hui, R. "DESIGN: A Financial Modeling System," Proceedings of the APL 1985 Conference: APL and the Future, Seattle, WA, May 12-16, 1985.

Blanning, R.W. "A Prolog-Based Framework for Model Management," Proceedings of the First International Workshop on Expert Database Systems, Kiawah Island, SC, October 24-27, 1984.

Bonczek, R.H., Holsapple, C.W. and Whinston, A.B. Foundations of Decision Support Systems, Academic Press, New York, NY, 1981.

Bonczek, R.H., Holsapple, C.W. and Whinston, A.B. "Developments in Decision Support Systems," in Advances in Computers (23), M. Yovits (ed.), Academic Press, Orlando, FL, 1984.

Bouwman, M. "Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis," Management Science (29:6), June 1983, pp. 653-672.

Bowen, D., Byrd, L. and Clocksin, W. "Programming with Full First-Order Logic, Machine Intelligence (10), January 1982, pp. 421-440.

Clark, K.L. and McCabe, F.G. "PROLOG: A Language for Implementing Expert Systems," Machine Intelligence (10), January 1982, pp. 455-470.

Clark, K.L. and Gregory, S. "PARLOG: A Parallel Logic Programming Language," research report, Department of Computing, Imperial College, London, 1983.

Clark, K.L. and McCabe, F.G. Micro-PROLOG: Programming in Logic, Prentice-Hall, Englewood Cliffs, NJ, 1984.

Clark, K.L. and McCabe, F.G. LPA MacPROLOG Reference Manual, Logic Programming Associates Ltd., London, 1985.

Clocksin, W.F. and Mellish, C.S. Programming in Prolog, Springer-Verlag, New York, NY, 1981.

Coelho, H. "Prolog: A Programming Tool for Logical Domain Modeling," in Processes and Tools for Decision Support, H. Sol (ed.), North-Holland, Amsterdam, 1983.

Colmerauer, A. "Opening the Prolog III Universe," BYTE, August 1987, pp. 177-182.

Darlington, J. and Kowalski, R.A. (eds.). Declarative System Architecture, SERC-DOI IKBS Architecture Study, Vol. 2, U.K. Government Department of Trade and Industry, London, 1983.

Dorby, T. "A Prolog Machine Architecture," technical note, Computer Science Division, University of California, Berkeley, CA, 1984.

Execucom, IFPS User's Manual, Release 10.0, Execucom Systems Corp., Austin, TX, 1984.

Fagin, B. "Issues in Caching Prolog Goals," Report No. UCB/CSD 84/204, Computer Science Division (EECS), University of California, Berkeley, CA, 1984.

Fordyce, K. "Looking at Worksheet Modeling Through Expert System Eyes," in Expert Systems for Business, G. Silverman (ed.), Addison-Wesley, Reading, MA, 1987.

French, P. LPA MacPROLOG User's Guide, Logic Programming Associates Ltd., London, 1985.

Futo, I., Darvas, F. and Szeredi, P. "The Application of Prolog to the Development of DBM and QA Systems," in Logic and Databases, H. Gallaire and J. Minker (eds.), Plenum Press, New York, 1978.

Ganoe, F. "Knowledge-Based Decision Support for Financial Analysis," Proceedings of the International Conference on Systems, Man, and Cybernetics, Halifax, Nova Scotia, Canada, October 9-12, 1984.

Goguen, J., Weiner, J. and Linde, C. "Reasoning and Natural Explanation," International Journal of Man-Machine Studies (19:6), December 1983, pp. 521-559.

Hasling, D., Clancey, W. and Rennels, G. "Strategic Explanations for a Diagnostic Consulting System," International Journal of Man-Machine Studies (20:1), January 1984, pp. 3-19.

Hayes-Roth, F., Waterman, D. and Lenat, D. Building Expert Systems, Addison-Wesley, Reading, MA, 1983.

Higgins, J. and Opdebeeck, E. "The Microcomputer as a Tool in Financial Planning and Control: Some Survey Results," Accounting and Business Research, Autumn 1984, pp. 333-340.

Hodges, W. Logic, Penguin Books, Middlesex, England, 1977.

Hogger, C. Introduction to Logic Programming, Academic Press, Orlando, FL, 1984.

Jarke, M. and Vassiliou, Y. "Coupling Expert Systems with Database Management Systems," in Artificial Intelligence Applications for Business, W. Reitman (ed.), Ablex, Norwood, NJ, 1984.

Kerschberg, L. and Dickinson, J. "FINEX: An Expert Support System for Financial Analysis," Proceedings of the Fifth International Workshop on Expert Systems and Their Applications, Avignon, France, May 13-15, 1985.

Kidd, A. and Cooper, M. "Man-Machine Interface Issues in the Construction and Use of an Expert System," International Journal of Man-Machine Studies (22:1), January 1985, pp. 91-102.

King, D. "Computer Generated Explanations of Financial Modeling Results: the ERGO Project," Execucom Systems Corp., Austin, TX (undated).

Kosy, D. and Wise, B. "Self-Explanatory Financial Planning Models," Proceedings of the National Conference on Artificial Intelligence (AAAI-84), William Kaufman, Inc., Los Altos, CA, August 1984, pp. 176-181.

Kowalski, R. Logic for Problem Solving, Elsevier, New York, NY, 1979.

Kowalski, R. "Logic Programming," in Information Processing 83, R. Mason (ed.), IFIP, Paris, France, 1983.

Lee, R.M. "Information System Semantics (a Logic-Based Approach)," Journal of Management Information Systems (1:2), Fall 1984, pp. 18-44.

Lee, R.M. "Database Inferencing for Decision Support," Decision Support Systems (1:1), January 1985, pp. 57-68.

LPA. Micro-PROLOG 3.1 Programmer's Reference Manual (4th ed.), Logic Programming Associates, Inc., Milford, CT, 1984a.

LPA. APES: Augmented Prolog for Expert Systems Reference Manual, Logic Programming Associates, Inc., Milford, CT, 1984b.

Lotus. Lotus 1-2-3 User's Manual, Lotus Development Corporation, Cambridge, MA, 1984.

Naylor, T.H. and Schauland, H. "A Survey of Users of Corporate Planning Models," Management Science (22:9), September 1976, pp. 927-937.

Poe, M.D., Nasr, R., Potter, J. and Slinn, J. "Bibliography on Prolog and Logic Programming," The Journal of Logic Programming (1), June 1984, pp. 81-142.

Robinson, R.A. "A Machine Oriented Logic Based on the Resolution Principle," Journal of the ACM (12), January 1965, pp. 23-41.

Rowe, N. Artificial Intelligence Through Prolog, Prentice-Hall, Englewood Cliffs, NJ, 1988.

Sprague, R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

Sterling, L. "Logical Levels of Problem Solving," The Journal of Logic Programming (2), June 1984, pp. 151-163.

Sterling, L. and Shapiro, E. The Art of Prolog, MIT Press, Cambridge, MA, 1986.

Turban, E. Decision Support and Expert Systems, Macmillan, New York, NY, 1988.

Van Roy, P. "A Prolog Compiler for the PLM," Report No. UCB/CSD 84/203, Computer Science Division (EECS), University of California, Berkeley, CA, 1984.

Walker, A. "Databases, Expert Systems, and PROLOG," in Artificial Intelligence Applications for Business, W. Reitman (ed.), Ablex, Norwood, NJ, 1984.

Waterman, D. A Guide to Expert Systems, Addison-Wesley, Reading, MA, 1986.

Whalen, T., Schott, B., Hall, N.G. and Ganoe, F. "Fuzzy Knowledge in Rule-Based Systems," in Expert Systems for Business, B. Silverman (ed.), Addison-Wesley, Reading, MA, 1987.

Wilkinson, J. "Financial Models: Helping Top Managers Plan," Arizona Business, First Quarter 1984, pp. 9-14.

## About the Author

Robert P. Minch is an associate professor in the Department of Computer Systems and Decision Sciences, College of Business, Boise State University. His current research interests focus on logical levels of information system management. He has published articles in several journals including Decision Sciences and IEEE Transactions on Systems, Man, and Cybernetics, and has presented papers at conferences including the International Conference on Information Systems and the Hawaii International Conference on Systems Sciences.

# Appendix Logic Programming

In contrast to traditional procedural programming languages such as BASIC or Pascal, logic programming is a declarative or non-procedural approach to problem definition and solution. In other words, rather than specifying how to solve a problem step by step, we specify what we know about the problem and what questions we would like answered. While some applications programs written in procedural languages may appear partially non-procedural (e.g., spreadsheet systems employing algorithms to internally schedule the order of cell evaluations), logic programming is fundamentally declarative — given facts and rules the system has an integral inferencing mechanism that is able to deduce all possible consequences that logically follow. Declarative languages have a number of advantages including their dual functions for both knowledge representation and problem solving, their dual functions for both specification and computation, their inherent parallelism, and their appropriateness for prototyping (Darlington and Kowalski, 1983).

Logic programming is not limited to the manipulation of numerical or character-based objects, as are most traditional programming languages. Instead, it can represent generic objects that have semantic meaning to the user, properties of objects, and relationships between objects. Thus we can capture qualitative knowledge (such as “alternative A is acceptable” or “alternative A is preferred to alternative B”) as well as quantitative knowledge. Two forms of knowledge may be stored: facts (such as those just listed) and rules (e.g., “alternative C is acceptable if there are no alternatives preferred to it”). A built-in inference mechanism answers user queries by referring to the stored facts and rules.

In more formal terms, logic programming involves the use of a restricted subset of first order predicate logic (Hodges, 1977) as a computer programming language (Clocksin and Mellish, 1981). In this language, statements consist of logical assertions in the form of Horn clauses. A Horn clause has a single conclusion that is implied by the conjunction of zero or more propositions, i.e.:

$$
P _ {0} \text {   if   } P _ {1} \text {   and   } P _ {2} \dots \text {   and   } P _ {n} \quad n > = 0
$$

where $P_{0}$ is called the head or conclusion of the clause and the conjunction of $P_{1}$ through $P_{n}$ form the body or conditions of the clause. Each proposition $P_{i}$ is of the form $p(t_{1}, t_{2}, \ldots, t_{m})$ where p is the predicate name and $t_{i}$ are its terms. The terms may be constants, variables, or functors. The Horn clause

## mother(X,Y) if parent(X,Y) and female(X)

is read "X is the mother of Y if X is the parent of Y and X is female." Horn clauses have the following logical (or declarative) interpretation: the conclusion is true if (but not only if) all conditions are true. Horn clauses also have the following procedural interpretation: to compute the head of the clause it is necessary to perform successfully the set of procedure calls that consist of the clause body. A clause with an empty set of conditions is always true and is called an assertion or a fact. A clause with an empty head is interpreted as a goal or query to be proved true or false. A logic program can then be defined as a set of Horn clause procedures activated by an initial goal clause (Kowalski, 1979).

In “pure” logic programming the declarative rather than the procedural interpretation of logic programs is paramount. Order of clauses is immaterial and all solutions to queries can be found. The logic sentences comprising the logic program as well as the interpreter’s inferencing and control strategies can take several forms. Unfortunately, pragmatic considerations such as execution efficiency and the need for a rich programming environment have limited the usefulness of pure logic programming approaches. They have also led to the development of impure but serviceable systems (such as Prolog) that constrain or enhance various characteristics of the underlying pure model.

Prolog was the first operational logic programming language. Today, it remains the most popular such system. A comprehensive bibliography of Prolog and logic programming work can be found in Poe, et al. (1984). For expository purposes the popular Edinburgh dialect of Prolog (Clocksin and Mellish, 1981) is used below. In this dialect the general form of implication is specified by

$$
P _ {0}: - P _ {1}, P _ {2}, \dots P _ {n}
$$

and the earlier example defining motherhood would be stated

$$
m o t h e r (X, Y): - p a r e n t (X, Y), f e m a l e (X)
$$

where '-' is read "if" and ',' is read "and." The simplest clause expressible in Prolog is an assertion or fact, examples of which are:

$$
\begin{array}{c} \text {likes(john,jane).} \\ \text { likes(Everyone,jane).} \end{array}
$$

The Edinburgh Prolog syntax requires constants to begin in lower case and variables to begin with an upper case character. For clarity, predicate names are italicized throughout this article. When both the head and body of a Prolog clause are present, the clause is called a rule, examples of which are:

$$
\begin{array}{l l} \text {likes(john, Opera) :- } & (\text {John likes opera if} \\ \text {likes(john,jane),} & \text {John likes Jane and} \\ \text {likes(jane, opera).} & \text {Jane likes opera}) \\ \text {likes(X,Z) :-} & (\text {X likes Z if} \\ \text {likes(X,Y),} & \text {X likes some Y and} \\ \text {likes(Y,Z).} & \text {Y in turn likes Z}) \end{array}
$$

Prolog interpreters operate in one of two modes. The first is “consultation” mode where the user may add facts and rules to the database. The second is “query” mode where the user submits goals to be disproved or proved by the inference engine. If variables are present in goals that are proved, the variables will be instantiated (bound) with the necessary values that make the overall goal true. A backtracking mechanism will locate and display multiple solutions to goals if they exist.

The relationship between logic, logic programming, and Prolog can be summarized concisely as follows: a Prolog system employs a depth-first, resolution-based, theorem-proving mechanism that operates on Horn clauses (a restricted subset of first-order predicate logic). Depth-first refers to the strategy whereby the search for solutions exhausts the deepest level for a given branch of the search tree before backtracking to investigate another branch (analogous to exploring all ramifications to a particular chess move before considering an alternative move).

Resolution is a particular method of inferencing or theorem proving developed by Robinson (1965). The essential principle is that, given two clauses containing a matching predicate symbol that is negated in one but not the other, the two original clauses can be resolved to form a new clause called the resolvent. The resolvent contains the disjunction of the original clauses, with the predicate symbol resolved upon eliminated. If a negated hypothesis is resolved against a database of clauses and results in a contradiction, then the original (non-negated) hypothesis is proved valid. Resolution possesses the important properties of soundness and completeness (Hogger, 1984). Soundness guarantees that any conclusions drawn are correct, while completeness assures that the algorithm will locate any consequence that follows from the stated hypotheses.

The representability and computability of Horn-clause logic and resolution is discussed by Hogger (1984), who notes that Horn-clause logic is a universal computing formalism and is equivalent in computational power to a universal Turing machine and all other universal computing formalisms (including traditional procedural programming languages such as FORTRAN). The practicality and efficiency of Prolog as an implementation vehicle is demonstrated by the recent emergence of a number of fast and easy-to-use Prolog compilers available for microcomputers (cf. Clark and McCabe, 1985; French, 1985).

Prolog violates the declarative nature of logic programming and the self-contained notion of predicate logic in a number of ways. Prolog interpreters normally incorporate procedural strategies such as considering terms within clauses in left-to-right order and clauses within programs in top-down fashion. These strategies deal with problems of non-determinism related to scheduling procedure calls and cases where several procedures match a procedure call, respectively. The role of clause terms as procedure parameters (either input or output) depends on the calling context, and the actual input/output is accomplished as a “side effect” of the theorem-proving process that instantiates variables with values sufficient to prove goal clauses true. Extralogical control mechanisms include the special “cut” predicate that is used to prevent unnecessary backtracking in cases where, for example, a goal is known to have only one solution. Despite these idiosyncrasies, Prolog is a practical surrogate for pure logic programming (Clocksin and Mellish, 1981) and provides expedient and useful extensions to logic programming (such as list processing) as well (Kowalski, 1983). Bonczek, et al. (1984) states: “Although traditional programming languages will continue to be important DSS development tools, languages such as Prolog and its descendants should play an increasingly important role in both the building of problem processors and the specification of modeling knowledge for use by problem processors” (p. 160).
