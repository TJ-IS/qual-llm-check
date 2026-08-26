---
otero_id: 236
otero_key: "FTPRRK75"
title: "A Prescriptive Analytics Method for Cost Reduction in Clinical Decision Making"
authors: "Xiao Fang; Yuanyuan Gao; Paul Jen-Hwa Hu"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/14372"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A PRESCRIPTIVE ANALYTICS METHOD FOR COST REDUCTION IN CLINICAL DECISION MAKING<sup>1</sup>

Xiao Fang Alfred Lerner College of Business and Economics, University of Delaware, 357 Purnell Hall, Newark, DE 19716 U.S.A. {xfang@udel.edu}

Yuanyuan Gao College of Business and Economics, California State University, East Bay, 25800 Carlos Bee Boulevard, Hayward, CA 94542 U.S.A. {yuanyuan.gao@csueastbay.edu}

Paul Jen-Hwa Hu David Eccles School of Business, University of Utah, 1655 East Campus Center Drive, Salt Lake City, UT 84112-8939 U.S.A. {paul.hu@eccles.utah.edu}

Containing skyrocketing health care costs is imperative. Toward that end, prescriptive analytics that analyzes health care data to recommend optimal decisions is both relevant and crucial. We develop a novel prescriptive analytics method to improve the cost effectiveness in clinical decision making (CDM), a critical health care dimension that can greatly benefit from analytics. Effective prescriptive analytics for CDM has to address its probabilistic, cost-sensitive, and investment-related characteristics simultaneously. Unlike existing methods that often overlook the investment-related characteristic, the proposed method accounts for all of these characteristics. Specifically, our method considers two sets of costs associated with clinical decisions—before and after an investment—in combination with the probabilities of cost changes due to the investment. In contrast, prevalent methods only emphasize one set of costs, before an investment. Furthermore, the proposed method involves both clinical and investment decisions, whereas existing methods ignore investment decisions. Empirical evaluations with two real-world clinical data sets indicate that the proposed method consistently and significantly outperforms several salient methods from previous research, thereby demonstrating the value of addressing the investment-related characteristic in efforts to improve CDM

Keywords: Machine learning, cost-sensitive learning, prescriptive analytics, health care, clinical decision making

## Introduction

Health care costs are skyrocketing. According to the Centers on Medicare & Medicaid Services, health care spending accounted for 17.92% of the U.S. gross domestic product (GDP)

in 2017, with total costs reaching \$3.5 trillion in 2017<sup>2</sup>. Substantial, pronounced efforts have been undertaken to reduce health care costs and improve service quality and patient outcomes (e.g., Agarwal et al. 2010; Aron et al. 2011; Menon and Kohli 2013; Menon et al. 2000). However, without proper cost containment measures, the growth of U.S.

health care expenditures is projected to outpace that of the nation’s GDP during 2018–2027 (Centers for Medicare & Medicaid Services). As Berwick and Hackbarth (2012, p. 1513) caution, “The need is urgent to bring US health care costs into a sustainable range for both public and private payers.” It is, therefore, imperative to develop viable solutions to curb rapidly rising costs in health care (Mango and Riefberg 2009).

Data-driven analytics is promising for increasing the cost effectiveness of health care, which is an inherently dataintensive sector (Dhar 2014; Fang et al. 2013). For example, the U.S. health care system has accumulated enormous amounts of data that pertain to clinical services and patient care (e.g., electronic health records [EHR]), medical claims, medications and their adverse effects, and pharmaceutical research and development. These data, rich in both breadth and depth, enable the development of analytics methods for optimal decision making (Davenport 2013). Indeed, datadriven analytics is central to health information technology (HIT), which represents a crucial and consequential research opportunity for information systems (IS) (Agarwal and Dhar 2014; Agarwal et al. 2010; Fichman et al. 2011).

Effective analytics can generate clinical intelligence about patients’ risks for future adverse health events (Lin et al. 2017), such that an

emerging avenue for knowledge discovery arises from using digital technology to enable new kinds of mathematical healthcare modeling and simulations .… [The] implementation and use of healthcare analytics tools and how they should be integrated with electronic health records warrants future research attention (Fichman et al. 2011, p. 425).

Echoing this call, Kohli and Tan (2016, p. 564) advocate that “IS researchers with technical and analytical interests can contribute to the design of algorithms and modeling … to further enrich EHR use in analytics.” The significance of data-driven analytics in health care also resonates with design science research that emphasizes the development and utilization of effective information technology artifacts, such as mathematical models and computational methods and systems, to address practical needs, as has been a focus of IS research since its inception (Hevner et al. 2004).

Toward that end, prescriptive analytics is particularly important and relevant, in that it seeks the best solution and outcome, given various choices and known parameters (Phillips-Wren et al. 2015; Wang and Hajli 2017; Watson 2014). For clinical decision making (CDM)—a process of using clinical data to make decisions about patient care and management<sup>3</sup>—prescriptive analytics can identify at-risk patients and recommend optimal clinical solutions (Kohli and Tan 2016), which could better support physicians’ CDM with patientlevel analyses. A growing emphasis on patient-level analytics has emerged as researchers and clinicians recognize that the ultimate impacts of HIT need to be measured at the patient level (Bardhan et al. 2014). In considering the values and uses of prescriptive analytics, we respond to calls for more attention to patient-level data analyses to generate useful, actionable insights (Angst et al. 2010; Gao et al. 2010).

Accordingly, we seek to develop a novel prescriptive analytics method to contain costs in the CDM realm. To achieve this goal, we need to address several eminent characteristics of CDM. First, CDM is intrinsically probabilistic because it builds on probabilistic diagnoses. Take mechanical ventilation, an invasive intervention to assist a patient’s respiration, as an example. An important clinical decision facing the physician is whether a patient should be removed from ventilation and rely on his or her own respiration system for breathing. Physicians usually make this decision on the basis of an estimated likelihood that the patient has gained sufficient recovery to breathe independently, which is a probabilistic diagnosis. Second, CDM is cost sensitive, because different decisions lead to differential costs. Continuing with the ventilation example, a physician’s decision to remove a patient from mechanical ventilation, when the patient actually should stay on ventilation, can result in complications that differ from those commonly associated with not removing a patient from ventilation when the patient in effect does not need it. These resulting complications require varying costs to treat. Third, the costs associated with clinical decisions could be altered by an investment. For example, an investment in putting patients on advanced ventilation (at an approximate cost of \$1,636 in the United States) could avoid a particular complication that normally would occur in the absence of this investment, thereby obviating the cost of treating that complication (Antonelli et al. 1998; Dasta et al. 2005), which in turn would alter the costs associated with distinct clinical decisions.

Existing prescriptive analytics methods usually consider the probabilistic and cost-sensitive characteristics of CDM but ignore its investment-related characteristic (Ling et al. 2006; Qiu et al. 2015; Turney 1995). For example, Qiu et al. (2015) develop a method to support physicians’ bed reservation decisions for patients by considering the probabilistic diagnosis that a patient needs a bed in the hospital. This method is cost sensitive in that it accounts for various costs associated with different decisions. However, effective support for CDM also requires prescriptive analytics methods to address investmentrelated characteristic. Our proposed method differs from extant methods by considering all three characteristics simultaneously. For the investment-related characteristic, we consider two sets of costs associated with clinical decisions— before and after an investment—in conjunction with the probabilities of cost changes due to the investment, while existing methods focus on the costs before an investment only. Furthermore, a physician’s decision to make a particular investment may have considerable cost implications, such that the investment could alter the costs associated with his or her decision. Thus our method targets both clinical and investment decisions, while existing methods overlook the latter.

In the next section, we review related works and highlight several essential differences that separate our study from previous research. We then formally define the focal problem and propose a novel prescriptive analytics method to solve it. Next, we use two real-world clinical data sets to evaluate the proposed method, with several prevalent methods as benchmarks. We conclude by discussing some important contributions, implications, and limitations of this study.

## Literature Review

Typically, a clinical decision classifies a patient into one of several predefined classes, such as being a candidate for removal from mechanical ventilation or not. Existing prescriptive analytics methods treat clinical decisions as classification decisions and often take a cost-sensitive learning approach to support CDM (e.g., Ling et al. 2006; Qiu et al. 2015; Turney 1995). The stream of cost-sensitive learning research closely relates to our study. Common inputs for a cost-sensitive learning method include a training data set that comprises previously classified instances and a cost matrix in which each element indicates the cost of classifying an instance as class i if it actually belongs to class j. A method learns from training data to construct a classifier that then can be used to assign an unclassified instance to one of the predefined classes, which minimizes the expected cost of classifying the instance. Existing cost-sensitive learning methods can be broadly categorized as threshold moving, distribution altering, or test cost-sensitive learning. In the following, we review representative methods of each category and then discuss how our method differs from these prevalent methods.

## Threshold Moving

A classification method assigns unlabeled instances to maximize classification accuracy. For example, a binary classification method predicts the probability that an instance belongs to a particular class, then assigns the instance to be of that class if the predicted probability exceeds an accuracymaximization threshold (e.g., 0.5) or of the other class otherwise (Elkan 2001). In general, threshold moving employs a classification method to predict the probability that an instance belongs to a particular class and classifies the instance on the basis of a cost-sensitive threshold calculated from the given classification costs (Elkan 2001; Fang 2013; Margineantu 2002; Pazzani et al. 1994). For example, Zhou and Liu (2006) propose a threshold moving method to train cost-sensitive neural networks; Sheng and Ling (2006) develop a method to search for a cost-sensitive threshold that minimizes the total cost of classifying training instances, then use the threshold to classify unlabeled instances. Unlike most threshold moving methods that use class-dependent classification costs, Zadrozny and Elkan (2001) develop a method that relies on instance-dependent classification costs. Recent threshold moving research features both novel methods (Fang 2013) and innovative applications (Qiu et al. 2015). For example, Fang (2013) proposes a cost-sensitive naïve Bayes method that infers the order relation between an instance’s probability of belonging to a particular class and the costsensitive threshold (e.g., greater than, equal to, less than). This method iteratively learns and infers the order relations from training data, then uses the inferred order relations to classify unlabeled instances. Qiu et al. (2015) apply threshold moving to develop a method to support physicians’ bed reservation decisions for patients in the emergency department, with the objective of minimizing the expected bed reservation cost.

## Distribution Altering

Distribution altering instead changes the class distribution in training data, according to the specified classification costs (Breiman et al. 1984; Domingos 1999; Jiang et al. 2014). The class distribution in training data can be altered with undersampling or oversampling. Undersampling removes instances from training data; oversampling instead adds instances to training data. Such sampling can be further categorized as random or intelligent. Random undersampling randomly selects training data instances to eliminate, whereas intelligent undersampling chooses appropriate instances to remove. One-sided selection (Kubat and Matwin 1997) represents an intelligent undersampling method; it identifies borderline, noisy, and redundant instances for removal. Similarly, random oversampling randomly duplicates instances in training data, whereas intelligent oversampling (e.g., synthetic minority oversampling, or SMOTE; Chawla et al. 2002) generates appropriate, synthetic instances and incorporates them into training data. Li et al. (2017) follow Chawla et al. (2002) and propose methods for setting two key parameters in SMOTE: oversampling rate and size of neighborhood. Weiss (2004) provides a comprehensive review; Gao et al. (2017) offer a more recent survey of undersampling and oversampling methods originally developed for learning from imbalanced data sets.

Class distribution altering can be accomplished with instance weighting (Zhao 2008) as well. For example, the class distribution in training data could be implicitly altered with instances in the training data, weighted in proportion to their classification costs (Lee and Zhu 2011; Ting 2002). In an iterative naïve Bayes method, the updates to the class-attribute distributions learned by the naïve Bayes approach follow predefined increments, so it weights training instances differently (Gama 2000). Ting (2002) also proposes an instance weighting method to induce a cost-sensitive decision tree from training data. By assigning greater weights to instances with higher classification costs, this method steers decision tree induction to focus more on instances with higher classification costs, thereby reducing the likelihood of misclassifying them and ultimately lowering total classification costs. With a similar approach, Jiang et al. (2014) develop an instance weighting method to make the Bayesian networks cost sensitive. MetaCost, a prevalent distribution altering method (Domingos 1999), alters the class distribution in training data by relabeling instances instead of sampling or weighting them. The rationale is that if instances in training data are relabeled as their optimal classes, according to classification costs, a conventional method can be applied to the modified training data to induce an optimal cost-sensitive classifier. MetaCost follows this logic by computing the optimal class for each instance in the training data and relabeling the instance if the current class differs from its optimal class.

## Test Cost-Sensitive Learning

Both threshold moving and distribution altering aim to minimize classification costs; test cost-sensitive learning also considers attribute costs, or the costs of acquiring attribute values of a particular instance (Turney 1995). For example, physicians can order medical tests for patients (e.g., blood tests) before making clinical decisions; the costs of the prescribed tests are attribute costs. Test cost-sensitive learning classifies unclassified instances to minimize the sum of attribute and classification costs (Ling et al. 2006; Turney 1995; Weiss et al. 2013). Turney (1995) proposes a hybrid method, built on genetic algorithms and decision trees, for test costsensitive learning. Ling and his colleagues (Ling et al. 2006; Ling et al. 2004) also build test cost-sensitive learning methods on a decision tree by extending the tree induction to develop a method that comprises two phases: training and testing. In the training phase, a test cost-sensitive decision tree is learned from training data, with the objective of minimizing the sum of the attribute and classification costs. In the testing phase, an unclassified instance is classified by the learned decision tree, with an attribute cost incurred if any attribute value of the instance is not available. Unlike these methods, a test cost-sensitive learning method for naïve Bayes learns a naïve Bayes model from training data and then, in the testing phase, deliberately selects unknown attributes to acquire their values, which minimizes the sum of attribute and classification costs (Chai et al. 2004). Another proposed test cost-sensitive learning method learns from training data to discover a subset of attributes whose values need to be obtained (Weiss et al. 2013).

This review of extant literature reveals several important differences that separate the proposed method from existing ones. First, our method employs two classification cost matrixes and recognizes that an investment could alter classification costs probabilistically. That is, in our method, classification costs are probabilistic, whereas existing methods only use one classification cost matrix to classify instances and view classification costs as deterministic. Second, both threshold moving and distribution altering make classification decisions only: to which class an unclassified instance should be assigned. Instead, our method makes both investment and classification decisions. An investment decision differs from a test decision in test cost-sensitive learning, such that it entails whether to make an investment, whereas the latter targets which attribute values to obtain. Third, our method is distinct in its objective. Both threshold moving and distribution altering attempt to minimize classification costs; test costsensitive learning seeks to minimize the sum of attribute and classification costs. Our method instead aims to minimize the sum of investment and classification costs. An investment cost, incurred with an investment to alter the classification costs, differs from an attribute cost incurred to obtain the value of a particular attribute. In Table 1, we highlight these distinctions.

## Theoretical Foundation

Although our method is analytical, its conceptualization stems from a foundation in prospect theory (Kahneman and Tversky 1979), which explains how people decide among alternatives (choices) in scenarios that involve risk and uncertainty. This theory posits that people evaluate probabilities nonlinearly, unlike expected utility theory suggesting that people evaluate them linearly (Gonzalez and Wu 1999; Prelec 2000; Tversky and Wakker 1995). As Kahneman and Tversky (1979, p. 279) indicate, “the aggravation that one experiences in losing a sum of money appears to be greater than the pleasure associated with gaining the same amount.” Decision making thus might reflect separate evaluations of gains and losses, such that people tend to be risk averse in choices involving gains but risk seeking in choices involving losses (Shafir and LeBoeuf 2002; Tversky and Kahneman 1992).

Table 1. Key Differences between Proposed Method and Existing Cost-Sensitive Learning Methods

<table><tr><td></td><td>Proposed Method</td><td>Threshold Moving</td><td>Distribution Altering</td><td>Test Cost-Sensitive</td></tr><tr><td>Number of Cost Matrixes Considered</td><td>Two</td><td>One</td><td>One</td><td>One</td></tr><tr><td>Classification Cost</td><td>Probabilistic</td><td>Deterministic</td><td>Deterministic</td><td>Deterministic</td></tr><tr><td>Decision</td><td>Investment and classification</td><td>Classification</td><td>Classification</td><td>Test and classification</td></tr><tr><td>Objective</td><td>Minimize the sum of investment and classification costs</td><td>Minimize classification costs</td><td>Minimize classification costs</td><td>Minimize the sum of attribute and classification costs</td></tr><tr><td>Representative Studies</td><td></td><td>Elkan (2001); Qiu et al. (2015)</td><td>Domingos (1999); Jiang et al. (2014); Ting (2002); Zhao (2008)</td><td>Ling et al. (2006); Turney (1995); Weiss et al. (2013)</td></tr></table>

From a psychological perspective, a strong feeling of fear arises due to uncertainty or variability with regard to gains, because a genuine fear of losing a sure gain is more painful than the pleasure associated with a potential gain, even if the latter promises potentially greater payoffs. As Clark and Lisowski (2017, p. 7433) explain, people’s greater concerns about “losing what they have than about what they might gain” guide their behaviors. In the gain domain, “certainty increases the aversiveness of losses as well as the desirability of gains” (Kahneman and Tversky 1979, p. 269), but in the loss domain, fearing an outcome, uncertainty increases the attractiveness of risk and hope.

Such considerations also could apply to clinical decision making, in that dealing with patient complications involves financial costs, similar to losses. Physicians might perceive their decision tasks according to a loss domain (i.e., cost of treating the resulting complications) and thus prefer an option that might reduce misclassification probability and costs, which also lowers the total cost of treating the patient. In such a setting, physicians could seek risk and choose to make an investment, such as prescribing advanced ventilation for patients currently on mechanical ventilation, in an attempt to mitigate the total costs of patient care, assuming the investment amount is reasonable. In line with Tversky and Kahneman (1992), people tend to be risk seeking in a scenario filled with information about losses, such that they are more willing to make an investment to alter misclassification probabilities and costs.

This reasoning also implies a reflection, such that “risk aversion in the positive domain is accompanied by risk seeking in the negative domain” (Kahneman and Tversky 1979, p. 268). A preference reversal, from risk averse to risk seeking, thus might occur if the choice options switch from gains to losses (Kahneman and Tversky 1979). For example, in a loss domain with negative values (e.g., costs), people might prefer probabilistic, larger losses over known, smaller losses. As Kahneman and Tversky note, this reflection effect “eliminates aversion for uncertainty or variability as an explanation of the certainty effect” (p. 269).

Our theoretical foundation also integrate regret theory (Zeelenberg et al. 1996), which asserts “first, that many people experience the sensations we call regret and rejoicing; and second, that in making decisions under uncertainty, they try to anticipate and take account of those sensations” (Loomes and Sugden 1982, p. 820). By and large, people have a tendency of avoiding negative feelings (regret) and embracing positive feeling (rejoice) (Larrick et al. 1995); thus they compare the outcomes of different choices, and their emotions are inherent to the decision (Zeelenberg et al. 1996). For example, people experience regret if an option not chosen ultimately would have been better (Loomes and Sugden 1982). Comparing the respective outcomes of different choices can be viewed as a process in people’s minds; that is, people compare the outcome of the option they chose with the outcome that “might have been,” had they chosen differently, which implies people take potential regret into account when choosing among alternatives (Bell 1983). The amount of regret a person feels depends on the difference between outcomes, in line with prospect theory, so he or she might be risk averse if choices involve gains and risk seeking if choices involve losses (Bell 1983; Loomes and Sugden 1982). In our context, physicians might tend to estimate the plausible outcomes of different alternatives and choose the one that minimizes their estimated feeling of regret. For example, they might choose to make an investment to mitigate (total) costs, if the “no investment” choice seems to be associated with a higher level of regret.

