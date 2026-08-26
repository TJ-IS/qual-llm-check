---
otero_id: 19052
otero_key: "R8HQE8CR"
title: "Decision support for “messy” problems"
authors: "Christian Wagner"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00052-k"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Briefing

# Decision support for “messy” problems

Christian Wagner

Department of Information and Operations Management, School of Business Administration, University of Southern California, Los Angeles, CA 90089-1421, USA

## Abstract

Problems that are non-quantitative and not bound to a narrow knowledge domain have been served unsatisfactorily by decision support and expert systems. Alternative techniques that address this type of problem are explained here using two key concepts: problem type dependent process support and domain related knowledge. Process support refers to the program steps and the data items useful in finding the solution. Domain related knowledge is knowledge drawn from a specific domain, yet through abstraction applicable to a wider range of problems. Results of preliminary empirical analyses suggest that both concepts are useful.

Keywords: Decision support system; Domain knowledge; Expertise; Expert system; Problem solving; Problem structure

## 1. Background and overview

Previously the application of information technology to individual decision support typically meant the use of decision support systems (DSS) for a variety of ad hoc numerical problems or the use of expert systems (ES) for symbolic problems in a well defined problem domain. The value of DSS results primarily from the suite of algorithmic and data presentation techniques that it provides for a wide variety of quantitative problems, the value of ES stems from their considerable reasoning capability in a small domain (see for instance [11]). Problems that were not amenable to quantitative solution methods or whose domain was too wide to be captured with ES technology were generally ignored.

This article describes key mechanisms of an alternative type of DSS which helps with these “messy”, wide-and-open, non-quantitative problems. The argument will focus on the conceptual design ideas underlying problem type specific support and domain related knowledge. Implementation examples and pilot evaluations are included to document the feasibility and value of the concepts.

## 2. Messy problems: nature and examples

At all levels of the firm, from operational to strategic, decision makers face “messy” problems. For example, a marketing manager will have to determine why a proven marketing strategy suddenly fails to produce an increase in sales, or an operations manager may have to come up with new ideas on how to cope with insufficient inventory capacity. These problems are semi-structured or unstructured and non-routine (compare [18]). They may consist of multiple, interlinked problems, as illustrated in [1]. They require domain knowledge, innovative thinking and general problem solving skills. Furthermore, these problems are not generally amenable, at least in the early phases of the search for a solution, to a quantitative formulation, thus complicating any possible computer support.

The lack of problem structure can manifest itself in several ways. The true cause of a problem or the means to determine the true cause may not be known. For example, an accounts manager may be faced with an increase in the age of accounts and more bad credits. The cause of this problem may be routine; e.g., a downturn in the economy has eroded payment behaviour. However, in order to make a quick and easy sale, company sales representatives may have targeted firms in poor financial condition. The accounts manager will probably have seen the former but not the latter case. Routine problems can be resolved via a search through the set of known causes (convergent thinking) and this type of situation is well suited for diagnosis with ES. In contrast, the solution of unknown problems requires innovative (divergent) thinking. This type of reasoning is not one where computer software has excelled.

In design tasks, a lack of structure will be indicated by an incompletely defined end state (goal) or initial state, and a lack of specific rules to move from the initial to the end state. A typical messy problem of this type is new product development, such as that for new automobiles. Particularly the early stage of the effort, generation of new product concepts, is difficult, as the product developer has to come up with ideas that are innovative (new to the market), useful (of value to customers) and feasible (e.g., can be produced cost effectively). This type of problem requires extensive domain knowledge, such as customer needs, existing products, and their features. Since there is no sure-fire formula for success in the generation of new ideas, product developers have to rely on general problem solving concepts, as for instance “incremental improvement” of an existing idea. To further complicate the situation, a significant portion of the effort requires non-quantitative strategies.

## 3. Solving messy problems: previous directions

Messy problems have characteristics that make it difficult to improve the performance of decision makers faced with them or to furnish computer based decision support. Despite this difficulty, there have been multiple attempts to address this problem set at least partially, either with software or without. One major direction has been the study of expert problem solver behaviour in an attempt to extract generally applicable solution finding principles. After all, experts exhibit significant skills even on problems for which their domain knowledge is limited. For instance, their performance is still reasonable at the fringes of their domain knowledge (see [29]). Furthermore, a comparison of expert problem solving behaviour independent of domain shows very similar behaviour, such as breadth-first reasoning [27], analogical reasoning [17,25], or skilled questioning [10]. Even in an unfamiliar problem area, such an individual, in association with someone who knows that domain (but not necessary how to attack the problem), should be able to exhibit successful problem solving behaviour. This approach has been advocated by individuals interested in problem solving per se, as well as by computer scientists, resulting in both paper-and-pencil oriented and computerized techniques. The common element is that they provide heuristics to guide the solution finding process.

