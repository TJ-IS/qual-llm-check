---
otero_id: 570
otero_key: "YF87H2ZU"
title: "Analyzing unstructured text data: Using latent categorization to identify intellectual communities in information systems"
authors: "Kai R. Larsen; David E. Monarchi; Dirk S. Hovorka; Christopher N. Bailey"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.02.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analyzing unstructured text data: Using latent categorization to identify intellectual communities in information systems

Kai R. Larsen ⁎, David E. Monarchi, Dirk S. Hovorka, Christopher N. Bailey

Leeds School of Business, University of Colorado, Boulder, 419 UCB, Boulder, CO 80309, United States

## a r t i c l e i n f o

Article history: Received 8 December 2006 Received in revised form 23 February 2008 Accepted 28 February 2008 Available online 6 March 2008

Keywords: Latent Categorization Method Unstructured data analysis Organization of information systems Research communities Sub<sup>fi</sup>elds Research topics

## a b s t r a c t

The Information Systems <sup>fi</sup>eld is structured by the research topics emphasized by communities of journals. The Latent Categorization Method categorized and automatically named IS research topics in 14,510 abstracts from 65 Information Systems journals. These topics were clustered into seven intellectual communities based on publication patterns. The technique develops categories from the data itself, it is replicable, is relatively insensitive to the size of the text units, and it avoids many of the problems that frequently accompany human categorization. As such LCM provides a new approach to analyzing a wide array of textual data.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Since the inception of the <sup>fi</sup>eld, Information Systems (IS) researchers have questioned the identity of the <sup>fi</sup>eld and have attempted to map the <sup>fi</sup>eld's intellectual organization. More recently, researchers have proposed normative frameworks of what constitutes the “core” of IS research [7,50]. However, some researchers are concerned that such a normative perspective might be overly constraining and that the “the vibrancy of the information systems discipline lies in its porous boundaries, or the relatively large grey area that characterizes its domain, and the interests of the information systems research community” [52, p. 1]. This current research agrees with the view presented by DeSanctis [18] that the identity of IS lies in the action of systematic inquiry and the interactions within communities of practice. In this research, we are guided by Benbasat and Zmud's [7] statement; “…the primary way in which a scholarly discipline signals its boundaries — and in doing so, its intellectual core — is through the topics that populate discipline-speci<sup>fi</sup>c research activities” (p. 184). However in contrast to Benbasat and Zmud's [7] normative approach, we argue that the identi<sup>fi</sup>cation of the <sup>fi</sup>eld's intellectual core is best achieved through empirical examination of what topics researchers actually investigate and publish in IS journals worldwide. We establish a historical view of the discipline [39] by determining the topics of intellectual interest to IS researchers over a 13 year period. We view IS as a “subject complex” which Apter [3] de<sup>fi</sup>nes as “…an integration of parts of a wide range of other subjects in terms of a well developed body of ideas and techniques” (p. 99). Applied and theoretical sciences like IS, cybernetics, chemistry, and physics relate to a broad range of other subjects that can be studied in terms of them. As a discipline, IS considers both “what is” and “what may be” in its behavioral and design aspects [27,54], has multiple reference disciplines [32,34], and has multiple epistemological perspectives [45,49]. It is, therefore, unlikely that IS can revolve around a clearly de<sup>fi</sup>ned and restricted set of topic areas or techniques because the subject matter itself is evolving and <sup>fi</sup>nding applications in new economic, personal, organizational, societal and cultural arenas.

The age and limitations of prior research combined with recent questions regarding the structure of the IS <sup>fi</sup>eld suggest that an updated, accurate, and comprehensive overview would be of immense value to the <sup>fi</sup>eld. In the absence of such a review, and due to the breadth and diversity of the IS <sup>fi</sup>eld, researchers may not fully comprehend the scope of IS sub<sup>fi</sup>elds, nor appreciate their colleagues' research interests and communities [36]. This lack of a comprehensive and replicable structure increases the dif<sup>fi</sup>culty of communicating within the <sup>fi</sup>eld, especially in an international context. Recent research indicates that North American research can be differentiated from European research based on research topics, theories, and sources [19–21]. Such differences support the argument that a comprehensive framework be based on representative journals from the whole <sup>fi</sup>eld, rather than merely a narrow sample of North American publications. Vessey et al. [57, p. 170] captured this necessity in the statement:

We believe that the <sup>fi</sup>eld should acknowledge not only those journals typically rated as being the top journals of our <sup>fi</sup>eld, such as those examined in this study, but also journals that focus on areas such as system development, human– computer interaction, and so on. What is needed is a portfolio of journals that represents the <sup>fi</sup>eld in its entirety and that can serve as guides not only to prospective authors but also to promotion and tenure committees.

The research presented here is a quantitative analysis of a larger dataset from a more extensive set of journals than has previously been examined. It is based on the perspective that scienti<sup>fi</sup>c <sup>fi</sup>elds are organized and structured by the corpus of research problems and criteria for evaluation accepted by a scienti<sup>fi</sup>c community of researchers [39]. This research presents the structure of the IS <sup>fi</sup>eld at two levels of analysis: the research topics that comprise the <sup>fi</sup>eld, and the communities of interest that perform research and publish articles on speci<sup>fi</sup>c sets of IS topics. In addition to those two levels, this research directly addresses the question of whether IS is composed of identi<sup>fi</sup>able sub<sup>fi</sup>elds as proposed by Banville and Landry [4]. From our perspective, these sub<sup>fi</sup>elds represent intellectual communities.

To identify the intellectual communities, the Latent Categorization Method (LCM) [44] was used to cluster abstracts into automatically named topic areas. A total of 14,510 abstracts published in 65 journals was included, making it the most comprehensive sample of IS literature examined to date by an order of magnitude. This paper presents two new views of the IS discipline;

1) A quantitative and replicable analysis of the research topics published in the IS literature.<sup>1</sup>

2) The intellectual communities of interest as represented by sets of interrelated topics, journal editors, reviewers, and contributors.

By using LCM to analyze research abstracts from a large set of IS journals, a comprehensive view of the scope and depth of research is developed. In addition, once a realistic view of the IS <sup>fi</sup>eld gains acceptance, future research may be tailored to speci<sup>fi</sup>c communities for the purposes of developing journal rankings [46], bodies of knowledge [28], and increasingly mature normative arguments [7].

This study introduces to Information Systems researchers the Latent Categorization Method (LCM), a new analytic technique that facilitates analysis of textual data that mathematically and computationally clusters and labels units of text, generally referred to as artifacts. LCM and related approaches have recently gained prominence in the IS <sup>fi</sup>eld [see for example, 14,60], and is capable of handling large datasets. LCM aims to:

develop a reproducible representation of artifacts (e.g., documents, interview data, survey data, etc.) and an approach to labeling that representation in a way that would (a) reduce… problems of human interpretation of the data; and (b) allow the application of quantitative techniques based on cardinal, rather than ordinal or nominal, data. Such an advance would offer an alternative as well as a complement to some existing methods for categorizing and labeling qualitative data [44, p. 351–352].

Although human categorization of text data provides valuable insights into phenomena, this method is prone to two potential problems. First, the time required to perform human coding often limits the amount of data analyzed. Second, the analysis of text data is prone to variability of human categorization of research topics/keywords [26,38,55]. As a computational technique, LCM is capable of analyzing very large datasets in a reproducible manner that is less susceptible to human interpretation bias.

Methods of semantic analysis, whether human or computationally based, are intended to determine the meaning of textbased data. Research articles use language to communicate perceptual experience and abstract concepts that map onto our inner or outer worlds. LCM and similar semantic analytic techniques view meaning as “almost entirely the relations that are represented and activated by words and collections of words” [42, p. 8]. From this perspective, to know what a word means is to possess the lexical network and “some set of techniques suf<sup>fi</sup>cient to attach the [word node] to the same experiences, objects or situations as are associated with it by other [speakers]” [40, p. 55]. Thus, LCM does not provide a “better” technique for extracting meaning from text units; rather it provides a rigorous, reproducible and largely automatic method for comparing meaning in large text-based datasets.

Through a thorough review of the literature, we show that, although previous research in this area has been in<sup>fl</sup>uential, LCM provides an opportunity to update and re<sup>fi</sup>ne our conceptualization of the intellectual communities which form the IS discipline. Latent Categorization is a novel and groundbreaking method that provides reliability in that any researcher using this method with the same parameters will get identical results. Finally, we discuss the potential contributions of this new method to the <sup>fi</sup>eld and discuss the implications of our analysis of intellectual communities within the IS <sup>fi</sup>eld.

## 2. Structure of the IS <sup>fi</sup>eld

## 2.1. Previous frameworks of the IS field

As noted by Vessey et al. [57, p.130], “since its inception, the <sup>fi</sup>eld has engaged in extensive self-examination.” This selfexamination has often been in response to criticism that the <sup>fi</sup>eld is a fragmented adhocracy,<sup>2</sup> undisciplined, and lacking a central theme [2,4,7,35]. While one response to this criticism is a prescriptive view (e.g., [7]), another response is exempli<sup>fi</sup>ed by the efforts to determine the structure of the <sup>fi</sup>eld [e.g., 57]. Iivari et al. [30] noted that a considerable body of IS knowledge exists but that it is quite broad in scope and distributed over a large number of journals. They call for the IS research community to take stock of and organize its knowledge.

