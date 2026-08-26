---
otero_id: 15078
otero_key: "JVSMAGF5"
title: "Can Humans Detect Errors in Data? Impact of Base Rates, Incentives, and Goals1"
authors: "Barbara D. Klein; Dale L. Goodhue; Gordon B. Davis"
year: "1997"
journal: "MIS Quarterly"
doi: "10.2307/249418"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can Humans Detect Errors in Data? Impact of Base Rates, Incentives, and Goals $^{1}$

By Barbara D. Klein
University of Michigan-Dearborn
Dearborn, MI 48128-1491
U.S.A.
bdklein@fob-f1.umd.umich.edu

Dale L. Goodhue
Terry College of Business
University of Georgia
Athens, GA 30602
U.S.A.
dgoodhue@cbacc.cba.uga.edu

Gordon B. Davis
Carlson School of Management
University of Minnesota
Minneapolis, MN 55455
U.S.A.
gdavis@csom.spcs.umn.edu

## Abstract

There is strong evidence that data items stored in organizational databases have a significant rate of errors. If undetected in use, those errors in stored data may significantly affect business outcomes. Published research suggests that users of information systems tend to be ineffective in detecting data errors. However, in this paper it is argued that, rather than accepting poor human error detection performance, MIS researchers need to develop better theories of human error detection and to improve their understanding of the conditions for improving performance. This paper applies several theory bases (primarily signal detection theory but also a theory of individual task performance, theories of effort and accuracy in decision making, and theories of goals and incentives) to develop a set of propositions about successful human error detection. These propositions are tested in a laboratory setting. The results present a strong challenge to earlier assertions that humans are poor detectors of data errors. The findings of the two laboratory experiments show that explicit error detection goals and incentives can modify error detection performance. These findings provide an improved understanding of conditions under which users detect data errors. They indicate it is possible to influence detection behavior in organizational settings through managerial directives, training, and incentives.

Keywords: Information attributes, user behavior, data

ISRL Categories: AD05, BG03, HC0201

## Introduction

Suppose your clerk is calculating pension benefits for individuals in a company. A record indicates that John Smith is 24 years old and has been with the firm for ten years. Is it likely your clerk would notice that this data implies John Smith started with the firm when he was fourteen years old? Would your clerk flag this as a possible error?

Between 1% and 10% of data items in critical organizational databases are estimated to be inaccurate (Laudon 1986; Morey 1982; Redman 1992). To contain the potential negative impact of inaccurate data in organizations, two main approaches have been suggested:

(1) automatically validate data as items are input to databases (e.g., Morey 1982; Paradice and Fuerst 1991) or (2) depend on users to detect and correct errors.

One might ask, why burden the user with the error correction task when other work has shown information systems could do it automatically? The reason is that system-based error correction, although very useful where it is applied, is limited by some important practical factors. First, organizations are not always willing to pay the extra up-front system development costs, or will only pay for limited error correction. Second, even with skilled error detection algorithm designers and functional experts who know the data, it is hard to anticipate all errors that might occur. Third, end user computing enhances the possibility of errors in data, since these applications are less likely to include effective system-based error correction.

Given these practical limitations, system-based error correction is a long way from rendering organizational data "clean." In such an environment, the optimal approach to error correction should probably include both human and system-based error correction.

However, most existing research suggests that humans are quite poor at error detection (Davis et al. 1967; Laudon 1986; Ricketts 1990). The editor's executive overview of a recently published paper (Ricketts 1990) states: "The results suggest that MIS management had better not rely on users to detect errors in computer outputs" (Executive Overview 1990). In other words, do not count on your clerk to catch the error about John Smith. If humans cannot detect errors, and efforts to automatically validate data have not succeeded in eliminating errors, organizations are extremely vulnerable to data inaccuracies.

In this paper, it is argued that the human ability to detect errors should not be written off prematurely. Rather, humans can and do detect errors, and human error detection performance can be improved. Knowledge about human performance in general needs to be brought to bear on the domain of error detection so that the conditions under which humans are more effective error detectors can be better understood. This is essential if resources are to be allocated efficiently to combined system and human-based data quality efforts.

To this end, this paper uses several theory bases (primarily signal detection theory but also a theory of individual task performance, theories of effort and accuracy in decision making, and theories of goals and incentives) to develop a set of propositions about successful human error detection. These propositions are tested in a laboratory setting. The findings present a strong challenge to earlier assertions that humans are, in general, poor error detectors. They represent useful steps in developing a better understanding of human error detection performance.

The remaining sections of this paper present (1) a review of prior research bearing directly on the question of the conditions under which individuals detect errors in data, (2) a theory of error detection and the research propositions, (3) the methodology and results of two laboratory experiments, (4) a synthesis of the research findings across the two experiments, and (5) conclusions, prescriptions for organizational settings, and suggestions for further research.

## Background

In a broad sense, this investigation falls within the area of data quality. While no single definition of data quality has been accepted by researchers working in this area, there is agreement that data accuracy, currency, and completeness are important areas of concern (Agmon and Ahituv 1987; Davis and Olson 1985; Fox et al. 1993; Huh et al. 1990; Madnick and Wang 1992; Wand and Wang 1996; Zmud 1978). This investigation adopts the definition of data quality (Huh et al. 1990) which includes four dimensions of data quality: accuracy, completeness, consistency, and currency. This study is primarily concerned with data accuracy, defined as agreement with either an attribute of a real world entity, a value stored in another database, or the results of an arithmetic computation (Huh, et al. 1990).

Several general conclusions can be drawn from the existing research on data quality. First, while it is difficult to compare error rates across studies, rates substantially greater than zero have been found in all of the studies addressing the extent to which data errors exist in databases (Ham, et al. 1985; Johnson et al. 1981; Knight 1992; Laudon 1986; Stone and Bublitz 1984). Second, there is disagreement about the extent to which efforts to purge all errors from databases should be attempted. Some researchers propose methods designed to completely rid databases of errors (Janson 1988; Svanks 1988; Naus 1975; Parsaye and Chignell 1993), while others propose tools for determining how to best allocate limited resources to controlling the level of data errors (Ballou and Pazer 1987a; Ballou and Tayi 1989; Ballou, et al. 1987; Bowen 1992; Paradice and Fuerst 1991). Third, many researchers argue that users need not discard data containing errors. A variety of approaches for using imperfect data have been suggested (Ballou and Pazer 1985a, 1987a, 1995; Bansal et al. 1993; Gaba and Winkler 1992; Garfinkel et al. 1986; O'Leary 1993; O'Neill and Vizine-Goetz 1988).

This study fits into this last category of the literature on data quality that describes ways in which users of information systems might modify their use of data if they are aware that there are errors. In general, the data quality literature argues that users are not very capable of finding errors in data and then altering the way in which they use the data. More specifically, there is considerable evidence of poor user performance in detecting data errors. A field experiment was conducted in which individuals were mailed banking confirmation statements with embedded errors (Davis et al. 1967). The individuals were asked to verify their account information and approximately half failed to detect important errors. Other research found that users of criminal information systems rarely detected errors in these records even though information provided to police departments by the FBI is accompanied by a warning stating that the user should verify that the information is accurate (Laudon 1986). A laboratory experiment was conducted in which over 90% of the subjects failed to detect a substantial data error in production planning reports (Ricketts 1990). The failure of humans to detect errors in data is also assumed in much of the literature on data quality, in which it is argued that resources should be devoted to the up-front improvement of the quality of data in organizational databases (e.g., Redman 1992, 1995).

The three studies mentioned above that tested human error detection abilities may underestimate the extent to which users can detect errors if there were situation-specific conditions in these studies that reduce error detection. For example, subjects in one study may not have understood that error detection was part of the experimental task (Ricketts 1990). Subjects who failed to detect the error in another study (Davis et al. 1967) may simply not have accepted responsibility for carefully checking the confirmation statements.

Guided primarily by a strong sense that the above research misrepresented organizational behavior in handling data, a pilot study was conducted to investigate whether actuaries typically detect errors in data (Klein 1995, 1996). Actuaries were studied because it was expected that (1) they would be highly motivated to detect errors since they use data of uncertain accuracy generated outside of their organizations and (2) they would develop effective methods for working with inaccurate data because errors frequently occur in this domain.

A series of semi-structured interviews was conducted with ten actuaries. All of the actuaries reported instances in which they successfully detected errors in data. These errors were detected when the data itself or values calculated using the data conflicted with the actuaries' prior expectations. For example, outliers such as very large or very small values or unexpected changes over time caught the actuaries' attention. The degree to which data items were reviewed for errors prior to use was affected by the actuaries' expectations about the likelihood of errors in a given dataset. The actuaries did not attempt to detect all errors, apparently responding to a perceived tradeoff between the time and effort required to find additional errors versus the potential impact of a more accurate dataset. These results suggested the value of additional research on human error detection behavior.

## A Theory of Error Detection

Conceptually, there are four possible outcomes in error detection tasks, as shown in Figure 1 (Baker and Schuck 1975; Levi 1985). In the example of the clerk in the pension calculation task, the data record for a given individual either does or does not contain an error. The clerk, when working with the record, either concludes or does not conclude that the record contains an error. Therefore, actual errors can be successfully detected (hits) or missed (misses). When no error exists, the clerk may incorrectly conclude there is an error (false alarm) or correctly conclude there is no error (correct rejection). Thus the performance of an individual can be characterized by a table like the one in Figure 1 with a conditional probability in each cell. A similar conceptualization of error detection behavior can be found in the considerable research that has been done in the area of imperfect quality control inspection in manufacturing systems (Ballou and Pazer 1982, 1985b, 1987b; Biegal 1974; Collins et al. 1973; Dorris and Foote 1978; Sinclair 1978).

