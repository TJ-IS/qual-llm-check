---
otero_id: 17116
otero_key: "XPM3JDBG"
title: "Controlling expert system recommendations with defeasible logic"
authors: "Donald Nute; Robert I Mann; Betty F Brewer"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90005-c"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Controlling Expert System Recommendations with Defeasible Logic $^{1}$

Donald NUTE \*, Robert I. MANN \*\* and Betty F. BREWER \*\*\*

\* Department of Philosophy, University of Georgia, Athens, GA 30602, USA

\*\* Department of Information Systems, Virginia Commonwealth University, Richmond, VA 23284, USA

\*\*\* Small Business Development Center, University of Georgia, Athens, GA 30602, USA

Nonmonotonic logics are alternatives to probabilistic systems for reasoning with uncertain or incomplete information. For the most part, these logics have not been implemented as automated reasoning systems or incorporated into expert systems that deal with real problems. Defeasible logic is a non-monotonic formalism implemented in an extension of the Prolog logic programming language called d-Prolog. FORE is an initial prototype expert system for selecting a business forecasting method. Written in d-Prolog, FORE demonstrates the feasibility of using defeasible logic to control the recommendations of expert systems with a significant degree of complexity. It also serves the secondary purpose of providing a foundation for development of a mature forecasting method selection system.

## 1. Introduction

Human reasoning is often nonmonotonic, meaning we draw conclusions that we must retract in the face of further evidence. A physician arrives at a diagnosis based on symptoms he observes and is certain about. The diagnosis, however, is not certain. He will replace his diagnosis with a new one if additional symptoms appear that conflict with the original diagnosis. Reasoning that can be defeated by further information is called non-monotonic reasoning, and human experts often base their conclusions on just such reasoning. If expert systems are to reason as effectively as humans, they must be able to reason nonmonotonically. In this paper, we will present a nonmonotonic formalism and show how it is used to control selection of forecasting methods in a prototype expert or knowledge based system.

Reasoning with uncertain or incomplete information has been implemented in expert systems by using probabilistic or fuzzy reasoning. The common wisdom is that these techniques make knowledge acquisition, system validation, and

![](/api/attachments/XPM3JDBG/fulltext/images/074cb16d81cd4dc41da37d309a4f6706ac283d3401c8fe7c0e9df151c501b3a1.jpg)

Donald Nute is Professor of Philosophy and Director of Artificial Intelligence Programs at the University of Georgia. His interest in logic programming, automated reasoning, natural language understanding and expert systems arises out of his philosophical research in logic, epistemology and the philosophy of language. Included among his more than fifty scholarly publications are Topics in Conditional Logic (1980), Essential Formal Semantics (1981), and Prolog Programming

in Depth (with Michael Covington and Andre Vellino, 1988).  
![](/api/attachments/XPM3JDBG/fulltext/images/0291969cc28f664495d83179d8ecedbd4217248dd7d98b18dccf107863175aeb.jpg)

Robert I. Mann. is Associate Professor of Information Systems at Virginia Commonwealth University. He has published articles in a number of journals, including MIS Quarterly, Data Base, Information and Management, Journal of Management Information Systems, Journal of Information Systems Management and Economic Inquiry. His current teaching and research interests include knowledge-based systems, computer assisted systems engineering (CASE) and structural methodologies.

tured systems development methodologies.  
![](/api/attachments/XPM3JDBG/fulltext/images/bf98e5f702750fc1a88a06923a5265556e600c46f65f117fa83c0a5d5bcd72bf.jpg)

Betty F. Brewer is Coordinator of Management Information Systems for the University of Georgia Small Business Development Center. She is pursuing a Masters degree in Artificial Intelligence at the University of Georgia. Her research interests include business oriented knowledge based systems and knowledge acquisition.

$^{1}$ This paper is an expanded and revised discussion of research first reported in Nute et al. (1988). We would like to thank the two anonymous referees whose comments prompted important changes from an earlier version of the paper. The first author received support for this work from the National Science Foundation under Grant No. IST-8505586.

maintenance of the resulting systems difficult. The forecasting method selection prototype we will describe uses 16 evaluative criteria to select from among 20 forecasting methods. Suppose we persuade an expert to rank the 20 forecasting methods with respect to each of the 16 evaluative criteria and to assign numbers to the methods as part of this ranking. Now we want to combine these numbers somehow to choose the appropriate methods for some combination of responses to the 16 evaluative criteria. To do this, we have to assume that the numbers assigned for each criterion accurately represent relative strength (or relative possibility for fuzzy systems) rather than just the order of ranking relative to that criterion. We also have to assume that the numbers are measuring the same quantity for each of the different criteria of selection. These assumptions are often implausible.

Even if numerical approaches are initially plausible for some domains, they are implausible for normative domains that involve reasoning with regulations, laws, policies, rules of evidence or other norms. For example, in American jurisprudence a defendant in a criminal case is presumed innocent until proven guilty. This presumption is not based on an estimate of the probability that a criminal defendant is innocent. Nor do we see how it can be explained by appeal to a notion of the degree to which a defendant belongs to the class of innocents as fuzzy logic would suggest.

