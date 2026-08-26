---
otero_id: 23408
otero_key: "7C9U3P55"
title: "Soft information systems"
authors: "Ivan F Jackson; David Hosking"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.32"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Soft information systems

IVAN F. JACKSON and DAVID HOSKING

Information Systems Group, Victoria University of Wellington.

Abstract: This paper describes a category of information systems called 'Soft information systems'. Basically these lie between conventional information systems in which data are well defined, and management support, and decision support systems. A soft system is a system which operates on soft data. Such data cover categories of information such as conjectures, predictions, feelings and opinions and are typically found in systems where there is some element of anticipation of the future. Such systems include career counselling systems, where clients have rather 'fuzzy' views of what they might wish to do, through to economic based systems used to predict levels of employment, inflation levels and interest rates etc. In between are management-type systems in which it is normally assumed that hard (i.e. factual) data are used, for instance in budgeting systems. The paper describes some previous work and the experimental systems which tested and explored the ideas involved as well as attempting to refine some of the techniques that can be used to deal with soft data.

## Introduction

It is probably true to say that over the years the main focus for information systems as a discipline has been the design and development of operations-oriented systems. Some of these are backbone systems constructed so as to support the transaction processing capabilities of the organization. Others are the support systems, ranging in scope from a mainstream system, such as a human resource management system (as distinct from a high-volume payroll), through to model-based management and decision support systems.

Accompanying this focus, especially in recent years, has been the rather tentative emergence of the expert system, the commercial outgrowth of research into artificial intelligence. Expert systems fall into a number of broad categories:

(1) Systems which are a component of a Decision Support System (DSS). In these systems the model behind the DSS is not passive but rather the expert system interactively engages the user in the information extraction process.

(2) CASE tools, used in the systems development process, where the expert system basically provides a sophisticated help facility for eliciting and organizing information on data relationships.

(3) Front desk systems, in which the skills level of the person dealing with the customer/client is supplemented by the knowledge base. A variation of this type is the so-called advice giving expert system (Carroll and McKendree, 1987).

(4) Training systems where the system tracks the trainee's learning pattern and presents material appropriate to it.

Particularly in these last two categories, the system may have to cope with persons giving vague and imprecise answers to questions asked. This may be because the user doesn't really have an understanding of what the system wants, or because a question may be open to a number of interpretations. This problem is not unique to expert systems. It is hoped that this paper will provide an insight into how issues of this nature may be addressed.

## Soft systems, soft data and fuzzy logic

It seems to the authors that another category of system exists, one which lies somewhere between the conventional support type system and an expert system. This is the soft information system, or merely the soft system. Such a system is defined to be 'an information system which operates on soft data'. Soft data, in turn, are defined to be 'all information that are not explicitly known to be true'. Thus the definition covers such categories of information as conjectures, predictions, feelings or opinions. As will be seen it can also include such imprecise data as value judgements.

A characteristic of such data is that it is:

(1) Often rather difficult to elicit values, or similar categories of information, from individuals.

(2) Quite a design challenge to express such information so that it is meaningful to the user.

Examples given in this paper address these issues.

A good example of the use of soft data is in what could be broadly classified as business economic forecasting, although it must be emphasised that the application is not seen as an economic one exclusively.

A forecast of the level of unemployment in each month of the coming year could be used for estimating fiscal requirements for the provision of social services. Both the forecast, and even the budget itself, can be considered to be made up of elements of soft data. The soft data may be contrasted to hard data which are the details about events that have actually occurred. Using the unemployment example, hard data would be the measured unemployment figures after they had actually happened.

The reader may compare the definition of soft data with one generally accepted for that of a fuzzy variable. One given by Holsapple and Whinston (1987) is “a variable that has more than one value at a time”. Each value in turn has an associated certainty factor. Further, ‘if a (hard) variable has one value, then it becomes fuzzy by adding an additional value’. Soft data thus overlaps the definition of a fuzzy variable. Thus the further out one projects the unemployment figures, the fuzzier the picture becomes. Also, depending on who one listens to, at any one time there could be several views as to what the figures would be.

The interesting thing about soft data is that they can become hard over time. Time will certainly tell how the unemployment estimates will really turn out. Just as for reporters, certain sources will invariably be found to be better than others. Normal practice will be to view these sources as being more reliable, although the others cannot completely be discounted.