## Investment-Adjusted Cost-Sensitive Learning: Problem and Method

To consider the probabilistic, cost-sensitive, and investmentrelated characteristics of CDM simultaneously, we formulate a new cost-sensitive learning problem (i.e., the investmentadjusted cost-sensitive learning problem) and propose a novel method to solve it.

## Problem Formulation

Let T be training data, in which each record corresponds to an already classified instance. A record consists of a vector of n attributes that jointly describe an instance, $X = \langle x _ { 1 } , x _ { 2 } , . . . , x _ { n } \rangle .$ and a class label y of the instance, $y \in \{ 0 , 1 \}$ . Let C be the classification cost matrix. As we show in Table 2, an element $c _ { i j }$ of C represents the cost of classifying an instance as class i when it actually belongs to class j, $i , j \in \{ 0 , 1 \}$

With an investment, there is a probability $\mathrm { o f } \ p _ { i j }$ that the classification cost $c _ { i j }$ changes to $c _ { i j }$ and a probability of 1 – $p _ { i j }$ that the investment fails and $c _ { i j }$ remains the same, $i , j \in \{ 0 , 1 \}$ Table 3 reveals the (new) classification cost matrix $\displaystyle { \overline { { C } } } ,$ and Table 4 summarizes the probability $p _ { i j }$ that a classification cost changes due to the investment, $i , j \in \{ 0 , 1 \}$

We define the investment-adjusted cost-sensitive learning problem as follows: Given training data T, cost matrixes C and C¯, the amount V of an investment, and the probability $p _ { i j }$ of classification cost change due to the investment, $i , j \in \{ 0 ,$ 1}, we need to learn from T to make two decisions for an unclassified instance: (1) whether to make the investment and (2) to which class we should classify an instance to minimize the expected total cost (i.e., sum of the investment cost and expected classification cost).

## Investment-Adjusted Cost-Sensitive Learning Method

To solve the problem, we make two assumptions. First, the cost of incorrectly classifying an instance logically is higher than that of classifying the instance correctly (Elkan 2001). We therefore assume $c _ { 1 0 } > c _ { 0 0 } , \overline { { c } } _ { 1 0 } > \overline { { c } } _ { 0 0 } , c _ { 0 1 } > c _ { 1 1 } ,$ and $\overline { { c } } _ { 0 1 } >$ $\overline { { c } } _ { 1 1 } .$ . Second, we assume that making an investment could reduce classification costs (Antonelli et al. 1998; Dasta et al. 2005), so $c _ { 0 0 } > \overline { { c } } _ { 0 0 } , c _ { 0 1 } > \overline { { c } } _ { 0 1 } , c _ { 1 0 } > \overline { { c } } _ { 1 0 } ,$ and $c _ { 1 1 } > { \overline { { c } } _ { 1 1 } } . { ^ 4 }$ These assumptions are both appropriate and consistent with previous research (Elkan 2001).

Next, we propose a way to make investment and classification decisions for an unclassified instance. Let p be the probability that the unclassified instance belongs to class 1. We can compute the expected total cost for that instance, for each possible combination of investment and classification decisions:

(1) If the investment decision is “no investment” and the instance is classified as class 1, the expected total cost $C _ { 1 }$ is given by

$$
C _ {1} = p c _ {1 1} + (1 - p) c _ {1 0}\tag{1}
$$

The expected total cost is the sum of the investment cost and the expected classification cost. In this case, the investment cost is 0, because no investment occurs. For the same reason, we calculate the expected classification cost using the cost matrix C in Table 2, and the expected classification cost is $p c _ { 1 1 } + ( 1 - p ) c _ { 1 0 } .$

(ii) If the investment decision is “no investment” and the instance is classified as class 0, the expected total cost $C _ { 2 }$ is

$$
C _ {2} = p c _ {0 1} + (1 - p) c _ {0 0}\tag{2}
$$

Likewise, the investment cost is 0, because no investment is made. Using the cost matrix C in Table 2, we compute the expected classification cost as $p c _ { 0 1 } + ( 1 - p ) c _ { 0 0 } .$

(iii) If the investment decision is “investment” and the instance is classified as class 1, the expected total cost $C _ { 3 }$ is

$$
\begin{array}{l} C _ {3} = V + p c _ {1 1} (1 - p _ {1 1}) + p \overline {{c}} _ {1 1} p _ {1 1} + \\ (1 - p) c _ {1 0} (1 - p _ {1 0}) + (1 - p) \overline {{c}} _ {1 0} p _ {1 0} \end{array}\tag{3}
$$

and the investment cost is V, because an investment has been made. The instance has a probability p of actually belonging to class 1 and is classified as class 1, so the expected classification cost becomes

Table 2. Classification Cost Matrix C

<table><tr><td></td><td>Actually Belonging to Class 0</td><td>Actually Belonging to Class 1</td></tr><tr><td>Classifying as Class 0</td><td> $C_{00}$ </td><td> $C_{01}$ </td></tr><tr><td>Classifying as Class 1</td><td> $C_{10}$ </td><td> $C_{11}$ </td></tr></table>

Table 3. New Classification Cost Matrix C¯

<table><tr><td></td><td>Actually Belonging to Class 0</td><td>Actually Belonging to Class 1</td></tr><tr><td>Classifying as Class 0</td><td> $\overline{c}_{00}$ </td><td> $\overline{c}_{01}$ </td></tr><tr><td>Classifying as Class 1</td><td> $\overline{c}_{10}$ </td><td> $\overline{c}_{11}$ </td></tr></table>

<table><tr><td colspan="4">Table 4. Probability  $p_{ij}$  of Cost Change Due to an Investment</td></tr><tr><td>Probability of Changing from  $c_{00}$  to  $\overline{c}_{00}$ </td><td>Probability of Changing from  $c_{01}$  to  $\overline{c}_{01}$ </td><td>Probability of Changing from  $c_{10}$  to  $\overline{c}_{10}$ </td><td>Probability of Changing from  $c_{11}$  to  $\overline{c}_{11}$ </td></tr><tr><td> $p_{00}$ </td><td> $p_{01}$ </td><td> $p_{10}$ </td><td> $p_{11}$ </td></tr></table>

$\int p c _ { 1 1 } + \big ( 1 - p \big ) c _ { 1 0 }$ if using cost matrix C in Table 2 $\Big ) p \overline { { c } } _ { 1 1 } + \big ( 1 - p \big ) \overline { { c } } _ { 1 0 }$ if using cost matrix $\bar { c }$ in Table 3

As we show in Table $^ { 4 , }$ with an investment, there is a probability of $\dot { p } _ { 1 1 }$ that $c _ { 1 1 }$ changes to $\overline { { c } } _ { 1 1 }$ and a probability of $( 1 ~ - ~ p _ { 1 1 } )$ that $c _ { 1 1 }$ remains intact. Also, there is a probability $\mathrm { o f } p _ { 1 0 }$ that $c _ { 1 0 }$ changes to $\overline { { c } } _ { 1 0 }$ and a probability of $\left( 1 - p _ { 1 0 } \right)$ that $c _ { 1 0 }$ remains the same. Thus, the expected classification cost becomes

$$
\begin{array}{l} p c _ {1 1} \left(1 - p _ {1 1}\right) + p \overline {{c}} _ {1 1} p _ {1 1} + \\ \left(1 - p\right) c _ {1 0} \left(1 - p _ {1 0}\right) + \left(1 - p\right) \overline {{c}} _ {1 0} p _ {1 0} \end{array}
$$

(iv) If the investment decision is “investment” and the instance is classified as class 0, the expected total cost $C _ { 4 }$ is calculated as

$$
\begin{array}{l} C _ {4} = V + p c _ {0 1} \left(1 - p _ {0 1}\right) + p \overline {{c}} _ {0 1} p _ {0 1} + \\ \left(1 - p\right) c _ {0 0} \left(1 - p _ {0 0}\right) + \left(1 - p\right) \overline {{c}} _ {0 0} p _ {0 0} \end{array}\tag{4}
$$

The investment is made, and the investment cost V is included in Equation (4). Because the instance has probability $p$ of actually belonging to class 1 but is classified as class 0, the expected classification cost becomes

