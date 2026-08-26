---
otero_id: 16963
otero_key: "TGDZFUKE"
title: "A natural language discourse model to explain linear programming models and solutions"
authors: "Harvey J Greenberg"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90104-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Natural Language Discourse Model to Explain Linear Programming Models and Solutions

Harvey J. GREENBERG

University of Colorado at Denver, Denver, CO 80202, USA

This paper presents a natural language (i.e., English) discourse model to explain a linear programming model and, possibly, its computed solution (which need not be optimal). Drawing from earlier syntactic translations, a semantic model is presented, based on economic input-output relations commonly found in large-scale linear programs. These are then shown how to form rule-driven explanations, which comprises a fundamental component of an intelligent mathematical programming system.

Keywords: Linear Programming, Discourse Models, Natural Language Processing, Mathematical Modeling, Artificial Intelligence, Model Management, Computer-assisted Analysis.

![](/api/attachments/TGDZFUKE/fulltext/images/e581ed9cd1e6ea5acb928106623d801e69ebcbf3907e8b131560e15c757e9b45.jpg)

Harvey J. Greenberg received his Ph.D. in operations research from the Johns Hopkins University in 1968. He joined the Faculty of Computer Science and Operations Research at Southern Methodist University. Having also been Associate Professor of Computer Science at Virginia Polytechnic Institute and senior analyst with the U.S. Department of Energy, Dr. Greenberg is currently Professor of Mathematics at the University of Colorado at Denver. With more than

50 research papers and 4 coedited books, Dr. Greenberg has developed computer-assisted analysis (CAA) for mathematical programming, incorporating methods of artificial intelligence. In 1986 this body of work was awarded the ORSA/Computer Science Technical Section's Prize for contributions to the interfaces between operations research and computer science. Currently, Dr. Greenberg is developing an 'Intelligent Mathematical Programming System' using natural language and graphics to assist building and analyzing mathematical programming models for decision support.

## 1. Introduction

The objective of a discourse model is to communicate with a user, to which we add: in a manner that is most natural for him or her. Here we present an English language discourse model to explain linear programming models and their solutions, which has been implemented in a computer-assisted analysis system, ANALYZE [5,6,7], and, we describe how this forms one fundamental component of an intelligent mathematical programming system.

One effort to use natural language input for LP model specification was by Shen and Krulee [16], but we consider here the computer composition of natural language output to explain the properties of the model and solution results. Although this may be used during model formulation, the current implementation is designed for use after a standard matrix file is created. For postoptimal analysis, a method used by Marge and Shaw [12] exploits the structure of the assignment model and focuses on particular queries, such as why some other assignment was suboptimal. Here we aim for generality, using a syntax to form a basis for translations.

In many cases syntax alone is inadequate, so a semantic model is presented using the economics of activity input-output (IO) relations, into which linear programming was born. Although this too has limits, some examples are presented to demonstrate how this at least partially fulfills the objective of a discourse model. To deal with more general situations, current research is extending the IO model to incorporate a graph-theoretic framework, like that of Sowa [17], combined with a propositional analysis model, like those given in van Dijk and Kintsch [2]. Unlike these general models, our goal is to focus on LP modeling and analysis: the discourse model need not be any broader in scope than its applications.

Also of future interest is the use of graphics since this is within our basic objective. One early suggestion for use of graphics for model formulation and documentation was by Mäller-Mehrbach [13], and this was used by Holvid [9]. More recently, Fischer, Greenfield and Jaikumar [3] and Greenfield [8] have used graphics to explain results. Both approaches are iconic and could be integrated into a natural language discourse model.

Since the results described here comprise the discourse model in the current version of ANALYZE (which is much enhanced over the earlier version given in [5]), a brief summary of its salient features seems appropriate.

The ANALYZE system was born from a need to analyze LP models and their solutions at the U.S. Department Of Energy. Early focus was simply on interactive query to enable experts to navigate quickly through the model in order to debug a run or, more generally, probe into the meaning of a solution. Increased demands for model verification, documentation, simplification and deeper analysis created the need for greater automation to extract ‘causal substructures’ that are forcing, redundant, infeasible or support an explanation of some particular interest, depending upon the application. This resulted in a fast, friendly conversational system with a collection of algorithms and heuristics to find causal substructures applicable to address a wide variety of questions.

From the capability of finding causal substructures came the need to explain them to non-experts, such as new personnel or middle management, giving rise to a discourse model built from a syntactic description of rows and columns using naming conventions created during matrix generation.

ANALYZE requires a matrix file as its input. Optionally, it accepts a solution file (else, defaults to the 'all logical basis') and a syntax file. The latter is needed to support natural language discourse, and it is one of the integrating links with CAMPS [11,7]. Due to the intrinsic auto-documentation capability of CAMPS, generation of the syntax file was not difficult to implement, which is illustrated in fig. 1.

Details of CAMPS can be found in the references, but it is no more complex than other table-driven languages for LP modeling (for example [19,18]). The structure of the syntax file, which we shall illustrate in the next section, is so simple that integration with any matrix generator can be done with no greater difficulty than parsing the modeler's comments.

