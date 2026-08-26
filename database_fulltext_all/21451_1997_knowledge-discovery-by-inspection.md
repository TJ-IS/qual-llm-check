---
otero_id: 21451
otero_key: "7FAVCERR"
title: "Knowledge discovery by inspection"
authors: "David McSherry"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00012-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge discovery by inspection

David McSherry \*

School of Information and Software Engineering, University of Ulster, Coleraine BT52 ISA, Northern Ireland, UK

## Abstract

Given the enormous size of many business databases, algorithms for knowledge discovery can often be applied to only a sample of the original data. Other methods used to improve efficiency include focusing on a restricted class of rules such as exact rules, or limiting the number of conditions in the discovered rules. It is shown that simple exact rules can often be discovered by visual inspection of frequency tables. An efficient algorithm for rule discovery by inspection is presented. The discovered rules include all exact rules with one or two conditions. © 1997 Elsevier Science B.V.

Keywords: Asymptotic complexity; Classification; Database; Data mining; Knowledge discovery; Rules

## 1. Introduction

Often the objective of data mining is the discovery of rules for a classification task such as assessing the creditworthiness of potential customers $[1]$ or predicting consumer loyalty to a product $[2]$ . A typical classification rule has one or more conditions on the left-hand side (LHS), and a single outcome class on the right-hand side (RHS). An exact rule is one that is true for all instances in the data set, while a probabilistic rule states the probability of an outcome class given its conditions.

Given the enormous size of many business databases, algorithms for knowledge discovery can often be applied to only a sample of the original data [3]. Other methods used to improve efficiency include focusing on a restricted class of rules such as exact rules [4], or limiting the number of conditions in the discovered rules [5]. Measures of rule interest include $p(E)$ ( $p(H|E) - p(H)$ ), where E and H are the LHS and RHS of a discovered rule [4], and the information theoretic $J$ -measure used in ITRULE [5]. Another simple measure of a rule's potential usefulness is the number (or proportion) of instances in the data set that support it [6].

As shown in the following section, simple exact rules can often be discovered by visual inspection of the frequencies of each attribute's values in each outcome class. An efficient algorithm for rule discovery by inspection is presented in Section 3.

## 2. The discovery process

Table 1 shows an artificial data set describing consumer products. Attributes in the data set are consumer ratings of the products for design (D), reliability (R) and economy (E). The outcome of interest is consumer loyalty to the product. Table 2 shows the frequency of each attribute value in the outcome classes HIGH, MEDIUM and LOW. Only a single access to each instance in the data set is required to construct the frequency tables. Alternatively, if the data set is stored as a relational database table, appropriate SQL queries can be formulated to retrieve the required frequencies.

Table 1  
Consumer loyalty data

<table><tr><td>Instance no.</td><td>Design</td><td>Reliability</td><td>Economy</td><td>Loyalty</td></tr><tr><td>1.</td><td>good</td><td>good</td><td>good</td><td>high</td></tr><tr><td>2.</td><td>average</td><td>good</td><td>good</td><td>medium</td></tr><tr><td>3.</td><td>average</td><td>average</td><td>good</td><td>high</td></tr><tr><td>4.</td><td>average</td><td>good</td><td>poor</td><td>high</td></tr><tr><td>5.</td><td>poor</td><td>good</td><td>good</td><td>high</td></tr><tr><td>6.</td><td>good</td><td>poor</td><td>poor</td><td>high</td></tr><tr><td>7.</td><td>poor</td><td>average</td><td>good</td><td>medium</td></tr><tr><td>8.</td><td>good</td><td>average</td><td>poor</td><td>low</td></tr><tr><td>9.</td><td>poor</td><td>average</td><td>poor</td><td>low</td></tr><tr><td>10.</td><td>poor</td><td>good</td><td>average</td><td>low</td></tr><tr><td>11.</td><td>average</td><td>poor</td><td>good</td><td>medium</td></tr><tr><td>12.</td><td>poor</td><td>poor</td><td>good</td><td>low</td></tr><tr><td>13.</td><td>average</td><td>average</td><td>average</td><td>medium</td></tr><tr><td>14.</td><td>average</td><td>average</td><td>poor</td><td>medium</td></tr><tr><td>15.</td><td>good</td><td>poor</td><td>good</td><td>low</td></tr><tr><td>16.</td><td>poor</td><td>poor</td><td>poor</td><td>low</td></tr><tr><td>17.</td><td>poor</td><td>good</td><td>poor</td><td>medium</td></tr><tr><td>18.</td><td>good</td><td>average</td><td>good</td><td>high</td></tr><tr><td>19.</td><td>average</td><td>good</td><td>average</td><td>medium</td></tr></table>

