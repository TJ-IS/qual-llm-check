---
otero_id: 21169
otero_key: "8CAHYK8J"
title: "A decision support methodology for stochastic multi-criteria linear programming using spreadsheets"
authors: "David C. Novak; Cliff T. Ragsdale"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00130-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support methodology for stochastic multi-criteria linear programming using spreadsheets

David C. Novak <sup>a,1</sup>, Cliff T. Ragsdale <sup>b,</sup>\*

<sup>a</sup>Department of Operations and Information Management, University of Connecticut, 1200 Hillside Road, Unit 1041 OPIM, Storrs, CT 06269-1041, USA

<sup>b</sup>Department of Business Information Technology, Virginia Tech, 1007 Pamplin Hall, Blacksburg, VA 24061, USA

Accepted 14 May 2002

## Abstract

In recent years, tools for solving optimization problems have become widely available through the integration of optimization software (or solvers) with all major spreadsheet packages. These solvers are highly effective on traditional linear programming (LP) problems with known, deterministic parameters. However, thoughtful analysts may rightly question the quality and robustness of optimal solutions to problems where point estimates are substituted for model parameters that are stochastic in nature. Additionally, while many LP problems implicitly involve multiple objectives, current spreadsheet solvers provide no convenient facility for dealing with more than one objective. This paper introduces a decision support methodology for identifying robust solutions to LP problems involving stochastic parameters and multiple criteria using spreadsheets. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Stochastic programming; Multi-criteria optimization; Decision support; Spreadsheets

## 1. Introduction

Linear programming (LP) is a mathematical programming technique designed to optimize a (single) linear objective function subject to a linear constraint set where all model parameters are assumed to be known with certainty. Over the past several decades, numerous applications for LP have been proposed for improving the efficiency of business operations [26]. Unfortunately, uncertainty in such things as costs, demand, interest rates, production yields, and equipment reliability is the practical reality faced by business decision makers (DMs) on a daily basis. As a result, some degree of randomness or uncertainty is likely to impact the parameter estimates used in medium- to long-term LP planning models and may also affect short-term models [6]. When one or more parameters in an LP problem are represented by a random variable, a stochastic LP problem results [26].

Effectively modeling the uncertainties in a stochastic LP model is a challenging yet necessary step in evaluating the robustness of a potential ‘‘optimal’’ solution to simultaneous changes in estimated parameter values. This is complicated by the fact that today’s information-rich business environment imposes numerous competitive, political, financial, environmental, and societal pressures on DMs [4]. The inherent non-commensurate and conflicting nature of these pressures often makes it difficult or impossible to formulate a single objective function for many real-world decision problems. In these situations, multi-criteria optimization techniques must be used to allow DMs to properly model and analyze the trade-offs inherent with multiple conflicting objectives [29].

As managerial DMs become increasingly aware of the availability and purpose of the solver optimization software built into today’s spreadsheets, questions about how to use this software with decision problems involving stochastic parameters and multiple criteria will likely emerge. A significant amount of research has been directed at developing techniques for solving stochastic programming problems. A similar level of effort has been devoted to challenging problems in multi-criteria optimization. Unfortunately, most of the resulting solution techniques are not easily understood by, available to, or implemented by practitioners in the business world. Additionally, relatively little work has focused on devising general solution procedures for optimization problems that are both stochastic and multi-criteria in nature.

The objective of this paper is to develop an easily understood methodology for solving stochastic, multicriteria LP problems in spreadsheets. We begin with a review of the research literature followed by a description of our proposed methodology. We then illustrate this methodology using a stochastic, multi-criteria production planning problem implemented in Microsoft Excel. Finally, we highlight the benefits of our methodology and offer some closing comments.

## 2. Literature review

While the respective research literatures addressing stochastic programming and multi-criteria optimization are quite extensive, relatively little work has been done on developing solution methodologies for problems that are both stochastic and multi-criteria in nature. We briefly review the literature in each of these areas below and provide several references to point interested readers to appropriate sources of additional information.

## 2.1. Stochastic programming

In general, three approaches to stochastic programming have received considerable attention. The first approach yields problems with probabilistic or chance constraints that restrict the probability of infeasibility to be no greater than a prespecified threshold value [23]. Chance-constraint problems incorporate the uncertainty associated with specific events or conditions into the model by using probability constraints. Unfortunately, this approach can lead to problems with nonconvex constraint sets that can be extremely difficult to solve [26].

The second approach focuses on modeling future response or recourse. Recourse problems involve obtaining information about a process or system after the observation of some random event [14]. A response is modeled for each outcome (or group of outcomes) that is observed. Multi-stage recourse problems involve altering second-stage or reactive decisions based on the outcomes associated with first-stage decisions that are proactive in nature (before random outcomes are observed). A major difficulty in solving recourse problems is that the required calculation of the expected value of the recourse function involves multidimensional integration. Furthermore, for stochastic programming problems involving discrete random variables, this function is nondifferentiable [14,26].

Another well-known approach to solving stochastic programming problems involves scenario-based analysis [8]. The origin of these scenarios can be very diverse; they may be from a known discrete distribution, be obtained from limited sample information or some type of approximation scheme, or come from some type of preliminary analysis involving the probability of their occurrence based on the opinion of an expert [21]. While scenario-based approaches provide a relatively straightforward way to implicitly account for uncertainty, they may rely on an exceptionally large number of scenarios. Scenario-based approaches generally rely on either the a priori forecasting of all possible outcomes or the discretization of a continuous multivariate probability distribution resulting in an exponential number of scenarios. For example, the discretization of n uncertain variables with m discretion points results in $m ^ { n }$ scenarios [25]. Thus, a problem with 20 uncertain variables and 3 discretion points results in $3 ^ { 2 0 } = 3 , 4 8 6 , 7 8 4 , 4 0 1$ scenarios. Clearly, this approach can be intractable for problems of realistic size.

## 2.2. Multi-criteria optimization from the perspective of stochastic programming

The techniques for solving deterministic multicriteria optimization problems can be broken into three general classes requiring, respectively, the prior, progressive, or posterior articulation of preferences by the DM [24].

With prior articulation methods, the DM makes trade-offs among the objectives before optimization. The DM’s trade-off preferences are modeled either in the constraints, the objective, or both. While this approach works well in theory [9,13,15], in practice it can be very difficult to elicit and model a DM’s true utility function accurately. As a result, there are few applications of this approach being used in practice [24].

Progressive articulation methods are interactive in nature, requiring the DM to provide trade-off information as the search for the best solution progresses. Examples of interactive procedures include STEM [3], the Geoffrion –Dyer –Feinberg procedure [11], the visual interactive approach [17,18], the interactive weighted Tchebycheff approach [29,30,32,33], the reference point approach [37], and the Zionts–Wallenius method [40,41]. These techniques help avoid the problem of having to assess the DM’s utility function. There is variation in the complexity associated with the different techniques. In general, as a problem becomes larger and more complex, the problem takes longer to solve. Some techniques may become extremely computationally intensive and may not provide results in a timely manner for large-scale problems. Computational burdens only increase when adding stochastic elements to a multi-criteria optimization problem. As a result, on large-scale problems, DMs may lose interest during the solution process and may feel that these techniques are not efficient or effective.

Posterior articulation methods first generate a representative set of nondominated solutions and then solicit trade-off information from the decision maker to identify the preferred solution. A number of methods involving posterior articulation of preferences have been proposed for deterministic problems [1,20,31,36]. This approach seems most attractive for stochastic multi-criteria optimization as it avoids the problem of assessing the DM’s utility function and also shields the DM from the computational burden associated with locating nondominated solutions.

## 2.3. Stochastic multi-criteria optimization

As mentioned earlier, relatively few studies have undertaken the challenge of solving stochastic multicriteria optimization problems. Studies that have probed into this area generally propose methodology tailored to a specific application or restrict their investigation to allowing stochastic elements in only some specific part of the model. Most of these studies also rely on combinations of stochastic programming and multi-criteria optimization techniques that may exhibit some of the weaknesses or inefficiencies mentioned above.

Youssef et al. [39] apply three heuristics to the same optimization problem and perform a comparative study between genetic algorithms (GA), simulated annealing (SA), and tabu search (TS). Ben Abdelaziz et al. [2] investigate several concepts of efficiency in the context of multiple objective stochastic linear programming (MOSLP) problems. They examine the MOSLP problem under four different contexts of partial information where varying assumptions are made concerning the preference structure of the decision maker. Dubois et al. [7] provide an overview of the similarities between decision under uncertainty and multi-criteria decision-making problems. They stress a unified view of the two traditionally separate and independent paradigms and discuss examples where different solution techniques and concepts might be applied to both types of problems.