![](/api/attachments/TGDZFUKE/fulltext/images/6c8cdbc99bd2a4314903467719bc4e20922d6e642216d562949b564801fa25ca.jpg)  
Fig. 1. CAMPS-ANALYZE Integration.

In addition to presenting the discourse models currently implemented, we describe a foundation for extended discourse. Our longterm aim in doing so is to develop an intelligent mathematical programming system of which natural language discourse is a fundamental part.

The rest of this paper is divided into three sections. Section 2 describes the syntax model currently implemented in ANALYZE and presents an abstraction to form the basis for a general schema. Section 3 describes the IO semantics model currently implemented in ANALYZE, and, section 4 presents avenues for further research, with particular focus on rule-driven models, where the basic syntax and semantic models can be applied to more complex situations.

## 2. Syntax

## 2.1. Syntax maps

We begin with a syntactic description of the rows (i.e., constraints) and columns (i.e., activities) of an LP model, using syntax maps introduced by Greenberg [5].

One modeling system, namely, CAMPS [11,7] passes syntax maps for the rows of the model. For example, suppose there is only one row class (material balance), given by

$\mathbf{M}:=[\text{balances}]\& \text{MT23 in } \& \text{LO45.}$

Here ‘balances’ could be omitted, as ANALYZE can infer this from the fact that each row in this class, i.e., whose name begins with M, is an equation with zero right-hand side. This separation is a necessary element of the row translation rule, &rt, which we shall define shortly, as we shall want to drop the verb ‘balances’ when using the syntactic translation as part of a semantic model.

Note that the syntax map is a mixture of literals (in this case 'in') and entity references (in this case &MT23 and &LO45). The modeling system provides tables to decode materials (MT) and locations (LO) from the row name by using characters 2–3 and 4–5, respectively. For example, let these entity tables be:

<table><tr><td>MT material</td></tr><tr><td>CO crude oil</td></tr><tr><td>DS distillate oil</td></tr><tr><td>RS residual oil</td></tr><tr><td>LO location</td></tr><tr><td>TX Texas</td></tr><tr><td>LA Louisiana</td></tr><tr><td>NE Northeast</td></tr></table>

Now let the LP matrix be:

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>A</td><td></td></tr><tr><td>MCOTX</td><td>+</td><td>+</td><td>+</td><td></td><td>-</td><td>-</td><td></td><td></td><td>-</td><td>-</td><td>= 0</td></tr><tr><td>MCOLA</td><td></td><td>+</td><td></td><td></td><td></td><td></td><td>-</td><td></td><td>-</td><td>-</td><td>= 0</td></tr><tr><td>MCONE</td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td>-</td><td>= 0</td></tr><tr><td>MRSNE</td><td></td><td></td><td>+</td><td></td><td></td><td></td><td>+</td><td>-</td><td></td><td>+</td><td>= 0</td></tr><tr><td>MDSNE</td><td></td><td></td><td></td><td>-</td><td></td><td>+</td><td>+</td><td>-</td><td>+</td><td>+</td><td>= 0</td></tr></table>

A syntactic translation of each row is done by using the syntax map with simple table lookup to compose the English descriptions:

Row MCOTX balances crude oil in Texas,
Row MCOLA balances crude oil in Louisiana,
Row MCONE balances crude oil in Northeast,
Row MRNSE balances residual oil in Northeast,
Row MDSNE balances distillate oil in Northeast.

In general, the syntax map for a row or column provides a direct translation by simple table lookup. It may be regarded as a template, exogenously supplied, composed of literals and entity references. The inclusion of a semantically translated verb, like 'balances', is a minor point here, except that we want the row translation rule, &rt, to separate a translation of the entities references with prepositions, say, suitably included.

The current implementation has the template Row $N_{i}$ &vt(i) &rt(i),

where $N_{i}$ is the name of row i; &vt(i) is the verb translation rule applied to row i; and, &rt(i) is the row translation rule applied to row i using the syntax map as previously defined. We now explain

Fig. 2  
Verb Translation Rule.

<table><tr><td>Type</td><td>Right-hand side</td><td>Fixed activity level</td><td>Verb (&amp;vt)</td></tr><tr><td rowspan="5">&lt;</td><td>-</td><td>n/a</td><td>demands</td></tr><tr><td>+</td><td>n/a</td><td>supplies</td></tr><tr><td>0</td><td>-</td><td>supplies</td></tr><tr><td></td><td>0</td><td>balances</td></tr><tr><td></td><td>+</td><td>demands</td></tr><tr><td rowspan="5">=</td><td>-</td><td>n/a</td><td>supplies</td></tr><tr><td>+</td><td>n/a</td><td>demands</td></tr><tr><td>0</td><td>-</td><td>demands</td></tr><tr><td></td><td>0</td><td>balances</td></tr><tr><td></td><td>+</td><td>supplies</td></tr><tr><td rowspan="5">&gt;</td><td>-</td><td>n/a</td><td>supplies</td></tr><tr><td>+</td><td>n/a</td><td>demands</td></tr><tr><td>0</td><td>-</td><td>demands</td></tr><tr><td></td><td>0</td><td>balances</td></tr><tr><td></td><td>+</td><td>supplies</td></tr></table>