Rule discovery by inspection relies on the presence of zeros in the frequency tables. For example, an attribute value that occurs only in one outcome class enables the immediate discovery of a rule with just one condition. Although there is no such attribute value in Table 2, D = average never occurs in LOW, so the outcome for any instance with this value must be HIGH or MEDIUM. Similarly, if E = average, the outcome must be MEDIUM or LOW. The following rule is therefore discovered: Rule 1. if D = average and E = average then MEDIUM. A goal-driven approach simplifies the discovery process. To discover rules with LOW as the target outcome class, we look for attribute values that eliminate HIGH and MEDIUM. Since D = good eliminates MEDIUM, and E = average eliminates HIGH, another rule is discovered: Rule 2. if D = good and E = average then LOW. Although Rule 2 appears to contradict Rule 1, it is nevertheless valid for the data set. Unlike Rule 1, however, it is not supported in the data set and can therefore be discarded.

Table 2  
Frequency tables for the consumer loyalty data

<table><tr><td>Loyalty: Design</td><td>H</td><td>M</td><td>L</td><td>Reliability</td><td>H</td><td>M</td><td>L</td><td>Economy</td><td>H</td><td>M</td><td>L</td></tr><tr><td>good</td><td>3</td><td>0</td><td>2</td><td>good</td><td>3</td><td>3</td><td>1</td><td>good</td><td>4</td><td>3</td><td>2</td></tr><tr><td>average</td><td>2</td><td>5</td><td>0</td><td>average</td><td>2</td><td>3</td><td>2</td><td>average</td><td>0</td><td>2</td><td>1</td></tr><tr><td>poor</td><td>1</td><td>2</td><td>4</td><td>poor</td><td>1</td><td>1</td><td>3</td><td>poor</td><td>2</td><td>2</td><td>3</td></tr></table>

Rules discovered by inspection of frequency tables based on the data set as a whole will be called surface rules. Many more rules can often be discovered by applying the same process to subsets of the original data set consisting of all instances with a given attribute value. A rule discovered in the subset can be transformed into a nonsurface rule that is true for the original data set by including the attribute value as an additional condition in the rule.

Frequency tables for the subset of the consumer loyalty data with E = good are shown in Table 3. In this case, the additional condition to be inserted in a discovered rule is E = good. Inspection of Table 3 with HIGH as the target outcome class reveals that D = good eliminates MEDIUM. Since two values of R eliminate LOW, two nonsurface rules are discovered: Rule 3. if D = good and R = good and E = good then HIGH; Rule 4. if D = good and R = average and E = good then HIGH. With MEDIUM and LOW as the target outcome classes, two more rules are discovered: Rule 5. if D = average and R = poor and E = good then MEDIUM; Rule 6. if D = good and R = poor and E = good then LOW. In all, 12 rules can be discovered by inspection from the consumer loyalty data, including the only two rules supported by more than one instance. The six rules that are not discovered all have three conditions and are supported by a single instance.

Table 3  
Frequency tables for the subset of the consumer loyalty data with E = good

<table><tr><td>Loyalty: Design</td><td>H</td><td>M</td><td>L</td><td>Reliability</td><td>H</td><td>M</td><td>L</td></tr><tr><td>good</td><td>2</td><td>0</td><td>1</td><td>good</td><td>2</td><td>1</td><td>0</td></tr><tr><td>average</td><td>1</td><td>2</td><td>0</td><td>average</td><td>2</td><td>1</td><td>0</td></tr><tr><td>poor</td><td>1</td><td>1</td><td>1</td><td>poor</td><td>0</td><td>1</td><td>2</td></tr></table>

## 3. Automating the discovery process

In this section, an algorithm for rule discovery by inspection is presented in which only supported rules are discovered, thus eliminating the need for repeated access to the data set to check for support. The theoretical framework is adapted and extended from the notation of rough set theory $[7,6]$ .

## 3.1. Definition 1

An extended attribute-value system is a tuple $(X, A, V, H, f, g)$ , where X is a nonempty finite set of objects (or instances), A is a finite set of discrete attributes, $V = \cup_{a \in A} \text{dom}(a)$ is the union of domains of the attributes in A, H is a finite set of outcome classes, $f: X \times A \to V$ assigns attribute values to instances in X so that $f(x, a) \in \text{dom}(a)$ for all $x \in X$ and $a \in A$ , and $g: X \to H$ assigns a unique outcome class to each $x \in X$ .

