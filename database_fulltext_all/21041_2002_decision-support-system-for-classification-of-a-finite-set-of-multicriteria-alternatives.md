---
otero_id: 21041
otero_key: "SX82C6VS"
title: "Decision support system for classification of a finite set of multicriteria alternatives"
authors: "O.I. Larichev; A.V. Kortnev; D.Yu. Kochin"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00132-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support system for classification of a finite set of multicriteria alternatives

O.I. Larichev <sup>a,</sup>\*, A.V. Kortnev <sup>a</sup>, D.Yu. Kochin <sup>b</sup>

<sup>a</sup>Institute for Systems Analysis, Russian Academy of Sciences, Prospect 60 let Octjabrja, 9, 117312 Moscow, Russia <sup>b</sup>Moscow Institute for Physics and Technology (Technical University), Dolgoprudniy, Institutskiy per., 9., 141700 Moscow, Russia

Received 1 January 2001; received in revised form 1 June 2001; accepted 1 July 2001

## Abstract

The paper presents a new decision method and a decision support system (DSS) for solving multicriteria classification problems: how to allocate alternatives having evaluations in the terms of several criteria into ordered decision classes. In contrast to previous statements of this problem, a relatively small subset of alternatives is presented for classification. The efficiency of the method is estimated as the minimum number of questions posed to the decision maker (DM) to accomplish the needed classification. The main ideas of the new method as well as its evaluation by a statistical modeling approach are presented in the paper. A practical example is given. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision maker; Decision support system; Multicriteria classification problems

## 1. Multicriteria classification problem in decision making

Along with multicriteria choice problems, people may face multicriteria classification problems. A feature of classification tasks is that it is not necessary to rank order the alternatives, but only to assign them to a small number of decision groups. Quite often these classes (or groups) may be rank-ordered, reflecting a different degree of quality. In this sense, the alternatives assigned to the first decision class are better than those assigned to the second class, and so on.

Such problems could be called problems of ordinal classification.

There are many practical tasks of this kind. One is the evaluation of applications for a loan in a bank. A bank officer is to decide which application is to be supported or rejected. Each applicant has different estimations in terms of several criteria. The problem for a bank manager is to define some rules for such decisions.

The second example is the evaluation of research units in a big research institute. Each team is evaluated over many criteria. The director of the institute has to make a comparative evaluation of research units assigning them to different categories by quality. The problem for the director is to define some rules for this classification.

The typical goal in such task is to assign alternatives to decision classes. In spite of the fact that classification tasks are widely spread in human decision making, their theoretical investigation within the framework of multicriteria decision making is scarce. De Montgolfier and Bertier [3] described a procedure of generalizing sets of attribute values into ordinal categories of a more general criterion on the basis of a decision maker’s judgment. This task may be viewed as that of ordinal classification. ELECTRE TRI [12] and the ROBOT Technique [1] are the most recent examples of an approach to ordinal classification based on the idea of assigning multiattribute alternatives to ordered classes.

One of the first methods and decision support systems (DSS) to find solution to the ordinal classification task is ordinal classification (ORCLASS) [5,6]. The ORCLASS method belongs to the family of Verbal Decision Analysis [7] methods. The methods have been developed for the solution of unstructured problems with qualitative parameters. The main features of such methods are: (1) a psychologically valid measurement of factors which are important for the decision; (2) psychologically valid way of eliciting information in the construction of a decision rule; (3) ability to check the decision maker’s consistency in the process of preferences elicitation.

The possibilities and limitations of human information processing system in multicriteria classification tasks were investigated in Ref. [9]. The limits of unaided human capabilities to solve classification problems with a small number of contradictions were found. The ORCLASS method creates an aid to the decision maker (DM) in the solution of multicriteria classification problems. The ORCLASS method and DSS use a verbal description of a problem in the DM language and provide checks of DM information for consistency.

The main task for the ORCLASS method is to create a decision rule to assign any set of alternatives to ordered decision classes. That is why a classification decision rule is developed with all possible combinations of estimations with many criteria taken into account.

The aim of this paper is to present the main ideas of the new method and the decision support system for ordinal classification of a relatively small set of alternatives. After a formal statement of the problem, a practical task is presented. The main ideas of the new method and its justification are given.

## 2. Statement of the problem

The task can be represented formally in the following way:

Given:

1. $K = 1 , 2 , . . . , N$ is a set of criteria;