the verb translation rule.

Each row is classified by its type (i.e., inequality or equation) and the sign of its right-hand side; and, if its right-hand side is zero, by the total value of its fixed activities. The table in fig. 2 gives this translation rule in extensive form, where the verb &vt(i) is from the set {supplies, demands, balances}.

The verb translation rule has the symmetric property: multiplication of an inequality row by -1 (and reversal of inequality) produces the same verb translation. This is not so for an equation, and the translation depends on the formulator's specification. ANALYZE has a signing convention that uses a (benchmark) solution if available to sign an equation by the sign of its optimal dual price. The interrogation of the fixed activity level contribution to the row value imparts another form of symmetry: the use of fixed activities to represent exogenous supplies and demands produces the same translation as the equivalent use of a nonzero right-hand side.

In addition to translating individual rows (or columns) by syntax, we can translate a collection, say a class, by substituting 'some' instead of a particular entity lookup where an entity reference appears in the syntax map. For example, the collection of all rows in our example translates to:

Rows that begin with M balance some material in some location.

More generally, let R be a set of rows with the same syntax map (i.e., names all begin with the same letter), say

$$
\mathbf {L} _ {1} \& \mathbf {E} _ {1} \mathbf {L} _ {2} [ \dots ]
$$

The literals $L_{1}$ are left alone, and the entity references, say $E_{1}$ , are substituted with ‘some’ &ET, where &ET is a translation of the entity class. (In our example &MT translates to ‘material’ and &LO translates to ‘location’.) Thus, the template for a class translation rule is:

Rows CD&VT $L_{1}$ some &ET( $E_{1}$ ) $L_{2}$

$$
\text { some } \& \mathrm{ET} (\mathrm{E} _ {2}) \dots
$$

where CD is the class description (e.g., 'that begin with M'), and &VT is the class verb translation rule.

The class verb translation rule is simply &vt if all rows in the class have the same verb translation. Otherwise, a more general verb is used, like 'constrains'. (Presently, this aspect is under study; early use of syntactic class translation, as a direct extension of individual translation, did not encounter this difficulty because classes formed naturally with rows having the same verb translation rule.) We shall return to this point of syntactic class extension for the general model in the next section.

## 2.2. General entity model

Now let us build a general syntactic translation rule, based on the notion that each row references entities. In particular, let $E_{1}, E_{2}, \ldots, E_{K}$ denote K entities, like regions, materials, time periods, etc. Let $E = E_{1} \times E_{2} \times \ldots \times E_{K}$ be the entity space, and define the handle as a function,

## H: $N \rightarrow E$ ,

where N is the set of admissible names (i.e., presently this is an 8-character string with some restrictions on the character set). Thus, if row i has name $N_{i}$ , $\mathrm{H}(N_{i})$ gives a product of entities referenced in the name. We include in each $E_{k}$ the null reference, which applies when a row does not reference the kth entity. Note the syntax map induces a handle function, which may thus be regarded as a special case of representation, by scanning the syntax map for entity references.

Each entity, $E_{k}$ , has a prephrase $\mathbf{P}(E_{k})$ , like a preposition. Then, for each non-null entity of a handle, H, we define the phrase $\mathrm{P}(E_{k})\&\mathrm{t}(e_{k})$ , where ‘&’ denotes concatenation with a blank inserted and $\mathrm{t}(e_{k})$ is the translation of entity value $e_{k}$ (in $E_{k}$ ). The row translation rule is then vt(type, level)&ht(H(N)), where vt is the (intrinsic) verb translation rule with arguments type (i.e., <, =, >) and level (i.e., rhs if nonzero; else, minus the total fixed activity level); ht is the handle translation rule with argument equal to the handle of the name of the row, H(N). The handle translation rule is the string,

$$
\operatorname{et} \left(E _ {1}, e _ {1}\right) \& \operatorname{et} \left(E _ {2}, e _ {2}\right) \& \dots \& \operatorname{et} \left(E _ {K}, e _ {K}\right),
$$

where et $(E_{k}, e_{k})$ is the primitive entity translation rule given by $\mathbf{P}(E_{k})\&\mathbf{t}(e_{k})$ if $e_{k}$ is not the null reference and is null if $e_{k}$ is the null reference.

The syntactic class translation rule is an extension of this as follows. Let $T(E_{k})$ be the translation of the entity set $E_{k}$ . Then, suppose a set of names have non-null entity references for exactly the same set of entities. We shall say that such a collection of names comprise a name class. In this case the class handle translation, say HT, is given by

$$
\operatorname{ET} \left(E _ {1}, e _ {1}\right) \& \dots \& \operatorname{ET} \left(E _ {K}, e _ {K}\right),
$$

