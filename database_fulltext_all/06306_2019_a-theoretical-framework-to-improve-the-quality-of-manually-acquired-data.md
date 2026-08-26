---
otero_id: 6306
otero_key: "RGZW9KTC"
title: "A theoretical framework to improve the quality of manually acquired data"
authors: "Tom Haegemans; Monique Snoeck; Wilfried Lemahieu"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.05.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A theoretical framework to improve the quality of manually acquired data

Tom Haegemans , Monique Snoeck, Wilfried Lemahieu

KU Leuven, Department of Decision Sciences and Information Management, Naamsestraat 69, B-3000 Leuven, Belgium

A R T I C L E I N F O

Keywords: Data quality Data entry Manually acquired data Information quality

## A B S T R A C T

We present a framework for organisations to prevent errors in data entry. It states that data entry errors can be prevented by a strong intention of data producers to enter data correctly and by a high task-technology <sup>fi</sup>t. Two empirical studies support the framework and demonstrate that a high task-technology <sup>fi</sup>t is relatively more important than the data producers’ intention. The framework re<sup>fi</sup>nes the theory of planned behaviour, and extends the explanatory domain of the task-technology <sup>fi</sup>t construct. The empirical evidence underlines the importance of the task-technology <sup>fi</sup>t construct, an often-neglected construct in information systems research

## 1. Introduction

Most of the data stored by organisations were once captured manually by human data producers [1]. Often, organisations have a good reason to still rely on manual data acquisition by humans instead of automatic procedures. Sometimes, automatisation of manual input procedures is simply impossible because the technology to replace these procedures is not yet developed. For example, consider the manual registration into an information system of observations made by psychiatrists while listening to their patients. At this moment, it is impossible to automate this procedure because no sensors currently exist that can make the same observations and register them automatically into an information system. Other times, it is too expensive to automate the manual input procedures. For instance, the complex business processes in <sup>fi</sup>nancial institutions resulting from a complex hierarchy of <sup>fi</sup>nancial products prove very costly to automate [2].

A signi<sup>fi</sup>cant (and well-known) problem with this manually ac quired data is that it is prone to errors. Examples of datasets reported to contain errors are <sup>fi</sup>nancial datasets [3], medical datasets [4–6], agri cultural datasets [7], inventory datasets [8] and criminal datasets [9]. When reported, the percentage of erroneous records ranges from 0 [10] to as high as 65% [8].

Even a single error in a dataset can have far-reaching negative consequences such as a<sup>f</sup>ecting statistical results, possibly leading to wrong decisions [11,12]. In addition, it is not hard to <sup>fi</sup>nd speci<sup>fi</sup>c si tuations where a data entry error caused serious issues. For example, in a <sup>fi</sup>nancial institution, a data entry error made by a clerk enabled a client to spend 2.1 million dollars without being noticed [13, par. 55]. In another case, a client of a <sup>fi</sup>nancial institution instead of a clerk, made an error. The client accidentally typed a wrong digit in an account number, causing the transfer of 100,000 dollars to an unknown person [14]. Also, the aviation sector is a<sup>f</sup>ected by data entry errors. Recently, the captain of an Airbus A330 mistakenly entered the wrong coordinates into the autopilot of a plane. Because the error remained unnoticed until after the plane took o<sup>f</sup>, the plane headed in the wrong direction and had to land at a di<sup>f</sup>erent airport [15]. In this same manner, some time ago, a typo in a computer terminal caused a major cloud service provider to go o<sup>fl</sup>ine [16].

These examples are illustrative of the importance of error prevention in manual data entry. This can be achieved by eliminating or mitigating their root causes. However, to the best of our knowledge, a theoretical framework that can help organisations identify root causes of errors in manually acquired data is missing from the literature.

In response, we propose and empirically evaluate the ‘Causes of Errors in Manually Acquired Data’ (CEMAD)-framework. The CEMAD framework is formulated at the level of an individual human data producer and states that two factors cause errors in manual data entry: a weak intention of the data producer to enter data correctly, and/or a low <sup>fi</sup>t between the technology, task and individual (task-technology <sup>fi</sup>t or TTF). The framework is grounded in empirical observations from an exploratory case study, and informed by the theory of planned behaviour and TTF model, which were combined to resolve the theoretical shortcomings explained in Section 2.2.

Both the theory of planned behaviour and TTF model are supported by a plethora of empirical <sup>fi</sup>ndings that could potentially justify the core hypotheses of the CEMAD framework and therefore would not require gathering additional empirical evidence. However, as will be explained in Section 3.2, additional empirical <sup>fi</sup>ndings are not only required to justify the CEMAD framework but such <sup>fi</sup>ndings would also be of interest to practitioners. For example, the CEMAD framework gives clear indications of possible data improvement actions (i.e. actions should improve the TTF and/or strengthen the data producers’ intention to enter data correctly). For practitioners, having such indications is useful, but for them, it is equally, if not more, important to know which kind of actions potentially have the largest impact on the actual behaviour. Therefore, additional empirical evidence was gathered by two experimental studies testing the core hypotheses of the CEMAD framework and examining the e<sup>f</sup>ect size of each of the framework's fac tors.

![](/api/attachments/RGZW9KTC/fulltext/images/7a8f3aa8e53e3b827fcc3e367d3858486c1803ca1bcc8a255adf077e1a66b01b.jpg)  
Fig. 1. The theory of planned behaviour [17].

The remainder of this manuscript is structured as follows. Section 2 introduces the two relevant theoretical frameworks: the theory of planned behaviour and the TTF model, and delineates their shortcomings in explaining errors in manually acquired data. Section 3 details the CEMAD framework and argues why its core hypotheses require additional empirical evidence. Section 4 provides empirical evidence resulting from a large-scale experiment for the hypotheses of the CEMAD framework. Section 5 demonstrates how the CEMAD framework can be applied in practice and provides additional empirical evidence for certain hypotheses of the CEMAD framework. Section 6 discusses the empirical results stemming from both the experiment and application. Section 7 delineates the practical implications of the framework. Section 8 concludes the research and lists opportunities for future research.

## 2. Theory development

## 2.1. Relevant theoretical models

In previous work [i.e. 3], we adopted a grounded theory approach to analyse the observations during an exploratory case study in a major Belgian <sup>fi</sup>nancial institution. During this study, we veri<sup>fi</sup>ed two home loan attributes using exhibits from the paper archive to <sup>fi</sup>nd errors, and conducted interviews and consulted the documentation of the home loan information system to identify the causes of the errors we found. We found that all identi<sup>fi</sup>ed errors could be best explained by a com bination of the theory of planned behaviour and TTF model.

## 2.1.1. The theory of planned behaviour

The theory of planned behaviour [17] is an established theory to explain human behaviour and is based on the theory of reasoned action. The theory (Fig. 1) states that the behaviour of an individual can be explained by how much actual control this individual has in order to perform the behaviour together with the intention that the individual has to exert the behaviour [18]. In its turn, the intention of the in dividual is determined by a combination of the attitude of the in dividual towards performing the behaviour, how the individual believes that others think about the behaviour and how much the individual perceives that he or she is in control of performing the behaviour [17]. Sometimes, the attitude construct is decomposed in an instrumental and experiential part [18, p. 82]. Instrumental attitude captures cognitive aspects of attitude like usefulness while experiential attitude captures a<sup>f</sup>ective dimensions like pleasantness.

The intention of individuals is closely related to their motivation: if an individual is motivated to perform a certain behaviour, s/he has a strong intention to perform the behaviour. In other words, the intention of an individual captures or ‘indexes’ his/her motivation [19, p. 2].

When applied in a data entry context, the theory of planned beha viour can be used to construct data quality improvement actions that target the psychosocial antecedents of intention [20]. For example, the instrumental attitude of data producers towards entering data correctly can be strengthened by providing these producers with information about why it is important to enter data correctly [20–22], or by providing them with monetary rewards. Their experiential attitude towards the behaviour of entering data correctly can become more positive by, for instance, making the information system more easy to use. The subjective norm of the data producers can become more positive if, for example, their peers state that they also enter data correctly and that they <sup>fi</sup>nd correctly entered data important. The perceived beha vioural control can be increased by, for example, making the data entry task less complex.

## 2.1.2. The task-technology fit model

The task-technology <sup>fi</sup>t (TTF) model, shown in Fig. 2, states that the performance of an individual in executing a task is determined by the ‘degree to which a technology assists an individual in performing his or her portfolio of tasks [23, p. 216] and by the behaviour [of the individual] of employing the technology in completing tasks’ [23, p. 218]. In other words, the performance of an individual in executing a task is determined by the TTF<sup>1</sup> and the utilisation of the technology [23]. In practice, this model is frequently used to explain how the errors of the output of an information system a<sup>f</sup>ect the performance of the task for which this output is used [see e.g. 25, p. 1831]. To the best of our knowledge, this model has not yet been applied in a data acquisition setting, while it could: the quality of data that a data producer entered can be considered as the performance (data quality) of this individual (data producer) in executing the (data entry) task. For example, in the context of manual data entry, a high TTF could mean that the structure of the data model (technology) <sup>fi</sup>ts the information structure of the real world (task) [26, p. 70], or that the design of the user interface (technology) reduces the short-term memory load of the data producers (individual abilities).

![](/api/attachments/RGZW9KTC/fulltext/images/f32bfc4281a77bcb58013764fbc3ec9a26db2bb66cfc6304f8bd803c10c83cb9.jpg)  
Fig. 2. A task-technology <sup>fi</sup>t (TTF) model [23].

