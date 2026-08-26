---
otero_id: 2052
otero_key: "PHX6KRAH"
title: "Collective taxonomizing: A collaborative approach to organizing document repositories"
authors: "Harris Wu; Michael D. Gordon; Weiguo Fan"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.031"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collective taxonomizing: A collaborative approach to organizing document repositories

Harris Wu <sup>a,</sup>⁎, Michael D. Gordon <sup>b</sup>, Weiguo Fan <sup>c</sup>

<sup>a</sup> Old Dominion University, Norfolk, VA 23508, USA

<sup>b</sup> University of Michigan at Ann Arbor, Ann Arbor, MI 48109, USA

<sup>c</sup> Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, USA

## a r t i c l e i n f o

Article history: Received 26 November 2009 Received in revised form 17 August 2010 Accepted 24 August 2010 Available online 28 September 2010

Keywords: Collective taxonomizing Web 2.0 Design science Structural knowledge Knowledge management

## a b s t r a c t

Keeping large, growing document repositories organized is a critical challenge. For example, the security failure prior to the 9/11 tragedy was partly due to the ineffectiveness of organizing documents shared among various intelligence organizations. Drawing on the success of Web 2.0 and theories from knowledge management, we argue that a shared document repository with no central organizer may bene<sup>fi</sup>t from collective taxonomizing: allowing community members to categorize documents with local document hierarchies and systematically coalesce those local hierarchies into a global taxonomy. Using a design science approach, we develop and evaluate a hierarchy coalescing algorithm. Empirical and analytical evaluation shows promise.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

An electronic document repository is the centerpiece of today's knowledge-based decision making systems [18]. Organization of documents in a repository is important to knowledge acquisition, storage, retrieval, transfer and knowledge-based decision making. However, often a repository contains documents shared by multiple organizations or individuals and has no one responsible for organizing its growing contents. Organizing documents in a shared document repository is a dif<sup>fi</sup>cult problem. For example, the security failure prior to the September 11 tragedy was partly due to the ineffectiveness in organizing the documents shared among various intelligence organizations [7].

Browsable hierarchies, or taxonomies, are much needed in shared document repositories even as keyword-based full-text search is available [14]. Taxonomies are particularly important for collections of multimedia documents which lack searchable textual description, such as diagrams, spreadsheets, presentations, images, video recordings or any types of binary <sup>fi</sup>les prevalent in today's document repository systems. Taxonomies allow users to not only browse and search these multimedia collections, but also comprehensively retrieve all items on a given topic within the entire repository. Taxonomies allow users to retrieve information by traversing a path of categories, which in cognitive terms requires only recognition instead of the recall of keywords.

Today's shared document repositories are taxonomized in two ways [37]. One way is to place all shared documents in a global hierarchy of categories. The other way is to let community members categorize documents into their own hierarchies and optionally share their hierarchies with each other. Both have their limitations. The global hierarchy approach suffers from the incompatibility of individual perspectives. The local hierarchy approach suffers from the lack of a single, global view containing the entire repository.

A new thrust in presenting and organizing information on the Web is to use the knowledge that is “out there” among Internet users. As illustrated by wikipedia.com, the largest online encyclopedia, a large diverse group of people can do better than a small team of experts. The ability to create something of high quality and emergent from individual users' knowledge and actions or to harness collective intelligence, is one of the core competencies of “Web 2.0” [37]. Our work is strongly of this Web 2.0 spirit. We suggest that when it is not possible (and often not desirable) for a document repository to be organized centrally, distributed organization is a powerful technique. As every individual user of a repository puts effort into organizing a part of the collection, combining their structural knowledge and efforts offers a powerful alternative to central or content-based methods of organizing information.

We intend to make the following contributions. First, we bring structural knowledge into the spotlight as an important type of knowledge to be fostered in a document repository. We use Nonaka's [23] knowledge creation framework to model how a shared document repository may support structural knowledge creation. As part of this modeling process we highlight the importance of combining structural knowledge embedded in distributed local document hierarchies. Second, we propose a collective approach to taxonomizing documents in a shared document repository and fostering structural knowledge creation by allowing for overlapping local document hierarchies and automatically constructing a global hierarchy from these local ones. Third, we design a hierarchy coalescing algorithm by choosing from a large pool of hierarchical clustering methods using a Design Science approach [22]. Fourth, using both quantitative and qualitative methods, we evaluate the collective taxonomizing approach in a knowledge creation environment. We evaluate the hierarchy coalescing algorithm through <sup>fi</sup>tness check, feasibility and usability validation, comparative studies, and robustness and scalability checks.

## 2. Taxonomizing a shared document repository

How documents are organized (i.e. the structure of a document repository) affects whether users can ef<sup>fi</sup>ciently utilize the repository to support their knowledge tasks. Humans rely on structures in cognitive processes including encoding, storage and recall [1]. Just as human organizations and knowledge domains often have a hierarchical nature, a document repository often utilizes a global hierarchy to organize the document collection. A global hierarchy's full, uniform view of the repository provides knowledge workers a common reference, which is important for decision making and collaboration within a community.

There are several challenges associated with relying on a manually maintained global hierarchy. From a cognitive perspective, a single hierarchy cannot accommodate all con<sup>fl</sup>icting viewpoints of knowledge workers or organizations. A single hierarchy adds a cognitive load to individuals who need to map the way they would organize information onto the way the hierarchy does. From a knowledge management perspective, the knowledge within a document collection is distributed and emergent rather than centralized and static [33]. It is impractical to have a central process responsible for collecting and maintaining local information. From a cost-benefit and management perspective, the effort to create and maintain a global hierarchy can often be prohibitive. In an inter-organizational environment, such as the intelligence community that constitutes many independent organizations, there may not be any single authority responsible for such efforts. From a change management perspective, maintenance of a global hierarchy, whether by a central authority or contributors, can be very dif<sup>fi</sup>cult for a growing document collection to which new documents are added frequently. Over time, even the most organized global hierarchy will suffer slow decline and death if the hierarchy is not well maintained or if the hierarchy becomes outdated by evolving topics. The latter concern is inevitable for a knowledge community with emerging interests, such as the information systems research community [2].

A local document hierarchy, on the other hand, is created by an individual worker or organizational unit and includes a subset of documents in the repository. Local hierarchies present personal views of the repository that suit the speci<sup>fi</sup>c interests of different workers, organizations, or groups engaged in common knowledge tasks. Local hierarchies are maintained by local authorities who are motivated to make the hierarchies useful for their knowledge work. Local hierarchies can be modi<sup>fi</sup>ed at the same time when individuals contribute new documents to the repository.

However, even with local hierarchies available, it is still desirable to have a global hierarchy for the entire collection. While a local hierarchy only provides an incomplete and possibly idiosyncratic view, a global hierarchy provides a complete, uniform view to all documents. A global hierarchy is not only a framework for categorizing content but is also a strategy to unify multiple constituencies. Some state-of-the-art repositories such as SharePoint™ support both local hierarchies and a manually maintained global hierarchy. However, to utilize both hierarchies a document must be <sup>fi</sup>led twice: once in a local hierarchy and once in the global hierarchy. Such duplicate <sup>fi</sup>ling involves signi<sup>fi</sup>cant costs.

One may argue that search engines can support information retrieval in place of document hierarchies. However browsing has its own value and cannot be replaced by search [13]. Even though fulltext and hyperlink-based search have been widely successful, nontextual documents such as images and videos are still largely not amenable to search engines [39]. Search in multimedia collections is aided by the recent development of social tagging systems, where Web users assign free-formed labels to documents and utilize these labels in keyword searches. Although supporting casual discovery, tags do not have hierarchical structures that allow for purposeful exploration. Indeed, the most notable de<sup>fi</sup>ciency of popular tagging systems is their inability to organize tags hierarchically. This severely limits the knowledge that can be created, embedded and reused through tags. Recent research has proposed social hierarchies [37], which allow users to share personal document or bookmark hierarchies with others, as opposed to social tagging.

We argue that in a shared document repository it is bene<sup>fi</sup>cial to allow for locally managed hierarchies, and then algorithmically merge these local hierarchies into a global hierarchy. When local hierarchies overlap with each other, the global hierarchy reconciles the con<sup>fl</sup>icting categorizations. We call this approach “collective taxonomizing”. Local hierarchies provide a means for users to maintain control over the documents of immediate interest to them. The global, system-generated hierarchy provides an unobtrusive way for users to collaboratively organize the whole collection. Unlike manually created hierarchies, a system-generated hierarchy can be updated frequently at a minimal cost. To our knowledge, determining how to algorithmically build a global hierarchy from many overlapping local document hierarchies is a new research problem.

