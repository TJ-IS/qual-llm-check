---
otero_id: 21491
otero_key: "DCUHZKHH"
title: "Hitting the wall: errors in developing and code inspecting a `simple' spreadsheet model"
authors: "Raymond R Panko; Ralph H Sprague"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00038-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hitting the wall: errors in developing and code inspecting a ‘simple’ spreadsheet model <sup>1</sup>

Raymond R. Panko <sup>)</sup>, Ralph H. Sprague Jr. <sup>2</sup>

UniÕersity of Hawaii, 2404 Maile Way, Honolulu, HI 98821, USA

## Abstract

Field audits and experiments have found substantial error rates when students and professionals have built spreadsheet models. In this study, 102 undergraduate MIS majors and 50 MBA students developed a model from a word problem that was relatively simple and free of domain knowledge. Even so, 35% of their 152 models were incorrect. There was no significant difference in errors per model between undergraduates and MBAs. Even among the 17 MBAs with 250 h or more of experience, 24% of the models contained errors. The cell error rate CER —the percentage of cells with errors—wasŽ . 2.0%. When 23 undergraduates attempted to audit their models through code inspection, only three with incorrect spreadsheets 15% produced clean spreadsheets when they finished the audit.Ž . q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Audit; Code inspection; Decision support system; End user computing; Error; Fault; Spreadsheet; Modeling

## 1. Introduction

## 1.1. The importance of spreadsheet modeling

Spreadsheet modeling is enormously important in business. Spreadsheet modeling has long been among the most widely used PC applications 28,37,42 ,<sup>w</sup> <sup>x</sup> especially among managers 28 . Many spreadsheet<sup>w</sup> <sup>x</sup> models guide important organizational decisions. It is difficult to imagine a firm making a critical decision without ‘going through the numbers’ with a spreadsheet model.

If anything, spreadsheet modeling should grow in importance in the future. Sprague and Carlson 50<sup>w</sup> <sup>x</sup> said that there are three components of decision support systems DSSs : modeling, data manage-Ž . ment, and the user interface. Early spreadsheet programs were only strong in modeling. However the growth of macro languages and Microsoft’s Visual Basic for Applications have brought extensive tools for customizing the user interface and for linking various modules into a coherent whole. In addition, thanks to the Open Database Connectivity ODBCŽ . protocol, spreadsheet models on Windows PCs can access client<sup>r</sup>server databases.

Given the importance of spreadsheet programs, it would be a serious concern if even a small fraction of spreadsheets contain errors. Yet Table 1 suggests that spreadsheet errors actually are fairly common. The table presents summary data from a number of experiments and field audits of real-world spreadsheet models. Perhaps the most significant pattern in the table is that every one of these studies has found error rates that would be unacceptable in practice.

Table 1  
Selected studies of spreadsheet errors

<table><tr><td>Study</td><td>Remarks</td><td>Cell error rate (CER)</td><td>Error per model</td><td>Percent of models with errors</td></tr><tr><td colspan="5">Field audits</td></tr><tr><td>Butler [1996]4</td><td>273 operational models</td><td></td><td></td><td>10.7%</td></tr><tr><td>Cragg and King [1993] [12]</td><td>20 operational models</td><td></td><td></td><td>25%</td></tr><tr><td>Davies and Ikin [1987] [15]</td><td>19 operational models</td><td></td><td></td><td>21%</td></tr><tr><td>Hicks [1995]5</td><td>1 module with 19 submodules about to enter operation</td><td>1.2%</td><td> $2.4^a$ </td><td> $26\%^a$ </td></tr><tr><td colspan="5">Development experiments</td></tr><tr><td>Brown and Gould [1987] [8]</td><td>Minimal definition of errors</td><td></td><td>0.6</td><td>44%</td></tr><tr><td>Brown and Gould [1987] [8]</td><td>Broader definition of errors</td><td></td><td></td><td>63%</td></tr><tr><td>Hassinen [1988] [25]</td><td>Paper and pencil exercise</td><td> $4.3\%^b$ </td><td>0.8</td><td>55%</td></tr><tr><td>Hassinen [1988] [25]</td><td>Computer exercise</td><td></td><td>1.7</td><td>48%</td></tr><tr><td>Lerch [1988] [34]</td><td>Fill in formulas in template</td><td> $9.3\%^b$ </td><td></td><td></td></tr><tr><td>Janvrin and Morrison [1996] [29],Morrison [1995] [40]</td><td>Study 1: links between worksheets</td><td> $7\%-14\%^c$ </td><td></td><td>84%–95%</td></tr><tr><td>Janvrin and Morrison [1996] [29]</td><td>Study 2: links between worksheets</td><td> $8\%-17\%^c$ </td><td></td><td></td></tr><tr><td>Panko and Halverson [forthcoming] [43]</td><td>General business students, working alone</td><td>5.6%</td><td>2.4</td><td>79%</td></tr><tr><td>Panko and Halverson [forthcoming] [43]</td><td>General business students, working in groups of four</td><td>1.9%</td><td>0.8</td><td>64%</td></tr><tr><td>Teo and Tan [1997] [53]</td><td>Undergraduate students</td><td>2.0%</td><td>0.5</td><td>42%</td></tr><tr><td colspan="5">Code inspection experiments</td></tr><tr><td>Galletta et al. [1993] [21]</td><td>Finding errors in seeded models</td><td> $34\%-54\%^d$ </td><td></td><td></td></tr><tr><td>Galletta et al. [1996–1997] [22]</td><td>Finding errors in seeded models</td><td> $45\%-55\%^d$ </td><td></td><td></td></tr></table>

<sup>a</sup> Errors per model and percent of models with errors computed on basis of submodules.  
<sup>b</sup> Errors per formula cell.  
<sup>c</sup> Errors per inter-spreadsheet link.  
<sup>d</sup> Percent of seeded errors not detected.

One potential threat to external validity in the experimental data is the possibility that the tasks used in past experiments may have been too difficult for subjects or may have required task domain knowledge that the subjects did not possess. If so, the high error rates seen in past experiments could be reflections of task unsuitability rather than of spreadsheet development per se. To address this threat, our study used a task designed to be relatively simple and free of domain knowledge.

Another potential threat to external validity in the experimental data is that some experiments have used undergraduate students 25,34,43,53 . This<sup>w</sup> <sup>x</sup> raises the concern that undergraduates may be inadequate surrogates for spreadsheet developers in organizations. To address this concern, we drew our sample both from undergraduate business classes and from MBA classes. In addition, among the MBA subjects, we analyzed differences in error rates between inexperienced and experienced spreadsheet users.

From human error research in general 3,47 , we<sup>w</sup> <sup>x</sup> know that error is present in all cognitive processes. As a result, we must develop ways to reduce inevitable errors by detecting and correcting them. One way to do this in spreadsheet modeling is to conduct code inspections 17 , which involve the detailed <sup>w</sup> <sup>x</sup> examination of the model’s code after it is developed. Galletta et al. 21,22 conducted code inspec- <sup>w</sup> <sup>x</sup> tion experiments using spreadsheet models seeded with errors. The models used in these experiments were developed by the experimenter, rather than by actual subjects. To see if people may have more trouble code inspecting their own models, we had some of our subjects code inspect their own models.

Finally, we examined the types of errors that subjects made, using the Panko and Halverson 45<sup>w</sup> <sup>x</sup> taxonomy of logical, mechanical, and omission errors. We were especially interested in seeing if undergraduates, inexperienced MBA students, and experienced MBA students made different types of errors.

## 2. Research on errors

## 2.1. Errors in real-world spreadsheet models

In recent years, we have seen a scattering of reports about errors in real-world spreadsheet models <sup>w</sup> <sup>x</sup> 44 . Given the reluctance of organizations to publicize embarrassments, these incidents may be only the tip of a large iceberg. A number of consultants, based on personal experience, have claimed that 20% to 40% of all spreadsheet models contain errors <sup>w</sup> <sup>x</sup> 13,16,32,48 .

