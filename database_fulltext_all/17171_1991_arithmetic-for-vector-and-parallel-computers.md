---
otero_id: 17171
otero_key: "PQVTT6JG"
title: "Arithmetic for vector and parallel computers"
authors: "J.Wolff von Gudenberg"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90045-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Arithmetic for vector and parallel computers \*

## J. Wolff von Gudenberg

Institut für Angewandte Mathematik, Universität Karlsruhe, 7500 Karlsruhe, Germany

In recent years large scientific computations are more and more carried out on vector and parallel computers. The performance of these machines has made it possible that large simulation programs replace expensive testing of prototypes. Therefore it is important that the computation is not only fast but also reliable. This aspect is usually not covered by computer vendors. A definition of accurate computer arithmetic including vector and matrix arithmetic, which is exactly the field where vector and parallel computers are applied, has been developed in Karlsruhe in the last decades. We show that this kind of accurate arithmetic can also be implemented on vector or parallel computers efficiently.

Keywords: Supercomputing, Computer arithmetic, Reliability of algorithms.

![](/api/attachments/PQVTT6JG/fulltext/images/470b751774bd0e316256dd9a2b75a6b30025258400bad6930d039411be710834.jpg)

J. Wolff von Gudenberg studied mathematics and computer science at the University of Karlsruhe where he also recieved his doctor degree and habilitation. He has worked as lecturer with the Institut für Formale Beschreibungsverfahren und Angewandte Informatik, Universität Karlsruhe. He has moved to the University of Würzburg, Institute für Informatik, 8700 Würzburg, Germany. His research interests are computer arithmetic, scientific software and programming language development, knowledge based systems and parallel architectures.

\* Manuscript of an invited talk at the 14th Symposium on Operations Research, Ulm, 6–8 September 1989.

## 1. State of the Art

Originally computers were developed for scientific computing, that means mainly numerical calculations in all fields of engineering and scientific modelling. Today computers are more and more general purpose machines which are also used for data retrieval and accounting functions. Computer programs also serve as decision support systems, those are systems which store a reasonable amount of data or knowledge together with some rules or programs which answer queries of the user. If in such systems decisions are derived by computations it is mandatory that these computations are reliable. In recent years algorithms for complete numerical tasks such as the solution of linear and non-linear systems of algebraic equations or differential equations have been developed which in general compute a sharp enclosure of the true solution of the problem. If this enclosure can not be obtained an appropriate message is output $[10]$ , $[16]$ , $[19]$ , $[20]$ , $[22]$ . These algorithms are based on a definition of accurate computer arithmetic which is more than just floating-point arithmetic for the reals.

Today supercomputers, i.e. parallel or vector computers, are mainly developed for scientific computation. They are especially used in many applications where an experimental justification of the computed data is impossible or too expensive. Therefore reliability of the computation is indispensable.

In the paper we summarize the definition of computer arithmetic in the sense of the Karlsruhe approach [13], [17] and then present circuits and algorithms for pipelined or parallel accurate scalar product computation, one key feature of the accurate arithmetic.

Before we go into details we like to discuss a few examples about the state of the art of existing floating-point arithmetic on vector computers.

$S_{2}$

Problem: Computation of sums with the following structure:

$$
S _ {0} \quad := \boxed {1} + 1 6 ^ {N} - 1 6 ^ {N} + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N}
$$

$$
+ 1 6 ^ {N} - 1 6 ^ {N} + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N}
$$

$$
S _ {1} \quad := 1 6 ^ {N} + \boxed {1} - 1 6 ^ {N} + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N}
$$

$$
+ 1 6 ^ {N} - 1 6 ^ {N} + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N}
$$

$$
\begin{array}{r l} := 1 6 ^ {N} - 1 6 ^ {N} + \boxed {1} & + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N} \\ + 1 6 ^ {N} - 1 6 ^ {N} & + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N} \end{array}
$$

$$
\begin{array}{r l} S _ {8 N + 4} & := 1 6 ^ {N} - 1 6 ^ {N} + 1 6 ^ {N - 1} - 1 6 ^ {N - 1} + \dots - 1 6 ^ {- N} \\ & \quad + 1 6 ^ {N} - 1 6 ^ {N} + 1 6 ^ {N - 1} - + \dots + 1 6 ^ {- N} - 1 6 ^ {- N} \\ & \quad + \boxed {1}. \end{array}
$$

