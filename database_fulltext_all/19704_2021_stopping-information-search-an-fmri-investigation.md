---
otero_id: 19704
otero_key: "FEKMHAHS"
title: "Stopping information search: An fMRI investigation"
authors: "Glenn J. Browne; Eric A. Walden"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113498"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stopping information search: An fMRI investigation

Glenn J. Browne <sup>\*</sup>, Eric A. Walden

![](/api/attachments/FEKMHAHS/fulltext/images/a895db79e1b2a5e853a2a7ada2c96bd0b04d2264e867e9cb17bf1e38290c527e.jpg)

Information Systems & Quantitative Sciences, Rawls College of Business, Texas Tech University, Lubbock, TX 79409, United States of America

## A R T I C L E I N F O

Keywords: Information search Stopping rules Decision making fMRI techniques Inhibition Neuroscience

## A B S T R A C T

Facilitating information search to support decision making is one of the core purposes of information technology. In both personal and workplace environments, advances in information technology and the availability of in formation have enabled people to perform much more search and access much more information for decision making than ever before. Because of this abundance of information, there is an increasing need to develop an improved understanding of how people stop search, since information available for most decisions is now almost infinite. Our goal in this paper is to further our understanding of information search and stopping, and we do so by examining the neurocorrelates of stopping information search. This is a process that involves both stopping the search and the decision to stop the search. We asked subjects to search for information about consumer products and to stop when they believed they had enough information to make a subsequent decision about whether to purchase those products while in a functional Magnetic Resonance Imaging (fMRI) chamber. Brain activation patterns revealed an extensive distributed network of areas that are engaged in the decision to stop searching for information that are not engaged in search itself, suggesting that stopping is a complex and cognitively demanding neurological activity. Implications for theory, particularly information overconsumption, and for IT design are discussed.

## 1. Introduction

Information search is now a ubiquitous aspect of people’s in teractions with information systems. Desktop, laptop, tablet, and mobile interfaces are all used increasingly to gather and synthesize information for decision making. From Google to Amazon to map and destination applications, websites now primarily promote and facilitate information search. We are arguably in the midst of a historic shift in the use of in formation systems, leaving the age in which systems are used primarily to enhance workplace productivity to an age in which the World Wide Web is the basic information system and is used primarily for missions of search and find, followed by the tasks of choose or consume. Decisions usually start with the decision maker gathering information about the decision. Customers read reviews (e.g., [118]), doctors and patients search for medical information (e.g., [113]), and people search social media to learn about companies, friends, or products (e.g., [50]), among innumerable types of searches performed every day. More information typically leads to better decisions. However, more information always leads to costlier decisions. As Herbert Simon said, “...in an informationrich world, the wealth of information means a dearth of something else: a scarcity of whatever it is that information consumes. What information consumes is rather obvious: it consumes the attention of its recipients. Hence a wealth of information creates a poverty of attention and a need to allocate that attention efficiently among the overabundance of in formation sources that might consume it” ([95], pp. 40–41). The more time, energy, and effort a decision maker spends searching for infor mation, the less attention he or she has available to give to something else. Attention is the primary resource of the decision maker, and in formation search consumes it.

Stopping is the primary determinant of how much of the scarce attention resource is consumed during a decision process. Stopping is also the primary determinant of decision potential. Decision potential is determined by the information a decision maker has—the best possible decision is a function of the information used to make the decision. A decision maker may not live up to his potential in using the information due to other limitations, but it is the quantity and quality of information available that yields potential, and it is stopping that solely determines the information available. In terms of the cost of decisions and the po tential of decisions, stopping is the prime factor.

The raison d’etre of information systems is to facilitate a decision maker’s search for information [19]. While it has been recognized for many years that decision makers have too much information [2], in recent years the quantity of information readily available to everyone has grown dramatically. A 2017 IBM whitepaper estimated that 90% of the world’s data had been created since 2016,<sup>1</sup> and International Data Corporation forecasts that the global datasphere will increase from 33 zettabytes in 2018 to 175 zettabytes in 2025 [86]. A 2019 report found that 28% of Americans are online almost constantly and that 81% go online daily.<sup>2</sup> These enormous amounts of information facilitate increased information search. A recent study found that almost 90% of effective employee work requires an initial search for information.<sup>3</sup> Another report showed that five of the top seven web-based activities involve search.<sup>4</sup> We now have an IT artifact, the internet, that supplies a virtually unlimited amount of easily accessible information for most decisions. However, people have limited information processing capa bilities, as noted above [95], and the unlimited amount of information now available can easily trigger the well-known phenomenon of infor mation overload and its accompanying suboptimal processing of infor mation [67,90,108] as well as internet addiction and technostress [102]. Further, research has shown that people are not particularly successful at applying good stopping rules on their own (e.g., [31]); therefore, it is increasingly important that information systems help facilitate the stopping of information search. Although prior research has investigated stopping behavior using experimental methods (e.g., [18]), there is still much to be learned about how people stop searching for information. It is difficult to build a system that facilitates stopping if we do not un derstand how people stop.

It is challenging to study the underlying mechanisms of stopping because no measurement of stopping behavior can describe the entire internal experience. Previous studies have asked subjects about stopping in self-reports (e.g., [18]) and have made inferences about stopping rules from protocols in which subjects used everyday language (e.g., [17]). Although valuable and quite revealing in advancing our understanding of stopping behavior, such methods suffer from subjects’ potential inability to articulate their judgment and reasoning and do not measure brain activity. Measuring brain activity can complement other methods and may suggest support or refutation of self-report or inferential measures based on the brain areas activated. To measure brain activity we can use a neurophysiological tool—functional magnetic resonance imaging (fMRI)—to examine the mechanisms of stopping. Neuroscience methods, including fMRI, are used regularly to investigate various as pects of decision making (e.g., [89,107,116]). As Dimoka et al. [45] point out, “Neurophysiological tools are particularly valuable for measuring IS constructs that people are either unable, uncomfortable, or unwilling to truthfully self-report” (p. 680).

NeuroIS is particularly useful in this context because we want to measure the metabolic cost of stopping information search to see whether it is higher than the metabolic cost of continuing information search. As an analogy, imagine a runner who is asked to stop running. One could measure the blood flow to different muscles in his legs while running and compare this to the blood flow in the legs while he was stopping and look at this difference to determine (a) which muscles were activated to stop and (b) how much more oxygenated blood was required for the legs to perform the stopping action. This is analogous to what we do in this study, except that we use fMRI to measure the blood flow in the brain during search and stopping.

Our goal in this research is to further our understanding of searching and stopping behavior. We use fMRI to map an IS construct, stopping information search, into brain regions. This is analogous to a using a survey to map IS constructs into self-reports. As Dimoka and Davis [43] state, “…certain brain activations can be associated with certain pro cesses and functions already shown by extant empirical studies in the cognitive neuroscience literature. … The fundamental research question is to identify (map) the neural correlates of the … constructs to quali tatively assess how the observed brain activations relate to processes already identified in the cognitive neuroscience literature” (p. 5). In essence, in this paper we attempt to discover “where the brakes are” in the brain; we do this to develop a better understanding of how people apply those brakes because stopping information search determines how much and what information a decision maker has available, and sup plying information is what the IS discipline is all about.

Our work thus contributes to theory in both the information systems literature and the neuro-IS literature. For information systems, we advance knowledge in the area of information search, which, as noted, has become one of the primary functions performed by people both at work and at leisure using the World Wide Web and various computing devices as technological enablers. We also advance our knowledge of stopping behavior, which enables decision making, actions, and new searches to occur. For neuro-IS and neuroscience generally, we add to our knowledge of brain areas used in the processing of information. Prior research has provided limited investigations of information search and stopping, and we add to that literature.

The remainder of the paper proceeds as follows. We next survey the literature on searching and stopping and generate hypotheses to be investigated in the current study. We then discuss the methodology used and describe the results of an investigation conducted to understand how searching and stopping are reflected in brain activity. We close with a discussion of the findings and directions for future research.

## 2. Background and literature review

