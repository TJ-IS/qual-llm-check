---
otero_id: 13892
otero_key: "AUKN86MG"
title: "Hotel selection using a modified TOPSIS-based decision support algorithm"
authors: "P.K. Kwok; Henry Y.K. Lau"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hotel selection using a modified TOPSIS-based decision support algorithm

P.K. Kwok<sup>⁎,a</sup>, Henry Y.K. Lau<sup>b</sup>

![](/api/attachments/AUKN86MG/fulltext/images/1c48cb26b3004fb4a6c5c8944697ebbde7bc0db661cbf1531a03f7578151ab1c.jpg)

<sup>a</sup> School of Intelligent Systems Science and Engineering, Jinan Univeristy (Zhuhai Campus), Zhuhai 519070, China

<sup>b</sup> Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong, Pokfulam, Hong Kong

## A R T I C L E I N F O

Keywords: Decision support system Multi-criteria decision-making Vague set TOPSIS Hotel selection Online travel agencies

## A B S T R A C T

While many studies pointed out that travellers often consider a basket of factors when they are selecting their accommodation, few online travel agency websites allow the travellers to actively express their preference about the selection criteria in order to receive tailor-made recommendations in return. The absence of this feature causes travellers to spend extra efort and time to compare the hotel options themselves. This paper presents a decision support algorithm, namely Vague Set TOPSIS, to help travellers to rank the hotel options. It was found in this research that the structure and assumptions of the conventional TOPSIS methods are not suitable for handling this decision problem. Therefore, this paper is novel in providing a foundational change to the conventional TOPSIS models such that it is more applicable to hotel selection. The validity of the proposed decision support algorithm was proved via three approaches, which are mathematical proofs, computer stochastic simulation experiments and a numerical case study using data obtained from Hotels.com.

## 1. Introduction

Research shows that travellers consider many factors when they are choosing hotels for their travels, such as location, price and cleanliness [1]. Online travel agencies (OTAs) are becoming increasingly popular because they aim at helping travellers to gather travel information on the same platform at low costs to assist their decision-making. Priceline, Expedia, TripAdvisor and Ctrip are the top four OTAs in the industry [2], which own many popular websites for hotel reservations. Their websites provide functions like sorting hotels based on room rate and reputation of the hotels. They also allow their customers to filter the hotel options based on dates, locations and property types. However, none of their websites allows travellers to provide their preference about the criteria for selecting hotels and then provides tailor-made recommendations. The absence of this feature causes travellers to spend extra efort and time to compare the hotel options themselves, which violates the original purpose of setting up OTAs. Therefore, OTAs should develop ways to actively take the customers’ needs and preferences into account when providing tailor-made recommendations for their customers just like traditional travel agencies.

In this big data era, a natural direction of this kind of problems would be to develop a personalised hotel package recommendation system, similar to other existing product recommendation systems in the market, such as Amazon.com [3]. These systems often provide suggestions based on the big data obtained from their customers, including their click-through and conversion rates. However, this ap proach may not be the best option in the tourism industry domain due to several unique characteristics of the tourism industry domain as pointed out in [4]. Therefore, it is still necessary to build a decision support system (DSS) which make decisions based on the preferences ofered by the travellers.

This paper elaborates on the development of a multi-criteria deci sion-making (MCDM) theory that can be implemented in a DSS to support travellers during the choice of the hotel option. Kou et al. [5] made the following description about the relationship between MCDM and DSS: “Integration of MCDM with DSS brings benefit to both fields. MCDM tools are useful in identifying and evaluating incompatible alternatives for DSS, while DSS can implement MCDM approaches and help maintain andretrieve MCDM models." This paper distinguishes itself from previous literature in the following ways:

1. To the best of our knowledge, the application of vague set TOPSIS (VS-TOPSIS) method or intuitionistic fuzzy TOPSIS (IF-TOPSIS) method for hotel selection is almost sparse, except [6].

2. The proposed decision support algorithm is not just an extension of the traditional TOPSIS method. It was found in this research that the structure and assumptions of the conventional TOPSIS methods (including the fuzzy TOPSIS, VS-TOPSIS and IF-TOPSIS methods) are not suitable for selecting hotels. This paper is novel in providing a foundational change to the conventional TOPSIS models such that it is more applicable to this decision problem. (Please refer to Section 2.3 for more details.)

It should be stressed that the method provided in this paper does not aim to replace the function of a recommendation system using big data, which is still best used for developing promotional strategies. In contrast, it provides additional function for the OTA websites such that travellers can actively tell the OTAs their preference towards the selection criteria and the OTAs can then rank the potential hotel options for the travellers based on their preferences.

This paper is organised as such: following the current introduction, Section 2 presents a literature review on the theories. Section 3 describes the proposed decision support algorithm, whereas Section 4 provides a numerical case study using the data obtained from Hotels. com. Section 5 provides mathematical foundations of the proposed decision support algorithm and compares the ranks generated by the proposed method and the conventional methods. Lastly, Section 6 summarises this topic and ofers suggestions for future work.

## 2. Related work

## 2.1. MCDM and TOPSIS

Decision problems often involve many conflicting and incommensurate criteria, which may pose a remarkable cognitive burden to the decision makers [7]. Studies pointed out that a high cognitive efort would negatively afect the experience and the perceived usefulness of the e-commerce platforms [8]. MCDM is an operation research methodology that can be implemented in a DSS to help decision makers to select the “best" option (alternative)<sup>1</sup> in the presence of multiple conflicting criteria. Examples of typical MCDM methods in clude WSM, WPM, SAW, AHP, ELECTRE, TOPSIS, and PROMETHEE. In particular, WSM, WPM, SAW and AHP help decision-makers to find a single optimal solution, whereas ELECTRE, TOPSIS and PROMETHEE further help them to obtain a ranking list of the alternatives [9]. Since a hotel selection event is also an MCDM issue, MCDM methods can be applied to help the travellers to rank the hotel options.

Among the MCDM methods, the TOPSIS (Technique for Order Preference by Similarity to an Ideal Solution) method is popular due to its relatively more intuitive and clearer logic that represents the ratio nale of human choice when it is compared to other outranking methods such as ELECTRE and PROMETHEE [10]. It ranks the alternatives based on their geometric distance from the positive ideal solutions (PIS) and the negative ideal solutions (NIS)<sup>2</sup> [11]. Table 1 illustrates the essential steps of the traditional TOPSIS method. There have been many applications of theTOPSIS method in the literature since its introduction. Table 2 lists some recent studies about the applications of the TOPSIS method in the tourism and travel-related domains.

## 2.2. Vague set theory

Humans’ subjective decision making and thought process usually involve fuzzy, imprecise and uncertain information. Fuzzy set theory was proposed to manage ambiguous data [10]. It is often used together with linguistic variables, such as “good", “fair" and “poor”. However, the fuzzy set theory has a shortcoming that it does not distinguish the evidence for “support" and the evidence for “against" [18]. Hence, Gau and Buehrer [19] introduced the vague set theory, in which the grade of membership is interval-based instead of point-based as in the fuzzy set theory. In detail, a vague set $V = { \Sigma _ { n = 1 } } ^ { n } [ \alpha ( u _ { i } ) , 1 - \beta ( u _ { i } ) ] / u _ { i }$ in the universe U contains a true membership function,i.e. $\alpha _ { \nu } ( u ) \in U$ between 0 and 1, and a false membership function, i.e. $\beta _ { \nu } ( u ) \in U$ between 0 and 1, such that $\gamma _ { \nu } ( u ) = 1 - \beta _ { \nu } ( u ) - \alpha _ { \nu } ( u ) \geq 0 . \ \gamma _ { \nu } ( u )$ is the imprecision membership function of the vague set. It is the smallest when the decisionmaker knows exactly the degree of membership of u ∈ $U ,$ and vice versa. This interval-based grade of membership nature in the vague set theory could capture the vagueness of data and the levels of knowledge-related uncertainty <sup>3</sup> of the decision-makers about the degree of membership of u ∈ U [20]. Thus, many papers extended the use of the vague set theory into the TOPSIS method to reduce the chance of getting a biased result from the DSS under the “garbage in, garbage out” philosophy. Examples of related works are shown in Table 2.

2.3. Shortcomings of the TOPSIS, VS-TOPSIS and IF-TOPSIS methods and the contributions of this paper

2.3.1. Absence of agreed methods to measure the distance from the PIS and NIS

TOPSIS method ranks the alternatives based on the distance between the performance of each alternative and the PIS, as well as the NIS [14]. Hence, the distance measurement is an important step of the TOPSIS method. However, unlike Cantor’s classical set theory, the vague set theory is a relatively new concept. Thus, currently, no consensus has been made among researchers on the methods for measuring the distance or similarity between two vague sets (Table 3). Therefore,this paper makes a fundamental change to the procedures of the traditional TOPSIS method so that its distance measurement can rely on the well-developed Euclidean distance.

## 2.3.2. Inappropriate assumptions

The TOPSIS method assumes that the criteria would be monotonically increasing or decreasing [12]. However, business travellers, in particular, those who are serving public organisations, do not aim at minimising their travel costs, but rather at approaching the travel budgets granted by their organisations, i.e. not much higher nor much lower than the budgets. In other words, the PIS of the criterion about the hotel room rate, in this case, is the traveller’s budget instead of the lowest room rate amongst all hotel options. However, the closeness coeficient (CC ) of the traditional TOPSIS method assumes that the distance between the performance of an alter native and the PIS should be inversely proportional to the distance between the performance of that alternative and the NIS. This assumption is not good enough to meet the requirements of business travellers. Therefore, this paper mathematically rewrites the conventional TOPSIS method in order to release this constraint.

2.3.3. Failure in considering the travellers’ preferences to uncertain information

Although the implementation of the vague set theory to the TOPSIS method enables it to capture humans’ knowledge-related uncertainty, few VS-TOPSIS methods consider how decision-makers would take preference to the uncertain information in the result. For example, a traveller with a pessimistic attitude towards uncertainty would prefer a lower weight on the imprecision information than a risk-taking one. Therefore, this paper provides a new score function at the end of its proposed method to handle this problem.

## 3. Proposed VS-TOPSIS model for hotel selection

Fig. 1 shows the framework of the proposed decision method, whereas Table 4 defines the notations and functions of the proposed VS-TOPSIS model.

Table 1  
Essential steps of the traditional TOPSIS method [12].

