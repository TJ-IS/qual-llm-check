---
otero_id: 7016
otero_key: "DBHFX2ME"
title: "If erring is human, is system use divine? Omission errors during post-adoptive system use"
authors: "Lazaros Goutas; Basil Hess; Juliana Sutanto"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113225"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# If erring is human, is system use divine? Omission errors during postadoptive system use

Lazaros Goutas<sup>a,⁎</sup>, Basil Hess<sup>b</sup>, Juliana Sutanto<sup>c</sup>

<sup>a</sup> Loughborough University, United Kingdom of Great Britain and Northern Ireland <sup>b</sup> Infosec Global, Toronto, Canada

<sup>c</sup> Lancaster University, United Kingdom of Great Britain and Northern Ireland

## A R T I C L E I N F O

Keywords: Human error Omission error Attention Use history Task variation Prospective memory Post-adoptive system use Mobile application Field study

## A B S T R A C T

Our study contributes to the research on human error during IS use by studying the antecedents of the omission errors that occur during routine instances of computerized work. While attention lapses have been identified as the main mechanism leading to omission errors, we still know little about how such lapses come about during post-adoptive system use. To address this limitation, we draw our theoretical insights from theories of attention and prospective memory to illustrate how the diferent forms of system use carry the potential to explain patterns of human error. Accordingly, we distinguish between two forms of use history that can consist of feature that are either related or unrelated to the execution of a focal task and examine their efects on the frequency of omission errors. We also examine the interaction efects of task variation on the aforementioned relationship. Our hypotheses are tested by analyzing log data associated with the use of a newly introduced mobile application in the context of a sailing sports event. Our results indicate that restricting one's system use on related task features reduces omission errors, whereas a use history based on unrelated task features produces the opposite efects. Further, task diversity positively moderates the relationship between a use history of unrelated features and omission errors. but has no significant moderating effect on the relationship between a use history of related features and omission errors. Our findings hold a number of implications for the literature on human error, and these are discussed alongside with the implications of our study for practitioners and system design.

## 1. Introduction

The title of this paper, which paraphrases Alexander Pope's famous quote, “To err is human, to forgive is divine”, illustrates the main aim of this paper, viz., an inquiry into the antecedents of human error in the context of routine computerized work. Research on human error has a long-standing tradition, and several works have examined instances and the implications of committing errors during computerized work [1–5]. However, we still know little about the antecedents of human error during IS use, and our paper sets out to make a contribution in this direction.

Understanding the conditions under which errors occur during IS use is of paramount importance, because of the high impact that ‘small errors can carry [6]. The recent outage in Amazon Web Services (AWS) that originally occurred because one employee incorrectly typed a command caused disruption to thousands of customers.<sup>1</sup> Second, ‘small errors carry significant economic and behavioral consequences: users on average spend 10% of their working time correcting their errors [1,5]. Last, committing errors while using computers has also been associated with negative emotions such as stress and frustration [4,7,8].

In this study, we focus on omission errors, which is the most frequent form of error [9,10]. Omission errors are typically attributed to some form of attention capture [11,12]. In order to examine how attention failures occur and lead to error during IS use, we are driven by the premise that human error cannot be understood without understanding action, as error is the byproduct of the same cognitive system that produces ‘correct’ actions [13]. From this standpoint, we argue that an enquiry into how patterns of system use are formed carries the potential to explain why errors occur.

As an indicative measure of the diferent patterns of IS use, we focus on the concept of use history, which is defined as the accumulated use of a basket of features that are available in a system and are used to accomplish specified tasks [14,15]. Most importantly, we extend the concept of use history by distinguishing between use histories that are either related or unrelated to the execution of a focal task. Last, given the acknowledged importance of task characteristics in terms of impacting attention [16,17], we further examine the moderating efect of task variation between the two forms of use history and the omission errors committed by IS users.

We test our hypotheses by examining the patterns of system use in a newly introduced mobile application in the context of a sailing sports event, namely the 2012 Kiel Week sailing event. Kiel Week involves about 5000 sailors from 50 diferent nations and attracts approximately three million visitors every year, and is generally considered to be the world's largest sailing event.<sup>2</sup> The mobile application introduced, named “Race Committee Cockpit” (RCC app), was developed for the purpose of facilitating the work of the event's race oficers, who were responsible for monitoring the race conditions, as well as ensuring that race participants comply with the set of rules imposed by the International Sailing Federation (ISAF).

The remainder of the paper is organized as follows. The next section provides a synopsis of work on human error, followed by the presentation of our hypotheses and research model. Section four outlines the research methodology, whereas section five provides the empirical analysis and the results of the study. The final section discusses the broader implications of our enquiry into the antecedents of human error, along with some limitations of the study.

## 2. Related research on human error

## 2.1. Defining error and understanding its underlying causes

The study of human error can be regarded as a discipline in its own right, as this topic can be considered to be as extensive as that covered by the term human performance [12]. Human error is defined as all the occasions in which a planned sequence of mental or physical activities fails to achieve its intended outcome [12]. In this respect, errors involve either a departure from an intended course of action (or a path of actions) planned towards a desired goal, or a deviation from an appropriate behavior at work [18].

Several taxonomies of human error have been developed in order to classify errors.<sup>3</sup> Our study sets out to obtain an understanding of the antecedents of error that occur during the execution of routine proce dural tasks consisting of well-established, goal-oriented task sequences that are commonly performed during IS use. The errors that occur while executing routine task sequences are known as omission errors [21]. An omission error is equivalent to a failure to recall the intention to carry out a task at the right time (e.g. being late to perform an intention), or instances where a necessary item is unwittingly omitted from a task sequence [10]. Omission errors primarily occur at the rule-based level of behavior and monitoring, where the composition of such a sequence of sub-routines in a familiar work situation is typically controlled by a stored rule or procedure [22,23]. Successful task execution at this level involves noticing an environmental cue that is associated in memory with a deferred intention [24]. As such, individuals need to keep the task goals in mind, given that the relevant cues occur while executing a task; moreover, task goals are not uniquely associated with intentions and must compete for retrieval with ongoing task goals [25].

Keeping goal intentions actively maintained is key in terms of avoiding errors [26]. A goal intention comprises of a collection of active cognitive schemata, the activation of which depends on the periodic review of the respective intention [11]. In the absence of such a review process, the activation of cognitive schemata will gradually decline and lead to errors associated with executing a delayed intention [27]. In such cases, internal or external distractors may inappropriately capture ongoing cognition and attention and result in goal neglect errors and action slips [26]. Prior to outlining our theoretical foundations on how attention lapses might occur during IS use and cause omission errors, we next provide a brief overview of existing IS works on human error.

## 2.2. Human error in IS research

Several works in the IS domain have enquired into the topic of human error. Certain studies have explored the efects of system characteristics on the errors committed by a system's users [28,29], whereas other works have explored human error under the prism of training users to commit fewer errors. An interesting debate that has emerged from this literature concerns the connotations associated with committing errors: a number of training studies have sought to identify mechanisms of reducing errors by preventing them from happening, as errors have been conceived to be frustrating and anxiety provoking, and thus disrupting to individual performance [1]. Other studies have stressed the positive efects associated with committing errors, especially with respect to exploring the diferent features of a system and breaking negative habits related to the use of a system [8,30].

Instances of human error have also been explored in other domains of IS research: Sein and Santhanam [31] explored the mechanisms through which committing errors can foster users' learning patterns and the efects of training in this relationship. Recent conceptual works have also attempted to stress the importance of the concept of human error in the IS usage research. For instance, Burton-Jones and Grange [32] highlighted the role of human error in terms of the relationship between efective IS use and performance, by arguing that efective use can improve the efectiveness and eficiency of a system's use by reducing the errors committed and also by improving error recovery.

## 3. Theoretical foundation

## 3.1. An attention-based view of individual behavior

Studies on human error converge on the finding that instances of omission errors can be attributed to attention lapses [10,33,34]. Attention refers to “the taking possession by the mind, in clear and vivid form, of one out of what seem several simultaneously possible objects or trains of thought” ([35], p. 403–404). Diferent types of attention have been identified, including selective attention, attentional vigilance, and executive attention [36,37]. According to Ocasio [37], “selective attention concerns the process by which individuals focus information processing on a specific set of sensory stimuli at a given point in time, whereas attentional vigilance describes the process by which individuals are able to sustain concentration or focus on a particular stimulus (e.g. waiting for a signal to occur). Last, executive attention involves allocating controlled cognitive resources in working memory to information independent from incoming sensory data. It enables individuals to process multiple goals quasi-simultaneously by switching back and forth between diferent stimuli, including directly observed stimuli and stimuli stored in memory, and bringing them together in working memory”.

The ability to devote attention towards the execution of a task is guided by a number of cognitive control capabilities, defined as “the supervisory cognitive mechanisms through which individuals monitor and control their own attention and cognitive processes” ([38], p. 1114). What is also important to note is that individuals' attentional capabilities are bounded because humans have a limited information processing ability and that the number of stimuli that can be attend to are limited [38,39]. It goes without saying that attentional deficits have been associated with negative behavioral and performance outcomes, a notable example of which includes human error [40].

## 3.2. Sustaining attention during task execution – a theory of prospective memory