The techniques rely on the human problem solver to “make sense” of the problem but supply structure and new directions to approach it. For example, the problem solver is given checklists to ask the “right” questions (e.g., [21,23]), techniques to form analogies between the current situation and an alternate one that may suggest solutions [9], or techniques to recombine known problem elements in new ways, in order to suggest solutions [3]. Many of these techniques have been known for decades, yet their implementation into computer tools, sometimes called idea processing systems, has taken much longer (e.g., [7,16,22,30]). Furthermore, the software packages frequently lack problem specificity and are free of domain knowledge and thus may seem to contribute little to the solution finding process. Tests regarding their usefulness have been inconclusive (e.g., [5,6]). In light of these findings, a more promising direction, although yet without much empirical support, is the development of techniques for specific tasks. For example, a software package may contain question sets targeted at specific problem solving tasks [26].

Artificial intelligence (AI) research has striven to design computer programs that apply a set of general heuristics to a variety of problems. These programs contained an internal representation of the selected problems and were able to find solutions independently, using problem decomposition, “hill climbing,” and other general rules. However, the problems were small and simple and better characterized as puzzles than as messy problems $[19,12]$ . Since then, several attempts have been made to provide additional general problem solving capability (e.g., $[24]$ ). One notable approach is the development of automated discovery systems (e.g., $[14]$ ). The results of this research direction have been impressive, such as the detection or re-discovery of scientific laws $[28]$ . However, even these programs require an internal, machine processable representation of the problem, thus again limiting their use to narrow domains and not to the problem type described earlier as messy.

A different AI research direction originates from efforts to classify knowledge about the world. These classifications or ontologies arrange knowledge about the world or relevant subsets thereof into (ideally) mutually exclusive and collectively exhaustive categories and sub-categories (e.g., [8,4,15]). Ontologies can provide the knowledge base for naive machine reasoning capability. In fault diagnosis or similar problems, ontologies can support an approximate reasoning process and thus, for instance, assist in case based reasoning. Searching through a categorization of system components and related problem causes, a reasoning mechanism can select cases most closely fitting the problem at hand. A human problem solver can later draw on this information to deal with the problem at hand [13,20], tailoring the system's generic solutions to the specific problem. While software of this kind contains more reasoning capability than idea processing systems, most of the reasoning and interpretation effort is again left to the human problem solver.

In summary, independent reasoning capability requires a significant internal problem representation and is limited largely to convergent reasoning. Yet messy problems which are wide and open in scope and not clearly defined do not fit these requirements. Thus, the more promising way to address messy problems appears to be a human-computer interaction with significant reliance on the human's reasoning capability. This model of computer support will be adopted here. We will first discuss the development of an idea processing system that relies little on domain knowledge, but is designed for a specific type of problem containing relevant process knowledge. Thereafter, we explain the gathering and application of high level, commonsense knowledge, drawn from categorized solution ideas, that can further improve the problem solving support capability of such software. While one method focuses on the problem solving process, the other one targets the problem domain at a high level of abstraction. Empirical evidence indicates that each of them is useful by itself. Combined they are expected to result in even higher levels of problem solving performance.

## 4. Problem type specific decision support

## 4.1. General concept

Following the assumption that problem solving expertise can exist independent of domain, the research project allocates some general problem solving knowledge within a computer program. The computer's role is to process knowledge concerning the sequence of steps to carry out, questions to ask, and data to store, yet relying on a person to supply rules and facts about the domain and to "make sense" of the results. To build software for this purpose, one has to study common problem solving methods for the chosen problem type and implement them, while ignoring any domain references. Specifically, the software has to incorporate knowledge of procedural steps, of the questions to ask, and of the data objects to collect, store, transform, and display. Equipped with these capabilities, the software can coach the user on problem formulation and solution finding, can provide stimuli for any brainstorming processes, and can serve as a record keeping tool.

