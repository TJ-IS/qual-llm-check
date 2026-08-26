---
otero_id: 16940
otero_key: "5GETWM9D"
title: "Solving discrete multicriteria decision problems based on logic-based decision support systems"
authors: "Han-Lin Li"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90070-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Solving Discrete Multicriteria Decision Problems Based on Logic-Based Decision Support Systems

Han-Lin LI \*

Department of Information Science, National Chiao Tung University, Hsinchu, Taiwan 30050, Republic of China

This study aims to formulate and solve discrete multicriteria decision making (D-MCDM) problems by utilizing artificial intelligent decision support systems. The major advantage of this approach is that data, functions, many D-MCDM methods, choice rules for methods, and the decision maker's preferences in D-MCDM can be integrated in a logical structure. Besides, based on the modulated D-MCDM method base and data base, the decision maker can flexibly choose suitable methods to solve decision problems. This paper first decomposes D-MCDM problems into alternative--attribute, attribute--criterion, criterion-method-recommendation and choice-method relationships, then transforms these relationships into 'Data', 'Function' and 'Rule' formats of logic-based programs. By following that, the typical D-MCDM methods as Dominant method, Lexicographic method, Weighting method, ELECTRE method, TOPSIS method and Method with fuzzy concept are coded in a PROLOG-type language in a consistent format. Some choice rules for these D-MCDM methods are then discussed. Finally, the inference process and the man-machine dialog of this system are analyzed.

Keywords: D-MCDM, DSS, PROLOG, ELECTRE, TOPSIS, AI, Production Systems, Connection Graph.

## 1. Introduction

There is an increasing awareness of the need to simultaneously identify and consider several objectives in the decision analysis, particularly for the study of large-scale systems. Multiple criteria decision making (MCDM) has then become an important field in many applications such as in resource planning, financial planning and inventory control. Discrete multiple criteria decision making (D-MCDM) is the decision situation in which the decision maker must choose among a finite number of alternatives which are evaluated on a common set of multiple criteria.

Since a real decision problem often involves numerous data, planning models and decision rules, a practically useful MCDM system must have ability to integrate versatile data, models and decision methods into data bases, model bases and method bases. Thus to allow the decision maker to flexibly extract specific data, models and decision methods to solve decision problems. Besides a successful D-MCDM system needs to have some choice rules for methods to assist the decision maker to choose suitable method(s) from a large D-MCDM method base. To achieve these goals, one of the best strategies is to combine the techniques of Artificial Intelligence (AI) and Decision Support Systems (DSS) into D-MCDM systems.

![](/api/attachments/5GETWM9D/fulltext/images/ecdcaaaa656d65af54561bf21a86ecd631673c23da66321e268fee6326752f8b.jpg)

AI is the system that exhibits the characteristics associated with the intelligence in human behavior-understanding, learning, reasoning, problem solving and so on [1]. It is convenient to utilize knowledge representation techniques in AI to represent D-MCDM decision methods and choice rules for methods. We may also use the reasoning ability of AI programs in our D-MCDM system to deduce decision based on built-in logic type D-MCDM methods. As DSS is the system composed of data bases, model bases and user-computer dialog subsystems [2], so a logic-based DSS is a DSS which has the deductive ability of integrating data, models, decision rules and recommendations into a logic structure. This deductive ability is built based on the knowledge engine techniques in AI [4].

This paper aims to present a logic-based DSS system to solve D-MCDM problems. The features of D-MCDM problems are described first. Following that, a D-MCDM type logic-based DSS is formulated. Then some typical D-MCDM methods are coded in PROLOG, a popular AI programming language, in a modular format. Following that some choice rules for D-MCDM methods are analyzed. To show the logical consistence among choice rules, D-MCDM methods and data, we then discuss the inference process of the system. Finally the man-machine dialog system is presented to demonstrate the operation of the system.

![](/api/attachments/5GETWM9D/fulltext/images/685a0e2a4a7839868784ca1f177e1bf0a112839a002e274056c15116e2cc39a3.jpg)  
Fig. 1. The D-MCDM Process.

2. Discrete Multicriteria Decision Making Processes

We may formulate the general solution process of a D-MCDM problem from a DSS aspect as in fig. 1. What D-MCDM wants to find is a list of priority of choice (PRTY) for n potential alternatives (ALT), that is, to decide

$$
D E C (A L T _ {i}, F R T Y _ {i}), \quad i \in [ 1, n ].\tag{1}
$$

This outcome is obtained by the following steps:

(1) The creation of alternative-attribute data file (ALT-ATTR)

The relationship of alternatives and their attributes can be represented in a pay off matrix ALT-ATTR with the element $a_{ij}$ which is the rating of the ith alternative on the jth attribute ( $i=1,2,\ldots,n$ and $j=1,2,\ldots,m$ ). Each row in ALT-ATTR is regarded as a 'Fact' in AI concept denoted as

$$
A L T - A T T R \left(A L T _ {i}, a _ {i 1}.. a _ {i j}.. a _ {i m}\right) \quad i \in [ 1, n ].\tag{2}
$$

(2) The identification of attribute-criterion functions (ATTR-CRIT)

The relationship among a decision criterion and attributes within an alternative is often represented by a function form. For a D-MCDM problem with q decision criteria and m attributes, the value level of the kth criterion $C_{k}$ can be expressed as the function of a set of attributes

$$
C _ {k} = C _ {k} \left(\dots , a _ {j}, \dots\right), \quad k \in [ 1, q ].\tag{3}
$$

Expression (3) can also be written as

$$
A T T R - C R _ {k} \left(\dots a _ {j}.. C _ {k}\right),\tag{4}
$$

which turns to have the form of 'Function' in AI.

(3) The derivation of alternative-criterion data file (ALT-CRIT)

Based on (2) and (3), we can derive the alternative-criterion relationship as

$$
A L T - C R I T \left(A L T _ {i}, C _ {i 1}.. C _ {i k}.. C _ {i q}\right), \quad i \in [ 1, n ],\tag{5}
$$

where $C_{ik}$ is the value level of the kth criterion for $ALT_{i}$

(4) The formulation of D-MCDM method set (CR-MD-REC)

Many current D-MCDM methods ([6], [8], [15], [16]) can be rearranged in a uniform criterion-method-recommendation(CR-MD-REC) form as

$$
\begin{array}{l} C R - M D - R E C (M E T D _ {d}, C _ {1 1}.. C _ {1 q}.. C _ {n 1}.. C _ {n q}, P R E F _ {d}, \\ P R T Y), \quad d \in [ 1, l ], \end{array} \tag {6}
$$

where $METD_{d}$ denotes dth D-MCDM method and $PREF_{d}$ represents the decision maker's preferences or subjective knowledge on criteria based on $METD_{d}$ . Expression (6) means, introducing method d, given criteria values $C_{1}..C_{q}$ and the preference information $PREF_{d}$ we can recommend priority PRTY for alternatives. These CR-MD-REC expressions of D-MCDM methods have the form of 'Rule' in AI.

(5) The development of choice rules for D-MCDM methods (CHO-METD)

Some choice rules for D-MCDM methods can be developed based on various decision environments. These rules can assist the decision maker to select a suitable method from a large D-MCDM method set. We code these choice-method rules as

