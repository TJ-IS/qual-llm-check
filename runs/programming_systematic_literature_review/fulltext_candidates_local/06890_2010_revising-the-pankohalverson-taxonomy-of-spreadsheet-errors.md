---
otero_id: 6890
otero_key: "965EBVK8"
title: "Revising the Panko–Halverson taxonomy of spreadsheet errors"
authors: "Raymond R. Panko; Salvatore Aurigemma"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Revising the Panko–Halverson taxonomy of spreadsheet errors

Raymond R. Panko ⁎, Salvatore Aurigemma

University of Hawaii, United States

## a r t i c l e i n f o

Article history: Received 1 December 2008 Received in revised form 15 February 2010 Accepted 22 February 2010 Available online 1 March 2010

Keywords: Spreadsheet Spreadsheet error End user development End user computing Execution error Taxonomy Error Violation Context error Omission Logic error Planning error Mistake Slip Lapse

## a b s t r a c t

Error taxonomies are useful because different types of errors have different commission and detection rates and because error mitigation techniques often are only useful for some types of errors. In the early 1990s, Panko and Halverson developed a spreadsheet error taxonomy. This paper updates that taxonomy to re<sup>fl</sup>ect human error research more fully. The taxonomy focuses on quantitative errors during development and testing but notes that qualitative errors are very important and that errors occur in all stages of the system development life cycle.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Spreadsheets are widely used in corporations, and there is strong convergent data showing that most corporate spreadsheets have material errors [15]. Consequently, a great deal of all spreadsheet research has focused on the study of errors. While one “solution” may be to stop using spreadsheets, human error research suggests that error rates probably are similar for other decision support system development technologies [14].

Nearly all spreadsheet error researchers have used taxonomies to categorize errors. They have done this because there are multiple error mechanisms with different commission rates, different detection rates, and differently susceptibilities to error avoidance and detection methods. Error mitigation strategies need to be developed and assessed with respect to speci<sup>fi</sup>c types of errors.

The purpose of this paper is to revisit and revise the widely cited Panko and Halverson [18] taxonomy of spreadsheet errors. There are several reasons for doing so. First, the taxonomy was based on aspects of general human error research known to Panko and Halverson in 1993. Second, subsequent taxonomies have identi<sup>fi</sup>ed important error types that were not included in the Panko and Halverson taxonomy. Third, the omission category in the taxonomy has proven to be too narrow, and the mechanical–logical–omission trichotomy in general needs to be replaced by the more widely used mistake–slip–lapse trichotomy.

This paper covers some of the same topics addressed by Powel, Baker, and Lawson [22], who included discussions of error classi<sup>fi</sup>cation, impact, frequency, creation and prevention, and detection. Most obviously, our paper differs by focusing primarily on the <sup>fi</sup>rst topic, error classi<sup>fi</sup>cation. We will note other differences later in this paper.

## 2. Taxonomies

## 2.1. Taxonomies

Taxonomies have long been used in science. Senders and Moray [30], writing about human error, said that:

... a taxonomy is a fundamental requirement for the foundation of empirical science. If we want a deep understanding of the nature, origins, and causes of human error, it is necessary to have an unambiguous classi<sup>fi</sup>cation scheme for describing the phenomenon we are studying. [p. 82.]

There is no “best” error taxonomy for spreadsheets [9,24] or any other type of human cognitive activity. Researchers and professionals with different focuses need different things from error taxonomies. For instance, spreadsheet designers need error taxonomies that distinguish between types of errors that need different amelioration strategies. The legal system, in contrast, needs distinctions that help assign responsibility for damages [30]. In addition, each taxonomy illuminates some aspects of a phenomenon while blinding the researcher or practitioner to other aspects of the phenomenon [1].

## 2.2. Phenomenological versus deep (theory-based) taxonomies

Senders and Moray [30] distinguished between different levels of taxonomies. The most super<sup>fi</sup>cial level consists of phenomenological taxonomies that are based on simple descriptions of error manifestations. For instance, typing errors at this level would be described by such things as keystroke transpositions. At the level of phenomenological errors, there is no explanation for why different errors occur.

Phenomenological taxonomies are useful for destroying myths about what types of error occur frequently. If a certain type of error proves to be particularly frequent, it merits particular attention. Conversely, if a type of error once believed to be important actually is fairly rare, then shifting resources from this type of errors to other types of errors may be important. Research using phenomenological taxonomies, then, can puncture false belief bubbles.

In addition, in spreadsheet experiments on the detection of errors, experimenters typically seed spreadsheets with errors that the researchers believe to be common errors [7,8,11,16]. Ideally, the selection of seeded errors should re<sup>fl</sup>ect the true relative frequencies of different kinds of errors. Otherwise, the results of these experiments measured as the percentage of errors detected will be misleading.

In contrast to phenomenological taxonomies, deeper taxonomies are informed by theory. This is especially valuable if a theory predicts manifestations of results. In error research, for instance, the theory may suggest that different types of errors will have different error occurrence rates, different detection rates, or different mechanisms for mitigation. Unfortunately, there is no complete theory for human error, so creating full deep taxonomies for spreadsheet errors is not possible today.

## 2.3. Error attribution

Nearly all spreadsheet error research is based on the analysis of spreadsheets that have already been developed. This suggests that we should only have phenomenological taxonomies. However, most published taxonomies of spreadsheet error still try to explain observed errors in terms of underlying theories. While this may be methodologically undesirable, it is also undesirable to use taxonomies that describe errors but give no clues as to why different types of errors occur or how they can be redressed.

In defense of attributing error causes, it may be plausible to infer the cause of many errors in operational spreadsheets. For instance, if a subject switches Year 1 and Year 2 sales values after reading them off a sheet of paper, this seems likely to be due to a lapse inside the subject's memory.

As we move from tightly controlled experiments to the inspection of operational spreadsheets, we are likely to need more purely phenomenological taxonomies. However, even this is only a conjecture. For instance, if an operational spreadsheet computes revenues on Row 47 and in the next row multiplies revenues by the corporate tax rate to compute corporate taxes, it is fairly clear that the spreadsheet developer mistakenly believed that corporate taxes are computed on the basis of revenues instead of income.

## 3. Human error taxonomies

## 3.1. Human error research

Our concern is not taxonomies in general but human error taxonomies. In this, we are fortunate because human error has been studied in many human cognitive domains for more than 100 years. These domains have included mathematics, programming, throwing switches, aircraft accidents, automobile accidents, nuclear incidents, proofreading, and linguistics, to name just a few. In the 1980s, researchers from different human cognition domains began to realize that they were seeing the same types of errors and error frequencies in different cognitive domains. Reason [28] summarized many of these convergent <sup>fi</sup>ndings. Panko [14] summarizes measured human error rates in studies in different <sup>fi</sup>elds.

Perhaps the most important <sup>fi</sup>nding from the converged error literature is that human cognitive processes produce the correct result nearly all the time but have a small inherent error rate that stems from the same processes that produce correct results [28]. In other words, the way we actually think (as opposed to the way we believe that we think) is the heart of the problem, not simple sloppiness.