$$
\left\{ \begin{array}{l l} p c _ {0 1} + (1 - p) c _ {0 0} & \text { if   using   cost   matrix } C \text { in   Table2 } \\ p \overline {{c}} _ {0 1} + (1 - p) \overline {{c}} _ {0 0} & \text { if   using   cost   matrix } \overline {{C}} \text { in   Table3 } \end{array} \right.
$$

With the investment, as indicated in Table $^ { 4 , }$ there is a probability of $\dot { \boldsymbol { p } } _ { 0 1 }$ that $c _ { 0 1 }$ changes to $c _ { 0 1 }$ and a probability of $\left( 1 - p _ { 0 1 } \right)$ that $c _ { 0 1 }$ remains the same. Also, there is a probability of ${ \dot { p } } _ { 0 0 }$ that $c _ { 0 0 }$ changes to $\overline { { c } } _ { 0 0 }$ and a probability of $( 1 - p _ { 0 0 } )$ that $c _ { 0 1 }$ remains unchanged. Therefore, the expected classification cost becomes

$$
\begin{array}{r l} p c _ {0 1} (1 - p _ {0 1}) + p \overline {{{c}}} _ {0 1} p _ {0 1} & + (1 - p) c _ {0 0} (1 - p _ {0 0}) \\ & + (1 - p) \overline {{{c}}} _ {0 0} p _ {0 0} \end{array}
$$

The optimal combination of investment and classification decisions incurs the least cost among $C _ { 1 } , C _ { 2 } , C _ { 3 } ,$ and $C _ { 4 } .$ Therefore, in Lemmas 1–4, we derive conditions for the optimal combination by comparing $C _ { 1 } , C _ { 2 } , C _ { 3 } ,$ and $C _ { 4 } .$ . In the following lemmas, we set $T _ { 0 } = c _ { 1 0 } - c _ { 0 0 } , \overline { { T } } _ { 0 } = \overline { { c } } _ { 1 0 } - \overline { { c } } _ { 0 0 } , T _ { 1 } = c _ { 0 1 }$ $- c _ { 1 1 } , \overline { { T } } _ { 1 } = \overline { { c } } _ { 0 1 } - \overline { { c } } _ { 1 1 } , D _ { 0 0 } = p _ { 0 0 } ( c _ { 0 0 } - \overline { { c } } _ { 0 0 } ) , D _ { 0 1 } = p _ { 0 1 } ( c _ { 0 1 } - \overline { { c } } _ { 0 1 } )$ $D _ { 1 0 } = p _ { 1 0 } ( c _ { 1 0 } - \overline { { c } } _ { 1 0 } )$ , and $D _ { 1 1 } = p _ { 1 1 } ( c _ { 1 1 } - \overline { { c } } _ { 1 1 } ) .$

Lemma 1. For an unclassified instance with probability p of belonging to class 1, it is optimal to invest and classify the instance as class 1 if Conditions (5) and (6) are satisfied:

$$
\left\{ \begin{array}{l l} p \geq \max \left(\frac {V - D _ {1 0}}{D _ {1 1} - D _ {1 0}}, \frac {V + T _ {0} - D _ {1 0}}{D _ {1 1} - D _ {1 0} + T _ {0} + T _ {1}}\right) & \text {if} D _ {1 1} > D _ {1 0} \\ \frac {V + T _ {0} - D _ {1 0}}{D _ {1 1} - D _ {1 0} + T _ {0} + T _ {1}} \leq p \leq \frac {D _ {1 0} - V}{D _ {1 0} - D _ {1 1}} & \text {if} D _ {1 0} - T _ {0} - T _ {1} <   D _ {1 1} <   D _ {1 0} \\ p \leq \min \left(\frac {D _ {1 0} - V}{D _ {1 0} - D _ {1 1}}, \frac {D _ {1 0} - V - T _ {0}}{D _ {1 0} - D _ {1 1} - T _ {0} - T _ {1}}\right) & \text {if} D _ {1 1} <   D _ {1 0} - T _ {0} - T _ {1} \end{array} \right.\tag{5}
$$

$$
\left\{ \begin{array}{l l} p \geq \frac {D _ {0 0} + T _ {0} - D _ {1 0}}{D _ {1 1} - D _ {1 0} - D _ {0 1} + D _ {0 0} + T _ {0} + T _ {1}} & \text { if } D _ {0 0} + D _ {1 1} + T _ {0} + T _ {1} > D _ {1 0} + D _ {0 1} \\ p \leq \frac {D _ {1 0} - D _ {0 0} - T _ {0}}{D _ {1 0} + D _ {0 1} - D _ {1 1} - D _ {0 0} - T _ {0} - T _ {1}} & \text { if } D _ {0 0} + D _ {1 1} + T _ {0} + T _ {1} <   D _ {1 0} + D _ {0 1} \end{array} \right.\tag{6}
$$

Proof: See Appendix A1.

Lemma 2. For an unclassified instance with probability p of belonging to class 1, it is optimal to invest and classify the instance as class 0 if Conditions (7) and (8) are satisfied:

$$
\left\{ \begin{array}{l l} p \geq \max \left(\frac {V - D _ {0 0} - T _ {0}}{D _ {0 1} - D _ {0 0} - T _ {0} - T _ {1}}, \frac {V - D _ {0 0}}{D _ {0 1} - D _ {0 0}}\right) & \text {if} D _ {0 1} > D _ {0 0} + T _ {0} + T _ {1} \\ \frac {V - D _ {0 0}}{D _ {0 1} - D _ {0 0}} \leq p \leq \frac {D _ {0 0} + T _ {0} - V}{D _ {0 0} + T _ {0} + T _ {1} - D _ {0 1}} & \text {if} D _ {0 0} <   D _ {0 1} <   D _ {0 0} + T _ {0} + T _ {1} \\ p \leq \min \left(\frac {D _ {0 0} + T _ {0} - V}{D _ {0 0} + T _ {0} + T _ {1} - D _ {0 1}}, \frac {D _ {0 0} - V}{D _ {0 0} - D _ {0 1}}\right) & \text {if} D _ {0 1} <   D _ {0 0} \end{array} \right.\tag{7}
$$

$$
\left\{ \begin{array}{l l} p \geq \frac {D _ {1 0} - T _ {0} - D _ {0 0}}{D _ {0 1} - D _ {0 0} - D _ {1 1} + D _ {1 0} - T _ {0} - T _ {1}} & \text { if } D _ {0 1} + D _ {1 0} > D _ {0 0} + D _ {1 1} + T _ {1} + T _ {0} \\ p \leq \frac {D _ {0 0} - D _ {1 0} + T _ {0}}{T _ {1} + T _ {0} - D _ {0 1} + D _ {0 0} + D _ {1 1} - D _ {1 0}} & \text { if } D _ {0 1} + D _ {1 0} <   D _ {0 0} + D _ {1 1} + T _ {1} + T _ {0} \end{array} \right.\tag{8}
$$

Proof: See Appendix A2.

Lemma 3. For an unclassified instance with probability p of belonging to class 1, it is optimal not to invest and classify the instance as class 1 if Conditions (9) and (10) are satisfied:

$$
\left\{ \begin{array}{l l} p \geq \frac {D _ {1 0} - V}{D _ {1 0} - D _ {1 1}} & \text { if } D _ {1 1} <   D _ {1 0} \\ p \leq \frac {V - D _ {1 0}}{D _ {1 1} - D _ {1 0}} & \text { if } D _ {1 1} > D _ {1 0} \end{array} \right.\tag{9}
$$

$$
\left\{ \begin{array}{l l} p \geq \max \left(\frac {T _ {0} + D _ {0 0} - V}{T _ {1} + T _ {0} + D _ {0 0} - D _ {0 1}}, \frac {T _ {0}}{T _ {1} + T _ {0}}\right) & \text { if } T _ {1} + T _ {0} + D _ {0 0} > D _ {0 1} \\ \frac {T _ {0}}{T _ {1} + T _ {0}} \leq p \leq \frac {V - T _ {0} - D _ {0 0}}{D _ {0 1} - T _ {1} - D _ {0 0} - T _ {0}} & \text { if } T _ {1} + T _ {0} + D _ {0 0} <   D _ {0 1} \end{array} \right.\tag{10}
$$

Proof: See Appendix A3.

Lemma 4. For an unclassified instance with probability $p$ of belonging to class 1, it is optimal not to invest and classify the instance as class 0 if Conditions (11) and (12) are satisfied:

$$
\left\{ \begin{array}{l l} p \leq \min \left(\frac {T _ {0} + V - D _ {1 0}}{T _ {0} + T _ {1} + D _ {1 1} - D _ {1 0}}, \frac {T _ {0}}{T _ {1} + T _ {0}}\right) & \text { if } T _ {0} + T _ {1} + D _ {1 1} > D _ {1 0} \\ \frac {D _ {1 0} - T _ {0} - V}{D _ {1 0} - T _ {0} - T _ {1} - D _ {1 1}} \leq p \leq \frac {T _ {0}}{T _ {1} + T _ {0}} & \text { if } T _ {0} + T _ {1} + D _ {1 1} <   D _ {1 0} \end{array} \right.\tag{11}
$$

$$
\left\{ \begin{array}{l l} p \geq \frac {D _ {0 0} - V}{D _ {0 0} - D _ {0 1}} & \text { if } D _ {0 1} <   D _ {0 0} \\ p \leq \frac {V - D _ {0 0}}{D _ {0 1} - D _ {0 0}} & \text { if } D _ {0 1} > D _ {0 0} \end{array} \right.\tag{12}
$$

Proof: See Appendix A4.

Building on Lemmas 1–4, we propose the investment-adjusted cost-sensitive learning (ICSL) method. As we illustrate in Figure 1, this method first employs a classification method, such as decision tree or naïve Bayes, to learn a classification model from training data T, then uses the learned model to estimate the probability p that an unclassified instance belongs to class 1. Next, the proposed method makes the investment and classification decisions for the unclassified instance according to Lemmas 1–4.

Having introduced the ICSL method, we characterize it in relation to existing cost-sensitive learning methods. The ICSL method yields the minimum cost among $C _ { 1 } , C _ { 2 } , C _ { 3 } ,$ and $C _ { 4 } ,$ or min $( C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } ) \mathrm { ; }$ ; existing cost-sensitive learning methods instead return the minimum cost between $C _ { 1 }$ and $C _ { 2 } ,$ or min( $C _ { 1 }$ $C _ { 2 } )$ , because they consider the cost matrix C only, without involving any investment decision (Elkan 2001; Jiang et al. 2014; Qiu et al. 2015). Thus, the proposed method should outperform existing cost-sensitive learning methods; that is, min $( C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } ) < \mathrm { m i n } ( C _ { 1 } , C _ { 2 } )$ when min( $C _ { 3 } , C _ { 4 } ) < \mathrm { m i n } ( C _ { 1 } ,$ $C _ { 2 } )$ . At a minimum, our method should be as good as existing methods, or min $C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } ) = \operatorname* { m i n } ( C _ { 1 } , C _ { 2 } )$ when $\operatorname* { m i n } ( C _ { 3 } ,$ $C _ { 4 } ) \ \geq \ \operatorname* { m i n } ( C _ { 1 } , C _ { 2 } ) . ^ 6$ We characterize the advantage of our proposed method over existing cost-sensitive learning methods as follows:

Proposition 1. When min $( C _ { 3 } , C _ { 4 } ) < \operatorname* { m i n } ( C _ { 1 } , C _ { 2 } )$ , the cost reduction by the proposed ICSL method, compared with existing cost-sensitive learning methods, min $( C _ { 1 } , C _ { 2 } ) { \mathrm { - m i n } } ( C _ { 1 }$ 2 $C _ { 2 } , C _ { 3 } , C _ { 4 } )$ , is greater if

(i) the investment amount V is smaller;

(ii) the classification cost reduction by the investment, $c _ { i j } - { \overline { { c } } } _ { i j } ,$ is larger, $i , j \in \{ 0 , 1 \} ,$ ; or

(iii) the probability $p _ { i j }$ of classification cost reduction by the investment is higher, $i , j \in \{ 0 , 1 \}$

Proof: See Appendix B.

According to Proposition 1, the proposed method is parti cularly advantageous and useful when the cost of an investment is reasonably small but the investment can significantly reduce the classification costs from $c _ { i j }$ to $\overline { { c } } _ { i j }$ with high probabilities, $i , j \in \{ 0 , 1 \}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ICSL (T, C,  $\bar{C}$ , V,  $p_{ij}$ )
T: training data
C,  $\bar{C}$ : cost matrixes shown in Tables 2 and 3
V: investment amount
 $p_{ij}$ : probability of classification cost change due to an investment, i, j ∈ {0, 1}

Learn a classification model by applying a classification method to T.
For each unclassified instance
    Use the learned classification model to estimate its probability p of belonging to class 1.
    Make the investment and classification decisions for the instance according to Lemmas 1–4.
End for

Figure 1. ICSL Method
</div>

## Empirical Evaluation

We empirically evaluated the proposed method with two realworld clinical data sets: one consisting of 1,122 mechanical ventilation cases and another comprising 102,294 breast cancer cases. We report the evaluation results from the mechanical ventilation data in this section, then summarize the results from the breast cancer data, which are qualitatively similar, in Appendix D. Here we describe our data and parameter calibrations, detail the benchmark methods and experimental procedure, and report the evaluation results for the mechanical ventilation data.

## Data and Parameter Calibrations

Mechanical ventilation is an invasive intervention commonly used in the intensive care unit (ICU) to assist patients respiration. According to Carson et al. (2006) and Wunsch et al. (2010), expenditures on mechanical ventilation in the United States, mainly for treating ventilation-related complications, have increased substantially, amounting to approximately \$31.39 billion in 2014. A common but critical clinical decision is whether a patient should be removed from mechanical ventilation and depend on his or her own respiration for breathing. By making this decision correctly, health care providers can greatly mitigate ventilation-related complications and reduce patient care costs (Boles et al. 2007). In our empirical evaluation, we used 1,122 mechanical ventilation cases, collected from a major tertiary medical center located in southern Taiwan, to illustrate the prescriptive performance of the proposed method, compared with several prevalent methods.<sup>7</sup> As we summarize in Table 5, each case is described by 17 attributes that could affect the physician’s ventilation removal decision and a class label attribute that indicates whether a patient actually should be removed from ventilation.<sup>8</sup>

We calibrated parameters that were essential for our empirical evaluation. Table 6 lists the classification costs for mechanical ventilation removal. With a \$1,636 investment in using advanced ventilation, the classification costs in Table 6 change to the new classification costs in Table 7, with the probabilities listed in Table 8. We summarize the parameter calibration details in Appendix C.

## Benchmark Methods and Experimental Procedure

As described, existing prescriptive analytics methods for CDM primarily rely on cost-sensitive learning that can be categorized as threshold moving, distribution altering, or test cost-sensitive learning. Test cost-sensitive learning targets attribute costs, or the cost of obtaining attribute values (Ling et al. 2006; Turney 1995; Weiss et al. 2013); it is not relevant to the investment-adjusted cost-sensitive learning problem, which involves no attribute costs. Therefore, we only consider threshold moving and distribution altering methods as benchmarks. The classical threshold moving method by Elkan (2001) is effective for cost-sensitive learning (Zhou and Liu 2006); applied to our focal problem, we can calculate a cost-sensitive threshold $\begin{array} { r } { t h r = \frac { c _ { 1 0 } - c _ { 0 0 } } { c _ { 1 0 } + c _ { 0 1 } - c _ { 0 0 } - c _ { 1 1 } } } \end{array}$ , where $c _ { i j }$ is a classification cost in the cost matrix C in Table $6 , i , j \in \{ 0 , 1 \}$ A patient is then classified as “not removing” $\mathrm { i f } p < t h r$ or as “removing” if p \$ thr, where p denotes the probability that the patient should be removed from ventilation. In general, distribution altering can be achieved with sampling (Chawla et al. 2002), instance weighting (Zhao 2008), or MetaCost (Domingos 1999). We compare the proposed method with synthetic minority oversampling (SMOTE; Chawla et al. 2002), a prevalent sampling method that is frequently included as a benchmark in previous cost-sensitive learning studies (e.g., Zhou and Liu 2006). We include a salient instance weighting method, implemented with a previously suggested weighting scheme (Jiang et al. 2014; Ting 2002; Zhao 2008). MetaCost is another benchmark; we follow Domingos (1999) to implement it. Because existing costsensitive learning methods do not involve investment decisions, benchmark methods note no investment costs and rely on the cost matrix C to make classification decisions. Table 9 summarizes these comparative methods.

Table 5. List of Attributes Considered for Mechanical Ventilation Removal Decision

<table><tr><td>Attribute</td><td>Attribute Type</td><td>Description</td></tr><tr><td>Gender</td><td>Nominal</td><td>Patient&#x27;s gender: male or female</td></tr><tr><td>Age</td><td>Numeric</td><td>Patient&#x27;s age</td></tr><tr><td>BH</td><td>Numeric</td><td>Patient&#x27;s height</td></tr><tr><td>BW</td><td>Numeric</td><td>Patient&#x27;s weight</td></tr><tr><td>BMI</td><td>Numeric</td><td>Patient&#x27;s body mass index</td></tr><tr><td>Diagnosis</td><td>Nominal</td><td>Patient&#x27;s diagnosis, such as lung disease or heart disease</td></tr><tr><td>ICU days</td><td>Numeric</td><td>Length of stay in ICU (in days)</td></tr><tr><td>Ventilation hours</td><td>Numeric</td><td>Length of using mechanical ventilation (in hours)</td></tr><tr><td>APACHE II</td><td>Numeric</td><td>Patient&#x27;s score in Acute Physiology and Chronic Health Evaluation II system</td></tr><tr><td>GCS</td><td>Numeric</td><td>Patient&#x27;s score in Glasgow Coma Scale Assessment</td></tr><tr><td>Cough function</td><td>Nominal</td><td>Whether a patient has cough: Yes or No</td></tr><tr><td>Sedation</td><td>Nominal</td><td>Whether a patient uses sedatives: Yes or No</td></tr><tr><td>PEEP</td><td>Numeric</td><td>Patient&#x27;s positive end-expiratory pressure in lung</td></tr><tr><td>Mode</td><td>Nominal</td><td>Patient&#x27;s ventilation mode: PSP (pressure support pressure) or PSV (pressure support ventilation)</td></tr><tr><td>Mg</td><td>Numeric</td><td>Content of Mg in patient&#x27;s blood</td></tr><tr><td>Restless</td><td>Nominal</td><td>Whether patient is restless: Yes or No</td></tr><tr><td>Cold sweats</td><td>Nominal</td><td>Whether patient has cold sweats: Yes or No</td></tr><tr><td>Liberation</td><td>Nominal</td><td>Whether patient should be removed from mechanical ventilation: Yes or No</td></tr></table>

<table><tr><td colspan="3">Table 6. Classification Cost Matrix C for Mechanical Ventilation Removal</td></tr><tr><td></td><td>Actually Not Removing</td><td>Actually Removing</td></tr><tr><td>Classifying as Not Removing</td><td> $c_{00} = \$9,760$ </td><td> $c_{01} = \$16,549$ </td></tr><tr><td>Classifying as Removing</td><td> $c_{10} = \$12,476$ </td><td> $c_{11} = \$0$ </td></tr></table>

<table><tr><td colspan="3">Table 7. New Classification Cost Matrix  $\overline{C}$  for Mechanical Ventilation Removal</td></tr><tr><td></td><td>Actually Not Removing</td><td>Actually Removing</td></tr><tr><td>Classifying as Not Removing</td><td> $\overline{c}_{00} = \$3,030$ </td><td> $\overline{c}_{01} = \$9,819$ </td></tr><tr><td>Classifying as Removing</td><td> $\overline{c}_{10} = \$5,746$ </td><td> $\overline{c}_{11} = \$0$ </td></tr></table>

<table><tr><td colspan="4">Table 8. Probability  $p_{ij}$  of Cost Change Due to an Investment (Mechanical Ventilation Removal)</td></tr><tr><td>Probability of Changing from  $c_{00}$  to  $\overline{c}_{00}$ </td><td>Probability of Changing from  $c_{01}$  to  $\overline{c}_{01}$ </td><td>Probability of Changing from  $c_{10}$  to  $\overline{c}_{10}$ </td><td>Probability of Changing from  $c_{11}$  to  $\overline{c}_{11}$ </td></tr><tr><td> $p_{00}=0.875$ </td><td> $p_{01}=0.875$ </td><td> $p_{10}=0.875$ </td><td> $p_{11}=0$ </td></tr></table>

Table 9. Summary of Comparison Methods

<table><tr><td>Method</td><td>Abbreviation</td><td>Role in our Evaluation</td><td>Cost Considered for Decision Making</td></tr><tr><td>Investment-adjusted cost-sensitive learning</td><td>ICSL</td><td>Proposed Method</td><td>Investment Cost and Classification Cost</td></tr><tr><td>Threshold moving</td><td>THR</td><td>Benchmark</td><td>Classification Cost</td></tr><tr><td>Synthetic minority over-sampling</td><td>SMOTE</td><td>Benchmark</td><td>Classification Cost</td></tr><tr><td>Instance weighting</td><td>IW</td><td>Benchmark</td><td>Classification Cost</td></tr><tr><td>MetaCost</td><td>MC</td><td>Benchmark</td><td>Classification Cost</td></tr></table>

Using the mechanical ventilation data set, the classification costs and probabilities of cost changes from Tables 6–8, and the investment amount (V = \$1,636), we comparatively examine the proposed method and benchmark methods. First, we randomly select two-thirds of the cases in the data set as training data and use the remainder as test data. Second, the proposed method learns from the training data to make the investment and classification decisions for each test case (i.e., cases in the test data); each benchmark method learns from the training data to make the classification decision for each test case.<sup>9</sup> Third, we calculate the cost incurred by each method. For a benchmark method, the cost is the sum of the cost of classifying each test case, according to the cost matrix C in Table 6. For example, the cost of classifying a test case as “not removing” when it actually is “removing” is \$16,549. The cost incurred by our method is the sum of the investment and classification costs of each test case. For example, if our method decides not to invest and makes a classification decision for the case, the investment cost is \$0, and the classification cost is determined according to the classification cost matrix C in Table 6. If our method instead decides to invest and makes a classification decision for the case, the investment cost becomes \$1,636, and the classification cost is obtained from the new classification cost matrix C¯ (Table 7) with probability $p _ { i j }$ (Table 8) or the classification cost matrix C (Table 6) with probability $1 - p _ { i j } .$ 10

## Experimental Results and Analyses

With this procedure, we conducted experiments to evaluate the effectiveness of our method, in comparison with that of each benchmark method. In addition, we examined the robustness of the performance improvements achieved.

## Effectiveness Analysis

We performed 100 experiments to assess the effectiveness of our method. To ensure an equal basis for comparison, in all investigated methods, we used the same classification algorithm to estimate the probability that a patient should be removed from ventilation. Specifically, we estimated using C4.5, a prevalent decision tree learning algorithm (Quinlan 1993; Zhao and Ram 2004), coupled with m-estimation (Cussens 1993).<sup>11</sup> Figure 2 plots the costs incurred by the proposed and each benchmark method, across 100 experiments; as shown, these costs are consistently lower for our method than for any benchmark. We also applied a Wilcoxon signed-rank test (Snedecor and Cochran 1989) to the cost data in Figure 2, which revealed that the proposed method significantly outperformed each benchmark method, at $p < 0 . 0 0 1$ As we summarize in Table 10, the cost of our method, averaged across 100 experiments, is \$255,987, whereas that of IW, the best-performing benchmark, is \$429,790. On average, the cost of our method is 40.44% lower than that of IW and 42.04% lower than that of THR (worst-performing benchmark).<sup>12</sup>

![](/api/attachments/FTPRRK75/fulltext/images/8210b27f12514675cca654daa4b7c622736fa5091d6f96911dc718684fb46852.jpg)  
Figure 2. Cost Incurred by Each Investigated Method, across 100 Experiments

Table 10. Average Cost Incurred: Our Method Versus Benchmark Methods

<table><tr><td>Method</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>ICSL (Our Method)</td><td>$255,987 (±$42,989)</td><td></td></tr><tr><td>THR</td><td>$441,903 (±$69,227)</td><td>42.04%</td></tr><tr><td>SMOTE</td><td>$435,899 (±$65,844)</td><td>41.14%</td></tr><tr><td>IW</td><td>$429,790 (±$66,068)</td><td>40.44%</td></tr><tr><td>MC</td><td>$434,924 (±$66,734)</td><td>41.13%</td></tr></table>

## Robustness Analysis

We examined the robustness of our method’s performance in several different scenarios. First, though we set the classification costs, probabilities of cost change, and investment amount by reviewing relevant literature and consulting with experienced physicians, it is important to confirm the robustness of our findings, using different classification costs, probabilities of cost change, or investment amount. Second, the proposed and benchmark methods used a decision tree algorithm to estimate the probability p that a patient should be removed from ventilation, so we reexamined their performance according to other classification algorithms (such as support vector machine) that also can estimate $p .$

Robustness Analysis in Scenario I: We considered the cost estimates over the range –40% to +40% by altering the classification costs in Table 6 from $c _ { i j } \times 6 0 \%$ to $c _ { i j } \times$ 140% for all $i , j \in \{ 0 , 1 \}$ , in increments of 10%.<sup>13</sup> We then conducted 100 experiments to compare the performance of our method and those of the benchmarks for each cost alteration. Table 11 summarizes the average costs; again, our proposed method substantially outperformed each benchmark method, and the average cost reduction increased with the classification costs $c _ { i j } ,$ in line with Proposition 1. For example, the average cost reduction by our method, compared with IW (best-performing benchmark), improved from 10.83% to 51.63% as the classification costs increased from $c _ { i j } \times 6 0 \% \mathrm { ~ t o ~ } c _ { i j } \times 1 4 0 \%$ . The Wilcoxon signed-rank test results reveal that the proposed method consistently and significantly outperformed every benchmark method $( p < 0 . 0 0 1 )$ ) across all cost alterations under analysis.

Table 11. Average Cost of Respective Methods across Different Classification Costs

<table><tr><td rowspan="2"></td><td>ICSL(Our Method)</td><td colspan="2">THR</td><td colspan="2">SMOTE</td><td colspan="2">IW</td><td colspan="2">MC</td></tr><tr><td>Cost: Average(± SD)</td><td>Cost:Average (±SD)</td><td>AverageCostReductionby ICSL</td><td>Cost:Average(± SD)</td><td>AverageCostReductionby ICSL</td><td>Cost:Average(± SD)</td><td>AverageCostReductionby ICSL</td><td>Cost:Average(± SD)</td><td>AverageCostReductionby ICSL</td></tr><tr><td> $c_{ij} \times 60\%$ </td><td>$ 227,259.97(±$30,244.24)</td><td>$ 263,452(±$35,122)</td><td>13.71%</td><td>$ 254,937(±$29,584)</td><td>10.86%</td><td>$ 254,786(±$30,345)</td><td>10.83%</td><td>$ 261,299(±$33,439)</td><td>12.93%</td></tr><tr><td> $c_{ij} \times 70\%$ </td><td>$ 225,329.56(±$27,484.19)</td><td>$ 299,247(±$34,951)</td><td>24.65%</td><td>$ 293,943(±$33,019)</td><td>23.19%</td><td>$ 290,378(±$34,244)</td><td>22.36%</td><td>$ 294,782(±$34,441)</td><td>23.48%</td></tr><tr><td> $c_{ij} \times 80\%$ </td><td>$ 240,324.70(±$40,981.73)</td><td>$ 354,870(±$54,159)</td><td>32.38%</td><td>$ 353,844(±$48,605)</td><td>32.13%</td><td>$ 346,030(±$51,519)</td><td>30.65%</td><td>$ 350,411(±$53,302)</td><td>31.43%</td></tr><tr><td> $c_{ij} \times 90\%$ </td><td>$ 238,043.40(±$37,426.11)</td><td>$ 384,861(±$60,324)</td><td>38.08%</td><td>$ 381,927(±$57,559)</td><td>37.45%</td><td>$ 370,826(±$51,645)</td><td>35.90%</td><td>$ 377,511(±$55,864)</td><td>36.91%</td></tr><tr><td> $c_{ij}$ </td><td>$255,987.12(±$42,989.37)</td><td>$441,903(±$69,227)</td><td>42.04%</td><td>$435,899(±$65,844)</td><td>41.14%</td><td>$429,790(±$66,068)</td><td>40.44%</td><td>$434,924(±$66,734)</td><td>41.13%</td></tr><tr><td> $c_{ij} \times 110\%$ </td><td>$ 265,925.40(±$44,734.20)</td><td>$ 487,853(±$69,325)</td><td>45.57%</td><td>$ 476,194(±$67,678)</td><td>44.13%</td><td>$ 469,276(±$64,633)</td><td>43.41%</td><td>$ 476,033(±$65,171)</td><td>44.21%</td></tr><tr><td> $c_{ij} \times 120\%$ </td><td>$ 271,100.84(±$45,341.69)</td><td>$ 524,685(±$65,615)</td><td>48.47%</td><td>$ 508,468(±$61,219)</td><td>46.72%</td><td>$ 506,599(±$63,404)</td><td>46.58%</td><td>$ 515,388(±$68,248)</td><td>47.44%</td></tr><tr><td> $c_{ij} \times 130\%$ </td><td>$ 276,093.94(±$35,623.07)</td><td>$ 575,280(±$64,281)</td><td>51.97%</td><td>$ 562,644(±$61,330)</td><td>50.78%</td><td>$ 553,949(±$60,909)</td><td>50.15%</td><td>$ 558,904.42(±$63,394)</td><td>50.55%</td></tr><tr><td> $c_{ij} \times 140\%$ </td><td>$ 279,792.10(±$38,431.92)</td><td>$ 596,035(±$75,270)</td><td>53.03%</td><td>$ 586,878(±$70,891)</td><td>52.25%</td><td>$ 578,268(±$68,475)</td><td>51.63%</td><td>$ 582,677(±$70,580)</td><td>51.91%</td></tr></table>

Similarly, we altered the probabilities of the classification cost change in Table 8 from $p _ { i j } \times 6 0 \%$ to $p _ { i j } \times 1 1 0 \%$ , in increments of $1 0 \% ,$ for all $i , j \in \{ 0 , 1 \}$ , and varied the investment amount from $V \times 6 0 \%$ to $V \times 1 4 0 \%$ in increments of $1 0 \% . ^ { 1 4 }$ We conducted 100 experiments to compare our method against the benchmarks for each probability alteration or investment amount variation and report the results in Tables 12 and 13. Again, the proposed method consistently and substantially outperformed all the benchmark methods, across all the investigated probability alterations or investment amounts. For example, the cost reduction attained with our method, relative to IW, improved from 17.12% to 47.34% as the probabilities of the cost change increased from $p _ { i j } \times 6 0 \%$ to $p _ { i j } \times 1 1 0 \%$ , and from 34.56% to 45.28% as the investment amount decreased from $V \times 1 4 0 \%$ to $V \times 6 0 \%$ . Overall, the cost reduction by the proposed method, relative to the benchmark methods, increases with the probabilities of cost changes and decreases with the investment amount, in line with Proposition 1. Furthermore, according to the Wilcoxon signed-rank test results, our method significantly outperformed all the benchmark methods $( p \textless 0 . 0 0 1 )$ , across all investigated probabilities or investment amounts.

Robustness Analysis in Scenario II: We also assessed the robustness of the comparative evaluation results by using other classification algorithms. That is, the proposed and benchmark methods could estimate the probability p that a patient should be removed from ventilation using classification algorithms such as logistic regression, support vector machine, and naïve Bayes. For each classification algorithm, we conducted 100 experiments to compare the performance of our method with those of the benchmarks. As we summarize in Tables 14–16, with each investigated classification algorithm, the cost of our method, averaged across 100 experiments, was substantially lower than that of any benchmark method. The Wilcoxon signed-rank test results show that our method consistently and significantly outperformed each benchmark method $( p < 0 . 0 0 1 )$ for each classification algorithm under evaluation.

Overall, the evaluation results reveal that the proposed method consistently and significantly outperforms all the benchmark methods, across various scenarios. The observed cost reductions by our method can be partially explained by its simultaneous consideration of the probabilistic, costsensitive, and investment-related characteristics of CDM, whereas existing methods overlook the investment-related characteristic. As a result, our proposed method is more effective for cost reduction in CDM and incurs lower costs than any benchmark methods.

Table 12. Average Cost of Respective Methods across Different Probabilities

<table><tr><td rowspan="2"></td><td>ICSL (Our Method)</td><td colspan="2">THR</td><td colspan="2">SMOTE</td><td colspan="2">IW</td><td colspan="2">MC</td></tr><tr><td>Cost: Average (± SD)</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td> $p_{ij} \times 60\%$ </td><td>$350,056(±$41,273)</td><td>$436,389(±$50,024)</td><td>19.77%</td><td>$422,173(±$40,365)</td><td>17.12%</td><td>$422,350(±$46,961)</td><td>17.12%</td><td>$428,108(±$48,200)</td><td>18.19%</td></tr><tr><td> $p_{ij} \times 70\%$ </td><td>$328,698(±$37,324)</td><td>$441,858(±$46,980)</td><td>25.62%</td><td>$438,316(±$51,853)</td><td>24.76%</td><td>$424,693(±$41,134)</td><td>22.55%</td><td>$433,981(±$49,192)</td><td>24.13%</td></tr><tr><td> $p_{ij} \times 80\%$ </td><td>$304,994(±$42,447)</td><td>$439,232(±$57,833)</td><td>30.57%</td><td>$433,087(±$59,098)</td><td>29.41%</td><td>$423,810(±$54,379)</td><td>27.99%</td><td>$432,966(±$58,331)</td><td>29.41%</td></tr><tr><td> $p_{ij} \times 90\%$ </td><td>$282,745(±$46,419)</td><td>$441,031(±$62,858)</td><td>36.00%</td><td>$430,870(±$57,717)</td><td>34.42%</td><td>$428,632(±$57,519)</td><td>34.20%</td><td>$434,690(±$61,516)</td><td>35.00%</td></tr><tr><td> $p_{ij}$ </td><td>$255,987(±$42,989)</td><td>$441,903(±$69,227)</td><td>42.04%</td><td>$435,899(±$65,844)</td><td>41.14%</td><td>$429,790(±$66,068)</td><td>40.44%</td><td>$434,924(±$66,734)</td><td>41.13%</td></tr><tr><td> $p_{ij} \times 110\%$ </td><td>$221,389(±$32,520)</td><td>$433,349(±$59,801)</td><td>48.88%</td><td>$426,498(±$62,039)</td><td>47.84%</td><td>$420,411(±$58,055)</td><td>47.34%</td><td>$424,100(±$59,814)</td><td>47.75%</td></tr></table>

Table 13. Average Cost of Respective Methods across Different Investment Amount

<table><tr><td rowspan="2"></td><td>ICSL (Our Method)</td><td colspan="2">THR</td><td colspan="2">SMOTE</td><td colspan="2">IW</td><td colspan="2">MC</td></tr><tr><td>Cost: Average (± SD)</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>V × 60%</td><td>$ 231,007(±$37,805)</td><td>$ 432,269(±$51,061)</td><td>46.64%</td><td>$ 427,389(±$52,495)</td><td>45.88%</td><td>$ 421,243(±$47,955)</td><td>45.28%</td><td>$ 431,436(±$52,921)</td><td>46.41%</td></tr><tr><td>V × 70%</td><td>$ 241,515(±$43,964)</td><td>$ 442,041(±$64,397)</td><td>45.51%</td><td>$ 431,653(±$53,487)</td><td>44.23%</td><td>$ 432,709(±$59,453)</td><td>44.34%</td><td>$ 437,172(±$60,449)</td><td>44.90%</td></tr><tr><td>V × 80%</td><td>$ 237,165(±$38,264)</td><td>$ 428,272(±$61,164)</td><td>44.68%</td><td>$ 429,169(±$58,247)</td><td>44.75%</td><td>$ 419,833(±$57,501)</td><td>43.60%</td><td>$ 424,035(±$59,866)</td><td>44.01%</td></tr><tr><td>V × 90%</td><td>$ 242,504(±$41,191)</td><td>$ 432,748(±$61,203)</td><td>44.09%</td><td>$ 427,187(±$52,050)</td><td>43.41%</td><td>$ 421,639(±$56,718)</td><td>42.58%</td><td>$ 425,525(±$58,479)</td><td>43.15%</td></tr><tr><td>V</td><td>$255,987(±$42,989)</td><td>$441,903(±$69,227)</td><td>42.04%</td><td>$435,899(±$65,844)</td><td>41.14%</td><td>$429,790(±$66,068)</td><td>40.44%</td><td>$434,924(±$66,734)</td><td>41.13%</td></tr><tr><td>V × 110%</td><td>$ 262,391(±$33,331)</td><td>$ 439,853(±$52,105)</td><td>40.33%</td><td>$ 438,371(±$46,253)</td><td>39.95%</td><td>$ 428,214(±$44,681)</td><td>38.78%</td><td>$ 436,585(±$51,505)</td><td>39.86%</td></tr><tr><td>V × 120%</td><td>$ 275,580(±$45,026)</td><td>$ 450,043(±$66,066)</td><td>38.82%</td><td>$ 437,675(±$63,049)</td><td>36.96%</td><td>$ 431,465(±$54,804)</td><td>36.29%</td><td>$ 439,792(±$60,886)</td><td>37.38%</td></tr><tr><td>V × 130%</td><td>$ 269,883(±$43,126)</td><td>$ 432,751(±$61,459)</td><td>37.69%</td><td>$ 426,434(±$69,739)</td><td>36.25%</td><td>$ 422,759(±$63,565)</td><td>36.07%</td><td>$ 422,717(±$60,077)</td><td>36.05%</td></tr><tr><td>V × 140%</td><td>$ 275,135(±$36,254)</td><td>$ 433,999(±$57,183)</td><td>36.51%</td><td>$ 421,774(±$50,832)</td><td>34.62%</td><td>$ 421,136(±$52,962)</td><td>34.56%</td><td>$ 422,720(±$51,052)</td><td>34.83%</td></tr></table>

<table><tr><td colspan="3">Table 14. Average Cost of Each Investigated Method (p Estimated with Logistic Regression)</td></tr><tr><td>Method</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>ICSL (Our Method)</td><td>$440,532 (±$61,510)</td><td></td></tr><tr><td>THR</td><td>$520,693 (±$66,868)</td><td>15.37%</td></tr><tr><td>SMOTE</td><td>$634,172 (±$85,979)</td><td>29.95%</td></tr><tr><td>IW</td><td>$565,667 (±$72,469)</td><td>22.11%</td></tr><tr><td>MC</td><td>$539,182 (±$70,793)</td><td>18.25%</td></tr><tr><td colspan="3">Table 15. Average Cost of Each Investigated Method (p Estimated with Support Vector Machine)</td></tr><tr><td>Method</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>ICSL (Our Method)</td><td>$415,647 (±$54,668)</td><td></td></tr><tr><td>THR</td><td>$503,859 (±$70,167)</td><td>17.34%</td></tr><tr><td>SMOTE</td><td>$704,839 (±$87,981)</td><td>40.61%</td></tr><tr><td>IW</td><td>$555,416 (±$71,709)</td><td>24.94%</td></tr><tr><td>MC</td><td>$529,880 (±$70,401)</td><td>21.33%</td></tr></table>

Table 16. Average Cost of Each Investigated Method (p Estimated with Naïve Bayes)

<table><tr><td>Method</td><td>Cost: Average (± SD)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>ICSL (Our Method)</td><td>$501,912 (±$61,495)</td><td></td></tr><tr><td>THR</td><td>$550,629 (±$88,048)</td><td>8.12%</td></tr><tr><td>SMOTE</td><td>$1,240,117 (±$119,745)</td><td>59.36%</td></tr><tr><td>IW</td><td>$816,913 (±$90,742)</td><td>38.21%</td></tr><tr><td>MC</td><td>$786,859 (±$97,728)</td><td>35.79%</td></tr></table>

## Discussion

Containing fast-growing costs is critical to the sustainability of health care services (Mango and Riefberg 2009), and prescriptive analytics for CDM can offer significant relevance and benefits (Manyika et al. 2011). From a research standpoint, prescriptive analytics in general and their support for CDM specifically represent high-impact areas in IS research (Chen et al. 2012; Goes 2015; Kohli and Tan 2016). As an illustrating example of such impacts, we develop a novel method to reduce health care costs. In light of the knowledge contribution framework of design science research (Gregor and Hevner 2013), our study contributes to extant literature in both problem formulation and solution development. We formulate a new cost-sensitive learning problem, distinctive in its consideration of the investment-related characteristic of CDM. We also develop a novel solution, the investmentadjusted cost-sensitive learning method, which takes the investment characteristic of CDM into account and considers classification costs as probabilistic, unlike prevalent costsensitive learning methods that regard them as deterministic. Furthermore, the proposed ICSL method integrates clinical (classification) and investment decisions to minimize the sum of classification and investment costs, unlike existing costsensitive learning methods that overlook the investment decision.

This study offers research implications for prescriptive analytics in general and their support for CDM in particular. First, our study indicates that continued research should approach prescriptive analytics problems by extending the costsensitive perspective that seeks to minimize expected costs. Second, we highlight the inherently probabilistic nature of prescriptive analytics problems that often involve different events and outcomes in the future. That is, future outcomes are probabilistic and the solutions to prescriptive analytics problems require accurate predictions of future outcomes. Third, we show that costs in prescriptive analytics problems can be altered probabilistically through an investment, reinforcing our claim that such problems should be regarded as probabilistic rather than deterministic. Then prescriptive analytics methods can encourage optimal decisions about a potential investment, in addition to offering classifications. Fourth, our problem formulation and method development should inform future research, by highlighting the value and feasibility of addressing probabilistic, cost-sensitive, investment-related characteristics of CDM simultaneously to improve cost effectiveness in health care. As a point of departure, this study encourages researchers to approach classification costs probabilistically, rather than deterministically, to better support CDM in health care and plausibly decisions in other contexts.

For health care practice, because we consider all three eminent characteristics of CDM, the proposed method better supports clinical decisions and could help contain health care costs more effectively than existing methods. As we demonstrate with the mechanical ventilation data set, our method reduces the costs associated with mechanical ventilation removal decisions substantially, compared with the bestperforming benchmarks. The U.S. expenditures on mechanical ventilation are substantial, for example reaching \$31.39 billion in 2014 (Carson et al. 2006; Wunsch et al. 2010), so the use of our proposed method could result in considerable cost reductions. As we detail in Appendix D, the use of our proposed method to support breast cancer diagnoses and decisions also can result in substantial cost reductions, compared with prevalent benchmark methods.

The proposed method arguably could be applied to other clinical decisions too. For example, diabetes is a common chronic disease, affecting approximately 366 million people worldwide, with projections that this number will increase to 552 million by 2030 (Whiting et al. 2011). Type 2 diabetes represents the most common form, accounting for 95% of all adult diabetes cases. Yet about 183 million patients are unaware of their disease, which causes serious diagnosis delays after its onset (Harris et al. 1992; Roche and Wang 2014) and significantly increases their risk of hyperglycemia, insulin resistance, low-grade inflammation, and accelerated atherogenesis (Schlienger 2013). These complications in turn can lead to cardio-cerebrovascular disease, renal disease, or diabetic foot (Schlienger 2013). According to the UK Prospective Diabetes Study Group (1998), intensive blood glucose control with sulphonylureas or insulin represents a promising investment for reducing the risk of renal disease, so to reduce clinical decision-making costs, physicians might apply our proposed method to predict (classify) whether a patient has Type 2 diabetes and determine whether to treat that patient with intensive blood glucose controls.

Overall, to apply the proposed method, physicians and health care organizations also need to estimate the probabilities of different outcomes (Bhugra 2008). Before reaching a diagnosis decision, physicians should consider the consequences of all plausible decisions, by answering several questions before applying our proposed method:

(1) What are plausible diagnosis decisions, according to the patient’s symptoms and laboratory results? For example, a patient’s symptoms might suggest two possible outcomes: benign versus malignant tumor.

(2) What is the probability of each decision outcome $( \mathrm { e . g . }$ 60% probability of benign, 40% probability of malignant)? Such probabilities could be assessed with machine learning algorithms such as decision trees, naïve Bayes, logistic regression, or support vector machines.

(3) What potential treatments are associated with each decision: surgery, chemotherapy, or other therapeutic interventions if the patient’s tumor is malignant?

(4) What are the consequences and complications likely result from a diagnosis decision?

(5) What are the estimated costs of these consequences and resulting complications? Physicians might obtain reasonable cost estimates from different sources, such as clinical literature and their health care organization’s proprietary systems.

(6) Are there measures or means available to mitigate the estimated costs? Equipped with clinical knowledge and personal experiences, physicians can evaluate potential measures to prevent specific complications or consequences. These measures and means are equivalent to an investment in our proposed method.

(7) What is the probability that the investment will be effective? It might fail to prevent foreseen consequences or complications effectively. Physicians and health care organizations can learn this probability from clinical literature reviews and their experiences and observations.

(8) What are the new estimations of the resulting costs associated with the complications and consequences after the investment? If the investment is successful, a patient can avoid some adverse consequences or complications.

Together, these questions can guide physicians and health care organizations in identifying decision outcomes; categorizing them into classes; deriving the probability $p$ that a unclassified instance belongs to class 1; calculating the classification costs $c _ { 0 0 } , c _ { 0 1 } , c _ { 1 0 } ,$ and $c _ { \mathrm { 1 1 } } .$ as well as the amount V of an investment; estimating the probability $p _ { i j }$ of a classification cost change due to the investment; and finally analyzing the new classification costs $\overline { { c } } _ { 1 0 } , \overline { { c } } _ { 0 0 } , \overline { { c } } _ { 0 1 } ,$ , and $\overline { { c } } _ { 1 1 } .$ . Our method is applicable to clinical decision-making tasks that fit our stated problem definition and scope. Taking the illustrating evaluation as an example, the proposed method cannot be utilized if patients are initially on advanced ventilation, because of the unavailability of the investment option.

We also expect that the proposed method might be applicable to important decisions in other domains, especially those with probabilistic, cost-sensitive, and investment-related characteristics. For example, our method could facilitate new product development (NPD) decisions, which tend to be risky and plagued by high failure rates (Ogawa and Piller 2006). To determine whether to proceed after the initial product design stage, the firm faces a probabilistic decision built on the estimated likelihood that the product will succeed in the market. Furthermore, NPD decisions are cost sensitive. If a firm erroneously classifies a subpar new product as a likely success, it will face substantial overstock costs; if it classifies a great new product as a failure, it suffers significant revenue losses. Finally, NPD decisions involve investments, such that a firm might invest in attractive incentives to get customers to co-design and preorder, which would reduce potential overstock costs (Ogawa and Piller 2006). Many real-world business decisions—loan approval decisions by financial institutions, offshore drilling decisions by petroleum companies, player drafting decisions by professional sports organizations—similarly have probabilistic, cost-sensitive, and investment-related characteristics and might benefit from our proposed method. For example, a financial institution could invest in additional in-depths background checks before approving a loan application, or a petroleum company could invest in advanced ocean bed explorations before deciding whether to proceed with offshore drilling operations.

## Conclusion

Effective prescriptive analytics for supporting CDM must address its probabilistic, cost-sensitive, and investment-related characteristics simultaneously. We formulate a new costsensitive learning problem that considers all these characteristics and propose a novel prescriptive analytics method to improve the cost effectiveness of CDM. Our method development relies on both prospect theory (Kahneman and Tversky 1979) and regret theory (Zeelenberg et al. 1996). The inputs include two sets of costs associated with clinical decisions, before and after an investment, and the probabilities of cost changes due to investments. Thus the proposed method can analyze the costs of different combinations of clinical and investment decisions and recommend optimal decisions to reduce total costs. Empirical evaluations with two real-world clinical data sets show that our method consistently and significantly outperforms several salient methods from previous research.

Our study also has several limitations that suggest the need for further research. First, we develop this method to support clinical decisions with two distinctive outcomes (e.g., removing or not removing a patient from mechanical ventilation). Many clinical decisions similarly involve dichotomous decision outcomes, but others have more than two decision outcomes. It is important to extend our method to accommodate such clinical decisions. Second, our study objective is to reduce costs for CDM, so our method development focuses only on cost factors, not other factors (e.g., patient risk) that also are essential to physicians’ clinical decision making. Our method could be extended to incorporate other considerations, such as pursuing minimal costs, subject to a constraint of maintaining patient risk below a particular threshold. Third, it would be interesting to adapt our method to support critical decisions in other domains, such as NPD. Continued studies could solve different, chal lenging, decision-making problems and produce new empirical evidence of the effectiveness of our method. Fourth, the ICLS problem might be solved by extending instance weighting methods (Ting 2002; Zhao 2008). However, traditional methods only consider one cost matrix and make classification decisions, whereas our focal problem involves two cost matrices and both classification and investment decisions. Direct applications of traditional instance weighting methods thus are not viable, but further research arguably might design novel instance weighting methods to handle two cost matrices and support both classification and investment decisions.

## References

Agarwal, R., and Dhar, V. 2014. “Big Data, Data Science, and Analytics: The Opportunity and Challenge for IS Research,” Information Systems Research (25:3), pp. 443-448.

Agarwal, R., Gao, G., DesRoches, C., and Jha, A. K. 2010. “Research Commentary—The Digital Transformation of Healthcare: Current Status and the Road Ahead,” Information Systems Research (21:4), pp. 796-809.

Angst, C. M., Agarwal, R., Sambamurthy, V., and Kelley, K. 2010. “Social Contagion and Information Technology Diffusion: the Adoption of Electronic Medical Records in US Hospitals,” Management Science (56:8), pp. 1219-1241.

Antonelli, M., Conti, G., Rocco, M., Bufi, M., De Blasi, R. A., Vivino, G., Gasparetto A., and Meduri, G. U. 1998. “A Comparison of Noninvasive Positive-Pressure Ventilation and Conventional Mechanical Ventilation in Patients with Acute Respiratory Failure,” New England Journal of Medicine (339:7), pp. 429-435.

Archer, D. F., Bernick, B., and Constantine, G. 2015. “Prevalence of Use and Cost of Compounded Menopausal Hormone Therapy,” Obstetrics and Gynecology (125, Suppl 1, 98S).

Areti, A., Yerra, V. G., Naidu, V. G. M., and Kumar, A. 2014. “Oxidative Stress and Nerve Damage: Role in Chemotherapy Induced Peripheral Neuropathy,” Redox Biology (2), pp. 289-295.

Aron, R., Dutta, S., Janakiraman, R., and Pathak, P. A. 2011. “The Impact of Automation of Systems on Medical Errors: Evidence from Field Research,” Information Systems Research (22:3), pp. 429-446.

Azoulay, E., Lemiale, V., Mokart, D., Pène, F., Kouatchet, A., Perez, P., and Darmon, M. 2014. “Acute Respiratory Distress Syndrome in Patients with Malignancies,” Intensive Care Medicine (40:8), pp. 1106-1114.

Bardhan, I., Ayabakan, S., Kirksey, K., and Zheng, E. 2014. “Value of Health Information Sharing in Reducing Healthcare Waste: An Analysis of Duplicate Testing across Hospitals,” in Proceedings of the 34<sup>th</sup> International Conference on Information Systems, Auckland, New Zealand (http://aisel.aisnet.org/ icis2014/proceedings/ISHealthcare/22/).

Bell, D. E. 1983. “Risk Premiums for Decision Regret,” Management Science (29:10), pp. 1156-1166.

Berwick, D. M., and Hackbarth, A. D. 2012. “Eliminating Waste in US Health Care,” Journal of the American Medical Association (307:14), pp. 1513-1516.

Bhugra, D. 2008. “Decision-Making in Psychiatry: What Can We Learn?,” Acta Psychiatrica Scandinavica (118:1), pp. 1-3.

Boles, J-M., Bion, J., Connors, A., Herridge, M., Marsh, B., Melot, C., Pearl, R., Silverman, H., Stanchina, M., Vieillard-Baron, A., and Weltke, T. 2007. “Weaning from Mechanical Ventilation,” European Respiratory Journal (29:5), pp. 1033-1056.

Breiman, L., Friedman, J. H., Olshen, R. A., and Stone, C. J. 1984. Classification and Regression Trees, London: Chapman and Hall.

Caplan, L. 2014. “Delay in Breast Cancer: Implications for Stage at Diagnosis and Survival,” Frontiers in Public Health (2), Article 87.

Carroll, C. L., and Zucker, A. R. 2006. “Complications Associated with Increased Duration of Mechanical Ventilation and Increased Costs in Pediatric Status Asthmaticus,” CHEST Journal (130:4), p. 242S-b.

Carson, S. S., Cox, C. E., Holmes, G. M., Howard, A., and Carey, T. S. 2006. “The Changing Epidemiology of Mechanical Ventilation: A Population-Based Study,” Journal of Intensive Care Medicine (21:3), pp. 173-182.

Centers for Medicare & Medicaid Services. “National Health Expenditure Projections 2018–2027,” (https://www.cms.gov/ research-statistics-data-and-systems/statistics-trends-andreports/nationalhealthexpenddata/downloads/forecastsummary. pdf; accessed February, 21, 2019).

Chai, X., Deng, L., Yang, Q., and Ling, C. X. 2004. “Test-Cost Sensitive Naive Bayes Classification,” in Proceedings of the 4<sup>th</sup> IEEE International Conference on Data Mining, pp. 51-58.

Chawla, N. V., Hall, L. O., Bowyer, K. W., and Kegelmeyer, W. P. 2002. “SMOTE: Synthetic Minority Oversampling Technique,” Journal of Artificial Intelligence Research (16), pp. 321-357.

Chen, H., Chiang, R., and Storey, V. 2012. “Business Intelligence and Analytics: From Big Data to Big Impact,” MIS Quarterly (36:4), pp. 1165-1188.

Cheng, T. F., Wang, J. D., and Uen, W. C. 2012. “Cost-Utility Analysis of Adjuvant Goserelin (Zoladex) and Adjuvant Chemotherapy in Premenopausal Women with Breast Cancer,” BMC Cancer (12), Article 33.

Clark, W. A., and Lisowski, W. 2017. “Prospect Theory and the Decision to Move or Stay,” in Proceedings of the National Academy of Sciences (114:36), pp. E7432-E7440.

Chu, Y. F., Jiang, Y., Meng, M., Jiang, J. J., Zhang, J. C., Ren, H. S., and Wang, C. T. 2010. “Incidence and Risk Factors of Gastrointestinal Bleeding in Mechanically Ventilated Patients,” World Journal of Emergency Medicine (1:1), pp. 32-36.

Cussens, J. 1993. “Bayes and Pseudo-Bayes Estimates of Conditional Probabilities and Their Reliability,” in Proceedings of the European Conference on Machine Learning, P. B. Brazdil (ed.), pp. 136-152.

Dasta, J. F., McLaughlin, T. P., Mody, S. H., and Piech, C. T. 2005. “Daily Cost of An Intensive Care Unit Day: The Contribution of

Mechanical Ventilation,” Critical Care Medicine (33:6), pp. 1266-1271.

Davenport, T. H. 2013. “Analytics 3.0,” Harvard Business Review (91:12), pp. 64-72.

Denham, J. W., Nowitz, M., Joseph, D., Duchesne, G., Spry, N. A., Lamb, D. S., Matthews, J., and Ball, J. 2014. “Impact of Androgen Suppression and Zoledronic Acid on Bone Mineral Density and Fractures in the Trans-Tasman Radiation Oncology Group (TROG) 03.04 Randomised Androgen Deprivation and Radiotherapy (RADAR) Randomized Controlled Trial for Locally Advanced Prostate Cancer,” BJU International (114:3), pp. 344-353.

Dhar, V. 2014. “Big Data and Predictive Analytics in Health Care,” Big Data (2:3), pp. 113-116.

Dinkelspiel, H. E., Tergas, A. I., Zimmerman, L. A., Burke, W. M., Hou, J. Y., Chen, L., Hillyer, G., Neugut A. I., Hershman D. L., and Wright, J. D. 2015. “Use and Duration of Chemotherapy and its Impact on Survival in Early-Stage Ovarian Cancer,” Gynecologic Oncology (137:2), pp. 203-209.

Domingos, P. 1999. “Metacost: A General Method for Making Classifiers Cost-Sensitive,” in Proceedings of the 5<sup>th</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp.155-164.

Elkan, C. 2001. “The Foundations of Cost-Sensitive Learning,” in Proceedings of the 17<sup>th</sup> International Joint Conference on Artificial Intelligence, pp. 973-978.

Elliott, M. W., Confalonieri, M., and Nava, S. 2002. “Where to Perform Noninvasive Ventilation?,” European Respiratory Journal (19:6), pp. 1159-1166.

Eskandar, N., and Apostolakos, M. J. 2007. “Weaning from Mech anical Ventilation,” Critical Care Clinics (23:2), pp. 263-274.

Fang, X. 2013. “Inference-based Naïve Bayes: Turning Naïve Bayes Cost-Sensitive,” IEEE Transactions on Knowledge and Data Engineering (25:10), pp. 2302-2313.

Fang, X., Liu Sheng, O. R., Goes, P. 2013. “When Is the Right Time to Refresh Knowledge Discovered from Data?,” Operations Research (61:1), pp. 32-44.

Fichman, R. G., Kohli, R., and Krishnan, R. (eds.). 2011. “Editorial Overview—the Role of Information Systems in Healthcare: Current Research and Future Trends,” Information Systems Research (22:3), pp. 419-428.

Gama, J. 2000. “Iterative Bayes,” Intelligent Data Analysis (4), pp. 475-488.

Gao, G., McCullough J., Agarwal R., and Jha A. 2010. “A Study of Online Physician Ratings by Patients,” Working Paper, R. H. Smith School of Business, University of Maryland, College Park.

Gao, H., Li, Y., Shang, J., Gu, M., Huang, Y., and Gong, B. 2017. “Learning from Class-Imbalanced Data: Review of Methods and Applications,” Expert Systems with Applications (73), pp. 220-239.

Girard, T. D., Shintani, A. K., Jackson, J. C., Gordon, S. M., Pun, B. T., Henderson, M. S., Dittus, R. S., Bernard, G. R., and Ely, E. W. 2007. “Risk Factors for Post-Traumatic Stress Disorder Symptoms Following Critical Illness Requiring Mechanical Ventilation: A Prospective Cohort Study,” Critical Care (11:1), Article R28.

Goes, P. B. 2015. “Inflection Point: Looking Back or Looking Forward,” MIS Quarterly (39:3), pp. iii-vii.

Gonzalez, R., and Wu, G. 1999. “On the Shape of the Probability Weighting Function,” Cognitive Psychology (38:1), pp. 129-166.

Gregor, S., and Hevner, A. 2013. “Positioning and Presenting Design Science Research for Maximum Impact,” MIS Quarterly (37:2), pp. 337-355.

Grigorakos, L., Sakagianni, K., Tsigou, E., Apostolakos, G., Nikolopoulos, G., and Veldekis, D. 2010. “Outcome of Acute Heroin Overdose Requiring Intensive Care Unit Admission,” Journal of Opioid Management (6:3), pp. 227-231.

Harris, M. I., Klein, R., Welborn, T. A., and Knuiman, M. W. 1992. “Onset of NIDDM Occurs at Least 4–7 Yr Before Clinical Diagnosis,” Diabetes Care (15:7), pp. 815-819.

Hayashi, Y., Morisawa, K., Klompas, M., Jones, M., Bandeshe, H., Boots, R., Lipman, J., and Paterson, D. L. 2013. “Toward Improved Surveillance: The Impact of Ventilator-Associated Complications on Length of Stay and Antibiotic Use in Patients in Intensive Care Units,” Clinical Infectious Diseases (56:4), pp. 471-477.

Hedman, E., El Alaoui, S., Lindefors, N., Andersson, E., Rück, C., Ghaderi, A., Kaldo, V., Lekander, M., Andersson, G., and Ljótsson, B. 2014. “Clinical Effectiveness and Cost-Effectiveness of Internet- vs. Group-based Cognitive Behavior Therapy for Social Anxiety Disorder: 4-Year Follow-Up of a Randomized Trial,” Behaviour Research and Therapy (59), pp. 20-29.

Heunks, L. M., and van der Hoeven, J. G. 2010. “Clinical Review: The ABC of Weaning Failure—A Structured Approach,” Critical Care (14), Article 245.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Hofmann, H. S., Rettig, G., Radke, J., Neef, H., and Silber, R. E. 2002. “Iatrogenic Ruptures of The Tracheobronchial Tree,” in Proceedings of European Journal of Cardio-Thoracic Surgery (21:4), pp. 649-652.

Hsu, C. W., and Sun, S. F. 2014. “Iatrogenic Pneumothorax Related to Mechanical Ventilation,” World Journal of Critical Care Medicine (3:1), pp. 8-14.

Jiang, L., Li, C., and Wang, S. 2014. “Cost-Sensitive Bayesian Network Classifiers,” Pattern Recognition Letters (45), pp. 211-216.

Kahneman, D., and Tversky, A. 1979. “Prospect Theory: An Analysis of Decision Under Risk,” Econometrica (47:2), pp. 263-292.

Kalanuria, A. A., Zai, W., and Mirski, M. 2014. “Ventilator-Associated Pneumonia in the ICU,” Critical Care (18), Article 208.

Kao, J. H., Kao, H. K., Chen, Y. W., Yu, W. K., Pan, S. W., Wang, J. H., Lien, T. C., Ho, L. I., and Kou, Y. R. 2013. “Impact and Predictors of Prolonged Chest Tube Placement in Mechanically Ventilated Patients with Acquired Pneumothorax,” Respiratory Care (58:12), pp. 2093-2100.

Kashefi, P., Abbasi, A., Abbasi, M., Davoodi, L., and Abbasi, S. 2015. “Comparison of the Efficacyof Nebulized Budesonide and Intravenous Dexamethasone Administration Before Extubation

in Prevention of Post-Extubation Complications Among Patients Admitted in Intensive Care Unit,” Advanced Biomedical Research (4), Article 11.

Kellie, S. P., Scott, M. J., Cavallazzi, R., Wiemken, T. L., Goss, L., Parker, D., and Saad, M. 2014. “Procedural and Educational Interventions to Reduce Ventilator-Associated Pneumonia Rate and Central Line-Associated Blood Stream Infection Rate,” Journal of Intensive Care Medicine (29:3), pp. 165-174.

Koenig, S. M., and Truwit, J. D. 2006. “Ventilator-Associated Pneumonia: Diagnosis, Treatment, and Prevention,” Clinical Microbiology Reviews (19:4), pp. 637-657.

Kohli, R., and Tan, S. S. L. 2016. “Electronic Health Records: How Can IS Researchers Contribute to Transforming Healthcare?,” MIS Quarterly (40:3), pp. 553-573.

Kubat, M., and Matwin, S. 1997. “Addressing the Curse of Imbalanced Training Sets: One-Sided Selection,” in Proceedings of the 14<sup>th</sup> International Conference Machine Learning, pp. 179-186.

Larrick, R. P., and Boles, T. L. 1995. “Avoiding Regret in Decisions with Feedback: A Negotiation Example,” Organizational Behavior and Human Decision Processes (63:1), pp. 87-97.

Larson, R. A., Conti, R., Padula, W. V., Apperley, J. F., Baccarani, M., Eigendorff, E., Guilhot, F., and Hehlmann, R. 2014. “What Is the Most Cost-Effective Strategy for Treating Newly Diagnosed Chronic Phase Chronic Myeloid Leukemia (CML) after Imatinib Loses Patent Exclusivity?,” Blood (124:21), pp. 738-738.

Lee, J. S., and Zhu, D. 2011. “When Costs Are Unequal and Unknown: A Subtree Grafting Approach for Unbalanced Data Classification,” Decision Sciences (42:4), pp. 803-829.

Le Guennec, L., Brisset, M., Viala, K., Essardy, F., Maisonobe, T., Rohaut, B., Demeret, S., Bolgert, F., and Weiss, N. 2014. “Post-Traumatic Stress Symptoms in Guillain–Barré Syndrome Patients after Prolonged Mechanical Ventilation in ICU: A Preliminary Report,” Journal of the Peripheral Nervous System (19:3), pp. 218-223.

Li, J., Liu, L. S., Fong, S., Wong, R. K., Mohammed, S., Fiaidhi, J., Sung, Y., and Wong, K. L. 2017. “Adaptive Swarm Balancing Algorithms for Rare-Event Prediction in Imbalanced Healthcare Data,” PLoS ONE (12:7), Article e0180830.

Lin, Y. K., Chen, H., Brown, R. A., Li, S. H., and Yang, H. J. 2017. “Healthcare Predictive Analytics for Risk Profiling in Chronic Care: A Bayesian Multitask Learning Approach,” MIS Quarterly (41:2) pp. 473-495.

Ling, C. X., Sheng, S., and Yang, Q. 2006. “Test Strategies for Cost-Sensitive Decision Trees,” IEEE Transactions on Knowledge and Data Engineering (18:8), pp. 1055-1067.

Ling, C. X., Yang, Q., Wang, J., and Zhang, S. 2004. “Decision Trees with Minimal Costs,” in Proceedings of the 21<sup>st</sup> International Conference on Machine Learning, pp. 69-76.

Loomes, G., and Sugden, R. 1982. “Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty,” The Economic Journal (92:368), pp. 805-824.

Lopez, M. E., Fallon, S. C., Lee, T. C., Rodriguez, J. R., Brandt, M. L., and Mazziotti, M. V. 2014 “Management of the Pediatric Spontaneous Pneumothorax: Is Primary Surgery the Treatment

of Choice?,” The American Journal of Surgery (208:4), pp. 571-576.

Mango, P. D., and Riefberg, V. E. 2009. “Three Imperatives for Improving US Health Care,” McKinsey Quarterly (2), pp. 40-44.

Mann, T. A. 2012. The Cost-Effectiveness of Cardiac Monitoring in Breast Cancer Patients Who Have Received Cardiotoxic Therapies, unpublished Ph.D. Dissertation, University of Texas, Austin.

Manyika, J., Chui, M., Brown, B., Bughin, J., Dobbs, R., Roxburgh, C., and Byers, A. 2011. “Big Data: The Next Frontier for Innovation, Competition, and Productivity,” McKinsey Global Institute (https://bigdatawg.nist.gov/pdf/MGI\_big\_data\_full\_ report.pdf; accessed n February 21, 2019).

Margineantu, D. D. 2002. “Class Probability Estimation and Cost-Sensitive Classification Decisions,” in Proceeding of 13<sup>th</sup> European Conference on Machine Learning, pp. 270-281.

Menon, N. M., and Kohli, R. 2013. “Blunting Damocles’ Sword: A Longitudinal Model of Healthcare IT Impact on Malpractice Insurance Premium and Quality of Patient Care,” Information Systems Research (24:4), pp. 918-932.

Menon, N. M., Lee, B., and Eldenburg, L. 2000.” Productivity of Information Systems in the Healthcare Industry,” Information Systems Research (11:1), pp. 83-92.

Misra, A. 2014. “Common Sports Injuries: Incidence and Average Charges,” ASPE, U.S. Department of Health & Human Services (https://aspe.hhs.gov/report/common-sports-injuries-incidenceand-average-charges).

Mittmann, N., Porter, J. M., Rangrej, J., Seung, S. J., Liu, N., Saskin, R., Cheung, M. C., Leighl, N. B., Hoch, J. S., Trudeau, M., and Evans, W. K. 2014. “Health System Costs for Stage-Specific Breast Cancer: A Population-Based Approach,” Current Oncology (21:6), pp. 281-293.

Moore, H. C., Unger, J. M., Phillips, K. A., Boyle, F., Hitre, E., Porter, D., Prudence A. F., and Albain, K. S. 2015. “Goserelin for Ovarian Protection During Breast-Cancer Adjuvant Chemotherapy,” New England Journal of Medicine (372:10), pp. 923-932.

Newman, J., Grobman, W. A., and Greenland, P. 2008. “Combination Polypharmacy for Cardiovascular Disease Prevention in Men: A Decision Analysis and Cost Effectiveness Model,” Preventive Cardiology (11:1), pp. 36-41.

Ogawa, S., and Piller, F. T. 2006. “Reducing the Risks of New Product Development,” MIT Sloan Management Review (47:2), pp.65-71.

Pazzani, M. J., Merz, C. J., Murphy, P. M., Ali, K., Hume, T., and Brunk, C. 1994. “Reducing Misclassification Costs,” in Proceeding of 13<sup>th</sup> International Conference Machine Learning, pp. 217-225.

Peitz, G. W., Troyer, J., Jones, A. E., Shapiro, N. I., Nelson, R. D., Hernandez, J., and Kline, J. A. 2014. “Association of Body Mass Index with Increased Cost of Care and Length of Stay for Emergency Department Patients with Chest Pain and Dyspnea,” Circulation: Cardiovascular Quality and Outcomes (7:2), pp. 292-298.

Phillips-Wren, G. E., Iyer, L. S., Kulkarni, U. R., and Ariyachandra, T. 2015. “Business Analytics in the Context of Big Data: A Roadmap for Research,” Communications of the Association for Information Systems (37:23), pp. 448-472.

Plastaras, J. P., Mesina, A., Grover, S., Mesina, C., Nasta, S., and Svoboda, J. 2014. “Risk Factors for Radiation Pneumonitis in Patients with Lymphoma Treated with Chemotherapy and Photon or Proton Radiation Therapy,” International Journal of Radiation Oncology \* Biology \* Physics (90:1), Supplement S682.

Prelec, D. 2000. “Compound Invariant Weighting Functions in Prospect Theory,” in Choices, Values, and Frames, D. Kahneman and A. Tversky, Cambridge, UK: Cambridge University Press, pp. 67-92.

Qiu, S., Chinnam, P. B., Murat, A., Batarse, B., Neemuchwala, H., and Jordan, W. 2015. “A Cost Sensitive Inpatient Bed Reservation Approach to Reduce Emergency Department Boarding Times,” Health Care Management Science (18:1), pp. 67-85.

Quinlan, J. R. 1993. C4.5: Programs for Machine Learning. San Mateo, CA: Morgan Kaufmann Publishers.

Raphaeli, T., and Menon, R. 2012. “Current Treatment of Lower Gastrointestinal Hemorrhage,” Clinics in Colon and Rectal Surgery (25:04), pp. 219-227.

Roche, M. M., and Wang, P. P. 2014. “Factors Associated with a Diabetes Diagnosis and Late Diabetes Diagnosis for Males and Females,” Journal of Clinical & Translational Endocrinology (1:3), pp. 77-84.

Roeggla, M., Roeggla, G., Muellner, M., Wagner, A., and Laggner, A. N. 1996. “The Cost of Treatment of Spontaneous Pneumothorax with the Thoracic Vent Compared with Conventional Thoracic Drainage,” CHEST Journal (110:1), p. 303.

Sadosky, A., Mardekian, J., Parsons, B., Hopps, M., Bienen, E. J., and Markman, J. 2015. “Healthcare Utilization and Costs in Diabetes Relative to the Clinical Spectrum of Painful Diabetic Peripheral Neuropathy,” Journal of Diabetes and its Compli cations (29:2), pp. 212-217.

Saltzman, J. R., Feldman, M., and Travis, A. 2015. “Approach to Acute Upper Gastrointestinal Bleeding in Adults,” UpToDate (https://www.uptodate.com/contents/approach-to-acute-uppergastrointestinal-bleeding-in-adults; accessed September 25, 2016).

Schlienger, J. L. 2013. “Type 2 Diabetes Complications,” La Presse Médicale(42:5), pp. 839-848.

Severgnini, P., Selmo, G., Lanza, C., Chiesa, A., Frigerio, A., Bacuzzi, A., and Dionigi, G. 2013. “Protective Mechanical Ventilation During General Anesthesia for Open Abdominal Surgery Improves Postoperative Pulmonary Function,” Anesthesiology (118:6), pp. 1307-1321.

Shafir, E., and LeBoeuf, R. A. 2002. “Rationality,” Annual Review of Psychology (53:1), pp. 491-517.

Sharma, P. P., Yu, A. T. C., Johnson, K. W., and Fonarow, G. 2014. “High and Low Cost Hospital Stays for Acute Heart Failure in the US: Findings from the Nationwide Inpatient Sample (NIS) 2011,” Journal of the American College of Cardiology (63:12), Supplement.

Shapiro, C. L., and Recht, A. 2001. “Side Effects of Adjuvant Treatment of Breast Cancer,” New England Journal of Medicine (344:26), pp. 1997-2008.

Sheng, V. S., and Ling, C. X. 2006. “Thresholding for Making Classifiers Cost-Sensitive,” in Proceedings of the 21<sup>st</sup> National Conference on Artificial Intelligence, pp. 476-481.

Sher, D. J., Wee, J. O., and Punglia, R. S. 2011. “Cost-Effectiveness Analysis of Stereotactic Body Radiotherapy and

Radiofrequency Ablation for Medically Inoperable, Early-Stage Non-Small Cell Lung Cancer,” International Journal of Radiation Oncology\* Biology\* Physics (81:5), p. e767.

Snedecor, G. W., and Cochran, W. G. 1989. Statistical Methods. Ames, IA: Blackwell Publishing Professional.

Terzi, E., Zarogoulidis, K., Kougioumtzi, I., Dryllis, G., Kioumis, I., Pitsiou, G., Machairiotis, N., Katsikogiannis, N., Lampaki, S., Papaiwannou, A., and Tsiouda, T. 2014. “Acute Respiratory Distress Syndrome and Pneumothorax,” Journal of Thoracic Disease (6:4), pp. S435-S442.

Tian, S., Hirshfield, K. M., Jabbour, S. K., Toppmeyer, D., Haffty, B. G., Khan, A. J., and Goyal, S. 2014. “Serum Biomarkers for the Detection of Cardiac Toxicity After Chemotherapy and Radiation Therapy in Breast Cancer Patients,” Frontiers in Oncology (4), Article 277.

Ting, K. M. 2002. “An Instance-Weighting Method to Induce Cost-Sensitive Tress,” IEEE Transaction on Knowledge and Data Engineering (14:3), pp. 659-665.

Tolwani, A. 2012. “Continuous Renal-Replacement Therapy for Acute Kidney Injury,” New England Journal of Medicine (367:26), pp. 2505-2514.

Torresini, G., Vaccarili, M., Divisi, D., and Crisci, R. 2001. “Is Video-Assisted Thoracic Surgery Justified at First Spontaneous Pneumothorax?,” European Journal of Cardio-Thoracic Surgery (20:1), pp. 42-45.

Turney, P. 1995. “Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm,” Journal of Artificial Intelligence Research (2), pp. 369-409.

Tversky, A., and Kahneman, D. 1992. “Advances in Prospect Theory: Cumulative Representation of Uncertainty,” Journal of Risk and Uncertainty (5:4), pp. 297-323.

Tversky, A., and Wakker, P. 1995. “Risk Attitudes and Decision Weights,” Econometrica: Journal of the Econometric Society (63:6), pp.1255-1280.

UK Prospective Diabetes Study Group. 1998. “Intensive Blood-Glucose Control with Sulphonylureas or Insulin Compared with Conventional Treatment and Risk of Complications in Patients with Type 2 Diabetes (UKPDS 33),” The Lancet (352:9131), pp. 837-853.

Vassilakopoulos, T., Zakynthinos, S., and Roussos, C. 1998. “The Tension–Time Index and The Frequency/Tidal Volume Ratio Are the Major Pathophysiologic Determinants of Weaning Failure and Success,” American Journal of Respiratory and Critical Care Medicine (158:2), pp. 378-385.

Wang, Y., and Hajli, N. 2017. “Exploring the Path to Big Data Analytics Success in Healthcare,” Journal of Business Research (70), pp. 287-299.

Watson, H. J. 2014. “Tutorial: Big Data Analytics: Concepts, Technologies, and Applications,” Communications of the Association for Information Systems (34:65), pp. 1247-1268.

Weiss, G. M. 2004. “Mining with Rarity: A Unifying Framework,” SIGKDD Explorations (6:1), pp. 7-19.

Weiss, Y., Elovici, Y., and Rokach, L. 2013. “The CASH Algorithm-Cost-Sensitive Attribute Selection Using Histograms,” Information Sciences (222), pp.247-268.

Whiting, D. R., Guariguata, L., Weil, C., and Shaw, J. 2011. “IDF Diabetes Atlas: Global Estimates of the Prevalence of Diabetes

for 2011 and 2030,” Diabetes Research and Clinical Practice (94:3), pp. 311-321.

Williams, A. D., O’Moore, K., Mason, E., and Andrews, G. 2014. “The Effectiveness of Internet Cognitive Behaviour Therapy (iCBT) for Social Anxiety Disorder Across Two Routine Practice Pathways,” Internet Interventions (1:4), pp. 225-229.

Wolff, A. C., Blackford, A. L., Visvanathan, K., Rugo, H. S., Moy, B., Goldstein, L. J., Stockerl-Goldstein, K., Neumayer, L., Langbaum, T. S., Theriault, R. L., and Hughes, M. E. 2015. “Risk of Marrow Neoplasms After Adjuvant Breast Cancer Therapy: The National Comprehensive Cancer Network Experience,” Journal of Clinical Oncology (33:4), pp. 340-348.

Wunsch, H., Linde-Zwirble, W. T., Angus, D. C., Hartman, M. E., Milbrandt, E. B., and Kahn, J. M. 2010. “The Epidemiology of Mechanical Ventilation Use in the United States,” Critical Care Medicine (38:10), pp.1947-1953.

Yi, A., Kim, H. H., Shin, H. J., Huh, M. O., Ahn, S. D., and Seo, B. K. 2009. “Radiation-Induced Complications After Breast Cancer Radiation Therapy: A Pictorial Review of Multimodality Imaging Findings,” Korean Journal of Radiology (10:5), pp. 496-507.

Zadrozny, B., and Elkan, C. 2001. “Learning and Making Decisions When Costs and Probabilities Are Both Unknown,” in Proceedings of the 7<sup>th</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 204-213.

Zeelenberg, M., Beattie, J., Van der Pligt, J., and De Vries, N. K. 1996. “Consequences of Regret Aversion: Effects of Expected Feedback on Risky Decision Making,” Organizational Behavior and Human Decision Processes (65:2), pp. 148-158

Zhao, H. 2008. “Instance Weighting versus Threshold Adjusting for Cost-Sensitive Classification,” Knowledge and Information Systems (15), pp. 321-334

Zhao, H., and Ram, S. 2004. “Constrained Cascade Generalization of Decision Trees,” IEEE Transactions on Knowledge and Data Engineering (16:6), pp. 727-739.

Zhou, Z. H., and Liu, X. Y. 2006. “Training Cost-Sensitive Neural Networks with Methods Addressing the Class Imbalance Problem,” IEEE Transactions on Knowledge and Data Engineering (18:1), pp. 63-77.

## About the Authors

Xiao Fang is Professor of Management Information Systems and J.P. Morgan Chase Senior Fellow at the Lerner College of Business & Economics and Institute for Financial Services Analytics, University of Delaware. He studies business analytics, social network analytics, and financial technology with research methods and tools drawn from reference disciplines including management science (e.g., optimization) and computer science (e.g., machine learning). He has published in business journals, including MIS Quarterly, Management Science, Operations Research, and Information Systems Research, as well as computer science outlets such as ACM Transactions on Information Systems and IEEE Transactions on Knowledge and Data Engineering.

Yuanyuan Gao is an assistant professor of the Department of Management in the College of Business and Economics at California State University, East Bay. She holds a Ph.D. in Information Systems from the University of Utah, an M.S. in Information Systems and Operation Management from the University of Florida, and a B.Sc. in Information Systems Management from the University of International Business and Economics. Her research interests include machine learning, data mining, decision support systems, text analytics, and social media analysis. Specifically, her research focuses on review analysis in social media.

Paul Jen-Hwa Hu is David Eccles Chair Professor at the David Eccles School of Business, the University of Utah. He received his Ph.D. in Management Information Systems from the University of Arizona. His current research interests include information technology for health care, technology implementation and management, business analytics, digital transformation, technology impacts and evaluations, and technology-enabled knowledge management. Paul has published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the AIS, Decision Sciences, and various IEEE and ACM transactions.

## Appendix A

## Proofs and Lemmas

## Proof of Lemma 1

If $C _ { 1 } \geq C _ { 3 } , C _ { 2 } \geq C _ { 3 }$ , and $C _ { 4 } \geq C _ { 3 } ,$ it is optimal to invest and classify the instance as class 1. By substituting $C _ { 1 }$ and $C _ { 3 }$ with Equations (1) and (3) respectively and rearranging terms, $C _ { 1 } \geq C _ { 3 }$ becomes

$$
p \left(D _ {1 1} - D _ {1 0}\right) \geq V - D _ {1 0}\tag{A1}
$$

To satisfy $C _ { 1 } \geq C _ { 3 } ,$ , the following condition must hold:

$$
\left\{ \begin{array}{l l} p \geq \frac {V - D _ {1 0}}{D _ {1 1} - D _ {1 0}} & \text { if } D _ {1 1} > D _ {1 0} \\ p \leq \frac {D _ {1 0} - V}{D _ {1 0} - D _ {1 1}} & \text { if } D _ {1 1} <   D _ {1 0} \end{array} \right.\tag{A2}
$$

$\mathrm { I f } D _ { 1 1 } = D _ { 1 0 } ,$ , inequality (A1) is independent $\mathrm { o f } p ,$ , and the investment-adjusted cost-sensitive learning problem becomes trivial. Then the equality situation $D _ { 1 1 } = D _ { 1 0 }$ is not considered by Condition (A2). In line with this reasoning, equality situations are not considered throughou Appendix A.

Similarly, $C _ { 2 } \geq C _ { 3 }$ implies

$$
p \left(D _ {1 1} - D _ {1 0} + T _ {0} + T _ {1}\right) \geq V + T _ {0} - D _ {1 0}
$$

To satisfy $C _ { 2 } \geq C _ { 3 } ,$ the following condition must hold:

$$
\left\{ \begin{array}{l l} p \geq \frac {V + T _ {0} - D _ {1 0}}{D _ {1 1} - D _ {1 0} + T _ {0} + T _ {1}} & \text { if } D _ {1 1} + T _ {0} + T _ {1} > D _ {1 0} \\ p \leq \frac {D _ {1 0} - V - T _ {0}}{D _ {1 0} - D _ {1 1} - T _ {0} - T _ {1}} & \text { if } D _ {1 1} + T _ {0} + T _ {1} <   D _ {1 0} \end{array} \right.\tag{A3}
$$

Combining Conditions (A2) and (A3) yields Condition (5).

For $C _ { 4 } \geq C _ { 3 }$ , we have

$$
p \left(D _ {1 1} - D _ {1 0} - D _ {0 1} + D _ {0 0} + T _ {0} + T _ {1}\right) \geq D _ {0 0} + T _ {0} - D _ {1 0}
$$

By solving this inequality, we obtain Condition (6). #

Lemmas 2–4 can be proved in similar ways.

## Proof of Lemma 2

If $C _ { 1 } \geq C _ { 4 } , C _ { 2 } \geq C _ { 4 }$ , and $C _ { 3 } \geq C _ { 4 }$ , it is optimal to invest and classify the instance as class 0. By replacing $C _ { 1 }$ and $C _ { 4 }$ with Equations (1) and (4), respectively, and rearranging terms, $C _ { 1 } \geq C _ { 4 }$ becomes

$$
p \left(D _ {0 1} - D _ {0 0} - T _ {0} - T _ {1}\right) \geq V - D _ {0 0} - T _ {0}
$$

Solving this inequality leads to the following condition:

$$
\left\{ \begin{array}{l l} p \geq \frac {V - D _ {0 0} - T _ {0}}{D _ {0 1} - D _ {0 0} - T _ {0} - T _ {1}} & \text { if } D _ {0 1} > D _ {0 0} + T _ {0} + T _ {1} \\ p \leq \frac {D _ {0 0} + T _ {0} - V}{D _ {0 0} + T _ {0} + T _ {1} - D _ {0 1}} & \text { if } D _ {0 1} <   D _ {0 0} + T _ {0} + T _ {1} \end{array} \right.\tag{A4}
$$

Similarly, $C _ { 2 } \geq C _ { 4 }$ becomes

$$
p \left(D _ {0 1} - D _ {0 0}\right) \geq V - D _ {0 0}
$$

To satisfy $C _ { 2 } \geq C _ { 4 } ,$ , the following condition must hold:

$$
\left\{ \begin{array}{l l} p \geq \frac {V - D _ {0 0}}{D _ {0 1} - D _ {0 0}} & \text { if } D _ {0 1} > D _ {0 0} \\ p \leq \frac {D _ {0 0} - V}{D _ {0 0} - D _ {0 1}} & \text { if } D _ {0 1} <   D _ {0 0} \end{array} \right.\tag{A5}
$$

By integrating Conditions (A4) and (A5), we derive Condition (7). Specifically, $\mathrm { f } D _ { 0 1 } > D _ { 0 0 } + T _ { 0 } + T _ { 1 } , \mathrm { b y } ( \mathrm { A } 4 )$ , the condition $\begin{array} { r } { p \ge \frac { { \cal V } - { D _ { 0 0 } } - { T _ { 0 } } } { { D _ { 0 1 } } - { D _ { 0 0 } } - { T _ { 0 } } - { T _ { 1 } } } } \end{array}$ must be satisfied. Because $D _ { 0 1 } > D _ { 0 0 } + T _ { 0 } + T _ { 1 }$ <sub>1</sub> implies $D _ { 0 1 } > D _ { 0 0 } ,$ according to (A5), the condition $\begin{array} { r } { p \ge \frac { V - D _ { 0 0 } } { D _ { 0 1 } - D _ { 0 0 } } } \end{array}$ must also be satisfied. Thus, $\mathrm { i f } D _ { 0 1 } > D _ { 0 0 } + T _ { 0 } + T _ { 1 } ,$ , the condition $\begin{array} { r } { p \ge \operatorname* { m a x } \left( \frac { V - D _ { 0 0 } - T _ { 0 } } { D _ { 0 1 } - D _ { 0 0 } - T _ { 0 } - T _ { 1 } } , \frac { V - D _ { 0 0 } } { D _ { 0 1 } - D _ { 0 0 } } \right) } \end{array}$ must be satisfied. Similarly, i $\mathrm { f } D _ { 0 1 } { < } D _ { 0 0 } , \mathrm { b y } ( \mathrm { A } 4 )$ and (A5), the condition $\begin{array} { r } { p \leq \operatorname* { m i n } \left( \frac { D _ { 0 0 } + T _ { 0 } - V } { D _ { 0 0 } + T _ { 0 } + T _ { 1 } - D _ { 0 1 } } , \frac { D _ { 0 0 } - V } { D _ { 0 0 } - D _ { 0 1 } } \right) } \end{array}$ must be satisfied. If $D _ { 0 0 } < D _ { 0 1 } < D _ { 0 0 } + T _ { 0 } + T _ { 1 }$ , by combining the condition for $D _ { 0 1 } < D _ { 0 0 } + T _ { 0 } + T _ { 1 }$ in (A4) and the condition for $D _ { 0 0 } < D _ { 0 1 }$ in (A5), we derive the condition $\begin{array} { r } { \frac { V - D _ { 0 0 } } { D _ { 0 1 } - D _ { 0 0 } } \leq p \leq \frac { D _ { 0 0 } + T _ { 0 } - V } { D _ { 0 0 } + T _ { 0 } + T _ { 1 } - D _ { 0 1 } } } \end{array}$

For $C _ { 3 } \geq C _ { 4 } ,$ we have

$$
p \left(D _ {0 1} - D _ {0 0} - D _ {1 1} + D _ {1 0} - T _ {1} - T _ {0}\right) \geq D _ {1 0} - T _ {0} - D _ {0 0}
$$

Solving this inequality yields Condition (8). #

## Proof of Lemma 3

If $C _ { 2 } \geq C _ { 1 } , C _ { 3 } \geq C _ { 1 }$ , and $C _ { 4 } \geq C _ { 1 } ,$ , it is optimal not to invest and classify the instance as class 1. By substituting $C _ { 3 }$ and $C _ { 1 }$ with Equations (3) and (1), respectively, and rearranging terms, $C _ { 3 } \geq C _ { 1 }$ becomes

$$
p \left(D _ {1 1} - D _ {1 0}\right) \leq V - D _ {1 0}
$$

Solving the inequality leads to Condition (9). Similarly, by substituting $C _ { 2 }$ and $C _ { 1 }$ with Equations (2) and (1), respectively, and rearranging terms, $C _ { 2 } \geq C _ { 1 }$ becomes

$$
p \left(T _ {1} + T _ {0}\right) \geq T _ {0}
$$

Thus, to satisfy $C _ { 2 } \geq C _ { 1 : }$ , the following condition must hold:

$$
p \geq \frac {T _ {0}}{T _ {1} + T _ {0}}\tag{A6}
$$

For $C _ { 4 } \geq C _ { 1 }$ , we have

$$
p \left(T _ {0} + T _ {1} + D _ {0 0} - D _ {0 1}\right) \geq T _ {0} + D _ {0 0} - V
$$

To satisfy $C _ { 4 } \geq C _ { 1 : }$ , the following condition must hold:

$$
\left\{ \begin{array}{l l} p \geq \frac {T _ {0} + D _ {0 0} - V}{T _ {1} + T _ {0} + D _ {0 0} - D _ {0 1}} & \text { if } T _ {1} + T _ {0} + D _ {0 0} > D _ {0 1} \\ p \leq \frac {V - T _ {0} - D _ {0 0}}{D _ {0 1} - T _ {1} - D _ {0 0} - T _ {0}} & \text { if } T _ {1} + T _ {0} + D _ {0 0} <   D _ {0 1} \end{array} \right.\tag{A7}
$$

By combining Conditions (A6) and (A7), we obtain Condition (10). #

## Proof of Lemma 4

If $C _ { 1 } \geq C _ { 2 } , C _ { 3 } \geq C _ { 2 }$ , and $C _ { 4 } \geq C _ { 2 } ,$ , it is optimal not to invest and classify the instance as class 0. By substituting $C _ { 1 }$ and $C _ { 2 }$ with Equations (1) and (2), respectively, and rearranging terms, $C _ { 1 } \geq C _ { 2 }$ becomes

$$
p \left(T _ {0} + T _ {1}\right) \leq T _ {0}
$$

Solving the inequality leads to the following condition:

$$
p \leq \frac {T _ {0}}{T _ {0} + T _ {1}}\tag{A8}
$$

Similarly, for $C _ { 3 } \geq C _ { 2 }$ , we have

$$
p \left(T _ {0} + T _ {1} + D _ {1 1} - D _ {1 0}\right) \leq T _ {0} + V - D _ {1 0}
$$

To satisfy $C _ { 3 } \geq C _ { 2 } ,$ the following condition must hold:

$$
\left\{ \begin{array}{l l} p \leq \frac {T _ {0} + V - D _ {1 0}}{T _ {0} + T _ {1} + D _ {1 1} - D _ {1 0}} & \text { if } T _ {0} + T _ {1} + D _ {1 1} > D _ {1 0} \\ p \geq \frac {D _ {1 0} - T _ {0} - V}{D _ {1 0} - T _ {0} - T _ {1} - D _ {1 1}} & \text { if } T _ {0} + T _ {1} + D _ {1 1} <   D _ {1 0} \end{array} \right.\tag{A9}
$$

Combining Conditions (A8) and (A9) yields Condition (11). For $C _ { 4 } \geq C _ { 2 }$ , we have

$$
p \left(D _ {0 1} - D _ {0 0}\right) \leq V - D _ {0 0}
$$

Solving the inequality leads to Condition (12). #

## Appendix B

## Proof of Proposition 1

Because min $C _ { 3 } , C _ { 4 } ) < \operatorname* { m i n } ( C _ { 1 } , C _ { 2 } )$ , the cost reduction by our method compared with existing cost-sensitive learning methods, min $( C _ { 1 } , C _ { 2 } ) -$ min $( C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 } )$ becomes

$$
\min \left(C _ {1}, C _ {2}\right) - \min \left(C _ {1}, C _ {2}, C _ {3}, C _ {4}\right) = \min \left(C _ {1}, C _ {2}\right) - \min \left(C _ {3}, C _ {4}\right)
$$

We analyze the cost reduction in several scenarios.

(i) I $\Gamma C _ { 1 } \leq C _ { 2 }$ and $C _ { 3 } \leq C _ { 4 }$

$$
\begin{array}{l} \min (C _ {1}, C _ {2}) - \min (C _ {3}, C _ {4}) \\ = C _ {1} - C _ {3} \\ = (1 - p) p _ {1 0} (c _ {1 0} - \overline {{c}} _ {1 0}) + p p _ {1 1} (c _ {1 1} - \overline {{c}} _ {1 1}) - V \end{array}
$$

Accordingly, the cost reduction is greater if the investment amount V is smaller, or $\mathrm { i f } c _ { 1 0 } - \overline { { c } } _ { 1 0 } \mathrm { o r } c _ { 1 1 } - \overline { { c } } _ { 1 1 } ( \mathrm { i . e }$ ., the classification cost reduction due to the investment) is larger, or ${ \mathrm { i f } } p _ { 1 0 } { \mathrm { o r } } p _ { 1 1 } ( { \mathrm { i . e . } }$ , the probability of classification cost reduction due to the investment) is greater. Thus, Proposition 1 holds when $C _ { 1 } \geq C _ { 2 }$ and $C _ { 3 } \geq C _ { 4 }$

(ii) $\operatorname { I f } C _ { 1 } \leq C _ { 2 }$ and $C _ { 4 } \leq C _ { 3 }$

$$
\begin{array}{l} \min (C _ {1}, C _ {2}) - \min (C _ {3}, C _ {4}) \\ = C _ {1} - C _ {4} \\ = p p _ {0 1} (c _ {0 1} - \overline {{c}} _ {0 1}) + (1 - p) p _ {0 0} (c _ {0 0} - \overline {{c}} _ {0 0}) - V + (1 - p) c _ {1 0} + p c _ {1 1} - (1 - p) c _ {0 0} - p c _ {0 1} \end{array}
$$

That is, the cost reduction is greater if the investment amount V is smaller, or if $\dot { \boldsymbol { c } } _ { 0 1 } - \overline { { \boldsymbol { c } } } _ { 0 1 } \mathrm { o r } \boldsymbol { c } _ { 0 0 } - \overline { { \boldsymbol { c } } } _ { 0 0 } \left( \mathrm { i } . \mathrm { e } . _ { \mathrm { : } } \right.$ , the classification cost reduction due to the investment) is larger, or if $p _ { 0 1 } \mathrm { o r } p _ { 0 0 } \mathrm { ( i . e ) }$ ., the probability of classification cost reduction due to the investment) is greater. Proposition 1 holds when $C _ { 1 } \leq C _ { 2 }$ and $C _ { 4 } \leq C _ { 3 }$

(iii) If $C _ { 2 } \leq C _ { 1 }$ and $C _ { 3 } \leq C _ { 4 }$

$$
\begin{array}{l} \min (C _ {1}, C _ {2}) - \min (C _ {3}, C _ {4}) \\ = C _ {2} - C _ {3} \\ = p p _ {1 1} (c _ {1 1} - \overline {{c}} _ {1 1}) + (1 - p) p _ {1 0} (c _ {1 0} - \overline {{c}} _ {1 0}) - V + p c _ {0 1} + (1 - p) c _ {0 0} - p c _ {1 1} - (1 - p) c _ {1 0} \end{array}
$$

Accordingly, the cost reduction is greater if the investment amount V is smaller, or $\mathrm { i f } c _ { 1 1 } - \overline { { c } } _ { 1 1 } \mathrm { o r } c _ { 1 0 } - \overline { { c } } _ { 1 0 }$ (i.e., the classification cost reduction due to the investment) is larger, or $\mathrm { i f } p _ { 1 1 } \mathrm { o r } p _ { 1 0 } \mathrm { ( i . e ) }$ ., the probability of classification cost reduction due to the investment) is higher. Proposition 1 holds when $C _ { 2 } \leq C _ { 1 }$ and $C _ { 3 } \leq C _ { 4 }$

(iv) $\operatorname { I f } C _ { 2 } \leq C _ { 1 }$ and $C _ { 4 } \leq C _ { 3 } ,$

$$
\begin{array}{l} \min (C _ {1}, C _ {2}) - \min (C _ {3}, C _ {4}) \\ = C _ {2} - C _ {4} \\ = p p _ {0 1} (c _ {0 1} - \overline {{c}} _ {0 1}) + (1 - p) p _ {0 0} (c _ {0 0} - \overline {{c}} _ {0 0}) - V \end{array}
$$

That is, the cost reduction is greater if the investment amount V is smaller, or if $\dot { \mathbf { \sigma } } _ { c _ { 0 1 } } - \overline { { c } } _ { 0 1 } \operatorname { o r } c _ { 0 0 } - \overline { { c } } _ { 0 0 } ( \mathrm { i } . \mathbf { e } .$ , the classification cost reduction due to the investment) is larger, or if ${ p } _ { 0 1 } \mathrm { o r } p _ { 0 0 } ( \mathrm { i . e . }$ , the probability of classification cost reduction due to the investment) is higher. Proposition 1 holds when $C _ { 2 } \leq C _ { 1 }$ and $C _ { 4 } \leq C _ { 3 }$

In summary, we show that Proposition 1 holds in all possible scenarios. #

## Appendix C

## Parameter Calibrations

To calibrate the classification costs in the cost matrix C, we identified common complications associated with different ventilation remova decisions by reviewing relevant literature and consulting experienced physicians knowledgeable about the clinical use of mechanical ventilation and related complications. We summarize the complications in Table C1. As an example, the top-right cell of Table C1 indicates five common complications if the decision is not to remove mechanical ventilation but a patient should have it removed. We then calculated the expected cost of treating each identified complication, as summarized in Table C2. Taking the estimated cost for treating ventilator-associated pneumonia as an example, for which Kellie et al. (2014, p. 166) estimated costs ranging from \$10,019 to \$39,828. We used the average of the cost range (\$24,924) in our evaluation. The estimated probability of ventilator-associated pneumonia (VAP) is 9%–27% for all mechanically ventilated patients (Kalanuria et al. 2014, p. 1), similar to a VAP occurrence rate of 27% reported in other studies (Koenig and Truwit 2006). We therefore included a 0.27 probability of developing VAP. The expected cost of treating this complication is $\$ 6,730$ . We list the treatment cost and probability of developing each common complication in Table C2, with the sources in Tables C3 and C4.<sup>15</sup>

<table><tr><td colspan="3">Table C1. Common Complications Associated with Different Ventilation Removal Decisions</td></tr><tr><td></td><td>Not Removing</td><td>Removing</td></tr><tr><td>Classified as Not Removing</td><td>Ventilation-associated pneumonia (Carroll and Zucker 2006)Pneumothorax (Hofmann et al. 2002)</td><td>Ventilation-associated pneumonia (Carroll and Zucker 2006)Pneumothorax (Kao et al. 2013)Gastrointestinal bleeding (Eskandar and Apostolakos 2007)Heart failure (Hayashi et al. 2013)Rhabdomyolysis (Carroll and Zucker 2006)</td></tr><tr><td>Classified as Removing</td><td>Post-extubation distress (Heunks and van der Hoeven 2010)Dyspnea (Vassilakopoulos et al. 1998)Post-traumatic stress (Girard et al. 2007)Ventilation-associated pneumonia (Carroll and Zucker 2006)Pneumothorax (Kao et al. 2013)</td><td>No complications</td></tr></table>

Table C2. Cost of Treating Each Common Complication Associated with Ventilation Removal Decisions

<table><tr><td>Complication</td><td>Probability of Developing Complication</td><td>Treatment Cost</td><td>Expected Treatment Cost</td></tr><tr><td>Ventilator-associated pneumonia (VAP)</td><td>0.27 (Kalanuria et al. 2014)</td><td>$24,924 (Kellie et al. 2014)</td><td>$6,730</td></tr><tr><td>Pneumothorax</td><td>0.30 (Hsu and Sun 2014; Terzi et al. 2014)</td><td>$10,101 (Lopez et al. 2014; Roeggla et al. 1996; Torresini et al. 2001)</td><td>$3,030</td></tr><tr><td>Gastrointestinal bleeding</td><td>0.47 (Chu et al. 2010)</td><td>$10,712 (Raphaeli et al. 2012; Saltzman et al. 2015)</td><td>$5,035</td></tr><tr><td>Heart failure</td><td>0.07 (Hayashi et al. 2013)</td><td>$15,767 (Sharma et al. 2014)</td><td>$1,104</td></tr><tr><td>Rhabdomyolysis</td><td>0.13 (Grigorakos et al. 2010)</td><td>$5,000 (Newman et al. 2008)</td><td>$650</td></tr><tr><td>Post-extubation distress</td><td>0.11 (Kashefi et al. 2015)</td><td>$8,052 (Azoulay et al. 2014; Tolwani 2012)</td><td>$886</td></tr><tr><td>Dyspnea</td><td>0.31 (Severgnini et al. 2013)</td><td>$ 3,664 (Peitz et al. 2014)</td><td>$1,136</td></tr><tr><td>Post-traumatic stress</td><td>0.22 (Le Guennec et al. 2014)</td><td>$3,151 (Hedman et al. 2014)</td><td>$694</td></tr></table>

Notes: According to Carroll and Zucker (2006), VAP is a common complication of a prolonged use of mechanical ventilation; its probability is mostly the same across different decision scenarios. Similarly, the probability of developing pneumothorax is similar in various decision scenarios (Carroll and Zucker 2006).

<table><tr><td>Complication</td><td>Treatment Cost</td><td>Explanation and Justification</td></tr><tr><td>Ventilator-associated pneumonia</td><td>$24,924</td><td>The estimated treatment cost ranges from $10,019 to $39,828 (Kellie et al. 2014, p. 166). We used the average ($24,924) in the evaluation.</td></tr><tr><td>Pneumothorax</td><td>$10,101</td><td>Surgery is a preferred treatment, and the cost ranges from $3,380 to $19,702 (Lopez et al. 2014, p. 573). The 95% confidence interval of the cost of using conventional intercostal chest tube drainage to treat pneumothorax is between $3,100 and $14,270, and that of using thoracic vents ranges from $500 to $2,480 (Roeggla et al. 1996). Two treatment costs— $2,750 and $1,925 per patient—are associated with pleural drainage and video-assisted thoracic surgery treatment, respectively (Torresini et al. 2001). Thus the lowest treatment cost is $500 and the highest is $19,702. We used $10,101 (the midpoint) as the treatment cost in the evaluation.</td></tr><tr><td>Gastrointestinal bleeding</td><td>$10,712</td><td>Gastrointestinal (GI) bleeding includes upper and lower forms. $^{1}$  The cost of treating upper GI bleeding ranges between $5647 and $15,776 (Saltzman et al. 2015). The cost of treating lower GI bleeding ranges from $9,700 to $11,800 (Raphaeli et al. 2012). We combined these cost ranges, derived a range of treating GI bleeding from $5,647 to $15,776, and used $10,712 (the midpoint) in the evaluation.</td></tr><tr><td>Heart failure</td><td>$15,767</td><td>A low cost (i.e., average at the 20th percentile and below) is $2,946, and a high cost (i.e., average at the 80th percentile and above) is $28,588 (Sharma et al. 2014). We used $15,767 (the midpoint) in the evaluation.</td></tr><tr><td>Rhabdomyolysis</td><td>$5,000</td><td>The treatment cost is $5,000 (Newman et al. 2008, p. 38). We used this estimated cost in the evaluation.</td></tr><tr><td>Post-extubation distress</td><td>$8,052</td><td>Renal replacement therapy is a treatment (Azoulay et al. 2014), and its average cost is $8,052 (Tolwani 2012, p. 2511). We used this value in the evaluation.</td></tr><tr><td>Dyspnea</td><td>$3,664</td><td>The mean cost is $3,663 (Peitz et al. 2014, p. 294), which we used in the evaluation.</td></tr><tr><td>Post-traumatic stress</td><td>$3,151</td><td>Post-traumatic stress is an anxiety disorder, and two treatment methods for anxiety disorder are Internet-based cognitive behavior therapy (ICBT) and cognitive behavioral group therapy (CBGT), with costs of $464 and $2,687, respectively (Hedman et al. 2014, p. 22). Because ICBT is a lower cost alternative to CBGT (Williams et al. 2014), the minimum treatment cost is $464. The maximum is $3,151 (i.e., $464 + $2,687), if ICBT are used first and followed by CBGT. We used $3,151 in the evaluation.</td></tr></table>

Notes: For probabilities or treatment costs that span ranges of values, we used a typical value of the range, such as its median. <sup>1</sup>https://www.uspharmacist.com/article/differentiating-upper-and-lower-gi-bleeds; accessed March 5, 2019.

<table><tr><td colspan="3">Table C4. Probabilities for Complications Associated with Ventilation Removal Decisions</td></tr><tr><td>Complication</td><td>Probability</td><td>Explanation and Justification</td></tr><tr><td>Ventilator-associated pneumonia</td><td>0.27</td><td>VAP occurs in 9%–27% of all mechanically ventilated patients (Kalanuria et al. 2014, p. 1), and the rate of 27% is supported by other studies (Koenig and Truwit 2006). We used 0.27 in the evaluation.</td></tr><tr><td>Pneumothorax</td><td>0.30</td><td>The probability of developing pneumothorax ranges from 14% to 87% (Hsu and Sun 2014, p. 9). We used 0.30 in the evaluation, because it is within the range and supported by other studies (Terzi et al. 2014).</td></tr><tr><td>Gastrointestinal bleeding</td><td>0.47</td><td>The probability of developing GI bleeding is 46.7% (Chu et al. 2010, p. 32). We used 0.47 (rounded from 46.7%) in the evaluation.</td></tr><tr><td>Heart failure</td><td>0.07</td><td>The occurrence rate of heart failure is 7.2% (Hayashi et al. 2013, p. 474); so we used 0.07 (rounded from 7.2%) in the evaluation.</td></tr><tr><td>Rhabdomyolysis</td><td>0.13</td><td>Of 16 patients with mechanical ventilation, 2 develop rhabdomyolysis (Grigorakos et al. 2010). Thus we used 0.13 (i.e., 2/16) in the evaluation.</td></tr><tr><td>Post-extubation distress</td><td>0.11</td><td>Kashefi et al. (2015) mention that 11.1% of patients in each of their studied groups develop post-extubation distress. We thus used 0.11 (rounded from 11.1%).</td></tr><tr><td>Dyspnea</td><td>0.31</td><td>The probability that patients with standard ventilation develop dyspnea is 30.8% (Severgnini et al. 2013, p. 1318). We used 0.31 (rounded from 30.8%) in the evaluation.</td></tr><tr><td>Post-traumatic stress</td><td>0.22</td><td>The probability of developing post-traumatic stress is 22% (Le Guennec et al. 2014, p. 220); so we used 0.22.</td></tr></table>

Different ventilation removal decisions can lead to various complications. In Table $^ { 6 , }$ we estimated the classification cost incurred by a ventilation removal decision as the total cost of treating the complications associated with the decision. For example, as we show in Table C1, patients are likely to suffer from five complications if the decision is not to remove mechanical ventilation when it should be removed. By summing the expected treatment costs of the five complications in Table C2, we can derive the classification cost $( \mathrm { i } . \mathrm { e } _ { . , \ : { c _ { 1 0 } } }$ in Table 6) for the decision not to remove mechanical ventilation from a patient who should have it removed.

With an investment in advanced, non-invasive, positive pressure ventilation, we expect a probability of 87.5% that patients will not develop ventilation-associated pneumonia (Antonelli et al. 1998). By obviating the need to treat ventilation-associated pneumonia, we obtain a new classification cost matrix (Table 7). For example, according to Table C2, the expected cost of treating ventilation-associated pneumonia is \$6,730; if this cost is avoided, the classification cost $c _ { 0 1 }$ in Table 6 (i.e., \$13,632) changes to $\overline { { c } } _ { 0 1 }$ in Table 7 (i.e., \$13,632 – \$6,730). We summarize in Table 8 the probabilities of changes in classification costs due to an investment. The investment amount V is the expense of using advanced non-invasive positive pressure ventilation, which is \$1,636 (Dasta et al. 2005; Elliott et al. 2002).

## Appendix D

## Empirical Evaluation with Breast Cancer Data

The American Cancer Society estimated that, in 2015 alone, there were approximately 292,130 new breast cancer patients in the United States.<sup>16</sup> A crucial clinical decision is whether a patient should be diagnosed as having malignant tumors in her breast(s). We use 102,294 breast cancer cases, obtained from KDD Cup 2008, to demonstrate the performance of our method in support of CDM, compared with the benchmark methods in Table 9.<sup>17</sup> Each case consists of 117 breast image features of a patient and a class label attribute that indicates whether the patient actually has malignant tumors. To calibrate the classification costs in the cost matrix C, we first identified the common complications associated with different diagnosis decisions by reviewing extant literature and consulting experienced medical experts. In Table D1, the top-right cell lists common complications if a patient is diagnosed as normal but has malignant tumors. The bottom-left and bottom-right cells indicate the frequent complications associated with common cancer treatments, such as chemo-therapy and radiation therapy. Typically, patients receive such common treatments if they are diagnosed to have malignant tumors. We obtained the cost of treating each of the frequently associated complications summarized in Table D2. The average cost of treating breast cancer increases by stage (Mittmann et al. 2014, p. 281): \$29,938 for stage 1, \$46,893 for stage 2, \$65,369 for stage 3, and \$66,627 for stage 4. Patients in our breast cancer data set were already at stage 3. The development and spread of malignant tumor cells could cause them to migrate and develop stage 4 breast cancer, which costs \$66,627 to treat. Thus, we used \$66,627 as the estimated treatment cost for the development and spread of malignant tumor cells to stage 4. Caplan (2014, p. 2) reports a 0.12 probability that patients in stage 3 will develop to stage 4 breast cancer, so the expected cost for treating this complication is \$7,995 (= \$66,627 × 0.12). In Table D3, we estimate the classification cost associated with each diagnosis decision as the total expected cost of treating the complications associated with that decision. We further detail how we derived the estimated treatment costs and probabilities in Tables D3 and D4.

Table D1. Complications Commonly Associated with Different Breast Cancer Diagnosis Decisions

<table><tr><td></td><td>Actual Benign (i.e., Normal)</td><td>Actual Malignant</td></tr><tr><td>Classifying as Benign (i.e., Normal)</td><td>No complications</td><td>Development and spread of malignant tumor cells (Caplan 2014)Ovarian failure (Shapiro and Recht 2001)Oxidative stress (Shapiro and Recht 2001)Cardiotoxicity (Shapiro and Recht 2001)Chemotherapy-associated leukemia (Shapiro and Recht 2001)Radiation pneumonitis (Shapiro and Recht 2001; Yi et al. 2009)Overlying bone fractures (Yi et al. 2009)</td></tr><tr><td>Classifying as Malignant</td><td>Ovarian failure (Shapiro and Recht 2001)Oxidative stress (Shapiro and Recht 2001)Cardiotoxicity (Shapiro and Recht 2001)Chemotherapy-associated leukemia (Shapiro and Recht 2001)Radiation pneumonitis (Shapiro and Recht 2001; Yi et al. 2009)Overlying bone fractures (Yi at al. 2009)</td><td>Ovarian failure (Shapiro and Recht 2001)Oxidative stress (Shapiro and Recht 2001)Cardiotoxicity (Shapiro and Recht 2001)Chemotherapy-associated leukemia (Shapiro and Recht 2001)Radiation pneumonitis (Shapiro and Recht 2001; Yi et al. 2009)Overlying bone fractures (Yiet al. 2009)</td></tr></table>

Table D2. Cost of Treating Each Complication Associated with Breast Cancer Diagnosis Decisions

<table><tr><td>Complication</td><td>Probability of Developing Complication</td><td>Treatment Cost</td><td>Expected Treatment Cost</td></tr><tr><td>Development and spread of malignant tumor cells</td><td>0.12 (Caplan 2014)</td><td>$66,627 (Mittmann et al. 2014)</td><td>$7,995</td></tr><tr><td>Ovarian failure</td><td> $0.30^1$ </td><td>$59,700 (Archer et al. 2015) $^2$ </td><td>$17,910</td></tr><tr><td>Peripheral neuropathy</td><td>0.35 (Areti et al. 2014)</td><td>$12,492 (Sadosky et al. 2014)</td><td>$4,372</td></tr><tr><td>Cardiotoxicity</td><td>0.27 (Tian et al. 2014)</td><td>$15,656 (Mann 2012)</td><td>$4,227</td></tr><tr><td>Chemotherapy-associated leukemia</td><td>0.0005 (Wolff et al. 2015)</td><td>$178,800 (Larson et al. 2014)</td><td>$89</td></tr><tr><td>Radiation pneumonitis</td><td>0.146 (Plastaras et al. 2014)</td><td>$10,134 (Sher et al. 2011)</td><td>$1,480</td></tr><tr><td>Overlying bone fractures</td><td>0.067 (Denham et al. 2014)</td><td>$4,452 (Misra 2014)</td><td>$298</td></tr></table>

<sup>1</sup>Source: http://www.uptodate.com/contents/overview-of-infertility-and-pregnancy-outcome-in-cancer-survivors; accessed October 12, 2015. <sup>2</sup>Infertility resource: http://www.ihr.com/infertility/egg-donation/egg-donation-egg-donor-costs.html.

<table><tr><td>Complication</td><td>Treatment Cost</td><td>Explanation and Justification</td></tr><tr><td>Development and spread of malignant tumor cells</td><td>$66,627</td><td>The average cost of breast cancer treatment increases by stage (Mittmann et al. 2014, p. 281): $29,938 for stage 1, $46,893 for stage 2, $65,369 for stage 3, and $66,627 for stage 4. Patients were already at stage 3. The development and spread of malignant tumor cells could cause them to develop stage 4 breast cancer, and the treatment cost would be $66,627.</td></tr><tr><td>Ovarian failure</td><td>$59,700</td><td>The treatment of ovarian failure consists of estrogen/progestin therapy and egg donation. $^{1}$  Archer et al. (2015) estimate $530 million to $1.1 billion for hormone therapy (estrogen therapy), and the prescriptions are estimated for 500,000 to 1 million women. The maximum possible cost for estrogen therapy is $1.1 billion/500,000 = $2,200. The minimum possible cost for estrogen therapy is $530 million/1 million = $530. The cost of egg donation consists of donation expenses across categories ($26,550 to $47,450) and donor expenses ($4,000 to $10,000). $^{2}$  The minimum cost of egg donation is $30,550 ($26,550 + $4,000), and the maximum cost is $57,450 ($47,450 + $10,000). Therefore, the maximum treatment cost for ovarian failure is $59,700 ($57,450 + $2,200 = $59,650, rounded up to $59,700); the minimum treatment cost is $31,100 ($30,550 + $530 = $31,080, rounded to $31,100). We used $59,700 in the evaluation.</td></tr><tr><td>Peripheral neuropathy</td><td>$12,492</td><td>According to Sadosky et al. (2015, p.216), the cost of treating diabetic peripheral neuropathy, the most common peripheral neuropathy, ranges between $12,492 and $30,755. $^{3}$  We used $12,492 in the evaluation.</td></tr><tr><td>Cardiotoxicity</td><td>$15,656</td><td>Multi-gated acquisition scanning is the “gold-standard” and most accepted treatment method for cardiotoxicity, with an average treatment cost of $15,656 (Mann 2012, p. 338).</td></tr><tr><td>Chemotherapy-associated leukemia</td><td>$178,800</td><td>The strategy for treating leukemia includes using imatinib ($76,800) and dasatinib or nilotinib ($102,000) (Larson et al. 2014). We used $178,800, or $76,800 + $102,000.</td></tr><tr><td>Radiation pneumonitis</td><td>$10,134</td><td>According to Sher et al. (2011), the monthly treatment cost for Grade 2 pneumonitis is $90.25, and the treatment lasts for three months. Thus, the treatment cost for Grade 2 pneumonitis is $271, or $90.25 × 3 = $270.75 (rounded up to $271). According to Sher et al. (2011, p. 3), the monthly treatment cost for Grade 3 pneumonitis is 1,643.76 ($1,371.32 + $272.44), and the treatment lasts for six months. Thus, the treatment cost for Grade 3 pneumonitis is $9,863, or $1,643.76 × 6 = $9,862.56 (rounded up to $9,863). The minimum cost is the cost to treat Grade 2 pneumonitis, $271. The maximum cost occurs when the treatment for grade 2 pneumonitis fails and the patient develops grade 3 pneumonitis. The maximum cost thus is $271 + $9,863 = $10,134. We used $10,134 in the evaluation.</td></tr><tr><td>Overlying bone fractures</td><td>$4,452</td><td>Treatment costs for eight bone injuries (fractures) range from $2,294 to $7,666 (Misra 2014, p. 5). The average of the eight treatment costs is $4,452, so we used this value.</td></tr></table>

<sup>1</sup>Advanced fertility center of Chicago: http://www.advancedfertility.com/premature-ovarian-failure.htm .  
<sup>2</sup>Infertility resource: http://www.ihr.com/infertility/egg-donation/egg-donation-egg-donor-costs.html  
<sup>3</sup>National Institute of Neurological Disorders and Stroke https://www.ninds.nih.gov/Disorders/Patient-Caregiver-Education/Fact-Sheets/Peripheral Neuropathy-Fact-Sheet.

<table><tr><td colspan="3">Table D4. Probabilities for Complications Associated with Breast Cancer Diagnosis Decisions</td></tr><tr><td>Complication</td><td>Probability</td><td>Explanation and Justification</td></tr><tr><td>Development and spread of malignant tumor cells</td><td>0.12</td><td>Patients in our breast cancer data set were already in stage 3. According to Caplan (2014, p. 2), the probability of developing stage 4 breast cancer from stage 3 ranges from 0.05 to 0.12. We used 0.12 in the evaluation.</td></tr><tr><td>Ovarian failure</td><td>0.30</td><td>According to the Cardonick&#x27;s (2015) “Overview of Infertility and Pregnancy Outcome in Cancer Survivors” (subsection “Risk of Infertility among Cancer Survivors”), the cumulative incidence of premature menopause (ovarian failure) approached 30%. We thus used 0.30 in the evaluation. (See Footnote 17 for details.)</td></tr><tr><td>Peripheral neuropathy</td><td>0.35</td><td>Around 30%–40% of patients undergoing chemotherapy develop peripheral neuropathy (Areti et al. 2014, p. 289). We used 0.35 (the average) in the evaluation.</td></tr><tr><td>Cardiotoxicity</td><td>0.27</td><td>Anthracyclines (AC), used alone or in combination with other chemotherapy agents, are common treatment agents (Tian et al. 2014, p. 1). When chemotherapy is provided together with ACs, the probability of cardiotoxicity can be as high as 27%. We used 0.27 in the evaluation.</td></tr><tr><td>Chemotherapy-associated leukemia</td><td>0.0005</td><td>According to the National Cancer Institute (U.S.), leukemia usually begins in the bone marrow. $^{1}$  Wolff et al. (2015) analyzed 109,560 person-years of patient follow-up and reported that the overall rate of marrow neoplasms (leukemia) after the treatment of breast cancer was 0.46 per 1,000 person-years. We rounded up to 0.05%.</td></tr><tr><td>Radiation pneumonitis</td><td>0.146</td><td>Of 89 patients treated with chemotherapy and photon or proton radiation therapy, 13 were diagnosed with radiation pneumonitis, or 14.6% (Plastaras et al. 2014), We used 0.146 in the evaluation.</td></tr><tr><td>Overlying bone fractures</td><td>0.067</td><td>The frequency of bone fractures after radiation is 72 of 1071 patients, or 6.7% (Denham et al. (2014, p. 347). We used 0.067 in the evaluation.</td></tr></table>

<sup>1</sup>National Cancer Institute: https://www.cancer.gov/types/leukemia.

<table><tr><td colspan="3">Table D5. Classification Cost Matrix C for Breast Cancer Diagnosis</td></tr><tr><td></td><td>Actually Benign</td><td>Actually Malignant</td></tr><tr><td>Classifying as Benign</td><td> $c_{00} = \$0$ </td><td> $c_{01} = \$36,371$ </td></tr><tr><td>Classifying as Malignant</td><td> $c_{10} = \$28,376$ </td><td> $c_{11} = \$28,376$ </td></tr></table>

Investing in the medication Goserelin to protect a patient’s ovaries increases the estimated probability that a patient will not develop ovarian failure to 66.70% (Moore et al. 2015). We obtain the new classification cost matrix in Table D6. For example, according to Table D2, the expected cost of treating ovarian failure is \$17,910; if this cost is obviated, classification cost $c _ { 1 0 } \left( \mathbb { S } 2 8 , 3 7 6 \right)$ in Table D5 changes to $\overline { { c } } _ { 1 0 } ( \mathbb { S } 2 8 , 3 7 6$ – \$17,910) in Table D6. We also summarize in Table D7 the probabilities of classification cost changes due to this investment. The investmen amount V is the expense of applying Goserelin, which costs \$1,153 (Cheng et al. 2012; Dinkelspiel et al. 2015). After calibrating the parameters, we performed experiments to examine the effectiveness and robustness of our method, using the procedure described in the “Empirical Evaluation” section in the main text

<table><tr><td colspan="3">Table D6. New Classification Cost Matrix  $\overline{C}$  for Breast Cancer Diagnosis</td></tr><tr><td></td><td>Actually Benign</td><td>Actually Malignant</td></tr><tr><td>Classifying as Benign</td><td> $\overline{c}_{00} = \$0$ </td><td> $\overline{c}_{01} = \$18,461$ </td></tr><tr><td>Classifying as Malignant</td><td> $\overline{c}_{10} = \$10,466$ </td><td> $\overline{c}_{11} = \$10,466$ </td></tr></table>

<table><tr><td colspan="4">Table D7. Probability  $p_{ij}$  of Cost Change Due to an Investment (Breast Cancer Diagnosis)</td></tr><tr><td>Probability of Changing from  $c_{00}$  to  $\overline{c}_{00}$ </td><td>Probability of Changing from  $c_{01}$  to  $\overline{c}_{01}$ </td><td>Probability of Changing from  $c_{10}$  to  $\overline{c}_{10}$ </td><td>Probability of Changing from  $c_{11}$  to  $\overline{c}_{11}$ </td></tr><tr><td> $p_{00}=0$ </td><td> $p_{01}=0.667$ </td><td> $p_{10}=0.667$ </td><td> $p_{11}=0.667$ </td></tr></table>

We conducted 100 experiments to examine the effectiveness of our method. For both the proposed and benchmark methods, we used C4.5, coupled with m-estimation, to estimate the probability p that a patient has malignant tumors. Overall, our method consistently recorded the lowest cost among all the investigated methods, across all the experiments. We applied a Wilcoxon signed-rank test to the experimental results, and our method significantly outperformed each benchmark method (p < 0.001). Furthermore, we observed substantial cost reductions over the benchmark methods, as summarized in Table D8. For example, the average cost of our method is \$7,079,357 across all 100 experiments, whereas that of MC (best-performing benchmark) is \$8,604,710. On average, the cost of our method, 20.43% lower than that of THR, 17.73% lower than that of MC, and 34.09% lower than that of SMOTE (worst-performing benchmark).

Table D8. Average Cost of Each Investigated Method, across 100 Experiments<sup>1</sup>

<table><tr><td>Method</td><td>Cost: Average (± Standard Deviation)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>Our Method (ICSL)</td><td>$7,079,357 (±$355,771)</td><td></td></tr><tr><td>THR</td><td>$8,638,207 (±$334,353)</td><td>20.43%</td></tr><tr><td>SMOTE</td><td>$10,769,447 (±$708,135)</td><td>34.09%</td></tr><tr><td>IW</td><td>$9,803,830 (±$371,288)</td><td>27.77%</td></tr><tr><td>MC</td><td>$8,604,710 (±$227,070)</td><td>17.73%</td></tr></table>

<sup>1</sup>The performance improvement attained with the breast cancer data is lower than that attained with the ventilation data. The differentials might reflect the relatively high imbalance in the breast cancer data: 101,671 records belong to class 0 (i.e., benign), and 623 records belong to class 1 (i.e., malignant).

Robustness Analysis in Scenario I: We created different evaluation situations by changing the investment amount from V × 60% to V × 140%, setting the classification costs in Table D5 from c × 60% to c × 140% for all $i , j \in \{ 0 , 1 \}$ , or altering the probabilities of cost change in Table D7 from $p _ { i j } \times 6 0 \% \mathrm { t o } p _ { i j } \times 6 0 \%$ for all $i , j \in \{ 0 , 1 \}$ , in increments of 10%.<sup>18</sup> Then we conducted 100 experiments to compare the performance outcomes. Again, our method significantly and substantially outperformed each benchmark method, at p < 0.001. Moreover, the cost reduction by our method increased with the classification costs and probabilities of cost change, and it decreased with the investment amount, in line with Proposition 1. For example, the cost reduction by our method relative to MC, the best-performing benchmark method, increased from 15.50% to 20.73% as the investment amount dropped from V × 140% to V × 60%.

Robustness Analysis in Scenario II: For all investigated methods, we used other classification algorithms to estimate the probability p that a patient has malignant tumors, including logistic regression, support vector machines, and naïve Bayes. We conducted 100 experiments for each method. As Tables D9–D11 reveal, the average cost of our method, across 100 experiments, was substantially lower than that of any benchmark method, for all the alternative classification algorithms. Furthermore, according to the Wilcoxon signed-rank test results, our method consistently and significantly outperformed each benchmark method (p < 0.001), for all the classification algorithms.

<table><tr><td colspan="3">Table D9. Average Cost of Each Investigated Method (p Estimated with Logistic Regression)</td></tr><tr><td>Method</td><td>Cost: Average (± Standard Deviation)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>Our Method (ICSL)</td><td>$6,499,451 (±$321,509)</td><td></td></tr><tr><td>THR</td><td>$7,527,023 (±$364,708)</td><td>13.65%</td></tr><tr><td>SMOTE</td><td>$8,214,865 (±$300,924)</td><td>20.91%</td></tr><tr><td>IW</td><td>$7,873,894 (±$347,888)</td><td>17.46%</td></tr><tr><td>MC</td><td>$7,857,071 (±$372,739)</td><td>17.28%</td></tr><tr><td colspan="3">Table D10. Average Cost of Each Investigated Method (p Estimated with Support Vector Machine)</td></tr><tr><td>Method</td><td>Cost: Average (± Standard Deviation)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>Our Method (ICSL)</td><td>$6,663,296 (±$337,369)</td><td></td></tr><tr><td>THR</td><td>$7,548,001 (±$361,195)</td><td>11.73%</td></tr><tr><td>SMOTE</td><td>$8,211,726 (±$303,896)</td><td>18.89%</td></tr><tr><td>IW</td><td>$7,821,624 (±$339,069)</td><td>14.83%</td></tr><tr><td>MC</td><td>$7,727,714 (±$320,242)</td><td>13.80%</td></tr></table>

<table><tr><td colspan="3">Table D11. Average Cost of Each Investigated Method (p Estimated with Naïve Bayes)</td></tr><tr><td>Method</td><td>Cost: Average (± Standard Deviation)</td><td>Average Cost Reduction by ICSL</td></tr><tr><td>Our Method (ICSL)</td><td>$103,467,473 (±$15,188,529)</td><td></td></tr><tr><td>THR</td><td>$159,124,779 (±$23,734,101)</td><td>34.95%</td></tr><tr><td>SMOTE</td><td>$186,939,406 (±$24,457,512)</td><td>44.74%</td></tr><tr><td>IW</td><td>$173,324,005 (±$25,425,072)</td><td>40.30%</td></tr><tr><td>MC</td><td>$258,753,201 (±$53,077,896)</td><td>59.46%</td></tr></table>
