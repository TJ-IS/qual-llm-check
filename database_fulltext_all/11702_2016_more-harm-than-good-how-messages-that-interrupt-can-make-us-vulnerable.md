---
otero_id: 11702
otero_key: "NVMGEYF8"
title: "More Harm Than Good? How Messages That Interrupt Can Make Us Vulnerable"
authors: "Jeffrey L. Jenkins; Bonnie Brinton Anderson; Anthony Vance; C. Brock Kirwan; David Eargle"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0644"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [37.187.7.74] On: 20 August 2016, At: 19:48 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/NVMGEYF8/fulltext/images/c68775442eedcb69c15da9f1219b6695332173f6e2bf17aad1eafafa6549be91.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## More Harm Than Good? How Messages That Interrupt Can Make Us Vulnerable

Jeffrey L. Jenkins, Bonnie Brinton Anderson, Anthony Vance, C. Brock Kirwan, David Eargle

To cite this article:

Jeffrey L. Jenkins, Bonnie Brinton Anderson, Anthony Vance, C. Brock Kirwan, David Eargle (2016) More Harm Than Good? How Messages That Interrupt Can Make Us Vulnerable. Information Systems Research

Published online in Articles in Advance 16 Aug 2016

http://dx.doi.org/10.1287/isre.2016.0644

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/NVMGEYF8/fulltext/images/fcc49f4d7489df44679577345c709c0c82e65467259b2fcb2a61487797bf48e4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# More Harm Than Good? How Messages That Interrupt Can Make Us Vulnerable

Jeffrey L. Jenkins, Bonnie Brinton Anderson, Anthony Vance Information Systems Department, Marriott School of Management, Brigham Young University, Provo, Utah 84602 {jeffrey\_jenkins@byu.edu, bonnie\_anderson@byu.edu, anthony@vance.name}

C. Brock Kirwan

Department of Psychology and Neuroscience Center, Brigham Young University, Provo, Utah 84602, kirwan@byu.edu

David Eargle

Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, Pennsylvania 15260, dave@daveeargle.com

ystem-generated alerts are ubiquitous in personal computing and, with the proliferation of mobile devices, Sdaily activity. While these interruptions provide timely information, research shows they come at a high cost in terms of increased stress and decreased productivity. This is due to dual-task interference (DTI), a cognitive limitation in which even simple tasks cannot be simultaneously performed without significant performance loss. Although previous research has examined how DTI impacts the performance of a primary task (the task that was interrupted), no research has examined the effect of DTI on the interrupting task. This is an important gap because in many contexts, failing to heed an alert—the interruption itself—can introduce critical vulnerabilities.

Using security messages as our context, we address this gap by using functional magnetic resonance imaging (fMRI) to explore how (1) DTI occurs in the brain in response to interruptive alerts, (2) DTI influences message security disregard, and (3) the effects of DTI can be mitigated by finessing the timing of the interruption. We show that neural activation is substantially reduced under a condition of high DTI, and the degree of reduction in turn significantly predicts security message disregard. Interestingly, we show that when a message immediately follows a primary task, neural activity in the medial temporal lobe is comparable to when attending to the message is the only task.

Further, we apply these findings in an online behavioral experiment in the context of a web-browser warning. We demonstrate a practical way to mitigate the DTI effect by presenting the warning at low-DTI times, and show how mouse cursor tracking and psychometric measures can be used to validate low-DTI times in other contexts.

Our findings suggest that although alerts are pervasive in personal computing, they should be bounded in their presentation. The timing of interruptions strongly influences the occurrence of DTI in the brain, which in turn substantially impacts alert disregard. This paper provides a theoretically grounded, cost-effective approach to reduce the effects of DTI for a wide variety of interruptive messages that are important but do not require immediate attention.

Keywords: multitasking; dual-task interference; security message; information security; Amazon Mechanical Turk; laboratory experimentation; fMRI; NeuroIS

History: Rob Fichman, Ram Gopal, Alok Gupta, Sam Ransbotham, Senior Editors; Alok Gupta, Associate Editor. This paper was received on March 1, 2015, and was with the authors 1 month for 1 revision. Published online in Articles in Advance August 16, 2016.

## 1. Introduction

System-generated alerts are a ubiquitous aspect of the user computing experience (Mark et al. 2012). While these interruptions can provide benefits in the form of timely information, an extensive body of research in the field of human-computer interaction (HCI) has shown that they can have a substantial negative impact in terms of reduced productivity (McFarlane 2002), increased stress (Mark et al. 2008), and increased task-completion time (Iqbal and Horvitz 2007). This is because of the phenomenon of dual-task interference (DTI), a limitation of the human cognitive system in which the human brain must rapidly switch attention between multiple tasks that are being attempted at the same time (Pashler 1994). Research indicates that when people attempt even simple tasks simultaneously, the tasks can “interfere with each other quite drastically, even though they are neither intellectually challenging nor physically incompatible” (Pashler 1994, p. 220).

Although previous research has examined how DTI impacts primary task performance (Pashler 1994)— the task that was interrupted—no research has examined the effect of DTI on the interrupting task itself— the system-generated alert. Responses to systemgenerated alerts are susceptible to DTI because they are typically secondary tasks that interrupt the completion of a users’ primary task of using a computer. Whereas performance of the primary task is considered important, carefully attending to the interrupting message is critically important in many contexts, such as information privacy and security (Jenkins and Durcikova 2013, Patil et al. 2015), healthcare (Phansalkar et al. 2013), and avionics (McFarlane and Latorella 2002), to name a few. However, it is unclear how the performance of an interruptive message is impacted by its interference with a primary task (see Figure 1).

To address this research gap, our objectives are threefold. First, we aim to explore how DTI occurs in the brain in response to interruptive messages. To do so, we take a NeuroIS approach—the application of neuroscience methods to information systems (IS)— which excels at revealing hidden mental processes “that are difficult or even impossible to measure with existing measurement methods and tools” (Dimoka et al. 2011, p. 688). Specifically, we used functional magnetic resonance imaging (fMRI) to observe DTI as it occurs in the brain in response to an interruptive message and a competing primary task (Anderson et al. 2016a). Second, we seek to explain how DTI in the brain causes people to disregard the message. Third, we intend to determine how to reduce DTI for interrupting messages by finessing their timing. HCI research on interruptions suggests that the severity of an interruption can be reduced by introducing it at a more opportune moment (Adamczyk and Bailey 2004). Accordingly, we examined how DTI can be reduced when an alert is introduced between the completion of primary tasks (see Figure 2).

We address these gaps in the context of interruptive security messages—messages that prompt the user to perform a security action. While some security messages require immediate attention (such as Web browser Secure Sockets Layer (SSL) warnings), many others do not (e.g., software update, backup, and malware scan notifications). Notwithstanding their importance, people often behave against the security message’s recommended course of action—a behavior known as security message disregard (Vance et al. 2014). Thus, the context of a security message is both important and appropriate for understanding how DTI influences users’ responses to system-generated alerts.

Figure 2 (Color online) Observing the Effect of DTI on the Secondary Task When it Occurs After (Rather Than During) a Primary Task  
![](/api/attachments/NVMGEYF8/fulltext/images/5d01fe2593924c261547cd6ce09da811ed5854ce98bfc58d3e2dba8790804a2f.jpg)

We pursue our research objectives through two complementary studies—an fMRI laboratory experiment involving permission warnings and a realistic online behavioral experiment. First, we show that neural activation in the medial temporal lobe (MTL)— a brain region associated with declarative memory— is substantially reduced under a condition of high DTI, which in turn significantly predicts security message disregard. Interestingly, we show that when a message immediately follows a primary task, neural activity in the MTL is comparable to when attending to the message is the only task. Second, we apply the fMRI findings to an online behavioral experiment in the context of a Web browser warning. We demonstrate a practical way to mitigate the DTI effect by presenting the warning at low-DTI times, and show how mouse cursor tracking and psychometric measures can be used to validate low-DTI times in other contexts.

Our findings suggest that although alerts are pervasive in personal computing, they should be bounded in their presentation. The timing of interruptions strongly influences the occurrence of DTI in the brain, which in turn substantially impacts alert disregard. This paper provides a theoretically grounded, costeffective approach to reduce the effects of DTI for a wide variety of interruptive messages that are important but do not require immediate attention.

Figure 1 (Color online) Observing the Effect of DTI on the Secondary Task—The System-Generated Alert—(b) Rather Than the Primary Task (a)  
![](/api/attachments/NVMGEYF8/fulltext/images/6d28b8fdca3782cc41a5ada1a9eca6445d10ec76d5cd39a702757bf22043a85e.jpg)

## 2. Literature Review and Theory

An area of literature known as interruption science documents that interruptions often decrease users’ performance of a primary task (Iqbal and Bailey 2010). This is particularly true in computer-mediated environments, as a substantial body of research shows that interruptions during computing tasks result in reduced productivity (McFarlane 2002), increased stress (Mark et al. 2008), and increased time required to complete the task (Iqbal and Horvitz 2007).