Goicoechea et al. [12] describe a method called PROTRADE that requires a complicated assessment of the DM’s multi-attribute utility function and uses chance constraints to allow a DM to trade between expected levels of the objective function and their respective probabilities of achieving desired levels. Changchit and Terrell [5] introduced the chance-constrained goal programming technique for modeling release decisions for a reservoir system with stochastic inflows. Sutardi et al.[34] combined stochastic dynamic programming and fuzzy integer goal programming to devise a solution methodology to address a multi-criteria sequential decision-making problem in water resource investment planning under budgetary and socio-technical uncertainty.

The STRANGE technique [35] is a progressive articulation scenario-based technique that assumes discrete sets of model parameters are given, each with its own subjective probability of occurrence. Klein et al. [16] proposed a progressive articulation technique that requires the DM to respond in a meaningful way to multistate, multi-attribute lotteries. Ringuest and Graves [24] propose a sampling-based, posterior articulation methodology for generating nondominated solutions for multiple objective optimization problems; however, this technique only accommodates stochastic elements in the objective function coefficients.

From this review of the literature, it appears that there is ample room for additional thought and research into a general framework or methodology for solving stochastic multi-criteria LP problems. It is our contention that the methodology most likely to be used by DMs for this class of computationally intensive problem will rely on the posterior articulation of preferences and avoid the complexities introduced by chance constraints, recourse modeling, and subjective discretization of stochastic optimization problems. A general methodology that embodies these principles is introduced below.

## 3. Proposed methodology

Fig. 1 provides a visual summary of our proposed methodology for solving stochastic, multi-criteria LP problems. As indicated in Fig. 1, the first step in our methodology is to formulate a valid model for the problem at hand. As will be illustrated later, the model formulation step must be carried out with the ensuing solution methodology in mind. Once the model is formulated, it is then used to generate and solve a series of problem scenarios. Each problem scenario is created by randomly generating values for the uncertain parameters in the model based on given probability distributions. Note that this methodology allows stochastic parameters to appear in any part of the model. The underlying distribution of the individual parameters need not be the same; however, the methodology requires the user to specify a distribution empirically or theoretically.

![](/api/attachments/8CAHYK8J/fulltext/images/f9ff6417390486d285618e139ad736e1000ec26c05f587c247c3a01b902c4abe.jpg)  
Fig. 1. Overview of proposed solution methodology.

As each problem scenario is generated, our methodology solves a weighted Tchebycheff program [29] to identify a non-dominated (or efficient) solution for the current problem. A solution with criterion vector $z ^ { * }$ is said to dominate a solution with criterion vector z $\mathrm { i f } \ z ^ { \ast }$ is as good as z in all its components and better than z is at least one component. Accordingly, a solution with criterion vector $z ^ { * }$ is non-dominated if no other solution dominates it.

Weighted Tchebycheff programs require the identification of optimal or ‘‘utopian’’ values for each of the n individual objectives in a problem (typically obtained by optimizing each of the n objectives individually). Then, for a given set of criterion weights, the weighted Tchebycheff program is solved to obtain a nondominated solution. Note that the criterion weights are randomly generated in our methodology. Fig. 2 illustrates how a nondominated solution might be located for a hypothetical problem with two criteria. We refer to this non-dominated solution as a candidate solution for the problem.

Note that the utopian point, criterion space, and candidate solution will likely differ for each scenario as various parameters in the model are randomly changed. The process of generating scenarios and solving weighted Tchebycheff programs continues until a sample of m candidate solutions exists, each representing a non-dominated solution to a problem scenario.

The next step in our methodology is referred to as re-evaluation. The re-evaluation process provides an indication of how robust a particular candidate solution is to uncertainty. For example, if 100 scenarios are being used, the candidate solutions for each of the 100 scenarios are each re-evaluated in the other 99 randomly generated scenarios. As each candidate solution is substituted into every problem scenario, various descriptive statistics are calculated to create a ‘‘picture’’ of the distribution of outcomes that may be expected if a given candidate solution is chosen for implementation.

For problems that involve multiple criteria, the next step in our methodology is to determine the Pareto ranking for each candidate solution. In this paper, we consider the criterion vector $z _ { i }$ for solution i to be the mean value produced on each criterion during the re-evaluation process, that is, $z _ { i } { = } ( \bar { z } _ { 1 } ,$ $\bar { z } _ { 1 } , . . . , \bar { z } _ { n } )$ . To determine a solution’s Pareto ranking, the entire pool of candidate solutions is analyzed to identify the non-dominated solutions. These nondominated solutions receive a Pareto ranking of one (1) and are then removed from the pool. The remaining solutions are then analyzed and a new set of nondominated solutions is identified, assigned a Pareto ranking of two (2), and then removed from the pool. This process continues until all candidate solutions have been assigned a Pareto ranking [28].

![](/api/attachments/8CAHYK8J/fulltext/images/d5be9226e8dd7d1944bb360afdcf78ad7426288dcfa25a74dee0f1211cd3e3cf.jpg)  
Fig. 2. Illustration of weighted Tchebycheff program solution in criterion space.

The next step in our methodology is to present the statistical and Pareto ranking information about the solutions to the DM. Ideally, this would be done in a way that allows the DM to sort, chart, and filter the candidate solutions in an exploratory manner to identify the solution that provides the greatest utility. Note that this methodology is heuristic in nature and implicitly integrates the preferences of the DM on a posterior articulation basis to identify the candidate solution for implementation.

In situations where stochastic parameters are continuous, there is an infinite number of potential solutions to consider. This is one reason why conventional scenario-based analysis may not be the best approach for addressing LP problems with continuous stochastic parameters. The primary difference between the proposed methodology and conventional scenario-based analysis is that the proposed methodology uses re-evaluation as a means of determining how robust a particular candidate solution is without considering an exceedingly large number of possible scenarios. In cases where the true value of a large number of parameters may be unknown, or where potential values of unknown parameters are continuous in nature, the goal of optimization is to generate a ‘‘good’’ solution. A ‘‘good’’ solution is obviously a subjective measure. Hence, our methodology leaves the final solution selection to the DM.

Although an adequate sample size is required to generate a ‘‘good’’ candidate solution, there is no need to examine all possible parameter combinations using this methodology. The proposed methodology is designed to work well even when a relatively small number of scenarios is considered because it focuses on identifying a number of robust solutions rather than trying to identify a single optimal solution. The number of scenarios required to ensure an adequate random sample size is itself a matter of uncertainty and is an open area of research. Obviously, there is a trade-off between generating many scenarios and the computational resources required to solve the problem. However, well-known replication determination conventions for simulation modeling provide an acceptable approach to generating an adequate number of scenarios for evaluation. Replication strategies are described in detail in Ref. [19].

## 4. Excel as a stochastic programming tool

Historically, mathematical programming problems were typically solved using special purpose optimization software packages such as GAMS, LINDO, AMPL, and MATLAB. While these packages are extremely effective at solving mathematical programming problems, the spreadsheet optimizer known as ‘‘solver’’ bundled with Microsoft Excel is currently the most readily available general-purpose optimization modeling system. The Excel solver is available to approximately 35 million users of office productivity software worldwide [10].

The widespread availability of the solver in Excel has spawned many optimization applications in both the private and public sectors [10]. In education, the number of instructors who have adopted Excel as the tool of choice for introducing students to optimization continues to increase. As Excel becomes a more commonly used tool in the mathematical programming field, issues relating to how one can model and solve LP problems with stochastic parameters and multiple objectives are likely to emerge as a key limitation to solving mathematical programming problems using Excel.

Fortunately, Excel provides an ideal software platform for solving various types of stochastic, multipleobjective LP problems using the methodology outlined in Fig. 1. Because Excel is a spreadsheet and data analysis tool, it has many useful built-in statistical and graphical capabilities. These features greatly facilitate the interpretation of scenario-based optimization results without having to export output data to other packages and without having to learn new specialized, software packages. Excel also provides a visual development language—Visual Basic for Applications (VBA)—in the same package as the spreadsheet. VBA provides a high degree of flexibility and control in creating decision support systems (DSS), giving developers easy access to the Excel’s extensive collection of data analysis objects and tools for creating graphical user interfaces. VBA also provides the ability to easily integrate external databases and communications and reporting tools via automation with Microsoft’s ActiveX technologies [38].

## 5. Example

We now illustrate how an LP problem with stochastic parameters and multiple objectives may be solved in Excel using our proposed methodology. The example model described in this paper is based on a network flow problem presented in Ref. [22]. The problem describes a recycling operation that processes four raw materials (newspaper, white office paper, mixed paper, and cardboard) through two alternate recycling processes to create three different products (newsprint pulp, packaging paper pulp, and print stock pulp). The network model for this problem is shown in Fig. 3 with corresponding profit maximizing LP model given in Fig. 4. (An additional objective for this problem is discussed shortly.)

The LP model given in Fig. 4 represents a deterministic, multistage production problem. Uncertainty is introduced to the model by assuming that the true values of the coefficients in the objective function (1) (representing revenues, production costs, and material costs), the coefficients in constraints 6 through 10 (the process yields), and the right-hand sides in constraints

