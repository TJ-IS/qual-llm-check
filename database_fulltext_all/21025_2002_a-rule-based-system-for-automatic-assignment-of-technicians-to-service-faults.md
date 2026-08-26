---
otero_id: 21025
otero_key: "QW9BAEEM"
title: "A rule-based system for automatic assignment of technicians to service faults"
authors: "Avinoam Lazarov; Peretz Shoval"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00122-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A rule-based system for automatic assignment of technicians to service faults

Avinoam Lazarov, Peretz Shoval\*

Department of Information Systems Engineering, Ben-Gurion University of the Negev, Beersheva 84105, Israel

Received 1 October 2000; received in revised form 1 June 2001; accepted 1 August 2001

## Abstract

We present a model and a prototype system for the assignment of technicians to handle computer system faults (including hardware, software and communications) that are reported by users connected to the organization’s computer network. The model attempts to simulate the assignment process of technicians, as carried out by the manager of a help desk. The model has been developed on the basis of a detailed study of the process of handling faults and the assignment of technicians in a number of organizations. In order to validate the model, simulation tests have been carried out, designed to compare the results of the model’s assignment process, in hundreds of cases, against assignments carried out by experts who participated in the experiments. The results show that in 48% of the cases, the system’s assignment of technicians was better than that of the experts, and that in 92% of the cases, the system achieved results as good or better than did the experts. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Help desk system; Decision support system; Assignment of technicians to faults; Rule-based system; Decision rules; Information retrieval

## 1. Introduction

We live in an era when organizations are equipping themselves with computer systems, communication devices, and many and varied software. A side effect of this circumstance is an increase in the number of computer system, communications and software faults, thus placing a burden on service agents. In most organizations, a user with a system failure calls a help desk and reports the problem. The manager of the help desk (or someone authorized by him/her) examines the report and decides which technician he believes is best suited to handle the case. The aim is to deal with the fault appropriately and efficiently, that is, as fast as possible, and with the least outlay in money and other resources. Selection of the technician most suited to deal with the reported failure is a complex procedure, requiring the application of a wide range of considerations, and its quality depends on experience. The problem becomes more acute as the frequency of faults increases, while the number of available technicians is limited. Another aspect of the problem is the ability of the manager, skilled and experienced as he may be, to weigh in the balance the wide variety of factors needed to assign the best technician to deal with a sudden emergency. It transpires that, in practice, the principle, and sometimes the only consideration in such an assignment, is that of location—that is, help desk managers assign an available technician who is closest to the place where the problem occurred—neglecting other relevant factors, such as suitability, experience, risk, etc.

To assist the manager of the help desk to handle this problem, a computerized model and system, Routing Faults System (RFS) has been developed. The principle aim is optimal assignment of technicians to service faults, taking into consideration a wide range of criteria, as well as the execution of the assignment task under conditions of pressure, that is, when there are many failures. The system applies a model for the assignment of technicians to faults that is based on three main stages: (a) analysis of the user report, to determine the nature of the fault; (b) execution of an initial selection of suitable technicians, based on a correlation between the nature of the fault and the technicians’ skills; and (c) execution of more refined selection of the most suitable technician, based on assignment rules that test the characteristics of the fault, the organization, and the above suitable technicians.

The model has been developed on the basis of a detailed study of the process of handling faults and the assignment of technicians in a number of organizations. In order to validate the model, simulation tests have been carried out, designed to compare the results of the model’s assignment process, in hundreds of cases, against selections carried out by experts who participated in the experiments. The results show that in 48% of the cases, the system’s assignment of technicians was better than that of the experts, and that in 92% of the cases, the system achieved results as good or better than did the experts.

The paper is structured as follows: the rest of this section surveys relevant areas of research into the problem under discussion, including operations research and expert systems. Section 2 details the model and the RFS systems that were developed to solve the problem. Section 3 describes the experiments that were carried out in order to evaluate the model and compare the choices it made against assignments by experts in the field. The results of the experiments are presented in Section 4, while Section 5 summarizes the study and suggests topics for further research.

## 1.1. Treatment of the problem by the operations research approach

The problem of assigning suitable technicians to service faults touches a specific field of operations research known as the assignment problem [1,2,3,7,8]. This problem is dealt with by means of linear programming. In the linear solution of problems, a target function is formulated which we want to maximize or minimize, under certain constraints. The solution of an assignment problem requires the existence of two properties: (a) feasibility—there is a solution to the problem as long as the supply equals the demand; (b) integrality—whenever the sources and the end targets are integers, every solution must also be an integer.

The solution of the problem of assigning technicians to service faults by means of ‘‘pure’’ operations research methods is problematic for the following reasons.

(1) In order to deal with the problem using operations research methods, it is necessary for the constraint—that the number of sources equals the number of end targets—to hold, but this requirement does not correspond to reality. In practice, two problematic conditions may hold: (a) starvation—there are more sources than targets, that is, more technicians than faults (latent unemployment of technicians); (b) flooding—there are more targets than sources, that is, the number of faults in the system is more than the available technicians can handle.

(2) A solution of the assignment problem assumes that the number of sources and end targets is equal and that a source for every target must be found, such that the total measured cost (that is, the target function) is minimized. From this assumption, two main problems arise.

(a) The target function for the solution covers only one aspect (e.g., minimum technical cost, minimum service time, minimum cost of service, maximum level of skill, etc.). In order to overcome this difficulty, the problem can be solved several times, with a different aspect being tested each time, and then aggregating the results and calculating a suitable average upon completion of the process. Such a solution is clumsy and time-consuming. Moreover, the weighting of the individual results to calculate the final solution is problematic.

(b) The assumption is that any source can service any target. In our problem—assignment of technicians—it is wrong to assume that all the technicians are equally competent to handle all types of fault. Moreover, it may well be that a particular technician is totally unsuited to service a specific fault. The assignment model does not permit consideration of differing skills between technicians (sources), in order to confine the assignment of certain technicians to some of the faults.

(3) The mathematical handling of the assignment problem assumes that the ‘‘rules of the game’’ are known in advance. Such rules include standard service duration, standard time of arrival to carry out servicing, etc. As noted, the solution is expressed in terms of a target function and predefined constraints, and it is impossible to introduce different decision rules as may be demanded by the situation. However, in the type of problem before us, it is necessary to consider and put into operation various decision rules, in accordance with changing needs.

## 1.2. Treatment of the problem by the expert systems approach

An expert system is an intelligent computer program that accumulates information regarding a particular field and then uses that knowledge and an inference mechanism in order to solve difficult problems requiring special expertise in the given field [5,6,10].

In many cases, an expert system does not solve a problem, but supplies information to the customer (user) on how to act to solve the given problem. The reasons for using expert systems partly correspond to those for which we make use of human experts [4]: attainment of faster and more reliable solutions, decrease in costs, reduction of monitoring procedures, lack of experts and wider access to information. Weiss and Kulikowski [12] noted a number of situations in which it is advisable to use expert systems: when it is difficult to find (human) experts in the field; when the cost of experts’ services is high; when much improvement is needed in the available knowledge, which can be gained from experience by using inference rules; when the problem is not sufficiently defined; and when the data of the problem and the relevant rules change frequently.

