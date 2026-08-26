---
otero_id: 5680
otero_key: "2Y4RFUZA"
title: "Social software for business process modeling"
authors: "Agnes Koschmider; Minseok Song; Hajo A Reijers"
year: "2010"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2009.21"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# Social software for business process modeling

Agnes Koschmider<sup>1</sup>, Minseok Song<sup>2</sup>, Hajo A Reijers<sup>3</sup>

<sup>1</sup>Institute of Applied Informatics and Formal Description Methods, Karlsruhe Institute of Technology, Germany; <sup>2</sup>Institute of Public Policy and Information Technology, Seoul National University of Technology, South Korea; <sup>3</sup>School of Industrial Engineering, Eindhoven University of Technology, the Netherlands

Correspondence:

Fax: þ 49(0) 721 608 4548;

E-mail: agnes.koschmider@kit.edu

## Abstract

Formal models of business processes are used for a variety of purposes. But where the elicitation of the characteristics of a business process usually takes place in a collaborative fashion, the building of the final, formal process model is done mostly by a single person. This article presents the design and implementation of a Recommendation-Based Process Modeling Support System with ‘social features.’ A process builder using this system will receive recommendations to complete or edit a formal business process model on the basis of previous usage of modeling fragments by her peers. Such features potentially improve the modeling process and, as such, the modeling outcome, that is, the quality of the process model. This article also contains an evaluation of the system’s usage and effectiveness, which builds on an experimental design. It is shown that process builders are inclined to follow up on the provided recommendations and that this will improve the semantical quality of the created model. However, information on peer usage of modeling fragments does not play a big role in selecting the recommendations being followed up. This article fits within a stream of research that puts emphasis on the modeling process, rather than on the model artifact. Journal of Information Technology (2010) 25, 308–322. doi:10.1057/jit.2009.21

Published online 20 July 2010

Keywords: business process models; recommender systems; social networks; process modeling support

## Introduction

n past years, the mapping of business processes in the form of process models has become the primary form of conceptual modeling (Davies et al., 2006). A business process model captures elements, typically in some graphical form, such as the activities that constitute the business process; the performers of these activities; the time, location, and modus of their execution; and the information that is processed. Process models are being widely used in the development of organizational structures (Wastell et al., 2006), information systems (Dumas et al., 2005), service-oriented architectures (Erl, 2005), and web services (Ferris, 2003).

Even with substantial numbers of practitioners modeling processes, with vendors such as Lombardi, IDS Scheer, and Pallas Athena providing the commercial tools to do so, and with a very active and expanding research community studying process models and languages, there is still reason to worry about the fate of this type of conceptual modeling.

In a research commentary, Wand and Weber argue that any form of conceptual modeling often falls into disuse by practitioners after an initial period of excitement (Wand and Weber, 2002). This view is confirmed by a wide range of empirical studies and anecdotal evidence (e.g., Batra and Marakas, 1995). Indeed, it has been noted that the success of process modeling efforts has already become a critical concern (Bandara et al., 2005) and that there are indications that practitioners struggle with various process modeling aspects and find limited support from academic literature in guiding their efforts.

To avert the potential downslide of process modeling, we believe that it takes an approach that is distinctly complementary to the focus on the process model artifact itself, which is so characteristic for much of the current research into process modeling. For example, one dominant stream of research (Sadiq and Orlowska 2000; van der Aalst and ter Hofstede, 2000) is concerned with the development of analysis techniques that can be used to detect different types of syntactical mistakes in a process model, but does not guide the modeler towards avoiding such mistakes. In line with Bandara et al. (2005), van Bommel et al. (2006), Rittgen (2007), we subscribe to the view that a focus on the modeling process is called for, paying attention to the actual decisions that modelers have to make to arrive at a process model that supports the efficient and effective development of a business or IT system. The soundness of this view is supported by a survey on conceptual modeling (Batra and Marakas, 1995) which concludes that it is precisely the lack of interest from the academic community for the act of data modeling that is missed by practitioners and has led to their decline of interest in it. The open question that we address in this article is how an individual modeler can be supported in creating a high-quality business process model.

Against this background, we present a system that supports the modeling process by providing recommendations to a process modeler. The recommendations consist of process model fragments that are deemed suitable for that modeler to complete a business process model that she is working on. To do so, the recommendation system takes into account a process builder’s modeling intention and uses a repository of process parts for composing recommendations. The recommendations that are provided by such a system are extended with a trust mechanism, based on the social context of the model builder. Heider’s famous ‘balance theory’ (Heider, 1958) suggests that individuals are more prone to interact with friends of friends rather than with unknown peers. Following this line of argument, process builders may also be willing to select recommendations that are based on decisions by known (skilled) persons, in contrast to unknown ones. Both features – the recommendations and the trust mechanism – are aimed at supporting the process builder in such a way that the quality of her modeling effort is positively affected and, as such, its outcome the formal process model.

Our most tangible contribution is that we show how the existing version of a recommendation-based modeling support system (Hornung et al., 2008) can be extended with capabilities to take social information into account. We describe in detail how the social networks can be gathered from the recorded history of the system’s usage, which consists of the name of the selected recommendation and the performer (users that selected a specific recommendation). When a modeler creates a new process, the modeling history of others who are close to the user can then be exploited. Additionally, we provide empirical indications for the willingness of process builders to follow up on such recommendations in creating a process model and, when they do, whether social information is relevant in choosing between the suggested alternatives. At a more abstract level, the contribution of this article is that it strengthens a research stream into process modeling that is more concerned with the modeling process than the model artifact. While both views have their merits, we believe that the ‘process-centered’ stream is underdeveloped, which – as we argue – can have serious ramifications for the field as a whole. Just as with the stream of ‘artifact-centered’ research, our approach fits into the design science research tradition of the IS field (Hevner et al., 2004), as it creates and evaluates an IT artifact intended to solve identified organizational problems. However, because we aim to affect and improve the actual decisions that modelers make, we are also duly concerned about the effectiveness of that artifact in that respect. This is the focus of the experimentation with our system described in this article.

The structure of the article is as follows. We first provide a section with background information on the problem context, aimed at the reader who is less familiar with the domain of conceptual modeling and process modeling in particular, and then provide a summary of works related to our approach. In the subsequent section, we sketch the functionality of the recommendation-based process modeling support system, after which the generation of social network structures is explained in detail in the next section. The design and results of our experiment to evaluate the use of the recommendation system is presented in the penultimate section. The article ends with conclusions and a reflection.

## Background

## Problem context

As mentioned in the introduction, business process modeling – also referred to as process mapping – is a special form of conceptual modeling. The article by Curtis et al. in 1992 is often seen as the rough birth date of the discipline. In this article, the authors describe how the research on process modeling evolved from an interest of software organizations to improve their development processes. The clarity of insight that graphical process models provided was considered very helpful for that purpose. Since then, process modeling has been applied in diverse domains, such as manufacturing (Elzinga et al., 1995), the service industry (Reijers, 2003), and healthcare (Liaw et al., 2006), for the development of a range of business and IT systems. The overview in Kettinger et al. (1997) covers a large variety of process modeling techniques halfway through the 1990s. Today, that supply has widened rather than diminished, with some of the most popular techniques being Eventdriven Process Chains (EPCs) (Scheer, 1998), the Business Process Modeling Notation (BPMN) (OMG, 2008), the Activity Diagrams in the UML family (Dumas and ter Hofstede, 2001), and workflow nets (van der Aalst, 1998). Dominant research streams are concerned with the verification of process models (Sadiq and Orlowska, 2000; van der Aalst and ter Hofstede, 2000) and the use of process models for process execution support (Georgakopoulos et al., 1995; Reichert and Dadam, 1998), while industrial efforts seem most concerned with standardization issues.

Various authors have accentuated the cooperative and communicative aspects of creating a conceptual model and a process model in particular. According to Hoppenbrouwers et al. (2005, 2006) and van Bommel et al. (2006), this act involves two related dialogues. The elicitation dialogue takes place between an informer (presumably a domain expert) and a model mediator (typically an information analyst). The formalization dialogue, on the other hand, takes place between the model mediator and the model builder (usually some tool is used to capture and verify the actual model). This view is congruent with the phases described in Frederiks and van der Weide (2006): An analyst interacts in an iterative fashion with domain experts to arrive at an informal model, which is then concretized into a complete formal specification.

