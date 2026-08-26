---
otero_id: 17096
otero_key: "6HAUJT24"
title: "Database organisation: An algorithmic framework for decision support systems in APL"
authors: "W.E. Cundiff"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90028-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Database Organisation: An Algorithmic Framework for Decision Support Systems in APL

W.E. CUNDIFF

Griffith University, Nathan, Brisbane, Queensland 4111, Australia

The three prevailing models of database structure (hierarchical, network and relational) are most often portrayed independently by diagrammatical convention or in the context of respective DBMS that mask the innerworkings. By adopting a glass-box approach, key database concepts are portrayed by way of an algorithmic treatment. Operations are specified in APL, utilising the single logic pattern of sequence to explore structural relationships. The approach is directed toward a category of concise idioms for prototype specification in applications requiring integral dialogue and data/modelbase management as found in decision support systems.

![](/api/attachments/6HAUJT24/fulltext/images/26aad78538831caaa810763ad38d986549b95f4d4855132b619bd008ca0281bb.jpg)

W.E. Cundiff is a senior lecturer in Organisational Modelling and Information Systems in the Division of Administration at Griffith University, Brisbane, Australia. Mr. Cundiff began his systems career in the late 1960s and obtained his Masters degree, concentrating in systems modelling and simulation, from Toronto's York University in 1976. He has written and consulted widely on systems and computing where his work has appeared in publications such as Applied Mathe-

matical Modelling, Simulation, and Technological Forecasting and Social Change. He is past Technical Director of an APL software house in Sydney, Australia and prior to that, Senior Research Associate with the Institute for Research on Public Policy in Montreal. Mr Cundiff has been on the Editorial Board of Transnational Data and Communications Report since 1978.

## 1. Introduction

The growth of decision support systems has been accompanied by a number of conceptual and developmental perspectives, mostly derivative and lacking a firm meta-theoretical foundation encompassing the overall field. In the absence of such underpinnings, the notion of a framework has been put forth as an organising principle to be applied and provide structure to DSS design [27]. A prevailing framework constructed around the three technology components of database, modelbase and dialogue management has gained wide currency among researchers and practitioners alike. Much effort, both in terms of software engineering and end-use is being devoted to achieving integration across the three components [4,18]. While truly multi-functionality software has been developed to embrace the technology triad, the majority of work is dedicated to bringing together software with quite disparate origins, purpose and design strategies.

The term ‘Confederation’ captures well the kind of loose coupling of functional subsystems that fosters individually directed growth among the modules that compose a comprehensive information system [20]. As a complement to the notion of confederation, ‘Sovereignty’, as set forth here, would suggest a highly self-contained development environment where linkages among constituent parts are tighter, more easily co-ordinated and less subject to environmental forces from without. The present discussion addresses database organisation within such a development environment which subsumes the three technology components stated above. APL notation is used to describe the operational and structural characteristics of database organisation with the capability of expressing complex relationships very concisely, developing prototype DSS as well as production level systems, and providing special purpose idioms [22] as building blocks for DSS. The reader's attention, however, is directed primarily to the algorithmic treatment of database organisation. The approach contrasts strongly with diagrammatical conventions, pseudo-code and other devices for process specification, and current data modelling tools for conveying database concepts. The framework requires no control structures for iteration or conditional branching. All algorithms then are stated purely as sequences.

## 2. Background

APL has maintained a high profile among practitioners of decision support from the outset of DSS the concept [25], through the 1970's [1], and to the present [17]. APL is a development environment for current research in the emergent area of group decision support systems [7]. Its impact on development productivity has been well documented [14], particularly in the DSS setting. Contrary to often held beliefs, APL has found its widest application by far in commercial systems [26]. The language has been utilised with notable success as a 'shorthand' for describing concepts in a number of disciplines such as mathematics [14,21] and economics [28]. Where information processing, i.e., moving data, sorting and isolating special cases dominates, APL earned a Turing Award from the Association for Computing Machinery for its creator as a notation for embodying such processes [15]. In the area of simulation, the language has gained considerable scope [5,6], especially with its application on true pipeline array processors [9]. Prototyping [19] and micro-computer applications for decision support [2] are fast growing areas of information systems development. Software houses regularly budget up to ten percent of fees for prototyping high performance systems, such as process control and automated manufacturing applications, in APL prior to low level coding [24].