Table 1 shows that systematic field audits of real-world spreadsheet models have reinforced concerns about spreadsheet accuracy. These four audits involved data from 313 real-world models from over 200 organizations. These studies found errors in 10.7% to 26% of the spreadsheets or spreadsheet modules they examined. In addition, Dent described an audit in an Australian firm that found errors in <sup>3</sup> about 30% of all models . Freeman 20 , in turn,<sup>w</sup> <sup>x</sup> described a study by Coopers and Lybrand in London. This study found errors in 90% of all spreadsheet models with more than 150 rows.

Although the rates of errors found in these field audits varied somewhat, at least some of the differences probably are due to methodological differences. The Butler study, for example, analyzed spreadsheets with an automated analysis tool similar to a grammar checker for word processors <sup>4</sup>. This tool would not warn the auditor if the developer had used the wrong algorithm in a calculation. Nor would it catch many other errors. Cragg and King 12 , in<sup>w</sup> <sup>x</sup> turn, note that their audits were fairly brief only 2 hŽ per model and were done by a single person and so. may have missed errors. Only the Hicks field audit used a methodology similar to code inspection 17<sup>w</sup> <sup>x</sup> in programming <sup>5</sup>. It used a cell-by-cell team audit with one developer and two team members from other departments. This intensive code inspection found 45 errors in 3856 cells, for a cell error rate Ž . CER of 1.2%. Of 19 submodules, 26% had errors.

## 2.2. High error rates in experiments

While formal audits give us real-world data, they do not give us detailed information about the types of errors that people make when they create spreadsheet models. Nor do they tell us the frequency with which developers make errors. For such information, we need experiments in which numerous subjects perform an identical task. Table 1 shows results from a number of these experiments. All have found disturbingly high error rates.

In most experiments, a majority of the spreadsheet models that developers created contained at least one error. In addition, the CER—the percentage of cells containing errors—has been a few percent. For larger models, this suggests that the issue is not whether such models have errors but rather how many errors they contain.

Error rates differ across the experiments. However this too seems to reflect methodological differences. The studies by Brown and Gould 8 , Hassi-<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>6</sup> nen 25 , Panko and Halverson 43 , and Teo and<sup>w</sup> <sup>x</sup> Tan 53 looked at errors for entire models at the end<sup>w</sup> <sup>x</sup> of a development phase. They had similar error rates. In contrast, the Lerch 34 and Janvrin and Morrison<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 29 studies only looked at certain especially difficult formula cells. This could plausibly account for their higher CER.

## 2.3. Error rates in other cognitiÕe actiÕities

Reason 47 summarized recent cognitive research<sup>w</sup> <sup>x</sup> on human error. He argued that human cognitive processes are very fast and flexible, but their methods of operation inherently produce a small error rate. In other words, correct performance and errors are due to the same underlying mechanisms. In all human activities, there will be errors. The only question is the rate of uncorrected errors, that is, errors that are not detected and fixed by people as they work.

Research in other human cognitive activities have told us that errors are not merely inevitable; they are actually predictable. Research has produced human error data from a large number of experiments and real world incidents across many types of human cognitive activity. These data collectively suggest that human beings have a natural uncorrected error rate of about 1%, plus or minus an order of magnitude. Of course the error rate will depend on the task, as will the error detection and correction rate. However, if spreadsheet error research did not also find errors in roughly 1% of all cells, the research itself would be rather suspect.

In programming, for example, we have data from numerous code inspections 17 of real-world pro-<sup>w</sup> <sup>x</sup> grams developed by experienced programmers <sup>w</sup> <sup>x</sup> <sup>7,8,9</sup> 5,7,17,30,49,52 . From these studies, we know that programmers have uncorrected errors in 1% to 10% of their statements even after careful development but before intensive testing. More precisely, programmers refer to what we call errors as faults, and they report fault rates in terms of faults per thousand lines of non-comment source code, KLOC. While there are different ways to count errors and lines of code 1 , the consistency among real-world<sup>w</sup> <sup>x</sup> code inspections is striking, suggesting a natural underlying error level in human cognitive processing for programming tasks.

In programming, faults per KLOC has proven to be a good measure because it is highly independent of the length of the program module being studied e.g., 46 . It allows programmers to look at a core error rate in their work. We hope that the CER will be similarly useful. While larger spreadsheet models should have a larger number of errors than smaller models, we speculate that the CERs will be roughly similar, allowing us to see the underlying error rate in spreadsheet model development.

While spreadsheet models are often believed to be much simpler and smaller than programs, surveys of developers have shown that many spreadsheet models are both large 9,12,24 and complex 24 . Third-<sup>w</sup> <sup>x</sup> <sup>w x</sup> generation language programs studied in field audits, in turn, tend to be built in relatively small modules. So finding comparable error rates should not be surprising.

Also encouraging us to believe that the error rates shown in Table 1 are reasonable is the fact that comparable error rates have been found in a variety of other computer applications 10,11 , even when <sup>w</sup> <sup>x</sup> expert subjects are used. There are also similar to error rates when subjects use a calculator or look up numbers from a table 38 .<sup>w</sup> <sup>x</sup>

## 2.4. Error cascades

In most matters, a handful of uncorrected errors in every hundred actions is a small penalty for speed and flexibility. But when there are long sequences of computations, as in spreadsheet models, even very low error rates cascade rapidly into a high probability of a bottom-line error.

Lorge and Solomon 35 developed a general<sup>w</sup> <sup>x</sup> method for analyzing error cascades. This method allows us to compute the probability of an error in a cascade of spreadsheet model cells. If there are N stages in this case,Ž . N cells in a cascade , and if the error rate per state is e Ž . in this case, the CER , then the probability of an error in the bottom-line value at the end of the cascade, E will be given by this formula:

$$
E = 1 - (1 - e) ^ {N}\tag{1}
$$

For instance, suppose that the CER is 2% and that there are only 50 cells in the cascade to a certain bottom line value. Then the probability of an error in the bottom line value will be 64%! Quite simply, unless the CER is vanishingly small, the probability of a bottom line error will be quite large. In fact, for larger models, the issue will be how many errors the model is likely to have. For the conditions in Eq. 1 , Ž . this would be the CER times the number of cells in the spreadsheet model.

## 2.5. Research in error detection and correction

Errors are inevitable. We know from protocol analysis studies in statistics problem solving 2 and <sup>w</sup> <sup>x</sup> writing 26 that people both detect and correct errors<sup>w</sup> <sup>x</sup> as they go along and also engage occasionally in more systematic error checking episodes, in which they go back over their work before they finish. From these studies, we also know that they miss many of their errors. For simple slips, the detection and correction rate is over 90%. For more complex errors, the error rate is much lower.

In programming, we know that we have to spend about a third of the total development time on systematic error checking after development. Otherwise, our programs will have an unacceptably high number of errors upon delivery. Often, this systematic error checking takes the form of team code inspection <sup>w</sup> <sup>x</sup> 17 . Team code inspection is used because both experiments and field experience have shown that individual inspectors will not catch a large fraction of all programming errors in programs. In experiments, the subjects of Basili and Selby 4 and Myers<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 41 only caught half of all seeded errors in test programs. As Table 1 show, the studies of Galletta et al. 21,22 had similar error detection rates with<sup>w</sup> <sup>x</sup> spreadsheet models seeded with errors. Tjahjono’s <sup>w</sup> <sup>x</sup> 14 subjects detected only 22% of seeded programming errors.

One concern with past laboratory studies is that the seeded models were developed by the experimenter rather than by subjects. As a result, the seeded experiments and spreadsheet models have followed good design practices. Subjects might have a more difficult time inspecting their own programs. First, many of their models used poor design and so might be difficult to read. Second, it seems plausible that people may have a harder time inspecting their own models than the models of others.

## 2.6. Types of errors

We noted earlier that error detection and correction rates seem to depend on the type of errors that are made. Several categorizations have been suggested for spreadsheet errors. We will follow the taxonomy created by Panko and Halverson 45 .<sup>w</sup> <sup>x</sup> They divided errors into mechanical, logical, and oversight errors, based on a classification scheme developed by Allwood 2 to study students working on statistics problems.