The need for improved stopping techniques in information search arises from the combination of data now available due to advances in information technology and the existing limitations on human infor mation processing. The internet and the World Wide Web have provided access to nearly limitless information for most important decisions. Advances in data mining and business analytics techniques are pro ducing data in enormous quantities that can be utilized if the appro priate tools and human capacities are available. Although IT can help process the enormous amounts of information available, and even replace human decision makers in some instances (e.g., loan applica tions, among many other examples), most important decisions still rely on the judgments, preferences, and choices of people (e.g., [80]). Peo ple’s cognition, however, remains significantly limited, especially in the capacity and speed of processing of working memory [72,87]. As noted by Simon, working memory is the “bottleneck” in cognition ([97], p. 61). Because decisions still need to be made, and people generally want to make at least a satisfactory decision in most situations, they attempt to utilize the information available. But both cognitive constraints and practical considerations such as time available necessarily limit the amount of information that can be sought, consumed, and utilized for any decision. Thus, given the effectively limitless amount of data now available for most important decisions, the choice of when to stop an information search is of increasing importance.

We turn now to research on information search and stopping behavior. Search is a fundamental human activity and therefore has received widespread attention in numerous scientific disciplines. The literatures are so vast that only a tiny fraction directly relevant to the current research can be recounted here.

Information search can be stopped using either normative or heu ristic rules. Normative rules for stopping have been studied in eco nomics, game theory, statistics, and psychology, and include such rules as the expected value of information, marginal value of additional in formation, Bayesian rules, and stopping in optional stopping tasks such as the “secretary problem,” a hiring problem with an unknown number of applicants viewed sequentially (e.g., [24,52,69,71,74,98]). However, research has found that normative stopping rules apply in a very narrow range of contexts, and people instead use heuristics to stop information gathering in the vast majority of situations [31,91,97].

Search as a heuristic process in decision making was pioneered by Simon [96,97] and others (e.g., [37,78,88]). In Simon’s view, search is a goal-directed process aimed at discovering alternatives. Numerous heuristic strategies can be employed during search, such as means-ends analysis and breadth-first or depth-first search [97]. Decision making is viewed as a process of “Intelligence,” “Design,” and “Choice,” in which the Intelligence phase consists of initial information search [97]. Crucially, at each stage of the process the decision maker must stop. Stopping the Intelligence, or information search, phase of decision making is the focus of the present study. Because of the focus on stopping information search, the sufficiency of information gathered, rather than the final choice, is the key concern.

As information search is fundamental in the use of information sys tems, IS research has investigated search and stopping in various con texts. Examples include decision support systems, the World Wide Web, information requirements determination, and product search tasks in the presence of recommendations [1,17,18,22,38,40,62,63,105]. Search has also been studied from an economic viewpoint in the IS literature, focusing on the relative costs of searching vs. stopping (e.g., [7,20,53]).

Cognitively, decision makers in search tasks must recognize that they have gathered enough information and that it is time to stop. They must make this assessment across a variety of different information search situations that occur constantly in business and in everyday life, from determining information requirements in systems analysis, to choosing a sofa to purchase, to deciding what to order in a restaurant. The above literature implicitly assumes that people can and do monitor the amount of information they have and make judgments against their evaluation of the necessary quantity of information. Furthermore, at some point they judge that the information is sufficient to make a choice. This is the mechanism we seek to investigate.

We make several assumptions about information search that are characteristic of most complex managerial and personal search tasks. These assumptions define an optional stopping task, since the decision maker chooses when to stop. First, we assume that information is ac quired sequentially by decision makers rather than all at once. In all but the simplest of problems, this leads to the need to stop the search before all available information is viewed and considered. Second, we assume that the total information available, including number of potential al ternatives, is not known in advance. Both of these assumptions force the decision maker to focus on search rather than choice [49,55,73]. In contrast, if the number of alternatives is known and the decision maker is permitted to view them all at once, the task is primarily one of choice rather than search.

The existing literature on search and stopping has been significant and useful, but gaps remain in our understanding. One important issue is that the studies concerning searching and stopping have all been behavioral. We do not have any understanding of the cognitive (meta bolic) costs of stopping and we do not know the relative costs of searching vs. stopping. Such an understanding is important because it can improve our theoretical understanding of why people may underacquire or over-acquire information. If our goal in organizations and in our personal lives is to acquire the optimal amount of information for decision making (or at least an amount close to optimal), then under standing the costs of searching and stopping is necessary.

To address this gap, and because it is difficult for a person to artic ulate how he judges the quantity and quality of information he has and how he judges the information to be sufficient, we turn to neuroscientific tools to observe the brain directly while people stop searching and to investigate the metabolic costs of searching and stopping.

Dimoka, Pavlou, and Davis [44] noted the opportunity to investigate online search using neuroscience techniques. Given its ubiquity in human behavior, search behavior has received surprisingly little attention from neuroscientists. The primary exception is visual search, which has been the subject of numerous investigations (e.g., [3,13]) using fMRI.

## 3. Theory development

The literature review makes it clear that searching and stopping are important IS phenomena [18,20,53,62], but an important gap remains in our understanding of how people stop the search process. The im plications for stopping when using IT artifacts require investigation, and we turn to research in psychology as a basis for our theory development.

Psychologists have investigated stopping behavior extensively in several types of tasks involving cognition and motor skills.<sup>5</sup> Many of these studies have been conducted in the neuroimaging domain (for reviews, see [75,76,100]). Two types of tasks have been used: The Go/ NoGo task, in which a subject provides or withholds a motor response depending on whether he observes one type of stimulus or another, and the Stop-Signal task, in which the subject responds on every trial unless he receives a signal to stop [100]. Areas of the brain active during such stopping tasks include the dorsolateral prefrontal cortex bilaterally, the anterior cingulate cortex, the anterior insula bilaterally, the putamen bilaterally, and the right inferior parietal lobe [32,100]. What these areas have in common is that they all are involved in executive control and evaluation functions—this is the underlying theory for stopping behavior in the brain. Many aspects of cognition are a function of ex ecutive control, and stopping is one of those aspects (and a critical one) since stopping is by definition a control function.

Our investigational design is a variant of the Stop-Signal task as used in fMRI experiments [5,6,29]. In the Stop-Signal task subjects are asked to engage in an action, usually pushing a button, until told to stop—for example, pushing the right button if an X is shown and the left button if an O is shown, until the screen background turns red [29]. In a Stop Signal task fMRI analysis, the activation on the stop signal is compared to the activation on the other trials [6,29,30]. Our investi gation is a variant because stopping is voluntary. Subjects must choose when to stop instead of being told to stop.

While we know that when commanded to stop subjects will show a specific pattern of activation [100], we do not know if this will be the case when they choose to stop on their own. We hypothesize that a specific pattern occurs, but it is possible that the stop signal in selfdirected stopping builds slowly. This is important because in the stopsignal task subjects are not always successful in stopping when told to do so. Presumably this is because it requires a great deal of mental effort to stop. fMRI measures oxygenated blood flow, so it is actually measuring metabolic cost to perform an action in the same way one might measure the oxygenated blood to a person’s legs when he or she prepares to jump. Thus, our measure is the metabolic cost of stopping vs. the metabolic cost of searching, as well as where in the brain the addi tional oxygen is needed to allow the cells to perform work.

As noted earlier, an IT artifact can facilitate stopping, and we pro pose two simple methods for doing so. The first is simply to preempt it. Instead of displaying unlimited information, an IT artifact can present a limited amount of information. Thus, the user will not have to engage executive control to stop; rather, the system will effectively do it for him or her. As a specific example, an IT artifact could provide only a portion of the relevant information and require the user to actively seek more. A second method for an IT artifact to facilitate stopping is to prompt the user. A simple example would be to present a reminder of how much the user has already searched and ask him if he is sure continuing is a good use of his time.

Of course, while most builders and designers of IT artifacts want to present an appropriate quantity and quality of information, it is not likely that all want to facilitate stopping search. In fact, for many com panies the opposite is true—they want to encourage ever greater amounts of search by discouraging stopping [27]. For example, many websites, such as Facebook, Pinterest, and LinkedIn, use infinite scroll ing to present a certain amount of information, but when the user nears the bottom more information loads automatically. Thus, such website have the opposite design to that suggested above and seem to be very good at discouraging the exercise of executive control to stop search. Perhaps that is why infinite scrolling has been called the web’s slot machine [48].