<table><tr><td rowspan="4">Data</td><td colspan="2">Behavior</td></tr><tr><td>Error Detected</td><td>Error Not Detected</td></tr><tr><td>Hit</td><td>Miss</td></tr><tr><td>False Alarm</td><td>Correct Rejection</td></tr></table>

Figure 1. Presence of Errors and Detector Responses

## Signal detection theory and error detection

A theory of error detection should give a better understanding of how situational characteristics affect the relative likelihood of the four possible outcomes in Figure 1. Signal detection theory is an extension of statistical decision theory. It has been applied in a broad range of psychological domains such as the detection of a tone (McNicol 1972), the detection of a flash of light (McNicol 1972), the detection of differences in the length of lines (Bonnel and Noizet 1979), the detection of social cues (Thompson 1978), recognition memory (Koppell 1977; Lockhart and Murdock 1970; Murdock 1982), the recognition of advertisements (Cradit et al. 1994; Singh and Churchill 1986), the evaluation of forecast accuracy (Levi 1985), and human vigilance (Craig 1987; Jerison 1967). The common thread across these studies is that there is an interest in explaining the performance of humans distinguishing between two classes of events. Signal detection theory labels these two classes of events as "noise" and "signal." Noise can be thought of as background; a signal is a stimulus that may be detected because it deviates from background noise. Signal detection theory explains the performance of humans who are trying to determine when a signal is present (Green and Swets 1966; McNicol 1972; Pastore and Scheirer 1974; Swets 1988).

In the context of error detection, a record without errors represents background noise and a record with a data error provides a signal. In the example of calculating accrued pensions, the clerk must examine a display of information and determine whether the data contained in the display are correct or errorful. Records with errors and records without errors present different aspects to the clerk. This presumably affects the clerk's perception of the record. Following signal detection theory, this can be represented by the two distributions in Figure 2 (Davies and Parasuraman 1981). A similar diagram used in analyzing system-based error detection options has been developed independent of signal detection theory (Paradice and Fuerst 1991).

The two curves shown in Figure 2 represent two different distributions of the internal state of the human detector that is said to mediate between a stimulus and a response (Davies and Parasuraman 1981). One of the curves represents the distribution of the internal state that occurs in the presence of random noise. The other curve represents the distribution of the internal state that occurs when a signal is added to random noise. A record with a glaring error might be perceived by the clerk as being near the right hand side of the figure, to the right of $x_{2}$ . These the clerk could reliably classify as errorful. A record with no hint of problems might be perceived as being near the left hand side of the figure, to the left of $x_{1}$ . These the clerk could reliably classify as correct. In general, it is assumed that the clerk is not able to perfectly distinguish correct from errorful records in all cases (Davies and Parasuraman 1981; Swets 1988). Thus, the two distributions overlap. Records perceived as being in the overlapping portion of the figure (between $x_{1}$ and $x_{2}$ ) cannot be so easily classified.

It should be noted that the stimulus variable on the x axis in Figure 2 has a much more abstract meaning when the diagram is applied to human-based error detection than it typically does in signal detection. In most signal detection research, x is the magnitude of some explicit signal such as the loudness of a tone, the brightness or duration of a light, or some other stimulus. In human-based error detection, x is a sort of “discomfort index” assumed to be generated by the human in the course of looking at the data. In the simplest cases, it might be based on only one or two variables (for example, the user might note with surprise and suspicion that the president of the company seems to be only 15 years old). In other cases it may be much more involved, encompassing several or many different data items in one or more records. It is assumed that the discomfort index is derived idiosyncratically by the human as he or she looks at the data.

In signal detection theory, two key factors drive the performance of individuals attempting to distinguish between signal and noise: the discriminability of the distributions and the response criterion. As the overlap between the two distributions increases, a greater portion of stimuli cannot be reliably classified, and discriminability has decreased. With decreased discriminability, false alarms or misses become more frequent. In the context of the clerk making pension calculations, high discriminability would mean that if there were an error, it would tend to be very glaring. Thus it would be easy to discriminate between correct and errorful records. Low discriminability would mean that many records had ambiguous clues that might or might not reflect actual errors.

![](/api/attachments/JVSMAGF5/fulltext/images/b7cd4ac3605d62566cf3878de59d2ff4cb33eca4065094ad2d3beb1bbc7b132f.jpg)  
Figure 2. Distributions for Data With an Error and Data Without Errors

For a given level of discriminability, signal detection theory suggests that human detectors set a response criterion at some point between $x_{1}$ and $x_{2}$ to determine whether to label an ambiguous stimulus as noise or as a signal. An example response criterion is shown in Figure 2 as $x_{c}$ . Perceptions to the right of $x_{c}$ would be labeled signal and perceptions to the left of $x_{c}$ would be labeled noise. An individual might set his or her response criterion at any point between $x_{1}$ and $x_{2}$ . For example, the clerk might decide to ignore all but the most glaring clues about errors (i.e., place the response criterion far to the right) and thus would have relatively more correct rejections, but also more misses. Alternatively, the clerk could decide to flag any even slightly ambiguous record as errorful (i.e., place the response criterion far to the left) and would have more hits, but also more false alarms.

Signal detection theory suggests that expectations about the base rate of errors will influence the placement of the response criterion, as will an assessment of the incentives derived from the costs and benefits of error detection. Compared to users who expect few errors in data, users who expect a high base rate of errors will suspect that more data items are in error both when errors exist and when errors do not exist. In other words, a clerk who expected that data from a particular firm would have many errors might tend to set his or her response criterion rather far to the left. However, if the clerk expected that most data from a second firm was error free, he or she might set the response criterion rather far to the right (Baker and Schuck 1975).

There is a large body of theoretical and empirical work addressing the question of the effect of base rate expectations in probabilistic judgment tasks. This research was recently synthesized (Koehler 1996) and acknowledges that there are conditions under which people make less use of base rate information than prescribed by a Bayesian normative standard (e.g., Gigerenzer et al. 1988; Kahneman and Tversky 1973; Nisbett and Borgida 1975). However, the argument presented is that people do not ignore base rate information and that there are a number of task conditions that affect the extent to which base rate information is used. Specifically, judgments have been found to be affected by base rates under three conditions: (1) when base rate expectations are developed through direct experience (Butt 1988; Christensen-Szalanski and Beach 1982; Christensen-Szalanski and Bushyhead 1981; Manis et al. 1980), (2) when base rate information is based on multiple, random samples from clearly-defined sample spaces (Gigerenzer et al. 1988; Ginossar and Trope 1987; Grether 1980), and (3) when base rates are based on large samples or provided by reliable sources (Ginossar and Trope 1987; Kassin 1979). A recent study provides further support for the contention that subjects use base rate information in probabilistic judgment tasks under at least some conditions and shows that judgments are improved when base rate information is presented graphically instead of in a verbal description of a problem (Roy and Lerch 1996).

Independent of expectations about base rates of errors, incentives derived from the costs and benefits of detecting or missing errors should also affect the placement of the response criterion. If a missed error is extremely damaging, the response criterion would be set far to the left. If a false alarm is extremely embarrassing, then the response criterion would be set far to the right (Baker and Schuck 1975).

Implicit in the above discussion is the assumption made in most applications of signal detection theory that discriminability is fixed for any given task. That is, it is assumed that individuals can adjust their response criteria but they cannot adjust discriminability. This is a reasonable assumption in the strictly perceptual task domains (such as the auditory detection of a tone) for which signal detection theory was originally developed. When discriminability is fixed, individuals cannot increase the rate of hits without also increasing the rate of false alarms. Consistent with this view of discriminability, signal detection theory does not generally address the link between effort and performance. However, in applying signal detection theory to the detection of errors in data, there may be changes in discriminability due to shifts in attention or effort in this semantic discrimination task. By trying harder or paying closer attention to a display of information, an individual may be better able to distinguish errors from correct data values. This suggests that effort may affect performance through changes in discriminability.

Signal detection theory thus provides a way of conceptualizing the error detection process as one in which individuals choose where to set their response criteria. They may also choose how much effort to expend in analyzing a data display, thus modifying their ability to discriminate between correct and errorful records. Changes in error detection performance can be analyzed in terms of shifts in discriminability and shifts in response criteria.

## Borrowing from additional theory bases

Three other theories are useful in understanding error detection performance: theories of individual task performance, theories of effort and accuracy in decision making, and theories of goal setting and incentives.

Theories of individual task performance. Theories of individual task performance provide some guidance for identifying conditions under which users can improve their discriminability. For example, experience seems to affect performance in general and may affect performance in error detection through increasing discriminability. Campbell's theory of individual task performance (depicted in Figure 3) suggests that experience, knowledge, and effort may affect error detection performance, presumably by affecting an individual's ability to successfully discriminate between correct and errorful records (Campbell 1990; Campbell and Pritchard 1976; Weber et al. 1993). While theories of expertise and knowledge are not directly applied in this study, Campbell's emphasis on the relationship between effort and task performance is used here.

