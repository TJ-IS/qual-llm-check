---
otero_id: 16951
otero_key: "9QQ9VS4Y"
title: "A support system for optimization modelling"
authors: "Indu Shekhar Singh; Sowmyanarayanan Sadagopan"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90075-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Support System for Optimization Modelling

Indu Shekhar SINGH
and Sowmyanarayanan SADAGOPAN
Indian Institute of Technology, Kanpur 208 016, India

With widespread use of executive decision support systems, the activity of modelling itself needs to be supported by a user friendly interface. This paper outlines an effort in this direction with respect to optimization modelling using linear programs. The approach is through a synthesis of a modelling language (LAMP) under development, for manipulating the structure, and a commercially available database management system for manipulating the data. Such a synthesis provides a very powerful 'what if' analysis capability paving the way for a new generation of modelling systems.

Keywords: Linear Programming, Decision Support, Modelling Languages, Data Management.

Indu Shekhar Singh is a Lecturer in Mechanical Engineering at Regional Institute of Technology, Jamshedpur. He graduated from Ranchi University. It was followed by a Master's Degree in Industrial Management from Indian Institute of Technology, Kanpur, where he is presently a Ph.D. student under the Quality Improvement Programme. His research interests are in the area of Modelling and Data Management.

S. Sadagopan is a Professor in Industrial Management and Engineering Programme at Indian Institute of Technology, Kanpur. He graduated from the College of Engineering, Guindy, Madras. He obtained his Masters and Doctorate degrees from Purdue University, USA. His research interests are in the areas of Modelling and Multiple Criteria Decision Making. His publications have appeared in European Journal of Operations Research, Journal of Optimization Theory and Applications and IEEE Transactions on Systems, Man and Cybernetics.

## 1. Introduction

## 1.1. Decision Support and Modelling

Decision Support Systems (DSS) represent a broad spectrum of ideas that support the executive decision processes with flexible access to data and models [17]. They represent a significant change in the attitude with which managers interact with computers. The traditional manager-computer interaction has been through data processing. It evolved slowly into the area of management information systems. Despite tremendous growth in the activities, the conventional approach had little significant impact on management. The modern approach, viz. the philosophy of decision support, interestingly, appears to have a tremendous impact on management style. The DSS approach emphasizes the fact that management involves primarily decision making and managers need a direct support, through tools and techniques, in the decision making activity. The revolution in computing in general and microcomputing in particular has helped in translating this philosophy into real life applications.

Traditionally the techniques of operations research and management science have been successfully applied to a variety of management problems. Though there were several isolated successes, they did not make a major impact. Primarily it was due to the indirect involvement of managers in the modelling processes. Thanks to the personal computer revolution, managers are increasingly getting involved in the modelling processes [3]. The silent spreadsheet modelling revolution was spearheaded by VisiCalc [4]. It has now evolved into sophisticated models like LOTUS, MULTIPLAN and IFPS [10]. This is a happy development both for managers and management scientists. In fact decision support systems and the associated modelling represent a renewed interest in OR/MS techniques [5]. It is generally felt that very soon managers will graduate into more sophisticated models including the use of OR/MS techniques, and the future decision support systems will have to address such situations. This paper outlines a possible approach to tackle such a scenario.

## 1.2. Mathematical Programming Models

We address ourselves in this paper to modelling using optimization techniques. We are convinced that optimization represents a major application technique in the entire gamut of OR/MS techniques. Several studies have vindicated this observation [18]. Among the several optimization techniques, mathematical programming represents the single most popular tool. Hence we restrict ourselves to mathematical programming models in this paper. In fact the major emphasis will be on linear programming, being the major application tool in several OR/MS studies.

Linear Programming has enjoyed a widespread acceptance in several application areas. It also enjoys an algorithm that is computationally efficient, in terms of empirical performance. The algorithm has also been efficiently implemented in the form of several computer codes that have been commercially available for many years. Added to this has been the several 'what if' analyses that have been generally possible in the form of parametric studies and sensitivity analysis. Last but not the least has been the 'ease of use' that is characteristic of the linearity of the constraints and the objective function, which appeals to the managerial community. Consequently, linear programs involving several thousands of variables and several hundreds of constraints have been traditionally solved in such diverse industries like Petroleum, Food, Transportation, Energy and the Service sector [25].

Almost all the applications of linear programming, made extensive use of computational facilities leading to several software products called LP Packages. But they primarily exploited the numerical problem solving capability of the digital computer [9]. Undoubtedly, but for the availability of computing equipment there was no possibility of the solutions. However, anyone trying to model a nontrivial problem would have realized that the very management of the model structure and model data can be very demanding. In fact unless one is very careful, he may be swarmed with the data. Since the ultimate purpose of modelling is insight and not numbers, modellers soon started looking for support in non-numeric computation as well. The early attempts in this direction were to develop matrix generators like MAGEN [7]. Very soon they were found to be inadequate and often artificial [8]. What the modeller needed was a natural interface with a high expressive power and 'ease of use'. This led to the growth of modelling languages in the recent years. The representative efforts in this direction are CML [19], LPM [14] and GAMS [2,15,18]. The modelling languages attempt to provide support in all the four stages of modelling, viz. formulation, data analysis, numerical solution and analysis of results. The traditional LP Packages concentrated primarily on the numerical solution aspect. In fact statistics show that the numerical solution does not account for more than 20 percent of the overall solution effort. Hence the evolution of modelling languages was but a natural process.

## 1.3. Our Approach

We perceive the flexibility of data and model access as the key component of decision support philosophy. The availability and affordability of personal computers have made the data accessible to managers. The technology of computer communication is extending this access to corporate data maintained at very different geographical locations as well. The development of database management systems (DBMS) offer the managers a flexible access to data.

Modelling languages, on the other hand provide a flexible access to models. We first develop a modelling language (LAMP), building on the ideas that have gone into the development of similar systems. Hopefully this will provide a basis for a new generation of model management systems. What is needed is a synthesis of the flexible access to data provided by data management and the flexible access to models provided by model management. Ultimately such a synthesis would provide support to the modelling process itself. This work is an attempt in this direction.

## 1.4. Outline of the Paper

