---
otero_id: 17140
otero_key: "BGKKVBM5"
title: "On the evaluation of heuristic information systems"
authors: "Bengt G Lundberg"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90018-m"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Evaluation of Heuristic Information Systems \*

Bengt G. LUNDBERG

Department of Computer and Systems Sciences, University of Stockholm, S-106 91 Stockholm, Sweden

The concept of heuristic information systems is introduced and discussed with respect to the properties and use of heuristic systems. The concept of heuristic information systems includes the concepts of expert systems and information retrieval systems. The conceptual framework used in the evaluation of information retrieval systems is applied to two published cases of expert systems evaluation. An analysis of the results shows that the two types of systems have similar performance characteristics in the chosen framework.

Keywords: Information systems, Heuristics, Models.

![](/api/attachments/BGKKVBM5/fulltext/images/daf778a264d2b7c3dfa2493c314e3400d4bbf934918f7b1e2b5ab66fd474fec7.jpg)

Bengt G. Lundberg is associate professor at the department of computer and systems sciences, University of Stockholm, Sweden. Lundberg received his Ph.D. from the Royal Institute of Technology, Stockholm, in 1982. His research interests have been in the areas of conceptual modelling and heuristic-based systems for decision support.

\* This work is supported by the National Swedish Board for Technical Development (STU).

## 1. Introduction

The introduction of heuristic-based information systems, such as expert systems and user-developed model-based systems, in practical contexts has stressed two important aspects of applied computer science, namely methodologies for incremental development of systems and methodologies for evaluation of the effectiveness of systems. These two aspects are important as the systems are intended primarily for user-developed computer-based systems that are applied to unstructured problems, or tasks, in which the data processing is controlled by the user's rules of thumb in solving a problem, or performing a task.

In this paper we will discuss a suitable conceptual framework for the evaluation of heuristic information systems. The methodology is primarily based on, and inspired by, the results presented in the area of information retrieval $[1,2]$ . In that research area long since experiences have been established concerning the evaluation of the effectiveness of retrieval systems and a conceptual framework for the evaluation of information retrieval systems has been accepted among the researcher (though not being completely satisfying, e.g. $[2]$ ).

In section two, we will present a definition of heuristic information systems and characterise some of their important properties and aspects. As a basis for the discussion a rule-based formalism for representing reasoning processes will be used [3]. The problems that are identified concerning the evaluation of heuristic information systems will be discussed in section three together with a comparison and discussion of results from information retrieval. In that section some empirical studies of expert systems/knowledge-based systems performance are also reviewed.

## 2. Heuristic information systems

A heuristic information system is defined here to be a system in which the processing of information is controlled by the rules of thumb supplied by a user. As will be shown, this implies that a heuristic information system is indeterministic in the sense that the results can be incomplete as well as redundant with respect to the expected result (“the relevance criterion”). Thus, according to the above definition, we assume that a user is supplying a process description and that this description represents the reasoning processes which are performed by the user when solving a problem or performing a task. The rules which a human being follows when performing an unstructured task are usually referred to as rules of thumb and thus represent the heuristics that are applied in a problem-solving process. These rules of thumb have the important properties of being imperfect in the sense that they in most cases lead to satisfying results, but may also give results that are worse than useless. Furthermore, the very process of representing/formalizing the rules of thumb of a human being introduces further ambiguities which makes the data processing, which is controlled by the formalized rules, even more difficult to anticipate and to predict the results with respect to relevance. It follows that the results obtained from such a system must be inspected by a human being in order to determine the veridicality of the results, i.e. the system must be used as an “advisory system” which can support a user in performing a task and, thus, should not be used as an autonomous task-performing system.

Example 1: Consider the following set of rules representing the rules of thumb of a human being when deciding how to go to work:

"take a taxi if it is winter and it is raining"

"take a tram if it is raining"

which we formalize as

$$
\begin{array}{l l} \text {   Winter   and   Raining   } & \Rightarrow \text {   Taxi   } \\ \text {   Raining   } & \Rightarrow \text {   Tram   } \end{array}
$$

