---
otero_id: 2904
otero_key: "GCS35EBK"
title: "On technology for functional requirement-based reference design retrieval in engineering knowledge management"
authors: "Yuh-Jen Chen; Yuh-Min Chen; Hui-Chuan Chu; Hao-Yun Kao"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On technology for functional requirement-based reference design retrieval in engineering knowledge management

Yuh-Jen Chen <sup>a</sup>, Yuh-Min Chen <sup>b,⁎</sup>, Hui-Chuan Chu <sup>c</sup>, Hao-Yun Kao <sup>d</sup>

<sup>a</sup> Department of Accounting and Information Systems, National Kaohsiung First University of Science and Technology, Kaohsiung, Taiwan, ROC <sup>b</sup> Institute of Manufacturing Engineering, National Cheng Kung University, Tainan, Taiwan, ROC

<sup>c</sup> Department of Special Education, National University of Tainan, Tainan, Taiwan, ROC

<sup>d</sup> Department of Information Management, National Sun Yat-Sen University, Kaohsiung, Taiwan, ROC

Received 25 September 2005; received in revised form 5 July 2007; accepted 6 October 2007 Available online 17 October 2007

## Abstract

Engineering design is a knowledge-intensive process, and includes conceptual design, detailed design, engineering analysis, assembly design, process design, and performance evaluation. Each of these tasks involves various aspects of technical knowledge and experience. Whether this technical knowledge and experience can be effectively shared is key to increasing product development capability and quality, and also to reducing the duration and cost of the development cycle. Consequently, providing engineering designers various query methods for retrieving engineering knowledge is one of the most important tasks in engineering knowledge management.

The study develops a technology for functional requirement-based reference design retrieval as a decision support mechanism, which can assist engineering designers to retrieve relevant design and associated knowledge for reference in conducting functional requirements of a product. This study involves the following tasks: (i) designing a functional requirement-based reference design retrieval process, (ii) developing techniques related to the technology for functional requirement-based reference design retrieval, and (iii) implementing a functional requirement-based reference design retrieval mechanism. The retrieval process includes the steps of functional requirement-based query, case searching and matching, and case ranking. The technology involves (i) a structured query model for functional requirements, (ii) an index structures for historical design cases, (iii) functional requirementbased case searching and matching mechanisms, (iv) a functional requirement-based case ranking mechanism, and (v) a case-based representation of designed entities. Finally, the experimental example with indexing and retrieving similar designed entities is conducted to demonstrate the proposed techniques worked efficiently. © 2007 Elsevier B.V. All rights reserved.

Keywords: Knowledge retrieval; Knowledge management; Engineering design

## 1. Introduction

The advent of the knowledge economy has made knowledge the most important asset of enterprises in the 21st century. The storage and effective employment of enterprise knowledge is essential to success. Consequently, effectively sharing and applying knowledge to increase business intelligence (BI) is crucial to enterprises in the present knowledge economy.

Engineering design [9,11–13,19,20,28,31] is the process of establishing requirements based on customer needs, and transforming them into performance specifications and functions, which are then mapped and converted into design solutions that can be economically produced using creativity, scientific principles, technical knowledge and experience. Whether this tacit knowledge and experience can be effectively shared and applied is key to increasing the capability and quality of product development, and to reducing time and cost of the development cycle. Consequently, organizing, storing, and retrieving information on product designs, the intent of a design and underlining design knowledge represent the basis of, and are the most important tasks in engineering knowledge management.

However, most traditional knowledge management systems and engineering data management systems only offer explicit knowledge searching functions, such as document searching, engineering data searching, team information searching, and workflow management [1–3,7,14,16–18,21,22,24,29–32]. There are still no methods for tacit engineering knowledge retrieval, this circumstance causes a bottleneck for sharing valuable engineering knowledge and experience in engineering design, so engineering knowledge management remains far from being realized.

The study develops a technology for functional requirement-based reference design retrieval, which can assist engineering designers to retrieve relevant design and associated knowledge for reference in conducting functional requirements of a product. The objective of this study can be obtained by performing the following tasks: (i) designing a functional requirement-based reference design retrieval process, (ii) developing techniques for functional requirement-based reference design retrieval, and (iii) implementing a functional requirement-based reference design retrieval mechanism. The techniques involved in functional requirementbased reference design retrieval include a structured query model for functional requirements, an index structures for historical design cases, functional requirement-based case searching and matching mechanisms, a functional requirement-based case ranking mechanism, and a case-based representation of designed entities. Finally, the experimental example with indexing and retrieving similar designed entities is performed to demonstrate the proposed techniques worked efficiently.

## 2. Overview of an engineering knowledge management framework

This section presents an overview of a proposed engineering knowledge management framework for supporting tacit knowledge-intensive activities in engineering design [4]. Fig. 1 presents the framework as a knowledge management life cycle, which consists of creation, capture, the compilation and storage, and the retrieval/reuse/query of tacit engineering knowledge. The elements in the knowledge management life cycle are explained below.

## 2.1. Engineering knowledge definition and creation

Engineering knowledge herein is defined as tacit technical knowledge of engineers, to support the phase of product design. These tacit technical knowledge items are identified as follows.

In engineering design, engineering designers usually apply various structured design methods to perform their tasks and achieve their design objectives. Examining engineering designer behavior reveals that four structured design methods are frequently employed in engineering design; these are feature-based design, engineering change, design by modification, and design by reference.

In feature-based design, product modeling uses a library of 2D or 3D features as design primitives. Product functional requirements are transformed into functional features, which are then converted into design specifications and manufacturing features. Engineering knowledge involved in feature-based design includes design intent, engineering principles, design experience, creativity, and product information. Product information can be subdivided into the areas of customer needs, functional requirements, functional features, and engineering specifications.

Engineering change is usually defined as a change to the form, fit or function of a product or part to satisfy customers' requirements. Engineering change is triggered by an engineering change request, after which the change is proposed, investigated, authorized/rejected, executed, reviewed, and archived in an orderly, structured design manner. Knowledge of engineering change can be specialized as change knowledge, which can be categorized into a reason for change and the content of the change, as well as the applied engineering principles.

Design by modification/design by reference is employed to reduce the design time and increase the working efficiency of engineering designers. In this method, a most similar engineering model is retrieved from the historical knowledge repository according to the product information, which then is slightly modified to create a new engineering model, or serves as a reference model for a new design. Tacit engineering knowledge is involved in both design by modification and design by reference, and includes product information, design intent, engineering principles, and design experience.

![](/api/attachments/GCS35EBK/fulltext/images/fe8522401c63c980fcc47e3454ae3e5428b876ab42ea16b12d53704f555e4949.jpg)  
Fig. 1. Engineering knowledge management framework.

## 2.2. Engineering knowledge extraction, capture, compilation and storage