Regardless of whether designers want to facilitate or impede the user’s executive control for stopping, stopping is an important factor in information search (it is a requirement in any real problem or decision of even minor complexity given the limitations on people’s information processing capabilities and their finite time limitations). We hypothesize that stopping information search will involve the same areas of the brain as other types of stopping tasks such as Stop-Signal because we conjecture that people possess a generalized stopping mechanism. Fortunately, basic motor skills stopping tasks such as Go/NoGo and Stop-Signal have been studied extensively in neuroscience and thus we have a good way to measure brain activity. Using the results of a recent meta-analysis by Swick et al. [100], we hypothesize:

H1. Stopping Hypothesis: Voluntarily stopping information search will result in bilateral activation in the anterior insular cortex, the putamen, the caudate, the thalamus, the posterior cingulate gyrus, the right inferior frontal gyrus, right inferior parietal lobe, right middle frontal gyrus, the right superior frontal gyrus, the left inferior frontal gyrus and right middle frontal gyrus.

This is a large number of areas so we duplicate Swick’s figure below (Fig. 1). This figure shows all of the voxels that have significant acti vation, on average, across 34 Stop-Signal experiments reported in 21 neuroscience papers. The lighter the color in the scans, the higher the level of significance.

Our main hypothesis is focused on the stopping aspects of the search process. However, neuroimaging data have an advantage over other methods of measuring IT constructs in that we measure the entire brain irrespective of our hypotheses. Thus, we may find additional activations besides those we hypothesize, and those should be reported for scientific completeness as they can form the basis for additional theorizing and knowledge creation. Therefore, this research also has an exploratory aspect, which is well accepted in the neuroIS literature [42–44] as well as science in general. We follow Dimoka’s [42] notion that “exploratory work is a well-accepted practice in the neuroscience literature by allowing brain data to speak for itself” (p. 834). We also observe that our research attempts to localize neurocorrelates of an IT construct (stop ping), and as many scholars have agreed, “localizing the neural corre lates of IT-related constructs could be a good starting point to add value to the neuroscience literature” [45 ,p. 696]. With that in mind, we offer the following exploratory hypothesis.

H2. Decision to Stop Hypothesis: The voluntary decision to stop in formation search will show neurocorrelates beyond those associated with motor skills stopping tasks.

## 4. Method

## 4.1. Subjects

Subjects were 21 students from a business school subject pool at a large research university in the southwestern U.S. The study was approved by the university’s institutional review board. The average age of our subjects was 22.6 years (Min = 20, Max = 29, StDev = 2.54). There were 13 males and 8 females. The subjects received course credit for participating.

## 4.2. Procedure

Before the investigation, subjects signed a consent form and answered demographic questions. They then received training outside of the scanner so they would understand the process during the investi gation. This training was used to familiarize the subject with the task and the procedures so that time in the MRI chamber was not wasted. They then were given a brief medical screening and entered the MRI chamber.

The investigational task required a subject to search for information about three products individually within a product class, and this was repeated for seven product classes. The products utilized were re frigerators, laptop computers, Blu-Ray players, cell phones, portable GPS systems, printers, and televisions. When subjects indicated they had gathered enough information (that is, they indicated they wanted to stop), they were given a question about why they chose to stop (shown in Fig. 2 and Fig. 3 below) as motivation for deliberative stopping. They then were given information about the second television and then the third television, following the same procedure, as shown in Fig. 4. Thus, the investigational design facilitated the measuring of searching and stopping information search, the focus of the present research. To motivate subjects to pay attention and to gather information, they were told they would need to make a choice as to which product they would choose at the end of each product session (although the choice made was

![](/api/attachments/FEKMHAHS/fulltext/images/0a4cb30530dda2490fb8c2a83607e8cc90bda40335ab47028d8a19ed313e234c.jpg)  
Fig. 2. Sample information screen from investigation.

![](/api/attachments/FEKMHAHS/fulltext/images/c22e963840e0d96deef1c620bf68a458df0aae811f3f2c69757607378cf106bb.jpg)  
Fig, 1. Areas of activation for Stop-Signal tasks from a meta-analysis of 34 experiments. Reprinted from Neuroimage, 56(3). D. Swick, V. Ashley. U. Turken, Are the neural correlates of stopping and not going identical? Ouantitative meta-analysis of two response inhibition tasks, pp. 1655–1665. Copyright 2011, with permission from Elsevier.

![](/api/attachments/FEKMHAHS/fulltext/images/ba3b876d28e5212555ab903150457f67227db4f24b76b196d70bd879850dd56a.jpg)  
Fig. 3. Protocol for one item.

![](/api/attachments/FEKMHAHS/fulltext/images/7cd91a2bb9b021292e456ad171c5a31a820430ee39e4217eaec0644209dffc3a.jpg)  
Fig. 4. Protocol for all three options of a single product type.

not of interest in this research).

Information about a product was given sequentially, one attribute at a time. Examples of attributes for a television were screen size, HDMI ports, and price, such as in Fig. 2. Each attribute was displayed for three seconds, and subjects were then given the choice of seeing another attribute or stopping the search for information about that product and moving to the next product. For example, for the first television, the initial attribute of information was the resolution of the television. If the subject wanted to see more information, he indicated that by pushing the appropriate button on the screen. The subject was allowed to gather as much or as little information as he desired (each product had between 35 and 50 attributes). When the subject had gathered all the information he desired and pressed the “Stop Gathering Information” option, a fix ation cross appeared for three seconds, followed by a question about why the subject stopped, as shown in Fig. 4. The subject was allowed 12 s to respond. This was followed by another three-second fixation cross. Then the next instance of the product began with an attribute displayed. The attributes were shown in the same order for every instance of the product. After all three instances of a product were shown, the subject was asked to choose among them as shown in Figure . He was allowed 12 s and fixation screens were shown for three seconds before and after the choice screen. This process was repeated for seven different product classes. The average amount of time spent searching about one product was 48.65 s (standard deviation 32.77).

## 4.3. Data acquisition

The functional imaging was conducted in a single session using a Siemens 3.0 Tesla Skyra to acquire gradient echo T2\*-weighted echo planer images (EPI). Each volume contained 50 slices acquired in an interleaved manner. Isotropic 3 mm<sup>3</sup> voxels were obtained using a flip angle of 80 degrees, with an echo time of 28 milliseconds and a repe tition time of 3 s. We also obtained high resolution T! images with 1 mm<sup>3</sup> isotropic voxels.

Images were corrected for subject motion using a standardized package called MCFLIRT [65]. Images were spatially smoothed to reduce extreme values using a Gaussian kernel with a width of 5 mm. High pass temporal filtering (using a filter width of 100 s) was also applied to the data to reove low frequency drift artifacts.

The analysis was carried out in two steps using FSL 5.98 software [84,111,112] www.fmrib.ox.ac.uk/fsl. First, we estimated an equation of the form: Activation = b1\*Stop + b2\*NonStop + b3\*fixation + b4\*WhyStopQuestion + b5\*WhichProduct + error. The independent variables were dummies equal to one during the time that a screen was being viewed. So, for example, WhyStopQuestion was coded as “one” if the subject was viewing the screen when he was asked the question “Why did you choose to stop gathering information” and as “zero” otherwise. WhichProduct started as “one” during the times that the question “Which product is best for you?” appeared on the screen and was “zero” otherwise. Stop was the last three seconds of the search (i.e., the epoch during which subjects chose to stop) and NonStop was the remainder of the search (i.e., all the times when the subject chose to continue). Thus, the betas capture the average levels of activation when the subject was viewing that particular screen. Because the blood flow looks very much like a gamma distribution taking about six seconds to peak, we convolved each dummy variable with a gamma distribution to shift the measurement in time and strength to match the physiological realities of blood flow. This is a standard correction used in fMRI ex periments [61].

Next, all 21 subjects’ data were pooled and a random effects analysis using FSL’s Flame 1 + 2 [9] generated areas of significant activation across all subjects. At each voxel we tested the hypothesis b1-b2 > 0, which asks whether the activation for stopping is significantly greater than the average activation for non-stopping stimuli. We then generated a 3D map of all the significant voxels of activation using color to denote significance, which we overlaid on a picture of the brain. We controlled for multiple comparisons by retaining only contiguous clusters of sig nificant activation that are large enough to have occurred by chance less than 5% of the time [114,115]. Our results are robust against inflated false positive rates [47] based on various types of cluster and voxel thresholding analyses we performed. Full details of these robustness checks are available from the authors upon request.

