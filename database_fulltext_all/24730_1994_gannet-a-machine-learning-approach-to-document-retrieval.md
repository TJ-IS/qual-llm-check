---
otero_id: 24730
otero_key: "GERDAJYC"
title: "GANNET: A Machine Learning Approach to Document Retrieval"
authors: "Hsinchun Chen; Jinwoo Kim"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518048"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# GANNET: A Machine Learning Approach to Document Retrieval

Hsinchun Chen & Jinwoo Kim

To cite this article: Hsinchun Chen & Jinwoo Kim (1994) GANNET: A Machine Learning Approach to Document Retrieval, Journal of Management Information Systems, 11:3, 7-41, DOI: 10.1080/07421222.1994.11518048

To link to this article: http://dx.doi.org/10.1080/07421222.1994.11518048

![](/api/attachments/GERDAJYC/fulltext/images/09ab4e1f9f43f000c5c4bba3171a09beda918b8b62aa3ef890c6d834c84165d5.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/GERDAJYC/fulltext/images/6baa3f125e5402edcd41f251a3ba4b3dffac63c18e62c717ab01689bdf2b669f.jpg)

Submit your article to this journal ↗

![](/api/attachments/GERDAJYC/fulltext/images/6913086df9dae1ae29eb1adf67c5dd778760b0edb2f2da2e3125c9e7e417aae8.jpg)

Article views: 1

![](/api/attachments/GERDAJYC/fulltext/images/7ece3f4d4ff780a5099113be4a1e9efa593a69718951c3b1d3d4f33870f0c346.jpg)

View related articles ↗

![](/api/attachments/GERDAJYC/fulltext/images/417a9eecdf733c34d1430e9c9acc7ed4c0eb2b34f9180440b75f010750ba0592.jpg)

Citing articles: 11 View citing articles ↗

# GANNET: A Machine Learning Approach to Document Retrieval

HSINCHUN CHEN AND JINWOO KIM

HSINCHUN CHEN received a Ph.D. in information systems from the Stern School of Business at New York University in 1989. He is an Assistant Professor of Management Information Systems at the Karl Eller Graduate School of Business at the University of Arizona. His research interests include computer-supported cooperative work, human-computer interactions, text-based information management and retrieval, internet resource discovery, knowledge acquisition and knowledge discovery, machine learning, and neural network modeling and classification. He received an NSF Research Initiation Award in 1992 and the Hawaii International Conference on System Sciences (HICSS) Best Paper Award in 1994. He was recently awarded a Digital Library Initiative grant by NSF/NASA/ARPA for a joint project with the University of Illinois from 1994 to 1998. Dr. Chen has published more than twenty articles in publications such as Communications of the ACM, IEEE Computer, IEEE Transactions on Systems, Man, and Cybernetics, IEEE EXPERT, Journal of the American Society for Information Science, Information Processing and Management, International Journal of Man-Machine Studies, and Advances in Computers.

JINWOO KIM received his Ph.D. in electrical and computer engineering, with a minor in management information systems, from the University of Arizona in 1994. He is currently a research associate in the Electrical and Computer Engineering Department at the University of Arizona. His research interests include evolution programs, parallel processing, discrete-event modeling and simulation, and machine learning. Dr. Kim has published in IEEE Transactions on Robotics and Automation.

ABSTRACT: Information retrieval using probabilistic techniques has attracted significant attention on the part of researchers in information and computer science over the past few decades. In the 1980s, knowledge-based techniques also have made an impressive contribution to “intelligent” information retrieval and indexing. More recently, information science researchers have turned to other, newer artificial intelligence-based inductive learning techniques including neural networks, symbolic learning, and genetic algorithms. The newer techniques have provided great opportunities for researchers to experiment with diverse paradigms for effective information processing and retrieval.

In this article we first provide an overview of newer techniques and their usage in information science research. We then present in detail the algorithms we adopted for a hybrid Genetic Algorithms and Neural Nets based system, called GANNET. GANNET performed concept (keyword) optimization for user-selected documents during information retrieval using the genetic algorithms. It then used the optimized concepts to perform concept exploration in a large network of related concepts through the Hopfield net parallel relaxation procedure. Based on a test collection of about 3,000 articles from DIALOG and an automatically created thesaurus, and using Jaccard's score as a performance measure, our experiment showed that GANNET improved the Jaccard's scores by about 50 percent and it helped identify the underlying concepts (keywords) that best describe the user-selected documents.

KEY WORDS AND PHRASES: intelligent information retrieval, machine learning.

THE AVAILABILITY OF CHEAP AND EFFECTIVE STORAGE DEVICES and information systems has prompted the rapid growth and proliferation of relational, graphical, and textual databases in the past few decades. Information collection and storage efforts have become easier, but the effort required to retrieve relevant information has become significantly more difficult, especially in large-scale databases. This situation is particularly evident for textual databases, which are widely used in traditional library science environments, in business applications (e.g., manuals, newsletters, and electronic data interchanges), and in scientific applications (e.g., electronic community systems and scientific databases). Information stored in these databases often has become voluminous, fragmented, and unstructured after years of intensive use. Only users with extensive subject area knowledge, system knowledge, and classification scheme knowledge [9] are able to maneuver and explore in these textual databases.

Most commercial information retrieval systems still rely on conventional inverted index and Boolean querying techniques. Even full-text retrieval produced less than satisfactory results $[3]$ . In the past few decades, probabilistic retrieval techniques have been used to improve the retrieval performance of information retrieval systems $[6, 49]$ . The approach is based on two main parameters, the probability of relevance and the probability of irrelevance of a document. Despite various extensions, probabilistic methodology still requires the independence assumption for terms and it suffers the difficulty of estimating term-occurrence parameters correctly $[33, 73]$ .

Since the late 1980s, knowledge-based techniques have been used extensively by information science researchers. These techniques have attempted to capture searchers' and information specialists' domain knowledge and classification scheme knowledge, effective search strategies, and query refinement heuristics in document retrieval systems design [10]. Despite their usefulness, systems of this type are considered performance systems [76]—they only perform what they were programmed to do (i.e., they are without learning ability). Significant efforts are often required to acquire knowledge from domain experts and to maintain and update the knowledge base.

A newer paradigm, generally considered to be the learning approach, has attracted attention of researchers in artificial intelligence, computer science, and other functional disciplines such as engineering, medicine, and business $[7, 53, 83]$ . In contrast to performance systems, which acquire knowledge from human experts, learning systems acquire knowledge automatically from examples—that is, from source data. The most frequently used techniques include symbolic, inductive learning algorithms such as ID3 [62], multiple-layered, feedforward neural networks such as Backpropagation net [72], and evolution-based genetic algorithms [30]. Many information science researchers have started to experiment with these techniques as well [2, 12, 13, 14, 33, 44].

In this paper, we present the design and a prototype implementation a hybrid genetic algorithms and neural networks based system, called GANNET, for “intelligent” information retrieval. The next section presents an overview of the learning techniques and some recent implementations in information retrieval (IR). We then describe the genetic algorithms and Hopfield neural networks we adopted for the hybrid system. The implementation details and testing results are presented in the fourth section, and we conclude the paper and describe future research directions in the final section.

## "Intelligent" Information Retrieval: An Overview

CREATING COMPUTER SYSTEMS WITH KNOWLEDGE OR "INTELLIGENCE" has long been the goal of researchers in artificial intelligence. Many interesting knowledge-based systems have been developed in the past few decades for such applications as medical diagnosis, engineering troubleshooting, and business decision making. Most of these systems have been developed based on manual knowledge acquisition process, a significant bottleneck for knowledge-based systems development.

A recent approach to knowledge elicitation is referred to as “knowledge mining” or “knowledge discovery” [26, 60]. Grounded on various machine learning techniques, the approach is automatic and it acquires knowledge or identifies patterns directly from some large collection of examples or real-life databases.

We review some of the important works of knowledge-based systems in IR and learning systems in IR, respectively, below.

## Knowledge-Based Systems in IR

There have been many attempts to capture information specialists' domain knowledge, search strategies, and query refinement heuristics in document retrieval systems design. For example, CoalSORT [54], a knowledge-based system, facilitates the use of bibliographic databases in coal technology. A semantic network, representing an expert's domain knowledge, embodies the system's intelligence. GRANT [18], developed by Cohen and Kjeldsen, is an expert system for finding sources of funding for given research proposals. Its search method—constrained spreading activation in a semantic network—makes inferences about the goals of the user and thus finds information that the user did not explicitly request but that is likely to be useful. Fox's CODER system [25] consists of a thesaurus that was generated from the Handbook of Artificial Intelligence and Collin's Dictionary. In CANSEARCH [61], a thesaurus is presented as a menu. Users browse and select terms for their queries from the menu. The "Intelligent Intermediary for Information Retrieval" ( $I^{3}R$ ), developed by Croft [19], consists of a group of "experts" that communicate via a common data structure, called the blackboard. The system consists of a user model builder, a query model builder, a thesaurus expert, a search expert (for suggesting statistics-based search strategies), a browser expert, and an explainer. The IOTA system, developed by Chiaramella and Defude, includes natural language processing of queries, deductive capabilities (related to user modeling, search strategies definition, use of expert and domain knowledge), management of full-text documents, and relevance evaluation of answers [17]. Chen and Dhar's METACAT [10] incorporates several human search strategies and a portion of the Library of Congress Subject Headings (LCSH) for bibliographic search. The system also includes a branch-and-bound algorithm for an automatic thesaurus (LCSH) consultation process.

The National Library of Medicine's thesaurus projects are probably the largest-scale effort that uses the knowledge in existing thesauri. In one of the projects, Rada and Martin [50, 65] conducted experiments for the automatic addition of concepts to MeSH (Medical Subject Headings) by including the CMIT (Current Medical Information and Terminology) and SNOMED (Systematized Nomenclature of Medicine) thesauri. Access to various sets of documents can be facilitated by using thesauri and the connections that are made among thesauri. The Unified Medical Language System (UMLS) project is a long-term effort to build an intelligent automated system that understands biomedical terms and their interrelationships and uses this understanding to help users retrieve and organize information from machine-readable sources [40, 46, 51]. The UMLS includes a Metathesaurus, a Semantic Network, and an Information Sources Map. The Metathesaurus contains information about biomedical concepts and their representation in more than ten different vocabularies and thesauri. The Semantic Network contains information about the types of terms (e.g., “disease,” “virus,” etc.) in the Metathesaurus and the permissible relationships among these types. The Information Sources Map contains information about the scope, location, vocabulary, and access conditions of biomedical databases of all kinds.

Another important component of information retrieval is user modeling capability, which is unique to reference librarians. During the user–librarian consultation process, the librarian develops an understanding of the type of user being dealt with on the basis of verbal and nonverbal clues. Usually, the educational level of the user, the type of question, the way the question is phrased, the purpose of the search, and the expected search results all play major roles in helping the librarian determine the needs of the user. The librarian, in essence, creates models of the user profile and the task requirements during the consultation process.

User modeling has played a crucial role in applications such as question-answering systems, intelligent tutoring systems, and consultation systems $[1, 8, 77, 78, 88]$ . An intelligent interface for document retrieval systems must also exhibit the user modeling capability of experienced human intermediaries. Daniels proposed a frame-based representation for a user model and rules for interacting with the users. She has shown that user modeling is a necessary function in the presearch information interaction $[21]$ . Rich's Grundy system builds models of its users, with the aid of stereotypes, and then uses those models to guide it in its task, suggesting novels that people may find interesting $[67, 68, 69]$ .