<table><tr><td>Step</td><td>Description</td><td>Equation</td></tr><tr><td>1</td><td>Construct a decision matrix D</td><td> $D = (x_{ij})_{m \times n}$ </td></tr><tr><td>2</td><td>Formulate a normalised decision matrix R</td><td> $R = (r_{ij})_{m \times n} = \left( x_{ij} / \sqrt{\sum_{i=1}^{m} x_{ij}^2} \right)_{m \times n}$ </td></tr><tr><td>3</td><td>Build a weighted normalised decision matrix V</td><td> $V = (v_{ij})_{m \times n} = (w_j r_{ij})_{m \times n}$  $\Sigma_{j=1}^{n} w_j = 1$ </td></tr><tr><td>4</td><td>Identify the positive ideal solution (PIS) ( $A^+ = \{ v_1^+, v_2^+, ..., v_n^+ \})$  and negative ideal solution (NIS) ( $A^- = \{ v_1^-, v_2^-, ..., v_n^- \})$ </td><td> $v_j^+ = \left\{ (\max_i v_{ij} | j \in J_b), (\min_i v_{ij} | j \in J_c) | i \in [1 \cdots m] \right\}$  $v_j^- = \left\{ (\min_i v_{ij} | j \in J_b), (\max_i v_{ij} | j \in J_b) | i \in [1 \cdots m] \right\}$  $J_b$  is a set of benefit criteria $J_c$  is a set of cost criteria</td></tr><tr><td>5</td><td>Calculate the separation measure ( $s_i^+$  and  $s_i^-$ )</td><td> $s_i^+ = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^+)^2} \quad \forall i \in [1..m]$  $s_i^- = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^-)^2} \quad \forall i \in [1..m]$ </td></tr><tr><td>6</td><td>Determine the closeness coefficient ( $CC_i$ )</td><td> $CC_i = s_i^- / (s_i^+ + s_i^-) \forall i \in [1 \cdots m]$ </td></tr></table>

Table 2

<table><tr><td>Paper(s)</td><td>Purposes</td><td>Major tools</td></tr><tr><td>[13]</td><td>Ranking the performance of tourism infrastructure in Iranian provinces</td><td>VIKOR and TOPSIS</td></tr><tr><td>[14]</td><td>Selecting enterprise resource planning systems for Turkish Airlines</td><td>Fuzzy AHP and TOPSIS</td></tr><tr><td>[15]</td><td>Assessing the performance of hotel websites</td><td>Fuzzy TOPSIS</td></tr><tr><td>[11]</td><td>Assessing the Intelligence Level of IoT-Based Tourist Attractions</td><td>Fuzzy TOPSIS</td></tr><tr><td>[6]</td><td>Selecting hotels based on online reviews</td><td>Vague Set TOPSIS</td></tr><tr><td>[16]</td><td>Selecting the best option in project management</td><td>Vague Set TOPSIS</td></tr></table>

Application of TOPSIS techniques in tourism and travel-related domains in recent years.  
Note: Vague sets and intuitionistic fuzzy sets are the same [17].

Examples of methods for measuring the distance/level of similarity between two vague values $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] \mathrm { a n d } \widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { y } ]$ . Some of them are being applied to the TOPSIS research.

<table><tr><td>Paper(s)</td><td>Methods</td></tr><tr><td>[21]</td><td>Similarity:  $1 - \frac{1}{2}\{|(\alpha_x - \alpha_y) - (\beta_x - \beta_y)|\}$ </td></tr><tr><td>[22]</td><td>Similarity:  $1 - \frac{1}{2}\{|(\alpha_x - \alpha_y) - (\beta_x - \beta_y)|\}$ </td></tr><tr><td>[23]</td><td>Similarity:  $1 - \frac{1}{2}\{|(\alpha_x - \alpha_y) - (\beta_x - \beta_y)| + |(\alpha_x - \alpha_y) + (\beta_x - \beta_y)|\}$ </td></tr><tr><td>[24]</td><td>Similarity: $\sqrt{\left(1 - \frac{1}{2} |(\alpha_x - \alpha_y) - (\beta_x - \beta_y)|\right)(1 - |((\alpha_x - \alpha_y) + (\beta_x - \beta_y))|)}$ </td></tr><tr><td>[25,6]</td><td>Hamming distance: $\frac{1}{2}[|(\alpha_x - \alpha_y)| + |\beta_x - \beta_y| + |(\alpha_x - \alpha_y) + (\beta_x - \beta_y)|]$ Normalised Hamming distance: $\frac{1}{2n}[|(\alpha_x - \alpha_y)| + |\beta_x - \beta_y| + |(\alpha_x - \alpha_y) + (\beta_x - \beta_y)|]$ Euclidean distance: $\sqrt{\frac{1}{2}[(\alpha_x - \alpha_y)^2 + (\beta_x - \beta_y)^2 + ((\alpha_x - \alpha_y)) + (\beta_x - \beta_y))^2] }$ Normalised Euclidean distance: $\sqrt{\frac{1}{2n}[(\alpha_x - \alpha_y)^2 + (\beta_x - \beta_y)^2 + ((\alpha_x - \alpha_y)) + (\beta_x - \beta_y))^2]}$ </td></tr></table>

The framework of the proposed decision support method (VS TOPSIS method).

## 3.1. Proposed VS-TOPSIS Step 1 – Construct a decision matrix using (1)

OTAs often store data about the room rate and performance of hotels. These data can be directly entered into the decision matrix D.

$$
D = (x _ {i j}) _ {N ^ {A} \times N ^ {C}}\tag{1}
$$

## 3.2. Proposed VS-TOPSIS Step 2 – Normalise the decision matrix using (2)

As the selection criteria are not directly comparable with each other, it is necessary to normalise the values in the decision matrix D to form R.

$$
R = (r _ {i j}) _ {N ^ {A} \times N ^ {C}} = \left(x _ {i j} / \sqrt {\sum_ {i = 1} ^ {m} x _ {i j} ^ {2}}\right) _ {m \times n}\tag{2}
$$

Referring to Table 1. if the traditional TOPSIS method were to be used, the next step would be multiplying the importance weights of the criteria to the matrix R to form a weighted normalised decision matrix. However,this paper suggests to postpone such a multiplication at later stage to solve the problem stated in Section 2.3.1 4. Theorem 3.2 shows that it is equivalent to consider the importance weights of the selection criteria in the TOPSIS method Step 3, 4 and 5 (Table 5).

Theorem 3.1. Let $a _ { i } \in \mathbb { R } _ { \geq 0 }$ for $i = 1 , 2 , \ldots ,$ n such that $a _ { i + 1 } \geq a _ { i }$ and $w \in [ 0 , 1 ]$ . Hence, max( ) max( )wa w a= and $\operatorname* { m i n } _ { i } ( w a _ { i } ) = w \operatorname* { m i n } _ { i } ( a _ { i } )$

Proof.

$$
\text {   If   } a _ {1} \leq a _ {2} \leq ... \leq a _ {n} \Leftrightarrow w a _ {1} \leq w a _ {2} \leq ... \leq w a _ {n} \Rightarrow \max _ {i} (w a _ {i}) = w a _ {n}
$$

Then $a _ { 1 } \leq a _ { 2 } \leq . . . \leq a _ { n } \Rightarrow \operatorname* { m a x } ( a _ { i } ) = a _ { n }$ i

w a wa w a wamax( ) = max( ) max( )=<sub>i n i i</sub>

$$
a _ {1} \leq a _ {2} \leq ... \leq a _ {n} \Leftrightarrow w a _ {1} \leq w a _ {2} \leq ... \leq w a _ {n} \Rightarrow \min _ {i} (w a _ {i}) = w a _ {1}
$$

Then $a _ { 1 } \leq a _ { 2 } \leq . . . \leq a _ { n } \Rightarrow \operatorname* { m i n } _ { i } ( a _ { i } ) = a _ { 1 }$

$$
\begin{array}{l} \Leftrightarrow w \min _ {i} (a _ {i}) = w a _ {1} \Leftrightarrow w \min _ {i} (a _ {i}) = \min _ {i} (w a _ {i}) \\ \text { Therefore,  max } _ {i} (w a _ {i}) = w \max _ {i} (a _ {i}) \text { and } \min _ {i} (w a _ {i}) = \min _ {t} (w a _ {i}) \end{array}
$$

Theorem 3.2. Denote the notations in 4. It is equivalent to consider the importance weights of the criteria in the TOPSIS method Step 3, 4, and 5.

Proof. The proof starts from Step 3 of the traditional TOPSIS method, which can be referred to Table 1.

Traditional TOPSIS Step 3: Construct the weighted normalised decision matrix

![](/api/attachments/AUKN86MG/fulltext/images/76e705ce07a0cbce61e3949721123a6aefd13e7749cd201ab3a1582e27c78381.jpg)  
Fig. 1. The framework of the proposed decision support method (VS-TOPSIS method).

Table 4  
Notations and functions for the VS-TOPSIS method.

<table><tr><td>Notion/Function</td><td>Definition</td></tr><tr><td>i, j</td><td>Positive integers, where i ∈ A and j ∈ C</td></tr><tr><td>A ⊆ [1. . NA]</td><td>A set of hotels available in the database.</td></tr><tr><td>C ⊆ [1. . NC]</td><td>A set of selection criteria.</td></tr><tr><td>Jb ⊆ C</td><td>A set of benefit criteria. Under the benefit criteria, the higher the score of a hotel (xij), the better is the hotel.</td></tr><tr><td>Jc ⊆ C</td><td>A set of cost criteria. Under the cost criteria, the lower the score of a hotel (xij), the better is the hotel.</td></tr><tr><td>NA ∈ Z+</td><td>The total number of hotels.</td></tr><tr><td>NC ∈ Z+</td><td>The total number of selection criteria.</td></tr><tr><td>α ∈ [0,1]</td><td>The true membership value. It shows the degree of an object belonging to a vague set, and 0 ≤ α + β ≤ 1.</td></tr><tr><td>β ∈ [0,1]</td><td>The false membership value. It shows the degree of an object not belonging to a vague set, and 0 ≤ α + β ≤ 1.</td></tr><tr><td>γ ∈ [0,1]</td><td>The imprecision membership of a vague set. It reflects the precision of the knowledge about an object belonging to a vague set, and γ = 1 - α - β ≥ 0.</td></tr><tr><td>widj = [αj, 1 - βj]</td><td>The importance weight of criterion j. The importance weights of the criteria are linguistic variables received from the travellers. These linguistic variables can be translated into vague values according to Table 6 as suggested in [26].</td></tr><tr><td>xij ∈ R</td><td>The score of hotel i under criterion j.</td></tr><tr><td>D = (xij)N^A × N^C</td><td>The decision matrix. It contains the scores of NA hotels under NC criteria.</td></tr><tr><td>rij ∈ [0,1]</td><td>The normalised score of hotel i under criterion j.</td></tr><tr><td>R = (rij)N^A × N^C</td><td>The normalised decision matrix. It contains the scores of NA hotels under NC criteria.</td></tr><tr><td>R+ = {r1+, r2+, ..., rNC+}</td><td>The positive ideal solution (PIS). It is a set which contains the “best” score under each criterion.</td></tr><tr><td>R- = {r1-, r2-, ..., rNC-}</td><td>The negative ideal solution (NIS). It is a set which contains the “worst” score under each criterion.</td></tr><tr><td>widj + = [αi+, 1 - βi+]</td><td>The weighted NC-dimensional Euclidean distance. It measures the separation between the performance of hotel i and the PIS.</td></tr><tr><td>widj - = [αi-, 1 - βi-]</td><td>The weighted NC-dimensional Euclidean distance. It measures the separation between the performance of hotel i and the NIS.</td></tr><tr><td>widj Θ = [αiΘ, 1 - βiΘ]</td><td>The converted form ofwidj+. (More explanation will be provided in VS-TOPSIS Step 4.)</td></tr><tr><td>widj = [αi, 1 - βi]</td><td>The aggregated suitability indicator of hotel i.</td></tr><tr><td>M (widj) ∈ [-1,1]</td><td>The proposed score function in this paper. It is a mark of hotel i under the selection criteria. With this mark, the hotels can be ranked into a descending order.</td></tr><tr><td>τ ∈ [0,1], φ ∈ [0,1]</td><td>The ratio allocated by the travellers on the level of importance of the confirmed (true membership and false membership) information and the uncertain information in M(Δi). Assumes that decision-makers would not intentionally ignore all the confirmed information and the uncertain information, i.e., τ = 0 and φ = 0 at the same time, so τ + φ is always positive.</td></tr></table>