![](/api/attachments/JVSMAGF5/fulltext/images/6309787019ec4aa476da3951d509423a7af8698477cfde178ad3b8c615fe34e3.jpg)  
Figure 3. Determinants of Individual Task Performance

Theories of effort, accuracy, and incentives in decision making. Theories of effort and accuracy in decision making suggest that individuals will adopt information processing strategies that focus effort on specific components of an information intensive task that are likely to lead to desirable outcomes. An underlying assumption of this perspective is that humans will devote no more mental resources or effort to task components than are demanded by task requirements. A number of studies have found that incentive structures can influence information processing strategies and hence performance (Cryer et al. 1990; Johnson and Payne 1985; Payne 1982; Payne et al. 1988). In the context of the error detection task, individuals may allocate their total effort (including effort focused on improving discriminability) so that they improve their total payoffs. In other words, discriminability can be influenced by incentive schemes that make it more attractive to successfully detect errors or schemes that provide incentives to both maximize hits and minimize false alarms.

Theories of goal setting and incentives. Although there are exceptions (e.g., Martin and Murberger 1994), many studies of human behavior show that goal setting affects task performance (e.g., Stock and Cervone 1990). Several literature reviews and meta-analyses conclude that specific, difficult goals improve task performance (Latham and Yukl 1975; Locke et al. 1981; Locke and Latham 1990; Mento et al. 1987). Task goals may operate by encouraging people to devote additional effort to a task (Locke et al. 1981) or by encouraging people to focus their effort on those components of a task emphasized by the goal (Teborg 1976).

Numerous studies have also demonstrated that performance-contingent incentives affect task performance in both laboratory and field settings (e.g., Eysenck and Eysenck 1980; Guzzo, et al. 1985; Henry and Strickland 1994; Hicken et al. 1992; Jenkins 1986; Lee 1988; Locke, et al. 1980; Morrison, et al. 1995). Several theorists have also suggested that there is an interaction between incentives and goal setting. That is, incentives increase commitment to task goals (Hollenbeck and Klein 1987; Locke et al. 1981). Empirical support for this interaction effect has been found (Lee 1988; Wright 1992).

This suggests that performance in detecting data errors might be significantly influenced through the explication of task goals (e.g., Locke and Latham 1984). One explanation for the poor performance of subjects in prior studies of human error detection is that subjects either did not understand that error detection was part of the experimental task (Ricketts 1990) or did not accept responsibility for reviewing data for errors (Davis et al. 1967). In contrast, actuaries in the pilot study seemed to consider detecting errors in data to be a part of their professional responsibilities (i.e., part of their goals).

Individuals who have not accepted error detection as a component of their task will presumably respond only to the most glaring of errors. Thus their response criteria will be set very far to the right, and presumably their discriminability will be quite low due to a lack of effort expended in error detection.

## Propositions

The theory of error detection outlined above can be summarized in a number of propositions about the conditions under which individuals will detect errors in data.

Proposition 1. Expectations about the base rate of errors in data will influence performance in error detection through shifts in the response criterion. Specifically, there will be both more hits and more false alarms when expectations about base rates of error are higher.

Proposition 2. Payoffs will influence performance in the detection of errors both through shifts in the response criterion and through changes in discriminability. If payoffs provide incentives for "hits," we might expect both shifts in the response criterion (i.e., more hits and more false alarms) and increased discriminability (i.e., fewer misses and fewer false alarms) due to greater effort. If there are both incentives for "hits" and penalties for "false alarms," we would not expect shifts in the response criterion, but we would expect increases in discriminability as individuals devote more effort to distinguishing errors from correct values.

Proposition 3. Explicit error detection goals will influence performance in error detection through changes in discriminability and the response criterion. In the extreme case, for users who do not understand and accept that error detection is a component of their task or job, discriminability should be quite poor and the response criterion far to the right. As responsibility for error detection is accepted and as the subtask of error detection is understood by the user, discriminability should increase. Users may also become more willing to label ambiguous signals as errors once they have accepted the goal of error detection. Thus, we may also see a shift in the response criterion. We expect to see a substantial increase in the hit rate and a more modest increase in the false alarm rate once the error detection component of a task is recognized and accepted.

## Experimental Methodology

Two laboratory experiments were conducted to test the three research propositions outlined above. Both experiments used the same basic experimental task, the same dependent variables, and the same type of subject. The first experiment addresses the impact of base rates and incentives. The second tests the effect of explicit error detection goals.

## Experimental task

The experimental task was the calculation of accrued pension benefits for employees in several firms using data containing a number of embedded errors. As a cover for the true focus of the experiment, subjects were told that the experiment was intended to study the use of spreadsheet software in business situations. After a brief review of the spreadsheet commands needed to manipulate data, subjects were given 80 minutes in which to perform the experimental task for at least two, but as many as possible, of six firms. The time limit was imposed in order to simulate organizational settings in which users who have several tasks to complete during a work day have to decide how much time to allocate to error detection.

Subjects were given three types of materials to assist them in their task: (1) a data file for the current year in spreadsheet format, (2) printed reports with the current and the previous year's data for each firm to facilitate comparisons over time, and (3) a procedure manual explaining the meaning of the data elements and the algorithm for the pension calculation. Finally, a short questionnaire containing items for manipulation checks was administered at the end of the experimental session.

Based on a task analysis and discussion with a domain expert, errors were embedded in 36 of the 100 employee records that subjects received for the first two firms. The embedded errors were similar to those discussed by the ten actuaries in the semistructured interviews. An example of an error in an employee record is an inconsistency between the value in the "hire date" field and the value in the "years of service" field. The task was validated by a domain expert to verify that the types of errors embedded in the data are representative of the data errors that occur in the domain. The embedded errors were the same in all of the experimental conditions.

## Dependent variables

To test the propositions, it is necessary to recognize when discriminability has changed and when response criteria have shifted. As explained below, there are several techniques for estimating discrimination unambiguously. Recognizing response criteria shifts is not so straightforward. In the absence of discrimination changes, a shift in response criteria can be recognized when hits and false alarms either both increase or both decrease. However, it is possible that when response criteria and discrimination change at the same time, we might see increases in hits but no change in false alarms. Thus, our ability to unambiguously recognize shifts in response criteria is somewhat limited.

With the above in mind, both experiments used the same four dependent variables. Two of these dependent variables are quite straightforward: the proportion of errors successfully detected (i.e., hits) and the proportion of correct records misidentified as errors (i.e., false alarms). In addition, two different measures of discrimination were used. In signal detection theory, discrimination is usually based on several different trials for each subject, where different incentives are applied to manipulate the response criterion and produce a collection of hit rate/false alarm rate pairs. In this experiment there is only a single hit rate/false alarm rate pair for each subject. We use a technique from signal detection theory that estimates both the maximum possible and the minimum possible discrimination given a single hit rate/false alarm rate pair, and takes the average of the two (McNicol 1972; Norman 1964; Pollack et al. 1964). This measure will be called Discrimination $_{SD}$ (based on Signal Detection Theory). Discrimination $_{SD}$ varies from .5, which is random performance, to 1.0 which is perfect performance. See Appendix A for more detail.

Because $Discrimination_{SD}$ is only an estimate of the true discriminability, we also use a second measure of discrimination from behavioral decision research (Yates 1990), in which discrimination is conceptualized as the extent to which items are correctly sorted. For example, a person asked to separate defective and perfect items exhibits perfect discrimination if all defective items are placed in one pile and all perfect items are placed in a second pile. The worst possible discrimination occurs if the proportion of defective items placed in each pile is equal to the base rate of defective items in the set of items being sorted. Yates' measure of discrimination, called Discrimination $_{BD}$ (based on Behavioral Decision Theory) in this study, is based on the extent to which the proportion of defective items in each pile deviates from the base rate. In this study, Discrimination $_{BD}$ varies from 0, which is random performance, to .23 which is perfect performance. See Appendix A for more detail.

## Subjects

Students from upper-level undergraduate and MBA business courses participated in the experiments. Students were used because they are less likely to have beliefs about the likelihood of errors in data than experienced professionals. The use of experienced professionals with domain-specific expectations could confound the manipulation of the expectations about the base rate of errors.

## Experiment 1: Impact of Base Rates and Incentives

The first experiment addresses propositions 1 and 2: Do expectations about the base rate of errors and incentive structures affect error detection performance? All of the subjects in this experiment were explicitly instructed to check the data for errors and to prepare a memo for the client indicating any errors found.

## Experimental treatments

The experimental treatments for experiment 1 divided subjects into four incentive structures and three base rate expectations (see Table 1).

Expectations about the base rate of errors. The expectation construct was operationalized using a short memo given to subjects as part of their preparation for the pension calculation task. In the high base rate condition, the memo stated that the clients for whom the subjects would be performing the accrued pension calculation task tend to provide data containing a lot of errors. In the low base rate condition, the memo stated that the clients for whom the subjects would be performing the accrued pension calculation task tend to provide data mostly free of errors. No mention of the accuracy of the data provided by the clients in the past is made in the memo read by subjects in a control condition.

Incentive structures. Instructions to the subjects at the beginning of the experiment were used to operationalize the incentive structure construct. In addition, the operative incentive scheme was prominently displayed on an overhead projector screen throughout the experiment. All incentives involved the necessary conditions for subjects being included in a lottery for \$100. Subjects had an a priori chance of one in 18 of winning the prize, making these incentives salient to them.

Table 1. Experimental Design for Experiment 1