$$
\begin{array}{l} C H O - M E T D \big (C H R _ {g}, S E L _ {g}, M E T D \big), \\ g \in [ 1, \gamma ], \end{array}\tag{7}
$$

where $CHR_{g}$ denotes the gth choice rule and the $SEL_{g}$ represents the decision maker's selection of method based on $CHR_{g}$ . Expression (7) means, suppose these are γ choice rules and the currently adopted rule is g, after inserting $SEL_{g}$ value, a method METD will be chosen.

(6) The specification or preferences

The decision maker specifies his preferences $(PREF_{d})$ on criteria following the method $(METD_{d})$ chosen in Step 5.

(7) The iterative decision process

The decision maker first selects a choice rule for methods. Then the system suggests one D-MCDM method, based on choice rules for methods, to solve the problem. After that, the decision maker specifies preferences following selected method. The system then integrates this method and preferences with ALT-CRIT to obtain the decision DEC. The process ends while the decision maker satisfies with the result, otherwise the process will continue iteratively.

This paper aims to formulate the general D-MCDM solution process in fig. 1 as a computer-aid decision support system shown in fig. 2. Where ALT-ATTR is stored in data bases, CRIT-ATTR in model bases. We code each D-MCDM method and choice rules for methods in logic forms to construct knowledge bases. The man-machine iterative decision process is as follows:

(1) The decision maker specifies his D-MCDM problem by creating or updating data or models.

(2) The computer will list choice rules for D-MCDM methods and help the decision maker to select a method.

(3) The decision maker chooses one D-MCDM method.

(4) The computer displays the suggested method. Based on the algorithm of chosen method, the computer requests the decision maker to specify his preferences among multiple criteria.

(5) The computer will integrate the selected method and preferences with relative data and functions to generate a tentative solution shown to the decision maker. The decision maker evaluates the solution and decides whether he will continue the process or not.

To formulate various D-MCDM method set and choice rules for methods in a uniform type of logic-based decision rules is the core issue of this intelligent D-MCDM DSS. Such formulation involves not only the logic expression of methods and choice rules but also the connection between these methods and choice rules. This expression is so-called ‘knowledge representation’ in AI terminology. The representation of knowledge is the combination of data structure and interpretive procedures which featurize ‘knowledge’ behavior. Decision rules or decision maker’s knowledge can be represented in many ways (such as Logic, Procedural, Analogical, Semantic Networks, Production Systems, Semantic Primitives and Frames). Since Production Systems have most often been used in AI programs to represent a body of knowledge [1], we apply production rules to show how decision rules are represented. Production Systems are a modular knowledge representation scheme. The basic idea of these systems is that the data structure consists of rules, called productions, in the form of condition-action pairs: ‘If this condition occurs, then do this action’. The major characteristics of the formalism are that the conditions in each rule are explicit and the interaction between rules are minimized. Since production rules facilitate human understanding and modification of systems with large amount of knowledge, such knowledge representation has been used in several large application systems like MYCIN, DENDRAL and AM [12].

![](/api/attachments/5GETWM9D/fulltext/images/e1ca2147e06b3bf621382c8e21bef2ec97c14fc8f10dc3d535f534df59bef410.jpg)  
Fig. 2. Intelligent MCDM DSS Framework.

As discussed in fig. 1 and fig. 2, four types of relationships, alternative-attribute(ALT-ATTR), criterion-attribute(CRIT-ATTR), criterion-method-recommendation(CR-MD-REC) and choice-method(CHO-METD), in the D-MCDM solution process can be specified by AI formats as 'Data', 'Function' and 'Rule'. It turns out that the decision algorithm in D-MCDM can be developed and operated by AI program (as LISP or PROLOG) conveniently.

## 3. Logic-based DSS and D-MCDM

The basic concept of a logic-based DSS, as discussed in [2], is to treat DSS as a kind of theorem-proving system in which the user's query is taken as a theorem remained to be proved from the existing axiom set. This axiom set is a combination of clauses involving data, functions and deductive rules. This logic-based approach can be illustrated, by production systems discussed above, with the following example:

'IF MODEL1(x,y) and DATA1(x,z)

and MODEL2(x1,z)

and RULE(x1,x2) THEN RECOM(y,x2)'.

The statement can be expressed in terms of first-order logic as