assuming the following three situations we arrive at the respective sets of conclusions:

<table><tr><td>Winter</td><td>Raining</td><td>Raining Winter</td></tr><tr><td>/</td><td>Tram</td><td>Tram Taxi</td></tr></table>

The rules of example 1 specify the reasoning process which is applied when solving a problem. The properties of the results of the process differ depending on the situations to which the process description is applied. Considering the left column of example 1 one can argue in two ways, namely that the process has been applied to an irrelevant situation or that the rules fail in that case as no results are deduced. Correspondingly, in the right column we arrive at a redundant result, and assuming that the results are not obviously contradictory a resulting ambiguity is not resolved. The middle column of the example thus must also be considered from those two points of view, namely that the result is incomplete and redundant.

When applying a heuristic system in practical cases the authority of the user and the degree of confidence in relevance of the system must be considered. From the above example it follows that the results of a heuristic system must be completed with judgements by the user, obviously when the results are assumed to be redundant or incomplete. The authority of a user can be considered to be of the following three types:

\- no authority to make choices; i.e. the result of the system is considered as a definite, and veridical, decision to be implemented. In this case the system is used as a decision making system.

\- authority to make a choice among an enumerated set of alternatives (i.e. it corresponds to the right case in the example above). In this case the system is used as an alternative-generating system.

authority to make a choice autonomously; i.e. the results of the system are considered as one source of information in making a decision. In this case the system can be considered as a decision supporting system, or as an alternative-proposing system.

The formal computerized system is effectively deterministic in the sense that a given process description (algorithm) and a given initial set of data the system will produce a specific set of resulting data. However, considered from an application point of view the system will produce results which are to be considered from the relevance point of view. The deficiencies of the results of a system can depend as well as on the process description as on the data to which the process description is applied.

## 3. Evaluation of heuristic information systems

In this section we will discuss the application of some effectiveness measures that have been developed and used in the research area of information retrieval, e.g. [2]. Further, we will review some empirical investigations of expert systems/knowledge-based systems and relate these results to those achieved in the area of information retrieval.

## 3.1. Effectiveness in information retrieval systems

In the research area of information retrieval the focus of interest has been concerned with the effectiveness, and to less degree with the efficiency, of information retrieval systems (in bibliographic applications). The typical scenario of an information retrieval application is that given a document database, or an index database, a request (query) is stated using a search language in order to get references to the bibliographic entities, in the database, on the topic as specified in the request. Effectively, in the system a match is performed between the request and a document description, the latter being represented by an index vector. The request and the document are considered to refer to the same topic, if the request and the index vector are sufficiently identical. Thus, the formal process taking place in an information retrieval system creates a mapping from the request to the index vector (which simply gives a type of name to the document). The not fully formalized process taking place in this context concerns the mapping from the information requirement to the query and, respectively, the mapping from the documents to the index vectors. Alternatively, you can consider the index vector and the request to be the formalized representations of concepts being informally represented, or an idea of a user. The general scheme of the information retrieval process becomes as outlined in fig. 1. The effectiveness of the system can be considered from two points of view:

![](/api/attachments/BGKKVBM5/fulltext/images/843671cbccc8022f661344acf99d96535bea84150fcab6d6d9876557ed84067c.jpg)  
Fig. 1. The general scheme of information retrieval systems.

![](/api/attachments/BGKKVBM5/fulltext/images/fc1aa0e7f1218a0b35192ce922138ed32338870a1e15a0a9194f12c757f687e1.jpg)  
Fig. 2. Precision-recall values for information retrieval systems, database systems, a medical diagnosis system and a research funding system.

\- the database view; according to which the important aspect is that the intended match is achieved between a request and a set of index vectors (i.e. we consider the mapping between two formal entities)

\- the information retrieval view; according to which the important aspect is that the intended mapping is achieved between an information requirement and an intended set of documents.

