---
otero_id: 25234
otero_key: "V8GPM6K9"
title: "Profiling Web Usage in the Workplace: A Behavior-Based Artificial Intelligence Approach"
authors: ""
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045711"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Profiling Web Usage in the Workplace: A Behavior-Based Artificial Intelligence Approach

Murugan Anandarajan

To cite this article: Murugan Anandarajan (2002) Profiling Web Usage in the Workplace: A Behavior-Based Artificial Intelligence Approach, Journal of Management Information Systems, 19:1, 243-266, DOI: 10.1080/07421222.2002.11045711

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045711

![](/api/attachments/V8GPM6K9/fulltext/images/8f219598b82fcb26a9194649d3ab66bae4bbae54f65ff3e0641d922f2f7f5e8c.jpg)

Published online: 23 Dec 2014.

![](/api/attachments/V8GPM6K9/fulltext/images/22cbdc4a7062e411c5327ae2d8e3d5c60ba0063b06ce4b0cb52066b78339c595.jpg)

Submit your article to this journal

![](/api/attachments/V8GPM6K9/fulltext/images/2cc32dd24ccbf9eded1c426b4f5e719d0927a2efaa7c47a87d3f80d469ca5c3a.jpg)

Article views: 51

![](/api/attachments/V8GPM6K9/fulltext/images/d6902e6c5d4f537924f2ffb6e6173cae203fbb18dd9100339fad68c44a353f63.jpg)

View related articles

![](/api/attachments/V8GPM6K9/fulltext/images/91d209cbf98f9b58fc171284d6d62c342e59c1fce40e11be7eb3c12f194c7459.jpg)

Citing articles: 6 View citing articles

# Profiling Web Usage in the Workplace: A Behavior-Based Artificial Intelligence Approach

MURUGAN ANANDARAJAN

MURUGAN ANANDARAJAN is an Associate Professor of Management Information Sys tems in the Department of Management at Drexel University. His current research interests include artificial intelligence-based classification systems in glaucoma and high-risk businesses scenarios, artificial life, and Internet usage. His research has appeared in journals such as Behaviour and Information Technology, Communication of the ACM, Computers and Operations Research, Decision Sciences, Information and Management, Journal of International Business Studies, and Omega-International Journal of Management Science, among others. Dr. Anandarajan is a coeditor of the book Internet Usage in the Workplace: A Social, Ethical and Legal Perspective (Idea Group Publishing, 2001), and editor of a special section on “Web Abuse in the Workplace” in the Communications of the ACM (January 2002).

ABSTRACT: Employees’nonwork-related Web surfing behavior results in millions of dollars of expenditure for organizations. This paper proposes the use of a behaviorbased artificial intelligence system to profile employee Web usage behavior. Two artificial neural networks (ANN) incorporating genetic algorithm techniques were developed for this purpose. The system was validated with two different data sets. The classification performance of the neural network models was compared to that of a statistical method. The results indicate that one of the ANN models, namely the simple recurrent network, was a superior classifier for this behavior-based problem. In addition, the uncertainty inherent in such classification decisions was examined with a loss matrix, and the holdout samples were reclassified using a loss matrix. The output of this intelligent system can be highly beneficial to managers in designing effective Web management policies.

KEY WORDS AND PHRASES: artificial neural networks, classification models, genetic algorithms, loss matrix, misclassification rate, profiling, Web usage.

THE UBIQUITOUS NATURE OF THE World Wide Web (commonly known as the Web) is dramatically revolutionizing the manner in which organizations and individuals alike acquire and distribute information. The International Data Group forecasts that the number of Web users worldwide will reach 1 billion by 2005 [40]. Studies also indicate that in the United States alone, Web commerce will account for approximately \$6.9 trillion by 2004 [12].

In addition to being a channel for commercial exchange, the Web also provides employees access to the world’s largest playground. This fact was highlighted in a Newsweek article headline that read “The Internet Has Brought Distractions into Cubicles, and Now Corporate America Is Fighting Back” [38]. Workplace Web users, however, may not view this as a potential problem. The sentiments of users on this issue were reflected in a succinct comment made by an employee in an interview with the author:

Looking up a work-related news story easily leads to checking the baseball standings or a movie review. It will only take a couple of seconds, right? A couple of seconds is no big deal in the greater scheme of things.

The problem, however, is that seconds turn to minutes, and these minutes add up to hours. A study conducted in a manufacturing firm found that in a typical eight-hour workday, over 250,000 Web sites were accessed by a workforce of 386 employees. Of particular concern to the organization was the discovery that approximately 90 percent of the accessed sites were nonwork-related [30]. Research by the Aberdeen Research Group [57] indicates that employees can squander anywhere from 30 minutes to three hours a day on nonwork Web-related activities.

The cost of ignoring this phenomenon can be enormous. A study conducted by the American Management Association found that such activities could cost billions of dollars a year in lost productivity [37]. In addition, such usage leads to increased security costs and network overload, as well as the risk of civil and criminal liability. These issues have prompted organizations to show a growing interest in understand ing and managing Web usage behavior in the workplace [14, 36].

Organizations respond to this growing issue in a variety of ways. Monitoring can vary from a laissez-faire attitude, where little is done to address this issue, to the other extreme of blocking Web sites that have no connection to work-related duties. However, an overzealous policy can be just as harmful as a nonexistent one. For instance, stringent blocking can hamper an employee’s use of the Web as a vital tool for business purposes. Thus, it is not surprising that approximately 73 percent of organizations have only acceptable usage policies or no restrictions at all [57].

The literature in Web security recommends that organizations should create socialization programs, which would lead to the modification of their employees’ Web usage behavior [34]. However, a fundamental problem facing Internet security managers is identifying the Web usage behavior of employees, a priori. A review of the information systems (IS) literature indicates that there are no established guidelines for selecting employees for such programs. This implies that managers have to rely on their judgment to make such decisions. This can be precarious since such multicue judgments are inherently difficult for decision-makers [29].

This study proposes the use of an artificial intelligence-based model (in terms of artificial neural networks and genetic algorithms) to assess and classify employees by their Web usage behavior. Based on an operational definition of Web usage behavio [4], individuals were classified as high nonwork users (if they achieved a high score on accessing nonwork-related Web pages such as arts and entertainment, travel and leisure, living/consumer, and sports/news) and low nonwork users if they attained a low score on accessing these types of Web pages.

The output of this intelligent system can be extremely beneficial to managers in the development of cognitive training and socialization programs. Such programs are vital for the modification of employees’ behavior and attitudes toward Web usage [34]. Thus, this decision tool will aid managers in designing effective Web management.

## Behavior-Based Artificial Intelligence

IN THE LAST FEW DECADES, THE FIELD OF artificial intelligence (AI) has focused almost exclusively on problems of identifying, formalizing, and representing knowledge. This classical or traditional AI approach (also known as knowledge-based AI) defines intelligence in terms of knowledge, which is based on Newell’s principle of rationality.