8, 9, and 10 (the product demands) are not known with certainty. Given the typical variability in the quality and consistency of recycled raw materials, it is reasonable to assume that some degree of uncertainty exists in process costs and yields. Similarly, if the values representing demand for the various pulps are based on market forecasts (rather than contractual obligations), some degree of uncertainty likely exists in both the demand and unit revenues for finished products.

In practice, many LPs with uncertain parameters are (conveniently) transformed into deterministic problems by using the expected or most likely value for each uncertain parameter and treating it as a fixed value. The problem is then solved as a traditional, deterministic LP. We demonstrate this approach and compare the optimal result obtained from the deterministic problem to the solution(s) identified using our proposed stochastic solution methodology. The appeal of stochastic programming is that it attempts to identify a solution to an optimization problem while directly addressing uncertainty rather than assuming it away. The deterministic solution is presented to serve as a benchmark to allow the reader to assess how well the stochastic solution methodology performs relative to the optimal solution for the deterministic problem.

![](/api/attachments/8CAHYK8J/fulltext/images/a317e41d7e9db48efef6aed5411c5292afee7425c885042baaa8abe19274765c.jpg)  
Fig. 3. Network representation of multistage recycling model.

$$
\begin{array}{r l} \text {Max:} & 4 8 (0. 9 5 \mathrm{X} _ {5 7} + 0. 9 \mathrm{X} _ {6 7}) + 5 4 (0. 9 \mathrm{X} _ {5 8} + 0. 9 5 \mathrm{X} _ {6 8}) + 6 1 (0. 9 \mathrm{X} _ {5 9} + 0. 9 5 \mathrm{X} _ {6 9}) \\ & - 5 \mathrm{X} _ {5 7} - 6 \mathrm{X} _ {5 8} - 8 \mathrm{X} _ {5 9} - 6 \mathrm{X} _ {6 7} - 8 \mathrm{X} _ {6 8} - 7 \mathrm{X} _ {6 9} - 2 0. 5 \mathrm{X} _ {1 5} - 1 9. 5 \mathrm{X} _ {1 6} - 2 3. 5 \mathrm{X} _ {2 5} - 2 5. 5 \mathrm{X} _ {2 6} \\ & - 2 9 \mathrm{X} _ {3 5} - 3 0 \mathrm{X} _ {3 6} - 2 8 \mathrm{X} _ {4 5} - 2 9 \mathrm{X} _ {4 6} \end{array}\tag{1}
$$

Subject to:

$$
\mathrm{X} _ {1 5} + \mathrm{X} _ {1 6} \leq 7 0\tag{2}
$$

$$
\mathrm{X} _ {2 5} + \mathrm{X} _ {2 6} \leq 5 0\tag{3}
$$

$$
\mathrm{X} _ {3 5} + \mathrm{X} _ {3 6} \leq 3 0\tag{4}
$$

$$
\mathrm{X} _ {4 5} + \mathrm{X} _ {4 6} \leq 4 0\tag{5}
$$

$$
0. 9 \mathrm{X} _ {1 5} + 0. 8 \mathrm{X} _ {2 5} + 0. 9 5 \mathrm{X} _ {3 5} + 0. 9 5 \mathrm{X} _ {4 5} - \mathrm{X} _ {5 7} - \mathrm{X} _ {5 8} - \mathrm{X} _ {5 9} = 0\tag{6}
$$

$$
0. 8 5 \mathrm{X} _ {1 6} + 0. 8 5 \mathrm{X} _ {2 6} + 0. 9 \mathrm{X} _ {3 6} + 0. 8 5 \mathrm{X} _ {4 6} - \mathrm{X} _ {6 7} - \mathrm{X} _ {6 8} - \mathrm{X} _ {6 9} = 0\tag{7}
$$

$$
0. 9 5 \mathrm{X} _ {5 7} + 0. 9 \mathrm{X} _ {6 7} \leq 6 0\tag{8}
$$

$$
0. 9 \mathrm{X} _ {5 8} + 0. 9 5 \mathrm{X} _ {6 8} \leq 4 0\tag{9}
$$

$$
0. 9 \mathrm{X} _ {5 9} + 0. 9 5 \mathrm{X} _ {6 9} \leq 5 0\tag{10}
$$

$$
\mathrm{X} _ {i j} > 0 \text {   for   all   } i \text {   and   } j\tag{11}
$$

Fig. 4. Mathematical formulation of deterministic multistage recycling model.

## 5.1. The deterministic solution

A spreadsheet representation of the deterministic model and its optimal solution is shown in Fig. 5. The optimal solution values for the various decision variables are presented in column B.

The optimal solution directs 58.08 units of newspaper to recycling process 1 (node 5), 11.92 units of newspaper to recycling process 2 (node 6), 50.0 units of mixed paper to recycling process 2 (node 6), and so on. The total profit associated with this solution is US\$2,792.02. Again, this represents the profit maximizing solution to a deterministic problem where all parameter values are assumed to be known with certainty.

As mentioned above, there is likely to be some degree of uncertainty in the production yields, processing costs, demands and revenues in this model. This, in turn, raises a number of questions about the deterministic solution in Fig. 5. For instance, if the values for multiple parameters change, by how much might the total profit change and, on average, how much profit could we expect this solution to produce? Or, if the values of multiple parameters change, on average, how close would the solution shown in Fig. 5 come to meeting the demand for each of the final products?

![](/api/attachments/8CAHYK8J/fulltext/images/312a8110e12601e2d15007d29425abf36054c8ecb4cee1bbb04647082dfa52bf.jpg)  
Fig. 5. Spreadsheet implementation and solution to the recycling problem.

Unfortunately, the answers to these very practical questions are not provided in the solution shown in Fig. 5. Our proposed methodology answers these (and other questions) and also allows the user to explore a variety of other solutions that, in the presence of uncertainty, may actually be better than the deterministic solution.

## 5.2. Re-formulating the model to accommodate uncertainty

To accommodate and analyze the effects of uncertainty in this application, we must first formulate the problem in a slightly different manner so as not to violate the conservation of flow constraints through the two recycling processes. To understand this, consider again the solution shown in Fig. 5. For this solution, the current flow into recycling process 2 (node 6) is 52.63 units (i.e., cell F7 plus cell F9). To balance the flow at node 6, cell B19 indicates that this same 52.63 units of material flows out of recycling process 2 (node 6) to be made into printing stock pulp (node 9). Now suppose that the value in cell E9, representing the production yield for mixed paper (node 2) that is sent to recycling process 2 (node 6), changes from 85% to 83% (changing cell F9 to $0 . 8 3 \times 5 0 = 4 1 . 5 )$ . In this case, the solution shown in Fig. 5 would have less than 52.63 units of material flowing into recycling process 2 (node 6). However, the solution would still have 52.63 units (cell B19) flowing out of recycling process 2 (node 6) to be made into printing stock pulp (node 9). Clearly, such a solution is impossible.

An alternate formulation of the problem that avoids the above difficulty is shown in Fig. 6. Here we use the variable $X _ { i j k }$ to indicate the amount of raw material represented by node i that is sent through recycling process represented by node $j$ and is destined for use in the finished good represented by node k. For instance, $X _ { 2 6 9 }$ represents the amount of mixed paper (node 2) that will undergo recycling process 2 (node

6) and be used to produce printing stock pulp (node 9). While the formulation in Fig. 6 appears a bit more daunting than the earlier one, it produces an equivalent optimal solution as shown in Fig. 7. Additionally, it allows the solution to be analyzed under any set of changes in parameter values.

For instance, again suppose the production yield for mixed paper (node 2) that is sent to recycling process 2 (node 6) changes from 85% to 83%. In this case, the solution shown in Fig. 7 would have $0 . 8 3 \times 0 . 9 5 \times 5 0 = 3 9 . 4 2 5$ units of mixed paper (node 2) flowing into recycling process 2 (node 6) and onward to help meet the demand for print stock pulp paper (node 9). Note that an additional 9.625 units of material flow to node 9 along the path from node 1 through node 6. Thus, the reduced yield on the flow from node 2 to node 6 results in a total of 49.05 units of material being available at node 9. Although this does not meet the deterministic demand for 50 units at node 9, we are now able to accurately describe how well the deterministic solution performs as parameters in the model change.

We emphasize that the reformulation of this problem was necessary so that re-evaluation of a candidate solution under alternate scenarios can be done in a meaningful way. Many problems would not require any sort of special reformulation of the original model. However, careful consideration needs to be given to this issue when applying this methodology.

## 5.3. Introducing an additional objective

In the preceding discussion, we illustrated that changes in model parameters may cause a given solution to meet more or less of the demand for a given product. In light of heightened awareness and concern over environmental issues, it is entirely possible that the manger of our hypothetical recycling facility would be interested in meeting as much of the demand for recycled materials as possible—even if this meant making less profit.

