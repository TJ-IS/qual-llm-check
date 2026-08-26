---
otero_id: 22320
otero_key: "FY26FZY3"
title: "Determination of an implementation order for IS projects"
authors: "Peretz Shoval; Ran Giladi"
year: "1996"
journal: "Information & Management"
doi: "10.1016/s0378-7206(96)01080-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Determination of an implementation order for IS projects

Peretz Shoval $^{1}$ , Ran Giladi

Information Systems Program, Department of Industrial Engineering and Management, Faculty of Engineering Sciences, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel

## Abstract

The process of information systems (IS) planning in an organization occurs when there is a set of IS projects that require implementation, generally within certain time frames and budgetary constraints. We propose a method for determining an optimal order of project implementation. The proposed method utilizes the cost–benefit graph, which considers the expected cost and benefit of each of the projects comprising the set, as well as the weight (importance) of the cost and benefit factors to the decision-makers. The method allows us to analyze the sensitivity of a preferred implementation order to changes in cost and benefits, and the importance of these factors.

Keywords: Cost–benefit analysis; Cost–benefit graph; Decision-making process; Information systems planning and selection; Project management

## 1. Introduction

Methods of planning, selecting and implementing information systems (IS) require that the organization's strategic plan and goals be translated into an overall scheme or architecture, normally with an attempt to allocate the IS resources across the projects. Some of the better known IS planning methods include IBM's business systems planning (BSP) [7], strategic systems planning (SSP) by Holland Systems Corporation [6], Rockharts' critical success factors (CSF) [10], method/1 by Arthur Anderson [3], McLean and Soden's hierarchical system planning approach [8], and Wetherbe and Davis' end/mean analysis [13]. Some of these deal with the challenging problem of determining the set of IS projects (systems) that require implementation within the planning horizon, but they do not provide structured, optimal solutions to the problem of setting up priorities. In other words, they fail to determine the order of project implementation.

For example, the CSF method is based on factors (SF), which determine the success or failure of the organization. The method involves: definition of the organizational objectives, definition of the SFs and measures for each, and analysis of the existing information systems. These components define the crucial subsystems, their interrelationships, and the information types for each subsystem, but does not determine the order of subsystem implementation. Similarly, McLean and Soden propose a hierarchy of four types of planning: strategic, long-range, medium-range, and short range. In the medium-range, a master plan for IS development is produced; this includes a portfolio, a design of the applications to be developed, and a schedule for hardware and software acquisition. But, again, no systematic method is provided for determining the order of the development. Ein-Dor and Segev [5] have concluded that there is no optimal plan for IS; therefore, the primary objective of planning can only assure that the resulting IS is consistent with the organizational policy.

Due to limited “theoretical” solutions, the implementation order of the IS projects is dictated by practical considerations. In real situations, there are resource constraints usually, which cause the decision-makers to compromise and rank-order the candidate projects according to certain criteria, such as: cost, expected benefit, probability of success or risk of failure, availability and capability of technological and human resources, etc. All these factors can be considered either the cost or benefit.

From a practical point of view, the decision-makers approach the problem of setting priorities in different ways. One approach (used by some authoritative managers) is intuition (“gut” feeling). A simplistic, perhaps shortsighted, approach is to order the projects by their expected costs, from cheap to expensive. This may be adopted when there are tough budget constraints that force the decision-makers to invest as little as possible in computing, or when the decision-makers are skeptical about the “worth” of an information system, and thus, want to spend as little as possible. The drawbacks of such methods are self evident.

The opposite approach is to order the IS projects by their benefits, from most to least beneficial. However, even with relatively unconstrained budgets, cost should not be neglected, because of the risks involved. After all, the more beneficial project is likely to be more costly, and the failure of such a project may have an adverse effect with respect to other IS projects.

Another approach is to order the IS projects by their rate of return on investment (ROI). While this approach considers both the costs and benefits, it requires that the expected benefits of the projects (as well as their costs) be expressed in monetary terms, so that the net present value (NPV) of the cash inflows associated with each project can be computed. As mentioned, the overall benefit of an IS project cannot usually be expressed in this way, so the ROI cannot be determined.

