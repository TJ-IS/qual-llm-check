---
otero_id: 26731
otero_key: "8EVFCSEH"
title: "Overcoming Ineffective Mental Representations in Base-Rate Problems"
authors: "Marie Christine Roy; F. Javier Lerch"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.2.233"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [137.132.123.69] On: 06 October 2015, At: 21:44 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/8EVFCSEH/fulltext/images/20850f2f8f679a42c50a06f56f075eac4b599d269349a253e46aaaf49598822c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Overcoming Ineffective Mental Representations in Base-Rate Problems

Marie Christine Roy, F. Javier Lerch,

## To cite this article:

Marie Christine Roy, F. Javier Lerch, (1996) Overcoming Ineffective Mental Representations in Base-Rate Problems. Information Systems Research 7(2):233-247. http://dx.doi.org/10.1287/isre.7.2.233

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/8EVFCSEH/fulltext/images/5d055bce7ffb529c6e9976ee888077b5c1adf1a28000ed4f484461e660758810.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Overcoming Ineffective Mental Representations in Base-rate Problems

Marie Christine Roy • F. Javier Lerch

Faculté des Sciences de L'Administration, Université Laval, Québec, Canada G1K 7P4

roymc@vm1.vlaval.ca

Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213
fl0c+@andrew.cmu.edu

Many biases have been observed in probabilistic reasoning, hindering the ability to follow normative rules in decision-making contexts involving uncertainty. One systematic error people make is to neglect base rates in situations where prior beliefs in a hypothesis should be taken into account when new evidence is obtained. Incomplete explanations for the phenomenon have impeded the development of effective debiasing procedures or tools to support decision making in this area. In this research, we show that the main reason behind these judgment errors is the causal representation induced by the problem context. In two experiments we demonstrate that people often possess the appropriate decision rules but are unable to apply them correctly because they have an ineffective causal mental representation. We also show how this mental representation may be modified when a graph is used instead of a problem narrative. This new understanding should contribute to the design of better decision aids to overcome this bias. (Base-rate Fallacy; Representational Aid; Mental Representation; Decision Support)

## 1. Introduction

A large number of studies have shown that people make systematic judgment errors and that these errors significantly impair human performance in a variety of decision making situations (Kahneman et al. 1982, Dawes 1986, Eddy 1982, Eggleston 1983, Joyce and Biddle 1981). Many of these judgment biases have been related to probabilistic reasoning (see Kahneman et al. 1982 for a review), undermining the ability to follow normative rules in decision-making contexts involving uncertainty. One of these biases is the neglect of base rates in situations where prior beliefs in a hypothesis should be taken into account when new evidence is obtained.

To illustrate, try solving the following problem:

Two cab companies operate in a given city, the Blue and the Green (according to the color of cab they run). 85% of the cabs in the city are Blue, and the remaining 15% are Green. A cab was involved in a hit-and run accident at night. A witness later identified the cab as a Green cab. The court tested the witness' ability to distinguish between Blue and Green cabs under nighttime visibility conditions. It found that the witness was able to identify each color correctly about 80% of the time, but confused it with the other color about 20% of the time. What do you think are the chances that the errant cab was indeed Green, as the witness claimed? (Tversky and Kahneman 1980).

If your answer is 80%, then you have succumbed to the fallacy. The correct answer is 41%.

Research in this judgment bias has identified some of the conditions that induce people to ignore base rates and only consider the new evidence (see Bar-Hillel 1983 for a review). However, the proposed explanations for the phenomenon have failed to identify the underlying cognitive processes that generate this error. The lack of a good theory has prevented the development of effective debiasing procedures or tools to support decision making in this area.

In order to develop better decision aids, we must identify the cognitive operations in need of support, and then identify the nature of the decision aids that may help to overcome human information processing limitations in these operations (Todd and Benbasat 1991,

Zachary 1988). This is the approach adopted in this study.

First, we show that the main obstacle to using base rates is the causal mental representation induced by typical base rate problems. People have a tendency to privilege causality in their way of thinking about these problems and this impedes their ability to correctly process questions such as “the probability that the cab was indeed green” in our example. Second, we show that information display can change the mental representation into one that is more effective to process the information in base-rate problems.

This study differs from those that typically explored the effectiveness of various information displays, because it focusses on the underpinnings of the decision process. Previous studies (Tan and Benbasat 1990, Jarvenpaa 1989, Vessey and Galetta 1991, Tan and Benbasat 1993, Coll et al. 1994) have taken for granted that individuals have acquired an appropriate mental representation of the problem, and focus on the way information extraction is facilitated or hindered by alternate forms of information display. For instance, Vessey and Galetta's cognitive fit theory states that graphs are more appropriate for spatial tasks, i.e. those involving the comparison of data values, whereas tables best support symbolic tasks in which specific values are needed. Consequently, some progress has been made on formulating a theory of information display, but its impact on problem representation or formulation remains a relatively unexplored area (Pracht and Courtney 1988, Loy 1991).

Some prior work has suggested that information displays help people construct better mental models (Loy 1991, Cole 1989). Cole, for instance, trained subjects to solve base-rate type problems with a variety of graphical and tabular feedback. He found a significant improvement in judgment accuracy because of the use of these different forms of display. We build upon his work by addressing these issues in a more systematic way, first by developing and testing a theory of mental representations, then specifying and testing an appropriate external aid to building a better mental representation. As opposed to Cole's studies, where training was used, we show that the simple presentation of the problem with a graph is sufficient to improve judgments.

The paper proceeds as follows: after briefly describing the base-rate fallacy phenomenon ( $§2$ ) and previous attempts to correct it ( $§3$ ), we state our research hypotheses in the light of what we propose to be the underlying mental representations driving the fallacy ( $§4$ ). Sections 5 and 6 describe two experiments, one designed to test for the mental representation and one to investigate the impact of a different form of external representation. We conclude by discussing the impact these findings have for the design of decision support tools and suggest future avenues of research.

## 2. The Base-Rate Fallacy

Normative rules prescribe that a prior probability associated with a belief in a hypothesis remains relevant when some new or more specific evidence is received. Bayes' rule dictates that $p(H|E)$ , the probability of a hypothesis H, given the information about the base rate or prior $p(H)$ (for instance, the distribution of taxi cabs in the city from the earlier example), evidence E (the witness says it was green), and the diagnosticity of the evidence $p(E|H)$ (the accuracy of the witness), be estimated with:

$$
p (H \mid E) = \frac {p (E \mid H) \times p (H)}{p (E \mid H) \times p (H) + p (E \mid \sim H) \times p (\sim H)}.
$$