## 5. Results

Subjects spent an average of 48.7 s (16.2 screens) searching for in formation. Searches of less than 9 s (3 screens) were discarded, so the range was 9 to 144 s and we had 428 usable searches out of 441 possible searches.

The contrast between the screen during which subjects chose to stop and all the other screens when they chose to continue yielded clusters of activation in the areas associated with stopping in motor skills tasks, a shown in Fig. 5. Like Swick et al. [100], whose results are shown in the top row of Fig. 5, we found bilateral activation across the anterior insula and putamen/thalamus (the four horizontal spots in the third and fourth images from the left on the bottom row; all subsequent references are also to the bottom row of the figure). We also found activation in the posterior cingulate (the dot in the middle of the fourth image from the right). We found activation in the right inferior frontal gyrus, right inferior parietal lobe, right middle frontal gyrus, and right superior frontal gyrus (the spots on the last two images on the right). Overall, our contrast shows strong activation in most of the known areas involved in stopping in motor skills tasks. Thus, the Stopping hypothesis (H1) is supported, suggesting a common mental process for stopping motor responses and search tasks, that is, a generalized stopping mechanism in cognition.

![](/api/attachments/FEKMHAHS/fulltext/images/2bfb2d1541f8256dabc25bac4422dfe63dba91f9cf8f6961a8817ea1e08cd1f2.jpg)  
Fig. 5. The top panel shows the areas proposed in the Stopping Hypothesis (H1). Reprinted from Neuroimage, 56(3), D. Swick, V. Ashley, U. Turken, Are the neural correlates of stopping and not going identical? Quantitative meta-analysis of two response inhibition tasks, pp. 1655–1665, Copyright 2011, with permission from Elsevier. The bottom panel shows areas of greater activation for stopping than for search in our data set. Lighter colors indicate greater levels of significance, e.g., yellow is greater than orange. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) [From the authors - We are not clear what this means, as we do not have any further interpretation.]

We also found activation beyond the areas known to be active in motor skills tasks, consistent with the Decision to Stop hypothesis (H2). There is additional activation in the thalamus (the lower center of the 6th image from the left in the bottom row). The thalamus is centrally located in the brain, and serves as a switchboard of sorts that helps focus attention on “…behaviorally relevant information from the environment ….” ([92], p. 211). Broadly, one can think of executive decisions about goal-directed behavior to reside in the front of the brain, while visual regions, which direct attention, lie in the back of the brain. The thalamus facilitates communication between the two. We also found extensive activation in the caudate (the upper center of the 6th image from the left). This region has been associated with learning in general [94] and goal directed learning [15].

The largest area of additional activation is in the visual cortex (the bottom part of all the images). There are particularly strong activations in the fusiform cortex, which is an area associated with the recognition of objects, faces, and words [4,14,46]. It is also implicated in the imagining of objects, faces, and words [51], and even in people who are blind [39].

We also examined the reverse contrast, in which there could be more activation during searching than stopping, and found no significant clusters of activation. Presumably, this is because during the stopping epoch the subject is still engaging in all of the search activity in addition to deciding to stop and implementing that decision. In other words, the person is still reading the information, storing it, updating perceptions, and pushing a button during the final slide. Thus, it seems that stopping is much more mentally demanding than simply searching.

## 6. Discussion

## 6.1. Discussion of results and implications for theory

Our goal in this paper was to discover the metabolic costs of searching and stopping to address a gap in understanding these phe nomena and to contribute to several different literatures. First, we establish that stopping behavior during information search activates the same areas that are active in motor skills tasks, suggesting a possible generalized stopping mechanism in the brain. Second, our findings contribute to an improved understanding of technostress, email and internet addiction, and other forms of extreme information intake that are now facilitated by the World Wide Web. If search is less cognitively costly than stopping, many types of extreme information intake are more easily explained and understood. Third, we contribute to the literature on information overload, because our findings reveal that people are likely to over-acquire information (since searching is cognitively less costly than stopping) and therefore are likely to experience information overload since working memory is quickly overwhelmed by the overacquisition of information.

The results of our investigation support both of our hypotheses. We observed activation of brain areas while subjects stopped information search that are also associated with stopping in motor skills tasks, and we observed activation beyond that associated with the decision to stop searching for information rather than simply the act of stopping. The most obviously striking result is simply the amount of activation in the brain during stopping. We must emphasize that this is relative activa tion. The comparisons are not to a baseline of zero, but rather to a baseline of searching for information. Thus, this is activation over and above what is necessary to read information, process it, update opinions about a product, and push a button.

As a general rule organisms are constructed to minimize metabolic costs. Brains are metabolically expensive to operate and strive to conserve energy whenever possible [70,77]. The extent of brain acti vation observed in our data suggests that stopping is cognitively costly. This means that there is probably an inherent bias against stopping in formation search and that not stopping may be the inherently preferred behavior (as further evidence, as noted, there are no significant clusters of activation within the brain in our data that are greater for searching than stopping). This can be problematic in an information rich envi ronment in the same way that the urge to continue (not stop) eating can be problematic in a calorie rich environment. Our information rich society may contribute to “information obesity,” in which we consume more information than we can process [16]. This suggests a significant problem given our limited cognitive capacity and time. Time spent searching for information about X necessarily limits the time spent making decisions, undertaking productive actions, and searching about Y. Given our well-known information processing limitations, especially in working memory, our brains are ill equipped to handle the quantities of information available to consume. Information overconsumption in terferes with consolidation of memories, and leads to information overload, attention exhaustion, ego depletion, and mental health prob lems such as internet addiction and technostress [8,26,54,56,60,67,90,102,108].

Current findings on the shallow processing of information through multi-tasking and information scanning suggest that information is seductive and that overconsumption is prevalent [16,26,66]. Our brains are hard-wired for very limited information intake; the severe limita tions on working memory attest to this fact [72,87]. However, just as we eat more in times of plenty (see, e.g., [58] for an evolutionary expla nation), we appear to circumvent our natural working memory limita tions through shallow processing and overconsume information when it is bountiful and easily accessible. And just as obesity in weight is a form of malnutrition [101,109], overconsumption of information and its consequent shallow processing lead to malnutrition in attention, pro cessing, and memory. Thus, since stopping is difficult in abundant en vironments (information, food, etc.), understanding the cognitive origins of stopping is critically important to improve human task per formance and welfare.

Information overconsumption is a problem that leads to many un desirable consequences, and our results provide new insights into extreme information intake. Internet addiction is a growing problem for people constantly tethered to their electronic devices [12,28,76,105,117], and technostress is a result of internet addiction and other real and perceived needs to interact on the web (e.g., [102]). Information overload (and email overload [99]) is another result of excessive information intake [8,60,68,90,108]. The results of our study suggest one reason for internet addiction, information overload, and other forms of extreme information intake—it is less cognitively (metabolically) demanding to continue to search for (and intake) in formation than it is to stop. This is an important insight and one that has not been previously suggested. It points to the need to devise ways of encouraging stopping through, for example, timed searches or other simple heuristics (e.g., pre-defined limits on the number of alternatives that will be considered in a decision problem) that limit information intake.

While there is a large literature on stopping in motor skills tasks, this is the first fMRI work to look at the decision to stop information search, and, as predicted, we found a great deal of activation beyond what would be expected from the act of stopping. While our results are a first step and are suggestive, they provide no definitive answers. We can, however, offer some thoughts about what those activations mean. The first concerns the thalamus, which coordinates goal-directed behavior with attention. It seems reasonable that this region would be activated during the time when a subject was deciding to stop. Stopping implies switching to a new task. In our investigation, this involved switching to a new object to evaluate or to choosing among objects already evaluated. In an everyday setting outside the laboratory, stopping information search often results in a similar switch, although it could also result in abandoning the search altogether or deferring it to a later time. In any case, there is some switching of attention and the thalamus should be active during this process.