## 4.2. Implementation

The software created for this purpose contains mechanisms to prompt the decision maker for the relevant elements of the problem definition. It also contains techniques that stimulate the user with previously recorded elements of the problem formulation to prompt for new ideas. The software's key contribution to the process is therefore its ability to ask questions that result in a useful problem formulation and that trigger new solution alternatives. Data elements are stored in a database that also retains associations the user made between these elements. The basic architecture of this software is comparable to those described in [16] and [30].

The program is domain-independent. A somewhat domain dependent version has also been developed; it trades off domain independence for the ability to generate associations between problem facts and system knowledge. For example, the program has stored hundreds of themes and associations between different concepts; one specific version that is geared toward automobile innovation makes associations between the concepts leather, luxury and durability. When prompted with the feature leather seats, the program then replies with luxury and durability as benefits.

## 4.3. Evidence of usefulness

To determine software effectiveness and domain independence, two rounds of empirical testing were undertaken. Responses to both studies were evaluated in terms of quantity and quality; the latter was measured by two raters via the criteria novelty (originality), relevance (applicability to the task, fulfilment of needs), and implementability (ease/difficulty of implementing the idea). Quality was measured for both products and product features. Quality ratings from -1 (worst) to +1 (best) were assigned and later aggregated. Ideas were considered good, if they exceeded a zero score in all three individual categories. In both studies, subjects were rewarded for their participation and appeared to be highly motivated.

Study 1 required subjects to think of new product/service ideas for the banking industry, in an attempt to determine yield differences for different idea generation mechanisms. The subjects were 34 MBA students (more than five years average work experience; 8 females), divided into four groups and instructed to use one of four techniques: Group 1 was told to think of benefits for the customer, and then to envision new banking products that would achieve the benefits. Group 2 focused on feature based ideas; Group 3 produced benefit based ideas. Group 4, the control, did not use any pre-described mechanism, and thus had to generate ideas in free-form. The Appendix contains the contents of the instruction and work sheets. Study findings are summarized in Table 1. Subjects who used theme based or product based idea generation appeared to generate the best results, generating the highest ratings on quantity and quality. Both were significantly more effective (t-test statistic) than feature based idea generation (p = .05, number of ideas) product based idea generation was also significantly better than the no-stimulus alternative (p = .05, number of good ideas).

Table 1  
Impact of idea generation mechanisms - Banking products

<table><tr><td rowspan="4">Mechanism</td><td rowspan="4">Mean no. of ideas</td><td rowspan="4">Mean no. of good ideas</td><td colspan="12">Comparison between methods (t-statistic)</td></tr><tr><td colspan="4">Feature</td><td colspan="4">Product</td><td colspan="4">No stimulus</td></tr><tr><td colspan="2">yn ideas</td><td colspan="2"># good</td><td colspan="2"># ideas</td><td colspan="2"># good</td><td colspan="2"># ideas</td><td colspan="2"># good</td></tr><tr><td>t</td><td>p</td><td>t</td><td>p</td><td>t</td><td>p</td><td>t</td><td>p</td><td>t</td><td>p</td><td>t</td><td>p</td></tr><tr><td>Theme</td><td>7.88</td><td>2.25</td><td>2.14</td><td>0.05</td><td>1.81</td><td>0.99</td><td>-0.87</td><td>0.40</td><td>-1.23</td><td></td><td>0.80</td><td>0.44</td><td>1.44</td><td>0.17</td></tr><tr><td>Feature</td><td>5.25</td><td>1.25</td><td></td><td></td><td></td><td></td><td>-2.28</td><td>0.05</td><td>-2.53</td><td>0.03</td><td>-0.85</td><td>0.41</td><td>-0.37</td><td>0.72</td></tr><tr><td>Product</td><td>9.62</td><td>3.25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.39</td><td>0.19</td><td>2.27</td><td>0.05</td></tr><tr><td>No stimulus</td><td>6.56</td><td>1.44</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Study 2 consisted of five in-depth interviews on automobile design ideas, followed by software based idea generation sessions. The purpose was to find out whether the structured software based method would be more successful than an interviewing procedure that did not use the formal process mechanisms. The five interviewees were professionals (college graduates, between 25 and 35 years of age, three males). In the first round of interviews, subjects responded in free form, with some “teaser” questions from the interviewer, if necessary (e.g., “did you buy a car lately? What did you buy? What made you choose this car?”). About two weeks after the verbal interviews, subjects worked again on the same task, this time with the computerized problem formulation and idea generation mechanisms, and without access to any of their earlier written responses. The outcomes of both rounds (number of ideas by mechanism and subject) are shown in Table 2. All subjects created more ideas with the software than without (t-test, p = .04), particularly features and benefits.