When asked for $p(H|E)$ , the probability of the hypothesis given the base rate and the evidence, subjects often give $p(E|H)$ as their answer, which in the taxi cab example is 80%. That is, they rely almost entirely on the more specific evidence when making their predictions. This apparent neglect of the base rate $p(H)$ is known as the “base-rate fallacy” (Bar-Hillel 1980).

This significant departure from normative theories has been a major concern for researchers in behavioral decision making because of the persistence of the phenomenon. Most of the effort was devoted to understanding why people apparently neglect the base-rate information and many explanations have been proposed: Representativeness (Kahneman and Tversky 1973), vividness (Nisbett et al. 1976), perceived relevance (Bar-Hillel 1980), or semantic confusion (Eddy 1982, Dawes 1986). A large number of studies have shown that the phenomenon appears in some problem settings but not in others. For instance, base rates are taken into account when they are viewed as a causal property (e.g. the proportion of candidates failing an exam, which is attributed to the difficulty of the exam, Ajzen 1977) or when the diagnostic information can not be interpreted causally (e.g. instead of a witness identifying a cab's color, he hears an intercom and the diagnostic information is the proportion of taxis having intercoms. No relationship between cab color and its having an intercom can be inferred. Bar-Hillel 1980). Changing the problem format, question formulation or order of presentation of the information had no effect on the occurrence of the fallacy (Tversky and Kahneman 1982, Lyon and Slovic 1976). There is therefore no evidence that the error is the consequence of an artifact such as the problem formulation.

## 3. Debiasing Strategies

A significant amount of research has been devoted to reducing the base-rate fallacy. Debiasing strategies can be classified into three different approaches. The first involves modifying the information presentation of the problem. This approach is based on a presumption that people will process the information correctly when it is presented in a form that elicits the appropriate mental procedures. Second, subjects are trained to use appropriate information processing strategies. The underlying premise is that once the correct process is acquired by individuals, they will transfer the knowledge to other problems of the same type. A third strategy involves replacing the individual with a model, which does not directly support the decision process, but rather suggests a normatively correct output.

## 3.1. Information Presentation

Two different categories of information presentation manipulations were used to improve base rate judgments: the first attempted to put more emphasis on the neglected information in the problem description; the second presented samples of population occurrences to illustrate the impact of the information. An example of emphasizing base rates is Fischhoff et al.'s (1979) "subjective sensitivity analysis." They had subjects consider how alternative values of the base rates would affect their estimates. Although the information presentation format was not modified per se, changing the value of the base rate had the effect of focusing more attention on it. They found this manipulation to elicit a larger number of correct responses. Fischhoff and Bar-Hillel (1984) review this and other attempts to focus attention on the base rate information. They show that these “focusing techniques” do not actually enhance people’s understanding, but merely encourage the use of whatever information that is presented. This result points out the importance of distinguishing between the subject’s understanding of the task vs. simply being enticed to use some information.

Gigerenzer et al. (1988) suggested that base rates would appear more salient, and consequently be used, if subjects were to witness the random sampling process. Using the classical Engineer-Lawyer problem (where subjects usually base their predictions of the person's profession on a person's description and ignore the base rates) (Kahneman and Tversky 1973), they asked subjects to pick out one description from an urn containing ten descriptions, after having provided the distribution of engineers and lawyers (base rate) in the urn. They found this procedure to have a positive impact on judgment accuracy.

Christensen-Szalanski and Beach (1982) presented subjects with slides of patients in a disease diagnosis context. When the test results and the presence of the disease were both on the slides, performance on the conditional question improved. However, when only the base rate (presence or absence of the disease) was presented on the slides and the diagnosticity of the test given separately, the base-rate fallacy remained prevalent. Although this manipulation was criticized as promoting the direct estimation of relative frequencies rather than helping people integrate base rate and diagnostic information (Beyth-Marom and Arkes 1983), results definitely indicate that presenting information in this way facilitates people's understanding of the situation. Similarly, Pollatsek et al. (1987) found that presenting subjects with a table of occurrences (e.g. a table containing the eye color and the hair color of 25 individuals) improved conditional probability judgments.

It therefore appears that presenting people with the population occurrences, e.g. sampling, slides or tables of the individuals with their characteristics, is effective for improving judgments. People may not become better Bayesians, but this type of representation seems to improve problem solving. No adequate explanation has been formulated for this effect, other than the increased saliency of the base-rate information in the presentation format.

## 3.2. Training

A different approach to debiasing is to train individuals on how to construct more effective representations of problem situations. Cole (1989) tested performance when feedback was given with a contingency table, a graphical representation, or nothing other than the correct answer, in a disease diagnosis problem. After being tutored on how to use the representations, subjects had 16 trials where they were given a written problem and once they answered were given feedback on the correct answer. Afterwards, they were given a last problem in a superficially different written form. Subjects who had previously received graphical or tabular feedback were highly accurate. Although Cole argues that using alternate representations helped people build a better “mental model,” it remains unclear how people’s original mental model failed and consequently how these new representations induced different information processing. Furthermore, it is possible that Cole’s subjects did not learn to correctly process the information in this situation, but were merely adjusting their responses according to the feedback, phenomenon described earlier as “focusing” (Fischhoff and Bar-Hillel 1984).

Lichtenstein and MacGregor (1984) gave subjects either a fill-in-the-blanks algorithm that brought subjects step by step to the correct solution or a tutorial based on a $2 \times 2$ contingency table. The algorithm gave the basic steps to calculate the required probability whereas the tutorial gave explanations as to the rationale behind these calculations after presenting the four categories of outcomes (true positives, true negatives, false positives, false negatives). Although all subjects performed well when using these support tools, the algorithm group failed to transfer the technique to a second unaided problem. The tutorial group, however, made better judgments in the second problem (31% gave correct answers and only 9% gave the diagnostic information).

In both Cole and Lichtenstein and MacGregor's experiments, subjects were trained to use different representations of the problem, and then told how to process the information correctly, i.e., groups learned to create a table or a graph before proceeding with the calculations. The training conditions, because they manipulate problem representation and problem solving, affected two aspects of the judgment process. Whether the trained groups performed better because they used a table or because subjects learned how to use the correct numbers for the calculations, or both, remains confounded. Furthermore, training can be made more effective when we know what subjects have to learn. As mentioned earlier, it appears that people do have the capacity to resolve these problems in certain contexts. It is possible that an intervention at the representation-building level alone is sufficient to bring about the improvements in performance.

## 3.3. Replacing the Decision Maker with a Model

A simple method for improving decisions in a Bayesian probability updating would be to integrate the correct computation into a decision support system. If a particular decision-making context is repetitive and the necessary calculations are well defined, then using a model would ensure accuracy in the probability estimates. Wright (1983) compared mental computation with a Bayesian model using subjective probabilities, and found the model to be significantly more accurate.

Since improving user understanding of the decision-making process is important when using models (Elsaesser, 1989, Henrion & Morgan, 1985, Shortliffe et al., 1975), it will still be essential that the problem be presented in a way that will induce a good intuition about the sensibleness of the decision output. A more process-oriented perspective on people's understanding and information processing strategies in these problems will contribute to the development of acceptable explanations and consequently to the greater application of normative models in decision making.

## 4. Mental Representations

Our explanation for the base-rate fallacy is that people are misled by their inadequate mental representation of the problem, not by their ignorance of the base rate itself. In order to understand why people make mistakes in these types of problems, we start by looking at how these problem statements are mapped into mental representations. First, recall that we focus our attention on problems in which the description contains a base rate (e.g. 85% of the cabs are blue) and some unreliable event (e.g. a diagnostic test or a witness testimony, accurate 80% of the time). The basic feature of these problems is that although the identifying source is not perfectly reliable, the information it provides is perceived to be “caused” by the characteristics of the object under scrutiny. We believe that this causal inference dominates the mental representation of the problem situation.

![](/api/attachments/8EVFCSEH/fulltext/images/2b160493d873d5105140333087680506a298f0e25863aba0efbab822e80138e4.jpg)  
Causal order if a cab is blue, what is the probability that the cab will be identified as blue?  
Counter to causal order if a cab is identified as blue, what is the probability that it is blue?

Recent developments in cognitive psychology indicate that people naturally organize narrative information in terms of their causal relations. According to Murphy and Medin (1985) the meanings of concepts generally include: (1) their constituent features and (2) the probability of occurrence of these features. They also incorporate, when the information is available, (3) the causal relationships between those features, in an effort to provide an explanation for their mutual presence. A significant portion of a concept meaning resides in this understanding of the theoretical relationships that shape the internal structure of a situation. Vera (1991) goes further in showing that properties, correlations and relations that are seen as causally important to a class of entities also tend to be the most central—it is only when causal theories run dry that people will resort to feature similarity for categorization (i.e. based on probabilistic weights or correlations).

The role of causal relationships provides a potential explanation for judgments observed in base-rate problems. Consider our cab example. The witness's testimony can be inferred as caused by the initial color of the cab. For instance, as a member of the jury who is asked to ascertain the likelihood that the blue cab company is involved in the accident, I may reason in the following manner: (1) The witness is accurate 80% of the time; (2) the witness has seen the color of a cab; (3) the witness testifies that it was green (4) therefore there is an 80% chance that the cab is indeed green. A schematic of the activated mental representation is given in Figure 1.

By contrast, the correct reasoning process would follow steps such as: (1) The witness says it was green; (2) the witness is accurate 80% of the time; (3) given the distribution of taxis (85% blue and 15% green), the witness says green when in fact it is blue 17% of the time (20% of 85%) and green when it is actually green 12% of the time (80% of 15%); (4) the probability it is green when the witness says it is green is therefore 41% (12%/ $(12\% + 17\%)$ ). This process is much more complex, but also requires conceptualizing the problem in terms of true and false positives, which are not highlighted in the mental representation.

The representation in terms of the cause-effect link leads to a reasoning process that fits the perceived causal order, i.e. starting with the color of the cab, then evaluating the probability of its identification. Judgments of the type "If the cab was blue, what is the probability that the witness says it was blue, or green?" are easily derived. Questions flowing in the causal order pose no problem of interest. Questions flowing counter to the natural causal order, as it is perceived by subjects, show how mental representations interfere with judgment. The fact that people systematically answer 80% to the question "If the witness says the cab was green, what is the probability that it was in fact green?", whatever the distribution of cabs, shows that they fit the question to "their" causal theory, restating it in a more natural order, such as "If the cab was green, what is the probability that the witness says it was green?". There are empirical indications to this inversion error in prior research (Dawes 1986, Eddy 1982).

A causal mental representation provides a useful heuristic to interpret questions. In the absence of such a representation, a subject would have to store more information and to process more data every time a question is asked. The downside is that when a question doesn't fit the representation, the subject may fall into a logical trap. Therefore:

HYPOTHESIS 1. Subjects will make more errors related to question reinterpretation when: (a) their mental representation of a problem incorporates a causal linkage, and (b) the question runs counter to the perceived causal flow compared to when either (a) or (b) are absent.

The types of errors expected are as follows:

Inversion errors: Reinterpreting a frequency question such as "How many cabs are identified as blue and are in fact green" as "How many cabs are blue and identified as green." Subjects answer 17 instead of 3 (based on a sample of 100 taxis)

Base-rate fallacy: Reinterpreting the question "The probability that a cab identified as green is in fact green" as "The probability that a green cab is identified as green." Subjects answer 80% instead of 41%.

When no causal link is inferred from the problem narrative, judgments are more accurate, that is, closer to the normative answer. If no causal theory can be derived, people must resort to feature similarity for categorization. Hence, the problem representation highlights the set of possible outcomes, rather than only those which are related to a causal link. Consider the intercom problem, for instance, which is stated as follows: Eighty-five percent of the cabs in the city are blue, 15% are green. A wounded pedestrian testified that he remembered hearing the sound of an intercom. Intercoms are installed in 80% of the green cabs and in 20% of the blue cabs. What is the chance that the cab was green? (Bar-Hillel 1980); the representation would be as in Figure 2:

In this case, the mental representation may either be based on the cab concept, with links to color (blue of green) and intercom (absent or present), or on the four concepts of cabs varying on their features (Woods 1975). Both induce a mental representation of four mental entities and invoke the evaluation of the number of objects in each category. Note two things. First, when asked to determine the probability of finding a green cab equipped with an intercom, people will naturally compute the joint probability that a cab is both green and equipped with an intercom (12%). If asked “What is the probability that a cab equipped with an intercom is a green cab?” they must compute the probability of hearing an intercom (12% + 17%) in order to figure out the probability that a cab equipped with an intercom is green (41%). Second, the absence of causality eliminates the dominance of a particular order, thus making judgments of the type P (blue and intercom) just as easy as P (intercom and blue).

<table><tr><td colspan="3">Figure 2 Mental Representation of the Intercom Problem (Noncausal)</td></tr><tr><td></td><td>With intercom</td><td>Without intercom</td></tr><tr><td>A blue cab</td><td>A blue cab with intercom</td><td>A blue cab without intercom</td></tr><tr><td>A green cab</td><td>A green cab with intercom</td><td>A green cab without intercom</td></tr></table>

If judgment is impaired by the inappropriate inclusion of causal relations, one way to improve judgments in base-rate fallacy-generating contexts would be to help people build better mental representations, similar to those used in non-causal problems, i.e., which highlight the four object categories. Previous results have shown that representing the problem situation in terms of the population distribution, and visualizing the members' characteristics facilitates judgments of their probability of occurrence (Christensen-Szalanski and Beach 1982, Pollatsek et al. 1987). Therefore:

HYPOTHESIS 2. An external representation of the problem which illustrates object categories will facilitate judgments in questions that go counter to the causal order.

Two experiments were performed to explore the validity of the hypotheses formulated here. In a first phase, the information processing strategies in causal and non-causal problems is investigated (H1). In a second phase, we study the possibility of inducing more effective representations with the use of alternate information presentation modes (H2).

## 5. Empirical Investigation of the Mental Representation

In a first phase, we investigate the difficulties, or biases, in judgments by using a typical base-rate fallacy problem. The context is a light bulb factory in which good and bad bulbs coming out of the assembly line are submitted to a scanner for diagnosis. The problem is followed by a table which subjects are asked to fill out. The table details the problem in terms of the number of true positives, true negatives, false positives and false negatives expected in a sample of 100 (Figure 3). It therefore permits a more extensive analysis of how the information is used. As opposed to conditional questions, where subjects apparently ignore some information, filling out a table will require the use of all information. If indeed a causal mental representation dominates the way people make their judgments, more errors will be observed in questions which run counter to the causal order of events, and the order of events will not have an effect on the level of accuracy in problems without causal links (H1).

## 5.1. Experiment 1

Subjects. One hundred and seventy five (175) undergraduate students participated in this experiment and received class credit.

Materials. Two different problems were used:

Causal problem: In a light bulb factory, eighty-five percent (85%) of the light bulbs on the assembly line are OK; the remaining 15% are defective. A scanning device is used to put a red mark on the defective bulbs it spots on the line. The scanning device is known to be accurate in 80% of its markings. That is, when bulbs are defective, the scanner marks them red 80% of the time. When the bulbs are good, the scanner will mark them red 20% of the time.

Noncausal problem: In a light bulb factory, eighty-five percent (85%) of the light bulbs on the assembly line are OK; the remaining 15% are defective. The defective bulbs are red 80% of the time. The good bulbs are red 20% of the time.

Design. Sixty eight subjects were randomly assigned to control conditions, i.e., they were given the problem without a table (35 causal problem, 33 non-causal problem). The rest of the subjects were assigned to solve the problems where part of the task was to fill out a table.

Procedure. Subjects were run in groups of 2 to 4 and were given a sheet of paper containing the problem description and the table to fill out (except for those in the control groups). The table is illustrated in Figure 3, with questions stated "How many bulbs are marked red and are actually defective." Once they had completed the table, they were asked to estimate conditional probabil-

## Figure 3 Table for Light Bulb Problem

Suppose 100 light bulbs are randomly selected and given to the scanner. The scanner marks some defective and others not defective. Fill in the blanks in the following table so it will show the results we would expect to find:

<table><tr><td>Number of bulbs that are marked red and are actually defective</td><td>Number of bulbs that are marked red and are actually OK</td></tr><tr><td>Number of bulbs that are marked OK and are actually defective</td><td>Number of bulbs that are marked OK and are actually OK</td></tr></table>

Once you have filled out the table, answer the following questions:

What is the probability that a bulb marked red is actually defective?

What is the probability that a bulb marked OK is actually OK?

ities: $p(\text{defective} \mid \text{red})$ and $p(\text{not defective} \mid \text{not red})$ , i.e., "What is the probability that a bulb marked red is actually defective" and "What is the probability that a bulb marked OK is actually OK."

Measurement. The independent variables were manipulated through the causal link that could or could not be inferred in the problem (i.e. the causal or the non-causal problem), and the counter to causal order of the questions (table questions and conditional questions). Dependent variables were measured with the number and type of errors performed (inversions, i.e. correct numbers in incorrect table cells and base-rate fallacy answers). Since we had two conditional questions, we coded the answers as correct when at least one of them was correct. This facilitated coding and was based on the premise that the correct processing strategy was triggered.

Results. Table 1 shows the general distribution of responses for the two experimental groups and the two control groups. The results in the causal problem control group were very close to those found by Lyon & Slovic (1976) using a similar light bulb problem. The median and modal answers were both .80, the typical base-rate fallacy response, and the number of correct answers was very low (11%). Although the level of accuracy was also low in the non-causal problem control group (21%), the median response for the conditional questions was the correct estimate, and most errors (conjunction errors, i.e. the simple multiplication of base rate and diagnostic information) reflected the use of the base rates.

Table 1 Results of Experiment 1

<table><tr><td rowspan="2">Response</td><td colspan="2">Problem</td></tr><tr><td>Causal</td><td>Noncausal</td></tr><tr><td>Control Group</td><td></td><td></td></tr><tr><td>Conditional questions</td><td></td><td></td></tr><tr><td>Correct</td><td>11%</td><td>21%</td></tr><tr><td>Base-rate Fallacy</td><td>51%</td><td>18%</td></tr><tr><td>Conjunction</td><td>14%</td><td>18%</td></tr><tr><td>Others</td><td>24%</td><td>43%</td></tr><tr><td></td><td>(n = 35)</td><td>(n = 33)</td></tr><tr><td>Table Group</td><td></td><td></td></tr><tr><td>Table</td><td></td><td></td></tr><tr><td>Correct</td><td>60%</td><td>80%</td></tr><tr><td>Inversion</td><td>13%</td><td>4%</td></tr><tr><td>Others</td><td>27%</td><td>16%</td></tr><tr><td>Conditional questions</td><td></td><td></td></tr><tr><td>Correct</td><td>35%</td><td>52%</td></tr><tr><td>Base-rate Fallacy</td><td>44%</td><td>12%</td></tr><tr><td>Conjunction</td><td>8%</td><td>17%</td></tr><tr><td>Others</td><td>13%</td><td>19%</td></tr><tr><td></td><td>(n = 48)</td><td>(n = 59)</td></tr></table>

Inversion: Correct numbers in incorrect cells.  
Conjunction: Multiplication of base rate and diagnostic information (0.80 × 0.15 = 0.12)  
Base-rate fallacy: Only diagnostic information (0.80).

The distribution of table answers was significantly different between the causal and noncausal problems, when coded as correct, inversion, and others ( $\Delta G^{2} = 5.65, 2 df, p < 0.10$ ). Thirteen percent (13%) of incorrect tables in the causal problem were due to inversion errors, i.e. subjects gave the correct numbers but in the incorrect cells. This most common mistake provides some indication that a question such as "The number of bulbs that are marked red and are OK" is reinterpreted as "The number of bulbs that are defective and marked OK." Only 4% made this mistake in the non-causal problem. Other mistakes fall into a variety of categories, most of which are calculation errors. The distribution of answers to the conditional questions shows a significantly higher percentage of base-rate fallacy answers for groups with the causal problem (likelihood ratio statistic $^{1}$ using GLIM, 1986) ( $\Delta G^{2} = 23.24$ , 1 df, p < 0.001) than for the noncausal problem. The significant differences in the distribution of answers to both conditionals and table questions provide evidence for H1, that a causal link will dominate judgments and make counter-to-causal questions difficult.

Further analysis shows that the two groups with tables did not significantly reduce their percentages of base-rate fallacy answers ( $\Delta G^{2} = 1.64, 1 df, ns$ ) with respect to the two groups without tables, which suggests that tables do not help to reduce the bias. The tables do, however, improve general accuracy, as is shown by the larger number of correct answers in the table groups ( $\Delta G^{2} = 16.3, 1 df, p < 0.001$ ).

## 5.2. Discussion

Our hypothesis about the source of errors observed in base-rate problems stated that people tend to construct causal mental representations and these determine the way information is processed. Experimental results show that when causal relationships are present in problems, they impact accuracy in answering questions that do not fit the causal order. Be it in the table questions, such as “the number of bulbs that are marked red and are really OK” or in conditional questions “the probability that a bulb marked red is really defective,” the number of correct answers is lower and the most frequently observed errors suggest that the questions are reinterpreted to fit the causal order.

Figure 4 Tables and Graphs Used in the Pilot Experiment  
A)