Another approach to reasoning with exceptions is to list all exceptions as explicit conditions for the rule. This produces long, unwieldy rules, but there is a more serious problem with this method. Consider the two rules ‘Automobiles normally use gasoline for fuel’ and ‘If an automobile does not have a diesel engine, then it uses gasoline for fuel.’ Knowing only that something is an automobile, the first rule but not the second will allow us to draw the tentative conclusion that it uses gasoline for fuel. We cannot apply the second rule at all unless we know that the automobile does not have a diesel engine, but the very idea behind non-monotonic reasoning is that we might have to draw a conclusion without this knowledge.

An alternative to the numerical and the explicit exceptions approaches is to represent nonmonotonic reasoning within a formal calculus. Defeasible logic is a nonmonotonic formalism that shows us how we can use logical form alone to determine when some rule-of-thumb or heuristic principle is defeated by other information. This approach does not rely on numerical probabilities or certainties. Defeasible logic is implemented in d-Prolog, an extension of the logic programming language Pro-log.

A common kind of expert system is one that can recommend to a user one or more of a set of alternative courses of action the user is considering. In describing many domains for which we would like to develop this kind of expert system, we will say that there are circumstances which indicate the different alternatives, other circumstances which counterindicate alternatives, and still other circumstances which absolutely rule out alternatives. Ideally, we would state the indications, counterindications, and absolute counterindications for the different alternatives as simple rules and the expert system would sort this information out for us and make appropriate recommendations for any situation. We can state the principles for performing this kind of reasoning in four English sentences:

(1) Recommend an alternative if it is indicated.

(2) Do not recommend an alternative if it is counterindicated.

(3) Recommend an indicated alternative, even if it is also counterindicated, if every alternative is counterindicated.

(4) Never recommend an alternative if it is absolutely counterindicated.

The first three of these principles are clearly defeasible; in fact, each can be defeated by its successor. Properly represented in defeasible logic, these principles can control selection of alternatives without using certainty factors. Later we will look at an an exact statement in d-Prolog of versions of these principles for our domain.

We will demonstrate the feasibility of using defeasible logic to control expert system recommendations with a prototype system called FORE. Written in d-Prolog, FORE recommends business forecasting methods appropriate to the user's needs and circumstances. We first describe the forecasting method selection problem and alternative approaches to its solution. Then logic programming and Prolog are introduced, followed by a detailed discussion of defeasible reasoning and d-Prolog. Finally, the prototype system is presented together with the precise formulation of the four selection principles listed above.

## 2. The Problem Domain: Selecting a Business Forecasting Method

To circumvent the problems associated with what is widely described as the knowledge acquisition bottleneck, we selected a published guide to forecasting as our expert. Georgoff and Murdick (1986) encapsulate a strategy for selecting a forecasting method in a 20 by 16 matrix that portrays 20 common forecasting techniques and uses 16 evaluative criteria to indicate the strengths and weaknesses of each technique.

The forecasting techniques chosen by Georgoff and Murdick include naive extrapolation and the following judgmental, counting, time series, and causal methods.

Judgmental methods: sales-force composite, jury of executive opinion, scenario methods, Delphi technique, and historical analogy.

Counting methods: market testing, consumer market survey, and industrial market survey.

Time series methods: moving averages, exponential smoothing, adaptive filtering, time series extrapolation, time series decomposition, and Box-Jenkins ARIMA.

Causal methods: correlation methods, regression models, leading indicators, econometric models, and input-output models.

Detailed descriptions of these and other forecasting methods may be found in Makridakis and Wheelwright (1987), a good overview for managers, and Wheelwright and Makridakis (1985) and Jarrett (1987), two good overviews for the more technically oriented.

The evaluative criteria chosen by Georgoff and Murdick include the following time, resource requirements, and input and output dimensions.

Time span: urgency and frequency.

Resource requirements: mathematical sophistication, computer resources, and financial resources.

Input: antecedent, variability, internal consistency, external consistency, and external stability.

Output: detail, accuracy, capability for reflecting direction changes, and form.

Details of these criteria are also discussed in Makridakis and Wheelwright (1987).

A considerable body of research has examined the effects of combining forecasts [Bates and Granger (1969) and Holden and Peel (1986)], but that option is not discussed by Georgoff and Murdick. Nor is the finding that various research efforts have determined that quantitative methods are more accurate than qualitative methods while others have found the converse [Mahmoud (1984)]. The relative accuracy of combinations of forecasts vs. single method forecasts and the relative accuracy of different time series forecasting methods have also been questioned in this literature.

Other expert forecasting method selection systems have been reported in the literature, for example in [Kumar and Hsu (1988)]. These systems use essentially the same forecasting methods and the same selection criteria used by Georgoff and Murdick; thus in this respect they are similar to FORE. They are also rule based systems. They differ, however, in the manner that they implement nonmonotonic or uncertain reasoning, using probabilistic weights and fuzzy logic rather than defeasible logic.

Since our primary goal is to test the feasibility of defeasible logic as a selection control mechanism, we are uncritical of the advice we find in the Georgoff and Murdick matrix. We try to extract rules from the matrix that tells us when a particular forecasting method is indicated, counterindicated, or absolutely counterindicated. We make no extensive attempt to correct vague or imprecise language used in the matrix or to improve the validity of the recommendations although some interpretation of the matrix is unavoidable. We recognize that as a useful tool for forecasting method selection, the prototype requires much refinement. Nevertheless, we would argue that FORE, and especially the defeasible control structure used in FORE, provides a plausible foundation for the development of a mature forecasting method selection system.