where ET is the following extension of et. If $e_{k}$ is the null reference, ET is the null string; if $e_{k}$ is \* (a special character not in the alphabet of names), ET is $\mathrm{P}(E_{k})\&$ ‘some’ &T( $E_{k}$ ); if $e_{k}$ is non-null reference in $E_{k}$ , ET is et (i.e., all members of the class reference the same entity value).

We now extend this to allow operations over entities. The handle function is extended whereby the kth entity reference can be an operation, like SUM or some general aggregation. If the image has operation op in its kth entity reference, the prephase PO(op) is assumed to exist. In this case the translations for both individual rows and columns and for name classes is exactly the same. For example, suppose a row accounts for the sum of labor in a region. Using labor and region as entities, the handle is (SUM, r), where SUM is the operation indication over labor (entity $E_{1}$ ) and r is a particular region ( $e_{2}$ ). Then, for PO(SUM) = 'sums' and P( $E_{2}$ ) = 'in', we would have the handle translation:

sums labor in r.

The extended class translation is:

sums labor in some region.

This abstraction of the syntax map, implemented in ANALYZE, plus the extension to operations form a basis for model specification with subsequent management and operation functions in mind. This offers an approach not only to explain the model, but also to bring out the syntactic components needed, so the input specifications can be designed along the same lines. Moreover, this provides a complement to innovative approaches to computer-assisted formulation, like Geoffrion's structured modeling [4], Welch's practitioners' approach [WE85], and Murphy and Stohr's expert system [14,15].

## 3. Semantics

## 3.1. IO semantics

We suppose a canonical form where an activity's sign pattern connotes inputs and outputs.

Continuing to view each row as a product of entities, an activity's input (i.e., negative coefficient) consumes or demands each entity; and, an output (i.e., positive coefficient) produces or supplies each entity of the row. To help fix ideas consider the translation in fig. 3.

This translation is achieved by a sequence of rules, based on the IO pattern of an activity. The numbers of inputs and outputs is determined, resulting in one of 9 IO classes according to the class translation table, shown in fig. 4.

Fig. 3  
Example of IO Semantic Translation.

<table><tr><td>Activity</td><td>IO Explanation</td></tr><tr><td>1</td><td>produces crude oil in Texas</td></tr><tr><td>2</td><td>produces crude oil in Texas and Louisiana</td></tr><tr><td>3</td><td>produces crude oil in Texas and residual oil in North-east</td></tr><tr><td>4</td><td>consumes distillate oil in Northeast</td></tr><tr><td>5</td><td>transfers crude oil in Texas to Northeast</td></tr><tr><td>6</td><td>transfers crude oil in Texas to distillate oil in North-east</td></tr><tr><td>7</td><td>blends crude oil in Louisiana into residual oil and distillate oil in Northeast</td></tr><tr><td>8</td><td>consumes residual oil and distillate oil in Northeast</td></tr><tr><td>9</td><td>distributes crude oil in Texas and Louisiana to distill- late oil in Northeast</td></tr><tr><td>A</td><td>consumes crude oil in Texas, Louisiana and North-east; and, produces residual oil and distillate oil in Northeast</td></tr></table>

Fig. 4  
IO Class Translation Table.

<table><tr><td rowspan="2">Number of inputs</td><td colspan="3">Number of outputs</td></tr><tr><td>0</td><td>1</td><td>&gt;1</td></tr><tr><td>0</td><td>N</td><td>P</td><td>P</td></tr><tr><td>1</td><td>C</td><td>T</td><td>D</td></tr><tr><td>&gt;1</td><td>C</td><td>B</td><td>M</td></tr></table>

N := is null,  
P := produces &rt (output),  
C := consumes &rt (input),  
T := transfers &rt (input) to &rt (output),  
B := blends &rt (input) into &rt (output),  
D := distributes &rt (input) to &rt (output),  
M := consumes &rt (input); l and, produces &rt (output),  
$\& \operatorname{rt}(i) := \langle \text{row translation of row } i \rangle$ (with compounding).

The first part of the IO semantic model is to apply the translation rules of fig. 4 to individual activities in the LP. (Dually, this applies to rows.) Now we consider IO classes.

Whereas IO classification of an activity for its individual translation is determined by its number of positive and negative coefficient values in the rows, class pattern formation is based on entities referenced by the rows. In particular, define an activity's entity lists, I and O, which each contain one of 3 values for each entity in the LP model: $\langle nil\rangle$ , \* or $\langle code\rangle$ . The lists are initialized to $\langle nil\rangle$ (for each entity), and the activity's nonzeroes are interrogated. For a positive value (+) in row i, its handle determines which entities are produced by this activity (this is done with the syntax map in ANALYZE). Suppose, for example, we look at activity 5 in our example, which has + in row MCONE. We consider CO a material (MT) output and NE a location (LO) output; so, O(MT) and O(LO) are affected. Similarly, when a negative value (-) is in row i, its handle determines which entries of I are affected. In our example, I(MT) and I(LO) are affected. Fig. 5 gives the complete entity lists for the example. Once the entity lists are formed, the IO Pattern is defined by the table in Fig. 6.

