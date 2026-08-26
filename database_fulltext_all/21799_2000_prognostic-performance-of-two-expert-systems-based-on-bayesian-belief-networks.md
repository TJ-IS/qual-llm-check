---
otero_id: 21799
otero_key: "KP6JXP5U"
title: "Prognostic performance of two expert systems based on Bayesian belief networks"
authors: "G.C Sakellaropoulos; G.C Nikiforidis"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00059-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Prognostic performance of two expert systems based on Bayesian belief networks

G.C. Sakellaropoulos, G.C. Nikiforidis <sup>),1</sup>

Computer Laboratory, School of Medicine, UniÕersity of Patras, GR-265 00 Rion-Patras, Greece

Accepted 20 September 1999

## Abstract

A decision support system for the prognosis at 24 h of head-injured patients of the intensive care unit ICU , based onŽ . Bayesian belief networks, is constructed by model selection methods applied to a database 637 cases of seven clinical andŽ . laboratory variables. Its performance is compared to other systems, including a simpler belief network that assumes conditional independence among the findings, and a human expert. Results indicate that its performance is not significantly different than that of the neurosurgeon expert and better than the performance of the independence model. Thus, the prognostic judgment of non-neurosurgeon ICU clinicians can be aided by the use of this system. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Decision support system; Expert system; Bayesian network; Head injury; Prognosis; ICU

## 1. Introduction

The task of estimating a head-injured patient’s prognosis involves the evaluation of many clinical and laboratory parameters. The clinician acts under uncertainty when he evaluates the available data to reach a patient’s prognosis. Yet, often clinical judgment is excellent, because people have proven their skill in managing uncertainty efficiently.

The human heuristic approach of combining evidence to reach a prognosis can deal successfully with a limited amount of evidence. The proliferation of large databases of patient findings, due to the increased use of computers in clinical settings, offers an abundance of available data, challenging the limited human capacity for indirect inference 18 . Deci-<sup>w</sup> <sup>x</sup> sion support systems that are able to model uncertainty and analyze diverse sources of information can therefore become a useful tool for medical experts.

The management of uncertainty in Medicine has been approached using many methodologies. Systems based on production rules did not manage to gain the acceptance of the clinicians, since the medical domain covers many problems that are very difficult to express with a set of rules. Consequently, their use in routine settings remained limited. Neural networks, on the other hand, while generally efficient, may sometimes lead to inconsistencies, e.g., diagnosis depending on the order in which findings are entered 5,23 .<sup>w</sup> <sup>x</sup>

Bayesian belief networks BNs are being increas-Ž . ingly used in the medical domain 3,21,22,35,39–<sup>w</sup> 42,48 as a knowledge representation for reasoning <sup>x</sup> under uncertainty. They permit the stepwise combination of prognostic evidence and provide a quantitative measure of belief in the final decision, in terms of probabilities values between 0 and 1 . Their Ž . ability to evaluate subjective evidence is compatible with routine clinical practice, since clinical and laboratory data are rarely of objective character.

BNs are graphs comprised of nodes and directed links. The nodes constitute probabilistic variables and the links represent the relation between two nodes. The links are quantified by a conditional probability matrix CP matrix that expresses the Ž . probabilistic relation between the outcomes of the parent node with the outcomes of the descendent child node.

The present study concerns the comparison of the performance of two BNs of different structure for the prognosis at 24 h of head-injured patients of the Intensive Care Unit ICU . The first naive BN isŽ . Ž . created under the assumption that all evidence variables are independent to each other given the patient’s outcome at 24 h, while to reach the second structure Ž . complex BN , we use data exploration methods to capture the conditional dependencies among the variables in a database. Two additional approaches are presented for comparison: the non-parametric method of k-nearest neighbors and a model for multiple logistic regression.

Despite the simplicity of its parametric form, the family of naive Bayes models is widely used in practice 3,21,22,39–42 . Published experimental ev-<sup>w</sup> <sup>x</sup> idence comparing naive and complex BNs is mixed. There exist studies that show an increase in diagnostic accuracy by considering some deviations from the naive model 49 , others find no statistically signifi- <sup>w</sup> <sup>x</sup> cant difference between the two approaches 52 , and <sup>w</sup> <sup>x</sup> some find naive BNs to be better 13,17 .<sup>w</sup> <sup>x</sup>

BNs that are supported by a database of patient records can capture the knowledge and experience acquired in years of medical practice in a big hospital and make it available to remote health care environments and to less experienced clinicians.

## 2. Material and methods

## 2.1. Database

The database contains the clinical and laboratory findings of 637 head injured patients of the Intensive Care Unit, collected during the period 1994–1998 in the University Hospital of Patras. The patient records were filled out by clinicians of the ICU and the Neurosurgery Department within the first hour after admission. For each patient, seven variables were recorded including actual outcome at 24 h as it is classified by the Glasgow Outcome Scale GOSŽ . <sup>w</sup> <sup>x</sup> 26 .

The choice upon the variables to include in the BNs Table 1 was made in accordance to generallyŽ . established opinion regarding their contribution to assessment of prognosis 2,6,19,20,26,31,38,44,51 . The outcomes were chosen so as to be mutually exclusive and cover the entire sample space. Continuous-valued variables were discretized with the appropriate choice of intervals.

The Glasgow Coma Scale GCS score wasŽ . recorded upon admission to the Hospital. Patients were intubated at the Emergency Department before entering the ICU. They either had GCS score in the range of 3–8 or their initial state in the range of 9–15 was deteriorating rapidly. For patients with CT scans showing more than one of the possible findings e.g., midline displacement and an edema the Ž . worst finding was taken into account for the previ-Ž ous example: midline displacement . In order to. reduce the subjectivity in the estimation of either GCS score or CT findings, the values entered in the database were the mean values of the estimations of seven experts in the corresponding fields Neurosur- Ž geons and Radiologists, respectively . The standard. deviation of their estimations was — as expected — very small, thus assuring the objective character of the information entered in the database. MAP was calculated as the weighted average of systolic SBPŽ . and diastolic DBP blood pressure at admissionŽ . <sup>w</sup>MAP<sup>s</sup>Ž . SBP<sup>q</sup>2<sup>=</sup>DBP <sup>r</sup>3 . The entire range of<sup>x</sup> MAP was divided into three intervals: below 60 mm Hg, between 60 and 120 mm Hg and above 120 mm Hg.