$\begin{array} { r } { \cot \widetilde { a } = [ \alpha _ { a } , 1 - \beta _ { a } ] \mathrm { a n d } \widetilde { b } = [ \alpha _ { b } , 1 - \beta _ { b } ] . } \end{array}$ Let also λ be any positive real numbers, i.e. $\lambda \in \mathbb { R } ^ { + }$ . The followings are the basic operators of vague sets (Bustince and Burillo [17] concluded vague sets and intuitionistic fuzzy sets are the same.) [27,28].

$$
\widetilde {a} \oplus \widetilde {b} = [ \alpha_ {a} + \alpha_ {b} - \alpha_ {a} \alpha_ {b}, 1 - \beta_ {a} \beta_ {b} ] \widetilde {a} \otimes \widetilde {b} = [ \alpha_ {a} \alpha_ {b}, 1 + \beta_ {a} \beta_ {b} - \beta_ {a} - \beta_ {b} ]
$$

=a b<sup>\~</sup> <sup>\~</sup> [max ( , ), max(1 , 1 )]<sub>a b</sub>

High

The notations for Theorem 3.2.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $W = (w_1 w_2 \ldots w_n)^T$ </td><td>The weight vector about the criteria in the TOPSIS method.  $w_j$  is the importance weight of criterion  $j$ .</td></tr><tr><td> $J_b$ </td><td>The benefit criteria in the TOPSIS method.</td></tr><tr><td> $J_c$ </td><td>The cost criteria in the TOPSIS method.</td></tr><tr><td> $R = (r_{ij})_{m \times n}$ </td><td>The normalised decision matrix in the TOPSIS method.</td></tr><tr><td> $r_{ij}$ </td><td>The normalised rating of alternative  $i$  about criterion  $j$ .</td></tr><tr><td> $R^+ = \{r_1^+, r_2^+, \ldots, r_n^+\}$ </td><td>The PIS in the TOPSIS method, which does not involve the weight ( $w_j$ ).</td></tr><tr><td> $R^- = \{r_1^-, r_2^-, \ldots, r_n^-\}$ </td><td>The NIS in the TOPSIS method, which does not involve the weight ( $w_j$ ).</td></tr><tr><td> $r_j^+$ </td><td> $\left\{ \left( \max_i v_{ij} \mid j \in J_b \right), \left( \min_i v_{ij} \mid j \in J_c \right) \mid i \in [1..m] \right\}$ .</td></tr><tr><td> $r_j^-$ </td><td> $\left\{ \left( \min_i v_{ij} \mid j \in J_b \right), \left( \max_i v_{ij} \mid j \in J_c \right) \mid i \in [1..m] \right\}$ .</td></tr><tr><td> $V = (v_{ij})_{m \times n}$ </td><td>The weighted normalised decision matrix in the TOPSIS method.</td></tr><tr><td> $v_{ij} = w_j r_{ij}$ </td><td>The weighted normalised rating of alternative  $i$  about criterion  $j$ .</td></tr><tr><td> $V^+ = \{v_1^+, v_2^+, \ldots, v_n^+\}$ </td><td>The PIS in the TOPSIS method, which consists of the weight ( $w_j$ ).</td></tr><tr><td> $V^- = \{v_1^-, v_2^-, \ldots, v_n^-\}$ </td><td>The NIS in the TOPSIS method, which consists of the weight ( $w_j$ ).</td></tr><tr><td> $v_j^+$ </td><td> $\left\{ \left( \max_i v_{ij} \mid j \in J_b \right), \left( \min_i v_{ij} \mid j \in J_c \right) \mid i \in [1..m] \right\}$ .</td></tr><tr><td> $v_j^-$ </td><td> $\left\{ \left( \min_i v_{ij} \mid j \in J_b \right), \left( \max_i v_{ij} \mid j \in J_c \right) \mid i \in [1..m] \right\}$ .</td></tr><tr><td> $s_i^+$ </td><td>The separation between the performance of the alternative  $i$  and the PIS.</td></tr><tr><td> $s_i^-$ </td><td>The separation between the performance of the alternative  $i$  and the NIS.</td></tr></table>

$$
V = (v _ {i j}) _ {m \times n} = (w _ {j} r _ {i j}) _ {m \times n} = (w _ {i}) _ {1 \times n} ^ {T} \cdot (r _ {i j}) _ {m \times n} = W \cdot R
$$

Traditional TOPSIS Step 4: Determine the PIS and NIS

$$
\begin{array}{l} v _ {j} ^ {+} = \left\{\left(\max _ {i} w _ {j} r _ {i j} \mid j \in J _ {b}\right), \left(\min _ {i} w _ {j} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] \right\} \\ = \left\{\left(w _ {j} \max _ {i} r _ {i j} \mid j \in J _ {b}\right), \left(w _ {j} \min _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] \right\} \\ = w _ {j} \left\{\left(\max _ {i} r _ {i j} \mid j \in J _ {b}\right), t \left(\min _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] = w _ {j} r _ {j} ^ {+} \right. \\ \Rightarrow V ^ {+} = \left\{v _ {1} ^ {+}, v _ {2} ^ {+}, \dots , v _ {n} ^ {+} \right\} = \left\{w _ {1} r _ {1} ^ {+}, w _ {2} r _ {2} ^ {+}, \dots , w _ {n} r _ {n} ^ {+} \right\} \\ 3. 1) \\ v _ {j} ^ {-} = \left\{\left(\min _ {i} v _ {i j} \mid j \in J _ {b}\right), \left(\max _ {i} v _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] \right\}. \\ = \left\{\left(w _ {j} \min _ {i} r _ {i j} \mid j \in J _ {b}\right), \left(w _ {j} \max _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] \right\}. \\ = w _ {j} \left\{\left(\min _ {i} r _ {i j} \mid j \in J _ {b}\right), \left(\max _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. m ] \right\}. \\ = w _ {j} r _ {j} ^ {-} \\ \Rightarrow V ^ {-} = \left\{v _ {1} ^ {-}, v _ {2} ^ {-}, \dots , v _ {n} ^ {-} \right\} = \left\{w _ {1} r _ {1} ^ {-}, w _ {2} r _ {2} ^ {-}, \dots , w _ {n} r _ {n} ^ {-} \right\}. \\ 3. 1) \end{array}
$$

Traditional TOPSIS Step 5: Calculate the separation measure of each alternative from the PIS and NIS points

$$
\begin{array}{l} s _ {i} ^ {+} = \sqrt {\sum_ {j = 1} ^ {n} (v _ {i j} - v _ {j} ^ {+}) ^ {2}} = \sqrt {\sum_ {j = 1} ^ {n} (w _ {j} r _ {i j} - w _ {j} r _ {j} ^ {+}) ^ {2}} \\ = \sqrt {\sum_ {j = 1} ^ {n} w _ {j} ^ {2} (r _ {i j} - r _ {j} ^ {+}) ^ {2}} = \sqrt {(w _ {j} ^ {2}) _ {1 \times n} ^ {T} \cdot [ (r _ {i j} - r _ {j} ^ {+}) ^ {2} ] _ {1 \times n}} \\ s _ {i} ^ {-} = \sqrt {\sum_ {j = 1} ^ {n} (v _ {i j} - v _ {j} ^ {-}) ^ {2}} = \sqrt {\sum_ {j = 1} ^ {n} (w _ {j} r _ {i j} - w _ {j} r _ {j} ^ {-}) ^ {2}} \\ = \sqrt {\sum_ {j = 1} ^ {n} w _ {j} ^ {2} (r _ {i j} - r _ {j} ^ {-}) ^ {2}} = \sqrt {(w _ {j} ^ {2}) _ {1 \times n} ^ {T} \cdot [ (r _ {i j} - r _ {j} ^ {-}) ^ {2} ] _ {1 \times n}} \end{array}
$$

As shown above, all equations consist of two components, i.e. w and $r ,$ and w can always be extracted from the equations. Hence, there is no diference in multiplying the importance weights of the criteria with the scores of the alternatives in Step 3, 4 or 5 of the TOPSIS method.

3.3. Proposed VS-TOPSIS Step 3 – Determine the PIS (R<sup>+</sup>) and NIS (R<sup>−</sup>) using (3) and (4) respectively

$$
r _ {j} ^ {+} = \left\{\left(\max _ {i} r _ {i j} \mid j \in J _ {b}\right), \left(\min _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. N ^ {A} ] \right\}\tag{3}
$$

$$
r _ {j} ^ {-} = \left\{\left(\min _ {i} r _ {i j} \mid j \in J _ {b}\right), \left(\min _ {i} r _ {i j} \mid j \in J _ {c}\right) \mid i \in [ 1.. N ^ {A} ] \right\}\tag{4}
$$

3.4. Proposed VS-TOPSIS Step 4 – Calculate the separation measure using the weighted N-dimensional Euclidean distance, i.e. (5) and (6)

The importance weights of the criteria (w ) are considered in this step and can be obtained by asking travellers to complete a quick survey about their preference towards each criterion as shown in Fig. 2. Cur rently, there is no unique way to translate the linguistic variable into a specific vague value [29]. Such a translation varies among diferent disciplines. For hotel selection, Pahari et al. [6] suggested to translate the linguistic variables received from the travellers into w using Table 6

## Traveller's Preference

Please rate vour opinion on the following criteria in terms of their level of importance in the selection of accomodation for your trip.

Criteria

1. Hotel's distance from major tourist attractions.

Important 7

2. Hotel's reputation

Medium

3. Hotel's room rate.

Unimportant

Please show your preference towards the value of the confirmed and uncertain information. (e.g. How much risk do you want to take along the trip?)

4. Confirmed information