Within the context of task execution. the role of attention is critical for two reasons: first, successful task execution requires individuals to dedicate attention towards monitoring environmental stimuli in order to draw memory associations and perform an upcoming task. Second, in order to execute of an intended action, attention needs to be shifted to the execution of an ongoing task [27]. The latter is contingent upon an individual's ability to maintain attentional control or to recover access to environmental stimuli or stimulus or goal representations if these are outside an individual's conscious focus [41].

Individuals tend to combine mechanisms for conscious monitoring for environmental cues and automatic retrieval [24]. The former would involve an attention-demanding executive control system that would encode the association between the external event pertinent to the intended action and the intended action itself [42]. In case of the latter, a target event automatically brings to mind the intended action. This system is assumed to support conscious recollection when an external cue automatically interacts with previously encoded actions stored in memory [42]. Automatic retrieval mechanisms are increasingly used as individuals gain experience with a task and task execution becomes automatic. As Dismukes [24] notes, “It would be uncommon for an experienced pilot to arrive at work thinking “I will lower the landing gear today when I turn onto final approach” (and it would be rather alarming if a pilot found this necessary)”.

The extent to which attention-demanding or automatic mechanisms are in operation largely depends on the characteristics of the tasks an individual has to perform, cue quality and strength, as well as the properties of the ongoing activity [42]. In sum, the more conscious mechanisms are used for cue monitoring, the higher the attentional demands placed on an individual. Accordingly, lapses can occur when individuals face either external or internal distractions, and their ability to maintain executive control becomes compromised [16,43]. Attention lapses can also occur when an individual's limited amount of cognitive resources needs to be devoted to an increased number of sources at the same time [44,45].

Taking stock of these insights, our survey of the literature on human error during IS use revealed that even if the link between attention lapses and omission error is acknowledged [17], studies have done little in terms of showing how such lapses come about. Our main proposition is that enquiring into the diverse forms of IS use can help better un derstand how attention lapses and omission errors occur. This position is strengthened by several studies showing that research into how sys tems are used can explain performance outcomes [46]. As Burton-Jones and Grange [32] argue, “…There is always the potential that users may overinvest, underinvest, or misdirect their eforts in creating and using systems… although the creation and use of information systems can improve over time, the process is likely to be never ending and error prone”.

In order to address this topic, and at the same align our study with works arguing that individual experience is a key determinant of human error [17,47], we focus on two distinct forms of system use that evolve over time; a use history that consists of related or unrelated features. We propose that these two forms of system use produce di verse attentional requirements, and accordingly diferentially impact the frequency of omission errors that users commit during system use. We explain these concepts in the next section, where we outline our proposed model.

## 4. A proposed model on omission error during post-adoptive system use

In this section, we outline our research model and hypotheses. In particular, we examine how, 1) the diverse patterns of system use as they evolve over time, and 2) the amount of variation in the tasks that users have to perform, can potentially explain the frequency of omission errors that users commit, given the strain that these two factors place on an individual's attentional ability. By pursuing 1), we join the call by Benlian [48] for additional research on how the changing patterns of system use over time can influence performance outcomes. Accordingly, our choice to study the efects of task variation on the frequency of omission errors that users perform is grounded upon existing studies showing that task characteristics significantly impact the propensity for human error [19]. We explain this argument in more detail in the following sub-sections, where we outline our research hypotheses.

## 4.1. Related and unrelated feature use history

Our main hypothesis is that the cumulative IS use history (and the diverse patterns that use histories can take) can explain the omission errors that users commit by producing diverse attentional requirements. The concept of use history evolves at the post-adoption stage, where users actively choose to explore, adopt, use and possibly extend one or more of a system's features [14]. The latter constitutes one's features in use, and essentially refers to “the basket of system features that are ready to be used by a user to accomplish tasks. System features that do not belong to one's features in use include the features of a system that remain unused, such as the features that are unfamiliar or unknown” ([15], p. 455). Users are in many instances faced with these options, as systems (e.g. word processors and spreadsheets) have many more features than those mandated for work accomplishment [14]. The decision of which features of a system are used can exceed the mandatory use of a system, where users are required to use specific features of an IS in order to execute their tasks [14].

While users decide which system's features become parts of their basket of features in use, they gain experience with what was initially a novel behavior, and engage less frequently in reflective consideration of this behavior and rely instead on previous patterns of behavior to direct their future behavior [14]. As users routinely apply any IS feature within their work context, the ever-accumulating prior-use experiences will imprint these use behaviors within their cognitive scripts and direct them towards task execution. Accordingly, an individual's past behavior will form his/her use history, which is defined as “… a collective, systematic account of an individual's prior use of an IT application and its features… and … learned situational-behavior sequences with respect to an IT application and its features that have become automatic” ([14], p. 542).

The concept of use history has been successful in terms of overcoming some of the shortcomings of earlier measures of system use (e.g. the frequency, duration, and the diferent system functionalities that are used) that have been considered to be too simplistic to capture the relationship between system use and its resulting outcomes [15,49]. This has been achieved through the integration of the diverse features of a system that actively form a user's basket of features in use with the evolution of use over time. In short, it has been argued that examining post-adoptive behavior at a feature level of analysis can provide insights into why users develop diverse patterns of feature use and, as a result, extract diferential value from an IS [14].

Notwithstanding the promise of the construct of use history in terms of explaining behavioral and performance outcomes (omission errors in our case), the related research on the features in use has yielded inconclusive results with respect to user performance. For instance, it has been argued that expanding one's basket of features in use is a form of exploratory behavior that enhances one's knowledge and mastery of a system's features that enhances individual performance [15]. An extended number of features in use also leads to other positive outcomes, such as an increased sense of autonomy and cognitive stimulation from the work environment [50]. In contrast, other studies have shown that a higher number of features in use does not necessarily lead to perfor mance increases; the adoption of additional features can take place in nonproductive ways, or similarly users may be overwhelmed by the presence of too many features, resulting in an inability to choose among feature sets or to apply the features efectively in their work [14,51].

We address these seemingly contradicting results by distinguishing between a related feature use history (RFUH) and an unrelated feature use history (UFUH). The diference between the two constructs is that RFUH includes all those features in use that are necessary for the execution of a focal task, whereas UFUH includes the use of features that are not directly related to the successful completion of this task, but can nevertheless exist in a system and form a user's basket of features in use (and one's use history). To ofer an example of UFUH, while typing this paper on a Microsoft Word processor, one of the authors clicked on the ‘SmartArt’ feature and started experimenting with diferent options, even though the task of writing this paper did not require the use of this feature in any way. In short, the cumulative use of features that are unrelated to the execution of a task (even though the use of this feature might have been required in the execution of a diferent task) constitutes UFUH. It can therefore be inferred that what counts as UFUH is dictated by the nature of the task that has to be performed, hence what is as an unrelated feature in use could be considered as a related feature in use at another point. This distinction can be particularly salient in work environments that involve the execution of routine tasks, where the potential of adapting the diferent features in use in order to exploit the benefits of explorative behavior makes little sense, given that successful task execution is performed in standardized, pre-specified ways.

Given that task execution at the rule-based level of regulation tends to become automatic over time [24,27], we essentially propose that a use history based on related features will lead to fewer omission errors, whereas a use history of unrelated features will produce the exact opposite results. RFUH implies higher attentional afordances that can be beneficial in the context of task execution, as the increased ability to maintain focus on task execution will lead to a less error-prone behavior [52]. This is because cues associated with an upcoming task will be able to produce a stronger association with existing memory traces of prior system use that have been based solely on task execution. In this respect, users do not have to ‘consume’ significant attentional resources to switch back and forth between efortful and automatic forms of monitoring for environmental cues. Similar to a routinized behavior that frees up mental resources and allows users to rapidly process information with little efort [38,53,54], RFUH will lead to fewer errors due to the lower attentional demands that it creates. Hence, we hypothesize:

Hypothesis 1. (H1) RFUH is negatively related to the number of omission errors committed by a system's users.

In contrast, we expect that a use history based on unrelated feature will produce the inverse efects. UFUH essentially refers to cumulative system use that occurs during task execution and is unrelated to it. As UFUH is likely to occur because users want to actively experiment with a system or just ‘play around’, it is expected to draw many linkages to the concept of mind wandering, which includes situations where “executive control shifts away from a primary task to the processing of personal goals that are unrelated to the focal task, and occurs without intention or even awareness that one's mind has drifted” ([44], p. 946). Omission errors are known to occur during such instances of mind wandering [43], and recent studies have shown that the link between mind wandering and human error becomes even stronger when taking into account the detrimental effects of mind wandering when it accumulates over time [26,45]. In the case of UFUH, users will have to resort to more attention-demanding forms of cue monitoring. This is because the link between cues for upcoming tasks and memory traces will be weaker, given that an increased number of unrelated features will form part of users' memory scripts. As users will also have to dedicate attentional resources to ongoing task execution, as well as to recovery from task-unrelated thinking, we expect UFUH to lead to a higher number of omission errors. Accordingly, we hypothesize:

Hypothesis 2. (H2) UFUH is positively related to the number of omission errors committed by a system's users.

## 4.2. Task variation