<table><tr><td rowspan="2">TEST</td><td colspan="3">DISEASE</td></tr><tr><td>YES</td><td>NO</td><td>SUM</td></tr><tr><td>POSITIVE</td><td>12</td><td>3</td><td>15</td></tr><tr><td>NEGATIVE</td><td>17</td><td>68</td><td>85</td></tr><tr><td>SUM</td><td>29</td><td>71</td><td>100</td></tr></table>

B)

<table><tr><td rowspan="2">TEST</td><td colspan="3">DISEASE</td></tr><tr><td>YES</td><td>NO</td><td>SUM</td></tr><tr><td>POSITIVE</td><td>3</td><td>17</td><td>20</td></tr><tr><td>NEGATIVE</td><td>12</td><td>68</td><td>80</td></tr><tr><td>SUM</td><td>15</td><td>85</td><td>100</td></tr></table>

C)

<table><tr><td rowspan="2">TEST</td><td colspan="3">DISEASE</td></tr><tr><td>YES</td><td>NO</td><td>SUM</td></tr><tr><td>POSITIVE</td><td>12</td><td>17</td><td>29</td></tr><tr><td>NEGATIVE</td><td>3</td><td>68</td><td>71</td></tr><tr><td>SUM</td><td>15</td><td>85</td><td>100</td></tr></table>