Overview of previous research

<table><tr><td>Article</td><td>Purpose</td><td>Years</td><td>Samplea</td><td>Method</td></tr><tr><td>[11]</td><td>Framework for research on MIS analysis and design.</td><td>N/A</td><td>N/A</td><td>Theoretical development.</td></tr><tr><td>[31]</td><td>Framework for MIS research</td><td>1973–1979</td><td>331 MIS doctoral dissertations.</td><td>Qualitative categorization.</td></tr><tr><td>[53]</td><td>Classification scheme for computing literature</td><td>N/A</td><td>N/A</td><td>Qualitative categorization.</td></tr><tr><td>[17]</td><td></td><td></td><td></td><td></td></tr><tr><td>[47]</td><td>Overview of business school IS research strategies</td><td>N/A</td><td>Survey of 12 IS program strategy statements.</td><td>Qualitative categorization.</td></tr><tr><td>[15]</td><td>Structure of MIS field</td><td>1972–1982</td><td>Articles associated with 47 MIS researchers.</td><td>Bibliographic citation analysis.</td></tr><tr><td>[16]</td><td>Structure of MIS field</td><td>1980–1985</td><td>Articles associated with 42 MIS researchers.</td><td>Bibliographic citation analysis.</td></tr><tr><td>[1]</td><td>Structure of IS field and its evolution</td><td>1968–1988</td><td>CACM, DB, DS, HBR, JMIS, MS, MISQ, SMR. 908 MIS articles in eight core journals.</td><td>Qualitative categorization.</td></tr><tr><td>[23]</td><td>Topic areas of computer science, software engineering and information systems</td><td>N/A</td><td>N/A</td><td>Theoretical development.</td></tr><tr><td>[56]</td><td>Overview of IS topics</td><td>1987–1992</td><td>Submissions to ISR. 397 papers.</td><td>Qualitative categorization.</td></tr><tr><td>[6,5]</td><td>Classification scheme for IS</td><td>1970–1987</td><td>MISQ, I&amp;M, DS, MS, CACM, JMIS, ISR, OS.</td><td>Qualitative categorization.</td></tr><tr><td>[25]</td><td>IS research themes (methodological rigor primary focus)</td><td>1980–1989</td><td>MISQ, JMIS, I&amp;M, ICIS, CACM, ACMCS, MS, DS, AMJ. 227 articles.</td><td>Qualitative categorization.</td></tr><tr><td>[12]</td><td>Show what the researchers are doing in the IS field</td><td>1981–1997</td><td>MISQ and I&amp;M. 1121 articles.</td><td>Qualitative categorization.</td></tr><tr><td>[57]</td><td>Research approaches and diversity in IS research field</td><td>1995–1999</td><td>ISR, JMIS, MISQ, MS, DS. 488 articles.</td><td>Qualitative categorization</td></tr><tr><td>[24]</td><td>Increasing understanding of computer science, software engineering and information systems disciplines.</td><td>1995–1999</td><td>Information Systems: ISR, JMIS, MISQ, MS, DS. Software Engineering: ACM TSEM, IST, JSS, IEEE Software, IEEE TSE, SPE. Computer Science: 13 journals [22] as selected in Ramesh et al. [24]. 1485 articles.</td><td>Qualitative categorization</td></tr></table>

<sup>a</sup> ACMCS — ACM Computing Surveys, ACM TSEM — ACM Transactions on Software Engineering and Methodologies, CACM — Communications of the ACM, DB — Data Base for Advances in Information Systems, DS — Decision Sciences , DSS — Decision Support Systems, HBR — Harvard Business Review, IEEE TEM — IEEE Transactions on Engineering Management. IEEE TSE — IEEE Transactions on Software Engineering, I&M — Information & Management. IST — Information and Software Technology, ISJ — Information Systems Journal, ISR — Information Systems Research, JSS — Journal of Systems and Software, JMIS — Journal of Management Information Systems, MS — Management Science, MISQ — MIS Quarterly, OS — Organization Science, SPE — Software Practice and Experience, SMR — Sloan Management Review.

Previous studies (see Table 1) have provided immeasurable value to the IS <sup>fi</sup>eld. Approaches have included historical documentation, the creation of keyword classi<sup>fi</sup>cation schemes, benchmarking, diversity assessments, frameworks, topic lists, taxonomies, social network overviews, and the examination of core vs. outlying topics.

Each of these studies examined a small selection of articles or abstracts from a subset of journals in the IS <sup>fi</sup>eld. The limited samples and journal selection raise the question of whether they accurately represent the entire IS field or just mainstream research published in the highest ranked journals. For these studies to claim to map the intellectual organization of the IS discipline, one must assume that all sub<sup>fi</sup>elds are well represented in just a few of the highest-ranking journals within a short time horizon. Swanson and Ramiller [56] captured the common limitations to these studies when they commented on their own work that “while the ISR submissions stream gives one picture of the research activity in the <sup>fi</sup>eld, work that some might label “IS” is almost certainly taking place out of the journal's sight” (p. 323). In addition, while North American journals dominate the rankings of IS journals, journals based outside of North America should be included to gain a complete view of IS as a discipline. It should also be noted that current ranking approaches [e.g., 51,61] will always discriminate against journals not part of the largest intellectual community, thereby invalidating arguments that only the top ranked journals in a <sup>fi</sup>eld need be examined. Finally, none of these studies have examined DeSanctis' [18] communities of practice, an important oversight that this paper intends to address.

## 2.2. Subfields identification within the information systems discipline

Banville and Landry [4, p. 49] state that “it is generally agreed that our discipline is made up of what has (sic) been called sub<sup>fi</sup>elds,” and Hirschheim and Klein [28] suggest that concise descriptions of the body of knowledge for a few sub<sup>fi</sup>elds “could lift the discourse on the state of knowledge in the IS research community to a new level for both the internal and external constituencies” [28, p. 264]. But Hirschheim and Klein continue by noting that “of course a potentially thorny question is what are the IS sub-specializations and where would such a listing of them come from” [28, p. 263]?

In this work, we consider two criteria for the identi<sup>fi</sup>cation of sub<sup>fi</sup>elds. First, the body of work or set of researchers must be of such a size that it is recognizable and would likely have several journals dedicated to a set of topics of interest. Second, sub<sup>fi</sup>elds are composed of interrelated topics that form a subject complex [3] or a network of topics with a cumulative tradition that become the focus of a community of researchers editors, reviewers, and journals over time. The sub<sup>fi</sup>elds should be expected to surface from analyses conducted on the same kind of data with several years between analyses.

A fuller understanding of the sub<sup>fi</sup>elds of IS also has implications for tenure processes and journal rankings. Lowry et al. [46] suggested that rankings of the journals of the whole IS <sup>fi</sup>eld create problems for researchers that conduct their work exclusively within a sub-discipline. They went on to state that “by leaning toward ‘mainstream’ journals, subdisciplines are inappropriately devalued, and their adherents are marginalized from the <sup>fi</sup>eld of IS” [46, p. 36]. If researchers self-select into sub<sup>fi</sup>elds, far-reaching implications for evaluation of research within the overall IS domain exist [10].

Given the uncertainty surrounding what actually constitutes sub<sup>fi</sup>elds, this current research seeks to con<sup>fi</sup>rm the existence as well as the identity of the sub<sup>fi</sup>elds which make up the IS discipline. With this information, future ranking studies as well as studies designed to determine the bodies of knowledge of sub<sup>fi</sup>elds may provide a greatly increased understanding of the overall IS domain.

Our assertion is that the structure and organization of the IS <sup>fi</sup>eld and its literature is a social phenomenon that evolves as information technologies, their applications, and their impacts are researched. The structure of the <sup>fi</sup>eld is represented by intellectual communities that observe, describe, research, and theorize about certain phenomena, and then present the results of these processes to the editors and reviewers of journals that are accepting of those ideas, research methods, and evaluative criteria. Intellectual communities can be delineated by what Kuhn [39] describes as a “disciplinary matrix.” This matrix consists, in part, of the topics of interest, problems, and exemplars, and criteria for evaluation shared by the community. We suggest that this matrix is re<sup>fl</sup>ected in the editorial policies of journals, and that the research deemed appropriate by the reviewers and editors is one means of identifying communities. This idea is well described by Kuhn [39, p 131] who states:

Some of the principles deployed in my explanation of science are irreducibly sociological, at least at this time… Whatever scienti<sup>fi</sup>c progress may be, we must account for it by examining the nature of the scienti<sup>fi</sup>c group, discovering what it values, what it tolerates, and what it distains.

As IS is transdisciplinary in nature, the boundaries of these communities are not likely to have clear demarcations. Instead the groupings indicate large-scale social structures which organize the intellectual communities that comprise the IS domain. The challenge, then, becomes one of <sup>fi</sup>nding a research method that can explicate these social structures.

