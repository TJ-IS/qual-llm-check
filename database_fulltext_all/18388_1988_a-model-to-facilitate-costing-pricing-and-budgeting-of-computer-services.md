---
otero_id: 18388
otero_key: "GSK4DWWD"
title: "A model to facilitate costing, pricing and budgeting of computer services"
authors: "Niv Ahituv; Magid Igbaria"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90011-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model to Facilitate Costing, Pricing and Budgeting of Computer Services

Niv Ahituv \*

Computers and Information Systems Program, Faculty of Management, Tel Aviv University, Tel Aviv, 69978, Israel

Magid Igbaria \*

Department of Management & Organizational Sciences, College of Business and Administration, Drexel University, Philadelphia, PA 19104, USA

This paper addresses the problem of establishing a financial policy for managing computer systems, and proposes a model incorporating the three facets of determining the cost rates of hardware resources, evaluating the impact of pricing policy, and budget planning. This approach is based on statistical analysis of the correlation among the consumption of various hardware resources.

Keywords: Computer resource management, Charging for computer services, Budgeting computer resources, Pricing policy for computing services.

![](/api/attachments/GSK4DWWD/fulltext/images/c88ff4db50a0059d55ced03aafbaebd6442df61208b9a94025dde170407ca484.jpg)

Niv Ahituv is an Associate Professor and Chairperson of the Computers and Information Systems Program at the Faculty of Management, Tel Aviv University, Israel. Formerly, he lectured at the Claremont Graduate School, the University of Calgary and the University of British Columbia, and managed the DP department at the Bank of Israel. He holds degrees of B.Sc. in Mathematics, M.B.A., M.Sc. and Ph.D. in Information Systems. His articles have appeared in

Computers & Operations Research, The Computer Journal, Information & Management, MIS Quarterly, Interfaces, Decision Sciences, Communications of the ACM, The Journal of Systems Management, and others. He has co-authored a book, Principles of Information Systems for Management. His main areas of interest are economics of computers, information economics, and information systems management and development.

The authors made equal contributions to the preparation of this paper, and their names are listed in alphabetical order. This paper is based on the doctoral dissertation of the second author, which was supervised by the first author.

## 1. Introduction

In order to manage a computer center financially, the financial management of a computing center involves three major activities: costing of computer activities, pricing of computer services, and budgeting for the future acquisition of resources and operations. While this is true for both hardware and software, the discussion in this paper is confined to hardware resources only.

The goal of costing is to provide management with information on the cost of each unit of resources being used, such as the cost of one second of CPU (Central Processing Unit) time, and the cost of one printed line. This is the basis for both pricing and budgeting.

Pricing has three pruposes [12]: cost recovery, effective allocation of computer resources, and regulation of demand for interchangeable scarce resources, for example, by encouraging the scheduling of jobs at night instead of peak-load. Furthermore, prices are not necessarily linearly related to costs, since they may reflect policies of encouraging or deterring the use of certain resources.

![](/api/attachments/GSK4DWWD/fulltext/images/4940175fb771481fb72fa088a89412cdc489cb03cb397b629376abfd5a4aba3b.jpg)

Magid Igbaria is Assistant Professor of management information systems at Drexel University. Formerly, he lectured at Tel Aviv University, Hebrew University and Ben-Gurion University in Israel, and acted as the administrative director of the Center of Management Information Systems (CEMIS) at Tel Aviv University. He holds a B.A. in Statistics and Business Administration, and an M.A. in Information Systems and Operations Research from Hebrew University; he received his Ph.D. in Management Information Systems from Tel Aviv University. His research interests include economics of computers, management of information systems, and microcomputers in business. His articles have appeared in Communications of the ACM and Computers & Operations Research

Budgeting is based on predictions concerning future demand and consumption of computer resources. The forecast derives from past data combined with knowledge of pricing policy and future trends of the firm's activities.

These three basic components of financial management are enabled charge-out formulas combining the various resources into a charging mechanism (see [4,5,10]). The data for the charge-out mechanism is the measured information on user consumption of each resource, which is collected and stored in the accounting routines residing in most Operating Systems of computer mainframes, such as SMF (System management Facilities) in IBM mainframes.

Having collected and stored this information, the next question is how to analyze it. The purpose of this study is to know how to analyze resource consumption information in order to evaluate the charging system, specifically for costing, pricing and budget planning.

## 2. The General Model

Before entering into a detailed description, we first present an overview of the model and its rationale.