A)  
![](/api/attachments/8EVFCSEH/fulltext/images/49653cf262bda2697f9ab8d0dbdffe4846dcd66470d3058edeaeb9d885a94011.jpg)

B)  
![](/api/attachments/8EVFCSEH/fulltext/images/d0f842ed25d5cf48396e2e37ed3115f5bcaf93434c1219a9db2ec49305c7db9e.jpg)

C)  
![](/api/attachments/8EVFCSEH/fulltext/images/151b52ca4837248dc55c7b9cc7d3bd6b9067ef424c50fb67959576c782a32c93.jpg)

□ patient who is OK

patient with disease

\+ positive test result

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

As we would expect, completing a table does help subjects think the problem through, in that it details the calculations needed to answer the conditional questions. In the non-causal problem control group, we observed that subjects tried to combine the base rate with the diagnostic information, but few did this accurately. With a table more than half gave at least one conditional estimate correctly. Therefore, a table may be an adequate decision making aid as long as the decision maker conceptualizes the problem as having four object categories. However, our results support the notion that subjects need to have formed an appropriate mental representation in order to identify the correct values.

## 6. Graphics as a Debiasing Tool

The objective of this second phase was to explore the possibility of “debiasing” judgments in situations where causality seems to dominate the reasoning process. Since the context is an nonmodifiable factor in real life decision making, helping people construct a more appropriate representation of causal problems may be the most fruitful avenue for debiasing efforts. This could be achieved by modifying the external representation of the information by highlighting object categories and occurrences. As previous research has indicated, presenting the population of occurrences helps construct a better mental representation for treating conditional “base-rate fallacy” type questions (Christensen-Szalanski and Beach 1982, Pollatsck et al. 1987, Cole 1989), and probably any other questions that go counter to the causal order. We chose a probability map similar to the one used by Cole (1989) because it is a simple way to illustrate object categories. Cole used three types of graphical representations and one kind of tabular representation and found them all to be equivalent in terms of feedback tools. However, compared to Cole, here there is no training involved. We aim to show that information display alone is enough to provide the proper mental model.