A preliminary step in the discovery process is the construction of an instance table for each attribute containing, as illustrated in Table 4, the sets of instances in which its values occur in each outcome class. Given an attribute-value system $(X, A, V, H, f, g)$ , the instance tables are constructed by applying the following function to each $a \in A$ , $v \in \text{dom}(a)$ , and $h \in H$ :

$$
\operatorname{supp} (a, v, h) = \left\{x \in X: f (x, a) = v, g (x) = h \right\}.
$$

Table 4  
Instance tables for the consumer loyalty data

<table><tr><td>Loyalty:</td><td>H</td><td>M</td><td>L</td></tr><tr><td colspan="4">Design</td></tr><tr><td>good</td><td>{1, 6, 18}</td><td>{}</td><td>{8, 15}</td></tr><tr><td>average</td><td>{3, 4}</td><td>{2, 11, 13, 14, 19}</td><td>{}</td></tr><tr><td>poor</td><td>{5}</td><td>{7, 17}</td><td>{9, 10, 12, 16}</td></tr><tr><td colspan="4">Reliability</td></tr><tr><td>good</td><td>{1, 4, 5}</td><td>{2, 17, 19}</td><td>{10}</td></tr><tr><td>average</td><td>{3, 18}</td><td>{7, 13, 14}</td><td>{8, 9}</td></tr><tr><td>poor</td><td>{6}</td><td>{11}</td><td>{12, 15, 16}</td></tr><tr><td colspan="4">Economy</td></tr><tr><td>good</td><td>{1, 3, 5, 18}</td><td>{2, 7, 11}</td><td>{12, 15}</td></tr><tr><td>average</td><td>{}</td><td>{13, 19}</td><td>{10}</td></tr><tr><td>poor</td><td>{4, 6}</td><td>{14, 17}</td><td>{8, 9, 16}</td></tr></table>

The set of instances in X that support a given rule R: [if $a_{1}=v_{1}$ and $a_{2}=v_{2}\cdots$ and $a_{n}=v_{n}$ then h] is $\cap_{i=1}^{n}\operatorname{supp}(a_{i}, v_{i}, h)$ . The following function, defined for all $a\in A$ and $v\in\operatorname{dom}(a)$ , is used to identify the outcome classes which are consistent with a given rule condition:

$$
\operatorname{cons} (a, v) = \left\{h \in H: \operatorname{supp} (a, v, h) \neq \phi \right\}.
$$

It can be shown that if $\cap_{i=1}^{n} \operatorname{supp}(a_i, v_i, h) \neq \phi$ , then $h \in \cap_{i=1}^{n} \operatorname{cons}(a_i, v_i)$ . It follows that if $\cap_{i=1}^{n} \operatorname{cons}(a_i, v_i) = \{h\}$ then $R$ : [if $a_1 = v_1$ and $a_2 = v_2$ and $a_n = v_n$ then $h$ ] holds for all $x \in X$ . The following theorem, stated without proof due to limitations of space, provides a basis for the discovery of nonsurface rules from certain subsystems of an attribute-value system.

## 3.2. Theorem 1

Let $(X, A, V, H, f, g)$ be a given attribute-value system and for any $a_{0} \in A$ and $v_{0} \in \text{dom}(a_{0})$ , let $X_{0} = \{x \in X: f(x, a_{0}) = v_{0}\}$ . If $R:$ [if $a_{1} = v_{1}$ and $a_{2} = v_{2} \cdots$ and $a_{n} = v_{n}$ then $h$ ] holds for all $x \in X_{0}$ , then $R':$ [if $a_{0} = v_{0}$ and $a_{1} = v_{1} \cdots$ and $a_{n} = v_{n}$ then $h$ ] holds for all $x \in X$ . Moreover, the instances in $X$ that support $R'$ are the same as those that support $R$ in $X_{0}$ .

## 3.3. Definition 2

Given an attribute-value system $(X, A, V, H, f, g)$ , let $X_{0}$ be a nonempty subset of X, and let $f_{0}$ and $g_{0}$ be the restrictions of f and g to $X_{0}$ . The attribute-value system $(X_{0}, A, V, H, f_{0}, g_{0})$ so defined will be called a subsystem of $(X, A, V, H, f, g)$ .