Table 1  
The variables included in the belief networks The clinical and laboratory variables included in the belief network, with their respective outcomes. The outcomes were chosen so as to be mutually exclusive and exhaust the sample space.

<table><tr><td colspan="2">GOS</td><td colspan="2">GCS</td></tr><tr><td>Outcome 1</td><td>Death</td><td>Outcome 1</td><td>Score 3–4</td></tr><tr><td>Outcome 2</td><td>Vegetative state</td><td>Outcome 2</td><td>Score 5–7</td></tr><tr><td>Outcome 3</td><td>Severe disability</td><td>Outcome 3</td><td>Score 8–10</td></tr><tr><td>Outcome 3</td><td>Moderate disability</td><td>Outcome 4</td><td>Score 11–13</td></tr><tr><td>Outcome 4</td><td>Good recovery</td><td>Outcome 5</td><td>Score 14–15</td></tr><tr><td colspan="2">Computerized Tomography (CT)</td><td colspan="2">Age</td></tr><tr><td>Outcome 1</td><td>Midline displacement</td><td>Outcome 1</td><td>0–10 years</td></tr><tr><td>Outcome 2</td><td>Mass lesion &gt;25 cm $^{3}$ </td><td>Outcome 2</td><td>11–20 years</td></tr><tr><td>Outcome 3</td><td>Mass lesion &lt;25 cm $^{3}$ </td><td>Outcome 3</td><td>21–40 years</td></tr><tr><td>Outcome 4</td><td>Edema</td><td>Outcome 4</td><td>41–60 years</td></tr><tr><td>Outcome 5</td><td>No findings</td><td>Outcome 5</td><td>more than 60 years</td></tr><tr><td colspan="2">Mean arterial pressure (MAP) [(SBP + 2DBP)/3]</td><td colspan="2">Delay (time lapsed between injury and admission)</td></tr><tr><td>Outcome 1</td><td>Less than 60 mm Hg</td><td>Outcome 1</td><td>Less than 2 h</td></tr><tr><td>Outcome 2</td><td>60–120 mm Hg</td><td>Outcome 2</td><td>2–6 h</td></tr><tr><td>Outcome 3</td><td>Greater than 120 mm Hg</td><td>Outcome 3</td><td>more than 6 h</td></tr><tr><td colspan="4">Pupil response</td></tr><tr><td>Outcome 1</td><td>Both pupils mydriatic</td><td></td><td></td></tr><tr><td>Outcome 2</td><td>Unequal pupillary size</td><td></td><td></td></tr><tr><td>Outcome 3</td><td>Normal</td><td></td><td></td></tr></table>

## 2.2. Bayesian networks

BNs 46 are directed acyclic graphs, consisting of <sup>w</sup> <sup>x</sup> nodes, representing random variables, and arcs, representing probabilistic dependencies between these variables Figs. 1 and 2 . Each node contains aŽ . conditional probability distribution of the form $P ( x / \pi _ { x } )$ in the CP matrix that describes the relationship between the variable x and its parents $\pi _ { x }$ Žthis includes the prior probabilities of the variables that have no parents . Each element of this matrix. expresses the probability of a child outcome given a combination of parental outcomes.

The main independence assumption represented by a BN is that each node is independent of all its non-descendent nodes, given its parents. This causes the joint probability distribution expressed by the BN to decompose into a product of local conditional distributions:

$$
P \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) = \prod_ {i = 1} ^ {n} P \left(x _ {i} \mid \pi_ {x _ {i}}\right).
$$

The decision upon how many outcomes a variable is assigned affects the structure of the conditional probability tables. If one assigns many outcomes to a variable that will acquire a parental position in the network, the total sample is divided in many parts and the probabilities are calculated over a smaller number of cases. In addition, some combinations of conditioning events may be extremely rare and thus the expert — that commonly provides these probabilities — may not be comfortable assessing some of the probabilities in the conditional probability table.

![](/api/attachments/KP6JXP5U/fulltext/images/2aa249706d5a6b61811b5b862c464edf3edc8a01aa38487f35f4c872c421ff0c.jpg)  
Fig. 1. The naive BN. Its structure is based on the assumption of conditional independence of the findings, given the patient’s outcome at 24 h.

![](/api/attachments/KP6JXP5U/fulltext/images/2dcbfb79e387cdcb97b6778800b83d23ac23cc104e22de80173487e4f3463acc.jpg)  
Fig. 2. The complex BN. Its architecture is reached with the use of statistical tests for conditional independence of the variables, as the result of an incremental search among the possible models. Applying the method of forward inclusion of edges, each edge not present in the initial model is added to the model and the current model is tested against the resulting model. This procedure is repeated until all edges found to be significant have been added to the model. Absence of an edge connecting two variables denotes that the two variables are independent, given the rest of the variables.

In our study, the CP matrices were calculated from the frequency counts of the database of findings. In order for the inference mechanism of the software we used to function properly, no matrix element should be zero, although there are possible configurations of patient findings that do not exist in our database.

As an example, consider the BN of Fig. 2. The CP matrix of node GOS contains elements of the form $p ( \mathrm { G O S } = i | \mathrm { C T } = j , \mathrm { G C S } = k )$ , for all combinations of i, j, k with $i , ~ j , ~ k \in \{ 1 , 2 , 3 , 4 , 5 \}$ . To calculate the probability pŽGOS<sup>s</sup>4 CT<sup><</sup> <sup>s</sup>1, GCS<sup>s</sup>1. from frequency counts, one needs to count the number of database entries that meet the criteria GOSŽ <sup>s</sup>4 and CT<sup>s</sup>1 and GCS<sup>s</sup>1 and divide them by the . number of entries that exhibit CTŽ . <sup>s</sup>1 and GCS<sup>s</sup>1 . If no entries with the combination GOSŽ <sup>s</sup>4 and CT<sup>s</sup>1 and GCS<sup>s</sup>1 exist in our database, the. corresponding element obtains the value zero. In such rare cases, we assigned the value of 1% to the corresponding conditional probability, knowing that