Another method is to order the projects by the cost to benefit ratio, from low to high. This ratio can be applied if the benefits are expressed in a numerical scale - as is usually done. But, it implies that the two factors (cost and benefit) are equally important. This may lead to peculiar decisions. For example, assume two projects: one with an expected cost of \$ 500 000 and expected benefit of 0.9, and another with an expected cost of \$ 250 000 and expected benefit of 0.45. The cost to benefit ratio suggests that the two (certainly entirely different) projects get the same priority, because 500 000/0.9=250 000/0.45.

Mehrez et al. [9] consider both the cost and benefit, and establish a relative ranking of alternative systems in a numerical scale (e.g. 1–5). First, they rank the systems according to their relative costs; second, they rank them according to their relative benefits. (“Benefit” reflects the degree to which the computer-related goals are attained.) Then, weighted scores are calculated by multiplying the score with the weight of cost and benefit. The weights reflect their relative importance according to the judgment of the decision-maker. Hence, the system that has the highest weighted score is selected. This procedure enables the decision-maker to determine the best alternative.

A practical, commonly used approach, which can be viewed as a compromise, is to consider “all the factors” together. This is done by asking the decision-maker to rank-order the set of candidate projects in one scale, by somehow considering both costs and benefits. If several decision-makers are involved (perhaps with conflicting interests), each may be asked to rank-order the candidate projects, and assuming that the lists are not identical, a compromise is sought by “negotiation” or pair-wise comparisons. A variant of this approach is to decide on a certain amount of money that will be allocated for the IS projects during a certain time frame (say a fiscal year), and ask the decision-makers to determine the top priority projects such that their total cost will not exceed that amount.

Two recent studies on IS planning address the issue of systems prioritization in more detail. In their methodology for IS planning and selection among alternative systems, Mehrez et al. deal, among other things, with determining priorities for systems development, so as to allow modular development and facilitate the allocation of resources. In determining priorities, they propose that the following elements be taken into account:

1. The importance of the organizational objectives that the systems help to achieve.

2. The technological means (hardware, software, etc.) required for developing the system.

3. The financial constraints, which dictate the annual rate of development.

4. Other constraints which express the capacity of the organization to incorporate and run the system (e.g. level of expertise, ability to obtain manpower, etc.).

These factors can be viewed as guidelines for determining priorities, but they do not provide a specific ordering scheme.

Agarwal et al. [1] propose a multidimensional methodology for systems prioritization that allows for initial prioritization of systems based on attributes that are mostly qualitative. They claim that in a situation where all aspects of a system are considered simultaneously, there can be a tendency to weight the quantitative or concrete criteria (such as cost) more heavily than the qualitative and abstract criteria (such as strategic objectives). Therefore, they suspect that projects that are financially attractive will be assigned a higher priority than projects that are strategically important. To overcome this problem, they propose a two-step approach: in the first, the systems will be evaluated on “strategic needs”, resulting in a systems portfolio that rank-order projects on mostly qualitative dimension. In the second step, the initial portfolio will have quantitative factors added to arrive at a final (modified) systems portfolio.

Agarwal et al. concentrated on the first step only. The input to their technique is a set of strategic needs identified by the users based on their objectives, or extracted from long term corporate goals. The needs are mapped onto business systems and then rank-ordered according to four qualitative dimensions: strategic, technical, political and philosophical. Each proposed need is scored on a 1–5 scale, and then for each system, a total point score is computed for each dimension. These totals are then used to generate a ranking of the systems. As the authors note, no attempt is made to combine the project ranks of every distinct dimension into one single rank. The decision to combine the ranks into a single one must be the outcome of the subjective tradeoffs among these dimensions. In addition to being highly subjective, another inadequacy of this approach is that it identifies four specific dimensions that are considered critical to the project prioritization, but the authors admit that different dimensions may be implemented for different types of systems. Therefore, they conclude that the rankings must be discussed and a consensus be reached before any final decision can be made on the allocation of resources.

