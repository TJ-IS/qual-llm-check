---
otero_id: 2326
otero_key: "58VTMAYA"
title: "Recommending Remedial Learning Materials to Students by Filling Their Knowledge GAPS1"
authors: "Konstantin Bauman; Alexander Tuzhilin"
year: "2018"
journal: "MIS Quarterly"
doi: "10.25300/misq/2018/13770"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RECOMMENDING REMEDIAL LEARNING MATERIALS TO STUDENTS BY FILLING THEIR KNOWLEDGE GAPS<sup>1</sup>

Konstantin Bauman Fox School of Business, Temple University, 1810 N. 13<sup>th</sup> Street, Philadelphia, PA 19122 U.S.A. {kbauman@temple.edu}

Alexander Tuzhilin Stern School of Business, New York University, KMC 44 West 4<sup>th</sup> Street New York, NY 10012 U.S.A. {atuzhili@stern.nyu.edu}

We study the problem of providing recommendations to students that help them in their studies. To address this problem, we present an approach of providing recommendations of remedial learning materials to students that fill the gaps in their knowledge of the subject in the courses they take. According to this method, we first identify gaps in the student’s mastery of various course topics. We then identify those items from the library of assembled learning materials that help us to fill those gaps, and recommend these identified materials to the student. We show empirically through A/B testing that this approach leads to better performance results, as measured by a student’s total score on the final exam across the personalized, nonpersonalized, and control groups and by improvement of the student’s average score on that exam in comparison to previously taken courses. The proposed method is scalable since it can be applied to a large number of students across many courses.

Keywords: Recommender systems, enhanced learning, on-line education, knowledge gap

## Introduction

Some academics and practitioners argue that higher education is going through a major transformation driven by (1) disruptive changes caused by the digital revolution and advances in online educational models and technologies (Christensen et al. 2011; Dellarocas and Van Alstyne 2013; Lucas 2014) and (2) strong pressure to educate the population and workforce better, more effectively, and on a larger scale, so that their knowledge is current and they are well trained. One of the major trends in the education industry are rapid advancements of technology-based educational learning tools and platforms, including the next generation of e-learning and learning management systems (LMSes) that are projected to go far beyond the current functionality of Blackboard, Sakai, Moodle, and other systems. The next generation of these systems will be significantly more active and will enhance student learning by providing various types of advice to students on what should be learned and how by employing adaptive learning and recommendation methods (Brusilovsky and Nejdl 2004; Graf et al. 2012; Peña-Ayala 2013). In particular, the industry has been moving rapidly in this direction with such companies as Khan Academy (www.khanacademy. org), Coursera (www.coursera.org), and Knewton (www. knewton.com) recommending different types of learning activities to students in order to proactively advance their knowledge of the subject matter covered in courses. In academia, the subject of technology enhanced learning (TEL), including adaptive learning, has been studied by various authors over the years (Balacheff et al. 2009).

One particular type of TEL relevant to the next generation of e-learning systems is recommender systems that provide various types of advice to students based on knowledge of a student’s prior performance and educational background. Some examples of this advice constitute recommendations of novel reading materials, requests to do additional quiz and homework assignment questions, and recommendations on whom to talk to in order to answer different types of questions about a subject. These types of advice provided by recommender systems are badly needed in many educational settings, and will be needed even more in the future within the context of the growth and proliferation of various e-learning environments for the following reasons. First of all, the volume of online educational materials and online knowledge sources has expanded extensively over the past several years and will continue to grow at a similar pace in the future. This will create an even greater deluge of different types of information of various levels of relevance, sophistication, and quality, making it harder for less-experience learners to digest and navigate though this massive content on their own. Still another factor making recommender systems important in e-learning settings is the advancement and increasing popularity of adaptive learning environments that try to personalize the student’s learning experience (Brusilovsky and Peylo 2003) including the provision of personalized recommendations. All of this points to the growing popularity of recommender systems in the context of TEL-based environments and the significant benefits they can provide to business and society, facilitating better education of future generations of students and helping the workforce stay current and welltrained.

TEL-based recommendations can be classified into two major types. The first type constitute knowledge enhancing recommendations that focus on the next learning activity, expanding and broadening the student’s knowledge of the subject matter. This type of recommendation is advocated by Khan Academy, Knewton, and some other companies and authors (Drachsler et al. 2015; Murphy et al. 2014; Wilson and Nichols 2015). The second type constitutes remedial advice that identifies existing gaps in a student’s knowledge of the subject matter while the student progresses through the course and attempts to “fill in” these gaps by recommending appropriate learning materials and activities. As discussed in the next section, this type of remedial advice differs significantly from knowledgeenhancing advice. Since the two approaches are complementary to each other, it is necessary to study both of them.

In this paper, we focus on the remedial approach to TELbased recommendations. In particular, we present a methodology that produces reactive personalized filling-the-gap recommendations to students by assembling a library of learning materials to be used for recommendation purposes, constructing the learning structure of the course and identifying various topics covered in it, determining gaps in student performance in the course, and identifying remedial learning materials to be recommended to students in order to fill in these knowledge gaps. Furthermore, we show empirically (through A/B testing) that this approach leads to better performance results, as measured by the student’s total score on the final exam and by improvement of the student’s average score on that exam (in comparison to previously taken courses). As we show in the paper, the proposed approach is scalable since it can be applied to hundreds of courses taught in large universities and to many students, and is also generic since it can be used in numerous types of learning institutions with different kinds of learning environments.

As a part of this study, we show that the proposed method produces good recommendations in the following sense. First, most of the students who received our recommendations found them relevant and helpful. Second, our personalized recommendations were not only appreciated by the students but were also effective for “good” students who had average grades between 70 and 90 in previous courses. This was the case because they lead to a significantly better performance of these students on the final exams compared to their prior performance before they received personalized recommendations. Third, our study showed no statistically significant performance differences between the control group and the nonpersonalized group of students who received a standard set of recommendations. Fourth, we have shown that personalized recommendations work significantly better than nonpersonalized ones for good students and some performance metrics.

## Prior Work

There has been extensive work on recommender systems over the past 20 years covering a broad range of topics and fields (Adomavicius and Tuzhilin 2005b; Ricci et al. 2011). In the Information Systems field, research on recommender systems has focused on several research streams (Li and Karahanna 2015). One such streams is the study of how recommender systems affect the sales of products in the long tail vis-à-vis the head of the frequency distribution. In particular, Brynjolfsson et al. (2011) found that customers’ usage of recommender systems is associated with increased consumption of niche products from the long tail. Also Fleder and Hosanagar (2009) studied the effects of recommender systems on aggregate demand and markets. They showed that recommender systems can lead to a reduction in aggregate sales diversity and the “rich-get-richer” effect. Another research stream studies performance of recommender systems from the business perspective. In particular, Kumar and

Benbasat (2006) showed recommendations and consumer reviews increase both the usefulness and social presence of the website. Further, the empirical analysis presented in Pathak et al. (2010) showed that strength of recommendations has a positive impact on sales. In addition, Ghose et al. (2012) proposed using important economics-related metrics, such as surplus, instead of classical machine learning and statistics-based metrics, such as RMSE, precision, and recall, when evaluating business performance of recommender systems. Moreover, Zhang et al. (2011) showed that a higher quality of personalized product recommendations is associated with lower product screening costs, but higher product evaluation cost. Still another research stream focuses on the impact of recommender systems on decision processes (Adomavicius and Tuzhilin 2005a; Xiao and Benbasat 2007, 2014).

Another important area where recommender systems made significant progress over the past decade is in the field of technology enhanced learning (TEL), where recommender systems can be classified into the following three main types (Manouselis et al. 2013): recommendations of (1) “good” novel items, such as web pages or books, (2) peers, such as suggesting users with similar interests, and (3) good pathways, such as sequences of learning items. The latest survey of these recommendation methods is presented in Drachsler et al. (2015), where most of the reviewed methods use standard rating-based recommendation techniques, including classical collaborative filtering, content-based, and hybrid methods (Adomavicius and Tuzhilin 2005b; Ricci et al. 2011).

More recent TEL recommendation methods, however, depart from these traditional approaches by focusing on the identification of gaps and strengths in students’ mastery of the subject matter and providing appropriate recommendations to improve students’ learning. In particular, Bethard et al. (2012) present an algorithm for identifying students’ misconceptions about the subject that they study (such as geology studies in their case) by analyzing students’ essays and comparing these essays with the set of concepts defined by a set of sentences learned from a subject-related text corpus. Then they recommend reading materials from the given library based on these identified misconceptions. The approach presented in Bethard et al. uses mostly nonlinear programming (NLP) methods and therefore is applicable mainly to the analysis of students’ essays and recommending appropriate reading materials based on this analysis. In contrast, our method does not rely exclusively on students’ essays since we also work with other types of documents, such as quizzes and exams, and mine key concepts from these sources, which makes our method more universal. We also automatically mine the knowledge taxonomy of the courses from the course syllabi, building the library of additional learning materials for the students. Furthermore, our method is applicable to a large variety of subjects and a number of course offerings (e.g., we applied it to 42 different course subjects in an online university in the case study discussed in the “Empirical Study” section and could have scaled it to many more if needed). Finally, unlike Bethard et al., we test whether our recommendations actually improve students’ performance in the course in a real-life experiment (using the A/B testing methods from the “Empirical Study” section).

Further, Underwood (2012) presented a method for building students’ profiles based on identification of their knowledge gaps and recommending the next learning activities for the students based on these profiles. These next learning activities focus on enhancing the student’s knowledge rather than on taking remedial actions of recommending additional supplementary materials in order to fill the knowledge gaps, as is done in our work. Zaldivar et al. (2012) describe the MetaMender system which uses the description of meta-rules written by the domain experts in order to personalize learning materials to be presented to the learner. In contrast to that paper, our approach does not rely on user-specified rules and works automatically in a scalable manner for a large number of courses by using machine-learning methods.

In addition to Underwood, the idea of recommending the next learning activity has been explored by Klasnja-Milicevic et al. (2011) who present an adaptive learning algorithm for their programming tutoring system. In particular, the proposed method analyzes the learning materials previously selected by a course instructor and identifies which of them fit students the most in terms of (1) their learning profile obtained from prior student performance and (2) their learning style, and recommends these materials to the students. The authors also conducted a controlled experiment and demonstrated that their approach outperforms the control group in terms of time taken to complete a lesson and also in the number of covered lessons per unit of time. The method proposed by Klasnja-Milicevic et al. uses extensive knowledge about one particular subject obtained from experts and delivered to students via the tutoring system (that is also built manually to a large extent) and, therefore, is not scalable to many courses, as is our method. Also, Klasnja-Milicevic et al. use a modified version of user-based collaborative filtering, whereas we propose a “filling-the-learning-gaps” approach that is very different.