The second area of clear activation is the caudate. The caudate is associated with a number of functions, including learning [11,25], memory [23], and imagining [34,82]. Activation in this area seems reasonable in the information search context because search requires a person to store information in memory for the purpose of learning about an item or idea.

There was also significant activation of the visual cortex. We reit erate that this was over and above the activation associated with searching, when the visual representation subjects saw was basically identical. We assume this is activation directed at reorienting attention (i.e., preparing to see new items), which is reasonable given that stop ping changes what a person will view.

The activation in the fusiform in particular suggests some important processes at work. In the present task people were asked to choose among products based on verbal descriptions of their characteristics. This might require creating a mental picture of the product—a task the fusiform would be well suited to handle, as the fusiform is implicated in imagining objects as well as recognizing them [33,41,51,64]. The important finding is that the fusiform showed heightened activation

during the stopping phase.

Prior research has examined the value of information [20,53] and the scent of information [40,83] as causes of search behavior. To these important constructs, based on our results, we add the concept of the exercise of executive control of stopping as an important factor in search behavior (which we can refer to as “volitional stopping” to emphasize that the stopping is voluntary or willful). Regardless of the costs and benefits of continuing search, in the presence of virtually unlimited in formation, the exercise of stopping behavior, i.e., volitional stopping, is the last step in the search process. Thus, an important omitted variable in the quest for an explanation of human search behavior is the user’s ability to exercise volitional stopping. Voluntariness has also been an important enhancement to other areas of IS research, such as the tech nology acceptance model [35,36,106].

We have also offered some insight for future theoretical research in information search and stopping. Existing theories have worked well in an environment with limited information, as the exercise of volitional stopping was not an issue if a user ran out of information to acquire. However, in a world of effectively unlimited information, as is the case with nearly all information systems with which users interact today, the ability of the user to voluntarily suspend his search process becomes increasingly important. Theories that do not take into account the IT artifact design features that impede or facilitate the exercise of volitional stopping will underperform. We have discussed three design featur es—infinite scrolling, limited lists, and prompts—that could impact stopping without changing the quality or quantity of information pro vided by an IT artifact. However, there are surely more and, given our results, IT researchers have a theoretical basis—the literature on stop ping in motor skills tasks—from which to draw arguments.

## 6.2. Implications for future research

This work has implications for research on individuals’ search opti mization, be it for personal or professional website searches, company database interfaces, or other electronic search venues. If people stop searching too quickly, they may miss information important to decision making. If they stop later than is necessary, time and energy (and money) are wasted. Research has shown that underacquisition and overacquisition of information are both problems in decision-making [31,81] and are costly. The higher the cognitive cost of stopping, the more likely that people will continue to search, since it delays the more costly (difficult) activity. As noted above, our results demonstrate the higher metabolic cost of stopping. If people are therefore more likely to over-acquire information, this represents a threat to the efficient acquisition of information for decision making. The use of appropriate stopping rules can lead to more accurate information acquisition and better use of decision makers’ time and money.

We noted above several areas of IT research that may benefit from our findings concerning searching and stopping. We have already dis cussed the web and the implications for stopping limitless searching possibilities. In addition, corporate databases and knowledge re positories may contain voluminous information and/or many postings on a topic of interest. Even if well categorized with appropriate key words, the amount of potential material may be vast. When should a person stop searching? We suggest that currently people stop using nothing but rudimentary heuristics. Another area of importance is in formation requirements determination for systems development. Ana lysts need to gather accurate and appropriate requirements to develop the system, but how does an analyst know when to stop gathering re quirements? Descriptive studies of stopping behavior in requirements determination have been performed (e.g., [17]), but much work remains and such work can benefit from an understanding of the metabolic costs of searching and stopping. These are just several examples. Virtually all areas of IT research and the development and use of IT artifacts involve information search in some way and therefore can benefit from an improved understanding of search and stopping. Information search and stopping are fundamental elements of the human experience [18,83,97] and therefore are relevant to most IT artifacts and people’s interactions with them.

There is also an opportunity for future research in addressing some of the limitations of the fMRI environment and this particular investiga tional design. We presented the information to subjects in a list, which we downloaded directly from Bestbuy.com. This in turn is the list of data fields for a particular product and is a very common way to display in formation. However, due to the fact that we needed to measure exactly when a person stopped, we presented this information an item at a time in a linear fashion, while an online user could have jumped around and gone back and forth between products and even different websites. This is also a limitation of the scanning environment because people only had four buttons for response. That makes it more difficult to navigate naturally in a scanner. Thus, it would be worthwhile to perform an experiment in which subjects navigated naturally or even to look at actual search data because natural navigation is very difficult in a lab. Of course, that involves a different research question, since cognitive stopping activity cannot be measured directly outside of a scanner. Nonetheless, triangulating on a phenomenon based on a variety of measurements can provide new insights.

Another limitation is that each attribute was displayed for exactly three seconds. The reason for this display is that it takes three seconds to acquire a full scan of the brain. Other brain imaging modalities, such as EEG [59] or galvanic skin responses [57], could be used to gain a better temporal resolution of the stopping procedure. This could help with understanding the order of the stopping process. Future research could use self-paced stopping tasks to gain a fuller understanding of the process.

An additional limitation is also likely due to the setting of the study in an fMRI chamber, and the probable desire (even if sub-conscious) by subjects not to remain in the chamber longer than necessary. As noted, subjects spent an average of 48.65 s searching for each product. For some products in a typical consumer setting this may be reasonable, especially if the person is already familiar with the product and knows more or less what he or she is seeking. However, for products such as a television set. less than a minute of search time seems too little. The environment of the fMRI chamber therefore limits ecological validity in some ways, but of course was necessary for our investigation. However, there is no reason to believe that our results will not generalize to typical search settings. People still need to search and stop, and the brain mechanisms involved should be the same regardless of how long searches last.

Finally, our data limit the detection of other factors that may influ ence searching and stopping. For example, users’ prior knowledge about a product (e.g., the person purchased a television within the past week) before searching and stopping was not measured [10,74]. Although it is necessary to isolate certain actions to measure in an fMRI experiment, knowledge of other factors that may impact the brain activity of interest, in this case searching and stopping, can add significantly to our under standing of the phenomenon of interest. Numerous additional fMRI studies would be needed to isolate other potentially relevant factors and to generate specific and testable hypotheses about them.

## 6.3. Implications for practice

There are implications for designers of IT artifacts when volitional stopping is included in a model of search behavior. Websites such as Facebook, which want users to search more and stick to the site, can use tools like infinite scrolling to impede the user’s ability to exercise control over stopping. However, not all IT designers will want to encourage search. Knowledge workers are estimated to spend up to 20% of their time searching for information [21,103]. The employers of these workers may want them to spend less time searching and more time engaging in other value creating activities. Similarly, consumer products companies may want to encourage purchases rather than searching (e.

$g _ { \cdot , }$ browsing). In both cases, companies can implement IT artifacts to facilitate the control of stopping. For example, they can provide fewer results and require users to actively seek more information if they desire it. Companies such as Google, Facebook, Amazon, Netflix, and most others limit the amount of information that is presented to users in terms of products, reviews, and choices generally.<sup>6</sup> Most people never leave the first page of Google’s search results [85], and Amazon.com only provides three to eight reviews of books (and, while it does not hide the “See all reviews” link, it does not particularly distinguish it with a larger font or a special button). It is arguable that most searchers do not notice these limitations, let alone object; if there were widespread outrage or many complaints the suppliers might change the appearance of the information.

There are numerous possible ways that the results of search could be presented that many people may argue are more ethical or fair. For example, Google could provide all its search results on one “page,” that is, have a very long scroll. Amazon and other retailers could provide many more reviews of their products. One issue with such a design is arguably people’s working memory capacity and attention span. The presentation of even 10 results on a page is more information than most people can hold in working memory [72]. Users of Google (and other sites) have the ability to change the default number of search results displayed per page and of course can also seek information beyond the first page, but as noted they rarely do so. While we, the authors, are always skeptical of the motives and behaviors of profit-seeking entities, in the case of search results it is arguable that the best advice is “user, heal thyself.” Another way to facilitate search without artificially limiting results might be to alert users when they have considered a certain number of options, read a certain number of reviews, searched the web or a database for a certain amount of time, etc. This would be a nudge that might prevent or reduce over-searching. It is important to note, however, that someone’s judgment would still be required to set the limits that trigger the alerts, and all human judgment is heuristic and nearly always sub-optimal [67]. The important point is that none of these suggestions concerns the quantity or quality of information; rather, it is about presenting information in a way that either facilitates or impedes the exercise of stopping behavior.