## 5. Discussion

The two small experiments jointly provide some evidence for domain independence and usefulness of the techniques. Method driven idea generation resulted in higher yields than free-form idea generation. In the banking study, free-form (no-stimulus) idea generation had one of the lowest yields, both in quantity and quality. In the car design experiment, free-form interviewing resulted in significantly less ideas than our software implementation. Thus, in both domains, a significant yield increase was achieved. Furthermore, software can be used as a process structuring tool. The car design study showed significant increases in the number of ideas, specifically on features and benefits. Thus, even without domain knowledge, software can help the user by implementing the process and eliciting and capturing user inputs.

## 6. Problem solution hierarchies and domain related knowledge

## 6.1. Overview

Process outcome can be improved without domain knowledge. Nevertheless, domain knowledge can lead to better results, given the experiences with expert systems. Yet domain knowledge is difficult to capture when the domain is large or frequently changing. The approach suggested here is the collection and representation of domain related knowledge. Domain related knowledge is knowledge that has been abstracted from specific problems. As such, it requires user intervention to become applicable to specific problems. However, due to its level of abstraction it is relevant for a wider problem set. For example, a rule of domain knowledge would state (in transcribed form) “increase sales to customers through discount pricing.” In contrast, a similar rule in domain related knowledge might state “capture interest through incentives”. The “capture interest” loosely matches the “increase sales to customers”, while “incentives” is a generalization of “discount pricing”. The lack of specificity of the second rule makes it applicable to multiple domains. For example, one may consider it as advice in such diverse areas as public speaking, advertising, or training of one’s pet.

Table 2  
Impact of product development software: Comparison of numbers of ideas

<table><tr><td rowspan="2"></td><td colspan="2">Theme</td><td colspan="2">Feature</td><td colspan="2">Product</td><td colspan="2">Benefit</td><td colspan="2">Total</td></tr><tr><td>verbal</td><td>software</td><td>verbal</td><td>software</td><td>verbal</td><td>software</td><td>verbal</td><td>software</td><td>verbal</td><td>software</td></tr><tr><td>Subject 1</td><td>6</td><td>4</td><td>17</td><td>16</td><td>8</td><td>7</td><td>3</td><td>29</td><td>34</td><td>56</td></tr><tr><td>Subject 2</td><td>6</td><td>8</td><td>5</td><td>12</td><td>7</td><td>9</td><td>6</td><td>56</td><td>24</td><td>85</td></tr><tr><td>Subject 3</td><td>8</td><td>5</td><td>18</td><td>20</td><td>11</td><td>6</td><td>6</td><td>13</td><td>43</td><td>44</td></tr><tr><td>Subject 4</td><td>6</td><td>7</td><td>11</td><td>53</td><td>9</td><td>1</td><td>4</td><td>31</td><td>30</td><td>92</td></tr><tr><td>Subject 5</td><td>3</td><td>5</td><td>5</td><td>12</td><td>16</td><td>5</td><td>3</td><td>21</td><td>27</td><td>43</td></tr></table>

t - 2.99  
p 0.04  
Significance: between subject comparison.  
dF 4

