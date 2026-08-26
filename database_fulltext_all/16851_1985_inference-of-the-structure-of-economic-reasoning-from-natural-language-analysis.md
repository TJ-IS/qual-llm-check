---
otero_id: 16851
otero_key: "R39FZNE5"
title: "Inference of the structure of economic reasoning from natural language analysis"
authors: "L.F. Pau"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90171-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inference of the Structure of Economic Reasoning from Natural Language Analysis

L.F. PAU

Battelle Institute, 7 route de Drize, CH-1227 Carouge, Switzerland

This paper introduces a tool for qualitative model building, based on the semi-automatic inference of the structure of specified economic reasoning by natural language analysis of descriptive texts (policy statements, articles). The applications are: assessment of the consistency of several economic analyses, construction of the structure of an econometric model. This work has being using the LISP programming language.

Keywords: Economics, Artificial intelligence, Natural language analysis, Modelling, Decision theory.

![](/api/attachments/R39FZNE5/fulltext/images/24f5fe119c3ca5348edb8a7c0240085d458fb5539f92013157b1dc30c4e30464.jpg)  
L.F. Pau is currently Senior scientist at the Battelle Memorial Institute. He has previously been on the faculty of the Technical University of Denmark, MIT, E.N.S. Télécommunications, University of Maryland. His research interests include artificial intelligence, planning, and diagnostics. He has authored five books.

North-Holland
Decision Support Systems 1 (1985) 313–321

## 1. Introduction

Quantitative econometric methods are based on the estimation of linear/non-linear, statistical, or logical relations between a number of economic variables $x = (x_{1}, \ldots, x_{n})$ , once the structure of these relations has been selected:

$$
f (x) = f \left(x _ {1}, \dots , x _ {n}\right) = 0, \epsilon \text { or   True }
$$

$0 \in \mathbb{R}^{\mathrm{P}}, \epsilon \triangleq$ statistical error

True ≜ logical value ‘True’.

In economics, a standard mathematical notation is already in extensive use for abstracting the functions f of an econometric model, without specifying the functional form, only the arguments, of each (e.g., $I = f_{1}(i, Y)$ , $M = f_{2}(Y, V, P)$ , etc.) This notation is frequently supplemented by indicating the signs of coefficients and partial derivatives (following Samuelson).

In these quantitative models, f is actually the structural representation of the equivalence relation E which states when two states $x^{1}$ and $x^{2}$ of the economy are considered equivalent:

$$
\left(x ^ {1} E x ^ {2}\right) \Leftrightarrow f \left(x ^ {1}\right) = f \left(x ^ {2}\right)
$$

However, besides the data, time horizon, and estimation problems (including the separation between exogenous and endogenous variables), the crucial difficulty in econometric model building is the selection of the functional structure as represented by f or E. And it is widely recognized that most of the debates in econometric theory are centered around the comparison of model structures.

At the same time, it must be realized that so-called ‘verbal’ economic analysis derives some strength from a much wider range of possible formulations of economic reasoning in terms of causality relations. Such causality relations have a wider meaning than explicit dependence, and sensitivity coefficients. Also, the range or sophistication of possible economic policies which can be modelled quantitatively, tends to be limited.

Therefore, without a way to assess the relative merits of quantitative and ‘verbal’ economic analyses, there is an urgent need to find tools which will help bridge the gap and enhance the quality of econometric model structures.

This paper proposes an entirely new approach [16] of an exploratory nature, which precedes the econometric or control theoretical model building. It consists in considering natural language understanding and formal language concepts, to infer semi-automatically the structure f from the processing of verbal/descriptive texts describing the corresponding economic reasoning (policy statements, verbal economic analyses, press articles, speeches, position papers, ...). In other words, the models like $I = f_{1}(i, Y)$ , etc. are extracted from natural language text (in words) with no equations.

At the same time, whereas the quantitative representation of policy goals or criteria has also proven difficult, these goals can now be represented by causal relations, and linked directly to the model structure in a unified way.

