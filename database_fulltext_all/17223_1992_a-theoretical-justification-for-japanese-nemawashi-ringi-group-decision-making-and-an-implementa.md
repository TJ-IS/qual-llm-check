---
otero_id: 17223
otero_key: "B262ZH9Z"
title: "A theoretical justification for Japanese nemawashi / ringi group decision making and an implementation of a nemawashi / ringi group decision support system"
authors: "Michael D. Wolfe"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90004-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A theoretical justification for Japanese nemawashi / ringi group decision making and an implementation of a nemawashi / ringi group decision support system

Michael D. Wolfe

Department of Management, College of Business and Economics, West Virginia University, Morgantown, WV 26506, USA

The success of Japanese group decision making suggested an investigation into some of the concepts involved, an attempt to provide a theoretical framework to explain this success, and the development of a computer architecture to support this style of group decision making. The Japanese style of group decision making relies heavily on the concept of nemawashi, in which a coordinator or facilitator is responsible for moving the group to consensus. An application of Arrow's theorem provides a theoretical justification for why this approach succeeds. An architecture is developed for a system which provides decision support to the coordinator, and which uses only inexpensive and widely available technology. The system was originally developed as a Portable version of an Entrepreneurs' Group Decision Support System and was called PEG. PEG provides an integrated system in which a variety of group decision models are readily accessible to the coordinator, and also facilitates communications among the group members and between the group and the coordinator. PEG also provides a method for combining the experts' quantitative estimates so as to provide a minimum-variance unbiased consensus.

Keywords: Group decision support systems (GDSS), Japanese decision making, Spreadsheet, Computer supported collaborative work (CSCW).

![](/api/attachments/B262ZH9Z/fulltext/images/fae010086753eabfae8224c6ce83ae663d8676f2e0cd1224862c8e1f7ada9f86.jpg)

Michael D. Wolfe received a Ph.D. in Mathematics in 1978, and a second Ph.D. from the Department of Management Science and Information Systems at the University of Texas at Austin in 1988. He has worked on large-scale parallel finite difference codes, on expert systems for accessing engineering databases, and on decision support systems for personnel management and logistics. Currently, he is working on low cost group decision support systems based on hypertext, and applications of such systems for Total Quality Management.

## 1. Introduction

Many decision makers must work in groups wherein they are faced with the problem of achieving consensus. This requirement for consensus is more characteristic of Japanese decision-making than of normal American decision making. While American decision makers often use groups, the final decision is often the sole responsibility of the senior participant, who may decide unilaterally, in contrast to the Japanese attempt to reach consensus via a process called nemawashi / ringi [31]. In the Japanese system, a coordinator is crucial to the process. The coordinator has no coercive authority, but works by persuasion.

This paper explores the theoretical difficulties involved in obtaining consensus, explores the design of a computer-based system architecture designed to assist a coordinator in bringing decision makers to a consensus, and describes an implementation of the system.

The system developed supports the group decision processes even with a coordinator who has no previous computer experience by the use of a suite of spreadsheet macros. It is designed to assist with any group decision problem satisfying the following conditions:

1. The group members are each able to provide a weighted list of their individual requirements; these requirements need not be closely related, but may well be orthogonal.

2. A list of alternatives can be obtained, and each alternative can be ranked relative to the decision makers' requirements. This will be discussed further in Section 5.

3. A coordinator is available to operate the system.

The system has minimal hardware requirements, but is nevertheless powerful enough to support the analysis required. The system was developed using spreadsheet software. It provides the members of the group with analyses of the alternatives under consideration, graphical displays of the information, if desired, a record of the models used in the analysis, and models for computing group rankings of the alternatives.

In particular, the system was implemented to assist seven investors in Austin, Texas, who were considering the formation of a consortium to acquire one or more properties. The group had made previous investments, and had a history of working together. Previously, the group had relied on intuition and manual analysis of property descriptions, and disappointing results had led them to request a more formal and scientific decision analysis system.

The capital requirements for investment were such that participation of all seven investors was necessary. As in the Japanese decision making model, a coordinator developed from among the group members, and became responsible for finding an investment alternative that was acceptable to all members of the group.

The problem of finding an alternative acceptable to all members of the group was complicated by the group members' varying goals for this project. All were interested in acquiring some commercial property in Austin and setting up some sort of business on it that would pay the carrying costs while the land appreciated. The investors were interested, however, in a variety of other, possibly conflicting issues, including:

\- trees: one investor had recently acquired a number of trees, was disappointed with the offers from wholesalers, and wanted the enterprise to include a nursery as an outlet for his trees;

\- “green” issues: several of the other investors wanted the enterprise to provide organic groceries for the Austin market;

\- cash flow vs. long term growth: some investors had a need for immediate cash flow, while others were more interested in tax-sheltered growth of equity.

The investors therefore wanted a system that would help them develop a consensus, a mutually suitable enterprise both in terms of its financial prospects, and in terms of some of these other issues.

Hardware resources available consisted of several PCs, and software available consisted of 1-2-3 $^{®}$ compatible spreadsheets. None of the investors were proficient with the PC. In particular, the coordinator had no previous computer experience.

The entire system was implemented on commonly available PC computers, connected only by "sneakernet," i.e. by someone walking around the set of floppy disks with the system data from computer to computer. Future research directions include development of a PC-LAN version.

The organization will therefore be as follows: Section 2 will describe some general considerations for computer assisted group decision support systems; Section 3 will discuss why Arrow's Impossibility Theorem makes group consensus such a theoretically difficult problem; Section 4 describes the Japanese method of nemawashi / ringi, and suggests how it overcomes Arrow's theoretical difficulties; Section 5 will then describe the specific implementation to the problem of the Austin investors.

## 2. Group Decision Support Systems

Substantial research has been done on Group Decision Support Systems GDSS which partially included effectiveness and cost issues. In any group process,

Actual Effectiveness

= Potential Effectiveness

$$
- \text {   Process   Losses   } + \text {   Process   Gains   }\tag{1}
$$

and this Actual Effectiveness might be enhanced by GDSS [15]. Other researchers have reached similar conclusions that GDSS might substantially improve the group decision-making process [1], [3], [4], [7], [8], [9], [10], [11], [14], [16], [18], [20], [22], [24], [27], [30], [33], and [35]. Some studies, however, found that the group decisions were equally effective with or without GDSS [32]. Even more disconcerting, however, were the results wherein the use of GDSS resulted in worse decisions [17], [29]. A survey of the field indicates that results are, at best, mixed and that the studies showing the success of GDSS have not computed the total cost of the group decision [21]. This cost is

