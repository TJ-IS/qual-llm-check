---
otero_id: 21615
otero_key: "W6NZ6E4E"
title: "Intelligent solution and analysis of goal programmes: the GPSYS system"
authors: "D.F. Jones; M. Tamiz; S.K. Mirrazavi"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00052-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent solution and analysis of goal programmes: the GPSYS system

D.F. Jones <sup>)</sup>, M. Tamiz <sup>1</sup>, S.K. Mirrazavi <sup>2</sup>

School of Computer Science and Mathematics, DiÕision of Mathematics and Statistics, UniÕersity of Portsmouth, Mercantile House, Hampshire Terrace, Portsmouth, PO1 2EG, UK

Accepted 6 August 1998

## Abstract

An overview of GPSYS, an intelligent linear and integer goal programming system is presented in this paper. The intelligent goal programming system is one which is designed to allow a non-specialist access to, and clear understanding of, goal programming solution and analysis techniques. GPSYS is equipped with GP speed up techniques and analysis tools such as Pareto detection and restoration, normalisation, automated lexicographic redundancy checking and an interactive facility. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Goal programming; Efficient modelling practices; Pareto efficiency

## 1. Goal programming

Goal programming GP is a multi-objective pro- Ž . gramming technique. GP can be considered as a mathematical programming method and a member of the multi-criteria decision making MCDM family.Ž . The variants of GP are numerous and contain many different sub-areas which can bewilder practitioners with no knowledge of GP but wish to apply it to their multi-objective real world situation. Weighted GP WGP , lexicographic GP LGP , ChebyshevŽ . Ž . GP, Fuzzy GP and Min Max GP are all major variants of GP. In addition, each of these variants can have further complicating conditions such as integer variables 4 , non-linear or fractional goals, <sup>w</sup> <sup>x</sup> stocasticity, and non-standard preference functions <sup>w</sup> <sup>x</sup> <sub>7</sub> <sub>.</sub>

## 2. GPSYS: the intelligent goal programming optimiser

A survey of the literature 6 reveals most deci-<sup>w</sup> <sup>x</sup> sion makers using slightly modified linear programming LP software to solve their GP models. This Ž . can lead to inefficiencies in speed and produces difficulties when the modeller wishes to interpret their results or employ more advanced GP modelling and analysis techniques 3,4 . To counteract these<sup>w</sup> <sup>x</sup> problems the GPSYS system 3,4 has been devel- <sup>w</sup> <sup>x</sup> oped.

GPSYS is an intelligent linear and integer goal programming system which is designed to allow a non-specialist access to, and clear understanding of, goal programming solution and analysis techniques. GPSYS allows for the solution and analysis of all variants mentioned above which mixes together the major variants with the advanced conditions, i.e., integer and non-standard preference using a single input style. Thus the decision makers using GPSYS will not find themselves restricted to a particular variant because of software or time considerations.

The basic solution mechanism in GPSYS is a modified revised-simplex LP based solver. It can be called upon to solve any LP sub-problem that should arise in the course of GP solution and analysis. Such calls include minimisation of a weighted GP; minimisation of a priority level in LGP; solution of a modified $\begin{array} { r } { \mathrm { L } _ { \infty } \operatorname { G P } ; } \end{array}$ re-optimisation after an interactive modification; continuous Pareto optimality restoration; calculation of an objective’s upper or lower bound; re-optimisation at a branch and bound node; and integer Pareto optimality detection and restoration 4 .<sup>w</sup> <sup>x</sup>

The GPSYS system allows the use of all of the above analysis and modelling tools simply by the setting of an option in the specification file i.e, at the click-of-a-button 10 .

## 2.1. GPSYS solution techniques

GPSYS is equipped with specialized GP speed up techniques such as advanced starting bases, NPswap, basis restriction, and E-Vector manipulation 3 . In <sup>w</sup> <sup>x</sup> addition to these, the variable fixing method of Ignizio 1 is used in order to ensure efficient solu-<sup>w</sup> <sup>x</sup> tion to LGP models. Different state-of-the-art branch and bound algorithms 4 are available in GPSYS for <sup>w</sup> <sup>x</sup> the solution of pure, mixed and zero–one weighted and lexicographic integer GP models. The above advanced GP speed up techniques and the method in Ref. 1 have been incorporated with the branch and<sup>w</sup> <sup>x</sup> bound techniques for the efficient solution of integer GP models 4 . A Modified form of Chebyshev GP is<sup>w</sup> <sup>x</sup> used to ensure minimal model size and thus more time-efficient solution.