2. $n _ { q }$ is the number of possible values on a scale of the qth criterion $( q { \in } K ) ;$ ;

3. $X _ { q } = \{ x _ { i q } \}$ is a set of values for the qth criterion (the scale of the qth criterion); $| X _ { q } | =$ $n _ { q } ( q { \in } K )$ ; the values on a scale are ordered from the best (first) to worst (last); the order of the values on one scale does not depend upon the values on the others;

4. $A { = } \{ y _ { i } \} ; ~ i { = } 1 , ~ 2 , . ~ . . ,$ t—the set off t vectors describing the given alternatives; $y _ { i } { = } ( y _ { i 1 } , y _ { i 2 } ,$ $\mathbf { \Sigma } \cdot \mathbf { \Sigma } \cdot , y _ { i N } )$ where $y _ { i q } { \in } X _ { q } ; y _ { i } { \in } Y ;$

5. L—number of decision classes ordered by the quality.

Required:

On the basis of a decision maker’s preferences (judgments), build a noncontradictory classification $A { \Rightarrow } \{ A _ { 1 } \} , 1 { = } 1 , 2 , . . . , L$ such that $A = \bigcup _ { l = 1 } ^ { N } \ A _ { l } ; \ A _ { l } \cap$ $A _ { k } = \emptyset { \mathrm { ~ i f ~ } } k { \neq } l { \mathrm { ( w h e r e ~ } } A _ { 1 }$ is a subset of vectors from $A ,$ assigned to the lth class) using a minimum number of classifications made directly by the decision maker.

Let us explain the term ‘‘noncontradictory’’ in the statement of the problem.

If we use natural numbers to denote values in the ordinal scale $X _ { q }$ for the qth criterion, we shall obtain a modified scale $B _ { q } { = } \{ 1 , 2 , . . . , n _ { q } \}$ , where $b _ { i q } < b _ { \mathrm { j } q } ,$ , if $x _ { i q }$ is more preferable for a decision than $x _ { \mathrm { j } q } .$ Thus, for each ordinal scale $X _ { q }$ we form the unique ordinal scale $B _ { q } ,$ reflecting DM preferences for values from $X _ { q } .$

This information from DM defines an antireflexive and transitive binary relation of strict preference (or dominance) $P ^ { 0 }$ on the set A:

$$
\begin{array}{l} P ^ {0} = \{(y _ {i}, y _ {j}) \in A \mid \forall_ {q} \in K, b _ {i q} \leq b _ {j q} \text { and } \\ \exists_ {q} ^ {0} \text { such   that } b _ {i q} ^ {0} <   b _ {j q} ^ {0} \}. \end{array}\tag{1}
$$

On the other hand, we know that decision classes are ordered for DM. This means that any alternative from the first class is more preferable for DM than any alternative from the second class, and so on. This property may be reflected in the following binary preference relation on the set A:

$$
P ^ {1} = \{(y _ {i}, y _ {j}) \in A \mid y _ {i} \in A _ {k}, y _ {j} \in A _ {l}, k <   l \}.\tag{2}
$$

It is natural to assume that a vector from Y, dominating the one under consideration, is to be in a more preferable class. Formally, this may be put down as follows:

$$
\text { if } (y _ {i}, y _ {j}) \in P ^ {0} \text { and } y _ {i} \in A _ {l}, \text { then } y _ {j} \notin A _ {k} \text { if } k <   l.\tag{3}
$$

Let us call a classification of the set A into classes noncontradictory if this requirement is fulfilled. The noncontradictory classification meets the following requirement:

$$
\text { if } (y _ {i}, y _ {j}) \in P ^ {0}, \text { then } (y _ {j}, y _ {i}) \notin P ^ {1}.\tag{4}
$$

Let us explain why the criterion $C _ { \mathrm { m i n } } \mathrm { \Pi } ^ { \mathrm { D M } } \mathrm { - } \mathrm { \bf a }$ minimum number of classifications made directly by DM—has been taken for the classification task.

It is possible to accomplish the task of classification by asking DM to classify directly all vectors from A. However, such a strategy is impractical even for a relatively small problem, because the number of such vectors could be large enough and it is a timeconsuming strategy for DM. Utilization of relation (1) allows one after each classification made by DM to classify in an indirect way some vectors that are in the relation of dominance to the one classified directly. Therefore, it is possible to solve the classification problem stated above with different numbers of classification tasks solved directly by DM. Each classification of a vector executed by DM requires some effort and valuable time. That is why, the criterion $C _ { \mathrm { m i n } } ^ { \mathrm { \phantom { * } } \mathrm { D M } }$ is quite natural for this problem.