Task characteristics are generally defined as the ‘real world’ dimensions that relate to the physical nature of a stimulus [55]. Research into the diferent aspects of task characteristics (e.g. complexity, variety, autonomy, feedback, identity and significance) has widely exhibited how the diferent task features can influence individual and group productivity/performance [56,57], as well as users' learning patterns [58–60].

In the context of human error, task characteristics (e.g. task complexity) have been found to afect both the frequency of errors, as well as the efectiveness of the diferent error recovery strategies [2,28,31,61]. Even if in cases of task execution that take place at the rule-based level of cognitive control and imply a lower level of complexity, the aforementioned findings regarding task complexity are not applicable [4], other task features, in particular the diversity of the tasks that have to be executed, can shed some light on the errors committed by a system's users at this level of cognitive control.

The concept of task variation, namely the frequency of diverse activities that occur while performing a particular task, has gained increased attention in terms of understanding its dynamics with respect to behavioral outcomes [57,59,60]. To ofer a better understanding of the concept of task variation, at a general level, while most activities comprising a task can significantly overlap with those of other tasks, workers still engage in high levels of cognitive activity, presumably due to variation in work content across tasks, such as diferences between consulting projects, surgeries, or legal cases [62]. In line with related works that examined the efects of task characteristics on IS success (e.g., [63]), we hypothesize that task variation will moderate the relationship between use history and omission errors.

Multitasking is widely known to produce additional attentional requirements [40]. In the case of task variation, users will tend to encounter diverse situations, which will require a higher amount of information processing. Moreover, in such cases preplanning tends to be dificult and thus leads to a greater need for acquiring information on an ongoing basis [64]. The more absorbing an ongoing activity is, the less likely that resources will be available for attention-demanding approaches to prospective remembering or that subjects will be able to successfully deploy strategic approaches to cue monitoring [42]. Accordingly, tasks requiring more focus will leave fewer cognitive resources available for task-unrelated activities [44]. Engaging in the latter under higher task variation should result in larger performance decrements (e.g. errors), because they require more active cognitive control [65].

Translating these insights into our study, we expect that conditions of higher task variation will place a bigger strain on a user's limited cognitive resources, given that under conditions of higher task variation successful performance will require users to divide attention among competing task activities. Therefore, users who maintain and enhance a use history of unrelated features are likely to commit more omission errors under task variation. The logic behind this builds on our previous hypothesis: As a use history of unrelated features is in itself attentionconsuming, the likelihood of committing omission errors under conditions of higher task variation will be even higher, as users will be less likely to maintain attentional control, given their limited amount of cognitive resources [44].

Following the same logic, a use history of related features is also likely to be negatively afected by an increased level of task variation, as the increased workload will direct users into the more efortful and resource-consuming patterns of cue monitoring. Under such conditions, users' ability to maintain attentional control might also be compromised, even if such users have a higher ‘attentional bufer’ due to maintaining a use history of related features. In sum, our third and fourth hypotheses are the following:

Hypothesis 3. (H3) Task variation will moderate the relationship between RFUH and the number of omission errors that are committed by a system's users, such that the negative relationship between RFUH and the number of omission errors will be weaker when users have to perform a wider variety of tasks.

Hypothesis 4. (H4) Task variation will moderate the relationship between UFUH and the number of omission errors that are committed by a system's users, such that the positive relationship between UFUH and the number of omission errors will be stronger when users have to perform a wider variety of tasks.

## 5. Research methodology

In this section, we first describe the research setting of our study. This is followed by an overview of our sources of empirical data, which include a combination of hand-written protocol data and log data that were derived from the usage of the RCC app that was deployed in the 2012 Kiel Week sailing event that took place between 16 and 24 June 2012. The last part in this section presents the operationalization of the variables in our model.

## 5.1. The 2012 Kiel Week sailing event and the deployment of the RCC app

In our attempt to identify omission errors during IS use, we collected data from the field deployment of a tablet application, called the Race Committee Cockpit application (RCC app). The RCC app incorporates the ISAF sailing rules<sup>4</sup> and, among others, allows the race oficers to schedule races, communicate start violations, manage the flags, and end races. To further ensure user acceptance of the new system, the race oficers of 2012 Kiel Week were involved in the iterative design and development processes of the RCC app. During the design and development processes, screenshots and early prototypes were demonstrated to them on a weekly basis. Prior to the 2012 Kiel Week sailing event, there was a preparatory sailing event where the application developers joined the race committee boat, and operated the RCC app to show how the RCC app should be used. In the evening before the first day of Kiel Week, there was a briefing session with all race oficers. Besides communicating instructions on how to use the RCC app, the race oficers were asked to practice using the app with ‘dummy’ races.

During the nine days of Kiel Week 2012, 360 races were conducted in 8 diferent race courses, with each race course including a number of races taking place in parallel. For each of the race courses, one dedicated team of race oficers located on a boat next to the race course was responsible for monitoring and refereeing the races. The head of the team was responsible for refereeing the races and communicating with members at shore via a handheld transceiver (VHF radio). One member was responsible for recording race events to the RCC app, which would then be transmitted via cellular network to an information system on the shore and broadcasted live onto the Internet; and two other members of the team were responsible for independently handwriting the race events into pre-defined forms, the so-called race protocols.

## 5.2. Data set: app log data and protocol data

Our first source of data is the hand-written race protocol data (PD) that served as the oficial description of events that took place in each race. In case of oficial complaints by one of the contestant teams, PD would be examined to respond to the complaints. Hence, we considered PD as our reference data. PD informed us of the actions/tasks that had to be performed in the RCC app. Our second source of data included data that was derived from the use of the RCC app. Each action (equal to a click) on the RCC app was logged and stored on the tablet device. Accordingly, the app log data (LD) recorded all the actions that were performed during the races. The use of the RCC app and accordingly the recorded LD actions also mirror tasks that had to be performed; RCC users were encouraged to use the app as accurately as possible, given that the use of hand-written protocols would gradually be substituted by the RCC app (in fact, Kiel Week 2015 was the first event where race monitoring was exclusively based on the RCC app). The comparison between PD and LD allowed us to classify the actions recorded in LD to: use of related features, use of unrelated features, and omission errors.

Some error types are detected from mismatches between LD and PD (e.g., the necessary actions indicated in PD are not evident in LD). In this case we assume that PD serves as the valid reference point and any mismatches in LD indicate errors. One could question this, in the sense that PD could also be a source of errors. We nevertheless maintain PD as a more objective ‘mirror’ of the tasks that had to be performed, firstly because PD was used as the reference point for oficial complaints, and second because all of the errors that we counted depended on actions that had to be performed according to PD; given the nature of tasks that race oficers had to perform, we consider it unlikely that false actions were reported in PD.

In total, 360 races were monitored by eight race oficers, who were named after the code words of maritime alphabet: Alpha, Charlie, Delta, Echo, Foxtrot, Golf, Juliet and Kilo. Out of the 360 races, 230 races could be linked to complete PD access and be translated into a digital format, and were consequently included in the data set. During the 230 races, a total of 3439 actions were recorded that were classified as related and unrelated feature uses. During a majority of the races (144 races), each race oficer had to administer at least two races in parallel. These 144 parallel races that corresponded to 2381 actions (related and unrelated feature uses) were used for the analysis. Our analysis was limited to 144 races, as the computation of some of our variables required the administration of at least one parallel race.

## 5.3. Operationalization of the variables

The dependent variable in our study is the number of omission errors committed in each race, which are classified as errors (ERROR). The main variables in our study are: related feature use history (RFUH), unrelated feature use history (UFUH), and task variation (TV).

$E R R O R _ { i j }$ is the number of omission errors in race j committed by the race oficer $i . ~ O _ { E R R O R _ { i j } } \in [ 0 , 9 ]$ consists of the following errors:

error : The running flag was not set.

error : The running course was not set.

error : The XRAY flag was set, but was never unset.

error : The BLUE flag was set, but was never unset.

error : According to PD, the race had ended, but the BLUE flag was not set.

error : The BLUE flag was set and immediately unset. This means the user noticed that he/she did not properly set the BLUE flag, and corrected it by firstly setting the BLUE flag, and then unsetting the BLUE flag again.

error : According to PD, a race started at time t, but the start of the race in LD was recorded at time $t + n .$ . To account for the possible processing delay of the RCC app and after consulting with the race committee oficers, we only count this error ${ \mathrm { i f ~ } } | n \ | \ > \ 9 0 \ s$

error : According to PD, the first boat crossed the finish line at time t, but the event in LD was recorded at time $t + n .$ To account for the possible processing delays and after consulting with the race committee oficers, we only count this error ${ \mathrm { i f ~ } } | n \mid { \mathrm { ~ > ~ } } 6 0 { \mathrm { ~ s } } $

error : According to PD, the last boat crossed the finish line at time t, but the event in LD was recorded at time $t + n .$ To account for the possible processing delays and after consulting with the race committee oficers, we only count this error ${ \mathrm { i f ~ } } | n \mid ~ > ~ 6 0 ~ s$

![](/api/attachments/DBHFX2ME/fulltext/images/e957cb90d0cc368731fee5b1cf0247cf267ac37b5e99371c529d1defe2b67573.jpg)  
Fig. 1. Examples of errors derived from LD and PD.