## 2.6.1. Mechanical errors

Mechanical errors include mistyping a number, accidentally typing a plus sign instead of a minus sign, pointing to a wrong cell when entering a formula, reading a number incorrectly from a problem statement, or selecting the wrong range. In the human error literature, they are often called slips 3 .<sup>w</sup> <sup>x</sup>

Surveying several typing studies, Kukich 33<sup>w</sup> <sup>x</sup> found that expert typists make uncorrected keystroke Ž . mechanical errors in 0.5% to 1% of all characters typed. In another related area, Swain and Guttman conducted simulations of nuclear plant operation <sup>10</sup>. They found that for simple tasks, such as selecting the right switch, error rates were between 0.3% and 1%.

In his field audit of a spreadsheet about to become operational, Hicks found that 64% of the errors discovered were mechanical errors, with pointing errors being the most common type of mechanical error <sup>5</sup>. In their spreadsheet experiments, Brown and Gould 8 , Floyd and Pyun 18 , and Lerch 34 all<sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> found considerable numbers of errors that we would classify as mechanical.

## 2.6.2. Logic errors

Logic errors involve faulty reasoning instead of simple mechanical slips. Logic errors include the use of the wrong algorithm or implementing the algorithm with the wrong logic. For instance, in our task, the subject had to add 30% to labor costs to account for fringe benefits. Some subjects divided labor costs by 70% instead of multiplying it by 130%. If it took you a second or two to see why that was incorrect, you see the subtlety of many logic errors.

Logic errors have been studied in other cognitive domains. In statistics for example, Allwood 2 found<sup>w</sup> <sup>x</sup> many logic errors in statistical problem solving by novices. In programming, we have long known that logic errors are important even in programs by expert programmers. In one study of 4339 lines of code at Aetna, for instance, 51% of the errors discovered were logic errors 17 .<sup>w</sup> <sup>x</sup>

Panko and Halverson 43 found many logic er- <sup>w</sup> <sup>x</sup> rors in their spreadsheet experiment and subdivided logic errors into Eureka errors 35 , which are easy to <sup>w</sup> <sup>x</sup> prove to be incorrect, and Cassandra errors, which are difficult to prove to be incorrect. This distinction was important because some subjects worked in teams. It was hypothesized that teams would have a difficult time dealing with Cassandra errors, and this in fact proved to be true. Panko and Halverson 45<sup>w</sup> <sup>x</sup> suggested additional ways to subcategorize logic errors. Among the spreadsheet studies in Table 1, <sup>5</sup> Hicks, Brown and Gould 8 , and Lerch 34 all<sup>w x</sup> <sup>w</sup> <sup>x</sup> found logic errors.

## 2.6.3. Omission errors

Finally, omission errors involve leaving something out of a model. For example, to compute the amount of a loan that he would need when purchasing a new home, one analyst forgot to include paying off the old mortgage, even though he had included the mortgage payoff in several previous analyses of the sale.

Specifically, in an experiment, an omission error is omitting a parameter given in the task statement. For instance, if respondents have to compute labor costs, they may forget to include fringe benefits or may forget that there are two members of a work team.

Only 4% of Hicks’ errors were omissions, although the main logic error consisted of omitting a parameter from an equation <sup>5</sup>. In the Brown and Gould 8 experiment, when omission errors were<sup>w</sup> <sup>x</sup> excluded, 44% of the spreadsheet models had errors.

When omission errors were included, this rose to 63%.

Omission errors are dangerous because they seem to be very difficult for developers to detect. Allwood’s 2 subjects detected<sup>w</sup> <sup>x</sup> none of their omission errors. In simulations of nuclear emergencies, Woods’ subjects never corrected misdiagnoses of the problem <sup>11</sup>.

It can be argued that the Panko and Halverson <sup>w</sup> <sup>x</sup> 45 taxonomy should be a two-by-two matrix, with errors of omission and commission for both mechanical and logic error rates. Indeed, this would be ideal. However it is very difficult in practice to characterize omission errors as logical or mechanical without interrogating subjects as they work. Panko and Halverson 43 did not do so. Nor did we in this<sup>w</sup> <sup>x</sup> Ž experiment..

Some writers, including Reason 47 , merge omis-<sup>w</sup> <sup>x</sup> sion and commission errors. However, given differences in detection and correction rates found between omission and other errors in past studies, it seems best to keep a specific omission category.

## 3. Research goals and hypotheses

Now that we have surveyed past research on spreadsheet errors, we will turn to our specific research goals and hypotheses.

## 3.1. Measuring error rates for a simple model

As discussed above, the error rates seen in past laboratory studies could plausibly be due to the tasks being too difficult for subjects or requiring task domain knowledge that subjects did not possess. So one research goal was to develop a simple and relatively domain-free model, then measure error rates for subjects. Given past research shown in Table 1, we selected three measures of error rates: the percentage of incorrect models containing at least one error, the number of errors per model, and the CER.

3.2. Comparing error rates for different types of subjects

As discussed earlier, many studies have been done with undergraduate subjects. This led to our goal of having different types of subjects do the task, so that we could compare their error rates. We chose to compare undergraduate business students with MBA students, to see if the latter group would in fact make fewer errors. We also wished to compare inexperienced with experienced spreadsheet developers. This was only possible to do among our MBA students. These goals led to the following specific hypotheses: a H1, MBA students make fewer errors Ž . per model than undergraduate students. b H2, Ex- Ž . perienced MBA students make fewer errors per model than inexperienced MBA students.

## 3.3. Types of errors

Given the taxonomy of error types given earlier, we wished to measure the percentages of errors that would fall into the logical, mechanical, and omission error categories.

## 3.4. Code inspection

As discussed earlier, code inspection studies to date have used models developed by the experimenter. Consequently, we wished to know if subjects code inspecting their own models will find fewer errors than the 50% figures found by Galletta et al. <sup>w</sup> <sup>x</sup> 21,22 . We did not create a formal hypothesis because this part of the research was exploratory. We had no independent data to tell us if a randomlyselected sample of subjects would correct 50% of the errors in these specific models.

## 3.5. Identifying subjects who made errors

In most human activities, there is a range of ability within the population. In general, studying individual differences in human error is extremely difficult, because in any given task, most subjects make no errors and the rest make only a handful. With a different task, or perhaps even with the same task on another day, the results could be different in terms of who makes errors and how many errors they make. To study individual differences conclusively in human error domains requires giving subjects a long series of tasks, in order to get a good average error rate for individuals. Nevertheless, the fact that we had a post-experiment questionnaire allowed us to compare subjects who made errors in our single task with subjects who did not. This part of the analysis was completely exploratory.

## 4. Methodology

## 4.1. The sample

The sample consisted of 152 students at the University of Hawaii. All participated as a class requirement. Students received full credit if they ‘gave the project their best shot.

In the sample, 102 subjects were upper-division undergraduate business students. All were MIS majors. All had previously taken two accounting courses and an introductory computer course that covered spreadsheet mechanics. An additional six undergraduates were excluded from the sample because their models or disks were unreadable.

The remaining 50 subjects were MBA students who had previously taken an accounting class or who had waived the class because of a previous accounting course. For spreadsheet modeling, all had taken the required course covering this topic or were currently taking the course. Those currently taking the course had already covered the spreadsheet modeling part of the course. An additional five MBA students were given the task but were excluded from in the sample because their models or disks were unreadable.

Following the procedures used by Galletta et al. <sup>w</sup> <sup>x</sup> 21 , MBA students were subdivided into inexperienced and experienced spreadsheet developers based on hours of experience. Inexperienced subjects were those with 100 h or less of spreadsheet experience. Experienced subjects were those with 250 h or more of experience. Following Galletta et al. 21 , we only <sup>w</sup> <sup>x</sup> considered development, auditing, and training experience. We did not consider time spent typing numbers into spreadsheets created by others.