The inclusion of stopping as a construct in search behavior can also have implications for certain populations. Children, teenagers, people with attention deficit hyperactive disorder, the elderly, and people with various mental health issues can exhibit deficits in executive control of stopping behavior [79,93,110]. Designers of systems for use by these populations (e.g., educational information systems, healthcare infor mation systems, and some governmental information systems) need to consider how the ability to engage in volitional stopping may influence the amount of search that users undertake. For example, people in these populations may benefit from prompts to help them with stopping behavior.

## 7. Conclusion

In summary, we propose that IT artifacts that can provide a surplus of information fundamentally change the nature of search. Specifically, the user’s ability to exercise voluntary stopping in the search process be comes an important factor. We show this by measuring the activity of brain regions during a search task that are known to be associated with stopping in motor skills tasks. We find these brain areas to be signifi cantly more activated by users when they choose to stop a search task than during the remainder of the search task. This supports our theory that executive control of stopping is an important factor in how long a user will search for information, which is in turn a prime determinant of the information the user has available to make a decision. Further, we argue that IT artifacts can include design features that impede or facil itate stopping. We conclude that IT designers, IT users, and IT re searchers should consider voluntary stopping behavior during search to be an important factor when they build, interact with, and study IT artifacts.

## References

[1] A.S. Abrahams, R. Barkhi, Concept comparison engines: a new frontier of search, Decis. Support. Syst. 54 (2) (2012) 904–918.

[2] R.L. Ackoff, Management misinformation systems, Manag. Sci. 14 (4) (1967) B147–B156.

[3] E.J. Anderson, S.K. Mannan, G. Rees, P. Sumner, C. Kennard, Overlapping functional anatomy for working memory and visual search, Exp. Brain Res. 200 (2010) 91–107.

[4] T.J. Andrews, A. Clarke, P. Pell, T. Hartley, Selectivity for low-level features of objects in the human ventral stream, Neuroimage 49 (1) (2010) 703–711.

[5] I. Anurova, D. Artchakov, A. Korvenoja, R.J. Ilmoniemi, H.J. Aronen, S. Carlson, Differences between auditory evoked responses recorded during spatial and nonspatial working memory tasks, Neuroimage 20 (2) (2003) 1181–1192.

[6] A.R. Aron, M.A. Gluck, R.A. Poldrack, Long-term test-retest reliability of functional MRI in a classification learning task, Neuroimage 29 (3) (2006) 1000–1006.

[7] J.Y. Bakos, Reducing buyer search costs: implications for electronic marketplaces, Manag. Sci. 43 (12) (1997) 1676–1692.

[8] D. Bawden, L. Robinson, The dark side of information: overload, anxiety and other paradoxes and pathologies, J. Inf. Sci. 35 (2) (2009) 180–191.

[9] C.F. Beckmann, M. Jenkinson, S.M. Smith, General multilevel linear modeling for group analysis in FMRI, Neuroimage 20 (2) (2003) 1052–1063.

[10] T. Betsch, S. Haberstroh, A. Glockner, T. Haar, K. Fiedler, The effects of routine strength on adaptation and information search in recurrent decision making. Organ, Behav, Hum, Decis, Process, 84 (1) (2001) 23–53

[11] A. Bischoff-Grethe, E. Hazeltine, L. Bergren, R.B. Ivry, S.T. Grafton, The influence of feedback valence in associative learning, Neuroimage 44 (1) (2009) 243–251.

[12] J.J. Block, Issues for DSM-V: Internet addiction, in: Am Psychiatric Assoc, 2008.

[13] P. Bourke, S. Brown, E. Ngan, M. Liotti, Functional brain organization of preparatory attentional control in visual search, Brain Res. 1530 (2013) 32–43.

[14] W. Braet, J. Wagemans, H.P. Op de Beeck, The visual word form area is organized according to orthography, Neuroimage 59 (3) (2012) 2751–2759.

[15] A. Brovelli, B. Nazarian, M. Meunier, D. Boussaoud, Differential roles of caudate nucleus and putamen during instrumental learning, Neuroimage 57 (4) (2011) 1580-1590.

[16] S. Brown, Coping with information obesity: a diet for information professionals. Bus. Inf. Rey, 29 (3) (2012) 168–173.

[17] G.J. Browne, M.G. Pitts, Stopping rule use during information search in design problems, Organ, Behay, Hum, Decis, Process, 95 (2) (2004) 208–224.

[18] G.J. Browne, M.G. Pitts, J.C. Wetherbe, Cognitive stopping rules for terminating information search in online tasks, MIS Ouart 31 (1) (2007) 89–104.

[19] G.J. Browne, E.A. Walden, Is there a genetic basis for information search propensity? A genotyping experiment, MIS Quarterly 44 (2) (2020) 747–770.

[20] E. Brynjolfsson, Y. Hu, D. Simester, Goodbye pareto principle, hello long tail: the effect of search costs on the concentration of product sales, Manag, Sci. 57 (8) (2011) 1373–1386.

[21] J. Bughin, M. Chui, J. Manyika, Capturing business value with socia technologies, McKinsey Quarterly 4 (2012). http://www.mckinsey.com/industrie s/high-tech/our-insights/capturing-business-value-with-social-technologies.

[22] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decis. Support. Syst. 25 (3) (1999) 225–237.

[23] H. Burianova, A.R. McIntosh, C.L. Grady, A common functional brain network for autobiographical, episodic, and semantic memory retrieval, Neuroimage 49 (1) (2010) 865–874.

[24] J.R. Busemeyer, A. Rapoport, Psychological models of deferred decision making, J. Math. Psychol. 32 (2) (1988) 91–134.

[25] N. Canessa, M. Motterlini, F. Alemanno, D. Perani, S.F. Cappa, Learning from other people’s experience: a neuroimaging study of decisional interactive learning, Neuroimage 55 (1) (2011) 353–362.

[26] N. Carr, The Shallows: What the Internet is Doing to Our Brains, WW Norton & Company, 2010.

[27] CBS News. Brain Hack. 60 minutes. Available at. http://www.cbsnews.com news/brain-hacking-tech-insiders-60-minutes/. April 9. 2017.

[28] P. Chebbi, K.S. Koong, L. Liu, R. Rottman, Some observations on internet addiction disorder research. J. Inf. Syst. Educ. 1 (1) (2001) 3–4.

[29] A.D. Chevrier, M.D. Noseworthy, R. Schachar, Dissociation of response inhibition and performance monitoring in the stop signal task using event-related fMRI, Hum. Brain Mapp. 28 (12) (2007) 1347–1358.

[30] J. Chikazoe, K. Jimura, S. Hirose, K.-i. Yamashita, Y. Miyashita, S. Konishi, Preparation to inhibit a response complements response inhibition during performance of a stop-signal task, J. Neurosci. 29 (50) (2009) 15870–15877.

[31] T. Connolly, B.K. Thorn, Predecisional information acquisition: effects of task variables on suboptimal search strategies, Organ. Behav. Hum. Decis. Process. 39 (3) (1987) 397–416.

[32] A. Craig, How do you feel–now? The anterior insula and human awareness, Nat. Rev. Neurosci. 10 (1) (2009) 59.

[33] S.H. Creem-Regehr. J.A. Neil. H.J. Yeh. Neural correlates of two imagined egocentric transformations. Neuroimage 35 (2) (2007) 916–927.

[34] A. D’Argembeau, G. Xue, Z.L. Lu, M. Van der Linden, A. Bechara, Neural correlates of envisioning emotional events in the near and far future, Neuroimage 40 (1) (2008) 398–407.

[35] F.D. Davis, Perceived usefulness, Perceived Ease of Use, and User Acceptance of Information Technology, MIS Quarterly 13 (3) (1989) 319–340.