<table><tr><td></td><td colspan="3">Expectations About the Base Rate of Errors</td></tr><tr><td>Incentive Structures</td><td>High</td><td>Low</td><td>Control(No Information)</td></tr><tr><td>1. Detection</td><td></td><td></td><td></td></tr><tr><td>2. Pension Calculation</td><td></td><td></td><td></td></tr><tr><td>3. Detection With False Alarm Penalty</td><td></td><td></td><td></td></tr><tr><td>4. Control (Random)</td><td></td><td></td><td></td></tr></table>

In the detection, pension calculation, and detection with false alarm penalty conditions, subjects were told that their performance on the task would be evaluated and that 30% of subjects with the best performance would be entered into a lottery from which one person would receive \$100. Subjects in the detection and detection with false alarm penalty conditions were told that performance on the confirmation memo would be weighted three times as heavily as performance on the accrued pension calculations, while subjects in the pension calculation condition were told that performance on the accrued pension calculations would be weighted three times as heavily as performance on the confirmation memo.

Instructions for the detection with false alarm penalty condition noted that there is a significant cost to the client for determining whether each item noted as an error in the confirmation memo is in fact incorrect. Subjects in this condition were told that both the number of errors noted and the amount of unnecessary costs incurred by the client would be considered in the evaluation of the quality of their confirmation memos.

The \$100 prizes were not contingent on task performance in the control condition. Subjects in this group were told that everyone who conscientiously participated in the experiment would be entered into a lottery from which one person would receive \$100.

Prizes were awarded within each of the twelve cells of the experimental design (see Table 1). Three prizes were awarded to subjects in the control condition (one for each level of the expectations about the base rate factor). For the other nine cells, the performance of all subjects with a given level of the expectations of the base rate factor and a given level of the incentive structure factor was evaluated, and subjects with performance in the top 30% were entered into a lottery.

## Experimental design

As noted, there are four levels of the incentive structure factor and three levels of the expectations of the base rate of errors factor. Subjects were randomly assigned to the twelve conditions (see Table 1). A power analysis suggested that a sample size of 18 observations per condition would be sufficient to detect an effect size equal to one standard deviation of the distribution of the dependent variables with a power of .95. This gave a total of 216 observations.

## Experiment 1 results

Table 2 presents the results of a standard ANOVA for each of the four dependent variables. No departures from the assumptions of independence of error terms, normality of error terms, and equality of population variances were detected. Additionally, no outliers were detected (Neter et al. 1990).

No main effects of the base rate expectations factor were found, although the power of these tests is greater than .98. Main effects of the incentive structure factor on hits, Discrimination $_{SD}$ and Discrimination $_{BD}$ were found. These results suggest that incentive structures have an effect on error detection performance. No statistically significant effect of incentive structures on false alarms was found. The power of this test is greater than .98. The factor level means showing the effect of the incentive structure factor on each of the four dependent variables are shown in Table 3.

The Tukey method of multiple comparisons was used to conduct pairwise comparisons of the incentive structure factor level means for each dependent variable (Neter et al. 1990). Using a family confidence coefficient of .95, it was concluded that (1) the hit rate of subjects in the detection condition is significantly greater than the hit rate of subjects in the pension calculation, detection with false alarm penalty, and control conditions and (2) the hit rate of subjects in the pension calculation condition is significantly greater than the hit rate of subjects in the control condition.

Table 2. Performance Affected by Incentive Structure

<table><tr><td></td><td>Hits</td><td>False Alarms</td><td> $Discrimination_{SD}$ </td><td> $Discrimination_{BD}$ </td></tr><tr><td>Main Effect of Incentive Structure</td><td>Yes(p=.0001)</td><td>No</td><td>Yes(p=.0053)</td><td>Yes(p=.0001)</td></tr><tr><td>Main Effect of Base Rate Expectations</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Interaction Effect</td><td>No</td><td>No</td><td>No</td><td>No</td></tr></table>

The Discrimination $_{SD}$ scores shown in Table 3 range from .81 to .86. A score of .50 reflects a complete lack of discrimination (i.e., random performance) and a score of 1.0 reflects perfect discrimination. Discrimination $_{SD}$ scores greater than .80 are generally considered to reflect good discrimination. The Tukey method of multiple comparisons was used to conduct pairwise comparisons of the incentive structure factor level means for Discrimination $_{SD}$ (Neter et al. 1990). Using a family confidence coefficient of .95 it was concluded that the discrimination of subjects in the detection condition is significantly better than the discrimination of subjects in the control condition and the detection with false alarm penalty condition. Results for Discrimination $_{BD}$ are similar to the results for Discrimination $_{SD}$ .

In addition to testing the research propositions, we performed an exploratory analysis of the kinds of errors that were detected by the subjects. We divided the 36 errors that were embedded in the employee records into three categories: (1) errors in information about an employee (e.g., incorrect ages and birthdates), (2) errors in information about employment dates (e.g., incorrect hire dates), and (3) errors in information related to salaries (e.g., incorrect pay rates). Table 4 shows the number of errors in each of the three categories and the average percent of subjects in the first experiment detecting these kinds of errors across all of the experimental conditions. For example, on average, each of the eight “employee information” errors was found by 31.8% of the subjects.

An analysis of whether errors encountered at the beginning of the experimental session were more likely to be detected than errors encountered later in the session was also conducted. Errors in the first and second spreadsheets encountered by the subjects were equally likely to be detected. Additionally, a relationship between the likelihood of error detection and the part of a spreadsheet in which a data error appears was not found.

## Experiment 2: Explicit Error Detection Goals

A second laboratory experiment was conducted to examine proposition 3, the impact of explicit error detection goals on error detection performance. A total of 72 students from upper-level undergraduate and MBA business courses participated in the experiment. $^{2}$

## Experimental treatment

For this experiment there was one independent variable, error detection goals, with two levels: (1) explicit error detection goals and (2) implicit error detection goals. Subjects were randomly assigned to a level of this factor. The error detection goal construct was operationalized through directions to the subjects. Subjects in the explicit error detection goal condition read the following instructions:

Table 3. Performance Increased With Detection and Pension Calculation Incentives

<table><tr><td></td><td colspan="4">Incentive Structures</td></tr><tr><td></td><td>Detection</td><td>Pension Calculation</td><td>Detection With False Alarm Penalty</td><td>Control</td></tr><tr><td>Hitsa</td><td>20.0 (.56)</td><td>16.0 (.44)</td><td>13.8 (.38)</td><td>12.2 (.34)</td></tr><tr><td>False Alarmsb</td><td>3.1 (.05)</td><td>2.4 (.04)</td><td>1.6 (.03)</td><td>1.5 (.02)</td></tr><tr><td>DiscriminationSD</td><td>.86</td><td>.83</td><td>.81</td><td>.81</td></tr><tr><td>DiscriminationBD</td><td>.0854</td><td>.0664</td><td>.0597</td><td>.0511</td></tr></table>

$^{a}$ Each cell in this row gives the mean number of hits followed by the mean hit rate in parentheses. $^{b}$ Each cell in this row gives the mean number of false alarms followed by the mean false alarm rate.

Table 4. Performance Affected by Error Type

<table><tr><td>Error Type</td><td>Number of Errors in Category</td><td>Average Percent of Subjects Detecting Error</td></tr><tr><td>Employee Information</td><td>8</td><td>31.8</td></tr><tr><td>Employment Dates</td><td>17</td><td>43.8</td></tr><tr><td>Salary Information</td><td>11</td><td>49.9</td></tr></table>

Errors are sometimes found in the data provided by our clients. When errors are found, a memo should be prepared to be sent to the client so that the client can provide any necessary instructions.

These instructions are identical to the instructions read by all of the subjects in the first experiment. Subjects in the implicit error detection goal condition read the following instructions:

Past experience has shown that computer-printed reports are too frequently accepted without question. Be sure to circle any parts of the reports which you feel are questionable.

These implicit instructions are identical to instructions given to subjects in the experiment conducted by Ricketts (1990) in which over

90% of the subjects failed to detect an error in data.

## Experiment 2 results

The effect of explicit error detection goals on error detection performance was analyzed using a standard ANOVA model for a one-factor experiment, with a separate model for each of the four dependent variables. A main effect for explicit error detection goals was found for hits (p = .0001), for false alarms (p = .0024), and for both measures of discrimination (p = .0001 for both measures). The factor level means showing the effect of explicit error detection goals on each of the four dependent variables are shown in Table 5.

An analysis of the residuals was conducted to determine whether the ANOVA models are appropriate for the data collected in Experiment 2 (Neter et al. 1990). A departure from the assumption of normality of error terms was detected for all four of the ANOVA models. Additional tests concerning differences between proportions were therefore conducted. These non-parametric tests are not affected by nonnormality of error terms.

Table 5. Performance Increased With Explicit Goal

<table><tr><td></td><td>Explicit Goal</td><td>Implicit Goal</td></tr><tr><td>Hitsa</td><td>11.0 (.31)</td><td>2.3 (.07)</td></tr><tr><td>False Alarmsb</td><td>0.9 (.03)</td><td>0.2 (.01)</td></tr><tr><td>DiscriminationSD</td><td>.79</td><td>.56</td></tr><tr><td>DiscriminationBD</td><td>.0464</td><td>.0102</td></tr></table>

$^{a}$ Each cell in this row gives the mean number of hits followed by the mean hit rate in parentheses.  
$^{b}$ Each cell in this row gives the mean number of false alarms followed by the mean false alarm rate.