The exact value of every sum is 1. Numerical results for N = 29, computed on a CRAY 2 are shown in table 1. The scalar mode produces the wrong result 0 if the 1 is in index position 0 through 129 of the vector and then switches to the correct result 1. The vector mode delivers results totally different from the scalar mode which can only be interpreted as random numbers. These results are produced due to the vectorization of the sum. For other supercomputers such as VP 400 EX or CONVEX similar results have been produced [7].

The second example again shows major differences between scalar and vector mode.

Table 1

<table><tr><td>Sum</td><td>Scalar Mode</td><td>Vector Mode</td></tr><tr><td> $S_{0}$ </td><td>0.000000000000000000E+00</td><td>-0.209715199999999999E+07</td></tr><tr><td> $S_{1}$ </td><td>0.000000000000000000E+00</td><td>0.209715199999999999E+07</td></tr><tr><td> $S_{2}$ </td><td>0.000000000000000000E+00</td><td>-0.104857599999999999E+07</td></tr><tr><td> $S_{3}$ </td><td>0.000000000000000000E+00</td><td>0.000000000000000000E+00</td></tr><tr><td> $S_{14}$ </td><td>0.000000000000000000E+00</td><td>-0.819200000000000000E+04</td></tr><tr><td> $S_{37}$ </td><td>0.000000000000000000E+00</td><td>0.131071999999999999E+06</td></tr><tr><td> $S_{56}$ </td><td>0.000000000000000000E+00</td><td>-0.974848000000000000E+06</td></tr><tr><td> $S_{129}$ </td><td>0.000000000000000000E+00</td><td>-0.747468762500000000E+07</td></tr><tr><td> $S_{130}$ </td><td>0.100000000000000000E+01</td><td>-0.747468762500000000E+07</td></tr><tr><td> $S_{161}$ </td><td>0.100000000000000000E+01</td><td>-0.208844799218738078E+07</td></tr><tr><td> $S_{207}$ </td><td>0.100000000000000000E+01</td><td>-0.104371199218738078E+07</td></tr><tr><td> $S_{236}$ </td><td>0.100000000000000000E+01</td><td>-0.209228699218738078E+07</td></tr></table>

Table 2

<table><tr><td>Mode</td><td>Argument</td><td>Result</td></tr><tr><td>VP (Scalar Mode)</td><td>-20</td><td> $-0.206552909409100166$  E-08</td></tr><tr><td>VP (Vector Mode)</td><td>-20</td><td> $-0.256113708019256592$  E-08</td></tr><tr><td>Inclusion</td><td>-20</td><td> $+0.11783542900387288_{1}^{6}$  E-08</td></tr><tr><td>VP (Scalar Mode)</td><td>-24</td><td> $+0.292800675988536086$  E-07</td></tr><tr><td>VP (Vector Mode)</td><td>-24</td><td> $+0.122934579849243164$  E-06</td></tr><tr><td>Inclusion</td><td>-24</td><td> $+0.72397392420504_{5988}^{6120}$  E-07</td></tr><tr><td>VP (Scalar Mode)</td><td>-27</td><td> $-0.246351252435671272$  E-06</td></tr><tr><td>VP (Vector Mode)</td><td>-27</td><td> $+0.143051147460937500$  E-05</td></tr><tr><td>Inclusion</td><td>-27</td><td> $-0.1144672447209827_{19}^{06}$  E-06</td></tr></table>

Problem: Given a vector $(x_{0}, x_{1}, \ldots, x_{N})$ . Computation of the sum

$$
S := \sum_ {i = 0} ^ {N} x _ {i},
$$

where the vector elements $x_{i}$ are computed as $x_{0} := 1$ ,

$$
x _ {i + 1} := x _ {i} \text {   四   } (\square y) \text {   四   } i, i = 0, \dots , N - 1,
$$

for different values of y and N=200. Numerical results, computed on a VP 400-EX, see table 2. Here the results are compared with a correct inclusion computed with ACRITH or FORTRAN-SC [23], to show that neither the scalar nor vector mode produces correct figures. Note that the correct inclusion of the sum is not an inclusion of the exponential function due to the finite length of the summands. Interval standard functions, however, belong to the runtime system of FORTRAN-SC or PASCAL-SC as well as algorithms to include the solutions of linear or nonlinear systems of equations, of eigenvalue problems and of zeros of polynomials to name only a few.