<table><tr><td colspan="3">All Improvements</td></tr><tr><td rowspan="4"></td><td colspan="2">Flight Operation</td></tr><tr><td colspan="2">Plane Size AdjustmentCargo/Passenger Space RedistributionFlight Volume Reduction</td></tr><tr><td></td><td>Cancel Empty FlightsTotal Flight Volume Reduction</td></tr><tr><td colspan="2">Planned Flight Delays</td></tr><tr><td rowspan="7"></td><td colspan="2">Reservation Policy</td></tr><tr><td colspan="2">Booking</td></tr><tr><td></td><td>OverbookingStandby TicketsCharter FlightsConfirmation RequirementReservation as a Privilege</td></tr><tr><td colspan="2">Monitoring</td></tr><tr><td></td><td>Check for Multiple BookingsCheck for Noshow HistoryKeep Noshow Blacklist</td></tr><tr><td colspan="2">Cancellation</td></tr><tr><td></td><td>Simplify CancellationsVoid Reservations</td></tr><tr><td rowspan="15"></td><td colspan="2">Behavior Change</td></tr><tr><td colspan="2">Agents</td></tr><tr><td></td><td>Shift Noshow Risk to Agents</td></tr><tr><td colspan="2">Passengers</td></tr><tr><td></td><td>Incentives</td></tr><tr><td></td><td></td></tr><tr><td></td><td>MonetaryNon-monetary</td></tr><tr><td></td><td>Disincentives</td></tr><tr><td></td><td>MonetaryNon-monetary</td></tr><tr><td></td><td>Mixed Incentives Disincentives</td></tr><tr><td></td><td>MonetaryNon-monetary</td></tr><tr><td></td><td>Advertising</td></tr><tr><td></td><td>Explain Impact of NoshowsDiscourage Reservations</td></tr><tr><td></td><td>Physical Action</td></tr><tr><td></td><td>Force Customers on PlaneCustomer Pick-up</td></tr><tr><td rowspan="3"></td><td colspan="2">Marketing</td></tr><tr><td colspan="2">Raise Airline Attractiveness</td></tr><tr><td></td><td>Change Prices</td></tr><tr><td rowspan="5"></td><td colspan="2">Airline Management</td></tr><tr><td colspan="2">Organizational Change</td></tr><tr><td></td><td>Downsizing</td></tr><tr><td></td><td>Reduce Staff</td></tr><tr><td></td><td>Merger</td></tr></table>

Fig. 1. Hierarchy of solutions to the airline noshow problem.

## 6.2. Knowledge elicitation: creation of hierarchies

When individuals or groups try to solve a problem, the result is typically a pool of ideas. These can be grouped in ontological form based on topical similarity. For example, if the problem is to reduce rush hour traffic, multiple ideas will relate to the issue of ride sharing. These issues can be organized in hierarchical or network fashion at different levels of abstraction. Fig. 1 shows one such example. The hierarchy was drawn from a pool of over 300 ideas related to the airline “no-show” problem (a customer who reserves a seat on a flight but then does not arrive on time). The reserved seat then remains empty, thus resulting in lost revenue. As reflected in Fig. 1, one typical solution to this problem is the overbooking of flights, shown here within the idea category Reservation Policy, subcategory Booking.

Hierarchies can also be employed to categorize problems' causes in a diagnosis hierarchy, which is particularly useful when multiple problem sources exist or when brainstorming for unknown causes is necessary. In addition, idea hierarchies have been used in group support software research, to help in the assessment of idea originality $[2]$ and in consensus building, but not for the generation of domain related knowledge.

Table 3  
Idea quantity and variety - Takeover problem

<table><tr><td rowspan="2">Subjects</td><td colspan="6">Internal factors</td><td colspan="3">External factors</td><td rowspan="2">All</td></tr><tr><td>Financial factors</td><td>Human resources</td><td>Product/ production</td><td>Marketing/ sales</td><td>Organization structure</td><td>Legal factors</td><td>Stock market</td><td>Buyer factors</td><td>Environment</td></tr><tr><td colspan="11">Idea count</td></tr><tr><td>Low-1</td><td>1</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>5</td></tr><tr><td>Low-2</td><td>1</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td></tr><tr><td>Low-3</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td></tr><tr><td>High-1</td><td>13</td><td>3</td><td>3</td><td>4</td><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>26</td></tr><tr><td>High-2</td><td>10</td><td>9</td><td>5</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>30</td></tr><tr><td>High-3</td><td>5</td><td>19</td><td>5</td><td>6</td><td>4</td><td>0</td><td>5</td><td>4</td><td>3</td><td>51</td></tr><tr><td>Lows combined</td><td>3</td><td>6</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>13</td></tr><tr><td>Highs combined</td><td>28</td><td>31</td><td>13</td><td>16</td><td>6</td><td>0</td><td>5</td><td>5</td><td>3</td><td>107</td></tr><tr><td>All subjects</td><td>106</td><td>78</td><td>24</td><td>31</td><td>10</td><td>2</td><td>10</td><td>19</td><td>5</td><td>285</td></tr><tr><td colspan="11">Number of addressed sub-categories</td></tr><tr><td>Low-1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>4</td></tr><tr><td>Low-2</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td></tr><tr><td>Low-3</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td></tr><tr><td>High-1</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>13</td></tr><tr><td>High-2</td><td>2</td><td>3</td><td>2</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>12</td></tr><tr><td>High-3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>2</td><td>0</td><td>1</td><td>2</td><td>1</td><td>19</td></tr><tr><td>Lows combined</td><td>2</td><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>8</td></tr><tr><td>Highs combined</td><td>4</td><td>3</td><td>6</td><td>6</td><td>2</td><td>0</td><td>1</td><td>2</td><td>1</td><td>25</td></tr><tr><td>All subjects</td><td>4</td><td>3</td><td>9</td><td>7</td><td>3</td><td>2</td><td>2</td><td>6</td><td>3</td><td>39</td></tr></table>