Each cell in the selection matrix represents a characteristic of the technique (column) as it applies to an evaluative criterion (row). Some of the cells represent strengths for a particular technique, others represent weaknesses. Some of the weakness cells preclude use of the associated technique; others simply indicate that the technique can be used, but that it has difficulty accommodating the associated evaluative criterion.

Herein lies the essential difficulty of the business forecasting problem and its suitability for our purpose. Rarely, in any given situation, will any forecasting technique have only its strength characteristics apply in that situation. In only a few situations will all forecasting techniques be precluded from use. In most situations, multiple techniques will possess both applicable strength characteristics and applicable weakness characteristics that do not completely preclude their use. In the following, a forecasting method will be indicated if it possesses applicable strength characteristics, it will be counterindicated if it possesses applicable weakness characteristics that do not preclude its use, and it will be absolutely counterindicated if it possesses applicable weakness characteristics that do preclude its use.

Table 1.

<table><tr><td>Dimension</td><td>Question</td><td>Naive extrapolation</td><td>Box-Jenkins time series</td></tr><tr><td>Forecast frequency</td><td>Are frequent forecast updates needed?</td><td>↑ CAN EASILYACCOMMODATEFREQUENT UPDATES</td><td>↑ FORECAST CAN BESYSTEMATICALLYUPDATED EASILY</td></tr><tr><td>Computer resource requirements</td><td>Are computer capabilities limited?</td><td>↑ COMPUTERCAPABILITIESARE NOT ESSENTIAL</td><td>↓ ↓ A COMPUTERIS ESSENTIAL</td></tr><tr><td>Output accuracy</td><td>Is a high level of accuracy critical?</td><td>↓ OFTEN PROVIDES ALIMITED PRACTICALLLEVEL OF ACCURACY</td><td>↑ FREQUENTLYTHE MOST ACCURATERFOR SHORT TO MEDIUMRANGE FORECASTS</td></tr><tr><td>Forecast urgency</td><td>Is the forecast needed immediately?</td><td>↑ RAPID RESULTSARE A STRONGADVANTAGE OFTHIS TECHNIQUE</td><td>↓ OPERATIONALIZINGPROGRAM CAN TAKE TIME,BUT FORECAST CAN BEPRODUCED QUICKLY</td></tr></table>

Adapted from Georgoff and Murdick (1986).

To illustrate, the partial matrix shown in table 1 includes columns for two of the 20 forecasting methods: the naive extrapolation technique and the Box-Jenkins time series technique. Four of the 16 evaluative criteria together with their associated questions are depicted by the rows of the matrix. Each intersecting cell represents the characteristics of a method relative to an evaluative criterion. Strengths are marked with an arrow pointing upward (↑), weaknesses that do not preclude use are marked with an arrow pointing downward (↓), and weaknesses that preclude use are marked with two arrows pointing downward (↓↓).

If the answer to a question is no, then the row is ignored. Techniques indicated by the remaining rows are qualified for consideration. If an indicated technique is absolutely counterindicated, then its use is precluded. If, on the other hand, its use is only counterindicated, one may or may not elect to use the technique. If an indicated technique is neither counterindicated nor absolutely counterindicated, it should be strongly considered for use. Thus, the matrix effectively classifies forecasting methods into three categories: 'recommended', 'not recommended', and 'recommended with reservations'.

Consider the situation in which frequent forecast updates are needed, computer capabilities are limited, a high level of accuracy is critical, and the forecast is needed immediately. The Box-Jenkins method would not be recommended (absolutely counterindicated by the characteristic ↓↓ A COMPUTER IS ESSENTIAL), while the naive extrapolation method would be recommended with reservations (counterindicated by the characteristic ↓ OFTEN PROVIDES A LIMITED PRACTICAL LEVEL OF ACCURACY).

Now consider the situation in which frequent forecast updates are needed, computer capabilities are not limited, a high level of accuracy is critical and the forecast is not needed immediately. The Box-Jenkins method would be recommended, while the naive extrapolation method would be recommended with reservations. $^{2}$

It should be noted that these outcomes are based solely on the limited version of the matrix shown above. Other evaluative criteria and other methods must be considered in a realistic evaluation. The entire 20 by 16 matrix is included in the prototype system.

## 3. Logic Programming and Prolog

Logic programming includes efforts to implement logical systems on computers and to use these implementations to solve real problems. The best known and most widely available logic programming environment at this time is the programming language Prolog. Clocksin and Mellish (1981) establish a de facto standard for Prolog syntax. Good implementations of Prolog are available on a wide range of equipment including IBM-PC compatibles. The rest of this section comprises an introduction to the basic features of the Prolog programming language. Readers familiar with Prolog may wish to skip to the next section.

Prolog is built around a theorem prover for a fragment of first order predicate logic called Horn clause logic. A Horn clause is an 'if-then' conditional with a single atomic formula as conclusion and a simple conjunction of atomic formulae as antecedent conditions. The atomic formulae may contain variables which are treated as though they fall within the scope of a universal quantifier at the beginning of the conditional. Most Prolog implementations allow disjunctive conditions in the clauses and provide other features that depart from the ideal that Horn clause logic represents. The advantage of Horn clause logic is that there is an algorithm for deciding whether one Horn clause follows logically from a specified set of Horn clauses. Nevertheless, Prolog provides a highly efficient theorem prover that trades decidability for additional speed and expressive power.