Learning materials recommendation methods were also explored in the industry. In particular, Khan Academy, similarly to Underwood, recommends the next learning activity to students based on information about their performance in the course (Murphy et al. 2014). This information is obtained by evaluating a student’s performance on a range of topics in a particular course that are arranged into a “knowledge map” of the course, which was constructed manually by a Khan Academy content manager. Furthermore, collecting recommended materials and associating them with the topic is also performed manually by the Academy’s content managers. In contrast to the Khan Academy approach, we focus on the identification and closure of the knowledge gaps in a student’s education, rather than on enhancing the student’s knowledge by recommending the next topic to learn. Also, unlike Khan Academy, we automated our recommendation methods by eliminating human work from the recommendation process, thus making our approach scalable to a larger number of courses.

In addition to Khan Academy, other industrial-strength recommendation engines have been developed in educational settings by Coursera and Knewton. However, Coursera recommends only courses to the students that might be of interest to them and, therefore, does not provide recommendations of remedial learning materials to students taking its courses. Knewton determines what each student knows and how that student learns best in a way that is similar to the Khan Academy approach (Wilson and Nichols 2015). After learning this information, Knewton recommends the next learning activity in order to advance the student’s knowledge of the subject matter in a way similar to Khan Academy. Similarly to Khan, Knewton constructs the knowledge map of the course using the domain knowledge of an expert, which is different from the way we do it in our project (see the following section for details).

In summary, although prior work on recommending learning materials to students in the TEL environment exists, there have been only few prior methods that identify the gaps in a student’s knowledge of the subject matter of the course and that also try to close those gaps. Most of the methods that propose specific algorithms of how to close these gaps take the more forward-looking, proactive approach of recommending the next learning activity rather than taking a defensive filling-the-gap reactive approach advocated in this paper. Also, the prior methods rely extensively on the manual approach of providing various types of learning materials and developing building blocks of the recommendation methods, which makes the proposed methods less scalable. In contrast, we have automated our method and made it scalable. In the next section, we describe our gap learning method and the corresponding filling-the-gap algorithm that looks at the prior historical information for a student taking a course, identifies possible learning problems based on this history, and reactively tries to remedy these problems by recommending additional supplementary learning materials in order to close those gaps.

## Filling-the-Gap Recommendation Method

In order to provide filling-the-gap recommendations to students taking a course, it is first necessary to assemble the library of learning materials to be used for recommendation purposes. It is also necessary to construct the learning structure of the course and identify various topics covered in it. After these two steps, we identify the gaps in students’ performance in the course and recommend remedial learning materials in order to fill-in these knowledge gaps. All of this suggests the following stages of the filling-the-gap recommendation process:

• Building the knowledge structure of the course

• Building the library of the remedial learning materials for the course

• Matching learning materials with the course topics

• Matching the test questions used in the course quizzes with the course topics

• Building students’ learning profiles for the course

• Identification of students’ knowledge gaps in the course

Preparing and providing recommendations of additional learning materials to underperforming students in order to close their knowledge gaps in the course

The rest of this section describes each of the stages of this filling-the-gap recommendation method

## Stage One: Building the Knowledge Structure of a Course

For each course in a curriculum, we build a taxonomy of the topics covered in that course. This taxonomy forms the knowledge structure of the course that organizes the knowledge that the students acquire in it. For example, Figure 1 shows a part of the Art History course taxonomy where each node represents a topic covered in the course.

Each topic node in the taxonomy has a set of obligatory reading materials that were selected by the instructor and assigned to that topic. The root of the course taxonomy represents the course as a whole. It also contains all of the obligatory reading materials assigned to the course.

In this project, we automatically built the course taxonomy from the syllabus, the weekly learning objectives, and the list of weekly reading materials provided by the instructor using information extraction and text mining methods. The specifics of this process that were used in our empirical study are explained in subsection “Providing Recommendations.” The online university with which we have worked has a very precise and well-developed course structure consisting of 8 weeks of learning sessions. Each week is associated with one particular topic and a set of reading materials assigned by the instructors for that week. Therefore, we were able to learn the course taxonomy automatically from the syllabus and other course resources. In cases when the reading materials did not appear explicitly in the class assignments for a particular week, they could have been learned and constructed from the course syllabus.

![](/api/attachments/58VTMAYA/fulltext/images/0f5fb692593388a835c19f707ff8110a006794509e3a584ac0dc2d5692be7def.jpg)  
Figure 1. Art History Course Taxonomy

However, in those learning applications where the course taxonomy cannot be directly extracted from the course syllabi (as we did in our empirical study as described in the subsection “Providing Recommendations”), this taxonomy can be automatically learned though various machine learning and text mining techniques, such as the ones described in Acharya and Sinha (2015), Chica et al. (2008), and Olney (2010). In particular, there is a body of work on extracting concept maps from educational text documents that can serve as the structure of the body of knowledge of a particular subject, such as presented in Olney (2010), Villalon and Calvo (2011), and Zubrinic (2012). Further, Zouaq and Nkambou (2008) describe how educational domain ontologies can be learned from course text materials. Similarly, in applications where the assignment of reading materials to the topic are not as straightforward as in our case, they can be learned from the data using the techniques described in Sujatha and Bandaru (2011). Still another approach to building the course structure would be hierarchical variations of the well-known LDA method, such as the one presented in Blei et al. (2010). Furthermore, this type of work is generalizable to other courses and educational settings, including our online university and beyond. In this paper, we have focused on using the taxonomy extraction method (and have not applied the machine learning methods reported in all of this prior work) because we can produce taxonomies for the structures of the courses in our online university really well by extracting them from the syllabi and the study guides that are already available for our courses, as explained above. Therefore, there is no need to apply the taxonomy learning methods reported in Zouaq and Nkambou or Chica et al. in our case.

Regardless of the way the taxonomy is obtained, automati cally or using the methods described in the previous paragraph, the taxonomies of the courses in our project consist of a tree of topics and subtopics, as shown in Figure 1. The leaves of the tree (shaded in Figure 1) constitute the smallest topics which are not further divisible, and usually correspond to only one piece of the reading material associated with the topic (e.g., a particular web-page, a chapter or a section of a book, an article, etc.). The taxonomy tree does not have to be balanced. In practice, however, it usually has a depth of three or four layers, depending on the nature of a particular course.

## Stage Two: Building the Library of Remedial Learning Materials

In this stage, we build the library of the course related reading materials that go beyond the set of obligatory reading materials assigned by the course instructor. These additional reading materials include popular textbooks, online articles, web pages, online videos, and other online materials that are related to the course. Each document in this library can have its own taxonomy that is based on the document's table of contents. For example, a textbook is divided into chapters, sections, and subsections that can be recommended as separate units. In contrast, some other documents, such as short articles, may not have any document structure and are recommended as the whole unit since they are not divisible into smaller pieces.

This library can be build from the open online sources using the following steps:

1. Identify key concepts for each topic in the course taxonomy by using the TF-IDF method as follows. For each topic in the course taxonomy, we have a text of obligatory reading materials for this topic. Based on this text and the corpus of Wikipedia articles, we calculate TF-IDF for each term in the text.<sup>2</sup> In addition to individual terms, we also apply the same method to the frequently occurring (e.g., top n) pairs and triples of terms. The sets of terms with high TF-IDF values (e.g., top n) form the set of key concepts of the course.

2. Find relevant reading materials on the Web for the key concepts identified in Step 1. In particular, for each concept (keyword), we launch a search query with this concept on the Web. For each search query, we collect the first n results returned by the search engine, including the links and the actual returned documents. In our study, we used Google as a search engine and set n = 10. As a result, we collect a (large) list of returned documents.

3. For each document returned in Step 2, check the relevance of this document and eliminate the irrelevant documents. In particular, we assume that if a document is relevant to the course, it should contain more than one key concept from the list produced in Step 1. Therefore we eliminate from the library those documents that appeared only once in all of the search results (and hence contain only one key concept from the list of all concepts).

In addition to deploying standard text mining techniques, it may also be feasible to use the popular LDA approach (Blei et ak, 2003) in order to identify the key concepts for the course. In particular, the LDA topic modeling approach can be applied to all the texts assigned to the leaf topics in the course taxonomy and would generate many words that are frequent not only in the course materials but also in all other documents at large. However, LDA may miss some of the infrequent words that are still important for a particular course. Another way to apply LDA to the corpus of documents would be by ignoring those terms that have low TF-IDF measures in order to detect pairs and triples of important words constituting one concept. Although feasible, this approach would not extend the set of important pairs and triples identified by our TF-IDF method and would also miss the pairs and triples of words with low TF-IDF numbers. As a result, we decided to use the TF-IDF method (rather than LDA) in this work.

Note that there could be some variations for the methods of building the library of remedial learning materials from the open sources using the described search engine approach. For example, Agrawal et al. (2010) followed a similar approach and showed that their method is able to automatically enrich a textbook with a suitable number of links to related web content. Although different in specific details, our method and the one presented in Agrawal et al. have the following steps in common: (1) finding the key concepts for the topics in the course taxonomy; (2) searching for these key concepts online; and (3) cleaning the retrieved results. These three steps define the essence of the library building method described in this section.

Finally, the proposed method is scalable and can be applied to many courses offered by a university. In our study described in the “Empirical Study” section, we have easily applied the method to 42 courses. In practice, it can be scaled to hundreds of such courses because it is linear in the number of them.

## Stage Three: Matching Learning Materials with the Course Topics

In this stage, we establish the relations between the learning materials from the library L built in the previous stage and the course taxonomy constructed in the first stage as follows. For each topic in the course taxonomy, we identify the best matching set of “units of knowledge” from the library (e.g., a book chapter, a Web page, or an article), thus establishing the links between the topic in the course taxonomy and the corresponding reading materials from the library. We do this identification by using the TF-IDF-based measure of correspondence between the unit of knowledge in the library and the text associated with the topic, as described earlier. Specifically, each topic in the course taxonomy is represented as a vector of the TF-IDF measures in the space of the key concepts $\{ c _ { 1 } , ~ . . . , ~ c _ { n } \}$ for the course, as described in the previous stage; that is, $V ( T ) = ( t f \_ i d f _ { \scriptscriptstyle T } ( c _ { \scriptscriptstyle 1 } ) , \ . . . , \ t f \_ i d f _ { \scriptscriptstyle T } ( c _ { \scriptscriptstyle n } ) )$ where the tf\_idf (c ) is the TF-IDF measure of the concept c computed based on the text associated with the course topic T and the corpus of Wikipedia articles. We also represent each unit of knowledge, U, from the library in the same way as $V ( U ) = ( t f \_ i d f _ { U } ( c _ { 1 ) , \dots , } t f \_ i d f _ { U } ( c _ { n } ) )$