## 3. The Latent Categorization Method

Latent Categorization is a method that quantitatively represents the implicit semantic relationships and the content of a corpus of text. The value computed for each text artifact can then be subjected to a clustering algorithm, factor analysis, etc. LCM begins by treating each text artifact as a set of words without structure. Non-content bearing words that occur only once or almost always in a text artifact, (e.g. “of”, “the”, and “be”) are removed. Articles, prepositions, pronouns, and conjunctions, as well as common adjectives and adverbs may also be removed.

The remaining words are stemmed to avoid having multiple forms of a word represented in the analysis. Stemming converts a word to a related form, i.e. it “con<sup>fl</sup>ates” the word. For example, stemming the words “walk”, “walking”, and “walked” reduces all three to “walk.”

The technical details of the subsequent numeric transformation and statistical processing steps may be reviewed in Larsen and Monarchi [44]. In brief, the method creates a sparse matrix with the unique stems as rows, the artifacts as columns, and the number of occurrences of a speci<sup>fi</sup>c stem in a speci<sup>fi</sup>c abstract as the cell value. This matrix was weighted using TFIDF before it was submitted to a singular value decomposition (SVD), and the resulting right singular vectors are clustered using an agglomerative clustering approach. The main weakness of the approach is that interpretation of the resulting dendrogram is left up to the researcher, thereby leading to massive amounts of work and potential <sup>fl</sup>aws of human interpretation [44].

This research develops an extension named Automatic Node Naming (ANN) that addresses this shortcoming in the standard LCM. After the decomposition and clustering, LCM as applied in this research consists of Word Impact Analysis (WIA), Automatic Node Naming (ANN), and Word Activation (WA). Word Impact Analysis (WIA) approximates the marginal impact that a speci<sup>fi</sup>c term in a cluster has on the proximity of the cluster to other clusters. That is, how does the presence of the term affect the joining of two clusters to form a new cluster? (Actually, the analysis is performed from the perspective of what would happen if the termwas removed from the cluster.) WIA allows the determination of the amount of movement in the position of the cluster centroid that would occur if the word was not present in the cluster. Technical details on WIA are provided in Appendix A. The Automatic Node Namer (ANN) is a simple rule-based system that navigates the dendrogram using a tree-traversal order (see Appendix B for technical details). An extension to LCM [44], ANN skips the leaf nodes by considering only those nodes in the dendrogram which are clusters composed of more than one leaf.

In summary WIA and ANN automatically process the nodes of the dendrogram in a consistent manner. The outcome is a set of named clusters. These topics may individually be analyzed using the WA technique, helping during the development of a de<sup>fi</sup>nition for each topic.

## 3.1. Word activation

While WIA and ANN have focused on representing the whole dataset, the concept of word activation (WA) is different. Word activation starts with a map of the relationships between all words in the whole dataset. Using this structure and the distances between words, information about a speci<sup>fi</sup>c cluster is superimposed on the structure to show which of the words were actually in<sup>fl</sup>uential and related within the cluster under examination. The graphic would indicate the 20 word-stems that were closest in the n-dimensional space to the location of the computing cluster. However, while words that are close together have a high probability of appearing in the same cluster, many do not. This presents an opportunity to understand the speci<sup>fi</sup>cs of what went into creating a cluster while also understanding what did not go into creating that same cluster.

The example shows the relationships of the cluster named “computing” with related words in the cluster. The thicker the line between words, the stronger the relationship is within this cluster. Items that are far apart, but with thick bonds indicate items that for the whole dataset are not close, but which within this particular cluster are quite related. Items without lines, while related to computing are not important within the context of this speci<sup>fi</sup>c cluster.

Examining the topic of computing in the HCI community, we <sup>fi</sup>nd that attitude and experience and reasonably close to anxious, age, gender, male, and female. It is also moderately close to adult, traits, and efficacy. Words that are close to computing for the whole dataset, but not close in this cluster, include literacy, like, technophobe, computer, microcomputer, aptitude, bout, and virus. This gives a good idea that this particular cluster is focused on attitudes to the process of computing and how experience and other variables, including anxiety, age, and gender, affect such attitudes. It is particularly instructive to observe the tight network of relationships between the activated words.

The cluster is not, however, focused on the hardware side as signi<sup>fi</sup>ed by the absence of links to computer and microcomputer, the literacy on such computers, computer aptitude, or technophobes. Neither is this particular cluster of research focused on computer viruses. It is fascinating to note that, in this example one might observe evidence suggesting stovepiping within the IS <sup>fi</sup>eld. A reasonable researcher might observe that concepts such as technophobe, liking, literacy, and aptitude deserve some attention during computing attitude research. Taken together, these relationships provide information that may be used to de<sup>fi</sup>ne the individual clusters.

## 3.2. Sample selection and application of LCM

LCM provides the power to analyze a much larger and thereby potentially more representative journal dataset then has been previously examined. As noted earlier, exclusion of journals based upon geography (North American vs. European) or selection of only “mainstream” journals effectively pre-determines the research topics of the <sup>fi</sup>eld because the selected subset of journals will re<sup>fl</sup>ect only certain intellectual communities. This selection of journals was based upon ranking of IS journals [e.g., 48,59,61]. An overview of the included journals may be found in Tables 3–9.

Abstracts from the selected IS journals were downloaded from automated databases, typed in manually, or retrieved through contacts with journal editors. To avoid disproportionate focus on journals with long publication histories over others, it was decided to include only articles published from

1990 through 2002. To allow further analysis of topics in individual journals, only journals where a minimum of 25 abstracts had been collected were included.<sup>3</sup> One notable exclusion in the original analysis was Management Science, which publishes some IS papers every year. Because Management Science does not itself note which papers are considered IS, the journal was originally excluded to avoid creating a tautology by applying a subjective de<sup>fi</sup>nition of what topics are considered IS. Only after a more advanced understanding of the IS <sup>fi</sup>eld was attained through analysis of the pure IS journals were IS articles from Management Science selected for analysis (analyzing all abstracts would likely have led to communities created for reference disciplines). The journal was then added to the existing data, and the same analysis conducted to determine community membership for the journal. In the results section, the journal is listed with its community but noted because it was projected into the semantic space after-the-fact.

## 3.3. Factor analysis of cluster structure

To understand the intellectual organization of the IS <sup>fi</sup>eld, we examined the relationships between journals and research topics by performing a factor analysis using the journals as variables and the clusters as observations. Each cell of the data contained the number of artifacts within a speci<sup>fi</sup>c cluster that came from the speci<sup>fi</sup>c journal.

Principal component analysis (PCA) with varimax rotation is the most common approach to factor analysis, and the orthogonal approach used in varimax <sup>fi</sup>ts with the LCM approach, which is also orthogonal. When the variables all have the same units, as they do here, the factors may be contrasted one versus another. The factor scores can therefore be used to understand which topics were most in<sup>fl</sup>uential within each factor or community. The scores were also comparable across communities so that analysis of across cross-community topics was possible.

## 4. Results: structure of the IS <sup>fi</sup>eld

## 4.1. Intellectual communities in information systems

Although the list of 324 research topics uncovered by this research is of interest, it alone does not provide satisfactory insight into the intellectual structure of the <sup>fi</sup>eld. Such structure was revealed in the seven sub<sup>fi</sup>elds or intellectual communities of journals and research topics presented below. The factor analysis (Table 2) accounted for 53% of the variance using seven factors as suggested by the Cattell scree test [9,29]. This is an acceptable level of variance for exploratory factor analysis according to contemporary standards [see, e.g., 41,61], especially when such a high proportion is derived from only 12% of the potential set of factors. While the Cattell test may sometimes result in an insuf<sup>fi</sup>cient number of factors, all factor solutions between two and six were examined and all excluded a signi<sup>fi</sup>cant number of journals as unexplainable by that factor solution. The Kaiser–Meyer–Olkin Measure of Sampling

Table 3  
Table 2 Total variance explained

<table><tr><td rowspan="2">Component</td><td colspan="3">Rotation sums of squared loadings</td></tr><tr><td>Total</td><td>% Variance</td><td>Cumulative %</td></tr><tr><td>1</td><td>8.096</td><td>13.494</td><td>13.494</td></tr><tr><td>2</td><td>4.713</td><td>7.855</td><td>21.348</td></tr><tr><td>3</td><td>4.598</td><td>7.663</td><td>29.011</td></tr><tr><td>4</td><td>4.022</td><td>6.704</td><td>35.715</td></tr><tr><td>5</td><td>4.015</td><td>6.692</td><td>42.407</td></tr><tr><td>6</td><td>3.601</td><td>6.002</td><td>48.409</td></tr><tr><td>7</td><td>2.913</td><td>4.855</td><td>53.264</td></tr></table>

Adequacy of .77 was well above the threshold value of .50 [33,58]. Bartlett's Test of Sphericity further shows signi<sup>fi</sup>cance below .001, well below the required cutoff point of .05, suggesting that factor analysis was appropriate for this dataset.