The output of a classification method could be presented as sets of boundary vectors (or alternatives). By boundary vectors we mean nondominated and nondominating vectors from each decision class. It is easy to see that any vector could be classified by its relation to boundary vectors.

## 3. Practical task

Let us suppose that DM is the head of a large research organization interested in formal comparison of several research units. This could be to justify division of resources between the units. Let us imagine that DM wants to take into account the following criteria:

1. Number of publications in referenced journals.

2. Number of papers accepted for international conferences.

3. Participation in program committees of conferences.

4. Number of research grants.

5. Number of contracts.

On each criterion, DM could define the quality grades ordered from the best to worst. Such grades present the levels of quality that DM wants to take into account. The number of such grades is usually not large and DM expresses them in his language. For example, he could formulate the ordinal scale for first criterion as:

Number of publications in referenced journals

1. Large—more than 4 multiplied by the number of researchers.

2. Average—2 –4 multiplied by the number of researchers.

3. Small—less than 2 multiplied by the number of researchers.

Let us note that DM himself defines the corresponding numbers.

DM could ask the research units to present him the necessary information for the last 2 or 3 years. On the basis of this information, he wants to classify the units into two classes:

The research unit deserves an increasing amount of support.

The research unit does not deserve an increased amount of support.

We could suggest that in a general case, the achievements of research units could differ by different criteria. Therefore, the task of classification may be very difficult. Let us suppose that each criterion scale has three estimates. In this case, the size of the multicriteria space is:

$$
S = 3 ^ {5} = 2 4 3.
$$

The number of research units is less than S.

The problem consists in the development of a decision method and decision support system helping DM in classification of research units. The classification is to be done with minimum time spent by DM and without contradictions.

## 4. Main ideas of classification method

Let us suppose that a vector $y _ { i }$ is presented to DM for the classification and he placed this vector into class $C _ { l } .$ . In accordance with Eq. (2) an indirect classification of some other vectors from the given subset could be made.

The number of indirectly classified vectors depends on the vector presented to DM for classification, and on the class assigned by DM to the vector being considered. To evaluate the possible amount of information obtained through classification by the decision maker of a vector from $Y ,$ it is necessary to calculate the number of indirectly classified vectors for each possible class for the vector presented.

Let $g _ { i l }$ denote the number of vectors definitely classified (from the given subset) by assigning class $C _ { l }$ to vector $y _ { i } .$ . Thus, $g _ { i l }$ characterizes the amount of information gained as a result of such decision. This amount depends on the class prescribed to the vector $y _ { i } .$ As we do not know in advance the class to which DM will assign the considered vector, it is reasonable to attempt to introduce some index which will characterize the likelihood of class $C _ { l }$ for vector $y _ { i }$ while evaluating the possible amount of information connected with the vector $y _ { i } .$ We propose the following heuristic approach to this problem.

Let $p _ { i l }$ denote the index that reflects the likeliness of $y _ { i } ,$ being assigned to class $C _ { l } .$ In that case, the expected amount of information $\varphi _ { i }$ connected with classification of vector $y _ { i }$ may be defined as:

$$
\phi_ {i} = \sum_ {l = 1} ^ {l = L} p _ {i l} g _ {i l}.\tag{5}
$$

The idea consists in the presentation to DM at each step of dialogue of the most informative vector for the classification corresponding to max $\phi _ { i }$ . Index $\phi _ { i }$ is calculated for the subset of given alternatives that have not been classified before this step of the dialogue.

The procedure guarantees the maximum of expected information at each step the dialogue with DM.

There may be different heuristics for the calculation of $p _ { i l }$ in formula (5). It is clear that the possibility of vector $y _ { i }$ to be assigned to class $C _ { l }$ is connected with some notion of the ‘‘similarity’’ of $\dot { y } _ { i }$ and elements of class $C _ { l } .$ In Ref. [8], the idea was proposed to introduce the notion of the center $c _ { l }$ of class $C _ { l }$ and the formula for its calculation was proposed. This is an artificial point in the criteria space with averaged values on all criteria. Although this center has no special physical sense, it reflects some averaged image of the class representative, and will be used later to evaluate the required ‘‘similarity’’. The distance from the center of class defines the probability $p _ { i l } .$