Database applications in DSS share common factors with database technology generally. However, DSS specific criteria have been postulated, as mentioned in the early reference to the technology triad and elsewhere [3]. APL, with its considerable power for array handling, has been a tool of developers of database management systems for some time [10,11,12]. The notation, in executable form, will be employed here to describe concepts central to hierarchical and relational models [8]. The cases as portrayed were influenced considerably by seeing APL in practice [13,23], the first addressing primarily numerical data; the second, mixed-data type relations and associated query capabilities. Finally, all that follows was carried out on an 8088-based IBM Personal System/2 Model 30 running at 8MHz. The APL is that developed by the IBM Madrid Scientific Centre and requiring an 8087 maths co-processor.

## 3. The Hierarchical Model

Within the model, data reside in a single multilevel array, the dimensions of which are application-specific (The reader is directed to fig. 1 for the global data structures referred to throughout this discussion). For instance an array of rank 6, could contain time series (VARIABLE) stored by period (TIMEFRAME); by item (ACTIVITY); by context, e.g. observed values for past performance, normative estimates of future, or progressively adjusted values for tactical planning (PERSPECTIVE). These could be further keyed by geographical area (SECTION) and or by industry class (INTEREST). The associated DBMS must permit the graceful retrieval and rearrangement of any or all of the levels into a new hierarchical structure for input to models or for reporting. For instance an application might call for a variance analysis between a prior forecast and observed performance. Designation of levels across the array can be effected by two parameters supplied dyadically to a function for selection where W ↔ level identifier within the array and X ↔ identifier of a series. An example could be a select performed at the VARIABLE level for a particular section. Initially:

3.1.1 Y ← φ, LEVIL [WW ← LEVIL[;1] i W ← 1 ↑ W;]

W, an alphanumeric identifier specifies the structural level array and X the particular row-identifier sought within the candidate level. An intermediate global variable (LEVIL) is used later for indexing into the appropriate strata in the database. W is a literal N × N array with unique characters in the row positions of the first column. Therefore the operation takes the first character of the supplied argument and seeks the index of W (dyadic iota) within the first column of LEVIL. The row location is used to extract from LEVIL the name of the level within the overall structure.

```txt
LEVIL
PERSPECTIVE
SECTION
INTEREST
ACTIVITY
VARIABLE
TIMEFRAME
```

<table><tr><td colspan="10">ρ DATA</td></tr><tr><td>7</td><td>3</td><td>4</td><td>5</td><td>2</td><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">PERSPECTIVE</td></tr><tr><td colspan="6">BASELINE RESEARCH</td><td>1</td><td colspan="3">BASE</td></tr><tr><td colspan="6">OBSERVED PERFORMANCE</td><td>2</td><td colspan="3">OBS</td></tr><tr><td colspan="6">DRAFT PLAN</td><td>3</td><td colspan="3">DRAFT</td></tr><tr><td colspan="6">ZONED PLAN</td><td>4</td><td colspan="3">ZONE</td></tr><tr><td colspan="6">NORMATIVE ESTIMATE</td><td>5</td><td colspan="3">NORM</td></tr><tr><td colspan="6">HISTORICAL RECORD</td><td>6</td><td colspan="3">HIST</td></tr><tr><td colspan="6">EXPLORATORY FORECAST</td><td>7</td><td colspan="3">FORE</td></tr><tr><td colspan="10">SECTION</td></tr><tr><td colspan="6">CAPRICORNIA</td><td>1</td><td colspan="3">CAP</td></tr><tr><td colspan="6">FAR NORTHERN</td><td>2</td><td colspan="3">FN</td></tr><tr><td colspan="6">CORMORANT PASS</td><td>3</td><td colspan="3">CP</td></tr><tr><td colspan="10">INTEREST</td></tr><tr><td colspan="6">AGGREGATE</td><td>1</td><td colspan="3">ALL</td></tr><tr><td colspan="6">TOURISM</td><td>2</td><td colspan="3">TOUR</td></tr><tr><td colspan="6">CONSERVATION</td><td>3</td><td colspan="3">CONS</td></tr><tr><td colspan="6">FISHING</td><td>4</td><td colspan="3">FISH</td></tr><tr><td colspan="10">ACTIVITY</td></tr><tr><td colspan="6">LINE FISHING</td><td>1</td><td colspan="3">LINE</td></tr><tr><td colspan="6">MUD CRABBING</td><td>2</td><td colspan="3">MUD</td></tr><tr><td colspan="6">GILL NETTING</td><td>3</td><td colspan="3">GILL</td></tr><tr><td colspan="6">BEAM TRAWLING</td><td>4</td><td colspan="3">BEAM</td></tr><tr><td colspan="6">BEACH SEINING</td><td>5</td><td colspan="3">BEACH</td></tr><tr><td colspan="10">VARIABLE</td></tr><tr><td colspan="6">LABOUR FORCE</td><td>1</td><td colspan="3">WORK</td></tr><tr><td colspan="6">BIOMASS</td><td>2</td><td colspan="3">BIO</td></tr><tr><td colspan="10">TIMEFRAME</td></tr><tr><td colspan="6">1985</td><td>1</td><td colspan="3">85</td></tr><tr><td colspan="6">1986</td><td>2</td><td colspan="3">86</td></tr><tr><td colspan="6">1987</td><td>3</td><td colspan="3">87</td></tr><tr><td colspan="10">REF</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>4</td><td>5</td><td>999</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>7</td><td>99</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