Hierarchical ordering and theme identification is a process that has to be completed by people, though software can be developed to assist in the process. The software initially contains all ideas in a non-hierarchical pool. It then allows for the assignment of each idea to (at least) one category. If a category does not exist, it is generated at that time. Categories are added to the idea pool, so that they can be assigned later to other, higher level categories. There are often multiple views on how to categorize the ideas. Nevertheless, hierarchical representations, if designed reasonably, are useful in determining relative idea frequencies and idea variety. A hierarchy should be considered reasonable if it represents the whole data set with a small number of descriptive and meaningful categories.

## 6.3. Implementation as domain-related knowledge

Idea hierarchies are useful in the generation of domain related rules and facts. For example, “cargo/passenger space redistribution” and “put luggage onto empty seats” could be represented as “To overcome empty seats, redistribute the plane’s cargo /seat space.” This rule can be stored and executed in any problem situation concerned with inadequately used airline resources. Still, the rule is related to airlines and is therefore domain specific. In a further abstraction step, it can be converted into a business rule: “To overcome under-utilization of a resource, increase alternate use of it.” The modified rule is applicable to a variety of business problems.

The application of domain related knowledge to a specific problem requires that rules and facts be converted back into domain dependent form. To achieve this, a specialization process is used. The software user is prompted with terms from the abstracted rule and asked to replace them with more specific terms fitting the domain. For example, the user may be prompted with the question “In your problem, what would be an example or an instance of a(n) environment?" to which he or she replies "political climate in Moscow." The software's question is generated by the domain related rule "To achieve success determine how the environment will impact you in terms of resource requirement," one of several domain related rules stored in the program. The software requests instantiations for all abstract concepts contained in a rule, for instance, success = victory over hard-liners, environment = political climate in Moscow, and resource requirement = backing by the military. The software then responds with the domain specific suggestion, here "To achieve victory over the hard-liners determine how the political climate in Moscow will impact you in terms of backing by the military." Not all software suggestions generated in this manner are relevant. In two benchmarking tests (15 rules/30 ideas generated and 50 rules/99 ideas generated) the software produced about $40\%$ syntactically incorrect, irrelevant, or mundane ideas.

## 6.4. Evidence of usefulness

Domain related rules, both general and specific, are fairly simple and the resulting ideas are not always correct or meaningful. To assess their usefulness despite these weaknesses, another empirical test was completed. In the experiment, 17 individuals (MBA students, more than 5 years average work experience, 6 females) brainstormed for causes of and solutions to the “takeover” problem. (potential criteria that make a company a target for being bought out by another organization). Subjects spent 15 minutes on the task (+2 minutes to finish off), working individually. The three most fluent (largest number of ideas) subjects produced 26 or more ideas each. Overall the subjects generated 285 ideas, or about one idea per minute per individual. The ideas of all subjects were collected in a pool from which an idea hierarchy was created. Aside from the idea aggregation in hierarchy form, the three most and least fluent individuals were identified and evaluated separately. All results are summarized in Table 3, showing the number of ideas per subject and idea diversity, measured by the number of addressed idea categories, etc. The differences both in idea quantity and diversity are evident. However, idea diversity appears to be difficult to achieve for any individual.

The nominal group consisting of all three high performers addressed 25 out of 39 subcategories, six more than the best individual, the low performer nominal group addressed at least 8. A computer program could augment problem solver performance by taking the place of the additional group members, prompting an individual decision maker for more idea diversity, based on its knowledge of a variety of solution categories. Its access to the rule set should yield more and better results than access to an idea hierarchy.