5. Uncertain information

Low

Fig. 2. An example of survey that travellers have to complete in order to tell the DSS about their opinion on the level of importance for each selection criteria.

Table 6  
Linguistic Variables and their Related Vague Value in [6].

<table><tr><td>Linguistic variable</td><td>Vague value</td></tr><tr><td>Very important</td><td>[0.85,0.85]</td></tr><tr><td>Important</td><td>[0.75,0.8]</td></tr><tr><td>Medium</td><td>[0.5,0.65]</td></tr><tr><td>Unimportant</td><td>[0.3,0.4]</td></tr><tr><td>Very unimportant</td><td>[0.15,0.15]</td></tr></table>

$$
\widetilde {d} _ {i} ^ {+} = \sqrt {\sum_ {j = 1} ^ {N ^ {C}} \widetilde {w} _ {j} ^ {2} (r _ {i j} - r _ {j} ^ {+}) ^ {2}}\tag{5}
$$

$$
\widetilde {d} _ {i} ^ {-} = \sqrt {\sum_ {j = 1} ^ {N ^ {C}} \widetilde {w} _ {j} ^ {2} (r _ {i j} - r _ {j} ^ {-}) ^ {2}}\tag{6}
$$

3.5. Proposed VS-TOPSIS Step 5 – Convert $\widetilde { \mathbf { d } } _ { \mathrm { i } } ^ { + }$ to fall in line with the meaning of $\cdot \widetilde { \mathbf { d } } _ { \mathrm { i } } ^ { - }$ using (7)

As illustrated in [18], a vague value, for example, $\widetilde { a } = [ \alpha _ { a } , 1 - \beta _ { a } ] ,$ can be interpreted as a vote about the degree of membership of an object u in the universe U. In detail, a means $\alpha _ { a }$ proportion of voters agree that an object u belongs to the membership $U , \beta _ { a }$ proportion of voters disagree that the object u belongs to the membership $U ,$ and $\gamma _ { a } = 1 - \alpha _ { a } - \beta _ { a }$ proportion of voters abstain to make the decision. Following this logic, $\mathbf { \bar { \alpha } } _ { \mathbf { \tilde { d } _ { i } } } ^ { - }$ is an indicator representing the level of suitability of hotel i for being the “best” option because the larger the value of $\mathbf { \widetilde { d } } _ { i } ^ { - }$ , the further the position of alternative i from the NIS. In contrast, $\widetilde { d } _ { i } ^ { + }$ is a mark showing the level of unsuitability of hotel i for being the “best” option because the larger the value of ${ d _ { i } } ^ { + }$ , the further away the position of alternative i from the PIS. Specifically, $\widetilde { d } _ { i } ^ { - } = [ \alpha _ { i } ^ { - } , 1 - \beta _ { i } ^ { - } ]$ represents ${ \alpha _ { i } } ^ { - }$ proportion of voters agree that hotel i is suitable to bethe “best” option fulfilling all the evaluation criteria, $\beta _ { i } ^ { - }$ proportion of voters think that hotel i is not suitable, and $\gamma _ { i } ^ { - } = 1 - { \alpha _ { i } } ^ { - } - { \beta _ { i } } ^ { - }$ proportion of voters abstain. Similarly, $\widetilde { d } _ { i } ^ { + } = [ \alpha _ { i } ^ { + } , 1 - \beta _ { i } ^ { + } ]$ means ${ \alpha _ { i } } ^ { + }$ proportion of voters agree that hotel i is not suitable to be the “best" option fulfilling all the evaluation criteria, ${ \beta _ { i } } ^ { + }$ proportion of voters think that hotel extiti is suitable, $\gamma _ { i } ^ { + } = 1 - { \alpha _ { i } } ^ { + } - { \beta _ { i } } ^ { + }$ proportion of voters ab stain. Shifting the angle of view, $\widetilde { d } _ { i } ^ { + }$ can be converted to be in line with $\widetilde { d } _ { i } ^ { - }$ in the form of $\widetilde { d } _ { i } ^ { \ominus } = [ \alpha _ { i } ^ { \ominus } 1 - \beta _ { i } ^ { \ominus } ]$ using (7) without afecting its meaning. This conversion is commonly adopted in building the pairwised comparison matrix in the Vague Set AHP method<sup>5</sup>, like in [30].

$$
\widetilde {d} _ {i} ^ {\ominus} = [ \alpha_ {i} ^ {\ominus}, 1 - \beta_ {i} ^ {\ominus} ] = [ \beta_ {i} ^ {+}, 1 - \alpha_ {i} ^ {+} ]\tag{7}
$$

## 3.6. Proposed VS-TOPSIS Step 6 – Aggregate $\widetilde { \mathsf { d } } _ { \mathrm { i } } ^ { - }$ and $\widetilde { \mathsf { d } } _ { \mathrm { i } } ^ { \ominus }$ using (8)

This aggregation method assumes that travellers prefer a hotel option which is the closest to the PIS to obtain the most advantages unless the efect of the drawbacks, i.e. the NIS, outweighs those advantages. This assumption is valid and commonin real-life decisions.

$$
\widetilde {d} _ {i} = [ \bar {\alpha} _ {i}, 1 - \bar {\beta} _ {i} ] = \widetilde {d} _ {i} ^ {-} \vee \widetilde {d} _ {i} ^ {\ominus} = [ \max (\alpha_ {i} ^ {-}, \alpha_ {i} ^ {\ominus}), \max (1 - \beta_ {i} ^ {-}, 1 - \beta_ {i} ^ {\ominus}) ]\tag{8}
$$

3.7. Proposed VS-TOPSIS Step 7 – Rank the hotel options using (9) and (10)

$\widetilde { d } _ { i }$ shows the suitability of hotel i for being the “best” option. However, there is still one final problem that $\widetilde { d } _ { i }$ is a vague value. It is sometimes dificult to compare two vague values because a vague value holds two information, i.e. “confirmed" information and “uncertain" information. For example, suppose the aggregated suitability indicator of Hotel $A _ { 1 }$ is $\widetilde { d } _ { A } = [ 0 . 2 , 0 . 6 ]$ , and that of Hotel $A _ { 2 }$ is $\widetilde { d } _ { B } = [ 0 . \ 3 , \ 0 . \ 5 ] .$ . It is hard to tell which one is better. Therefore, inspired by $[ 3 1 ] ^ { 6 }$ , this paper proposes a new score function to rank these vague values as shown in (9) (Proofs are provided in Section 5).

$$
M (\widetilde {d} _ {i}) = \tau (\alpha_ {i} - \beta_ {i}) - \phi \gamma_ {i}\tag{9}
$$

The notion behind (9) is similar to the SAW method<sup>7</sup>, which is another type of MCDM method. It allows the proposed DSS to rank the hotel options based on travellers’ favour to the importance weight of the confirmed information and the uncertain information. Using (9), the hotel options (alternatives) can be ranked in descending order, and the best alternative $A ^ { * }$ can be determined using (10).

$$
A ^ {*} = \{A _ {i} = \max _ {i} M (\widetilde {d} _ {i}) \}\tag{10}
$$

Hotel $A ^ { * }$ is the best option among the hotels in the database of the OTAs. It should be recommended to the traveller.

## 4. Numerical case study

This section presents a numerical case study to demonstrate the proposed hotel selection algorithm. Three hotels located in Hong Kong are selected for this demonstration, namely the Regal Airport Hotel $\left( A _ { 1 } \right)$ , Novotel Citygate Hong Kong $\left( A _ { 2 } \right)$ , and Gateway Marco Polo Hotel $( A _ { 3 } ) .$ . The data of these hotels were obtained from Hotels.com, a popular OTA website, on 21 July 2018. The check-in and check-out date were assumed to be 1 September 2018 and 2 September 2018 respectively. Fig. 3 shows the screenshots of those three hotels on Hotels.com. Suppose the traveller only considers three criteria when he is selecting the hotel for his trip, which are the convenience to Hong Kong Disneyland $( C _ { 1 } ) ,$ , reputation $\left( C _ { 2 } \right)$ and room rate $\left( C _ { 3 } \right)$ of the hotels. Therefore, the score of each alternative under those criteria is listed in Table 8. Assume the traveller places the level of importance of each criterion as Table $^ { 7 , }$ similar to most Chinese’s thought as reported in [32]. Also, suppose the importance weight of the confirmed information and the uncertain information are $\tau = 1$ and $\phi = 0 . 5$ respectively.

Logically speaking, a rational traveller would consider Hotel $A _ { 1 }$ as the best choice among the three options based on the three criteria in this case study. The reason behind is that Hotel $A _ { 1 }$ is the closest to the Hong Kong Disneyland, highest in reputation and lowest in the room rate. Likewise, Hotel $A _ { 2 }$ would be the second choice, whereas Hotel $A _ { 3 }$ should be the last choice, i.e. Hotel A > Hotel $A _ { 2 } >$ Hotel $A _ { 3 } .$ The hypothesis in this case study is that the proposed VS-TOPSIS method should generate the same rank as this logical interpretation at the end of this case study. Tables 7–10 display the calculation steps and results in this case study.

Referring to Table $1 0 , M ( \widetilde { d } _ { 1 } ) > M ( \widetilde { d } _ { 2 } ) > M ( \widetilde { d } _ { 3 } )$ so the ranking order of the three hotels is Hotel A₁ ≥ Hotel $A _ { 2 } >$ Hotel $A _ { 3 } .$ Hence, Hotel $A _ { 1 }$ should berecommended to the traveller based on criteria $C _ { 1 } , C _ { 2 } ,$ and $C _ { 3 } .$ As the rank of the hotel options obtained from the proposed VS-TOPSIS method is the same as the illustrated rank at the beginning, the proposed VS-TOPSIS method is shown to be trustworthy. As a remark, this numerical case study is only part of the validation of the proposed VS-TOPSIS method. As there is a possibility that the input dataset can bias the results of a real-life case study, this paper provides a stochastic computer simulation study in Section 5.2, which further validates the proposed method using random numbers.

![](/api/attachments/AUKN86MG/fulltext/images/835d1bf6d8bf614f032ee1fa891990e71fd52f1ae5689f7a7ba3c7bf59812fee.jpg)  
Fig. 3. Screenshots of the hotel information on Hotels.com.

Table 7  
The key performance indicator and the importance weight of the criteria.

<table><tr><td>Criterion ( $C_j$ )</td><td>Key Performance Indicator</td><td>Level of Importance</td><td>Importance Weight ( $\widetilde{w}_j$ )</td></tr><tr><td>1. Convenient to Hong Kong Disneyland</td><td>Distance from the Hong Kong Disneyland in kilometre</td><td>Important</td><td>[0.75,0.8]</td></tr><tr><td>2. Reputation</td><td>Number of stars obtained in the customer review</td><td>Medium</td><td>[0.5,0.65]</td></tr><tr><td>3. Room rate</td><td>US Dollar</td><td>Unimportant</td><td>[0.3,0.4]</td></tr></table>