```csv
▼SELECT[□]▼
▼ R ← W SELECT X;WW;Y;X1
[1] Y ← φ, LEVIL[WW ← LEVIL[;1] i W ← 1↑W;]
[2] X1 ←(φ, Y[;20 + i 4], ((1↑ρ Y), 1) ρ”) i X
[3] φ W, ‘←’, 50 φ X1
[4] REF["ρ WW; i ρ, X] ← X
```

```csv
▼STRUCTURE[□]▼
▼ STRUCTURE X;ZZ
[1] X ← (X ≠ ',')/X
[2] LEV ← LEVIL[ZZ ← LEVIL[;1] i X;]
[3] REF ← REF[ZZ;]
[4] DAT ← 2 1 3 Q DATA[P;S;I;A;V;T]
▼
INSERT[□]▼
▼ W INSERT X
[1] DAT ← DAT, [PRC]X
```

```csv
[2] REF[DIM;REF[DIM;] i0] ← W
▼
▼EXCLUDE[□]▼
▼W EXCLUDE X;L;MASK
[1] MASK ← (1↑ρ DAT) ρ1
[2] MASK[REF[L ← LEV[;1] iW;] iX] ← O
[3] DAT ← MASK/[L-3]DAT
```

```txt
SELECTS
4.1.I (φ PARTNO, QONHAND), DESCRIPTION
4.2.I INVENTORY
4.3.I (φ PARTNO), DESCRIPTION, φ QONHAND
4.4.I (DESCRIPTION ^. = 'BOLT') ≠ INVENTORY
4.5.I DISTINCT Q[;2]
4.6.Q ((Q[;2] = 221) ^Q[;5] > 0)/[1]Q
4.7.Q ((Q[;1] = 54) ∨ Q[;1] = 64)/[1]Q
4.8.Q ((Q[;1] = 64) ∨ Q[;1] = 54) ^Q[;2] ≠ 209/Q
4.9.Q (100 < PRICE × QONHAND)/[1]Q
4.10.I (DESCRIPTION[;3] = 'B')/[1]INVENTORY
4.11.I INVENTORY[↓, QONHAND;]
4.12.Q AVG (PRICE > 10)/PRICE
4.13.Q (AVG (Q[;2] = 221/PRICE), +/(Q[;2] = 221)/QONORDER
4.14.Q +/Q[;2] = 221
4.15.I +/DESCRIPTION ^. = 'BOLT'
4.16.Q (PRICE BETWEEN .30 10.00)/Q

▼DISTINCT□▼
▼ R ← DISTINCT X
[1] R ← (1 10 < \X^0. = X)/X

▼AVG□▼
▼ R ← AVG X
[1] R ← (+/X) ÷ ρ X

▼BETWEEN□▼
▼ R ← W BETWEEN X
[1] R ← (X[1] ≤ W) ^X[2] ≥ W

Fig. 1.
```

Y is locally assigned an evaluation of the name indexed in LEVIL, with the result that Y becomes the array, not simply the identifier. Following the conversion and assignment:

## 3.1.2 $\mathbf{X}1\gets (\phi ,\mathbf{Y}[;20 + \iota 4],((1\uparrow \rho \mathbf{Y}),1)\rho^{\prime \prime})\iota \mathbf{X}$

Here the selected array (REGION $\leftrightarrow$ Y) is segmented into fields 21-25, to which a blank column is reshaped and catenated along the last dimension. This is raveled, i.e. the 2 dimensional structure is converted to a vector and evaluated to become numeric, again with the combination of the two primitive functions, execute and ravel. The outcome of this operation is the row position(s) occupied by the numeric key(s) supplied as the right argument earlier (X) within the resultant vector. This is finally, executing right to left, assigned locally to X1. Then:

## 3.1.3 $\phi \mathbf{W},' \leftarrow', 50\bar{\phi} X1$

Recalling 3.1.1, W was reassigned the single literal value as taken from the leading position in the right argument. If W had been "SECTION", W would now be "S". Reading from right to left in 3.1.1, the relative array positions assigned to X1 is converted to a character string for type compatibility, then catenated to the literal (between single quotes) left-facing assignment primitive. The resulting literal string is then catenated to W locally and evaluated to create dynamically a new global variable S containing the index values for subsequent use. The above operations can be performed repeatedly on any individual or combination of levels to establish a path through the database which ultimately gives a tree structure characteristic of the hierarchical model. Following execution and assignments of the variable indicated in W, the coded values originally supplied as the right argument (X) are stored for subsequent reference:

## 3.1.4 REF['ρ W; ι ρ, X] ← X

A numeric array is indexed by row (the relative positions as now contained in W) and by column the number of values originally supplied in 3.1.2, thus a single row with single or multiple column interactions designates the cells in REF where the numeric codes in X are globally stored for later use.

Once the path through the hierarchy is determined, it may be desirable to restructure the nodes to create a new hierarchy. Recalling that new global variables are created by the previous sequence of operations, identified by a single character name, and assigned the cell position within the desired level:

## 3.2.1 LEV $\leftarrow$ LEVIL [ZZ $\leftarrow$ LEVIL[;1] $\iota$ X;]

Here X is supplied as a character string composed of the single character identifiers discussed above. If the database is structured in six levels with the levels identified top down as PERSPECTIVE, SECTION, INTEREST, ACTIVITY, VARIABLE, AND TIMEFRAME, then it may be restructured by supplying a newly sequenced string. If column 1 of LEVIL were the first six consecutive letters of the individual array identifiers, then the index of 'VSIAPT' in LEVIL [;1] would yield a new index vector: 523416 In 3.2.1 this is assigned locally to ZZ. This index vector then is utilised to effect a row-wise rearrangement of LEVIL which is assigned to LEV globally. LEV and LEVIL contain identical content (names of the levels) but are simply ordered differently. LEV is the literal companion to REF which must now also have an identical rotation of row positions so that there is a direct row-wise correspondence between the two arrays. This is effected by REF ← REF[ZZ;].

Recall again that for a six dimensional array, there will be six global variables identifying it, one for each level in the hierarchy. By successive operations of 3.1.1–3.1.4, the level identifiers will contain the index values for selected parts of each level. Ultimately all retrievals will culminate in an array with a maximum rank of 3. The target array is first obtained by a level by level decomposition of the total array using the level identifiers. Given a six dimensional array (DATA) containing the entire database:

## 3.2.2 DAT←213Q DATA [P; S; I; A; V; T]

The above operation produces the decomposition by level. The resulting six dimensional array undergoes a transposition, whereby the planar dimension is interchanged with the columnar dimension and assigned to DAT, preserving the original values in DATA. At this stage, a data structure has been derived which is manageable conceptually, i.e. rank 3 or lower, and easier for applying mathematical operations for modelling or reporting. For instance it may be desirable to perform simple arithmetic on the resultant structure. If a summation is sought, the level across which the operation is to be effected is designated by reference to the index array (LEV) mentioned earlier, finding the index of X in the first column, and making a global assignment for subsequent indexing into the target array. Recalling the discussion earlier, the resulting structure of rank 3 cannot be indexed directly with DIM but must be adjusted simply by a new assignment: PRC ← DIM-3. PRC will contain the dimension (plane, row or column) along which the mathematical operation is to be carried out. With the global PRC a summation is made by plus reduction: +/[PRC] DAT.