An algorithm called INSPECT for rule discovery from a given attribute-value system $(X, A, V, H, f, g)$ can now be defined in terms of a supporting algorithm, called INSPECT-s, for the discovery of surface rules. Only supported rules are discovered by INSPECT-s, and the number of instances that support each rule is returned with the rule. INSPECT first applies INSPECT-s to $(X, A, V, H, f, g)$ . For each $a_{0} \in A$ and $v_{0} \in \text{dom}(A)$ , it then applies INSPECT-s to the subsystem defined by $X_{0} = \{x \in X : f(x, a_{0}) = v_{0}\}$ . It inserts $a_{0} = v_{0}$ as an additional condition in each rule discovered in $X_{0}$ to produce a rule which by Theorem 1 holds for all $x \in X$ and is supported by the same instances as the original rule.

## 3.4. Algorithm INSPECT-s

3.4.1. Given an attribute-value system (X, A, V, H, f, g), to discover surface rules with a target outcome class $h \in H$ on the RHS

(1) Let $h_1 \in H - \{h\}$ and select $a_1 \in A$ and $v_1 \in \operatorname{dom}(a_1)$ such that $\operatorname{supp}(a_1, v_1, h_1) = \phi$ but $\operatorname{supp}(a_1, v_1, h) \neq \phi$ . If such an attribute value exists, the first condition $a_1 = v_1$ of a potential rule has been discovered. If not, then no rule with the target outcome class on the RHS can be discovered by INSPECT-s.

(2) Now suppose that conditions $a_{1}=v_{1}$ , $a_{2}=v_{2}$ , $\cdots a_{k}=v_{k}$ of a potential rule have been selected such that $\cap_{i=1}^{k}\operatorname{supp}(a_{i},v_{i},h)\neq\phi$ . If $\cap_{i=1}^{k}\operatorname{cons}(a_{i},v_{i})=\{h\}$ then a rule R: [if $a_{1}=v_{1}$ and $a_{2}=v_{2}\cdots$ and $a_{k}=v_{k}$ then h] has been discovered and the number of instances that support R is $\operatorname{card}(\cap_{i=1}^{k}\operatorname{supp}(a_{i},v_{i},h))$ . Otherwise, choose $h_{k+1}\in\cap_{i=1}^{k}\operatorname{cons}(a_{i},v_{i})-\{h\}$ , $a_{k+1}\in A-\{a_{1},a_{2},\cdots a_{k}\}$ and $v_{k+1}\in\operatorname{dom}(a_{k+1})$ such that $\operatorname{supp}(a_{k+1},v_{k+1},h_{k+1})=\phi$ but $\cap_{i=1}^{k+1}\operatorname{supp}(a_{i},v_{i},h)\neq\phi$ . If such an attribute value exists, insert $a_{k+1}=v_{k+1}$ as an additional condition in the rule and repeat (2). Otherwise, backtrack to the nearest i<k, if any, for which an alternative choice of $a_{i}$ or $v_{i}$ is available.

(3) Repeat (1) and (2) with all possible choices of $a_i \in A$ and $v_i \in \mathrm{dom}(a_i)$ .

By the following theorem, the set of rules discovered by INSPECT when there are only two outcome classes is the set of all rules with one or two conditions.

## 3.5. Theorem 2

The rules discovered by INSPECT from a given attribute-value system $(X, A, V, H, f, g)$ include all rules with one or two conditions. The maximum number of conditions in a discovered rule is the number of outcome classes.

The rules discovered by INSPECT are the same as those discovered by the visual inspection method described in Section 2. In addition to the consumer loyalty data, the algorithm has been applied to some well-known data sets. The contact lens data [10] is based on a simplified version of the optician's real-world problem of selecting a suitable type of contact lenses, if any, for an adult spectacle wearer. In this experiment, INSPECT failed to discover only three of the nine possible rules. The discovered rules were supported by 3.7 instances on average, compared with an average of 3.3 instances for the complete set of rules.

Attributes in the congressional voting records data set [8], collected by Jeff Schlimmer from a 1984 session of the United States Congress, are the votes of congressmen on 16 budget issues. The outcome to be predicted is the party affiliation of the voter. As there are only two outcome classes, the rules discovered by INSPECT must, by Theorem 2, consist of all rules with one or two conditions. With Democrat as the target outcome class, 211 rules, all with two conditions, were discovered by INSPECT, with support ranging from one to 151 instances. Interestingly, the six most strongly supported of the discovered rules involve the physician fee freeze vote, the most informative attribute according to Quinlan [9].

In [6], the outcome to be predicted from nine attributes of cars such as number of cylinders, type of fuel system and compression ratio is mileage. In this experiment, INSPECT discovered more than 60% of all the possible rules. The discovered rules were supported by 2.32 instances on average compared with 2.33 instances for the set of all possible rules.