![](/api/attachments/RGZW9KTC/fulltext/images/81e18bec16a95b3bb428c04c0e83f32a415432524584b00b7ebf6b50b04a9879.jpg)  
Fig. 3. The CEMAD (causes of errors in manually acquired data) framework. The core interactions of the framework are depicted in bold. The hypotheses underlying the core interactions will be tested in the remainder of the study

When the TTF construct is applied in the context of data entry, it is conceptually equal to the degree of actual behavioural control of the theory of planned behaviour. Indeed, when an information system (technology) <sup>fi</sup>ts the reality (task) and the individual abilities of the data producer, it o<sup>f</sup>ers the data producer the right opportunities and resources to enter data of high quality and thus provides him or her with a high degree of behavioural control.

## 2.2. Shortcomings of the theoretical models in explaining errors in manually acquired data

While both theories have their merits in clarifying the use of technology, they fall short when used with the aim of <sup>fi</sup>nding the root causes of errors in manually acquired data. To serve such a purpose, it is not only important that a theory is able to explain all or most of the errors in manually acquired data, but also that there is su<sup>fi</sup>cient in formation available about the antecedents of its core constructs. Information about the antecedents of factors that explain errors in manually acquired data is important as it can serve as a basis for concrete data quality improvement guidelines.

The theory of planned behaviour was able to explain all errors in the manually acquired data in the exploratory case study [3, p. 15:6]. However, the theory only delineates antecedents for one of its two core constructs: the individuals’ intention to perform a certain kind of behaviour. The theory does not contain antecedents for the actual behavioural control construct.

Yet, in a manual data entry context, the data producers’ resources could potentially have a signi<sup>fi</sup>cant impact on the correctness of the data which is even larger than that of their intention to enter data correctly. For example, in a recent replication of the theory of planned behaviour in a data entry context, we found that the statistical control variables related to actual behavioural control were more strongly correlated to errors in the entered data compared to the data producers intention [27]. As such, antecedents for the actual behavioural control construct would be of particular interest to organisations aiming to prevent errors in manually acquired data.

While each model has some shortcomings, they can easily be linked together as the TTF construct is a specialisation of the actual behavioural control construct, which are both conceptually equal in the case of manual data entry. Consequently, to explain errors in manually ac quired data, we propose to combine both models as follows: replace the actual behavioural control construct of the theory of planned behaviou with the TTF construct of the TTF model. In the remainder of this paper, the resulting model will be called the ‘Causes of Errors in Manually Acquired Data (CEMAD)-framework’. Compared to the theory of planned behaviour, the CEMAD framework is better able to explain errors in manually acquired data as the TTF construct speci<sup>fi</sup>es which resources individuals require to enter high quality data. By demonstrating the utility of the TTF construct to explain errors in the input of an information system, rather than to explain how errors in the output of an information system a<sup>f</sup>ect the performance of a task, we extend the explanatory domain of this construct.

## 3. The causes of errors in manually acquired data (CEMAD)- framework

## 3.1. Research model and hypotheses

The CEMAD framework, which is depicted in Fig. 3, is empirically grounded in the results of an exploratory case study [i.e. 3], and is informed by the TTF model and by the theory of planned behaviour. It posits that errors in manually acquired data can be explained by a low intention of the data producers to enter data correctly, by a poor TTF, or by a combination of those two factors. In this section, we will present the relevant constructs of both theories as part of the CEMAD framework, tailor the de<sup>fi</sup>nitions of these constructs to the manual data ac quisition context, and formulate hypotheses that are empirically veri<sup>fi</sup>able.

Errors in Manual Data Entry. An error in manual data entry is de<sup>fi</sup>ned as a situation where the data producer did not enter the correct registration for an attribute of a real-world object that he or she observed. These errors in manually entered data can be interpreted as the data producer having a low individual performance.

At the same time, this construct is related to data quality: an error in manual data entry results in a de<sup>fi</sup>ciency in the quality of this data [28, p. 89].

Task-Technology Fit and Antecedents of Task-Technology Fit. When tailored to manual data entry, TTF is de<sup>fi</sup>ned as ‘the degree to which a technology assists the individual [data producer] in performing his or her [manual data acquisition] task’ [23, p. 216]. A manual data acquisition task entails that the individual exerts a certain behaviour that turns an observation of an attribute of a real-world object into a re gistration in a database.

User Intention and Antecedents of User Intention. In the CEMAD framework, user intention is de<sup>fi</sup>ned as the ‘readiness’ of data producers to enter data without errors [18, p. 43]. This de<sup>fi</sup>nition is in accordance with how intention is de<sup>fi</sup>ned in the theory of planned behaviour [17].

The Impact of User Intention and Task-Technology Fit on Errors in Manually Acquired Data. Errors in manually acquired data are caused by a low intention of the data producers to enter high quality data and/or a low degree of TTF. A stronger intention of the users to produce high quality data or an increase in the degree of TTF will lead to fewer errors. These propositions are presented in Hypotheses 1 and 2.

Hypothesis 1. An increase in the intention of the data producers to enter correct data will cause an increase in the number of correctly entered registrations.

Hypothesis 2. An increase in the <sup>fi</sup>t between the data entry task, technology and data producers will cause an increase in the number of correctly entered registrations.

At the same time, we expect an interaction e<sup>f</sup>ect between the degree of TTF and the intention of the data producers to enter high quality data. For example, the intention of the data producers towards entering high quality data can be reinforced by increasing the degree of TTF as it might a<sup>f</sup>ect the perceived behavioural control and experiential attitude of these data producers [20, p. 1885]. This premise is stated in Hypothesis 3.

Hypothesis 3. An increase in the <sup>fi</sup>t between the data entry task, technology and data producers strengthens the e<sup>f</sup>ect of increasing the data producers’ intention, thus increases the number of correctly entered registrations.

## 3.2. The need for additional empirical evidence

Both theory of planned behaviour and TTF model have been tested multiple times in several empirical studies resulting in a multitude of evidence supporting their underlying hypotheses (for meta reviews see e.g. [29–32]). Yet, this plethora of empirical evidence is not su<sup>fi</sup>cient to justify the e<sup>f</sup>ects of the CEMAD framework's constructs. In what follows, we explain per construct, why additional empirical evidence is required.

## 3.2.1. Task-technology fit

The claims concerning the TTF construct could have been supported by empirical evidence stemming from studies empirically investigating the TTF model (TTF construct), or theory of planned behaviour (actual behavioural control). However, the evidence from these studies is not su<sup>fi</sup>cient for the following reasons.

On the one hand, existing TTF studies always employ the TTF construct to explain how errors in the output of an information system a<sup>f</sup>ect the performance of a task for which this output is used. In contrast, in the CEMAD framework, TTF is expected to explain errors in the input of an information system. This signi<sup>fi</sup>cant di<sup>f</sup>erence in context requires additional empirical evidence and an adaptation on how this construct should be measured.

In its original context, the degree of TTF has mostly been measured by employing user evaluations. Previous research has indicated this to be an e<sup>f</sup>ective measurement technique under the assumption that ‘users will give evaluations based on the extent to which systems meet their needs and abilities’ [25, p. 1830, emphasis added]. However, in the case of manual data acquisition, the increase in performance, i.e. the reduction of the frequency or size of errors in manually entered data, will not always directly bene<sup>fi</sup>t the user. For example, during the interviews with the data producers, we were given the impression that these employees were positive about the technology to enter home loans, while during the observation of a data entry task, we witnessed the same technology as having a poor <sup>fi</sup>t with the task of manually entering data. Therefore, in this new context, the TTF construct should be assessed objectively rather than by user evaluations.

On the other hand, evidence from studies applying the theory of planned behaviour does also not su<sup>fi</sup>ce to justify claims concerning the TTF construct. At <sup>fi</sup>rst sight, this is surprising as, in the context of manual data entry, the TTF construct is conceptually equal to the actual behavioural control construct of the theory of planned behaviour. Yet, the interaction between actual behavioural control and behaviour is almost never tested in empirical applications of the theory. For example, in a recent systematic literature review of applications of the theory of planned behaviour in information system research, none of the identi<sup>fi</sup>ed studies tested this hypothesis [27]. This can be explained by the fact that the theory of planned behaviour originates from the psychological research domain, which is primarily interested in the perceptions of individuals about behavioural control [17, p. 183].

## 3.2.2. Intention

In contrast with the role of TTF in manual data acquisition, the e<sup>f</sup>ect of intention on the behaviour of individuals can already be reasonably well justi<sup>fi</sup>ed by the existing empirical evidence supporting the theory of planned behaviour. For example, meta-reviews of the theory of planned behaviour indicate that many studies reported a correlation between the intention of individuals and their behaviour [e.g. 29, p. 489]. However, because the individuals’ intention is rarely tested in combination with their degree of actual behavioural control, there are at least two interesting aspects about the e<sup>f</sup>ect of the data producers intention on manually entered data that remain unclear: (1) the magnitude of the interaction between intention and TTF on the amount of errors and (2) the relative importance of both core constructs. Therefore, in the next sections, we empirically test the impact of intention versus TTF on the correctness of a data entry task.

## 4. Study 1: Empirically testing the CEMAD framework using an experimental approach

In this part, we empirically test the hypotheses underlying the core interactions of the CEMAD framework presented in Fig. 3 by means of an experiment on Amazon Mechanical Turk (MTurk).

MTurk is a platform to recruit human workers to perform Human Intelligence Tasks (HITs) in return for a small monetary reward. Typically, a HIT is a task that can be easily executed by humans, but is di<sup>fi</sup>cult (if not impossible) to be executed by computers [33,34]. Many of the HITs on MTurk require little time and e<sup>f</sup>ort [33, p. 454] and reward human workers an amount between 0.01\$ and 1\$ [35]. This means that MTurk enables researchers to engage a large sample of in dividuals to execute a simple task for a small amount of money. Not surprisingly, MTurk has been widely used to collect research data in a variety of scienti<sup>fi</sup>c disciplines.