Despite their successful and useful application in numerous domains, the development process for knowledge-based systems is often slow and painstaking. Knowledge engineers or system designers need to be able to identify subject and classification knowledge from some sources (usually some domain experts) and to represent the knowledge in computer systems. The inference engines of such systems, which mainly emulate human problem-solving strategies and cognitive processes $[10]$ , may not be applicable across different applications.

## Learning Systems: Neural Networks, Symbolic Learning, and Genetic Algorithms

Contrary to the manual knowledge acquisition process used in knowledge-based systems design, learning systems rely on algorithms to extract knowledge or identify patterns in data. Various statistics-based algorithms have been developed by management scientists and have been used extensively over the past few decades for quantitative data analysis. These algorithms examine quantitative data for the purposes of [58]: (1) clustering descriptors with common characteristics, for example, factor analysis and principal components analysis; (2) hypothesis testing for differences among different populations, for example, t-test and analysis of variance (ANOVA); (3) trend analysis, for example, time series analysis; and (4) correlation between variables, for example, correlation coefficient and linear/multiple regression analysis [27, 56]. These analysis techniques often rely on complex mathematical models, stringent assumptions, or special underlying distributions. The findings are then presented in mathematical formulas and parameters.

## Learning Systems: An Overview

The symbolic machine learning technique, the resurgent neural networks approach, and evolution-based genetic algorithms provide drastically different methods of data analysis and knowledge discovery. These techniques, which are diverse in their origins and behaviors, have shown unique capabilities in analyzing qualitative, symbolic data. We provide a brief overview of these three classes of techniques along with a representative technique for each class below.

\- Symbolic Learning and ID3: Symbolic machine learning techniques, which can be classified based on such underlying learning strategies as rote learning, learning by being told, learning by analogy, learning from examples, and learning from discovery [7], have been studied extensively by AI researchers over the past two decades. Among these techniques, learning from examples, a special case of inductive learning, appears to be the most promising symbolic machine learning technique for knowledge discovery in real databases. It induces a general concept description that best describes the positive and negative examples.

Quinlan's ID3 decision-tree building algorithm and its descendants [63, 64] are simple and yet powerful algorithms for inductive learning. ID3 takes objects of a known class, described in terms of a fixed collection of properties or attributes, and produces a decision tree incorporating these attributes that correctly classifies all the given objects. It uses an information-economics approach aimed at minimizing the expected number of tests to classify an object. Its output can be summarized in terms of IF-THEN rules. ID3 has been used successfully for various classification and prediction applications.

\- Neural Networks and Backpropagation: The foundation of the neural networks paradigm was laid in the 1950s and has attracted significant attention in the past decade due to the development of more powerful hardware and neural algorithms. Nearly all connectionist algorithms have a strong learning component. In symbolic machine learning, knowledge is represented in the form of symbolic descriptions of the learned concepts. In connectionist learning, on the other hand, knowledge is learned and remembered by a network of interconnected neurons, weighted synapses, and threshold logic units [47, 71]. Learning algorithms such as Delta rule can be applied to adjust connection weights so that the network can predict or classify unknown examples correctly.

Among the numerous artificial neural networks that have been proposed recently, Backpropagation networks have been extremely popular for their unique learning capability. Backpropagation networks [72] are fully connected, layered, feedforward models. Activations flow from the input layer through the hidden layer, then to the output layer. A Backpropagation network typically starts out with a random set of weights. The network adjusts its weights each time it sees an input–output pair. Each pair is processed at two stages, a forward pass and a backward pass. The forward pass involves presenting a sample input to the network and letting activations flow until they reach the output layer. During the backward pass, the network's actual output is compared with the target output and error estimates are computed for the output units. The weights connected to the output units are adjusted in order to reduce the errors (a gradient descent method). The error estimates of the output units are then used to derive error estimates for the units in the hidden layer. Finally, errors are propagated back to the connections stemming from the input units. The Backpropagation network updates its weights incrementally until the network stabilizes.

\- Genetic Algorithms and Classifier System: During the past decade there has been a growing interest in algorithms that rely on analogies to natural processes and Darwinian survival of the fittest. The emergence of massively parallel computers made these algorithms of practical interest. The best-known algorithm in this class is probably the classifier system proposed by Holland [5], which represents knowledge in terms of parallel, interconnected production rules.

Genetic algorithms were developed based on the principle of evolution [30, 43, 52]. In such algorithms a population of individuals (potential solutions) undergoes a sequence of unary (mutation) and higher-order (crossover) transformations. These individuals strive for survival: a selection (reproduction)

scheme, biased toward selecting fitter individuals, produces the individuals for the next generation. After some number of generations the program converges—the best individual represents the optimum solution.

Over the past years there have been several studies that compare the performance of these techniques for different applications as well as some systems that use hybrid representations and learning techniques. We summarize some of these studies below.

Mooney et al. [57] found that ID3 was faster than a Backpropagation net, but the Backpropagation net was more adaptive to noisy data sets. The performances of these two techniques were comparable, however. Weiss and Kapouleas [82, 83] suggested using resampling technique such as leave-one-out for evaluation instead of using a holdout testing data set. Discriminant analysis methods, Backpropagation net, and decision tree-based inductive learning methods (like ID3) were found to achieve comparable performance for several data sets. Fisher and McKusick [24] found that using batch learning, Backpropagation performed as well as ID3, but it was more noise-resistant. They also compared the effect of incremental learning versus batch learning. Kitano [41] performed systematic, empirical studies on the speed of convergence of Backpropagation networks and genetic algorithms. The results indicated that genetic search is, at best, equally efficient as faster variants of the Backpropagation algorithm in very small scale networks, but is far less efficient in larger networks. Earlier research by Montana and Davis [55], however, showed that performance was improved by using some domain-specific genetic operators to train the Backpropagation network, instead of the conventional Backpropagation Delta learning rule. Harp et al. [38] also achieved good results by using GAs for neural network design.

Systems developed by Kitano [41] and Harp et al. [38] are also considered hybrid systems (genetic algorithms and neural networks) as are systems like COGIN [35], which performed symbolic induction using genetic algorithms and SC-net [37], which is a fuzzy connectionist expert system. Other hybrid systems developed in recent years employ symbolic and neural net characteristics. For example, Touretzky and Hinton [80] and Gallant [29] proposed connectionist production systems, and Derthick [22] and Shastri [75] developed different connectionist semantic networks. The system reported here is also a hybrid system that utilizes the optimization property of the genetic algorithms and the parallel relaxation capability of the Hopfield neural networks. Details about these methods are presented in the next section.

## Learning Systems in IR

The adaptive learning techniques cited have also drawn attention from researchers in information science. Neural networks computing, in particular, seems to fit well with conventional retrieval models such as the vector space model $[73]$ and the probabilistic model $[49]$ .

Doszkocs et al. [23] provide an excellent overview of the use of connectionist models in information retrieval. These models include several related information-processing approaches, such as artificial neural networks, spreading activation models, associative networks, and parallel distributed processing. In contrast to more conventional information-processing models, connectionist models are “self-processing” in that no external program operates on the network: the network literally processes itself, with “intelligent behavior” emerging from the local interactions that occur concurrently between the numerous network nodes through their synaptic connections. By taking a broader definition of connectionist models, these authors were able to discuss the well-known vector space model, cosine measures of similarity, and automatic clustering and thesaurus in the context of network representation. Based on the network representation, spreading activation methods such as constrained spreading activation adopted in GRANT [18] and the branch-and-bound algorithm adopted in METACAT [10] can be considered as variants of connectionist activation. However, only a few systems are considered classical connectionist systems that typically consist of weighted, unlabeled links and exhibit some adaptive learning capabilities.

The work of Belew is probably the earliest connectionist model adopted in IR. In AIR [2], he developed a three-layer neural network of authors, index terms, and documents. The system used relevance feedback from its users to change its representation of authors, index terms, and documents over time. The result was a representation of the consensual meaning of key words and documents shared by some group of users. One of his major contributions was the use of a modified correlational learning rule. The learning process created many new connections between documents and index terms. Rose and Belew [70] extended AIR to a hybrid connectionist and symbolic system called SCALIR which used analogical reasoning to find relevant documents for legal research. Kwok [44] developed a similar three-layer network of queries, index terms, and documents. A modified Hebbian learning rule was used to reformulate probabilistic information retrieval. Wilkinson and Hingston [84, 85] incorporated the vector space model in a neural network for document retrieval. Their network also consisted of three layers: queries, terms, and documents. They have shown that spreading activation through related terms can help improve retrieval performance.

While the above systems represent information retrieval applications in terms of their main components of document, queries, index terms, authors, and so on, other researchers used different neural networks for more specific tasks. Lin [45] adopted a Kohonen network for information retrieval. Kohonen's feature map, which produced a two-dimensional grid representation for $N$ -dimensional features, was applied to construct a self-organizing (unsupervised learning), visual representation of the semantic relationships between input documents. In [48], a neural algorithm developed by MacLeod was used for document clustering. The algorithm exhibited effectiveness comparable to that of conventional hierarchical clustering algorithms. Chen et al. [12, 13, 15] reported a series of experiments and system developments that generated an automatically created weighted network of key words from large textual databases and integrated it with several existing man-made thesauri (e.g., LCSH). Instead of using a three-layer design, Chen's systems developed a single-layer, interconnected, weighted/labeled network of key words (concepts) for "concept-based" information retrieval. A blackboard-based design that supported browsing and automatic concept exploration using the Hopfield neural network's parallel relaxation method was adopted to facilitate the usage of several thesauri [13].

Despite the popularity of using neural networks for information retrieval, we see only limited use of other adaptive learning techniques. In [4], the researchers used discriminant analysis and a simple symbolic learning technique for document classification. Their symbolic learning process simply represented the numeric classification results in terms of IF-THEN rules. We adopted an ID3 decision-tree building algorithm for information retrieval [16]. For a small test collection of documents, the inductive learning method did a good job in identifying the concepts (key words) that best represent the set of documents identified by users as relevant (positive examples) and irrelevant (negative examples). More testing, however, is under way to determine the effectiveness of example-based document retrieval using ID3.

Our literature search revealed several implementations of genetic algorithms in information retrieval. Gordon [33] presented a genetic algorithms-based approach for document indexing. Competing document descriptions (key words) are associated with a document and altered over time by using genetic mutation and crossover operators. In his design, a key word represents a gene (a bit pattern), a document's list of key words represents individuals (a bit string), and a collection of documents initially judged relevant by a user represents the initial population. Based on a Jaccard's score matching function (fitness measure), the initial population evolved through generations and eventually converged to an optimal (improved) population—a set of key words that best described the documents. Gordon [34] adopted a similar approach to document clustering. His experiment showed that after genetically redescribing the subject description of documents, descriptions of documents found corelevant to a set of queries will bunch together. Redescription improved the relative density of co-relevant documents by 39.74 percent after twenty generations and 56.61 percent after forty generations. Raghavan and Agarwal [66] have also studied the genetic algorithms in connection with document clustering. Petry et al. [59] applied genetic programming to a weighted information retrieval system. In their research, a weighted Boolean query was modified in order to improve recall and precision. They found that the form of the fitness function has a significant effect upon performance. Yang and his coworkers [86, 87] have developed adaptive retrieval methods based on genetic algorithms and the vector space model using relevance feedback. They reported the effect of adopting genetic algorithms in large databases, the impact of genetic operators, and GA's parallel searching capability. Frieder and Siegelmann [28] also reported a data placement strategy for parallel information retrieval systems using a genetic algorithms approach. Their results compared favorably with pseudo-optimal document allocations.

