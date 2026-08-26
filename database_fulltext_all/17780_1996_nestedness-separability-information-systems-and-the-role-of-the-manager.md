---
otero_id: 17780
otero_key: "MYXKB2RP"
title: "nestedness, separability, information systems, and the role of the manager"
authors: "John R. Conlon; Sumali J. Conlon; Chi Hwang"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00036-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Nestedness, separability, information systems, and the role of the manager

John R. Conlon $^{a,*}$ , Sumali J. Conlon $^{b}$ , Chi Hwang $^{c}$

$^{a}$ Department of Economics and Finance, University of Mississippi, University, MS 38677, USA $^{b}$ Division of Management Information Systems, Department of Management and Marketing, University of Mississippi, University, MS 38677, USA

$^{c}$ Department of Computer Information Systems, College of Business Administration. California State Polytechnic University, Pomona, CA 91768-4083, USA

Received 20 January 1994; revised 25 August 1995; accepted 2 January 1996

## Abstract

This paper models the information processing problems of a firm by using the computation and optimization of mathematical functions as an analogy to the firm's information processing and decision making activities. This representation allows us to model the division of labor through the concept of functional nestedness, while the decentralization of information and decision making can be modeled through functional separability. The approach is illustrated through a series of simple applications, which examine, for example, how decision problem structures affect the demand for information technology, and how developments in information technology influence the demand for managerial skill.

Keywords: Problem structure; Nestedness; Separability; Division of labor; Decentralization; What-if analysis; Demand for managerial skill

## 1. Introduction

Improvements in information technology have led to an increased emphasis on information processing and decision making in firms (Daft and Lengel, 1986; Galbraith, 1974; Huber, 1982, 1984, Huber and McDaniel, 1986; Tushman and Nadler, 1978). Crucial to this process is the division of labor in the firm (Smith, 1965). However, the problem now becomes, not just how to divide labor among humans, but also how to divide intellectual labor between humans and computers.

Traditionally, information processing and the division of labor in the firm have been modeled through flow charting techniques (Colter, 1984; Couger and Knapp, 1974). Recently, however, Moore and Whinston (1986, 1987) have built on the work of Marschak and Radner (1972) incorporating the tools of information economics to model the firm's information problem. Their approach allows them to analyze information quantitatively, and thus permits the researcher to develop a wide range of interesting new insights.

The purpose of this paper is to supplement this quantitative approach with a treatment of the division of labor, decentralization, and decision problem structure. To do this, we use the computation and optimization of mathematical functions as analogies to the firm's information processing and decision making activities. The concepts of functional nestedness and separability then assume a fundamental importance. Separability is a concept used by economists to model situations in which different decisions depend upon disjoint sets of information, allowing these decisions to be decentralized (see Deaton and Muellbauer, 1980). Functional nestedness is a broader notion, expressing complex functions as compositions of simpler functions. This concept allows us to model the division of labor more generally. Our approach is illustrated through simple examples on topics such as how decision problem nestedness structures affect the demand for information technology, and how developments in information technology affect the demand for managerial skill.

The next section introduces functional nestedness and separability, and relates these concepts to the division of labor and decentralization. Section 3 treats separability and the decentralization of information and decision making, while Section 4 illustrates the concept of nestedness, showing that certain nestedness structures create a comparative advantage for computerized information support over human assistants. Section 5 illustrates the framework by modeling the effect of information systems on the role of the manager, and Section 6 concludes. Some of the issues discussed here are treated in slightly greater depth in the working paper version of this article (Conlon et al., 1995), which is available upon request.

The purpose of this paper is to introduce a framework. Several topics are therefore covered very briefly, and only a few very simple illustrative results are derived. In addition, our primary goal is not to present a systematic methodology for determining which tasks are appropriate for computers as opposed to humans, but rather to provide a framework within which the division of labor and decentralization can be more easily discussed.

## 2. Division of labor, nestedness, and separability

Traditionally, there have been two major approaches to the analysis of the division of labor in organizations: information flow (Burton and Obel, 1980; Daft and Lengel, 1986; Davenport and Short, 1990; Huber, 1982), and decision flow (Bonczek et al., 1981; Huber, 1982; Meador et al., 1986). This paper develops a simple mathematical framework building loosely on these two approaches. First, to model the distinction between information and decisions, consider the problem

$$
\operatorname{Max} _ {b} f (b; x _ {1}, x _ {2}, \dots , x _ {n}),
$$

where b is a variable chosen by the decision maker, and $x_{1}, x_{2}, \ldots, x_{n}$ are data on which the decision maker bases her choice. For example, $x_{1}, x_{2}, \ldots, x_{n}$ may be a set of market prices, and b might be a vector which indicates the choice of which products to produce and in what quantities. The data $x_{1}, x_{2}, \ldots, x_{n}$ represent information, while the choice variable b represents a decision (though decisions at one level of an organization might become information for another level). See Marschak and Radner (1972) for a similar formulation.

The problem immediately arises as to how one can understand the structure of the above problem. This section begins to answer this question by showing how decentralization and the division of labor can be represented through functional nestedness and separability.

![](/api/attachments/MYXKB2RP/fulltext/images/aaa71f5d587e83d9af7fac6db7dc2a0ce8932c523727fc71510c5a49ba15369e.jpg)  
Fig. 1. A flow chart for a nested problem.

## 2.1. Nestedness and the division of labor

This subsection briefly describes the concept of nestedness and relates it to the division of labor. A nested function is one which can be represented as a composition of simpler functions. For example, the function

$$
F (x, y, z) = f (g (x, y), h (x, z))\tag{1}
$$