There were 26 inexperienced spreadsheet developers in our MBA sample. They had a mean of only

11 h of experience. Twenty-one had no experience developing models at work. There were 17 experienced spreadsheet developers in the MBA sample. Their mean hours of experience was 2269. The median was 635. One subject with 200 h of experience was not categorized because he or she had more than 100 h but less than 250. Another six could not be categorized because of ambiguities in their responses to the experience scale.

In a post-experiment questionnaire, subjects rated their spreadsheet expertise. The mean on a 7-point scale was 4.8 4.8 for undergraduates, 4.7 for MBAs .Ž . Sixty-two percent used the three highest values on the scale. Another 21% selected the middle value.

Another question asked about the adequacy of their spreadsheet knowledge for the experimental task. Eight-eight percent rated their spreadsheet knowledge as adequate. Another 11% rated their knowledge as barely adequate. One subject rated his or her knowledge as inadequate. This MBA student, however, built a correct model. Undergraduate and graduate distributions were almost identical. This distribution seems reasonable, because the task only required basic spreadsheet skills.

In a third question, we asked subjects if they had a difficult time with the spreadsheet knowledge required for the specific task in the experiment. Eighty-six percent disagreed, with 56% choosing extreme disagreement on the 7-point scale. Ten percent agreed, with 1% choosing extreme agreement.

## 4.2. Procedure

The subjects did not work in the laboratory. Instead, they took the experimental materials home in a sealed envelope. They opened the envelope while sitting in front of a blank spreadsheet file. They had 45 min to do the task, which was about twice the length of time subjects averaged on a pre-test. Eighty-nine percent said that they had sufficient time, 5% choose the neutral value on a 7-point scale, and 6% chose values of 1 through 3. Seventy-three percent chose 7, indicating strongest agreement.

Not using the control of laboratory work is controversial. However there was little incentive to cheat, because subjects knew that they would get full credit if they merely gave the task their best effort.

More importantly, we argue that not doing the task in a laboratory added to realism. One concern with laboratory studies is that they are unrealistic and so create errors. By allowing subjects to work in a more comfortable environment, we hoped to reduce that threat to external validity.

As a cross check, we had another 10 undergraduate subjects do the development task in the laboratory. Thirty percent had errors, in contrast to 37% of the undergraduates who did the assignment on a take-home basis. The difference in number of errors per spreadsheet was not significant. In addition, if people working at home had cheated, we would expect them to have had a lower rate of incorrect spreadsheets. We also checked each of the models in this study to ensure that they were not merely copies of someone else’s work.

The packet contained a consent form and a set of instructions. Both were explained in class before handing out the packet. The packet also contained a brief problem statement, which we present below.

Finally, the packet also contained a post-experiment questionnaire. This questionnaire asked about the subjects’ perceptions of the problem, the experiment experience, their performance, and their background.

When some undergraduate subjects returned their packets, they were given 10 min of in-class instruction on the data in Table 1. The purpose was to sensitize them to the dangers of spreadsheet errors. They were then taught for 10 min how to code-inspect a model by going through it cell-by-cell. We showed them how to check for incorrect formulas and noted that they need to check facts in the model against those in the problem statement. We showed them how to use Excel’s tools for drawing arrows to the cells referred to in formulas. The subjects were then given their disks and problem statements to take home again and code inspect.

## 4.3. The task

As discussed earlier, the task was designed to be simple and relatively domain-free. Fig. 1 shows the specific task used in the experiment. We call it the ‘Wall Task,’ because it requires the subject to prepare bids for building a wall made of either brick or lava rock. The domain knowledge consists of measuring the wall’s volume, multiplying this by the cost per cubic foot, simple labor calculations, and the additions of fringe benefits and a profit margin.

In the post-experiment questionnaire, we asked respondents to rate the problem’s difficulty on a 5-point scale, with 5 being high. Sixty-six percent of the respondents chose 1 or 2, and another 29% chose 3. Only 5% chose values at the high difficult end ofŽ . the scale. We seem to have succeeded in producing a relatively simple problem from most subjects’ point of view.

In another question, we asked respondents if they had a difficult time with the knowledge required in the problem. Seventy percent disagreed, with 41% choosing extreme disagreement. Sixteen percent agreed, with 2% choosing extreme agreement.

## 4.4. Error determination

To assess errors, we used a standard spreadsheet solution. Fig. 2 shows this solution.

The first author compared the subjects’ models with the standard solution. If there was no error in the bottom line values, he recorded that fact. If a bottom line value in the subject’s model was incorrect, he identified the errors and corrected them until the model gave the correct bottom line values.

<table><tr><td>Labor Hours</td><td></td><td></td></tr><tr><td>Days per person</td><td>3</td><td></td></tr><tr><td>Hours per day</td><td>8</td><td></td></tr><tr><td>Hours per person</td><td>24</td><td></td></tr><tr><td>People</td><td>2</td><td></td></tr><tr><td>Hours</td><td>48</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Labor Cost</td><td></td><td></td></tr><tr><td>Pay per hour</td><td>$10</td><td></td></tr><tr><td>Pay</td><td>$480</td><td></td></tr><tr><td>Fringe benefit rate</td><td>20%</td><td></td></tr><tr><td>Fringe benefits</td><td>$96</td><td></td></tr><tr><td>Labor cost</td><td>$576</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Wall Volume</td><td></td><td></td></tr><tr><td>Height</td><td>6</td><td></td></tr><tr><td>Length</td><td>20</td><td></td></tr><tr><td>Thickness</td><td>2</td><td></td></tr><tr><td>Volume</td><td>240</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Materials Cost</td><td>Brick</td><td>Lava</td></tr><tr><td>Cost per cubic foot</td><td>$2</td><td>$3</td></tr><tr><td>Materials cost</td><td>$480</td><td>$720</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Total Cost and Bid</td><td>Brick</td><td>Lava</td></tr><tr><td>Labor plus materials cost</td><td>$1,056</td><td>$1,296</td></tr><tr><td>Profit margin rate</td><td>30%</td><td></td></tr><tr><td>Profit margin</td><td>$317</td><td>$389</td></tr><tr><td>Bid</td><td>$1,373</td><td>$1,685</td></tr></table>

Fig. 2. Standard solution for the wall problem.

Omission Error

Failing to include a fact explicitly given in the task statement

Logic Error

A mistake caused by the subject having the wrong algorithm for solving the step or making a mistake implementing the algorithm

Mechanical Error

An error caused by a simple slip such as pointing to the wrong cell, mistyping a number, typing the wrong operator, selecting the wrong cell or range, misreading a number from the task statement, and so forth

Fig. 3. Rules for Classifying Errors by Type. a Omission error, failing to include a fact explicitly given in the task statement; b LogicŽ . Ž . error, a mistake caused by the subject having the wrong algorithm for solving the step or making a mistake implementing the algorithm; cŽ . Mechanical error, an error caused by a simple slip such as pointing to the wrong cell, mistyping a number, typing the wrong operator, selecting the wrong cell or range, misreading a number from the task statement, and so forth

## 4.5. Classifying errors

Of the 63 errors, 61 were classified as mechanical, logical, or omission errors. Two errors couldŽ not be classified because the original spreadsheets were damaged. As the first author corrected errors,. he wrote a brief description of each error. After the descriptions were collected, both authors independently classified errors into mechanical, logical, and omission errors. Fig. 3 shows the definitions they used. They disagreed upon only two errors initially. One was indisputably an omission error; it involved leaving a fact in the problem statement out of the model. One of the authors, however, initially classified it as a mechanical problem. The second involved multiplying the labor cost by 0.2 to give labor cost plus fringe benefits. The labor cost should have been multiplied by 1.2. One author classified this as a mechanical error, the other as a logic error. Based on the fact that students in homework assignments frequently make the mistake of multiply by a factor instead of by one plus the factor, it was jointly decided that this was a logic error. Identical mechanical errors are not made frequently by multiple people. Measured by the kappa statistic 6 , the inter-rater<sup>w</sup> <sup>x</sup> reliability was 0.939.