In the next section we describe the major features of a modelling (LAMP), we have developed. We demonstrate the ideas with an agricultural example used as an illustration. We use the problem solving software LINDO [21] as the problem solver. In the third section we extend the data management capabilities of a relational Database Management System (DBMS) for data analysis, results analysis and report writing phases of model building. By using a state-of-the-art DBMS software, UNIFY [24], we avoid duplication of work that goes with the development of current generation of mathematical programming software. Also by exploiting the sophisticated power of the data management software we demonstrate an interactive analysis capability that is not attainable by the present generation of LP Packages and matrix generators. The power we obtain is not at the cost of 'ease of use' also. In fact relational data management systems and query languages enable a far more elegant way of analysis. To enable the use of relational DBMS we provides an alternate standard to the conventional MPS system [12] which is getting to be archaic [10]. The new representation once again is more elegant and can easily interface with any relational data management software. The final section mentions the major conclusions and recommendations.

## 2. Model Language LAMP

## 2.1. Introduction

Mathematical programs are expressed in one kind of form for human modellers and quite a different form for computer codes. The modellers' form is symbolic, quite readable and uses a notation native to the domain viz., constraints, variables and objectives. The algorithmic form, on the other hand, requires an explicit form, typically variable-by-variable list of nonzero coefficients. Translation from the modeler's form to the algorithmic form is thus an unavoidable task in mathematical programming based models. In the traditional approach to translation, specialized programming languages and systems called matrix generators were employed. A modern approach is to leave as much of the translation work as possible to the machine. Central to such an approach is a machine readable modelling language that expresses the mathematical program in much the same way as the modeler does. It is generally accepted that modelling languages lead to a more reliable modelling scheme often at a lower overall cost [8].

The general advantages of modelling languages are verifiability, modifiability, documentability, independence and simplicity. Each one of them represent a significant advantage as observed by Fourier [8], in great detail. In the light of the above advantages several prototype modelling languages have been under development, for example, UIMP, MGRW, LPM, GAMS, CML and ALPS [6,11,14,15,19,23] in the recent years. LAMP was developed at IIT Kanpur both as a vehicle for teaching/research and to try out our ideas on the synthesis of flexible data and model access, which in our view constitutes the central theme of decision support systems.

## 2.2. Design Goals

The following features were adopted as the design goals in our implementation. They were arrived at after extensive study of the existing systems under development elsewhere. The major emphasis, however, was on proving the ideas and not on the development of a software product, which calls for much larger manpower investment of a different skill. The design goals were as follows:

(i) The declarative language must be

symbolic - most problem elements representable using mnemonic symbols.

general - ability to define most of the linear programs; extendable to integer and nonlinear programs.

understandable - a natural form easily comprehended by the user.

(ii) The system must be sufficiently ‘user friendly’.

(iii) The system must be usable on any interactive terminal with a limited standard keyboard character set.

(iv) The system must meet at least the following features with reference to linear programs:

(a) Symbolic identification of constraint, variables, RHS, objectives.

(b) Grouping of variables, constraints.

(c) Indexing expressions.

(d) Ability to parametrically specify constraints, variables.

(e) Blending constraints.

(f) Special features like bounds, time lag/lead.

(g) Interface with standard problem solving software for LP and a standard DBMS software.

## 2.3. Implementation

## 2.3.1. Introduction

The LAMP system has been implemented on DEC-10 system at IIT Kanpur. Most of the code is written in PASCAL [13]. The exercise has been primarily to prove the ideas, rather than developing a full fledged software product. Hence the diagnostic capabilities of the model are limited. The system has, however, been well tested.

The LAMP system uses LINDO [21] and GINO [16] as problem solving software for linear and nonlinear programs respectively. The data management software is the product UNIFY [24] that runs on a unix based machiner UPTRON S-32, available at IIT Kanpur which is networked to the DEC-10 machine.

The actual model building is in two stages, model structure definition and model data definition. In the first stage, one defines the terminology and then the abstract structure of the model using a simple syntax detailed in section 2.3.2. In the model data definition phase the data are generated by executing the model structure with the data on files to produce the actual data for interfacing to a problem solving software. The format of the generated data is an industry standard MPS file [12] as well as a relational format, which we believe would be the future generation standard.

Full details of implementation are available in [22]. The main features are briefly described below.

## 2.3.2. The Syntax

The syntax of LAMP has been kept close to the way mathematical programs are typically written by most modellers. The summation symbol has been replaced by 'SUM' to enable one to use LAMP even with ordinary terminals. The other parts of the language use natural symbols.

The basic building block is an atom, a group of atoms constitute a molecule. Molecules are typically used as index variables. A typical example would be the molecule 'month' consisting of atoms 'January', 'February' and 'March'. The variables, constraints and objective function are built out of identifiers which may be scalar or arrays, indexed over the molecules. To provide maximum flexibility LAMP allows different molecules to have common atoms and provides automatic evaluation of cartesian products for summation. LAMP also provides for variables to appear on the right-hand side when it is natural to modelling. Multi-level indexing of identifiers, multiple terms and parametric terms are also permitted by LAMP. The values corresponding to coefficient identifiers are stored in file (possibly obtained from corporate database of the organization through the use of some datamanagement software) and the matrix generated at the time of execution of LAMP. LAMP provides for automatic generation of coefficients in the case of specially structured constraints, such as bounds, simple or generalized.

Every effort has been taken to keep the representation as natural as possible. For example, a typical constraint set could be

SUM[MONTH: FERTREQ.CROP.MONTH

$$
\left. \left. * M O N T H? \right] <   = T F E R T R E Q. C R O P, \right.
$$

indicating that the fertilizer required (FERTREQ) summed over all the months must be limited to the total fertilizer required (TFERTREQ) for every crop. The coefficients indicating the fertilizer requirement come from the indexed identifier, FERTREQ.CROP.MONTH. The molecule name to the left of the symbol ‘:’, i.e., MONTH, represents the summation set. The decision variables are indicated by MONTH?. It may be noted that the model structure is independent of data, i.e., the structure of the constraint set would be independent of the number of months considered for planning.

The detailed syntax of the language in standard EBNF form [13] is given in fig. 1.

## 2.3.3. Main Features

The main features of the LAMP system are as follows:

(i) Indexed Constraints. LAMP allows a simple definition of constraints indexed by one or more molecules, permitting multi-level indexing (up to three levels are permitted in the current implementation).

Example:

SUM[CROP:LABORREQ.CROP.MONTH

$$
\left. \left. * C R O P? \right] <   = L A B O R A V L. M O N T H. \right.
$$

<table><tr><td colspan="2">metasymbol</td><td>Meaning</td></tr><tr><td>=</td><td></td><td>is defined to be</td></tr><tr><td>:</td><td></td><td>alternatively</td></tr><tr><td>.</td><td></td><td>end of production</td></tr><tr><td>[X]</td><td></td><td>0 or 1 instance of X</td></tr><tr><td>(X)</td><td></td><td>0 or more instance of X</td></tr><tr><td>(X;Y)</td><td></td><td>a grouping; either X or Y</td></tr><tr><td>&quot;XYZ&quot;</td><td></td><td>the terminal symbol XYZ</td></tr><tr><td rowspan="4">Problem</td><td rowspan="4">=</td><td>“Problem”</td></tr><tr><td>Terminology</td></tr><tr><td>Objective</td></tr><tr><td>Constraint_sequence.</td></tr><tr><td rowspan="2">Terminology</td><td rowspan="2">=</td><td>Molecule_sequence</td></tr><tr><td>Identifier_sequence.</td></tr><tr><td>Molecule_sequence</td><td>=</td><td>Molecule_definition“eoln”{Molecule_definition“eoln)}.</td></tr><tr><td>Molecule_definition</td><td>=</td><td>Molecule_name“=”Atom_name{“,“Atom_name}.</td></tr><tr><td>Molecule_name</td><td>=</td><td>Name.</td></tr><tr><td>Atom_name</td><td>=</td><td>Name.</td></tr><tr><td>Name</td><td>=</td><td>Letter(Alphanumeric).</td></tr><tr><td>Letter</td><td>=</td><td>(&quot;a&quot;; &quot;b&quot;;..&quot;; &quot;z&quot;).</td></tr><tr><td>Alphanumeric</td><td>=</td><td>Letter; Digit.</td></tr><tr><td>Digit</td><td>=</td><td>(&quot;0&quot;; &quot;1&quot;;..&quot;; &quot;9&quot;).</td></tr><tr><td>Identifier_sequence</td><td>=</td><td>Identifier“$”“eoln”{Identifier“$”eoln”.</td></tr><tr><td>Identifier</td><td>=</td><td>Name{“.”Molecule_name”.</td></tr><tr><td>Objective</td><td>=</td><td>Operator LHS“eoln”.</td></tr><tr><td>Operator</td><td>=</td><td>(&quot;MIN&quot;; “MAX”).</td></tr><tr><td>I HS</td><td>=</td><td>Term[“+”Term_spl].</td></tr><tr><td>Term_spl</td><td>=</td><td>(Term; Parm_term).</td></tr><tr><td>Parm_term</td><td>=</td><td>Parameter Term.</td></tr><tr><td>Term</td><td>=</td><td>“[”Summation_id“:”Coefficient_id“*”Variable_id(“?”|“?”)(“”|“”)”.</td></tr><tr><td>Parameter</td><td>=</td><td>Name.</td></tr><tr><td>Summation_id</td><td>=</td><td>Molecule_name{“:”Molecule_name}.</td></tr><tr><td>Coefficient_id</td><td>=</td><td>Identifier.</td></tr><tr><td>Variable_id</td><td>=</td><td>(Molecule_name; Identifier).</td></tr><tr><td>Constraint_sequence</td><td>=</td><td>General-sequence{Spl_sequence}.</td></tr><tr><td>General_sequence</td><td>=</td><td>General_cons“eoln”{General_cons“eoln”}.</td></tr><tr><td>General_cons</td><td>=</td><td>“SUM”LHS(“&lt;=”;“&gt;=”;“=”)RHS.</td></tr><tr><td>RHS</td><td>=</td><td>Identifier.</td></tr><tr><td>SPl_sequence</td><td>=</td><td>Spl_cons“eoln”{Spl_cons“eoln”}.</td></tr><tr><td>Spl_cons</td><td>=</td><td>{Bounds_cons_seq}{Simple_sum_cons_seq}.</td></tr><tr><td>Bounds_cons_seq</td><td>=</td><td>Bounds_cons“eoln”{Bounds_cons“eoln”}.</td></tr><tr><td>Bounds_cons</td><td>=</td><td>(Molecule_name;identifier)“?”(“&lt;=”;“&gt;=”;“=”)RHS.</td></tr><tr><td>Simple_sum_cons_seq</td><td>=</td><td>Simple_sum_cons“eoln”{Simple_sum_cons“eoln”}.</td></tr><tr><td>Simple_sum_cons</td><td>=</td><td>“SUM”“[”Summation_id“:”Variable_id“?”“]”(“&lt;=”;“&gt;=”;“=”)RHS.</td></tr></table>

Fig. 1. EBNF Grammar for LAMP.

(ii) Sum of Terms. LAMP allows a constraint or a set of constraints to be composed of more than one symbolic term.

Example:

```txt
SUM[CROP: WATERREQ.CROP.MONTH *CROP?] + [LIVSTOCK: WATERREQ.LIVSTOCK. MONTH *LIVSTOCK?] <= TOTWATER.MONTH.
```

(iii) Sum of terms with Constant Multipliers. For parametric analysis one would like to have a provision for a constant multiplier to be included in the model. LAMP has a provision to accommodate this.

Example:

MAX[CROP: PROFIT.CROP \* CROP?]

(iv) Blending Constraints. Blending constraints can be accommodated as a special case of (iii). Example:

```txt
SUM[CROP: WATER.CROP * CROP?]
+ ALPHA[LIVSTOCK: WATER.
LIVSTOCK * LIVSTOCK?] = ZERO.
```

(v) Bounds. Most mathematical programs contain bounds. Special algorithms like bonded variable algorithms exploit this special structure. LAMP provides for bounds as a special constraint, so that the user need not provide the coefficients.

Example:

CROP? $< =$ CEILING.CROP.

(vi) Simple Summation. A good number of constraints in any mathematical program is in the form of a simple summation of a set of variables. To save the unnecessary entry of these coefficients in the data files LAMP provides for a mechanism of generating such unit coefficients automatically. Example:

```txt
SUM[CROP: CROP?] <= TOTLAND.
```

(vii) Special Features. Special features include the generation of combinatorial constraints. The cartesian product of indices can be indicated in the model structure rather than explicitly defining a molecule listing the elements of cartesian product.

Example:

$$
\begin{array}{c} \text { MIN } [ \text { ROW }: \text { COLUMN }: \text { COST }. \text { ROW }. \\ \text { COLUMN } * \text { ROW }. \text { COLUMN }? ]. \end{array}
$$

(viii) Restricted Summation. Restricted summations can be handled by defining another molecule consisting of restricted atoms.

Example:

```txt
MIX = APPLE, ORANGE,
SUM[MIX: MIX?] <= CEILMIX.
```

(ix) Nonlinear Terms. Nonlinear terms can be handled by interactively specifying the form of nonlinearity of objective function/constraints. The current implementation allows polynomials and standard trignometric functions only.

## 2.4. Illustrative Example

## 2.4.1. Sample Problem

To illustrate the capability of the LAMP system, we will use the following agricultural planning example, adapted from [14].

A farm manager is planning for the next session consisting of the periods May, June and July months. The various crops for the season under consideration being cotton and onion (cultivation crops grown in a field) and apples and oranges (grown in an orchard). The land availabilities for the field and the orchard are 1850 and 600 units out of the total 2700 units, the balance being used for grazing. The labour availability is limited to 5850 units. The total availability of water is limited to 205,000, 265,000, and 275,000 units in the months of May, June and July respectively, out of which 200,000, 260,000 and 270,000 units only can be used for crops. The corresponding availability figures for fertilizer are 4,000, 5,000, and 6,000 units. The farm is maintaining livestock, i.e., cattle and sheep also. The per unit profit contributions per unit area of cultivation and similar figures for the livestock type are known. There are bounds on the production level of the crops and livestock. In addition a minimum quantity of production must be ensured. The per unit requirement of water, labour and fertilizer are given. The entire data is summarized in table 1 to table 7. The farm manager is interested in an optimal strategy that maximizes his revenue.

Minimum production.  
Unit profit contribution.  
Table 1  
Land availability.  
Table 5

<table><tr><td>Field</td><td>Orchard</td><td>Total</td></tr><tr><td>1850</td><td>600</td><td>2700</td></tr></table>

<table><tr><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td><td>Cattle</td><td>Sheep</td></tr><tr><td>6453</td><td>6110</td><td>4814</td><td>8812</td><td>500</td><td>600</td></tr></table>

Table 2A  
Average unit labour requirements.

<table><tr><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td></tr><tr><td>2.9</td><td>2.7</td><td>1.0</td><td>1.5</td></tr></table>

Table 6A  
Bounds for crops.  
Table 2B

Labour availability.

<table><tr><td>Total</td></tr><tr><td>5850</td></tr></table>

<table><tr><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td></tr><tr><td>2000</td><td>250</td><td>500</td><td>800</td></tr></table>

Table 6B

Table 3A  
Unit water requirement.

<table><tr><td></td><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td><td>Cattle</td><td>Sheep</td></tr><tr><td>May</td><td>65</td><td>-</td><td>-</td><td>-</td><td>1</td><td>4</td></tr><tr><td>June</td><td>80</td><td>60</td><td>50</td><td>75</td><td>2</td><td>5</td></tr><tr><td>July</td><td>90</td><td>64</td><td>85</td><td>-</td><td>3</td><td>6</td></tr></table>

Bounds for livestock.

<table><tr><td>Cattle</td><td>Sheep</td></tr><tr><td>400</td><td>300</td></tr></table>

Table 7A

Table 3B  
Water available for crops.

<table><tr><td></td><td>Quantity</td></tr><tr><td>May</td><td>200,000</td></tr><tr><td>June</td><td>260,000</td></tr><tr><td>July</td><td>270,000</td></tr></table>

Unit fertilizer requirements.

<table><tr><td></td><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td></tr><tr><td>May</td><td>1</td><td>4</td><td>7</td><td>10</td></tr><tr><td>June</td><td>2</td><td>5</td><td>8</td><td>11</td></tr><tr><td>July</td><td>3</td><td>6</td><td>9</td><td>12</td></tr></table>

Yield data.  
Table 3C  
Total water available.

<table><tr><td></td><td>Quantity</td></tr><tr><td>May</td><td>205,000</td></tr><tr><td>June</td><td>265,000</td></tr><tr><td>July</td><td>275,000</td></tr></table>

Table 4B  
Fertilizer availability.

<table><tr><td></td><td>Quantity</td></tr><tr><td>May</td><td>4,000</td></tr><tr><td>June</td><td>5,000</td></tr><tr><td>July</td><td>6,000</td></tr></table>

Table 4A

<table><tr><td>Cotton</td><td>Onion</td><td>Apple</td><td>Orange</td></tr><tr><td>12</td><td>13</td><td>14</td><td>15</td></tr></table>

Table 7B

<table><tr><td>Quantity</td></tr><tr><td>15,000</td></tr></table>

## 2.4.2. LAMP Formulation of the Sample Problem

The sample problem discussed in section 2.4.1 is written in LAMP using the syntax specified in fig. 1. The terminology phase appears in fig. 2 and the constraints and objective function appear in fig. 3.

## 3. Data Management

## 3.1. Introduction

Most real life problems tend to be of reasonably large size involving several thousands of variables and several hundreds of constraints. Obviously, one has to ensure that each and every coefficient that goes into the model is correct both in its value and its association with the appropriate variable and constraint. This is definitely not a trivial issue. The early matrix generators used several check utilities to perform this task. Substantial portion of the mathematical programming software like MPSX [12], LINDO [20] is devoted to the job of data validation.

<table><tr><td colspan="2">• ?? NOTE : Lines starting with &#x27; * &#x27; are &#x27; Comment&#x27; lines.</td></tr><tr><td colspan="2">• = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td></tr><tr><td colspan="2">• TERMINOLOGY PHASE</td></tr><tr><td colspan="2">• MOLECULE</td></tr><tr><td colspan="2">• = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td></tr><tr><td colspan="2">MONTH = MAY,JUNE,JULY</td></tr><tr><td colspan="2">CROP = COTTON,ONION,APPLE,ORANGE</td></tr><tr><td colspan="2">FIELD = COTTON,ONION</td></tr><tr><td colspan="2">ORCHARD = APPLE,ORANGE</td></tr><tr><td colspan="2">LIVSTOCK = CATTLE,SHEEP</td></tr><tr><td colspan="2">RESOURCE-LAND,LABOR,WATER,FERTLZER</td></tr><tr><td colspan="2">* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==</td></tr><tr><td colspan="2">• IDENTIFIER</td></tr><tr><td colspan="2">* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =</td></tr><tr><td colspan="2">* LAND AVAILABILITY: (Table_1)</td></tr><tr><td colspan="2">TOTALAVL$</td></tr><tr><td colspan="2">FIELDAVL$</td></tr><tr><td colspan="2">ORCHAVL$</td></tr><tr><td colspan="2">• LABOR: (Table_2)</td></tr><tr><td colspan="2">LABORREQ.CROP$ (Table_2A)</td></tr><tr><td colspan="2">LABORAVL$ (Table_2B)</td></tr><tr><td colspan="2">• WATER: (Table_3)</td></tr><tr><td colspan="2">WATERREQ.CROP.MONTH$ (Table_3A)</td></tr><tr><td colspan="2">WATERREQ.LIVSTOCK.MONTH$ (Table-3A)</td></tr><tr><td colspan="2">TOTWATER.MONTH$ (Table_3B)</td></tr><tr><td colspan="2">WATERAVL.MONTH$ (Table_3C)</td></tr><tr><td colspan="2">* FERTLZER: (Table_4)</td></tr><tr><td colspan="2">FERTREQ.CROP.MONTH$ (Table_4A)</td></tr><tr><td colspan="2">FERTAVL.MONTH$ (Table_4B)</td></tr><tr><td colspan="2">* UNIT PROFIT: (Table_5)</td></tr><tr><td colspan="2">PROFIT.CROP$</td></tr><tr><td colspan="2">PROFIT.LIVSTOCK$</td></tr><tr><td colspan="2">* BOUNDS: (Table_6)</td></tr><tr><td colspan="2">CEIL.CROP$ (Table_6A)</td></tr><tr><td colspan="2">CEIL.LIVSTOCK$ (Table_6B)</td></tr><tr><td colspan="2">* YIELD: (Table_7)</td></tr><tr><td colspan="2">YIELD.CROP$ (Table_7A)</td></tr><tr><td colspan="2">MINPROD$ (Table_7B)</td></tr></table>

Fig. 2. Terminology Phase.

The modeller needs help in the presentation of results which again become voluminous. Report Writer Programs devoted to this task have been appended to the standard mathematical programming software. Both these tasks, viz. data validation and report writing act as heavy overheads on the problem solving software. In addition detailed 'what if' analyses that are mandatory in any mod-

```txt
* PROBLEM STRUCTURE
* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
* OBJECTIVE
* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
MAX [CROP : PROFIT.CROP * CROP?] + ALPHA[LIVSTOCK : PROFIT.
LIVSTOCK * LIVSTOCK?]
* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
* CONSTRAINTS
* = = = = = = = = = = = = = = = = = = = = = = = = = = =
* wateravailability(Total)
SUM[CROP : WATERREQ.CROP.MONTH * CROP?] + [LIVSTOCK : WATERREQ.
LIVSTOCK.MONTH * LIVSTOCK?] <= TOTWATER.MONTH
* Labouravailability
SUM[CROP : LABORREQ.CROP * CROP?] <= LABORAVL
* Landavailability
SUM[CROP :CROP?] <= TOTALAVL
* Fieldlandavailability
SUM[FIELD :FIELD?] <= FIELDAVL
* Orchardlandavailability
SUM[ORCHARD :ORCHARD?] <= ORCHAVL
* Wateravailability for crops
SUM[WATERREQ.CROP.MONTH * CROP?] <= WATERAVL.MONTH
* Minimum yields
SUM[CRC":YIELD.CROP * CROP?] >= MINPROD
* Fertilizer consumption
SUM[CROP :FERTREQ.CROP.MONTH * CROP?] <= FERTAVL.MONTH
* Ceiling on crops
CROP? <= CEIL.CROP
* Ceiling on livestock
LIVSTOCK? <= CEIL.LIVSTOCK
* == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ||
```

## Fig. 3. Model Structure.

elling activity require an ability to modify the data and the structure, and re-solve the problem, interactively. These considerations led us to explore the possibility of using database management software to perform the tasks of data validation, output report writing, sensitivity and other 'what if' analysis.

Database management systems have the attractive feature of introducing an independence between data structure and data manipulation. In the model management concept we would like to have the structure of the model and the data independently kept and linked only at the time of actually running the model. This provides us an ability to retrieve and update data with an elegance and power that surpass qualitatively any matrix generator type software currently available. The support which a modeller gets in such tasks as data validation and manipulation is truly remarkable, with the availability of DBMS software.

Relational database management systems have been the most extensively researched models in the recent years. The reasons are many; the chief among them being their elegance and versatility. We first view the input and output of a standard LP Problem as a set of relations and then illustrate the advantages one derives from such a reformulation.

## 3.2. Input Data Model

The input data of a LP problem can be viewed as a set of eight normalized relations.

(i) ivar - the list of variables,

(ii) icon - the list of constraints (includes the objective function as the first constraint),

(iii) ivarn - the list of variable names,

(iv) iconsn - the list of constraint names,

(v) ivarlb - the lower bounds (if any),

(vi) ivarub - the upper bounds (if any),

(vii) imat - the coefficient matrix elements (non-zero values only),

(viii) iconsd - the constraint detail (type and RHS value).

The structure of these relations is as follows:

(i) ivar : (var\_id),

(ii) icon: (cons\_id),

(iii) ivarn: $\overline{(\text{var\_id}^+}$ , var\_name),

(iv) iconsn: $\overline{(\text{cons\_id}^+, \text{cons\_name})}$ ,

(v) ivarlb: $(\overline{\text{var\_id}^+}, \text{lower\_bound})$ ,

(vi) ivarub: $(\overline{\text{var\_id}^+}$ , upper\_bound),

(vii) imat: (cons\_id $^{+}$ , vari\_id $^{+}$ , mat\_element),

(viii) iconsd: $\overline{(\text{cons\_id}^+, \text{cons\_type}, \text{rhsvalue})}$ .

Note: (a) underlined field(s) constitute the key of the relation. (b) + indicate that the key is linked to a base field.

## 3.3. Solution Values Model

The solution of the linear program can also be viewed as a set of four normalized relations:

(i) ovar - solution values,

(ii) ocon - constraint values,

(iii) objr - cost range,

(iv) orhsr - rhs range.

The structure of these relations is as follows:

(i) ovar: (var\_id $^{+}$ , solution, relative\_cost),

(ii) ocon: $(\overline{\text{cons\_id}}^{+}$ , slack, dual\_price), (iii) objr: (var\_id $^{+}$ , current\_cost $^{+}$ , cost\_increase, cost\_decrease),

(iv) orhsr: (cons\_id $^{+}$ , current\_rhs $^{+}$ , rhs\_increase, rhs\_decrease).

The type and format of the fields are summarized below:

(a) var\_id: string of length 8,

(b) cons\_id : string of length 7,

(c) var\_name: string of length 32,

(d) cons\_name: string of length 32, (e) all other fields are numeric of float type (13, 6), i.e., 13 digit long numbers with 6 digits to the right of the decimal point.

Note: These formats are compatible with MPS format [12].

## 3.4. Data Analysis

## 3.4.1. Introduction

A relational view of the data and solution values enable us to exploit the power of the relational DBMS software to assist the analyst in the different aspects of the modelling process. Various kinds of sensitivity and 'what if' analysis can be performed in a flexible manner. Every relational DBMS software supports a query language which is nonprocedural. Non procedurality enables the modeller to view the task without getting involved in the details of how exactly the task must be translated into a set of procedures. The actual procedure conversion can be conveniently left to the machine, thereby permitting a metalevel interface between the modeller and the machine. Most of the query languages have the property of relational completeness, i.e., any query of arbitrary complexity concerning the database can be written with the help of the query language. Also most query languages support user friendly interfaces for interactive editing, report writing, data entry etc. Such an environment facilitates fairly complex analysis, to be performed with ease. We will illustrate the ideas using SQL (Structured Query Language) [24] which is emerging to be the one of the popular query languages. For the sake of clarity we classify the analysis into three stages viz.

(i) Input Data Analysis,

(ii) Solution Report,

(iii) 'What if' Analysis.

## 3.4.2. Input Data Analysis

(i) Problem Statistics. Statistics like the count of variables, count of constraints of different type, nonzero coefficient count, unit coefficient count, density of the matrix, etc. can be conveniently obtained using SQL. Such gross measures provide a preliminary level of check and a rough idea of complexity of the numerical solution of the problem. Sample Query No. 1 illustrates these features (appendix).

(ii) Problem Summary. An ordered list (in any order) of variables, constraints, variable names, constraint names, right hand sides, bounds etc. can be obtained to enable a neat summary of the problem data. Sample Query No. 2 illustrates these features (appendix).

(iii) Simple Error Checking / Consistency Checking. Minimal consistency checks are provided by the relational model directly. For example, the linking of the key of the relation imat (matrix) with the variable list (ivar) and constraint list (icon) ensures that the matrix elements are defined only for valid variables and constraints. Checking for a variable that does not have non zero coefficient in any constraint and/or a constraint with no nonzero coefficient corresponding to any variable can provide a simple error check. Such errors easily creep in many of the large scale problems due to a variety of reasons. Also one can easily check for any constraints with all zero/negative coefficients with a positive right hand side element, which indicates a serious inconsistency. Sample Query No. 3 in appendix illustrates these features.

(iv) Sophisticated Checking. Many of the LP packages provide for a picture clause which pictures elements in a range say (100–999). One can easily get such pictures using SQL. Problem specific data checking like the set of variables that use a specific resource, say water, can be obtained. Checks for simple upper bound, generalized upper bounds can also be made relatively easily. Pattern matching, say checking for a transportation type constraint set can also be obtained. Sample Query No. 4 in Appendix illustrates these features.

## 3.4.3. Output Analysis

(i) Simple Reporting. Printing of solution values in a specified order, partial summary, like breakup of profit into broad product-categories, printing of constraint in specified order, say decreasing order of shadow prices, slack levels can be readily obtained. Sample Query No. 5 in appendix illustrates these features.

(ii) Specialised Reports. List of variables in increasing order of total contribution to the overall profit can be obtained. Sample Query No. 6 in appendix illustrates this feature.

## 3.4.4. What-if Analysis

Feasibility check of a specified solution or a perturbed solution can be made. 100% rule can be tested [1]. Solution with the exclusion/inclusion of a variable(s)/constraint(s) can be obtained. Sensitivity of a function of objective function, say ratio of overall profit from field, to the overall profit from orchard can be obtained as a function of some data. Effect of tightening/relaxing an inequality or a set of inequalities can be studied. Sample Query No. 7 in appendix illustrates these features.

Note: (a) Some of the queries necessitate storing the results of a query for which temporary relations ofunct(kofun, ov1, of1, of2, of3, of4, of5) and orhfunct(krhfun, rc1, rf1, rf2, rf3, rf4, rf5) have been introduced in the SQL statements. (b) These queries are purely illustrative and not exhaustive. More sophisticated queries can be found in [22]. (c) The interesting aspect is that all the query statements are 'on the fly' analysis and not preprogrammed analysis provided in many LP packages. If need be, the representative queries can be catalogued for routine use also.

## 4. Conclusions

We have outlined in this paper a synthesis of modelling languages and data management systems to form the basis of a support system for optimization modelling. We demonstrate the flexibility and power attainable with such an approach. It is believed that a support system like this would go a long way in the interactive model building process using other techniques as well.

## Appendix

```txt
{Q:1 ... Problem Statistics }
{ ________________ }
{ No of variables }
    select count(*) from ivar/
{ No of constraints }
    select count(*) from icon/
{ No of <= constraints }
    select count(*) from iconsd where cons_type
    = 'L'/ 
{ No of nonzero coefficients }
    select count(*) from imat/
{ No of unit coefficients }
    select count(*) from imat where imat.mat_element = 1/
{ Matrix density }
    delete ofunct/
    insert into ofunct(kofun): {'matden '} /
    update ofunct set of1 = select count(*) from
    imat;
    where kofun = 'matden * '/ 
    update ofunct set of2 = select count(*) from
    ivar;
    where kofun = 'matden * '/ 
    update ofunct set of3 = select count(*) from
    icon;
    where kofun = 'matden * '/ 
    update ofunct set of4 = of1/(of2 * of3)
    where kofun = 'matden * '/ 
    select kofun, of1, of2, of3, of4 from ofunct
    where kofun = 'matden * '/ 
{ Q:2 ... Problem Summary }
{ ________________ }
{ List of constraint names in ascending order }
    select cons_name from iconsn order by
    cons_name asc/
{ List of bounds in descending order }
    select * from ivarub order by upper_bound
    desc/
{ Q:3 ... Simple error checking }
{ ________________ }
{ Check for variable with no nonzero matrix coefficient }
    select ivar.var_id from ivar where ivar.var_id
^ =
```

```sql
select imat.var_id from imat where imat.
    mat_element^ = 0/

{ Check for constraints having no nonzero LHS
    elements but with nonzero RHS values }
    select icon.cons_id,cons_type,rhsvalue from
    icon,iconsd
    where icon.cons_id = iconsd.cons_id and
    iconsd.cons_id^ =
    select imat.cons_id from imat
    where imat.mat_element^ = 0 and imat.
    cons_id^
    ='1    '/

{ Q:4 ... Sophisticated checking }
{ ________________ }
{ Picturing the matrix in a range }
    select * from imat where imat.mat_element
    between 100
    and 999
    order by imat.var_id asc, imat.cons_id asc/

{ Variables that use a specific resource - say
    WATER }
    select unique imat.var_id, cons_name from
    imat,iconsn
    where imat.cons_id = iconsn.cons_id and
    cons_name is in
    ⟨' * WATER * ', 'WATER * '⟩/
{ Simple Upper Bound }
    select iconsn.cons_id,cons_name from iconsn,
    imat
    where imat.cons_id = iconsn.cons_id and
    iconsn.cons_id^ =
    select imat.cons_id from imat where imat.
    mat_element^=1;
    group by iconsn.cons_id
    having sum(imat.mat_element) = 1/

{ Generalized Upper Bound }
    select inconsn.cons_id,cons_name from
    iconsn,imat
    where imat.cons_id = iconsn.cons_id and
    iconsn.cons_id^ =
    select imat.cons_id from imat where imat.
    mat_element^=1;
    group by iconsn.cons_id
    having sum(imat.mat_element) > 1/

{ Transportation type pattern }
    select imat.var_id, count(*) from imat
    where imat.mat_element = 1 and imat.cons_id^
    ='1    '
    group by imat.var_id/
    select imat.cons_id, count(*) from imat
    where imat.mat_element = 1 and imat.cons_id^
    ='1    '
```

```sql
group by imat.cons_id/
{ Q:5 ... Solution Analysis }
{ ---- }
{ Simple Report }
    select ovar.var_id,ovar.solution from ovar
    where ovar.solution > 0
    order by ovar.solution desc/
{ Partial Summary - Contribution from orchard and field }
    select sum(imat.mat_element * ovar.solution)
    from imat,ovar
    where imat.var_id = ovar.var_id and imat.
    cons_id = '1' and ovar.var_id is in
    ⟨'APPLE *','ORANGE *'>/ 
    select sum(imat.mat_element * ovar.solution)
    from imat,ovar
    where imat.var_id = ovar.var_id and imat.
    cons_id = '1' and ovar.var_id is in
    ⟨'COTTON *','ONION *'>/ 
    select * from imat where imat.cons_id = '1'
    /
    select * from ovar/
{ Q:6 ... Sophisticated Analysis }
{ ---- }
{ Variable List in increasing order of profit contribution }
    select imat.mat_element * ovar.solution from
    imat,ovar
    where imat.var_id = ovar.var_id and imat.
    cons_id = '1'
    and ovar.solution > 0/
{ Q:7 ... What If Analysis }
{ ---- }
{ Feasibility check }
    select iconsd.cons_id,sum(imat.mat_element * 
    ovar.solution), cons_type,rhsvalue from
    iconsd,imat,ovar
    where iconsd.cons_id = imat.cons_id and 
    ovar.var_id = imat.var_id and imat.cons
    _id ^= '1'
    group by imat.cons_id/
{ Routine Sensitivity Analysis : Output in some
    order }
    select sum(ovar.solution * current_cost) from 
    ovar,objr
    where ovar.var_id = objr.var_id and ovar.solve 
    tion > 0/
    select ovar.var_id,ovar.solution,ovar.solution *
    current _cost
    from ovar,objr where ovar.var_id = objr.var_id 
    order by current_cost desc/
```

```txt
{ Simple Analysis }
{ Delete a variable say 'ONION * ' & create MPS file }
lines 0
separator ' '
select cons_type,iconsd.cons_id from iconsd into w2/
lines 0
separator ' '
select imat.var_id,imat.cons_id,imat.mat_element from imat
where imat.var_id ^= 'ONION * ' into w4/
lines 0
separator ' '
select iconsd.cons_id,rhsvalue from iconsd into w6/
{ 100% Rule : Simultaneous Changes within Ranges }
{ All Basic variable objective coefficients change by 2% }
delete ofunct/
lines 0
select objr.var_id,objr.var_id,current_cost,
cost_increase,cost_decrease,current_cost *
1.02 from objr into f1/insert into ofunct (kofun,ov1,of1,of2,of3,of4):
from f1/
update ofunct set of5 = (of4 - 0f1)/of2 where (of4 - of1) > 0/
update ofunct set of5 = (of4 - of1)/of3 where (of4 - of1) < 0/
select * from ofunct/
select sum(of5) from ofunct,ovar
where kofun = ovar.var_id/
{ Revised Solution with some perturbation }
delete ofunct/
lines 0/
select ovar.var_id,ovar.var_id,ovar.solution,relative_cost
from ovar into f2/
insert into ofunct(kofun,ov1,of1,of2):
from f2/
update ofunct set of4 = of1 * 0.97 where kofun is in ⟨'COTTON * ','ONION * '⟩
update ofunct set of4 = of1 * 1.02 where not kofun is in ⟨'COTTON * ','ONION * '⟩
select * from ofunct/
select iconsd.cons_id,sum(imat.mat_element * of4),cons_type,rhsvalue from iconsd, imat,ovar,ofunct
where iconsd.cons_id = imat.cons_id and
```

ovar.var\_id = imat.var\_id and kofun = imat.
var\_id and imat.cons\_id ^='
1
group by imat.cons\_id/
{ Relative ratio of contribution from crops and livestock as function of cost vector }
{All Basic variable objective coefficients change by 2% }
delete ofunct/
insert into ofunct (kofun,ov1,of1,of2, of3):
select objr.var\_id,objr.var\_id,current\_cost,
cost\_increase,cost\_decrease from objr/
update ofunct set of4 =
select ovar.solution from ovar,ofunct
where ovar.var\_id = kofun/
update ofunct set of5 = 1.02 \* of1 \* of4/
insert into ofunct(kofun,ov1,of1,of2,of3, of4,of5):
{'result\*', 'result\* ',0.0,0.0,0.0,0.0,0.0}/
update ofunct set of5 = select sum(of5)
from ofunct where kofun ^=' result \* ';
where kofun = 'result \* '/
update ofunct set of1 =
select sum(of5) from ofunct where kofun ^='
result \* ' and kofun is in {'COTTON \* ', ONION \* '};
where kofun = 'result \* '/
update ofunct set of2 =
select sum(of5) from ofunct where kofun ^='
result \* ' and not kofun is in
{'COTTON \* ', 'ONION'};
where kofun = 'result \* '/
{ Changing the inequalities to equality for a set of constraints }
select \* from iconsd/
update iconsd set cons\_type = 'E'
where iconsd.cons\_id is in {'5 \*, '6 \* ', '7 \* '}/
select \* from iconsd/

## References

[1] Bradley, S.P., A.C. Hax and T.L. Magnanti, Applied Mathematical Programming (Addison-Wesley, 1977).

[2] Bisschop, J. and A. Meeraus, Selected Aspects of a General Algebraic Modeling Language, Proceedings of the 9th IFIP Conference on Optimization Techniques, Warsaw, 223-233.

[3] Bodily, S.E., Modern Decision Making - A Guide to Modeling with Decision Support System (McGraw-Hill, 1985).

[4] Bodily, S.E., Spreadsheet Modeling as a Stepping Stone, Working Paper, Darden Graduate Business School, University of Virginia (1986) 1–24.

[5] Brook, A., A. Drud and A. Meeraus, High Level Modeling Systems and Nonlinear Programming, Discussion Paper, Development Research Department, World Bank, Report No. DRD113, (1984) 1–31.

[6] Ellison, E.F.D. and G. Mitra, UIMP: User Interface for Mathematical Programming, ACM Transactions on Mathematical Software 8, no. 3 (September, 1982) 229–255.

[7] Fourer, R. and M.I. Harrison, A Modern Approach to Computer Systems for Linear Programming, MIT Sloan School of Management, Working Paper No. 988-78 (1978) 1-58.

[8] Fourer, R., Modeling Languages versus Matrix Generators for Linear Programming, ACM Transactions on Mathematical Software 9, no. 2, (June, 1983) 143–183.

[9] Geoffrion, A.M., Structured Modeling: A Progress Report, Proceedings of the 12th International Symposium on Mathematical Programming (August, 1985) 1–21.

[10] Geoffrion, A.M., An Introduction to Structured Modeling. Working Paper No. 338, Western Management Science Institute, Univ. of California (1986) 1–67.

[11] IBM World Corporation, Matrix Generator and Report Writer (MGRW) Program Reference Manual, No. SH19-5014, New York (1972).

[12] IBM World Trade Corporation, IBM Mathematical Programming Systems Extended/370 (MPSX/370) Program Reference Manual, 2nd ed., No. SH19-1095-1, New York (1976).

[13] Jensen, K. and N. Wirth, Pascal User Manual and Report, 3rd ed. (Springer-Verlag, New York, 1985).

[14] Katz, S., L.J. Risman and M. Rodeh, A System for Constructing Linear Programming Models, IBM Systems Journal 19, no. 4 (1980) 505–520.

[15] Kendrick, D.A. and A. Meeraus, GAMS: An Introduction, Draft Book, The World Bank (February 1985).

[16] Liebman, J., L. Lasdon, L. Schrage and A. Waren, Modeling and Optimization with GINO (The Scientific Press, Palo Alto, CA, 1986).

[17] McCosh, A.M., M. Scott and S. Michael, Management Decision Support Systems (Macmillan Press, 1978).

[18] Meeraus, A., An Algebraic Approach to Modelling, Journal of Economic Dynamic and Control 5 (1983) 81–108.

[19] Mills, R.E., R.B. Fetter and R.F. Averill, A Computer Language for Mathematical Program Formulation, Decision Sciences 8 (1977) 427–444.

[20] Schrage, L., Linear Programming Models with LINDO, The Scientific Press, Palo Alto, CA, 1981).

[21] Schrage, L., User's Manual for LINDO, The Scientific Press, Palo Alto, CA, 1981).

[22] Singh, I.S., A Support System for Optimization Modelling, Ph.D. Thesis (being submitted) (Indian Institute of Technology, Kanpur, 1986).

[23] Steinberg, D.I., ALPS (Advanced Linear Programming System): An easy to use Mathematical Programming Package, Proc. ORSA/TIMS Joint National Meeting (Atlanta, GA, 1977).

[24] Unify Corporation, UNIFY Relational Data Base Management System: Reference and Tutorial Manuals (Portland, OR, 1984).

[25] Williams, H.P., Model Building in Mathematical Programming, 2nd ed. (John Wiley, 1985).