The new feature of the proposed method is the idea to take into account the variation in the number of the indirectly classified alternatives from the given set of alternatives. It is possible to consider $g _ { i l }$ as random parameter $G _ { i }$ with expected value $\mathrm { M G } _ { i }$ . Let us note: $\varphi _ { i } { = } \mathrm { M G } _ { i } .$

The parameter representing the variation of $G _ { i }$ near $M G _ { i }$ is a standard deviation:

$$
\sigma_ {i} = \sqrt {\mathrm{D} G _ {i}} = \sqrt {M (G _ {i} - M G _ {i}) ^ {2}}.
$$

Where: $\mathrm { D } G _ { i }$ is the variance of $G _ { i } .$

It is necessary to take not an absolute but relative deviation. Really, with large values of $\varphi _ { i } ,$ it is possible to have a large deviation. Therefore, let us take as the characteristic of the expected amount of information the following:

$$
\psi_ {i} = \frac {\varphi_ {i}}{1 + v \frac {\sigma_ {i}}{\varphi_ {i}}}, \qquad v \geq 0.\tag{6}
$$

Where: $\sigma / \varphi _ { i }$ is the relative deviation of $g _ { i l }$ from average value and v is the relative importance of variance. It will be evaluated in the experiment presented below.

At each step of dialogue, the check of possible DM contradictions is done on the basis of requirement (4) in respect to given alternatives. In the case of a contradiction, contradictory answers are presented to DM for the analysis and elimination of a contradiction.

Table 1  
SAC and ORCLASS comparison

<table><tr><td rowspan="3">Criteria</td><td rowspan="3">Subset</td><td rowspan="3">Subset cardinality</td><td colspan="9">Classes</td></tr><tr><td colspan="3">2</td><td colspan="3">3</td><td colspan="3">4</td></tr><tr><td>Variance</td><td>SAC questions asked</td><td>ORCLASS questions asked</td><td>Variance</td><td>SAC questions asked</td><td>ORCLASS questions asked</td><td>Variance</td><td>SAC questions asked</td><td>ORCLASS questions asked</td></tr><tr><td rowspan="5">4</td><td>1</td><td>81</td><td>0.00</td><td>19.00</td><td>19.00</td><td>0.00</td><td>42.00</td><td>42.00</td><td>0.00</td><td>42.00</td><td>42.00</td></tr><tr><td>1/2</td><td>40</td><td>2.00</td><td>14.09</td><td>18.64</td><td>2.00</td><td>24.07</td><td>31.29</td><td>2.00</td><td>26.76</td><td>31.51</td></tr><tr><td>1/3</td><td>27</td><td>2.33</td><td>12.34</td><td>15.70</td><td>2.50</td><td>19.30</td><td>24.21</td><td>2.33</td><td>20.48</td><td>22.80</td></tr><tr><td>1/4</td><td>20</td><td>2.50</td><td>10.20</td><td>13.20</td><td>2.50</td><td>15.57</td><td>19.25</td><td>2.50</td><td>16.13</td><td>17.42</td></tr><tr><td>1/5</td><td>16</td><td>2.67</td><td>8.90</td><td>11.37</td><td>2.63</td><td>13.03</td><td>15.14</td><td>2.50</td><td>13.33</td><td>14.24</td></tr><tr><td rowspan="5">5</td><td>1</td><td>243</td><td>0.00</td><td>32.00</td><td>32.00</td><td>0.00</td><td>65.25</td><td>65.25</td><td>0.00</td><td>72.75</td><td>72.75</td></tr><tr><td>1/2</td><td>121</td><td>2.75</td><td>27.04</td><td>31.00</td><td>2.45</td><td>54.66</td><td>62.14</td><td>2.25</td><td>66.17</td><td>80.39</td></tr><tr><td>1/3</td><td>81</td><td>2.75</td><td>23.87</td><td>27.71</td><td>2.63</td><td>45.32</td><td>55.13</td><td>2.33</td><td>52.65</td><td>66.34</td></tr><tr><td>1/4</td><td>60</td><td>3.00</td><td>21.61</td><td>26.07</td><td>2.63</td><td>38.71</td><td>49.66</td><td>2.33</td><td>43.24</td><td>56.15</td></tr><tr><td>1/5</td><td>48</td><td>3.25</td><td>19.63</td><td>25.15</td><td>2.80</td><td>33.51</td><td>44.26</td><td>2.50</td><td>36.88</td><td>47.28</td></tr><tr><td rowspan="5">6</td><td>1</td><td>729</td><td>0.00</td><td>108.50</td><td>108.50</td><td>0.00</td><td>165.25</td><td>165.25</td><td>0.00</td><td>204.50</td><td>204.50</td></tr><tr><td>1/2</td><td>364</td><td>3.38</td><td>70.32</td><td>124.11</td><td>2.75</td><td>113.17</td><td>160.11</td><td>2.25</td><td>156.73</td><td>197.89</td></tr><tr><td>1/3</td><td>243</td><td>3.38</td><td>63.27</td><td>118.16</td><td>2.63</td><td>100.54</td><td>146.35</td><td>2.38</td><td>133.99</td><td>184.17</td></tr><tr><td>1/4</td><td>182</td><td>3.45</td><td>55.75</td><td>110.73</td><td>3.25</td><td>90.35</td><td>136.61</td><td>3.13</td><td>112.66</td><td>168.69</td></tr><tr><td>1/5</td><td>145</td><td>3.63</td><td>51.33</td><td>106.47</td><td>3.50</td><td>80.90</td><td>128.49</td><td>3.00</td><td>95.90</td><td>152.89</td></tr></table>