A Prolog program/database is simply a collection of clauses. There is no syntactic distinction between program and data or knowledge in Prolog, although good programming practice may require us to distinguish the two conceptually. Computation begins when Prolog is presented with a query. It treats this query as a theorem to be proved from the database. If the query contains no variables, Prolog will respond with a 'yes' or a 'no'. If there are variables in the query, Prolog will try to find values for the variables for which the query can be proved. If it succeeds, it will display these values as the solution to the query. If asked to find other solutions, Prolog will backtrack and try to find another proof, again displaying the new variable bindings. It will continue finding new proofs and solutions until it can find no more or until the user indicates that no more are required. Because it can find many solutions to a single query, Prolog is called nondeterministic.

While we find structured procedural programming in Prolog to be easy and natural with some experience, we will concentrate on the declarative programming methods for which the language is primarily used. Let's look at a simple example of a Prolog program/database and a Prolog computation. An atomic formula is represented by a predicate and a list of arguments. Some examples are:

```prolog
parent(john, babyjane).
parent(mary, babyjane).
parent(grandpa, john).
male(john).
male(grandpa).
female(mary).
female(babyjane).
```

In Prolog, single atomic formulae asserted like this are called facts. With this database the following queries would succeed, producing a 'yes' response:

?- parent (john, babyjane).

?- male (john).

The query

?- male(X).

would produce two solutions:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$X = \mathrm{john},$ $X = \mathrm{grandpa}.$
</div>

Notice that we begin variable expressions with capital letters and we begin predicates and constants with lower case letters.

Conditional rules are represented using the operator :-, which we read 'if'. Likely rules for our developing database are

```prolog
father(F, C) :-
parent(F, C),
male(F).
```

grandparent(GP, GC) :-
parent(GP, X),
parent(X, GC).

With these rules and the facts we provided above, the query

?- father(john, babyjane).

will succeed, and the query

?- father(grandpa, mary).

will fail. The query

?- mother(mary, babyjane).

will also fail, of course, because we have not told Prolog anything about the predicate mother. The query

?- grandparent(GP, GC).

will produce the single solution

$GP =$ grandpa,

GC = babyjane.

A program that can infer new facts from other rules and facts is sometimes called an inference engine. As we have seen, Prolog has a powerful built-in inference engine. In fact, all computation in Prolog involves the efforts of the built-in inference engine to prove some goal from available data.

The Prolog inference engine treats all rules as absolute rules. Whenever it accepts the condition of a rule, it also accepts the consequent. Nothing can defeat this process.

## 4. Defeasible Logic and d-Prolog

d-Prolog (defeasible Prolog) is a program written in Prolog that extends both Prolog syntax and the Prolog inference engine. This Prolog extension is developed and compared with other approaches to the same or similar problems in a series of research reports and publications [Nute and Lewis (1986) and Nute (1987, 1988, 1988a)].

The basic insight behind d-Prolog is that people draw conclusions from available evidence and justify those conclusions on the basis of the normal or typical case. The conclusion is defeasible – additional (contradictory) information could cause us to change the conclusion. For example, if asked to build a bird cage we will put a roof on it. If asked why we spent time and materials on a roof, we will say, 'So the bird won't fly away.' But suppose we were not told that the bird to be kept in the cage can fly. Still we can respond that normally birds can fly, and lacking evidence to the contrary, we are justified in presuming that the bird to be kept in the cage can fly.

The rule ‘Birds fly’ is defeasible. We know that penguins, ostriches, very young birds, dead birds, and so on, do not fly. But we will apply the rule in any case where we do not have evidence that we are dealing with an atypical case. We say the rule is defeasible, then, just because there are cases where the condition for the rule, ‘This is a bird’, is true, but the consequent, ‘This can fly’, is false.

Defeasible rules are extremely common: 'Matches burn when they are struck', 'A mother will be relieved if her baby stops crying', 'One should keep ones promises', 'A smoker's health will improve if he stops smoking', 'Friends keep their appointments', 'Students may not park on campus', and so on. Any of these could be offered in support of some conclusion we have reached or some action we have taken, yet every one of them has exceptions. Wet matches don't burn, mothers aren't relieved when their babies stop crying because they are choking, it is permissible to break a promise if a life is at stake, and so on.

We want to be able to represent these rules in a logic programming environment. More importantly, we want our inference engine to know how to use these rules, that is, when to use a defeasible rule and when not to use it. Basically, we use a defeasible rule unless we are in a situation where it is defeated. When are we in such a situation?

Obviously, we know that a defeasible rule is defeated in a case where we know for certain that the condition of the rule is true and the consequent is false. We take a perfectly ordinary-looking match from a box and scratch it against the side of the box. It doesn't light. Repeated attempts are unsuccessful. We accept the defeasible rule that matches burn when they are struck, but we clearly do not conclude that this match is burning. Instead, we may wonder what there is about this particular match that makes it an exception to the rule.

Other, more interesting cases where rules are defeated involve competing rules. Mollusks normally have shells but cephalopods normally don't. Fred is both a mollusk and a cephalopod. Does Fred have a shell? To decide, we need to know whether Fred is either an exceptional mollusk or an exceptional cephalopod. Without this information, we can't decide. And if we have evidence that Fred is neither a normal mollusk nor a normal cephalopod, we still won't be able to decide which rule to use. But suppose we know only that a cephalopod is a kind of mollusk. Then we have evidence that Fred is a special kind of mollusk, but so far as we know he is a perfectly ordinary cephalopod. So we use the defeasible rule for cephalopods and conclude that Fred does not have a shell.