In this new approach, one specifies a number of basic economic policy terms (endogeneous aggregates, exogenous variables, instrument variables), of comparison relations among these, which will all be considered as primitive syntactic symbols. Each sentence in the text to be analyzed is then viewed as the result of a sequence of production rules concatenating these primitives into such sentences. By a manual procedure (on a word processor), the original text is first abstracted to include these primitives only, with proper additional symbols. Next, an automatic grammatical inference algorithm written in LISP will derive from this abstract, wl.at were the production rules involved and especially how they were linked together via non-primitive terms. Combining inference with parsing, the result is a grammar characterizing the economic reasoning process. This process or grammar can also be represented in graph form, the nodes being the states of the grammar, and the arc labels the production rules. One specific economic reasoning is then displayed as a path in this graph, and it shows very clearly causality relations, including distributed feedback effects.

![](/api/attachments/R39FZNE5/fulltext/images/e1650b99c2cd3170403a3900fac31435c42ead8978b6eb9c07da766e60018d89.jpg)  
Figure 1. Inference of Econometric Languages from Natural Language.

Whereas recently a number of works have been dealing with natural language understanding in general $[3,4,9,14,17,24]$ , with language query systems, or with compilers for econometric model building, there is no known reference dealing with economic applications as described above and in [16]. Our approach is also different from algebraic symbol manipulations, and from the extraction of predetermined terms in econometric equations represented by a tree [15,23].

It must be stressed that more evolved and complex natural language analysis schemes are known today $[1,2,5,21]$ . The primary emphasis of this paper is however to define a problem, and describe a solution which, although semi-automatic and imperfect, is quite useful even for large texts (see section 7). The same point of view has been used in other application areas $[11,20]$ .

Sections 2 and 3 deal with a brief introduction to formal languages and their inference, as applied to econometric models. The way in which the economic reasoning language is specified is described in section 4. The semi-automatic inference algorithm is presented in section 5, with an example in section 6. The applications of this approach are reviewed in section 7.

![](/api/attachments/R39FZNE5/fulltext/images/acbbf38858e63f9a3312bec42d901ccd8e647fceebd9e9631dc30843fffd93b6.jpg)

Languages used: Higher level declarative languages

Inference: Truth maintenance / coherence checking
w.r.t. grammar G, with backtracking in case of new rules

![](/api/attachments/R39FZNE5/fulltext/images/27452ee1b8e228650bd1fa51ef9b44b8882f84a8546f5372fd7d89a34f143632.jpg)  
Figure 2. Inference by Artificial Intelligence Economic Expert System.

2. Inference of the Econometric Model Structure

## 2.1. Econometric Model

If we define:

$X \triangleq$ exogeneous variables;

$Y \triangleq$ endogeneous variables (state variables, simultaneous variables);

$U \triangleq$ instrument variables

$\theta \triangleq$ model parameters

the simplest econometric model is represented by:

(i) Criterion

(ii) Model

$$
\begin{array}{l} \text { Max } J (Y, U) \\ F (X, Y, U, \theta) = 0 \\ \text { or } \epsilon \end{array}
$$

(iii) Measurement equation

(iv) Feedback policy

$$
U = P (Y, \theta)
$$

(v) Constraints

$$
(Y, U) \in \mathbb {K}
$$

## 2.2. Qualitative Model

The qualitative model will be defined in terms of a sequence of causality relations (with feedbacks) between the notions $X, Y, U$ , merged into states $S \triangleq (X, Y, U)$ . A state $S$ is either one of the notions $X, Y, U$ or an attributed syntactic expression of these; a causality relation $\Rightarrow$ signifies that the second state $S_j$ is a consequence of the first state $S_i$ :

$$
S _ {i} \Rightarrow S _ {j}\tag{1}
$$

## 2.3. Inference of the Model Structure

The purpose of this inference is to identify the structures of the criterion J, of the model F, of the measurement H, and of the feedback policy P. By this identification, we express the fact that J, F, H, P do not imply quantitatively any causality relation between states S which is not already in the qualitative model derived from the original text used as learning.

## 3. Formal Languages