BNs are relatively insensitive to imprecisions in these quantities 25 .<sup>w</sup> <sup>x</sup>

BNs are used to facilitate probabilistic inference. Every time that a new piece of evidence is available, it is introduced to the BN and causes an update of the belief in the various prognostic outcomes. In other words, the system calculates the posterior probability of the prognostic outcomes, given the specific evidence.

## 2.3. Determination of complex BN’s architecture

The development of a BN for the prognosis of head-injured patients involves the determination of the network’s architecture and the calculation of the CP matrices that facilitate the inference mechanism.

A number of techniques for learning from data have been developed 4,24 , based on Bayesian <sup>w</sup> <sup>x</sup> methods 9 or on concepts of information theory <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 7,32 . In this study we treat the clinical problem of prognosis as a multivariate statistical analysis of discrete data, approached through a graphical log– linear model. The term log–linear stems from the fact that the probability density function is given as a log–linear expansion. If we restrict ourselves to the subclass of decomposable graphical log–linear models, we can use model selection methods to reach a graphical model compatible with our data and then transform it into an equivalent BN.

Graphical log–linear models 8,15,53 are probability models for multivariate random observations whose independence structure is characterized by a graph, the conditional independence graph. The conditional independence graph consists of a set of vertices, corresponding to our clinical or laboratory variables, and a set of undirected edges that connect pairs of vertices. Each missing edge denotes that the two unconnected variables are independent, conditioned on the rest. Decomposable graphical models have the property that their density function can be factorized under a numbering of the vertices 27 .<sup>w</sup> <sup>x</sup> This numbering guarantees that for every vertex in the graph, its lower-indexed adjacent vertices form complete sets, i.e., sets with all vertices joined. By directing all existing edges from vertices of lower index to vertices of higher index, we obtain a directed graph whose Markov properties 12,36 are<sup>w</sup> <sup>x</sup> identical to those of the undirected one. The localŽ .

Markov property for directed graphs 28,33 says that<sup>w</sup> <sup>x</sup> a vertex is independent of its non-descendants, given its parents, i.e., the main independence statement represented by a BN.

The search among the space of decomposable models can be made with different techniques that result in either a set of acceptable models 16 or in<sup>w</sup> <sup>x</sup> one model that is the best model according to some criterion. In this study, we use the method of forward inclusion of edges 14 . It is a sequential procedure, <sup>w</sup> <sup>x</sup> since it assumes a current model and looks to add or delete edges one at a time to that model. The forward inclusion process begins by considering the model with all variables independent main effects modelŽ . and seeing how the quality of data description is affected by adding each edge in turn, i.e., by assuming lack of conditional independence. Edges that meet a predefined criterion are eligible for inclusion and the most significant edge is added. This process is repeated until no edge is significant for inclusion.

The criterion used is the significance of the statistics for testing the current model against the larger models in which one additional edge has been added. Significance of test statistics was measured by their p-values. The edge that has the most significant test statistic — and does not already exist in the model — is added; the process continues until no edge achieves the 0.05 level of significance.

The test statistic usually used in the forward inclusion procedure is the deviance difference theŽ difference of the log-likelihood , which has a chi- . squared distribution as the sample size tends to infinity. Strictly, it is valid only in large samples and in case of sparse tables, i.e., tables including many cells possible variables’ configurations with zero Ž . counts, the results may be unreliable. Hence, we used Monte Carlo approximations of the exact p-values 30,45 , from the conditional distribution of the<sup>w</sup> <sup>x</sup> test statistics given the sufficient marginals under the hypothesis.

Model selection was performed using the program CoCo 1 . The patient cases were imported to CoCo <sup>w</sup> <sup>x</sup> from the software that keeps the patient database, after a filter was applied to establish compatibility in the data format. The search was limited in the space of decomposable models. The undirected model selected using CoCo was then transformed into directed acyclic graph by forcing all the edges from vertices of lower index to point to vertices of higher index.

The resulting BN structure Fig. 2 and all theŽ . necessary CP matrices calculated from the databaseŽ . were then introduced to the DXpress graphical network editor and compiled using the DXpress inference engine.

## 2.4. Inference

The general problem of inference in BNs is proven to be NP-hard 10,11 but efficient local computa-<sup>w</sup> <sup>x</sup> tions algorithms have been developed 27,34,54 . We<sup>w</sup> <sup>x</sup> are interested in the posterior belief in the GOS outcomes as new evidence regarding the rest of the variables becomes available. Information from the clinical or laboratory examination of the patient is entered to the two BNs and propagates through the network to reach the GOS node. Each piece of evidence has a different impact on the GOS outcomes, depending on both the relative position of the evidence node to the GOS node and to the conditional probability matrices along the route from the evidence node to the GOS node. The two BNs exhibit therefore different responses to the same evidence and the underlying reason for this is that different conditional independence assumptions have been made during their construction.

## 2.5. Validation

The prognostic performance of the belief networks was evaluated using the actual outcome at 24 h as gold standard. Their performance is compared with expert’s opinion and two other techniques that are known to perform very well in classification tasks 37 , namely<sup>w</sup> <sup>x</sup> k-nearest neighbors and polychotomous regression 29 .<sup>w</sup> <sup>x</sup>

k-nearest neighbors is a non-parametric classification technique in which the k closest examples in the training set are found and the distribution of their GOS outcomes provides the estimate of the test case’s prognostic outcome. Proximity between examples is determined with Euclidean measures of distance in the six-dimensional space of the predictive variables. We experimented on the choice of k and found that k<sup>s</sup>3 gave the best results. Polychotomous regression, on the other hand, fits a polychotomous logistic regression model using linear splines and their tensor products. It provides estimates for conditional outcome probabilities, which can be used to predict GOS outcomes.