Cost of Group Decision

= Decision Process Cost

$$
+ \text {   Decision   Theoretic   Cost,   }\tag{2}
$$

where the decision process cost is the total cost of reaching the decision, including the time of the decision makers and the cost of a GDSS (if any). The decision theoretic cost is the difference between the outcome of the decision reached and the outcome if the optimal decision which could have been taken.

Few of the above studies investigated this total cost of the group decision. Some emphasize the impact of their GDSS on process cost, while others emphasize the decision theoretic cost. Some researchers de-emphasize the group process altogether in favor of a process which algorithmically selects the decision theoretic optimum [19].

Mixed results are to be expected, however, as shown in the next section.

## 3. Arrow's Impossibility Theorem

Arrow, investigating group decision processes in 1952, discovered that, under a few very plausible assumptions, there can be no single logically consistent algorithm for combining individual preferences into a group preference, thereby demonstrating an “impossibility” result for any GDSS. To understand the underlying problem, assume there are three options: A, B, and C, and three decision makers, Alpha, Beta, and Gamma. Alpha prefers A to B to C; Beta prefers B to C to A; Gamma prefers C to A to B. Then the majority, choosing pairwise, prefers A to B, B to C, and C to A; there is no logically consistent way to resolve this conflict, as is shown rigorously by the following:

Specifically, suppose a group G of $N \geq 2$ decision makers is presented with a set of $M \geq 3$ alternatives S. Let $\pi_{i}$ be the ordering of S preferred by $i \in G$ . Let $\Pi(\pi_{1}, \ldots, \pi_{N})$ be the group preference ordering on S. Then a minimal set of reasonable restrictions on $\Pi$ might include:

1. $\Pi$ is defined for every possible set of $\pi_{i}$ ;

2. For every pair of elements $s_i$ , $s_j \in S$ , if every member of $G$ prefers $s_i$ to $s_j$ , then $\Pi$ prefers $s_i$ to $s_j$ ;

3. If $\Pi(\pi_1, \ldots, \pi_N)$ prefers $s_i$ to $s_j$ , and if each $\pi_i^*$ has the same preference for $s_i$ over $s_j$ as $\pi_i$ (which may vary with i) then $\Pi(\pi_i^*, \ldots, \pi_N^*)$ prefers $s_i$ to $s_j$ .

Theorem (Arrow). If a group preference $\Pi$ satisfies 1-3, above, then $\exists g\in G\ni \forall \pi_{1},\ldots ,\pi_{N},$ $\Pi (\pi_1,\dots ,\pi_N) = \pi_g.$

The decision maker g is called the dictator [2]. The original statement of this theorem had a minor technical flaw, which was later corrected [5].

What the theorem states is that, given (at least) three alternatives, there are 6 ways in which these may be ordered; given (at least) two decision makers, there are, then, 36 possibilities for individual rankings. The only algorithm for selecting a group ranking from the individual rankings which is internally consistent over all 36 possibilities is the algorithm that merely accepts the ranking of one member of the group and uses that as the group ranking.

The conclusion is that no single algorithmic method can ever be effective to resolve all possible group decision problems.

A non-algorithmic or heuristic method is a group decision paradigm chosen on an ad-hoc basis by the coordinator to fit the specifics of the situation. Such a method is not precluded by Arrow's theorem, which only implies that no single method will work in all cases. The Japanese nemawashi / ringi is such a non-algorithmic method.

## 4. Nemawashi / Ringi

In Japanese decision making, the final stage, called ringi, consists of the circulation of a formal document, describing the decision made, among all members of the group. At this point, unanimous consensus is almost certain. This certainty of unanimous consensus is made possible by a preceding period of informal negotiations spear-headed by a coordinator or ritsuan-sha, a process called nemawashi. The process consists of five steps:

1. Information collection (joho shyushyu);

2. Data analysis and alternative generation (ritsuan);

3. Tentative plan selection by the coordinator (sentaku);

4. Negotiation and persuasion (nemawashi); and finally the

5. Formal document circulation (ringi).

These five steps have traditionally been performed by Japanese decision makers without using formal decision analysis or GDSS support (saki is often used in lieu of GDSS); however, a proposal for a set of tools has recently been suggested. Details are beyond the scope of this paper, but may be found in [31]. To summarize very briefly, the tools consist of a set of ad hoc models for computing the group rankings of the alternatives chosen. The coordinator must obtain (with pencil and paper, perhaps) a matrix of decision maker requirements and weights, a matrix evaluating each alternative against each requirement, a vector of decision maker relative influence, and a vector of decision maker difficulty of persuasion. Then, using multi-attribute utility theory, a matrix giving the cardinal rating of each alternative for each participant is obtained.

The ritsuan-sha may then select the model most appropriate for the group and decision under consideration from a selection of six broad classes of group decision models along with, typically, four variants of each class. The four variants are obtained by using either, neither, or both the influence and difficulty of persuasion vector in computing the group consensus rating of the alternatives.

A detailed description of each model is beyond the scope of this paper (but see [31]) Basically, the six classes are

1. Average (or sum) of individual rankings;

2. Majority rule (which may not exist, if there are more than three alternatives, but which may be very effective when it does exist);

3. Minimum of maximum preference difference;

4. Minimum dissatisfaction exceeding a threshold;

5. Minimum sum of dissatisfaction excluding un-persuadable participants; and

6. Coordinator's choice (when there is a decision theoretic optimum not indicated by the group members' preferences, or when nothing else works.)

An implementation and extension of these tools was developed and used for the PEG system.

## 5. PEG

The underlying theory for PEG is that each decision maker i can provide a set $A_{i}=\{a_{ij}\}$ of quantifiable requirements or criteria, where $j=1,\ldots,n_{i}$ , and a vector $\mathbf{w}_{i}=(\mathbf{w}_{ij})$ of weights. Without loss of generality, we can assume a single set of requirements $A=\cup A_{i}=\{a_{j}\}$ , i.e., that the decision makers have the same set of criteria, namely the union of all their criteria, and the distinguishing factor is the individual weight vector. An alternative $X_{k}$ is then described by its vector $\mathbf{x}_{k}=(\mathbf{x}_{kj})$ where $x_{kj}$ is the value of requirement j for alternative k. From the $w_{i}$ and the $x_{k}$ we may obtain (by any number of models) vectors for each decision maker $\mathbf{u}_{i}=(\mathbf{u}_{ik})$ where $u_{ik}$ is the scalar utility value decision maker i places on alternative k. The simplest model is the linear one, $u_{ik} = w_i \cdot x_k$ ; however, a number of non-linear models have been proposed, and could, in principle, be implemented [12].

