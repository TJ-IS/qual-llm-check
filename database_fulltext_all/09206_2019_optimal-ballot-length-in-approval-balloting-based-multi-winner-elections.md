---
otero_id: 9206
otero_key: "5Q3JH6NU"
title: "Optimal ballot-length in approval balloting-based multi-winner elections"
authors: "Yu Xiao; Hongzhong Deng; Xin Lu; Jun Wu"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.12.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal ballot-length in approval balloting-based multi-winner elections

Yu Xiao<sup>a</sup>, Hongzhong Deng<sup>a</sup>, Xin Lu<sup>b,a</sup>, Jun Wu<sup>a,\*</sup>

![](/api/attachments/5Q3JH6NU/fulltext/images/a05fca2a3a6cd5e17626557c33e8e2f383d710ce5be066ee0558b3b4193cd542.jpg)

<sup>a</sup> College of Systems Engineering, National University of Defense Technology, Changsha 410073, Hunan, PR China

<sup>b</sup> School of Business, Central South University, Changsha 410083, Hunan, PR China

## A R T I C L E I N F O

Keywords: Group decision making Voting Approval balloting Ballot-length

## A B S T R A C T

As a common task for choosing a group of representatives, the problem of approval voting has been studied in contexts varying from democratic elections, to sports, to products marketing, and to multi-criteria decision making. In these applications, the length of individual ballots is often enforced, but how many candidates should be approved in an individual ballot is still a puzzling question. The experimental framework we present here endeavors to understand the impact of ballot-length in the efectiveness of election outcomes. Our results suggest that: (1) given the number of voters and candidates, the efectiveness of election outcome is U-shaped in the variance of individual ballot-length; (2) the determination of the optimal ballot-length critically depends on the accuracy of ballots; (3) more voters bring more efective election outcomes. Our study of how ballot length afects the efectiveness of election outcome provides new insights into an understudied area, and it can serve as a starting point for future studies of the approval balloting-based elections in other retail contexts.

## 1. Introduction

The task of selecting several candidates from a set of three or more candidates is encountered in many situations [1]. For example, people choose representatives to govern on their behalf in democracies, companies select groups of products to promote to their customers [2], search engines decide which webpages to display for users in response to a given query [3]. The need of formal rules becomes one of the central issues of these tasks to perform the selection [1,4]. In this study, we focus on the study of multi-winner approval elections, which are even more ubiquitous than single-winner ones but less studied $[ 5 , 6 ]$ . There are two typical multi-winner rules, best-k rules and committee scoring rules [5], and we use the committee scoring rule which generalizes single-winner scoring rule (t-approval score) to perform the experiments in this paper. The t-approval score of a candidate is the number of voters who consider him as the top t candidates [7]. In such elections, voters submit approval ballots over the candidates and based on these ballots several candidates with relatively high t-approval scores are elected, which we call winning committees. It should be noted that approval ballots may not be ordinal ballots of several candidates which they ‘approve’ of, and the ballot length restrictions are enforced, where the number of candidates that voters can approve is limited [8].

Multi-winner election with approval balloting has been used in many contexts over the past several decades [9-11], such as public elections [12], oficials elections [13] and academic societies [8]. One of the most common features observed in practice is that the length of individual approval ballots is enforced [13], whereas the determination of the optimal length still remains an unsolved problem both in literature and practice. Small length leads the lack of decision information or error, on the other hand, long length always brings too much ties in the final election outcome. Especially in extreme cases the individual ballots contain only one candidate or all of them, which is intuitive in most practical applications. It is natural to consider that there is a ground truth ranking of the candidates, and how to determine the optimal ballot-length, that is, to approximate this ground truth ranking and recover the social optimum ones is an important issue which should be investigated in the process of election rule-designing.

So far, studies on approval balloting-based multi-winner elections have mainly focused on the various ways approval ballots can be counted to elect a winning committee [12]. However, despite the empirical studies, only a few studies have focused on the research of bestresponse for submitting ballots, the so-called optimal ballot-length. Lee [8] provides justification for some ballot-length restrictions under complete information and highlights a stark trade-of between stable and desirable election outcomes in his study. Laslier et al. [12] conclude that voters should entail voting by pairwise comparison of two critical candidates: the strongest expected loser and the weakest expected winner to fulfill the best responses of approval balloting, but they do not provide any instructions for voters about the optimal number of candidates they should vote for. However, to the best of our knowledge, there exists so far no systematic and testable theory of the optimal ballot-length in the rule-designing of approval balloting-based multiwinner elections. In such scenarios, we here focus on the study of the optimal ballot-length in diferent situations of elections with approval balloting.