Crucial for the motivation of this work is the following observation. While the elicitation phase is commonly recognized as a collaborative effort, the formalization dialogue is mostly a solitary activity, requiring specific skills. In other words, the model mediator typically also builds the model. According to Rittgen (2007), the few available descriptive studies on process modeling support the scenario of a single expert modeler who creates a formal model of some part of a business. Indeed, the available business process modeling tools on the market today are mostly ‘one-person tools’, that is, (1) they assume that only one modeler is changing the model at any point in time (Rittgen, 2008), and (2) the created models are not reused and further assembled in IT implementation projects (Thom et al., 2008). The former factor potentially results in dissatisfaction of business users with current IT implementations because of missing, sketchy or otherwise inadequate content. The latter factor directly affects the economic risk of projects involving process modeling, with the wheel being re-invented time and time again.

Our work can be seen as relevant within the wider discussion of how IS methods and tools contribute to successful IS development. While vendors of tools often do not adequately understand the needs of IS development organizations, there is a lack of research that considers tool support in the light of the recognition of the concept of ‘method in action’ (Lundell and Lings, 2004). The focus of the dominant streams of research on process modeling that we referenced is on the process artifact, while we feel that tools that support the decision-making process during the actual modeling process should also be considered.

## Related work

Existing work that is relevant to this article’s subject can be differentiated into five categories: (1) Social network analysis, (2) recommender systems, (3) web service composition, (4) process reuse, and (5) process modeling support.

## Social network analysis

The study of social network analysis has attracted the interest of scientists from different fields such as: (1) sociology (Watts, 1999), (2) psychology (Kenny and LaVoie, 1984), (3) economy (Tichy et al., 1979), and computer science. In the computer science field the studies related to our approach are using social networks as a method for communicating trust or distrust, (Golbeck, 2005; Guha et al., 2004), propagating changes (Mason et al., 2008) or analyzing interpersonal relationships in an organization (Barnes et al., 1998; van der Aalst et al., 2005).

## Recommender system

Various types of recommender systems can be distinguished. A content-based recommender system (Basu et al., 1998) suggests an item to a user based upon a description of the item and the user’s interests in the past. This kind of recommender system has its roots in the information retrieval (IR) community (Baeza-Yates and Ribeiro-Neto, 1999) and suggests items containing text documents, websites, or movies. Collaborative recommender systems (Herlocker et al., 2004) predict what a user wants based on what she and people with similar preferences preferred in the past. The focus of this kind of system is the similarity calculation of users rather than of items (as in contentbased systems). The combination of content-based and collaborative-based recommender systems is termed a hybrid recommender system (Burke, 2002). The recommendation-based modeling support system, described in the article, can be regarded as a specific type of a hybrid recommender system which incorporates some features of content-based and collaborative-based systems (Koschmider and Oberweis, 2009).

## Web service composition