Then for each topic T in the course taxonomy and for each source of materials S 0 L consisting of a set of units of knowledge belonging to the same location (such as a website) or logically combined into one group (such as chapters in a book or articles in a special issue of a journal), we define similarity between T and S as the highest cosine similarity between the course topic’s vector $V ( T )$ and the subset of units of knowledge from this source $( X \subset S )$ among all subsets of these units,<sup>3</sup> that is,

$$
\text { Similarity } (S, T) = \max _ {X \subset S} \left(\cos \left(V \left(\bigcup_ {U _ {i} \in X} U _ {i}\right), V (T)\right)\right)\tag{1}
$$

For example, if a book has 15 chapters, we select the subset of the chapters that has the highest similarity matching score with the course topic T. The problem of identifying such subset X that maximizes criterion (1) can be formulated as a mixed integer nonlinear programming (MINLP) problem (see Appendix A for details), which is known to be NP-hard (Lee and Leyffer 2012). Since the general optimization problem is NP-hard, we find such similarity maximizing subset X using the following heuristic search among the subsets of the units of knowledge S.

For each leaf node in the course structure taxonomy, we select the most relevant subset of the units of knowledge from the source of knowledge S (such as a website with multiple pages or a book with several chapters) that is limited to only one or two units. For each internal node in the taxonomy, we take the union of all the units of knowledge assigned to its children. Note that we limit the number of units from one source that can be assigned to a leaf node to two units for the following reasons. First, as discussed in the first stage, we assume that the leaf topics in the course taxonomy and the units of knowledge in the source of materials represent a small and indivisible piece of knowledge and, therefore, they have a one-to-one match in most cases. We actually experimented with setting this constraint to three units of knowledge and found that in about 75% of the cases, leaf topics match to only one unit of knowledge; in about 20% of the cases, they match to two units of knowledge; and in less than 10% of the cases, the most relevant subset contains three units of knowledge. Since three or more units happen in less than 10% of all the cases, we decided to limit the knowledge subset to only one and two units. The second reason for limiting the maximal number of units that can be assigned to a leaf node is that we do want to limit the number of materials recommended to the student in order not to overwhelm him or her with too much information. Having this natural limit on the size of best matching subset of units from one source, the problem of identifying this subset can be solved in polynomial time.

In this study we proposed our own heuristic (as described above), as opposed to relying on the prior approaches, such as the ones presented in Binshtok (2007) and Guo (2009), because we really need to limit the number of recommended materials due to the nature of our problem and for the reasons explained above (note that these prior heuristics do not have this constraint, have different performance objectives, and usually produce many more alternatives). Note that our heuristic does not guarantee finding the best matching subset of items in the source. However, for the leaf topics of the course taxonomy, it guarantees finding the best set of items consisting of one or two elements, which is enough for our particular problem having natural constraints of limiting the number of leaf units to a very small set, as explained above (i.e., we do not want to overload the students with too much information). The situation is more complex for the interior nodes where our heuristic does not necessarily find the best matching subset of items from the source. However, the comparison analysis with the optimal MINLP approach (presented in Appendix A) showed our heuristic not only works faster (in polynomial time), but also finds the near optimal solution (i.e., identifies the most relevant subset of units of knowledge from the source in most of the cases and almost the best matching subsets in the remaining ones).

As a result of applying the proposed heuristic, we obtain the subset of the units of knowledge from S that represents topic T in the best possible way for each topic T and source S by maximizing criterion (1) among all subsets containing one or two elements.

Furthermore, for each topic node T from the course taxonomy, we identify source of knowledge S with the highest similarity to topic T in terms of equation (1) among all the library sources $S \in L .$ . Finally, we establish the link from topic T to $U n i t s ( S _ { T } , T )$ , that is, the subset of units from source $S _ { T }$ that constitutes the most matching reading materials from $S _ { T }$ to topic T. Thus, the subset of units of knowledge $S _ { T }$ fits topic T in the best way across the entire library $L .$ For example, our algorithm may match topic “Renaissance in Italy” with several pages from site “arthistory.about.com.”

Note that our similarity measure presented in equation (1) is based on the standard cosine similarity. We actually experimented with other textual similarity measures, such as Euclidian Distance, Pearson correlation, and Jaccard coefficient. These textual similarity measures were compared in prior literature, such as Huang (2008) and Strehl et al. (2000), and it was shown that their performance was comparable across different problems and different datasets.

We compared these textual similarity measures in our case and found that, although they produce different ranking of the materials relevant to the topics, they identify the same material as the most “relevant” to the course topics in most of the cases. Since we use only the materials that are the most relevant for the topic based on one of these measures in our study, we maintain that comparing the four performance measures in terms of the most relevant materials (vis-à-vis their ranking) is the most appropriate approach in our case. Since the four metrics produced similar performance results, this means that they are good substitutes for each other. Therefore, we selected the Cosine similarity measure as a representative example of the measures and refer to it throughout the rest of the paper.

Our algorithm for processing this step doesn’t involve any user input and, therefore, is automatic. Valerio et al. (2007) and Kokkodis et al. (2014) present other algorithms performing similar tasks. However, Kokkodis et al. focus on matching videos and Valerio et al. focus on matching documents with knowledge map concept models.

The only way to do comparisons between different types of matching algorithms is to conduct additional experiments and to show that the approaches, such as presented by Valerio et al. and others, actually work better in the sense that they produce recommendations leading to better performance results for the students. This is the case because several alternative algorithms may produce different sets of reading materials, and the only way to compare which materials are more helpful for students is to actually recommend them and see which ones really improve students’ performance and by how much. In our experimental settings, we decided against doing the experimental comparisons of our proposed materials matching algorithm with other approaches because (1) we expected it to produce very marginal performance improvements (if any) and (2) we did not have enough students to produce additional experiments that might show significant results. Also, we used our own method (described in this section) in this paper because it fits better our paradigm of recommending learning materials using the course taxonomy topics with the reading materials assigned to them.

## Stage Four: Matching Test Questions with the Course Topics

Each course has one or several tests consisting of the set of test questions. For each test question, we determine the set of leaf topics in the course taxonomy for which this test question corresponds as follows. We (1) represent test question q as a vector based on the text of the question using the same TF-IDF methodology as for the course taxonomy nodes $V _ { q } =$ $( t f \_ i d f _ { q } ( c _ { 1 } ) , \ldots , t f \_ i d f _ { q } ( c _ { n } ) )$ (see the previous subsection for specifics); (2) compute similarity measure ρ between question $T \mathrm { s }$ vector $V _ { q }$ and all of the leaf topic $T _ { i } ^ { \ast } \mathbf { s }$ vectors $V _ { T _ { i } }$ ; in our study, we used the cosine similarity measure for ρ (i.e., ρ(q, $T _ { i } ) = c o s ( V _ { q } , \ V _ { T _ { i } } \ ) )$ , but it can also be any other similarity measure, such as Pearson correlation; and (3) define a match between the question and the topic when the similarity measure between the two exceeds a certain threshold.<sup>4</sup> For example, question “The Rococo style began in (Italy/ Flanders/France/Spain), at the end of the reign of Louis XIV” matches topic Rococo because it contains concept “Rococo.”

As a result, we obtain the bipartite graph of relations between the course topics and the quiz questions that appeared on all the tests of that course. Note that this is a many-to-many relation, as Figure 2 demonstrates (i.e., a quiz question can cover several course topics and a course topic can appear in several test questions). Then for each leaf topic $T _ { i }$ from the course taxonomy, we determine the corresponding list of questions Q matching the topic in the bipartite graph.

This step is fully automated and fits well into the overall recommendation framework, as our experiments described in the subsection “Providing Recommendations” show. However, we have presented only one particular method of establishing correspondence between the course topics and the quiz questions, and some other alternative approaches are also feasible. For example, Desmarais (2011) addresses the same problem using a matrix factorization (MF) technique. However, Desmarias’s method is used for establishing correspondence between the test questions and the set of “skills” (that are very similar to our “topics”), where the set of skills (topics) is defined by the set of latent features that are identified using the MF approach. In contrast, the set of topics is explicitly defined in our case, as explained in the first stage and, therefore, is not latent. Furthermore, since we focus on recommendations of new materials, it is important for the set of topics to be explicitly defined (vis-à-vis being latent), so that we can clearly explain to the student into which specific course topics the recommended learning materials fit. This means that the MF method is less applicable to our case because it deals with the latent set of topics, and our method relies on the explicitly defined topics, as explained above.

Feng et al. (2009) present a tutoring system where teachers were asked to tag each question with one or several skills. Although this handcrafted approach is applicable as a part of our method, it requires involvement of a domain expert. In contrast to this work, we automated our approach. To validate how our automated “quiz questions” to “course topics” matching approach worked in our application, we manually checked its performance for 5 (out of 42) courses and found the discovered relations to be accurately constructed.

![](/api/attachments/58VTMAYA/fulltext/images/9bfa98fa8ba7821eca8addfb7802637dcf35add59f9ff571d32a4cc8af63aa02.jpg)  
Figure 2. Topic–Question Correspondence

## Stage Five: Building Student’s Profile

For each student and a course offering we determine how well the student understood all the leaf topics specified in the course taxonomy by analyzing the student’s performance in that course and calculating a certain performance score for each leaf topic in the course taxonomy. Although this score can be computed in many different ways, we propose to do it by calculating the weighted ratio of the correct answers to the list of questions pertaining to this topic, such as the ones provided on a test (based on the bipartite graph of topics and questions defined by relationship ρ and described in the previous stage). More formally, we compute the performance score of student S on topic T based on the set of related questions Q as follows:

$$
\text { Performance } (S, T) = \frac {\sum_ {q \in Q} \rho (q , T) * A _ {q} ^ {S}}{\sum_ {q \in Q} \rho (q , T)}
$$

where