Design intent, applied engineering principles and heuristics, and engineering collaboration contents can be extracted during engineering design, and associated with the design object as notes for reference [4]. When an engineering model is completed and checked into a project knowledge repository, the product information and knowledge related to the engineering model are captured and stored in product information and engineering knowledge libraries, respectively. Furthermore, the product information and engineering knowledge are compiled in rule format and deposited in an engineering rule base. Once a design project is completed, the engineering models and related knowledge are archived in a historical knowledge repository for reuse later.

## 2.3. Engineering knowledge retrieval/reuse/query

Relevant product information and engineering knowledge can be retrieved when an engineering model is checked out or copied from the project knowledge repository. Similarly, historical engineering models, related product information and engineering knowledge also can be referenced or copied to provide a reference for new projects. Moreover, engineering designers can conveniently query engineering knowledge through the knowledge query function effectively to solve related design problems.

Engineering design is a knowledge and creativityintensive process. The execution of each task in a process depends on multi-faceted design knowledge and experience. Therefore, knowledge retrieval is required to enable the sharing of engineering knowledge to support engineering knowledge management in engineering design, and to reduce the duration and cost of the product development cycle.

Engineering design is the systematic process of identifying customer requirements; translating them into the functional requirements of a product, and then mapping these functional requirements into functional features and engineering specifications that can be economically met during manufacture, by exploiting creativity, scientific principles and technical knowledge. Therefore, a multi-layer reference design retrieval, which involves customer requirement-based reference design retrieval, functional requirement-based reference design retrieval, and functional feature-based reference design retrieval should be developed to support various levels of knowledge retrieval in engineering design.

This study primarily focuses on the functional requirement-based knowledge retrieval, which is displayed as the shaded portion and surrounded by the broken line, as illustrated in Fig. 1.

## 3. Functional requirement-based reference design retrieval

This section describes the process of functional requirement-based reference design retrieval. The retrieval process comprises three main portions, namely (i) the establishment of the functional requirement-based query model, (ii) the definition and establishment of index structures for historical design cases, and (iii) searching, matching and ranking similar design cases. Each portion involves several crucial techniques. The establishment of a functional requirement-based query model involves the definition and a structured representation of the functional requirement. The definition and establishment of index structures for historical design cases involves the casebased representation of designed entities and the establishment of index structures of historical design cases. Finally, techniques related to searching, matching and ranking similar historical cases involve functional requirementbased case searching, matching and similarity ranking.

## 3.1. Functional requirement-based reference design retrieval process

The process of functional requirement-based reference design retrieval aims to find design cases as references from the historical knowledge repository that most closely match the functional requirements in the query of the engineering designer. As shown in Fig. 2, functional requirement-based reference design retrieval has three main parts. Each part is detailed as follows.

## 3.1.1. Establishment of functional requirement-based query model

The functional requirement-based query model is established to define functional requirement, and build a structured query model for functional requirements through a structured representation, to facilitate the searching and matching similar design cases.

## 3.1.2. Definition and establishment of index structures for historical design cases

In this study, the index structures for historical design cases are established according to the key elements/terms in the description of functional requirements. The project manager can save the completed design cases into the historical knowledge repository through the index structures. These saved design cases are collected into a suitable case set based on the defined index structures. The index structures facilitates searching and matching similar design cases to provide engineering designers a convenient way to find the historical design cases that are most similar to the functional requirement-based query model from the historical knowledge repository.

![](/api/attachments/GCS35EBK/fulltext/images/3f6e819c0d2edd7021df946c0cfeaf6cb64b045d30c112ad37355667e83b313a.jpg)  
Fig. 2. Functional requirement-based reference design retrieval process.

![](/api/attachments/GCS35EBK/fulltext/images/ec82d16efd6cd278eba4b1df325a6c079dac008f9acdc362f653a9f996fc4582.jpg)  
Fig. 3. Basic structure of the semantic graphs.

## 3.1.3. Searching, matching and ranking similar design cases

The searching, matching and ranking similar design cases are performed mainly to retrieve functional requirement-based similar design cases based on the aforementioned functional requirement-based query model and the index structure for historical design cases. Furthermore, the retrieved design cases would be ranked in order of calculated similarities to the most valuable reference design.

## 3.2. Establishment of functional requirement-based query model

## 3.2.1. Definition of functional requirement

This subsection defines the description of functional requirement. A basic description of functional requirement in engineering design can be defined as “Adverb” + “Verb” + “Noun”. Meanwhile, “Verb + Noun” is called the functional entity and “Adverb” is the modifier of the functional entity. For example, “tightly combine pennibs”, “easily change ink-reservoir” and so on. Additionally, the types of functional design and functional decomposition are defined to offer engineering designers further descriptions of functional type. The type of functional design includes basic function, operation function, need function, and patch function, while the type of functional decomposition includes main function, interdependent function, and auxiliary function.

## 3.2.2. Representation of functional requirement

This study applies the semantic graph theory [4,26,27] (Fig. 3) as a foundation for developing a structured representation of functional requirement based on the defined description. Fig. 4 presents an example of a structured representation of functional requirement derived from semantic graph theory. This structured query model has thee representing parts, namely (i) representation of the functional entity, (ii) representation of the modifier of the functional entity, and (iii) representation of the function type. The boxes indicate concepts such as entities, attributes, states and events, while the ellipse shows the interconnection among the concepts.

Based on the semantic graph representation for functional requirement in Fig. 4, the description of functional requirement is defined as follows.

```txt
[Proposition:
    [Open]-
    (Object)-->[Door]
    (Modifier)-->[Conveniently]
    (Decomposition Type)-->[Basic Function]
    (Design Type)-->[Operation Function]
]
```

## 3.3. Definition and establishment of index structures for historical design cases

This section first presents a case-based representation of designed entities to record related product information and engineering knowledge. Subsequently, the index structures for historical design cases are defined and established.

## 3.3.1. Design of representation model for product design case

From Fig. 5, a “Case” is viewed as a box that contains related tags and links the product information and engineering knowledge of a design entity (such as an engineering model) [4]. The scheme of a case consists of three features — case feature, model feature, and semantic feature. Case feature defines the contents of case

![](/api/attachments/GCS35EBK/fulltext/images/aedce884ec137931b630b492dd619d854353f20f8ea3a6503ea31d49ea18faa8.jpg)  
Fig. 4. Structured representation of functional requirement (an example).

![](/api/attachments/GCS35EBK/fulltext/images/731c93212a8bb6130af11f5c5094904d2dbccfe303149a02805c99cd92ee1a9b.jpg)  
Fig. 5. Conceptual case model.