To model this, we define level of service (LOS) to be the percentage of met customer demand for a given product. So, an additional objective for this problem might be to maximize the minimum LOS for all our products. That is, we will assume that (ignoring profits) the DM would prefer a solution that provides a 95% (LOS) on all three products to a solution that

$$
\begin{array}{r l} \text {Max:} & 4 8 [. 9 5 (. 9 X _ {1 5 7} +. 8 X _ {2 5 7} +. 9 5 X _ {3 5 7} +. 9 5 X _ {4 5 7}) +. 9 (. 8 5 X _ {1 6 7} +. 8 5 X _ {2 6 7} +. 9 X _ {3 6 7} +. 8 5 X _ {4 6 7}) ] \\ & + 5 4 [. 9 (. 9 X _ {1 5 8} +. 8 X _ {2 5 8} +. 9 5 X _ {3 5 8} +. 9 5 X _ {4 5 8}) +. 9 5 (. 8 5 X _ {1 6 8} +. 8 5 X _ {2 6 8} +. 9 X _ {3 6 8} +. 8 5 X _ {4 6 8}) ] \\ & + 6 1 [. 9 (. 9 X _ {1 5 9} +. 8 X _ {2 5 9} +. 9 5 X _ {3 5 9} +. 9 5 X _ {4 5 9}) +. 9 5 (. 8 5 X _ {1 6 9} +. 8 5 X _ {2 6 9} +. 9 X _ {3 6 9} +. 8 5 X _ {4 6 9}) ] \\ & - 2 0. 5 (X _ {1 5 7} + X _ {1 5 8} + X _ {1 5 9}) - 1 9. 5 (X _ {1 6 7} + X _ {1 6 8} + X _ {1 6 9}) \\ & - 2 3. 5 (X _ {2 5 7} + X _ {2 5 8} + X _ {2 5 9}) - 2 5. 5 (X _ {2 6 7} + X _ {2 6 8} + X _ {2 6 9}) \\ & - 2 9 (X _ {3 5 7} + X _ {3 5 8} + X _ {3 5 9}) - 3 0 (X _ {3 6 7} + X _ {3 6 8} + X _ {3 6 9}) \\ & - 2 8 (X _ {4 5 7} + X _ {4 5 8} + X _ {4 5 9}) - 2 9 (X _ {4 6 7} + X _ {4 6 8} + X _ {4 6 9}) \\ & - 5 (. 9 X _ {1 5 7} +. 8 X _ {2 5 7} +. 9 5 X _ {3 5 7} +. 9 5 X _ {4 5 7}) \\ & - 6 (. 8 5 X _ {1 6 7} +. 8 5 X _ {2 6 7} +. 9 X _ {3 6 7} +. 8 5 X _ {4 6 7}) \\ & - 6 (. 9 X _ {1 5 8} +. 8 X _ {2 5 8} +. 9 S X _ {3 S B} +. S S X _ {4 S B}) \\ & - \mathrm{8}. (\mathrm{8S} _ {\mathrm{168}} +. \mathrm{8S} _ {\mathrm{268}} +. \mathrm{9S} _ {\mathrm{368}} +. \mathrm{8S} _ {\mathrm{468}}) \\ & - \mathrm{8}. (\mathrm{9S} _ {\mathrm{159}} +. \mathrm{8S} _ {\mathrm{259}} +. \mathrm{9S} _ {\mathrm{359}} +. \mathrm{9S} _ {\mathrm{459}}) \\ & - \mathrm{7}. (\mathrm{8S} _ {\mathrm{169}} +. \mathrm{8S} _ {\mathrm{269}} +. \mathrm{9S} _ {\mathrm{369}} +. \mathrm{8S} _ {\mathrm{469}}) \end{array}
$$

Subject to:

$$
\mathrm{X} _ {1 5 7} + \mathrm{X} _ {1 6 7} + \mathrm{X} _ {1 5 8} + \mathrm{X} _ {1 6 8} + \mathrm{X} _ {1 5 9} + \mathrm{X} _ {1 6 9} <   7 0
$$

$$
\mathrm{X} _ {2 5 7} + \mathrm{X} _ {2 6 7} + \mathrm{X} _ {2 5 8} + \mathrm{X} _ {2 6 8} + \mathrm{X} _ {2 5 9} + \mathrm{X} _ {2 6 9} <   5 0
$$

$$
\mathrm{X} _ {3 5 7} + \mathrm{X} _ {3 6 7} + \mathrm{X} _ {3 5 8} + \mathrm{X} _ {3 6 8} + \mathrm{X} _ {3 5 9} + \mathrm{X} _ {3 6 9} \leq 3 0
$$

$$
\mathrm{X} _ {4 5 7} + \mathrm{X} _ {4 6 7} + \mathrm{X} _ {4 5 8} + \mathrm{X} _ {4 6 8} + \mathrm{X} _ {4 5 9} + \mathrm{X} _ {4 6 9} \leq 4 0
$$

$$
. 9 5 \left(. 9 \mathrm{X} _ {1 5 7} +. 8 \mathrm{X} _ {2 5 7} +. 9 5 \mathrm{X} _ {3 5 7} +. 9 5 \mathrm{X} _ {4 5 7}\right) +. 9 \left(. 8 5 \mathrm{X} _ {1 6 7} +. 8 5 \mathrm{X} _ {2 6 7} +. 9 \mathrm{X} _ {3 6 7} +. 8 5 \mathrm{X} _ {4 6 7}\right) \leq 6 0
$$

$$
. 9 \left(. 9 \mathrm{X} _ {1 5 8} +. 8 \mathrm{X} _ {2 5 8} +. 9 5 \mathrm{X} _ {3 5 8} +. 9 5 \mathrm{X} _ {4 5 8}\right) +. 9 5 \left(. 8 5 \mathrm{X} _ {1 6 8} +. 8 5 \mathrm{X} _ {2 6 8} +. 9 \mathrm{X} _ {3 6 8} +. 8 5 \mathrm{X} _ {4 6 8}\right) \leq 4 0
$$

$$
. 9 \left(. 9 \mathrm{X} _ {1 5 9} +. 8 \mathrm{X} _ {2 5 9} +. 9 5 \mathrm{X} _ {3 5 9} +. 9 5 \mathrm{X} _ {4 5 9}\right) +. 9 5 \left(. 8 5 \mathrm{X} _ {1 6 9} +. 8 5 \mathrm{X} _ {2 6 9} +. 9 \mathrm{X} _ {3 6 9} +. 8 5 \mathrm{X} _ {4 6 9}\right) \leq 5 0
$$

$$
i, j
$$

Fig. 6. Alternate formulation of multistage recycling problem.

meets 100% of the demand for two products but only 75% of the demand for the third product. For our recycling problem, such an objective could be implemented by adding the following objective and constraints to the problem:

Max: LOS

Subject to:

$$
\begin{array}{r l} & \mathrm{LOS} \leq [ 0. 9 5 (0. 9 X _ {1 5 7} + 0. 8 X _ {2 5 7} + 0. 9 5 X _ {3 5 7} \\ & \quad + 0. 9 5 X _ {4 5 7}) + 0. 9 (0. 8 5 X _ {1 6 7} + 0. 8 5 X _ {2 6 7} + 0. 9 X _ {3 6 7} \\ & \quad + 0. 8 5 X _ {4 6 7}) ] / 6 0 \end{array}
$$

$$
\begin{array}{r l} \mathrm{LOS} & \leq [ 0. 9 (0. 9 X _ {1 5 8} + 0. 8 X _ {2 5 8} + 0. 9 5 X _ {3 5 8} + 0. 9 5 X _ {4 5 8}) \\ & + 0. 9 5 (0. 8 5 X _ {1 6 8} + 0. 8 5 X _ {2 6 8} + 0. 9 X _ {3 6 8} \\ & + 0. 8 5 X _ {4 6 8}) ] / 4 0 \end{array}
$$

$$
\begin{array}{r l} \mathrm{LOS} & \leq [ 0. 9 (0. 9 X _ {1 5 9} + 0. 8 X _ {2 5 9} + 0. 9 5 X _ {3 5 9} + 0. 9 5 X _ {4 5 9}) \\ & + 0. 9 5 (0. 8 5 X _ {1 6 9} + 0. 8 5 X _ {2 6 9} + 0. 9 X _ {3 6 9} \\ & + 0. 8 5 X _ {4 6 9}) ] / 5 0 \end{array}
$$

LOSV1:

Note that the first three constraints above impose lower bounds on the LOS for each of the three products produced by the recycling process. Clearly, if LOS = 1, then 100% of all demand is met. So by making LOS as large as possible, the minimum LOS for all three products is made as close to 100% as possible.

To optimize both objectives using the weighted Tchebycheff technique, we must first identify utopian values for both the profit and LOS objectives in this problem. Ordinarily, this would require us to solve a separate optimization problem for each of our objectives. However, Figs. 5 and 6 indicate that the utopian profit level for this problem is US\$2792.02. Also note that this solution meets all the demand. Thus, the deterministic solution appears to simultaneously allow for both the maximization of profit and a 100% LOS for all products.