Although not empirically validated, interruptions have also been suggested to influence people’s responses to system-generated alerts—the interruptions themselves—particularly in the context of security messages. Yee argues that “interrupting users with prompts presents security decisions in a terrible context: it teaches users that security issues obstruct their main task and trains them to dismiss prompts quickly and carelessly” (Yee 2004, p. 49). Bravo-Lillo et al. (2011) suggest that interruptive security warnings are often ignored or suboptimally addressed because users have a limited cognitive ability to switch between tasks. Patil et al. (2015) found that interruptive privacy notices on mobile devices are poorly attended to. These findings are consistent with DTI theory, which we describe next.

## 2.1. Dual-Task Interference Theory

DTI is a powerful theoretical lens for explaining why interruptions impact and are impacted by concurrent tasks. It has been used to explain performance decrements in a variety of contexts, including driving while talking on the phone (Strayer and Johnston 2001), searching concurrently for multiple pieces of information (Navon and Miller 1987), and texting while walking (Plummer et al. 2015). Normally, people are not aware of tasks interfering with each other unless the two tasks are cognitively difficult, physically incompatible, or evoke emotional reactions. However, just the opposite is actually true: when people are involved in even simple cognitive tasks, they cannot process information or perform behaviors related to other tasks as effectively (e.g., Logan 1978).

In the IS literature, DTI has proved a useful reference theory. For example, Heninger et al. (2006) investigated the role of DTI in group support systems, finding that groups using synchronous text discussions were not able to process the new information they were receiving, which led to lower decision quality. Shaft and Vessey (2006) explored DTI in the context of software comprehension and modification, and found that DTI caused conflict between the performance of these two tasks. Cameron and Webster (2013) studied how IT can facilitate multiple overlapping conversations, and found that DTI worsened relational outcomes. Finally, Jenkins and Durcikova (2013) used DTI as an explanation of why people fail to follow security education training. However, none of these studies considered the effect of DTI on an interrupting secondary task. We address this theoretical gap by extending DTI theory to explain the degradation of performance for the interrupting task.

DTI typically occurs under one of two paradigms: bisensory and divided attention (Szameitat et al. 2011). Under the bisensory paradigm, people engage in two tasks simultaneously, such as walking and talking. By contrast, under the divided attention paradigm, people switch attention between stimuli, such as when a system-generated alert interrupts a primary task. In this context, two primary models explain why DTI occurs: (1) the capacity-sharing model and (2) the bottleneck model.

The capacity-sharing model assumes that people share mental capacity among tasks (Tombu and Jolicœur 2003). Because humans have finite cognitive resources (Marois and Ivanoff 2005), performance is impaired when multiple tasks are performed together, as less cognitive capacity is available for each individual task (Tombu and Jolicœur 2003). Second, the bottleneck (task-switching) model explains that parallel processing may be impossible for certain mental operations (Dux et al. 2006, Pashler 1994, Sigman and Dehaene 2006). This model assumes various cognitive mechanisms are used to process information and operations. If two tasks require the same constrained mechanism at the same time, one or both of the tasks will be delayed or impaired (Navon and Miller 2002). This limitation is referred to as a bottleneck. With any task, there could be a single or multiple bottlenecks that can affect performance.

The capacity-sharing and bottleneck models have been extensively studied as alternative explanations of dual-task interference. Kahneman (1973) was among the earliest to propose the two competing models. Since then, various studies in neuroscience and psychology have explored which model is the most salient predictor of dual-task interference. Researchers using fMRI and other neural methods observe support for both models; although, depending on the context, researchers frequently find different brain regions that are influenced by DTI. For example, capacity-sharing and bottleneck effects have been observed in the lateral prefrontal cortex, superior medial frontal cortex (Marois and Ivanoff 2005), lateral parietal cortex, visual cortex, dorsal premotor cortex (Dux et al. 2006), bilateral visual occipitotemporal cortices, bilateral superior temporal auditory cortices, motor, premotor, and cerebellar cortices (Sigman and Dehaene 2008), to name a few. Hence, for a given context it is important to understand how DTI occurs in the brain and which brain regions are affected to minimize DTI. In this study, we answer these questions in a system-generated alert setting, allowing us to present system-generated alerts in such a way to reduce the effects of DTI. In the following experiments described in Sections 3 and 4, we use the capacity-sharing and bottleneck models to hypothesize why DTI affects security message disregard.

## 2.2. Reducing DTI Through Intelligent Timing of Interruptions

Our third objective stated in Section 1 is to reduce DTI for interrupting messages. Research has identified three main factors that influence the severity of interruptions: (1) the delay of interruption, (2) the complexity of the interrupting secondary task, and (3) the timing of the interruption (Borst et al. 2015). In the case of timing, researchers have sought to minimize the impact of an interruption by presenting the interruption at an opportune moment (McFarlane 2002). However, it is still not clear how to best identify such moments (Adamczyk and Bailey 2004). Nonetheless, this research generally shows that the impact of the interruption on a primary task can be reduced through some form of intelligent timing. In Section 3, we examine how DTI occurs in the brain in response to interruptive messages, and how intelligent timing can reduce this effect.

## 3. Experiment 1—fMRI

In Experiment 1, we conduct an fMRI study to explore how DTI influences users’ responses to interruptive messages. Specifically, we examine how DTI influences security message disregard—behaving against the security message’s recommended course of action (Vance et al. 2014)—in a security-warning context. Experiment 1 encompasses three classes of hypotheses— fMRI, behavioral, and fMRI–behavioral—which we summarize in Figure 3.

## 3.1. Experimental Context

For the fMRI and the behavioral hypotheses, we predict that higher DTI will result in lower activation of relevant brain regions (in this case, the medial temporal lobe; see below) and higher security warning disregard. For the integrated fMRI–behavioral hypotheses, we predict that lower activation of relevant brain regions under a condition of higher DTI will lead to higher security warning disregard.

The task described in Section 3.2 has a primary working-memory task and a long-term declarativememory task as the interrupting security task. Working memory refers to the initial encoding and manipulation of information and requires sustained rehearsal and/or attention to maintain that information during a delay (Baddeley 2012), while long-term declarative memory refers to the ability to maintain representations of facts and events over a delay that does not include active maintenance of the information. Declarative memory is critically dependent on MTL structures, including the hippocampus (Squire et al. 2004). Declarative memory typically stores information that is remembered longer than 15–30 seconds without continual rehearsal (Atkinson and Shiffrin 1971), although the MTL can be engaged over short delays (see Jeneson and Squire 2012). Accordingly, recalling security training information, even very recent training, requires use of declarative memory (Friedman and Goldman-Rakic 1988) and will result in neural activation changes in the MTL.

3.1.1. High-DTI vs. Warning Only. Conditions of high-DTI (responding to an interruptive security message) result in lower activation in the MTL associated with recalling security information than in the warning-only task (i.e., only responding to the security message). Consistent with the capacity-sharing model, the brain often cannot meet the demands of the multiple tasks simultaneously (e.g., responding to a warning in the middle of another primary task). Thus, DTI inhibits one’s ability to maintain multiple MTLdependent representations in response to the security message. For example, Schon et al. (2016) suggest that during working memory maintenance periods, declarative memory retrieval may be inhibited because of limited cognitive resources availability.

Likewise, the bottleneck model predicts that performing the primary task and responding to the security message may be cognitively incompatible. In one scenario, unless a user releases the cognitive resource from the primary task, it is impossible for the user to activate MTL-dependent representations to process the security message. In another scenario, the user may switch tasks, but in anticipation of continuing the primary task, may not expend as extensively MTL-dependent cognitive resources (Dux et al. 2006, Pashler 1994, Sigman and Dehaene 2006). In either case, neural activation in the MTL decreases. Thus, we hypothesize the following:

Figure 3 (Color online) Overview of Three Classes of Hypotheses in Experiment 1  
![](/api/attachments/NVMGEYF8/fulltext/images/db9b90abcb86b12c3bba70730ec955712052d39e3888924dda3c32b723d2942c.jpg)

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> In the MTL region of the brain, activity will be lower under the high-DTI condition as compared to the warning-only condition.

We also predict that users will have greater security message disregard under conditions of high-DTI (i.e., when presenting the security message in the middle of another task) compared to when they are only completing the secondary warning-only task (i.e., when only responding to security messages). Literature has extensively validated the relationship between DTI and task performance even in simple tasks (Pashler 1994). For example, when short-term memory is consumed by asking people to memorize a simple piece of information, performance on tasks, such as their speed in classifying stimuli and information, decreases (Logan 1978).

In the context of both models of DTI, the decreased activation in the MTL resulting from high-DTI suggests that users were not able to access information from declarative memory to assess the security message. Performance will thereby decrease, as security behavior was informed possibly by inadequate information and processing. Unless a user releases the cognitive resources from the primary task, it may be impossible for the user to process the security message and the user will simply disregard it (Dux et al. 2006, Pashler 1994, Sigman and Dehaene 2006). In either case, performance decreases.

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> Security message disregard will be higher under the high-DTI condition as compared to the warning-only condition.

Building on our previous hypotheses, if high-DTI decreases activity in the MTL (H1) and this decrease explains why security message disregard will be higher in high-DTI conditions (H2), we hypothesize that the difference in MTL activation between high-DTI and warning-only tasks should predict the change in security message disregard between the two conditions. In summary, we have the following:

<sup>Hypothesis</sup> <sup>3</sup> <sup>(H3).</sup> Between the warning-only and high-DTI conditions, a decrease in activation of the MTL will predict an increase in security warning disregard.

3.1.2. High-DTI vs. Low-DTI. Similar to H1, we predict that conditions of high DTI will result in less activation in the MTL than conditions of low DTI. As previously discussed, responding to a security message after a primary task is not immune to DTI. The bottleneck model explains that switching between tasks causes interference that decreases task performance (Pashler 1994). Research shows that people’s responses are usually more error prone and slower following a task switch (Monsell 2003). In high-DTI scenarios, users must switch between tasks many times to accomplish both (much like a computer switches between threads to run multiple programs). However, unlike conditions of high DTI, the user only needs to switch between tasks once in a low-DTI condition (at the end of the primary task to respond to the security message). This decrease in task switching reduces the amount of interference (Dux et al. 2006).

Likewise, when a security message is presented after a task (low DTI), the primary task and the security message do not compete for the same limited cognitive resources—i.e., users may fully devote available cognition to one task and then the other after accounting for the DTI of the switching cost. As such, the capacity-sharing model also predicts that DTI will be less in conditions of low DTI compared to high DTI.

Activation in the MTL will likely be higher under conditions of low DTI than conditions of high DTI. After the impact of switching tasks, the brain can activate MTL-dependent representations as needed to perform the security task, whereas this ability is restricted in conditions of high DTI. We therefore hypothesize the following:

<sup>Hypothesis</sup> <sup>4</sup> <sup>(H4).</sup> For the MTL region of the brain, activity will be lower under the high-DTI condition compared to the low-DTI condition.

Similar to H2, we also hypothesize that performance under conditions of high DTI will be lower than under conditions of low DTI. When a security message does not interrupt another task, responding to the security messages does not compete for cognitive resources as much. Hence, one has access to more cognitive resources to activate the MTL to more ideally respond to the security message, resulting in less security message disregard. The capacity-sharing and bottleneck models of DTI would therefore predict improved performance (Pashler 1994). Consequently, we hypothesize the following:

<sup>Hypothesis</sup> <sup>5</sup> <sup>(H5).</sup> Security message disregard will be higher under the high-DTI condition as compared to the low-DTI condition.

Building on our previous hypotheses, if high DTI decreases activity in the MTL compared with low DTI (H4) and this decrease explains why security message disregard will be higher in high-DTI versus low-DTI conditions (H5), we hypothesize that the difference in MTL activation between high-DTI and low-DTI conditions should predict the change in security message disregard. In summary, we have the following:

Figure 4 (Color online) Example Permission Warning  
![](/api/attachments/NVMGEYF8/fulltext/images/7abfd48745b860b2bda9ac7f46649ac46e6474a45c2ca15335fb79a50ff3d133.jpg)

<sup>Hypothesis</sup> <sup>6</sup> <sup>(H6).</sup> Between the low-DTI and high-DTI conditions, a decrease in activation of the MTL will predict an increase in security warning disregard.

## 3.2. Methodology

To test our hypotheses, we utilized a repeatedmeasure experimental design that required participants to respond to security warnings that either interrupted or did not interrupt a primary task. For the primary task, subjects were asked to memorize or encode a seven-digit code. After a short encoding time, participants were given a brief rehearsal period, in which they were required to maintain the information in working memory. Finally, participants were asked to retrieve the code. We chose a task that consumed working memory because many real-world tasks on computers have similarly high working memory demands (e.g., reading a Web page, searching for information, etc.). Research suggests that maintaining information in working memory requires brain structures including the hippocampus and amygdala (Friedman and Goldman-Rakic 1988). Furthermore, recent research suggests that working memory maintenance utilizes several MTL areas (Schon et al. 2016), suggesting that other MTL processes such as memory retrieval may be interrupted during working memory maintenance periods.

The security messages used in this experiment were operationalized as permission warnings similar to those that are displayed as users install a Google Chrome browser extension (see Figure 4 for an example). The warning listed the permissions the application was requesting.