Table 8  
The score of the hotels.

<table><tr><td>Alternative (Ai)/Criterion (Cj)</td><td>Convenient to Hong Kong Disneyland (km)</td><td>Reputation (no. of stars)</td><td>Room rate (US dollars)</td></tr><tr><td>1. Hotel A1</td><td>11</td><td>4.5</td><td>129</td></tr><tr><td>2. Hotel A2</td><td>11</td><td>4.0</td><td>140</td></tr><tr><td>3. Hotel A3</td><td>13</td><td>4.0</td><td>189</td></tr></table>

## 5. Validations

A decision method is claimed to be valid if it can vield choices that accurately reflect the values of the decision-maker [33]. However, this statement is a paradox when it comes to MCDM, in hotel selection particularly, because only the decision-maker can tell whether the solution provided by the MCDM method fits his needs. Nevertheless, the decision-maker needs decision support because he cannot compare the alternatives under many conflicting criteria directly and objectively. Consequently, it is dificult to find a reference point or benchmark to compare the methods in this context. Hence, no direct way is available to validate the decision outcomes of an MCDM method as diferent MCDM methods often yield diferent ranking outcomes when being applied to the same problem [7,10,34,35]. Bernroider and Stix [35] viewed that the decision generated by the MCDM method can be validated based on the strength of a collection of the three pieces of evidence, which are the content validity (including face validity), criterion validity and construct validity. Content validity is about the validity of the input data. Construct validity is about the empirical and theoreticalsupport of the decision method. Criterion validity is about whether the proposed method can generate similar results to other similar methods. This paper assumes that the data in the OTAs' database is valid, so content validity is confirmed beyond doubt. Papers which propose new MCDM methods usually focus on the latter two types of validity. For construct validity, this paper provides a series of mathematical proofs and descriptions in Sections 3 and 5.1 (Theorems 3.1-3.2 and 5.1-5.6). They confirm the logic and causal relationship of the proposed VS-TOPSIS method. The same method was used in $[ 1 6 , 3 6 ] .$ For criterion validity, this paper presents a simulation study in Section 5.2 to show the relationship among the proposed VS-TOPSIS method, the traditional TOPSIS method and the conventional VS-TOPSIS method. The study tests the methods using a large set of random samples in a controlled and replicable environment. Since random numbers are used, the conclusion made is less biased to a specific data set or decision context. The design of this simulation study is largely based on the work of [12,33]. Papers such as [36] also usedthis method to validate their proposed method.

Table 9  
The normalised score of the hotels, the PIS and the NIS.

<table><tr><td>Alternative (Ai)/Criterion (Cj)</td><td>Convenient to Hong Kong Disneyland</td><td>Reputation</td><td>Room rate</td></tr><tr><td>1. Hotel A1</td><td>0.54</td><td>0.62</td><td>0.48</td></tr><tr><td>2. Hotel A2</td><td>0.54</td><td>0.55</td><td>0.52</td></tr><tr><td>3. Hotel A3</td><td>0.64</td><td>0.55</td><td>0.70</td></tr><tr><td>PIS (R+)</td><td>0.54</td><td>0.62</td><td>0.48</td></tr><tr><td>NIS (R-)</td><td>0.64</td><td>0.55</td><td>0.70</td></tr></table>

Table 10  
The suitability indicators, marks and rank of the hotels

<table><tr><td>Alternative (Ai)</td><td> $\widetilde{d}_{i}^{+}$ </td><td> $\widetilde{d}_{i}^{-}$ </td><td> $\widetilde{d}_{i}^{\ominus}$ </td><td> $\widetilde{d}_{i}$ </td><td>M(di)</td><td>Rank</td></tr><tr><td>1. Hotel A1</td><td>[0.00,0.00]</td><td>[0.12,0.15]</td><td>[1.00,1.00]</td><td>[1.00,1.00]</td><td>1.00</td><td>1</td></tr><tr><td>2. Hotel A2</td><td>[0.04,0.05]</td><td>[0.11,0.13]</td><td>[0.95,0.96]</td><td>[0.95,0.96]</td><td>0.90</td><td>2</td></tr><tr><td>3. Hotel A3</td><td>[0.12,0.15]</td><td>[0.00,0.00]</td><td>[0.85,0.88]</td><td>[0.85,0.88]</td><td>0.72</td><td>3</td></tr></table>

## 5.1. Mathematical foundations of the modified score function

Since (9) is inspired by [31], it can be verified if it can fulfil the requirements of Wang et al.'s [31] theories. In detail, Wang et al. [31] mainly compared their score function with [37] and [38].

Let x be a vague value, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ]$ . C x( ) is the score function in [37], whereas $H ( \widetilde { x } )$ is the score function in [38].

$$
C (\widetilde {x}) = \alpha_ {x} - \beta_ {x} H (\widetilde {x}) = \alpha_ {x} + \beta_ {x}
$$

Theorem 5.1. Let x be a vague value, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] _ { \mathrm { { \ell } } }$ , and $M ( \widetilde { x } )$ be the score function, then $| - 1 \leq M ( \widetilde { x } ) \leq 1$

Proof. Recalling the definition in Table 4, α ∈ [0,1],

$$
\begin{array}{l} \text { Proof.   Recalling   the   definition   in   Table   4,   } a _ {x} \in [ 0, 1 ], \\ \beta_ {x} \in [ 0, 1 ],   \gamma_ {x} = 1 - \beta_ {x} - \alpha_ {x} \in [ 0, 1 ],   \tau \in [ 0, 1 ] \text {   and   } \phi \in [ 0, 1 ] \\ M (\widetilde {x}) = \tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} \leq \tau (1 - 0) - \phi (0) \leq 1 \\ M (\widetilde {x}) = \tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} \geq \tau (0 - 1) - \phi (0) \geq - 1 \\ \text { Therefore,   } - 1 \leq M (\widetilde {x}) \leq 1. \end{array}
$$

Theorem 5.2. Let x and y be two vague values, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] .$ $\widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { y } ] ,$ and $\tau + \phi > 0 . \quad M ( \widetilde { x } ) \geq M ( \widetilde { y } )$ if and only if $\begin{array} { r } { \alpha _ { x } - \alpha _ { y } \geq \frac { \tau - \phi } { \tau + \phi } ( \beta _ { x } - \beta _ { y } ) . } \end{array}$

Proof. In case M x M y ( ) ( ),

$$
\tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} \geq \tau (\alpha_ {y} - \beta_ {y}) - \phi \gamma_ {y}
$$

$$
(\tau + \phi) \alpha_ {x} + (\phi - \tau) \beta_ {x} - \phi \geq (\tau + \phi) \alpha_ {y} + (\phi - \tau) \beta_ {y} - \phi
$$

$$
(\alpha_ {x} - \alpha_ {y}) \geq \frac {\tau - \phi}{\tau + \phi} (\beta_ {x} - \beta_ {y})
$$

Therefore, $M ( \widetilde { { x } } ) \geq M ( \widetilde { { y } } )$ if and only $\begin{array} { r } { \mathrm { i f } \alpha _ { x } - \alpha _ { y } \ge \frac { \tau - \phi } { \tau + \phi } ( \beta _ { x } - \beta _ { y } ) } \end{array}$ . Also, in case $\tau = 1$ and $\phi = 0 . 5 , ~ M ( \widetilde { x } ) \ge M ( \widetilde { y } ) ~ \mathrm { i f }$ and only if $\begin{array} { r } { ( \alpha _ { x } - \alpha _ { y } ) \ge \frac { 1 } { 3 } ( \beta _ { x } - \beta _ { y } ) } \end{array}$ and hence fulfilling the requirement of Wang et al.'s [31] score function.

Theorem 5.3. Let x and y be two vague values, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] .$ $\widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { v } ] , x \neq y , \phi > 0$ and $C ( \widetilde { \boldsymbol { x } } ) = C ( \widetilde { \boldsymbol { y } } )$ . If $H ( \widetilde x ) < H ( \widetilde y )$ , then $M ( \widetilde { x } ) < M ( \widetilde { y } ) ;$ ; if $H ( \widetilde { x } ) > H ( \widetilde { y } )$ , then $M ( \widetilde { \boldsymbol { x } } ) > M ( \widetilde { \boldsymbol { y } } )$

Proof. In case $C ( \widetilde { \boldsymbol { x } } ) = C ( \widetilde { \boldsymbol { y } } ) _ { : }$ , then $H ( \widetilde x ) \neq H ( \widetilde y )$ . Otherwise,

$$
\left\{ \begin{array}{l} C (\widetilde {x}) = C (\widetilde {y}) \\ H (\widetilde {x}) = H (\widetilde {y}) \end{array} \right. \Leftrightarrow \left\{ \begin{array}{l} \alpha_ {x} - \beta_ {x} = \alpha_ {y} - \beta_ {y} \\ \alpha_ {x} + \beta_ {x} = \alpha_ {y} + \beta_ {y} \end{array} \right. \Leftrightarrow \left\{ \begin{array}{l} \alpha_ {x} = \alpha_ {y} \\ \beta_ {x} = \beta_ {y} \end{array} \right. \Leftrightarrow \widetilde {x} = \widetilde {y}
$$

This result does not agree with the assumption that $\widetilde x \neq \widetilde y$ Referring to (9), it is straightforward that

$$
\begin{array}{r} M (\widetilde {x}) = \tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} = \tau (\alpha_ {x} - \beta_ {x}) - \phi (1 - \beta_ {x} - \alpha_ {x}) \\ = \tau C (\widetilde {x}) + \phi H (\widetilde {x}) - \phi \end{array}
$$

$$
\begin{array}{c} M (\widetilde {y}) = \tau (\alpha_ {y} - \beta_ {y}) - \phi \gamma_ {y} = \tau (\alpha_ {y} - \beta_ {y}) - \phi (1 - \beta_ {y} - \alpha_ {y}) \\ = \tau C (\widetilde {y}) + \phi H (\widetilde {y}) - \phi \end{array}
$$

Since $C ( \widetilde { x } ) = C ( \widetilde { y } ) , M ( \widetilde { x } ) - M ( \widetilde { y } ) = \phi ( H ( \widetilde { x } ) - H ( \widetilde { y } ) )$ . As $\phi > 0 ,$ $M ( \widetilde { x } ) - M ( \widetilde { y } ) < 0$ if and only if $H ( \widetilde { x } ) - H ( \widetilde { y } ) < 0 .$ Also, $M ( \widetilde { x } ) - M ( \widetilde { y } ) > 0 \mathrm { ~ i ~ }$ f and only if $H ( \widetilde { x } ) - H ( \widetilde { y } ) > 0 .$ . Therefore, it is obviously $M ( \widetilde { x } ) < M ( \widetilde { y } )$ in case $C ( \widetilde { x } ) = C ( \widetilde { y } )$ and $H ( \widetilde x ) < H ( \widetilde y )$ . In contrast, $M ( \widetilde { x } ) > M ( \widetilde { y } )$ in case $C ( \widetilde { \boldsymbol { x } } ) = C ( \widetilde { \boldsymbol { y } } )$ and $H ( \widetilde { x } ) > H ( \widetilde { y } )$ . This proof shows that the proposed score function involves similar attribute with the Wang et al.'s [31] score function. It agrees with the function H when the function C is invalid.

Theorem 5.4. Let x and y be two vague values, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] ,$ $\widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { v } ] , x \neq y , \tau > 0 ,$ , and $H ( \widetilde { x } ) = H ( \widetilde { y } )$ ). $\begin{array} { r } { \mathrm { f } C ( \widetilde { x } ) < C ( \widetilde { y } ) , } \end{array}$ then $M ( \widetilde { x } ) < M ( \widetilde { y } ) ;$ if $C ( \widetilde { x } ) > C ( \widetilde { y } )$ , then $M ( \widetilde { \boldsymbol { x } } ) > M ( \widetilde { \boldsymbol { y } } )$