![](/api/attachments/5Q3JH6NU/fulltext/images/bb384e251dac3f97d9460de3b48e0cea7304ab4c21359f09a4e13d787ab5cee2.jpg)  
Fig. 1. The displayed inherent ability of candidate $c _ { j }$ for voter $\nu _ { i } .$

In this study, we develop a framework based on the “inherent ability” of candidates [14] to investigate the optimal ballot-length in the approval balloting-based elections problems. Our method can generate the ground truth ranking of the candidates and synthetic approval ballots with adjustable accuracy and length. Using the synthetic approval ballots and the new voting efectiveness criterion, the optimal approval ballot-length can be determined with high probability. Our results provide a characterization of the optimal length in approval balloting-based elections - leading to a justification of relationship between ballot-length restrictions and the target winning committee size. In particular, this provides some justification for the restrictions enforced by plurality voting and aid them in determining the ballot length in election rule-designing.

The remainder of this paper is organized as follows. We first introduce the experiment framework in Section 2. We then present the experimental results in Section 3. We conclude with a summary of our contributions and a discussion of future work in Section 4.

## 2. Experiment framework of multi-winner elections with approval balloting

## 2.1. Experimental approval ballot generation method

Derived from the a newly proposed experimental ranking data generation method in previous work [14], Firstly, we develop an experimental approval ballot generation method. Let $V = ( \nu _ { 1 } , \nu _ { 2 } , . . . \nu _ { N } )$ be a list of N voters and $C = ( c _ { 1 } , c _ { 2 } , . . . c _ { M } )$ be a set of M candidates with representative elements $\nu _ { i }$ and $c _ { j } ,$ respectively. We assume that there ex ists a ground truth ranking of the candidates, which can be the latent ranking of the actual strengths of each candidate that individual voters – and by extension, the election itself – are attempting to estimate given the displayed abilities of those candidates. To acquire the ground truth ranking of the candidates, we assume that each candidate has an “inherent ability”, and we denote it by $\phi _ { j }$ for the candidate $c _ { j } .$ It may be a certain attribute of $c _ { j } ,$ such as the height of a person, the quality of a product. We assume that the inherent ability $\phi _ { j }$ follows a uniform distribution in the region [0,1]. Then the ground truth rank $r _ { j }$ of candidate $c _ { j }$ is acquired based on $\phi _ { j } ,$ and denote by $R _ { 0 } = [ r _ { 1 } , r _ { 2 } , . . . , r _ { M } ]$ the ground truth ranking of candidates. Intuitively, a larger inherent ability of a candidate corresponds to a higher rank. Because voters may not be perfectly aware of $\phi _ { j }$ in practice, we introduce $\widetilde { \phi } _ { i j } ,$ the displayed in herent ability of candidate $c _ { j }$ for voter $\nu _ { i } ,$ and we assume that voters evaluate candidates and decide whether approve candidates or not based on it. Denote by $B _ { i } = [ \widetilde { b } _ { i 1 } , \widetilde { b } _ { i 2 } , . . . , \widetilde { b } _ { i M } ]$ the ballot given by voter $\nu _ { i } ,$ and if $\nu _ { i }$ declares his or her approval for the candidate $c _ { j } , \ b _ { i j } = 1$ otherwise, $b _ { i j } = 0 .$ . As shown in Fig. 1, the $\widetilde { \phi } _ { i j }$ is a random variable following a uniform distribution in the region $[ \phi _ { j } - \phi _ { j } ( 1 - \beta _ { i j } ) , \phi _ { j } + ( 1 - \phi _ { j } ) ( 1 - \beta _ { i j } ) ] . \beta _ { i j } \in [ 0 , 1 ]$ represents the accuracy of the displayed inherent ability of candidate $c _ { j }$ for the voter $\nu _ { i } ,$ notice that a larger $\beta _ { i j }$ brings a narrower distribution region, and a more accurate displayed inherent ability $\widetilde { \phi } _ { i j } .$ . When $\beta _ { i j } = 1 , \ \widetilde { \phi } _ { i j } = \phi _ { j }$ , which means that voter $\nu _ { i }$ can evaluate the candidate $c _ { j }$ exactly according to

![](/api/attachments/5Q3JH6NU/fulltext/images/24445bb8e552eb91cd92ea516758bf47d51b9d063bf998b94ea626b8042fc3ed.jpg)

$$
B _ {i}
$$