Instead of using a particular set of cases for testing, we used a 10-fold cross validation 50<sup>w</sup> <sup>x</sup> scheme for validating the models. This divides the entire data set in 10 mutually exclusive parts at random. Then each part in turn is kept as the test set and the remaining cases are used for fitting and to predict those in the test set. When this is performed 10 times, every case has been predicted and the performance computed. It is a technique generally applied when the data sets are relatively small. In our case, it is used to overcome the small number of patients of the ‘‘vegetative state’’ outcome.

## 3. Results

The evaluation of performance of the two BNs is twofold:

Ž .i identical evidence were introduced to the BNs and their response regarding the posterior beliefs in the prognostic outcomes was recorded.

Ž . Ž ii a varying collection of cases due to cross validation was introduced to DXpress to perform . inference on the two BNs. The predictions of the GOS outcome were compared to the actual outcome and to the predictions made by the other systems.

Table 2 shows the degree of sensitivity of GOS node due to a finding at another node. Two quantities were measured, the mutual information 46 or<sup>w</sup> <sup>x</sup> Ž entropy reduction and the quadratic score 43 . The. <sup>w</sup> <sup>x</sup> mutual information between GOS and another variable equals the expected reduction in entropy of GOS due to a finding in another variable. It obtains its minimum value 0 if the variable is independentŽ . of GOS, while its maximum equals the entropy of GOS base value in Table 2 . The quadratic scoring Ž . shows the expected difference between the distribution at GOS without a finding in another variable, to the distribution of GOS with the finding. Its minimum value is zero if the variable is independent of GOS and its maximum value is one. The variables are shown in descending order of strength.

The prior belief in each GOS outcome is identical to the relative frequency of occurrence of the corresponding GOS outcome in the training set of the database and it is therefore common to both structures. In other words, 38.2% of the 637 patients of the training set actually died or were in vegetative state at 24 h, while 24.9% fully recovered.

Fig. 3 shows the response of the two BNs after patterns of evidence are introduced. A patient observed to have pupils of unequal size and CT showing midline displacement is assigned a 61.1% probability of death within 24 h by the complex BN while the naive BN supports the same outcome with 70.7% probability.

If the patient has pupils of unequal size her CT shows an edema and she is in coma GCSŽ . <sup>s</sup>5 to 7 , the two BNs favor different outcomes. The complex BN supports the ‘‘death’’ outcome, while with the same evidence the naive BN selects ‘‘good recovery’ as the most probable outcome.

Table 2  
Sensitivity of ‘‘GOS’’ due to a finding at another node  
The degree of sensitivity of GOS node due to a finding at another node. Two quantities were measured, the mutual information or entropy Ž reduction and the quadratic score. The variables are shown in descending order of strength..

<table><tr><td colspan="3">Complex BN</td><td colspan="3">Naive BN</td></tr><tr><td>Node</td><td>Mutual information</td><td>Quadratic score</td><td>Node</td><td>Mutual information</td><td>Quadratic score</td></tr><tr><td colspan="3">Base value 1.87</td><td colspan="3">Base value 1.87</td></tr><tr><td>CT</td><td>0.31771</td><td>0.0985610</td><td>CT</td><td>0.20702</td><td>0.0335458</td></tr><tr><td>PUPIL</td><td>0.30235</td><td>0.0767133</td><td>PUPIL</td><td>0.20647</td><td>0.0375259</td></tr><tr><td>GCS</td><td>0.19838</td><td>0.0369472</td><td>GCS</td><td>0.09126</td><td>0.0163234</td></tr><tr><td>MAP</td><td>0.05621</td><td>0.0060566</td><td>MAP</td><td>0.03623</td><td>0.0060612</td></tr><tr><td>DELAY</td><td>0.02285</td><td>0.0020431</td><td>AGE</td><td>0.03534</td><td>0.0055444</td></tr><tr><td>AGE</td><td>0.00951</td><td>0.0015747</td><td>DELAY</td><td>0.02285</td><td>0.0020438</td></tr></table>

![](/api/attachments/KP6JXP5U/fulltext/images/a5e1c6deeaeb62d8ce2a56a7e96f7b93ce073542ad717393c52751d6daee1f2a.jpg)  
Fi<sub>g</sub> . 3 . Th<sub>e</sub> diff<sub>eren</sub>t <sub>responses o</sub>f th<sub>e</sub> t<sub>wo</sub> BN<sub>s w</sub>h<sub>en presen</sub>t<sub>e</sub>d <sub>w</sub>ith th<sub>e same ev</sub>id<sub>ence</sub>. F<sub>or a pa</sub>ti<sub>en</sub>t <sub>w</sub>ith <sub>unequa</sub>l <sub>pup</sub>il<sub>s an</sub>d CT <sub>scan s</sub>h<sub>ow</sub>i<sub>ng m</sub>idli<sub>ne</sub> di<sub>sp</sub>l<sub>acemen</sub>t b<sub>o</sub>th BN<sub>s</sub> favor the <sup>‘ ‘</sup> death<sup>’ ’</sup> outcome with var<sub>y</sub>in<sub>g</sub> beliefs The initial belief in death 3 6 1 % is boosted with these <sub>p</sub>ieces of evidence to 6 1 1 % com<sub>p</sub>lex BN or to 7Ž . Ž . Ž .0 7 % naive BN For a <sub>p</sub>atient in coma GCS 5 to 7 with une<sub>q</sub>ual <sub>p</sub>u<sub>p</sub>ils and CT showin<sub>g</sub> edema the two BNs <sub>p</sub>redict different outcomes . The com<sub>p</sub>lex BN shows that beliefs in <sub>g</sub>oŽ . od and moderate recover outcomes are reduced in favor of more severe outcomes The <sup>‘ ‘</sup> death<sup>’ ’</sup> outcome receives the hi hest belief 3 1 8% The naive BN followŽ . s the o osite route <sub>;</sub> it reduces the belief in the <sup>‘ ‘</sup> death<sup>’ ’</sup> outcome and <sub>p</sub>redicts <sub>g</sub>ood recover<sub>y</sub> 34. 1 % . It also assi<sub>g</sub>ns lar<sub>g</sub>e beliefs to moderate disabilities 28 .4% .Ž . Ž .