Unfortunately, the fact that we make relatively few mistakes as we do cognitive work is not good enough in some contexts. For instance, software programmers usually are 95% to 98% accurate when they write code [14]. However, in programs that have long <sup>fl</sup>ows of logic, even this high level of accuracy is not enough. The same is true in spreadsheets.

A third important <sup>fi</sup>nding is that while we are good at avoiding errors as we work and catching many of our errors immediately, we are not as good at detecting errors after the fact [14]. When we examine a cognitive artifact such as a program, we typically <sup>fi</sup>nd only 60% to 70% of the errors, and this varies widely by error type [14].

In this paper, we attempt to exploit the work on error taxonomies in human error research. This makes this paper different from the critical review of Powell, Baker, and Lawson [22], which was not based on the human error literature.

## 3.2. What is an error?

The most fundamental issue in any error taxonomy is how to de<sup>fi</sup>ne “error.” Senders and Moray [30] de<sup>fi</sup>ned an error as:

“an action that is not intended by the actor;not desired by a set of rules or an external observer; orthat led the task or system outside its accepted limits”

Senders and Moray [30], p. 25.

The key point is that there needs to be a criterion for determining whether something is correct or an error. In many cases, the criterion will be obvious, such as a mistyped number. In other cases, especially in matters of good practices, there may not be a universally accepted criterion.

## 3.3. Mistakes, slips, and lapses

In his book, Human Error, Reason [28] presented a taxonomy of human errors based on prior work by Reason and Mycielska [29] and Norman [13]. This taxonomy, shown in Fig. 1, begins with a basic distinction between planning and execution errors. If the plan is wrong, this is a mistake, regardless of how good the implementation is. However, if the plan is correct but the execution is wrong, this is a slip or lapse.

The distinction between slips and lapses was proposed by Norman [13].A slip is an error during a sensory-motor action, such as typing the wrong number (say \$120,000 instead of \$210,000) or pointing to the wrong cell when entering a formula. In contrast, a lapse occurs within

<table><tr><td>Stage of Error</td><td colspan="2">Type of Error</td></tr><tr><td>Error in Planning</td><td>Mistake</td><td>Logic or mathematical error, etc.</td></tr><tr><td rowspan="2">Error in Execution</td><td>Slip</td><td>Sensory-motor error</td></tr><tr><td>Lapse</td><td>Error cause by memory overload</td></tr></table>

Sources: Norman [13]; Reason [29].

Fig. 1. Mistakes versus slips and lapses.

the person's head. A lapse is a failure in memory. A lapse often is caused by overloading the limited human memory capacity.

This taxonomy has possible implications for automated spreadsheet error detection programs, which only work on <sup>fi</sup>nal spreadsheet artifacts. It is likely that errors involving planning and memory that occur “off the spreadsheet” will leave few if any artifacts in the spreadsheet for automated analysis tools to <sup>fi</sup>nd. Even slips during the execution may not leave artifacts for automated spreadsheet analysis programs to <sup>fi</sup>nd.

For human error hunters, too, the three types of errors suggest that constraining inspection to the spreadsheet itself is likely to miss many errors. It is mandatory to inspect requirements, designs, and domain algorithms to understand if they have been executed properly in the spreadsheet.

## 3.4. Rasmussen

Rasmussen [27] further divided mistakes into rule-based mistakes, which occur when the developer or tester applies a heuristic rule incorrectly, and knowledge-based mistakes, which occur when no rule applies and the person must use his or her general knowledge of the device or electrical engineering in general. Although the Rasmussen [27] taxonomy is important, applying it runs into two serious issues. First, developers and testers must be highly experienced, or they will not have well-developed heuristic rules or adequate knowledge. More seriously, this taxonomy cannot be used without doing a protocol analysis. We will not include this distinction in our taxonomy because most research does not use protocol analysis.

## 3.5. Allwood

A study by Allwood [2] examined the commission rates and detection rates for different types of errors. Allwood [2] conducted a protocol analysis study using students solving mathematical problems. Allwood's students made 327 errors as they worked. Six out of every ten errors were execution errors, which involved something like doing an addition incorrectly. However, the subjects spontaneously caught 83% of execution errors as they worked. Consequently, execution errors accounted for only 29% of the <sup>fi</sup>nal errors.

Logic errors that involved mathematical thinking, namely solution method errors and higher-level math errors, only accounted for a quarter of all errors made, but their relatively low error detection rates (48% and 25% respectively), resulted in their accounting for 40% of all <sup>fi</sup>nal errors.

Skip errors involved subjects skipping a step in a solution process. These errors were comparatively rare, accounting for only 9% of all errors. However, none were detected spontaneously, so they resulted in 29% of all <sup>fi</sup>nal errors.

Panko and Halverson [18] based their taxonomy of spreadsheet development errors heavily on Allwood's taxonomy and research <sup>fi</sup>ndings.

## 3.6. Flower and Hayes

Another intriguing error insight comes from Flower and Hayes [6], who used protocol analysis to study the writing process. They found that their subjects needed to work at several levels of abstraction simultaneously. Subjects had to select speci<sup>fi</sup>c words while generating sentences; and sentence production had to <sup>fi</sup>t into the author's plan for the paragraph, for larger units of the document, for the document as a whole, and for the document's purpose (requirements). Planning had to be done at all levels of abstraction simultaneously. Each level of abstraction, furthermore, created constraints that had to be obeyed when considering other levels.

Fig. 2 shows that we portray the Flower and Hayes taxonomy of concerns as a context pyramid that is inverted, placing all of the weight of all context levels on the writing of each word. This can create an enormous load on the writer's memory and planning resources. Indeed, interruption studies have shown that writing is one of the most cognitively-intensive human activity domains [6].

In spreadsheet development, the same heavy mental load is likely to occur. Whenever a developer enters a formula, he or she has to be cognizant of the algorithm for the formula, the algorithm for a larger section of the spreadsheet, the spreadsheet design as a whole, and the spreadsheet's external requirements. An error may occur because of a <sup>fl</sup>aw at any of these levels.

## 3.7. Violations

Earlier, we noted that even when we are attempting to work diligently, errors are inevitable because of the very ways in which human cognition works [28]. In software, testing, Beizer [4] has argued that programmers must be held blameless for errors found in testing because of the inevitability of errors even when people are diligent.

However, the argument that errors are innocent does not apply if the person is intentionally circumventing policies and rules. This idea was <sup>fi</sup>rst articulated in human research on automobile accidents, in which speeding, drinking, and other violations of the law are viewed as non-inevitable and blameful [28]. Consequently, it makes sense to make a distinction between innocent errors due to human cognitive processes and errors due to violations.

In driving, there are speci<sup>fi</sup>c laws that prescribe most types of dangerous driving behavior. Consequently, identifying certain driving actions as violations often is straightforward. However, even if talking on a hands-free mobile phone is legal, it signi<sup>fi</sup>cantly reduces a person's driving ability, and accidents we have when talking on hands-free mobile phone, while not illegal, may still be negligence. The usefulness of a distinction between innocent errors and violations seems to be most useful where there is strong agreement on what is acceptable and unacceptable.

## 4. Spreadsheet error taxonomies

So far, we have looked at general human error taxonomies. We will now look speci<sup>fi</sup>cally at spreadsheet error taxonomies.