The connectionist approach to IR and Gordon's GAs in IR provided great insight for this research. Specifically, we attempted to investigate in more depth the role of genetic algorithms adaptation for optimizing concept description in example-based document retrieval; we also aimed to integrate the optimization capability of the genetic algorithms with the parallel exploration (search) property of the Hopfield networks. Details about our design are reported below.

WE DESCRIBE HERE IN ALGORITHMIC DETAIL THE GENETIC ALGORITHMS and neural networks adopted in our hybrid system for adaptive information retrieval.

## Genetic Algorithms

Genetic algorithms (GAs) [30, 43, 52] are problem-solving systems based on principles of evolution and heredity. A GA maintains a population of individuals, $P(t) = x_1, \ldots, x_n$ at iteration $t$ . Each individual represents a potential solution to the problem at hand and is implemented as some (possibly complex) data structure $S$ . Each solution $x_i$ is evaluated to give some measure of fitness. Then a new population at iteration $t + 1$ is formed by selecting the fitter individuals. Some members of the new population undergo transformation by means of genetic operators to form new solutions. There are unary transformations $m_i$ (mutation type), which create new individuals by a small change of a single individual and higher-order transformations $c_j$ (crossover type), which create new individuals by combining parts from several (two or more) individuals. For example, if parents are represented by a five-dimensional vector $(a_1, a_2, a_3, a_4, a_5)$ and $(b_1, b_2, b_3, b_4, b_5)$ , then a crossover of chromosomes after the second gene produces offspring $(a_1, a_2, b_3, b_4, b_5)$ and $(b_1, b_2, a_3, a_4, a_5)$ . The control parameters for genetic operators (probability of crossover and mutation) need to be carefully selected to provide better performance. The intuition behind the crossover operation is information exchange between different potential solutions. After some number of generations the program converges—the best individual hopefully represents the optimum solution. Goldberg [30] presents a good summary of many recent GA applications in biology, computer science, engineering, operations research, physical sciences, and social sciences.

Genetic algorithms use a vocabulary borrowed from natural genetics. We would talk about genes (or bits), individuals (chromosomes or bit strings), and population (of individuals). Populations evolve through generations. Our genetic algorithm is executed in the following steps:

## 1. Initialize population and evaluate fitness:

To initialize a population, we need first to decide the number of genes for each individual and the total number of chromosomes (popsize) in the initial population. When adopting GAs in IR, each gene (bit) in the chromosome (bit string) represents a certain keyword or concept. The loci (locations of a certain gene) decide the existence (1, ON) or nonexistence (0, OFF) of a concept. A chromosome represents a document that consists of multiple concepts. The initial population contains a set of documents that are judged relevant by a searcher through relevance feedback. The goal of the GAs is to find an optimal set of documents that best match the searcher's needs (expressed in terms of underlying key words or concepts). An evaluation function for the fitness of each chromosome was selected based on Jaccard's score matching function as used by Gordon [33] for document indexing. The Jaccard's score between two sets $X$ and $Y$ is computed as:

$$
\# (X \cap Y) / \# (X \cup Y),
$$

where $\# (S)$ indicates the cardinality of set $S$ . The Jaccard's score is a common measure of association in information retrieval [81].

## 2. Reproduction (selection):

Reproduction is the selection of a new population with respect to the probability distribution based on the fitness values. Fitter individuals have better chances of getting selected for reproduction [52]. A roulette wheel with slots $(F)$ sized according to the total fitness of the population is defined as follows:

$$
F = \sum_ {i = 1} ^ {\text { popsize }} f i t n e s s (V _ {i}),
$$

where $fitness(V_i)$ indicates the fitness value of chromosome $V_i$ according to the Jaccard's score.

Each chromosome has a certain number of slots proportional to its fitness value. The selection process is based on spinning the wheel popsize times; each time we select a single chromosome for a new population. Obviously, some chromosomes will be selected more than once. This is in accordance with the genetic inheritance: the best chromosomes get more copies, the average stay even, and the worst die off.

## 3. Recombination (crossover and mutation):

Now we are ready to apply the first recombination operator, crossover, to the individuals in the new population. The probability of crossover, $p_{c}$ , gives us the expected number $p_{c} \times popsize$ of chromosomes that should undergo the crossover operation. For each chromosome, we generate a random number r between 0 and 1; if $r < p_{c}$ , then the chromosome is selected for crossover. We then mate selected pairs of chromosomes randomly: for each pair of coupled chromosomes, we generate a random number pos from the range of $(1..m - 1)$ , where m is the total number of genes in a chromosome. The number pos indicates the position of the crossing point. The coupled chromosomes exchanged genes at the crossing point as described earlier.

The next recombination operator, mutation, is performed on a bit-by-bit basis. The probability of mutation, $p_{m}$ , gives us the expected number of mutated bits $p_{m} \times m \times popsize$ . Every bit in all chromosomes of the whole population has an equal chance to undergo mutation, that is, to change from 0 to 1 or vice versa. For each chromosome in the crossovered population and for each bit within the chromosome, we generate a random number r from the range of (0..1); if $r < p_{m}$ , we mutate the bit.

## 4. Convergence:

Following reproduction, crossover, and mutation, the new population is ready for its next generation. The rest of the evolutions are simply cyclic repetitions of the above steps until the system reaches a predetermined number of generations or converges (i.e., no improvement in the overall fitness of the population).

However, due to the unique knowledge representation scheme required of the GAs—binary bit strings—many problems cannot be represented conveniently using GAs. For many applications the most difficult problem is to transform the underlying representation into fixed-length bit strings. Koza [43] observed:

Representation is a key issue in genetic algorithm work because the representation scheme can severely limit the window by which the system observes its worlds. . . . String-based representation schemes are difficult and unnatural for many problems and the need for more powerful representations has been recognized for some time.

In summary, GA representation schemes do not have dynamic variability. The initial selection of string length limits in advance the number of internal states of the system and limits what the system can learn. Another consequence of the representation requirement of GAs is their inability to deal with nontrivial constraints $[52]$ .

In recent years, researchers have suggested using real number instead of bit strings for representation $[52]$ . There have also been attempts to use knowledge-augmented genetic operators for GAs $[36, 55]$ . Goldberg $[31, 32]$ proposed messy GAs to address some of the representation problems. In messy GAs, strings are of variable length. Simple crossover is replaced by two even simpler operators: splice and cut.

When using GAs in IR, the optimized concepts are also severely constrained by the bit strings available in the initial population. That is, the system can only use the key words of the documents supplied by the users to find other relevant documents. Key words that are relevant, but not in the initial document set, will not be considered in GA optimization. In order to address this problem, we propose to incorporate a neural network of related concepts (concept space), which acts as the (mother) nature for the GAs, constantly providing new, useful genes for GA evolution. The optimized genes from one round of GA optimization can call the nature and produce other similar genes. These new genes can then be used in the next round of GA optimization. By using a network of concepts (and some underlying search method), GAs can change their underlying representation dynamically. We hope this will alleviate the fixed-length representation problem of GAs and improve overall optimization.

## Hopfield Networks

An excellent candidate for creating a network of related key words had been proposed by Chen et al. [12, 13], who used an asymmetric similarity function to produce automatic thesauri for different underlying databases. The output was a weighted network of keywords, akin to a single-layered neural network. They also adopted a variant of the Hopfield parallel relaxation procedure for network search [13] and concept clustering [11]. We present here an overview of the Hopfield network and sketch the algorithm we adopted for our hybrid system.

The Hopfield net [39, 79] was introduced as a neural net that can be used as a content-addressable memory. Knowledge and information can be stored in single-layered interconnected neurons (nodes) and weighted synapses (links) and can be retrieved based on the network's parallel relaxation method—nodes are activated in parallel and are traversed until the network reaches a stable state (convergence). It had been used for various classification tasks [47] and was also used recently by the authors in a blackboard-based retrieval system [13].

A weighted network of keywords generated automatically using 3,000 computing-related articles extracted from DIALOG was reported in [12]. These articles were used by a group of researchers specializing in international computing technologies. Most articles were useful for evaluating foreign computing technologies, especially those in the former Soviet Union. Key words and user-specific folders were used extensively in this environment. We adopted this weighted network as the nature for the concepts that may be of interest to users of such database. Our prototype system contained 1,488 nodes (key words) and 44,486 links (probabilities between 0 and 1), for example, (supercomputing 0.275 parallel programming), (parallel programming 0.225 multi-processor) (parallel programming 0.124 supercomputing), and so on.

Our implementation incorporated basic Hopfield net iteration and convergence ideas. However, significant modification was also made to accommodate the unique characteristics for information retrieval, for example, asymmetric link weights and the continuous SIGMOID transformation function. With the optimized output (key words) generated by GAs and the association of key words captured by the network, the Hopfield parallel relaxation algorithm activates neighboring terms, combines weighted links, performs a transformation function (a SIGMOID function, $f_{s}$ ), and determines the outputs of newly activated nodes. The process repeats until node outputs remain unchanged with further iterations. The node outputs then represent the concepts that are strongly related to the initial optimized concepts provided by the GAs. With these dynamically increasing genes (key words), the GAs can perform reproduction and recombination again to produce even better populations. A sketch of the Hopfield net activation algorithm follows:

## 1. Assigning synaptic weights:

The “training” phase of the Hopfield net is completed when the weights have been computed based on the similarity function discussed earlier. $t_{ij}$ represents the “synaptic” weight from node i to node j. Each node represents a gene (key word) in GAs.

## 2. Initialization with optimized GA output:

An initial set of optimized key words $\{S_{1}, S_{2}, \ldots, S_{m}\}$ is provided by the GA procedure. Each node in the network that matches the key words is initialized to have a weight of 1.

$$
\mu_ {i} (0) = x _ {i}, 0 \leq i \leq n - 1.
$$

$\mu_{i}(t)$ is the output of node i at time t and $x_{i}$ , which has a value between 0 and 1, indicates the input pattern for node i.

3. Activation, weight computation, and iteration:

$$
\mu_ {j} (t + 1) = f _ {s} \left[ \sum_ {1 = 0} ^ {n - 1} t _ {i j} \mu_ {i} (t) \right], 0 \leq j \leq n - 1,
$$

where $f_{s}$ is the continuous SIGMOID transformation function as shown below [20, 42].