The following tables (Tables 3–9) consist of two groups of columns. First, the topic areas of each community of interest are split into four columns. The columns present the main topics, how many abstracts clustered into that topic, a de<sup>fi</sup>nition for the topic, and factor scores. The order of the topics was determined using factor scores derived through regression analysis, where community scores for each topic were computed from the coef<sup>fi</sup>cients. Sorting the community scores illustrates which topics are important in each community. To save space, only topics with a factor score N3.0 are de<sup>fi</sup>ned in the table. The last row of each table lists research topics with factor scores between 3.0 and 1.0.

The second group of columns outlines the journals around which researchers of the community focus their submissions.

The factor loadings are the components of each factor in terms of the original variables. Journals with loadings ≥.3 are listed in the right-hand column of the community tables below. Journals that loaded highly on more than one factor were listed in multiple communities with an asterisk when listed in their non-primary community location.

Community 1 — Management Information Systems research (Table 3), with Information and Management as the most representative journal, focuses on the organization and individuals within the organization, as well as the tools used to improve the ef<sup>fi</sup>ciency of organizations. The topics as well as the journals indicate that this factor might arguably represent the main thrust of what is often referred to as Management Information Systems research. It is interesting to note that the most mainstream and highly ranked IS journals — such as MIS Quarterly, Information Systems Research, and Journal of Management Information Systems are found in this community.

This community is quite heterogeneous and accounts for almost twice as much variance as any other community in the analysis (13.5%). Intuitively it appears that this community should be subject to further subdivision. We therefore redid our analysis for only the articles in journals that loaded on factor one (MIS community) in the <sup>fi</sup>rst analysis at a factor loading of .5 or higher (selecting .5 prevented selection of articles that primarily belonged in another factor). For these 14 journals (including Management Science), there was a clear unidimensional structure.

Our research agrees with some previous papers and combines a number of topics within this community. It is important, however, to distinguish between an intellectual community and a topic. Every intellectual community contains research on many topics, and each researcher will (with a few notable exceptions) work on several topics. Some researchers may also do cross-community research. Because of this, the approach of analyzing individual papers provides advantages over the previous quantitative approaches of examining individual researchers.

Management Information Systems (MIS) community

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journala</td><td>Factor loading</td></tr><tr><td>Groups</td><td>260</td><td>Research on groups and group support systems (GSS), Group Decision Support Systems (GDSS).</td><td>6.24</td><td>Information &amp; Management</td><td>.843</td></tr><tr><td>Management</td><td>145</td><td>Management of businesses and organizations and information technology.</td><td>5.66</td><td>European Journal of Information Systems</td><td>.776</td></tr><tr><td>Strategy</td><td>148</td><td>Business strategy and relationships to IS strategy.</td><td>5.01</td><td>MIS Quarterly</td><td>.773</td></tr><tr><td>Planning</td><td>143</td><td>Planning for systems. Related to strategies, methodologies, and integration.</td><td>3.64</td><td>Journal of Information Technology Management</td><td>.733</td></tr><tr><td>EDI</td><td>97</td><td>Research on Electronic Data Interchange (EDI) and its value.</td><td>3.23</td><td>Journal of Management Information Systems</td><td>.731</td></tr><tr><td>Firms</td><td>92</td><td>Firms investments, and strategy.</td><td>3.2</td><td>The Journal of Strategic Information Systems</td><td>.660</td></tr><tr><td>CASE</td><td>83</td><td>Research on Computer Assisted Software Engineering (CASE).</td><td>3.09</td><td>Information Systems Research</td><td>.637</td></tr><tr><td>BPR</td><td>88</td><td>Business Process Re-engineering, Business Process Redesign. Processes and change.</td><td>3.05</td><td>Journal of Systems Management</td><td>.627</td></tr><tr><td>Projects</td><td>145</td><td>Research on projects for software developments.</td><td>3.01</td><td>Journal of Information Technology International Journal of Information Management The Journal of Information Systems Management Information Resources Management Journal Management Science Information Systems Journal Journal of Organizational Computing &amp; Electronic Commerce Information Technology &amp; People* Decision Support Systems Business Process Management Journal Australian Journal of Information Systems* Journal of Information Systems*</td><td>.615 .614 .580 .573 .545** .522 .463 .430 .416 .354 .348 .324</td></tr><tr><td colspan="4">Community also includes: Success, Business, Outsourcing, DSS, Organizations, End-users, Research, Decisions, Expert, Investing, Software, Models, Users, Methodologies, Job, Teams, Quality, Innovations, Change, EIS, Skills, Risks, Training, Companies, Databases, Knowledge.</td><td>Journals loading below .3 were not included in the list.</td><td></td></tr></table>

Global and Societal (GS) research

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Countries</td><td>133</td><td>Globally focused research comparing countries, especially on telecommunications, internet, economy, service, culture, and technology use in general.</td><td>13.51</td><td>The Electronic Journal on Information Systems in Developing Countries</td><td>.828</td></tr><tr><td rowspan="9">Culture</td><td rowspan="9">99</td><td rowspan="9">Culture and technology in organizations and across borders.</td><td rowspan="9">5.27</td><td>Journal of Global Information Management</td><td>.809</td></tr><tr><td>Information Technology for Development</td><td>.807</td></tr><tr><td>Journal of Global Information Technology Management</td><td>.761</td></tr><tr><td>The Information Society</td><td>.743</td></tr><tr><td>Information Technology &amp; People</td><td>.568</td></tr><tr><td>International Journal of Information Management*</td><td>.489</td></tr><tr><td>Journal of the AIS</td><td>.423</td></tr><tr><td>Journal of Information Technology*</td><td>.323</td></tr><tr><td>Journal of Strategic Information Systems*</td><td>.312</td></tr><tr><td colspan="4">Community also includes: Web, Internet, Global, Students, Virtual, Commerce, Service, Industry, Technology, Management, Health, Policies, Social, Business.</td><td colspan="2">Journals loading below .3 were not included in the list.</td></tr></table>

Asterisk denotes one of 16 journals that loaded on two communities.

Community 2 — Global and Societal research (Table 4), is focused on the ways in which information technologies in<sup>fl</sup>uence developing countries and society in general. The Electronic Journal on Information Systems in Developing Countries is the most representative journal, and topics unique to this community include countries, culture, internet, global, health, and social. The placement of the Journal of the AIS in this category is surprising, but this may be due to a small sample of abstracts from this journal (25 abstracts).

Community 3 — Human–Computer Interaction research (Table 5) focuses on the design, use and interaction of humans and computers. This community supports research on interfaces, visualization and computing at the individual and group levels. Other topics unique to this community include work, programs, text, tasks, language, and hypertext. The community is best represented by the journal Behavior and Information Technology.

Community 4 — Electronic Commerce research (Table 6) publishes articles on topics such as electronic markets and modern technologies such as the Internet, the World Wide Web, and virtual technologies. The community is best represented by the International Journal of Electronic Commerce.

Community 5 — Systems and Software Engineering research (Table 7) is focused on computer software testing and veri<sup>fi</sup>cation, architecture, formal speci<sup>fi</sup>cations and other aspects of IS engineering. Within this community, IEEE Transactions on Software Engineering is the most representative journal.

Community 6 — Information Storage and Retrieval research (Table 8). Although it shares topics with Community 5 (algorithms, objects and parallel processes), this community is differentiated by its interest in reliability, architecture, real-time computing, and software reuse. Information retrieval is the focus, whether structured and database-related, or unstructured and document-based. This community has Information Systems as its most representative journal.

Human–Computer Interaction (HCI) research

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Interfaces</td><td>190</td><td>Research on interfaces to computing, and user interactions with the interfaces.</td><td>7.92</td><td>Behaviour and Information Technology</td><td>.847</td></tr><tr><td>Design</td><td>186</td><td>Research on design of software.</td><td>6.00</td><td>International Journal of Human-Computer Interaction</td><td>.748</td></tr><tr><td>Visualization</td><td>120</td><td>Research on visualization of information, programming interfaces as well as web and programming interfaces.</td><td>4.29</td><td>International Journal of Man-Machine Studies</td><td>.682</td></tr><tr><td>Knowledge</td><td>360</td><td>Knowledge research. Ties to ontologies, Knowledge-Based Systems (KBS), and experts.</td><td>4.00</td><td>International Journal of Human-Computer Studies</td><td>.680</td></tr><tr><td>Human interaction</td><td>97</td><td>Research on human-computer interactions.</td><td>3.68</td><td>Computers in Human Behavior</td><td>.545</td></tr><tr><td>Computing</td><td>107</td><td>Research on attitudes towards computing. Relationships to anxiety, learning, and efficacy.</td><td>3.59</td><td>Data Base for Advances in Information Systems*</td><td>.511</td></tr><tr><td>Users</td><td>108</td><td>Research on users, user participation, and user satisfaction.</td><td>3.49</td><td>Knowledge-Based Systems*</td><td>.478</td></tr><tr><td>Students</td><td>204</td><td>Research on students and learning in relation to information technology.</td><td>3.48</td><td>Journal of Computer Information Systems MIS Quarterly*</td><td>.319 .308</td></tr><tr><td colspan="4">Community also includes: Learning, Work, Programs, Text, Tasks, Communication, Job, Expert, End-users, Language, Cognition, Hypertext, Errors, Training, Virtual, Computing, Context.</td><td>Journals loading below .3 were not included in the list.</td><td></td></tr></table>