```prolog
has_shell(X) := mollusk(X).
neg has_shell(X) := cephalopod(X).
mollusk(X) :- cephalopod(X).
cephalopod(fred).
```

One last case introduces a new element. We know that a damp match will sometimes burn and sometimes not. Suppose that our experience does not tell us that damp matches either normally do or normally do not burn. Then we don't accept either of the two possible defeasible rules about striking damp matches. But we do accept that a damp match might not burn if it is struck. And this is enough to prevent us from using the rule 'Matches burn when they are struck' when we know the match in question is damp. This kind of might conditional is what we will call a defeater. It never entitles us to draw a conclusion, but in the right circumstances it does prevent us from using other rules to draw conclusions. We will want to represent defeaters in our logic programming environment.

d-Prolog understands the principles we have just established for deciding when to use a defeasible rule. It can apply these principles to complicated chains of reasoning involving several interacting absolute rules, defeasible rules and defeaters, even in cases where a person has difficulty sorting out the different interactions.

Absolute rules are represented in d-Prolog as ordinary Prolog rules. Defeasible rules are represented using the operator := which we read 'normally...if'. For example,

fly(X) := bird(X).

says normally something can fly if it is a bird. We represent defeaters in d-Prolog with the operator : , which we read 'might...if'. For example,

neg burns(X): ^ match(X), damp(X), struck(X).

says that something might not burn if it is a damp match and it is struck.

Notice the operator neg in the last example. This is also an innovation in d-Prolog. Prolog does not have a true negation. We need negation to express rules that say when a conclusion cannot be drawn, or when a negative conclusion can be drawn.

We represent our earlier mollusk/cephalopod example in d-Prolog with the following database:

When we want d-Prolog to use defeasible rules in its attempt to answer a query, we use the operator @ to invoke the built-in defeasible inference engine. With this database, the d-Prolog query

?- @ has\_shell(fred).

will fail, and the query

?- @ neg has\_shell(fred).

will succeed. Suppose we add another fact and a defeater to our database:

has\_shell(X) : ^ nautilus(X).
nautilus(fred).

Now both our queries fail because the defeasible rule for mollusks gets defeated by the defeasible rule for cephalopods, the defeasible rule for cephalopods gets defeated by the defeater for nautili, and the defeater never licenses any conclusion.

One last feature of d-Prolog to mention, before we look at our business forecasting method selector, is the way it handles presumptions. A presumption is a simple statement we accept, although we are aware that certain evidence would lead us to reject it. It is a kind of defeasible fact. For example, we might presume 'The incumbent will be reelected', but we also believe 'The incumbent will not be reelected if he is implicated in a voteselling scandal'. We can represent presumptions in d-Prolog using the built-in Prolog predicate true. This predicate requires no arguments, so true is a complete atomic formula all by itself. Furthermore, true always succeeds. We capture our election example with the following database.

elected(incumbent) := true.

neg elected(incumbent) :=

implicated\_in\_scandal(incumbent).

Given these two rules, the d-Prolog query

?- @ elected(incumbent).

will succeed unless something is added that makes the query

?- @ implicated\_in\_scandal(incumbent).

succeed. Then the first query will fail.

Besides absolute rules and facts, d-Prolog provides ways to represent defeasible rules, defeaters, and presumptions. More importantly, it knows how to use these representations to reach conclusions in much the same manner people do in simple cases. It extends these methods to reach conclusions in complicated cases where people have difficulty sorting out the interactions of several rules, but it does this by using, over and over again, the same principles we have extracted from the simple cases.

Other formalisms for nonmonotonic reasoning encounter the multiple extensions problem. The intuitive idea behind these systems is that of a minimal model [McCarthy (1980, 1986)], a fixed point [McDermott and Doyle (1980)], or a default extension [Reiter (1980)] of a nonmonotonic theory. In general, there will be more than one of these for a particular theory. Then either the logical consequences of the theory are taken to be the intersection of the extensions of the theory (McCarthy; McDermott and Doyle) or no attempt is made to choose between extensions (Reiter). Hanks and McDermott (1986) link this problem to a supposed inability of nonmonotonic formalisms to handle temporal reasoning adequately.

Defeasible logic avoids the multiple extensions problem because its proof procedure is not motivated by the same kinds of semantical considerations as these earlier systems. While defeasible theories can have multiple extensions, these are never generated as part of the proof procedure. Instead, the defeasible logic proof procedure generates a unique logical closure [Nute (1988, 1989)]. Other recent nonmonotonic formalisms avoid the multiple extensions problem as well [Poole (1985), Loui (1987), Geffner and Pearl (1987) and Geffner (1988)].

## 5. A Prototype for Selecting a Business Forecasting Method

It is straightforward to represent the conditions that indicate, counterindicate, or absolutely counterindicate different business forecasting methods in ordinary Prolog rules. These rules will have one of the following general forms in Prolog.

indicated(Method) :- Condition\_1.

counterindicated(Method) :- Condition\_2.

absolutely\_counterindicated(Method) :-

Condition\_3.

There could be more than one rule of each type for any given method.