Proof. The proof is similar to Theorem 5.3.

In case $H ( \widetilde { x } ) = H ( \widetilde { y } )$ , then $C ( \widetilde { x } ) \neq C ( \widetilde { y } )$ . Otherwise,

$$
\left\{ \begin{array}{l} C (\widetilde {x}) = C (\widetilde {y}) \\ H (\widetilde {x}) = H (\widetilde {y}) \end{array} \right. \Leftrightarrow \left\{ \begin{array}{l} \alpha_ {x} - \beta_ {x} = \alpha_ {y} - \beta_ {y} \\ \alpha_ {x} + \beta_ {x} = \alpha_ {y} + \beta_ {y} \end{array} \right. \Leftrightarrow \left\{ \begin{array}{l} \alpha_ {x} = \alpha_ {y} \\ \beta_ {x} = \beta_ {y} \end{array} \right. \Leftrightarrow \widetilde {x} = \widetilde {y}
$$

This result does not agree with the assumption that $\widetilde x \neq \widetilde y .$ Referring to (9), it is straightforward that

$$
\begin{array}{r} M (\widetilde {x}) = \tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} = \tau (\alpha_ {x} - \beta_ {x}) - \phi (1 - \beta_ {x} - \alpha_ {x}) \\ = \tau C (\widetilde {x}) + \phi H (\widetilde {x}) - \phi \end{array}
$$

$$
\begin{array}{r} M (\widetilde {y}) = \tau (\alpha_ {y} - \beta_ {y}) - \phi \gamma_ {y} = \tau (\alpha_ {y} - \beta_ {y}) - \phi (1 - \beta_ {y} - \alpha_ {y}) \\ = \tau C (\widetilde {y}) + \phi H (\widetilde {y}) - \phi \end{array}
$$

$\mathrm { S i n c e ~ } \ H ( \widetilde { x } ) = H ( \widetilde { y } ) , \ M ( \widetilde { x } ) - M ( \widetilde { y } ) = \tau ( C ( \widetilde { x } ) - C ( \widetilde { y } ) ) . \ \mathrm { ~ A s ~ } \ \tau \ > \ 0 ,$ $M ( \widetilde x ) - M ( \widetilde y ) < 0 \quad \mathrm { ~ i f ~ } \quad \mathrm { a n d ~ } \quad \mathrm { o n l y } \quad \mathrm { i f } \quad C ( \widetilde x ) - C ( \widetilde y ) < 0 . \quad \mathrm { A l s o , }$ $M ( \widetilde { x } ) - M ( \widetilde { y } ) > 0$ if and only if $C ( \widetilde { x } ) - C ( \widetilde { y } ) > 0 .$ . Hence, it is obviously $M ( \widetilde { x } ) < M ( \widetilde { y } )$ in case $H ( \widetilde { x } ) = H ( \widetilde { y } )$ and $C ( \widetilde { x } ) < C ( \widetilde { y } )$ . In contrast, $M ( \widetilde { \boldsymbol { x } } ) > M ( \widetilde { \boldsymbol { y } } )$ in case $H ( \widetilde { x } ) = H ( \widetilde { y } )$ and $C ( \widetilde { x } ) > C ( \widetilde { y } )$ . This proof shows that the proposed score function involves similar attribute with the Wang et al.'s [31] score function. It agrees with the function C when the function H is invalid.

Theorem 5.5. Let x and y be two vague values, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] ,$ $\widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { y } ] , \quad x \neq y , \quad \mathrm { a n d } \quad \tau + \phi > 0 . \quad \mathrm { I f } \quad C ( \widetilde { x } ) > C ( \widetilde { y } )$ and $H ( \widetilde { x } ) > H ( d e \dot { y } )$ then $M ( \widetilde { \boldsymbol { x } } ) > M ( \widetilde { \boldsymbol { y } } )$ . In contrast, if $C ( \widetilde { x } ) < C ( \widetilde { y } )$ and $H ( \widetilde x ) < H ( \widetilde y )$ then $M ( \widetilde { x } ) < M ( \widetilde { y } )$ .

Proof. Referring to (9), it is straightforward that

$$
\begin{array}{r l} & M (\widetilde {x}) = \tau (\alpha_ {x} - \beta_ {x}) - \phi \gamma_ {x} = \tau (\alpha_ {x} - \beta_ {x}) - \phi (1 - \beta_ {x} - \alpha_ {x}) \\ & \qquad = \tau C (\widetilde {x}) + \phi H (\widetilde {x}) - \phi \\ & M (\widetilde {y}) = \tau (\alpha_ {y} - \beta_ {y}) - \phi \gamma_ {y} = \tau (\alpha_ {y} - \beta_ {y}) - \phi (1 - \beta_ {y} - \alpha_ {y}) \\ & \qquad = \tau C (\widetilde {y}) + \phi H (\widetilde {y}) - \phi \\ & \Rightarrow M (\widetilde {x}) - M (\widetilde {y}) = \tau (C (\widetilde {x}) - C (\widetilde {y})) + \phi (H (\widetilde {x}) - H (\widetilde {y})) \end{array}
$$

Hence, as $\phi + \tau > 0 \Rightarrow \phi > 0 \mathrm { o r } \tau > 0 , M ( \widetilde { x } ) - M ( \widetilde { y } ) > 0$ if and only $\mathrm { i f } ~ C ( \widetilde { x } ) > C ( \widetilde { y } )$ and $H ( \widetilde { x } ) > H ( \widetilde { y } )$ . In contrast, $M ( \widetilde { x } ) - M ( \widetilde { y } ) < 0$ if and only if $C ( \widetilde { x } ) < C ( \widetilde { y } )$ and $H ( \widetilde x ) < H ( \widetilde y )$

Table 11  
The settings of Experiment A and Experiment B.

<table><tr><td></td><td>Experiment A</td><td>Experiment B</td></tr><tr><td>Assumption</td><td>Knowledge-related uncertainty is absent</td><td>Knowledge-related uncertainty is present</td></tr><tr><td>Situation</td><td>The importance weight of each criterion and the scores of every alternative are both crisp</td><td>The importance weight of each criterion is vague, whereas the scores of every alternative is crisp</td></tr><tr><td>Control group</td><td>Traditional TOPSIS method  $w_j = a \quad \forall a \in [0.1,0.9]$ </td><td>Conventional VS-TOPSIS method $\widetilde{w}_j = [a,b] \quad \forall a \in [0.1,0.9], b \in [a,0.9]$ </td></tr><tr><td>Experimental Group</td><td>Proposed VS-TOPSIS method  $\widetilde{w}_j = [a,a] \quad \forall a \in [0.1,0.9]$ </td><td>Proposed VS-TOPSIS method  $\widetilde{w}_j = [a,b] \quad \forall a \in [0.1,0.9], b \in [a,0.9]$ </td></tr></table>

Table 12  
Essential steps of the conventional VS-TOPSIS method.

<table><tr><td>Step</td><td>Description</td><td>Equation</td></tr><tr><td>1</td><td>Construct a decision matrix D</td><td> $D = (x_{ij})_{m \times n}$ </td></tr><tr><td>2</td><td>Formulate a normalised decision matrix R</td><td> $R = (r_{ij})_{m \times n} = \left( x_{ij} / \sqrt{\sum_{i=1}^{m} x_{ij}^2} \right)_{m \times n}$ </td></tr><tr><td>3</td><td>Build a weighted normalised decision matrix V</td><td> $V = (v_{ij})_{m \times n} = (\widetilde{w}_j r_{ij})_{m \times n}$ </td></tr><tr><td>4</td><td>Identify the PIS  $(A^+ = \{\bar{v}_1^+, \bar{v}_2^+, ..., \bar{v}_n^+\})$  and NIS  $(A^- = \{\bar{v}_1^-, \bar{v}_2^-, ..., \bar{v}_n^-\})$ </td><td> $v_j^+ = \left\{ \left( \max_i \bar{v}_{ij} \mid j \in J_b \right), (min_i \bar{v}_{ij} \mid j \in J_c) \mid i \in [1..m] \right\}$  $v_j^- = \{(min_i \bar{v}_{ij} \mid j \in J_b), (max_i \bar{v}_{ij} \mid j \in J_c) \mid i \in [1..m]\}$ </td></tr><tr><td>5</td><td>Calculate the separation measure  $(s_i^+ \text{ and } s_i^-)$ </td><td> $s_i^+ = \sqrt{\frac{1}{2} \sum_{j=1}^{n} \left\{ \begin{array}{c} (\alpha_{ij} - \alpha_j^+)^2 + (\beta_{ij} - \beta_j^+)^2 \\ +[(\alpha_{ij} - \alpha_j^+) + (\beta_{ij} - \beta_j^+)]^2 \end{array} \right\}^2}$  $s_i^- = \sqrt{\frac{1}{2} \sum_{j=1}^{n} \left\{ \begin{array}{c} (\alpha_{ij} - \alpha_j^-)^2 + (\beta_{ij} - \beta_j^-)^2 \\ +[(\alpha_{ij} - \alpha_j^-) + (\beta_{ij} - \beta_j^-)]^2 \end{array} \right\}}$ </td></tr><tr><td>6</td><td>Determine the closeness coefficient  $(CC_i)$ </td><td> $CC_i = s_i^-/(s_i^+ + s_i^-) \forall i \in [1 \cdots m]$ </td></tr></table>

Theorem 5.6. Let $\widetilde { x }$ and $\widetilde { y }$ be two vague values, $\widetilde { x } = [ \alpha _ { x } , 1 - \beta _ { x } ] .$ $\widetilde { y } = [ \alpha _ { y } , 1 - \beta _ { v } ] , x \neq y ,$ and $\tau + \phi > 0 . \mathrm { I f } M ( \widetilde { x } ) = M ( \widetilde { y } ) ,$ , then either $C ( \widetilde { x } ) > C ( \widetilde { y } )$ and $H ( \widetilde x ) < H ( \widetilde y )$ or $C ( \widetilde { x } ) < C ( \widetilde { y } )$ and $H ( \widetilde { x } ) > H ( \widetilde { y } )$