Suppose, hypothetically, that an individual program runs alone on a computer (i.e., there is no multiprogramming). Suppose also that the program is fully “deterministic”, that is, for any input transaction the program always performs the same sequence of instructions with no conditions; i.e., IF paths. Clearly, such a program is fully predictable: when the number of input transactions is known, one can precisely calculate the consumption (CPU time, the number of channel activities (EXCPs), and the number of printed lines). When future growth in the consumption of one resource can be predicted, one can derive the required capacity of other resources, and thus tell which of them may be a potential bottleneck.

In reality, however, there are two major factors hampering the “deterministic” approach. First, due to the existence and the nature of multiprogramming and the virtual storage (VS) environment, certain performance variables (e.g., CPU time, and EXCP) may be affected by the random mix of programs resident in memory at any moment. Second, in the sense that they contain IF statements, programs are not “deterministic” thus the execution of various code segments is conditional on inputs, etc.

Each run of a computer program (a job) can be attributed to a list (a vector) of actual performance variables: CPU time, number of accesses to disk and tape drives, number of input records, and number of output records. Due to these factors, various runs of the same program probably differ in their performance vectors.

Nevertheless, it is likely that some groups of programs maintain a common profile of resource consumption: e.g., all the programs that deal with inventory control or all the programming assignments of first-year students. This can be checked by sampling a large number of performance vectors and then running a linear regression on the vector elements (or on transformation of the elements into their functions; e.g., logarithmic). The results will indicate whether the consumption of a given resource is highly correlated with other one (e.g., whether CPU time is highly correlated with disk operations). If the results indicate high correlation among all the jobs running in a certain installation, we shall call this a homogeneous installation; otherwise, the installation is heterogeneous.

Even in a heterogeneous installation, it may be possible to identify a number of homogeneous groups; e.g., in the case of student assignments in an academic institution. Within each group, the correlation will be high; between the groups the correlation will be lower. Still, by constructing a set of simultaneous equations, one can identify the relationships among the consumption of various resources, and use these equations to model and analyze the computer resource consumption. On the basis of these assumptions, which have been empirically tested in a number of installations and found to be valid [9], one can build coefficient matrices that indicate the relationships among the consumption of various computer resources. The general model of these relationships is designed to provide the information system manager with a tool to support his/her decisions concerning costing of computer services, evaluating the impact of pricing policy, and planning the budget.

The model may be described as follows. There are groups of jobs consuming computer resources, and each job uses a certain amount of some or all of the hardware resources. In order to predict future utilization, the current consumption is measured for each computer resource; for example, CPU can be measured by CPU time in seconds. Ahituv & Igbaria [1] note that future utilization, which is denoted by $E(T)$ equals current utilization plus the additional expected utilization, based on computing the statistical relationships among the consumption of various resources.

Let J be the number of hardware resources (e.g., CPU, disks, printers, etc.). Denote the various resource variables by

$$
T = \left[ \begin{array}{c} t _ {1} \\ \cdot \\ \cdot \\ \cdot \\ t _ {J} \end{array} \right].
$$

Let $M$ be the number of homogeneous groups of jobs. Then for each group $\{m\}$ , $m = 1, \ldots, M$ , there is a statistical set of equations as follows:

$$
\boldsymbol {T} = \boldsymbol {A} _ {m} + \boldsymbol {B} _ {m} \boldsymbol {T}.
$$

Where $A_{m}$ and $B_{m}$ are, respectively, the intercept and the slope regression coefficient matrices.

Denote by U a vector of the current utilization of each resource.

Let $A$ be a matrix constructed by concatenating the $M$ sub-matrices $A_{m}, m = 1, \ldots, M$ .

Let $B$ be a matrix constructed by concatenating the $M$ sub-matrices $B_{m}, m = 1, \ldots, M$ .

Suppose it is known that the consumption of one computer resource will be increased in the future. Then the expected future utilization of all the resources is provided by the following equations:

$$
E (T) = U + [ B P + A I ] K,
$$

where

P = column vector of zeros, except that one element corresponds to the computer resource whose consumption is predicted to grow. This element has a value equal to the additional consumption.

$I =$ as $P$ , except that the specific element has a value of one.

$K =$ the number of new jobs expected to run on the system.

If the consumption data was transformed for linear regression purpose (e.g., a logarithmic transformation), then the above equation should be modified as follows:

$$
E (T) = U + [ B P + A I ] ^ {f} K,
$$