In recent years however, the AI community has begun to stress the importance of embodied intelligence within these systems. This movement has been referred to as the behavior-based AI approach [48]. This approach defines intelligence in terms of observed behavior—that is, understanding common behavior through the construction of artificial systems—which account for the environmental pressures on the selfpreservation of the system [47]. Researchers have used artificial neural networks (ANN) to design such behavioral-based systems in order to stay close to plausible biological structures [5, 41].

## Artificial Neural Networks

An ANN is a parallel, dynamic system of highly interconnected and interacting parts based on the principles of neurobiological models. ANNs have at least two potentia strengths over the more traditional model-fitting techniques such as regression [10]. First, ANNs are capable of detecting and extracting nonlinear relationships and interactions among predictor variables. Second, the ANN’s inferred patterns and associated estimates of precision do not depend on any assumptions relating to the distribution of the variables.

Similar to the biological structure of the human brain, the fundamental building block of an ANN is the neuron. As illustrated in Figure 1, the artificial neuron receives a multitude of inputs that represent the attributes or stimuli in a data set. Through the use of a learning algorithm, the optimal connection weights, which represent both the strength and nature of the connection between neurons, are determined. These weights are then applied to each input and the weights and the inputs are aggregated. An activation function $( F )$ is then applied to the aggregated value to produce an output for a single neuron as

$$
o = F \left(\sum_ {i = 1} ^ {n} x _ {i} w _ {i}\right),
$$

![](/api/attachments/V8GPM6K9/fulltext/images/a9defce23892f212ddf656056068e50d827061f1dd71aa5db6b5bd9c701df28d.jpg)  
Figure 1. The Functioning of an Artificial Neuron

Activation functions are needed to introduce nonlinearity into the network. The selection of the activation function depends on the nature of the input data and objective of the network [22]. Since one of the objectives of this study is to interpret the final outputs of the neural network as posterior probabilities for a categorical target variable, the softmax function [10, 23, 35] was used. This is defined as

$$
y _ {k} = \frac {\exp (\mathrm{net} _ {k})}{\sum_ {k} \exp (\mathrm{net} _ {k})},
$$

where $k = 1 , . . . , k ,$ , and

$$
\mathrm{net} _ {k} = \sum_ {j} w _ {j k} z _ {j},
$$

where $z _ { j }$ is the output of neuron j in the hidden layer, and $w _ { j k }$ is the output of neuron k in the output layer.

This study compares the predictive ability of two ANN topologies to profile Web usage behavior. The first topology, the multilayer perceptron, is based solely on feed forward connections, whereas the second topology, the simple recurrent networks, is based on both feedback and feed-forward connections. These network topologies are described briefly below.

The multilayer perceptrons (MLP) topology is one of the most widely implemented neural network architectures. In its simplest form, this network has a three-layer, feed-forward, hierarchical structure. The complexity of the network, in terms of ar chitecture, influences the levels of accuracy achieved by the model. A typical MLP is shown in Figure 2.

One of the traditional weaknesses of the MLP network is its inability to fill in patterns due to its complete reliance on feed-forward connections. For instance, if part of the input pattern applied in the network is missing or corrupt, larger errors will be propagated through the network to the output. For a behavior-based system to be more effective, an ANN with feedback loops and additional sensors would be necessary. One such ANN topology is called the simple recurrent network (SRN).

![](/api/attachments/V8GPM6K9/fulltext/images/e49dfdcdeeb42819461276456557955d5b7f77beb9eaa96f905ad77d3bc5d707.jpg)  
Figure 2. General Structure of the Multilayer Perception Network Topolog

The SRN topology has a small number of neurons in the input layer, which receive feedback signals from the hidden layer. These self-excitatory units, which act as sensors, are commonly referred to as context units, and are very common in the natural neural networks of the brain. A context unit is defined as “an input layer unit in a simple recurrent net that receives information from hidden units” [21]. These units remember past activity and are useful when the past value of the network influences present information processing.

As illustrated in Figure 3, in the SRN topology, the output of the hidden layers from the previous time step are copied to the context units $( \mathbf { C } _ { I } , . . . , \mathbf { C } _ { p } )$ in the input layer. In addition, the context units are locally recurrent (that is, they feed back to themselves). The network combines the past values of the context units with the present inputs to obtain the present net output. The use of feedback connections in the simple recurrent model makes it less sensitive to noise and lack of synchronization. In addition, it also permits the network to learn at a faster rate than the feed-forward network [46].

![](/api/attachments/V8GPM6K9/fulltext/images/13240a610b87abdce5fd26c0c1155b0bc769fbb14d25ddd5cc81ca58dcdd1935.jpg)  
Figure 3. General Structure of the Simple Recurrent Network Topology.

## ANN Learning Algorithms

As discussed earlier, each connection in the ANN has a weight, which is initially generated from random numbers ranging from {–1 to 1}. The output value of a neuron is a function of the weighted sum of its inputs. A large positive input to the neuron will activate it (that is, the output of the neuron will be close to one), whereas a large negative input will inhibit it (that is, the output of the neuron will be close to zero). Determining the network weights is a critical component of the learning process. These weights are generated by an iterative training process, where case examples with known outputs are repeatedly presented to the network. A commonly used learning method in neural networks is the back propagation algorithm, which relies on gradient techniques for network training [55]. However, research has shown that back propagation may not necessarily provide the best and fastest way to train neural networks [6, 15, 32].

This study uses an alternate approach to learning—that is, selectionism—where a complete behavior system is generated by an evolutionary process. Evolutionary development has been shown to be an extremely important source for generating more complexity in systems [42]. It has also been proposed by neurobiologists to be the major mechanism underlying new functionality in the brain [11]. One such selectionis technique is called genetic algorithms (GA).

GA is a stochastic heuristic optimization search technique that is designed after the natural selection process followed in biological evolution, that is, it follows the nature of sexual reproduction in which the genes of two parents combine to form those of their offspring. This method has been shown to perform well in obtaining globa solutions for difficult nonlinear functions [5, 6]. This generate-and-test strategy identifies and exploits regularities in the environment, and converges on solutions that are globally optimal or nearly so.

When the GA is applied to determine the weights of an ANN, an initial population of chromosomes (which in this study are the weights), representing possible solutions to a problem, is created. Each set of chromosomes is represented by a sequence of genes. The fitness function determines the potential of a chromosome as a possible solution by evaluating the chromosome with respect to an objective function. Each of these individuals has certain characteristics that make them more or less fit as members of the population. The fittest chromosomes will have a higher probability of mating than lesser-fit members to produce progeny that have a significant chance of retaining the desirable attributes of their parents. For a more detailed description of genetic algorithms [5, 6, 7, 9].

## Methodology

## Data Collection