<table><tr><td colspan="18">M2</td><td></td></tr><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td>Input</td><td>From</td><td>To</td><td>To</td><td>Output</td><td>Unit Proc. Cost</td><td></td><td></td><td></td><td>Proc. Cost</td><td></td><td></td><td></td><td>Supply(-) &amp; Demand(+)</td><td>Unit Cost(-) &amp; Revenue(+)</td><td></td><td></td></tr><tr><td>5</td><td></td><td>8.70</td><td>1</td><td>5</td><td>7</td><td>7.437</td><td>$17.50</td><td>1-5</td><td>0.9</td><td>$13.00</td><td></td><td>1</td><td>-70.00</td><td>-70.00</td><td>-$7.50</td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td>0.00</td><td>1</td><td>6</td><td>7</td><td>0.000</td><td>$17.10</td><td>1-6</td><td>0.85</td><td>$12.00</td><td></td><td>2</td><td>-50.00</td><td>-50.00</td><td>-$12.50</td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td>49.38</td><td>1</td><td>5</td><td>8</td><td>40.000</td><td>$18.40</td><td>2-5</td><td>0.8</td><td>$11.00</td><td></td><td>3</td><td>-18.24</td><td>-30.00</td><td>-$20.00</td><td></td><td></td><td></td></tr><tr><td>8</td><td></td><td>0.00</td><td>1</td><td>6</td><td>8</td><td>0.000</td><td>$18.80</td><td>2-6</td><td>0.85</td><td>$13.00</td><td></td><td>4</td><td>-40.00</td><td>-40.00</td><td>-$15.00</td><td></td><td></td><td></td></tr><tr><td>9</td><td></td><td>0.00</td><td>1</td><td>5</td><td>9</td><td>0.000</td><td>$20.20</td><td>3-5</td><td>0.95</td><td>$9.00</td><td></td><td>5</td><td>0.00</td><td>0.00</td><td>$0.00</td><td></td><td></td><td></td></tr><tr><td>10</td><td></td><td>11.92</td><td>1</td><td>6</td><td>9</td><td>9.625</td><td>$17.95</td><td>3-6</td><td>0.9</td><td>$10.00</td><td></td><td>6</td><td>0.00</td><td>0.00</td><td>$0.00</td><td></td><td></td><td></td></tr><tr><td>11</td><td></td><td>0.00</td><td>2</td><td>5</td><td>7</td><td>0.000</td><td>$15.00</td><td>4-5</td><td>0.95</td><td>$13.00</td><td></td><td>7</td><td>60.00</td><td>60</td><td>$48.00</td><td></td><td></td><td></td></tr><tr><td>12</td><td></td><td>0.00</td><td>2</td><td>6</td><td>7</td><td>0.000</td><td>$18.10</td><td>4-6</td><td>0.85</td><td>$14.00</td><td></td><td>8</td><td>40.00</td><td>40</td><td>$54.00</td><td></td><td></td><td></td></tr><tr><td>13</td><td></td><td>0.00</td><td>2</td><td>5</td><td>8</td><td>0.000</td><td>$15.80</td><td>5-7</td><td>0.95</td><td>$5.00</td><td></td><td>9</td><td>50.00</td><td>50</td><td>$61.00</td><td></td><td></td><td></td></tr><tr><td>14</td><td></td><td>0.00</td><td>2</td><td>6</td><td>8</td><td>0.000</td><td>$19.80</td><td>5-8</td><td>0.9</td><td>$6.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td></td><td>0.00</td><td>2</td><td>5</td><td>9</td><td>0.000</td><td>$17.40</td><td>5-9</td><td>0.9</td><td>$8.00</td><td></td><td colspan="4">Income Summary</td><td></td><td></td><td></td></tr><tr><td>16</td><td></td><td>50.00</td><td>2</td><td>6</td><td>9</td><td>40.375</td><td>$18.95</td><td>6-7</td><td>0.9</td><td>$6.00</td><td></td><td colspan="3">Total Revenue</td><td>$8,090.00</td><td></td><td></td><td></td></tr><tr><td>17</td><td></td><td>18.24</td><td>3</td><td>5</td><td>7</td><td>16.463</td><td>$13.75</td><td>6-8</td><td>0.95</td><td>$8.00</td><td></td><td colspan="3">Total Material Cost</td><td>$2,114.84</td><td></td><td></td><td></td></tr><tr><td>18</td><td></td><td>0.00</td><td>3</td><td>6</td><td>7</td><td>0.000</td><td>$15.40</td><td>6-9</td><td>0.95</td><td>$7.00</td><td></td><td colspan="3">Total Processing Cost</td><td>$3,183.14</td><td></td><td></td><td></td></tr><tr><td>19</td><td></td><td>0.00</td><td>3</td><td>5</td><td>8</td><td>0.000</td><td>$14.70</td><td></td><td></td><td></td><td></td><td colspan="3">Net Profit</td><td>$2,792.02</td><td></td><td></td><td></td></tr><tr><td>20</td><td></td><td>0.00</td><td>3</td><td>6</td><td>8</td><td>0.000</td><td>$17.20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21</td><td></td><td>0.00</td><td>3</td><td>5</td><td>9</td><td>0.000</td><td>$16.60</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22</td><td></td><td>0.00</td><td>3</td><td>6</td><td>9</td><td>0.000</td><td>$16.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23</td><td></td><td>40.00</td><td>4</td><td>5</td><td>7</td><td>36.100</td><td>$17.75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>24</td><td></td><td>0.00</td><td>4</td><td>6</td><td>7</td><td>0.000</td><td>$19.10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25</td><td></td><td>0.00</td><td>4</td><td>5</td><td>8</td><td>0.000</td><td>$18.70</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>26</td><td></td><td>0.00</td><td>4</td><td>6</td><td>8</td><td>0.000</td><td>$20.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27</td><td></td><td>0.00</td><td>4</td><td>5</td><td>9</td><td>0.000</td><td>$20.60</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td></td><td>0.00</td><td>4</td><td>6</td><td>9</td><td>0.000</td><td>$19.95</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>29</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 7. Spreadsheet implementation of revised formulation.

Fig. 8 shows the necessary changes to our spreadsheet model to simultaneously optimize both objectives using a weighted Tchebycheff formulation. Specifically, in cells P22 through P25, we have added formulas that compute the net profit and actual LOS associated with each product. In cells Q22 through Q25, we have listed the target or utopian values for each of the objectives. In general, each of the target values is determined by optimizing the model for each of the individual objectives. Although this model has two objectives, the LOS objective requires that we keep track of three separate LOS values that all share a common target value. Next, in cells R22 through R25, we list the weights associated with each objective. Again note that each of the LOS values shares a common weight corresponding to the weight for the LOS objective. Finally, the weighted percentage deviation of each objective from its target value is calculated in cells S22 through S25. Note that our methodology randomly generates the weights for each objective. We then solve for the solution that minimizes the maximum of the weighted percentage deviations to obtain a non-dominated solution to the problem.

## 5.4. Modeling uncertainty

With minor modifications, the same model shown in Fig. 8 was used to implement our methodology. First, the parameter values for Yield, Unit Processing Costs, Demand, and Revenues were generated randomly from triangular distributions. Triangular distributions were used because, pragmatically, it would likely be easiest for managers of this type of operation to specify minimum, most likely, and maximum values for the various uncertain values. Any other probability distributions could easily used if desired. A separate worksheet was created as shown in Fig. 9 to facilitate this process. A simple VBA macro was written to copy randomly generated variates from this worksheet into appropriate cells in our optimization model as needed.