![](/api/attachments/965EBVK8/fulltext/images/adb0186d2b1cf525b26b888a1df4b4e31e8d43e81391bf2c4c99d105cb2e66ae.jpg)  
Fig. 2. The context pyramid in writing.

## 4.1. Human error taxonomies and experiments

Many spreadsheet taxonomies have been based on data from experiments. Powell, Baker, and Lawson [22], citing Reason [20], note that experiments are dangerous because they are often contrived. Certainly, this is true in some experiments. However, spreadsheet experiments usually require a developer to create a spreadsheet from a word problem or to attempt to detect errors in a spreadsheet. These activities do not seem to be overly contrived.

More importantly, experiments are useful in isolating the speci<sup>fi</sup>c aspects of human cognition and error making. In general, spreadsheets have focused on determining whether research results from software development will carry over to spreadsheet development. In general, they do [16,18].

In addition, experiments are useful not only in measuring raw error rates but in noting how commission and detection rates differ for different types of errors. For instance, Panko [16] found that omission errors are detected much less frequently than other types of errors—a <sup>fi</sup>nding seen in research in other human cognitive domains [28].

Even for inspections for operational spreadsheets, results from human error research are of practical importance. If detection rates really are different for different types of errors, then the pro<sup>fi</sup>le of detected errors will not match the pro<sup>fi</sup>le of real errors in spreadsheets. Also, if research shows that the detection of errors in longer formulas is less than it is in shorter formulas [16], this means that error detection protocols should specify minimum times to be spent on more complex formulas. In software code inspection, furthermore, it has been found that detection yield is strongly tied to the maximum number items to be covered in an inspection, and the minimum time to be taken in inspection [5,14].

## 4.2. Galletta

Galletta et al. [8] conducted an experiment using MBA students and accountants working on their CPA accreditation. In this study, subjects inspected spreadsheets looking for errors. Galletta, et al. [8] divided errors into two types. Domain errors occurred when a formula required knowledge of accounting. Device errors involved using the computer and the spreadsheet program—typing errors and pointing errors. The study found that device errors had a higher detection rate than domain errors.

## 4.3. Panko and Halverson

For their 1993 experiment on errors in spreadsheet development and inspection, Panko and Halverson [18] created a taxonomy of spreadsheet research issues as a three dimensional cube. Fig. 3 shows that the three sides of this cube were research issue, life cycle stage, and methodology (experiment, survey, etc.) for addressing the research issues.

Research issues included structural concerns (poor structure), actual errors, user work practices, assumptions, and spreadsheet model's characteristics (size, percentage of cells that are formulas or data, complexity of formulas, one-time use versus many-time use, the number of people who use the spreadsheet, risks, and control policies). In other words, the taxonomy went well beyond quantitative and qualitative error categories and well beyond error studies in general.

Under “actual errors,” which meant quantitative errors, the taxonomy noted several ways to count errors and noted that each has advantages and disadvantages. The error-counting metrics listed were the percentage of models containing errors, the number of errors per model, the distribution of errors by magnitude or severity, and the cell error rate.

For error magnitude and severity, Panko and Halverson [18] noted that, “Some errors are important, other unimportant. One measure is the size of the error as a percentage of the correct bottom-line value. Another is whether a decision would have been different had the error not been made. We suspect that quite a few errors are either too small to be important or still give answers that lead to the correct decisions.”

![](/api/attachments/965EBVK8/fulltext/images/c188c6724fcfcc68801955646cd1bb7b0c4fad85416e17d2471d53a0e2d73589.jpg)  
Fig. 3. Panko and Halverson spreadsheet risks research cube

Powell, Baker, and Lawson [24] discussed error magnitude in some detail and did so even more in an earlier [21] paper. They focused on the dollar magnitudes and percentage magnitudes of errors. Other studies have looked at the seriousness of the errors in the context in which the spreadsheet was used [15].

In terms of the cell error rate, which is the percentage of cells that contain an error, Panko and Halverson [18] were taking a cue from software development research, which has long measured the faults per thousand lines of noncomment source code (faults/KLOC). The rate of faults/KLOC is roughly the same across programs. This allows software developers to get a rough estimate of the number of errors they can expect to <sup>fi</sup>nd when inspecting a module of code with known length. In manufacturing, reliability engineers also measure average error rates for different types of activities, in order to design and manage processes.

Consequently, Panko and Halverson [18] suggest measuring error frequency in terms of the cell error rate (CER)—the percentage of cells containing errors. For the computation of CERs, Panko and Halverson [18] argued that spreadsheet research should divide the total number of errors in value (formula and constant) cells by the total number of value cells. We will see that this CER measure has proven to be inadequate.

Like faults/KLOC, the CER is a rough way to anticipate the number of errors in a spreadsheet, just as faults/KLOC is in software. Not every spreadsheet will have the same cell error rate, much less every module in a spreadsheet. In addition, for both faults/KLOC and CER calculations, omissions and some other errors do not occur in a particular cell and therefore do not affect the number of cells, except, in the case of omissions, to reduce them. Like other types of base error rates [14], the cell error rate is a useful indicator of anticipated error rates, not a precision tool for estimating human error rates. However, it is a powerful way to show that spreadsheet cell error rates are far too high for safety, given the long chains of formulas leading to results in spreadsheets.

Panko and Halverson [19,20] also argued that errors should be counted only once, in the cells in which they occur. For example, if this error is repeated in copied cells, it should only be counted as a single error. (The original formula that is copied is called the root formula.) Also, only cells in which the error was actually made should be counted, not dependent cells that are incorrect only because of errors in precursor cells. Most subsequent studies have used this “original sin” approach. Of course, in computing cell error rates, the same numerator and denominator must be used. For example, if only the root formula in a row of copied cells is used as the numerator for a copying error, the same must be true in the denominator.

Fig. 4 shows the Panko and Halverson [18] taxonomy of development and testing error types. The taxonomy <sup>fi</sup>rst divides errors into qualitative and quantitative errors. This demarcation of the two types of errors was very simple. If something makes a computed (“bottom-line”) value incorrect, then it is a quantitative error. If it did not, it is a qualitative error.

The most common qualitative error is putting a constant instead of a cell reference into a formula [Panko, 1988]. For instance, if the tax equals the income before tax times the tax rate of 15%, the formula for tax should not give the cell reference to income before tax and then multiply this by 15%. If the tax rate changes, <sup>fi</sup>nding all instances of where changes should be made is dif<sup>fi</sup>cult. Consequently, some instances of the tax rate would be changed, but others might not be changed because they are not found. This practice of inserting a number in an equation is often called hardcoding.

Panko [1988] suggested that hardcoding, while not creating immediate errors, would result in later errors. Teo and Tan [31] tested this conjecture. They found that students who did hardcoding did, in fact, made more errors during subsequent what-if analyses. Reason [28] calls errors that do not produce an immediate numerical error but that are likely to produce subsequent numerical errors later latent errors. For example, suppose the developer does not turn on cell protection (a qualitative error). Later, a user may mistakenly type a number in a formula cell. Now, the spreadsheet's computations are incorrect (a quantitative error).