This gives the final IO pattern for the example:

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>A</td></tr><tr><td>MT</td><td>+</td><td>+</td><td>S</td><td>-</td><td>.</td><td>T</td><td>B</td><td>C</td><td>T</td><td>B</td></tr><tr><td>LO</td><td>+</td><td>S</td><td>S</td><td>-</td><td>T</td><td>T</td><td>T</td><td>-</td><td>D</td><td>D</td></tr></table>

Fig. 5  
IO Entity Lists for Example.

<table><tr><td rowspan="2"></td><td colspan="2">1</td><td colspan="2">2</td><td colspan="2">3</td><td colspan="2">4</td><td colspan="2">5</td><td colspan="2">6</td><td colspan="2">7</td><td colspan="2">8</td><td colspan="2">9</td><td colspan="2">A</td></tr><tr><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td><td>I</td><td>O</td></tr><tr><td>MT</td><td colspan="2">CO</td><td colspan="2">CO</td><td>*</td><td colspan="2">DS</td><td>CO</td><td>CO</td><td>CO</td><td>RS</td><td>CO</td><td>*</td><td>*</td><td></td><td>CO</td><td>DS</td><td>CO</td><td>*</td><td></td></tr><tr><td>LO</td><td colspan="2">TX</td><td colspan="2">*</td><td>*</td><td colspan="2">NE</td><td>TX</td><td>NE</td><td>TX</td><td>NE</td><td>LA</td><td>NE</td><td>NE</td><td></td><td>*</td><td>NE</td><td>*</td><td>NE</td><td></td></tr></table>

Each pattern has a template, giving a class translation rule based on IO semantics. Fig. 7 gives the translation for the example, using the above IO pattern table. Note that, for K entities, there are potentially $K^{10}$ activity classes with this approach, which is combinatorially explosive if we try to compose a separate template for each of these. The implementation, however, is additive, not multiplicative, in that there are no more than 10K templates because the translations are composed by their parts separately. In fact, only 10 templates plus a composition rule is needed to yield translations, as given in fig. 7. (Note: here the 10 activities define their own class; in general, a class will contain many activities.) To get the complete IO translations shown in fig. 7 a form of compounding was used. That is, consider activity class 1. Initial concatenation of the entity IO translations, shown in fig. 4 is:

## supplies 1 material and supplies 1 location

(inserting 'and'). The final translation rule first recognizes the redundancy. The rule is to eliminate redundant use of the same verb, in this case

Fig. 6  
Entity IO Pattern Table.

<table><tr><td rowspan="2">I</td><td colspan="3">O</td></tr><tr><td> $\langle nil\rangle$ </td><td>*</td><td> $\langle code\rangle$ </td></tr><tr><td> $\langle nil\rangle$ </td><td> $\langle nil\rangle$ </td><td>S</td><td>+</td></tr><tr><td>*</td><td>C</td><td>*</td><td>D</td></tr><tr><td> $\langle code\rangle$ </td><td>-</td><td>B</td><td>. if EQT if NE</td></tr></table>

S: = 'supplies multiple' &T( $E_{k}$ )  
+: = 'supp'ies 1' &T( $E_{k}$ )  
C: = 'consumes multiple' &T( $E_{k}$ )  
B: = 'blends' &T( $E_{k}$ )

\- : = 'consumes 1' &T( $E_{k}$ )

D: = 'distributes' &T( $E_{k}$ )

∴ = ‘for some (fixed)' &T( $E_{k}$ )

T: = 'transfers' & T ( $E_{k}$ )

$(T(E_k): = \text{translation of entity } E_k)$

'supplies'. Further, 'in' was inserted as the prephrase of 'location', replacing 'and' when forming the final discourse, shown in fig. 7.

It is important to recognize that the text composition stems from the syntax map, making the final description problem-specific, but the rules for text composition are intrinsic, which is how we can provide general support. Moreover, the fixed words, like supplies, consumes, transfers and blends, could be put into an object-oriented framework. The main point here is that for many models words like these are descriptive and aid understanding.

## 3.2. Examples of Analysis

Here we illustrate the discourse models with examples of analysis using LP problems described elsewhere.

Let us begin with a production and distribution model, called TANGLEWOOD, taken from Jensen and Barnes [10] and used by others to illustrate new approaches to computer-assisted modeling [4,19,1,7]. We shall first analyze the original version, which has an optimal solution.

Fig. 7  
IO Class Translations for Example.

<table><tr><td>Activity class</td><td>Explanation</td></tr><tr><td>1</td><td>supplies 1 material in 1 location</td></tr><tr><td>2</td><td>supplies 1 material in multiple locations</td></tr><tr><td>3</td><td>supplies multiple materials in multiple locations</td></tr><tr><td>4</td><td>consumes 1 material in 1 location</td></tr><tr><td>5</td><td>transfers location for some (fixed) material</td></tr><tr><td>6</td><td>transfers material in some location to some (other) material in some (other) location</td></tr><tr><td>7</td><td>blends materials and transfers location</td></tr><tr><td>8</td><td>consumes multiple materials and distributes loca-tions</td></tr><tr><td>9</td><td>transfers material and distributes locations</td></tr><tr><td>A</td><td>blends materials and distributes locations</td></tr></table>