Before providing subjects with a graphical representation, it was important to establish the fact that subjects could recognize the correct depiction of the problem information in the graphics. The external representation must be considered legitimate for it to be used. A pilot experiment was performed where the problem was depicted with either tables or graphs (Figure 4). Subjects were asked to pick out the graph or table (among three) which correctly represented a disease diagnosis problem situation. Only 7 out of 17 subjects chose the correct table, whereas 13 out of 15 chose the correct graph ( $\Delta G^{2} = 5.38, 1 df, p < 0.05$ ). Interestingly, the most common mistake in the table condition was to select the table which represented the inversion observed in the previous experiment (7 out of 17 subjects). In the graph condition, only 2 out of 15 subjects selected the corresponding inverted graph. These results suggest the superiority of a graph to depict this situation and showed that most subjects can recognize the problem information in it.

Figure 5 Graphical Representation of Disease Problem  
![](/api/attachments/8EVFCSEH/fulltext/images/24589d4802f0b8d1eb97de8587619ec2a49c369b6b90f9eda0f3606451cd3b26.jpg)

An important issue is raised when a problem situation is to be presented with an alternate display format: Should the display be provided in addition to the traditional information format, in this case the full problem narration, or replace it? Since a causal representation seems robust and favored to other forms of mental representations, graphs presenting redundant information run the risk of being ignored. We therefore included two conditions in our experiment: one in which the graph is given in addition to the full problem description and another in which the graph contains information necessary for problem solving, and not presented elsewhere. With this second condition, we insured that all subjects would use the graph to solve the problem.

## 6.1. Experiment 2

Subjects. Four hundred fifty one (451) undergraduate students participated in this study. They were randomly assigned to one of three experimental treatments.

Materials. All subjects in this experiment were given a typical base-rate fallacy problem. We selected a disease diagnosis problem using the same base rate and diagnostic probabilities given in the lightbulb problem used earlier.