$$
\begin{array}{r l} & \text {   'MODEL } (x, y) \& D A T A 1 (x, z) \& M O D E L 2 (x 1, z) \\ & \& R U L E (x 1, x 2) \dashrightarrow R E C O M (y, x 2) ^ {\prime}, \end{array}
$$

where DATA1 is a data file, MODEL1 and MODEL2 are functions with inputs x and x1 respectively. RULE is a deductive rule while RECOM is a final recommendation. A typical query from users is as RECOM(?,A), i.e., to find y's value given x2 = A. To respond to this request, the theorem prover will first use A to deduce x1 values from RULE then to call function MODEL2 to obtain z values, then to select values for x in DATA1, and finally call MODEL1 to obtain y values.

Following this logic, the D-MCDM problems discussed above can be represented by three clauses in a logic-based DSS form as

$$
\begin{array}{r l} & R E C (A L T _ {i}, M E T D _ {d}, P R T Y _ {i}) \\ & \& C H O - M E T D (C H R _ {g}, S E L _ {g}, M E T D _ {g}) \\ & \& (C H R _ {g}, S E L _ {g}) \dashrightarrow D E C (A L T _ {i}, P R T Y _ {i}), \quad (8) \\ & A L T - C R I T (A L T _ {i}, C _ {i 1}.. C _ {i q}) \\ & \& \dots \& A L T - C R I T (A L T _ {j}, C _ {j 1}.. C _ {j q}) \\ & \dots \& C R - M D - R E C (M E T D _ {d}.. C _ {i 1}.. C _ {i q}.. C _ {j 1}.. C _ {j q}.. \\ & P R E F _ {d}, P R T Y _ {i}) \dashrightarrow R E C (A L T _ {i}, M E T D _ {d}, P R T Y _ {i}) \\ & \quad (9) \\ & A L T - A T T R (A L T, a _ {1}.. a _ {m}) \& A T T R - C R _ {1} (\dots a _ {j}.. C _ {1}) \\ & \& \dots \& A T T R - C R _ {q} (\dots a _ {j}.. C _ {q}) \\ & \dashrightarrow A L T - C R I T (A L T, C _ {1}.. C _ {q}). \end{array}
$$

Suppose the user's request is say $DEC(ALT_i?)$ , i.e., given $ALT_i$ to find $PRTY_i$ . This DSS will first request the decision maker to specify $CHR_g$ , $SEL_g$ values to determine $METD_d$ , as in Expression (8). Then this DSS will evaluate 'REC' predicate by first using $ALT_i$ to find other relative $ALT_j$ , $j \in [1, n]$ , and to select values for $C_{i1}..C_{iq}..C_{j1}..C_{jq}..$ from ALT-CRIT predicate which is derived from Expression (10). Then the system requests the decision maker to specify $PREF_d$ based on $METD_d$ . Finally by inserting $METD_d$ , $PREF_d$ and $C_{i1}..C_{jq}..$ into 'CR-MD-REC' predicate we can find value $PRTY_i$ . We may also find priority values for all alternatives simultaneously by replacing $ALT_i$ in DEC predicate with ALT which is the list of whole alternatives written as $DEC(ALT, PRTY)$ . Here 'CR-MD-REC' and 'CHO-METD' are the major issues of this logic-based D-MCDM DSS. We will discuss 'CR-MD-REC' in section 4 and analyze 'CHO-METD' in section 5.

Now let us clarify the term of 'priority' as: for a finite set of alternative $ALT = [ALT_1, \ldots, ALT_i, \ldots, ALT_n]$ , we define that

IF the number of alternatives which are superior to $ALT_{i}$ is 'k', and

IF the number of alternatives which can not compare with $ALT_{i}$ is ‘u’,

THEN the priority of $ALT_{i}$ , denoted as $PRTY_{i}$ , is $PRTY_{i} = 'k + 1'$ to $k + 1 + u$ .

Table 1

<table><tr><td rowspan="2">ALT</td><td colspan="3">attribute</td><td colspan="2">criterion</td><td rowspan="2">k</td><td rowspan="2">u</td><td rowspan="2">PRTY(k+1~k+1+u)</td></tr><tr><td>a1</td><td>a2</td><td>a3</td><td>c1</td><td>c2</td></tr><tr><td> $ALT_1$ </td><td>3</td><td>2</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $ALT_2$ </td><td>2</td><td>2</td><td>1</td><td>4</td><td>1</td><td>1</td><td>2</td><td>2-4</td></tr><tr><td> $ALT_3$ </td><td>2</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>2-3</td></tr><tr><td> $ALT_4$ </td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>3-4</td></tr><tr><td> $ALT_5$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>5</td></tr></table>

Consider an example of 5 alternatives ( $ALT_{1}$ to $ALT_{5}$ ), each alternative has three attributes (a1, a2, a3) as in table 1. Suppose there are two decision criteria c1 and c2 defined as $c1 = a1 + a2, c2 = a3$ . Let both criteria be benefit criteria then the precedence diagram for criteria dominance is shown in fig. 3. Obviously $ALT_{2}$ can not compare with $ALT_{3}$ and $ALT_{4}$ . Following the definition of ‘priority’ defined above, we can assign priority values to each alternative as in table 1. More analysis about PRTY can be found later in table 3.

Based on the above definition of priority, we can code predicate REC(ALT, METD, PRTY) in a PROLOG-type language as

$REC(ALT_{i}=x, METD=yy, PRTY=[zz1, zz2])$ if

Count-greater( $ALT_{i}=x,\quad ALT_{j}=1,\quad number=$ z1, METD = yy), Clause(1)

$zz1 = z1 + 1,$

Count-neither( $ALT_{i}=x,\quad ALT_{j}=1,\quad number=z2,\quad METD=yy$ ),

$zz2 = z1 + z2 + 1.$

where notation ‘,’ means ‘AND’. The predicate ‘Count-greater’ is to count, based on a given method, the number of whole alternatives $ALT_{j}$ ( $j \in [1, n]$ ) which are greater than a given alternative $ALT_{i}$ . Predicate ‘Count-neither’ is to count the number of whole alternative which can not compare with $ALT_{i}$ . Here $ALT_{j}=1$ means we compare a specific $ALT_{i}$ with each $ALT_{j}$ in order starting from the first alternative. Predicate ‘Count-greater’ is defined as

![](/api/attachments/5GETWM9D/fulltext/images/9f2972d5b66af171381ce519a7d3d878ad2e59a13e3d33abc3c64167aa4f6159.jpg)  
Fig. 3.

Count-greater( $ALT_{i}=x,\quad ALT_{j}=y,\quad number=z1,$ METD=y1) if Clause(2)

yy is $y + 1$ ,

Count-greater(x, yy, xx, y1),

(Greater $(x, y, y1)$ , $z1$ is $xx + 1$ or $z1$ is $xx$ ).

where predicate 'Greater' is used to compare alternatives $ALT_i$ and $ALT_j$ . If $ALT_i$ is superior to $ALT_j$ then $Greater = \text{true}$ and $z1$ is $xx + 1$ ; otherwise $Greater = \text{false}$ and $z1$ is $xx$ . Clause (2) recursively evaluates each 'Greater' statement between a specific $ALT_i$ and an $ALT_j$ in turn. Similarly we can define predicate 'Count-neither' as

Count-neither( $ALT_{i}=x,\quad ALT_{j}=y,\quad number=z,$ METD=m) if Clause(3)

y1 is $y + 1$ ,

Count-neither(x, y, z1, m),

(not Greater $(x, y, m)$ , not Greater $(y, x, m))$ , $z$ is $z1 + 1$ or

z is z1).

Examining Clauses (1), (2), (3), we clearly know that predicate 'Greater' is the only required information used to evaluate $REC(ALT_i, METD_d, PRTY_i)$ . Therefore based on a pairwise comparison of alternatives we can list the priority for whole alternatives. For the rest of this paper, we will translate some typical D-MCDM methods into rules which are headed by 'Greater' predicate.

## 4. D-MCDM Decision Rules

We may classify D-MCDM methods based upon different forms of preference information from the decision maker. Referring to [8], [6] a list of some typical D-MCDM methods is shown in fig. 4. The classification has been made in two parts: first, the type of information needed from the decision maker; secondly, the major methods in any branch formed from the first part. In this section, some typical D-MCDM methods, such as Dominant Method, Lexicographic Method, Simple Weighting Method, ELECTRE Method, TOPSIS Method and Method with fuzzy concept, are coded in an uniform rule style by a PROLOG-type language. The rules of selecting a method based on these methods can also be coded in PROLOG language, discussed in the next section.

## 4.1. Dominant Decision Rule (METD = 1)

For two records in ALT-CRIT file ( $ALT_{i}$ , $C_{i1}$ , $..C_{ik}..C_{iq}$ ) and ( $ALT_{j}$ , $C_{j1}..C_{jq}$ ), let all $C_{k}$ be benefit criteria, then Dominant decision method [8] states that

If $C_{ik} \geq C_{jk}, \forall k = 1,..,q$ and $C_{ig} > C_{jg} \ni g \in [1..q]$ Then $ALT_i > ALT_j$ ,

where notation ‘>’ means superior to. This rule can be written in PROLOG-type languages headed by ‘Greater’ as

Greater $(ALT_{i} = x1, ALT_{j} = x2, METD = 1)$ if

$$
A L T - C R I T (x 1, y 1, \dots , y q),
$$