Table 6 shows the number and percentage of subjects in each experimental condition with zero hits and with one or more hits. The conclusion from a test of the difference between these two population proportions (McClave and Benson 1994) is that the two proportions are not equal (p < .001). Thus there is a relationship between the explication of error detection goals and the hit rate.

Table 6. Hit Rate Increased With Explicit Goal

<table><tr><td></td><td>Hits = 0</td><td>Hits &gt; 0</td></tr><tr><td>Explicit Goal</td><td>2 (5.6%)</td><td>34 (94.4%)</td></tr><tr><td>Implicit Goal</td><td>28 (77.8%)</td><td>8 (22.2%)</td></tr></table>

Using a similar analysis, we conclude that there is a relationship between the explication of error detection goals and the false alarm rate, significant at .001, as shown in Table 7.

Table 7. False Alarm Rate Increased With Explicit Goal

<table><tr><td></td><td>FAs = 0</td><td>FAs &gt; 0</td></tr><tr><td>Explicit Goal</td><td>19 (52.8%)</td><td>17 (47.2%)</td></tr><tr><td>Implicit Goal</td><td>33 (91.7%)</td><td>3 (8.3%)</td></tr></table>

Table 8 shows the number and percentage of subjects in each experimental condition with Discrimination $_{SD}$ scores greater than and less than .76, the median Discrimination $_{SD}$ score across both experimental conditions. A test of the difference between these two population proportions shows that there is a relationship between the explication of error detection goals and discrimination as measured by Discrimination $_{SD}$ (p < .001).

Table 8. Discrimination $_{SD}$ Increased With Explicit Goal

<table><tr><td></td><td>DiscriminationSD&lt;.76</td><td>DiscriminationSD&gt;.76</td></tr><tr><td>Explicit Goal</td><td>7 (19.4%)</td><td>29 (80.6%)</td></tr><tr><td>Implicit Goal</td><td>30 (83.3%)</td><td>6 (16.7%)</td></tr></table>

Table 9 shows the number and percentage of subjects in each experimental condition with Discrimination $_{BD}$ scores greater than and less than .0127, the median Discrimination $_{BD}$ score across both experimental conditions. A test of the difference between these two population proportions shows that there is a relationship between the explication of error detection goals and discrimination as measured by Discrimination $_{BD}$ (p < .001).

## Discussion of Experimental Results

The results relative to the three research propositions are summarized in Table 10.

Table 9. Discrimination $_{BD}$ Increased With Explicit Goal

<table><tr><td></td><td>Discrimination $_{BD}$ &lt;.0127</td><td>Discrimination $_{BD}$ &gt;.0127</td></tr><tr><td>Explicit Goal</td><td>6 (16.7%)</td><td>30 (83.3%)</td></tr><tr><td>Implicit Goal</td><td>30 (83.3%)</td><td>6 (16.7%)</td></tr></table>

In general, there is strong evidence that incentives for hits had an impact on discriminability, and a suggestion that they also had an impact on the response criterion. For the strongest incentive condition, hits and discriminability were statistically greater than the control condition; false alarms were greater, although not in a statistically significant amount. For the middle level of incentives, hits, false alarms, and discrimination all fell in the middle range between the control and the strongest incentive condition. False alarms were rather rare and differences due to different incentives did not achieve statistical significance. However, the pattern of increased hits and increased false alarms simultaneously is suggestive of a response criterion shift.

There was also strong evidence of the impact of explicit goals. Both hits and false alarms increase in a statistically significant fashion with explicit goals, indicating a clear response criterion shift. In addition, the increase in discrimination due to explicit goals was statistically significant.

However, the findings were not as predicted in three specific respects, to be discussed below. First of all, there was no support for proposition 1 (impact of expected base rate of errors).

The two relevant questions from the manipulation check questionnaire administered after the experiment suggest that the expectations may have only been weakly manipulated. For one question there is no statistically significant difference between the conditions. For another question, there is a statistically significant difference, but the mean scores for all conditions fall in the middle of a five point scale and range from 2.8 to 3.5. It is also possible that any early expectations about base rates were quickly revised by the subjects' experience as they found numerous errors in the data early in the experimental session. It appears that the base rate expectations were either very quickly disconfirmed or were never successfully manipulated. Thus no conclusions should be drawn about the impact of expected base rates on error detection performance.

A second finding not in line with predictions was the impact of the "detection with false alarm penalty" incentive condition, which rewarded subjects for hits while penalizing them for false alarms. We had expected that such an incentive scheme would prevent a shift in the response criterion, but increase discrimination. While it seems to have accomplished the first of these, it did not accomplish the second: subjects in this condition had no more hits, no more false alarms, and no discernible increase in discrimination over the subjects in the control condition. The admonition to avoid false alarms seems to have overpowered the incentive for hits. Instructions given to subjects in this condition indicated that the cost incurred because of a false alarm was no greater than the benefit of an extra hit, but it may be that the saliency of the "significant cost" of false alarms was much greater than the saliency of the benefits of hits. This could have created such a strong incentive to avoid false alarms that subjects refused to shift their response criteria or to take risks by attempting to discriminate more carefully. Only the most glaring errors would be reported under such conditions. It remains for future research to determine whether it is generally true that an admonition against false alarms will have the same chilling effect on error detection performance it had here.

Table 10. Summary of Results for Research Propositions

<table><tr><td>Error Detection Performance Will Be Influenced By:1. Expectations about the base rate of errors.2(a). Payoffs for hits.</td><td>Research ResultsConclusions not possible.Increase in discriminability and some evidence of response criterion shift.</td></tr><tr><td>2(b). Penalties for false alarms.</td><td>No increase in discriminability and no change in the response criterion.</td></tr><tr><td>3. Explicit error detection goals.</td><td>Strong support for increases in performance.</td></tr></table>

The third finding not in line with predictions was that, although experiment 2 showed a clear shift in the response criterion due to explicit goals, experiment 1 showed only a non-statistically significant shift in the response criterion due to incentives. While incentives increased hits in a statistically significant fashion, and at the same time increased false alarms, the increase in false alarms was not statistically significant. Thus there is a suggestion that the response criterion changed due to greater incentives, but no solid evidence. To investigate this further in an exploratory mode, a nonparametric analysis similar to that used in testing the impact of explicit goals on false alarms was performed. Table 11 shows the number of subjects in each level of the incentive structure factor in experiment 1 with zero false alarms and with one or more false alarm.

Table 11. False Alarm Rate Affected by Incentive Structure

<table><tr><td></td><td>FAs = 0</td><td>FAs &gt; 0</td></tr><tr><td>Detection</td><td>15</td><td>39</td></tr><tr><td>Pension Calculation</td><td>16</td><td>38</td></tr><tr><td>Detection with False Alarm Penalty</td><td>22</td><td>32</td></tr><tr><td>Control</td><td>29</td><td>25</td></tr></table>

The conclusion from a test of the difference between these population proportions (McClave and Benson 1994) is that the proportions are not equal (p < .05). Thus, overall there is a relationship between incentives and the false alarm rate. A further test shows that the relationship between incentives and false alarms disappears when the control group is excluded from the analysis. Taken together the two tests suggest that an absence of incentives to detect data errors (i.e., the control condition) minimizes the false alarm rate but that there is not a significant difference in the false alarm rates of subjects influenced by the other three incentive structures.

## Conclusion

There are two major findings from this research. The first is strong evidence (contrary to the current wisdom in the information systems literature) that humans do seem to be able to detect errors under certain circumstances. The second is support for the model of human error detection behavior including the following components: (1) a "discomfort index" response criterion and a critical value used in deciding if a record is correct or errorful, (2) the critical value can be shifted based on perceived incentives and expected base rates, and (3) the ability of humans to improve their discriminability by exerting greater effort. This model has encouraging support from the data.

Of particular practical importance, these results suggest that prior studies that concluded that users of information systems cannot be counted on to detect errors may have overgeneralized their results. Under more general conditions, individuals can detect data errors and their error detection performance responds to explicit goals and incentives in expected ways. More specifically, we have reproduced the results found by Ricketts (1990) but shown that these are representative of the special case where the error detection goal is only implicit in the task. When error detection is made an explicit goal, subjects respond by shifting their response criteria and by devoting greater effort to the error detection task, thereby improving discriminability. Furthermore, when error detection is an explicit goal, subjects respond to incentives by adjusting effort (and resulting discriminability) to maximize payoff. In addition, there is a suggestion that subjects also shift their response criteria in reaction to incentives, but this latter effect did not achieve statistical significance.

This study specifically focused on data accuracy, which is one of several types of data deficiencies that researchers have noted in the data quality literature. The findings may well generalize to the detection of problems of data consistency and data currency. However, it is likely that the findings are not generalizable to the recognition of problems of data completeness.

This paper began with an example of a clerk calculating pension benefits for a person who apparently joined a firm at age 14. The question posed was, would your clerk flag the record as a possible error? The empirical evidence presented here suggests that you shouldn't rule out the ability of your clerk to flag this kind of error, especially if you can modify his or her goals and incentives. Although it would be rash to rely on the findings of a single study as the basis of specific advice to your staff of clerks, it is possible to project what such advice might look like, should the findings here be replicated in future studies. Attempting to articulate such advice also highlights questions that need to be resolved by future research, if we are to confidently design the most effective data quality program.