## 7. Summary and research outlook

Real problems are often messy and difficult. Although this problem type is by nature not well suited for computerization, the article has introduced two methods for computer based decision support. The first one furnishes process support by asking questions and recording relevant data while being highly domain independent. The second one abstracts and “recycles” domain related knowledge for use in new problems. Although both methods are relatively simple, the preliminary empirical data indicates a significant positive impact on idea yield. The main benefit of these methods is the value they bring to the solution finding effort without the need for a complete computer based problem representation.

A concern in the development of new support methods such as these will be the users' willingness to apply them. Problem solving success cannot be guaranteed simply through the use of the software. Success is largely dependent on the problem solver. A user may become discouraged and refrain from future use of the techniques, particularly because traditional types of computer based decision support and expert systems have come up with the (computationally) "right" solution given the existing data. The computer system acting simply as facilitation or brainstorming tool, has been much less prevalent. User acceptance may ultimately prove to be the most important issue, deciding success or failure of this type of technology.

## Acknowledgements

This research was supported in part by the National Science Foundation under Grant No. SES-9016305. The research assistance of Chharlie [correct spelling] Chau, Lisa Davis, Albert Hayashi, David Kang, and Karl Kortepeter is acknowledged.

## Appendix 1

## Appendix: Banking problem question and answer sheets

Each subject received a sheet describing the problem and the idea generation task. The task description differed, based on the treatment group to which a subject was assigned. All four task descriptions are listed below.

## Problem

Financial institutions are facing difficult times. For example, a drop in home purchases has reduced income from mortgages, while reductions in consumer spending have negatively affected the credit card business. Similarly, institutional borrowers are shopping for the lowest interest rates and often satisfy their borrowing needs through other sources than conventional financial institutions. Given this situation, you are asked to come up with new product ideas. These may include new ideas for loans, savings or other financial services.

Your answers will be judged both in terms of quantity and quality. Please record your answers on the following sheets.

## Group 1 version:

Instead of simply writing down your answers, you are asked to use a specific method to come up with solutions. First think of a theme or general concept and then let that theme or concept trigger new idea variations.

Example:

THEME / CONCEPT INNOVATION
Affordability fixed-rate negative amortization mortgage low interest credit card

## Group 2 version:

Instead of simply writing down your answers, you are asked to use a specific method to come up with solutions. First think of a product feature and then let that feature trigger new idea variations.

Example:

FEATURE INNOVATION

interest rate fixed-rate negative amortization mortgage low interest credit card

## Group 3 version:

Instead of simply writing down answers, you are asked to use a specific method to come up with solutions. First think of an existing product/service you may want to as a basis to develop solutions through variation.

Example:

EXISTING PRODUCT INNOVATION
Negative amortization fixed-rate negative
mortgage amortization mortgage
Credit card low interest credit card

## Group 4 version:

Instead of simply writing down answers, you are asked to specify both the idea and the triggering (or underlying) thought if there is one.

Example: INNOVATION

INNOVATION TRIGGERING
THOUGHT
Low interest rate credit
card low interest rate
Fixed-rate negative
amortization mortgage –

## References

[1] Ackoff, R., “The Art and Science of Mess Management,” Interfaces, Vol. 11, No. 1, Feb. 1981, pp. 20–26.

[2] Connolly, T., Jessup, L.M. and Valacich, J.S., “Effects of Anonymity and Evaluative Tone on Idea Generation in Computer-Mediated Groups,” Management Science, Vol. 36, No. 6, 1990, pp. 689–703.

[3] Crovitz, H.F., Galton's Walk, Harper and Row, New York, 1970.

[4] Dahlgren, K., Naive Semantics for Natural Language Understanding, Kluwer Academic Publishers, Boston, 1988.

[5] Durand, D.E. and VanHuss, S.H., “Creativity Software and DSS,” Information and Management, Vol. 23, No. 1, 1992, pp. 1–6.

[6] Elam, J.J. and Mead, M., “Can Software Influence Creativity?” Information Systems Research, Vol. 1, No. 1, March 1990, pp. 1–22.

[7] Elam, J.J. and Mead, M., “Designing for Creativity: Considerations for DSS Development,” Information and Management, Vol. 13, No. 5, 1987, pp. 215–222.