Because MTurk is often used to collect research data, the validity and reliability of using MTurk as a research tool are frequently investigated. In such investigations, the MTurk workers are compared against other populations, and the platform is used to replicate other in<sup>fl</sup>uential experiments. Regarding the population of MTurk, samples of MTurk workers are found to be a better representation of the US population than samples of other panels or student samples and thus have the potential to generalise to a more varied population than traditional methods [33]. The replication studies conducted on MTurk show that results of other experiments replicate well [36,37], if the experimental design is simple [38]. These investigations demonstrate that MTurk is a valid research environment re searchers can use to conduct experiments [39].

Despite its many advantages, research has pointed to several con cerns that need to be considered when using the MTurk to collect research data. One frequently mentioned concern is that the environment of the participants cannot be controlled in the same way actual laboratory environments can be controlled. For example, MTurk workers might have installed a di<sup>f</sup>erent browser, disabled JavaScript, experience technical problems, or experience distractions [33]. As detailed in the next section, care has been taken to design the experiment to minimise the potential e<sup>f</sup>ect of such elements.

MTurk has one characteristic that makes this platform particularly well-suited to empirically test the core interactions of the CEMAD fra mework: almost all of the HITs found on the platform can be classi<sup>fi</sup>ed as data entry tasks. For example, HITs range from transcribing text, to classifying images, translating small texts, <sup>fi</sup>lling in academic ques tionnaires, identifying objects in images, <sup>fi</sup>nding relevant information, processing natural language and transcribing audio [33,35,40]. Thi characteristic bene<sup>fi</sup>ts the validity of our study in two signi<sup>fi</sup>cant ways. First, by using MTurk, we can conduct an experiment that can be dis guised as yet another data entry task without telling the subjects that they are participating in a data entry experiment. As such, the experiment will not have any ‘demand characteristics’ that could make the subjects, for example, behave in a more favourable way [41] such as observed in the Hawthorne studies [42]. Second, because many other HITs on MTurk can be classi<sup>fi</sup>ed as data entry tasks, workers are likely to be experienced in performing such tasks. This experience is com parable to the experience of workers in organisations who perform data entry tasks as part of their job. In other words, the context of an experiment on MTurk is comparable to the organisational context for which the CEMAD framework was designed.

## 4.1. Method

## 4.1.1. Design and sample

The core interactions of the CEMAD framework were tested using a two-by-two factorial experimental design. In such a design, two separate factors are tested by varying each factor by two levels. In our case, we tested the factors ‘intention’ and ‘TTF’ by varying the level of these factors from low to high. Table 1 displays the design of the experiment which allows for testing the individual treatments and the interaction between intention and TTF [43].

In total, 2575 MTurk workers accepted the HIT containing the experiment. For every worker who accepted the HIT, we logged their worker ID and time of acceptance. Of these 2575 logged workers, 2407 <sup>fi</sup>nished the HIT and submitted their work, resulting in an attrition rate of 6.52%.<sup>2</sup> One hundred and eighty-three (183) workers appeared in the log <sup>fi</sup>le more than once, which could indicate that these workers refreshed their page because of technical di<sup>fi</sup>culties. These workers were excluded, and 2224 workers remained. Some of the remaining 2224 workers participated in previous pilot runs of the experiment and

## Table 1

Design of the two-by-two factorial laboratory experiment. The rows represent the experimental groups and the columns represent the course of action. Letter R in the <sup>fi</sup>rst column indicates that the subjects were randomly assigned to an experimental group. Letter X in the second column indicates that the subjects received a certain treatment. The treatments were designed to vary each factor by two levels corresponding to the two by two factorial design. Letter O in the last column stands for the observation of the outcomes of the experiment.

<table><tr><td>R</td><td> $X_{\text{LowInt, LowTTF}}$ </td><td>O</td></tr><tr><td>R</td><td> $X_{\text{HighInt, LowTTF}}$ </td><td>O</td></tr><tr><td>R</td><td> $X_{\text{LowInt, HighTTF}}$ </td><td>O</td></tr><tr><td>R</td><td> $X_{\text{HighInt, HighTTF}}$ </td><td>O</td></tr></table>

could be biased if they happened to be assigned to a di<sup>f</sup>erent experi mental group in the previous run. For example, if a worker was assigned in the <sup>fi</sup>rst run to the intention group, and in the actual run to the control group, the worker's intention might be higher than a worker who did not yet participate. To prevent such a bias, we removed the 199 workers who participated in a previous run of the experiment. Finally, because the initial plan was to sample 2000 workers, we picked the <sup>fi</sup>rst 2000 workers of the remaining 2025.<sup>3</sup>

## 4.1.2. Procedure and treatment

The experiment was disguised as a normal data entry task using a HIT on MTurk with the characteristics in Table 2.

On MTurk, before a potential worker executes a HIT, s/he can preview the task before actually accepting the HIT. In our case previewing the HIT could potentially lead to a bias. For example, a worker with a low intention to execute the HIT correctly might decide not to accept the HIT while a worker with a high intention to enter the data correctly could be more inclined to start the HIT, leading to a problem of self-selection. To this end, we disabled the HIT preview feature using JavaScript.

If a worker accepted the HIT, s/he was assigned to an experimental group in a round robin fashion based on the experimental group of the previous worker.

The actual data entry task was a request to copy a string of characters from a picture and was designed to strike a balance between clarity and di<sup>fi</sup>culty. Clarity was ensured by providing simple instructions and by avoiding characters that could be misinterpreted (e.g. O vs. 0 or I vs. l vs. 1). The di<sup>fi</sup>culty of the data entry task needed to be ensured so it would be easier to observe an e<sup>f</sup>ect of the factors under investigation. Therefore, we created a string of 70 characters consisting of ‘A’, ‘C’, ‘G’ and ‘T’, and, to avoid copy/pasting, we presented this string using an image.<sup>4</sup> The data entry task was presented to the control group using the web page shown in Fig. 4.

For each treatment group, the data entry task was modi<sup>fi</sup>ed to cause an increase in the intention construct, the TTF construct or both constructs combined.

To strengthen the intention of the subjects to enter data correctly, we tried to convince them of the importance of entering the data correctly. We told them that correct data entry would bene<sup>fi</sup>t cancer research<sup>5</sup> and explicitly stated that the string of characters is a DNA sequence (which is commonly represented by the characters A , C , G and ‘T’ and explains why we chose those characters<sup>6</sup>). In most realworld settings, data producers are paid a <sup>fi</sup>xed wage, and their income does not depend on their performance. So, to avoid the intention being in<sup>fl</sup>uenced by monetary considerations, we explicitly stated that the HIT would be automatically approved after one minute and that the worker would receive his/her reward in any case. The resulting HIT, which was presented to the intention group, is shown in Fig. 5.

Table 2  
The parameters of the MTurk HIT.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Title</td><td>‘Enter the characters as shown in the image’</td></tr><tr><td>Description</td><td>‘You will be asked to copy approximately 70 characters.’</td></tr><tr><td>Key words</td><td>‘data collection’ and ‘data entry’</td></tr><tr><td>Max. completion time</td><td>30 min</td></tr><tr><td>Worker characteristics</td><td>Not participated in previous runs AND from UK OR US</td></tr><tr><td>Hide HIT if worker does not match the inclusion criteria?</td><td>Yes</td></tr><tr><td>Payment</td><td>0.22$</td></tr><tr><td>Bonus</td><td>No</td></tr></table>

To increase the TTF, we made the data entry task less di<sup>fi</sup>cult by grouping the characters in groups of 5 characters, separated by dashes. The resulting HIT, which was presented to the TTF group, is shown in Fig. 6.

The group that received both treatments was presented the page shown in Fig. 7.

## 4.1.3. Analysis

The individual observations were analysed using a logistic regression model. Logistic regression is an established way to analyse data from a two by two factorial experiment [45] and only assumes that the residuals follow the binomial distribution [46]. In our case, the binomial assumption is robust because the observations are randomly sampled [46].

When the logistic regression model only contains binary regressors, as in this study, its <sup>fi</sup>t can be evaluated by comparing the model against the saturated model using the likelihood ratio test [47]. If the likelihood ratio test indicates there is likely no di<sup>f</sup>erence between the residuals of the tested model and the saturated model (the perfect model), the tested model is likely to have a good <sup>fi</sup>t. The likelihood ratio test comparing the <sup>fi</sup>tted model to the saturated model returned $\chi ^ { 2 } = 1 9 5 3 . 4 ,$ df =−1996, p < 0.748. This means that the null hypothesis cannot be rejected and that the <sup>fi</sup>tted model is likely to be similar to the perfect model, indicating that the logistic regression model has a good <sup>fi</sup>t.

## 4.2. Results

The summary of the individual responses is presented in a threedimensional contingency table in Table 3. The logistic regression model to further analyse the individual responses is presented in Eq. (1). The results of the regression analysis are shown in Table 4. The probabilities of entering the data correctly (marginal e<sup>f</sup>ects), derived from the logistic regression model are summarised in Fig. 8.

![](/api/attachments/RGZW9KTC/fulltext/images/07749ba4952f7474740ac18bd33861797621dfbdb3af845423914811d0846c95.jpg)  
Fig. 4. The web page shown to the subjects in the control group.

![](/api/attachments/RGZW9KTC/fulltext/images/9473ab98114050c8d3354a32ade1cf63b3ff06a944e884974004a32e213eb93a.jpg)  
Fig. 5. The web page shown to the subjects in the intention group.