(a) k=2  
![](/api/attachments/5Q3JH6NU/fulltext/images/e60d1e446474fb4e271fb7129a50759417dd9b854b80fb0678e0ef1cd24a9edb.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/69ea64a5278d7159fd56f1b17031159e07f62af65ac62c752b6c9f8cd9c7ed25.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/e9b82b6b4d165dd9e6ff530ac6a7b2af00309eefe4b6d4b6cb2ce0cf31c5fac4.jpg)  
Fig. 3. Election outcome effectiveness measure D versus ballot length $L _ { 0 }$ with various $k ,$ where $N = 1 0 0 , M = 1 0 , \beta = 0 . 9$ and the length is identical. The results were averaged over 100 independent trials.

Table 1 Election outcome efectiveness measure D versus ballot length $L _ { 0 }$ with various $k ,$ where $N = 1 0 0 , M = 1 0$ , and $\beta = 0 . 9 .$ The results were averaged over 100 independent trials.

<table><tr><td> $L_0$ </td><td>k=2</td><td>k=3</td><td>k=5</td></tr><tr><td>1</td><td>1.36</td><td>4.33</td><td>14.99</td></tr><tr><td>2</td><td>0.08</td><td>2.12</td><td>4.64</td></tr><tr><td>3</td><td>0.88</td><td>1.11</td><td>2.59</td></tr><tr><td>4</td><td>0.88</td><td>2.39</td><td>2.09</td></tr><tr><td>5</td><td>1.5</td><td>2.40</td><td>0.79</td></tr><tr><td>6</td><td>9.6</td><td>5.01</td><td>1.89</td></tr><tr><td>7</td><td>16</td><td>17.69</td><td>2.5</td></tr><tr><td>8</td><td>16</td><td>21</td><td>7.61</td></tr><tr><td>9</td><td>16</td><td>21</td><td>25</td></tr><tr><td>10</td><td>16</td><td>21</td><td>25</td></tr></table>

the inherent ability. Whereas when $\beta _ { i j } = 0 , \tilde { \phi } _ { i j }$ is a random variable with a uniform distribution in the region $[ 0 , 1 ] ,$ and voter v makes random decision on whether to approve the candidate $c _ { j }$ or not. Note that in this paper, we assume that the displayed accuracy $\beta _ { i j }$ for all candidates and voters are identical, meaning $\beta _ { i j } = \beta$ for all $i \in [ 1 , N ]$ and $j \in [ 1 , M ]$

The length of the ballot $B _ { i }$ is $L _ { i } = | \{ \widetilde { b } _ { i j } | \ \widetilde { b } _ { i j } = 1 , 1 \leq j \leq M \} |$ , and $0 \leq$ $L _ { i } \ \leq \ M .$ While in practice of the multi-winner elections based on approval balloting, there are two common restrictions of ballot length often observed. One is that the length of the approval ballots voters submitted is fixed to be identical, and another is that there is an upper bound on the number of candidates that voters can choose in individual ballots. Given this, to investigate the optimal ballot length objectively and comprehensively, we define the ballot length and perform experiments respectively. For the first one, we assume that the length of all the ballots $L _ { i } { = } L _ { 0 }$ for all $i \in [ 1 , N ]$ . While for the second one, we assume that $L _ { i }$ is a random variable following a uniform distribution in the region $[ 1 , L _ { 0 } ]$ , as shown in Fig. 2.

## 2.2. Efectiveness measure of election outcome with approval balloting

Under approval-based voting, denoted by $A = ( a _ { i j } ) _ { N \times M }$ the ballot matrix, in which $a _ { i j } = 1$ represents that the voter v declares his or her approval for the candidate $c _ { j } ,$ otherwise, $a _ { i j } = 0$ . Accordingly, $\begin{array} { r } { L _ { i } = \sum _ { j = 1 } ^ { M } a _ { i j } } \end{array}$ is the length of the ballot submitted by v and $S _ { j } = \textstyle \sum _ { i = 1 } ^ { N }$ a <sub>ij</sub> is the t-approval score of the candidate $c _ { j } ,$ and the final ranking of candidates $\hat { R }$ can be obtained by sorting their t-approval scores in the descending order, with which the winning committee can be determined. As a result, the efectiveness of the election outcome can be quantified by measuring the distance D between the final ranking of candidates $\overset { \vartriangle } { \hat { R } }$ and the ground truth ranking $R _ { 0 } .$