From these, the group models developed for nemawashi / ringi allow the computation of a single group vector $\mathbf{u}_{\mathrm{m}}(\mathbf{u}_{\mathrm{km}})$ the group utility for alternative k and model m.

In this notation, several of the nemawashi / ringi group models may be written

$$
\mathrm{u} _ {\mathrm{km}} = \sum_ {\mathrm{i}} \lambda_ {\mathrm{i}} \mathrm{u} _ {\mathrm{i}},\tag{3}
$$

where $\lambda_{i}$ is the weight or influence attributed to decision maker i. This is obvious for class 1, but is also true for class 5, where the $\lambda_{i}$ for unpersuadable individuals is set to 0. In fact, this group utility function will be appropriate as long as the following is true: Every pair of alternatives which are indifferent to each individual are indifferent to the group as a whole [19].

As a consequence of Arrow's theorem, no model will work under all circumstances. An innovative feature of this system, then, is the provision of a large and extensible library of models for group decision making, from which the ne-mawashi / ringi ritsuan-sha may select the model that will bring the group to a consensus.

PEG, then, provides a platform on which any of the above Watabe, Holsapple, and Whinston models may be “hung,” and, in addition, provides implements to facilitate the acquisition of the A, w, and Z data needed. The PEG system provides support for four basic stages of group decision making:

1. Requirements Definition: Each member of the decision-making group provides a list $A_{i}$ of requirements and weights;

2. Evaluation of Alternatives: A group of domain experts (which may be disjoint or overlapping with the group of decision makers) provides a list of alternatives $X_{k}$ , and an estimate of how each alternative may be measured with respect to the decision makers' requirements to provide the set of vectors $x_{k}$ ;

3. Selection of Alternatives: The coordinator uses the various models in the system to compute the $u_{km}$ , and thereby to select the alternative most likely to win group acceptance; and

4. The system provides simple persuasion tools to assist in getting the group to accept the alternative.

PEG actually consists of a set of spreadsheet macros, models, and procedures, which will be described. Development of the system covered a period of several months. A very simple system, providing nemawashi / ringi support only for the coordinator, was actually used in the project. A network version, in which all group members could access the models simultaneously was developed, but was not available in time to use in the actual decision-making process.

## Stage 1: Requirements Definition

The requirements definition phase consists of obtaining a list of all the requirements of all the decision makers, along with a list of relative weights. In principle, decision makers could be allowed to use any relative weights they like -0-1,1-n, etc.; however, for ease of implementation, decision makers were asked to use a scale of 1–10. The process as it actually developed (no LAN was accessible) did not fit neatly into either Delphi or Nominal Group. The procedure without a LAN is described below.

1. All decision makers are asked to prepare a list of decision factors and decision variables that would affect the investment. If possible, this was to be done in columns 1 and 2 of a specially prepared spreadsheet; for those members with no access to a PC, this could be done on ruled paper (provided.) The coordinator gathers as many of these as are submitted, and prepares a list for circulation.

{When PEG was actually used, only one member responded to this request, and the initial list was essentially prepared by the coordinator with the single (paper) response entered manually. See Figure 1.}

2. The list is circulated in both electronic (floppy disk) and paper form. The group members are given spreadsheets which are protected, except for the two columns in which requirements and weights are to be entered, thereby forcing their data into a known area of their spreadsheet. No group member can deliberately or inadvertently delete another member's requirements. After seeing the original list, group members are encouraged to enter new requirements directly on the spreadsheet, along with weights. Weights are to be entered on a scale of 1 to 10. Failure to assign any weight to one of the listed factors is assumed to indicate a weight of 0. The weights must be manually checked to make sure group members used the correct scale. If another scale is used, the system linearly re-scales the weights.

<table><tr><td></td><td>A</td><td>B</td></tr><tr><td>41</td><td></td><td>Ranking</td></tr><tr><td>42</td><td>Decision Factor</td><td></td></tr><tr><td>43</td><td>Profitability of fruit stand</td><td>10</td></tr><tr><td>44</td><td>Profitability of nursery</td><td>9</td></tr><tr><td>45</td><td>Real Estate Prices</td><td>8</td></tr><tr><td>46</td><td>Synergy?</td><td></td></tr><tr><td>47</td><td>Availability of good location</td><td>7</td></tr><tr><td>48</td><td>Fruit/vegetable margins</td><td></td></tr><tr><td>49</td><td>Tree/shrub margins</td><td></td></tr><tr><td>50</td><td>Availability of management, produce</td><td>9</td></tr><tr><td>51</td><td>Availability of management, overall</td><td>7</td></tr><tr><td>52</td><td>Opportunity for tree stand</td><td>4</td></tr><tr><td>53</td><td>Competition, other supply side</td><td></td></tr><tr><td>54</td><td>Size of W. Austin market</td><td></td></tr><tr><td>55</td><td></td><td></td></tr><tr><td>56</td><td></td><td></td></tr></table>

Fig. 1. Spreadsheet for Entering Decision Factor Requirements Provided to Group Members. Decision makers are asked to submit requirements to the coordinator, who enters the next suggested requirement in the highlighted cell and weights in the adjacent cell. This is then circulated, and group members are able to see requirements and weights submitted by other group members.