The theory of formal languages is used here to manipulate the symbols representing the states S [7,8,22,25]. The language $L(G)$ is defined by:

(i) A terminal vocabulary, $V_{\mathsf{T}} \triangleq (S_1, S_2, \ldots)$

(ii) A non-terminal vocabulary, $V_{\mathbb{N}} \triangleq (A_1, A_2, \ldots, A_n)$

(iii) An initial symbol, $\sigma$

(iv) A grammar G represented by a set of production rules, by which the string of concatenated symbols on the left is rewritten into the string on the right:

$$
\begin{array}{l l}\alpha \stackrel {{Z _ {i}}} {{\rightarrow}} \beta&(\text { also   noted } \alpha \stackrel {{i}} {{\rightarrow}} \beta)\\\alpha , \beta \in (V _ {\mathrm{T}} U V _ {\mathrm{N}}) ^ {*}&(\text { set   of   mixed   strings   of }\\&\text { symbols   from } V _ {\mathrm{T}} \text { and }\\&V _ {\mathrm{N}})\end{array}
$$

Because the terminal vocabulary $V_{T}$ is in our application a set of economic states, the production rules will specify exactly the causality relations between these states.

The language $L(G)$ is then the set of strings $x \in V_{T}^{*}$ of terminal symbols, derived from $\sigma$ by a sequence of production rules:

$$
L (G) = \left(x \in V _ {T} ^ {*}, \sigma^ {Z _ {1}, Z _ {2} \dots , Z _ {p}} \rightarrow x\right)
$$

$L(G)$ is said to be regular iff all production rules Z are of the type:

$$
A _ {1} \xrightarrow {Z} S _ {2} A _ {3} \text { or } A _ {1} \xrightarrow {Z} S _ {2}
$$

The language is context-free if all production rules are of the type:

$$
A _ {1} \stackrel {Z} {\rightarrow} \alpha \in (V _ {\mathrm{T}} U V _ {\mathrm{N}}) ^ {*}
$$

The inference of G then consists in, for given $V_{T}$ , $V_{N}$ , $\sigma$ , and within a family of feasible grammars, to infer all production rules of G from a set of learning sentences $\Delta$ (natural text after abstraction) assumed to belong to $L(G)$ . The results are:

(i) The production rules $Z_{1}, \ldots, Z_{n}$ representing $G$ ;

(ii) The sequences of production rules leading from $\sigma$ to each learning sentence in $\Delta$ ; these sequences of production rules express jointly the causality relations representing the economic reasoning underlying $\Delta$ .

4. Specification of the Economic Reasoning Language L(G)

## 4.1. Non-Terminal Vocabulary $V_{N}$

A finite number m of non-terminal symbols, $A_{1}, \ldots, A_{m}$ is specified as needed.

## 4.2. Terminal Vocabulary $V_{T}$

An automatic lexical analysis of the learning text is first carried out to estimate the frequencies of occurrence and co-occurrence of the words in $\Delta$ . The least frequent words or word co-occurrences may have to be discarded. Next, the remaining words are classified into various classes of a lexicon/thesaurus representing a relational abstraction [6,10,24,25]:

## 4.2.1. Logical Symbols

1. Quantifiers (all, set of, the, some, ...)

2. Truth functions (or, and, not, if, else, then...)

3. Punctuation (.,;)

4. Explicit causality relations:

$\Leftarrow$ (reflects, is due to), $\Rightarrow$ (implies, effect on, results in)

## 4.2.2. Uninterpreted Symbols

They are all problem dependent; all pronouns are replaced by variables:

1. Constants (2–5%, 2.03 \$, >8%, n-th quarter, high, low, stable, increasing, decreasing, ...)

2. Variables: - all endogenous variables $Y$ - all exogenous variables $X$ - all instrument variables $U$

or logical states $S_{i}$ obtained by logical combination hereof. Since all variables are treated equally, the inference system will not make any difference; the manual abstracting procedure may however add a suffix $Y$ , $X$ or $U$ to indicate the type considered.