Fig. 8  
A Discovered Redundant Constraint in TANGLEWOOD.

<table><tr><td>CCCC</td></tr><tr><td>HHHH</td></tr><tr><td>WWWW</td></tr><tr><td>AAAA</td></tr><tr><td>CHNS</td></tr><tr><td>HOEA</td></tr><tr><td>MPWA + + + + &gt; 0</td></tr></table>

This may be to audit the model or just to try to become familiar with it. After reading in the matrix file, we execute the ANALYZE command that searches for qualitative inferences that may be of importance. In particular, ANALYZE finds a redundant constraint, namely row MPWA, which is pictured in fig. 8.

Note that it was possible to detect the redundancy by the sign pattern alone; the magnitudes of the coefficients are irrelevant. We now want to know what these rows and columns mean. Fig. 9 shows a dialogue from this point, which we next explain.

Line 1 is the ANALYZE system prompt for a command input from the terminal, and line 2 asks for an explanation of the row just pictured, namely MPWA in fig. 8. The explanation is a straightforward syntactic translation using the syntax map shown in fig. 10, which was put into the syntax file by CAMPS.

The syntax file, as shown in fig. 10, begins with the row syntax maps. (Lines with \* in column 1 are merely comments that may appear in any input file to ANALYZE.) To translate row MPWA, ANALYZE fetches the row class whose