Our pool of omission errors includes both ‘pure’ omissions (error1–error5), where a necessary item is unwittingly omitted from a task sequence, as well as an additional set of omission errors (error6–error9), where the intention to carry out an action is not recalled at the right time [10]. For errors 7–9, we had to decide on a decide on an acceptable minimum amount of delay that would count as an omission error beyond reasonable doubt. To achieve this, we consulted the Race Committee Oficers, as well as the Head of the Racing Committee whose role was instrumental in the design and rollout of the RCC app. Examples of errors derived from LD and PD are shown in Fig. 1. This example shows a correct setting of the PAPA flag (marker 1), but there was an error in scheduling the race (error ; the actual starting time according to PD is 17:00, but it was scheduled in LD to start at 17:05) (marker 2), and there was a missing action of unsetting the BLUE flag (error ) (marker 3).

The set of observed actions in the RCC app that was performed by race oficer i on race j can be classified as related feature use (RFU), unrelated feature use (UFU), and ERROR. Let $a _ { i j }$ denote an action performed by race officer i on race j, and a classifier class (a) ∈ {RFU,UFU,ERROR}. Previously, we explained the list of actions coded as errors that define our dependent variable. The list of actions coded as RFU and UFU are summarized in Appendix A. We first created this list and split actions into related and unrelated features. In order to avoid any mistakes with the operationalization of actions into related and unrelated actions, we checked and confirmed our operationalization of the two variables with the Head of the Race Committee Oficers, who was instrumental in the design and rollout of the RCC app. Following the consultation process, we did not make the operationalization of the variables, as we had a 100% overlap with the Head of the Race Committee.<sup>5</sup>

Let $A _ { i j } = \{ a _ { i j } : c l a s s ( a _ { i j } ) \neq E R R O R \}$ denote the set of related and unrelated features in use during race j on course i. The set of prescribed actions consists of a set of 4 necessary actions derivable from PD (see Appendix B). Let $p a _ { i j }$ denote a prescribed action performed by race oficer i on race j, and let $P A _ { i j }$ denote the set of prescribed actions during race j on course i.

Related Feature Use History $( R F U H ) _ { i j }$ is defined as the cumulative number of related features in use in the RCC app by race oficer i, before race j. That is $R F U H _ { i j } = \Sigma _ { l = 1 } { ^ { j - 1 } } \mid \{ a _ { i l } \in A _ { i l } : c l a s s ( a _ { i l } ) = R F U \} |$

Unrelated Feature Use History $( U F U H ) _ { i j }$ is defined as the cumulative number of unrelated features in use in the RCC app by race oficer i, before race j. That is $U F U H _ { i j } = \Sigma _ { l = 1 } { } ^ { j - 1 } \mid \{ a _ { i l } \in A _ { i l } : c l a s s ( a _ { i l } ) = U F U \} |$

Task Variation $( T V _ { i j } )$ is defined as the amount of variation in the prescribed actions between race $j ~ ( P A _ { i j } )$ and its corresponding parallel races. A detailed explanation of how we computed task variation can be found in Appendix C.

## 5.4. Control variables.

In addition to the dependent and independent variables, we also measured several control variables that we deemed important. These are: 1) the external environmental conditions in terms of the wind strength, 2) the ‘normality’ of a race, and 3) the individual-specific efects of the diferent race oficers.

Wind strength (WIND) was measured for each race and documented in PD. Measurement was done using a wind measurement device on the race committee boats. The unit of wind is knot. Since the race oficer using the RCC app were on a boat ofshore, the environmental condi tion in terms of the wind strength may have an impact on user performance, given that external distractions can potentially cause interruptions and increase the frequency of errors [66], and are also known to impact the propensity of experiencing attention lapses and conse quently performing omission errors [43].

Race Flag (FLAG): In ‘normal’ race situations, race oficers start with raising the PAPA flag. In ‘special’ situations, such as restarting an aborted race, the race oficers may start the race with other flags, such as the BLACK flag. We thus include the race flag as a dummy variable for controlling for the ‘normality’ of the race $( \mathrm { i . e . , F L A G } = 0  \mathrm { P A P A } ,$ FLAG = 1 → other than PAPA). The ‘normality’ of the race may therefore afect the race oficers' tendency to commit errors.

Race Oficer (OFFICER): To account for the individual diferences in cognitive resources (e.g. general mental ability and working memory capacity) that are known to afect the propensity of experiencing attention lapses [67] and conducting omission errors [16], we included each race oficer as a control variable. Those are: ALPHA, CHARLIE, DELTA, ECHO, FOXTROT, GOLF, JULIET, and KILO. The number associated with each oficer refers to the frequency of parallel races that he/she had to administer throughout the sailing event. For the analysis, officer ALPHA was used as the baseline

## 6. Data analysis and results

Before listing the correlation and the descriptive statistics for the variables in our model (Tables 1 and 2), we would like to make a note on the impact and the magnitude of errors in our study: the number of omission errors performed on average per race was 2.43 (St. Dev. $= 1 . 1 8 )$ . To ofer a sense of the relative impact of omission errors, the average number of related features in use (RFU) that RCC users performed per race was 10.2 (St. Dev. = 6.03). Also, every error counts;

Table 1  
Summary of descriptive statistics.

<table><tr><td colspan="5">Continuous variables</td></tr><tr><td></td><td>Min</td><td>Max</td><td>Mean</td><td>Std. Dev</td></tr><tr><td>ERROR</td><td>0</td><td>6</td><td>2.43</td><td>1.18</td></tr><tr><td>WIND</td><td>4.5</td><td>27.0</td><td>14.13</td><td>4.00</td></tr><tr><td>RFUH</td><td>0</td><td>402</td><td>207.45</td><td>90.14</td></tr><tr><td>UFUH</td><td>0</td><td>585</td><td>191.42</td><td>150.63</td></tr><tr><td>TV</td><td>0</td><td>1</td><td>0.37</td><td>0.26</td></tr></table>

Categorical variables

<table><tr><td>Variable</td><td>Frequency</td><td>%</td></tr><tr><td>FLAG-0</td><td>96</td><td>66.7</td></tr><tr><td>FLAG-1</td><td>48</td><td>33.3</td></tr><tr><td>COURSE-ALPHA</td><td>3</td><td>2.1</td></tr><tr><td>COURSE-CHARLIE</td><td>25</td><td>17.4</td></tr><tr><td>COURSE-DELTA</td><td>23</td><td>16.0</td></tr><tr><td>COURSE-ECHO</td><td>20</td><td>13.9</td></tr><tr><td>COURSE-FOXTROT</td><td>16</td><td>11.1</td></tr><tr><td>COURSE-GOLF</td><td>32</td><td>22.2</td></tr><tr><td>COURSE-JULIET</td><td>21</td><td>14.6</td></tr><tr><td>COURSE-KILO</td><td>4</td><td>2.8</td></tr></table>

Table 2  
Correlation statistics.

<table><tr><td></td><td>ERROR</td><td>WIND</td><td>FLAG</td><td>OFFICER</td><td>RFUH</td><td>UFUH</td><td>TV</td></tr><tr><td>ERROR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WIND</td><td>-0.091</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FLAG</td><td>-0.248</td><td>0.061</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>OFFICER</td><td>0.191</td><td>0.142</td><td>0.336</td><td>1</td><td></td><td></td><td></td></tr><tr><td>RFUH</td><td>0.055</td><td>0.001</td><td>-0.046</td><td>0.133</td><td>1</td><td></td><td></td></tr><tr><td>UFUH</td><td>-0.114</td><td>0.010</td><td>-0.153</td><td>0.630</td><td>0.362</td><td>1</td><td></td></tr><tr><td>TV</td><td>-0.115</td><td>0.212</td><td>-0.021</td><td>-0.154</td><td>0.202</td><td>0.033</td><td>1</td></tr></table>

given the criticality of capturing the race accurately in order to avoid and/or address formal complaints from the contestants of the sailing event, no error can be taken lightly.

We also conducted robustness checks for our model using errors 1–5 and errors 6–9 respectively. We obtained similar results as in our main model, with the only diference that the interaction efect between TV and UFUH in the model with errors 1–5 as the dependent variable was not statistically significant. We attribute this to the unbalanced frequency of errors in the two models, given that errors 1–5 did not occur in 52 of the 144 races, whereas errors 6–9 did not occur in only 17 of the 144 races.

Before proceeding with our hypotheses testing, we standardized the coeficients of the continuous variables for ease of comparison. To account for the count data in the dependent variable, we used a Poisson regression model. Allison and Waterman [68] suggest using the negative binomial model as an alternative to Poisson in the presence of over dispersion. Since there is no significant indication of over-dispersion (we are not able to reject the null-hypothesis of equi-dispersion at the 5% significance level), we proceed with a Poisson regression model.<sup>6</sup> Model 1 in Table 3 is without the interaction terms (H1 and H2), whereas Model 2 in Table 3 is with the interaction terms (H3 and H4). The values of variance inflation factor (VIF) for our continuous variables were not higher than 5, which means that no multicollinearity problem exists in any of the models [70]. The regression results of all

Table 3  
Analysis results.

