---
otero_id: 24966
otero_key: "BEN67UZU"
title: "A Model Management Approach to Business Process Reengineering"
authors: "Levent V. Orman"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518202"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model Management Approach to Business Process Reengineering

Levent V. Orman

To cite this article: Levent V. Orman (1998) A Model Management Approach to Business Process Reengineering, Journal of Management Information Systems, 15:1, 187-212, DOI: 10.1080/07421222.1998.11518202

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518202

![](/api/attachments/BEN67UZU/fulltext/images/8a8a0fbf5a1d3919d7e0eb9ca3d9c1a0a55cf98fd364f592d7878cc6b5635d96.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/BEN67UZU/fulltext/images/84ab8c24f52ce2a8975c5e9efa1ef2beffc86cbdf3f78ace784515410ae33479.jpg)

Submit your article to this journal ↗

![](/api/attachments/BEN67UZU/fulltext/images/cf6880f74e5ca4aced4db359901df3abeca21b7231edbe4347d8e513fdd6bbd1.jpg)

Article views: 11

![](/api/attachments/BEN67UZU/fulltext/images/185d67448b8b9b67f66654bcdbc54cbd06f4a48270364cba4ab3157669e4e85a.jpg)

View related articles ↗

![](/api/attachments/BEN67UZU/fulltext/images/80afaca0148697d4d9ae4fccefbde3819af2f480fb88e157dfbb2f0bdb85192b.jpg)

Citing articles: 2 View citing articles ↗

# A Model Management Approach to Business Process Reengineering

LEVENT V. ORMAN

LEVENT V. ORMAN is Associate Professor of Information Systems at Cornell University, Graduate School of Management. He received a Ph.D. in information systems from Northwestern University. He has published in a variety of journals, including recent articles in MIS Quarterly, Information Systems, Decision Support Systems, IEEE Transactions on Data and Knowledge Engineering, Journal of Intelligent Information Systems, and Acta Informatica. His current research interests are data quality and integrity, business process reengineering, and electronic commerce.

ABSTRACT: A prescriptive and analytical approach is taken to business process reengineering (BPR). The objectives are to provide precise guidelines for process redesign to take full advantage of the efficiencies created by information technologies, and to develop techniques to evaluate alternative structures. A decision-making paradigm of organizations is adopted, and organizational processes are viewed as collections of decision models. Such a simplified analytical model provides an effective methodology to describe and quantify the impact of information technology on organizational structures and processes. The model explains and quantifies a variety of organizational issues such as: the significance of hierarchical structures in organizations, the need for business process reengineering after the introduction of information technology, and the exact conditions under which information technology may (and should) lead to more or less centralized structures. Reoptimization of business processes after the introduction of information technology is formulated as a dynamic programming problem.

KEY WORDS AND PHRASES: business process reengineering, decision models, hierarchies, model complexity, model management, organization design.

BUSINESS PROCESS REENGINEERING IS THE POPULAR TERM for comprehensive reoptimization of organizational processes and structures, often following the introduction of new information technologies into an organization. There is considerable anecdotal evidence that even small changes in the use of information technology (IT) in an organization may require major restructuring of the organization to take full advantage of the efficiencies created by the technology $[3, 11, 12, 13]$ . Conversely, there is also considerable evidence that, without major restructuring, the introduction of IT may not produce the savings needed even to justify the investment $[33, 36]$ . Although the evidence for organizational restructuring to accompany technological change is strong, there is much less agreement on exactly what organizational changes are needed to take full advantage of the technology. The controversy includes both macro- and micro-level changes. At the macro level, the most salient issue is the change in the degree of centralization of decision making, with related questions about the depth and shape of organizational hierarchies. At the micro level, the most salient issue is job definition and content, with related questions about communication patterns, employees' job satisfaction, and skill requirements.

There is a remarkable degree of disagreement on the impact of IT on organizations in all of these areas. IT may be expected to increase centralization because it increases the information-processing capacity of managers, allowing them to centralize more decisions $[35, 42, 43]$ . IT may also be expected to decrease centralization because it reduces the cost of communication and coordination and allows decisions to be delegated $[6, 19, 31, 42]$ . IT may be expected to decrease the depth of organizational hierarchies since it automates some of the middle-management functions, facilitating the movement of information through the organizational hierarchy $[7, 42]$ . IT may also increase the depth of hierarchies by reducing the delays and distortions introduced by the movement of information through the hierarchy $[5, 35]$ . IT may be expected to reduce job satisfaction and diminish skill requirements by routinizing work, by subdividing work into small, highly specialized and repetitive tasks, and by subjecting humans to machine control $[6, 42, 43]$ . IT may also be expected to increase job satisfaction, enrich jobs, and replace low-level clerical jobs with high-skill professional jobs by automating the most mundane tasks $[2, 22, 43]$ .

One explanation for the inconsistency of the empirical evidence is that the impact of IT on organizations is nondeterministic. IT creates options for the organization, and the organizational choice among those options creates the variation in observed outcomes $[10, 28, 43]$ . This explanation is valuable in establishing the complexity of the interactions but not very useful in prediction or prescription, and it gives no guidance to the implementor of IT or business process reengineering. A second explanation for the inconsistency of the empirical evidence is in the treatment of IT as one specific factor. In fact, IT contains many diverse technologies that can be used to support a variety of organizational processes. What gets supported determines what would be the optimum structure for the remaining processes! Clearly, automating clerical tasks would have a different impact on the organization than building executive support systems for top management $[24, 37]$ . This explanation is valuable in narrowing the research question and providing a general framework for prediction and prescription. However, general macro-level prescriptions about organizational structures are not always easy to translate into specific micro-level changes in organizational processes even when those prescriptions are available $[21]$ , and further refinement of the prescriptions is often necessary.

This article takes a prescriptive and analytical approach to business process reengineering. It attempts to determine what changes need to take place to take full advantage of the efficiencies created by IT through a simplified analytical model of organization as an information-processing system. The two major questions are the identification of general structural changes necessary to take full advantage of IT and the efficient implementation of those general changes through a redesign of specific organizational processes. The objectives are to provide insight into the structure of business processes and to provide guidance and analytical tools for the reengineering efforts. In the process, a number of organizational issues are explained and quantified, including the significance of hierarchies, how they concentrate power on top, and how they may create employee alienation at the bottom, the need for business process reengineering after the introduction of IT, the exact conditions under which IT may and should lead to more or less centralized structures, and the exact location and nature of those structural changes. An information processing–decision making paradigm of organizations is adopted $[15, 17, 38, 40]$ . Organizational processes are viewed as collections of decision models within the general framework of organizational information processing. Each decision model is identified by a type of decision which is its output, and contains a sequence of information-processing tasks $[26]$ . The information-processing tasks are the smallest identifiable units of analysis, and their optimum arrangement is the critical design variable determining the efficiency of the resulting structures. The structures will be evaluated in terms of the cost of information processing and the cost of communication among tasks $[21]$ . Both criteria are heavily influenced by the arrangement of tasks, since those arrangements determine what tasks need to communicate with each other, the direction and the content of communication, and the possible sharing of tasks among models.

## Business Processes as Decision Models

A DECISION-MAKING PARADIGM OF ORGANIZATIONS IS ADOPTED where organizational processes are viewed as collections of decision models. Each decision model is associated with a specific type of organizational decision, and it is characterized by a collection of constraints that the decision is required to satisfy. A decision model is a construct that transforms input data into a specific decision that satisfies the constraints of the model. Such decisions are called “satisficing” decisions. Optimizing decisions are special cases of satisficing decisions since optimality conditions can be viewed also as constraints. This view of a decision model is similar to the production rules of expert systems where a set of constraints and a specific action completely characterize each rule, and the satisfaction of the constraints leads to the execution of the action. A constraint is a predicate that transforms a set of input variables to a binary variable (TRUE/FALSE), and it is implemented by a decision task that is the smallest unit of analysis for structural purposes. Decision tasks receive input, search through the input using some decision algorithm to identify the input values that satisfy the constraint involved, and pass on the reduced (and possibly transformed) search space to the next task. After executing all tasks of a model, the set of input values (called the search space) is reduced to a specific decision. In decision theoretic terms, each task reduces the uncertainty associated with the decision and passes on the remaining uncertainty to the next task until all (or sufficient) uncertainty is removed to reach the decision $[26]$ . In decision theory, a utility function is employed to determine the benefits derived from uncertainty reduction, and the costs are assumed to be determined by the market prices. There is a close correspondence between the utility-based analysis of decision theory where costs are assumed to be given by a market place, and the cost-based analysis of model management we employ. To some extent they are substitutes since there is a considerable overlap in analysis, but they are also complementary since neither costs nor utility can be ignored in a complete analysis. Costs are especially critical in a structural analysis since there is a more intuitive and direct relationship between costs and structure, and the costs cannot be assumed given by the market place since there is often no market internal to the organization to determine the price of information. As a matter of fact, the cost of producing and disseminating information appears to be the critical factor behind most organizational structure, where utility plays a more restricted role of providing a threshold to determine what information is worth producing and maintaining $[15]$ .