is nested, since it is obtained by first calculating g and h, and then using these values to calculate $f(g, h) = F$ . This nestedness structure generates the flow chart in Fig. 1. The variables x and y enter into the calculation of g, and x again, and also z, enter into h, after which the values of g and h enter into f, yielding the ultimate value of the function F.

Nestedness may be used to represent possibilities for division of labor in information processing. Thus, each of the simple calculations $f, g$ , and $h$ above can be assigned to a different employee, rather than having a single employee calculate the whole function $F$ . The important point, then, is the relative complexity of the function $F$ , compared to the functions $f, g$ and $h$ . This complexity can be represented by computation costs, e.g., $c_f, c_g$ , and $c_h$ for $f, g$ , and $h$ , respectively. Thus, suppose an individual's ability to handle a problem exhibits increasing marginal costs in the complexity of the problem, so that the cost of having a single person calculate $F$ , $c_F$ say, exceeds $c_f + c_g + c_h$ , then division of labor (e.g., specialization) would reduce computation costs (see Smith, 1965).

## 2.2. Separability and decentralization

The concept of separability is a special case of nestedness. The function $F(x_{1}, x_{2}, \ldots, x_{n})$ , for example, is separable if the set of variables $\{x_{1}, x_{2}, \ldots, x_{n}\}$ can be split into disjoint subsets of variables somehow, e.g., $\{x_{1}, x_{2}, \ldots, x_{k}\}$ and $\{x_{k+1}, x_{k+2}, \ldots, x_{n}\}$ .

![](/api/attachments/MYXKB2RP/fulltext/images/40e0fb3d78c46625e141155c632ffc8e6fa2d1bc866490427e8620d41eadcb6a.jpg)  
Fig. 2. Separability - A particular structure for the flow chart.

$\ldots, x_{n} \}$ such that F can be represented as a composition of functions of these subsets, as in

$$
\begin{array}{r l} F (x _ {1}, x _ {2}, \dots , x _ {n}) & = f (g _ {1} (x _ {1}, x _ {2}, \dots , x _ {k}), \\ & g _ {2} (x _ {k + 1}, x _ {k + 2}, \dots , x _ {n})). \end{array}\tag{2}
$$

Separability, here, requires the variables in $g_{1}$ to be disjoint from the variables in $g_{2}$ . Thus, the function in Eq. (1) above is not separable since x appears in both $g(x, y)$ and $h(x, z)$ .

The functional structure in Eq. (2) generates a flow chart as in Fig. 2. Thus, the variables $x_{1}, x_{2}, \ldots, x_{k}$ are used in the calculation of $g_{1}$ , and the variables $x_{k+1}, x_{k+2}, \ldots, x_{n}$ are used in the calculation of $g_{2}$ , while the values of $g_{1}$ and $g_{2}$ are used in the calculation of $f$ , yielding the ultimate value of the function $F$ . Here $F$ is separable into two subaggregates $g_{1}$ and $g_{2}$ , but an arbitrary number of subaggregates are, in general, possible (see Deaton and Muellbauer, 1980).

While nestedness generates opportunities for division of labor, separability allows informational decentralization as well as division of labor. Thus, since the function in Eq. (2) is separable, the agent who calculates the function $g_{1}$ need only know the values of $x_{1}, x_{2}, \ldots, x_{k}$ , and the agent who calculates $g_{2}$ need only know $x_{k+1}, x_{k+2}, \ldots, x_{n}$ , while the agent who calculates f need only know the values of $g_{1}$ and $g_{2}$ calculated by the other two agents. Thus, the agent who evaluates f need not know all the variables upon which f ultimately depends, since the agents who calculate $g_{1}$ and $g_{2}$ aggregate the original variables ( $x_{1}, x_{2}, \ldots, x_{n}$ ) into two subaggregates ( $g_{1}$ and $g_{2}$ ). That is, if we think of the agent who calculates f as “upper management” (as opposed to, say, the “middle management” who calculate $g_{1}$ and $g_{2}$ ), then the existence of these subaggregates vastly simplifies the upper manager’s task (for a paper examining a special case of information aggregation, see Banker and Datar, 1989).

We may also want to define “near separability” as the case where subaggregates have some, but very few variables in common, as in, e.g., the function:

$$
\begin{array}{r l} F (x _ {1}, x _ {2}, \dots , x _ {4 0}) & = f (g _ {1} (x _ {1}, x _ {2}, \dots , x _ {1 9}, x _ {2 0}), \\ & g _ {2} (x _ {1 9}, x _ {2 0}, \dots , x _ {4 0})). \end{array} \tag {3}
$$

Here $g_{1}$ and $g_{2}$ have only two variables in common, $x_{19}$ and $x_{20}$ . Such near separable functions will also permit some informational decentralization, though less. E.g., for Eq. (3), the agent who calculates $g_{1}$ and the agent who calculates $g_{2}$ must both know $x_{19}$ and $x_{20}$ . However, the $g_{1}$ -agent does not need to know $x_{21}$ through $x_{40}$ , and the $g_{2}$ -agent does not need to know $x_{1}$ through $x_{18}$ .

A serious definition of near separability, of course, would have to be more precise. For example, Conlon et al. (1995) argue that a function like

$$
\begin{array}{r l} F (x _ {1}, x _ {2}, \dots , x _ {4 0}) & = f (g _ {1} (x _ {1}, x _ {2}, \dots , x _ {2 9}, x _ {3 0}), \\ & g _ {2} (x _ {1 1}, x _ {1 2}, \dots , x _ {4 0})) \end{array} \tag {4}
$$

should be considered near separable if, say, $x_{21}$ through $x_{30}$ are unimportant to $g_{1}$ , and $x_{11}$ through $x_{20}$ are unimportant in $g_{2}$ , where importance is measured by the value of information (Marschak and Radner, 1972; Moore and Whinston, 1986; West and Courtney, 1993). However, a full discussion here would take us too far afield.