THE DATA USED IN THIS STUDY WAS COLLECTED using a survey instrument, which was mailed to a random sample of 1,500 alumni of a university in the Northeastern United States. Participation in the study was voluntary and the potential respondents were assured that their responses would be kept confidential. There were 325 surveys returned within two weeks, and another 170 received within a month after a follow-up postcard was mailed. After discarding 50 surveys because of incompleteness, there were 445 usable surveys. The participation rate was consistent with other studies, where potential respondents were not screened for their willingness to take part in a survey [45]. Of the 445 individual responses, 334 had Web access at work. Of this sample, however, only 154 reported using the Web at work. Table 1 summarizes the characteristics of the samples used in this study.

## Variable Selection

The choice of input variables used in the classification models is an important consideration in the design of the neural networks. Based on previous IS literature, predictors of Web usage behavior—low nonwork-related usage and high nonwork-related usage, was classified using 1-of-C coding, that is, each dummy variable was given the value zero except for the one corresponding to the correct category, which was given the value one. Web usage behavior was analyzed with regard to nine characteristics (that is, nine input neurons). The variables include motivational factors such as perceived enjoyment [18, 33, 53] and perceived usefulness [1, 17, 18]; skill factors such as experience [16, 20, 28]; formal/self-training [3, 27, 43]; as well as task structure [51, 52], gender [24, 25], education, and income. Table 2 provides a summary of these input variables and its corresponding measurement instrument. Univariate analysis was performed to determine whether the data consisted of the two groups of Web users. As can be observed from the t-values in Table 3, the variables for both groups were statistically significant with the exception of education. The lack of significance of the education variable could be attributed to the fact that the sample consisted of users with similar educational background. Table 4 provides the correlation matrix of the variables as well as the reliability of the measures, all of which were greater than the threshold criteria suggested by Nunnally [39].

Table 1. Respondent Profiles

<table><tr><td>Demographics</td><td colspan="2">Sample 1n = 154</td><td colspan="2">Sample 2an = 163</td></tr><tr><td>Gender</td><td></td><td></td><td></td><td></td></tr><tr><td>Male</td><td>97</td><td>63.00%</td><td>99</td><td>60.72%</td></tr><tr><td>Female</td><td>57</td><td>37.00%</td><td>64</td><td>39.28%</td></tr><tr><td>Age</td><td></td><td></td><td></td><td></td></tr><tr><td>20–30</td><td>32</td><td>20.60%</td><td>99</td><td>60.89%</td></tr><tr><td>31–40</td><td>49</td><td>31.50%</td><td>49</td><td>29.87%</td></tr><tr><td>41–50</td><td>41</td><td>26.60%</td><td>11</td><td>6.76%</td></tr><tr><td>51–60</td><td>24</td><td>15.40%</td><td>4</td><td>2.48%</td></tr><tr><td>over 60</td><td>9</td><td>5.90%</td><td>0</td><td>0.00%</td></tr><tr><td>Size of business</td><td></td><td></td><td></td><td></td></tr><tr><td>1–999 employees</td><td>76</td><td>49.30%</td><td>99</td><td>61.10%</td></tr><tr><td>1,000–9,999</td><td>40</td><td>25.70%</td><td>38</td><td>22.95%</td></tr><tr><td>over 10,000</td><td>39</td><td>25.00%</td><td>26</td><td>15.95%</td></tr><tr><td>Current position</td><td></td><td></td><td></td><td></td></tr><tr><td>Top-level manager</td><td>27</td><td>17.50%</td><td>13</td><td>8.30%</td></tr><tr><td>Middle-level manager</td><td>30</td><td>19.60%</td><td>24</td><td>14.70%</td></tr><tr><td>Lower-level manager</td><td>14</td><td>9.00%</td><td>27</td><td>15.65%</td></tr><tr><td>Professional</td><td>60</td><td>39.00%</td><td>48</td><td>29.85%</td></tr><tr><td>Administrative support</td><td>10</td><td>6.20%</td><td>29</td><td>18.20%</td></tr><tr><td>Other</td><td>13</td><td>8.70%</td><td>22</td><td>13.30%</td></tr><tr><td colspan="5">aOut-of-populationsample.</td></tr></table>

## Designing and Implementing the Artificial Neural Networks

The ANNs for this study was developed on NeuroSolutions, a Windows-based neural software application. The optimum weights that were loaded into the networks were obtained using Genehunter, a Windows-based GA software application. Since the sample size used in this study was relatively small, the k-fold-cross-validation method was used to evaluate the performance of the classification models. This technique has been described in detail and used extensively in numerous studies [8, 56].

Downloaded by [University of the Sunshine Coast] at 02:34 06 August 2017  
<sub>Sum</sub>m<sup>aryofVariablesUsedinTh</sup>

<table><tr><td>Variables</td><td>Definition</td><td>Previous studies</td><td>Items and scale</td></tr><tr><td colspan="4">Demographic factors</td></tr><tr><td>Income level</td><td></td><td></td><td>Single item</td></tr><tr><td>Gender</td><td></td><td>[24, 25, 54]</td><td>Single item</td></tr><tr><td>Education</td><td></td><td></td><td>Single item</td></tr><tr><td>Motivational factors</td><td></td><td></td><td>Six-item scale (1 = strongly disagree to 5 = strongly agree)</td></tr><tr><td rowspan="7">Perceived usefulness</td><td rowspan="7">The degree to which a person believes that using a particular system would enhance their job [19].</td><td rowspan="7">[1, 17, 18, 26, 44, 50]</td><td>The Internet provides the precise information I need</td></tr><tr><td>The Internet provides up-to-date information</td></tr><tr><td>The Internet is user friendly</td></tr><tr><td>The Internet is accurate</td></tr><tr><td>The information content on the Internet meets my needs</td></tr><tr><td>Using the Internet would increase my productivity on the job</td></tr><tr><td>Four-item scale (1 = strongly disagree to 5 = strongly agree)</td></tr><tr><td rowspan="4">Perceived enjoyment</td><td rowspan="4">An individual&#x27;s tendency to interact spontaneously, inventively, and imaginatively with the computer [53].</td><td rowspan="4">[18, 33, 53]</td><td>Spontaneous</td></tr><tr><td>Imaginative</td></tr><tr><td>Flexible</td></tr><tr><td>Creative</td></tr><tr><td>Computer skills</td><td></td><td></td><td>Four-item scale (1 = none to 5 = very extensive)</td></tr><tr><td rowspan="4">Experience</td><td rowspan="4">User&#x27;s knowledge or expertise in and performing tasks on the Internet [2]</td><td rowspan="4">[20, 28]</td><td>Using Internet search engines, such as Yahoo, Infoseek</td></tr><tr><td>Downloading files from the Internet</td></tr><tr><td>Creating Web pages</td></tr><tr><td>Accessing the Internet</td></tr></table>