3. Relations (equal to, greater than, indexed to)

4. Functions (plus, merger with, ...)

5. Relational applications (greater than, extreme, lagged value, forecasted value, positive impact, maximum)

## 4.3. Grammar

Described here in an informal way, all production rules considered are of the following types:

Expression → Constant/Variable

$$
\text { Variables } \rightarrow \text { Variables } / \text { Variable }
$$

$$
\text { Relational   expression } \rightarrow \text { Expression }
$$

$$
\text { Functional   expression } \rightarrow \text { Expression }
$$

$$
\text { Truth   expression } \rightarrow \text { Expression }
$$

$$
\text { Causality   expression } \rightarrow \text { Expression }
$$

$$
\text { Quantifier - Variables } \rightarrow \text { Quantifier - }
$$

$$
\text { Variables } / \text { Variables }
$$

Constant/Relation-Expression → Expression

The grammar G of the language $L(G)$ will be represented in a graph-like structure. The arcs of the graph are the production rules, with as nodes the legal strings from $(V_{\mathrm{T}}UV_{\mathrm{N}})^{*}$ . The vocabulary $V_{T}$ and grammar G may be specified in a high level language of a compiler and parser is available (INTERLISP, PROLOG, ATN) (e.g., see [18]).

## 5. Inference Algorithms

As indicated in the Introduction, the proposed procedure is semi-automatic, as currently implemented.

## 5.1. Manual Coding into Terminal Vocabulary

Using the text editing system of a commercial word processor, each word in the learning text $\Delta = (x)$ is first reduced if necessary (articles, pronouns, etc.), and then codified into one of the classes of symbols in the terminal vocabulary $V_{\mathrm{T}}$ as listed in section 4.2. The easiest coding system is to add a suffix index if needed. Punctuation is accounted for, because the inference algorithm will only operate on one sentence $x \in \Delta$ at the time. This manual phase is quite fast on a word processor (e.g., 10 words/minute).

## 5.2. Automatic Inference Algorithm

The inference problem is in general quite difficult, but a few simple algorithms can be tested [7,8]. If unsuccessful, exhaustive search is possible, especially as the library of economic causal relations is not so large (e.g., 1000 production rules). The algorithm used is described in Appendix 1. It has been programmed in LISP. language (see Appendix 2).

## 5.3. Graph Representation

The inferred grammar G is represented by a graph, including its state $S_{i}$ as nodes, and where the arcs are the production rules; the bottom node is the entire learning text $\Delta$ .

## 6. Example

This small example is given for illustrative purpose only; the inference step will not be discussed, and only the result will be given.

## 6.1.Text

The sentence $x = \Delta$ is: 'A decline in factory orders reflects negative impact of high interest rates on the second quarter business activity'.

## 6.2. Terminal Vocabulary $V_{T}$

```txt
. : then
+ : and/also
⇐ : reflects, is due to
⇒ : implies, results in
2-5 : 2-5%
< 8 : < 8%
> 15 : > 15%
Trend{↘ : decreasing
↗ : increasing
= : equal, stable
∧ : high
∀ : low
Judgement{⊕ : positive impact
⊖ : negative impact
f Y : factory orders (Y)
i X : interest rates (X)
b Y : business activity (Y)
Qn : n-th quarter
```

6.3. Non-terminal vocabulary $V_{N}: A_{I}-A_{g}$

6.4. Maximal grammar G (see Fig. 3)

$$
1 \sim 1 ^ {\prime}
$$