Fig. 1.  
A numerical example.

<table><tr><td>Hardware resources</td><td>Capacity C</td><td>Utilization U</td><td>Utilization Ratios</td></tr><tr><td>CPU (seconds)</td><td>75600</td><td>33991</td><td>0.45</td></tr><tr><td>Disks (I/O operations)</td><td>1587600</td><td>878662</td><td>0.55</td></tr><tr><td>Printers (lines)</td><td>1360800</td><td>1007642</td><td>0.74</td></tr></table>

$^{a}$ It is assumed that the time interval is 24 hours.  
$^{b}$ The resource utilization fractions are defined as the utilization/capacity for each hardware resource, that is, $U_{j}/C_{j}$ where j denotes resource j.

where $f$ is a transformation function (e.g., exponential).

For purposes of illustration, we introduce a simplified numerical example. Consider a computing center consisting of three main hardware resources: CPU, disks, and line printers. Figure 1 provides data for this example with two columns of capacity (C) and utilization (U) for each of the three hardware resources.

There is a wide variation in resource utilization, and the implications of this in a system balance is a need for a major reconfiguration of resource capacity.

Let us also assume that the data was collected from an insurance company with two groups of jobs: life and other insurance: M=2 and J=3 and the matrix B includes two sub-matrices $B_{1}$ and $B_{2}$ .

$$
B = \left[ \begin{array}{c c c c c c} 1 & 0. 5 9 & 0. 1 5 & 1 & 0. 5 8 & 0. 5 3 \\ 0. 3 3 & 1 & 0. 1 6 & 0. 8 1 & 1 & 0. 5 0 \\ 1. 0 2 & 0. 3 4 & 1 & 0. 4 8 & 0. 4 3 & 1 \end{array} \right],
$$

where $B_{1}$ is the first three columns and $B_{2}$ is the last three columns.

A is the matrix

$$
A = \left[ \begin{array}{c c c c c c} 0 & - 1. 2 & 1. 1 3 & 0 & - 1. 1 & - 0. 1 1 \\ 4. 7 5 & 0 & 4. 9 & 4. 3 7 & 0 & 3. 5 \\ 4. 4 6 & 4. 1 8 & 0 & 5. 3 & 4. 1 & 0 \end{array} \right].
$$

The matrices B and A are shown in terms of regression coefficients after a logarithmic transformation has been performed on the data; i.e., earlier in the analysis of the data, it was realized that a logarithmic transformation was appropriate.

Now suppose the managers are considering the addition of 50 new life insurance job, and that each job is expected to use 403 EXCPs. We are interested in knowing whether there is likely to be a bottleneck.

The vector $P$ will be equal to

$$
P = \left[ \begin{array}{c} 0 \\ \operatorname{Ln403} \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 6 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right].
$$

The zeros indicate that there is no change in the consumption of the other jobs.

The vector I will be

$$
I = \left[ \begin{array}{l} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right],
$$

and the number of new life insurance jobs is 50, hence K = 50.

The expected consumption will be

$$
E (T) = U + [ B P + A I ] ^ {f} K.
$$

This will yield

$$
E (T) = \left[ \begin{array}{c} 3 4 4 9 1 \\ 8 9 8 6 6 2 \\ 1 0 3 1 6 4 2 \end{array} \right],
$$

and the new resource utilization ratios will become

$$
\left[ \begin{array}{c} 0. 4 6 \\ 0. 5 7 \\ 0. 7 6 \end{array} \right].
$$

Thus adding new life insurance jobs will not create severe bottleneck. However, the increased printer usage may put additional stress on the system, and the manager of the computer center should remove the bottleneck by considering one or more of the following alternatives:

(1) do not add new jobs;

(2) reduce printer utilization by shifting some jobs to other systems;

(3) reduce the printing consumption of some jobs by increasing the price of this resource relative to substitute resources (e.g., visual display);

(4) increase printer capacity by upgrading the system.

This numerical example has demonstrated how the model can provide the information system manager with a tool to support hardware policy by:

(1) predicting the effects of introducing a new group of jobs to an existing workload, and

(2) predicting early warning of possible bottlenecks.

The analysis demonstrated here assumes a computer system with three hardware resources. In a real computer system environment there are usually more than three. The analysis of such a system would require that the framework here, especially the matrices, be modified to include all the hardware resources as well as all user groups.

The model was tested on real data in a number of installations and found to be valid. The next section illustrates how the model can be applied to managing hardware resources; the issues of costing, pricing and budgeting are addressed.