## 3. Building structural knowledge in a document repository

Organizing documents contained in repositories can also be studied from the perspective of structural knowledge. Structural knowledge, also called relational knowledge, is de<sup>fi</sup>ned as the knowledge of how elements within a domain are interrelated [8]. Structural knowledge is a building block of cognition. The relationships among information in memory have been viewed as cognitive structures or knowledge structures, which are essential to recall and comprehension. Schema theory [25] claims that knowledge is stored in information packets called schemas, and it is the interrelationships among schemas that give them meaning. While a theoretical construct, structural knowledge can be represented in tangible structures. In an online document repository, structural knowledge can be elicited by allowing individuals to categorize documents with hierarchies [31]. For example, the way that an intelligence analyst organizes documents in their local document hierarchy embeds the analyst's personal, implicit knowledge by indicating how she believes information in these documents is interrelated. Similarly, structural knowledge of a central authority can be embedded into a global hierarchy. Once represented in tangible structures, structural knowledge can bene<sup>fi</sup>t others. Much educational research has been devoted to the conveyance of structural knowledge. An expert's explicit organization of subject matter functions as a scaffold for others to assimilate information they hope to learn. Many studies have linked conveyance and acquisition of structural knowledge to problem solving performance [19,34].

Building and sharing structural knowledge among a repository's user community is therefore critical. In fact, knowledge sharing and reuse can all be considered as part of a continuous knowledge creation cycle. In Nonaka's “spiral” model [23] for organizational knowledge creation (Fig. 1), knowledge is created through a cycle of four intertwining modes of conversion between tacit (unexpressed) and explicit (expressed) knowledge: externalization, internalization, socialization and combination. Internalization refers to the conversion of explicit knowledge into tacit knowledge, which corresponds to learning, understanding or sense-making. Externalization refers to the expression of tacit knowledge as explicit knowledge, or codi<sup>fi</sup>cation. Socialization refers to creating tacit knowledge through social interactions and shared experience. Combination refers to creating explicit knowledge from other explicit knowledge, through merging, categorizing, sorting, or re-contextualizing.

A cycle of structural knowledge creation in a document repository can be modeled as follows. Users can internalize structural knowledge from documents and hierarchies. They assimilate structural knowledge by reading and learning from documents and understanding their relationships to other documents in the hierarchy. Often, this requires utilizing contextual information from personal experience that goes beyond what is explicit in the document collection. A user's tacit structural knowledge thus assimilated can be externalized by a local document hierarchy, which can then be shared with others. Sharing local document hierarchies or collaboratively building them contributes to the socialization process among repository users. Existing document repository systems support internalization, externalization and socialization to various degrees (Fig. 2).

However, no existing repositories effectively support combination of explicit structural knowledge contained in local document hierarchies. Except for a few experts whose structural knowledge may be represented in a centrally-managed taxonomy, users cannot effectively share their dynamic, up-to-date structural knowledge with their community. Without combination, the cycle of assimilating, combining and disseminating structural knowledge is missing a crucial link (Fig. 2). This missing link is a cause of deteriorated organization in many existing repositories, which eventually leads to information overload, costprohibitive knowledge reuse, and a vicious knowledge cycle. In the remainder of this paper, we design and evaluate an algorithm supporting the combination of explicit structural knowledge embedded in the local hierarchies. We believe that a large diverse group of people has more structural knowledge and, if aided by a proper knowledge combination mechanism, can do better than a small central team of experts in taxonomizing a large document repository.

## 4. The hierarchy coalescing algorithm

Our goal is to build a global hierarchy of documents that coalesces individual users' local hierarchies. When local hierarchies overlap with each other, the global hierarchy attempts to reconcile con<sup>fl</sup>icting categorizations. We call our algorithm a hierarchy coalescing algorithm. We do not claim to invent a brand new statistical technique. Rather, we try to methodologically achieve the best design by treating design as a search process among a large pool of alternatives [15]. In this section we review extant research, present the algorithm, and justify our design choices.

## 4.1. Literature review

The generation of a coalesced hierarchy can be considered a document clustering problem, which has been the focus of many studies in the areas of text mining and information retrieval [27]. Based on cognitive principles Andersen concludes: “retrieval of information is facilitated if it is organized hierarchically” [1].

There are both agglomerative and divisive hierarchical clustering methods [12]. Agglomerative methods merge similar objects into groups and eventually merge all groups into a single cluster. Divisive methods start from a single cluster that contains all objects and divide clusters into smaller clusters. Divisive techniques are not widely used because it is dif<sup>fi</sup>cult to <sup>fi</sup>nd effective rules to divide the clusters, and those rules are usually arbitrary [12]. Agglomerative methods have been more popular and successful with hierarchical document clustering for information retrieval [29].

Most clustering methods utilize document content such as a document-keyword matrix as the input data [28]. However, it is dif<sup>fi</sup>cult to apply content-based clustering to non-textual documents such as spreadsheets and images. Content-based clustering overlooks any additional information users could add as they work with documents and the collection. With the advent of the Web, the hyperlink structure among web documents or user access logs has been used as the clustering input [35,36].

Document hierarchies contain rich information that can be used by document clustering or other data mining techniques. However, to our knowledge, no one has applied data mining to individual user's hierarchies in a document collection to construct a new hierarchy at a higher level of generality. The coalesced hierarchy may <sup>fi</sup>nd two seemingly unrelated documents from different local document collections relevant to the same topic. Coalesced hierarchy therefore allows users to not only recall a comprehensive list of documents on a given topic, but also make serendipitous discoveries. A “transportation security” category in the coalesced hierarchy for intelligence community's shared documents, for example, might have connected <sup>fi</sup>ndings from various agencies and warned analysts of Al Qaeda's hijacking plans.

![](/api/attachments/PHX6KRAH/fulltext/images/ea332ff54c137a5eba5041862e2f1eabfb03770c0117ed77feaaaab5efda54fa.jpg)  
Fig. 1. Nonaka's [23] spiral model for organizational knowledge creation.

![](/api/attachments/PHX6KRAH/fulltext/images/9b38340e11d3eb8efea2ea0ba08431e35896aa76b8ff06125db628283d1d0578.jpg)  
Fig. 2. Building structural knowledge in a document repository.

## 4.2. The hierarchy coalescing algorithm

The coalescing algorithm produces a global hierarchy through agglomerative hierarchical clustering of documents from local hierarchies. For clarity of presentation, we demonstrate the algorithm using a small example before discussing the design rationale and alternatives in the next section. Fig. 3 describes the details of the algorithm.

The algorithm <sup>fi</sup>rst captures the structural information from local hierarchies in a document-category matrix. Table 1 shows our example of 3 local hierarchies created by three different organizations containing 7 documents, and the corresponding document-category matrix. Documents are represented by vectors such as (0, …, 1, …, 0), where 1 indicates that the document belongs to a certain category. Note that local hierarchies overlap with each other. For example, document 1 is in both hierarchies A and B.

Second, the algorithm computes the pair-wise dissimilarities between documents. We de<sup>fi</sup>ne the similarity using the Jaccard measure [17]. The Jaccard similarity between two vectors (sets of attributes) X and Y is de<sup>fi</sup>ned as |X∩Y|/|X UY|. In other words, the Jaccard similarity between two documents X and Y is the number of categories that contain both document X and Y divided by the number of categories that contain either X or Y. In our example, the similarity between documents 1 and 2 is 1/3: there is only one category (A1) that contains both documents 1 and 2, hence X∩Y=1; there are three categories that contain either document 1 or 2, hence X UY=3. We de<sup>fi</sup>ne dissimilarity as 1 similarity. The dissimilarity between documents 1 and 2 is 1−1/3=2/3. The Jaccard dissimilarity between any two documents ranges between 0 and 1, with 0 being the most similar (identically categorized) and 1 being totally dissimilar (no co-occurrence in any category). Note that the dissimilarity between a document and itself is always 0. Table 2 shows the pair-wise dissimilarity matrix for the sample documents given in Table 1.

Third, the algorithm recursively merges the most similar documents into groups, and re-computes the pair-wise dissimilarities at each step. We choose to use the Average Linkage method [17] to merge similar groups until all shared documents are merged into a single group. In the Average Linkage method, the dissimilarity between two groups is de<sup>fi</sup>ned as the average dissimilarity between all document pairs between two groups. Table 3 shows the merging process. At Step 0, each document belongs to its own group. At Step 1, the pair with the smallest pair-wise dissimilarity is chosen to merge. If several pairs have the same smallest dissimilarities, one pair is randomly chosen. Groups 3 and 4 are merged at Step 1 at a dissimilarity of 0.333. We use the smaller group label for the merged group. Both of these groups now have a category label 3. After each merging step, the pair-wise dissimilarity matrix is updated and new dissimilarities between groups are calculated using the Average Linkage method. At Step 2, groups 5 and 7 are merged at a dissimilarity of 0.5. At step 3, groups 3 and 5 are merged at a dissimilarity of 0.625. The merging process goes on until all documents are merged into one group.