## 5. Results

Table 2 summarizes results for both the development and code inspection phases of the experiment.

## 5.1. Undergraduates Õs. MBAs

A quick scan of Table 2 indicates that MBAs did not do much better than undergraduates. Even a quarter of the MBA students with more than 250 h of model development experience had errors in their models. Confirming this impression, t-test for undergraduates vs. MBAs had a probability of 0.223. Hypothesis H1, that MBA students make fewer errors per model than undergraduate students, was not supported.

An F-test comparing undergraduates, experienced MBAs and inexperienced MBAs also found no statistically significant difference, with a probability of 0.414. The difference between experienced and inexperienced MBAs had a probability of 0.112, based on a t-test for the number of errors in the model. Hypothesis H2, that experienced MBA students make fewer errors per model than inexperienced MBA students, was not supported.

A larger sample of experienced MBAs might have produced statistical significance. However even if the difference between experienced and inexperienced MBA students had been statistically significant, it would make little practical difference. Even on this simple problem, a quarter of the experienced MBA students made errors. This fraction is unacceptable from a business viewpoint. So trying to predict differences in error rates across groups, while potentially useful in assessing detailed error rates, would leave intact the main error finding—that all groups produced a level of errors that would be unacceptable in practice.

T<sub>a</sub>bl<sub>e</sub> 2 S<sub>ummary</sub> <sub>o</sub>f <sub>resu</sub>lt<sub>s</sub>

<table><tr><td></td><td>Total sample</td><td>Undergrad MIS majors</td><td>All MBA students</td><td>InexperiencedaMBA students</td><td>ExperiencedaMBA students</td></tr><tr><td colspan="6">Development phase</td></tr><tr><td>Number of subjects</td><td>152</td><td>102</td><td>50</td><td>26</td><td>17</td></tr><tr><td>Spreadsheets with errors (%)</td><td>35%</td><td>37%</td><td>30%</td><td>35%</td><td>24%</td></tr><tr><td>Errors per spreadsheet (mean)</td><td>0.41</td><td>0.44</td><td>0.36</td><td>0.46</td><td>0.24</td></tr><tr><td>Standard deviation</td><td>0.61</td><td>0.62</td><td>0.60</td><td>0.71</td><td>0.44</td></tr><tr><td>Total errors</td><td>63</td><td>45</td><td>18</td><td>12</td><td>4</td></tr><tr><td>CER (cell error rate) overall</td><td>2.0%</td><td>2.2%</td><td>1.7%</td><td>2.3%</td><td>1.1%</td></tr><tr><td colspan="6">Code inspection phaseb</td></tr><tr><td>Inspected spreadsheets with errors</td><td>23</td><td></td><td></td><td></td><td></td></tr><tr><td>Models corrected completely</td><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>% of models corrected completely</td><td>13%</td><td></td><td></td><td></td><td></td></tr><tr><td>% of errors corrected</td><td>18%</td><td></td><td></td><td></td><td></td></tr></table>

Th<sub>e</sub> t-t<sub>es</sub>t f<sub>or</sub> th<sub>e num</sub>b<sub>er o</sub>f <sub>errors per mo</sub>d<sub>e</sub>l f<sub>or un</sub>d<sub>ergra</sub>d<sub>ua</sub>t<sub>es vs</sub> . MBA<sub>s</sub> h<sub>a</sub>d <sub>a pro</sub>b<sub>a</sub>bilit<sub>y o</sub>f 0.223 .  
Th<sub>e</sub> F-t<sub>es</sub>t f<sub>or</sub> diff<sub>erences</sub> i<sub>n</sub> th<sub>e num</sub>b<sub>er o</sub>f <sub>errors per mo</sub>d<sub>e</sub>l <sub>among un</sub>d<sub>ergra</sub>d<sub>ua</sub>t<sub>es</sub> i<sub>nexper</sub>i<sub>ence</sub>d MBA<sub>s an</sub>d <sub>exper</sub>i<sub>ence</sub>d MBA<sub>s</sub> h<sub>a</sub>d <sub>a pro</sub>b<sub>a</sub>bilit<sub>y o</sub>f 0.4 1 4  
<sup>a</sup> E<sub>xper</sub>i<sub>ence</sub>d MBA <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t<sub>s</sub> h<sub>ave</sub> h<sub>a</sub>d 250 h <sub>or</sub> <sub>more</sub> <sub>o</sub>f <sub>crea</sub>ti<sub>ng,</sub> <sub>au</sub>diti<sub>ng,</sub> <sub>an</sub>d t<sub>eac</sub>hi<sub>ng</sub> <sub>sprea</sub>d<sub>s</sub>h<sub>ee</sub>t<sub>s</sub> <sub>a</sub>t <sub>wor</sub>k. I<sub>nexper</sub>i<sub>ence</sub>d MBA <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t<sub>s</sub> h<sub>a</sub>d 1 00 h <sub>or</sub> f<sub>ewer</sub>.  
<sup>b</sup> C<sub>o</sub>d<sub>e</sub> i<sub>nspec</sub>ti<sub>ons</sub> <sub>were</sub> <sub>on</sub>l<sub>y</sub> d<sub>one</sub> b<sub>y</sub> 23 <sub>un</sub>d<sub>ergra</sub>d<sub>ua</sub>t<sub>e</sub> <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t<sub>s</sub> . N<sub>o</sub> <sub>s</sub>t<sub>u</sub>d<sub>en</sub>t <sub>w</sub>ith <sub>a</sub> <sub>correc</sub>t <sub>sprea</sub>d<sub>s</sub>h<sub>ee</sub>t <sub>mo</sub>d<sub>e</sub>l <sub>c</sub>h<sub>ange</sub>d it d<sub>ur</sub>i<sub>ng</sub> <sub>co</sub>d<sub>e</sub> i<sub>nspec</sub>ti<sub>on</sub>.

Because of the lack of statistical significance, our reporting will focus on data from the total sample. Table 2, however, gives more specific information by group.

## 5.2. Spreadsheets with errors

The simplest measure of errors is the fraction of all spreadsheet models that contained errors. In this study, 53 of the 152 spreadsheets developed by the subjects had errors. Although this 35% error rate was lower than the error rates found in past experiments, it was still quite high. Even with a rather simple and domain-free task, errors were abundant.

## 5.3. Numbers of errors

As in the studies by Brown and Gould 8 , Panko<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> <sup>6</sup> and Halverson 43 , and Hassinen 25 , although the fraction of spreadsheets with errors was high, the subjects actually made very few errors per model on the average. Our subjects only made 63 errors—a mere 0.42 errors per model. Even among the 53 models with errors, only 10 had two errors. None had more than two.

As Panko and Halverson 43 discussed, the prob- <sup>w</sup> <sup>x</sup> lem with spreadsheets is not that people make a large number of errors. It is that there are many cells on the logic cascades of cells leading to the bottom line figures. As noted earlier, even a tiny CER will be multiplied over a logic cascade into a high probability of an error in bottom line values.

## 5.4. Cell error rate

As discussed earlier, we are especially interested in the CER—the number of errors per hundred model cells. Our subject models averaged 20.5 cells per spreadsheet, with a high standard deviation of 7.6. There was no statistical difference between correct spreadsheets 20.7 cells and incorrect spread- Ž . sheets 20.2 cells .Ž .

The 152 models had a total of 3116 cells. The subjects made 63 errors, so the cell error rate was 2.0%. If the CER had been based on the standard solution’s 25 cells per model, the CER would be 1.7%.

As expected, given the simple nature of the task, this cell error rate was lower than those in shown in Table 1. This suggests that our problem was indeed simpler than past problems. The only exception is the Teo and Tan 53 study, which also used our<sup>w</sup> <sup>x</sup> Wall Task <sup>12</sup>.

However even this relatively low CER would still be unacceptable in the real world. In large models, having 2% of all cells in error would mean not just a high probability of an error in the bottom line but also a high number of errors per model. As noted earlier, the Hicks field audit had a CER of 1.2% and found many errors in the model audited <sup>5</sup>.