The distinction between quantitative and qualitative errors is not the same as the distinction between serious and nonserious errors. Many quantitative errors are small, while qualitative errors can lead to extremely serious errors later. In addition, many qualitative errors such as poor design reduce productivity and cause other problems even if they do not result in numerical errors. Ignoring qualitative errors is not an option for corporations. Having said this, researchers have tended to focus on quantitative errors because much spreadsheet error research has been done at least in part to document that there is a spreadsheet accuracy problem, and quantitative errors are more convincing than qualitative errors.

Following Allwood [2] broadly, Panko and Halverson [18] divided quantitative errors into three basic types: mechanical, logic, and omission errors.

➢ Mechanical errors are typing errors, pointing errors, and other simple slips and lapses. Mechanical errors can be frequent, but they have a high chance of being caught by the person making the error.

➢ Logic errors are incorrect formulas due to choosing the wrong algorithm or creating the wrong formula to implement the algorithm.

➢ Omissions are requirements left out of the model. They often result from a misinterpretation of the situation. Human factors research has shown that omission errors are especially dangerous because they have low detection error rates [14,28].

Panko and Halverson's <sup>fi</sup>rst study using the taxonomy was a development experiment in which subjects created a spreadsheet working alone, in groups of two, or in groups of four [19]. The authors conducted an inter-rater reliability test on the taxonomy's tripartite distinction between quantitative mechanical, logical, and omission errors. The subjects made the same 209 quantitative errors according to both researchers, for a 100% reliability rate in overall error counting. Within these quantitative errors, the researchers initially disagreed on the classi<sup>fi</sup>cation of a single error that occurred in three spreadsheets. This represented 99.6% reliability. The point of disagreement was a single error made by three different subjects who added expenses to revenues to get income, instead of subtracting expenses from revenues. One researcher classi<sup>fi</sup>ed this as a logic error (believing that they should be added), the other as a mechanical error (typing a + instead of a −).

Panko [16] later conducted an inspection study, using a modi<sup>fi</sup>- cation of the Galletta et al. [8] inspection task and a variant of the Fagan [5] code inspection methodology. This time, Panko tested the distinction between omission errors and other types of errors (mechanical and logical). Consistent with other research on human error, omission errors were detected much less frequently than other types of errors. The study also found that errors in long formulas were detected less frequently than errors in shorter formulas.

The third dimension in the Panko–Halverson spreadsheet research issues cube was life cycle stage. Based on the prior spreadsheet literature, Panko and Halverson [18] divided the spreadsheet life cycle (not just the spreadsheet development life cycle) into 5 stages: requirements and design, cell entry, the draft stage (after careful development but before testing), debugging (testing), and operation (use after development). Panko and Halverson [18] suggested that the error rate varies strongly across this life cycle, as Fig. 5 indicates. Through the draft stage, errors typically increase with time. During testing and when operational use of the spreadsheets has begun, errors tend to decrease (although errors sometimes increase during operational use, especially if cell protection is not turned on).

Although the Panko and Halverson [18] taxonomy has been fairly well validated by experiments, some limitations have become obvious over time. First, although the taxonomy has both an error type dimension and a spreadsheet life cycle perspective, Panko and Halverson did not <sup>fl</sup>esh out the lifecycle dimension. They did not look at the types of errors that occur during the initial analysis and requirements. More concretely, because they did not study ongoing use they were not aware until later of overwriting errors, in which a user overwrites a formula in an operational spreadsheet with a number.

![](/api/attachments/965EBVK8/fulltext/images/68272a070dba07abe6545bf8b02a180bc73582ea63af7e2987e02a742e5ed8a4.jpg)  
Fig. 4. Panko and Halverson 1996 taxonomy of development and testing error types.

![](/api/attachments/965EBVK8/fulltext/images/38600b75a7c9f3e57d01aaf12cbad57f9af2fea13e2dd4dfb45e6698f569de99.jpg)  
Fig. 5. Cell error rate (CER) by life cycle stage.

Second, they focused on omission errors because these were the subject of earlier human error research. However, an omission of a requirement is only one type of requirement noncompliance [12].

Third, the taxonomy did not recognize the important distinction between sensory-motor slips and memory lapses. This is important because it is likely that automated error detection tools seem more likely to catch slips than lapses that occur inside a person's head.

## 4.4. Rajalingham

Rajalingham led the creation of a taxonomy in 2000 [25] and expanded on this taxonomy in 2005 [26]. The initial taxonomy [25], like the Panko and Halverson [18] taxonomy, makes the distinction between qualitative and quantitative errors. It then makes a distinction between accidental and reasoning quantitative errors. This is similar to the Panko and Halverson [18] mechanical versus logical distinction, but its terminology (accidental versus reasoning) is better connotatively.

Another important addition in this taxonomy is the distinction between developer and end user accidental errors. Panko and Halverson [18] only focused on developer errors. They did not consider the types of errors that end users would make after development. Most obviously, they failed to consider data entry errors, which can be very important. These errors can include inputting incorrect data or even overwriting a formula with a number.

Rajalingham, et al. [25] also considers errors that users make in interpreting the results of spreadsheets, even if the spreadsheet is numerically correct. This was a major insight.

## 4.5. Howe and Simkin

For a code inspection experiment, Howe and Simkin [11] created a new taxonomy for spreadsheet errors.

➢ Data entry errors. Out of range values, negative values, a value entered as a label.

➢ Clerical and non-material errors. Incorrect dates in labels, misleading labels, and so forth. (Previous studies have ignored such errors.)

➢ Rules violations. Cell entries which violate a stated company policy. These violations do not have to be deliberate.

➢ Formula errors. Inaccurate range references, embedded constants (hardcoding), and illogical formulas.

Violations are parts of the model that violate requirements. Omission errors do this, but so do many other types of errors, such as computing overtime pay for a salaried employee who is not eligible to receive overtime pay. This is different from the concept of violations in driving, described earlier, which involve deliberate misconduct.

One concern with the taxonomy is that it mixes quantitative and qualitative errors. Misleading labels might be classi<sup>fi</sup>ed as either, while hardcoding is normally seen as a qualitative error because it does not make a computed value incorrect immediately.

## 4.6. Powell, Lawson, and Baker

For their series of projects involving the creation, testing, and use of an inspection (auditing) methodology for operational spreadsheets, Powell, Lawson, and Baker [23,24] developed another taxonomy of errors.

➢ Logic errors: formula is used incorrectly, leading to an incorrect result.

➢ Reference errors: a formula contains one or more incorrect references to other cells.

➢ Hardcoding: one or more numbers appear in formulas, and the practice is suf<sup>fi</sup>ciently dangerous.

➢ Copy/paste: a formula is wrong due to an incorrect cut and paste.

➢ Data input: an incorrect data input is used.

➢ Omission: a formula is wrong because one of its input cells is blank.

While laboratory experiments may have enough context to use theory-informed taxonomies, Powell, Lawson, and Baker [23,24] decided that they used a phenomenological taxonomy based on the forms of the errors they encountered. As noted earlier, moving to more purely phenomenological taxonomies may be desirable as we move from laboratory experiments to operational spreadsheets.