Our solution to the issue of the systems prioritization is based on the cost–benefit graphical (CBG) method, which considers both the expected costs and benefits of the projects, as well as the weight (i.e. importance) of these factors to the decision-maker

## 2. The cost-benefit graph

The cost-benefit graph (CBG) was introduced as a method for selecting a preferred computer system from alternative systems $[12]$ . The graph has two vertical axes that represent the benefits and costs of the alternative systems (IS projects), along with a horizontal axis for the weights scale.

## 2.1. The benefits

The “ideal” measure of benefit is in terms of money, i.e. the profits or savings earned. In the case of IS, however, the benefits are often difficult to measure in monetary terms. Even though some attributes can be measured (e.g. expected revenues or savings), others are measurable only in non-quantitative terms (e.g. the ease of use, satisfaction, reliability of vendor, etc.). Consequently, in order to compute the overall benefit of a system and make quantitative comparisons, all measures of the different attributes must be converted to one common scale: percentage. Having a common measure for the different attributes, numerous multi-attribute decision models can be applied in order to calculate the overall benefit of the system. (See discussion in [2], [4], and [11]). In this study, we are not concerned with the pros and cons of such models. It suffices to say that there are methods that estimate the expected benefit of each IS project and express it in a 0–1 scale or percentage.

Assuming that the benefit of each alternative system is estimated on such a scale, we normalize the benefits of all alternative systems, such that the best system gets the maximum value, 1, and the benefit of any other system, i, equals (benefit $_{i}$ /benefit $_{best}$ ). The resulting normalized benefits are marked on the normalized benefits axis of the graph.

## 2.2. The costs

The cost of a system, similar to the costs of projects in other areas, can be easily measured in monetary values, and there is usually no need to express cost in surrogate terms. Note, however, that since the total cost of a system may be spread over a long period of time, it is important to consider all types of costs and express them in present value terms. The next step is to normalize the cost values of the alternative systems, i.e. to transform them onto the same scale, such that a costly alternative is low and a less costly one high, in the scale. There are many methods of making this transformation. We adopt a linear transformation, according to which, the normalized cost of the least costly system gets the maximum value, 1, and the normalized cost of any other project, i, decreases proportionally, i.e. ( $cost_{min}/cost_{i}$ ). This transformation method maps the cost values onto a scale that is equivalent to the normalized benefits scale. In other words, the maximum values of both are 1, and the less beneficial projects, or more costly ones, decrease proportionally.

## 2.3. The weights

The horizontal axis of the graph is the weights scale, expressing the relative importance of the benefit and cost factors. The weights range 0–1; at the intersection point with the benefit axis, the weight of benefit (p) is 1 and that of the cost factor is 0. Similarly, at the intersection point with the cost axis, the weight of cost (1−p) is 1 and that of benefit is 0, etc. The line that connects the (normalized) benefit and cost values of each alternative system signifies its expected benefit at any given point on the weights axis. The lines of alternative systems intersect, and the upper cover of the lines (i.e. the highest possible points of all lines) signifies the best alternative at any point on the weights (horizontal) axis.

Table 1 and Figure 1 exemplify the cost–benefit graph. The table shows the costs and benefits of three alternative systems (projects), A, B and C. Nominal costs are given in thousands of dollars, and nominal benefits are expressed in a 0–1 scale. The next two columns show the normalized costs and benefits. Costs are normalized as follows. The cost of B, the least costly project, is transformed to 1, and the cost of any other project is transformed by dividing 400 by its nominal cost. Benefits are normalized as follows. The benefit of A, the most beneficial project, is transformed to 1, and the benefit of any other project is transformed by dividing its nominal benefit by 0.9.

Table 1  
Cost and benefit of three projects

<table><tr><td>Project code</td><td>Nominal cost (K$)</td><td>Nominal benefit</td><td>Normalized cost</td><td>Normalized benefit</td></tr><tr><td>A</td><td>700</td><td>0.9</td><td>0.571</td><td>1.000</td></tr><tr><td>B</td><td>400</td><td>0.5</td><td>1.000</td><td>0.556</td></tr><tr><td>C</td><td>500</td><td>0.8</td><td>0.800</td><td>0.889</td></tr></table>