Table 3  
The average predictive performance of the five systems under study, after 10-fold cross validation  
The performance of the systems under study. 3-nearest neighbors exhibits the best performance, followed by the human expert. The complex BN performs better than the naive, while its difference with the human expert’s is insignificant. Both BNs exhibit better success rates in either of the extreme outcomes death — good recovery .Ž .

<table><tr><td rowspan="2">Actual outcome at 24 h</td><td rowspan="2">Number of cases</td><td colspan="5">Success rate (%)</td></tr><tr><td>Human expert</td><td>Complex BN</td><td>Naive BN</td><td>3-Nearest neighbors</td><td>Polychotomous logistic regression</td></tr><tr><td>Death</td><td>230</td><td>83</td><td>85</td><td>72</td><td>95</td><td>71</td></tr><tr><td>Vegetative state</td><td>15</td><td>77</td><td>62</td><td>53</td><td>90</td><td>49</td></tr><tr><td>Severe disability</td><td>90</td><td>86</td><td>76</td><td>59</td><td>85</td><td>81</td></tr><tr><td>Moderate disability</td><td>143</td><td>81</td><td>68</td><td>53</td><td>87</td><td>72</td></tr><tr><td>Good recovery</td><td>159</td><td>82</td><td>89</td><td>67</td><td>93</td><td>80</td></tr><tr><td>Overall</td><td>637</td><td>83</td><td>80</td><td>64</td><td>91</td><td>74</td></tr></table>

This is an example of network activations that lead to the assignment of large posterior beliefs to two diametrically opposing outcomes death and goodŽ recovery . While it is intuitively easy to identify a. trend when the BNs assign competing beliefs to neighboring prognostic outcomes, cases like these seem to lead to contradictions. The reason for this is that some patterns of evidence are compatible with both patients that died at 24 h and with patients that exhibited a good recovery. Apart from that, the reader should bear in mind that the prior belief in the GOS outcomes is not uniformly distributed, and therefore not all possible patterns of evidence will produce updated beliefs that will follow a clear trend towards one outcome.

Table 3 shows analytically the performance of the systems under study. The 3-nearest neighbors method exhibited the best performance 91% success rate , Ž . followed by the human expert 83% and the com- Ž . plex BN 80% . Polychotomous regression correctly Ž . predicted the patient’s outcome in 74% of the cases, while the naive BN in 64%. All the above differences are significant $( p < 0 . 0 1 )$ , except for that between the human expert and the complex BN Ž p<sup>)</sup> 0.05 . The success rate of the complex BN is better . than the success rate of the naive BN in all GOS outcomes, while both exhibit their best success rates in the extreme outcomes death — good recovery .Ž .

The performance of the three parametric methods is consistent with the complexity of the assumptions they make. Polychotomous regression can be viewed as an extension to the naive BN but it does not take into account the interactions among the predictors, as the complex BN does. The complex BN uses the database of findings for this purpose and is therefore more compatible with the specific population of patients. If one is not interested in making qualitative assessments e.g., conditional independence state- Ž ments , it is always tempting to use ‘‘black box’’ . techniques likeŽ k-nearest neighbors or neural networks for classification purposes due to their very. good performance.

Table 4  
The percentage of times the BNs were surprised  
The ‘‘Times Surprised’’ table. The columns <sup>)</sup>90% and <sup>-</sup>10% indicate the level of belief that the BNs assign to an outcome. The ratios indicate the number of times the BN was wrong out of the number of times it made such a confident prediction.

<table><tr><td rowspan="3">GOS outcome</td><td colspan="6">Predicted probability (belief)</td></tr><tr><td colspan="3">&lt; 10%</td><td colspan="3">&gt;90%</td></tr><tr><td>Complex BN</td><td>Naive BN</td><td>Significance of difference</td><td>Complex BN</td><td>Naive BN</td><td>Significance of difference</td></tr><tr><td>Death</td><td>3.96% (4/101)</td><td>9.95% (19/191)</td><td>p&lt;0.05</td><td>9.09% (4/44)</td><td>10.59% (9/85)</td><td>p&gt;0.05</td></tr><tr><td>Vegetative state</td><td>1.04% (6/578)</td><td>2.38% (15/630)</td><td>p&lt;0.05</td><td>0.00% (0/0)</td><td>0.00% (0/0)</td><td>-</td></tr><tr><td>Severe disability</td><td>2.67% (6/225)</td><td>7.99% (25/313)</td><td>p&lt;0.005</td><td>0.00% (0/0)</td><td>0.00% (0/0)</td><td>-</td></tr><tr><td>Moderate disability</td><td>5.70% (11/193)</td><td>6.06% (12/198)</td><td>p&gt;0.05</td><td>0.00% (0/0)</td><td>0.00% (0/0)</td><td>-</td></tr><tr><td>Good recovery</td><td>3.08% (6/195)</td><td>6.87% (16/233)</td><td>p&lt;0.05</td><td>0.00% (0/0)</td><td>0.00% (0/4)</td><td>-</td></tr><tr><td>Total</td><td>2.55% (33/1292)</td><td>5.56% (87/1565)</td><td>p&lt;0.001</td><td>9.09% (4/44)</td><td>10.11% (9/89)</td><td>p&gt;0.05</td></tr></table>