Many related approaches focus on a composition of Web services (e.g., (Milanovic and Malek, 2004)) or Web services that are semantically enriched (e.g., (Schaffner et al., 2007; Born et al., 2008). Especially the second type of results (semantically enriched services) uses well-defined knowledge representation languages in order to support automated search capabilities or information analytics (Nagarajan, 2006). However, the limitations of these approaches are that preliminary work is required to build up a (background) ontology in order to use semantic technologies and insufficient quality metrics are provided to describe the usefulness of recommendations that ease the service selection. In the next section we sketch our techniques for the usefulness of recommendations.

We believe that a semi-automatic composition of web services is much easier than the composition of business processes (the recommendation of appropriate process model parts with a process model part being edited can be regarded as a process composition). Usually, web services are considered to be black-boxes where no knowledge about the user’s modeling purpose, perspective, role, or history is required.

## Process reuse

Several authors have proposed methods for process model reuse (Kim et al., 2002; Madhusudan et al., 2004), albeit with little impact on the modeling context and user’s modeling intention and requirements. None of these solutions proposes techniques that will enable the user to finish her design most efficiently.

## Process modeling support

The initial idea of a recommendation-based process modeling support has been described in Koschmider (2007). In practice, we realized that the recommendation engines often suggested process parts that dealt with the desired process but which were actually modeled for a different purpose. Therefore, we extended the recommendation system by taking the modeling perspective into account (Koschmider et al., 2008).

Based upon these extensions of the modeling support system, this article presents a technology for Web 2.0 which plays an important role by enabling new forms of information sharing and exploitation of social relationships. We note that the generation of a social network from recommendation history requires consideration of more relationships than in the enumerated related works in the field of social network analysis.

## Recommendation-based process modeling support

A recommendation-based process modeling support system (Koschmider, 2007; Hornung et al., 2008) suggests process builders fitting processes regarding the builder’s modeling intention and modeling history of a community of users. This recommendation system implementation embeds two types of modeling support in order to achieve the user’s modeling intention:

1. A query interface allows users to request process models or process model parts that are of interest to them. We define a process model part as a logically coherent group of process elements belonging together (e.g., approval, billing, or shipping).

2. A recommender component proposes appropriate process model parts which fit to a business process model that is currently being edited. The user can invoke the recommender component by highlighting the corresponding element group to be completed by process reuse. This component of the modeling support should be used if the user is not sure how to complete the process. In this case the results from the query can be unsatisfying due to the process builder’s vague intention of the process model.

However, when the recommendation system has been invoked the process builder can configure the process model (part) suggestions in her workspace by inserting or deleting process elements. Subsequently, the process builder can store the modified process version in a process repository for further process reuse.

Before making models and model parts searchable, we need to index them. Process model parts are handled in the same way that the complete models are handled, but additionally, we store a pointer to the business process model with which they are associated. For example, for a business process which consists of three distinct process model parts, we would include four virtual documents in our index: the whole process and each of the three parts.

After indexing the processes users can use the query interface which uses Lucene’s query parser syntax (http:// lucene.apache.org/java/docs/queryparsersyntax.html), and users can enter seven query arguments:

\- Title: referring to names of process elements (e.g. approved request)

\- First element: searching for a specific first element(s) in the process model

\- Last element: searching for a specific last element(s) in the process model

\- Property: referring to specific properties of a process model assigned by users before storing the process in the repository (e.g., standard signifies a standard process)

\- Purpose: referring to models fulfilling one of the four modeling purposes such as analysis, documentation, execution, or reengineering

\- Objective description: searching for processes fulfilling an objective (e.g., processes modeling handling of order request). This field is only searchable if process builders have annotated the process with the corresponding data before storing the model in the repository

\- Previous user selection: searching for a specific user who selected a recommendation.

To overcome a limitation through a controlled vocabulary, we use WordNet (a free English taxonomy, http://wordnet.princeton.edu). With standard Boolean operators, such as AND, OR, and NOT, users can express more complex queries.

Processes that meet process builders’ criteria are displayed first in a table-based result list as depicted in Table 1. The ranking criterion Score reflects the name match between the user’s query and each process model in the repository. The frequency criterion describes how often a process model has been selected/reused by other users, and the average number of insertions and deletions describe the number of operations made when selecting a recommendation. To encourage process builders’ trust and participation by those process builders who are unskilled in process modeling, we extended the table-based result by one more criterion, which indicates the names of persons who selected a recommendation (Previous User).

We consider these ranking criteria as our ‘metrics’ for usefulness of recommendations. In several empirical designs we discovered that a high match between the user’s query input and the recommendation (in our context reflected by the criterion Score) was the greatest influence factor for selecting a recommendation. Therefore, we assigned the greatest weight for the Score criterion in our overall ranking of recommendation results.

When double clicking on recommendation(s) in the table-based view a graphical-based visualization of the process will be opened, as shown in Figure 1. In the example the user query returns 10 suggestions for processes or process model parts, while Figure 1 shows two of them.

In Figure 1 the process builder can preview related process model parts for each recommendation (see Show related process model parts). The idea is that process model parts that succeed or precede the part in question and which are used in the same modeling domain that the process builder is in at the moment (e.g., Manufacturing) can help to estimate the degree of fitness of a recommended part.

By pushing the button Show related process models, the user can preview all phases of the BPM life-cycle, from the early documentation of a process through subsequent phases of analysis and execution. To realize the functionality of previewing related process models, we construct a user profile based on the respective search history (Koschmider et al., 2008).

Table 1 Extended table-based result list with previous user selection

<table><tr><td>#</td><td>Process name</td><td>Score</td><td>Frequency</td><td>Avg. insertion</td><td>Avg. deletion</td><td>Previous users</td></tr><tr><td>1</td><td>Check order</td><td>95.02</td><td>5</td><td>15</td><td>3</td><td>M. Song</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>10</td><td>Handle orders</td><td>48.85</td><td>3</td><td>20</td><td>4</td><td>A. Koschmider</td></tr></table>

![](/api/attachments/2Y4RFUZA/fulltext/images/7233c235664179b1292afa3fa692e4cf90ea099158266de204b3a68df3f93c27.jpg)  
Figure 1 Visualization of fitting recommendations.

With a right mouse click (in the previous user column), the user can open network structures which were generated from process models or recommendation history. In the next section, we discuss social network-based recommendation support in detail.

## Social network-based recommendation support

This section discusses how to exploit social networks in the context of business process modeling. Three networks can be generated from a process repository and a recommendation system. Table 2 shows the three social networks and their properties.

From a process repository, process model parts are used to derive a social network in which a node represents an organizational unit (e.g., performer or department) in which it is described. Arcs among nodes show the relationship between organizational units, and weight values on arcs indicate the strength of the relationship. This network enables users to consider the fitness between two process model parts in terms of organizational units. The other two networks can be derived from a recommendation system. When users model a business process, two typical behaviors occur. First, process builders select some of the process model parts from the process repository and combine them to make a new process model. However, if they cannot find a proper process model part, they can make a new part by editing an existing one or by combining some parts. A recommendation system can register these kinds of behaviors (i.e., user history, insertion history) and two kinds of networks can be generated from the history. From the user history, a network which shows the similarity between users can be derived. It supports reusing the modeling history of ‘neighborhoods’ in order to faster complete an edited process model. A network from the insertion history shows the insertion structure in terms of users and enables propagating changes of existing process parts across ‘clique’ members.

The remaining section explains how to generate and use the social networks in detail.

Social network from process models

Process models contain information about performers who will execute processes. From this information, social networks among performers can be derived. Before explaining the methods of deriving social networks, a typical process model can be defined as follows.

[Process model] A process model, PM, is a 5-tuple (P, T, F, R, p) where

(i) (P,T,F) is a WF-net (van der Aalst, 1998),

(ii) R is a set of performers,

(iii) p:T-R, that is, performer (R) assignment for a task (T).

The process model extends Workflow nets $( P , T , F )$ with performers (R). In a Workflow net, P, T, and F refer to places, transitions, and flow relations, respectively. The models in the process repository are represented in terms of a Petri net. Activities are modeled by transitions, and causal dependencies are modeled by places and arcs. Performers related to activities are specified in the above transitions.

To generate social networks from the process models, three types of metrics defined in Song (2006) can be considered. They are transfer of work, subcontracting, and cooperation. The transfer of work metrics and the subcontracting metrics take into account causal dependencies (i.e., based on ordering of activities) among performers, while the cooperation metrics consider the occurrence of performers. The causal dependency is defined as follows.

[causal dependency, ) ] Let $P M = \left( P , T , F , R , \pi \right)$ be a process model. For $\stackrel { \cdot } { t } _ { 1 } , t _ { 2 } , \in T , t _ { 1 } \Rightarrow t _ { 2 }$ if and only if path $\left( t _ { 1 } \to t _ { 2 } \right)$ is elementary and $\left( t _ { 1 } , t _ { 2 } \right) \in { \cal F } ^ { 2 }$

path (x-y) if and only if there is a path of nodes in the graph corresponding to (P,T,F). A path is elementary if each node appears only once. If R is a relation, then $R ^ { n } = \{ ( a _ { 1 } , a _ { 3 } ) ^ { * } \in A \times A | \dot { \exists } _ { a _ { 2 \in A } } \Lambda ( a _ { 1 } , a _ { 2 } ) \in R ^ { n - 1 } ( a _ { 2 } , a _ { 3 } ) \in R \}$ and $R ^ { * }$ is the transitive closure.

If $t _ { 1 }$ and $t _ { 2 }$ have a causal dependency, $t _ { 1 }$ is followed by $t _ { 2 }$ in the process model. Within a process model there is a transfer of work from performer i to performer j if there are two subsequent activities where the first activity is assigned to i and the second activity to j. Considering the frequency of transfers, the weight values on arcs between performers can be calculated using the following formula.

$$
\begin{array}{c} r _ {1} > _ {M} r _ {2} = \sum_ {p \in M} (| r _ {1} \Rightarrow_ {p} r _ {2} |) / \\ \sum_ {p \in M} \sum_ {i, j \in p} | i \Rightarrow_ {p} j | \end{array}
$$

$r _ { 1 } > _ { M } r _ { 2 }$ denotes the total number of transfers from performer $r _ { 1 }$ to $r _ { 2 }$ in process models divided by the total number of transfers in the models. Such formula enables deriving a social network among performers, which shows the transfer of works between them.

Subcontracting considers the number of times performer j executes an activity in between two activities executed by performer i. This may indicate that work was subcontracted from i to j. The cooperation ignores causal dependencies and simply counts how frequently two performers participate in activities of the same models. The more often two organizational units work together, the stronger their relation is.

Table 2 Overview of the social networks

<table><tr><td>Source</td><td>Nodes</td><td>Arcs</td></tr><tr><td>Process model</td><td>Org. units</td><td>Strength between org. units</td></tr><tr><td>User history</td><td>Users</td><td>Similarity between users</td></tr><tr><td>Insertion history</td><td>Users</td><td>Insertion history in terms of users</td></tr></table>

![](/api/attachments/2Y4RFUZA/fulltext/images/1fd818a07e8feb5b90d0f659b98e89df8f5ecce0eac5f6d217581a26e27e743a.jpg)  
Figure 2 Social Network from process models.

The social network from process models provides an organizational view of business processes. When a user queries possible candidate process models, the result could show the related social network and analysis results. As an example, the process repository contains five process models as shown in Figure 2. The user is not sure how to continue her business process under construction. She invoked the recommender component in order to be supported by the recommendation system. In the extended table-based result list (see Table 1) she right-clicked on the first network structure alternative and thus the social network opened, as depicted in Figure 2.

In this figure each process model in the repository contains information on performers. The network depicted in the figure is derived by considering the transfer of work between performers. In the network, the nodes refer to the performers in the process models and the arcs show the transfer of work between the performers. For example, since the work is transferred from ‘Ronny’ to ‘Tom’ at the ‘verify customer order 1’ process, an arc between ‘Ronny’ to ‘Tom’ is added in the social network.

If the process builder is not sure which recommendation to select after a customer request (‘verify customer order 1 vs ‘verify customer order 2’ which have the same process structure, but are performed by different performers), she can consult the social network. If the user takes into account the connections between the performers (i.e., ‘Mike,’ ‘Sue,’ ‘Jana’) in the existing process (i.e., ‘customer request’) and the two performers (i.e., ‘Ronny,’ ‘Peter’), there is no direct connection to ‘Ronny,’ but two connections to ‘Peter’ (i.e., ‘Sue’ to ‘Peter’ and ‘Mike’ to ‘Peter’). Thus, ‘verify customer order 2’ process could be more attractive to the user, since the performers are more tightly connected. The process builder can combine the edited business process with ‘verify customer order 2’ and save it as a new business process. Note that the names of performers are used in the process models and the social network in the example for ease of understanding. Of course, in a real process model, a group of people, such as roles, department, etc., is assigned to a task. And nodes in a social network also represent groups of people.

## Social network from user history

This section discusses the use of social networks from a recommendation history. The user history in a recommendation-based modeling support system consists of the name of the selected recommendation and the performer (user that edited or selected a specific recommendation). Note the different consideration of users. In the previous section the transfer of work between performers is taken into account. In this section users who selected and edited processes lay the foundation for the social network generation. In Figure 3 the user selected the process model part customer request (edited and selected by Jane and Peter) and the directly succeeding process model part verify customer order (edited and selected by Anna, John, and Jim).

The recommendation system also stores (for each modeling purpose $\mathbf { e . g . }$ , analysis, documentation, execution, or reengineering) the order of selected process model parts into the workspace of the user. Table 3 shows an example.

In the table each row refers to an operation of a user. For example, user uses process $P _ { 1 }$ and process model parts $P _ { 2 }$ and $\bar { P } _ { 1 }$ is located before $P _ { 2 } .$ user uses the same process model parts $( \mathrm { i } . \mathrm { e } . , P _ { 1 }$ and $P _ { 2 } )$ , but the order is different from that of $u s e r _ { 1 }$ (while the modeling purpose is the same).

From the information on the selected processes and preceding/succeeding history, social networks can be derived. Table 4 shows an example of the user history generated from the modeling history of the community of users. In the table, each row refers to a user (u) and a column corresponds to a process model (p) in the repository. Each cell $( c _ { i j } )$ shows the number of uses of the process model $\left( { p } _ { j } \right)$ by the user $\left( u _ { i } \right)$ . The right part of the table shows how frequently users use a certain order of process models. Each cell represents the number of uses of an order of processes $( P _ { j } \to \hat { P } _ { k } )$ by a user (u ).

From the matrix, the distance between two users can be measured by comparing the corresponding row vectors. Several distance measures, such as Minkowski distance,

![](/api/attachments/2Y4RFUZA/fulltext/images/2a9c72b84e57e48e6a214e9f7057bb554854bfd6b6611fddeffe64b79c62374f.jpg)  
Figure 3 Social Network according to recommendation names.

Table 3 Preceding/succeeding history

<table><tr><td></td><td>Preceding process</td><td>Succeeding process</td></tr><tr><td> $User_1$ </td><td> $P_1$ </td><td> $P_2$ </td></tr><tr><td> $User_2$ </td><td> $P_2$ </td><td> $P_1$ </td></tr><tr><td> $User_1$ </td><td> $P_2$ </td><td> $P_3$ </td></tr><tr><td> $User_3$ </td><td> $P_1$ </td><td> $P_2$ </td></tr><tr><td> $User_4$ </td><td> $P_4$ </td><td> $P_5$ </td></tr><tr><td> $User_2$ </td><td> $P_1$ </td><td> $P_5$ </td></tr><tr><td>:</td><td>:</td><td>:</td></tr></table>

Table 4 User history

<table><tr><td></td><td> $P_1$ </td><td> $P_2$ </td><td> $P_3$ </td><td> $P_4$ </td><td>...</td><td> $P_N$ </td><td> $P_1 \rightarrow P_2$ </td><td> $P_1 \rightarrow P_3$ </td><td></td><td> $P_{N-1} \rightarrow P_N$ </td></tr><tr><td> $User_1$ </td><td>2</td><td>1</td><td>0</td><td>0</td><td>...</td><td>2</td><td>2</td><td>0</td><td>...</td><td>2</td></tr><tr><td> $User_2$ </td><td>2</td><td>1</td><td>0</td><td>0</td><td>...</td><td>2</td><td>0</td><td>1</td><td>...</td><td>2</td></tr><tr><td> $User_3$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>...</td><td>0</td><td>1</td><td>0</td><td>...</td><td>0</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td></tr><tr><td> $User_M$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>...</td><td>0</td><td>0</td><td>0</td><td>...</td><td>0</td></tr></table>

Table 5 Realistic user history

<table><tr><td></td><td> $P_1$ </td><td> $P_2$ </td><td> $P_3$ </td><td> $P_4$ </td><td> $P_5$ </td><td> $P_6$ </td><td> $P_7$ </td><td> $P_8$ </td><td> $P_9$ </td><td> $P_{10}$ </td><td> $P_{11}$ </td><td> $P_{12}$ </td><td> $P_{13}$ </td></tr><tr><td> $User_1$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $User_2$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $User_3$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td></tr><tr><td> $User_4$ </td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $User_5$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $User_6$ </td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $User_7$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $User_8$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $User_9$ </td><td>0</td><td>1</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $User_{10}$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

(P ¼ check Order2, P ¼ check Order3, $P _ { 3 } = \mathsf { o r d e r }$ approval, $P _ { 4 } = \mathrm { O r d e r }$ Checking, P ¼ CheckOrderAvailability, $P _ { 6 } =$ order\_approval, $P _ { 7 } = { \mathsf { h a n d l e } }$ rejected order, $P _ { 8 } { = } \mathsf { m a n a g e }$ order approvals, $P _ { 9 } = { \mathsf { c u s t o m e r } }$ order, $P _ { 1 0 } =$ check credibility, $P _ { 1 1 } = \mathsf { c h e c k e d }$ order availability, $P _ { 1 2 } =$ validate Order, P ¼ approve order).

Hamming distance, Pearson’s correlation coefficient, etc., can be applied. They are defined as follows.

$$
\text { Minkowski   distance } (u _ {i}, u _ {j}) = \sum_ {k = 1} ^ {m} \left| c _ {i k} - c _ {j k} \right| ^ {2} | ^ {n}) ^ {1 / n}
$$

$$
\text { Hamming   distance } (u _ {i}, u _ {j}) = \sum_ {k = 1} ^ {m} \delta (c _ {i k}, c _ {j k}) / m
$$

$$
\text { where } \delta (x, y) = \left\{ \begin{array}{c} 0 \text { if } (x > 0 \Lambda y > 0) V (x = y = 0) \\ 1 \text { otherwise } \end{array} \right.
$$

Pearson<sup>0</sup>s correlation coefficient $( u _ { i } , u _ { j } )$

$$
= \sum_ {k = 1} ^ {m} c _ {i k}, c _ {j k}) / \sum_ {k = 1} ^ {m} c _ {i k} ^ {2} + \sum_ {k = 1} ^ {m} c _ {j k} ^ {2} - \sum_ {k = 1} ^ {m} c _ {i k}, c _ {j k})
$$