The concepts of separable and near separable functions find analogies in the concepts of decomposable and near decomposable dynamical systems, discussed by Simon and Ando (1961) and Courtois (1985). Simon and Ando show, for example, that, in short term analysis, one can ignore interactions between loosely connected subsystems when analyzing interactions within these systems, and that, in long term analysis, one can ignore interactions within these subsystems when studying interactions between them. However, they focus on predicting dynamical systems, while we focus on the decomposition of complex decision problems.

Nestedness and separability provide a convenient framework within which to model the information processing problem of the firm. This may be why two recent models of hierarchical firm structure assume highly separable information processing problems. Radner (1992) models the problem of a firm as adding a large set of numbers quickly with a given set of processors, while Sobel (1992) considers a firm which must count a large number of objects, and occasionally loses count. Both problems are separable in an arbitrary manner, and so, put no constraints on the division of labor or the decentralization of information in the firm.

## 3. Separability and the decentralization of information and decision making

This section considers the role of separability in organizational decentralization. Two different types of decentralization must be distinguished here: decentralization of information and decentralization of decision making. We illustrate these two concepts through a series of three representative organizational problem structures. For an analysis of information decentralization in the absence of separability, see Marschak and Radner (1972).

The most favorable case for decentralization in a firm would be a problem such as choosing a, b, c and d to maximize:

$$
\begin{array}{r l} & F (a, b, c, d; x _ {1}, x _ {2}, \dots , x _ {8}) \\ & \quad = f (g _ {1} (a, b; x _ {1}, x _ {2}, x _ {3}), \\ & \quad g _ {2} (c; x _ {4}, x _ {5}), g _ {3} (d; x _ {6}, x _ {7}, x _ {8})). \end{array}\tag{5}
$$

This function is separable in both the decision variables $a, b, c, d$ , and the data $x_{1}, x_{2}, \ldots, x_{8}$ . Thus, if $f$ is increasing in $g_{1}, g_{2}$ and $g_{3}$ , then the problem of choosing $a, b, c$ and $d$ to maximize $F$ can be divided up among three departments, e.g., responsibility centers or decision units (Duncan, 1974), who maximize $g_{1}, g_{2}$ and $g_{3}$ separately. Since the function is separable in the decision variables, and $f$ is increasing in the $g$ 's, departments do not share responsibility for any decision variables, so they do not need to coordinate. Similarly, since the function is separable in the data, departments do not need to share information. Thus, this problem allows decentralization of both information and decision making.

By contrast, consider the problem

$$
\begin{array}{r l} & F (a, b, c, d; x _ {1}, x _ {2}, \dots , x _ {8}) \\ & \quad = f (g _ {1} (a, b; x _ {1}, x _ {2}, x _ {3}), \\ & \quad g _ {2} (c; x _ {3}, x _ {4}, x _ {5}, x _ {6}), g _ {3} (d; x _ {5}, x _ {6}, x _ {7}, x _ {8})). \end{array}\tag{6}
$$

This problem does not allow informational decentralization, since the $g_{1}$ and $g_{2}$ departments both need to know $x_{3}$ , and the $g_{2}$ and $g_{3}$ departments both need to know $x_{5}$ and $x_{6}$ . However, Eq. (6) does allow decentralization of decision making, if f is increasing in the g's.

The differences between the problems in Eq. (5)

and Eq. (6) have implications for the structure of the organization's internal communications and data base system. In problem (5), each department could maintain its own relatively simple database, with no coordination between departments. In problem (6), the firm might benefit from a centralized database, designed so that each department can use the information it needs, without dealing with the data used by other departments. This would represent a centralized database with views, which could be maintained using a sophisticated database management system such as ORACLE or DB2.

Problems like Eq. (6) might also describe geographically decentralized organizations, with different locations depending mainly on local data, but also using data from other locations. Such problems might be “near separable” in the data, and so, call for partially distributed database systems. As Gavish and Pirkul (1986) point out for branch banking, “most transactions related to a customer’s activity can be channeled to a local processor which contains a local database, thus significantly reducing the long distance communication costs and delays that are associated with a centralized system.” Of course, the design of such systems will also depend on concurrency costs and the relative frequency of queries versus updating (Ram and Narasimhan, 1994).

The issue of near separability can be illustrated using a simple model of a distributed firm, with two locations, A and B, say, and two database fragments, a and b (richer models would require sophisticated numerical optimization techniques – see, e.g., Dowdy and Foster, 1982; Ram and Narasimhan, 1994). Ignore concurrency costs, etc., and assume fragment a is more closely related to location A, and similarly for b and B. In this setup, one can compare costs of various distributed structures. Thus, having fragment a at location A and fragment b at location B will tend to be superior to having both at one location if cross updates are less common than own updates, and cross queries are less common than own queries. Similarly, this distributed structure will tend to be superior to having both fragments at both locations if cross queries are less common than own updates (see Conlon et al., 1995 for details). These conditions all clearly reflect near separability.

Other issues are of course also relevant. E.g., with concurrency costs, if queries are common relative to updates, then networks with multiple copies of files will tend to be relatively more efficient (Ram and Narasimhan, 1994). See also King (1983), and, for a discussion of some of the enormous body of literature on the file assignment problem, Dowdy and Foster (1982) and Ram and Narasimhan (1994).

Finally, consider the decision problem of choosing a, b, c, and d to maximize

$$
\begin{array}{r l} & F (a, b, c, d; x _ {1}, x _ {2}, \dots , x _ {8}) \\ & \quad = f (g _ {1} (a, b; x _ {1}, x _ {2}, x _ {3}), g _ {2} (b, c; x _ {4}, x _ {5}), \\ & \quad g _ {3} (d; x _ {6}, x _ {7}, x _ {8})). \end{array}\tag{7}
$$