Table 4 shows another aspect of the performance of the two BNs, namely how often the BNs were quite confident in their beliefs, but were wrong. The complex BN is more accurate than the naive for those cases that it assigned beliefs smaller than 10%. For example, the complex BN assigned less than 10% belief in the outcome ‘‘death’’ in 101 cases. In four of them 3.96% , it was wrong because ‘‘death’’ Ž . was the real outcome. The corresponding error for the naive BN was 9.95%. Except for estimations of the ‘‘moderate disability’’ outcome, such error rates are significantly different for the two BNs, in favor of the complex.

The complex BN also exhibits a better calibration. Fig. 4 shows the observed relative frequency of an outcome for the corresponding amount of belief assigned to this outcome. For example, of all the times the naive BN assigned belief equal to 70% to an outcome, that outcome was really observed in 55% of them. An optimal classification method would follow the diagonal of this graph. The proximity to the diagonal is therefore a measure of calibration of the method under study. The complex BN is evidently closer to the diagonal than the naive BN.

![](/api/attachments/KP6JXP5U/fulltext/images/c10747ee469203477b750555102fbec5fe787b2b1ffe7a55061a84e0eaf07a6a.jpg)  
Fig. 4. The calibration curve indicates whether the belief expressed by the BNs are appropriate. It shows the observed relative frequency of outcomes for a given level of belief in that outcome. The calibration curve of an optimal system would coincide with the diagonal of the graph. The complex BN’s calibration curve is closer to the diagonal than the naive’s.

## 4. Concluding remarks

This study concerns the investigation of the performance of alternative methodologies for the estimation of patients’ prognosis. While other techniques e.g., 3-nearest neighbors proved to be excel-Ž . lent for this task, our main interest lies in the domain of Bayesian probabilistic approaches for reasons other than performance.

It is the consistent agreement between plausible reasoning and probability calculus that suggests that human intuition invokes some form of probabilistic computation. Reasoning takes place when our knowledge embodies conditional independence assumptions. Graphical methods make it easy to represent such assumptions and to maintain consistency and completeness in probabilistic knowledge bases. Independencies among the variables can be dealt explicitly, during the designing as well as in the reasoning phase. BNs have formal probabilistic semantics and, yet, can serve as a natural mirror of knowledge structures in the human mind 47 . This<sup>w</sup> <sup>x</sup> facilitates the encoding and interpretation of knowledge in terms of a probability distribution, enabling inference and optimal decision making. Additionally, BN systems are interactive and can cope with incomplete evidence; the clinician directly observes the impact of new evidence as they become available and thus evaluates the predictive strength of each clinical and laboratory finding.

While the performance of neither BN is better than the expert neurosurgeon’s in predicting the outcome of head injured patients at 24 h, the benefit of using such an analytical system is expected to be more substantial when used by non-experts. The knowledge embodied in the system reflects the experience gathered by a large-scale clinical setting and the patient management of skilled clinicians. When used in remote health units, where neurosurgeons are not available, the system transfers this knowledge to the local medical doctors.

The expert system based on the complex BN is being used by expert neurosurgeons for the last 6 months. An evaluation scheme is under construction, involving a number of criteria regarding the system’s efficiency as well as the ease of use and satisfaction of the users. It will cover the issues of time response of the system, the accuracy of the information it provides, its ability to support critical question answering and its usefulness. Preliminary reactions by the users show that they consider it a useful tool supporting their decisions. They value the system’s ability for quantitative assessments of prognosis and for displaying the gradual acquisition of belief after each entry of clinical or laboratory observation. Additionally, they find useful the system’s ability to respond to fictitious cases with incomplete patient findings, acting as a simulator.

We believe that for a decision support system to become attractive to the end user and become a tool in his<sup>r</sup>her everyday routine, clarity of the techniques used and relevance of these techniques to the end user’s own ways of information processing are needed. BNs adopt a procedure of information evaluation that resembles the way medical doctors have been educated to value information and reach judgments. The calculation of post-test probabilities for each clinical or laboratory test performed and the successive incorporation of the patient under study to a different sub-population is a procedure that is implicitly performed although often not accuratelyŽ . in everyday clinical practice. BNs offer a clear representation of this process.

The maintenance of a database containing many variables related to the specific domain is essential, since the database provides both the training set for a possible structure and objective values for the CP matrices. The prognostic performance of a complex BN is expected to be more sensitive to database characteristics than that of the naive BN, since its structure is determined by conditional independence tests between the variables in the database. Two variables are connected in the BN when the appropriate statistical test fails to support the conditional independence of the two variables given the rest. Since the test uses the database records for the calculations, possibly different structures in terms ofŽ connections among the variables are expected to be. selected by the algorithm as the database grows in size.

The expert’s belief in the patient’s outcome at 24 h was recorded after all available information regarding each case was gathered. The cases were classified according to the expert’s belief in one of the five prognostic outcomes. The other system BNs were then fed with exactly the same evidence that the expert had at his disposal. The BNs calculated exact probabilities and therefore the cases were categorized according to the most favored outcome out-Ž come with maximum probability ..

Clinicians can benefit from the ability of the model selection techniques to investigate the existence of conditional dependence between pairs of clinical or laboratory variables and consult other sources of evidence to estimate the patient’s prognosis.

## References

<sup>w</sup> <sup>x</sup> 1 J.H. Badsberg, Model search in contingency tables by CoCo, in: Y. Dodge, J. Whittaker Eds. , Computational Statistics,Ž . COMPSTAT 1992, Neuchatel, Physica Verlag, Heidelberg, 1992, p. 251–256.

<sup>w</sup> <sup>x</sup>2 P. Barlow, L. Murray, G. Teasdale, Outcome after severe head injury — the Glasgow model, in: W.A. Corbett Ed. ,Ž . Medical Applications of Microcomputers, Wiley, 1987, p. 105–126.

<sup>w</sup> <sup>x</sup> 3 M. Bibbo, P.H. Bartels, T. Pfeifer, D. Thompson, C. Minimo, H.G. Davidson, Belief network for grading prostate lesions, Analytical and Quantitative Cytology and Histology 15 1993 124–135.Ž .

<sup>w</sup> <sup>x</sup> 4 W.L. Buntine, Operations for learning with graphical models, JAIR 2 1994 159–225.Ž .