[8] Hayes, P.J., “The Naive Physics Manifesto,” in Mitchie, D. (ed.) Expert Systems in the Micro Electronic Age, Edinburgh University Press, Edinburgh, 1979.

[9] Holyoak, K.J. and Thagard, P., “Analogical Mapping by Constraint Satisfaction,” Cognitive Science, Vol. 13, No. 3, 1989, pp. 295–355.

[10] Kepner, C.H. and Tregoe, B.B., The Rational Manager, McGraw-Hill, New York, 1965.

[11] Klein, M. and Methlie, L.B., Expert Systems: A Decision Support Approach, Addison-Wesley, Wokingham, 1990.

[12] Korf, R.E., “Towards a Model of Representation Changes,” Artificial Intelligence, Vol. 14, 1980, pp. 41–78.

[13] Kriegsman, M. and Barletta, R., “Building a Case-Based Help Desk Application,” IEEE Expert, Vol. 8, Dec. 1993, pp. 18–26.

[14] Langley P., Simon, H.A., Bradshaw, G.L. and Zytkow, J.M., Scientific Discovery: Computational Explorations of the Creative Processes, The MIT Press, Cambridge, 1987.

[15] Lord, C. and Dahlgren, K., “Representation of Business and Financial Knowledge in the NewSelector System,” Working Paper, IBM Los Angeles Scientific Centre, Jan. 1990.

[16] MacCrimmon, K.R. and Wagner, C., “An Information System for Alternative Generation,” Journal of Management Information Systems, Vol. 8, No. 3, Winter 1991/92, pp. 49–68.

[17] Marchant, G., “Analogical Reasoning and Hypothesis Generation in Auditing,” The Accounting Review, Vol. 64, No. 3, July 1989, pp. 500–513.

[18] Mintzberg, H., Raisinghani, D. and Theoret, A., “The Structure of ‘Unstructured’ Decision Processes,” Administrative Sciences Quarterly, Vol. 21, 1976, pp. 256–275.

[19] Newell, A. and Simon, H.A., “GPS: A Program that Simulates Human Thought,” in Feigenbaum, E.A. and Feldman, J. (eds.) Computers and Thought, Academic Press, New York, 1963.

[20] Niwa, K., “A Knowledge-Based Human-Computer Cooperative System for Ill-Structured Management Domains,” IEEE Transactions on Systems, Man and Cybernetics, Vol. 16, No. 3, May/June 1986, pp. 335–342.

[21] Osborn, A.F., Applied Imagination, Scribner, New York, 1963.

[22] Pastrick, G., “Brainstorming Software,” PC Magazine, April 30, 1991, pp. 329–338.

[23] Rhodes, J., Conceptual Toolmaking: Expert Systems of the Mind, Basil Blackwell, Cambridge, 1991.

[24] Schank, R.C., Explanation Patterns, Lawrence Erlbaum Associates, New York, 1986.

[25] Silverman, B.G., “The Use of Analogues in the Innovation Process: A Software Engineering Protocol Analysis,” IEEE Transactions on Systems, Man and Cybernetics, Vol. 15, No. 1, Jan./Feb. 1985, pp. 30–44.

[26] Thierauf, R.J., Creative Computer Software for Strategic Thinking and Decision Making, Quorum Books, Westport, 1993.

[27] Vessey, I., “Expertise in Debugging Computer Programs: A Process Analysis,” International Journal of Man-Machine Studies, Vol. 23, 1985, pp. 459–494.

[28] Walker, M.G., “How Feasible is Automated Discovery,” IEEE Expert, Vol. 2, Spring 1987, pp. 69–82.

[29] Waterman, D.A., A Guide to Expert Systems, Addison-Wesley, Reading, 1986.

[30] Young, L.F., Decision Support and Idea Processing Systems, Wm.C. Brown Publishers, Dubuque, 1989.

![](/api/attachments/R8HQE8CR/fulltext/images/491ee3d54331f1bd800d3355267832a19ca3219bf9fc2c05875124c124a91701.jpg)

Christian Wagner is Assistant Professor of information systems at the University of Southern California's School of Business Administration. He holds a Diplom-Ingenieur degree in industrial engineering from the Technical University Berlin and a Ph.D. in Business Administration from the University of British Columbia. Wagner's research interests include computer support for non-quantitative problem solving and database design. Results

of his research have appeared in management, information systems and marketing journals in the United States, Europe and Japan.