Asterisk denotes one of 16 journals that loaded on two communities.

Table 6 Electronic Commerce (EC) research

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Market</td><td>196</td><td>Research on markets and their use of technology. Especially electronic markets and relationships to pricing, risk, stocks, and trading.</td><td>12.20</td><td>International Journal of Electronic Commerce</td><td>.894</td></tr><tr><td>Internet</td><td>135</td><td>Research focusing on the Internet itself.</td><td>6.87</td><td>Electronic Markets</td><td>.845</td></tr><tr><td>Web</td><td>164</td><td>Research on the web, web site design, web commerce, navigation, site quality, and marketing.</td><td>4.69</td><td>Journal of Organizational Computing and Electronic Commerce</td><td>.811</td></tr><tr><td>Virtual</td><td>109</td><td>Research on virtual communities and virtuality.</td><td>3.92</td><td>Journal of Computer-Mediated Communication</td><td>.744</td></tr><tr><td>Commerce</td><td>75</td><td>Research on commerce, for the most part electronic commerce.</td><td>3.91</td><td>Australian Journal of Information Systems Information Systems Frontiers Communications of the AIS</td><td>.376 .371 .301</td></tr><tr><td colspan="4">Community also includes: Online, Communication, Job, Expert, End-users, Language, Cognition, Hypertext, Errors, Training, Virtual, Computing, Context.</td><td>Journals loading below .3 were not included in the list.</td><td></td></tr></table>

Community 7 — Knowledge-Based Systems research (Table 9) is focused on intelligent systems. This community's focus includes knowledge systems, agent-based system, expert systems, and several related topics. Many of the topics overlap with other communities, and the community is best represented by International Journal of Intelligent Systems in Accounting, Finance and Management.

## 4.2. Trans-community topics

An additional analysis of the topics and journals revealed topics that appeared in multiple communities. These topics are signi<sup>fi</sup>cant because they are of intellectual interest to a wider community of editors, reviewers and journals. This interest by the greater IS community may indicate that they are considered important, and possibly central, themes to IS research. Topics that appear in more than two communities include groups, projects, business, expert, models, knowledge, web, students, virtual, design, networks, and mobile.

## 4.3. Validation of framework

The starting point for the factor analysis leading to the <sup>fi</sup>nal framework was the combination of journals and topics, so these building blocks were selected for the validation effort. Because of the inclusive nature of the study we did not expect to <sup>fi</sup>nd experts who understood journals and topics for the whole IS <sup>fi</sup>eld, and therefore designed the study to take advantage of the respondents' areas of expertise. The respondents were evenly selected from the editorial boards of all the journals in our study, and 270 online questionnaire requests were sent out. 24 requests were returned as undeliverable or suggesting that the respondent would be out of the of<sup>fi</sup>ce until after our deadline for <sup>fi</sup>nishing the survey, leaving 140 useable responses for a response rate of 57% after one follow-up request.

The survey was designed to give each respondent an openended option of listing the three journals most similar to the focal journal they were contacted about. It was decided to make this open-ended to examine the representativeness of the selected journals. Of the 325 journals listed by the respondent, 180 or 55% were included in our study. Given that databases of journals in our <sup>fi</sup>eld range between 376 (Oklahoma State database) and 576 (Deakin University database), this indicates that while our study included only 10–18% of the journals in these databases, the journals selected were on respondents' minds.

Using the seven communities suggested by LCM, it was examined whether human experts selected as most similar those journals that belonged in the same community as the journal for which they were on the editorial board. With the exception of one journal, the Journal of the AIS, the expert agreement with LCM was remarkably high. For JAIS, it was clear that almost all the respondents mentioning it or who were on its editorial board considered it part of the MIS community. This con<sup>fi</sup>rmed our earlier worry about this journal having just 25 abstracts in our analysis, and that its placement was strongly dependent on the small sample which was most likely not representative for later articles. After JAIS was removed from the study, an 89% agreement between LCM and experts was reached, with a Cohen's kappa [13] of .83, generally acknowledged as “almost perfect” [43].

Systems and Software Engineering (SSE) research

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Programs</td><td>229</td><td>Research on programs and programming languages.</td><td>7.38</td><td>IEEE Transactions on Software Engineering</td><td>.894</td></tr><tr><td>Test</td><td>152</td><td>Research on testing of software.</td><td>6.38</td><td>ACM Transactions on Software Engineering and Methodology</td><td>.789</td></tr><tr><td>Software</td><td>226</td><td>Research on software reliability and failure as well as processes to avoid low reliability.</td><td>5.86</td><td>The Journal of Systems and Software</td><td>.770</td></tr><tr><td>Verification</td><td>109</td><td>Research on verification. Related to behavior and states.</td><td>4.34</td><td>Automated Software Engineering</td><td>.740</td></tr><tr><td>Algorithms</td><td>206</td><td>Research on algorithms.</td><td>3.87</td><td>Computer Journal</td><td>.601</td></tr><tr><td>Architecture</td><td>77</td><td>Research on software architectures.</td><td>3.32</td><td>Australian Computer Journal</td><td>.547</td></tr><tr><td>Formal specifications</td><td>88</td><td>Research on formal specifications.</td><td>3.16</td><td>Journal of Software Maintenance: Research and Practice</td><td>.484</td></tr><tr><td></td><td></td><td></td><td></td><td>Journal of the ACM*</td><td>.324</td></tr><tr><td colspan="4">Community also includes: Objects, Maintenance, Protocols, Real-time, Codes, Parallel, Components, Projects, Language, Graphs, Net, Metrics, Mobile, Scheduling, Design, Distributed, Security, Client/Server, Code, Tools, Trees, Networks, Reuse, Requirements, Methods, Logic.</td><td colspan="2">Journals loading below .3 were not included in the list.</td></tr></table>

Table 8  
Information Storage and Retrieval (ISR) research

<table><tr><td colspan="4">Community topic areas</td><td colspan="2">Community journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Queries</td><td>142</td><td>Research on database queries.</td><td>8.51</td><td>Information Systems</td><td>.801</td></tr><tr><td>Databases</td><td>119</td><td>Database research, including queries, and design.</td><td>5.71</td><td>Journal of Database Management</td><td>.706</td></tr><tr><td>Objects</td><td>213</td><td>Research on objects and object orientation, including programming and databases.</td><td>5.59</td><td>ACM Transactions on Information Systems</td><td>.681</td></tr><tr><td>Algorithm</td><td>206</td><td>Research on algorithms.</td><td>5.06</td><td>Computer Journal*</td><td>.595</td></tr><tr><td>Models</td><td>191</td><td>Research focusing on model development</td><td>4.32</td><td>ACM Computing Surveys</td><td>.589</td></tr><tr><td>Protocols</td><td>173</td><td>Research on protocols for transactions, especially in a database sense.</td><td>3.85</td><td>Data Base for Advances in Information Systems</td><td>.532</td></tr><tr><td>Documents</td><td>91</td><td>Research on documents, both document retrieval and IS development related documents.</td><td>3.72</td><td>Journal of the ACM</td><td>.477</td></tr><tr><td></td><td></td><td></td><td></td><td>Journal of Research and Practice in Information Technology</td><td>.429</td></tr><tr><td></td><td></td><td></td><td></td><td>Australian Computer Journal*</td><td>.413</td></tr><tr><td colspan="4">Community also includes: Retrieval, Web, Trees, Data, Graphs, Parallel, Temporal, Files, Hypermedia, Search, Groups, Hypertext, Images, Mobile, Ethics, Methods, Link, Memory, Multimedia.</td><td>Journals loading below .3 were not included in the list.</td><td></td></tr></table>

Asterisk denotes one of 16 journals that loaded on two communities.

The second part of the validation survey concerned whether the expert respondents would pick out the same topics found by LCM to belong to the community that LCM had determined. Given that neither the journal placement nor the topic placement could overlap with expert rater opinion unless they both made sense, we expected a good kappa here as well, though moderated for the much higher cognitive strain of this task. The raters were given 42 topic names and de<sup>fi</sup>nitions and asked to select between two to <sup>fi</sup>ve topics that best represented the focal journal. After removing the Journal of the AIS, a Cohen's kappa of .62 was achieved. While this is generally considered a “substantial” level of inter-rater agreement [43], it was so much lower than the kappa for the journal exercise that it requires further discussion. One possibility is that while the underlying analysis was solid, the naming procedure did not properly represent the content of each cluster or topic. Another possibility is that the second task was cognitively more dif<sup>fi</sup>cult in that it required reading much text and then comparing 42 topics. Finally, the respondents were also asked not simply to mention the topics they themselves generally dealt with, but rather the topics the journal had in common with other journals in that category, and because many of these journals have wide scopes individual reviewers may not have understood all aspects of a journal's focus. In conclusion, it is clear that the kappas for both tasks are well beyond acceptable, suggesting that the results from LCM were valid.

