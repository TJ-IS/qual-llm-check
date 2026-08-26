---
otero_id: 24954
otero_key: "5GX2BXSX"
title: "The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process"
authors: "Teresa M. Shaft; Iris Vessey"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518196"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process

Teresa M. Shaft & Iris Vessey

To cite this article: Teresa M. Shaft & Iris Vessey (1998) The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process, Journal of Management Information Systems, 15:1, 51-78, DOI: 10.1080/07421222.1998.11518196

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518196

![](/api/attachments/5GX2BXSX/fulltext/images/ed3d7015438ea2c86acd31504115140cdd1f019c375f966830500a70f0a447b6.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/5GX2BXSX/fulltext/images/f40913092324574b374d59574b4c7c0bcb7e37875ad40bb9fe79bb8e61c06311.jpg)

Submit your article to this journal ↗

![](/api/attachments/5GX2BXSX/fulltext/images/afc2b4a3eaf832bfa84da53a26ee28361d5db40066fad64ddf3ac309aa09565b.jpg)

Article views: 4

![](/api/attachments/5GX2BXSX/fulltext/images/834f0ee3aca8c909f839e8044e85d0c2cb2c9d11f5f4a792a2bf7a1c3c737716.jpg)

View related articles ↗

# The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process

TERESA M. SHAFT AND IRIS VESSEY

TERESA M. SHAFT is an Assistant Professor of Management Information Systems at the University of Tulsa. She received her Ph.D. from the Pennsylvania State University in 1992. Her research interests include the cognitive processes used during systems development, knowledge-based systems, and the application of information systems to environmental management. She has published her research in a variety of journals including Information Systems Research, Data Base Advances, Behavior and Information Technology, International Journal of Software Engineering and Knowledge Engineering, and the Journal of Industrial Ecology.

IRIS VESSEY is Professor of Information Systems at Indiana University. She received her Ph.D. in information systems from the University of Queensland, Australia, in 1984. Her research interests center on evaluating emerging information systems technologies. Her teaching interests lie in systems analysis and design. Specifically, she is interested in the cognitive fit of representations, methodologies, and techniques to software development tasks and to the design of software, and in the role of the application in systems development. Other interests include the relationship between organizational structure and information systems infrastructures. She is also vitally concerned with the emergence of information systems as a discipline.

ABSTRACT: Recent research using professional programmers suggests that knowledge of the application domain plays a major role in the cognitive processes they use to understand computer programs. In general, programmers use a more top-down comprehension process when working in familiar application domains, and a more bottom-up process in unfamiliar domains. The present study builds on that research by further characterizing comprehension processes. The findings show that: (1) certain programmers use different types of comprehension processes depending on their familiarity with the application domain (flexible approach), while others do not (top-down and bottom-up approaches); (2) familiarity with the application domain and the use of a particular comprehension process have marked effects on references programmers make to both application and programming domain knowledge; and (3) programmers who use a flexible comprehension process achieved the highest levels of comprehension. The present research also examines some cognitive determinants of the comprehension process. The findings highlight the need to consider application, as well as programming, domain knowledge as areas of computer programming expertise, to investigate factors influencing use of specific comprehension processes, and to develop tools to support flexible comprehension processes.

KEY WORDS AND PHRASES: application domain, computer program comprehension, metacognition, program understanding, system maintenance.

UNDERSTANDING COMPUTER PROGRAMS IS CRUCIAL TO THE PERFORMANCE of many programming tasks; it plays a major role, for example, in the testing and debugging phases of program development and in the later program maintenance and enhancement phases. Further, in software maintenance, which consumes from 50 percent to 80 percent of information systems budgets [21], programmers spend 50 percent to 90 percent of their time understanding existing programs [10, 31].

Recent literature has begun to stress the importance of application domain knowledge to software $[5, 16]$ . By application domain knowledge, we mean knowledge of the problem area addressed by the computer program of interest. Most studies on application domain knowledge have investigated the early stages of systems development, analysis and design, stages in which application domain knowledge is expected to play its most significant role $[1, 11, 39]$ . Curtis, Krasner, and Iscoe $[11]$ conclude that “the thin spread of application domain knowledge” is one of the most salient problems in large-scale systems development. Futher, they state that “aggregating these [application domain] issues across behavioral levels [i.e., individual, team, project, and company] points to the importance of managing learning, especially of the application domain, as a major factor in productivity, quality, and costs.”

At first glance, we might expect application domain knowledge to have less impact in later stages of the software life cycle. Consider, however, the following story that was recounted to the authors: A university administrator received phone calls from irate parents demanding to know why their child was not admitted to the university while friends' children, with lower SAT/ACT scores had been admitted. Eventually the problem was traced to a program, written by an outside firm. The program sorted students' scores in ascending, rather than descending, sequence and prepared admission letters to students with lower, rather than higher scores. Imagine trying to explain to a parent that his or her child had been denied admission because the student earned high marks on the SAT. Worse, however, hundreds of admissions letters had been sent to students whose scores did not meet the university's admission requirements. Only one piece of domain knowledge was needed to properly program the sort that caused this huge error: the knowledge that high scores on SAT/ACTs are desirable. Clearly, then, knowledge of the application domain plays a significant role in all stages of development.

In this study we focus on program comprehension, which is crucial in the later stages of the development life cycle. Like the majority of researchers before us, by comprehension we mean, simply, understanding existing program code $[18, 41]$ . Although certain authors have noted differences in comprehension based on specific computer programs $[12, 36]$ , little or no attempt has been made to understand the implications of those differences. More recently, Shaft and Vessey $[35]$ report the findings of the first empirical study to address explicitly the influence of application domain knowledge on program comprehension. Their study demonstrated that the differences between two apparently conflicting theories of the comprehension process, the so-called top-down [8] and bottom-up theories [29], are due to differences in knowledge of the application domain.

While recent research has paid increasing attention to application domain knowledge, how such knowledge affects the program comprehension process has not been addressed. The objective of this paper is to characterize the effect of application domain knowledge and the accompanying comprehension processes, on program comprehension.

## Previous Research

COMPREHENSION RESEARCH, LIKE MOST SOFTWARE RESEARCH, HAS TYPICALLY focused on issues related to the programming domain, as opposed to the application domain [16]. For example, several studies sought and found evidence to support Brooks' top-down theory of comprehension by showing that programmers use "beacons" to verify hypotheses about program content [15, 41]. Beacons are "sets of features that typically indicate the occurrence of certain structures or operations in the code" [9, p. 549] and are therefore in the programming domain. Such investigations could therefore use short programs (approximately twenty source lines of code [SLOC]) that performed typical programming functions, such as searches or sorts, as well as student participants who possessed little or no application domain knowledge. These studies found support for Brooks's theory. Note, however, that although the theory is couched in terms of knowledge of "overall program function," which implies application domain knowledge, these studies tested it at an elementary programming level.

Curtis et al. [12] investigated comprehension as part of a larger investigation into the effectiveness of documentation formats. Professional programmers responded to comprehension questions after studying programs (of approximately 50 SLOC each) from three domains. Programmers' domain experience was not controlled. The effect due to a particular program was nearly as strong as the effect due to programmer differences and was significant for the three types of comprehension questions. This finding, together with the large program differences noted in their earlier studies [36], led the authors to conclude that a “taxonomy of application types might be helpful in explaining these differences” [12, p. 186].

Pennington [29, 30] focused on the mental representations that programmers developed as an outcome of comprehension. The program she used was larger than those used in previous experimental studies (200 SLOC) and domain-rich (the program kept track of and computed specifications for industrial plant designs). As in Curtis et al. [12], participants were professional programmers and application domain knowledge was not controlled. Pennington concluded that the types of knowledge structures programmers developed resulted from the use of a bottom-up comprehension process.

Letovsky [26] examined what he called cognitive events such as asking questions and conjecturing about the code, as the basis for developing a conceptual model of programmers' comprehension processes.

Shaft and Vessey [35] studied the role of application domain knowledge on the program comprehension process. They hypothesized that Brooks's top-down theory [8] and Pennington's bottom-up theory [29] might both be correct, but in different circumstances: Top-down comprehension processes are more likely when the programmer is familiar with the application domain; bottom-up processes are more likely when the programmer is unfamiliar with the application domain. Their thesis was verified in a study in which professional programmers studied programs in both familiar and unfamiliar application domains.

![](/api/attachments/5GX2BXSX/fulltext/images/1bb0f54a77df5b8c85d1593efbec1d7427dcaad6412e0457ed90795aacca36a6.jpg)  
Figure 1. Model of the Computer Program Comprehension Process