![](/api/attachments/RGZW9KTC/fulltext/images/de6b8b24f51ac697c54626e6d3bcb9027709abbb70cfbd09caa6fccb7cd64a1c.jpg)  
Fig. 6. The web page shown to the subjects in the TTF group.

![](/api/attachments/RGZW9KTC/fulltext/images/517c81c41c9d3fbbaa1a2e33aa13be571e60f7e1166ad9c6f5139758b83666fd.jpg)  
Fig. 7. The web page shown to the subjects in both treatments group.

The three-dimensional contingency table of the individual responses.

<table><tr><td colspan="2">Factor</td><td colspan="2">Outcome</td><td rowspan="2">Total</td></tr><tr><td>Intention</td><td>TTF</td><td>Correct</td><td>Not Correct</td></tr><tr><td rowspan="2">Low</td><td>Low</td><td>294</td><td>207</td><td>501</td></tr><tr><td>High</td><td>442</td><td>69</td><td>511</td></tr><tr><td rowspan="2">High</td><td>Low</td><td>353</td><td>117</td><td>470</td></tr><tr><td>High</td><td>465</td><td>53</td><td>518</td></tr><tr><td>Total</td><td></td><td>1554</td><td>446</td><td>2000</td></tr></table>

$$
\text { IsCorrect } = \beta_ {0} + \beta_ {1} \text { Intention } + \beta_ {2} \text { TTF } + \beta_ {3} (\text { Intention } \times \text { TTF })\tag{1}
$$

The results of this study provide support for all identi<sup>fi</sup>ed hypotheses, except for the hypothesis concerning the interaction e<sup>f</sup>ect between intention and TTF.

The hypothesis regarding the e<sup>f</sup>ect of the data producers’ intention is supported at the 1% signi<sup>fi</sup>cance level. The coe<sup>fi</sup>cient of intention in the logistic regression model is positive and has a p value of less than 0.001 (see Table 4). According to the same model, as summarised in Fig. 8, an increase in intention caused the data producers to enter the data more correctly: the percentage of correctly entered data rose from 58.68% to 75.11%. This increase of 16.42 percentage points or 27.99% is highly signi<sup>fi</sup>cant $( p < 0 . 0 0 1 )$ ).

The hypothesis concerning the e<sup>f</sup>ect of TTF is also supported at the 1% signi<sup>fi</sup>cance level. In the results of the logistic regression model, we see that the coe<sup>fi</sup>cient of this factor is positive with a p value of less than 0.001. The summary of the marginal e<sup>f</sup>ects (Fig. 8) shows that after improving the TTF, the percentage of correctly entered data rose from 58.68% to 86.50%. This increase of approximately 47.40% is highly signi<sup>fi</sup>cant $( p < 0 . 0 0 1 )$ .

The hypothesis about the interaction of intention and TTF is par tially supported. In our study, we have not found evidence that an increase in TTF strengthens the e<sup>f</sup>ect of increasing the data producers’ intention. This means that the whole is not greater than the sum of the parts. The coe<sup>fi</sup>cient of the interaction term in the logistic regression

## Table 4

The results of the logistic regression analysis. The estimates are presented on the log-odds scale and are presented with their standard error and p value. Legend: signi<sup>fi</sup>cant at the 10%\*, 5%\*\* and 1%\*\*\* signi<sup>fi</sup>cance level.

<table><tr><td>Coefficient</td><td>Estimate</td><td>Std. error</td><td>p Value</td></tr><tr><td>Intercept</td><td>0.35086</td><td>0.09073</td><td>&lt; 0.001***</td></tr><tr><td>Intention</td><td>0.75343</td><td>0.14004</td><td>&lt; 0.001***</td></tr><tr><td>TTF</td><td>1.50634</td><td>0.15807</td><td>&lt; 0.001***</td></tr><tr><td>Intention × TTF</td><td>-0.43889</td><td>0.23955</td><td>0.067*</td></tr></table>

model is negative and marginally signi<sup>fi</sup>cant. Yet, we did <sup>fi</sup>nd evidence that the percentage of correctly entered registrations would increase if both treatments were combined. The di<sup>f</sup>erence in the percentage of correctly entered data between the control group and the group that received both treatments is 31.09 percentage points or 52.97% and is highly signi<sup>fi</sup>cant $( p \textless 0 . 0 0 1 )$ ). The di<sup>f</sup>erence between the groups that received a single treatment and the group that received both treatments is 14.66 percentage points $( p < 0 . 0 0 1 )$ or 19.52% for the group that received the intention treatment and 3.27 percentage points $( p = 0 . 1 0 4 )$ or 3.78% for the group that received the TTF treatment.

Interestingly, these results show that the e<sup>f</sup>ect of an increase in TTF on reducing the errors in manually acquired data is more important than the e<sup>f</sup>ect of increasing the data producers’ intention. First, as shown by the results in Table 4, the coe<sup>fi</sup>cient of TTF is twice as large as the coe<sup>fi</sup>cient of intention (log odds of 0.75 vs. 1.51). Second, as indicated by the marginal e<sup>f</sup>ects analysis in Fig. 8, the di<sup>f</sup>erence between the group that received both treatments and the group that received the TTF treatment is much smaller (and only marginally signi<sup>fi</sup>cant, $\begin{array} { r } { p = 0 . 1 0 4 ) } \end{array}$ than the di<sup>f</sup>erence between the same group and the group that received the intention treatment (strongly signi<sup>fi</sup>cant $p \ : < \ : 0 . 0 0 1 )$ ).

## 5. Study 2: applying the framework in a major Belgian <sup>fi</sup>nancial institution

The CEMAD framework was applied in a major <sup>fi</sup>nancial institution to decrease the amount of errors in home loan data and more speci<sup>fi</sup>- cally, the errors in the value of assets that were used as collateral for these home loans. It is crucial that the value of the collateral for a home loan is correct because these home loans are sometimes used as collateral for mortgage-backed securities. The <sup>fi</sup>nancial crisis of 2007 demonstrated that the collateral for home loans that serve as collateral for mortgage-backed securities should be correct [48].

The value of the collateral for home loans is manually entered by home loan advisers who are instructed to enter this data without error. The <sup>fi</sup>nancial institution employs two groups of home loan advisers: senior and junior home loan advisers. The di<sup>f</sup>erence between the two is that senior home loan advisers are more experienced and are asked to disseminate knowledge and educate junior home loan advisers. In this work, we study data entry by junior home loan advisers.

While we applied the framework in the <sup>fi</sup>nancial institution, we were given a minimum, yet highly appreciated amount of resources to study the framework's e<sup>f</sup>ectiveness in practice. However, due to the limited set of resources, we encountered several problems leading to important limitations of the study. For example, under perfect cir cumstances, to test the e<sup>f</sup>ect of intention on the amount of errors in the entered data, one would split the population into two groups: a treatment group and a control group, and only distribute the treatment to the treatment group. This way, one can be more con<sup>fi</sup>dent that the effect of an increased intention was due to the intention treatment and not caused by an external factor. However, as will be explained, because the <sup>fi</sup>nancial institution was strongly determined to prevent errors from happening, they made us distribute an additional intention treatment to all home loan advisers, and not only to a treatment group. As a consequence, the evidence of this study possesses lower degrees of internal validity compared to the MTurk study.

![](/api/attachments/RGZW9KTC/fulltext/images/c069343903c4cb8ef0e4d553c21b94bbb1a960fa8b852d9950c9368902b91223.jpg)  
Fig. 8. The marginal results per experimental group and the di<sup>f</sup>erences between the experimental groups including p values, standard errors between brackets and relative di<sup>f</sup>erences.

## 5.1. Method

## 5.1.1. Design

The application of the CEMAD framework was investigated using a study containing two components: an experimental one and an observational one.

The experimental component is depicted in Fig. 5 and provides evidence concerning the e<sup>f</sup>ect of intention (Hypothesis 1). The ex periment consisted of two behavioural interventions designed in co operation with the company under study. The goal of these interven tions was to strengthen the intention of home loan advisers to ente data correctly.

The <sup>fi</sup>rst behavioural intervention was targeted only at half of the junior advisers and was delivered via an email containing a link to a web page showing the treatment. Because participating in the <sup>fi</sup>rst in tervention was voluntarily, the assignment of subjects to this group, called the double treatment group, was not random. As such, the experimental set-up to test this behavioural intervention is equal to a nonequivalent group design.

The second behavioural intervention was directed to all junior ad visers because the company wanted to take immediate action to reduce the amount of errors in home loan data. In terms of experimental design, the approach to test the second treatment shows characteristics

## Table 5

The design of the <sup>fi</sup>eld experiment in research design notation. Half of the ju nior home loan advisers were randomly picked and invited via email to watch a behavioural intervention $( X _ { \mathrm { e m a i l } } ) .$ . Some junior advisers accepted the invitation while others did not. This caused the groups to be non-equivalent (the letter N stands for non-equivalent groups). Next, every senior home loan adviser was instructed to communicate to the junior advisers (i.e. their peers) that correct data entry is essential. This communication is the second behavioural inter vention and was delivered to every junior adviser. Finally, we used the digital archive to check each junior adviser's record for whether s/he entered a home loan correctly before $( O _ { 1 } )$ and after $\left( O _ { 2 } \right)$ the interventions.

<table><tr><td>N</td><td> $O_1$ </td><td> $X_{\text{email}}$ </td><td> $X_{\text{peers}}$ </td><td> $O_2$ </td></tr><tr><td>N</td><td> $O_1$ </td><td></td><td> $X_{\text{peers}}$ </td><td> $O_2$ </td></tr></table>

similar to a single group pre- and post-test design.