Besides these rules, the FORE knowledge base includes a set of questions used to ask the user about the circumstances in which the business forecast is to be made. At the beginning of a consultation, an automatic procedure asks the questions and stores the answers. Some questions are only asked if the system already received a certain answer to an earlier question. This prevents the system from asking a question that the user would find silly in light of earlier answers he had given.

After gathering information about the user's circumstances, the system reaches a recommendation. It will first try to find a business forecasting method that is indicated but for which there is no counterindication. If one or more methods in this category are found, the system reports them and the consultation ends. If there is no “ideal” recommendation, the system finds all indicated methods that are not absolutely counterindicated. Of course, at this point any indicated method will also have counterindications. When the system reports its recommendations, it also reports the counterindications. If no method is indicated, or if every indicated method is also absolutely counterindicated, the system reports that it can make no recommendation.

A selection strategy like the one we have just described would normally receive a procedural treatment as part of a specialized inference engine or control structure. By contrast, it can be represented declaratively in d-Prolog. To do this, it is convenient to presume that no “ideal” method will be found. This presumption will be defeated if, after all, there turns out to be an indicated method with no counterindications. With this presumption, the declarative metarules for the system look like this:

(1) none\_recommended\_unconditionally := true.

(2) neg none\_recommended\_unconditionally : known(recommend, \_).

(3) recommend(Method) := indicated(Method).

(4) neg recommend(Method): counterindicated(Method).

(5) recommend(Method) := none\_recommended\_unconditionally, indicated(Method), counterindicated(Method).

(6) neg recommend(Method) :-
absolutely\_counterindicated(Method).

The first rule, a presumption that we will not find a method that has no counterindications, simplifies our statement of the other rules in the set. The fifth rule tells us that we can recommend an indicated method even if it is also counterindicated if every indicated method is also counterindicated. These six rules represent a structure that applies to many domains where strengths and weaknesses of alternative recommendations must be compared. $^{3}$

The main procedure for FORE includes the d-Prolog query

?- @ recommend(Method).

Whenever a suitable method is found, it is remembered and reported to the user together with any counterindications.

If a method is available that has no counterindications, it will be found first using rule 3. When it is reported, the system will also add the fact

known(recommend, Method).

to the database, substituting the name of the method for the variable Method. This fact, together with rule 2, will defeat the presumption stated in rule 1. This in turn will prevent the first condition of rule 5 from being satisfied for any method, and the system will not recommend any counterindicated methods.

If every method found by rule 3 is counterindicated, then rule 4 will defeat rule 3 for every method. In this case, the system never adds the fact

## known(recommend, Method).

to the database. Now the first condition of rule 5 is satisfied by the presumption in rule 1, and the system looks for the next best choice: an indicated method that also has counterindications.

The last rule, of course, defeats any method that is absolutely unacceptable in the circumstances.

These six simple rules give the system considerable power. They automatically arrange the methods available in the system into a hierarchy of suitability. Ideal methods, and nothing else, will be reported if they are available. If not, any indicated method that is counterindicated but not absolutely counterindicated will be reported. Thus, the system makes a recommendation even when no method can be found that exactly fits the circumstances. Of course, there may always arise a situation where no method fits even approximately. Because the selection strategy is represented declaratively rather than procedurally, it is a fairly simple matter to modify it. For example, we might implement a hierarchy with more levels by using predicates counterindicated\_1, counterindicated\_2, and so on.

As an example of the way a business forecasting method could be represented in FORE, let's look at the rules specified by table 1. We have changed the format of the conditions for these rules to make them easier to read.

(7) indicated(naive\_extrapolation) :- frequent\_forecasts\_are\_needed.

(8) indicated(naive\_extrapolation) :- computer\_capabilities\_limited.

(9) indicated(naive\_extrapolation) :- forecast\_needed\_immediately.

(10) counterindicated(naive\_extrapolation): - high\_level\_of\_accuracy\_is\_critical.

(11) indicated(box\_jenkins) :-
frequent\_forecasts\_are\_needed.

(12) indicated(box\_jenkins) :-
high\_level\_of\_accuracy\_is\_critical.

(13) counterindicated(box\_jenkins): - forecast\_needed\_immediately.

(14) absolutely\_counterindicated(box\_jenkins) :- computer\_capabilities\_limited.

Suppose the condition for rule 11 is satisfied. Then if the conditions in rules 13 and 14 are not satisfied, the Box-Jenkins method will be recommended. If the condition for rule 13 is satisfied, FORE will still recommend the Box-Jenkins method if there is no other method that is indicated but not counterindicated. That is, of course, unless the condition for rule 14 is satisfied. Then the Box-Jenkins method will not be recommended no matter what else happens.

The recommendation of the Box-Jenkins method gets flipped on or off depending on the situation. The hierarchy of choices we get here does not depend on the order that either the Box-Jenkins rules or the six metarules are entered into the knowledge base. d-Prolog determines the hierarchy using the metarules and their logical forms alone.

The reader might object that rule 14 is not needed. Instead, we could just add the condition of rule 14 with a negation to rules 11 and 12. Then the Box-Jenkins method would never be recommended unless computer capabilities were of an acceptable level. However, there are good reasons for preferring the method we see here.