data, including case name, ID, tag ID, name, model creator, contributor, date, language, version, and location. Meanwhile, model feature indicates the tag for product information that records detailed information about a design entity, including customer requirements, functional requirements, and functional features. Finally, semantic feature represents the tags for engineering knowledge that also record the design knowledge and experience of engineering designers. These tags for engineering knowledge are classified into three categories — (i) the tag for feature-based design, (ii) the tag for engineering change, and (iii) the tag for design by modification/reference. Each of these tags points to relevant production information or engineering knowledge.

![](/api/attachments/GCS35EBK/fulltext/images/7910d88933522a332a03376961f914d3319b6919afa2ab3e53c5624988dca1bb.jpg)  
Fig. 6. Prototype index structure of historical design cases.

![](/api/attachments/GCS35EBK/fulltext/images/b2d83553630f9e39cc770c2e23a1502228c9ce4d3ed75672e3961fcbb02ef4e1.jpg)  
Fig. 7. Index structure for nouns (an example).

## 3.3.2. Definition and establishment of index structures for historical design cases

The primary function of the index structures for historical design cases is to support searching and matching similar design cases according to the functional requirement-based query model described by engineering designers. Therefore, five index structures are established based on the characteristics of key elements/terms in the functional requirement as well as the defined prototype of index structure for historical design cases (Fig. 6). These five index structures are: (i) the index structure for nouns, (ii) the index structure for verbs, (iii) the index structure for adverbs, (iv) the index structure for design functions, and (v) the index structure for decomposition functions. The defined prototype of index structure for historical design cases comprises three layers, namely (i) a conceptual layer — an abstract set for describing the classified concept, (ii) a synonym layer — a synonym set for describing a particular abstract concept, and (iii) a case layer — a set of design cases for recording the same elements/terms.

![](/api/attachments/GCS35EBK/fulltext/images/5f0e1aa4c191ef28dc08c836e0435f476b30fdd3937acde5b0ce9a768148ebe4.jpg)  
Fig. 8. Index structure for verbs (an example).

![](/api/attachments/GCS35EBK/fulltext/images/4ef9aa32e4fecc06ab600f60dd592497c6d5b0f0d806887decfe3f8a81b203c4.jpg)  
Fig. 9. Index structure for adverbs (an example).

3.3.2.1. Index structure for nouns. The purpose of the index structure for nouns is to help the system to find similar design cases based on the element “Noun” in the functional requirement-based query model. As shown in Fig. 7, the index structure for nouns has six layers, namely (from top to bottom) (i) domain layer, (ii) product layer, (iii) major module layer, (iv) component layer, (v) synonym layer, and (vi) case layer.

3.3.2.2. Index structure for verbs. The index structure for verbs helps the system to find similar design cases according to the element “Verb” in the functional requirement-based query model. As displayed in Fig. 8, the index structure for verbs has seven layers in the order, (i) domain layer, (ii) behavior layer, (iii) sense layer, (iv) action layer, (v) subaction layer, (vi) synonym layer, and (vii) case layer.

3.3.2.3. Index structure for adverbs. The main purpose of building the index structure for adverbs is to find similar design cases that have the same element “Adverb” in the functional requirement-based query model. As illustrated in Fig. 9, the index structure for adverbs has six layers, namely (i) domain layer, (ii) modifier layer, (iii) sense layer, (iv) subsense layer, (v) synonym layer, and (vi) case layer.

3.3.2.4. Index structure for design functions. As shown in Fig. 10, the index structure for design functions has two layers, namely (i) design-type layer and (ii) case layer. The design-type layer contains the types of basic function, operation function, need function and patch function.

![](/api/attachments/GCS35EBK/fulltext/images/3c7688ab64e8801d0936a4e7b85a8b399658e5c97d5de8beca9a18d1468dd3ac.jpg)  
Fig. 10. Index structure for design functions.

![](/api/attachments/GCS35EBK/fulltext/images/c628e62c01258b73900a20f61c4a3eaf6846b99aebbfc3d40d122a4dfb59a621.jpg)  
Fig. 11. Index structure for decomposition functions.

## 3.3.2.5. Index structure for decomposition functions.

The index structure for decomposition functions is similar to that for design functions. It also has two layers in the order (i) decomposition-type layer and (ii) case layer. The decomposition-type layer includes three function types, namely main function, interdependent function and auxiliary function, as depicted in Fig. 11.

## 3.4. Searching, matching and ranking similar design cases

This section establishes a structured index method using the concept of a complete tree structure of the K-ary Tree [10,15] to identify quickly the most valuable design cases as references based on the functional requirement-based query model. The primary method is to apply the UID (Unique Element Identifiers) equation to reduce the number of index entries during the search and thus increase efficiency of the search for similar design cases. Therefore, this section first explains the establishment of this structured index. Then, the searching, matching and ranking of similar design cases are developed based on the established structured index.

## 3.4.1. Establishment of structured index

Based on the five index structures for historical design cases established in Section 3.3.2, every node in each tree structure is visited and assigned an UID value using the K-ary Tree method. UID was established using the top to bottom mode, with the value of the parent node in the highest layer taken as UID = 1. The UID values of the child nodes are calculated according to the UID value of the parent node and the branch locations of the child nodes. The equation for the UID value of a child node is defined as follows.

$$
\operatorname{Child} (i, j) = k (i - 1) + j + 1\tag{1}
$$

where i represents the UID value of the parent node; $j ~ ( 1 \leq j \leq k )$ indicates the branch location of the child node under its parent node, and k is the largest of branches in the tree structure.

![](/api/attachments/GCS35EBK/fulltext/images/63222b5707f7e76c730b512b4680bd120af1d391214579b47736f2e2aa7a2933.jpg)  
Fig. 12. K-ary Tree (example of index structure for nouns).

Table 1  
Results for calculating UID values

<table><tr><td>Node</td><td>UID value</td><td>Node</td><td>UID value</td></tr><tr><td>Chassis</td><td>1</td><td>Shock-reduced</td><td>2</td></tr><tr><td>Brake system</td><td>3</td><td>Shock-absorber</td><td>5</td></tr><tr><td>Suspension</td><td>6</td><td>Damping</td><td>7</td></tr></table>

As presented in Fig. 12, and as in the example of the index structure of nouns, the largest branch number is 3, the UID value of the node N is 1; the UID value of its child node bShock-ReducedN is 3(1−1)+1+1=2, and the UID value of the first child node bShock-AbsorberN under the node bShock-ReducedN is 3(2−1)+1+1=5. Accordingly, all the UID values for all the nodes are determined, as shown in Table 1.

## 3.4.2. Searching and matching similar design cases

Similar design cases are searched and matched mainly to retrieve similar design cases through the established index structure for historical design cases based on the described key elements/terms in the functional requirement-based query model.

The “searching similar design cases” involves two searching modes, namely accurate searching mode and similar searching mode. The details are presented below.