$$
f _ {s} \left(n e t _ {j}\right) = \frac {1}{1 + \exp \left[ \frac {- \left(n e t _ {j} - \theta_ {j}\right)}{\theta_ {0}} \right.},
$$

where

$$
n e t _ {j} = \sum_ {1 = 0} ^ {n - 1} t _ {i j} \mu_ {i} (t), \theta_ {j}
$$

serves as a threshold or bias and $\theta_{0}$ is used to modify the shape of the SIGMOID function.

This formula shows the parallel relaxation property of the Hopfield net. At each iteration, all nodes are activated at the same time. The weight computation scheme,

$$
n e t _ {j} = \sum_ {1 = 0} ^ {n - 1} t _ {i j} \mu_ {i} (t),
$$

is also a unique characteristic of the Hopfield net algorithm. Based on parallel activation, each newly activated node derives its new weight based on the summation of the products of the weights assigned to its neighbors and their synapses.

\- Convergence:

The above process is repeated until there is no change in terms of output between two iterations, which is accomplished by checking:

$$
\sum_ {j = 0} ^ {n - 1} \mid \mu_ {j} (t + 1) - \mu_ {j} (t) \mid \leq \varepsilon ,
$$

where $\varepsilon$ is the maximal allowable error (a small number). The final output represents the set of terms relevant to the starting key words. Some default threshold values were selected for $(\theta_{j},\theta_{0})$ . More details about threshold selection are discussed later.

## A Hybrid System: GANNET

Gordon [33] adopted GAs to indexing by simultaneously supplying alternative descriptions to the same document and then deriving better descriptions based on GA reproduction and recombination. After forty generations, Jaccard's score improved by about 20 percent. Gordon's research has provided great insight regarding the representation issues for using GAs in IR and he has shown the potential for such a technique. However, we believed we could adopt the same approach for relevance feedback in IR and, even more importantly, that we could combine GAs with the popular neural networks techniques that have been adopted frequently in IR. We hoped that by combining the unique optimization capability of the GAs and the powerful associative exploration property of the neural networks (Hopfield networks, in particular), we could improve IR performance.

Figure 1 shows the overall structure of GANNET. The GAs manipulate input documents and their associated key words to generate an initial set of optimized key words—a process called concept optimization. In the following concept discovery or concept exploration process, this set of key words is then used by the Hopfield network to produce other relevant key words (new genes suggested by the nature). These Hopfield-suggested key words are included in GAs for the next round of concept optimization. The process repeats until there is no further improvement in the overall fitness. During the actual implementation, we improved the GAs by adopting a parameter selection procedure for $p_{c}$ and $p_{m}$ and we improved the Hopfield net procedure by adopting a dynamic threshold for $\theta_{j}$ .

Figure 2 shows a desired behavior of our hybrid design. The un-shaded regions show the potential improvement based on the GAs; the shaded regions show the potential improvement from the Hopfield networks. Gordon's research has shown the gain from GAs after a fixed number of generations—the first un-shaded GAs region. Our iterative GA/HP (HP: Hopfield) cycles aimed to improve the overall fitness by allowing the nature to alter the underlying representations of the GAs and to explore a larger and more relevant search space. We envision that fitness will improve even more significantly using the iterative GANNET cycles and performance will converge over time. Detailed examples and some benchmark testing results are provided in the following sections.

## System Implementation and Evaluation

WE DEVELOPED A PROTOTYPE SYSTEM IN C on a DECStation 5000/120 (25 MIPS workstation, running ULTRIX). A test database of 3,000 articles from DIALOG was used to generate a Hopfield network of 1,488 nodes and 44,486 weighted links. We present a sample session, some implementation details, and the benchmark testing results below.

## Sample Session

In our hybrid system, a key word represents a gene (bit) in GAs or a node in the Hopfield network; a user-selected document represents a chromosome (individual); and a set of user-selected documents represents the initial population.

![](/api/attachments/GERDAJYC/fulltext/images/c2993853accd53b7e1cdcf8542f820e5314c41eabfd4c887792554e5de211b7b.jpg)  
Figure 1. A Proposed Framework  
Genetic Algorithms for Concepts Optimization

The key words used in the set of user-selected documents were first identified to represent the underlying bit strings for the initial population. Each bit represented the same unique key word throughout the complete GAs process. When a key word was present in a document, the bit was set to 1, otherwise it was 0. Each document could then be represented in terms of a sequence of 0s and 1s. The key words of five user-selected documents are presented below. The set of unique concepts present in these sample documents is also summarized—thirty-three key words (genes) in total. Notice that some concepts were folder names assigned by the users (in the format of \*.\*), such as QUERY.OPT folder for query optimization topics, DBMS.AI folder for artificial intelligence and databases topics, KEVIN.HOT folder for “HOT” (current) topics studied by Kevin (a Russian computing researcher).  
Input Documents and Key Words

<table><tr><td>DOC0</td><td>DATA RETRIEVAL, DATABASE, COMPUTER NETWORKS, IMPROVEMENTS, INFORMATION RETRIEVAL, METHOD, NETWORK, MULTIPLE, QUERY, RELATION, RELATIONAL, RETRIEVAL, QUERIES, RELATIONAL DATABASES, RELATIONAL DATABASE, US, CARAT.DAT, GQP.DAT, ORUS.DAT, QUERY.OPT</td></tr><tr><td>DOC1</td><td>INFORMATION, INFORMATION RETRIEVAL, INFORMATION STORAGE, INDEXING, RETRIEVAL, STORAGE, US, KEVIN.HOT</td></tr><tr><td>DOC2</td><td>ARTIFICIAL INTELLIGENCE, INFORMATION RETRIEVAL SYSTEMS, INFORMATION RETRIEVAL, INDEXING, NATURAL LANGUAGE PROCESSING, US, DBMS.AI, GQP.DAT</td></tr><tr><td>DOC3</td><td>FUZZY SET THEORY, INFORMATION RETRIEVAL SYSTEMS, INDEXING, PERFORMANCE, RETRIEVAL SYSTEMS, RETRIEVAL, QUERIES, US, KEVIN.HOT</td></tr><tr><td>DOC4</td><td>INFORMATION RETRIEVAL SYSTEMS, INDEXING, RETRIEVAL, STAIRS, US, KEVIN.HOT</td></tr></table>

## Total Set of Concepts

DATA RETRIEVAL, DATABASE, COMPUTER NETWORKS, IMPROVEMENTS, INFORMATION RETRIEVAL, METHOD, NETWORK, MULTIPLE, QUERY, RELATION, RELATIONAL, RETRIEVAL, QUERIES, RELATIONAL DATABASES, RELATIONAL DATABASE, US, CARAT.DAT, GQP.DAT, ORUS.DAT, QUERY.OPT, INFORMATION,

![](/api/attachments/GERDAJYC/fulltext/images/3442d1f30d250cf78c6cef7cf7aa9e00938e8421efbb1a163dae50527528280c.jpg)  
Figure 2. Ideal Fitness Improvement using GANNET

INFORMATION STORAGE, INDEXING, STORAGE, KEVIN.HOT, ARTIFICIAL INTELLIGENCE, INFORMATION RETRIEVAL SYSTEMS, NATURAL LANGUAGE PROCESSING, DBMS.AI, FUZZY SET THEORY, PERFORMANCE, RETRIEVAL SYSTEMS, STAIRS,

Initial Genetic Pattern of Chromosome in Population

<table><tr><td>chromosome</td><td>fitness</td></tr><tr><td>11111111111111111110000000000000</td><td>[0.287744]</td></tr><tr><td>000010000001000100001111100000000</td><td>[0.411692]</td></tr><tr><td>000010000000000101000010011110000</td><td>[0.367556]</td></tr><tr><td>000000000001100100000010101001110</td><td>[0.427473]</td></tr><tr><td>000000000001000100000010101000001</td><td>[0.451212]</td></tr></table>

Average fitness = 0.3891

We computed the fitness of each document based on its relevance to other documents in the user-selected set. As discussed earlier, we adopted the same Jaccard's score matching function used in [33]. Higher Jaccard's score (a value between 0 and 1) indicated stronger relevance between two documents. For document 0, we computed five different Jaccard's scores between document 0 and documents 0, 1, 2, 3, and 4, respectively (shown below). An average fitness was then computed for document 0 (0.28774). The same procedure was applied to other documents to compute their fitesses. A document that included more concepts shared by other documents had a higher Jaccard's score.

Jaccard's Score of DOC0 and DOC0 = 1.000000

Jaccard's Score of DOC0 and DOC1 = 0.120000

Jaccard's Score of DOC0 and DOC2 = 0.120000

Jaccard's Score of DOC0 and DOC3 = 0.115384

Jaccard's Score of DOC0 and DOC4 = 0.083333

Average fitness (Jaccard's Score) of Document0: 0.28774

If a user provides documents that are closely related, the average fitness for the complete document set will be high. If the user-selected documents are only loosely related, their overall fitness will be low. Generally, GAs did a good job optimizing a document set that was initially low in fitness. Using the previous example, the overall Jaccard's score increased over generations. The optimized population contained only one single chromosome, with an average fitness value of 0.45121. The optimized chromosome contained six relevant key words that best described the initial set of documents.

Optimized Chromosomes in the Population

<table><tr><td>chromosome</td><td>fitness</td></tr><tr><td>000000000001000100000010101000001</td><td>[0.45121]</td></tr><tr><td>000000000001000100000010101000001</td><td>[0.45121]</td></tr><tr><td>000000000001000100000010101000001</td><td>[0.45121]</td></tr><tr><td>0000800000001000100000010101000001</td><td>[0.45121]</td></tr><tr><td>000000000001000100000010101000001</td><td>[0.45121]</td></tr><tr><td>0000000000001000100000010101000001</td><td>[0.45121]</td></tr></table>

Average fitness = 0.4512

Derived Concepts from Optimized Population

RETRIEVAL, US, INDEXING, KEVIN.HOT, INFORMATION RETRIEVAL SYSTEMS, STAIRS,

In our initial implementation, we adopted a standard GA procedure incorporating a fixed number of generations (40) and empirically selected $p_{c}$ and $p_{m}$ probabilities. Because the application of the GAs was basically a random, parallel search process, its performance was affected strongly by the control parameters, especially $p_{c}$ and $p_{m} - p_{c}$ exploited the search space by using the fitter individuals while $p_{m}$ explored the search space by randomly mutating bits [52]. Figure 3a shows the fitness deterioration and figure 3b shows the fitness improvement when using different initial populations and $p_{c}$ and $p_{m}$ . In most cases, fitness increased and converged to a certain level after about ten generations, but in some cases average fitness decreased, as shown in figure 3a.

According to past research [52, 74], GAs lack robust heuristics to determine good values for their parameters. Typically $P_{m}$ is much smaller than $P_{c}$ and GAs often converge quickly after the first several generations. Based on these observations, we adopted a revised GA that performed short cycles (each cycle contained ten generations) of evolution. At each cycle GANNET adopted various combinations of $p_{c}$ and $p_{m}$ values to form candidate populations, and selected the best population among these candidates for the next cycle. If fitness improved in a given cycle, GANNET incremented $p_{m}$ for the next cycle in an attempt to explore the search space fully and to avoid a local minimum. The process terminated when the fitness no longer improved in two consecutive processing cycles. In essence, this variant GA performed reproduction using a smaller number of generations and dynamically changing parameters in order to exploit and explore the search space fully.

As shown in figure 4 (each line represents a different $p_{c}$ and $p_{m}$ combination), fitness improved significantly in the first cycle. The best population produced from Cycle 1 was used in Cycle 2 for further optimization using different $p_{c}$ and $p_{m}$ values. The optimization process converged after four cycles. In our experiment, most test cases converged after about six cycles. Typical $p_{c}$ selected ranged between 0.7 and 0.9 and $p_{m}$ ranged between 0.01 and 0.03.

(a)  
![](/api/attachments/GERDAJYC/fulltext/images/b1b4049e66e374cd75161775d0cf28667fb4672aa7963930360ebaa0e1dcf469.jpg)

![](/api/attachments/GERDAJYC/fulltext/images/f0855d6af02c63633e24e95767ae1a3d22667f7d3a049b533f7a3e30cd151c7e.jpg)  
Figure 3. Examples of Fitness Variation using GAs (each line represents a test run with $p_{c}$ and $p_{m}$ )

## Hopfield Net for Concept Discovery

After concepts were optimized by GAs, they were used as input to the Hopfield network to activate other relevant concepts. The overall Hopfield network activation sensitivity was mainly controlled by two threshold values, $\theta_{0}$ and $\theta_{j}$ . In our implementation, we fixed the $\theta_{0}$ value at 0.0, that is, no threshold, and we changed the $\theta_{j}$ values to obtain different levels of activation. As shown in figure 5, the number of concepts generated by the Hopfield network was inversely determined by the $\theta_{j}$ threshold (each line represents a different test case).

For the concepts identified by the Hopfield network, the ones that were activated by higher threshold tended to be more relevant to the initial concepts. In order to prevent dilution of the original concepts by less relevant concepts, good threshold values needed to be carefully selected. We adopted some empirical heuristics based on our experimentation. Because the number of activated concepts increased exponentially when we decreased the threshold value, we gradually decreased $\theta_{j}$ . When a new $\theta_{j}$ produced more than three new concepts, GANNET terminated the Hopfield network activation process. This ad hoc procedure allowed us to identify a reasonable set of related key words from the Hopfield network.

![](/api/attachments/GERDAJYC/fulltext/images/40f993f21819a2f82833628c5b200040b93503e6a46f7d31b54421ba19e228c7.jpg)

![](/api/attachments/GERDAJYC/fulltext/images/a7f6e7c858510d3355977109bbaa9d9ce8843508aa35bf11514a58c9e365b496.jpg)

![](/api/attachments/GERDAJYC/fulltext/images/367b250a5e987fd894b0df5a0d0a591fc95cad06d9be0289a3f9aa8f97317a7b.jpg)

![](/api/attachments/GERDAJYC/fulltext/images/10f6c6133c17bebebb533e38518afd4b02ce7c3203461559ddbf6802d6a380b9.jpg)  
Fitness Improvement in Cycles Using Different $P_{c}$ and $P_{m}$  
represents a different $p_c$ and $p_m$ combination; fitness improved significantly in cycle 1)

![](/api/attachments/GERDAJYC/fulltext/images/4eb6a072f4da00425a7a4887503763691db6a85434ef7cf60fe69b4fbb8cd63b.jpg)  
Figure 5. Activated Concepts as a Function of $\theta_{j}$  
(each line represents a different test case; the number of concepts generated was inversely determined by $\theta_{j}$ )

As shown below using the same example, GANNET proceeded to the Hopfield network activation process with the output generated from GAs, that is, the optimized key words: RETRIEVAL, US, INDEXING, KEVIN.HOT, INFORMATION RETRIEVAL SYSTEMS, STAIRS. By decrementing $\theta_{j}$ values from 0.18, the final threshold value was selected at 0.08. Three other related concepts were identified, namely, INFORMATION, INFORMATION RETRIEVAL, and THESAURI.

Input Concepts to Hopfield Neural Network

RETRIEVAL, US, INDEXING, KEVIN.HOT, INFORMATION RETRIEVAL SYSTEMS, STAIRS

Activated Concepts in Hopfield Net

<table><tr><td>Threshold value = 0.20</td><td>0 Concepts activated</td></tr><tr><td>Threshold Value = 0.19</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.18</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.17</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.16</td><td>0 Concepts activated</td></tr></table>

<table><tr><td>Threshold value = 0.15</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.14</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.13</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.12</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.11</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.10</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.09</td><td>3 Concepts activated</td></tr><tr><td>Threshold value = 0.08</td><td>7 Concepts activated</td></tr><tr><td>Stopping threshold value = 0.09</td><td></td></tr><tr><td>Activated concepts = INFORMATION</td><td>INFORMATION RETRIEVAL</td></tr></table>

Total Set of Concepts from GA/HP

INFORMATION, INFORMATION RETRIEVAL, THESAURI, RETRIEVAL, US, INDEXING, KEVIN.HOT, INFORMATION RETRIEVAL SYSTEMS, STAIRS,

After the concept discovery procedure, we then retrieved the set of documents which contained at least one new Hopfield-activated key word. This simple process generated a lot of documents as candidates. Our experiment showed that in order to retain relevant documents and for computational reason, the appropriate number of documents to include for the next GA procedure was between five and fifteen. In order to adopt only highly relevant documents, we compared the Jaccard's scores of the candidate documents. As shown in the example below, the number of candidate documents generated was 2,628. GANNET computed the Jaccard's score of each document and used the optimized fitness value from the prior GA process (0.4512) to retrieve documents. Four documents were selected. In order to identify more documents (such that the total number of selected documents was between five and fifteen), GANNET lowered the Jaccard's cutoff by 0.05 in order to identify more documents that had a fitness value greater than 0.3512. When a desired number of documents was obtained, GANNET retrieved these documents and used them as the chromosomes of the population in the next round of concept optimization (GA) and concept exploration (HP). In this example, fourteen documents were retrieved for the next GA/HP process. This GA/HP cycle was repeated until there was no more fitness improvement from the process—that is, the process converged.

```txt
Jaccard's Score of Documents
Number of selected text = 2,628
Average Jaccard's fitness = 0.079001
Max. Jaccard's score = 0.6667
Fitness threshold = 0.4512 → Number of selected document = 4
Fitness threshold = 0.4012 → Number of selected document = 4
Fitness threshold = 0.3512 → Number of selected document = 14
```

Selected Documents and Key Words

<table><tr><td>DOC0</td><td>AAIS, HELP, INFORMATION, INFORMATION RETRIEVAL, INDEXING, RETRIEVAL, US, AAIS.SYS, CARAT.DAT, +</td></tr><tr><td>DOC1</td><td>INFORMATION, INFORMATION RETRIEVAL, INDEXING, SEMANTIC RELATIONSHIPS, THESAURI, GE, KEVIN.HOT, +</td></tr><tr><td>DOC2</td><td>CLASSIFICATION, INFORMATION, INDEX TERMS, INFORMATION RETRIEVAL, INDEXING, QUERY LANGUAGES, THESAURI, UR, KEVIN.HOT, +</td></tr><tr><td>DOC3</td><td>INFORMATION, INFORMATION RETRIEVAL, INFORMATION STORAGE, INDEXING, RETRIEVAL, STORAGE, US, KEVIN.HOT, +</td></tr><tr><td>DOC4</td><td>EXPERT, INFORMATION, INFORMATION RETRIEVAL SYSTEMS, GB, KEVIN.HOT, INFORMATION RETRIEVAL, INDEXING, RETRIEVAL, SORTING, +</td></tr><tr><td>DOC5</td><td>INFORMATION RETRIEVAL, INDEXING, THESAURI, UR, KEVIN.HOT, +</td></tr><tr><td>DOC6</td><td>INFORMATION RETRIEVAL, INDEXING, THESAURI, HU, KEVIN.HOT, +</td></tr><tr><td>DOC7</td><td>INFORMATION RETRIEVAL SYSTEMS, INFORMATION RETRIEVAL, MEDICAL LITERATURE, US, KEVIN.HOT, +</td></tr><tr><td>DOC8</td><td>INFORMATION RETRIEVAL, INDEXING, FR, UK, US, KEVIN.HOT, +</td></tr><tr><td>DOC9</td><td>DATABASE, HIGH LEVEL LANGUAGES, INFORMATION RETRIEVAL SYSTEMS, INFORMATION RETRIEVAL, INDEXING, SOCIAL SCIENCES, CA, US, KEVIN.HOT, +</td></tr><tr><td>DOC10</td><td>DATA RETRIEVAL, INFORMATION RETRIEVAL, INDEXING, US, KEVIN.HOT, +</td></tr><tr><td>DOC11</td><td>INFORMATION RETRIEVAL SYSTEMS, THESAURI, UK, US, KEVIN.HOT, +</td></tr><tr><td>DOC12</td><td>FUZZY SET THEORY, INFORMATION RETRIEVAL SYSTEMS, INDEXING, PERFORMANCE, RETRIEVAL SYSTEMS, RETRIEVAL, QUERIES, US, KEVIN.HOT, +</td></tr><tr><td>DOC13</td><td>INFORMATION RETRIEVAL SYSTEMS, INDEXING, RETRIEVAL, STAIRS, US, KEVIN.HOT, +</td></tr></table>

## A Complete Session

Another complete example of the GA/HP cycles is shown below:

<table><tr><td>DOC 0</td><td>PARALLELISM, WARREN ABSTRACT MACHINE, US, PETER.HOT,</td></tr><tr><td>DOC 1</td><td>LOGIC PROGRAMMING, PARALLELISM, PARALLEL PROCESSING, PETER.HOT, PARALLEL PROGRAMMING, WARREN ABSTRACT MACHINE, US</td></tr><tr><td>DOC 2</td><td>LOGIC, PARALLEL, MULTIPROCESSOR, SUN, WORKSTATION, PETER.HOT, WARREN ABSTRACT MACHINE, US</td></tr></table>

## Total Set of Concepts

PARALLELISM, WARREN ABSTRACT MACHINE, US, PETER.HOT, LOGIC PRO-

GRAMMING, PARALLEL PROCESSING, PARALLEL PROGRAMMING, LOGIC, PARALLEL, MULTIPROCESSOR, SUN, WORKSTATION,

Initial Genetic Pattern of Chromosomes in Population

<table><tr><td>chromosome</td><td>fitness</td></tr><tr><td>111100000000</td><td>[0.634921]</td></tr><tr><td>111111100000</td><td>[0.607143]</td></tr><tr><td>011100011111</td><td>[0.527778]</td></tr></table>

Average fitness = 0.5899

Optimized Genetic Pattern of Population

<table><tr><td>chromosome</td><td>fitness</td></tr><tr><td>111100000000</td><td>[0.63492]</td></tr><tr><td>111100000000</td><td>[0.63492]</td></tr><tr><td>111100000000</td><td>[0.63492]</td></tr><tr><td>111100000000</td><td>[0.63492]</td></tr><tr><td>111100000000</td><td>[0.63492)</td></tr><tr><td>111100000000</td><td>[0.63492]</td></tr></table>

Average fitness = 0.6349

Derived Concepts from Optimized Population

PARALLELISM, WARREN ABSTRACT MACHINE, US, PETER.HOT

Activated Concepts in Hopfield Net

<table><tr><td>Threshold value = 0.25</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.24</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.23</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.22</td><td>0 Concepts activated</td></tr><tr><td>Threshold value = 0.21</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.20</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.19</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.18</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.17</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.16</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.15</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.14</td><td>1 Concepts activated</td></tr><tr><td>Threshold value = 0.13</td><td>23 Concepts activated</td></tr></table>

Stopping threshold value = 0.14

Activated concepts = PARALLEL PROGRAMMING

## Total Set of Concepts from GA/HP

PARALLEL PROGRAMMING, PARALLELISM, WARREN ABSTRACT MACHINE, US, PETER.HOT,

... Repetition of the GA/HP procedures ...

<table><tr><td colspan="3">Jaccard&#x27;s Score of Documents</td></tr><tr><td colspan="3">Number of selected text = 2,731</td></tr><tr><td colspan="3">Average Jaccard&#x27;s fitness = 0.097456</td></tr><tr><td colspan="3">Max. Jaccard&#x27;s score = 0.8000</td></tr><tr><td>Fitness threshold = 0.6349 →</td><td colspan="2">Number of selected document = 2</td></tr><tr><td>Fitness threshold = 0.5849 →</td><td colspan="2">Number of selected document = 3</td></tr><tr><td>Fitness threshold = 0.5349 →</td><td colspan="2">Number of selected document = 3</td></tr><tr><td>Fitness threshold = 0.4849 →</td><td colspan="2">Number of selected document = 13</td></tr></table>

<table><tr><td colspan="2">Final Selected Documents and Key Words</td></tr><tr><td>DOC 0</td><td>PARALLEL PROGRAMMING, SYNCHRONISATION, US, PETER.HOT,</td></tr><tr><td>DOC 1</td><td>PROGRAM DEBUGGING, PARALLEL PROGRAMMING, US, PETER.HOT,</td></tr><tr><td>DOC 2</td><td>PARALLEL PROGRAMMING, SOFTWARE TOOL, US, PETER.HOT,</td></tr><tr><td>DOC 3</td><td>PARALLEL PROGRAMMING, SOFTWARE TOOL, US, PETER.HOT,</td></tr><tr><td>DOC 4</td><td>PARALLEL PROGRAMMING, PETRI NET, US, PETER.HOT,</td></tr><tr><td>DOC 5</td><td>PARALLEL PROGRAMMING, VERIFICATION, US, PETER.HOT,</td></tr><tr><td>DOC 6</td><td>PARALLEL PROCESSING, PARALLEL PROGRAMMING, US, PETER.HOT,</td></tr><tr><td>DOC 7</td><td>PARALLEL PROGRAMMING, MULTIPROCESSOR, US, PETER.HOT,</td></tr><tr><td>DOC 8</td><td>DEBUGGING, PARALLEL PROGRAMMING, US, PETER.HOT,</td></tr><tr><td>DOC 9</td><td>PARALLEL PROGRAMMING, MULTIPROCESSOR, US, PETER.HOT,</td></tr><tr><td>DOC 10</td><td>PARALLEL PROGRAMMING, SOFTWARE TOOL, US, PETER.HOT,</td></tr><tr><td>DOC 11</td><td>PARALLEL PROGRAMMING, US, PETER.HOT,</td></tr><tr><td>DOC 12</td><td>PARALLEL PROGRAMMING, QUICKSEARCH, US, PETER.HOT,</td></tr></table>

The initial fitness of the three documents was 0.5899. After the first GA procedure, the fitness increased to 0.6349. The optimized concepts were sent to HP to find PARALLEL PROCESSING. This new key word was then used to identify more relevant documents and the GA/HP process continued. As shown in figure 6, as a result of optimizing the output from HP using GA—that is, a HP/GA cycle (HP followed by GA)—fitness improved over cycles and eventually converged after three HP/GA cycles (converged fitness: 0.7675). This finding was consistent with our desired level of fitness improvement using the proposed hybrid architecture as shown in figure 2.

## Evaluation Results

Table 1 summarizes the results from our benchmark testing. In the testing we randomly retrieved five test cases of 1-document, 2-document, 3-document, 4-document, 5-document, and 10-document examples, respectively, from the 3,000-document database. There were thirty test cases in total. For each test case, an initial fitness based on the Jaccard's score was computed. For 1-document and 2-document test cases, their initial fitness tended to be higher due to the smaller sample size (see column 2 of Table 1).

![](/api/attachments/GERDAJYC/fulltext/images/a924dfc4161d5361aa49d0247d353cfac4de8f278ea9ab21056942f7103e3bdd.jpg)  
Figure 6. Sample Fitness Improvement in GA/HP Cycles  
(fitness improved over cycles and eventually converged after three GA/HP cycles)

In Table 1, we also report important performance measures in terms of the Jaccard's scores for the first GA and the final HP/GA (converged) processes, the CPU times, and the average improvements in fitness. The important findings are summarized as follows:

1. Using the basic GA optimization process without the Hopfield activation component, our system achieved an average fitness improvement from 5.38 percent to 17.7 percent. This finding was consistent with the performance improvement for indexing reported by Gordon [33].

Another interesting observation was that when more initial documents were present, the initial fitness tended to be lower, which allowed the system to do a better job in improving the precision of the initial key words and in identifying other relevant documents. As shown in Table 1, fitness improvement increased as a function of the number of initial documents, from 5.38 percent to 17.7 percent. This finding also suggested that when initial user-supplied documents are fuzzy and not well articulated, GAs will be able to make a more significant contribution in suggesting other relevant documents. This could be quite important for complex information retrieval sessions during which searchers need help in query articulation and search refinement.

The number of documents suggested by GANNET after the first GA process was between 9 and 13, with an average of about 11 documents. The CPU times required of the first GA process was also quite reasonable, with an average of 0.168 seconds.

2. With the repetitive HP/GA cycles, the overall fitness improved even more. On an average, the Jaccard's score improved from the GA's 0.5511 to a final HP/GA score of about 0.6655. The average fitness improvement over the initial score went from

7.19 percent for the initial GA to 47.79 percent for the repetitive HP/GA. This finding confirmed the power of adopting our hybrid GA-HP architecture. Similar to the finding in GA optimization, GANNET improved the fitness more when the initial number of documents was small and/or when the initial documents were not strongly related.

The average number of documents suggested by GANNET was about ten, similar to that suggested by GA alone. But the CPU time required averaged at 2.46 seconds, which was significantly longer than the first GA process. This result was expected due to the extensive computational effort required of our design. On average, GANNET performed about five HP/GA cycles in order to reach a “global” convergence.

The system essentially performed an incremental, evolutionary leap by executing a GA optimization using the genes presented by one population, calling the nature for more related genes, executing another GA optimization using the newer set of genes, calling the nature again, until finally even the nature cannot improve the population. In figure 7 we present a graphic display of the fitness improvement over HP/GA cycles for the thirty test cases.

## Conclusion

INFORMATION RETRIEVAL RESEARCH HAS BEEN ADVANCING VERY QUICKLY over the past few decades. Researchers have experimented with techniques ranging from probabilistic models and the vector space model, to a knowledge-based approach and recent machine learning techniques. At each stage, significant insights regarding how to design more useful and “intelligent” information retrieval systems have been gained.

We have presented an extensive review of IR research which was mainly based on machine learning techniques. Connectionist modeling and learning, in particular, has attracted considerable attention due to its strong resemblance to some existing IR models and techniques. Symbolic machine learning and genetic algorithms, two popular candidates for adaptive learning in other applications, on the other hand, have only been used occasionally. Based on Gordon's research using GAs in adaptive indexing, we explored the idea of using GAs in adaptive IR and further expanded the static GA representation to a hybrid architecture that contained both a GA concept optimization component and a Hopfield network-based concept exploration component.

Our hybrid prototype system, GANNET, performed an iterative GA-HP concept optimization and exploration process in order to evolve in a larger search space. Our benchmark testing results confirmed the power of using GAs alone, with an average fitness improvement of about 7 percent. But when using the complete GANNET cycles, fitness improved even more significantly to about 48 percent.

We believe this research has shed light on the usefulness of adopting both genetic algorithms and neural networks in an integrated framework for adaptive information retrieval. By combining the robust optimization characteristic of the genetic algorithms and the associative property of the Hopfield network, an information retrieval system can analyze the user-supplied evidence and “learn” from the users. We envision the proposed design being incorporated in a truly interactive retrieval environment in which users can continuously provide relevance feedback and the system can adapt to the users' needs.

Table 1 System Benchmark Testing Results

<table><tr><td>No.</td><td>rel.</td><td>First GA score</td><td>Impr. %</td><td>CPU (sec.)</td><td>Slcted. doc.</td><td>Final HP/GA score</td><td>Impr. %</td><td>CPU (sec.)</td><td>Slcted. doc.</td><td>HP/GA cycle</td></tr><tr><td colspan="11">1 doc</td></tr><tr><td>1</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.067</td><td>7</td><td>1.0</td><td>0.0</td><td>2.033</td><td>5</td><td>6</td></tr><tr><td>2</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.05</td><td>25</td><td>0.7214</td><td>-27.9</td><td>0.983</td><td>7</td><td>5</td></tr><tr><td>3</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.067</td><td>7</td><td>0.5058</td><td>-49.4</td><td>1.45</td><td>9</td><td>4</td></tr><tr><td>4</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.05</td><td>9</td><td>0.7857</td><td>-21.4</td><td>1.45</td><td>7</td><td>6</td></tr><tr><td>5</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.067</td><td>5</td><td>0.8353</td><td>-16.5</td><td>1.15</td><td>17</td><td>6</td></tr><tr><td></td><td>avg.</td><td>1.0</td><td>0.0</td><td>0.06</td><td>10.6</td><td>0.7696</td><td>-23</td><td>1.41</td><td>9</td><td>5.4</td></tr><tr><td colspan="11">2 doc</td></tr><tr><td>1</td><td>0.5139</td><td>0.5139</td><td>0.0</td><td>0.083</td><td>10</td><td>0.7722</td><td>50.3</td><td>0.75</td><td>6</td><td>4</td></tr><tr><td>2</td><td>0.5833</td><td>0.5833</td><td>0.0</td><td>0.1</td><td>8</td><td>0.4611</td><td>-20.9</td><td>5.26</td><td>5</td><td>5</td></tr><tr><td>3</td><td>0.6111</td><td>0.6111</td><td>0.0</td><td>0.083</td><td>5</td><td>0.6140</td><td>0.5</td><td>1.32</td><td>5</td><td>5</td></tr><tr><td>4</td><td>0.6486</td><td>0.6486</td><td>0.0</td><td>0.067</td><td>10</td><td>0.5211</td><td>-19.7</td><td>4.42</td><td>5</td><td>8</td></tr><tr><td>5</td><td>0.7857</td><td>0.7857</td><td>0.0</td><td>0.083</td><td>16</td><td>0.7692</td><td>-2.1</td><td>1.07</td><td>13</td><td>5</td></tr><tr><td></td><td>avg.</td><td>0.6285</td><td>0.0</td><td>0.08</td><td>9.8</td><td>0.6275</td><td>1.62</td><td>2.56</td><td>6.8</td><td>5.4</td></tr><tr><td colspan="11">3 doc</td></tr><tr><td>1</td><td>0.3841</td><td>0.3984</td><td>3.72</td><td>0.023</td><td>8</td><td>0.6963</td><td>81.3</td><td>0.83</td><td>6</td><td>4</td></tr><tr><td>2</td><td>0.4157</td><td>0.4360</td><td>4.88</td><td>0.1</td><td>5</td><td>0.5202</td><td>25.1</td><td>1.53</td><td>5</td><td>6</td></tr><tr><td>3</td><td>0.4286</td><td>0.4611</td><td>7.1</td><td>0.1</td><td>13</td><td>0.5609</td><td>30.9</td><td>1.21</td><td>9</td><td>5</td></tr><tr><td>4</td><td>0.5032</td><td>0.5215</td><td>3.6</td><td>0.133</td><td>5</td><td>0.5591</td><td>11.1</td><td>3.08</td><td>10</td><td>5</td></tr><tr><td>5</td><td>0.5899</td><td>0.6349</td><td>7.6</td><td>0.083</td><td>16</td><td>0.7692</td><td>30.4</td><td>0.783</td><td>13</td><td>4</td></tr><tr><td></td><td>avg.</td><td>0.4904</td><td>5.38</td><td>0.088</td><td>9.4</td><td>0.6211</td><td>35.76</td><td>1.49</td><td>8.6</td><td>4.8</td></tr><tr><td colspan="11">4 doc</td></tr><tr><td>1</td><td>0.2898</td><td>0.3010</td><td>3.8</td><td>0.117</td><td>22</td><td>1.0</td><td>245.1</td><td>3.197</td><td>17</td><td>4</td></tr><tr><td>2</td><td>0.3078</td><td>0.3142</td><td>2.1</td><td>0.1</td><td>15</td><td>0.5289</td><td>71.8</td><td>4.13</td><td>12</td><td>5</td></tr><tr><td>3</td><td>0.3194</td><td>0.3495</td><td>9.4</td><td>0.283</td><td>5</td><td>0.4695</td><td>46.1</td><td>1.6</td><td>8</td><td>6</td></tr><tr><td>4</td><td>0.3319</td><td>0.3442</td><td>3.7</td><td>0.25</td><td>11</td><td>0.6609</td><td>99.1</td><td>1.83</td><td>5</td><td>4</td></tr><tr><td>5</td><td>0.4409</td><td>0.5060</td><td>14.7</td><td>0.25</td><td>10</td><td>1.0000</td><td>126.8</td><td>2.08</td><td>5</td><td>4</td></tr><tr><td></td><td>avg.</td><td>0.3629</td><td>6.74</td><td>0.2</td><td>12.6</td><td>0.7319</td><td>117.8</td><td>2.57</td><td>9.4</td><td>4.6</td></tr><tr><td colspan="11">5 doc</td></tr><tr><td>1</td><td>0.3048</td><td>0.3370</td><td>10.5</td><td>0.4</td><td>12</td><td>0.4655</td><td>52.7</td><td>9.58</td><td>8</td><td>6</td></tr><tr><td>2</td><td>0.3068</td><td>0.3267</td><td>6.4</td><td>0.15</td><td>7</td><td>0.4538</td><td>47.9</td><td>1.28</td><td>13</td><td>3</td></tr><tr><td>3</td><td>0.3194</td><td>0.3575</td><td>11.9</td><td>0.52</td><td>5</td><td>0.5387</td><td>68.7</td><td>2.97</td><td>10</td><td>3</td></tr><tr><td>4</td><td>0.4655</td><td>0.5671</td><td>21.8</td><td>0.3</td><td>21</td><td>1.0000</td><td>114.8</td><td>3.32</td><td>17</td><td>4</td></tr><tr><td>5</td><td>0.6181</td><td>0.7171</td><td>16.0</td><td>0.12</td><td>21</td><td>1.0000</td><td>61.8</td><td>4.64</td><td>17</td><td>4</td></tr><tr><td></td><td>avg.</td><td>0.4610</td><td>13.32</td><td>0.298</td><td>13.2</td><td>0.6916</td><td>69.18</td><td>4.36</td><td>13</td><td>4</td></tr><tr><td colspan="11">10 doc</td></tr><tr><td>1</td><td>0.2489</td><td>0.2824</td><td>13.5</td><td>0.32</td><td>18</td><td>0.3057</td><td>22.8</td><td>5.48</td><td>31</td><td>4</td></tr><tr><td>2</td><td>0.2038</td><td>0.2282</td><td>12.9</td><td>0.35</td><td>8</td><td>0.4524</td><td>122.0</td><td>2.3</td><td>9</td><td>6</td></tr><tr><td>3</td><td>0.2016</td><td>0.2343</td><td>16.2</td><td>0.47</td><td>6</td><td>0.4367</td><td>116.6</td><td>2.5</td><td>6</td><td>3</td></tr><tr><td>4</td><td>0.4997</td><td>0.6201</td><td>24.1</td><td>0.13</td><td>5</td><td>0.7905</td><td>58.2</td><td>0.63</td><td>5</td><td>3</td></tr><tr><td>5</td><td>0.3727</td><td>0.4540</td><td>21.8</td><td>0.13</td><td>11</td><td>0.7722</td><td>107.2</td><td>0.983</td><td>6</td><td>4</td></tr><tr><td></td><td>avg.</td><td>0.3638</td><td>17.7</td><td>0.28</td><td>9.6</td><td>0.5515</td><td>85.36</td><td>2.38</td><td>11.4</td><td>4</td></tr><tr><td></td><td>AVG.</td><td>0.5511</td><td>7.19</td><td>0.168</td><td>10.87</td><td>0.6655</td><td>47.79</td><td>2.46</td><td>9.7</td><td>4.7</td></tr></table>

![](/api/attachments/GERDAJYC/fulltext/images/ef31effd51c9dd90dff32e27953f711cdc2cb33a04a0b3056d0296974614a27a.jpg)  
Figure 7. Fitness Improvement in Benchmark Testing (each line represents a different test case)

For future research, we plan to examine the feasibility of adopting weighted bit string (0..1) instead of the original 0/1 values for GAs. By assigning weights to each key word (gene) (e.g., using the term frequency and inverse document frequency [73]), a system may be able to better delineate between good genes (concepts, key words) and bad genes. Another research direction will involve incorporating more natures into the hybrid system. By incorporating more sources of knowledge (i.e., multiple thesauri) [13], we believe GANNET will be able to make more significant adjustments to its underlying representation and thus make a bigger and better evolutionary leap.

## REFERENCES

1. Appelt, D. The role of user modelling in language generation and communication planning. In User Modelling Panel, Proceedings of the Ninth International Joint Conference on Artificial Intelligence, Los Angeles, August 1985, pp. 1298–1302.

2. Belew, R.K. Adaptive information retrieval. In Proceedings of the Twelfth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Cambridge, MA, June 25–28, 1989, pp. 11–20.

3. Blair, D.C., and Maron, M.E. An evaluation of retrieval effectiveness for a full-text document-retrieval system. Communications of the ACM, 28, 3 (1985), 289–299.

4. Blosseville, M.J.; Hebrail, G.; Monteil, M.G.; and Penot, N. Automatic document classification: natural language processing, statistical analysis, and expert system techniques used together. In Proceedings of the Fifteenth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Copenhagen, June 21–24, 1992, pp. 51–57.

5. Booker, L.B.; Goldberg, D.E.; and Holland, J.H. Classifier systems and genetic algorithms. In J.G. Carbonell (ed.), Machine Learning, Paradigms and Methods. Cambridge: MIT Press, 1990, pp. 235–282.

6. Bookstein, A., and Swanson, D.R. Probabilistic models for automatic indexing. Journal of the American Society for Information Science, 26, 1 (January–February 1975), 45–50.

7. Carbonell, J.G.; Michalski, R.S.; and Mitchell, T.M. An overview of machine learning. In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (eds.), Machine Learning, an Artificial Intelligence Approach. Palo Alto, CA: Tioga Publishing, 1983, pp. 3–23.

8. Chen, H., and Dhar, V. Reducing indeterminism in consultation: a cognitive model of user/librarian interaction. In Proceedings of the 6th National Conference on Artificial Intelligence (AAAI-87), Seattle, July 13–17, 1987, pp. 285–289.

9. Chen, H., and Dhar, V. User misconceptions of online information retrieval systems. International Journal of Man-Machine Studies, 32, 6 (June 1990), 673–692.

10. Chen, H. and Dhar, V. Cognitive process as a basis for intelligent retrieval systems design. Information Processing and Management, 27, 5 (1991), 405–432.

11. Chen, H.; Hsu, P.; Orwig, R.; Hoopes, L.; and Nunamaker, J.F. Automatic concept classification of text from electronic meetings. Communications of the ACM, 37, 10 (October 1994).

12. Chen, H., and Lynch, K.J. Automatic construction of networks of concepts characterizing document databases. IEEE Transactions on Systems, Man and Cybernetics, 22, 5 (September–October 1992), 885–902.

13. Chen, H.; Lynch, K.J.; Basu, K.; and Ng, T. Generating, integrating, and activating thesauri for concept-based document retrieval. IEEE EXPERT, Special Series on Artificial Intelligence in Text-Based Information Systems, 8, 2 (April 1993), 25–34.

14. Chen, H., and Mahboob, G. Example-based document retrieval: an inductive machine learning approach. Center for Management of Information, College of Business and Public

Administration, University of Arizona, Working Paper, CMI-WPS, 1992.

15. Chen, H., and Ng, T. An algorithmic approach to concept exploration in a large knowledge network (automatic thesaurus consultation): symbolic branch-and-bound vs. connectionist Hopfield net activation. Journal of the American Society for Information Science (1994), forthcoming.

16. Chen, H., and She, L. Inductive query by examples (IQBE): a machine learning approach. In Proceedings of the 27th Annual Hawaii International Conference on System Sciences (HICSS-27), Information Sharing and knowledge Discovery Track, Maui, January 4–7, 1994.

17. Chiaramella, Y., and Defude, B. A prototype of an intelligent system for information retrieval: IOTA. Information Processing and Management, 23, 4 (1987), 285–303.

18. Cohen, P.R., and Kjeldsen, R. Information retrieval by constrained spreading activation in semantic networks. Information Processing and Management, 23, 4 (1987), 255–268.

19. Croft, W.B., and Thompson, R.H. I $^{3}$ R: a new approach to the design of document retrieval systems. Journal of the American Society for Information Science, 38, 6 (1987), 389–404.

20. Dalton, J., and Deshmane, J. Artificial neural networks. IEEE Potentials, 10, 2 (April 1991), 33–36.

21. Daniels, P.J. The user modelling function of an intelligent interface for document retrieval systems. In B.C. Brookes (ed.), Intelligent Information Systems for the Information Society. Amsterdam: Elsevier Science Publishers B.V., North-Holland, 1986.

22. Derthick, M. Mundane Reasoning by Parallel Constraint Satisfaction. Ph.D. dissertation, Carnegie Mellon University, 1988.

23. Doszkocs, T.E.; Reggia, J.; and Lin, K. Connectionist models and information retrieval. Annual Review of Information Science and Technology (ARIST), 25 (1990), 209–260.

24. Fisher, D.H., and McKusick, K.B. An empirical comparison of ID3 and back-propagation. In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (IJCAI-89), Detroit, August 20–25, 1989, pp. 788–793.

25. Fox, E.A. Development of the CODER system: A testbed for artificial intelligence methods in information retrieval. Information Processing and Management, 23, 4 (1987), 341–366.

26. Frawley, W.J.; Pietetsky-Shapiro, G.; and Matheus, C.J. Knowledge discovery in databases: an overview. In G. Piatetsky-Shapiro and W.J. Frawley (eds.), Knowledge Discovery in Databases. Cambridge, MA: MIT Press, 1991, pp. 1–30.

27. Freund, J.E. Mathematical Statistics. Englewood Cliffs, NJ: Prentice-Hall, 1971.

28. Frieder, O., and Siegelmann, H.T. On the allocation of documents in multiprocessor information retrieval systems. In Proceedings of the Fourteenth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Chicago, October 13–16, 1991, pp. 230–239.

29. Gallant, S.I. Connectionist expert system. Communications of the ACM, 31, 2 (1988), 152–169.

30. Goldberg, D.E. Genetic Algorithms in Search, Optimization, and Machine Learning. Reading, MA: Addison-Wesley, 1989.

31. Goldberg, D.E. Messy genetic algorithm: motivation, analysis, and first results. Complex Systems, 3 (1989), 493–530.

32. Goldberg, D.E. Messy genetic algorithm revisited: studies in mixed size and scale. Complex Systems, 4 (1990), 415–444.

33. Gordon, M. Probabilistic and genetic algorithms for document retrieval. Communications of the ACM, 31, 10 (October 1988), 1208–1218.

34. Gordon, M. User-based document clustering by redescribing subject descriptions with a genetic algorithm. Journal of the American Society for Information Science, 42, 5 (June 1991), 311–322.

35. Greene, D.P., and Smith, S.F. COGIN: symbolic induction with genetic algorithms. In Proceedings of the Tenth National Conference on Artificial Intelligence (AAAI-92), San Jose, CA, July 12–16, 1992, pp. 111–116.

36. Grefenstette, J.J. Incorporating problem specific knowledge into genetic algorithms. In L. Davis (ed.), Genetic Algorithms and Simulated Annealing. San Mateo, CA: Morgan Kauffmann, 1987, pp. 42–60.

37. Hall, L.O., and Romaniuk, S.G. A hybrid connectionist, symbolic learning system. In Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI-90), Boston,