{In actual usage, after seeing the coordinator's list, most group members added new requirements, typically one or two per member, and assigned weights. The correct scale for weights was used by five of the seven members, and the other two lists were re-scaled.}

3. The individual lists are combined into a master list. If the users provide their responses in electronic form, their individual spreadsheets are copied onto a hard disk, and a macro extracts individual requirements and weights and inserts these into the coordinator's master requirements document. Paper documents are entered into the master spreadsheet manually. The new master is then recirculated as in step 2; if additional requirements are identified, or weights changed, this step is repeated until the list converges.

{In the actual trial, only one iteration was needed.}

4. While the requirements document is circulating, a table is prepared with the coordinator's ranking of each group member. The separate columns for influence and difficulty of persuasion, mentioned above, are combined into a single column. This table is never shown to the group members.

The process of circulating documents on floppy disks is referred to as “sneakernet.”

“Sneakernet” is in many ways inferior to a system which provides concurrent access; however, this method actually has one slight advantage over a concurrent version which uses a Local Area Network (LAN) in that the group never need actually meet, thereby saving the cost of a group meeting, and allowing the members to interact, using the software, at times most convenient to each member. The LAN version, however, should greatly reduce decision time. After the decision had been reached, a LAN became available, and a LAN version prepared. The group process was then simulated on the LAN, as data acquired previously was re-entered into the LAN version. The LAN procedure is similar to the “sneakernet” procedure, except that group members may enter their requirements simultaneously, and paper submissions are not allowed. The architecture of the LAN version is shown in Figure 2.

In the LAN version, the spreadsheets look the same to the group members; however, the actual, underlying structure is more complicated and new macros are required. Some of this new structure is indicated in Figure 3, which was adapted from a user's actual submission. The user finds that most of the cells in the spreadsheet are protected. In this case, the user has write access only to the rows 82 through 84, as indicated by the box, and only has write access to column D. In an actual implementation, the user would have more than three rows, but only one column. Thus, the users can see all requirements and all weights currently proposed by other users, but can only change their own weights and requirement.

A set of macros is provided to support these functions, as shown in the users' menu, Figure 4. These macros are Post and Import. The Posting macro copies the two columns of the decision makers' spreadsheets to a node of the network where the coordinator has read access; the Import macro imports the master list of requirements into the decision makers' spreadsheets from a node where the coordinator has write access and the decision makers have read-only access.

Requirements for Investor 1

![](/api/attachments/B262ZH9Z/fulltext/images/3019249914a549af5f05cdca2fbf7bd2d1fe5b72a83fff1e7b19c8466bd8d646.jpg)  
Requirements for Investor 2  
Fig. 2. Preliminary version of an architecture for requirements determination software on a local area network. Decision makers submit requirements through the network using spreadsheet macros. No computer expertise is needed. Decision makers are not provided access to models or other facilities on the system at this time.

The coordinator's spreadsheet has macros to import all the decision makers requirements, to combine these into a master list, and to export the master list to an area of the local area network where the coordinator has write access and the group members have read-only access.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td></tr><tr><td>69</td><td colspan="10"></td><td colspan="2"></td></tr><tr><td>70</td><td rowspan="2">Decision Variables</td><td rowspan="2" colspan="9"></td><td rowspan="21" colspan="2"></td></tr><tr><td>71</td></tr><tr><td>72</td><td>Buy vs Rent</td><td>10</td><td>10</td><td>9</td><td>10</td><td>10</td><td>6</td><td>9.2</td><td></td><td></td></tr><tr><td>73</td><td>Parking/Traffic</td><td>7</td><td>9</td><td>10</td><td>8</td><td>8</td><td>2</td><td>7.3</td><td></td><td></td></tr><tr><td>74</td><td>Advertising venues</td><td>8</td><td>9</td><td>2</td><td>8</td><td>7</td><td>5</td><td>6.5</td><td></td><td></td></tr><tr><td>75</td><td>Size of labor staff</td><td>6</td><td>8</td><td>8</td><td>5</td><td>9</td><td>3</td><td>6.5</td><td></td><td></td></tr><tr><td>76</td><td>Days/Hours to be open</td><td>5</td><td>7</td><td>8</td><td>5</td><td>9</td><td>2</td><td>6.0</td><td></td><td></td></tr><tr><td>77</td><td>Wholesale/retail</td><td></td><td>2</td><td>9</td><td>5</td><td>6</td><td>10</td><td>5.3</td><td></td><td></td></tr><tr><td>78</td><td>Product breadth</td><td></td><td>2</td><td>8</td><td>2</td><td>8</td><td>10</td><td>5.0</td><td></td><td></td></tr><tr><td>79</td><td>Combined Operations</td><td>6</td><td>5</td><td></td><td>5</td><td>8</td><td>5</td><td>4.8</td><td></td><td></td></tr><tr><td>80</td><td>Mail order business</td><td></td><td>2</td><td>6</td><td>2</td><td>8</td><td>10</td><td>4.7</td><td></td><td></td></tr><tr><td>81</td><td>Store design/operation (physical scale)</td><td></td><td>5</td><td>9</td><td>5</td><td>6.5</td><td>1</td><td>4.4</td><td></td><td></td></tr><tr><td>82</td><td>Pesticide service</td><td>3</td><td>2</td><td>10</td><td>1</td><td>6</td><td>2</td><td>4.0</td><td></td><td></td></tr><tr><td>83</td><td>Organic</td><td>3</td><td></td><td></td><td>8</td><td>6</td><td>3</td><td>3.3</td><td></td><td></td></tr><tr><td>84</td><td>landscaping/contracting</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td><td>3</td><td>2.0</td><td></td><td></td></tr><tr><td>85</td><td>Length of lease</td><td></td><td>10</td><td></td><td></td><td></td><td></td><td>1.7</td><td></td><td></td></tr><tr><td>86</td><td>Prices</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>87</td><td>Proximity to hike &amp; bike crowd</td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td></tr><tr><td>88</td><td rowspan="3" colspan="10"></td></tr><tr><td>89</td></tr><tr><td>90</td></tr></table>

Fig. 3. The various sections of a group member's spreadsheet The section for the groups' decision variables are shown in the box in column A, rows 70-90. The weights of all the investors are (anonymously) displayed in columns B through G, and the group weights as ascertained by the coordinator are in column H. The investor "owns" the decision variables in rows 82–84, and the weights in column D. This is the only part of the spreadsheet this investor may change.

![](/api/attachments/B262ZH9Z/fulltext/images/f68b9ff6e74272019cdfb77f863b689c9edb374adff5f3244d44e4fe3f8fd91b.jpg)  
Fig. 4. Group members' menu. This menu to the macros allows the group members to update their individual spreadsheets by importing other decision factors, variables and weights from the group spreadsheet, or to export their additional factors, variables and weights to the coordinator.

A portion of the coordinator's menu options are shown in Figure 5.

Some of the requirements proposed may have no non-zero weights attached, and these are now dropped from the list. At this point, the coordinator has a comprehensive list of all the decision makers' requirements and weights entered into the first two columns of a spreadsheet.

## Stage 2: Evaluation of Alternatives

The second step in the process is to obtain a list of alternatives, and to evaluate these alternatives against the user requirements obtained in step I. These are actually two separate sub-steps. The first sub-set, generation of alternatives, will vary from system to system. Initially, as wide a range of alternatives as possible is desired, so the experts and decision makers can “funnel” down to the best possibility. Decision makers and experts can suggest alternatives. In the specific case of PEG, the coordinator obtained a list of properties available at “distress” prices and lying along the Austin interstate.

The second sub-step, that of evaluation of alternatives against requirements, is a technical, quantitative process which must be carried out by domain experts. In the specific case of the real-estate investment problem, these were real estate experts, although, in general, they are specialists skilled at quantitative analysis within the domain of decision. The group of domain experts may be distinct from the decision makers, or may overlap. The domain expert for the initial trial was, in fact, the coordinator, but this will, in general, not be the case.

<table><tr><td></td><td>AH</td><td>AI</td><td>AJ</td><td>AK</td><td>AL</td><td>AM</td><td>AN</td><td>AO</td><td>AP</td><td>AQ</td><td>AR</td><td>AS</td></tr><tr><td>1</td><td rowspan="2" colspan="12"></td></tr><tr><td>2</td></tr><tr><td>3</td><td rowspan="2" colspan="12">Please:</td></tr><tr><td>4</td></tr><tr><td>5</td><td rowspan="3" colspan="12">Hit thekey (the grey key at the top of the keyboard)Then select:</td></tr><tr><td>6</td></tr><tr><td>7</td></tr><tr><td>8</td><td rowspan="4" colspan="12">Expertsto modify expert profilesInvestorsto modify investor profilesProjectionsto modify the estimates before Posting</td></tr><tr><td>9</td></tr><tr><td>10</td></tr><tr><td>11</td></tr><tr><td>12</td><td rowspan="6" colspan="12">Hold down the Alt key and the F key to bring in new factorsHold down the Alt key and the V key to bring in new VariablesHold down the Alt key and the V key to bring in new VotesHold down the Alt key and the P key to Post results</td></tr><tr><td>13</td></tr><tr><td>14</td></tr><tr><td>15</td></tr><tr><td>16</td></tr><tr><td>17</td></tr></table>

Fig. 5. A partial view of the coordinator's menu options. This menu allows coordinators to update their spreadsheet with group members' input made since the last update, to output the group results, and to modify the weights associated with investors and experts. In addition to the options shown, the coordinator may switch among various group models, and may make votes anonymous or identified.

Since PEG is intended for use by decision makers with limited budgets, the requirements are prioritized. If funds are not available, low priority requirements will either not be evaluated, or will not be evaluated as carefully as high priority requirements. The rankings of requirements are obtained by summing (or averaging) the individual rankings, weighted by the individual decision maker's “importance” as determined by the coordinator, and by the cost of obtaining the information.

If the experts compute the ratings using formal models, they are encouraged to include these models in the spreadsheet as a record. Otherwise, they may simply list their ranking of the alternatives vs. the requirements as numbers.

<table><tr><td colspan="3">Option #: 1&quot;Thunderbird Motors&quot; spaceCorner of Koenig Lane and WoodrowLease 1 yearCost ($1,800) per monthOption to buy at any time for ($225,000)Building 800 square feetTotal space 12,500 square feetPayments at 11% ($2,143) for 30 years</td></tr><tr><td colspan="3">Projected investment:</td></tr><tr><td colspan="3">Temporary structures: ( $10,000)Advertising: ($20,000)(small TV, radio, newspapers)</td></tr><tr><td colspan="3">Staff: ($45,000) per year1 manager8 part-time employees($3,750) per month</td></tr><tr><td colspan="3">Store Start-up Expense ($10,000)(Fixtures, signage, etc.)</td></tr><tr><td colspan="3">Projected Gross Sales, First Year $325,000</td></tr><tr><td colspan="3">Projected COGS: ($200,000)(Based on 50% nursery50% fruits and vegetables</td></tr><tr><td colspan="3">Amount of inventory ($16,000)</td></tr><tr><td colspan="3">This option assumes stocking modest amounts of certified organic produce and setting prices slightly higher than supermarket and large nurseries emphasizing convenience.</td></tr><tr><td colspan="3">Total investment, 1st month: ($61,550)</td></tr><tr><td colspan="3">Monthly Revenue: $4,867Total Income, 1st Year $58,400</td></tr><tr><td colspan="3">Annual Return: 95%</td></tr></table>

Fig. 6. One Expert's Analysis of Investment Option I. This is the actual document initially submitted by the expert when asked to rank alternatives vs. requirements. Note that this is not in the format requested, but had to be “massaged” by the coordinator to achieve the required rankings.

While this step is standard in the systems life cycle, i.e. translating user requirements into technical specifications, two problems arise in practice:

1. The experts do not address the user requirements in their analysis of the alternative, but perform a standard analysis dictated by the standard methodology of their field of expertise; and

2. When two or more experts are asked to respond, the responses are inconsistent.

In an actual trial of the system, the experts' responses were not consistent among the alternatives, and did not directly address the requirements developed in stage 1. This problem may, therefore, be expected to sometimes arise in future uses of the system, and must be addressed by the coordinator. One of the actual responses for one alternative is shown in Figure 6.

From the experts' responses, the vector $x_{1}$ of ratings of each option vs. the requirements must be computed. The ideal procedure is as follows:

1. The experts each have a copy of the requirements/options matrix, extracted from the master spreadsheet.

2. The experts develop a model of each alternative directly on their copy of the spreadsheet, in a section of the spreadsheet outside the matrix.

3. Numerical values for the matrix are computed directly from the model.

4. The spreadsheets with the models are archived for future reference, and the values of the matrix are extracted and returned to the coordinator.

5. The system then combines the experts' matrices into a single matrix.

In the trial, the experts provided spreadsheet models similar to Figure 6 for each alternative, although the models varied slightly. The coordinator then, using the models, selected 10 requirements, ranked each of the alternatives on a scale from 1 to k for each of the 10 selected requirements, and entered these values manually into the matrix. The requirements were selected partially based on the decision makers' rankings of importance, and partly based on ease of computing the rankings (i.e., looking for the lost wallet under the lamppost because the light is better there.)

## Combining Expert Judgments

Watabe, Holsapple, and Whinston indicate that this stage, that of obtaining expert evaluations of alternatives vs. requirements, is an important part of nemawashi / ringi group decision making, but gloss over the difficulties that may be involved in a practical application. Where the requirement is “profitability of the nursery aspect of the business,” for example, the experts may not respond in directly comparable terms: for example, one might respond with an estimate of net present value (NPV), another with an estimate of internal rate of return (IRR), and another with a model that estimates the vector of future cash flows without a scalar measure of comparison. The experts may also respond with ordinal rankings, which are not amenable to arithmetic manipulation. Even when an effort is made to constrain the experts within prescribed parameters, experts tend to respond using the methodology and language of their training.

The PEG solution to these problems, outlined above, is to have the coordinator resolve these discrepancies.

It may, however, be the case that the experts' judgments are expressed in the form of scalar estimates, as, e.g. if all the experts provide an estimate of NPV as their measure of the profitability of the nursery. In this case, there remains the problem of obtaining a single measure from the estimates. This is a problem which has been debated at length [6], [13], [23], [25], [26], [28], [34]. The simple solution used by PEG is a potentially important contribution to the theory and practice of GDSS.

The PEG system assumes that, initially, the coordinator has some idea about the quality and reliability of the experts, and that records are kept of the experts' predictions, and the actual performance of the quantity predicted vs. the prediction. In the case of investments, the experts predict, at regular intervals, the prices of the components of a portfolio at the end of the interval. For a more general system, the experts provide for each alternative to be acquired how they expect it to eventually measure up to each requirement. In practice, actual performance is expected to differ from the experts' predictions. Over time, the experts will make their predictions for a series of projects, estimating, in each case, the performance of similar alternatives against similar requirements. Mathematically, describe the actual performance of the alternative vs. the requirements as a random vector $\mathbf{X}(t)$ , for the project whose performance becomes known at time t.

Without loss of generality, we write

$$
\mathbf {X} (t) = \hat {\mathbf {Y}} _ {i} (t) - \epsilon_ {i} (t),\tag{4}
$$

where $\epsilon_{i}(t)$ is a random vector with mean 0. Thus the $\hat{Y}_{i}(t)$ represent the ith expert's best (unbiased) guess as to the value which the random process $\mathbf{X}(t)$ will take at time t. We do not make the usual assumptions that the errors are i.i.d.

Thus, PEG computes a linear function $\Phi_{t}$ such that

$$
\hat {\mathrm{X}} (\mathrm{t}) = \boldsymbol {\Phi} _ {\mathrm{t}} \left(\hat {\mathrm{Y}} _ {1} (\mathrm{t}), \hat {\mathrm{Y}} _ {2} (\mathrm{t}), \dots , \hat {\mathrm{Y}} _ {\mathrm{m}} (\mathrm{t})\right)\tag{5}
$$

is the consensus estimate of $\mathbf{X}(t)$ .

In fact, we have developed an optimal estimator of $\hat{X}(t)$ in the sense that the resulting

$$
\varepsilon (t) \equiv \mathbf {X} (t) - \hat {\mathbf {X}} (t)
$$

is the minimum variance unbiased linear estimator.

(6)

In addition, $\Phi_{t}$ varies with time: as PEG is used, the information about the experts' reliability is re-assessed, and the formula for evaluating their judgments is revised.

In order to compute $\Phi_{t}$ , we must make one additional assumption, namely that the matrices $\operatorname{Var}(\varepsilon(t))$ do exist for all t, where $\epsilon(t)$ is the random vector whose components are the $\epsilon_{i}(t)$ .

Theorem. The optimal linear consensus estimate that may be obtained from the collection of the various experts' estimates is

$$
\hat {X} (t) = \boldsymbol {a} (t) ^ {T} \hat {Y} (t),\tag{7}
$$

where

$$
\boldsymbol {a} (t) = \left(\operatorname{Var} (\epsilon (t))\right) ^ {- 1} \lambda ,\tag{8}
$$

where $\lambda(t) = \lambda(t)$ 1 is chosen so that the components $a_{i}$ of $\pmb{a}$ satisfy

$$
\sum a _ {i} (t) = 1.\tag{9}
$$

Stage 3: Group Ranking of Alternatives

Watabe, Holsapple, and Whinston list 21 different models for combining the matrix W of decision makers' weight vectors $w_{i}$ with the experts' matrix X of alternatives vs. requirements. The default in PEG is the simple linear model given by (3). The $\lambda_{i}$ are obtained as manual inputs from the coordinator. The other models are available in the spreadsheet as named ranges, and the coordinator may use them if the first model fails to achieve a consensus.

<table><tr><td>Decision Factor</td><td>Weighted Consensus</td><td>Option 1</td><td>Option 2</td></tr><tr><td>Profitability of fruit stand</td><td>9.5</td><td>1</td><td>2</td></tr><tr><td>Profitability of nursery</td><td>9.3</td><td>1</td><td>2</td></tr><tr><td>Real Estate Prices</td><td>8.8</td><td>2</td><td>1</td></tr><tr><td>Synergy?</td><td>7.5</td><td>2</td><td>1</td></tr><tr><td colspan="4">Decision Variables</td></tr><tr><td>Buy vs Rent</td><td>9.2</td><td>1</td><td>2</td></tr><tr><td>Parking/Traffic</td><td>7.3</td><td>1</td><td>2</td></tr><tr><td>Advertising venues</td><td>6.5</td><td>2</td><td>1</td></tr><tr><td>Size of labor staff</td><td>6.5</td><td>1</td><td>2</td></tr><tr><td>Days/Hours to be open</td><td>6.0</td><td>1</td><td>2</td></tr><tr><td>Wholesale/retail</td><td>5.3</td><td>-</td><td>-</td></tr><tr><td>Weighted Sum</td><td></td><td>47.8333</td><td>22.833</td></tr><tr><td colspan="4">Note: number = rank (1st or 2nd) Score = 2-rank</td></tr></table>

Fig. 7. Rankings of two options. This particular model simply ranks each option from 1 to number-of-options, uses the average weight assigned to the option by the group, and takes the weighted average rank (weighted by group average weight) to determine a weighted overall rank. The coordinator may accept this ranking and present it to the group, or select some other group model if the alternative chosen by this method is unacceptable, i.e. if the group cannot reach consensus on this alternative.

Annual Return vs. Gross Revenues  
![](/api/attachments/B262ZH9Z/fulltext/images/5dd83c28359c2768fff59c3e119ce4885f32894b2d6e5d86b3d729b3887274dc.jpg)  
Gross revenues as a percent of original projection  
Fig. 8. Sample chart presented to decision makers as part of persuasion process. The spreadsheet makes a variety of visual effects available to the experts to share in making their points to the group, of which the above chart is merely a typical representative.

![](/api/attachments/B262ZH9Z/fulltext/images/ec8daa0ce24f6ac0f5ff6083d91c50d6b167e6d5bb804aff08c05a06fc82589c.jpg)  
Private Models for Expert 2  
Fig. 9. Possible Architecture of PEG on LAN during nemawashi process. This is the system for the experts rather than the decision-makers, and assumes the experts are sophisticated enough to develop and use computer models, as opposed to Figure 2, where users were limited to a single template established just for communications.

For the specific problem of the Austin real estate investment, the computations were done in a different order: group weights for the requirements were obtained first, then a group ranking of alternatives was obtained, rather than obtaining individual rankings and using these to obtain group rankings. This procedure is not adequate for all group models, but it was sufficient for the initial test. The results are shown in Figure 7.

The group weight for each requirement was obtained by taking an average of individual weights, weighted by the coordinator's estimate of each investor's expertise. The options were then ranked, and the weighted rank computed. On the basis of this evaluation, the coordinator then presented Option 1 to the investors.

## Stage 4: Nemawashi

At this point, the group is presented with alternatives, and the coordinator tries to achieve a consensus. This may be done either with “sneakernet” or using a LAN. In the “sneakernet” version, the coordinator visits, telephones, or mails materials to each group member. Because the models were developed on a spreadsheet, persuasive materials are readily available. For example, the spreadsheet was used to obtain a variety of graphs indicating the potential performance of the selected option, as shown in Figure 8.

The system without a LAN is quite inexpensive, requiring, at a minimum, only an 8088 class PC with a 1-2-3 $^{®}$ compatible spreadsheet, available, using current technology and prices, for under 1,000.

If a LAN, the architecture shown in Figure 9 makes a more sophisticated version of nemawashi possible. This is the architecture expected to be used for computer-supported cooperative work (CSCW) by the experts, where participants are provided access to all the power of the computer for their analysis, in addition to the communications facilities. This is the most sophisticated system studied, and is much more complicated that the simple version available to the decision makers shown in Figure 2.

In the same manner that requirements were exchanged during stage I, model parameters and assumptions may be exchanged at this point, with individual group members sending spreadsheet extracts to a place on the network that the coordinator can read, and the coordinator sending group parameter estimates to a network node where the group members have read-only access. Charts, similar to Figure 4, may be placed in the central “electronic blackboard” location for perusal as well, using the spreadsheet facility for saving graphics in a separate file, which may be placed (using a macro) in the appropriate place, even by a coordinator with no knowledge of spreadsheets or LAN management.

Another advantage of the LAN method is that a permanent record of the decision-making process, not just the result, is kept to prevent future recriminations and to provide a “group memory” which may be of assistance in future group decisions. Since the members entered their own data for this record, there is no possibility of the coordinator adding errors (or being accused of adding errors) as the information is transcribed to the GDSS as it must be under the “sneakernet” architecture. While the trade-off chosen will be the decision of the coordinator, it will clearly depend on the preferences of the group members.

A possible disadvantage of the LAN approach to nemawashi is the basically informal nature of the process. Ultimately the nemawashi stage is really the province of the coordinator who must use informal persuasion, supported by the PEG system. In the “sneakernet” version, the disk is kept by the coordinator, who walks it around the group, typically meeting with group members in a “one-on-one” basis. In the first two stages of the process, the joho shyushyu and ritsuan, data collection from computerphobic members of the group could be done manually and later entered into the system. This can be a better method of acquiring data from users reluctant to have their informal ideas recorded early in the decision making process.

Similarly, once the coordinator has selected a tentative plan and used the GDSS to develop audio-visual items which support the plan, these items may be generated privately and walked around to those group members reluctant to deal with the machine. This mode of functioning is lost when using the concurrent LAN version. Another disadvantage is the loss of intertemporal group decision support: one advantage offered by the sequential use device is that it allows decision makers with schedule conflicts to have a “virtual” meeting using the technology, and this possibility is lost if all users must access the system simultaneously.

Finally, the cost of a LAN system exceeds the cost of the sneakernet version by a significant amount. The cost of a node on a LAN is approximately twice the cost of a minimally configured PC, and, in addition, a file-server machine is necessary, so an estimate of the cost of the LAN version, with N group members, is approximately \$2,000 × N.

The facilitator only system and the sequential group member system can be implemented using current technology for less than \$1,000, since all that is required is an 8088 class CPU and a 1-2-3 $^{\textregistered}$ spreadsheet software package. The concurrent system requires a PC for each group member and a LAN, so, for a group of N members, the cost is approximately \$2,000 × N.

## 6. Summary and Conclusions

This paper indicates that, based on the work of Arrow, there is a solid theoretical foundation for the success of Japanese nemawashi / ringi decision making. Where groups must reach consensus, Arrow has shown that no single, algorithmic approach will work in all cases. However, the multiple, non-algorithmic nemawashi / ringi method, in which a coordinator has access to a large library of heuristic group models, can provide the tools needed for consensus to be reached if the correct model is present in the library.

The contribution of this paper is to demonstrate an architecture for the implementation of a system which supports cooperative work using these nemawashi / ringi methods. A primary goal of this implementation, which was achieved, was to provide a portable, low cost GDSS that might be used by coordinators who must bring a group of decision makers to consensus, and who lack access to the more expensive and sophisticated GDSS. The system described in this paper consists of procedures, spreadsheet templates and macros, and is portable to any computer environment supporting a spreadsheet, hence it may operate in a very low-cost environment, without any physical networking. The system is, in addition, capable of taking advantage of a local area network, if one is available. The procedures, templates, and macros provide decision-makers and experts support for:

1. Gathering user requirements and the weights the users associate with those requirements;

2a. Obtaining a set of alternatives;

2b. Having a group of experts evaluate those alternatives against the user requirements, and combining the expert evaluations into a single evaluation;

3. Selecting the group alternative; and

4. Presenting this alternative to the group members.

In combining quantitative expert opinions into a single number, there is no agreement on how to define what a “best” approach would mean. Taking as a working hypothesis that the experts opinions represent a “correct” assessment of the situation plus a random error term, the quantitative estimate with minimal expected error is obtained. The system then supports the coordinator by computing, via a variety of group models, suggestions for alternatives on which the group may achieve consensus. The system is, however, strictly a decision support system, and ultimately relies on the coordinator’s judgement for the most appropriate group model.

The system developed was successfully used by a group of investors who needed both mathematical analysis of potential investments and a means of coordinating somewhat disparate goals. The system provides a large and extensible library of models for computing group alternatives on an ad hoc basis. Finally, the method provided for combining inconsistent expert judgments represents an important advance for GDSS.

Limitations of the research project described herein include:

\- The potential of this system for enhancement of group decision making effectiveness was demonstrated in a qualitative manner, but was not measured. In terms of equation (2), however, the very low cost makes the system an attractive option as part of an overall GDSS strategy for decision makers with limited resources.

\- A single trial cannot indicate what sort of mean levels of overall cost reduction might be expected from use of the system.

Future research needs to be done using the system in a variety of settings in order to quantify the enhancement of group effectiveness as well as the mean reduction in group decision making costs.

## Acknowledgment

I would like to thank Mr. Robert Pyeatt, the coordinator of the group, who provided invaluable cooperation and assistance with this project, and without whose help and inspiration PEG would not have been possible. I would also like to thank Professor M. Hatcher for his invaluable encouragement, and Ms. J. Ward for her editorial assistance.

## References

[1] J.M. Abram, C.Y. Chang, V.G. Rutenberg, E. Tse and R.P. Wishner (Advanced Information & Decision Systems). Distributed Decision Making Environment. Griffiss AFB NY: Rome Air Development Center (COTD), 1982, RADC-TR-82-310.

[2] Kenneth J. Arrow, Social Choice and Individual Values, 2nd ed. (Wiley, New York, 1963).

[3] Tung Bui and Matthias Jarke, Communications Requirements for Group Decision Support Systems, Journal of Management Information Systems 2, No. 4 (1986) 8–20.

[4] A. Burns, M.A. Rathwell and R.C.A. Thomas, Distributed Decision-Making System, Decision Support Systems 3 (1987) 121–131.

[5] J.W.S. Cassels, Economics for Mathematicians, London Mathematical Society Lecture Note Series 62 (Cambridge University Press, Cambridge, 1981).

[6] Robert T. Clemen, Calibration and the Aggregation of Probabilities, Management Science, 32, No. 3 (1986) 312–314.

[7] David A. Dierolf and Karen J. Richter, Computer-Aided Group Problem Solving for Unified Life Cycle Engineering (ULCE), IDA Paper P-2149 (Institute for Defense Analysis, Alexandria, VA, 1989).

[8] James Patrick Driscoll and Jeffrey Ayres King, An Empirical Experiment Evaluating the Effectiveness of Group Decision Support Systems (GDSS), AD A201 864 (Naval Postgraduate School, Monterey, CA, 1988).

[9] R. Eck, M. Goul, A. Philippakis and S. Richards, Group

Operating Systems for Decision Factories of the Future: An Extended Relational GDSS Architecture. (Arizona State University, Tempe, AZ, 1989).

[10] J.D. Eveland and T.K. Bikson, Work Group Structures and Computer Support: A Field Experiment, ACM Transactions on Office Information Systems 6, No. 4 (1988) 354–379.

[11] Young-Ok Fijol and Mary A. Woodbury, Group DSS and Decision Outcome Measures: A Comparative Study in Distributed Versus Non-distributed Settings, AD A180 949 (Naval Postgraduate School, Monterey, CA, 1987).

[12] Peter C. Fishburn, Nonlinear Preference and Utility Theory. (Johns Hopkins University Press, Baltimore, MD, 1988).

[13] S. French, Calibration and the Expert Problem, Management Science 32, No. 3 (1986) 315–320.

[14] R. Brent Gallupe, Gerardine DeSanctis and Gary W. Dickson, Computer-Based Support for Group Problem Finding: An Experimental Investigation, MIS Quarterly 12, No. 2 (1988) 277–296.

[15] George P. Huber, Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques. DSS-82 (1982) 96–108.

[16] Amy L. Hughes, Daniel H. Webb, A Comparative Study of GDSS Use: Empirical Evidence and Model Design (Naval Postgraduate School, Monterey, CA, 1987).

[17] Sirkka L. Jarvenpaa, V. Srinivasan Rao and George P. Huber, Computer Support for Meetings of Groups Working on Unstructured Problems: A Field Study, MIS Quarterly 12, No. 4 (1988) 645–666.

[18] M. Tawfik Jelassi and Renée A. Beauclair, An Integrated Framework for Group Decision Support Systems Design, Information and Management 13 (1987) 143–153.

[19] Ralph L. Keeney and Howard Raiffa, Decisions with Multiple Objectives (Wiley, New York, 1976).

[20] Gregory E. Kersten, NEGO - Group Decision Support System, Information and Management 8 (1985) 237-246.

[21] Kenneth L. Kraemer and John Leslie King, Computer-Based Systems for Cooperative Work and Group Decision Making, ACM Computing Surveys 20, No. 2 (1988) 115–146.

[22] Ting-Peng Liang, Model Management for Group Decision Support, MIS Quarterly 12, No. 4 (1988) 667-680.

[23] Dennis V. Lindley, Another Look at an Axiomatic Approach to Expert Resolution Management Science 32, No. 3 (1986) 303–304.

[24] Kathleen E. Moffitt, Computer Support for Group Decision Making: An Overview, Technical report No. 88-2 (Decision Systems Research Center, Arizona State University, Tempe, AZ, 1988).

[25] P.A. Morris, An Axiomatic Approach to Expert Resolution, Management Science 29, No. 1 (1983) 24–32.

[26] Peter A. Morris, Observations on Expert Aggregation, Management Science 32, No. 3 (1986) 321–328.

[27] J.F. Nunamaker, Lynda M. Applegate and Benn R. Konsynski, Computer-Aided Deliberation: Model Management and Group Decision Support, Operations Research 36, No. 6 (1988) 826–846.

[28] Mark J. Schervish, Comments on Some Axioms for Combining Expert Judgments, Management Science 32, No. 3 (1986) 306–311.

[29] Jill Y. Smith and Michael T. Vanecek, Computer Conferences and Task-Oriented Decisions: Implications for Group Decision Support, Information and Management 14 (1988) 123–132.

[30] David Sutherland and Robert Crosslin, Group Decision Support Systems: Factors in a Software Implementation, Information and Management 16 (1989) 93–103.

[31] Kazuo Watabe, Clyde W. Holsapple and Andrew B. Whinston, Coordinator Support in a Nemawashi Decision Process, Decision Support Systems 8 (1992) this issue.

[32] Richard T. Watson, Gerardine DeSanctis and Marshall

Scott Poole, Using a GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences, MIS Quarterly 12, No. 3 (1988) 463–477.

[33] Howard J. Weiss and J. Yael Assous, Reduction in Problem Size for Ranking Alternatives in Group Decision-Making, Computations Operations Research 14, No. 1 (1987).

[34] Robert L. Winkler, Expert Resolution, Management Science 32, No. 3 (1986) 298–302.

[35] Ilze Zigurs, M. Scott Poole and Gerardine L. DeSanctis, A Study of Influence in Computer-Mediated Group Decision Making, MIS Quarterly 12, No. 4 (1988) 625–644.