The Minkowski distance is a generalization of the Euclidean distance. It has a parameter n: n ¼ 1 is the Rectilinear distance also referred to as Manhattan distance, n ¼ 2 is the Euclidean distance, and for large values of n the metric approximates the Chebyshev distance. The Hamming distance does not consider the absolute frequency but only whether it is 0 or not. Another metric is Pearson’s correlation coefficient which is frequently used to find the relationship among users. Its value ranges from 1 to þ 1. If two users have similar preferences, the value between them is close to 1. 1 means a maximal negative line relationship between users. Using the distance measure, the distance matrix among users can be calculated and then transformed into a network form. From the network, by applying a certain threshold value, unimportant arcs can be removed. If two users are connected in the network, it means that the two users used a similar set of process models during their previous process designs.

For example, there is a recommendation history shown in Table 5. Note that the preceding/succeeding information is not considered in this example.

The table shows a recommendation history where 10 users were involved who selected a total of 13 process models. The purpose of the models was documentation. From this history, a social network shown in Figure 4 is derived. Note that the threshold value of 0.3 is applied, and arcs (of whichever weight value is less than the threshold) are removed.

There are five cliques in the network. They are $\{ u s e r _ { 1 } ,$ user }, {user }, {user , user , user }, {user , user }, {use $r _ { 6 } , u -$ $s e r _ { 1 0 } \}$ . Users who have similar process usage pattern are directly connected to each other and are ‘neighbors.’ Thus, when the user designs a new process model, she can use the history of her neighborhoods. For example, in the figure, the history of $u s e r _ { 4 }$ is used in the recommendation system for user but can be used to find a neighborhood of a user. For example, Table 5 can be extended to include the history of the order of process models, and a social network can be calculated from the combined table.

## Social network from insertion history

The third way of generating social network is taking into account the insertion history of process models. The recommendation system stores the order of inserted process model parts into the workspace of a user. A user of the recommendation system can generate a new process model and insert it into the repository. A user can search for suitable process models and generate a new model by combining them. Table 6 shows an example of insertion history. In the table, user generates ‘customer order process by merging ‘check order availability’ and ‘check credibility.’ A user can also take one process model and modify it to make a new process model. In the table, user modifies ‘customer order’ and generates ‘check order.’