Suppose we add an additional evaluative criterion to the example. Table 1 would be modified by adding a fifth row. The result is shown in table 2. Table 2 includes a new indicator for naive extrapolation and an absolute counterindicator for the Box-Jenkins method. Using the knowledge representation method we recommend, we would only have to add one rule with one condition for the new indicator and one rule with one condition for the new absolute counterindicator. None of the existing rules would need to be modified. Using the explicit exceptions method, we must add the new exception to each rule telling us when the Box-Jenkins method is indicated (rules 11 and 12). And if there were any absolute counterindications for naive extrapolation represented in any of the rules in the knowledge base, we would have to pick them up and add them to the new indicator for this method. Obviously, this becomes more complicated as more criteria are represented in the knowledge base.

The situation will not always be this simple. Some conditions may be counterindications in some circumstances but not in others. These specific counterindications will be added only to those positive rules that are affected. But in general the separation of pros and cons into separate rules provides a powerful schema for knowledge representation. We think it comes closer to capturing the way people actually formulate the reasons for the decisions they make.

Table 2.

<table><tr><td>Dimension</td><td>Question</td><td>Naive extrapolation</td><td>Box-Jenkins time series</td></tr><tr><td>Forecast frequency</td><td>Are frequent forecast updates needed?</td><td> $\uparrow$  CAN EASILYACCOMMODATEFREQUENT UPDATES</td><td> $\uparrow$  FORECAST CAN BESYSTEMATICALLYUPDATED EASILY</td></tr><tr><td>Computer resource requirements</td><td>Are computer capabilities limited?</td><td> $\uparrow$  COMPUTERCAPABILITIESARE NOT ESSENTIAL</td><td> $\downarrow \downarrow$  A COMPUTERIS ESSENTIAL</td></tr><tr><td>Output accuracy</td><td>Is a high level of accuracy critical?</td><td> $\downarrow$  OFTEN PROVIDES ALIMITED PRACTICALLEVEL OF ACCURACY</td><td> $\uparrow$  FREQUENTLYTHE MOST ACCURATERFOR SHORT TO MEDIUM RANGE FORECASTS</td></tr><tr><td>Forecast urgency</td><td>Is the forecast needed immediately?</td><td> $\uparrow$  RAPID RESULTSARE A STRONGADVANTAGE OFTHIS TECHNIQUE</td><td> $\downarrow$  OPERATIONALIZINGPROGRAM CAN TAKE TIME, BUT FORECAST CAN BEPRODUCED QUICKLY</td></tr><tr><td>Input antecedent</td><td>Are only limited past data available?</td><td> $\uparrow$  SOME PAST DATAARE REQUIRED, BUT EXTENDED HISTORY ISNOT ESSENTIAL</td><td> $\downarrow \downarrow$  PAST HISTORY IESSENTIAL WITH DETAILREQUIRED</td></tr></table>

Adapted from Georgoff and Murdick (1986).

Constantly revising existing rules is difficult and introduces opportunities for error. The revised rules are also longer and more difficult for those responsible for maintaining the knowledge base to understand. We suggest that it is easier to understand and use a larger number of simple rules than a smaller number of very complicated rules, especially if the complicated rules include the same conditions in different combinations.

There were difficulties involved in basing our knowledge base on the Georgoff and Murdick matrix that did not derive from our decision to use defeasible logic in the system. The cells in the matrix contain further explanations of the relationship between the evaluative criteria and the techniques, explanations that are open to interpretation. While some criteria are clearly indicators for a method, it is often difficult to tell whether the method is only indicated if some cluster of appropriate criteria are satisfied or if each criterion indicates the method independently. The correct interpretation of the instructions for using the matrix would probably produce multiple rules indicating each method, but with more than one condition in each rule. The knowledge base for FORE, which includes exactly one condition in each positive rule, is a first, rough cut at interpreting the Georgoff and Murdick matrix.

By using the cited article as the sole and undisputed source of knowledge, it is in principle possible to evaluate the prototype system by comparing its recommendations against those obtained by a user following the guidelines given in the article. In practice, the recommendations obtained using the article will probably vary from one user to another. Besides the problems of interpretation discussed in the last paragraph, it is sometimes unclear whether criteria that are counterindicators for a technique rule out the technique absolutely. And the evaluative criteria themselves are sometimes ambiguous, which forced us to make certain decisions in formulating the questions the system uses to gather information from the user.

## 6. Summary and Conclusions

We have introduced FORE, a prototype expert consultation system designed to demonstrate the feasibility of building such systems using d-Prolog, an implementation of a logic for defeasible reasoning. The business forecasting problem domain was discussed, together with three alternative approaches to problem solution: absolute reasoning systems, probabilistic and fuzzy reasoning systems, and nonmonotonic reasoning systems. We proposed that, for this problem domain, a non-monotonic reasoning system is the appropriate solution. To extend those concepts, Prolog, a well-known logic programming language, was introduced as an example of an absolute reasoning inference engine. Then d-Prolog, a language that extends Prolog's syntax and inference engine to accommodate defeasible reasoning, was introduced. Finally, the prototype FORE was discussed in detail. Examples of the absolute rules and the controlling defeasible metarules were given and explained.

FORE represents a significant effort to develop a system for selecting a business forecasting method, but much more work is required to turn it into a truly useful system. Additional analysis of the Georgoff and Murdick procedure is needed. At the same time, the knowledge base should be expanded to include more forecasting methods, more evaluative dimensions, and additional heuristics. The user interface should be expanded to include an enhanced explanatory facility and to allow easier system modification by the knowledge engineer.