The match process thus maps the formalized information requirement to a number of documents in the database, which is the set of retrieved documents. In the set of retrieved documents some are relevant with respect to the information requirement. Further, the set of retrieved documents that are found relevant is a subset of the set of relevant documents stored in the database. In the area of information retrieval the following definitions are introduced in order to characterize the effectiveness of a system, e.g. [2]:

recall: the ratio between the number of retrieved relevant documents and the number of stored relevant documents
precision: the ratio between the number of retrieved relevant documents and the number of retrieved documents.

An ideal system is a system in which the recall and precision values are both 1.0 (100%), which in fact is an assumption made in traditional database systems (see fig. 2). However, empirical data shows that the performance of the best information retrieval systems is approximately as shown in fig. 2 (e.g. [4]). It follows that the relationship between precision and recall in information retrieval systems can be characterized roughly by the equation precision = -recall + 1.0

in the middle of the recall interval 0.0 to 1.0.

In traditional data processing systems, e.g. database systems, the assumption is made that the processing system is complete in the sense that a data request always returns all relevant data and nothing else. In other words the problem is considered to be well-structured. In the context of information retrieval systems we have to cope with the ambiguities introduced by the mappings between requirements and queries as well as between index vectors and documents. Thus, we have to consider the retrieval problem to be only partly structured.

## 3.2. A classification expert system

As one part of study on expert system design the performance of an expert system has been investigated [5]. The study concerns the expert system SEEK in which the disease of a patient is determined from a set symptom, i.e. the system creates a mapping from a set of symptoms to a stored disease description. When evaluating the system it is supplied with sets of symptoms and the system determines the corresponding disease. The correctness of the constructed mapping is compared with the diagnoses given by medical experts. The data from the empirical investigation are here given in extensio (except for the names of the deseases, cf. [5]) in table 1.

In the empirical evaluation a total of 121 cases were used of which 89 were correctly diagnosed and 19 were given a false diagnosis (the rest is assumed to give no diagnosis, as the paper does not say what the result is).

Table 1  
Results from a medical diagnosis system.

<table><tr><td>Desease</td><td>Percentage</td><td>Correct result</td><td>False positives</td></tr><tr><td>1</td><td>27%</td><td>(9/33)</td><td>0</td></tr><tr><td>2</td><td>100%</td><td>(42/42)</td><td>9</td></tr><tr><td>3</td><td>67%</td><td>(12/18)</td><td>4</td></tr><tr><td>4</td><td>96%</td><td>(22/23)</td><td>5</td></tr><tr><td>5</td><td>80%</td><td>(4/5)</td><td>1</td></tr><tr><td>Average</td><td>74%</td><td>(89/121)</td><td>Total 19</td></tr></table>

The concepts of precision and recall are not appropriate to apply in this case because to each set of symptoms (which correspond to a request) at most one diagnosis is derived. The average recall over the 121 cases is calculated to be 74%. The average precision is calculated to be 82%, i.e. $89/(89 + 19)$ . However, it should be noted that these latter values are calculated after summing the individual cases and not the average of the recall values, respectively precision values. When these values are introduced in the precision-recall diagram (see fig. 2) we find that the effectiveness is much better than for the results obtained in an information retrieval system. The reason for the difference in retrieval effectiveness is probably that in the domain of the medical application the involved experts are well-trained in the comparatively formalized domain, e.g. symptoms and diagnosis are extensively specified in medical training books (compared to individually constructed concepts of users when requesting bibliographic documents).

## 3.3. A knowledge-based retrieval system

An interesting example of the application of ideas from several disciplines is the GRANT system [6]. The GRANT system is a so called knowledge-based system for searching funding agencies, for research proposals, in a “catalogue” in which the agencies are characterized with respect to the kind of research they support. The search method is supported by a semantic net representing the relationships between concepts used in the description of the research areas. The semantic net can be considered to have at one end the descriptions of the funding agencies and at the other end the descriptions of project proposals. An inference engine then searches the semantic net from project proposals to funds according to a search strategy. In GRANT three different strategies are used

BF: a breadth-first strategy, restricted to 4 links depth and avoiding nodes with “extremely high fan-out”.