Results may be stored for later use in a number of ways, notably by creating a new global variable for maintaining intermediate values or more efficiently by catenating a new array to the array identified as DAT. The latter is achieved by referencing the global PRC and where X is the result of the summation, say, DAT ← DAT, [PRC]X will result in a new composite array containing the results of the summation. To perform subsequent, more complex operations, the numeric index array REF is used to store a variable for future reference. If W is a user supplied code for later reference, then the following will store the code:

## 3.3.1 REF[DIM; REF [DIM;] $\iota 0]\gets \mathbf{W}$

While it is desirable to contract arrays for ease of performing mathematical operations and to store variables by catenation to the target arrays, it is also good practice to selectively exclude unwanted data from the existing subject. Given that levels have been selected, subsets of data at each level have been extracted, the resulting array has been hierarchically restructured, further decomposition to array rank 3 is effected, mathematical operations have been carried out and results stored in the appropriate form, the structure now can be further decomposed retaining only the relevant data:

## 3.4.1 MASK $\leftarrow (1\uparrow \rho \mathrm{DAT})\rho 1$

The above operation will initiate the creation of a boolean vector or mask made up of 1's and 0's. This is achieved by deriving the number of the first dimension of DAT and assigning to a mask a vector of 1's of length equal to the first dimension of DAT. REF and LEV are used together in order to specify the positions within MASK for inserting 0's to make the Boolean vector. This is achieved by supplying the level for exclusion (W) along with the numeric codes specifying the precise parts of the array to be discarded (X):

## 3.4.2 MASK [REF[L ← LEV[;1] i W;] i X] ← 0

Remembering the direct row-wise correspondence between REF and LEV, the level is sought by seeking the index of W, a literal, in the first column of LEV and assigning to L. Using L as a row designator for indexing into REF, X will be used to find the column intersections for the data to be excluded. This secondary indexing is then used for inserting the 0's into the boolean vector, MASK. The designated parts of the matrix DAT corresponding to 0's in MASK, are then compressed from DAT and the abiding array reassigned to DAT:

## 3.4.3 DAT $\leftarrow$ MASK/[L-3]DAT

## 4. The relational model

The approach presented here is comparative in that SQL queries are used as vehicles for exploring APL equivalents. The actual SQL queries and relations appear elsewhere [13] and are adopted for use here due to their wide familiarity to the SQL and relational database user community. The tables in particular are presented along with their internally represented data type and dimensionally. (See table 1.)

All values in the QUOTATIONS relation are stored in numeric fields. Once tables are created and maintained in an APL workspace, the notational queries can be tested by direct execution, and maintained by creating literal strings and evaluating the expression with the execute primitive or by user-defined functions. A number of operations will now be portrayed. Along the way, special user-defined functions will be discussed:

The first query effects an internal join by way of reordering the attributes from the INVENTORY table.

4.1.1 SELECT PARTNO, QONHAND, DESCRIPTION FROM INVENTORY ( $\bar{\phi}$ PARTNO, QONHAND), DESCRIPTION

Noting the mixed data types involved, the numeric attributes must first of all be converted to literals before the DESCRIPTION attribute can be catenated (joined internally)

4.2.1 SELECT \* FROM INVENTORY
INVENTORY OR SUPPLIERS OR QUOTATIONS

In order to view an entire relation one need only key the table name.

Table 1
INVENTORY.

<table><tr><td>207</td><td>GEAR</td><td>75</td></tr><tr><td>209</td><td>CAM</td><td>50</td></tr><tr><td>221</td><td>BOLT</td><td>650</td></tr><tr><td>222</td><td>BOLT</td><td>1250</td></tr><tr><td>231</td><td>NUT</td><td>700</td></tr><tr><td>232</td><td>NUT</td><td>1100</td></tr><tr><td>241</td><td>WASHER</td><td>6000</td></tr><tr><td>285</td><td>WHEEL</td><td>350</td></tr><tr><td>295</td><td>BELT</td><td>85</td></tr><tr><td>PARTNO(Numeric, 9×1)</td><td>DESCRIPTION(Literal, 9×8)</td><td>QONHAND(Numeric, 9×1)</td></tr></table>

4.3.1 SELECT PARTNO, DESCRIPTION, QONHAND FROM INVENTORY