3.4.2.1. Accurate searching mode. The accurate searching mode is used to search the matching node in the index structure according to the key element/term in the functional requirement-based query model, and to determine a design case set with the same UID value as that of the matching node. Given the example in Fig. 7, if the node bShock-AbsorberN is exactly the described noun in the functional requirement-based query model and its UID value is 5, then a design case set with the same UID value of 5 is found, which contains cases 2, 11 and 19, as shown in Fig. 13.

3.4.2.2. Similar searching mode. The similar searching mode is triggered by matching a node that does not record any case according to the key element/term in the functional requirement-based query model. Then, the similar searching mode can trace back to the parent node of the matching node by calculating the UID value of the parent node (Eq. (2)). The UID values of other child nodes of the parent node are obtained from the calculated UID value of the parent node (Eq. (1)). Finally, similar design cases are found though the obtained UID values of the child nodes. Meanwhile, the equation for the UID value of a parent node is defined as follows.

$$
\text { Parent } (i) = [ (i - 2) / k + 1 ]\tag{2}
$$

In Eq. 2, i represents the UID value of the node itself while k indicates the largest number for branches in the tree structure.

As in the example shown in Fig. 7, if the conditional noun in the functional requirement-based query model is “Suspension” and this node bSuspensionN in the index structure for nouns has no design case set, then the UID value of its parent node “Shock-Reduced” [(6 −2)/ 3+ 1= 2] is obtained by utilizing the UID value of the node bSuspensionN (UID= 6) and Eq. (2). Next, the other UID values for nodes that are synonymous with “Suspension” (bShock-AbsorberN\_UID=5 and bDampingN\_UID=7) are determined through the UID value of the parent node “Shock-Reduced” (UID= 2)) and Eq. (1). Finally, the similar design cases that record UID = 5 or UID= 7 are found — Case 2, Case 11, Case 19, Case 8 and Case 21 as shown in Fig. 14.

![](/api/attachments/GCS35EBK/fulltext/images/1d8a6a5628cd23106364efc49f29643d9649cf7cba4c63887ea6336270ae94d5.jpg)  
Fig. 13. Accurate searching (example of index structure for nouns).

![](/api/attachments/GCS35EBK/fulltext/images/bcfdbf88efa2de39161eef6ef12edb056a5c85b97995405cbb3cdbcfa8882e48.jpg)  
Fig. 14. Similar searching (example of index structure for nouns).

The foregoing searching modes can be represented as an algorithm written in C language, as presented in Fig. 15.

Based on the results of searching for similar design cases, the Boolean operation is conducted to sift out the more similar design cases. Therefore, this study defines five types for sifting out more similar design cases in the following order of priority. Meanwhile, the first four types ((i), (ii), (iii), and (iv)) are combined for the intersection operation.

(i) {V\_CS}∩{N\_CS}∩{A\_CS}∩{DES\_CS}∩ {DEC\_CS}

(ii) {V\_CS}∩{N\_CS}∩{A\_CS}∩{DES\_CS} or {V\_CS}∩{N\_CS}∩{A\_CS}∩{DEC\_CS}

(iii) {V\_CS}∩{N\_CS}∩{A\_CS}

(iv) {V\_CS}∩{N\_CS}

(v) {N\_CS}

where

“V\_CS” represents a set of design cases most similar to “Verb”,

“N\_CS” represents a set of design cases most similar to “Noun”,

“A\_CS” represents a set of design cases most similar to “Adverb”,

“DES\_CS” represents a set of design cases most similar to “Design Type”, and

“DEC\_CS” represents a set of design cases most similar to “Decomposition Type”.

For the defined five types used to sift similar design cases, the design cases obtained from the first type of combination for the intersection operation are the most similar to the functional requirement-based query model. If the result of the intersection operation with the first type of combination is a null set, then the second type of combination is used to perform the intersection operation, producing design cases that are the secondmost similar to the functional requirement-based query model. In this way, the intersection operation is conducted continuously. Additionally, if the result from the first four types of combinations in the intersection operation is a null set, then the fifth type for sifting similar design cases is employed and the obtained design cases are regarded as the most similar design cases.

## 3.4.3. Ranking similar design cases

The obtained similar design cases discussed in the previous subsection, are ranked by calculating the degree of similarity with the functional requirementbased query model to provide engineering designers the most possible reference.

The calculation performed to rank similar design cases utilizes primarily the weight equation for the different elements/terms (verbs, nouns, adverbs, design types, and decomposition types) in the design case. Their weights are thus determined in their own index structure for historical design cases. The calculation of weight value can be divided into two modes based on the modes of accurate searching and similar searching, as discussed in Section 3.4.2. As shown in Fig. 16, if the accurate searching mode is operated (Fig. 16(a)), then the weight for the design cases should be 1 (Eq. (3)); if the similar searching

```txt
int times,no,num,maxLEVEL,totalnode,savedno,answerno;
float fatherUID;

for(no=1;no=totalnode;no++)
{
    if(word==table[Node][no])
    {
    ROW=no;
    tempUID[savedno]=table[UID][no];
    break;
    }
}

if(table[CASEid][ROW]==null)
{
    savedno=savedno-1;
    fatherUID=(table[UID][ROW]-1)/k+1
    for(num=1;num=maxUID;num++)
    {
    if((num<=fatherUID)&&(fatherUID<num+1))
    {
    fatherUID=num;
    for(no=1;no=totalnode;no++)
    {
    if(table[UID][no]==fatherUID)
    {
    ROW=no;
    break;
    }
    }
    }
    }
}

if(table[CHILDno][ROW]!=0)
{
    for(times=1;times=table[CHILDno][ROW];times++)
    {
    tempUID[savedno]=k*(fatherUID+1)+times+1;
    savedno=savedno+1;
    }
}

for(no=1;no=savedno;no++)
{
    for(times=1;times=totalnode;times++)
    {
    if((tempUID[savedno]==table[UID][times])&&(table[CASEeid][times]))
    {
    for(anwserno=1;answerno;answerno++)
    {
    anwserCASEid[answerno]=table[CASEid][times];
    }
    }
    }
}
```  
Fig. 15. The algorithm for searching design cases.

mode is operated (Fig. 16(b)), then the weight for the design cases should be determined by applying the concept of entropy [5,25] (Eq. (3)). When a term appears in a certain class with a higher frequency (with more design cases), this term better describes this class. Therefore, the obtained weight is larger.

In Eq. (3), $d _ { i j }$ denotes that the total number j of design cases in ith class while W represents the weight of the (a) The Weight Value of Case for Accurate Searching

![](/api/attachments/GCS35EBK/fulltext/images/18fa379d2d8c6e2504a380dd5351dfc2b34d2559dc86eaf4b020fdf9a3913aa5.jpg)