This taxonomy's use of omission errors is very different from the use of omission errors in the Panko and Halverson [18] taxonomy. In the Panko and Halverson usage, something in the requirements is left out of the spreadsheet. This is not likely to be detectable by looking at the spreadsheet. In contrast, in the Powell, Lawson, and Baker [23,24] taxonomy, an omission error means pointing to a blank cell. This type of omission error proved to be rare in the Powell, Lawson, and Baker study [24]. In this taxonomy, there is nothing like the omission errors posited by Panko and Halverson [18].

Hardcoding is described as a qualitative error in the Panko and Halverson [18] and the Rajalingham [2005] taxonomy. Howe and Simkin [11] always classify it as a formula error, which can either be quantitative or qualitative. In the Powell, Lawson, and Baker [21] taxonomy, hardcoding is usually not counted as an error but is, “unless it is suf<sup>fi</sup>ciently dangerous.” The taxonomy, then, does not follow the usual quantitative-versus-qualitative distinction. Instead, it counts some qualitative errors if they are serious but counts all quantitative errors, even if they are not serious.

## 5. A revised Panko and Halverson taxonomy

Based on the previous discussion, we now present our revised taxonomy of spreadsheet errors.

## 5.1. Measuring errors

As discussed earlier, it is important to have a common agreement about how to count the number of errors. Also as discussed earlier, counting the number of errors is not trivial. Most studies use the “original sin” rule—only counting an error in the cell in which it occurs. Although this rule generally is relatively easy to apply, some measurement goals need to take different approaches. For instance, if the goal is to quantify the impact of an error, then the focus falls explicitly on values in subsequent cells [21]. If a root cell is copied, furthermore, the fact that copied formulas create inaccuracies in multiple bottom-line variables cannot be ignored [21] in studies of impacts.

Another issue occurs when counting errors in a workbook with multiple worksheets. If the same error occurs in multiple worksheets, there is some merit to counting it as a single error, but if the goal is to assess what percentage of all worksheets are incorrect, then it would be better to count the error once in each worksheet [24].

The concept of cell error rates (CERs), as noted earlier, is derived from the programming concept of faults per thousand lines of (noncomment) source code (faults/KLOC). It is important, in counting cell error rates, to specify the denominator precisely. In software development, comment statements typically are excluded from the denominator. In spreadsheets, this would correspond to excluding label cells.

<table><tr><td>Acronym</td><td>Denominator</td><td>Use</td></tr><tr><td>CERV</td><td>Value cells (numbers and formulas)</td><td>Cell error rates have traditionally been measured this way</td></tr><tr><td>CERF</td><td>Formula cells</td><td>Focuses on formula error rates, which usually are much higher than value error rates</td></tr><tr><td>CERN</td><td>Number cells</td><td>Good for looking at input errors</td></tr><tr><td>CERT</td><td>Text cells</td><td>Good for looking at documentation</td></tr><tr><td>CERA</td><td>All nonempty cells (label and value cells)</td><td>Not very useful, but some studies use it</td></tr></table>

Fig. 6. Types of cell error rates (CERs).

As noted earlier, Panko and Halverson [18] used the number of value cells–constants and formulas–as the denominator in their studies. Some subsequent studies, however, used all non-empty cells (including text cells) in their denominator, while other cell error rates have been based only on formula cells. Differences in denominators for calculating the CER can make research results dif<sup>fi</sup>cult to compare across studies.

Fig. 6 identi<sup>fi</sup>es some possible ways of de<sup>fi</sup>ning cell error rates and gives suggested names to be used in future research.

➢ CERV is based on value cells. This includes numerical and formula cells.

➢ CERF is based on formula cells. If most errors occur in formula cells, then CERF will be larger than CERV for the same number of errors.

➢ CERN is based on numerical cells. It is useful for discussing data input errors.

➢ CERA is based on all non-empty cells, including formula cells, numerical cells, and label cells.

Researchers should specify which form of cell error rate they are reporting. They should also report the number of numerical, formula, and text cells separately to allow others to rebase their error rates for the comparison with results from other studies. For formulas, the number of unique formulas should be reported as well, for both in the numerator and denominator.

## 5.2. Violations and innocent errors

Fig. 7 shows our revised taxonomy of spreadsheet errors. Following Reason [28], the taxonomy <sup>fi</sup>rst divides all errors into violations and innocent errors. Most errors are innocent errors, but some problems are due to deliberate violations of corporate standards or guidelines for spreadsheet development. Worse yet, some incorrect spreadsheets are incorrect because of more serious violations, such as outright fraud or puffery (using exaggerated or “cooked” numbers to encourage people to make poor decisions). While employees should not be punished for innocent errors, violations deserve sanctions.

What about unknowing departures from policies and speci<sup>fi</sup>ed good practices? Are they also violations? We believe that they are not. Unless a departure is intentional or is characterized by considerable negligence, it is not a violation. This follows the mens rea requirement for criminal prosecutions under the law.

## 5.3. Qualitative versus quantitative errors

For innocent errors, this taxonomy continues to use the distinction between qualitative and quantitative errors. Quantitative errors, quite simply, are incorrect formulas or data cells that make the model incorrect. Qualitative errors, in turn, may lead to quantitative problems later but do not make the model incorrect immediately.

In the original Panko and Halverson [18] taxonomy, quantitative errors produced immediate incorrect results. However, a model can become incorrect without immediately giving the wrong number. For instance, if a user overwrites a formula with a number, bottom-line calculations may be correct for this usage although the model is no longer generally correct. To give another example, if an incorrect cell reference points to a cell that happens to have the same value as a correct cell, then this pointing error, while clearly an error, will not result in an incorrect value [21].

Even with special cases, it appears that quantitative errors can be counted fairly unambiguously. Qualitative errors, in contrast, typically are violations of good spreadsheet development practice. However, there is no strong consensus for what constitutes good spreadsheet practices.

## 5.4. Planning errors (mistakes) versus execution errors (slips and lapses)

The taxonomy divides quantitative errors into planning errors versus execution errors. This distinction focuses on the instant when the user begins to enter the formula. An error before that instant is a planning error. An error made after that instant is an execution error.

![](/api/attachments/965EBVK8/fulltext/images/e9e11d9d5ee95d35a9436e5626c6b909c7953507407f46e088874c641d9ebb4c.jpg)  
Fig. 7. Revised taxonomy of errors.

In terms of the Norman and Reason distinctions described earlier, a planning error is a mistake, while an execution error is a slip or a lapse.

## 5.5. Domain and spreadsheet expression planning errors

The taxonomy divides planning errors into domain planning errors and spreadsheet expression planning errors. This distinction argues that planning has two aspects. First, planning for a formula or section needs to have a domain component. If the spreadsheet deals with aircraft wing design, aerodynamics is likely to be important in creating an algorithm.

In addition, the developer must have a plan for expressing the domain plan on a spreadsheet. Spreadsheet expression may include the use of functions. It also may mean expressing domain concepts that do not naturally <sup>fi</sup>t the row/column design of spreadsheets into a spreadsheet section with multiple formulas.

This distinction is important because automated spreadsheet error detection programs seem more likely to <sup>fi</sup>nd spreadsheet expression planning problems than domain planning problems. Domain planning problems may not be detectible without domain knowledge.