There are two popular distance measures which can be used to evaluate the similarity of two rankings, the Spearman footrule distance and the Kendall tau distance. The Spearman footrule distance is the sum, over all candidates $c _ { j } \in C ,$ of the absolute diference between the rank of $c _ { j }$ according to the two rankings. Then the Spearman footrule distance between the final ranking of candidates $\hat { R }$ and the ground truth ranking $R _ { 0 }$ is

$$
F (\hat {R}, R _ {0}) = \sum_ {j = 1} ^ {M} | \hat {R} (c _ {j}) - R _ {0} (c _ {j}) |.\tag{1}
$$

While, the Kendall tau distance counts the number of pairwise dis agreements between two rankings, and the distance between the final ranking of candidates $\hat { R }$ and the ground truth ranking $R _ { 0 }$ is

![](/api/attachments/5Q3JH6NU/fulltext/images/6157d261b1ee50df57f5a0d0a762b7e901d93857bd14914b4c74f991317dcea6.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/d6fa1dc941c30fdb0810db6f4f235a114343196e98dc059083a85bd440334125.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/196832af4906f169021b5d7fc6152290e5a067be1c49d6cb5438b474f43cfaae.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/66c5525839f75099e5244b58b3ca1daa21f118cb9cc978849907bcc8898237e7.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/ad8ac9c59b5884050bde7eb8f9ff01efb29fc6252d416268f2505e58b2fd5beb.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/e96fc82942581a17d4723d9bf93478a5fe49dfc88d488b9ac3ecf966ba3d91a1.jpg)  
Fig. 5. Election outcome efectiveness measure D versus ballot length $L _ { 0 }$ with various $\beta ,$ where N = 100, $M = 1 0 ,$ and $k = 3 .$ . The results were averaged over 100 independent trials.

$$
K (\hat {R}, R _ {0}) = | \{(c _ {i}, c _ {j}) | i <   j, \hat {R} (c _ {i}) <   \hat {R} (c _ {j}), \quad b u t \quad R _ {0} (c _ {i}) > R _ {0} (c _ {j}) \} |.\tag{2}
$$

Notice that $\hat { R } ( c _ { j } )$ and $R _ { 0 } ( c _ { j } )$ are the rank of candidate $c _ { j } .$ Intuitively, the smaller the value of $F ( \overset { \land } { R } , R _ { 0 } )$ and $K ( \stackrel { \wedge } { R } , R _ { 0 } )$ is, the more efective the election outcome is. It should be noted that we have performed a host of experiments and found that there was no diference between the two distance measures in evaluating the similarity between the election outcome $\hat { R }$ and the ground truth ranking $R _ { 0 } .$ Thus, we use the Kendall tau distance $K ( \stackrel { \wedge } { R } , R _ { 0 } )$ to evaluate the efectiveness of the election outcomes, and denote it by $D = K ( \hat { R } , R _ { 0 } )$