<table><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td rowspan="2" colspan="6">Recycling Problem</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td>Unit Proc.</td><td></td><td></td><td></td><td>Proc.</td><td></td><td></td><td></td><td>Supply(-) &amp; Demand(+)</td><td rowspan="2">Unit Cost(-) &amp; Revenue(+)</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>4</td><td></td><td>Input</td><td>From</td><td>To</td><td>To</td><td>Output</td><td>Cost</td><td></td><td>Arc</td><td>Yield</td><td>Cost</td><td></td><td>Node</td><td>Flow</td></tr><tr><td>5</td><td></td><td>8.69</td><td>1</td><td>5</td><td>7</td><td>7.433</td><td>$17.50</td><td></td><td>1-5</td><td>0.9</td><td>$13.00</td><td></td><td>1</td><td>-70.00</td><td>-70.00</td><td>-$7.50</td><td></td><td></td></tr><tr><td>6</td><td></td><td>0.00</td><td>1</td><td>6</td><td>7</td><td>0.000</td><td>$17.10</td><td></td><td>1-6</td><td>0.85</td><td>$12.00</td><td></td><td>2</td><td>-50.00</td><td>-50.00</td><td>-$12.50</td><td></td><td></td></tr><tr><td>7</td><td></td><td>49.38</td><td>1</td><td>5</td><td>8</td><td>40.000</td><td>$18.40</td><td></td><td>2-5</td><td>0.8</td><td>$11.00</td><td></td><td>3</td><td>-18.25</td><td>-30.00</td><td>-$20.00</td><td></td><td></td></tr><tr><td>8</td><td></td><td>0.00</td><td>1</td><td>6</td><td>8</td><td>0.000</td><td>$18.80</td><td></td><td>2-6</td><td>0.85</td><td>$13.00</td><td></td><td>4</td><td>-40.00</td><td>-40.00</td><td>-$15.00</td><td></td><td></td></tr><tr><td>9</td><td></td><td>0.00</td><td>1</td><td>5</td><td>9</td><td>0.000</td><td>$20.20</td><td></td><td>3-5</td><td>0.95</td><td>$9.00</td><td></td><td>5</td><td>0.00</td><td>0.00</td><td>$0.00</td><td></td><td></td></tr><tr><td>10</td><td></td><td>11.92</td><td>1</td><td>6</td><td>9</td><td>9.629</td><td>$17.95</td><td></td><td>3-6</td><td>0.9</td><td>$10.00</td><td></td><td>6</td><td>0.00</td><td>0.00</td><td>$0.00</td><td></td><td></td></tr><tr><td>11</td><td></td><td>0.00</td><td>2</td><td>5</td><td>7</td><td>0.000</td><td>$15.00</td><td></td><td>4-5</td><td>0.95</td><td>$13.00</td><td></td><td>7</td><td>60.00</td><td>60</td><td>$48.00</td><td></td><td></td></tr><tr><td>12</td><td></td><td>0.00</td><td>2</td><td>6</td><td>7</td><td>0.000</td><td>$18.10</td><td></td><td>4-6</td><td>0.85</td><td>$14.00</td><td></td><td>8</td><td>-40.00</td><td>40</td><td>$54.00</td><td></td><td></td></tr><tr><td>13</td><td></td><td>0.00</td><td>2</td><td>5</td><td>8</td><td>0.000</td><td>$15.80</td><td></td><td>5-7</td><td>0.95</td><td>$5.00</td><td></td><td>9</td><td>50.00</td><td>50</td><td>$61.00</td><td></td><td></td></tr><tr><td>14</td><td></td><td>0.00</td><td>2</td><td>6</td><td>8</td><td>0.000</td><td>$19.80</td><td></td><td>5-8</td><td>0.9</td><td>$6.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td></td><td>0.00</td><td>2</td><td>5</td><td>9</td><td>0.000</td><td>$17.40</td><td></td><td>5-9</td><td>0.9</td><td>$8.00</td><td></td><td colspan="3">Income Summary</td><td></td><td></td><td></td></tr><tr><td>16</td><td></td><td>50.00</td><td>2</td><td>6</td><td>9</td><td>40.371</td><td>$18.95</td><td></td><td>6-7</td><td>0.9</td><td>$6.00</td><td></td><td colspan="2">Total Revenue</td><td>$8,090.00</td><td></td><td></td><td></td></tr><tr><td>17</td><td></td><td>18.25</td><td>3</td><td>5</td><td>7</td><td>16.467</td><td>$13.75</td><td></td><td>6-8</td><td>0.95</td><td>$8.00</td><td></td><td colspan="2">Total Material Cost</td><td>$2,114.87</td><td></td><td></td><td></td></tr><tr><td>18</td><td></td><td>0.00</td><td>3</td><td>6</td><td>7</td><td>0.000</td><td>$15.40</td><td></td><td>6-9</td><td>0.95</td><td>$7.00</td><td></td><td colspan="2">Total Processing Cost</td><td>$3,183.11</td><td></td><td></td><td></td></tr><tr><td>19</td><td></td><td>0.00</td><td>3</td><td>5</td><td>8</td><td>0.000</td><td>$14.70</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Net Profit</td><td>$2,792.02</td><td></td><td></td><td></td></tr><tr><td>20</td><td></td><td>0.00</td><td>3</td><td>6</td><td>8</td><td>0.000</td><td>$17.20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Weighted %</td><td></td></tr><tr><td>21</td><td></td><td>0.00</td><td>3</td><td>5</td><td>9</td><td>0.000</td><td>$16.60</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Objectives</td><td>Actual</td><td>Target</td><td>Weight</td><td>Deviation</td></tr><tr><td>22</td><td></td><td>0.00</td><td>3</td><td>6</td><td>9</td><td>0.000</td><td>$16.30</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Net Profit</td><td>$2,792.02</td><td>$2,792.02</td><td>0.75</td><td>0.00%</td></tr><tr><td>23</td><td></td><td>40.00</td><td>4</td><td>5</td><td>7</td><td>36.100</td><td>$17.75</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Newsprint Pulp LOS</td><td>1.000</td><td>1.000</td><td>0.25</td><td>0.00%</td></tr><tr><td>24</td><td></td><td>0.00</td><td>4</td><td>6</td><td>7</td><td>0.000</td><td>$19.10</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Packing Paper Pulp LOS</td><td>1.000</td><td>1.000</td><td>0.25</td><td>0.00%</td></tr><tr><td>25</td><td></td><td>0.00</td><td>4</td><td>5</td><td>8</td><td>0.000</td><td>$18.70</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Printing Stock Plup LOS</td><td>1.000</td><td>1.000</td><td>0.25</td><td>0.00%</td></tr><tr><td>26</td><td></td><td>0.00</td><td>4</td><td>6</td><td>8</td><td>0.000</td><td>$20.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Maximum</td><td>0.00%</td></tr><tr><td>27</td><td></td><td>0.00</td><td>4</td><td>5</td><td>9</td><td>0.000</td><td>$20.60</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td></td><td>0.00</td><td>4</td><td>6</td><td>9</td><td>0.000</td><td>$19.95</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">Number of Scenarios</td><td>100</td></tr><tr><td>29</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">Run</td></tr><tr><td>31</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 8. Spreadsheet implementation of formulation with multiple objectives.

![](/api/attachments/8CAHYK8J/fulltext/images/e57d998c15244942ffb8d10c5fa5f0deb1e4f8b01662655aedfc2141ff36f9fc.jpg)  
Fig. 9. Random number generators for the recycling problem.

An example of a single stochastic scenario, referred to as scenario 1, is presented in Fig. 10. Note that the optimal solution obtained by solving this MOLP problem is different from that of the original deterministic problem. Also note that for the solution shown, the minimum LOS of 94.2% is achieved with a level of profit somewhat lower than the target profit value for this scenario. This illustrates the trade-off between profit and LOS that the DM faces in this problem.

A VBA macro was written to automate the process of generating random scenarios, optimizing them with solver, storing the resulting scenarios and candidate solutions on a separate worksheet. It is a relatively simple process to automatically store the scenarios and candidate solutions in an external database file if desired or warranted by problem size.

## 5.5. Re-evaluation

Once m scenarios have been generated and optimized, each candidate solution is re-evaluated in each of the other m  1 scenarios. (In our example, we used m = 100.) Re-evaluation is intended to provide insight into how robust each candidate solution is as the uncertain parameters in the model change. An example of solution re-evaluation is presented in Fig. 11. Suppose the randomly generated parameter values shown in this figure represent scenario 2. This example demonstrates how the candidate solution for scenario 1 shown in Fig. 10 would be re-evaluated in scenario 2.

Notice that the solution values shown in Fig. 11 correspond to the candidate solution obtained by solving scenario 1 in Fig. 10. Thus, if the candidate solution identified from scenario 1 is implemented and the yields, processing costs, and demands represented by scenario 2 occur, the recycler would actually earn a profit of US\$2,366.89, which is more than the utopian value under scenario 1. However, only 86.8% of the demand for newspaper pulp would be satisfied—which is lower than the minimum LOS of 94.1% identified in the solution to scenario 1.

As illustrated here, the yield, processing cost, demand, and revenue parameters vary as each candi-

![](/api/attachments/8CAHYK8J/fulltext/images/259670029fe0f42b575a949083465114fd1aa4d95a5c908807fefc7788e131f9.jpg)  
Fig. 10. Example of a random problem scenario.

![](/api/attachments/8CAHYK8J/fulltext/images/3938b536e1b2ecdcaa1bde3c0fbeaa1a36672279a3ef4153065eac6956caf6b8.jpg)  
Fig. 11. Re-evaluation of a candidate solution.

date solution is re-evaluated under each scenario. As a result, the total profit and minimum LOS associated with the candidate solution being re-evaluated will change as the parameters change from scenario to scenario. Because the supply of raw recyclable materials is assumed to be known and constant across all scenarios, each candidate solution adheres to the same upper bound limits relating to input quantities. However, the candidate solutions differ in how these available inputs are allocated and how much output is generated under each scenario.