Equations of lines(projects) A and C at point p: $1.0 \times p + 0.571 \times (1 - p) = 0.889 \times p + 0.8 \times (1 - p) \Rightarrow \mathrm{p}(\mathrm{A}/\mathrm{C}) = 0.674$ Equations of lines(projects) B and C at point q: $0.556 \times q + 1.0 \times (1 - q) = 0.889 \times q + 0.8 \times (1 - q) \Rightarrow q(\mathrm{B}/\mathrm{C}) = 0.375$

![](/api/attachments/FY26FZY3/fulltext/images/4b529247878c9968f3a94587fadeda0b8ef61611dc46d47614a8b78b0ad2292a.jpg)  
Fig. 1. Cost-benefit graph for three projects.

Figure 1 shows the lines of the three projects. The upper cover of the lines is of interest; if the weight of benefit is above 0.674 (where the lines of projects A and C intersect), project A will be selected; if the weight of benefit is less than 0.375 (where the lines of projects B and C intersect), project B will be selected; and if the weight of benefit lies within these two values, project C will be selected. The equations at the bottom of Table 1 show how the P-values at the relevant points of intersection are calculated.

The advantage of the graphical cost-benefit method is that it enables the decision-maker to decide on an optimal alternative while taking into consideration the weights of the cost and benefit factors. Hence, the decision is no longer deterministic, because the method is sensitive to what is important to the decision-maker. Moreover, the graphical method permits the decision-maker to see the level of confidence at which the decision is made. The decision-maker is able to see the optimal alternative for any point on the weights axis, and closeness of the next-best alternative, depending on the points where the lines of the optimal and next-best alternatives intersect.

The CBG method is widely used for the selection of a system from a set of alternatives. The method is taught to IS students (at least in Israeli universities) in systems analysis and project management courses. It is utilized in IS bids, being a part of a government standard for IS projects. Moreover, there is at least one commercial DSS tool that utilizes the method. It can be easily implemented using any spreadsheet software (like Excel or Lotus)

## 3. Utilizing CBG to determine priorities of IS projects

In this section, we show how the CBG method can help determine the order of IS projects implementation. Assume a given set of projects requiring implementation. These projects may have been defined as a part of a master plan for IS development. We assume that each project is independent, i.e. its implementation does not depend on other projects. Otherwise, dependent projects must be treated as one. The cost–benefit graph is applied as follows.

To explain how the graph can be utilized to determine the order of project implementation, we use an example from a university. Each project in the set has a pair of values for its cost and benefit. Assume that the IS long-range planning committee identified six IS projects that need to be implemented. For each, the planning committee estimated its expected cost (in thousands of \$) and benefit (in a 0–1 scale). The six projects were: student records and academic status (A); research contracts (B); personnel management (C); construction and maintenance (D); inventory and suppliers (E); and finance and accounting (F). Table 2 shows the nominal and normalized costs and benefits of the projects, and Figure 2 shows the respective cost–benefit graph.

Table 2  
Cost and benefit of six projects

<table><tr><td>Project code</td><td>Nominal cost (K$)</td><td>Nominal benefit</td><td>Normalized cost</td><td>Normalized benefit</td></tr><tr><td>A</td><td>700</td><td>0.9</td><td>0.571</td><td>1.000</td></tr><tr><td>B</td><td>400</td><td>0.5</td><td>1.000</td><td>0.556</td></tr><tr><td>C</td><td>500</td><td>0.8</td><td>0.800</td><td>0.889</td></tr><tr><td>D</td><td>500</td><td>0.6</td><td>0.800</td><td>0.667</td></tr><tr><td>E</td><td>600</td><td>0.7</td><td>0.667</td><td>0.778</td></tr><tr><td>F</td><td>900</td><td>0.8</td><td>0.444</td><td>0.889</td></tr></table>