<sub>by</sub> <sub>[</sub>U<sup>niversity</sup> <sup>of</sup> <sup>the</sup> <sup>Sunshine</sup> <sup>Coast]</sup> <sup>at</sup> <sup>02:34</sup> <sup>06</sup>  
<sub>m</sub>m<sup>aryofVariablesUsedinThisStudy(c</sup>

<table><tr><td>Variables</td><td>Definition</td><td>Previous studies</td><td>Items and scale</td></tr><tr><td>Formal training/ self-training</td><td>Instruction on the use of the Internet, focusing on efforts to transfer knowledge [31]</td><td>[3, 27, 31, 43]</td><td>Four-item scale (1=very little to 5=very extensive)Vendors or outside consultantsIn-house company coursesBy a fellow workerSelf-study; self-taught</td></tr><tr><td rowspan="2">Task structure</td><td></td><td></td><td>Four-item scale (1=very little extent to 5=very large extent)</td></tr><tr><td>The extent to which there are known procedures that specify the sequence of steps to be followed [51, 52]</td><td>[51, 52]</td><td>To what extent is there a defined body of knowledge that can guide you in doing your work?To what extent is there a understandable sequence of steps that can be followed in doing your work?To what extent can you actually rely on established procedures and practices to do your work?To what extent are your tasks the same day-to-day?</td></tr><tr><td rowspan="2">Nonwork Web usage</td><td></td><td></td><td>Seven-item scale (1=very unlikely to 5=very likely)</td></tr><tr><td>System usage has been the primary Indicator of technology acceptance.Cronin [14] among others suggests the Web sites used in this study.</td><td>[1, 13, 17, 18, 49]</td><td>Nonwork-related Web sites:Arts and entertainment, travel and leisure, living/consumer, sports/news</td></tr></table>

Table 3. Comparison of the Nonwork-Related Web User Groups

<table><tr><td rowspan="2"></td><td colspan="2">Low Nonwork-related Web usage</td><td colspan="2">High Nonwork-related Web usage</td><td rowspan="2">t-test</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Income</td><td>3.932</td><td>1.403</td><td>4.713</td><td>1.780</td><td>-2.917***</td></tr><tr><td>Education</td><td>4.151</td><td>1.036</td><td>4.150</td><td>0.969</td><td>0.004</td></tr><tr><td>Gender</td><td>1.411</td><td>0.495</td><td>1.238</td><td>0.428</td><td>2.322**</td></tr><tr><td>Web experience</td><td>2.203</td><td>1.696</td><td>3.538</td><td>0.976</td><td>-6.029***</td></tr><tr><td>Web formal training</td><td>1.208</td><td>0.987</td><td>1.683</td><td>0.739</td><td>-3.394</td></tr><tr><td>Web self-training</td><td>2.562</td><td>2.028</td><td>3.825</td><td>1.100</td><td>-4.847</td></tr><tr><td>Perceived enjoyment</td><td>1.764</td><td>1.256</td><td>2.572</td><td>0.479</td><td>-5.348</td></tr><tr><td>Task structure</td><td>2.610</td><td>1.059</td><td>2.006</td><td>0.884</td><td>3.837***</td></tr><tr><td>Perceived usefulness</td><td>3.088</td><td>0.833</td><td>3.408</td><td>0.891</td><td>-2.287*</td></tr><tr><td colspan="6">Notes: * = p &lt; 0.01; ** p &lt; 0.05; *** p &lt; 0.001.</td></tr></table>

The 154 case examples were randomly divided into k = 5 groups. The first group was set aside and the remaining (k – 1) = 4 groups were used to train the classification models. These training samples were used to determine the best set of weights for the network, which allowed the ANN to classify the input vectors with a satisfactory level of accuracy. The kth group was then used to test the ANN’s classification ability. This process was repeated for all five groups. The following steps were used to design the networks.

## Step 1: Designing the Training ANN Model

a. The networks were designed by inputting the characteristics of the Web usage behavior with respect to factors such as income (x ), gender $( x _ { _ 2 } )$ , and so on, together with the output variable characterizing the Web usage behavior. The input data was standardized between the range {–1 to 1} to avoid undue influences of the measurement scales on the network training. The standardized data set was calculated as

$$
S _ {i} ^ {n} = \frac {2 (x _ {i} ^ {n} + \min (x _ {i}))}{(\max (x _ {i}) - \min (x _ {i})) - 1},
$$

where $x _ { i } ^ { n }$ is the component i of case example n, min(x ) is the minimum of component i across the input data set, $\operatorname* { m a x } ( x _ { _ i } )$ is the maximum of componen i across the input data set.

<sub>lityStatisticsandCorrelationsfortheVaria</sub>b<sup>lesUsedinThisS</sup>

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Reliability</td><td colspan="10">Correlations</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td> $Income^a$ </td><td>1.00</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Education^a$ </td><td>1.00</td><td>0.292</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Web experience</td><td>0.90</td><td>0.230</td><td>0.096</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Web formal training</td><td>0.61</td><td>0.162</td><td>0.090</td><td>0.553</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Web self-training^a$ </td><td>1.00</td><td>0.186</td><td>0.175</td><td>0.844</td><td>0.522</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Perceived enjoyment</td><td>0.78</td><td>0.198</td><td>0.086</td><td>0.649</td><td>0.603</td><td>0.641</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Task structure</td><td>0.86</td><td>-0.355</td><td>-0.107</td><td>-0.297</td><td>-0.136</td><td>-0.206</td><td>-0.204</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Perceived usefulness</td><td>0.83</td><td>-0.023</td><td>0.073</td><td>0.359</td><td>0.268</td><td>0.270</td><td>0.212</td><td>-0.001</td><td>1.000</td><td></td><td></td></tr><tr><td> $Gender^a$ </td><td>1.00</td><td>-0.312</td><td>-0.244</td><td>-0.170</td><td>-0.045</td><td>-0.121</td><td>-0.158</td><td>0.098</td><td>-0.197</td><td>1.000</td><td></td></tr><tr><td>Nonwork-related Web sites</td><td>0.79</td><td>0.231</td><td>0.000</td><td>0.440</td><td>0.266</td><td>0.367</td><td>0.399</td><td>-0.298</td><td>0.183</td><td>-0.186</td><td>1.000</td></tr><tr><td colspan="12">Notes: a These variables were measured with a single item.The absolute values of correlation &gt; 0.10 are significant at 0.05 or lower.</td></tr></table>

b. In creating the hidden layer<sup>1</sup> the standardized inputs were multiplied by the weights (which is created in step 2) leading to each hidden neuron. At each hidden neuron, the input weight products were summed and a sigmoid function was applied to adjust the sum back to the range {0 to 1}. Thus, for each hidden neuron column we have

$$
z _ {j} = \mathrm{sigmoid} \left(\sum_ {i = 1} ^ {m} x _ {i} w _ {i j} ^ {(1)} + w _ {\mathrm{bias}} ^ {(1)}\right),
$$

where $w _ { i j } ^ { ( 1 ) }$ are the weights linking the inputs and hidden layers and $w _ { \mathrm { b i a s } } ^ { ( 1 ) }$ is the bias term corresponding to the weights linking the input and hidden layers.

The outputs of the neurons in the hidden layer are then multiplied by the weights leading to the output, where the softmax activation function was applied to produce the posterior probabilities. Thus, the outputs of the network $( y _ { k } )$ are determined as

$$
y _ {k} = \frac {1}{1 - \exp \left(- \left(\sum_ {j = 1} ^ {2} z _ {j} w _ {j k} ^ {(2)} + w _ {\mathrm{bias}} ^ {(2)}\right)\right)},
$$

where $w _ { j k } ^ { ( 2 ) }$ are the wrights linking the hidden and output layers, and $w _ { \mathrm { b i a s } } ^ { ( 2 ) }$ is the bias term corresponding to the wrights linking the hidden and output layers.

## Step 2: Determining the Optimum Weights Using GA

a. This study uses genetic algorithms to determine the optimum weights that are used to test the ANNs. An initial population of 26 chromosomes, representing possible solutions to the problem, was randomly generated. As mentioned previously, a chromosome is equivalent to a set of weights. The chromosomes potential as the optimum solution is determined by the mean squared error that was used as the fitness function.

b. Based on these relative fitness values, individuals in the current population were selected for reproduction. Although the chromosomes are selected at random, the probability of selection is proportional to fitness of the chromosomes. This means the higher the fitness function value of the individual, the higher its chances of being chosen for the reproduction process. The selection strategy used in this study is called the roulette wheel selection, where a roulette wheel with slots (S) is sized according to the total fitness function and represented as

$$
\mathrm{S} = \sum_ {i = 1} ^ {\text {popsize}} \operatorname{fitness} \left(F _ {i}\right),
$$

where F indicates the fitness of the value of the chromosome according to mean square error (MSE) for the individual i, popsize is the number of individuals in the population.

This selection process is based on spinning the wheel; with each spin a single chromosome is selected for a new population. In accordance with the theory of inheritance, the fittest chromosomes were selected more than once, whereas the least fit were eliminated.

c. The parent individuals selected from the current generation were then recombined using a crossover operator to produce two new offspring, one of which moved into the next generation. The mates for the crossover were chosen randomly from the initial population with the restriction that no individual could crossover with itself. The crossover rate was set at $P _ { \mathrm { c r o s } } = 0 . 9$ , that is, there is a 90 percent probability that crossover will occur. Since the crossover process can lose potentially useful information, mutation with a small probability $( P _ { _ \mathrm { M U T } } = 0 . 0 0 5 )$ was introduced. Following the crossover and mutation processes, the new population was ready for its next generation.

d. The remainder of the evolutions were basically cyclic repetitions of the steps given above, until the system converged to the lowest average MSE (that is, no improvement in the overall fitness of the population). This was reached before the 500th iteration of the genetic algorithm. This set of weights was then loaded into the ANN for the testing stage.

## Step 3: Testing the ANN

To test the robustness of the predictive ANN models, the training and holdout data sets were then applied to the networks. The confusion matrix shown in Table 5 presents the correct and incorrect classifications of the training and holdout samples. A can be observed in panel (a), the neural network models classified the training sample with an overall accuracy rate of over 97 percent for both ANN classifiers. This is not surprising since these networks were trained with the same data sets, resulting in the presence of an optimistic bias. Of greater interest was the overall accuracy of the classifiers for the holdout and out-of-sample data sets (that is, data sets that the network had not seen before). As can be observed in panel (b), both neural network models had a classification accuracy of over 86 percent for the holdout sample and an accuracy rate of 84 percent for the out-of-population sample (panel c).

In an effort to further compare the effectiveness of the neural networks, their results were compared with those of a multiple discriminant analysis (MDA) model. MDA, unlike neural networks, is a linear model, and thus, assumes that the data set used to distinguish outputs must be linearly separable. As can be observed in Table 5, the MDA classifier had an overall accuracy of only 57 percent. This suggests that nonlinear effects are present in the classification problem and that linear techniques such as MDA may be inadequate to classify Web users.

<sub>ontinue</sub>d

<table><tr><td colspan="7">Table 5. Classification Accuracy of Models</td></tr><tr><td colspan="7">Panel (a): Training Sample</td></tr><tr><td rowspan="3">Classification method predicted group</td><td colspan="6">Actual group membership</td></tr><tr><td colspan="2">ANN (MLP)</td><td colspan="2">ANN (SRN)</td><td colspan="2">MDA</td></tr><tr><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Group 1</td><td>309</td><td>6</td><td>314</td><td>2</td><td>155</td><td>35</td></tr><tr><td>Group 2</td><td>11</td><td>290</td><td>6</td><td>294</td><td>165</td><td>261</td></tr><tr><td>Total</td><td>320</td><td>296</td><td>320</td><td>296</td><td>320</td><td>296</td></tr><tr><td>Overall accuracy*</td><td>97.27%</td><td></td><td>98.72%</td><td></td><td>68.31%</td><td></td></tr><tr><td>Type 1 error</td><td>0.03</td><td></td><td>0.02</td><td></td><td>0.52</td><td></td></tr><tr><td>Type 2 error</td><td>0.02</td><td></td><td>0.01</td><td></td><td>0.12</td><td></td></tr><tr><td>Error rate</td><td>0.03</td><td></td><td>0.01</td><td></td><td>0.32</td><td></td></tr><tr><td colspan="7">k-1-fold cross-validation method was used in this study, where k = 5; n = 616; group 1 = low nonwork usage (320); group 2 = high nonwork usage (296).</td></tr><tr><td colspan="7">Table 5. Classification Accuracy of Models (continued)</td></tr><tr><td colspan="7">Panel (b): Cross-Validation (In-Sample)</td></tr><tr><td rowspan="3">Classification method predicted group</td><td colspan="6">Actual group membership</td></tr><tr><td colspan="2">ANN (MLP)</td><td colspan="2">ANN (SRN)</td><td colspan="2">MDA</td></tr><tr><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Group 1</td><td>70</td><td>11</td><td>73</td><td>6</td><td>49</td><td>38</td></tr><tr><td>Group 2</td><td>10</td><td>63</td><td>7</td><td>68</td><td>31</td><td>36</td></tr><tr><td>Total</td><td>80</td><td>74</td><td>80</td><td>74</td><td>80</td><td>74</td></tr><tr><td>Overall accuracy*</td><td>86.32%</td><td></td><td>91.57%</td><td></td><td>54.95%</td><td></td></tr><tr><td>Type 1 error</td><td>0.13</td><td></td><td>0.09</td><td></td><td>0.39</td><td></td></tr><tr><td>Type 2 error</td><td>0.15</td><td></td><td>0.08</td><td></td><td>0.51</td><td></td></tr><tr><td>Error rate</td><td>0.14</td><td></td><td>0.08</td><td></td><td>0.45</td><td></td></tr><tr><td colspan="7">n = 154; group 1 = low nonwork usage (80); group 2 = high nonwork usage (74).</td></tr></table>

<sub>):Cross-Valida</sub>t<sup>ion(Out-of-S</sup>

<table><tr><td rowspan="3">Classification method predicted group</td><td colspan="6">Actual group membership</td></tr><tr><td colspan="2">ANN (MLP)</td><td colspan="2">ANN (SRN)</td><td colspan="2">MDA</td></tr><tr><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Group 1</td><td>85</td><td>9</td><td>90</td><td>6</td><td>63</td><td>30</td></tr><tr><td>Group 2</td><td>16</td><td>53</td><td>11</td><td>56</td><td>38</td><td>32</td></tr><tr><td>Total</td><td>101</td><td>62</td><td>101</td><td>62</td><td>101</td><td>62</td></tr><tr><td>Overall accuracy*</td><td>84.82%</td><td></td><td>89.72%</td><td></td><td>56.99%</td><td></td></tr><tr><td>Type 1 error</td><td>0.16</td><td></td><td>0.11</td><td></td><td>0.38</td><td></td></tr><tr><td>Type 2 error</td><td>0.15</td><td></td><td>0.10</td><td></td><td>0.48</td><td></td></tr><tr><td>Error rate</td><td>0.15</td><td></td><td>0.10</td><td></td><td>0.42</td><td></td></tr><tr><td colspan="7">n = 163; group 1 = low nonwork usage (101); group 2 = high nonwork usage (62).* overall accuracy = (true positive + true negative)/(true positive + true negative + false positive + false negative).</td></tr></table>

## Evaluating the Network’s Performance

THE PERCENTAGE OF CORRECTLY CLASSIFIED OBSERVATIONS may not necessarily be the most useful measure for analyzing employees Web usage behavior. An importan goal of the classification models was to minimize the probability of misclassification, where misclassification was calculated in terms of type 1 and type 2 errors. A type 1 error is defined as “a high nonwork-related Web user is incorrectly classified as a low nonwork user,” and a type 2 error is defined as “a low nonwork-related Web user is incorrectly classified as a high nonwork user.” Based on the assumption that both type of errors were equally serious, an error rate was calculated, where the error rate is the ratio of the number of errors to the number of cases examined. As can be observed in Table 5, the ANN (SRN) had the lowest error rate of 0.08, indicating that it was a superior classifier in terms of misclassification than ANN (MLP) and MDA.

Since the classification process of Web users is fraught with uncertainty, it is important to account for the inherent risk typically present in such problems. Most previous studies in ANN classification have examined the issue of uncertainty in terms of symmetric or zero-one loss function, that is, zero losses are assumed if taking the correct decisions, and misclassifications are given a unit loss. Although this symmetric function may be valid for some applications, in the current context it would result in a classifier with very little practical use. Since misclassifications may carry different penalties and the goal of this study was to minimize the overall loss, an asymmetric loss function was used to calculate the cost of the misclassification. This function assigns zero cost when a correct decision is made and different cost levels for misclassifications. Since a type 1 error is considered to be more serious than a type 2 error, the cost of a type 1 error was set to be either 10, 20, 30, 40, or 50 times than that of a type 2 error. In reality however, the selection of the cost ratio depends on the specific scenarios facing organizations. These cost ratios were combined with the posterior probability outputs of the ANN models to produce a loss matrix [9]. The threshold values of the loss matrix can help managers make minimum risk decisions. The expected loss of misclassification was calculated as

$$
\mathrm{expectedloss} = \pi_ {0} * c _ {0} + \pi_ {1} * c _ {1},
$$

where $\pi _ { 0 } , \pi _ { 1 }$ is the posterior probability of high and low nonwork users, respectively, and $c _ { 0 } , c _ { 1 }$ is the cost of misclassifying of high and low nonwork users, respectively.

The expected costs of the various misclassification cost ratios is shown in Table 6. As can be observed, the ANN (SRN) classifier model dominates the other classification models with the lowest expected loss for the cost ratios. This implies that the ANN (SRN) model is the most cost-sensitive classifier.

Next, the cross-validation samples were reclassified using these threshold values. Reclassification is done by combining the posterior probabilities from the networks with a suitable matrix of loss coefficients, thus, not requiring any network training [10]. As expected, Table 7 shows a decrease in type 1 errors as its relative cost increases. Further, as can be observed in Tables 5 and 7, the misclassification rate of a type 1 error is lower for asymmetric cost functions than that of the symmetric cost functions. This is to be expected since the goal of the symmetric cost function is to maximize the correct classification [9], whereas the asymmetric function reduces the most costly error. Thus, by using the output of the ANNs and asymmetric cost functions, managers can make minimum risk decisions.

Table 6. Loss Matrix for the Classification Models

<table><tr><td>Misclassification error</td><td colspan="5">Cost ratios</td></tr><tr><td>Type 1: Type 2</td><td>10:1</td><td>20:1</td><td>30:1</td><td>40:1</td><td>50:1</td></tr><tr><td colspan="6">Classifier model</td></tr><tr><td>ANN-BP</td><td>0.01</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td></tr><tr><td>ANN-GA</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.04</td></tr><tr><td>MDA</td><td>0.22</td><td>0.43</td><td>0.65</td><td>0.87</td><td>1.08</td></tr></table>

To further validate the results of this study, data was collected from four organizations in the United States using the original survey instrument. The demographics of this data set are given in Table 1. The classification results of the out-of-population sample is shown in Table 5, panel (c), and as can be observed, the overall accuracy rate for the ANN (SRN) network was 89.7 percent. In addition, the overall error rate of this classifier model was lower than the ANN (MLP) and the MDA classifier. The out-of-population data was reclassified using the asymmetric cost ratios. As with the in-sample cross-validation data set, the ANN (SRN) classifier decreased type 1 errors as the relative cost of the type 2 errors increased (see Table 7). Based on these observations, the external validity of the ANN classifier could be considered to be strong.

## Conclusions

ANECDOTAL EVIDENCE INDICATES THAT, as Web usage in organizations grows, the level of employee nonwork usage rises. Such usage has serious repercussions that include loss of productivity, clogged networks, and potential civil and criminal liability, all of which could be a substantial cost to the organization. To date, most organizations have attempted to combat the problem by incorporating an acceptable usage policy, which research has shown to be largely ineffective. Research also indicates that the modification of user behavior through cognitive training and socialization is necessary in developing an effective Web management strategy.

This study proposes the use of AI-based behavior models, which can profile employees’ Web usage behavior, a priori. Such classification models can prove to be very useful to managers in the development of their Web management strategies. The data used to develop the classifiers were collected through a survey instrument. The classification performance of two neural network topologies, namely ANN (MLP), ANN (SRN), and the standard statistical technique MDA were compared using symmetric and asymmetric loss functions. The overall results indicate that the classification performance of the neural network models were far superior to the MDA model.

<table><tr><td colspan="6">Table 7. Reclassification of Holdout Samples Utilizing the Asymmetric Loss Ratios: ANN (SRN)</td></tr><tr><td rowspan="2">Cost ratios</td><td colspan="2">In-sample misclassification</td><td rowspan="2">Cost ratios</td><td colspan="2">Out-of-sample misclassification</td></tr><tr><td>Type 1 error</td><td>Type 2 error</td><td>Type 1 error</td><td>Type 2 error</td></tr><tr><td>10:1</td><td>53.85%</td><td>46.15%</td><td>10:1</td><td>64.71%</td><td>35.29%</td></tr><tr><td></td><td>7</td><td>6</td><td></td><td>11</td><td>6</td></tr><tr><td>20:1</td><td>53.85%</td><td>46.15%</td><td>20:1</td><td>58.82%</td><td>41.18%</td></tr><tr><td></td><td>7</td><td>6</td><td></td><td>10</td><td>7</td></tr><tr><td>30:1</td><td>38.46%</td><td>61.54%</td><td>30:1</td><td>35.29%</td><td>64.71%</td></tr><tr><td></td><td>5</td><td>8</td><td></td><td>6</td><td>11</td></tr><tr><td>40:1</td><td>30.77%</td><td>69.23%</td><td>40:1</td><td>23.53%</td><td>76.47%</td></tr><tr><td></td><td>4</td><td>9</td><td></td><td>4</td><td>13</td></tr><tr><td>50:1</td><td>23.08%</td><td>92.31%</td><td>50:1</td><td>11.76%</td><td>88.24%</td></tr><tr><td></td><td>3</td><td>12</td><td></td><td>2</td><td>15</td></tr></table>

Specifically, however, the results show that the ANN (SRN) model outperformed the ANN (MLP) model for all data sets. ANNs (SRNs) superior classification performance could be attributed to the features of context nodes and feedback loops, which makes it more suitable for behavior-based AI systems. In addition, a loss matrix was created to consider the uncertainty that is typically inherent in such problems. The results indicate that the ANN (SRN) classifier produced lower threshold values than ANN (MLP) and MDA models, which implies that the ANN (SRN) model is the more risk averse classifier among the models examined in this study. The results reveal that by using these threshold values, the more costly misclassification error (type 1) can be reduced. Furthermore, the external validity of the models was checked with an out-of-population data set. The results indicate that the models might be generalizable to different organizations.

A major limitation of this study is the use of a dichotomous classification of Web users. Future studies might consider categorizing Web users in a different way. In addition, not all the possible variables were considered in developing the classification models. For instance, researchers could also consider variables such as management and organizational support. Future research will have to examine what these variables are and formally incorporate them into the classifier models. Moreover, this study only compared the ANN topologies while holding all other parameters constant. For example, the sample sizes of the data sets were limited and the various proportions between low and high nonwork usage were not considered. Another limitation of the study is that the samples used in this study have similar educational backgrounds. This could potentially affect the generalizability of the study’s findings.

From an IS research perspective, this study introduces ANN as an alternative tool to the more traditional statistical techniques. The methodology presented in this study can be applied to a wide range of problems such as end-user classification and prediction of IS utilization. It could also be utilized as an analysis tool for contingency models such as the information-processing framework.

Users of these classification models may be cautious of such aids, since these models appear to take decision-making out of their hands. However, by having the ability to profile the various types of Web users, managers can specifically design their Web management strategies more effectively. The implementation of such strategies, for example through socialization, and cognitive training, may reduce the occurrence of nonwork-related Web usage behavior. These classifier models can also complement the current strategies of organizations by providing managers with insights into the characteristics of the Web users. This would aid organizations in approaching the subject of employees’ Web usage in a more informed manner.

## NOTE

1. After extensive experimentation, a two-neuron hidden layer was found to be the mos suitable network structure.

## REFERENCES

1. Adams, D.A.; Nelson, R.R.; and Todd, P.A. Perceived usefulness, ease of use and usage of information technology: A replication. MIS Quarterly, 16, 2 (1992), 227–247.

2. Ajzen, I., and Fishbein, M. Understanding Attitudes and Predicting Behavior. Upper Saddle River, NJ: Prentice Hall, 1980.

3. Amoroso, D.L., and Cheney, P.H. Testing a causal model of end-user application effec tiveness. Journal of Management Information Systems, 8, 1 (Summer 1991), 63–89.

4. Anandarajan, M.; Simmers, C.; and Igbaria, M. An exploratory investigation of the antecedents and impact of Internet usage: An individual perspective. Behaviour and Information Technology, 19, 1 (2000), 69–85.

5. Arbib, M.A., and House, D.H. Depth and detours: An essay on visually guided behavior. In M.A. Arbib and A.R. Hanson (eds.), Vision, Brain, and Cooperative Computation. Cambridge, MA: MIT Press/Bradford Books, 1987, pp. 129–163.

6. Archer, N., and Wang, S. Application of the back propagation neural network algorithm with monotonicity constraints for two-group classification problems. Decision Sciences, 24, 1 (1993), 60–75.

7. Baeck, T., and Schwefel, H.P. An overview of evolutionary algorithms for parameter optimization. Evolutionary Computation, 1, 1 (1993), 1–23.

8. Baker, J.A.; Kornguth, P.J.; Lo, J.Y.; Willliford, M.E.; and Floyd, C.E. Breast cancer: Prediction with artificial neural network based on BI-RADS standardized lexicon. Journal of Radiology, 196, 3 (1995), 817–822.

9. Berardi, V.L., and Zhang, G.P. The effect of misclassification cost on neural network classifiers. Decision Sciences, 30, 3 (1999), 659–682.

10. Bishop, C.M. Neural Networks for Pattern Recognition. New York: Oxford University Press, 1995.

11. Changeux, J.P. Neuronal Man: The Biology of Mind. Oxford: Oxford University Press, 1986.

12. Commerce Net. Knowledge: Internet statistics. Commerce Net, San Jose, CA, November 2001. Available at www.commerce.net/research/stats/indust.html.

13. Cronin, M.J. Doing More Business on the Internet. New York: Van Nostrand Reinhold, 1995.

14. Cronin, M.J. The Internet as a competitive business resource. In M. Cronin (ed.), The Internet Strategy Handbook. Boston: Harvard Business School Press, 1996, pp. 1–22.

15. Curry, B., and Morgan, P. Neural networks: A need for caution. Omega-Internationa Journal of Management Science, 25, 2 (1997), 123–133.

16. Daly, E.M.; Lancee, W.J.; and Polivy, J. A conical model for the taxonomy of emotiona experience. Journal of Personality and Social Psychology, 45, 2 (1983), 443–457.

17. Davis, F.D. Perceived usefulness, perceived ease of use, and user acceptance of informa tion technology. MIS Quarterly, 13, 3 (1989), 983–1003.

18. Davis, F.D. Extrinsic and intrinsic motivation to use computers in the workplace. Jour nal of Applied Social Psychology, 22, 14 (1992), 1111–1132.

19. Davis, F.D.; Bagozzi, R.P.; and Warshaw, P.R. User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35, 8 (1989), 982–1003.

20. DeLone, W.H. Determinants of success for computer usage in small business. MIS Quarterly, 12, 1 (1988), 51–61.

21. Elman, J.L. Finding structure in time. Cognitive Science, 14, 2 (1990), 179–211.

22. Fausett, L. Fundamentals of Neural Networks. Upper Saddle River, NJ: Prentice Hall, 1994.

23. Finke, M., and Muller, K.R. Estimating a-posteriori probabilities using stochastic net work models. In M. Mozer, P. Smolensky, D. Touretzky, J. Elman, and A. Weigend (eds.), Proceedings of the Connectionist Models Summer School. Mahwah, NJ: Lawrence Erlbaum, 1994, pp. 324–331.

24. Gefen, D., and Straub, D.W. Gender differences in the perception and use of e-mail: An extension to the technology acceptance model. MIS Quarterly, 21, 4 (1997), 389–400.

25. Harrison, A.W.; Rainer, R.K.; and Houcwarter, G. Gender differences in computing activities. Journal of Social Behavior and Personality, 12, 4 (1997), 849–868.

26. Igbaria, M. User acceptance of microcomputer technology: An empirical test. Omega An International Journal of Management Science, 21, 1 (1993), 73–90.

27. Igbaria, M. Testing the determinants of microcomputer usage via a structural equation model. Journal of Management Information Systems, 11, 4 (Spring 1995), 87–105.

28. Igbaria, M.; Pavri, F.; and Huff, S. Microcomputer application: An empirical look a usage. Information and Management, 16, 4 (1989), 187–196.

29. Kleinmuntz, B. Why we still use our heads instead of formulas: Towards an integrated approach. Psychological Bulletin, 107, 3 (1990), 296–310.

30. LaPlante, A. Start small, think infinite. Computerworld, 33, 13 (1997), 24–30.

31. Lee, D.S. Usage pattern and sources of assistance to personal computer users. MIS Quarterly, 10, 4 (1986), 313–325.

32. Lenard, M.; Alam, P.; and Madey, G. The applications of neural networks and a qualitative response model to the auditors going concern uncertainty decision. Decision Sciences, 26, 2 (1995), 209–227.

33. Malone, T.W. Toward a theory of intrinsically motivating instruction. Cognitive Science, 4, 3 (1981), 333–369.

34. McBride, P. Develop secure Internet practices. Internet Security Advisor, 4, 2 (2000), 18–25.

35. McCullagh, P., and Nelder, J.A. Generalized Linear Models. London: Chapman and Hall, 1989.

36. McWilliams, G., and Stepanek, M. Taming the info monster. Business Week, 22, 25 (1998), 170–172.

37. Mesa, C. The high cost of cyberslacking. Workforce, 79, 12 (2000), 22–24.

38. Naughton, K. CyberSlacking. Newsweek, 134, 48 (1999), 62–65.

39. Nunnally, J.C. Psychometric Theory. New York: McGraw-Hill, 1978.

40. Pastore, M. The big picture demographics. Information Data Corporation, New York, 2001. Available at cyberatlas.internet.com/big\_picture.demographics/article/0,1323,5911\_ 326181,00.html.

41. Pfeifer, R., and Verschure, P. Distributed adaptive control: A paradigm for designing autonomous agents. In F.J. Varela and P. Bourgine (eds.), Proceedings of the First European Conference on Artificial Life. Cambridge, MA: MIT Press/Bradford Books, 1992, pp. 21–30

42. Ray, T. An approach to the synthesis of life. In C.G. Langton, C. Taylor, D. Farmer, and S. Ramussen (eds.), Artificial Life II, Proceedings of the Workshop on Artificial Life. Cambridge, MA: MIT Press, 1992, pp. 325–371.

43. Raymond, L. The impact of computer training on the attitudes and usage behavior of small business managers. Journal of Small Business Management, 26, 3 (1988), 8–13.

44. Robey, D. User attitudes and management information systems use. Academy of Management Journal, 22, 3 (1979), 527–538.

45. Scandura, T.A., and Lankau, M.J. Relationships of gender, family responsibility and flexible work hours to organizational commitment and job satisfaction. Journal of Organiza tional Behavior, 18, 4 (1997), 377–391.

46. Simard, P.Y.; Ottaway, M.B.; and Ballard, D.H. Fixed point analysis for recurrent net works. In D.S. Touretzky (ed.), Advances in Neural Information Processing Systems. San Mateo, CA: Morgan Kaufmann, 1989, pp. 149–159.

47. Smithers, T. Taking eliminative materialism seriously: A methodology for autonomous systems research. In F.J. Varela and P. Bourgine (eds.), Toward a Practice of Autonomous Systems, Proceedings of the First European Conference on Artificial Life. Cambridge, MA: MIT Press/Bradford Books, 1992, pp. 31–40.

48. Steels, L. Exploring analogical representations. In P. Maes (ed.), Designing Autonomous Agents: Theory and Practice from Biology to Engineering and Back. Cambridge, MA: MIT Press/Bradford Books, 1990, pp. 71–88.

49. Straub, D.; Limayem, M.; and Karahanna, E.E. Measuring system usage: Implications for IS theory testing. Management Science, 41, 8 (1995), 1328–1342.

50. Thompson, R.L.; Higgins, C.A.; and Howell, J.M. Influence of experience on personal computer utilization: Testing a conceptual model. Journal of Management Information Sys tems, 11, 1 (Summer 1994), 167–187.

51. Tushman, M.L., and Nadler, D.A. Information processing as an integrating concept in organizational design. Academy of Management Review, 3, 4 (1978), 613–624.

52. Umanath, N.S., and Kim, K.K. Task-structure relationship of information systems devel opment subunit: A congruence perspective. Decision Sciences, 23, 4 (1992), 819–838.

53. Webster, J. Playfulness and computers at work. Ph.D. dissertation, New York University, New York, 1989.

54. Williams, S.W.; Ogletree, S.M.; Wodburne, W.; and Rafeld, P. Gender roles, compute attitudes and dyadic computer interaction: Performance in college students. Sex Roles: A Jour nal of Research, 29, 8 (1994), 515–526.

55. Wong, B.K.; Bodnovich, T.A.E.; and Selvi, Y. A bibliography of neural networks appli cation research: 1988–1994. Expert Systems, 12, 3 (1995), 253–261.

56. Wu, W.; Massart, D.L.; and Jong, S.D. Kernel-PCA algorithms for wide data Part II: Fas cross-validation and application in classification of NIR data. Chemometrics and Intelligent Laboratory Systems, 37, 2 (1997), 271–280.

57. Yasin, R. Web slackers. Internet Week (March 3, 2000). Available at www.internetweek .com/lead/lead101599.htm.