A medical center has developed a blood test to diagnose virulitis, a serious disease, in patients that are referred to the center after presenting abdominal pain, one of the associated symptoms. The center knows from experience that only 15% of all patients that present this pain actually have virulitis, the remaining 85% are OK. The blood test is known to be accurate in 80% of its diagnoses, whether the patient has the disease or not. That is, when a patient has virulitis, he or she receives a positive result 80% of the time. When the patient is OK, he or she gets a negative result 80% of the time.

In the second graph condition, the diagnosticity of the test was not given in the problem narrative. The second paragraph read as follows:

The blood test is known not to be wholly accurate in its diagnoses. That is, when a patient has virulitis, he or she may receive a negative test result. When the patient is OK, he or she may receive a positive result

Design. There were three groups: The first group (control) received the problem and a series of counter-to-causal questions. The first two questions were conditionals (What is the probability that a patient who scores positive on the test actually has the disease). Then four questions referred to the four categories of outcomes, as those given previously in the $2 \times 2$ tables (e.g. How many patients will receive a positive test result and actually have the disease?). The second group received a similar problem narrative and questions, but in addition had a graph depicting the four categories of outcomes (Figure 5). The third group had similar materials as the second group, with the exception of the problem narrative, which in this condition did not contain the diagnostic information.

Condition 1: Written problem only.

Condition 2: Written problem with graph.

Condition 3: Incomplete written problem with graph.

Procedure. Subjects were run in groups during class periods and were given a questionnaire containing the problem description and a series of questions to answer. The experimental conditions were randomly given to students in each class.

Measurement. Our independent variable was the presence or absence of a graph to represent the problem and with each graph, the presentation or not of the written diagnostic information. Dependent variables were measured with the number and type of errors performed (inversions, base-rate fallacy) in frequency or conditional questions, similarly to experiment 1.

Results. Table 2 shows the general distribution of responses for the three experimental groups. As predicted, the control condition generated a very high base-rate fallacy response rate (66%) and few accurate answers (1%). When a graph was presented to subjects, the number of correct answers increased (39%) and the base-rate fallacy decreased significantly (39%) ( $\Delta G^{2} = 22.1$ , 1 df., $p < 0.001$ ) compared to the control condition. However, the base-rate fallacy still remained a dominant error.

An even more dramatic improvement was observed in the third condition, where subjects were forced to consult the graph to find the necessary information. When a graph was presented without the diagnostic information in the problem description (graph-no diagnostic group), the accuracy of responses was improved significantly (61%) compared to the second condition (graph group) ( $\Delta G^{2} = 14.92, 1 df, p < 0.001$ ) and the base-rate fallacy was almost nonexistent (3%).

Table 2 also presents a general classification of responses given in the frequency questions (equivalent to those in the $2 \times 2$ table). The accuracy was very low in the control condition (7%). Interestingly, more subjects gave the correct numbers in an incorrect order (11%). Furthermore, out of the 15 inversions, 12 were of the same type as the most frequently observed in the first experiment, i.e., 12, 3, 17, 68 instead of 12, 17, 3, 68, the correct sequence. As noted previously, this suggests that because of a dominant causal mental representation such as “disease → diagnosis,” the question “How many patients who receive a positive test are actually OK” is interpreted as “patients who have the disease and are diagnosed as being OK.” Many subjects (33%) gave the diagnostic information or its complement (80% or 20%) instead of the actual number of cases (these errors are referred to as percentages in Table 2). In both graph conditions, answers were very accurate (71% and 81%). The research hypothesis is therefore supported by these results (H2).

Table 2 Results of Experiment 2

<table><tr><td rowspan="2">Response</td><td colspan="3">Groups</td></tr><tr><td>Control</td><td>Graph</td><td>GraphNo Diagnostic</td></tr><tr><td colspan="4">Conditional Questions</td></tr><tr><td>Correct</td><td>1%</td><td>39%</td><td>61%</td></tr><tr><td>Base-rate Fallacy</td><td>66%</td><td>39%</td><td>3%</td></tr><tr><td>Conjunction</td><td>15%</td><td>7%</td><td>8%</td></tr><tr><td>Others</td><td>17%</td><td>16%</td><td>29%</td></tr><tr><td colspan="4">Frequency Questions</td></tr><tr><td>Correct</td><td>7%</td><td>71%</td><td>81%</td></tr><tr><td>Inversion</td><td>11%</td><td>2%</td><td>1%</td></tr><tr><td>Percentages</td><td>33%</td><td>9%</td><td>0%</td></tr><tr><td>Others</td><td>49%(n = 148)</td><td>18%(n = 153)</td><td>18%(n = 150)</td></tr></table>

Inversion. Correct numbers in incorrect cells.  
Conjunction. Multiplication of base rate and diagnostic information (0.80 × 0.15 = 0.12)  
Base-rate fallacy. Only diagnostic information (0.80).  
Percentages Only diagnostic information, in percentages (80% or 20%).

## 6.2. Discussion

We hypothesized that, because causality dominates and biases people's judgments, graphics would help build a more effective mental representation of the problem. The graph eliminates irrelevant causal cues and permits the visualization of population occurrences. Our results support the contention that an external representation which illustrates object categories improves the way people process the information in the problem. The simple presentation of a graph reduced the bias' occurrence and improved response accuracy.

We found, however, that the highest proportion of correct answers is obtained when the diagnostic information is not specified in the verbal problem description. Our explanation is that when people read the problem and have all the necessary information, they will create their representations and work with them when answering the questions. The graph presents redundant information and therefore requires an additional cognitive effort that may not be judged as needed. Also, the cognitive theories on conceptualization (Murphy and Medin 1985, Vera 1991) suggest that causality dominates over categorization. Subjects may have been more comfortable with their causal representations of the problem than with the graph. Therefore, the most effective way to get people to use graphs and to debias their judgement is for the graph to have information that they cannot find elsewhere.

## 7. Conclusion

## 7.1. Summary of Results

Base-rate fallacy has been described as a generalized tendency to ignore base rates in favor of more specific evidence (Bar-Hillel 1980). Because the answers to many Bayesian problems seem to indicate that people neglect base rate information, researchers have concentrated their efforts on trying to explain why people believe that this information is unimportant for the judgment at hand. Similarly, debiasing efforts have focused mainly on trying to have people recognize the impact of base rates, e.g., by making them more salient (Fischhoff et al. 1979, Fischhoff and Bar-Hillel 1984) or by training them to use Bayes' rule (Cole 1989). These efforts have had limited success, either because they did not improve people's understanding or they were time consuming. We argue that the limited knowledge about the cognitive processes underlying the bias has undermined efforts to develop useful decision aids.