Each decision task $t_{i}$ is characterized by two parameter types: The cost $c_{i}$ , and the selectivities $s_{i}^{v}$ for each input variable v of task i. The cost of a task is intuitively defined as the resources used to execute the task, such as the value of the decision maker's time for a typical decision task, or the value of the computer time for automated decision tasks. Formally, the cost of a decision task is defined by the complexity function of the implementing algorithm, which is a function of the size of its input variables. Complexity functions are used widely in algorithm analysis [32], and they are positive nondecreasing functions of the sizes of input variables, measuring the amount of (computing) resources used to execute the algorithm. The size of the input variable v of a task $t_{i}$ is called the search space of the task $t_{i}$ with respect to the variable v. Tasks facing large search spaces are more costly than others given the same complexity function due to the nondecreasing characteristic of complexity functions. Similarly, the tasks with higher-order complexity functions are more costly than others, given the same search space. The cost of a task is also referred to as its “complexity.” The second type of parameter is the selectivities $s_{i}^{v}$ of a task $t_{i}$ for each input variable v, or $s_{i}$ when the variable involved is obvious. Selectivity is defined as the remaining search space after the execution of the task as a percentage of the initial search space or alternatively 1—the percent reduction in search space affected by the execution of the task.

## Example 1

A commercial bank has a simple decision model with two tasks for processing mortgage loan applications. Task $t_{1}$ enforces the constraint that requires the applicant to be a homeowner. Task $t_{2}$ involves the constraint requiring the applicant to have an annual income over 30K. Those who satisfy both constraints are approved for a loan.

Mortgage loan decision model

$$
t _ {1}: \quad \text {   homeowner   constraint   }
$$

$$
t _ {2}: \quad \text { salary } > 3 0 k \text {   constraint }
$$

The complexity function for both $t_{1}$ and $t_{2}$ is given as cx where c is a constant and the input variable x is the daily number of applicants. Assuming 100 applicants per day,

60 percent of whom are homeowners, and 20 percent of whom have a salary >30K, the resulting parameters are $c_{1}=c_{2}=100c$ , $s_{1}=0.60$ , and $s_{2}=0.20$ .

The definition of complexity function implies that the cost of a task is dependent on the search spaces of its input variables, and the reduction in any search space achieved by executing a task influences the cost of subsequent tasks. In decision theoretic terms, reduction in uncertainty achieved by executing a task reduces the uncertainty faced by subsequent tasks. Such interaction among the tasks implies that some sequences of tasks are better than others, and (at least) one sequence is the optimum for each model. The structure of a single model is determined solely by the sequence of its tasks, and the optimum structure is the sequence that minimizes the total cost of the model. The extension to multiple interacting models is introduced in the next section, leading to more complex hierarchical structures.

## Example 2

## Case 1

Given the mortgage loan decision model of example 1, with two tasks $t_1, t_2$ , costs $c_1 = c_2 = 100c$ , and selectivities $s_1 = 0.60$ and $s_2 = 0.20$ , the cost of the sequence $(t_1, t_2)$ is $c_1 + s_1c_2 = 100c + 60c = 160c$ , but the cost of $(t_2, t_1)$ is $c_2 + s_2c_1 = 100c + 20c = 120c$ . Different sequences lead to different costs since the execution of a task reduces the search space for the subsequent tasks (e.g., if an applicant does not meet the homeowner test, then there is no need to check his or her salary). Clearly $(t_2, t_1)$ is the optimum sequence with cost $120c$ , as opposed to $160c$ . Intuitively, $(t_2, t_1)$ has lower cost since $t_2$ is a more stringent test, and the costs are the same.

## Case 2

Now assume that $t_{2}$ is more costly to test than $t_{1}$ , with $c_{2}=400c$ and $c_{1}=100c$ , possibly because of the need to verify salaries, but home ownership is a public record. Now the cost of $(t_{1}, t_{2})$ is $c_{1} + s_{1}c_{2} = 100c + 240c = 340c$ , and the cost of $(t_{2}, t_{1})$ is $c_{2} + s_{2}c_{1} = 400c + 20c = 420c$ . Clearly now, $(t_{1}, t_{2})$ is optimal, demonstrating the critical importance of task complexity in structure. In general, the cost of a sequence $t_{i_{1}}, \ldots, t_{i_{n}}$ is

$$
\sum_ {j = 1} ^ {n} c _ {i _ {j}} (v _ {j}),
$$

where $v_{j}$ are the set of variables obtained by substituting <EQ> or variable v, where $v_{o}$ is the search space for variable v.

## Case 3

Similarly, now further assume that $s_1 = 0.90$ . Now the cost of $(t_1, t_2)$ is $c_1 + s_1c_2 = 100c + 360c = 460c$ , clearly higher than the cost of $(t_2, t_1)$ , whose cost remains $420c$ .

$(t_{2}, t_{1})$ is once again the optimal solution, demonstrating the critical importance of selectivity in determining structure.

So far, the selectivities of tasks were assumed independent of the structure, when in fact selectivity of a task may depend on the uncertainty it faces and, hence, what tasks have already been executed. Borrowing Bayesian terminology, $s_{ij}$ will refer to the joint selectivity of tasks ij (i.e., the selectivity achieved by executing tasks i and j); $s_{i/j}$ will refer to the selectivity of task i given that task j has already been executed. If the selectivities are independent, $s_{ij} = s_i s_j$ follows from laws of probabilistic independence. Similarly, $s_{ij} = s_{i/j} s_j$ follows from the definition of conditional selectivity. It is important to note that independence of selectivities does not imply that the tasks are independent. Task independence in common parlance implies no common variables, and that means selectivity = 1 for all tasks that do not involve the variable in question.

## Example 3

An extended mortgage loan decision model is given with three tasks:

Extended mortgage decision model

$t_1$ : Homeowner constraint

$t_2$ : salary $>30\mathrm{k}$ constraint

$t_{3}$ : life expectancy > 20 years constraint

with parameters $c_{1} = c_{2} = c_{3} = 100c$ , $s_{1} = 0.60$ , $s_{2} = 0.20$ , and $s_{3} = 0.70$ .

Case 1

Assuming independence of selectivities, the optimum sequence is $(t_{2}, t_{1}, t_{3})$ from the most stringent test to the least since the costs are the same. The total cost of the optimum sequence is $c_{2} + s_{2}c_{1} + s_{12}c_{3} = 100c + 20c + 12c = 132c$ since $s_{2} = 0.20$ and $s_{12} = 0.20 \times 0.60 = 0.12$ .

## Case 2

Now assume interdependence of $s_{1}$ and $s_{2}$ since those with salary >30k are more likely to be homeowners. Assuming $s_{12} = 0.15 \neq 0.20 \times 0.60$ , the optimum sequence is $(t_{2}, t_{3}, t_{1})$ with total cost of $c_{2} + s_{2}c_{3} + s_{23}c_{1} = 100c + 20c + 14c = 134c$ since $s_{23} = 0.20 \times 0.70 = 0.14$ . The second best sequence is $(t_{2}, t_{1}, t_{3})$ with total cost of $c_{2} + s_{2}c_{1} + s_{12}c_{3} = 100c + 20c + 15c = 135c$ since $s_{12} = 0.15$ . The cost of sequence $(t_{2}, t_{1}, t_{3})$ has increased from 132c to 135c due to the interdependence between $s_{1}$ and $s_{2}$ . Clearly, the interaction among the tasks is a critical variable in determining structure.

## Example 4

A retailer has a simple decision model with three tasks to make an advertising decision in a given region:

Advertising decision model

$t_1$ : low demand constraint

$t_2$ : low advertising cost constraint

$t_3$ : low production cost constraint

The decision rule is to advertise if all three constraints are satisfied. The complexity of each task is cx, where x is the number of regions.

## Case 1