## 5.5. Types of errors

The study by Panko and Halverson 43 noted that<sup>w</sup> <sup>x</sup> subjects made many distinct errors. This was also true in the current study. Table 3 shows the errors made by subjects.

Table 3 shows that undergraduates and MBAs made extremely similar percentages of omission, logic, and mechanical errors. In fact, despite the relatively small number of errors, this similarity extended down even to common individual errors within categories.

## 5.5.1. Omission Errors

Omission errors were the most common, accounting for 54% of all errors. Interestingly, there were only five distinct omission errors, and all but one were committed more than once. One error—forgetting that there were two people in each work crew—accounted for a third of all errors in the entire experiment.

In fact, there were 25 omission errors in the computation of labor cost. These accounted for almost half the errors in the total study. One possible explanation is that the number of facts in the problem statement for the computation of labor costs was fairly large, so that subjects may have had a difficult time retaining the information in their limited working memory. Our subjects could have used scratch paper to write down facts as they worked, but we collected all papers the subjects used, and very few wrote facts on the task statement or on scratch paper. Various omitted facts may have literally dropped out of memory. This may be a fruitful area for further research. This is plausible because we have long known that working memory can only hold about seven items 39 . This limited working memory is <sup>w</sup> <sup>x</sup> used not only to hold numbers but also to hold plans for the algorithm being considered and for broader planning 3,47 . Mattson and Baars 36 argued that<sup>w</sup> <sup>x</sup> <sup>w x</sup> error detection is in part determined by available attentional resources. If the resources are not sufficient, they argued, omission errors will occur.

Table 3 Errors by type

<table><tr><td>Type of error</td><td>Number of errors</td><td>% of errors for total sample</td><td>% of errors for undergrads</td><td>% of errors for MBAs</td></tr><tr><td>Omission errors</td><td>33</td><td>54%</td><td>56%</td><td>50%</td></tr><tr><td>Omitted two workers in labor calculation</td><td>20</td><td>33%</td><td>35%</td><td>28%</td></tr><tr><td>Omitted 30% profit margin</td><td>4</td><td>7%</td><td>7%</td><td>6%</td></tr><tr><td>Omitted fringe benefits</td><td>4</td><td>7%</td><td>7%</td><td>6%</td></tr><tr><td>Omitted 3 days in labor calculation</td><td>4</td><td>7%</td><td>7%</td><td>6%</td></tr><tr><td>One other omission error occurred once</td><td></td><td></td><td></td><td></td></tr><tr><td>Logic errors</td><td>26</td><td>43%</td><td>42%</td><td>44%</td></tr><tr><td>Profit margin on materials only</td><td>6</td><td>10%</td><td>9%</td><td>11%</td></tr><tr><td>For profit margin, divided by 0.7</td><td>5</td><td>8%</td><td>7%</td><td>11%</td></tr><tr><td>Two other logic errors occurred twice</td><td></td><td></td><td></td><td></td></tr><tr><td>11 other logic errors occurred once</td><td></td><td></td><td></td><td></td></tr><tr><td>Mechanical errors</td><td>2</td><td>3%</td><td>2%</td><td>6%</td></tr><tr><td>Two mechanical errors occurred once</td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td>61</td><td>100%</td><td>100%</td><td>100%</td></tr></table>

Two errors could not be classified because of damage to the spreadsheet models.

## 5.5.2. Logic errors

Logic errors were almost as numerous but were more diverse. While there were only five distinct omission errors, there were 16 distinct logical errors. At least in this study, then, logic errors were much less predictable than omission errors. There seems to be a strong random element in logic error-making.

## 5.5.3. Mechanical Errors

Mechanical errors were almost nonexistent; there were only two definite mechanical errors. One was a pointing error, while the other appeared to be an error in reading and then writing down the fringe benefit rate. The popular perception of spreadsheet errors as pointing and typographical errors was not borne out in this study.

Typographical errors, in fact, were nonexistent, although one or two errors classified in other ways could possibly have been typographical errors. This lack of typographical errors was astonishing, because skilled typists make one uncorrected error in about every 200 keystrokes 33 . In contrast, our subjects <sup>w</sup> <sup>x</sup> probably hit 20,000 to 30,000 keys without making a single uncorrected typographical error in numbers and formulas we did not study text cells . Ž .

## 5.5.4. Types of errors: implications

The wide variety of errors suggests that when we audit spreadsheets it will not be enough to inspect parts of the problem that seem especially difficult and to ignore other parts of the model. Although some types of errors are more likely than others, error-making appears to be extremely diverse. If this is generally true, it will mean that specific errors will not be very predictable. From one study, of course, we cannot draw general conclusions. We need to see if similar patterns appear in other experiments and, more importantly, in real-world spreadsheet models.

## 5.6. Code inspection

As noted earlier, some subjects were given their models back with instructions to code inspect them. This was not possible in all undergraduate classes or in MBA classes from which subjects were drawn.

None of the subjects with correct spreadsheets made any changes. Of the subjects with incorrect spreadsheets, 23 attempted to correct their spreadsheets. As discussed above, we anticipated that our subjects would do poorly because they were inspecting their own models and because their models tended to be difficult to read. Indeed, only three of the 23 subjects with errors 13% corrected theirŽ . spreadsheets. Another 17 made no changes. Three caught a single error in a two-error model, and one other actually added an error without fixing any. Counting errors instead of models, the subjects fixed only 21% of their 23 errors. Counting the subject who added an error during the code inspection, a net of 18% of the errors were fixed.

Our error rates are higher than those found in the code inspection studies by Galletta et al. 21,22 . In <sup>w</sup> <sup>x</sup> those studies, subjects caught about half of all seeded errors. One might dismiss our higher error detection rates by saying that our students were undergraduates, while Galletta et al. used CPAs and MBAs. However we gave the 1996 Galletta et al. problem set and half of the 1993 problem set to another group of 26 undergraduate MIS majors. The other half ofŽ the 1993 problem set involved accounting knowledge we could not assume for our students. Our. undergraduate subjects caught almost exactly the same fraction of errors that the Galletta et al. subjects 21,22 caught. So class standing cannot be the<sup>w</sup> <sup>x</sup> whole story.

## 5.7. Who makes errors?

Can we distinguish between people who make errors and people who do not? In general, the questions that we asked on the post-experiment questionnaire provided little power to distinguish people who built correct spreadsheets from those who did not.

We asked 36 questions that might have distinguished between the two groups of subjects. Among those that did not distinguish between spreadsheets with errors and clean spreadsheets at the 0.05 cut-off were confidence in the accuracy of the spreadsheet and various measures of prior knowledge. Only three questions distinguished subjects who made errors from those that did not at the 0.05 cut-off.

First, when asked for the best number of people to have done the model development in a team, subjects with errors had a mean of 1.7 people, while for subjects without errors, the mean was 1.4. This suggests that the subjects who made errors may have been somewhat lacking in confidence after the experiment, despite their answers to direct confidence questions.

Second, subjects who made errors were more likely to have said that they had a difficult time with the accounting knowledge required in the problem Ž . 2.94 on a 7-point scale. than were those who did not have errors 2.32 . However, the difference inŽ . means was small.

Third, subjects who did not have errors rated their accounting expertise somewhat higher 4.70 on aŽ 7-point scale than did subjects who had errors 4.10 .. Ž .

These few differences, although statistically significant, were too small to have any practical predictive power. It appears that giving people questionnaires to assess whether or not they commit errors will not have much predictive power. In addition, given 36 questions, three positives is about what one would expect by chance.

These results seem to suggest that error-making has a strong random element. The same people who made errors in this experiment might be the people with correct spreadsheets in another experiment. Of course, there might be other factors that we have not taken into account.

## 6. Conclusion