## 2. Definition of Computer Arithmetic

Shortly said we define computer arithmetic in a way that all basic operations in all spaces that occur in numerical computation deliver a correctly rounded result. None of the spaces which include complex numbers, vector and matrix spaces and intervals can be represented exactly on a computer with finite word length. Therefore we have to define computer arithmetic by a mapping from a space to a proper subspace, usually called a rounding. If the rounding preserves as much of the structure of the original space as possible it is called a semimorphism. In formulas a semimorphism reads as follows.

For a space $M$ and a proper subset $N$ let

□: $M \to N \subset M$

$$
\bigwedge_ {a, b \in N} a \text {   回   } b := \Box (a \circ b),\tag{RG}
$$

$$
\circ \in \{+, -, *, / \}\tag{R1}
$$

$$
\bigwedge_ {a \in N} \square a = a\tag{rounding}
$$

(R2)

$$
\bigwedge_ {a, b \in M} (a \leq b \Rightarrow \square a \leq \square b) (\text { monotone })\tag{R3}
$$

$$
\bigwedge_ {a \in M} \Box (- a) = - \Box (a) \quad (\text { antisym. })
$$

For interval spaces the rounding additionally is outwardly directed

$$
(\mathrm{R} 4) \bigwedge_ {a \in M} a \subseteq \square a
$$

The symbol □ denotes an arbitrary monotone rounding. Particularly interesting are the rounding to the nearest ○ or the directed roundings ∇ (downwardly) or △ (upwardly). This definition of computer arithmetic holds for all spaces of numerical computation. It delivers maximally accurate results, i.e.

$$
\bigwedge_ {a, b \in N} | a \text {回} b - a \circ b | <   \epsilon^ {*} | a \circ b |
$$

where