The speed up techniques and considerations lead to faster solution times and the handling of models as large as current large-scale LP’s 2 and provide a<sup>w</sup> <sup>x</sup> good base on which to build the analysis tools and integrated package.

## 2.1.1. GPSYS analysis tools

An area being of equal importance to the solving of a GP model is the correct modelling of the GP. This area has posed real problems in the past for practitioners and has led to several works dealing with the effective modelling of GP and avoidance of common pitfalls 5,9 . In order to aid this process,<sup>w</sup> <sup>x</sup> analysis techniques have been developed and implemented in GPSYS so as to automatically detect, or avoid or to rectify modelling errors. Such techniques include Pareto inefficiency detection and restoration <sup>w</sup> <sup>x</sup> <sup>w x</sup> 4,8 , redundant priority level detection 5 and normalisation techniques to overcome incommensurability 3,9 . In the case of normalisation, the user with<sup>w</sup> <sup>x</sup> experience can select their preferred normalisation technique to the solution of the GP problem. For other users, a hybrid algorithm 9 has been included<sup>w</sup> <sup>x</sup> which measures the level of incommensurability in the model and selects an appropriate normalisation technique based on the result. Alongside these, methods to provide a closer representation of the decision makers utility structure such as interactive algorithms 11 and preference modelling 7 have been<sup>w</sup> <sup>x</sup> <sup>w x</sup> developed. The GPSYS system allows the use of all of the above analysis and modelling tools simply by the setting of an option in the specification file. A format of the specification file is given by Fig. 1.

Some of the techniques, such as lexicographic redundancy checking are automatically used as part of the solution process. Others like Pareto inefficiency detection and restoration, can be set to be automatically triggered in the case of the system detecting inefficiency. Efficiency is then either automatically restored or interactively restored according to the wishes of the user.

The GPSYS system is developed for practitioners not familiar with GP but wishing to apply it to their multi-objective real-world situation as well as GP experts who wish to proceed beyond the standard to more advanced modelling and analysis 3,4 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/W6NZ6E4E/fulltext/images/f39124442ec7a2c9af7a68ea1a211530f7b022aa12c3506dc760a7d10fe012d6.jpg)  
Fig. 1. GPSYS specifications file.

## 2.2. A unified input and an appropriate output format

GPSYS is capable of taking input generated from any LP modelling package which it converts into the appropriate GP model. The input format of all GP variants has the following common components: an objective set; a hard constraint set; a set of target values; and a set of weights corresponding to negative and positive deviations from the target values.

In general there needs to be a balance in the amount of output information given to the user. GPSYS produces format specific to the GP variant and extensions used 3,4 . The following information<sup>w</sup> <sup>x</sup> is produced for each objective: the objective number and name; target and achieved values; and lower and upper bounds. A customised output format can be produced for the advanced analysis of the GP model solved. This output format varies depending upon the type of the GP model e.g., Chebyshev GP, integer LGP, etc.

## 3. Summary

This note has overviewed the benefits of using an integrated goal programming package, such as GP-SYS, over the standard method of solution on an LP solver. The benefits found are greater speed of solution, easier use of analysis techniques, easier access to the whole GP paradigm, and greater scope for experimentation to produce different solutions. The development of such a package as GPSYS should aid GP users in the building of effective, accurate GP models which reflect the reality of the situation they wish to model. It is also hoped that GPSYS will help to broaden the application of the less commonly used variants<sup>r</sup>extensions of GP by bringing their reach of the average GP user. The intelligent nature of the analysis and solution within GPSYS makes it particularly useful for those without much experience of the GP technique but who wish to use GP to build realistic models.

A demonstration version of GPSYS is available upon request from the authors.

## References

<sup>w</sup> <sup>x</sup> 1 J.P. Ignizio, Linear Programming in Single and Multiple Objective Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 2 J.P. Ignizio, T.M. Cavalier, Linear Programming, Prentice-Hall, 1994.