Fuzzy logic is beginning to enter the information systems mainstream. A number of fuzzy processors have been built in the USA and Japan. Johnson (1989) lists potential fuzzy applications. These range from data retrieval methods, because fuzzy logic can make fast and accurate guesses as to where to find data, to stock market searching where traditional search and sort criteria use crisp criteria that will throw out a company's stock that does not precisely match them.

Johnston feels that ‘fuzzy logic may be able to solve problems that involve controlling or modelling the real world that have proved difficult to solve with traditional logic or even with artificial intelligence (AI) based rules’. He quotes Zadeh, inventor of fuzzy logic: ‘most natural concepts in the world are not crisp, they are fuzzy... The reason AI has so many unfulfilled promises is that it uses conventional logic; it is an albatross around AI’s neck’.

## Using decision theory — ‘adaptive’ systems

## London School of Economics work — career choices

An early example of the development of what could be described as a soft system was attempted by the Decision Analysis Unit of the London School of Economics (LSE). The Unit was addressing the difficulties in advising people (particularly students) on career choices (Wooler, 1985). The researchers had problems with the North American (software) systems, commonly used in schools, which made occupational suggestions based on asking a student a number of questions designed to narrow down the field of choice. The assumption behind those systems was seen to be a set of values associated with work which people entering the workforce commonly attempt to realize.

The problem with this is that the suggestions are based on typical responses. If a large number of responses were often found to be idiosyncratic then it is likely that many career suggestions made would be inappropriate. Further, the user construes his or her career problem to be fundamentally different from that assumed by the system. The problem was identified as 'the meaningfulness problem'. The issue was 'why should clients take any notice of the occupational or job recommendations made by a system if the work goals and values which it ascribes to them are not their own...?'

What is needed then is a system which would adapt itself to the changed environment. Putting it another way, the system should take account of changing circumstances and ‘get smarter’ as it goes along. Hence the term adaptive system.

The LSE team designed a system call SELSTRA (Woller and Wisudha, 1985). SELSTRA stands for Self Elaborating Structuring and Assessment. It was recognized that value elicitation is frequently a complex task for elicitor and respondent alike. While it may be desirable to have a completely unstructured approach to defining the problem space, in practice this is not feasible. What was done was to provide the client (i.e., the student) with the top level of what is essentially a value tree, as illustrated in the capitalized components of Figure 1.

In operation, the client is then encouraged to think about his/her situation in terms of these basic values. He/she is asked subjectively to add new value items at a lower level. In effect, a user hierarchy is established of attributes which the client thinks are important to his/her particular situation. The client thus fills out what is described as the subjective problem space. Example client entries are shown in lower case in Figure 1.

The client is then asked to weight the different values. More specifically he/she is asked to assess the relative importance of each factor in each value set. In SELSTRA these are scaled from 1 to 100 but the scale is subsequently reduced to 0 to 1 (see Figure 1), and thus values bear an uncanny resemblance to the values within a fuzzy set. The values actually reflect a preference ordering within the value space. The system subsequently uses decision theory to suggest career options. These are, however, at a very broad level such as marketing, or publishing. While the main purpose of the system is to assist career counsellors to focus rapidly on issues of concern to the client, the counsellor could check the choices for realism and completeness, and clarify misconceptions about possible career choices. (LSE also uses a system called MAUD to similarly test out choice options).