## 5. Discussion

The structure and identity of the IS discipline has been a persistent question since the <sup>fi</sup>eld's inception. This research avoided many of the problems and limitations of prior studies to show that the IS discipline is composed of seven identi<sup>fi</sup>able intellectual communities or sub<sup>fi</sup>elds. While this research demonstrates that the IS <sup>fi</sup>eld has sub<sup>fi</sup>elds with clear demarcations, the inclusion of some topics in multiple communities demonstrates porosity of boundaries that characterizes vibrant intellectual communities and indicates research topics which are of interest to the broader IS <sup>fi</sup>eld. However, although these different communities work on some common topics, the existence of different communities with different publication outlets suggests that researchers in different communities may often be unaware of complementary or overlapping research interests.

Knowledge-Based Systems (KBS) research

<table><tr><td colspan="4">Community Topic Areas</td><td colspan="2">Community Journals</td></tr><tr><td>Topics</td><td>#Abs</td><td>Definition</td><td>Factor score</td><td>Journal</td><td>Factor loading</td></tr><tr><td>Knowledge</td><td>360</td><td>Knowledge research. Ties to ontologies, Knowledge-Based Systems (KBS), and experts.</td><td>8.99</td><td>International Journal of Intelligent Systems in Accounting, Finance &amp; Management</td><td>.777</td></tr><tr><td>Agents</td><td>149</td><td>Research on agents.</td><td>7.45</td><td>Expert Systems with Applications</td><td>.752</td></tr><tr><td>Expert</td><td>249</td><td>Experts and Expert Systems (ES). Relationships to knowledge and tools.</td><td>5.88</td><td>Knowledge-Based Systems</td><td>.680</td></tr><tr><td>Audit</td><td>78</td><td>Research on auditing of expert systems and on auditing expert systems.</td><td>5.60</td><td>International Journal of Human-Computer Studies*</td><td>.459</td></tr><tr><td>Networks</td><td>225</td><td>Neural networks, trees, and routing.</td><td>4.25</td><td>Autonomous Agents and Multi-Agent Systems</td><td>.426</td></tr><tr><td></td><td></td><td></td><td></td><td>Journal of Information Systems</td><td>.361</td></tr><tr><td></td><td></td><td></td><td></td><td>International Journal of Man-Machine Studies*</td><td>.345</td></tr><tr><td></td><td></td><td></td><td></td><td>Information Systems Frontiers*</td><td>.341</td></tr><tr><td colspan="4">Community also includes: Rules, Decisions, Case, Design, Market, Fuzzy, Business, Planning, Learning, Models, Workflow.</td><td colspan="2">Journals loading below .3 were not included in the list.</td></tr></table>

Asterisk denotes one of 16 journals that loaded on two communities.

By identifying the intellectual communities underlying the IS discipline, this study provides an answer to Hirschheim and Klein's [28] “thorny question,” of where to begin de<sup>fi</sup>ning the “body of knowledge” for sub-specialization in the <sup>fi</sup>eld. They have argued that this is of tantamount importance before the discourse of the IS <sup>fi</sup>eld can be lifted to a new level. By examining the latent characteristics of abstracts published in a sample that was an order of magnitude larger than anything analyzed before, the central topics and intellectual communities of the IS <sup>fi</sup>eld were identi<sup>fi</sup>ed. This is the <sup>fi</sup>rst step to determining the bodies of knowledge of the sub<sup>fi</sup>elds and increasing communication among them.

Knowledge of an academic discipline's identity provides researchers with the ability to communicate with internal and external constituencies alike. Because certain classes of problems cannot be solved without communication between sub<sup>fi</sup>elds [36], increasingly insular sub<sup>fi</sup>elds decrease the probability of successful research outcomes. Communication problems with external constituencies decrease the likelihood that academicians and practitioners can successfully <sup>fi</sup>nd common ground. Because of the importance of both internal and external communication, the discourse related to <sup>fi</sup>nding and communicating the IS <sup>fi</sup>eld's identity takes on paramount importance.

Discourse about the IS <sup>fi</sup>eld's identity and composition has reemerged in the context of journals ranking and “crisis in the IS <sup>fi</sup>eld”. This research has shown just how open a journal may have to be to constitute a true umbrella journal for the IS <sup>fi</sup>eld, rather than just the MIS community. In this study, we <sup>fi</sup>nd that the top ranked journals in IS, including MISQ, ISR, and JMIS have focused their publication activities primarily in the MIS research community.

When comparing previous studies of the structure of the <sup>fi</sup>eld to the seven intellectual communities found in this study, some striking observations may be made. Of the seven previous studies examining journals (see Table 1), four cover only journals in the MIS Research community. Two studies cover only two communities: (MIS and Information Storage and Retrieval) and one study covered three communities (MIS, Information Storage and Retrieval, and Systems and Software Engineering). Surprisingly, four communities (Global and Societal, Human–Computer Interaction, Electronic Commerce, and Knowledge-Based Systems) are supported by journals that were not sampled in any of the prior studies. This is due in part to the newness of the communities relative to the timeframes of the prior studies. But it also illuminates the evolutionary nature of the <sup>fi</sup>eld and the need to include a broad sample of journals if we want to understand the entire discipline, rather than only those parts represented by a few top journals.

The boundary porosity between communities is of special interest in this research. The MIS community shares topics with <sup>fi</sup>ve other communities, indicating a large degree of boundary porosity. The topics web, internet, virtual and service are held in common between the Electronic Commerce and Global and Societal communities, suggesting interest in the in<sup>fl</sup>uence and application of e-commerce on the societal and global levels. In contrast to the <sup>fi</sup>ndings of Glass et al. [24] who found little overlap between the disciplines of IS and software engineering, there are many topics shared between the Information Storage and Retrieval and Software Engineering communities within the IS <sup>fi</sup>eld. This difference in our research may be due to the larger number of journals and articles included in this current study, as well as the avoidance of existing frameworks for analysis and sorting.

This research provides the opportunity for a new type of journal ranking study based upon publications within the set of seven communities. Such rankings would arguably lead to fairer evaluations of and by IS researchers who conduct most or all of their work within one of the communities. Recognizing these communities may help researchers to target publications outlets for their research topics, and should help tenure and promotion committees evaluate researchers' production.

This study also introduces Latent Categorization and a new extension as a new analytic method for analysis of the burgeoning volume of textual data available to IS researchers. Previously the sheer size of textual datasets that might provide interesting insights and theory development for IS phenomenon limited researchers' ability to analyze the data. LCM also provides for replicable analyses by avoiding many of the categorization and interpretation problems to which many qualitative methods are prone.

By itself, LCM provides replicable clusters of text artifacts. Unfortunately, while such clusters may be used for further statistical analysis such as factor analysis, it is essentially uninterpretable except though overlaying human analysis. The need for such an overlay mitigates the advantage of being able to analyze large datasets. Further, the need to cut a dendrogram at a certain level without taking the underlying semantics into consideration introduces problems in interpretations and analysis. By applying word impact analysis, LCM is capable of analyzing truly large datasets (orders of magnitude larger than the one used in this paper). By adding ANN, a semantically natural cutoff point is selected that allows better understanding of the underlying content and clusters that have a higher latent semantic consistency.

This study adds to our understanding of the IS landscape by identifying the topics researchers and editors actually select for publication and how the <sup>fi</sup>eld is organized by research outlet. To the extent that one agrees with the normative suggestions for restricting the “identity” of IS to the nomological net surrounding the information technology artifact, some of these communities will <sup>fi</sup>nd it easier to do so given their topics of interest. But research in IS, as it has been practiced and published in the past, has multiple identities which will most likely continue to defy well-de<sup>fi</sup>ned boundaries as technology itself evolves and <sup>fi</sup>nds new personal, social, and cultural niches to <sup>fi</sup>ll.

## 6. Limitations

This study is subject to several limitations including the removal of a few journals; the inability to categorize an abstract in more than one cluster; the retention of some words unrelated to the topics under consideration, and the limited presence of human judgment.

It is important to note that the low number of data points for some journals leads us to remove these journals from the sample and to question two journals' placement due to their short publication history. In addition, the aggregation of the abstracts over the thirteen-year period leads to a snapshot — rather than a history — of a dynamic and evolving <sup>fi</sup>eld. Future work should take this evolution into account and show how new research areas and communities have developed over time. Further, during the factor analysis, three journals loaded at less than .3 on any factor, leading us to remove them from further analysis: Accounting, Management, and Information Technologies (currently Information and Organization), the Journal of End User Computing, and the Scandinavian Journal of Information Systems. While this is not uncommon during factor analysis, future work including more IS journals may <sup>fi</sup>nd additional small intellectual communities containing these and other journals.

A signi<sup>fi</sup>cant limitation of this research was that we were not able to categorize an abstract in more than one cluster. Clearly, some articles deal with multiple topics, and should be placed in more than one cluster. This is an potentially fruitful area for future research.