$$
\epsilon^ {*} <   \left\{ \begin{array}{l l} \frac {1}{2} \beta^ {1 - l} & \text { for } \square = \bigcirc \\ \beta^ {1 - l} & \text { otherwise } \end{array} , \right.
$$

$\beta$ denotes the base and l the mantissa length of the corresponding floating-point format. For matrix multiplication (RG) reads

$$
\begin{array}{l} \bigwedge_ {A, B \in M R} A \boxtimes B := \square (A * B) \\ := \left(\square \sum_ {j = 1} ^ {n} a _ {i j} * b _ {j k}\right) \end{array}\tag{RG}
$$

that means a computation of scalar products with only one rounding.

## 3. Implementation of Arithmetic on Sequential Computers

The implementation of computer arithmetic defined by a semimorphism seems to be impossible since in (RG) the correct (possibly infinitely long) result $a \circ b$ is used and rounded to obtain the approximate result. But whenever $a \circ b$ is not representable on the computer it is sufficient to replace it by an appropriate and representable value $a \tilde{\circ} b$ with $\Box(a \circ b) = \Box(a \tilde{\circ} b)$ . For the four floating point operations $a \tilde{\circ} b$ can be computed either in an accumulator with $2l + 1$ digits and one bit or in an accumulator with $l + 2$ digits and two bits. Efficient implementations of these operations are well known (see the IEEE standard arithmetic processors, [9], for example).

Correct scalar products can be computed in accumulators with $2(l + |\text{emin}| + \text{emax})$ digits where emin and emax denote the minimal and maximal exponent of the floating-point system, respectively. g guard digits are additionally included in the register to prevent intermediate overflows [17]. Since the correct representation of products of floating-point numbers needs 2l digits it suffices to regard summation algorithms.

In practice we do not kneed a long accumulator but only a storage unit. We divide the long register into segments of length l. All the summands have lengt 2l and therefore fit digitwise into a subrange of length 3l of the long register, which is determined by the exponent of the summand. Therefore an accumulator of length 3l receives the appropriate part of the long accumulator, which now only serves as a storage unit and the properly shifted summand is added. The result is written back into the long storage unit and a carry is handled if necessary. Various different carry handling procedures have been implemented in software and hardware [5], [15], [1], [8].

The accurate summation algorithm using the long accumulator or storage unit, respectively, is not the only one known. Another algorithm uses the addition with remainder which means that the sum of two floating-point numbers may be represented exactly by two non-overlapping floating-point numbers.

Definition. Let $x, y \in R(\beta, l)$ be two floating-point numbers with $l$ digits of base $\beta$ then we say that $x$ precedes $y (x > y)$ if either $x$ or $y$ is equal to zero or if $ex(x) \geq ex(y)$ and $x \in R(b, ex(x) - ex(y))$ where $ex(z)$ denotes the exponent of $z$ . $x$ strongly precedes $y$ if $x > y$ and $ex(x) \geq ex(y) + l$ . $x$ and $y$ are called non-overlapping if either $x$ strongly precedes $y$ or vice versa.

For addition with remainder we use the following notation

$$
(s, r) := a + b
$$

where

$s:=a\oplus b$ and $r:=\left\{\begin{array}{ll}b-(s-a)&\text{if } |a|\geq |b|\\ a-(s-b)&\text{otherwise.}\end{array}\right.$

The following lemma holds:

Lemma. If $(s, r) := a + b$ then $s > r \wedge ex(x) \geq ex(r) + l$ .

For the computation of the rounded sum $s$

$$
s = \sum_ {i = 1} ^ {n} x _ {i}
$$

we use the following algorithm AR-sum: repeat $(n - 1)$ times

for $i:=n-1$ downto 1 do

$$
(x _ {i}, x _ {i + 1}) := x _ {i} + x _ {i + 1}
$$

Theorem. During algorithm AR-sum the invariant $s = \sum_{i=1}^{n} x_{i}$ holds. After termination of AR-sum it holds

$$
\Box s = \Box (x _ {1} + x _ {2}) \text {   if   } \Box \in \{\nabla , \Delta \}
$$

$$
\bigcirc s = \left\{ \begin{array}{l l} x _ {1} & \text { if } x _ {2} \notin \left[ \frac {1}{2} - \beta^ {- l}, \frac {1}{2} \right] \cdot \beta^ {e x (x _ {1}) - l} \\ \bigcirc (x _ {1} + x _ {2} + x _ {3}) & \text { otherwise } \end{array} \right.
$$

Proof: [2]

Note that other termination criteria may be used to speed-up the summation.

## 4. Implementation of Arithmetic on Vector Computers

In comparison to general purpose computers, vector processors achieve their high speed of computation by means of pipeline technology whereby during each machine cycle a result is obtained. It is not at all difficult to implement efficiently pipelined floating-point addition, subtraction and multiplication algorithms which fulfill the requirements of a semimorphism. Division needs more circuitry or more than one cycle but is also possible.

<table><tr><td>g</td><td>emax</td><td>l</td><td></td><td>emin</td><td></td></tr></table>

Fig. 1. Long accumulator.

If scalar products and sums are to be computed with high speed on vector processors or supercomputers, one must develop circuits which accept and process one summand (a product) per machine cycle. This is possible only if the addition is done by means of pipeline technology.

In this chapter two different circuits for accurate summation are described. Both are derived from the sequential algorithm using the long accumulator. The first one we call the summing matrix circuit. Consider the long accumulator depicted in fig. 1. This is split into independent adders (by addition we mean addition or subtraction) of width a digits (fig. 2)

Each summand is shifted according to its exponent and split at the borders of each two adders. The addition of the summand may now be performed in parts of width a from right to left where also carries must be handled. The process, however, is inherently sequential and the next summand can only be added if all additions and carry propagations are finished. But we can fold this long accumulator to form a summing matrix (fig. 3).

The summing matrix contains $c \cdot r$ adders of width a arranged in c columns and r rows. a is to be chosen that addition as well as carry registration may be performed in one machine cycle, the relations $c \cdot a \geq l$ and $c \cdot r \cdot a \geq (\text{emax} + l + |\text{emin}|) + g$ determine c and r. Transfer registers including an exponent identification part are contained in each individual adder.

The incoming summands are now first shifted in a shifting unit into the correct position according to their exponents. The shift is executed as a ringshift. This means that the part of the summand which hangs over the right end is reinserted at the left end of the shift register (fig. 3 upper part, summands 2 and 3). The summand is distributed onto the c independent parts of width a of the shift register. Each part receives an exponent identification according to a specific digit in it, e.g. the least significant one. The shifted and expanded summand now drops into the top row of the summing matrix which represents the least significant digits of the long accumulator and thereafter proceeds row by row through the summing matrix, moving ahead one row in each machine cycle. The addition is executed as soon as the exponent identification of a transfer register in the summing matrix coincides with the exponent identification part of the summand.

![](/api/attachments/PQVTT6JG/fulltext/images/636f15570963006926ea893ea970c943d13f179628049579063c7bbc431898ee.jpg)  
Fig. 2. Split accumulator and shifted summand.

If the summand remains connected after shifting the addition is performed in one row of the matrix otherwise the least significant part is added in one row and the most significant part in the adjacent row.

The addition may cause carries. Carry registers between the independent adders absorb these car-ries. In the next machine cycle these carries are added into the next more significant adder, possibly together with another summand. In this way, during each machine cycle one summand can be fed into the summing matrix, although the carry handling of one summand may take several machine cycles.

After input of the last summand the rows can be read starting with the least significant row, provided the row in question does not require any carry handling. In this case the carries first must be removed. The readout process can use the same data path by which the summands pass through the matrix. Thus the result rows follow the last summand on its way through the transfer registers. During the readout process additions and carry handling in the more significant rows may still be executed.

Simultaneously with the readout process the rounding to the required floating-point format can be executed.

For more details see [11].

If the summing matrix is to be realized in VLSI technology it may happen that the complete summing matrix does not fit on a single chip. One should then try to develop components for the columns of the summing matrix since the number of connections (pins) between adjacent columns is much smaller than that between neighboring rows.

An implementation study using the system GENESIL has been carried out [12].

Recall that the summing matrix is an input-driven pipelined device which can accept one operand each cycle and therefore needs no starting time. But since the single result has to drop through the whole matrix we have a finish time proportional to the number of rows r.

![](/api/attachments/PQVTT6JG/fulltext/images/531b1061ad52ec33e917132ba76994ecba09de54cf78bd560defa4702c58324a.jpg)  
Fig. 3. Summation matrix consisting of $h = c \cdot r$ independent adders. $E$ : Exponent identification, $TR$ : Transfer register, $AC$ : Accumulator register.

![](/api/attachments/PQVTT6JG/fulltext/images/b15a0edd881607ca6159051eb14f94a12df4c789697d3edaf73b9b7518670129.jpg)  
Fig. 4. Column of summing matrix.

For a scalar product unit a fast multiplication unit which delivers the exact double-length product of two floating-point numbers has to be added before the summing matrix.

The step from the long accumulator to the long storage unit may be analogously repeated in an appropriate manner and saves a lot of circuitry. In this case we only have one row of adders and the columns are totally decoupled. All entries of one column are stored in a register memory where each cell also contains a carry counter which is wide enough to store the sum of all carries emerging from the addition. (This limits the maximal number of summands, to $2^{k-1}$ where k is the width of the carry counter in bits.)

Each summation step now lasts 4 cycles (see fig. 4)

(1) Exponent identification (EPI), sign and mantissa reach input register (RI) of the device.

2. The memory part (carry and accu) corresponding to EPI and the operand reach the registers before summation (RBS).

3. Addition and transfer of result, carry part and EPI to register after summation (RAS).

4. Storing result and carry part according to EPI.

The two register sets RBS and RAS serve to handle pipeline conflicts which may occur if two different summands have the same exponent identification either directly one after the other or with one other identification in between. In the first case RI and RBS contain the same EPI. Then reading from memory is blocked off and the result of the first addition is written to RBS. In the latter case RI and RAS contain the same EPI. Then again the reading is suppressed and the contents of RAS is written to RBS instead. For details see [11].

## 5. Implementation of Arithmetic on Parallel Computers

Parallel computers achieve their high speed of computation by means of replicating the same processor several times. Computers from 2 through $2^{16}$ processors are on the market. All these processors operate in parallel on different data streams. Mostly the processors are sequential computers which have a floating-point unit and a local memory attached with them. Since scalar products seldom appear isolated in vector and matrix computations it is reasonable to execute scalar products sequentially. We then can use the algorithms described in chapter 3. Sample implementations for the AMT-DAP and Tx-3 computer as well as for pipelined computers [21] have been investigated.

Since on the other hand summation of n elements on a parallel computer may be performed in $\log_{2}(n)$ steps it is interesting to see whether accurate floating-point summation of n elements is also possible in $O(\log_{2}(n))$ time.

The simple example $s = 100 + 4 + 4 + 0$ summed in 2-digits decimal arithmetic following the usual pattern of the log sum algorithm shows that this is not trivial since the elements never change and the result $\bigcirc s = 110$ is never reached.

We can, however, derive other efficient parallel summing algorithms.

The first one is the odd-even summation.

Algorithm OE-sum

(O) for all odd $i$ do

$$
(a _ {i}, a _ {i + 1}) := a _ {i} + a _ {i + 1}
$$

(E) for all even $i \neq n$ do

$$
(a _ {i}, a _ {i + 1}) := a _ {i} + a _ {i + 1}
$$

If steps (O) and (E) are repeated n-1 times and if leading zeros are skipped, all relevant information for the sum is condensed in 3 elements of the original vector. Therefore 2 more steps suffice to compute an approximation with 1 ulp accuracy.

This algorithm is optimal for linearly connected processors.

For other computer models we can derive more efficient accurate summation algorithms. We only have to follow the pattern of a sorting algorithm, using comparison-exchange steps and replace the comparison-exchange operation by an addition with remainder. As one example we suggest the bitonic summation.

Algorithm BS-sum (bitonic summation)

(1) for $i := 0$ to $q - 1$ do

(2) for $j = i$ downto 0 do

(3) for all $k$ where $k \mod 2^j < 2^j$ do

(4) if $k \mod 2^{i+2} < 2^{i+1}$ then

$$
\begin{array}{l} \left(a _ {k + 1}, a _ {k + 2 ^ {j} + 1}\right) := a _ {k + 1} + a _ {k + 2 ^ {j} + 1} \\ \text { else } \end{array}
$$

$$
\left(a _ {k + 2 ^ {j} + 1}, a _ {k + 1}\right) := a _ {k + 1} + a _ {k + 2 ^ {j} + 1}
$$

This algorithm is defined for $n = 2^{q}$ otherwise zeros have to be filled in. The time complexity obviously is $\frac{1}{2} \log n \cdot (\log n + 1)$ . Again we have that all information relevant for the sum is condensed in three elements so that one further pass of BS-SUM or one step (E) followed by a step (0) of OE-sum computes a 1 ulp accurate sum, if zeros are discarded.

## 6. Implementation Overview

In the previous chapters we have developed efficient pipelined or parallel summation units or algorithms so that a computer which provides all vector and matrix operations, namely addition, subtraction and scalar product, can be constructed. We like to finish our paper with an overview of some existing, commercially available implementations of computer arithmetic including optimal scalar products

## References

[1] Arithmos Benutzerhandbuch. SIEMENS AG, Bestell-Nr.: U 2900-J-Z 87-1.

[2] Bohlender, G., Genaue Berechnung mehrfacher Summen Produkte und Wurzeln von Gleitkommazahlen und allgemeine Arithmetik in höheren Programmiersprachen. Dissertation, Universität Karlsruhe, 1978.

[3] Bohlender, G., Rall, L.B., Ullrich, Ch., Wolff v. Gudenberg, J.: PASCAL-SC: Wirkungsvoll programmieren, kontrolliert rechnen. Bibliographisches Institut, Mannheim/Wien/Zürich, 1986.

[4] Bohlender, G., Rall, L.B., Ullrich, Ch., Wolff v. Gudenberg, J.: PASCAL-SC: A Computer Language for Scientific Computation. Academic Press (Perspectives in Computing, vol. 17), Orlando, 1987. (In [10].)

[5] Bohlender, G., Teufel, T.: BAP-SC: A decimal floating-point processor for optimal arithmetic.

[6] Bohlender, G., Wolff v. Grudenberg, J.: Parallel Accurate Summation Algorithms. Interner Bericht, Institut für Angewandte Mathematik, Universität Karlsruhe, 1989.

[7] Hammer, R.: How Reliable is the Arithmetic of Vector Computers? Proceedings of SCAN 89, Academic Press, Orlando, to appear.

[8] High Accuracy Arithmetic. Subroutine library, program description and user's guide, IBM Programm No. 5664-185, Publication No. GC 33-6163.

[9] IEEE Standard for Binary Floating-Point Arithmetic, ANSI/IEEE Standard P754.

<table><tr><td>Computer</td><td>Software Hardware</td><td>Algorithm</td><td>Floating-point format</td><td>Comments</td></tr><tr><td>MC-68000 *</td><td>S</td><td>LA</td><td>PASCAL-SC(13-digit decimal)</td><td></td></tr><tr><td>MC-68000 *</td><td>S</td><td>LA</td><td>IEEE(53-digit dual)</td><td>Initialisation prevents long carry propagation</td></tr><tr><td>intel 80386</td><td>S</td><td>LA</td><td>IEEE</td><td></td></tr><tr><td>APL-PC X A</td><td>S</td><td>AR</td><td>IEEE</td><td></td></tr><tr><td>IBM/370 *</td><td>S/F</td><td>LA</td><td>IBM/370(14-digit hexadecimal)</td><td>cache, 20 opcodes microcode ACRITH/ARITHMOS</td></tr><tr><td>SIEMENS *</td><td></td><td></td><td></td><td></td></tr><tr><td>BAP-SC *</td><td>H</td><td>LA</td><td>PASCAL-SC</td><td>2 accus</td></tr><tr><td>plug-in board (layout)</td><td>H</td><td>LA</td><td>IEEE</td><td>cache memory for fast context switch</td></tr><tr><td>CYBER-205</td><td>S</td><td>AR</td><td>CYBER(47 bit dual)</td><td>suffers from inaccurate basic operations</td></tr><tr><td>VP 400</td><td>S</td><td>AR</td><td>IBM/370</td><td></td></tr><tr><td>chip-set (layout)</td><td>H</td><td>SM</td><td>IEEE</td><td>GENESIL, VAX</td></tr></table>

[10] Kaucher, E., Kulisch, U., Ullrich, Ch. (Eds.): Computer Arithmetic, Scientific Computing and Programming Languages. Teubner, Stuttgart, 1987.

[11] Kirchner, R., Kulisch, U.: Accurate Arithmetic for vector processors. Journal of parallel and distributed computing 5, 250–270, 1988.

12] Knöfel, A.: Entwurf eines Arithmetikprozessors für das optimale Skalarprodukt mit Hilfe eines Silicon Compilers, Diplomarbeit, Universität Karlsruhe, 1988.

[13] Kulisch, U.: Grundlagen des Numerischen Rechnens – Mathematische Begründung der Rechnerarithmetik, Bibliographisches Institut, Mannheim, 1976.

[14] Kulisch, U. (Ed.): PASCAL-SC: A PASCAL extension for scientific computation; information manual and floppy disks; version IBM PC/AT; operating system DOS. B.G. Teubner Verlag (Wiley-Teubner series in computer science), Stuttgart, 1987.

[15] Kulisch, U. (Ed.): PASCAL-SC: A PASCAL extension for scientific computation; information manual and floppy disks; version ATARI ST. B.G. Teubner Verlag, Stuttgart, 1987.

[16] Kulisch, U., Miranker, W.L. (Eds.): A new approach to scientific computation. Proc. of the Symposium held at the IBM Research Center, Yorktown Heights, NY, 1982. Academic Press, New York, 1983.

[17] Kulisch, U., Miranker, W.L.: Computer Arithmetic in Theory and Practice. Academic Press, New York, 1981.

[18] Kulisch, U., Miranker, W.L.: The Arithmetic of the Digital Computer: A New Approach. SIAM Review, Vol. 28, No. 1, March 1986 (pp. 1–40).

[19] Kulisch, U., Stetter, H.J. (Eds): Scientific Computation with Automatic Result Verification. Computing Supplementum 6. Springer Verlag, Wien/New York, 1988.

[20] Kulisch, U., Ullrich, Ch. (Eds): Wissenschaftliches Rechnen und Programmiersprachen. B.G. Teubner Verlag (Berichte des German Chapter of the ACM), Stuttgart, 1982.

[21] Schumacher, G.: Genauigkeitsfragen bei algebraisch-numerischen Algorithmen auf Skalar- und Vektorrechnern. Dissertation, Universität Karlsruhe, 1989.

[22] Ullrich, Ch., Wolff v. Gudenberg, J. (Eds): Accurate Numerical Algorithms. Research Reports ESPRIT, Springer-Verlag, Berlin, 1989.

[23] Walter, W., Ullrich, Ch., Rump, S.M., Metzger, M., Kulisch, U., Bleher, J.H.: FORTRAN-SC, A study of a FORTRAN Extension for Engineering/Scientific Computation with Access to ACRITH, Computing 39, 93–110, 1987.