While extensive comparison with the original Georgoff and Murdick procedure will undoubtedly uncover difficulties with FORE, the system can be verified fully in another sense. In its current stage of development FORE is intended to demonstrate the feasibility of using defeasible reasoning and d-Prolog to implement systems where the reasoning process is inherently nonmonotonic. With this goal in mind, the real question is not whether FORE is a completely adequate implementation of the Georgoff and Murdick procedure, but whether the control mechanism provided by our small set of defeasible rules gives us the recommendations we expect given our interpretation of the Georgoff and Murdick matrix. Using this criterion, FORE is successful.

FORE suggests two goals for further research. The first is to integrate defeasible logic into a mature tool for expert system development. One feature of such a tool would be an explanatory facility that not only explains why it makes a recommendation, but also gives meaningful answers to inquiries about why it does not make some alternative recommendation. The second goal is to develop a mature knowledge base for forecasting method selection. We believe that this second goal will be easier to reach using defeasible logic. $^{4}$

## References

Bates, J. and M. Granger, The Combination of Forecasts, Operations Research Quarterly 20 (1969) 451–468.

Clocksin, W.F. and C.S. Mellish, Programming in Prolog, 2nd edition (Springer Verlag, Berlin, 1984).

Geffner, Hector, On the Logic of Defaults, Proc. AAAI-88: The Seventh National Conference on Artificial Intelligence (Morgan Kaufmann, Los Angeles, CA, 1988).

Geffner, Hector and Judea Pearl, A Framework for Reasoning with Defaults, TR-94b (Cognitive Systems Laboratory, UCLA, October 1987).

Georgoff, D.M. and R.G. Murdick, Manager's Guide to Forecasting, Harvard Business Review (January–February 1986) 110–120.

Hanks, Steve and Drew McDermott, Nonmonotonic Logic and Temporal Projection, Artificial Intelligence 33 (1987) 379–412.

Holden, K. and D.A. Peel, An Empirical Investigation of Combinations of Economic Forecasts, Journal of Forecasting (October–December 1986) 229–242.

4 Source code for a version of d-Prolog that runs under the Arity/Prolog interpreter on the IBM-PC is available for a \$15 distribution fee (check made out to ARTIFICIAL INTELLIGENCE PROGRAM DEVELOPMENT FUND or purchase order). The source code is in standard Edinburgh syntax and easily adaptable to run under other Prolog implementations. Three research reports, including Nute and Lewis (1986), and a set of sample d-Prolog knowledge bases accompany d-Prolog. Anyone interested in receiving source code for FORE may request it at the same time d-Prolog is requested. There is no additional distribution fee for FORE. Please write d-Prolog Distribution, Artificial Intelligence Programs, 111 Graduate Studies Research Center, The University of Georgia, Athens, GA 30602, USA.

Jarrett, J., Business Forecasting Methods (Basil Blackwell Ltd., Oxford, 1987).

Kumar, S. and C. Hsu, An Expert System Framework for Forecasting Method Selection, Proceedings of the 21st Hawaii International Conference on System Sciences. (IEEE Computer Society Press of the IEEE, Washington, DC, 1988).

Loui, Ronald, Response to Hanks and McDermott: Temporal Evolution of Beliefs and Beliefs About Temporal Evolution, Cognitive Science 11 (1987) 303–317.

Mahmoud, E., 1984. Accuracy in Forecasting: A Survey, Journal of Forecasting (April–June 1984) 139–159.

McCarthy, John, Circumscription - A Form of Non-monotonic Reasoning, Artificial Intelligence 13 (1980) 27-39.

McCarthy, John, Applications of Circumscription to Formalizing Commonsense Knowledge, Artificial Intelligence 28 (1986) 89–116.

McDermott, Drew and Jon Doyle, Non-monotonic Logic I, Artificial Intelligence 13 (1980) 41–72.

Makridakis, S. and S.C. Wheelwright, The Handbook of Forecasting, A Manager's Guide, 4th edition (John Wiley & Sons, New York, 1987).

Nute, Donald, Defeasible reasoning and decision support systems, Decision Support Systems 4 (1988) 97–110.

Nute, Donald, Defeasible Reasoning: A Philosophical Analysis in Prolog, in: James H. Fetzer, ed., Aspects of Artificial Intelligence (Kluwer Academic Publishers, Boston, MA, 1988a).

Nute, Donald, Defeasible Logic and Temporal Projection, Proceedings of the 21st Hawaii International Conference on System Science (IEEE Computer Society Press, Washington, DC, 1989).

Nute, Donald and Michael Lewis, d-Prolog: A User's Manual, ACMC Research Report 01-0017 (University of Georgia, Athens, GA, 1986).

Nute, Donald, Robert Mann and Betty Brewer, Using Defeasible Logic to Control Selection of a Business Forecasting Method, Proceedings of the 21st Hawaii International Conference on System Science (IEEE Computer Society Press, Washington, DC, 1988).

Poole, Terry, On the Comparison of Theories: Preferring the Most Specific Explanation, Proceedings of the Ninth International Joint Conference on Artificial Intelligence (Morgan Kaufmann, Los Angeles, CA, 1985).

Wheelwright, S.C. and S. Makridakis, Forecasting Method for Management, 4th edition (John Wiley & Sons, New York, 1985).