Here the $g_{1}$ and $g_{2}$ departments are both affected by the decision variable b.

Problem (7) allows informational decentralization, but not decentralization of decision making. Some mechanism is thus needed in Eq. (7) to resolve conflicts between the $g_{1}$ and $g_{2}$ departments. Robey's description of the crew scheduling problem of a U.S. airline gives an example of a decision making structure appropriate for this sort of problem (Robey, 1981). The airline set up a System Operation Center to handle interruptions in flight scheduling. "Planners from pilot utilization, flight attendant utilization, aircraft routing, and customer service" departments would coordinate through this center, using "separate real time information systems to support joint problem solving" (emphasis added). This center therefore facilitates joint decision making with significant information decentralization.

Alternatively, some sort of central authority could impose a choice of $b$ on the $g_1$ and $g_2$ departments, possibly based on some subset of the information in $\{x_1, x_2, x_3, x_4, x_5\} - \text{say } b = b^*(x_1, x_2, x_5)$ , if the central authority does not know $x_3$ or $x_4$ . The two departments would then take $b^*$ as given when choosing $a$ and $c$ . A third approach could grant authority over $b$ to one of the departments. For example, control over $b$ could be granted to the $g_1$ department. This department could thus choose $b$ to maximize $g_1$ , so $b$ would be a function of $x_1, x_2$ , and $x_3$ , as in $b = b^*(x_1, x_2, x_3)$ . The $g_2$ department would then take $b^*$ as given, and choose $c$ to maximize $g_2(c, b^*, x_4, x_5)$ , yielding $c = c^*(b^*(x_1, x_2, x_3), x_4, x_5)$ , so the $g_1$ department's choice of $b$ would become data from the point of view of the $g_2$ department.

Finally, the firm could use a transfer pricing scheme to induce the $g_{1}$ department to take partial account of the interests of the $g_{2}$ department or visa versa (Conlon et al., 1995). The transfer pricing scheme will depend on the forms of f, $g_{1}$ and $g_{2}$ , so there is additional information which can be incorporated into Eq. (7) beyond just the flow of information.

## 4. Nestedness and the division of labor between managers and information systems

This section uses nestedness to model the division of labor between routine and unstructured tasks. It then shows that decision problems with certain types of nestedness structures tend to require what-if analysis, and so, create information processing needs for which computers have a relative advantage compared to human assistants or clerks.

## 4.1. The division of labor between routine and unstructured tasks

We begin by writing down an extremely simple model of a decision problem with routine and unstructured components, where the routine part can be assigned to either a human assistant or an information system. A decision problem will be unstructured if it changes frequently in nature, or involves unusual elements (Gorry and Scott-Morton, 1971; Simon, 1951, 1960). Such problems are better handled by human managers than by information systems, since information systems are less capable than humans of handling “novel” situations (Jacob et al., 1989). Novel situations may also be better handled by managers than by human assistants who follow routinized bureaucratic procedures. As Rao et al. (1992) point out, a novice “tends to mechanically utilize concepts” while an expert is “more creative in his or her approach” to problem solving.

Thus, suppose the manager must choose a decision variable b, say, to maximize