( $\bar{\phi}$ PARTNO), DESCRIPTION, $\bar{\phi}$ QONHAND

This is a variation on 4.1.1, but with further mixing of literal and numeric attribute data types using the format primitive.

4.4.1 SELECT \* FROM INVENTORY WHERE DESCRIPTION = 'BOLT'

Here, all attributes are selected for those tuples containing the designated field.

(DESCRIPTION ^. = 'BOLT') ≠ INVENTORY

The inner product operator is employed where a new primitive is effectively created by combining two existing primitives, here the logical 'and' and 'equals'. The result is a boolean mask which is used to compress $(\neq)$ the array across the first dimension.

## 4.5.Q SELECT DISTINCT PARTNO FROM QUOTATIONS

Here a synonym for QUOTATIONS - Q is introduced. Direct indexing by row or column permits shorthand versions of sequences to be issued.

DISTINCT Q[;2]

A special user-defined monadic function is created and maintained along with the relations in a workspace shared by only two object types – functions and variables. DISTINCT computes a boolean mask in the parenthetic express to the left of the compression primitive, which is then executed to extract the unique numbers in the vector argument X.

$\nabla \mathbf{R}\gets$ DISTINCT X

$$
[ 1 ] \mathrm{R} \leftarrow (1 1 0 <   \backslash X ^ {0}. = X) / X \nabla
$$

4.6.Q SELECT \* FROM QUOTATIONS WHERE PARTNO = 221 AND QONORDER > 0

Here the synonym is used for indexing on two attributes based on a combination of three logical conditions. Compression of Q along the 1st dimension results in a retrieval of the designated data meeting the logical conditions. ((Q[;2] = 221) ^Q[;5] > 0)/[1] Q

4.7.Q SELECT \* FROM QUOTATIONS WHERE SUPPNO = 54 OR SUPPNO = 64

This is a similar query to that shown in 4.6.Q. Note that / [1] is the same as the short form for operation, either compression or reduction across the first dimension. ((Q[;1] = 54) v Q[;1] = 64)/ [1] Q

Table 2
QUOTATIONS.

<table><tr><td>51</td><td>221</td><td>0.30</td><td>10</td><td>50</td></tr><tr><td>51</td><td>231</td><td>0.10</td><td>10</td><td>0</td></tr><tr><td>53</td><td>222</td><td>0.25</td><td>15</td><td>200</td></tr><tr><td>53</td><td>232</td><td>0.10</td><td>15</td><td>0</td></tr><tr><td>53</td><td>241</td><td>0.08</td><td>15</td><td>0</td></tr><tr><td>54</td><td>209</td><td>18.00</td><td>21</td><td>0</td></tr><tr><td>54</td><td>221</td><td>0.10</td><td>30</td><td>150</td></tr><tr><td>54</td><td>231</td><td>0.04</td><td>30</td><td>200</td></tr><tr><td>54</td><td>241</td><td>0.02</td><td>30</td><td>200</td></tr><tr><td>57</td><td>285</td><td>21.00</td><td>14</td><td>0</td></tr><tr><td>57</td><td>295</td><td>8.50</td><td>21</td><td>24</td></tr><tr><td>61</td><td>221</td><td>0.20</td><td>21</td><td>0</td></tr><tr><td>61</td><td>222</td><td>0.20</td><td>21</td><td>200</td></tr><tr><td>61</td><td>241</td><td>0.05</td><td>21</td><td>0</td></tr><tr><td>64</td><td>207</td><td>29.00</td><td>14</td><td>20</td></tr><tr><td>64</td><td>209</td><td>19.50</td><td>7</td><td>7</td></tr><tr><td>SUPPNO (16,1)</td><td>PARTNO (16,1)</td><td>PRICE (16)</td><td>DELIVERY TIME (16,1)</td><td>QONOR-DER (16)</td></tr></table>

4.8.Q SELECT \* FROM QUOTATIONS WHERE - (SUPPNO = 64 OR SUPPNO = 54) AND NOT PARTNO = 209

(((Q[;1] = 64) ∨ Q[;1] = 54) ^Q[;2] ≠ 209) ≠ Q

The above query, while similar in terms of logical relationships indicates the growing complexity of grouping operations by nesting of individual boolean tests.