In summary, most (but not all) “programming” studies to date have used simple programs where knowledge of the application domain has not been an issue $[15, 16, 41, 42]$ . The use of small programs can be justified in theoretically based studies of the programming domain and in studies of the programming domain in which application domain knowledge is controlled. An objective of this study is to highlight the importance of carefully evaluating the appropriateness of using domain-free task materials to investigate any stage of the life cycle.

## The Current Study

FIGURE 1 PRESENTS OUR MODEL OF THE COMPREHENSION PROCESS. It is based on Letovsky's [26] view of programmers as "knowledge-based understanders." We developed and tested the model in a prior study [35]. An overview of the model is presented here for convenience. The model consists of essentially three components: (1) a knowledge base, comprised of both programming and application domain knowledge, (2) a mental model, which is the programmer's internal or mental representation of the computer program and the way in which it functions, and (3) the assimilation or comprehension process.

Our study seeks answers to four general research questions that are crucial to better understanding the comprehension process. Consistent with figure 1, the first two questions focus on characterizing knowledge of both the application and programming domains gained during comprehension. Although we know that knowledge of the application domain has an impact on the nature of the comprehension process used to understand a program $[35]$ , we do not know how that knowledge affects the type of knowledge heeded during comprehension. It would be interesting to know whether knowledge of the application domain compensates for knowledge of the programming domain. That is, do such programmers require less extensive programming training? To investigate these issues, we pose the following research question:

## Q1: Does familiarity with the application domain affect the knowledge programmers use in program comprehension?

Similarly, although familiarity with the application domain has been shown to influence a programmer's use of a particular process, little prior research has investigated how the use of a particular comprehension process influences the knowledge programmers use while studying a program. If a particular process influences the type of knowledge used, this implies, at some level, that certain processes allow programmers better access to certain types of knowledge. In this case, programmers who are adept at using particular processes could be assigned to tasks that require that knowledge; conversely, programmers could be taught to use particular processes when certain types of knowledge are required. To consider these issues, we pose the next research question:

## Q2: Does the comprehension process used affect the knowledge programmers use in program comprehension?

It is also important to investigate whether application domain knowledge and comprehension processes influence the effectiveness of comprehension. If application domain knowledge were found to improve comprehension, programmers with relevant domain knowledge would be expected to complete programming assignments more quickly and effectively than those without it, and managers could exploit this knowledge when assigning tasks. Similar arguments can be made with respect to the comprehension process. It is also possible that an interaction between application knowledge and comprehension process results in one enhancing or interfering with the other. We pose the following research question:

## Q3: Does familiarity with the application domain and/or the nature of the comprehension process influence the effectiveness of comprehension?

Finally, we consider the effect of cognitive determinants on the use of a particular comprehension process. For instance, the use of a meta-model to guide cognitive processes has been reported in a wide variety of situations $[13]$ . The use of meta-models, however, has received little attention in the context of software. To investigate these issues, we consider the following research question:

Q4: Does the use of a meta-model affect the type of comprehension process programmers use during program comprehension?

## Methodology

WE CONDUCTED A PROCESS TRACING STUDY IN WHICH PROGRAMMERS studied computer programs from two application domains, one familiar, the other unfamiliar. Concurrent verbal protocol analysis was used to examine the comprehension process because it provides a rich set of data about cognitive processes in a relatively natural working environment. (See [14] for an analysis of different process tracing methods.) To minimize potential validity problems, we trained subjects to provide verbal protocol data, instructed them only to “think aloud” during problem solving (and not to explain their thought processes), and did not probe for specific facts [32].

## Task Setting

Accounting was selected as the familiar application domain because of the ubiquitous nature of accounting systems and therefore the ease of identifying potential subjects. Hydrology was selected as the unfamiliar application domain because it is unrelated to accounting. Hence, it was relatively easy to identify subjects with accounting experience but no hydrology experience.

COBOL was the programming language investigated because of its predominance as a business programming language. An estimated $77 \times 10^{9}$ lines of COBOL code are in use in the United States [4]. Because such COBOL programs represent a significant corporate asset, the continued importance of knowledge concerning the comprehension of COBOL programs is assured for the foreseeable future.

## Subjects

Twenty-four information systems (IS) professionals employed in developing and/or maintaining COBOL accounting applications participated in the study. A background questionnaire was administered prior to the study to assess subjects' experience. The average participant was 36.5 years of age (range: 24–52), had 10.7 years experience as an IS professional (range: 3–20), and knew 5 programming languages (range: 1–11); 80 percent were men. The average self-reported score for COBOL knowledge was 4.7 on a five-point scale (range: 3–5). Job titles ranged from senior programmer to team leader. Accounting application domain knowledge was assessed via the number of accounting credit hours (average = 10.2 credit hours) and the number of years of experience in accounting applications (average = 6.7 years). No subject had experience in the hydrology domain.

## Experimental Materials

The experimental materials included computer programs and comprehension questions. The computer programs served as stimulus materials, while the comprehension questions were used to assess programmers' understanding of the computer programs.

## Computer Programs

The experiment required a program to familiarize participants with the experimental procedures and one each from the accounting and hydrology domains. The programs accessed all files sequentially and contained internal sorts. The practice program (99 SLOC, 33 in the PROCEDURE DIVISION) read and sorted an inventory file and prepared a report that listed inventory levels for all items.

The accounting program was a modified version of an operational payroll program that computed and produced paychecks, mailing labels, and a pay roster. The pay roster was organized by location and listed the name, social security number, budget code, gross pay, and net pay of each individual who received a paycheck. Modifications were made to facilitate comprehension by using more meaningful paragraph and variable names and reordering paragraphs.

The hydrology program was a modified version of an operational water quality management program that computed averages and variances for seven parameters (coliform, nitrate, chloride, lead, fluoride, pH, and alkalinity) based on test results. The report was organized by well identification number with the average, variance, and maximum value of test results printed for each month. Similar modifications were carried out to improve comprehension. Further changes were made because changes made over time had made the program difficult to understand.

It was important that the programs for the two domains be comparable based on an overall measure of comparability. However, most program metrics focus on only one of the many types of information embedded in a computer program (usually control flow or data flow $[43]$ ). Empirical studies indicate that counts of the number of SLOC, which do not focus on a single type of information, are highly correlated with other metrics and are as predictive of effort (e.g., programming, maintenance, etc.) as other measures $[24, 27]$ . The two major criticisms of SLOC as a metric are that it cannot be used to compare across programming languages and different counting standards can invalidate within-language comparisons $[23]$ . These criticisms are not relevant to this study, which used only one programming language. Hence, SLOC was used to assess the comparability of the two programs. Counts of SLOC were prepared using the standard presented in $[22]$ . The total counts for the accounting and hydrology programs were 417 and 416, respectively. Breakdowns based on DIVISIONS (IDENTIFICATION, ENVIRONMENT, DATA, and PROCEDURE) were 3, 20, 234, 160 for the accounting program and 3, 18, 233, 163 for the hydrology program, indicating comparability overall, and across divisions.

## Comprehension Questions

Two approaches are predominantly used to assess programmers' understanding of computer programs: free recall [36, 38] and responses to comprehension questions [12, 18, 29, 30]. Free recall requires a programmer to recall a program after a period of study. It therefore requires memorization, which may or may not involve understanding [6, 12], and can be used for only quite small programs. We therefore used questions to assess comprehension.

Two question sets were prepared for each application domain to minimize potential validity and reliability problems. Ten questions based on each of four different types of information (function, data flow, control flow, and state; see $[30]$ ) were constructed and randomly assigned to the two question sets such that each contained equal numbers of “yes” and “no” responses. The sequence in which the types of questions were presented was generated randomly and was the same in each set. The questions were tested with professional programmers in a pilot study, which resulted in minor wording changes. Participants were randomly assigned one of the question sets so that, after studying the program, half responded to each set. No systematic differences between the two question sets were detected.

Examples of the questions are presented below: The first two questions are from the accounting (familiar) domain; the second two from the hydrology (unfamiliar) domain. The first and third questions are correctly answered by “yes,” the second and fourth questions by “no.”

Are mailing labels created for each employee?

Does LOC-DL equal "NEW KENSINGTON" when ST-LOCATION equals "UP"?

Is OUTPUT-VALUES performed before OUT-MONTH-HEADERS?

Does the value of PARAM-TEST affect the value of TIME-MAX?