[36] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Manag, Sci. 35 (8) (1989) 982–1003.

[37] A.D. De Groot, Thought and choice in chess, Moulton Publishers, The Hague, 1978.

[38] B.G.C. Dellaert, G. Haubl, Searching in choice mode: consumer decision processes in product search with recommendations, J. Mark. Res. 49 (2) (2012) 277–288.

[39] A.G. De Volder, H. Toyama, Y. Kimura, M. Kiyosawa, H. Nakano, A. Vanlierde, M. C. Wanet-Defalque, M. Mishina, K. Oda, K. Ishiwata, M. Senda, Auditory triggered mental imagery of shape involves visual association areas in early blind humans, Neuroimage 14 (1 Pt 1) (2001) 129–139.

[40] A.R. Dennis, N.J. Taylor, Information foraging on the web: the effects of “acceptable” internet delays on multi-page information search behavior, Decis Support. Syst. 42 (2) (2006) 810–824.

[41] E.K. Diekhof, H.E. Kipshagen, P. Falkai, P. Dechent, J. Baudewig, O. Gruber, The power of imagination–how anticipatory mental imagery alters perceptual processing of fearful facial expressions, Neuroimage 54 (2) (2011) 1703–1714.

[42] A. Dimoka, How to conduct a functional magnetic resonance (FMRI) study in social science research, MIS Q. 36 (3) (2012) 811–840.

[43] A. Dimoka, F. Davis, Where Does TAM Reside in the Brain? The Neural Mechanisms Underlying Technology Adoption, in: Proceedings of the Twenty-Ninth International Conference on Information Systems. Paris. 2008

[44] A. Dimoka, P.A. Pavlou, F.D. Davis, Research commentary—NeuroIS: the potential of cognitive neuroscience for information systems research, Information Systems Research 22 (4) (2011) 687–702.

[45] A. Dimoka, et al., On the use of neurophysiological tools in IS research: developing a research agenda for NeuroIS, MIS Q. 36 (3) (2012) 679–702

[46] L. Dricot, B. Sorger, C. Schiltz, R. Goebel, B. Rossion, The roles of "face" and "nonface" areas during individual face perception: evidence by fMRI adaptation in a brain-damaged prosopagnosic patient. Neuroimage 40 (1) (2008) 318–332