Prior to starting the experiment, participants were required to learn which permission warnings were malicious and which were acceptable. We instructed participants to reject all warnings that contained any malicious permissions and to accept all others.Toensure that participants learned which permissions were malicious, they were required to pass a quiz. The quiz asked participants to correctly identify the malicious and acceptable permissions in an order-randomized list Online Appendix A (available as supplemental material at http://dx.doi.org/10.1287/isre.2016.0644) lists all acceptable and malicious permissions). If participants misclassified any of the permissions, they were notified which ones were misclassified, and the list order was then reset and randomized again. Participants were required to repeat the quiz until they correctly classified all permissions. After successfully finishing the training, participants completed the experiment in three treatments presented in a random order. To relieve participants’ fatigue during the experiment, there was a brief rest period in between each treatment. We describe each treatment below (see Figure 5). In addition, Online Appendix A includes figures of each stage of the experiment depicted in Figure 5 (e.g., encode, rehearsal, etc.).

Treatment A2 High-DTI0 In the high-DTI treatment, participants were presented a seven-digit code. They were asked to encode the code for five seconds. Afterward, the code disappeared and a warning was shown. Participants were then given seven seconds (with a jitter of ±3 seconds to avoid multicollinearity in the fMRI analysis) to click on either reject or accept based on their previous training. At this time, the warning disappeared and a question appeared asking participants to select the code they were most recently asked to memorize among five other codes. Participants were given seven seconds to select the code and then given a break for five seconds to be used as a baseline in the analysis. Participants repeated this 18 times. Since the warning was presented during a working memory maintenance period (i.e., between the encoding and retrieval screens), security message disregard was likely influenced by DTI.

Figure 5 (Color online) Experimental Design  
![](/api/attachments/NVMGEYF8/fulltext/images/48b86923e435d446c0ad9b8b6a7ac7e95f849f391d8f9f78bb32ce769a6911f8.jpg)

Treatment B2 Low-DTI0 Treatment B followed the same procedure as Treatment A, except the ordering of the seven-second warning page and the sevensecond break page was changed. Participants first encoded the code, retained that code in their memory for the rehearsal period, retrieved the code, and then responded to the warning. This was repeated 18 times with a five-second break between each trial to be used as a baseline in the analysis. As the warning did not occur during the rehearsal period, security message disregard was less likely influenced by DTI than in Treatment A.

Treatment C2 Warning-Only0 In this treatment, participants only saw warnings and did not receive the encode/retrieve task. Like the previous treatments, participants were given seven (±3) seconds to respond to the warning. This was repeated 18 times with a break between each trial to be used as a baseline in the analysis. Since there was no memorization task, security message disregard was likely not influenced by DTI.

3.2.1. Behavioral Pilot Test. We followed the guidelines provided by Dimoka (2012) for conducting an fMRI study. This included performing a behavioral pilot test outside of the MRI scanner to ensure that subjects perform the task as expected, are manipulated, and that the protocol is clear. Please see Online Appendix C for details.

3.2.2. MRI Procedure. We ran the experiment in an fMRI laboratory. fMRI has high spatial resolution and can localize neural activation to specific brain regions in a noninvasive manner (see Figure 6).

Participants were verbally informed about experimental procedures. Participants viewed the experimental images on a large MR-compatible monitor at the opening of the MRI scanner by means of a mirror attached to the head coil. Before being placed inside the MRI scanner, participants were given an MR-compatible trackball, which they used to interact with the security warnings and memorization task throughout the experiment. Extensive technical details regarding MRI acquisition parameters and data preprocessing procedures are documented in Online Appendix D.

Single-subject regression (first-level) analyses were carried out by creating regressors for each event type: memory code display, high-DTI warning, low-DTI rehearsal, memory retrieval, low-DTI warning, warning-only warning, and working-memory only rehearsal. Regressors for motion (three translations and three rotations) were included in the model as effects of no interest. Periods without explicit task demands were included in the model as an implicit baseline (i.e., the breaks shown in Figure 5). Stimulus durations were modeled as illustrated in Figure 5 and as described in Section 3.2.

Figure 6  
(Color online) MRI Scanner  
![](/api/attachments/NVMGEYF8/fulltext/images/8ed169008002c622790aac68828ff23d68f64e818a62d1b473a5769fe3d7eff1.jpg)

Beta values for the conditions of interest were then entered into group-level analyses (whole-brain, voxelwise t-tests), which were used to determine significant clusters of activation. Corrections for multiple comparisons were determined through Monte Carlo simulations (Forman et al. 1995). All clusters of activation were thresholded at a voxel-wise p-value < 0002 and a spatial extent (i.e., cluster size) threshold of k > 40 contiguous voxels (1,080 mm<sup>3</sup>), controlling family-wise error rate to p < 0005. Significant activation clusters (functionally defined regions of interest) as defined in the group-level analysis were further interrogated by extracting mean beta values within the clusters for each participant.

3.2.3. Participants. We recruited 24 participants from the university community. Each participant was screened for MRI compatibility, native-English speaking, corrected-normal visual acuity, and right handedness. We excluded those with color blindness or who were taking psychotropic medications. In accordance with the university’s institutional review board protocol, all participants were given an informed consent form to sign. Of the 24 participants, 11 were female and 13 were male. Participant age ranged from 18 to 40 years of age with a mean age of 23.7 years. Participants were paid \$25 for approximately one hour in the scanner.

## 3.3. Results

3.3.1. High-DTI vs. Warning-Only Treatment fMRI Analysis. We first analyze Hypotheses 1–3 that explore the relationship between brain activation and security message disregard in the high-DTI and warning-only treatments. In this analysis, we examined the neural correlates of responding to security warnings under dual-task conditions by comparing activation for the high-DTI warning/rehearsal period (in which participants were required to maintain a seven-digit code in their working memory and respond to the warning stimulus) with activation for the warning in the warning-only condition using paired t-tests. We exclusively masked the results of this comparison with the warning versus baseline comparison to eliminate spurious activations (such as visual responses to the stimulus and motor responses from manipulating the trackball). We found several significant clusters (regions of interest, or ROIs) of activation (see Table B1 in Online Appendix B). In particular, activation was greater in the MTL for the warning-only condition than for the high-DTI condition $( t ( \bar { 2 } 3 ) = 3 . 5 3 4 , p < 0 . 0 0 5 )$ , suggesting that participants were utilizing the MTL more for processing the security warning in the warning-only condition, supporting H1 (see Figure 7).

In addition to the fMRI analysis,weexplored howDTI influenced participants’ actual security message disregard. As shown in Table 1, security message disregard was significantly higher in the high-DTI treatment than in the warning-only treatment $( \chi 2 ( 1 ) = 4 0 . 3 9 1$ $p < 0 . 0 1 )$ , supporting H2.

We next explored whether the change in MTL activation between the high-DTI and warning-only treatments predicts participants’ change regarding security message disregard. We specified a regression model with participants’ change in terms of security message disregard as the dependent variable and participants’ change in MTL activation between the two treatments as the independent variable. The results support the notion that the change in MTL activation significantly influences security message disregard:

Figure 7 (Color online) Increased Activity in Response to the Warning-Only Condition Compared with the High-DTI Condition—Warm Colors Indicate Increased Blood Flow  
![](/api/attachments/NVMGEYF8/fulltext/images/9362680fb5c1c4e1cfad4177eba93ebaca515649c422e032776735a9fd0d68ee.jpg)

Table 1 fMRI Warning Performance

<table><tr><td rowspan="2">Treatment</td><td colspan="2">Security warning (%)</td></tr><tr><td>Disregard</td><td>Regard</td></tr><tr><td>High-DTI</td><td>22.92</td><td>77.08</td></tr><tr><td>Low-DTI</td><td>8.80</td><td>91.20</td></tr><tr><td>Warning Only</td><td>7.41</td><td>92.59</td></tr></table>

$\beta = - 0 . 5 1 9 , ~ t ( 2 3 ) = 2 . 8 4 4 , ~ p < 0 . 0 1 , ~ R ^ { 2 } = 0 . 2 6 9 ,$ , supporting H3.

3.3.2. High-DTI vs. Low-DTI Treatment fMRI Analysis. We perform similar analyses to test Hypotheses 4–6 exploring the relationship between brain activation and security message disregard in the high-DTI and low-DTI treatments. We compared activation during the warning/rehearsal period for the high-DTI condition with activation during the rehearsal period for the low-DTI condition. In both conditions, participants were required to maintain a sevendigit code in their working memory. However, in the high-DTI condition, participants also responded to the warning stimuli. Therefore, in addition to the working-memory-related activity, we also anticipated activation related to viewing and responding to the warning stimuli in the high-DTI condition. To control for this, we exclusively masked the high-DTI versus low-DTI comparison with a comparison of the activation for the warning task in the warning-only treatment versus the baseline. The resulting activation was therefore free of spurious visual system activation related to viewing the stimulus and the motor activation related to responding with the trackball. We identified four significant clusters of activation, including regions in the bilateral MTL that overlapped with the regions observed in the previous analysis. The significant clusters of activation included two in the MTL, comprising parts of the anterior hippocampus, entorhinal, and perirhinal cortices (see Table B2 in Online Appendix B). In each of these regions, activation was significantly greater for the low-DTI rehearsal period than for the high-DTI delay period $( t ( 2 3 ) = 4 . 3 0 8 , p < 0 . 0 0 1 )$ , suggesting participants utilized the MTL more for working memory maintenance in the low-DTI treatment, thus supporting H4 (see Figure 8).

We examined how the differences between the high-DTI and low-DTI conditions influenced participants’ actual security message disregard. As shown in Table 1, security message disregard was significantly higher in the high-DTI treatment than in the low-DTI treatment $( \chi 2 ( 1 ) = 3 2 . 2 7 9 , ~ p < 0 . 0 1 )$ . A further chisquared test indicated that there was no difference in security message disregard in the low-DTI treatment and the warning-only treatment $( \chi 2 ( 1 ) = 0 . 5 6 0$ $p > 0 . 0 5 )$ , supporting H5.

Figure 8 (Color online) Increased Activity in Response to the Low-DTI Condition Compared with the High-DTI Condition—Warm Colors Indicate Increased Blood Flow  
![](/api/attachments/NVMGEYF8/fulltext/images/cfba5bc41fa5347f4cc03cba377ffd6eefca6ff24ebda0fd6a9a0f1a6962d90b.jpg)  
In addition, we explored whether the change in MTL activation between the high-DTI and low-DTI treatments predicted participants’ change in security message disregard. We specified a regression model with the change in security message disregard as the dependent variable and the change in MTL between the two treatments as the independent variable. The results suggest that the change in MTL significantly influences security message disregard: $\beta = - 0 . 4 7 0$ t4235 = 20495, p < 0001, $R ^ { 2 } = 0 . 2 1 2 ,$ , supporting H6.

Finally, we tested supplementary hypotheses comparing MTL activation and security message disregard between low-DTI and warning-only scenarios, which are presented in Online Appendix E. Interestingly, the analyses show that when a message immediately follows a primary task, neural activity in the MTL is comparable to when attending to the message is the only task.

## 3.4. Experiment 1—Discussion

Both the fMRI and behavioral analysis supported our hypotheses. First, we found that participants in the high-DTI treatment exhibited less activation in the bilateral MTL than participants in the warning-only treatment. This suggests that DTI inhibits one’s ability to utilize the MTL to retrieve information from the long-term memory necessary to respond to permission warnings. People had more than 15% higher security message disregard in the high-DTI treatment than in the warning-only treatment. We found that the change in MTL predicted participants’ change in terms of warning response accuracy.

Second, we found that displaying the warning between the working memory tasks (i.e., not during the rehearsal period) improved performance. In the low-DTI treatment, participants had more activation in the MTL than in the high-DTI treatment. Likewise, in the high-DTI treatment, participants had an approximately 14% higher security message disregard than those in the low-DTI treatment. The change in MTL in this comparison also predicted participants’ change in warning response accuracy.

## 4. Experiment 2—Google Chrome Cleanup Tool

Experiment 2 applies the fMRI insights gained in Experiment 1 to evaluate interventions for mitigating DTI in a realistic scenario. We create hypotheses that identify various low-DTI timings during which to display system-generated alerts. We then empirically test these hypotheses in an ecologically valid scenario. As a result, this study provides an artifact (i.e., security messages that appear during low-DTI timings) for practitioners to reduce security message disregard. Furthermore, it demonstrates how one can apply the findings of Experiment 1 to determine appropriate low-DTI timings.

## 4.1. Experimental Context

As a context to test our hypotheses, we implemented Google Chrome Cleanup Tool (CCT) messages used in Chrome for Windows (see Figure 9). Google Chrome accounts for more than 56% of the global desktop browser market share (StatCounter 2015), and so the CCT potentially impacts millions of users. The CCT detects if malware has tampered with the host computer and manipulated the browser or other Internet settings (Google 2015). When a problem is detected, the CCT displays a message to the user asking for permission to remove the unwanted software and restore Chrome’s original settings. Although the CCT message is important, it does not require immediate attention and, therefore, can be delayed.

For this study, we collaborated with a team of Google Chrome security engineers who develop the CCT—a security message that can be delayed—to identify five low-DTI times to display security messages during the browsing experience. These times were selected according to (1) DTI theory and the results of fMRI results of Experiment 1, (2) input from Google engineers on moments that were frequent in occurrence and generalizable across a wide variety of web-based activities and users, and (3) a feasibility assessment for implementing in a Web browser.

For comparison, we also chose four high-DTI times. These times were selected to be in the middle of other tasks, which, based on DTI theory and Experiment 1, should exhibit higher DTI. This resulted in a betweensubject design with nine conditions (five low- and four high-DTI times). Examples of each of the conditions are presented in Online Appendix F. Table 2 summarizes the selected low- and high-DTI times.

Figure 9 (Color online) Google Chrome Cleanup Tool Message  
![](/api/attachments/NVMGEYF8/fulltext/images/dcd17bc0773c4bbf9ad0f50acd7513099cb1436ec0c566dc9378373ad3e84d80.jpg)

Table 2 Summary of Conditions

<table><tr><td>Code</td><td>Condition</td><td>Description</td><td>n</td></tr><tr><td colspan="4">Low-DTI conditions</td></tr><tr><td>LowDTI-1</td><td>Low-DTI: On first page load</td><td>At the beginning of starting the first task</td><td>96</td></tr><tr><td>LowDTI-2</td><td>Low-DTI: After video</td><td>After the video</td><td>96</td></tr><tr><td>LowDTI-3</td><td>Low-DTI: Switching Web domains</td><td>After interacting with a website</td><td>95</td></tr><tr><td>LowDTI-4</td><td>Low-DTI: Waiting for web-based task to complete</td><td>Waiting for a file to process</td><td>94</td></tr><tr><td>LowDTI-5</td><td>Low-DTI: Waiting for page load</td><td>Waiting for a page to load</td><td>95</td></tr><tr><td colspan="4">High-DTI conditions</td></tr><tr><td>HighDTI-1</td><td>High-DTI: During video</td><td>In the middle of watching a video</td><td>97</td></tr><tr><td>HighDTI-2</td><td>High-DTI: While typing</td><td>In the middle of typing</td><td>95</td></tr><tr><td>HighDTI-3</td><td>High-DTI: While transferring information</td><td>In the middle of transferring a confirmation code</td><td>94</td></tr><tr><td>HighDTI-4</td><td>High-DTI: On the way to close window</td><td>In the middle of the movement to close the Web page</td><td>94</td></tr><tr><td></td><td></td><td>Total number of participants</td><td>856</td></tr></table>

## 5. Hypotheses

We hypothesize how the five different low-DTI times influence security message disregard compared to the high-DTI times. Experiment 1 demonstrated that a low-DTI time for security messages is between tasks (i.e., after completing one task and before completing another task). Consistent with DTI theory, when processing a security message before or after another task, people experienced significantly more activation in the MTL region of the brain, suggesting that they processed the message more completely (see H4 results). Processing messages between tasks decreased security message disregard compared to processing a security message in the middle of another task (see H5 results).

We propose that displaying a security message when a Web page first loads in the browser is one such between-task time and will therefore exhibit low DTI and less security message disregard. This is because when a Web page first loads, users are not yet fully engaged in their new task. Rather, they are about to begin a new task or are between tasks. As such, consistent with DTI theory and our fMRI findings in Experiment 1, people should engage in greater cognitive processing of the security messages at this time, and security message disregard will decrease. In summary, we hypothesize the following:

<sup>Hypothesis</sup> <sup>7</sup> <sup>(H7).</sup> Displaying a security message when a browser page first loads will result in lower security message disregard than displaying the message during high-DTI times.

Likewise, we posit that another between-task, low-DTI time is when a user finishes viewing a webbased video. Videos are an extremely popular type of media on the Web (YouTube 2015). Often, people will experience a state of cognitive absorption while watching videos—a state of deep involvement with and focused attention on the media (Agarwal and Karahanna 2000). During such times, people have limited cognitive resources to perform other tasks. However, on completion, these resources are temporarily released before the next task. Displaying a security message immediately after a web-based video is therefore an appropriate between-task time. During this time, DTI will be low, and the user has a higher likelihood of having cognitive resources available to process security messages. Consistent with Experiment 1, security message disregard will decrease. In summary, we hypothesize the following:

<sup>Hypothesis</sup> <sup>8</sup> <sup>(H8).</sup> Displaying a security message when a web-based video ends will result in lower security message disregard than displaying a message during high-DTI times.

Third, we posit that when people switch Web domains, they experience a between-task time that will exhibit low DTI and thereby low security message disregard. When a person switches domains, it is an indicator that the person is between tasks. Although perhaps not always the case, the probability of having just ended a task and starting a new task is higher than if someone is still browsing a Web page on the same domain. In this case, consistent with Experiment 1, one’s likelihood of processing the security message will be greater, and security message disregard will be lower. In summary, we hypothesize the following:

<sup>Hypothesis</sup> <sup>9</sup> <sup>(H9).</sup> Displaying a security message when switching domains will result in lower security message disregard than displaying a message during high-DTI times.

In Experiment 1, we also found that responding to security messages in isolation results in lower DTI than when responding to messages in the middle of a task. When users’ only task is responding to security messages, they have higher activation in the MTL region of the brain (see the results to H1). This suggests that participants devote more cognitive resources to the processing of security messages at this time. As a result, people have lower disregard when responding to security messages in isolation compared to responding to security messages in the middle of another task (see the results to H2).

Waiting for a web-based task to complete is an isolated time to respond to security messages that will result in low DTI and have lower security message disregard. Users frequently must wait for web-based tasks to complete. Examples include waiting for a picture to upload, a report to be generated, or a credit card transaction to be processed. During these times, a security message can be presented in isolation without competing with other tasks. Users can therefore devote more cognitive resources to the processing of the security message, which, consistent with Experiment 1, will result in lower security message disregard. In summary, we hypothesize the following:

<sup>Hypothesis</sup> <sup>10</sup> <sup>(H10).</sup> Displaying a security message while waiting for “processing” to finish will result in lower security message disregard than displaying a message during high-DTI times.

Finally, similar to waiting for a web-based task to complete, we propose that waiting for a page to load is also an isolated time to respond to security messages that will have low DTI and lower security message disregard. While the user waits for a page to load, the user’s task is temporarily suspended, and the screen is often blank. Thus, there are minimal task demands and stimuli to consume cognitive resources, and the user can respond to the security message in isolation. Again, Experiment 1 shows that when responding to security messages in isolation, users will experience greater activation in the MTL, leading to less security message disregard (H1, H2). Building on these findings, we hypothesize the following:

<sup>Hypothesis</sup> <sup>11</sup> <sup>(H11).</sup> Displaying a security message while waiting for a page to load will result in lower security message disregard than displaying a message during high-DTI times.

## 5.1. Procedure

Participants were instructed that their task was to help create an archive of online videos. To increase realism, we did not tell participants upfront that a purpose of the task was also to explore how they respond to security messages. Participants were given a Web page URL to watch a 30-second commercial video. After watching the video, participants were given another URL that led them to a video archive website. On this website, they were asked to enter the URL for the video they had watched and to summarize the video in at least 25 words (the system enforced the word count). After submitting their summary, the Web page displayed the following message for 10 seconds: “Please wait while we fetch and process the video.” After processing completed, participants were given a confirmation code that they were required to enter on another Web page to receive payment.

The two websites were designed by the research team specifically for this study and included Java-Script that could trigger the CCT message. With permission from Google, the CCT message displayed was identical in appearance to the actual one displayed in Chrome for Windows. Consistent with the way CCT is displayed in Chrome, the CCT message remained visible over the content of the Web page until the user either accepted or dismissed it, or until the Web page was closed.

The experimental system randomly assigned each participant to one condition. The five low-DTI conditions were displayed as follows. First, in the LowDTI-1 (“On first page load”) condition, participants saw the Google CCT prompt when they navigated to the first Web page. In the LowDTI-2 (“After video”) condition, participants saw the prompt after finishing the video. In the LowDTI-3 (“Switching Web domains”) condition, participants saw the prompt when switching domains to the second website. In the LowDTI-4 (“Waiting for web-based task to complete”) condition, participants saw the prompt while waiting for the system to upload the video on the second Web page. For the LowDTI-5 (“Waiting for page load”) condition, we implemented an artificial loading delay of six seconds as the second page loaded. A few seconds into the loading delay, the CCT message was shown.

The remaining four high-DTI conditions were similar to the low-DTI conditions except that the CCT message was displayed in the middle of a task. For the HighDTI-1 (“During video”) condition, participants saw the CCT message 10 seconds into the 30-second video. In the HighDTI-2 (“While typing”) condition, participants saw the prompt while typing the description of the video (when they typed word 10 out of 25). In the HighDTI-3 (“While transferring information”) condition, participants saw the CCT message as they were given the confirmation code that they needed to enter in the payment website. Finally, in the HighDTI-4 (“On the way to close window”) condition, participants were shown the prompt as they were in the middle of moving the mouse cursor to close the window. The system recorded whether participants clicked on the “Run Chrome Cleanup

Tool” button, the “Dismiss” button, or ignored the message.

Participants completed a post-task survey to gather demographic and manipulation check information. Furthermore, the post-task survey disclosed the real purpose of the experiment—to explore how people respond to Google CCT. We then provided a link that educated participants on the real prompt and what they should do if they see it.

## 5.2. Dependent and Independent Variable

We conceptualized our dependent variable—security message disregard—as whether participants ignored the message or responded to it (a binary variable). We chose this instead of whether participants clicked on the “Run Chrome Cleanup Tool” or “Dismiss” buttons because feedback from the pilot test indicated that some people clicked “Dismiss” if they thought the prompt itself was malware (which is not an example of disregarding the message, but rather a thoughtful response). However, as the CCT prompt does not automatically disappear when ignored, responses from the pilot test suggest that not responding to the warning was a result of not noticing or giving attention to the warning. Thus, we deem an appropriate conceptualization of security message disregard as whether participants ignored the message.

As some messages were displayed earlier in the task than others, we also recorded how long the message was displayed as a control variable in the analysis. While people were responding, we captured their mouse cursor movements to explore whether they were quickly “clicking the message away” or actually paying attention to and processing the message (Anderson et al. 2015, 2016b). Finally, we recorded the condition to use it as an independent variable in the analysis.

## 5.3. Participants

We recruited participants from Amazon’s Mechanical Turk (MTurk). Social scientists are increasingly using MTurk, as the diversity of the participant pool is larger than that of typical undergraduate college samples, and the data are as reliable as those collected using other methods (Buhrmester et al. 2011). We had 856 participants, with 94–97 participants per condition. Following the suggestion of Steelman et al. (2014), all participants were required to be from the United States. The average age of participants was 34.68 years old; 56% were male. All participants were required to take the experiment using Google Chrome on Windows, the only version of Chrome that includes the CCT. Participants were paid \$1 USD for approximately a six-minute task. Table 2 shows the participant breakdown per condition.

## 6. Results

## 6.1. Manipulation Check

Prior to analyzing the security message disregard for the different conditions, we conducted a manipulation check to verify that our hypothesized times had lower DTI than the high-DTI times. In a post-task survey, we asked all participants the following question on a seven-point Likert agreement scale as a manipulation check for DTI: “When the above message appeared, I was busy doing other things” (with the CCT message shown above the question). An analysis of variance (ANOVA) indicated that a difference existed among the different conditions, $F ( 8 , 8 0 0 ) =$ $1 0 . 9 7 9 , p < 0 . 0 0 1$ . Using a Tukey post-hoc comparison analysis, we found that people reported significantly less DTI for each of the low-DTI conditions than for the high-DTI conditions.

## 6.2. Mouse Movement Analysis

As another method for evaluating the effectiveness of our low-DTI conditions, we performed an analysis of users’ mouse cursor movements to see if users responded more thoughtfully to the CCT prompt in the low-DTI times compared to the high-DTI times. The analysis of mouse cursor movements allows for finegrained temporal precision in capturing users’ emotional and cognitive states within a natural environment (Hibbeln et al. 2016). See Online Appendix G for a summary of mouse cursor-tracking literature. If a user dismisses a message without reading or cognitively processing the message, the user’s mouse cursor movements are more direct and move more quickly to the dismiss button. However, if a user takes time to read and cognitively process the message, the mouse cursor often deviates away from the most direct path to dismiss the message as movements indicating an unconscious movement in addition to the conscious one (Hibbeln et al. 2016). In addition, users often move more slowly as they are cognitively processing the message (Anderson et al. 2015, 2016b; Hibbeln et al. 2016).

We test whether users in the low-DTI conditions had slower speed and greater deviation—the indicators of cognitive processing—while responding to messages in the low-DTI conditions versus the high-DTI conditions. An ANOVA suggested that differences in deviation $( F ( 8 , 3 7 1 ) = 7 . 6 7 5 , ~ p < 0 . 0 0 1 )$ and speed $( F ( 8 , 3 7 1 ) = 1 5 . 7 8 3 , p < 0 . 0 0 1 )$ exist among the low- and high-DTI conditions. In the post-hoc comparison, we found that people who responded to the security message in the low-DTI conditions had more deviation and slower movement speeds than those people who responded to messages in the high-DTI conditions. This suggests that users in the low-DTI condition had indicators of greater cognitive processing of the security message.

Table 3 Percentage of Disregard for Each Condition (Ranked from Lowest to Highest)

<table><tr><td>Code</td><td>Condition</td><td>Disregarded (%)</td></tr><tr><td>LowDTI-5</td><td>Low-DTI: Waiting for page load</td><td>22.11</td></tr><tr><td>LowDTI-4</td><td>Low-DTI: While processing</td><td>24.47</td></tr><tr><td>LowDTI-2</td><td>Low-DTI: After video</td><td>43.75</td></tr><tr><td>LowDTI-1</td><td>Low-DTI: On first page load</td><td>44.79</td></tr><tr><td>LowDTI-3</td><td>Low-DTI: Switching domains</td><td>46.32</td></tr><tr><td>HighDTI-4</td><td>High-DTI: On the way to close window</td><td>74.47</td></tr><tr><td>HighDTI-2</td><td>High-DTI: While typing</td><td>77.89</td></tr><tr><td>HighDTI-1</td><td>High-DTI: During video</td><td>79.38</td></tr><tr><td>HighDTI-3</td><td>High-DTI: While transferring information</td><td>87.23</td></tr></table>

## 6.3. Main Analysis

We then tested our hypotheses using logistic regression contrasts. We included security message disregard as the dependent variable (coded as 1 for disregard and 0 if the participant responded). As independent variables, we included a control variable for how long the message was shown, accounting for variance due to some messages being displayed longer than others in different conditions. We then modeled each condition as a dummy variable. To compare conditions to each other, we treated each condition as the reference class (the condition to which every other condition is compared) in separate analyses. We applied a Bonferroni correction to account for alpha slippage.

Table 3 summarizes the security message disregard for each condition. Table 4 summarizes the results. The Nagelkerke $R ^ { 2 }$ for the model was 0.290. Displaying the message during each of the low-DTI conditions resulted in significantly lower disregard than all of the high-DTI conditions, supporting H7–H11.

## 7. Experiment 2—Discussion

In this experiment, we chose five low-DTI times to display the CCT prompt. These times were chosen based on (1) DTI theory and Experiment 1 results, (2) input from Google engineers on moments that were frequent in occurrence and generalizable, and (3) a feasibility assessment for implementing in a Web browser.

The analysis of disregard supported our hypotheses. Namely, people had significantly and substantially less disregard in every low-DTI time compared to every high-DTI time. In addition, we confirmed that DTI influenced user’s mouse cursor movement; users in the low-DTI conditions demonstrated mousing indicators of more thoughtful processing than users in the high-DTI conditions.

## 8. General Discussion

System-generated alerts are ubiquitous in HCIs. While providing timely information, alerts also result in decreased performance (Mark et al. 2008). The experiments of this study explored how a subset of these alerts—security messages—increase security message disregard when they interrupt a users’ primary task because of the neural phenomenon of DTI.

This study had three objectives. First, we explored how DTI occurs in the brain in response to interruptive messages. We designed an fMRI experiment that examined how activation in the MTL changes when security messages induce DTI by interrupting a primary task. The MTL is the brain region responsible for retrieving information from declarative memory to properly respond to security messages. We found that activation in the MTL decreased when security messages interrupted a primary task, indicating that longterm memory is inhibited under conditions of high DTI.

Second, we explained how DTI affects users’ responses to interruptive messages. We tied the fMRI and behavioral performance data by showing that decreases in MTL activation under a condition of high DTI directly predict participants’ increased security message disregard. We followed the approach enjoined by Dimoka: “By acquiring behavioral data together with fMRI data, virtually in real-time, it may be possible to link brain activity with behavioral responses and thereby to predict behavior in situations where alternative means have failed” (Dimoka 2012, pp. 814–815). Thus, our linkage of fMRI and behavioral data provides strong evidence of the influence of DTI on security message disregard.

Table 4 Condition Comparisons with Bonferroni Adjustments

<table><tr><td>Treatment</td><td>LowDTI-1</td><td>LowDTI-2</td><td>LowDTI-3</td><td>LowDTI-4</td><td>LowDTI-5</td><td>HighDTI-1</td><td>HighDTI-2</td><td>HighDTI-3</td></tr><tr><td>LowDTI-2</td><td>0.01 ns</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LowDTI-3</td><td>-0.02 ns</td><td>-0.03 ns</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LowDTI-4</td><td>0.20**</td><td>0.19**</td><td>0.22**</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LowDTI-5</td><td>0.23**</td><td>0.22**</td><td>0.24**</td><td>0.02 ns</td><td></td><td></td><td></td><td></td></tr><tr><td>HighDTI-1</td><td>-0.35***</td><td>-0.36***</td><td>-0.33***</td><td>-0.55***</td><td>-0.57***</td><td></td><td></td><td></td></tr><tr><td>HighDTI-2</td><td>-0.33***</td><td>-0.34***</td><td>-0.32***</td><td>-0.53***</td><td>-0.56***</td><td>0.01 ns</td><td></td><td></td></tr><tr><td>HighDTI-3</td><td>-0.42***</td><td>-0.43***</td><td>-0.41***</td><td>-0.63***</td><td>-0.65***</td><td>-0.08 ns</td><td>-0.09 ns</td><td></td></tr><tr><td>HighDTI-4</td><td>-0.30***</td><td>-0.31***</td><td>-0.28***</td><td>-0.50***</td><td>-0.52***</td><td>0.05 ns</td><td>0.03 ns</td><td>0.13 ns</td></tr></table>

Notes. Shaded areas indicate analyses to test hypotheses; ns, nonsignificant.  
<sup>∗∗</sup>p < 0001; <sup>∗∗∗</sup>p < 00001.

Third, we investigated how to mitigate the effects of DTI by adjusting the timing of messages. In both the fMRI and the behavioral experiment, we found that presenting security messages after or between primary tasks lowers security message disregard. In the fMRI experiment, we found that presenting the security message after the primary task resulted in greater activation of the MTL, similar to when people were solely focused on responding to the security message. Furthermore, we showed that the decrease in MTL activation between the high-DTI and low-DTI treatments directly predicted participants’ increased security message disregard. Security message disregard was not significantly different between the low-DTI and warning-only treatment, suggesting that through effective timing, a low-DTI condition can have similar results as if the security message were the primary task.

Similarly, in the behavioral experiment using the realistic context of the CCT, people disregarded the CCT prompt less during every low-DTI time compared to every high-DTI time. This was consistent both with DTI theory and the main finding from Experiment 1 that the timing of the interruption mattered. Table 5 summarizes the contributions of both studies.

## 8.1. Contributions to Research

This paper makes several contributions to research. First, DTI scholars have largely focused on how interruptions decrease performance of primary tasks (e.g., work productivity). However, in many contexts it is vital to understand how performance with a systemgenerated alert (the interruption itself) is influenced by DTI. This paper contributes by demonstrating that DTI suppresses activity in the MTL region of the brain, which decreases one’s ability to retrieve the necessary information from declarative memory to properly respond to the security message. Although the exact neural systems involved likely vary depending on the nature of the primary task and system-generated alert, we would expect the overall timing-dependent pattern of activation to remain the same. This provides a sound theoretical foundation for objectively measuring the influence of DTI in the brain for other systemgenerated alerts.

Second, our research shows that the change in activation in the MTL regions of the brain between higherand lower-DTI conditions predicts security message disregard. A regression analysis indicated that the change in MTL activation between treatments alone accounted for 26.9% of the variance in security message disregard behavior in one analysis and 22.1% in the other. Thus, we contribute by directly tying fMRI data and behavioral performance data, providing a powerful objective predictor of security message disregard.

Third, although system-generated alerts are ubiquitous in personal computing, our results show why they should be bounded in their presentation. In the fMRI experiment, timing the security message to display between primary tasks resulted in significantly higher neural activation of the MTL and substantially decreased security message disregard close to the level for when responding to the security message is the exclusive task. That is, there was no statistical difference in security message disregard between the low-DTI group and the warning-only group as shown in Online Appendix E. Similarly, in the more realistic context of Experiment 2, participants disregarded the Google CCT prompt significantly less when the prompt was shown during low-DTI times.

Table 5 Contributions

<table><tr><td>Element of research</td><td>Type</td><td>Contributions</td></tr><tr><td colspan="3">Experiment 1. fMRI experiment</td></tr><tr><td>Interruptive messages induce DTI</td><td>Theoretical, empirical</td><td>Found that activation in the MTL decreased when messages interrupted a primary task, indicating that long-term memory is inhibited under conditions of high DTI.</td></tr><tr><td>DTI decreases the effectiveness of messages</td><td>Theoretical, empirical</td><td>Showed MTL activation under a condition of high DTI directly predicted increases in security message disregard behavior.</td></tr><tr><td>Good timing mitigates the effect of DTI</td><td>Theoretical, empirical</td><td>Demonstrated that displaying the message at low-DTI times results in significantly higher MTL activation and lower security message disregard, indicating that the effects of DTI can be mitigated by finessing the timing of when a security message is displayed.</td></tr><tr><td colspan="3">Experiment 2. Online chrome cleanup tool experiment</td></tr><tr><td>Low-DTI timings during Web browsing</td><td>Artifactual</td><td>Identified and validated five low-DTI timings during common Web browsing experiences, offering practical means of mitigating the effect of DTI.</td></tr><tr><td>Mouse cursor-tracking measures</td><td>Methodological</td><td>Showed that two mouse cursor-tracking measures of cognitive processing—movement deviation and speed—can be used to validate low- vs. high-DTI times.</td></tr><tr><td>Triangulation and real-world testing of fMRI findings</td><td>Empirical</td><td>In a realistic task, established that presenting security messages during low-DTI times results in significantly lower security message disregard relative to high-DTI times, corroborating the fMRI results of Experiment 1.</td></tr></table>

Finally, Experiment 2 introduces a novel method for measuring DTI and whether people are thoughtfully responding to system-generated alerts. Namely, we found that DTI influences how people move the computer mouse in response to alerts. When DTI was high, the users’ mouse cursor movements were significantly more direct and moved more quickly to dismiss the CCT prompt. By contrast, when DTI was low, users’ mouse cursor movements deviated more away from the most direct path to dismiss the message, and moved more slowly toward other information on the message, an indication that people were reading and cognitively processing the message. This finding builds on prior mouse-tracking work (Hibbeln et al. 2016), suggesting that mouse cursor movement is an effective means of assessing DTI.

## 8.2. Contributions to Practice

Understanding how people respond to system-generated alerts is important to promote a secure computing environment. Our results suggest that for those messages that can be safely preempted or delayed, waiting until between primary tasks to display a message will result in substantially higher performance on the security task. Again, in our experiments using security messages, users’ security message disregard was decreased 15% by displaying the security warning between primary tasks in Experiment 1. In Experiment 2, security message disregard decreased from 87.23% (worst-case high-DTI scenario) to 22.11% (bestcase low-DTI scenario) by finessing the timing of the Google CCT prompt. These results suggest that there is a considerable benefit to be realized in practice by either preempting or postponing an alert to a low-DTI time.

As an immediate benefit of our research, we identified and validated five low-DTI timings during common Web browsing experiences that effectively mitigated the effects of DTI in Experiment 2. In selecting these times, we collaborated with a team of Google Chrome security engineers who develop the CCT— a security message that can be delayed. These times were selected according to (1) DTI theory and the results of fMRI results of Experiment 1, (2) input from Google engineers on moments that were frequent in occurrence and generalizable across a wide variety of web-based activities and users, and (3) a feasibility assessment for implementing in a Web browser. In every case, security message disregard was lower in these low-DTI times than for all of the high-DTI times.

Researchers and practitioners should use these findings to identify ways to finesse the timing of systemgenerated alerts in other contexts so that they are resistant to the effects of DTI.

## 8.3. Limitations

This research is subject to certain limitations. First, the fMRI method imposes constraints that may hinder the realism of the task. Subjects must lie supine and still in a narrow tube for the duration of the experiment. We reduced some of this artificiality because of the interactive nature of our web-based experimental design. Moreover, this limitation was at least partially compensated for by performing Experiment 2 in a realistic and very common setting (56% of all Internet users use Google Chrome) to provide greater ecological validity. We leave to future research the application of field methodologies that can achieve greater levels of external validity.

Second, our design for Experiment 1 required participants to become very familiar with the list of risky permission warnings. We believe that we may have trained them more thoroughly than is typical of corporate security training. We intentionally did not want the subjects to use their own security judgment because doing so might introduce variance that may cloud our view of the effects of DTI. Similarly, subjects were exposed to 54 security warnings over the course of Experiment 1. This number was necessary to ensure a sufficient signal-to-noise ratio for the fMRI analysis. Most users will not encounter anything close to that many security messages of the same type within an hour. However, we compensated for this lack of realism in Experiment 2, in which each participant responded to only one security message. In this way, Experiment 2 enhanced the overall ecological validity of the study.

Finally, both experiments utilized a security message context. Security messages represent an important and prominent subset of system-generated alerts. Furthermore, security message disregard has high practical implications—ignoring security messages often has more severe consequences than completing the primary task. Because our hypotheses are based on robust theory that is not specifically about security messages, we expect they will hold in other contexts involving security-generated alerts. However, future research should examine how DTI influences other types of system-generated alerts.

## 9. Conclusion

Users frequently disregard system-generated alerts. In this paper, we identify DTI as a major contributor of this disregard. Previous studies on DTI primarily explained how it decreased performance on a primary task when a secondary task interrupts or is performed concurrently. In this study, we show that performance on the interruptive message itself also decreases when it interrupts a primary task. We show in an fMRI and behavioral online experiment that the effects of DTI can be alleviated by timing alerts to display between primary tasks, rather than interrupting a primary task. Furthermore, our results warn of the substantial negative impact that DTI may have for system-generated alerts that cannot be delayed.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0644.

## Acknowledgments

The authors thank the senior editors, reviewers, and special issue workshop participants for their helpful feedback. The authors also wish to thank Elisabeth Morant, Adrienne Porter Felt, and Robert Shield of Google, Inc., for their collaboration on the Google Chrome Cleanup Tool experiment. Finally, the authors thank the 2015 participants of the Gmunden Retreat on NeuroIS, IFIP Working Group 8.11/11.13 Dewald Roode Information Security Workshop, and Workshop on Security and Human Behavior for their input on this work. This research was funded by the National Science Foundation [Grants CNS-1422831 and DGE-1247842] and a Google Faculty Research Award.

## References

Adamczyk PD, Bailey BP (2004) If not now, when? The effects of interruption at different moments within task execution. Dykstra-Erickson E, Tscheligi M, eds. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 271–278.

Agarwal R, Karahanna E (2000) Time flies when you’re having fun: Cognitive absorption and beliefs about information technology usage. MIS Quart. 24(4):665–694.

Anderson BB, Vance A, Kirwan CB, Eargle D, Jenkins JL (2016a) How users perceive and respond to security messages: A NeuroIS research agenda and empirical study. Eur. J. Inform. Systems 25(4):364–390.

Anderson B, Vance A, Kirwan B, Jenkins J, Eargle D (2016b) From warning to wallpaper: Why the brain habituates to security warnings and what can be done about it. J. Management Inform. Systems. Forthcoming.

Anderson BB, Kirwan CB, Jenkins JL, Eargle D, Howard S, Vance A (2015) How polymorphic warnings reduce habituation in the brain: Insights from an fMRI study. Kim J, Begole B, eds. Proc. 33rd ACM Conf. Human Factors Comput. Systems (ACM, New York), 2883–2892.

Atkinson RC, Shiffrin RM (1971) The control processes of shortterm memory. Institute for Mathematical Studies in the Social Sciences, Stanford University, Stanford, CA.

Baddeley AD (2012) Working memory: Theories, models, and controversies. Annual Rev. Psych. 63:1–29.

Borst JP, Taatgen NA, van Rijn H (2015) What makes interruptions disruptive? A process-model account of the effects of the problem state bottleneck on task interruption and resumption. Kim J, Begole B, eds. Proc. 33rd ACM Conf. Human Factors Comput. Systems (ACM, New York), 2971–2980.

Bravo-Lillo C, Cranor LF, Downs J, Komanduri S, Sleeper M (2011) Improving computer security dialogs. Campos P, Graham N, Jorge J, Nunes N, Palanque P, Winckler M, eds. Human-Comput. Interaction–INTERACT 2011, Lecture Notes Comput. Sci., Vol. 6949 (Springer-Verlag, Berlin Heidelberg), 18–35.

Buhrmester M, Kwang T, Gosling SD (2011) Amazon’s Mechanical Turk: A new source of inexpensive, yet high-quality, data? Perspect. Psych. Sci. 6(1):3–5.

Cameron A-F, Webster J (2013) Multicommunicating: Juggling multiple conversations in the workplace. Inform. Systems Res. 24(2): 352–371.

Dimoka A (2012) How to conduct a functional magnetic resonance (fMRI) study in social science research. MIS Quart. 36(3): 811–840.

Dimoka A, Pavlou PA, Davis FD (2011) Research commentary– neuroIS: The potential of cognitive neuroscience for information systems research. Inform Systems Res. 22(4):687–702.

Dimoka A, Banker RD, Benbasat I, Davis FD, Dennis AR, Gefen D, Gupta A et al. (2012) On the use of neurophysiological tools in IS research: Developing a research agenda for neuroIS. MIS Quart. 36(3):679–702.

Dux PE, Ivanoff J, Asplund CL, Marois R (2006) Isolation of a central bottleneck of information processing with time-resolved fMRI. Neuron 52(6):1109–1120.

Forman SD, Cohen JD, Fitzgerald M, Eddy WF, Mintun MA, Noll DC (1995) Improved assessment of significant activation in functional magnetic resonance imaging (fMRI): Use of a cluster-size threshold. Magnetic Resonance Medicine 33(5): 636–647.

Friedman H, Goldman-Rakic P (1988) Activation of the hippocampus and dentate gyrus by working-memory: A 2-deoxyglucose study of behaving rhesus monkeys. J. Neuroscience 8(12): 4693–4706.

Google (2015) Year one: Progress in the fight against unwanted software. (December 9), https://googleonlinesecurity.blogspot .com/2015/12/year-one-progress-in-fight-against.html.

Heninger WG, Dennis AR, Hilmer KM (2006) Research note– Individual cognition and dual-task interference in group support systems. Inform. Systems Res. 17(4):415–424.

Hibbeln M, Jenkins JL, Schneider C, Valacich JS, Weinmann M (2016) How is your user feeling? Inferring emotion through human–computer interaction devices. MIS Quart. Forthcoming.

Iqbal ST, Bailey BP (2010) OASIS: A framework for linking notification delivery to the perceptual structure of goal-directed tasks. ACM Trans. Comput.-Human Interaction 17(4):1–28.

Iqbal ST, Horvitz E (2007) Disruption and recovery of computing tasks: Field study, analysis, and directions. Rosson MB, Gillmore D, eds. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 677–686.

Jeneson A, Squire LR (2012) Working memory, long-term memory, and medial temporal lobe function. Learn. Memory 19(1):15–25.

Jenkins JL, Durcikova A (2013) What, I shouldn’t have done that? The influence of training and just-in-time reminders on secure behavior. Baskerville R, Chau M, eds. Proc. ICIS 2013, Milan.

Kahneman D (1973) Attention and Effort (Prentice Hall, Englewood Cliffs, NJ).

Logan GD (1978) Attention in character-classification tasks: Evidence for the automaticity of component stages. J. Experiment Psychol. 107(1):32–63.

Mark G, Gudith D, Klocke U (2008) The cost of interrupted work: More speed and stress. Czerwinski M, Lund A, eds. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 107–110.

Mark G, Voida S, Cardello A (2012) A pace not dictated by electrons: An empirical study of work without email. Chi E, Höök K, eds. Proc. SIGCHI Conf. Human Factors Comput. Systems (ACM, New York), 555–564.

Marois R, Ivanoff J (2005) Capacity limits of information processing in the brain. Trends Cognitive Sci. 9(6):296–305.

McFarlane D (2002) Comparison of four primary methods for coordinating the interruption of people in human-computer interaction. Human-Comput. Interaction 17(1):63–139.

McFarlane DC, Latorella KA (2002) The scope and importance of human interruption in human-computer interaction design. Human-Comput. Interaction 17(1):1–61.

Monsell S (2003) Task switching. Trends Cognitive Sci. 7(3):134–140.

Navon D, Miller J (1987) Role of outcome conflict in dual-task interference. J. Experiment Psych.-Human Perceptions Performance 13(3):435–448.

Navon D, Miller J (2002) Queuing or sharing? A critical evaluation of the single-bottleneck notion. Cognitive Psych. 44(3):193–251.

Pashler H (1994) Dual-task interference in simple tasks: Data and theory. Psych. Bull. 116(2):220–244.

Patil S, Hoyle R, Schlegel R, Kapadia A, Lee AJ (2015) Interrupt now or inform later?: Comparing immediate and delayed privacy feedback. Kim J, Begole B, eds. Proc. 33rd ACM Conf. Human Factors Comput. Systems (ACM, New York), 1415–1418.

Phansalkar S, van der Sijs H, Tucker AD, Desai AA, Bell DS, Teich JM, Middleton B, Bates DW (2013) Drug–drug interactions that should be non-interruptive in order to reduce alert fatigue in electronic health records. J. Amer. Medical Inform. Assoc. 20(3):489–493.

Plummer P, Apple S, Dowd C, Keith E (2015) Texting and walking: Effect of environmental setting and task prioritization on dualtask interference in healthy young adults. Gait Posture 41(1): 46–51.

Schon K, Newmark RE, Ross RS, Stern CE (2016) A working memory buffer in parahippocampal regions: Evidence from a load effect during the delay period. Cerebral Cortex 26(5):1965–1974.

Shaft TM, Vessey I (2006) The role of cognitive fit in the relationship between software comprehension and modification. MIS Quart. 30(1):29–55.

Sigman M, Dehaene S (2006) Dynamics of the central bottleneck: Dual-task and task uncertainty. PLoS Biol. 4(7):1227–1238.

Sigman M, Dehaene S (2008) Brain mechanisms of serial and parallel processing during dual-task performance. J. Neuroscience 28(30):7585–7598.

Squire L, Clark R, Bayley P (2004) Medial temporal lobe function and memory. Gazzaniga M, ed. The Cognitive Neurosciences (MIT Press, Cambridge, MA), 691–708.

StatCounter (2015) Statcounter global stats. http://gs.statcounter .com/-desktop-browser-ww-monthly-201408-201508.

Steelman ZR, Hammer BI, Limayem M (2014) Data collection in the digital age: Innovative alternatives to student samples. MIS Quart. 38(2):355–378.

Strayer DL, Johnston WA (2001) Driven to distraction: Dual-task studies of simulated driving and conversing on a cellular telephone. Psych. Sci. 12(6):462–466.

Szameitat AJ, Schubert T, Muller HJ (2011) How to test for dualtask-specific effects in brain imaging studies: An evaluation of potential analysis methods. NeuroImage 54(3):1765–1773.

Tombu M, Jolicœur P (2003) A central capacity sharing model of dual-task performance. J. Experiment Psych.-Human Perceptions Performance 29(1):3–18.

Vance A, Anderson BB, Kirwan CB, Eargle D (2014) Using measures of risk perception to predict information security behavior: Insights from electroencephalography (EEG). J. Assoc. Inform. Systems 15(10):679–722.

Yee K-P (2004) Aligning security and usability. Security Privacy, IEEE 2(5):48–55.

YouTube (2015) Statistics. https://www.youtube.com/yt/press/ statistics.html.

![](/api/attachments/NVMGEYF8/fulltext/images/4efc0992fecaab6d04cbefbe71703b04e930d374e4be2612dc0700d9a15d49ed.jpg)  
This work is licensed under a Creative Commons Attribution-NoDerivatives 4.0 International License. You are free to download this work and share with others commercially or noncommercially, but cannot change in any way, and you must attribute this work as “Information Systems Research. Copyright © 2016, The Author(s). http://dx.doi.org/10.1287/isre.2016.0644, used under a Creative Commons Attribution License: http://creativecommons.org/licenses/ by-nd/4.0/.”