## 5.6. Slip and lapse execution errors

Execution errors <sup>fi</sup>t the distinction between slips and lapses discussed earlier. This distinction may also have implications for automated error detection. Slips may lead to errors in pointing to the wrong cell and other errors that leave detectable patterns on a spreadsheet. Lapses, which occur within the brain, may be less likely to leave such detectible patterns.

## 5.7. Life cycle stages and roles

Fig. 7 shows development and testing errors. However, as the Panko and Halverson taxonomy [18] noted, we also note that spreadsheets generally go through a system life cycle that begins with the analysis of the current situation and needs and ends when the spreadsheet is terminated or replaced.

The <sup>fi</sup>rst part of this life cycle is the system development life cycle. However, most of a spreadsheet's life is spent in operational use, so we need to focus on the entire system life cycle—not only on the systems development life cycle.

Different types of errors will occur at different stages of the systems life cycle. For requirements and design, the software engineering literature may provide good guidance on what to look for—including the fact that a large fraction of all errors occur during requirements and design instead of during programming and testing [12]. In addition, spreadsheet development often uses a process more akin to agile development than traditional development, so spreadsheet professionals should look for error research in the context of nontraditional development.

Arguably the most important stage is operational use. Many speci<sup>fi</sup>c errors, such as entering the wrong number for a variable or incorrectly importing data, occur primarily during operational use. Violations also must be anticipated, such as violations of privacy or the use of spreadsheets to commit fraud. Other operational use problems include lack of maintenance of documentation, of version control, and transitions when the developer or maintainer changes jobs.

Another aspect of life cycle thinking is that there are several possible organization roles involved. During development, for instance, there may be separate developers, testers, managers, and organizational clients. During operational use, there may be separate owners, operators who enter data and do other hands-on tasks, customers of the information, and other roles. We need to think about violations and innocent errors that may be made by each potential role during each stage of the life cycle to understand error mitigation needs.

Of course some of these roles may be combined—most obviously if the developer is also the tester, client and user of the spreadsheet. However, even when roles are combined, it may still make sense to think in terms of logical roles to consider possible errors. In addition, while combining roles may decrease some errors, such as communication errors, it may make others more likely, such as the tendency to become <sup>fi</sup>xated in ways that make a person less able to see the errors that they made.

## 6. Inter-rater reliability analysis

Taxonomies, like any other research methodology, should be judged on a number of criteria. Every taxonomy should face the entire battery of tests required to assess its internal and external validity, but a particular concern is reliability. Reliability means that if different people use the taxonomy to classify the same events or items, they will classify individual items in the same way. A taxonomy that cannot be applied reliably by different people is a failed taxonomy. To assess the reliability of our taxonomy, the two authors conducted an interrater reliability study in which they independently classi<sup>fi</sup>ed errors in a corpus of spreadsheets.

Reliability never is 100%. In general, an inter-rater reliability of 90% or higher is the goal, although an inter-rater reliability of 60% to 70% may make a study publishable as an exploratory study. In <sup>fi</sup>eld studies, which deal with messier situations, somewhat lower inter-rater reliability values will be acceptable. Even then, however, methodology designers must use coarser taxonomies whose broader categories can be assigned robustly, so that inter-rater reliability will stay high.

The corpus of spreadsheets was created for a previous study [17]. In that study, students developed spreadsheet models from the Kooker word problem. This task had students develop a two-year pro forma (projected) income statement. The full corpus has 74 spreadsheets. For this study, we used the <sup>fi</sup>rst 50 spreadsheets in this corpus but threw out six that could not be analyzed with a trial version of Spreadsheet Professional™. This limitation was irrelevant to this study, but we wished to maintain commonality for other studies using the corpus. Of these 44 remaining spreadsheets, 40 contained errors. The total number of errors was 98

As a pre-test, the two authors independently classi<sup>fi</sup>ed errors in the <sup>fi</sup>rst 5 spreadsheets of the corpus. When they compared the results, they realized that they were not focusing precisely on whether the error happened during formula planning or execution. After clarifying that target, the two authors categorized errors in the remaining 39 spreadsheets, which contained a total of 86 errors.

Errors in the corpus had been identi<sup>fi</sup>ed previously. The Kooker task has an unambiguous solution. A rater (different from the ones in this study) found spreadsheets with incorrect answers, identi<sup>fi</sup>ed the error, and <sup>fi</sup>xed the error. If the spreadsheet was still incorrect, he repeated this process until the spreadsheet was correct. He recorded the errors.

In the reliability protocol, the <sup>fi</sup>rst thing to do was to classify the error as a planning error (mistake before entering the formula) or an execution error in entering the formula. The two authors did this before they sub-classi<sup>fi</sup>ed planning and execution errors into subtypes. They then went back to each error. They classi<sup>fi</sup>ed each planning error as a domain planning error or as a spreadsheet expression planning error. They classi<sup>fi</sup>ed each execution error as a lapse or as a slip.

For the 39 spreadsheets used in this phase, the authors agreed on the two-phase classi<sup>fi</sup>cation of 85 out of the 88 errors, for an inter-rater reliability value of 96.6%. This is acceptable reliability. Although classi<sup>fi</sup>cation may seem to be dif<sup>fi</sup>cult in the abstract, the two authors noted that it was fairly easy to classify most errors when they were seen in context. Overall, the taxonomy appears to be reliable when raters used the protocol to classify errors. However, like any taxonomy it is not perfect. Applying this taxonomy and protocol to other corpuses may disclose other weaknesses. In particular, we suspect that errors in long complex formulas would be very dif<sup>fi</sup>cult to classify.

## 7. Error frequency

## 7.1. Error frequency

A major bene<sup>fi</sup>t of taxonomies is the ability of taxonomy users to examine the relative frequencies of different types of errors. As noted earlier, different types of errors may call for different avoidance and detection strategies. If a rare error type is extremely expensive to address, addressing it may not be worth the effort. In contrast, if an error type thought to be rare proves to be frequent, more attention may be needed to its strategies for its amelioration.

## 7.2. Spreadsheet error detection programs

A potentially important tool for detecting errors is the automated spreadsheet error detection program, which is typi<sup>fi</sup>ed by Spreadsheet Professional and Excel Error Check. These tools work by highlighting anomalous patterns in the spreadsheet, such as a cell with no precedents or a change in the copying pattern of a formula as it is copied across columns or rows. It is reasonable to assume that these tools will work best for identifying slip errors. Planning errors and lapses within the developer's head may leave no pattern for the software to identify.

## 7.3. Errors in our corpus

Although the purpose of the reliability analysis was to assess the reliability of the taxonomy and protocol, it is interesting to note the distribution of errors found in the study. Fig. 8 summarizes the 85 jointly classi<sup>fi</sup>ed errors. The <sup>fi</sup>gure shows that 82% of the errors were mistakes (planning errors), and all but one of these mistakes was a domain planning error. Only 18% of the errors were execution errors, and more of these were lapses than slips.