Note that the demand constraints in this example are treated as ‘‘soft’’ constraints that need not be satisfied exactly. No explicit penalty is assessed on candidate solutions that fail to meet the expected demand in particular scenarios. Also note that during the re-evaluation process, it is possible for a given candidate solution to produce more of a given product than is demanded. As a result, during re-evaluation, our total revenue function is modified to account for the fact that we cannot sell more of a product than is demanded.

Once all re-evaluations are completed, summary statistics for key measures such as average net profit, average net flow (output for the three products), and average level of service (LOS) are computed. The DM may then judge the quality of a candidate solution by examining the average profit and average level of service (LOS) data. Candidate solutions providing profit or LOS too far from desired levels can be eliminated from further consideration.

## 5.6. Data summary and analysis

The various summary statistics shown in Fig. 12 provide important information for evaluating the robustness of a candidate solution under uncertainty. In the context of this paper, the average total profit, average LOS, and Pareto rank are assumed to be the important metrics. Obviously, metrics of interest are problem specific and will differ from one application to the next.

VBA code was written to place the minimum, maximum, and standard deviation of each performance measure in the comment property associated with cell (as shown for cell B19). Strictly defined, LOS cannot exceed 100%, as 100% is the maximum level of service possible. However, for the purpose of this paper, a LOS greater than 100% simply implies that output is exceeding demand (there is a surplus of output).

<table><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td></tr><tr><td>Candidate Solution</td><td>Net Profit</td><td>Newsprint LOS</td><td>Packing Paper LOS</td><td>Print Stock LOS</td><td>Minimum LOS</td><td>Pareto Rank</td><td></td><td></td><td></td></tr><tr><td>2</td><td>47</td><td>$1,817</td><td>91.7%</td><td>96.2%</td><td>93.5%</td><td>91.7%</td><td>1</td><td></td><td></td></tr><tr><td>3</td><td>49</td><td>$1,793</td><td>97.7%</td><td>81.7%</td><td>97.6%</td><td>81.7%</td><td>2</td><td></td><td></td></tr><tr><td>4</td><td>30</td><td>$1,776</td><td>90.5%</td><td>102.9%</td><td>90.0%</td><td>90.0%</td><td>2</td><td></td><td></td></tr><tr><td>5</td><td>67</td><td>$1,764</td><td>90.8%</td><td>99.7%</td><td>86.4%</td><td>86.4%</td><td>3</td><td></td><td></td></tr><tr><td>6</td><td>90</td><td>$1,757</td><td>91.8%</td><td>100.1%</td><td>85.9%</td><td>85.9%</td><td>4</td><td></td><td></td></tr><tr><td>7</td><td>85</td><td>$1,755</td><td>101.7%</td><td>80.5%</td><td>93.8%</td><td>80.5%</td><td>5</td><td></td><td></td></tr><tr><td>8</td><td>93</td><td>$1,747</td><td>85.3%</td><td>94.9%</td><td>99.9%</td><td>85.3%</td><td>5</td><td></td><td></td></tr><tr><td>9</td><td>8</td><td>$1,745</td><td>94.4%</td><td>90.2%</td><td>81.2%</td><td>81.2%</td><td>6</td><td></td><td></td></tr><tr><td>10</td><td>60</td><td>$1,741</td><td>95.4%</td><td>82.9%</td><td>99.9%</td><td>82.9%</td><td>6</td><td></td><td></td></tr><tr><td>11</td><td>18</td><td>$1,739</td><td>81.6%</td><td>82.2%</td><td>78.1%</td><td>78.1%</td><td>7</td><td></td><td></td></tr><tr><td>12</td><td>33</td><td>$1,733</td><td>96.9%</td><td>96.7%</td><td>90.3%</td><td>90.3%</td><td>2</td><td></td><td></td></tr><tr><td>13</td><td>70</td><td>$1,731</td><td>96.7%</td><td>91.7%</td><td>79.3%</td><td>79.3%</td><td>7</td><td></td><td></td></tr><tr><td>14</td><td>91</td><td>$1,719</td><td>94.8%</td><td>87.8%</td><td>91.5%</td><td>87.8%</td><td>3</td><td></td><td></td></tr><tr><td>15</td><td>71</td><td>$1,711</td><td>100.0%</td><td>91.2%</td><td>92.1%</td><td>91.2%</td><td>2</td><td></td><td></td></tr><tr><td>16</td><td>29</td><td>$1,696</td><td>89.6%</td><td>101.7%</td><td>91.3%</td><td>89.6%</td><td>3</td><td></td><td></td></tr><tr><td>17</td><td>17</td><td>$1,692</td><td>92.7%</td><td>98.9%</td><td>96.2%</td><td>92.7%</td><td>1</td><td></td><td></td></tr><tr><td>18</td><td>4</td><td>$1,681</td><td>105.4%</td><td>96.4%</td><td>87.6%</td><td>87.6%</td><td>4</td><td></td><td></td></tr><tr><td>19</td><td>87</td><td>$1,677</td><td>81.4%</td><td>94.5%</td><td>81.4%</td><td>81.4%</td><td>7</td><td></td><td></td></tr><tr><td>20</td><td>24</td><td>$1,665</td><td>79.9%</td><td>97.0%</td><td>79.9%</td><td>79.9%</td><td>8</td><td></td><td></td></tr><tr><td>21</td><td>48</td><td>$1,657</td><td>94.1%</td><td>93.4%</td><td>97.7%</td><td>93.4%</td><td>1</td><td></td><td></td></tr><tr><td>22</td><td>58</td><td>$1,653</td><td>93.5%</td><td>85.3%</td><td>99.0%</td><td>85.3%</td><td>5</td><td></td><td></td></tr><tr><td>23</td><td>86</td><td>$1,648</td><td>97.1%</td><td>105.5%</td><td>84.7%</td><td>84.7%</td><td>6</td><td></td><td></td></tr><tr><td>24</td><td>35</td><td>$1,640</td><td>95.3%</td><td>91.7%</td><td>94.2%</td><td>91.7%</td><td>2</td><td></td><td></td></tr><tr><td>25</td><td>84</td><td>$1,637</td><td>78.2%</td><td>88.6%</td><td>88.5%</td><td>78.2%</td><td>9</td><td></td><td></td></tr><tr><td>26</td><td>31</td><td>$1,634</td><td>100.7%</td><td>99.7%</td><td>85.7%</td><td>85.7%</td><td>5</td><td></td><td></td></tr><tr><td>27</td><td>3</td><td>$1,629</td><td>102.1%</td><td>78.9%</td><td>99.9%</td><td>78.9%</td><td>9</td><td></td><td></td></tr><tr><td>28</td><td>59</td><td>$1,628</td><td>93.8%</td><td>109.0%</td><td>86.7%</td><td>86.7%</td><td>5</td><td></td><td></td></tr><tr><td>29</td><td>72</td><td>$1,618</td><td>94.6%</td><td>88.4%</td><td>93.7%</td><td>88.4%</td><td>4</td><td></td><td></td></tr></table>

Fig. 12. Summary of re-evaluation results for all candidate solutions.

Excel also provides user-friendly tools that allow one to easily summarize data and conduct advanced statistical analyses. All of these statistical tools can also be accessed through VBA to create various tables and/or graphs for a DSS. Most of these data analysis features are not available in other specialized optimization software packages, making Excel the tool of choice for implementing this type of methodology.

## 5.7. Data filtering and graphing

The summary statistical data generated for each candidate solution during the re-valuation process can easily overwhelm the DM. Clearly, the DM needs a way to sort through or filter these data to identify the most promising set of solutions. Fortunately, we can use Excel’s built-in data filter to sort and select data according to any search criteria involving any combination of profit, LOS, and/or Pareto ranking. For example, Fig. 13 shows the results of applying a filter to the Pareto rank metric to only consider scenarios in the first three Pareto levels. (The deterministic solution is also shown for comparison purposes even though it has a Pareto rank of 7.) Note that only 16 out of 100 scenarios fall in the first three Pareto ranks. Thus, Excel’s built-in data filtering capability quickly allowed us to identify the solutions that are on or near the efficient frontier of our decision space.

It is especially significant to note that the original deterministic solution to the problem is in the seventh Pareto layer and is dominated by 32 other candidate solutions. Also, recall that the deterministic solution provided a profit of US\$2792.02 and 100% LOS in the ‘‘most likely’’ scenario presented in Figs. 4 and 6. However, when this solution is evaluated in the 100 randomly generated scenarios, it produces an average profit of only US\$1569 and an average minimum LOS of 87.9%. Clearly, the proposed methodology provides the DM with much better solutions to choose from.

![](/api/attachments/8CAHYK8J/fulltext/images/d5e0c6422bb7e62cdb929bc641ad821337cba24aeaa8a52e8cafdd5bfb92c776.jpg)  
Fig. 13. Example of filtering based on Pareto rank.

## 6. Conclusions