[47] A. Eklund. T.E. Nichols, H. Knutsson, Cluster failure: why fMRI inferences for spatial extent have inflated false-positive rates, Proc. Natl. Acad. Sci. 113 (28 (2016) 7900–7905.

[48] N. Eyal, Infinite scroll: The Web’s slot machine, in: TechCruch, 2012.

[49] D.D. Fehrenbacher, S. Djamasbi, Information systems and task demand: an exploratory pupillometry study of computerized decision making, Decis. Support. Syst. 97 (2017) 1–11.

[50] N. Feng, H. Feng, D. Li, M. Li, Online media coverage, consumer engagement and movie sales: a PVAR approach, Decis. Support. Syst. 131 (2020), 113267.

[511 K. Fliessbach. S. Weis, P. Klaver, C.E. Elger. B. Weber, The effect of word concreteness on recognition memory, Neuroimage 32 (3) (2006) 1413–1421.

[52] P. Freeman, The secretary problem and its extensions: a review, in: International Statistical Review/Revue Internationale de Statistique., 1983, pp. 189–206

[53] A. Ghose, A. Goldfarb, S.P. Han, How is the mobile Internet different? Searc costs and local activities, Inform. Syst. Res. 24 (3) (2012) 613–631.

[54] M.S. Hagger, C. Wood, C. Stiff, N.L.D. Chatzisarantis, Ego depletion and the strength model of self-control: A meta-analysis, Psychol. Bull. 136 (4) (2010) 495–525.

[55] H.M. Simpson, S.M. Hale, Pupillary changes during a decision-making task, Percept. Mot. Skills 29 (2) (1969) 495–498.

[56] E.M. Hallowell, Overloaded Circuits: Why Smart People Underperform, Harvard

[57] A. Heinzl, E. Hemmer, Channel choice and human information stopping behavior: on the applicability of galvanic skin response in studies on human information behavior, in: Proceedings of the Gmunden Retreat on NeuroIS 3. 2011

[58] B. Heitmann, K. Westerterp, R. Loos, T. Sørensen, K. O’Dea, P. McLean, T. evolution and the environment. Obesity Reviews 13 (10) (2012) 90–922

[59] E. Hemmer, A. Heinzl, T. Neben, Information-seeking stopping behavior: on the role of information visibility created by other social actors, Proceedings of the Gmunden Retreat on NeuroIS 14 (2012)

[60] P. Hemp, Death by information overload, Harv. Bus. Rev. 87 (9) (2009) 82–89

[61] R. Henson, K. Friston, Convolution models for fMRI, in: K. Friston, et al. (Eds.), Statistical parametric mapping: The analysis of functional brain images, 2011,

[62] S.Y. Ho. D. Bodoff, K.Y. Tam. Timing of adaptive web personalization and its effects on online consumer behavior, Inform Syst Res 22 (3) (2011) 660–679

[63] W. Hong, J.Y. Thong, K.Y. Tam, The effects of information format and shopping task on consumers’ online shopping behavior: a cognitive fit perspective,

[64] A. Ishai, J.V. Haxby, L.G. Ungerleider, Visual imagery of famous faces: effects of memory and attention revealed by fMRI, Neuroimage 17 (4) (2002) 1729–1741.

[65] M. Jenkinson, P. Bannister, M. Brady, S. Smith, Improved optimization for the robust and accurate linear registration and motion correction of brain images, Neuroimage 17 (2) (2002) 825–841.

[66] C.A. Johnson, The information diet: A case for conscious consumption, O’Reilly Media. 2012.

[67] D. Kahneman, Thinking, Fast and Slow, Farrar, Straus and, Giroux, New York, 2011.

[68] T. Klingberg, The overflowing brain: information overload and the limits of working memory. Oxford University Press.. 2008

[69] C.A. Kogut. Consumer search behavior and sunk costs, J. Econ. Behav. Organ. 14 (3) (1990) 381–392.

[70] S.B. Laughlin, T.J. Sejnowski, Communication in neuronal networks, Science 301 (5641) (2003) 1870–1874.

[71] D.V. Lindley, Dynamic programming and decision theory, Appl. Stat. (1961) 39–51.

[72] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychol. Rey, 63 (2) (1956) 81–97.

[73] C. Mogilner, B. Shiv, S.S. Iyengar, Eternal Quest for the Best: Sequential (vs. Simultaneous) Option Presentation Undermines Choice Commitment, J. Consumer Res. 39 (6) (2013) 1300–1312.

[74] S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, J. Consum. Res. 23 (1997) 263–277.

[75] S.H. Mostofsky, D.J. Simmonds, Response inhibition and response selection: two sides of the same coin, J Cognitive Neurosci 20 (5) (2008) 751–761.

[76] H. Nakata, K. Sakamoto, A. Ferretti, M.G. Perrucci, C. Del Gratta, R. Kakigi, G. L. Romani, Negative BOLD effect on somato-motor inhibitory processing: an fMRI study, Neurosci. Lett. 462 (2) (2009) 101–104.

[77] A. Navarrete, C.P. van Schaik, K. Isler, Energetics and the evolution of human brain size, Nature 480 (7375) (2011) 91–93.

[78] A. Newell, On the Analysis of Human Problem Solving Protocols, in: P.P. N. Johnson-Laird, P.C. Wason (Eds.), Thinking – Readings in Cognitive Science, Cambridge University Press, Cambridge, 1977, pp. 46–61.

[79] A.J. Oldehinkel, C.A. Hartman, R.F. Ferdinand, F.C. Verhulst, J. Ormel, Effortful control as modifier of the association between negative emotionality and adolescents' mental health problems. Dey. Psychopathol, 19 (2) (2007) 523–539

[80] J.W. Payne, J.R. Bettman, E.J., The Adaptive Decision Maker, Cambridge University Press, Cambridge, 1993.

[81] J.W. Payne, J.R. Bettman, M.F. Luce, When time is money: decision behavior under opportunity-cost time pressure, Organ. Behav. Hum. Decis. Process. 66 (2) (1996) 131–152.

[82] M.L. Pelchat, A. Johnson, R. Chan, J. Valdez, J.D. Ragland, Images of desire: foodcraving activation during fMRI. Neuroimage 23 (4) (2004) 1486–1493.

[83] P. Pirolli, S. Card. Information foraging, Psychol, Rey, 106 (4) (1999) 643

[84] J.B. Poline. K.J. Worsley. A.C. Evans. K.J. Friston. Combining spatial extent and peak intensity to test for activations in functional imaging. Neuroimage 5 (2) (1997) 83–96.

[85] L. Ray, We surveyed 1,400 searchers about google - here’s what we learned available at https://moz.com/blog/new-google-survey-results. Accessed 10/29/ 20.

[86] D. Reinsel, J. Gantz, J. Rydning, The Digitization of the World from Edge to Core, International Data Corporation White Paper, 2018. Available at, https://storelabs .org/media/idc-seagate-dataage-whitepaper.pdf.

[87] D. Reisberg, Cognition, 7th ed., Norton & Company, New York, 2018.

[88] W.R. Reitman, Cognition and Thought: An Information-Processing Approach, Wiley, New York, 1965.

[89] A. Riaz, S. Gregor, S. Dewan, Q. Xu, The interplay between emotion, cognition and information recall from websites with relevant and irrelevant images: a neuro-IS study, Decis. Support. Syst. 111 (2018) 113–123.

[90] P.G. Roetzel. D.D. Fehrenbacher, On the role of information overload in information systems (IS) success: Empirical evidence from decision support systems, in: 40th International Conference on Information Systems (ICIS), Munich, 2019.

[91] G. Saad, J.E. Russo, Stopping criteria in sequential choice, Organ. Behav. Hum. Decis. Process. 67 (3) (1996) 258–270.

[92] Y.B. Saalmann, S. Kastner, Cognitive and perceptual functions of the visua thalamus, Neuron 71 (2) (2011) 209–223.

[93] R. Schachar, V.L. Mota, G.D. Logan, R. Tannock, P. Klim, Confirmation of an inhibitory control deficit in attention-deficit/hyperactivity disorder. J. Abnorm Child Psychol, 28 (3) (2000) 227–235

[94] C.A. Seger, K. Braunlich, H.S. Wehe, Z. Liu, Generalization in category learning: the roles of representational and decisional uncertainty, J. Neurosci. 35 (23) (2015) 8802–8812.

[95] H.A. Simon, Designing organizations for an information-rich world, in: M. Greenberger (Ed.), Communication, and the Public Interest, The Johns Hopkins Press, Baltimore, 1971.

[96], H.A. Simon, The structure of ill structured problems, Artif, Intell, 4 (3) (1974)

[97] H.A. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1996.

[98] G.J. Stigler, The economics of information, J. Polit. Econ. 69 (3) (1961) 213–225.

[99] J.-F. Stich, M. Tarafdar, P. Stacey, C. Cooper, Appraisal of email use as a source of workplace stress: A person-environment fit approach, J. Assoc. Inform. Syst. 20 (2) (2019). https://doi.org/10.17705/1iais.00531.

[100] D. Swick, V. Ashley, U. Turken, Are the neural correlates of stopping and not going identical? Quantitative meta-analysis of two response inhibition tasks, Neuroimage 56 (3) (2011) 1655–1665.

[1011 S.A. Tanumihardio. C. Anderson. M. Kaufer-Horwitz. I. Bode. N.J. Emenaker. A M. Hagg. J.A. Satia. HJ. Silver. D.D. Stadler. Poverty. obesity. and malnutrition an international perspective recognizing the paradox, J. Am. Diet. Assoc. 107 (11) (2007) 1966–1972.

[102] M. Tarafdar, Q. Tu, T.S. Ragu-Nathan, Impact of technostress on end-user satisfaction and performance, J. Manage. Info Syst. 27 (3) (2011) 303–334.

[103] E. Trapasso, Managers say the majority of information obtained for their work is useless, Accenture survey finds, in: Accenture News Release, 2007.

[104] O. Turel, A. Serenko, P. Giles, Integrating technology addiction and use: an empirical investigation of online auction users, MIS O. 35 (4) (2011) 1043–1062.

[105] O. Turetken, R. Sharda, Development of a fisheye-based information search processing aid (FISPA) for managing information overload in the web environment, Decis. Support. Syst. 37 (3) (2004) 415–434.

[106] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: four longitudinal field studies, Manag. Sci. 46 (2) (2000) 186–204.

[107] E. Vul, C. Harris, P. Winkielman, H. Pashler, Puzzlingly high correlations in fMRI studies of emotion, personality, and social cognition, Perspect. Psychol. Sci. 4 (3) (2009) 274–290.

[108] K.E. Weick, K.M. Sutcliffe, Information overload revisited, in: The Oxford Handbook of Organizational Decision Making, 2008, pp. 56–75.

[109] J.C. Wells, Obesity as malnutrition: the role of capitalism in the obesity globa epidemic, Am. J. Hum. Biol. 24 (3) (2012) 261–276.

[110] B.R. Williams, J.S. Ponesse, R.J. Schachar, G.D. Logan, R. Tannock, Development of inhibitory control across the life span, Dev. Psychol. 35 (1) (1999) 205.

[111] A.M. Winkler, G.R. Ridgway, M.A. Webster, S.M. Smith, T.E. Nichols, Permutation inference for the general linear model, Neuroimage 92 (2014) 381–397.

[112] M.W. Woolrich, T.E. Behrens, C.F. Beckmann, M. Jenkinson, S.M. Smith, Multilevel linear modelling for FMRI group analysis using Bayesian inference Neuroimage 21 (4) (2004) 1732–1747.

[113] D.K. Wong, M.-K. Cheung, Online Health Information Seeking and eHealth Literacy among Patients Attending a Primary Care Clinic in Hong Kong: A Cross Sectional Survey, J. Med. Internet Res. 21 (3) (2019), e10831.

[114] K. Worsley, Statistical analysis of activation images, in: P.M.M.a.S.M.S. P. Jezzard

[115] K.J. Worsley. C.H. Liao, J. Aston. V. Petre. G.H. Duncan. F. Morales. A.C. Evans A general statistical analysis for fMRI data. Neuroimage 15 (1) (2002) 1–15.

[116] Q. Xu, S. Gregor, Q. Shen, Q. Ma, W. Zhang, A. Riaz, The power of emotions in online decision making: A study of seller reputation using fMRI, Decision Support Systems 31 (2020) 1–11

[117] Z. Xu, O. Turel, Y. Yuan, Online game addiction among adolescents: motivation and prevention factors, Eur. J. Inf. Syst. 21 (3) (2012) 321–340.

[118] D. Yin, S.D. Bond, H. Zhang, Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews, MIS Quarterly 38 (2) (2014) 539–560.

Glenn J. Browne is the Jerry S. Rawls Chair and Professor of Information Systems & Decision Sciences at the Rawls College of Business at Texas Tech University. He received his Ph.D. from the University of Minnesota. His research focuses on cognitive and behavioral issues in managerial decision making, systems development, and project management. Particular areas of interest include information search, stopping rules, in formation requirements determination, and decision-making processes. His publications have appeared in MIS Quarterly, Management Science, Organizational Behavior and Human Decision Processes, Journal of the Association for Information Systems, Journal of Management Information Systems, Journal of Behavioral Decision Making, Decision Sciences, Information Systems Journal, and other journals. He is co-author of a paper published in Journal of the AIS that was named one of the top five papers in the Information Systems discipline for 2009.

Eric A. Walden received his Ph.D. from the University of Minnesota, and is currently the James C. Wetherbe Professor of Information Systems and Ouantitative Sciences at the Rawls College of Business at Texas Tech University. He is also the director of the Texas Tech Neuroimaging Institute, and the founder and first director of the Master of Science program in Data Science at Texas Tech. His prior research has appeared in MIS Quarterly, Harvard Business Review, Journal of the AIS, Information Systems Research and Neuroimage. He has been awarded the AIS Senior Scholars' “Best Publication's Award." Journal of the Association of Information Systems, and named to the Journal of the Association of Information Systems Reviewer Hall of Fame.