Given 100 regions $c_{1} = c_{2} = c_{3} = 100c$ . The probability of $t_{1}, t_{2}$ , or $t_{3}$ being satisfied in a region is $s_{1}, s_{2}$ , or $s_{3}$ , respectively. $s_{1} = 0.60$ , $s_{2} = 0.20$ , $s_{3} = 0.70$ . Assuming independence of tasks, the optimum sequence is $(t_{2}, t_{1}, t_{3})$ with total cost of $c_{2} + s_{2}c_{1} + s_{12}c_{3} = 100c + 20c + 12c = 132c$ .

## Case 2

By changing the cost $c_{2}=400c$ , the optimum sequence becomes $(t_{1}, t_{2}, t_{3})$ with total cost of $c_{1}+s_{1}c_{2}+s_{12}c_{3}=100c+240c+12c=352c$ .

## Case 3

Assuming interdependence of $s_{1}$ and $s_{2}$ with $s_{12} = 0.15 \neq 0.20 \times 0.60$ , the optimum sequence is $(t_{2}, t_{3}, t_{1})$ with total cost of $c_{2} + s_{2}c_{3} + s_{23}c_{1} = 100c + 20c + 14c = 134c$ , as in the previous example.

Some variables are created within tasks rather than being input from the environment. The task that creates a variable is called a “source,” and the task that uses such a variable is called a “target.” Such derived variables are assigned an initial size of arbitrarily large M to prevent target tasks executing before the source task in the optimal solution. Only the source task with its especially small selectivity can bring M down to its realistic size. This special case corresponds to the dependency graphs of systems analysis $[34]$ .

The decision model approach to process design can be generalized to continuous variables and infinitely large search spaces. So far, search space has been used to measure the uncertainty faced by a task, and the reduction in search space has been used as a measure of uncertainty reduction achieved by executing a task. These measures are intuitive and useful when finite discrete search spaces are involved, but they fail for continuous or infinitely large search spaces, which are commonly found in decision models. A more general concept than the size of the search space is provided by information theory to measure uncertainty, which is the concept of entropy $[16]$ . Entropy is commonly used to measure the uncertainty related to a random variable, and can be used to measure the uncertainty faced by a task. Similarly, change in entropy can be used to measure the change in uncertainty due to the execution of a task. More importantly, for finite discrete search spaces with no additional information about the search space, entropy specializes to the size of the search space, justifying our initial intuitive choice. Given a random variable with a probability distribution $p(x)$ , its entropy is defined as $-\int p(x)\log(p(x))dx$ . Similarly, for a discrete random variable with probabilities $p_{i}$ associated with each distinct outcome i, its entropy is defined as

$$
- \sum_ {i} p _ {1} \log (p _ {i}).
$$

For the loan decision of example 1, a binary predicate (i.e., YES/NO decision) defined on a search space of 100 customers leads to $2^{100}$ possible outcomes. With no additional information, each outcome is equally likely, that is,

$$
p _ {i} = \frac {1}{2 ^ {1 0 0}}.
$$

$$
\text { Entropy } = - \sum \frac {1}{2 ^ {1 0 0}} \log_ {2} \left(\frac {1}{2 ^ {1 0 0}}\right) = - 2 ^ {1 0 0} \frac {1}{2 ^ {1 0 0}} \log_ {2} \left(\frac {1}{2 ^ {1 0 0}}\right) = 1 0 0,
$$

which is equal to the search space.

Search space is an appropriate measure of uncertainty for discrete variables with the assumption of no additional prior information. The existence of prior information would require the use of entropy for an exact measure of uncertainty. Similarly, for continuous variables, entropy would be the appropriate measure of uncertainty since search space would involve infinitely large spaces.

## Example 5

A product pricing decision requires meeting a revenue goal within a short-term capacity constraint. This model involves two tasks:

$$
\begin{array}{l l} \text { Product   pricing   model } \\ t _ {1}: & \text { capacity   constraint   test } \\ t _ {2}: & \text { revenue   goal   test } \end{array}
$$

Assume that the feasible prices initially have a uniform distribution over the \$10–18 range. The capacity constraint selects only the range \$10–14, and the revenue goal selects only the range \$12–18, resulting in acceptable prices within the \$12–14 range. Note that a revenue-maximizing model would be similar except for possibly returning a unique price (entropy = 0). Assuming uniform distributions:

Initial entropy $= -\int_{10}^{18}\frac{1}{8}\log \left(\frac{1}{8}\right)dx = 3$

Final entropy $= -\int_{12}^{14}\frac{1}{2}\log \left(\frac{1}{2}\right)dx = 1$

Entropy after $t_1 = -\int_{10}^{14}\frac{1}{4}\log \left(\frac{1}{4}\right)dx = 2$ ;

Entropy after $t_2 = -\int_{12}^{18}\frac{1}{6}\log \left(\frac{1}{6}\right)dx = 2.5$ .

The next step is the computation of uncertainty reduction: When computing with search spaces, we have used reduction in search space as a percentage of the initial search space to measure the reduction in uncertainty. This measure fails with entropy since the initial entropy may be zero or negative. The appropriate measure of uncertainty reduction is the change in entropy due to a task as a percentage of the total change in entropy due to all tasks, since entropy changes can be meaningfully compared, but comparisons between changes and absolute entropies are not very meaningful $[16]$ . Most significantly, this measure of entropy change again specializes to search-space reduction as a percentage of initial search space, with the assumption that initial search spaces are much larger than the final search spaces remaining after all the tasks have been executed. Selectivity is still defined as a one-percent reduction in uncertainty.

## Example 6

The product pricing model of example 5 leads to the following selectivities by each task:

Total change in entropy = 3-1 = 2.

Entropy reduction by $t_1 = \frac{3 - 2}{2} = 0.50$

Selectivity $s_1$ of $t_1 = 1 - 0.50 = 0.50$

Entropy reduction by $t_2 = \frac{3 - 2.5}{2} = 0.25$

Selectivity $s_2$ of $t_2 = 1 - 0.25 = 0.75$

Entropy reduction by $t_1, t_2 = \frac{3 - 1}{2} = 1.00$

Selectivity $s_{12}$ of $t_1, t_2 = 0$

where the selectivities are consistent with the intuition about uncertainty reduction.

In summary, entropy reduction as a measure of uncertainty reduction specializes to search-space reduction when:

a. The search space is finite and discrete.

b. No prior information about the search space is available.

c. The initial search space is much larger than the final search space remaining after the execution of all tasks (or, alternatively, the final search space is null).

We will continue to use search space as a measure of uncertainty because of its intuitive and practical value, whenever these assumptions can be reasonably expected to hold.

## Multimodel Structures

AN ORGANIZATION CAN BE VIEWED AS A COLLECTION OF INTERACTING decision models. Structuring each model independently, without considering its interaction with others, is likely to be suboptimal. Complex organizations containing such multiple interacting models require a complex architecture involving multilevel, multicomponent structures to minimize information-processing costs $[17]$ . The principal tool of structuring is decomposition. Decomposition is often touted as the basis of all structure $[1]$ . It has been studied extensively, but there is no consensus about why and when systems should be decomposed into smaller components. The oldest theory is information overload. It suggests that organizational activities are decomposed into smaller tasks and assigned to different employees to prevent the complexity of a job from exceeding employees' complexity tolerance $[39]$ . This theory is simple and quite effective in explaining the cognitive limitations of humans, but it does not capture the essence of structure. It does not explain the structure often found within an individual job, nor does it explain extensive structure imposed on relatively idle components of an organization (e.g., when large processors are assigned to relatively small tasks in computerized systems).

The second theory proposes a reduction in the complexity of a system by dividing complex units into small relatively independent units $[34, 41]$ . The reduction is claimed to follow from the multiplicative effect on complexity of the variables within a unit, as opposed to the additive effect on complexity when the variables are split into multiple independent units. This theory elegantly explains the effect of interdependent variables on complexity in contrast with the effect of independent variables. It further suggests that complexity could be reduced by splitting interdependent variables into separate independent units, but only by ignoring their interdependence and producing a suboptimal solution. That tradeoff between reduction of complexity and sub-optimization has not been clearly quantified and is addressed in this paper.

The third theory suggests that processors (human or machine) are more efficient in repetitive execution of the same task than in switching from task to task, leading to savings when the tasks are decomposed and processors are specialized $[2, 25, 40]$ . This theory is related to information theory and information economics since it deals with the information content of each unit. However, the theory acknowledges that, while saving switching costs, decomposition introduces communication and coordination costs in all cases except when the tasks are completely independent. Moreover, specialized processors introduce additional risk associated with processor failure, since any failure by a specialized processor has an impact on all tasks that share it $[19]$ . This theory also has difficulty quantifying the tradeoffs, and demonstrating why and when the switching costs would be so significantly higher than the communication and failure costs to provide the basis of fundamental structures.