This paper introduces a methodology for solving stochastic multi-criteria LP problems and provides an example of how Microsoft Excel can be used to implement this methodology. The flexibility provided by VBA allows developers and practitioners to write code directly in Excel modules and worksheets using the Visual Basic editor included with Excel. VBA statements can be written to perform both complex and simple mathematical functions and formatting within an Excel workbook. There are a number of benefits associated with using Excel to solve stochastic, multi-criteria LP problems:

 Excel is the most widely distributed spreadsheet package in the world [10],

 Excel provides a user-friendly environment for setting up and solving various optimization problems, and

 Excel provides a robust set of built-in data analysis tools and features that can be used to sort, summarize, and display important information used for decision making.

A motivating factor for this paper is to provide users with a methodology that is easy to understand, flexible, and allows them to take advantage of numerous built-in features associated with a readily available software package. Through the use of dynamic scenario generation using a random number generator, a collection of possible candidate solutions can be considered for any stochastic LP problem. The candidate solution generated for each scenario is reevaluated against all of the other randomly generated scenarios in the model. The user can compare and contrast numerous alternatives and view key metrics associated with each candidate solution, such as average cost, the maximum value of a particular variable across a range of possible scenarios, and the average level of service. Using Excel, these results can easily be presented in both graphical and tabular formats. The user is then able to select the most robust solution based on how each individual candidate solution is expected to perform over a wide range of possible parameter values.

## References

[1] J.F. Bard, M. Wamsganss, A matching-based interactive method for MCDM, Proceedings of the International Conference on Multiple Criteria Decision Making, Bangkok, Thailand, 1990, pp. 963– 978.

[2] F. Ben Abdelaziz, P. Lang, R. Nadeau, Dominance and efficiency in multicriteria decision under uncertainty, Theory and Decision 47 (1999) 191 – 211.

[3] R. Benayounn, J. de Montgolfier, J. Tergny, O. Larichev, Linear programming with multiple objective functions: step method (STEM), Mathematical Programming 1 (3) (1971) 366– 375.

[4] J.H. Boyett, J.T. Boyett, Beyond Workplace 2000: Essential Strategies for the New American Corporation, Dutton, E.P. Dutton, New York, 1995.

[5] A. Changchit, M.P. Terrell, A multiobjective reservoir operation model with stochastic inflows, Computers and Industrial Engineering 24 (2) (1993) 303 – 313.

[6] M. Dempster, Stochastic Programming, Academic Press, London, 1980.

[7] D. Dubois, M. Grabisch, F. Modave, H. Prade, Relating decision under uncertainty and multicriteria decision making models, International Journal of Intelligent Systems 15 (2000) 967– 979.

[8] J. Dupaova´, Scenario-base stochastic programs: resistance with respect to sample, Annals of Operations Research 64 (1996) 21 – 38.

[9] P.H. Farquhar, Utility assessment methods, Management Science 30 (1984) 1283– 1300.

[10] D. Fylstra, L. Lasdon, J. Watson, A. Waren, Design and use of the Microsoft Excel solver, Interfaces, (September – October, 1998) 29– 55.

[11] A.M. Geoffrion, J.S. Dyer, A. Feinber, An interactive approach for multicriterion optimization, with an application to the operation of an academic department, Management Science 19 (4) (1972) 357 – 368.

[12] A. Goicoechea, D.R. Hansem, D.R. Duckstein, Multiobjective Decision Analysis With Engineering and Business Applications, Wiley, New York, 1982.

[13] C.L. Hwang, A.S. Masud, Multiple Objective Decision Making—Methods and Applications, Springer, New York, 1979.

[14] P. Kall, S.W. Wallace, Stochastic Programming, Wiley, New York, 1994.

[15] R.L. Keeney, H. Raiffa, Decision with Multiple Objective: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[16] G. Klein, H. Moskowitz, A. Ravindran, Interactive multiobjective optimization under uncertainty, Management Science 36 (1990) 58–75.

[17] P. Korhonen, J. Laakso, A visual interactive method for solving the multicriteria problem, European Journal of Operational Research 24 (2) (1986) 277 – 287.

[18] P. Korhonen, J. Wallenius, A Pareto race, Naval Research Logistics 35 (6) (1988) 615– 623.

[19] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, 2nd ed., McGraw-Hill, New York, 1991.

[20] J.N. Morse, Reducing the size of the nondominated set: pruning by clustering, Computers and Operations Research 7 (1980) 55– 66.

[21] S.B. Petkov, Multiperiod planning and scheduling of multiproduct batch plants under demand uncertainty, Industry and Engineering Chemistry Research 36 (11) (1997) 4864 – 4881.

[22] C.T. Ragsdale, Spreadsheet Modeling and Decision Analysis: A Practical Introduction to Management Science, 3rd ed., South-Western, Cincinnati, 2001.

[23] T.R. Rakes, G.R. Reeves, Selecting tolerances in chance-constraint programming: a multiple objective linear programming approach, Operations Research Letters 4 (2) (1985).

[24] J.L. Ringuest, S.B. Graves, A sampling-based method for generating nondominated solutions in stochastic MOMP problems, European Journal of Operational Research 126 (2000) 651 – 661.

[25] S.M. Sanchez, D.L. Smith, E.C. Lawrenece, Sensitivity and scenario analysis for simulation metamodels, Proceedings of the Winter Conference on Simulation, ACM Digital Library, San Diego, CA, USA, December 8 – 11, 1996, pp. 1440 – 1447.

[26] S. Sen, J.L. Higle, An introductory tutorial on stochastic linear programming models, Interfaces, (March – April, 1999) 33– 61.

[28] N. Srinivas, K. Deb, Multiobjective optimization using nondominated sorting in genetic algorithms, Evolutionary Computation 2 (3) (1994) 221– 248.

[29] R.E. Steuer, Multiple Criteria Optimization: Theory, Computation, and Application, Wiley, New York, 1986.

[30] R.E. Steuer, E.U. Choo, An interactive weighted Tchebycheff procedure for multiple objective programming, Mathematical Programming 26 (1) (1983) 326 – 344.

[31] R.E. Steuer, F.W. Harris, Intra-set point generation and filtering in decision and criterion space, Computers and Operations Research 7 (1980) 41 – 53.

[32] R.E. Steuer, J. Silverman, A.W. Whisman, A combined Tchebycheff/aspiration criterion vector interactive multiobjective programming procedure, Management Science 39 (10) (1993) 1255 – 1260.

[33] M. Sun, A. Stam, R.E. Steuer, Interactive multiple objective programming using Tchebycheff programs and artificial neural networks, Computers and Operations Research 27 (2000) 601 – 620.

[34] Sutardi, C.R. Bector, I. Goulter, Multiobjective water resources investment planning under budgetary uncertainty and fuzzy environment, European Journal of Operational Research 82 (1995) 556– 591.

[35] J. Teghem Jr., D. DuFrane, M. Thauvoye, P. Kunsch, STRANGE: an interactive method for multi-objective linear programming under uncertainty, European Journal of Operational Research 26 (1986) 65– 82.

[36] A. Torn, A sampling-search-clustering approach for exploring the feasible/efficient solutions of MCDM problems, Computers and Operations Research 7 (1980) 67 – 79.

[37] A.P. Weirzbicki, The use of reference objectives in multiobjective optimization, in: Lectures Notes in Economics and Mathematical Systems, vol. 177, Springer, New York, 1980, pp. 468 – 486.

[38] E. Wells, S. Harshbarger, Microsoft Excel 97: Developer’s Handbook, Microsoft Press, Redmond, 1997.

[39] H. Youssef, S.M. Sait, H. Adiche, Evolutionary algorithms, simulated annealing and Tabu search: a comparative study, Artificial Intelligence 14 (2001) 167 – 181.

[40] S. Zionts, J. Wallenius, An interactive programming method for solving the multiple objective programming problem, Management Science 22 (6) (1976) 652 – 663.

[41] S. Zionts, J. Wallenius, An interactive multiple objective linear programming method for a class of underlying nonlinear utility functions, Management Science 29 (5) (1983) 519 – 529.

David C. Novak is an Assistant Professor in the Department of Operations and Information Management at the University of Connecticut. He received a PhD in Management Science and Information Technology from Virginia Tech. He also holds a MS in Agricultural and Applied Economics and a BA in Economics from Virginia Tech. Dr. Novak’s research interests include networking and telecommunications, applied simulation, and mathematical programming and applied statistics.

Cliff T. Ragsdale is a Professor in the Department of Business Information Technology and Director of the Dominion Center for Energy Modeling and Optimization at Virginia Tech. He received his PhD in Management Science and Information Technology from the University of Georgia. He also holds an MBA in Finance and BA in Psychology from the University of Central Florida. His primary areas of research interest include microcomputer systems and technology, artificial intelligence, mathematical programming and applied statistics. He has published numerous research articles in journals such as Decision Sciences, Decision Support Systems, Naval Research Logistics, OMEGA: The International Journal of Management Science, Computers and Operations Research, Financial Service Review, Personal Financial Planning, and other publications. He is also the author of the book Spreadsheet Modeling and Decision Analysis published by South-Western.