## 3. Costing of Computer Services

Prior to the era of multiprogramming, direct costing was not a big problem. Every program, while being run on a computer, occupied all the computing resources because an individual program runs alone on a computer. It was reasonable, therefore, to adopt the elapsed time of a run as a sole measurement of cost. This is not true any more because with multiprogramming, several programs can simultaneously share the same resources [2,4].

Suppose the allocation of computing cost is made according to the direct and indirect costing method [12.18]. The most common method for allocating the direct and indirect cost consists of the following steps [2,15]:

(1) identify measurable computing activities;

(2) allocate direct costs;

(3) allocate overhead (indirect) costs;

(4) predict the consumption for a given period of time (e.g., a year);

(5) determine standard rates for each unit of resource being used.

The discussion in this section relates to steps 4 and 5.

The cost per unit of consumption is defined by the predicted sum of the direct and overhead costs divided by the predicted consumption for each resource.

Define

$TC_{j} =$ predicted total cost for resource $j$ .

$DC_{j} =$ predicted direct cost for resource $j$ .

$I C_{j}$ = predicted overhead (indirect) cost for resource j.

$E(T)$ = a vector describing the expected future utilization of the hardware resources.

$V_{j}$ = vector of zeros, except element $j$ , which equals one.

$CR_{j}$ = expected cost per unit of consumption of resource j.

Then

$$
C R _ {j} = \frac {D C _ {j} + I C _ {j}}{V _ {j} E (T)} = \frac {T C _ {j}}{V _ {j} E (T)}.
$$

Clearly, this method requires careful estimation of both cost and consumption. The general model can assist in improving the prediction of consumption. This method, then, decreases the risk a computer center takes when it sets cost rates at the beginning of the budget year.

Continuing the previous example, suppose the expected total costs per day are 1777, 311, 577 for CPU, disks and line printers, respectively. The cost rate is the total cost divided by total predicted utilization, and therefore the standard cost rate for each resource will be

CPU second = \$0.05152,

Disk EXCP = \$0.00035,

A line printed = \$0.00056.

## 4. Pricing of Computer Services

Several studies have developed methods for pricing of computer services [5]. Among the common methods are the incremental cost method and flexible pricing.

The problem emphasized by most of these studies is that several computer components are used during the execution of a job, and the selected pricing method must take into account all the components.

Consequently, the charge-out formula is a multi-argument function. If we manage to decrease the number of arguments, the pricing mechanism will be simpler. Our purpose in this section, then, is to reduce the number of arguments by utilizing the proposed model.

An example of a multi-argument (component) pricing formula was given by Drury & Bates [6]:

$$
\text { Charge } = Q (C r _ {1} + D r _ {2} + L r _ {3} + \dots),
$$

where

$$
Q = \text { priority   factor }
$$

$$
\tilde {C} = \text { CPU   time   used }
$$

$D =$ number of Disk I/O operations

$$
L = \text { lines   printed }
$$

$$
r _ {t} = \text { cost   rate   for   resource } t, t = 1, 2, \dots
$$

Suppose there are only two variables, $X_{1}$ and $X_{2}$ (CPU and Disks, for example), and $X_{1}=f(X_{2})=\mathring{a}+b_{1}X_{2}+E$ . This formula represents a regression equation to estimate $X_{1}$ (e.g. CPU time), where E represents a random error factor. Suppose the charge is $(r_{1}X_{1}+r_{2}X_{2})$ , then, by substituting the regression equation into the charging formula we get:

$$
\text { Charge } = \sum r _ {j} \left(\mathring {a} _ {i j} + b _ {i j} X _ {i}\right),
$$

where $\mathring{a}_{ij}$ and $b_{ij}$ are the regression coefficients to predict $X_{j}$ given $X_{i}$ (taken from matrices A and B of the model). $r_{j}$ is the rate per consumption of one unit of resource j, and J is number of the components (resources) ( $\mathring{a}_{ij}=0$ and $b_{ij}=1$ when i=j). In matrix notation:

$$
\text { Charge } = R [ B P + A I ] ^ {f},
$$

where R is a vector of per unit consumption rate of each resource.

Continuing the previous example, suppose we want to charge for a life insurance run and we expect that the job will utilize 400 EXCPs. Then according to the correlation matrix in section 2,

$$
\left[ B P + A I \right] ^ {f} = \left[ \begin{array}{c} 1 0 \\ 4 0 0 \\ 4 8 0 \end{array} \right],
$$