Although the resulting 53% variance accounted for after the factor analysis was acceptable for exploratory analysis, it indicated that there may be other smaller — often emerging — communities in coexistence with the identi<sup>fi</sup>ed seven major communities of the <sup>fi</sup>eld. Future research should identify these sub-communities and their relationships to the main communities. Such an analysis may <sup>fi</sup>nd that the information systems development sub<sup>fi</sup>eld examined by Hirschheim and Klein [28] represents such a small community.

## Acknowledgements

This paper has bene<sup>fi</sup>ted greatly from comments by Claude Banville, Henri Barki, Akhil Kumar, Detmar Straub, and Zoya A. Voronovich. We also owe a great debt of gratitude to editors of several of the journals covered by this analysis for going to great lengths to grant us access to data.

## Appendix A. Word Impact Analysis

This section begins by looking at two leaves being joined together, and then extends the approach to include the joining of clusters.

Let i and j be the two leaves being joined to form a new cluster. Choose one of them, say j, and copy the jth column of the weighted term-frequency matrix, A, to a new vector ${ \bf q } _ { j } ,$ calling it a pseudo-artifact (a pseudo-document in Deerwester, 1990).

In the k-dimensional space of $\mathbf { A } _ { k } ,$ the pseudo-artifact may be written as

$$
\mathbf {q} _ {k j} = \mathbf {q} _ {j} ^ {T} \mathbf {U} _ {k} \mathbf {S} _ {k} ^ {- 1}\tag{0.1}
$$

[8].

The weighted artifacts with squared Euclidian distance as the dissimilarity measure can be written as

$$
A _ {k} ^ {T} A _ {k} = V _ {k} S _ {k} ^ {2} V _ {k} ^ {T}\tag{0.2}
$$

Using Eq. (0.1) for the approximation to artifact j and Eq. (0.2) for artifact i, the cosine between them is

$$
\cos \theta_ {i j} = \frac {\left(\mathbf {v} _ {i} ^ {T} \mathbf {S}\right) \left(\mathbf {U} ^ {T} \mathbf {q} _ {j}\right)}{\left| \left| \mathbf {v} _ {i} ^ {T} \mathbf {S} \right| \right| _ {2} \left| \left| \mathbf {U} ^ {T} \mathbf {q} _ {j} \right| \right| _ {2}}\tag{0.3}
$$

where the subscript k has been dropped for clarity. (This is also true in all subsequent equations.)

In turn, because U, S, and V are all known, Eq. (0.3) can be written as

$$
\cos \theta_ {i j} = c _ {0} \frac {\sum_ {l = 1} ^ {t} q _ {j l} c _ {i}}{\sqrt {\sum_ {h = 1} ^ {k} \left(\sum_ {l = 1} ^ {t} u _ {h l} q _ {j l}\right) ^ {2}}}\tag{0.4}
$$

where

$$
\begin{array}{l} c _ {0} = \sqrt {\sum_ {h = 1} ^ {k} (v _ {i h} s _ {h h}) ^ {2}} = | | e _ {i} ^ {T} \mathbf {V} _ {k} \mathbf {S} _ {k} | | _ {2} \\ c _ {i} = \sum_ {h = 1} ^ {k} s _ {h h} v _ {i h} u _ {h l} = e _ {i} ^ {T} \mathbf {V} _ {k} \mathbf {S} _ {k} \mathbf {U} _ {k} \end{array}\tag{0.5}
$$

and $e _ { i } ^ { T }$ is the jth column of a d×d identity matrix.

Eq. (0.4), can be used to determine the difference that the presence or absence of a speci<sup>fi</sup>c term in the query, $q _ { i l } ,$ has upon cos $\theta _ { i j } .$ The approach is simply to compute the cosine with and without the term in the query, cos $\theta _ { i j }$ and cos $\theta _ { i j _ { l } }$ respectively. The difference between them divided by cos $\theta _ { i j }$ and then subtracted from 1 provides a measure of the impact of this term on the association between the i and j artifacts. (Note that the sum of these proportions will not, in general, equal 1 because of the interactions of the terms in the denominator of Eq. (0.4).) The result is labeled $p _ { i j _ { l } }$

$$
p _ {i j _ {l}} = \left(\cos \theta_ {i j} - \cos \theta_ {i j _ {l}}\right) / \cos \theta_ {i j}\tag{0.6}
$$

with larger values indicating greater impact.

The procedure is to display the $p _ { i j _ { l } }$ in decreasing magnitude to determine the principle determinants of the value of the cosine, cos $\theta _ { i j } .$ Experience suggests that at most 10 terms are the determinants for each cosine. (Note that the matrix of these cosines is not symmetric due to the interactions within the term–term matrix [for a discussion of the transitive effects of terms in LSI, see 37]). At this point, a knowledge structure may be constructed by examining this data for each point in the dendrogram.

## Appendix B. Automatic Node Namer

As the Automatic Node Namer (ANN) navigates the tree, it goes through the following steps to develop the name for each cluster. In the description below, all points on the dendrogram are “nodes”. Leaves are the nodes at the bottom of the tree, the original data items which are being clustered. Clusters are groupings of two nodes which may or may not be clusters themselves. (Leaves cannot be clusters.) The two nodes which are members of a cluster may themselves be clusters.

1. For each pair of nodes which combine to form a new cluster, ANN <sup>fi</sup>rst determines the list of words in each node whose contribution to forming the cluster exceeds a threshold set by the analyst.

2. ANN next combines the two lists into a proposed name based on whether the analyst has required that all candidate words for the name exist in both lists or in only one. Within the list, the words are in decreasing magnitude of their contribution (see step 1).

3. Then ANN invokes the following rule set.

a. If either of the nodes is a leaf node, then the proposed name becomes the name of the cluster.

b. If neither node is a leaf node, then

