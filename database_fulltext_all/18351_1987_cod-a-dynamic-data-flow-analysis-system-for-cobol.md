---
otero_id: 18351
otero_key: "V9N85EXZ"
title: "COD — A dynamic data flow analysis system for Cobol"
authors: "T.Y. Chen; H. Kao; M.S. Luk; W.C. Ying"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90061-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# COD - A Dynamic Data Flow Analysis System for Cobol \*

T.Y. Chen
Department of Computer Science, University of Melbourne,
Parkville 3052, Australia

H. Kao, M.S. Luk
Centre of Computer Studies and Applications, University of Hong Kong, Pokfulam Road, Hong Kong

and

W.C. Ying

Dental Data Processing Unit, University of Hong Kong, Pokfulam Road, Hong Kong

This paper presents a description of an automated data flow analysis system for Cobol programs - COD. It detects all data flow anomalies as well as certain kinds of errors and has been found to be a very helpful tool for testing and developing Cobol programs.

Keywords: COBOL, software reliability, data flow analysis, automated testing system, automated development system.

![](/api/attachments/V9N85EXZ/fulltext/images/4944e49dedbf412b1b5ef29613772c633fac0cf94d70f15613dcd6ccfc0addc9.jpg)

T.Y. Chen obtained his B.Sc. and M. Phil. from the University of Hong Kong, M.Sc. and D.I.C. from the Imperial College of Science and Technology, and Ph.D. from the University of Melbourne. His research interests include logic programming, expert systems and software engineering. He has taught at the University of Hong Kong and University of Melbourne. Currently he is a Senior Lecturer in Computer Science at the University of Melbourne.

## 1. Introduction

Large software systems, due to their size and complexity, are usually susceptible to errors in spite of the high cost of development. Errors in certain systems (e.g., air traffic control) may be disastrous. Therefore, it is of paramount importance to test the reliability of such systems, perhaps through automated processes.

![](/api/attachments/V9N85EXZ/fulltext/images/5a6e60b28bfa7fe300b10cb0a09cab5ef61b0a2f9428bbdc7bda7ac052e8d394.jpg)

H. Kao is now an Associate System Analyst of the Wing On Computer System Ltd., responsible for designing software packages for banking and retail department store. Currently he is in charge of the development of the Credit Sales System for the Wing On Department Store. He gained his B.Sc. in Mathematics and Computer Science from the University of Hong Kong in 1983.

![](/api/attachments/V9N85EXZ/fulltext/images/7f816dede31607b8376a3aa0c4f3195bb2c2a7ccc7f1d2805bad1b7e802c05ae.jpg)

![](/api/attachments/V9N85EXZ/fulltext/images/1b4d9c57cfdad2463e993dcb92d0d0c314a1b647ff03d5e025d0ef5a37b36262.jpg)

M.S. Luk is a Senior Computer Officer in the University of Hong Kong. He has over 10 years' experience of system development. Currently his interests are library automation and desktop publishing. He was a science graduate of the University of Hong Kong and obtained his M.B.A. degree in Cranfield Institute of Technology, U.K.

W.C. Ying is the Chief Programmer of the Dental Data Processing Unit of the University of Hong Kong. He is interested in the socio-technical approach to information system implementation and the application of engineering principles in software development. He received his B.Sc. in Electrical Engineering from the University of Hong Kong and his M.Sc. in Information System from the University of London.

In program testing, data flow analysis implies analysis of usages of data in a program (Huang [4]). Detected improper usage of data, known as a data flow anomaly, will give clues to help in identifying the sources and locations of errors in the program and will also reveal impure codings such as unnecessary initialization of variables, redundant codings, etc. This methodology has been found to be useful in improving the quality of software (e.g. see Chan and Chen [2], Chen and Leung [3]).

Osterweil and Fosdick [6] first proposed that detection of data flow anomalies could be performed through the scanning of the source program. Such an analysis is said to be static. Later, Huang [4] proposed that data flow analysis could be performed in parallel with program execution. This is called a dynamic approach. It is achieved by inserting software probes into the original source program; this is known as program instrumentation. The dynamic approach is more powerful than the static approach in revealing and locating anomalies associated with array elements, pointers and parameters passing.