Our assumption is that human-based error detection and system-based error detection should be integrated. In particular, all worker-detected errors should be studied to identify the generic types and, as appropriate, rules should be entered into the automated error detection schemes to incorporate these newly found error types. To make that integrated system work effectively:

1. The clerks need to know that it is a part of their job to look for and flag suspicious data.

2. Presumably, the clerks should be made aware of the different likelihood of errors in the different sources of data they use. However, there is no evidence yet that workers can take advantage of base rate information in fine tuning their behavior.

3. Ideally, you would like to focus the clerks' attention on errors that had an important impact, rather than inconsequential errors. However, there is no evidence yet that workers can incorporate information about different kinds of errors with different levels of seriousness (i.e., can they focus on and find certain kinds of serious errors and not waste time on others).

4. The clerks need to have some explicit incentive scheme that rewards them for finding errors. However, it is not clear what types of explicit rewards are most cost effective, for example, public recognition, immediate monetary reward, or part of performance review.

5. A finely tuned incentive scheme would take into account how difficult different types of errors are to find and use that and the expected organizational impact to adjust incentives. However, there is as yet no research on this topic.

6. Until evidence is found to the contrary, these findings suggest that there should be no penalty or special attention paid to the time lost or other costs due to false alarms, since this could perhaps discourage all error flagging activities. This inability to curb false alarms is potentially very daunting to managers who might worry about huge extra costs if numerous "false alarms" begin to occupy workers' time.

7. Presumably there are some individual characteristics that are associated with better error detection performance. These could be the basis of training programs or hiring programs. However, there is as yet no research on this topic.

Again, this single study should not be used as a guide to practice. However, the results reported here suggest that new studies built on the premise that users of information systems can detect errors in data are worthwhile. Numerous research directions are implied in the above list of potential guidelines and unanswered questions.

We would make one final comment to summarize and place the results reported here in context. There has been plenty of research about human behavior establishing the notion that humans respond to incentives and goals in general. However, the reigning view expressed in MIS research has been that most humans do not detect errors in data. The quote in the introduction of this paper from the MIS Quarterly's executive overview for the Ricketts (1990) paper captures this view nicely: "MIS management had better not rely on users to detect errors in computer outputs." What our findings do is make a strong case that error detection should be considered within the realm of what is known about human behavior in general. Since errors exist in organizational databases, human error detection is important. Researchers can now proceed to investigate this important topic, using accumulated knowledge about human behavior as a basis for further study.

## Acknowledgements

We would like to thank the associate editor, three anonymous reviewers, Glenn Browne, John Campbell, Fred Davis, and Bill Fox for their many comments and suggestions about this study.

## References

Agmon, N. and Ahituv, N. "Assessing Data Reliability in an Information System," Journal of Management Information Systems (4:2), 1987, pp. 34–44.

Baker, E. M. and Schuck, J. R. "Theoretical Note: Use of Signal Detection Theory to Clarify Problems in Evaluating Performance in Industry," Organizational Behavior and Human Performance (13:3), 1975, pp. 307–317.

Ballou, D. P. and Pazer, H. L. "The Impact of Inspector Fallibility on the Inspection Policy

in Serial Production Systems," Management Science (28:4), 1982, pp. 387–399.

Ballou, D. P. and Pazer, H. L. "Modeling Data and Process Quality in Multi-Input, Multi-Output Information Systems," Management Science (31:2), 1985a, pp. 150–162.

Ballou, D. P. and Pazer, H. L. "Process Improvement Versus Enhanced Inspection in Optimized Systems," International Journal of Production Research (23:6), 1985b, pp. 1233–1245.

Ballou, D. P. and Pazer, H. L. "Cost/Quality Tradeoffs for Control Procedures in Information Systems," OMEGA: International Journal of Management Science (15:6), 1987a, pp. 509–521.

Ballou, D. P. and Pazer, H. L. "Designing Inspection Strategies for Uncertain Environments," Decision Sciences (18:2), 1987b, pp. 217–233.

Ballou, D. P. and Pazer, H. L. "Designing Information Systems to Optimize the Accuracy-Timeliness Tradeoff," Information Systems Research (6:1), 1995, pp. 51–72.

Ballou, D. P. and Tayi, G. K. "Methodology for Allocating Resources for Data Quality Enhancement," Communications of the ACM (32:3), 1989, pp. 320–329.

Ballou, D. P., Pazer, H. L., Belardo, S., and Klein, B. "Implications of Data Quality for Spreadsheet Analysis," Data Base (18:3), 1987, pp. 13–19.

Bansal, A., Kauffman, R. J., and Weitz, R. R. "Comparing the Modeling Performance of Regression and Neural Networks as Data Quality Varies: A Business Value Approach," Journal of Management Information Systems (10:1), 1993, pp. 11–32.

Biegel, J. E. "Inspection Errors and Sampling Plans," A.I.I.E. Transactions (6), 1974, pp. 281–287.

Bonnel, A. and Noizet, G. "Application of Signal Detection Theory to Perception of Differences in Line Length," Acta Psychologica (43:1), 1979, pp. 1–21.

Bowen, P. L. Managing Data Quality in Accounting Information Systems: A Stochastic Clearing System Approach, University Microfilms International, Ann Arbor, MI, 1992.

Butt, J. "Frequency Judgments in an Auditing-Related Task," Journal of Accounting Research (26), 1988, pp. 315–330.

Campbell, J. P. "Modeling the Performance Prediction Problem in Industrial and Organizational Psychology," in Handbook of Industrial and Organizational Psychology (2nd ed.), M. D. Dunnette and L. M. Hough (eds.), Consulting Psychologists Press, Inc., Palo Alto, CA, 1990, pp. 687–732.

Campbell, J. P. and Pritchard, R. D. "Motivation Theory in Industrial and Organizational Psychology," in Handbook of Industrial and Organizational Psychology, M. D. Dunnette (ed.), Rand McNally College Publishing Company, Chicago, 1976, pp. 63–130.

Christensen-Szalanski, J. J. J. and Beach, L. R. "Experience and the Base-Rate Fallacy," Organization Behavior and Human Performance (29:2), 1982, pp. 270–278.

Christensen-Szalanski, J. J. J. and Bushyhead, J. B. "Physicians' Use of Probabilistic Information in a Real Clinical Setting," Journal of Experimental Psychology: Human Perception and Performance (7:4), 1981, pp. 928–935.

Collins, R. D., Case, K. E., and Bennett, G. K. "The Effects of Inspector Error on Single Sampling Inspection Plans," International Journal of Production Research, (11), 1973, pp. 289–298.

Cradit, J. D., Tashchian, A., and Hofacker, C. F. "Signal Detection Theory and Single Observation Designs: Methods and Indices for Advertising Recognition Testing," Journal of Marketing Research (31:1), 1994, pp. 117–127.

Craig, A. "Signal Detection Theory and Probability Matching Apply to Vigilance," Human Factors (29:6), 1987, pp. 645–652.

Cryer, E. H., Bettman, J. R., and Payne J. W. "The Impact of Accuracy and Effort Feedback and Goals on Adaptive Decision Behavior," Journal of Behavioral Decision Making (3:1), 1990, pp. 1–16.

Davies, D. R. and Parasuraman, R. The Psychology of Vigilance, Academic Press, London, 1981.

Davis, G. B. and Olson, M. H. Management Information Systems: Conceptual Foundations, Structure, and Development,

2nd ed., McGraw-Hill Book Company, New York, 1985.

Davis, G. B., Neter, J., and Palmer, R. R. "An Experimental Study of Audit Confirmation," Journal of Accountancy (123:6), 1967, pp. 36–44.

Dorris, A. L. and Foote, B. L. "Inspection Errors and Statistical Quality Control: A Survey," A.I.I.E. Transactions (10:2), 1978, pp. 184–192.

"Executive Overview," MIS Quarterly (14:1), March 1990, p. 62.

Eysenck, M. W. and Eysenck, M. C. "Effects of Monetary Incentives on Rehearsal and on Cued Recall," Bulletin of the Psychonomic Society (15:4), 1980, pp. 245–247.

Fox, C., Levitin, A., and Redman, T. "The Notion of Data and Its Quality Dimensions," Information Processing & Management (30:1), 1993, pp. 9–19.

Gaba, A. and Winkler, R. L. "Implications of Errors in Survey Data: A Bayesian Model," Management Science (38:7), 1992, pp. 913–925.

Garfinkel, R. S., Kunnathur, A. S., and Liepins, G. E. "Optimal Imputation of Erroneous Data: Categorical Data, General Edits," Operations Research (34:5), 1986, pp. 744–751.

Gigerenzer, G., Hell, W., and Blank, H. "Presentation and Content: The Use of Base Rates as a Continuous Variable," Journal of Experimental Psychology: Human Perception and Performance (14:3), 1988, pp. 513–525.

Ginossar, Z. and Trope, Y. "Problem Solving in Judgment Under Uncertainty," Journal of Personality and Social Psychology (52:3), 1987, pp. 464–473.

Green, D. M. and Swets, J. A. Signal Detection Theory and Psychophysics, Wiley, New York, 1966.

Grether, D. M. "Bayes Rule as a Descriptive Model: The Representativeness Heuristic," The Quarterly Journal of Economics (95:3), 1980, pp. 537–557.

Guzzo, R. A., Jette, R. D., and Katzell, R. A. "The Effects of Psychologically Based Intervention Programs on Worker Productivity: A Meta-Analysis," Personnel Psychology (38:2), 1985, pp. 275–291.