Proof. In order to fulfil this theorem setting, the following condition must be satisfied $( C ( \widetilde { x } ) - C ( \widetilde { y } ) ) ( H ( \widetilde { x } ) - H ( \widetilde { y } ) ) < 0$ Also, $\begin{array} { r } { M ( \widetilde { x } ) = M ( \widetilde { y } ) \Rightarrow \alpha _ { x } - \alpha _ { y } = \frac { \tau - \phi } { \tau + \phi } ( \beta _ { x } - \beta _ { y } ) } \end{array}$ (Theorem 5.2)

$$
\begin{array}{r l} & {(C (\widetilde {x}) - C (\widetilde {y})) (H (\widetilde {x}) - H (\widetilde {y})) = (\alpha_ {x} - \alpha_ {y}) ^ {2} - (\beta_ {x} - \beta_ {y}) ^ {2}} \\ & {\qquad = \left[ \frac {\tau - \phi}{\tau + \phi} (\beta_ {x} - \beta_ {y}) \right] ^ {2} - (\beta_ {x} - \beta_ {y}) ^ {2}} \\ & {\qquad = \left[ \left(\frac {\tau - \phi}{\tau + \phi}\right) ^ {2} - 1 \right] (\beta_ {x} - \beta_ {y}) ^ {2} <   0} \end{array}
$$

As a remark, since $\begin{array} { r } { \tau + \phi > 0 , \left( \frac { \tau - \phi } { \tau + \phi } \right) ^ { 2 } } \end{array}$ must be smaller than 1, i.e. $\left( \frac { \tau - \phi } { \tau + \phi } \right) ^ { 2 } < 1$ . Also, $( \beta _ { x } - \beta _ { y } ) ^ { 2 }$ must be positive. Therefore, $\begin{array} { r } { \left\lceil \left( \frac { \tau - \phi } { \tau + \phi } \right) ^ { 2 } - 1 \right\rceil ( \beta _ { x } - \beta _ { y } ) ^ { 2 } < 0 . } \end{array}$ . Since $( C ( \widetilde { x } ) - C ( \widetilde { y } ) ) ( H ( \widetilde { x } ) - H ( \widetilde { y } ) ) < 0 ,$ it can be concluded that it $M ( \widetilde { \boldsymbol { x } } ) = M ( \widetilde { \boldsymbol { y } } )$ , then either $C ( \widetilde { x } ) > C ( \widetilde { y } )$ and $H ( \widetilde x ) < H ( \widetilde y )$ or $C ( \widetilde { x } ) < C ( \widetilde { y } )$ and $H ( \widetilde { x } ) > H ( \widetilde { y } )$ . This result again proved that the proposed score function can fulfil the condition of Wang et al.'s [31] score function.

To conclude, the proposed score function can fulfil the requirements of Wang et al.'s [31] score function. Hence, it should be treated as trustworthy.

Table 13  
Results of the Experiments (95% confidence level)

<table><tr><td>Experiment</td><td>Average spearman correlation coefficient</td></tr><tr><td>Experiment A</td><td>0.92 ± 0.002</td></tr><tr><td>Experiment B</td><td>0.86 ± 0.003</td></tr></table>

5.2. A comparison of the proposed VS-TOPSIS method, the traditional TOPSIS method and the conventional VS-TOPSIS method

The study included two experiments: Experiment A and Experiment B. Each experiment was divided into a control group and experimental group for making a comparison. Table 11 shows the settings of the experiments.

## 5.2.1. Sampling

A computer simulation was run for 10000 times. As a remark, the results were said to be statistically significant under 95% confidence level.

## 5.2.2. Procedures

This experiment assumed that there were 6 hotel options and 6 criteria (3 benefit criteria and 3 cost criteria). A computer program was written to rank the alternatives. At the start of each iteration, the computer generated the score of each alternative under each criterion between 0 and 1000 following a uniform distribution. These random numbers simulated the obiective data available in the OTAs' database Then, it produced the importance weight of each criterion according to the specification in Table 11. Afterwards, it put the alternatives in a descending order using the traditional TOPSIS method (Table 1), conventional VS-TOPSIS method (Table 12) and proposed VS-TOPSIS method (Section 3) respectively based on the selection criteria. In ad dition, the computer program supposed $\tau = 1$ and $\phi = 0 . 5$

## 5.2.3. Results

At the end of each iteration of each experiment, the ranks of alternatives generated from the control group and the experimental group were put in a pairwise comparison. Spearman’s Rank Correlation was calculated using $( 1 1 ) ^ { 8 }$ to measure the similarity between the ranks produced by the two groups. This is a common approach in the MCDM field to determine the statistical significance of the diference between the ranks generated by the proposed method and the conventional methods, so as to validate the proposed method [16,36,39]. Table 13 presents the average Spearman Correlation Coeficient obtained in each experiment.

![](/api/attachments/AUKN86MG/fulltext/images/4ef75bab41efe64be614f4a674ab79dba4f616aeb0e6861183b75a3fe99e9186.jpg)  
(a) Experiment A

![](/api/attachments/AUKN86MG/fulltext/images/90c196721e82748ea57126e2d7f04ef0b9d4e1c834f9b1f48a08ab01c100883e.jpg)  
(b) Experiment B  
Fig. 4. Results of the Sensitivity Study (Each experiment was repeated for 10000 times).

$$
r _ {s} = 1 - \frac {6 \sum_ {k = 1} ^ {N} D _ {k} ^ {2}}{N (N ^ {2} - 1)}\tag{11}
$$

Combining the results in Experiments A and $\mathbf { B } ,$ the proposed VS-TOPSIS method often yielded similar rank with the traditional TOPSIS method in the absence of knowledge-related uncertainty. When the knowledge-related uncertainty was present, the proposed VS-TOPSIS method also produced similar rank with the conventional VS-TOPSIS method in most cases. This feature can provide users with the con fidence to use the proposed VS-TOPSIS method for ranking the options in a hotel selection problem.

A sensitivity analysis was performed to assess the robustness of the experiments’ results. The study was carried out by increasing the number of alternatives $( N ^ { A } )$ in Experiments A and B from 6 to 60 while keeping the number of criteria $( N ^ { C } )$ at 6 throughout the experiment. The results are displayed in Fig. 4. It appeared that the Spearman’s Correlation Coeficient headed upwards as $N ^ { A }$ grew. However, its rate of change decreased when $N ^ { A }$ increased.

## 5.2.4. Discussion and conclusion

Two possible reasons could lead to the distinctions between the outputs of the control group and the experimental group in the two experiments. First, diferent operators were used for handling crisp values and vague values in Experiment A, i.e. $a + b \neq \widetilde { a } \oplus \widetilde { b }$ . Second, there was a diferent interpretation of the distances from the PIS and NIS, which were used to produce the score of the alternatives, in both experiments. To be specific, the traditional TOPSIS method and conventional VS-TOPSIS method both tried to look for the proportion of the distance from the NIS and the total distance from the NIS and PIS, while the proposed VS-TOPSIS method ranked the alternatives based on their closeness to the PIS unless the efect of NIS outweighs the advantages obtained in the PIS.

Additional studies were performed to verify the second reason. It was found that if the traditional $C C _ { i }$ (Tables 1 and 12 Step 6) was used to rank the alternatives in the proposed VS-TOPSIS method, the average Spearman Correlation Coeficient in Experiment A and that in Experiment B would rise to $0 . 9 7 ~ \pm ~ 0 . 0 0 1$ and $0 . 9 1 ~ \pm ~ 0 . 0 0 2$ respectively (95% confidence level) <sup>9</sup>.

Regarding the observations in the sensitivity study, it appeared that the increase of $\cdot _ { N } A$ did not largely afect the conclusion of Experiments A and B. Instead, it seemed that larger $N ^ { A }$ could dilute the dissimilarity of the rank in the outcomes. Referring to (11) about Spearman Correlation Coeficient, if the sum of the diferences between the ranks $( { \Sigma _ { i = 1 } } ^ { N } { D _ { i } } ^ { 2 } )$ is kept constant, the Spearman Correlation Coeficient $\left( r _ { s } \right)$ will increase as the number of elements in the ranks (N) enlarges. Consequently, there was a general upward trend for the Spearman Correlation Coeficient when $N ^ { A }$ became larger.

This experiment did not include the following benefits arose from the characteristics of proposed VS-TOPSIS method: Firstly, it relaxed the assumption of the conventional TOPSIS methods that the performance of the alternatives under a criterion should be monotonically increasing or decreasing. Secondly, the proposed VS-TOPSIS method could avoid possible arguments among researchers on the method of measuring the separation or similarity between two vague values or sets. It used the standard Euclidean distance for crisps value to calculate such separation. Lastly, it allowed travellers to rank the alternatives based on their favour of the confirmed information and the uncertain information by adjusting the weightings in $M ( \widetilde { d } _ { i } )$ .

## 6. Conclusion and contributions of this work

Many studies pointed out that travellers often consider many factors during hotel selection. However, few OTA websites provide tailor-made recommendations by allowing their customers to feed in their preference for the levels of importance of the hotel selection criteria. The absence of this feature makes travellers spend extra time and efort to compare the hotel options themselves. Therefore, this paper proposes a decision support algorithm to support travellers for selecting their favouritehotels. It has also provided the following contributions to the research field of DSS, MCDM and tourism management.

Firstly, this paper introduces a decision support algorithm that can be applied to the OTA websites to help travellers rank the hotel options based on their preference for the levels of importance of the hotel selection criteria. The algorithm is based on a proposed VS-TOPSIS method. While the use of the VS-TOPSIS method in the hotel selection field has seldom been studied in the previous literature, a numerical case study is presented using the data obtained from Hotels.com to demonstrate itsapplicability.

Secondly, this paper makes a foundational change to the conven tional TOPSIS models (including fuzzy TOPSIS, IF-TOPSIS and VS-TOPSIS) such that it is more applicable for hotel selection. It makes the decision support algorithm more justifiable by changing its way to measure the distance between the performance of each alternative and the ideal solutions. In addition, it provides a new score function to support travellers’ decision based on their preference for uncertain information. Furthermore, it provides a unique benefit to the business travellers, who can have their travel cost match with their travel budget instead of the minimum cost.

Lastly, this paper provides a detailed study on the comparison of the proposed VS-TOPSIS method with the traditional TOPSIS method and the conventional VS-TOPSIS method. It was found that the proposed VS-TOPSIS method was able to yield similar rank to the traditional TOPSIS method or the conventional VS-TOPSIS method in most of the time.