After the interventions were distributed, we checked the value of the collateral of two home loans for each junior home loan adviser: one that was registered before the interventions were distributed (O ) and one after the interventions were distributed (O ). This was possible because, for each asset that serves as collateral for a home loan, the home loan advisers are instructed to scan in an exhibit proving its value (e.g. sales agreement) and upload it to a digital repository. We used these exhibits to verify the value of the asset registered in the database.

In the observational component, we gathered evidence related to the TTF hypothesis. During previous studies at the same <sup>fi</sup>nancial institution [27], we found that the sales agreement of the collateral for some home loans included the value of movable goods. If this value is mentioned on the sales agreement, the advisers should deduct this from the total amount because it is not possible to use movables as collateral for a home loan. In these cases, the task of entering the data correctly becomes more di<sup>fi</sup>cult and the technology does not provide help. In addition, the individual might not know which procedure s/he should follow while executing the task. Based on these considerations, whether or not the home loan includes movables can be used as a proxy to measure TTF: when such a situation occurs, the TTF is lower than usual. The TTF factor was investigated using a behavioural study because the <sup>fi</sup>nancial institution did not allow us to make changes to the task or information system. The key downside of an observational approach compared to an experimental one is that an observational approach does not allow us to make causal inferences.

## 5.1.2. Sample

To study the application of the CEMAD framework in the <sup>fi</sup>nancial institution, we sampled two types of entities: home loans and junior home loan advisers.

The selection of home loans was made with regard to the TTF factor. As previously explained, the TTF can vary across the sample because some home loans might be more di<sup>fi</sup>cult to enter than others. Here, the task becomes more complex without the technology supporting this complexity, causing the TTF between two home loans to be di<sup>f</sup>erent. To control for the di<sup>f</sup>erence in TTF between home loans, we ensured that the selected home loans were either (1) equally di<sup>fi</sup>cult to register, or (2) that they contained an objectively observable characteristic that indicated their registration di<sup>fi</sup>culty. To ensure that the home loans without an objectively observable di<sup>f</sup>erence in di<sup>fi</sup>culty would be equally hard to enter, we only selected home loans of the most easy sort (i.e. home loans to acquire a property). As previously noted, we noticed that for some home loans the di<sup>f</sup>erence in di<sup>fi</sup>culty was objectively observable (i.e. the sales agreement of the collateral sometimes con tained movable goods). This objectively observable entering di<sup>f</sup>erence was used as a proxy to test the e<sup>f</sup>ect of TTF.

We investigated junior home loan advisers and not senior advisers because the seniors were already expected to have a strong intention to enter home loans correctly. For example, the senior advisers attend a seminar each year where they are informed about the importance of entering home loans correctly. Knowing why it is important to enter data correctly strengthens the attitude of data producers in a positive way and thus increases their intention to enter correct data [22]. From the total population of approximately 750 home loan advisers, 564 are junior home loan advisers. Of these 564 junior advisers, we selected 406 junior advisers who registered a home loan before and after the interventions. Of these junior advisers who entered home loans, 202 received an email with a link to a questionnaire containing the behavioural intervention video and 110 of them <sup>fi</sup>lled in the questionnaire and watched the behavioural intervention video, leading to a response rate of 54.46%. These 110 junior advisers who watched the video were assigned to the ‘two treatments’-group. The 296 remaining advisers who did not watch the video were assigned to the single treatment group.

## 5.1.3. Procedure and treatments

The junior home loan advisers received one or two behavioural treatments in the form of a behavioural intervention, determined by the experimental group to which they belonged. The two interventions di<sup>f</sup>er in the way they were delivered to the junior home loan advisers. The <sup>fi</sup>rst intervention was delivered via email and the second was delivered via their peers. Both of the interventions were designed to strengthen the intention of the data producers by targeting their instrumental attitude. The advisers in the ‘two treatments’-group received both behavioural interventions, and those in the single treatment group only received the behavioural intervention via their peers.

Intervention 1: Knowledge Dissemination via Email. The <sup>fi</sup>rst intervention was delivered via email only to the ‘two treatments’-group. Half of the junior home loan advisers received an email containing a link to a questionnaire containing three components. The <sup>fi</sup>rst component contained measures regarding their current behavioural beliefs and inten tion about entering data correctly. These results were analysed in another study [27] and revealed that 31% of the data producers had a poor intention to enter data correctly. The second component, which is analysed in this study, contained the actual behavioural intervention video and a question to check whether the subjects actually watched and understood the behavioural intervention video. All the respondents answered this question correctly. The third component, which was also analysed in another study [22], contained measures about the e<sup>f</sup>ect of the behavioural intervention video on the data producers’ intention, instrumental attitude, experiential attitude, subjective norm and per ceived behavioural control. The results showed that the behavioural intervention video increased the intention of the data producers to enter data correctly and that this increase could be explained by an increase in their instrumental attitude [22]. The full questionnaire and the videos are available upon request from the authors.

The behavioural intervention video, or the second component of the questionnaire, contained information on why it is important to enter the value of collateral for home loans correctly. That is, home loans are often used as collateral for mortgage-backed securities, which are a relatively cheap way for a <sup>fi</sup>nancial institution to raise extra capital. Because errors in this data were partly responsible for the <sup>fi</sup>nancial crisis of 2007 [48], the Belgian national bank regularly checks whether the registrations are correct. If the national bank <sup>fi</sup>nds too many errors, the <sup>fi</sup>nancial institution is no longer allowed to sell mortgage-backed securities and has to raise capital through other, more expensive

mechanisms.

All the components of the survey were constructed in close cooperation with the home loan product manager and were pre-tested in a local branch by several cognitive interviews with home loan advisers. The components were presented in Dutch, which is the mother tongue of the respondents. In addition, the video was subtitled in Dutch to ensure that every respondent would be able to receive its message, even when his/her audio was turned o<sup>f</sup>.

Intervention 2: Knowledge Dissemination via Peers. The second inter vention was delivered to all junior home loan advisers using the senior home loan advisers (i.e. their peers). A week after the questionnaire containing the <sup>fi</sup>rst behavioural intervention closed, the senior advisers were invited to a seminar. During this seminar, the home loan product manager gave a presentation containing two parts. First, she explained why it is important that the value of the collateral for the home loans be entered correctly by using the same arguments that were given in the video of the <sup>fi</sup>rst intervention. Next, she stressed that the audience of the presentation, the senior home loan advisers, should make sure this knowledge is disseminated to the junior advisers and that they could do this by showing another movie made available on the knowledge base. The presentation and the second movie are available upon request from the authors.

## 5.1.4. Analysis

The data of the <sup>fi</sup>eld experiment, containing observations of two home loan registrations per respondent (812 observations in total), was analysed using a logistic mixed regression model. A mixed regression model is well-suited to support the hierarchical data structure resulting from the study's design.

At the lowest level, the data re<sup>fl</sup>ects characteristics about the home loans and at the highest level, the data re<sup>fl</sup>ects characteristics of the home loan advisers. In terms of <sup>fi</sup>xed and random e<sup>f</sup>ects, the identi<sup>fi</sup> cation number of the advisers was modelled as a random e<sup>f</sup>ect. This random e<sup>f</sup>ect introduces a separate regression line per adviser and clusters the observations so each cluster contains the observations of one home loan adviser. This results in 406 clusters (i.e. junior advisers) and two observations (i.e. home loans) per cluster. The <sup>fi</sup>xed e<sup>f</sup>ects component contains variables to model characteristics about the home loans and home loan advisers.

The <sup>fi</sup>t of a mixed logistic regression model can be assessed by goodness-of-<sup>fi</sup>t tests such as those proposed by Evans and Hosmer [49], Sturdivant and Hosmer [50] and Perera et al. [51]. However, the reliability of these goodness-of-<sup>fi</sup>t tests is not investigated in cases where there is a signi<sup>fi</sup>cant number of clusters and the number of observations per cluster is low, such as in our analysis. Therefore, as an alternative, we assessed the goodness-of-<sup>fi</sup>t by investigating how well the model was able to predict the outcomes of the current dataset. To this end, we calculated the c-statistic, which is equivalent to the area under the ROC curve. The c-statistic is 0.9541 and indicates that the model <sup>fi</sup>ts the data well.

## 5.2. Results

The result of the logistic mixed e<sup>f</sup>ects regression model is presented in Table 6. The regression model contains coe<sup>fi</sup>cients to di<sup>f</sup>erentiate between the treatment and single treatment group, to make a distinction between the home loans registered before the treatment and after the treatment, and to separate home loans containing movables from those without.

Three coe<sup>fi</sup>cients are of particular interest. The coe<sup>fi</sup>cient of the interaction term (Adviser.InTreatmentGroup × Loan.RegAfterTreatment) indicates the gains of the double treatment group, relative to the single treatment group and captures the e<sup>f</sup>ect of the <sup>fi</sup>rst behavioural intervention, directed at the double treatment group. Such an interaction term is often used to analyse observations resulting from a nonequivalent group design, which is then called a di<sup>f</sup>erence-in-di<sup>f</sup>erence analysis [52]. The coe<sup>fi</sup>cient of Loan.RegAfterTreatment represents the e<sup>f</sup>ect of the second behavioural intervention directed to all junior home loan advisers. The coe<sup>fi</sup>cient of Loan.HasMovables reveals the (noncausal) e<sup>f</sup>ect of the home loan containing movables on the behaviour of the junior home loan advisers and is, as explained, a proxy for TTF.

The <sup>fi</sup>xed e<sup>f</sup>ects of the mixed e<sup>f</sup>ects logistic regression analysis (dependent variable is Loan.IsCorrect). The identi<sup>fi</sup>cation number of the home loan advise is included as a random e<sup>f</sup>ect. The estimates are presented on the log-odd scale and are presented with their standard error and p value. Legend: sig ni<sup>fi</sup>cant at the 10%\*, 5%\*\* or 1%\*\*\* signi<sup>fi</sup>cance level.