July 29–August 3, 1990, pp. 783–788.

38. Harp. S.; Samad. T.; and Guha, A. Towards the genetic synthesis of neural networks. In Proceedings of the Third International Conference on Genetic Algorithms. San Mateo, CA: Morgan Kaufmann, 1989.

39. Hopfield, J.J. Neural network and physical systems with collective computational abilities. Proceedings of the National Academy of Science, USA, 78, 8 (1982), 2554–2558.

40. Humphreys, B.L., and Lindberg, D.A. Building the unified medical language system. In Proceedings of the Thirteenth Annual Symposium on Computer Applications in Medical Care. Washington, DC: IEEE Computer Society Press, November 5–8, 1989, pp. 475–480.

41. Kitano, H. Empirical studies on the speed of convergence of neural network training using genetic algorithms. In Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI-90), Boston, July 29–August 3, 1990, pp. 789–795.

42. Knight, K. Connectionist ideas and algorithms. Communications of the ACM, 33, 11 (November 1990), 59–74.

43. Koza, J.R. Genetic Programming: On the Programming of Computers by Means of Natural Selection. Cambridge, MA: MIT Press, 1992.

44. Kwok, K.L. A neural network for probabilistic information retrieval. In Proceedings of the Twelfth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Cambridge, MA, June 25–28, 1989, pp. 21–30.