Fourth, the algorithm obtains the coalesced hierarchy by reversing the merging steps from the final group to individual documents. Table 4 shows the resulting hierarchy, or so-called dendogram. The horizontal axis in the dendogram is a scaled representation of dissimilarity between groups in the merging process. The merged hierarchy allows users to recall a comprehensive list of documents on a given topic. For example while separate hierarchies have placed documents 1 and 6, 1 and 2, and 2 and 6 in the same categories, the coalesced hierarchy places 1, 2 and 6 in the same category. While not shown in the example, it is worth-noting that the above clustering procedure preserves the original local structures. If a local hierarchy or its subhierarchy did not share any documents in common with any other local hierarchies, then this hierarchy would remain intact as a subhierarchy within the coalesced hierarchy.

Last, the algorithm labels the categories in the coalesced hierarchy. While our present focus is on how to build a coalesced structure, the categories need to be textually labeled to be meaningful to knowledge workers. The labeling process is as follows. A local sub-hierarchy that does not share any documents in common with other local hierarchies will remain intact through the clustering process. We assign the original category labels supplied by their creators to these intact local sub-hierarchies. For a category in the coalesced hierarchy that contains documents from multiple local hierarchies, we collect the titles of underlying documents within that category and also the labels of local categories that contain these documents. We use a simple keyword extraction method, which chooses the four most frequent keywords from the collection of titles to label the given category. A con<sup>fi</sup>gurable exclusion list <sup>fi</sup>lters out words such as ${ \ " } { \sf a } { \ " } ,$ “the”, or keywords common to the whole document collection. At this step, repository documents not belonging to any local hierarchies are added to the coalesced hierarchy under a <sup>fi</sup>rst-level category labeled “Uncategorized”.

<table><tr><td>Local hierarchies</td><td>→</td><td>Document-category matrix</td><td>→</td><td>Dissimilarity matrix</td><td>→</td><td>Hierarchical clusters</td><td>→</td><td>Global hierarchy</td></tr><tr><td colspan="9">Input: k local hierarchies, containing n categories and m documents in total.1. Construct an m x n document-category matrix A.  $A_{ij} = 1$  iff. document i belongs to category j. Each of the m documents is represented by a row vector  $A_i$  of size 1 x n, i = 1, ... m.2. Computes the pair-wise Jaccard dissimilarities between document vectors, and store the results into an m x m matrix B.  $B_{ij} = 1 - |A_i \cap A_j| / |A_i \cup A_j|$ .3. Merges the most similar documents into groups, and re-computes the pair-wise similarities at each step.3a. Start with m clusters, each containing a single entity (document), and the m x m dissimilarity matrix B.3b. Search the dissimilarity matrix for the most similar pair of clusters. Let the most similar clusters be u and v.3c. Merge clusters u and v. Label the newly formed cluster (uv). Update the entries in the similarity matrix by deleting the rows and columns corresponding to clusters u and v and adding a row and column giving the dissimilarities between (uv) and remaining clusters.3d. Repeat Steps 3b and 3c m-1 times. Record the identity of clusters merged and the dissimilarity levels at which the merges take place.3e. All documents will be in a single cluster at termination of the algorithm.4. Obtains the hierarchy by reversing the merging steps from the final group to individual documents. Reversal stops when a predefined maximum level of depth is reached, or when the number of documents in a category is less than a predefined minimum category size.5. Labels the categories in the generated hierarchy recursively as follows.5a. Starts from the top of the Coalesced hierarchy.5b. For each child of the current node, C, label the category using Steps c and d. Children are defined as the categories directly below a given node.5c. If the sub-hierarchy (defined as all categories and documents below a given node) below C belong to a single local hierarchy exclusively, then: all the categories in the sub-hierarchy, including C, are labeled using the original category names in the local hierarchy.5d. Else, extract all keywords from titles of all documents under C, excluding keywords from a pre-defined word list (words such as “the”, “a”, etc.). Rank them by frequency of occurrence. Concatenate the top 4 ranked keywords, with spaces in between, as the label of the category.5e. Go back to Step b, to label all children of C.Output: A global hierarchy containing m documents.</td></tr></table>

Fig. 3. The hierarchy coalescing algorithm.

## 4.3. Alternative techniques

Design is a search process to choose best available means to reach desired ends [15]. Building a coalesced hierarchy is a clustering problem which involves three basic steps: a) obtain the data set; b) compute pair-wise similarity (or dissimilarity/distance); c) execute the clustering method. Below we explore the many design alternatives in each step and theoretically argue for our design choice.

## 4.3.1. Alternative input data

To accomplish our goal of combining structural knowledge, we use the document-category association embedded in local document hierarchies as the input. The most popular clustering method in information retrieval literature is the Cosine–Centroid [28] method utilizing document-keyword vectors as the input. During evaluation we will compare our technique against the content-based Cosine–Centroid method to see which one generates clusters that better <sup>fi</sup>t the respective original data.

## 4.3.2. Alternative similarity measures

There can be many different ways to compute the similarity or dissimilarity between the documents represented by documentcategory vectors. For example, the similarity can be measured by Euclidean distance or cosine. Our choice of the Jaccard similarity measure is derived from two assumptions and the design requirement of our algorithm. Our assumptions concur with the informationtheoretic basis of similarity [21].

First we assume that the “structural” similarity between two documents a and b in a collection of categories C should be determined by their commonality and difference in the way they are categorized. The commonality, c, can be represented by the number of common categories in C that both documents belong to. The difference, d, can be represented by the number of distinct categories in C that only one of the two documents belongs to. We use t to denote totality, de<sup>fi</sup>ned as the total number of categories that contain either or both of the documents: t=c+d. The similarity s between a and b in C should be a function of c and t:

$$
s (a, b, C) = \mathrm{g} (c, t) \quad \mathrm{t} > 0, t \geq c \geq 0.\tag{i}
$$

Second we specify the numeric range of the similarity measure to be [0, 1]. If two documents have no commonality, then the similarity between them should be 0. The similarity between two identical objects should be 1. That is,

$$
\mathbf {g} (0, t) = 0, \quad \mathbf {g} (t, t) = 1.\tag{ii}
$$

Many similarity measures, including Cosine and normalized Euclidean, satisfy these two assumptions. Now recall that the goal of our algorithm is to merge local document hierarchies. Therefore the similarity between two documents needs to be compatible with aggregation of document collections. To illustrate aggregation, suppose a larger collection of categories C consists of two sub-collections, C1 and C2. In C1, documents a and b have similarity ${ \sf s } _ { 1 } = { \sf g } \left( c _ { 1 } , t _ { 1 } \right)$ . In $C 2 ,$ documents a and b have similarity ${ \sf S } _ { 2 } = { \sf g } ( c _ { 2 } , t _ { 2 } )$ . Then the overall similarity between a and b in C should be a weighted average of their similarities, $s _ { 1 }$ and $s _ { 2 } ,$ in two respective collections C1 and C2. This aggregation requirement stipulates that the similarity between a pair of documents should be fairly determined when local hierarchies are merged. Naturally the weight should be based on their commonality and difference in both category collections. We use totality t as the weight. That is, we require:

Table 1  
An example of 3 hierarchies with seven documents in total.

<table><tr><td colspan="3">Hierarchy A</td><td colspan="3">Hierarchy B</td><td colspan="3">Hierarchy C</td></tr><tr><td>A1:</td><td></td><td></td><td>B1:</td><td></td><td></td><td>C1:</td><td></td><td></td></tr><tr><td>Document-1</td><td></td><td></td><td>Document-1</td><td></td><td></td><td>Document-2</td><td></td><td></td></tr><tr><td>Document-2</td><td></td><td></td><td>Document-6</td><td></td><td></td><td>Document-6</td><td></td><td></td></tr><tr><td>A2:</td><td></td><td></td><td>B2:</td><td></td><td></td><td>C2:</td><td></td><td></td></tr><tr><td>Document-7</td><td></td><td></td><td>Document-3</td><td></td><td></td><td>Document-7</td><td></td><td></td></tr><tr><td>A2.1</td><td></td><td></td><td>Document-5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Document-3</td><td></td><td></td><td>Document-7</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Document-4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A2.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Document-5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>A1</td><td>A2</td><td>A2.1</td><td>A2.2</td><td>B1</td><td>B2</td><td>C1</td><td>C2</td></tr><tr><td>Doc1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Doc2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Doc3</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Doc4</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Doc5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Doc6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Doc7</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td colspan="9">Document vectors, or the document-category matrix</td></tr></table>