This pattern of errors suggests that Spreadsheet Professional and Microsoft Error Check are not likely to be effective on this corpus of spreadsheets. Actually, only some spreadsheets in the corpus were included in the reliability study because these spreadsheets had previously been used in a study of the ability of Spreadsheet Professional and Excel Error Check to <sup>fl</sup>ag known errors in the spreadsheets [3]. In that study, <sup>fi</sup>ve students applied Spreadsheet Professional and Excel Error Check to the spreadsheets in the corpus. There were 88 errors in the corpus. For each tool, then, there were 440 errors to assess as being <sup>fl</sup>agged or not <sup>fl</sup>agged. One student judged that Excel Error Check correctly <sup>fl</sup>agged a single error, for a success rate of 0.22%. One student judged that Spreadsheet Professional correctly tagged 4 errors, for a success rate of almost 1%.

<table><tr><td></td><td>Number</td><td>Percent</td></tr><tr><td>Total Errors</td><td>88</td><td></td></tr><tr><td>Total Errors Jointly Classified*</td><td>85</td><td>100%</td></tr><tr><td>Planning Errors (Mistakes)</td><td>70</td><td>82%</td></tr><tr><td>Domain</td><td>69</td><td>81%</td></tr><tr><td>Spreadsheet Expression</td><td>1</td><td>1%</td></tr><tr><td>Execution Errors</td><td>15</td><td>18%</td></tr><tr><td>Slip</td><td>6</td><td>7%</td></tr><tr><td>Lapse</td><td>9</td><td>11%</td></tr></table>

Fig. 8. Jointly classi<sup>fi</sup>ed errors in reliability study.

It may be that this corpus was misleading because the student subjects made a very large number of domain errors due to ignorance. However, another development study on almost the same task found that undergraduate students without spreadsheet work experience and MBA students with substantial spreadsheet development and testing experience made very similar types of errors. In addition, in his three-person code inspection of an operational spreadsheet, Hicks [10] found that most errors were logic errors.

Another concern is that the students did not do a map analysis in which they visually could see patterns in the spreadsheet. However, the <sup>fi</sup>rst author of this paper did a Spreadsheet Professional map analysis. It did not help in <sup>fi</sup>nding any of the known errors in the spreadsheet.

## 7.4. Errors in the Powell, Baker, and Lawson audit of 50 spreadsheets

In their auditing study of 50 operational spreadsheets, Powell, Baker, and Lawson [23] found a very different pattern of errors. In that study, testers collected and recorded information about the spreadsheet. They then did a map analysis with Spreadsheet Professional, ran Spreadsheet Professional tests to <sup>fl</sup>ag errors, ran XL Analyst against the spreadsheet, and did a code inspection on the remaining formulas. Ignoring hardcoding errors, which we classify as a qualitative error, 63% of the errors were reference errors, copy/paste errors, and omission errors (referencing an empty cell). These correspond to slips in our classi<sup>fi</sup>cation. Only 35% of the errors discovered were logic errors, most of which would seem to be what we call planning errors (mistakes). Finally, data errors accounted for 2% of the errors.

In addition, Powell, Baker, and Lawson [23] found most of their errors using error detection programs. Map analysis, Spreadsheet Professional tests, and XL Analyst found 81% of the errors. Code inspection only found 18.2% of the errors discovered in the study.

One possible explanation is that the operational spreadsheets that Powell, Baker, and Lawson [23] studied really did have very different error patterns than our student-generated spreadsheets. Another explanation is that Powell, Baker, and Lawson's [23] code inspection was ineffective so that few errors were found beyond those found by using the automated tools

One speci<sup>fi</sup>c concern is the speed of inspection. Fagan [5] found that rapid code inspection <sup>fi</sup>nds fewer errors than slower code inspection. In some studies, the fall-off in detection effectiveness is very large [14]. The median amount of time spent in the Powell, Baker, and Lawson [23] study on the entire audit was 195 min. The median number of formulas was 1294. Even if all the auditing time was used for code inspection, this would allow only 9 s per formula. Of course, most code inspections (but certainly not all) would focus on root formulas. There was a median of only 105 or 193 unique (root) formulas, giving more time per formula. Even so, given the complexity of the protocol, code inspection probably took a relatively small percentage of the total time.

Another speci<sup>fi</sup>c concern is that each of the Powell, Baker, and Lawson [23] inspections used only a single inspector. In software development, code inspection is done in teams [5,14]. In spreadsheet code inspection experiments, subjects working alone only caught about half of all errors [15]. When a one-person inspection is added to the inspection rate problem, it seems plausible that the code inspection part of the study was inef<sup>fi</sup>cient. While software auditing tools might do well in <sup>fi</sup>nding slip errors, inadequate code inspection would tend to undercount logic (planning errors).

A third speci<sup>fi</sup>c concern is that in the Powell, Baker, and Lawson [23] audit, the inspectors did not know the requirements for the spreadsheet they were inspecting. This would make it more dif<sup>fi</sup>cult to identify mistakes. In their later study of 25 spreadsheets, Powell, Baker, and Lawson [21] did have the requirements, but the detailed data from the study examined in this section is not available for the newer study.

For these three reasons, we believe that the Powell, Baker, and Lawson [23] study probably undercounted planning errors.

## 8. Perspective

## 8.1. Changes in the taxonomy

This paper has revised and expanded the Panko and Halverson [18] taxonomy of spreadsheet errors. The purpose of the early taxonomy was to support quantitative research studies to demonstrate that quantitative spreadsheet errors are frequent, that quantitative spreadsheet errors are dif<sup>fi</sup>cult to detect, and that many spreadsheet errors are signi<sup>fi</sup>cant. Fig. 7 shows the revised taxonomy. This taxonomy makes a number of new distinctions.

➢ First, there is a distinction between blameless (innocent) errors and culpable violations of laws or required corporate practices.

➢ Second, the distinction between logic, mechanical, and omission errors has been replaced by the more common distinction between domain and spreadsheet expression planning errors (mistakes) on the one hand and implementation errors (slips and lapses) on the other hand [13,28]. Planning errors are incorrect intentions. Implementation errors are the incorrect implementation of plans.

➢ Among planning errors, domain planning errors occur when the developer makes a mistake in the knowledge domain of the model (<sup>fi</sup>nance, ecology, physics, etc.). Spreadsheet expression planning errors occur when the developer plans an incorrect spreadsheet expression of the domain algorithm.

➢ Logic errors become mistakes, while mechanical errors are divided into slips and lapses. Slips are sensory-motor errors, such as typing and pointing errors. In contrast, lapses are memory errors [13].

## 8.2. Relative error frequency

We need research to assess the relative frequency of various types of errors. In our corpus, for which we had unambiguous quantitative error data, that most errors were planning errors, and most of these were domain planning errors. Among the execution errors, more than half were lapses occurring in the developer's head. Powell, Baker, and Lawson [23] found very different things in their examination of 50 operational spreadsheets, although we have concerns about the ability of their methodology to detect planning errors and perhaps lapses.

## 8.3. Time to change our research focus

Today, the idea that signi<sup>fi</sup>cant quantitative errors are frequent has been broadly accepted. In any case, people who still reject that experimental and <sup>fi</sup>eld evidence regarding them are not likely to have their opinions changed by further quantitative research. It is now time to shift our focus toward qualitative errors, which may be far more common than quantitative errors, and identifying the large number of different types of errors that are possible in different life cycle stages and by people with different roles to play.