![](/api/attachments/2Y4RFUZA/fulltext/images/4d785d512585ad4f52a0d6a3380393a5ef89c0f7627579bfacb39ea9b114abe1.jpg)  
Figure 4 Social Network from Table 5.

From this information a social network reflecting the history can be generated. Figure 5 shows the social network derived from Table 6. Figure 5(a) shows a graphical view of the insertion history from the table. In the figure, nodes represent process models and arcs show relationships between process models. For example, since the ‘customer order’ is designed with ‘check credibility’ and ‘check order availability,’ there are arcs from ‘check credibility’ to ‘customer order’ and from ‘check order availability’ to ‘customer order.’ From this figure, by replacing the process model with the user who generated it, the social network depicted in Figure 5(b) is generated.

Social networks from insertion history cannot be used to find neighborhoods, but for change propagation. Whenever one of the members of the clique changes a process the other neighbors who are affected by this modification will be informed about this change. This notification is optional and will be performed only if users have activated this functionality.

## Research method

## Design

To evaluate our modeling support system and investigate our main conjectures regarding its effectiveness, an experiment has been conducted. Basically, the experiment should gain insight into the following questions:

1. Will process builders be inclined to follow up on the suggestions of our recommendation-based process modeling support system? It is more or less a basic assumption underlying all our endeavors in this field that process builders will be interested in, and follow up on modeling recommendations. However, this has not been tested in an empirical fashion so far.

2. Will the support of a recommendation-based process modeling support system improve the modeling process? The second basic assumption behind our work is that the use of a recommendation system – beyond perhaps being appreciated by model builders – will increase the quality of the process model and would not be less efficient than modeling from scratch. After all, some balance is expected between the additional time that is required to evaluate recommendations and the saved modeling time when following up a recommendation (both compared to a traditional, unsupported situation).

3. If process builders follow up recommendations of the support system, will social information play any role in their decision-making? The specific expectation we have is that recommendations that are based on modeling decisions of people who are socially close to a model builder will receive favorable attention. On the basis of the extension of our recommendation system, as outlined in the previous sections, we are now able to approach this question with an experimental design.

The specific hypotheses with respect to these questions are as follows (numerals corresponding with the previous questions):

H1: Process builders that receive modeling recommendations to create part of a process model will more often use a recommendation than build that model part from scratch.

H2a: Process builders using a recommendation system will create process models in the same time as those without the support of a recommendation system.

H2b: Process builders using a recommendation system will create process models of a higher semantic quality than do those without the support of a recommendation system.

H2c: Process builders using a recommendation system will create process models of a higher syntactic quality than do those without the support of a recommendation system.

H3a: Process builders that follow up recommendations will favor those recommendations that refer to previously used model parts by well-known people over recommendations without any information on previous use.

H3b: Process builders that follow up recommendations will favor those recommendations that refer to previously used model parts by well-known people over those that refer to people they do not know well.

The experiment that has been conducted took place in the semester of 2008 and involved the participation of 28 graduate and post-graduate students. All students followed a course in Workflow Management at the University of Karlsruhe. We refer to this group as the experiment group. Subsequently their members were asked to model a business process handling business trips on the basis of an informal description of the procedure in use. Note how this phase coincides with the formalization phase that has been distinguished in the introduction of this article as being of central interest to us.

Table 6 Process insertion history

<table><tr><td></td><td>Used processes</td><td>Inserted process</td></tr><tr><td> $User_1$ </td><td>Check order availability + check credibility</td><td>Customer order</td></tr><tr><td> $User_2$ </td><td>Customer order</td><td>Check order</td></tr><tr><td> $User_3$ </td><td>Customer order + handle reject order</td><td>Order approval</td></tr><tr><td> $User_4$ </td><td>Order approval + notify customer</td><td>Approval process</td></tr><tr><td>:</td><td>:</td><td>:</td></tr></table>

![](/api/attachments/2Y4RFUZA/fulltext/images/15261a4a1e6f2e2596e7dfe6f7d44fe1c8659e63cd76f68d869adab78fc73f56.jpg)  
Figure 5 Generating social network from insertion history. (a) Insertion history of process models; (b) Social network from insertion, history of process models.

The informal process description was divided into three subsequent parts: (1) the checking of the travel application, (2) the booking of the hotel room and the car, and (3) the activities which needed to be handled after returning from the trip. The participants were given access to a repository of process model parts, and the system generated recommendations on the basis of this repository. Overall, each participant received a set of recommendations on each of the three parts of the informal description of the process. For each part, they were given three alternative modeling parts (thus, participants received nine recommendations in total). The participants were not obliged to follow up on these recommendations, that is, they were free to ignore them. The obvious alternative was to build a modeling part themselves.

To prepare the repository and the recommendations, the following procedure was undertaken. Previously, the same modeling exercise was given to 24 different students of the same university who followed the same course. We refer to these students as the preparation group. These students had to create the model on the basis of the same informal description, but were given no modeling support whatsoever. The time that they spent on building the model was recorded using a self-assessment form. From the models created in this way, 19 solutions were considered to be acceptable (and five were not). The main criteria that were employed were the semantic quality (or validity) of the model and the syntactic quality. With respect to the former, issues were addressed such as: ‘Does the model represent the exercise truthfully?’ and ‘Are no parts missing and are no parts spurious?’ The syntactical quality was checked with questions such as ‘Does the model contain wrongly matched pairs of logical connectors?’ and ‘Are all parts of the mode reachable?’

To prepare our system for the evaluation the repository has been populated with process model parts that were derived from three business process models randomly selected from the 19 acceptable solutions. Then, the three process models have been fragmented into nine process model parts. Each of the process models have been fragmented at the same position so that each model part related to exactly one part of the modeling exercise. Consequently, the repository contained three process model parts of roughly similar quality for the ‘beginning’ of the process, three process model parts of equal quality for the ‘middle’ and finally three equal parts for the process ‘end.’

Subsequently, each of the 28 persons were asked regarding their relationships within this particular group (who knew whom) with the question, ‘To what extent do you know individual X?’ for each of the other 27 persons. The interviewees could choose between three answers: (1) not all, (2) somewhat, and (3) very well. Based on their answers, a social network of the interviewees has been generated. This information was used to annotate the nine process model parts individualized for each of the participants. To be precise, for each participant we randomly attached (1) to three of the nine model parts (one for each of the three parts of the modeling exercise) the name of a person whom that participant knew well, (2) to three model parts the name of a person whom the participant did not know well, and (3) for the three remaining model parts no information on previous usage at all was provided. Note how the information on the social relationships was used to mimic information that could have been gathered in a real setting on historic, actual usage of the modeling fragments by the support system. During the experiment the participants were not aware that this information was artificial.

In the actual experiment, each participant was individually observed carrying out the modeling exercise, for example, what recommendations were followed up, which adjustments were made, which parts were modeled from scratch, etc. Also, an automatic log was generated for the actual use of both the modeling tool and the recommendation tool. The observations were then matched with these automatic logs to improve and validate their quality. The automatically generated logs were also used to record the modeling time. After the experiment, each individual participant was interviewed about the reasons for following up a recommendation (or not) and the information that they used in this decision-making process.

Students volunteered to participate in the experiment and received a small financial reward. The reward was dependent only on their participation – not on the quality of the created model or the modeling decisions.

## Results

To investigate hypothesis H1, the occasions on which participants selected a recommendation at each of the three parts in the modeling exercise were considered. We advance the null hypothesis that the average number of times that a recommendation is used to cover a part is equal to the average number of times the model part is created from scratch. In other words, the average difference between the two equals zero. The alternative hypothesis would be that the number of parts modeled on the basis of recommendations is bigger than the parts modeled from scratch. To test this, 28 paired frequencies of modeling decisions are at our disposal. (For example, participant Thorsten decides to select a recommendation for parts 2 and 3 of the model, but models part 1 himself. In his case, the difference equals 1.) For the 28 participants, the mean value is 2.5 and the median 3, hinting at a strong preference for using a recommendation. A t-test was used to determine the significance of this result. It provides a P-value of 0.000 o0.05, which shows that the preference is highly significant at a 95% confidence level. A sign test on the difference in medians gives a similar small P-value, which confirms the strong tendency to base all parts of the formal model on recommendations. Therefore, the alternative hypothesis must be accepted, leading to the acceptance of H1: Modelers are inclined to follow up recommendations, assuming that they satisfy a certain quality level.