<table><tr><td></td><td>Model 1DV: ERROR</td><td>Model 2DV: ERROR</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>WIND</td><td>-0.010 (0.060)***</td><td>0.015 (0.062)</td></tr><tr><td colspan="3">FLAG-0 (baseline)</td></tr><tr><td>FLAG-1</td><td>-0.166 (0.150)</td><td>-0.206 (0.153)</td></tr><tr><td colspan="3">OFFICER-ALPHA (baseline)</td></tr><tr><td>OFFICER-CHARLIE</td><td>-0.206 (0.407)</td><td>-0.125 (0.430)</td></tr><tr><td>OFFICER-DELTA</td><td>-3.323 (1.261)**</td><td>-3.482 (1.303)**</td></tr><tr><td>OFFICER-ECHO</td><td>-0.109 (0.395)</td><td>-0.064 (0.410)</td></tr><tr><td>OFFICER-FOXTROT</td><td>0.546 (0.415)</td><td>0.532 (0.433)</td></tr><tr><td>OFFICER-GOLF</td><td>0.223 (0.430)</td><td>0.355 (0.445)</td></tr><tr><td>OFFICER-JULIET</td><td>-0.814 (0.474)</td><td>-0.743 (0.485)</td></tr><tr><td>OFFICER-KILO</td><td>-0.511 (0.534)</td><td>-0.467 (0.566)</td></tr><tr><td colspan="3">Main variables</td></tr><tr><td>RFUH</td><td>-0.399 (0.172)*</td><td>-0.432 (0.175)*</td></tr><tr><td>UFUH</td><td>1.227 (0.476)**</td><td>1.335 (0.489)**</td></tr><tr><td>TV</td><td></td><td>-0.064 (0.062)</td></tr><tr><td>RFUH:TV</td><td></td><td>-0.078 (0.068)</td></tr><tr><td>UFUH:TV</td><td></td><td>0.151 (0.061)*</td></tr><tr><td>AIC</td><td>474.46</td><td>473.71</td></tr></table>

<sup>⁎⁎⁎</sup> Significant $\mathrm { a t } < 0 . 0 0 1$  
⁎⁎ Significant $\mathbf { a t } < 0 . 0 1$  
<sup>⁎</sup> Significant $\mathrm { a t } < 0 . 0 5 .$  
<sup>.</sup> Significant $\mathrm { a t } < 0 . 1 .$  
models are summarized in Table 4.

The data analysis shows that RFUH reduces omission errors whereas UFUH increases omission errors. Hence, H1 and H2 are supported. The standardized variables make it possible to compare the magnitudes between the coeficient estimates. As shown in Model 1, UFUH has larger efect on omission errors than RFUH. The efect of UFUH on omission errors is magnified by the degree of variation in terms of the parallel tasks that a race oficer has to perform. Task variation (TV) however has no significant moderating efect on the relationship between RFUH and omission errors. Hence, only H4 is supported. In the next section, we discuss these findings in more detail.

## 7. Discussion

In this section, we discuss the contributions of our study for the research on human error and post-adoptive system use. We also discuss the practical implications of our study in terms of user training and error management. Last, we elaborate on the limitations of our research and the possible extensions that can be made to our study.

## 7.1. Contributions to research

Our study firstly contributes to the post-adoptive system use literature by empirically showcasing how diferent forms of system use can lead to diverse performance outcomes, and in particular into omission errors. We examined the antecedents of omission errors in the context of executing largely standardized, procedural task sequences. Omission errors occurring at this level have typically been attributed to attention lapses. Earlier studies have argued that in such settings, the extent to which such lapses occur can be attributed to the degree of user experience and the characteristics of the tasks that users have to per form [17]. We extended this argument by showing that omission errors are indeed dependent on individuals' cumulative use of a system, and as such we join other works highlighting the importance of better understanding the patterns of system use over time [48]. Most importantly, however, we show that cumulative system use can unfold in diverse ways and diferentially impact the frequency of omission errors.

We drew our insights from the concept of use history [14,15], and we argued that use histories can unfold in diverse ways and produce the inverse efects in terms of committing omission errors; a history of using a system according to features that are related to the execution of specific tasks leads to fewer omissions, whereas a use history that encompasses an extended number of system features leads to the exact opposite results. In this respect, we extend existing studies by arguing that what matters in terms of combatting omission errors during the execution of PM tasks is not the cumulative use of a system per se, but rather cumulative system use in a focused manner.

Table 4 Summary of the results.

<table><tr><td>Hypotheses</td><td>Empirical support</td></tr><tr><td>H1. RFUH is negatively related to the number of omission errors that are committed by a system&#x27;s users.</td><td>Supported</td></tr><tr><td>H2. UFUH is positively related to the number of omission errors that are committed by a system&#x27;s users.</td><td>Supported</td></tr><tr><td>H3. Task variation will moderate the relationship between RFUH and the number of errors that are committed by a system&#x27;s users, such that the positive relationship between RFUH and the number of omission errors will be weaker when users have to perform a wider variety of tasks.</td><td>Not supported</td></tr><tr><td>H4. Task variation will moderate the relationship between UFUH and the number of errors that are committed by a system&#x27;s users, such that the negative relationship between UFUH and the number of omission errors will be stronger when users have to perform a wider variety of tasks.</td><td>Supported</td></tr></table>

Additionally, our study shows that using an extended number of a system's features can be a double-edged sword: while a number of studies have highlighted the benefits of IS infusion ([71]: [82]. or that extended, innovative, or emergent use can be a means of fostering individual mindfulness and maintaining performance reliability [15,72,73], we show that in the context of routine, procedural tasks that do not necessarily require devising innovative solutions, an extended use of a system's features can produce adverse efects on user performance. This is not to say that our study downplays any of the acknowledged positive efects of mindful use in terms of combatting error [72]. Given that mindfulness is equally about the quality of attention as it is about the conservation of attention [74], we argue that it is important to emphasize that innovative or extended use (an inherent component of mindful use) is also resource consuming and can be redundant in certain task contexts.

At the theoretical level, we argued that the key to successful task execution is noticing environmental cues, which in turn trigger intended actions by involving mechanisms that draw associations with existing memory [42]. The process of cue monitoring can either involve more conscious, efortful and attention-demanding mechanisms, or it can involve mechanisms where such associations are done automatically. Automatic retrieval becomes increasingly the norm as task execution becomes repetitive over time. Nonetheless, depending on a number of parameters (e.g. task characteristics, cue quality and strength), attention-demanding mechanisms can complement the more resource-free mechanisms. In sum, given the limited amount of cognitive resources that any individual is equipped with, the more conscious mechanisms are used for cue monitoring, the higher the attentional demands, and consequently the higher the probability of lapses and errors.

While this framework initially provides support to our findings, our study nevertheless provides some nuanced findings and makes some possible extensions: firstly, contrary to what we hypothesized, we did not find support for the moderating efect of task variation on the relationship between RFUH and omission error. While it is likely that users were able to maintain an ‘attentional bufer’ from this relatively resource-free form of use history, the negative coeficient of the moderating efect (albeit not significant) seems to suggest that the additional burden of task variation starts to consume the attentional ‘bufer’. Perhaps more importantly, there is a need for better conceptualization and measurement of the attentional requirements of both ongoing and PM tasks.

Secondly, the literature on human error argues that it is important to examine the characteristics of the prescribed tasks that individuals have to perform in order to assess whether attention-demanding or automatic mechanisms of cue monitoring will be in operation. Our study shows that it is equally important to complement the study of ongoing task characteristics with an examination of the actual activities during task execution, given that the two forms of use history in our study lead to the exact opposite performance results. In this respect, our study contributes to the ongoing debate around the ways in which task variation impacts task performance [62]. In sum, our unique empirical setting and dataset that included a documentation of both prescribed and performed actions, enabled us to conduct such an enquiry and yielded some highly interesting results.

## 7.2. Implications for practice

Our study holds several practical implications: First, we observe that providing users with initial training is simply not enough in terms of combating errors. In our study, users received training, not only in terms of obtaining detailed instructions about the procedures they had to follow prior to the real-time use of the system, but also in terms of having ample time to practice with the system on their own, thus resembling the two types of procedural and conceptual model training procedural [75]. As a number of users tend to disregard training manuals and similar support systems [76], it is important for organizations to understand the conditions under which errors occur in situ. To this efect, our study shows that in the case of executing procedural tasks, particular attention should be paid on how systems are used over time. Efective error management techniques should therefore not only consist of regular monitoring of the ways in which use histories are formed, but also of targeted interventions in cases of deviance from patterns of related feature use.

It is important for such interventions to occur before a use history of unrelated features turns into routinized action. An additional implica. tion of our study is that suitable mechanisms of sustaining attention also need to be identified, and most importantly including such elements into user training also seems imminent. In this respect, investing in training to enhance users' cognitive abilities (i.e. general mental ability and working memory capacity) seems to be a worthwhile undertaking. While research on the efects of training on working memory abilities has yielded inconclusive results, it has been acknowledged that such eforts make sense in the context of executing routine tasks.<sup>7</sup> Last, it is important to note that in cases where ‘playing around’ during system use cannot be avoided, it is best if such user behavior takes place under conditions where task variation is the lowest; even if high task variation might make users more alert [17], an increasing use of unrelated features will undermine user performance, and make the shift to patterns of related feature use more dificult.