![](/api/attachments/7C9U3P55/fulltext/images/223a5a86099099fe25d791e420794318f90c7e9f3318741ef66827da360f2584.jpg)  
Figure 1. An example of a hierarchy of values entered by a client, (modified from work by Wooler et al. — see References.

## An Otago University study - career advice

Following on from the LSE work a prototype system was initiated by first author (at his earlier place of employment) to see if an expert systems approach could be used for careers advising. The system was based on a USA model developed by Holland (1977) and adapted by the New Zealand Council for Educational Research. With the Self-Directed Search (SDS), a student self-administers and self-scores a test designed to describe people and work environments. In point of fact the tool has been subject to rather strong criticisms as to bias (e.g. towards males), but that was not really the issue in the study.

In the test the student would come up with a 3-character code which is supposed to point him/her towards suitable jobs (as specified in the New Zealand Occupations Finder). In the manual system (which was filled in by the students as the first part of the study), the student merely responded with a yes/no answer. However, everything is not black and white in the real world so it was decided to introduce a degree of shading into recording the answers. Thus, when a question appeared on the screen, the user interacted with the system by moving the cursor along a bar which became denser the higher the value to be scored (on a range of 0 to 5). The shading was introduced to represent a measure of fuzziness in the answers. The system has a number of features in common with an expert system:

(1) It had a knowledge base. In fact, this was a series of linked databases with occupations, linked to jobs, linked to educational level needed, linked to sources of information. It also had a level of expertness in how it interpreted the rules as to which linkages were followed. The prototype also had a variety of help mechanisms ranging from help screens in the use of the system to dictionary definitions of word meanings, etc.

(2) It accumulated data in the form of fuzzy sets (attributable to each of 6 separate personality types). At the end of each sequence a student could view the whole sequence set and make modifications as required.

One of the first results to come out of the study was that the answers from the fuzzy approach were different from the yes/no approach. Further, when answers to questions were expressed as fuzzy variables, it was perceived that not all the questions were required. In other words, if within a given threshold for a particular question, virtually the entire sample (the test was given to some 320 students) were scored as 'artistic', then that answer could be discarded. In this way a set of the questions could be honed as the purpose of the test was coming up with discriminating, rather than common, pointers.

A major goal of the study was to evaluate the design approaches used in the soft system, and specifically the treatment of such imprecise data. In this regard students were asked to evaluate the system. Some indicative responses are given below. The responses may provide some helpful ideas for other designers.

(i) The approach:

(a) I prefer this over the manual system; you get more involved; this method provides occupations you may not have considered before or may not know about.

(b) Even in this form it would be a valuable tool in reaffirming someone's own desires, but it should not stress its own finality i.e. other forms of counselling are needed.

(c) The computer is a lot more fun.

(d) I like it because it is easy to operate and there is a feeling of confidentiality about communicating with a computer rather than a live interviewer. There is a feeling it would be objective, analytical and unbiased.

(e) The program seems more personal when presented in this format, because it gives the impression that there is more control over the information being gathered; that it reflects a more individual picture than is achieved by ticking boxes (i.e. in the manual version).

(f) Package not OK for high school students because explanations needed for each job.

(g) I wish I had this when I was at school; it is a marvellous idea and it deserves developing to its utmost potential.

(ii) Comments on career choices:

(a) Career choices match very closely with the type of career positions I have held over the last 10 years.

(b) Quite fun to do, but the career choices were very wrong for me I think.

(c) May be difficult for some respondents to assess accurately their own personality traits.

(d) I went through the program twice; the first time the job selection was satisfactory; the second time the job was an actuary. I don't know what an actuary is so I am unable to comment on whether or not it is a suitable option for me.

(e) The job list seems very restrictive

(iii) Technical aspects:

(a) The package should be designed so that the person who is answering it can go back to the previous question if necessary; they may like to add something, or if they miss a question by mistake (in fact it is possible to alter answers after a whole set but this seems insufficient).

(b) I was not able to go through all the questions first to get an idea of the questionnaire as a whole, which I find a disadvantage. Also there is no way of going back into the program or jumping forward.

(c) You need a progress report part way through to break it up and to encourage you to keep going.

(d) On a manual questionnaire you can miss out sections that don't relate to you; you cannot miss something out and come back to it; I think the program would be better if you could skip areas you had no interest in at all.

(e) The program was easy to follow, in some cases too easy as when there is no challenge it is easy to get bored with something.

(f) Too many instructions. It was annoying to have to read them over and over again in case they contained something different.

(g) There was some difficulty with the definitions being inter-mixed with the instructions; these should be totally separate (the student screens were mono).

(h) A bit too much reading; also makes the screen less cluttered and simple to read to help maintain interest; more icons would help.

## A system for interest rates

## Background

Unfortunately the careers advising study had to be put on hold. The Careers Advising Unit was to be moved from the Department of Labour to the Department of Education which in turn was to become a Ministry. The jobs of the advisers to this project were to be abolished and new ones readvertised. Other priorities thus endured. In the circumstances it was decided to pursue the investigation into soft systems with one designed to handle interest rate predictions.

The soft systems approach was tried because of inadequacies of existing predictive systems in coping with the effects of major disruptive political factors on the economy.

The current New Zealand Labour Government has had a number of internal disruptions, squabbles and crises in confidence, largely brought about by a conflict between a laissez-faire reformist Minister of Finance and his supporters, and the left-wing Labour political party. In particular there have been a fundamental series of disagreements about the economy and methods for lowering inflation and interest rates and arresting unemployment. The disagreements subsequently ended in the sacking of the Minister of Finance and a close associate. The impact of these political disagreements has caused distortions in the financial indicators which were proportionally much greater than those one would expect from normal market forces.

Not surprisingly, there are all sorts of experts who, at the time, had a view on where interest rates were heading, and indeed there is a thriving interest rate futures market. There tends to be multiple, and sometimes conflicting, opinions, especially when there is a political crisis. In other cases routine predictions offered by economic forecasting agencies are available for inclusion into the system.

It should be emphasised that while the system was designed to provide better interest rate predictions, an information systems goal was to investigate streamlining the knowledge elicitation and input phases. In developing the system techniques used in earlier expert systems were combined with techniques which seemed more appropriate to the area under study. In particular, it was seen that a given opinion could be broken down into a series of predictions over time. Fuzzy set theory could then be used in aggregating the series of predictions into an overall one generated by the system. Further goodness factors could be developed and assigned to the various opinion sources as an indicator of their reliability and accuracy.

## The need for soft information

The political machinations which overwhelmed the more fundamental driving factors in the market (e.g., supply and demand) have already been mentioned. It was quite clear therefore that a further dimension needed to be added to the system, namely an estimate of the potential impact of a political disruption. Intuitively one could postulate a particular event having a minor, major or possibly neutral effect. The effect would assume different values over time. One opinion might be that interest rates 'will increase for a while, and then level off'. This implies that a graphical representation would be appropriate.

Returning back to the economic section, the aim of the soft information system would be to distil predictions in terms of their reliability and to attempt to equate certain kinds of events in terms of their impact. As will be discussed below, the soft descriptor is used because essentially the information being fed into the system consists of predictions and opinions. The intent of the system is therefore to compare the soft information with the eventual hard information, representing the true and accurately recorded indicators as they actually occur. A description of this soft information system is described in subsequent sections.

## The model

## Model overview

A schematic diagram of the model of the system for entering, storing and analysing soft data is displayed in Figure 2. The approach used is particularly suitable for soft data on a numeric index — preferably one that is updated regularly so that a constant stream of hard data is available.

![](/api/attachments/7C9U3P55/fulltext/images/c28625fe88a3354ff7412b73dd56302e3d65b7e19d0a7ae4da432a3865bd5e08.jpg)  
Figure 2. Overview of system functions.

The model consists of a number of distinct components, as shown in flow diagram form in Figure 3. These were implemented separately and combined as modules to make up the system.

The basic operation of the system runs along the following lines: data can be entered directly into the data interface or can first be given meaning by the data interpreter. The data interface summarizes the data for storage purposes and stores it in the current soft data file.

As will be seen later, the soft data consists of one of more points of a predictive information set. For convenience, this set is known as an information set. Each information set will have originated from a particular source which is given a unique code. This code is stored with the data and appears in the source reliability file along with a factor indicating how reliable the source has been for making accurate predictions in the past. This factor is called the goodness factor (GF) for the source. New sources will have neutral GFs. Hard data is also entered into the system through the data interface and stored in the hard data file.

An additional feature is the data comparator which compares currently active soft data from the current data file with what has actually happened (i.e. the data from the hard data file). Each active information set has its accuracy evaluated and has a GF attributed to it. The GF is updated as time progresses. When the active time-frame for a particular information set has expired (i.e. its impact is zero) it is archived in the archive file. Its final GF is appended to the source GF, which is updated in the source reliability file.

## The data interpreter

As much of the soft data that is available is very imprecise, an interpreter is needed to give the data some meaning. In its basic form the interpreter is a human processor knowledgeable in the area under study. That person must take an opinion or prediction from whatever source (e.g., financial journal, economic prediction service) and recast it into a form acceptable to the system.

![](/api/attachments/7C9U3P55/fulltext/images/1e713ba6ec3300da0bc00493df778f1968989bbcab69c67901bf5a44fa53fd15.jpg)  
Figure 3. Model of the soft data system.

## The soft data interface

This key component of the system is shown diagrammatically in Figures 4 and 5. The aim of this interface is to aid the user in formulating and recording opinions and predictions of future movements of the index under study. The interface essentially quantifies the input. The first entry is the selection of the particular arena the opinion is based on. The choices are Political, Economic, Sentiment, External and Markets. Thus, if the opinion is based on the contents of a political event (e.g., Cabinet infighting) the Political would be appropriate. However, if an opinion is based solely on “gut-feeling” then Sentiment would be the option to choose.

Although this input is important for the purposes of labelling an information set, it is currently not used for anything else. Its intended purpose is so a history can be built on each of these areas and then used to aid prediction.

The next step is the selection of the general direction of movement for the index (refer to Figure 5). What was wanted was a human-machine interface that accurately reflected how a human perceived a trend, range of predicted values, or movement over time. A typical prediction might be that 'interest rates are expected to rise until March and then level off or even fall slightly'. It was felt that intuitively a graphical representation would closely approximate how an individual perceived the pattern. Subsequently it was found that people with little computer experience readily grasped the idea.

![](/api/attachments/7C9U3P55/fulltext/images/b905ee4290b9779bf45b7847f31d319fbcee322ef893a912082537ace5ce013f.jpg)  
Figure 4. Soft data interface.

![](/api/attachments/7C9U3P55/fulltext/images/0b6bfcdd44884edd148247279e5aab0f119f92165e6759ee854f39d860bc7d18.jpg)  
Figure 5. Magnitude and shape definition.

In the system the options are:

(1) Constant curve slope.

(2) Increasing curve slope.

(3) Decreasing curve slope.

(4) Single point prediction.

The first three options are for a movement over a period of time. The increasing/decreasing curves may be exponential i.e., small change to start with, magnitude of changing increasing, or logarithmic, i.e., large change at beginning, magnitude of change decreasing over time. The last option is a prediction of the value at a single point in time. The entry for this is very similar to entering hard data, that is the date and then the value at the date of entry.

If the prediction is not constant over time then increasing or decreasing curves must be selected. Basically three curves are presented:

(i) Once a curve has been selected, the size of the movement must be indicated. This is where a degree of fuzziness is introduced. Every person has a different idea of what constitutes a large, small or medium change. Thus a particular forecaster may predict a large movement in an index; another a relatively small movement, and yet both mean essentially the same thing. We are dealing with fuzzy concepts such as large, small or somewhere in between. To cope with this situation a magnitude factor is chosen on a five point scale. From this entry largeness measures are associated with each source so that over time, a specific meaning can be imputed when a particular source says large, small or whatever. Over time, then, the degree of fuzziness can be reduced (assuming the source is reasonably consistent).

(ii) Once the shape of the curve and its magnitude have been selected, it is necessary to define the beginning and ending dates over which the prediction is in effect. This may be suitable for some predictions, but in some cases, a prediction implies the presence of break points at intermediate points (for instance, reflecting the statement ‘rising and then levelling off’). In effect when intermediate points are used the original curve is corrected to reflect time intervals on a ratio scale. The process is depicted in Figure 5.

(iii) The last step in the process is to enter the information source so that over time the accuracy evaluator (described below) can assess the goodness of each source.

## The accuracy evaluator

In very basic terms, the accuracy evaluator compares the soft data with the hard data over the same timeframe and evaluates how accurately the predictions estimate the actual index movements.

A given soft data element (i.e., a prediction) over a number of points in its life is compared against the hard data. When the accuracy evaluator is started, all non-archived soft data is scanned to see if hard data exists over its time-frame. Those points which have not already been evaluated are compared with the actual. It is here that accuracy and GFs are used to record how close the predicted was to the actual (for the difference between these two factors, see below). After each new point has been examined, the GF for the information set is updated. The GF associated with the individual data element is added to the GF associated with the source. When this is complete the data, together with its GF, is archived according to source. This way, the GF contains the historical predictive accuracy for the information set and for the source of that data. The mathematics involved in process is presented in the Appendix.

## The predictor

The predictor uses the information in the system to make a prediction at some date in the future. The predicted value, and the GF, an estimate of the likely accuracy of the prediction, for the prediction, is displayed. In line with the conventions associated with fuzzy logic the GF is represented on a scale of from 0 to 1, with 0 being very bad and 1 being extremely good. When a future date is selected the predictor examines all the soft data active on that date. It then uses the GFs of these data combined with the GFs of the source of the data as an aggregated weight to form one overall prediction. This becomes the system prediction.

## Conclusions

The paper describes systems which handle soft information. This has been defined as any information which is not explicitly known to be true. A characteristic of such soft information systems is the difficulty of eliciting clear-cut answers to questions asked, and the further difficulty of expressing values, opinions and the like as meaningful measures. To help overcome this problem use was made of fuzzy logic.

Three soft information systems are described. The first is an adaptive system developed by the Decision Analysis Unit of the LSE. Clients searching for a career are encouraged to express their views as to a possible career in the form of a hierarchy of values. Clients are asked to weigh alternative views or values and decision theory is used to assign appropriate weights. The system is called adaptive because the original list of values may be decomposed and restructed with values given by the client.

<table><tr><td colspan="2">● predicted</td></tr><tr><td rowspan="2">○ actual</td><td>● predicted</td></tr><tr><td>○ actual</td></tr><tr><td>Low AF (say 0.3)</td><td>High AF (say 0.8)</td></tr></table>

The second system derived from the one developed at LSE, was also in the nature of a careers advisor. Here fuzzy logic was used explicitly to reduce the number of questions down to those which discriminated one set of abilities from another. Students using the system often found it easier to deal with a computer than with a human interviewer. Many of the comments received from the students will be helpful for future designers.

The third system, described in some detail, was used to distil the opinions of so-called experts on the likely impact of 5-year New Zealand Government Stock. Such experts typically consisted of financial writers and professional economic services. The system must be able to handle often contradictory and vague opinions as to the future movement of an economic index. Equally, for an economic model, it could be a measure representing the level of inflation, foreign exchange movements, commodity prices and the like. The basic requirement in this case, is that at some stage a physical index (i.e., actual measured or hard data) must be available.

Over time, various sources of opinion and prediction (soft data) could be evaluated against what actually happened (hard data). In this way the various sources could be assessed as to their accuracy. To do this some of the ideas used in earlier expert systems and some elements of fuzzy set theory, were adapted and incorporated in the system. As well as being able to measure and compare the goodness of the soft information sources, the goodness factors can be used to weight each source in terms of arriving at an overall prediction. In this the system shows considerable promise.

All three systems belong to a class of information systems called soft information systems. In this world, variables can have multiple values, reflecting as does the real world, a situation where everything is neither black nor white. It is considered that there are many applications both in industry and the social sciences, where this applies and it could be that such systems produce a new challenge to systems designers.

## References

Carroll, J. M. and McKendree, J. (1987) Interface design issues for advice-giving expert systems. Comm ACM, 30.

Duda, R., et al (1978) Development of the PROSPECTOR system for mineral exploration. SRI Report Projects 5822 and 6415, Stanford Research Institute, Palo Alto.

Holland, J. L. (1973) Making vocational choices: a theory of careers. Prentice-Hall, Inc., Englewood Cliffs.

Holland, J. L. (1982) The self-directed search: a guide to educational and vocational planning. NZ Council for Educational Research, Wellington (NZ adaptation).

Holsapple, C. W. and Whinston, A. B. (1987) Business expert systems. Irwin, Homewood, Ill.

Jonnson, R. C. (1989) That fuzzy feeling. Datamation, July 15, 39–43.

Shortliffe, E. H. (1976) Computer based medical consultations: MYCIN. American Elsevier, New York.

Naylor, C. (1984) How to build an inferencing engine, from Expert systems – principles and case studies. Chapman and Hall, London.

Dubois, D. and Prade, H. (1985) A review of fuzzy set aggregation connectives. Information Sciences, 36, 85–121.

Silvert, A. (1979) Symmetric summation: a class of operations on fuzzy sets. Transs IEEE, Systems, Man, Cybernetics, 9, 659–67.

Wooler, S. and Lewis, B. (1982) Computer-assisted career counselling: a new approach. British Journal of Guidance and Counselling, 10.

Wooler, S. (1985) Let the decision maker decide!: a case against assuming common occupational structures. J. Occupational Psychology, 16, 2, 217–27.

Wooler, S. and Wisudha, A. (1985) An educational approach to designing computer-based career guidance systems. British J. Educational Technology, 16, 2, 135–44.

## Appendix

Soft system mathematics

Goodness and accuracy factors

Goodness and accuracy factors are both measures of accuracy. Accuracy factors (AFs) measure the accuracy of a point prediction. That is, the predicted and actual values are compared at a certain point in time. Example:

A goodness factor (GF) for a series prediction (a constant stream of predicted points) measures how well the predicted points represent the actual movements. Thus, it consists of a number of AFs combined together. Example:

![](/api/attachments/7C9U3P55/fulltext/images/a1fce1cd9e962a65d3b7295ec221eb37a12b235ee5a682570fcb6b77c48b0ef6.jpg)  
A GF for a source is a measure of the past record of the source at predicting the future. Example: a source that is constantly making predictions which are incorrect will have a low GF attributed to it. However, if the same source started making a number of accurate predictions then its GF will increase. Note that the $(0,1)$ scale has been selected arbitrarily. A -1 to 1 scale was considered (with 0 being perfect and -1 and 1 being the imperfect extremes). The $(0,1)$ scale has an advantage in that it fits more in the line of probability and fuzzy set theory.

## Measurement of accuracy factors

Given a predicted point $(p)$ and the actual value of that point (a) at a certain time $(t)$ , we wish to be able to make a comparison and measure the magnitude of difference in terms of the $(0,1)$ scale. The formula used is as follows:

$$
\mathrm{AF} (\mathrm{at} t) = \frac {(\mathrm{a} * r) - | p - \mathrm{a} |}{(\mathrm{a} * r)}
$$

$$
(\text { If   } \mathrm{AF} <   = 0 \text {   then   } \mathrm{AF} = 0. 0 1)
$$

where r is a proportion between 0 and 1 which alters the zero point for the AF measurement. Note that if r is 1 then the AF is simply p/a (if p < a).

Altering the value for r will change the degree of accuracy for predictions quite considerably. Thus, the value will depend on the area being examined. For example a prediction of 9 mm daily rainfall compared with a measured 10 mm might be considered to be quite accurate, where as a 9% interest rate prediction against the actual 10% is quite inaccurate. In the first case, a higher value for r would be used than in the second when measuring the AF.

The implemented system was tested using data from the New Zealand 5-year Government Stock market. With this target, an r value of 0.1 is used and seems to return sensible figures.

## Combination of accuracy measures

There are two cases where we wish to combine accuracy measures. The first is where the GF of a series prediction is to be updated. The old GF is combined with the AF of the new data point to make a new, updated GF. It is suggested that the initial GF for a prediction be 0.5 (neutral i.e., we do not know whether it is good or bad). With each further point that is evaluated, the GF will be updated.

The other case is where the time-frame for a prediction has expired and a prediction has been completely evaluated i.e. all points have been compared and AFs calculated. Once this happens, the GF for the source of the prediction must be amended for the new results.

Conceptually, we want a function that if the AF is greater than the old GF, then it adds new goodness to it and thus the updated GF will be greater than the old. However, if the AF is less that the old GF, the reverse should apply, and the updated GF will be lower than the old one. Several methods have been investigated to do this.

Bayesian probability theory is used in several expert and inferencing systems (e.g., the PROSPECTOR mineral exploration system, Duda et al., 1978) to tie such information together and can be found in many mathematical texts.

In expert systems such as MYCIN (Shortliffe, 1976), the knowledge base is already built and the events they are dealing with are very precise. Symptoms are either there or not there. If they are, an increased probability of the correct illness being diagnosed is the result. The soft information system does not have this predefined knowledge base nor are the events and results clear cut.

Another problem with Bayesian theory is that independence between events is assumed. It is highly unlikely that the points in a time series can be considered to be independent of each other. One consolation is that the other expert systems like MYCIN also suffer from this problem (Naylor, 1984).

Fuzzy set theory is another possibility. This uses a $(0,1)$ scale to represent the degree of membership to a set. Fuzzy logic defines a very small set of operations to deal with uncertainty. These are:

$$
\begin{array}{r l} \mathrm {x \text {fuzzy AND y}} & = \mathrm{MIN(x,y)} \\ \mathrm {x \text {fuzzy OR y}} & = \mathrm{MAX(x,y)} \\ \mathrm{NOTx} & = 1 - \mathrm{x} \end{array}
$$

In attempting to apply this to our purpose, we see that our conceptual requirement above is not satisfied. However, further investigation into the area of fuzzy set theory has shown different types of aggregation connectives (Dubois and Prade, 1985) such as the symmetric sum (Silvert, 1979). Several of the interesting ones are listed below (@ is the aggregation function):

$$
\mathrm{x} @ \mathrm{y} = ((\mathrm{x} ^ {\mathrm{a}} \pm \mathrm{y} ^ {\mathrm{a}}) / 2)\tag{[Al]}
$$

This reduces to the following:

$$
\begin{array}{l} \mathbf {a} = - \infty \texttt {x @ y} = \mathbf {M I N (x , y)} \\ \mathbf {a} = - 1 \texttt {x @ y} = 2 \mathrm{xy/(x+y)} \\ \mathbf {a} = 0 \qquad \mathbf {x @ y} = \mathrm{xy} \\ \mathbf {a} = 1 \qquad \mathbf {x @ y} = (\mathrm{x+y}) / 2 \\ \mathbf {a} = + \infty \texttt {x @ y} = \mathbf {M A X (x , y)} \end{array}
$$

(Harmonic Mean)

(Geometric Mean)

(Arithmetic Mean)

$$
\mathrm{x} @ \mathrm{y} = \frac {\mathrm{xy}}{1 - \mathrm{x} - \mathrm{y} + 2 \mathrm{xy}}\tag{[A2]}
$$

$$
\mathrm{x} @ \mathrm{y} = \frac {\mathrm{x} + \mathrm{y} - \mathrm{xy}}{1 - \mathrm{x} - \mathrm{y} + 2 \mathrm{xy}}\tag{[A3]}
$$

$$
\mathrm{x} @ \mathrm{y} = \frac {\text { MIN } (\mathrm{x} , \mathrm{y})}{1 - | \mathrm{x} - \mathrm{y} |}\tag{[A4]}
$$

$$
\mathrm{x} @ \mathrm{y} = \frac {\mathrm{MAX} (\mathrm{x} , \mathrm{y})}{1 - | \mathrm{x} - \mathrm{y} |}\tag{[A5]}
$$

Equation A1 above reflects several averaging techniques. The problem is, however, that the mean of two numbers, one of which is the mean of all the past results, will not fairly reflect the past. A long run average (arithmetic or geometric) does seem to give good results. Alternative A2 was tested in the system and was found to satisfy the requirement above. It also seemed to work well except that it was inclined to produce high results. Alternatives A4 and A5 were also tested with far better results. Alternative A4 again tended towards high results with A5 being a lot more conservative. In the event, Equation A5 was the one eventually selected for use in the system. There is no clear best or correct method; the one selected depends on many factors, including the subject being investigated, computer memory and programming language constraints.

## Aggregating and weighting future predictions

In order to get output from the system, we need to take all the predictions about the future and combine them so as to obtain one overall prediction. To achieve this, the prediction(s) for the desired time period in the future are taken and weighed by the updated GF of their source (the combination of the source GF and the current GF of the date). The arithmetic average of these weighted values is calculated to give the prediction. A GF for this is provided by simply averaging the source GFs. Another idea to calculate the GF for the prediction would be to weight the weights.

$$
\text { Overall   prediction } = \frac {\sum (\text { prediction } * \mathrm{GF} \text { of   source })}{\sum \mathrm{GF} \text { of   source }}
$$

Example: suppose three predictions were available for a particular future date: 9.0, 10.0 and 15.0, and these predictions had respective source GFs of 0.8, 0.9 and 0.5. Obviously, more weight will be put on the first two. The calculation is as follows:

$$
\begin{array}{r l} \text { Overall   prediction } & = \frac {}{0 . 8 + 0 . 9 + 0 . 5} \\ & = 2 3. 7 / 2. 2 \\ & = 1 0. 7 7 \end{array}
$$

This has a GF of 2.2/3 which is 0.73.

A geometric average would probably be better, but due to the fact that an nth root function is not available, it is not used. The above method is currently being tested in the system. Once a good history of the sources prediction accuracy has been developed, the predictions will be fed back into the system to provide another source of information.

## Biographical notes

Ivan F. Jackson is Professor of Management Information Systems at Victoria University of Wellington. David Hosking was a research assistant in the Information Systems Group there. Jackson also acts as a management consultant with PA Management Consultants. He has been working in the computing area since 1961. He worked in the USA in large systems sales development with Burroughs Corporation and as a management consultant in Salt Lake City. He returned to New Zealand in 1972 and became Director, Systems Development, with the State Services Commission. He spent 12 years at Otago University and published Corporate Information Management in 1986. He has been active in a number of governmental reviews, most recently of electronics and information technology with the Department of Scientific and Industrial Research.

Address for Correspondence: Professor Ivan F. Jackson, c/o Information Systems Group, PO Box 600, Victoria University of Wellington, Wellington, New Zealand.