(b) The Weight Value of Case for Similar Searching  
![](/api/attachments/GCS35EBK/fulltext/images/0119ddfc84c9afa8b22c705caf591f3b023552e40532e27bf2e3a03974df33d8.jpg)  
Fig. 16. Allocation of weights for (a) accurate searching and (b) similar searching.

design cases that belong to a certain term in the index structure.

$W { = } \left\{ \sum _ { j = 1 } ^ { d _ { i j } } d _ { i j } \right.$ if Search Model is in Similar Searching Mode ; if Search Model is in Accurate Searching Mode

$$
\mathrm{Sim} \Big (\vec {q}, \vec {\mu} \Big) = \frac {\vec {q} \cdot \vec {\mu}}{| \vec {q} | \times | \vec {\mu} |}\tag{3}
$$

4

The vector model, mentioned in information retrieval [23], is adopted to calculate the total similarity value Sim of a design case. As indicated in Fig. 17, the weight values for different described terms/elements in the index structures for historical design cases can be represented as the number of dimensions of a vector. For example, if the intersection operation is applied to five terms/elements in the first type of combination for this operation, then the weights of these five terms/elements are expressed in as a 5-dimensional vector equation $\vec { q }$ , and then the cosine between the vector $\vec { q }$ and the unit vector $\vec { \mu }$ is calculated using Eq. (4) to determine their similarity.

An example clarifies the explanation of the steps in searching, matching and ranking similar design cases is in the following.

If the search modes for the four key elements/terms (nouns, verbs, design types and decomposition types) in the functional requirement described by the engineering designer are all accurate searching modes, while the search mode for the other key element (adverbs) is the similar searching mode, then the steps and results are as follows.

![](/api/attachments/GCS35EBK/fulltext/images/553872e8bc883604f11da85e37b52e5beaf5ffcac50234ef6bc85fbe1a074919.jpg)  
Fig. 17. Adopted cosine of θ is sim(μ,q) (an example).

Step 1: Assume that the similar design cases derived from the accurate searching mode and similar searching mode by using Eqs. (1) and (2), are respectively as shown below:

Accurate Searching Mode:

$$
\left\{ \begin{array}{l} \mathrm {N\_CS} = \{C (i) \} = \{C _ {3}, C _ {1 1}, C _ {1 3}, C _ {1 5} \} \\ \mathrm {V\_CS} = \{C (j) \} = \{C _ {2}, C _ {3}, C _ {5}, C _ {1 1}, C _ {1 5} \} \\ \mathrm {DES\_CS} = \{C (k) \} = \{C _ {3}, C _ {9}, C _ {1 1}, C _ {1 2}, C _ {1 5} \} \\ \mathrm {DEC\_CS} = \{C (h) \} = \{C _ {3}, C _ {9}, C _ {1 1}, C _ {1 5} \} \end{array} \right.
$$

Similar Searching Mode:

$$
\begin{array}{r l} \{\mathrm {A\_CS} & = \{C (m) \} \cup \{C (n) \} \cup \{C (p) \} \\ & = \{C _ {2}, C _ {3}, C _ {5}, C _ {7}, C _ {8}, C _ {1 1}, C _ {1 2}, C _ {1 5}, C _ {1 6} \} \end{array}
$$

Meanwhile, $C ( m ) { = } \{ C _ { 2 } , C _ { 8 } , C _ { 1 1 } \} , C ( n ) { = } \{ C _ { 3 } , C _ { 5 } , C _ { 1 2 } , $ $C _ { 1 6 } \}$ , and $C ( \boldsymbol { p } ) = \{ C _ { 7 } , C _ { 1 5 } \}$

Step 2: Using Eq. (3), calculate the weights for the similar design cases of each element/term.

$$
\begin{array}{r l} W (\mathrm {N\_CS}) & = W (C (i)) = 1 (\text { i.e., } W (C _ {3}) = W (C _ {1 1}) \\ & = W (C _ {1 3}) = W (C _ {1 5}) = 1) W (\mathrm {V\_CS}) \\ & = W (C (j)) = 1 (\text { i.e., } W (C _ {2}) = W (C _ {3}) \\ & = W (C _ {5}) = W (C _ {1 1}) = W (C _ {1 5}) \\ & = 1) W (\mathrm {DES\_CS}) = W (C (k)) \\ & = 1 (\text { i.e., } W (C _ {3}) = W (C _ {9}) = W (C _ {1 1}) \\ & = W (C _ {1 2}) = W (C _ {1 5}) = 1) W (\mathrm {DEC\_CS}) \\ & = W (C (h)) = 1 (\text { i.e., } W (C _ {3}) = W (C _ {9}) \\ & = W (C _ {1 1}) = W (C _ {1 5}) = 1) \end{array}
$$

$$
\begin{array}{l} W (\mathrm {A\_CS}) = W (C (m)) = 3 / 9 \\ \quad \text {(i.e.,} W (C _ {2}) = W (C _ {8}) = W (C _ {1 1}) = 3 / 9) \\ W (\mathrm {A\_CS}) = W (C (n)) = 4 / 9 \\ \quad \text {(i.e.,} W (C _ {3}) = W (C _ {5}) = W (C _ {1 2}) = W (C _ {1 6}) = 4 / 9) \\ W (\mathrm {A\_CS}) = W (C (p)) = 2 / 9 \\ \quad \text {(i.e.,} W (C _ {7}) = W (C _ {1 5}) = 2 / 9) \end{array}
$$

Step 3: Conduct the first type of combinations for the intersection operation (Boolean Operation)

$$
\begin{array}{l} \text {(i)} \{\mathrm {V\_CS} \} \cap \{\mathrm {N\_CS} \} \cap \{\mathrm {A\_CS} \} \cap \{\mathrm {DES\_CS} \} \cap \\ \{\mathrm {DEC\_CS} \} = \{C _ {3}, C _ {1 1}, C _ {1 5} \} \end{array}
$$

Step 4: Calculate the total similarity for each similar design case obtained in Step 3 using Eq. (4).

$$
\vec {c} _ {3} = \langle 1, 1, \frac {4}{9}, 1, 1 \rangle , \vec {c} _ {1 1} = \langle 1, 1, \frac {3}{9}, 1, 1 \rangle ,
$$

$$
\vec {c} _ {1 5} = \langle 1, 1, \frac {2}{9}, 1, 1 \rangle , \vec {\mu} = \langle 1, 1, 1, 1, 1 \rangle
$$

$$
\operatorname{Sim} \left(\vec {c} _ {3}, \vec {\mu}\right) = \frac {\vec {c} _ {3} \cdot \vec {\mu}}{| \vec {c} _ {3} | \times | \vec {\mu} |} = 0. 9 7 0
$$

$$
\operatorname{Sim} \left(\vec {c} _ {1 1}, \vec {\mu}\right) = \frac {\vec {c} _ {1 1} \cdot \vec {\mu}}{| \vec {c} _ {1 1} | \times | \vec {\mu} |} = 0. 9 5 6
$$

$$
\operatorname{Sim} \left(\vec {c} _ {1 5}, \vec {\mu}\right) = \frac {\vec {c} _ {1 5} \cdot \vec {\mu}}{\left| \vec {c} _ {1 5} \right| \times \left| \vec {\mu} \right|} = 0. 9 3 8
$$

Step 5: Ranking similar design cases based on the results obtained in Step 4.

The result of the first type of combination in the intersection operation is not a null set, and the obtained design cases are $C _ { 3 } , C _ { 1 1 }$ , and $C _ { 1 5 } .$ . Ranking in order of similarity yields the ultimate result, $\mathrm { C a s e } _ { 3 } , \mathrm { C a s e } _ { 1 1 } ,$ and $\mathrm { C a s e } _ { 1 5 }$ . Consequently, ${ \mathrm { C a s e } } _ { 3 }$ is the most similar and valuable design case to the functional requirement-based query model as described by the engineering designer.

## 4. System implementation and use: an example

## 4.1. System implementation

Based on the proposed techniques for functional requirement-based reference design retrieval, a prototype functional requirement-based reference design retrieval mechanism was implemented at the Enterprise System Engineering Lab (ESEL) of National Cheng Kung University, Taiwan, ROC.

Figs. 18 and 19 present a subset of the user interfaces of a functional requirement-based reference design retrieval mechanism. Meanwhile, Fig. 18 shows the screen of functional requirement description for the users, while Fig. 19 displays the screen of similarity ranking for retrieved cases. Moreover, Fig. 20 illustrates the E-R model in constructing database. Fig. 21 presents a schema diagram for the database.

## 4.2. The scenario of users used

Based on the implemented system, this subsection aims to describe the scenarios of how the users are to be used. As illustrated in Fig. 22, the scenario is initiated by requesting reference designs in designing functions of a part. Subsequently, functional description for of reference designs is conducted in the screen of the implemented system. According the functional description, the design entities with similar functional features are orderly searched, matched, retrieved and ranked in running this system. Finally, the most similar design entity with related design knowledge and experience are good references for designers who are in the phase of designing functional features.

![](/api/attachments/GCS35EBK/fulltext/images/18c2889e43cf265a81bbeb7c0514dad87956a11228d08932fd246431e5db61c4.jpg)  
Fig. 18. User interface— functional requirement description.

## 5. An experimental result on performance

In order to evaluate the performance of the developed system with the index structures, a novel and effective method, entitled “All Nodes without Replication (ANOR)” [15] was proposed by Lee et al., 1996. Therefore, this study adopted this measure to evaluate the system as follows.

The experiment on the performance of the developed system was conducted by designing a mold for passive components at System Engineering Center, Industrial Technology Research Institute, Taiwan. In this experiment, ten designers who have over four-year design experience for the functional requirement analysis task are required as experimental targets. The experiment on indexing and retrieving similar designed entities within the index structure of noun has been executed on Acer Power 590h PC™ workstation with a local Conner CP30200 disk. In the Conner CP230200 model [8], the disk access times required to retrieve the postings list of a keyword is the sum of B+-tree access time and postings list access time, as shown in Eq. (5).

$$
T _ {\text { search }} = T _ {\text { btree }} + T _ {\text { posting }}\tag{5}
$$

In Eq. (5), the disk access time of B+-tree is $T _ { \mathrm { b t r e e } } =$ $l ^ { * } t _ { \mathrm { r a n d o m } } ,$ while the disk access time of the postings list of a keyword is $T _ { \mathrm { p o s t i n g } } { = } t _ { \mathrm { r a n d o m } } { + } ( N _ { \mathrm { b l o c k \mathrm { ~ p e r } \mathrm { ~ k e y } } } { - } 1 ) ^ { \ast } t _ { \mathrm { s e q } } .$ Meanwhile, the number of disk blocks of the postings list per keyword is $\begin{array} { r } { N _ { \mathrm { b l o c k \mathrm { - } p e r \mathrm { \_ k e y } } } = \left\lceil \frac { S _ { \mathrm { p o s t i n g } } } { n _ { \mathrm { k e v } } } \right\rceil } \end{array}$

![](/api/attachments/GCS35EBK/fulltext/images/88eb420a6757877a725bf5de9be3abf8e191bc0eeb7aa7014aec3354356de9fd.jpg)  
Fig. 19. User interface — similarity ranking for retrieval cases.

![](/api/attachments/GCS35EBK/fulltext/images/f614aa6a65695d7a17cd9cddc21eea56b59335c5499573a83004ef57df96fead.jpg)

Fig. 20. E-R model of the design case.

<table><tr><td></td><td>Case_Name</td><td>Case_Id</td><td>Eng_Model_Loc</td><td>移除篩選</td><td>sl_Langu</td><td>Eng_Model_Name</td><td>Eng_Model_Creato</td><td>Eng_Model_G</td></tr><tr><td></td><td>Car</td><td>1</td><td>Doc_001</td><td>English</td><td>Car_Model</td><td>Marly</td><td>Emp_005</td><td></td></tr><tr><td></td><td>Car</td><td>2</td><td>Doc_101</td><td>English</td><td>car_Model</td><td>James</td><td>Emp_025</td><td></td></tr><tr><td></td><td>Car</td><td>3</td><td>Doc_006</td><td>English</td><td>Car_Model</td><td>james</td><td>Emp_002</td><td></td></tr><tr><td></td><td>Truck</td><td>4</td><td>Doc_211</td><td>English</td><td>Truck_Model</td><td>james</td><td>Emp_113</td><td></td></tr><tr><td></td><td>Car</td><td>5</td><td>Doc_234</td><td>English</td><td>Car_Model</td><td>Marly</td><td>Emp_678</td><td></td></tr><tr><td></td><td>Car</td><td>7</td><td>Doc_154</td><td>English</td><td>Car_Model</td><td>Denis</td><td>Emp_112</td><td></td></tr><tr><td></td><td>SUV</td><td>12</td><td>Doc_687</td><td>English</td><td>SUV_Model</td><td>Denis</td><td>Emp_269</td><td></td></tr><tr><td></td><td>SUV</td><td>15</td><td>Doc_587</td><td>English</td><td>SUV_Model</td><td>Oliver</td><td>Emp_638</td><td></td></tr><tr><td></td><td>Car</td><td>16</td><td>Doc_387</td><td>English</td><td>Car_Model</td><td>Oliver</td><td>Emp_521</td><td></td></tr><tr><td></td><td>Car</td><td>21</td><td>Doc_328</td><td>English</td><td>Car_Model</td><td>Marly</td><td>Emo_367</td><td></td></tr><tr><td></td><td>RV</td><td>23</td><td>Doc_638</td><td>English</td><td>RV_Model</td><td>Peter</td><td>Emp_689</td><td></td></tr><tr><td></td><td>Car</td><td>25</td><td>Doc_368</td><td>English</td><td>Car_Model</td><td>Peter</td><td>Emp_6398</td><td></td></tr><tr><td></td><td>Car</td><td>28</td><td>Doc_638</td><td>English</td><td>Car_Model</td><td>John</td><td>Emp_3298</td><td></td></tr><tr><td></td><td>Truck</td><td>34</td><td>Doc_873</td><td>English</td><td>Truck_Model</td><td>Dinos</td><td>Emo_57623</td><td></td></tr><tr><td></td><td>Car</td><td>39</td><td>Doc_637</td><td>English</td><td>car_model</td><td>Dinos</td><td>Emo_2843</td><td></td></tr><tr><td></td><td>Car</td><td>43</td><td>Doc_682</td><td>English</td><td>Car_Model</td><td>Dinos</td><td>Emp_5787</td><td></td></tr><tr><td></td><td>Car</td><td>47</td><td>Doc_587</td><td>English</td><td>Car_Model</td><td>Wildcat</td><td>Emp_638</td><td></td></tr><tr><td></td><td>RV</td><td>78</td><td>Doc_367</td><td>English</td><td>RV_Model</td><td>Wildcat</td><td>Emp_386</td><td></td></tr><tr><td></td><td>Car</td><td>80</td><td>Doc_367</td><td>English</td><td>Car_Model</td><td>jean</td><td>Emp_628</td><td></td></tr><tr><td></td><td>Truck</td><td>90</td><td>Doc_343</td><td>English</td><td>Truck_Model</td><td>Jean</td><td>Emp_642</td><td></td></tr><tr><td></td><td>Car</td><td>134</td><td>Doc_368</td><td>English</td><td>Car_Model</td><td>Jean</td><td>Emp_571</td><td></td></tr></table>

Fig. 21. Schema for design cases in database.

![](/api/attachments/GCS35EBK/fulltext/images/4fe3d65328c143ed0a7a2a63d4705043c95c58f40a167b0fe65c0d86f8849c12.jpg)  
Fig. 22. The scenario of users used.

<sup>- -</sup>We have experimented in a ten user's environment after building a partial inverted index in a 100 Mb disk space. Meanwhile, we have assumed the database contains 100,000 designed entities with 50,000 keywords. Fig. 23 shows the result of the experiment obtained by accessing the index for a given keyword 100 times each and averaging the access times. Clearly, the disk access time gradually decreases with increasing promotion rate of incremental values.

This experimental result certainly demonstrates that the proposed techniques worked efficiently for indexing and retrieving similar designed entities in the index structure of noun.

In measuring designers' satisfactions, the Delphi Method [6] has become a widely used tool for obtaining a consensus of opinion from a panel of experts. Therefore, this study conducts the Delphi Method to investigate the ten designers' satisfactions for their retrieved results by the system. By using the designed questionnaire shown in Table 2, the finding indicates that over ninety percent of designers satisfied the results for retrieving and ranking similar design cases.

![](/api/attachments/GCS35EBK/fulltext/images/ede495cfe0e8dd0dbae39204a23be94f65b062d9985e989721f161046244563e.jpg)  
Fig. 23. Experimental disk access time within index structure of noun.

## 6. Conclusions and discussions

## 6.1. General remarks

This study first presents an engineering knowledge management framework, and then focuses on developing technology for functional requirement-based reference design retrieval. The crucial techniques in functional requirement-based reference design retrieval include (i) the definition and representation of a structured query model for functional requirements, (ii) the establishment of index structures for historical design cases, (iii) functional requirement-based case searching and matching, (iv) functional requirement-based case ranking, and (v) a case-based representation of designed entities. The functional requirement-based reference design retrieval mechanism is implemented based on the aforementioned techniques.

The results of this study facilitate the practical sharing of engineering knowledge for engineering knowledge management in engineering design environments, and can thus increase product development capability, reduce development cycle time and cost, and ultimately enhance product marketability.

## Table 2

The questionnaire of evaluating designers' satisfactions

1. The degree of which the function entry “Noun” supports designers in identifying query. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 2. The degree of which the function entry “Noun” supports designers in identifying goal and output. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 3. The degree of which the function entry “Verb” supports designers in identifying query. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 4. The degree of which the function entry “Verb” supports designers in identifying goal and output. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 5. The degree of which the function entry “Adverb” supports designers in identifying query. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 6. The degree of which the function entry “Adverb” supports designers in identifying goal and output. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 7. The user interface spend less time than that by manual evaluation. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 8. The user interface easy to use. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1) 9. The user interface useful to identification. □Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)

## 6.2. Future research

Engineering design can be seen as a transformation process from customer requirements through functional requirements, functional form features and engineering specifications to final product geometry. Therefore, products must be defined on several levels other than that of customer requirements to enable reference design retrieval. Hence, the following further research can be pursued to enhance the practical sharing of engineering knowledge in engineering design.

## 6.2.1. Functional feature-based reference design retrieval mechanism

Functional features are obtained by analyzing functional requirements. In the task, historical product information and engineering knowledge are retrieved as references based on the perspective of functional features. Therefore, effectively retrieving theses references from the historical knowledge repository based on the description of functional features represents an important issue in future research.

## 6.2.2. Engineering specification-based reference design retrieval mechanism

This issue represents an extension of the functional feature-based reference design retrieval mechanism. Based on the search results of the functional featurebased reference design retrieval mechanism, the engineering specification-based reference design retrieval mechanism can filter more precise results by using engineering specifications.

## Acknowledgement

The authors would like to thank the National Science Council of the Republic of China for financially supporting this research under Contract No. NSC 93-2212- E-006-021.

## References

[1] Y.M. Chen, M.W. Liang, Design and implementation of a collaborative engineering information system for allied concurrent engineering, International Journal of Computer Integrated Manufacturing 13 (1) (1999) 11–30.

[2] Y.M. Chen, Y.D. Zan, Enabling allied concurrent engineering through distributed engineering information management, Robotics and Computer-Integrated Manufacturing 16 (1) (2000) 9–27.

[3] Y.M. Chen, W.S. Shir, C.Y. Shen, Distributed engineering change management for allied concurrent engineering, International Journal of Computer Integrated Manufacturing 15 (2) (2002) 127–151.

[4] Y.M. Chen, Y.J. Chen, C.B. Wang, H.C. Chu, Knowledge refinement for engineering knowledge management, Concurrent Engineering, Research and Applications 13 (1) (2005) 43–56.

[5] H.L. Chieu, H.T. Ng, A maximum entropy approach to information extraction from semi-structured and free text, 18th National Conference on Artificial Intelligence, 2002, pp. 786–791.

[6] C. Chou, Developing the e-Delphi system: a web-based forecasting tool for educational research, British Journal of Educational Technology 33 (2) (2002) 234–236.

[7] D.W. Cockshoot, Engineering data management for concurrent engineering globally, Computing & Control Engineering Journal 7 (2) (1996) 69–74.

[8] Conner Periperials, Inc., CP-30200 specification summary, 1995.

[9] G.E. Dieter, Engineering Design, McGraw-Hill, New York, 2000.

[10] S. Dongwook, J. Hyuncheol, J. Honglan, BUS: an effective indexing and retrieval scheme in structured documents, ACM International Conference on Digital Libraries, 1998, pp. 235–243.

[11] A. Ertas, J.C. Jones, The Engineering Design Process, Wiley, NY, 1993.

[12] A. Ertas, J.C. Jones, The Engineering Design Process, 2d ed., Wiley, New York, 1996.

[13] C. Hales, Managing Engineering Design, Longman Scientific & Technical, 1993.

[14] G.R. Homer, D.M. Thompson, M. Deacon, A distributed document management system, Computing & Control Engineering Journal 13 (6) (2002) 315–318.

[15] Y.K. Lee, S.J. Yoo, K. Yoon, P.B. Berra, Index structures for structured documents, ACM International Conference on Digital Libraries, 1996, pp. 91–99.

[16] K.M. Lee, C.W. Lau, K.M. Yu, Y.K. Fung, Development of a dynamic data interchange scheme to support product design in agile manufacturing, International Journal of Production Economics 87 (3) (2004) 295–308.

[17] E.Y. Li, H. Lai, Collaborative work and knowledge management in electronic business, Decision Support Systems 39 (4) (2005) 545–547.

[18] D.E. O'Leary, Enterprise knowledge management, Computer 31 (3) (1998) 54–61.

[19] G. Pahl, W. Beitz, K. Wallace, Engineering Design, Design Council, London, 1984, p. 1984.

[20] S. Pugh, Total Design — Integrated Methods for Successful Product Engineering, Addition–Wesley Publishing Company, Wokingham, 1990.

[21] T.S. Raghu, A. Vinze, A business process context for knowledge management, Decision Support Systems 43 (3) (2007) 1062–1079.

[22] B. Ramesh, A. Tiwana, Supporting collaborative process knowledge management in new product development teams, Decision Support Systems 27 (1–2) (1999) 213–235.

[23] B.Y. Ricardo, R.N. Berthier, Modern Information Retrieval, ACM Press, 1999.

[24] C.P. Ruppel, S.J. Harrington, Sharing Knowledge through Intranets: A Study of Organizational Culture and Intranet Implementation, Professional Communication, IEEE Transactions on, vol. 44, No. 1, 2001, pp. 37–52.

[25] C. Shannon, A mathematical theory of communication, Bell System Technical Journal, Vol. 27, pp. 379–423 and 623–656, 1948.

[26] J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, IBM Systems Research Institute, NY, 1984.

[27] W.M. Tepfenhart, J.P. Dick, J.F. Sowa, Conceptual structures: current practices, International Conference on Conceptual Structures, 1994.

[28] D.G. Ullman, The Mechanical Design Process, 2d ed., McGraw-Hill, New York, 2003.

[29] C.P. Wei, J.H. Hu, H.H. Chen, Design and evaluation of a knowledge management system, Software IEEE 19 (3) (2002) 56–59.

[30] K.Y. Wong, E. Aspinwall, Development of a knowledge management initiative and system: A case study, Expert Systems with Applications 30 (4) (2006) 633–641.

[31] L. Xu, Z. Li, S. Li, F. Tang, A decision support system for product design in concurrent engineering, Decision Support Systems 42 (4) (2007) 2029–2042.

[32] X. Zhang, H. Han, An empirical testing of user stereotypes of information retrieval systems, Information Processing & Man agement 41 (3) (2005) 651–664.

![](/api/attachments/GCS35EBK/fulltext/images/09584bae7e39b37d7937cd9ff9f625be7df434f9e82c670d97e1226dbdcbdbbd.jpg)  
Dr. Yuh-Jen Chen is currently an Assistant Professor of the Department of Medical Information Management, Kaohsiung Medical University, Taiwan, ROC. He received his Ph D. and M S. degrees from the Institute of Manufacturing Engineering of National Cheng Kung University in 2005 and 2001 respectively, and gained his BS degree from the Department of Mathematics of Chung Yuan Christian University, Taiwan, ROC, in

1999. His current research interests include enterprise system development and implementation, knowledge engineering and man agement, e-Business, and medical information management.

![](/api/attachments/GCS35EBK/fulltext/images/c771c4008df1cb6a2d6789c406fb05933cc4dd5fb2fb1d3f7d0d1ecb3e376b4c.jpg)

Dr. Yuh-Min Chen is currently a Professor and the Director of the Institute of Manufacturing Engineering, College of Electrical Engineering and Computer Science, National Cheng Kung University, Taiwan, ROC. He graduated from The Ohio State University with a Ph.D. degree in Industrial and Systems Engineering in 1991 and received his M.S. and B.S. degrees from National Tsing Hua University, Taiwan, ROC, in 1981 and 1983 respectively. Before joining

the faculty of the Institute of Manufacturing Engineering in 1994, he worked as a Research Engineer in Structural Dynamics Research Corporation, USA for three years. His current research interests include enterprise integration, engineering data and knowledge management, computer-aided concurrent engineering, and manufacturing information systems.

![](/api/attachments/GCS35EBK/fulltext/images/26f3969d969554d67795ed68a20a71995d03e74d886758a4971b7e9cddb6e256.jpg)

Dr. Hui-Chuan Chu is an Associate Profes sor of the Department of Special Education, National University of Tainan in Taiwan, ROC. She received her Ph.D. degree from Columbia University in 1998. Her research interests are knowledge management, teacher knowledge and integration of information technology in teacher education.

![](/api/attachments/GCS35EBK/fulltext/images/9abac8570d59338731e89372eef0bab9c25bd2c0ea6a312a5118edf2da870d05.jpg)

Mr. Hao-Yun Kao is now a Ph.D. candidate in the Department of Information Management at National Sun Yat-Sen University, Kaohsiung, Taiwan. Mr. Kao had been an Instructor with 6 years teaching experience in the Department of Medical Informatics Management, Kaohsiung Medical University, Taiwan. Prior to entering the Ph.D. program, he received a B.S. degree in Healthcare Administration. He had practical experience about 14 years in health-

care organization. His current research interests include organizational, competency development and strategies issues in e-health, and healthcare administration.