45. Lin, X.; Soergel, D.; and Marchionini, G. A self-organizing semantic map for information retrieval. In Proceedings of the Fourteenth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Chicago, October 13–16, 1991, pp. 262–269.

46. Lindberg, D.A., and Humphreys, B.L. The UMLS knowledge sources: tTools for building better user interface. In Proceedings of the Fourteenth Annual Symposium on Computer Applications in Medical Care. Los Alamitos, CA: Institute of Electrical and Electronics Engineers, November 4–7, 1990, pp. 121–125.

47. Lippmann, R.P. An introduction to computing with neural networks. IEEE Acoustics Speech and Signal Processing Magazine, 4, 2 (April 1987), 4–22.

48. MacLeod, K.J., and Robertson, W. A neural algorithm for document clustering. Information Processing and Management, 27, 4 (1991), 337–346.

49. Maron, M.E., and Kuhns, J.L. On relevance, probabilistic indexing and information retrieval. Journal of the ACM, 7, 3 (July 1960), 216–243.

50. Martin, B.K., and Rada, R. Building a relational data base for a physician document index. Medical Information, 12, 3 (July–September 1987), 187–201.

51. McCray, A.T., and Hole, W.T. The scope and structure of the first version of the UMLS semantic network. In Proceedings of the Fourteenth Annual Symposium on Computer Applications in Medical Care. Los Alamitos, CA: Institute of Electrical and Electronics Engineers, November 4–7, 1990, pp. 126–130.