Let us undertake an investigation of the new method for the classification of a given set of alternatives. We call this method subset alternatives classification (SAC).

## 5. Evaluation of the new method efficiency

To compare the new method of classification of a given set of multicriteria alternatives with the method ORCLASS, it is possible to use the statistical modeling approach. We could model different kinds of boundaries between decision classes and compare the average performance of both methods (average number of questions posed to DM).

Practical experience of utilizing classification by decision making shows that DM tends to use decision rules, having fairly definite structure [10,11]. In a general case, each of the rules has the structure of a tree whose root contains combinations of the values of t most important features (criteria). A certain number of less important criteria typical of the given class are added. Usually, minor criteria are ‘‘interchangeable’’ and the rule of adding them to the tree root has the form of the binomial coefficient $C _ { p } ^ { \ k }$ . Here p is the total number of minor criteria $\scriptstyle ( N = p + t )$ and k is the number of criteria that should be added to the main ones to make a decision.

Statistical modeling was applied to all tasks with $N ( 4 \leq N \leq 6 )$ criteria and $L ( 2 \leq L \leq 4 )$ classes, each criterion scale had $n _ { q } = 3$ estimations.

Within the limits of such parameters, decision rules of the type presented above were generated randomly for each boundary of a decision class. In a random way, a subset of all possible alternatives was taken: 1/ 2, 1/3, 1/4, 1/5 and so on. For each subset, the algorithm presented above was applied with several different levels of variance—v. The average number of questions for each task characterized by a number of criteria, decision classes and subset of alternatives was received for different levels of variance. The algorithm also calculates the relation of the number of questions to the number of boundary vectors because the latter presents the absolute minimum of questions needed for a classification. This index could be called one of absolute efficiency.

Table 2 SAC effectiveness

<table><tr><td rowspan="2">Criteria</td><td colspan="3">Classes</td></tr><tr><td>2</td><td>3</td><td>4</td></tr><tr><td>4</td><td>2.4</td><td>2.3</td><td>2.2</td></tr><tr><td>5</td><td>3.0</td><td>2.7</td><td>2.4</td></tr><tr><td>6</td><td>3.5</td><td>3.1</td><td>2.6</td></tr></table>

Table 3  
Recommended value of variance