The reliability of the question sets was assessed via the Kuder-Richardson statistic (the special form of Cronbach's alpha for dichotomous variables). The average alpha was 0.72 (accounting domain: 0.75 and 0.60; hydrology domain: 0.83 and 0.71), which meets conventional levels of acceptability and compares favorably with the alphas reported in prior studies [12]. The robustness of the question sets is further supported by the fact that thirty items are generally necessary to achieve this level of reliability [28].

## Experimental Design

A within-subjects design, with application domain as the within-subjects factor, was used to examine the research questions. A within-subjects design is recommended in studies of computer programmers due to high levels of interprogrammer variability $[7]$ . Subjects rated their familiarity with the application domain after they studied each program. A paired t-test of differences showed that subjects were more familiar with the accounting domain than the hydrology domain (t = 5.84; p < 0.0001; df = 23).

## Experimental Procedure

We conducted a pilot study prior to the main study to test the experimental materials and procedures, and determine the length of the comprehension period. Based on the pilot study, programmers in the main study were permitted fifteen minutes to study each program.

Because concurrent verbal protocols were collected, subjects were run individually through the study. The experiment took place in three segments, a practice session (to familiarize participants with the process of thinking aloud and the experimental procedures), and two experimental sessions (one in each application domain). At the beginning of each segment, programmers were given a copy of the source code and asked to study the program to gain as complete an understanding of the program as the time allowed. At the end of each study period, programmers were asked to respond to a set of comprehension questions. The order of presentation of the two application domains was counterbalanced. Programmers were allowed a short break after each segment.

## Verbal Protocol Analysis

The coding categories and protocol analysis procedures are described below. The complete coder's manual is available from the first author.

## Coding Categories

Three categories of codes were needed to investigate the research questions: (1) whether certain statements were hypotheses or inferences; (2) the type of knowledge heeded during comprehension; and (3) the level of detail. Only those statements determined to be hypotheses or inferences were coded for type of knowledge and level of detail.

First, statements were categorized as hypotheses or inferences to distinguish between a more top-down and a more bottom-up comprehension process $[3, 8, 35]$ .¹ A more top-down process is hypothesis-driven and is therefore characterized by relatively more hypotheses than inferences. A hypothesis occurs when a programmer states an expectation about the purpose of the program based on limited information. It is usually stated in the form of a conjecture. In the following protocol segment,

1. Let's see, what are you doing.

2. MASTERFILE. Okay, looks like a payroll program.

3. This should be so much nicer.

the second statement of the protocol is a hypothesis because the programmer conjectures that the program processes payroll.

A more bottom-up process is inferential in nature and is therefore characterized by relatively more inferences than hypotheses. An inference occurs when a programmer builds up to some understanding based on examination of the computer program. Thus, an inference is usually stated in the form of a conclusion, as in the following example:

141. There's a MATCH-WELL-ID

142. If matched, if matched it checks to see if it matched again, of course, it's after it does FINISH-MONTH

143. Oh, it read another well.

144. So that test

145. So WORKING-STORAGE must be the prime

In the statements prior to statement 145, the programmer is examining conditional statements within the code. Based on that examination, he infers correctly (statement

145) that the purpose of a working-storage variable is the prime, or initial value, used to make comparisons.

Second, these statements were coded according to the type of knowledge they referenced: application or programming domain knowledge. In the first excerpt above, the critical statement (no. 2) involves application domain knowledge: The programmer refers to “payroll program,” indicating that the function of the program was to process payroll. This involved a translation from the programming domain to the application domain. In the second excerpt, the critical statement (no. 145) is assigned a code to indicate programming domain knowledge: The programmer refers to initializing a working-storage variable and there is no translation to the application domain.

Third, the statements were coded according to their level of detail. According to Brooks [8], a high-level reference is expected to occur more frequently with a top-down comprehension process, while a low-level reference is expected to occur more often with a bottom-up comprehension process. High-level references encompass the whole program or multiple modules (i.e., more than one paragraph, file, etc.) within the program. Low-level references refer to a single module or single line of code. In the first excerpt above, the critical statement (no. 2) refers to “payroll,” the general purpose of the program. Hence, the statement would be coded as high-level. The critical statement in the second excerpt (no. 145) refers to a single variable and is therefore coded as low-level.

## Protocol Analysis Procedures

Both the pilot and the main study protocols were transcribed and phrased with one task assertion per line. First, we prepared a coding manual that contained detailed definitions, examples for each coding category, and rules for assigning codes. Next, we trained two coders who were familiar with COBOL but unfamiliar with the research questions. They coded the pilot protocols during training and all forty-eight protocols from the study proper (two from each of twenty-four participants).

Interrater reliability was assessed using Cohen's Kappa [9] and judged according to levels of acceptability suggested by Landis and Koch [25]. Coders were trained to "substantial" levels of agreement (Kappa $(K) \geq 0.61$ ) on the pilot study protocols. In the main study, the level of agreement for each of the three code categories was significant and each reflected substantial levels of agreement (hypotheses/inferences category: $K = 0.66$ , raw agreement $= 0.96$ , $z = 34.37$ , $p < 0.001$ ; type of knowledge category: $K = 0.79$ , raw agreement $= 0.90$ , $z = 26.63$ , $p < 0.001$ ; level of detail category: $K = 0.61$ , raw agreement $= 0.76$ , $z = 19.15$ , $p < 0.001$ ). The first author met with coders to reconcile disagreements in each category.

## Specific Research Questions

General research questions 1, 2, and 4 can now be specified in more detail. General research question 1 involves the effect of familiarity with the application domain on knowledge used during the program comprehension process. We might expect domain familiarity to result in more, and perhaps higher-level, references to application domain knowledge. It would be more intriguing, however, if the use of programming domain knowledge changes with levels of familiarity with the application domain. We state the following specific research questions:

Q1a: Do programmers make more application domain references in the familiar than the unfamiliar application domain?

Q1b: Do programmers make more programming domain references in the familiar than the unfamiliar application domains?

Q1c: Do programmers make relatively more high-level application domain references in the familiar than the unfamiliar application domain?

Q1d: Do programmers make relatively more high-level programming domain references in the familiar than the unfamiliar application domains?

General research question 2 involved the effect of the nature of the comprehension process on the type of knowledge used in program comprehension. Because a top-down comprehension process is accompanied by the statement of hypotheses regarding program function, we expect these programmers to make more extensive use of application domain knowledge than programmers using a more bottom-up process. This leads us to the following specific research questions:

Q2a: Do programmers using top-down comprehension processes make more application domain references than those using bottom-up processes?

Q2b: Do programmers using top-down comprehension processes make more programming domain references than those using bottom-up processes?

Q2c: Do programmers using top-down comprehension processes make relatively more high-level application domain references than those using bottom-up processes?

Q2d: Do programmers using top-down comprehension processes make relatively more high-level programming domain references than those using bottom-up processes?

General research question 4 has to do with the influence of a meta-model on the nature of the comprehension process used. $^{2}$ Meta-cognition refers to the intentional use of a meta-model to guide a cognitive process. Meta-cognition can aid in selecting a strategy, monitoring progress on the task, and regulating that progress [13]. On the other hand, programmers may use a meta-model unintentionally. For example, a programmer might use a particular problem-solving approach through habit even when that approach may not be the most effective—that is, an Einstellung effect [2]. We therefore pose the following specific research questions:

Q4a: Do programmers intentionally use a meta-model to select a particular comprehension process, regardless of their familiarity with the application domain?

Q4b: Do programmers unintentionally use a meta-model to select a particular comprehension process, regardless of their familiarity with the application domain?

## Data Analysis

# The Nature of the Comprehension Process in Familiar and Unfamiliar Application Domains

COMPREHENSION PROCESSES WERE CHARACTERIZED VIA PARTICIPANTS' PROCESS SCORES, obtained by subtracting the number of inferences in a protocol from the number of hypotheses. Hence, a more top-down comprehension process is reflected in a positive process score. $^{3}$ Table 1 presents the process scores for each programmer in the two application domains, and demonstrates that, in general, programmers use a more top-down process when working in a familiar domain. However, factors other than application domain familiarity also play a role in the process used: in six out of twenty-four instances, the process scores for the unfamiliar application domain were higher than for the familiar domain, suggesting that these programmers used more top-down processes in the unfamiliar domain.

We then classified each comprehension session as either top-down or bottom-up based on process score to examine whether the comprehension process a programmer used changed in a more absolute sense. Ten of the observations (from nine subjects) fell at the median, which led us to examine the comprehension processes of programmers in just the upper (more top-down) and lower (more bottom-up) process score quartiles. Use of quartiles is consistent with Pennington [29, 30]. Table 2 presents the process score and classification (top-down or bottom-up) for subjects in each application domain. Based on a paired t-test of the twelve observations, programmers used a more top-down process in the familiar application domain $t = 3.79, p = 0.001, df = 11$ .

Reorganizing these results reveals three distinct, equal-sized process groups (Table 3), one that used top-down processes in both application domains (the top-down group), another that used bottom-up processes in both domains (the bottom-up group), and a third group that used a top-down process in the familiar application domain and a bottom-up process in the unfamiliar domain (the flexible group). No programmer used a more top-down comprehension process in the unfamiliar domain and a more bottom-up process in the familiar domain. Hence, despite the fact that, in general, programmers used a more top-down process in the familiar domain, certain programmers used a similar approach (top-down or bottom-up) regardless of their familiarity with the application domain, while others changed their process between domains, in an absolute sense.

To explore further how the three groups' comprehension processes differ, we examine how their process changed during the protocols. Each protocol was divided into quartiles based on number of assertions. The average process score for each group in each quartile was calculated and plotted for each domain (see figures 2a and 2b).

Table 1. Process Scores for Each Programmer in Each Domain

<table><tr><td rowspan="2">Subject ID</td><td colspan="2">Process scores</td><td rowspan="2">Difference score</td></tr><tr><td>Accounting</td><td>Hydrology</td></tr><tr><td>1</td><td>2</td><td>-2</td><td>4</td></tr><tr><td>2</td><td>7</td><td>1</td><td>6</td></tr><tr><td>3</td><td>-7</td><td>-1</td><td>-6</td></tr><tr><td>4</td><td>-5</td><td>-1</td><td>-4</td></tr><tr><td>5</td><td>-1</td><td>-6</td><td>5</td></tr><tr><td>6</td><td>-2</td><td>-2</td><td>0</td></tr><tr><td>7</td><td>-3</td><td>-2</td><td>-1</td></tr><tr><td>8</td><td>2</td><td>-3</td><td>5</td></tr><tr><td>9</td><td>1</td><td>-1</td><td>2</td></tr><tr><td>10</td><td>1</td><td>1</td><td>0</td></tr><tr><td>11</td><td>7</td><td>1</td><td>6</td></tr><tr><td>12</td><td>-2</td><td>-5</td><td>3</td></tr><tr><td>13</td><td>-3</td><td>-1</td><td>-2</td></tr><tr><td>14</td><td>2</td><td>-2</td><td>4</td></tr><tr><td>15</td><td>-5</td><td>-8</td><td>3</td></tr><tr><td>16</td><td>2</td><td>0</td><td>2</td></tr><tr><td>17</td><td>2</td><td>1</td><td>1</td></tr><tr><td>18</td><td>3</td><td>1</td><td>2</td></tr><tr><td>19</td><td>-6</td><td>-5</td><td>-1</td></tr><tr><td>20</td><td>-2</td><td>-2</td><td>0</td></tr><tr><td>21</td><td>-1</td><td>-1</td><td>0</td></tr><tr><td>22</td><td>5</td><td>-1</td><td>6</td></tr><tr><td>23</td><td>-1</td><td>3</td><td>-4</td></tr><tr><td>24</td><td>3</td><td>-2</td><td>5</td></tr></table>

Figure 2a shows dramatic differences among the three groups in the familiar domain. The top-down and flexible groups start with similar positive (hypothesis-driven) process scores. The top-down group's process score drops fairly steadily through the four quartiles. On the other hand, the flexible group's process score drops dramatically during the second quartile, then moves up again as comprehension progresses, representing the greatest variation in process.

In the unfamiliar domain we find a similar, but less distinct, pattern. The top-down group begins with a positive process score, which drops to a slightly inference-driven process in the second quartile, returns to a hypothesis-driven process in the third quartile, then drops slightly in the fourth quartile. Given their lack of appropriate application domain knowledge, it is not surprising that these programmers were unable to sustain a hypothesis-driven process throughout the comprehension period; in other words, of necessity, they resorted at times to a somewhat more inferential (bottom-up) process. The flexible group again demonstrated the widest variation in process, while the bottom-up group used a bottom-up, inferential process in all quartiles of both domains (i.e., process scores < 0).

Based on this analysis, the flexible group is flexible with respect to the comprehension process used between the two domains, and also within each domain. These programmers altered their process, moving from a hypothesis-driven to an inference-driven process more readily than the other groups. This flexibility is reminiscent of the opportunistic problem solving observed during design [19, 20]. The effectiveness of a flexible process is further explored below.

Table 2. Process Scores and Classification of Programmers in Upper and Lower Quartiles

<table><tr><td rowspan="2">Subject ID</td><td colspan="2">Accounting domain</td><td colspan="2">Hydrology domain</td></tr><tr><td>Process score</td><td> $Process\ classification^a$ </td><td>Process score</td><td> $Process\ classification^a$ </td></tr><tr><td>19</td><td>-6</td><td>BU</td><td>-5</td><td>BU</td></tr><tr><td>15</td><td>-5</td><td>BU</td><td>-8</td><td>BU</td></tr><tr><td>7</td><td>-3</td><td>BU</td><td>-2</td><td>BU</td></tr><tr><td>20</td><td>-2</td><td>BU</td><td>-2</td><td>BU</td></tr><tr><td>8</td><td>2</td><td>TD</td><td>-3</td><td>TD</td></tr><tr><td>14</td><td>2</td><td>TD</td><td>-2</td><td>TD</td></tr><tr><td>1</td><td>2</td><td>TD</td><td>-2</td><td>TD</td></tr><tr><td>24</td><td>3</td><td>TD</td><td>-2</td><td>TD</td></tr><tr><td>17</td><td>2</td><td>TD</td><td>1</td><td>TD</td></tr><tr><td>18</td><td>3</td><td>TD</td><td>1</td><td>TD</td></tr><tr><td>2</td><td>7</td><td>TD</td><td>1</td><td>TD</td></tr><tr><td>11</td><td>7</td><td>TD</td><td>1</td><td>TD</td></tr></table>

$^{a}$ BU = Bottom-up comprehension process; TD = top-down comprehension process.

Table 3. Nominal Classification of Process

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Hydrology domain</td></tr><tr><td>Top-down</td><td>Bottom-up</td></tr><tr><td rowspan="2">Accounting domain</td><td>Top-down</td><td>4</td><td>4</td></tr><tr><td>Bottom-up</td><td>0</td><td>4</td></tr></table>

Characterizing the Use of Application and Programming Domain Knowledge

The following sections address the first two research questions. Table 4 presents the data on which the analyses are based.

## Effect of Application Domain Familiarity

Question 1 addresses the type and level of knowledge used in familiar and unfamiliar application domains. Because this analysis is independent of comprehension process, we use data for all three process groups. See the rows labeled “Overall” in Table 4 for the specific data.

![](/api/attachments/5GX2BXSX/fulltext/images/19f565d47ae71ef9023216175a0be756d10509a42ca013ea81c26c4683786f37.jpg)  
Figure 2a. Process Scores in the Familiar (Accounting) Domain for Each Process Group

Questions 1a and 1b involve the number of application and programming domain references programmers make in the familiar and unfamiliar application domains. Question 1a is analyzed by comparing the proportion of application domain references made in the familiar domain against the null hypothesis that the proportion is 0.5. From the data in Table 4, the proportion of application domain references made in the familiar domain was significantly higher than 0.5 (60/82 = 0.73, z = 4.09, p < 0.001), and the proportion of application domain references is higher in the familiar than in the unfamiliar domain. $^{4}$

Question 1b is similar to question 1a and we analyze it in a similar fashion. The proportion of programming domain references is virtually the same, irrespective of application domain (93/188 = 0.49; z = -0.15, p = 0.88).

Questions 1c and 1d address the level of knowledge used in the familiar and unfamiliar application domains. Question 1c considers the level of application domain references made in the two domains. This question is addressed by comparing the proportion of high-level application domain references (i.e., the number of high-level application references divided by the total number of application references) in each domain. The proportions of high-level references in the familiar domain (21/60 = 0.35) and in the unfamiliar domain (8/22 = 0.36) are not significantly different (z = -0.15, p = 0.88). $^{5}$

![](/api/attachments/5GX2BXSX/fulltext/images/086980853a34e56d464ba763470f52d3fc5904d1847e227e33cdbb80ea98d835.jpg)  
Figure 2b. Process Scores in the Unfamiliar (Hydrology) Domain for Each Process Group

Question 1d is similar to question 1c but considers the level of programming domain references. The proportion of high-level programming domain references is again virtually the same, irrespective of application domain (55/93 = 0.59 versus 56/95 = 0.59; z = 0.12, p = 0.90).

## Effect of Using Top-Down and Bottom-Up Comprehension Processes

We now compare the top-down and bottom-up process groups to determine the effect of comprehension process on the type and level of references made (question 2). These questions are analyzed in a similar fashion to question 1. Questions 2a and 2b address the number of application and programming domain references made using top-down and bottom-up comprehension processes, respectively. The proportion of application domain references made using a top-down process exceeds that using a bottom-up process (37/55 = 0.67, z = 2.43, p = 0.02). The effect holds in the familiar application domain (26/(26 + 13) = 0.67, z = 1.92, p = 0.05), but not the unfamiliar (11/(11 + 5) = 0.69, z = 1.25, p = 0.21). The proportion of programming domain references is virtually the same regardless of comprehension process: overall (74/(74 + 67) = 0.52, z = 0.59, p = 0.56), and in both domains—familiar: (37/(37 + 30) = 0.55, z = 0.73, p = 0.46); unfamiliar: (37/(37 + 37) = 0.5, z = 0, p = 1.00).

Table 4. Summary of Types and Levels of References by Process Group

<table><tr><td rowspan="3">Process group</td><td colspan="4">Familiar application domain</td><td colspan="4">Unfamiliar application domain</td><td colspan="4">Across application domains</td></tr><tr><td colspan="2">Appln. refs.</td><td colspan="2">Pgg refs.</td><td colspan="2">Appln. refs.</td><td colspan="2">Pgg refs.</td><td colspan="2">Appln. refs.</td><td colspan="2">Pgg refs.</td></tr><tr><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td rowspan="2">Top-down</td><td>14(26)</td><td>12</td><td>23(37)</td><td>14</td><td>5(11)</td><td>6</td><td>25(37)</td><td>12</td><td>19(37)</td><td>18</td><td>48(74)</td><td>26</td></tr><tr><td></td><td>(63)</td><td></td><td></td><td></td><td>(48)</td><td></td><td></td><td></td><td>(111)</td><td></td><td></td></tr><tr><td rowspan="2">Bottom-up</td><td>2(13)</td><td>11</td><td>19(30)</td><td>11</td><td>2(5)</td><td>3</td><td>21(37)</td><td>16</td><td>4(18)</td><td>14</td><td>40(67)</td><td>27</td></tr><tr><td></td><td>(43)</td><td></td><td></td><td></td><td>(42)</td><td></td><td></td><td></td><td>(85)</td><td></td><td></td></tr><tr><td rowspan="2">Flexible</td><td>5(21)</td><td>16</td><td>13(26)</td><td>13</td><td>1(6)</td><td>5</td><td>10(21)</td><td>11</td><td>6(27)</td><td>21</td><td>23(47)</td><td>24</td></tr><tr><td></td><td>(47)</td><td></td><td></td><td></td><td>(47)</td><td></td><td></td><td></td><td>(74)</td><td></td><td></td></tr><tr><td rowspan="2">Overall</td><td>21(60)</td><td>39</td><td>55(93)</td><td>38</td><td>8(22)</td><td>14</td><td>56(95)</td><td>39</td><td>29(82)</td><td>53</td><td>111(188)</td><td>77</td></tr><tr><td></td><td>(153)</td><td></td><td></td><td></td><td>(117)</td><td></td><td></td><td>(270)</td><td></td><td></td><td></td></tr></table>

Questions 2c and 2d involve the level of knowledge references observed with top-down and bottom-up processes. The proportion of high-level application references is greater when using a top-down comprehension process (19/37 = 0.51 versus 4/18 = 0.22; z = 1.76, p = 0.08). This effect is manifested only in the familiar (14/26 = 0.54 versus 2/13 = 0.15, z = 1.96, p = 0.05) and not in the unfamiliar domain (5/11 = 0.45 versus 2/5 = 0.4, z = -0.34, p = 0.73). The proportion of high-level programming domain references does not vary with the comprehension process (48/74 = 0.65 versus 40/67 = 0.60, z = 0.46, p = 0.65). This result holds in both the familiar (23/37 = 0.62 versus 19/30 = 0.63, z = 0.16, p = 0.88) and unfamiliar domains (25/37 = 0.67 versus 21/37 = 0.57, z = 0.72, p = 0.47).

## Effect of Using a Flexible Comprehension Process

Here, we characterize the ways in which the flexible group differs from the other two process groups by comparing domain references. The analyses conducted parallel those in the previous sections.

Flexible and Top-Down Process Groups: The flexible and top-down groups made similar numbers of application domain references $(27/(27+37)=0.42, z=-1.13, p=0.26)$ . This finding holds in both domains (familiar: $21/(21+26)=0.45, z=-0.58, p=0.56$ ; unfamiliar: $11/(11+5)=0.65, z=-0.97, p=0.33$ ). However, the flexible group made fewer references to programming domain knowledge $(47/(47+74)=0.39, z=-2.45, p=0.01)$ , a finding that holds in the unfamiliar $(21/(21+37)=0.36, z=-1.97, p=0.05)$ , but not the familiar application domain $(26/(26+37)=0.41, z=-1.26, p=0.21)$ . With respect to the level of the references, the flexible group made fewer high-level application domain references than the top-down group $(6/27=0.22$ versus $19/37=0.51$ , $z = -2.10, p = 0.04$ ). This finding holds in the familiar (5/21 = 0.24 versus 14/26 = 0.40, z = -1.79, p = 0.07), but not in the unfamiliar domain (1/6 = 0.17 versus 5/11 = 0.45, z = -0.66, p = 0.51). Finally, the proportion of high-level programming references does not vary between the top-down and flexible process groups (23/47 = 0.49 versus 48/74 = 0.65, z = -1.54, p = 0.12). This finding holds in both domains (familiar: 13/26 = 0.5 versus 23/37 = 0.62, z = -0.70, p = 0.48; unfamiliar: 10/21 = 0.48 versus 25/37 = 0.68, z = -1.21, p = 0.23).

Flexible and Bottom-Up Process Groups: The flexible and bottom-up groups made similar proportions of application domain references $(27/(27+18)=0.60, z=1.19, p=0.23)$ . This results hold in both domains (familiar: $21/(21+13)=0.62, z=1.20, p=0.22$ ; unfamiliar: $6/(6+5)=55, z=0.00, p=1.00$ ). However, the flexible group made significantly fewer references to programming knowledge $(47/(47+67)=0.41, z=-1.87, p=0.06)$ , a finding that holds in the unfamiliar $(21/(21+37)=0.36, z=-1.97, p=0.05)$ , but not in the familiar domain $(26/(26+30)=0.46, z=-0.40, p=0.69)$ . With respect to level of references, there were no differences in the number of high-level application domain references made overall $(6/27=0.22\text{ versus }4/18=0.22, z=0, p=1.00)$ or in either domain (familiar: $5/21=0.24\text{ versus }2/13=0.21, z=0.15, p=0.88$ ; unfamiliar: $1/6=0.17\text{ versus }2/5=0.4, z=-0.19, p=0.85$ ). There were also no differences in the number of high-level programming references made overall $(23/47=0.49\text{ versus }40/67=0.60, z=-0.95, p=0.34)$ or in either domain (familiar: $13/26=0.50\text{ versus }19/30=0.63, z=-0.73, p=0.46$ ; unfamiliar: $10/21=0.48\text{ versus }21/37=0.57, z=-0.40, p=0.69$ ).

## The Impact of Application Domain Knowledge and Process on the Effectiveness of Comprehension

Research question 3 investigates the effect of application domain knowledge and comprehension process on the effectiveness of comprehension. An ANOVA was conducted using process group (i.e., top-down, bottom-up, or flexible) as a between-subjects factor and application domain as a within-subjects factor. The dependent variable was the percentage of comprehension questions answered correctly. Table 5a presents the descriptive data, while Table 5b presents the results of the analysis. The effect for process group reached conventional significance levels $p = 0.10$ ; the effect for application domain did not $p = 0.11$ ; nor did the interaction effect $p = 0.62$ . The average percentage of correct answers for the top-down, bottom-up, and flexible process groups was 50 percent, 61 percent, and 71 percent, respectively. At first glance, this pattern of results was surprising because the literature suggests that a top-down process is more powerful than a bottom-up process [8].

To interpret these results, recall the graphs presented as figures 2a and 2b. Comprehension processes of the flexible group appeared to change opportunistically. It seems likely, therefore, that flexible processes may allow programmers to grasp the greatest amount of knowledge in a given time period. The bottom-up group demonstrated the next highest level of comprehension. A bottom-up process is data-driven, requiring programmers to study the code in detail. Note that the comprehension questions are quite detailed, since questions that can be answered by a yes/no response must be specific. The detailed study of program code consistent with a bottom-up process would benefit a programmer when answering such comprehension questions.

Table 5.  
a. Means and standard deviations of comprehension scores across domains and process groups

<table><tr><td>Domain:</td><td>Accounting</td><td>Hydrology</td><td>Mean by process group</td></tr><tr><td colspan="4">Process group:</td></tr><tr><td>Top-down</td><td>56.25(13.77)</td><td>43.75(24.62)</td><td>50.00(19.64)</td></tr><tr><td>Bottom-up</td><td>71.25(9.46)</td><td>50.00(21.60)</td><td>60.63(19.17)</td></tr><tr><td>Flexible</td><td>72.50(15.55)</td><td>68.75(13.15)</td><td>70.63(13.48)</td></tr><tr><td>Mean by domain</td><td>66.67(14.20)</td><td>54.17(21.51)</td><td>60.42(18.93)</td></tr></table>

b. Comprehension findings by process group

<table><tr><td>Source</td><td>Sum of squares</td><td>Mean square</td><td>DF</td><td>F value</td><td>p value</td></tr><tr><td>Process group</td><td>1,702.08</td><td>851.04</td><td>2</td><td>2.98</td><td>0.10</td></tr><tr><td>Error</td><td>2,568.75</td><td>285.42</td><td>9</td><td></td><td></td></tr><tr><td>Domain</td><td>937.50</td><td>937.50</td><td>1</td><td>3.09</td><td>0.11</td></tr><tr><td>Process group/domain interaction</td><td>306.25</td><td>153.13</td><td>2</td><td>0.51</td><td>0.62</td></tr><tr><td>Error</td><td>2,731.25</td><td>303.47</td><td>9</td><td></td><td></td></tr></table>

Finally, the top-down group used a hypothesis-driven process in both domains. During the initial stages of comprehension, a programmer using such a process is unlikely to be studying a program in great detail. Figures 2a and 2b support this notion. The process scores of the top-down process group declined during the later quartiles, particularly in the familiar domain. It appears likely, therefore, that this group's relatively low comprehension scores are due to not studying the program at a sufficiently detailed level to respond to the comprehension questions correctly. With a longer comprehension period, their level of comprehension might have increased. It is also likely that these programmers gained a different type of knowledge from that tapped in the detailed comprehension questions. In summary, our data suggest that the most powerful approach to comprehension is for programmers to adapt their comprehension processes to their knowledge of the application domain, and to seek knowledge at different levels during the comprehension process.

## Use of a Meta-Model on Programmers' Comprehension Processes

Research question 4 considers the role of cognitive determinants in the program comprehension process. Because some programmers did not change their process, in an absolute sense based on familiarity with the application domain (see Table 3), we postulate that programmers might use a meta-model to select a comprehension process.

## Intentional Use of a Meta-Model: The Role of Meta-Cognition

Meta-cognition refers to “one’s knowledge concerning one’s own cognitive processes” [15, p. 232]. In the context of computer program comprehension, meta-cognition occurs when programmers consciously and intentionally use a particular comprehension process. It could explain, therefore, why some programmers used similar comprehension processes in both application domains (either top-down or bottom-up), as reflected in Table 3.

Comments made during the debriefing period revealed that some programmers might consciously select a comprehension strategy. Hence, the decision was made to formally investigate the possibility of meta-cognition, and a questionnaire was mailed to participants following the initial data collection. $^{6}$ Because meta-cognition involves the conscious use of a cognitive process, it is appropriate to assess programmers' use of meta-cognition directly. The questionnaire was developed based on prior literature [13] and on definitions of top-down and bottom-up comprehension processes [3, 8]. The questionnaire was examined by independent cognition researchers prior to distribution. $^{7}$ Because these results are based on retrospective reports, they should be considered exploratory.

Ten of the twelve programmers in our three process groups completed a questionnaire on their use of meta-cognition in general and in this study in particular. They reported using meta-cognition in ten out of twenty instances; eight of those instances related to conscious use of a more top-down comprehension process. In general, programmers also reported modifying their comprehension process according to such factors as size, complexity, familiarity, and nature of the application (numerically intensive or report generation). Shaft [33] presents a detailed analysis of the results from all participants in the study.

Table 6, which presents the results for the twelve programmers in the three process groups, shows that there is not a good match between the comprehension process programmers were observed using and the ones they reported using—that is, although programmers reported that, in ten of twenty instances, they made conscious choices regarding process, the process they reported matched our observations in only two of those ten instances. There are two possible explanations: (1) programmers intentionally used a particular comprehension process, but were unable to identify (i.e., label) the process correctly, or (2) programmers were influenced by a social-desirability bias. A social-desirability bias occurs when an individual responds to a questionnaire item based on what is perceived to be the socially desirable (“good” or “acceptable”) answer [28]. In the context of software development, programmers may have been trained to believe that anything top-down is better than anything bottom-up, which may have biased their responses [17].

Table 6. Actual and Perceived Comprehension Processes of Programmers Based on Process Groups

<table><tr><td rowspan="2">Process group</td><td rowspan="2">Subject</td><td colspan="2">Familiar domain</td><td colspan="2">Unfamiliar domain</td></tr><tr><td>Actual</td><td>Perceived</td><td>Actual</td><td>Perceived</td></tr><tr><td rowspan="4">Top-down</td><td>2</td><td>7</td><td>None</td><td>1</td><td>Top-down</td></tr><tr><td>11</td><td>7</td><td>—</td><td>1</td><td>—</td></tr><tr><td>17</td><td>2</td><td>None</td><td>1</td><td>None</td></tr><tr><td>18</td><td>3</td><td>None</td><td>1</td><td>None</td></tr><tr><td rowspan="4">Bottom-up</td><td>7</td><td>-3</td><td>None</td><td>-2</td><td>None</td></tr><tr><td>15</td><td>-5</td><td>Top-down</td><td>-8</td><td>Top-down</td></tr><tr><td>19</td><td>-6</td><td>Top-down</td><td>-5</td><td>Top-down</td></tr><tr><td>20</td><td>-2</td><td>Top-down</td><td>-2</td><td>Top-down</td></tr><tr><td rowspan="4">Flexible</td><td>1</td><td>2</td><td>Bottom-up</td><td>-2</td><td>Bottom-up</td></tr><tr><td>8</td><td>2</td><td>—</td><td>-3</td><td>—</td></tr><tr><td>14</td><td>2</td><td>None</td><td>-2</td><td>None</td></tr><tr><td>24</td><td>3</td><td>None</td><td>-2</td><td>Top-down</td></tr></table>

## Unintentional Use of a Meta-Model: The Role of Experience

Unintentional use of a meta-model occurs when a programmer habitually uses a particular comprehension process without making a conscious choice (an Einstellung effect), which results from experience [2]. To investigate, we compared the backgrounds of the three process groups using data collected during the initial participant screening process. There were no differences in the demographic variables for the top-down and bottom-up groups. However, the flexible group, as Table 7 shows, differed significantly from the other two groups. Age was significantly lower than that of the other groups (31 years compared with 37 years; p = 0.04). Factors that would be expected to vary with age (see Table 7) were also significantly lower for this group. Hence, we cannot rule out the presence of an Einstellung effect among older programmers who may use a particular comprehension process irrespective of familiarity with the application domain.

Further, the evidence supports the distinction between meta-cognition (conscious choice of a process) and an Einstellung effect (habitual use of a process). Unlike the suspected Einstellung effect, meta-cognition was not affected by experience: Programmers who indicated using meta-cognition were, on average, thirty-seven years of age, while those who indicated not using meta-cognition were thirty-six years of age, on average. Hence, it appears that the use of meta-cognition and the possible Einstellung effect are motivated by distinct factors.

Table 7. Demographic Differences between Flexible Group and Top-Down and Bottom-Up Groups

<table><tr><td rowspan="2">Variable</td><td colspan="3">Means</td></tr><tr><td>Flexible group</td><td>Top-down and bottom-up groups</td><td>p value</td></tr><tr><td>Age</td><td>31.00</td><td>37.38</td><td>0.0356</td></tr><tr><td>Length of time working in COBOL</td><td>5.88</td><td>13.88</td><td>0.0005</td></tr><tr><td>Years IS experience</td><td>4.08</td><td>15.07</td><td>0.0001</td></tr><tr><td>Years accounting IS experience</td><td>3.83</td><td>10.02</td><td>0.0155</td></tr><tr><td>Number of applications</td><td>2.75</td><td>7.00</td><td>0.0129</td></tr></table>

## Discussion

THIS STUDY EXTENDS PRIOR RESEARCH THAT FOUND THAT PROGRAMMERS use more top-down comprehension processes when the application domain is familiar to them and more bottom-up processes when the domain is unfamiliar.

## Findings

Examination of the two extreme “process” quartiles (top-down and bottom-up) revealed that subjects fell evenly into three categories: those who used top-down processes in both familiar and unfamiliar application domains; those who used bottom-up processes in both; and those who used a more top-down process in the familiar domain and a more bottom-up process in the unfamiliar domain. No subject used a more top-down process in the unfamiliar domain and a more bottom-up process in the familiar domain.

Table 8 summarizes the findings regarding the knowledge used by the three process groups from the viewpoint of both familiarity with the application domain (question 1) and use of top-down vis-à-vis bottom-up comprehension processes (question 2). With respect to question 1, use of a more top-down (i.e., hypothesis-driven) process, was manifested in greater use of application domain knowledge in the comprehension process. There were no differences in level of application domain references, or in the number or level of references to the programming domain.

With respect to question 2, data from the top-down and bottom-up process groups showed that top-down comprehension processes resulted in both significantly more application domain references, as well as higher-level application references, than bottom-up processes, but only in the familiar application domain. Programming domain references were unchanged across domains. This finding is important because it highlights the fact that application domain knowledge was used in addition to, but not to compensate for, programming knowledge.

The flexible group, which changed comprehension processes across domains, was similar to the other process groups with regard to the number of application domain references. However, in comparison to the top-down group, the flexible group made lower-level references to application knowledge, both overall and in the familiar domain. The flexible group also made fewer references to programming knowledge than the other two process groups. This difference was detected in the unfamiliar but not the familiar application domain. Comprehension process had little effect on the level of programming domain references. These differences between the flexible and other process groups are further supported by the way their process scores changed during the comprehension process (recall figures 2a and 2b).

Table 8. Summary of Findings Based on Type and Level of References

<table><tr><td rowspan="2"></td><td rowspan="2">Domain familiarity (Q1)</td><td colspan="3">Top-down vs. Bottom-up groups (Q2)</td><td colspan="3">Flexible vs. top-down groups</td><td colspan="3">Flexible vs. bottom-up groups</td></tr><tr><td>Overall</td><td>Familiar</td><td>Unfamiliar</td><td>Overall</td><td>Familiar</td><td>Unfamiliar</td><td>Overall</td><td>Familiar</td><td>Unfamiliar</td></tr><tr><td>Application domain references</td><td>fam &gt; unf (0.001)</td><td>TD &gt; BU (0.02)</td><td>TD &gt; BU (0.05)</td><td>TD = BU (0.21)</td><td>FL = TD (0.26)</td><td>FL = TD (0.56)</td><td>FL = TD (0.33)</td><td>FL = BU (0.23)</td><td>FL = BU (0.22)</td><td>FL = BU (1.00)</td></tr><tr><td>Programming domain references</td><td>fam = unf (0.88)</td><td>TD = BU (0.56)</td><td>TD = BU (0.46)</td><td>TD = BU (1.0)</td><td>TD &gt; FL (0.01)</td><td>FL = TD (0.21)</td><td>TD &gt; FL (0.05)</td><td>BU &gt; FL (0.06)</td><td>FL = BU (0.69)</td><td>BU &gt; FL (0.05)</td></tr><tr><td>Level of application domain references</td><td>fam = unf (0.88)</td><td>TD &gt; BU (0.08)</td><td>TD &gt; BU (0.05)</td><td>TD = BU (0.73)</td><td>TD &gt; FL (0.04)</td><td>TD &gt; FL (0.07)</td><td>FL = TD (0.51)</td><td>FL = BU (1.00)</td><td>FL = BU (0.88)</td><td>FL = BU (0.85)</td></tr><tr><td>Level of programming domain references</td><td>fam = unf (0.90)</td><td>TD = BU (0.65)</td><td>TD = BU (0.88)</td><td>TD = BU (0.47)</td><td>FL = TD (0.12)</td><td>FL = TD (0.48)</td><td>FL = TD (0.23)</td><td>FL = BU (0.34)</td><td>FL = BU (0.46)</td><td>FL = BU (0.69)</td></tr></table>

Further, comprehension was significantly higher for the flexible group than for the other two groups. This finding is particularly interesting because earlier models of comprehension $[3, 8]$ argued that a particular approach to comprehension was the most appropriate or powerful. Our findings support Pennington's observation that computer programmers who use a comprehension strategy in which references to the domain and the program are interconnected results in better comprehension $[30]$ . A flexible strategy is also reminiscent of Guindon et al.'s $[19, 20]$ opportunistic approach to software design.

We considered the possibility that certain programmers use a meta-model to determine their approach to comprehending computer programs. Meta-cognition reflects a conscious choice of comprehension process, and the process used may therefore vary according to a number of factors. In this instance, we investigated whether they may use a particular process, irrespective of familiarity with the application domain. Investigation of meta-cognition revealed, however, that, in general, programmers who used a top-down process reported that they did not purposely choose a comprehension process, while those who used a bottom-up process reported using a top-down process.

The issue of meta-cognition needs, however, to be disentangled from issues of social-desirability bias and expertise. One preliminary indicator of the impact of expertise might be found in differences between the flexible process group and the top-down and bottom-up groups. The flexible group, despite the fact that it was significantly younger than the other two groups, achieved the highest levels of comprehension. This finding highlights the need to distinguish between meta-cognition and possible Einstellung effects for older programmers, which would result in the use of a similar comprehension process regardless of the environment.

## Strengths and Limitations of the Study

The strengths of this study are its use of professional programmers, the formal coding of verbal protocols, and the power of the within-subjects design. First, many studies use students as subjects, a practice that is justified when examining novice learning or when the theory does not posit “novice-expert” differences. Because our research questions related to application domain knowledge, which is not taught in any curricula, it was important that we use professional programmers. The use of such subjects increases the external validity and generalizability of the results. However, it also limits the sample size.

A second strength of this study is that all protocols were transcribed and formally coded, unlike many similar studies $[26, 30]$ . Third, the use of a within-subjects design allowed us to control for individual programmer differences [37]. In controlling for programmer variability, a within-subjects design yields greater power than between-subjects designs with the same number of participants.

The potential limitations of the study center on the sample size and the size of the computer programs used as task materials. With respect to the relatively small sample size, note, first, that a small number of participants is the norm for studies using process tracing methods, such as verbal protocols, due to the cost of collecting, transcribing, and analyzing process data. Note that the sample size in this study is larger than the majority of prior protocol analysis studies $[26]$ . Second, the small sample size is offset by the rich data afforded by the protocol analysis method $[32]$ . Further, verbal protocols are widely acknowledged as the most appropriate approach to investigating comprehension processes $[34]$ . Third, our sample size was large enough, as demonstrated by the fact that our research design had adequate statistical power to detect significant differences for the between-subjects factor (process group) included in our design. Small sample sizes are a concern when null hypotheses are accepted, because it is possible that a true difference could not be detected due to lack of power. Hence, the strengths from the use of professional programmers, the use of a method particularly suited to collecting the type of data required, the formal coding of the protocols, and use of a within-subjects design outweigh the limitation that might be attributed to sample size.

A second potential limitation of this study is that the programs used as task materials were fairly small compared with the million-lines-of-code systems that exist in practice $[11]$ . These programs were substantially larger, however, than those used in previous studies of program comprehension (e.g., $[15]$ ). In addition, the size of the programs allowed us to keep participation time to approximately four hours, which we considered the upper limit for most professionals. Finally, these programs differentiated between the two application domains sufficiently well, as demonstrated by domain familiarity ratings.

## Implications

Our findings have implications for both research and practice. From the viewpoint of conducting research into the systems development process, our findings demonstrate the need to consider not only the programming domain, but also the application domain. We found, however, that familiarity with the application domain and use of different comprehension processes had effects on the amount and level of both application and programming domain knowledge. This demonstrates the need to consider the effects on application-related variables.

Second, comprehension underlies other programming tasks such as testing and debugging, as well as maintenance. Maintenance, for example, frequently requires incorporating additional functionality into a program. Knowledge of the application domain could influence both the initial stages of understanding the requirements of any new features, as well as actually implementing the change. Similarly, debugging is usually conceptualized as requiring programming expertise (see, for example, [40]). Given the recent evidence on the importance of application domain knowledge, research should also be conducted into its role in other programming-related efforts.

Third, more studies are needed to investigate how programmers choose a program comprehension process. This study presented an initial investigation of the use of meta-cognition and identified a possible Einstellung effect. However, more research is required to distinguish these two factors from each other, from social-desirability bias, and from aspects of expertise.

Fourth, the flexible process group achieved the highest levels of comprehension. Interestingly, the programmers in this group were significantly younger than those in the group that used the same comprehension process in both domains. We suspect an Einstellung effect may lead older programmers habitually to use a particular process, which stimulates two possible directions for future research. First, longitudinal studies could assess how programmers' comprehension processes adapt over time and the influence of such changes on the effectiveness of comprehension. Second, programmers could be trained to use a more flexible approach to comprehension. Studies could then investigate whether these programmers achieve higher levels of comprehension with a flexible rather than a fixed comprehension process.

From a practical perspective, our research has implications for the development of tools to support the software maintenance process, as well as the training, hiring, and management of programmers. First, the growing body of evidence pointing to the importance of the application domain in performing software tasks suggests that software tool builders should investigate ways of incorporating characteristics of the application domain into tools. For example, tools that allow programmers to access a domain model would benefit those working in unfamiliar domains. Second, the enhanced performance of programmers using flexible comprehension processes suggests that tool builders should investigate the design of tools that allow programmers to adapt their comprehension process readily from a hypothesis-driven to an inference-driven process. For example, tools that link high-level representations (such as structure charts) with source code would allow programmers to move easily from a high-level notation to direct examination of the code. The tool should also allow programmers to move in the reverse direction. Therefore, a reverse-engineering tool that generates a high-level representation from current source code could support maintenance efforts.

From the viewpoint of hiring, training, and management of programmers, the findings of this study suggest that hiring programmers with experience in a given area, or providing explicit training to help programmers gain application domain knowledge, may be a worthwhile investment for organizations. Programmers gain application domain knowledge based on programming assignments, but organizations do not necessarily use these assignments to develop programmers' application domain knowledge explicitly. Careful assignment of personnel to projects to develop application domain knowledge may be a key to developing the “exceptional designers” who often play critical roles in successful large-scale development $[11]$ .

## NOTES

1. Statements that were neither hypotheses nor inferences were not coded.

2. Research Question 3 does not require more specific questions for analysis.

3. Detailed statistical analysis of this data is presented in [35].

4. This figure is calculated by dividing the number of application domain references made in the familiar domain, 60, by the number of application domain references made across the two application domains, 82. For the reader's convenience, these data are indicated by bold typeface in Table 4. Continuity correction factors are used to compute z-scores.

5. For the reader's convenience, the specific data used to investigate Research Question 1(b) are indicated by italics in Table 4.

6. The questionnaire is available from the first author upon request or can be found in [33].

7. Because we were interested in a programmer's specific choice or behavior (i.e., if a programmer chose a specific process and which process) rather than a latent construct, there were no scales to subject to post-hoc reliability and validity analyses.

## REFERENCES

1. Adelson, B., and Soloway, E. The role of domain experience in software design. IEEE Transactions on Software Engineering, SE-11, 11 (1985), 1351-1360.

2. Anderson, J.R. Cognitive Psychology and Its Implications. New York: W.H. Freeman, 1985.

3. Basili, V.R., and Mills, H.D. Understanding and documenting programs. IEEE Transactions on Software Engineering, SE-8, 3 (May 1982), 270-283.

4. Bennett, K.H.; Cornelius, B.J.; Munro, M.; and Robson, D.J. Software maintenance: a key area for research. University Computing, 10 (1988), 184–188.

5. Blum, B. Volume, distance, and productivity. Journal of Systems and Software, 9 (1989), 217–226.

6. Boehm-Davis, D. Software comprehension. In M. Helander (ed.), Handbook of Human-Computer Interaction. Amsterdam: Elsevier Science Publishers, 1988, pp. 107–121.

7. Brooks, R.E. Studying programmer behavior experimentally: the problems of proper methodology. Communications of the ACM, 23, 4 (1980), 207–213.

8. Brooks, R.E. Towards a theory of the comprehension of computer programs. International Journal of Man-Machine Studies, 18 (1983), 543–554.

9. Cohen, J.A. Coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20 (1960), 37–46.

10. Dyson-Hudson, N. Taming the COBOL maintenance monster. Computer Languages, 9, 9 (1992) 40–44.

11. Curtis, B.; Krasner, H.; and Iscoe, N. A field study of the software design process for large systems. Communications of the ACM, 31, 11 (1988), 1268–1287.

12. Curtis, B.; Sheppard, S.B.; Kruesi-Bailey, E.; Bailey, J.; and Boehm-Davis, D.A. Experimental evaluation of software documentation formats. Journal of Systems and Software, 8 (1989), 167–207.

13. Flavell, J.H. Metacognitive aspects of problem solving. In L. Resnick (ed.), The Nature of Intelligence. Hillsdale, NJ: Ablex Publishing, 1976.

14. Ford, J.K.; Schmitt, N.; Schechtman, S.L.; Hults, B.M.; and Doherty, M.L. Process tracing methods: contributions, problems, and neglected research questions. Organizational Behavior and Human Decision Processes, 43 (1989), 75–117.

15. Gellenbeck, E.M., and Cook, C.R. An investigation of procedure and variable names as beacons during program comprehension. In J. Koenemann-Belliveau, T.G. Moher, and S.P. Robertson (eds.), Empirical Studies of Programmers: Fourth Workshop. Norwood, NJ: Ablex Publishing, 1991, pp. 65–79.

16. Glass, R., and Vessey, I. Toward a taxonomy of software application domains: history. Journal of Systems and Software, 17, 2 (1992), 189–199.

17. Goldman, L. Using Tests in Counseling. New York: Prentice-Hall, 1971.

18. Green, T.R.G. Conditional program statements and their comprehensibility to professional programmers. Journal of Occupational Psychology, 50 (1977), 93–109.

19. Guindon, R. Knowledge exploited by experts during software system design. International Journal of Man-Machine Studies, 33 (1990), 323–342.

20. Guindon, R.; Krasner, H.; and Curtis, B. Breakdowns and processes during the early activities of software design by professionals. In G.M. Olson, S. Sheppard, and E.S. Soloway (eds.), Empirical Studies of Programmers: Second Workshop. Norwood, NJ: Ablex Publishing, 1987, pp. 65–82.

21. Jarzabek, S. Domain model-driven software reengineering and maintenance. Journal of Systems and Software, 20 (1993), 37–51.

22. Jones, C. Programmer Productivity. New York: McGraw-Hill, 1986.

23. Jones, C. Software metrics: good, bad, and missing. IEEE Computer (September 1994), 98–100.

24. Kemerer, C.F. Software complexity and software maintenance: a survey of empirical research. Annals of Software Engineering, 1 (August 1995).

25. Landis, J.R., and Koch, G.G. The measurement of observer agreement for categorical data. Biometrics, 33 (1977), 259–274.

26. Letovsky, S. Cognitive processes in program comprehension. In E.S. Soloway and S. Iyengar (eds.), Empirical Studies of Programmers: First Workshop. Norwood, NJ: Ablex Publishing, 1986, pp. 58–79.

27. Lind, R., and Vairavan, K. An experimental study of software metrics and their relationship to software development effort. IEEE Transactions on Software Engineering, SE-15, 5 (1989), 649–653.

28. Nunnally, J.C. Psychometric Theory, 2d ed. New York: McGraw-Hill. 1978.

29. Pennington, N. Comprehension strategies in programming. In G.M. Olson, S. Sheppard, and E. Soloway (eds.), Empirical Studies of Programmers: First Workshop. Norwood, NJ: Ablex Publishing, 1987, pp. 100–113.

30. Pennington, N. Stimulus structures and mental representations in expert comprehension of computer programs. Cognitive Psychology, 19 (1987), 295–341.

31. Robson, D.; Bennett, K.; Cornelius, B.; and Munro M. Approaches to program comprehension. Journal of Systems and Software, 14 (1991), 79–84.

32. Russo, J.E.; Johnson, E.J.; and Stephens, D.L. The validity of verbal protocols. Memory and Cognition, 17, 6 (1989), 759–769.

33. Shaft, T.M. Helping programmers understand computer programs: the use of metacognition. Data Base Advances, 26, 4 (1995), 25–46.

34. Shaft, T.M. Responses to comprehension questions and verbal protocols as measures of computer program comprehension processes. Behavior and Information Technology. 16, 6 (1997), 320–336.

35. Shaft, T.M., and Vessey, I. The relevance of application domain knowledge: the case of computer program comprehension. Information Systems Research, 6, 3 (1995), 286–299.

36. Sheppard, S.B.; Curtis, B.; Milliman, P.; and Love, T. Modern coding practices and programmer performance. IEEE Computer, 12, 12 (1979), 41–49.

37. Sheil, B.A. The psychological study of programming. ACM Computing Surveys, 13, 1 (1981), 101–120.

38. Sime, M.E.; Green, T.R.G.; and Guest, D.J. Psychological evaluations of two conditional constructions used in computer languages. International Journal of Man-Machine Studies, 5 (1973) 105–113.

39. Vessey, I., and Conger, S.A. Learning to specify information requirements: the relationship between applications and methodology. Journal of Management Information Systems, 10, 2 (1993), 177–201.

40. Weiser, M. Programmers use slices when debugging. Communications of the ACM, 25, 7 (1984), 352–357.

41. Wiedenbeck, S. Processes in computer program comprehension. In E.S. Soloway and S. Iyengar (eds.), Empirical Studies of Programmers: First Workshop. Norwood, NJ: Ablex Publishing, 1986, pp. 48–57.

42. Wiedenbeck, S. The initial stage of program comprehension. International Journal of Man-Machine Studies, 35 (1991), 517–540.

43. Zuse, H. Software Complexity: Measure and Methods. New York: Walter de Gruyter, 1991.