52. Michalewicz, Z. Genetic Algorithms + Data Structures = Evolution Programs. Berlin: Springer-Verlag, 1992.

53. Michalski, R.S. A theory and methodology of inductive learning. In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (eds.), Machine Learning, An Artificial Intelligence Approach. Palo Alto, CA: Tioga Publishing, 1983, pp. 83–134.

54. Monarch, I., and Carbonell, J.G. CoalSORT: a knowledge-based interface. IEEE Expert (Spring 1987), 39–53.

55. Montana, D.J., and Davis, L. Training feedforward neural networks using genetic algorithms. In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (IJCAI-89), Detroit, August 20-25, 1989, pp. 762-767.

56. Montgomery, D.D. Design and Analysis of Experiments. New York: John Wiley, 1976.

57. Mooney, R.; Shavlik, J.; Towell, G.; and Gove, A. An experimental comparison of symbolic and connectionist learning algorithms. In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (IJCAI-89), Detroit, August 20–25, 1989, pp. 775–780.

58. Parsaye, K.; Chignell, M.; Khoshafian, S.; and Wong, W. Intelligent Databases. New York: John Wiley, 1989.

59. Petry, F.; Buckles, B.; Prabhu, D.; and Kraft, D. Fuzzy information retrieval using genetic algorithms and relevance feedback. In Proceedings of the ASIS Annual Meeting, 1993, pp. 122–125.