Since Cobol is one of the most widely, if not the most widely used language we have developed a dynamic data flow analysis system for Cobol (COD). This paper presents a description of and experience in using it. The implementation problems and their solutions are also addressed. We have found COD a very useful automated aid to test the reliability and to improve the quality of programs.

## 2. Theoretical Backgrounds of Data Flow Analysis for Cobol

Recently, Kao and Chen [5] pointed out that in order to increase the capabilities of detecting and locating anomalies, the characteristics of data types, data structures, and operations on data must be taken into consideration when defining the types of actions, the types of states, and the state transition diagrams. They proposed new definitions of them for data flow analysis of Cobol programs. These were used in implementing COD. Kao and Chen also showed how the conventional classification of actions into define, reference and undefined are inadequate for Cobol programs. Instead the proposed these actions:

$d$ - define

$r$ - reference

$u$ - undefine

$f$ - input

$w$ - output

o - open

c - close

f is applied by a READ verb; w by a WRITE or REWRITE verb; o by an OPEN verb and c by a CLOSE verb. Otherwise, d occurs to a variable when it is assigned a value; r when its value is non-destructively referenced; and u when its value becomes unknown or undefined.

With the above classification, Cobol programs have the following types of data flow anomalies (a is used to denote an action):

1. $fa$ where $a$ is not $r$ ;

2. df;

3. dd;

4. du;

5. dc;

6. ur;

7. uw;

8. uu;

9. wr;

10. ww;

11. wu;

12. for input mode, oa where a is not f;

13. for output or extend mode, $oa$ where $a$ is not $d$ ;

14. for input-output mode, oa where a is neither f nor d;

15. for files that are declared in the File Section and that have not yet been opened, a where a is not o;

16. for an already opened file, a where a is o;

17. for input mode, $a$ where $a$ is either $d$ or $w$ ;

18. for output mode, a where a is either f or r.
Corresponding to the above types of actions and anomalies, a variable can be assumed to be in one of the following eight states:

$D$ - defined

$R$ - referenced

$U$ - undefined

$F$ - input

W - output

O - opened

$C$ - closed

A - abnormal

The initial state of a variable is assigned as fol-

![](/api/attachments/V9N85EXZ/fulltext/images/f082bf238b9937f093097dbc5c4d1821d2898ba9b97023a910038d3a944d6f1a.jpg)  
Fig. 1. State Transition Diagram for Variables under Files Declared for Input in the File Section.

lows:

1. $C$ if the variable is declared in the File Section;

2. D if the variable is declared in the Working-

Storage Section with association of a VALUE clause;

3. $U$ otherwise.

![](/api/attachments/V9N85EXZ/fulltext/images/34b7b663869d76d9a0cc9e1bb97e1c4f8f25c3f0c64cf083f870e97356a681f8.jpg)  
Fig. 2. State Transition Diagram for Variables under Files Declared for Output in the File Section.

<table><tr><td></td><td>F</td><td>R</td><td>D</td><td>U</td><td>W</td><td>O</td><td>C</td><td>A</td></tr><tr><td>f</td><td> $A^*$ </td><td>F</td><td>A</td><td>F</td><td>F</td><td>F</td><td>A</td><td>A</td></tr><tr><td>r</td><td>R</td><td>R</td><td>R</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td></tr><tr><td>d</td><td>A</td><td>D</td><td>A</td><td>D</td><td>D</td><td>D</td><td>A</td><td>A</td></tr><tr><td>w</td><td>A</td><td>W</td><td>W</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td></tr><tr><td>u</td><td>A</td><td>U</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td></tr><tr><td>o</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td><td>A</td><td>O</td><td>A</td></tr><tr><td>c</td><td>A</td><td>C</td><td>A</td><td>C</td><td>C</td><td>A</td><td>A</td><td>A</td></tr></table>

Fig. 3. State Transition Table for Variables under Files Declared for Input-Output in the File Section.

![](/api/attachments/V9N85EXZ/fulltext/images/717303a9ed706756ead375c8242796610996019817cacbea9e23adac9f233ff2.jpg)  
Fig. 4. State Transition Diagram for Variables Declared in the Working-Storage Section.