<table><tr><td rowspan="3">Criteria</td><td rowspan="3">Subset</td><td rowspan="3">Cardinality</td><td colspan="9">Classes</td></tr><tr><td colspan="3">2</td><td colspan="3">3</td><td colspan="3">4</td></tr><tr><td>Variance</td><td>Questions asked</td><td>Efficiency</td><td>Variance</td><td>Questions asked</td><td>Efficiency</td><td>Variance</td><td>Questions asked</td><td>Efficiency</td></tr><tr><td rowspan="4">4</td><td>1/2</td><td>40</td><td>2.00</td><td>14.09</td><td>46.22</td><td>2.00</td><td>24.07</td><td>63.11</td><td>2.00</td><td>26.76</td><td>71.22</td></tr><tr><td>1/3</td><td>27</td><td>2.33</td><td>12.34</td><td>50.71</td><td>2.50</td><td>19.30</td><td>71.37</td><td>2.33</td><td>20.48</td><td>79.54</td></tr><tr><td>1/4</td><td>20</td><td>2.50</td><td>10.20</td><td>58.64</td><td>2.50</td><td>15.57</td><td>78.59</td><td>2.50</td><td>16.13</td><td>83.60</td></tr><tr><td>1/5</td><td>16</td><td>2.67</td><td>8.90</td><td>63.97</td><td>2.63</td><td>13.03</td><td>83.50</td><td>2.50</td><td>13.33</td><td>86.25</td></tr><tr><td rowspan="4">5</td><td>1/2</td><td>121</td><td>2.75</td><td>27.04</td><td>32.50</td><td>2.45</td><td>54.66</td><td>39.85</td><td>2.25</td><td>66.17</td><td>48.23</td></tr><tr><td>1/3</td><td>81</td><td>2.75</td><td>23.87</td><td>35.85</td><td>2.63</td><td>45.32</td><td>47.15</td><td>2.33</td><td>52.65</td><td>60.04</td></tr><tr><td>1/4</td><td>60</td><td>3.00</td><td>21.61</td><td>38.21</td><td>2.63</td><td>38.71</td><td>52.68</td><td>2.33</td><td>43.24</td><td>68.40</td></tr><tr><td>1/5</td><td>48</td><td>3.25</td><td>19.63</td><td>41.13</td><td>2.80</td><td>33.51</td><td>58.43</td><td>2.50</td><td>36.88</td><td>73.45</td></tr><tr><td rowspan="4">6</td><td>1/2</td><td>364</td><td>3.38</td><td>70.32</td><td>27.48</td><td>2.75</td><td>113.17</td><td>34.05</td><td>2.25</td><td>156.73</td><td>36.91</td></tr><tr><td>1/3</td><td>243</td><td>3.38</td><td>63.27</td><td>30.34</td><td>2.63</td><td>100.54</td><td>37.51</td><td>2.38</td><td>133.99</td><td>45.35</td></tr><tr><td>1/4</td><td>182</td><td>3.45</td><td>55.75</td><td>34.04</td><td>3.25</td><td>90.35</td><td>40.99</td><td>3.13</td><td>112.66</td><td>52.06</td></tr><tr><td>1/5</td><td>145</td><td>3.63</td><td>51.33</td><td>36.52</td><td>3.50</td><td>80.90</td><td>44.73</td><td>3.00</td><td>95.90</td><td>58.25</td></tr></table>

So, we have two indexes of efficiency: relative (comparison with ORCLASS by statistical modeling approach) and absolute (number of questions required, divided by the number of boundary vectors).

![](/api/attachments/SX82C6VS/fulltext/images/8f93796376106b0c26b8c6524cd8a6eb440fcf5099304ae592c00156c7655fa8.jpg)  
Fig. 1. Evaluation of the alternative screen.

## 6. Results

Table 1 gives a comparison of the results of SAC and ORCLASS for different subsets of objects.

For each number of criteria, the first line presents the case of classification for a complete set of possible alternatives. For this case, the average number of questions is the same as in SAC (variance is equal to zero) and ORCLASS.

It is easy to notice that the introduction of the variance reduces considerably the average number of questions posed to DM. The difference becomes more evident with an increasing number of criteria. The optimal variance values received in the experiments are given in Table 2.

Table 2 could give a recommendation as to how to select the value of variance in the tasks of different sizes. However, this choice does not guarantee that the efficiency of the method in each particular case would be optimal.

The evaluation of absolute efficiency index of SAC gives the results presented in Table 3.

It is easy to see that absolute efficiency increases with the growth of decision classes number and decreases with the growth of the size of a problem.

Let us note that in the difference for ORCLASS, the method SAC allows one to find only a boundary for a given set of alternatives. The boundaries built by ORCLASS allocate all vectors $y _ { i }$ into decision classes.

## 7. Decision support system implementing the method SAC

Decision support systems are powerful tools helping DM in the solution of different practical problems [2]. The method presented above was implemented in the form of DSS for Windows environment.

The input information is:

criteria with ordinal scales with verbal evaluations of quality grades;

decision classes;