UKW: unconstrained keyword search, i.e. a project proposal and an agency must have an immediate relation to a common concept (i.e. only two links are involved).

Table 2  
Results from the GRANT system.

<table><tr><td></td><td>BF</td><td>UKW</td><td>BC</td></tr><tr><td>Retrieved</td><td>2145</td><td>164</td><td>305</td></tr><tr><td>Retrieved relevant</td><td>132</td><td>58</td><td>88</td></tr><tr><td>Relevant</td><td>132</td><td>132</td><td>132</td></tr><tr><td>Precision (%)</td><td>6</td><td>36</td><td>29</td></tr><tr><td>Recall (%)</td><td>100</td><td>44</td><td>67</td></tr></table>

EC: endorsement constrained search; according to this strategy the search is controlled by knowledge about how agencies usually support projects. An example of this kind of knowledge is that funding agencies support research on topics that are specializations of their main research area for support.

In GRANT about 700 agencies are represented and in the evaluation of the system 27 proposals have been used. The results of the searches have been evaluated by experts and the results of the evaluations are as shown in table 2 [6].

Here it should be noticed that the set of relevant funds is determined from the breadth-first search, which due to its rather unrestricted strategy, cf. above, is assumed to retrieve all the relevant funds (though, of course, with very low precision). Further, the data presented above are also sums over a number of cases for which precision and recall values are calculated. By inserting the precision-recall value pair in the precision-recall diagram (see fig. 2) we find that the results found in the GRANT system, for the respective search method, are similar to those found in the area of information retrieval.

## 3.4. Comments

In the preceding sections we have presented the cases on the evaluation of heuristic-based systems. From the examples one finds that the performance of the GRANT system is comparable with the performance of information retrieval systems. However, the performance of the medical diagnosis system is better than in the other two cases. This observation can be explained by the fact that in the medical diagnosis case the domain of the system is rather well-structured and that the employed concepts are established in the literature on the specific topic. In information retrieval contexts, as well as in the research funding case, the descriptions, and classifications, are based on the concepts used in the respective documents. We can also observe a difference in objectives between the systems. In information retrieval systems, and also in the GRANT system, irrelevant items are accepted among the results and thus we can consider these systems to be decision supporting systems in the sense that the user has to make the final choice. In the medical diagnosis system SEEK the focus of the evaluation concerned the relevant results only (i.e. one correctly concluded desease for each set of symptoms) and the objective is to arrive at methods for eliminating incorrectly concluded deseases. Thus, the objective is to arrive at a decision making system.

Considering the presented systems and the discussion on authority of users in section 2 we find that we can consider two types of systems, namely: - systems in which not relevant alternatives are acceptable (and, these are possibly refused by the user)

\- systems in which only relevant alternatives are acceptable

In the former case we must assume that the user is able to distinguish negatively-valued alternatives from positively-valued alternatives, besides being able to, at least to some extent, rank alternatives. In the latter case the domain must be structured to the extent that the corresponding (formalized) system distinguishes positively-valued alternatives from negatively-valued alternatives. Correspondingly, we can identify three types of qualities of systems with respect to the precision/recall-measures of the systems, as follows:

(1) decision-making systems, which must have perfect precision and recall, i.e. precision = 100% and recall = 100%.

(2) alternative-generating systems, which may have a recall value less than 100% (and precision = 100%).

(3) alternative-proposing systems, which may have recall as well as precision less than 100% (including the case that no alternatives are proposed).

## 4. Some problem aspects.

The basic problem in information retrieval, and in other heuristic information systems, is the specification of the mapping between cause and effect of an information process. The mapping can be considered to be of the type

![](/api/attachments/BGKKVBM5/fulltext/images/0b090f4acb551d1c287b8023fa6abba0664e9996ca99af99874695465fed5481.jpg)  
Fig. 3. Mapping at the conceptual level and the symbol level.

## $\mathbf{A} \Rightarrow \mathbf{B}$ ,