$$
g (c _ {1} + c _ {2}, t _ {1} + t _ {2}) = g (c _ {1}, t _ {1}) ^ {*} t _ {1} / (t _ {1} + t _ {2}) + g (c _ {2}, t _ {2}) ^ {*} t _ {2} / (t _ {1} + t _ {2}).\tag{iii}
$$

Now we prove that only the Jaccard measure ful<sup>fi</sup>lls the aggregation requirement:

Theorem. If a similarity s between documents a and b in collection C satis<sup>fi</sup>es Assumptions (i), (ii) and (iii), then s = c/t. That is, s is the Jaccard similarity between a and b.

Proof. Suppose we split the collection C into C1, which includes all categories that contain both a and b, and C2, which includes other categories. The similarity between a and b in C1 is g(c, c), and the similarity in C2 is g(0, d). Note that c +d=t. Then,

$$
\begin{array}{l} s = g (c, t) = g (c + 0, c + d) \\ \quad = g (c, c) ^ {*} c / (c + d) + g (0, d) ^ {*} 0 / (c + d) \\ \quad = g (c, c) ^ {*} c / (c + d) = 1 ^ {*} c / (c + d) = c / t. \end{array}
$$

## 4.3.3. Alternative clustering methods

Alternative techniques for building a coalesced hierarchy may use the same input data matrix and Jaccard similarity (dissimilarity) measure, but another clustering method. In addition to average linkage, other popular clustering methods include Single Linkage, Complete Linkage, Centroid, and Ward's method [17]. Each of these methods has a different way to determine the distance, or dissimilarity, between any two clusters of objects. Since the two clusters with the minimum cluster distance are chosen for merging at each step, different clustering methods result in different coalesced hierarchies.

In Single Linkage, the distance between two clusters is de<sup>fi</sup>ned as the smallest distance between any pair of inter-cluster objects. Two clusters can be merged because of one similar inter-cluster document pair, even if all other document pairs are very dissimilar. This results in a “chaining” phenomenon. It can be said that Single Linkage assumes that clusters are well separated, which does not hold for documents in a typical shared repository.

In Complete Linkage, the distance between two clusters is de<sup>fi</sup>ned as the maximum distance between any pair of inter-cluster objects.

Table 2  
The pair-wise dissimilarity matrix.

<table><tr><td>Document</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1</td><td>0</td><td>0.667</td><td>1</td><td>1</td><td>1</td><td>0.667</td><td>1</td></tr><tr><td>2</td><td>0.667</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0.667</td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>0</td><td>0.333</td><td>0.500</td><td>1</td><td>0.500</td></tr><tr><td>4</td><td>1</td><td>1.00</td><td>0.333</td><td>0</td><td>0.750</td><td>1</td><td>0.750</td></tr><tr><td>5</td><td>1</td><td>1</td><td>0.500</td><td>0.750</td><td>0</td><td>1</td><td>0.500</td></tr><tr><td>6</td><td>0.667</td><td>0.667</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>7</td><td>1</td><td>1</td><td>0.500</td><td>0.750</td><td>0.500</td><td>1</td><td>0</td></tr></table>

Recall that two documents with no co-occurrence in the same category are considered totally dissimilar by the Jaccard measure. Hence Complete Linkage applied on the Jaccard similarity matrix results in a large number of small “strongly connected” clusters.

With the Centroid method, the distance between two clusters is de<sup>fi</sup>ned as the dissimilarity between their centroids, which can be thought of as the “centers” of these clusters. Because the documentcategory vectors are binary vectors, the centroid of document clusters has to be calculated as medoid, a binary vector whose element at each position is the median of the values in document vectors at the same position. The medoid is a rather imperfect approximation to the centroid, especially when the number of documents in a cluster is relatively small. Another disadvantage of the Centroid method is that the distance at which clusters are combined can actually decrease from one step to the next. That would imply that document clusters merged at early stages can be more dissimilar than those merged at later stages, which is not a desirable property. In a coalesced hierarchy, we would like the categories at lower levels to be more similar to each other than categories at higher levels.

In Ward's method, the medoid is <sup>fi</sup>rst calculated for each cluster. Each pair of clusters is then tentatively linked and the medoid is determined for the combined cluster. At each step, the two clusters that actually merge are those which result in the smallest increase in the overall sum of the squared within-cluster Euclidean distances. Ward's method has a strong tendency to create clusters of the same size, or so-called spherical clusters. In other words, Ward's method tends to impose a spherical structure on the coalesced hierarchy. Since there may be both large and small topics in a document repository, we would like the coalesced hierarchy to be free of any imposed structures.

We chose the Average Linkage method because it mostly likely results in reasonable clusters. The Average Linkage method has recently been shown to perform better than others in keyword-based document clustering algorithms for information retrieval [20].

## 4.3.4. Alternative labeling methods

Labeling document clusters has been a challenge to cluster-based retrieval mechanisms. Typically a cluster is represented by a sample of documents from the cluster or/and a set of automatically generated descriptive keywords [14]. We chose a simple keyword extraction method using document titles. There has been increasing research attention on the labeling of document clusters. Most of these efforts use weighting strategies to select top candidate keywords or phrases from the cluster of texts for cluster labeling [24]. Document summarization is another <sup>fl</sup>ourishing <sup>fi</sup>eld [38]. Our category labeling procedure can be improved with ongoing advancements in these <sup>fi</sup>elds. Category labeling will be a focus in our future research.

The agglomeration schedule.

<table><tr><td>1 2 3 4 5 6 7</td><td>-</td><td>Step 0</td></tr><tr><td>1 2 3 3 5 6 7</td><td>0.333</td><td>Step 1</td></tr><tr><td>1 2 3 3 5 6 5</td><td>0.500</td><td>Step 2</td></tr><tr><td>1 2 3 3 3 6 3</td><td>0.625</td><td>Step 3</td></tr><tr><td>1 2 3 3 3 2 3</td><td>0.667</td><td>Step 4</td></tr><tr><td>1 1 3 3 3 1 3</td><td>0.667</td><td>Step 5</td></tr><tr><td>1 1 1 1 1 1 1</td><td>1.00</td><td>Step 6</td></tr></table>

Table 4 The dendogram output from SPSS® using Average Linkage.  
![](/api/attachments/PHX6KRAH/fulltext/images/432b4afeb18885b2d2f55ff9b2c93826752918acf80e124217bc12affb2a6e38.jpg)

Design is a search process to discover an effective solution to a problem [15]. We have de<sup>fi</sup>ned our problem as a hierarchical document clustering problem: how to construct a global hierarchy of documents that combines overlapping local hierarchies of smaller document collections. We have searched for various means to address this problem. For a document similarity measure, we formalized our goal mathematically and were able to prove Jaccard similarity as the optimal choice. For clustering and labeling methods, the sheer size and complexity of the solution space forced us to search for satisfactory solutions, or to satis<sup>fi</sup>ce [15]. For clustering methods we found average linkage as the most appropriate, which was in agreement with existing design knowledge in content-based clustering [20]. For category labeling, our design started from a ranked keyword listing, which would be suf<sup>fi</sup>cient in proving the viability of our approach. The labeling issue will be further studied in future research.

Build and evaluate are the two design processes in the design science research [22]. In the next two sections we will evaluate the usefulness and “goodness” of the hierarchy coalescing algorithm.

## 5. Evaluation of a collective taxonomizing system

To con<sup>fi</sup>rm the usefulness of the collective taxonomizing approach, we would like to verify two things. First, we want to con<sup>fi</sup>rm that a local hierarchy indeed embeds an individual's rich structural knowledge about the repository and, therefore, effectively supports their knowledge work. Second, we want to con<sup>fi</sup>rm that the coalesced hierarchy is able to combine various individuals' structural knowledge in a way that proves useful to the entire community of repository users.

We developed a prototype system utilizing the hierarchy coalescing algorithm and deployed the system in an academic document repository. Through automated data collection and user interviews, we evaluated whether local hierarchies and the coalesced hierarchy were indeed useful. The prototype system also functioned as a data collection vehicle to support further evaluation of the hierarchy coalescing algorithm.

## 5.1. A prototype collective taxonomizing system