Further research should be done on finding ways to incorporate the proposed technique with other MCDM techniques, such as AHP, ELECTRE and PROMETHEEP, to further increase its value. Further ex periments should be done on comparing the proposed method with other MCDM methods. Psychological experiments should also be done to verify whether the final option suggested by the decision support algorithm is favourable to the travellers.

## References

[1] T. Lockyer, Understanding the dynamics of the hotel accommodation purchase decision, Int. J. Contemp. Hospital. Manage. 17 (2005) 481–492, https://doi.org/ 10.1108/09596110510612121.

[2] N. Patel, Online Travel Agencies. https://www.biz.uiowa.edu/henry/download research/OnlineTTTravel. pdf, 2016, (accessed 13 Nov 2017).

[3] G. Linden, B. Smith, J. York, Recommendations: Item-to-item collaborative fil tering, IEEE Internet Comput. 7 (2003) 76–80, https://doi.org/10.1109/MIC.2003. 1167344

[4] Q. Liu, Y. Ge, Z. Li, E. Chen, H. Xiong, Personalized travel package recommendation, 2011 IEEE 11th International Conference on Data Mining, 2011, pp. 407–416, , https://doi.org/10.1109/ICDM.2011.118.

[5] G. Kou, Y. Shi, S. Wang, Multiple criteria decision making and decision support systems …guest editor’s introduction, Decision Support Systems 51 (2011) 247–249, https://doi.org/10.1016/j.dss.2010.11.027.

[6] S. Pahari, D. Ghosh, A. Pal, An online review-based hotel selection process using intuitionistic fuzzy topsis method, in: P.K. Pattnaik, S.S. Rautaray, H. Das, J. Nayak (Eds.), Progress in Computing, Analytics and Networking, Springer, Singapore, 2018, pp. 203–214.

[7] J. Gettinger, E. Kiesling, C. Stummer, R. Vetschera, A comparison of representations for discrete multi-criteria decision problems. Decision Support Systems 54 (2013) 976–985. https://doi.org/10.1016/i.dss.2012.10.023.

[8] S. Huang, Designing utility-based recommender systems for e-commerce: Evaluation of preference-elicitation methods, Electron. Commerce Res. Appl. 10 (2011) 398–407, https://doi.org/10.1016/i.elerap.2010.11.003

[9] T.C.-K. Huang, Y.-L. Chen, T.-H. Chang, A novel summarization technique for the support of resolving multi-criteria decision making problems, Decision Support Systems 79 (2015) 109–124, https://doi.org/10.1016/j.dss.2015.08.004.

[10] S.-T. Li, W.-C. Chou, Power planning in ict infrastructure: A multi-criteria operational performance evaluation approach, Omega 49 (2014) 134–148, https://doi. org/10.1016/j.omega.2014.05.006.

[11] X. Guo, T. Zeng, Y. Wang, J. Zhang, Fuzzy topsis approaches for assessing the intelligence level of iot-based tourist attractions, IEEE Access 7 (2019) 1195–1207, https://doi.org/10.1109/ACCESS.2018.2881339

[12] I. Chamodrakas, I. Leftheriotis, D. Martakos, In-depth analysis and simulation study of an innovative fuzzy approach for ranking alternatives in multiple attribute decision making problems based on topsis, Appl. Soft Comput. 11 (2011) 900–907, https://doi.org/10.1016/j.asoc.2010.01.010.

[13] M. Bagheri, P. Shojaei, M. Khorami, A comparative survey of the condition of tourism infrastructure in iranian provinces using vikor and topsis, Decision Sci. Lett. 7 (2018) 87-102.

[14] H.S. Kilic, S. Zaim, D. Delen, Development of a hybrid methodology for erp system selection: The case of turkish airlines, Decision Supp. Syst. 66 (2014) 82–92, https://doi.org/10.1016/j.dss.2014.06.011.

[15] S. Qi, R. Law, D. Buhalis, A modified fuzzy hierarchical topsis model for hotel website evaluation, Hospitality, travel, and tourism: concepts, methodologies, tools and applications, IGI Global. 2015, pp. 263–283.

[16] S. Zhou, W. Liu, W. Chang, An improved topsis with weighted hesitant vague in formation, Chaos, Solitons Fractals 89 (2016) 47–53, https://doi.org/10.1016/j. chaos 2015.09.018

[17] H. Bustince, P. Burillo, Vague sets are intuitionistic fuzzy sets, Fuzzy Sets Systems 79 (1996) 403–405, https://doi.org/10.1016/0165-0114(95)00154-9.

[18] A. Lu, W. Ng, Vague sets or intuitionistic fuzzy sets for handling vague data: which one is better?, Springer Berlin Heidelberg, Berlin, Heidelberg, 2005, pp. 401–416.

[19] W.L. Gau, D.J. Buehrer, Vague sets, IEEE Trans. Syst. Man Cybernetics 23 (1993) 610–614.

[20] X.H. Li, G.O. Liu. Y.O. Zhao. Land exploitation and consolidation proiect evaluation based on vague set theory, Chinese Control Decision Conference (CCDC) 2016 (2016) 155–160, https://doi.org/10.1109/CCDC.2016.7530972.

[21] S.M. Chen, Similarity measures between vague sets and between elements, IEEE

Trans. Syst. Man Cybernetics 27 (1997) 153–158, https://doi.org/10.1109/3477. 552198.

[22] D.H. Hong, C. Kim, A note on similarity measures between vague sets and between elements, Information Sci. 115 (1999) 83–96, https://doi.org/10.1016/S0020- 0255(98)10083-X

[23] F. Li, Z. Xu, Measures of similarity between vague sets, J. Software 12 (2001) 922–927.

[24] A. Lu, W. Ng, Managing Merged Data by Vague Functional Dependencies, Springer Berlin Heidelberg, Berlin, Heidelberg, 2004, pp. 259–272.

[25] E. Szmidt, J. Kacprzyk, Distances between intuitionistic fuzzy sets, Fuzzy Sets Syst. 114 (2000) 505–518, https://doi.org/10.1016/S0165-0114(98)00244-9.

[26] D. Zhang, J. Zhang, K.K. Lai, Y. Lu, An novel approach to supplier selection based on vague sets group decision, Expert Systems Appl. 36 (2009) 9557–9563, https:/ doi.org/10.1016/j.eswa.2008.07.053

[27] Z. Xu, Intuitionistic fuzzy aggregation operators, IEEE Trans. Fuzzy Syst. 15 (2007) 1179–1187, https://doi.org/10.1109/TFUZZ.2006.890678.

[28] S.K. De, R. Biswas, A.R. Roy, Some operations on intuitionistic fuzzy sets, Fuzzy Set Syst. 114 (2000) 477–484, https://doi.org/10.1016/S0165-0114(98)00191-2.

[29] Q. Li, A novel likert scale based on fuzzy sets theory, Expert Syst. Appl. 40 (2013) 1609–1618, https://doi.org/10.1016/j.eswa.2012.09.015.

[30] Z. Xu, H. Liao, Intuitionistic fuzzy analytic hierarchy process, IEEE Trans. Fuzzy Syst. 22 (2014) 749–761, https://doi.org/10.1109/TFUZZ.2013.2272585.

[31] J. Wang, J. Zhang, S.Y. Liu, A new score function for fuzzy mcdm based on vague set theory, Int. J. Comput. Cognition 4 (2006).

[32] H. Tsai, S. Yeung, P.H.L. Yim, Hotel selection criteria used by mainland chinese and foreign individual travelers to hong kong, Int. J. Hospital. Tourism Administ. 12 (2011) 252–267. https://doi.org/10.1080/15256480.2011.590738

[33] S.H. Zanakis, A. Solomon, N. Wishart, S. Dublish, Multi-attribute decision making: A simulation comparison of select methods, Eur. J. Operat. Res. 107 (1998) 507–529, https://doi.org/10.1016/S0377-2217(97)00147-1.

[34] E. Mulliner, N. Malys, V. Maliene, Comparative analysis of mcdm methods for the assessment of sustainable housing afordability, Omega 59 (2016) 146–156, https://doi.org/10.1016/j.omega.2015.05.013.

[35] E. Bernroider, V. Stix, A method using weight restrictions in data envelopmen analysis for ranking and validity issues in decision making, Comput. Operat. Res. 34 (2007) 2637–2647, https://doi.org/10.1016/j.cor.2005.10.005.

[36] T. Kuo, A modified topsis with a diferent ranking index, Eur. J. Operat. Res. 260 (2017) 152–160, https://doi.org/10.1016/j.ejor.2016.11.052.

[37] S.-M. Chen, J.-M. Tan, Handling multicriteria fuzzy decision-making problems based on vague set theory, Fuzzy Sets Syst. 67 (1994) 163–172, https://doi.org/10. 1016/0165-0114(94)90084-1

[38] D.H. Hong, C.-H. Choi, Multicriteria fuzzy decision-making problems based on vague set theory, Fuzzy Sets Syst. 114 (2000) 103–113, https://doi.org/10.1016 S0165-0114(98)00271-1

[39] D. Kannan, A.B.L. de Sousa Jabbour, C.J.C. Jabbour, Selecting green suppliers based on gscm practices: Using fuzzy topsis applied to a brazilian electronics company, Eur, J. Operat, Res, 233 (2014) 432–447.

![](/api/attachments/AUKN86MG/fulltext/images/a573986232a9ab636db41047f6eaa019f18ad3ee02273a4bc05431680b67402f.jpg)  
P.K. Kwok graduated from The University of Hong Kong with a B.Eng. degree in Logistics Engineering and Supply Chain Management and a Ph.D. degree in the Department of Industrial and Manufacturing Systems Engineering. His research interests include multi-criteria decision making, group decision making, decision analytics, virtual reality, discrete-event simulation and crisis management. P.K. Kwok was a research assistant in the in the Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong. He is now an assistant professor in the School of Intelligent Systems Science and Engineering, Jinan University, China.

![](/api/attachments/AUKN86MG/fulltext/images/538d04e4e77ff86a4e3ba79342824d5f42deed6ee33b2f31c13ea7cc9b448c65.jpg)

Henry Y.K. Lau is an Associate Professor in the Department of Industrial and Manufacturing Systems Engineering, The University of Hong Kong. Henry graduated from the University of Oxford with a BA Degrees in Engineering Science and a DPhil in Robotics. Prior to joining The University of Hong Kong, he has been working in industry for many years as a Systems Engineer and Section Manager at the UK Atomic Energy Authority (UKAEA) and AEA Technology plc., working on projects involving bespoke tele-robotics systems and advanced automation systems for the nuclear industry in decommissioning and waste management. While working in England. Henry was a Croucher Foundation Research Fellow at the University of Oxford Robotics Research Group, and a visiting lecturer at

Brasenose College teaching Engineering Science. Henry's research interest includes arti ficial intelligence, in particular in artificial immune systems (AIS), intelligent automation for material handling, virtual and augmented reality systems