<sup>w</sup> <sup>x</sup> 5 P. Cheeseman, In defense of probability, in: Proceedings of the 9th International Joint Conference on Artificial Intelligence, William Kaufmann, Los Angeles, 1985.

<sup>w</sup> <sup>x</sup> 6 S.C. Choi, R.K. Narayan, R.L. Anderson, J.D. Ward, Enhanced specificity of prognosis in severe head injury, J. Neurosurg. 69 1988 381–385.Ž .

<sup>w</sup> <sup>x</sup> 7 C.K. Chow, C.N. Liu, Approximating discrete probability distributions with dependence trees, IEEE Transactions on Information Theory IT-14 1968 462–467.Ž .

<sup>w</sup> <sup>x</sup> 8 R. Christensen, Log–Linear models, Springer-Verlag, 1990.

<sup>w</sup> <sup>x</sup> 9 G. Cooper, E. Herskovits, A Bayesian method for the induction of probabilistic networks from data, Machine Learning 9 Ž . 1992 309–347.

10 G.F. Cooper, The computational complexity of probabilistic inference using Bayesian belief networks, Artificial Intelligence 42 1990 393–405.Ž .

11 P. Dagum, M. Luby, Approximating probabilistic inference in Bayesian belief networks is NP-hard, Artificial Intelligence 60 1993 141–153.Ž .

<sup>w</sup> <sup>x</sup> 12 A.P. Dawid, S.L. Lauritzen, Hyper Markov laws in the statistical analysis of decomposable graphical models, Ann. Stat. 21 1993 1272–1317.Ž .

<sup>w</sup> <sup>x</sup> 13 F.T. de Dombal, The diagnosis of acute abdominal pain with computer assistance: worldwide perspective, Ann. Chir. 45 Ž . 1991 273–277.

<sup>w</sup> <sup>x</sup> 14 A.P. Dempster, Covariance selection, Biometrics 28 1972Ž . 157–175.

<sup>w</sup> <sup>x</sup> 15 D. Edwards, Introduction to Graphical Modelling, Springer-Verlag, 1995.

<sup>w</sup> <sup>x</sup> 16 D. Edwards, T. Havranek, A fast model selection procedure for large families of models, J. Am. Stat. Assoc. 82 1987Ž . 205–213.

<sup>w</sup> <sup>x</sup>17 F.H. Edwards, R.S. Davies, Use of a Bayesian algorithm in the computer-assisted diagnosis of appendicitis, Surg. Gynecol. Obstet. 158 1984 219–222.Ž .

<sup>w</sup> <sup>x</sup> 18 A.S. Elstein, Clinical judgment: psychological research and medical practice, Science 194 1976 696–700.Ž .

<sup>w</sup> <sup>x</sup> 19 Z. Feldman, C.F. Contant, C.S. Robertson, R.K. Narayan, R.G. Grossman, Evaluation of the Leeds prognostic score for severe head injury, Lancet 337 1991 1451–1453. Ž .

<sup>w</sup> <sup>x</sup> 20 R.M. Gibson, G.C. Stephenson, Aggressive management of severe closed head trauma: time for reappraisal, Lancet, 1989, 369–371.

<sup>w</sup> <sup>x</sup> 21 P.W. Hamilton, N. Anderson, P.H. Bartels, D. Thompson, Expert system support using Bayesian belief networks in the diagnosis of fine needle aspiration biopsy specimens of the breast, J. Clin. Pathol. 47 1994 329–336.Ž .

<sup>w</sup> <sup>x</sup> 22 N.L. Harris, Probabilistic belief networks for genetic counseling, Computer Methods and Programs in Biomedicine 32 Ž .1990 37–44.

<sup>w</sup> <sup>x</sup> 23 D. Heckerman, Probabilistic interpretations for MYCIN’s certainty factors, Uncertainty in Artificial Intelligence, North-Holland, 1986.

<sup>w</sup> <sup>x</sup> 24 D. Heckerman, D. Geiger, D. Chickering, Learning Bayesian Networks: the combination of knowledge and statistical data, Technical Report, Microsoft TR-94-09, 1994.

<sup>w</sup> <sup>x</sup> 25 M. Henrion, M. Pradhan, B. Del Favero, K. Huang, G. Provan, P. O’Rorke, Why is diagnosis using belief networks insensitive to imprecision in probabilities?, in: Proceedings of the 12th Conference on Uncertainty in Artificial Intelligence, Morgan Kaufmann, San Francisco, 1996.

<sup>w</sup> <sup>x</sup> 26 B. Jennett, M. Bond, Assessment of outcome after severe brain damage, Lancet i 1975 480–484.Ž .

<sup>w</sup> <sup>x</sup> 27 F.V. Jensen, S.L. Lauritzen, K.G. Olesen, Bayesian updating in causal probabilistic networks by local computations, Computational Statistics Quarterly 4 1990 269–282.Ž .

<sup>w</sup> <sup>x</sup> 28 H. Kiiveri, T.P. Speed, J.B. Carlin, Recursive causal models, J. Aust. Math. Soc. Series A 36 1984 30–52.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 C. Kooperberg, S. Bose, C.J. Stone, Polychotomous regression, J. Am. Stat. Assoc. 92 1997 117–127.Ž .

<sup>w</sup> <sup>x</sup> 30 S. Kreiner, Graphical modelling using DIGRAM, Research report 11<sup>r</sup>89, Statistical Research Unit, Univ. of Copenhagen 1989.

<sup>w</sup> <sup>x</sup> 31 J.A. Kruse, M.C. Thill-Baharozian, R.W. Carlson, Comparison of clinical assessment with APACHE II for predicting mortality risk in patients admitted in a medical intensive care unit, JAMA 260 1988 1739–1742.Ž .

<sup>w</sup> <sup>x</sup> 32 W. Lam, F. Bacchus, Learning Bayesian belief networks. An approach based on the MDL principle, Computational Intelligence 10 1994 269–293.Ž .