We developed our system on top of Everything (everything2.org), a state-of-the-art open-source content management system. Everything allows a system administrator to create a taxonomy containing prede<sup>fi</sup>ned categories and allows users to contribute documents to the taxonomy and construct hyperlinks among documents. This system has sophisticated search functionality for document retrieval and can capture user feedback through a non-intrusive voting mechanism. In addition, Everything has many add-on modules contributed from the open-source community.

We installed an add-on module that allows users to build their local document hierarchies and share these hierarchies with each other. We further enhanced Everything's document organization capability by providing a system-coalesced hierarchy. We also implemented a logging feature to record all user click-streams.

We chose to deploy our system on a class website (Fig. 4) for a Database Management course used by 45 students. Students were ideally suited to acquire and create new knowledge and could be directly motivated to share it with others. A class environment allowed us to closely observe a group of individuals who were spending a considerable amount of time daily on knowledge acquisition and creation. The students contributed over a thousand documents during the semester in a variety of media formats (.ppt, . doc, .pdf, .avi, .jpeg, .txt, etc.). Students could use search, hyperlink, and hierarchies to navigate this shared document repository. They could search for documents by keywords or various attributes such as author and creation time, could browse the “recent contributions” section on the website by following system-created hyperlinks and could follow author-created hyperlinks among contributions.

Besides using search and hyperlinks, students could navigate hierarchies on the right-hand side of the webpage, just as they could navigate a <sup>fi</sup>le system using Microsoft Windows Explorer. Each student could build a personal hierarchy to categorize documents of interest to them, which could include documents submitted by anyone in the class. Students could also use a class hierarchy, the coalesced hierarchy generated daily from individuals' personal hierarchies. In addition, students could browse the collection of documents using a time hierarchy, which arranged documents based on the week in the semester when they were contributed. The time hierarchy roughly represents class topics by the week they were presented throughout the semester. Using the time hierarchy is functionally equivalent to searching for documents based on creation time or browsing the “recent contributions” section. However, navigating the hierarchy may be less effort-consuming than searching or following hyperlinks. The time hierarchy was provided as a control instrument in our study to provide a baseline for comparing hierarchy against other navigation mechanisms.

## 5.2. Research hypotheses

We designed a research-intensive knowledge creation task for students. The assignment was an individual research paper for which most documents in the repository would be potentially useful. Students focused on this assignment for the last month of the semester. We made several hypotheses based on the structural knowledge creation model developed earlier in this paper.

First and foremost, we wanted to <sup>fi</sup>nd out (qualitatively) whether students <sup>fi</sup>nd the collective taxonomizing approach helpful to their learning:

H1. Students <sup>fi</sup>nd personal hierarchies and coalesced hierarchy helpful to their learning.

The premise of the collective taxonomizing approach is that users can externalize their structural knowledge into local hierarchies. Users' structural knowledge partly comes from the internalization of knowledge embedded in repository documents. We hypothesize:

H2. Personal hierarchies cover N50% of the documents in the repository. H3. The documents contained in personal hierarchies have higher-thanaverage quality.

If the structural knowledge in local hierarchies can be combined, students would frequently use the coalesced hierarchy and bene<sup>fi</sup>t from using it:

H4. Students would utilize the coalesced hierarchy more frequently than the time hierarchy. While the look and feel of these hierarchies are the same, the coalesced hierarchy contains combined structural knowledge that encodes meaningful relationships among documents.

H5. The coalesced hierarchy is more likely to lead users to higher quality documents than hyperlinks, search or the time hierarchy. Different navigation mechanisms provide different social, contextual cues about a document. For example, before a student follows a hyperlink contained in a document, the context around the hyperlink suggests the usefulness of the destination. Documents retrieved through keyword search are related to the keyword query. In contrast, the coalesced hierarchy works implicitly as a recommender system based on the structural knowledge of all contributing users. Before a student retrieves a document from the coalesced hierarchy, the student knows the topical relationship between this document and other documents in the repository. We believed that the structural knowledge embedded in the coalesced hierarchy provides richer cues than time or keyword association, and are hence more likely to lead students to documents useful to their work.

Last and most importantly, we believe that knowledge is created from building (externalizing) the personal hierarchies and using (internalizing) the coalesced hierarchy. The results of knowledge creation (i.e. the research papers and the class performance) should be correlated with the usage of personal hierarchies and the coalesced hierarchy:

H6. A student's term paper quality and overall class performance are both positively correlated to the number of documents within personal hierarchy.

H7. A student's term paper quality and overall class performance are both positively related to the usage frequency of the coalesced hierarchy.

## 5.3. Data collection and results

At the end of the semester, the website contained 1049 documents and 45 local hierarchies. Anonymous evaluation was used to collect students' feedback on the system. Over 90% of the students indicated that the personal hierarchies and coalesced hierarchy features on the class website were indeed helpful to their learning. H1 was supported.

The quality of documents was measured using the system's voting feature. When a document contributed by another user was displayed, a student could voluntarily and anonymously vote on that document as being either “useful” or “not useful”. Because the voting was voluntary, the mechanism provides a sampled opinion rather than a complete, comprehensive evaluation. We call a document high quality if more voters considered the document useful than not. We also collected click-stream data on the web server to analyze the usage of different navigation mechanisms. We limited the data set to the last month of the semester when students focused on the research paper task. The usage frequency is determined by the number of documents actually accessed through a certain mechanism as re<sup>fl</sup>ected by clickthrough's. For example, expanding and collapsing a category in a hierarchy does not count toward usage. However, retrieving a document through the hierarchy does.

H2 and H3 were both supported. During the semester students categorized 63% of the documents in the repository. Overall, 32% of the documents in the repository were voted high quality. Of categorized documents, however, 49% were voted high quality. Personal hierarchies covered a majority of the repository and included high-quality documents. Over 96% of high-quality documents in the repository were included in personal hierarchies. H4 was supported by clickthrough data (Table 5) using paired two-tailed t-tests (pb0.01). The coalesced hierarchy was used more often than the time hierarchy.

Local and coalesced hierarchies led students to documents that were more likely to be of high quality, compared to all other retrieval mechanisms. Through personal hierarchies, the likelihood of retrieving a high-quality document was 52.35%. Through the coalesced hierarchy, the likelihood of retrieving a high-quality document was 52.26%. As shown in Table 5, the likelihood of retrieving a high-quality document through other mechanisms was around 30%. The data showed no signi<sup>fi</sup>cant difference between the percentages of high-quality documents retrieved from coalesced and local hierarchies. These results suggest that the coalesced hierarchy confers more information cues and effectively lead users to high-quality documents. H5 was supported.

By plotting students' term papers and <sup>fi</sup>nal grades against the numbers of documents within their personal hierarchies, it is clear that their grades and the sizes of their personal hierarchies were positively correlated. H6 was supported. It seems that students indeed gained knowledge from building the personal hierarchies. An alternative explanation is that more serious or diligent students would categorize more documents into their personal hierarchies and would also get higher grades as they put more effort into the class.

While student performance had many factors, we did <sup>fi</sup>nd the following. Students focused on writing the term paper during the last month of the semester. However, we were surprised to <sup>fi</sup>nd that, even then, students spent a lot of effort building their personal hierarchies. Their personal hierarchies grew 30% in terms of number of documents and 40% in terms of number of categories. Local hierarchies, therefore, must have provided students a value that exceeded the effort to build them. Through interviews and inspecting local hierarchies, we found that students used local hierarchies not only to store useful documents for more ef<sup>fi</sup>cient retrieval, but also to organize their thoughts for their term papers. Some categories contained documents supporting particular arguments or sections in their term papers. These observations con<sup>fi</sup>rm that local hierarchies are useful for knowledge acquisition and creation, which further justi<sup>fi</sup>es the need to integrate individuals' dynamic, up-to-date structural knowledge.

A student's term paper quality and overall class performance were both positively related to the usage frequency of the coalesced hierarchy. However, the correlation was weak and the data plots showed outliers. Two students got a C in the class but were among the most frequent users of the coalesced hierarchy. Upon further examination, we found that these two students also had the smallest number of documents in their personal hierarchies. They appeared to be information “free-riders” who used the coalesced hierarchy to obtain references during their paper writing effort. From another perspective, they were “novices” and therefore were more likely to gain structural knowledge from the coalesced hierarchy. However, the best students who got an A from the class also extensively used the coalesced hierarchy. One A student used the coalesced hierarchy even more often than her own personal hierarchy. Through follow-up interviews, we found that most students used the coalesced hierarchy for two main purposes. One was to explore all documents on a certain topic and periodically check to see if any new documents had been added on a certain topic. The other main use of the coalesced hierarchy was to discover new, emerging topics in the website. As students expanded their personal hierarchies with new categories, the coalesced hierarchy also grew with new topics emerging from them. In a way, the coalesced hierarchy worked implicitly as a recommender system based on all contributing users' perspectives. In summary, the coalesced hierarchy provided students a complete, emergent view of the document repository.