This article adopts a variant of the last two theories and proposes “sharing” as a fundamental basis for structure. Interacting models of a complex organization have many common tasks, and avoiding duplication of a common task, for every model that needs it, can be a significant source of efficiency. However, tasks exist in a context; they are rarely identical in multiple contexts, which makes sharing difficult. More specifically, tasks are optimized to fit into the context of a specific model, and shared tasks cannot be optimized as effectively since they need to serve multiple objectives. This tradeoff between savings resulting from sharing and the costs resulting from suboptimization of shared tasks is critical in determining optimum structure. The relationship to structure is through decomposition. Decomposition creates smaller components that are more readily shareable by more models. The savings produced by more sharing, and the costs resulting from suboptimization of the shared components, determine the optimum level of decomposition and the variety of structures it causes.

## Example 7

The commercial bank in example 1 has two decision models associated with each mortgage loan application: one for a short-term loan and one for a long-term loan. Each model is executed for each loan applicant, and each consists of two tasks as shown below:

$$
\begin{array}{l l} \text {Short - term loan decision} & \text {Long - term loan decision} \\ t _ {1}: \text {homeowner constraint} & t _ {1}: \text {homeowner constraint} \\ t _ {2}: \text {salary > 30k constraint} & t _ {3}: \text {life expectancy > 20 years constraint} \end{array}
$$

The complexity function for $t_{1}$ , $t_{2}$ , and $t_{3}$ is given as cx where c is a constant, and x is the number of applicants. Assuming 100 applicants per day, 60 percent of whom are homeowners, 20 percent of whom have a salary >30K, and 30 percent of whom have a life expectancy >20 years; the resulting parameters are $c_{1}=c_{2}=c_{3}=100c$ , $s_{1}=0.60$ , $s_{2}=0.20$ , $s_{3}=0.30$ .

## Case 1

If the two models were executed independently, the optimum sequence would be $(t_{2}, t_{1})$ and $(t_{3}, t_{1})$ , respectively, leading to the costs of $c_{2} + s_{2}c_{1} = 100c + 20c = 120c$ , and $c_{3} + s_{3}c_{1} = 100c + 30c = 130c$ , respectively. Total cost $= 120c + 130c = 250c$ .

## Case 2

Alternatively, consider the decomposition of these two models into three models, each containing only one task, with $t_{1}$ shared by the two decisions. To achieve the benefits of sharing, $t_{1}$ has to be executed first, otherwise $t_{2}$ and $t_{3}$ will produce different sets of customers to be processed, and the benefits of sharing will be lost! With decomposition, $t_{1}$ will be executed only once at a cost of $c_{1}=100c$ , and $t_{2}$ and $t_{3}$ will be executed next each at a cost of $s_{1}c_{2}=s_{1}c_{3}=60c$ . Total cost $100c+60c+60c=220c$ . Clearly, decomposition pays since $220c<250c$ .

## Case 3

However, by changing the homeowner percentage to 80 percent, $s_{1}=0.80$ , the decomposed model would lead to a cost of $c_{1}+s_{1}c_{2}+s_{1}c_{3}=100c+80c+80c=260c$ , which is clearly higher than the undecomposed models whose costs remain unchanged. In this case, the savings of 100c on the home ownership test task comes at too great a cost of suboptimization of each model by changing the optimum sequence of executing tasks.

## Case 4

Now also change the cost of $t_{1}$ by reducing it to 50c. The cost of undecomposed models now is $c_{2} + s_{2}c_{1} = 100c + 10c = 110c$ and $c_{3} + s_{3}c_{1} = 100c + 15c = 115c$ , respectively, with the total cost of 225. The cost of decomposed models is $c_{1} + s_{1}c_{2} + s_{1}c_{3} = 50c + 80c + 80c = 210$ . Clearly, decomposition is the optimum solution again.

Decomposition does not in and of itself reduce complexity; rather, it facilitates sharing. Sharing reduces complexity since shared tasks do not have to be duplicated for every decision model that needs them. Sharing also leads to local suboptimization, since models cannot do their information processing in the optimum sequence but have to accommodate the structure imposed by the shared task. This imposition is realized through communication between the shared task and the models that receive information from it, and it is often called “communication and coordination cost” [19]. Clearly, this cost is much higher than the cost of transporting messages. It also involves the cost of accommodating the messages received, by rearranging the tasks comprising the receiving model.

## Example 8

The retailer in example 4 has two decision models to make an advertising decision and a production increase decision in each region:

Advertising decision model

Production increase decision model

$t_1$ : low demand constraint

$t_3$ : low production cost constraint

$t_2$ : low advertising cost constraint

t4: adequate capital constraint

$t_3$ : low production cost constraint

The decision rule is to advertise if $t_{1}$ , $t_{2}$ , $t_{3}$ are satisfied, and to increase production if $t_{3}$ , $t_{4}$ are satisfied. $c_{1}=c_{2}=c_{3}=c_{4}=100c$ . $s_{1}=0.60$ , $s_{2}=0.20$ , $s_{3}=0.72$ , $s_{4}=0.30$ . The critical question is whether to decompose $t_{3}$ as a separate model to be shared by the two decisions.

## Case 1

Assuming independence, the undecomposed models have the optimum sequence $(t_{2}, t_{1}, t_{3})$ and $(t_{4}, t_{3})$ , respectively, and their costs are $c_{2} + s_{2}c_{1} + s_{12}c_{3} = 100c + 20c + 12c = 132c$ , and $c_{4} + s_{4}c_{3} = 100c + 30c = 130c$ , respectively, with total cost of 262c. The decomposed models would lead to the optimum sequence of $(t_{3}, t_{2}, t_{1})$ and $(t_{3}, t_{4})$ , with the total cost of $c_{3} + s_{3}c_{2} + s_{3}c_{4} + s_{23}c_{1} = 100c + 72c + 72c + 14c = 258c$ . Clearly decomposition is optimal.

## Case 2

Now assume interdependence of $t_{2}$ and $t_{3}$ where $s_{23}=0.20<0.72\times0.20$ . The cost of undecomposed models remains the same at 262c, but the cost of decomposed models is now $c_{3}+s_{3}c_{2}+s_{3}c_{4}+s_{23}c_{1}=100c+72c+72c+20c=264c$ . Clearly, decomposition is no longer optimal, demonstrating the critical importance of task interdependence in determining structure.

## Example 9

The continuous version of example 8 has the same decision models where the advertising decision requires the tasks of forecasting demand, determining the advertising cost function, estimating the production cost function, and maximizing yield; and the production decision model requires forecasting demand, estimating the production cost function, applying the short-term capital equipment constraint, and minimizing cost. Past sales and production data are input into both models.

Advertising decision model

Production decision model

$t_1$ : forecast demand

$t_2$ : determine advertising cost function

$t_1$ : forecast demand

$t_3$ : estimate production cost function

$t_3$ : estimate production cost function

$t_4$ : maximize yield

$^{t}_{5}$ : apply capital equipment constraint

$^{t}_{6}$ : minimize cost

Each task imposes a constraint on the decision and reduces uncertainty. Assuming $t_{1}$ and $t_{3}$ convert large input spaces to a small number of alternatives, and hence have very small selectivities, and the task complexities are approximately the same, the optimum solution would involve a decomposition and sharing of $t_{1}$ and $t_{3}$ . Many organizational processes have such clear decompositions, leading to intuitive and simple designs without formal analysis.

## Structure and Reengineering

DECOMPOSITION, INTRODUCED IN THE PREVIOUS SECTION, HAS A NUMBER of implications for organizational structures. It explains a variety of commonly observed structures and processes and predicts a variety of empirically testable characteristics of structures and processes.

## Decomposition Leads to Hierarchical Structures