![](/api/attachments/SX82C6VS/fulltext/images/d315e9523338fc88fbee96b5c63d81db99b9689d14a348bd662ee13a926ee048.jpg)  
Fig. 2. Resolving contradiction screen.

<table><tr><td>Parameter</td><td>Status</td></tr><tr><td>Classification</td><td>Subset</td></tr><tr><td>Job</td><td>Not finished</td></tr><tr><td>Contradictions</td><td>No</td></tr><tr><td>From subset classified</td><td>5 of 22</td></tr><tr><td>Overall classified</td><td>25 of 243</td></tr><tr><td>Questions to DM</td><td>1</td></tr><tr><td>Probabilities</td><td>2(0.48) 4(0.52)</td></tr><tr><td>Dispersion level</td><td>1.000000</td></tr><tr><td></td><td></td></tr></table>

Fig. 3. Information screen.

set of real alternatives;

level of dispersion.

After entering the input information into the computer, the program of classification starts. The example of the computer screen typical for the classification stage is given below (Fig. 1).

DM classifies alternatives one after another until a complete classification of given alternatives is done. In case of contradiction, the system presents a pair of contradictory alternatives and asks DM to change one or both answers (Fig. 2).

The information about the current status of the system is presented in a special window (Fig. 3).

In the line ‘‘Probabilities’’, the system informs DM about the numbers of the indirectly classified alternatives in case DM chooses the first or the second class and about the probabilities of such choice (the distance from the center of the corresponding class).

After all alternatives are classified, DSS begins the process of boundary validation. This means that boundary alternatives are presented to DM to validate their class for a second time. In the case of partial classification, all the boundary alternatives are presented.

When classification is done, the system presents a list of given alternatives with indication of the assigned decision classes.

## 8. Example

Let us return to the example presented above. Let us suppose that the list from 23 research units is given for the classification into two decision classes (Table 4). Each unit has estimations by five criteria, and the corresponding number in Table 4 presents each verbal estimate.

The 23 given alternatives are a subset from a general set of 243 possible alternatives. The level of dispersion was assumed equal to three.

During the classification, the following decision rule (imitating DM preferences) was taken: ‘‘for research units of the first class, the number of best (first) estimates is no less than two and the number of worst estimates, no more than one’’.

The classification was accomplished with 15 questions to DM.

The boundary elements of classes are:

Lower boundary of first class:

11231 13212 21122 21221 22111

Upper boundary of second class:

11332 12322 13132 22231 23221 23322 31331 32311 33131

Results of the classification

<table><tr><td>Name</td><td>Evaluation</td><td>Class</td></tr><tr><td>Unit1</td><td>11231</td><td>1</td></tr><tr><td>Unit2</td><td>11332</td><td>2</td></tr><tr><td>Unit3</td><td>12322</td><td>2</td></tr><tr><td>Unit4</td><td>13112</td><td>1</td></tr><tr><td>Unit5</td><td>13132</td><td>2</td></tr><tr><td>Unit6</td><td>13212</td><td>1</td></tr><tr><td>Unit7</td><td>13232</td><td>2</td></tr><tr><td>Unit8</td><td>13332</td><td>2</td></tr><tr><td>Unit9</td><td>21122</td><td>1</td></tr><tr><td>Unit10</td><td>21221</td><td>1</td></tr><tr><td>Unit11</td><td>22111</td><td>1</td></tr><tr><td>Unit12</td><td>22231</td><td>2</td></tr><tr><td>Unit13</td><td>23221</td><td>2</td></tr><tr><td>Unit14</td><td>23322</td><td>2</td></tr><tr><td>Unit15</td><td>31331</td><td>2</td></tr><tr><td>Unit16</td><td>32311</td><td>2</td></tr><tr><td>Unit17</td><td>32312</td><td>2</td></tr><tr><td>Unit18</td><td>33131</td><td>2</td></tr><tr><td>Unit19</td><td>33231</td><td>2</td></tr><tr><td>Unit20</td><td>33312</td><td>2</td></tr><tr><td>Unit21</td><td>33322</td><td>2</td></tr><tr><td>Unit22</td><td>33332</td><td>2</td></tr><tr><td>Unit23</td><td>33332</td><td>2</td></tr></table>

The boundaries presented above divide only the given alternatives and in general case could not be used for a classification of the other ones.