4.9.Q SELECT \* FROM QUOTATIONS
WHERE PRICE \* QONORDER > 100.00

(100 < PRICE × QONORDER)/[1] Q

Here, the query operates on fragmented parts of the QUOTATIONS table. These are shown in table 2.

4.10.I SELECT \* FROM INVENTORY WHERE DESCRIPTION LIKE 'B\_'

As was shown in the discussion on hierarchical organisation, specified literal columns can be subjected to boolean tests for matching

(DESCRIPTION [;3] = 'B')/[1] INVENTORY

The query shown also uses a fragmented part of the literal DESCRIPTION field from the INVENTORY TABLE.

4.11.1 SELECT \* FROM INVENTORY ORDER BY 3 DESC

Sorting operations are effected by a combination of array indexing and built-in primitives.

INVENTORY [↓, QONHAND;]

Executing right to left, QONHAND, a 9 by 1 array is raveled to a vector, then supplied as an argument to the gradedown primitive which will yield the relative vector positions by magnitude in descending order.

4.12.Q SELECT AVG(PRICE) FROM QUOTATIONS WHERE PRICE > 10

A user-defined function is introduced here corresponding to the built-in functions found in SQL.

AVG (PRICE > 10)/PRICE

Executing right to left, a boolean mask is computed within the parentheses, then applied to compress out those elements from PRICE(a vector of sixteen elements). The explicit result is passed via R to AVG where the mean is computed and displayed.

$\nabla \mathbf{R}\gets \mathbf{AVG}\mathbf{X}$

$$
[ 1 ] \mathrm{R} \leftarrow (+ / \mathrm{X}) \div \rho \mathrm{X} \nabla
$$

4.13.Q SELECT AVG(PRICE) SUM(QONORDER) FROM QUOTATIONS WHERE PARTNO = 221

Here, a combination or logical tests combine with two compressions and a plus reduction to extracted the desired tuples.

$$
\begin{array}{l} (\text { AVG } (Q [; 2 ] = 2 2 1) / \text { PRICE }), + / (Q [; 2 ] = 2 2 1) / \\ \text { QONORDER } \end{array}
$$

4.14.Q SELECT COUNT (\*) FROM QUOTATIONS WHERE PARTNO = 221

Using the synonym, and executing right to left, a boolean test is made with the resulting vector of 0's and 1's, a plus reduction is applied to the vector to simply sum the 1's which indicates when conditions have been met.

\+ /Q[;2] = 221

4.15.I SELECT COUNT (\*) FROM INVENTORY WHERE DESCRIPTION = 'BOLT' + /DESCRIPTION ^. = 'BOLT'

This query is best described as a combination of operations described in 4.4.I and 4.14.Q.

4.16.Q SELECT \* FROM QUOTATIONS WHERE PRICE BETWEEN .30 and 10.00 (PRICE BETWEEN .30 10.00) + Q

$\nabla \mathbf{R}\gets \mathbf{W}$ BETWEEN X

$$
[ 1 ] \mathrm{R} \leftarrow (\mathrm{X} [ 1 ] \leq \mathrm{W}) ^ {\wedge} \mathrm{X} [ 2 ] \geq \mathrm{W} \nabla
$$

A user-defined function is included where two logical tests are made to establish the outer bounds of the range. Internally, two boolean vectors are created which are the compared element-by-element for satisfying the logical 'and'. The result is a composite vector used as a mask to perform the column-wise compression and yielding those tuples from the QUOTATIONS relation satisfying the conditions.

## 5. Conclusion

Several database concepts have been portrayed using sequential algorithms formulated in APL. Given the scope of the discussion, very little notation was required to reveal the fine structure of database organisation. With the knowledge that only two object types may co-exist in an APL workspace (variables and functions), the capability to develop sovereign DSS embodying the technology triad indicates both the reasons for the popularity of APL in DSS development and abiding potential for creating sovereign information systems in support of management decision making.

## References

[1] R.G. Canning, "APL and Decision Support Systems", EDP Analyzer 14, No. 5 (1976) 1-12.

[2] G. Chandrasekaran and R. Ramesh, "Microcomputer Based Multiple Criteria Decision Support System for Strategic Planning", Information & Management 12 (1987) 163–172.