Through anonymous evaluation forms and during user interviews, students provided various suggestions to improve the system. One common suggestion was to allow students to share their personal hierarchies with each other in a peer-to-peer fashion. The other major suggestion was to improve the labeling of categories in the coalesced hierarchy. We will explore these directions in future research.

## 5.4. Summary

Evaluation of our prototype system con<sup>fi</sup>rmed the value of both local hierarchies and the system-generated coalesced hierarchy. The coalesced hierarchy is effective in leading users to high-quality documents and providing a full, emergent view of the shared document repository. However, our hierarchy coalescing technique is highly exploratory in nature and dif<sup>fi</sup>cult to evaluate by a prototype system alone. In the next section we focus on a comparative evaluation of our hierarchy coalescing algorithm against other alternatives.

![](/api/attachments/PHX6KRAH/fulltext/images/ef79d8bb0d4f75617346f0ff592f89ee66006cfdadb9c30bb2dfecd4db0b3d87.jpg)  
Fig. 4. A screenshot of the class website.

## 6. Evaluation of the hierarchy coalescing algorithm

Based on Jobson's [17] methodology of evaluating exploratory analyses, we evaluated our hierarchy coalescing algorithm from the perspectives of internal <sup>fi</sup>tness test, external validation, and robustness check. For the internal fitness test, we evaluated the <sup>fi</sup>tness of our coalesced structure to the underlying original data using an objective <sup>fi</sup>tness measure, the Cophenetic correlation coef<sup>fi</sup>cient [10]. For external validation, we asked knowledge workers to evaluate whether a coalesced hierarchy is feasible, and if so, whether it is useful. We also asked knowledge workers to evaluate the coalesced hierarchy generated by our technique against those generated by alternative techniques. For the robustness check, we evaluated the impact of truncated data and noise. We also examined the scalability issue.

## 6.1. Internal fitness test using Cophenetic correlation coefficient

When we described our technique in Section 3, we explored several alternatives and argued theoretically for our design choice. To show that our technique is superior to these alternatives in practice, we compared our technique against them using an objective measure. The Cophenetic correlation coef<sup>fi</sup>cient measures how well clusters represent the actual distances between objects. This measure can be used to compare cluster solutions obtained using different algorithms [10]. The Cophenetic coef<sup>fi</sup>cient is de<sup>fi</sup>ned as the correlation between the pair-wise dissimilarity between documents (computed independently of their positions in a hierarchy) and their Cophenetic dissimilarity within the hierarchy. Cophenetic dissimilarity is the between-cluster dissimilarity at which these two documents are <sup>fi</sup>rst joined together in the same group during the merging process. In other words, the Cophenetic coef<sup>fi</sup>cient measures how well document–document similarities are preserved by the hierarchy. The correlation coef<sup>fi</sup>cient ranges between 0 and 1, with 1 being a perfect correlation. Large values of Cophenetic coef<sup>fi</sup>cient indicate a high-quality clustering solution.

We applied different clustering techniques to the 45 local hierarchies obtained by users of the prototype system. Each clustering technique involved a bsimilarity measure, clustering methodN pair. Table 6 shows the Cophenetic coef<sup>fi</sup>cients of the resulting hierarchies, based on the respective similarity measure used in different clustering techniques. Consistent with our theoretical analysis, the Jaccard– Average technique performed better than all others. Average Linkage appears to be a good choice of clustering method, as Jaccard–Average performed better than Jaccard–Ward's. A Cophenetic coef<sup>fi</sup>cient above 0.8 can reject the null hypothesis of a single cluster versus the alternative hypothesis of a system of nested clusters [17]. As further con<sup>fi</sup>rmation of the bene<sup>fi</sup>ts of the Jaccard–Average approach we adopted, its Cophenetic coef<sup>fi</sup>cient of 0.9 indicates that the coalesced hierarchy it generated provides a good <sup>fi</sup>t for underlying documents based on their membership in local hierarchies. Finally, Jaccard–Average performed better than Cosine–Centroid, a more traditional document clustering method that uses document content as its input rather than structural information. This suggests that the structural information embedded in local hierarchies is appropriate as input for document clustering.

## 6.2. External validation by knowledge workers

Only knowledge workers could ultimately judge the value of a coalesced hierarchy. We conducted the following two experiments with MBA student subjects. All the subjects had taken the database management course in previous semesters under different instructors.

The goal of Experiment A was two-fold. First, we wanted to con<sup>fi</sup>rm that both the structure and the category labels in our coalesced hierarchy were usable by knowledge workers. Second, we wanted to better understand whether knowledge workers were likely to agree to a common hierarchy regardless of the techniques involved. In this experiment, we drew 10 random documents from the document repository in the prototype system. We then presented these documents to 16 students and provided them with the top two levels of the coalesced hierarchy in the prototype system (a total of 13 categories overall). Students were asked to place documents into these categories.

The results of Experiment A showed that 76% of the time, students placed the document in the hierarchy “correctly” (i.e. the same way as the coalesced hierarchy did). This result suggests that the knowledge workers could meaningfully utilize the categories of the coalesced hierarchy. Notably there was one document that none of the 16 students was able to place “correctly”, which indicated a potential mis-categorization problem by the coalesced hierarchy. The agreement among students about proper placement of a document in a category, however, was much higher. We de<sup>fi</sup>ne the convergence of a document as the percentage of documents in the most common category used for that document. For example, if 10 students place a document into category 1, and the other 6 students place the document into other categories, then the convergence for that document is $1 0 / 1 6 = 6 2 . 5 \%$ . The average convergence for all documents is 93%. For the one document that was not “correctly” categorized by any students, the categorization results almost perfectly converge (94% convergence). Upon closer examination, we found that this document was indeed “mis-categorized” by the coalesced hierarchy. In fact, this document only existed in one person's personal hierarchy in the system and that person clearly mis-categorized the document. The convergence results show good potential for knowledge workers to reach agreement in understanding and interpreting the coalesced hierarchy. The convergence results also suggested that the category labels in our coalesced hierarchy were suf<sup>fi</sup>ciently representative and discriminating for the students' categorization task.

Table 5  
Retrieval of high-quality documents by different navigation mechanisms

<table><tr><td></td><td>Personal hierarchies</td><td>Coalesced hierarchy</td><td>Time hierarchy</td><td>Search</td><td>Hyperlink</td></tr><tr><td># of total document accesses</td><td>1595</td><td>155</td><td>26</td><td>126</td><td>3652</td></tr><tr><td># of accesses to high-quality documents</td><td>835</td><td>81</td><td>7</td><td>40</td><td>1228</td></tr><tr><td>% retrieving a high-quality document</td><td>52.35%</td><td>52.26%</td><td>26.92%</td><td>31.75%</td><td>33.63%</td></tr></table>

The goal of Experiment B was to compare the quality of hierarchies generated by different techniques. In this experiment, 10 students in one class were given one week to read the same 28 textual documents related to the class and instructed to create personal hierarchies with which to categorize them. After the personal hierarchies were collected, they were merged using different techniques. Each student was then presented with four hierarchies, each containing all 28 documents. The students did not know that three hierarchies were automatically generated and that the fourth hierarchy was a randomly chosen personal hierarchy of another student. Measures were taken so that a student would not receive their own hierarchy. The three automatically generated hierarchies were created using different clustering methods: Jaccard–Average (our technique), Jaccard–Ward's, and Cosine–Centroid (the latter method using document text as input, the <sup>fi</sup>rst two using students' personal hierarchies). The students were asked to evaluate the quality of these hierarchies on a 1–5 scale. Further, students were asked to improve the category labels in each hierarchy and then re-evaluate them.

Table 7 shows the results of Experiment B. Using a paired two-tailed t-test, Jaccard–Average scored higher than the other methods (pb0.05) with larger differences among methods after category re-labeling. The results con<sup>fi</sup>rmed that the hierarchy generated from our algorithm produced a good compromise of personal hierarchies. The score for Jaccard–Average increased from 3.6 to 4.3 after re-labeling, which suggests potential improvement for category labeling.

## 6.3. Robustness and scalability check