To test hypothesis H2a, the differences in modeling between the experiment and the preparation group were considered. Note that these are not paired observations since the members of the groups differ. The standardized skewness and kurtosis values for the modeling times of both groups are within the range expected when assuming normal distributions of the modeling times. The nullhypothesis is that the mean modeling times for both groups are the same; the alternative hypothesis is that these times differ. The 95% confidence interval for the mean modeling time of the experiment group equals [69.418, 80.916], while that of the preparation group is [71.455, 85.212]. Since the intervals overlap, there is no significant difference at this confidence level. This is also the case for the standard deviations for these groups. Therefore, we accept H2a: The same time is needed to build a process model with or without recommendation support.

With hypothesis H2b, we turn our attention to the semantic quality of the process models created by both groups. Of the 24 process models in the preparation group, only four displayed a completely valid representation of the exercise, in the sense that the represented business logic was completely correct and that no obvious parts were missing or spurious. For the 28 process models built by the experiment group using the recommendation system, 19 were completely valid. Since the data are not normally distributed for the preparation group, the non-parametric Kruskall-Wallis test is used to test the null hypothesis that the medians of both groups are the same (the alternative hypothesis being that the median for the experiment group is higher). This test gives a P-value of 0.000, which is much smaller than the 0.05 threshold. Therefore, the alternative hypothesis must be accepted, leading to the acceptance of H2b: The semantic quality of the process models created under support of the recommendation system is higher.

The other aspect in comparing the quality of the process models concerns the syntactical quality. Of the 24 process models created by the preparation group, 14 displayed no syntactical mistakes; of the 28 process models created by the experiment group, 11 showed no syntactical mistakes whatsoever. Once more, the data are not normally distributed; thus the Kruskall-Wallis test is used to test the null hypothesis that the medians of both groups are the same (the alternative hypothesis being that the median for the experiment group is higher). The resulting P-value equals 0.911, which means that the null hypothesis cannot be rejected. In other words, hypothesis H2c must be rejected: The syntactical quality of the process models created under support of the recommendation system is not higher.

The final set of hypotheses deals with the influence of the social information that accompanies some of the recommendations. To investigate hypothesis H3a, we compare per participant from all the recommendations that he/she followed up the proportion that relate to previous well-known users to the ones containing no information on previous use. Thus, for example, from the three recommendations that Thorsten followed up, one of them was connected to (a supposed) previous use of that model part by someone he knows well, while he followed up one recommendation that did not contain any information on previous use (the remaining recommendation relating to someone he does not know well). A t-test to test the null-hypothesis that there is no difference between the mean number of decisions for either type of recommendation leads to a P-value of 0.190. Therefore, the null hypothesis cannot be rejected and we must reject hypothesis H3a. In other words, process builders that follow up recommendations do not seem to particularly favor those recommendations that relate to previously used model parts by people in their social network.

Similarly, to test hypothesis H3b we compare per participant the number of recommendations he/she followed up that refer to well-known previous users to the number of recommendations that relate to people not known by the modeler. The t-test to check the null-hypothesis illustrates that there is no difference between the mean number of decisions for either type of recommendation, resulting in a P-value of 0.155. The null hypothesis must therefore be rejected when assuming a 95% confidence interval. Therefore, H3b must be rejected as well. Information on previous usage of recommendations by peers of the process builder seems to play no big role in their selection.

## Discussion

## Interpretation

The experiment provides strong support for process builders’ preference for and active use of recommendations as provided by the proposed support system. Clearly, for each part of the modeling exercise each participant in the experiment received three recommendations, meaning that someone would need to feel very strongly about the lack of quality of all recommendations in order to model a process part himself/herself. Recall that the recommendations are derived from previous acceptable solutions. It is open to question whether it would be possible, in general, to provide such strong recommendation support, but our reference situation is that of organizations that have hundreds or thousands of process models in use from highly related domains. This is increasingly becoming a realistic situation, considering the reports on actual process modeling practice in industry (Becker et al., 2000; Gulla and Brasethvik, 2000; Siegeris and Grasl, 2008). In other words, the attractiveness of a recommendation system receives strong support from this experiment.

The obvious next issue is whether such support is of any value. What follows from the experiment is that, in accordance with our expectation, the modeling time itself does not change with respect to a traditional situation. So, the support system does not make the building effort less efficient. What is surprising is that the semantic quality of the process models is positively affected, while no relation can be found between recommendation usage and improved syntactical quality. In other words, a relation can be inferred from our data that a recommendation system prevents process builders from forgetting relevant parts of the informal model or including spurious parts. Clearly, this is a highly relevant outcome and supports further development of this support. However, syntactical mistakes are not prevented as effectively. That syntactical mistakes can be created at all when using recommendations can be explained from the practice that recommended process parts are often edited by the process builders, as noted in our observations.

Finally, the experiment gives no reason to believe that the kind of social information that was included in this setting is of much importance in the model building process. On the one hand, this is disappointing and contrasts with our initial assumptions about the impact that social information would have. On the other hand, it gives support for the existing practice of solitary process building.

To get a better insight into the role of social information, in our follow-up to the experiment our participants were asked whether they (a) noticed and (b) considered the social information tags to the recommendations at all. All but one was aware of this information, but only two stated that this information affected their decision making in some way. Much more important in deciding to follow up a recommendation was the semantic match between the model part and modeling part content (mentioned 21 times), the tag score of the recommendation (mentioned eight times), and the name of the recommended model part (mentioned five times). (Note that multiple answers were possible.) From this feedback, it can be inferred that social information plays only a minor role in the decision to follow up recommendations.

## Implications

The most important implication from our work for practice is that the usage of recommendation systems should be actively considered by vendors of process modeling suites, like ARIS, Protos, Lomardi, and TIBCO. In this way, large repositories that are at the disposal of their clients can be more actively used to support their process builders. Our results show an increased interest of users and enhanced semantic quality. This is an extremely important benefit in the setting of individual modelers building process models, at a time when little opportunity exists to receive feedback on the created work by peers.