In sum, the problem of finding the optimal individual ballot length can be solved by finding a ballot length $L ^ { ' }$ which can minimize the distance between the election outcome $\hat { R }$ and the ground truth $R _ { 0 } .$ Given this, we consider approval-based multi-winner voting rules that take as an input a tuple $( V , C , A , L _ { 0 } ,$ k) of voters $V ,$ candidates $C ,$ the ballot matrix $A ,$ ballot-length $L _ { 0 } ,$ a positive integer $k \leq | C |$ , which is the target winning committee size. It is natural to consider the top k can didates in the election outcome as the winning committee. Given this, in this paper, we consider the rank of candidates which are not bigger than k in the election outcome $\hat { R }$ as the first and the rank of candidates which are bigger than k in the election outcome $\hat { R }$ as the second, which means that there can be ties in $\hat { R } .$ . Similarly, for the precision of counting the distance between $\hat { R }$ and $R _ { 0 } ,$ we consider the rank of candidates in ground truth ranking $R _ { 0 }$ which are not bigger than k as the first, and the rank of candidates which are bigger than k are considered as the second. Note that in our experiments, if $c _ { i }$ and $c _ { j }$ share the same rank in $\hat { R }$ but they are ranked in diferent positions in $R _ { 0 } ,$ there will be a pair of disagreement between two rankings $\hat { R }$ and $R _ { 0 } ,$ which sounds reasonable because the election outcome failed to provide the correct information for decision makers.

## 3. Experimental results of optimal ballot length in multi-winner elections

We now try to find the optimal ballot lengths $L ^ { ' }$ with diferent $\beta$ and k in diferent situations of ballot length restrictions. We first generate various sets of synthetic ballots using the experimental ballot generation method, and then we convert them into the rankings of candidates, that is, the election outcomes. We next compare the efectiveness of the election outcomes and find the optimal ballot-length which leads the election outcome most appropriate the ground truth. We focus specifically on the investigation of relationship between the target committee size k and the optimal ballot-length $L ^ { ' }$ with diferent restrictions of ballot length. Moreover, we compare the experiment results between two restrictions of ballot length, i.e. identical length and length with upper bounds. For the convenience of investigation, the number of candidates M is fixed to 10. All experiments are repeated 100 times in order to obtain stable results.

## 3.1. Experimental results of ballots with fixed lengths

## 3.1.1. The existence of the optimal ballot length

To investigate the existence of the optimal ballot length, we perform a host of experiments and present the efectiveness measure of election outcome D as a function of the ballot length $L _ { 0 }$ in Fig. 3, in which $N = 1 0 0 , \ M = 1 0$ , and $\beta { = } 0 . 9$ . The specific data is also presented in Table 1, and the best efectiveness measure is emphasized in bold and italic. As we can see, the efectiveness measure of election outcome is Ushaped in the variance of ballot length. In other words, there is an optimal solution of how many candidates should be involved in a ballot with a kind of combination of β, N, M and k. It should be noted that we have conducted a variety of experiments and obtained similar results.

## 3.1.2. The impact of the ballot accuracy

To investigate the impact of the ballot accuracy $\beta$ on the determining of the optimal ballot-length $L ^ { * } ,$ we perform numerical experiments and present the election outcome efectiveness measure D with various $L _ { 0 }$ and $\beta$ in Fig. 4 and Fig. 5. We observe that, with the increasing of the ballot accuracy $\beta$ in Fig. $^ { 4 , }$ the “valley” is becoming more and more obvious. In other words, when the ballot accuracy is low, the election outcomes of many ballot-length options $L _ { 0 }$ are very similar to each other. However, when the ballot accuracy is high, election outcomes of the ballot length which approximates the target size k outperform the other options of ballot length by a significant margin. Fig. 5 strengthens this analysis further and suggests that when the voters can provide ballots with high accuracy, the length of individual ballot should be a number very close to the target size k. When the ballots are not accurate, there are a lot of choices of the ballot length. Furthermore, when the ballot accuracy is 1, we find that the best ballot length is equal to k. Clearly, if the ballot accuracy $\beta = 1$ , the candidates chosen by voter $\nu _ { i }$ must be the top- ${ \mathbf { \nabla } } \cdot { L } _ { 0 }$ candidates. Given this, we have $R _ { 0 } = \{ 1 , ~ . ~ . ~ . ~ 1 , ~ 2 , ~ . ~ . ~ . ~ 2 \}$ , the ground truth ranking of the candidates, in which $^ { \mathfrak { a } } \mathbf { 1 } ^ { \mathfrak { n } }$ and $" 2 "$ are the rank of the corresponding candidates, and the number of $^ { \mathfrak { a } } \mathbf { 1 } ^ { \mathfrak { n } }$ is k. The election outcome $\hat { R }$ will be $\hat { R } = \{ r _ { 1 } = 1 , ~ r _ { 2 } = 1 , ~ . ~ . ~ . ~ r _ { L _ { 0 } } = 1 , ~ r _ { L _ { 0 } + 1 } = 2 , ~ r _ { L _ { 0 } + 2 } = 2 , ~ . ~ . ~ . ~ r _ { M } = 2 \} ,$ in which $L _ { 0 }$ is the length of ballots. The distance between the ground truth $R _ { 0 }$ and the election outcome $\hat { R }$ is as the following:

![](/api/attachments/5Q3JH6NU/fulltext/images/3892d247ded3300bbb6e512d97956485bea1f3cf80f6072074afb13b04da8c22.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/1438799e5e3ba1693840d67d2e0e4022542ac7adc8689866c532ea39beb53803.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/f3e18c1332aceff2954933ed472b14c57990d331860ef330d8ece198ab2075bb.jpg)

$$
D (\widehat {R}, R _ {0}) = \left\{ \begin{array}{c} k (L _ {0} - k) + (L _ {0} - k) (M - L _ {0}), L _ {0} > k \\ 0, L _ {0} = k \\ L _ {0} (k - L _ {0}) + (k - L _ {0}) (M - k), L _ {0} <   k \end{array} \right.\tag{3}
$$

Obviously, the election outcome of $L _ { 0 } = k$ is most efective. Given this, we have concluded that the best ballot length is equal to k when the ballot accuracy is 1. Overall, the accuracy of individual ballots has a remarkable impact on the determination of how many candidates should be chosen in an individual ballot.

## 3.1.3. The impact of the target committee size

To investigate the impact of the number of candidates desired k on the determining of the optimal ballot-length $L ^ { * } ,$ that is, the relationship between the k and the optimal ballot-length $L ^ { ' , }$ , we perform numerical experiments and present the efectiveness measure D with various k and $L _ { 0 }$ in Fig. 6, where $\beta { = } 1 . 0 , 0 . 9$ , and 0.8. The color of each lump corresponds to the value of the Kendall tau distance D. A blue lump corresponds to a small value for Kendall tau distance, meaning that the election outcome is efective, while a red lump corresponds to a large value for Kendall tau distance, meaning that the election outcome is quite diferent from the ground truth. We observe that, with increasing values of the $k ,$ the optimal ballot-length $L ^ { * }$ increase. This suggests that the number of candidates desired k has a remarkable impact on the chosen of best ballot length. To some degree, we can consider that when the ballots are reliable, the ballot length should be chosen as a number which approximates the target committee size k.

## 3.1.4. The impact of the number of voters

To investigate the impact of the number of voters N on the efectiveness of election outcome, we perform numerical experiments with various $N ,$ which are shown as colored lumps in Fig. 7, and the ballot accuracy $\beta$ in experiments is 0.9. The color of each lump corresponds to the value of the Kendall tau distance between the election outcome and the ground truth. A blue lump corresponds to a small value for Kendall tau distance, meaning that the election outcomes are similar to ground truth, while a red lump corresponds to a large value for Kendall tau distance, meaning that the election outcomes are not efective. We observe that, the blue lumps are getting deeper and deeper with the increasing of the number of voters N, which means that the election outcomes are more and more efective. This suggests that decision makers can improve the efectiveness of the election outcome by adding more voters.

## 3.2. Experimental results of ballots with variable lengths

## 3.2.1. The existence of the optimal ballot length

To investigate the existence of the optimal ballot length in the situation of ballot length with upper bounds, we perform a host of experiments and present the efectiveness measure of election outcome D as a function of the ballot length $L _ { 0 }$ in Fig. $^ { 8 , }$ in which $N { = } 1 0 0 , M { = } 1 0 ,$ and $\beta = 0 . 9 .$ . Similar to the situation above, the efectiveness measure of election outcome is U-shaped in the variance of ballot length, meaning that there is an optimal solution of how many candidates should be involved in a ballot with a kind of combination of $\beta ,$ N, M and k.

![](/api/attachments/5Q3JH6NU/fulltext/images/cc19983c67b7c34ff803040634c17a2320a868cb79daf8eb5651cd50a724dad2.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/28d9eeaf7caa245ee3b7736af90383f2c1b0759dc6b6f0ec29f7652306d7fa7c.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/68057a2fb2add5d668431f62ffb0fa805fc34508ef207f4ce1927bee8c21327a.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/723bd610934bd7be31f625eef0aa10100eddd71702d554786fc4df4270de6d71.jpg)  
Fig. 8. Election outcome efectiveness measure D versus ballot length $L _ { 0 }$ with various $k ,$ where N = 100, M = 10, β=0.9 and the length has an upper bound. The results were averaged over 100 independent trials.

## 3.2.2. The impact of the ballot accuracy

To investigate the impact of the ballot accuracy $\beta$ on the determining of the optimal ballot-length $L ^ { ' }$ when the ballot length has an upper bound, we perform numerical experiments and present the election outcome efectiveness measure D with various $L _ { 0 }$ and $\beta$ in Fig. 9. It should be noted that we have observed results which are slightly diferent to the results when the ballot length is identical. When the ballot accuracy is high, the optimal ballot length $L ^ { * }$ should be a number slightly bigger than the target size $k ,$ while the election outcomes of many ballot-length options $L _ { 0 }$ are very similar to each other when the ballot accuracy is low, meaning that there are a lot of choices in the ballot length designing.

## 3.2.3. The impact of the target committee size

To investigate the impact of the number of candidates desired k on the determining of the optimal ballot-length $L ^ { ' }$ in the situation of the ballot length with upper bounds, we perform numerical experi ments and present the efectiveness measure D with various β, k and $L _ { 0 }$ in Fig. 10. The color of each lump corresponds to the value of the Kendall tau distance D. A blue lump corresponds to a small value for Kendall tau distance, meaning that the election outcome is effective, while a red lump corresponds to a large value for Kendall tau distance, meaning that the election outcome is quite diferent from the ground truth. Similarly, we find that the number of candidates desired k has a remarkable impact on the chosen of best ballot length, that is, with increasing values of the k, the optimal ballotlength $L ^ { ' }$ increases. However, it is worth noting that the optimal ballot-length $L ^ { ' }$ can be slightly bigger than the target size of winning committee k.

In addition, we have found similar results when investigating the impact of the number of voters N in the situation of ballot length with upper bounds: more ballots bring more efective election outcome. Due to the limitation of space, this result is not shown here.

Overall, experimental results show that the ballot accuracy and the target winning committee size have impact on the determining of the optimal ballot length both in the situation of identical length and the length with upper bounds. Furthermore, the optimal ballot length $L ^ { ' }$ should be chosen as a number which approximates the target committee size k when the ballot length is identical, while for the ballot length with upper bounds, the optimal ballot length $L ^ { ' }$ should be chosen as a number slightly bigger than the target committee size $k .$

## 4. Conclusion and discussion

Studies on voting and selecting have received increasing attention in the past few decades. In this study, we focused on the choosing of the optimal individual ballot length in diferent situations of ballot length restrictions. We accomplished this study by modifying an experimental data generation method to generate the required individual synthetic ballots with adjustable accuracy and length. We have demonstrated that both the accuracy and the number of candidates desired have significant efects on the optimal ballot length.

Using the synthetic ballots generation method, we performed many experiments and obtained some useful findings: 1) when the ballot length is identical, the more accurate the ballots are, the closer the optimal ballot length is to the number of target winning committee size, while for the ballot length with upper bounds, the optimal ballot length is slightly bigger than the target winning committee size; 2) More voters bring more efective election outcomes. These evidences can serve as a further justification for researchers and managers incentives designing the complete election system.

This paper makes several novel contributions to the literature of the optimal ballot-length in approval balloting-based multi-winner elections. First, we modified and tested a synthetic ballots generation method that can aid researchers in their voting studies. Second, our experimental results shed important light on the investigation of the relationship between the number of target winning committee size and the number of candidates which they will optimally approve of. Finally, the conclusions we have made may be helpful in many situations of election with approval balloting.

<sup>=</sup> <sup>0</sup>. β

Fig. 9. Election outcome efectiveness measure D versus ballot length L0 and target size k with various β, where N = 100, M = 10. The results were averaged over 100 independent trials.

![](/api/attachments/5Q3JH6NU/fulltext/images/dd6a6378ce60ccb19be8ade6cc342f593c714d4c8f61d3e3eb287977d8431ebb.jpg)

<sup>=</sup> <sup>0</sup>. β  
Fig. 10. The election outcome efectiveness measure D with various β, L0 and k, where M = 10 and N=100. The results were averaged over 100 independent trials.  
![](/api/attachments/5Q3JH6NU/fulltext/images/e0b77b413c7f66b3e1d415cc98da56423734c36d43d52fb809db40b0ae06d903.jpg)

<sup>=</sup> <sup>1</sup>. β  
![](/api/attachments/5Q3JH6NU/fulltext/images/a2e0913ef598d20537112cfddeb9e5f67c6322d7222efe2ba4c316642aa1a73d.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/d67f641a7f8af258951ccb6fc3734155bfb4bc88e94bdb648cfcee02d068ba6c.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/fda712a875ea002539ee60c7357af30210624517a32efb94e63ed58e430032ff.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/fc656fbe2c124e71f06348216b45682e58a330a6fc59004abe2ab1101aec1012.jpg)

## Acknowledgments

Jun Wu acknowledges the National Natural Science Foundation of China under grant nos. 71871217, 71371185, 71690233 and the Program for New Century Excellent Talents in University under grant no. NCET-12-0141. Hongzhong Deng acknowledges the National Natural Science Foundation of China under grant no. 71771214. Xin Lu acknowledges the National Natural Science Foundation of China under grant nos. 71522014, 71771213, 71790615, and 91846301. We thank Yapeng Li, Mingze Qi and Ye Deng for their helpful insights.

## References

[1] J. Freixas, B. Tchantcho, N. Tedjeugang, Voting games with abstention: linking completeness and weightedness, Decision Support Systems 57 (1) (2014) 172–177.

[2] P. Skowron, P. Faliszewski, J. Lang, Finding a collective set of items: from proportional multirepresentation to group recommendation, Artificial Intelligence 241 (2016) 191–216.

[3] C. Dwork, R. Kumar, M. Naor, D. Sivakumar, Rank aggregation methods for the web, WWW 2001, Proceedings of the 10th International Conference on World Wid Web, 2001, pp. 613–622 New York.

[4] J. Freixas, X. Molinero, S. Roura, Complete voting systems with two classes of voters: weightedness and counting, Annals of Operations Research 193 (1) (2012) 273–289.

[5] E. Elkind, P. Faliszewski, P. Skowron, A. Slinko, Properties of multiwinner voting rules, Social Choice & Welfare 48 (2017) 599–632.

[6] M. Regenwetter, B. Grofman, Approval voting, borda winners, and condorcet winners: evidence from seven elections, Management Science 44 (4) (1998) 520–533.

[7] J.G. Birnberg, L.R. Pondy, C.L. Davis, Efect of three voting rules on resource allocation decisions, Management Science 16 (6) (1970) 356–356.

[8] B.E. Lee, How long is a piece of string? An exploration of multi-winner approval voting and ballot-length restrictions, arXiv:1711.05092, Technical Report. (1711)

[9] P.C. Fishburn. JD.C. Little. An experiment in approval voting. Management Science 34 (5) (1988) 555–568.

[10] S.J. Brams, P.C. Fishburn, Approval voting, American Political Science Review 72 (3) (1978) 831–847.

[111 E. Carreras, A decisiveness index for simple games, European Journal of Operationa Research 163 (2) (2005) 370–387.

[12] J.F. Laslier, K.V.D. Straeten, Strategic voting in multi-winner elections with ap proval balloting: a theory for large electorates, Social Choice & Welfare 47 (3) (2017) 1–29.

[13] R. Lachat, J.F. Laslier, K.V.D. Straeten, Strategic voting under committee approval: an application to the 2011 regional government election in Zurich, PSE Working Papers, 2015.

![](/api/attachments/5Q3JH6NU/fulltext/images/2b2a795f138c28029ca49feb1a2826fd27b6c09b662a8ba4152bcaa77a1310b5.jpg)

[14] Y. Xiao, Y. Deng, J. Wu, H. Deng, L. Xin, Comparison of rank aggregation methods based on inherent ability. Naval Research Logistics 64 (6) (2017) 556–565

![](/api/attachments/5Q3JH6NU/fulltext/images/35c06779b049ed0d2d197878587ffff74a8fd4f3646983f752f3c34a83707ca3.jpg)

![](/api/attachments/5Q3JH6NU/fulltext/images/0ff86359f68bf49a968f0c0856f4f41f362fa42c8bee597c40a97e6f8505353c.jpg)  
Yu Xiao received the B.S. degree in communication engineering from Sichuan University. Chengdu. Sichuan. China, in 2014 and the M.S. degree in management science and engineering from National University of Defense Technology, Changsha, Hunan, China, in 2016. He is currently pursuing the Ph.D. degree in management science and engineering at National University of Defense Technology. His research interest includes multi-criteria decision analysis and rank aggregation, graph theory and voting theory.

![](/api/attachments/5Q3JH6NU/fulltext/images/6c042ee261be737543e00a11f7409f8ee2c375a99ae9e8fc327de4e5468d036a.jpg)

Dr. Hongzhong Deng received his Ph.D. degree in management science from National University of Defense Technology, China, in 2008. From 2007 to 2008, he was an academic visitor at the London School of Economics and Political Science, UK. From 2018 to 2019, he was an academic visitor at the University of Oxford, UK. He joined National University of Defense Technology in 2002 and currently is a professor. His research interests are in the areas of complex systems, social networks analysis.

Dr. Xin Lu received his B.S. degree in management science from Sichuan University, China, in 2006 and Ph.D. degree in Department of Public Health Sciences from Karolinska Institutet, Sweden, in 2013. From 2009 to 2013, he was a research associate at the Department of Sociology, Stockholm University, Sweden. From 2012 to 2013, he was a research fellow at the Institute for Future Studies, Stockholm University, Sweden. He joined National University of Defense Technology in 2013 and currently is a professor. His research interests are in the areas of big data, social networks and dynamics of human behavior.

Dr. Jun Wu received his B.S. degree in management science from Sichuan University, China, in 2002 and Ph.D. degree in management science from National University of Defense Technology, China, in 2008. From 2007 to 2008, he was a visiting Ph.D. student at the Institute for Mathematical Sciences, Imperial College London, UK. From 2016 to 2017, he was an academic visitor at the Department of Computer Science, University of California, Davis. He joined National University of Defense Technology in 2008 and currently is a professor. His research interests are in the interdisciplinary areas of mangement science, information science and network science.