To test the robustness of our technique, we applied random sampling and perturbation to the data collected from the prototype system. We drew samples in two ways. One was to randomly pick 50% of documents and thus get a document-category matrix with a reduced number of rows. The other was to randomly pick 50% of the local hierarchies and thus reduce the document-category matrix by columns. Using both methods, top-level categories of resulting hierarchies largely matched those from the full input data. As a perturbation test, we randomly interchanged 1% of the non-zero entries with zero entries in the document-category matrix, to simulate user errors in categorization. The top-2 levels of categories in resulting hierarchies remained the same. However, when we increased the perturbation percentage to 5%, we started to notice changes in the top-2 levels of coalesced hierarchy. These results suggested that our technique is robust to careless errors but sensitive enough to capture evolving categories.

For the scalability check, we simulated over 100,000 documents by creating 100 perturbed copies for each actual document in the document-category matrix from the prototype system using a 20% perturbation percentage. It took the hierarchy coalescing algorithm about 50 min to complete (averaged over 3 runs) on a Linux PC with two Intel 2 GHz Pentium 4 CPUs and 2 GB of memory. It suggests that for a large shared repository with hundreds of thousands of documents, the coalesced hierarchy can be generated daily at a low cost.

## 6.4. Summary and limitation

We have evaluated the hierarchy coalescing technique both analytically and empirically. Using data from the prototype system and questionnaire-based experiments, the results con<sup>fi</sup>rmed that our hierarchy coalescing algorithm can produce a useful coalesced hierarchy and our design choice outperforms alternatives. Evaluation also suggests potential for improvement in category labeling.

The prototype system and evaluation are rather limited in scale. To update the system-generated hierarchy frequently, the coalescing algorithm can bene<sup>fi</sup>t from scalability enhancements. The most timeconsuming step in the algorithm is the agglomerative hierarchical clustering step with O(N<sup>2</sup>) algorithmic complexity. In recent years there has been <sup>fl</sup>ourishing research on improving the scalability of hierarchical clustering. For example, Scatter/Gather [6] achieves O(N) through fractionalization. The original data set is split into subsets called fractions, whose centroids are calculated and clustered. Each document is then assigned to the cluster with the closest centroid. BIRCH [42], Balanced Iterative Reducing and Clustering using Hierarchies, achieves O(N) using a special data structure called Cluster Feature tree for storing summary information about clusters and reducing the data set. CURE [11], Clustering Using Representatives, reduces large data sets through a combination of random sampling and partitioning. With parallel computing, the time of hierarchical clustering can be potentially reduced to O(logN) [30]. Our technique can bene<sup>fi</sup>t from these methods and other scalability enhancements being developed for hierarchical clustering. Note that although the pair-wise similarity computation is also of ${ \mathrm { O } } ( { \mathrm { N } } ^ { 2 } )$ complexity, the computation and storage can be largely reduced as document-category vectors are sparse. For each document, the system stores and computes similarities for only the documents that co-exist with the given document in at least one category and defaults as 0 for similarity to all other documents. Furthermore, pair-wise similarities can be incrementally updated by a real-time process when a document is categorized or schema changes occur.

The coalescing algorithm is based on the premise that local hierarchies embed rich structural knowledge and that noises will be dominated by correct categorizations. Few con<sup>fl</sup>icting or orthogonal local hierarchies may lead to noisy results. The algorithm is suited for people or groups with similar backgrounds and interests who will likely have overlapping, non-orthogonal local hierarchies. If multiple people/groups have totally different purposes and thus view the documents in completely different ways the majority view or the larger local hierarchies will win. Our evaluation using MBA students was limited in that the students were not subject experts and their views may have been similarly shaped by classroom teaching. Real knowledge communities should also have overlapping local hierarchies but the amount of overlap would be different depending on the particular community. While limited, the evaluation shows promise for real-world situations such as knowledge workers in the same global enterprise or counter-terror intelligence analysts from different agencies.

Table 6  
Cophenetic coef<sup>fi</sup>cients of resulting hierarchies from different techniques.

<table><tr><td></td><td>Data input</td><td>Similarity</td><td>Clustering method</td><td>Cophenetic coefficient</td></tr><tr><td>Jaccard-Average</td><td>Document-Category matrix</td><td>Jaccard</td><td>Average</td><td>0.9110</td></tr><tr><td>Jaccard-Ward&#x27;s</td><td>Document-Category matrix</td><td>Jaccard</td><td>Ward&#x27;s</td><td>0.8505</td></tr><tr><td>Euclidean-Average</td><td>Document-Category matrix</td><td>Euclidean</td><td>Average</td><td>0.4949</td></tr><tr><td>Cosine-Centroid</td><td>Document-Keyword  $matrix^a$ </td><td>Cosine</td><td>Centroid</td><td>0.7517</td></tr></table>

<sup>a</sup> For non-textual documents, only titles of these documents are used as input.

## 7. Conclusion and future work

We have proposed a collective taxonomizing approach to organize a shared, growing document repository by allowing individually managed local document hierarchies and algorithmically building a global hierarchy that combines them. We have highlighted structural knowledge embedded in the document hierarchies as an important type of knowledge being managed in a document repository. Using Nonaka's framework [23], we have illustrated that combining local structural knowledge into a global hierarchy bene<sup>fi</sup>ts organizational knowledge creation. We have designed an algorithm that builds a global, coalesced hierarchy from overlapping local document hierarchies. The algorithm was designed through careful search and evaluation processes using a design science approach [22].

Empirical evaluation shows promise. The coalesced hierarchy provided users a full, emergent view of the document repository. The coalesced hierarchy led users to high-quality documents by working implicitly as a recommender system based on the structural knowledge of all contributing users. The algorithm outperformed other design alternatives.

Structural knowledge tends to get stale quickly [2]. To build structural knowledge in a document repository, the speed of structural knowledge creation needs to exceed the attrition rate. Each knowledge conversion mode in the spiral of structural knowledge creation [23] has to be made ef<sup>fi</sup>cient so that the spiral expands rather than contracts. Our collective taxonomizing approach attempts to improve the ef<sup>fi</sup>ciency of the combination of structural knowledge and is particularly useful for large, growing multimedia document collections shared by multiple organizations or a large user community.

Our hierarchy coalescing algorithm can be readily implemented in a document repository where local document hierarchies are available. Local hierarchies can be captured in various ways. For example, a snapshot of a <sup>fi</sup>le system can be taken if the local hierarchies are <sup>fi</sup>le-directory based or an online document repository can collect users' personal bookmark hierarchies. Because local hierarchies can be captured without the actual content of documents certain privacy issues can be avoided. Some repositories store documents with attributes (metadata) from various classi<sup>fi</sup>cation schemes. The categorical attributes can be translated into document categories which in turn can be utilized by our algorithm to generate the coalesced hierarchy. Recent research has proposed social hierarchies [32], which allow users to share personal document or bookmark hierarchies with others, as opposed to social tagging. Our collective taxonomizing approach can be directly applied to such social hierarchies. There have also been attempts to build clusters or hierarchies of tags on top of existing social tagging systems [16,26]. In general, these techniques attempt to identify parent–child relationships among tags. The items in their resulting hierarchies are tags instead of documents. Therefore, these hierarchies inherit the problems with tags such as noise, spam, synonymy, homonymy and polysemy. It would be interesting to see how our collective taxonomizing approach may complement or build upon collaborative tagging systems. For example, the hierarchy coalescing algorithm may be integrated with tag clustering algorithms to generate document hierarchies using both local hierarchies and free-form tags.

Table 7 User evaluation of the hierarchies generated by different methods.  
![](/api/attachments/PHX6KRAH/fulltext/images/2773b2c991500279d0b2b5377cdc537d854be7a1475b9498045e833852fbe058.jpg)

Our research is related to ontology mapping, hierarchy integration, database integration, data fusion, and other data integration efforts. Ontology mapping (surveyed in [5]) and merging have gained much attention in recent years [9,41]. Our research focuses on the ontologymerging problem in a shared document repository. As a statistical association-mining technique, our algorithm can be applied to those <sup>fi</sup>elds when a large number of overlapping hierarchies are to be merged. Our technique is not suitable for merging few con<sup>fl</sup>icting or orthogonal hierarchies. Our research is related to hierarchy integration approaches, which typically use one existing hierarchy as the master hierarchy [4]. Integration of databases from different sources often involves schema integration and entity integration [43]. Our research is also related to data fusion (for a survey please see [3]) — the process of integrating multiple records representing the same real-world object into a single representation.

Our research is different from text categorization research, which classi<sup>fi</sup>es documents into pre-de<sup>fi</sup>ned categories [40]. However, it is possible to combine our technique with text categorization. Our technique can create an initial coalesced hierarchy, which is then used to categorize incoming documents. This combined approach is highly scalable, as incoming documents are categorized on an incremental basis. We can also combine our automated technique with manual intervention by allowing human indexers to manually prune or label the automatically coalesced hierarchy. Our evaluation found that better category labels can signi<sup>fi</sup>cantly improve the usefulness of the coalesced hierarchy.