<table><tr><td>Coefficient</td><td>Estimate</td><td>Std. Error</td><td>p Value</td></tr><tr><td>Intercept</td><td>2.437469</td><td>0.2974417</td><td>&lt; 0.001***</td></tr><tr><td>Adviser.InTreatmentGroup</td><td>-0.2246529</td><td>0.3720603</td><td>0.546</td></tr><tr><td>Loan.RegAfterTreatment</td><td>0.5002607</td><td>0.287138</td><td>0.081*</td></tr><tr><td>Adviser.InTreatmentGroup × Loan.RegAfterTreatment</td><td>0.1823616</td><td>0.5258868</td><td>0.729</td></tr><tr><td>Loan.HasMovables</td><td>-3.496642</td><td>0.4617241</td><td>&lt; 0.001***</td></tr></table>

The regression model was further studied by a marginal e<sup>f</sup>ects analysis (Fig. 9 and 10), and the di<sup>f</sup>erence-in-di<sup>f</sup>erence analysis is graphically presented in Fig. 11.

The results of these analyses provide evidence for the hypotheses concerning intention and TTF. Because we were not given any resources to change aspects of TTF (e.g. increasing the usability of the information system), the design of the study did not allow us to test the hy pothesis concerning the interaction between intention and TTF.

The hypothesis about the intention of the data producers (Hypothesis 1) is weakly supported, and its evidence is mixed. On the one hand, the positive coe<sup>fi</sup>cient of the Loan.RegAfterTreatment parameter indicates that, all other factors zero, the behavioural intervention presented at the seminar had on average a positive e<sup>f</sup>ect on correctly entering home loans. This <sup>fi</sup>nding is marginally signi<sup>fi</sup>cant (p = 0.081) and provides weak support for Hypothesis 1. On the other hand, the interaction term indicating the gains of the double treatment group, relative to the single treatment group is small and not signi<sup>fi</sup>cant. Likewise, the marginal e<sup>f</sup>ects analyses in Fig. 11 shows that for each level of Loan.HasMovables, the di<sup>f</sup>erence over time is small and not signi<sup>fi</sup>cant. This indicates that the e<sup>f</sup>ect of the behavioural intervention video is either non-existent or overshadowed by the behavioural in tervention given in the seminar.

The hypothesis about the e<sup>f</sup>ect of TTF (Hypothesis 2) is supported. The coe<sup>fi</sup>cient of Loan.HasMovables is large and signi<sup>fi</sup>cant at the 0.1% signi<sup>fi</sup>cance level. The marginal e<sup>f</sup>ects analysis further shows the impact of this factor. If the sales agreement of the collateral of the home loans did not contain movables, the percentage of correctly entered data ranges between 90 and 95 (Fig. 9). Conversely, if the sales agreement contained movables, the percentage of correctly entered data ranges between 21 and 36. However, this factor was not in<sup>fl</sup>uenced by an experimental treatment and therefore does not allow causal inference.

## 6. Discussion

Table 7 lists how the <sup>fi</sup>ndings of the empirical studies support the hypotheses underlying the CEMAD framework. In what follows, each hypothesis is discussed in more detail.

## 6.1. Hypothesis 1: Intention

The results of both experiments concerning the e<sup>f</sup>ect of the data producers’ intention on the amount of errors in the data they entered are largely in line with our expectations. In particular, the e<sup>f</sup>ect of intention across the two studies has the same direction, however, the strength and the signi<sup>fi</sup>cance of the e<sup>f</sup>ect vary between the two studies. The results of the lab experiment exhibit a large e<sup>f</sup>ect of strengthening the data producers’ intention on the amount of errors. For example, the free-of-error rate of the group that received the intention treatment was about 28% higher than the control group, and this e<sup>f</sup>ect was signi<sup>fi</sup>cant at the 1% signi<sup>fi</sup>cance level. The <sup>fi</sup>ndings of the application of the framework in the <sup>fi</sup>nancial institution provide mixed evidence for the intention hypothesis. To strengthen the intention of the data producers, two interventions were distributed to two groups. Both groups received the same intervention, and one group received an additional intervention. After the intervention was distributed to both groups, both groups entered the data more correctly. The size and the signi<sup>fi</sup>cance of the e<sup>f</sup>ect depend on which group the adviser was assigned to and whether the sales agreement of the collateral for the home loan contained movables or not. Nevertheless, the p values of these di<sup>f</sup>erences ranged between 0.083 and 0.141, rendering them non-signi<sup>fi</sup>cant or only marginally signi<sup>fi</sup>cant. The intervention that was only distributed to one group had no observable e<sup>f</sup>ect on the amount of errors in data.

![](/api/attachments/RGZW9KTC/fulltext/images/48174a3179fedda1ba5c53121e67833fde045055dbde7dd3288adee01559481e.jpg)  
Fig. 9. The marginal results per experimental group and the di<sup>f</sup>erences between the experimental groups including p values, standard errors between brackets and relative di<sup>f</sup>erences. In this analysis, the parameter of Loan.HasMovables is set to 0.

![](/api/attachments/RGZW9KTC/fulltext/images/30bc52590897fbc2a652355daf7565718d2d8c719f7972e6067302b2caff6627.jpg)  
Fig. 10. The marginal results per experimental group and the di<sup>f</sup>erences between the experimental groups including p values, standard errors between brackets and relative di<sup>f</sup>erences. In this analysis, the parameter of Loan.HasMovables is set to 1.

The di<sup>f</sup>erences between the <sup>fi</sup>ndings of the MTurk and application experiments can be explained as follows. First, the experiment during the application of the framework su<sup>f</sup>ered from sub-optimal design due to the limited amount of available resources. This sub-optimal design resulted in the application experiment having lower degrees of internal validity compared to the MTurk experiment. For example, the appli cation experiment had no real control group, had a smaller sample size, its data contained fewer errors and the time between the measurements varied greatly depending on the subject. As such, the evidence of the MTurk should be treated in higher regard compared to the evidence of the application study. Second, the experimental treatment of the MTurk experiment might have had a stronger e<sup>f</sup>ect on the data producers intention compared to the treatments that were given during the application of the framework in the <sup>fi</sup>nancial institution. For example, the behavioural treatment of the MTurk experiment to increase the data producers’ intention contained a statement about cancer. For some participants, this might have triggered psychosocial processes related to self-relevance, even more so when the data producers recently lost a friend or relative due to the disease. These self-relevance processes might have had a stronger e<sup>f</sup>ect on the data producers’ intention than those triggered at the employees of the <sup>fi</sup>nancial institution.

![](/api/attachments/RGZW9KTC/fulltext/images/889e3f789ff7ba1d247950a5b05e87a8c91e0ad5418976b2526211cc085e1966.jpg)  
(a) In this illustration, the parameter of Loan.HasMovables is set to 0.

The fact that the behavioural intervention in the <sup>fi</sup>nancial institution that was distributed to all home loan advisers had an observable e<sup>f</sup>ect and the other intervention did not is probably also related to the sub-optimal experimental design of the application study. The sub-op timal experimental design might have caused the e<sup>f</sup>ect of the intervention distributed to all advisers to be a false positive. That is, to observe this e<sup>f</sup>ect, the adopted setup was similar to a single group preand post-test design. The <sup>fi</sup>ndings of such single group designs might have been in<sup>fl</sup>uenced by external events that are unrelated to the be havioural intervention [43]. At the same time, the e<sup>f</sup>ect of the inter vention distributed to one group of advisers might be a false negative. In a preliminary study, we found evidence that the intention of the data producers was strengthened by the behavioural intervention [22]. The e<sup>f</sup>ect of their strengthened intention to enter data correctly on the amount of errors in the data these producers entered, might have been too small to observe. The free-of-error rate of the value of the collateral for the home loans was relatively high, resulting in little room for improvement or, the e<sup>f</sup>ect of the other behavioural intervention might have overshadowed the e<sup>f</sup>ect of the <sup>fi</sup>rst behavioural intervention.

![](/api/attachments/RGZW9KTC/fulltext/images/ce8cbd7526da3d34712407a39c7668db95bdfd64a58673be849f6aeb7f22b759.jpg)  
(b) In this illustration, the parameter of Loan.HasMovables is set to 1.  
Fig. 11. Graphical illustrations of how the di<sup>f</sup>erence-in-di<sup>f</sup>erence approach was applied to investigate the gains of the double treatment group, relative to the single treatment group as a consequence of the <sup>fi</sup>rst behavioural intervention. The outcome axis represents the error rate as estimated by the regression model.

Table 7  
A summary of the hypotheses and how the evidence from the two empirical studies provides support for the hypotheses.

<table><tr><td>Nr.</td><td>Hypothesis</td><td>MTurk experiment</td><td>Application experiment</td></tr><tr><td>H1</td><td>An increase in the intention of the data producers to enter correct data will cause an increase in the number of correctly entered registrations.</td><td>Supported</td><td>Weakly supported (mixed evidence)</td></tr><tr><td>H2</td><td>An increase in the fit between the data entry task, technology and data producers will cause an increase in the number of correctly entered registrations.</td><td>Supported</td><td>Supported (not causally)</td></tr><tr><td>H3</td><td>An increase in the fit between the data entry task, technology and data producers strengthens the effect of increasing the data producers&#x27; intention, and thus increases the number of correctly entered registrations.</td><td>Partly supported</td><td>Not tested</td></tr></table>

The intention of the data producers to enter data correctly can be strengthened by a behavioural intervention targeting one of the psychosocial factors as identi<sup>fi</sup>ed by the theory of planned behaviour [27]. Which psychosocial antecedent should be targeted is contextual and should be determined on a case-by-case basis. Nevertheless, a few things should be kept in mind.