Consider a model $M_{1}$ shared by a set of models $E_{1}, \ldots, E_{n}$ . Call $M_{1}$ the “manager,” and $E_{i}$ the “employees,” since $M_{1}$ produces an output that reduces the uncertainty faced by $E_{1}, \ldots, E_{n}$ , and the output of $M_{1}$ can be viewed as a directive since it restricts the activities of $E_{1}, \ldots, E_{n}$ . $M_{1}$ in return, can share a model T with other models $M_{2}, \ldots, M_{k}$ . Call T the “top manager” for the same reasons, and possibly continue to create higher-level managers in the same fashion. The resulting multilevel hierarchy is a very common structure in both automated systems and human organizations. The structure is constrained to be hierarchical since every model has only one manager whose output is the starting point for that model’s information processing. Each model can have only one manager, since each model can share only a starting sequence of its tasks. Sharing from the middle of the sequence will not lead to savings, since the shared task will face different search spaces in each model due to the execution of different tasks preceding it as demonstrated in example 7. (This assumption will be relaxed in the multimodel formulation presented later, leading to nonhierarchical structures). Obviously, the manager itself can share a starting sublist of its list of tasks, leading to a multilevel hierarchy so common in structural design. Hierarchies follow directly from the assumptions that models execute their tasks in a linear sequence and share from the top of the sequence to realize the benefits of sharing.

## Decomposition and Its Consequent Hierarchies Concentrate "Power" in Certain Models

The shared model M (manager) described above is in a critical position within the organization. It provides a critical output shared by many models (its employees), and its failure affects many models. This is the essence of a manager's “power” in an organization, measured in terms of its contribution to the organizational performance, or in terms of the cost of its failure. Lower-level models $E_{1}, \ldots, E_{n}$ are in a precarious position with respect to the manager model. On the one hand, they depend on it for their performance; on the other hand, the communication (directives) from the manager often forces them to suboptimize locally and limit their contribution to the organization. It is not unusual then for an employee to perceive the manager model as limiting its performance and contribution, and robbing it of organizational power, as we will see in the next proposition.

## Decomposition and Hierarchies Lead to “Bureaucratic Alienation”

The organizational literature is replete with references to the alienation employees feel within highly bureaucratic hierarchical structures $[25, 27]$ . It is possible to explain the alienation as the discrepancy between the contribution an employee could make to an organization and the contribution that she or he is allowed to make by the structure. The bigger the discrepancy, the more the employee would feel constrained by the structure and prevented from making her or his maximum contribution and deriving the benefits thereof. Consider the employee assigned to the short-term loan decision in the decomposed model of example 7. Clearly, this employee would think that the short-term loan decision model is grossly inefficient. If he or she were allowed to make the decision alone, as in the undecomposed model of example 7, as opposed to being instructed by the shared model, he or she could make the decision much more efficiently by changing the sequence of tasks, and reducing the cost from 160c to 120c. Consequently, the employee is likely to feel restrained by his or her manager and unable to contribute his maximum to the organization, leading to alienation. Of course, his narrow specialization limits his vision and prevents him from observing the long-term loan decision model; hence, he is unable to see and appreciate the sharing and its benefits to the organization. Sharing, and the consequent benefits to the organization, put a straitjacket on individual employees and prevent them from maximizing their own impact on the organization, as they perceive it.

Automated Components of an Organization Have to Be Structured Together with Human Components to Create an “Organizational Fit”

Information systems literature is replete with references to “organizational fit” where computer-based models and human-based models, each designed alone to be efficient, do not work well when they are brought together $[14, 29, 37, 44]$ . It is possible to explain the organizational fit problem as the suboptimization resulting from structuring each component separately, as opposed to designing a single efficient structure that encompasses both components. Historically, the components were designed separately since there was no effective framework to subject both the human and the computer-based organization to the same type of analysis. Decision models appear promising to provide that framework. Consider the two models of example 7, and assume that the short-term loan is an automated and the long-term loan is a human decision model. When each one is structured separately, no decomposition is justified, since the benefits of sharing tasks between the two are not considered. Alternatively, structuring the system as a whole leads to a decomposition, as shown in example 7. Clearly, designing human and machine-based models separately is suboptimal. Moreover, sharing small-model components between systems and humans has been suggested; this forms the basis of “decision support systems” $[30, 39]$ .

Automating Some Tasks May Have Extraordinary Repercussions throughout the Organization, Requiring “Business Process Reengineering”

Mere automation of a task, and the consequent reduction in the cost of executing it, may lead to suboptimization. Reoptimization may require radical changes in the complete organizational structure, as commonly suggested in the business process reengineering literature $[8, 11, 12]$ . The intuition behind this requirement is based on the sensitivity of the optimum structure to the cost of executing tasks. Changing the selectivity or the cost of a task may have a dramatic effect on the optimum structure, and the effects may propagate over many models as a result of sharing and the strong interaction it creates. Example 7 demonstrated in case 2 that decomposition was undesirable when all tasks were equally difficult to execute. However, when one task was (presumably) automated, and its cost dropped 50 percent, decomposition became desirable, making the optimum organizational structure dependent on the cost of executing each task.

## Low-Selectivity Tasks Are More Likely to Be Found at Higher Levels of the Organizational Hierarchy

High-level managerial decision models are more likely to be ill-defined, fuzzy models, with large amounts of external information processed in cursory and intuitive fashion to focus the organization quickly and efficiently around some well-defined goals. These are low-selectivity models by virtue of the fact that they receive large amounts of unorganized, high uncertainty, external information, and produce small search spaces focused around well-defined internal goals with little uncertainty. The desirability of low-selectivity models at high levels in an organization can be shown easily within the model management paradigm. Example 7 informally demonstrated this proposition since a task $t_{1}$ with high selectivity (80 percent) was not shareable, but when its selectivity was reduced (60 percent), it became shareable, which led to a decomposition, which in turn pushed $t_{1}$ upward in the task sequence and in the structural hierarchy to realize the benefits of sharing. In general, a task $t_{1}$ is more likely to be shared with all the consequences listed above, as its selectivity is reduced, assuming that all complexity functions are monotonically nondecreasing. Given two models $(t_{2}, t_{1})$ and $(t_{3}, t_{1})$ where $t_{2}$ and $t_{3}$ correspond to all tasks preceding $t_{1}$ in the two models respectively, let the complexity functions of $t_{1}, t_{2}$ , and $t_{3}$ be $c_{1}(x), c_{2}(x)$ , and $c_{3}(x)$ respectively, where x is the initial search space faced by the two models, and let the selectivities be $s_{1}, s_{2}$ , and $s_{3}$ , respectively. The cost of the undecomposed models is given as:

$$
c _ {u} = c _ {2} (x) + c _ {3} (x) + c _ {1} (s _ {2} x) + c _ {1} (s _ {3} x)
$$

since $t_{2}$ and $t_{3}$ are executed first with the search space x, and $t_{1}$ is executed next in each model with an appropriately reduced search space. Similarly, the cost of the decomposed model is:

$$
c _ {d} = c _ {1} (x) + c _ {2} (s _ {1} x) + c _ {3} (s _ {1} x).
$$

since $t_1$ is executed once with the initial search space, and $t_2$ and $t_3$ are executed next in each model for the reduced search space. The proposition is that $c_d - c_u$ becomes smaller (i.e., decomposition more desirable) as the selectivity $s_1$ becomes smaller. In other words $(c_d - c_u)$ and $s_1$ change in the same direction, or