One threat to external validity in past spreadsheet experiments has been the concern that tasks used in the experiments were too difficult for subjects or required domain knowledge that subjects did not possess. To assess this possibility, our subjects used a task that was simple and relatively free of requirements for domain knowledge. Although our subjects did have somewhat lower error rates than subjects in past experiments, our subjects still made errors in 35% of their models and in 2.0% of all cells. If real-world spreadsheets had even an order of magnitude fewer errors, this would still be too much for safety in corporate spreadsheet development. When our subjects code inspected their own models for errors, furthermore, they found only about one error in ten. Overall, the concern that past experiments used problems that were too difficult for the subjects cannot be used to dismiss our subjects’ unacceptably high error rates.

Quite simply, to err is human. Human factors studies, including those using computers, have consistently shown that while people do not make many errors, they do have natural error rates that often are on the order of 1% or more of their actions. Most of these human factors studies, furthermore, have been done on people who are experts in their fields. Error-making is not a novice-level phenomenon. Our study found that inexperienced and experienced spreadsheet developers made about the same number of errors per spreadsheet model. In addition, Galletta et al. 21 found that when experienced spreadsheet<sup>w</sup> <sup>x</sup> developers audited models, they did not find a higher percentage of the errors in these models than did inexperienced spreadsheet developers. This lack of large differences between relative novices and experts has also been seen in other studies, for instance in Grudin’s 23 study of typing. This is not to say <sup>w</sup> <sup>x</sup> that novice–expert differences do not exist. It is only to say that they are not an order of magnitude in size. Looking at the error rates in Table 1, we would need error rates lower by one or two orders of magnitude to make spreadsheet modeling is a safe activity.

Professional programmers have long known that they have error rates comparable to those in Table 1 when they have ‘finished’ a program or module <sup>w</sup> <sup>x</sup> <sup>7,8,9</sup> 5,7,17,30,49,52 . As a result, professional programmers use development disciplines that call for spending about a third of their time testing the program. One of the techniques they use to check for errors is code inspection 17 , in which a team of <sup>w</sup> <sup>x</sup> programmers systematically checks the code for errors. First, members of the team check the code individually. Then, in a meeting, they read through the program line by line. During this process, members report the errors they discovered before the meeting. In addition, the team discovers additional program faults during the meeting.

Unfortunately, independent audits are rare in spreadsheet modeling 24 , and even data testing<sup>w</sup> <sup>x</sup> with extreme values is also uncommon 24 . In addi-<sup>w</sup> <sup>x</sup> tion, data on spreadsheet and programming codeŽ . inspection errors for individuals indicates that only team inspections are likely to succeed at reducing programming and spreadsheet development errors to an acceptable level.

In general, it seems that we will need the kinds of deep testing seen in professional programming for important spreadsheets. This will involve sophisticated data testing and team code inspections. In fact, we will have to rethink the entire development process. Professional programmers have to conduct team design inspections before they ever begin to code. In contrast, Cragg and King 12 found that the 31<sup>w</sup> <sup>x</sup> spreadsheet developers that they interviewed rarely did much planning before they start filling in cells on a spreadsheet. Both Brown and Gould 8 and Panko<sup>w</sup> <sup>x</sup> and Halverson 43 noted a lack of planning in their<sup>w</sup> <sup>x</sup> experiments.

Perhaps spreadsheet developers have felt that their models are small compared to the programs of professional programmers, but as noted earlier we know that many spreadsheets are quite large and complex. We also know that spreadsheet developers often have considerable difficulty when they try to understand even their own spreadsheets and often have problems finding appropriate ways of handling computational tasks 27 . Quite simply, spreadsheet development looks quite a bit like programming.

Fortunately, if our goal is to teach developers how to create spreadsheets professionally, we may be able to draw on what we already know about program development. Not everything in programming development will carry over to spreadsheet development, of course. Still, in many ways, teaching spreadsheet developers how to develop their spreadsheets more safely is likely to be largely a matter of ‘teaching new dogs old tricks’.

For further information on spreadsheet errors, consult the Spreadsheet Research Website at http:<sup>rr</sup>www.cba.hawaii.edu<sup>r</sup>panko<sup>r</sup>ssr<sup>r</sup>. For more information on human error in general, consult the Human Error Website at http:<sup>rr</sup>www.cba.hawaii. edu<sup>r</sup>panko<sup>r</sup>humanerr<sup>r</sup>.

## References

<sup>w</sup> <sup>x</sup> 1 A.J. Albrecht, J. Gaffney Jr., Software function, software lines of code, and development effort prediction: a software science, IEEE Trans. Software Eng. 9 11 1983 639–648.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 C.M. Allwood, Error detection processes in statistical problem solving, Cogn. Sci. 8 4 1984 413–437.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 B.J. Baars Ed. , Experimental Slips and Human Error, Ž . Plenum, New York, 1992.

<sup>w</sup> <sup>x</sup> 4 V.R. Basili, R.W. Selby, Jr., Four applications of a software data collection and analysis methodology, in: J.K. Skwirzynski Ed. , Software System Design Methods, Springer-Verlag, Ž . Berlin, 1986, pp. 3–33.

<sup>w</sup> <sup>x</sup> 5 B. Beizer, Software Testing Techniques, 2nd edn., Van Nostrand-Reinhold, New York, 1990.

6 Y.M.M. Bishop, S.E. Fienberg, P.W. Holland, Discrete Multivariate Analysis: Theory and Practice, MIT Press, Cambridge, MA, 1975.

<sup>w</sup> <sup>x</sup> 7 B.W. Boehm, Improving software productivity, Computer 20 Ž . Ž . 9 1987 43–57.

<sup>w</sup> <sup>x</sup> 8 P.S. Brown, J.D. Gould, An experimental study of people creating spreadsheets, ACM Trans. Office Information Systems 5 3 1987 258–272.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 E.G. Cale Jr., Quality issues for end-user developed software, J. Systems Manage. 45 1 1994 36–39.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 S.K. Card, T.P. Moran, A. Newell, The Psychology of Human–Computer Interaction, Erlbaum, Hillsdale, NJ, 1983.

<sup>w</sup> <sup>x</sup> 11 H.C. Chan, H.J. Lu, K.K. Wei, A survey of SQL language, J. Database Manage. 4 4 1993 4–15. Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 P.G. Cragg, M. King, Spreadsheet modelling abuse: an opportunity for OR?, J. Operational Res. Soc. 44 8 1993Ž . Ž . 743–752.

<sup>w</sup> <sup>x</sup> 13 R. Creeth, Microcomputer spreadsheets: their uses and abuses, J. Accountancy 159 6 1985 90–93.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 A.D. Danu Tjahjono, Exploring The Effectiveness Of Formal Technical Review Factors With CSRS, A Collaborative Software Review System, Technical Report ICS-TR-95-08, Information and Computer Science Department, Univ. of Hawaii, Honolulu, HI, 96822, June, 1996.

<sup>w</sup> <sup>x</sup> 15 N. Davies, C. Ikin, Auditing spreadsheets, Australian Accountant, December 1987 pp. 54–56.Ž .

16 S. Ditlea, Spreadsheets can be hazardous to your health, Personal Computing, January 1987 pp. 60–69.Ž .

<sup>w</sup> <sup>x</sup> 17 M.E. Fagan, Design and code inspections to reduce errors in program development, IBM Systems J. 15 3 1976 182–Ž . Ž . 211.

<sup>w</sup> <sup>x</sup> 18 B.D. Floyd, J. Pyun, Errors in Spreadsheet Use, working paper 167, Center for Research on Information Systems, Information Systems Department, New York Univ., New York, 1987.

<sup>w</sup> <sup>x</sup> 19 E.H. Forman, N.D. Singpurwalla, An empirical stopping rule for debugging and testing computer software, J. Am. Stat. Assoc., Application Section 72 360 1977 750–757.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 D. Freeman, How to make spreadsheets error-proof, J. Accountancy 181 5 1996 75–77. Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 D.F. Galletta, D. Abraham, M. ElLouadi, W. Lekse, Y.A. Pollalis, J.L. Sampler, An empirical study of spreadshee error-finding performance, Accounting Manage. Information Technol. 3 2 1993 79–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 D.F. Galletta, K.S. Hartzel, S.E. Johnson, J.L. Joseph, S. Rustagi, Spreadsheet presentation and error detection, J. Manage. Information Systems 13 3 Winter 1996 45–63.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J.T. Grudin, Error patterns in novice and skilled transcription typing, Chap. 6, in: W.E. Cooper Ed. , Cognitive Aspects of Ž .