Because the syntactical quality is not visibly affected and syntactical errors still occur under the guidance of a recommendation system, the combined usage of tools to support process modelers in checking the syntactical quality of their model should be actively considered, for example, as provided by the open source tool Woflan (http://is.tm.tue.nl/research/woflan.htm, last consulted on November 2008). As mentioned, the recommendation system does provide support for avoiding syntactical errors, but this feature was deactivated during the experiment in order to provide transparency. The open source tool WoPeD (http://www.woped.org) is a fine example where model building and verification features are closely integrated in the same user interface.

For research, a very preliminary insight from our work is that it seems more fruitful for work on providing collaborative process modeling support (e.g., in (Rittgen, 2007)) to focus on the elicitation dialogue. After all, process building can be supported by recommendations as evaluated in this article, while social information and, in turn, interaction does not seem to play too big a role in the formalization dialogue. Nonetheless, in the presented work social networks derived from data were used that had been gathered within the use of that recommendation system. To build social networks, other information could have been used that was available in the wider context of process modeling which would have perhaps been more attractive to interest process builders. For example, the reputation of people, their skill level in process building, their history in process model creation, etc., could all be features to consider. Because the infrastructure is there in the form of the recommender and social network tools that was described, further investigations could take place with relatively small start-up costs.

## Limitations

Because students participated in the conducted experiment, the usual external validity problems arise. Despite this, we agree with Batra et al. (1990), Recker and Dreiling (2007) that in the area of conceptual modeling in general and process modeling in particular the selection of students over practitioners can, in fact, be advisable. Results from both domain understanding and problem-solving tasks could have been confounded by participants that were able to bring to bear prior business knowledge in one of the areas (Siau and Loo, 2006).

A major limitation in our experimental set-up is the use of inter-personal acquaintance as a proxy for historical usage patterns by process building peers. An alternative would have been to add an extra phase to our experimental set-up. In this way, actual usage of (tagless) recommendations by one group could have been used as a basis for creating the social usage tags for the recommendations in the final phase with the experiment group. The use of this artificial information may have been a cause for the low usage in the experiment of recommendations that (supposedly) had been used by peers. Alternatively, social information is really not of any importance, but this should be backed up by further research.

## Conclusion

Business process modeling tools on the market today are mostly ‘one-person tools’ and mostly do not support an efficient reuse of process models, resulting in dissatisfaction of business users with current IT implementations. The focus of this article was on improving the formalization dialogue of creating process models using a particular tool and thus improving the current IT implementations. Users were guided in this respect within the context of a recommendation-based process modeling support system to which ‘social’ features were added. Three kinds of social networks were used: (1) a social network from a process model repository, (2) a social network from a user history, and (3) a social network from an insertion history. The social network from process models provides an organizational view of business processes. The social network from user history shows the relationship among modelers who use the recommendation system. The social network from insertion history shows the relationship among modelers who decided for identical recommendations.

To investigate the effectiveness of the recommendation system a two phase experiment has been conducted. In the first phase students were instructed to model a business process regarding handling a business trip, but without giving them any modeling support. In the second phase a group of students had to create the same model, but this time they were given the modeling support system. The participants were not obliged to follow up these recommendations, and they were free to ignore them.

The experiment confirms that modelers are inclined to follow up recommendations as provided by the system. If users decide to reuse recommendations, then they do not increase their modeling time and they can improve the semantic quality of the process models. The syntactical quality of the process models created under support of the recommendation system is not notably affected. Our assumption could not be confirmed within the experiment that users favor recommendations that refer to previously used model parts by well-known people over those that refer to people that they do not know well.

While some of the results of the recommendation system are very promising to deal with the inherent risks of process building as a solitary activity – in particular with respect to semantic quality – many challenges remain. Central problems include finding more informative ways to catalogue and represent parts of business process models, better ways to identify relationships between the model parts, discovering the user’s intentions and requirements, and from there automatic prediction of the process model parts that will enable the user to finish her design most efficiently. Furthermore, we believe that the recommendation system would get a significant improvement if researchers from the Human Computer Interaction domain were brought into the conversation. A tight collaboration with that discipline should establish a continuous feedback loop between the technical solutions being envisioned and the development of process model by process builders.

We recall from our experiment and our discussion of its limitations that the annotation of model parts was artificial, which, in retrospect, may have been a serious impediment. Therefore, more research work seems required within realistic settings, such as intra- or inter-organizational process modeling collaborations, where capabilities and skills of group members are crucial for the project success. Because the feasibility and attractiveness of a recommendation system have been demonstrated, it seems worthwhile to extend its support. The direction would then be towards generating better process models on the basis of information that is readily available – be it from the social context of the process builder or otherwise.

To conclude this article, we feel that the line of our research with its focus on the modeling process rather than on the model artifact shows strong signs of viability. We hope it will inspire other researchers to join this stream, thus further developing the discipline of process modeling towards providing actual support for supporting organizational development initiatives.

## References

Baeza-Yates, R. and Ribeiro-Neto, B. (1999). Modern Information Retrieval, Reading, MA: Addison Wesley.

Bandara, W., Gable, G. and Rosemann, M. (2005). Factors and Measures of Business Process Modelling: Model building through a multiple case study, European Journal of Information Systems 14(4): 347–360.

Barnes, G., Cerrito, P. and Levi, I. (1998). A Mathematical Model fo Interpersonal Relationships in Social Networks, Social Networks 20: 179–196.

Basu, C., Hirsh, H. and Cohen, W.W. (1998). Recommendation as Classification: Using social and content-based information in recommendation, in Proceedings of the Fifteenth National Conference on Artificial Intelligence (Madison, WI, United States); Menlo Park, CA: American Association for Artificial Intelligence, 714–720.

Batra, D. and Marakas, G. (1995). Conceptual Data Modelling in Theory and Practice, European Journal of Information Systems 4: 185–185.

Batra, D., Hoffler, J.A. and Bostrom, R.P. (1990). Comparing Representations with Relational and EER Models, Communications of the ACM 33(2): 126–139.

Becker, J., Rosemann, M. and Uthmann, C. (2000). Guidelines of Business Process Modeling, in: W.N.P. van der Aalst, J. Desel and A. Oberweis (eds.) Business Process Management. Models, Techniques, and Empirical Studies Lecture Notes in Computer Science, vol. 1806, Berlin: Springer Verlag. 30–49.

Born, M., Brelage, C., Markovic, I., Pfeiffer, D. and Weber, I. (2008). Auto-Completion for Executable Business Process Models, in 3rd International Workshop on Semantics for Web Services (Milan, Italy, 2008); Berlin, Heidelberg, Germany, NY, USA: Springer, 1–6.

Burke, R. (2002). Hybrid Recommender Systems: Survey and experiments, User Modeling and User-Adapted Interaction 12(4): 331–370.

Curtis, B., Kellner, I. and Over, J. (1992). Process Modeling, Communications of the ACM 35: 75–90.

Davies, I, Green, P., Rosemann, M., Indulska, M. and Gallo, S. (2006). How do Practitioners Use Conceptual Modeling in Practice? Data & Knowledge Engineering 58(3): 358–380.

Dumas, M. and Hofstede, A. (2001). UML Activity Diagrams as a Workflow Specification Language, in M. Gogolla and C. Kobryn (eds.) 4th International Conference on The Unified Modeling Language, Modeling Languages, Concepts, and Tools, Lecture Notes in Computer Science, vol. 2185, Berlin: Springer Verlag, 76–90.

Dumas, M., Van der Aalst, W.M.P. and ter Hofstede, A.H.M. (eds.) (2005). Process Aware Information Systems: Bridging people and software through process technology, Hoboken, NJ: John Wiley & Sons.

Elzinga, D., Horak, T., Lee, C. and Bruner, C. (1995). Business Process Management: Survey and methodology, IEEE Transactions on Engineering Management 42(2): 119–128.

Erl, T. (2005). Service-Oriented Architecture: Concepts, technology, and design, Upper Saddle River, NJ: Prentice-Hall.

Ferris, C. (2003). What are Web Services? Communications of the ACM 46(6): 31–32.

Frederiks, P. and van der Weide, T. (2006). Information Modeling: The process and the required competencies of its participants, Data & Knowledge Engineering 58(1): 4–20.

Georgakopoulos, D., Hornick, M. and Sheth, A. (1995). An Overview of Workflow Management: From process modeling to workflow automation infrastructure, Distributed and Parallel Databases 3(2): 119–153.

Golbeck, J.A. (2005). Computing and Applying Trust in Web-based Social Networks, Ph.D. thesis, College Park, MD, USA, chair-James Hendler.

Guha, R., Kumar, R., Raghavan, P. and Tomkins, A. (2004). Propagation of Trust and Distrust, in Proceedings of the 13th International Conference on World Wide Web (NY, USA); New York: ACM, 403–412.

Gulla, J. and Brasethvik, T. (2000). On the Challenges of Business Modeling in Large-scale Reengineering Projects, in 4th International Conference on Requirements Engineering (Washington, DC, USA); New York: IEEE, 17–26.

Heider, F. (1958). The Psychology of Interpersonal Relations, New York: Wiley. Herlocker, J.L., Konstan, J.A., Terveen, L.G. and Riedl, J.T. (2004). Evaluating Collaborative Filtering Recommender Systems, ACM Transactions on Information Systems 22(1): 5–53.

Hevner, A., March, S., Park, J. and Ram, S. (2004). Design Science in Information Systems Research, Management Information Systems Quarterly 28(1): 75–106.

Hoppenbrouwers, S., Lindeman, L. and Proper, H. (2006). Capturing Modeling Processes - Towards the MoDial Modeling Laboratory, in: R. Meersman, Z. Tari and P. Herrero (eds.) OTM 2006 Workshops Lecture Notes in Computer Science, vol. 4278, Berlin: Springer Verlag, 1242–1252.

Hoppenbrouwers, S., Proper, H. and van Reijswoud, V. (2005). Navigating the Methodology Jungle - The communicative role of modelling techniques in information system development, Computing Letters 1(3): 97–106.

Hornung, T., Koschmider, A. and Lausen, G. (2008). Recommendation Based Process Modeling Support: Method and user experience, in: Q. Li, S. Spaccapietra, E. Yu and A.A. Olive (eds.) 27th International Conference on Conceptual Modeling Lecture Notes in Computer Science, vol. 5231, Berlin: Springer Verlag, 265–278.

Kenny, D. and LaVoie, L. (1984). The Social Relations Model, American Journal of Sociology 105: 141–182.

Kettinger, W., Teng, J. and Guha, S. (1997). Business Process Change: A study of methodologies, techniques, and tools, Management Information Systems Quarterly 21: 55–80.

Kim, J.H., Suh, W. and Lee, H. (2002). Document-Based Workflow Modeling: A case-based reasoning approach, Expert Systems with Applications 23(2): 77–93.

Koschmider, A. (2007). A<sup>¨</sup> hnlichkeitsbasierte Modellierungsunterstu¨tzung fu¨r Gescha¨ftsprozesse, Dissertation, Karlsruhe: Karlsruhe University Press, University of Karlsruhe.

Koschmider, A. and Oberweis, A. (2009). Designing Business Processes with a Recommendation-based Editor, in J. vom Brocke and M. Rosemann (eds.) International Handbook on Business Process Management, vol. 1, Berlin: Springer, Verlag.

Koschmider, A., Habryn, F. and Gottschalk, F. (2008). Real Support for Perspective-Compliant Business Process Design, in D. Ardagna, M. Mecella and J. Yang (eds.) BPM 2008 Workshops LNBIP, vol. 17, Milan, Italy: Springer Verlag, 30–41.

Liaw, S., Deveny, E., Morrison, I. and Lewis, B. (2006). Clinical, Information and Business Process Modeling to Promote Development of Safe and Flexible Software, Health Informatics Journal 12(3): 199–211.

Lundell, B. and Lings, B. (2004). Method in Action and Method in Tool: A stakeholder perspective, Journal of Information Technology 19(3): 215–223.

Madhusudan, T., Zhao, J.L. and Marshall, B. (2004). A Case-based Reasoning Framework for Workflow Model Management, Data Knowledge Engineering 50(1): 87–115.

Mason, W., Jones, A. and Goldstone, R.L. (2008). Propagation of Innovations in Networked Groups, Journal of Experimental Psychology: General American Psychological Association 137(3): 422–433.

Milanovic, N. and Malek, M. (2004). Current Solutions for Web Service Composition, Internet Computing, IEEE 8(6): 51–59.

Nagarajan, M. (2006). Semantic Annotations in Web Services, in J. Cardoso and A.P. Sheth (eds.) Semantic Web Services, Processes and Applications, Berlin: Springer, Verlag.

OMG 2008. Business process modeling notation, V1.1, Specification (January 2008). [www document] http://www.omg.org/spec/BPMN/1.1/PDF (accessed October 2008).

Recker, J. and Dreiling, A. (2007). Does it Matter Which Process Modelling Language we Teach or Use? An Experimental Study on Understanding Process Modelling Languages Without Formal Education, in 18th Australasian Conference on Information Systems (The University of Southern Queensland, Toowoomba, Australia, 2007). 356–366.

Reichert, M. and Dadam, P. (1998). ADEPT Flex – Supporting dynamic changes of workflows without losing control, Journal of Intelligent Information Systems 10(2): 93–129.

Reijers, H. (2003). Design and Control of Workflow Processes: Business process management for the service industry, Lecture notes in Computer Science, vol. 2617, Berlin: Springer, Verlag.

Rittgen, P. (2007). Negotiating Models, in J. Krogstie, A.L. Opdahl and G. Sindre (eds.) 19th International Conference on Advanced Information Systems Engineering Lecture Notes in Computer Science, vol. 4495, Berlin: Springer Verlag, 561–573.

Rittgen, P. (2008). COMA Handbook: Collaborative modeling architecture, Version 2.0, University College of Boras, School of Business and Informatics [www document] http://coma.nu/COMA\_Handbook.pdf.

Sadiq, W. and Orlowska, M. (2000). Analyzing Process Models Using Graph Reduction Techniques, Information Systems 25(2): 117–134.

Schaffner, J., Meyer, H. and Weske, M. (2007). A Formal Model for Mixed Initiative Service Composition, in Proceedings of The IEEE Internationa Conference on Services Computing (Salt Lake City, UT, USA); Salt Lake City, USA: IEEE Computer Society, 443–450.

Scheer, A.-W. (1998). ARIS – Business Process Modeling, 2nd edn, Berlin: Springer, Verlag.

Siau, K. and Loo, P.-P. (2006). Identifying Difficulties in Learning UML, Information Systems Management 23(3): 43–51.

Siegeris, J. and Grasl, O. (2008). Model Driven Business Transformation – An experience report, in M. Dumas, M. Reichert and M.C. Shan (eds.) 6th International Conference on Business Process Management Lecture Notes in Computer Science, vol. 5240, Berlin: Springer Verlag.

Song, M. (2006). Organizational mining in Business Process Management, Ph.D. thesis, Pohang University of Science and Technology, Pohang, South Korea.

Thom, L., Reichert, M., Chiao, C., Iochpe, C. and Hess, G. (2008). Inventing Less, Reusing More, and Adding Intelligence to Business Process Modeling, in: S.S. Bhowmick, J. Ku¨ng and R. Wagner (eds.) Lecture Notes in Computer Science, vol. 5181, Berlin: Springer, Verlag, 837–850.

Tichy, N., Tushman, M. and Fombrun, C. (1979). Social Network Analysis for Organizations, Academy of Management Review 4(4): 507–519.

van Bommel, P., Hoppenbrouwers, S., Proper, H. and van der Weide, T. (2006). Exploring Modelling Strategies in a Meta-modelling Context, in: R. Meersman, Z. Tari and P. Herrero (eds.) Lecture Notes in Computer Science, Berlin: Springer, Verlag, 1128–1137.

van der Aalst, W.M.P. (1998). The Application of Petri Nets to Workflow Management, The Journal of Circuits, Systems and Computers 8(1): 21–66.

van der Aalst, W.M.P. and ter Hofstede, A. (2000). Verification of Workflow Task Structures: A petri-net-based approach, Information Systems 25(1): 43–69.

van der Aalst, W.M.P., Reijers, H.A. and Song, M. (2005). Discovering Social Networks from Event Logs, Computer Supported Cooperative Work 14(6): 549–593.

Wand, Y. and Weber, R. (2002). Research Commentary: Information systems and conceptual modeling – A research agenda, Information Systems Research 13(4): 363–376.

Wastell, D., McMaster, T. and Kawalek, P. (2006). The Rise of the Phoenix: Methodological innovation as a discourse of renewal, Journal of Information Technology 22(1): 59–68.

Watts, D.J. (1999). Networks, Dynamics and the Small-world Phenomenon, American Journal of Sociology 105(2): 493–527.

## About the authors

Agnes Koschmider is a senior researcher (PostDoc) at the Institute of Applied Informatics and Formal Description Methods, at Karlsruhe Institute of Technology (KIT), Universita¨t Karlsruhe (TH). Her current research concentrates on methods that assist users during business process modeling. After her Ph.D. in 2007 she joined the group of Wil van der Aalst at TU Eindhoven and the group of Oscar Pastor at TU Valencia for research visits. Agnes Koschmider has served as a reviewer in many international conferences and journals, and co-organized national and international conferences (e.g., INFORMATIK 2003, BTW 2005, WI 2007). She is an elected member of the GI (German Society for Informatics) presidium since 2006.

Minseok Song is a research professor in the Institute of Public Policy and Information Technology at Seoul National University of Technology. Before that, he worked as a postdoctoral researcher in the Information Systems group at Eindhoven University of Technology. His research interests include workow, business process management, process mining, process knowledge management, simulation, BPR, and social network analysis. He published articles in Information Systems, Decision Support Systems, Computer Supported Cooperative Work, Computers in Industry, and other journals.

Hajo A Reijers is an associate professor in the Information Systems group at Eindhoven University of Technology and an Affiliated Professor with the TIAS/Nimbas Business School of Tilburg University. Before that, he worked as a management consultant for Accenture and Deloitte. His research interests cover business process redesign, business process modeling, workflow management technology, and simulation. He has published over 75 refereed papers, for example in the Journal of Management Information Systems, Information systems, Data & Knowledge Engineering, and Organization Studies.