$$
\begin{array}{r l} \text { Charge } & = [ 0. 0 5 1 5 0. 0 0 0 3 5 0. 0 0 0 5 6 ] \left[ \begin{array}{l} 1 0 \\ 4 0 0 \\ 4 8 0 \end{array} \right] \\ & = 0. 9 2 4. \end{array}
$$

This shows that there is no need to measure the consumption of more than one component provided that the consumption of the various components are statistically correlated. Hence, it is easier to compute the charges.

Suppose management wishes to encourage or discourage a certain group of jobs, while retaining the principle that the same charge will be levied for the same service within the group.

The solution proposed here is to establish a charging formula which is sensitive to the varying characteristics of particular job groups. The charge in this case will be a function of the job group, the consumption and cost rate for every resource. For example, if management were to place a low or high charge on job group m, then this group would pay proportionally less or more than other groups.

$$
\text { Charge } = Q _ {m} \Sigma r _ {j} \left(\mathring {a} _ {i j} + b _ {i j} \bar {X} _ {i}\right),
$$

where $Q_{m}$ is called the priority factor.

$Q_{m} \neq 1$ when the job belongs to group m, if $Q_{m} < 1$ , the management wishes to encourage group m, $Q_{m} > 1$ the management wishes not to encourage group m.

$Q_{m} = 1$ otherwise.

In matrix notation the charge will be

$$
\text { Charge } = Q _ {m} R [ B P + A I ] ^ {f}.
$$

Suppose $Q_{m}$ for life insurance jobs equals 0.90 (management wishes to encourage this group), then,

$$
\text { Charge } = 0. 9 0 \cdot 0. 9 2 4 = 0. 8 3 1 6.
$$

If management wishes to encourage or discourage certain groups of jobs and the use of a certain resource, too, then the charge formula will be

$$
\text { Charge } = \Sigma Q _ {m j} r _ {j} \left(\mathring {a} _ {i j} + b _ {i j} X _ {i}\right),
$$

where $Q_{m,j}$ denotes the priority factor of resource j and group m.

$Q_{mj} \neq j$ when the job belongs to group m and uses resource j,

$Q_{mj} = 1$ otherwise.

In matrix notation

$$
\text { Charge } = R ^ {\prime} Q [ B P + A I ] ^ {f},
$$

where Q is a priority matrix that equals an identity matrix if and only if the job does not belong to group m. Otherwise, it is a diagonal matrix containing (1) all over the main diagonal except for the element k, which has the value $Q_{m}$ .

Referring to the numerical example, suppose management wishes to encourage life insurance jobs to increase their use of the CPU, and $Q_{mj}=0.95$ (rate charged is lower than that of other jobs).

Then, the price for using CPU = 0.0515 · 0.95 = 0.049, and

$$
\text { Charge } = [ 0. 0 4 9 0. 0 0 0 3 5 0. 0 0 0 5 6 ] \left[ \begin{array}{l} 1 0 \\ 4 0 0 \\ 4 8 0 \end{array} \right] = 3 0. 9 0.
$$

This shows how management can use the model as a tool for balancing computer resource utilization and for encouraging or discouraging the use of a certain hardware resource or group.

## 5. Budget Planning

A budget is defined as a financial plan for a certain time period. It represents the authorization to utilize organizational resources to operate existing information systems, to develop new applications, and to add new capacities [4]. Usually it requires workload prediction.

Here we present a method for predicting the workload and forecasting the growth of computer usage, while taking into account the possibility of adding new resources (upgrading). Our purpose is to answer the following three questions:

(1) If any hardware resource is likely to become a bottleneck, what upgrading is needed for the system?

(2) If there are no bottlenecks, what is the expected consumption, and what are the expected costs? For example, estimating the number of lines to be printed will enable us to order an appropriate amount of papers. The cost will be incorporated into budget planning.

(3) Based on the capacity of computer resources, future utilization, and expected revenue, can we assess the maximum revenue to be derived from the system?

The calculations are based on the following expressions:

$$
\frac {\text { Capacity }}{\text { Utilization }} = \frac {\text { Maximum   revenue }}{\text { Expected   revenue }}.
$$

Hence, Maximum revenue = (Capacity/ Utilization) · Expected revenue.

The expected utilization is given by

$$
E (T) = U + \left[ B P + A I \right] ^ {f} K
$$

The expected costs are