From a system design perspective, it is acknowledged that investing in system-based error correction mechanisms can be problematic, especially in the case of end user computing [77]. Nevertheless, introducing features that sustain users' attentional abilities (e.g. through arousal techniques and/or regular reminders) appears to be a sensible option. Nonetheless, our results indicate that the most important thing in terms of combating omission errors is to redirect individuals from the use of unnecessary features, and most importantly to avoid that such patterns of usage become routinized over the course of time. As such, restricting system use during the earlier stages of system deployment to only related and mandatory features appears to be eminent in order to combat omission error, as users have limited knowledge of a system's features at this stage [78].

## 7.3. Limitations and suggestions for future research

Our study also comes along with a number of limitations: First, we focus only on omission errors that take place at the level of rule-based regulation. While on the one hand we cover a broad spectrum of omission errors at this level of cognitive control, our study does not explore other classes of errors that occur at the knowledge and the skillbased level of cognitive regulation. Future studies can complement ours by examining whether and how the diverse forms of system use also afect the patterns of errors occurring in settings that involve the execution of more complex tasks. It could be the case that under such conditions, an extended basket of features in use that accumulates over time and encapsulates patterns of emergent and integrative use [79], might produce diferent results from ours. Second, our hypotheses were tested over a set period of time and in a sailing sport setting; future studies could firstly examine whether our inferences hold over a larger time span, given that patterns of system use are likely to change over the course of time [80]. Future studies could also test our hypotheses in more ‘typical’ settings of computerized work (e.g. in spreadsheet development), as computerized work in the context of sailing sports may produce certain peculiarities that compromise the generalizability of our findings.

Also, we strongly believe that the concept of attention will gain a more prominent position in the literature on post-adoptive system use. Testing the efects of the diferent aspects of usage (e.g. the duration and the scope of usage, the intention to use a system and the perceived ease of use) on users' attentional abilities and patterns of attention allocation can yield novel insights into how system usage afects both positive and negative aspects of performance.

Last, a large body of research in the area of mind wandering has shown that when individuals experience attention lapses, they tend to lose focus and the mind shifts into internal trains of thought that are unrelated to ongoing task execution, which leads to errors [16,26,81]. Future research on post-adoptive system use could also benefit from examining the interplay between such internal trains of thought and the diverse patterns of system use. Such an enquiry can shed further light into how use histories are formed, and how positive and negative aspects of user performance are ultimately afected.

## 8. Conclusion

In this study we have sought to stress the need to study errors during post-adoptive system use, and we attempted to examine human error under the prism of how the information systems are actually used over time, while executing procedural tasks. Our analysis yielded some interesting results: when systems are used repeatedly in a focused manner, users tend to commit fewer errors. In contrast, when unrelated features become embedded in individuals' use history, the efects can be deleterious, even more so under conditions of high task variation. In sum, human error in system usage is a persistent problem in modern organizations, even in times where automation is more pervasive than ever before; given that humans are ultimately the end users of a system and those primarily responsible for error, our study contributes towards the efective management of error by stressing the need to enquire into how systems are used, and in particular by examining the formation of use histories.

## Author contribution

All authors contributed equally to this paper.

## Appendix A. List of actions

<table><tr><td>Identifier</td><td>Action</td><td>Related feature</td><td>Unrelated feature</td><td>Explanation and comments</td></tr><tr><td>id1</td><td>Select race</td><td>x</td><td>x</td><td>Selecting a race to officiate. When this action was performed one time per each parallel race, we coded it as related feature use. When it was performed more than once per each parallel race, we coded it as unrelated feature use.</td></tr><tr><td>id2</td><td>Set start time</td><td>x</td><td></td><td>Setting the starting time of a race.</td></tr><tr><td>id3</td><td>Reset start time</td><td>x</td><td></td><td>Reschedule the starting time of a race.</td></tr><tr><td>id4</td><td>Reset time button</td><td>x</td><td></td><td>Pressing the button reset time after the start time was rescheduled</td></tr><tr><td>id5</td><td>Set running flag/PAPA</td><td>x</td><td>x</td><td rowspan="2">Setting running flag. When each of these actions was performed one time per race, we coded it as related feature use. When they were performed more than once per race, it was coded as unrelated feature use, as only one out of the four flags can be raised during the course of a race.</td></tr><tr><td>id6</td><td>Set running flag/ZULU</td><td>x</td><td>x</td></tr><tr><td>id7</td><td>Set running flag/BLACK</td><td>x</td><td>x</td><td></td></tr><tr><td>id8</td><td>Set running flag/INDIA</td><td>x</td><td>x</td><td></td></tr><tr><td>id9</td><td>Postpone race</td><td>x</td><td></td><td>Postpone a race which is not yet started</td></tr><tr><td>id10</td><td>Postpone race/ALPHA</td><td>x</td><td></td><td>Postpone a race which is not yet started with a remark that there is no more racing today</td></tr><tr><td>id11</td><td>Postpone race/HOTEL</td><td>x</td><td></td><td>Postpone a race which is not yet started with a remark that further information is available offshore</td></tr><tr><td>id12</td><td>abortSt</td><td>x</td><td></td><td>Abandon and postpone a race during the start phase</td></tr><tr><td>id13</td><td>abortSt/ALPHA</td><td>x</td><td></td><td>Abandon race during the start phase with a remark that there is no more racing today</td></tr><tr><td>id14</td><td>abortSt/HOTEL</td><td>x</td><td></td><td>Abandon a race during start phase with a remark that further information is available offshore</td></tr><tr><td>id15</td><td>Set individual recall/XRAY</td><td>x</td><td></td><td>Starting an individual recall</td></tr><tr><td>id16</td><td>Unset individual recall/XRAY</td><td>x</td><td></td><td>Ending of an individual recall</td></tr><tr><td>id17</td><td>General recall/yes</td><td>x</td><td></td><td>Recall the whole race (answering Ok in confirmation dialog)</td></tr><tr><td>id18</td><td>General recall/no</td><td></td><td>x</td><td>Canceling recall of the whole race</td></tr><tr><td>id19</td><td>Set running course/yes</td><td>x</td><td></td><td>Setting the running course</td></tr><tr><td>id20</td><td>Set running course/no</td><td></td><td>x</td><td>Canceling setting the running course</td></tr><tr><td>id21</td><td>abortAp</td><td>x</td><td></td><td>Abandon and postpone a running race</td></tr><tr><td>id22</td><td>abortNovember</td><td>x</td><td></td><td>Abandon a running race with a remark that more information is available at the start line</td></tr><tr><td>id23</td><td>Set blue flag/yes</td><td>x</td><td></td><td>Signaling that the first boat has crossed the finish line</td></tr><tr><td>id24</td><td>Set blue flag/no</td><td></td><td>x</td><td>Canceling the signal that the first boat has crossed the finish line</td></tr><tr><td>id25</td><td>Unset blue flag/yes</td><td>x</td><td></td><td>Signaling that the last boat has crossed the finish line</td></tr><tr><td>id26</td><td>Unset blue flag/no</td><td></td><td>x</td><td>Canceling the signal that the last boat has crossed the finish line</td></tr><tr><td>id27</td><td>Login</td><td></td><td>x</td><td>Login to another race course administered by another user</td></tr><tr><td>id28</td><td>Cancel login</td><td></td><td>x</td><td>Canceling login</td></tr><tr><td>id29</td><td>Select event</td><td></td><td>x</td><td>Select sailing event (after login)</td></tr><tr><td>id30</td><td>Select course</td><td></td><td>x</td><td>Select course (after selecting an event)</td></tr><tr><td>id31</td><td>Select label</td><td></td><td>x</td><td>Click on the label of the RCC app that has no functionality</td></tr><tr><td>id32</td><td>Reset race/no</td><td></td><td>x</td><td>Canceling reset race</td></tr></table>

Appendix B. List of prescribed actions

<table><tr><td>Identifier</td><td>Action</td><td>Explanation and comments</td></tr><tr><td>pa1</td><td>Start time</td><td>The start time of the race, as documented on the hand-written protocols.</td></tr><tr><td>pa2</td><td>Running flag</td><td>The running flag that was raised (PAPA, ZULU, BLACK or INDIA) as documented on the hand-written protocols.</td></tr><tr><td>pa3</td><td>Set blue flag</td><td>Signaling that the first boat has crossed the finish line (as documented on the hand-written protocols)</td></tr><tr><td>pa4</td><td>Unset blue flag</td><td>Signaling that the last boat has crossed the finish line (as documented on the hand-written protocols).</td></tr></table>

## Appendix C. Operationalization of task variation

Task Variation $\mathrm { ( T V _ { i j } ) }$ is defined as the variability of the prescribed actions between race j $( P A _ { i j } )$ and its corresponding parallel races. We measure $\mathrm { T V _ { i j } }$ as (1 – task similarity). Task similarity is quantified in a vector space model, a technique frequently used for information retrieval tasks such as comparing similarities of documents or websites. Objects can be represented as a vector. Similarity between the vectors is calculated as the absolute value of the cosine of the angle between the vectors. Consider the set $P A _ { i j } ,$ for each parallel race $k ,$ we extract the overlapping actions (OA) in time for race k as follows:

$O A _ { k } = \{ p a _ { i k } \in P A _ { i k } : t i m e ( p a _ { i k } ) \in [ t _ { m i n } , ^ { j } , t _ { m a x } ^ { ~ j } ] \}$ , namely all actions on race k between the first action (at time $t _ { m i n } ^ { ~ j } )$ and the last action (at time $t _ { m a x } ^ { j } )$ on race j respectively.

Let ${ t _ { m i n } } ^ { k }$ and $t _ { m a x } ^ { k }$ denote the time of the first and last related feature use in $O A _ { k }$ respectively. We extract the overlapping actions in the race under investigation (race j) as follows:

$O A _ { j } = \{ p a _ { i j } \in P A _ { i j } : t i m e ( p a _ { i j } ) \in [ t _ { m i n } { } ^ { k } , t _ { m a x } { } ^ { k } ] \}$ , namely all actions on race j between the first action (at time $t _ { m i n } ^ { k } )$ and the last action (at time $t _ { m a x } ^ { k } )$ on race k respectively.

We then map the overlapping actions $O A _ { k }$ and $O A _ { j }$ to a vector space. As the actions correspond to 4 related features in use that are listed in this Appendix, we map $O A _ { k }$ and $O A _ { j }$ to 4-dimensional vectors $\overrightarrow { O A _ { k } }$ and $\overrightarrow { O A _ { j } }$ which contain a value of zero or one. The similarity between $\overrightarrow { O A _ { k } }$ and $\overrightarrow { O A _ { j } }$ is defined as follows: $\begin{array} { r } { ( \overrightarrow { O A _ { k } } , \overrightarrow { O A _ { j } } ) = \left| \frac { \overrightarrow { O A _ { k } } \cdot \overrightarrow { O A _ { j } } } { \| \overrightarrow { O A _ { k } } \| \| \overrightarrow { O A _ { j } } \| } \right| , } \end{array}$ whereas $\overrightarrow { O A _ { k } }$ is the vector with the overlapping actions of race $\mathbf { k } ,$ and $\overrightarrow { O A _ { j } }$ is the vector with the overlapping actions of race j. The absolute value of cosine yields a value between 0 and 1, ranging from minimum to maximum similarity. In case of multiple parallel races, we take the average of the similarity indices to obtain the TS measure.

## References

[1] F.C. Brodbeck, D. Zapf, J. Prümper, M. Frese, Error handling in ofice work with computers: a field study, J. Occup. Organ. Psychol. 66 (4) (1993) 303–317.

[2] D.F. Galletta, D. Abraham, M. El Louadi, W. Lekse, Y.A. Pollalis, J.L. Sampler, An empirical study of spreadsheet error-finding performance, Account. Manag. Inf. Technol, 3 (2) (1993) 79–95

[3] D.F. Galletta, K.S. Hartzel. S.E. Johnson, J.L, Joseph, S. Rustagi, Spreadsheet presentation and error detection: an experimental study, J. Manag, Inf. Syst. (1996) 45–63.

[4] D. Zapf, F.C. Brodbeck, M. Frese, H. Peters, J. Prümper, Errors in working with office computers: a first validation of a taxonomy for observed errors in a field setting, International Journal of Human-Computer Interaction 4 (4) (1992) 311–339.

[5] D. Zapf, G.W. Maier, G. Rappensperger, C. Irmer, Error detection, task characteristics, and some consequences for software design, Appl. Psychol. 43 (4) (1994) 499–520.

[6] J.L. Carlo, K. Lyytinen, R.J. Boland Jr., Dialectics of collective minding: contradictory appropriations of information technology in a high-risk project, MIS O. 36 (4) (2012) 1081–1108.

[7] P. De Vries, C. Midden, D. Bouwhuis, The effects of errors on system trust, self confidence, and the allocation of control in route planning International Journal of Human-Computer Studies 58 (6) (2003) 719–735.

[8] M. Frese, F. Brodbeck, T. Heinbokel, C. Mooser, E. Schleifenbaum, P. Thiemann, Errors in training computer skills: on the positive function of errors, Human-Computer Interaction 6 (1) (1991) 77–93.

[9] P.E. Love, D.J. Edwards, Z. Irani, D.H. Walker, Project pathogens: the anatomy of omission errors in construction and resource engineering project, IEEE Trans. Eng. Manag. 56 (3) (2009) 425–435.

[10] J. Reason, Combating omission errors through task analysis and good reminders, Quality and Safety in Health Care 11 (1) (2002) 40–44.