[3] E.K. Clemons, "Database Design for Decision Support", Proc. 14th Hawaii International Conference on System Sciences (Western Periodicals, North Hollywood, 1981) 580–588.

[4] E. Countryman, "Interactive Financial Planning System Interface into Hierarchical Database", Proc. IFPS Users' Association 1987 National Meeting (EXECUCOM, Austin, TX, 1987) 87–88.

[5] W.E. Cundiff "Model Integration and Algorithmic Transparency in APL", Applied Mathematical Modelling 8 (1984) 445-448.

[6] W.E. Cundiff, "On the Specification of Diverse Models in APL", Simulation 45, No. 3 (1985) 138–143.

[7] W.E. Cundiff, “Interactive Software for the Capture, Management, and Analysis of Data in Delphi Inquiries”, Technological Forecasting and Social Change 28 (1985) 173–185.

[8] C.J. Date, An Introduction to Database Systems 2nd ed. (Addison Wesley Publ. comp., Reading, 1977; ISBN: 0-201-14439-5).

[9] J. Delo and S. Friedman, "True Shared Variables as an Aid to System Design", Proc. APL84, Helsinki (June, 1984).

[10] J. Engal, "Hierarchical Data Management", Proc. APL 76 (Association for Computing Machinery, New York, 1976) 113–126.

[11] G. Gould, "A Relational Database Management System in APL", Proc. APL 83: First Australian APL Users Conference (APL Users Group, Sydney, 1983).

[12] B.C. Hagenbuch, “APL and the Relational Model of Data” in: A.J. Rose and B.A. Schick, Eds., APL in Practice (John Wiley & Sons, New York, 1980; ISBN: 0-471-08275-9) 111–119.

[13] IBM, SQL/Data System Terminal Users' guide - VM/SP, SH24-5045, International Business Machines, Boca Raton (1983).

[14] K.E. Iverson, Algebra; an Algorithmic Treatment (Addison-Wesley. Publ. comp., Menlo Park, 1972).

[15] K.E. Iverson, "Notation as a Tool of Thought", Communications of the ACM 231 (1980) 444-465.

[16] P.G.W. Keen and T.J. Gambino, "Building a Decision Support System: the Mythical Man-Month Revisited", in: J.L. Bennet, Ed., Building Decision Support Systems (Addison-Wesley, Reading, 1983; ISBN: 0-201-00563-8).

[17] P.G.W. Keen, "Value Analysis: Justifying Decision Support Systems", in: R.H. Sprague and H.J. Watson, Eds., Decision Support Systems – Putting Theory into Practice (Prentice-Hall International (UK), London, 1986; ISBN: 0-471-10092-7).

[18] J. Moyer, "Impact: Interfacing IFPS Dimension with Information Associates Databases for University Budgeting and Planning", Proc. IFPS' Users' Association 1987 National Meeting (EXECUCOM, Austin TX, 1987) 301–315.

[19] J.D. Naunann and M.A. Jenkins, "Prototyping: The New Paradigm for Systems Development", MIS Quarterly 6, No. 3 (1982) 29–44.

[20] S. Neumann and M. Hadass, "DSS and Strategic Decisions" California Management Review 22, No. 2 (1980) 77–84.

[21] D.L. Orth, Calculus in a New Key (APL Press, Swarthmore, 1976; ISBN: 0-917326-05-9).

[22] A.J. Perlis and S. Rugaber, "The APL Idiom List", Research Report No. 87, Department of Computer Science, Yale University (1977).

[23] C. Sanderson, "A Planning System", I.P. Sharp Associates, Sydney, (1981).

[24] D. Scott, "Computer-Aided Manufacturing of Semi-Conductors" I.P. Sharp Newsletter 10, No. 3 (1982) 7–9.

[25] R. Seaburg and C. Seaburg, "Computer-Based Decision Systems in Xerox Corporate Planning", Management Science 20 No. 4 (1973) 575–584.

[26] A. Smith, APL: A Design Handbook for Commercial Systems (John Wiley & Sons Ltd., Chichester, 1982; ISBN: 0-471-10092-7).

[27] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall Publ. Comp., Englewood Cliffs, 1982).

[28] S. Wilson, “APL as an Instructional Language for Quantitatively Orientated Courses: An Example from Production Economics”, Departmental Information Report 75-5, Staff Paper 11, Texas A&M University (1975).