$$
A _ {q} ^ {S} = \left\{ \begin{array}{l} 1, \text { if   student   S   answered   question   q   correctly } \\ 0, \text { otherwise } \end{array} \right.
$$

For example, if there are 10 questions in the test corresponding to the topic Rococo in the Art History example with equal weights for each question, and Joe answered 9 of them correctly, then Joe's score for this topic is 0.9, which means that Joe understood the topic Rococo well. In contrast, if John answered only 5 questions correctly, his score for the topic Rococo would only be 0.5, which means that he did not master this topic properly.

## Stage Six: Knowledge Gaps Identification

After we determine students’ performance scores for each leaf topic in the course taxonomy, we identify their knowledge gaps (i.e., those topics in which they performed poorly). In particular, we examine the performance scores that a student received in the leaf topics and claim that the student has a knowledge gap in a topic if either

(1) his/her performance score in this topic is low (i.e., below a certain threshold level), or

(2) he/she has knowledge gaps in a “sufficient” number of subtopics (e.g., more than 66%) of that topic, and therefore needs remedial actions for these subtopics.

We determine the above threshold level as the median of the scores in this topic taken over all the students in the class. Further, if a student has a sufficient number of knowledge gaps among all the subtopics of a topic (at least two-thirds), then we aggregate these knowledge gaps to the whole parent topic. Referring to Figure 1, if Joe has a knowledge gap in topics “Rococo” and “Renaissance in Italy,” we’ll claim that Joe’s knowledge in the whole topic “Revival and Rebirth in Europe” is poor and identify it as a knowledge gap.

## Stage Seven: Preparing and Providing Recommendations

Given the structure of a course (as specified in the first stage), the identified gaps in student knowledge in the class (as determined in the previous stage), and the links between the topics in the course taxonomy and the supplemental reading materials from the library (as determined in the third stage), we next provide recommendations of the supplementary reading materials to the students in order to close these knowledge gaps. In particular, for each knowledge gap topic node in the course taxonomy, we recommend to the student those supplementary reading materials that are linked to that node as described in the third stage. Note that these recommendations are personalized to the individual students since different students have different knowledge gaps. Still, in case of two students having the same set of knowledge gaps, they will receive the same set of recommended materials.

It is also important to note that if a student has a knowledge gap in some topic that has subtopics in the course taxonomy, we will provide recommendations for this topic but will not provide separate recommendations for any of its subtopics. For example, if Joe has knowledge gaps in topics “Rococo”

and “Renaissance in Italy” and, therefore, in topic “Revival and Rebirth in Europe” (see Art History taxonomy in Figure 1), then he will receive recommendations only for the entire topic “Revival and Rebirth in Europe.”

Although there are no prespecified limits on the number of recommended materials to a student, in practice it is limited based on the following considerations: (1) the number of gaps that a student has cannot exceed the number of topics in the course taxonomy, and (2) only one material is recommended for each gap by our method. Therefore, the number of recommended materials per course cannot exceed the number of topics in the course taxonomy. Furthermore, if we have too many gaps in the subtopics of a particular topic, we conclude that the student has a gap in the parent topic itself (using certain decision rules described earlier in the paper). As a result, we recommend the remedial material for the parent topic (vis-à-vis several materials for its children), thus reducing the number of recommended materials for the course even further. As we experienced in practice, the lists of recommendations are usually no longer than 10 materials even for the worst performing students in the class.

## Empirical Study

We conducted a field study with participation by students from a major online university, that was accredited by the Distance Education Accrediting Commission (DEAC), over a period of three semesters, where each semester consists of 9 weeks, 8 of which are dedicated to the studies and the last week to the final exams. Each course in this university is worth three credits. In the rest of this section, we describe the structure and nature of the course offerings, the data that we collected during the study, and the other details of the experimental setup.

## Data

A total of 910 students of the university participated in our experiment. These students have taken courses in Computers Science (CS), Business Administration (BA) and General Studies (GS), such as Mathematics, English, Psychology, Art History, etc. Overall, the university offered 13 different types of CS courses, 18 types of BA courses, and 11 types of GS courses during these three semesters.

Each course has a syllabus and a set of learning materials selected by the instructor and assigned to the course. Furthermore, each week of studies in the course constitutes one structured unit of learning, thus the whole 8-week course is partitioned into eight well-defined learning units. In other words, each week is carefully structured in terms of the studying process at that university and consists of (1) a set of obligatory reading materials, assigned to all the students for the week, (2) various assignments provided to the students for the week, (3) questions to be discussed on the discussion forums, and (4) a self-testing quiz that does not contribute to the overall grade for the course. There are also two graded quizzes administered by the university during the semester that contribute to the final grade for the course. The final exam is open book, and it is given online at the end of the semester during week 9. The unit of analysis in our study is the student/course pair specifying a course that a student takes during a particular semester. Overall, we collected data on 1,512 student/course pairs throughout three semesters covered in our study.

To validate our method described in the previous section, we conducted the following experiment (the so-called A/B test) that observed students’ performance in the set of courses that they have been taking and provided recommendations to them according to this method. Within each course we randomly split the student/course pairs into the following three groups in order to provide different types of recommendations to them and to compare their performance results:

• The control group to whom we did not provide any recommendations in the course.

The nonpersonalized recommendations group consisting of the students who received “generic” (nonpersonalized) recommendations sent to everybody in that group. Therefore, all students in this group received the same set of recommendations as the falling-behind students in the personalized group who failed all of their tests and thus needed help in all of the topics of the course.

The personalized recommendations group consisting of the student/course pairs to whom we provided recommendations based on the method described in the previous section.

Furthermore, we divide all of the students into the following three groups: excellent, good, and falling behind students based on the average grade that they received across all previously taken courses. In particular, we define the good students as those whose GPA in all the previously taken courses lies between 70 and 90, excellent students as those whose GPA is above 90, and falling behind students as those whose GPA is below 70. Note that it is a natural division that usually corresponds to the standard classifications of students into A, B, C, and D/F students adopted by many universities (excellent being A students, good being B and C students, and falling behind being D and F students in our case). We use this classification in the “Results” section to compare the performance of personalized, nonpersonalized and control groups across the good, excellent, and falling behind students on the final exams.

## Providing Recommendations

The online university that we use in our experiment uses Moodle (moodle.org) as its learning management platform (LMS). Therefore, in order to provide recommendations to the students, we build a module that communicates with the Moodle database.

As the first step, we build the taxonomy of the courses based on the information provided by course instructors. Each course in this university has a syllabus and a set of assignments for each week of studies that include learning objectives and the corresponding reading materials. Our script collects all of this data from the Moodle database and organizes it into a taxonomy structure, as described in stage one. Therefore, most of the courses have taxonomies consisting of a root representing the entire course, eight nodes on the second level (one node for each week of the studies), and two or three child nodes at the third level specifying either the learning objective(s) for the week or the obligatorily assigned reading materials for the week.

In the second step of our method we used Google API in order to find web content that is relevant to the course materials, as described in the second stage, and add it into the course materials library. We next matched the units of knowledge from our library with the topics in the course taxonomy based on the method described in the third stage. To build the student knowledge profiles and to compute their performance scores, we used the data of weekly and graded quizzes.

We provided recommendations to the students in personalized and nonpersonalized groups by sending them e-mails with the lists of links to the recommended materials. These e-mails were generated automatically by our software that imbedded links to the recommended reading materials into the standard e-mail template we produced. As an example, a copy of the recommendation letter is presented in Appendix B. Further, the links were configured to go through our server in order to find out which students actually opened recommended materials.

Recommendations to the second and the third experimental groups were provided up to three times per semester. The first recommendation of supplementary reading materials was produced shortly before the students took graded Quiz 1 in the third week of studies and addressed the knowledge gaps in the student’s performance on weekly quizzes conducted during weeks 1 and 2. The second recommendation was provided before the students took graded Quiz 2 in the sixth week of studies addressing the knowledge gaps identified through weekly quizzes during weeks 3–5. Finally, the last recommendation was provided shortly before the students took the final exam at the end of the semester, addressing the knowledge gaps identified through the course quizzes.

The number of recommended materials for the nonpersonalized group of students is equal to the number of high-level course topics covered by the graded quiz (see stage seven), that is, in preparation for the final exam they received eight recommended materials, each material corresponding to one week of their studies.

## Performance Measures

The goal of our experiments is to show that personalized recommendations lead to better performance results in the course. Therefore, we compare the performance results of the personalized, nonpersonalized, and control groups across the good, falling behind, and excellent students on the final exams (as explained in the “Data” subsection) in terms of the measures defined below.

Each course in our experiment has the final exam in the form of a quiz that includes questions covering most of the topics from the course. Since our methodology of filling-the-gap recommendations helps the students to master poorly performed topics and therefore should lead to better performance in the course, it is natural to use student’s (absolute) performance on the final exam as a performance measure for our methodology. Since there are 42 different courses in our study and each one of them has its own specifics and unique distribution of grades on the final exam, another good performance measure is the normalized grade on the final exam, where normalization is done by subtracting the average grade from the student’s grade and dividing it by the standard deviation for all the students in the course.

Another good performance measure is the improvement of student’s performance in the current course vis-à-vis his/her performance in the previous courses. The “previous courses” can be the last course, the last two courses, or all previous courses, either taken across all the subjects or within the same subject area as the current course (e.g., within Computer Science, Business, or Mathematics) (we decided to focus on Mathematics courses as opposed to all General Studies courses because they are more uniform and it is hard to compare GS across all subjects). Furthermore, we also use this same student improvement performance measure, but in the normalized (versus absolute) form, as explained above.

## Survey

In addition, at the end of each semester we also sent a survey to those students who have received at least one recommendation during the entire semester. The purpose of the survey is to see how well they perceived our recommendations and also to detect possible biases and problems with the experimentation. In particular, we asked the students in the survey how much time they spent studying recommended materials, how much they liked our recommendations, that is, what was their overall impression of our recommendations (as opposed to the individual recommendations, as is normally done in recommender systems), and several other questions that are presented in the Appendix C.

## Results

We produced two types of results in our experimental study: the first one is related to the survey described in the “Survey” subsection above, and the second one to the performance results of the students in the courses they took that are characterized by the measures described in the “Performance Measures” subsection.

## Survey Results

As explained in “Survey” subsection, we sent a survey to the students at the end of each semester. In particular, it was sent 653 times to the students over the period of three semesters, 393 times students started the survey, and 344 times they finished the survey. Furthermore, one of the questions in the survey was whether or not students recall receiving recommendations during the semester, and it turned out that 332 students indeed recalled receiving recommendations while 61 did not. Note that some of the students who recall receiving recommendations actually didn’t finish the survey. As a result, we ended up with a response pool of 283 responses to the survey from those students in the personalized and nonpersonalized groups who recalled receiving at least one recommendation during the semester and who have completed the survey.

As the results of our survey show, 81% of the students in the response pool regularly spent at least 5 hours per week on average studying for the courses they take. This means that most of the students in the personalized and nonpersonalized groups who recalled receiving at least one recommendation during the semester and who have completed the survey take their online education seriously and study diligently in their courses.

Furthermore, as Figure 3 shows, the students responding to our survey took our recommendations seriously and studied the recommended extra reading materials diligently, especially when preparing for the final exam (i.e., 58% studied at least 2 hours). Note that this is not the total amount of time it takes the student to prepare for the final exam but an incremental time reading extra materials.

Moreover, as Figure 4 demonstrates, a significant majority of the students in the personalized and nonpersonalized groups who recalled receiving at least one recommendation during the semester and who have completed the survey, liked our recommendations. In particular, 87% of students agree (or even strongly agree) that the recommended materials were relevant for the course, 85% of the students agree that recommended materials were helpful in their studies, 78% of the students learned new things from additional materials, and 80% of the students would like to recommend our recommendation tool to their friends.

Ideally, we would like to incorporate these student responses, including preparation time, gender, age, and other similar variables capturing these responses, into the analysis of student performance, as presented in the following subsection. Unfortunately, it is hard to accomplish this for the following reasons. First, the control group and the best students from the personalized group did not participate in the survey. Also, only 35% of those students who received the survey, indeed, responded to it. Therefore, there are significant biases in the population of students who responded to our survey, which makes it inappropriate to compare the experimental groups based on the survey data. Despite all of these points, we nevertheless analyzed the survey data to see how various types of survey variables affect student performance on the final exam. The results of this comparison are presented in Appendix D, and they show that there are no significant differences except in a few of cases.

In summary, our survey shows that students liked our recommendations. Also further analysis of survey data is inappropriate due to various biases in that data. Finally, the more appropriate analysis of student performance on the final exams (as opposed to survey data) will be presented in the following subsection, where we explore whether our recommendations are more effective (and not only liked and considered useful by the students, as demonstrated in this section).

## Student Performance Results

We compare performance results of the students on the final exam for the control, personalized and nonpersonalized groups across various experimental settings and measures. As described in the “Performance Measures” subsection, we measure student performances on the final exam in absolute (i.e., the raw score) and normalized (the normalized score) terms. We also compare the student’s performance in a course versus his/her performance in the previously taken course(s) where no recommendations were provided, as explained in the “Performance Measures” subsection. Also, we do this comparison for the cases when the previously taken courses were taken (1) in all of the subjects offered at the university and (2) in the same subject area as the given course. Finally, as explained in the “Empirical Study” section, we compare the performance of the excellent, good, and falling behind students across the personalized, nonpersonalized and control groups in terms of the performance measures described in the “Performance Measures” subsection.

![](/api/attachments/58VTMAYA/fulltext/images/dd0a89c5832751d7e91f6776ff9c5ba4a6816a4a1e28aa323c04bbc94f396da0.jpg)  
Figure 3. Time of Studying Recommended Materials

![](/api/attachments/58VTMAYA/fulltext/images/1460451870ce7d7a9bd85c67eec902882a60d55184af020fe8ecbb57436b5a50.jpg)  
Figure 4. How Students Like Our Recommendations

As Table 1 shows, the numbers of students who completed the final exam in all of the courses they take in our study are 295, 363, and 376 for the control, nonpersonalized, and personalized groups, respectively. Also, the number of students in all of the courses who follow our recommendations are 138 and 101 for the nonpersonalized and personalized groups, respectively. Note that, unlike as it appears in Table 1, the conversion rates are approximately the same for the personalized and nonpersonalized groups for the following reason. According to our approach, not all students in the personalized group have actually received recommendations (i.e., only 252 out of 376 students). Therefore, the percentages of the students in the personalized and nonpersonalized groups that followed our recommendations are 101/252 = 40% and 138/363=38%, respectively. Further, our study shows that there are no statistically significant differences across control, nonpersonalized, and personalized groups for all of the previous performance metrics for various groups of previous courses presented in the “Performance Measures” subsection. For example, rows (3)–(5) in the first column of Table 1 present three of these metrics, and Table 1 shows that there are insignificant differences among them across the three columns.

We next compare the performance of the three experimental groups. In particular, Figure 5 shows the comparison in grade

<table><tr><td colspan="4">Table 1. Experimental Groups Statistics</td></tr><tr><td>Experimental Group</td><td>Control</td><td>Nonpersonalized</td><td>Personalized</td></tr><tr><td>Number of (student, course) pairs</td><td>295</td><td>363</td><td>376</td></tr><tr><td>Number of (student, course) pairs who followed the recommendations</td><td>-</td><td>138</td><td>101</td></tr><tr><td>Average previous performance</td><td>83.17</td><td>83.29</td><td>83.13</td></tr><tr><td>Performance in the last taken course</td><td>80.79</td><td>81.24</td><td>80.72</td></tr><tr><td>Performance in the last taken course in the same subject</td><td>79.49</td><td>80.79</td><td>80.03</td></tr></table>

Table 2. Numbers of Students in Excellent, Good, and Falling Behind Subgroups

<table><tr><td>Experimental Group</td><td>Control</td><td>Nonpersonalized</td><td>Personalized</td></tr><tr><td>Number of “excellent” students</td><td>58</td><td>92</td><td>82</td></tr><tr><td>Number of “good” students</td><td>206</td><td>245</td><td>272</td></tr><tr><td>Number of “falling behind” students</td><td>31</td><td>26</td><td>22</td></tr></table>

![](/api/attachments/58VTMAYA/fulltext/images/3a0c2c2fd0e57f560651f67eb3893f229dfe16532201d739b720c91a16e734e2.jpg)

Figure 5. Histogram of Grade Improvement by Average Previous Grade

improvements across the three groups for the students having average performances on all previously taken courses ranging from 55 to 100 points (as shown on the X axis). As Figure 5 shows, performance improvements for personalized recommendations are higher across all of the types of good students (ranges 70–75, 75–80, 80–85, and 85–90) in comparison to the control and the nonpersonalized groups. Furthermore, for all of the good students (ranges 70–90), the performance improvement for the personalized group is significantly better than for the control group. Note that such students constitute about 70% of the total number of students, as is shown in Figure 6 and Table 2.

For the falling behind students, we observe larger values of the grade improvements than for the good students. We believe that this is the case because these students have no choice but to improve their performance if they indeed want to continue their studies and not drop out of the program. Furthermore, the number of such poorly performing students is really small, as is demonstrated Figure 6 and Table 2 (i.e., there are fewer than 15 students in each of the three experimental groups and in each bin of the Figure 5). Therefore, these performance differences are statistically insignificant and are highly inconclusive.

![](/api/attachments/58VTMAYA/fulltext/images/b59232dee8ca704c13136cabb0718650712a48b5116133f0674542416a6ed25b.jpg)  
Figure 6. Histogram of Students by Average Previous Grade

Further, note that the average performance improvements are noticeably lower for the excellent than for the good students. One plausible reason for that could be that no one in the excellent group can really improve his or her performance because there is an upper bound of 100 on this performance, while some of the excellent students lose their performance, thus decreasing the average scores for the group. Another possible explanation is that the earlier classes are quite basic (such as introduction to programming), while subsequent courses became more challenging, and many excellent students could not mentally adjust to this gap.

Moreover, for the falling-behind and the excellent students, the comparison between the personalized and the other groups are not statistically significant. One of the reasons for this is that these two groups are quite small: as Figure 6 and Table 2 show, falling-behind students constitute 7% and excellent students constitute 22% of the students. Another reason why personalized recommendations have no effects on excellent students is because our system seldom sends recommendations to the excellent students (since they are already doing fine in their studies). Similar results are observed for the good students in the case of measuring not only absolute but also normalized (as defined in the “Performance Measures subsection) performance improvements.

In addition to the average performance improvement over all previously taken courses, we also considered the improvement taken over the last previously taken course. We also observe similar results in this case: the group of good students receiving personalized recommendations has significantly higher performance improvements than the control group of good students. Furthermore, similar results hold for the case of normalized version of this metric (as defined in the “Performance Measures subsection). Moreover, we examined performance improvements for other metrics used in this paper. The results are reported in Appendix E (including Table E1 there). Although improvements are observable in many cases, they are sometimes not statistically significant (see Appendix E for details). For example, consider the normalized version of the “differences with the last course within the same subject” measure. As one can see from Table E1 of Appendix E, although the values of 1.32 and 2.89 for the control and personalized groups are different, there is no statistically significant gain in comparison between these two groups in terms of the aforementioned measure. Note that when we computed this performance measure, we restricted the sample only to those students who have taken at least two courses within the same subject, such as Business or Computer Science. For example, we had 201 students belonging to personalized, 190 students to the nonpersonalized, and 156 to the control groups when we did the comparison using this performance measure. However, only 57 students from the personalized group followed our recommendations. Although their performance on the final exam was significantly improved in comparison to the control group of 156 students (see Table E1), the number of these students (57) was too small to “move the needle” for the entire personalized group. Hence, the overall performance for the control versus personalized groups (having 156 and 201 students respectively) did not show any performance improvements on average. The same reasoning is applicable to the variable “differences with all the previous courses within the same subject” in Table E1 of Appendix E and thus also explains why there are no statistically significant differences between the entire personalized and control groups for this measure.

We have compared the performance of all the students across the three groups so far. We next focus on comparing performance of only those good students who followed our recommendations (i.e., by clicking on at least one recommended material during the semester). The results of this comparison are presented in the Appendix E (Table E1) for all the performance measures and in the graphical form in Figures 7– 10 for some of them. In particular, Figures 7–10 show the box plots<sup>5</sup> of the absolute and normalized performance scores on the final exam taken across the control, nonpersonalized, and personalized groups. Note, that the number of students (num) differ significantly across the three groups, as shown in Figures 7–10. This is the case because only those students who actually followed at least one of our recommendations are included in the personalized and nonpersonalized group counts in this type of comparison.

![](/api/attachments/58VTMAYA/fulltext/images/229cd1424a36cc5c4841d0812e685803507d5a8fd8535cad428b166152408a98.jpg)  
(a) Absolute

![](/api/attachments/58VTMAYA/fulltext/images/b87c58cd2c4e0a235b7dd79efb49767223eae1d85b90552034151ecac2bb1c28.jpg)  
(b) Normalized

Figure 7. Performance of Good Students on the Final Exam in (a) Absolute and (b) Normalized Terms  
![](/api/attachments/58VTMAYA/fulltext/images/7f524f8eb61b86c6f305f93571d1b79c2d07ad6f071f5c94aa4beb0a9962671e.jpg)  
(a) Absolute

![](/api/attachments/58VTMAYA/fulltext/images/77c12c056f72d8185868c41cc70c8e3cc4d462d1433d02ff5818c8a4190866a8.jpg)  
(b) Normalized  
Figure 8. The Difference in Performance of Good Students with the Last Course in (a) Absolute and (b) Normalized Terms Taken Across All Available Courses

Further, Figure 7 presents the performance results of good students on the final exam in absolute and normalized terms respectively. As the figure shows, the personalized group outperforms the control group in both the absolute and the normalized terms (i.e., average grades are 83.22 versus 79.39 and 0.11 versus -0.16 respectively.

Further, the results are statistically significant at the 0.05 significance level for both the absolute and normalized cases. The personalized group also outperforms the nonpersonalized group in both absolute and normalized terms, but this difference is not significant. The performance differences between the nonpersonalized and control groups are not statistically significant in cases a and b.

Figure 8 presents the grades comparison for the good students on the final exam of the current versus the last of the previously taken courses when no recommendations were provided and that previous course was selected from all of the available courses.

In particular, Figure 8(a) shows that the personalized group outperforms the control and nonpersonalized groups in absolute terms (performance improvement of 5.83 versus -0.37 and 0.78 respectively) and this improvement is statistically significant at the 0.05 significance level. Moreover, Figure 8(b) shows that the personalized group also outperforms the control and the nonpersonalized groups in normalized terms (performance improvement of 0.38 versus -0.11 and -0.15, respectively) and this improvement is statistically significant in both cases at the 0.01 significance level. Further, performance improvement differences between the nonpersonalized and control groups are not statistically significant in both cases (a and b).

![](/api/attachments/58VTMAYA/fulltext/images/555928d650e43b0fc66aebdc598c623fb12084d5cd4713567ff2f77ce684cdaa.jpg)  
(a) Absolute

![](/api/attachments/58VTMAYA/fulltext/images/6301a4e4b92743697c47269f42aa5d73a7afc461efdf63f77f33b39780048883.jpg)  
(b) Normalized  
Figure 9. The Difference in Performance of Good Students on the Last Course Within the Same Subject Area in (a) Absolute and (b) Normalized Terms<sup>6</sup>

Further, Figure 9 presents the grades comparison for the good students on the final exam of the current versus the last of the previously taken courses when no recommendations were provided and the previous course was selected from the courses in the same subject area (e.g., if the current course is in Computer Science (CS), then the previously taken courses are restricted only to CS courses).

As Figure 9 shows, the personalized group also outperforms the control and the nonpersonalized groups in absolute (performance improvement of 7.32 versus 1.32 and 0.39) and normalized (performance improvement of 0.22 versus -0.14 and 0.06) terms, and the difference in improvement between the personalized and control groups is statistically significant for both the absolute and normalized cases (with p-value < 0.05). The difference of improvements between the personalized and the nonpersonalized groups is statistically significant in the absolute case at the 0.05 significance level. Further, the differences between performance improvements of the nonpersonalized and control groups are not statistically significant in both cases (a and b).

In addition to Figures 7–9 that present the comparisons between the personalized, nonpersonalized, and control groups for the absolute and normalized performances on the final exams for the good students, Table E1 in Appendix E also presents such comparisons but it also does it for additional cases including comparison of improvements from all of the previously taken courses across all three groups of students. Note that Table E1 in Appendix E, containing performance results for good students, has only a couple of measures where performance results are not statistically significant (but where the personalized group, nevertheless, outperforms the control group) and, therefore, we do not discuss them in this section. As an example to illustrate our point, however, Figure 10 shows the performance differences for good students between the absolute score in the current course and the average score computed across the previously taken courses in the same subject area in which no recommendations were provided to the students. Although Figure 10 shows the performance improvement of 4.35 versus 1.70 and 0.85 for the personalized versus the control and the nonpersonalized groups, this difference is not statistically significant having p-value equal 0.22 and 0.18 respectively because of a small sample sizes.

This completes the description of our empirical results obtained in this study.

## Conclusions

In this paper we presented a method for providing automatic personalized filling-the-gap recommendations to students that gathers data on students’ progress through the course, identifies knowledge gaps in their learning of the course materials, and provides remedial recommendations of learning materials to the students with the purpose of filling these gaps. Furthermore, we empirically tested our filling-the-gap method in the setting of an online university using the A/B testing methodology and obtained the following results.

![](/api/attachments/58VTMAYA/fulltext/images/7657d8b3bc8b019c0ab66670a67053d45b2f3596131d36189df753bfc542ee99.jpg)  
Figure 10. Differences in Absolute Performance for All Previously Taken Courses in the Same Subject for Good Students

First, we showed that most of the students, who received our recommendations, found them relevant and helpful. Second, our personalized recommendations were helpful mostly to the good students (whose average final exam scores across the previously taken courses was between 70 and 90). These students improved their performance on the final exams significantly more (in comparison to their prior performance before they received personalized recommendations) than the students from the control group. Third, our study did not produce significant performance improvements for the excellent students because (1) many excellent students did so well in their courses that they did not even need any recommendations, and (2) this sample was fairly small (12 students), making it hard to draw any statistically significant inferences. Fourth, personalized recommendations did not help falling behind students in any significant way. This is the case because the group size was small: only six falling behind students, who received personalized recommendations, actually followed (clicked on) them. Fifth, our study showed no statistically significant performance differences between the nonpersonalized recommendations and the control group of students who did not receive any recommendations. Sixth, we have also shown that personalized recommendations work significantly better than nonpersonalized ones for good students and some performance metrics.

We have also shown that the proposed recommendation approach is scalable since it can be applied to a large number of courses offered by large universities. In addition, our method is linearly scalable in the number of students, thus making it applicable to the MOOC-like applications having many students. Finally, we have also shown that the proposed approach is generic and can, potentially, be used in numerous other learning institutions having different types of learning environments since our methodology made only few limiting assumptions about the structure and the nature of the courses. In particular, we assume that the course structure can be either extracted from the course syllabi or learned from the course materials. We also assume that there are enough questions in the quizzes to cover every topic and subtopic included in a course. In those environments where this may not be feasible the proposed method will fill in the gaps in those topics that are covered by quiz questions. We argue that those topics would be the most important ones in the course, and, therefore, the proposed method still would be helpful for students.

We also observe certain differences in recommendation effectiveness across some subjects. For example, we observed that recommendations for the Business students were more effective than for the Computer Science students. However, these differences were not statistically significant, mainly due to the small sample sizes of the Business and the CS students. One plausible reason for this is that business students need to read more while studying various business courses, while the CS students need to practice more their computing skills, including doing various exercises, developing software, etc. Therefore, recommendations of additional reading materials for business classes were, apparently, more effective than for the CS classes. However, since these performance differences were not statistically significant, we did not present them in the paper and designated them as the topics of future research.

As a part of the future work, we would like to examine whether some of the more advanced techniques deployed at any one of the seven stages of the filling-the-gap recommendation method described in the section “Filling-the-Gap Recommendation Method” can significantly improve the performance of our recommendation system. We also plan to examine how various synonym techniques can help to improve the performance of our system. We would also like to deploy some of the existing taxonomy learning methods described in stage one and see how well they perform in those applications where course taxonomies cannot be easily derived from the course syllabi or from the study guides. Furthermore, we would like to work on the development of hybrid recommendation methods where some recommendations are being generated by an automated system, like ours, while others are being handcrafted by the users. Finally, we would like to examine which factors of the online learning application contributed positively to the performance improvements of the system and which ones had negative effects.

## Acknowledgments

We thank Professor Natalia Levina and Professor Priya Raghubir for assistance with the experimental design, and Professor Anindya Ghose for comments that greatly improved the manuscript.

## References

Acharya, A., and Sinha, D. 2015. “Construction of Automated Concept Map of Learning Using Hashing Technique,” Advances in Intelligent Systems and Computing (327), pp. 567-578.

Adomavicius, G., and Tuzhilin, A. 2005a. “Personalization Technologies: A Process-Oriented Perspective,” Communications of the ACM (48:10), pp. 83-90.

Adomavicius, G., and Tuzhilin, A. 2005b. “Toward the Next Generation of Recommender Systems: A Survey of the State-of-the-Art and Possible Extensions,” IEEE Transactions on Knowledge and Data Engineering (17:6), pp. 734-749.

Agrawal, R., Gollapudi, S., Kenthapadi, K., Srivastava, N., and Velu, R. 2010. “Enriching Textbooks through Data Mining,” in Proceedings of the 1<sup>st</sup> ACM Symposium on Computing for Development, New York: ACM, Article 19.

Balacheff, N., Ludvigsen, S., de Jong, T., Lazonder, A., and Barnes, S. (eds.). 2009. Technology-Enhanced Learning: Principles and Products, Dordrecht, Netherlands: Springer Science+Business Media B.V.

Bethard, S., Okoye, I., Hang, H., Sultan, A., Martin, J. H., and Sumner, T. 2012. “Identifying Science Concepts and Student Misconceptions in an Interactive Essay Writing Tutor,” in Proceedings of the 7<sup>th</sup> Workshop on the Innovative Use of NLP for Building Educational Applications, Stroudsburg, PA: Association for Computational Linguistics, pp. 12-21.

Binshtok, M., Brafman, R. I., Shimony, S. E., Martin, A., and Boutilier, C. 2007. “Computing Optimal Subsets,” in Proceedings of the 22<sup>nd</sup> National Conference on Artificial Intelligence (Volume 2), A. Cohn (ed.), AAAI Press, pp. 1231-1236.

Blei, D., Griffiths, T., and Jordan, M. 2010. “The Nested Chinese Restaurant Process and Bayesian Nonparametric Inference of Topic Hierarchies,” Journal of the ACM (57:2), Article 7.

Blei, D., Ng, A., and Jordan, M. 2003. “Latent Dirichlet Allocation,” Journal of Machine Learning Research (3), pp. 993-1022.

Brusilovsky, P., and Nejdl, W. 2004. “Adaptive Hypermedia and Adaptive Web,” in Practical Handbook of Internet Computing, M. P. Singh (ed.), Boca Raton, FL: CRC Press.

Brusilovsky, P., and Peylo, C. 2003. “Adaptive and Intelligent Web-Based Educational Systems,” International Journal of Artificial Intelligence in Education, (13:2-4), pp. 159-172.

Brynjolfsson, E., Hu, Y. J., and Simester, D. 2011. “Goodbye Pareto Principle, Hello Long Tail: The Effect of Search Costs on the Concentration of Product Sales,” Management Science (58:8), pp. 1373-1386.

Chica, S., Ahmad, F., Martin, J. H., and Sumner, T. 2008. “Pedagogically Useful Extractive Summaries for Science Education,” in Proceedings of the 22<sup>nd</sup> International Conference on Computational Linguistics, Manchester, August, pp. 177-184.

Christensen, C. M., Horn, M. B., Caldera, L., and Soares, L. 2011. “Disrupting College: How Disruptive Innovation Can Deliver Quality and Affordability to Postsecondary Education,” Center for American Progress, February 8.

Dellarocas, C., and Van Alstyne, M. 2013. “Money Models for MOOCs,” Communications of the ACM (56:8), pp. 25-28.

Desmarais, M. C. “Mapping Question Items to Skills with Nonnegative Matrix Factorization,” ACM SIGKDD Explorations Newsletter (13:2), pp. 30-36.

Drachsler, H., Verbert, K., Santos, O. C., and Manouselis, N. 2015. “Panorama of Recommender Systems to Support Learning,” in Recommender Systems Handbook, F. Ricci, L. Rokach, and B. Shapira (eds.), New York: Springer, pp. 421-451.

Feng, M., Heffernan, N. T., Heffernan, C., and Mani, M. 2009. “Using Mixed-Effects Modeling to Analyze Different Grain-Sized Skill Models in an Intelligent Tutoring System,” IEEE Transactions on Learning Technologies (2:2), pp. 79-92.

Fleder, D. M., and Hosanagar, K. 2009. “Blockbuster Culture’s Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity,” Management Science (55:5), pp. 697-712.

Ghose, A., Ipeirotis, P. G., and Li, B. 2012. “Designing Ranking Systems for Hotels on Travel Search Engines by Mining User-Generated and Crowdsourced Content,” Marketing Science (31:3), pp. 493-520.

Graf, S., Lin, F., Kinshuk, and McGreal, R. 2012. Intelligent and Adaptive Learning Systems: Technology Enhanced Support for Learners and Teachers, Hershey, PA: IGI Global.

Guo, Y., and Gomes, C. P. 2009. “Learning Optimal Subsets with Implicit User Preferences,” in Proceedings of the 21<sup>st</sup> International Joint Conference on Artificial Intelligence, C. Boutilier (ed.), pp. 1052-1057.

Huang, A. 2008. “Similarity Measures for Text Document Clustering,” in Proceedings of the New Zealand Computer Science Research Student Conference, Christchurch, April 14-18.

Klasnja-Milicevic, A., Vesin, B., Ivanovic, M., and Budimac, Z. 2011. “E-Learning Personalization Based on Hybrid Recommendation Strategy and Learning Style Identification,” Computers & Education (56:3), pp. 885-899.

Kokkodis, M., Kannan, A., and Kenthapadi, K. 2014. “Assigning Educational Videos at Appropriate Locations in Textbooks,” in Proceedings of the International Conference on Educational Data Mining, International Data Mining Society.

Kumar, N., and Benbasat, I. 2006. “Research Note: The Influence of Recommendations and Consumer Reviews on Evaluations of Websites,” Information Systems Research (17:4), pp. 425-439.

Lee, J., and Leyffer, S. 2012. Mixed Integer Nonlinear Programming, New York: Springer-Verlag.

Li, S. S., and Karahanna, E. 2015. “Online Recommendation Systems in a B2C E-Commerce Context: A Review and Future Directions,” Journal of the Association for Information Systems (16:2), pp. 72-107.

Lucas, H. 2014. “Disrupting and Transforming the University,” Communications of the ACM (57:10), pp. 32-35.

Manouselis, N., Drachsler, H., Verbert, K., and Duval, E. 2013. Recommender Systems for Learning, New York: Springer Briefs in Electrical and Computer Engineering.

Murphy, R., Gallagher, L., Krumm, A., Mislevy, J., and Hafter, A. 2014. Research on the Use of Khan Academy in Schools, Menlo Park, CA: SRI Education.

Olney, A. 2010. “Extraction of Concept Maps from Textbooks for Domain Modeling,” in Intelligent Tutoring Systems, V. Aleven, J. Kay, and J. Mostow (eds.), Berlin: Springer, pp. 390-392.

Pathak, B., Garfinkel, R., Gopal, R. D., Venkatesan, R., and Yin, F. 2010. “Empirical Analysis of the Impact of Recommender Systems on Sales,” Journal of Management Information Systems (27:2), pp. 159-188.

Peña-Ayala, A. (ed.). 2013. Intelligent and Adaptive Educational-Learning Systems: Achievements and Trends, Berlin: Springer.

Rajaraman, A., and Ullman, J. D. 2011. Mining of Massive Datasets, Cambridge, England: Cambridge University Press.

Ricci, F., Rokach, L., Shapira, B., and Kantor, P. B. 2011. Recommender Systems Handbook (1<sup>st</sup> ed.), New York: Springer-Verlag New York, Inc.

Strehl, A., Ghosh, J., and Mooney, R. 2000. “Impact of Similarity Measures on Web-Page Clustering,” in Proceedings of the Workshop on Artificial Intelligence for Web Search, pp. 58-64.

Sujatha R, and Rao, B. R. K. 2011. “Taxonomy Construction Techniques—Issues and Challenges,” Indian Journal of Computer Science and Engineering (2:5), pp. 661-671.

Underwood, J. 2012. “Metis: A Content Map-Based Recommender System for Digital Learning Activities,” in Educational Recommender Systems and Technologies: Practices and Challenges, O. C. Santos and J. G. Boticario (eds.), Hershey, PA: IGI Global, pp. 24-42.

Valerio, A., Leake, D., and Cañas, A. J. 2007. “Automatically Associating Documents with Concept Map Knowledge Models,” in paper presented at the 33<sup>rd</sup> Latin American Informatics Conference, San Jose, Costa Rica

Villalon, J., and Calvo, R. 2011. “Concept Maps as Cognitive Visualizations of Writing Assignments,” Educational Technology & Society (14:3), pp. 16-27.

Wilson, K., and Nichols, Z. 2015. “The Knewton Platform: A General-Purpose Adaptive Learning Infrastructure,” Knewton Technical White Paper (https://www.knewton.com/wp-content/ uploads/knewton-technical-white-paper-201501.pdf).

Xiao, B., and Benbasat, I. 2007. “E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact,” MIS Quarterly (31:1), pp. (1): 137-209.

Xiao, B., and Benbasat, I. 2014. “Research on the Use, Characteristics, and Impact of e-Commerce Product Recommendation Agents: A Review and Update for 2007–2012,” in Handbook of Strategic E-Business Management, F. J. Martinez-López (ed.), New York: Springer, pp. 403-431.

Zaldivar, V. A., Burgos, D., and Pardo, A. 2012. “Meta-Rule Based Recommender Systems for Educational Applications,” in Educational Recommender Systems and Technologies: Practices and Challenges, O. C. Santos and J. G. Boticario (eds.), Hershey, PA: IGI Global, pp. 211-231.

Zhang, T., Agarwal, R., and H. C. Lucas. 2011. “The Value of IT-Enabled Retailer Learning: Personalized Product Recommendations and Customer Store Loyalty in Electronic Markets,” MIS Quaterly (35:4), pp. 859-881.

Zouaq, A., and Nkambou, R. 2008. “Building Domain Ontologies from Text for Educational Purposes,” IEEE Transactions on Learning Technologies (1:1), pp. 49-62.

Zubrinic, K., Kalpic, D., and Milicevic, M. 2012. “The Automatic Creation of Concept Maps from Documents Written Using Morphologically Rich Languages,” Expert Systems with Applications (36:16), pp. 12709-12718.

## About the Authors

Konstantin Bauman is an assistant professor in the Management Information Systems Department of the Fox School of Business, Temple University. His current research interests include machine learning, recommender systems, technology enhanced learning, and natural language processing. Konstantin received his M.S. in Mathematics from Moscow State Lomonosov University in 2008, his M.S. in Data Mining from Moscow Institute of Physics and Technology in 2009, and his Ph.D. in Geometry and Topology from Mathematical Institute of the Russian Academy of Science in 2012. Before joining Temple, Konstantin worked for four years as a research scientist at the Stern School of Business, New York University, and for five years at the research division of Yandex LLC, working on data mining and machine learning problems.

Alexander Tuzhilin is the Leonard Stern Professor of Business and the Chair of the Department of Information, Operations and Management Sciences at the Stern School of Business, New York University. His research interests include personalization, recommender systems and data mining. He has produced over 120 research publications on these and related topics. Alexander has served on the organizing committees of numerous conferences, including as program and general chair of the IEEE International Conference on Data Mining (ICDM), and as program and conference chair of the ACM Conference on Recommender Systems (RecSys). He currently serves as editor-in-chief for ACM Transactions on Management Information Systems.

# RECOMMENDING REMEDIAL LEARNING MATERIALS TO STUDENTS BY FILLING THEIR KNOWLEDGE GAPS

Konstantin Bauman Fox School of Business, Temple University, 1810 N. 13<sup>th</sup> Street, Philadelphia, PA 19122 U.S.A. {kbauman@temple.edu}

Alexander Tuzhilin Stern School of Business, New York University, KMC 44 West 4<sup>th</sup> Street New York, NY 10012 U.S.A. {atuzhili@stern.nyu.edu}

## Appendix A

## MINLP Problem Statement and Comparison Analysis

In stage three (of the “Filling-the-Gap Recommendation Method” section of the paper), we discuss the problem of identifying the best matching subset of units of knowledge from each source of materials $S \in L$ for each topic T in the course taxonomy. In particular, we search for subset X that maximizes criterion (1). This problem can be formulated as a mixed integer nonlinear programming (MINLP) problem as follows.

Let us denote by $a _ { \scriptscriptstyle X } = \{ a _ { 1 } , . . . , a _ { \scriptscriptstyle s } \}$ the indicator vector of subset X, such that $a _ { i } = 1 \mathrm { i f } i ^ { \mathrm { t h } }$ unit of knowledge from the source S belongs to subset $X ,$ and $a _ { i } = 0$ otherwise. Therefore, the problem can be formulated as searching for the vector $a _ { X }$ with values $a _ { i } \in \{ 0 , 1 \}$ maximizing the following criterion:

$$
\max _ {a _ {X}} \left(\frac {\left(\sum a _ {i} \cdot V (U _ {i})\right) \cdot V (T)}{\| \sum a _ {i} \cdot V (U _ {i}) \| \cdot \| V (T) \|}\right)
$$

constituting the MINLP problem.

Furthermore, since the described problem, as specified in stage three by Equation (1), can be solved optimally in a “reasonable” time for small sources of knowledge S, we compare the time and the performance of the heuristic proposed in stage three with the full (optimal) MINLP approach. In particular, we used the SCIP library (Achterberg 2009) to generate the MINLP solution of the problem. It turned out that this “hard” problem could be solved optimally in a reasonable time only for those cases when the number of items in a source did not exceed 30. Therefore, we compare the proposed heuristic with the MINLP approach based on the sources containing up to 30 items. The results of this comparison are presented in Figure A1 and show the times needed to identify the best matching subset from a given source for these two methods respectively.<sup>1</sup> Note that different subjects, topics, and sources have a different number of important key concepts, and, thus, they need different times to calculate cosine similarity distances. Therefore, the trend in the MINLP graph is unstable, as can be seen in Figure A1. Note, however, that the performance differences between our heuristic and the MINLP approach are recognizable and are quite significant in the cases of large numbers of items, as is shown in Figure A1.

![](/api/attachments/58VTMAYA/fulltext/images/1746dc1952e1ad12d769972da12808c66c432202f4add952103719075224c171.jpg)

Figure A1. Comparison of the Proposed Heuristic MINLP Approach in Terms of the Time Needed to Identify the Best Matching Subset of Items from the Source for a Given TOpic

As Figure A1 shows, it takes only 5 seconds for the MINLP method to identify the best matching subset of the units of knowledge from the source having 27 book chapters for a given topic from the course taxonomy. If a course has 100 topics, a book containing 27 chapters would take 8.33 minutes by the MINLP approach to process and identify the best matching subsets for all of the topics in the course. In contrast, it would take only about 30 seconds to do the same by our method. Note that this difference is significantly bigger than in our particular example for those cases having a larger number of units of knowledge in a source because the MINLP problem is NP-hard as is explained above.

Furthermore, we compared the performance of the two approaches in terms of how well they identify the best matching source of knowledge for a given topic of the course taxonomy. It turned out that the proposed heuristic and the MINLP approaches identify the same source of knowledge to be the most relevant for a given topic in 96.3% of all the cases. In the rest of the cases, our heuristic identifies the source with cosine similarity measure to the topic having 95.3% of the cosine measure to the best source identified by MINLP approach on average. This means that the proposed heuristic identifies the most relevant sources of knowledge in most (96.3%) of the cases, and identifies almost the best matching source in the rest of the cases.

Note that our heuristic does not guarantee finding the best matching subset of items in the source. However, for the leaf topics of the course taxonomy, it guarantees finding the best set of items consisting of one or two elements, which is enough for our particular problem having natural constraints of limiting the number of leaf units to a very small set, as explained in stage three (i.e., we do not want to overload the students with too much information). The situation is more complex for the interior nodes where our heuristic does not necessarily find the best matching subset of items from the source. However, our heuristic works fine (identifies the most relevant subset of units of knowledge from the source in many cases and almost the best matching subsets in the remaining ones) for the following reasons. First, the comparison of the proposed heuristic with the MINLP approach described above showed that both of them identify the same subset of units of knowledge from the source in 58.8% of the cases. Second, in the remaining 41.2% of cases, the proposed heuristic identified the subset with cosine similarity measure to the topic being, on average, within 94.6% of the cosine measure of the best subset identified by MINLP approach.

## Reference

Achterberg, T. 2009. “SCIP: Solving Constraint Integer Programs,” Mathematical Programming Computation (1:1), pp. 1-41.

## Appendix B

## An Example of a Recommendation Letter

Dear Joe,

Based on the analysis of the materials covered in the course so far, we believe that you should review the following topics and the corresponding materials while preparing for the Final Exam:

Course: Art History

Themes:

• Ancient Greece and Rome

We suggest that you study chapters: 2, 3 from “Art History The Basics”

• Art of Revolution: Neoclassicism and Romanticism

We suggest that you study the following pages: page\_1; page\_2; page\_3 on cite www.radford.edu.

Note that all the listed materials are clickable.

We hope that you will find them useful in your study.

Best regards,

\*\*\*\*

Associate Provost for Academic Affairs

\*\*\*\* University

If you want to opt out of the future e-mails, please follow this link: unsubscribe.

## Appendix C

## The Survey Questions

Did you recall receiving at least one e-mail letter from Education Tools with recommendations of additional materials?

YES

• NO – then skip to the end of survey

## Part 1: Details

Please specify for which course you received recommendations?

(If you have received recommendations for more than one course, please choose only one of them and fill this form based on it.)

To the best of your memory, how many e-mails with recommendations / for this course have you received during the last term?

Which of the following statements describes your experience of / obtaining recommended materials?

• I had no problems with obtaining them

• I had problems with opening e-mails

• I had problems with opening recommended web-sites

• I had problems with downloading recommended PDF documents

• I had problems with opening recommended PDF documents

Other: TEXT

## Part 2: Time

How many assignments have you done in this course during the current term?

None

• Less than a half

• More than a half

• All assignments

How many hours per week have you spent on average studying for this course?

• less than 1 hour

1–2 hours

• 2–3 hours

• 3–5 hours

• 5–8 hours

more than 8 hours

How much time have you spent studying additional materials/recommended to you via Education Tools?

f In preparing for the first Graded Quiz

In preparing for the second Graded Quiz

f In preparing for the Final Exam

• not received

• 0 hours

• less than 1 hour

• 1–2 hours

• 2–3 hours

• 3–5 hours

more than 5 hours

Based on your experience would it be better if our Education Tools provided

• Much more materials

• More materials

• Same amount of materials

• Less materials

• Much less materials

How much time would be optimal for you to spend on studying additional materials recommended by Education Tools during preparation for the Final Exam?

0 hours

• less than 1 hour

• 1–2 hours

• 2–3 hours

• 3–5 hours

• more than 5 hours

What should the best time be for you to receive recommendations of additional materials (comparing to the actual time when the recommendations were provided to you)?

f In preparing for the first Graded Quiz

f In preparing for the second Graded Quiz

f In preparing for the Final Exam

• Should be earlier

• It was the right time

Should be later

• Not applicable

Please specify your preferences of time (e.g., a few hours/days/weeks earlier/later):

## TEXT

## Part 3: Quality

To what extent do you agree or disagree with each of the following statements?

f Recommended materials were relevant for the course

f Recommended materials were hard to understand

f Recommended materials were helpful in your studies

f You have learned new things from recommended materials

f You understand why we sent you that particular recommendations

f You discussed your recommended materials with your classmates

f You would like to recommend use of this Education Tools to your friend

f You would like to recommend this course to your friend

• Not Applicable

• Strongly disagree

• Disagree

Neutral

• Agree

• Strongly agree

Please make suggestions, how we can make our recommendations better?

## TEXT

## Part 4: Demographics

What is your gender?

What is your age?

• Under 25 years old

• 25–44 years old

• 45 years or older

Education: What is the highest degree or the school level that you have completed?

Employment Status: Are you currently…?

How much time per week do you have left after fulfilling all of your work and family obligations?

0 hours

• 1–3 hours

• 3–6 hours

• 6–9 hours

more than 9 hours

## Appendix D

## Analysis of Survey Data

We analyzed the survey data to see how various types of survey variables affect student performance on the final exam. For each of the variables from the survey, we performed statistical tests to check if a student’s performance on the final exam differs significantly across different values of these variables.<sup>2</sup> Our results show that there are no statistically significant differences in student performances on the final exam for most of the variables. Only in the following two cases were these differences significant. First, for the variable “Studying time for a course per week,” the performance was significantly better for the value of “3–5 hours” than for the value “more than 8 hours.” This surprising and unintuitive result could be explained by the fact that an underperforming student needs more time to study but still falls behind. Another plausible reason could be the fact that an average or a bad student tends to report exaggerated working hours in order to look better, whereas a diligent student tends to report honest answers. Second, for variable “Studying time of recommended materials in preparation for the final exam,” the performance was significantly better for the value of “2–3 hours” than for “1–2 hours.” This result confirms our claim that our recommendations were helpful. In summary, we did not observe any significant influences of the survey variables on students’ performance on the final exam with the exception of the few cases described above. In those few cases where we indeed observed it, we cannot draw any serious conclusions because (1) the population of the students submitting their surveys was small and (2) we expect that many students did not provide honest answers in their surveys (such as telling us the correct time they spent studying for the course).

## Appendix E

## Results for Good Students

Table E1 shows the performance results for the good students. The first column in this table presents the name of the corresponding performance metric (such as normalized difference to two previously taken courses considered across all available courses). The rest of the columns specify the performance metric for the following groups of students respectively: control group (C); nonpersonalized group (Non P); students from nonpersonalized group who followed the recommendations (Non P-F); personalized group (P); and students from personalized group who followed the recommendations (P-F).

Note that we use the following marks in the table:

\* – marks the result for the personalized group if it is significantly different from the control group at 0.05 significance level

† – marks the result for the personalized group if it is significantly different from the nonpersonalized (i.e., standard) group at 0.05 significance level.

<table><tr><td colspan="6">Table E1. Results for Good Students Having Average GPA Between 70 and 90</td></tr><tr><td>Type of Difference</td><td>C</td><td>Non P</td><td>Non P-F</td><td>P</td><td>P - F</td></tr><tr><td>Absolute Exam Grades</td><td>79.39</td><td>80.47</td><td>79.32</td><td>81.92</td><td>83.22*</td></tr><tr><td>Normalized Exam Grades</td><td>-0.16</td><td>-0.05</td><td>-0.02</td><td>0.04*</td><td>0.10*</td></tr><tr><td>Diff to Last courses: All subjects: Absolute</td><td>-0.37</td><td>0.64</td><td>0.78</td><td>3.47*</td><td>5.83*</td></tr><tr><td>Diff to Last courses: All subjects: Normalized</td><td>-0.10</td><td>-0.11</td><td>-0.04</td><td>0.10*</td><td>0.38*</td></tr><tr><td>Diff to Last courses: Same subjects: Absolute</td><td>1.32</td><td>1.38</td><td>0.39</td><td>2.89</td><td>7.32*</td></tr><tr><td>Diff to Last courses: Same subjects: Normalized</td><td>-0.13</td><td>-0.11</td><td>0.06</td><td>-0.13</td><td>0.22*</td></tr><tr><td>Diff to All previous courses: All subjects: Absolute</td><td>-1.68</td><td>0.07</td><td>-1.30</td><td>0.59*</td><td>1.75*</td></tr><tr><td>Diff to All previous courses: All subjects: Normalized</td><td>-0.16</td><td>-0.14</td><td>-0.09</td><td>0.03*</td><td>0.09*</td></tr><tr><td>Diff to All previous courses: Same subjects: Absolute</td><td>1.70</td><td>1.74</td><td>0.85</td><td>1.73</td><td>4.35</td></tr><tr><td>Diff to All previous courses: Same subjects: Normalized</td><td>-0.13</td><td>-0.11</td><td>-0.02</td><td>-0.02</td><td>0.09</td></tr></table>