$$
R ^ {\prime} \left[ U + [ B P + A I ] ^ {f} K \right],
$$

where R is a vector whose elements are the costs of each resource; it represents the expected costs of using one unit of each resource. Furthermore, if the resource is a bottleneck, then it takes into account the cost of upgrading.

The expected revenue is given by

$$
D ^ {\prime} \left[ U + [ B P = A I ] ^ {f} K \right],
$$

where D is a vector of prices.

The maximum revenue can be computed similarly substituting capacity for utilization.

Continuing the numerical example, suppose the system can meet the addition of 50 new life insurance jobs without bottlenecks, except for 24000 additional printed lines. Management must add to the coming budget \$13.44 (24000·0.00056) per day. Assuming that the management wishes to encourage the use of the CPU, then the total increase in expected daily revenue from CPU usage equals \$45 (0.90·50). The expected costs and revenues will be added to the future budget.

## 6. Summary and Discussion

On the basis of the concept of the correlation matrix, we have presented a new approach for determining the cost rates of hardware resources, the charging rates for computer services, and the budget for a computer center. To the best of our knowledge, this is the first attempt to apply a correlation matrix to decision making regarding the financial management of computer systems.

Since the problem was establishment of a financial policy for computer services, it was natural to base its resolution on current resource consumption. It was shown that the derived policy can encourage job groups to use ceratin resources, or discourage them from doing so, especially when the resources are likely to become bottlenecks. If the resources are in a peak-load situation, it is possible to consider decreasing utilization of a given resource by increasing its price, by upgrading its capacity, or by tuning it. These alternatives must be taken into account in the budget planning of a computer system. Further, the model indicates where management can apply changes, and provides a way of measuring the impact of the policy or operational change. The method is simple to adopt and to explain.

## References

[1] N. Ahituv and M. Igbaria, A Model for Predicting and Evaluating Computer Resource Consumption, Communications of the ACM, 1988 (in press).

[2] N. Ahituv and S. Neumann, Principles of Information Systems for Management, W.C. Brown, Dubuque, Iowa, 2nd edition, 1986.

[3] L. Billera, D. Heath and J. Rannan, Internal Telephone Billing Rates, Operations Research, Vol. 26, No. 6, 1978, pp. 956–965.

[4] I. Borovits, Management of Computer Operations, Prentice-Hall Inc., Englewood Cliffs, New Jersey, 1984.

[5] I. Borovits and S. Neumann, Internal Pricing of Computer Services, Computer Journal, Vol. 21, No. 3, 1978, pp. 199–204.

[6] D.H. Drury and J.E. Bates, Data Processing Chargeback Systems: Theory and Practice, The Society of Management Accountants of Canada, Hamilton, Ontario, 1979.

[7] P. Ein-Dor and K. Jones, Information Systems Management, Elsevier Sciences Pub., New York, NY., 1985.

[8] J.T. Hootman, The Pricing Dilemma, Datamation, Vol. 15, No. 8, 1969, pp. 61–66.

[9] M. Igbaria, A Model for Analyzing and Evaluating Computer Resource Consumption, Ph.D. Dissertation, Tel Aviv University, 1986 (in Hebrew).

[10] J.P.C. Kleijnen, Computers and Profits, Addison-Wesely Pub., Reading, Mass., 1980.

[11] M. Lin, System for Charging Computer Services, Journal of Systems Management, Vol. 34, No. 11, 1983, pp. 6–10.

[12] L. McKell, J. Hansen and L. Heitger, Charging for Computer Resources, ACM Computing Surveys, Vol. 11, No. 2, 1979, pp. 105–120.

[13] H. Merrill, Merrill's Expanded Guide to Computer Performance Using SAS Systems, SAS Institute Inc., Cary, NC, 1984.

[14] N.R. Neilson, The Allocation of Computer Resources – Is Pricing the Answer?, Communications of the ACM, Vol. 13, No. 8, 1970, pp. 467–474.

[15] W.E. Sharpe, The Economics of Computers, Columbia University Press, New York, NY, 1969.

[16] S. Smidt, Flexible Pricing of Computer Services, Management Science, Vol. 14, No. 10, 1968, pp. B581-B600.

[17] S. Sobczak, Pricing Computer Usage, Datamation, Vol. 20, No. 2, 1974, pp. 61–64.

[18] G. Wiorkowski, and J. Wiorkowski, A Cost Allocation Model, Datamation, Vol. 19., No. 8, 1973, pp. 60–65.