The number of possible rules examined by INSPECT is always less than $2r(mk)^{r}$ , where r is the number of distinct outcomes, m is the number of attributes, and k is the number of values of each attribute. Although only a single access to each instance is required, the computation of set intersections means that n, the size of the data set, is a factor of the order of $n^{2}$ in the algorithm's complexity. With the elimination of rules that are specialisations of other discovered rules, its worst-case complexity is exponential in two times the number of outcome classes. In contrast, the complexity of ITRULE is exponential in the number of attributes [5]. INSPECT is therefore more efficient provided, as often the case in large databases, the number of outcome classes is small relative to the number of attributes.

## 4. Summary and conclusions

It has been shown that simple rules can often be discovered by visual inspection of frequency tables. An efficient algorithm for rule discovery based on the same method of looking for zeros in frequency tables, or empty sets in instance tables, has been presented. Although all rules with one or two conditions are discovered, the maximum number of conditions in a discovered rule is the number of outcome classes. Rules with fewer conditions are easier to understand $[12]$ , though may not be preferred when used for classification if they involve tests with unusually high cost $[10]$ . The trade-off between accuracy and simplicity may also be important, although surprisingly high levels of accuracy have been achieved by very simple rules $[11]$ .

Focusing on the discovery of simple exact rules may be a reasonable strategy provided they are not already known to domain experts or considered too obvious. The surface rules discovered by INSPECT are distinctive in that each condition of a surface rule must eliminate, by itself, one or more of the alternative outcome classes. Such conditions may be considered interesting discoveries in their own right, for example, if the eliminated outcomes represent alternative consumer choices.

Although the rules discovered by INSPECT appear to be well supported on average, a strongly supported rule may not be discovered if it has more than two conditions. In one experiment, the most strongly supported rule was missed even though it had only three conditions. However, INSPECT can be modified to guarantee the discovery of all rules with up to a specified number of conditions. For example, the application of INSPECT-s to all subsystems of a given attribute-value system defined by fixing the values of two attributes (and insertion of the attribute values as additional conditions in the discovered rules) can be shown to guarantee the discovery of all rules with three conditions.

## Acknowledgements

The author is grateful to the anonymous referees for their comments and suggestions.

## References

[1] J. Cendrowska, PRISM: An Algorithm for Inducing Modular Rules, International Journal of Man-Machine Studies 27 (4) (1987) 349–370.

[2] W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, Knowledge Discovery in Databases: an Overview, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, Chap. 1, AAAI Press, Menlo Park, CA, 1991.

[3] R.C. Holte, Very Simple Classification Rules Perform Well on Most Commonly Used Datasets, Machine Learning 11 (1) (1993) 63–90.

[4] P.M. Murphy, D.W. Aha, UCI Repository of Machine Learning Databases, http://www.ics.uci.edu/\~mlearn/MLRepository.html (1995).

[5] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[6] J.R. Quinlan, Simplifying decision trees, International Journal of Man-Machine Studies 27 (3) (1987) 221–234.

[7] Z. Pawlak, Rough classification, International Journal of Man-Machine Studies 20 (5) (1984) 469–483.

[8] G. Piatetsky-Shapiro, Discovery, Analysis, and Presentation of Strong Rules, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, Chap. 13, AAAI Press, Menlo Park, CA, 1991.

[9] R.J. Shortland, R.T. Scarfe, Data Mining Applications in BT, BT Technology Journal 12 (4) (1994) 17–22.

[10] E. Simoudis et al., Developing Customer Vulnerability Models using Data Mining Techniques, Proceedings of the International Symposium on Intelligent Data Analysis, Baden-Baden, Germany, 1995, pp. 181–185.

[11] P. Smyth, R.M. Goodman, Rule Induction Using Information Theory, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, Chap. 9, AAAI Press, Menlo Park, CA, 1991.

[12] W. Ziarko, Discovery, Analysis, and Representation of Data Dependencies in Databases, in: G. Piatetsky-Shapiro, W.J. Frawley (Eds.), Knowledge Discovery in Databases, Chap. 11, AAAI Press, Menlo Park, CA, 1991.

![](/api/attachments/7FAVCERR/fulltext/images/3a73d85c3490927e9681867bed08baad0f2c5efcffc02c5543eebae2aed2979d.jpg)  
David McSherry graduated with first class honours in Mathematics at Queen's University Belfast in 1973 and was awarded the degrees of MSc and PhD in 1974 and 1976. Having previously held academic posts at Queen's University and Lancaster University, he is a lecturer in Computer Science in the School of Information and Software Engineering at the University of Ulster. His research interests include machine learning, knowledge discovery, case-based

reasoning and expert systems. He has published numerous research articles in International Journals and Conference Proceedings.