When an action is applied on a variable, its state will undergo transitions accordingly to the state transition diagrams as depicted in Figures 1 to 4. Entrance into the state A indicates the occurrence of an anomaly. It should be noted that two consecutive f will not induce an anomaly if some items of its corresponding record have been referenced between the occurrences of these two f actions. For this case, the dotted line should be used in Figure 1, otherwise the solid line should be used. Similarly, in Figure 3, $A^{*}$ is F, otherwise $A^{*}$ is A.

## 3. Structure and Main Features of COD

COD was coded in Pascal using the UWPAS Pascal version, and was implemented on an Univac-1100. The system flowchart of COD is depicted in Figure 5.

Only Cobol programs free of syntax errors may be analysed by COD. The program instrumentation subsystem will insert software probes into the original source program to generate an instrumented program and a reformatted source listing. These software probes are used in tracing data flow anomalies. In the reformatted source listing, a block number and a statement number are attached to every original source statement as an aid in locating anomalies. The instrumented program is then compiled and linked to produce an executable module. Although a Cobol program is normally composed of four divisions: IDENTIFICATION, ENVIRONMENT, DATA and PROCEDURE, it is only necessary to have program instrumentation for the DATA DIVISION and PROCEDURE DIVISION.

Upon execution, in addition to the normal output, anomaly and path reports will also be produced. The anomaly report contains the locations, types, and sources of the anomalies; the path report provides additional information about the executed code.

Since the presence of a data flow anomaly only indicates that a programming error might have been committed, it will be very helpful if errors can automatically be distinguished from anomalies. COD can identify certain types of anomalies as errors; these are treated fatal anomalies.

## 4. Implementation Methods and Problems

## 4.1. Data Division

When COD scans through the DATA DIVISION of a Cobol program, names of identifiers and their associated information (such as the dimensions of a table) will be stored in a symbol table. Such information will be used during the analysis of the PROCEDURE DIVISION. Since a Cobol program usually contains a large number of identifiers, a hash table is used for building this symbol table. A hash table of Cobol verbs and their effective actions is also used. All these will be used during the analysis of the PROCEDURE DIVISION.

![](/api/attachments/V9N85EXZ/fulltext/images/594c854d2f50131c61aea2d08ebadeabf90a2b16bca5797e255518dabf3f5cc6.jpg)  
Fig. 5. System Flowchart of COD.

## 4.2. State Variables

For each variable declared in the Cobol program, COD will generate a state variable to keep track of its transitions. The state variable name is generated by prefixing it with ZS. For example, if variable ABC is declared as:

## 01 ABC PIC...

then the declaration of its state variable $ABC$ is

## 01 ZSABC PIC...

The assignments of the initial values to the state variables are explained later. State transitions are traced by calling subroutine 'ST'. Suppose a statement has actions $a_{1}$ and $a_{2}$ on variables ABC and DEF respectively. Then, the following software probes would be inserted:

CALL 'ST' USING ZSABC, $a_1$ .

CALL 'ST' USING ZSDEF, $a_{2}$ .

## 4.3. Group Items

In a hierarchical structure, there are two types of Cobol data items: group and elementary. A group item is one which has subordinate items, while an elementary item has none. In COD, we assume that if an action is applied to a group item, then the same action is applied to all its subordinate items. It should be noted that file variables are also treated as group items.

As an example, if

```txt
01 A.
02 B PIC X(10).
02 C PIC 9(5).
```

then the program instrumentation for the statement, MOVE SPACE TO A is:

```txt
CALL 'ST' USING ZSB, d.
CALL 'ST' USING ZSC, d.
```

When an action is applied to individual subordinate items, the following rules are obeyed:

(1) if this action directs all subordinate items to the same state, then the group item will be assigned that state;

(2) if the resulting states of the subordinate items are mixed, then the subordinate items are searched for states A, U, R, D in that sequence, and the group item is assigned with the first found state.

Note that other states $(F, W, O$ and C) are not searched for in rule (2). If any of the subordinate items falls into one of these states, all other subordinate items in the same group must follow, then rule (1) applies.