```txt
1 ANALYZE
2 EXPLAIN ROW
3 Row MPWA demands min amount produced for Washington.
4 ANALYZE
5 EXPLAIN COLUMN CHWACH
6 Activity CHWACH consumes 1 unit of stock for
7 Washington, 1 unit of max customer demand for
8 Chicago and 1 unit of max amount shipped for
9 Washington; and, it produces 1 unit of min
10 customer demand for Chicago and 1 unit of min
11 amount produced for Washington.
12 ANALYZE
13 PICTURE
14 C
15 H
16 W
17 A
18 C
19 H
20 BSWA = = 0
21 CLCH + > +
22 MPWA + > 0
23 PR + = MIN
24 THCH - > -
25 XPWA - > -
26 ANALYZE
27 EXPLAIN COL PIC?
28 There are 2 activity classes, according to IO:
29 Class 1 supplies 1 timber merchant for some (fixed)
30 wood plant & chair retailer...there are 16
31 activities whose names all match CH****
32 Class 2 supplies 1 timber merchant & wood plant &
33 chair retailer...there are 8 activities whose names
34 all match WO****
35 Picture of Activity IO Classes
36 ----
37 1 2
38 ----
39 timber merchant + +
40 wood plant . +
41 chair retailer . +
```  
Fig. 9. ANALYZE Dialogue for Optimal TANGLEWOOD.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
* The following comprise the syntax maps for 6 row classes
W min amount shipped for &amp;TI34
M min amount produced for &amp;WO34
X max amount produced for &amp;WO34
C min customer demand for &amp;CH34
T max customer demand for &amp;CH34
B stock for &amp;WO34
* :$\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($ $\)\($\(\)
TABLES ...the following define the 3 entity tables
*
TI timber merchant
ON Ontario
QU Quebec
WO wood plant
WA Washington
PH Philadelphia
DE Denver
BU Buffalo
CH chair retailer
NE New York
HO Houston
SA San Francisco
CH Chicago
ENDATA
</div>

Fig. 10. Syntax /File created by CAMPS for TANGLEWOOD.

name begins with the letter M, which note has the syntax map:

M := min amount produced for &WO34.

The entity reference, &WO34, directs the EXPLAIN command of ANALYZE to the entity table WO (which represents wood plants), and tells it to use table lookup with characters 3 and 4 in the row's name. In this case we lookup the code WA in the entity table WO thus obtaining the row translation,

## &rt(MPWA)

= min amount produced for Washington.

To complete the translation, the verb 'demands' is inferred by the verb translation rule in fig. 1. This is what appears on line 3, which is the ANALYZE response to the EXPLAIN query.

Following the ANALYZE prompt on line 4, we now ask for an explanation of one of the columns, namely CHWACH. The response given in lines 6–11 is formed by IO semantics, based on the inputs (i.e., negative coefficients) and outputs (i.e., positive coefficients), as pictured in lines 14–25. The row translation rule, &rt, is used as before to fill in the meaning of each input requirement and each output of the activity.

In our example we have multiple inputs (namely, in rows BSWA, THCH and XPWA) and multiple outputs (namely, in rows CLCH and

MPWA). Note only body rows (i.e., not free rows, such as the objective) are considered. Thus, the translation table directs ANALYZE to template M. The compounding capability of the row translation rule, &rt, provides the discourse shown in lines 6–11, using the row syntax maps as illustrated.

In line 27 another form of explanation is requested, signified by the terminal? in the EXPLAIN command. This asks for an accumulation of activity classes, based on IO semantics relative to the entities defined in the syntax file (namely, TI, WO and CH). The patterns shown in the resulting IO picture in lines 35–41 are formed by a deeper inference, still from the same IO considerations as in the translation of a single column. Here, however, the underlying rules are more complex. The point is that the syntax file, which was easily generated by CAMPS, provided enough information to allow an analyst to probe into the meaning of the model.

Now let us consider an infeasible scenario of TANGLEWOOD, devised to illustrate the use of explanation in debugging. The successive reduction methods in ANALYZE failed to detect infeasibility, so automatic diagnosis was unsuccessful (a modified procedure is under development, based on flow considerations that would diagnose the infeasibility in this case). Fig. 11 shows how the explanation aided interactive diagnosis by informing the analyst about supplies and demands.

<table><tr><td>1</td><td colspan="6">ANALYZE</td></tr><tr><td>2</td><td colspan="6">EXPLAIN ROWS?</td></tr><tr><td>3</td><td>Rows that begin with</td><td colspan="5">W=min amount shipped for some timber merchant</td></tr><tr><td>4</td><td></td><td colspan="5">M=min amount produced for some wood plant</td></tr><tr><td>5</td><td></td><td colspan="5">X=max amount produced for some wood plant</td></tr><tr><td>6</td><td></td><td colspan="5">C=min customer demand for some chair retailer</td></tr><tr><td>7</td><td></td><td colspan="5">T=max customer demand for some chair retailer</td></tr><tr><td>8</td><td></td><td colspan="5">B=stock for some wood plant</td></tr><tr><td>9</td><td colspan="6">ANALYZE</td></tr><tr><td>10</td><td colspan="6">* check total supply versus total demand</td></tr><tr><td>11</td><td colspan="6">ANALYZE</td></tr><tr><td>12</td><td colspan="6">ADDRIM ROW * L=0/*</td></tr><tr><td>13</td><td>Number</td><td>Level</td><td>PR</td><td>LO Bound</td><td>UP Bound</td><td>Dual Price</td></tr><tr><td>14</td><td>14</td><td>34500.0</td><td>0</td><td>36250.0</td><td>*</td><td>- 3.00</td></tr><tr><td>16</td><td colspan="6">ANALYZE</td></tr><tr><td>17</td><td colspan="6">ADDRIM ROW * U=*/99999</td></tr><tr><td>18</td><td>Number</td><td>Level</td><td>PR</td><td>LO Bound</td><td>UP Bound</td><td>Dual Price</td></tr><tr><td>19</td><td>12</td><td>5000.0</td><td>0</td><td>- *</td><td>7900.0</td><td>- 20.00</td></tr><tr><td>20</td><td colspan="6">ANALYZE</td></tr><tr><td>21</td><td colspan="6">* demand exceeds supply and is out of kilter</td></tr><tr><td>22</td><td colspan="6">ANALYZE</td></tr><tr><td>23</td><td colspan="6">DISPLAY ROW * L=7900/*</td></tr><tr><td>24</td><td rowspan="2">Name</td><td rowspan="2">Stat</td><td rowspan="2">Level</td><td rowspan="2">PR</td><td rowspan="2">LO Bound</td><td rowspan="2">UP Bound</td></tr><tr><td>25</td></tr><tr><td>26</td><td>WMON</td><td>I</td><td>13500.0</td><td>0</td><td>16000.0</td><td>*</td></tr><tr><td>27</td><td>WMQU</td><td>L</td><td>16000.0</td><td>0</td><td>16000.0</td><td>*</td></tr><tr><td>28</td><td colspan="6">ANALYZE</td></tr><tr><td>29</td><td colspan="6">EXPLAIN</td></tr><tr><td>30</td><td colspan="6">Row WMON demands min amount shipped for Ontario</td></tr><tr><td>31</td><td colspan="6">Row WMQU demands min amount shipped for Quebec</td></tr><tr><td>32</td><td colspan="6">ANALYZE</td></tr><tr><td>33</td><td colspan="6">* the min demands for Ontario and Quebec are out of kilter!</td></tr></table>

Fig. 11. ANALYZE Dialogue to Diagnose Infeasible TANGLEWOOD.

The first explanation, in lines 3–8, translates the syntax maps, but with 'some' inserted according to the class translation rule, which extends direct syntactic translation from syntax maps. For example, note from fig. 10 that row class W translates by the template:

min amount shipped for &TI23.

Now the entity reference, &TI34, is translated 'some' &ET(TI),

where &ET(TI) is the translation of entity class TI: timber merchant. Thus, we obtain the row classes by the class translation rule, using the template induced by the syntax map.

Now the analyst sees the meanings and thinks of a supply-demand imbalance. Line 10 is a comment made by the analyst and is ignored by ANALYZE (some operating systems, like PRIMOS, allow a session to be 'logged' for later review). Now line 12 uses the ADDRIM command to add rim values of rows for which the lower bound is nonnegative (i.e., in the range 0/\*, where \* denotes infinity). Of interest is the sum total of the lower bounds, skipping rows with now lower bound (i.e., negative infinity). This displays a total demand of 36250. Then, line 17 uses AD-DRIM again to get total supply by adding the upper bounds over rows that have finite upper bounds, displaying a sum total of only 7900. (The LIST or EXPLAIN commands could be executed first to note that all coefficients are unity, so that straight summations apply.) Line 22 is another comment made by the analyst, who now recognizes the imbalance. In lines 25–28 out of kilter demands are displayed, and the diagnosis is at hand. Final explanations are given in lines 31–32, and a final comment is entered in line 34.

The foregoing examples serve not only to illustrate the discourse models implemented in ANALYZE, but also to demonstrate how the explanations aid analysis, like the infeasibility diagnosis, besides the more obvious model management functions (like documentation). Furthermore, the natural language discourse would be incorporated into the modeling system and checks for redundancy and consistency performed during formulation. The use of ANALYZE for postformulation analysis was only to illustrate the potential of discourse to improve decision support at any phase. There are, however, limitations to the scope of syntax and IO semantics alone. It is necessary to consider additional discourse to explain more complex situations. This is an avenue for further research, which we discuss next.

## 4. Avenues for Further Research

The discourse model implemented in ANALYZE addresses a fundamental need in linear programming model management and analysis, and the underlying concepts and methods extend to other modeling frameworks. This is, however, only a first step towards building intelligence into a modeling system, and further research is needed to make such a goal a reality.

First, the general syntax model needs practical exercise (and probable refinement) to test its scope. Second, alternative semantic models need study to develop a major building block for more complex explanations. In both cases it is important to determine precisely how such discourse models affect the design of the modeling system, itself.

Third, a rule-driven discourse model is barely formulated. The idea, is to consider situations, like those described by Greenberg [6], for which the knowledge base contains a rule to direct the translation process. Much research is needed to determine the form and content of a knowledge base, which would be initially constructed during a model's formulation (or in major revision). Here learning models are appropriate, but their form and content also requires further research.

Besides the conceptual developments needed to achieve practicable ends, the issues of implementation are paramount. Information structures and fundamental algorithms (and heuristics) also require further study, including the exploitation of advanced computer architectures.

## References

[1] G.H. Bradley, Implementation of a Structured Modeling Language for Optimization, presented at the 12th Mathematical Symposium, Boston, MA (1985).

[2] T.A. van Dijk and W. Kintsch, Strategies of Discourse Comprehension (Academic Press, 1983).

[3] M. Fisher, A. Greenfield and R.A. Jaikumar, VERGIN: A Decision Support System for Vehicle Routing, Harvard Business School working paper 82–62 (1982).

[4] A.M. Geoffrion, Structured Modeling, Western Management Science Draft Manuscript, University of California at Los Angeles, Los Angeles, CA (1985).

[5] H.J. Greenberg, A Functional Description of ANALYZE: A Computer-Assisted Analysis System for Linear Programming Models, ACM TOMS 9 (1983) 18–56.

[6] H.J. Greenberg, Towards An Intelligent Mathematical Programming System, presented at the Workshop of the TIMS College on the Practice of Management Science (notes available from author) (Aug., 1985).

[7] H.J. Greenberg, C. Lucas and G. Mitra, Computer-Assisted Modelling and Analysis of Linear Programming Problems: Towards a Unified Framework, Brunel University working paper, Uxbridge (1986).

[8] A. Greenfield, Improving the User/Model Interface for Sensitivity Analysis, Ph.D. dissertation, University of Pennsylvania, Philadelphia, PA (1984).

[9] A. Holvid, Towards A Unified Method for Constructing and Implementing LP Models, CDC report 770427 (1979).

[10] P.A. Jensen and J.W. Barnes, Network Flow Programming (Wiley, 1980).

[11] C. Lucas, G. Mitra and K. Darby-Bowman, Modelling of Mathematical Programs: An Analysis of Strategy and an Outline Description of a Computer Assisted System, Brunel University working paper, Uxbridge (1985).

[12] C.R. Marge and J.J. Shaw, Explaining Optimal Solutions to an Assignment Model, Transcript SP-497, Alphatech, Inc., Burlington, MA (1985).

[13] H. Müller-Mehrbach, Graphically Illustrating LP Models, Presented at the 8-th Mathematical Programming Symposium, Budapest (1976).

[14] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Working paper GBA 85–40, New York University (1985).

[15] F.H. Murphy and E.A. Stohr, Incorporating Rules for Model Building in an Artificial Intelligence System for Formulating Linear Programs, Working paper, New York University (1986).

[16] S.N.T. Shen and G.K. Krulee, Solving Linear Programming Problems Stated in English by Computer, Proceedings of ACM (1973).

[17] J.F. Sowa, Conceptual Information Processing (North-Holland, 1975).

[18] J.S. Welch, Jr., PAM--A Practitioners' Approach to Modeling, Technical report, Ketron, Inc. (Oct., 1985).

[19] C. Witzgall and M. McClain, Problem and Data Specification for Linear Programs, U.S. National Bureau of Standards technical report (Nov., 1984).