We believe managing structural knowledge is a key challenge for knowledge sharing and decision making. We are studying how peer sharing of document hierarchies may complement the coalesced hierarchy in sharing structural knowledge. We plan to improve category labeling and explore scalability enhancements for the algorithm. We are developing hybrid algorithms that utilize both structural knowledge and the content of documents. We also plan to extend our evaluation to industry knowledge environments.

## Acknowledgement

This work is partly supported by the National Science Foundation under Grant No. 0713290.

## References

[1] J.R. Anderson, Cognitive Psychology and Its Implications, W.H. Freeman and Company, New York, 1995.

[2] H. Barki, S. Rivard, J. Talbot, A keyword class<sup>fi</sup>cation scheme for IS Research Literature: an update, MIS Quarterly 17 (1993) 209–226

[3] J. Bleiholder, F. Naumann, Data fusion, ACM Computing Survey 41 (2008) 1–41.

[4] T.-H. Cheng, C.-P. Wei, A clustering-based approach for integrating documentcategory hierarchies, IEEE Transactions on Systems, Man and Cybernetics-Part A 38 (2008) 410–424.

[5] N. Choi, I. Song, H. Han, A survey on ontology mapping, ACM SIGMOD Record 35 (2006) 34–41.

[6] D.R. Cutting, D.R. Karger, J. Pedersen, Constant interaction-time scatter/gather browsing of very large document collections, 16th annual international ACM SIGIR conference, Pittsburgh, 1993.

[7] L.E. Davis, G.Y. Treverton, D. Byman, S. DALY, W. Rosenau, Coordinating the War on Terrorism, The Rand Corporation Report OP-110-RC, , 2004.

[8] G.M. Diekhoff, K.B. Diekhoff, Cognitive maps as a tool in communicating structural knowledge, Educational Technology 22 (1982) 28–30

[9] A. Doan, J. Madhaven, R. Dhamankar, P. Domingos, A. Helevy, Learning to match ontologies on the semantic web, The VLDB Journal 12 (2003) 303–319.

[10] B.S. Everitt, G. Dunn, Applied Multivariate Data Analysis, Oxford University Press, New York, 1992.

[11] S.R. Guha, R. Rastogi, K. Shim, CURE: An ef<sup>fi</sup>cient clustering algorithm for large databases, ACM SIGMOD International Conference on Management of Data, 1998, pp. 73–84.

[12] J.A. Hartigan, Statistical theory in clustering, Journal of Classi<sup>fi</sup>cation 2 (1985) 63–76.

[13] M. Hearst, C. Karadi, Searching and browsing text collections with large category hierarchies, Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI), Atlanta, GA, 1997.

[14] M.A. Hearst, J.O. Pedersen, Reexamining the cluster hypothesis: scatter/gather on retrieval results 19th annual international ACM SIGIR conference, Zurich 1996

[15] A.R. Hevner, S.T. March, J. Park, Design science in information systems research, MIS Quarterly 28 (2004) 75–105.

[16] P. Heymann, H. Garcia-Molina, Collaborative Creation of Communal Hierarchical Taxonomies in Social Tagging Systems. Technical Report InfoLab 2006-10. Stanford University. Stanford. 2006.

[17] J.D. Jobson, Applied Multivariate Data Analysis, Springer-Verlag, New York, 1992

[18] A. Kankanhalli, B. Tan, K. Wei, Conributing knowledge to electronic document repositories: an empirical investigation, MIS Quarterly 29 (2005) 113–144.

[19] J.H. Larkin, J. McDermottt, D.P. Simon, H.A. Simon, Expert and novice performance in solving physics problems, Science (1980) 1335–1342.

[20] A. Leuski, Evaluating document clustering for interactive information retrieval, 10th international conference on Information and knowledge management Atlanta, 2001, pp. 33–40.

[21] D. Lin, An information-theoretic de<sup>fi</sup>nition of similarity, International Conference on Machine Learning, Madison, 1998.

[22] S.T. March, G. Smith, Design and natural science research on information technology, Decision Support Systems 15 (1995) 251–266.

[23] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1994) 14–37.

[24] D. Radev, W. Fan, Z. Zhang, WebInEssence: personalized web-based multidocument summarization, NAACL Workshop on Automatic Summarization, Pittsburg, 2001.

[25] D.E. Rumelhart, Schemata: The building blocks of cognition, Lawrence Erlbaum Hillsdale, NJ, 1980.

[26] P. Schmitz, Inducing Ontology from Flickr Tags, Workshop in Collaborative Web Tagging, 2006.

[27] M. Steinbach, G. Karypis, V. Kumar, A comparison of document clustering techniques, KDD Workshop on Text Mining, 2000.

[28] E.M. Voorhees, Implementing agglomerative hierarchical clustering algorithms for use in document retrieval, Information Processing and Management 22 (1986) 465–476.

[29] P. Willett, Recent trends in hierarchical document clustering: a critical review, Information Processing and Management 24 (1988) 577–597.

[30] C.-H. Wu, S.-J. Horng, H.-R. Tsai, Ef<sup>fi</sup>cient parallel algorithms for hierarchical clustering on arrays with recon<sup>fi</sup>gurable optical buses, Journal of Parallel and Distributed Computing 60 (2000) 1137–1153.

[31] H. Wu, M. Gordon, Collaborative <sup>fi</sup>ling in a document repository, Proceedings of the ACM SIGIR 2004, Shef<sup>fi</sup>eld, UK, 2004, pp. 518–519.

[32] H. Wu, M. Gordon, From social tagging to social hierarchies — sharing deeper structural knowledge in Web 2.0, Communications of the Association for Information Systems, 24, 2009.

[33] H. Wu, M. Gordon, Collaborative structuring: organizing document repositories effectively and ef<sup>fi</sup>ciently, Communications of the ACM 50 (July 2007) 86–91.

[34] H. Wu, M. Gordon, K. DeMaagd, Document co-organization in an online knowledge community, ACM Conference on Human Factors in Computing Systems, Vienna, Austria, 2004, pp. 1211–1214.

[35] H. Wu, M. Gordon, K. DeMaagd, N. Bos, Link analysis for collaborative knowledge building, Proceedings of the ACM 14th Conference on Hypertext and Hypermedia, Nottingham, UK, 2003, pp. 216–217.

[36] H. Wu, M. Gordon, K. DeMaagd, W. Fan, Mining web navigations for intelligence, Decision Support Systems 41 (2006) 574–591.

[37] H. Wu, M.D. Gordon, From Social Tagging to Social Hierarchies: Sharing Deeper Structural Knowledge in Web 2.0, Communications of the Association for Information Systems, 24, 2009.

[38] H. Wu, D.R. Radev, W. Fan, Towards answer-focused summarization, Proceedings of the International Conference on Information Technology and Applications, Bathurst, Australia, 2002.

[39] H. Wu, M. Zubair, K. Maly, Collaborative classi<sup>fi</sup>cation of growing collections with evolving facets, Proceedings of the ACM 17th Conference on Hypertext and Hypermedia (Hyptertext'07) Manchester, UK, 2007.

[40] Y. Yang, An evaluation of statistical approaches to text categorization, Information Retrieval 1 (1999) 69–90.

[41] D. Zhang, W. Lee, Web taxonomy integration using support vector machines, 13th international conference on World Wide Web New York, 2004

[42] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: An ef<sup>fi</sup>cient data clustering method for very large databases, ACM SIGMOD Conference, 1996.

[43] H. Zhao, S. Ram, Combining schema and instance information for integrating heterogeneous data sources, Data and Knowledge Engineering 61 (2007) 281–303.

Harris Wu is an assistant professor at the College of Business and Public Administration, Old Dominion University. His research mainly focuses on how to harvest social knowledge and facilitate inter-organizational collaboration for information retrieval, software engineering and technology innovation.

Michael Gordon is a professor of business information technology at the University of Michigan. His research interests include information retrieval, especially adaptive methods and methods that support knowledge sharing among groups; information and communication technology in the service of social enterprise (promoting economic development, providing health care delivery, and improving educational opportunities for the poor); and using information technology along with social methods to support business education.

Weiguo Fan is an associate professor of information systems and computer science at the Virginia Polytechnic Institute and State University. His research interests include personalization, data mining, text/web mining, web computing, business intelligence, digital library, and knowledge sharing and individual learning in online communities.