[111 J. Reason. Lapses of attention in everyday life, in: R. Parasuraman, D. Davis (Eds.) Varieties of Attention, Academic Press, New York, 1984, pp. 179–189.

[12] J. Reason, Human Error, Cambridge University Press, 1990.

[13] P.A. Booth, Errors and theory in human-computer interaction, Acta Psychol. 78 (1 (1991) 69–96.

[14] J.S. Jasperson, P.E. Carter, R.W. Zmud, A comprehensive conceptualization of postadoptive behaviors associated with information technology enabled work systems, MIS Q. 29 (3) (2005) 525–557.

[15] H. Sun, Understanding user revisions when using information system features: adaptive system use and triggers, MIS Q. 36 (2) (2012) 453–478.

[16] J.G. Randall, F.L. Oswald, M.E. Beier, Mind-wandering, cognition, and performance: a theory-driven meta-analysis of attention regulation, Psychol. Bull. 140 (6) (2014) 1411–1431.

[17] P.K. Sanjram, A. Khan, Attention, polychronicity, and expertise in prospective memory performance: Programmers’ vulnerability to habit intrusion error in multitasking, International Journal of Human-Computer Studies 69 (6) (2011) 428–439.

[18] J. Reason, A. Hobbs, Managing Maintenance Error: A Practical Guide, Ashgate, Aldershot, 2003.

[19] M.I. Bolton. A task-based taxonomy of erroneous human behavior. International Journal of Human-Computer Studies 108 (2017) 105–121.

[20] D. Hofmann, M. Frese, Errors, error taxonomies, error prevention, and error management: laying the groundwork for discussing errors in organizations, in: D. Hofmann, M. Frese (Eds.), Errors in Organizations, Routledge, Taylor & Francis, New York, 2011, pp. 1–44.

[21] R.R. Panko, S. Aurigemma, Revising the Panko–Halverson taxonomy of spreadsheet errors, Decis, Support, Syst, 49 (2) (2010) 235–244.

[22] J. Rasmussen, Skills, rules, and knowledge; signals, signs, and symbols, and other distinctions in human performance models, IEEE Transactions on Systems, Man and Cybernetics (3) (1983) 257–266

[23] J. Rasmussen. K. Vicente. Coping with human errors through system design: im: plications for ecological interface design, International Journal of Man-Machine

Studies 31 (5) (1989) 517–534.

[24] K. Dismukes, Concurrent task management and prospective memory: pilot error as a model for the vulnerability of experts, Proceedings of the Human Factors and Ergonomics Society Annual Meeting 50 (9) (2006) 909–913.

[25] S. Loft, R.W. Remington, Prospective memory and task interference in a continuous monitoring dynamic display task, J. Exp. Psychol. Appl. 16 (2) (2010) 145–157.

[26] J.C. McVay, M.J. Kane, Drifting from slow to “d’oh!”: working memory capacity and mind wandering predict extreme reaction times and executive control errors, J. Exp. Psychol. Learn. Mem. Cogn. 38 (3) (2012) 525–549.

[27] P.K. Sanjram, Attention and intended action in multitasking: an understanding of cognitive workload, Displays 34 (4) (2013) 283–291.

[28] S. Goswami, H.C. Chan, H.W. Kim, The role of visualization tools in spreadsheet error correction from a cognitive fit perspective, J. Assoc. Inf. Syst. 9 (6) (2008) 321–343.

[29] J. Lazar, A. Allen, J. Kleinman, C. Malarkey, What frustrates screen reader users on the web: a study of 100 blind users, International Journal of Human-Computer Interaction 22 (3) (2007) 247–269.

[30] N. Keith, M. Frese, Efectiveness of error management training: a meta-analysis, J. Appl. Psychol. 93 (1) (2008) 59.

[31] M.K. Sein, R. Santhanam, Research report. Learning from goal-directed error recovery strategy, Inf. Syst. Res. 10 (3) (1999) 276–285.

[32] A. Burton-Jones, C. Grange, From use to efective use: a representation theory perspective, Inf. Syst. Res. 24 (3) (2013) 632–658.

[33] D.A. Norman, Categorization of action slips, Psychol. Rev. 88 (1) (1981) 1–15.

[34] J. Reason, Human error: models and management, BMJ 320 (7237) (2000 768–770.

[36] A.J. Hofman, W. Ocasio, Not all events are attended equally: toward a middle range theory of industry attention to external events, Organ. Sci. 12 (4) (2001) 414-434.

[37] W. Ocasio, Attention to attention, Organ. Sci. 22 (5) (2011) 1286–1296.

[38] D. Laureiro-Martinez, Cognitive control capabilities, routinization propensity, and decision-making performance, Organ. Sci. 25 (4) (2014) 1111–1133.

[39] H.E. Pashler, The Psychology of Attention, MIT Press, Cambridge, MA, 1999.

[40] D. Kahneman, Attention and Efort, Prentice-Hall, Englewood Clifs, NJ, 1973.

[41] R.W. Engle, M.J. Kane, Executive attention, working memory capacity, and a twofactor theory of cognitive control, in: B. Ross (Ed.), The Psychology of Learning and Motivation, Academic Press, New York, NY, 2004, pp. 145–199.

[42] M.A. McDaniel, G.O. Einstein, Strategic and automatic processes in prospective memory retrieval: a multiprocess framework, Appl. Cogn. Psychol. 14 (7) (2000) S127–S144.

[43] S.M. Casner, J.W. Schooler, Vigilance impossible: diligence, distraction, and day dreaming all lead to failures in a practical monitoring task, Conscious. Cogn. 35 (2015) 33–41.

[44] J. Smallwood, J.W. Schooler, The restless mind, Psychol. Bull. 132 (2006) 946–958.

[45] D.R. Thomson, P. Seli, D. Besner, D. Smilek, On the link between mind wandering and task performance over time, Conscious. Cogn. 27 (2014) 14–26.

[46] A. Burton-Jones, D.W. Straub Jr., Reconceptualizing system usage: an approach and empirical test, Inf. Syst. Res. 17 (3) (2006) 228–246.

[47] M. Frese, N. Keith, Action errors, error management, and learning in organizations, Annu, Rey, Psychol, 66 (2015) 661–687.

[48] A. Benlian, IT feature use over time and its impact on individual task performance, J. Assoc, Inf, Syst. 16 (3) (2015) 144–173.

[49] I. Benbasat, H. Barki, Ouo vadis TAM? J. Assoc, Inf, Syst, 8 (4) (2007) 211–218

[50] T.G. Gill. Expert systems usage: task change and intrinsic motivation. MIS O. 20 (3 (1996) 301–329.

[51] M.S. Silver, Decision support systems: directed and nondirected change, Inf. Syst. Res, 1 (1) (1990) 47–70.

[52] I. Aggarwal, A.W. Woolley, Do you see what I see? The efect of members’ cognitive styles on team processes and errors in task execution, Organ. Behav. Hum. Decis. Process, 122 (1) (2013) 92–99.

[53] J.A. Bargh, T.L. Chartrand, The unbearable automaticity of being, Am, Psychol, 54 (7) (1999) 462.

[54] M.D. Cohen, R. Burkhart, G. Dosi, M. Egidi, I, Marengo, M. Warglien, S. Winter. Routines and other recurring action patterns of organizations: contemporary research issues, Ind. Corp. Chang. 5 (3) (1996) 653–698.

[55] R.E. Wood, Task complexity: definition of the construct, Organ. Behav. Hum. Decis. Process, 37 (1) (1986) 60–82.

[56] R.M. Fuller, A.R. Dennis, Does fit matter? The impact of task-technology fit and appropriation on team performance in repeated tasks, Inf. Syst. Res. 20 (1) (2009) 2-17.

[57] B.R. Staats, F. Gino, Specialization and variety in repetitive tasks: evidence from a Japanese bank, Manag. Sci. 58 (6) (2012) 1141–1159.

[58] T. Mukhopadhyay, P. Singh, S.H. Kim, Learning curves of agents with diverse skill in information technology-enabled physician referral systems, Inf. Syst. Res. 22 (3) (2011) 586–605.

[59] S. Narayanan, S. Balasubramanian, J.M. Swaminathan, A matter of balance: specialization. task variety. and individual learning in a software maintenance en: vironment, Manag, Sci, 55 (11) (2009) 1861–1876

[60] M.A. Schilling, P. Vidal, R.E. Ployhart, A. Marangoni, Learning by doing something else: variation, relatedness, and the learning curve, Manag. Sci. 49 (1) (2003) 39–56.

[61] P.H. Chung, M.D. Byrne, Cue efectiveness in mitigating postcompletion errors in a routine procedural task, International Journal of Human-Computer Studies 66 (4) (2008) 217–232.

[62] E. Avgerinos, B. Gokpinar, Task variety in professional service work: when it helps and when it hurts, Prod. Oper. Manag. 27 (7) (2018) 1368–1389.

[63] R. Sharma, P. Yetton, The contingent efects of training, technical complexity, and task interdependence on successful information systems implementation, MIS Q. 31 (2) (2007) 219–238.

[64] J. Karimi, T.M. Somers, Y.P. Gupta, Impact of environmental uncertainty and task characteristics on user satisfaction with data, Inf. Syst. Res. 15 (2) (2004) 175–193.

[65] R. Kanfer, P.L. Ackerman, Motivation and cognitive abilities: an integrative/aptitude-treatment interaction approach to skill acquisition, J. Appl. Psychol. 74 (1989) 657–690.

[66] C. Speier, J.S. Valacich, I. Vessey, The influence of task interruption on individual decision making: an information overload perspective, Decis. Sci. 30 (2) (1999) 337–360.

[67] M.J. Kane, R.W. Engle, Working-memory capacity and the control of attention: the contributions of goal neglect, response competition, and task set to Stroop interference, J. Exp. Psychol. Gen, 132 (1) (2003) 47–70

[68] P.D. Allison, R.P. Waterman, Fixed–efects negative binomial regression models, Sociol, Methodol, 32 (1) (2002) 247–265

[69] A.C. Cameron, K. Pravin, P.K. Trivedi, Regression-based tests for overdispersion in the poisson model, J. Econ. 46 (3) (1990) 347–364.

[70] J. Cohen, P. Cohen, Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, Lawrence Erlbaum, 1975

[71] K.J. Fadel, User adaptation and infusion of information systems, J. Comput. Inf Syst. 52 (3) (2012) 1–10.

[72] B.S. Butler, P.H. Gray, Reliability, mindfulness, and information systems, MIS Q. 30 (2) (2006) 211–224.

[73] X. Li, J.P.A. Hsieh, A. Rai, Motivational diferences across post-acceptance information system usage behaviors: an investigation in the business intelligence systems context, Inf. Syst. Res. 24 (3) (2013) 659–682

[74] J. McAvoy, T. Nagle, D. Sammon, Using mindfulness to examine ISD agility, Inf. Syst. J. 23 (2) (2013) 155–172.

[75] R. Santhanam, M.K. Sein, Improving end-user proficiency: effects of conceptual training and nature of interaction, Inf. Syst. Res. 5 (4) (1994) 378–399.

[76] A.W. Lazonder, H. van der Meii, Effect of error information in tutorial doc. umentation, Interact. Comput. 6 (1) (1994) 23–40.

[77] B.D. Klein, D.L. Goodhue, G.B. Davis, Can humans detect errors in data? Impact of base rates, incentives, and goals, MIS Q. 21 (2) (1997) 169–190.

[78] A. Durcikova, K.J. Fadel, B.S. Butler, D.F. Galletta, Research note-knowledge ex ploration and exploitation: the impacts of psychological climate and knowledge management system access, Inf. Syst. Res. 22 (4) (2011) 855–866.

[79] V.L. Saga, R.W. Zmud, The nature and determinants of IT acceptance, routinization, and infusion, Proceedings of the IFIP TC8 Working Conference on Difusion, Transfer and Implementation of Information Technology, 1993, pp. 67–86.

[80] A. Burton-Jones, M.J. Gallivan, Toward a deeper understanding of system usage in organizations: a multilevel perspective, MIS Q. (2007) 657–679.

[81] J. Smallwood, Distinguishing how from why the mind wanders: a process–occurrence framework for self-generated mental activity, Psychol. Bull. 139 (3) (2013 519–535.

[82] S.S. Kim, N. Malhotra, A user empowerment approach to information systems infusion, JEEE Trans, Eng, Manag, 61 (4) (2005) 656–668

Lazaros Goutas is a Lecturer in Information Systems at the School of Business and Economics, Loughborough University, U.K. He received his PhD in Social and Political Science from the University of Cambridge. His research is grounded in the broader do mains of HCI and digital transformation. Part of his work has been published in Decision Support Systems, CACM, Electronic Markets, and his most recent work is currently under review in leading information systems journals

Basil Hess is a Chief Cryptographic Engineer at Infosec Global. His research is focused on performance, optimizations and security. He obtained his MSc in Computer Science with a focus on Information Security from ETH Zurich in 2010, where he worked on elliptic curve cryptographic implementations and secure multi-party computation. He obtained his PhD in Information Systems at ETH Zurich in 2014. As part of his PhD research. he was in corporate research at SAP SE, working on some of the company's pioneering projects in Mobile, Internet of Things, UX, and embedded security. Basil's main areas of focus at InfoSec Global is the cryptographic core of our Agilesec Platform comprising of both classical and post-quantum cryptographic implementations, optimizations, sidechannel, and fault-attack countermeasures.

Juliana Sutanto is a Professor of Information Systems in the Management Science Department at the Lancaster University Management School. Her research focuses on artifact design and behavioral analysis in digital communications and interactions, and she subscribes to the design and behavioral sciences paradigms. She won INFORMS ISS Design Science Award 2013 for her empirical work on privacy-safe personalized offerings. Her research work has been published in leading information systems journals, such as MIS Quarterly, Information Systems Research, Journal of Management Information Systems and IEEE Transactions on Engineering Management among others.