i. if neither node has a name (i.e., each node's name is a zero-length string, “”), then the name of the cluster is set to a zero-length string also. (This rule is analystselectable.)

ii. if only one of the nodes has a name (the other is a zero-length string), and all of the words in that name exist in the proposed name for this cluster, then the proposed name becomes the name. Otherwise the name for this cluster is set to “”.

iii. if both of the nodes have names, then the cluster name is set to the union of the words in the names of the two nodes and the words in the proposed name.

4. ANN moves to the next node by tree-traversal order until all nodes are examined and nodes <sup>fi</sup>tting the criteria are labeled.

In this case, the dendrogram was automatically analyzed with a cosine cutoff of .10, a value that when tested worked well for small and large datasets alike. This left most of the dendrogram labeled with the words that best represented the content of the cluster below every fusion-point. At this point in the process, a set of topics have emerged and need to be de<sup>fi</sup>ned through word activation analysis.

## References

[1] M. Alavi, P. Carlson, A review of MIS research and disciplinary development, Journal of Management Information Systems 8 (4) (1992) 45–62.

[2] M. Alavi, E.A. Joachimsthaler, Revisiting DSS implementation research: a meta-analysis of the literature and suggestions for researchers, MIS Quarterly 16 (1) (1992) 95.

[3] M.J. Apter, Cybernetics: a case study of a scienti<sup>fi</sup>c subject-complex, The Sociological Review Monograph 18 (1972) 93–116.

[4] C. Banville, M. Landry, Can the <sup>fi</sup>eld of MIS be disciplined? Communications of the ACM 32 (1) (1989) 48–60.

[5] H. Barki, S. Rivard, J. Talbot, An information systems keyword classification scheme. MIS Ouarterly 12 (2) (1988) 299–322

[6] H. Barki, S. Rivard, J. Talbot, A keyword classi<sup>fi</sup>cation scheme for IS research literature: an update, MIS Quarterly 17 (2) (1993) 209–226.

[7] I. Benbasat, R.W. Zmud, The identity crisis within the IS discipline: de<sup>fi</sup>ning and communicating the discipline's core properties, Information Systems Research 27 (2) (2003) 183–194

[8] M.W. Berry, S.T. Dumais, G.W. O'Brien, Using linear algebra for intelligent information retrieval. SIAM Review 37 (4) (1995) 573-595.

[9] R.B. Cattell, The scree test for the number of factors multivariate behavioral research, 1966. 1: 245–276 http://www.gar<sup>fi</sup>eld.library. upenn.edu/classics1983/A1983PY50000001.pdf.

[10] C. Chau, et al., Measuring researcher-production in information systems, JAIS 3 (2002) 145–215.

[11] N.L. Chervany, G.W. Dickson, K.A. Kozar, An Experimental Gaming Framework for Investigating the In<sup>fl</sup>uence of Management Information systems on Decision Effectiveness, University of Minnesota, Minneapolis, Minnesota, 1972

[12] E. Claver, R. González, J. Llopis, An analysis of research in information systems (1981–1997), Information & Management 37 (4) (2000) 181-195.

[13] J. Cohen, A coef<sup>fi</sup>cient of agreement for nominal scales, Educational and Psychological Measurement 20 (1) (1960) 37–46.

[14] K. Coussement, D. Van den Poel, Improving customer complaint management by automatic email classi<sup>fi</sup>cation using linguistic style features as predictors, Decision Support Systems 44 (4) (2008) 870–882.

[15] M.J. Culnan, The intellectual development of management information systems, 1972–1982: a co-citation analysis, Management Science 32 (2) (1986) 156–172.

[16] M.J. Culnan, Mapping the intellectual structure of MIS, 1980–1985: a cocitation analysis, MIS Quarterly 11 (3) (1987) 341–353

[17] D.E. Denning, et al., The proposed new computing reviews classi<sup>fi</sup>cation scheme, Communications of the ACM 24 (7) (1981) 419–433.

[18] G. Desanctis, The social life of information research, JAIS 4 (7) (2003) 360–376.

[19] R.J. Evaristo, E. Karahanna, Is North American IS research different from European IS research? The DATA BASE for Advances in Information Systems 28 (3) (1997) 32–43.

[20] R.D. Galliers, M. Meadows, A discipline divided: globalization and parochialism in IS research, Communications of the AIS 11 (2003) 108–117.

[21] R.D. Galliers, E.A. Whitley, An anatomy of European Information Systems Research ECIS 1993–ECIS 2002: some initial <sup>fi</sup>ndings, European Conference on Information Systems, 2002, Gdansk, Poland

[22] R. Geist, et al., Computing research programs in the U.S. Communications of the ACM 36 (12) (1996).

[23] R.L. Glass, A comparative analysis of the topic areas of computer science, software engineering, and information systems, Journal of Systems and Software 19 (3) (1992) 277–289.

[24] R.L. Glass, V. Ramesh, I. Vessey, An analysis of research in computing disciplines, Communications of the ACM 47 (6) (2004) 89–94.

[25] V. Grover, C.C. Lee, D.E. Durand, Analyzing methodological rigor of MIS survey research from 1980–1989, Information & Management 24 (6) (1993) 305–317.

[26] J.A. Hampton, Testing the prototype theory of concepts, Journal of Memory and Language 34 (1995) 686–708.

[27] A.R. Hevner, et al., Design science in IS research, MIS Quarterly 28 (1) (2004) 75–106.

[28] R. Hirschheim, H.K. Klein, Crisis in the IS <sup>fi</sup>eld? A critical re<sup>fl</sup>ection on the state of the discipline, Journal of AIS 4 (10) (2003) 237–293.

[29] J.L. Horn, R. Engstrom, Cattell's scree test in relation to Bartlett's Chisquare test and other observations on the number of factors problem, Multivariate Behavioral Research 14 (3) (1979) 283–300.

[30] J. Iivari, R. Hirschheim, H.K. Klein, Towards a distinctive body of knowledge for information systems experts: coding ISD process knowledge in two IS journals, Information Systems Journal 14 (2004) 313–342.

[31] B. Ives, S. Hamilton, G.B. Davis, A framework for research in computerbased management information systems, Management Science 26 (1980) 910–934.

[32] B. Ives, et al., What every business student needs to know about information systems, Communications of the AIS 9 (2002) 467–477.

[33] H.F. Kaiser, Analysis of factorial simplicity, Psychometrika 39 (1974) 31–36.

[34] P.W. Keen, MIS research: reference disciplines and a cumulative tradition, Proceedings of the First International Conference on Information Systems, 1980, pp. 9–18

[35] D. Khazanchi, B.E. Munkvold, Is information systems a science? An inquiry into the nature of the information systems discipline, Data Base for Advanced in Information Systems 31 (3) (2000) 24–42.

[36] J.L. King, K. Lyytinen, Reach and grasp, MIS Quarterly 28 (4) (2004) 539-551.

[37] A. Kontostathis, W.M. Pottenger, Detecting patterns in the LSI term– term matrix, Proceedings of the Workshop on Foundations of Data Mining and Discovery, IEEE International Conference on Data Mining, IEEE.2002

[38] J.K. Kruschhke, ALCOVE: an exemplar based connectionist model of category learning, Psychological Review 99 (1992) 22–44.

[39] T. Kuhn, The Structure of Scienti<sup>fi</sup>c Revolutions, 2nd ed.The University of Chicago Press, Chicago, 1970.

[40] T. Kuhn, Commensurability, capability, communicability, in: J. Conant, J. Haugeland (Eds.), The Road Since Structure, University of Chicago Press, Chicago, 2000.

[41] D.M. Lahuis, S. Mellor, Antiunion and prounion attitudes as predictors of college students' willingness to join a union, Journal of Psychology 135 (6) (2001) 661–681.

[42] T.K. Landauer, LSA as a theory of meaning, in: D.S.M. Thomas, K. Landauer, Simon Dennis, Walter Kintsch (Eds.), Handbook of Latent Semantic Analysis, Lawrence Erlbaum Associates, Mahwah, NJ, 2007.

[43] J.R. Landis, G.G. Koch, The measurement of observer agreement fo categorical data, Biometrics 33 (1) (1977) 159–174.

[44] K.R. Larsen, D.E. Monarchi, A mathematical approach to categorization and labeling of qualitative data: the latent categorization method, Sociological Methodology 34 (1) (2004) 349–392.

[45] A.S. Lee, Integrating positivist and interpretive approaches to organiza tional research, Organization Science 2 (4) (1991) 342–365.

[46] P.B. Lowry, D. Romans, A. Curtis, Global journal prestige and supporting disciplines: a scientometric study of information systems journals, Journal of the Association for Information Systems 5 (2) (2004) 29–77.

[47] J.L. McKenney, in: J.L. McKenney (Ed.), Introduction to Part V, in The Information Systems Research Challenge: Proceedings, Harvard Business School Press, Boston, Massachusetts, 1984, pp. 335–337.

[48] N.A. Mylonopoulos, V. Theoharakis, Global perceptions of IS journals, Communications of the ACM 44 (9) (2001) 29–33.

[49] W. Orlikowski, The duality of technology: rethinking the concept of technology in organizations, Organization Science 3 (2) (1992) 398–427.

[50] W.J. Orlikowski, S.R. Barley, Technology and institutions: what can research on information technology and research on organizations learn from each other? MIS Quarterly 25 (2) (2001) 145–165.

[51] R.K. Rainer, M. Miller, Examining differences across journal rankings, Communications of the ACM 48 (2) (2005) 91–94.

[52] V. Sambamurthy, Editorial notes, Information Systems Research 16 (1) (2005) 1–5.

[53] J.E. Sammet, The new (1982) computing reviews classi<sup>fi</sup>cation system — <sup>fi</sup>nal version, Communications of the ACM 25 (1) (1982) 13–25.

[54] H.A. Simon, The Sciences of the Arti<sup>fi</sup>cial, The M.I.T. Press, Cambridge, MA, 1981.

[55] S.A. Sloman, B.C. Malt, A. Fridman, Categorization versus similarity: the case of container names, in: U. Hahn, M. Ramscar (Eds.), Similarity and Categorization, Oxford University Press, Oxford, England, 2001, pp. 73–86.

[56] E.B. Swanson, N.C. Ramiller, Information systems research thematics: submissions to a new journal. 1987-1992, Information Systems Research 4 (4) (1993) 299–330.

[57] I. Vessey, V. Ramesh, R.L. Glass, Research in information systems: an empirical study of diversity in the discipline and its journals, Journal of Management Information Systems 19 (2) (2002) 129–174.

[58] J.T. Walker, Statistics in Criminal Justice: Analysis and Interpretation, Jones and Barlett Publishers. Boston, MA. 1999.

[59] K.A. Walstrom, B.C. Hardgrave, Forums for information systems scholars: III, Information & Management 39 (2) (2001) 117–124.

[60] C.-P. Wei, C.C. Yang, and C.-M. Lin, A Latent Semantic Indexing-based approach to multilingual document clustering. Decision Support Systems, in press.

[61] M.E. Whitman, A.R. Hendrickson, A.M. Townsend, Research commentary. Academic rewards for teaching, research, and service: data and discourse, Information Systems Research 10 (2) (1999) 99–109.

Kai R. Larsen is an Associate Professor of Information Systems at the University of Colorado/Boulder Leeds School of Business. His research interests revolve around social in<sup>fl</sup>uence in adoption of information systems and automatic knowledge extraction from text. He has published in several journals, including Communications of the ACM, Journal of Management Information Systems, Sociological Methodology, and the European Journal of Information Systems.

Doctor Monarchi is a retired Full Professor of Systems at the University of Colorado at Boulder (UCB), where he was a member of the faculty from 1972 to 2006. He has published in various academic journals, such as the Journal of the American Statistical Association, Communications of the ACM, and Decision Support Systems, and presented his work both nationally and internationally. Doctor Monarchi's primary areas of interest are natural language programming, data and text mining, and knowledge extraction.

Dirk S. Hovorka is a Scholar in Residence at the Leeds School of Business, University of Colorado at Boulder. He received his B.A. from Williams College, MA and was awarded M.S. degrees in Geology and in Interdisciplinary Telecommunications as well as a Ph.D. in Information Systems from the University of Colorado. His research includes in<sup>fl</sup>uences of social networks on knowledge exchange, the philosophical foundations of IS research, information technology tailoring, and information systems in science.

Christopher N. Bailey is a graduate of the Information Systems program at the Leeds School of Business, University of Colorado. He currently works for Wall Street on Demand.