First, recent research has shown that in one data entry context, instrumental attitude was the most important determining antecedent [27]. This can be explained as follows: in an organisational context, often, the person that enters the data is not the same as the person that will use the data [53]. This situation might cause the data producer not to know why it is important to enter the data correctly, rendering the instrumental attitude of the data producers towards entering data correctly low. Thus, if the data producers are not yet aware why correct data entry is important, providing such feedback might be an inexpensive and e<sup>f</sup>ective way to strengthen their instrumental attitude, and as a consequence, intention towards entering data correctly [22].

Second, the behavioural intervention should try to pull the data producers into entering data correctly rather than pushing them into this type of behaviour. Interventions that push data producers into entering data correctly highlight that data producers are required to enter data correctly while interventions that pull data producers into entering data correctly aim at creating an internal desire to enter data correctly. Pushing data producers into entering data correctly, for example, by increasing managerial pressure might have a small or adverse e<sup>f</sup>ect [54].

Third, there are many types of behavioural interventions that can be used to strengthen the intention of the data producers towards entering data correctly. Some examples are providing information, persuasion, increasing skills, goal setting, and so on [30]. Recent research has pointed out that the most e<sup>f</sup>ective behavioural intervention types are motivational appeals, persuasion and increasing skills [31].

## 6.2. Hypothesis 2: Task-technology fit

The evidence of both empirical studies strongly supported the hypothesis concerning TTF. Interestingly, in both studies, as evidenced by the coe<sup>fi</sup>cients of the regression models, TTF had a much greater e<sup>f</sup>ect on/correlation with the amount of errors in the manually acquired data than the increased intention of the data producers. This observation is similar to the observation of the study where the TTF model was proposed. That is, Goodhue and Thompson [23] found that, compared to other factors, TTF had the greatest power in explaining the performance of individuals when utilising managerial information [24].

However, the importance of the TTF or actual behavioural constructs, which are conceptually equal in the context of manual data entry, is often neglected when behavioural theories are applied in an information system context. For example, in a recent overview of studies that empirically and quantitatively tested the theory of planned behaviour in an information system context, none of the studies in cluded measures for actual behavioural control [27]. In addition, several frequently cited individual information system theories such as the technology acceptance model [55], do not include constructs that capture the degree to which individuals have control over using information system artefacts [24].

Therefore, the <sup>fi</sup>ndings of this study can be considered additional evidence for the relative importance of the TTF construct in the context of information systems.

## 6.3. Hypothesis 3: Interaction between task-technology fit and intention

The interaction of intention and TTF (Hypothesis 3) was only tested in the MTurk study. The evidence of the MTurk study partly supported this hypothesis. That is, the evidence showed there was most likely an interaction between both constructs, but, that the interaction of both treatments has the opposite direction as was anticipated. The e<sup>f</sup>ect of the combination of both treatments is not greater, but smaller than the sum of the individual treatment e<sup>f</sup>ects. Nevertheless, the combination of both treatments resulted in a lower amount of errors than each treatment separately.

That the combination of treatments is not greater than the sum of parts can be explained by the law of diminishing returns. This law states that at a certain point, adding a unit of a factor that determines production output will result in a lower incremental per-unit return. In this case, error-free data can be considered as production output and the factors that determine this output are intention and TTF. Obviously, it is easier to increase an error-free rate of 50% to 51% than to increase the same rate from 98% to 99%.

## 7. Implications for practice

From a practical viewpoint, the CEMAD framework can mainly be used to guide data quality improvement actions. For example, if during data quality assessment it was found that the errors were mostly caused by a low TTF, future actions that aim to improve the quality of the assessed data should invest in closing the gap between the task requirements, abilities of the individual data producer and the functionality of the technology. During our case study, for instance, we found that there was a low <sup>fi</sup>t between the data entry task and the technology because the information system required the data producers to enter the net monthly wage of the obligors, while in reality the obligors could receive a weekly wage, a variable wage or be self-employed. Because of to this poor <sup>fi</sup>t between the task and the technology, the data producers had to register the data according to various and complex business rules. As a result, the wage of the obligors was sometimes erroneously entered. To reduce the errors in the wage of the obligors, we advised the organisation to redesign the information system so the structure of the data would correspond to the structure of the reality. In contrast, if a data quality assessment points into the direction of the data producers having a low intention to enter data correctly (e.g. there are many rounding errors), organisations are advised to distribute behavioural interventions aimed at increasing their intention. In some cases, both factors of the CEMAD framework should be targeted.

When organisations use the framework to reduce errors in manually acquired data, the following should be kept in mind. First, the decision on which factor(s) to improve and how this/these factor(s) should be improved should be made with the context in mind and should be based on a cost/bene<sup>fi</sup>t analysis. On the one hand, error-free data will be bene<sup>fi</sup>cial for the organisation, while on the other hand, reducing errors in data leads to a certain cost. During the application of the framework, this trade-o<sup>f</sup> was especially relevant as distributing behavioural interventions was probably less e<sup>f</sup>ective than if we would have increased the TTF. However, in this case, and probably in other cases as well, distributing a behavioural intervention was cheaper than the alternative. Second, when interventions are applied to reduce the amount of errors in manually acquired data, new errors are prevented from en tering the database, but existing errors still reside in the database. Therefore, after new errors are prevented from entering the database, organisations should resolve the existing errors, by undertaking data cleaning activities.

## 8. Conclusion and future research

The goal of this research was to propose a theoretical framework that can help organisations to explain the errors in their manually acquired data and therefore can serve as a basis to guide future data entry improvement actions.

In response, we introduced and empirically validated the CEMAD (Causes of Errors in Manually Acquired Data)-framework using several empirical studies each with a distinct research method in a total of two separate settings. The CEMAD framework states that errors during manual data entry are caused by a weak intention of the data producers to enter the data appropriately and/or by a low degree of <sup>fi</sup>t between the data entry task, the technology and the data producer.

The CEMAD framework is informed by the existing theories on user behaviour and TTF but provides more insights in two ways. First, our theoretical framework re<sup>fi</sup>nes the theory of planned behaviour with the TTF construct so it can function as a basis for concrete guidelines on data quality improvement. Second, the proposed framework demon strates that the TTF construct, which is mostly used to explain how errors in the output of an information system a<sup>f</sup>ect the performance of a task, is also relevant to explain errors in the input of an information system, i.e. errors in manual data acquisition.

In both empirical studies, we found that to prevent errors in manual data entry, a high TTF is relatively more important than the data producers having a high intention to enter data correctly. This is additional empirical evidence for the importance of the TTF construct, a construct often neglected in information system research.

Future work should further investigate which aspects of TTF contribute the most to the correctness of manually acquired data and test the predictive power of the theoretical framework.

## Con<sup>fl</sup>ict of interest

The <sup>fi</sup>rst author was funded by the organisation at which one of the empirical studies took place.

## Acknowledgements

We would like to thank KBC Group NV for their <sup>fi</sup>nancial and op erational support.

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at https://doi.org/10.1016/j.im.2018.05.014.

## References

[1] A. Maydanchik, Data Quality Assessment, Technics Publications, 2007.

[2] J. Dias, D. Patnaik, E. Scopa, E. van Bommel, Automating the Bank's Back O<sup>fi</sup>ce, Tech. Rep. McKinsey, 2012.

[3] T. Haegemans, M. Snoeck, W. Lemahieu, F. Stumpe, A. Goderis, Towards a theo retical framework to explain root causes of errors in manually acquired data, International Conference on Information Quality, Ciudad Real, Spain, 2016, pp. 15:1 15:10.

[4] K. Thiru, A. Hassey, F. Sullivan, Systematic review of scope and quality of electronic patient record data in primary care, BMJ 326 (7398) (2003) 1070.

[5] D.G.T. Arts, N.F. De Keizer, G.-J. Sche<sup>f</sup>er, De<sup>fi</sup>ning and improving data quality in medical registries: a literature review, case study, and generic framework, J. Am. Med. Inform. Assoc. 9 (6) (2002) 600 611.

[6] D.R. Goldhill, A. Sumner, APACHE II, data accuracy and outcome prediction, Anaesthesia 53 (10) (1998) 937–943

[7] M.N. Espetvedt, O. Reksen, S. Rintakoski, O. Osterås, Data quality in the Norwegian dairy herd recording system: agreement between the national database and disease recording on farm, J. Dairy Sci. 96 (4) (2013) 2271–2282 http://www.ncbi.nlm. nih.gov/pubmed/23462169

[8] N. DeHoratius, A. Raman, Inventory record inaccuracy: an empirical analysis, Manag. Sci. 54 (4) (2008) 627–641.

[9] K.C. Laudon, Data quality and due process in large interorganizational record sys tems, Commun. ACM 29 (1) (1986) 4–11.

[10] N.G. Weiskopf, C. Weng, Methods and dimensions of electronic health record data quality assessment: enabling reuse for clinical research, J. Am. Med. Inform. Assoc. 20 (2013).144–151

[11] K.A. Barchard, L.A. Pace, Preventing human error: the impact of data entry methods on data accuracy and statistical results, Comput. Hum. Behav. 27 (5) (2011) 1834–1839, http://dx.doi.org/10.1016/j.chb.2011.04.004.

[12] M. Kozak, W. Krzanowski. I. Cichocka, J. Hartley, The effects of data input errors on subsequent statistical inference, J. Appl. Stat. 42 (9) (2015) 2030–2037 http:// www.tandfonline.com/doi/full/10.1080/02664763.2015.1016410.