![](/api/attachments/FY26FZY3/fulltext/images/2e9f583dfe848d7f69c80796c9d014101220516439237078c77995a51c037fa9.jpg)  
Fig. 2. Cost-benefit graph for six projects.

The objective is to decide on the optimal implementation order of all the projects. To do so, the decision-maker first must determine the weight of the cost and benefit factors, i.e. the relative importance of cost and benefit factors to the organization. Then, from the selected point on the weights axis, we draw a vertex that intersects with the lines representing the projects. The intersection points determine the order or priorities of the projects, such that the highest (upper) point indicates the top priority project, etc. Hence, the priority is determined according to the expected values of the projects for the given weights of the cost and benefit factors. Let us assume in our example that the weight of benefits is p=0.8 (80%). As Figure 2 shows, the order of the system implementation is: A, C, F, E, D, B.

Table 3

Note that in an extreme case, when the decision-maker considers benefit (quality) only, i.e. when the weight of benefit equals 1, the priority of the projects is based on benefits only; then project A is first, projects C and F are second, etc. in order. At the other extreme, when there are severe budgetary constraints and only the cost counts, project B is first in order, and projects C and F tie for the second, etc.

We can see that at points that are “close” to the extremes, the priorities do not change. For example, at a weight of benefit, p=0.75 (and cost=0.25), the priorities are still the same as those for the extreme case, where p=1. Similarly, at p=0.25 (and cost=0.75), the priorities are still the same as those for the extreme case, where p=0. Generally, the order of the projects would change when the lines of any two projects intersect, signifying a shift in their priority only. For example, the lines of projects A and C intersect when p=0.676 (p is calculated as follows: $1 \times p + 0.571 \times (1 - p) = 0.889 \times p + 0.8 \times (1 - p)$ .) It means that if the decision-maker determines that the weight of benefit is less than 0.676, project C gains top priority, and project A becomes second in priority. Similarly, the lines of projects A and E intersect at p=0.302, meaning that when the weight of benefit is higher than this figure, project A gains priority over project E, but when the weight of benefit is lower, project E is prior to A.

When the decision-maker sets the weights of cost and benefit, such that the vertex passes close to an intersection between the two, the order of the projects becomes almost immaterial. When the vertex does not pass close to an intersection point, it indicates a definite order. Hence, the graph shows the sensitivity of project ordering to the weights of cost and benefit as determined by the decision-maker. Sometimes, the decision-maker cannot decide upon the exact weighting of benefit and cost, and prefers to specify a range of weights. The graph shows if there is any shift in the priorities within that range, and tells the decision-maker how confident he or she can be about the ordering.

Due to the fact that the CBG method is supported by a software tool (or a spreadsheet, like Excel and Lotus), the graph can show the sensitivity of project ordering to changes in the expected cost or benefit of individual projects. Any change is immediately reflected on the graph.

## 3.1. Change in ordering over time

The CBG determines a priori, the order of implementation of a given set of projects. At the beginning, the top project, or several projects, are implemented depending on the budget available. The rest of the projects are “made to wait” for implementation, until the budget allows. The order of implementation of the remaining projects may change with time due to the changes in weights (importance) of benefits and costs. The order of the remaining projects may then change accordingly. But, even if the weights of benefit and cost do not change, it is still possible that the order of the remaining projects will change, because the next decision depends on the relative costs and benefits, after the first has been removed from the list.

As an example, let us assume that the top two priority projects, A and C, have now been implemented, and the decision-maker must now consider further investment in IS projects. At this stage, the original graph is no longer relevant; projects A and C are removed from the list. We do not have to re-normalize the costs of the remaining four projects, because (in this example) the least costly project, B, has not been implemented (removed) yet, but we have to re-normalize the benefits, because the most beneficial project, A, is no longer on the list. The most beneficial project among the remaining four is F, and so its benefit is normalized to 1. The revised data are shown in Table 3, and the corresponding graph is shown in Figure 3. The ordering of the remaining 4 projects depends (as before) on the weights of benefit and cost, which may or may not change. Assuming the same weights as previously (i.e. p=0.8), the order of the four projects is: F, E, D, B (with no change compared to the original order).