$$
\begin{array}{l c l} \sigma & \xrightarrow {1} & A _ {1}. i x \Rightarrow A _ {2} \\ \sigma & \xrightarrow {1 ^ {\prime}} & A _ {2} \Leftarrow A _ {1}. i X \\ A _ {2} & \xrightarrow {5} & \odot A _ {3} b Y A _ {4} \\ & \xrightarrow {6} & \oplus A _ {3} b Y A _ {5} \\ & \xrightarrow {7} & = A _ {3} b Y A _ {6} \\ A _ {4} & \xrightarrow {8} & \Rightarrow A _ {7}. f Y \\ A _ {5} & \xrightarrow {9} & \Rightarrow A _ {8}. f Y \\ A _ {6} & \xrightarrow {1 0} & \Rightarrow A _ {9}. f Y \\ A _ {1} & \xrightarrow {2} & \pi \\ & \xrightarrow {3} & = \\ & \xrightarrow {4} & \searrow \\ A _ {7} & \xrightarrow {1 1} & \searrow \\ & \xrightarrow {1 2} & A _ {1} \\ & \xrightarrow {1 3} & \nearrow \\ A _ {3} & \xrightarrow {1 6} & Q _ {1} \\ & \xrightarrow {1 7} & Q _ {2} \\ & \xrightarrow {1 8} & Q _ {3} \\ & \xrightarrow {1 9} & Q _ {4} \\ A _ {8} & \xrightarrow {1 4} & A _ {7} \\ A _ {9} & \xrightarrow {1 5} & A _ {7} \end{array}
$$

Figure 3. Maximal Grammer G.

## Table 1 -Grammar G

This grammar G includes more causality relations than present in $\Delta$ . It is maximal in the sense of including, for given $V_{T}$ , all rules acceptable in terms of the economic language family (section 4.3).

## 6.5. Inference

The learning sentence has been coded into:

$$
\mathrm{x} = \searrow \mathrm{fY} \Leftarrow = (\wedge \mathrm{iX} \Rightarrow \ominus \sigma 2. \mathrm{bY})
$$

$$
\text { or } (\neg \mathrm{iX} \Rightarrow \ominus \sigma 2. \mathrm{by}) \Rightarrow \searrow \mathrm{fY}
$$

The inference yields:

$$
\sigma \xrightarrow {1 \cdot (2 + 5 \cdot (1 7 + 8 \cdot 1 1))} x
$$

![](/api/attachments/R39FZNE5/fulltext/images/078f77394a87bf8c805fa343456734f0054fc8737bf22174fa2cd70f725d24ea.jpg)  
Figure 4.

represented by the parsing graph, or sequence of production rules, which illustrates very clearly the causality relations in this economic reasoning (see Fig. 4).

## 7. Applications of Inference of the Structure of Economic Reasoning

## 7.1. Structure of an Econometric Model

(a) In terms of the classification between exogenous/instrument variables and endogenous variables, which is often very subjective, the graph representation (sections 5.3, 6.5) of the inferred grammar G leads to the following logical rules:

(i) Exogeneous/instrument variables can only be those states $S_{i}$ represented by leaves (branch terminations) of the graph, or be those states $S_{j}$ which are connected along one open path to other exogenous/instrument variables;

(ii) Endogeneous variables are those states $S_{k}$ included in closed cycles within the graph, or which are connected along one open path to at least one exogenous/instrument variable.

(b) The criteria or goals are those endogenous states to which a relational application is attached (section 4.2.2.5).

(c) One can also infer the structure of a control low P by, e.g., finding out which endogenous variables explain (i.e., are cause of) the minimum lending rate. This is obvious from the graph, and the distinction is then very clear between monetarist rules, supply oriented rules, Keynesian rules and their variants.

## 7.2. Consistency of an Economic Reasoning

If two texts $\Delta_{1}$ , $\Delta_{2}$ discuss the same issue, and must be consistent, this consistency can easily be checked by analyzing and matching the corresponding graphs. An example hereof is the preparation of position papers or in negotiations. Tests were carried out on texts of up to 9000 words, with automatic graph matching computation.

## 7.3. Comparison of Two Economic Reasonings

If two texts $\Delta_{1}, \Delta_{2}$ use the same terminal vocabulary and class of grammar, but are written by two different experts, one can compare through the corresponding graphs the structure of their reasonings in an almost visual way. Such a test has been conducted on four texts of 3000 words about monetary policy.

## 7.4. Forecasting

Assuming now consistency in the reasoning, the graph may help synthesize economic analyses for various assumptions on the exogenous and instrument variables. This has been tested on a learning text of 4000 words with 550 production rules, dealing with relative currency adjustments.