$$
F ^ {\#} (b; x _ {1}, x _ {2}, \dots , x _ {n}),\tag{8}
$$

where $x_{1}, x_{2}, \ldots, x_{n}$ are data or information relevant to the problem and within the manager's knowledge domain. Suppose also that the function $F^{\#}$ is difficult to systematize or automate. We use the pound sign (\#), here, to indicate that $F^{\#}$ is difficult to systematize.

An information system or human assistant can then help the manager if the manager's original unstructured problem can be split up into subproblems, some of which are routine in nature, and so, can be handled by the information system or assistant, leaving the manager with a residual problem which is still unstructured, and so, requires managerial judgement, but is simpler than the original problem. Such problems are called “semistructured” (Gorry and Scott-Morton, 1971), since, as described by Keen (Keen, 1976), “parts of the analysis have sufficient potential for systematization for the computer to be of value, but... the decision maker's insight and judgement are needed to control the process.”

Thus, suppose the function $F^{\#}$ is nested as in:

$$
\begin{array}{r l} & F ^ {\#} (b; x _ {1}, x _ {2}, \dots , x _ {n}) \\ & = f ^ {\#} (b; x _ {1}, x _ {2}, g (x _ {2}, x _ {3}, \dots , x _ {n})), \end{array}\tag{9}
$$

where the g function is sufficiently routine to assign to an information system or assistant, while $f^{\#}$ is still unstructured (we include $x_{2}$ in g and also directly in $f^{\#}$ to emphasize that we are not requiring separability in the data). Here g might be a simple statistical summary of the data $x_{2}, x_{3}, \ldots, x_{n}$ . Alternatively, g may be, e.g., a complicated prediction statistic.

If the problem is nested in this way, and the calculation of g is delegated to an information system or assistant, the manager's problem can be reduced to the potentially simpler problem of optimizing $f^{\#}(b; x_{1}, x_{2}, g)$ , where the value of g is given to the manager by the information system or assistant. Problem structures like Eq. (9) will be generated if the manager needs to base decisions on some function of environmental variables, which does not include any of the manager's decision variables.

If there is only one, fairly routine way of calculating g, then it seems plausible that, in the absence of an information system, g will be calculated by an assistant, rather than by the manager, whose time is more valuable. However, in many applications, the information system takes over tasks which had not previously been performed by a human assistant.

One possible explanation for this is that there might be several different methods of performing this task. One method might draw on the superior judgement and experience of the manager, while another method might be more structured and so more appropriate for an assistant (again, see Rao et al., 1992), but very computation-intensive. If the structured approach is too difficult, then, in the absence of an information system, it may be easier for the manager to use her own judgement to solve the problem. Computer technology may then reduce the relative cost of the structured approach, and so, introduce a division of labor between the manager and the information system where none previously existed between the manager and human assistants. Other explanations, of course, are also possible.

The relative advantage of computers compared to human assistants will, of course, depend in part on the cost and power of computers. A second factor, however, will be how repetitive the task is. A task which will be performed only once may be better assigned to a clerk, or to the manager's intuitive judgement. However, if a series of similar tasks is to be performed repeatedly over time, then it may be worth while to make the investment in a system capable of performing all of the repetitions of these tasks.

To see this, let $c_{A}$ be the cost of one repetition of the relevant type of calculation by the assistant, let $c_{P}$ be the cost of programming the computer to do the calculation, and let $c_{C}$ be the cost of a single repetition of the calculation by an appropriately programmed computer. Then $C_{A}=k\;c_{A}$ , is the cost of having an assistant perform k repetitions of the task, while the cost of performing the k repetitions on a computer is $C_{C}=c_{P}+k\;c_{C}$ . Presumably, $c_{C}$ will be much smaller than $c_{A}$ , so $C_{C}$ will be smaller than $C_{A}$ when k is large. This will be important in our discussion of what-if analysis below.

## 4.2. Nestedness, what-if analysis, and DSS

The discussion in last subsection might apply to an information system which does statistical analysis of previously collected data. However, in many cases users must interact with information systems in more complicated ways, employing, e.g., what-if analysis or simulation on a DSS. This subsection briefly considers one such scenario.

Consider the problem of choosing a and b to optimize the nested function

$$
\begin{array}{r l} & G ^ {\#} (a, b; x _ {1}, x _ {2}, \dots , x _ {n}) \\ & = g ^ {\#} (a, b; x _ {1}, x _ {2}, h (b, x _ {2}, x _ {3}, \dots , x _ {n})), \end{array}\tag{10}
$$

say, where $G^{\#}$ and $g^{\#}$ are unstructured, while h is more routine. This is a situation in which some decision variable, b, enters into the potentially automated problem, h, but also has “unsystematic” effects. The variable therefore also enters directly into the function $g^{\#}$ , which cannot be treated systematically by an information system (see Fig. 3).

This type of problem may arise in simulation analysis. Thus, h might be a model in the model base describing the short term effects of output price on demand and profits, while the longer term effects (such as responses by other firms), may be more difficult to model, and so, may be left for the manager to consider in an intuitive, but unsystematic way.

Another example would be the facility location problem (Murty, 1976). The choice variable b would then be a vector of proposed plant locations, output levels, etc., h would be the standard objective function, and the data $x_{2}$ , $x_{3}$ , ..., $x_{n}$ would be the standard inputs into the facility location problem. Since facility location involves additional issues besides those considered in the usual optimization problem (e.g., local regulations, infrastructure, etc.), the vector of locations in b would also enter the unsystematic part of the decision problem in Eq. (10).

Problems such as Eq. (10) present difficulties which did not appear in problems like Eq. (9), even though Eq. (10) is also nested. In particular, the information system cannot calculate the function h until the manager has chosen a value for $b$ , and the manager cannot choose $b$ until the system has calculated $h$ . The manager will therefore have to use the information system in a more interactive manner. For example, the manager might choose a series of values of $b$ , have the system evaluate $h$ , and then consider the implications of these values of $b$ and $h$ for the problem $g^{\#}(a, b; x_1, x_2, h)$ . This would be essentially “what-if” analysis.

![](/api/attachments/MYXKB2RP/fulltext/images/1e760074bd52eb8cbf0e9e1cab820e7dbc39246cd6bf6a2799aed95da074fc11.jpg)  
Fig. 3. A problem requiring what-if analysis.

Alternatively, in a problem such as the facility location problem, the system may propose an initial suggested distribution of facilities. The manager would then consider each of the proposed locations in detail, and eliminate some on the basis of information such as local regulations, etc. The system could then reoptimize with the set of possible sites appropriately reduced. Thus, the system would again need to allow the manager to manipulate choice variables to assess the consequences of various possible decisions (see, e.g., Randhawa and West, 1995 for a discussion of a similar two-phase procedure).

One interesting consequence of this problem structure is that, since the solution to a single maximization problem such as Eq. (10) may require what-if analysis, it would therefore require the repeated performance of very similar calculations. However, this is precisely the sort of situation which favors the use of an information system rather than a human clerk, as we saw at the end of the previous subsection. Since similar calculations must be performed repeatedly, the initial programming investment, $c_{p}$ , becomes worthwhile. In other words, when the problem has a nestedness structure of the form in Eq. (10), computerized information systems acquire an additional advantage over human assistants. With an information system, the user does not need to begin with the precisely appropriate question, because the system reduces the marginal cost of asking a series of related questions as the user refines her ideas.

The model also yields additional insights. For example, if the problem being simulated involves a large number of decision variables, then it will become more difficult for the manager to get a clear sense of the problem's behavior. Thus, the manager may need more repetitions to understand the situation well. This will further increase the advantage of the computer system as compared to a human assistant, even if we hold programming costs, $c_{P}$ , and the relative computation costs per repetition, $c_{A}$ and $c_{C}$ , constant.

5. An illustration: Information systems and the role of the manager

This section uses the framework of Section 4 to examine how an information system affects a firm's demand for managerial skill. Specifically, we show that this effect may depend crucially on the firm's returns to scale in complexity.

Consider the following spectrum of possible information processing problems for the firm, which increases in complexity as n increases:

$$
\operatorname{Max} _ {b} F ^ {n} (b; y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n}).\tag{11}
$$

Here b is a choice variable, and the x's and y's are data on which the choice of b will be based (the y's are distinguished from the x's because they will soon be incorporated into an information system). We measure complexity simply in terms of the number of variables the manager must consider, $m + n$ . Richer measures are, of course, possible (e.g., we could treat m and n as separate components of complexity; see below).

For specificity, assume that $F^{n}$ takes the form

$$
\begin{array}{r l} & F ^ {n} (b; y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n}) \\ & = M (n) - \left[ G ^ {n} (y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n}) - b \right] ^ {2} \end{array}\tag{12}
$$

and note that $F^{n}$ achieves its maximum value of $M(n)$ when b equals $G^{n}$ . Assume that $M(n)$ is increasing in n, so more complex problems yield higher attainable values of $F^{n}$ .

Finally, suppose that the board of directors of a firm simultaneously chooses one of these problems to solve, and a manager to solve it. Clearly these two choices will be interrelated. In the long run we assume that both of these variables adjust optimally.

Once the manager is hired, her problem is essentially to estimate the function $G^{n}$ as accurately as possible. Assume that $G^n$ is separable in the following way:

$$
\begin{array}{r l} G ^ {n} \big ( & y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n} \big) \\ & = g ^ {n} \big (h \big (y _ {1}, y _ {2}, \dots , y _ {m} \big); x _ {1}, x _ {2}, \dots , x _ {n} \big), \end{array}\tag{13}
$$

with h sufficiently structured that it can be computed by an information system (but also so complicated that it would be better to have the manager solve the problem using judgement than to have a human assistant use a structured approach; see Section 4.1). We will consider the firm's problem with and without the assistance of this information system.

Suppose first that the manager is unassisted by an information system. The accuracy of the manager's estimate of $G^{n}$ will depend on the complexity of the problem and on the skill of the manager. Thus, assume that the manager's estimate of $G^{n}$ is given by

$$
\begin{array}{r l} b ^ {*} = G ^ {n} \big ( & y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n} \big) \\ & + \alpha (s, m + n) \epsilon , \end{array}\tag{14}
$$

where $\epsilon$ is a random variable with mean zero and variance $\sigma_{\epsilon}^{2}$ , s is the manager's skill, $m + n$ measures the complexity of the problem, and $\alpha(s, m + n)$ is a factor determining the size of the estimation error. Since $\epsilon$ has mean zero, the manager does not make systematic errors in one direction or the other. Systematic errors could presumably be corrected with experience.

Managerial skill, here, is defined to be whatever intrinsic qualities allow the manager to make better decisions (in this case, whatever allows the manager to choose $b^{*}$ more accurately). Thus, assume that $\alpha_{1}<0$ (skill reduces estimation errors), where subscripts denote partial derivatives. Also, assume that $\alpha_{2}>0$ (complexity increases estimation errors), and that $\alpha_{12}<0$ (managerial skill reduces errors more, the more complicated the problem is). Note that there are many dimensions of managerial ability, for example, supervision skills, which are being ignored in this formulation.

If the manager chooses $b^{*}$ as in Eq. (14), the expected payoff to the firm will be

$$
\begin{array}{r l} & E F ^ {n} \big (b ^ {*}; y _ {1}, y _ {2}, \dots , y _ {m}; x _ {1}, x _ {2}, \dots , x _ {n} \big) \\ & = M (n) - \big [ \alpha (s, m + n) \big ] ^ {2} \sigma_ {\epsilon} ^ {2}. \end{array}\tag{15}
$$

Define the function $\beta(s, m+n)$ to be $\beta(s, m+n) = [\alpha(s, m+n)]^2 \sigma_{\epsilon}^2$ , and let the cost to the firm of hiring a manager with skill $s$ be $c(s)$ , with $c'(s) > 0$ (note that we are holding other factors constant, such as the availability of managers of a given skill level). Then the expected benefit to the firm, net of the cost of managerial skill, becomes

$$
M (n) - \beta (s, m + n) - c (s).\tag{16}
$$

The board of directors must choose skill s and complexity n to maximize this expression.

We now ask how the introduction of an information system affects the choice of skill level. We model the information system as reducing the value of m. Thus, if this system is used to calculate $h(y_{1}, y_{2}, \ldots, y_{m})$ , the manager's problem reduces to maximizing

$$
M (n) - \left[ g ^ {n} (h; x _ {1}, x _ {2}, \dots , x _ {n}) - b \right] ^ {2}\tag{17}
$$

in which m has essentially been reduced to one. Thus, the manager's solution will take the form $b^{*}=g^{n}(h;x_{1},x_{2},\ldots,x_{n})+\alpha(s,n+1)\epsilon$ , where the complexity, $m+n$ , of the problem has been reduced to $n+1$ by use of the information system, so the error, $\alpha(s,n+1)\epsilon$ has a smaller variance (simpler problems have smaller estimation errors). The expected benefit net of the cost of managerial skill therefore becomes $M(n)-\beta(s,n+1)-c(s)$ , which is identical to expression (16) above, except that m has been replaced by 1.

Of course, the manager will have to expend some skill or effort in managing either the information system, or the personnel responsible for managing the information system. Still, it seems reasonable to model the effect of the information system as reducing m. Thus, the introduction of the information system may reduce the complexity of the manager's original task from $n + m$ to $n + 1$ , while managing the system increases the complexity of his/her task from $n + 1$ to $n + m_{1}$ . This will represent an overall reduction in complexity if $m_{1} < m$ . However, this analysis conflates two potentially quite different dimensions of managerial skill: decision making and supervision.

Thus, to determine the effect of the introduction of an information system on the demand for managerial skill, we should examine the effect of a reduction in m on the firm's optimal choice of s. In the present framework, the direction of this effect depends only on whether the marginal returns to complexity are diminishing $(M'(n))$ decreasing, so

$M''(n) < 0$ or increasing $(M'(n) \text{ increasing, so } M''(n) > 0)$ .

Proposition 1. Under diminishing returns to complexity, the introduction of an information system, which reduces m, will also reduce the optimal choice of s, i.e., it will reduce the firm's demand for managerial skill. Similarly, if the marginal benefit of complexity is increasing, then the introduction of an information system will increase the firm's demand for managerial skill.

Proof. This uses standard optimization techniques (see Conlon et al., 1995).

This result can be understood by considering the effect of an information system on the optimal level of complexity of the manager's residual decision problem. Under increasing returns to complexity, for example, when m is reduced by the introduction of an information system, the optimal total complexity of the manager's decision problem, $m + n$ , is actually increased. The information system, by simplifying the manager's initial problem, allows the firm to benefit from the increasing returns offered by more complicated problems. Since the complexity of the manager's problem increases, the firm needs a more skilled manager, so the firm's demand for managerial skill rises (see Conlon et al., 1995 for details).

These results, of course, are based on several restrictive assumptions. Nevertheless, they suggest strongly that, to understand the effect of improvements in information technology on the firm's demand for managerial skill, we should understand the returns to complexity for the firm. For example, suppose that we modify the model to allow the component of complexity represented by m to enter the decision error factor $\alpha$ differently from the component represented by n, so we must write $\alpha = \alpha(s, m, n)$ , rather than $\alpha = \alpha(s, m + n)$ . Suppose also that $\alpha_{sm} < 0$ (this is a natural generalization of $\alpha_{12} < 0$ above). Then, while our results are not as clean as those in Proposition 1 above, it is still the case that an information system, which decreases m, is more likely to increase demand for managerial skill, if there are increasing returns to complexity. It would, of course, also be interesting to explore these issues using the framework of Section 4.2, rather than Section 4.1.

## 6. Conclusion

As several authors have argued (e.g., Colter, 1984; Necco et al., 1987), no single modelling technique can represent all aspects of the typical firm's complex information processing problem. A combination of approaches has therefore been encouraged. Mathematical representations of separability and nestedness structures can capture many dimensions of a decision problem, though at the cost of considerable complexity. Thus, if an analyst wants to obtain a simple overview of a wide range of interrelated data flows in a single model, the present approach may be prohibitively difficult, and an information flow diagram may be more appropriate. On the other hand, the approach here can encompass a rich set of factors within a single model, and may therefore be most appropriate when the analyst wishes to obtain a deeper understanding of the interrelations between the different aspects of a given decision problem structure.

We have illustrated this approach through a series of very simple applications. Some additional applications might include (a) extending the discussion in Section 3 to allow for information consolidation departments such as accounting departments, (b) modelling the optimal use of a DSS by a boundedly rational manager, to perform what-if analysis for nontrivially nested problems like that in Section 4.2, (c) using nestedness to represent the building up of models from simple components in a Model Management Systems framework (Blanning, 1993), and (d) capturing some of the other aspects of managerial skill, such as supervision or leadership, in addition to superior problem solving ability.

## Acknowledgements

Unusually detailed comments from two anonymous referees, and suggestions from Andrew Whinston, have led to major improvements in this paper. Any remaining errors are, of course, our sole responsibility.

## References

R.D. Banker and S.M. Datar, Sensitivity, Precision, and Linear Aggregation of Signals for Performance Evaluation, Journal of Accounting Research 27, No. 1 (Spring 1989) 21–39.

R.W. Blanning, Model Management Systems: An Overview, Decision Support Systems 9, No. 1 (Jan. 1993) 9–18.

R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundation of Decision Support Systems (Academic Press, New York, 1981).

R.M. Burton and P. Obel, A Computer Simulation Test of the M-Form Hypothesis, Administrative Science Quarterly 25, No. 3 (Sept. 1980) 457–466.

M.A. Colter, A Comparative Analysis of System Analysis Techniques, MIS Quarterly 8, No. 1 (March 1984) 51–66.

J.R. Conlon, S.J. Conlon and C. Hwang, Nestedness, Separability, Information Systems, and the Role of the Manager, Working Paper, University of Mississippi (March 1995).

J.D. Couger and R.W. Knapp, System Analysis Techniques (Wiley, New York, 1974).

P.-J. Courtois, On Time and Space Decomposition of Complex Structures, Communications of the ACM 28, No. 6 (June 1985) 590–603.

R.L. Daft and R.H. Lengel, Organizational Information Requirements, Media Richness, and Structural Design, Management Science 32, No. 5 (May 1986) 554–571.

T.H. Davenport and J.E. Short, The New Industrial Engineering: Information Technology and Business Process Redesign, Sloan Management Review 31, No. 4 (Summer 1990) 11–27.

A. Deaton and J. Muellbauer, Economics and Consumer Behavior (Cambridge University Press, Cambridge, 1980).

L.W. Dowdy and D.V. Foster, Comparative Models of the File Assignment Problem, ACM Computing Surveys 14, No. 2 (June 1982) 287–313.

R.B. Duncan, Modifications in Decision Structure in Adapting to the Environment: Some Implications for Organizational Learning, Decision Sciences 5, No. 4 (Oct. 1974) 705–725.

J.R. Galbraith, Organization Design: An Information Processing View, Interfaces 4, No. 3 (May 1974) 28–36.

B. Gavish and H. Pirkul, Computer and Database Location in Distributed Computer Systems, IEEE Transactions on Computers C-35, No. 7 (July 1986) 583–590.

G.A. Gorry and M.S. Scott-Morton, Framework for Management Information Systems, Sloan Management Review 13, No. 1 (Fall, 1971) 55–70.

G.P. Huber, Organizational Information Systems: Determinants of Their Performance and Behavior, Management Science 28, No. 2 (Feb. 1982) 138–155.

G.P. Huber, The Nature of Design of Post-Industrial Organizations, Management Science 30, No. 8 (Aug. 1984) 928–951.

G.P. Huber and R.R. McDaniel, The Decision-Making Paradigm of Organizational Design, Management Science 32, No. 5 (May 1986) 572–589.

V.S. Jacob, J.C. Moore and A.B. Whinston, An Analysis of Human and Computer Decision-Making Capabilities, Information and Management 16, No. 5 (May 1989) 247–255.

G.W. Keen, “Interactive” Computer Systems for Managers: A Modest Proposal, Sloan Management Review 18, No. 1 (Fall 1976) 1–17.

J.L. King, Centralized versus Decentralized Computing: Organizational Considerations and Management Options, ACM Computing Surveys 15, No. 4 (Dec. 1983) 319–349.

J. Marschak and R. Radner, Economic Theory of Teams (Yale University Press, New Haven, 1972).

C.L. Meador, M.J. Guyote and W.L. Rosenfeld, Decision Support Planning and Analysis: The Problems of Getting Large-Scale DSS Started, MIS Quarterly 10, No. 2 (June 1986) 159–177.

J.C. Moore and A.B. Whinston, A Model of Decision-Making with Sequential Information-Acquisition - Part I, Decision Support Systems 2, No. 4 (Dec. 1986) 285-307.

J.C. Moore and A.B. Whinston, A Model of Decision-Making with Sequential Information-Acquisition – Part II, Decision Support Systems 3, No. 1 (March 1987) 47–72.

K.G. Murty, Linear and Combinatorial Programming (John Wiley and Sons, New York, 1976).

C.R. Necco, C.L. Gordon and N.W. Tsai, System Analysis and Design: Current Practices, MIS Quarterly 11, No. 4 (Dec. 1987) 461–476.

R. Radner, Hierarchy: The Economics of Managing, Journal of Economic Literature 30, No. 3 (Sept. 1992) 1382–1415.

R. Ram and S. Narasimhan, Database Allocation in a Distributed Environment: Incorporating a Concurrency Control Mechanism and Queuing Costs, Management Science 40, No. 8 (Aug. 1994) 969–983.

S.U. Randhawa and T.M. West, An Integrated Approach to Facility Location Problems, Computers and Industrial Engineering 29, No. 1-4 (Sept. 1995) 261-265.

H.R. Rao, V.S. Jacob and F. Lin, Hemispheric Specialization, Cognitive Differences, and Their Implications for the Design of Decision Support Systems, MIS Quarterly 16, No. 2 (June 1992) 145–151.

D. Robey, Computer Information Systems and Organization Structure, Communications of the ACM 24, No. 1 (Oct. 1981) 679–687.

H.A. Simon, A Formal Theory of the Employment Relationship, Econometrica 19, No. 3 (July 1951) 293–305.

H.A. Simon, The New Science of Management Decision (Harper and Row, New York, 1960).

H.A. Simon and A. Ando, Aggregation of Variables in Dynamic Systems, Econometrica 29, No. 2 (April 1961) 111–138.

A. Smith, The Wealth of Nations (Modern Library, New York, 1965).

J. Sobel, How to Count to One Thousand, Economic Journal 102, No. 410 (Jan. 1992) 1–8.

M.L. Tushman and D.A. Nadler, An Information Processing Approach to Organizational Design, Academy of Management Review 3, No. 3 (July 1978) 613–624.

L.A. West and J.F. Courtney, The Information Problems in Organizations: A Research Model for the Value of Information and Information Systems, Decision Sciences 24, No. 2 (March/April 1993) 229–251.

![](/api/attachments/MYXKB2RP/fulltext/images/15f085b805fc118c98d18627c10f276c893eae56c27b3fc4fd1fdcb751b89811.jpg)

John R. Conlon is an Associate Professor of Economics at the University of Mississippi. He received a B.A. and M.S. in Mathematics from the University of Chicago in 1978 and a Ph.D. in Economics from the University of Chicago in 1988. His research interests include production economics, mathematical economics, information economics, and game theory. He has articles in the Journal of Economic Theory, the Journal of Economic Dynamics and Control,

![](/api/attachments/MYXKB2RP/fulltext/images/779396655ecdc7038b135b118450834f5ca4c481e4edd4479d894ae034fe5d9f.jpg)  
Chi Hwang is an Assistant Professor of Management Information Systems at California State Polytechnic University, Pomona. He received a Ph.D. in Management Information Systems from the University of Mississippi in 1995, and has ten years of industrial experience as a system analyst and consultant. His research interests include intelligence based information systems, natural language processing, and group decision support systems. He has articles in the

the Journal of Productivity Analysis, Economics Letters, and the Journal of the American Society for Information Science.

![](/api/attachments/MYXKB2RP/fulltext/images/1dbf093b11b1039a95e1d724f046062f0583ae2f1cf088132712e09b2b66a64c.jpg)

Sumali J. Conlon is an Associate Professor of Management Information Systems at the University of Mississippi. She received a B.A. in statistics from Thammasat University, Thailand, in 1979 and a Ph.D. in Computer Science from the Illinois Institute of Technology in 1990. Her research interests include natural language processing, databases, information retrieval, decision support systems and software engineering. Her publications include several proceedings

papers as well as articles in Information Processing and Management, Decision Support Systems, Omega, the Journal of the American Society for Information Science, the International Journal of Lexicography, and Linguistica Computazionale.

Journal of Information Science, the International Journal of Information and Management Science, Information and Management, and Omega.