60. Piatetsky-Shapiro, G. Workshop on knowledge discovery in real databases. In International Joint Conference of Artificial Intelligence (1989).

61. Pollitt, S. Cansearch: an expert systems approach to document retrieval. Information Processing and Management, 23, 2 (1987), 119–138.

62. Quinlan, J.R. Discovering rules by induction from large collections of examples. In D. Michie (ed.), Expert Systems in the Micro-electronic Age. Edinburgh: Edinburgh University Press, 1979, pp. 168–201.

63. Quinlan, J.R. Learning efficient classification procedures and their application to chess end games. In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (eds.), Machine Learning, An Artificial Intelligence Approach. Palo Alto, CA: Tioga Publishing, 1983, pp. 463–482.

64. Quinlan, J.R. Induction of decision trees. Machine Learning, 1 (1986), 81–164.

65. Rada, R.; Mili, M.; Bicknell, E.; and Blettner, E. Development and application of a metric on semantic nets. IEEE Transactions on Systems, Man, and Cybernetics, 19, 1 (January–February 1989), 17–30.

66. Raghavan, V.V., and Agarwal, B. Optimal determination of user-oriented clusters: an application for the reproductive plan. In Proceedings of the Second International Conference on Genetic Algorithms and Their Applications, Cambridge, MA, July 1987, pp. 241–246.

67. Rich, E. Building and exploiting user models. In International Joint Conference of Artificial Intelligence, Tokyo, August 1979, pp. 720–722.

68. Rich, E. User modeling via stereotypes. Cognitive Science, 3 (1979), 329–354.

69. Rich, E. Users are individuals: individualizing user models. International Journal of Man-Machine Studies, 18, 3 (March 1983), 199–214.

70. Rose, D.E., and Belew, R.K. A connectionist and symbolic hybrid for improving legal research. International Journal of Man-Machine Studies, 35, 1 (1991), 1–33.

71. Rumelhart, D.E.; Hinton, G.E.; and McClelland, J.L. A general framework for parallel distributed processing. In D.E. Rumelhart, J.L. McClelland, and the PDP Research Group (eds.), Parallel Distributed Processing. Cambridge, MA: MIT Press, 1986, pp. 45–76.

72. Rumelhart, D.E.; Hinton, G.E.; and Williams, R.J. Learning internal representations by error propagation. In D.E. Rumelhart, J.L. McClelland, and the PDP Research Group (eds.), Parallel Distributed Processing. Cambridge, MA: MIT Press, 1986, pp. 318–362.

73. Salton, G. Automatic Text Processing. Reading, MA: Addison-Wesley, 1989.

74. Schaffer, J.; Caruana, R.; Eshelman, L.; and Das, R. A study of control parameters affecting online performance of genetic algorithms for function optimization. In Proceedings of the Third International Conference on Genetic Algorithms. San Mateo, CA: Morgan Kaufmann, 1989, pp. 51–60.

75. Shastri, L. Why semantic networks? In J.F. Sowa (ed.), Principles of Semantic Networks: Explorations in the Representation of Knowledge. San Mateo, CA: Morgan Kauffmann, 1991, pp. 109–136.

76. Simon, H. Artificial intelligence: where has it been, and where is it going? IEEE Transactions on Knowledge and Data Engineering, 3, 2 (June 1991), 128–136.

77. Sleeman, D. UMFE: a user modeling front-end subsystem. International Journal of Man-Machine Studies, 23 (1985), 63–77.

78. Swartout, W. Explanation and the role of the user model: how much will it help? In User Modelling Panel, Proceedings of the Ninth International Joint Conference on Artificial Intelligence, Los Angeles, August 1985, pp. 1298–1302.

79. Tank, D.W., and Hopfield, J.J. Collective computation in neuronlike circuits. Scientific American, 257, 6 (December 1987), 104–114.

80. Touretzky, D., and Hinton, G.E. A distributed connectionist production system. Cognitive Science, 12, 3 (1988), 423–466.

81. VanRijsbergen, C.J. Information Retrieval, 2d ed. London: Butterworths, 1979.

82. Weiss, S.M., and Kapouleas, I. An empirical comparison of pattern recognition, neural nets, and machine learning classification methods. In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (IJCAI-89), Detroit, August 20–25, 1989, pp. 781–787.

83. Weiss, S.M., and Kulikowski, C.A. Computer Systems That Learn: Classification and Prediction Methods from Statistics, Neural Networks, Machine Learning, and Expert Systems. San Mateo, CA: Morgan Kaufmann, 1991.

84. Wilkinson, R., and Hingston, P. Using the cosine measure in neural network for document retrieval. In Proceedings of the Fourteenth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, Chicago, October 13–16, 1991, pp. 202–210.

85. Wilkinson, R.; Hingston, P.; and Osborn, T. Incorporating the vector space model in a neural network used for document retrieval. Library Hi Tech, 10, 12 (1992), 69–75.

86. Yang, K., and Korfhage, R.R. Effects of query term weights modification in document retrieval: a study based on a genetic algorithm. In Proceedings of the Second Annual Symposium on Document Analysis and Information Retrieval, Las Vegas, April 26–28, 1993, pp. 271–285.

87. Yang, J.; Korfhage, R.R.; and Rasmussen, E. Query improvement in information retrieval using genetic algorithms: a report on the experiments of the TREC project. In Text Retrieval Conference (TREC-1), Gaithersburg, MD, November 4–6, 1993, pp. 31–58.

88. Zissos, A.Y., and Witten, I.H. User modeling for a computer coach: a case study. International Journal of Man–Machine Studies, 23 (1985), 729–750.