Cost and benefit of four projects (projects A and C done)

<table><tr><td>Project code</td><td>Nominal cost (K$)</td><td>Nominal benefit</td><td>Normalized cost</td><td>Normalized benefit</td></tr><tr><td>A</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>B</td><td>400</td><td>0.5</td><td>1.000</td><td>0.625</td></tr><tr><td>C</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>500</td><td>0.6</td><td>0.800</td><td>0.750</td></tr><tr><td>E</td><td>600</td><td>0.7</td><td>0.667</td><td>0.875</td></tr><tr><td>F</td><td>900</td><td>0.8</td><td>0.444</td><td>1.000</td></tr></table>

![](/api/attachments/FY26FZY3/fulltext/images/e1a5d9867ede9ed85dac76cbf90dcece66b521a750404166c8f4386bb96e5caf.jpg)  
Fig. 3. Cost–benefit graph for four projects.

So far, we assumed no change in the set of projects; i.e. the same projects with the same expected costs and benefits remain intact. But, as time passes, both the expected costs and benefits of the existing projects may change, and new projects may be added. Consequently, a new graph must be constructed that will include all these changes. We learn from this that the graph determines the ordering of projects in a single decision-making process, i.e. in one “cycle” of decision-making. If all the projects cannot be implemented (due to budgetary constraints), a revised graph must be constructed in the next decision-making cycle, taking into account the set of IS projects at that time.

## 4. Selecting a subset of projects, given limited budgets

The cost–benefit graph guides the decision-maker to the optimal order of project implementation, but the actual implementation depends on the actual budgets. A limited budget may inhibit implementation according to the recommended order. Assume, for example, that the top priority project costs more than that the budget allows. The solution is to implement the next best project in the ordered list, and retain the first project, as well as the rest, for the next iteration when more budget becomes available. Note again that in the next iteration, the whole graph will have to be revised; hence, it is not guaranteed that the previously defined top projects will remain on the top of the revised list.

Another possibility occurs when the given budget allows implementation of more than one project, but not necessarily in the optimal order. Obviously, the top project(s) should be selected from the ordered list, but first, the costs of those projects must be estimated, and compared with the total budget. If a project is encountered whose cost exceeds the remaining budget (after allocation of the required sums to the previous projects), we must skip onto the next project on the list provided that it costs less than the remaining budget, etc. Consequently, because of the budgetary constraint, we may end up implementing projects not necessarily in the optimal order.

![](/api/attachments/FY26FZY3/fulltext/images/db4fbfb11b5a68c77c0c18cdf24ea4f4c745919f7a5fe3568ecdac225fe64964.jpg)  
Fig. 4. Optimal IS project vs. budget.

This is exemplified in Figure 4, which represents ordering of the above six projects. The horizontal axis of the graph represents the available budget, and the bars signify the projects that can be implemented for a given budget. Assume that the decision-maker specifies the weight of benefit p as 0.8 (and that of cost as 0.2). For this value of p, the optimal order of implementation of the six projects, as we have shown, is: A, C, F, E, D, B. Assume that the total budget allocated for the IS projects is 2000 (in thousands of \$). The cost of the two top projects, A and C, equals \$1200. Since cost of F, the next project in the list, exceeds the remaining budget, we skip onto the next best project, E, that costs only \$600. Note that all the projects will be implemented at one go only if the available budget is \$3600, whereas, if the budget is limited, say \$450, only one project, which in this example happens to be last in the ordered list, will be implemented because it is based on a relatively high weight of the benefit factor.

## 5. Summary

We proposed a graph-based method to determine the optimal order implementation of a given set of IS projects. The method considered the expected costs and benefits of the IS projects, as well as the weights (importances) of these factors to the decision-makers. We made several assumptions, which in reality, are not always met: first, we assumed that there is a master plan that defines a close set of IS projects; second, we assumed that the costs and benefits of the projects can be forecasted; third, the projects are independent, and if not, we treated the dependent projects as one project, for which a combined set of costs and benefits is computed. We have seen that if the total budget allocated for the IS project is restricted, the actual order of implementation is not necessarily optimal, but is as close as possible to the optimum. We have also seen that the graph-based method proposes an ordered list, which is good for one decision-making cycle. If all the projects cannot be implemented in that cycle (due to a constrained budget), there may be changes in the remaining projects, new projects next time, and different weights of the cost and benefit factors; hence, a new optimal order may be proposed – what was initially important may have less relevance another time.