There exists a wide range of very different expert systems, both in their planning and design, and in their capabilities. Nonetheless, they do have a number of common properties and components [4,6,9]. An accepted approach for applying expert systems uses a ‘‘knowledge base’’ (KB), which contains a set of rules in the form ‘‘if situation ( then action’’. Each one of the KB rules is meant to be relevant for analysis of some aspects of the problem in the application area. Two formats exist for following rules in the process of searching for a solution. (1) Forward chaining—applying ‘‘rules forward’’: if the ‘‘situation’’ condition holds, do ‘‘action’’. (2) Backward chaining—applying the rules in the opposite way: if you want ‘‘action’’ to happen, do ‘‘situation’’. Application of the rules is not based on data existing in the KB, but on the desired result.

Unfortunately, the rules do not always enable unambiguous results to be obtained, and it is often necessary to make many more assumptions, even after the rules have been applied. Therefore, every expert system needs to have a mechanism known as ‘‘inference engine’’, which must sometimes operate under indeterminate conditions or incomplete information. This requires information to be cross-referenced and needs the application of a number of rules that can complement one another.

To sum up, in light of the shortcomings of operations research methods in solving our problem, and in light of the properties of expert systems, we decided to develop a model to solve the problem, which applies both statistical methods and rules for assigning technicians to reported faults. The rules apply the knowledge and work procedures of experts who carry out such assignments in the field.

## 2. Model for assigning technicians to faults

## 2.1. Principles and assumptions of the model

The purpose of the model incorporated in the RFS system is to assign the most suitable technicians to deal with hardware, software, or communications faults as reported by the users. The model solves the problem in a number of phases: In the first phase, an automatic analysis is performed on the report of the fault received from the user. It may be assumed that the report is sent via electronic mail, fax or telephone, and that it is expressed in the form of text (i.e., sentences and phrases formulated in commonly used language). The first goal is to analyze the report automatically to allow the system to proceed. In this phase, one of the problems is to deal with words/terms appearing in the report that have more than one interpretations. For example, let us look at two reports containing the word ‘‘access’’; (a) ‘‘I can’t open access’’; (b) ‘‘I can’t access the net’’. In the first case, it is probable that the user wishes to say that he or she cannot operate the data management program MS-Access, while in the second case, the user probably wishes to indicate that he or she cannot connect to the network. The result of the first stage of the model is the translation of the report into a vector of standardized keywords that represent the reported problem.

The main problem that the model handles is the assignment of the most appropriate technician to service the fault. The problem’s solution involves testing the correlation of the details of the fault with various parameters that characterize the technicians and the organization. In the search for the solution to our problem, the work of managers of help desks in leading Israeli companies was observed, and interviews were conducted with experts in the field (heads of departments, team leaders and help desk managers) in order to learn about their thinking and assessments when assigning technicians. As a result, a multi-stage model was defined: (a) In the preliminary stage, described earlier, the user’s fault report, which is submitted in natural language, is analyzed and converted into a weighted list of keywords. (b) In stage 2, initial selection, statistical correlation is carried out between the keyword vector representing the fault, and keyword vectors representing the qualifications of the technicians in the organization. The result is a selected group of the technicians most qualified to service the fault. (c) In the third stage—rule-based selection—assignment rules are applied that relate to properties of the fault and of the organization, as well as to the further characteristics of the technicians selected earlier. As a result, each of the relevant technicians gets a more accurate rating of qualification. (d) In stage 4, the optimal assignment is made, taking into account not only one fault that must be serviced by the most suitable technician, but the accumulation of a number of faults to which a similar number of the most suitable technicians must be assigned.

Fig. 1 presents the process-flow diagram of the model. Before describing the model in detail, here are a number of assumptions that we make, based on observations and interviews with experts working in the field in various organizations.

(1) Number of faults reported per workday: during the workday, the average number of reported faults shows a low level of variation. That is, it is possible to anticipate the number of faults with a high degree of confidence (of course, the number of daily faults varies from organization to organization).

(2) All the reported faults are dealt with on the same day: in most of the organizations, at least 90% of the faults are dealt with on the day they are reported. The model assumes that all the faults are dealt with on the day of the report. In other words, every fault must have a technician assigned to it.

(3) Various fields of technicians expertise: in most of the organizations, it is assumed that nearly all the technicians can handle all types of fault, and so the main consideration in making an assignment is the geographical location of the technician vis-a\`-vis the location of the fault. The model’s assumption is different: we assume that there are specializations, and thus, differences in the technicians’ abilities to service various faults. This assumption enables us to build a better assignment model than that commonly used in practice.

## 2.2. Analysis of fault report

As stated above, reports of faults come to the system in the form of textual sentences (let us say, by electronic mail or by the user filling out a form on an input screen). Automatic analysis of the message includes several actions: (a) breaking the report down into words—‘‘parsing’’; (b) removal of insignificant words; (c) a search for standardized keywords that will represent the report; (d) weighting of keywords. At the end of this stage, the user’s report is represented by a weighted vector of keywords. For example, the sentence ‘‘Neither the modem nor the hd are working’’ would yield a weighted vector, [modem(1), hd(1)], in which the numbers in parenthesis are weightings obtained by summing the number of times a keyword appears in the report.

![](/api/attachments/QW9BAEEM/fulltext/images/f5eaa5ef841dc65a3d0d296ac5d6d207d7bd97f7f1871342eece694427e5c7bb.jpg)  
Fig. 1. Process-flow diagram of the model and system.

## 2.2.1. Breaking down the report into words

In this sub-stage, the individual words of which the report is composed are identified. A word is a sequence of characters separated by one or more spaces, except for the first and last words.

## 2.2.2. Removal of insignificant words

In this sub-stage, removal of insignificant words is carried out, words such as ‘‘my’’, ‘‘or’’, ‘‘and’’. This is achieved by means of a ‘‘stop list’’; any word appearing on this list is eliminated from the report: thus, in the next sub-stage, only significant words are included in the analysis.

## 2.2.3. Search for keywords

In this sub-stage, the purpose is to replace words in the report with ‘‘standardized’’ words to represent the fault. To do this, the grammatical stems of the significant words must be found. This search for word stems can be executed in a number of ways, such as ‘‘lookup tables’’, ‘‘successors variety’’, ‘‘affix removal’’, and ‘‘n-gram’’. We have chosen to apply the ‘‘lookup table’’ method, in which all the relevant words for a particular field are stored in all the possible forms in which they can be used (such as singular and plural); for each word, its stem, defined as a standardized keyword, is recorded. Of course, it is probable that many words have the same stem. On possible way to apply lookup tables is illustrated in Fig. 2. The table ‘‘Terms’’ includes all the significant words, in their various forms, each with a number indicating its keyword. The ‘‘Keywords’’ table lists all the numbers and names of the relevant keywords.

The main advantage of this method is that, except in cases of human error (incorrect input), there is no danger of error in identifying a keyword. A further advantage is the ability to search by use of synonyms or similar words. For example, ‘‘hard disk’’, ‘‘hard drive’’ and ‘‘hd’’ are regarded as synonyms and can thus be accorded the same keyword (hd). The disadvantage of this method is that the database must include all the significant words and their variants (e.g., plural and singular).

## 2.2.4. Weighting of keywords

After the keywords of a report have been identified, they are weighted in order to establish their importance in the fault report. This sub-stage has two parts.

(1) Counting the frequency with which each keyword appears.

(2) Correction for phrases: a user’s report may include phrases that have a specific meaning different from those of the individual words they contain. For example, let us say a report has been received with the sentence, ‘‘I can’t restart windows explorer’’. Analysis of the individual words is likely to create the following keyword vector: [windows(1), explorer(1)]. That is, there are, apparently, problems with the ‘‘Windows’’ operating system and with the Internet browser ‘‘Explorer’’. However, the user’s intention was actually to report that he or she could not open the file manager of the Windows system (known as Windows Explorer). This problem is found in the system because the Terms Table includes the phrase ‘‘Windows Explorer’’, which indicates the keyword ‘‘explorer’’. That is, phrases in the database have to replace their individual words, and thus, the keyword vector representing the report is corrected.

## 2.3. Initial (statistical) selection of technicians

This stage is designed to find suitable technicians of a certain level of ability to service the fault. To this end, a correlation is calculated between the keyword vector of the fault report and respective vectors of the various technicians. That is, every technician is represented by a weighted keyword vector that represents his or her degree of expertise and qualification to service the various faults represented by the keywords.

For example, let us assume that a fault report was received, stating ‘‘Neither my mouse nor my modem are working’’. Analysis of the fault report will create the keyword vector [mouse(1), modem(1)]. Now, let us assume there are three technicians characterized by the vectors: Tec-a: [mouse(100), modem(100), printer(100)]; Tec-b: [mouse(50), modem(50), printer(100)]; and Tec-c: [mouse(100, modem(100), printer(50)]. It can be seen that technicians Tec-a and Tec-c are equally qualified in this case, while Tec-b is less so.

![](/api/attachments/QW9BAEEM/fulltext/images/ae35b7314d8fcc8f7193a5a11222da5c605d4a9614ad98d4ad854d1b4c2e5438.jpg)  
Fig. 2. Application of lookup tables.

The correlation between the ‘‘faults’’ vector and the ‘‘technicians’’ vectors is calculated by means of the ‘‘cosine formula’’ that was presented in the SMART system [11]:

$$
\mathrm{cosine} (P _ {j}, M _ {i}) = \frac {\sum_ {k = 1} ^ {t} \left((P _ {j k} - \overline {{P}}) \cdot (M _ {i k} - \overline {{M}})\right)}{\sqrt {\sum_ {k = 1} ^ {t} (P _ {j k}) ^ {2} \cdot \sum_ {k = 1} ^ {t} (M _ {i k}) ^ {2}}}
$$

where fault report i is represented by vector $M _ { i t } \colon M _ { i 1 }$ $M _ { i 2 } , . . . , M _ { i t } ,$ while technician $j ^ { \circ } \mathbf { s }$ profile is represented by the vector $P _ { j t } ; P _ { j 1 } , P _ { j 2 } , . . . , P _ { j t } . { \overline { { M } } }$ is the average of the components of vector $\overline { { M } } _ { i k } ,$ while $\overline { P }$ is the average value of the components of vector $\overline { { P } } _ { i k }$

The rationale behind the formula is that the more qualified a technician is to service a fault, the higher a grade he or she receives. The formula takes into account not only the needs of the fault, but also other properties, such as over-qualification. For example, we saw earlier that technicians Tec-a and Tec-c have equal ability to handle the reported fault. However, technician Tec-a has greater skill regarding printers than does Tec-c. The correlation formula will actually give a higher grade to Tec-c, for if Tec-a is assigned to the fault, and a report of a printer failure is then received, technician Tec-c, being available, would have to be assigned, although he or she is less suited to service printer faults.

As a result of the correlation formula, a ranked list of relevant technicians is obtained. It is possible at this stage that two technicians can get the same ranking, but this is unimportant since a more refined analysis will follow. The size of the group can be established in a number of ways: (1) by setting a minimum rating, such that the group can only include technicians with that rating or above; (2) by setting a fixed number of technicians; or (3) by setting a fixed percentage of technicians.

There are some disadvantages in setting a minimum rating. If it is set too high, there is a risk that a group may come up empty. On the other hand, if the rating is set too low, the group may contain too many technicians, so that the screening of the technicians in the next stage is liable to be time-consuming. The advantage of this method is that it guarantees a minimal preestablished rating, beyond which only improvements can be made. In the two other methods (fixed number or percentage), the inclusion of a certain number of technicians, to continue to the second stage of selection, is assured. A further advantage of these latter methods is that while the list may contain a technician who received a low rating, he or she might actually be selected in the following stage, due to other considerations (to be detailed below).

In our system, we implemented the second method, that is, the inclusion on the list of a fixed number of technicians. The number we chose is half the number of technicians available in the organization. Although this a relatively high number, we made this decision because, overall, we had defined for our system only a small number of technicians (less than 10), and our aim was to transfer enough technicians to the following selection phase to enable us to test the effect of the assignment rules on the choice of technician.

## 2.4. Rule-based selection of technicians

The goal of the second stage is to refine the decision, that is, to choose the most appropriate technicians from the list of relevant technicians obtained in the first stage. This is accomplished by taking into account additional factors omitted from the correlation formula. For example, it may well be that the technician who received the highest ranking in the first stage is servicing another fault, located far away. The factors taken into account in this phase relate to the technicians’ qualifications and to various organizational parameters, and, as noted above, they are expressed in assignment rules.

## 2.4.1. Assignment rules

After many observations of the work of help desk managers and support personnel, and in light of the interviews conducted with experts from leading Israeli companies, a number of assignment rules were defined that apply their knowledge and thought processes. These rules allow many factors to be included in the assignment process, such as, technicians knowledge and skill, the organization’s work procedures, and so on. Most of the assignment rules were defined on the basis of observing and analyzing the help desk procedures. Small parts of the rules are new, in the sense that they were not utilized in practice by the organizations examined. In general, it can be said that in their daily work, the help desk managers do not apply a wide range of decision rules. This is particularly true when the pace of decision-making is high and work pressure does not permit thorough deliberation. In such an event, practically only one consideration is taken into account, the location of the reported fault in relation to those of the technicians (as detailed below). In contrast, our model makes use of a range of assignment rules and applies them to each fault and technician.

Table 2  
Table 1  
Suitability ratings by type of fault

<table><tr><td rowspan="2">Type of fault</td><td colspan="5">Technician</td></tr><tr><td>Tec-1</td><td>Tec-2</td><td>Tec-3</td><td>Tec-4</td><td>Tec-5</td></tr><tr><td>Hardware</td><td>80</td><td>100</td><td>100</td><td>70</td><td>20</td></tr><tr><td>Software</td><td>70</td><td>50</td><td>100</td><td>100</td><td>100</td></tr><tr><td>Network</td><td>100</td><td>60</td><td>0</td><td>70</td><td>50</td></tr></table>

It should be made clear that the set of assignment rules that we put into application in the model and the system is incomplete, and it is certainly possible to define additional rules. However, our goal was to demonstrate that the quality of assignment of technicians is improved by the application of such rules, rather than to ‘‘discover’’ all the possible rules.

There follow details and examples of the assignment rules that were applied in the model. Rule 1 (If (type of fault) = X, then suitability rating = Y).

This rule expresses the degree of suitability of the technician to the type of fault, distinguishing between faults in software, hardware and network. Table 1 shows the degrees of suitability recorded in the database for five technicians for each of the three fault types, and the ratings ranging from 0 (completely unsuitable) to 100 (completely suitable). Note: the values presented in the table, as in other tables below, are only examples: in practice, they are set by the help desk manager, or someone else authorized by the organization.

Rule 2 (If (subject of fault) = X, then degree of suitability = Y).

This rule expresses the degree of suitability of the technician to handle the subject of the fault. The subject of the fault is a subdivision of the type of fault, as exemplified in Table 2, relating to hardware. Here, too, the values range from 0 to 100.

Note: Rules 1 and 2 seem to overlap with the initial (statistical) approach, but they are included here because we want to consider the factors type and subject of fault in the overall rating of the relevant technicians. Rule 3 (If (cost of fault) = X, and (experience/seniority of technician) = Y, then suitability rating = Z).

This rule examines the estimated cost of the fault and the experience/seniority of the technician. The higher the estimated cost (that is, causing greater damage to the organization), the hope is to assign a technician of greater experience, in order to guarantee that the repair be carried out successfully. The suitability rating of each technician is determined by an appropriate combination of cost/experience. Below is a (partial) example: if the cost of the fault is high and the technician is highly experienced, the suitability rating will be 100, but if the technician’s experience is moderate, then the grade will be 50, while a new (trainee) technician would receive only a 20. On the other hand, if the cost of the fault is low and the technician is highly experienced, the suitability rating would be only 70, as opposed to his grade 100 when the cost is high. This rule is designed to prevent the ‘‘wasteful’’ assignment of a senior technician to a simple fault.

Rule 4 (If (risk level of the fault site) = X and (certification for risk of the technician) = Y, then suitability rating = Z).

This rule checks the risk level of the location where the fault occurred and the level of risk the technician is certified to handle. The risk level can be determined in various ways: for example, in a chemical plant, there are going to be areas with differing levels of risk. On the other hand, every technician has a certified level of risk to which he or she is allowed to be exposed. The considerations for determining such a level include family or social situation, and so on. In our system, we included three risk levels for the locations of the faults, and three levels of technician certification, high, medium and low.

Suitability rating by subject of fault (hardware type)

<table><tr><td rowspan="2">Subject of fault</td><td colspan="5">Technician</td></tr><tr><td>Tec-1</td><td>Tec-2</td><td>Tec-3</td><td>Tec-4</td><td>Tec-5</td></tr><tr><td>Monitor</td><td>100</td><td>30</td><td>80</td><td>80</td><td>30</td></tr><tr><td>Modem</td><td>80</td><td>50</td><td>100</td><td>70</td><td>20</td></tr><tr><td>Mouse</td><td>70</td><td>100</td><td>90</td><td>10</td><td>40</td></tr></table>

The purpose of the rule is to assign a technician with a certification level equal to the site risk level, but it is likely that the technician has a higher certification than needed. During the selection process, the following conditions can occur:

. Fault location risk level is higher than technician certification.

. Fault location risk level is equal to technician certification.

. Fault location risk level is lower than technician certification.

The differences between the fault location risk level and the technician certification, and the resulting correlation scores are shown in Table 3. A zero difference indicates full equality between the two, giving a score of 100. A positive difference (1 or 2) indicates that the technician can be assigned, but his or her certification is higher than necessary. A negative difference means that the technician does not have the necessary level of certification to service the fault. This case may be considered to be a limiting condition, ruling out the assignment of the technician (no matter what are the ratings on other rules). Another possibility is to regard such a case as special, but permissible, and to express the lack of sufficient certification by means of a low selection score. In Table 3, the latter possibility is illustrated, i.e., by use of low scores.

Rule 5 (If (type of fault) = X and (employment time of technician) = Y, then suitability rating = Z).

Table 3  
Suitability ratings by risk levels of technicians and faults (i – j)

<table><tr><td rowspan="2">Risk level of fault (j)</td><td colspan="3">Risk level of technician (i)</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>0 (100)</td><td>1 (80)</td><td>2 (60)</td></tr><tr><td>2</td><td>-1 (40)</td><td>0 (100)</td><td>1 (80)</td></tr><tr><td>3</td><td>-2 (20)</td><td>-1 (40)</td><td>0 (100)</td></tr></table>

Table 4  
Suitability ratings by percentage employment and type of fault (i – j)

<table><tr><td rowspan="2">Time of employment</td><td colspan="3">Type of fault</td></tr><tr><td>Software</td><td>Hardware</td><td>Network</td></tr><tr><td>1</td><td>50</td><td>80</td><td>100</td></tr><tr><td>1/2</td><td>80</td><td>50</td><td>50</td></tr><tr><td>1/3</td><td>100</td><td>40</td><td>20</td></tr></table>

The experience of the experts indicates that it takes longer to repair a hardware fault than to service a software fault, while network faults take the most time. For this reason, one must take into account whether a technician is employed full or part time. Even if a particular technician is suited to handle a fault according to other criteria, if she works only part time, there is a risk that she cannot deal with the fault on the same day, so a part-timer’s rating is lower than that of a full-timer. Table 4 exemplifies the suitability ratings for various combinations of type of fault and time of employment, given three levels: full, half and third.

The suitability ratings were determined with the aim of guaranteeing a good correlation between the typical time needed to service each type of fault, and the percentage employment of the technician. For example, for network faults, a rating of 100 is given to a full-time worker, since such a fault takes the most time to correct. For a hardware problem, the same technician gets a lower rating (80) and even lower (50) for a software fault. On the other hand, for software faults, which take, on average, the least time to correct, a technician working 1/ 3 part time gets a maximal rating and low ratings for hardware and networks (40 and 20, respectively).

Rule 6 (If (secrecy level of site) = X and (security clearance of technician) = Y, then suitability rating = Z).

This rule is similar to Rule 4, which deals with levels of risk. There are organizations that require an appropriate security clearance system for personnel (such as defense industries or companies making innovative products, etc.). Table 5 exemplifies the various possible conditions in applying this rule. Rule 7 (If (location of fault) = X and (location of technician) = Y, then suitability rating = Z).

This rule considers the geographical distance between the site of the reported fault and the technician. We should note that this is the principle rule taken into consideration in actual practice by help desk managers when assigning technicians to faults.

Table 6  
Suitability ratings by levels of fault secrecy and technicians’ security clearance (i – j)

<table><tr><td rowspan="2">Level of fault secrecy (j)</td><td colspan="3">Level of technician&#x27;s security clearance (i)</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>0 (100)</td><td>1 (70)</td><td>2 (50)</td></tr><tr><td>2</td><td>-1 (40)</td><td>0 (100)</td><td>1 (80)</td></tr><tr><td>3</td><td>-2 (30)</td><td>-1 (50)</td><td>0 (100)</td></tr></table>

The rule is applied in two stages. (1) The location of the technician is checked and a temporary rating is given according to the distance from the site of the fault, as presented in Table 6. In the model, three areas were identified according to the work procedures of a large communications company that serves customers throughout the country. (2) A check is now carried out to see whether a technician handling a fault in the north of the country is supposed to be sent to service a fault in the south, or vice versa. If so, then a ‘‘penalty’’ of  5000 is inserted (instead of  1000). Although it is feasible to completely prevent such a situation, we chose not to do so, because despite the great distance, it should remain possible to assign a technician if he or she is the most suitable according to the other criteria. Such situations do certainly arise in practice: not infrequently, technicians in a company providing servicing are sent to distant places at great cost, in order that the company can meet its obligations to provide a good service. The use of a penalty rating is designed to ensure that only in extreme cases will a technician be assigned to service a fault very far away (such as hundreds of kilometers).

## Rule 8 (If (requester) = X, then suitability rating = Z).

A good assignment system must also take into account ‘‘unofficial’’ or ‘‘unwritten’’ conditions that are prevalent in an organization [4,6]. This rule gives expression to personal relationships and perhaps to problems existing between certain users and certain technicians (that is, how well the user and the technician ‘‘get along’’ together). Undoubtedly, this is not a main goal of the assignment system, and therefore, the weight of this rule must be lower than the weights of other rules. Table 7 presents suitability ratings applied in the system. Three levels of suitability are identified (as is customary in the field of organizational behavior in answers to the question, ‘‘Do you have good relations with technician i?’’ (very, moderate, not at all). It may be assumed that the help desk manager updates these data from time to time. Rule 9 (If (user status/position) = X, then suitability rating = Z).

Suitability ratings by relative distance—stage 1 of rules application

<table><tr><td rowspan="2">Location of fault</td><td colspan="3">Location of technician</td></tr><tr><td>North</td><td>Center</td><td>South</td></tr><tr><td>North</td><td>1000</td><td>0</td><td>-1000</td></tr><tr><td>Center</td><td>-1000</td><td>1000</td><td>-1000</td></tr><tr><td>South</td><td>-1000</td><td>0</td><td>1000</td></tr></table>

This rule also belongs to the field of organizational behavior. As a general rule, it is preferable to assign a technician in accordance with the status or position of the user. For example, assignment of a low-level technician to handle a problem of the CEO or Managing Director may be regarded as ‘‘intolerable’’ in a certain organization. At any rate, it can be seen in practice that when the managing director reports a fault, a most senior technician is immediately sent over, even if the fault in question is a simple one that a trainee could handle. Application of this rule resembles that of Rule 4, which is based on calculating the difference between the status of the user and that of the technician, and the accordance of a suitability score for each difference. For this reason, no illustrative table is presented here.

## 2.4.2. Weighting of assignment rules

In the assignment process, all the assignment rules are applied to the relevant technicians, but each rule will have its own appropriate weighting. The relative importance of each rule is likely to vary from organization to organization: in one case, the physical location of the technician may be paramount, while in another, the professional experience of the technician is more important, and so on. Therefore, the model enables the individual weighting of each rule to be redefined. It is not essential to predetermine the weighting of the various rules, hence, initially all rules may have equal weight.

Table 7  
Suitability ratings for technician – user relationships

<table><tr><td rowspan="2">User identity</td><td colspan="4">Technician</td></tr><tr><td>Tec-1</td><td>Tec-2</td><td>Tec-3</td><td>Tec-4</td></tr><tr><td>111</td><td>1</td><td>2</td><td>3</td><td>1</td></tr><tr><td>222</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>333</td><td>2</td><td>1</td><td>2</td><td>1</td></tr><tr><td>444</td><td>3</td><td>3</td><td>2</td><td>2</td></tr></table>

As a result of applying the rules to the data of the reported fault, each technician (from those who were selected in the initial stage as relevant) receives a final suitability rating—his or her weighted average rating of all the assignment rules, calculated by the formula:

$$
\mathrm{Rank} _ {j} = \frac {\sum W _ {i} \mathrm{Rule} _ {i j}}{\sum W _ {i}}
$$

where $W _ { 1 }$ is the weight of Rule i, $\mathrm { R u l e } _ { i j }$ is the score received by technician j for Rule i, and Rank<sub>j</sub> is technician $j ^ { \circ } \mathbf { s }$ overall rating.

## 2.5. Optimal assignment of technicians to faults

After the second (refined) phase of selection, a final suitability rating for each technician relevant to the reported fault is calculated. It would seem that all that remains is to assign the technician with the highest score. This would be the correct course of action where there is only one fault waiting to be handled. However, when it is necessary to assign technicians to service numerous faults, the assignment decision must take into account more than one fault at a time. For example, if two faults require attention, it may not actually be appropriate to assign to the first fault the most suitable technician, because he or she may turn out to be even more suited to service the second fault. Therefore, the model does not assign a technician to an individual fault, but selects the best technicians to handle a number of faults. This method of assignment has two advantages:

. A large planning horizon—in the assignment for a number of faults, a better and more reliable result is obtained because the overall benefit gained from the assignment process is greater than when technicians are assigned on the basis of individual faults.

. When there is a build-up of a number of faults, the non-assignment of a technician to more than one fault is ensured, so no pressure is exerted on any one technician. In this way, the distribution of faults among the technicians is better than the immediate assignment of a technician when a fault is reported.

In the current application, we decided to limit to three, the number of faults for which an assignment procedure is to be carried out. That is, the system ‘‘accumulates’’ three faults and then assigns the three most suitable technicians. The decision rule is that the sum of the scores of the three technicians assigned to service the three faults is maximal. Of course, it is best to assign the technician with the highest score relative to a particular fault to service that fault, but it is possible that the same technician will receive the best rating for more than one fault, something to be avoided. That is, the system chooses the best technician on condition that a different technician is assigned to each fault.

Below, we give an example of assignment in such a case: we shall assume that for three consecutive fault, the same three technicians were chosen as candidates to service the faults, as presented in Table 8. If each assignment was done on its own, and the only criterion was the maximal rating for each fault, the result would be: Fault 1—Technician C; Fault 2— Technician C; Fault 3—Technician B. That is, Technician C would be assigned to two faults, while Technician A would not be assigned at all.

In the system’s assignment technique, which tests three consecutive faults and assigns a technician to one of them, there are six possible assignments of the same three technicians, as shown in Table 9. As can be seen, the best grouping is that with the highest total score, 270 (shown in bold).

## 2.6. Application of model—the RFS system

The model is applied in a pilot system written in Visual Basic with the database management program MS-Access. The main aim of the development of the system was to make it possible to test simulated faults occurring in organizations and to evaluate the quality of the model in comparison with the quality of assignments achieved by experts. The system includes four principal modules, as required by the model described here, that is: (a) a model to analyze the user fault reports; (b) a model to carry out initial (statistical) selection; (c) a model to carry out secondary (rule-based) selection; (d) a model to carry out optimal assignment of a group of technicians to service a group of faults.

Table 8  
Technicians’ scores—example of final assignment

<table><tr><td>Fault number</td><td>Technician</td><td>Final score</td></tr><tr><td>1</td><td>A</td><td>70</td></tr><tr><td>1</td><td>B</td><td>60</td></tr><tr><td>1</td><td>C</td><td>90</td></tr><tr><td>2</td><td>A</td><td>90</td></tr><tr><td>2</td><td>B</td><td>60</td></tr><tr><td>2</td><td>C</td><td>100</td></tr><tr><td>3</td><td>A</td><td>80</td></tr><tr><td>3</td><td>B</td><td>90</td></tr><tr><td>3</td><td>C</td><td>80</td></tr></table>

Table 9  
Assignment possibilities of three technicians to three faults

<table><tr><td>Fault</td><td>Technician</td><td>Score</td><td>Fault</td><td>Technician</td><td>Score</td><td>Fault</td><td>Technician</td><td>Score</td><td>Total Score</td></tr><tr><td>1</td><td>1</td><td>70</td><td>2</td><td>2</td><td>60</td><td>3</td><td>3</td><td>80</td><td>210</td></tr><tr><td>1</td><td>1</td><td>70</td><td>2</td><td>3</td><td>100</td><td>3</td><td>2</td><td>90</td><td>260</td></tr><tr><td>2</td><td>1</td><td>90</td><td>1</td><td>2</td><td>60</td><td>3</td><td>3</td><td>80</td><td>230</td></tr><tr><td>2</td><td>1</td><td>90</td><td>1</td><td>3</td><td>90</td><td>3</td><td>2</td><td>90</td><td>270</td></tr><tr><td>3</td><td>1</td><td>80</td><td>2</td><td>2</td><td>60</td><td>1</td><td>3</td><td>90</td><td>230</td></tr><tr><td>3</td><td>1</td><td>80</td><td>2</td><td>3</td><td>100</td><td>1</td><td>2</td><td>60</td><td>240</td></tr></table>

## 3. Experiments to test the model

In this section, we describe experiments that were carried out using the system. These incorporated a series of faults for which the system assigned technicians, while experts, receiving the same data, performed the same task independently.

## 3.1. The faults

For the purpose of the experiments, the data on hundreds of faults, observed in real time, were collected, from which 350 representative faults were selected. We took care that the choice covered all types of fault (hardware, software and networks) and the wide range of parameters relevant to the various assignment rules (such as risk levels, user status, location of faults, etc.). In order to eliminate bias, we excluded faults, the correction of which is predetermined (e.g., if a report of a computer mouse failure is received, there is no attempt to repair it, and a new mouse is sent to the user).

## 3.2. The participating experts

During the development of the model and application of the system, the work of some 10 help desk managers—experts in leading Israeli companies in their field—was observed and studied. In the model and system testing phase, i.e., when the experiments were being carried out, three experts participated: the manager of a communications network in a large academic department of a university (Ben-Gurion University of the Negev); the help desk and communications network manager of a communications company (Motorola), and the networks maintenance manager in a national telephone company (Bezeq). Each of the three has vast experience and deals directly with assignment of technicians to service faults reported by users and customers.

## 3.3. Assignments by the experts

During the experiments, the experts were given data on the faults and the available technicians, and they were asked to make their assignments according to their best judgment. The technician data and their suitability scores for each subject were arranged in the form of tables: of course, the same data were fed into the RFS system. One after another, the fault reports were presented to each expert for them to make their assignments. During their work, the experts were asked to ‘‘think out loud’’ in order to enable their procedures, doubts and judgments, to be recorded. Two experiments were carried out with the experts.

. First experiment—in this experiment, all the assignment rules were applied.

. Second experiment—the fault location rule was omitted: during the observation and study of how the experts carried out their tasks (and before analysis of the results of the first experiment), it had already become clear to us that the principal—sometimes the only—consideration was the location of the technician in relation to the location of the fault. That is, even if the technician were not the most suited to service the fault, if he was in the vicinity of the fault, he would be assigned to deal with it. The purpose of the second experiment was to neutralize the question of location, in order to evaluate the quality of the system’s assignments in comparison to those of the experts, even when the location rule is irrelevant. In the second experiment, therefore, the experts were told that the organization operates in one building. This is not a hypothetical situation since there are organizations in which all the users are situated in one central location, such as a single building or campus. The second experiment included all the same faults as in the first, but it took place 5 months later, so it could be assumed that the experts would not remember the faults and the assignments they made the first time round.

## 4. Results and evaluation

## 4.1. Method of analysis

During the experiments with the experts, each of their assignments for each fault was recorded. Upon completion of each experiment, the average suitability rating of the technicians was calculated, as assigned to each fault by the experts. Averages were used in order to reduce to a minimum the influence of the differences between the experts. Afterwards, the system was run on the same fault and technician data, and the suitability rating of each assigned technician was recorded, as determined by the system. Finally, the experts’ average suitability ratings were compared to those of the system. Whether by the experts or the system, the suitability ratings were calculated for each of the rules, and accordingly, it was determined who performed the better assignments, the experts or the system. For example, let us take Rule 2 (sub-types of fault) and let us assume that a modem was reported as faulty. If the system assigned (in accordance with this rule) a technician with a rating of 80 (as shown in the table of ratings for this rule), and if the experts assigned a technician or technicians whose rating (or the average rating of the technicians selected) was 50, then it can be stated that the system ‘‘won’’.

In the various suitability rules, it is possible to identify various conditions that enable a determination of who ‘‘won’’ or ‘‘lost’’ (i.e., who performed a better or worse assignment). In some of the rules, one can distinguish only three types of result: ‘‘Win’’ for the system (i.e., a loss for the experts), a loss for the system, or equality. For some other rules, six types of result are identifiable for the system: ‘‘Absolute Win’’, ‘‘Relative Win’’, ‘‘Equality (draw)’’, ‘‘Relative Equality’’, ‘‘Relative Loss’’, and ‘‘Absolute Loss’’.

For Rules 1, 2, 3, 5 and 8, just the three types of result (as shown above) are distinguished: ‘‘Win’’ or ‘‘Loss’’ for the system, or ‘‘Equality’’. These results are determined by comparing the suitability ratings in the technicians’ profiles for each of the rules. An example was shown above in connection with Rule 2.

For Rules 4, 6, 7 and 9, the six types of result are distinguished, in accordance with the size of differences between the technicians’ ratings. Let us take as an example Rule 9 (user status/position): if, for a particular fault, the user’s status is 2, and the technician assigned by the system has a rating of 3, the difference is 1 (3  2). Now, if the experts assigned to the same fault a technician with a rating of 1, then the difference is  1 (1  2). Therefore, in this case, it can be said that the system achieved ‘‘Relative Win’’. On the basis of the differences between the required assignments and those carried out in practice, whether by the experts or the system, the six types of result are defined, as illustrated in Table 10. The table details, for each type of result, the possible differences between the system and expert assignments for each of the rules. There follow details of each of the six types of result.

. Absolute Win—this result satisfies conditions in which the system assignment is exact (i.e., the system assigned a technician with exactly the same rating as that of the fault), while the expert assignment is inexact (the expert made an assignment with different ratings for technician and fault). Conditions 1–4 in Table 10 fall within the ‘‘Absolute Win’’ result. As can be seen, the values of the differences for these conditions between the system and expert assignments are (  2, 0), (  1, 0), (1, 0) and (2, 0).

. Relative Win—this result satisfies the conditions in which the assignment carried out by the system is inexact but is better than that of the experts. Conditions 5 – 8 in the table fall within this result. The values of the differences for these conditions between the system and expert assignments are (2, 1), (2, 1), (1, 1) and (2, 1).

. Equality—this result satisfies the condition in which both the system and the experts make exact assignments, in which case the difference value is (0, 0), as in condition 9 of the table.

Table 11  
Table 10  
Possible differences in system and expert assignment

<table><tr><td>Type of result</td><td>Condition number</td><td>Expert difference</td><td>System difference</td></tr><tr><td rowspan="4">Absolute Win</td><td>1</td><td>-2</td><td>0</td></tr><tr><td>2</td><td>-1</td><td>0</td></tr><tr><td>3</td><td>1</td><td>0</td></tr><tr><td>4</td><td>2</td><td>0</td></tr><tr><td rowspan="4">Relative Win</td><td>5</td><td>-2</td><td>-1</td></tr><tr><td>6</td><td>-2</td><td>1</td></tr><tr><td>7</td><td>-1</td><td>1</td></tr><tr><td>8</td><td>2</td><td>1</td></tr><tr><td>Equality</td><td>9</td><td>0</td><td>0</td></tr><tr><td rowspan="4">Relative Equality</td><td>10</td><td>-2</td><td>-2</td></tr><tr><td>11</td><td>-1</td><td>-1</td></tr><tr><td>12</td><td>1</td><td>1</td></tr><tr><td>13</td><td>2</td><td>2</td></tr><tr><td rowspan="3">Relative Loss</td><td>14</td><td>0</td><td>1</td></tr><tr><td>15</td><td>0</td><td>2</td></tr><tr><td>16</td><td>1</td><td>2</td></tr><tr><td rowspan="7">Absolute Loss</td><td>17</td><td>-1</td><td>-2</td></tr><tr><td>18</td><td>1</td><td>-2</td></tr><tr><td>19</td><td>0</td><td>-2</td></tr><tr><td>20</td><td>2</td><td>-2</td></tr><tr><td>21</td><td>0</td><td>-1</td></tr><tr><td>22</td><td>1</td><td>-1</td></tr><tr><td>23</td><td>2</td><td>-1</td></tr></table>

. Relative Equality—this result satisfies the condition in which neither the system nor the experts make exact assignments according to requirements, but the size of the error is equal, as in conditions 10– 13 in the table. The values of the differences are (  2,  2), (  1,  1), (1, 1) and (2, 2).

. Relative Loss—this result satisfies the conditions in which the system assignments are poorer than those of the experts, but the system does not actually err, because it makes an over-assignment (that is, the assigned technician is over-qualified to service the fault), as in conditions 14–16 in the table. The difference values are (0, 1), (0, 2) and (1, 2).

. Absolute Loss—this result satisfies the conditions in which the expert assignments are better than those of the system, and, in addition, the technician assigned by the system does not meet the requirements, as in conditions 17 –23 in the table. The difference values are (  1,  2), (1,  2) (0,  2) (2,  2), (0,  1), (1,  1) and (2,  1).

It can therefore be determined for each fault and each rule who made a better assignment according to the three or six types of result described above. As a result, how many faults received results for each type and each rule can be calculated, and this allows conclusions to be reached about the quality of the assignments made by the system in comparison to those of the experts.

## 4.2. Comparison of results

About 350 faults were included in the experiments. In the first experiment, all the assignment rules were taken into account, while in the second experiment, Rule 7 (location) was omitted. Tables 11 and 12 present the results of the two experiments. The numbers in each table indicate the number of faults for each type of result for each rule. The value ‘‘irrelevant’’ indicates rules for which only three types of result were defined: ‘‘Win’’, ‘‘Equality’’, or ‘‘Loss’’.

Consolidated results of experiment 1

<table><tr><td rowspan="2">Rules</td><td colspan="6">Results</td></tr><tr><td>Absolute Win</td><td>Relative Win</td><td>Equality</td><td>Relative Equality</td><td>Relative Loss</td><td>Absolute Loss</td></tr><tr><td>Type of fault (1)</td><td>71</td><td>irrelevant</td><td>32</td><td>irrelevant</td><td>irrelevant</td><td>48</td></tr><tr><td>Subject of fault (2)</td><td>71</td><td>irrelevant</td><td>32</td><td>irrelevant</td><td>irrelevant</td><td>48</td></tr><tr><td>Cost of fault (3)</td><td>75</td><td>irrelevant</td><td>33</td><td>irrelevant</td><td>irrelevant</td><td>43</td></tr><tr><td>Risk level (4)</td><td>48</td><td>14</td><td>20</td><td>26</td><td>22</td><td>20</td></tr><tr><td>Full/Part time (5)</td><td>34</td><td>irrelevant</td><td>84</td><td>irrelevant</td><td>irrelevant</td><td>33</td></tr><tr><td>Security level (6)</td><td>33</td><td>18</td><td>24</td><td>43</td><td>23</td><td>11</td></tr><tr><td>Location (7)</td><td>45</td><td>15</td><td>45</td><td>24</td><td>7</td><td>15</td></tr><tr><td>User identity (8)</td><td>72</td><td>irrelevant</td><td>36</td><td>irrelevant</td><td>irrelevant</td><td>43</td></tr><tr><td>User status (9)</td><td>28</td><td>12</td><td>24</td><td>47</td><td>29</td><td>11</td></tr></table>

Table 12  
Consolidated results of experiment 2

<table><tr><td rowspan="2">Rules</td><td colspan="6">Results</td></tr><tr><td>Absolute Win</td><td>Relative Win</td><td>Equality</td><td>Relative Equality</td><td>Relative Loss</td><td>Absolute Loss</td></tr><tr><td>Type of fault (1)</td><td>71</td><td>irrelevant</td><td>33</td><td>irrelevant</td><td>irrelevant</td><td>46</td></tr><tr><td>Subject of fault (2)</td><td>71</td><td>irrelevant</td><td>33</td><td>irrelevant</td><td>irrelevant</td><td>46</td></tr><tr><td>Cost of fault (3)</td><td>80</td><td>irrelevant</td><td>28</td><td>irrelevant</td><td>irrelevant</td><td>42</td></tr><tr><td>Risk level (4)</td><td>62</td><td>16</td><td>25</td><td>20</td><td>17</td><td>10</td></tr><tr><td>Full/Part time (5)</td><td>44</td><td>irrelevant</td><td>79</td><td>irrelevant</td><td>irrelevant</td><td>27</td></tr><tr><td>Security level (6)</td><td>41</td><td>17</td><td>18</td><td>35</td><td>20</td><td>19</td></tr><tr><td>User identity (8)</td><td>73</td><td>irrelevant</td><td>36</td><td>irrelevant</td><td>irrelevant</td><td>41</td></tr><tr><td>User status (9)</td><td>48</td><td>14</td><td>31</td><td>20</td><td>29</td><td>8</td></tr></table>

Table 13 summarizes the results of the experiments in percentages. The calculation is the mean of the results of the two experiments in relation to the number of faults included (Rule 7 is not included in experiment 2). It is worth noting that the weighting of the rules was kept equal, despite the option that enables differential weightings to be accorded each rule. The reason for this was that the introduction of such differentials would have made it impossible to detect any significant changing trend, which is possible when all the rules have the same weighting.

## 4.3. Evaluation of results

After consolidating and weighting the experimental results, the final results are obtained, as presented in

Table 14. The results are summarized according to five measures:

(1) Percentage of faults for which the system gave better results than those of the experts— includes ‘‘Absolute Win’’ and ‘‘Relative Win’’.

(2) Percentage of faults for which the system gave better or equal results than those of the experts—includes ‘‘Absolute Win’’, ‘‘Relative Win’’, ‘‘Equality’’, and ‘‘Relative Equality’’.

(3) Percentage of faults for which the system gave exactly the right results to handle the fault— includes ‘‘Absolute Win’’ and ‘‘Equality’’.

(4) Percentage of faults for which the system ‘‘lost’’, that is, the experts gave better results than the system—includes ‘‘Relative Loss’’ and ‘‘ Absolute Loss’’.

Table 13  
Consolidated results of the experiments, in percents

<table><tr><td rowspan="4">Rule</td><td colspan="12">Results</td></tr><tr><td colspan="2">Absolute Win</td><td colspan="2">Relative Win</td><td colspan="2">Equality</td><td colspan="2">Relative Equality</td><td colspan="2">Relative Loss</td><td colspan="2">Absolute Loss</td></tr><tr><td colspan="12">Experiment</td></tr><tr><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td>Type of fault (1)</td><td>47.3</td><td>47.3</td><td>-</td><td>-</td><td>21.0</td><td>22.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>31.7</td><td>30.7</td></tr><tr><td>Subject of fault (2)</td><td>47.3</td><td>47.3</td><td>-</td><td>-</td><td>21.0</td><td>22.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>31.7</td><td>30.7</td></tr><tr><td>Cost of fault (3)</td><td>49.7</td><td>53.3</td><td>-</td><td>-</td><td>21.7</td><td>18.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>28.7</td><td>28.0</td></tr><tr><td>Risk level (4)</td><td>32.0</td><td>41.3</td><td>9.3</td><td>10.7</td><td>13.3</td><td>16.7</td><td>17.3</td><td>13.3</td><td>14.7</td><td>11.3</td><td>13.3</td><td>6.7</td></tr><tr><td>Full/Part time (5)</td><td>22.3</td><td>29.3</td><td></td><td>-</td><td>56.0</td><td>52.7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>21.7</td><td>18.0</td></tr><tr><td>Security level (6)</td><td>21.7</td><td>27.3</td><td>11.7</td><td>11.3</td><td>16.0</td><td>12.0</td><td>28.3</td><td>23.3</td><td>15.3</td><td>13.3</td><td>7.0</td><td>12.7</td></tr><tr><td>Location (7)</td><td>29.8</td><td>-</td><td>9.9</td><td>-</td><td>29.8</td><td>-</td><td>15.9</td><td>-</td><td>4.6</td><td>-</td><td>9.9</td><td>-</td></tr><tr><td>User identity (8)</td><td>48.0</td><td>48.7</td><td></td><td>-</td><td>23.7</td><td>24.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>28.3</td><td>27.3</td></tr><tr><td>User status (9)</td><td>18.3</td><td>32.0</td><td>8.0</td><td>9.3</td><td>15.7</td><td>20.7</td><td>31.3</td><td>13.3</td><td>19.3</td><td>19.3</td><td>7.3</td><td>5.3</td></tr><tr><td>Average</td><td>35.2</td><td>40.8</td><td>9.7</td><td>10.4</td><td>24.2</td><td>23.6</td><td>23.2</td><td>16.7</td><td>13.5</td><td>14.7</td><td>20.0</td><td>19.9</td></tr><tr><td>Average of two experiments</td><td>38.0</td><td></td><td>10.1</td><td></td><td>23.9</td><td></td><td>20.0</td><td></td><td>14.1</td><td></td><td>20.0</td><td></td></tr></table>

Table 14  
Final consolidated results

<table><tr><td>Measure of success</td><td>Conditions included</td><td>Value (%)</td></tr><tr><td>(1) Percentage of faults for which the system gave better results than those of experts</td><td>“Absolute Win” and “Relative Win”</td><td>48.1</td></tr><tr><td>(2) Percentage of faults for which the system gave better or equal results than those of experts (not worse than the experts)</td><td>“Absolute Win”, “Relative Win”, “Equality” and “Relative Equality”</td><td>92.0</td></tr><tr><td>(3) Percentage of faults for which the system gave exactly the right results to handle the fault</td><td>“Absolute Win” and “Equality”</td><td>61.9</td></tr><tr><td>(4) Percentage of faults for which the system lost, i.e., experts gave better results than the system</td><td>“Relative Loss” and “Absolute Loss”</td><td>8.0</td></tr><tr><td>(5) Percentage of faults for which the system gave accurate results, i.e., under-qualified technicians was not assigned to faults</td><td>Percentage of faults for which the difference between the system assignment and the required ≥0</td><td>81.7</td></tr></table>

(5) Percentage of faults for which the system gave accurate results, that is, under-qualified technicians were not assigned to a fault—includes conditions in which the difference between the system assignment and that required $\geq 0$

It can be seen, therefore, that for 48% of the faults, the system made better assignments than those of the experts, and in 92% of the cases, the system achieved equal or better results than did the experts. That is to say, for only 8% of the faults, the experts did better than the system. These results substantiate the validity of the model and the system.

## 5. Conclusions and topics for further research

In this study, a model for assigning technicians to service faults was presented. The procedure is carried out in several stages: (a) analysis of the fault report and its translation into a vector of standardized keywords; (b) carrying out a preliminary selection of a group of the most suitable technicians, on the basis of a statistical correlation between the fault report vector and vectors representing each of the technicians; (c) carrying out a second (refined) selection process according to assignment rules and suitability ratings for each of the above group of technicians; and (d) a final assignment of the most suitable technicians to handle a set of accumulated faults.

The model was implemented in an assignment system and was tested in the framework of experiments, which included the assignment of technicians to service some 350 typical faults. The performance of the system was compared to that of experts in the field, who carried out assignment of technicians to the same faults.

Analysis of the results of the system’s assignments, in comparison to those of the experts, shows that the quality of assignment by the system according to the criterion ‘‘system assignment better than or equal to that of the experts’’ is high, reaching 92% of the reported faults (while only in 8% of the cases did the experts achieve better results). In addition, we saw that the percentage of faults for which an exact assignment was made (according to requirements) or even better (technician over-qualified but not underqualified) reached 81.7%. This result was achieved when each assignment by the system was tested according to requirements, by the fault characteristics, without comparison with the experts.

As we have seen, in order to make a correct assignment of a technician to service a fault, the administrators must take many considerations into account, particularly when they are under pressure. As a result, they often rely on just the geographical location of the technician. The advantage of the model is that all the relevant suitability rules can be taken into account, thus leading to optimal decision-making. Another advantage is the speed of assignment: system assignment is clearly faster than that done by a person, however expert. In the framework of the experiments, it was found that the assignment time by the system took about 2 s, while the experts took between 60 and 90 s on average. This advantage becomes significant when many (or even hundreds) of daily faults must be handled. Moreover, the system does not become ‘‘fatigued’’, feel under pressure, or look for ‘‘shortcuts’’—unlike a human, nor does it go on vacation, leaving the work for a subordinate to handle. In addition, use of the system obviously frees the help desk manager to deal with other business. A more appropriate assignment of technicians not only improves customer/user service but helps to lower the organization’s technician costs, since it becomes unnecessary to employ technicians ‘‘who know how to do everything’’ and who are therefore expensive; it is sometimes possible to employ some junior technicians who are paid less and who can be assigned to faults suited to their abilities.

Turning to the disadvantages of the system, we should note the difficulties in defining the suitability rules. The process of identifying the rules is lengthy and necessitates interviews with experts and observation of their work. Any organization wishing to apply the model will need to adapt the rules to its particular conditions, or to identify and define some specific rules. As can be seen, our rules are not exactly defined; in particular, there is no guarantee that the suitability ratings determined for each technician for each rule are accurate. Much practical experience is needed in order to adjust and ratify them. Moreover, a mechanism is required to update the technicians’ ratings (for example, due to gaining experience). This requires the organization to operate a system of ratings revision for each of the suitability rules. A further problem with these rules is the determination of their relative weighting importance: in the present work, we noted that they can be weighted, but this topic has not been investigated. In future research, there is room for testing such weighting of the rules and how changing the weightings affect the quality of assignment.

Another subject for further research is maintenance of the assignment system: it needs regular periodic updating, such us a review of the standardized terms and key words in the lookup tables. A maintenance procedure must be devised that is not merely dependent on the relevant manager’s initiative, but which also learns new terms from the users’ fault reports.

One of the requisite improvements in the system, with which we did not deal, is in the field of identifying the cause of the fault. By this, we mean that when a fault report is received, the system should carry out a number of tests to try to detect the cause(s) of the fault. For example, a deductive statistical procedure could be used, by means of which it would be possible to deduce probable causes from a database of previous similar faults and reports. As a result, it would be possible to advise the technician of previous solutions that had proven successful. For this purpose, a log could be maintained at each user station, in which details of the hardware, software and network would be recorded, as well as, of course, a history of relevant faults and servicing.

When a fault report is received from the station, the system can compare it to the database and use it to help identify likely causes, even before a technician has been assigned. The station log would also enable the system to identify ‘‘problematic users/stations’’. For example, if the system identifies recurrent fault reports, it might recommend that, instead of sending a technician every time to service the fault, an instructor be sent to teach the user how to make best use of his or her computer set up. The use of such logs would also enable future faults to be anticipated. For example, it would be possible to learn the expected lifetime of a particular item, and thus, to predict or prevent faults by preventative maintenance (e.g., by replacement of a part prior to its failure). The existence of historical records would allow data mining, both for discovering and identifying faults, and for assigning technicians on the basis of historic data. For example, investigating the historical data might discover that a specific technician handles problems involving the e-mail/ Internet server, quickly and efficiently. Thus, when such a fault arises, it is worth assigning that particular technician to it.

## References

[1] M. Amini, M. Racer, A hybrid heuristic for the generalized assignment problem, European Journal of Operational Research 87 (1995) 343– 348.

[2] D.R. Armstrong, J. Zhiying, On solving a variation of the assignment problem, European Journal of Operational Research 87 (1995) 142 – 147.

[3] J.G. Blackstone, D.T. Phillips, G.L. Hoggy, A state of the art survey of dispatching rules for manufacturing job shop operations, International Journal of Production Research 20 (1) (1982) 27– 45.

[4] E. Castillo, E. Alvarez, Expert Systems: Uncertainty and Learning, Elsevier, London, 1991.

[5] R. Davis, B.G. Buchanan, Meta level knowledge—overview and applications, Proceedings of the 5th International Joint Conference on Artificial Intelligence, William Kaufmann, Cambridge, MA, 1977, pp. 920 – 927.

[6] M. Donald, Introductory Readings in Expert Systems, Gordon & Breach, New York, 1982.

[7] J. Finlay, J. Jones, Neural networks for system fault management, Proceedings of Workshop on Neural Networks: Techniques and Applications, University of Liverpool, Ellis Horwood, 1993, pp. 287–299.

[8] W. Grossmann, G. Guariso, H. Werthner, A min cost flow solution for dynamic assignment problems in networks with storage devices, Management Science 41 (1) (1995) 83 – 93.

[9] J.R. Quinlan, Fundamentals of the Knowledge Engineering Problem, University of Sydney Press, Sydney, 1982.

[10] E. Rich, Artificial Intelligence, McGraw-Hill, New York, 1983.

[11] G. Salton, W. Mcgill, Introduction to Modern Information Retrieval, McGraw-Hill, New York, 1983.

[12] S.M. Weiss, C.A. Kulikowski, A Practical Guide to Designing Expert Systems, Kowman and Allanheld Publishers, London, 1984.

![](/api/attachments/QW9BAEEM/fulltext/images/f1234f13972972caf592b9f0a82391d4f599f8d38f2648eebe958b6b41e71904.jpg)  
Avinoam Lazarov received his BSc and MSc degrees in Industrial Engineering and Management, with majors in Information Systems from Ben-Gurion University. This paper is a product of his thesis, which was supervised by Prof. Shoval. Mr. Lazarov works for the Open University of Israel, where he is the coordinator of Information Systems Analysis and Design courses, and heads the section of Organization and Work Methods.

![](/api/attachments/QW9BAEEM/fulltext/images/0aa350c7df3c0c7d754f1dcc6eddf5127b1ba36a6ae7640ff343151a67e561a3.jpg)

Dr. Peretz Shoval is Professor of Information Systems, founder and head of the Department of Information Systems Engineering at Ben-Gurion University, Israel. Dr. Shoval received his BA degree in Economics and MSc degree in Information Systems from Tel-Aviv University, and his PhD degree in Information Systems from the University of Pittsburgh, where he specialized in expert systems for information retrieval. Prof.

Shoval’s research interests include information systems analysis and design methods, data modeling and database design, and information retrieval and filtering. He has authored over a hundred technical papers that appeared in refereed journals and conferences. Shoval has developed various methodologies and tools for systems analysis and design, and for conceptual and logical database design.