<sup>w</sup> <sup>x</sup> 33 S.L. Lauritzen, A.P. Dawid, B.N. Larsen, H.G. Leimer, Independence properties of directed Markov fields, Networks 20 1990 491–505.Ž .

<sup>w</sup> <sup>x</sup>34 S.L. Lauritzen, D.J. Spiegelhalter, Local computations with probabilities on graphical structures and their application to expert systems with discussion , J. R. Stat. Soc. B 50 1988Ž . Ž . 157–224.

<sup>w</sup> <sup>x</sup> 35 S.L. Lauritzen, B. Thiesson, D.J. Spiegelhalter, Lecture notes in Statistics 89, in: P. Cheeseman, R. Oldford Eds. , Select-Ž . ing Models from Data: Artificial Intelligence and Statistics IV, Springer Verlag, New York.

<sup>w</sup> <sup>x</sup> 36 S.L. Lauritzen, N. Wermuth, Graphical models for associations between variables, some of which are qualitative and some quantitative, Ann. Stat. 17 1989 31–57.Ž .

<sup>w</sup> <sup>x</sup> 37 T.S. Lim, W.Y. Loh, Y.S. Shih, A comparison of prediction accuracy, complexity and training time of thirty-three old and new classification algorithms, Machine Learning, to appear.

<sup>w</sup> <sup>x</sup> 38 T.G. Luerssen, M.R. Klauber, L.F. Marshall, Outcome from head injury related to patient’s age: a longitudinal prospective study of adult and pediatric head injury, J. Neurosurg. 68 Ž . 1988 409–416.

<sup>w</sup> <sup>x</sup> 39 R. Montironi, L. Diamanti, R. Pomante, D. Thompson, P.H. Bartels, Subtle changes in benign tissue adjacent toprostate neoplasia detected with a Bayesian belief network, Journal of Pathology 182 4 1997 442–449. Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 R. Montironi, P.H. Bartels, D. Thompson, L. Diamanti, E. Prete, Androgen-deprived prostate adenocarcinoma: evaluation of treatment-related changes versus no distinctive treatment effect with a Bayesian belief network. A methodological approach, European Urology 30 3 1996 307–315.Ž . Ž .

<sup>w</sup> <sup>x</sup> 41 R. Montironi, P.H. Bartels, P.W. Hamilton, D. Thompson, Atypical adenomatous hyperplasia adenosis of the prostate:Ž . development of a Bayesian belief network for its distinction from well-differentiated adenocarcinoma, Human Pathology 27 4 1996 396–407.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 R. Montironi, P.H. Bartels, D. Thompson, M. Scarpelli, P.W. Hamilton, Prostatic intraepithelial neoplasia PIN . Perfor-Ž . mance of Bayesian belief network for diagnosis and grading, Journal of Pathology 177 2 1995 153–162.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 R.E. Neapolitan, Probabilistic Reasoning in Expert Systems: Theory and Algorithms, Wiley, New York, 1990.

<sup>w</sup> <sup>x</sup> 44 C. Parkan, L. Hollands, The use of efficiency linear programs for sensitivity analysis in medical decision making, Med. Decision Making 10 1990 116–125.Ž .

<sup>w</sup> <sup>x</sup>45 W.M. Patefield, Algorithm AS 159. An efficient method of generating random r<sup>=</sup>c tables with given row and column totals, Applied Statistics 30 1981 91–97.Ž .

<sup>w</sup> <sup>x</sup> 46 J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufman, San Mateo, CA, 1988.

<sup>w</sup> <sup>x</sup> 47 J. Pearl, Causal diagrams for empirical research, Biometrika 82 1995 669–710.Ž .

<sup>w</sup> <sup>x</sup> 48 L. Roberts, C.E. Kahn Jr., P. Haddawy, Development of a Bayesian network for diagnosis of breast cancer, Working notes of the IJCAI workshop on building probabilistic networks, 1995.

<sup>w</sup> <sup>x</sup> 49 B. Seroussi, Computer-aided diagnosis of acute abdominal pain when taking into account interactions, Methods of Information in Medicine 25 1986 194–198.Ž .

<sup>w</sup> <sup>x</sup> 50 M. Stone, Cross-validatory choice and assessment of statistical predictions with discussion , J. R. Stat. Soc. Series BŽ . Ž . 36 1974 111–147.Ž .

<sup>w</sup> <sup>x</sup> 51 G. Teasdale, B. Jennett, Assessment of coma and impaired consciousness, A practical scale, Lancet, 1974, 81–84.

<sup>w</sup> <sup>x</sup> 52 B.S. Todd, R. Stamper, The relative accuracy of a variety of medical diagnostic programs, Methods of Information in Medicine 33 4 1994 402–416.Ž . Ž .

<sup>w</sup> <sup>x</sup> 53 J. Whittaker, Graphical Models in Applied Multivariate Statistics, Wiley, 1990.

<sup>w</sup> <sup>x</sup> 54 N.L. Zhang, D. Poole, Exploiting causal independence in Bayesian network inference, JAIR 5 1996 301–328.Ž .

George C. Sakellaropoulos, MSc. He received his Diploma in Physics in 1993 from the University of Athens, Greece. In 1995, he received his MSc in Medical Physics from the University of Patras, Greece. He is now finishing his PhD in Medical Informatics in the same University. His primary scientific interests lie in the application of Bayesian networks, decision support systems, data reduction and image analysis in Medicine. B&W Photography is his top leizure time activity.

George Nikiforidis was born in Athens, Greece in 1949. He received the Italian degree in Physics and the diploma of specialization in Atomic and Nuclear Physics, both from the University of Milan in 1973 and 1980, respectively and a PhD in Medical Physics, from the University of Patras, Greece in 1981. He became a Professor and Chairman of Medical Physics, University of Patras, in January 1997. Since 1996, he is Director of the Postgraduate course on Medical Physics, of the University of Patras. His research interests are in medical physics, mathematica modeling and biostatistics.