## 4.4.Table

Since dynamic analysis can evaluate the values of table subscripts at execution time, table elements can be analysed individually. COD associates each table element with a state variable by declaring a table of state variables of the same dimensions as the table to be analysed. For example, if we have:

## 02 TABLEA OCCURS 10 TIMES PIC...

then the corresponding table of state variables is declared as:

## 02 ZSTABLEA OCCURS 10 TIMES PIC...

The instrumented software probes for the statement, MOVE 1 TO TABLEA(I), are:

Note that the subscript variable I must be referenced first.

## 4.5. REDEFINES Statement

In a Cobol program, several variables can share the same memory location through the use of a REDEFINES statement in the DATA DIVISION. In referencing such variables, there are two possible cases:

(1) The hierarchical structure and memory size of the redefined items and redefining items are the same.

(2) The hierarchical structure and memory size of the redefined items and redefining items are different.

Handling of case (1) is quite similar to that of variable aliasing in Fortran (Chen and Leung [3]). For an illustration, suppose we have:

$$
\begin{array}{l l l l} 0 2 & A. \\ & 0 3 & B & P I C X (1 0). \\ & 0 3 & C & P I C X (1 0). \\ 0 2 & X R E D E F I N E S A. \\ & 0 3 & Y & P I C 9 (1 0). \\ & 0 3 & Z & P I C 9 (1 0). \end{array}
$$

then the corresponding instrumented software probes are:

<table><tr><td>02</td><td>ZSA.</td><td></td><td></td></tr><tr><td></td><td>03</td><td>ZSB</td><td>PIC...</td></tr><tr><td></td><td>03</td><td>ZSC</td><td>PIC...</td></tr><tr><td>02</td><td>ZSX.</td><td></td><td></td></tr><tr><td></td><td>03</td><td>ZSY</td><td>PIC...</td></tr><tr><td></td><td>03</td><td>ZSZ</td><td>PIC...</td></tr></table>

When there is an action applied on B or C, the same action is assumed to be applied on Y or Z respectively, and vice versa. For the statement, say, MOVE 10 TO Y, its instrumented software probes are

```txt
CALL 'ST' USING ZSY, d.
CALL 'ST' USING ZSB, d.
```

The handling of the data flow analysis for case (2) is different. For example, let us assume we have:

```txt
02 P PIC X(10).
02 Q REDEFINES P.
03 QA PIC 9(5).
03 QB PIC 9(5).
```

then the corresponding instrumented software probes are:
02 ZSP PIC...
02 ZSQ.
03 ZSQA PIC...
03 ZSQB PIC...

The rule used is that $P$ and $Q$ should always have the same state. The rules described in section 4.3 for group items are valid for $Q$ . If actions are applied to $QA$ or $QB$ such that $Q$ 's state changes, then $P$ changes state accordingly.

## 4.6. RENAMES Statement

The use of a RENAMES statement enables one to regroup the data items in a Cobol program. When COD recognizes such statements in the DATA DIVISION, it will store the information about the group of items to be renamed. When a statement has an action on it, the same action will then be applied on all the elementary data items which are renamed. As an example of illustration, suppose we have:

02 A.
03 B PIC X.
03 D PIC X.
03 E PIC X.
66 K RENAMES D THRU E.

Then, the corresponding instrumented software probes for the statement, say, MOVE 'XY' TO K, are

CALL 'ST' USING ZSD, d.
CALL 'ST' USING ZSE, d

## 4.7. PERFORM Statement

There are four possible cases:

(1) The PERFORM statement does not contain UNTIL phrase. There is no instrumentation since no variables are involved in this statement.

(2) The PERFORM statement contains the UNTIL phrase but no VARYING phrase. Suppose we have PERFORM PARA UNTIL I = 50. It should be noted that the condition will be tested irrespective of whether PARA is to be executed or not. Thus, the corresponding instrumented pro-

ZSPARA.
PERFORM PARA.
CALL 'ST' USING ZSI, r.

The main purpose of having an additional paragraph ZSPARA is to incorporate the logic flow correctly.

(3) The PERFORM statement contains the UN-TIL and VARYING phrases. Consider the following statement:

PERFORM PARA VARYING K FROM N BY 1
UNTIL J = 50.

The corresponding instrumented program segment is:

CALL 'ST' USING ZSN, r.
CALL 'ST' USING ZSK, dr.
CALL 'ST' USING ZSJ, r.
PERFORM ZSPARA VARYING K
FROM N BY 1
UNTIL J = 50.

ZSPARA.
CALL 'ST' USING ZSK, d.
PERFORM PARA.
CALL 'ST' USING ZSJ, r.
CALL 'ST' USING ZSK, r.

(4) The PERFORM statement contains the AFTER phrase. The program instrumentation is similar to the previous one.

## 4.8 CALL Statement

In a Cobol program, many subprograms activated by a CALL statement in the main program are stored on a separate file. Usually they are well tested and stored in executable and relocatable form. In such cases, during the instrumentation of the main program by COD, it cannot gain access to the source codings of the subprograms. Also there are technical problems in instrumenting the main program and subprogram separately.

There may be parameters passing between the main program and subprograms, although COD does not perform program instrumentation on the subprogram, with the incorporation of the methodology proposed by Chan and Chen [1], it can still monitor the data flow analysis of parameters. In this method, parameters are classified as:

1. input and left unaltered during the execution of the subprogram;

2. input acting also as output;

3. input acting also as working variables during the execution of the subprogram;

4. output.

We use $P_{i}$ , $P_{io}$ , $P_{iw}$ and $P_{o}$ to denote these four types of parameters. Corresponding to every CALL statement in the calling program, we have the following effective actions: r on $P_{i}$ , rd on $P_{io}$ , ru on $P_{iw}$ and d on $P_{o}$ .

This methodology is not only simple and easy to implement, but it allows data flow analysis to be performed on different program segments independently. If the users of COD want to perform data flow analysis on subprograms, it can be done by changing the subprograms into the form of main programs.

## 4.9. COPY Statement

If the input source code contains COPY statements, COD incorporates the source code from the Cobol library in the form of a listing during a pre-compilation phase. The listing is then used as general input, but it obviously involves a considerable amount of overhead. In fact, it could have been implemented in another way by searching the Cobol library first to obtain the source code. However, the source library is machine dependent, so the first approach was used in COD

## 5. Conclusion

COD uses the techniques of data flow analysis and program instrumentation to detect errors of

Cobol programs. It has been found that COD is easy to use and very helpful in revealing errors. Whenever there is a data flow anomaly, the type of the anomaly, the anomalous variable with subscript values if it is a table element, and the block numbers as well as the statement numbers of the anomalous actions would be output in the anomaly report.

From our experience, COD is more than a testing tool and could be used effectively as a development tool for Cobol programs. It is well known that the earlier the errors are detected, the lower the cost of the software product. Therefore, the methods of COD are recommended for the development phase.

## Acknowledgement

The authors would like to thank Dr. J.T. Yu for his support of this project and Prof. E.H. Sibley for his editorial refinement.

## References

[1] F.T. Chan and T.Y. Chen, "On Data Flow Analysis Across a Subroutine Boundary" Proceedings of International Computer Symposium, Vol. 1, 170–176, 1980.

[2] F.T. Chan and T.Y. Chen, "AIDA - A Dynamic Data Flow Anomaly Detection System for Pascal Programs" (to appear in Software - Practice and Experience).

[3] T.Y. Chen and H. Leung, "The Use of Data Flow Analysis as an Aid to Developing Fortran Programs", Proceedings of the 9th Australian Computer Conference, 240-249, 1982.

[4] J.C. Huang, "Detection of Data Flow Anomaly Through Program Instrumentation", IEEE Transactions on Software Engineering, SE-5, 226-236, 1979.

[5] H. Kao and T.Y. Chen, "Data Flow Analysis for Cobol", SIGPLAN Notices, Vol. 19, No. 7, 18-21, 1984.

[6] L.J. Osterweil and L.D. Fosdick, "DAVE - A Validation Error Detection and Documentation System for Fortran Programs", Software - Practice and Experience, Vol. 6, 473-486, 1976.