Skilled Typewriting, Springer-Verlag, New York, 1983, pp. 121–143.

<sup>w</sup> <sup>x</sup> 24 M.J.J. Hall, A risk and control oriented study of the practices of spreadsheet application developers, in: Proceedings of the 29th Hawaii International Conference on System Sciences, Vol. II, January 1996, pp. 364–373.

<sup>w</sup> <sup>x</sup> 25 K. Hassinen, An Experimental Study of Spreadsheet Errors Made by Novice Spreadsheet Users, Department of Computer Science, Univ. of Joensuu, P.O. Box 111, SF-80101 Joensuu, Finland, 1988.

<sup>w</sup> <sup>x</sup> 26 J.R. Hayes, L.S. Flower, Identifying the organization of writing processes, in: L. Gregg, E. Steinberg Eds. , Cogni-Ž . tive Processes in Writing, Erlbaum, Hillsdale, NJ, 1980, pp. 3–30.

<sup>w</sup> <sup>x</sup> 27 D.G. Hendry, T.R.G. Green, Creating, comprehending, and explaining spreadsheets: a cognitive interpretation of what discretionary users think of the spreadsheet model, Int. J. Human–Comput. Studies 40 6 1994 1033–1065.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 M. Igbaria, F.N. Pavri, S.L. Huff, Microcomputer applications: an empirical look at usage, Information Manage. 16 4Ž . Ž .1989 187–196.

<sup>w</sup> <sup>x</sup> 29 D. Janvrin, J. Morrison, Factors influencing risks and outcomes in end-user development, in: Proceedings of the 29th International Conference on System Sciences, Vol. II, Maui, Hawaii, January 1996, pp. 346–355.

<sup>w</sup> <sup>x</sup> 30 C. Jones, Programming Productivity, McGraw-Hill, New York, 1986.

<sup>w</sup> <sup>x</sup> 31 B. Kantowitz, R.D. Rorkin, Human Factors: Understanding People–System Relationships, Wiley, New York, 1983.

<sup>w</sup> <sup>x</sup> 32 R. Kee, Programming standards for spreadsheet software, CMA Mag. 62 3 1988 55–60.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 K. Kukich, Techniques for automatically correcting words in text, ACM Computing Surveys 24 4 1992 377–436.Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 F.J. Lerch, Computerized financial planning: discovering cognitive difficulties in knowledge building. Unpublished doctoral dissertation, Univ. of Michigan, Ann Arbor Sci. Publ., Ann Arbor, MI, 1988.

<sup>w</sup> <sup>x</sup> 35 I. Lorge, H. Solomon, Two models of group behavior in the solution of eureka-type problems, Psychometrika 20 2Ž . Ž .1955 139–148.

<sup>w</sup> <sup>x</sup> 36 M. Mattson, B.J. Baars, Error-minimizing mechanisms: boosting or editing, in: B.J. Baars Ed. , Experimental SlipsŽ . and Human Error, New York, Plenum, 1992, pp. 263–287.

<sup>w</sup> <sup>x</sup> 37 E.R. McLean, L.A. Kappelman, J.P. Thompson, Converging end-user and corporate computing, Commun. ACM 36 12Ž . Ž .1993 79–92.

<sup>w</sup> <sup>x</sup> 38 R.E. Melchers, M.V. Harrington, Human Error in Simple Design Tasks, Report No. 31, Civil Engineering Research Reports, Monash Univ., 1982.

<sup>w</sup> <sup>x</sup> 39 G.A. Miller, The magic number seven plus or minus two, Psychol. Rev. 63 1956 81–97.Ž .

<sup>w</sup> <sup>x</sup> 40 Morrison, 1995.

<sup>w</sup> <sup>x</sup> 41 G.J. Myers, A controlled experiment in program testing and code walkthroughs<sup>r</sup>inspections, Commun. ACM 21 9Ž . Ž . 1978 760–768.

<sup>w</sup> <sup>x</sup> 42 R.R. Panko, End User Computing: Management, Applications, and Technology, Wiley, New York, 1988.

<sup>w</sup> <sup>x</sup> 43 R.R. Panko, R.H. Halverson, Jr., Are two heads better than one? at reducing errors in spreadsheet development , Office Ž . Systems Res. J., forthcoming.

<sup>w</sup> <sup>x</sup> 44 R.R. Panko, R.H. Halverson, Jr., Introduction to the minitrack on risks in end user computing, in: Proceedings of the 29th Hawaii International Conference on System Sciences, Vol. II, Maui, Hawaii, January 1996a pp. 324–325.Ž .

<sup>w</sup> <sup>x</sup> 45 R.R. Panko, R.H. Halverson, Jr., Spreadsheets on trial: a survey of research on spreadsheet risks, in: Proceedings of the 29th Hawaii International Conference on System Sciences, Vol. II, Maui, Hawaii, January 1996b pp. 324–325.Ž .

<sup>w</sup> <sup>x</sup> 46 L.H. Putnam, W. Myers, Measures for Excellence: Reliable Software on Time, on Budget, Yourdon, Englewood Cliffs, NJ, 1992.

<sup>w</sup> <sup>x</sup> 47 J. Reason, Human Error, Cambridge Univ. Press, Cambridge, UK, 1990.

<sup>w</sup> <sup>x</sup> 48 B. Ronen, M.A. Palley, H. Lucas, Spreadsheet analysis and design, Commun. ACM 32 1 1989 84–92.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 B. Spencer, Software inspections at applicon, in: T. Gilb, D. Graham Eds. , Software Inspection, Addison-Wesley, Work-Ž . ingham, England, 1993, pp. 264–279.

<sup>w</sup> <sup>x</sup> 50 R.H. Sprague, Jr., E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982. <sup>w</sup> <sup>x</sup> 51 Strauss, Ebenau, 1983.

<sup>w</sup> <sup>x</sup> 52 S.H. Strauss, R.G. Ebenau, Software Inspection Process, McGraw-Hill, New York, 1994.

<sup>w</sup> <sup>x</sup> 53 T.S.H. Teo, M. Tan, Quantitative and qualitative errors in spreadsheet development, in: Proceedings of the Thirtieth Hawaii International Conference on System Sciences, Vol. III, Kihei, Hawaii, January 1997, pp. 149–155.

![](/api/attachments/DCUHZKHH/fulltext/images/9f02613569a8f569775a33e92ba9e49df169dca6326b138c1a0911ab91a5b502.jpg)

Dr. Raymond R. Panko is a professor of decision sciences in the College of Business Administration at the University of Hawaii. He received his Ph.D. from Stanford University. He has been involved with end-user computing since the 1960s and began his current program of research on spreadsheet research in 1993. He is also involved in groupwork research; in fact, his initial work on spreadsheet development was an exploration of groupwork in an end

user computing context. His e-mail address is panko@hawaii.edu. His home page is http:<sup>rr</sup>www.cba.hawaii.edu<sup>r</sup>panko. He maintains a website on spreadsheet research. That URL is http:<sup>rr</sup>www.cba.hawaii.edu<sup>r</sup>panko<sup>r</sup>ssr<sup>r</sup>.

![](/api/attachments/DCUHZKHH/fulltext/images/8945c153aefaecc8852259c548cbcf8c241b237a22c30aeddb0e644d3be8f466.jpg)

Dr. Ralph H. Sprague, Jr. is also a professor of decision sciences in the College of Business Administration at the University of Hawaii. He received his Ph.D. from Indiana University. Dr. Sprague is one of the most widely-cited authors in Decision Support Systems. His e-mail address is sprague@hawaii. edu. His home page is http:<sup>rr</sup>www. cba.hawaii.edu<sup>r</sup>sprague.