<sup>w</sup> <sup>x</sup> 3 D.F. Jones, The design and development of an intelligent goal programming system, PhD thesis, University of Portsmouth, UK, 1995.

<sup>w</sup> <sup>x</sup> 4 S.K. Mirrazavi, Investigation and development of efficient integer and integer goal programming systems, PhD thesis, University of Portsmouth, UK, 1997.

<sup>w</sup> <sup>x</sup> 5 C. Romero, Handbook of Critical Issues in Goal Programming, Pergamon, Oxford, 1991.

<sup>w</sup> <sup>x</sup> 6 M. Tamiz, D.F. Jones, E. El-Darzi, A review of goal programming and its applications, Ann. Operational Res. 58 Ž . 1993 39–53.

<sup>w</sup> <sup>x</sup> 7 M. Tamiz, D.F. Jones, Improving the flexibility of goal programming via preference modelling techniques, Omega 23 1995 41–48.Ž .

<sup>w</sup> <sup>x</sup>8 M. Tamiz, D. F Jones, Goal programming and pareto efficiency, J. Information Optimisation Sci. 17 2 1996 1–17.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 M. Tamiz, D.F. Jones, An example of good modelling practice in goal programming: means for overcoming incommensurability, in : R. Caballero, F. Ruiz, R. Steuer Eds. ,Ž . Advances in Multiple Objective and Goal Programming, Lecture Notes in Economics and Mathematical Systems, Springer, 455, pp. 29–37.

<sup>w</sup> <sup>x</sup> 10 M. Tamiz, D.F. Jones, S.K. Mirrazavi, Intelligent Solution and Analysis of Goal Programmes: the GPSYS System, Technical Report, School of Computer Science and Mathematics, University of Portsmouth, UK, 1997.

<sup>w</sup> <sup>x</sup> 11 M. Tamiz, D.F. Jones, Interactive frameworks for investigation of goal programming models: theory and practice, J. Multi-Criteria Decision Analysis 6 1997 52–60.Ž .

![](/api/attachments/W6NZ6E4E/fulltext/images/c5a73be2c1f6a8e0f62156196d8f86a6906af6876cfc6c9b793b1001441c8e33.jpg)

Dr. Seyed Keyvan Mirrazavi. He has a BSc in Mathematics and Computing and a PhD in Operational Research from the University of Portsmouth, UK. He is currently a research fellow in the school of Computer Science and Mathematics, University of Portsmouth, UK. His areas of interest include software development, Time-tabling, Genetic Algorithm, Integer Programming, Integer Goal Programming, Pareto Efficiency and its extensions to Integer Goal programming

and their applications to real-life problems. He is also involved in the organisation of the MOPGP international conferences.

![](/api/attachments/W6NZ6E4E/fulltext/images/2175a861b9cc161faef6b903d21d6804da775a2efe07f841be17565140c33786.jpg)

Dr. Dylan Francis Jones. He has a BSc from the University of Southampton, UK and a PhD in Operational Research from the University of Portsmouth, UK. He currently holds a lecturing post at the University of Portsmouth, UK. His research interests include multiple objective optimisation and decision support, goal programming, mathematical programming, heuristic methods, and the design of intelligent software for the analysis and solution of the above math-

ematical methods. He has published articles in international journals including Journal of the Operational Research Society; European Journal of Operational Research; OMEGA; and Computers and Operations Research. He is actively involved with the organisation of the MOPGP conference series and is one of the founders of MOPGP.

![](/api/attachments/W6NZ6E4E/fulltext/images/d4a44be9fc60f14b465e42df0f102612efa8f4eb44efb770440494455e44d889.jpg)

Dr. Mehrdad Tamiz. He is a principa lecturer and consultant in Operational Research. He is based in the School of Computer Science and Mathematics, University of Portsmouth, UK. He has a BSc in Mathematics with Operational Research from University of London, UK and a PhD in Mathematical Programming from Brunel University, UK. His main research interests are in efficient modelling and solving linear, integer, multi-objective and goal program-

ming problems, portfolio selection and analysis, risk analysis and volatility measurement of stocks and shares. He is actively involved with the organisation of the MOPGP conference series and is one of the founders and chairman of MOPGP.