Our first objective was to identify the "biasing" process. In order to do this, we decomposed the problem and attempted to pinpoint the difficulties faced by subjects in these typical base-rate fallacy problems. Our first hypothesis stated that subjects would have difficulty in answering questions that went counter to the causal order of events that dominated their mental representations. Results supported this hypothesis. Subjects made more mistakes when questions did not fit the causal order in the problem description. Also, the type of errors they made suggests that they reinterpret questions to fit the causal order.

Our second research objective was to explore the possibility of inducing a more effective mental representation by modifying the presentation format. The underlying theory contends that better performance is achieved when the representation highlights categories of objects and reduces irrelevant causal cues. The results of a second experiment provide support for this theory. When subjects were given a graph (a probability map), their answers were significantly improved, and base-rate fallacy was reduced. This improvement was even more dramatic when not all the information could be found in the problem narrative (in which case subjects were forced to use the graph).

## 7.2. Implications for Decision Support System Design

Among previous debiasing attempts, the most effective techniques were the ones which modified the external problem representation, such as slides, tables or graphs. Since the bias appears to originate from a particular mental representation of the problem, it seems sensible that these tools would have a positive impact on performance.

In our research, we shed some light on this issue, first by determining the dysfunctional characteristics of the mental representations people use, which establishes a foundation for determining the required features in alternative information presentation modes. It seems that an important characteristic of a more effective representation is its absence of causal cues. It also appears that the capability to visualize the population characteristics and/or the interaction between these characteristics is also an important feature. Of course, both the absence of causality and the capability to visualize features of objects are closely associated since two features presented simultaneously reduces the possibility of perceiving them as one causing the other in a temporal framework.

Graphics may be one of the superior forms of representation because they illustrate feature interactions (which are not as clearly perceptible in contingency tables) and they are easy to create and use (as opposed to slides or tables of occurrences). We believe that they should become critical elements in DSS design for probabilistic reasoning:

a) As Representational Aids. As we have seen, Bayesian reasoning in an unaided decision environment can bring about systematic biases in judgments. In the aided case, the person will develop an understanding and representation of the problem as depicted by an appropriate external representation. Representations such as graphics help the problem solver visualize the situation in terms of the possible outcomes, and extract the information relevant for the judgment to be made. One problem discovered when performing these studies is the reduced effectiveness of graphs when people already possess the necessary information to solve the problem. This has important implications for the general design of representational aids. If decision makers are familiar with the situation, they may not feel the need for, and consequently not use alternate presentation modes. Representational aids will therefore be more effective through directed change design (Silver 1990), i.e. restricting the retrieval of information to formats of presentation that are most apte to reduce judgment biases. Restrictiveness should be used with caution, however, since we know that “focusing techniques” can superficially correct judgments, but have little impact on the decision maker’s understanding (Fischhoff and Bar-Hillel 1984).

b) As Explanation Tools. The use of normative models in decision support would significantly improve the treatment of information dealing with uncertainty, because of the pervasive errors people exhibit in this context. The primary factor impeding the use of these models seems to be that they are difficult for users to understand. When normative probability estimates differ from the user's subjective estimates, the decision aid's problem-solving process may be questioned. Since graphs which illustrate the problem situation appear to be recognized as legitimate (pilot experiment), their use in explanations should increase the acceptability of recommended solutions.

## 7.3. Implications for Future Research

Developing a better understanding of how people build and use mental representations is critical to specifying debiasing tools. When researchers attempt different debiasing interventions through trial and error, results show some tools that work, others that don't. Most often it is not very clear how those that are effective change the way people process the information. We need to get a better grasp of the underlying cognitive processes in decision making in order to build a body of knowledge on appropriate debiasing tools. This may not only mean that researchers in the decision support area acquaint themselves with the a body of knowledge from other disciplines such as cognitive psychology, but also develop this knowledge to make it relevant and useful for decision support development.

There remains a significant number of issues that need clarification, both in understanding the process underlying the base-rate fallacy and in the way representational aids affect decision processes. We know very little about how mental representations are constructed and used. Procedures using protocol analysis and cognitive modeling may give us important and generalizable insights into human information processing characteristics and limitations in situations where systematic errors are made in simple problems. In particular, pinpointing the role of causality in conceptual representation may help develop a better understanding of the way people interpret and process decision-making situations where causal cues are present.