[13] V.R. Moore, NSWCCA 260, (2016) https://www.caselaw.nsw.gov.au/decision/ 5834d37ce4b058596cba1abd.

[14] K.A. Olsen, The \$100,000 keying error, Computer 41 (4) (2008)

[15] L. Josephs, This is How An Airplane Ended Up at the Wrong Airport, (2016 September) http://qz.com/775903.

[16] C. Newton, How a Typo Took Down S3, The Backbone of the Internet, 2017, https://www.theverge.com/2017/3/2/14792442/amazon-s3-outage-cause-typointernet-server

[17] I. Ajzen, The theory of planned behavior, Organ. Behav. Hum. Decis. Process. 50 (1991) 179–211.

[18] M. Fishbein, I. Ajzen, Predicting and Changing Behavior: The Reasoned Action Approach, Psychology Press, 2010.

[19] P. Sheeran, Intention-behavior relations: a conceptual and empirical review, Eur. Rev. Soc. Psychol. 12 (1) (2002) 1–36.

[20] G.D. Murphy, Improving the quality of manually acquired data: applying the theory of planned behaviour to data quality, Reliab. Eng. Syst. Saf. 94 (12) (2009) 1881 1886.

[21] Y.W. Lee, D.M. Strong, Knowing-why about data processes and data quality, J. Manag, Inf, Systems 20 (3) (2003) 13–39.

[22] T. Haegemans, M. Snoeck, J. Lismont, W. Lemahieu, The link between the data producers’ knowing-why and their intention to enter data correctly, IEEE Conference on Business Informatics. JEEE. Thessaloniki, Greece, 2017

[23], D.L.. Goodhue, R.L.. Thompson. Task-technology fit and individual performance, MIS Q. 19 (2) (1995) 213–236

[24] D.L. Goodhue, Task-technology <sup>fi</sup>t: a critical (but often missing!) Construct in models of information systems and performance, in: P. Zhang, D. Galletta (Eds.), Human-Computer Interaction and Management Information Systems: Foundations M.E. Sharpe, 2006, pp. 184–204 (Ch. 9).

[25] D.L. Goodhue, Understanding user evaluations of information systems, Manag. Sci. 41 (12) (1995)1827–1844.

[26] K. Orr, Data quality and systems theory, Commun, ACM 41 (2) (1998) 66–71

[27] T. Haegemans, M. Snoeck, W. Lemahieu, Entering data correctly: an empirical evaluation of the theory of planned behaviour in the context of manual data ac quisition, Reliab. Eng. Syst. Saf. (2018) (in press)

[28] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Commun. ACM 39 (November (11)) (1996) 86–95.

[29] C.J. Armitage, M. Conner, E<sup>fi</sup>cacy of the theory of planned behaviour: a metaanalytic review, Br. J. Soc. Psychol. 40 (2001) 471 499.

[30] W. Hardeman, M. Johnston, D.W. Johnston, D. Bonetti, N.J. Wareham A.L. Kinmonth, Application of the theory of planned behaviour in behaviour change interventions: a systematic review, Psychol. Health 17 (2) (2002) 123–158

[31] H. Steinmetz, M. Knappstein, I. Ajzen, P. Schmidt, R. Kabst, How e<sup>f</sup>ective are be havior change interventions based on the theory of planned behavior? Zeitschrift für Psychologie 224 (3) (2016) 216 233, http://dx.doi.org/10.1027/2151-2604/ a000255

[32] S. Cane, R. McCarthy, Analyzing the factors that a<sup>f</sup>ect information systems use: a

task-technology <sup>fi</sup>t meta-analysis, J. Comput. Inf. Syst. 50 (1) (2009) 108 123 http://www.iacis.org/jcis/jcis.php.

[33] A. Kittur, E.H. Chi, B. Suh, Crowdsourcing user studies with mechanical turk, ACM Conference on Human Factors in Computing Systems (2008) 453–456 http://dl. acm.org/citation.cfm?id=1357127.

[34] J. Ross, L. Irani, M.S. Silberman, A. Zaldivar, B. Tomlinson, Who are the crowdworkers? Shifting demographics in mechanical Turk, ACM Conference on Human Factors in Computing Systems (2010) 2863 http://portal.acm.org/citation.cfm? doid=1753846.1753873.

[35] G. Paolacci, J. Chandler, P.G. Ipeirotis, Running experiments on Amazon mechan ical Turk, Judg. Decis. Mak. 5 (5) (2010) 411–419 http://repub.eur.nl/pub/31983.

[36] M.J.C. Crump, J.V. McDonnell, T.M. Gureckis, Evaluating Amazon's mechanical Turk as a tool for experimental behavioral research. PLoS ONE 8 (3) (2013).

[37] J.D. Weinberg, J. Freese, D. McElhattan, Comparing data characteristics and results of an online factorial survey between a population-based and a crowdsource-re cruited sample, Sociol. Sci. 1 (August) (2014) 292–310 http://www. sociologicalscience.com/articles-vol1-19-292/.

[38] Y. Krupnikov, A.S. Levine, Cross-sample comparisons and external validity, J. Exp. Polit, Sci, 1 (1) (2014) 59–80.

[39] W. Mason, S. Suri, Conducting behavioral research on Amazon's mechanical Turk, Behav. Res. Methods 44 (March (1)) (2012) 44:1 44:23 http://www.ncbi.nlm.nih. gov/pubmed/21717266.

[40] M. Buhrmester, T. Kwang, S.D. Gosling, Amazon's mechanical Turk: a new source of inexpensive, yet high-quality, data? Perspect. Psychol. Sci. 6 (1) (2011) 3–5, http:/ dx.doi.org/10.1177/1745691610393980.

[41] M.T. Orne, Demand characteristics and the concept of quasi-controls, Artifact in Behavioral Research, Academic Press, 1969, pp. 143–179 Ch. 5.

[42] F.J. Roethlisberger, W.J. Dickson, Management and the Worker, Harvard University Press, 1939.

[43] W.R. Shadish, T.D. Cook, D.T. Campbell, Experimental and Quasi-Experimental Designs for Generalized Causal Inference, Houghton Mi<sup>fl</sup>in, 2002.

[44] J.P. Simmons, L.D. Nelson, U. Simonsohn, False-positive psychology: undisclosed <sup>fl</sup>exibility in data collection and analysis allows presenting anything as signi<sup>fi</sup>cant, Psychol. Sci. 22 (11) (2011) 1359–1366 http://journals.sagepub.com/doi/10. 1177/0956797611417632.

[45] A.A. Montgomery, T.J. Peters, P. Little, Design, analysis and presentation of factorial randomised controlled trials, BMC Med. Res. Methodol. 3 (1) (2003) 26 http://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288- 3-26.

[46] C.-YJ. Peng. K.L.. Lee. G.M. Ingersoll. An introduction to logistic regression analysis and reporting, J. Educ. Res. 96 (1) (2002) 37–41.

[47] N. Nagelkerke, J. Smits, S. le Cessie, H. van Houwelingen, Testing goodness-of-<sup>fi</sup>t of the logistic regression model in case-control studies using sample reweighting, Stat.

Med. 24 (1) (2005) 121–130.

[48] V.V. Acharya, M. Richardson, Causes of the <sup>fi</sup>nancial crisis, Crit. Rev. 9 (4) (2009) 12 21.

[49] S.R. Evans, D.W. Hosmer, Goodness of <sup>fi</sup>t tests in mixed e<sup>f</sup>ects logistic models characterized by clustering, Commun. Stat. 33 (5) (2004) 1139–1155.

[50] R.X. Sturdivant, D.W. Hosmer, A smoothed residual based goodness-of-<sup>fi</sup>t statistic for logistic hierarchical regression models, Comput. Stat. Data Anal. 51 (8) (2007) 3898 3912.

[51] A.A.P.N.M. Perera, M.R. Sooriyarachchi, S.L. Wickramasuriya, A goodness of <sup>fi</sup>t test for the multilevel logistic model, Commun. Stat. 45 (2) (2016) 643–659 https:// www.tandfonline.com/doi/full/10.1080/03610918.2013.868906.

[52] J.H. Stock, M.W. Watson, Introduction to Econometrics, 3rd Ed., Addison-Wesley, 2012.

[53] D. Te’eni, Behavioral aspects of data production and their impact on data quality, J. Database Manag, 4 (2) (1993) 30–38

[54] R. Molina, K. Unsworth, M. Hodkiewicz, E. Adriasola, Are managerial pressure, technological control and intrinsic motivation e<sup>f</sup>ective in improving data quality? Reliab. Eng. Syst. Saf. 119 (2013) 26–34.

[55] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Q. 13 (3) (1989) 319–340

Tom Haegemans is PhD candidate at the KU Leuven. He holds a Master's degree in Information Management and a Bachelor's degree in Applied Informatics. His research interests include: data quality measurement, representation of data quality measurements, causes of errors in manually acquired data, and data alignment strategies.

Monique Snoeck is full professor at the KU Leuven, and visiting professor at the U Namur. Her research focuses on enterprise modeling, requirements engineering, model driven engineering and business process management. Her main guiding research themes are the integration of di<sup>f</sup>erent modelling approaches into a comprehensive approach, the quality of models through formal grounding, model to code transformations and educational aspects of conceptual modelling. She has published over 80 peer-reviewed papers.

Wilfried Lemahieu is Dean of the Faculty of Economics and Business (FEB) of KU Leuven. He holds a master's degree in Business and Information Systems Engineering and a PhD in Applied Economics, both from KU Leuven. As a member of the Department of Decision Sciences and Information Management of FEB, he conducts research on big data storage, integration and analytics; data quality; business process management; and service oriented architectures. His research was published in leading journals such as International Journal of Information Management; Applied Soft Computing; and Decision Support Systems.