## References

[1] Agarwal, R., Roberge, L. and Tannniru, M., “MIS planning: a methodology for systems prioritization”, Information and Management 27, 1994, 261–274.

[2] Green, P. and Tull, D., Research for Marketing Decisions, Fourth Edition, Prentice Hall, New Jersey, 1987.

[3] Arthur Anderson and Co., Method/1: An Information Systems Methodology, Subject File AA4665, Item 57 (1982).

[4] Dror, M., Shoval, P. and Yelin, A., “Multi-Objective Linear Programming”, Decision Support Systems 7, 1991, 221–232.

[5] Ein-Dor, P. and Segev, E., “Strategic Planning for Management Information Systems”, Management Science 24, 1978, 1631–1641.

[6] Holland Systems Corporation, Strategic Systems Planning, MD154-0486, Ann Arbor, Michigan, 1986.

[7] IBM, Business System Planning - Information Systems Planning Guide, IBM GE20-0527-2, White Plains, New York, 1978.

[8] McLean, E.R. and Soden, J., Strategic Planning for MIS, John Wiley, New York, 1977.

[9] Mehrez, A., Howard, G., Lugasi, Y. and Shoval, P., "Information System Planning and Selection: A Multi-

Attribute Theoretic Approach", The Computer Journal 36(6), 1993, 525–541.

[10] Rockart, J.F., “Chief Executives Define Their Own Data Needs”, Harvard Business Review, March–April 1979, 215-229.

[11] Shoval, P. and Lugasi, Y., “Models for Computer Systems Evaluation and Selection”, Information and Management 12, 1987, 117–129.

[12] Shoval, P. and Lugasi, Y., “Computer Systems Selection: The Graphical Cost-Benefit Approach”, Information and Management 15, 1988, 163–172.

[13] Wetherbe, J. C. and Davis, G. B., Strategic Planning Through End/Means Analysis, Working Paper, MIS Research Center, University of Minnesota, 1982.

![](/api/attachments/FY26FZY3/fulltext/images/f0642b749c4b114d0a0fcbbeed37011432cd2b6da8111824a8f9b31631ac17ad.jpg)

Peretz Shoval is a Professor of Information Systems Engineering at the Ben-Gurion University, Israel. He earned his Ph.D. in Information Systems (1981) from the University of Pittsburgh, where he specialized in expert systems for information retrieval. In 1984 he joined the Dept. of Industrial Engineering and Management at the Ben-Gurion University, where he started and is head of the Information Systems Engineering

program. Prior to moving to academia, he held professional and managerial positions in computer companies and in the IDF. Shoval's research interests include database design, information systems analysis and design methods, economics of information systems, and information retrieval. He has published numerous papers in scientific journals. Shoval is the developer of the ADISSA methodology and tools for systems analysis and design, and also of ADDS system for conceptual and logical database design.

![](/api/attachments/FY26FZY3/fulltext/images/80ff9210066448ef6da80f56f8144a29e92654b3f4e799d19ac20fb4324583c7.jpg)

Ran Giladi is the Head of the Department of Communication Systems Engineering, and Lecturer of Information Systems at the Department of Information Systems and Management, Ben-Gurion University of the Negev, Israel. He earned B.A. in Physics (1980) and M.Sc. in Biomedical-Engineering (1983), both from the Technion -Israel Institute of Technology, and Ph.D. in Management Information Systems from Tel-Aviv University (1992). Prior

to moving to academia, he was co-founder of a multinational data communications firm. Giladi is involved in the Israeli data and telecommunications systems. His research interests include computer and communication systems performance, data networks and communications, and network management systems.