Although this research was specifically focused on the base-rate fallacy, the results may be generalized to other types of problems, and to other judgment biases. For instance, we would expect that graphs would help improve judgment accuracy in other situations where causality or temporal order appear to dominate (e.g., the evaluation of conditional probabilities described by Tversky and Kahneman (1980). More research is needed to define the mental representations people use in these contexts, and to verify the potential usefulness of alternate information presentation modes to support these decisions. $^{2}$

Lyne Bouchard, the associate editor, and three anonymous reviewers for comments on earlier versions of this paper. The research was partially supported by grants from the Social Sciences and Humanities Research Council of Canada.

## References

Ajzen, I., "Intuitive Theories of Events and the Effects of Base-rate Information on Predictions," J. Personality and Social Psychology, 35 (1977), 303–314.

Bar-Hillel, M., "The Role of Sample Size in Sample Evaluation," Organizational Behavior and Human Performance, 24 (1979), 245–257.

——, "The Base-rate Fallacy in Probability Judgments," Acta Psychologica, 44 (1980), 211–233.

—, "The Base-rate Fallacy Controversy," Decision Making Under Uncertainty, R. W. Scholz (Ed.), Elsevier Science Publishers B. V., North Holland, 1983, 39–61.

Beyth-Marom, R. and H. R. Arkes, "Being Accurate but Not Necessarily Bayesian: Comment on Christensen-Szalanski and Beach," Organizational Behavior and Human Performance, 31 (1983), 255–257.

Bishop, Y. M. M., S. E. Fienberg, and P. W. Holland, Discrete Multivariate Analysis: Theory and Practice, MIT Press, Cambridge, MA, 1975

Christensen-Szalanski, J. J. J. and L. R. Beach, "Experience and the Base-rate Fallacy," Organizational Behavior and Human Performance, 29 (1982), 270–278.

Cole, W. G., "Understanding Bayesian Reasoning via Graphical Displays," CHI'89 Proceedings, ACM Press, Austin, TX, 1989.

Coll, R. A., J. H. Coll, and G. Thakur, "Graphs and Tables: A Four-factor Experiment," Comm. ACM, 37, 4 (1994), 77-86.

Dawes, R. M., "Representative Thinking in Clinical Judgment," Clinical Psychology Review, 6 (1986), 425–441.

Desanctis, G., "Computer Graphics as Decision Aids: Directions for Research," Decision Sciences, 15 (1984), 463–487.

Eddy, D. M., "Probabilistic Reasoning in Clinical Medicine: Problems and Opportunities," in Judgment Under Uncertainty: Heuristics and Biases, D. Kahneman, P. Slovic and A. Tversky (Eds), Cambridge University Press, 1983, 249–267.

Eggleston, R., Evidence, Proof and Probability, Weidenfeld and Nicolson, London, 1983.

Elsaesser, C., "Explanation of Bayesian Conditioning for Decision Support Systems," Doctoral Dissertation, Carnegie Mellon University, Pittsburgh, PA, Dissertation Abstracts International, Vol. 50, 10A, 1989.

Fischhoff, B. and M. Bar-Hillel, "Focusing Techniques: A Shortcut to Improving Probability Judgments?", Organizational Behavior and Human Performance, 34 (1984), 175–194.

—, P. Slovic and S. Lichtenstein, "Subjective Sensitivity Analysis," Organizational Behavior and Human Performance, 23 (1979), 339–359.

Gigerenzer, G., W. Hell, and H. Blank, "Presentation and Content: The Use of Base Rates as a Continuous Variable," J. Experimental Psychology, 1, 3 (1988), 513–525

Ginosar, Z. and Y. Trope, "The Effects of Base Rates and Individuating Information on Judgments About Another Person," J. Experimental and Social Psychology, Vol. 16 (1980), 228–242.

Hamm, R. M., "Accuracy of Probabilistic Inference Using Verbal vs. Numerical Probabilities," Psychonomics Society Meetings, Chicago, IL, 1988.

Henrion, M. and M. G. Morgan, "A Computer Aid for Risk and Other Policy Analysis," Risk Analysis, 5, 3 (1985), 195–208.

Jarvenpaa, S. L., "The Effect of Task Demands and Graphical Format on Information Processing Strategies," Management Sci., 35, 3 (1989), 285–303.

Joyce, E. and G. Biddle, "Are Auditors' Judgments Sufficiently Regressive?", J Accounting Res., 19, 2 (1981), 323–349.

Kahneman, D. and A. Tversky, "On the Psychology of Prediction," Psychological Review, 80 (1973), 237–251.

—, P. Slovic and A Tversky (Eds.), Judgment Under Uncertainty. Heuristics and Biases, Cambridge University Press, Cambridge, MA, 1982.

Lichtenstein, S. and D. MacGregor, "Structuring as an Aid to Performance in Base Rate Problems," Technical Report 84-16, Decision Research, Eugene, OR, 1984.

Loy, S. L., "The Interaction Effects Between General Thinking Skills and an Interactive Graphics-based DSS to Support Problem Structuring," Decision Sciences, 22 (1991), 846–868.

Lyon, D. and P. Slovic, "Dominance of Accuracy Information and Neglect of Base Rates in Probability Estimations," Acta Psychologica, 40 (1976), 287–298.

Murphy, G L. and D. L. Medin, "The Role of Theories in Conceptual Coherence," Psychological Review, 92 (1985), 289–316.

Payne, C. D. (Ed.), The GLIM (Generalized Linear Interactive Modeling) System Manual, Release 377, Numerical Algorithms Group, Downer's Grove, IL, 1986.

Polk, Thad A., Verbal Reasoning, School of Computer Science Tech Report CMU-CS-92-178, Pittsburgh, PA, 1992.

Pollatsek, A., A. D. Well, C. Konold, P. Hardiman and G. Cobb, "Understanding Conditional Probabilities," Organizational Behavior and Human Decision Processes, 40 (1987), 255–269.

Pracht, W. E. and J. F. Courtney, "The Effects on an Interactive Graphics-based DSS to Support Problem Structuring," Decision Sciences, 19, 3 (1988), 598–621.

Shortliffe, E., R. Davis, S. Axline, B. Buchanan, C. Green, and S. Cohen, "Computer Based Consultations in Clinical Therapeutics: Explanation and Rule Acquisition Capabilities of the MYCIN System," Computers and Biomedical Res., 8 (1975), 303–320.

Silver, M., S., "Differential Analysis for Computer-based Decision Support," Doctoral Dissertation, University of Pennsylvania, Philadelphia, PA, 1986.

—, "Decision Support Systems: Directed and Non-directed Change," Information Systems Res., 1, 1 (1990), 47–70.

Simon, H. and J. R. Hayes, "Psychological Differences Among Problem Isomorphs," reprinted in Models of Thought, Yale Univ. Press, New Haven, CT, 1977.

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Tan, J. K. H. and I. Benbasat, "Processing of Graphical Information: A Decomposition Taxonomy to Match Data Extraction Tasks and Graphical Representations," Information Systems Res., 1, 4 (1990), 416–439.

— and —, "The Effectiveness Graphical Presentation for Information Extraction: A Cumulative Experimental Approach," Decision Sciences, 24 (1993), 167–191.

Todd, P. and I. Benbasat, "An Experimental Investigation of the Impact of Computer Based Decision Aids on Decision Making Strategies," Information Systems Res., 2, 2 (1991), 87–115

— and —, "The Use of Information in Decision Making: An Experimental Investigation of the Impact of Computer-based Decision Aids," MIS Quarterly, 16, 3 (1992), 373–395.

Tversky, A. and D. Kahneman, "Causal Schemas in Judgments Under Uncertainty," in M. Fishbein (Ed.) Progress in Social Psychology, Erlbaum, Hillsdale, NJ, 1980.

— and —, "Evidential Impact of Base Rates," in Judgment Under Uncertainty; Heuristics and Biases, Cambridge University Press, Cambridge, England, 1982.

Vera, A H, "Concepts and Causation," doctoral dissertation, Cornell University, Ithaca, NY, Dissertation Abstracts International, 51, 12B, 1991.

Vessey, I., "Cognitive Fit. A Theory-based Analysis of the Graphs versus Tables Literature," Decision Sciences, 22 (1991), 219–240.

— and D. Galetta, "Cognitive Fit: An Empirical Study of Information Acquisition," Information Systems Res., 2, 1 (1991), 63–85.

Woods, W. A., "What's in a Link: Foundations for Semantic Networks," in D. G. Bobrow, A Collins, (Eds.), Representation and Understanding: Studies in Cognitive Science, Academic Press, New York, 1975, 35–82.

Wright, W., "An Empirical Test of a Bayesian Decision Support Procedure in a Financial Context," International Conference on Information Systems Proceedings, Houston, TX, 1983.

Zachary, W., "A Cognitively Based Functional Taxonomy of Decision Support Techniques," Human-Computer Interaction, 2 (1986), 25–63.

—, "Decision Support Systems: Designing to Extend the Cognitive Limits," in Handbook of Human-Computer Interaction, Elsevier Science Publishers B.V., North-Holland, Amsterdam, 1988.

Izak Benbasat, Associate Editor. This paper was received on August 26, 1993, and has been with the authors 14 months for 3 revisions.