$$
\begin{array}{l} \frac {d}{d s _ {1}} (c _ {d} - c _ {u}). \\ = \frac {d}{d s _ {1}} (c _ {1} (x) + c _ {2} (s _ {1} x) + c _ {3} (s _ {1} x) - c _ {2} (x) - c _ {3} (x) - c _ {1} (s _ {2} x) - c _ {1} (s _ {3} x) \\ = \frac {d}{d s _ {1}} (c _ {2} (s _ {1} x) + c _ {3} (s _ {1} x)) \text { since all other terms are independent of } s _ {1} \\ = x \frac {d}{d y} c _ {2} (y) + x \frac {d}{d y} c _ {3} (y), \text { by substituting } y = s _ {1} x. \end{array}
$$

$\geq 0$ , since all terms are nonnegative.

The derivatives are nonnegative since the complexity functions have been assumed to be monotonically nondecreasing, and x is nonnegative since it is defined as the size of the search space (or total reduction in entropy). The extension to multivariable complexity functions is straightforward. Intuitively, this proposition is equivalent to splitting relatively independent tasks into separate units, if one defines independence of a task from the rest of a model as its closeness to the top of the optimum sequence of tasks. Those tasks at the top are relatively independent of others since they can be separated and shared with relatively small communication cost. Those at the bottom impose heavy communication costs, since the rest of the model has to be rearranged to absorb the communication from the shared task.

Among Interdependent Tasks, Those That Reinforce Each Other (Low Joint Selectivity) Are More Likely to Be Found in Higher Levels of an Organizational Hierarchy, and Those That Negatively Affect Each Other (High Joint Selectivity) Are Likely to Be at Lower Levels

Top-level decisions in an optimum organization are likely to be those that benefit the organization as a whole, rather than benefiting a specific department at the expense of another. The narrow political decisions are made at lower levels through battles among departments. This conclusion follows immediately from the previous proposition that low-selectivity tasks are more likely to be at the top and shared. Treating multiple interdependent tasks as a single task, their joint low selectivity pushes them up as a group in the hierarchy and allows them to be shared. Joint low selectivity means positive reinforcement among the tasks since they increase each other's effectiveness by reducing search spaces for subsequent tasks.

Cost Reduction May Lead to a Variety of Outcomes Depending on Task Uncertainty and Task Specialization

The complexity of this analysis explains the contradictions in the organizational impact literature of information systems, since automated systems often result in cost reductions for various organizational tasks. Similarly, the business process reengineering literature, although explicit in the need to restructure, has great difficulty prescribing what structural changes may be appropriate following automation and the consequent reduction in various costs. The model management paradigm suggests four possibilities depending on two factors. Task uncertainty refers to the uncertainty reduction achieved by a task. Task specialization refers to the frequency of occurrence of the task within the organization (i.e., whether it is specific to a small set of decision models, or common to many). High uncertainty–high occurrence tasks such as statistical decision models lead to increased centralization when their costs are reduced; high uncertainty–low occurrence tasks such as individualized decision support models lead to decentralization upon cost reduction; low uncertainty–high occurrence tasks such as communication and coordination models lead to decentralization; and low uncertainty–low occurrence tasks such as clerical decision models lead to increased centralization upon cost reduction. The intuition behind these results can be summed up as a shift in resources and power toward those models that become more efficient through cost reduction and automation.

Top-level, highly uncertain, and highly common tasks, when they are automated, concentrate power and decision making in those models. Since they are common within the organization, there are efficiencies to be gained from sharing these tasks, and those who execute such tasks are in a position to make major contributions to the organization by reducing their costs and derive the benefits by centralizing the common task and consolidating the power resulting from the dependence of many decision models on the common task. High uncertainty–low occurrence tasks such as individualized decision support models, on the other hand, lead to decentralization of structures and decisions, since these models, while gaining power, cannot wield organization wide influence because of the specialized nature of their contribution, and hence contribute to the dispersion of power. This is commonly observed in the rise of staff functions and consequent dispersion of power in professional organizations such as universities and hospitals. Low uncertainty–high occurrence tasks also lead to decentralization under cost reduction, since they push power and decisions toward lower-level (i.e., low-uncertainty) models. This is commonly observed in decentralization that results from communication and coordination technologies. Low uncertainty–low occurrence tasks, on the other hand, increase centralization by reducing their costs, since they push the power away from themselves to higher levels in the organization. This is often observed when clerical tasks such as word processing are automated, often leading to central control of these functions through secretarial pools and word-processing departments. In sum, high uncertainty refers to top-level tasks in the organizational hierarchy and low uncertainty to low-level tasks. High occurrence allows the models to exert organization-wide influence; low occurrence prevents it by pushing the power away to other models.

In model management terminology, assume that two models are given with tasks $(t_{1}, t_{2})$ and $(t_{1}, t_{3})$ , cost functions $c_{1}(x)$ , $c_{2}(x)$ , and $c_{3}(x)$ and the selectivities $s_{1}$ , $s_{2}$ , $s_{3}$ for the tasks $t_{1}$ , $t_{2}$ , $t_{3}$ , respectively. Cost reduction may lead to four distinct outcomes, depending on uncertainty and task specialization. Generalization to multiple models with multiple tasks is straightforward by analyzing two models and two tasks at a time.

Such a restricted analysis is sufficient to determine the general tendencies. A more general approach to determine the exact optimum solution under each condition is introduced in the section on structural design. As demonstrated above, the cost of the undecomposed model is:

$$
c _ {u} = c _ {2} (x) + c _ {3} (x) + c _ {1} (s _ {2} x) + c _ {1} (s _ {3} x),
$$

and the cost of the decomposed model where $t_{1}$ is shared is:

$$
c _ {d} = c _ {1} (x) + c _ {2} (s _ {1} x) + c _ {2} (s _ {1} x).
$$

$t_{1}$ is the common, high-occurrence task; $t_{2}$ and $t_{3}$ are specialized low-occurrence tasks. It is safe to assume that all three tasks have similar selectivities since neighboring tasks within a shared sequence tend to have similar selectivities, and neighboring tasks are more likely to exchange positions and lead to structural change than distant tasks in the sequence. The difference of the two costs is:

$$
c _ {d} - c _ {u} = c _ {1} (x) + c _ {2} (s _ {1} x) + c _ {3} (s _ {1} x) - c _ {2} (x) - c _ {3} (x) - c _ {1} (s _ {2} x) - c _ {1} (s _ {3} x).
$$

$c_{d} - c_{u} < 0$ implies that decomposition decreases costs, and hence leads to more decomposition, that is, more centralization.

$c_{d} - c_{u} > 0$ implies that decomposition increases costs, and hence reduces decomposition, that is, less centralization,

$c_{d} - c_{u} = 0$ implies no definite trend where the changes depend on the exact values of the parameters.

If we assume positive cost functions with nonzero search spaces, the following four cases correspond to the four types of tasks experiencing cost reduction:

Case 1: High Uncertainty–High Occurrence Task ( $t_{1}$ with low selectivity)

$$
\begin{array}{l l} \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = c _ {1} (x) > 0 & \text {   that   is,   less   centralization.   } \\ c _ {1} \to \infty & \\ \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = - c _ {2} (x) - c _ {3} (x) <   0 & \text {   that   is,   more   centralization   } \\ c _ {1} \to 0 & \end{array}
$$

implying increased centralization as the cost of $t_1$ goes down.

Case 2: Low Uncertainty–High Occurrence Task ( $t_{1}$ with high selectivity)

$$
\lim c _ {d} - c _ {u} = - c _ {1} (x)
$$

$$
s _ {1}, s _ {2}, s _ {3} \rightarrow 1
$$

that is, more centralization

$$
c _ {1} \rightarrow \infty
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\lim_{s_1, s_2, s_3 \to 1} c_d - c_u = 0$ that is, neutral $c_1 \to 0$ implying slightly decreased centralization as the cost of $t_1$ goes down.
</div>

Case 3: High Uncertainty–Low Occurrence Tasks ( $t_{2}$ , $t_{3}$ with low selectivity)

$$
\begin{array}{l l} \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = - c _ {2} (x) - c _ {3} (x) <   0 & \text { that   is,   more   centralization } \\ c _ {2}, c _ {3} \to \infty & \\ \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = c _ {1} (x) > 0 & \text { that   is,   less   centralization } \\ c _ {2}, c _ {3} \to 0 & \end{array}
$$

implying decreased centralization as the costs of $t_{2}$ and $t_{3}$ go down.

Case 4: Low Uncertainty–Low Occurrence Tasks ( $t_{2}$ , $t_{3}$ with high selectivity)

$$
\begin{array}{l l} \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = 0 & \text { that   is,   neutral } \\ c _ {2}, c _ {3} \to \infty & \\ \lim _ {s _ {1}, s _ {2}, s _ {3} \to 0} c _ {d} - c _ {u} = - c _ {1} (x) <   0 & \text { that   is,   more   centralization } \\ c _ {2}, c _ {3} \to 0 & \end{array}
$$

implying slightly increased centralization as the costs of $t_2$ and $t_3$ go down.

Clearly, the impact of information technology on organizational structures depends on a variety of factors, explaining some of the inconsistencies in the literature.

## Structural Design

THE STRUCTURAL DESIGN PROBLEM INVOLVES CHOOSING THE OPTIMAL decomposition by balancing the benefits of sharing with the costs of communication (that is, model suboptimization to accommodate shared models) [9, 18]. To determine the cost of model suboptimization, we will formulate the problem of finding the optimum sequence of information processing within a single model, and then formulate the multimodel problem—that is, balancing the costs of deviating from the optimum sequence in each model against the obvious benefits of sharing.

A model T with tasks $t_{1}, \ldots, tn$ is given. Each $t_{i}$ has a complexity function $c_{i}$ , and selectivity $s_{i}$ . Extension to multiple variables is straightforward by treating $c_{i}$ and $s_{i}$ as vectors. The selectivity $s_{i}$ is defined as $1-r_{i}$ where $r_{i}$ is the percent reduction in search space by executing the task $t_{i}$ . The complexity of each task $t_{i}$ is assumed to be proportional to its search space, and it is reduced by the joint selectivity of all the tasks that have been executed prior to $t_{i}$ . The cost of information processing for a particular sequence of tasks is the total cost of executing all the tasks in that sequence. The single-model problem is to find the optimum sequence of execution for the tasks $t_{1},\ldots,t_{n}$ to minimize the cost of information processing. This problem is a special case of the sequential decision making problem [24, 26] and can be formulated as a dynamic programming problem [32, 38]. It is simpler to solve than the general sequential decision making problem, since the tasks comprising the model (process) are given, and they all need to be executed to satisfy the model. The only decision is the sequence of execution that determines the amount of sharing possible. In the general sequential decision-making problem, a strategy rather than a sequence is sought, and a stopping rule is used at each step to determine if the next step is necessary. This analysis requires a utility function for each task to compute whether its contribution to the decision exceeds its cost. The model management approach does not require a utility function, which is a major advantage since utility functions are notoriously difficult to obtain and verify. The critical problem in business process reengineering is one of structure, as determined by sequence and sharing, rather than computing the value of processes and tasks, which leads to the special case developed here. Extensions beyond structure and the determination of the value and the contribution of processes are left for future work. Finally, considerable computational simplification is possible since some tasks in every process are fixed in sequence because of input–output relationships with other tasks. These fixed sequences can be consolidated into a single task, which simplifies the structural design problem considerably, as shown in the case study presented below.

## Single Model

Given the tasks $t_1, \ldots, t_n \in T$ ; selectivities $s_1, \ldots, s_n \in S$ ; and costs $c_1, \ldots, c_n \in C$ ,

$$
f (T _ {i}) = \underset {t _ {p} \in T - T _ {i}} {\text { MIN }} (\Pi S _ {i}) c _ {p} + f (T _ {i} \cup t _ {p}),
$$

where $T_{i}$ and $S_{i}$ are a set of tasks and the corresponding set of selectivities, respectively.

The objective is to find the optimum cost $f(\Phi)$ where $f(T)=0$ and $\Phi$ is the null set. Intuitively, $f(T_{i})$ represents the optimum cost of the partial model $T-T_{1}$ , that is, the minimum remaining cost after the execution of the tasks $T_{i}$ . It is equal to the cost of the next task $t_{p}+$ the minimum remaining cost after $T_{i}\cup t_{p}$ . The remaining cost after all tasks have been executed is $f(T)=0$ , and the minimum remaining cost before any task is executed $f(\Phi)$ is the objective function. The problem is computationally solvable with complexity of $O(n!)$ .

## Multimodel Formulation

The single-model formulation can be extended in a straightforward fashion to accommodate

multiple models and the sharing of tasks among them.

Given $n$ tasks $t_1, \ldots, t_n \in T$ , with selectivities $s_1, \ldots, s_n \in S$ , respective costs $c_1, \ldots, c_n \in C$ , and $r$ models each consisting of a subset of those tasks $M_1, \ldots, M_r \subseteq T$ ,

$$
f (T _ {1}, \ldots , T _ {t}) = \begin{array}{c} M I N \\ t _ {1} \in T - T _ {1} \\ \cdot \\ \cdot \\ \cdot \\ t _ {r} \in T - T _ {r} \end{array} \sum_ {i - 1} ^ {r} ((\Pi S _ {i}) c _ {i}) - \sum_ {i, j = 1} ^ {i, j = r} ((P I S _ {i}) c _ {i}) + f (T _ {1} \cup t _ {1}, \ldots , T _ {r} \cup t _ {r})
$$

where $f(M_1, \ldots, M_r) = 0$ and the optimum solution is given by $f(\Phi, \ldots, \Phi)$ .

Intuitively, the formulation is similar to the single-model case. $f(T_{1},\ldots,T_{r})$ represents the optimum cost of the partial model $M_{1}-T_{1},\ldots,M_{r}-T_{r}$ , that is, the minimum remaining cost after the execution of $T_{1},\ldots,T_{r}$ . It is equal to the cost of the next step $(t_{1},\ldots,t_{r})+$ the remaining cost after the execution of $(T_{1}\cup t_{1},\ldots,T_{r}\cup t_{r})$ . The tasks that are common to multiple models at the beginning of their sequences are executed only once, leading to the subtraction of their costs in the formulation for every duplicate count. The remaining cost after the execution of all tasks of all models $f(M_{1},\ldots,M_{r})=0$ , and the remaining cost before the execution of any tasks $f(\Phi,\ldots,\Phi)$ is the objective function. The problem is computationally tractable with complexity $O(n!r)$ .

## A Case Study: Corporate Purchasing System

A purchasing requisition originates in a department. The originating department identifies possible vendors before forwarding the requisition to the purchasing department. The purchasing department requests bids from vendors using a standard “request for quotation” (RFQ) form. Once the bids are received and a vendor is selected, a purchasing order is prepared and coded with the account number for the originating department, and copies are sent to the vendor, the originating department, and filed in the purchasing department.

Upon receiving the shipment, the receiving department sends a warehouse receipt to purchasing. When the invoice is received, it is audited at the purchasing department who compare it with the purchase order and the warehouse receipt. Once the auditing is complete, the invoice is sent to the accounting department for payment, or returned with an explanation in case of an error. Here is a simplified list of tasks comprising the purchasing system:

$t_1$ : select vendors

$t_2$ : request bids

$t_3$ : prepare purchase order

$t_4$ : receive warehouse receipt

$$
\begin{array}{l l} t _ {5}: & \text {receive invoice} \\ t _ {6}: & \text {audit invoice} \\ t _ {7}: & \text {pay} \end{array}
$$

$t_{3}$ $t_{4}$ , and $t_{5}$ can be combined into a single task $t_{0}$ since their sequence is fixed and not controllable. The vendor selection in a department takes on average 60 minutes of search through vendor files and eliminates 80 percent of all vendors as inappropriate for the item needed. RFQ forms are more complex. They take about 120 minutes to fill, duplicate, and send to the selected vendors. An expected 90 percent of vendors are eliminated through the bidding process since they submit clearly noncompetitive bids or do not respond to the RFQ at all because they are unable to fill the order at this time. Selecting the best vendor, preparing the purchase order, and receiving the corresponding warehouse receipt and the invoice takes approximately 60 minutes on average. Auditing the invoice takes 30 minutes, and an average 10 percent of them are found to be in error and returned. Issuing payment vouchers takes 30 employee minutes (2 employees, 15 minutes each). Using expected time of work as a measure of complexity, and (1-reduction in search space) as a measure of selectivity:

$$
\begin{array}{l} s _ {1} = 0. 2 0 \quad s _ {2} = 0. 1 0 \quad s _ {0} = 1 \quad s _ {6} = 0. 9 0 s _ {7} = 1 \\ c _ {1} = 6 0 \quad c _ {2} = 1 2 0 \quad c _ {0} = 6 0 \quad c _ {6} = 3 0 \quad c _ {7} = 3 0 \end{array}
$$

## Case 1

The dynamic programming formulation returns the sequence $t_{1}, t_{2}, t_{0}, t_{6}, t_{7}$ as the optimum solution with the cost $60 + 24 + 1.2 + 0.6 + 0.5 = 86.3$

## Case 2

Now consider two separate departments executing the identical tasks, except that selecting vendors $(t_{1})$ is specific to each department, since the relevant vendors are different for each department. The dynamic programming formulation of the multi-model problem returns the sequence $t_{2}, t_{1}, t_{0}, t_{6}, t_{7}$ as the optimum sequence in each department with $t_{2}$ shared, corresponding to the centralization of the bidding process. The total cost is $120 + 2 \times (6 + 1.2 + 0.6 + 0.5) = 136.6$ , clearly less than the decentralized bidding solution with the cost $2 \times 86.3 = 172.6$ .

## Case 3

Consider the implementation of departmental vendor databases which largely automates the vendor search process $t_{1}$ , reducing its cost to 30. This reduces the cost of centralized bidding solution of Case2 to $120 + 2 \times (3 + 1.2 + 0.6 + 0.5) = 130.6$ . However the optimum solution using the new parameters is decentralization of the bidding process back to the departments (although the cost of bidding has not changed). The optimum solution in each department is again $t_{1}, t_{2}, t_{0}, t_{6}, t_{7}$ , with the total cost for two departments $2 \times (30 + 24 + 1.2 + 0.6 + 0.5) = 112.6$ , which is clearly less than the cost of centralized bidding solution of case 2 which is now 130.6.

## Case 4

Consider the implementation of EDI technology to link the company with its suppliers, largely automating the request for quotations and the bidding process, reducing its cost to 60. This reduces the cost of the decentralized bidding process of case 3 for the two departments to $2 \times (30 + 12 + 1.2 + 0.6 + 0.5) = 88.6$ .

However, the optimum solution changes again to the centralization of the bidding process. The optimum sequence for each department is again $t_{2}, t_{1}, t_{0}, t_{6}, t_{7}$ , with $t_{2}$ centralized and shared. The total cost for the two departments is $60 + 2 \times (3 + 1.2 + 0.6 + 0.5) = 70.6$ , which is clearly less than the cost of decentralized solution 88.6.

## Conclusions

THERE IS CONSIDERABLE EVIDENCE THAT IT HAS A SIGNIFICANT IMPACT on organizational structure, although the exact nature and characteristics of that impact are not well understood. On the prescriptive side, IT creates significant opportunities for increased efficiency through business process reengineering, although again the precise nature and the direction of reengineering efforts are not well established. The decision model paradigm of organizations provides an effective methodology to describe and quantify the organizational impact of IT, and to direct and specify the appropriate reengineering efforts to maximize the benefits from IT. Decision models provide a simplified analytical model of organizations as decision-making entities, and organizational structure as the arrangement of decision models and the decision tasks comprising them. An analytical model quantifies a variety of organizational issues, including the need for business process reengineering after the introduction of IT, and the exact conditions under which IT may lead to more or less centralized structures. Reoptimization of business processes following the introduction of IT is formulated as a dynamic programming problem and shown to be computationally tractable.

Like all analytical models, the formulation emphasizes some characteristics of tasks that are heavily influenced by IT, but assumes away some other characteristics. Behavioral characteristics such as employee skills, motivation, incentives, and resistance are not part of the mathematical model, although they can significantly affect the feasibility of transition from the current structure to a more efficient structure envisioned by BPR. The emphasis in this paper is on the determination of the efficient structures, but not on the transition strategies from the current state to the more efficient state. Effective transition strategies are left for future work.

A major assumption in the model is the view of organizations as collections of decision models that process information and reduce uncertainty. This information-processing view of organizations has been extensively studied in the literature, and its strengths and weaknesses are well documented. It models information-processing tasks of managers well, but it is less successful in modeling the physical processes of a manufacturing-type environment. These shortcomings also apply here. The approach developed in this paper applies primarily to the information-processing tasks of an organization, where successive tasks reduce uncertainty for the organization and eventually lead to a managerial decision. It is possible to extend the model to physical processes by modeling tasks as reducing “uncertainty” in the nature of a final physical product. However, this is a rather unnatural model, and other process modeling techniques may well be more appropriate for describing physical processes.

## REFERENCES

1. Alexander, C. Notes on the Synthesis of Form. Cambridge, MA: Harvard University Press, 1967.

2. Attewell, P., and Rule, J. Computing and organizations: what we know and what we don't know. Communications of the ACM, 27, 4 (1984), 2184–2192.

3. Barley, S. Technology as an occasion for structuring. Administrative Science Quarterly, 31 (1986), 1–24.

4. Blanning, R. Model management systems: an overview. Decision Support Systems, 9, 1 (1993), 9–18.

5. Blau, P.M.; Falbe, C.M.; McKinley, W.; and Tracy P.K. Technology and organization in manufacturing. Administrative Science Quarterly, 21 (1976), 20–81.

6. Burton, R.M., and Obel, B. Designing Efficient Organizations: Modeling and Experimentation. Amsterdam: Elsevier, 1984.

7. Crowston, K.; Malone, T.W.; and Lin, F. Cognitive science and organization design: a case study in computer conferencing. Human Computer Interaction, 3 (1987), 59–85.

8. Curtis, B.; Kellner, M.I.; and Over, J. Process modeling. Communications of the ACM, 35, 9 (1992), 75–90.

9. Drenick R.F. A Mathematical Organization Theory. Amsterdam: North-Holland, 1986.

10. Gurbaxani, V., and Whang, S. The impact of information systems on organizations and markets. Communications of the ACM, 34, 1 (1991), 233–251.

11. Hackman, J.R., and Oldham, G.R. Work Redesign. New York: Addison Wesley, 1980.

12. Hammer, M. Reengineering work: don't automate, obliterate. Harvard Business Review (July 1990), 104–112.

13. Hammer, M., and Champy, J. Reengineering the Corporation: A Manifesto for Business Revolution. New York: HarperCollins, 1993.

14. Huber, G.P. The nature of organizational decision making and the design of decision support systems. MIS Quarterly, 5, 2 (1981), 1–10.

15. Huber, G.P., and McDaniel, R.R. The decision making paradigm of organization design. Management Science, 32, 5 (1986), 576–589.

16. Jones, D.S. Elementary Information Theory. Oxford: Oxford University Press, 1973.

17. Knight, K.E. Organizations: An Information System Perspective. New York: Wadsworth, 1979.

18. Kocher, M., and Deutsch, K.W. Decentralization by function and location. Management Science, 19 (1973), 841–856.

19. Malone, T.W. Modeling coordination in organizations and markets. Management Science, 33, 10 (1987), 1317–1332.

20. Malone, T.W.; Crowston, K.; Lee, J.; and Pentland, B.T. Tools for inventing organizations: towards a handbook of organizational processes. Proceedings of IEEE Workshop on Enabling Technologies Infrastructure for Collaborative Enterprises, 1993, pp. 620–641.

21. Malone, T.W., and Smith, S.A. Modeling the performance of organizational structures. Operations Research, 36, 3 (1988), 421–436.

22. Mann, F.C., and Williams, L.K. Observations on the dynamics of a change to EDP

equipment. Administrative Science Quarterly, 5 (1960), 217–256.

23. Marcus, M.L., and Robey, D. Information technology and organizational change: causal structure in theory and research. Management Science, 34, 5 (1988), 583–598.

24. Marschak, J., and Radner, R. Economic Theory of Teams. New Haven, CT: Yale University Press, 1972.

25. Mintzberg, H. Structure in Fives: Designing Effective Organizations. Englewood Cliffs, NJ: Prentice-Hall, 1983.

26. Moore, T.C., and Whinston, A.B. A model of decision making with sequential information acquisition. Decision Support Systems, 2, 4 (1986), 289–308.

27. Morgan, G. Images of Organization. New York: Sage, 1986.

28. Orlikowski, W.J. The duality of technology: rethinking the concept of technology in organizations. Organization Science, 3 (1992), 398–427.

29. Orman, L. Information intensive modeling. MIS Quarterly, 11, 1 (1987), 73–84.

30. Orman, L. Information cost as a determinant of system architecture. Information and Software Technology, 36, 3 (1994), 165–172.

31. Osterman, P. The impact of computers on the employment of clerks and managers. Industrial and Labor Relations Review, 39 (1986), 175–186.

32. Ozan, T. Applied Mathematical Programming. New York: Wiley 1985.

33. Panko, R. Is office productivity stagnant? MIS Quarterly, 15, 2 (1991), 2–18.

34. Paulson, D., and Wand, Y. An automated approach to information system decomposition. IEEE Transactions on Software Engineering, 18, 3 (1992), 174–189.

35. Pfeffer, J., and Leblebici, H. Information technology and organization structure. Pacific Sociological Review, 20 (1977), 241–261.

36. Roach, S.S. Services under siege: the restructuring imperative. Harvard Business Review (September 1991), 22–29.

37. Robey, D. Computer information systems and organization structure. Communications of the ACM, 24, 10 (1981), 679–687.

38. Sacco, W. Dynamic Programming. New York: Janson, 1987.

39. Simon, H. Rationality as a process and product of thought. American Economic Review, 68, 2 (1973), 1–16.

40. Tushman, M.L., and Nadler, D.A. Information processing as an integrating concept in organization design. Academy of Management Review, 3, 3 (1978), 613–624.

41. Wand, Y., and Weber, R. On ontological models of an information system. IEEE Transactions on Software Engineering, 16, 11 (1990), 1282–1292.

42. Whisler, T.L. Information Technology and Organizational Change. New York: Wadsworth, 1970.

43. Zuboff, S. New worlds of computer-mediated work. Harvard Business Review, 61 (1983), 142–152.

44. Zviran, M. Relationship between organizational and information system objectives: some empirical evidence. Journal of Management Information Systems, 7, 1 (1990), 65–84.