Ham, J., Losell, D., and Smieliauskas, W. "An Empirical Study of Error Characteristics in Accounting Populations," The Accounting Review (60:3), 1985, pp. 387–406.

Henry, R. A. and Strickland, O. J. "Performance Self-Predictions: The Impact of Expectancy Strength and Incentives," Journal of Applied Social Psychology (24:12), 1994, 1056–1069.

Hicken, S., Sullivan, H., and Klein, J. "Learner Control Modes and Incentive Variations in Computer-Delivered Instruction," Educational Technology Research and Development (40:4), 1992, pp. 15–26.

Hollenbeck, J. and Klein, H. "Goal Commitment and the Goal-Setting Process: Problems, Prospects, and Proposals for Future Research," Journal of Applied Psychology (72:2), 1987, pp. 212–220.

Huh, Y. U., Keller, F. R., Redman, T. C., and Watkins, A. R. "Data Quality," Information and Software Technology (32:8), 1990, pp. 559–565.

Janson, M. "Data Quality: The Achilles Heel of End-User Computing," OMEGA: International Journal of Management Science (16:5), 1988, pp. 491–502.

Jenkins, D. C. "Financial Incentives," in Generalizing from Laboratory to Field Settings, E. A. Locke (ed.), Lexington Books, Lexington, MA, 1986, pp. 167–180.

Jerison, H. J. "Signal Detection Theory in the Analysis of Human Vigilance," Human Factors (9:3), 1967, pp. 285–288.

Johnson, E. J. and Payne, J. W. "Effort and Accuracy in Choice," Management Science (31:4), 1985, pp. 395–414.

Johnson, J. R., Leitch, R. A., and Neter, J. "Characteristics of Errors in Account Receivable and Inventory Audits," The Accounting Review (56:2), 1981, pp. 270–293.

Kahneman, D. and Tversky, A. "On the Psychology of Prediction," Psychological Review (80:4), 1973, pp. 237–251.

Kassin, S. M. "Base Rates and Prediction: The Role of Sample Size," Personality and Social Psychology Bulletin (5:2), 1979, pp. 210–213.

Klein, B. D. "End User Detection of Errors in Data: Preliminary Findings and an Experimental Study," Proceedings of the

Northeast Decision Sciences Institute 1995 Annual Meeting, Providence, RI, March 1995, pp. 227–229.

Klein, B. D. "Error Detection and Correction in Actuarial Data," Proceedings of the 1996 Information Resources Management Association International Conference, Washington, D.C., May 1996, pp. 73–79.

Knight, B. "The Data Pollution Problem," Computerworld (26:39), 1992, pp. 81–83.

Koehler, J. J. "The Base Rate Fallacy Reconsidered: Descriptive, Normative, and Methodological Challenges," Behavioral and Brain Sciences (19:1), 1996, pp. 1–53.

Koppell, S. "Decision Latencies in Recognition Memory: A Signal Detection Theory Analysis," Journal of Experimental Psychology: Human Learning & Memory (3:4), 1977, pp. 445–457.

Latham, G. P. and Yukl, G. A. "A Review of Research on the Application of Goal Setting in Organizations," Academy of Management Journal (18:4), 1975, 824–845.

Laudon, K. C. "Data Quality and Due Process in Large Interorganizational Record Systems," Communications of the ACM (29:1), 1986, pp. 4–11.

Lee, C. "The Effects of Goal Setting and Monetary Incentives on Self-Efficacy and Performance," Journal of Business and Psychology (2:4), 1988, pp. 366–372.

Levi, K. "A Signal Detection Framework for the Evaluation of Probabilistic Forecasts," Organizational Behavior and Human Decision Processes (36:2), 1985, pp. 143–166.

Locke, E. A. and Latham, G. P. Goal Setting: A Motivational Technique That Works, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1984.

Locke, E. A. and Latham, G. P. "Work Motivation and Satisfaction: Light at the End of the Tunnel," Psychological Science (1:4), 1990, pp. 240–246.

Locke, E. A., Feren, D. B., McCaleb, V. M., Shaw, K. N., and Denny, A. T. "The Relative Effectiveness of Four Methods of Motivating Employee Performance," in Changes in Working Life, K. Duncan, M. Gruneberg, and D. Wallis (eds.), Wiley, New York, 1980, pp. 363–388.

Locke, E. A., Shaw, K. N., Saari, L. M., and Latham, G. P. "Goal Setting and Task Performance: 1969–1980," Psychological Bulletin (90:1), 1981, 125–152.

Lockhart, R. S. and Murdock, B. B. "Memory and the Theory of Signal Detection," Psychological Bulletin (74:2), 1970, pp. 100–109.

Madnick, S. E. and Wang, R. Y. "Introduction to the TDQM Research Program," Total Data Quality Management Research Program Working Paper #92-01, Boston, 1992.

Manis, M., Dovalina, I., Avis, N. E., and Cardoze, S. "Base Rates Can Affect Individual Predictions," Journal of Personality and Social Psychology (38:2), 1980, pp. 231–248.

Martin, B. A. and Murberger, M. A. "Effects of Self-Esteem and Assigned Goals on Actual and Perceived Performance," Journal of Social Behavior and Personality (9:1), 1994, pp. 81–87.

McClave, J. T. and Benson, P. G. Statistics for Business and Economics, Dellen Publishing Company, San Francisco, 1994.

McNicol, D. A Primer of Signal Detection Theory, George Allen & Unwin Ltd., London, 1972.

Mento, A. J., Steel, R. P., and Karren, R. J. "A Meta-Analytic Study of the Effects of Goal Setting on Task Performance: 1966–1984," Organizational Behavior and Human Decision Processes (39:1), 1987, pp. 52–83.

Morey, R. C. "Estimating and Improving the Quality of Information in a MIS," Communications of the ACM (25:5), 1982, pp. 337–342.

Morrison, G. R., Ross, S. M., Gopalakrishnan, M., and Casey, J. "The Effects of Feedback and Incentives on Achievement in Computer-Based Instruction," Contemporary Educational Psychology (20:1), 1995, pp. 32–50.

Murdock, B. B. "Recognition Memory," in Handbook of Research Methods in Human Memory and Cognition, C. R. Puff (ed.), Academic Press, New York, 1982, pp. 2–26.

Naus, J. I. Data Quality Control and Editing, Marcel Dekker, Inc., New York, 1975.

Neter, J., Wasserman, W., and Kutner, M. H. Applied Linear Statistical Models, Irwin, Homewood, IL, 1990.

Nisbett, R. E. and Borgida, E. "Attribution and the Psychology of Prediction," Journal of Personality and Social Psychology (32:5), 1975, pp. 932–943.

Norman, D. A. "A Comparison of Data Obtained with Different False-Alarm Rates," Psychological Review (71:1), 1964, pp. 243–246.

O'Leary, D. E. "The Impact of Data Accuracy on System Learning," Journal of Management Information Systems (9:4), 1993, pp. 83–98.

O'Neill, E. T. and Vizine-Goetz, D. "Quality Control in Online Databases," in Annual Review of Information Science and Technology, M. E. Williams (ed.), Elsevier Science Publishers, Amsterdam, 1988, pp. 125–156.

Paradice, D. B. and Fuerst, W. L. "An MIS Data Quality Methodology Based on Optimal Error Detection," Journal of Information Systems (5:1), 1991, pp. 48–66.

Parsaye, K. and Chignell, M. "Data Quality Control with SMART Databases," AI Expert (8:5), 1993, pp. 23–27.

Pastore, R. E. and Scheirer, C. J. "Signal Detection Theory: Considerations for General Application," Psychological Bulletin (81:12), 1974, pp. 945–958.

Payne, J. W. "Contingent Decision Behavior," Psychological Bulletin (92:2), 1982, pp. 382–402.

Payne, J. W., Bettman, J. R., and Johnson, E. J. "Adaptive Strategy Selection in Decision Making," Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), 1988, 534–552.

Pollack, I., Norman, D. A., and Galanter, E. "An Efficient Non-Parametric Analysis of Recognition Memory," Psychonomic Science (1:1), 1964, pp. 327–328.

Redman, T. C. Data Quality: Management and Technology, Bantam Books, New York, 1992.

Redman, T. C. "Improve Data Quality for Competitive Advantage," Sloan Management Review (36:2), 1995, p. 99–107.

Ricketts, J. A. "Powers-of-Ten Information Biases," MIS Quarterly (14:1), 1990, pp. 63–77.

Roy, M. C. and Lerch, F. J. "Overcoming Ineffective Mental Representations in Base-Rate Problems," Information Systems Research (7:2), 1996, pp. 233–247.

Sinclair, M. A. "A Collection of Modelling Approaches for Visual Inspection in Industry," International Journal of Production Research (16:4), 1978, pp. 275–292.

Singh, S. N. and Churchill, G. A. "Using the Theory of Signal Detection to Improve Ad Recognition Testing," Journal of Marketing Research (23:4), 1986, pp. 327–336.

Stock, J. and Cervone, D. "Proximal Goal-Setting and Self-Regulatory Processes," Cognitive Therapy and Research (14:5), 1990, pp. 483–498.

Stone, M. and Bublitz, B. "An Analysis of the Reliability of the FASB Data Bank of Changing Price and Pension Information," The Accounting Review (59:3), 1984, pp. 469–473.