where the symbols A and B refer to concepts (e.g. as concept are described in free-text queries or free-text documents). However, the symbols represent concepts which we assume cannot be completely described. Thus, what we are considering is the intended mapping between a concept $C_{A}$ and a concept $C_{B}$ , which in a formal model are represented by the symbols A and B, respectively. This can be illustrated as in fig. 3 by introducing a concept level and a symbol level.

The work of M. Polanyi [7] focus on the tacit dimension of human knowledge. The basic assumption made states that human beings are not able to articulate all their knowledge (and thus are not able to explicitly represent it in a formalism).

The obvious case appears when a human being has two, similar, concepts $C_{A'}$ and $C_{A''}$ and in situations to which these apply associates concepts $C_{B}$ and $C_{C}$ respectively. However, the underlying rules are articulated, and are represented as

$$
\mathbf {A} \Rightarrow \mathbf {B}
$$

$$
\mathbf {A} \Rightarrow \mathbf {C}
$$

According to the formalized rules a conflict appears concerning which action to perform when the pre-misses are satisfied. In order to resolve the conflict, the arguments $k_{1}$ and $k_{2}$ can, in principle, augment the rules giving the refined rules

$$
\mathrm{A}, \mathrm{k} _ {1} \Rightarrow \mathrm{B}
$$

$$
\mathbf {A}, \mathbf {k} _ {2} \Rightarrow \mathbf {C}
$$

Here we find that by restricting the applicability of the rules we arrive at a rule system with improved precision ratio. Correspondingly, by broadening the concept of the premisses we arrive at systems with higher recall values, see also [4]. Thus, a heuristic system can to some extent be tuned by the use of concept hierarchies, such as ISA-hierarchies [3], in which the concepts that are applied are chosen with respect to the desired precision/recall-ratio. However, these measures do not imply that the overall performance of a system will be improved.

The idea of tacit knowledge, as it is presented above, concerns independent variables which are tacitly considered when solving a problem (or making a decision) and which primarily have implications in the selection of alternatives. Such cases are frequent, in particular, in administrative decision making as often all relevant variables, and problem aspects, are not known in advance.

In technical problem-solving the set of independent variables are usually closed, e.g. in diagnosing the faulty components of a device. In such cases the mapping between the independent and the dependent variables can, at least in principle, be enumerated explicitly. However, when the number of independent variables is large and their interactions are complex it becomes difficult, or impossible, to construct an exhaustive representation. The problem then concerns the construction of a partial tentative mapping which can produce advices for action, e.g. proposing possible faulty components. Methodological knowledge on the construction of the mappings between independent and dependent variables is today to large extent incomplete.

## 5. Conclusion

In this paper we have introduced the concept of heuristic information systems, which is considered to include the concepts of expert system and information retrieval systems. Further, we have applied the evaluation methods used in the area of information retrieval to analyse two published evaluations of expert systems/knowledge-based systems and have found the performances of the systems to be of the same level of effectiveness. The identified and outlined properties of heuristic information systems are explained within a tentative model based on the idea of tacit knowledge of human-beings.

## References

[1] F.W. Lancaster, E.G. Fayen: Information Retrieval On-Line, Melville Publ. Comp., 1973.

[2] G. Salton, M.J. McGill: Introduction to Modern Information Retrieval, McGraw-Hill Inc., 1983.

[3] E. Rich: Artificial Intelligence, McGraw-Hill, New York, 1983.

[4] G. Salton: Another look at automatic text-retrieval systems, Communications of the ACM, Vol 29, no 7, 1986.

[5] P. Politakis, S.H. Weiss: Using empirical analysis to refine expert systems knowledge bases, Artificial Intelligence, Vol 22, pp 23–48, 1984.

[6] P.R. Cohen, R. Kjeldsen: Information retrieval by constrained spreading activation in semantic networks, Information Processing & Management, Vol 23, no 4, pp. 255-268, 1987.

[7] M. Polanyi: Personal Knowledge: Towards a Post-Critical Philosophy, University of Chicago Press, Chicago, 1962.