Let us note that contrary to the case of complete classification, the set of boundary alternatives does not represent any compact decision rule, since these boundaries are built of real alternatives.

## 9. Discussion

The results demonstrate that the subset alternatives classification (SAC) method surpasses the ORCLASS method and the absolute efficiency of SAC is quite satisfactory. For example, the problem with N = 5, L = 3, the subset is 1/5 of the full set, the SAC method gives on the average 38.71 questions to DM in comparison with 65.25 questions for ORCLASS. In this case, the average absolute efficiency of SAC is equal to 52.68%.

The SAC method is a convenient tool in the hands of DM for the solution of new problems. In case of repeated problems, it could be a supplementary method to the methods of data envelopment analysis [4].

## Acknowledgements

The authors express the gratitude to an unknown reviewer for valuable comments and detailed reading of the paper. The research is partly supported by the Russian Foundation for Basic Research grant 01-01- 00514.

## References

[1] C.A. Bana e Costa, Absolute and relative evaluation problematics. The concept of neural level and the MCDA robot technique, in: M. Cerny, D. Gluckaufova, D. Loula (Eds.), Proceedings of the International Workshop on Multicriteria Decision Making. Methods – Algorithms – Applications Liblice, 18–22 March, Prague, 1991.

[2] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundation of Decision Support Systems, Academic Press, New York, 1981.

[3] J. de Montgolfier, P. Bertier, Approche Multicritere des Problems de Decision, Edicions Hommes et Techniques (Paris, 1978).

[4] M. Halme, T. Joro, P. Korhonen, S. Salo, J. Wallenius, A value efficiency approach to incorporating preference information in data envelopment analysis, Management Science 45 (1) (January, 1999) 103–115.

[5] O.I. Larichev, A study on the internal organization of expert knowledge, Pattern Recognition and Image Analysis 5 (1) (1995) 57– 63.

[6] O.I. Larichev, H.M. Moshkovich, Direct Classification Problems in Decision Making, Proceedings of the USSR Academy of Sciences, vol. 287, Nauka, Russia, Moscow, 1986, pp. 570– 576.

[7] O.I. Larichev, H.M. Moshkovich, Direct classification method and the problem of eliciting reliable expert information, Technical Cybernetics 1 (1987) 151 – 161, Russia, Moscow.

[8] O.I. Larichev, H.M. Moshkovich, An approach to ordinal classification problems, International Transactions of Operational Research 1 (3) (1994) 375 – 385.

[9] O.I. Larichev, H.M. Moshkovich, S.B. Rebrick, Systematic research into human behavior in multi attribute object classification problems, Acta Psychologica 68 (1988) 171 – 182.

[10] A.I. Mechitov, Utilization of hierarchical criteria systems by decision making, in: S.V. Emelianov, O.I. Larichev (Eds.), Descriptive studies of Multi-Criteria Decision Making Procedures, Collected Papers, Issue 9, The Institute for System Studies, Moscow, 1980, pp. 67–75, in Russian.

[11] E.M. Moshovich, O.P. Kundinov, Utilization of ordinal classification for R&D evaluation in research institute, in: S.V. Larichev, O.I. Larichev (Eds.), Decision Support Systems, Collected Papers, Issue 12, The Institute for System Studies, Moscow, 1986, pp. 56– 61, in Russian.

[12] W. Yu, ELECTRE TRI, aspect methodologiques et Manuel d’utilisation, Document du LAMSADE, 74, Universite de Paris-Dauphine, Paris, 1992.

Oleg I. Larichev received his PhD degree in applied mathematics and Doctor of Sciences degree in Decision Making from the Institute of Control and Management, Russian Academy of Sciences in 1965 and 1975, respectively. He joined the Institute for Systems Analysis in 1976. He is the head of the Decision Making Department. He published nine books (two in English) and 200 papers. He is a professor of the Moscow Institute for Physics and Technology (Technical University). His research interests include multicriteria decision making, cognitive psychology and artificial intelligence.

Anatoly V. Kortnev received his PhD degree in applied mathematics from the Institute of Control and Management, Russian Academy of Sciences in 1967. He published 32 papers. He is the scientific secretary of the Informatics and Computer Sciences Department of the Russian Academy of Sciences. His research interests include decision making in organizations and organizational behavior.

Dmitry Yu. Kochin is a student of the Moscow Institute for Physics and Technology (Technical University). His research interests include multicriteria decision making and decision support systems.