$$
A L T - C R I T (x 2, z 1, \dots , z q),\tag{Clause(4}
$$

$$
y 1 \geq z 1, y 2 \geq z 2, \dots , y q \geq z q,
$$

$$
(y 1 > z 1 \text {   or   } y 2 > z 2 \text {   or   } \dots \text {   or   } y q > z q),
$$

where METD = 1 means Dominant Method is the first method in our D-MCDM method base.

## 4.2. Lexicographic Decision Rule (METD = 2)

In a certain decision environment, a single criterion seems to predominate. To treat this situation we need to compare the alternatives based on the most important attribute. The method requires the decision maker to rank criteria in the order of importance. Let $C_{1}$ be the first important criterion and $C_{k}$ be the kth important criterion, and so on. Then for the comparison of a pairwise alternative $ALT_{i}$ , $ALT_{j}$ , the Lexicographic decision rule states that [15]

If $C_{i1} > C_{j1}$ Then $ALT_{i} > ALT_{j}$ OR

If $C_{i1} = C_{j1}, C_{i2} > C_{j2}$ Then $ALT_i > ALT_j$ OR
:

$$
\text { If } C _ {i 1} = C _ {j 1}, \dots , C _ {i q - 1} = C _ {j q - 1},
$$

$C_{iq} > C_{jq}$ Then $ALT_{i} > ALT_{j}$ .

![](/api/attachments/5GETWM9D/fulltext/images/e69d74831f52b271ccf077bbad5b2e2291b650587020984cf3724072e7f1533d.jpg)  
Fig. 4. A List of Some Typical D-MCDM Methods.

The rule is written in PROLOG headed by predicate 'Greater' as

$$
\begin{array}{l} \text { Greater } (A L T _ {i} = x 1, A L T _ {j} = x 2, M E T D = 2) \text { if } \\ \quad A L T - C R I T (x 1, y 1, y 2,..., y q), \\ \quad A L T - C R I T (x 2, z 1, z 2,..., z q), \\ \quad ((y 1 > z 1; \quad \text { Clause(5) } \\ \quad (y 1 = z 1, y 2 > z 2); \\ \quad \dots \\ \quad (y 1 = z 1,..., y q - 1 = z q - 1, y q > z q)). \\ \text { where   notation   `;` means 'OR'. } \end{array}
$$

## 4.3. Simple Weighting Decision Rule (METD = 3)

The Simple Weighting Method is one of the most popular methods of MCDM. Suppose the decision maker specifies a set of importance weights to the criteria, $w = [w1, w2, \ldots, wq]$ . Then the most preferred alternative $ALT^*$ is selected such that

$$
A L T ^ {*} = \left[ A L T _ {i} \mid \underset {i} {\text { MAX }} \sum_ {k = 1} ^ {q} w _ {k} C _ {i k}, \quad \forall k \in [ 1, q ] \right].
$$

In order to facilitate the computational problems caused by the different units of $C_{k}$ in the ALT-CRIT matrix, we need to normalize criteria to obtain comparable scales. This normalization can be achieved by the linear scale transformation between criteria as

$$
\begin{array}{l} C _ {i k} ^ {r} = \frac {C _ {i k} - C _ {k} ^ {\min}}{C _ {k} ^ {\max} - C _ {k} ^ {\min}} \text { for   benefit   criteria } C _ {i k}, \\ C _ {i k} ^ {r} = \frac {C _ {k} ^ {\max} - C _ {i k}}{C _ {k} ^ {\max} - C _ {k} ^ {\min}} \text { for   cost   criteria } C _ {i k}, \end{array}
$$

where $C_{k}^{min}$ and $C_{k}^{max}$ denote the minimum and maximum kth criterion values over the whole alternatives. It is clear that the scale of measurement varies precisely from 0 to 1 for each criterion. Assuming all criteria are benefit criteria then we may utilize this formula to transfer ALT-CRIT( $ALT_{i}, C_{i1},..,C_{iq}$ ) into NOM-ALT-CRIT( $ALT_{i}, C_{i1},..,C_{iq}$ ) coded in a PROLOG-type language as Clause(6), (7a), (7b), (8) in the appendix.

## 4.4. ELECTRE Decision Rule (METD = 4)

The ELECTRE method (Elimination et Choice Translating Reality) was originally introduced by Benayoun et al. and has been developed by Roy and Nijkamp (in [8]). This method states that even though two alternatives $ALT_{i}$ and $ALT_{j}$ do not dominate each other mathematically, the decision maker accepts the risk of regarding $ALT_{i}$ as almost surely better than $ALT_{j}$ based on the degrees of satisfaction and unsatisfaction. The decision maker examines both the degree to which the preference weights are in agreement with pairwise dominance relationships (concordance set) and the degree to which weighted evaluations differ from each other (discordance set). The ELECTRE method takes the following steps:

Step 1. Calculate the normalized ALT-CRIT matrix, as in Clause(6) and (7a), (7b) in the appendix.

Step 2. Calculate the weighted normalized ALT-CRIT matrix W-NOR-ALT-CRIT as

$$
W - N O M - A L T - C R I T \left(A L T _ {i}, V _ {i 1},..., V _ {i k},..., V _ {i q}\right),
$$

where $V_{ik} = w_kC_{ik}^r$

Step 3. Determine the concordance and discordance set: For a pair of alternative $ALT_{i}$ and $ALT_{j}(i=j)$ , the set of decision criteria CRIT[1,...,k,...,q] is divided into two subsets. The concordance set $F_{ij}$ is composed of all criteria for which $ALT_{i}$ is preferred to $ALT_{j}$ , which is

$$
F _ {i j} = \left\{k \mid V _ {i k} \geq V _ {j k} \right\}.
$$

The complementary subset is called the discordance set, which is

$$
G _ {i j} = \left\{k \mid V _ {i k} \leq V _ {j k} \right\}.
$$

Step 4. Calculate the concordance and discordance indices: The concordance index is equal to the sum of the weights associated with criteria contained in the concordance set, defined as

$$
f _ {i j} = \sum_ {k \in F _ {i j}} w _ {k}.
$$

The discordance index is used to denote the degree to which $ALT_{i}$ are worse than $ALT_{j}$ , defined as

$$
g _ {i j} = \max _ {k \in G _ {i j}} \left| V _ {i k} - V _ {j k} \right| / \max _ {k \in [ 1, q ]} \left| V _ {i k} - V _ {j k} \right|.
$$

Obviously, $0 \leq f_{ij} \leq 1$ and $0 \leq g_{ij} \leq 1$ . A higher $f_{ij}$ value indicates that $ALT_{i}$ is superior to $ALT_{j}$ . A higher value of $g_{ij}$ implies that, for the discordance criteria, $ALT_{i}$ is less favorable than $ALT_{j}$ .

Step 5. Determine the concordance and discordance dominance indices: The decision maker are inquired to assign two threshold values P and Q. The decision rule of comparing the largeness of $ALT_{i}$ and $ALT_{j}$ is as

$$
\text { if   } f _ {i j} \geq P \text {   and   } g _ {i j} \leq Q \text {   then   } A L T _ {i} > A L T _ {j}.
$$

We formulate above five steps in the form of logic rules headed by the predicate 'Greater' as in Clause(9) and (10) of the appendix. Although ELECTRE method is a complicated method, we may code this method in PROLOG by a clear and compact way. To add ELECTRE method in our D-MCDM method base, we only need to edit extra Clauses(9) and (10).

## 4.5. TOPSIS Decision Rule (METD = 5)

The Technique for Order Preference by Similarity to Ideal Solution (TOPSIS), developed by Yoon and Hwang [8], was formulated based on the concept that the better alternatives have the shorter distance from the ideal solution and the further distance from the negative-ideal solution. Suppose that each criterion takes the monotonically increasing (or decreasing) utility; then the 'ideal' solution is composed of all best criteria values attainable, and the 'negative-ideal' solution composed of all worst criteria values attainable. The algorithm of TOPSIS method can be presented as following successive steps:

Step 1. Construct the weighted normalized ALT-CRIT matrix W-NOR-ALT-CRIT as

$$
W - N O M - A L A T - C R I T \left(A L T _ {i}, V _ {i 1}, \dots , V _ {i k}, \dots , V _ {i q}\right),
$$

where $V_{ik} = \omega_k C_{ik}^r, \forall i \in [1, n]$ .

Step 2. Determine ideal and negative-ideal solutions: Let the ideal solution be $A^{*}$ and the negative ideal solution be $A^{-}$ , defined respectively as

$$
\begin{array}{r l} A ^ {*} & = \left\{\max _ {i} V _ {i k} \Big | \forall i \in [ 1, n ], k \in [ 1, q ] \right\} \\ & = \left\{V _ {1} ^ {*},.., V _ {k} ^ {*},.., V _ {q} ^ {*} \right\}. \end{array}
$$

$$
\begin{array}{r l} A ^ {-} & = \left\{\min _ {i} V _ {i i} \Big | \forall i \in [ 1, n ], k \in [ 1, q ] \right\} \\ & = \left\{V _ {1} ^ {-},..., V _ {k} ^ {-},..., V _ {q} ^ {-} \right\}. \end{array}
$$

Step 3. Calculate the separation measure: The separation of each alternative from the ideal one is calculated as

$$
S _ {i} ^ {*} = \sqrt {\sum_ {k = 1} ^ {q} \left(V _ {i k} - V _ {k} ^ {*}\right) ^ {2}}.
$$

Similarly, the separation from the negative-ideal one is given as

$$
S _ {i} ^ {-} = \left| \sum_ {k = 1} ^ {q} \left(V _ {i k} - V _ {k} ^ {-}\right) ^ {2} \right|.
$$

Step 4. Calculate the relative closeness to the ideal solution: The relative closeness of $ALT_{i}$ with respect to $A^{*}$ is defined as

$$
C L _ {i} ^ {*} = S _ {i ^ {-}} / \left(S _ {i} ^ {*} + S _ {i} ^ {-}\right), \quad 0 <   C L _ {i} ^ {*} <   1.
$$

While $ALT_{i} = A^{*}$ , $CL_{i}^{*} = 1$ and $CL_{i}^{*} = 0$ if $ALT_{i} = A^{-}$ . $ALT_{i}$ is closer to $A^{*}$ as $CL_{i}^{*}$ approaches to 1.

Step 5. Rank the preference order: A set of alternatives are ranked according to the descending order of $CL_{i}^{*}$ , denoted as

$$
\begin{array}{r l} & \text { if } C L _ {i} ^ {*} > C L _ {j} ^ {*} \text { then } A L T _ {i} > A L T _ {j} \text { and } P R T Y _ {i} \\ & \quad <   P R T Y _ {j}. \end{array}
$$

The above steps can be formulated in the form of logic rules headed by the predicate 'Greater' as in Clauses(11) to (15) in the appendix. Again we find Clauses(6), (7a), (7b), (10), already edited by other methods, can be shared by TOPSIS method.

## 4.6. Fuzzy Decision Rule (METD = 6)

A fuzzy set is a set without a clear boundary [14], [11]. A fuzzy set %F (prefix by %) in a space X is characterized by a membership function f mapping from x to the interval [0, 1]. Let %A(x), %B(x) and %C(x) be fuzzy atomic formulas and a(x), b(x), c(x) be their membership functions, then the conjunction, disjunction and negation are defined as follows:

Conjunction: $\% A(x) = \% B(x)\& \% C(x)$ iff $a(x) = \min \{b(x),c(x)\} \forall x\in X.$

Disjunction: $\% A(x) = \% B(x)$ or $\% C(x)$ iff $a(x) = \max \{b(x), c(x)\} \forall x \in X$ .

Negation: $\% A(x) = -\% B(x)$ iff $a(x) = 1 - b(x)\forall x\in X.$

Due to the problems such as scaling and compatibility, it is not easy to specify the precise membership function. Referring to Chang [3], when we can do is to find some attributes so that a membership function is a monotonic increasing (decreasing) function of the attributes. In other words, we need to find an attribute x such that the membership function f satisfies the following condition:

if $x1 > x2$ then $f(x1) > f(x2)$ .

We now briefly represent some ways of writing fuzzy decision rules for D-MCDM problems. For the example of determining the priority to purchase products, let its ALT-CRIT table as a table 2(a). Suppose the decision maker's fuzzy knowledge of determining product's purchasing priority is

'The bigger the product and the better the product, the greater possibility of purchasing the product'.

This fuzzy decision rule will then contain three fuzzy concepts %BIG, %BET and %GREAT. Let 'big' and 'bet' be the membership functions of %BIG and %BET respectively and be expressed as

$$
\begin{array}{l} \text { if   } \text { quantity } (i) > \text { quantity } (j) \text { then } b i g (i) \\ \quad \succ b i g (j), \\ \text { if   } \text { quality } (i) > \text { quality } (j) \text { then } b e t (i) \succ b e t (j), \\ i, j \in [ 1, 2, 3, 4 ]. \end{array}
$$

We often use rank concept to express superior nation ‘>’. For example, $big(i) \succ big(j)$ means i alternative has higher rank than j alternative, shown in table 2(b). Since %GREAT is the conjunction of %BIG and %BET, we can define ‘Greater’, the membership function of %GREAT, as

$$
\text { if } \max \{b i g (i), b e t (i) \} > \max \{b i g (i), l e t (j) \}
$$

then Greater(i) > Greater(j).

The rule is written here while its result is in table 2(d).

$$
\begin{array}{c} \text { Greater } (A L T _ {i} = x 1, A L T _ {j} = x 2, \\ M E T D = 6) \text { if } \end{array}\tag{Clause(16}
$$

$$
\begin{array}{l} M \text {-sort} (x 1, z z 1), \\ M \text {-sort} (x 2, z z 2), \\ z z 1 > z z 2. \\ M \text {-sort} (A L T = x, r a n k = z z) \text { if } \quad C l a u s e (1 7) \\ S O R T 1 (A L T = x, q u a n t i t y = y 1, r a n k = z 1), \\ S O R T 2 (A L T = x, q u a l i t y = y 2, r a n k = z 2), \\ z z = m a x (x, z 1, z 2). \end{array}
$$

where SORT1 and SORT2 predicates are to short the whole alternatives in ALT-CRIT file based on 'quantity' and 'quality' values respectively, then rank each alternative in order. SORT1 and SORT2 are specified elsewhere. If the decision maker wants to change his decision expressed in fuzzy knowledge as: 'The bigger the product OR the better the product is, the greater possibility of purchasing the product will be'. This is the query to find the disjunction of %BIG and %BET which can be done simply by replacing zz variable in Clause(17) as $zz = \min(x, z1, z2)$ .

## 5. Some Choice Rules for D-MCDM Methods

The decision maker can select any method, from the D-MCDM method base discussed above, to solve his decision problems. However, some decision makers may need some instructions to direct him how to choose a D-MCDM method. Since different MCDM methods are introduced for different decision situations, there exists no specific choice rule. For the methods listed in fig. 4, this section suggests two sample choice rules represented by tree diagrams in fig. 5 and fig. 6. Fig. 5 shows the first choice rule for D-MCDM methods. The first question in fig. 5 asks the user whether he wants to list the possible dominant alternatives or not. If the answer to question 1 is 'YES' then Dominant Method (METD=1) is used, otherwise the follow-up questions are asked. The second question asks whether the decision criteria are fuzzy. If the answer is 'YES' then Method with fuzzy concept is used. The third

Table 2

<table><tr><td rowspan="2">ALT</td><td colspan="2">(a) ALT-CRIT</td><td rowspan="2">(b) %BIGbig</td><td rowspan="2">(c) %BETbetter</td><td rowspan="2">(d) %GREAT = %BIG&amp;%BETgreater</td></tr><tr><td>quantity</td><td>quality</td></tr><tr><td>#1</td><td>100</td><td>L</td><td>4</td><td>3</td><td>3</td></tr><tr><td>#2</td><td>120</td><td>M</td><td>3</td><td>2</td><td>2</td></tr><tr><td>#3</td><td>140</td><td>H</td><td>1</td><td>1</td><td>1</td></tr><tr><td>#4</td><td>130</td><td>M</td><td>2</td><td>2</td><td>2</td></tr></table>

![](/api/attachments/5GETWM9D/fulltext/images/2b3e92c77f87fc4fcb8fa6224d4eda731d73670337f8f2b5f235a5c6560c0b41.jpg)  
Fig. 5. First Choice Rule for D-MCDM Method.

questions asks the decision maker whether he can rank the criteria in the order of importance. If he can then be Lexicographic method is applied. The remaining three methods, i.e., Simple Weighting Method, ELECTRE Method and TOPSIS Method are the methods for assessing weights of criteria. The question 4 asks the decision maker the feature of preference information for criteria. If the decision criteria can be simply weighted then Simple Weighting Method is used. If the preference should consider the concordance and discordance dominant values the ELECTRE Method is used. TOP-SiS Method is adopted while the decision preference should consider the closeness to the ideal solution. The first choice rules for methods (CHO-METD, CHR = 1) as mentioned in expression (7), can be coded in a PROLOG-type language as

CHO-METD(CHR = 1, METD = y if Clause(18) SELECT1(y, x1, x2, x3, x4),

![](/api/attachments/5GETWM9D/fulltext/images/9935f81cc71d2798b765db2e92b44a6b1a3c65d9a17687d354dfa1a9ebdc8f94.jpg)  
Fig. 6. Second Choice Rule for D-MCDM Methods.

RESP(x1), RESP2(x2), RESP3(x3), RESP4(x4).

Where $RESPi(xi)$ , i=1 to 4 is the decision maker's response to the ith question in fig. 5. SELECT1 is a data type predicate with input x1 to x4 and output y, represented by values as

SELECT1(1, YES, -, -, -),

SELECT1(2, NO, NO, YES, -),

SELECT1(3, NO, NO, NO, 1),

SELECT1(4, NO, NO, NO, 2),

SELECT1(5, NO, NO, NO, 3),

SELECT1(6, NO, YES, -, -).

We may formulate other choice rules for D-MCDM methods based on different decision situations. For example, fig. 6 is the tree diagram of our second set of choice rules. The feature of this set of rules is that it allows the user to use more than one D-MCDM method to do compound analysis. If the decision maker prefers to using two or more methods to make decision, his answer to question 1 is '2'. Then the follow-up question (Q4) will request the decision maker to choose multiple methods for analysis. Suppose the decision maker chooses two methods (METD = p, METD = q) for compound analysis. Then the system will first evaluate two queries $REC(ALT, METD = c, ?)$ , $REC(ALT, METD = d, ?)$ and obtains the results as $REC(ALT, METD = c, PRTY(Pc, Pc))$ and $REC(ALT, METD = d, PRTY(Pd, Pd))$ . Then the compound priority of combining $METD_{c}$ and $METD_{d}$ can be calculated as

CREC[ALT, METD = (c, d),

$PRTY(\min(Pc, Pd), \max(Pc, Pd)]$ .

Take the case in table 1 for example, we can calculate the compound priority of combing Dominant Method and Simple Weighting Method as in table 3. This compound method analysis provides to the careful decision maker a more flexible way to evaluate decision results.

The choice rule in fig. 6 can be coded in a PROLOG-type language as

CHO-METD(CHR = 2, METD = y) if Clause(19)
RESPS1(1),

SELECT2(y, x2, x3),

Table 3
Compound Priority of Combining Dominant Method and Simple Weighting Method.

<table><tr><td rowspan="2">ALT</td><td colspan="3">Attribute</td><td colspan="2">Criterion</td><td colspan="3">DEC(ALT, METD = Dominant, PRTY(P1, P1&#x27;)</td><td colspan="4">DEC(ALT, METD = Simple Weighting, PRTY(P2, P2&#x27;)</td><td>CDEC(ALT, METD = (Dom M, S.W M), PRTY(P, P&#x27;)</td></tr><tr><td>a1</td><td>a2</td><td>a3</td><td>c1</td><td>c2</td><td>k1</td><td>u1</td><td>P1 = k1 + 1 ~ P1&#x27; = k1 + 1 + u1</td><td>c = (2/3)c1 + (1/3)c2</td><td>k2</td><td>u2</td><td>P2 = k2 + 1 ~ P2 = k2 + 1 + u2</td><td>P = min(P1, P2) ~ P&#x27; = max(P1&#x27;, P2&#x27;)</td></tr><tr><td>1</td><td>3</td><td>2</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td><td>1</td><td>5</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>2</td><td>1</td><td>4</td><td>1</td><td>1</td><td>2</td><td>2-4</td><td>3</td><td>1</td><td>1</td><td>2-3</td><td>2-4</td></tr><tr><td>3</td><td>2</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>2-3</td><td>3</td><td>1</td><td>1</td><td>2-3</td><td>2-3</td></tr><tr><td>4</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>3-4</td><td>2</td><td>3</td><td>0</td><td>4</td><td>3-4</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>5</td><td>0</td><td>4</td><td>0</td><td>5</td><td>5</td></tr></table>

RESPS2(x2), RESPS3(x3).

where SELECT2 data values are

SELECT2(3, 2, 1),

SELECT2(4, 2, 2),

SELECT2(5, 2, 3).

Clause(19) has a similar type as Clause(18). Where RESPSI(1) means the response to question 1 is '1'.

The compound recommendation of using multiple methods is coded as

From examining fig. 5, fig. 6, Clauses(18), (19) and (20), it is worth to note that our system can code different choice rules for D-MCDM methods in a compact and flexible style. Using this system, the user can conveniently formulate his specific D-MCDM choice rules. In fact, one of the major advantages of logic programming languages is that we can easily translate the statements in a decision tree into modulated logic rules.

## 6. The Inference Process and a Dialog System

The above six D-MCDM method rules and two choice rules can be integrated directly into a logic-based DSS to solve the D-MCDM problem. We may use a connection graph in AI [3], [1] to connect the clauses mentioned above as in fig. 7. Five components in our logic-based D-MCDM DSS shown in fig. 7 are

(1) Decision query: As $DEC(ALT, PRTY = ?)$ , it is a query of looking for the choosing priority for all alternatives.

(2) Choice rules: Composed by Clauses(18), (19) and (20). These rules are utilized to determine adopted methods based on the decision maker's choice.

(3) D-MCDM method bases: There are two kinds of method clauses in this base. The first rules are the main method clauses which are headed by predicate ‘Greater’ as Clause(4), (5), (8), (9), (11) and (16). The second rules are the common clauses shared by many methods. For example, Clause(6), (7a) and (7b) are common clauses used by Simple Weighting Method, ELECTRE Method and TOPSIS Method. Since all D-MCDM method are coded in an uniform and modular way, we may flexibly expand and update this method base. Generally, if a user wants to add a new D-MCDM method into this method base, he only needs to specify the new method's main clauses while other common clauses may be found from existing clauses in the method base.

(4) Model bases: Composed by several ATTR-CRIT formulas which are the set of functions defining the relationship between each criterion with relative attributes.

(5) Databases: Composed by ALT-ATTR data files and some parameter values of the decision maker's preference.

This inference process of evaluating a query $DEC(ALT, PRTY = ?)$ is as follows:

Step 1. The user (decision maker) first selects one set choice rules (Clause(18) or Clauses(19), (20)). Then the system requests the user to answer some questions. Based on the users responses RESP(1) to RESP(4) or RESP(1) to RESP(4)), the system recommends the D-MCDM method (METD) for solving problems.

Step 2. The system will assign METD value in Clause(1), (2) and (3) to evaluate the query REC(ALT, METD, PRTY = ?). Then the relative main method clause is called to perform the evaluation. For example if METD = 3, the system will call Clause(8), and if METD = 4, Clause(9) will be called.

Step 3. By following the main method clause called in Step 2, some common clauses and data are used to evaluate the decision query. For example if METD = 4, the inference processes of evaluating the query REC(ALT, METD = 4, PRTY = ?) are

(1) Initialize $ALT_{i} = 1$ to compute $DEC(ALT_{i} = 1, 4, ?)$ by counting Greater ( $ALT_{i} = 1$ , $ALT_{j}, 4$ ), where $j \in [1, n]$ .

(2) Based on Clause(9), the system calls W-NOM-ALT-CRIT, WEIGHT, P and Q.

![](/api/attachments/5GETWM9D/fulltext/images/6bb9e3e185ba7762c6ff7b7fb4ffc87296c09f4ac5892c5468d699ec3312dcfe.jpg)  
Fig. 7.

(3) The system then requests the decision maker to specify WEIGHT and P, Q values. These values are stored in the data base.

(4) The system calls Clause(10), then calls WEIGHT from the data base and calls NOM-ALT-CRIT in Clause(6).

(5) Following Clause(6), the system calls Clauses(7a) and (7b).

(6) ALT-CRIT values in Clauses(7a) and (7b) come from the models in the model base and the raw data file ALT-CRIT in the data base.

(7) The system extracts data records

![](/api/attachments/5GETWM9D/fulltext/images/be7c642e28e5fc99673b9b0957efc7e81e265f1d73a2e2c7038a554c4fcfbd6e.jpg)  
Fig. 8. A D-MCDM Dialog System.

ALT-ATTR(ALT $_{i}$ …), ALT-ATTR(ALT $_{j}$ …) and inputs these records into Models CR $_{1}$ ...CR $_{q}$ to generate ALT-CRIT. Inserting ALT-CRIT and WEIGHT, P and Q values, the system evaluates Clauses(7a), (7b), (6), (10), (9), (3), (2), (1) sequentially to obtain the priority value of ALT $_{1}$ (PRTY $_{1}$ ).

(8) Let $ALT_{i} = 2$ to $n$ , repeat (1) to (7) to obtain PRTY for whole alternatives.

A man-machine dialog subsystem corresponding to the connection graph of fig. 7 is depicted in fig. 8. The major functions of this subsystem are: (1) Data edit; (2) Criterion and function edit; (3) D-MCDM method edit; (4) Choice rule edit; (5) Execution. Functions (1), (2), (3) and (4) are used to create, update and manipulate separated data files, criteria, D-MCDM methods and choice rules for methods. Function (5) is directly used by the decision maker to find recommending decision.

We now take the case in table 3 for example to show the operation of this dialog system.

Step 1. Data Edit. Enter the numbers of alternatives and attributes. Then creates an alternative–attribute (ALT-ATTR) data file AAI.

Step 2. Criterion and Function Edit. Enter the ALT-ATTR file name AAI and the number of criteria. Then specifies the criterion functions. Let the name of resulting ALT-CRIT file be ACI.

Step 3. D-MCDM Methods Edit. Coding six or more D-MCDM method programs as in Clause(1) to Clause(17).

Step 4. Choice Rule Edit. Coding possible choice rules as in Clause(18) to Clause(20).

Step 5. Execution.

(5.1) Input the ALT-CRIT file name ready for use, here is 'ACI'.
(5.2) Input the identifier member of Choice Rule, here is '1' (the choice rule in fig. 5). Then the system requests the decision maker to answer a set of questions. Following the decision maker's responses, here is 'NO NO NO 1', the system recommends to use Simple Weighting Method.
(5.3) Based on Simple Weighting Method, the decision maker is requested to specify weights on criteria. Here the decision maker specifies two sets of weights.

(5.4) Finally the system merges AC1, weights on criteria with Simple Weighting Method to find solutions.

If the decision maker feels unsatisfactory with the result, he may do the following action(s):

(1) Specify his preferences on criteria again, as done in 5.3.

(2) Select another Choice Rule, or update current Choice Rules.

(3) Update ALT-ATTR data file, or reedit criterion functions.

(4) Update D-MCDM methods.

## 7. Conclusion Remarks

Compared with conventional D-MCDM methods described in [6], [8], [15], of this logic-based D-MCDM DSS have the advantages as discussed below.

(1) Uniformity: All D-MCDM methods and choice rules for methods are encoded in an uniform 'IF-THEN' form. All main clauses of methods are headed by uniform 'Greater' and 'REC' predicates. All choice rules for methods are headed by 'CHO-METD' predicate. Besides, all decision queries are represented by a uniform 'DEC' format. With its uniform structure, this system can often be more easily understood by the decision maker, and can be more conveniently developed by the planner. One of major difficulties in most of current D-MCDM methods is that each method or the choice rules for methods has different input, process and output forms. The inconsistent formats among methods greatly prohibit the integration of methods.

(2) Modularity: All data, functions, methods and choice rules within the proposed system are formulated in modular units. With the feature of modularity, this system can add, modify, or delete individual data, function, method or choice rule without affecting the remainder of the system. In other words, we may update each clause in Clause(1) to Clause(22) without causing any change in other clauses. Production systems, used in our system to represent decision methods and choice rules, have been found as the most effective way among representation techniques to minimize the interactions between rules. Because production systems facilitate human understanding and modification of systems with large amount of knowledge, it has been used in several recent large application systems. Most of conventional D-MCDM methods and systems illustrate their computer program as nonmodular or procedural representation. For nonmodular computer programs, the modification of a procedure may generally cause a series of changes of other procedure; therefore the programmer must understand the interactions of all of its pieces. Obviously that is a difficult task for which user.

(3) Integrity and Flexibility: Based on the features of uniformity and modularity of this system, choice rules, D-MCDM methods, data and functions are stored in choice rule set, method bases and data bases respectively. Elements of these bases are flexible to be accessed, expanded, manipulated and integrated according to the decision process chosen by the user. Besides, following the guide of menu (fig. 8), the user will feel easy to operate the system.

However, this system has the disadvantage of computational inefficiency, which should be overcome in further studies. The strong modularity and uniformity of methods and decision rules in this system may cause high overhead in their use in program execution. Since this system performs every reasoning by means of the match-action cycle and convey all information by means of the context data structure, it will take a long time and large memory space to evaluate a decision query. To test the effectiveness of this system, we coded the whole program by a Turbo PROLOG language on an IBM-PC AT machine. Given the size of ALT-CRIT as 8 by 5 (8 alternatives and 5 criteria), it takes around 10 minutes to evaluate a query by ELECTRE Method which requires heavier numerical computation. These experiments show that if we want to use this system to solve more complicated D-MCDM problems or want to expand this system to solve continuous-multicriteria-decision-making(C-MCDM) problems involving heavy computational burden, we need to modify the current structure of this system. One possible way of modification is, by sacrificing some of the advantages of production systems, to code D-MCDM or C-MCDM meth ods in other procedural languages (as Fortran), while choice rules for methods are still coded in the same PROLOG program. Then to create a control program between PROLOG and Fortran environments to convey information between the two subsystems. This modified system will operate as first to use the current PROLOG program to determine which method to choose. After determining the adopted method, the control program extracts selected method from a Fortran coded MCDM method base and extracts data and functions from data and model basis into working area to execute computation. It will be interesting to analyze the usefulness and limitations of this modified approach in further studies.

## Appendix

PROLOG-type programs for Simple Weighting Method

$$
N O M - A L T - C R I T
$$

$$
(A L T = x, y _ {1}, \dots , y _ {q}) \text { if }\tag{Clause(6}
$$

$$
A L T - C R I T (x, z _ {1}, \dots , z _ {q}),
$$

$$
M I N - C R I T (m _ {1}, \dots , m _ {k}, \dots m _ {q}),
$$

$$
M A X - C R I T (M _ {1},..., M _ {k},... \dot {M} _ {q}),
$$

$$
(y _ {1} \text {   is   } (z _ {1} - m _ {1}) / (M _ {1} - m _ {1}),
$$

$$
y _ {q} \text {   is   } (z _ {1} - m _ {q}) / (M _ {q} - m _ {q})),
$$

where $m_k = C_k^{\min}$ and $M_k = C_k^{\max}$ . MIN-CRIT $m_k$ is coded as

$$
A L T - C R I T (y _ {1}, y _ {1 1},.. y _ {1 q}),\tag{Clause(7a}
$$

$$
x _ {q} \text {   is   } \min (y _ {1 q},..., y _ {n q})).
$$

$$
M _ {k}
$$

$$
M A X - C R I T (x _ {1},..., x _ {q}) \text {   if   }\tag{Clause(7b}
$$

$$
(x _ {1} \text {   is   } \max (y _ {1 1},..., y _ {n 1}),
$$

$$
x _ {q} \text {   is   } \max (y _ {1 q},..., y _ {n q})).
$$

Then we can write Simple Additive Weighting decision rule to compare largeness between alternatives $ALT_{i}$ and $ALT_{j}$ :

$$
\begin{array}{l} \text { Greater } (A L T _ {i} = x 1, A L T _ {j} = x 2, M E T D = 3) \text {   if } \\ \text { NOM - ALT - CRIT } (x 1, y 1, y 2,..., y _ {q}), \\ \text { NOM - ALT - CRIT } (x 2, z 1, z 2,..., z _ {q}), \\ \text { Weight } (w 1, w 2,..., w _ {q}), \quad \text { Clause(8) } \end{array}
$$

Clause(9)

where $P, Q$ values are specified by the decision maker. W-NOM-ALT-CRIT is coded as

Clause(10)

Clause(11)

$$
+ (a _ {2} - b _ {2}) ^ {2} +.. + (a _ {q} - b _ {q}) ^ {2}).\tag{Clause(12}
$$

$$
\begin{array}{l l} \text {Ideal - solution} (u 1, u 2,..., u q) \text {if} & \text {Clause(14)} \\ W \text {-NOM - ALT - CRIT} (1, y 1 1,..., y 1 q), \\ W \text {-NOM - ALT - CRIT} (n, y n 1,..., y n q), \\ u 1 = \max (y 1 1,..., y n 1), \\ \vdots \\ u q = \max (u 1 q,..., y n q). \\ \text {Negative - solution} (v 1, v 2,..., v q) \text {if} & \text {Clause(15)} \\ W \text {-NOM - ALT - CRIT} (1, y 1 1,..., y 1 q), \\ \vdots \\ W \text {-NOM - ALT - CRIT} (n, y n 1,..., y n q), \\ v 1 = \min (y 1 1,..., y n 1), \\ \vdots \\ v 2 = \min (y 1 q,..., y n q). \end{array}
$$

## References

[1] A. Barr and E.A. Feigenbaum, eds., The Handbook of Artificial Intelligence I, II, III, Stanford University (1981).

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, NY (1981).

[3] C.L. Chang, Introduction to Artificial Intelligence, JMA Press (1985).

[4] M.C. Chen and Lawrence J. Henschen, On the Use and Internal Structure of Logic-Based Decision Support Systems, Decision Support Systems 1, No. 3 (1985).

[5] W.F. Clocksin and C.S. Mellish, Programming in Prolog, Springer-Verlag (1981).

[6] A. Goicoechea and D.R. Hansen and L. Duckstein, Multi-objective Decision Analysis with Eng. and Business Applications (1982).

[7] G.A. Gorry and R.B. Knumland, in: L. Bennett, ed., Artificial Intelligence Research and Decision Support Systems, Addison-Wesley (1983).

[8] C. Hwang and K. Yoon, Multiple Attribute Decision Making, Springer-Verlag (1981).

[9] H.-L. Li, To Build a Data-Knowledge Base Management System by Utilizing RDBMS, Information Science and Engineering 2, No. 1 (1986).

[10] H.-L. Li, To Design a Data-Knowledge Base System in Micro-Computers, Journal of Policy and Information Systems 10, No. 1 (1986).

[11] C.V. Negoita, Expert System and Fuzzy Systems, Benjamin/Cumming, Inc. (1985).

[12] E. Rich, Artificial Intelligence, McGraw-Hill (1983).

[13] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ (1982).

[14] L. Zadeh, Making Computers Think Live People, IEEE Spectrum, August (1984).

[15] M. Zeleny, Multiple Criteria Decision Making, McGraw Hill, New York (1982).

[16] P.L. Yu, Multiple Criteria Decision Making: Concepts, Techniques and Extensions, Plenum, New York (1985).