## 8. LISP Implementation

It includes:

(a) A manual procedure, on a word processor, whereby the descriptive text is abstracted into the terminal and non-terminal symbols of the formal grammar (see section 5.1);

(b) An automatic parsing of the concatenated strings of symbols;

(c) An automatic inference algorithm (assuming a regular grammar), which will create the production rules involved, and show how they were linked together via non-primitive terms (see section 5.2 and Appendix 1);

(d) A display of the causal semantic network, for the editing of the nodes, edges, and labels, as well as for specifying a judgmental forecast (see section 5.3);

(e) An interface to the estimation algorithm which generates all allowed paths between two specified sets of nodes.

## 9. Conclusion

This research is based on two essential remarks. First, language is an instrument of human reason, and not merely a medium for the expression of thought.

Next, qualitative/‘verbal’ economic reasoning is often more convincing to decision makers than uncertain numerical forecasts or computations, especially when medium/long-term actions are debated. Perhaps econometric models reinforce the relative weight of short term decisions, while qualitative analyses help in the preparation of longer term decisions.

At the same time, these qualitative reasonings/analyses tend to be inconsistent, and sometimes subjective. Thus need for an analytical tool to discriminate subjective evaluation elements from quantified objective factors [12], while relating the two. This paper has tried to contribute to that.

## Appendix 1

## Inference Algorithm

## 1. Regular Grammar

If $G$ is regular of type 3 (see Section 3), three algorithms are available; they are based on the theorems of Kleene and l'Etoile, which state that there is an integer $N$ such that for all $x \in L(G)$

$|x| > N, x$ can broken down into $x = uvw$ with $uv^k w \in L(G), k \notin |\mathbf{N}| -$

## 1. Algorithm 1:

(i) Find subsequences $v$ such that $x = uv^k w, k \geq 2$ for all sentences $x$ in $\Delta$ .

(ii) Repeat i for various decompositions of u, w in x.

2. Algorithm 2: Compute for increasing values of k, the maximal canonic language; compute the equivalence classes, until all sentences x are produced by such a grammar.

3. Algorithm 3: If there are variable repetitions of the same sub sequence v in the learning string $x \in \Delta$ , then the following procedure is proposed instead of Algorithm 1. It is based on the concept of successor of different symbols which appear in the strings of $\Delta$ .

Let us consider the set $M \triangleq (V_{\mathrm{T}} U(\lambda))$ , $\lambda$ being a symbol whose length is nil, and define a set Q from a bijective mapping $\gamma$ from M into Q:

$$
q _ {i} \triangleq \gamma (a _ {i}), q _ {i} \in Q, a _ {i} \in M
$$

For each element $q_{i} \in Q$ , a set $Sq_{i}$ is defined such as:

$$
S q _ {i} \triangleq (a \in M | \exists \delta , \Omega \in V _ {r} ^ {*}, \delta a _ {i} a \Omega \in \Delta)
$$

$Sq_{i}$ is the set of elements of M which are the successors of $a_{i}$ in the strings of $\Delta$ . Two states $q_{i}$ and $q_{j}$ are said equivalent if:

$$
S q _ {i} = S q _ {j}
$$

Let $Q'$ be the set of equivalence classes $q_i'$ of $Q$ . For each element $q_i' \in Q'$ , a set $Tq_i'$ is defined such as:

$$
T q _ {i} ^ {\prime} \triangleq (a \in M \mid a = \gamma^ {- 1} (q _ {j}), \forall q _ {j} \in q _ {i} ^ {\prime})
$$

$Tq_{j}^{\prime}$ is the set of elements of $M$ which are the antecedents of the elements $a \in Sq_{i}^{\prime} \triangleq (U_{k}(Sq_{k}), q_{k} \in q_{i}^{\prime})$ . Then, $\eta, R$ and $q_{0}^{\prime}$ are defined as follows:

$$
\begin{array}{l l} (i) & \eta \colon Q ^ {\prime} x V _ {T} \to Q ^ {\prime} \\ & \eta (q _ {i} ^ {\prime}, \alpha \in S q _ {i} ^ {\prime}) \triangleq (q _ {j} ^ {\prime} | \alpha \in T q _ {j} ^ {\prime}) \\ & \eta (q _ {i} ^ {\prime}, \alpha \notin S q _ {i} ^ {\prime}) \triangleq q _ {\phi} (\text { fail   state }) \end{array}
$$

(ii) $R \triangleq (q_i' \mid \lambda \in Sq_i')$

(iii) $q_0^{\prime} = (q_j^{\prime}|\lambda \in Tq_j^{\prime})$

The inferred automaton is $(Q', V_{\mathrm{T}}, \eta, q_{0}', R)$ ; it is deterministic and minimal and Card $(Q') \leq (\text{Card } (V_{\mathrm{T}}) + 1)$ .

## 2. Non-Regular Grammars

The parsing must then use an exhaustive search in the language L, with reduction based on the structure outlined in section 4.3 and on the preliminary remark in this section. In such a case, and if available, one can also use one of the simple inference algorithms for augmented transition networks (ATN).

## References

[1] ACL, Association for Computational Linguistics, annual meetings.

[2] Bara, B.G. ed. Natural Language Processing, North-Holland, Amsterdam, New York (1984).

[3] Bobrow, D. and A. Collins, Representation and Understanding, Academic Press, New York (1975).

[4] Burton, R., Semantic grammars, PhD thesis, UC Irvine, CA (1976),

[5] Cercone, N. Ed. Computational linguistics, Pergamon Oxford (1983).

[6] Charniak, E. and Y. Wilks, Computational Semantics, North-Holland, Amsterdam, New York (1976).

[7] Fu, K.S. and R. Booth, Grammatical inference, IEEE Trans. Vol. SMC-5, pt 1 (Jan. 1975); pt 2 (July 1975).

[8] Hays-Roth, F. Pattern Directed Inference. Academic Press, New York (1978).

[9] Hayes, J.E., D. Michie and L.I. Mikulich, (Ed.) Machine Intelligence, Wiley, New York (1979).

[10] Iversen, K.E., Notation as a tool of thought, Commun. ACM 23 (Aug. 1980) 444.

[11] Johnson, W., The role of prior knowledge in the comprehension of simple technical text, NTIS (1982) AD-A-115638.

[12] Jensen, A., Personal communication about Johan Voght-Norway (1982).

[13] Marcus, M.P. An overview of a theory of syntactic recognition for Natural language, AI Memo 531 MIT (July 1979).

[14] Marcus, M.P. A Theory of Syntactic Recognition for natural Languages, (Parsifal parsing) MIT Press, Cambridge MA (1980).

[15] NG, E.W. (Ed.) Symbolic and algebraic computation, EUROSAM-79, Springer, Berlin (1979).

[16] Pau. L.F., Inference of the structure of economic reasoning from natural language analysis, Society for Economic Dynamics and Control, Copenhagen (June 1981).

[17] Rescher, N., Plausible Reasoning. Van Gorcum Publ., Amsterdam (1976).

[18] Roos, J.L., Semantic recognition of econometric models with syntactic automata, Proc. COMPSTAT 1982, pt II (Short papers), Physica-Verlag, Vienna (1982).

[19] Roos, J.L., Les automates formels appliqués à l'étude et à la classification des modèles économétriques, RAIRO 17 (1983) No. 2.

[20] Rowley, M.B., Foundations for the development of a single natural language interface NTIS (1982) AD-A-112866.

[21] Siekmann, J. (Ed.) Automation of Reasoning, Springer, Berlin (1983).

[22] Shortliffe, E., MYCIN: A Computer-Based Medical Consultation System, Elsevier/North-Holland, Amsterdam, New York (1976).

[23] Steward, D.W., Partitioning and tearing systems of equations. SIAM J. Numerical Analysis (1965) Vol. 2.

[24] Winograd, T. Understanding Natural Language, Academic Press, New York (1972).

[25] Woods, 1970.