Svanks, M. I. "Integrity Analysis," Information and Software Technology (30:10), 1988, pp. 595–605.

Swets, J. A. "Measuring the Accuracy of Diagnostic Systems," Science (240:4857), 1988, pp. 1285–1294.

Teborg, J. R. "The Motivational Components of Goal Setting," Journal of Applied Psychology (61:5), 1976, pp. 613–621.

Thompson, S. C. "Detection of Social Cues: A Signal Detection Theory Analysis," Personality & Social Psychology Bulletin (4:3), 1978, pp. 452–455.

Wand, Y. and Wang, R. Y. "Anchoring Data Quality Dimensions in Ontological Foundations," Communications of the ACM (39:11), 1996, pp. 86–95.

Weber, E. U., Bockenholt, U., Hilton, D. J., and Wallace, B. "Determinants of Diagnostic Hypothesis Generation: Effects of Information, Base Rates, and Experience," Journal of Experimental Psychology: Learning, Memory, and Cognition (19:5), 1993, pp. 1151–1164.

Wright, P. M. "An Examination of the Relationships Among Monetary Incentives, Goal Level, Goal Commitment, and

Performance," Journal of Management (18:4), 1992, pp. 677–693.

Yates, J. F. Judgment and Decision Making, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1990.

Zmud, R. W. "An Empirical Investigation of the Dimensionality of the Concept of Information," Decision Sciences (9:2), 1978, pp. 187–195.

## About the Authors

Barbara D. Klein is an assistant professor of MIS at the University of Michigan-Dearborn. She received her Ph.D. in Information and Decision Sciences from the University of Minnesota and has published in Database and Information Resources Management Journal. Her research interests include data quality, errors in information retrieval, and the acquisition of database query skills.

Dale L. Goodhue is an assistant professor of MIS at the University of Georgia's Terry College of Business. He received his Ph.D. in MIS from MIT and has published in Management Science, MIS Quarterly, and Sloan Management Review. His research interests include measuring the impact of information systems, the impact of task-technology fit on performance, and the management of data and other IS infrastructures/resources.

Gordon B. Davis is Honeywell Professor of Management Information Systems, an endowed chair in the Carlson School of Management, University of Minnesota, and a professor of accounting. His doctorate is from Stanford University. He has honorary doctorates from the University of Lyon, France, and the University of Zurich, Switzerland. Professor Davis is the author of fifteen texts and numerous articles in management information systems, data processing, programming, and EDP auditing. His consulting, professional seminar teaching, and research interests include management of knowledge work; MIS planning; information requirements determination; the management information system: concepts, structure, and development; control and audit of information systems; and quality control for user-developed systems.

## Appendix A

## Measures of Discrimination

Two measures of discrimination are used in this investigation. The first measure is an estimate of a standard measure of discriminability from signal detection theory (McNicol 1972; Norman 1964; Pollack et al. 1964). The second measure is a measure of discrimination from behavioral decision theory (Yates 1990). The measure from signal detection theory is called Discrimination $_{SD}$ here, and the measure from behavioral decision theory is called Discrimination $_{BD}$ . Discrimination $_{SD}$ is discussed in the first section, and Discrimination $_{BD}$ is discussed in the second section.

## Discrimination $_{SD}$

All of the points on the curve in Figure A1 represent equivalent discriminability, but different response criteria. Figure A1 shows a pair of points representing different hit and false alarm rates. The performance represented by point a is attained by an increased willingness to report a signal compared to the performance represented by point b (McNicol 1972).

![](/api/attachments/JVSMAGF5/fulltext/images/69835fed1ed68ee991b6cba37333c7c379ccbfd7c2b036f4d8456343a8baf687.jpg)  
Figure A1. Receiver-Operating Characteristic Curve

The curve shown in Figure A1 is called a Receiver-Operating Characteristic (ROC) curve. A ROC curve always takes the convex shape shown in Figure A1 if the underlying distributions of noise and signal are normally distributed (McNicol 1972). The extent of overlap between the noise and signal distributions determines the area under a ROC curve. Thus, the area under a ROC curve is a measure of discriminability.

The area under a ROC curve for a particular subject can be determined if a number of points along a ROC curve are known. This can be done by controlling discriminability across a series of experimental trials and simultaneously manipulating a subject's response criterion. In this investigation, a within-subject manipulation of the response criterion was not made because this would have been detrimental to the critical realism of the experimental task. Thus, for each subject, there is only one hit rate and one false alarm rate.

The area under a ROC curve can be estimated when only one hit rate and one false alarm rate are known. The basis of this procedure is finding points in a unit square representing discriminability better than the observed performance, worse than the observed performance, and equivalent to the observed performance (McNicol 1972; Norman 1964; Pollack et al. 1964).

![](/api/attachments/JVSMAGF5/fulltext/images/c416373716624675d16674f7fdbc47ced7d748b99dc2c3e8af59eee3029eeb7d.jpg)  
Figure A2. Regions Representing Discriminability Better Than, Worse Than, and Equivalent to Point i

Point i in Figure A2 represents a known hit rate and a known false alarm rate. Figure A2 shows the unit square divided into four regions. A ROC curve containing point i cannot pass through the regions labeled "better" and "worse." The other two regions (labeled E1 and E2) contain points that do not necessarily represent a change in discriminability compared to point i. A ROC curve containing point i must be drawn completely inside the regions E1 and E2 (McNicol 1972). $^{3}$

The maximum possible area under a ROC curve that includes point i is given by:

$$
\text { Maximum   Area } = (E 1 + E 2 + \text { Worse }) / (E 1 + E 2 + \text { Worse } + \text { Better })
$$

The minimum possible area under a ROC curve that includes point i is given by:

$$
\text { Minimum   Area } = \text { Worse } / (E 1 + E 2 + \text { Worse } + \text { Better })
$$

Discrimination $_{SD}$ is equal to the average of the maximum possible area under the ROC curve and the minimum possible area under the ROC curve (Pollack et al. 1964).

## Discrimination $_{BD}$

The second measure of discrimination used in this investigation, $Discrimination_{BD}$ , is a discrimination index (Yates 1990). The discrimination index is a measure of the extent to which a subject is able to correctly categorize stimuli. In this investigation, subjects worked with two types of stimuli: records containing an error and records not containing an error. Subjects placed these stimuli into two categories: records reported as errors in the confirmation memo and records not reported as errors in the confirmation memo.

Consider a case in which a subject is completely unable to distinguish records containing an error from records not containing an error. In this case, we would expect the number of records correctly reported as containing an error in the confirmation memo divided by the total number of records reported in the confirmation memo to be equal to the base rate of errors. We would also expect the number of records containing an error but not reported in the confirmation memo divided by the total number of records not reported in the confirmation memo to be equal to the base rate of errors. The discrimination index is a measure of a subject's improvement over this complete lack of discrimination.

Figure A3 illustrates the definition of the four inputs (labeled A, B, C, and D) to the calculation of $Discrimination_{BD}$ .

![](/api/attachments/JVSMAGF5/fulltext/images/1cdba0a1ae55071d9df50996539503d140d383a23b7d9ab3e31b19b02ffc5a58.jpg)  
Figure A3. Inputs to the Calculation of Discrimination $_{BD}$

A is equal to the number of items reported as errors when an error exists, B is equal to the number of items not reported as errors when an error exists, C is equal to the total number of items reported as errors, and D is equal to the total number of items not reported as errors.

The three-step algorithm used to compute Discrimination $_{BD}$ is outlined below. The implementation of each step of the algorithm for a subject with perfect discrimination is also presented in italicized text.

Step 1. The number of items reported as errors that are actually errors (A) is divided by the number of items reported as errors (C). The base rate of errors in the population is then subtracted from this intermediate result. The resulting difference is first squared and then weighted by the total number of items reported as errors (C).

For a subject with perfect discrimination, A/C is equal to 1. When the base rate of errors in the population (.36) is subtracted from this intermediate result, we get .64. When this difference is squared and then weighted by the total number of items reported as errors (36), we get 14.75.

Step 2. The number of items not reported as errors that are actually errors (B) is divided by the number of items not reported as errors (D). The base rate of errors in the population is then subtracted from this intermediate result. The resulting difference is first squared and then weighted by the total number of items not reported as errors (D).

For a subject with perfect discrimination, B/D is equal to 0. When the base rate of errors in the population (.36) is subtracted from this intermediate result, we get -.36. When this difference is squared and then weighted by the total number of items not reported as errors (64), we get 8.29.

Step 3. The outcomes of the calculations in Step 1 and Step 2 are summed and the result is divided by the total number of items in the population (C+D).

When we add 14.75 and 8.29 and then divide this result by the total number of items in the population (100), we get .23. The upper bound of Discrimination $_{BD}$ (i.e., the value we get for a subject with perfect discrimination) is therefore .23.

In the extreme case in which no items are reported as errors (i.e., both A and C are equal to zero), Step 1 of the algorithm is skipped. Step 3 is changed to read "The outcome of the calculation in Step 2 is divided by the total number of items in the population." In the extreme case in which all items are reported as errors (i.e., both B and D are equal to zero), Step 2 of the algorithm is skipped. Step 3 is changed to read "The outcome of the calculation in Step 1 is divided by the total number of items in the population." In these two extreme cases, Discrimination $_{BD}$ is equal to zero, which correctly reflects a complete lack of discrimination.