## References

[1] G.T. Allison, P. Zelikow, Essence of Decision: Explaining the Cuban Missile Crisis, Longman Publishers, Englewood Cliffs, NJ, 1999 2nd Edition.

[2] C.M. Allwood, Error detection processes in statistical problem solving, Cognitive Science 8 (4) (1984).

[3] S. Aurigemma and R.R. Panko, (2009). “Experiment on the Accuracy of Static Testing (Auditing) Programs in Detecting Spreadsheet Errors,” presentation at the workshop “Spreadsheets: The Dark Matter of IT” at The Forty-Second Hawaii International Conference on System Sciences Waikoloa Hawaji January 5 2009

[4] B. Beizer, Software Testing Techniques, Van Nostrand, New York, 1990 2nd ed.

[5] M.E. Fagan, Design and code inspections to reduce errors in program development IBM Systems Journal 15 (3) (1976)

[6] L.A. Flower, J.R. Hayes, The dynamics of composing: making plans and juggling constraints, in: L.W. Gregg, E.R. Steinberg (Eds.), Cognitive Processes in Writing, Lawrence Erlbaum Associates, Hillsdale, NJ, 1980, pp. 31–50.

[7] D.F. Galletta, K.S. Hartzel, S. Johnson, J.L. Joseph, Spreadsheet presentation and error detection: an experimental study, Journal of Management Information Systems 13 (2) (1997) Winter.

[8] D.F. Galletta, D. Abraham, M. El Louadi, W. Lekse, Y.A. Pollailis, J.L. Sampler, An empirical study of spreadsheet error-<sup>fi</sup>nding performance, Journal of Accounting Management, and Information Technology 3 (2) (1993) April-June.

[9] T.A. Grossman, O. Özlük, Research strategy and scoping survey on research practices, Proceedings of EuSpRIG 2003, European Spreadsheet Risks Interest Group, 2003, July 24-25, Trinity College, Dublin, Ireland

[10] L. Hicks, NYNEX, personal communication with the <sup>fi</sup>rst author via electronic mail, June 21, 1995.

[11] H. Howe, M. Simkin, F. Mark, Factors affecting the ability to detect spreadsheet errors, Decision Sciences Journal of Innovative Education 4 (1) (2006) Not 2008

[12] T.C. Jones, Programming Productivity, McGraw-Hill, New York, 1986.

[13] D.A. Norman, Categorization of action slips, Psychological Review 88 (1981).

[14] R.R. Panko, Human Error Website. (http://panko.shilder.hawaii.edu/panko/ HumanErr/). Honolulu, HI: University of Hawaii (2009a)

[15] R.R. Panko, Spreadsheet Research (SSR) Website. (http://panko.shilder.hawaii.edu/ panko/ssr/). Honolulu, HI: University of Hawaii (2009b).

[16] R.R. Panko, Applying code inspection to spreadsheet testing, Journal of Management Information Systems 16 (2) (1999) Fall.

[17] R.R. Panko, Two experiments inreducing overcon<sup>fi</sup>dence in spreadsheet development, Journal of Organizational and End User Computing 19 (1) (2007) January-March.

[18] R.R. Panko Jr., R.P. Halverson, An experiment in collaborative spreadsheet development, Journal of the Association for Information Systems 2 (4) (2001) July.

[19] R.R. Panko, R.P. Halverson Jr., Are two heads better than one? (at reducing errors in spreadsheet modeling), Of<sup>fi</sup>ce Systems Research Journal 15 (1) (1997) Spring.

[20] R.R. Panko, R.P. Halverson Jr, Spreadsheets on trial: a framework for research on spreadsheet risks, Proceedings of the Twenty-Ninth Hawaii International Conference on System Sciences, 1996, pp. 326–335, Volume II.

[21] S.G. Powell, K.R. Baker, B. Lawson, Impact of errors on operational spreadsheets Proceedings of the European Spreadsheet Risks Interest Group, EuSpRIG 2007 Conference, 2007, pp. 57–68, July

[22] S.G. Powell, K.R. Baker, B. Lawson, A critical review of the literature on spreadsheet errors, Decision Support Systems 46 (2008).

[23] S.G. Powell, K.R. Baker, B. Lawson, An auditing protocol for spreadsheet models Information & Management 45 (2008).

[24] S.G. Powell, K.R. Baker, B. Lawson, Errors in operational spreadsheets, Journal of Organizational and End User Computing 21 (3) (2009) July-September.

[25] Rajalingham, Kamalasen; Chadwick, David R.; & Knight, Brian. (2000, July 17-18). “Classi<sup>fi</sup>cation of Spreadsheet Errors,” Symposium Proceedings EuSpRIG 2000, University of Greenwich, London, UK, European Spreadsheet Risks Interest Group, pp. 23-34.

[26] K. Rajalingham, (2005, July). “A Revised Classi<sup>fi</sup>cation of Spreadsheet Errors,” Proceedings of the 2005 European Spreadsheet Risks Interest Group, EuSpRIG 2005, Greenwich, London, 185-199.

[27] J. Rasmussen, Skills, rules, knowledge: signals, signs and symbols and other distractions in human performance models, IEEE Transactions: Systems, Man, and Cybernetics, SMC-13 (1983).

[28] J.T. Reason, Human Error, Cambridge University Press, Cambridge, England, 1990

[29] J.T. Reason, K. Mycielska, Absent-Minded? The Psychology of Mental Lapses and Everyday Errors, Prentice Hall. Englewood Cliffs, N.I. 1982

[30] J.W. Senders, N.P. Moray, Human Error: Cause, Prediction, and Reduction Lawrence Erlbaum. Hillsdale. NH. 1991.

[31] T.S.H. Teo, M. Tan, Spreadsheet development and “what-if” analysis: quantitative versus qualitative errors, Accounting, Management and Information Technologies 9 (1999).

## FURTHER READING

[32] R.R. Panko, R.H. Sprague Jr., Hitting the wall: errors in developing and code inspecting a “simple” spreadsheet model, Decision Support Systems 22 (4) (1998) April.

Professor Raymond Panko began his IT career as an end user FORTRAN programmer at the Boeing Company. This led him to an MBA at Seattle University, a PhD at Stanford, and a stint at Stanford Research Institute, where he worked under Doug Engelbart. His initial research focused on end user communication tools. In the 1980s, he turned primarily to studies of end user development. In 1988, Wiley published his End User Computing: Management, Applications, and Technology, which focused heavily on end user development. In the early 1990s, he began conducting research on spreadsheet development, especially errors in spreadsheet development and use. He has maintained this focus since then, due to a lack of imagination. He attempts to ground his spreadsheet research in general human error research. He maintains a website on spreadsheet research (http:// panko.shidler.hawaii.edu/ssr) and another on human error research (http://panko.shilder. hawaii.edu/humanerr).

Salvatore Aurigemma is a PhD student at the University of Hawaii, in the Communication and Information Sciences Program. He has a master's degree in information systems. His primary research interest is security. He is a commander in the U.S. Navy Reserves.
